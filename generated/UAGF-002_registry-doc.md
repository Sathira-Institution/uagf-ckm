# UAGF-002 — Canonical Knowledge Registry (Rendered View)

*Rendered from CKM — profile=registry-doc · ckm_release=2.0.0-staging · render_date=2026-07-28 · engine=uagf-renderer/0.1*

*This artifact is a disposable render. Truth lives in the Canonical Knowledge Model.*

## Accountability (DOM-ACCOUNTABILITY)

### UGR-045 — Human Accountability for AI Outcomes  [Normative]

The organization must ensure that every consequential AI decision has a clearly identified human accountable for the outcome, with documented responsibility and authority.

**Intent.** Maintain human responsibility for AI outcomes, preventing accountability gaps.

| Field | Value |
|---|---|
| Requirement Type | legal, standard, principle |
| Applicability | All organizations with AI systems that make consequential decisions |
| Lifecycle Stages | all-stages |
| Priority | critical |
| Risk Categories | accountability, human-rights |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 14) [pending-verification]; REF-ISO42001 (Clause 5.3) [pending-verification]; REF-OECD-AIP [pending-verification] |
| See also (informative) | UGR-001, UGR-004, UGR-015, UGR-016 |
| Expected Evidence | Accountability assignment records, accountability documentation, training records, incident review records |
| Related Controls | Human Oversight Control, Accountability Chain, Incident Management |

**Implementation Guidance**
1. Map AI decisions to accountable humans
2. Document accountability assignments
3. Include in approval workflows
4. Log accountability records
5. Review assignments regularly

## Auditability (DOM-AUDITABILITY)

### UGR-035 — AI System Logging  [Normative]

AI systems must log all material decisions, actions, and events, including inputs, outputs, decision rationale, and human interventions, in a format suitable for audit and review.

**Intent.** Enable audit, investigation, and continuous improvement through complete records of AI system behavior.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations with AI systems |
| Lifecycle Stages | all-stages |
| Priority | critical |
| Risk Categories | auditability, accountability |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 12) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-036, UGR-037, UGR-045 |
| Expected Evidence | Logging policy, log records, log retrieval test results, log integrity verification records |
| Related Controls | Audit Logging Control, Log Retention, Log Integrity |

**Implementation Guidance**
1. Define logging requirements
2. Implement logging mechanisms
3. Ensure logs are immutable
4. Retain logs per policy
5. Test log retrieval

### UGR-036 — Audit Trail Retention  [Normative]

The organization must retain audit trails for AI systems for a defined retention period (minimum 5 years for high-risk systems) in a tamper-evident format that supports retrieval and replay.

**Intent.** Ensure evidence is available for audits, investigations, and regulatory reviews.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations with AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | auditability, compliance |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 12) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification]; REF-TH-PDPA (Section 23) [pending-verification] |
| See also (informative) | UGR-035, UGR-037, UGR-045 |
| Expected Evidence | Retention policy document, retention implementation records, retrieval test results, retention compliance reports |
| Related Controls | Log Retention, Data Archiving, Evidence Management |

**Implementation Guidance**
1. Define retention periods by risk tier
2. Implement tamper-evident storage
3. Test retrieval
4. Verify integrity
5. Document retention policies

### UGR-037 — Audit Trail Retrieval  [Normative]

The organization must be able to retrieve audit trails for AI systems upon request from authorized parties (auditors, regulators, data subjects) within a reasonable timeframe.

**Intent.** Enable timely response to audit and regulatory requests.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations with AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | auditability, compliance |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 12) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification]; REF-TH-PDPA (Sections 30-36) [pending-verification] |
| See also (informative) | UGR-035, UGR-036 |
| Expected Evidence | Retrieval procedure documentation, retrieval test results, response time records, retrieval request logs |
| Related Controls | Log Retrieval, Audit Response, Data Access |

**Implementation Guidance**
1. Design retrieval mechanisms
2. Test retrieval regularly
3. Define response SLAs
4. Document retrieval procedures
5. Train staff

## Data Governance (DOM-DATA)

### UGR-020 — Data Quality for AI Systems  [Normative]

The organization must ensure that data used for training, validation, and operation of AI systems is of sufficient quality, including accuracy, completeness, relevance, and representativeness for the intended use.

