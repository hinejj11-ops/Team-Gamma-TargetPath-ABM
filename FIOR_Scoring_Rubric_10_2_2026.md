# FIOR Account Scoring Rubric

Version: draft for workflow build. Score anchors other than Annual Contract Value and the tier cutoffs are Team Gamma proposals and may change after TargetOrate confirms them. The weights (35, 25, 30, 10) are fixed.

Iteration 7 draft addition: the Competitive Lock Gate (see "Competitive Lock Gate" below) and the C8 definition of "locked". The 12 and 24 month windows come from TargetOrate; the band boundaries, the handling of unknown status, and the other items in `workflow/Competitive_Lock_Gate_Open_Items.md` are Team Gamma assumptions pending TargetOrate confirmation.

## Purpose

Score one account on the 14 FIOR criteria using only the evidence in the account record. Each criterion has anchored score levels so repeated runs on the same record produce the same score.

## Required inputs

- The account record from the TargetOrate company database
- The filled ICP Template: target industries, size range, technology (required and preferred), geography, compliance requirements
- The client's product list and average deal size
- The client's trigger relevance list, partner target list, and executive title list
- The Scoring As Of Date for the run (required for the Competitive Lock Gate; state it for every run and do not substitute the current date)

## Global scoring rules

1. Score each criterion as a whole number from 1 to 10. Use the anchor scores shown (10, 8, 6, 4, 2). Use the odd score between two anchors (9, 7, 5, 3) only when the account fully meets the lower anchor and partly meets the higher one, and state which conditions were met.
2. Work from the top band down and take the first band whose condition is fully met. A combination not listed takes the lower adjacent score.
3. Score only from the account record and the inputs above. Do not use outside knowledge to fill a gap.
4. Cite the field name and value behind every score.
5. Missing data: if the field a criterion needs is blank or marked unknown, return NS (not scored). A blank is not a zero. Score 2 only when the record shows the signal is absent. Whether an NS sends the account to a consultant is decided only by the Review rule ("When an account goes to a consultant") below.
6. Stale data (proposed thresholds): intent signals older than 90 days count as absent. Company data older than 12 months, and contact or role data older than 6 months, are scored but flagged.
7. Confidence: High when the record states the fact directly, Medium when it is inferred, Low when the evidence is thin. Low confidence triggers review.
8. For each criterion return: criterion number, score (or NS), band, evidence cited (field and value), confidence, review flag (yes or no) and reason.

---

## FIT (35% weight)

### 1. Industry / Segment Match

Evidence: industry and sub-industry fields, company description, and ICP target industry/sub-industry definitions.

Evaluate the account against each ICP profile independently. An industry match from one ICP profile and a sub-industry match from a different ICP profile may not be combined to create a stronger match. Use the single ICP profile that produces the strongest fully supported fit.

| Score | Condition |
| --- | --- |
| 10 | Industry and sub-industry both match the same primary ICP profile |
| 8 | Industry matches a primary ICP profile and the sub-industry is adjacent, unspecified, or otherwise compatible with that same profile |
| 6 | Industry or sub-industry matches a secondary/adjacent category explicitly recognized by the ICP, but the account does not fully satisfy a primary profile |
| 4 | Industry/sub-industry is not listed in the ICP, but the account demonstrably serves the ICP's target buyers or use case |
| 2 | Account is explicitly outside/excluded by the ICP, or has no supported logical link to an ICP profile |

Rules:

1. **Same-profile rule:** Industry and sub-industry must match the same ICP profile to receive a score of 10. Do not combine an industry from one ICP profile with a sub-industry from another profile.
2. **Explicit-exclusion rule:** If the ICP explicitly identifies the account's industry, sub-industry, use case, or business category as outside the ICP, score C1 = 2. An otherwise matching parent industry does not override an explicit exclusion.
3. **Specific-over-general rule:** When a specific sub-industry/use-case classification conflicts with a broader industry classification, the more specific classification governs when the ICP explicitly addresses it.
4. Do not infer an industry or sub-industry from unrelated fields solely to improve the score.
5. If the industry/sub-industry evidence itself is missing or genuinely contradictory, return NS for C1 and apply the Review rule (Industry and Sub-Industry are fatal fields, so the account is held) rather than assuming a fit.

Flag trigger: if account evidence contains materially conflicting industry classifications that cannot be resolved using the ICP hierarchy above, score using the best fully supported classification and route the account to consultant review.

