# UAGF v2.0 — Canonical Knowledge Model

**Universal AI Governance Knowledge Infrastructure**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Alpha](https://img.shields.io/badge/Status-Alpha-orange)](https://github.com/Sathira-Institution/uagf-ckm)
[![Build Status](https://github.com/Sathira-Institution/uagf-ckm/actions/workflows/ci.yml/badge.svg)](https://github.com/Sathira-Institution/uagf-ckm/actions)

---

## 🌍 What is UAGF?

UAGF (Universal AI Governance Framework) is a **Canonical Knowledge Infrastructure** for AI governance that enables interoperability across international standards, national regulations, and organizational policies through a common governance language.

> **UAGF does not replace standards. It connects them.**  
> **UAGF does not replace regulations. It translates them.**  
> **UAGF does not replace governance frameworks. It enables them to interoperate.**

### Core Principles

- **Open by Design** — Public benefit, CC BY 4.0 licensed
- **Evidence over Assumption** — Reality First approach
- **Vendor & Origin Neutral** — No preference for any technology or region
- **AI-Native** — Machine-readable by design (JSON-LD, RDF, YAML)
- **Interoperable** — Connects ISO, NIST, EU AI Act, PDPA, and more

---

##  What's in This Repository?

This repository contains the **CKM 2.0.0-Alpha** release:

- **`ckm/`** — Canonical Knowledge Model (source of truth)
  - `requirements/` — UGR (Unified Governance Requirements) in YAML
  - `domains/` — Governance Domains (11 total)
  - `references/` — External References (EU AI Act, ISO 42001, etc.)
  - `cv/` — Controlled Vocabularies (enums as first-class objects)
  
- **`ckm-staging/`** — Migration staging area (pre-ratification)
- **`generated/`** — Rendered artifacts (Markdown, JSON, JSON-LD)
- **`tests/`** — Automated test suite (E2E regression tests)
- **`reports/`** — Validation and migration reports

### Key Tools

- `migrate_ckm.py` — Migration runner (legacy → CKM)
- `validate_ckm.py` — Schema validator (K-1 to K-8 invariants)
- `render_ckm.py` — Multi-format renderer (doc/json/jsonld/ai-context)
- `manifest.yaml` — Migration configuration (WP-005)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PyYAML (`pip install pyyaml`)

### 1. Validate the CKM

```bash
python validate_ckm.py --ckm-dir ckm