**Intent.** Prevent AI system errors and biases caused by poor quality data.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations that develop or operate AI systems |
| Lifecycle Stages | development, operation |
| Priority | high |
| Risk Categories | fairness, safety, privacy |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 10) [pending-verification]; REF-ISO42001 (Annex A (Data Integrity)) [pending-verification]; REF-TH-PDPA (Section 23) [pending-verification] |
| See also (informative) | UGR-021, UGR-022 |
| Expected Evidence | Data quality criteria documentation, data quality assessment reports, remediation records, data quality monitoring logs |
| Related Controls | Data Quality Control, Data Validation, Data Monitoring |

**Implementation Guidance**
1. Define data quality criteria
2. Implement data quality checks
3. Document data quality assessments
4. Address quality issues
5. Monitor data quality continuously

### UGR-021 — Data Lineage and Provenance  [Normative]

The organization must maintain data lineage records that track the origin, transformation, and flow of data used in AI systems from source to consumption, enabling traceability and auditability.

**Intent.** Enable traceability of data used in AI systems for audit, compliance, and error investigation.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations that develop or operate AI systems |
| Lifecycle Stages | development, operation |
| Priority | high |
| Risk Categories | privacy, fairness, auditability |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 10) [pending-verification]; REF-ISO42001 (Annex A (Data Integrity)) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-020, UGR-035, UGR-036 |
| Expected Evidence | Data lineage records, data flow diagrams, transformation logs, lineage verification records |
| Related Controls | Data Tracking, Data Provenance, Audit Logging |

**Implementation Guidance**
1. Document data sources
2. Track data transformations
3. Maintain lineage records
4. Include lineage in audit trails
5. Verify lineage accuracy

### UGR-022 — Data Classification for AI Systems  [Normative]

The organization must classify data used in AI systems according to sensitivity, regulatory requirements, and risk, and apply appropriate controls based on classification.

**Intent.** Ensure appropriate protection for data based on sensitivity and regulatory requirements.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations that process data through AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | privacy, security |
| Automation Potential | high |
| Derived from | REF-TH-PDPA (Section 23) [pending-verification]; REF-ISO42001 (Annex A (Privacy)) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-020 |
| Expected Evidence | Data classification schema, classification assignments, control implementation records, classification review records |
| Related Controls | Data Protection, Access Control, Data Handling Procedures |

**Implementation Guidance**
1. Define data classification schema
2. Classify data used in AI systems
3. Apply controls based on classification
4. Document classification decisions
5. Review classifications periodically

## Governance & Leadership (DOM-GOV)

### UGR-001 — AI Governance Ownership  [Normative]

The organization must designate a person or function with overall accountability for AI governance, including policy development, risk oversight, and compliance monitoring.

**Intent.** Ensure clear ownership and accountability for AI governance across the organization.

| Field | Value |
|---|---|
| Requirement Type | standard, legal |
| Applicability | All organizations that develop, deploy, or operate AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | governance |
| Automation Potential | medium |
| Derived from | REF-ISO42001 (Clause 5.3) [pending-verification]; REF-EUAIA (Article 26) [pending-verification]; REF-TH-PDPA (Section 41) [pending-verification] |
| See also (informative) | UGR-002, UGR-003, UGR-015 |
| Expected Evidence | AI governance role description, assignment documentation, org chart showing AI governance structure, meeting minutes of governance reviews |
| Related Controls | AI Policy Framework, Top Management Commitment, Governance Roles and Responsibilities |

**Implementation Guidance**
1. Define AI governance role with documented responsibilities
2. Assign to an accountable individual or committee
3. Include in job descriptions and performance objectives
4. Document the assignment
5. Review annually

### UGR-002 — AI Policy Framework  [Normative]

The organization must establish, document, and maintain an AI policy that defines governance principles, risk tolerance, ethical commitments, and compliance requirements for AI systems.

**Intent.** Provide a formal, documented foundation for AI governance that communicates organizational commitments and expectations.

| Field | Value |
|---|---|
| Requirement Type | standard |
| Applicability | All organizations that develop, deploy, or operate AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | governance |
| Automation Potential | low |
| Derived from | REF-ISO42001 (Clause 5.2) [pending-verification]; REF-EUAIA (Article 26) [pending-verification]; REF-OECD-AIP [pending-verification] |
| See also (informative) | UGR-001, UGR-004 |
| Expected Evidence | Approved AI policy document, communication records, training completion records, policy review records |
| Related Controls | AI Governance Ownership, Top Management Commitment, Policy Communication and Training |

