# Exception Handling Prompt

## Purpose
Handle scoring exceptions without silently inventing evidence or bypassing human approval.

## Prompt
Classify each exception using the TargetPath source hierarchy and Data Requirements Matrix.

Exception classes:
- MISSING EVIDENCE: required field blank/Unknown/unverified -> NS where required. If the field is Company Name, Industry or Sub-Industry, or Target ACV, hold the account and request the data. Otherwise compute the low (NS=2) and high (NS=10) bound totals; review only if the two tiers differ, else add an audit note.
- EXPLICIT NEGATIVE: verified absence -> use the applicable numeric rubric band.
- CONTRADICTION: structured sources conflict -> use source hierarchy and flag review.
- STALE EVIDENCE: score only as the rubric permits and flag when thresholds are exceeded.
- STRATEGIC OUTLIER: score normally, then route for consultant review; do not manipulate the score.
- RUBRIC AMBIGUITY: do not invent a new anchor. Record competing interpretations and escalate methodology.
- SELF REVIEW DISCREPANCY: first pass and recheck disagree and the rubric text does not settle it -> keep the first pass score, record both readings, escalate to the consultant.
- DATA/SCHEMA ERROR: malformed or unavailable required input -> stop or route according to severity.
- VALIDATION CONFLICT: never change production scoring merely to match an answer key; send to adjudication.

Return Exception Class, Affected Criterion, Evidence, Temporary Disposition, Required Human Action, and whether scoring may continue.