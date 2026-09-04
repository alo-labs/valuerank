# ValueRank v1.4.0 Scores

**Updated:** September 4, 2026 · **Cohort:** 21 · **Retained dimensions:** 13 · **Cost mode:** AA + DeepSWE

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | Composite Cost |
|---:|---|---:|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 69.4 | 69.2 | 6 | 12.04 |
| 2 | GLM-5.3 Flash | 65.6 | 51.1 | 11 | 1.72 |
| 3 | GPT-5.6 Sol | 61.3 | 73.5 | 3 | 30.72 |
| 4 | GPT-6 Astra | 61.0 | 73.1 | 4 | 30.72 |
| 5 | Grok 4.6 | 60.8 | 61.2 | 8 | 15.06 |
| 6 | Claude Opus 5 | 59.9 | 79.0 | 1 | 57.58 |
| 7 | Kimi K3 | 59.6 | 74.2 | 2 | 31.03 |
| 8 | GLM-5.3 | 58.3 | 63.9 | 7 | 18.91 |
| 9 | Muse Spark 1.2 | 53.0 | 47.9 | 13 | 12.87 |
| 10 | Claude Fable 5 | 52.1 | 72.0 | 5 | 75.40 |
| 11 | Gemini 3.7 Flash | 50.8 | 36.3 | 15 | 6.39 |
| 12 | GPT-5.6 Luna | 49.8 | 30.6 | 17 | 2.75 |
| 13 | Qwen3.8 Max | 48.0 | 51.4 | 10 | 21.11 |
| 14 | DeepSeek V4 Pro | 44.9 | 32.1 | 16 | 8.82 |
| 15 | GPT-5.5 | 43.4 | 53.3 | 9 | 39.32 |
| 16 | Gemini 3.6 Flash | 40.1 | 23.1 | 20 | 7.96 |
| 17 | DeepSeek V4 Flash | 39.9 | 18.7 | 21 | 3.83 |
| 18 | Claude Opus 4.8 | 36.8 | 48.1 | 12 | 59.43 |
| 19 | GLM-5.2 | 34.8 | 26.2 | 19 | 15.16 |
| 20 | Gemini 3.5 Flash | 34.0 | 27.3 | 18 | 16.09 |
| 21 | Claude Sonnet 5 | 26.5 | 37.8 | 14 | 86.76 |

## Pareto frontier

Undominated on composite cost versus quality: **Gemini 3.8 Flash, Claude Opus 5, GPT-5.6 Sol, Kimi K3, GLM-5.3 Flash**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
| Cost | 29.76% | lower |
| Non-Hallucination | 7.14% | higher |
| Terminal-Bench v2.1 | 7.14% | higher |
| DeepSWE | 8.33% | higher |
| GDPval-AA v2 | 7.14% | higher |
| τ³-Banking | 5.95% | higher |
| AA-LCR | 4.76% | higher |
| AA-Omniscience Accuracy | 4.76% | higher |
| HLE | 4.76% | higher |
| GPQA Diamond | 4.76% | higher |
| SciCode | 4.76% | higher |
| CritPt | 3.57% | higher |
| AA Intelligence Index | 7.14% | higher |

## Normalized dimension matrix

Dimension order is the order in weights above:

[costComposite, omniNonHallucination, terminalBenchV21, deepswePassAt1, gdpvalV2, tau3Banking, aaLcr, omniAccuracy, hle, gpqaDiamond, scicode, critpt, intelligenceIndex]

