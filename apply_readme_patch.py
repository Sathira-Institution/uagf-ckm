# -*- coding: utf-8 -*-
import io, sys

PATH = "README.md"
with io.open(PATH, encoding="utf-8") as f:
    content = f.read()

PATCHES = []
def P(pid, find, repl):
    PATCHES.append((pid, find, repl))

P("1A",
'[![Validation: 10/10 PASS](https://img.shields.io/badge/Validation-10/10%20Gates%20PASS-brightgreen)](reports/e2e_summary_RELEASE.json)',
'[![E2E: 11/11 PASS](https://img.shields.io/badge/E2E-11/11%20PASS-brightgreen)](reports/e2e_summary.json)')

P("1B",
'| **Validation** | Human-centric and fragmented review | Structured multi-gate validation through the 13-Gate Validation Kernel |',
'| **Validation** | Human-centric and fragmented review | Structured multi-gate validation through the Validation Kernel (K-1..K-8) and the automated E2E suite (G1\u2013G11) |')

P("2A",
'''Standard development and transformation workflows use the **10-Gate Core Validation Profile (G1\u2013G10)**:

```bash
# Execute Core Validation Profile (G1-G10)
python validate_ckm.py --target ckm/ --profile core-validation
```''',
'''Standard development and transformation workflows exercise the Validation Kernel (K-1..K-8) via the validation CLI:

```bash
# Execute the Validation Kernel against a CKM dataset
python validate_ckm.py ckm-2.0.0-alpha
```

The Validation Kernel implements the kernel-level checks (K-1..K-8). End-to-end pipeline verification is performed separately by the automated E2E suite (`tests/run_e2e.py`), which implements automated gates G1\u2013G11.''')

P("2B",
'This process verifies the defined behavior of the governance knowledge pipeline, including validation, transformation, rendering, and regression properties.',
'''The repository's automated end-to-end (E2E) verification suite executes 11 gates (G1\u2013G11):

- G1\u2013G9: Automated pipeline verification covering migration, staged-model validation, rendering, fidelity, and related pipeline checks.
- G10: Release snapshot integrity and ratification metadata verification (release manifest validation, SHA-256 file hash verification, and published/ratified metadata checks).
- G11: Deterministic reproducibility verification \u2014 two independent renders are byte-identical (deterministic stamp).

The Validation Kernel (K-1..K-8) is distinct from these higher-level E2E gates (G1\u2013G11): `validate_ckm.py` runs the Kernel checks; `tests/run_e2e.py` orchestrates the pipeline-level gates and the release-integrity/reproducibility checks.

This process verifies the defined behavior of the governance knowledge pipeline, including validation, transformation, rendering, reproducibility, and regression properties.''')

P("2C",
'''Development workflows use the **10-Gate Core Validation Profile (G1\u2013G10)**. However, official publication and immutable institutional releases require the **13-Gate Full Institutional Release Profile (G1\u2013G13)**.

The additional institutional release gates (G11\u2013G13) verify:
-   **G11:** Cryptographic artifact integrity (SHA-256 manifests).
-   **G12:** Institutional ledger and ratification status (Human Accountability).
-   **G13:** Licensing (CC BY 4.0) and security compliance.

An official release is not simply a successful rendering; it is a validated and institutionally verified snapshot of the Canonical Knowledge Model.''',
'''Development workflows use the Validation Kernel (K-1..K-8) and the automated E2E suite (G1\u2013G11). The current repository implements automated E2E gates G1\u2013G11 only.

The Full Institutional Release concept includes additional institutional release controls beyond the automated E2E gate sequence. These controls are not implemented as G12/G13 automated gate IDs in `tests/run_e2e.py`. Each control has its own handling mechanism:

-   **IC-1:** Cryptographic artifact integrity \u2014 handled through the release-cutting workflow (`cut_release.py`) and release-manifest generation/verification (SHA-256).
-   **IC-2:** Institutional ledger and ratification status \u2014 handled through the Founder/institutional ratification process and the UFD ledger (Human Accountability).
-   **IC-3:** Licensing (CC BY 4.0) and security compliance \u2014 handled as an institutional licensing and security responsibility outside the automated E2E gate sequence.

An official immutable release therefore requires both automated technical verification (G1\u2013G11) and explicit institutional ratification performed outside of the automated E2E gate sequence.''')

P("2D",
'''                     \u2502  Core Profile  \u2502  \u2190 Standard CI/CD (G1\u2013G10)
                     \u2502    (G1\u2013G10)    \u2502''',
'''                     \u2502  Validation    \u2502  \u2190 Validation Kernel (K-1..K-8)
                     \u2502    (K-1..K-8)  \u2502''')

