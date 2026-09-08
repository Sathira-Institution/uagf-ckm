# UAGF Operator & Auditor Guide (v2.0.0-alpha)

> **Status:** v2.0.0-alpha — validated pipeline, pending institutional release.
> **Audience:** compliance officers, auditors, developers, governance architects.
> **Rule of this repo:** Edit the CKM. Validate the CKM. Render the CKM. Never edit a derived artifact.

---

## ⚠️ Alpha Disclosure (Reality First)

This is an alpha release. The automated pipeline is fully operational and fail-closed;
the following governance items are explicitly pending Founder decision and block the
institutional release (but not the technical pipeline):

- **Batch B activation:** 12 of 15 approved UGRs remain inactive in staging.
- **D-06 verification:** `derives_from` source verification pending.
- **Ledger ratification:** partial (UFD-001/007 ratified 2026-08-28; OD-K2/K3/OD-13 pending).
- **Source hashes:** placeholders in `sources[]` until snapshot freeze.

---

## Alpha verification without make

Verified runtime: **Python 3.12** (3.12.14 on the verification host). Other Python
versions are unverified. Install Python 3.12 with venv support before starting.
Run this Bash sequence from the repository root. Make is optional convenience
only; it was unavailable on the verification host, so its targets are UNVERIFIED.
The existing Make targets use repository output paths and are not substitutes for
this isolated sequence.

The runner writes some reports relative to its working directory even when
`--out-summary` is supplied. Copy only its required inputs and scripts to a fresh
temporary workspace first. The source checkout and its committed baselines stay
untouched. Keep the printed workspace path if you need to preserve the evidence;
temporary directories may be removed by the host.

```bash
set -e
export PYTHONDONTWRITEBYTECODE=1
export UAGF_VERIFY="$(mktemp -d /tmp/uagf-alpha-verify.XXXXXX)"
python3.12 -m venv "$UAGF_VERIFY/venv"
source "$UAGF_VERIFY/venv/bin/activate"
python --version
python -m pip install -r requirements.txt
python - <<'PYSETUP'
import os
import shutil
from pathlib import Path
work = Path(os.environ["UAGF_VERIFY"]) / "work"
work.mkdir()
for name in ("migrate_ckm.py", "validate_ckm.py", "render_ckm.py", "manifest.yaml",
             "tests", "legacy", "batch-b", "ckm", "ckm-2.0.0-alpha", "governance"):
    source = Path(name)
    if source.is_dir():
        shutil.copytree(source, work / name)
    else:
        shutil.copy2(source, work / name)
shutil.copytree("generated/baseline", work / "generated/baseline")
(work / "reports").mkdir()
print(work)
PYSETUP
cd "$UAGF_VERIFY/work"
python validate_ckm.py ckm-2.0.0-alpha -o reports/release_validation.json
python migrate_ckm.py --legacy legacy/UAGF-002_v1.0_source.md --manifest manifest.yaml --batch-b batch-b --out ckm-staging --report reports/migration_report.json
python tests/run_e2e.py --ckm ckm-staging --release-base ckm-2.0.0-alpha --ledger governance/UFD_Decisions_Ledger.yaml --migration-report reports/migration_report.json --baseline-dir generated/baseline --out-summary reports/e2e_summary.json
python render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-doc --out generated/UAGF-002_registry-doc.md
python render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-json --out generated/UAGF-002_registry.json
python render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-jsonld --out generated/UAGF-002_registry.jsonld
python render_ckm.py --ckm ckm-2.0.0-alpha --ckm-release 2.0.0-alpha --profile registry-ai-context --scope object:UGR-15 --out generated/UGR-15_ai-context.txt
```

All paths after `cd` are under `$UAGF_VERIFY/work`, outside the source checkout:

- `ckm-2.0.0-alpha/`: copied release data, validated first and used for the four
  standalone renders. These renders describe the release, not the migrated overlay.
- `ckm-staging/`: newly migrated incremental overlay. E2E validates and renders a
  temporary merged view of release plus overlay; staging wins on conflicts.
