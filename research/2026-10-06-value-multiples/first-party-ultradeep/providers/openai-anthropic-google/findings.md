# First-party provider rules and API pricing: OpenAI, Anthropic, Google

**Coverage date:** October 6, 2026  
**Work stage:** Retrieve/Triangulate contribution; incomplete because the required Codex in-app browser was unavailable in this subagent.  
**Models assigned:** GPT-6 Sol, GPT-5.6 Sol, GPT-6 Astra, GPT-5.6 Luna, GPT-6 Luna; Claude Opus 5.5, Claude Opus 5; Gemini 3.8 Flash.  
**Evidence boundary:** This note carries forward only first-party source observations already recorded in ValueRank packages checked October 5. It does not represent a fresh October 6 visit to those pages. No provider pricing page or API rate card was freshly retrieved here.

## Browser access and retrieval status

The requested Codex in-app browser was not available in this subagent. `cua.createBrowserTab("iab", ...)` returned `Browser is not available: iab`; Codex app UI access through CUA was denied by the safety layer. A Codex app `open_in_codex` request for one Google search URL returned `queued` and exposed no rendered page or results. I did not use Edge, another external browser, or `web__run`.

As a result:

- **Fresh source pages opened in this contribution:** 0.
- **Successful browser searches:** 0.
- **Search attempts logged:** 1 attempted OpenAI query; it was not executed and returned no results.
- **Inherited first-party source records inspected:** 7 links across the assigned providers.
- **First-party API rate cards captured for these exact models:** 0.
- **Current plan price/tier matrices captured for these exact models:** 0.

The direct links below are inherited from existing project package records. Their prior retrieval dates are preserved where the package recorded them; the current task did not independently refresh them.

## Model-by-model status

| ValueRank model | Inherited first-party plan rule | Eligible plan tiers and current prices | Exact-model allowance match | First-party API rates | API-equivalent calculation |
|---|---|---|---|---|---|
| GPT-6 Sol | OpenAI help says Codex limits vary by plan and points account holders to their usage dashboard or CLI `/status`. | Not captured. The inherited help record has no current tier/price matrix or model-specific quota. | No numeric quota or tier assignment for GPT-6 Sol in the captured provider record. | Not captured. No exact model rate, cache rate, long-context bracket, or temporary price was recorded. | Not determinable: no absolute provider allowance, exact-model rate schedule, or measured token mix. |
| GPT-5.6 Sol | Same OpenAI account-specific policy; the separate ChatGPT model-limit link is not evidence of a Codex GPT-5.6 Sol allowance. | Not captured. | No numeric Codex allowance for this exact model. | Not captured. | Not determinable for the same missing inputs; ChatGPT model caps cannot be transferred to Codex. |
| GPT-6 Astra | Same OpenAI account-specific policy. | Not captured. | No numeric Codex allowance for this exact model. | Not captured. | Not determinable. The inherited record does not give model-specific quota units or a rate schedule. |
| GPT-5.6 Luna | Same OpenAI account-specific policy. | Not captured. | No numeric Codex allowance for this exact model. | Not captured. | Not determinable. |
| GPT-6 Luna | Same OpenAI account-specific policy. | Not captured. | No numeric Codex allowance for this exact model. | Not captured. | Not determinable. |
| Claude Opus 5.5 | Anthropic’s Max page describes Max 5x and Max 20x as relative per-session usage multipliers, with a separate shared weekly limit. The usage explainer says consumption depends on model, features, effort, conversation length, and complexity, with Claude and Claude Code sharing account limits. | Pro is the comparison baseline and Max 5x/20x are named in the inherited Max-policy record. Exact Opus 5.5 eligibility by tier and current plan prices were not captured. | The policy is account/plan-level and does not state an Opus 5.5-specific unit allowance. | Not captured. No Opus 5.5 base, cache-read/write, long-context, batch, or temporary API rate was recorded. | Not determinable: relative multipliers are not absolute token/API-dollar allowances; no exact-model rate or workload mix is available. |
| Claude Opus 5 | Same Anthropic account/plan rules. | Pro baseline and Max 5x/20x appear in the policy record; exact Opus 5 eligibility and current plan prices were not captured. | No Opus 5-specific allowance units. | Not captured. No exact Opus 5 rate schedule or cache/long-context/temporary price was recorded. | Not determinable for the same reasons as Opus 5.5. Do not transfer Opus 5.5 API rates. |
| Gemini 3.8 Flash | The Gemini Apps policy summary says usage is compute-based, varies by model/features/task, refreshes every five hours until a weekly cap, and identifies AI Pro as 4x standard and AI Ultra as 5x or 20x Pro depending on subscription. A separate Google AI credits page covers product-specific credits, not Gemini Apps compute limits. | AI Pro and AI Ultra are named in the inherited policy summary; current local prices and Gemini 3.8 Flash tier eligibility were not captured. | No 3.8 Flash-specific quota or credit conversion is in the inherited policy record. | Not captured. No Gemini 3.8 Flash input, output, cached-input, long-context, batch, or temporary API rate was recorded. | Not determinable: compute-based usage has no absolute unit budget in the captured summary, and exact-model pricing/token mix is missing. Google AI credits cannot be substituted for Gemini Apps compute quota. |

