# UAGF CKM — Build in Public (Alpha)
PY=python3

test:            ## run full E2E regression suite (validator -> migrate -> render -> diff)
	$(PY) tests/run_e2e.py

validate:        ## validate the release dataset against Kernel K-1..K-8
	$(PY) validate_ckm.py ckm-2.0.0-alpha

migrate:         ## re-run migration (legacy -> ckm-staging), incl. ratified Batch B
	$(PY) migrate_ckm.py --batch-b batch-b

render:          ## regenerate all artifacts from the release
	$(PY) render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-doc    --out generated/UAGF-002_registry-doc.md
	$(PY) render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-json   --out generated/UAGF-002_registry.json
	$(PY) render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-jsonld --out generated/UAGF-002_registry.jsonld
	$(PY) render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-ai-context --scope object:UGR-15 --out generated/UGR-15_ai-context.txt

release:         ## cut a new immutable release from staging (refuses to overwrite)
	$(PY) cut_release.py
