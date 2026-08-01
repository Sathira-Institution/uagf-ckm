**UAGF-002**	Canonical Knowledge Registry

**UNIFIED AI GOVERNANCE FRAMEWORK**

*UAGF Knowledge Series*

**UAGF-002**

**Canonical Knowledge Registry**

The Unified Governance Requirement (UGR) Registry, Taxonomy, and Crosswalk Mappings of the UAGF Ecosystem

| **Version 1.0  ·  PUBLIC RELEASE** *The canonical source of truth for all UAGF governance requirements — 30 Unified Governance Requirements across 10 Governance Domains.* |
| --- |

**Developed by SATHIRA Institution**

Original Author: Apichai Chuensuang

Contributors: UAGF Working Group (Open Contribution)

Published July 2026  ·  Licensed under CC BY 4.0

## **Document Control**

| **Field** | **Detail** |
| --- | --- |
| **Document Code** | UAGF-002 |
| **Title** | Canonical Knowledge Registry |
| **Version** | 1.0 |
| **Classification** | Public Framework Document |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Series** | UAGF Knowledge Series |
| **Developed By** | SATHIRA Institution |
| **Original Author** | Apichai Chuensuang |
| **Contributors** | UAGF Working Group (Open Contribution) |
| **Publication Date** | July 2026 |
| **Status** | PUBLIC RELEASE |
| **Companion Documents** | UAGF-001 (Foundations), UAGF-003 (Governance Framework) |

| **NOTE: **Language Edition: International Edition (English only), in accordance with UAGF-DOC-001 §7.2. This edition is intended for international audiences and is therefore exempt from the default Thai-primary bilingual convention (§7.1). |
| --- |

# **0.  ****Preface**

The Unified AI Governance Framework (UAGF) is built on a simple but powerful idea: governance requirements from different sources can be translated into a single, unified language that everyone can understand and use.

This document — UAGF-002 — is the canonical knowledge backbone of the entire UAGF ecosystem. It contains the complete registry of Unified Governance Requirements (UGRs), the taxonomy of governance concepts, and the crosswalk mappings that connect requirements to their original sources.

Consider this document the "source of truth" for UAGF. When UAGF-003 (Governance Framework) references a requirement, or UAGF-004 (Reference Patterns) applies a control, they are all referencing the same canonical definitions contained here.

This document is designed to be:

- Machine-readable — structured for integration with governance systems

- Human-readable — clear definitions and examples for practitioners

- Traceable — every requirement links back to its original source

- Versioned — changes are tracked and documented

The framework is published under Creative Commons BY 4.0, ensuring it remains a public benefit resource for generations to come.

### **0.1  Normative vs. Informative Classification**

This document distinguishes between two types of content:

| **Type** | **Description** | **Example** |
| --- | --- | --- |
| **[Normative] Requirements** | Content that constitutes the mandatory requirements of the UAGF framework. Organizations claiming conformance with UAGF must comply with these. | UGR Registry, Taxonomy Structure, Crosswalk Methodology |
| **[Informative] Descriptions** | Content that provides examples, additional explanations, or implementation guidance to help understand the requirements, but is not mandatory. | Application examples, illustrations, Rationale |

| **NOTE: **All content labeled [Normative] uses requirement language (SHALL, SHOULD, MAY) as standardized in UAGF-DOC-001 §10. Content labeled [Informative] uses descriptive language. |
| --- |

### **0.2  Positioning Statement**

UAGF is an independent, vendor-neutral, and technology-agnostic governance methodology.

This document — UAGF-002 — is the canonical knowledge registry that contains the unified requirements, taxonomy, and crosswalk mappings that underpin the entire UAGF ecosystem. It does not replace laws, regulations, standards, audits, or certification schemes.

Its purpose is to provide a single source of truth for all governance requirements, enabling organizations, regulators, and technology providers to reference the same canonical definitions.

UAGF is a public benefit initiative. No commercial interest, vendor, or product governs its content. Any organization, any system, and any framework can reference UAGF-002 without locking into any specific technology or provider.

# **1.  ****Scope  [Normative]**

### **1.1  Scope Statement**

This document provides the complete canonical knowledge registry of the Unified AI Governance Framework (UAGF). It contains:

- The complete UGR Registry (Unified Governance Requirements) with all fields and definitions

- The Taxonomy Registry defining all governance concepts and their relationships

- The Crosswalk Mapping connecting UGRs to their original sources (laws, standards, principles)

- The Traceability Framework enabling end-to-end tracking from source to implementation

This document is the authoritative reference for all UAGF requirements and definitions.

This document does NOT:

- Replace legal advice, regulatory interpretation, or certification schemes

- Provide technology-specific implementation guidance (see UAGF-005)

- Define assessment methodology or maturity models (see UAGF-003)

- Offer implementation patterns or reference architecture (see UAGF-004, UAGF-005)

### **1.2  Out of Scope  [Normative]**

The following areas are explicitly outside the scope of this document:

| **ID** | **Topic** | **Rationale** |
| --- | --- | --- |
| **UAGF-OOS-007** | Implementation Guidance | This document defines requirements; implementation guidance is in UAGF-005. |
| **UAGF-OOS-008** | Maturity Assessment | Assessment methodology is in UAGF-003. |
| **UAGF-OOS-009** | Sector-Specific Patterns | Sector patterns are in UAGF-004. |
| **UAGF-OOS-010** | Technology-Specific Mappings | UAGF is technology-agnostic. |

# **2.  ****Intended Audience  [Informative]**

This document is intended for:

| **Sector / Role** | **How They Use This Document** |
| --- | --- |
| **Governance Architects** | Reference for canonical requirements when designing governance frameworks |
| **Compliance Officers** | Source of truth for regulatory requirements mapping |
| **System Integrators** | Reference for building governance-enabled systems that reference UGRs |
| **Standards Developers** | Reference for aligning new standards with the UAGF taxonomy |
| **Auditors** | Reference for traceability verification |
| **Technology Providers** | Reference for UGR-compatible system design |

# **3.  ****UAGF Knowledge Series Roadmap  [Informative]**

The UAGF Knowledge Series consists of five core documents:

| **UAGF-001  ·  Foundations** Why the world needs systematic AI governance |
| --- |

**↓**

| **UAGF-002  ·  Canonical Knowledge Registry** UGR Registry · Taxonomy · Crosswalk · Traceability   ← YOU ARE HERE |
| --- |

