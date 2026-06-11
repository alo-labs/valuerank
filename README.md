# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v0.9  
**Updated:** June 12, 2026  
**Scope:** 14 DeepSWE-listed models, 20 scored dimensions

## What ValueRank is

ValueRank is a production-weighted ranking of frontier AI models. It combines benchmark quality, reliability, speed, and a composite cost term into a single rank-based score.

v0.9 keeps the DeepSWE-constrained roster and makes hallucination resistance a primary reliability factor:

- Keeps the ranked pool limited to **models listed on DeepSWE**
- Explicitly excludes **Grok-Build-0.1**
- Explicitly excludes **Gemini 3 Flash**
- Adds **AA-Omniscience Hallucination Rate** at **6%** weight, taken from IFBench, which moves from **18%** to **12%**
- Refreshes **AA-Omniscience Index** and hallucination-rate rows from the current Artificial Analysis Omniscience payload
- Formalizes a **family-level alias rule** for benchmark rows that publish only a public reasoning-profile suffix such as `GPT-5.5 (xhigh)` or `Claude Opus 4.8 (max)`
- Keeps the existing neutral-50 missing-data rule where no exact or policy-allowed current row exists

## v0.9 Ranking

Composite cost is built from normalized Artificial Analysis eval cost plus normalized DeepSWE average cost per task, then renormalized back to a `0–100` cost scale before rank-normalization.

| Rank | Model | Score | Quality | Composite Cost |
|---|---|---:|---:|---:|
| 1 | Gemini 3.1 Pro | 69.4 | 61.8 | $13.78 |
| 2 | MiMo-V2.5-Pro | 61.1 | 48.1 | $7.04 |
| 3 | MiniMax M3 | 58.5 | 54.9 | $18.32 |
| 4 | Kimi K2.6 | 52.8 | 44.7 | $17.95 |
| 5 | GPT-5.5 | 52.1 | 64.3 | $50.97 |
| 6 | Claude Opus 4.8 | 51.2 | 65.7 | $80.37 |
| 7 | DeepSeek V4-Pro | 49.5 | 37.8 | $14.22 |
| 8 | Gemini 3.5 Flash | 48.5 | 54.4 | $35.56 |
| 9 | GPT-5.4 Mini | 45.4 | 40.0 | $18.95 |
| 10 | GLM 5.1 | 43.8 | 40.5 | $25.82 |
| 11 | Claude Sonnet 4.6 | 43.8 | 43.0 | $31.73 |
| 12 | GPT-5.4 | 41.9 | 48.2 | $39.90 |
| 13 | Claude Opus 4.6 | 41.3 | 42.3 | $31.87 |
| 14 | Claude Opus 4.7 | 40.7 | 54.3 | $100.00 |

## Primary Sources Used in v0.9

- [DeepSWE](https://deepswe.datacurve.ai/)
- [Terminal-Bench 2.1](https://www.tbench.ai/leaderboard/terminal-bench/2.1)
- [Vals SWE-bench Verified](https://www.vals.ai/benchmarks/swebench)
- [Scale SWE-bench Pro public leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [Ai2 IFBench analysis](https://allenai.org/blog/ifbench-artificial-analysis)
- [OSWorld-Verified official results](https://os-world.github.io/)
- Artificial Analysis evaluation pages for **GPQA Diamond**, **HLE**, **SciCode**, **RULER/LCR**, **AA-Omniscience Index**, and **AA-Omniscience Hallucination Rate**
- Artificial Analysis model pages for current eval cost, speed, and intelligence-index values

## Files

- [scores.md](/Users/shafqat/valuerank/scores.md): final rankings and normalized scores
- [raw-data.md](/Users/shafqat/valuerank/raw-data.md): benchmark inputs used for v0.9
- [methodology.md](/Users/shafqat/valuerank/methodology.md): scoring method, weights, cohort rules, and alias policy
- [site/index.html](/Users/shafqat/valuerank/site/index.html): published static site
