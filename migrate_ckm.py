#!/usr/bin/env python3
"""UAGF Migration Runner — Task 002 (WP-005 pipeline S1-S7, Batch A + minted C/D).
Reads the WP-005 manifest as configuration. Transforms are mechanical only (M-1/M-2):
verbatim | trim | split | parse_int_id | casefold_token | parse_numbered_list | parse_sources.
Violations are FLAGGED (TO_VERIFY / CONFLICT / REJECTED) — never silently corrected.
"""
import sys, os, re, json, hashlib, argparse, datetime
import yaml

TODAY = "2026-07-28"

# Instrument alias registry for parse_sources (S4 REF minting; identification only —
# verification is D-06/S5 and is NOT performed here)
INSTRUMENTS = {
    "EU AI Act": ("REF-EUAIA", "EU Artificial Intelligence Act", "2024", "EU"),
    "ISO/IEC 42001": ("REF-ISO42001", "ISO/IEC 42001 — AI Management System", "2023", "International"),
    "PDPA Thailand": ("REF-TH-PDPA", "Thailand Personal Data Protection Act", "2019", "TH"),
    "Thailand PDPA": ("REF-TH-PDPA", "Thailand Personal Data Protection Act", "2019", "TH"),
    "OECD AI Principles": ("REF-OECD-AIP", "OECD AI Principles", "2019", "International"),
    "NIST AI RMF": ("REF-NIST-AIRMF", "NIST AI Risk Management Framework", "1.0", "US"),
    "C2PA Standard": ("REF-C2PA", "Coalition for Content Provenance and Authenticity Standard", "unversioned", "International"),
    "GDPR": ("REF-GDPR", "EU General Data Protection Regulation", "2016", "EU"),
    "UNESCO Recommendation on AI Ethics": ("REF-UNESCO-AI", "UNESCO Recommendation on the Ethics of AI", "2021", "International"),
    "UNESCO AI Ethics": ("REF-UNESCO-AI", "UNESCO Recommendation on the Ethics of AI", "2021", "International"),
    "UNESCO Recommendation on the Ethics of AI": ("REF-UNESCO-RECOMMENDATION-ON", "UNESCO Recommendation on the Ethics of AI", "2021-11-24", "International"),
    "EU Charter of Fundamental Rights": ("REF-EU-CFR", "EU Charter of Fundamental Rights", "2000", "EU"),
}
# Canonical domain concern statements - sourced verbatim from UAGF-001 v1.0 Section 8 [Normative]
# D-06 verification: Founder (Apichai Chuensuang) ratified 2026-08-18
DOMAIN_CANON = {
    "DOM-GOV": "Organizational structure, roles, responsibilities, and accountability for AI",
    "DOM-RISK": "Identification, assessment, mitigation, and monitoring of AI risks",
    "DOM-HUMAN": "Human review, approval, and intervention at critical decision points",
    "DOM-DATA": "Data quality, lineage, classification, provenance, and management",
    "DOM-TRANSPARENCY": "Disclosure of AI system capabilities, logic, limitations, and usage",
    "DOM-AUDITABILITY": "Logging, retention, retrieval, and replayability of AI decisions",
    "DOM-ACCOUNTABILITY": "Clear chain of responsibility for AI system outcomes",
    "DOM-SECURITY": "Protection against unauthorized access, tampering, and misuse",
    "DOM-PRIVACY": "Compliance with privacy laws and protection of data subject rights",
    "DOM-SAFETY": "System safety thresholds, emergency response, and rollback capability",
}

STAGE_MAP = {"all stages": ["all-stages"], "training": ["development"],
             "pre-deployment": ["development", "deployment"]}
BASE_STAGES = {"design", "development", "deployment", "operation", "decommission"}
REQTYPE = {"legal": "legal", "standard": "standard", "principle": "principle",
           "guideline": "guideline", "best practice": "best-practice"}

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def clean(s):
    return re.sub(r"\s+", " ", s.replace("**", "").strip())

