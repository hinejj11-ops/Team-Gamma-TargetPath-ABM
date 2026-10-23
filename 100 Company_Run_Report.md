# TargetPath ABM Run Report: Synthetic 100 Company Dataset

**Status: PROVISIONAL. Nothing is approved.** Steps 0 to 6 of the workflow are complete. The run stops at the human input checkpoint (Step 7). No consultant input has been applied.

| Item | Value |
|---|---|
| Repository and branch | hinejj11-ops/Team-Gamma-TargetPath-ABM, branch `synthetic-100-company` (commit c52b396) |
| Dataset | `data/100_Company_Dataset_Synthetic_Test.csv`: 100 accounts, 54 columns, no Ground Truth column (no split needed) |
| Scoring As Of Date | October 11, 2026 (chosen by you; the dataset README built its dates around this day) |
| ICP | `examples/TargetOrate_Completed_ICP_Example.md` (synthetic) |
| Rubric | `FIOR_Scoring_Rubric_10_2_2026.md`, Iteration 7 draft, with the Competitive Lock Gate |
| Validation assets | Not opened. Nothing under `/validation/` was read |
| Workflow version label | MVP v1.1 integration run (self review step included). Proposed changes in v1.1 are not yet accepted, so treat results as a test run |

The branch README says not to run this data against the MVP until TargetOrate adjudication is complete. You asked for the run, so I ran it, but read every result as a workflow stress test of synthetic fixtures, not as accounts to prospect or as a measure of scoring accuracy.

## 1. Input validation (Step 0): PASS WITH REVIEW

- ICP present with usable C1 to C4 benchmarks (explicit ranges, required/preferred/incompatible tech, served regions, compliance). Scoring As Of Date supplied.
- **10 accounts held** because a fatal field is missing: 5 with blank Industry (rows 21, 37, 53, 69, 85) and 5 with blank Target ACV (rows 22, 38, 54, 70, 86). They receive no total or tier. Data request below.
- Non fatal gaps carried as NS and tested with the low and high bound rule: blank Employee Count (5 accounts), blank Geography (5), blank Data / Analytics (50), blank Cloud Infrastructure (22), Unknown compliance fields, undated intent or trigger records.
- Incumbent fields valid. Contract Renewal Date values are all valid dates or blank. No evidence dates fall after the As Of Date.

## 2. Portfolio summary

Scored accounts: 90. Held: 10.

| Recommended tier after the Competitive Lock Gate | Accounts |
|---|---|
| Tier 1 | 5 |
| Tier 2 | 36 |
| Tier 3 | 30 |
| Nurture / Inbound Only | 10 |
| Disqualified (Competitive Lock) | 9 |
| HELD (no tier) | 10 |

Score implied tier before the gate: Tier 1 6, Tier 2 54, Tier 3 19, Nurture 11.