P("2E",
'''              \u2502  Full Institutional Profile \u2502  \u2190 Immutable Snapshot
              \u2502        (G1\u2013G13)             \u2502
              \u2502                             \u2502
              \u2502  + Cryptographic Integrity  \u2502
              \u2502  + Institutional Ratification\u2502
              \u2502  + License & Security       \u2502''',
'''              \u2502  Full Institutional Profile \u2502  \u2190 Immutable Snapshot
              \u2502 (institutional controls \u2014  \u2502
              \u2502  not automated E2E gates)  \u2502
              \u2502                             \u2502
              \u2502  + Release manifest & hashes\u2502
              \u2502  + Institutional ratification\u2502
              \u2502  + License & security checks\u2502''')

P("3A",
'''## Validation Kernel
The UAGF Validation Kernel defines thirteen architectural gates. Standard CKM transformation and rendering pipelines execute the Core Validation Profile (G1\u2013G10), while official publication and immutable institutional releases require the Full Institutional Release Profile (G1\u2013G13).''',
'''## Validation Kernel
The UAGF Validation Kernel (K-1..K-8) enforces defined architectural invariants, structural constraints, semantic constraints, provenance requirements, and pipeline integrity conditions via `validate_ckm.py`. The automated E2E suite (`tests/run_e2e.py`) implements pipeline-level gates G1\u2013G11. Official publication and immutable institutional releases additionally involve institutional release controls beyond the automated E2E gate sequence: IC-1 (release manifest & SHA-256 hashes) handled through the release-cutting workflow (`cut_release.py`); IC-2 (institutional ratification) handled through the Founder/institutional ratification process and the UFD ledger; and IC-3 (license & security checks) handled as an institutional responsibility outside the automated E2E gate sequence.''')

P("3B",
'''The UAGF Validation Kernel operates through two distinct execution profiles to balance continuous development with institutional rigor:

-   **Core Validation Profile (G1\u2013G10):** Executed automatically during continuous integration (CI) for standard CKM transformation, migration, validation, and deterministic rendering.
-   **Full Institutional Release Profile (G1\u2013G13):** Enforced exclusively for official publication and immutable institutional release snapshots, incorporating additional cryptographic, institutional, and compliance verifications.''',
'''The UAGF verification architecture separates three layers:

-   **Validation Kernel (K-1..K-8):** Kernel-level checks executed by `validate_ckm.py`.
-   **Automated E2E Gates (G1\u2013G11):** Executed automatically during continuous integration (CI) by `tests/run_e2e.py`; G1\u2013G9 cover pipeline verification, G10 covers release snapshot integrity & ratification metadata verification, and G11 covers deterministic reproducibility.
-   **Institutional Release Controls (IC-1..IC-3):** Cryptographic release-manifest integrity, institutional ratification, and license & security compliance \u2014 handled through the release-cutting workflow (`cut_release.py`), the Founder/institutional ratification process, and institutional responsibility respectively. These controls are not implemented as automated gate IDs in `tests/run_e2e.py`.''')

P("3C",
'''    subgraph Phase4 ["Phase 4: Institutional & Release Boundary (G11\u2013G13)"]
        G10 --> G11["<b>G11</b><br/>Cryptographic Integrity"]
        G11 --> G12["<b>G12</b><br/>Institutional Ratification"]
        G12 --> G13["<b>G13</b><br/>License & Security Compliance"]
    end

    G13 -->|ALL PASS| RELEASE["<b>\u2713 Validated Immutable Release</b>"]''',
'''    subgraph Phase4 ["Phase 4: Institutional & Release Boundary (IC-1\u2013IC-3, outside automated E2E sequence)"]
        G10 --> IC1["<b>IC-1</b><br/>Cryptographic Integrity<br/>(release manifest, SHA-256)"]
        IC1 --> IC2["<b>IC-2</b><br/>Institutional Ratification<br/>(Founder / UFD ledger)"]
        IC2 --> IC3["<b>IC-3</b><br/>License & Security Compliance"]
    end

    IC3 -->|INSTITUTIONAL RELEASE CRITERIA SATISFIED| RELEASE["<b>\u2713 Validated Immutable Release</b>"]''')

P("3D",
'    G12 -.->|FAIL| HOLD',
'    IC2 -.->|NOT SATISFIED| HOLD')

P("3E",
'''    style G11 fill:#F5F3EE,stroke:#C9A45A,color:#0A1833
    style G12 fill:#F5F3EE,stroke:#C9A45A,color:#0A1833
    style G13 fill:#F5F3EE,stroke:#C9A45A,color:#0A1833''',
'''    style IC1 fill:#F5F3EE,stroke:#C9A45A,color:#0A1833
    style IC2 fill:#F5F3EE,stroke:#C9A45A,color:#0A1833
    style IC3 fill:#F5F3EE,stroke:#C9A45A,color:#0A1833''')