### 2. Company Size

Evidence: annual revenue, employee count, ICP size range.

| Score | Condition |
| --- | --- |
| 10 | Revenue and employees both inside the ICP range |
| 8 | One inside the range, the other within 25% of the range edge |
| 6 | Both within 25% of the range edge |
| 4 | One outside the range by more than 25% |
| 2 | Both outside the range by more than 25% |

Flag trigger: revenue is an estimate, or revenue per employee is far outside the norm for the sector.

### 3. Technology Stack

Evidence: detected technologies, ICP required and preferred technology lists. "Current" means current versions and cloud based.

| Score | Condition |
| --- | --- |
| 10 | All required technologies present and the stack is current |
| 8 | All required present; some preferred missing |
| 6 | At least three quarters of required technologies present |
| 4 | Fewer than three quarters of required present |
| 2 | None present, or a directly competing or incompatible platform |

Rules:
- **Missing-versus-absent rule:** A blank, unknown, or otherwise unverified required technology field is missing evidence and returns C3 = NS when the record is too incomplete to determine required-stack coverage. Do not convert a blank field into evidence that the technology is absent.
- **Affirmative-absence rule:** A low numeric band is permitted only when the structured technology record affirmatively establishes that required technology is not present, or identifies a directly competing/incompatible platform. Examples include an explicit `None`, `Not present`, verified absence, or a named incompatible platform in the applicable structured field.
- **Coverage denominator rule:** Calculate the fraction of required technologies present only when each required technology category has an affirmative present/absent determination. If one or more required categories are blank/unknown and their status could change the applicable scoring band, return NS instead of estimating a percentage from the populated fields.
- Preferred technology fields may affect the 10-versus-8 distinction only after all required technologies are affirmatively confirmed present. A blank preferred field does not by itself make required-stack evidence incomplete.
- A populated Technology Evidence Date establishes recency; it does not prove that blank technology categories were checked and found absent.
- Structured V2 technology fields are authoritative. Legacy narrative technology-stack fields may provide audit context but may not fill blank required structured categories.

### 4. Geography / Compliance Ready

Evidence: headquarters and operating regions, certifications held, ICP geography and compliance requirements.

| Score | Condition |
| --- | --- |
| 10 | In a target geography and all required compliance items met |
| 8 | In a target geography with one non critical compliance gap |
| 6 | In an adjacent geography that can be served, compliance met |
| 4 | A required compliance item is missing, in a target or adjacent geography |
| 2 | Outside the served geography, or a regulatory blocker |

Rules:
- **Unknown-versus-failed rule:** A blank, `Unknown`, or otherwise unverified applicable compliance field is missing evidence, not evidence that the requirement failed. If unresolved compliance evidence could change the applicable scoring band, return C4 = NS.
- **Affirmative-gap rule:** Score the required-compliance-missing band only when the structured record affirmatively states that an applicable required framework is not met (for example `No`, `Not certified`, `Not ready`, or equivalent verified negative evidence).
- **Applicability rule:** Evaluate only compliance frameworks required by the governing ICP profile and geography/use case. A blank or negative value for a framework that is not applicable must not reduce C4.
- **Noncritical-gap rule:** The 8 band requires affirmative evidence that all required compliance is met plus one explicitly identified noncritical compliance gap. Do not use `Unknown` as a noncritical gap.
- **Regulatory-blocker rule:** Score 2 only when the record affirmatively establishes a regulatory blocker or an outside/unserved geography; do not infer a blocker from missing compliance data.
- A populated Compliance Evidence Date establishes recency but does not prove that blank or `Unknown` compliance fields were checked and failed.
- Structured V2 compliance fields are authoritative; legacy narrative fields may provide context but may not replace missing required structured compliance evidence.

---

## INTENT (25% weight)

### 5. Intent Signals & Research Behavior

Evidence: third party surge topics, website visits, content downloads, keyword activity, each with a date. A signal type is one of those four categories.

| Score | Condition |
| --- | --- |
| 10 | Three or more signal types in the last 30 days |
| 8 | Two signal types in the last 30 days, or three or more in the last 90 days |
| 6 | One signal type in the last 30 days, or two in the last 90 days |
| 4 | One signal type in the last 90 days, or only generic activity (for example a homepage visit) |
| 2 | The record shows no signals in 90 days |

