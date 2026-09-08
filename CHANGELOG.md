# Alpha change evidence — W0 through W2-B

Scope: main at `8376006f5fb011a14d7184240e80a5f6def4e170`; W1 merge baseline
`933bc4e558445246da6547c4f6616a604446f00a`. This is a work-package extract,
not a complete historical changelog or a declaration of release readiness.
Dates are Git author dates; subjects below are reproduced from non-merge history.
The source `git log --oneline --no-merges` and dated log are preserved under
`~/ai-workspace/uagf-evidence/w3-release-evidence-2026-09-09/`.

## W0 — baseline implementation and evidence preservation

[2026-09-08] 8d283b1 fix(p1-4): enforce ingested_ugrs_enforced=33 with fail-closed gates (… (#6)

W0 evidence preservation is recorded separately in
`~/ai-workspace/uagf-evidence/w0-2026-09-08-8d283b1/preservation.json`.
The commit is the implementation baseline, not a new W0 preservation commit.

## W1 — reproducible Alpha documentation

[2026-09-08] 0fa7c33 docs: make alpha setup and verification reproducible

Merged at `933bc4e558445246da6547c4f6616a604446f00a`; merge commits are
excluded from the change entries by design.

## W2-A — local regression evidence

No separate W2-A change appears in this main non-merge history. Do not infer
that its local test suite was merged. It tested W1 baseline `933bc4e`:
`~/ai-workspace/uagf-evidence/w2a-regression-2026-09-08/tested-sha.stdout`.
Nine tests passed in `tests-final.stderr`, with exit 0 recorded in
`tests-final.command.json` in that directory. This is historical local evidence,
not a fresh test result at W2-B.

## W2-B — technical preparation authority boundary

[2026-09-09] 8376006 fix: constrain W2-B staging preparation to technical-only authority (#8)

See [RELEASE.md](RELEASE.md) for the staging-only scope and FAIL-CLOSED
acknowledgment behavior. Technical verification does not establish compliance
certification, institutional ratification, or production readiness.