| Rank | Model | Normalized dimensions |
|---:|---|---|
| 1 | Gemini 3.8 Flash | [70.0, 50.0, 85.0, 95.0, 25.0, 80.0, 85.0, 75.0, 75.0, 95.0, 52.5, 45.0, 65.0] |
| 2 | GLM-5.3 Flash | [100.0, 90.0, 60.0, 42.5, 95.0, 90.0, 60.0, 5.0, 15.0, 25.0, 0.0, 15.0, 55.0] |
| 3 | GPT-5.6 Sol | [32.5, 10.0, 90.0, 85.0, 70.0, 72.5, 55.0, 85.0, 85.0, 90.0, 72.5, 100.0, 85.0] |
| 4 | GPT-6 Astra | [32.5, 60.0, 97.5, 95.0, 55.0, 65.0, 10.0, 95.0, 90.0, 100.0, 10.0, 95.0, 90.0] |
| 5 | Grok 4.6 | [60.0, 100.0, 60.0, 60.0, 85.0, 72.5, 0.0, 30.0, 40.0, 80.0, 60.0, 32.5, 70.0] |
| 6 | Claude Opus 5 | [15.0, 40.0, 97.5, 95.0, 100.0, 60.0, 30.0, 90.0, 95.0, 70.0, 65.0, 90.0, 100.0] |
| 7 | Kimi K3 | [25.0, 55.0, 80.0, 72.5, 65.0, 85.0, 95.0, 45.0, 70.0, 80.0, 95.0, 75.0, 80.0] |
| 8 | GLM-5.3 | [45.0, 85.0, 50.0, 72.5, 90.0, 95.0, 35.0, 15.0, 45.0, 30.0, 85.0, 50.0, 75.0] |
| 9 | Muse Spark 1.2 | [65.0, 80.0, 30.0, 25.0, 60.0, 25.0, 100.0, 40.0, 60.0, 5.0, 80.0, 32.5, 45.0] |
| 10 | Claude Fable 5 | [5.0, 30.0, 72.5, 80.0, 80.0, 40.0, 42.5, 100.0, 100.0, 50.0, 100.0, 85.0, 95.0] |
| 11 | Gemini 3.7 Flash | [85.0, 25.0, 10.0, 50.0, 15.0, 30.0, 85.0, 70.0, 5.0, 40.0, 90.0, 0.0, 30.0] |
| 12 | GPT-5.6 Luna | [95.0, 5.0, 40.0, 60.0, 35.0, 5.0, 65.0, 35.0, 10.0, 17.5, 25.0, 60.0, 15.0] |
| 13 | Qwen3.8 Max | [40.0, 65.0, 45.0, 30.0, 75.0, 100.0, 17.5, 10.0, 55.0, 55.0, 35.0, 55.0, 60.0] |
| 14 | DeepSeek V4 Pro | [75.0, 0.0, 20.0, 42.5, 40.0, 55.0, 25.0, 55.0, 25.0, 62.5, 5.0, 40.0, 25.0] |
| 15 | GPT-5.5 | [20.0, 20.0, 60.0, 60.0, 10.0, 45.0, 72.5, 80.0, 65.0, 80.0, 72.5, 80.0, 40.0] |
| 16 | Gemini 3.6 Flash | [80.0, 45.0, 0.0, 10.0, 5.0, 0.0, 72.5, 60.0, 20.0, 62.5, 30.0, 5.0, 0.0] |
| 17 | DeepSeek V4 Flash | [90.0, 15.0, 20.0, 15.0, 30.0, 50.0, 17.5, 25.0, 0.0, 10.0, 15.0, 20.0, 5.0] |
| 18 | Claude Opus 4.8 | [10.0, 75.0, 72.5, 35.0, 45.0, 15.0, 5.0, 50.0, 80.0, 35.0, 45.0, 67.5, 50.0] |
| 19 | GLM-5.2 | [55.0, 95.0, 5.0, 5.0, 20.0, 20.0, 42.5, 0.0, 30.0, 0.0, 20.0, 67.5, 20.0] |
| 20 | Gemini 3.5 Flash | [50.0, 35.0, 20.0, 0.0, 0.0, 10.0, 85.0, 65.0, 50.0, 45.0, 40.0, 10.0, 10.0] |
| 21 | Claude Sonnet 5 | [0.0, 70.0, 35.0, 20.0, 50.0, 35.0, 50.0, 20.0, 35.0, 17.5, 52.5, 25.0, 35.0] |

## Coverage decision

The score is zero-gap across all retained dimensions. Speed is the only dropped candidate dimension: GPT-6 Astra has no numeric speed on its selected AA page, so it is kept as null rather than neutral-filled.
