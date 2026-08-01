# UAGF CKM — Build in Public (Alpha)
PY=python3
CKM_DIR ?= ckm-2.0.0-alpha        # single canonical default for validate/render; override: make CKM_DIR=ckm-staging render
RELEASE ?= 2.0.0-alpha

test:            ## full E2E regression (G1-G11): validator -> migrate -> render -> diff -> reproducibility
	$(PY) tests/run_e2e.py

validate:        ## Kernel K-1..K-8 validation of $(CKM_DIR)
	$(PY) validate_ckm.py $(CKM_DIR)

migrate:         ## legacy -> ckm-staging (incl. ratified Batch B)
	$(PY) migrate_ckm.py --batch-b batch-b

render:          ## regenerate all artifacts from $(CKM_DIR)
	$(PY) render_ckm.py --ckm $(CKM_DIR) --ckm-release $(RELEASE) --profile registry-doc    --out generated/UAGF-002_registry-doc.md
	$(PY) render_ckm.py --ckm $(CKM_DIR) --ckm-release $(RELEASE) --profile registry-json   --out generated/UAGF-002_registry.json
	$(PY) render_ckm.py --ckm $(CKM_DIR) --ckm-release $(RELEASE) --profile registry-jsonld --out generated/UAGF-002_registry.jsonld
	$(PY) render_ckm.py --ckm $(CKM_DIR) --ckm-release $(RELEASE) --profile registry-ai-context --scope object:UGR-15 --out generated/UGR-15_ai-context.txt

repro:           ## reproducibility: render twice, require byte-identical outputs (RC-2)
	$(PY) render_ckm.py --ckm $(CKM_DIR) --ckm-release $(RELEASE) --profile registry-doc --out /tmp/rr1.md
	$(PY) render_ckm.py --ckm $(CKM_DIR) --ckm-release $(RELEASE) --profile registry-doc --out /tmp/rr2.md
	cmp /tmp/rr1.md /tmp/rr2.md && echo "REPRODUCIBLE: byte-identical"

release:         ## cut a new immutable release from staging (refuses overwrite)
	$(PY) cut_release.py