**↓**

| **UAGF-003  ·  Governance Framework** Assessment · Controls · Conformance · Maturity · Domains |
| --- |

**↓**

| **UAGF-004  ·  Reference Patterns** Government · Healthcare · Finance · SME · GenAI |
| --- |

**↓**

| **UAGF-005  ·  Implementation Guide** Architecture · Roadmap · Governance Lifecycle |
| --- |

**Figure 1 — ****UAGF Knowledge Series Roadmap**

# **4.  ****The Unified Governance Requirement (UGR)  [Normative]**

### **4.1  What Is a UGR?**

A Unified Governance Requirement (UGR) is the canonical unit of governance within UAGF. Every governance requirement collected from laws, standards, principles, or guidance is translated into one canonical requirement that is referenced throughout the UAGF ecosystem.

Key characteristics of a UGR:

| **Characteristic** | **Description** |
| --- | --- |
| **Canonical** | One stable, versioned identifier for each requirement |
| **Traceable** | Links back to all original sources |
| **Actionable** | Clear, plain-language statement that is implementable |
| **Consistent** | Same concept, same definition, across all documents |

### **4.2  UGR ID Format  [Normative]**

| **UGR-XXXX** |
| --- |

| **Element** | **Description** | **Example** |
| --- | --- | --- |
| **UGR** | Unified Governance Requirement | UGR |
| **XXXX** | 4-digit sequential number (0001–9999) | 0015 |

| **EXAMPLE: **UGR-0015 — "AI systems must undergo human review before consequential decisions are executed." |
| --- |

### **4.3  UGR Record Structure  [Normative]**

Every UGR in the registry SHALL have the following fields:

| **Field** | **Description** | **Required** |
| --- | --- | --- |
| **UGR ID** | Canonical requirement identifier | Yes |
| **Title** | Short, descriptive name | Yes |
| **Statement** | Clear, actionable requirement in plain language | Yes |
| **Requirement Type** | Legal / Standard / Principle / Guideline / Best Practice | Yes |
| **Applicability** | Which organizations/systems this applies to | Yes |
| **Lifecycle Stage** | Design / Development / Deployment / Operation / Decommission | Yes |
| **Priority** | Critical / High / Medium / Low | Yes |
| **Risk Category** | Human Rights / Safety / Privacy / Security / Fairness / Transparency | Yes |
| **Primary Domain** | Which of the 10 Governance Domains applies | Yes |
| **Sources** | Original source documents with specific references | Yes |
| **Intent** | Why this requirement exists | Yes |
| **Expected Evidence** | What must be produced to demonstrate compliance | Yes |
| **Related Controls** | Organizational controls that address this requirement | Yes |
| **Cross References** | Related UGRs | No |
| **Implementation Guidance** | How to implement (generic, vendor-neutral) | Yes |
| **Automation Potential** | High / Medium / Low / None | No |
| **Status** | Active / Deprecated / Under Review | Yes |
| **Revision History** | Version, Date, Author, Change Description | No |

# **5.  ****UGR Registry — Complete Requirements List  [Normative]**

This section contains the complete registry of 30 Unified Governance Requirements (UGRs), organized into 10 Governance Domains. Every UGR follows the canonical record structure defined in Section 4.3.

## **Category 1: Governance ****&**** Leadership (DOM-GOV)**

### **UGR-001 — AI Governance Ownership**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-001 |
| **Title** | AI Governance Ownership |
| **Statement** | The organization must designate a person or function with overall accountability for AI governance, including policy development, risk oversight, and compliance monitoring. |
| **Requirement Type** | Standard / Legal |
| **Applicability** | All organizations that develop, deploy, or operate AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Governance |
| **Primary Domain** | DOM-GOV |
| **Sources** | ISO/IEC 42001, Clause 5.3; EU AI Act, Article 26; PDPA Thailand, Section 41 |
| **Intent** | Ensure clear ownership and accountability for AI governance across the organization. |
| **Expected Evidence** | AI governance role description, assignment documentation, org chart showing AI governance structure, meeting minutes of governance reviews |
| **Related Controls** | AI Policy Framework, Top Management Commitment, Governance Roles and Responsibilities |
| **Cross References** | UGR-002, UGR-003, UGR-015 |
| **Implementation Guidance** | 1. Define AI governance role with documented responsibilities; 2. Assign to an accountable individual or committee; 3. Include in job descriptions and performance objectives; 4. Document the assignment; 5. Review annually |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-002 — AI Policy Framework**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-002 |
| **Title** | AI Policy Framework |
| **Statement** | The organization must establish, document, and maintain an AI policy that defines governance principles, risk tolerance, ethical commitments, and compliance requirements for AI systems. |
| **Requirement Type** | Standard |
| **Applicability** | All organizations that develop, deploy, or operate AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Governance |
| **Primary Domain** | DOM-GOV |
| **Sources** | ISO/IEC 42001, Clause 5.2; EU AI Act, Article 26; OECD AI Principles |
| **Intent** | Provide a formal, documented foundation for AI governance that communicates organizational commitments and expectations. |
| **Expected Evidence** | Approved AI policy document, communication records, training completion records, policy review records |
| **Related Controls** | AI Governance Ownership, Top Management Commitment, Policy Communication and Training |
| **Cross References** | UGR-001, UGR-004 |
| **Implementation Guidance** | 1. Draft AI policy with input from legal, risk, and technical stakeholders; 2. Obtain executive approval; 3. Publish and communicate to all relevant staff; 4. Review and update annually; 5. Document version history |
| **Automation Potential** | Low |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-003 — Top Management Commitment**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-003 |
| **Title** | Top Management Commitment |
| **Statement** | Top management must demonstrate commitment to AI governance by approving the AI policy, allocating resources, and regularly reviewing AI governance performance. |
| **Requirement Type** | Standard |
| **Applicability** | All organizations that develop, deploy, or operate AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Governance |
| **Primary Domain** | DOM-GOV |
| **Sources** | ISO/IEC 42001, Clause 5.1; EU AI Act, Article 26 |
| **Intent** | Ensure AI governance has executive-level support and resources to be effective. |
| **Expected Evidence** | Executive meeting minutes, approved resource allocation documents, governance review reports, signed policy approval |
| **Related Controls** | AI Governance Ownership, AI Policy Framework, Governance Review Cadence |
| **Cross References** | UGR-001, UGR-002 |
| **Implementation Guidance** | 1. Schedule regular AI governance reviews at executive level; 2. Include AI governance in board or management reporting; 3. Document resource allocation decisions; 4. Maintain meeting minutes; 5. Track governance KPIs |
| **Automation Potential** | Low |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-004 — AI Governance Roles and Responsibilities**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-004 |
| **Title** | AI Governance Roles and Responsibilities |
| **Statement** | The organization must define and document roles, responsibilities, and authorities for AI governance, including who is accountable for AI system decisions, risk management, and compliance. |
| **Requirement Type** | Standard / Legal |
| **Applicability** | All organizations that develop, deploy, or operate AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Governance, Accountability |
| **Primary Domain** | DOM-GOV |
| **Sources** | ISO/IEC 42001, Clause 5.3; EU AI Act, Article 26; PDPA Thailand, Section 41 |
| **Intent** | Ensure clear accountability for AI-related decisions and activities across the organization. |
| **Expected Evidence** | RACI matrix, role descriptions, org chart, accountability assignment records |
| **Related Controls** | Human Oversight, Accountability Chain, Access Control |
| **Cross References** | UGR-001, UGR-015, UGR-045 |
| **Implementation Guidance** | 1. Map AI governance roles to organizational structure; 2. Document responsibilities in RACI matrices; 3. Communicate roles to all relevant personnel; 4. Include in training programs; 5. Review and update annually |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 2: Risk Management (DOM-RISK)**

