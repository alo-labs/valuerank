# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.3  
**Updated:** July 28, 2026  
**Scope:** 18 DeepSWE Best models, 12 scored dimensions

## What ValueRank is

ValueRank is a production-weighted ranking of frontier AI models. It combines benchmark quality, reliability, speed, and a composite cost term into a single rank-based score.

v1.3 expands the cohort to the **full current DeepSWE Best roster (n=18)**, keeps the **zero-gap** rule (no neutral-50 fills), drops dimensions without full AA coverage on the new models, and uses **DeepSWE-only Cost** because AA Intelligence Index total eval cost is unpublished for `Kimi K2.7 Code`.

- Keeps the ranked pool limited to **models on the current DeepSWE Best leaderboard**
- Explicitly excludes off-roster historical models: **Grok-Build-0.1**, **Gemini 3 Flash**, **Claude Opus 4.6**
- Includes **Grok 4.5**, **Claude Opus 5**, **GPT-5.6 Sol/Terra/Luna**, **Kimi K3**, **Muse Spark 1.1**, and other July 2026 DeepSWE entrants
- Uses only **benchmarks with full coverage across all 18 ranked models**
- Drops **IFBench**, **Terminal-Bench Hard**, and **τ²-Bench Telecom** (missing on newest AA model pages)
- Reruns the excluded-benchmark audit against **official sources first**, then secondary implementations

## v1.3 Ranking

Cost is DeepSWE average cost per task scaled to 0–100 (highest-cost model = 100), then rank-normalized.

| Rank | Model | Score | Quality | Composite Cost |
|---|---|---:|---:|---:|
| 1 | Kimi K3 | 66.9 | 67.9 | 17.61 |
| 2 | Grok 4.5 | 62.8 | 48.1 | 9.17 |
| 3 | Muse Spark 1.1 | 61.0 | 42.6 | 8.94 |
| 4 | GPT-5.6 Terra | 60.7 | 61.7 | 18.75 |
| 5 | GPT-5.6 Sol | 60.2 | 74.7 | 31.78 |
| 6 | Claude Opus 5 | 57.1 | 75.8 | 44.85 |
| 7 | GPT-5.6 Luna | 56.2 | 43.9 | 11.48 |
| 8 | GPT-5.5 | 55.3 | 62.0 | 27.39 |
| 9 | Claude Fable 5 | 53.0 | 75.2 | 81.93 |
| 10 | GLM-5.2 | 52.4 | 43.8 | 14.85 |
| 11 | Gemini 3.6 Flash | 51.7 | 39.9 | 13.37 |
| 12 | GPT-5.4 | 47.8 | 48.1 | 21.40 |
| 13 | Claude Opus 4.8 | 42.4 | 56.9 | 50.08 |
| 14 | Gemini 3.1 Pro | 39.7 | 47.4 | 35.91 |
| 15 | Kimi K2.7 Code | 34.8 | 9.6 | 10.68 |
| 16 | Gemini 3.5 Flash | 34.8 | 34.6 | 27.80 |
| 17 | Claude Sonnet 5 | 32.8 | 48.2 | 100.00 |
| 18 | Claude Sonnet 4.6 | 30.3 | 19.7 | 20.91 |

## v1.3 Frontier

Undominated on composite cost vs. quality:

- Claude Opus 5
- GPT-5.6 Sol
- Kimi K3
- Grok 4.5
- Muse Spark 1.1

## Sources Used in v1.3

- [DeepSWE](https://deepswe.datacurve.ai/) (Best roster; updated July 25, 2026)
- [Artificial Analysis model pages](https://artificialanalysis.ai/models)
- Evidence ledger: [`.refresh/v1.3/`](.refresh/v1.3/)

## Files

- [scores.md](scores.md): final rankings and normalized scores
- [raw-data.md](raw-data.md): benchmark inputs and official-first exclusion audit
- [methodology.md](methodology.md): scoring method, weights, cohort rules, and audit policy
- [site/index.html](site/index.html): published static site