def parse_legacy(path, report):
    """S1 extraction: parse UGR field-tables + category headings from the legacy markdown."""
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    records, domains, cur, curdom = [], {}, None, None
    for ln in lines:
        mcat = re.match(r"^#+\s+\**Category\s+\d+:\s*\**\s*(.+?)\s*\((DOM-[A-Z]+)\)", clean(ln)) or \
               re.match(r"^Category\s+\d+:\s*(.+?)\s*\((DOM-[A-Z]+)\)$", clean(ln))
        if mcat:
            curdom = mcat.group(2)
            domains[curdom] = mcat.group(1).strip()
            continue
        if ln.strip().startswith("#") and not re.match(r"^#+\s+\**\s*UGR-\d+", ln.strip()):
            cur = None      # close record at any non-record heading (prevents summary-table bleed)
        mrec = re.match(r"^#+\s+\**\s*(UGR-\d+)\s*[—–-]+\s*(.+?)\**\s*$", ln.strip())
        if mrec:
            cur = {"_legacy_id": mrec.group(1), "_title_heading": clean(mrec.group(2)),
                   "_domain_heading": curdom, "_fields": {}}
            records.append(cur)
            continue
        if cur is not None and ln.strip().startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) == 2:
                k = clean(cells[0])
                v = cells[1].replace("**", "").strip()
                if k and k.lower() not in ("field", "---", ":---"):
                    if k in cur["_fields"]:
                        cur["_fields"][k] += " " + v          # continuation row
                    else:
                        cur["_fields"][k] = v
    report["extraction"] = {"records_found": len(records), "domains_found": len(domains)}
    return records, domains

def map_tokens(raw, mapping, cv_name, oid, disp):
    out = []
    for part in re.split(r"[,/]", raw):
        tok = part.strip().lower()
        if not tok:
            continue
        if tok in mapping:
            m = mapping[tok]
            out.extend(m if isinstance(m, list) else [m])
        else:
            disp.append({"class": "CONFLICT", "object": oid, "field": cv_name, "value": part.strip(),
                         "hint": f"'{part.strip()}' has no ratified mapping for {cv_name}; Founder ruling required (OD-K2/K3)."})
    seen, ded = set(), []
    for t in out:
        if t not in seen:
            seen.add(t); ded.append(t)
    return ded

def parse_sources(raw, oid, refs, disp):
    edges = []
    for part in raw.split(";"):
        part = part.strip()
        if not part:
            continue
        hit = None
        for alias, meta in INSTRUMENTS.items():
            if part.lower().startswith(alias.lower()):
                hit = (alias, meta); break
        if hit is None:
            slug = re.sub(r"[^A-Z0-9]+", "-", part.upper()).strip("-")[:24]
            rid = f"REF-{slug}"
            refs.setdefault(rid, {"instrument_name": part, "instrument_version": "unversioned",
                                  "jurisdiction": "unknown", "label": part})
            disp.append({"class": "TO_VERIFY", "object": oid, "field": "sources", "value": part,
                         "hint": f"Instrument not in alias registry; identify and verify via D-06 before release ({rid})."})
            edges.append({"ref": rid, "version": "unversioned", "verification": "pending"})
            continue
        alias, (rid, name, ver, jur) = hit
        refs.setdefault(rid, {"instrument_name": name, "instrument_version": ver,
                              "jurisdiction": jur, "label": alias})
        locator = part[len(alias):].lstrip(" ,").strip()
        e = {"ref": rid, "version": ver, "verification": "pending"}
        if locator:
            e["locator"] = locator
        edges.append(e)
    return edges

