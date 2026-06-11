# ValueRank
**Frontier AI model ranking focused on production value**

**Version:** v1.1  
**Updated:** June 12, 2026  
**Scope:** 13 DeepSWE-listed models, 15 scored dimensions

## What ValueRank is

ValueRank is a production-weighted ranking of frontier AI models. It combines benchmark quality, reliability, speed, and a composite cost term into a single rank-based score.

v1.1 keeps the DeepSWE-constrained roster, keeps hallucination resistance as a primary reliability factor, and reruns the benchmark-gap audit with an official-source-first pass plus current secondary implementations:

- Keeps the ranked pool limited to **models listed on DeepSWE**
- Explicitly excludes **Grok-Build-0.1**
- Explicitly excludes **Gemini 3 Flash**
- Explicitly excludes **Claude Opus 4.6**
- Keeps **AA-Omniscience Hallucination Rate** at **6%** weight, with **IFBench** at **12%**
- Uses only **benchmarks with full coverage across all 13 ranked models**
- Keeps the active score at **zero missing benchmark cells**
- Reruns the excluded-benchmark audit against **official benchmark-owner sources first**, then current secondary implementations such as **Artificial Analysis**, **Kaggle Benchmarks**, and **LLM Stats**
- Finds that the official-first audit still does **not** unlock any additional zero-gap benchmark

## v1.1 Ranking

Composite cost is built from normalized Artificial Analysis eval cost plus normalized DeepSWE average cost per task, then renormalized back to a `0–100` cost scale before rank-normalization.

| Rank | Model | Score | Quality | Composite Cost |
|---|---|---:|---:|---:|
| 1 | Gemini 3.1 Pro | 73.6 | 67.5 | $13.78 |
| 2 | GPT-5.5 | 62.2 | 77.3 | $50.97 |
| 3 | MiMo-V2.5-Pro | 58.1 | 44.2 | $7.04 |
| 4 | MiniMax M3 | 56.0 | 52.4 | $18.32 |
| 5 | GPT-5.4 | 54.4 | 64.2 | $39.90 |
| 6 | Kimi K2.6 | 54.3 | 47.4 | $17.95 |
| 7 | Claude Opus 4.8 | 51.8 | 66.3 | $80.37 |
| 8 | Gemini 3.5 Flash | 49.9 | 55.4 | $35.56 |
| 9 | DeepSeek V4-Pro | 48.0 | 36.3 | $14.22 |
| 10 | GLM 5.1 | 40.0 | 36.7 | $25.82 |
| 11 | Claude Opus 4.7 | 39.0 | 52.0 | $100.00 |
| 12 | GPT-5.4 Mini | 36.5 | 29.3 | $18.95 |
| 13 | Claude Sonnet 4.6 | 32.6 | 29.6 | $31.73 |

## v1.1 Frontier

Undominated on composite cost vs. quality:

- Gemini 3.1 Pro
- GPT-5.5
- MiMo-V2.5-Pro

## Sources Used in v1.1

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
