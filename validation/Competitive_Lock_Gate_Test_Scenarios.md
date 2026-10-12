# Competitive Lock Gate Test Scenarios (Iteration 7, draft)

**Status:** Written by Team Gamma, not by TargetOrate. Expected results follow the gate rules in `FIOR_Scoring_Rubric_10_2_2026.md` as currently proposed. They are a regression check on the gate logic, not an independent accuracy measure. Open assumptions are listed in `workflow/Competitive_Lock_Gate_Open_Items.md`.

This file is validation only. Do not read it during a normal scoring run.

## How to use
Each scenario isolates the gate. The score implied tier comes from the account total as usual, and the gate is applied to it. Run the gate prompt logic (Step 5A in `MASTER_PROMPT.md`) on the inputs and compare the result with the last two columns. Expected results were produced by a script and checked against hand written expectations for every row.

Band key: 1 = open window (under 12 months), 2 = capped at Tier 3 (12 to 24 months inclusive), 3 = disqualified (over 24 months, or locked with no renewal date). "Band 2 to 1" means band 2 from the renewal date, moved to band 1 by the satisfaction rule.

| ID | Scenario | As Of Date | Score Implied Tier | Contract Status | Renewal Date | Satisfaction | Band (date to final) | Gate Action | Expected Recommended Tier | Review Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| G01 | Renewal 11 months 29 days out (under 12, exclusive) | 2026-10-11 | Tier 1 | Locked | 2027-10-10 | Unknown | 1 to 1 | Open window: no cap | Tier 1 | N |
| G02 | Renewal exactly 12 months out (lower edge of capped band, inclusive) | 2026-10-11 | Tier 1 | Locked | 2027-10-11 | Unknown | 2 to 2 | Capped at Tier 3 | Tier 3 | N |
| G03 | Renewal exactly 24 months out (upper edge of capped band, inclusive) | 2026-10-11 | Tier 2 | Locked | 2028-10-11 | Unknown | 2 to 2 | Capped at Tier 3 | Tier 3 | N |
| G04 | Renewal 24 months plus 1 day out | 2026-10-11 | Tier 1 | Locked | 2028-10-12 | Unknown | 3 to 3 | Disqualified | Disqualified (Competitive Lock) | Y |
| G05 | Locked with no renewal date | 2026-10-11 | Tier 1 | Locked | none | Unknown | 3 to 3 | Disqualified | Disqualified (Competitive Lock) | Y |
| G06 | CloudBridge pattern: 85, Tier 1, renewal 2028-03-25 | 2026-10-11 | Tier 1 | Locked | 2028-03-25 | Unknown | 2 to 2 | Capped at Tier 3 | Tier 3 | N |
| G07 | Cap leaves Tier 3 unchanged | 2026-10-11 | Tier 3 | Locked | 2028-03-25 | Unknown | 2 to 2 | Capped at Tier 3 (no change) | Tier 3 | N |
| G08 | Cap never raises a Nurture account | 2026-10-11 | Nurture / Disqualify | Locked | 2028-03-25 | Unknown | 2 to 2 | Capped at Tier 3 (no change) | Nurture / Disqualify | N |
| G09 | Dissatisfied, beyond 24 months, moves to capped band | 2026-10-11 | Tier 1 | Locked | 2029-03-25 | Dissatisfied | 3 to 2 | Capped at Tier 3 | Tier 3 | N |
| G10 | Dissatisfied, capped band, moves to open window | 2026-10-11 | Tier 1 | Locked | 2028-03-25 | Dissatisfied | 2 to 1 | Open window: no cap | Tier 1 | N |
| G11 | Dissatisfied, locked with no renewal date, moves to capped band | 2026-10-11 | Tier 1 | Locked | none | Dissatisfied | 3 to 2 | Capped at Tier 3 | Tier 3 | N |
| G12 | Satisfied, open window, moves to capped band | 2026-10-11 | Tier 1 | Locked | 2027-06-30 | Satisfied | 1 to 2 | Capped at Tier 3 | Tier 3 | N |
| G13 | Satisfied, capped band, moves to disqualified | 2026-10-11 | Tier 1 | Locked | 2028-03-25 | Satisfied | 2 to 3 | Disqualified | Disqualified (Competitive Lock) | Y |
| G14 | Satisfied, already beyond 24 months, stays disqualified | 2026-10-11 | Tier 2 | Locked | 2029-03-25 | Satisfied | 3 to 3 | Disqualified | Disqualified (Competitive Lock) | Y |
| G15 | Neutral satisfaction causes no move | 2026-10-11 | Tier 1 | Locked | 2028-03-25 | Neutral | 2 to 2 | Capped at Tier 3 | Tier 3 | N |
| G16 | Renewal date already passed: open window plus review | 2026-10-11 | Tier 1 | Locked | 2026-08-01 | Unknown | 1 to 1 | Open window: no cap | Tier 1 | Y |
| G17 | Not locked account with a renewal date: gate not applied | 2026-10-11 | Tier 1 | Not locked | 2028-03-25 | Unknown | n/a | Gate not applied | Tier 1 | N |
| G18 | Contract status Unknown: gate not evaluated | 2026-10-11 | Tier 1 | Unknown | 2028-03-25 | Unknown | n/a | Gate not evaluated (contract status unknown) | Tier 1 | N |
| G19 | No incumbent: gate not applied | 2026-10-11 | Tier 1 | No incumbent | none | none | n/a | Gate not applied | Tier 1 | N |
| G20 | Same record rerun on 2027-03-25 (exactly 12 months to renewal) | 2027-03-25 | Tier 1 | Locked | 2028-03-25 | Unknown | 2 to 2 | Capped at Tier 3 | Tier 3 | N |
| G21 | Same record rerun on 2027-03-26 (under 12 months): moves to open window | 2027-03-26 | Tier 1 | Locked | 2028-03-25 | Unknown | 1 to 1 | Open window: no cap | Tier 1 | N |
| G22 | Month end rule: 12 months from 2028-02-29 is 2029-02-28 (no 29th), so renewal 2029-02-28 is exactly 12 months and capped | 2028-02-29 | Tier 1 | Locked | 2029-02-28 | Unknown | 2 to 2 | Capped at Tier 3 | Tier 3 | N |

## Coverage notes
- The 20 company set (`data/20_Company_Dataset_Iteration7.csv`) exercises only one branch: five locked accounts, all in the capped band, and only CloudBridge changes tier. See `validation/Expected_FIOR_Results_ITERATION7_GATE_DRAFT.csv`.
- No account in the 20 company set is in the open window, over 24 months, missing a renewal date, dissatisfied, or satisfied. Those branches are covered only by the scenarios above. Add accounts for these branches to the 100 company test set.
