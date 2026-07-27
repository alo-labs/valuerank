# AA search: Kimi K2.7 Code — Index eval cost

**Date:** 2026-07-28  
**Branch:** `main` (search-only; no ranking/site score changes)  
**Verdict:** **NOT FOUND** — AA Intelligence Index **total eval cost** is unpublished for Kimi K2.7 Code.

---

## Verdict summary

| Metric | Status | Value |
|--------|--------|-------|
| AA Index **total eval cost** (`intelligenceIndexCost.total` / “Cost to Run Artificial Analysis Intelligence Index”) | **NOT FOUND** for Kimi K2.7 Code | — |
| AA **cost per Intelligence Index task** (`costPerIntelligenceIndexTask`) | **NOT FOUND** for Kimi K2.7 Code (absent from chart series) | — |
| API **token pricing** (≠ eval cost) | **FOUND** | Input **$0.95**/MTok, Output **$4.00**/MTok, Cache hit **$0.19**/MTok |
| DeepSWE avg cost/task (ValueRank fallback) | Present in local evidence | **$2.82** |

**Recommendation:** **Keep DeepSWE-only** Cost for the v1.3 cohort. Do **not** restore composite AA+DeepSWE cost until AA publishes Index total eval cost for Kimi K2.7 Code (the sole gap among 18 cohort models).

---

## Canonical URLs

| What | URL | Result |
|------|-----|--------|
| **Canonical model page** | https://artificialanalysis.ai/models/kimi-k2-7-code | 200 — live page |
| Providers / API pricing | https://artificialanalysis.ai/models/kimi-k2-7-code/providers | 200 — token $/provider |
| Models index / search | https://artificialanalysis.ai/models?search=kimi | Lists Kimi family |
| Related: Kimi K3 (HAS eval cost) | https://artificialanalysis.ai/models/kimi-k3 | Eval cost published |
| Related: Kimi K2.6 (HAS eval cost; deprecated) | https://artificialanalysis.ai/models/kimi-k2-6 | Eval cost in Cost-to-Run chart |
| Intelligence methodology | https://artificialanalysis.ai/methodology/intelligence-benchmarking | Describes how Index cost is computed |
| **404 slugs tried** | `/models/kimi-k2.7`, `/models/kimi-k2-7`, `/models/kimi-k2.7-code`, `/models/kimi-k2p7-code`, `/models/kimi-k2-7-code-high`, `/models/moonshot-kimi-k2-7-code`, `/api/models/kimi-k2-7-code` | All 404 |

**AA slug / display name:** `kimi-k2-7-code` / “Kimi K2.7 Code” (Moonshot/Kimi, open weights, released June 2026).

---

## What “eval cost” means (vs token pricing)

ValueRank’s AA Cost input is **not** $/MTok list price. It is AA’s **Intelligence Index total evaluation cost**:

- UI label: **“Cost to Run Artificial Analysis Intelligence Index”**  
  (“Cost (USD) to run all evaluations in the Artificial Analysis Intelligence Index”)
- Payload field used by v1.3 extractor: `intelligenceIndexCost.total`  
  (see [`.refresh/v1.3/extract_aa_metrics.py`](extract_aa_metrics.py) → `extract_nested(..., "intelligenceIndexCost", "total")`)
- Chart breakdown components when published: `answerCost` + `reasoningCost` + `cacheWriteCost` + `cacheReadCost` + `nonCacheInputCost`

Token pricing on the same page is a **different** metric (hero “Price” tiles + FAQ).

---

## Evidence: NOT FOUND (Index total eval cost)

### 1. Parsed `currentModel` object (local full HTML scrape)

Source: [`.refresh/v1.3/aa/kimi-k2.7-code__kimi-k2-7-code.html`](aa/kimi-k2.7-code__kimi-k2-7-code.html)

Brace-balanced JSON parse of `currentModel` for slug `kimi-k2-7-code`:

- `intelligenceIndex` = **41.949…** (present)
- `price1mInputTokens` = **0.95**, `price1mOutputTokens` = **4**, `cacheHitPrice` = **0.19** (present)
- `intelligenceIndexCost` = **undefined / absent** (not null — **key missing**)
- `intelligenceIndexCostPerTask` = **absent**

Cost/price keys on the object are only token-price / blended-price fields — no Index total.

### 2. Live SPA (Playwright / CDP, 2026-07-28)

Page: https://artificialanalysis.ai/models/kimi-k2-7-code

