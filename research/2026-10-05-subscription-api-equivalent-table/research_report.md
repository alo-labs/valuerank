# Subscription plan value by exact model variant

**Research date:** 2026-10-05. **Workflow:** Silver Bullet Deep Research, Ultradeep mode. **Status:** package assembled; automated Silver Bullet validators and parent review remain pending.

## Executive Summary

This report compares subscription routes only when an exact ValueRank model variant and an API-pricing-comparable allowance are evidenced. The roster contains 25 exact model IDs and efforts, drawn from the project's current raw data and README.[1] Eleven rows have at least one quantified exact route in the candidate set; fourteen remain without a qualified comparable denominator or current exact route. “Best quantified” means the greatest profile-dependent API-priced allowance per effective monthly fee among the routes with usable denominators. It does not mean a universal market-wide minimum where a competing subscription has exact model access but an opaque quota.

OpenCode publishes Go at US$10/month and Go Plus at US$40/month, together with exact model catalog names, model-specific monthly dollar use limits, matching token prices, and five-hour/weekly reset shares.[2] Ollama publishes Pro at US$20/month or US$200/year, with US$60 monthly usage credits; Max at US$100/month with US$300 credits; and Team at US$500/month with US$1,000 shared credits, plus model-specific token tariffs.[3] Z.AI publishes weekly and five-hour plan credits, a model-specific credit formula, current API rates, and current promotional rules.[4][5][6][13]

Selected routes span OpenCode for several exact catalog routes, Ollama Pro annual for Kimi K3 and DeepSeek V4 Pro, and Z.AI Coding Max annual for GLM-5.3. GLM-5.3-Flash's current snapshot route is Z.AI Max annual while the all-day half-credit promotion remains active through October 7; outside that short campaign, the value comparison depends on whether use falls during peak or off-peak hours. Its separate overnight campaign is time-limited and is not extrapolated to a full-month token allowance.[2][3][5][6][13]

The unknown rows are explicit. OpenAI/Codex crowdsourced allowance evidence was restricted to the TiboTattle homepage; it displayed a checking/loading state without a numeric series, so no OpenAI subscription denominator was used.[10][15] Claude and Gemini plan-meter observations lack a model/version-specific API-priced token mix; Kimi membership credits are relative rather than convertible; and Alibaba's exact Qwen3.8 Max token-credit coefficient is not public in the inspected docs.[8][9][11][12] No current-window user-reported numeric allowance was used as a route denominator. Profile definitions, calculations, all 60 qualified tier/cadence rows and eight unqualified DeepSeek catalog exception rows, evidence links, claims, and remaining gaps are included in the linked data package.

## Introduction and scope

Prices and plan terms were checked as of October 5, 2026. The roster's exact ID and benchmark effort are preserved row by row; the effort value is metadata and is not used to infer plan entitlement.[1] The work compares publicly evidenced routes, not all possible subscription programs. Fifteen source records cover the roster, first-party routes, current research packages, and the allowed Codex homepage observation. All 25 roster IDs appear in `table.md` and `model-coverage.csv`.

## Findings

OpenCode is the strongest direct route source for its catalog: the public page exposes monthly plan prices, matching API-route prices, and per-model plan caps. The ratio of model-specific limit to subscription fee yields stable US-dollar value multiples for a given model and tier; token totals still vary with the selected profile and published context-price bracket.[2] Go and Go Plus each appear for every relevant exact route, so the complete table retains both tiers rather than just the chosen tier. DeepSeek V4 Flash is left unranked at the exact-version level. ValueRank raw-data identifies the evaluated version as V4 Flash 0731; DeepSeek's September 10 notice says the previous V4 Flash was retired and the legacy API name is temporarily routed to V4.1 Flash. OpenCode separately lists V4 Flash and V4.1 Flash with different Go caps, but does not disclose the upstream version served by its legacy catalog row; Ollama lists V4.1 Flash. The eight adjacent catalog tier rows and their prices/allowances are retained in `route-exceptions.csv` solely to document the gap, and no V4.1 sibling allowance is applied to the roster row.[1][2][3][7]

Ollama's included credits are denominated in dollars and reset monthly without rollover. Pro annual reduces the effective fee to US$16.67/month while retaining US$60 monthly credits; Max and Team are also retained in every relevant model comparison. Team's balance is shared, so its computed envelope is a team-wide single-model illustration rather than a per-user result.[3] Ollama's token totals for DeepSeek routes differ by the provider's published peak/off-peak API rates, while the US-dollar credit value itself remains fixed.[3]

Z.AI uses a non-dollar quota, so its calculations apply the provider's exact model-specific input, cached-input, and output multipliers to each profile and then the matching public API tariff. Lite, Pro, and Max weekly quotas and five-hour caps are retained. Z.AI's current public price page discloses monthly and annual-equivalent prices; the plan documentation confirms quarterly billing but the inspected public page did not expose its fee. Quarterly value multiples therefore remain blank/not computable, not derived from an assumed discount.[4][5][6][14]