**Implementation Guidance**
1. Draft AI policy with input from legal, risk, and technical stakeholders
2. Obtain executive approval
3. Publish and communicate to all relevant staff
4. Review and update annually
5. Document version history

### UGR-003 — Top Management Commitment  [Normative]

Top management must demonstrate commitment to AI governance by approving the AI policy, allocating resources, and regularly reviewing AI governance performance.

**Intent.** Ensure AI governance has executive-level support and resources to be effective.

| Field | Value |
|---|---|
| Requirement Type | standard |
| Applicability | All organizations that develop, deploy, or operate AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | governance |
| Automation Potential | low |
| Derived from | REF-ISO42001 (Clause 5.1) [pending-verification]; REF-EUAIA (Article 26) [pending-verification] |
| See also (informative) | UGR-001, UGR-002 |
| Expected Evidence | Executive meeting minutes, approved resource allocation documents, governance review reports, signed policy approval |
| Related Controls | AI Governance Ownership, AI Policy Framework, Governance Review Cadence |

**Implementation Guidance**
1. Schedule regular AI governance reviews at executive level
2. Include AI governance in board or management reporting
3. Document resource allocation decisions
4. Maintain meeting minutes
5. Track governance KPIs

### UGR-004 — AI Governance Roles and Responsibilities  [Normative]

The organization must define and document roles, responsibilities, and authorities for AI governance, including who is accountable for AI system decisions, risk management, and compliance.

**Intent.** Ensure clear accountability for AI-related decisions and activities across the organization.

| Field | Value |
|---|---|
| Requirement Type | standard, legal |
| Applicability | All organizations that develop, deploy, or operate AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | governance, accountability |
| Automation Potential | medium |
| Derived from | REF-ISO42001 (Clause 5.3) [pending-verification]; REF-EUAIA (Article 26) [pending-verification]; REF-TH-PDPA (Section 41) [pending-verification] |
| See also (informative) | UGR-001, UGR-015, UGR-045 |
| Expected Evidence | RACI matrix, role descriptions, org chart, accountability assignment records |
| Related Controls | Human Oversight, Accountability Chain, Access Control |

**Implementation Guidance**
1. Map AI governance roles to organizational structure
2. Document responsibilities in RACI matrices
3. Communicate roles to all relevant personnel
4. Include in training programs
5. Review and update annually

## Human Oversight (DOM-HUMAN)

### UGR-015 — Human Oversight for High-Risk AI  [Normative]

High-risk AI systems must be designed and operated in a way that enables effective human oversight, including the ability for humans to intervene, override, or stop the system when necessary.

**Intent.** Ensure human judgment remains the final authority for consequential AI decisions, preventing full automation of decisions with significant impact.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations deploying high-risk AI systems |
| Lifecycle Stages | design, development, operation |
| Priority | critical |
| Risk Categories | human-rights, safety, accountability |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 14) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification]; REF-OECD-AIP [pending-verification] |
| See also (informative) | UGR-004, UGR-016, UGR-017, UGR-045 |
| Expected Evidence | Human oversight design documentation, approval workflow definitions, human review logs, override records |
| Related Controls | Human Oversight Control, Approval Workflow, Human Intervention Mechanism |

**Implementation Guidance**
1. Identify decision points requiring human review
2. Define approval workflows
3. Assign responsible human authorities
4. Log all review decisions
5. Maintain audit trail

### UGR-016 — Human Approval Workflow  [Normative]

The organization must establish documented approval workflows for AI system decisions, specifying who must approve which types of decisions, under what conditions, and within what timeframe.

**Intent.** Ensure decisions of consequence are routed through a documented, accountable approval process before execution.

| Field | Value |
|---|---|
| Requirement Type | standard |
| Applicability | All organizations with AI systems that make consequential decisions |
| Lifecycle Stages | design, development, operation |
| Priority | high |
| Risk Categories | accountability, governance |
| Automation Potential | medium |
| Derived from | REF-ISO42001 (Clause 8) [pending-verification]; REF-EUAIA (Article 14) [pending-verification] |
| See also (informative) | UGR-015, UGR-017, UGR-045 |
| Expected Evidence | Approval workflow documentation, approval records, escalation logs, workflow review records |
| Related Controls | Approval Workflow, Human Oversight Control, Escalation Procedure |

