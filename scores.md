# ValueRank v1.9.8 Scores

**Updated:** October 18, 2026 · **Cohort:** 19 · **Retained dimensions:** 16 · **Default cost basis:** API Costs (AA total evaluation cost)

API Costs uses the AA total evaluation cost in USD; Plan Costs divides that same value by the highest eligible subscription Value Multiple and by the model's AA Intelligence Index (USD per Index point). The site switcher recalculates the main rank and cost-based charts using the selected basis.

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | AA eval-cost penalty (lower better) | Baseline priority coverage | Missing metrics |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Gemini 4 Argon | 74.1 | 82.6 | 2 | 27.64 | 84.85% (112/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy), Speed |
| 2 | GPT-6.1 Sol | 70.1 | 71.0 | 5 | 12.42 | 88.64% (117/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 3 | Claude Sonnet 5.5 | 69.5 | 85.4 | 1 | 83.36 | 88.64% (117/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 4 | GPT-6 Astra | 64.1 | 75.2 | 4 | 43.67 | 81.06% (107/132 priority) | DeepSWE v1.1 |
| 5 | GPT-5.6 Sol | 62.9 | 69.8 | 6 | 39.79 | 100.00% (132/132 priority) | none |
| 6 | Claude Opus 5.5 | 60.3 | 76.7 | 3 | 100.00 | 88.64% (117/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 7 | GPT-6 Sol | 58.6 | 59.3 | 8 | 17.64 | 92.42% (122/132 priority) | Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 8 | Grok 4.7 | 56.6 | 66.9 | 7 | 57.04 | 92.42% (122/132 priority) | Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 9 | MiMo-V2.6-Pro | 53.7 | 42.7 | 10 | 2.37 | 69.70% (92/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy) |
| 10 | MiMo-V2.6-Flash | 50.7 | 24.5 | 16 | 1.26 | 54.55% (72/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy), Bug Hunt Bench |
| 11 | GPT-5.6 Luna | 46.0 | 38.6 | 13 | 3.67 | 100.00% (132/132 priority) | none |
| 12 | Gemini 3.8 Flash | 43.5 | 42.0 | 11 | 18.63 | 100.00% (132/132 priority) | none |
| 13 | GPT-6 Luna | 42.4 | 29.0 | 15 | 1.40 | 92.42% (122/132 priority) | Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 14 | Claude Opus 5 | 40.7 | 48.9 | 9 | 83.54 | 100.00% (132/132 priority) | none |
| 15 | GLM-5.3 | 40.5 | 40.8 | 12 | 28.75 | 100.00% (132/132 priority) | none |
| 16 | Claude Haiku 5.5 | 37.9 | 24.0 | 17 | 1.81 | 88.64% (117/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 17 | DeepSeek V4 Flash | 31.4 | 21.9 | 18 | 5.45 | 100.00% (132/132 priority) | none |
| 18 | Qwen3.8 Max | 31.3 | 33.5 | 14 | 56.67 | 95.45% (126/132 priority) | Terminal-Bench 4.0 |
| 19 | DeepSeek V4 Pro | 26.5 | 17.9 | 19 | 12.89 | 95.45% (126/132 priority) | Terminal-Bench 4.0 |

## Bug Hunt Emphasis Ranking

Bug Hunt is included in the main **19-model primary ranking** at **15.15%**. The companion emphasis view uses the same cohort and increases Bug Hunt's weight to **21.13%** by re-ranking the other retained dimensions within those models.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
| 1 | Gemini 4 Argon | 40.7/105 | 74.5 | n=3 (mean) | high (verified ceiling) | Antigravity CLI / Google | 1 |
| 2 | GPT-6.1 Sol | 44.3/105 | 73.7 | n=3 (mean) | max (verified first-party tier; below ultra ceiling) | Codex CLI / OpenAI ChatGPT account | 2 |
| 3 | Claude Sonnet 5.5 | 51.3/105 | 71.9 | n=3 (mean) | max (max) | Claude Code / Anthropic | 3 |
| 4 | GPT-5.6 Sol | 43.5/105 | 65.9 | n=2 (mean) | max (max) | Codex CLI / OpenAI | 5 |
| 5 | Claude Opus 5.5 | 41.7/105 | 62.5 | n=3 (mean) | max (max) | Claude Code / Anthropic | 6 |
| 6 | GPT-6 Sol | 29.3/105 | 60.6 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 7 |
| 7 | Grok 4.7 | 29/105 | 56.5 | n=5 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 8 |
| 8 | GPT-5.6 Luna | 31.3/105 | 49.4 | n=3 (mean) | max (max) | Codex CLI / OpenAI | 11 |
| 9 | Gemini 3.8 Flash | 18/105 | 42.1 | n=3 (mean) | high (verified ceiling) | Antigravity CLI / Google | 12 |
| 10 | Claude Opus 5 | 27/105 | 41.9 | n=1 (single) | max (max) | Claude Code / Anthropic | 14 |
| 11 | GPT-6 Luna | 18.3/105 | 40.7 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 13 |
| 12 | GLM-5.3 | 19/105 | 39.7 | n=1 (single) | max (verified setting) | Claude Code / Z.ai API / Z.ai API | 15 |
| 13 | Claude Haiku 5.5 | 18.3/105 | 36.4 | n=3 (mean) | xhigh (xhigh) | Claude Code / Anthropic | 16 |
| 14 | Qwen3.8 Max | 25.7/105 | 32.9 | n=3 (mean) | max (verified ceiling) | Claude Code / Alibaba API / Alibaba API | 18 |
| 15 | DeepSeek V4 Flash | 21.7/105 | 32.8 | n=3 (mean) | max (verified ceiling) | Claude Code / DeepSeek API / DeepSeek API | 17 |
| 16 | DeepSeek V4 Pro | 16/105 | 25.5 | n=1 (single) | max (first-party; effort effect inconclusive) | Claude Code / DeepSeek API / DeepSeek API | 19 |

Source: [Bug Hunt Bench](https://bughunt.productcompass.pm/) and the pinned [owner scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/aec976170df89a371384174ca87646a9a8c82415/results/combined-scoreboard.csv) at commit **aec976170df89a371384174ca87646a9a8c82415**. The run configuration details and coverage gaps are in [raw-data.md](raw-data.md).

## Pareto frontier

Undominated on composite cost versus quality: **GPT-6.1 Sol, GPT-6 Luna, MiMo-V2.6-Pro, MiMo-V2.6-Flash, Claude Sonnet 5.5, Gemini 4 Argon**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
| Cost | 18.94% | lower |
| Non-Hallucination | 4.55% | higher |
| [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) | 4.55% | higher |
| Instruction Following (LiveBench) | 3.79% | higher |
| DeepSWE v1.1 | 18.94% | higher |
| [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 4.55% | higher |
| [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | 3.79% | higher |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 3.03% | higher |
| [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 3.03% | higher |
| [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 3.03% | higher |
| [GPQA Diamond (legacy)](https://artificialanalysis.ai/evaluations/gpqa-diamond) | 3.03% | higher |
| [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 3.03% | higher |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 2.27% | higher |
| [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 4.55% | higher |
| Speed | 3.79% | higher |
| [Bug Hunt Bench](https://bughunt.productcompass.pm/) | 15.15% | higher |

## Normalized dimension matrix

Dimension order is the order in weights above:

[costComposite, omniNonHallucination, terminalBenchV4, livebenchInstructionFollowing, deepswePassAt1, gdpvalV21, automationBenchAA, aaLcr, omniAccuracy, hle, gpqaDiamond, scicode, critpt, intelligenceIndex, speed, bugHuntFixedOf105]

| Rank | Model | Normalized dimensions |
|---:|---|---|
| 1 | Gemini 4 Argon | [44.4, 100.0, ⊘, ⊘, 100.0, 61.1, 100.0, 27.8, 55.6, 94.4, ⊘, 94.4, 61.1, 88.9, ⊘, 70.6] |
| 2 | GPT-6.1 Sol | [66.7, 55.6, ⊘, ⊘, 73.3, 44.4, 72.2, 66.7, 94.4, 72.2, ⊘, 33.3, 91.7, 80.6, 29.4, 88.2] |
| 3 | Claude Sonnet 5.5 | [11.1, 66.7, ⊘, ⊘, 80.0, 94.4, 94.4, 61.1, 61.1, 88.9, ⊘, 88.9, 80.6, 94.4, 82.4, 100.0] |
| 4 | GPT-6 Astra | [27.8, 61.1, 100.0, 90.9, ⊘, 38.9, 83.3, 38.9, 88.9, 77.8, 100.0, 44.4, 80.6, 80.6, 17.6, 94.1] |
| 5 | GPT-5.6 Sol | [33.3, 11.1, 50.0, 63.6, 86.7, 55.6, 50.0, 88.9, 77.8, 66.7, 75.0, 61.1, 100.0, 61.1, 47.1, 82.4] |
| 6 | Claude Opus 5.5 | [0.0, 38.9, ⊘, ⊘, 60.0, 100.0, 88.9, 94.4, 100.0, 100.0, ⊘, 100.0, 91.7, 100.0, 58.8, 76.5] |
| 7 | GPT-6 Sol | [55.6, 33.3, ⊘, 45.5, 66.7, 27.8, 55.6, 80.6, 66.7, 55.6, ⊘, 72.2, 72.2, 66.7, 64.7, 58.8] |
| 8 | Grok 4.7 | [16.7, 88.9, ⊘, 81.8, 93.3, 83.3, 77.8, 5.6, 44.4, 44.4, ⊘, 66.7, 13.9, 52.8, 52.9, 52.9] |
| 9 | MiMo-V2.6-Pro | [83.3, 77.8, ⊘, ⊘, ⊘, 77.8, 38.9, 100.0, 16.7, 61.1, ⊘, 83.3, 55.6, 52.8, 5.9, 8.8] |
| 10 | MiMo-V2.6-Flash | [100.0, 50.0, ⊘, ⊘, ⊘, 50.0, 66.7, 0.0, 0.0, 0.0, ⊘, 11.1, 0.0, 19.4, 11.8, ⊘] |
| 11 | GPT-5.6 Luna | [77.8, 5.6, 0.0, 9.1, 53.3, 22.2, 5.6, 80.6, 33.3, 16.7, 12.5, 27.8, 44.4, 11.1, 76.5, 64.7] |
| 12 | Gemini 3.8 Flash | [50.0, 44.4, 16.7, 100.0, 46.7, 11.1, 44.4, 55.6, 72.2, 50.0, 87.5, 55.6, 27.8, 30.6, 88.2, 8.8] |
| 13 | GPT-6 Luna | [94.4, 22.2, ⊘, 0.0, 40.0, 0.0, 11.1, 72.2, 38.9, 5.6, ⊘, 38.9, 38.9, 19.4, 70.6, 20.6] |
| 14 | Claude Opus 5 | [5.6, 27.8, 83.3, 36.4, 33.3, 88.9, 27.8, 16.7, 83.3, 83.3, 62.5, 50.0, 66.7, 72.2, 23.5, 47.1] |
| 15 | GLM-5.3 | [38.9, 83.3, 66.7, 54.5, 26.7, 66.7, 61.1, 27.8, 11.1, 27.8, 25.0, 77.8, 33.3, 41.7, 41.2, 29.4] |
| 16 | Claude Haiku 5.5 | [88.9, 72.2, ⊘, ⊘, 0.0, 33.3, 0.0, 11.1, 22.2, 33.3, ⊘, 16.7, 50.0, 30.6, 100.0, 20.6] |
| 17 | DeepSeek V4 Flash | [72.2, 16.7, 33.3, 27.3, 13.3, 5.6, 16.7, 27.8, 27.8, 11.1, 0.0, 0.0, 5.6, 0.0, 94.1, 35.3] |
| 18 | Qwen3.8 Max | [22.2, 94.4, ⊘, 72.7, 6.7, 72.2, 22.2, 47.2, 5.6, 38.9, 43.8, 22.2, 13.9, 41.7, 0.0, 41.2] |
| 19 | DeepSeek V4 Pro | [61.1, 0.0, ⊘, 18.2, 20.0, 16.7, 33.3, 47.2, 50.0, 22.2, 43.8, 5.6, 22.2, 5.6, 35.3, 0.0] |

## Coverage decision

The current AA Intelligence Index score-versus-total-benchmark-cost frontier, and its near-frontier families, are reconciled into the selected catalog (see Model inclusion in methodology.md). The primary rank uses each model's available exact-version values and renormalizes its retained priorities per row; the ranking table reports the available-priority percentage and missing metric names. 12 source candidates have no rankable primary score. Dropped candidate dimensions are listed below; missing values remain null rather than receiving zero or neutral scores.

## External benchmark coverage

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) provides the current AA component scores used by this release. [LiveBench](https://livebench.ai/) Instruction Following contributes for rows with an eligible value; its Overall Score and Cost Per Successful Task remain supplemental. [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) remains supplemental under this release's dimension-selection policy. See [raw-data.md](raw-data.md) for source-backed tables.
