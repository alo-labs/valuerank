# ValueRank
**Frontier AI configurations ranked by value for software engineering and DevOps: benchmark quality against what the work costs**

**Version:** v3.0.0
**Updated:** October 19, 2026
**Methodology:** 3.0.0 · SDLC basket v1 · anchor version v3-2026-10-21
**Scope:** 32 cohort configurations (31 with a value score) from a 49-model AA-mapped roster; value is a 25% cost score (nominal weight; 37% of API and 18% of Plan value variance) plus 75% quality over 11 benchmark leaves

## Current result

ValueRank ranks frontier AI model configurations (see Model inclusion) by value for software engineering and DevOps work, separately for API buyers and for subscription (Plan) buyers. Value is a fixed **25%** cost score plus **75%** benchmark quality. That weight is nominal: on the current panel cost accounts for 37% of the variance in API value and 18% in Plan value, because cost scores spread more than quality scores (see [methodology.md](methodology.md)). Cost is the contestant-model API token cost for the SDLC basket (not total agent or workflow operating cost): Artificial Analysis' (AA) published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, scored on a log scale against frozen anchors so cost ratios keep their size. Coding and terminal tasks (Coding Agent Index, Terminal-Bench 4.0 (AA Index run), SciCode) make up 53% of the basket's cost (median over 29 configurations with the full basket; 40% to 85%); AA-Briefcase, GDP.pdf, which have no quality leaf, make up 14%; the Coding Agent Index's SWE-Atlas QnA (124 of its 303 tasks) has no quality leaf either, and its cost share is not separable because AA publishes one pooled cost. Quality is the weighted mean of 11 benchmark leaves on fixed 0–100 anchors, and every ranked configuration has all 11 for its exact configuration (O36): a leaf AA has not run comes from another party's run of the same benchmark, then from the model provider's published result, and a configuration still missing one after a logged exhaustive search is listed, not ranked. The Plan ranking divides the basket's API cost by a subscription route's Value Multiple at full utilisation, with one row per configuration and plan (O48), and uses the API cost, flagged, when no route is admitted. No Value Multiple is yet identified on the basket itself (0 of 90 rows), so the Plan ranking is labelled exploratory.

Claude Sonnet 5.5 leads the Plan ranking at 59.5 (owner-named transfer); GPT-6.1 Sol (xhigh) leads the API ranking at 58.8; Claude Sonnet 5.5 leads on quality.

