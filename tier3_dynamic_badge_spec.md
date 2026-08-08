# UAGF Certification — Tier 3: Dynamic Trust Badge Specification
**Status:** DRAFT v0.1 — pending Founder ratification. ⚑ **This tier requires a ruling on OD-07 before implementation** (see §7).

## 1. Why the badge must be dynamic
A static badge asserts a past event ("assessed in March") and keeps asserting it after the underlying facts change. That is precisely the documentation-drift failure UAGF exists to eliminate, transposed onto trust. A UAGF badge is therefore a **live rendering of current pipeline state**, not a certificate image: it is `Render(profile=trust-badge, scope=organization, …)` — the same engine, a new profile, no new architecture.

**Consequence to state plainly to every consumer:** the badge reports whether an organization's own governance pipeline is currently passing its declared gates. It is not a conformance certificate for any AI system, and not a legal attestation.

## 2. Endpoint
```
GET /api/v1/trust-badge/{organization_id}
Accept: application/json
```
- `organization_id` — the holder's registry identifier (ACTOR reference; see cert-registry-schema.yaml).
- Public, unauthenticated read. Rate-limited. No adopter instance data is ever returned (Kernel invariant V-5: Tier-2 data stays outside the public surface — the badge exposes *status*, never governed content).

## 3. Response schema
| Field | Type | Meaning |
|---|---|---|
| `organization_id` | string | Holder identifier |
| `cert_id` | string | `GCID-2026-CERT-NNNNNN` |
| `tier` | integer | 3 |
| `status` | enum | `ACTIVE` · `UNDER_REVIEW` · `SUSPENDED` · `EXPIRED` |
| `last_validated_timestamp` | ISO 8601 | When the holder's pipeline last reported a complete gate run |
| `ckm_release_validated` | string | Release the holder's run was performed against |
| `invariant_violations` | array | Open violations: `{invariant, count, first_seen, severity}` — empty array when clean |
| `open_dispositions` | object | `{TO_VERIFY, CONFLICT, REJECTED}` counts from the holder's latest migration report |
| `gates` | object | `{total, passed, failed}` from the holder's E2E summary |
| `verification_hash` | string | SHA-256 over the reported state; matches the registry entry |
| `status_reason` | string | Human-readable cause of any non-ACTIVE status |
| `expires` | ISO 8601 | Certification expiry (independent of live status) |

### 3.1 Status semantics
- **ACTIVE** — latest run green, no open invariant violations, no undeclared render differences, report freshness within policy.
- **UNDER_REVIEW** — automatic, machine-triggered (§4). Not a penalty and not an accusation: it means the reported state no longer supports an ACTIVE claim until re-validated.
- **SUSPENDED** — requires an explicit Founder decision (UFD reference recorded). Machines may never set SUSPENDED; the difference between "the numbers changed" and "trust is withdrawn" is a governance judgement, not a computation.
- **EXPIRED** — `expires` has passed. Purely temporal.

## 4. Webhook trigger logic
The holder's CI posts its E2E summary to the certification service after each run.

```
on report_received(report):
    if report.undeclared_render_differences > 0:      → status = UNDER_REVIEW   # primary trigger
    elif any(report.invariant_violations):            → status = UNDER_REVIEW
    elif report.gates.failed > 0:                     → status = UNDER_REVIEW
    elif report.dispositions.REJECTED > 0:            → status = UNDER_REVIEW
    else:                                             → status = ACTIVE
    always: last_validated_timestamp = report.timestamp
            verification_hash = sha256(canonical_json(reported_state))

on no_report_for(policy_window):                      → status = UNDER_REVIEW
    # silence is not evidence of health (Reality First); staleness downgrades, never sustains
```
Transitions to and from `SUSPENDED` are excluded from this logic and require a Founder decision record. Every transition is appended to an immutable status history.

**Why `undeclared_render_differences > 0` is the primary trigger:** an undeclared difference means an artifact and its model disagree without declaration — either a hand-edited artifact or silent loss. That single number is the sharpest available signal that the holder's discipline has lapsed.

## 5. Sample request and response
```bash
curl -s -H "Accept: application/json" \
  https://api.sathira.institute/api/v1/trust-badge/ORG-000042
```
```json
{
  "organization_id": "ORG-000042",
  "cert_id": "GCID-2026-CERT-000117",
  "tier": 3,
  "status": "UNDER_REVIEW",
  "last_validated_timestamp": "2026-08-01T09:14:22Z",
  "ckm_release_validated": "2.0.0-alpha",
  "invariant_violations": [
    {"invariant": "V-4", "count": 3, "first_seen": "2026-08-01T09:14:22Z", "severity": "error"}
  ],
  "open_dispositions": {"TO_VERIFY": 11, "CONFLICT": 2, "REJECTED": 0},
  "gates": {"total": 13, "passed": 11, "failed": 2},
  "verification_hash": "9f547154b524f9eda8dc35e44ba6b2e73d1c7570887f3325aa8785e3930d676a",
  "status_reason": "Undeclared render differences detected in the holder's latest run; three unmapped vocabulary values open.",
  "expires": "2028-08-01T00:00:00Z"
}
```
A clean holder returns `"status": "ACTIVE"`, `"invariant_violations": []`, `"gates": {"total": 13, "passed": 13, "failed": 0}`.

## 6. Badge rendering profile
`trust-badge` is registered as a rendering profile, subject to the same rules as every other view:
- **Input scope:** one organization's current certification state plus its latest report.
- **Output:** JSON (canonical) and an SVG/HTML render for display.
- **Transformation rules:** status derivation per §4; no field may be displayed that is not present in the source state (RE-2, no invention).
- **Loss policy:** the SVG display view is declared-lossy (shows status and date only) and links to the full JSON; the JSON view is lossless.
- **Validation:** `verification_hash` recomputed on render; mismatch fails closed and emits no badge (RE-7) — a badge that cannot be verified is not displayed as a degraded badge, it is not displayed at all.

## 7. ⚑ Governance precondition (must be resolved before build)
UAGF's published scope statement (UAGF-OOS-003) declares UAGF a methodology and **not a certification scheme**, and open decision **OD-07** on the traceability chain terminus has never been ruled. This tier issues an organization-level trust signal, which is the activity that statement excludes.

Two coherent resolutions, both available to the Founder:
1. **Institutional separation (recommended).** SATHIRA Institution operates the certification program; UAGF remains the neutral public model it certifies against. The badge is then a SATHIRA attestation about a holder's use of UAGF, not UAGF certifying anyone. Requires no change to UAGF's scope statement, only clear labelling on every response and in the registry.
2. **Amend the scope statement.** Rule OD-07 to place certification inside UAGF's mandate and revise UAGF-OOS-003 accordingly — a constitutional change with consequences for the neutrality claim, since a body that certifies has interests in what it certifies.

Until one is ruled, this specification stands as a design, and no endpoint should be published.