### **UGR-005 — AI Risk Management System**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-005 |
| **Title** | AI Risk Management System |
| **Statement** | The organization must establish, implement, and maintain a risk management system for AI systems that identifies, analyzes, evaluates, treats, and monitors AI-related risks throughout the AI system lifecycle. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations deploying high-risk AI systems; all organizations with AI systems |
| **Lifecycle Stage** | Design, Development, Deployment, Operation |
| **Priority** | Critical |
| **Risk Category** | Safety, Human Rights, Governance |
| **Primary Domain** | DOM-RISK |
| **Sources** | EU AI Act, Article 9; ISO/IEC 42001, Clause 6.1; NIST AI RMF, Govern Function |
| **Intent** | Ensure systematic identification and management of AI risks from design through deployment and operation. |
| **Expected Evidence** | Risk assessment methodology document, completed risk assessments, risk treatment plans, risk monitoring records, risk review meeting minutes |
| **Related Controls** | Risk Assessment, Risk Treatment, Risk Monitoring, Risk Review |
| **Cross References** | UGR-006, UGR-007 |
| **Implementation Guidance** | 1. Define AI risk assessment methodology; 2. Conduct risk assessments for all AI systems; 3. Document risk treatment plans; 4. Monitor risks continuously; 5. Review and update assessments regularly |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-006 — AI Risk Classification**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-006 |
| **Title** | AI Risk Classification |
| **Statement** | The organization must classify each AI system according to its risk level, considering the potential impact on health, safety, fundamental rights, and organizational objectives. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations that deploy AI systems |
| **Lifecycle Stage** | Design, Development, Pre-deployment |
| **Priority** | High |
| **Risk Category** | Safety, Human Rights, Governance |
| **Primary Domain** | DOM-RISK |
| **Sources** | EU AI Act, Article 6; ISO/IEC 42001, Clause 6.1; NIST AI RMF |
| **Intent** | Enable proportionate governance by matching controls to risk level. |
| **Expected Evidence** | Risk classification criteria document, classification records per AI system, classification review records |
| **Related Controls** | Risk Assessment, Proportional Controls, Risk-based Approval |
| **Cross References** | UGR-005, UGR-015 |
| **Implementation Guidance** | 1. Define risk classification criteria; 2. Assess each AI system against criteria; 3. Assign risk tier (e.g., Low/Medium/High/Critical); 4. Document classification decisions; 5. Review classifications periodically |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-007 — AI Impact Assessment**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-007 |
| **Title** | AI Impact Assessment |
| **Statement** | The organization must conduct impact assessments for high-risk AI systems to evaluate potential effects on individuals, communities, and organizational operations before deployment. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations deploying high-risk AI systems |
| **Lifecycle Stage** | Development, Pre-deployment |
| **Priority** | High |
| **Risk Category** | Human Rights, Safety, Privacy |
| **Primary Domain** | DOM-RISK |
| **Sources** | EU AI Act, Article 26; ISO/IEC 42001, Clause 6.1; NIST AI RMF |
| **Intent** | Identify and mitigate potential negative impacts before AI systems are deployed. |
| **Expected Evidence** | Completed impact assessments, mitigation plans, approval records, review records |
| **Related Controls** | Risk Assessment, Privacy Impact Assessment, Human Rights Impact Assessment |
| **Cross References** | UGR-005, UGR-006 |
| **Implementation Guidance** | 1. Define impact assessment methodology; 2. Conduct assessments for high-risk AI systems; 3. Document findings and mitigation measures; 4. Review and update assessments |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 3: Human Oversight (DOM-HUMAN)**