Rules:
- A blank intent field is NS, not 2.
- An explicit negative value such as `Verified no website signal`, `Verified no content signal`, `Verified no third-party signal`, or `Verified no sales signal` is affirmative evidence of absence, not an intent signal.
- Do not count the date attached to an explicit negative value as a signal event. The date establishes when the absence was verified.
- If every populated structured intent category within the 90-day window affirmatively states that no signal was present and there are no positive structured signals, score C5 = 2.
- Positive and explicit-negative records may coexist. Count only positive signal types when applying the 30/90-day scoring bands.

### 6. Buying Triggers & Trigger Events

Evidence: funding, leadership change, technology migration, contract renewal, product launch, compliance requirement, each with a date. A trigger is relevant if it appears on the client's trigger relevance list.

| Score | Condition |
| --- | --- |
| 10 | Two or more distinct trigger types in the last 6 months, at least one relevant |
| 8 | One relevant trigger in the last 6 months |
| 6 | One loosely relevant trigger in the last 6 months, or a relevant trigger 6 to 12 months old |
| 4 | Only a trigger older than 12 months, or an irrelevant one |
| 2 | No triggers found |

Rules:
- An explicit negative value such as `Verified no trigger`, `No trigger identified`, or an equivalent structured statement is affirmative evidence that no buying trigger was found and scores C6 = 2 when no positive structured trigger is present.
- Do not treat the date attached to an explicit negative trigger record as evidence that a trigger occurred. The date establishes when the absence was verified.
- Score 10 needs two distinct trigger types. Trigger Type and Trigger Date may each hold up to two entries separated by a semicolon, matched in order. With a single entry, 8 is the highest score available.
- A blank Trigger Type is missing evidence and follows the global NS rule; it is not equivalent to `Verified no trigger`.
- When structured Trigger Type / Trigger Date evidence is present, legacy narrative trigger fields may not override it.

Flag trigger: the trigger is a leadership change (the named leader may have moved on again).

### 7. Decision Timeline & Buying Readiness

Evidence: stated or documented buying timeline, such as an RFP, evaluation notes or CRM stage.

| Score | Condition |
| --- | --- |
| 10 | Active buying cycle, with an evaluation or RFP underway |
| 8 | Near term decision expected within 6 months |
| 6 | Decision expected in 6 to 12 months |
| 4 | Long term, beyond 12 months |
| 2 | Timeline unclear, with no evidence either way beyond that |

Rule: if the timeline is inferred from other signals (criteria 5 and 6) instead of stated, cap the score at 6 and flag for review.

### 8. Competitive Context & Urgency

Evidence: incumbent vendor, satisfaction notes, contract end date.

| Score | Condition |
| --- | --- |
| 10 | Dissatisfied with a competitor |
| 8 | No competitor in place |
| 6 | Competitor contract renews within 6 months |
| 4 | Competitor contract renews in more than 6 months, or the date is unknown |
| 2 | Contract locked with a competitor |

Definitions (Iteration 7 clarification; preserves every C8 score in the Iteration 6 key):
- "Contract locked with a competitor" (score 2) means Incumbent Contract Status is `Locked` and the Contract Renewal Date is 12 or more months after the Scoring As Of Date, or no renewal date is stated.
- A `Locked` contract renewing in more than 6 and fewer than 12 months scores 4, as "renews in more than 6 months".
- A date that is unknown with a status other than `Locked` scores 4. A blank incumbent with no other evidence follows the global NS rule.
- C8 scores the criterion only. The tier effect of a lock is applied by the Competitive Lock Gate below.

---

## OPPORTUNITY (30% weight)

### 9. Annual Contract Value

Evidence: estimated first year contract value, built from the client's average deal size and the account's size. Bands supplied by TargetOrate.

| Score | Condition |
| --- | --- |
| 10 | Above $500K |
| 8 | $250K to $500K (inclusive of $500K) |
| 6 | $100K to under $250K |
| 4 | Under $100K |

Rule: edge values ($500K, $250K, $100K) go to the lower band shown above.

### 10. Expansion Potential

Evidence: the client's product list, the account's business units, subsidiaries or departments, any note of other needs. Cite the reason for each product counted.

| Score | Condition |
| --- | --- |
| 10 | Three or more client products apply, and the account has multiple units that could adopt them |
| 8 | Two products apply across more than one department or unit |
| 6 | One additional product or department is plausible |
| 4 | Limited expansion path beyond the first use case |
| 2 | Single use case with no visible expansion path |

