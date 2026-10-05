# Consultant Review Prompt

## Purpose
Standardize human-in-the-loop review of accounts flagged by the scoring engine.

## Prompt
Review only the accounts/criteria flagged for consultant review. Treat the original FIOR rubric and client ICP as authoritative; do not optimize toward a desired tier or score.

For every flagged item:
1. State the AI score or NS and the exact evidence used.
2. State the review trigger.
3. Determine whether the issue is a data gap, contradictory evidence, stale evidence, rubric ambiguity, strategic outlier, or AI execution error.
4. Choose one disposition: APPROVE AI RESULT; OVERRIDE; REQUEST DATA; ESCALATE METHODOLOGY.
5. For an override, record the replacement score, exact evidence, governing rubric band, reviewer rationale, and reviewer identity/date.
6. Never fill a missing fact from intuition or outside knowledge unless the workflow has explicitly authorized and documented external research.

Return an approval log with Company, Criterion, AI Result, Trigger, Disposition, Approved Result, Rationale, and Follow-up.