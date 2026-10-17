# Scope: first-party subscription-plan allowances for ValueRank models

## Research question

As of **2026-10-06**, what paid first-party subscription plans expose coding/product access to each of ValueRank's 13 ranked model IDs, what do those plans cost, how does each provider describe its included allowance and reset rules, and can the published plan quota be translated into API-list-price-equivalent usage from the same exact model?

## Ranked model roster

| Rank | Exact ValueRank model ID | First-party provider |
|---:|---|---|
| 1 | `gpt-6-sol` | OpenAI |
| 2 | `gpt-5.6-sol` | OpenAI |
| 3 | `gpt-6-astra` | OpenAI |
| 4 | `claude-opus-5-5` | Anthropic |
| 5 | `grok-4.7` | xAI |
| 6 | `gpt-5.6-luna` | OpenAI |
| 7 | `kimi-k3` | Moonshot AI |
| 8 | `grok-4.6` | xAI |
| 9 | `gemini-3.8-flash` | Google DeepMind |
| 10 | `glm-5.3` | Z.AI |
| 11 | `gpt-6-luna` | OpenAI |
| 12 | `claude-opus-5` | Anthropic |
| 13 | `qwen3.8-max` | Alibaba |

Mistral is excluded because it is not in ValueRank's ranked roster. No unranked variants may be substituted.

## Workstreams and evidence boundaries

1. **First-party plan facts:** eligible plan names, current published price and displayed currency/market, exact model availability when explicitly stated, quota unit, windows, resets, overage/top-up rules, and temporary terms. These are provider-published claims about plan design.
2. **First-party API pricing:** exact model/version rate cards with input, cached input, output, context tiers, promotional dates and currency. These rates may price an actual usage log, but do not themselves establish how much subscription usage a user receives.
3. **API-price-equivalent plan allowance:** calculate only when the first-party plan defines a quota unit and the same provider publishes a deterministic conversion from that unit to exact-model token components. Where model, token mix, context tier, or unit conversion is missing or usage is dynamic, use `N/C` and state the blocker. A range may be calculated only from explicit published component bounds.
4. **End-user reports:** user-measured results remain a separate workstream, date-limited to publication and measurement intervals from **2026-09-06 through 2026-10-06 inclusive**. Provider-published plan/API claims never become a user-reported value-multiple numerator. OpenAI community numerical evidence is restricted to the TiboTattle homepage; its aggregate observations are not individual user datapoints and cannot be assigned to exact models or current plan tiers.

## Inclusion rules

- Match exact model IDs and model versions; distinguish consumer app labels from API model IDs.
- Include currently offered consumer paid plans that provide access to a ranked model or plan-specific coding tool; disclose when first-party sources do not establish exact model access.
- Preserve provider's stated market/currency, list vs promotional price, start/end dates, and billing cadence.
- Preserve separate 5-hour, daily, weekly, and monthly quotas; do not treat one as the whole subscription allowance.
- Keep included plan usage, paid top-ups, API metering, user reports, and provider estimates separate.
- For non-computable plan/API equivalents, say what exact provider data would be needed to calculate them.

## Exclusions

- Provider-published quotas are not end-user value multiples.
- Third-party subscription resellers, bundled cross-provider plans, and unranked model variants.
- Mistral and models absent from the 13-row roster.
- Speculative token or task volumes, inferred model identity, and inferred plan-price mappings.
- User-measured reports outside the current one-month window.

## Deliverables

A provider-by-plan allowance table, 13-model coverage matrix, source/evidence/query/claim ledgers, API-equivalent calculations where computable, triangulation, three critique cycles, decision record, handoff, and the nine-phase Silver Bullet Ultradeep rollup. The sibling `coding-subscriptions` package and user-reported value-multiple table remain the source for community reports.