**Implementation Guidance**
1. Identify decisions requiring approval
2. Define approvers and conditions
3. Document timeframes and escalation paths
4. Implement workflow tooling
5. Review workflow effectiveness periodically

### UGR-017 — Human Intervention Mechanism  [Normative]

The organization must implement mechanisms that allow authorized human operators to intervene, override, or halt AI system actions in real time when necessary to prevent harm or correct erroneous behavior.

**Intent.** Ensure humans can stop or correct AI actions when necessary.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations deploying high-risk AI systems |
| Lifecycle Stages | design, development, operation |
| Priority | critical |
| Risk Categories | human-rights, safety, accountability |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 14) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification] |
| See also (informative) | UGR-015, UGR-045 |
| Expected Evidence | Intervention mechanism design documentation, intervention procedure documents, training completion records, intervention logs |
| Related Controls | Human Oversight Control, Emergency Stop, Rollback Procedure |

**Implementation Guidance**
1. Design intervention mechanisms
2. Document intervention procedures
3. Train operators
4. Log all interventions
5. Review intervention effectiveness

## Privacy (DOM-PRIVACY)

### UGR-060 — Lawful Basis for Personal Data Processing  [Normative]

The organization must establish and document a lawful basis for all processing of personal data by AI systems, including consent, contract, legal obligation, vital interest, public task, or legitimate interest.

**Intent.** Ensure all personal data processing by AI systems has a valid legal foundation.

| Field | Value |
|---|---|
| Requirement Type | legal |
| Applicability | Organizations processing personal data through AI systems |
| Lifecycle Stages | all-stages |
| Priority | critical |
| Risk Categories | privacy, human-rights |
| Automation Potential | medium |
| Derived from | REF-TH-PDPA (Section 24) [pending-verification]; REF-EUAIA (Article 10) [pending-verification]; REF-ISO42001 (Annex A (Privacy)) [pending-verification] |
| See also (informative) | UGR-061, UGR-062, UGR-064 |
| Expected Evidence | Lawful basis documentation, privacy notices, consent records (if applicable), processing activity records |
| Related Controls | Data Protection Impact Assessment, Privacy Notice, Consent Management |

**Implementation Guidance**
1. Map AI data processing to lawful bases
2. Document lawful bases
3. Review periodically
4. Include in privacy notices
5. Maintain records

### UGR-061 — Data Subject Rights  [Normative]

The organization must support data subject rights in AI systems, including the right to access, correct, delete, restrict processing, object, and data portability, with documented procedures and response timelines.

**Intent.** Protect individual rights regarding personal data processed by AI systems.

| Field | Value |
|---|---|
| Requirement Type | legal |
| Applicability | Organizations processing personal data through AI systems |
| Lifecycle Stages | operation |
| Priority | high |
| Risk Categories | privacy, human-rights |
| Automation Potential | high |
| Derived from | REF-TH-PDPA (Sections 30-36) [pending-verification]; REF-ISO42001 (Annex A (Privacy)) [pending-verification] |
| See also (informative) | UGR-060, UGR-062, UGR-064 |
| Expected Evidence | Rights request procedures, request response records, response time monitoring, training records |
| Related Controls | Data Subject Request Management, Privacy Rights, Access Control |

**Implementation Guidance**
1. Map data subject rights to AI systems
2. Define response procedures
3. Implement request mechanisms
4. Train staff
5. Monitor response times

### UGR-062 — Data Protection Impact Assessment  [Normative]

The organization must conduct Data Protection Impact Assessments (DPIAs) for AI systems that process personal data, particularly where processing is likely to result in high risk to individuals' rights and freedoms.

**Intent.** Identify and mitigate privacy risks before AI systems process personal data.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations processing personal data through AI systems |
| Lifecycle Stages | design, development, deployment |
| Priority | high |
| Risk Categories | privacy |
| Automation Potential | medium |
| Derived from | REF-TH-PDPA (Section 23) [pending-verification]; REF-ISO42001 (Clause 6) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-060, UGR-061, UGR-064 |
| Expected Evidence | DPIA documentation, mitigation records, approval records, review records |
| Related Controls | Privacy Impact Assessment, Risk Assessment, Data Protection |