### **UGR-015 — Human Oversight for High-Risk AI**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-015 |
| **Title** | Human Oversight for High-Risk AI |
| **Statement** | High-risk AI systems must be designed and operated in a way that enables effective human oversight, including the ability for humans to intervene, override, or stop the system when necessary. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations deploying high-risk AI systems |
| **Lifecycle Stage** | Design, Development, Operation |
| **Priority** | Critical |
| **Risk Category** | Human Rights, Safety, Accountability |
| **Primary Domain** | DOM-HUMAN |
| **Sources** | EU AI Act, Article 14; ISO/IEC 42001, Clause 8; OECD AI Principles |
| **Intent** | Ensure human judgment remains the final authority for consequential AI decisions, preventing full automation of decisions with significant impact. |
| **Expected Evidence** | Human oversight design documentation, approval workflow definitions, human review logs, override records |
| **Related Controls** | Human Oversight Control, Approval Workflow, Human Intervention Mechanism |
| **Cross References** | UGR-004, UGR-016, UGR-017, UGR-045 |
| **Implementation Guidance** | 1. Identify decision points requiring human review; 2. Define approval workflows; 3. Assign responsible human authorities; 4. Log all review decisions; 5. Maintain audit trail |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-016 — Human Approval Workflow**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-016 |
| **Title** | Human Approval Workflow |
| **Statement** | The organization must establish documented approval workflows for AI system decisions, specifying who must approve which types of decisions, under what conditions, and within what timeframe. |
| **Requirement Type** | Standard |
| **Applicability** | All organizations with AI systems that make consequential decisions |
| **Lifecycle Stage** | Design, Development, Operation |
| **Priority** | High |
| **Risk Category** | Accountability, Governance |
| **Primary Domain** | DOM-HUMAN |
| **Sources** | ISO/IEC 42001, Clause 8; EU AI Act, Article 14 |
| **Intent** | Ensure decisions of consequence are routed through a documented, accountable approval process before execution. |
| **Expected Evidence** | Approval workflow documentation, approval records, escalation logs, workflow review records |
| **Related Controls** | Approval Workflow, Human Oversight Control, Escalation Procedure |
| **Cross References** | UGR-015, UGR-017, UGR-045 |
| **Implementation Guidance** | 1. Identify decisions requiring approval; 2. Define approvers and conditions; 3. Document timeframes and escalation paths; 4. Implement workflow tooling; 5. Review workflow effectiveness periodically |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-017 — Human Intervention Mechanism**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-017 |
| **Title** | Human Intervention Mechanism |
| **Statement** | The organization must implement mechanisms that allow authorized human operators to intervene, override, or halt AI system actions in real time when necessary to prevent harm or correct erroneous behavior. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations deploying high-risk AI systems |
| **Lifecycle Stage** | Design, Development, Operation |
| **Priority** | Critical |
| **Risk Category** | Human Rights, Safety, Accountability |
| **Primary Domain** | DOM-HUMAN |
| **Sources** | EU AI Act, Article 14; ISO/IEC 42001, Clause 8 |
| **Intent** | Ensure humans can stop or correct AI actions when necessary. |
| **Expected Evidence** | Intervention mechanism design documentation, intervention procedure documents, training completion records, intervention logs |
| **Related Controls** | Human Oversight Control, Emergency Stop, Rollback Procedure |
| **Cross References** | UGR-015, UGR-045 |
| **Implementation Guidance** | 1. Design intervention mechanisms; 2. Document intervention procedures; 3. Train operators; 4. Log all interventions; 5. Review intervention effectiveness |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 4: Data Governance (DOM-DATA)**

### **UGR-020 — Data Quality for AI Systems**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-020 |
| **Title** | Data Quality for AI Systems |
| **Statement** | The organization must ensure that data used for training, validation, and operation of AI systems is of sufficient quality, including accuracy, completeness, relevance, and representativeness for the intended use. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations that develop or operate AI systems |
| **Lifecycle Stage** | Development, Training, Operation |
| **Priority** | High |
| **Risk Category** | Fairness, Safety, Privacy |
| **Primary Domain** | DOM-DATA |
| **Sources** | EU AI Act, Article 10; ISO/IEC 42001, Annex A (Data Integrity); PDPA Thailand, Section 23 |
| **Intent** | Prevent AI system errors and biases caused by poor quality data. |
| **Expected Evidence** | Data quality criteria documentation, data quality assessment reports, remediation records, data quality monitoring logs |
| **Related Controls** | Data Quality Control, Data Validation, Data Monitoring |
| **Cross References** | UGR-021, UGR-022 |
| **Implementation Guidance** | 1. Define data quality criteria; 2. Implement data quality checks; 3. Document data quality assessments; 4. Address quality issues; 5. Monitor data quality continuously |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-021 — Data Lineage and Provenance**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-021 |
| **Title** | Data Lineage and Provenance |
| **Statement** | The organization must maintain data lineage records that track the origin, transformation, and flow of data used in AI systems from source to consumption, enabling traceability and auditability. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations that develop or operate AI systems |
| **Lifecycle Stage** | Development, Training, Operation |
| **Priority** | High |
| **Risk Category** | Privacy, Fairness, Auditability |
| **Primary Domain** | DOM-DATA |
| **Sources** | EU AI Act, Article 10; ISO/IEC 42001, Annex A (Data Integrity); NIST AI RMF |
| **Intent** | Enable traceability of data used in AI systems for audit, compliance, and error investigation. |
| **Expected Evidence** | Data lineage records, data flow diagrams, transformation logs, lineage verification records |
| **Related Controls** | Data Tracking, Data Provenance, Audit Logging |
| **Cross References** | UGR-020, UGR-035, UGR-036 |
| **Implementation Guidance** | 1. Document data sources; 2. Track data transformations; 3. Maintain lineage records; 4. Include lineage in audit trails; 5. Verify lineage accuracy |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-022 — Data Classification for AI Systems**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-022 |
| **Title** | Data Classification for AI Systems |
| **Statement** | The organization must classify data used in AI systems according to sensitivity, regulatory requirements, and risk, and apply appropriate controls based on classification. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations that process data through AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Privacy, Security |
| **Primary Domain** | DOM-DATA |
| **Sources** | PDPA Thailand, Section 23; ISO/IEC 42001, Annex A (Privacy); NIST AI RMF |
| **Intent** | Ensure appropriate protection for data based on sensitivity and regulatory requirements. |
| **Expected Evidence** | Data classification schema, classification assignments, control implementation records, classification review records |
| **Related Controls** | Data Protection, Access Control, Data Handling Procedures |
| **Cross References** | UGR-020, UGR-030, UGR-031 |
| **Implementation Guidance** | 1. Define data classification schema; 2. Classify data used in AI systems; 3. Apply controls based on classification; 4. Document classification decisions; 5. Review classifications periodically |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 5: Transparency (DOM-TRANSPARENCY)**

