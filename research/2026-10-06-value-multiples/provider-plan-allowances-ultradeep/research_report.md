# First-party subscription allowances for ValueRank models

**As of:** 2026-10-06 (Australia/Sydney). **Workflow:** Silver Bullet Deep Research, Ultradeep. **Scope:** first-party plan and API documentation for all 13 ranked ValueRank model IDs across seven providers. **Status:** evidence package assembled; validator logs and independent package review are the final checks.

## Executive summary

This Ultradeep review documents first-party subscription terms and API rate cards for all 13 ValueRank model IDs across seven providers. It separates paid-plan price, product/model access, allowance units, API pricing, and end-user observed usage because the sources do not make these interchangeable. Most providers publish a price, relative quota label, message/task cap, or rolling reset but do not disclose the exact model-specific token mix needed to calculate the subscription's API-list-price equivalent. Consequently, a complete API-equivalent allowance multiple is not available for those plans.

Z.AI is the single bounded exception in the reviewed first-party material: its GLM-5.3 Coding Plan documents weekly and five-hour credit caps, a credit formula, and an API rate card. The resulting API-price-equivalent range is theoretical and composition-dependent, not user-observed consumption. For OpenAI, Anthropic, xAI, Google, Moonshot AI/Kimi, and Alibaba, at least one conversion input remains absent or conflicting; their plan-equivalent cells stay N/C, not zero. Exact API tariffs are recorded separately and do not fill a subscription-quota gap.

These provider materials are useful for fees and rate-card denominators, but they are not eligible numerators in the companion end-user value-multiple table. That table can include only actual user-reported measurements valued at API rates, with the exact plan tier and measurement window recorded. The 13-model roster and ordering are fixed from the project ranking source and model data [1]. No rates are transferred between model variants, no currencies are ranked without FX normalization, and no provider marketing or allowance claim is presented as measured user usage.

## Introduction

### Scope and method

Research ran in Ultradeep mode under Silver Bullet's nine-phase workflow. Retrieval used the Codex built-in in-app browser only, with direct first-party plan, help, and developer pages as claim sources. Search pages are logged for query provenance but are not factual evidence. The package contains 28 first-party source records plus the local roster record (29 total; mean source credibility 100/100). The Ultradeep nominal source target is 30 with a maximum of 40 and a minimum average credibility of 75; the 15-minute time-based triage gate had elapsed, and the remaining known gaps are explicit. The paid-plan scope includes routes with first-party documented access to ranked products: ChatGPT Go is listed at A$13, but its feature block does not establish a Codex allowance or exact ranked-model access, so it is excluded as a verified route; Free is outside the paid-plan scope. See `query_log.jsonl`, `sources.jsonl`, and `vloop-rollup.json`.

Plan entitlement, plan allowance, API tariff, and end-user observed usage were kept separate. A plan/API equivalent is shown only when a first-party source supplies the allowance unit and a deterministic conversion for the exact model. USD API rates remain in USD; plan fees remain in the page's currency and region. No exchange rate or cross-provider value rank is inferred.

## Main Analysis

The provider findings below distinguish paid-plan access, quota descriptions, API rate cards, and conversion limits.

### OpenAI

