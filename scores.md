# ValueRank v1.9.4 Scores

**Updated:** October 8, 2026 · **Cohort:** 13 · **Retained dimensions:** 12 · **Default cost basis:** API Costs (AA total evaluation cost)

API Costs uses the AA total evaluation cost in USD; Plan Costs divides that same value by the highest eligible subscription Value Multiple. The site switcher recalculates the main rank and cost-based charts using the selected basis.

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | AA eval-cost penalty (lower better) |
|---:|---|---:|---:|---:|---:|
| 1 | GPT-6 Sol | 70.5 | 66.9 | 5 | 17.75 |
| 2 | GPT-5.6 Sol | 70.0 | 75.8 | 2 | 39.79 |
| 3 | GPT-6 Astra | 64.8 | 73.9 | 3 | 43.67 |
| 4 | Claude Opus 5.5 | 63.6 | 81.9 | 1 | 100.00 |
| 5 | Grok 4.7 | 57.8 | 69.6 | 4 | 57.04 |
| 6 | GPT-5.6 Luna | 50.8 | 39.0 | 9 | 3.67 |
| 7 | Kimi K3 | 49.3 | 51.4 | 6 | 42.01 |
| 8 | Grok 4.6 | 48.5 | 43.3 | 7 | 22.24 |
| 9 | Gemini 3.8 Flash | 41.5 | 31.9 | 10 | 18.63 |
| 10 | GLM-5.3 | 36.3 | 30.0 | 11 | 28.75 |
| 11 | GPT-6 Luna | 35.6 | 17.1 | 13 | 1.40 |
| 12 | Claude Opus 5 | 34.7 | 42.3 | 8 | 83.54 |
| 13 | Qwen3.8 Max | 26.5 | 26.9 | 12 | 56.67 |

## Bug Hunt Emphasis Ranking

Bug Hunt is included in the main **13-model primary ranking** at **17.86%**. The companion emphasis view uses the same cohort and increases Bug Hunt's weight to **24.59%** by re-ranking the other retained dimensions within those models.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
| 1 | GPT-5.6 Sol | 43.5/105 | 71.8 | n=2 (mean) | max (max) | Codex CLI / OpenAI | 2 |
| 2 | GPT-6 Sol | 29.3/105 | 70.2 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 1 |
| 3 | GPT-6 Astra | 45/105 | 67.7 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 3 |
| 4 | Claude Opus 5.5 | 41.7/105 | 65.2 | n=3 (mean) | max (max) | Claude Code / Anthropic | 4 |
| 5 | Grok 4.7 | 28.8/105 | 57.8 | n=4 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 5 |
| 6 | GPT-5.6 Luna | 31.3/105 | 52.8 | n=3 (mean) | max (max) | Codex CLI / OpenAI | 6 |
| 7 | Grok 4.6 | 28.7/105 | 48.6 | n=3 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 8 |
| 8 | Kimi K3 | 21/105 | 47.3 | n=1 (single) | default (default) | Claude Code / OpenRouter / OpenRouter | 7 |
| 9 | Gemini 3.8 Flash | 18/105 | 38.1 | n=3 (mean) | high (verified ceiling) | Antigravity CLI / Google | 9 |
| 10 | Claude Opus 5 | 27/105 | 35.3 | n=1 (single) | max (max) | Claude Code / Anthropic | 12 |
| 11 | GLM-5.3 | 19/105 | 34.7 | n=1 (single) | max (verified setting) | Claude Code / Z.ai API / Z.ai API | 10 |
| 12 | GPT-6 Luna | 18.3/105 | 33.4 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 11 |
| 13 | Qwen3.8 Max | 25.7/105 | 27.0 | n=3 (mean) | max (verified ceiling) | Claude Code / Alibaba API / Alibaba API | 13 |

Source: [Bug Hunt Bench](https://bughunt.productcompass.pm/) and the pinned [owner scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv) at commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c**. The run configuration details and coverage gaps are in [raw-data.md](raw-data.md).

## Pareto frontier

Undominated on composite cost versus quality: **GPT-5.6 Sol, GPT-5.6 Luna, Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna**.

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
| 1 | GPT-6 Sol | [83.3, 33.3, 83.3, 25.0, 58.3, 70.8, 58.3, 66.7, 75.0, 75.0, 75.0, 66.7] |
| 2 | GPT-5.6 Sol | [50.0, 8.3, 91.7, 50.0, 50.0, 83.3, 75.0, 75.0, 58.3, 100.0, 66.7, 91.7] |
| 3 | GPT-6 Astra | [33.3, 66.7, 66.7, 33.3, 91.7, 25.0, 91.7, 83.3, 25.0, 83.3, 91.7, 100.0] |
| 4 | Claude Opus 5.5 | [0.0, 41.7, 66.7, 100.0, 100.0, 91.7, 100.0, 100.0, 100.0, 91.7, 100.0, 83.3] |
| 5 | Grok 4.7 | [16.7, 83.3, 100.0, 83.3, 83.3, 0.0, 41.7, 41.7, 66.7, 8.3, 58.3, 58.3] |
| 6 | GPT-5.6 Luna | [91.7, 0.0, 45.8, 16.7, 0.0, 70.8, 25.0, 8.3, 8.3, 50.0, 8.3, 75.0] |
| 7 | Kimi K3 | [41.7, 58.3, 66.7, 41.7, 33.3, 100.0, 50.0, 50.0, 91.7, 58.3, 33.3, 25.0] |
| 8 | Grok 4.6 | [66.7, 100.0, 33.3, 58.3, 75.0, 41.7, 16.7, 16.7, 33.3, 8.3, 25.0, 50.0] |
| 9 | Gemini 3.8 Flash | [75.0, 50.0, 45.8, 8.3, 41.7, 50.0, 66.7, 58.3, 50.0, 25.0, 16.7, 0.0] |
| 10 | GLM-5.3 | [58.3, 75.0, 8.3, 66.7, 66.7, 16.7, 8.3, 25.0, 83.3, 33.3, 41.7, 16.7] |
| 11 | GPT-6 Luna | [100.0, 16.7, 25.0, 0.0, 8.3, 58.3, 33.3, 0.0, 16.7, 41.7, 0.0, 8.3] |
| 12 | Claude Opus 5 | [8.3, 25.0, 16.7, 91.7, 25.0, 8.3, 83.3, 91.7, 41.7, 66.7, 83.3, 41.7] |
| 13 | Qwen3.8 Max | [25.0, 91.7, 0.0, 75.0, 16.7, 33.3, 0.0, 33.3, 0.0, 8.3, 50.0, 33.3] |

## Coverage decision

The score is zero-gap across all retained dimensions for the 13 exact-match models. 14 models remain in the 27-model source roster without a primary rank because they lack exact eligible Bug Hunt results. Dropped candidate dimensions are listed below; missing values remain null rather than receiving neutral scores.

## External benchmark coverage

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) provides the current AA component scores used by this release. [LiveBench](https://livebench.ai/) Instruction Following remains supplemental because the pinned release lacks full coverage in the exact-match cohort; its Overall Score and Cost Per Successful Task are also supplemental. [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) remains supplemental because coverage is incomplete in the exact-match cohort. See [raw-data.md](raw-data.md) for source-backed tables.
