# Exception Handling Prompt

## Purpose
Handle scoring exceptions without silently inventing evidence or bypassing human approval.

## Prompt
Classify each exception using the TargetPath source hierarchy and Data Requirements Matrix.

Exception classes:
- MISSING EVIDENCE: required field blank/Unknown/unverified -> NS where required.
- EXPLICIT NEGATIVE: verified absence -> use the applicable numeric rubric band.
- CONTRADICTION: structured sources conflict -> use source hierarchy and flag review.
- STALE EVIDENCE: score only as the rubric permits and flag when thresholds are exceeded.
- STRATEGIC OUTLIER: score normally, then route for consultant review; do not manipulate the score.
- RUBRIC AMBIGUITY: do not invent a new anchor. Record competing interpretations and escalate methodology.
- DATA/SCHEMA ERROR: malformed or unavailable required input -> stop or route according to severity.
- VALIDATION CONFLICT: never change production scoring merely to match an answer key; send to adjudication.

Return Exception Class, Affected Criterion, Evidence, Temporary Disposition, Required Human Action, and whether scoring may continue.