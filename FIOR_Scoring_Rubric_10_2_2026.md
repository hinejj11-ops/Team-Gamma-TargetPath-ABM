# FIOR Account Scoring Rubric

Version: draft for workflow build. Score anchors other than Annual Contract Value and the tier cutoffs are Team Gamma proposals and may change after TargetOrate confirms them. The weights (35, 25, 30, 10) are fixed.

## Purpose

Score one account on the 14 FIOR criteria using only the evidence in the account record. Each criterion has anchored score levels so repeated runs on the same record produce the same score.

## Required inputs

- The account record from the TargetOrate company database
- The filled ICP Template: target industries, size range, technology (required and preferred), geography, compliance requirements
- The client's product list and average deal size
- The client's trigger relevance list, partner target list, and executive title list

## Global scoring rules

1. Score each criterion as a whole number from 1 to 10. Use the anchor scores shown (10, 8, 6, 4, 2). Use the odd score between two anchors (9, 7, 5, 3) only when the account fully meets the lower anchor and partly meets the higher one, and state which conditions were met.
2. Work from the top band down and take the first band whose condition is fully met. A combination not listed takes the lower adjacent score.
3. Score only from the account record and the inputs above. Do not use outside knowledge to fill a gap.
4. Cite the field name and value behind every score.
5. Missing data: if the field a criterion needs is blank or marked unknown, return NS (not scored) and flag for review. A blank is not a zero. Score 2 only when the record shows the signal is absent. This rule is interim until TargetOrate supplies its tiered list of criterion importance and a fallback for missing information.
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
5. If the industry/sub-industry evidence itself is missing or genuinely contradictory, apply the global NS/review rules rather than assuming a fit.

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

Rule: if compliance data is absent from the record, return NS.

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

Total = FIT + INTENT + OPPORTUNITY + RELATIONSHIP, out of 100. Round the total to the nearest whole number before assigning a tier.

| Total | Recommended tier | Approach |
| --- | --- | --- |
| 80 to 100 | Tier 1 | 1:1 ABM |
| 60 to 79 | Tier 2 | 1:Few ABM |
| 40 to 59 | Tier 3 | 1:Many ABM |
| Under 40 | Nurture / Disqualify | Inbound only |

Dimension status (proposed): Strong at 70% or more of the dimension maximum, Moderate at 40% to 69%, Weak below 40%.

Missing data in totals (proposed): average only the criteria that were scored. If more than one criterion in a dimension is NS, or any criterion in RELATIONSHIP is NS, mark the dimension incomplete and route the account to review before a total is accepted.

Tier is a recommendation only. The AI outputs a recommended tier and the consultant approves it.

## Per account review triggers

Route a single account to a consultant when any of these is true:

- Any criterion returns NS beyond the tolerance above
- Any criterion is scored with Low confidence
- Data provider category and company description disagree on industry
- A contact's role is not verified in the last 6 months, or the trigger is a leadership change
- A timeline, ACV or competitor status was inferred rather than stated
- The total falls within 2 points of a tier cutoff (for example 58 to 61)
- The account scores 2 on both Industry and Company Size
- A former customer churned unhappy (criterion 14)
