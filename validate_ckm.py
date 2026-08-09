#!/usr/bin/env python3
"""UAGF CKM Schema Validator v0.2 — Kernel K-1..K-8 (WP-004 v0.2), fail-closed.
Enhancements: explainable findings (field/value/reason/allowed/reference) + machine fix hints.
NEVER auto-fixes data (Reality First)."""
import sys, os, re, json, argparse, datetime
import yaml

ENVELOPE_REQUIRED = ["id","type","label","status","version","owner_module","created","modified","tier"]
LIFECYCLE = ["proposed","in-review","approved","published","deprecated","superseded","withdrawn"]
APPROVED_PLUS = {"approved","published","deprecated","superseded"}
ID_PATTERN = re.compile(r"^([A-Z][A-Z0-9]*)-([A-Za-z0-9\-]+)$")
KNOWN_PREFIXES = {"UGR","DOM","REF","REL","CV","UFD","ASM"}
TYPE_PREFIX = {"Requirement":"UGR","Domain":"DOM","ExternalReference":"REF",
               "ControlledVocabulary":"CV","RelationshipType":"REL"}
UGR_REQUIRED = ["statement","intent","requirement_type","applicability","lifecycle_stages",
                "priority","risk_categories","implementation_guidance","expected_evidence","related_controls"]
UGR_CV = {"requirement_type":"CV-ReqType","lifecycle_stages":"CV-Stage","priority":"CV-Priority",
          "risk_categories":"CV-RiskCat","automation_potential":"CV-Auto","conformance_level":"CV-ConfLevel"}
ACYCLIC = ["requires","extends","depends_on"]

def F(rule,obj,msg,sev="error",field=None,value=None,allowed=None,hint=None,ref=None):
    return {"error":rule,"object":obj,"severity":sev,"msg":msg,"field":field,"value":value,
            "allowed_values":allowed,"hint":hint,"reference":ref or f"Kernel {rule}"}

def load(root):
    objs,errs = {},[]
    for dp,_,fs in os.walk(root):
        for fn in sorted(fs):
            if not fn.endswith((".yaml",".yml")): continue
            p = os.path.join(dp,fn)
            try:
                d = yaml.safe_load(open(p,encoding="utf-8"))
            except yaml.YAMLError as e:
                errs.append(F("K-1",fn,f"YAML parse failure: {e}",hint="Fix YAML syntax; no content may enter unparsed.")); continue
            if not isinstance(d,dict):
                errs.append(F("K-1",fn,"File is not a mapping")); continue
            oid = d.get("id",f"<no-id:{fn}>")
            if oid in objs:
                errs.append(F("K-2/ID-2",oid,"Duplicate canonical identifier",field="id",value=oid,
                              hint="Identifiers are permanent and unique forever; assign a new integer.",
                              ref="Kernel K-2 (ID-2)"))
            objs[oid]=d
    return objs,errs

