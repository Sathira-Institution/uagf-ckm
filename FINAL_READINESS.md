# Alpha readiness evidence

**Alpha: ready for scoped technical review, not production deployment or institutional
release.** This assessment is bounded to main `8376006f5fb011a14d7184240e80a5f6def4e170`
and the historical evidence below. W1 baseline is `933bc4e558445246da6547c4f6616a604446f00a`.
“Ready” means the listed documentation or tested behavior exists; it is not a
certification, full gate-coverage claim, or governance ratification.

## Available for scoped review

- **Documentation:** reproducible Python 3.12 setup, isolated verification, and
  explicit runner limits exist in [GUIDE](docs/GUIDE.md#alpha-verification-without-make),
  [README](README.md#4-what-the-runner-checks), and [CONTRIBUTING](CONTRIBUTING.md);
  `0fa7c33` and W2-B clarification `8376006`.
- **Error paths:** W2-A historical local regression records nine passing tests,
  including evidence-error summaries, source ambiguity, expiry boundaries, and
  duplicate fallback handling. Evidence: `w2a-regression-2026-09-08/tests-final.stderr`,
  `tests-final.command.json`, and `tested-sha.stdout` (W1 baseline). This suite is
  not established as merged or rerun at W2-B.
- **Authority boundary:** `8376006` requires explicit technical acknowledgment,
  refuses existing destinations, preserves source authority metadata without
  verifying it, and discloses overlay-only scope. Evidence:
  [cut_release.py](cut_release.py), [regression](tests/run_release_preparation.py),
  and `w2b-compatibility-2026-09-09/test-results.txt`.
- **Scoped pipeline evidence:** that W2-B test log records preparation regression
  success, validation of 57 release objects with zero errors, E2E PASS with five
  normal summary gates, and successful renders for four profiles. It records
  Python 3.12.14 and PyYAML 6.0.3. W3 does not present these as a fresh full-pipeline run.

All relative evidence paths above are under `~/ai-workspace/uagf-evidence/`.
These are local retained files, not public CI links or immutable storage guarantees.
The W3 packet is `w3-release-evidence-2026-09-09/`, containing draft copies,
source logs, wording decisions, and verification records.

## Not established as ready

- **Full G1–G11 coverage:** five normal runner gates are implemented. E2E does not
  run migration, verify release-manifest hashes, execute red/green fixtures, or
  audit arbitrary generated-file edits. `manual_authoring_events` reads migration
  `silent_corrections`. Evidence: [README runner scope](README.md#4-what-the-runner-checks)
  and [GUIDE](docs/GUIDE.md#alpha-verification-without-make) at `8376006`.
- **Complete CKM from preparation:** the 25-object staging overlay contains 18
  requirements and 7 references, no domains or CVs. It cannot replace the release
  base. Evidence: `w2b-compatibility-2026-09-09/dataset-inventory.json` and
  [preparation guide](docs/GUIDE.md#technical-staging-preparation) at `8376006`.
- **External pilot and production deployment:** the cited records establish local
  technical checks only; they supply no external pilot acceptance or production
  qualification. These remain proposed/future work in [ROADMAP](ROADMAP.md),
  as recorded in W3 `decisions.md`; no absence claim about unexamined systems is made.
- **Institutional authorization:** preparation does not verify Founder ratification.
  Publication needs explicit scoped ledger approval and remaining institutional
  controls. Evidence: `8376006`, [authority contract](docs/authority-contract.md),
  [ledger](governance/UFD_Decisions_Ledger.yaml), and [GUIDE](docs/GUIDE.md#technical-staging-preparation).
- **Residuals and portability:** F-414 remains carried with original disposition
  unavailable; no closure is inferred. Other Python versions and Make targets remain
  unverified in the documented environment. Evidence: [GUIDE](docs/GUIDE.md#alpha-verification-without-make)
  and [CONTRIBUTING](CONTRIBUTING.md) at `8376006`.

**FAIL-CLOSED:** failed or unknown implemented gate results cannot be treated as a
technical PASS (`8d283b1`; [runner](tests/run_e2e.py)). Missing release acknowledgment
fails before writes (`8376006`). Neither behavior establishes universal failure
coverage. **Verification ≠ Compliance Certification.** No institutional ratification,
immutable storage, or production readiness is inferred from these results.
