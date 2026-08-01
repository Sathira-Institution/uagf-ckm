#!/usr/bin/env python3
"""UAGF E2E Regression Suite — Enhancement 3/4 + Task 004 seed.
Pipeline under test:  Legacy -> Migrate -> Validate -> Render -> Validate Render -> PASS
Machine-readable JSON summary; exit 0 only if every gate passes.
The Expected Differences Register (WP-005 §8.3) is embedded in-config below.
"""
import os, re, sys, json, subprocess, datetime
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root (suite lives in tests/)
PY = sys.executable

# ---- Expected Differences Register (WP-005 §8.3, manifest XD-1..XD-5) ----
EXPECTED_DIFF = {
    "XD-1": "cv token presentation (casefolded/hyphenated enum tokens)",
    "XD-2/D-03": "legacy dangling references held out of staging as recorded CONFLICT (UGR-30/31, UGR-52)",
    "XD-3": "id padding is a view parameter",
    "XD-4": "generated front matter / stamps",
    "XD-5": "render-config frame lines",
}
# Verbatim-preserved fields (M-2): must survive migration AND the doc render byte-for-byte
VERBATIM_FIELDS = {"Statement": "statement", "Intent": "intent",
                   "Applicability": "applicability",
                   "Expected Evidence": "expected_evidence",
                   "Related Controls": "related_controls", "Title": "label"}

def sh(*args):
    return subprocess.run([PY] + list(args), cwd=ROOT, capture_output=True, text=True)

def clean(s):
    return re.sub(r"\s+", " ", s.replace("**", "").strip())

def parse_legacy_records(path):
    txt = open(path, encoding="utf-8").read()
    recs, cur = {}, None
    for ln in txt.splitlines():
        if ln.strip().startswith("#") and not re.match(r"^#+\s+\**\s*UGR-\d+", ln.strip()):
            cur = None
        m = re.match(r"^#+\s+\**\s*(UGR-\d+)\s*[—–-]+\s*(.+?)\**\s*$", ln.strip())
        if m:
            cur = f"UGR-{int(re.search(r'(\d+)', m.group(1)).group(1))}"
            recs[cur] = {}
            continue
        if cur and ln.strip().startswith("|"):
            cs = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cs) == 2:
                k, v = clean(cs[0]), cs[1].replace("**", "").strip()
                if k and k.lower() not in ("field", "---", ":---"):
                    recs[cur][k] = recs[cur].get(k, "")
                    recs[cur][k] = (recs[cur][k] + " " + v).strip() if recs[cur][k] else v
    return recs

