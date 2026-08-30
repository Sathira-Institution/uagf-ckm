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

## 🚀 Quick Start (5 minutes)

UAGF is a knowledge compiler, not a document editor.

1. **Edit source** — modify `legacy/` (raw input) or `ckm/` (canonical model).
2. **Migrate** — `python migrate_ckm.py` (conservative, provenance-preserving).
3. **Validate** — `python validate_ckm.py --require-ledger` (Kernel K-1..K-8; fail-closed).
4. **Render** — `python render_ckm.py` (deterministic profiles + Loss Manifests).
5. **Verify** — `python tests/run_e2e.py` (G1–G11, determinism vs baselines).

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

Do not trust rendered documents. Trust the JSON evidence in `reports/`.

### 1. `migration_report.json`
- `"silent_corrections": 0` — must be zero; the system never auto-fixes.
- `"dispositions"` — conflicts held for Founder decision (recorded, never dropped).

### 2. `merged_validation.json`
- `"result": "PASS"`, `"error_count": 0` — any invariant violation halts the pipeline.
- `"objects_loaded": 57` — expected dataset (33 Req + 11 Dom + 7 Ref + 6 CV).

### 3. `e2e_summary.json`
- `"overall_result": "PASS"` — all gates green.
- `baseline_comparison.status` — `IDENTICAL` means renders match committed baselines
  (regression guard active); any undeclared change fails the pipeline.

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
Verified against `generated/baseline/` on every run.
