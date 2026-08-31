#!/usr/bin/env python3
"""UAGF Reference Renderer — Task 003 seed (WP-006 unified pipeline).
One engine: Resolver -> Expansion -> Transformer -> Template -> Serializer -> Stamp.
Profiles: registry-doc | registry-json | registry-jsonld | registry-ai-context.
RE-2: every rendered value traces to a model slot. RE-3: lossy profiles emit a loss manifest.
"""
import os, re, json, argparse, datetime
import yaml

BASE_IRI = "https://uagf.sathira.institute"   # pending OD-06 name ruling for public minting

def load_model(ckm_dir):
    objs = {}
    for dp, _, fs in os.walk(ckm_dir):
        for fn in sorted(fs):
            if fn.endswith((".yaml", ".yml")):
                d = yaml.safe_load(open(os.path.join(dp, fn), encoding="utf-8"))
                if isinstance(d, dict) and "id" in d:
                    objs[d["id"]] = d
    return objs

def resolve_scope(objs, scope):
    if scope.startswith("object:"):
        oid = scope.split(":", 1)[1]
        if oid not in objs:
            raise SystemExit(f"RENDER REFUSED: scope target '{oid}' unresolvable (fail-closed)")
        return {oid}
    if scope == "module:M-CORE":
        return set(objs)
    raise SystemExit(f"RENDER REFUSED: unknown scope '{scope}'")

def pad(oid):  # ID-3: padding is a rendering concern
    m = re.match(r"UGR-(\d+)$", oid)
    return f"UGR-{int(m.group(1)):03d}" if m else oid

def stamp(profile, scope, ckm_release, ckm_dir):
    """Deterministic stamp: derived ONLY from release metadata + dataset content hash.
    No wall clock. Same (profile, scope, release, dataset) => byte-identical artifact (RC-2)."""
    import hashlib
    rel_cut = "unreleased"
    mp = os.path.join(ckm_dir, "release_manifest.json")
    if os.path.exists(mp):
        rel_cut = json.load(open(mp, encoding="utf-8")).get("cut", "unreleased")
    h = hashlib.sha256()
    for dp, _, fs in sorted(os.walk(ckm_dir)):
        for fn in sorted(fs):
            if fn.endswith((".yaml", ".yml")):
                h.update(open(os.path.join(dp, fn), "rb").read())
    return {"profile": profile, "scope": scope, "ckm_release": ckm_release,
            "release_cut": rel_cut, "render_token": h.hexdigest()[:16],
            "engine": "uagf-renderer/0.2", "source_of_truth": BASE_IRI}

def ugrs_by_domain(objs, ids):
    doms = sorted([o for o in objs.values() if o.get("type") == "Domain" and o["id"] in ids],
                  key=lambda d: d["id"])
    out = []
    for d in doms:
        us = sorted([o for o in objs.values() if o.get("type") == "Requirement"
                     and o["id"] in ids
                     and (o.get("edges", {}).get("belongs_to", {}) or {}).get("primary") == d["id"]],
                    key=lambda u: int(u["id"].split("-")[1]))
        out.append((d, us))
    return out

def fmt_sources(u):
    parts = []
    for e in u.get("edges", {}).get("derives_from", []) or []:
        s = e["ref"]
        if e.get("locator"):
            s += f" ({e['locator']})"
        if e.get("verification") == "pending":
            s += " [pending-verification]"
        parts.append(s)
    return "; ".join(parts)

def render_doc(objs, ids, st):
    L = ["# UAGF-002 — Canonical Knowledge Registry (Rendered View)", "",
         f"*Rendered from CKM — profile={st['profile']} · ckm_release={st['ckm_release']} · "
         f"release_cut={st['release_cut']} · render_token={st['render_token']} · engine={st['engine']}*",
         "", "*This artifact is a disposable render. Truth lives in the Canonical Knowledge Model.*", ""]
    for d, us in ugrs_by_domain(objs, ids):
        L.append(f"## {d['label']} ({d['id']})")
        L.append("")
        for u in us:
            L.append(f"### {pad(u['id'])} — {u['label']}  [Normative]")
            L.append("")
            L.append(u["statement"])
            L.append("")
            L.append(f"**Intent.** {u['intent']}")
            L.append("")
            L.append(f"| Field | Value |")
            L.append(f"|---|---|")
            L.append(f"| Requirement Type | {', '.join(u.get('requirement_type', []))} |")
            L.append(f"| Applicability | {u.get('applicability','')} |")
            L.append(f"| Lifecycle Stages | {', '.join(u.get('lifecycle_stages', []))} |")
            L.append(f"| Priority | {u.get('priority','')} |")
            L.append(f"| Risk Categories | {', '.join(u.get('risk_categories', []))} |")
            L.append(f"| Automation Potential | {u.get('automation_potential','')} |")
            L.append(f"| Derived from | {fmt_sources(u)} |")
            refs = u.get("edges", {}).get("references", []) or []
            if refs:
                L.append(f"| See also (informative) | {', '.join(pad(r) for r in refs)} |")
            L.append(f"| Expected Evidence | {u.get('expected_evidence','')} |")
            L.append(f"| Related Controls | {u.get('related_controls','')} |")
            L.append("")
            L.append("**Implementation Guidance**")
            for i, s in enumerate(u.get("implementation_guidance", []), 1):
                L.append(f"{i}. {s}")
            L.append("")
    loss = {"omitted_slots": ["provenance", "owner_module", "created", "modified", "version",
                              "status", "tier"],
            "note": "Documentation view omits machine metadata by declared design (RE-3)."}
    return "\n".join(L), loss