## Provider records and interpretation

### OpenAI

The existing OpenAI package captured the Codex plan help page on October 5, 2026. It says limits depend on the ChatGPT plan and directs the user to account-specific usage/reset information. That is a provider statement about how limits are surfaced, not a numeric allowance for any of the five models. The Plus overview and GPT-5.6/GPT-6 Pro ChatGPT limit page appear as links in the existing roster coverage matrix, but their capture timestamp/content was not preserved in the inspected source ledger.

No first-party OpenAI API pricing source was found in the inspected current-month package records. The task’s required API-rate table, including cached input, long-context brackets, and temporary pricing, therefore remains uncovered for all five models.

### Anthropic

The existing current-month Anthropic package records two opened provider-help pages checked October 5. The Max-plan page describes 5x/20x relative session allowance and a separate weekly limit. The usage explainer attributes consumption to model and workload characteristics and says chat and Claude Code use shared account limits. Neither record provides absolute token/API-dollar limits, and neither was captured as an exact Opus 5 or Opus 5.5 allowance.

No Anthropic API pricing source was present in the inspected current-month source ledger. Exact current plan prices, Opus 5/5.5 tier eligibility, API rates, cache rates, long-context surcharges, batch discounts, and temporary pricing were not retrieved.

### Google

The existing other-provider coding package records Gemini Apps limits and Google AI credits pages checked October 5. The former gives provider-level compute/quota semantics; the latter concerns separate product-specific credits. Neither record establishes Gemini 3.8 Flash’s exact app-tier access, absolute quota units, plan prices, or API pricing.

No Google AI Studio / Gemini API pricing source for Gemini 3.8 Flash was captured in the inspected package. Input/output/cache/long-context/batch/temporary rates remain uncovered.

## Calculation rule

No fixed dollar allowance is calculated for any assigned model. A valid API-equivalent envelope would require, at minimum, an exact-model rate card and an absolute allowance denominator tied to the eligible plan and period, plus the pricing-relevant usage mix (uncached input, cached input and cache writes if applicable, output, context length, and any batch/temporary rate conditions). The inherited OpenAI quota is account-specific but has no numerical value in the captured record; Anthropic publishes relative multipliers without an absolute base; Gemini policy is compute-based and task-dependent. Applying an assumed token mix or publishing a plan cap as observed usage would invent a value.

## Sources and remaining work

The source IDs and inherited facts are in `sources.jsonl` and `evidence.jsonl`. The attempted query and browser failure are in `query_log.jsonl`. The package remains incomplete until the required in-app browser is available and the current provider plan pages and exact-model API rate cards can be opened and recorded.
