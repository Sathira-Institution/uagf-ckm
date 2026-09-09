# Alpha technical release preparation

**TECHNICAL PREPARATION ONLY.** This procedure describes `8376006` and
[cut_release.py](cut_release.py). Institutional release requires explicit scoped
Founder ratification recorded in the [UFD ledger](governance/UFD_Decisions_Ledger.yaml)
and the remaining institutional controls. The acknowledgment flag is not approval;
the script does not verify the ledger. See the [authority contract](docs/authority-contract.md)
and [existing preparation guide](docs/GUIDE.md#technical-staging-preparation).

## Scope and limits

The checked-in staging overlay has **25 objects: 18 requirements and 7 references**,
with no domains or controlled vocabularies. The script copies this overlay only;
it does not merge the release base or validate completeness. Evidence:
`~/ai-workspace/uagf-evidence/w2b-compatibility-2026-09-09/dataset-inventory.json`
and `test-results.txt`; implementation and guide at `8376006`.

It preserves source status and authority metadata without verification and assigns
`ckm_release`. The manifest contains `preparation_scope` and `dataset_scope`,
without generating blanket `ratified_by`. Compatibility names such as
`ckm-2.0.0-alpha` and `release_manifest.json` do not establish authorization.
SHA-256 hashes are generated for copied files, excluding the manifest itself;
the script does not independently verify them. The renderer reads `cut`, does not
verify hashes, and does not propagate these scope fields. Existing-destination
refusal is overwrite protection, not immutable storage. These limits are documented
in [GUIDE](docs/GUIDE.md#technical-staging-preparation) at `8376006`.

## Prepare in isolation

Use the Python 3.12 environment established by the
[Alpha setup sequence](docs/GUIDE.md#alpha-verification-without-make).
From the repository root, with that environment active:

```bash
(
set -e
UAGF_SOURCE="$PWD"
UAGF_PREP="$(mktemp -d /tmp/uagf-technical-prep.XXXXXX)"
cp -R "$UAGF_SOURCE/ckm-staging" "$UAGF_PREP/ckm-staging"
cd "$UAGF_PREP"
python "$UAGF_SOURCE/cut_release.py" --acknowledge-technical-only
printf 'Output workspace: %s\n' "$UAGF_PREP"
)
```

The output directory is `ckm-2.0.0-alpha` within the printed workspace. Do not remove the existing
release base in the source checkout to make this command run. Preserve output,
stdout/stderr, exit status, input revision, and environment alongside the evidence.
Missing acknowledgment or invalid arguments fail before writes (exit 2); an existing
destination is refused (exit 1). This is the tested **FAIL-CLOSED** boundary, not a
claim of transactional recovery from every possible runtime failure. Evidence:
[preparation regression](tests/run_release_preparation.py) at `8376006` and the
W2-B `test-results.txt` cited above.

## Verification before considering further release action

1. From the source root in the configured environment, run
   `python tests/run_release_preparation.py`. It uses isolated preparation fixtures.
   Require exit 0 and inspect its assertions; this is separate from E2E.
2. Follow the complete [isolated verification sequence](docs/GUIDE.md#alpha-verification-without-make):
   validate the copied release base, migrate into isolated staging, then run
   `tests/run_e2e.py` with the release base, ledger, migration report, and committed
   baselines. Keep reports outside the source checkout. Migration must precede E2E.
   The migrated E2E dataset is separate from the copied preparation snapshot, so those E2E results do not automatically validate that specific snapshot.
3. Run all four explicit render commands in that sequence: `registry-doc`,
   `registry-json`, `registry-jsonld`, and `registry-ai-context` (UGR-15 scope).
   Preserve outputs and loss manifests. These standalone renders use the release
   base; E2E uses a temporary merged release-plus-overlay view.
4. Inspect exit codes and reports. Apply FAIL-CLOSED interpretation: unknown or
   failed implemented gates cannot authorize a PASS. A scoped technical PASS cannot
   authorize institutional publication. Preserve evidence for separate Founder review.

These commands and limits are grounded in `0fa7c33`, `8d283b1`, and `8376006`.
Historical W2-B `test-results.txt` records preparation checks, 57-object release
validation, migration, scoped E2E PASS, and four successful renders. Those results
are bounded by their recorded inputs and are not a W3 rerun of the full pipeline.
E2E's five normal gates do not establish full G1–G11 coverage; it does not perform
migration, release-hash verification, red/green fixture execution, or an audit of
arbitrary generated-file edits. See [runner scope](README.md#4-what-the-runner-checks).

**Verification ≠ Compliance Certification.** This document makes no claim of
production readiness or governance ratification; see [FINAL_READINESS.md](FINAL_READINESS.md).
