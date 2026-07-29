# Universal AI Governance Framework (UAGF)

> **A Canonical Knowledge Infrastructure for Interoperable AI Governance**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Alpha](https://img.shields.io/badge/Status-Alpha-orange)](https://github.com/Sathira-Institution/uagf-ckm)
[![Public Good](https://img.shields.io/badge/Public-Good-green)](#public-benefit)
[![Machine Readable](https://img.shields.io/badge/Machine-Readable-blue)](#canonical-knowledge-model)

---

## Why UAGF Exists

Modern AI governance is increasingly fragmented.

Organizations today must navigate multiple standards, regulations, and internal governance frameworks, each using different terminology, structures, and assumptions.

Examples include:

- ISO/IEC 42001
- EU AI Act
- NIST AI RMF
- OECD AI Principles
- Thailand PDPA
- Organizational AI Policies

Although these documents often pursue similar governance goals, they are not directly interoperable.

**UAGF provides a canonical knowledge layer that allows these governance systems to work together without replacing them.**

---

## What is UAGF?

The **Universal AI Governance Framework (UAGF)** is an open, machine-readable knowledge infrastructure for AI governance.

Rather than creating another governance framework, UAGF provides a **Canonical Knowledge Model (CKM)** that enables existing governance knowledge to be represented in a common language.

> **UAGF does not replace standards. It connects them.**
>
> **UAGF does not replace regulations. It translates them.**
>
> **UAGF does not replace governance frameworks. It enables them to interoperate.**

---
---

### 💡 The Core Differentiator: One Model, Many Views

> **UAGF maintains a single Canonical Knowledge Model (CKM) as the absolute source of truth.**
> 
> Every document, dataset, API response, JSON-LD graph, AI context, and user interface is **rendered** from that model. 
> 
> **Documentation is a generated artifact — not the authoritative source.**

This "Model-First" architecture ensures:
- **Zero Drift:** The human-readable document and the machine-readable JSON-LD are always 100% synchronized.
- **Single Source of Truth:** Updates are made to the CKM (YAML), and all views are automatically regenerated.
- **Future-Proof:** New output formats (e.g., new API endpoints, new UI dashboards) can be added without rewriting any governance content.
# Core Philosophy

Truth lives in the **Canonical Knowledge Model**.

Everything else is a render.

Documents are disposable.

Knowledge is permanent.

---

# Design Principles

UAGF follows several fundamental principles.

### 🌍 Open by Design

Developed as a public-good initiative and released under CC BY 4.0.

### 🔍 Evidence over Assumption

Every governance statement should be traceable to verifiable sources.

### ⚖ Vendor & Origin Neutral

No preference for vendors, countries, technologies, or governance traditions.

### 🤖 AI-Native

Machine-readable by design using structured knowledge representations.

### 🔄 Interoperable

Connects governance knowledge across standards, regulations, and organizational policies.

### 📖 Reality First

Documentation is generated from the knowledge model—not maintained independently.

---

# Architecture

```
                   External Sources

      ISO 42001
      EU AI Act
      NIST AI RMF
      OECD AI Principles
      PDPA
      Organizational Policies

                │
                ▼

     Canonical Knowledge Model (CKM)

                │
        ┌───────┼────────┐
        ▼       ▼        ▼

    Markdown  JSON-LD   RDF

        ▼       ▼        ▼

 Documentation  APIs   AI Context
```

The CKM is the single source of truth.

Every artifact—including documents, APIs, JSON-LD, RDF, AI context, and web interfaces—is generated from the same canonical model.

---

# Repository Structure

```
.
├── ckm/
│   ├── requirements/
│   ├── domains/
│   ├── references/
│   └── cv/
│
├── ckm-staging/
│
├── generated/
│
├── reports/
│
├── tests/
│
├── migrate_ckm.py
├── validate_ckm.py
├── render_ckm.py
├── manifest.yaml
│
└── README.md
```

---

# Repository Contents

## Canonical Knowledge Model

```
ckm/
```

The canonical source of truth.

Contains:

- Unified Governance Requirements (UGRs)
- Governance Domains
- External References
- Controlled Vocabularies

---

## CKM Staging

```
ckm-staging/
```

Migration workspace before ratification.

---

## Generated Artifacts

```
generated/
```

Automatically rendered outputs including:

- Markdown
- JSON
- JSON-LD
- RDF
- AI Context

These artifacts are disposable.

The CKM remains the only source of truth.

---

## Tests

```
tests/
```

Automated validation including:

- Kernel validation
- Migration validation
- Render regression
- End-to-End regression tests

---

## Reports

```
reports/
```

Generated reports such as:

- Validation reports
- Migration reports
- Regression reports

---

# Tooling

## validate_ckm.py

Validates the Canonical Knowledge Model.

Checks:

- Kernel invariants
- Schema integrity
- Controlled vocabularies
- Relationship consistency
- Namespace rules

---

## migrate_ckm.py

Migrates legacy documents into the CKM.

Features:

- Provenance tracking
- Deterministic migration
- No silent correction
- Machine-verifiable validation

---

## render_ckm.py

Renders CKM into multiple output formats.

Supported profiles include:

- registry-doc
- registry-json
- registry-jsonld
- registry-rdf
- registry-ai-context

---

## manifest.yaml

Migration configuration and mapping specification.

---

# Quick Start

## Requirements

- Python 3.10+
- PyYAML

Install dependencies

```bash
pip install pyyaml
```

---

## Validate the CKM

```bash
python validate_ckm.py --ckm-dir ckm
```

---

## Render Documentation

```bash
python render_ckm.py \
  --profile registry-doc \
  --release 2.0.0
```

---

## Generate JSON-LD

```bash
python render_ckm.py \
  --profile registry-jsonld \
  --release 2.0.0
```

---

## Run End-to-End Tests

```bash
python tests/run_e2e.py
```

---

# Example Workflow

```
Legacy Documents

        │

        ▼

Migration Runner

        │

        ▼

Canonical Knowledge Model

        │

        ▼

Validator

        │

        ▼

Renderer

        │

        ▼

Markdown
JSON
JSON-LD
RDF
AI Context
```

---

# Current Project Status

| Component | Status |
|------------|--------|
| Canonical Knowledge Model | ✅ Alpha |
| Kernel Validator | ✅ Implemented |
| Migration Pipeline | ✅ Prototype |
| Rendering Engine | ✅ Prototype |
| JSON-LD | ✅ Supported |
| RDF | 🚧 In Progress |
| Reference Verification | 🚧 In Progress |
| Stable Release | 🚧 Planned |

---

# Governance

Architecture evolution is documented through Working Papers (WP).

Major architectural changes require formal review before becoming part of the Canonical Knowledge Model.

The CKM remains the single authoritative source of governance knowledge.

---

# Public Benefit

UAGF is developed and maintained by **Sathira Institution** as an open public-good initiative.

The project aims to improve AI governance interoperability by providing openly available, machine-readable governance knowledge that can be used by:

- Governments
- Standards organizations
- Researchers
- Industry
- Educational institutions
- Civil society

UAGF is intended to complement—not replace—existing governance standards, regulations, and organizational frameworks.

---

# License

This project is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** License.

You are free to:

- Share
- Adapt
- Build upon

provided appropriate attribution is given.

---

# Citation

If you use UAGF in research, academic publications, or derived work, please cite:

```bibtex
@misc{uagf2026,
  title={Universal AI Governance Framework},
  author={Sathira Institution},
  year={2026},
  url={https://github.com/Sathira-Institution/uagf-ckm},
  note={Canonical Knowledge Infrastructure for Interoperable AI Governance}
}
```

---

# Roadmap

## Alpha

- ✅ Canonical Knowledge Model
- ✅ Kernel Validation
- ✅ Migration Pipeline
- ✅ Rendering Engine
- ✅ JSON-LD

## Beta

- ⬜ Reference Verification
- ⬜ RDF Export
- ⬜ REST API
- ⬜ Public Registry
- ⬜ Governance Profiles

## Stable

- ⬜ CKM 2.0
- ⬜ Long-Term Governance
- ⬜ Community Contributions
- ⬜ International Crosswalk Library

---

# Acknowledgements

UAGF is developed as an open public-good initiative by **Sathira Institution**.

Our goal is to make trustworthy AI governance knowledge openly available, interoperable, and machine-readable for the benefit of the global community.


