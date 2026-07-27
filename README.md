# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.3.1  
**Updated:** July 28, 2026  
**Scope:** 17 DeepSWE Best models (ranked), 12 scored dimensions

## What ValueRank is

ValueRank is a production-weighted ranking of frontier AI models. It combines benchmark quality, reliability, speed, and a composite cost term into a single rank-based score.

v1.3.1 ranks **n=17** models from the current DeepSWE Best roster, keeps the **zero-gap** rule (no neutral-50 fills), drops dimensions without full AA coverage on the new models, and restores **AA+DeepSWE composite Cost**. **Kimi K2.7 Code** remains on DeepSWE but is **excluded from the ranked cohort** because AA Intelligence Index total eval cost is unpublished ([search evidence](.refresh/v1.3/aa-kimi-k27-cost-search.md)).

- Keeps the ranked pool limited to **models on the current DeepSWE Best leaderboard** with complete Cost inputs
- Explicitly excludes off-roster historical models: **Grok-Build-0.1**, **Gemini 3 Flash**, **Claude Opus 4.6**
- Excludes **Kimi K2.7 Code** from ranking (no AA Index total eval cost; DeepSWE row preserved in raw-data)
- Includes **Grok 4.5**, **Claude Opus 5**, **GPT-5.6 Sol/Terra/Luna**, **Kimi K3**, **Muse Spark 1.1**, and other July 2026 DeepSWE entrants
- Uses only **benchmarks with full coverage across all 17 ranked models**
- Drops **IFBench**, **Terminal-Bench Hard**, and **τ²-Bench Telecom** (missing on newest AA model pages)
- Reruns the excluded-benchmark audit against **official sources first**, then secondary implementations

## v1.3.1 Ranking

Cost is the average of normalized AA Index total eval cost and normalized DeepSWE avg cost per task (0–100, higher = costlier), then rank-normalized.

| Rank | Model | Score | Quality | Composite Cost |
|---|---|---:|---:|---:|
| 1 | Grok 4.5 | 60.6 | 44.9 | 10.27 |
| 2 | Kimi K3 | 59.2 | 66.4 | 30.45 |
| 3 | Muse Spark 1.1 | 58.9 | 39.5 | 9.34 |
| 4 | GPT-5.6 Terra | 58.8 | 60.0 | 27.67 |
| 5 | GPT-5.6 Sol | 58.2 | 73.8 | 46.46 |
| 6 | Claude Opus 5 | 56.5 | 74.3 | 56.48 |
| 7 | GPT-5.6 Luna | 53.9 | 41.1 | 14.13 |
| 8 | GPT-5.5 | 53.0 | 60.3 | 38.36 |
| 9 | Gemini 3.6 Flash | 52.6 | 36.2 | 13.14 |
| 10 | GLM-5.2 | 52.0 | 41.2 | 14.22 |
| 11 | Gemini 3.1 Pro | 51.0 | 45.6 | 25.19 |
| 12 | Claude Fable 5 | 50.0 | 73.6 | 90.97 |
| 13 | GPT-5.4 | 47.0 | 45.6 | 30.11 |
| 14 | Gemini 3.5 Flash | 42.8 | 30.5 | 23.14 |
| 15 | Claude Opus 4.8 | 40.8 | 54.2 | 58.36 |
| 16 | Claude Sonnet 5 | 32.9 | 45.5 | 85.61 |
| 17 | Claude Sonnet 4.6 | 21.7 | 17.2 | 40.26 |

## v1.3.1 Frontier

Undominated on composite cost vs. quality:

- Claude Opus 5
- GPT-5.6 Sol
- GPT-5.6 Terra
- Kimi K3
- Grok 4.5
- Muse Spark 1.1
- Gemini 3.1 Pro

## Sources Used in v1.3.1

- [DeepSWE](https://deepswe.datacurve.ai/) (Best roster; updated July 25, 2026)
- [Artificial Analysis model pages](https://artificialanalysis.ai/models)
- Evidence ledger: [`.refresh/v1.3/`](.refresh/v1.3/)

## Files

- [scores.md](scores.md): final rankings and normalized scores
- [raw-data.md](raw-data.md): benchmark inputs and official-first exclusion audit
- [methodology.md](methodology.md): scoring method, weights, cohort rules, and audit policy
- [site/index.html](site/index.html): published static site
