# MVP v1.1 — 280-criterion discrepancy audit and remediation worklist

**2026-10-12 | Scoring As Of: 2026-10-11 | Status: REVIEW REQUIRED**

## Reconciliation baseline
The independent rule-based candidate was committed as `validation/MVP_v1_1_Fresh_Scoring_Candidate.csv` **before** inspecting the expected-results files. A later cell-by-cell comparison with `validation/Expected_FIOR_Results_ADJUDICATED_WORKING.csv` identified **249/280 matching C1–C14 cells and 31 mismatches**. This is **raw candidate-to-key agreement (88.9%)**, not model accuracy or verified rubric conformance. The candidate is incomplete and should not be approved.

| Criterion | Mismatches |
|---|---:|
| C1 Industry | 3 |
| C4 Geography/compliance | 3 |
| C5 Intent | 4 |
| C8 Competitive context | 5 |
| C12 Win probability | 6 |
| C13 Relationship | 1 |
| C14 Engagement/champion | 9 |
| **Total** | **31** |

No mismatch in C2, C3, C6, C7, C9, C10 or C11 against this key; matching the key does not prove correctness.

## Evidence-based adjudication examples (not automatically overwritten)

- **Pioneer, Stratagem, Pinnacle — C1:** The first-pass candidate scored 8/4/4, while the key has 10/10/10. The completed ICP explicitly lists Enterprise Software + Cybersecurity & Compliance under different profiles? In particular, ICP 1 includes IT Services & Consulting + Cybersecurity & Compliance as a same-profile match, and Enterprise Software + Cybersecurity & Compliance likewise belongs to ICP 1. These require re-derivation from the ICP table rather than a hand-built subset of profiles. **Candidate implementation defect.**
- **Nexis — C4:** The account has ISO 27001 = `No`; the key gives 8 and the candidate gives 4. Under the rubric, an affirmed *required* compliance gap normally scores 4; the 8 band is only a *noncritical* gap after all required compliance is met. **Key appears inconsistent; escalate before altering key.**
- **Vanguard, Meridian, Veritas, AlphaCentric — C8:** The dataset explicitly says `No incumbent` while the key records NS. The rubric C8 score 8 states `No competitor in place`. **Key appears inconsistent unless a documented override exists.**
- **Pioneer — C8:** `Incumbent Contract Status=Unknown`; the candidate gives NS while the key gives 4. The rubric says an unknown *date* for a known competitor scores 4, but an unknown *incumbent status* requires distinguishing missing evidence from known competitor presence. **Methodology ambiguity; mandatory consultant review.**
- **Nexis and other identified active champions — C14:** The candidate gives 10 for `Identified: VP Mktg actively pushing for evaluation`; the key gives 8. The rubric's Iteration 4 active-champion rule explicitly assigns 10 to current advocacy. **Key appears inconsistent.** Other C14 cases need independent evidence rechecks.
- **C12 (6 mismatches):** The candidate simplified budget, competitive position and historical win-rate handling. Re-evaluate against the reference-list 50% baseline and the exact rubric; do not automatically accept either side.
- **C5 (4 mismatches):** Recompute distinct signal types and their ages as of 2026-10-11; do not count explicit negatives or duplicate types. Some fixture totals may reflect an earlier scoring date.
- **C13 Veritas:** A past customer at a former employer does not necessarily prove a current active VP-level relationship. Verify the role, recency and relationship-strength evidence before accepting the key's 10.

## Corrective work required

1. Fix candidate's incomplete C1 ICP profile map, C3 preferred-technology distinction, C4 unknown-versus-affirmed-failure, C5 distinct signal/date logic, C8 unknown-status behavior, C11 market leader proxy, C12 three-factor win probability, C13 verification cap, and C14 champion/customer precedence. Re-score from the full rubric, not from the expected key.
2. Create **one evidence row per criterion** (280 rows) with exact input field/value, rubric band, confidence, NS rationale, and first-pass vs second-pass decision.
3. Separately adjudicate key inconsistencies; preserve original key and document proposed corrections with rationale and reviewer identity.
4. Recompute all dimensions, half-up totals, tier sensitivity bounds, gate bands and mandatory review flags. No reviewer approval may be simulated.
5. Retest human correction/approval using dated sourced data. Consultant must actually approve before release.

## Acceptance decision

**FAIL / HOLD:** The fresh candidate is diagnostic only. Neither the first-pass implementation nor the draft validation key is established as an independent truth source. Keep PR #19 draft and the 100-company test blocked until the 280-row second-pass audit and human disposition are complete.
