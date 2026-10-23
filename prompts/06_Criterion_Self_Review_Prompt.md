# Criterion Self Review Prompt

## Purpose
Have the scoring engine check its own work. After the first scoring pass, every criterion for every account is derived again and compared with the first pass before anything goes to a human.

## When to run
After Steps 1 to 5 of `MASTER_PROMPT.md` (first pass scores, roll ups, tier, review status) and before the human input checkpoint (`prompts/07_Human_Input_Correction_Prompt.md`).

## Prompt
You are the TargetPath self review auditor. First pass scoring is complete. Recheck every criterion C1 to C14 for every account, and recheck the roll up math.

Rules:
1. Work one account at a time and one criterion at a time. Do not sample and do not skip criteria that look obvious.
2. Derive first, compare second. For each criterion, reread the account evidence and the rubric band table, and derive the score again from the top band down before looking at the first pass score. Then compare the two.
3. Run these checks on every criterion:
   - **a. Evidence exists.** Every field and value cited is actually in the account record, with the value as cited.
   - **b. Correct band.** The first band whose condition is fully met was taken. An odd score (9, 7, 5, 3) states which conditions were met.
   - **c. Missing versus absent.** Blank or Unknown evidence returned NS, not a low score. Explicit negative values were treated as absence only where the rubric allows it.
   - **d. Precedence rules.** Structured V2 fields over legacy narrative fields; C1 same profile and exclusion rules; C3 and C4 missing versus absent rules; C5 and C6 explicit negative rules; C13 relationship precedence; C14 customer status first, then champion meaning.
   - **e. Caps and flags.** C7 inferred timeline cap; C13 role verification cap; stale data thresholds; leadership change flag; confidence level consistent with the evidence.
   - **f. Source hierarchy.** ICP benchmark cited for C1 to C4. Reference lists used only where the ICP does not own the parameter.
   - **g. Forbidden evidence.** Nothing under `/validation/` and no Ground Truth field influenced any score.
   - **h. Math.** Dimension averages use scored criteria only, correct multipliers, correct sum, rounding to the nearest whole number with exact .5 rounding up, correct tier cutoff, the low and high bound tiers computed for every account with an NS (review only when they differ, held only when a fatal field is missing), and every review trigger evaluated (including within 2 points of a cutoff).
   - **i. Competitive Lock Gate.** Applied only to `Locked` contracts; band computed from the Scoring As Of Date using under 12, 12 to 24 inclusive, and over 24 or no date; satisfaction move taken from the structured field only; cap never raised a tier; both the score implied tier and the post gate tier reported.
4. Resolve each disagreement between the re derivation and the first pass:
   - If the rubric text and the cited evidence support the re derived score, correct the score, record both scores, and recompute that account's dimension scores, total, tier, and review status.
   - If the rubric text does not settle it (two reasonable readings), do not choose. Keep the first pass score, record both readings, and mark ESCALATE for consultant review.
5. Never change a score because of the tier it would produce, to match an expected result, or to look consistent with another account. Consistency across accounts comes from applying the same rubric rule, not from copying scores.
6. Run the recheck once. If a correction changes an account, recheck only the affected criteria and roll ups one more time. Do not iterate further. Anything still unresolved goes to the consultant.
7. Do not read or use anything under `/validation/`.

## Return
- **Self review log.** One row per mismatch or correction: Company | Criterion | First Pass | Recheck | Check That Failed (a to i) | Resolution (Corrected / ESCALATE) | Final Score | Rubric Citation. For criteria that matched, a single line per account is enough, for example "Acme: C1 to C14 confirmed, checks a to i passed".
- **Per account result.** Confirmed, Corrected, or Escalated.
- **Updated portfolio rows** for every corrected account.
- **Summary counts.** Accounts reviewed, criteria rechecked (should equal 14 times the number of accounts), mismatches found, corrections made, escalations raised, and which checks failed most often.

A self review escalation is a workflow level review trigger. It adds routing to the consultant. It never changes a rubric band, weight, tier cutoff, or ICP benchmark.
