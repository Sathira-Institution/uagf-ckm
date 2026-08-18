# UAGF Authority & Semantic Contract

**Status:** RATIFIED
**Version:** v1.0
**Date:** 2026-08-18
**Authority:** Founder (Apichai Chuensuang)
**Scope:** All UAGF verification tools, APIs, validation profiles, reports, evidence packages, and public documentation

---

## 1. Purpose

This document establishes the constitutional and semantic boundary of what the **Unified AI Governance Framework (UAGF)** is authorized to determine, verify, report, and provide — and what UAGF is explicitly **not authorized to determine, certify, or assume**.

The purpose of this boundary is to:

* prevent scope expansion beyond UAGF's defined authority;
* prevent verification results from being misrepresented as legal or regulatory certification;
* preserve organizational and human accountability;
* prevent unsupported governance or legal conclusions;
* establish a consistent semantic contract across all UAGF implementations and interfaces;
* ensure that UAGF reports remain defensible, auditable, and evidence-bounded.

The governing principle is:

> **Verification ≠ Compliance Certification**

A successful UAGF verification result establishes only that the evaluated inputs satisfied the applicable UAGF verification rules under the stated verification context. It does **not**, by itself, establish legal, regulatory, organizational, or real-world compliance.

---

## 2. Constitutional Authority Model

UAGF operates as a **verification infrastructure layer**, not as the ultimate authority over organizational governance, legal applicability, or regulatory interpretation.

The following authority boundaries are constitutional:

| Layer | Has Authority To | Does NOT Have Authority To |
| --- | --- | --- |
| **Canonical Knowledge Model (CKM)** | Define canonical objects, vocabulary, invariants, schemas, and formally established semantic constraints | Redefine organizational governance semantics or impose organization-specific obligations without an explicit governing decision |
| **Crosswalk Registry** | Define defensible mappings between external requirements/artifacts and canonical UAGF concepts, including provenance and rationale | Override, redefine, or silently alter canonical semantics |
| **Validation Semantics** | Define machine-checkable rules derived from established canonical invariants and validation contracts | Create new legal, regulatory, or organizational obligations merely through implementation |
| **Verification Engine / CLI / API** | Execute approved verification rules against supplied inputs and produce deterministic results within the declared verification context | Determine organizational applicability, legal interpretation, or final governance accountability |
| **Reports / Evidence Packages** | Report verification results, mappings, provenance, evidence references, detected gaps, mismatches, limitations, and verification context | Represent a verification result as legal compliance certification, regulatory approval, or organizational attestation |
| **User / Organization** | Determine applicability, interpret organizational context, make governance decisions, and retain accountability | Delegate ultimate governance, legal, or organizational accountability to UAGF |
| **UAGF as a System** | Provide verification infrastructure, evidence handling, reproducible validation, and structured governance interoperability | Certify legal/regulatory compliance, provide legal advice, or assume organizational accountability |

---

## 3. Verification Boundary

UAGF may determine whether a defined input satisfies a defined UAGF verification rule.

Such a determination is bounded by the verification context, including where applicable:

* canonical version;
* validation profile;
* rule/ruleset version;
* supplied artifacts and evidence;
* declared configuration;
* execution environment;
* provenance information;
* verification timestamp;
* applicable scope.

Therefore:

> **A UAGF verification result is a statement about the evaluated evidence and verification rules, not a universal statement about the organization's overall compliance or governance condition.**

Where required evidence is absent, ambiguous, invalid, stale, contradictory, or outside the declared verification scope, UAGF MUST NOT silently infer compliance.

The resulting state MUST instead communicate the applicable limitation, such as:

* `UNVERIFIED`
* `INCONCLUSIVE`
* `BLOCKED`
* `FAILED`
* or another explicitly defined non-certifying state.

---

## 4. No Compliance Certification

UAGF MUST NOT represent any verification result as:

* legal compliance certification;
* regulatory approval;
* statutory certification;
* organizational compliance attestation;
* legal opinion;
* regulatory interpretation;
* guarantee of legal safety;
* guarantee of organizational governance adequacy.