**Implementation Guidance**
1. Define DPIA methodology
2. Conduct DPIAs for high-risk AI systems
3. Document findings
4. Implement mitigations
5. Review periodically

### UGR-063 — Sensitive Data Protection  [Normative]

The organization must apply enhanced protections for sensitive personal data (e.g., health data, biometric data, racial or ethnic origin, political opinions, religious beliefs) processed by AI systems, including explicit consent where required.

**Intent.** Ensure enhanced protection for sensitive data that carries higher privacy risk.

| Field | Value |
|---|---|
| Requirement Type | legal |
| Applicability | Organizations processing sensitive personal data through AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | privacy, human-rights |
| Automation Potential | high |
| Derived from | REF-TH-PDPA (Section 26) [pending-verification]; REF-EUAIA (Article 10) [pending-verification]; REF-ISO42001 (Annex A (Privacy)) [pending-verification] |
| See also (informative) | UGR-060, UGR-061 |
| Expected Evidence | Sensitive data identification records, enhanced control implementation, consent records, monitoring logs |
| Related Controls | Data Classification, Enhanced Data Protection, Consent Management |

**Implementation Guidance**
1. Identify sensitive data
2. Apply enhanced controls
3. Obtain explicit consent where required
4. Document processing
5. Monitor compliance

### UGR-064 — Privacy Impact Assessment  [Normative]

The organization must conduct privacy impact assessments for AI systems that process personal data, evaluating privacy risks and implementing appropriate mitigations before deployment.

**Intent.** Systematically identify and address privacy risks in AI systems.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations processing personal data through AI systems |
| Lifecycle Stages | design, development, deployment |
| Priority | high |
| Risk Categories | privacy |
| Automation Potential | medium |
| Derived from | REF-TH-PDPA (Section 23) [pending-verification]; REF-ISO42001 (Clause 6) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-060, UGR-061, UGR-062 |
| Expected Evidence | PIA documentation, mitigation records, approval records, review records |
| Related Controls | Data Protection Impact Assessment, Risk Assessment, Data Protection |

**Implementation Guidance**
1. Define PIA methodology
2. Conduct PIAs for AI systems
3. Document findings
4. Implement mitigations
5. Review periodically

## Risk Management (DOM-RISK)

### UGR-005 — AI Risk Management System  [Normative]

The organization must establish, implement, and maintain a risk management system for AI systems that identifies, analyzes, evaluates, treats, and monitors AI-related risks throughout the AI system lifecycle.

**Intent.** Ensure systematic identification and management of AI risks from design through deployment and operation.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations deploying high-risk AI systems; all organizations with AI systems |
| Lifecycle Stages | design, development, deployment, operation |
| Priority | critical |
| Risk Categories | safety, human-rights, governance |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 9) [pending-verification]; REF-ISO42001 (Clause 6.1) [pending-verification]; REF-NIST-AIRMF (Govern Function) [pending-verification] |
| See also (informative) | UGR-006, UGR-007 |
| Expected Evidence | Risk assessment methodology document, completed risk assessments, risk treatment plans, risk monitoring records, risk review meeting minutes |
| Related Controls | Risk Assessment, Risk Treatment, Risk Monitoring, Risk Review |

**Implementation Guidance**
1. Define AI risk assessment methodology
2. Conduct risk assessments for all AI systems
3. Document risk treatment plans
4. Monitor risks continuously
5. Review and update assessments regularly

### UGR-006 — AI Risk Classification  [Normative]

The organization must classify each AI system according to its risk level, considering the potential impact on health, safety, fundamental rights, and organizational objectives.

**Intent.** Enable proportionate governance by matching controls to risk level.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations that deploy AI systems |
| Lifecycle Stages | design, development, deployment |
| Priority | high |
| Risk Categories | safety, human-rights, governance |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 6) [pending-verification]; REF-ISO42001 (Clause 6.1) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-005, UGR-015 |
| Expected Evidence | Risk classification criteria document, classification records per AI system, classification review records |
| Related Controls | Risk Assessment, Proportional Controls, Risk-based Approval |

