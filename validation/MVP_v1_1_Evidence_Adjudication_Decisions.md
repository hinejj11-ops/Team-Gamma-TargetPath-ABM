# MVP v1.1 — Evidence Adjudication Decisions (Provisional)

**2026-10-12 | 2026-10-11 scoring as-of | Not human approved**

These decisions are based on the rubric, completed synthetic ICP and structured account evidence. They **do not overwrite** the historical expected-score key. Any changed criterion must flow through a new full composite and gate calculation before release.

| Account(s) | Criterion | Key / candidate | Evidence-based ruling | Status |
|---|---|---|---|---|
| Stratagem Software; Pinnacle Enterprise Tech | C1 | 10 / 4 | **10.** IT Services & Consulting + Cybersecurity & Compliance match ICP 1 together; candidate omitted this ICP profile. | Candidate defect identified |
| Pioneer Digital Services | C1 | 10 / 8 | **10.** Enterprise Software + Cybersecurity & Compliance match ICP 1 together; candidate's reduced map was incomplete. | Candidate defect identified |
| Nexis Cloud Systems | C4 | 8 / 4 | **4.** ISO 27001 is `No`, an affirmative missing required compliance item. Rubric C4=8 requires all required compliance met. | Draft key challenge |
| Quantum Integration Group | C4 | 8 / 4 | **4.** ISO 27001 is `No`; cannot classify as a noncritical gap without explicit evidence. | Draft key challenge |
| Crestview Cloud Group | C4 | NS / 10 | **NS.** HealthTech SaaS with HIPAA `Unknown`; applicable compliance unresolved. | Candidate defect identified |
| Vanguard Integrators; Meridian IT Solutions; Veritas Cloud Partners; AlphaCentric IT | C8 | NS / 8 | **8.** Structured `Incumbent Contract Status=No incumbent` satisfies the rubric's no-competitor anchor. | Draft key challenge |
| Pioneer Digital Services | C8 | 4 / NS | **NS + mandatory review.** Structured status `Unknown` with an incumbent mentioned in narrative is not affirmative evidence of contract status; rubric's unknown-date rule is distinct. | Needs consultant decision |
| Nexis; Apex; Summit; Optima; Crestview; Helix | C14 | 8 / 10 | **10** when structured champion says `VP Mktg actively pushing for evaluation`. The rubric explicitly identifies active internal advocacy as 10. | Draft key challenge |
| Quantum Integration Group | C14 | 8 / 2 | **2** if `None identified yet` and no meeting/engagement evidence; named contacts alone do not create engagement. | Draft key challenge |
| Zenith Software Partners | C14 | 8 / 4 | **4** for marketing-only nurture/webinar history with no champion or direct meeting. | Draft key challenge |
| Veritas Cloud Partners | C13 | 10 / 8 | **Not yet adjudicated.** `Past customer at former employer (strong warmth)` does not establish active VP-level relationship and may support 8 or 6 depending on warm introduction evidence. | Escalate |
| All C12 mismatches | C12 | various | Historical win-rate baseline only supports a favorable factor under the stated applicability rule; budget confirmation and competitive favorability must be separately tested. Do not assume a budget-unconfirmed account has a favorable historical rate. | Re-derive individually |
| C5 mismatches | C5 | various | Count only distinct, dated positive signal types within 30/90 days of 2026-10-11; ignore explicit negatives and undated narrative. | Re-derive individually |

## Implementation defects to fix

- Candidate C1 profile map omitted same-profile pairings explicitly present in the completed ICP.
- Candidate C4 must test *applicable* compliance requirements and return NS for applicable Unknown values.
- Candidate C8 must distinguish known `No incumbent` from `Unknown` contract status; a named incumbent with unknown contract status always routes to review.
- Candidate C12 collapsed a three-factor model into two flags.
- Candidate C14 must use current champion advocacy, customer status and actual engagement evidence rather than senior titles alone.

## Release gate

The candidate is **not a validated production scoring engine**. Historical expected results are **not independently verified ground truth**. No consultant has approved a changed expected-score entry. Next: implement the above in a reproducible scorer, rerun all 280 cells with evidence citations and self-review, recalculate composite and competitive gate, then obtain actual consultant adjudication. Do not merge PR #19 or start 100-company scoring until those steps are complete.