def to_json_obj(u):
    j = {k: v for k, v in u.items() if k not in ("provenance", "_file")}
    j["iri"] = f"{BASE_IRI}/id/{u['type'].lower()}/{u['id']}"
    return j

def render_json(objs, ids, st):
    data = {"stamp": st,
            "objects": [to_json_obj(objs[i]) for i in sorted(ids)]}
    loss_items = []
    for i in sorted(ids):
        o = objs[i]
        omitted = [k for k in ("provenance", "_file") if k in o]
        if omitted:
            loss_items.append({"object": o["id"], "omitted_slots": omitted,
                               "note": "machine metadata omitted by declared design (RE-3)"})
    loss = {"profile_rule": "registry-json renders all model slots verbatim except machine provenance metadata; adds derived IRI and stamp wrapper",
            "items": loss_items}
    return json.dumps(data, indent=2, ensure_ascii=False), loss

def render_jsonld(objs, ids, st):
    g = []
    loss_items = []
    for i in sorted(ids):
        o = objs[i]
        node = {"@id": f"uagf:{o['type'].lower()}/{o['id']}", "@type": o["type"],
                "label": {"@value": o.get("label"), "@language": "en"}}
        for k in ("statement", "intent", "applicability", "priority", "version", "status"):
            if o.get(k) is not None:
                node[k] = o[k]
        for k in ("requirement_type", "lifecycle_stages", "risk_categories"):
            if o.get(k):
                node[k] = o[k]
        e = o.get("edges") or {}
        if (e.get("belongs_to") or {}).get("primary"):
            node["belongsTo"] = f"uagf:domain/{e['belongs_to']['primary']}"
        if e.get("derives_from"):
            node["derivesFrom"] = [
                {"@id": f"uagf:externalreference/{d['ref']}", "locator": d.get("locator"),
                 "verification": d.get("verification")} for d in e["derives_from"]]
        if e.get("references"):
            node["references"] = [f"uagf:requirement/{r}" for r in e["references"]]
        g.append(node)
        # F1+F2: declare ALL omitted slots, key-presence semantics (matches registry-json)
        omitted = [k for k in ("implementation_guidance", "expected_evidence",
                               "related_controls", "automation_potential",
                               "conformance_level", "provenance",
                               "owner_module", "created", "modified", "tier") if k in o]
        if omitted:
            loss_items.append({"object": o["id"], "omitted_slots": omitted,
                               "note": "implementation/operational metadata omitted by declared design (RE-3)"})
    doc = {"@context": {"@vocab": f"{BASE_IRI}/vocab/", "uagf": f"{BASE_IRI}/id/",
                        "belongsTo": {"@type": "@id"}, "references": {"@type": "@id"}},
           "stamp": st, "@graph": g}
    loss = {"profile_rule": "registry-jsonld is declared-lossy; normative statement and traceability edges preserved verbatim; slots present with empty/null values are declared as loss by key presence",
            "items": loss_items}
    return json.dumps(doc, indent=2, ensure_ascii=False), loss

def render_ai_context(objs, ids, st):
    outs, loss_items = [], []
    for i in sorted(ids):
        u = objs[i]
        if u.get("type") != "Requirement":
            continue
        refs = u.get("edges", {}).get("references", []) or []
        dom = (u.get("edges", {}).get("belongs_to") or {}).get("primary", "")
        src = fmt_sources(u)
        block = (f"[UAGF Requirement {pad(u['id'])} | Domain: {dom} | "
                 f"Priority: {u.get('priority','').upper()} | Force: Normative]\n"
                 f"Obligation: {u['statement']}\n"           # statement NEVER compressed (byte-equal)
                 f"Why: {u['intent']}\n"
                 f"Applies to: {u.get('applicability','')}\n"
                 f"Anchors: {src}\n"
                 + (f"Related: {', '.join(pad(r) for r in refs)}\n" if refs else "")
                 + f"Source of truth: {BASE_IRI}/id/requirement/{u['id']} (CKM {st['ckm_release']})")
        outs.append(block)
        loss_items.append({"object": u["id"],
                           "compressed": ["implementation_guidance", "expected_evidence",
                                          "related_controls", "requirement_type",
                                          "lifecycle_stages", "risk_categories"],
                           "statement_integrity": "byte-equal (uncompressed by rule)"})
    loss = {"profile_rule": "registry-ai-context is declared-lossy; normative statement is never truncated or paraphrased",
            "items": loss_items}
    return "\n\n".join(outs), loss

PROFILES = {"registry-doc": render_doc, "registry-json": render_json,
            "registry-jsonld": render_jsonld, "registry-ai-context": render_ai_context}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckm", default="ckm-staging")
    ap.add_argument("--profile", required=True, choices=sorted(PROFILES))
    ap.add_argument("--scope", default="module:M-CORE")
    ap.add_argument("--ckm-release", default="2.0.0-staging")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    objs = load_model(a.ckm)
    ids = resolve_scope(objs, a.scope)
    st = stamp(a.profile, a.scope, a.ckm_release, a.ckm)
    artifact, loss = PROFILES[a.profile](objs, ids, st)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    open(a.out, "w", encoding="utf-8").write(artifact)
    if loss is not None:
        lp = a.out + ".loss-manifest.json"
        json.dump({"stamp": st, "loss": loss}, open(lp, "w", encoding="utf-8"),
                  indent=2, ensure_ascii=False)
    # F4: stdout ต้องตรงกับสิ่งที่เขียนจริง (แก้ predicate mismatch เดิม)
    print(f"RENDERED {a.profile} -> {a.out}"
          + (" (+loss manifest)" if loss is not None else " (lossless)"))

if __name__ == "__main__":
    main()
