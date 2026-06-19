# ValueRank v1.2 Raw Data

**Version:** v1.2
**Updated:** June 20, 2026

v1.2 keeps only dimensions with full 8-model coverage after shrinking the cohort from 13 to 8 current DeepSWE-listed models.

## Primary Sources

- [DeepSWE](https://deepswe.datacurve.ai/) for `DeepSWE pass@1` and `DeepSWE Avg Cost ($)`
- Artificial Analysis model pages for:
  - `IFBench`
  - `GDPval-AA v2` (uses `gdpval_normalized` × 100; the older raw-points scale used in v1.1 was retired)
  - `Terminal-Bench v2.1` (reported as `Terminal-Bench Hard`)
  - `τ²-Bench Telecom`
  - `AA-LCR`
  - `AA-Omniscience Accuracy`
  - `AA-Omniscience Hallucination Rate`
  - `Humanity's Last Exam`
  - `GPQA Diamond`
  - `SciCode`
  - `CritPt`
  - `Artificial Analysis Intelligence Index v4.1`
  - `Speed`
  - `Eval Cost`

## Artificial Analysis model-page reconstruction

For the 11 current Artificial Analysis benchmark dimensions retained in v1.2:

- 7 cohort rows were visible on the current `GPT-5.5 (xhigh)` model page.
- The missing `Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)` row was filled from its own current model page at `/models/claude-fable-5`.
- For Gemini 3.5 Flash, the AA `(high)` variant was used because the `(medium)` variant does not publish GDPval-AA v2, AA Intelligence Index v4.1, or a complete Terminal-Bench Hard v2.1 score, which would break zero-gap.

This preserves primary-source provenance while eliminating benchmark gaps.

## IFBench

| Model | IFBench |
|---|---:|
| GPT-5.5 | 76 |
| Claude Fable 5 | 63 |
| Claude Opus 4.8 | 62 |
| GPT-5.4 | 74 |
| Claude Sonnet 4.6 | 57 |
| Gemini 3.5 Flash | 76 |
| Kimi K2.7 | 63 |
| Gemini 3.1 Pro | 77 |

## AA-Omniscience

| Model | Accuracy | Non-Hallucination Rate | Hallucination Rate |
|---|---:|---:|---:|
| GPT-5.5 | 52 | 20 | 80 |
| Claude Fable 5 | 61 | 59 | 41 |
| Claude Opus 4.8 | 37 | 82 | 18 |
| GPT-5.4 | 41 | 15 | 85 |
| Claude Sonnet 4.6 | 30 | 73 | 27 |
| Gemini 3.5 Flash | 57 | 43 | 57 |
| Kimi K2.7 | 23 | 25 | 75 |
| Gemini 3.1 Pro | 61 | 62 | 38 |

## DeepSWE

| Model | DeepSWE pass@1 | DeepSWE Avg Cost ($) |
|---|---:|---:|
| GPT-5.5 | 67 | 7.23 |
| Claude Fable 5 | 70 | 13.41 |
| Claude Opus 4.8 | 59 | 13.22 |
| GPT-5.4 | 52 | 5.65 |
| Claude Sonnet 4.6 | 30 | 5.52 |
| Gemini 3.5 Flash | 37 | 7.34 |
| Kimi K2.7 | 31 | 2.82 |
| Gemini 3.1 Pro | 12 | 9.48 |

## Agentic / reasoning benchmarks

| Model | GDPval-AA | Terminal-Bench Hard | τ²-Bench Telecom | AA-LCR | HLE | GPQA | SciCode | CritPt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.5 | 50 | 61 | 94 | 74 | 44 | 94 | 56 | 27 |
| Claude Fable 5 | 64 | 63 | 99 | 70 | 53 | 93 | 60 | 29 |
| Claude Opus 4.8 | 56 | 58 | 94 | 68 | 46 | 92 | 53 | 21 |
| GPT-5.4 | 45 | 58 | 87 | 74 | 42 | 92 | 57 | 23 |
| Claude Sonnet 4.6 | 45 | 53 | 76 | 71 | 30 | 87 | 47 | 3 |
| Gemini 3.5 Flash | 43 | 41 | 95 | 69 | 41 | 92 | 53 | 13 |
| Kimi K2.7 | 35 | 45 | 90 | 66 | 33 | 90 | 47 | 10 |
| Gemini 3.1 Pro | 24 | 54 | 96 | 73 | 45 | 94 | 59 | 18 |

## Artificial Analysis model-page refresh

| Model | Eval Cost ($) | Speed (tok/s) | AA Index |
|---|---:|---:|---:|
| GPT-5.5 | 2588.36 | 58.3 | 55 |
| Claude Fable 5 | 6227.74 | 0.0 | 60 |
| Claude Opus 4.8 | 4011.58 | 58.8 | 56 |
| GPT-5.4 | 2261.30 | 146.5 | 51 |
| Claude Sonnet 4.6 | 3355.85 | 53.6 | 47 |
| Gemini 3.5 Flash | 1141.63 | 159.2 | 50 |
| Kimi K2.7 | 530.36 | 55.8 | 42 |
| Gemini 3.1 Pro | 859.81 | 122.8 | 46 |

Note: Claude Fable 5 speed is reported as 0.0 by Artificial Analysis — likely too new for reliable speed measurement. This drives Fable 5 to the bottom of the Speed dimension in the normalized ranking. Recheck on next AA refresh.

## Composite cost construction

| Model | AA Cost (0-100) | DeepSWE Cost (0-100) | Composite Cost (0-100) |
|---|---:|---:|---:|
| GPT-5.5 | 41.56 | 53.87 | 47.72 |
| Claude Fable 5 | 100.00 | 100.00 | 100.00 |
| Claude Opus 4.8 | 64.41 | 98.57 | 81.49 |
| GPT-5.4 | 36.31 | 42.14 | 39.22 |
| Claude Sonnet 4.6 | 53.89 | 41.17 | 47.53 |
| Gemini 3.5 Flash | 18.33 | 54.73 | 36.53 |
| Kimi K2.7 | 8.52 | 20.99 | 14.75 |
| Gemini 3.1 Pro | 13.81 | 70.68 | 42.24 |

## Official-first excluded benchmark audit

These benchmarks were re-checked during the v1.2 official-first audit and remain excluded because no currently published implementation contains all 8 ranked ValueRank models:

| Benchmark | Official source outcome | Best current secondary outcome |
|---|---|---|
| APEX-Agents | [Mercor official leaderboard](https://www.mercor.com/apex/apex-agents-leaderboard/) still misses `Claude Fable 5`, `Kimi K2.7 Code`, `Claude Opus 4.8`, and `Claude Sonnet 4.6` from the v1.2 cohort | [Artificial Analysis APEX-Agents-AA](https://artificialanalysis.ai/evaluations/apex-agents-aa) covers 5 of 8 — still missing `Claude Fable 5`, `Claude Opus 4.8`, and `Kimi K2.7 Code` |
| ITBench | [IBM Research ITBench Kaggle benchmark](https://www.kaggle.com/benchmarks/ibm-research/itbench) does not contain any of the 8 exact ValueRank model names | [Artificial Analysis ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) remains incomplete |
| MMMU-Pro | [MMMU benchmark site](https://mmmu-benchmark.github.io/) is the original paper-era leaderboard and does not contain the current 8-model cohort | [Artificial Analysis MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro) and [LLM Stats MMMU-Pro](https://llm-stats.com/benchmarks/mmmu-pro) remain incomplete |
| MMLU-Pro | [TIGER-Lab official leaderboard](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) does not contain the current 8-model cohort | [Kaggle MMLU-Pro](https://www.kaggle.com/benchmarks/open-benchmarks/mmlu-pro) and [LLM Stats MMLU-Pro](https://llm-stats.com/benchmarks/mmlu-pro) remain incomplete |
| LiveCodeBench | [LiveCodeBench official site](https://livecodebench.github.io/) is still the original paper-era leaderboard and does not contain the current 8-model cohort | [Kaggle LiveCodeBench](https://www.kaggle.com/benchmarks/open-benchmarks/livecodebench), [Artificial Analysis LiveCodeBench](https://artificialanalysis.ai/evaluations/livecodebench), and [LLM Stats LiveCodeBench](https://llm-stats.com/benchmarks/livecodebench) remain incomplete |
| Global-MMLU-Lite | [Cohere Labs Global-MMLU-Lite Kaggle benchmark](https://www.kaggle.com/benchmarks/cohere-labs/global-mmlu-lite) does not contain the current 8-model cohort | Secondary implementations remain incomplete as well |
| AIME 2025 | The benchmark owner publishes the exam itself, not a current frontier-model leaderboard | [Kaggle AIME 2025](https://www.kaggle.com/benchmarks/open-benchmarks/aime-2025) and [Artificial Analysis AIME 2025](https://artificialanalysis.ai/evaluations/aime-2025) remain incomplete |
| MATH-500 | The benchmark owner publishes the dataset and benchmark definition, not a current frontier-model leaderboard | [Kaggle MATH-500](https://www.kaggle.com/benchmarks/open-benchmarks/math-500) is the strongest current alternative but still covers only a subset of the 8-model cohort |