def validate(objs):
    fs=[]
    cvs={i:o for i,o in objs.items() if o.get("type")=="ControlledVocabulary"}
    terms={i:{t.get("token") for t in (o.get("terms") or [])} for i,o in cvs.items()}
    for oid,o in objs.items():
        for s in ENVELOPE_REQUIRED:
            if s not in o or o[s] in (None,""):
                fs.append(F("K-1",oid,f"Envelope slot missing: {s}",field=s,
                            hint="Every canonical object carries the full K-1 envelope.",ref="Kernel K-1"))
        m=ID_PATTERN.match(str(o.get("id","")))
        if not m:
            fs.append(F("K-2",oid,"Identifier does not match <PREFIX>-<id>",field="id",value=o.get("id"),
                        hint="Use the canonical short form, e.g. UGR-15.",ref="Kernel K-2 (ID-1)"))
        else:
            pre=m.group(1)
            if pre not in KNOWN_PREFIXES:
                fs.append(F("N-3",oid,f"Prefix '{pre}' not in ratified prefix registry",field="id",value=pre,
                            allowed=sorted(KNOWN_PREFIXES),
                            hint="Reserved-not-activated prefixes require Founder activation before use.",
                            ref="Kernel K-7 (N-3)"))
            exp=TYPE_PREFIX.get(o.get("type"))
            if exp and pre!=exp:
                fs.append(F("K-2",oid,f"Prefix '{pre}' does not match type '{o.get('type')}'",field="id",
                            value=pre,allowed=[exp],hint=f"Objects of type {o.get('type')} use prefix {exp}-.",
                            ref="Kernel K-2"))
            if pre=="UGR":
                t=m.group(2)
                if not t.isdigit():
                    fs.append(F("K-2",oid,"UGR id tail must be an opaque integer",field="id",value=t,
                                hint="IDs carry no meaning; use a plain integer.",ref="Kernel K-2 (ID-1)"))
                elif t!=str(int(t)):
                    fs.append(F("K-2",oid,"Canonical id stores unpadded integer",field="id",value=t,
                                allowed=[str(int(t))],
                                hint="Zero-padding is rendering-only (ID-3); store the bare integer.",
                                ref="Kernel K-2 (ID-3)"))
        st=o.get("status")
        if st is not None and st not in LIFECYCLE:
            fs.append(F("L-1",oid,f"Status '{st}' not in kernel lifecycle vocabulary",field="status",value=st,
                        allowed=LIFECYCLE,hint="Map legacy statuses in provenance; CKM status comes from the pipeline.",
                        ref="Kernel K-5 (L-1)"))
        if st in APPROVED_PLUS and not o.get("ratified_by"):
            fs.append(F("V-7",oid,f"Status '{st}' requires a ratified_by decision reference",
                        field="ratified_by",allowed=["UFD-<n> reference"],
                        hint="Attach the Founder decision reference (UFD ledger, pending OD-13) or keep status below 'approved'. Never fabricate a decision.",
                        ref="Kernel K-5/K-8, Invariant V-7"))
        if o.get("tier") not in (1,2,None):
            fs.append(F("K-1",oid,"tier must be 1 or 2",field="tier",value=o.get("tier"),allowed=[1,2]))
        ver=str(o.get("version",""))
        if ver and not re.match(r"^\d+\.\d+$",ver):
            fs.append(F("L-2",oid,f"Version '{ver}' is not MAJOR.MINOR",field="version",value=ver,
                        hint="Use MAJOR.MINOR; MAJOR changes require a supersedes edge.",ref="Kernel K-5 (L-2)"))
        if o.get("tier")==2:
            fs.append(F("V-5",oid,"Tier-2 instance data present in public model dataset (forbidden)",
                        field="tier",value=2,
                        hint="Remove adopter-side instance; Tier-2 lives outside UAGF by design (OD-09).",
                        ref="Kernel K-8, Invariant V-5"))
    for oid,o in objs.items():
        if o.get("type")!="Requirement": continue
        for a in UGR_REQUIRED:
            if a not in o or o[a] in (None,"",[]):
                fs.append(F("B.2",oid,f"Required UGR attribute missing: {a}",field=a,
                            hint="Populate from legacy source verbatim (M-2) — never invent.",
                            ref="WP-004 B.2 UGR schema"))
        for a,cv in UGR_CV.items():
            if a not in o or o[a] is None: continue
            vals=o[a] if isinstance(o[a],list) else [o[a]]
            if cv not in terms:
                fs.append(F("CV-1",oid,f"Bound CV '{cv}' not present in dataset",field=a,
                            hint=f"Include {cv} in the dataset scope.",ref="Kernel K-4 (CV-1)")); continue
            for val in vals:
                if val not in terms[cv]:
                    fs.append(F("V-4",oid,f"'{val}' is not a valid member of {cv}@{cvs[cv].get('version')}",
                                field=a,value=val,allowed=sorted(x for x in terms[cv] if x),
                                hint=f"Map '{val}' via the ratified legacy_map or request Founder ruling (OD-K2/OD-K3). Never auto-fix.",
                                ref="Kernel K-4, Invariant V-4"))
        e=o.get("edges") or {}
        pr=(e.get("belongs_to") or {}).get("primary")
        if not pr:
            fs.append(F("B.2",oid,"belongs_to.primary missing (exactly 1 required)",field="edges.belongs_to.primary",
                        hint="Every Requirement belongs to exactly one primary Domain.",ref="WP-004 B.2 / K-3"))
        elif pr not in objs:
            fs.append(F("V-1",oid,f"belongs_to target '{pr}' does not resolve",field="edges.belongs_to.primary",
                        value=pr,hint="Add the Domain object or correct the id. Never delete the edge silently.",
                        ref="Kernel K-3, Invariant V-1"))
        elif objs[pr].get("type")!="Domain":
            fs.append(F("R-2",oid,f"belongs_to target '{pr}' is not a Domain",field="edges.belongs_to.primary",
                        value=pr,ref="Kernel K-3 (R-2)"))
        df=e.get("derives_from") or []
        if not df:
            fs.append(F("V-3",oid,"Requirement has no derives_from edge",field="edges.derives_from",
                        hint="Every Requirement derives from >=1 ExternalReference (UGR-TRACE-001 successor); build the edge from legacy 'Sources'.",
                        ref="Kernel K-8, Invariant V-3"))
        for d in df:
            t=d.get("ref")
            if t not in objs:
                fs.append(F("V-1",oid,f"derives_from target '{t}' does not resolve",
                            field="edges.derives_from[].ref",value=t,
                            hint="Mint the ExternalReference in Migration S4 (verify via D-06/S5) or correct the id.",
                            ref="Kernel K-3, Invariant V-1"))
            elif objs[t].get("type")!="ExternalReference":
                fs.append(F("R-2",oid,f"derives_from target '{t}' is not an ExternalReference",
                            field="edges.derives_from[].ref",value=t,ref="Kernel K-3 (R-2)"))
            if d.get("verification") not in ("verified","pending"):
                fs.append(F("V-3",oid,f"derives_from to '{t}' lacks verification disposition",
                            field="edges.derives_from[].verification",value=d.get("verification"),
                            allowed=["verified","pending"],
                            hint="D-06 outcomes only; REJECTED edges are quarantined, not stored bare.",
                            ref="WP-005 S5, Invariant V-3"))
        for r in (e.get("references") or []):
            if r not in objs:
                fs.append(F("V-1",oid,f"references target '{r}' does not resolve",field="edges.references[]",
                            value=r,hint="If legacy dangling ref: record [CONFLICT] and route to Founder (cf. D-03). Never silently drop.",
                            ref="Kernel K-3, Invariant V-1"))
    referenced=set()
    for oid,o in objs.items():
        e=o.get("edges") or {}
        b=(e.get("belongs_to") or {}).get("primary")
        if b: referenced.add(b)
        for d in (e.get("derives_from") or []):
            if d.get("ref"): referenced.add(d["ref"])
        for r in (e.get("references") or []): referenced.add(r)
    for oid,o in objs.items():
        if o.get("tier")==1 and o.get("status")=="published":
            if not (o.get("edges") or {}) and oid not in referenced and o.get("type") not in ("Domain","ControlledVocabulary"):
                fs.append(F("V-2",oid,"Published Tier-1 object has no normative edge (orphan)",
                            hint="Connect the object or question why it exists.",ref="Kernel K-8, Invariant V-2"))
    for et in ACYCLIC:
        g={i:[t for t in ((o.get("edges") or {}).get(et) or [])] for i,o in objs.items()}
        st={}
        def dfs(n):
            st[n]=1
            for t in g.get(n,[]):
                if st.get(t)==1:
                    fs.append(F("V-6",n,f"Cycle detected on '{et}' via {t}",field=f"edges.{et}",
                                hint="Break the cycle; these edge types are declared acyclic.",
                                ref="Kernel K-3, Invariant V-6"))
                elif st.get(t) is None and t in g: dfs(t)
            st[n]=2
        for n in g:
            if st.get(n) is None: dfs(n)
    return fs