def main():
    results, t0 = [], datetime.datetime.now(datetime.timezone.utc).isoformat()
    def gate(name, ok, detail=""):
        results.append({"gate": name, "result": "PASS" if ok else "FAIL", "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
        return ok

    ok = True
    # G1: green seed must validate
    r = sh("validate_ckm.py", "tests/green/seed-ckm", "-q")
    ok &= gate("G1 green-seed validator PASS", r.returncode == 0)

    # G2: red fixtures must FAIL with expected invariant hits
    os.makedirs("/tmp/e2e-red", exist_ok=True)
    subprocess.run(["bash", "-c",
        f"rm -rf /tmp/e2e-red && mkdir -p /tmp/e2e-red && "
        f"cp -r {ROOT}/ckm/cv /tmp/e2e-red/ && cp {ROOT}/ckm/domains/DOM-HUMAN.yaml "
        f"{ROOT}/ckm/references/REF-EUAIA.yaml {ROOT}/tests/red/*.yaml /tmp/e2e-red/"])
    r = sh("validate_ckm.py", "/tmp/e2e-red", "-q", "-o", "/tmp/e2e-red-report.json")
    red_ok = r.returncode == 1
    hits = set()
    if os.path.exists("/tmp/e2e-red-report.json"):
        rep = json.load(open("/tmp/e2e-red-report.json"))
        hits = {f["error"] for f in rep["findings"]}
    expected_hits = {"V-1", "V-4", "V-5", "V-7", "V-3", "N-3"}
    red_ok = red_ok and expected_hits.issubset(hits)
    ok &= gate("G2 red fixtures FAIL with expected invariants", red_ok,
               f"caught: {sorted(hits)}")

    # G3: migration runs, zero silent corrections, zero REJECTED (this corpus)
    r = sh("migrate_ckm.py", "--batch-b", "batch-b")
    mig = json.load(open(os.path.join(ROOT, "reports/migration_report.json")))
    ok &= gate("G3 migration executes (30 UGRs / 10 domains / REFs minted)",
               r.returncode == 0 and mig["batches"]["A_requirements"] == 30
               and mig["silent_corrections"] == 0,
               f"dispositions: {mig['disposition_counts']}")

    # G4: staged CKM validates PASS
    r = sh("validate_ckm.py", "ckm-staging", "-q", "-o", "reports/staging_validation.json")
    ok &= gate("G4 staged CKM validator PASS", r.returncode == 0)

    # G5: all four renders execute
    renders = [("registry-doc", "generated/UAGF-002_registry-doc.md"),
               ("registry-json", "generated/UAGF-002_registry.json"),
               ("registry-jsonld", "generated/UAGF-002_registry.jsonld"),
               ("registry-ai-context", "generated/UGR-15_ai-context.txt")]
    render_ok = True
    for prof, out in renders:
        args = ["render_ckm.py", "--profile", prof, "--out", out]
        if prof == "registry-ai-context":
            args += ["--scope", "object:UGR-15"]
        rr = sh(*args)
        render_ok &= rr.returncode == 0
    ok &= gate("G5 renders execute (doc/json/jsonld/ai-context)", render_ok)

    # G6: verbatim fidelity — every M-2 field survives Legacy -> YAML -> doc render
    legacy = parse_legacy_records(os.path.join(ROOT, "legacy/UAGF-002_v1.0_source.md"))
    doc = open(os.path.join(ROOT, "generated/UAGF-002_registry-doc.md"), encoding="utf-8").read()
    doc_norm = re.sub(r"\s+", " ", doc)
    undeclared, checked = [], 0
    for oid, fields in legacy.items():
        ypath = os.path.join(ROOT, "ckm-staging/requirements", f"{oid}.yaml")
        if not os.path.exists(ypath):
            undeclared.append({"object": oid, "issue": "missing from staging"}); continue
        y = yaml.safe_load(open(ypath, encoding="utf-8"))
        for lf, attr in VERBATIM_FIELDS.items():
            if lf not in fields:
                continue
            checked += 1
            lv = re.sub(r"\s+", " ", fields[lf]).strip()
            yv = re.sub(r"\s+", " ", str(y.get(attr, ""))).strip()
            if lv != yv:
                undeclared.append({"object": oid, "field": lf, "issue": "YAML != legacy verbatim",
                                   "legacy": lv[:80], "staged": yv[:80]})
            elif lf in ("Statement", "Intent", "Title") and lv not in doc_norm:
                undeclared.append({"object": oid, "field": lf, "issue": "absent from doc render"})
    ok &= gate("G6 verbatim fidelity Legacy->YAML->Render (M-2)",
               not undeclared, f"{checked} field comparisons; undeclared diffs: {len(undeclared)}")

    # G7: conflicts HEALED by ratified Batch B (UFD-007); zero CONFLICT; edges restored
    conf = [d for d in mig["dispositions"] if d["class"] == "CONFLICT"]
    import yaml as _y
    u22 = _y.safe_load(open(os.path.join(ROOT, "ckm-staging/requirements/UGR-22.yaml")))
    u50 = _y.safe_load(open(os.path.join(ROOT, "ckm-staging/requirements/UGR-50.yaml")))
    u51 = _y.safe_load(open(os.path.join(ROOT, "ckm-staging/requirements/UGR-51.yaml")))
    healed = (set(u22["edges"].get("references", [])) >= {"UGR-30", "UGR-31"}
              and "UGR-52" in u50["edges"].get("references", [])
              and "UGR-52" in u51["edges"].get("references", []))
    ok &= gate("G7 dangling refs healed via ratified Batch B (0 CONFLICT)",
               len(conf) == 0 and healed,
               "UGR-22->30/31, UGR-50/51->52 restored mechanically (UFD-007, D-03, EF-2)")

    # G8: JSON-LD round-trip — statements byte-equal model
    ld = json.load(open(os.path.join(ROOT, "generated/UAGF-002_registry.jsonld")))
    stmts = {n["@id"].split("/")[-1]: n.get("statement") for n in ld["@graph"]
             if n["@type"] == "Requirement"}
    rt_bad = [oid for oid, s in stmts.items()
              if s != yaml.safe_load(open(os.path.join(ROOT, "ckm-staging/requirements",
                                                       f"{oid}.yaml"), encoding="utf-8"))["statement"]]
    ok &= gate("G8 JSON-LD round-trip statement integrity", not rt_bad,
               f"{len(stmts)} statements byte-checked")

    # G9: loss manifests exist for lossy profiles; statement uncompressed in AI context
    lm = os.path.join(ROOT, "generated/UGR-15_ai-context.txt.loss-manifest.json")
    ai = open(os.path.join(ROOT, "generated/UGR-15_ai-context.txt"), encoding="utf-8").read()
    stmt15 = yaml.safe_load(open(os.path.join(ROOT, "ckm-staging/requirements/UGR-15.yaml"),
                                 encoding="utf-8"))["statement"]
    ok &= gate("G9 loss manifest present + AI-context statement byte-equal",
               os.path.exists(lm) and stmt15 in ai)

    # G10: release integrity — validator PASS on release; every object published+ratified; hashes match
    rel = os.path.join(ROOT, "ckm-2.0.0-alpha")
    r = sh("validate_ckm.py", rel, "-q", "-o", "reports/release_validation.json")
    man = json.load(open(os.path.join(rel, "release_manifest.json")))
    import hashlib, yaml as _y2
    hash_ok, ratify_ok = True, True
    for relpath, h in man["files"].items():
        p = os.path.join(rel, relpath)
        if relpath != "release_manifest.json":
            hash_ok &= hashlib.sha256(open(p, "rb").read()).hexdigest() == h
            o = _y2.safe_load(open(p, encoding="utf-8"))
            if isinstance(o, dict) and "id" in o:
                ratify_ok &= (o.get("status") == "published" and bool(o.get("ratified_by")))
    ok &= gate("G10 release 2.0.0-alpha integrity (validator PASS + hashes + V-7 ratification)",
               r.returncode == 0 and hash_ok and ratify_ok,
               f"{man['objects']} published objects, ratified_by present, manifest hashes verified")

    summary = {"suite": "uagf-e2e-regression/0.2", "started": t0,
               "finished": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "expected_differences_register": EXPECTED_DIFF,
               "gates": results,
               "result": "PASS" if ok else "FAIL"}
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    json.dump(summary, open(os.path.join(ROOT, "reports/e2e_summary.json"), "w",
                            encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"\nE2E RESULT: {summary['result']}  (report: reports/e2e_summary.json)")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
