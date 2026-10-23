# ValueRank
**Frontier AI configurations ranked by value for software engineering and DevOps: benchmark quality against what the work costs**

**Version:** v3.0.0
**Updated:** October 19, 2026
**Methodology:** 3.0.0 · SDLC basket v1 · anchor version v3-2026-10-23
**Scope:** 27 cohort configurations (27 with a value score) from a 61-model AA-mapped roster; value is a 25% cost score (nominal weight; -108% of API and -45% of Plan value variance) plus 75% quality over 10 benchmark leaves

## Current result

ValueRank ranks frontier AI model configurations (see Model inclusion) by value for software engineering and DevOps work, separately for API buyers and for subscription (Plan) buyers. Value is a fixed **25%** cost score plus **75%** benchmark quality. That weight is nominal: on the current panel cost's covariance allocation of value variance is -108% on the API basis and -45% on the Plan basis; a negative allocation means dearer configurations score higher on quality, so cost offsets quality differences instead of adding spread of its own (see [methodology.md](methodology.md)). Cost is the contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost): Artificial Analysis' (AA) published cost of running the AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, scored on a log scale against frozen anchors so cost ratios keep their size. Coding and terminal tasks (Coding Agent Index, Terminal-Bench 4.0 (AA Index run), SciCode) make up 19% of the basket's cost (median over 27 configurations with the full basket; 6% to 31%); AA-Briefcase, GDP.pdf, which have no quality leaf, make up 27%; the Coding Agent Index's SWE-Atlas QnA (124 of its 290 tasks) has no quality leaf either, and its cost share is not separable because AA publishes one pooled cost. Quality is the weighted mean of 10 benchmark leaves on fixed 0–100 anchors, and every ranked configuration has all 10 for its exact configuration (O36): a leaf AA has not run comes from another party's run of the same benchmark, then from the model provider's published result, and a configuration still missing one after a logged exhaustive search is listed, not ranked. The Plan ranking divides the basket's API cost by a subscription route's Value Multiple at full utilisation, with one row per configuration and plan (O48), and uses the API cost, flagged, when no route is admitted. No Value Multiple is yet identified on the basket itself (0 of 91 rows), so the Plan ranking is labelled exploratory.

Claude Opus 5.5 (xhigh) leads the Plan ranking at 54.0 (owner-named transfer); GPT-6.1 Sol (xhigh) leads the API ranking at 50.2; Claude Opus 5.5 leads on quality.

