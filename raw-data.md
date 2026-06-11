# ValueRank v1.0 Raw Data

**Version:** v1.0  
**Updated:** June 12, 2026

v1.0 keeps only dimensions with full 14-model coverage.

## Primary Sources

- [DeepSWE](https://deepswe.datacurve.ai/) for `DeepSWE pass@1` and `DeepSWE Avg Cost ($)`
- Artificial Analysis model pages for:
  - `IFBench`
  - `GDPval-AA`
  - `Terminal-Bench Hard`
  - `τ²-Bench Telecom`
  - `AA-LCR`
  - `AA-Omniscience Accuracy`
  - `AA-Omniscience Non-Hallucination Rate`
  - `Humanity's Last Exam`
  - `GPQA Diamond`
  - `SciCode`
  - `CritPt`
  - `Artificial Analysis Intelligence Index`
  - `Speed`
  - `Eval Cost`

## Artificial Analysis model-page reconstruction

For the 11 current Artificial Analysis benchmark dimensions retained in v1.0:

- 13 cohort rows were visible on the current `GPT-5.5 (xhigh)` model page
- the missing `GPT-5.4 mini (xhigh)` row was filled from its own current model page

This preserves primary-source provenance while eliminating benchmark gaps.

## IFBench

| Model | IFBench |
|---|---:|
| GPT-5.5 | 76 |
| Claude Opus 4.8 | 62 |
| GPT-5.4 | 74 |
| Claude Opus 4.7 | 59 |
| Claude Sonnet 4.6 | 57 |
| Gemini 3.5 Flash | 76 |
| Claude Opus 4.6 | 53 |
| GPT-5.4 Mini | 73 |
| Kimi K2.6 | 76 |
| MiniMax M3 | 83 |
| MiMo-V2.5-Pro | 80 |
| GLM 5.1 | 76 |
| Gemini 3.1 Pro | 77 |
| DeepSeek V4-Pro | 76 |

## AA-Omniscience

| Model | Accuracy | Non-Hallucination Rate | Hallucination Rate |
|---|---:|---:|---:|
| GPT-5.5 | 57 | 14 | 86 |
| Claude Opus 4.8 | 47 | 64 | 36 |
| GPT-5.4 | 50 | 11 | 89 |
| Claude Opus 4.7 | 46 | 64 | 36 |
| Claude Sonnet 4.6 | 40 | 54 | 46 |
| Gemini 3.5 Flash | 52 | 39 | 61 |
| Claude Opus 4.6 | 46 | 39 | 61 |
| GPT-5.4 Mini | 37 | 10 | 90 |
| Kimi K2.6 | 33 | 61 | 39 |
| MiniMax M3 | 15 | 84 | 16 |
| MiMo-V2.5-Pro | 23 | 75 | 25 |
| GLM 5.1 | 24 | 71 | 29 |
| Gemini 3.1 Pro | 55 | 50 | 50 |
| DeepSeek V4-Pro | 43 | 6 | 94 |

## DeepSWE

| Model | DeepSWE pass@1 | DeepSWE Avg Cost ($) |
|---|---:|---:|
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

## Agentic / reasoning benchmarks

| Model | GDPval-AA | Terminal-Bench Hard | τ²-Bench Telecom | AA-LCR | HLE | GPQA | SciCode | CritPt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.5 | 63 | 61 | 94 | 74 | 44 | 94 | 56 | 27 |
| Claude Opus 4.8 | 69 | 58 | 94 | 68 | 46 | 92 | 53 | 21 |
| GPT-5.4 | 59 | 58 | 87 | 74 | 42 | 92 | 57 | 23 |
| Claude Opus 4.7 | 63 | 52 | 89 | 70 | 40 | 91 | 55 | 12 |
| Claude Sonnet 4.6 | 59 | 53 | 76 | 71 | 30 | 87 | 47 | 3 |
| Gemini 3.5 Flash | 58 | 41 | 95 | 69 | 41 | 92 | 53 | 13 |
| Claude Opus 4.6 | 56 | 46 | 92 | 71 | 37 | 90 | 52 | 13 |
| GPT-5.4 Mini | 47 | 52 | 83 | 69 | 27 | 87 | 50 | 10 |
| Kimi K2.6 | 49 | 44 | 96 | 70 | 36 | 91 | 53 | 8 |
| MiniMax M3 | 58 | 42 | 89 | 74 | 37 | 93 | 45 | 4 |
| MiMo-V2.5-Pro | 54 | 43 | 94 | 73 | 34 | 87 | 50 | 4 |
| GLM 5.1 | 52 | 43 | 98 | 62 | 28 | 87 | 44 | 5 |
| Gemini 3.1 Pro | 41 | 54 | 96 | 73 | 45 | 94 | 59 | 18 |
| DeepSeek V4-Pro | 53 | 46 | 96 | 66 | 36 | 89 | 50 | 13 |

## Artificial Analysis model-page refresh

| Model | Eval Cost ($) | Speed (tok/s) | AA Index |
|---|---:|---:|---:|
| GPT-5.5 | 3357.00 | 50.1 | 60 |
| Claude Opus 4.8 | 4685.85 | 58.7 | 61 |
| GPT-5.4 | 2851.01 | 82.0 | 57 |
| Claude Opus 4.7 | 5117.14 | 43.8 | 57 |
| Claude Sonnet 4.6 | 1694.19 | 42.4 | 44 |
| Gemini 3.5 Flash | 1551.60 | 144.8 | 55 |
| Claude Opus 4.6 | 1745.71 | 36.9 | 46 |
| GPT-5.4 Mini | 1353.87 | 147.8 | 49 |
| Kimi K2.6 | 947.87 | 60.1 | 54 |
| MiniMax M3 | 308.34 | 42.6 | 55 |
| MiMo-V2.5-Pro | 160.82 | 38.9 | 54 |
| GLM 5.1 | 543.95 | 74.7 | 51 |
| Gemini 3.1 Pro | 892.28 | 109.8 | 57 |
| DeepSeek V4-Pro | 267.82 | 44.8 | 52 |

## Composite cost construction

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
