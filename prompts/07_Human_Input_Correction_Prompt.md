# Human Input and Correction Prompt

## Purpose
Give the consultant a defined point in the chain to review results, add information, and correct the AI. Corrections flow back through the scoring math instead of being patched in by hand.

## When to run
After the self review (`prompts/06_Criterion_Self_Review_Prompt.md`) and before outputs are finalized. Run it again whenever the consultant returns with new data.

## Prompt

### Part A: Present the review packet, then stop
Present to the consultant:
1. The portfolio table after self review, with recommended tier and review status.
2. The review queue. For each flagged account or criterion: the AI result, the evidence used, the trigger, and what would resolve it (data needed or decision needed).
3. Any self review escalations.
4. A reminder that the consultant may also challenge any account or criterion that is not in the queue.
5. A request for input, using `templates/Human_Review_Input_Template.csv` or plain language.

Then stop and wait. Do not produce final outputs and do not mark any account approved until the consultant responds or tells you to release the results as provisional.

### Part B: Accept and check the input
Accept these input types:
- **APPROVE.** Accept the AI result unchanged.
- **DATA CORRECTION.** A field in the account record is wrong. Needs the corrected value, a source, and a date.
- **DATA SUPPLIED.** Fills a blank or Unknown field. Needs the value, a source, and a date.
- **OVERRIDE.** Change a criterion score. Needs the replacement score, the governing rubric band, and the evidence.
- **CONTEXT NOTE.** A judgment that does not change a score, such as a documented strategic exception. It is recorded and carried into the final output.
- **ESCALATE.** Send a methodology or rubric question to the workflow owner.

Checks before applying anything:
- Every input names the company, the criterion or field, the reviewer, and the date.
- Data inputs without a source and date are logged but not used. The criterion stays NS and you ask for the source.
- If an override's stated evidence does not meet the named rubric band, say so, show the mismatch, and ask the reviewer to confirm the override with a rationale or choose ESCALATE. A confirmed override is applied and marked "differs from rubric band".
- A request to change rubric bands, weights, tier cutoffs, or ICP benchmarks is not a correction. Treat it as ESCALATE. Do not create a local rule.
- Never fill a missing fact from intuition or outside knowledge.
- Keep the original AI result next to every change.

### Part C: Apply the input and recompute
1. Change the working copy of the record only, never the original dataset file. Mark each changed field "Human supplied" or "Human corrected" with its source and date.
2. Rescore only the criteria that use a changed field (use the Data Requirements Matrix to map fields to criteria). For an override, use the reviewer's score.
3. Run the self review checks (a to i in prompt 06) on every changed criterion.
4. Recompute the dimension scores, total, rounded total, tier, Competitive Lock Gate result, and review triggers. State which triggers cleared and which new ones appeared. Flag any account whose correction or override moves it across a tier cutoff so the reviewer sees it.
5. Final tier assignment still requires consultant approval. Mark an account approved only when the consultant says so.

## Return
- **Human input log.** Company | Criterion or Field | Input Type | Original AI Result or Value | Human Value | Source or Evidence | Reviewer and Date | Resulting Score | Resulting Total and Tier | Crossed Tier Cutoff (Y/N) | Open Follow Up.
- **Updated portfolio table.** Accounts still waiting on human input are labeled PROVISIONAL.

## Blind validation runs
In a blind validation run (`prompts/05_Validation_Adjudication_Prompt.md`), accept no human input. Return the review packet, label every result PROVISIONAL, and note that this step was not exercised.