**Competitive Lock Gate.** It applied to 55 scored accounts with a Locked contract. 9 were disqualified, 15 were capped from Tier 1 or 2 to Tier 3, and 1 account that scored into Tier 1 did not stay there (#1 CloudBridge Solutions).

**Highest priority accounts (Tier 1 after the gate):**

- #11 Meridian IT Solutions: 86 (review: Missing data straddles tiers (NS: C4; low bound Tier 2, high bound Tier 1))
- #5 Pioneer Digital Services: 83 (review: Missing data straddles tiers (NS: C3, C5, C8; low bound Tier 2, high bound Tier 1))
- #81 Elmstone Enterprise Solutions 02: 83 (review: Contact role not verified in last 6 months; Renewal date on or before As Of Date: confirm whether contract renewed)
- #55 Redwood Digital Systems 01: 80 (review: Missing data straddles tiers (NS: C2, C3, C4, C5, C7; low bound Tier 3, high bound Tier 1); Contact role not verified in last 6 months)
- #25 Cedar Enterprise Solutions 01: 80 (review: Missing data straddles tiers (NS: C3; low bound Tier 2, high bound Tier 1); Low confidence C8: Structured contradiction: No incumbent but Dissatisfied; scored 8 (alt 10); ESCALATE)

**Review rate.**

- Scored accounts sent to review: **82 of 90 (91 percent)**. Acceptable with no trigger: 8. Held: 10.
- Counting only triggers that are in the rubric, the rate is 81 of 90 (90 percent). 1 account is flagged only by the workflow added ICP disqualifier check (see section 6), so that check barely changes the review volume.
- Mandatory exceptions (uncapped): 41. Routine reviews: 41 of 90 (46 percent) against the proposed 25 percent ceiling, or 40 (44 percent) on rubric triggers only.
- All 5 Tier 1 accounts carry at least one review trigger, so no Tier 1 recommendation is clean yet.
- The ceiling is exceeded by a wide margin. Per the rubric, report it as a finding about the data and rules: the largest drivers are missing data bounds, stale or blank role verification dates, and the synthetic fixture design that deliberately seeds exceptions.
- Sampled check: 8 Acceptable accounts, so the consultant spot checks at least 3.

Review triggers fired (an account can have several):

| Trigger | Accounts | Mandatory | What resolves it |
|---|---|---|---|
| NS bounds straddle tiers | 41 | No | Supply the NS fields named in the Data Gaps column (for example Cloud Infrastructure, Data / Analytics, SOC 2, ISO 27001, GDPR, Geography, Employee Count, intent dates, trigger dates) |
| Role not verified in 6 months | 35 | No | Re verify named contacts and record a Role Verification Date within 6 months |
| ICP disqualifying factor (workflow added) | 22 | No | Confirm the ICP exclusion applies, or document a strategic exception |
| Within 2 points of cutoff | 19 | No | Consultant judgment on tier; the total is within 2 points of a cutoff |
| Lock gate disqualification, past renewal, or unknown status with named incumbent | 19 | Yes | Confirm contract status and renewal date; approve or reject the disqualification |
| Conflicting industry classification | 14 | Yes | Confirm the correct industry and sub industry classification |
| Self review escalation | 9 | Yes | Rule on the rubric question (C9 at $250K; C8 with No incumbent and Dissatisfied) |
| Leadership change trigger | 8 | No | Confirm the named leader is still in role |
| C1 and C2 both 2 | 8 | No | Confirm the account is a true non fit or document an exception |
| Low confidence criterion | 5 | Yes | Resolve the contradictory structured fields |
| Unhappy churn | 5 | No | Review churn reason before any outreach |
| Revenue per employee outlier | 1 | No | Confirm revenue and employee count (row 20 shows $650M on 25 employees) |

## 3. Ranked portfolio

Disqualified accounts follow the ranked accounts, then held accounts. Dimension scores are Fit /35, Intent /25, Opportunity /30, Relationship /10. Full text reasons, evidence and gate details are in the two CSV files.

| Rank | Company | Fit | Intent | Opp | Rel | Total | Score Tier | Gate | Recommended | Review | Reason | Low / High | Self Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Meridian IT Solutions | 35.0 | 22.5 | 21.0 | 7.0 | 86 | Tier 1 | Not applied | Tier 1 | Review | Missing data straddles tiers (NS: C4; low bound Tier 2, high bound Tier 1) | T2 / T1 | Confirmed |
| 2 | Pioneer Digital Services | 35.0 | 22.5 | 19.5 | 6.0 | 83 | Tier 1 | Not evaluated (status unknown) | Tier 1 | Review | Missing data straddles tiers (NS: C3, C5, C8; low bound Tier 2, high bound Tier 1) | T2 / T1 | Confirmed |
| 3 | Elmstone Enterprise Solutions 02 | 35.0 | 17.5 | 24.0 | 6.0 | 83 | Tier 1 | Open window (band 1) | Tier 1 | Review | Contact role not verified in last 6 months; Renewal date on or before As Of Date: confirm whether contract renewed |  | Confirmed |
| 4 | CloudBridge Solutions | 35.0 | 18.8 | 22.5 | 6.0 | 82 | Tier 1 | Capped to Tier 3 (band 2) | Tier 3 | Acceptable |  |  | Confirmed |
| 5 | Redwood Digital Systems 01 | 35.0 | 17.5 | 19.5 | 8.0 | 80 | Tier 1 | Not applied | Tier 1 | Review | Missing data straddles tiers (NS: C2, C3, C4, C5, C7; low bound Tier 3, high bound Tier 1); Contact role not verified in last 6 months; Total 80 within 2 points of the 80... | T3 / T1 | Confirmed |
| 6 | Cedar Enterprise Solutions 01 | 35.0 | 17.5 | 21.0 | 6.0 | 80 | Tier 1 | Not applied | Tier 1 | Review | Missing data straddles tiers (NS: C3; low bound Tier 2, high bound Tier 1); Low confidence C8: Structured contradiction: No incumbent but Dissatisfied; scored 8 (alt 10);... | T2 / T1 | Escalated |
| 7 | Zenith Digital Systems 02 | 35.0 | 16.7 | 19.5 | 7.0 | 78 | Tier 2 | Open window (band 1) | Tier 2 | Review | Missing data straddles tiers (NS: C2, C4, C6; low bound Tier 2, high bound Tier 1); Total 78 within 2 points of the 80 cutoff | T2 / T1 | Confirmed |
| 8 | Aegis Tech Group | 35.0 | 17.5 | 19.5 | 6.0 | 78 | Tier 2 | Not applied | Tier 2 | Review | Total 78 within 2 points of the 80 cutoff | T2 / T2 | Confirmed |
| 9 | Beacon Digital Systems 01 | 35.0 | 16.7 | 19.5 | 6.0 | 77 | Tier 2 | Open window (band 1) | Tier 2 | Acceptable |  | T2 / T2 | Confirmed |
| 10 | Westbridge Enterprise Solutions 02 | 35.0 | 16.7 | 19.5 | 6.0 | 77 | Tier 2 | Open window (band 1) | Tier 2 | Review | Renewal date on or before As Of Date: confirm whether contract renewed | T2 / T2 | Confirmed |
| 11 | AlphaCentric IT | 31.5 | 16.2 | 19.5 | 9.0 | 76 | Tier 2 | Not applied | Tier 2 | Review | Conflicting industry classification |  | Confirmed |
| 12 | Xenon Software Collective 02 | 29.8 | 21.2 | 18.0 | 7.0 | 76 | Tier 2 | Open window (band 1) | Tier 2 | Review | Contact role not verified in last 6 months |  | Confirmed |
| 13 | Nexis Cloud Systems | 29.8 | 17.5 | 19.5 | 9.0 | 76 | Tier 2 | Not applied | Tier 2 | Acceptable |  |  | Confirmed |
| 14 | Summit IT Consulting | 35.0 | 13.8 | 21.0 | 6.0 | 76 | Tier 2 | Not applied | Tier 2 | Acceptable |  | T2 / T2 | Confirmed |
| 15 | Keystone Enterprise Solutions 01 | 35.0 | 13.3 | 21.0 | 6.0 | 75 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Acceptable |  | T2 / T2 | Confirmed |
| 16 | BlueMatrix Technologies | 35.0 | 12.5 | 22.5 | 5.0 | 75 | Tier 2 | Not applied | Tier 2 | Review | Contact role not verified in last 6 months | T2 / T2 | Confirmed |
| 17 | Keystone Data Services 01 | 28.0 | 23.3 | 16.5 | 5.5 | 73 | Tier 2 | Not applied | Tier 2 | Review | C14: former customer churned unhappy; champion evidence conflicts; ICP disqualifying factor, tier above Nurture (workflow added): Target ACV below $50K | T2 / T2 | Confirmed |
| 18 | Optima Cloud Solutions | 35.0 | 17.5 | 13.5 | 7.0 | 73 | Tier 2 | Not applied | Tier 2 | Review | Self review escalation: C9: RUBRIC CONFLICT at $250K edge (rule says lower band, band text includes $250K in 8); ESCALATE |  | Escalated |
| 19 | OmniTech Systems | 28.0 | 13.8 | 24.0 | 7.0 | 73 | Tier 2 | Not applied | Tier 2 | Review | Leadership change trigger; ICP disqualifying factor, tier above Nurture (workflow added): excluded category (Outsourced Digital Marketing) |  | Confirmed |
| 20 | Jasper Security Labs 02 | 25.7 | 20.0 | 19.5 | 7.0 | 72 | Tier 2 | Not applied | Tier 2 | Review | Low confidence C8: Structured contradiction: No incumbent but Dissatisfied; scored 8 (alt 10); ESCALATE; Contact role not verified in last 6 months; Self review escalatio... | T2 / T2 | Escalated |
| 21 | Veritas Cloud Partners | 35.0 | 13.3 | 15.0 | 8.0 | 71 | Tier 2 | Not applied | Tier 2 | Review | Missing data straddles tiers (NS: C3, C4, C5; low bound Tier 3, high bound Tier 2) | T3 / T2 | Confirmed |
| 22 | Apex ServiceNow Partner | 26.2 | 15.0 | 21.0 | 9.0 | 71 | Tier 2 | Not applied | Tier 2 | Review | Conflicting industry classification; Leadership change trigger; Self review escalation: C9: RUBRIC CONFLICT at $250K edge (rule says lower band, band text includes $250K ... |  | Escalated |
| 23 | Granite Enterprise Solutions 01 | 28.0 | 13.8 | 22.5 | 7.0 | 71 | Tier 2 | Open window (band 1) | Tier 2 | Review | Contact role not verified in last 6 months; Leadership change trigger; Renewal date on or before As Of Date: confirm whether contract renewed; ICP disqualifying factor, t... |  | Confirmed |
| 24 | Vanguard Integrators | 35.0 | 17.5 | 13.5 | 5.0 | 71 | Tier 2 | Not applied | Tier 2 | Review | Contact role not verified in last 6 months; Self review escalation: C9: RUBRIC CONFLICT at $250K edge (rule says lower band, band text includes $250K in 8); ESCALATE | T2 / T2 | Escalated |
| 25 | Orion Enterprise Solutions 01 | 35.0 | 12.5 | 18.0 | 5.0 | 71 | Tier 2 | Open window (band 1) | Tier 2 | Review | Missing data straddles tiers (NS: C3, C4; low bound Tier 3, high bound Tier 2); Contact role not verified in last 6 months; Renewal date on or before As Of Date: confirm ... | T3 / T2 | Confirmed |
| 26 | Unity Cloud Partners 02 | 24.5 | 21.2 | 16.5 | 8.0 | 70 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Contact role not verified in last 6 months |  | Confirmed |
| 27 | Delta Security Labs 01 | 25.7 | 17.5 | 21.0 | 6.0 | 70 | Tier 2 | Open window (band 1) | Tier 2 | Review | Contact role not verified in last 6 months; ICP disqualifying factor, tier above Nurture (workflow added): employees and revenue both materially outside ICP | T2 / T2 | Confirmed |
| 28 | Foresight Digital Systems 01 | 28.0 | 16.2 | 18.0 | 7.0 | 69 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Contact role not verified in last 6 months | T2 / T2 | Confirmed |
| 29 | Lighthouse Security Labs 01 | 21.0 | 21.7 | 19.5 | 6.0 | 68 | Tier 2 | Not applied | Tier 2 | Review | Missing data straddles tiers (NS: C3, C4, C5; low bound Tier 3, high bound Tier 2); Low confidence C8: Structured contradiction: No incumbent but Dissatisfied; scored 8 (... | T3 / T2 | Escalated |
| 30 | Harbor Software Collective 01 | 26.2 | 16.2 | 16.5 | 9.0 | 68 | Tier 2 | Open window (band 1) | Tier 2 | Review | Conflicting industry classification |  | Confirmed |
| 31 | Elmstone Data Services 02 | 24.5 | 16.2 | 18.0 | 9.0 | 68 | Tier 2 | Not evaluated (status unknown) | Tier 2 | Review | Contract status unknown with a named incumbent: consultant review required before final tier approval |  | Confirmed |
| 32 | Stratagem Software | 28.0 | 11.2 | 21.0 | 7.0 | 67 | Tier 2 | Not applied | Tier 2 | Acceptable |  | T2 / T2 | Confirmed |
| 33 | Indigo Enterprise Solutions 02 | 35.0 | 7.5 | 19.5 | 5.0 | 67 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Missing data straddles tiers (NS: C3, C6, C7; low bound Tier 3, high bound Tier 2) | T3 / T2 | Confirmed |
| 34 | Vertex Digital Systems 02 | 28.0 | 16.2 | 16.5 | 6.0 | 67 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Contact role not verified in last 6 months; ICP disqualifying factor, tier above Nurture (workflow added): Target ACV below $50K | T2 / T2 | Confirmed |
| 35 | Praxis Security Labs 01 | 25.7 | 17.5 | 16.5 | 7.0 | 67 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Contact role not verified in last 6 months; ICP disqualifying factor, tier above Nurture (workflow added): employees and revenue both materially outside ICP | T2 / T2 | Confirmed |
| 36 | Fidelity Security Labs 02 | 25.7 | 15.0 | 19.5 | 6.0 | 66 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Missing data straddles tiers (NS: C4, C6; low bound Tier 3, high bound Tier 2); ICP disqualifying factor, tier above Nurture (workflow added): employees and revenue both ... | T3 / T2 | Confirmed |
| 37 | Northstar Technology Advisors 01 | 29.8 | 16.7 | 12.0 | 7.0 | 65 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Acceptable |  | T2 / T2 | Confirmed |
| 38 | Aster Enterprise Solutions 02 | 28.0 | 13.8 | 19.5 | 4.0 | 65 | Tier 2 | Not applied | Tier 2 | Review | Low confidence C8: Structured contradiction: No incumbent but Dissatisfied; scored 8 (alt 10); ESCALATE; Leadership change trigger; Self review escalation: C8: Structured... | T2 / T2 | Escalated |
| 39 | Evergreen Cloud Partners 01 | 23.3 | 18.3 | 16.5 | 7.0 | 65 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Missing data straddles tiers (NS: C3, C5; low bound Tier 3, high bound Tier 2) | T3 / T2 | Confirmed |
| 40 | Boreal Security Labs 02 | 21.0 | 16.2 | 19.5 | 8.0 | 65 | Tier 2 | Open window (band 1) | Tier 2 | Review | Missing data straddles tiers (NS: C3, C4; low bound Tier 3, high bound Tier 2); Contact role not verified in last 6 months; ICP disqualifying factor, tier above Nurture (... | T3 / T2 | Confirmed |
| 41 | Fidelity Software Collective 02 | 24.5 | 21.7 | 13.5 | 5.0 | 65 | Tier 2 | Open window (band 1) | Tier 2 | Review | Missing data straddles tiers (NS: C3, C4, C5; low bound Tier 3, high bound Tier 2); ICP disqualifying factor, tier above Nurture (workflow added): Target ACV below $50K | T3 / T2 | Confirmed |
| 42 | Pinnacle Enterprise Tech | 28.0 | 10.0 | 19.5 | 7.0 | 65 | Tier 2 | Not applied | Tier 2 | Review | Missing data straddles tiers (NS: C3; low bound Tier 3, high bound Tier 2); Contact role not verified in last 6 months | T3 / T2 | Confirmed |
| 43 | Indigo Data Services 02 | 21.0 | 18.3 | 21.0 | 3.5 | 64 | Tier 2 | Not applied | Tier 2 | Review | Missing data straddles tiers (NS: C3, C5; low bound Tier 3, high bound Tier 2); C14: former customer churned unhappy; champion evidence conflicts | T3 / T2 | Confirmed |
| 44 | Crestview Cloud Group | 30.3 | 13.8 | 12.0 | 7.0 | 63 | Tier 2 | Not applied | Tier 2 | Review | Missing data straddles tiers (NS: C4; low bound Tier 3, high bound Tier 2); Conflicting industry classification | T3 / T2 | Confirmed |
| 45 | Monarch Cloud Partners 01 | 21.0 | 15.0 | 18.0 | 9.0 | 63 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Conflicting industry classification; Leadership change trigger |  | Confirmed |
| 46 | Xenon Security Labs 02 | 25.7 | 13.3 | 18.0 | 6.0 | 63 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Missing data straddles tiers (NS: C4, C5; low bound Tier 3, high bound Tier 2); Contact role not verified in last 6 months; ICP disqualifying factor, tier above Nurture (... | T3 / T2 | Confirmed |
| 47 | Kestrel Cloud Partners 02 | 25.7 | 15.0 | 15.0 | 7.0 | 63 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Missing data straddles tiers (NS: C3; low bound Tier 3, high bound Tier 2) | T3 / T2 | Confirmed |
| 48 | Redwood Technology Advisors 01 | 23.3 | 16.2 | 15.0 | 8.0 | 63 | Tier 2 | Not evaluated (status unknown) | Tier 2 | Review | Missing data straddles tiers (NS: C4; low bound Tier 3, high bound Tier 2); Conflicting industry classification; Contact role not verified in last 6 months; ICP disqualif... | T3 / T2 | Confirmed |
| 49 | Mosaic Enterprise Solutions 02 | 28.0 | 7.5 | 21.0 | 6.0 | 63 | Tier 2 | Open window (band 1) | Tier 2 | Review | Contact role not verified in last 6 months; Renewal date on or before As Of Date: confirm whether contract renewed; ICP disqualifying factor, tier above Nurture (workflow... |  | Confirmed |
| 50 | Silverline Enterprise Solutions 01 | 28.0 | 10.0 | 18.0 | 6.0 | 62 | Tier 2 | Open window (band 1) | Tier 2 | Review | Contact role not verified in last 6 months; Renewal date on or before As Of Date: confirm whether contract renewed; ICP disqualifying factor, tier above Nurture (workflow... |  | Confirmed |
| 51 | Westbridge Data Services 02 | 21.0 | 12.5 | 19.5 | 9.0 | 62 | Tier 2 | Not evaluated (status unknown) | Tier 2 | Review | Conflicting industry classification; Leadership change trigger |  | Confirmed |
| 52 | Lucent Technology Advisors 02 | 26.2 | 11.2 | 15.0 | 9.0 | 62 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Conflicting industry classification |  | Confirmed |
| 53 | Lighthouse Software Collective 01 | 28.0 | 16.2 | 12.0 | 5.0 | 61 | Tier 2 | Not evaluated (status unknown) | Tier 2 | Review | Missing data straddles tiers (NS: C3; low bound Tier 3, high bound Tier 2); Contact role not verified in last 6 months; Total 61 within 2 points of the 60 cutoff | T3 / T2 | Confirmed |
| 54 | Horizon Technology Advisors 02 | 28.0 | 15.0 | 10.5 | 7.0 | 61 | Tier 2 | Capped to Tier 3 (band 2) | Tier 3 | Review | Missing data straddles tiers (NS: C4; low bound Tier 3, high bound Tier 2); Total 61 within 2 points of the 60 cutoff | T3 / T2 | Confirmed |
| 55 | Praxis Software Collective 01 | 23.3 | 16.2 | 13.5 | 7.0 | 60 | Tier 2 | Open window (band 1) | Tier 2 | Review | Missing data straddles tiers (NS: C4; low bound Tier 3, high bound Tier 2); Conflicting industry classification; Total 60 within 2 points of the 60 cutoff | T3 / T2 | Confirmed |
| 56 | Beacon Technology Advisors 01 | 24.5 | 16.7 | 13.5 | 5.0 | 60 | Tier 2 | Not applied | Tier 2 | Review | Missing data straddles tiers (NS: C3, C4, C5; low bound Tier 3, high bound Tier 2); Total 60 within 2 points of the 60 cutoff | T3 / T2 | Confirmed |
| 57 | Cedar Data Services 01 | 21.0 | 12.5 | 21.0 | 4.5 | 59 | Tier 3 | Not evaluated (status unknown) | Tier 3 | Review | Conflicting industry classification; Contact role not verified in last 6 months; Leadership change trigger; C14: former customer churned unhappy; champion evidence confli... |  | Confirmed |
| 58 | Orion Data Services 01 | 21.0 | 13.8 | 16.5 | 7.0 | 58 | Tier 3 | Not evaluated (status unknown) | Tier 3 | Review | Missing data straddles tiers (NS: C3; low bound Tier 3, high bound Tier 2); Contact role not verified in last 6 months; Total 58 within 2 points of the 60 cutoff | T3 / T2 | Confirmed |
| 59 | Northstar Digital Systems 01 | 28.0 | 8.3 | 19.5 | 2.0 | 58 | Tier 3 | Band 2 cap, no change | Tier 3 | Review | Missing data straddles tiers (NS: C4, C6, C14; low bound Tier 3, high bound Tier 2); Total 58 within 2 points of the 60 cutoff | T3 / T2 | Confirmed |
| 60 | Lucent Digital Systems 02 | 24.5 | 8.3 | 16.5 | 8.0 | 57 | Tier 3 | Band 2 cap, no change | Tier 3 | Review | Missing data straddles tiers (NS: C3, C4, C6; low bound Tier 3, high bound Tier 2) | T3 / T2 | Confirmed |
| 61 | Vertex Technology Advisors 02 | 28.0 | 13.8 | 10.5 | 5.0 | 57 | Tier 3 | Band 2 cap, no change | Tier 3 | Acceptable |  | T3 / T3 | Confirmed |
| 62 | Jasper Software Collective 02 | 23.3 | 13.8 | 10.5 | 7.0 | 55 | Tier 3 | Not evaluated (status unknown) | Tier 3 | Review | Conflicting industry classification; Contact role not verified in last 6 months | T3 / T3 | Confirmed |
| 63 | Zenith Technology Advisors 02 | 23.3 | 15.0 | 9.0 | 7.0 | 54 | Tier 3 | Not applied | Tier 3 | Review | Missing data straddles tiers (NS: C4, C5, C7; low bound Tier 3, high bound Tier 2); Conflicting industry classification | T3 / T2 | Confirmed |
| 64 | Granite Data Services 01 | 21.0 | 11.2 | 18.0 | 4.0 | 54 | Tier 3 | Not evaluated (status unknown) | Tier 3 | Review | Missing data straddles tiers (NS: C3, C14; low bound Tier 3, high bound Tier 2); Contract status unknown with a named incumbent: consultant review required before final t... | T3 / T2 | Confirmed |
| 65 | Novus Tech Services | 21.0 | 7.5 | 19.5 | 6.0 | 54 | Tier 3 | Band 2 cap, no change | Tier 3 | Review | Scores 2 on both Industry and Company Size; ICP disqualifying factor, tier above Nurture (workflow added): excluded category (Outsourced Digital Marketing); employees and... |  | Confirmed |
| 66 | Harbor Security Labs 01 | 21.0 | 10.0 | 15.0 | 8.0 | 54 | Tier 3 | Band 2 cap, no change | Tier 3 | Review | Missing data straddles tiers (NS: C3, C4, C6; low bound Tier 3, high bound Tier 2); ICP disqualifying factor, tier above Nurture (workflow added): Target ACV below $50K; ... | T3 / T2 | Confirmed |
| 67 | Aster Data Services 02 | 21.0 | 12.5 | 16.5 | 3.5 | 54 | Tier 3 | Not evaluated (status unknown) | Tier 3 | Review | Contact role not verified in last 6 months; C14: former customer churned unhappy; champion evidence conflicts | T3 / T3 | Confirmed |
| 68 | Noble Software Collective 02 | 15.8 | 12.5 | 12.0 | 6.0 | 46 | Tier 3 | Open window (band 1) | Tier 3 | Review | ICP disqualifying factor, tier above Nurture (workflow added): excluded category (Outsourced Digital Marketing); verified incompatible technology |  | Confirmed |
| 69 | Foresight Technology Advisors 01 | 17.5 | 12.5 | 9.0 | 7.0 | 46 | Tier 3 | Band 2 cap, no change | Tier 3 | Review | Conflicting industry classification; Contact role not verified in last 6 months | T3 / T3 | Confirmed |
| 70 | Tidal Security Labs 01 | 7.0 | 11.2 | 19.5 | 5.0 | 43 | Tier 3 | Open window (band 1) | Tier 3 | Review | Scores 2 on both Industry and Company Size; Renewal date on or before As Of Date: confirm whether contract renewed; ICP disqualifying factor, tier above Nurture (workflow... | T3 / T3 | Confirmed |
| 71 | Silverline Data Services 01 | 10.5 | 10.0 | 16.5 | 2.5 | 40 | Tier 3 | Open window (band 1) | Tier 3 | Review | C14: former customer churned unhappy; Total 40 within 2 points of the 40 cutoff; Renewal date on or before As Of Date: confirm whether contract renewed; ICP disqualifying... |  | Confirmed |
| 72 | Cobalt Cloud Partners 02 | 12.2 | 11.7 | 13.5 | 2.0 | 39 | Nurture | Band 2 cap, no change | Nurture | Review | Missing data straddles tiers (NS: C5; low bound Nurture / Inbound Only, high bound Tier 3); Total 39 within 2 points of the 40 cutoff | N / T3 | Confirmed |
| 73 | Driftwood Technology Advisors 02 | 15.8 | 7.5 | 9.0 | 6.0 | 38 | Nurture | Band 2 cap, no change | Nurture | Review | Contact role not verified in last 6 months; Total 38 within 2 points of the 40 cutoff |  | Confirmed |
| 74 | Mosaic Data Services 02 | 10.5 | 8.8 | 15.0 | 4.0 | 38 | Nurture | Not evaluated (status unknown) | Nurture | Review | Missing data straddles tiers (NS: C3, C4; low bound Nurture / Inbound Only, high bound Tier 3); Low confidence C14: Last Meeting date contradicts 'zero prior touchpoints ... | N / T3 | Confirmed |
| 75 | Tidal Software Collective 01 | 15.8 | 6.7 | 13.5 | 2.0 | 38 | Nurture | Not applied | Nurture | Review | Missing data straddles tiers (NS: C5, C14; low bound Nurture / Inbound Only, high bound Tier 3); Total 38 within 2 points of the 40 cutoff | N / T3 | Confirmed |
| 76 | Noble Security Labs 02 | 7.0 | 10.0 | 16.5 | 4.0 | 38 | Nurture | Band 2 cap, no change | Nurture | Review | Missing data straddles tiers (NS: C3, C4, C14; low bound Nurture / Inbound Only, high bound Tier 3); Total 38 within 2 points of the 40 cutoff; Scores 2 on both Industry ... | N / T3 | Confirmed |
| 77 | Helix Cloud Solutions | 14.0 | 5.0 | 12.0 | 6.0 | 37 | Nurture | Band 2 cap, no change | Nurture | Review | Self review escalation: C9: RUBRIC CONFLICT at $250K edge (rule says lower band, band text includes $250K in 8); ESCALATE; Scores 2 on both Industry and Company Size; Rev... |  | Escalated |
| 78 | Driftwood Digital Systems 02 | 10.5 | 5.0 | 16.5 | 5.0 | 37 | Nurture | Band 2 cap, no change | Nurture | Review | Missing data straddles tiers (NS: C3, C4, C5; low bound Nurture / Inbound Only, high bound Tier 3); Contact role not verified in last 6 months | N / T3 | Confirmed |
| 79 | Zenith Software Partners | 7.0 | 6.2 | 16.5 | 5.0 | 35 | Nurture | Band 2 cap, no change | Nurture | Review | Missing data straddles tiers (NS: C3, C4; low bound Nurture / Inbound Only, high bound Tier 3); Self review escalation: C9: RUBRIC CONFLICT at $250K edge (rule says lower... | N / T3 | Escalated |
| 80 | Juniper Technology Advisors 01 | 9.3 | 7.5 | 10.5 | 6.0 | 33 | Nurture | Band 2 cap, no change | Nurture | Review | Missing data straddles tiers (NS: C4; low bound Nurture / Inbound Only, high bound Tier 3) | N / T3 | Confirmed |
| 81 | Quantum Integration Group | 8.8 | 7.5 | 15.0 | 2.0 | 33 | Nurture | Band 2 cap, no change | Nurture | Review | Scores 2 on both Industry and Company Size |  | Confirmed |
| 82 | Horizon Digital Systems 02 | 35.0 | 12.5 | 18.0 | 6.0 | 72 | Tier 2 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Missing data straddles tiers (NS: C2, C3, C4; low bound Tier 3, high bound Tier 2); Contact role not verified in last 6 months; Competitive Lock Gate disqualification | T3 / T2 | Confirmed |
| 83 | Unity Analytics Group 02 | 28.0 | 16.2 | 21.0 | 6.0 | 71 | Tier 2 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Contact role not verified in last 6 months; Competitive Lock Gate disqualification |  | Confirmed |
| 84 | Monarch Analytics Group 01 | 25.7 | 15.0 | 18.0 | 6.0 | 65 | Tier 2 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Contact role not verified in last 6 months; Competitive Lock Gate disqualification | T2 / T2 | Confirmed |
| 85 | Delta Software Collective 01 | 28.0 | 15.0 | 12.0 | 7.0 | 62 | Tier 2 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Missing data straddles tiers (NS: C4; low bound Tier 3, high bound Tier 2); Competitive Lock Gate disqualification | T3 / T2 | Confirmed |
| 86 | Boreal Software Collective 02 | 23.3 | 10.0 | 16.5 | 9.0 | 59 | Tier 3 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Missing data straddles tiers (NS: C3; low bound Tier 3, high bound Tier 2); Conflicting industry classification; Total 59 within 2 points of the 60 cutoff; Competitive Lo... | T3 / T2 | Confirmed |
| 87 | Kestrel Analytics Group 02 | 21.0 | 11.2 | 18.0 | 7.0 | 57 | Tier 3 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Contact role not verified in last 6 months; Leadership change trigger; Scores 2 on both Industry and Company Size; Competitive Lock Gate disqualification |  | Confirmed |
| 88 | Evergreen Analytics Group 01 | 25.7 | 8.3 | 16.5 | 5.0 | 56 | Tier 3 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Missing data straddles tiers (NS: C3, C6; low bound Tier 3, high bound Tier 2); Competitive Lock Gate disqualification | T3 / T2 | Confirmed |
| 89 | Cobalt Analytics Group 02 | 16.3 | 6.2 | 16.5 | 6.0 | 45 | Tier 3 | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Scores 2 on both Industry and Company Size; Competitive Lock Gate disqualification | T3 / T3 | Confirmed |
| 90 | Juniper Digital Systems 01 | 7.0 | 8.8 | 18.0 | 5.0 | 39 | Nurture | Disqualified (Competitive Lock) | Disqualified (Competitive Lock) | Review | Missing data straddles tiers (NS: C2, C3, C4; low bound Nurture / Inbound Only, high bound Tier 2); Contact role not verified in last 6 months; Total 39 within 2 points o... | N / T2 | Confirmed |
| Held | Aspen Analytics Group 01 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Industry | | Confirmed |
| Held | Aspen Cloud Partners 01 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Target ACV ($) | | Confirmed |
| Held | Ion Analytics Group 01 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Industry | | Confirmed |
| Held | Ion Cloud Partners 01 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Target ACV ($) | | Confirmed |
| Held | Quartz Analytics Group 01 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Industry | | Confirmed |
| Held | Quartz Cloud Partners 01 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Target ACV ($) | | Confirmed |
| Held | Yellowstone Analytics Group 02 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Industry | | Confirmed |
| Held | Yellowstone Cloud Partners 02 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Target ACV ($) | | Confirmed |
| Held | Glacier Analytics Group 02 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Industry | | Confirmed |
| Held | Glacier Cloud Partners 02 | n/a | n/a | n/a | n/a | n/a | n/a | Not evaluated | HELD | Held | Fatal field missing: Target ACV ($) | | Confirmed |

## 4. Held accounts: data request

- #21 Aspen Analytics Group 01: needs Industry
- #22 Aspen Cloud Partners 01: needs Target ACV ($)
- #37 Ion Analytics Group 01: needs Industry
- #38 Ion Cloud Partners 01: needs Target ACV ($)
- #53 Quartz Analytics Group 01: needs Industry
- #54 Quartz Cloud Partners 01: needs Target ACV ($)
- #69 Yellowstone Analytics Group 02: needs Industry
- #70 Yellowstone Cloud Partners 02: needs Target ACV ($)
- #85 Glacier Analytics Group 02: needs Industry
- #86 Glacier Cloud Partners 02: needs Target ACV ($)

## 5. Self review (prompt 06)

- Accounts reviewed: 100. Criteria rechecked: 1400 (14 times 100). Each criterion was derived again from the rubric bands, top down, in a separate program that does not share code with the first pass, then compared.
- Mismatches between first pass and recheck: 5. Corrections made: 0. Unresolved: 0.
- All 5 mismatches are the same rubric conflict at C9 and are **escalated, not resolved**: the band table puts exactly $250K in the 8 band, while the edge value rule sends $250K to the lower band (6). First pass kept 6.
- Four more accounts are escalated for a two reading question the recheck could not settle: C8 with Incumbent Contract Status 'No incumbent' but Incumbent Satisfaction 'Dissatisfied'. First pass and recheck both gave 8 (no competitor in place); the other reading gives 10.
- Checks a to i: evidence citations, band selection, NS versus absence, precedence rules, caps, source hierarchy, forbidden evidence, roll up math (including low and high bounds for every NS account), and the gate (band, satisfaction move, tier effect) all passed except the escalated items above. Check a first reported 38 false failures because contact names with an apostrophe (Brian O'Connor) broke my quote parsing; I fixed the checker and reran, and no scoring change was involved.

| Account | Criterion | Reading 1 (kept) | Reading 2 | Total and tier under reading 2 |
|---|---|---|---|---|
| #4 Vanguard Integrators | C9 | 6 | 8 | 73 (T2), tier unchanged |
| #6 Apex ServiceNow Partner | C9 | 6 | 8 | 73 (T2), tier unchanged |
| #8 Optima Cloud Solutions | C9 | 6 | 8 | 75 (T2), tier unchanged |
| #19 Zenith Software Partners | C9 | 6 | 8 | 36 (N), tier unchanged |
| #20 Helix Cloud Solutions | C9 | 6 | 8 | 39 (N), tier unchanged |
| #25 Cedar Enterprise Solutions 01 | C8 | 8 | 10 | 81 (T1), tier unchanged |
| #43 Lighthouse Security Labs 01 | C8 | 8 | 10 | 70 (T2), tier unchanged |
| #73 Aster Enterprise Solutions 02 | C8 | 8 | 10 | 67 (T2), tier unchanged |
| #91 Jasper Security Labs 02 | C8 | 8 | 10 | 73 (T2), tier unchanged |

No escalated reading changes any tier. Limit of this check: the same model wrote both programs, so agreement shows internal consistency, not independent verification. A consultant spot check of the Acceptable group and a sample of criteria is still needed.

## 6. Interpretation calls to confirm

The rubric leaves these open. I chose the most literal reading and flagged it so you can overrule it.

1. **C9 at exactly $250K** scored 6 (edge value rule); band text says 8. Escalated (5 accounts, no tier change).
2. **C1 cross profile pairs** (for example FinTech SaaS with Cloud Infrastructure & DevOps) scored 6, because the same profile rule bars combining profiles and the pair is not a listed combination. They are routed to review as conflicting classification (14 accounts).
3. **C10 single product, single department** scored 2 (no visible expansion path in the record). A reader could argue for 4.
4. **C11** uses the reference list proxy (revenue $100M or more, or 500 or more employees). The weak band (4) never applies because no evidence is partial.
5. **C12 similar deal win rate** is treated as favorable only when budget is confirmed and the account is a SaaS, mid market or scaling enterprise company, since the baseline is 50 percent or more only with confirmed budget. This is an inference from the reference list, not account data.
6. **C13** 'Warm intro via executive sponsor' scored 8 (mutual connection able to introduce an executive), then capped at 6 when role verification is blank or older than 6 months. 'Past customer at former employer' scored 6.
7. **C5 and C6 undated records**: positive signal types with no date are not counted (data contract). If no dated evidence remains the criterion is NS rather than 2.
8. **C8 with a renewal date already past** (8 accounts, renewal date August 1, 2026) scored 6 as 'within 6 months', and the gate sends them to review to confirm whether the contract renewed.
9. **Role verification trigger** fires whenever named contacts exist and the verification date is blank or older than 6 months, even when the C13 score is already 6 or lower. This is the literal rubric text and accounts for much of the review volume.
10. **ICP disqualifier check (workflow added, not in the rubric trigger list):** the ICP names hard disqualifiers (excluded category, ACV under $50K, both size measures out of range, verified incompatible tech) that no tier rule enforces. Accounts that hit one but still land above Nurture are routed to review rather than auto rejected, as the ICP says ambiguous cases should be. Remove it if you prefer the rubric triggers only.
11. **Revenue per employee screen** (C2 flag) has no sector norm in the inputs, so I used a standard 1.5 IQR outlier fence on this dataset. It flags row 20 only.
12. **Unknown contract status** triggers mandatory review only when the incumbent is a named incumbent (2 accounts). 8 more scored accounts have Unknown status with 'Multiple alternatives' and are not flagged.

## 7. Data quality limitations and source conflicts

- Legacy Competitive Context says 'No incumbent provider identified' while structured Incumbent Contract Status is Locked (structured used): 6 accounts
- Existing Connections says cold account with zero prior touchpoints, but Last Contact Date or Last Meeting Date is populated: 24 accounts
- Incumbent Contract Status Locked but Incumbent / Competitor blank: 6 accounts
- Incumbent Contract Status 'No incumbent' but Incumbent Satisfaction populated (4 Dissatisfied, 1 Neutral): 5 accounts
- Legacy Tech Stack text does not mention the structured CRM (legacy ignored for C3, per rubric): 41 accounts
- Rows 21 to 100 are invented fixtures that reuse narratives from 20 seed rows, so results measure routing and rule behavior, not scoring accuracy. No expected answers exist for this set.
- Many criteria are NS by design: C3 NS in 36 scored accounts, C4 NS in 40, C5 NS in 15, C6 NS in 10.

## 8. Quality control checklist status

- Done: inputs gated, no validation assets read, no ground truth field, source hierarchy applied, NS tested with low and high bounds, exact .5 totals rounded up, tier cutoffs applied to rounded totals, As Of Date stated for every gate calculation, gate applied to Locked contracts only with no cap raising a tier, both implied and post gate tiers reported, self review covered all 1,400 criteria.
- Not done (needs a human): consultant approval of every tier, the 10 percent sampled check of Acceptable accounts, review of every flagged account, human override and data entry through the correction template.

## 9. Your input (Step 7)

Challenge any account or criterion. To submit approvals, data corrections, supplied data, overrides, context notes or escalations, use `templates/Human_Review_Input_Template.csv` or plain language. Data needs a source and a date, overrides need the governing rubric band and evidence. I will rescore, rerun the self review checks on changed criteria, and recompute totals, tiers and gate results. Until then every result stays PROVISIONAL.
