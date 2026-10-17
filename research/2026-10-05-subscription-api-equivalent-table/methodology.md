# Methodology

## Decision rule

The comparison selects the largest profile-specific API-equivalent monthly allowance per effective monthly subscription fee among qualified exact-variant routes. The reciprocal is the effective subscription spend per US$1 of API-priced value. This is a relative plan-value measure; it is not a cash refund, actual account bill, or general token cap.

## Standard token workloads

| Profile | Uncached input | Cached input read | Output | Cache write |
|---|---:|---:|---:|---:|
| P1 — balanced agent | 50% | 25% | 25% | 0% |
| P2 — uncached development | 75% | 0% | 25% | 0% |
| P3 — prompt reuse | 20% | 60% | 20% | 0% |

Each profile represents one million total model tokens across the indicated categories. These are transparent comparison scenarios, not a claim about ValueRank benchmark prompts or any user's traffic. Image, audio, tool, MCP, cache-write, and provider-specific reasoning-token overhead is excluded.

## API price and plan calculations

For a route with API rates in USD per million tokens, profile cost per million total tokens is:

`profile_API_USD_per_1M = uncached_input_share × input_rate + cached_input_share × cached_read_rate + output_share × output_rate`.

For OpenCode, a published model-specific monthly dollar limit is the monthly API-priced value. The API-equivalent token envelope for each profile is that limit divided by the profile's route cost per million tokens. Go and Go Plus share route token prices but publish different model-specific limits. Each model has a five-hour cap equal to 20% of its monthly limit, a 50% weekly cap, and a monthly 100% limit. Grok 4.6/4.7 token envelopes use the published ≤200K context rates; GPT-6 Luna and GPT-5.6 Luna use ≤272K context rates. The table does not assume larger-context requests.

For Ollama, included dollar credits are divided by the same provider's listed input/cached-input/output rates. The API-equivalent dollar allowance equals the included dollar credit amount; token totals depend on profile and time-based tariffs. Pro annual is $200 prepaid for 12 months and includes $60 usage credits each month. Max is $100 monthly/$300 credits. Team is $500 monthly/$1,000 shared credits. Team values are shared across the team and are not per-seat comparisons.

For Z.AI, credits are not dollars. Weekly quota is converted to an average month as `weekly_credits × 52 / 12`; the separate five-hour credit quota remains a concurrency/reset constraint and is not multiplied by monthly weeks. For one million total tokens, profile credit use is `100 × (input_share × input_multiplier + cached_share × cached_multiplier + output_share × output_multiplier)`. Estimated millions of tokens equal monthly-equivalent credits divided by profile credits per million. API-equivalent USD equals estimated token millions times the matching GLM model's API cost per million. No cache-write or MCP calls are included.

Z.AI values have an additional time basis. Standard peak-rate credits are the baseline. Official plan docs say usage outside weekday 14:00–18:00 Singapore time consumes 50% of normal credits. A workload entirely off-peak therefore has twice the profile token and API-equivalent allowance; a mixed schedule requires the actual peak/off-peak share. On 2026-10-05, a temporary all-day 50%-credit campaign is active through 2026-10-07, so its 2× scenario is shown separately. The additional Flash campaign grants zero quota consumption through ZCode/AutoClaw from 23:00–09:00 Singapore time, or doubles available quota for other supported agents during that window. This partial-day offer is not stacked or annualized into a monthly token total.

## Fee and cadence

All selected-provider comparisons preserve USD as published. Monthly fees remain monthly. Annual prepaid fees show the total and effective monthly price (annual amount / 12). A quarterly billing option is documented for Z.AI, but its exact price was absent from the inspected current public page. The six GLM-5.3 and GLM-5.3-Flash quarterly rows retain their published credits and independently computed profile API-equivalent usage, while fee_per_period is explicitly not published, effective monthly fee and fee-dependent multiples are not computable, and annual-effective monthly price is marked not applicable to quarterly billing. routes.json preserves numeric nulls with categorical feeStatus and valueMultipleStatus; no monthly or annual price is transferred. No price is inferred from a claimed discount.

## Identity and exact-variant policy

Provider catalog labels must match a ValueRank exact model variant. A dated first-party mapping may establish an alias only for the provider route it documents; it does not establish how a third-party subscription routes a separately labeled catalog entry. DeepSeek's 2026-09-10 change log says its previous-generation V4 Flash was retired and its legacy direct API name is temporarily routed to V4.1 Flash. OpenCode separately lists V4 Flash and V4.1 Flash with different Go caps, but does not disclose which upstream variant its legacy subscription catalog row serves; Ollama lists V4.1 Flash only. Therefore no current subscription is qualified for the roster's DeepSeek V4 Flash 0731 variant. The eight provider tier rows appear in `route-exceptions.csv` as unqualified evidence, and no V4.1 tariff or allowance is applied to the roster row. Z.AI's documentation redirects GLM-5.2 plan requests to GLM-5.3, so that subscription is excluded for the GLM-5.2 row. Exact-model labels are not extended by vendor-family mention.

## Evidence classes

- `provider_published_model_specific_usd_cap`: route provider publishes the specific monthly dollar limit and route-specific API token prices.
- `provider_published_usage_credits`: provider publishes paid monthly dollar credits and model tariffs.
- `provider_published_credit_formula_analyst_derived`: provider publishes a non-dollar plan quota, model multipliers, formula, and corresponding API tariffs; analyst computes the profile values.
- `not_computable`: exact plan/model may exist, but a comparable denominator or public term price is missing.

## User-reported allowance treatment

The current-window research packages were reviewed for 2026-09-05–2026-10-05. No user-reported numeric allowance was used as a denominator. Reports that omit plan tier are treated as “not stated” and never assigned the thread author's tier. For OpenAI/Codex crowdsourced numeric allowance, only the TiboTattle homepage was allowed; it displayed a checking/loading state, so no number was entered.

## Limits

Values are point-in-time and depend on route availability, account region, context size, cache rate, plan reset rules, model API rates, and Z.AI usage schedule. The roster table is not a complete subscription-market census. A maximum among quantified routes is not proof of global minimum where a competing service's allowance is opaque.
