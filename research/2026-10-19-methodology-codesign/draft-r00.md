# ValueRank methodology — draft r00 (v2.0.0 as published 2026-10-19)

## Objective

Artificial Analysis (AA) publishes a Pareto frontier of Intelligence Index vs. total USD cost to run its Intelligence Index benchmarks. That frontier does not answer the question ValueRank exists for: **which frontier AI model is actually lowest cost for the value it delivers in practice**, once (a) subscription-plan economics are considered (a $20–$300/month plan can buy many times its fee in API-priced usage) and (b) benchmarks geared to real software-engineering work are weighed alongside general intelligence. ValueRank ranks the AA Pareto and near-Pareto models by that practical value, on two bases: API (pay per token) and Plan (subscription).

## Cohort

- Every model family on AA's rendered Intelligence-Index-vs-total-cost Pareto line, as observed (never recomputed from rounded values), plus every near-frontier family: a configuration whose rounded Index is within 3 points of the frontier's best Index at equal or lower cost. Each family is ranked with one selected configuration (reasoning effort). Current cohort: 19 models (e.g. GPT-6.1 Sol, GPT-6 Luna, Claude Opus/Sonnet/Haiku 5.5, Gemini 4 Argon, MiMo-V2.6 Pro/Flash, Grok 4.7, DeepSeek V4, GLM-5.3, Qwen3.8 Max).
- Evidence is exact-variant only: no result is transferred between model versions, reasoning efforts or agent harnesses. Missing values stay missing (never zero-, mean- or neutral-filled); per-row coverage and missing metric names are published.

## Cost (25% of the overall score, both bases)

- **Token efficiency** = AA's total USD cost to run the AA Intelligence Index benchmarks (tokens spent × list price).
- **API basis input**: AA total cost ÷ the model's AA Intelligence Index = USD per Index point.
- **Plan basis input**: that ÷ the highest eligible subscription **Value Multiple** = effective USD per Index point. Models with no eligible plan route fall back to the API figure (flagged).
- **Value Multiple** = API-priced usage a plan delivers ÷ plan fee. Evidence rules: provider-published quotas/marketing are never used as the numerator; only end-user-reported API-priced usage (last month, exact model variant, plan tier, date) or, for Anthropic and OpenAI Codex, SemiAnalysis's controlled subscription-account measurements with workload projections. Owner-authorised assumptions are labelled as such (e.g. Opus 5.5's measured Claude multiples ~57–59× applied to other Claude models; a common GPT multiple ~8–11×; MiMo 1.5× provisional). Each route carries an evidence grade: measured / claim / estimate / assumption.
- **Scoring**: log scale within the ranked cohort, score = 100 × (ln c_max − ln c) / (ln c_max − ln c_min); cheapest = 100, dearest = 0. Cohort spans ~2.9 to ~151 USD/point on API.

## Quality (75% of the overall score)

Each quality dimension is rank-normalised within the models that have a value: ((n − rank)/(n − 1)) × 100, ties averaged. Quality score = priority-weighted mean of a row's available dimensions (renormalised per row). Priorities (share of the 75%):

| Dimension | Priority | Share of overall |
|---|---:|---:|
| DeepSWE v1.1 (AA Coding Agent Index; pass@1 averaged over 3 attempts, 113 tasks; agentic SWE) | 25 | 17.52% |
| Bug Hunt Bench (planted bugs fixed /105, agent model+harness, owner scoreboard) | 20 | 14.02% |
| AA-Omniscience non-hallucination rate | 6 | 4.21% |
| Terminal-Bench 4.0 (official leaderboard; supplemental, many gaps) | 6 | 4.21% |
| GDPval-AA v2.1 | 6 | 4.21% |
| AA Intelligence Index (composite) | 6 | 4.21% |
| LiveBench Instruction Following | 5 | 3.50% |
| AutomationBench-AA | 5 | 3.50% |
| Speed (AA output tokens/s) | 5 | 3.50% |
| AA-LCR v1.1 (long context) | 4 | 2.80% |
| AA-Omniscience accuracy | 4 | 2.80% |
| HLE | 4 | 2.80% |
| GPQA Diamond (legacy) | 4 | 2.80% |
| SciCode | 4 | 2.80% |
| CritPt | 3 | 2.10% |

Overall = 0.25 × cost score + 0.75 × quality score (a row without a cost is scored on quality alone). Ties break by lower cost, then name. Provider-published benchmark claims are used only when the benchmark version and exact variant match, are labelled, and are replaced by owner results when available.

## Outputs

README/methodology/scores Markdown and a static site (valuerank.alolabs.dev) with API/Plan toggle, a cost-weight slider (default 25%), per-model evidence pages, and a Pareto view of composite cost vs quality. Current results — API: Gemini 4 Argon 69.5, GPT-6.1 Sol 65.7, Claude Sonnet 5.5 65.0. Plan: Claude Sonnet 5.5 77.2, Claude Opus 5.5 70.1, GPT-6.1 Sol 66.8.

## Known limitations

- Rank normalisation of quality discards magnitudes; benchmark displays are rounded; no uncertainty intervals.
- Coverage is uneven (Terminal-Bench 4.0, LiveBench IF and DeepSWE have gaps; coverage 58–100% of weight).
- Value Multiples are sparse, partly assumptions, and measured on specific workloads; plan rate limits, weekly caps and throttling are not modelled beyond the multiple.
- AA cost uses list prices and AA's token mix, not the user's workload; caching/batch discounts are not modelled.
- Bug Hunt and DeepSWE measure model+harness stacks, not the model alone.
