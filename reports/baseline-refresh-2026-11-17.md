# JSON-LD Baseline Refresh — 2026-11-17

## Scope

Refreshed `generated/baseline/registry-jsonld.baseline` to match the
deterministic merged-view output produced by `tests/run_e2e.py`.

## Reason

The E2E runner was refactored by commit `aba8848` to validate a temporary
merged view:

- release snapshot: `ckm-2.0.0-alpha`
- staging overlay: `ckm-staging`
- precedence: staging overlay over release snapshot

The previous baseline was created before the merged-view refactor and
represented the pre-merged-view lifecycle state.

## Evidence

- Baseline history: `c35e16c`
- Merged-view refactor: `aba8848`
- Release artifact: `a1f5f25`
- Release authority: `UFD-007`
- Current render run 1 SHA-256:
  `5bd8a701e776f6653e0f89398eb50738786b43c9adad5d7b4a891e7895981a66`
- Current render run 2 SHA-256:
  `5bd8a701e776f6653e0f89398eb50738786b43c9adad5d7b4a891e7895981a66`

## Observed changes

- 30 objects changed from `proposed` to `published` in the merged view.
- Batch B reference reconciliation added:
  - `UGR-30` and `UGR-31` to the relevant requirement references.
  - `UGR-52` to the relevant requirement references.
- No source CKM or staging object was modified by this refresh.

## Decision boundary

This refresh updates a derived regression baseline. It does not create,
grant, or infer institutional ratification. The release authority remains
the existing governance record referenced by `UFD-007`.