### **UGR-025 — AI System Disclosure**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-025 |
| **Title** | AI System Disclosure |
| **Statement** | Users must be informed when they are interacting with an AI system, including the nature and purpose of the system, in a clear and understandable manner. |
| **Requirement Type** | Legal / Principle |
| **Applicability** | All organizations with user-facing AI systems |
| **Lifecycle Stage** | Operation |
| **Priority** | High |
| **Risk Category** | Transparency, Human Rights |
| **Primary Domain** | DOM-TRANSPARENCY |
| **Sources** | EU AI Act, Article 50; OECD AI Principles; UNESCO Recommendation on the Ethics of AI |
| **Intent** | Ensure users are aware they are interacting with AI and can make informed decisions about their engagement. |
| **Expected Evidence** | Disclosure mechanism implementation records, user awareness verification, disclosure policy documents |
| **Related Controls** | Transparency Control, User Notification, Consent Management |
| **Cross References** | UGR-026, UGR-027 |
| **Implementation Guidance** | 1. Identify all user-facing AI systems; 2. Design disclosure mechanisms; 3. Implement disclosures; 4. Verify user awareness; 5. Monitor compliance |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-026 — Synthetic Content Labeling**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-026 |
| **Title** | Synthetic Content Labeling |
| **Statement** | AI-generated synthetic content (including text, images, audio, and video) must be clearly labeled as AI-generated or AI-manipulated in a machine-readable and human-readable format. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations that generate synthetic content using AI |
| **Lifecycle Stage** | Operation |
| **Priority** | High |
| **Risk Category** | Transparency, Disinformation |
| **Primary Domain** | DOM-TRANSPARENCY |
| **Sources** | EU AI Act, Article 50; C2PA Standard |
| **Intent** | Prevent deception by ensuring users can identify AI-generated content. |
| **Expected Evidence** | Labeling implementation records, content labeling examples, integrity verification records |
| **Related Controls** | Content Labeling, Provenance Tracking, Integrity Verification |
| **Cross References** | UGR-025, UGR-027 |
| **Implementation Guidance** | 1. Implement content labeling mechanisms; 2. Use standard formats (e.g., C2PA); 3. Label all synthetic content; 4. Verify labeling integrity; 5. Include labeling in audit trails |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-027 — Deepfake Disclosure**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-027 |
| **Title** | Deepfake Disclosure |
| **Statement** | Deepfake content (AI-generated or manipulated image, audio, or video that resembles real persons or events) must be clearly disclosed as artificially generated or manipulated. |
| **Requirement Type** | Legal |
| **Applicability** | Organizations that generate or distribute deepfake content |
| **Lifecycle Stage** | Operation |
| **Priority** | High |
| **Risk Category** | Transparency, Disinformation, Human Rights |
| **Primary Domain** | DOM-TRANSPARENCY |
| **Sources** | EU AI Act, Article 50(4); EU AI Act, Article 3(66) |
| **Intent** | Prevent misinformation and deception through realistic synthetic media. |
| **Expected Evidence** | Deepfake detection records, disclosure labels, disclosure event logs, compliance monitoring records |
| **Related Controls** | Content Labeling, Deepfake Detection, Disclosure Management |
| **Cross References** | UGR-025, UGR-026 |
| **Implementation Guidance** | 1. Detect deepfake content; 2. Apply disclosure labels; 3. Ensure labels are visible and understandable; 4. Log disclosure events; 5. Monitor for compliance |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 6: Auditability (DOM-AUDITABILITY)**

### **UGR-035 — AI System Logging**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-035 |
| **Title** | AI System Logging |
| **Statement** | AI systems must log all material decisions, actions, and events, including inputs, outputs, decision rationale, and human interventions, in a format suitable for audit and review. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations with AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | Critical |
| **Risk Category** | Auditability, Accountability |
| **Primary Domain** | DOM-AUDITABILITY |
| **Sources** | EU AI Act, Article 12; ISO/IEC 42001, Clause 8; NIST AI RMF |
| **Intent** | Enable audit, investigation, and continuous improvement through complete records of AI system behavior. |
| **Expected Evidence** | Logging policy, log records, log retrieval test results, log integrity verification records |
| **Related Controls** | Audit Logging Control, Log Retention, Log Integrity |
| **Cross References** | UGR-036, UGR-037, UGR-045 |
| **Implementation Guidance** | 1. Define logging requirements; 2. Implement logging mechanisms; 3. Ensure logs are immutable; 4. Retain logs per policy; 5. Test log retrieval |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-036 — Audit Trail Retention**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-036 |
| **Title** | Audit Trail Retention |
| **Statement** | The organization must retain audit trails for AI systems for a defined retention period (minimum 5 years for high-risk systems) in a tamper-evident format that supports retrieval and replay. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations with AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Auditability, Compliance |
| **Primary Domain** | DOM-AUDITABILITY |
| **Sources** | EU AI Act, Article 12; ISO/IEC 42001, Clause 8; PDPA Thailand, Section 23 |
| **Intent** | Ensure evidence is available for audits, investigations, and regulatory reviews. |
| **Expected Evidence** | Retention policy document, retention implementation records, retrieval test results, retention compliance reports |
| **Related Controls** | Log Retention, Data Archiving, Evidence Management |
| **Cross References** | UGR-035, UGR-037, UGR-045 |
| **Implementation Guidance** | 1. Define retention periods by risk tier; 2. Implement tamper-evident storage; 3. Test retrieval; 4. Verify integrity; 5. Document retention policies |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-037 — Audit Trail Retrieval**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-037 |
| **Title** | Audit Trail Retrieval |
| **Statement** | The organization must be able to retrieve audit trails for AI systems upon request from authorized parties (auditors, regulators, data subjects) within a reasonable timeframe. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations with AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Auditability, Compliance |
| **Primary Domain** | DOM-AUDITABILITY |
| **Sources** | EU AI Act, Article 12; ISO/IEC 42001, Clause 8; PDPA Thailand, Sections 30-36 |
| **Intent** | Enable timely response to audit and regulatory requests. |
| **Expected Evidence** | Retrieval procedure documentation, retrieval test results, response time records, retrieval request logs |
| **Related Controls** | Log Retrieval, Audit Response, Data Access |
| **Cross References** | UGR-035, UGR-036 |
| **Implementation Guidance** | 1. Design retrieval mechanisms; 2. Test retrieval regularly; 3. Define response SLAs; 4. Document retrieval procedures; 5. Train staff |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 7: Accountability (DOM-ACCOUNTABILITY)**

### **UGR-045 — Human Accountability for AI Outcomes**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-045 |
| **Title** | Human Accountability for AI Outcomes |
| **Statement** | The organization must ensure that every consequential AI decision has a clearly identified human accountable for the outcome, with documented responsibility and authority. |
| **Requirement Type** | Legal / Standard / Principle |
| **Applicability** | All organizations with AI systems that make consequential decisions |
| **Lifecycle Stage** | All stages |
| **Priority** | Critical |
| **Risk Category** | Accountability, Human Rights |
| **Primary Domain** | DOM-ACCOUNTABILITY |
| **Sources** | EU AI Act, Article 14; ISO/IEC 42001, Clause 5.3; OECD AI Principles |
| **Intent** | Maintain human responsibility for AI outcomes, preventing accountability gaps. |
| **Expected Evidence** | Accountability assignment records, accountability documentation, training records, incident review records |
| **Related Controls** | Human Oversight Control, Accountability Chain, Incident Management |
| **Cross References** | UGR-001, UGR-004, UGR-015, UGR-016 |
| **Implementation Guidance** | 1. Map AI decisions to accountable humans; 2. Document accountability assignments; 3. Include in approval workflows; 4. Log accountability records; 5. Review assignments regularly |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 8: Security (DOM-SECURITY)**

