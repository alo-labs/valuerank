# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.0  
**Updated:** June 12, 2026  
**Scope:** 14 DeepSWE-listed models, 15 scored dimensions

## What ValueRank is

ValueRank is a production-weighted ranking of frontier AI models. It combines benchmark quality, reliability, speed, and a composite cost term into a single rank-based score.

v1.0 keeps the DeepSWE-constrained roster, keeps hallucination resistance as a primary reliability factor, and hardens the benchmark policy to zero gaps:

- Keeps the ranked pool limited to **models listed on DeepSWE**
- Explicitly excludes **Grok-Build-0.1**
- Explicitly excludes **Gemini 3 Flash**
- Keeps **AA-Omniscience Hallucination Rate** at **6%** weight, with **IFBench** at **12%**
- Uses only **benchmarks with full coverage across all 14 ranked models**
- Formalizes a **family-level alias rule** for benchmark rows that publish only a public reasoning-profile suffix such as `GPT-5.5 (xhigh)` or `Claude Opus 4.8 (max)`
- Removes the old **neutral-50 missing-data rule** from the active score because v1.0 contains **no missing benchmark cells**

## v1.0 Ranking

Composite cost is built from normalized Artificial Analysis eval cost plus normalized DeepSWE average cost per task, then renormalized back to a `0–100` cost scale before rank-normalization.

| Rank | Model | Score | Quality | Composite Cost |
|---|---|---:|---:|---:|
| 1 | Gemini 3.1 Pro | 74.7 | 68.8 | $13.78 |
| 2 | GPT-5.5 | 62.8 | 78.6 | $50.97 |
| 3 | MiMo-V2.5-Pro | 58.5 | 44.7 | $7.04 |
| 4 | MiniMax M3 | 57.1 | 53.0 | $18.32 |
| 5 | Kimi K2.6 | 55.3 | 48.0 | $17.95 |
| 6 | GPT-5.4 | 55.2 | 66.0 | $39.90 |
| 7 | Claude Opus 4.8 | 53.4 | 68.6 | $80.37 |
| 8 | Gemini 3.5 Flash | 50.5 | 57.1 | $35.56 |
| 9 | DeepSeek V4-Pro | 48.8 | 36.8 | $14.22 |
| 10 | GLM 5.1 | 41.4 | 37.3 | $25.82 |
| 11 | Claude Opus 4.7 | 40.8 | 54.4 | $100.00 |
| 12 | GPT-5.4 Mini | 37.9 | 30.0 | $18.95 |
| 13 | Claude Sonnet 4.6 | 35.4 | 31.8 | $31.73 |
| 14 | Claude Opus 4.6 | 35.3 | 34.2 | $31.87 |

## Primary Sources Used in v1.0

- [DeepSWE](https://deepswe.datacurve.ai/)
- [Artificial Analysis model pages](https://artificialanalysis.ai/models)
- [Artificial Analysis Omniscience evaluation](https://artificialanalysis.ai/evaluations/omniscience?omniscience-hallucination-rate=hallucination-rate&omniscience-index=omniscience-index-vs-cost&omniscience-accuracy=accuracy-vs-cost#omniscience-hallucination-rate-tabs)
- [Ai2 IFBench analysis](https://allenai.org/blog/ifbench-artificial-analysis)
- Artificial Analysis benchmark cards used for **GPQA Diamond**, **HLE**, **SciCode**, **CritPt**, **GDPval-AA**, **Terminal-Bench Hard**, **AA-LCR**, **AAI**, **AA-Omniscience Accuracy**, and **AA-Omniscience Non-Hallucination Rate**

## Files

- [scores.md](/Users/shafqat/valuerank/scores.md): final rankings and normalized scores
- [raw-data.md](/Users/shafqat/valuerank/raw-data.md): benchmark inputs used for v1.0
- [methodology.md](/Users/shafqat/valuerank/methodology.md): scoring method, weights, cohort rules, and alias policy
- [site/index.html](/Users/shafqat/valuerank/site/index.html): published static site