### 11. Strategic Value

Evidence: market position, public customer references, partner ecosystem. Three tests:

- Market leader: top quartile by revenue in its segment
- Referenceable: publishes case studies or is a named customer of peers
- Partnership potential: appears in the client's partner target list

| Score | Condition |
| --- | --- |
| 10 | All three tests met |
| 8 | Two tests met |
| 6 | One test met clearly |
| 4 | One test met weakly |
| 2 | No tests met |

### 12. Win Probability

Evidence: win rate on similar closed deals, competitive position, budget status. A factor is favorable when similar deal win rate is 50% or higher, when the competitive position is neutral or better, or when budget is confirmed (one test per factor).

| Score | Condition |
| --- | --- |
| 10 | All three factors favorable |
| 8 | Two favorable, and budget confirmed is one of them |
| 6 | Two favorable without budget confirmed, or budget confirmed alone with the others neutral |
| 4 | One favorable factor |
| 2 | No favorable factor, or a known unfavorable one |

---

## RELATIONSHIP (10% weight)

### 13. Existing Connections

Evidence: named contacts with title, last contact date and role verification date. Executive means a title on the client's executive title list (for example VP and above).

| Score | Condition |
| --- | --- |
| 10 | Active relationship with a VP level or higher contact, contact within 12 months |
| 8 | Active relationship with a director or manager, or a named mutual connection who can make a warm intro to an executive |
| 6 | Mutual connections exist but no direct relationship |
| 4 | Weak links only, such as the same network or a past event meeting |
| 2 | The record shows no connections |

Rules:
- **Relationship-strength precedence:** `Existing Connections & History` determines whether a relationship is active, warm/mutual, weak, or absent. `Named Key Contacts` establishes who is known and their title; a senior title alone does not prove an active relationship.
- A named VP, C-suite executive, director, or manager may satisfy the title component of a scoring band only when the relationship evidence independently supports that band.
- Marketing-only engagement such as webinar registration or nurture-email activity is a weak connection for C13 and does not become an active executive relationship merely because a senior contact is named.
- A cold account or explicit statement of zero prior touchpoints scores C13 = 2 even when named contacts are present.
- A warm introduction or named mutual connection may support the 8 or 6 band as specified above, depending on whether an executive introduction is actually available.
- Past-event or conference contact without evidence of an ongoing active relationship remains in the weak-link band.
- If the contact's role was not verified in the last 6 months, cap the score at 6 and flag for review.
- A blank `Existing Connections & History` field is NS. Do not infer relationship strength from `Named Key Contacts` alone.

### 14. Engagement History

Evidence: customer status, champion field, meeting, demo and event history, churn reason if any.

| Score | Condition |
| --- | --- |
| 10 | Current customer in good standing, or an identified and active champion |
| 8 | Former customer who left on good terms, or a champion identified but no purchase |
| 6 | Past direct engagement such as a meeting, demo or event, with no champion |
| 4 | Marketing engagement only, such as email opens or a webinar |
| 3 | Former customer who churned unhappy (flag for review) |
| 2 | No prior engagement |

Rules:
- **Customer-status precedence:** Explicit customer status is evaluated first. A current customer in good standing scores 10. A former customer in good standing scores at least 8. An unhappy churn scores 3 and triggers review; a champion label does not override an explicit unhappy-churn status.
- **Active-champion rule:** A champion status that explicitly describes current internal advocacy or active support qualifies as an identified and active champion and scores 10. Examples include `Strong Champion: Former user advocating internally` and `Identified: VP Mktg actively pushing for evaluation`.
- **Identified-but-not-active rule:** A champion is scored 8 only when the record identifies a champion but does not establish current advocacy/action or explicitly indicates no purchase/activation.
- **Emerging/moderate support:** Labels such as `Emerging Champion` or `Moderate Champion` are not automatically active champions. Use the description: if it shows current advocacy/action, score 10; if it shows support or pain without active advocacy, score 8.
- **No-champion rule:** `None identified`, gatekeeper-only evidence, or equivalent negative champion evidence does not create engagement. Use documented direct/marketing engagement to select 6, 4, or 2.
- Do not infer an active champion solely from a senior title in `Named Key Contacts`.
- When champion evidence and engagement-history evidence conflict, use the more specific structured customer/champion evidence and flag material contradictions for review.

---

## Total score, tier and dimension status

Average the scored criteria in each dimension, then multiply by the dimension multiplier.

