# TargetPath Quality-Control Checklist

Use before releasing a scored ABM portfolio.

- [ ] Required inputs are present and readable.
- [ ] Completed ICP supplies C1-C4 benchmarks.
- [ ] Account dataset conforms to the Data Requirements Matrix.
- [ ] Validation-only assets were quarantined during normal scoring.
- [ ] No Ground Truth validation field influenced scoring.
- [ ] Source hierarchy was applied consistently.
- [ ] Blank/Unknown evidence was not treated as affirmative absence.
- [ ] Structured V2 fields took precedence over legacy narrative fields.
- [ ] Every C1-C14 result has evidence, band, confidence, and review rationale.
- [ ] Every NS was tested with the low (2) and high (10) bounds; review was triggered only where the tier differs, and fatal fields (Company Name, Industry, Target ACV) were held.
- [ ] The share of accounts sent to review was reported against the 25 percent ceiling, and accounts not reached are labeled provisional.
- [ ] Totals ending exactly in .5 were rounded up.
- [ ] 10 percent of `Acceptable` accounts (at least 3) were spot checked by a consultant, and any error widened the check to the whole group.
- [ ] The scoring file contained no Ground Truth column (see `tools/split_ground_truth.py`).
- [ ] Stale evidence thresholds were applied.
- [ ] Dimension weights and total rounding were calculated correctly (exact .5 rounds up).
- [ ] Tier cutoffs were applied to the rounded total.
- [ ] Self review covered all 14 criteria for every account (criteria rechecked equals 14 times accounts).
- [ ] Every self review mismatch was corrected with a rubric citation or escalated; no score was changed to reach a tier.
- [ ] A Scoring As Of Date was stated and used for every gate calculation.
- [ ] The Competitive Lock Gate was applied only to `Locked` contracts, with the correct band, satisfaction move, and tier effect, and no cap raised a tier.
- [ ] Both the score implied tier and the post gate tier are reported, and gate disqualifications were routed to the consultant.
- [ ] All mandatory review triggers were surfaced.
- [ ] Human overrides include evidence and rationale.
- [ ] Human supplied or corrected data carries a source and date and is marked in the audit trail.
- [ ] Original AI results are kept beside every human change, and totals, tiers, and triggers were recomputed.
- [ ] Accounts still waiting on human input are labeled provisional.
- [ ] Strategic outliers were reviewed rather than score-manipulated.
- [ ] Final portfolio output contains data-gap and review status.
- [ ] Validation comparison, when performed, occurred only after a blind run.
- [ ] Validation disagreements were adjudicated rather than automatically trained away.
- [ ] Synthetic test assets are clearly distinguished from production client data.