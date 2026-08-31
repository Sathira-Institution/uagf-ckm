#!/usr/bin/env python3
"""
E2E runner for UAGF (strict fail-closed, merged-view validation).

Semantics (see docs/validation-merge-semantics.md):
- ckm-staging is an INCREMENTAL OVERLAY over the release snapshot (ckm-2.0.0-alpha).
- Validation and rendering run against a TEMPORARY MERGED VIEW:
    merged = release_base + staging overlay (staging wins on conflicts)
- Non-destructive: original directories are never modified.
- Baselines are created only when merged validation PASSes.
- Dangling references (V-1) are recorded as [CONFLICT] for Founder routing (D-03).
"""
import os, sys, subprocess, yaml, json, hashlib, argparse, tempfile, shutil, difflib, datetime, re
from pathlib import Path

PROFILES = ["registry-doc", "registry-jsonld", "registry-ai-context"]

def load_manifest(path="manifest.yaml"):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def copy_tree_into(src, dst):
    src_p, dst_p = Path(src), Path(dst)
    if not src_p.exists():
        return
    for root, dirs, files in os.walk(src_p):
        rel = os.path.relpath(root, src_p)
        target = dst_p if rel == "." else dst_p.joinpath(rel)
        target.mkdir(parents=True, exist_ok=True)
        for fn in files:
            shutil.copy2(Path(root) / fn, target / fn)

def build_merged_view(release_dir, staging_dir):
    tmp = tempfile.mkdtemp(prefix="uagf-merged-")
    if os.path.isdir(release_dir):
        copy_tree_into(release_dir, tmp)
    if os.path.isdir(staging_dir):
        copy_tree_into(staging_dir, tmp)
    return tmp

def run_validator(ckm_dir, ledger_path=None, out_report=None):
    cmd = [sys.executable, "validate_ckm.py", ckm_dir]
    if ledger_path:
        cmd += ["--require-ledger", ledger_path]
    if out_report:
        cmd += ["-o", out_report]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr

def run_renderer(profile, outpath, ckm, scope="module:M-CORE", ckm_release="2.0.0-merged"):
    cmd = [sys.executable, "render_ckm.py", "--ckm", ckm, "--profile", profile,
           "--scope", scope, "--ckm-release", ckm_release, "--out", outpath]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def _normalized_lines(text, allowed_kinds):
    """Apply declared normalizations (XD-*) symmetrically BEFORE diffing."""
    out = []
    for raw in text.splitlines():
        line = raw
        if "id_padding_presentation" in allowed_kinds:
            line = re.sub(r"\bUGR-(\d{1,4})\b",
                          lambda m: "UGR-%04d" % int(m.group(1)), line)
        if "generated_front_matter" in allowed_kinds:
            if re.search(r"\b(render_token|ckm_release|rendered_at)\b\s*[:=]", line):
                continue
        if "cv_token_presentation" in allowed_kinds:
            s = line.strip()
            if re.fullmatch(r"[-A-Za-z0-9_]+(\s*,\s*[-A-Za-z0-9_]+)*", s):
                line = line.lower().replace("_", "-")
        out.append(line)
    return out

