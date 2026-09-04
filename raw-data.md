# ValueRank v1.4.0 Raw Data

**Version:** v1.4.0 · **Updated:** September 4, 2026 · **DeepSWE source update:** September 3, 2026 · **AA source:** Artificial Analysis Intelligence Index v4.1.1

All 21 current DeepSWE Best models are retained. Raw AA benchmark values are percentages below for readability; the machine-readable files preserve fractions. Speed is shown when published but is not part of the primary score because GPT-6 Astra is N/A.

## Selected AA pages

| Model | AA slug | AA effort | Source |
|---|---|---|---|
| Gemini 3.8 Flash | gemini-3-8-flash | high | [page](https://artificialanalysis.ai/models/gemini-3-8-flash) |
| GLM-5.3 Flash | glm-5-3-flash | max | [page](https://artificialanalysis.ai/models/glm-5-3-flash) |
| GPT-5.6 Sol | gpt-5-6-sol | max | [page](https://artificialanalysis.ai/models/gpt-5-6-sol) |
| GPT-6 Astra | gpt-6-astra-xhigh | xhigh | [page](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) |
| Grok 4.6 | grok-4-6-medium | medium | [page](https://artificialanalysis.ai/models/grok-4-6-medium) |
| Claude Opus 5 | claude-opus-5 | max | [page](https://artificialanalysis.ai/models/claude-opus-5) |
| Kimi K3 | kimi-k3 | max | [page](https://artificialanalysis.ai/models/kimi-k3) |
| GLM-5.3 | glm-5-3 | max | [page](https://artificialanalysis.ai/models/glm-5-3) |
| Muse Spark 1.2 | muse-spark-1-2 | xhigh | [page](https://artificialanalysis.ai/models/muse-spark-1-2) |
| Claude Fable 5 | claude-fable-5 | max | [page](https://artificialanalysis.ai/models/claude-fable-5) |
| Gemini 3.7 Flash | gemini-3-7-flash-medium | medium | [page](https://artificialanalysis.ai/models/gemini-3-7-flash-medium) |
| GPT-5.6 Luna | gpt-5-6-luna | max | [page](https://artificialanalysis.ai/models/gpt-5-6-luna) |
| Qwen3.8 Max | qwen3-8-max | not stated | [page](https://artificialanalysis.ai/models/qwen3-8-max) |
| DeepSeek V4 Pro | deepseek-v4-pro | max | [page](https://artificialanalysis.ai/models/deepseek-v4-pro) |
| GPT-5.5 | gpt-5-5 | xhigh | [page](https://artificialanalysis.ai/models/gpt-5-5) |
| Gemini 3.6 Flash | gemini-3-6-flash | high | [page](https://artificialanalysis.ai/models/gemini-3-6-flash) |
| DeepSeek V4 Flash | deepseek-v4-flash | max | [page](https://artificialanalysis.ai/models/deepseek-v4-flash) |
| Claude Opus 4.8 | claude-opus-4-8 | max | [page](https://artificialanalysis.ai/models/claude-opus-4-8) |
| GLM-5.2 | glm-5-2 | max | [page](https://artificialanalysis.ai/models/glm-5-2) |
| Gemini 3.5 Flash | gemini-3-5-flash | high | [page](https://artificialanalysis.ai/models/gemini-3-5-flash) |
| Claude Sonnet 5 | claude-sonnet-5 | max | [page](https://artificialanalysis.ai/models/claude-sonnet-5) |

## Full primary input matrix

| # | Model | Effort | DeepSWE pass@1 | DeepSWE avg cost | GDPval-AA v2 | τ³-Banking | Terminal-Bench v2.1 | SciCode | AA-LCR | HLE | GPQA | CritPt | Omni Accuracy | Omni Non-Hallucination | AA Index | AA eval cost | Speed tok/s |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Gemini 3.8 Flash | high | 74.0% ± 1.0% | $2.36 | 52.27% | 44.95% | 87.64% | 53.59% | 81.00% | 47.82% | 95.25% | 18.29% | 54.60% | 44.82% | 58.68 | $825.83 | 326.9 |
| 2 | GLM-5.3 Flash | max | 63.0% ± 4.0% | $0.24 | 63.23% | 47.22% | 84.27% | 46.06% | 78.00% | 39.85% | 91.21% | 15.43% | 27.50% | 72.37% | 57.46 | $138.02 | 47.4 |
| 3 | GPT-5.6 Sol | max | 73.0% ± 3.0% | $6.46 | 60.51% | 44.33% | 88.01% | 56.13% | 77.67% | 49.49% | 94.14% | 32.29% | 59.40% | 7.80% | 60.93 | $2017.29 | 76.5 |
| 4 | GPT-6 Astra | xhigh | 74.0% ± 3.0% | $6.52 | 55.28% | 43.09% | 89.14% | 49.54% | 74.00% | 54.59% | 96.26% | 31.43% | 61.85% | 51.68% | 60.99 | $2004.12 | — |
| 5 | Grok 4.6 | medium | 67.0% ± 2.0% | $3.45 | 61.57% | 44.33% | 84.27% | 54.63% | 72.67% | 42.12% | 93.54% | 17.71% | 41.93% | 76.00% | 59.01 | $929.97 | 63.5 |
| 6 | Claude Opus 5 | max | 74.0% ± 4.0% | $11.84 | 66.20% | 42.06% | 89.14% | 55.67% | 75.67% | 54.87% | 93.23% | 29.14% | 60.87% | 39.18% | 63.05 | $3836.05 | 57.1 |
| 7 | Kimi K3 | max | 69.0% ± 5.0% | $4.65 | 58.40% | 45.98% | 85.02% | 58.68% | 82.67% | 46.90% | 93.54% | 23.43% | 47.58% | 46.80% | 59.70 | $2425.11 | 39.2 |
| 8 | GLM-5.3 | max | 69.0% ± 3.0% | $3.99 | 62.91% | 50.31% | 83.90% | 56.48% | 76.33% | 42.26% | 91.72% | 19.14% | 33.85% | 70.45% | 59.51 | $1238.50 | 75.3 |
| 9 | Muse Spark 1.2 | xhigh | 55.0% ± 2.0% | $3.70 | 55.75% | 34.85% | 80.15% | 56.37% | 83.33% | 45.46% | 90.40% | 17.71% | 45.38% | 66.71% | 56.76 | $639.27 | 235.8 |
| 10 | Claude Fable 5 | xhigh | 70.0% ± 3.0% | $13.41 | 61.15% | 38.14% | 84.64% | 60.19% | 76.67% | 55.47% | 92.63% | 28.57% | 65.35% | 36.36% | 62.07 | $5455.22 | 70.0 |
| 11 | Gemini 3.7 Flash | medium | 65.0% ± 3.0% | $2.03 | 49.58% | 35.46% | 78.28% | 57.87% | 81.00% | 38.97% | 92.12% | 9.43% | 54.00% | 34.13% | 53.42 | $277.50 | 295.4 |
| 12 | GPT-5.6 Luna | max | 67.0% ± 4.0% | $0.61 | 53.46% | 31.13% | 80.90% | 52.55% | 78.33% | 39.48% | 91.11% | 20.57% | 42.73% | 7.42% | 52.32 | $173.85 | 125.2 |
| 13 | Qwen3.8 Max | xhigh | 57.0% ± 3.0% | $3.73 | 61.05% | 51.34% | 81.27% | 52.89% | 74.33% | 43.05% | 92.73% | 20.00% | 31.85% | 58.25% | 58.08 | $1532.07 | 38.8 |
| 14 | DeepSeek V4 Pro | max | 63.0% ± 6.0% | $1.67 | 53.84% | 39.59% | 78.65% | 49.19% | 75.33% | 41.01% | 92.83% | 18.00% | 49.10% | 5.17% | 53.20 | $616.95 | 60.2 |
| 15 | GPT-5.5 | xhigh | 67.0% ± 6.0% | $7.23 | 49.09% | 38.97% | 84.27% | 56.13% | 79.00% | 45.78% | 93.54% | 27.14% | 57.95% | 10.98% | 56.31 | $2796.05 | 84.0 |
| 16 | Gemini 3.6 Flash | high | 47.0% ± 4.0% | $2.21 | 45.71% | 29.90% | 77.53% | 52.66% | 79.00% | 40.82% | 92.83% | 10.57% | 49.97% | 44.37% | 51.58 | $412.03 | 208.8 |
| 17 | DeepSeek V4 Flash | max | 53.0% ± 4.0% | $0.46 | 52.36% | 39.38% | 78.65% | 49.88% | 74.33% | 38.55% | 90.81% | 16.57% | 40.38% | 8.30% | 51.77 | $323.26 | 140.0 |
| 18 | Claude Opus 4.8 | max | 59.0% ± 2.0% | $13.22 | 53.89% | 34.23% | 84.64% | 53.47% | 73.00% | 48.66% | 92.02% | 20.86% | 48.83% | 60.75% | 57.33 | $3752.32 | 62.2 |
| 19 | GLM-5.2 | max | 44.0% ± 2.0% | $3.92 | 49.88% | 34.64% | 77.90% | 50.46% | 76.67% | 41.15% | 89.49% | 20.86% | 24.33% | 73.70% | 52.64 | $843.44 | 69.9 |
| 20 | Gemini 3.5 Flash | high | 36.0% ± 4.0% | $3.45 | 41.86% | 32.16% | 78.65% | 53.12% | 81.00% | 42.68% | 92.22% | 13.14% | 51.40% | 37.83% | 51.96 | $1042.43 | 204.6 |
| 21 | Claude Sonnet 5 | max | 54.0% ± 4.0% | $26.40 | 54.18% | 37.32% | 80.52% | 53.59% | 77.00% | 41.29% | 91.11% | 16.86% | 40.05% | 60.63% | 55.26 | $4010.51 | 82.1 |

## Cost construction

| Model | AA cost penalty | DeepSWE cost penalty | Composite cost |
|---|---:|---:|---:|
| Gemini 3.8 Flash | 15.14 | 8.94 | 12.04 |
| GLM-5.3 Flash | 2.53 | 0.91 | 1.72 |
| GPT-5.6 Sol | 36.98 | 24.47 | 30.72 |
| GPT-6 Astra | 36.74 | 24.70 | 30.72 |
| Grok 4.6 | 17.05 | 13.07 | 15.06 |
| Claude Opus 5 | 70.32 | 44.85 | 57.58 |
| Kimi K3 | 44.45 | 17.61 | 31.03 |
| GLM-5.3 | 22.70 | 15.11 | 18.91 |
| Muse Spark 1.2 | 11.72 | 14.02 | 12.87 |
| Claude Fable 5 | 100.00 | 50.80 | 75.40 |
| Gemini 3.7 Flash | 5.09 | 7.69 | 6.39 |
| GPT-5.6 Luna | 3.19 | 2.31 | 2.75 |
| Qwen3.8 Max | 28.08 | 14.13 | 21.11 |
| DeepSeek V4 Pro | 11.31 | 6.33 | 8.82 |
| GPT-5.5 | 51.25 | 27.39 | 39.32 |
| Gemini 3.6 Flash | 7.55 | 8.37 | 7.96 |
| DeepSeek V4 Flash | 5.93 | 1.74 | 3.83 |
| Claude Opus 4.8 | 68.78 | 50.08 | 59.43 |
| GLM-5.2 | 15.46 | 14.85 | 15.16 |
| Gemini 3.5 Flash | 19.11 | 13.07 | 16.09 |
| Claude Sonnet 5 | 73.52 | 100.00 | 86.76 |

## Supplemental Artificial Analysis coverage

These fields are preserved for future analysis but remain outside the primary score because they are incomplete across the current cohort or are not part of the current AA v4.1.1 weighted index.

| Field | Available | Missing models | Role |
|---|---:|---|---|
| mlcrOverall | 17/21 | gpt-6-astra, gemini-3.8-flash, grok-4.6, gemini-3.7-flash | Supplemental / not scored |
| harveyLab | 11/21 | gpt-6-astra, gemini-3.8-flash, glm-5.3, grok-4.6, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, qwen3.8-max, muse-spark-1.2, deepseek-v4-flash | Supplemental / not scored |
| apexAgents | 5/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, grok-4.6, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash | Supplemental / not scored |
| mmmuPro | 12/21 | claude-fable-5, glm-5.3, grok-4.6, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, muse-spark-1.2, deepseek-v4-flash, glm-5.2 | Supplemental / not scored |
| livecodebench | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| aime25 | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| analystAgent | 8/21 | gpt-6-astra, gemini-3.8-flash, glm-5.3, grok-4.6, gpt-5.6-luna, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, qwen3.8-max, muse-spark-1.2, deepseek-v4-flash, gemini-3.6-flash, glm-5.2 | Supplemental / not scored |
| automationBenchPartialScore | 11/21 | gpt-6-astra, claude-opus-5, glm-5.3, grok-4.6, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, qwen3.8-max, muse-spark-1.2, deepseek-v4-flash | Supplemental / not scored |
| enterpriseOpsGym | 15/21 | gpt-6-astra, gemini-3.8-flash, grok-4.6, qwen3.8-max, deepseek-v4-flash, gemini-3.6-flash | Supplemental / not scored |
| itBenchSre | 6/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, claude-fable-5, glm-5.3, grok-4.6, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash | Supplemental / not scored |
| briefcaseElo | 19/21 | gemini-3.7-flash, glm-5.3-flash | Supplemental / not scored |
| briefcaseRubricPassRate | 19/21 | gemini-3.7-flash, glm-5.3-flash | Supplemental / not scored |
| briefcaseTotalCost | 19/21 | gemini-3.7-flash, glm-5.3-flash | Supplemental / not scored |

## Dropped primary candidate

| Dimension | Missing model | Treatment |
|---|---|---|
| Speed | GPT-6 Astra | incomplete cohort coverage; values remain null and are not neutral-filled |

Missing values are intentionally represented as null; no old-version, model-family, median, or neutral-fill substitution is used.

## Machine-readable artifacts

- [.refresh/v1.4/deepswe.json](.refresh/v1.4/deepswe.json): current DeepSWE extraction
- [.refresh/v1.4/aa_metrics.json](.refresh/v1.4/aa_metrics.json): decoded current AA model payloads
- [.refresh/v1.4/scores.json](.refresh/v1.4/scores.json): normalized scores and rankings
- [.refresh/v1.4/coverage_matrix.json](.refresh/v1.4/coverage_matrix.json): primary and supplemental availability
- [research/2026-09-04-valuerank-refresh/evidence.jsonl](research/2026-09-04-valuerank-refresh/evidence.jsonl): source/evidence ledger