**Implementation Guidance**
1. Define risk classification criteria
2. Assess each AI system against criteria
3. Assign risk tier (e.g., Low/Medium/High/Critical)
4. Document classification decisions
5. Review classifications periodically

### UGR-007 — AI Impact Assessment  [Normative]

The organization must conduct impact assessments for high-risk AI systems to evaluate potential effects on individuals, communities, and organizational operations before deployment.

**Intent.** Identify and mitigate potential negative impacts before AI systems are deployed.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations deploying high-risk AI systems |
| Lifecycle Stages | development, deployment |
| Priority | high |
| Risk Categories | human-rights, safety, privacy |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 26) [pending-verification]; REF-ISO42001 (Clause 6.1) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-005, UGR-006 |
| Expected Evidence | Completed impact assessments, mitigation plans, approval records, review records |
| Related Controls | Risk Assessment, Privacy Impact Assessment, Human Rights Impact Assessment |

**Implementation Guidance**
1. Define impact assessment methodology
2. Conduct assessments for high-risk AI systems
3. Document findings and mitigation measures
4. Review and update assessments

## Safety (DOM-SAFETY)

### UGR-070 — AI System Safety Testing  [Normative]

AI systems must be tested for safety before deployment, including testing for harmful outputs, unintended behaviors, and failure modes, with results documented and reviewed.

**Intent.** Prevent harm from AI system failures or unintended behaviors.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations deploying AI systems |
| Lifecycle Stages | development, deployment |
| Priority | high |
| Risk Categories | safety |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 15) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-071, UGR-072 |
| Expected Evidence | Safety testing records, test reports, remediation records, approval records |
| Related Controls | Safety Testing, Safety Monitoring, Risk Assessment |

**Implementation Guidance**
1. Define safety testing requirements
2. Conduct pre-deployment testing
3. Document results
4. Review findings
5. Remediate issues

### UGR-071 — Safety Thresholds and Monitoring  [Normative]

The organization must define safety thresholds for AI system behavior and continuously monitor system performance against these thresholds during operation.

**Intent.** Detect and respond to unsafe AI system behavior during operation.

| Field | Value |
|---|---|
| Requirement Type | standard |
| Applicability | Organizations deploying AI systems |
| Lifecycle Stages | operation |
| Priority | high |
| Risk Categories | safety |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 15) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-070, UGR-072 |
| Expected Evidence | Safety threshold documentation, monitoring records, alert records, incident records |
| Related Controls | Safety Monitoring, Alerting, Incident Response |

**Implementation Guidance**
1. Define safety thresholds
2. Implement monitoring
3. Configure alerts
4. Document incidents
5. Review thresholds periodically

### UGR-072 — AI System Rollback and Suspension  [Normative]

The organization must have documented procedures to suspend or roll back AI systems when unsafe behavior is detected, with clear authority and escalation paths.

**Intent.** Enable rapid response to unsafe AI system behavior.

| Field | Value |
|---|---|
| Requirement Type | standard |
| Applicability | Organizations deploying AI systems |
| Lifecycle Stages | operation |
| Priority | high |
| Risk Categories | safety |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 15) [pending-verification]; REF-ISO42001 (Clause 8) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-070, UGR-071 |
| Expected Evidence | Rollback/suspension procedures, exercise records, incident records, authority assignment records |
| Related Controls | Incident Response, Emergency Procedures, Rollback Capability |

**Implementation Guidance**
1. Define rollback/suspension procedures
2. Assign authority
3. Test procedures
4. Document exercises
5. Review and update

## Security (DOM-SECURITY)

### UGR-050 — AI System Security  [Normative]

AI systems must be protected against unauthorized access, manipulation, and misuse through appropriate security controls, including access control, encryption, and monitoring.

**Intent.** Prevent security breaches that could compromise AI system integrity, confidentiality, or availability.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | All organizations with AI systems |
| Lifecycle Stages | all-stages |
| Priority | high |
| Risk Categories | security |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 15) [pending-verification]; REF-ISO42001 (Annex A (Security)) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-051 |
| Expected Evidence | Security control implementation records, security assessment results, incident response records, monitoring logs |
| Related Controls | Access Control, Encryption, Security Monitoring, Incident Response |

**Implementation Guidance**
1. Conduct security risk assessments
2. Implement security controls
3. Monitor security events
4. Test security regularly
5. Respond to incidents