P("3F",
'''| Profile | Gates | Use Case | Enforcement |
| :--- | :--- | :--- | :--- |
| **Core Validation Profile** | G1\u2013G10 | Standard CKM transformation, CI/CD, PR validation | Automated |
| **Full Institutional Release Profile** | G1\u2013G13 | Official publication, immutable release snapshots | Automated + Human Ratification |''',
'''| Layer | Checks | Use Case | Enforcement |
| :--- | :--- | :--- | :--- |
| **Validation Kernel** | K-1..K-8 | Kernel-level structural/semantic/provenance validation | Automated (`validate_ckm.py`) |
| **Automated E2E Gates** | G1\u2013G11 | CI/CD pipeline verification, incl. release integrity (G10) and reproducibility (G11) | Automated (`tests/run_e2e.py`) |
| **Institutional Release Controls** | IC-1..IC-3 | Official publication, immutable release snapshots | Manual Founder/institutional ratification + `cut_release.py` |''')

P("3G",
'''| **G11** | Cryptographic Integrity & Artifact Manifest | SHA-256 manifest verification for all committed outputs |
| **G12** | Institutional Ledger & Ratification | Founder/Institutional sign-offs and decision records |
| **G13** | License & Security Compliance | CC BY 4.0 boundaries, software licenses, security disclosures |''',
'''| **IC-1** | Cryptographic Integrity & Artifact Manifest | SHA-256 manifest verification for release outputs (generated by `cut_release.py`) |
| **IC-2** | Institutional Ledger & Ratification | Founder/Institutional sign-offs and decision records (UFD ledger) |
| **IC-3** | License & Security Compliance | CC BY 4.0 boundaries, software licenses, security disclosures |''')

P("3H",
'''> **Architectural Note:** Gates G11\u2013G13 (highlighted in Institutional Gold) represent the **Full Institutional Release Profile** boundary. These gates enforce human accountability, cryptographic integrity, and legal compliance\u2014ensuring that no automated system can bypass institutional ratification.''',
'''> **Architectural Note:** The institutional release controls IC-1..IC-3 (highlighted in Institutional Gold) represent the **Full Institutional Release** boundary. They embody human accountability, cryptographic integrity, and legal compliance\u2014ensuring that no automated system can bypass institutional ratification. Each control has its own handling mechanism: IC-1 through the release-cutting workflow (`cut_release.py`) and release-manifest generation/verification; IC-2 through the Founder/institutional ratification process and the UFD ledger; and IC-3 as an institutional licensing and security responsibility. None of IC-1..IC-3 is implemented as an automated gate ID in `tests/run_e2e.py` (which implements G1\u2013G11). The executable semantics of the automated E2E gates are those implemented in `tests/run_e2e.py` and summarized in the Quick Start.''')

P("4A",
'''A release is eligible for publication only when the **Full Institutional Release Profile (G1\u2013G13)** has been satisfied. These requirements include:

-   All applicable Core Validation Kernel gates (G1\u2013G10) passing.
-   Cryptographic integrity and artifact manifests verified (G11).
-   Required institutional ledger and ratification decisions recorded (G12).
-   License boundaries and security contacts validated (G13).''',
'''A release is eligible for publication only when the applicable technical and institutional release requirements have been satisfied:

-   Technical (CI-verified): Validation Kernel checks (K-1..K-8) and automated E2E gates (G1\u2013G11), including release snapshot integrity (G10) and deterministic reproducibility (G11).
-   Institutional (handled outside CI): cryptographic release manifest recorded (IC-1), institutional ledger and ratification decisions recorded (IC-2), and license boundaries and security contacts designated and reviewed (IC-3).''')

P("4B",
'-   [ ] End-to-End validation suite passes all applicable validation gates.',
'''-   [ ] Validation Kernel (K-1..K-8) passes.
-   [ ] Automated E2E suite (G1\u2013G11) passes all applicable gates.''')

# ---- apply with strict verification ----
ok = True
for pid, find, repl in PATCHES:
    n = content.count(find)
    if n != 1:
        print(f"[FAIL] {pid}: FIND found {n} times (expected 1) - aborted, file NOT written")
        ok = False
        break
    content = content.replace(find, repl)
    print(f"[OK]   {pid} applied")

if not ok:
    sys.exit(1)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("\n--- post-checks ---")
for bad in ["G13", "13-Gate", "e2e_summary_RELEASE", "G11\u2013G13"]:
    print(f"count '{bad}': {content.count(bad)} (expect 0)")
print(f"count 'IC-1': {content.count('IC-1')} (expect >0)")
print("\nALL 17 PATCHES APPLIED SUCCESSFULLY")
