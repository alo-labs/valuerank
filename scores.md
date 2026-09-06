# ValueRank v1.5.0 Scores

**Updated:** September 6, 2026 · **Cohort:** 21 · **Retained dimensions:** 12 · **Cost mode:** DeepSWE-only

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | Composite Cost |
|---:|---|---:|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 68.5 | 67.9 | 5 | 8.94 |
| 2 | Grok 4.6 | 64.1 | 64.9 | 6 | 13.07 |
| 3 | GLM-5.3 Flash | 63.8 | 47.0 | 12 | 0.91 |
| 4 | GPT-6 Astra | 59.4 | 75.3 | 1 | 24.70 |
| 5 | GPT-5.6 Sol | 59.1 | 72.6 | 2 | 24.47 |
| 6 | Gemini 3.7 Flash | 58.9 | 49.2 | 10 | 7.69 |
| 7 | GLM-5.3 | 54.9 | 61.8 | 8 | 15.11 |
| 8 | Kimi K3 | 54.6 | 63.7 | 7 | 17.61 |
| 9 | GPT-5.6 Luna | 53.1 | 36.0 | 17 | 2.31 |
| 10 | Claude Opus 5 | 53.1 | 70.7 | 3 | 44.85 |
| 11 | DeepSeek V4 Pro | 52.1 | 36.8 | 16 | 6.33 |
| 12 | Muse Spark 1.2 | 49.5 | 46.9 | 13 | 14.02 |
| 13 | Claude Fable 5 | 48.6 | 68.8 | 4 | 50.80 |
| 14 | Qwen3.8 Max | 48.3 | 47.5 | 11 | 14.13 |
| 15 | DeepSeek V4 Flash | 47.7 | 25.7 | 20 | 1.74 |
| 16 | Gemini 3.6 Flash | 42.8 | 28.0 | 19 | 8.37 |
| 17 | GPT-5.5 | 42.2 | 52.5 | 9 | 27.39 |
| 18 | Gemini 3.5 Flash | 36.0 | 23.7 | 21 | 13.07 |
| 19 | GLM-5.2 | 33.8 | 28.7 | 18 | 14.85 |
| 20 | Claude Opus 4.8 | 32.4 | 42.8 | 14 | 50.08 |
| 21 | Claude Sonnet 5 | 27.0 | 39.5 | 15 | 100.00 |

## Pareto frontier

