# Contributing to UAGF
UAGF is model-first. **Contributions edit CKM objects only** (`ckm-staging/` inputs via `batch-b/`-style proposals,
CVs, or pipeline code). Do not hand-edit derived artifacts under `generated/` or machine-generated reports.
The current CI compares three rendered profiles against baselines; it does not
reject arbitrary generated-file edits or run red/green fixtures.

Before opening a PR:
1. Follow the [Python 3.12 setup and isolated verification sequence](docs/GUIDE.md#alpha-verification-without-make): install requirements, validate release data, migrate, run ledger-aware E2E, then render supported profiles. Make is optional and UNVERIFIED on the verification host. The runner reads migration evidence and checks a merged release-plus-overlay view; it does not perform migration or release-manifest hashing. Its five normal summary gates do not establish full G1–G11 coverage.
2. Never auto-fix data: anomalies are flagged TO_VERIFY / CONFLICT / REJECTED, and CONFLICTs require a Founder ruling.
3. New normative content (Requirements, CV terms, Domains) enters only through a Founder decision recorded in
   `governance/UFD_Decisions_Ledger.yaml`; PRs may *propose*, the ledger *ratifies*.

**Verification ≠ Compliance Certification.** Alpha limitations and pending Founder
dispositions remain. F-414 is a carried residual; no closure is inferred.

**Contribution licensing:** by submitting a contribution you agree to license it under CC BY 4.0,
the repository license (inbound = outbound).
