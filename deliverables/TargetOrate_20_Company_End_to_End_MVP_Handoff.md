# TargetOrate 20-Company MVP — End-to-End Consultant Handoff
**Scoring as of 2026-10-11 | v1.1 integration | PROVISIONAL — not client-approved**

## Executive overview
This packet follows the client workflow from account/ICP inputs, integrity checks, 14-criterion FIOR scoring, weighted composite, competitive-contract gate, exception review, to account action cards. It uses the **fresh candidate run** in `validation/MVP_v1_1_Fresh_Scoring_Candidate.csv`, not the historical adjudicated expected-results key. **Scores are illustrative and subject to the documented rubric discrepancies.** The 20-account dataset is synthetic; no claims of real market intelligence or human approvals are made.

## End-to-end workflow and artifact mapping
1. **Input and Step 0 gating:** `data/20_Company_Dataset_Iteration7.csv`; preserve 54 fields and source dates. Fatal holds: missing name, industry/sub-industry or target ACV.
2. **Completeness and integrity:** `validation/MVP_v1_1_Blind_Input_Audit.md`; missing criteria remain NS, not zero or an assumed low score.
3. **FIOR evaluation:** `validation/MVP_v1_1_Fresh_Scoring_Candidate.csv`; 14 criteria across Fit 35%, Intent 25%, Opportunity 30%, Relationship 10%.
4. **Weighted composite and rationale:** scores in the portfolio table below; retain criterion-level supporting source fields.
5. **Decision gate:** check tier-boundary cases, missing data, role verification, conflicting evidence and competitive-contract status.
6. **Human review:** TargetOrate consultant resolves all mandatory exceptions, adjudicates contested rubric interpretations, signs off tiers; sample 10% of otherwise acceptable cases (minimum three). This step **has not been performed**.
7. **Delivery:** weighted portfolio and 20 account cards below. Do not represent as final client rankings until human signoff.

## Provisional 20-company portfolio
| Account | Candidate score | Candidate post-gate tier | Consultant priority / exception |
|---|---:|---|---|
| CloudBridge Solutions | 84 | Tier 3 (contract cap) | 17-month locked incumbent; do not invest as Tier 1 |
| Nexis Cloud Systems | 74 | Tier 2 | C4 ISO 27001 No; verify compliance eligibility |
| Aegis Tech Group | 77 | Tier 2 | C4 compliance unknown; confirmed RFP |
| Vanguard Integrators | 74 | Tier 2 | C3 analytics missing; no incumbent |
| Pioneer Digital Services | 81 | Tier 1 **unconfirmed** | C3/C5/C8 NS; named incumbent status unknown; mandatory review |
| Apex ServiceNow Partner | 73 | Tier 2 | Leadership change; ISO 27001 No |
| Summit IT Consulting | 74 | Tier 2 | C4 compliance unknown; long-term buying |
| Optima Cloud Solutions | 75 | Tier 2 | Confirmed RFP; limited cross-sell |
| BlueMatrix Technologies | 74 | Tier 2 | C3 analytics unknown; long-term buying |
| Stratagem Software | 59 | Tier 3 **disputed** | C1 same-profile ICP mapping defect; tier may change |
| Meridian IT Solutions | 86 | Tier 1 **unconfirmed** | C4 compliance unknown; verify before prioritizing |
| Crestview Cloud Group | 66 | Tier 2 | Verify HIPAA applicability and C4 NS; disputed key |
| OmniTech Systems | 71 | Tier 2 | Explicitly outside ICP despite other strengths |
| Pinnacle Enterprise Tech | 57 | Tier 3 **disputed** | C1 same-profile ICP mapping defect; tier may change |
| Veritas Cloud Partners | 73 | Tier 2 | C3/C4/C5 NS; prior customer relationship |
| AlphaCentric IT | 81 | Tier 1 **provisional** | Validate mismatched industry/subindustry ICP profile |
| Novus Tech Services | 54 | Tier 3 | Outside ICP, 17-month incumbent lock |
| Quantum Integration Group | 33 | Nurture / Disqualify | Outside ICP, incompatible stack, locked incumbent |
| Zenith Software Partners | 35 | Nurture / Disqualify | Outside ICP, C3/C4 NS, locked incumbent |
| Helix Cloud Solutions | 40 | Tier 3 **boundary** | Outside ICP, incompatible stack, locked incumbent; 40-point threshold |

## 20 account action cards
Each card includes a score, rationale, evidence gap and recommended consultant action. All actions are proposed, not approved.