The following distinction is mandatory:

> **UAGF verifies defined evidence against defined verification rules. The organization and its qualified advisors determine applicability, interpretation, and compliance.**

A mapping between an external requirement and a UAGF artifact does not, by itself, establish that the organization satisfies the underlying legal or regulatory obligation.

---

## 5. Constitutional Disclaimer

The following statement is immutable at the semantic level and MUST appear in:

* every UAGF verification report;
* every CLI verification output where output metadata/footer is supported;
* every API response metadata structure;
* every public UAGF documentation surface describing verification results;
* every externally consumable evidence package where a verification conclusion is presented.

> **"UAGF provides verification infrastructure. Verification is not compliance certification. Organizational applicability and legal compliance remain the responsibility of the user and their qualified advisors."**

Implementations MAY provide additional explanatory language, but MUST NOT weaken, contradict, or materially alter the meaning of this statement.

---

## 6. What UAGF Does NOT Do

UAGF explicitly does NOT:

* provide legal advice;
* provide authoritative regulatory interpretation;
* certify organizational compliance with laws, regulations, or standards;
* determine whether a legal or regulatory requirement applies to a specific organization unless such applicability has already been explicitly supplied as an input/decision;
* replace qualified human judgment;
* replace organizational governance authorities;
* guarantee that passing verification establishes legal safety;
* guarantee that all real-world risks have been identified;
* assume organizational accountability;
* override organizational sovereignty;
* create new governance obligations merely because a technical rule can be implemented;
* infer missing evidence as positive evidence;
* convert a successful verification result into an implied certification or attestation.

---

## 7. What UAGF DOES

UAGF explicitly DOES:

* provide deterministic verification infrastructure within a declared verification context;
* evaluate defined governance artifacts against approved machine-checkable rules;
* map organizational artifacts to canonical UGRs and related concepts with provenance;
* preserve source references and mapping rationale where required;
* identify gaps, mismatches, inconsistencies, and unverifiable conditions;
* generate structured verification results;
* generate auditable evidence packages where supported by the implementation;
* record cryptographic hashes and verification metadata where defined by the applicable evidence specification;
* support reproducible verification where the relevant reproducibility contract is satisfied;
* enable cross-standard interoperability through canonical vocabulary and semantic mappings;
* expose limitations and unresolved human determinations rather than silently resolving them.

---

## 8. Evidence Boundary

UAGF verification is bounded by the evidence supplied to the verification process.

UAGF MAY establish:

> "The supplied artifact satisfied verification rule X under verification context Y."

UAGF MUST NOT automatically convert that result into:

> "The organization is compliant."

unless a separate, explicitly authorized certification mechanism exists outside this contract.

Cryptographic integrity mechanisms, timestamps, hashes, provenance records, and reproducibility evidence establish properties of the evidence package and verification process. They do not independently establish the truth of every underlying organizational assertion.

---

## 9. Human and Organizational Accountability

UAGF does not remove or transfer accountability from the organization.

The organization remains responsible for:

* determining which requirements apply;
* providing accurate and sufficient evidence;
* making governance decisions;
* obtaining appropriate professional advice where necessary;
* interpreting verification findings within its operational context;
* addressing identified gaps;
* maintaining ongoing compliance and governance obligations.

UAGF may assist these activities through evidence and verification infrastructure but does not become the accountable decision-maker.

### Non-Delegation Principle

> **Verification capability may be delegated to UAGF. Accountability may not be delegated to UAGF.**

---

## 10. Semantic Non-Override Rule

No UAGF implementation component may silently redefine the meaning of a canonical concept.

In particular:

* application code MUST NOT override canonical semantics;
* validation rules MUST be traceable to an authorized semantic source;
* reports MUST preserve the meaning of verification states;
* APIs MUST NOT expose a stronger semantic claim than the underlying verification result supports;
* public documentation MUST NOT imply capabilities that the implementation does not provide.

