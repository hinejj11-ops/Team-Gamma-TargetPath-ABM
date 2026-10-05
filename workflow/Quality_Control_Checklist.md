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
- [ ] NS values and incomplete dimensions are flagged correctly.
- [ ] Stale evidence thresholds were applied.
- [ ] Dimension weights and total rounding were calculated correctly.
- [ ] Tier cutoffs were applied to the rounded total.
- [ ] All mandatory review triggers were surfaced.
- [ ] Human overrides include evidence and rationale.
- [ ] Strategic outliers were reviewed rather than score-manipulated.
- [ ] Final portfolio output contains data-gap and review status.
- [ ] Validation comparison, when performed, occurred only after a blind run.
- [ ] Validation disagreements were adjudicated rather than automatically trained away.
- [ ] Synthetic test assets are clearly distinguished from production client data.