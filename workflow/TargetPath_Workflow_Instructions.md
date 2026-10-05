# TargetPath ABM Workflow Instructions

## Objective
Run a repeatable AI-assisted ABM account-scoring process with explicit human controls.

## Operating Chain
1. **Prepare inputs.** Complete the client ICP and account-data template; maintain the TargetOrate reference lists.
2. **Gate inputs.** Run `prompts/01_Input_Validation_Prompt.md`. STOP if the ICP is absent; otherwise resolve fatal errors and identify NS/review items.
3. **Score accounts.** Run `prompts/02_FIOR_Scoring_Prompt.md` using `MASTER_PROMPT.md` and the frozen scoring artifacts.
4. **Handle exceptions.** Use `prompts/04_Exception_Handling_Prompt.md` for missing, contradictory, stale, ambiguous, or strategic-outlier cases.
5. **Decision gate.** If no mandatory review trigger exists, proceed to output. If a trigger exists, route only the affected accounts/criteria to consultant review.
6. **Consultant review.** Run `prompts/03_Consultant_Review_Prompt.md`; document approve/override/request-data/escalate decisions.
7. **Human approval.** Follow `workflow/Human_Approval_Instructions.md`. AI recommendations are not self-approving.
8. **Publish outputs.** Populate the portfolio and account-summary templates. Preserve audit rationale and data-gap flags.
9. **Validate changes.** When testing workflow/rubric changes, run `prompts/05_Validation_Adjudication_Prompt.md` against quarantined test assets only after the blind run.

## Source hierarchy
FIOR Rubric -> Completed Client ICP -> Client Target Reference Lists -> Account Dataset -> No unsupported assumptions.

## Production boundary
The included ICP, account data, and validation results are synthetic capstone assets. Replace client-specific examples in production; preserve the workflow controls.