| Plan rank | API rank | Configuration | Plan value | API value | Quality | Quality coverage | API cost (USD per basket run) | Plan cost (USD per basket run) | Plan route | Flags | Noise band (Plan / API) |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | 13 | [Claude Sonnet 5.5 (max)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5/) | 59.5 | 51.4 | 64.5 | 100% | $9,373.65 | $159.15 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–28† / 12–21 |
| 4 | 1 | [GPT-6.1 Sol (xhigh)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-xhigh/) | 59.1 | 58.8 | 61.6 | 100% | $827.23 | $76.79 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 1–28† / 1–5 |
| 7 | 14 | [Claude Opus 5.5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5-5/) | 58.7 | 50.5 | 63.7 | 100% | $9,989.15 | $169.60 | Claude Pro $20 · Opus 5.5 (58.9×, measured) | — | 1–28 / 12–21 |
| 9 | 11 | [Claude Sonnet 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-xhigh/) | 58.6 | 52.3 | 59.4 | 100% | $2,836.05 | $48.15 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–28† / 6–11 |
| 14 | 4 | [GPT-6.1 Sol (high)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-high/) | 58.0 | 57.9 | 59.6 | 100% | $700.51 | $65.03 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 1–28† / 1–5 |
| 16 | 2 | [GPT-6.1 Sol (medium)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-medium/) | 57.9 | 58.2 | 58.5 | 100% | $531.56 | $49.35 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 1–28† / 1–5 |
| 20 | 5 | [GPT-6.1 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-1-sol/) | 57.7 | 56.7 | 61.1 | 100% | $1,267.66 | $117.68 | ChatGPT Pro 500 $500 · GPT-6.1 Sol (10.772×, measured) | — | 1–28 / 1–5 |
| 23 | 10 | [Claude Sonnet 5.5 (high)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-high/) | 57.6 | 52.4 | 55.3 | 100% | $1,248.00 | $21.19 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 1–28† / 6–11 |
| 29 | 15 | [GPT-6 Astra (max)](https://valuerank.alolabs.dev/models/gpt-6-astra/) | 54.4 | 50.4 | 61.0 | 100% | $6,107.09 | $421.61 | ChatGPT Pro 200 $200 · GPT-6 Astra (14.485×, measured) | — | 29–73 / 12–21 |
| 30 | 7 | [GPT-6.1 Sol (low)](https://valuerank.alolabs.dev/models/gpt-6-1-sol-low/) | 54.3 | 55.1 | 52.6 | 100% | $375.21 | $34.83 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 29–73† / 6–11 |
| 33 | 18 | [Claude Sonnet 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-medium/) | 54.2 | 49.8 | 49.0 | 100% | $731.63 | $12.42 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 29–73† / 12–21 |
| 39 | 12 | [GPT-6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-6-sol/) | 53.3 | 51.7 | 56.8 | 100% | $1,999.41 | $185.61 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 29–73† / 12–21 |
| 42 | 29 | [Claude Opus 5 (max)](https://valuerank.alolabs.dev/models/claude-opus-5/) | 53.2 | 45.2 | 55.9 | 100% | $8,733.13 | $148.27 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 29–73† / 22–30 |
| 45 | 6 | [GPT-6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-6-luna/) | 53.0 | 55.3 | 47.4 | 100% | $132.87 | $12.33 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 29–73† / 6–11 |
| 49 | 16 | [GPT-5.6 Sol (max)](https://valuerank.alolabs.dev/models/gpt-5-6-sol/) | 52.9 | 50.2 | 58.7 | 100% | $4,238.14 | $393.44 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 29–73† / 12–21 |
| 53 | 19 | [Claude Haiku 5.5 (xhigh)](https://valuerank.alolabs.dev/models/claude-haiku-5-5/) | 52.6 | 49.5 | 43.7 | 100% | $292.07 | $4.96 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 29–73† / 12–21 |
| 58 | 23 | [Claude Sonnet 5.5 (low)](https://valuerank.alolabs.dev/models/claude-sonnet-5-5-low/) | 51.6 | 47.6 | 44.8 | 100% | $578.39 | $9.82 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | — | 29–73† / 22–30 |
| 59 | 3 | [MiMo-V2.6-Pro](https://valuerank.alolabs.dev/models/mimo-v2-6-pro/) | 51.6 | 57.9 | 55.1 | 100% | $136.13 | $115.28 | MiMo Token Plan Max $100 · quota ceiling (provider-derived) (1.1808×, assumption) | subset cost, provider-claimed leaf | 29–73† / 1–5 |
| 61 | 8 | [Gemini 4 Argon (high)](https://valuerank.alolabs.dev/models/gemini-4-argon/) | 51.6 | 55.1 | 64.5 | 100% | $3,628.64 | $3,628.64 | — | API-cost fallback | 29–73 / 6–11 |
| 62 | 9 | [GPT-5.6 Luna (max)](https://valuerank.alolabs.dev/models/gpt-5-6-luna/) | 51.6 | 52.7 | 48.4 | 100% | $319.25 | $29.64 | ChatGPT Pro 500 $500 · common GPT assumption (10.772×, assumption) | — | 29–73† / 6–11 |
| 65 | 20 | [Claude Haiku 5.5 (high)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-high/) | 51.5 | 49.2 | 40.8 | 100% | $181.35 | $3.08 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 29–73† / 12–21 |
| 69 | 24 | [Claude Fable 5.1 (max)](https://valuerank.alolabs.dev/models/claude-fable-5-1/) | 51.5 | 46.9 | 59.7 | 100% | $11,580.62 | $909.71 | Claude Max $100 · Fable 5.1 (12.73×, measured) | partial component, valuation basis unverified | 29–73 / 22–30 |
| 75 | 21 | [Claude Haiku 5.5 (medium)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-medium/) | 50.9 | 49.2 | 38.4 | 100% | $114.51 | $1.94 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 74–83† / 12–21 |
| 78 | 30 | [Claude Haiku 5.5 (max)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-max/) | 49.8 | 45.0 | 44.1 | 100% | $973.34 | $16.53 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 74–83† / 22–30 |
| 81 | 22 | [Claude Haiku 5.5 (low)](https://valuerank.alolabs.dev/models/claude-haiku-5-5-low/) | 49.1 | 48.1 | 34.5 | 100% | $71.52 | $1.21 | Claude Pro $20 · common Claude assumption (58.9×, assumption) | AA cost caveat | 74–83† / 22–30 |
| 84 | 17 | [Muse Spark 1.3 (max)](https://valuerank.alolabs.dev/models/muse-spark-1-3/) | 46.1 | 50.0 | 56.3 | 100% | $2,764.98 | $2,764.98 | — | API-cost fallback | 84–85 / 12–21 |
| 85 | 28 | [Grok 4.7 (xhigh)](https://valuerank.alolabs.dev/models/grok-4-7/) | 43.4 | 46.0 | 55.5 | 100% | $6,700.02 | $6,700.02 | — | API-cost fallback | 84–85 / 22–30 |
| 86 | 27 | [GLM-5.3 (max)](https://valuerank.alolabs.dev/models/glm-5-3/) | 42.7 | 46.3 | 52.1 | 100% | $3,186.29 | $3,186.29 | — | API-cost fallback | 86–88 / 22–30 |
| 87 | 25 | [Gemini 3.8 Flash (high)](https://valuerank.alolabs.dev/models/gemini-3-8-flash/) | 42.4 | 46.7 | 50.3 | 100% | $2,073.44 | $2,073.44 | — | API-cost fallback | 86–88 / 22–30 |
| 88 | 26 | [DeepSeek V4 Pro (max)](https://valuerank.alolabs.dev/models/deepseek-v4-pro/) | 41.0 | 46.7 | 45.3 | 100% | $801.50 | $801.50 | — | API-cost fallback | 86–88 / 22–30 |
| 89 | 31 | [Qwen3.8 Max](https://valuerank.alolabs.dev/models/qwen3-8-max/) | 38.9 | 41.8 | 48.9 | 100% | $5,417.03 | $5,417.03 | — | API-cost fallback | 89 / 31 |
| — | — | [Muse Wonder Full (max)](https://valuerank.alolabs.dev/models/muse-wonder-full/) | — | — | 64.4 | 100% | — | — | — | no cost | — / — |

Values are rounded for display; ranks are competition ranks (equal values share the better rank). The Plan rank is that of the configuration's own plan row (its selected route) in the Plan ranking of every plan below. Benchmark sampling noise (O39, an independent-task approximation): two values must differ by about 3.3 value points (median, 95%) to separate, and 0 of 30 adjacent API ranks and 28 of 88 adjacent Plan ranks do. Its net direction is not established: every configuration is scored on the same tasks, which correlates their errors and narrows the true threshold (API 1 at correlation 0.3, 2 at correlation 0.6; Plan 31 at correlation 0.3, 31 at correlation 0.6), while sources it leaves out widen it (run-to-run and harness variance, AA's single cost run and, for the 69 Plan rows on owner-named transfers, the transfer's error). The noise band column groups each row with the band's first row it cannot be told apart from (O42); a Plan band marked † rests on an owner-named transfer and excludes its error: a transferred multiple can be wrong by a factor of about 3.8 before the row's value moves by the median threshold (a tolerance, not an estimate of the transfer's error). The S1T scenario shares in [scores.md](scores.md) show each row's rank-1 and top-3 frequencies under that noise.

### Plan ranking: every plan (O48)

The Plan ranking has one row per configuration and subscription plan (owner decision O48): each plan on which the configuration has an admitted route, with that plan's route chosen by the official comparator; a configuration with no admitted route keeps one API-cost row. Rows of one configuration share its quality and API cost and differ only by the plan's Value Multiple. The table above shows each configuration's own plan row (its selected route).

| Plan rank | Configuration | Plan | Value Multiple | Plan cost (USD per basket run) | Plan value | Quality | Route evidence | Noise band |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | Claude Sonnet 5.5 (max) | Claude Pro | 58.9× | $159.15 | 59.5 | 64.5 | assumption | 1–28† |
| 2 | Claude Sonnet 5.5 (max) | Claude Max 20x | 58.63× | $159.88 | 59.4 | 64.5 | assumption | 1–28† |
| 3 | Claude Sonnet 5.5 (max) | Claude Max 5x | 57.25× | $163.73 | 59.4 | 64.5 | assumption | 1–28† |
| 4 | GPT-6.1 Sol (xhigh) | ChatGPT Pro 500 | 10.772× | $76.79 | 59.1 | 61.6 | assumption | 1–28† |
| 5 | GPT-6.1 Sol (xhigh) | ChatGPT Pro 100 | 10.55× | $78.41 | 59.0 | 61.6 | assumption | 1–28† |
| 6 | GPT-6.1 Sol (xhigh) | ChatGPT Pro 200 | 10.42× | $79.39 | 59.0 | 61.6 | assumption | 1–28† |
| 7 | Claude Opus 5.5 (max) | Claude Pro | 58.9× | $169.60 | 58.7 | 63.7 | controlled | 1–28 |
| 8 | Claude Opus 5.5 (max) | Claude Max 20x | 58.63× | $170.38 | 58.7 | 63.7 | controlled | 1–28 |
| 9 | Claude Sonnet 5.5 (xhigh) | Claude Pro | 58.9× | $48.15 | 58.6 | 59.4 | assumption | 1–28† |
| 10 | Claude Sonnet 5.5 (xhigh) | Claude Max 20x | 58.63× | $48.37 | 58.6 | 59.4 | assumption | 1–28† |
| 11 | Claude Opus 5.5 (max) | Claude Max 5x | 57.25× | $174.48 | 58.6 | 63.7 | controlled | 1–28 |
| 12 | Claude Sonnet 5.5 (xhigh) | Claude Max 5x | 57.25× | $49.54 | 58.6 | 59.4 | assumption | 1–28† |
| 13 | GPT-6.1 Sol (xhigh) | ChatGPT Plus | 8.1× | $102.13 | 58.4 | 61.6 | assumption | 1–28† |
| 14 | GPT-6.1 Sol (high) | ChatGPT Pro 500 | 10.772× | $65.03 | 58.0 | 59.6 | assumption | 1–28† |
| 15 | GPT-6.1 Sol (high) | ChatGPT Pro 100 | 10.55× | $66.40 | 57.9 | 59.6 | assumption | 1–28† |
| 16 | GPT-6.1 Sol (medium) | ChatGPT Pro 500 | 10.772× | $49.35 | 57.9 | 58.5 | assumption | 1–28† |
| 17 | GPT-6.1 Sol (high) | ChatGPT Pro 200 | 10.42× | $67.23 | 57.9 | 59.6 | assumption | 1–28† |
| 18 | GPT-6.1 Sol (medium) | ChatGPT Pro 100 | 10.55× | $50.39 | 57.9 | 58.5 | assumption | 1–28† |
| 19 | GPT-6.1 Sol (medium) | ChatGPT Pro 200 | 10.42× | $51.01 | 57.8 | 58.5 | assumption | 1–28† |
| 20 | GPT-6.1 Sol (max) | ChatGPT Pro 500 | 10.772× | $117.68 | 57.7 | 61.1 | controlled | 1–28 |
| 21 | GPT-6.1 Sol (max) | ChatGPT Plus | 10.55× | $120.16 | 57.6 | 61.1 | controlled | 1–28 |
| 21 | GPT-6.1 Sol (max) | ChatGPT Pro 100 | 10.55× | $120.16 | 57.6 | 61.1 | controlled | 1–28 |
| 23 | Claude Sonnet 5.5 (high) | Claude Pro | 58.9× | $21.19 | 57.6 | 55.3 | assumption | 1–28† |
| 24 | Claude Sonnet 5.5 (high) | Claude Max 20x | 58.63× | $21.29 | 57.6 | 55.3 | assumption | 1–28† |
| 25 | GPT-6.1 Sol (max) | ChatGPT Pro 200 | 10.42× | $121.66 | 57.6 | 61.1 | controlled | 1–28 |
| 26 | Claude Sonnet 5.5 (high) | Claude Max 5x | 57.25× | $21.80 | 57.5 | 55.3 | assumption | 1–28† |
| 27 | GPT-6.1 Sol (high) | ChatGPT Plus | 8.1× | $86.48 | 57.3 | 59.6 | assumption | 1–28† |
| 28 | GPT-6.1 Sol (medium) | ChatGPT Plus | 8.1× | $65.62 | 57.2 | 58.5 | assumption | 1–28† |
| 29 | GPT-6 Astra (max) | ChatGPT Pro 200 | 14.485× | $421.61 | 54.4 | 61.0 | controlled | 29–73 |
| 30 | GPT-6.1 Sol (low) | ChatGPT Pro 500 | 10.772× | $34.83 | 54.3 | 52.6 | assumption | 29–73† |
| 31 | GPT-6 Astra (max) | ChatGPT Pro 500 | 13.91× | $439.04 | 54.3 | 61.0 | controlled | 29–73 |
| 32 | GPT-6.1 Sol (low) | ChatGPT Pro 100 | 10.55× | $35.56 | 54.2 | 52.6 | assumption | 29–73† |
| 33 | Claude Sonnet 5.5 (medium) | Claude Pro | 58.9× | $12.42 | 54.2 | 49.0 | assumption | 29–73† |
| 34 | Claude Sonnet 5.5 (medium) | Claude Max 20x | 58.63× | $12.48 | 54.2 | 49.0 | assumption | 29–73† |
| 35 | GPT-6.1 Sol (low) | ChatGPT Pro 200 | 10.42× | $36.01 | 54.2 | 52.6 | assumption | 29–73† |
| 36 | Claude Sonnet 5.5 (medium) | Claude Max 5x | 57.25× | $12.78 | 54.2 | 49.0 | assumption | 29–73† |
| 37 | GPT-6 Astra (max) | ChatGPT Pro 100 | 13.22× | $461.96 | 54.1 | 61.0 | controlled | 29–73 |
| 38 | GPT-6.1 Sol (low) | ChatGPT Plus | 8.1× | $46.32 | 53.6 | 52.6 | assumption | 29–73† |
| 39 | GPT-6 Sol (max) | ChatGPT Pro 500 | 10.772× | $185.61 | 53.3 | 56.8 | assumption | 29–73† |
| 40 | GPT-6 Sol (max) | ChatGPT Pro 100 | 10.55× | $189.52 | 53.3 | 56.8 | assumption | 29–73† |
| 41 | GPT-6 Sol (max) | ChatGPT Pro 200 | 10.42× | $191.88 | 53.2 | 56.8 | assumption | 29–73† |
| 42 | Claude Opus 5 (max) | Claude Pro | 58.9× | $148.27 | 53.2 | 55.9 | assumption | 29–73† |
| 43 | Claude Opus 5 (max) | Claude Max 20x | 58.63× | $148.95 | 53.2 | 55.9 | assumption | 29–73† |
| 44 | Claude Opus 5 (max) | Claude Max 5x | 57.25× | $152.54 | 53.1 | 55.9 | assumption | 29–73† |
| 45 | GPT-6 Luna (max) | ChatGPT Pro 500 | 10.772× | $12.33 | 53.0 | 47.4 | assumption | 29–73† |
| 46 | GPT-6 Luna (max) | ChatGPT Pro 100 | 10.55× | $12.59 | 52.9 | 47.4 | assumption | 29–73† |
| 47 | GPT-6 Astra (max) | ChatGPT Plus | 8.1× | $753.96 | 52.9 | 61.0 | controlled | 29–73 |
| 48 | GPT-6 Luna (max) | ChatGPT Pro 200 | 10.42× | $12.75 | 52.9 | 47.4 | assumption | 29–73† |
| 49 | GPT-5.6 Sol (max) | ChatGPT Pro 500 | 10.772× | $393.44 | 52.9 | 58.7 | assumption | 29–73† |
| 50 | GPT-5.6 Sol (max) | ChatGPT Pro 100 | 10.55× | $401.72 | 52.8 | 58.7 | assumption | 29–73† |
| 51 | GPT-5.6 Sol (max) | ChatGPT Pro 200 | 10.42× | $406.73 | 52.8 | 58.7 | assumption | 29–73† |
| 52 | GPT-6 Sol (max) | ChatGPT Plus | 8.1× | $246.84 | 52.6 | 56.8 | assumption | 29–73† |
| 53 | Claude Haiku 5.5 (xhigh) | Claude Pro | 58.9× | $4.96 | 52.6 | 43.7 | assumption | 29–73† |
| 54 | Claude Haiku 5.5 (xhigh) | Claude Max 20x | 58.63× | $4.98 | 52.6 | 43.7 | assumption | 29–73† |
| 55 | Claude Haiku 5.5 (xhigh) | Claude Max 5x | 57.25× | $5.10 | 52.5 | 43.7 | assumption | 29–73† |
| 56 | GPT-6 Luna (max) | ChatGPT Plus | 8.1× | $16.40 | 52.3 | 47.4 | assumption | 29–73† |
| 57 | GPT-5.6 Sol (max) | ChatGPT Plus | 8.1× | $523.23 | 52.2 | 58.7 | assumption | 29–73† |
| 58 | Claude Sonnet 5.5 (low) | Claude Pro | 58.9× | $9.82 | 51.6 | 44.8 | assumption | 29–73† |
| 59 | MiMo-V2.6-Pro | MiMo Token Plan Max | 1.1808× | $115.28 | 51.6 | 55.1 | assumption | 29–73† |
| 60 | Claude Sonnet 5.5 (low) | Claude Max 20x | 58.63× | $9.87 | 51.6 | 44.8 | assumption | 29–73† |
| 61 | Gemini 4 Argon (high) | API-cost fallback (no admitted plan) | — | $3,628.64 | 51.6 | 64.5 | fallback | 29–73 |
| 62 | GPT-5.6 Luna (max) | ChatGPT Pro 500 | 10.772× | $29.64 | 51.6 | 48.4 | assumption | 29–73† |
| 63 | Claude Sonnet 5.5 (low) | Claude Max 5x | 57.25× | $10.10 | 51.6 | 44.8 | assumption | 29–73† |
| 64 | GPT-5.6 Luna (max) | ChatGPT Pro 100 | 10.55× | $30.26 | 51.5 | 48.4 | assumption | 29–73† |
| 65 | Claude Haiku 5.5 (high) | Claude Pro | 58.9× | $3.08 | 51.5 | 40.8 | assumption | 29–73† |
| 66 | Claude Haiku 5.5 (high) | Claude Max 20x | 58.63× | $3.09 | 51.5 | 40.8 | assumption | 29–73† |
| 67 | GPT-5.6 Luna (max) | ChatGPT Pro 200 | 10.42× | $30.64 | 51.5 | 48.4 | assumption | 29–73† |
| 68 | Claude Haiku 5.5 (high) | Claude Max 5x | 57.25× | $3.17 | 51.5 | 40.8 | assumption | 29–73† |
| 69 | Claude Fable 5.1 (max) | Claude Max 5x | 12.73× | $909.71 | 51.5 | 59.7 | controlled | 29–73 |
| 70 | MiMo-V2.6-Pro | MiMo Token Plan Pro | 1.0944× | $124.39 | 51.4 | 55.1 | assumption | 29–73† |
| 71 | Claude Fable 5.1 (max) | Claude Max 20x | 12.425× | $932.04 | 51.4 | 59.7 | controlled | 29–73 |
| 72 | MiMo-V2.6-Pro | MiMo Token Plan Standard | 0.99× | $137.50 | 51.2 | 55.1 | assumption | 29–73† |
| 73 | MiMo-V2.6-Pro | MiMo Token Plan Lite | 0.984× | $138.34 | 51.2 | 55.1 | assumption | 29–73† |
| 74 | GPT-5.6 Luna (max) | ChatGPT Plus | 8.1× | $39.41 | 50.9 | 48.4 | assumption | 74–83† |
| 75 | Claude Haiku 5.5 (medium) | Claude Pro | 58.9× | $1.94 | 50.9 | 38.4 | assumption | 74–83† |
| 76 | Claude Haiku 5.5 (medium) | Claude Max 20x | 58.63× | $1.95 | 50.9 | 38.4 | assumption | 74–83† |
| 77 | Claude Haiku 5.5 (medium) | Claude Max 5x | 57.25× | $2.00 | 50.8 | 38.4 | assumption | 74–83† |
| 78 | Claude Haiku 5.5 (max) | Claude Pro | 58.9× | $16.53 | 49.8 | 44.1 | assumption | 74–83† |
| 79 | Claude Haiku 5.5 (max) | Claude Max 20x | 58.63× | $16.60 | 49.8 | 44.1 | assumption | 74–83† |
| 80 | Claude Haiku 5.5 (max) | Claude Max 5x | 57.25× | $17.00 | 49.7 | 44.1 | assumption | 74–83† |
| 81 | Claude Haiku 5.5 (low) | Claude Pro | 58.9× | $1.21 | 49.1 | 34.5 | assumption | 74–83† |
| 82 | Claude Haiku 5.5 (low) | Claude Max 20x | 58.63× | $1.22 | 49.1 | 34.5 | assumption | 74–83† |
| 83 | Claude Haiku 5.5 (low) | Claude Max 5x | 57.25× | $1.25 | 49.0 | 34.5 | assumption | 74–83† |
| 84 | Muse Spark 1.3 (max) | API-cost fallback (no admitted plan) | — | $2,764.98 | 46.1 | 56.3 | fallback | 84–85 |
| 85 | Grok 4.7 (xhigh) | API-cost fallback (no admitted plan) | — | $6,700.02 | 43.4 | 55.5 | fallback | 84–85 |
| 86 | GLM-5.3 (max) | API-cost fallback (no admitted plan) | — | $3,186.29 | 42.7 | 52.1 | fallback | 86–88 |
| 87 | Gemini 3.8 Flash (high) | API-cost fallback (no admitted plan) | — | $2,073.44 | 42.4 | 50.3 | fallback | 86–88 |
| 88 | DeepSeek V4 Pro (max) | API-cost fallback (no admitted plan) | — | $801.50 | 41.0 | 45.3 | fallback | 86–88 |
| 89 | Qwen3.8 Max | API-cost fallback (no admitted plan) | — | $5,417.03 | 38.9 | 48.9 | fallback | 89 |

- **subset cost**: scored on the workload of the components it has, against that workload's own anchors; its ordering against main-workload rows is not identified (O17).
- **provider-claimed leaf**: a quality leaf comes from the model provider's own published result (O36's last source); the row competes but earns no interval label (E233).
- **provisional quality**: observed leaves cover under 70% of quality weight, fewer than two software-engineering leaves or under 40% software-engineering weight are observed, or DeepSWE is missing; ranked and flagged, never floored (O8).
- **partial component**: AA marks tasks of a basket component missing or declined (E37), or the component's cost cannot be reconciled with AA's prices (E170).
- **valuation basis unverified**: AA's cost reconciles with neither its displayed prices nor a registered price record; ranked, but outside interval outputs and cost anchors (E170 outcome 4).
- **no cost**: AA publishes no cost for the configuration, so it has no value score and no rank (AGENTS.md); its quality is shown.
- **AA cost caveat**: AA states that its published cost omits a pricing term.
- **API-cost fallback**: no admitted Plan route; the Plan ranking uses the API cost (O13).

Not ranked (17 roster models): Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, DeepSeek V4 Flash, GLM-5.2, GLM-5.3 Flash, GPT-5.5, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.7 Flash, Grok 4.6, Grok 4.6 (xhigh), Kimi K3, MiMo-V2.6-Flash, Muse Spark 1.2, Muse Spark 1.3 (xhigh), Muse Wonder. Reasons are listed in [scores.md](scores.md#not-ranked). Of these, 5 qualify for the cohort but are listed, not ranked, because a benchmark is still missing after a logged search (O36, O38): DeepSeek V4 Flash (no FrontierCode 1.1); Grok 4.6 (xhigh) (no FrontierCode 1.1); MiMo-V2.6-Flash (an AA frontier family; no Bug Hunt Bench); Muse Spark 1.3 (xhigh) (no FrontierCode 1.1); Muse Wonder (no FrontierCode 1.1).

**Listed frontier families: indicative value, not ranked and not comparable (O41).** Quality is the mean over the leaves the configuration has, renormalised, with no imputation, so these values cannot be compared with the ranking above.

| Configuration | Missing | Quality (remaining leaves) | Quality coverage | Plan value (indicative) | API value (indicative) | API cost (USD per basket run) | Plan cost (USD per basket run) |
|---|---|---:|---:|---:|---:|---:|---:|
| MiMo-V2.6-Flash | Bug Hunt Bench | 53.9 | 90% | 52.6 | 60.0 | $60.37 | $52.59 |

### What the evidence supports

- API basis, main workload: the definite frontier (no configuration can beat it on both cost and quality anywhere inside the published record's precision and missing-evidence bounds) is Gemini 4 Argon (high), GPT-6.1 Sol (xhigh), Claude Sonnet 5.5 (max), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low), GPT-5.6 Luna (max), GPT-6 Luna (max), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (low); the possible frontier adds none. Not evaluable on this workload: Claude Fable 5.1 (max), MiMo-V2.6-Pro, Muse Wonder Full (max). Cheapest at or above quality 55.3: GPT-6.1 Sol (medium) (confirmed). (Bar comparison: compares 15 configurations that can qualify.) Cheapest at or above quality 47.4: not unique; possibly GPT-5.6 Luna (max), GPT-6 Luna (max). (Bar comparison: compares 22 configurations that can qualify.) Cheapest at or above quality 59.6: not unique; possibly GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high). (Bar comparison: compares 7 configurations that can qualify.)
- Plan basis: interval outputs not evaluated (no row has FullCost and an identified M_W (E61/E67)).
- API basis, displayed record (not a claim; E203): cheapest at or above quality 55.3: GPT-6.1 Sol (medium) ($531.56 per basket run; 16 reach it); at or above quality 47.4: GPT-6 Luna (max) ($132.87 per basket run; 23 reach it); at or above quality 59.6: GPT-6.1 Sol (high) ($700.51 per basket run; 8 reach it).
- API basis, noise-margin companion (O44; each bar plus 4.5 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 59.8: GPT-6.1 Sol (xhigh) ($827.23 per basket run); at or above quality 51.8: GPT-6.1 Sol (low) ($375.21 per basket run); at or above quality 64.0: Gemini 4 Argon (high) ($3,628.64 per basket run).
- Plan basis, displayed record (not a claim; E203): cheapest at or above quality 55.3: claude-sonnet-5-5-high@claude-pro ($21.19 per basket run; 48 reach it); at or above quality 47.4: gpt-6-luna@chatgpt-pro-500 ($12.33 per basket run; 66 reach it); at or above quality 59.6: gpt-6.1-sol-high@chatgpt-pro-500 ($65.03 per basket run; 25 reach it).
- Plan basis, noise-margin companion (O44; each bar plus 4.5 quality points, so the bar's own configuration cannot decide it): cheapest at or above quality 59.8: gpt-6.1-sol-xhigh@chatgpt-pro-500 ($76.79 per basket run); at or above quality 51.8: claude-sonnet-5-5-high@claude-pro ($21.19 per basket run); at or above quality 64.0: claude-sonnet-5-5@claude-pro ($159.15 per basket run).
- Fill-sensitive (E234): the displayed-record cheapest row changes when gap-filled leaves are removed or lowered by the measured offset at API quality 59.6, Plan quality 59.6.
- These outputs compare ranked configurations only; listed families shown with an indicative value (O41) are outside them (O43): MiMo-V2.6-Flash.

Scenario shares by stream, diagnostics and the release gates are in [scores.md](scores.md); the inputs behind every number are in [raw-data.md](raw-data.md).

## Model inclusion

**Frontier rule.** Every model family on the Pareto frontier that Artificial Analysis (AA) renders on its Intelligence Index versus total cost to run chart is ranked at its highest point on that line (along the strictly rising line also its dearest). Frontier membership is AA's rendered line as observed; ValueRank never recomputes it from rounded values.

**Near-frontier rule.** A plotted configuration is near-frontier when its public (rounded integer) Intelligence Index is within 3 points of the rendered frontier's Index at its cost, meaning the highest Index among rendered-frontier points that cost no more. Every near-frontier family is ranked or is explicitly deferred by a dated, reasoned roster decision. Its selected configuration may differ from the near configuration: it is the configuration already ranked for exact DeepSWE and Bug Hunt evidence when there is one, else the near point with the smallest Index gap. The cost ratio to the frontier is reported for information only.

Policy as recorded: A plotted configuration is near-frontier when it lies within 3 Intelligence Index points of the rendered frontier at its cost. Every near-frontier model family must be in the primary ranking, with its own selected configuration, or be explicitly deferred with a dated, reasoned roster decision. The cost ratio to the cheapest frontier point of equal or higher intelligence is reported for information only.

Chart observed 2026-10-17T18:48:27Z (Intelligence Index v4.3.2): 694 catalog models selected, 189 plotted points and 18 rendered Pareto vertices across 7 families. 9 plotted points across 6 families are near-frontier.

Near-frontier models: 6 required, 0 deferred by roster decision.

Frontier families and the configuration selected for each:

- Claude Haiku 5.5: Claude Haiku 5.5 (xhigh)
- Claude Opus 5.5: Claude Opus 5.5 (max with fallback)
- Claude Sonnet 5.5: Claude Sonnet 5.5 (max with fallback)
- GPT-6 Luna: GPT-6 Luna (max)
- GPT-6.1 Sol: GPT-6.1 Sol (max)
- MiMo-V2.6-Flash: MiMo-V2.6-Flash
- MiMo-V2.6-Pro: MiMo-V2.6-Pro

Near-frontier families and each family's near point closest to the frontier (a family's primary configuration is its configuration with exact DeepSWE and Bug Hunt results when it has one, O30, and every other effort with both results is ranked as its own row, O33, so the ranked configurations can differ):

- Claude Haiku 5.5: Claude Haiku 5.5 (low), 1 Index point below the frontier
- Claude Opus 5.5: Claude Opus 5.5 (medium with fallback), 1 Index point below the frontier
- Claude Sonnet 5.5: Claude Sonnet 5.5 (xhigh with fallback), 2 Index points below the frontier
- GPT-5.6 Luna: GPT-5.6 Luna (low), 1 Index point below the frontier
- GPT-6 Astra: GPT-6 Astra (xhigh), 2 Index points below the frontier
- Gemini 4 Argon: Gemini 4 Argon (high), 1 Index point below the frontier

AA footnote (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (low)): Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis.

## How v3 scores value

- **Cost is the SDLC basket.** SDLC basket v1: AA's published cost of running the Coding Agent Index, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0 (AA Index run), SciCode and AA-LCR once at API rates, in USD per basket run. Pending capture: FrontierCode, ITBench-AA. v2 used AA's cost to run the whole Intelligence Index per Index point.
- **Cost keeps its magnitude.** The cost score is 100 × (ln c_H − ln c) / (ln c_H − ln c_L), clipped to 0–100, against anchors frozen with anchor version `v3-2026-10-21`. A model entering or leaving the cohort does not move another model's score. At the API anchors, doubling cost costs 2.74 value points, which 3.65 quality points offset.
- **Quality is measured, not ranked.** Each of the 11 leaves is placed on fixed 0–100 anchors from its raw value, so quality no longer depends on which other models are ranked. Only configurations with every leaf are ranked (O36), so all ranked rows are scored on the same benchmarks; each leaf filled from another party or a provider is listed in [raw-data.md](raw-data.md#leaf-gap-fills-and-searches-o36).
- **Plan value is route evidence.** Each subscription route carries its Value Multiple, evidence grade (controlled measurement, concordant reports, owner-named assumption) and identification status; the Plan ranking is labelled exploratory until multiples are identified on the basket.
- **Uncertainty is shown, not hidden.** Interval outputs certify which frontier and cheapest-above-a-bar claims the published record supports; scenario shares report frequencies over declared streams.
- v3 values are not numerically comparable with v2 or earlier releases.

## Sources and audit trail

- [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) and its model pages: Intelligence Index component scores and the per-task evaluation costs of the basket.
- [AA Coding Agent Index, DeepSWE v1.1](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1): DeepSWE pass@1 and the Coding Agent Index cost for each exact configuration.
- AA's own Terminal-Bench 4.0 run (the leaf; [tbench.ai](https://www.tbench.ai/leaderboard/terminal-bench/4.0) rows fill a gap and serve as a cross-check, O37), [Bug Hunt Bench](https://bughunt.productcompass.pm/) owner-published runs, [Cognition's FrontierCode leaderboard](https://cognition.com/data/frontiercode-leaderboard/data.json) and model-provider results for leaves AA has not run (O36).
- [SemiAnalysis subscription measurements](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) (owner-selected 2026-10-07) for the Claude and ChatGPT plan Value Multiples; owner-named transfers are labelled as assumptions.
- The evidence bundle in `data/scores.json` lists every input artifact with its SHA-256; bundle hash `634d0ccf66d118be9d426fd205623f1bd981f4de386f4894fc653145d41685fb`.
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

Observed 2026-10-17T18:48:27Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 694 catalog models selected; 189 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 694 models, plotted 189 eligible points, and displayed 18 frontier points. Public metric/export gaps are shown explicitly. All 7 distinct frontier model families are required in the main ranking using exact selected configurations; 6 are included. Other effort configurations remain separate comparison entries. 9 plotted configurations from 6 families lie within 3 Index points of the rendered frontier; 6 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | $10.63 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | $31.17 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | $47.85 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 34 (rounded) | $56.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 38 (rounded) | $94.07 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.55 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36): no Bug Hunt Bench |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 41 (rounded) | $157.58 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 56 (rounded) | $7,259.50 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |
| [GPT-5.6 Luna (low)](https://artificialanalysis.ai/models/gpt-5-6-luna-low) | gpt-5-6-luna-low | 21 (rounded) | $27.02 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-5.6 Luna family is represented in the primary ranking by its selected configuration (gpt-5-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 29 (rounded) | $34.31 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Haiku 5.5 (max)](https://artificialanalysis.ai/models/claude-haiku-5-5) | claude-haiku-5-5 | 43 (rounded) | $330.25 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (medium with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-medium) | claude-opus-5-5-medium | 51 (rounded) | $1,626.81 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh) | claude-sonnet-5-5-xhigh | 52 (rounded) | $2,176.82 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Gemini 4 Argon (high)](https://artificialanalysis.ai/models/gemini-4-argon) | gemini-4-argon | 53 (rounded) | $2,407.24 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 51 (rounded) | $2,925.01 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-6 Astra family is represented in the primary ranking by its selected configuration (gpt-6-astra-xhigh). No result is transferred between efforts. |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 52 (rounded) | $3,802.98 | Near AA frontier (within 3 Index points) | Missing from source roster | Exact evaluated variant absent from source roster |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 53 (rounded) | $5,324.10 | Near AA frontier (within 3 Index points) | Primary ranked | None |
