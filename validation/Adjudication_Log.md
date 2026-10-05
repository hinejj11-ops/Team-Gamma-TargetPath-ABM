# Validation Adjudication Log

## Purpose
Preserve human adjudication of residual disagreements after the frozen Iteration 6 blind validation run. This file is validation-only and must never be used as scoring evidence.

## Baseline
- Raw criterion agreement after Iteration 6: 255/280 (91.1%).
- Residual disagreements examined: 25.
- Adjudication categories: model/execution error, validation-key error, rubric ambiguity, data ambiguity.
- This log documents adjudication; it does not authorize the scoring engine to read validation assets during normal runs.

## Adjudicated residuals

| Account | Criterion | Iteration 6 | Original Key | Classification | Adjudicated disposition |
|---|---|---:|---:|---|---|
| Apex ServiceNow Partner | C1 | 8 | 10 | Validation-key error | 8; cross-profile matches cannot create C1=10 |
| Crestview Cloud Group | C1 | 8 | 10 | Validation-key error | 8; cross-profile matches |
| AlphaCentric IT | C1 | 8 | 10 | Validation-key error | 8; cross-profile matches |
| Vanguard Integrators | C3 | NS | 4 | Validation-key error | NS; required Data/Analytics is blank |
| BlueMatrix Technologies | C3 | NS | 4 | Validation-key error | NS; required Data/Analytics is blank |
| Pinnacle Enterprise Tech | C3 | NS | 4 | Validation-key error | NS; required Data/Analytics is blank |
| Zenith Software Partners | C3 | NS | 4 | Validation-key error | NS; required Data/Analytics is blank |
| Quantum Integration Group | C3 | NS | 2 | Model/execution error | 2; explicit incompatible legacy on-prem platform |
| Helix Cloud Solutions | C3 | NS | 2 | Model/execution error | 2; explicit incompatible legacy on-prem platform |
| Apex ServiceNow Partner | C4 | 4 | 8 | Validation-key error | 4; applicable required ISO 27001 explicitly No |
| Stratagem Software | C4 | 4 | 8 | Validation-key error | 4; applicable required ISO 27001 explicitly No |
| Pinnacle Enterprise Tech | C4 | 4 | 8 | Validation-key error | 4; applicable required ISO 27001 explicitly No |
| AlphaCentric IT | C6 | 4 | 6 | Rubric ambiguity | Escalate: loosely relevant trigger aged 6-12 months is uncovered |
| Pinnacle Enterprise Tech | C6 | 4 | 6 | Rubric ambiguity | Escalate: same uncovered band |
| Veritas Cloud Partners | C6 | 4 | 6 | Rubric ambiguity | Escalate: same uncovered band |
| Vanguard Integrators | C7 | 6 | 8 | Model/execution error | 8; explicit 3-6 month timeline satisfies near-term band |
| Meridian IT Solutions | C8 | NS | 8 | Validation-key error | NS; structured competitive evidence missing |
| AlphaCentric IT | C8 | NS | 8 | Validation-key error | NS; structured competitive evidence missing |
| Vanguard Integrators | C8 | NS | 8 | Validation-key error | NS; structured competitive evidence missing |
| Veritas Cloud Partners | C8 | NS | 8 | Validation-key error | NS; structured competitive evidence missing |
| Meridian IT Solutions | C12 | 8 | 10 | Validation-key error | 8; all three favorable factors not established |
| AlphaCentric IT | C12 | 8 | 10 | Validation-key error | 8; all three favorable factors not established |
| Vanguard Integrators | C12 | 2 | 4 | Validation-key error | 2; no favorable factor affirmatively established |
| Veritas Cloud Partners | C12 | 2 | 4 | Validation-key error | 2; no favorable factor affirmatively established |
| Veritas Cloud Partners | C13 | <10 | 10 | Data/rubric ambiguity | Escalate: strong warmth does not clearly establish active VP+ relationship |

## Summary
- 18 validation-key errors
- 3 model/execution errors
- 4 unresolved rubric/data ambiguities
- Raw agreement remains 91.1%.
- Crediting confirmed key errors gives 273/280 = 97.5% adjudicated agreement.
- Excluding four genuinely ambiguous cases gives 273/276 = 98.9% adjudicated accuracy on determinable cases.

Do not silently resolve the four ambiguities. Any future rule change belongs in a separately tested iteration.