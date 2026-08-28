# UAGF validation merge semantics (staging as overlay over release base)

## Purpose
- Canonical interpretation used by the E2E runner:
  ckm-staging is an INCREMENTAL OVERLAY over the release snapshot (ckm-2.0.0-alpha).
- Explains how the merged dataset is constructed for validation and why.

## Process
1. Base: read-only release snapshot (ckm-2.0.0-alpha/)
2. Overlay: staging dataset (ckm-staging/) — staging files replace or augment
   base files of matching path.
3. Merged dataset is assembled in a TEMPORARY directory:
   - copy release base into temp dir (if present),
   - overlay staging into temp dir (staging wins on conflicts),
   - ensure cv/, domains/, references/ present in merged view
     (required by kernel invariants).
4. Validate ONLY the merged temp dir. Never validate staging in isolation
   while staging is an incremental overlay.
5. Merge is non-destructive: original release and staging are never modified.
6. Unresolved dangling references (V-1) are recorded as [CONFLICT] dispositions
   and routed to Founder (cf. D-03) — never auto-resolved or dropped.

## Rationale
- Removes false positives caused by validating an incomplete (incremental)
  staging set against invariants that require the full dataset
  (137 findings in run 33023552439; see reports/gate-review-2026-08-27.md).
- Preserves manifest semantics; migration logic stays unmodified.

## Baselines
- generated/baseline/<profile>.baseline is created ONLY after merged validation PASSes.
- Missing baseline reports BASELINE_PENDING (visible pending action), never an implicit pass.
- Undeclared render differences against an existing baseline FAIL the run.

## Governance
- Part of Layer 0 closure (gate review 2026-08-27).
- No manifest.success_criteria changes; no Batch B activation; no ledger
  ratification — all remain Founder-only actions.