The Australia-localized ChatGPT page displays Plus at A$30/month and Pro from A$155/month, with expanded Codex usage on Plus and Pro. The current Help Center describes a shared Work/Codex usage meter. For Plus and Standard Business it estimates five-hour local messages at 5–45 for GPT-6 Astra, 15–150 for GPT-6 Sol, and 350–3,000 for GPT-6 Luna, while warning that task size, settings, and weekly limits affect actual use. Current Pro 100/200/500 tiers have no five-hour Work/Codex cap, but still have included-use limits; new Pro 200 allowance is lower than a grandfathered earlier cohort, whose treatment ends 2026-10-29 for the specified signup window. These are message estimates and windows, not token budgets or API-dollar quotas. [ChatGPT pricing](https://chatgpt.com/pricing/) [2], [Work/Codex usage](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) [3], [Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers) [4].

The API page lists exact rows for GPT-6 Astra, GPT-5.6 Sol, and GPT-6 Luna. It lists `gpt-6.1-sol`, not the ranked `gpt-6-sol`, and has no exact `gpt-5.6-luna` row. No sibling or punctuation-based transfer is made. API rates for the exact available IDs are in `model_coverage.csv`; no OpenAI plan row gets an API-equivalent range because the plan meter does not publish request token composition or full period quota. [OpenAI API pricing](https://developers.openai.com/api/docs/pricing) [5].

### Anthropic

The official web plan page lists Pro at USD 20/month, Max 5x at USD 100/month, and Max 20x at USD 200/month. Max describes 5x or 20x Pro per-session use, a five-hour reset, and a shared weekly cap across models; no absolute Opus-specific token or API-dollar cap is published. Claude Code is available with Pro and Max, while paid usage credits are a separate purchase after included allowance is used. The exact API tariffs are USD 4 / 0.20 cached read / 5 cache write / 20 output per million tokens for Opus 5.5, and USD 5 / 0.50 / 6.25 / 25 for Opus 5. Because a rate card cannot reveal the undisclosed subscription token mix, both model plan/API equivalents remain N/C. [Max plan](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) [6], [Claude/API pricing](https://claude.com/pricing#api) [7], [usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans) [8], [Claude Code access](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) [29].

### xAI

The current consumer page displays SuperGrok at USD 30/month and SuperGrok Plus at USD 100/month. xAI says paid Grok products share one flexible weekly pool; the FAQ gives no pool size or model-specific API-dollar amount, and separately sold extra usage credits are not included quota. The inspected consumer model table shows Grok 4.6 but does not establish Grok 4.7 subscription access. The developer tariff does list both API models: short-context rates are USD 2 input / 0.50 cached input / 6 output per million tokens; long-context rates are USD 4 / 1 / 12. Grok 4.7's plan access and both models' API-price-equivalent plan allowances therefore remain unverified/N/C. [xAI pricing](https://x.ai/pricing) [9], [Grok FAQ](https://docs.x.ai/grok/faq) [10], [API pricing](https://docs.x.ai/developers/pricing) [11].

### Google DeepMind

The Australia-localized page displays AI Plus at A$7.99/month, AI Pro at A$32.99/month, and AI Ultra at A$149.99 for 5x Pro usage or A$329.99 for 20x. App limits depend on prompt complexity, models/features, and conversation length; they use a compute-based five-hour allowance up to a weekly limit. This is not a published API token allowance. Consumer support documentation uses the label Gemini 3 Flash, but does not map that label to the exact API model ID `gemini-3.8-flash`. The API directory confirms the ID and the API price page lists USD 0.75 input / 0.075 cached input / 3.75 output per million tokens through 2026-12-31; the scheduled 2027-01-01 rates are 1.50 / 0.15 / 7.50. The subscription API equivalent stays N/C due both model crosswalk and compute conversion gaps. [Google AI subscriptions](https://gemini.google/subscriptions/) [12], [Gemini app limits](https://support.google.com/gemini/answer/16275805) [13], [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) [14], [API models](https://ai.google.dev/gemini-api/docs/models) [15].

### Moonshot AI / Kimi

Kimi's official membership help page lists Andante CNY 49/month, Moderato CNY 99, Allegretto CNY 199, and Allegro CNY 699. It estimates about 30, 60, 150, and 360 Agent uses from shared monthly credits and lists Kimi Code access; these task counts are provider estimates, not K3 token allotments. A second first-party Code page says new members have no weekly cap but retain a rolling five-hour rate window and shared monthly quota; existing legacy subscribers retain weekly limits. The membership page instead says Kimi Code has a separate five-hour/week limit. Since these are conflicting official descriptions and use different tier labels (Andante et al. versus Go/Plus/Pro), the current Code reset and exact K3 tier mapping remain unresolved.

Kimi's API documents give exact `kimi-k3` rates of USD 3 input / 0.30 cache read / 15 output per million, with cache writes at USD 3 for five-minute TTL and USD 6 for one-hour TTL. The quickstart confirms the API model ID and states API access requires a minimum USD 1 account top-up; API recharge limits are not subscription credits. The plan/API equivalent is N/C because the membership credit balance and exact tier crosswalk are not public. [Kimi membership prices](https://www.kimi.com/en/help/membership/membership-pricing) [16], [Kimi Code membership](https://www.kimi.com/code/docs/en/kimi-code/membership.html) [17], [K3 API pricing](https://platform.kimi.ai/docs/pricing/chat) [18], [API limits](https://platform.kimi.ai/docs/pricing/limits) [19], [K3 quickstart](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) [20].

### Z.AI

Z.AI publishes Lite at USD 18 list / USD 12.60 current promotional monthly price, Pro at USD 80 / USD 56, and Max at USD 168 / USD 117.60. Weekly plan credits are 10,000 / 60,000 / 140,000 with separate five-hour caps of 2,000 / 12,000 / 28,000. GLM-5.3 is an exact supported plan model. The provider also publishes its credit formula: weights 6.9 for uncached input, 1.7 for cached input, and 24 for output per million-token basis, with API prices of USD 1.40 / 0.26 / 4.40 per million respectively.

At those published rates, one million cached-input tokens correspond to 170 credits and USD 0.26, or USD 0.0015294 per credit; one million uncached-input tokens correspond to 690 credits and USD 1.40, or USD 0.0020290 per credit; output falls between those values. Applying the lower and upper per-credit values to the average monthly credits (weekly quota × 52/12) gives Lite USD 66.27–87.92, Pro USD 397.65–527.54, and Max USD 927.84–1,230.92 in API list-price-equivalent usage per average month. These are composition bounds, not realized usage, and exclude the current all-day off-peak half-credit incentive running 2026-09-25 through 2026-10-07, as well as the separately linked GLM-5.3-Flash promotion. [Z.AI plan](https://zcode.z.ai/en) [21], [plan overview](https://docs.z.ai/devpack/overview) [22], [usage policy](https://docs.z.ai/devpack/usage-policy) [23], [API prices](https://docs.z.ai/guides/overview/pricing) [24], [campaign notice](https://docs.z.ai/devpack/notice/event-glm-5.3-flash) [25].

### Alibaba

Alibaba's personal Token Plan lists monthly Lite at CNY 39 current / CNY 60 list with 11,500 credits; Essential CNY 79 / 120 with 25,500; Standard CNY 139 / 180 with 45,000; and Pro CNY 499 / 600 with 180,000. Credits refresh monthly without rollover; weekly plan limits were removed in September. Qwen3.8 Max is listed as supported, but the official page says deductions depend on model, token volume, thinking mode, and tool calls and publishes no deterministic Qwen3.8-Max credit coefficient. A provider-controlled nighttime offer currently uses 40% of ordinary credits for Qwen3.8 Max during 22:00–08:00; it is not projected across a whole month.

Alibaba Cloud Model Studio separately identifies API ID `qwen3.8-max` and lists USD 1.65 input, 4.951 output, 0.206 implicit cached input, 2.063 explicit cache creation, and 0.137 explicit cache read per million tokens. Because the personal Token Plan and Model Studio API are separate channels, and the personal plan conversion is missing, API-equivalent allowance remains N/C. [Token Plan overview](https://platform.qianwenai.com/docs/token-plan/overview) [26], [personal plan](https://platform.qianwenai.com/docs/token-plan/personal/token-plan-personal-overview) [27], [qwen3.8-max Model Studio pricing](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) [28].

## Synthesis

### Model-by-model coverage

The exact 13-row model crosswalk, tier status, API tariff, context/date notes, evidence IDs, and missing inputs are in `model_coverage.csv`. The only ranked ID with a computable bounded plan API-dollar range is GLM-5.3. Every other row is N/C, not zero. In particular, the OpenAI `gpt-6.1-sol` API row is not substituted for `gpt-6-sol`; Grok 4.7 consumer access, Gemini app/API identity, and Kimi tier mapping remain unverified.

## Limitations

The publication does not disclose token composition for most subscription quotas, so API rate cards alone cannot yield an included allowance value. Several product/API model labels do not resolve to the exact ranked variant; current Kimi Code reset descriptions conflict; and Alibaba does not publish a deterministic Qwen3.8-Max personal-plan credit coefficient. Z.AI's calculated range depends on input/cache/output composition and therefore is a bound, not realized usage. Prices are shown in source currencies without cross-provider FX ranking. Source-level gaps and exclusions are enumerated in `exclusions.jsonl`; calculations are reproducible from `calculations.csv`; query provenance is in `query_log.jsonl`.

## Recommendations

1. Keep this first-party subscription research separate from the user-reported four-column Value Multiple table. First-party allowance claims may support plan-fee or API-rate evidence, but must never supply that table's usage numerator.
2. Use published API prices only when the exact model ID, version, and region/context tier match. Leave unmatched API rows unpriced.
3. Display local subscription currency alongside USD API equivalence; do not infer FX or a cross-provider value rank.
4. Retain current promotional and list prices separately, and do not project limited-time credits across a full month.
5. Prioritize exact-model included-token meters for OpenAI, Anthropic, xAI, and Google; xAI Grok 4.7 access; Google's app/API ID crosswalk; Kimi's plan-tier/reset crosswalk and credit conversion; Alibaba's Qwen3.8-Max plan coefficient; and exact API rates for ranked OpenAI `gpt-6-sol` and `gpt-5.6-luna`.

## Bibliography

[1] ValueRank project (2026). "Ranked model roster and model data." [Project ranking source](../../../scores.md); [model data source](../../../raw-data.md).
[2] OpenAI (2026). "ChatGPT pricing." https://chatgpt.com/pricing/
[3] OpenAI (2026). "Managing usage with GPT-6 Astra in Work and Codex." https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex
[4] OpenAI (2026). "About ChatGPT Pro tiers." https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
[5] OpenAI (2026). "API pricing." https://developers.openai.com/api/docs/pricing
[6] Anthropic (2026). "What is the Max plan?" https://support.claude.com/en/articles/11049741-what-is-the-max-plan
[7] Anthropic (2026). "Claude pricing and API pricing." https://claude.com/pricing#api
[8] Anthropic (2026). "Manage usage credits for paid Claude plans." https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
[9] Anthropic (2026). "Use Claude Code with your Pro or Max plan." https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
[10] xAI (2026). "Pricing." https://x.ai/pricing
[11] xAI (2026). "Grok FAQ." https://docs.x.ai/grok/faq
[12] xAI (2026). "API pricing." https://docs.x.ai/developers/pricing
[13] Google (2026). "Google AI subscriptions." https://gemini.google/subscriptions/
[14] Google (2026). "Gemini Apps limits and upgrades." https://support.google.com/gemini/answer/16275805
[15] Google (2026). "Gemini API pricing." https://ai.google.dev/gemini-api/docs/pricing
[16] Google (2026). "Gemini API models." https://ai.google.dev/gemini-api/docs/models
[17] Moonshot AI (2026). "Kimi membership pricing and plan overview." https://www.kimi.com/en/help/membership/membership-pricing
[18] Moonshot AI (2026). "Kimi Code membership benefits." https://www.kimi.com/code/docs/en/kimi-code/membership.html
[19] Moonshot AI (2026). "Kimi API chat pricing." https://platform.kimi.ai/docs/pricing/chat
[20] Moonshot AI (2026). "Kimi API rate limits." https://platform.kimi.ai/docs/pricing/limits
[21] Moonshot AI (2026). "Kimi K3 quickstart." https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
[22] Z.AI (2026). "Coding Plan pricing." https://zcode.z.ai/en
[23] Z.AI (2026). "GLM Coding Plan overview." https://docs.z.ai/devpack/overview
[24] Z.AI (2026). "GLM Coding Plan usage policy." https://docs.z.ai/devpack/usage-policy
[25] Z.AI (2026). "API pricing." https://docs.z.ai/guides/overview/pricing
[26] Z.AI (2026). "GLM-5.3-Flash usage campaign." https://docs.z.ai/devpack/notice/event-glm-5.3-flash
[27] Alibaba (2026). "Qwen Token Plan overview." https://platform.qianwenai.com/docs/token-plan/overview
[28] Alibaba (2026). "Personal Token Plan." https://platform.qianwenai.com/docs/token-plan/personal/token-plan-personal-overview
[29] Alibaba (2026). "qwen3.8-max model information." https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max

## Methodology

The reviewed sources are first-party product, support, and API-pricing pages retrieved on 2026-10-06 using the Codex in-app browser. Query provenance is in `query_log.jsonl`; source identities and credibility assessments are in `sources.jsonl`; atomic evidence and claim support are in `evidence.jsonl` and `claims.jsonl`; exclusions and calculation inputs are persisted in their corresponding ledgers. Plan and API terms were compared only where the exact ranked model ID, subscription route, region, and allowance unit were stated. Missing or conflicting conversion inputs remain N/C. No provider-published allowance is used as an end-user measured-use numerator; the companion value-multiple table accepts only API-priced usage reported from actual user measurements.

## Report Metadata

- Workflow: WF-SILVER-DEEP-RESEARCH; flow step: FS-SILVER_DEEP_RESEARCH; atomic flow: AF-DECIDE.
- Mode: ultradeep; research type: default; as-of date: 2026-10-06.
- Scope: first-party subscription and API documentation for the 13 ranked ValueRank models.
- Retrieval fallback: search CLI unavailable; Codex in-app browser used for page retrieval.
- Evidence boundary: provider pages support fees and tariff facts only, not observed-user allowance numerators.
- Package: `research/2026-10-06-value-multiples/provider-plan-allowances-ultradeep/`.
