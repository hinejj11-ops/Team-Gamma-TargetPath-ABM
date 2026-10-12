# MVP v1.1 — Human Checkpoint Contract Smoke Test

**Date:** 2026-10-12. **Status:** Prompt-contract walkthrough, not a live consultant session or independent AI execution.

## Scenario HC01 — Unsupported data correction
CloudBridge contract status proposed `Not locked` with no dated source. Expected: log request but **do not apply**; keep locked and Tier 3 provisional; request evidence. Prompt 07 Part B explicitly requires source/date. **Documentary check: PASS.**

## Scenario HC02 — Supported correction (hypothetical)
If a consultant supplies dated, verifiable evidence that CloudBridge is `Not locked`, the workflow must change the working copy only, rescore C8 if affected, recalculate all dimensions and post-gate tier, preserve original Tier 3, and request fresh tier approval. No such evidence is present, so **no correction was applied**. **Workflow specification check: PASS; execution: PENDING.**

## Scenario HC03 — Rubric override
An override without rubric-band evidence must be challenged and flagged as `differs from rubric band` if explicitly confirmed; changing the rubric itself must be escalated. **Documentary check: PASS; execution: PENDING.**

## Scenario HC04 — Blind test / consultant absence
When no consultant has responded, the account remains **PROVISIONAL**. No AI-generated approval is permitted. **Documentary check: PASS; execution: PENDING.**

## Acceptance boundary
These four checks inspect the prompt and approval policy; they do not prove that a model will consistently follow them in a real multi-turn run. A genuine human-in-the-loop exercise with recorded inputs and before/after account scores remains required for full acceptance.
