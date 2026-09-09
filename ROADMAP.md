# Alpha roadmap — no delivery dates or guarantees

This is a planning view at `8376006`, not an institutional commitment. Every item
has a planning label; NOW also records the completed evidence milestone, so
“planned” does not mean its cited implementation is unfinished. Future items are
proposals from the W3 task, recorded in the W3 evidence `decisions.md`, not claims
of implemented capability. Authority remains with the
[Founder ledger](governance/UFD_Decisions_Ledger.yaml) and
[authority contract](docs/authority-contract.md).

## NOW — completed work through W2-B

- **planned — completed milestone:** W0 baseline and evidence preservation;
  `8d283b1` and `~/ai-workspace/uagf-evidence/w0-2026-09-08-8d283b1/preservation.json`.
- **planned — completed milestone:** W1 reproducible Alpha setup and scoped
  verification documentation; `0fa7c33`, merged at `933bc4e`.
- **planned — completed local evidence milestone:** W2-A nine regression tests
  passed at W1 baseline; `~/ai-workspace/uagf-evidence/w2a-regression-2026-09-08/tests-final.stderr`.
  No separate W2-A test commit is present in the main history examined; see [CHANGELOG](CHANGELOG.md).
- **planned — completed milestone:** W2-B technical-only preparation boundary,
  staging-scope disclosure, and preparation regression; `8376006` and
  `~/ai-workspace/uagf-evidence/w2b-compatibility-2026-09-09/test-results.txt`.

## NEXT — proposed gap work

- **planned:** W2 contribution templates; review and extend the existing proposal
  guidance without treating proposals as ratification. Basis: W3 scope decision and
  [CONTRIBUTING](CONTRIBUTING.md) at `8376006`; completion is not asserted.
- **planned:** W4 code-quality assessment and changes if findings justify them.
  No defect inventory or guaranteed refactor is asserted. Basis: W3 scope decision.
- **planned:** W5 external pilot, with scope and acceptance evidence to be defined.
  The cited local verification is not external pilot evidence. Basis: W3 scope
  decision and [readiness evidence limits](FINAL_READINESS.md).

## LATER — future aspirations

- **aspirational:** Full G1–G11 coverage; current five-gate limitations are documented
  in [README](README.md#4-what-the-runner-checks) at `8376006`.
- **aspirational:** Multi-agent protocol exploration; no working protocol is claimed.
  Basis: W3 scope decision, preserved in the evidence directory below.
- **aspirational:** Enterprise features, subject to future requirements and evidence;
  no production deployment or enterprise readiness is claimed. Basis: W3 scope decision.

Planning decisions: `~/ai-workspace/uagf-evidence/w3-release-evidence-2026-09-09/decisions.md`.
All future verification must retain FAIL-CLOSED handling of unknown/failed checks;
technical PASS is not compliance certification or Founder ratification
([RELEASE](RELEASE.md), `8d283b1`, `8376006`).
