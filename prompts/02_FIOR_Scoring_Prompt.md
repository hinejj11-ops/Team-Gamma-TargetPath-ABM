# FIOR Scoring Prompt

## Purpose
Execute the frozen TargetPath FIOR scoring engine after input validation passes.

## Prompt
Using `MASTER_PROMPT.md` as the authoritative orchestration instructions, score every account against the FIOR rubric, completed client ICP, Client Target Reference Lists, Criteria Ranking Model, and FIOR Data Requirements Matrix.

Requirements:
- Apply the source hierarchy exactly.
- Score C1-C14 independently from permitted structured evidence.
- Preserve all Iteration 6 evidence-governance rules, including same-profile C1 matching, missing-versus-absent C3/C4 handling, explicit-negative C5/C6 handling, C13 relationship precedence, and C14 champion semantics.
- Return NS rather than guessing when required evidence is unavailable.
- Retain criterion-level evidence, benchmark, band, confidence, and review rationale.
- Compute weighted Fit, Intent, Opportunity, and Relationship scores and the rounded composite only as permitted by the rubric.
- Apply tier and mandatory-review rules.
- Do not read or use `/validation/` or validation-only ground-truth fields.

Return the ranked portfolio table defined in `MASTER_PROMPT.md` plus an audit trail sufficient for consultant review.