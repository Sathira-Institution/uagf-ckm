#!/usr/bin/env python3
"""Prepare a technical staging-overlay snapshot; does not ratify or publish objects."""
import argparse, os, sys, json, shutil, hashlib, datetime
import yaml

RELEASE = "2.0.0-alpha"
SRC, DST = "ckm-staging", f"ckm-{RELEASE}"
NAME = "Universal AI Governance Knowledge Infrastructure"

WARNING = ("WARNING: This script performs technical preparation only. It does NOT "
           "verify Founder ratification in the UFD ledger. Institutional release "
           "requires explicit ledger approval.")
parser = argparse.ArgumentParser(description=__doc__, epilog=WARNING)
parser.add_argument("--acknowledge-technical-only", action="store_true",
                    help="acknowledge that preparation does not authorize institutional release")
args = parser.parse_args()
print(WARNING, file=sys.stderr)
if not args.acknowledge_technical_only:
    parser.error("--acknowledge-technical-only is required; no artifacts prepared")

if os.path.exists(DST):
    print(f"REFUSED: snapshot dir {DST} already exists (overwrite protection)"); sys.exit(1)
shutil.copytree(SRC, DST)
count = 0
for dp, _, fs in os.walk(DST):
    for fn in fs:
        p = os.path.join(dp, fn)
        o = yaml.safe_load(open(p, encoding="utf-8"))
        if not isinstance(o, dict) or "id" not in o:
            continue
        o["ckm_release"] = RELEASE
        yaml.safe_dump(o, open(p, "w", encoding="utf-8"), sort_keys=False,
                       allow_unicode=True, width=1000)
        count += 1
manifest = {"ckm_release": RELEASE, "cut": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "canonical_name": NAME, "namespace": "https://uagf.sathira.institute",
            "preparation_scope": "technical-only; Founder ratification not verified",
            "dataset_scope": "ckm-staging overlay only; not a complete merged CKM release",
            "objects": count, "files": {}}
for dp, _, fs in os.walk(DST):
    for fn in sorted(fs):
        p = os.path.join(dp, fn)
        manifest["files"][os.path.relpath(p, DST)] = hashlib.sha256(open(p, "rb").read()).hexdigest()
json.dump(manifest, open(os.path.join(DST, "release_manifest.json"), "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)
print(f"TECHNICAL SNAPSHOT PREPARED: {DST} | {count} staging-overlay objects prepared | not a complete merged CKM release | Founder ratification not verified")