| Dimension | Criteria | Multiplier | Maximum |
| --- | --- | --- | --- |
| FIT | 1 to 4 | 3.5 | 35 |
| INTENT | 5 to 8 | 2.5 | 25 |
| OPPORTUNITY | 9 to 12 | 3.0 | 30 |
| RELATIONSHIP | 13 to 14 | 1.0 | 10 |

Total = FIT + INTENT + OPPORTUNITY + RELATIONSHIP, out of 100. Round the total to the nearest whole number before assigning a tier. A total that ends exactly in .5 rounds up (74.5 becomes 75). Compute from unrounded dimension scores. (Iteration 7 tie rule; the Iteration 6 keys rounded some ties down, see the README.)

| Total | Recommended tier | Approach |
| --- | --- | --- |
| 80 to 100 | Tier 1 | 1:1 ABM |
| 60 to 79 | Tier 2 | 1:Few ABM |
| 40 to 59 | Tier 3 | 1:Many ABM |
| Under 40 | Nurture / Disqualify | Inbound only |

Dimension status (proposed): Strong at 70% or more of the dimension maximum, Moderate at 40% to 69%, Weak below 40%.

Missing data in totals: average only the criteria that were scored within each dimension. This gives a provisional total. Whether that total can be released is decided by the Review rule below.

Tier is a recommendation. An account with no review trigger (Review Status `Acceptable`) does not need an individual review. The consultant still approves its tier as part of signing off the portfolio, after the sampled check in the Quality Control Checklist. An account with any review trigger needs consultant approval before release and is labeled provisional until then.

## When an account goes to a consultant (single review rule, Iteration 7 proposed)

This one rule replaces three earlier rules that disagreed: the global missing data rule, the "more than one NS per dimension" tolerance, and the rank based routing in `MASTER_PROMPT.md`. Nothing else decides whether a missing value causes review.

**Rule for missing data (NS).**
1. Cannot score at all (fatal). If Company Name, Industry or Sub-Industry (C1), or Target ACV (C9) is missing, the account is held and a data request goes to the consultant. These are the Criteria Ranking Model ranks 1 to 3. Without them the tier cannot be defended and no bound can be computed.
2. Any other NS: compute the total twice, once with every NS criterion set to 2 (low bound) and once set to 10 (high bound), using the same dimension formula and rounding. If both totals give the same tier, the missing data cannot change the recommendation. The account is not reviewed for the NS; the output carries an audit note listing the missing fields. If the two totals give different tiers, the account goes to the consultant, with the specific fields that would settle it listed.
3. Evidence rank only orders the queue (see the ceiling paragraph below). It never decides, by itself, whether an account is reviewed.

**Why this rule.** A consultant's time is worth spending only where the missing value could change what the client does. A tier that stays the same at the worst case and the best case needs no human to fill the gap. A tier that changes needs one. This ties review to the decision rather than to the number of blanks.

**Other triggers (unchanged).** Low confidence, conflicting industry classification, unverified role older than 6 months or a leadership change trigger, an inferred timeline or ACV or competitor status, a total within 2 points of a tier cutoff, scoring 2 on both Industry and Company Size, an unhappy churn, and the Competitive Lock Gate outcomes listed below.

**The test behind every trigger.** A step goes to a human only when at least one of these is true: (a) the value is a judgment the rubric cannot settle (conflicting industry classification, a strategic outlier, rubric ambiguity); (b) the evidence cannot be checked from the record (an inferred timeline, ACV or competitor status, a role not verified in 6 months, low confidence); (c) the recommendation could flip on a small change (a total within 2 points of a cutoff, or a missing value whose bounds straddle a tier); or (d) the cost of being wrong is high and hard to reverse (a Tier 1 spend, an unhappy former customer, a contract that may have renewed). Anything that fails all four tests is handled by the workflow and logged, not reviewed. This is the reasoning TargetOrate asked for; the individual triggers follow from it, and a new trigger should be added only if it passes one of the four tests.

**Review volume ceiling (proposed).** Plan for no more than 25 percent of accounts in a run going to a consultant (for example 25 of 100). Reasoning: at roughly 15 minutes per account, 25 reviews is about 6 hours, which one consultant can complete in a working day, so a run can be turned around within a day; above that, review becomes the bottleneck and approvals become rushed. The figure is a Team Gamma proposal and needs TargetOrate's real consultant capacity.