### UGR-051 — AI System Security Testing  [Normative]

AI systems must be tested for security vulnerabilities before deployment and periodically during operation, with findings documented and remediated.

**Intent.** Identify and remediate security vulnerabilities before they can be exploited.

| Field | Value |
|---|---|
| Requirement Type | standard |
| Applicability | All organizations with AI systems |
| Lifecycle Stages | development, deployment, operation |
| Priority | medium |
| Risk Categories | security |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 15) [pending-verification]; REF-ISO42001 (Annex A (Security)) [pending-verification]; REF-NIST-AIRMF [pending-verification] |
| See also (informative) | UGR-050 |
| Expected Evidence | Security testing reports, vulnerability remediation records, testing schedule, penetration test results |
| Related Controls | Vulnerability Management, Security Testing, Penetration Testing |

**Implementation Guidance**
1. Define security testing requirements
2. Conduct pre-deployment testing
3. Schedule periodic testing
4. Document findings
5. Remediate vulnerabilities

## Transparency (DOM-TRANSPARENCY)

### UGR-025 — AI System Disclosure  [Normative]

Users must be informed when they are interacting with an AI system, including the nature and purpose of the system, in a clear and understandable manner.

**Intent.** Ensure users are aware they are interacting with AI and can make informed decisions about their engagement.

| Field | Value |
|---|---|
| Requirement Type | legal, principle |
| Applicability | All organizations with user-facing AI systems |
| Lifecycle Stages | operation |
| Priority | high |
| Risk Categories | transparency, human-rights |
| Automation Potential | medium |
| Derived from | REF-EUAIA (Article 50) [pending-verification]; REF-OECD-AIP [pending-verification]; REF-UNESCO-RECOMMENDATION-ON [pending-verification] |
| See also (informative) | UGR-026, UGR-027 |
| Expected Evidence | Disclosure mechanism implementation records, user awareness verification, disclosure policy documents |
| Related Controls | Transparency Control, User Notification, Consent Management |

**Implementation Guidance**
1. Identify all user-facing AI systems
2. Design disclosure mechanisms
3. Implement disclosures
4. Verify user awareness
5. Monitor compliance

### UGR-026 — Synthetic Content Labeling  [Normative]

AI-generated synthetic content (including text, images, audio, and video) must be clearly labeled as AI-generated or AI-manipulated in a machine-readable and human-readable format.

**Intent.** Prevent deception by ensuring users can identify AI-generated content.

| Field | Value |
|---|---|
| Requirement Type | legal, standard |
| Applicability | Organizations that generate synthetic content using AI |
| Lifecycle Stages | operation |
| Priority | high |
| Risk Categories | transparency, disinformation |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 50) [pending-verification]; REF-C2PA [pending-verification] |
| See also (informative) | UGR-025, UGR-027 |
| Expected Evidence | Labeling implementation records, content labeling examples, integrity verification records |
| Related Controls | Content Labeling, Provenance Tracking, Integrity Verification |

**Implementation Guidance**
1. Implement content labeling mechanisms
2. Use standard formats (e.g., C2PA)
3. Label all synthetic content
4. Verify labeling integrity
5. Include labeling in audit trails

### UGR-027 — Deepfake Disclosure  [Normative]

Deepfake content (AI-generated or manipulated image, audio, or video that resembles real persons or events) must be clearly disclosed as artificially generated or manipulated.

**Intent.** Prevent misinformation and deception through realistic synthetic media.

| Field | Value |
|---|---|
| Requirement Type | legal |
| Applicability | Organizations that generate or distribute deepfake content |
| Lifecycle Stages | operation |
| Priority | high |
| Risk Categories | transparency, disinformation, human-rights |
| Automation Potential | high |
| Derived from | REF-EUAIA (Article 50(4)) [pending-verification]; REF-EUAIA (Article 3(66)) [pending-verification] |
| See also (informative) | UGR-025, UGR-026 |
| Expected Evidence | Deepfake detection records, disclosure labels, disclosure event logs, compliance monitoring records |
| Related Controls | Content Labeling, Deepfake Detection, Disclosure Management |

**Implementation Guidance**
1. Detect deepfake content
2. Apply disclosure labels
3. Ensure labels are visible and understandable
4. Log disclosure events
5. Monitor for compliance