### **UGR-050 — AI System Security**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-050 |
| **Title** | AI System Security |
| **Statement** | AI systems must be protected against unauthorized access, manipulation, and misuse through appropriate security controls, including access control, encryption, and monitoring. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | All organizations with AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Security |
| **Primary Domain** | DOM-SECURITY |
| **Sources** | EU AI Act, Article 15; ISO/IEC 42001, Annex A (Security); NIST AI RMF |
| **Intent** | Prevent security breaches that could compromise AI system integrity, confidentiality, or availability. |
| **Expected Evidence** | Security control implementation records, security assessment results, incident response records, monitoring logs |
| **Related Controls** | Access Control, Encryption, Security Monitoring, Incident Response |
| **Cross References** | UGR-051, UGR-052 |
| **Implementation Guidance** | 1. Conduct security risk assessments; 2. Implement security controls; 3. Monitor security events; 4. Test security regularly; 5. Respond to incidents |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-051 — AI System Security Testing**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-051 |
| **Title** | AI System Security Testing |
| **Statement** | AI systems must be tested for security vulnerabilities before deployment and periodically during operation, with findings documented and remediated. |
| **Requirement Type** | Standard |
| **Applicability** | All organizations with AI systems |
| **Lifecycle Stage** | Development, Pre-deployment, Operation |
| **Priority** | Medium |
| **Risk Category** | Security |
| **Primary Domain** | DOM-SECURITY |
| **Sources** | EU AI Act, Article 15; ISO/IEC 42001, Annex A (Security); NIST AI RMF |
| **Intent** | Identify and remediate security vulnerabilities before they can be exploited. |
| **Expected Evidence** | Security testing reports, vulnerability remediation records, testing schedule, penetration test results |
| **Related Controls** | Vulnerability Management, Security Testing, Penetration Testing |
| **Cross References** | UGR-050, UGR-052 |
| **Implementation Guidance** | 1. Define security testing requirements; 2. Conduct pre-deployment testing; 3. Schedule periodic testing; 4. Document findings; 5. Remediate vulnerabilities |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 9: Privacy (DOM-PRIVACY)**

### **UGR-060 — Lawful Basis for Personal Data Processing**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-060 |
| **Title** | Lawful Basis for Personal Data Processing |
| **Statement** | The organization must establish and document a lawful basis for all processing of personal data by AI systems, including consent, contract, legal obligation, vital interest, public task, or legitimate interest. |
| **Requirement Type** | Legal |
| **Applicability** | Organizations processing personal data through AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | Critical |
| **Risk Category** | Privacy, Human Rights |
| **Primary Domain** | DOM-PRIVACY |
| **Sources** | PDPA Thailand, Section 24; EU AI Act, Article 10; ISO/IEC 42001, Annex A (Privacy) |
| **Intent** | Ensure all personal data processing by AI systems has a valid legal foundation. |
| **Expected Evidence** | Lawful basis documentation, privacy notices, consent records (if applicable), processing activity records |
| **Related Controls** | Data Protection Impact Assessment, Privacy Notice, Consent Management |
| **Cross References** | UGR-061, UGR-062, UGR-064 |
| **Implementation Guidance** | 1. Map AI data processing to lawful bases; 2. Document lawful bases; 3. Review periodically; 4. Include in privacy notices; 5. Maintain records |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-061 — Data Subject Rights**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-061 |
| **Title** | Data Subject Rights |
| **Statement** | The organization must support data subject rights in AI systems, including the right to access, correct, delete, restrict processing, object, and data portability, with documented procedures and response timelines. |
| **Requirement Type** | Legal |
| **Applicability** | Organizations processing personal data through AI systems |
| **Lifecycle Stage** | Operation |
| **Priority** | High |
| **Risk Category** | Privacy, Human Rights |
| **Primary Domain** | DOM-PRIVACY |
| **Sources** | PDPA Thailand, Sections 30-36; ISO/IEC 42001, Annex A (Privacy) |
| **Intent** | Protect individual rights regarding personal data processed by AI systems. |
| **Expected Evidence** | Rights request procedures, request response records, response time monitoring, training records |
| **Related Controls** | Data Subject Request Management, Privacy Rights, Access Control |
| **Cross References** | UGR-060, UGR-062, UGR-064 |
| **Implementation Guidance** | 1. Map data subject rights to AI systems; 2. Define response procedures; 3. Implement request mechanisms; 4. Train staff; 5. Monitor response times |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-062 — Data Protection Impact Assessment**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-062 |
| **Title** | Data Protection Impact Assessment |
| **Statement** | The organization must conduct Data Protection Impact Assessments (DPIAs) for AI systems that process personal data, particularly where processing is likely to result in high risk to individuals' rights and freedoms. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations processing personal data through AI systems |
| **Lifecycle Stage** | Design, Development, Pre-deployment |
| **Priority** | High |
| **Risk Category** | Privacy |
| **Primary Domain** | DOM-PRIVACY |
| **Sources** | PDPA Thailand, Section 23; ISO/IEC 42001, Clause 6; NIST AI RMF |
| **Intent** | Identify and mitigate privacy risks before AI systems process personal data. |
| **Expected Evidence** | DPIA documentation, mitigation records, approval records, review records |
| **Related Controls** | Privacy Impact Assessment, Risk Assessment, Data Protection |
| **Cross References** | UGR-060, UGR-061, UGR-064 |
| **Implementation Guidance** | 1. Define DPIA methodology; 2. Conduct DPIAs for high-risk AI systems; 3. Document findings; 4. Implement mitigations; 5. Review periodically |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-063 — Sensitive Data Protection**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-063 |
| **Title** | Sensitive Data Protection |
| **Statement** | The organization must apply enhanced protections for sensitive personal data (e.g., health data, biometric data, racial or ethnic origin, political opinions, religious beliefs) processed by AI systems, including explicit consent where required. |
| **Requirement Type** | Legal |
| **Applicability** | Organizations processing sensitive personal data through AI systems |
| **Lifecycle Stage** | All stages |
| **Priority** | High |
| **Risk Category** | Privacy, Human Rights |
| **Primary Domain** | DOM-PRIVACY |
| **Sources** | PDPA Thailand, Section 26; EU AI Act, Article 10; ISO/IEC 42001, Annex A (Privacy) |
| **Intent** | Ensure enhanced protection for sensitive data that carries higher privacy risk. |
| **Expected Evidence** | Sensitive data identification records, enhanced control implementation, consent records, monitoring logs |
| **Related Controls** | Data Classification, Enhanced Data Protection, Consent Management |
| **Cross References** | UGR-060, UGR-061 |
| **Implementation Guidance** | 1. Identify sensitive data; 2. Apply enhanced controls; 3. Obtain explicit consent where required; 4. Document processing; 5. Monitor compliance |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-064 — Privacy Impact Assessment**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-064 |
| **Title** | Privacy Impact Assessment |
| **Statement** | The organization must conduct privacy impact assessments for AI systems that process personal data, evaluating privacy risks and implementing appropriate mitigations before deployment. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations processing personal data through AI systems |
| **Lifecycle Stage** | Design, Development, Pre-deployment |
| **Priority** | High |
| **Risk Category** | Privacy |
| **Primary Domain** | DOM-PRIVACY |
| **Sources** | PDPA Thailand, Section 23; ISO/IEC 42001, Clause 6; NIST AI RMF |
| **Intent** | Systematically identify and address privacy risks in AI systems. |
| **Expected Evidence** | PIA documentation, mitigation records, approval records, review records |
| **Related Controls** | Data Protection Impact Assessment, Risk Assessment, Data Protection |
| **Cross References** | UGR-060, UGR-061, UGR-062 |
| **Implementation Guidance** | 1. Define PIA methodology; 2. Conduct PIAs for AI systems; 3. Document findings; 4. Implement mitigations; 5. Review periodically |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

