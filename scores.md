# ValueRank v1.4.0 Scores

**Updated:** September 5, 2026 · **Cohort:** 21 · **Retained dimensions:** 12 · **Cost mode:** AA + DeepSWE

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | Composite Cost |
|---:|---|---:|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 68.2 | 67.4 | 6 | 12.04 |
| 2 | GLM-5.3 Flash | 66.1 | 50.0 | 11 | 1.72 |
| 3 | Grok 4.6 | 60.9 | 61.3 | 8 | 15.06 |
| 4 | GPT-5.6 Sol | 59.1 | 71.7 | 4 | 30.72 |
| 5 | GLM-5.3 | 58.9 | 65.5 | 7 | 18.91 |
| 6 | GPT-6 Astra | 58.2 | 70.3 | 5 | 30.72 |
| 7 | Kimi K3 | 58.0 | 73.5 | 2 | 31.03 |
| 8 | Claude Opus 5 | 57.1 | 76.9 | 1 | 57.58 |
| 9 | Muse Spark 1.2 | 54.8 | 50.0 | 12 | 12.87 |
| 10 | Gemini 3.7 Flash | 53.9 | 39.2 | 14 | 6.39 |
| 11 | GPT-5.6 Luna | 50.5 | 29.5 | 17 | 2.75 |
| 12 | Claude Fable 5 | 50.5 | 72.0 | 3 | 75.40 |
| 13 | Qwen3.8 Max | 48.3 | 52.2 | 10 | 21.11 |
| 14 | DeepSeek V4 Pro | 46.8 | 33.4 | 16 | 8.82 |
| 15 | Gemini 3.6 Flash | 43.1 | 25.8 | 20 | 7.96 |
| 16 | GPT-5.5 | 42.1 | 52.5 | 9 | 39.32 |
| 17 | DeepSeek V4 Flash | 41.5 | 18.6 | 21 | 3.83 |
| 18 | GLM-5.2 | 37.1 | 28.6 | 18 | 15.16 |
| 19 | Gemini 3.5 Flash | 35.1 | 28.1 | 19 | 16.09 |
| 20 | Claude Opus 4.8 | 34.0 | 45.3 | 13 | 59.43 |
| 21 | Claude Sonnet 5 | 25.9 | 38.1 | 15 | 86.76 |

## Pareto frontier

Undominated on composite cost versus quality: **Gemini 3.8 Flash, Claude Opus 5, GPT-5.6 Sol, Kimi K3, GLM-5.3 Flash**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
| Cost | 32.05% | lower |
| Non-Hallucination | 7.69% | higher |
| DeepSWE | 8.97% | higher |
| GDPval-AA v2 | 7.69% | higher |
| τ³-Banking | 6.41% | higher |
| AA-LCR | 5.13% | higher |
| AA-Omniscience Accuracy | 5.13% | higher |
| HLE | 5.13% | higher |
| GPQA Diamond | 5.13% | higher |
| SciCode | 5.13% | higher |
| CritPt | 3.85% | higher |
| AA Intelligence Index | 7.69% | higher |

## Normalized dimension matrix

Dimension order is the order in weights above:

[costComposite, omniNonHallucination, deepswePassAt1, gdpvalV2, tau3Banking, aaLcr, omniAccuracy, hle, gpqaDiamond, scicode, critpt, intelligenceIndex]

