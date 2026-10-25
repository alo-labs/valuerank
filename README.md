# ValueRank
**Frontier AI configurations ranked by value for software engineering and DevOps: benchmark quality against what the work costs**

**Version:** v3.0.0
**Updated:** October 19, 2026
**Methodology:** 3.0.0 · SDLC basket v1 · anchor version v3-2026-10-23
**Scope:** 9 cohort configurations (9 with a value score) from a 61-model AA-mapped roster; value is a 25% cost score (nominal weight; 115% of API and 28% of Plan value variance) plus 75% quality over 13 benchmark leaves

## Current result

ValueRank ranks frontier AI model configurations (see Model inclusion) by value for software engineering and DevOps work, separately for API buyers and for subscription (Plan) buyers. It publishes 2 rankings (owner decision O53), each over the configurations that have its complete benchmark set: the **max-effort ranking** below (one configuration per model family at its top effort, scored on the AA leaves plus LiveBench 2.0 Overall and two Vals AI boards) and the AI Coding Daily ranking after it. The max-effort ranking's leaves: FrontierCode 1.1 15%, Terminal-Bench 4.0 (AA run) 11%, Bug Hunt Bench 8%, Vibe Code Bench v1.1 (Vals) 5%, Code Migration v1.1 (Vals) 6%, LiveBench 2.0 Overall 15% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares. Value is a fixed **25%** cost score plus **75%** benchmark quality. That weight is nominal: on the current panel cost's covariance allocation of value variance is 115% on the API basis and 28% on the Plan basis; an allocation above 100% means quality's is negative: dearer configurations score higher on quality, so the quality differences partly offset the cost differences instead of adding spread of their own (see [methodology.md](methodology.md)). Cost is the contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost): Artificial Analysis' (AA) published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates (the max-effort ranking's basket; each ranking admits its own components, E254), scored on a log scale against frozen anchors so cost ratios keep their size. Coding and terminal tasks (Coding Agent Index, Terminal-Bench 4.0 (AA Index run), SciCode) make up 48% of the basket's cost (median over 8 configurations with the full basket; 36% to 85%); AA-Briefcase, GDP.pdf, which have no quality leaf, make up 17%; the Coding Agent Index's SWE-Atlas QnA (124 of its 290 tasks) has no quality leaf either, and its cost share is not separable because AA publishes one pooled cost. Quality is the weighted mean of 13 (in the max-effort ranking; 11 in the AI Coding Daily ranking) benchmark leaves on fixed 0–100 anchors, and every configuration ranked in a ranking has all of that ranking's leaves for its exact configuration (O36): a leaf AA has not run comes from another party's run of the same benchmark, then from the model provider's published result, and a configuration still missing one after a logged exhaustive search is listed, not ranked. The Plan ranking divides the basket's API cost by a subscription route's Value Multiple at full utilisation, with one row per configuration and plan (O48), and uses the API cost, flagged, when no route is admitted. No Value Multiple is yet identified on the basket itself (0 of 27 rows), so the Plan ranking is labelled exploratory.

Claude Opus 5.5 leads the Plan ranking at 64.3; DeepSeek V4.1 Flash 1017 leads the API ranking at 60.4; Claude Opus 5.5 leads on quality.

| Plan rank | API rank | Configuration | Plan value | API value | Quality | Quality coverage | API cost (USD per basket run) | Plan cost (USD per basket run) | Plan route | Flags | Noise band (Plan / API) |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | 6 | [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 64.3 | 54.0 | 67.9 | 100% | $9,351.72 | $158.77 | Claude Pro $20 · Opus 5.5 (58.9×, measured) | — | 1–10 / 6–9 |
| 4 | 8 | [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 63.8 | 53.5 | 67.1 | 100% | $8,931.28 | $151.63 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–10† / 6–9 |
| 7 | 3 | [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 62.7 | 60.2 | 64.3 | 100% | $1,233.11 | $114.47 | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | — | 1–10 / 1–3 |
| 11 | 9 | [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 59.8 | 51.5 | 51.3 | 100% | $966.92 | $16.42 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 11–20† / 6–9 |
| 14 | 7 | [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 58.8 | 53.8 | 65.0 | 100% | $5,885.05 | $406.29 | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | — | 11–20 / 6–9 |
| 17 | 4 | [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 58.1 | 57.5 | 47.4 | 100% | $125.72 | $11.67 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 11–20† / 4–5 |
| 22 | 1 | [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 53.7 | 60.4 | 58.2 | 100% | $410.04 | $410.04 | — | API-cost fallback | 22–26 / 1–3 |
| 23 | 2 | [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 51.9 | 60.3 | 54.2 | 100% | $136.13 | $115.28 | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | subset cost | 22–26† / 1–3 |
| 27 | 5 | [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 50.6 | 55.5 | 64.3 | 100% | $3,557.77 | $3,557.77 | — | API-cost fallback | 27 / 4–5 |

Values are rounded for display; ranks are competition ranks (equal values share the better rank). The Plan rank is that of the configuration's own plan row (its selected route) in the Plan ranking of every plan below. Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 2.8 value points (median, 95%) to separate, and 0 of 8 adjacent API ranks and 1 of 9 adjacent Plan ranks of different configurations do (17 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 1 at correlation 0.3, 3 at correlation 0.6; Plan 2 at correlation 0.3, 2 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 14 Plan rows on an owner assumption (an owner-named transfer or an O46 quota ceiling), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (owner-named transfer or O46 quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 2.3 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise.

### Plan ranking: every plan (O48)

The Plan ranking has one row per configuration and subscription plan (owner decision O48): each plan on which the configuration has an admitted route, with that plan's route chosen by the official comparator; a configuration with no admitted route keeps one API-cost row. Rows of one configuration share its quality and API cost and differ only by the plan's Value Multiple. The table above shows each configuration's own plan row (its selected route).

| Plan rank | Configuration | Plan | Value Multiple | Plan cost (USD per basket run) | Plan value | Quality | Route evidence | Noise band |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | Claude Opus 5.5 (max) | Claude Pro | 58.9× | $158.77 | 64.3 | 67.9 | controlled | 1–10 |
| 2 | Claude Opus 5.5 (max) | Claude Max 20x | 58.63× | $159.50 | 64.3 | 67.9 | controlled | 1–10 |
| 3 | Claude Opus 5.5 (max) | Claude Max 5x | 57.25× | $163.35 | 64.2 | 67.9 | controlled | 1–10 |
| 4 | Claude Sonnet 5.5 (max) | Claude Pro | 58.9× | $151.63 | 63.8 | 67.1 | assumption | 1–10† |
| 5 | Claude Sonnet 5.5 (max) | Claude Max 20x | 58.63× | $152.33 | 63.8 | 67.1 | assumption | 1–10† |
| 6 | Claude Sonnet 5.5 (max) | Claude Max 5x | 57.25× | $156.00 | 63.7 | 67.1 | assumption | 1–10† |
| 7 | GPT-6.1 Sol (max) | ChatGPT Pro 500 | 10.772× | $114.47 | 62.7 | 64.3 | controlled | 1–10 |
| 8 | GPT-6.1 Sol (max) | ChatGPT Plus | 10.55× | $116.88 | 62.7 | 64.3 | controlled | 1–10 |
| 8 | GPT-6.1 Sol (max) | ChatGPT Pro 100 | 10.55× | $116.88 | 62.7 | 64.3 | controlled | 1–10 |
| 10 | GPT-6.1 Sol (max) | ChatGPT Pro 200 | 10.42× | $118.34 | 62.6 | 64.3 | controlled | 1–10 |
| 11 | Claude Haiku 5.5 (max) | Claude Pro | 58.9× | $16.42 | 59.8 | 51.3 | assumption | 11–20† |
| 12 | Claude Haiku 5.5 (max) | Claude Max 20x | 58.63× | $16.49 | 59.8 | 51.3 | assumption | 11–20† |
| 13 | Claude Haiku 5.5 (max) | Claude Max 5x | 57.25× | $16.89 | 59.7 | 51.3 | assumption | 11–20† |
| 14 | GPT-6 Astra (max) | ChatGPT Pro 200 | 14.485× | $406.29 | 58.8 | 65.0 | controlled | 11–20 |
| 15 | GPT-6 Astra (max) | ChatGPT Pro 500 | 13.91× | $423.08 | 58.7 | 65.0 | controlled | 11–20 |
| 16 | GPT-6 Astra (max) | ChatGPT Pro 100 | 13.22× | $445.16 | 58.5 | 65.0 | controlled | 11–20 |
| 17 | GPT-6 Luna (max) | ChatGPT Pro 500 | 10.772× | $11.67 | 58.1 | 47.4 | assumption | 11–20† |
| 18 | GPT-6 Luna (max) | ChatGPT Pro 100 | 10.55× | $11.92 | 58.0 | 47.4 | assumption | 11–20† |
| 19 | GPT-6 Luna (max) | ChatGPT Pro 200 | 10.42× | $12.07 | 58.0 | 47.4 | assumption | 11–20† |
| 20 | GPT-6 Luna (max) | ChatGPT Plus | 8.1× | $15.52 | 57.1 | 47.4 | assumption | 11–20† |
| 21 | GPT-6 Astra (max) | ChatGPT Plus | 8.1× | $726.55 | 56.8 | 65.0 | controlled | 21 |
| 22 | DeepSeek V4.1 Flash 1017 (max) | API-cost fallback (no admitted plan) | — | $410.04 | 53.7 | 58.2 | fallback | 22–26 |
| 23 | MiMo-V2.6-Pro | MiMo Token Plan Max | 1.1808× | $115.28 | 51.9 | 54.2 | assumption | 22–26† |
| 24 | MiMo-V2.6-Pro | MiMo Token Plan Pro | 1.0944× | $124.39 | 51.7 | 54.2 | assumption | 22–26† |
| 25 | MiMo-V2.6-Pro | MiMo Token Plan Standard | 0.99× | $137.50 | 51.3 | 54.2 | assumption | 22–26† |
| 26 | MiMo-V2.6-Pro | MiMo Token Plan Lite | 0.984× | $138.34 | 51.3 | 54.2 | assumption | 22–26† |
| 27 | Gemini 4 Argon (high) | API-cost fallback (no admitted plan) | — | $3,557.77 | 50.6 | 64.3 | fallback | 27 |

- **subset cost**: scored on the workload of the components it has, against that workload's own anchors; its ordering against main-workload rows is not identified (O17).
- **provider-claimed leaf**: a quality leaf comes from the model provider's own published result (O36's last source); the row competes but earns no interval label (E233).
- **provisional quality**: observed leaves cover under 70% of quality weight, fewer than two software-engineering leaves or under 40% software-engineering weight are observed, or a leaf weighing 20% or more of its ranking's quality is missing; ranked and flagged, never floored (O8).
- **partial component**: AA marks tasks of a basket component missing or declined (E37), or the component's cost cannot be reconciled with AA's prices (E170).
- **valuation basis unverified**: AA's cost reconciles with neither its displayed prices nor a registered price record; ranked, but outside interval outputs and cost anchors (E170 outcome 4).
- **no cost**: AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown.
- **AA cost caveat**: AA states that its published cost omits a pricing term.
- **API-cost fallback**: no admitted Plan route; the Plan ranking uses the API cost (O13).

Not ranked in the max-effort ranking (52 roster models): Claude Fable 5, Claude Fable 5.1, Claude Haiku 5.5, Claude Haiku 5.5 (high), Claude Haiku 5.5 (low), Claude Haiku 5.5 (medium), Claude Opus 4.8, Claude Opus 5, Claude Opus 5.5 (high), Claude Opus 5.5 (medium), Claude Opus 5.5 (xhigh), Claude Sonnet 5, Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (low), Claude Sonnet 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4 Flash, DeepSeek V4 Pro, GLM-5.2, GLM-5.3, GLM-5.3 Flash, GPT-5.5, GPT-5.6 Luna, GPT-5.6 Luna (low), GPT-5.6 Sol, GPT-6 Astra (high), GPT-6 Astra (xhigh), GPT-6 Luna (high), GPT-6 Luna (low), GPT-6 Luna (medium), GPT-6 Luna (xhigh), GPT-6 Sol, GPT-6.1 Sol (high), GPT-6.1 Sol (low), GPT-6.1 Sol (medium), GPT-6.1 Sol (xhigh), Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Gemini 3.8 Flash, Grok 4.6, Grok 4.6 (xhigh), Grok 4.7, Kimi K3, MiMo-V2.6-Flash, MiniMax-M3.1-Flash, Muse Spark 1.2, Muse Spark 1.3, Muse Spark 1.3 (xhigh), Muse Wonder, Muse Wonder Full, Qwen3.8 Max. Reasons are listed in [scores.md](scores.md#not-ranked). Of these, 20 qualify for the cohort but are listed, not ranked, because a benchmark is still missing after a logged search (O36, O38): GPT-6.1 Sol (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Opus 5.5 (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Opus 5.5 (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6.1 Sol (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Astra (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (high) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (medium) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-5.6 Luna (low) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (an AA frontier family; no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Haiku 5.5 (low) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Opus 5.5 (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); Claude Sonnet 5.5 (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Astra (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6 Luna (low) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); GPT-6.1 Sol (xhigh) (no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); MiMo-V2.6-Flash (an AA frontier family; no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall); MiniMax-M3.1-Flash (no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall).

**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| GPT-6.1 Sol (high) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 54.6 | 74% | 55.6 | 55.5 | $431.07 | $40.02 |
| Claude Opus 5.5 (high) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 57.7 | 74% | 58.7 | 51.4 | $1,860.17 | $31.58 |
| Claude Opus 5.5 (medium) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 56.5 | 74% | 58.6 | 51.7 | $1,423.70 | $24.17 |
| GPT-6.1 Sol (medium) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 51.8 | 74% | 54.5 | 54.8 | $318.05 | $29.53 |
| GPT-6 Astra (high) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 56.1 | 74% | 51.2 | 49.2 | $2,382.09 | $221.14 |
| Claude Haiku 5.5 (high) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 39.2 | 74% | 54.4 | 51.9 | $70.85 | $1.20 |
| GPT-6 Luna (xhigh) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 36.0 | 74% | 48.7 | 51.1 | $49.41 | $4.59 |
| Claude Haiku 5.5 (medium) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 35.2 | 74% | 51.4 | 50.8 | $45.91 | $0.78 |
| GPT-6 Luna (high) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 34.2 | 74% | 48.2 | 50.6 | $37.39 | $3.47 |
| GPT-6 Luna (medium) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 31.6 | 74% | 47.5 | 48.7 | $25.26 | $2.34 |
| GPT-5.6 Luna (low) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 20.5 | 74% | 39.8 | 40.4 | $20.71 | $1.92 |
| Claude Haiku 5.5 | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 42.2 | 74% | 56.3 | 52.4 | $107.10 | $1.82 |
| Claude Haiku 5.5 (low) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 30.0 | 74% | 47.5 | 47.5 | $28.12 | $0.48 |
| Claude Opus 5.5 (xhigh) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 60.0 | 74% | 58.5 | 50.6 | $3,374.80 | $57.30 |
| Claude Sonnet 5.5 (xhigh) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 55.5 | 74% | 57.1 | 49.9 | $1,826.03 | $31.00 |
| GPT-6 Astra (xhigh) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 58.0 | 74% | 52.0 | 49.8 | $2,899.42 | $269.16 |
| GPT-6 Luna (low) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 21.2 | 74% | 40.9 | 40.9 | $8.37 | $0.78 |
| GPT-6.1 Sol (xhigh) | Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 55.9 | 74% | 56.0 | 55.7 | $512.20 | $47.55 |
| MiMo-V2.6-Flash | Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 46.2 | 66% | 48.4 | 57.8 | $60.37 | $52.59 |
| MiniMax-M3.1-Flash | Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall | 49.2 | 66% | 45.8 | 54.2 | $234.35 | $234.35 |

### AI Coding Daily ranking

The configurations AI Coding Daily has tested, mostly at high and medium effort, scored on the AA leaves plus AI Coding Daily. Its leaves: FrontierCode 1.1 21%, Terminal-Bench 4.0 (AA run) 17%, Bug Hunt Bench 12%, AI Coding Daily (excl. bug finding) 10% (software engineering 60%), plus the 7 leaves outside software engineering every ranking shares. It ranks 15 configurations, each with every leaf for its exact configuration (O36); its cost anchors and quality bars are its own (anchor version `v3-2026-10-23-aicd`), so its values are not comparable with the max-effort ranking's. The interactive table is at [valuerank.alolabs.dev/rankings/ai-coding-daily/](https://valuerank.alolabs.dev/rankings/ai-coding-daily/).

| Plan rank | API rank | Configuration | Plan value | API value | Quality | Quality coverage | API cost (USD per basket run) | Plan cost (USD per basket run) | Plan route | Flags | Noise band (Plan / API) |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | 6 | [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 58.1 | 48.9 | 60.1 | 100% | $1,860.17 | $31.58 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–11† / 1–8 |
| 4 | 5 | [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 58.0 | 49.2 | 59.0 | 100% | $1,423.70 | $24.17 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–11† / 1–8 |
| 7 | 1 | [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 55.2 | 52.7 | 57.2 | 100% | $431.07 | $40.02 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 1–11† / 1–8 |
| 11 | 2 | [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 53.8 | 51.7 | 54.2 | 100% | $318.05 | $29.53 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 1–11† / 1–8 |
| 14 | 7 | [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 53.5 | 48.8 | 42.1 | 100% | $70.85 | $1.20 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 12–24† / 1–8 |
| 18 | 10 | [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 51.9 | 47.7 | 38.4 | 100% | $45.91 | $0.78 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 12–24† / 9–14 |
| 21 | 12 | [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 51.6 | 46.8 | 58.6 | 100% | $2,382.09 | $221.14 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 12–24† / 9–14 |
| 25 | 8 | [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 49.0 | 48.8 | 42.8 | 100% | $79.56 | $7.39 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 25–42† / 1–8 |
| 29 | 11 | [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 46.8 | 47.1 | 38.0 | 100% | $49.41 | $4.59 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 25–42† / 9–14 |
| 32 | 3 | [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 46.4 | 51.4 | 49.2 | 100% | $136.13 | $115.28 | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | — | 25–42† / 1–8 |
| 33 | 4 | [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 46.3 | 50.6 | 52.8 | 100% | $324.12 | $324.12 | — | API-cost fallback | 25–42 / 1–8 |
| 37 | 9 | [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 45.9 | 47.9 | 58.7 | 100% | $1,857.94 | $1,857.94 | — | API-cost fallback | 25–42 / 9–14 |
| 39 | 13 | [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 45.9 | 46.6 | 35.8 | 100% | $37.39 | $3.47 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 25–42† / 9–14 |
| 43 | 14 | [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 44.3 | 45.6 | 32.3 | 100% | $25.26 | $2.34 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 43–46† / 9–14 |
| 47 | 15 | [GPT-5.6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-5-6-luna-low/) | 36.6 | 38.2 | 21.3 | 100% | $20.71 | $1.92 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 47–50† / 15 |

Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 4.4 value points (median, 95%) to separate, and 1 of 14 adjacent API ranks and 1 of 19 adjacent Plan ranks of different configurations do (30 more adjacent Plan pairs are one configuration on two plans, ordered by the plans' multiples alone; E258). Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 1 at correlation 0.3, 1 at correlation 0.6; Plan 1 at correlation 0.3, 1 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 48 Plan rows on an owner assumption (an owner-named transfer or an O46 quota ceiling), that assumption's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner assumption (owner-named transfer or O46 quota ceiling) and excludes its error: an assumed multiple can be wrong by a factor of about 5.3 before the row's value moves by the median threshold (a tolerance, not an estimate of the assumption's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise. AI Coding Daily's noise treats its six graded projects as six trials of the share of 60 points (n = 6, the wide reading, E263); read as 60 trials, the median threshold would be 3.2 (API) and 3.2 (Plan), with 1 and 1 adjacent ranks separable.

Cohort configurations without this ranking's full set (14): Claude Haiku 5.5, Claude Haiku 5.5 (low), Claude Haiku 5.5 (max), Claude Opus 5.5, Claude Opus 5.5 (xhigh), Claude Sonnet 5.5, Claude Sonnet 5.5 (xhigh), GPT-6 Astra, GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol, GPT-6.1 Sol (xhigh), MiMo-V2.6-Flash, MiniMax-M3.1-Flash.

### What the evidence supports

- API basis, main workload: the definite frontier (no configuration can beat it on both cost and quality anywhere inside the published record's precision and missing-evidence bounds) is Claude Sonnet 5.5 (max), DeepSeek V4.1 Flash 1017 (max), Claude Opus 5.5 (max), GPT-6.1 Sol (max), GPT-6 Astra (max), GPT-6 Luna (max); the possible frontier adds none. Not evaluable on this workload: MiMo-V2.6-Pro. Cheapest at or above quality 64.3: GPT-6.1 Sol (max) (confirmed). (Bar comparison: compares 5 configurations that can qualify.) Cheapest at or above quality 54.2: DeepSeek V4.1 Flash 1017 (max) (confirmed). (Bar comparison: compares 6 configurations that can qualify.) Cheapest at or above quality 65.0: not unique; possibly Claude Sonnet 5.5 (max), GPT-6 Astra (max). (Bar comparison: compares 3 configurations that can qualify.)
- Plan basis: interval outputs not evaluated (no row has FullCost and an identified M_W (E61/E67)).
- API basis, displayed record (not a claim; E203): cheapest at or above quality 64.3: GPT-6.1 Sol (max) ($1,233.11 per basket run; 5 reach it); at or above quality 54.2: DeepSeek V4.1 Flash 1017 (max) ($410.04 per basket run; 6 reach it); at or above quality 65.0: GPT-6 Astra (max) ($5,885.05 per basket run; 3 reach it).
- API basis, noise-margin companion (O44; each bar plus 3.8 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 68.1: none; at or above quality 58.0: DeepSeek V4.1 Flash 1017 (max) ($410.04 per basket run); at or above quality 68.8: none.
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 64.3: GPT-6.1 Sol (max) on ChatGPT Pro 500 ($114.47 per basket run; 15 reach it); at or above quality 54.2: GPT-6.1 Sol (max) on ChatGPT Pro 500 ($114.47 per basket run; 16 reach it); at or above quality 65.0: Claude Sonnet 5.5 (max) on Claude Pro ($151.63 per basket run; 10 reach it).
- Plan basis, noise-margin companion (O44; each bar plus 3.8 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 68.1: none; at or above quality 58.0: GPT-6.1 Sol (max) on ChatGPT Pro 500 ($114.47 per basket run); at or above quality 68.8: none.
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): GPT-6.1 Sol (high), Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Sol (medium), GPT-6 Astra (high), Claude Haiku 5.5 (high), GPT-6 Luna (xhigh), Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-5.6 Luna (low), Claude Haiku 5.5, Claude Haiku 5.5 (low), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh), MiMo-V2.6-Flash, MiniMax-M3.1-Flash.

Scenario shares by stream, diagnostics and the release gates are in [scores.md](scores.md); the inputs behind every number are in [raw-data.md](raw-data.md).

## Model inclusion

**Frontier rule.** Every model family on the Pareto frontier that Artificial Analysis (AA) renders on its Intelligence Index versus total cost to run chart is ranked at its highest point on that line (along the strictly rising line also its dearest). Frontier membership is AA's rendered line as observed; ValueRank never recomputes it from rounded values.

**Near-frontier rule.** A plotted configuration is near-frontier when its public (rounded integer) Intelligence Index is within 3 points of the rendered frontier's Index at its cost, meaning the highest Index among rendered-frontier points that cost no more. Every near-frontier family is ranked or is explicitly deferred by a dated, reasoned roster decision. Every configuration AA plots on the frontier or within the gap is a cohort row (O51); a near family's primary configuration is its near point with the smallest Index gap. The cost ratio to the frontier is reported for information only.

Policy as recorded: A plotted configuration is near-frontier when it lies within 3 Intelligence Index points of the rendered frontier at its cost. Every near-frontier model family must be in the primary ranking, with its own selected configuration, or be explicitly deferred with a dated, reasoned roster decision. The cost ratio to the cheapest frontier point of equal or higher intelligence is reported for information only.

Chart observed 2026-10-23T05:27:39Z (Intelligence Index v4.3.2): 697 catalog models selected, 189 plotted points and 18 rendered Pareto vertices across 7 families. 11 plotted points across 8 families are near-frontier.

Near-frontier models: 8 required, 0 deferred by roster decision.

Frontier families and the configuration selected for each:

- Claude Haiku 5.5: Claude Haiku 5.5 (xhigh)
- Claude Opus 5.5: Claude Opus 5.5 (max with fallback)
- Claude Sonnet 5.5: Claude Sonnet 5.5 (max with fallback)
- GPT-6 Luna: GPT-6 Luna (max)
- GPT-6.1 Sol: GPT-6.1 Sol (max)
- MiMo-V2.6-Flash: MiMo-V2.6-Flash
- MiMo-V2.6-Pro: MiMo-V2.6-Pro

Near-frontier families and each family's near point closest to the frontier (every configuration AA plots on or near the frontier is a cohort row, each effort its own row, O51; a family's primary configuration is its near point closest to the frontier, E193):

- Claude Haiku 5.5: Claude Haiku 5.5 (low), 1 Index point below the frontier
- Claude Opus 5.5: Claude Opus 5.5 (medium with fallback), 1 Index point below the frontier
- Claude Sonnet 5.5: Claude Sonnet 5.5 (xhigh with fallback), 2 Index points below the frontier
- DeepSeek V4.1 Flash 1017: DeepSeek V4.1 Flash 1017 (max), 3 Index points below the frontier
- GPT-5.6 Luna: GPT-5.6 Luna (low), 1 Index point below the frontier
- GPT-6 Astra: GPT-6 Astra (xhigh), 2 Index points below the frontier
- Gemini 4 Argon: Gemini 4 Argon (high), 1 Index point below the frontier
- MiniMax-M3.1-Flash: MiniMax-M3.1-Flash, 3 Index points below the frontier

AA footnote (Claude Haiku 5.5 (max), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (low)): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## How v3 scores value

- **Cost is the SDLC basket.** SDLC basket v1: AA's published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, in USD per basket run. Pending capture: ITBench-AA. v2 used AA's cost to run the whole Intelligence Index per Index point.
- **Cost keeps its magnitude.** The cost score is 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100, against anchors frozen with anchor version `v3-2026-10-23`. A model entering or leaving the cohort does not move another model's score. At the API anchors, doubling cost costs 3.04 value points, which 4.06 quality points offset.
- **Quality is measured, not ranked.** Each leaf (13 in the max-effort ranking) is placed on fixed 0–100 anchors from its raw value, so quality no longer depends on which other models are ranked. Only configurations with every leaf are ranked (O36), so all ranked rows are scored on the same benchmarks; each leaf filled from another party or a provider is listed in [raw-data.md](raw-data.md#leaf-gap-fills-and-searches-o36).
- **Plan value is route evidence.** Each subscription route carries its Value Multiple, evidence grade (controlled measurement, concordant reports, owner-named assumption) and identification status; the Plan ranking is labelled exploratory until multiples are identified on the basket.
- **Uncertainty is shown, not hidden.** Interval outputs certify which frontier and cheapest-above-a-bar claims the published record supports; scenario shares report frequencies over declared streams.
- v3 values are not numerically comparable with v2 or earlier releases.

## Sources and audit trail

- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and its model pages: Intelligence Index component scores and the per-task evaluation costs of the basket.
- [AA Coding Agent Index v2.0](https://artificialanalysis.ai/agents/coding-agents): the Coding Agent Index cost (FrontierCode, Terminal-Bench and SWE-Atlas-QnA-AA) for each exact configuration (O50); AA withdrew DeepSWE v1.1 in October 2026 and it is no longer a leaf (O49).
- AA's own Terminal-Bench 4.0 run (the leaf; [tbench.ai](https://www.tbench.ai/leaderboard/terminal-bench/4.0) rows fill a gap and serve as a cross-check, O37), [Bug Hunt Bench](https://bughunt.productcompass.pm/) owner-published runs, [Cognition's FrontierCode leaderboard](https://cognition.com/data/frontiercode-leaderboard/data.json) and model-provider results for leaves AA has not run (O36).
- [SemiAnalysis subscription measurements](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (owner-selected 2026-10-07) for the Claude and ChatGPT plan Value Multiples; owner-named transfers are labelled as assumptions.
- The evidence bundle in `data/scores.json` lists every input artifact with its SHA-256; bundle hash `52bd888352339da35c4799b554f736f5acdf1f84539a486dd62a46f6b8d831e7`.
- [Methodology co-design record](research/2026-10-19-methodology-codesign/): the reviewed specification, every owner and editor decision, and each reviewer's findings.

## Files

- [methodology.md](methodology.md): how value, cost, quality, the Plan basis and the uncertainty outputs are computed
- [scores.md](scores.md): rankings, leaf scores, basket costs, Plan routes, interval outputs, scenario shares, diagnostics and release gates
- [raw-data.md](raw-data.md): every leaf input with its evidence locator, component costs, benchmark source tables, Plan routes and the evidence bundle
- [https://valuerank.alolabs.dev/](https://valuerank.alolabs.dev/): website, generated by `valuerank.site.build` (source under [valuerank/site/](valuerank/site/))
- [https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/](https://valuerank.alolabs.dev/benchmarks/terminal-bench-4/): current Terminal-Bench 4.0 score-versus-cost page
- [data/](data/): machine-readable snapshots and generated outputs (pipeline code lives in [valuerank/](valuerank/))
- [docs/](docs/README.md): contributor documentation (repository layout, architecture, development, testing, refresh and release); `npm run verify` runs every check


## AA intelligence and total-cost comparison

Observed 2026-10-23T05:27:39Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 697 catalog models selected; 189 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 697 models, plotted 189 eligible points, and displayed 18 frontier points. Public metric/export gaps are shown explicitly. All 7 distinct frontier model families are required in the main ranking using exact selected configurations; 5 are included. Other effort configurations remain separate comparison entries. 11 plotted configurations from 8 families lie within 3 Index points of the rendered frontier; 5 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | $10.63 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | $31.17 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | $47.85 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 34 (rounded) | $56.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 38 (rounded) | $94.07 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.55 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 41 (rounded) | $157.58 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 56 (rounded) | $7,259.50 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |
| [GPT-5.6 Luna (low)](https://artificialanalysis.ai/models/gpt-5-6-luna-low) | gpt-5-6-luna-low | 21 (rounded) | $27.02 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 29 (rounded) | $34.31 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [MiniMax-M3.1-Flash](https://artificialanalysis.ai/models/minimax-m3-1-flash) | minimax-m3-1-flash | 43 (rounded) | $283.18 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| [Claude Haiku 5.5 (max)](https://artificialanalysis.ai/models/claude-haiku-5-5) | claude-haiku-5-5 | 43 (rounded) | $330.25 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [DeepSeek V4.1 Flash 1017 (max)](https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017) | deepseek-v4-1-flash-1017 | 45 (rounded) | $444.60 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (medium with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-medium) | claude-opus-5-5-medium | 51 (rounded) | $1,626.81 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Sonnet 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh) | claude-sonnet-5-5-xhigh | 52 (rounded) | $2,176.82 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Gemini 4 Argon (high)](https://artificialanalysis.ai/models/gemini-4-argon) | gemini-4-argon | 53 (rounded) | $2,407.24 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 51 (rounded) | $2,925.01 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 52 (rounded) | $3,802.98 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 53 (rounded) | $5,324.10 | Near AA frontier (within 3 Index points) | Primary ranked | None |