## **Category 10: Safety (DOM-SAFETY)**

### **UGR-070 — AI System Safety Testing**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-070 |
| **Title** | AI System Safety Testing |
| **Statement** | AI systems must be tested for safety before deployment, including testing for harmful outputs, unintended behaviors, and failure modes, with results documented and reviewed. |
| **Requirement Type** | Legal / Standard |
| **Applicability** | Organizations deploying AI systems |
| **Lifecycle Stage** | Development, Pre-deployment |
| **Priority** | High |
| **Risk Category** | Safety |
| **Primary Domain** | DOM-SAFETY |
| **Sources** | EU AI Act, Article 15; ISO/IEC 42001, Clause 8; NIST AI RMF |
| **Intent** | Prevent harm from AI system failures or unintended behaviors. |
| **Expected Evidence** | Safety testing records, test reports, remediation records, approval records |
| **Related Controls** | Safety Testing, Safety Monitoring, Risk Assessment |
| **Cross References** | UGR-071, UGR-072 |
| **Implementation Guidance** | 1. Define safety testing requirements; 2. Conduct pre-deployment testing; 3. Document results; 4. Review findings; 5. Remediate issues |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-071 — Safety Thresholds and Monitoring**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-071 |
| **Title** | Safety Thresholds and Monitoring |
| **Statement** | The organization must define safety thresholds for AI system behavior and continuously monitor system performance against these thresholds during operation. |
| **Requirement Type** | Standard |
| **Applicability** | Organizations deploying AI systems |
| **Lifecycle Stage** | Operation |
| **Priority** | High |
| **Risk Category** | Safety |
| **Primary Domain** | DOM-SAFETY |
| **Sources** | EU AI Act, Article 15; ISO/IEC 42001, Clause 8; NIST AI RMF |
| **Intent** | Detect and respond to unsafe AI system behavior during operation. |
| **Expected Evidence** | Safety threshold documentation, monitoring records, alert records, incident records |
| **Related Controls** | Safety Monitoring, Alerting, Incident Response |
| **Cross References** | UGR-070, UGR-072 |
| **Implementation Guidance** | 1. Define safety thresholds; 2. Implement monitoring; 3. Configure alerts; 4. Document incidents; 5. Review thresholds periodically |
| **Automation Potential** | High |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

### **UGR-072 — AI System Rollback and Suspension**

| **Field** | **Value** |
| --- | --- |
| **UGR ID** | UGR-072 |
| **Title** | AI System Rollback and Suspension |
| **Statement** | The organization must have documented procedures to suspend or roll back AI systems when unsafe behavior is detected, with clear authority and escalation paths. |
| **Requirement Type** | Standard |
| **Applicability** | Organizations deploying AI systems |
| **Lifecycle Stage** | Operation |
| **Priority** | High |
| **Risk Category** | Safety |
| **Primary Domain** | DOM-SAFETY |
| **Sources** | EU AI Act, Article 15; ISO/IEC 42001, Clause 8; NIST AI RMF |
| **Intent** | Enable rapid response to unsafe AI system behavior. |
| **Expected Evidence** | Rollback/suspension procedures, exercise records, incident records, authority assignment records |
| **Related Controls** | Incident Response, Emergency Procedures, Rollback Capability |
| **Cross References** | UGR-070, UGR-071 |
| **Implementation Guidance** | 1. Define rollback/suspension procedures; 2. Assign authority; 3. Test procedures; 4. Document exercises; 5. Review and update |
| **Automation Potential** | Medium |
| **Status** | Active |
| **Revision History** | v1.0 (2026-06-28, UAGF WG, Initial creation) |

# **6.  ****UGR Registry Summary  [Informative]**

The table below summarizes the distribution of the 30 Unified Governance Requirements across the 10 Governance Domains.

| **Domain** | **UGR ID Range** | **Count** |
| --- | --- | --- |
| **Governance ****&**** Leadership (DOM-GOV)** | UGR-001 to UGR-004 | 4 |
| **Risk Management (DOM-RISK)** | UGR-005 to UGR-007 | 3 |
| **Human Oversight (DOM-HUMAN)** | UGR-015 to UGR-017 | 3 |
| **Data Governance (DOM-DATA)** | UGR-020 to UGR-022 | 3 |
| **Transparency (DOM-TRANSPARENCY)** | UGR-025 to UGR-027 | 3 |
| **Auditability (DOM-AUDITABILITY)** | UGR-035 to UGR-037 | 3 |
| **Accountability (DOM-ACCOUNTABILITY)** | UGR-045 | 1 |
| **Security (DOM-SECURITY)** | UGR-050 to UGR-051 | 2 |
| **Privacy (DOM-PRIVACY)** | UGR-060 to UGR-064 | 5 |
| **Safety (DOM-SAFETY)** | UGR-070 to UGR-072 | 3 |