| Plan rank | API rank | Configuration | Plan value | API value | Quality | Quality coverage | API cost (USD per basket run) | Plan cost (USD per basket run) | Plan route | Flags | Noise band (Plan / API) |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | 9 | [Claude Opus 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-opus-5-5-xhigh/) | 54.0 | 47.1 | 57.5 | 100% | $3,374.80 | $57.30 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–30† / 1–13 |
| 4 | 8 | [Claude Opus 5.5 (high)](https://valuerank.alolabs.dev/models/claude-opus-5-5-high/) | 53.8 | 47.3 | 55.3 | 100% | $1,860.17 | $31.58 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–30† / 1–13 |
| 7 | 7 | [Claude Opus 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-opus-5-5-medium/) | 53.7 | 47.4 | 54.2 | 100% | $1,423.70 | $24.17 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–30† / 1–13 |
| 9 | 12 | [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 53.7 | 46.7 | 58.6 | 100% | $5,073.84 | $86.14 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–30† / 1–13 |
| 13 | 13 | [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 53.5 | 46.4 | 58.9 | 100% | $6,039.13 | $102.53 | Claude Pro $20 · Opus 5.5 (58.9×, measured) | — | 1–30 / 1–13 |
| 16 | 14 | [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 52.3 | 45.9 | 53.2 | 100% | $1,826.03 | $31.00 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–30† / 14–20 |
| 19 | 2 | [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 51.6 | 50.0 | 55.3 | 100% | $796.76 | $73.97 | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | — | 1–30 / 1–13 |
| 22 | 1 | [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 51.5 | 50.2 | 53.7 | 100% | $512.20 | $47.55 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 1–30† / 1–13 |
| 26 | 3 | [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 50.8 | 49.6 | 52.1 | 100% | $431.07 | $40.02 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 1–30† / 1–13 |
| 31 | 17 | [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 49.5 | 44.6 | 39.7 | 100% | $107.10 | $1.82 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 31–58† / 14–20 |
| 34 | 4 | [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 49.2 | 48.1 | 48.9 | 100% | $318.05 | $29.53 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 31–58† / 1–13 |
| 37 | 11 | [GPT-6 Astra (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-astra-xhigh/) | 49.0 | 46.7 | 56.2 | 100% | $2,899.42 | $269.16 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 31–58† / 1–13 |
| 40 | 18 | [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 48.9 | 43.6 | 40.9 | 100% | $191.49 | $3.25 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 31–58† / 14–20 |
| 43 | 16 | [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 48.7 | 45.4 | 55.8 | 100% | $3,844.56 | $265.42 | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | — | 31–58 / 14–20 |
| 48 | 19 | [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 48.1 | 43.4 | 36.4 | 100% | $70.85 | $1.20 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 31–58† / 14–20 |
| 51 | 15 | [GPT-6 Astra (high)](https://valuerank.alolabs.dev/models/gpt-6-astra-high/) | 47.7 | 45.4 | 53.8 | 100% | $2,382.09 | $221.14 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 31–58† / 14–20 |
| 56 | 21 | [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 46.1 | 41.7 | 32.3 | 100% | $45.91 | $0.78 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 31–58† / 21–25 |
| 59 | 20 | [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 43.6 | 43.3 | 36.7 | 100% | $79.56 | $7.39 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 59–74† / 14–20 |
| 62 | 25 | [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 43.5 | 39.3 | 27.0 | 100% | $28.12 | $0.48 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 59–74† / 21–25 |
| 65 | 10 | [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 43.0 | 47.1 | 55.0 | 100% | $1,857.94 | $1,857.94 | — | API-cost fallback | 59–74 / 1–13 |
| 67 | 5 | [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 42.5 | 47.6 | 44.7 | 100% | $136.13 | $115.28 | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | — | 59–74† / 1–13 |
| 68 | 6 | [DeepSeek V4.1 Flash 1017 (max)](https://valuerank.alolabs.dev/models/deepseek-v4-1-flash-1017/) | 42.4 | 47.4 | 48.1 | 100% | $324.12 | $324.12 | — | API-cost fallback | 59–74 / 1–13 |
| 72 | 22 | [GPT-6 Luna (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-luna-xhigh/) | 41.1 | 41.0 | 31.6 | 100% | $49.41 | $4.59 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 59–74† / 21–25 |
| 76 | 23 | [GPT-6 Luna (high)](https://valuerank.alolabs.dev/models/gpt-6-luna-high/) | 40.2 | 40.3 | 29.5 | 100% | $37.39 | $3.47 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 75–83† / 21–25 |
| 80 | 24 | [GPT-6 Luna (medium)](https://valuerank.alolabs.dev/models/gpt-6-luna-medium/) | 39.4 | 39.6 | 27.0 | 100% | $25.26 | $2.34 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 75–83† / 21–25 |
| 84 | 26 | [GPT-6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-6-luna-low/) | 34.9 | 35.8 | 17.3 | 100% | $8.37 | $0.78 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 84–87† / 26 |
| 88 | 27 | [GPT-5.6 Luna (low)](https://valuerank.alolabs.dev/models/gpt-5-6-luna-low/) | 32.3 | 32.7 | 17.0 | 100% | $20.71 | $1.92 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 88–91† / 27 |

Values are rounded for display; ranks are competition ranks (equal values share the better rank). The Plan rank is that of the configuration's own plan row (its selected route) in the Plan ranking of every plan below. Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 3.9 value points (median, 95%) to separate, and 2 of 26 adjacent API ranks and 51 of 90 adjacent Plan ranks do. Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 2 at correlation 0.3, 2 at correlation 0.6; Plan 52 at correlation 0.3, 53 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 78 Plan rows on owner-named transfers, the transfer's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner-named transfer and excludes its error: a transferred multiple can be wrong by a factor of about 1.0 before the row's value moves by the median threshold (a tolerance, not an estimate of the transfer's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise.

### Plan ranking: every plan (O48)

The Plan ranking has one row per configuration and subscription plan (owner decision O48): each plan on which the configuration has an admitted route, with that plan's route chosen by the official comparator; a configuration with no admitted route keeps one API-cost row. Rows of one configuration share its quality and API cost and differ only by the plan's Value Multiple. The table above shows each configuration's own plan row (its selected route).

| Plan rank | Configuration | Plan | Value Multiple | Plan cost (USD per basket run) | Plan value | Quality | Route evidence | Noise band |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | Claude Opus 5.5 (xhigh) | Claude Pro | 58.9× | $57.30 | 54.0 | 57.5 | assumption | 1–30† |
| 2 | Claude Opus 5.5 (xhigh) | Claude Max 20x | 58.63× | $57.56 | 53.9 | 57.5 | assumption | 1–30† |
| 3 | Claude Opus 5.5 (xhigh) | Claude Max 5x | 57.25× | $58.95 | 53.9 | 57.5 | assumption | 1–30† |
| 4 | Claude Opus 5.5 (high) | Claude Pro | 58.9× | $31.58 | 53.8 | 55.3 | assumption | 1–30† |
| 5 | Claude Opus 5.5 (high) | Claude Max 20x | 58.63× | $31.73 | 53.8 | 55.3 | assumption | 1–30† |
| 6 | Claude Opus 5.5 (high) | Claude Max 5x | 57.25× | $32.49 | 53.7 | 55.3 | assumption | 1–30† |
| 7 | Claude Opus 5.5 (medium) | Claude Pro | 58.9× | $24.17 | 53.7 | 54.2 | assumption | 1–30† |
| 8 | Claude Opus 5.5 (medium) | Claude Max 20x | 58.63× | $24.28 | 53.7 | 54.2 | assumption | 1–30† |
| 9 | Claude Sonnet 5.5 (max) | Claude Pro | 58.9× | $86.14 | 53.7 | 58.6 | assumption | 1–30† |
| 10 | Claude Sonnet 5.5 (max) | Claude Max 20x | 58.63× | $86.54 | 53.7 | 58.6 | assumption | 1–30† |
| 11 | Claude Opus 5.5 (medium) | Claude Max 5x | 57.25× | $24.87 | 53.6 | 54.2 | assumption | 1–30† |
| 12 | Claude Sonnet 5.5 (max) | Claude Max 5x | 57.25× | $88.63 | 53.6 | 58.6 | assumption | 1–30† |
| 13 | Claude Opus 5.5 (max) | Claude Pro | 58.9× | $102.53 | 53.5 | 58.9 | controlled | 1–30 |
| 14 | Claude Opus 5.5 (max) | Claude Max 20x | 58.63× | $103.00 | 53.5 | 58.9 | controlled | 1–30 |
| 15 | Claude Opus 5.5 (max) | Claude Max 5x | 57.25× | $105.49 | 53.4 | 58.9 | controlled | 1–30 |
| 16 | Claude Sonnet 5.5 (xhigh) | Claude Pro | 58.9× | $31.00 | 52.3 | 53.2 | assumption | 1–30† |
| 17 | Claude Sonnet 5.5 (xhigh) | Claude Max 20x | 58.63× | $31.14 | 52.3 | 53.2 | assumption | 1–30† |
| 18 | Claude Sonnet 5.5 (xhigh) | Claude Max 5x | 57.25× | $31.90 | 52.3 | 53.2 | assumption | 1–30† |
| 19 | GPT-6.1 Sol (max) | ChatGPT Pro 500 | 10.772× | $73.97 | 51.6 | 55.3 | controlled | 1–30 |
| 20 | GPT-6.1 Sol (max) | ChatGPT Plus | 10.55× | $75.52 | 51.6 | 55.3 | controlled | 1–30 |
| 20 | GPT-6.1 Sol (max) | ChatGPT Pro 100 | 10.55× | $75.52 | 51.6 | 55.3 | controlled | 1–30 |
| 22 | GPT-6.1 Sol (xhigh) | ChatGPT Pro 500 | 10.772× | $47.55 | 51.5 | 53.7 | assumption | 1–30† |
| 23 | GPT-6.1 Sol (max) | ChatGPT Pro 200 | 10.42× | $76.46 | 51.5 | 55.3 | controlled | 1–30 |
| 24 | GPT-6.1 Sol (xhigh) | ChatGPT Pro 100 | 10.55× | $48.55 | 51.5 | 53.7 | assumption | 1–30† |
| 25 | GPT-6.1 Sol (xhigh) | ChatGPT Pro 200 | 10.42× | $49.16 | 51.5 | 53.7 | assumption | 1–30† |
| 26 | GPT-6.1 Sol (high) | ChatGPT Pro 500 | 10.772× | $40.02 | 50.8 | 52.1 | assumption | 1–30† |
| 27 | GPT-6.1 Sol (xhigh) | ChatGPT Plus | 8.1× | $63.23 | 50.8 | 53.7 | assumption | 1–30† |
| 28 | GPT-6.1 Sol (high) | ChatGPT Pro 100 | 10.55× | $40.86 | 50.8 | 52.1 | assumption | 1–30† |
| 29 | GPT-6.1 Sol (high) | ChatGPT Pro 200 | 10.42× | $41.37 | 50.8 | 52.1 | assumption | 1–30† |
| 30 | GPT-6.1 Sol (high) | ChatGPT Plus | 8.1× | $53.22 | 50.1 | 52.1 | assumption | 1–30† |
| 31 | Claude Haiku 5.5 (xhigh) | Claude Pro | 58.9× | $1.82 | 49.5 | 39.7 | assumption | 31–58† |
| 32 | Claude Haiku 5.5 (xhigh) | Claude Max 20x | 58.63× | $1.83 | 49.5 | 39.7 | assumption | 31–58† |
| 33 | Claude Haiku 5.5 (xhigh) | Claude Max 5x | 57.25× | $1.87 | 49.4 | 39.7 | assumption | 31–58† |
| 34 | GPT-6.1 Sol (medium) | ChatGPT Pro 500 | 10.772× | $29.53 | 49.2 | 48.9 | assumption | 31–58† |
| 35 | GPT-6.1 Sol (medium) | ChatGPT Pro 100 | 10.55× | $30.15 | 49.2 | 48.9 | assumption | 31–58† |
| 36 | GPT-6.1 Sol (medium) | ChatGPT Pro 200 | 10.42× | $30.52 | 49.1 | 48.9 | assumption | 31–58† |
| 37 | GPT-6 Astra (xhigh) | ChatGPT Pro 500 | 10.772× | $269.16 | 49.0 | 56.2 | assumption | 31–58† |
| 38 | GPT-6 Astra (xhigh) | ChatGPT Pro 100 | 10.55× | $274.83 | 48.9 | 56.2 | assumption | 31–58† |
| 39 | GPT-6 Astra (xhigh) | ChatGPT Pro 200 | 10.42× | $278.26 | 48.9 | 56.2 | assumption | 31–58† |
| 40 | Claude Haiku 5.5 (max) | Claude Pro | 58.9× | $3.25 | 48.9 | 40.9 | assumption | 31–58† |
| 41 | Claude Haiku 5.5 (max) | Claude Max 20x | 58.63× | $3.27 | 48.9 | 40.9 | assumption | 31–58† |
| 42 | Claude Haiku 5.5 (max) | Claude Max 5x | 57.25× | $3.34 | 48.8 | 40.9 | assumption | 31–58† |
| 43 | GPT-6 Astra (max) | ChatGPT Pro 200 | 14.485× | $265.42 | 48.7 | 55.8 | controlled | 31–58 |
| 44 | GPT-6 Astra (max) | ChatGPT Pro 500 | 13.91× | $276.39 | 48.6 | 55.8 | controlled | 31–58 |
| 45 | GPT-6.1 Sol (medium) | ChatGPT Plus | 8.1× | $39.26 | 48.5 | 48.9 | assumption | 31–58† |
| 46 | GPT-6 Astra (max) | ChatGPT Pro 100 | 13.22× | $290.81 | 48.4 | 55.8 | controlled | 31–58 |
| 47 | GPT-6 Astra (xhigh) | ChatGPT Plus | 8.1× | $357.95 | 48.2 | 56.2 | assumption | 31–58† |
| 48 | Claude Haiku 5.5 (high) | Claude Pro | 58.9× | $1.20 | 48.1 | 36.4 | assumption | 31–58† |
| 49 | Claude Haiku 5.5 (high) | Claude Max 20x | 58.63× | $1.21 | 48.1 | 36.4 | assumption | 31–58† |
| 50 | Claude Haiku 5.5 (high) | Claude Max 5x | 57.25× | $1.24 | 48.0 | 36.4 | assumption | 31–58† |
| 51 | GPT-6 Astra (high) | ChatGPT Pro 500 | 10.772× | $221.14 | 47.7 | 53.8 | assumption | 31–58† |
| 52 | GPT-6 Astra (high) | ChatGPT Pro 100 | 10.55× | $225.79 | 47.6 | 53.8 | assumption | 31–58† |
| 53 | GPT-6 Astra (high) | ChatGPT Pro 200 | 10.42× | $228.61 | 47.6 | 53.8 | assumption | 31–58† |
| 54 | GPT-6 Astra (max) | ChatGPT Plus | 8.1× | $474.64 | 47.2 | 55.8 | controlled | 31–58 |
| 55 | GPT-6 Astra (high) | ChatGPT Plus | 8.1× | $294.09 | 46.9 | 53.8 | assumption | 31–58† |
| 56 | Claude Haiku 5.5 (medium) | Claude Pro | 58.9× | $0.78 | 46.1 | 32.3 | assumption | 31–58† |
| 57 | Claude Haiku 5.5 (medium) | Claude Max 20x | 58.63× | $0.78 | 46.1 | 32.3 | assumption | 31–58† |
| 58 | Claude Haiku 5.5 (medium) | Claude Max 5x | 57.25× | $0.80 | 46.1 | 32.3 | assumption | 31–58† |
| 59 | GPT-6 Luna (max) | ChatGPT Pro 500 | 10.772× | $7.39 | 43.6 | 36.7 | assumption | 59–74† |
| 60 | GPT-6 Luna (max) | ChatGPT Pro 100 | 10.55× | $7.54 | 43.6 | 36.7 | assumption | 59–74† |
| 61 | GPT-6 Luna (max) | ChatGPT Pro 200 | 10.42× | $7.64 | 43.5 | 36.7 | assumption | 59–74† |
| 62 | Claude Haiku 5.5 (low) | Claude Pro | 58.9× | $0.48 | 43.5 | 27.0 | assumption | 59–74† |
| 63 | Claude Haiku 5.5 (low) | Claude Max 20x | 58.63× | $0.48 | 43.4 | 27.0 | assumption | 59–74† |
| 64 | Claude Haiku 5.5 (low) | Claude Max 5x | 57.25× | $0.49 | 43.4 | 27.0 | assumption | 59–74† |
| 65 | Gemini 4 Argon (high) | API-cost fallback (no admitted plan) | — | $1,857.94 | 43.0 | 55.0 | fallback | 59–74 |
| 66 | GPT-6 Luna (max) | ChatGPT Plus | 8.1× | $9.82 | 42.9 | 36.7 | assumption | 59–74† |
| 67 | MiMo-V2.6-Pro | MiMo Token Plan Max | 1.1808× | $115.28 | 42.5 | 44.7 | assumption | 59–74† |
| 68 | DeepSeek V4.1 Flash 1017 (max) | API-cost fallback (no admitted plan) | — | $324.12 | 42.4 | 48.1 | fallback | 59–74 |
| 69 | MiMo-V2.6-Pro | MiMo Token Plan Pro | 1.0944× | $124.39 | 42.3 | 44.7 | assumption | 59–74† |
| 70 | MiMo-V2.6-Pro | MiMo Token Plan Standard | 0.99× | $137.50 | 42.1 | 44.7 | assumption | 59–74† |
| 71 | MiMo-V2.6-Pro | MiMo Token Plan Lite | 0.984× | $138.34 | 42.0 | 44.7 | assumption | 59–74† |
| 72 | GPT-6 Luna (xhigh) | ChatGPT Pro 500 | 10.772× | $4.59 | 41.1 | 31.6 | assumption | 59–74† |
| 73 | GPT-6 Luna (xhigh) | ChatGPT Pro 100 | 10.55× | $4.68 | 41.0 | 31.6 | assumption | 59–74† |
| 74 | GPT-6 Luna (xhigh) | ChatGPT Pro 200 | 10.42× | $4.74 | 41.0 | 31.6 | assumption | 59–74† |
| 75 | GPT-6 Luna (xhigh) | ChatGPT Plus | 8.1× | $6.10 | 40.3 | 31.6 | assumption | 75–83† |
| 76 | GPT-6 Luna (high) | ChatGPT Pro 500 | 10.772× | $3.47 | 40.2 | 29.5 | assumption | 75–83† |
| 77 | GPT-6 Luna (high) | ChatGPT Pro 100 | 10.55× | $3.54 | 40.2 | 29.5 | assumption | 75–83† |
| 78 | GPT-6 Luna (high) | ChatGPT Pro 200 | 10.42× | $3.59 | 40.1 | 29.5 | assumption | 75–83† |
| 79 | GPT-6 Luna (high) | ChatGPT Plus | 8.1× | $4.62 | 39.5 | 29.5 | assumption | 75–83† |
| 80 | GPT-6 Luna (medium) | ChatGPT Pro 500 | 10.772× | $2.34 | 39.4 | 27.0 | assumption | 75–83† |
| 81 | GPT-6 Luna (medium) | ChatGPT Pro 100 | 10.55× | $2.39 | 39.3 | 27.0 | assumption | 75–83† |
| 82 | GPT-6 Luna (medium) | ChatGPT Pro 200 | 10.42× | $2.42 | 39.3 | 27.0 | assumption | 75–83† |
| 83 | GPT-6 Luna (medium) | ChatGPT Plus | 8.1× | $3.12 | 38.6 | 27.0 | assumption | 75–83† |
| 84 | GPT-6 Luna (low) | ChatGPT Pro 500 | 10.772× | $0.78 | 34.9 | 17.3 | assumption | 84–87† |
| 85 | GPT-6 Luna (low) | ChatGPT Pro 100 | 10.55× | $0.79 | 34.9 | 17.3 | assumption | 84–87† |
| 86 | GPT-6 Luna (low) | ChatGPT Pro 200 | 10.42× | $0.80 | 34.9 | 17.3 | assumption | 84–87† |
| 87 | GPT-6 Luna (low) | ChatGPT Plus | 8.1× | $1.03 | 34.2 | 17.3 | assumption | 84–87† |
| 88 | GPT-5.6 Luna (low) | ChatGPT Pro 500 | 10.772× | $1.92 | 32.3 | 17.0 | assumption | 88–91† |
| 89 | GPT-5.6 Luna (low) | ChatGPT Pro 100 | 10.55× | $1.96 | 32.3 | 17.0 | assumption | 88–91† |
| 90 | GPT-5.6 Luna (low) | ChatGPT Pro 200 | 10.42× | $1.99 | 32.2 | 17.0 | assumption | 88–91† |
| 91 | GPT-5.6 Luna (low) | ChatGPT Plus | 8.1× | $2.56 | 31.6 | 17.0 | assumption | 88–91† |

- **subset cost**: scored on the workload of the components it has, against that workload's own anchors; its ordering against main-workload rows is not identified (O17).
- **provider-claimed leaf**: a quality leaf comes from the model provider's own published result (O36's last source); the row competes but earns no interval label (E233).
- **provisional quality**: observed leaves cover under 70% of quality weight, fewer than two software-engineering leaves or under 40% software-engineering weight are observed, or a leaf of 20% or more (FrontierCode, Terminal-Bench) is missing; ranked and flagged, never floored (O8).
- **partial component**: AA marks tasks of a basket component missing or declined (E37), or the component's cost cannot be reconciled with AA's prices (E170).
- **valuation basis unverified**: AA's cost reconciles with neither its displayed prices nor a registered price record; ranked, but outside interval outputs and cost anchors (E170 outcome 4).
- **no cost**: AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown.
- **AA cost caveat**: AA states that its published cost omits a pricing term.
- **API-cost fallback**: no admitted Plan route; the Plan ranking uses the API cost (O13).

Not ranked (34 roster models): Claude Fable 5, Claude Fable 5.1, Claude Opus 4.8, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (low), Claude Sonnet 5.5 (medium), DeepSeek V4 Flash, DeepSeek V4 Pro, GLM-5.2, GLM-5.3, GLM-5.3 Flash, GPT-5.5, GPT-5.6 Luna, GPT-5.6 Sol, GPT-6 Sol, GPT-6.1 Sol (low), Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Gemini 3.8 Flash, Grok 4.6, Grok 4.6 (xhigh), Grok 4.7, Kimi K3, MiMo-V2.6-Flash, MiniMax-M3.1-Flash, Muse Spark 1.2, Muse Spark 1.3, Muse Spark 1.3 (xhigh), Muse Wonder, Muse Wonder Full, Qwen3.8 Max. Reasons are listed in [scores.md](scores.md#not-ranked). Of these, 2 qualify for the cohort but are listed, not ranked, because a benchmark is still missing after a logged search (O36, O38): MiMo-V2.6-Flash (an AA frontier family; no Bug Hunt Bench); MiniMax-M3.1-Flash (no Bug Hunt Bench).

**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| MiMo-V2.6-Flash | Bug Hunt Bench | 43.2 | 85% | 43.4 | 49.0 | $60.37 | $52.59 |
| MiniMax-M3.1-Flash | Bug Hunt Bench | 45.5 | 85% | 41.3 | 46.5 | $234.35 | $234.35 |

### What the evidence supports

- API basis, main workload: the definite frontier (no configuration can beat it on both cost and quality anywhere inside the published record's precision and missing-evidence bounds) is Claude Sonnet 5.5 (max), Claude Opus 5.5 (max), GPT-6.1 Sol (max), Claude Opus 5.5 (xhigh), GPT-6.1 Sol (xhigh), GPT-6 Astra (xhigh), GPT-6.1 Sol (high), MiMo-V2.6-Pro, Claude Haiku 5.5 (xhigh), GPT-6.1 Sol (medium), GPT-6 Luna (max), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), GPT-6 Luna (high), GPT-6 Luna (medium), GPT-6 Luna (low); the possible frontier adds none. Cheapest at or above quality 48.9: not unique; possibly GPT-6.1 Sol (high), GPT-6.1 Sol (medium). (Bar comparison: compares 14 configurations that can qualify.) Cheapest at or above quality 32.3: not unique; possibly Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium). (Bar comparison: compares 21 configurations that can qualify.) Cheapest at or above quality 55.0: GPT-6.1 Sol (max) (confirmed). (Bar comparison: compares 8 configurations that can qualify.)
- Plan basis: interval outputs not evaluated (no row has FullCost and an identified M_W (E61/E67)).
- API basis, displayed record (not a claim; E203): cheapest at or above quality 48.9: GPT-6.1 Sol (medium) ($318.05 per basket run; 14 reach it); at or above quality 32.3: Claude Haiku 5.5 (medium) ($45.91 per basket run; 21 reach it); at or above quality 55.0: GPT-6.1 Sol (max) ($796.76 per basket run; 8 reach it).
- API basis, noise-margin companion (O44; each bar plus 5.2 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 54.2: GPT-6.1 Sol (max) ($796.76 per basket run); at or above quality 37.5: Claude Haiku 5.5 (xhigh) ($107.10 per basket run); at or above quality 60.2: none.
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 48.9: claude-opus-5-5-medium@claude-pro ($24.17 per basket run; 47 reach it); at or above quality 32.3: claude-haiku-5-5-medium@claude-pro ($0.78 per basket run; 68 reach it); at or above quality 55.0: claude-opus-5-5-high@claude-pro ($31.58 per basket run; 25 reach it).
- Plan basis, noise-margin companion (O44; each bar plus 5.2 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 54.2: claude-opus-5-5-medium@claude-pro ($24.17 per basket run); at or above quality 37.5: claude-haiku-5-5@claude-pro ($1.82 per basket run); at or above quality 60.2: none.
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): MiMo-V2.6-Flash, MiniMax-M3.1-Flash.

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

AA footnote (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (low)): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## How v3 scores value

- **Cost is the SDLC basket.** SDLC basket v1: AA's published cost of running the AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, in USD per basket run. Pending capture: Coding Agent Index, ITBench-AA. v2 used AA's cost to run the whole Intelligence Index per Index point.
- **Cost keeps its magnitude.** The cost score is 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100, against anchors frozen with anchor version `v3-2026-10-23`. A model entering or leaving the cohort does not move another model's score. At the API anchors, doubling cost costs 2.17 value points, which 2.90 quality points offset.
- **Quality is measured, not ranked.** Each of the 10 leaves is placed on fixed 0–100 anchors from its raw value, so quality no longer depends on which other models are ranked. Only configurations with every leaf are ranked (O36), so all ranked rows are scored on the same benchmarks; each leaf filled from another party or a provider is listed in [raw-data.md](raw-data.md#leaf-gap-fills-and-searches-o36).
- **Plan value is route evidence.** Each subscription route carries its Value Multiple, evidence grade (controlled measurement, concordant reports, owner-named assumption) and identification status; the Plan ranking is labelled exploratory until multiples are identified on the basket.
- **Uncertainty is shown, not hidden.** Interval outputs certify which frontier and cheapest-above-a-bar claims the published record supports; scenario shares report frequencies over declared streams.
- v3 values are not numerically comparable with v2 or earlier releases.

## Sources and audit trail

- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and its model pages: Intelligence Index component scores and the per-task evaluation costs of the basket.
- [AA Coding Agent Index v2.0](https://artificialanalysis.ai/agents/coding-agents): the Coding Agent Index cost (FrontierCode, Terminal-Bench and SWE-Atlas-QnA-AA) for each exact configuration (O50); AA withdrew DeepSWE v1.1 in October 2026 and it is no longer a leaf (O49).
- AA's own Terminal-Bench 4.0 run (the leaf; [tbench.ai](https://www.tbench.ai/leaderboard/terminal-bench/4.0) rows fill a gap and serve as a cross-check, O37), [Bug Hunt Bench](https://bughunt.productcompass.pm/) owner-published runs, [Cognition's FrontierCode leaderboard](https://cognition.com/data/frontiercode-leaderboard/data.json) and model-provider results for leaves AA has not run (O36).
- [SemiAnalysis subscription measurements](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (owner-selected 2026-10-07) for the Claude and ChatGPT plan Value Multiples; owner-named transfers are labelled as assumptions.
- The evidence bundle in `data/scores.json` lists every input artifact with its SHA-256; bundle hash `152a534fdfe40e97b4112047ee476bf425b7b0b551d200d7b46c4f3738b3b4c4`.
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

Observed 2026-10-23T05:27:39Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 697 catalog models selected; 189 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 697 models, plotted 189 eligible points, and displayed 18 frontier points. Public metric/export gaps are shown explicitly. All 7 distinct frontier model families are required in the main ranking using exact selected configurations; 6 are included. Other effort configurations remain separate comparison entries. 11 plotted configurations from 8 families lie within 3 Index points of the rendered frontier; 7 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | $10.63 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | $31.17 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | $47.85 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 34 (rounded) | $56.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 38 (rounded) | $94.07 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.55 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36): no Bug Hunt Bench |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 41 (rounded) | $157.58 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Primary ranked | None |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 56 (rounded) | $7,259.50 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |
| [GPT-5.6 Luna (low)](https://artificialanalysis.ai/models/gpt-5-6-luna-low) | gpt-5-6-luna-low | 21 (rounded) | $27.02 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 29 (rounded) | $34.31 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [MiniMax-M3.1-Flash](https://artificialanalysis.ai/models/minimax-m3-1-flash) | minimax-m3-1-flash | 43 (rounded) | $283.18 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36): no Bug Hunt Bench |
| [Claude Haiku 5.5 (max)](https://artificialanalysis.ai/models/claude-haiku-5-5) | claude-haiku-5-5 | 43 (rounded) | $330.25 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [DeepSeek V4.1 Flash 1017 (max)](https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017) | deepseek-v4-1-flash-1017 | 45 (rounded) | $444.60 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (medium with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-medium) | claude-opus-5-5-medium | 51 (rounded) | $1,626.81 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Sonnet 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh) | claude-sonnet-5-5-xhigh | 52 (rounded) | $2,176.82 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Gemini 4 Argon (high)](https://artificialanalysis.ai/models/gemini-4-argon) | gemini-4-argon | 53 (rounded) | $2,407.24 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 51 (rounded) | $2,925.01 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 52 (rounded) | $3,802.98 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 53 (rounded) | $5,324.10 | Near AA frontier (within 3 Index points) | Primary ranked | None |