The route outcomes do not erase evidence gaps. The plan reports for Claude and Gemini describe utilization percentages or relative plan limits rather than exact per-variant token budgets. Kimi's public membership tiers use relative agent credits with no published API conversion; Alibaba identifies Qwen3.8 Max access and monthly plan credits but no model-specific conversion coefficient. Such routes cannot be ranked against API-priced allowances without a missing denominator.[8][9][11][12]

## Workload profiles and interpretation

Three profiles make the API-equivalent usage comparable while exposing mix sensitivity: P1 uses 50% uncached input, 25% cached reads, and 25% output; P2 uses 75% uncached input and 25% output; P3 uses 20% uncached input, 60% cached reads, and 20% output. Cache writes and tools are set to zero. These are scenarios, not observed benchmark traces. OpenCode and Ollama dollar credits map directly to monthly route-dollar value, while tokens per month are profile-dependent. Z.AI converts weekly credits using a 52/12 monthly factor, a documented credit formula, and the corresponding per-token API price.[2][3][5][6]

Z.AI also varies by time. The base scenario assumes full-rate peak credit consumption; an all-off-peak scenario doubles the token/API-equivalent amount because the provider states that off-peak usage consumes half the normal credits. No mixed schedule is invented. The current all-day half-credit campaign through 2026-10-07 is separately shown as a 2× current-window case. The GLM-5.3-Flash offer additionally grants zero quota consumption via ZCode or AutoClaw from 23:00 to 09:00 Singapore time, or double quota via other supported agents in that window. Neither the partial-day offer nor any possible stacking is annualized.[5][13]

## Coverage and limitations

The table distinguishes a selected quantified route from an unquantified provider alternative. “Best quantified” is a bounded statement over the documented candidate set; it is not a complete provider-market census. Account meters, request estimates, broad family access, relative-credit plan descriptions, and user anecdotes do not establish API-equivalent monthly use by themselves. Model names can also change their served version: the dated DeepSeek alias notice is recorded so the legacy model ID does not inherit a sibling cap without a direct identity mapping.[7]

Route availability can vary by region. Muse Spark 1.2 Contributor is marked limited-region in OpenCode's model catalog.[2] OpenCode token envelopes for Grok assume requests in the ≤200K pricing bracket and GPT Luna rates use the ≤272K bracket; larger contexts require their separate price row and a recalculation.[2] Z.AI's mixed peak/off-peak amount depends on schedule. Ollama Team is shared usage. Alibaba's Qwen plan-credit model coefficient and Z.AI quarterly price remain missing. These limits are carried into CSV/JSON fields and do not receive guessed substitutes.

## Decision and next step

Use the `table.md` and `tier-register.md` as a current, evidence-bounded comparison; use `route-tiers.csv` and `routes.json` to reproduce the formulas. No numeric user-reported plan allowance was promoted to an entitlement. A saved local validator, run through LeanCTX shell execution, passed coverage, route-tier, arithmetic, date-window, referential-integrity, and package-presence checks. Silver Bullet-specific automated gates and parent review remain pending.

## Bibliography

[1] ValueRank current model roster. Retrieved 2026-10-05. ../../raw-data.md; ../../README.md.
[2] OpenCode Go usage limits and model pricing. Retrieved 2026-10-05. https://opencode.ai/v2/docs/console/go.
[3] Ollama pricing. Retrieved 2026-10-05. https://ollama.com/pricing.
[4] ZCode / GLM Coding Plan pricing. Retrieved 2026-10-05. https://zcode.z.ai/en.
[5] Z.AI GLM Coding Plan overview. Retrieved 2026-10-05. https://docs.z.ai/devpack/overview.
[6] Z.AI API pricing. Retrieved 2026-10-05. https://docs.z.ai/guides/overview/pricing.
[7] DeepSeek Models & Pricing and current API release notes. Retrieved 2026-10-05. https://api-docs.deepseek.com/quick_start/pricing/.
[8] Alibaba Cloud AI Token Plans and Token Plan documentation. Retrieved 2026-10-05. https://www.alibabacloud.com/en/campaign/ai-landing-page-token?_p_lc=1.
[9] Current allowance research index. Retrieved 2026-10-05. ../2026-10-05-allowance-research-index.md.
[10] TiboTattle / OpenAI Codex allowance research. Retrieved 2026-10-05. ../2026-10-05-tibotattle-openai/report.md.
[11] Other provider chat allowance research. Retrieved 2026-10-05. ../2026-10-05-other-provider-chat/report.md.
[12] Other provider coding allowance research. Retrieved 2026-10-05. ../2026-10-05-other-provider-coding/report.md.
[13] GLM-5.3-Flash Usage Campaign. Retrieved 2026-10-05. https://docs.z.ai/devpack/notice/event-glm-5.3-flash.
[14] ZCode Connect Models — Trial Quota and Coding Plans. Retrieved 2026-10-05. https://zcode.z.ai/en/docs/configuration.
[15] TiboTattle — Codex allowance estimates homepage. Retrieved 2026-10-05. https://tibotattle.com/.