- Hero Price tiles: **$0.95** input / **$4.00** output / **$0.19** cache hit.
- FAQ: *“Kimi K2.7 Code costs $0.95 per 1M input tokens and $4.00 per 1M output tokens…”* (token pricing only).
- Verbosity note: generated **100M** output tokens on Intelligence Index (token *volume*, not $ cost).
- Embedded **Cost to Run** series (`answerCost` labels): **20 models** — includes **Kimi K2.6** and **Kimi K3**, **does not include Kimi K2.7 Code**.
- Embedded **costPerIntelligenceIndexTask** series: **12 models** — includes **Kimi K3**, **not** Kimi K2.7 Code.
- No page text matching AA’s prose pattern `it cost $X to evaluate` for this model.

### 3. Cost-to-Run chart totals (same page payload; for contrast)

Sum of stacked components for Kimi models that *are* published:

| Model | Approx. Index total (sum of parts) | Matches ValueRank `evalCost`? |
|-------|--------------------------------------|-------------------------------|
| Kimi K2.6 | ~$840.64 | (not in v1.3 cohort) |
| Kimi K3 | **$2437.406835042445** | Yes — exact match to evidence |
| **Kimi K2.7 Code** | **absent from series** | — |

### 4. Local v1.3 pipeline state

| Artifact | Kimi K2.7 Code `evalCost` |
|----------|---------------------------|
| [`.refresh/v1.3/evidence.jsonl`](evidence.jsonl) | `null` (only null among 18) |
| [`.refresh/v1.3/aa_metrics.json`](aa_metrics.json) | `null` |
| [`.refresh/v1.3/scores.json`](scores.json) | `null`; `costMode: "deepswe-only"` |
| [`.refresh/v1.3/run_manifest.json`](run_manifest.json) | Note: DeepSWE-only due to unpublished AA Index total for Kimi K2.7 Code |
| [`raw-data.md`](../../raw-data.md) / [`methodology.md`](../../methodology.md) | Same claim documented |

Cohort check: **17/18** models have AA `evalCost`; **only** Kimi K2.7 Code is missing.

---

## Evidence: FOUND (token pricing only — do not use as ValueRank Cost)

From live page + FAQ + `currentModel`:

> “Kimi K2.7 Code costs $0.95 per 1M input tokens and $4.00 per 1M output tokens (based on Kimi's API). For a blended rate (7:2:1 cache hit/input/output ratio), this is $0.72 per 1M tokens.”

Also: Cache hit **$0.19**/MTok (−80%).

**These are API prices, not AA Index total eval cost.**

---

## False lead / extractor pitfall

A naive window search after `kimi-k2-7-code` can surface  
`intelligenceIndexCost.total = 1040.8780605451614`.

That value is **Gemini 3.5 Flash’s** published eval cost (same number in `evidence.jsonl`), appearing later in the RSC payload (comparison widgets). Brace-parsed `currentModel` for Kimi **does not** own that field. Do not treat $1040.88 as Kimi K2.7 Code’s Index cost.

---

## How to re-check / extract if AA publishes later

1. Open https://artificialanalysis.ai/models/kimi-k2-7-code  
2. In page HTML / RSC payload, parse `currentModel` (slug `kimi-k2-7-code`) and read **`intelligenceIndexCost.total`**.  
3. Confirm the model label appears in the **“Cost to Run Artificial Analysis Intelligence Index”** chart data (`answerCost` / stacked components).  
4. Re-run [`.refresh/v1.3/extract_aa_metrics.py`](extract_aa_metrics.py) — it already looks for `intelligenceIndexCost.total`.  
5. Only if **all 18** cohort models have non-null `evalCost`, consider restoring composite AA+DeepSWE Cost (product decision; out of scope for this search).

---

## Prior ValueRank claim — verification

Claim (v1.3): uses DeepSWE-only Cost because AA Index total eval cost is unpublished for Kimi K2.7 Code.

**Verified correct** against live AA + local scrapes + evidence (2026-07-28).

---

## Recommendation (explicit)

- **Keep DeepSWE-only** for Cost (zero-gap).  
- **Do not** invent / impute Index cost from token prices × 100M tokens (would not match AA’s cache-aware methodology).  
- **Do not** silently change rankings from this search task.  
- Revisit composite AA+DeepSWE Cost **only after** AA publishes `intelligenceIndexCost` for Kimi K2.7 Code (and cohort remains complete).
---

## Decision ({DATE} — ValueRank {VERSION})

**User decision:** Exclude **Kimi K2.7 Code** from the ranked cohort rather than keep DeepSWE-only Cost for all models. Cost construction restored to AA+DeepSWE composite for **n=17**. This search verdict (NOT FOUND) remains the evidence for the exclusion.