| Rank | Model | Normalized dimensions |
|---:|---|---|
| 1 | Gemini 3.8 Flash | [70.0, 50.0, 95.0, 25.0, 80.0, 85.0, 75.0, 75.0, 95.0, 52.5, 45.0, 65.0] |
| 2 | GLM-5.3 Flash | [100.0, 90.0, 42.5, 95.0, 90.0, 60.0, 5.0, 15.0, 25.0, 0.0, 15.0, 55.0] |
| 3 | Grok 4.6 | [60.0, 100.0, 60.0, 85.0, 72.5, 0.0, 30.0, 40.0, 80.0, 60.0, 32.5, 70.0] |
| 4 | GPT-5.6 Sol | [32.5, 10.0, 85.0, 70.0, 72.5, 55.0, 85.0, 85.0, 90.0, 72.5, 100.0, 85.0] |
| 5 | GLM-5.3 | [45.0, 85.0, 72.5, 90.0, 95.0, 35.0, 15.0, 45.0, 30.0, 85.0, 50.0, 75.0] |
| 6 | GPT-6 Astra | [32.5, 60.0, 95.0, 55.0, 65.0, 10.0, 95.0, 90.0, 100.0, 10.0, 95.0, 90.0] |
| 7 | Kimi K3 | [25.0, 55.0, 72.5, 65.0, 85.0, 95.0, 45.0, 70.0, 80.0, 95.0, 75.0, 80.0] |
| 8 | Claude Opus 5 | [15.0, 40.0, 95.0, 100.0, 60.0, 30.0, 90.0, 95.0, 70.0, 65.0, 90.0, 100.0] |
| 9 | Muse Spark 1.2 | [65.0, 80.0, 25.0, 60.0, 25.0, 100.0, 40.0, 60.0, 5.0, 80.0, 32.5, 45.0] |
| 10 | Gemini 3.7 Flash | [85.0, 25.0, 50.0, 15.0, 30.0, 85.0, 70.0, 5.0, 40.0, 90.0, 0.0, 30.0] |
| 11 | GPT-5.6 Luna | [95.0, 5.0, 60.0, 35.0, 5.0, 65.0, 35.0, 10.0, 17.5, 25.0, 60.0, 15.0] |
| 12 | Claude Fable 5 | [5.0, 30.0, 80.0, 80.0, 40.0, 42.5, 100.0, 100.0, 50.0, 100.0, 85.0, 95.0] |
| 13 | Qwen3.8 Max | [40.0, 65.0, 30.0, 75.0, 100.0, 17.5, 10.0, 55.0, 55.0, 35.0, 55.0, 60.0] |
| 14 | DeepSeek V4 Pro | [75.0, 0.0, 42.5, 40.0, 55.0, 25.0, 55.0, 25.0, 62.5, 5.0, 40.0, 25.0] |
| 15 | Gemini 3.6 Flash | [80.0, 45.0, 10.0, 5.0, 0.0, 72.5, 60.0, 20.0, 62.5, 30.0, 5.0, 0.0] |
| 16 | GPT-5.5 | [20.0, 20.0, 60.0, 10.0, 45.0, 72.5, 80.0, 65.0, 80.0, 72.5, 80.0, 40.0] |
| 17 | DeepSeek V4 Flash | [90.0, 15.0, 15.0, 30.0, 50.0, 17.5, 25.0, 0.0, 10.0, 15.0, 20.0, 5.0] |
| 18 | GLM-5.2 | [55.0, 95.0, 5.0, 20.0, 20.0, 42.5, 0.0, 30.0, 0.0, 20.0, 67.5, 20.0] |
| 19 | Gemini 3.5 Flash | [50.0, 35.0, 0.0, 0.0, 10.0, 85.0, 65.0, 50.0, 45.0, 40.0, 10.0, 10.0] |
| 20 | Claude Opus 4.8 | [10.0, 75.0, 35.0, 45.0, 15.0, 5.0, 50.0, 80.0, 35.0, 45.0, 67.5, 50.0] |
| 21 | Claude Sonnet 5 | [0.0, 70.0, 20.0, 50.0, 35.0, 50.0, 20.0, 35.0, 17.5, 52.5, 25.0, 35.0] |

## Coverage decision

The score is zero-gap across all retained dimensions. The dropped candidate dimensions are listed below with their missing cohort rows; their values remain null rather than being replaced by a neutral score.

## External benchmark supplements

LiveBench provides the four-task Instruction Following view and the Overall Score versus Cost Per Successful Task Pareto analysis; Terminal-Bench 4.0 provides the current standalone terminal-agent leaderboard. Their incomplete cohort coverage keeps them supplemental rather than weighted into this zero-gap ranking. See [raw-data.md](raw-data.md) for the source-backed tables.
