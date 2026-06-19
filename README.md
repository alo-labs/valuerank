# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.2 
**Updated:** June 20, 2026 
**Scope:** 8 DeepSWE-listed models, 15 scored dimensions

## What ValueRank is

ValueRank is a production-weighted ranking of frontier AI models. It combines benchmark quality, reliability, speed, and a composite cost term into a single rank-based score.

v1.2 shrinks the cohort from 13 to 8 DeepSWE-listed models and adds Claude Fable 5, keeps hallucination resistance as a primary reliability factor, and reruns the benchmark-gap audit with an official-source-first pass plus current secondary implementations.

> The five v1.1-ranked models that are no longer on DeepSWE (`GPT-5.4 Mini`, `MiMo-V2.5-Pro`, `MiniMax M3`, `GLM 5.1`, `DeepSeek V4-Pro`) are preserved with their v1.1 scores in [methodology.md](/Users/shafqat/valuerank/methodology.md#v11-scores-of-models-removed-from-cohort) for historical reference.

- Keeps the ranked pool limited to **models listed on DeepSWE**
- Explicitly excludes **Grok-Build-0.1**
- Explicitly excludes **Gemini 3 Flash**
- Explicitly excludes **Claude Opus 4.6**
- Adds **Claude Fable 5** *(NEW in v1.2)*
- Keeps **AA-Omniscience Hallucination Rate** at **6%** weight, with **IFBench** at **12%**
- Uses only **benchmarks with full coverage across all 8 ranked models**
- Keeps the active score at **zero missing benchmark cells**
- Reruns the excluded-benchmark audit against **official benchmark-owner sources first**, then current secondary implementations such as **Artificial Analysis**, **Kaggle Benchmarks**, and **LLM Stats**
- Finds that the official-first audit still does **not** unlock any additional zero-gap benchmark

## v1.2 Ranking

Composite cost is built from normalized Artificial Analysis eval cost plus normalized DeepSWE average cost per task, then renormalized back to a `0–100` cost scale before rank-normalization.

| Rank | Model | Score | Quality | Composite Cost |
|---|---|---:|---:|---:|
| 1 | Gemini 3.1 Pro | 59.1 | 59.8 | $42.24 |
| 2 | Gemini 3.5 Flash | 59.0 | 50.2 | $36.53 |
| 3 | Claude Fable 5 | 57.6 | 76.5 | $100.00 |
| 4 | GPT-5.5 | 56.9 | 66.2 | $47.72 |
| 5 | GPT-5.4 | 56.7 | 51.9 | $39.22 |
| 6 | Claude Opus 4.8 | 46.1 | 56.6 | $81.49 |
| 7 | Kimi K2.7 | 38.5 | 18.2 | $14.75 |
| 8 | Claude Sonnet 4.6 | 26.2 | 20.7 | $47.53 |

## v1.2 Frontier

Undominated on composite cost vs. quality (6 models):

- Gemini 3.1 Pro
- Gemini 3.5 Flash
- Claude Fable 5
- GPT-5.5
- GPT-5.4
- Kimi K2.7

## Sources Used in v1.2

Active scored dimensions still use primary sources:

- [DeepSWE](https://deepswe.datacurve.ai/)
- [Artificial Analysis model pages](https://artificialanalysis.ai/models)
- [Artificial Analysis Omniscience evaluation](https://artificialanalysis.ai/evaluations/omniscience?omniscience-hallucination-rate=hallucination-rate&omniscience-index=omniscience-index-vs-cost&omniscience-accuracy=accuracy-vs-cost#omniscience-hallucination-rate-tabs)
- [Ai2 IFBench analysis](https://allenai.org/blog/ifbench-artificial-analysis)

The official-first gap audit also checked:

- [Mercor APEX-Agents leaderboard](https://www.mercor.com/apex/apex-agents-leaderboard/)
- [IBM Research ITBench Kaggle benchmark](https://www.kaggle.com/benchmarks/ibm-research/itbench)
- [MMMU benchmark site](https://mmmu-benchmark.github.io/)
- [TIGER-Lab MMLU-Pro leaderboard](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)
- [LiveCodeBench official site](https://livecodebench.github.io/)
- [Cohere Labs Global-MMLU-Lite Kaggle benchmark](https://www.kaggle.com/benchmarks/cohere-labs/global-mmlu-lite)
- [Open Benchmarks AIME 2025 Kaggle benchmark](https://www.kaggle.com/benchmarks/open-benchmarks/aime-2025)
- [Open Benchmarks MATH-500 Kaggle benchmark](https://www.kaggle.com/benchmarks/open-benchmarks/math-500)
- Secondary benchmark implementations on [Artificial Analysis evaluations](https://artificialanalysis.ai/evaluations), [Kaggle Benchmarks](https://www.kaggle.com/benchmarks), and [LLM Stats](https://llm-stats.com/benchmarks)

## Files

- [scores.md](/Users/shafqat/valuerank/scores.md): final rankings and normalized scores
- [raw-data.md](/Users/shafqat/valuerank/raw-data.md): benchmark inputs and official-first exclusion audit
- [methodology.md](/Users/shafqat/valuerank/methodology.md): scoring method, weights, cohort rules, and audit policy
- [site/index.html](/Users/shafqat/valuerank/site/index.html): published static site
