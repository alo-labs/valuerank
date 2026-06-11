# ValueRank v0.9 Raw Data

**Version:** v0.9  
**Updated:** June 12, 2026

This file records the primary-source benchmark inputs explicitly refreshed for v0.9.

## DeepSWE

Source: [deepswe.datacurve.ai](https://deepswe.datacurve.ai/)

| Model | DeepSWE pass@1 | DeepSWE Avg Cost ($) |
|---|---:|
| GPT-5.5 | 70 | 6.61 |
| Claude Opus 4.8 | 58 | 12.58 |
| GPT-5.4 | 56 | 4.38 |
| Claude Opus 4.7 | 54 | 18.19 |
| Claude Sonnet 4.6 | 32 | 5.52 |
| Gemini 3.5 Flash | 28 | 7.42 |
| Claude Opus 4.6 | 28 | 5.39 |
| GPT-5.4 Mini | 24 | 2.08 |
| Kimi K2.6 | 24 | 3.16 |
| MiniMax M3 | 20 | 5.57 |
| MiMo-V2.5-Pro | 19 | 1.99 |
| GLM 5.1 | 18 | 7.46 |
| Gemini 3.1 Pro | 10 | 1.84 |
| DeepSeek V4-Pro | 8 | 4.22 |

Excluded:

- Grok-Build-0.1
- Gemini 3 Flash

## Terminal-Bench 2.1

Source: [tbench.ai leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.1)

| Model | Terminal-Bench 2.1 |
|---|---:|
| GPT-5.5 | 83.4 |
| Claude Opus 4.8 | 78.9 |
| Gemini 3.1 Pro | 70.7 |
| Claude Opus 4.7 | 69.7 |
| GLM 5.1 | 58.7 |

## IFBench

Source: [Ai2 IFBench / Artificial Analysis analysis](https://allenai.org/blog/ifbench-artificial-analysis)

| Model | IFBench |
|---|---:|
| Gemini 3.1 Pro | 77.1 |
| GPT-5.5 | 75.9 |
| GPT-5.4 | 73.9 |

## SWE-bench Verified

Source: [Vals SWE-bench Verified](https://www.vals.ai/benchmarks/swebench)

| Model | SWE-bench Verified |
|---|---:|
| Claude Opus 4.8 | 88.6 |
| GPT-5.5 | 82.6 |
| Claude Opus 4.7 | 82.0 |
| Gemini 3.1 Pro | 79.1 |
| Gemini 3.5 Flash | 78.8 |
| GPT-5.4 | 78.0 |
| Claude Opus 4.6 | 77.9 |
| Claude Sonnet 4.6 | 77.3 |
| GLM 5.1 | 76.6 |
| Kimi K2.6 | 76.1 |
| GPT-5.4 Mini | 73.2 |

## SWE-bench Pro

Source: [Scale SWE-bench Pro public leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public)

Family-level alias mapping used where the public leaderboard row includes only a reasoning-profile suffix.

| Ranked model | Source row | SWE-bench Pro |
|---|---|---:|
| GPT-5.4 | `gpt-5.4 (xHigh)*` | 59.10 |
| Claude Opus 4.6 | `claude-opus-4-6 (thinking)*` | 51.90 |
| Gemini 3.1 Pro | `gemini-3.1-pro (thinking)*` | 46.10 |

## OSWorld-Verified

Source: [OSWorld official benchmark site](https://os-world.github.io/) and its `osworld_verified_results.xlsx`

| Model | OSWorld-Verified |
|---|---:|
| MiniMax M3 | 75.19 |
| Kimi K2.6 | 73.06 |

## Artificial Analysis evaluation refresh

Sources:

- [GPQA Diamond](https://artificialanalysis.ai/evaluations/gpqa-diamond)
- [Humanity's Last Exam](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
- [SciCode](https://artificialanalysis.ai/evaluations/scicode)
- [Artificial Analysis Long Context Reasoning](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning)
- [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience)

Family-level alias mapping used where the public leaderboard row includes a benchmark-profile suffix.

### GPQA Diamond

| Ranked model | Source row | GPQA |
|---|---|---:|
| Gemini 3.1 Pro | `Gemini 3.1 Pro Preview` | 94.14 |
| GPT-5.5 | `GPT-5.5 (xhigh)` | 93.54 |
| MiniMax M3 | `MiniMax-M3` | 92.93 |
| Gemini 3.5 Flash | `Gemini 3.5 Flash` | 92.22 |
| Claude Opus 4.8 | `Claude Opus 4.8 (max)` | 92.02 |
| Kimi K2.6 | `Kimi K2.6` | 91.11 |
| DeepSeek V4-Pro | `DeepSeek V4 Pro (Max)` | 88.79 |
| Claude Sonnet 4.6 | `Claude Sonnet 4.6 (max)` | 87.47 |
| GPT-5.4 Mini | `GPT-5.4 mini (xhigh)` | 87.47 |
| GLM 5.1 | `GLM-5.1` | 86.77 |

### HLE

| Ranked model | Source row | HLE |
|---|---|---:|
| Claude Opus 4.8 | `Claude Opus 4.8 (max)` | 45.74 |
| Gemini 3.1 Pro | `Gemini 3.1 Pro Preview` | 44.72 |
| GPT-5.5 | `GPT-5.5 (xhigh)` | 44.30 |
| Gemini 3.5 Flash | `Gemini 3.5 Flash` | 40.96 |
| MiniMax M3 | `MiniMax-M3` | 37.12 |
| Kimi K2.6 | `Kimi K2.6` | 35.91 |
| DeepSeek V4-Pro | `DeepSeek V4 Pro (Max)` | 35.87 |
| MiMo-V2.5-Pro | `MiMo-V2.5-Pro` | 33.78 |
| Claude Sonnet 4.6 | `Claude Sonnet 4.6 (max)` | 29.98 |
| GLM 5.1 | `GLM-5.1` | 28.04 |
| GPT-5.4 Mini | `GPT-5.4 mini (xhigh)` | 26.65 |

### SciCode

| Ranked model | Source row | SciCode |
|---|---|---:|
| Gemini 3.1 Pro | `Gemini 3.1 Pro Preview` | 58.91 |
| GPT-5.4 | `GPT-5.4 (xhigh)` | 56.60 |
| GPT-5.5 | `GPT-5.5 (xhigh)` | 56.13 |
| Claude Opus 4.8 | `Claude Opus 4.8 (max)` | 53.47 |
| Kimi K2.6 | `Kimi K2.6` | 53.47 |
| Gemini 3.5 Flash | `Gemini 3.5 Flash` | 53.12 |
| MiMo-V2.5-Pro | `MiMo-V2.5-Pro` | 50.23 |
| DeepSeek V4-Pro | `DeepSeek V4 Pro (Max)` | 50.00 |
| GPT-5.4 Mini | `GPT-5.4 mini (xhigh)` | 49.88 |
| Claude Sonnet 4.6 | `Claude Sonnet 4.6 (max)` | 46.76 |
| MiniMax M3 | `MiniMax-M3` | 45.37 |
| GLM 5.1 | `GLM-5.1` | 43.75 |

### RULER / LCR

| Ranked model | Source row | LCR |
|---|---|---:|
| GPT-5.5 | `GPT-5.5 (xhigh)` | 74.33 |
| MiniMax M3 | `MiniMax-M3` | 74.00 |
| MiMo-V2.5-Pro | `MiMo-V2.5-Pro` | 73.33 |
| Gemini 3.1 Pro | `Gemini 3.1 Pro Preview` | 72.67 |
| Claude Sonnet 4.6 | `Claude Sonnet 4.6 (max)` | 70.67 |
| Kimi K2.6 | `Kimi K2.6` | 69.67 |
| Gemini 3.5 Flash | `Gemini 3.5 Flash` | 69.33 |
| GPT-5.4 Mini | `GPT-5.4 mini (xhigh)` | 69.33 |
| Claude Opus 4.8 | `Claude Opus 4.8 (max)` | 67.67 |
| DeepSeek V4-Pro | `DeepSeek V4 Pro (Max)` | 66.33 |

### AA-Omniscience

v0.9 uses two Omniscience metrics:

- **AA-Omniscience Index** at 1% weight, higher is better.
- **AA-Omniscience Hallucination Rate** at 6% weight, lower is better.

The hallucination-rate weight is transferred from IFBench, reducing IFBench from 18% to 12%.

| Ranked model | Source row | AA-Omniscience Index | Hallucination Rate |
|---|---|---:|---:|
| Gemini 3.1 Pro | `Gemini 3.1 Pro Preview` | 32.93 | 49.87% |
| MiniMax M3 | `MiniMax-M3` | 1.37 | 16.08% |
| MiMo-V2.5-Pro | `MiMo-V2.5-Pro` | 3.60 | 24.55% |
| DeepSeek V4-Pro | `DeepSeek V4 Pro (Reasoning, Max Effort)` | -10.02 | 93.98% |
| GPT-5.5 | `GPT-5.5 (xhigh)` | 20.07 | 85.53% |
| Gemini 3.5 Flash | `Gemini 3.5 Flash (high)` | 22.68 | 60.69% |
| Claude Opus 4.8 | `Claude Opus 4.8 (Adaptive Reasoning, Max Effort)` | 27.43 | 35.89% |
| Kimi K2.6 | `Kimi K2.6` | 6.42 | 39.26% |
| GLM 5.1 | `GLM-5.1 (Reasoning)` | 1.93 | 29.38% |
| GPT-5.4 Mini | `GPT-5.4 mini (xhigh)` | -18.68 | 89.79% |
| Claude Sonnet 4.6 | `Claude Sonnet 4.6 (Adaptive Reasoning, Max Effort)` | 12.37 | 46.14% |
| GPT-5.4 | `GPT-5.4 (xhigh)` | 5.65 | 88.64% |
| Claude Opus 4.7 | `Claude Opus 4.7 (Adaptive Reasoning, Max Effort)` | 26.17 | 36.18% |
| Claude Opus 4.6 | `Claude Opus 4.6 (Adaptive Reasoning, Max Effort)` | 13.50 | 61.33% |

## Artificial Analysis model-page refresh

Current model-page refreshes used for eval cost, speed, and index:

| Model | Eval Cost ($) | Speed (tok/s) | AA Index |
|---|---:|---:|---:|
| GPT-5.5 | 3357.00 | 49 | 60 |
| Claude Opus 4.8 | 4685.85 | 60 | 61 |
| GPT-5.4 | 2851.01 | 82 | 57 |
| Claude Opus 4.7 | 5117.14 | 44 | 57 |
| Claude Sonnet 4.6 | 1694.19 | 42 | 44 |
| Gemini 3.5 Flash | 1551.60 | 145 | 55 |
| Claude Opus 4.6 | 1745.71 | 37 | 46 |
| GPT-5.4 Mini | 1353.87 | 150 | 49 |
| Kimi K2.6 | 947.87 | 57 | 54 |
| MiniMax M3 | 308.34 | 42 | 55 |
| MiMo-V2.5-Pro | 160.82 | 38 | 54 |
| GLM 5.1 | 543.95 | 74 | 51 |
| Gemini 3.1 Pro | 892.28 | 110 | 57 |
| DeepSeek V4-Pro | 267.82 | 45 | 52 |

## Composite cost construction

v0.9 no longer feeds raw Artificial Analysis eval cost directly into the `Cost` dimension.

Instead:

- `AA Cost (0-100)` normalizes current AA eval cost across the ranked DeepSWE cohort, with the highest-cost model set to `100`
- `DeepSWE Cost (0-100)` normalizes current DeepSWE average cost per task across the ranked DeepSWE cohort, with the highest-cost model set to `100`
- `Composite Cost (0-100)` averages those two penalty terms back onto a single `0-100` scale

| Model | AA Cost (0-100) | DeepSWE Cost (0-100) | Composite Cost (0-100) |
|---|---:|---:|---:|
| GPT-5.5 | 65.60 | 36.34 | 50.97 |
| Claude Opus 4.8 | 91.57 | 69.16 | 80.37 |
| GPT-5.4 | 55.71 | 24.08 | 39.90 |
| Claude Opus 4.7 | 100.00 | 100.00 | 100.00 |
| Claude Sonnet 4.6 | 33.11 | 30.35 | 31.73 |
| Gemini 3.5 Flash | 30.32 | 40.79 | 35.56 |
| Claude Opus 4.6 | 34.11 | 29.63 | 31.87 |
| GPT-5.4 Mini | 26.46 | 11.43 | 18.95 |
| Kimi K2.6 | 18.52 | 17.37 | 17.95 |
| MiniMax M3 | 6.03 | 30.62 | 18.32 |
| MiMo-V2.5-Pro | 3.14 | 10.94 | 7.04 |
| GLM 5.1 | 10.63 | 41.01 | 25.82 |
| Gemini 3.1 Pro | 17.44 | 10.12 | 13.78 |
| DeepSeek V4-Pro | 5.23 | 23.20 | 14.22 |

## Remaining neutral-only dimensions in v0.9

The following ValueRank dimensions remain in the schema and weights, but no current source-audited model rows were usable for the DeepSWE-constrained cohort in v0.9:

- LiveCodeBench v4
- Tau2-Bench
- BrowseComp
- MMLU-Pro
- AIME 2025

These dimensions therefore still contribute neutral 50.0 where no exact or allowed family-level alias row exists.
