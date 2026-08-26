# UAGF Gate-by-Gate Review — 2026-08-27

This report records the gate-by-gate analysis and findings for the UAGF v2.0.0-alpha repository as inspected on 2026-08-27. It is an evidence artifact for the automated pipeline remediation tasks executed thereafter.

Summary verdict

- Overall readiness: Moderate (70/100). Core tooling present (migration, validation, rendering). Key gaps: missing canonical requirements dataset in ckm/requirements, missing E2E runner (tests/run_e2e.py), pending ledger ratification and Batch B activation.

Key observations

- CKM artifacts: ckm/cv/*, ckm/domains/*, ckm/references/* exist. ckm/requirements in this branch snapshot is effectively empty.
- Migration: migrate_ckm.py implements S1–S7 mechanical transforms and writes ckm-staging. Produces reports/migration_report.json.
- Validation: validate_ckm.py implements the Validation Kernel (K-1..K-8), includes ledger check via --require-ledger.
- Rendering: render_ckm.py implements deterministic stamps, loss manifests, and multiple profiles (registry-doc, registry-json, registry-jsonld, registry-ai-context).
- CI: .github/workflows/ci.yml exists but calls validate_ckm.py against ckm-2.0.0-alpha and invokes tests/run_e2e.py (which is missing). CI must be patched to validate ckm-staging and to pass ledger argument.
- Manifest: manifest.yaml contains pipeline preconditions, ugr_mapping, invariants (V-1..V-7), expected_differences, and success_criteria (ingested_ugrs:45). Several open_items are marked pending: D-06-verification-pass, batch-b-remainder, ledger-countersign.

Required immediate actions (high level)

1. Provide an E2E runner (tests/run_e2e.py) that reads manifest.yaml and enforces expected_differences + determinism (G11).
2. Publish governance/UFD_Decisions_Ledger.yaml skeleton to allow validate_ckm.py --require-ledger checks to run (ledger entries remain PENDING-FOUNDER-COUNTERSIGN).
3. Patch CI to run migrate -> validate (with --require-ledger) -> render -> e2e -> upload reports and to not run cut_release in normal CI.
4. Populate Batch B remaining UGRs (12 of 15) or adjust manifest.success_criteria accordingly (founder decision required).

Open manifest items (explicit)

- D-06-verification-pass: pending — affects derives_from verification.
- batch-b-remainder: pending — 12 UGRs not activated.
- ledger-countersign: pending — UFD ledger awaits Founder counter-signature.
- sources[].content_hash: placeholders remain ("<sha256-at-snapshot>").

Repository actions performed

- A new E2E runner will be created on branch: layer0/e2e-runner (tests/run_e2e.py).
- A ledger skeleton will be created on branch: layer0/ledger (governance/UFD_Decisions_Ledger.yaml).
- CI workflow patch will be created on branch: layer0/ci (.github/workflows/ci.yml).

This file is committed as an evidence artifact in reports/gate-review-2026-08-27.md
