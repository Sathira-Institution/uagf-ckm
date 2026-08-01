# Contributing to UAGF
UAGF is model-first. **Contributions edit CKM objects only** (`ckm-staging/` inputs via `batch-b/`-style proposals,
CVs, or pipeline code). Everything under `generated/` and `reports/` is a disposable render — CI rejects any PR
that hand-edits them (regenerate-and-diff gate).

Before opening a PR:
1. `make test` — the 11-gate E2E suite must be green (validator → migrate → render → diff → reproducibility).
2. Never auto-fix data: anomalies are flagged TO_VERIFY / CONFLICT / REJECTED, and CONFLICTs require a Founder ruling.
3. New normative content (Requirements, CV terms, Domains) enters only through a Founder decision recorded in
   `governance/UFD_Decisions_Ledger.yaml`; PRs may *propose*, the ledger *ratifies*.

**Contribution licensing:** by submitting a contribution you agree to license it under CC BY 4.0,
the repository license (inbound = outbound).
