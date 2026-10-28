# Competitive Lock Gate: Assumptions and Open Items

**Status:** The gate was confirmed by TargetOrate. This file is kept as the record of the assumptions behind it and may be updated when TargetOrate reviews the delivered files. The gate itself is in `FIOR_Scoring_Rubric_10_2_2026.md` (Competitive Lock Gate) and `MASTER_PROMPT.md` (Step 5A). Tests are in `validation/Competitive_Lock_Gate_Test_Scenarios.md`.

## What came from TargetOrate and what came from Team Gamma

| Element | Source |
|---|---|
| Three bands based on renewal timing: score normally near renewal, cap at Tier 3 in the middle, disqualify when far out or locked with no date | TargetOrate feedback |
| Windows of 12 and 24 months, with reasoning (6 to 9 month sales cycle, evaluation usually starts 9 to 12 months before renewal) | TargetOrate feedback |
| Dissatisfied moves up one band, satisfied moves down one band, unknown leaves the score unchanged | TargetOrate feedback |
| Incumbent Satisfaction means the account's satisfaction with its current vendor, populated in production by TargetOrate | TargetOrate feedback |
| Exact boundaries: under 12 months, 12 to 24 inclusive, over 24 | Team Gamma decision, 2026-10-11 |
| Everything listed under Assumptions below | Team Gamma assumption |

## Assumptions

| ID | Assumption | Where it applies | Impact if wrong |
|---|---|---|---|
| A1 | Boundaries are under 12 months (open), 12 to 24 inclusive (capped), over 24 (disqualified). The feedback used "within 12 months" and "12 to 24 months", which overlap at 12, so the team chose the boundaries. | Rubric gate Step 1 | Only accounts renewing within about a day of 12 or 24 months |
| A2 | The gate applies only when Incumbent Contract Status is `Locked`. A named incumbent with no stated lock is not treated as locked. This is a new field; Iteration 6 data stored the word `Locked` in the satisfaction column. | Rubric gate; data matrix; dataset | If TargetOrate has no lock indicator, lock must be inferred, which changes which accounts the gate touches |
| A3 | Unknown or blank contract status means the gate cannot be resolved and a mandatory consultant review is required for accounts with a named incumbent. An unknown never costs the account points. | Rubric gate | A locked account hiding behind a blank keeps an overstated tier |
| A4 | Locked with no renewal date is Band 3 (disqualify). If the structured satisfaction field says `Dissatisfied`, it moves up to Band 2 (cap at Tier 3). | Rubric gate; scenarios G05, G11 | Changes outcome for undated locked accounts |
| A5 | The satisfaction move applies in every band, so a satisfied locked account renewing in 12 to 24 months is disqualified, and one renewing under 12 months is capped at Tier 3. This applies the feedback literally. | Scenarios G12 to G14 | May be harsher than TargetOrate intends |
| A6 | Satisfaction evidence comes only from the structured Incumbent Satisfaction field. The legacy narrative Competitive Context field cannot substitute. | Rubric gate Step 2 | Pioneer's narrative says "dissatisfied" but its structured value is `Unknown` and it is not locked, so it is unaffected today |
| A7 | A renewal date on or before the As Of Date is treated as Band 1 and sent to consultant review, because we cannot tell whether the contract renewed. | Rubric gate rule 2; scenario G16 | Stale dates could wrongly open or hide an account |
| A8 | Months are calendar months. If the target day does not exist, the last day of that month is used. | Rubric gate Step 1; scenario G22 | Edge dates only |
| A9 | The Scoring As Of Date is a required input for each run, not the run clock, so the same record and date always give the same result. | MASTER_PROMPT inputs and Step 0 | Without it, results change silently as time passes |
| A10 | A cap never raises a tier. Tier 3 and Nurture stay as they are. | Rubric gate Step 3 | Low |
| A11 | Disqualified accounts keep their score, are listed at the end of the ranking, and go to the consultant. Caps do not go to the consultant on their own. This keeps review volume low. | MASTER_PROMPT Steps 5A and 8; human approval doc | Review volume ceiling; see question 7 |
| A12 | The 12 and 24 month windows are defaults. A client ICP may set different windows. | ICP template and example | If TargetOrate wants fixed windows, remove the ICP option |
| A13 | C8 clarification: `Locked` with renewal 12 or more months out, or no date, scores 2. `Locked` renewing in more than 6 and under 12 months scores 4. This matches the C8 scores of the earlier iteration. | Rubric C8 | The old C8 bands overlapped ("renews in more than 6 months" versus "locked") |
| A14 | The gate changes the recommended tier only. Criterion scores, totals, and C12 are not changed. | Rubric gate | If TargetOrate wants C12 to reflect the lock, C12 needs a rule |
| A15 | Iteration 7 dataset recoding: rows that held `Locked` in Incumbent Satisfaction now have contract status `Locked` and satisfaction `Unknown`; "Multiple alternatives" rows are `Not locked`; blank incumbents are `No incumbent`; Pioneer is `Unknown`. | `data/20_Company_Dataset_Iteration7.csv` | Test data only |
| A16 | The expected outcomes and the 22 gate scenarios were written by Team Gamma. They test that the gate follows its rules, not that the rules are right. | `validation/` | An independent check would need someone who did not write the rules |
| A17 | The vendor event reference schema and evidence controls are built; no event may be used until a public source is verified. | Not in the gate | See question 9 |

