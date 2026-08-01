#!/usr/bin/env python3
"""S8-S9: ratify staged objects (per UFD-007) and cut an immutable CKM release snapshot."""
import os, sys, json, shutil, hashlib, datetime
import yaml

RELEASE = "2.0.0-alpha"
SRC, DST = "ckm-staging", f"ckm-{RELEASE}"
NAME = "Universal AI Governance Knowledge Infrastructure"   # OD-06 RATIFIED (UFD-007)

if os.path.exists(DST):
    print(f"REFUSED: release dir {DST} already exists (releases are immutable, RB-3)"); sys.exit(1)
shutil.copytree(SRC, DST)
count = 0
for dp, _, fs in os.walk(DST):
    for fn in fs:
        p = os.path.join(dp, fn)
        o = yaml.safe_load(open(p, encoding="utf-8"))
        if not isinstance(o, dict) or "id" not in o:
            continue
        o["status"] = "published"
        o.setdefault("ratified_by", "UFD-007")   # S8: Founder ratification reference
        o["ckm_release"] = RELEASE
        yaml.safe_dump(o, open(p, "w", encoding="utf-8"), sort_keys=False,
                       allow_unicode=True, width=1000)
        count += 1
manifest = {"ckm_release": RELEASE, "cut": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "canonical_name": NAME, "namespace": "https://uagf.sathira.institute",
            "ratified_by": "UFD-007 (see governance/UFD_Decisions_Ledger.yaml)",
            "objects": count, "files": {}}
for dp, _, fs in os.walk(DST):
    for fn in sorted(fs):
        p = os.path.join(dp, fn)
        manifest["files"][os.path.relpath(p, DST)] = hashlib.sha256(open(p, "rb").read()).hexdigest()
json.dump(manifest, open(os.path.join(DST, "release_manifest.json"), "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)
print(f"RELEASE CUT: {DST} | {count} objects published | ratified_by UFD-007")