1. **CloudBridge Solutions — 84 / Tier 3 after cap.** Strong Fit, active RFP and confirmed budget; 2028-03-25 incumbent renewal restricts near-term opportunity. **Action:** maintain strategic nurture; verify dissatisfaction and renewal rather than override contract cap.
2. **Nexis Cloud Systems — 74 / Tier 2.** Strong technical alignment, active buying; ISO 27001 is explicitly No. **Action:** confirm required compliance before allocating sales resources.
3. **Aegis Tech Group — 77 / Tier 2.** Active RFP and budget with incomplete applicable compliance evidence. **Action:** request compliance documentation and validate competitive win likelihood.
4. **Vanguard Integrators — 74 / Tier 2.** No incumbent and relevant funding trigger; missing analytics technology evidence. **Action:** qualify stack and verify funding-driven project budget.
5. **Pioneer Digital Services — 81 / Tier 1 unconfirmed.** Strong ICP profile and active evaluation; three NS criteria and unknown incumbent contract status. **Action:** mandatory review; resolve contract status and C3/C5 before approving investment.
6. **Apex ServiceNow Partner — 73 / Tier 2.** Strong intent and confirmed budget, but leadership change and ISO 27001 No. **Action:** confirm sponsor continuity and compliance fit.
7. **Summit IT Consulting — 74 / Tier 2.** Strong ICP fit, identified advocate; long buying horizon and unknown compliance. **Action:** nurture champion while collecting regulatory evidence.
8. **Optima Cloud Solutions — 75 / Tier 2.** Active RFP and budget, but limited product expansion. **Action:** validate decision committee and prioritize focused pilot.
9. **BlueMatrix Technologies — 74 / Tier 2.** Product breadth and moderate champion; analytics stack evidence missing. **Action:** verify technology integration and buying timeline.
10. **Stratagem Software — 59 / disputed Tier 3.** Strong industry/sub-industry ICP match was undercounted by candidate. **Action:** correct C1 and recalculate; do not treat Tier 3 as settled.
11. **Meridian IT Solutions — 86 / Tier 1 unconfirmed.** Active evaluation, no incumbent, confirmed budget; compliance Unknown. **Action:** clear compliance exception before approving Tier 1.
12. **Crestview Cloud Group — 66 / Tier 2.** Technical compatibility and identified champion; conflicting HIPAA/compliance treatment. **Action:** establish regulatory applicability and rescore C4.
13. **OmniTech Systems — 71 / Tier 2.** Commercial breadth but sub-industry explicitly outside ICP. **Action:** human review of ICP exception before investment.
14. **Pinnacle Enterprise Tech — 57 / disputed Tier 3.** Candidate C1 incorrectly omitted same-profile industry match; missing analytics evidence. **Action:** correct C1, resolve C3 and recalculate tier.
15. **Veritas Cloud Partners — 73 / Tier 2.** Former customer relationship and no incumbent; technology/compliance/intent evidence gaps. **Action:** re-engage past contact and complete due diligence.
16. **AlphaCentric IT — 81 / provisional Tier 1.** Confirmed budget, no incumbent, broad technology alignment; mismatched industry/sub-industry pairing. **Action:** consultant verifies ICP interpretation before approval.
17. **Novus Tech Services — 54 / Tier 3.** Small outside-ICP account, locked incumbent, limited readiness. **Action:** low-touch nurture only.
18. **Quantum Integration Group — 33 / Nurture.** Outside ICP, incompatible on-prem stack, ISO 27001 No and incumbent lock. **Action:** disqualify active pursuit pending material change.
19. **Zenith Software Partners — 35 / Nurture.** Outside ICP and locked competitor; technology/compliance unknown. **Action:** defer investment and track changes.
20. **Helix Cloud Solutions — 40 / disputed Tier 3.** Outside ICP and incompatible cloud stack; exactly on tier boundary. **Action:** independent review before any active pursuit.

## Exception queue and human approval
**Mandatory review first:** Pioneer (unknown incumbent status); CloudBridge and other locked competitors (contract gate); Aegis, Summit, Meridian, Veritas and Zenith (unknown compliance); Stratagem and Pinnacle (C1 mapping changes); Crestview (HIPAA applicability); Helix (threshold); leadership-change accounts. Other missing technology/intent scores must undergo NS 2–10 sensitivity checks. Historical key disagreements in C5, C12, C13 and C14 remain unresolved. A routine 25% review planning target **never limits mandatory exceptions**.

Consultant disposition template: account; criterion; evidence source/date; original band; proposed band; reason; NS low/high; tier before/after; gate before/after; reviewer; approval date; decision (approve/reject/hold). **No approvals are asserted.**

## MVP completion and next steps
**Demonstrated:** dataset ingestion, preliminary scores for 20 accounts, composite calculation, contract cap, candidate portfolio, 20 consultant action cards, exception routing, documented known defects.

**Not yet demonstrated:** independently re-derived 280/280 scoring accuracy, complete criterion evidence and self-review, actual consultant approval, live verified vendor-disruption list (currently empty), 100-company scalability.

**Step 3 — 100-company expansion:** after fixing material scoring disagreements and confirming 20-account acceptance, apply the same input schema and rules to 100 companies, preserve score provenance, track NS bounds and exceptions, sample accepted cases and report tier distributions. Do not claim successful 100-company processing until executed.

**Step 4 — final toolkit packaging:** deliver modular scoring/review prompts, prompt chains, QC checklist, workflow/human approval instructions, input/exception/output templates, test cases, and versioned evidence/decision log, alongside a client demonstration and documented limitations.