## Questions for TargetOrate (Karen)

Ask the first five first.

| # | Question | Why it matters |
|---|---|---|
| 1 | Do we read your three bands correctly: under 12 months scores normally, 12 to 24 months inclusive is capped at Tier 3, over 24 months is disqualified? | Confirms A1 |
| 2 | Should evidence that the incumbent is satisfied move a locked account down a band at every band, including from capped to disqualified? Or should satisfaction only ever remove an upgrade? | A5 |
| 3 | When a locked account has no renewal date but is dissatisfied, should it move from disqualified to capped at Tier 3? | A4 |
| 4 | Will TargetOrate have a contract lock indicator in production data, separate from satisfaction? If not, can we infer a lock from a named incumbent plus a future renewal date? | A2 |
| 5 | Should a vendor event at the incumbent (price rise, acquisition, compliance scandal) also count as evidence of dissatisfaction for the gate band, so a locked account whose vendor is in trouble can leave the cap? Your note described it as moving the C8 band only. | A17; avoids a capped account staying hidden when its vendor is in crisis |
| 6 | Should disqualified accounts be dropped, or kept on a quarterly watch list so they are re screened when the window changes? | A11; your point about staying visible |
| 7 | Do disqualifications and past renewal dates going to review, with caps not reviewed, fit your ceiling on review volume? | A11 |
| 8 | Are 12 and 24 months fixed for every TargetOrate client, or should each client's ICP set them? | A12 |
| 9 | Do you want the vendor event reference list built now, or after handover? | A17 |
| 10 | If the renewal date is already in the past, should we assume the contract renewed, treat the account as open, or ask a consultant? | A7 |
| 11 | How old can satisfaction or dissatisfaction evidence be before we ignore it? | Not yet defined; no staleness rule exists for this field |
| 12 | If an account's narrative says "dissatisfied" but the structured satisfaction field is `Unknown`, do you agree the structured field wins? | A6 |
| 13 | Could someone at TargetOrate who did not write these rules check five or six gate cases so we have an independent check? | A16 |

## Other open questions for TargetOrate (review rule and scoring)

| # | Question | Why it matters |
|---|---|---|
| 14 | Do you agree with one review rule for missing data: hold the account only if Company Name, Industry or Target ACV is missing, and otherwise review only when setting the missing criteria to 2 versus 10 changes the tier? | Replaces three conflicting rules |
| 15 | Is a ceiling of 25 percent of accounts per run reviewed (about 6 hours for 25 accounts at 15 minutes each) realistic for your consultants? What is the real figure? | The ceiling is a Team Gamma estimate |
| 16 | When a run exceeds the ceiling, is it acceptable to release the accounts not reviewed as provisional? | Overflow handling |
| 17 | Should totals ending exactly in .5 round up? | New tie rule |
| 18 | Can production data carry two trigger types per account so C6 can reach 10? | C6 band 10 was unreachable with one trigger |
