# Research scope

## Question

For the exact ValueRank models named below, did a paid coding-subscription user publish a measured usage report within 2026-09-06–2026-10-06 and provide enough account or local usage-meter detail to calculate API-price-equivalent usage divided by subscription cost?

## In scope

Search Reddit first, then Hacker News and developer communities. Consider OpenCode Go/Go Plus, Ollama, Z.AI Code, Kimi Code, Qwen coding subscriptions, Grok coding plans, and other relevant paid coding-agent subscriptions. Exact target models:

1. GLM-5.2
2. GLM-5.3
3. GLM-5.3-Flash
4. DeepSeek V4 Pro
5. DeepSeek V4 Flash 0731
6. Kimi K3
7. Qwen3.8 Max
8. Grok 4.6
9. Grok 4.7
10. GPT-6 Sol
11. GPT-5.6 Sol
12. GPT-6 Astra
13. GPT-5.6 Luna
14. GPT-6 Luna
15. GPT-5.5

Both the post date and the reported measurement interval must fall within 2026-09-06 through 2026-10-06 inclusive.

## Candidate eligibility

A numeric case is eligible only when the source identifies an actual end-user and exact paid plan tier, names the exact model/version, and reports personally measured account usage/allowance or a user-controlled usage log for an in-window measurement. The usage data must be detailed enough to price the actual measured tokens/requests against an authoritative API rate for that same model/version and to compare the result with the paid subscription cost for the corresponding interval.

The numerator is derived only from user-measured use multiplied by exact-model API pricing. Provider-announced quotas, estimated request budgets, marketing claims, benchmark workloads, or subscription allowances alone cannot provide the numerator. Do not infer plan tier, model variant, token counts, measurement window, API rates, or subscription price.

## Out of scope

- Mistral models/plans.
- Native Codex numeric allowance and use claims; another workstream owns them.
- User reports published or measured outside the date window.
- Provider quota announcements as a substitute for user-measured usage.
- Model aliases without a defensible exact-version match.
- Local usage estimates without enough measured units or a matching API rate card.
- Extrapolated usage beyond the observed interval.

## Calculation rule

For a same-model measured interval, calculate API-equivalent spend from measured, priced components: `input_tokens × input_rate + cached_input_tokens × cached_input_rate + output_tokens × output_rate`, each rate expressed per one million tokens and divided by 1,000,000. Do not double-count reasoning tokens if the provider includes them in output tokens. Convert currency only with a dated, sourced rate. Divide API-equivalent spend by the actual paid subscription amount allocated to that same interval. If any component, exact model rate, or interval-matched plan price is missing, mark the record non-computable rather than substituting provider quota data.

## Required evidence boundaries

Keep provider account meters, user-controlled local logs, API-equivalent numerators, provider-published quotas, and subscription price denominators as distinct fields. Every candidate and exclusion must retain direct source links, reporter identity (public handle as displayed), exact tier, exact model string, publication date, measurement interval, and query provenance. Searches with no qualifying result must be logged by model, platform, and exact query; a bounded search result is not proof that no report exists.
