# ValueRank v1.3 Raw Data
**Version:** v1.3
**Updated:** July 28, 2026
v1.3 ranks the full current DeepSWE Best roster (**n=18**). Dimensions without full cohort coverage are excluded (zero-gap). Cost uses **DeepSWE average cost per task only** because Artificial Analysis Intelligence Index total eval cost is unpublished for `Kimi K2.7 Code`.
## Primary Sources
- [DeepSWE](https://deepswe.datacurve.ai/) for `DeepSWE pass@1` and `DeepSWE Avg Cost ($)` (Best / max-effort row per family; source updated July 25, 2026)
- Artificial Analysis model pages for retained AA dimensions (see evidence ledger under `.refresh/v1.3/`)
## Artificial Analysis variant selection
Per family, the AA model-page variant with the most complete coverage of **retained** dimensions is used:
- `Kimi K3` → [`kimi-k3`](https://artificialanalysis.ai/models/kimi-k3)
- `Grok 4.5` → [`grok-4-5`](https://artificialanalysis.ai/models/grok-4-5)
- `Muse Spark 1.1` → [`muse-spark-1-1`](https://artificialanalysis.ai/models/muse-spark-1-1)
- `GPT-5.6 Terra` → [`gpt-5-6-terra`](https://artificialanalysis.ai/models/gpt-5-6-terra)
- `GPT-5.6 Sol` → [`gpt-5-6-sol`](https://artificialanalysis.ai/models/gpt-5-6-sol)
- `Claude Opus 5` → [`claude-opus-5`](https://artificialanalysis.ai/models/claude-opus-5)
- `GPT-5.6 Luna` → [`gpt-5-6-luna`](https://artificialanalysis.ai/models/gpt-5-6-luna)
- `GPT-5.5` → [`gpt-5-5`](https://artificialanalysis.ai/models/gpt-5-5)
- `Claude Fable 5` → [`claude-fable-5`](https://artificialanalysis.ai/models/claude-fable-5)
- `GLM-5.2` → [`glm-5-2`](https://artificialanalysis.ai/models/glm-5-2)
- `Gemini 3.6 Flash` → [`gemini-3-6-flash`](https://artificialanalysis.ai/models/gemini-3-6-flash)
- `GPT-5.4` → [`gpt-5-4`](https://artificialanalysis.ai/models/gpt-5-4)
- `Claude Opus 4.8` → [`claude-opus-4-8`](https://artificialanalysis.ai/models/claude-opus-4-8)
- `Gemini 3.1 Pro` → [`gemini-3-1-pro-preview`](https://artificialanalysis.ai/models/gemini-3-1-pro-preview)
- `Kimi K2.7 Code` → [`kimi-k2-7-code`](https://artificialanalysis.ai/models/kimi-k2-7-code)
- `Gemini 3.5 Flash` → [`gemini-3-5-flash`](https://artificialanalysis.ai/models/gemini-3-5-flash)
- `Claude Sonnet 5` → [`claude-sonnet-5`](https://artificialanalysis.ai/models/claude-sonnet-5)
- `Claude Sonnet 4.6` → [`claude-sonnet-4-6-adaptive`](https://artificialanalysis.ai/models/claude-sonnet-4-6-adaptive)

## DeepSWE

| Model | Effort | DeepSWE pass@1 | DeepSWE Avg Cost ($) |
|---|---|---:|---:|
| Claude Opus 5 | max | 74 | 11.84 |
| GPT-5.6 Sol | max | 73 | 8.39 |
| GPT-5.6 Terra | max | 70 | 4.95 |
| Claude Fable 5 | max | 70 | 21.63 |
| Kimi K3 | max | 69 | 4.65 |
| GPT-5.6 Luna | max | 67 | 3.03 |
| GPT-5.5 | xhigh | 67 | 7.23 |
| Claude Opus 4.8 | max | 59 | 13.22 |
| Grok 4.5 | high | 54 | 2.42 |
| Claude Sonnet 5 | max | 54 | 26.40 |
| Muse Spark 1.1 | xhigh | 53 | 2.36 |
| GPT-5.4 | xhigh | 52 | 5.65 |
| Gemini 3.6 Flash | high | 49 | 3.53 |
| GLM-5.2 | max | 44 | 3.92 |
| Gemini 3.5 Flash | medium | 37 | 7.34 |
| Kimi K2.7 Code | — | 31 | 2.82 |
| Claude Sonnet 4.6 | high | 30 | 5.52 |
| Gemini 3.1 Pro | high | 12 | 9.48 |

## AA-Omniscience

| Model | Accuracy | Hallucination Rate |
|---|---:|---:|
| Kimi K3 | 46.0 | 50.9 |
| Grok 4.5 | 52.0 | 53.5 |
| Muse Spark 1.1 | 40.6 | 38.1 |
| GPT-5.6 Terra | 45.9 | 85.2 |
| GPT-5.6 Sol | 58.5 | 88.8 |
| Claude Opus 5 | 54.2 | 50.1 |
| GPT-5.6 Luna | 41.5 | 90.1 |
| GPT-5.5 | 56.9 | 85.5 |
| Claude Fable 5 | 61.4 | 54.9 |
| GLM-5.2 | 25.1 | 28.1 |
| Gemini 3.6 Flash | 50.2 | 53.5 |
| GPT-5.4 | 50.0 | 88.6 |
| Claude Opus 4.8 | 46.6 | 35.9 |
| Gemini 3.1 Pro | 55.2 | 49.9 |
| Kimi K2.7 Code | 38.6 | 80.3 |
| Gemini 3.5 Flash | 51.9 | 60.7 |
| Claude Sonnet 5 | 38.3 | 37.2 |
| Claude Sonnet 4.6 | 40.0 | 46.1 |

## Agentic / reasoning benchmarks (retained)

| Model | GDPval-AA | AA-LCR | HLE | GPQA | SciCode | CritPt |
|---|---:|---:|---:|---:|---:|---:|
| Kimi K3 | 59.4 | 74.7 | 44.4 | 93.5 | 58.7 | 23.4 |
| Grok 4.5 | 51.4 | 67.7 | 40.3 | 93.1 | 54.0 | 15.4 |
| Muse Spark 1.1 | 43.8 | 63.3 | 45.1 | 89.8 | 58.2 | 15.1 |
| GPT-5.6 Terra | 54.1 | 74.0 | 41.8 | 92.5 | 53.9 | 30.0 |
| GPT-5.6 Sol | 61.8 | 73.7 | 47.2 | 94.1 | 56.1 | 32.3 |
| Claude Opus 5 | 68.1 | 70.0 | 52.6 | 93.2 | 55.7 | 29.1 |
| GPT-5.6 Luna | 54.1 | 74.0 | 37.2 | 91.1 | 52.5 | 20.6 |
| GPT-5.5 | 49.5 | 74.3 | 44.3 | 93.5 | 56.1 | 27.1 |
| Claude Fable 5 | 62.3 | 70.0 | 53.3 | 92.6 | 60.2 | 28.6 |
| GLM-5.2 | 50.5 | 71.3 | 40.1 | 89.5 | 50.5 | 20.9 |
| Gemini 3.6 Flash | 46.1 | 69.7 | 38.3 | 92.8 | 52.7 | 10.6 |
| GPT-5.4 | 44.6 | 74.0 | 41.6 | 92.0 | 56.6 | 23.4 |
| Claude Opus 4.8 | 54.6 | 67.7 | 45.7 | 92.0 | 53.5 | 20.9 |
| Gemini 3.1 Pro | 23.2 | 72.7 | 44.7 | 94.1 | 58.9 | 17.7 |
| Kimi K2.7 Code | 34.3 | 66.3 | 32.8 | 89.6 | 47.5 | 10.0 |
| Gemini 3.5 Flash | 42.2 | 69.3 | 41.0 | 92.2 | 53.1 | 13.1 |
| Claude Sonnet 5 | 55.1 | 70.7 | 39.6 | 91.1 | 53.6 | 16.9 |
| Claude Sonnet 4.6 | 43.9 | 70.7 | 30.0 | 87.5 | 46.8 | 3.1 |

## Artificial Analysis model-page refresh

| Model | Eval Cost ($) | Speed (tok/s) | AA Index |
|---|---:|---:|---:|
| Kimi K3 | 2437.41 | 33.3 | 57.1 |
| Grok 4.5 | 639.87 | 58.3 | 53.8 |
| Muse Spark 1.1 | 548.07 | 129.0 | 50.6 |
| GPT-5.6 Terra | 2060.40 | 137.2 | 55.0 |
| GPT-5.6 Sol | 3442.81 | 82.2 | 58.9 |
| Claude Opus 5 | 3835.51 | 54.6 | 60.7 |
| GPT-5.6 Luna | 944.97 | 194.9 | 51.2 |
| GPT-5.5 | 2777.91 | 84.0 | 54.8 |
| Claude Fable 5 | 5630.52 | 72.1 | 59.9 |
| GLM-5.2 | 765.10 | 225.2 | 51.1 |
| Gemini 3.6 Flash | 726.70 | 239.6 | 50.1 |
| GPT-5.4 | 2185.46 | 153.5 | 51.4 |
| Claude Opus 4.8 | 3752.55 | 56.0 | 55.7 |
| Gemini 3.1 Pro | 815.11 | 127.4 | 46.5 |
| Kimi K2.7 Code | — | 45.7 | 41.9 |
| Gemini 3.5 Flash | 1040.88 | 187.6 | 50.2 |
| Claude Sonnet 5 | 4010.12 | 74.2 | 53.4 |
| Claude Sonnet 4.6 | 3355.85 | 47.8 | 47.2 |

Note: `Kimi K2.7 Code` has no published AA Intelligence Index total eval cost on its current model page; Cost dimension therefore uses DeepSWE-only for the whole cohort (zero-gap).

## Cost construction (DeepSWE-only)

| Model | DeepSWE Cost (0-100) | Composite Cost (0-100) |
|---|---:|---:|
| Kimi K3 | 17.61 | 17.61 |
| Grok 4.5 | 9.17 | 9.17 |
| Muse Spark 1.1 | 8.94 | 8.94 |
| GPT-5.6 Terra | 18.75 | 18.75 |
| GPT-5.6 Sol | 31.78 | 31.78 |
| Claude Opus 5 | 44.85 | 44.85 |
| GPT-5.6 Luna | 11.48 | 11.48 |
| GPT-5.5 | 27.39 | 27.39 |
| Claude Fable 5 | 81.93 | 81.93 |
| GLM-5.2 | 14.85 | 14.85 |
| Gemini 3.6 Flash | 13.37 | 13.37 |
| GPT-5.4 | 21.40 | 21.40 |
| Claude Opus 4.8 | 50.08 | 50.08 |
| Gemini 3.1 Pro | 35.91 | 35.91 |
| Kimi K2.7 Code | 10.68 | 10.68 |
| Gemini 3.5 Flash | 27.80 | 27.80 |
| Claude Sonnet 5 | 100.00 | 100.00 |
| Claude Sonnet 4.6 | 20.91 | 20.91 |

## Dropped dimensions (incomplete coverage)

| Dimension | Models missing |
|---|---|
| IFBench | Claude Opus 5, Kimi K3, GPT-5.6 Luna, Grok 4.5, Claude Sonnet 5, Gemini 3.6 Flash |
| Terminal-Bench Hard | Claude Opus 5, Kimi K3, GPT-5.6 Luna, Grok 4.5, Claude Sonnet 5, Gemini 3.6 Flash |
| τ²-Bench Telecom | Claude Opus 5, Kimi K3, GPT-5.6 Luna, Grok 4.5, Claude Sonnet 5, Gemini 3.6 Flash |

## Official-first excluded benchmark audit

Re-checked against the n=18 DeepSWE Best cohort. A benchmark remains excluded unless a currently published implementation contains **all 18** ranked models.

| Benchmark | Official source outcome | Best current secondary outcome |
|---|---|---|
| APEX-Agents | [Mercor APEX-Agents](https://www.mercor.com/apex/apex-agents-leaderboard/) does not cover the expanded July 2026 DeepSWE cohort (missing multiple new models including Claude Opus 5, GPT-5.6 family, Kimi K3, Grok 4.5, Muse Spark, etc.) | [AA APEX-Agents-AA](https://artificialanalysis.ai/evaluations/apex-agents-aa) still incomplete for n=18 |
| ITBench | [IBM ITBench Kaggle](https://www.kaggle.com/benchmarks/ibm-research/itbench) lacks exact ValueRank cohort names | [AA ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) incomplete |
| MMMU-Pro | [MMMU site](https://mmmu-benchmark.github.io/) is paper-era / incomplete for current cohort | [AA MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro) incomplete |
| MMLU-Pro | [TIGER-Lab MMLU-Pro](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) incomplete for current cohort | Kaggle / LLM Stats incomplete |
| LiveCodeBench | [LiveCodeBench](https://livecodebench.github.io/) paper-era leaderboard incomplete | AA / Kaggle / LLM Stats incomplete |
| Global-MMLU-Lite | [Cohere Labs Kaggle](https://www.kaggle.com/benchmarks/cohere-labs/global-mmlu-lite) incomplete | Secondary incomplete |
| AIME 2025 | Owner publishes exam, not full frontier leaderboard | AA / Kaggle incomplete for n=18 |
| MATH-500 | Owner publishes dataset, not full frontier leaderboard | Kaggle incomplete for n=18 |