# ==========================================
# NEW ADDITION: K-8 Ledger Validation (for Full Institutional Release Profile)
# ==========================================

def load_ledger(ledger_path):
    """Load and parse the UFD Decisions Ledger YAML file.

    Returns (ledger_dict, error_message). On success error_message is None.
    """
    if not ledger_path:
        return None, "No ledger path provided"
    if not os.path.exists(ledger_path):
        return None, f"Ledger file not found at {ledger_path}"
    try:
        with open(ledger_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            return None, "Ledger content is not a mapping"
        return data, None
    except Exception as e:
        return None, f"Error parsing ledger: {e}"


def validate_ratification_ledger(obj, ledger_decisions):
    """
    K-8 Invariant: Verify that 'ratified_by' references a valid decision in the ledger
    and that the referenced decision is in 'ratified' status.
    ledger_decisions is expected to be a mapping of decision_id -> decision_object.
    """
    ratified_by = obj.get('ratified_by')
    if not ratified_by:
        # Draft/staging items may legitimately lack a ratified_by reference.
        return True, None
    if ratified_by not in ledger_decisions:
        return False, f"K-8 VIOLATION: 'ratified_by' references '{ratified_by}', which is not found in the UFD Decisions Ledger."
    decision = ledger_decisions[ratified_by]
    decision_status = decision.get('status')
    if decision_status != 'ratified':
        return False, f"K-8 VIOLATION: Decision '{ratified_by}' is not in 'ratified' status (current: {decision_status})."
    return True, None

# ==========================================
# NEW ADDITION: CLI Argument for Ledger
# ==========================================

def parse_args():
    parser = argparse.ArgumentParser(description="UAGF Validation Kernel")
    parser.add_argument("ckm_dir", help="Path to the CKM directory")
    parser.add_argument("-o","--out",default=None,help="Write JSON report to file")
    parser.add_argument("-q","--quiet",action="store_true",help="Suppress human output")
    parser.add_argument("--require-ledger", help="Path to UFD_Decisions_Ledger.yaml (Enforces K-8)", default=None)
    return parser.parse_args()

# ==========================================
# Main execution (modified to optionally load ledger and enforce K-8 checks)
# ==========================================

def main():
    args = parse_args()

    # Load ledger if requested
    ledger_data = None
    if args.require_ledger:
        ledger, error = load_ledger(args.require_ledger)
        if error:
            print(f"[CRITICAL] {error}", file=sys.stderr)
            sys.exit(2)  # Exit 2: CRITICAL_KERNEL_ERROR
        ledger_data = ledger.get('decisions', {}) or {}
        print(f"[INFO] Ledger loaded: {len(ledger_data)} decisions found.", file=sys.stderr)

    objs,le = load(args.ckm_dir)
    findings = le + validate(objs)

    # If ledger loaded, run K-8 ratification checks against each object
    if ledger_data is not None:
        for oid,obj in objs.items():
            is_valid, msg = validate_ratification_ledger(obj, ledger_data)
            if not is_valid:
                findings.append(F("K-8", oid, msg, sev="error", field="ratified_by", value=obj.get('ratified_by'), ref="Kernel K-8"))

    errors=[f for f in findings if f["severity"]=="error"]
    rep={"validator":"uagf-ckm-validator/0.2","kernel":"WP-004 v0.2 (K-1..K-8)",
         "dataset":os.path.abspath(args.ckm_dir),
         "timestamp":datetime.datetime.now(datetime.timezone.utc).isoformat(),
         "objects_loaded":len(objs),"objects_by_type":{},
         "findings":findings,"result":"PASS" if not errors else "FAIL","error_count":len(errors)}
    for o in objs.values():
        t=o.get("type","<untyped>"); rep["objects_by_type"][t]=rep["objects_by_type"].get(t,0)+1
    if not args.quiet:
        for f in findings:
            L=[f"{'ERROR' if f['severity']=='error' else 'WARN'} [{f['error']}]", f"Object: {f['object']}"]
            if f.get("field"): L.append(f"Attribute: {f['field']}")
            if f.get("value") is not None: L.append(f"Value: {f['value']!r}")
            L.append(f"Reason: {f['msg']}")
            if f.get("allowed_values"): L.append("Allowed values: "+", ".join(map(str,f["allowed_values"])))
            if f.get("hint"): L.append(f"Hint: {f['hint']}")
            L.append(f"Reference: {f['reference']}")
            print("  "+"\n    ".join(L)+"\n",file=sys.stderr)
    out=json.dumps(rep,indent=2,ensure_ascii=False)
    if args.out: open(args.out,"w",encoding="utf-8").write(out)
    print(out if args.quiet else f"RESULT: {rep['result']} | objects: {len(objs)} | errors: {rep['error_count']}")
    if args.out is None and args.quiet: pass
    sys.exit(0 if rep["result"]=="PASS" else 1)

if __name__=="__main__": main()