- If more than 25 percent trigger, review in this order: fatal data holds first, then accounts whose bounds straddle Tier 1, then accounts near a cutoff, then the rest. Accounts not reached are released as provisional, never as approved.
- Report the review rate for every run. A rate above the ceiling is a finding about the data or the rules and should be reported, not hidden.

**Sampled check (proposed).** A consultant spot checks 10 percent of `Acceptable` accounts, at least 3, chosen by the consultant, before release. Any error found in the sample means the whole `Acceptable` group is reviewed. The 10 percent figure is a Team Gamma proposal for TargetOrate to confirm.

## Competitive Lock Gate (proposed, Iteration 7)

**Why it exists.** C8 scores a locked competitor contract as one criterion, so a lock can lower a total but cannot stop a strong account from reaching Tier 1. The ICP lists a locked competitor with no actionable exit window as a hard disqualifier, but nothing connected that rule to FIOR. The gate connects them. It changes the recommended tier only. It never changes a criterion score or the total.

**Inputs.** Score implied tier (from the rounded total and the tier table), Incumbent Contract Status, Contract Renewal Date, Incumbent Satisfaction, and the Scoring As Of Date. Window lengths default to 12 and 24 months and may be set in the client ICP.

**Applies when** Incumbent Contract Status is `Locked`.
- `Not locked` or `No incumbent`: gate not applied.
- `Unknown` or blank: gate not evaluated. Record "contract status unknown". An unknown status is neither a lock nor a clearance, and it never costs the account points.

**Step 1: band from the renewal date.** Add 12 and 24 calendar months to the Scoring As Of Date. If the target day does not exist in that month, use the last day of the month.

| Band | Condition | Meaning |
| --- | --- | --- |
| 1 Open window | Renewal date is earlier than As Of Date plus 12 months (under 12 months) | Score normally, eligible for Tier 1 |
| 2 Capped | Renewal date is from As Of Date plus 12 months through As Of Date plus 24 months, both inclusive | Cap at Tier 3 |
| 3 Locked out | Renewal date is later than As Of Date plus 24 months, or no renewal date is stated | Disqualify |

**Step 2: satisfaction move.** Use only the structured Incumbent Satisfaction field. The legacy narrative Competitive Context field may not substitute.
- `Dissatisfied`: move one band toward Band 1 (3 to 2, 2 to 1; Band 1 stays).
- `Satisfied`: move one band toward Band 3 (1 to 2, 2 to 3; Band 3 stays).
- `Neutral`, `Unknown`, or blank: no move. An unknown never costs the account points.

**Step 3: tier effect of the final band.**

| Final band | Effect on the recommended tier |
| --- | --- |
| 1 | None. Any tier the score supports, including Tier 1. |
| 2 | Tier 1 or Tier 2 becomes Tier 3. Tier 3 and Nurture / Disqualify are unchanged. A cap never raises a tier. |
| 3 | `Disqualified (Competitive Lock)`, whatever the score. |

**Rules.**
1. Always report both the Score Implied Tier and the Recommended Tier after the gate, the band before and after the satisfaction move, and the fields and values used.
2. A renewal date on or before the As Of Date is Band 1, and the account goes to consultant review to confirm whether the contract renewed.
3. The gate uses the Scoring As Of Date, never the run clock. The same record and the same date always give the same result. When the date changes, rerun the gate; a capped account moves into the open window by itself when its renewal falls under 12 months away.
4. The gate result is a recommendation. A consultant may approve a documented strategic exception. The AI never lifts a cap or reverses a disqualification itself.
5. Vendor level events at the incumbent (price increases, acquisitions, compliance events and similar) are not part of this gate. They are a possible later addition to C8 and are listed in `workflow/Competitive_Lock_Gate_Open_Items.md`.

## Per account review triggers

Route a single account to a consultant when any of these is true:

- Missing data whose low and high bounds give different tiers, or a fatal missing field (see the Review rule above)
- Any criterion is scored with Low confidence
- Data provider category and company description disagree on industry
- A contact's role is not verified in the last 6 months, or the trigger is a leadership change
- A timeline, ACV or competitor status was inferred rather than stated
- The total falls within 2 points of a tier cutoff (for example 58 to 61)
- The account scores 2 on both Industry and Company Size
- A former customer churned unhappy (criterion 14)
- The Competitive Lock Gate disqualifies the account, or the contract renewal date is on or before the Scoring As Of Date