def compare_and_classify_diff(profile, baseline_path, new_path, allowed_kinds):
    if not os.path.exists(baseline_path):
        return {"status": "NO_BASELINE", "undeclared_diffs": []}
    if sha256(baseline_path) == sha256(new_path):
        return {"status": "IDENTICAL", "undeclared_diffs": []}
    with open(baseline_path, encoding="utf-8") as f: base = f.read()
    with open(new_path, encoding="utf-8") as f: new = f.read()
    base_n = _normalized_lines(base, allowed_kinds)
    new_n  = _normalized_lines(new, allowed_kinds)
    if base_n == new_n:
        return {"status": "DIFFER_DECLARED_ONLY", "undeclared_diffs": [],
                "diff_count": 0, "applied_kinds": sorted(allowed_kinds)}
    diffs = list(difflib.unified_diff(base_n, new_n, lineterm=""))
    undeclared = [ln for ln in diffs
                  if ln[:1] in ("+", "-") and ln[:3] not in ("+++", "---")]
    return {"status": "DIFFER", "undeclared_diffs": undeclared,
            "diff_count": len(undeclared), "applied_kinds": sorted(allowed_kinds)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="manifest.yaml")
    ap.add_argument("--ledger", default=None)
    ap.add_argument("--ckm", default="ckm-staging")
    ap.add_argument("--release-base", default=os.environ.get("UAGF_RELEASE_DIR", "ckm-2.0.0-alpha"))
    ap.add_argument("--baseline-dir", default="generated/baseline")
    ap.add_argument("--out-summary", default="reports/e2e_summary.json")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out_summary) or ".", exist_ok=True)
    manifest = load_manifest(args.manifest)
    expected_diffs = manifest.get("expected_differences", [])
    allowed_kinds = {d.get("kind") for d in expected_diffs}

    summary = {"manifest_id": manifest.get("manifest", {}).get("id"),
               "ckm": args.ckm,
               "release_base": args.release_base,
               "validation_scope": "merged(release+staging)",
               "timestamp": None, "gates": {}, "profiles": {},
               "pending_actions": []}

    merged_dir = build_merged_view(args.release_base, args.ckm)
    try:
        # Step 1: validation on MERGED view
        rc, out, err = run_validator(merged_dir, ledger_path=args.ledger,
                                     out_report="reports/merged_validation.json")
        validation_pass = (rc == 0)
        summary["gates"]["validation"] = {
            "result": "PASS" if validation_pass else "FAIL",
            "rc": rc, "scope": "merged"}
        if not validation_pass:
            summary["gates"]["validation"]["stderr"] = err
            summary["gates"]["validation"]["stdout"] = out

        # Dangling refs (V-1) -> [CONFLICT] dispositions for Founder (D-03)
        conflict_count = err.count("[V-1]")
        if conflict_count:
            summary["gates"]["MERGED_DANGLING_REFS"] = {
                "result": "FAIL",
                "detail": f"{conflict_count} dangling refs (V-1) — record [CONFLICT], route to Founder (D-03)"}

        # Step 2: determinism (G11) — render twice from merged view
        for profile in PROFILES:
            os.makedirs("reports/e2e_tmp", exist_ok=True)
            p1 = f"reports/e2e_tmp/{profile}.run1.out"
            p2 = f"reports/e2e_tmp/{profile}.run2.out"
            rc1, o1, e1 = run_renderer(profile, p1, ckm=merged_dir)
            rc2, o2, e2 = run_renderer(profile, p2, ckm=merged_dir)
            if rc1 != 0 or rc2 != 0:
                summary["profiles"][profile] = {"render_status": "FAIL", "rcs": [rc1, rc2], "stderr": [e1, e2]}
                continue
            h1, h2 = sha256(p1), sha256(p2)
            entry = {"render_status": "DETERMINISTIC" if h1 == h2 else "NON_DETERMINISTIC", "hash": h1}

            # Step 3: baseline compare, or create ONLY if validation passed
            baseline = os.path.join(args.baseline_dir, profile + ".baseline")
            if not os.path.exists(baseline):
                if validation_pass and h1 == h2:
                    os.makedirs(args.baseline_dir, exist_ok=True)
                    shutil.copy2(p1, baseline)
                    shutil.copy2(p1, os.path.join("reports", f"{profile}.baseline"))
                    entry["baseline_comparison"] = {"status": "BASELINE_CREATED", "path": baseline}
                else:
                    entry["baseline_comparison"] = {"status": "BASELINE_PENDING"}
                    summary["pending_actions"].append(f"commit baseline for {profile} after validation PASS")
            else:
                comp = compare_and_classify_diff(profile, baseline, p1, allowed_kinds)
                entry["baseline_comparison"] = comp

            summary["profiles"][profile] = entry

        # Overall (fail-closed)
        overall = "PASS"
        if not validation_pass:
            overall = "FAIL"
        if conflict_count:
            overall = "FAIL"
        for p, v in summary["profiles"].items():
            if v.get("render_status") != "DETERMINISTIC":
                overall = "FAIL"
            if v.get("baseline_comparison", {}).get("undeclared_diffs"):
                overall = "FAIL"
        summary["overall_result"] = overall
        summary["timestamp"] = datetime.datetime.now(datetime.timezone.utc).isoformat()

        with open(args.out_summary, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        sys.exit(0 if overall == "PASS" else 1)
    finally:
        shutil.rmtree(merged_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