- `generated/`: new supported-profile renders and adjacent `*.loss-manifest.json`
  files, plus copied committed baselines in `generated/baseline/`.
- `reports/`: release validation, migration, merged validation, E2E summary, and
  `e2e_tmp/` render pairs. The E2E merged dataset is temporary and removed by the runner.

There is no `--profile all`; each supported profile needs its own invocation.
Migration must precede E2E, which reads the migration report but does not run migration.
CI additionally installs pytest and pytest-cov, but does not execute pytest or coverage;
they are not needed for the sequence above.

**Verification ≠ Compliance Certification.** A PASS is bounded by the
[implemented runner checks](../README.md#4-what-the-runner-checks); it does not
establish full G1–G11 coverage, release hash verification, red/green fixture
execution, or rejection of arbitrary generated-file edits. Authority remains with
the [authority contract](authority-contract.md) and Founder decisions. F-414 remains
a carried residual; its original disposition text is unavailable, and no closure
is inferred from these commands.

---

## 🧭 Repository Map

| Path | Purpose | Who touches it |
|---|---|---|
| `ckm/` | Canonical Knowledge Model — single source of truth | Engineering / Founder |
| `legacy/` | Raw source material (migration input) | Migration tooling |
| `ckm-staging/` | Candidate objects awaiting activation | Pipeline (automated) |
| `ckm-2.0.0-alpha/` | Immutable release snapshot | Read-only |
| `governance/` | UFD Decisions Ledger — human ratifications | **Founder only** |
| `reports/` | Evidence artifacts (validation, migration, e2e) | Auditors / QA |
| `generated/` | Derived outputs + baselines — never edit manually | Pipeline (automated) |
| `docs/` | Human documentation (this file) | Documentation owner |

---

## 🔍 How to Read the Evidence (Audit Guide)

Inspect the fresh JSON evidence in `$UAGF_VERIFY/work/reports/` together with the
inputs and command results; committed reports are historical evidence.

### 1. `migration_report.json`
- `"silent_corrections": 0` — must be zero; the system never auto-fixes.
- `"dispositions"` — conflicts held for Founder decision (recorded, never dropped).

### 2. `merged_validation.json`
- `"result": "PASS"`, `"error_count": 0` — any invariant violation halts the pipeline.
- `"objects_loaded": 57` — expected dataset (33 Req + 11 Dom + 7 Ref + 6 CV).

### 3. `e2e_summary.json`
- `"overall_result": "PASS"` — all implemented summary gates pass and profile renders are deterministic.
- `profiles.<profile>.baseline_comparison.status` — `IDENTICAL` means a baseline match;
  `DIFFER_DECLARED_ONLY` permits differences declared in the manifest. Undeclared
  differences fail. Baseline creation is not an established comparison.

### 4. `*.loss-manifest.json`
- Declares what each profile omits/compresses and why.
- `"statement_integrity": "byte-equal"` — normative text is never truncated or paraphrased.

---

## ⚖️ Handling Conflicts (The Human Layer)

If `migration_report.json` shows a `CONFLICT` (e.g., dangling reference):

1. **Do not** edit JSON/YAML manually to hide it.
2. Open a **CONFLICT Disposition** issue (template provided).
3. Await **Founder ratification** in `governance/UFD_Decisions_Ledger.yaml`.
4. Re-run the pipeline; the conflict resolves through authority, not silence.

For Founder-only rulings (mappings, activations), use the **Governance Ruling Request** template.

---

## ❓ FAQ

**Q: Why can't I edit files in `generated/`?**
A: They are derived artifacts; the next pipeline run overwrites them. Edit `ckm/` instead.

**Q: Why does CI fail with a K-8/V-7 violation after I approved a requirement?**
A: Status `approved` requires a `ratified_by` Founder decision reference.
Automation cannot fabricate authority.

**Q: What does "deterministic rendering" guarantee?**
A: Identical CKM + identical profile = byte-identical output, every time.
The E2E runner checks two renders for each of its three profiles and compares
existing baselines. A standalone renderer invocation does not run these checks.
