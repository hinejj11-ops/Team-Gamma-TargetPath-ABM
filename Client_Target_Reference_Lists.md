# TargetOrate Evaluation Criteria & Parameters

## Purpose and Authority

This file contains **TargetOrate-level reference parameters** used by the FIOR workflow. Client-specific targeting criteria belong in the completed ICP.

### Source-of-truth rule

- **FIOR Rubric** controls scoring anchors and missing-data behavior.
- **Client ICP** controls client-specific industry, company-size, geography, compliance, technographic, stakeholder, and disqualification definitions.
- **This reference list** supplies TargetOrate product/expansion definitions, strategic-value benchmarks, historical win-rate assumptions, and reusable baseline examples.
- If this file conflicts with a completed client ICP on a client-specific targeting field, the **client ICP governs** and the conflict is flagged for review.

The technology and geography/compliance values below are retained as the baseline used to build the synthetic capstone ICP. In production, the completed client ICP is the operative benchmark for C3 and C4.

---

## 1. Technology Stack Baseline (Criterion 3)

### Required Technology Categories

- **CRM / Sales Engagement:** Salesforce CRM, HubSpot Enterprise, or Apollo.io
- **Cloud Infrastructure:** AWS, Microsoft Azure, or Google Cloud Platform (GCP)
- **Data / Analytics:** Snowflake, Databricks, or Segment

### Preferred Technologies

- **Intent / ABM Data Providers:** 6sense, Demandbase, ZoomInfo Enterprise
- **Marketing Automation:** Marketo, Pardot (Marketing Cloud Account Engagement)

### Incompatible / Competing Stacks

Proprietary legacy on-premise databases without cloud connectors, or direct competing ABM point solutions locked under enterprise exclusivity contracts.

**Operational note:** Apply the completed client ICP when scoring C3. If account technology evidence is too thin to test the required categories, return `NS` as directed by the rubric rather than assuming incompatibility.

---

## 2. Geography & Compliance Baseline (Criterion 4)

### Baseline Served Geographies

- North America (US, Canada)
- Western Europe (UK, Germany, France, Nordics)
- Major APAC hubs (including Australia; the synthetic example ICP also includes New Zealand)

### Baseline Compliance & Security Frameworks

- SOC 2 Type II
- ISO 27001
- GDPR for European operations
- HIPAA for HealthTech SaaS accounts

**Operational note:** Apply the completed client ICP when scoring C4. Missing compliance evidence is not evidence of noncompliance; use `NS` when the rubric requires it.

---

## 3. Client Product Lines & Expansion Mapping (Criterion 10)

TargetOrate's enterprise product catalog for expansion assessment:

- **TargetOrate Core ABM Platform:** Account targeting and orchestration engine.
- **Intent Data & Surge Intelligence Module:** Third-party buyer intent integration.
- **Pipeline Analytics & Multi-Touch Attribution Suite:** Revenue attribution and closed-won analytics.

### Expansion Scoring Guide

- **Band 10:** Active use cases for all three products across multiple departments such as sales, marketing, and revenue operations.
- **Band 8:** Two products across more than one department/unit; commonly Core ABM + Intent Data across marketing and sales.
- **Band 6:** One additional product or department is plausibly supported by account evidence.
- Apply the remaining rubric bands exactly as written in the FIOR rubric.

---

## 4. Strategic Value Benchmarks (Criterion 11)

Evaluate the rubric's strategic-account tests using evidence in the permitted inputs:

- **Market Leader Test:** Top quartile proxy = revenue $100M+ or employee count 500+ in the account's segment.
- **Referenceable Test:** Evidence that the company publishes case studies, appears on approved customer/reference lists, or can credibly act as a peer reference.
- **Partnership Potential Test:** Evidence that the company appears in TargetOrate's approved strategic partner ecosystem.

Do not award a test when the required evidence is unavailable.

---

## 5. Win Probability & Historical Benchmarks (Criterion 12)

- **Historical Win Rate Baseline:** TargetOrate's average win rate on similar mid-market/enterprise SaaS deals is ≥50% when budget is confirmed.
- **Favorable Competitive Position:** Incumbent is absent, disliked, or tied to an expiring contract within 6 months.
- **Budget Confirmed:** Supported by procurement notes, RFP issuance, or active executive sponsorship.

Score C12 using the exact FIOR rubric anchors. Do not infer budget confirmation, competitive favorability, or historical comparability without supporting evidence.