**Total: 30 Unified Governance Requirements across 10 Governance Domains.**

# **7.  ****Crosswalk Mapping  [Informative]**

The crosswalk tables below map each UGR back to the specific clauses and articles of major external sources, providing bidirectional traceability between UAGF and existing laws and standards.

### **7.1  EU AI Act Coverage**

| **EU AI Act Article** | **Description** | **Related UGRs** |
| --- | --- | --- |
| **Article 6** | Classification of high-risk AI systems | UGR-006 |
| **Article 9** | Risk management system | UGR-005 |
| **Article 10** | Data and data governance | UGR-020, UGR-021 |
| **Article 12** | Record-keeping and logging | UGR-035, UGR-036, UGR-037 |
| **Article 14** | Human oversight | UGR-015, UGR-016, UGR-017 |
| **Article 15** | Accuracy, robustness, and cybersecurity | UGR-050, UGR-051, UGR-070, UGR-071, UGR-072 |
| **Article 26** | Obligations of deployers | UGR-001, UGR-004, UGR-007 |
| **Article 50** | Transparency obligations | UGR-025, UGR-026, UGR-027 |

### **7.2  ISO/IEC 42001 Coverage**

| **ISO/IEC 42001 Clause** | **Description** | **Related UGRs** |
| --- | --- | --- |
| **Clause 5.1** | Leadership and commitment | UGR-003 |
| **Clause 5.2** | Policy | UGR-002 |
| **Clause 5.3** | Organizational roles, responsibilities, and authorities | UGR-001, UGR-004 |
| **Clause 6.1** | Actions to address risks and opportunities | UGR-005, UGR-006, UGR-007, UGR-062, UGR-064 |
| **Clause 8** | Operation | UGR-015, UGR-016, UGR-017, UGR-035, UGR-070, UGR-071, UGR-072 |
| **Annex A** | Controls | UGR-020, UGR-021, UGR-022, UGR-050, UGR-060, UGR-061, UGR-063 |

### **7.3  Thailand PDPA Coverage**

| **PDPA Section** | **Description** | **Related UGRs** |
| --- | --- | --- |
| **Section 23** | Data protection impact assessment | UGR-036, UGR-062, UGR-064 |
| **Section 24** | Lawful basis for processing | UGR-060 |
| **Section 26** | Sensitive personal data | UGR-063 |
| **Sections 30–36** | Data subject rights | UGR-037, UGR-061 |
| **Section 41** | Data Protection Officer | UGR-001, UGR-004 |

# **8.  ****Traceability Framework  [Normative]**

### **8.1  Traceability Chain**

Every UGR in the registry SHALL maintain traceability to its original sources. The traceability chain is:

| **ORIGINAL SOURCE** Law · Standard · Principle |
| --- |

**↓**

| **UGR STATEMENT** |
| --- |

**↓**

| **PRIMARY DOMAIN** |
| --- |

**↓**

| **RELATED CONTROLS** |
| --- |

**↓**

| **IMPLEMENTATION GUIDANCE** |
| --- |

**↓**

| **EXPECTED EVIDENCE** |
| --- |

**Figure 2 — ****UGR Traceability Chain**

### **8.2  Traceability Requirements  [Normative]**

| **Requirement ID** | **Description** |
| --- | --- |
| **UGR-TRACE-001** | Every UGR SHALL reference at least one original source document. |
| **UGR-TRACE-002** | Every UGR SHALL reference a Primary Domain. |
| **UGR-TRACE-003** | Every UGR SHALL have Implementation Guidance that can be traced to the original requirement. |
| **UGR-TRACE-004** | Expected Evidence SHALL be directly linked to the UGR statement. |
| **UGR-TRACE-005** | Cross References SHALL connect related UGRs. |

# **9.  ****Revision History**

| **Version** | **Date** | **Author** | **Change Description** |
| --- | --- | --- | --- |
| **v1.0** | 2026-07-04 | Apichai Chuensuang | Initial public release — PUBLIC RELEASE |

# **10.  ****Glossary**

This glossary defines the canonical terms used throughout this registry. All UAGF documents SHALL use these definitions consistently.

| **Term** | **Definition** |
| --- | --- |
| **Crosswalk** | A mapping that shows the relationship between UGRs and their original sources (laws, standards, principles). |
| **Cross-Reference** | A link from one UGR to another related UGR. |
| **Implementation Guidance** | Practical, vendor-neutral steps for implementing a UGR. |
| **Lifecycle Stage** | The stage of AI system development to which a UGR applies (Design, Development, Deployment, Operation, Decommission). |
| **Priority** | The relative importance of a UGR (Critical, High, Medium, Low). |
| **Requirement Type** | The nature of the requirement (Legal, Standard, Principle, Guideline, Best Practice). |
| **Risk Category** | The type of risk addressed (Human Rights, Safety, Privacy, Security, Fairness, Transparency). |
| **Traceability** | The ability to link a UGR back to its original source and forward to its implementation guidance and expected evidence. |
| **UGR Registry** | The complete collection of all Unified Governance Requirements. |

# **11.  ****Contact ****&**** License**

| **Contact** | **Detail** |
| --- | --- |
| **Developed By** | SATHIRA Institution |
| **Original Author** | Apichai Chuensuang |
| **Document** | UAGF-002 · Version 1.0 · Public Framework |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Website** | uagf.synapsa.ai (Open Contribution Portal) |

### **License ****&**** Copyright**

This document is published under Creative Commons Attribution 4.0 International (CC BY 4.0). You are free to share and adapt the material for any purpose, even commercially, provided you give appropriate credit.

| **RECOMMENDATION: **Recommended Attribution: "UAGF-002 Canonical Knowledge Registry" by Apichai Chuensuang, SATHIRA Institution, is licensed under Creative Commons Attribution 4.0 International. |
| --- |

**© 2026 SATHIRA Institution · Original Author: Apichai Chuensuang · CC BY 4.0**

*This document is published for public benefit. No commercial entity controls its content.*

		Version 1.0	PUBLIC RELEASE  ·  CC BY 4.0	Page  of