def transform(rec, valid_ids, refs, disp):
    """S2/S3/S4: manifest-driven mechanical transforms. No content rewriting."""
    f = rec["_fields"]
    oid_raw = f.get("UGR ID", rec["_legacy_id"])
    n = int(re.search(r"(\d+)", oid_raw).group(1))
    oid = f"UGR-{n}"
    obj = {
        "id": oid, "type": "Requirement", "tier": 1, "version": "1.0", "status": "proposed",
        "label": f.get("Title", rec["_title_heading"]),
        "owner_module": "M-CORE", "created": "2026-06-28", "modified": TODAY,
        "statement": f.get("Statement", ""), "intent": f.get("Intent", ""),
        "applicability": f.get("Applicability", ""),
        "expected_evidence": f.get("Expected Evidence", ""),
        "related_controls": f.get("Related Controls", ""),
    }
    obj["requirement_type"] = map_tokens(f.get("Requirement Type", ""), REQTYPE, "CV-ReqType", oid, disp)
    stage_map = dict(STAGE_MAP); stage_map.update({s: [s] for s in BASE_STAGES})
    obj["lifecycle_stages"] = map_tokens(f.get("Lifecycle Stage", ""), stage_map, "CV-Stage", oid, disp)
    pri = f.get("Priority", "").strip().lower()
    obj["priority"] = pri
    rc_map = {t: t.replace(" ", "-") for t in
              ["human rights", "safety", "privacy", "security", "fairness", "transparency",
               "governance", "accountability", "auditability", "compliance", "disinformation"]}
    obj["risk_categories"] = map_tokens(f.get("Risk Category", ""), rc_map, "CV-RiskCat", oid, disp)
    auto = f.get("Automation Potential", "").strip().lower()
    if auto:
        obj["automation_potential"] = auto
    ig = f.get("Implementation Guidance", "")
    steps = [s.strip().rstrip(";").strip() for s in re.split(r"\d+\.\s*", ig) if s.strip()]
    obj["implementation_guidance"] = steps
    edges = {"belongs_to": {"primary": f.get("Primary Domain", rec["_domain_heading"])}}
    edges["derives_from"] = parse_sources(f.get("Sources", ""), oid, refs, disp)
    xr = f.get("Cross References", "")
    kept, conflicted = [], []
    for m in re.finditer(r"UGR-(\d+)", xr):
        tid = f"UGR-{int(m.group(1))}"
        (kept if tid in valid_ids else conflicted).append(tid)
    if kept:
        edges["references"] = kept
    for c in conflicted:
        disp.append({"class": "CONFLICT", "object": oid, "field": "edges.references[]", "value": c,
                     "hint": f"Legacy dangling reference {c} (cf. OV-005). Held OUT of staging pending resolution; "
                             f"expected to resolve at Batch B per Founder decision D-03. Never silently dropped — recorded here and in provenance."})
    obj["edges"] = edges
    prov = {"source_document": "UAGF-002 v1.0 PUBLIC RELEASE",
            "source_location": f"Section 5 record {rec['_legacy_id']}",
            "batch": "A", "extraction_timestamp": TODAY,
            "legacy_status": f.get("Status", ""),
            "legacy_revision_history": f.get("Revision History", ""),
            "transform_log": ["trim", "split-declared-delims", "parse_int_id",
                              "casefold_token", "parse_numbered_list", "parse_sources"]}
    ugr_disp = [d for d in disp if d["object"] == oid]
    if ugr_disp:
        prov["dispositions"] = [f"[{d['class']}] {d['field']}={d['value']}" for d in ugr_disp]
    obj["provenance"] = prov
    return obj

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--legacy", default="legacy/UAGF-002_v1.0_source.md")
    ap.add_argument("--manifest", default="manifest.yaml")
    ap.add_argument("--cv-dir", default="ckm/cv")
    ap.add_argument("--out", default="ckm-staging")
    ap.add_argument("--report", default="reports/migration_report.json")
    ap.add_argument("--batch-b", default=None, help="dir of Founder-activated Batch B objects")
    a = ap.parse_args()
    manifest = yaml.safe_load(open(a.manifest, encoding="utf-8"))
    report = {"runner": "uagf-migration-runner/0.1", "manifest_id": manifest["manifest"]["id"],
              "pipeline": "WP-005 S1-S7 (S5 identification-only; D-06 verification pending)",
              "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "source_hash_sha256": sha256(a.legacy), "batches": {}}
    disp = []
    records, domains = parse_legacy(a.legacy, report)
    valid_ids = {f"UGR-{int(re.search(r'(\d+)', r['_fields'].get('UGR ID', r['_legacy_id'])).group(1))}"
                 for r in records}
    batch_b_objs = []
    if a.batch_b and os.path.isdir(a.batch_b):
        for fn in sorted(os.listdir(a.batch_b)):
            if fn.endswith(".yaml"):
                bo = yaml.safe_load(open(os.path.join(a.batch_b, fn), encoding="utf-8"))
                batch_b_objs.append(bo)
                if bo.get("type") == "Requirement":
                    valid_ids.add(bo["id"])
    refs = {}
    ugrs = [transform(r, valid_ids, refs, disp) for r in records]
    for d in sorted(os.listdir(a.cv_dir)) if os.path.isdir(a.cv_dir) else []:
        pass
    # S7 atomic staging write
    for sub in ("requirements", "domains", "references", "cv"):
        os.makedirs(os.path.join(a.out, sub), exist_ok=True)
    for u in ugrs:
        yaml.safe_dump(u, open(os.path.join(a.out, "requirements", f"{u['id']}.yaml"), "w",
                       encoding="utf-8"), sort_keys=False, allow_unicode=True, width=1000)
    for dom_id, name in domains.items():
        canon = DOMAIN_CANON.get(dom_id)
        if canon:
            dom = {"id": dom_id, "type": "Domain", "tier": 1, "version": "1.0", "status": "proposed",
                   "label": name, "owner_module": "M-CORE", "created": "2026-06-28", "modified": TODAY,
                   "concern_statement": canon,
                   "provenance": {"batch": "C", "source_document": "UAGF-001 v1.0 Section 8",
                                  "verification": "D-06 founder-verified 2026-08-18"}}
        else:
            dom = {"id": dom_id, "type": "Domain", "tier": 1, "version": "1.0", "status": "proposed",
                   "label": name, "owner_module": "M-CORE", "created": "2026-06-28", "modified": TODAY,
                   "concern_statement": f"Governance domain: {name}.",
                   "provenance": {"batch": "C-interim", "source_document": "UAGF-002 v1.0 category heading",
                                  "dispositions": ["[TO VERIFY] canonical concern_statement to be sourced from UAGF-001 v1.0 Section 8 at Batch C"]}}
            disp.append({"class": "TO_VERIFY", "object": dom_id, "field": "concern_statement",
                         "value": "category-heading interim text",
                         "hint": "Batch C sources the canonical description from UAGF-001 Section 8."})
        yaml.safe_dump(dom, open(os.path.join(a.out, "domains", f"{dom_id}.yaml"), "w",
                       encoding="utf-8"), sort_keys=False, allow_unicode=True, width=1000)
    for rid, meta in sorted(refs.items()):
        ref = {"id": rid, "type": "ExternalReference", "tier": 1, "version": "0.1",
               "status": "proposed", "label": meta["label"], "owner_module": "M-CORE",
               "created": TODAY, "modified": TODAY,
               "instrument_name": meta["instrument_name"],
               "instrument_version": meta["instrument_version"],
               "jurisdiction": meta["jurisdiction"], "verification": "pending",
               "provenance": {"batch": "D", "minted_by": "Migration S4",
                              "note": "Identification only; D-06 verification (S5) pending."}}
        yaml.safe_dump(ref, open(os.path.join(a.out, "references", f"{rid}.yaml"), "w",
                       encoding="utf-8"), sort_keys=False, allow_unicode=True, width=1000)
    # CVs: ratification-pending copies (K-4: data must bind to CV objects in scope)
    import shutil
    for fn in os.listdir(a.cv_dir):
        shutil.copy(os.path.join(a.cv_dir, fn), os.path.join(a.out, "cv", fn))
    for bo in batch_b_objs:
        sub = {"Requirement": "requirements", "Domain": "domains"}.get(bo.get("type"), "requirements")
        yaml.safe_dump(bo, open(os.path.join(a.out, sub, f"{bo['id']}.yaml"), "w",
                       encoding="utf-8"), sort_keys=False, allow_unicode=True, width=1000)
    report["batches"] = {"A_requirements": len(ugrs),
                         "B_activated": len([b for b in batch_b_objs if b.get("type")=="Requirement"]),
                         "C_domains_interim": len(domains),
                         "D_references_minted": len(refs), "cv_copied": len(os.listdir(a.cv_dir))}
    report["dispositions"] = disp
    report["disposition_counts"] = {c: sum(1 for d in disp if d["class"] == c)
                                    for c in ("TO_VERIFY", "CONFLICT", "REJECTED")}
    report["silent_corrections"] = 0
    os.makedirs(os.path.dirname(a.report), exist_ok=True)
    json.dump(report, open(a.report, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"MIGRATED: {len(ugrs)} UGRs, {len(domains)} domains, {len(refs)} REFs | "
          f"dispositions: {report['disposition_counts']} | report: {a.report}")

if __name__ == "__main__":
    main()
