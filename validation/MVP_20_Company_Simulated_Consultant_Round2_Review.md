# Round 2 — Simulated Consultant Exception Resolution
**October 12, 2026 | MBA simulation only | no actual TargetOrate approval**

Round 1 is recorded in `validation/MVP_20_Company_Simulated_Consultant_Round1_Decisions.csv`: 7 simulated approvals, 13 holds, 0 overrides. This document is a decision proposal, **not** a record of new user approval.

## Group A — Approve tier conditionally, preserve explicit evidence limitations
These accounts have a stable weighted tier across the NS 2–10 bounds or a stable known score. Consultant must decide whether the business may pursue them while completing due diligence.

| Account | Score/tier | Proposed Round 2 disposition | Evidence limitation |
|---|---|---|---|
| Nexis Cloud Systems | 74 / Tier 2 | HOLD for compliance decision | ISO 27001 explicitly No. Confirm whether this is an absolute prerequisite; cannot assume compliant. |
| Aegis Tech Group | 77 / Tier 2 | APPROVE tier conditionally, compliance hold on pursuit | C4 unknown; sensitivity 70–77 stays Tier 2. |
| Apex ServiceNow Partner | 73 / Tier 2 | HOLD for sponsor/compliance verification | Leadership change and ISO 27001 No. |
| Summit IT Consulting | 74 / Tier 2 | APPROVE tier conditionally, compliance hold on pursuit | C4 unknown; 67–74 stays Tier 2. Long buying horizon. |

## Group B — Missing evidence changes tier; do not auto-approve
| Account | Candidate score/tier | NS low–high | Proposed Round 2 disposition |
|---|---|---|---|
| Pioneer Digital Services | 83 / Tier 1 | 67–84 | HOLD. Unknown incumbent contract plus C3/C5 gaps. Resolve contract before tier approval. |
| Meridian IT Solutions | 86 / Tier 1 | 79–86 | HOLD. Unknown compliance can reduce Tier 1 to Tier 2. |
| Crestview Cloud Group | 65 / Tier 2 | 59–66 | HOLD. Industry/subindustry conflict; establish HIPAA applicability. |
| Pinnacle Enterprise Tech | 64 / Tier 2 | 59–66 | HOLD. Missing analytics C3 could reduce Tier 2 to Tier 3. |
| Veritas Cloud Partners | 73 / Tier 2 | 57–76 | HOLD. Missing C3/C4/C5 could reduce tier. |
| Zenith Software Partners | 35 / Nurture | 35–49 | HOLD tier, recommend no active pursuit. Outside ICP and locked. |

## Group C — Strategic overrides / investment eligibility
| Account | Score/tier | Proposed Round 2 disposition | Rationale |
|---|---|---|---|
| OmniTech Systems | 71 / Tier 2 | HOLD active pursuit; request strategic exception | Outside ICP; leadership change. A numerical Tier 2 is not automatic permission to invest. |
| AlphaCentric IT | 81 / Tier 1 | HOLD pending ICP classification | FinTech SaaS industry + HealthTech SaaS subindustry cross-profile; needs consultant determination. |
| Helix Cloud Solutions | 40 / Tier 3 | HOLD investment; recommend nurture-only | Exactly at threshold, outside ICP, incompatible stack, locked incumbent. Do not silently change scoring tier. |

## Proposed consultant review decisions
- **Tier approval** and **investment eligibility** are distinct. A stable Tier 2 score can be accepted while pursuing compliance evidence.
- For unresolved NS tier-sensitive cases, retain the current proposed tier as a *candidate*, not an approved tier.
- A consultant can approve a policy-based disqualification or low-touch nurture without inventing evidence.
- No client/vendor intelligence, compliance certificate, contract detail or champion validation has been independently verified.
- After the consultant responds, append the Round 2 dispositions to a new decision log; do not overwrite Round 1 history.

## Review signoff fields
Account; Round 2 choice (approve tier / hold / override); investment permission (pursue / conditional / nurture only / do not pursue); justification; unresolved evidence; simulated consultant identity; review date.
