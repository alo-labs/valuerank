# ValueRank v1.9.1 Scores

**Updated:** September 30, 2026 · **Cohort:** 10 · **Retained dimensions:** 12 · **Default cost basis:** API Costs (AA total evaluation cost)

API Costs uses the AA total evaluation cost in USD; Plan Costs divides that same value by the highest eligible subscription Value Multiple. The site switcher recalculates the main rank and cost-based charts using the selected basis.

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | AA eval-cost penalty (lower better) |
|---:|---|---:|---:|---:|---:|
| 1 | GPT-5.6 Sol | 72.2 | 77.0 | 2 | 39.79 |
| 2 | GPT-6 Astra | 65.8 | 75.1 | 3 | 43.67 |
| 3 | Claude Opus 5.5 | 64.5 | 83.0 | 1 | 100.00 |
| 4 | Grok 4.6 | 51.8 | 44.4 | 5 | 22.24 |
| 5 | GPT-5.6 Luna | 51.1 | 37.1 | 7 | 3.67 |
| 6 | Kimi K3 | 50.7 | 52.5 | 4 | 42.01 |
| 7 | Gemini 3.8 Flash | 44.5 | 31.7 | 8 | 18.63 |
| 8 | GLM-5.3 | 37.7 | 29.4 | 9 | 28.75 |
| 9 | Claude Opus 5 | 35.8 | 42.9 | 6 | 83.54 |
| 10 | Qwen3.8 Max | 25.8 | 26.9 | 10 | 56.67 |

## Bug Hunt Emphasis Ranking

Bug Hunt is included in the main **10-model primary ranking** at **17.86%**. The companion emphasis view uses the same cohort and increases Bug Hunt's weight to **24.59%** by re-ranking the other retained dimensions within those models.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
| 1 | GPT-5.6 Sol | 43.5/105 | 73.6 | n=2 (mean) | max (max) | Codex CLI / OpenAI | 1 |
| 2 | GPT-6 Astra | 45/105 | 68.6 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 2 |
| 3 | Claude Opus 5.5 | 41.7/105 | 65.6 | n=3 (mean) | max (max) | Claude Code / Anthropic | 3 |
| 4 | GPT-5.6 Luna | 31.3/105 | 52.4 | n=3 (mean) | max (max) | Codex CLI / OpenAI | 5 |
| 5 | Grok 4.6 | 28.7/105 | 52.1 | n=3 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 4 |
| 6 | Kimi K3 | 21/105 | 48.3 | n=1 (single) | default (default) | Claude Code / OpenRouter / OpenRouter | 6 |
| 7 | Gemini 3.8 Flash | 18/105 | 40.9 | n=3 (mean) | high (verified ceiling) | Antigravity CLI / Google | 7 |
| 8 | Claude Opus 5 | 27/105 | 36.5 | n=1 (single) | max (max) | Claude Code / Anthropic | 9 |
| 9 | GLM-5.3 | 19/105 | 35.5 | n=1 (single) | max (verified setting) | Claude Code / Z.ai API / Z.ai API | 8 |
| 10 | Qwen3.8 Max | 25.7/105 | 26.4 | n=3 (mean) | max (verified ceiling) | Claude Code / Alibaba API / Alibaba API | 10 |

Source: [Bug Hunt Bench](https://bughunt.productcompass.pm/) and the pinned [owner scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv) at commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c**. The run configuration details and coverage gaps are in [raw-data.md](raw-data.md).

## Pareto frontier

Undominated on composite cost versus quality: **GPT-5.6 Sol, Grok 4.6, GPT-5.6 Luna, Claude Opus 5.5**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
| Cost | 22.32% | lower |
| Non-Hallucination | 5.36% | higher |
| DeepSWE v1.1 | 22.32% | higher |
| [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 5.36% | higher |
| [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | 4.46% | higher |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 3.57% | higher |
| [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 3.57% | higher |
| [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 3.57% | higher |
| [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 3.57% | higher |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 2.68% | higher |
| [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 5.36% | higher |
| [Bug Hunt Bench](https://bughunt.productcompass.pm/) | 17.86% | higher |

## Normalized dimension matrix

Dimension order is the order in weights above:

[costComposite, omniNonHallucination, deepswePassAt1, gdpvalV21, automationBenchAA, aaLcr, omniAccuracy, hle, scicode, critpt, intelligenceIndex, bugHuntFixedOf105]

| Rank | Model | Normalized dimensions |
|---:|---|---|
| 1 | GPT-5.6 Sol | [55.6, 11.1, 100.0, 44.4, 55.6, 77.8, 66.7, 66.7, 66.7, 100.0, 66.7, 88.9] |
| 2 | GPT-6 Astra | [33.3, 66.7, 77.8, 22.2, 88.9, 22.2, 88.9, 77.8, 22.2, 77.8, 88.9, 100.0] |
| 3 | Claude Opus 5.5 | [0.0, 33.3, 77.8, 100.0, 100.0, 88.9, 100.0, 100.0, 100.0, 88.9, 100.0, 77.8] |
| 4 | Grok 4.6 | [77.8, 100.0, 33.3, 55.6, 77.8, 44.4, 22.2, 11.1, 33.3, 5.6, 22.2, 55.6] |
| 5 | GPT-5.6 Luna | [100.0, 0.0, 50.0, 11.1, 0.0, 66.7, 33.3, 0.0, 11.1, 44.4, 0.0, 66.7] |
| 6 | Kimi K3 | [44.4, 55.6, 77.8, 33.3, 33.3, 100.0, 44.4, 44.4, 88.9, 55.6, 33.3, 22.2] |
| 7 | Gemini 3.8 Flash | [88.9, 44.4, 50.0, 0.0, 44.4, 55.6, 55.6, 55.6, 55.6, 22.2, 11.1, 0.0] |
| 8 | GLM-5.3 | [66.7, 77.8, 11.1, 66.7, 66.7, 11.1, 11.1, 22.2, 77.8, 33.3, 44.4, 11.1] |
| 9 | Claude Opus 5 | [11.1, 22.2, 22.2, 88.9, 22.2, 0.0, 77.8, 88.9, 44.4, 66.7, 77.8, 44.4] |
| 10 | Qwen3.8 Max | [22.2, 88.9, 0.0, 77.8, 11.1, 33.3, 0.0, 33.3, 0.0, 5.6, 55.6, 33.3] |

## Coverage decision

The score is zero-gap across all retained dimensions for the 10 exact-match models. 12 models remain in the 22-model source roster without a primary rank because they lack exact eligible Bug Hunt results. Dropped candidate dimensions are listed below; missing values remain null rather than receiving neutral scores.

## External benchmark coverage

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) provides the current AA component scores used by this release. [LiveBench](https://livebench.ai/) Instruction Following is included in the primary score; its Overall Score and Cost Per Successful Task are supplemental views. [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) remains supplemental because coverage is incomplete in the exact-match cohort. See [raw-data.md](raw-data.md) for source-backed tables.