Undominated on composite cost versus quality: **GPT-6 Astra, Gemini 3.8 Flash, GPT-5.6 Sol, Gemini 3.7 Flash, GLM-5.3 Flash**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
| Cost | 31.65% | lower |
| Non-Hallucination | 7.59% | higher |
| DeepSWE | 8.86% | higher |
| [GDPval-AA v2](https://artificialanalysis.ai/evaluations/gdpval-aa) | 7.59% | higher |
| [τ³-Banking](https://artificialanalysis.ai/evaluations/tau3-banking) | 6.33% | higher |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 5.06% | higher |
| [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 5.06% | higher |
| [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 5.06% | higher |
| [GPQA Diamond (legacy)](https://artificialanalysis.ai/evaluations/gpqa-diamond) | 5.06% | higher |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 3.80% | higher |
| [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 7.59% | higher |
| Speed | 6.33% | higher |

## Normalized dimension matrix

Dimension order is the order in weights above:

[costComposite, omniNonHallucination, deepswePassAt1, gdpvalV2, tau3Banking, aaLcr, omniAccuracy, hle, gpqaDiamond, critpt, intelligenceIndex, speed]

| Rank | Model | Normalized dimensions |
|---:|---|---|
| 1 | Gemini 3.8 Flash | [70.0, 50.0, 95.0, 25.0, 75.0, 65.0, 70.0, 70.0, 95.0, 45.0, 65.0, 90.0] |
| 2 | Grok 4.6 | [62.5, 80.0, 60.0, 85.0, 95.0, 57.5, 45.0, 45.0, 90.0, 30.0, 80.0, 20.0] |
| 3 | GLM-5.3 Flash | [100.0, 95.0, 42.5, 90.0, 85.0, 45.0, 5.0, 10.0, 25.0, 15.0, 45.0, 10.0] |
| 4 | GPT-6 Astra | [25.0, 60.0, 95.0, 60.0, 65.0, 45.0, 95.0, 90.0, 100.0, 95.0, 100.0, 30.0] |
| 5 | GPT-5.6 Sol | [30.0, 10.0, 85.0, 70.0, 70.0, 90.0, 85.0, 85.0, 80.0, 100.0, 85.0, 65.0] |
| 6 | Gemini 3.7 Flash | [80.0, 25.0, 50.0, 20.0, 15.0, 70.0, 75.0, 75.0, 85.0, 10.0, 35.0, 100.0] |
| 7 | GLM-5.3 | [40.0, 90.0, 72.5, 95.0, 90.0, 32.5, 15.0, 35.0, 30.0, 50.0, 70.0, 50.0] |
| 8 | Kimi K3 | [35.0, 55.0, 72.5, 65.0, 80.0, 100.0, 40.0, 65.0, 72.5, 75.0, 75.0, 5.0] |
| 9 | GPT-5.6 Luna | [90.0, 5.0, 60.0, 40.0, 5.0, 85.0, 30.0, 5.0, 17.5, 60.0, 25.0, 70.0] |
| 10 | Claude Opus 5 | [15.0, 40.0, 95.0, 100.0, 60.0, 25.0, 90.0, 95.0, 65.0, 90.0, 95.0, 15.0] |
| 11 | DeepSeek V4 Pro | [85.0, 0.0, 42.5, 45.0, 55.0, 57.5, 55.0, 20.0, 57.5, 40.0, 15.0, 35.0] |
| 12 | Muse Spark 1.2 | [55.0, 85.0, 25.0, 55.0, 30.0, 20.0, 35.0, 55.0, 5.0, 35.0, 55.0, 95.0] |
| 13 | Claude Fable 5 | [5.0, 30.0, 80.0, 80.0, 40.0, 80.0, 100.0, 100.0, 45.0, 85.0, 90.0, 40.0] |
| 14 | Qwen3.8 Max | [50.0, 65.0, 30.0, 75.0, 100.0, 12.5, 10.0, 50.0, 50.0, 55.0, 60.0, 0.0] |
| 15 | DeepSeek V4 Flash | [95.0, 15.0, 15.0, 30.0, 50.0, 32.5, 25.0, 0.0, 10.0, 20.0, 10.0, 75.0] |
| 16 | Gemini 3.6 Flash | [75.0, 45.0, 10.0, 5.0, 0.0, 45.0, 60.0, 15.0, 57.5, 0.0, 5.0, 80.0] |
| 17 | GPT-5.5 | [20.0, 20.0, 60.0, 10.0, 45.0, 95.0, 80.0, 60.0, 72.5, 80.0, 40.0, 60.0] |
| 18 | Gemini 3.5 Flash | [62.5, 35.0, 0.0, 0.0, 10.0, 0.0, 65.0, 40.0, 40.0, 5.0, 0.0, 85.0] |
| 19 | GLM-5.2 | [45.0, 100.0, 5.0, 15.0, 25.0, 12.5, 0.0, 25.0, 0.0, 67.5, 20.0, 45.0] |
| 20 | Claude Opus 4.8 | [10.0, 75.0, 35.0, 35.0, 20.0, 5.0, 50.0, 80.0, 35.0, 67.5, 50.0, 25.0] |
| 21 | Claude Sonnet 5 | [0.0, 70.0, 20.0, 50.0, 35.0, 75.0, 20.0, 30.0, 17.5, 25.0, 30.0, 55.0] |

## Coverage decision

The score is zero-gap across all retained dimensions. The dropped candidate dimensions are listed below with their missing cohort rows; their values remain null rather than being replaced by a neutral score.

## External benchmark supplements

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) provides the current AA component scores used by this release. [LiveBench](https://livebench.ai/) provides the four-task Instruction Following view and the Overall Score versus Cost Per Successful Task Pareto analysis; [Terminal-Bench 4.0](https://www.tbench.ai/) provides the current standalone terminal-agent leaderboard. Their incomplete cohort coverage keeps them supplemental rather than weighted into this zero-gap ranking. See [raw-data.md](raw-data.md) for the source-backed tables.
