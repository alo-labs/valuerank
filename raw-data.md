# ValueRank v1.5.0 Raw Data

**Version:** v1.5.0 · **Updated:** September 6, 2026 · **DeepSWE source update:** September 3, 2026 · **AA source:** [Artificial Analysis Intelligence Index v4.2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

All 21 current DeepSWE Best models are retained. Raw AA benchmark values are percentages below for readability; the machine-readable files preserve fractions. Speed is included because the v4.2 snapshot publishes numeric values for all selected pages. The external benchmark tables are kept separate from the AA source matrix so version identities remain unambiguous.

## Selected AA pages

| Model | AA slug | AA effort | Source |
|---|---|---|---|
| Gemini 3.8 Flash | gemini-3-8-flash | not stated | [page](https://artificialanalysis.ai/models/gemini-3-8-flash) |
| Grok 4.6 | grok-4-6 | not stated | [page](https://artificialanalysis.ai/models/grok-4-6) |
| GLM-5.3 Flash | glm-5-3-flash | not stated | [page](https://artificialanalysis.ai/models/glm-5-3-flash) |
| GPT-6 Astra | gpt-6-astra-xhigh | not stated | [page](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) |
| GPT-5.6 Sol | gpt-5-6-sol | not stated | [page](https://artificialanalysis.ai/models/gpt-5-6-sol) |
| Gemini 3.7 Flash | gemini-3-7-flash | not stated | [page](https://artificialanalysis.ai/models/gemini-3-7-flash) |
| GLM-5.3 | glm-5-3 | not stated | [page](https://artificialanalysis.ai/models/glm-5-3) |
| Kimi K3 | kimi-k3 | not stated | [page](https://artificialanalysis.ai/models/kimi-k3) |
| GPT-5.6 Luna | gpt-5-6-luna | not stated | [page](https://artificialanalysis.ai/models/gpt-5-6-luna) |
| Claude Opus 5 | claude-opus-5 | not stated | [page](https://artificialanalysis.ai/models/claude-opus-5) |
| DeepSeek V4 Pro | deepseek-v4-pro | not stated | [page](https://artificialanalysis.ai/models/deepseek-v4-pro) |
| Muse Spark 1.2 | muse-spark-1-2 | not stated | [page](https://artificialanalysis.ai/models/muse-spark-1-2) |
| Claude Fable 5 | claude-fable-5 | not stated | [page](https://artificialanalysis.ai/models/claude-fable-5) |
| Qwen3.8 Max | qwen3-8-max | not stated | [page](https://artificialanalysis.ai/models/qwen3-8-max) |
| DeepSeek V4 Flash | deepseek-v4-flash | not stated | [page](https://artificialanalysis.ai/models/deepseek-v4-flash) |
| Gemini 3.6 Flash | gemini-3-6-flash | not stated | [page](https://artificialanalysis.ai/models/gemini-3-6-flash) |
| GPT-5.5 | gpt-5-5 | not stated | [page](https://artificialanalysis.ai/models/gpt-5-5) |
| Gemini 3.5 Flash | gemini-3-5-flash | not stated | [page](https://artificialanalysis.ai/models/gemini-3-5-flash) |
| GLM-5.2 | glm-5-2 | not stated | [page](https://artificialanalysis.ai/models/glm-5-2) |
| Claude Opus 4.8 | claude-opus-4-8 | not stated | [page](https://artificialanalysis.ai/models/claude-opus-4-8) |
| Claude Sonnet 5 | claude-sonnet-5 | not stated | [page](https://artificialanalysis.ai/models/claude-sonnet-5) |

## AA source input matrix

| # | Model | Effort | DeepSWE pass@1 | DeepSWE avg cost | AA-Briefcase Elo | GDPval-AA v2 | τ³-Banking | AA Terminal-Bench v2.1 | SciCode | GDP.pdf all-pass | AA-LCR v1.1 | HLE | GPQA (legacy) | CritPt | Omni Accuracy | Omni Non-Hallucination | AA Index | AA eval cost | Speed tok/s |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Gemini 3.8 Flash | high | 74.0% ± 1.0% | $2.36 | 1203.78 | 48.29% | 44.95% | 87.64% | 56.60% | 19.00% | 81.33% | 47.82% | 95.25% | 18.29% | 54.60% | 44.82% | 47.07 | $1077.95 | 311.0 |
| 2 | Grok 4.6 | medium | 67.0% ± 2.0% | $3.45 | 1537.76 | 57.35% | 50.72% | 88.39% | 56.48% | 18.80% | 80.33% | 42.91% | 94.95% | 17.14% | 48.23% | 65.71% | 50.58 | $1632.13 | 62.7 |
| 3 | GLM-5.3 Flash | max | 63.0% ± 4.0% | $0.24 | 1459.13 | 58.65% | 47.22% | 84.27% | 51.62% | 13.00% | 80.00% | 39.85% | 91.21% | 15.43% | 27.50% | 72.37% | 46.22 | $219.23 | 46.1 |
| 4 | GPT-6 Astra | xhigh | 74.0% ± 3.0% | $6.52 | 1538.14 | 52.87% | 43.09% | 89.14% | 55.67% | 32.20% | 80.00% | 54.59% | 96.26% | 31.43% | 61.85% | 51.68% | 54.31 | $2778.30 | 67.0 |
| 5 | GPT-5.6 Sol | max | 73.0% ± 3.0% | $6.46 | 1478.66 | 56.37% | 44.33% | 88.01% | 57.06% | 28.20% | 84.00% | 49.49% | 94.14% | 32.29% | 59.40% | 7.80% | 51.26 | $2463.56 | 87.4 |
| 6 | Gemini 3.7 Flash | medium | 65.0% ± 3.0% | $2.03 | 1116.43 | 46.77% | 32.78% | 85.77% | 57.18% | 23.60% | 81.67% | 47.87% | 94.55% | 14.29% | 55.32% | 35.47% | 45.24 | $687.92 | 319.1 |
| 7 | GLM-5.3 | max | 69.0% ± 3.0% | $3.99 | 1518.58 | 58.97% | 50.31% | 83.90% | 59.03% | 11.80% | 79.67% | 42.26% | 91.72% | 19.14% | 33.85% | 70.45% | 48.58 | $1762.24 | 82.9 |
| 8 | Kimi K3 | max | 69.0% ± 5.0% | $4.65 | 1499.88 | 54.37% | 45.98% | 85.02% | 59.49% | 19.60% | 88.67% | 46.90% | 93.54% | 23.43% | 47.58% | 46.80% | 50.23 | $3069.54 | 41.9 |
| 9 | GPT-5.6 Luna | max | 67.0% ± 4.0% | $0.61 | 1342.42 | 49.64% | 31.13% | 80.90% | 53.59% | 23.00% | 83.67% | 39.48% | 91.11% | 20.57% | 42.73% | 7.42% | 43.44 | $213.83 | 130.1 |
| 10 | Claude Opus 5 | max | 74.0% ± 4.0% | $11.84 | 1647.02 | 61.90% | 42.06% | 89.14% | 56.37% | 21.60% | 79.33% | 54.87% | 93.23% | 29.14% | 60.87% | 39.18% | 54.05 | $5545.57 | 60.1 |
| 11 | DeepSeek V4 Pro | max | 63.0% ± 6.0% | $1.67 | 1269.34 | 49.83% | 39.59% | 78.65% | 51.04% | 13.00% | 80.33% | 41.01% | 92.83% | 18.00% | 49.10% | 5.17% | 42.11 | $706.75 | 70.6 |
| 12 | Muse Spark 1.2 | xhigh | 55.0% ± 2.0% | $3.70 | 1346.23 | 51.35% | 34.85% | 80.15% | 57.41% | 16.80% | 79.00% | 45.46% | 90.40% | 17.71% | 45.38% | 66.71% | 46.84 | $821.67 | 318.4 |
| 13 | Claude Fable 5 | xhigh | 70.0% ± 3.0% | $13.41 | 1533.52 | 56.77% | 38.14% | 84.64% | 61.00% | 24.00% | 82.33% | 55.47% | 92.63% | 28.57% | 65.35% | 36.36% | 53.19 | $7603.22 | 71.5 |
| 14 | Qwen3.8 Max | xhigh | 57.0% ± 3.0% | $3.73 | 1392.33 | 56.68% | 51.34% | 81.27% | 53.24% | 21.80% | 78.33% | 43.05% | 92.73% | 20.00% | 31.85% | 58.25% | 46.91 | $1937.50 | 40.6 |
| 15 | DeepSeek V4 Flash | max | 53.0% ± 4.0% | $0.46 | 1262.58 | 48.56% | 39.38% | 78.65% | 50.35% | 14.20% | 79.67% | 38.55% | 90.81% | 16.57% | 40.38% | 8.30% | 40.84 | $363.48 | 133.0 |
| 16 | Gemini 3.6 Flash | high | 47.0% ± 4.0% | $2.21 | 955.24 | 41.72% | 29.90% | 77.53% | 53.36% | 17.40% | 80.00% | 40.82% | 92.83% | 10.57% | 49.97% | 44.37% | 40.29 | $508.75 | 216.4 |
| 17 | GPT-5.5 | xhigh | 67.0% ± 6.0% | $7.23 | 1138.77 | 44.96% | 38.97% | 84.27% | — | — | 84.33% | 45.78% | 93.54% | 27.14% | 57.95% | 10.98% | 45.62 | $— | 84.7 |
| 18 | Gemini 3.5 Flash | high | 36.0% ± 4.0% | $3.45 | 871.07 | 38.13% | 32.16% | 78.65% | 53.94% | 19.80% | 73.33% | 42.68% | 92.22% | 13.14% | 51.40% | 37.83% | 39.73 | $1419.97 | 218.8 |
| 19 | GLM-5.2 | max | 44.0% ± 2.0% | $3.92 | 1238.86 | 46.04% | 34.64% | 77.90% | 51.16% | — | 78.33% | 41.15% | 89.49% | 20.86% | 24.33% | 73.70% | 42.54 | $— | 73.1 |
| 20 | Claude Opus 4.8 | max | 59.0% ± 2.0% | $13.22 | 1319.47 | 49.63% | 34.23% | 84.64% | 54.40% | — | 77.67% | 48.66% | 92.02% | 20.86% | 48.83% | 60.75% | 46.44 | $— | 63.1 |
| 21 | Claude Sonnet 5 | max | 54.0% ± 4.0% | $26.40 | 1358.11 | 50.24% | 37.32% | 80.52% | 54.28% | 13.20% | 82.00% | 41.29% | 91.11% | 16.86% | 40.05% | 60.63% | 45.11 | $5312.58 | 82.9 |

## [LiveBench](https://livebench.ai/) external component

[LiveBench](https://livebench.ai/) release **2026_06_25** supplies the four-task Instruction Following mean and its seven-category Overall Score. Cost is the official **Cost Per Successful Task** field. The pinned table matches **20/21** ranked models and includes **1 official supplemental model** outside that cohort: **Claude Fable 5.1**. GPT-6 Astra is unavailable in this release.

| Model | LiveBench variant | Instruction Following | Overall Score | Cost Per Successful Task |
|---|---|---:|---:|---:|
| Gemini 3.8 Flash | gemini-3.8-flash-high | 81.41 | 75.83 | $0.3073 |
| Claude Opus 5 | claude-opus-5-max-effort | 63.77 | 80.08 | $0.7067 |
| GPT-5.6 Sol | gpt-5.6-sol-max | 71.85 | 81.05 | $0.5070 |
| Claude Fable 5 | claude-fable-5-max-effort | 75.77 | 82.97 | $1.4777 |
| GLM-5.3 | glm-5.3 | 69.30 | 76.14 | $0.4504 |
| Kimi K3 | kimi-k3 | 71.36 | 79.19 | $0.3510 |
| Grok 4.6 | grok-4.6 | 71.87 | 78.04 | $0.2068 |
| GPT-5.6 Luna | gpt-5.6-luna-max | 60.12 | 73.56 | $0.1677 |
| GPT-5.5 | gpt-5.5-xhigh | 70.73 | 80.19 | $0.4356 |
| Gemini 3.7 Flash | gemini-3.7-flash-high | 79.93 | 78.83 | $0.1571 |
| GLM-5.3 Flash | glm-5.3-flash | 52.82 | 71.59 | $0.0305 |
| DeepSeek V4 Pro | deepseek-v4-pro | 62.35 | 71.57 | $0.0498 |
| Claude Opus 4.8 | claude-opus-4-8-max-effort | 72.03 | 76.22 | $0.9858 |
| Qwen3.8 Max | qwen3.8-max | 74.08 | 78.46 | $0.2750 |
| Muse Spark 1.2 | muse-spark-1.2-xhigh | 74.33 | 77.95 | $0.3753 |
| Claude Sonnet 5 | claude-sonnet-5-xhigh-effort | 63.86 | 76.04 | $0.5134 |
| DeepSeek V4 Flash | deepseek-v4-flash | 63.14 | 65.48 | $0.0161 |
| Gemini 3.6 Flash | gemini-3.6-flash-high | 75.37 | 73.59 | $0.2353 |
| GLM-5.2 | glm-5.2 | 62.29 | 73.16 | $0.2246 |
| Gemini 3.5 Flash | gemini-3.5-flash-high | 75.60 | 74.64 | $0.2489 |
| Claude Fable 5.1 | claude-fable-5-1-max-effort | 72.99 | 83.41 | $1.2117 |

LiveBench Pareto frontier (Overall Score vs Cost Per Successful Task): **DeepSeek V4 Flash, GLM-5.3 Flash, Gemini 3.7 Flash, Kimi K3, GPT-5.5, GPT-5.6 Sol, Claude Fable 5.1**.

## [Terminal-Bench 4.0](https://www.tbench.ai/) external component

The current official [Terminal-Bench 4.0](https://www.tbench.ai/) snapshot contains **14 rows** and overlaps **11/21** ranked models. It replaces the old standalone TB2.1 publication; the AA source matrix above keeps its v2.1 field only as explicit AA-source provenance.

| Rank | Model | Agent | Resolution rate | Tokens | Cost |
|---:|---|---|---:|---:|---:|
| 1 | GPT-6 Astra | Codex | 58.2% ± 2.8% | 1.5B | $3,300 |
| 2 | Fable 5.1 | Claude Code | 57.9% ± 3.8% | 2.7B | $6,200 |
| 3 | Opus 5 | Claude Code | 51.8% ± 3.4% | 6.5B | $6,000 |
| 4 | Fable 5 | Claude Code | 44.5% ± 3.8% | 3.8B | $7,300 |
| 5 | GLM-5.3 | Claude Code | 41.8% ± 3.2% | 8.7B | $2,700 |
| 6 | GPT-5.6 Sol | Codex | 37.3% ± 3.8% | 4.4B | $2,500 |
| 7 | Opus 4.8 | Claude Code | 23.6% ± 3.6% | 6.4B | $6,500 |
| 8 | GPT-5.6 Terra | Codex | 21.5% ± 3.3% | 5.7B | $1,700 |
| 9 | Grok 4.6 | Grok Build | 20.3% ± 3.1% | 4.0B | $3,600 |
| 10 | Gemini 3.8 Flash | mini-SWE-agent | 19.1% ± 3.4% | 17.2B | $1,800 |
| 11 | GPT-5.6 Luna | Codex | 17.3% ± 2.8% | 11.6B | $300 |
| 12 | Grok 4.5 | Grok Build | 12.4% ± 2.6% | 3.4B | $2,100 |
| 12 | Sonnet 5 | Claude Code | 12.4% ± 3.1% | 21.6B | $9,600 |
| 14 | Gemini 3.7 Flash | mini-SWE-agent | 11.2% ± 2.4% | 11.1B | $1,300 |

## Cost construction

Cost mode: **DeepSWE-only**. AA total evaluation cost is available for **18/21** models; missing AA costs are **GPT-5.5, Claude Opus 4.8, GLM-5.2**. No selective substitution is used.

| Model | AA cost penalty | DeepSWE cost penalty | Composite cost |
|---|---:|---:|---:|
| Gemini 3.8 Flash | — | 8.94 | 8.94 |
| Grok 4.6 | — | 13.07 | 13.07 |
| GLM-5.3 Flash | — | 0.91 | 0.91 |
| GPT-6 Astra | — | 24.70 | 24.70 |
| GPT-5.6 Sol | — | 24.47 | 24.47 |
| Gemini 3.7 Flash | — | 7.69 | 7.69 |
| GLM-5.3 | — | 15.11 | 15.11 |
| Kimi K3 | — | 17.61 | 17.61 |
| GPT-5.6 Luna | — | 2.31 | 2.31 |
| Claude Opus 5 | — | 44.85 | 44.85 |
| DeepSeek V4 Pro | — | 6.33 | 6.33 |
| Muse Spark 1.2 | — | 14.02 | 14.02 |
| Claude Fable 5 | — | 50.80 | 50.80 |
| Qwen3.8 Max | — | 14.13 | 14.13 |
| DeepSeek V4 Flash | — | 1.74 | 1.74 |
| Gemini 3.6 Flash | — | 8.37 | 8.37 |
| GPT-5.5 | — | 27.39 | 27.39 |
| Gemini 3.5 Flash | — | 13.07 | 13.07 |
| GLM-5.2 | — | 14.85 | 14.85 |
| Claude Opus 4.8 | — | 50.08 | 50.08 |
| Claude Sonnet 5 | — | 100.00 | 100.00 |

## Supplemental Artificial Analysis coverage

These fields are preserved for future analysis but remain outside the primary score because they are incomplete across the current cohort or are not separate ValueRank dimensions. AA-Briefcase and GDP.pdf are current v4.2 source components represented in the raw matrix; GPQA Diamond is retained as an explicitly labelled legacy ValueRank input. LiveBench and TB4 are external coverage-only components under the same no-imputation policy.

| Field | Available | Missing models | Role |
|---|---:|---|---|
| mlcrOverall | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| harveyLab | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| apexAgents | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| mmmuPro | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| livecodebench | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| aime25 | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| analystAgent | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| automationBenchPartialScore | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| enterpriseOpsGym | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| itBenchSre | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| briefcaseRubricPassRate | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| briefcaseTotalCost | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| livebenchOverall | 20/21 | GPT-6 Astra | Supplemental / not scored |
| livebenchInstructionFollowing | 20/21 | GPT-6 Astra | Supplemental / not scored |
| livebenchCostPerSuccessfulTask | 20/21 | GPT-6 Astra | Supplemental / not scored |
| terminalBenchV4 | 11/21 | Kimi K3, GPT-5.5, GLM-5.3 Flash, DeepSeek V4 Pro, Qwen3.8 Max, Muse Spark 1.2, DeepSeek V4 Flash, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | Supplemental / not scored |

## Dropped primary candidate

| Dimension | Missing model | Treatment |
|---|---|---|
| Terminal-Bench 4.0 | Kimi K3, GPT-5.5, GLM-5.3 Flash, DeepSeek V4 Pro, Qwen3.8 Max, Muse Spark 1.2, DeepSeek V4 Flash, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | incomplete cohort coverage; values remain null and are not neutral-filled |
| Instruction Following (LiveBench) | GPT-6 Astra | incomplete cohort coverage; values remain null and are not neutral-filled |
| SciCode | GPT-5.5 | incomplete cohort coverage; values remain null and are not neutral-filled |

Missing values are intentionally represented as null; no old-version, model-family, median, or neutral-fill substitution is used.

## Machine-readable artifacts

- [.refresh/v1.4/deepswe.json](.refresh/v1.4/deepswe.json): current DeepSWE extraction
- [.refresh/v1.4/aa_metrics.json](.refresh/v1.4/aa_metrics.json): decoded current AA model payloads
- [.refresh/v1.4/scores.json](.refresh/v1.4/scores.json): normalized scores and rankings
- [.refresh/v1.4/coverage_matrix.json](.refresh/v1.4/coverage_matrix.json): primary and supplemental availability
- [.refresh/v1.4/livebench.json](.refresh/v1.4/livebench.json): pinned LiveBench task/category/cost snapshot and Pareto data
- [.refresh/v1.4/tb4.json](.refresh/v1.4/tb4.json): normalized official Terminal-Bench 4.0 rendered leaderboard
- [research/2026-09-06-valuerank-refresh-v4-2/README.md](research/2026-09-06-valuerank-refresh-v4-2/README.md): v4.2 source-change and scoring decision record
