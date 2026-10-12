# Incumbent Vendor Disruption Intelligence (v1.1)

## Purpose
Use public, source-verifiable incumbent vendor developments to support the FIOR C8 competitive-context assessment. This is not a substitute for private client data on whether a specific account is dissatisfied with its incumbent.

## Evidence contract
Maintain `data/Incumbent_Vendor_Events_Reference.csv` with Vendor, Event Type, Event Date, Severity, Source URL, Source Publisher, Verified On, Verification Status, Scope and Analyst Notes. The initial list is empty: **no verified public event has been established for the synthetic accounts**.

Acceptable event types include material price increase, acquisition, major layoffs, key executive departure, product end-of-life, cybersecurity incident, verified regulatory enforcement, and material litigation. Treat allegations as allegations; do not assume wrongdoing based on an investigation or lawsuit. Require an identifiable primary document or credible dated reporting, a working public URL, and analyst verification of vendor identity and event relevance.

## Scoring rule
1. Match the *structured* Incumbent / Competitor field to the named vendor. Ambiguous vendor matches are escalated, not scored.
2. Match only verified, applicable, recent events; no unverified or stale event may change C8. A verified event must demonstrably affect the incumbent product, geography, or service relevant to the account. No account-wide dissatisfaction may be inferred from vendor news.
3. Re-derive C8 using the frozen rubric. If the normal C8 evidence already supports the higher band, retain it. If a verified disruption creates a supported competitive opening, **propose** at most one adjacent-band uplift in the consultant-review packet with exact source, relevance, and baseline vs. proposed score. Do not automatically apply an uplift until a consultant approves the interpretation; never exceed C8=10.
4. Recompute totals and investment-tier eligibility only after consultant disposition. A vendor event does **not** override the independent competitive-contract lock gate; lock-band improvement requires account-specific verified dissatisfaction in the structured satisfaction field.
5. Preserve the event identifier/date/source, C8 before/after, reviewer and approval date; retain previous results and raise a review flag.

## Maintenance
Review quarterly and on significant verified events. Revalidate dated sources and expire unsupported entries. This is a **capability with an empty initial reference dataset**, not a functioning live-news monitoring service.
