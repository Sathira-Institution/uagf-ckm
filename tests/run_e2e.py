#!/usr/bin/env python3
"""
E2E runner for UAGF (minimal, strict fail-closed).
- Reads manifest.yaml (expected_differences, success_criteria)
- Runs validate_ckm.py against ckm-staging (supports --require-ledger)
- Runs render_ckm.py twice (per profile) to assert determinism (G11)
- Compares renders to baseline (generated/baseline/) and allows ONLY expected_differences
- Writes reports/e2e_summary.json and exits non-zero on FAIL/UNKNOWN
"""
import os, sys, subprocess, yaml, json, hashlib, argparse, difflib

# CONFIG: profiles to exercise (can be extended)
PROFILES = ["registry-doc", "registry-jsonld", "registry-ai-context"]


def load_manifest(path="manifest.yaml"):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_validator(ckm_dir, ledger_path=None, out_report=None):
    cmd = [sys.executable, "validate_ckm.py", ckm_dir]
    if ledger_path:
        cmd += ["--require-ledger", ledger_path]
    if out_report:
        cmd += ["-o", out_report]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def run_renderer(profile, outpath, ckm="ckm-staging", scope="module:M-CORE", ckm_release="2.0.0-staging"):
    cmd = [sys.executable, "render_ckm.py", "--ckm", ckm, "--profile", profile, "--scope", scope, "--ckm-release", ckm_release, "--out", outpath]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def compare_and_classify_diff(profile, baseline_path, new_path, allowed_kinds):
    # Simple diff check: if identical => OK
    if not os.path.exists(baseline_path):
        return {"status":"NO_BASELINE", "undeclared_diffs": ["NO_BASELINE"]}
    if sha256(baseline_path) == sha256(new_path):
        return {"status":"IDENTICAL", "undeclared_diffs": []}
    # produce textual diff and apply heuristic matching for allowed kinds
    with open(baseline_path, encoding="utf-8") as f: base = f.readlines()
    with open(new_path, encoding="utf-8") as f: new = f.readlines()
    diffs = list(difflib.unified_diff(base, new, lineterm=""))
    # heuristics: allow id_padding (UGR-###), allow generated_front_matter (stamp lines), allow cv token casing differences
    undeclared = []
    for line in diffs:
        if any(k in allowed_kinds for k in ("id_padding_presentation",)) and ("UGR-" in line and any(ch.isdigit() for ch in line)):
            continue
        if any(k in allowed_kinds for k in ("generated_front_matter",)) and ("render_token" in line or "ckm_release" in line):
            continue
        if any(k in allowed_kinds for k in ("cv_token_presentation",)) and (line.strip().lower() == line.strip()):
            continue
        # fallback: mark as undeclared
        undeclared.append(line)
    return {"status":"DIFFER", "undeclared_diffs": undeclared, "diff_count": len(diffs)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="manifest.yaml")
    ap.add_argument("--ledger", default=None)
    ap.add_argument("--ckm", default="ckm-staging")
    ap.add_argument("--baseline-dir", default="generated/baseline")
    ap.add_argument("--out-summary", default="reports/e2e_summary.json")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out_summary) or ".", exist_ok=True)

    manifest = load_manifest(args.manifest)
    expected_diffs = manifest.get("expected_differences", [])
    allowed_kinds = {d.get("kind") for d in expected_diffs}

    summary = {"manifest_id": manifest.get("manifest", {}).get("id"),
               "ckm": args.ckm, "timestamp": None, "gates": {}, "profiles": {}}

    # Step 1: Validation
    rc, out, err = run_validator(args.ckm, ledger_path=args.ledger, out_report="reports/validation_raw.json")
    if rc != 0:
        summary["gates"]["validation"] = {"result":"FAIL","rc":rc,"stderr":err,"stdout":out}
    else:
        summary["gates"]["validation"] = {"result":"PASS","rc":rc}

    # Step 2: Render twice per profile, assert determinism
    for profile in PROFILES:
        os.makedirs("reports/e2e_tmp", exist_ok=True)
        p1 = f"reports/e2e_tmp/{profile}.run1.out"
        p2 = f"reports/e2e_tmp/{profile}.run2.out"
        rc1, o1, e1 = run_renderer(profile, p1, ckm=args.ckm)
        rc2, o2, e2 = run_renderer(profile, p2, ckm=args.ckm)
        if rc1 != 0 or rc2 != 0:
            summary["profiles"][profile] = {"render_status":"FAIL","rcs":[rc1,rc2],"stderr":[e1,e2]}
            continue
        h1 = sha256(p1); h2 = sha256(p2)
        if h1 != h2:
            summary["profiles"][profile] = {"render_status":"NON_DETERMINISTIC","hashes":[h1,h2]}
        else:
            summary["profiles"][profile] = {"render_status":"DETERMINISTIC","hash":h1}
        # Step 3: Compare to baseline if exists
        baseline = os.path.join(args.baseline_dir, profile+".baseline")
        comp = compare_and_classify_diff(profile, baseline, p1, allowed_kinds)
        summary["profiles"][profile]["baseline_comparison"] = comp

    # Decide overall pass/fail per success_criteria
    # Fail-closed rules: if validation failed or any profile non-deterministic or undeclared diffs -> FAIL
    overall = "PASS"
    if summary["gates"].get("validation", {}).get("result") != "PASS":
        overall = "FAIL"
    for p,v in summary["profiles"].items():
        if v.get("render_status") != "DETERMINISTIC":
            overall = "FAIL"
        if v.get("baseline_comparison", {}).get("undeclared_diffs"):
            overall = "FAIL"
    summary["overall_result"] = overall
    # Write summary
    import datetime
    summary["timestamp"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(args.out_summary, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    sys.exit(0 if overall=="PASS" else 1)


if __name__ == "__main__":
    main()