Where implementation behavior conflicts with this contract, the implementation is considered non-conforming.

---

## 11. No Implied Authority

The following must never be inferred solely from the existence of a UAGF verification result:

* legal approval;
* regulatory approval;
* certification;
* accreditation;
* organizational authorization;
* risk acceptance;
* governance approval;
* executive approval;
* professional advice;
* continuing compliance.

Any such conclusion requires an independently authorized decision or mechanism.

---

## 12. Verification State Integrity

UAGF MUST preserve the distinction between:

* verified;
* failed;
* partially verified;
* unverified;
* inconclusive;
* blocked;
* not applicable where applicability has been explicitly established.

A system MUST NOT convert an unresolved or unavailable condition into a positive verification result merely to complete a workflow.

Where the evidence required to reach a conclusion is unavailable, the system SHOULD fail closed with respect to the verification claim.

---

## 13. Enforcement

Any UAGF tool, API, report, documentation surface, or evidence package that materially violates this contract is considered a **governance defect**, not a feature enhancement.

Violations MUST be handled according to their nature:

1. **Semantic / governance defect** → recorded through the applicable governance issue/change-control mechanism.
2. **Implementation defect** → recorded through the engineering defect mechanism.
3. **Security vulnerability** → reported through `SECURITY.md` or the designated security reporting mechanism.
4. **Potential constitutional conflict** → escalated for Founder determination.

A defect that causes UAGF to make an unauthorized compliance, legal, or governance claim MUST be treated as release-blocking until resolved or explicitly dispositioned by the authorized Founder decision.

---

## 14. Change Control

This contract is **append-only at the decision-history level**.

No implementation, documentation, API schema, validation rule, or report template may silently alter this contract.

Any substantive amendment MUST:

1. receive a new version identifier;
2. be recorded through a new UFD / Founder decision record;
3. identify the exact semantic change;
4. identify affected components and artifacts;
5. document compatibility implications where applicable;
6. receive explicit Founder ratification before becoming authoritative.

Previous versions MUST remain traceable.

No subordinate artifact may claim authority to supersede this contract.

---

## 15. Authority Precedence

Where conflicting interpretations exist, the following precedence applies:

**Founder-ratified constitutional decision**
↓
**Ratified UAGF Authority & Semantic Contract**
↓
**Canonical registries / canonical semantic sources**
↓
**Approved validation semantics and specifications**
↓
**Implementation**
↓
**Reports / public documentation / examples**

Lower-level artifacts MUST NOT override higher-level authority.

If a conflict cannot be resolved from the existing authoritative sources, the result MUST be treated as an unresolved governance issue and escalated for Founder decision.

---

## 16. External Representation Rule

Any external communication of a UAGF result MUST preserve the distinction between:

**Verification Result**

and

**Compliance Determination**

Permitted representation:

> "UAGF verified the supplied artifacts against the specified verification rules."

Prohibited representation:

> "UAGF certified the organization as compliant."

unless an explicitly separate and authorized certification regime exists and is clearly distinguished from ordinary UAGF verification.

---

## 17. Contract Conformance Requirement

Every UAGF component within scope MUST be evaluated for conformance to this contract.

At minimum, conformance review SHOULD verify:

* semantic consistency;
* authority boundaries;
* verification-state behavior;
* disclaimer presence where required;
* absence of implied certification;
* evidence/provenance integrity;
* correct handling of insufficient evidence;
* consistency between CLI, API, reports, and documentation;
* traceability to authoritative semantic sources.

A component that passes functional tests but violates this semantic contract is **not considered constitutionally conformant**.

---

## 18. Constitutional Principle

The foundational principle of this contract is:

> **UAGF may verify evidence.
> UAGF may expose evidence gaps.
> UAGF may structure governance evidence.
> UAGF may support human decisions.
> UAGF may not become the authority that the evidence is intended to help humans exercise.**

UAGF exists to strengthen accountable governance — not to replace it.

---

**Ratified by Founder (Apichai Chuensuang) on 2026-08-18**
