# ValueRank v1.9.6 Scores

**Updated:** October 8, 2026 · **Cohort:** 16 · **Retained dimensions:** 16 · **Default cost basis:** API Costs (AA total evaluation cost)

API Costs uses the AA total evaluation cost in USD; Plan Costs divides that same value by the highest eligible subscription Value Multiple. The site switcher recalculates the main rank and cost-based charts using the selected basis.

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | AA eval-cost penalty (lower better) | Baseline priority coverage | Missing metrics |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | GPT-6.1 Sol | 74.3 | 74.6 | 2 | 12.42 | 88.64% (117/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 2 | GPT-5.6 Sol | 65.5 | 71.5 | 4 | 39.79 | 100.00% (132/132 priority) | none |
| 3 | GPT-6 Astra | 64.2 | 72.9 | 3 | 43.67 | 100.00% (132/132 priority) | none |
| 4 | GPT-6 Sol | 61.9 | 60.7 | 6 | 17.75 | 92.42% (122/132 priority) | Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 5 | Claude Opus 5.5 | 61.6 | 78.4 | 1 | 100.00 | 88.64% (117/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), GPQA Diamond (legacy) |
| 6 | Grok 4.7 | 58.4 | 70.1 | 5 | 57.04 | 92.42% (122/132 priority) | Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 7 | MiMo-V2.6-Pro | 54.1 | 41.9 | 10 | 2.37 | 69.70% (92/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy) |
| 8 | MiMo-V2.6-Flash | 51.6 | 25.8 | 15 | 1.26 | 54.55% (72/132 priority) | Terminal-Bench 4.0, Instruction Following (LiveBench), DeepSWE v1.1, GPQA Diamond (legacy), Bug Hunt Bench |
| 9 | Kimi K3 | 46.2 | 49.6 | 7 | 42.01 | 91.67% (121/132 priority) | Terminal-Bench 4.0, Speed |
| 10 | Grok 4.6 | 45.6 | 43.8 | 8 | 22.24 | 100.00% (132/132 priority) | none |
| 11 | GPT-5.6 Luna | 43.3 | 34.8 | 12 | 3.67 | 100.00% (132/132 priority) | none |
| 12 | Gemini 3.8 Flash | 42.7 | 38.7 | 11 | 18.63 | 100.00% (132/132 priority) | none |
| 13 | GLM-5.3 | 36.7 | 34.3 | 13 | 28.75 | 100.00% (132/132 priority) | none |
| 14 | GPT-6 Luna | 36.5 | 21.8 | 16 | 1.40 | 92.42% (122/132 priority) | Terminal-Bench 4.0, GPQA Diamond (legacy) |
| 15 | Claude Opus 5 | 35.8 | 42.6 | 9 | 83.54 | 100.00% (132/132 priority) | none |
| 16 | Qwen3.8 Max | 26.7 | 28.3 | 14 | 56.67 | 95.45% (126/132 priority) | Terminal-Bench 4.0 |

## Bug Hunt Emphasis Ranking

Bug Hunt is included in the main **16-model primary ranking** at **15.15%**. The companion emphasis view uses the same cohort and increases Bug Hunt's weight to **21.13%** by re-ranking the other retained dimensions within those models.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
| 1 | GPT-6.1 Sol | 44.3/105 | 77.4 | n=3 (mean) | max (verified first-party tier; below ultra ceiling) | Codex CLI / OpenAI ChatGPT account | 1 |
| 2 | GPT-5.6 Sol | 43.5/105 | 67.7 | n=2 (mean) | max (max) | Codex CLI / OpenAI | 2 |
| 3 | GPT-6 Astra | 45/105 | 67.0 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 3 |
| 4 | GPT-6 Sol | 29.3/105 | 63.3 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 4 |
| 5 | Claude Opus 5.5 | 41.7/105 | 62.8 | n=3 (mean) | max (max) | Claude Code / Anthropic | 5 |
| 6 | Grok 4.7 | 28.8/105 | 56.7 | n=4 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 6 |
| 7 | GPT-5.6 Luna | 31.3/105 | 46.5 | n=3 (mean) | max (max) | Codex CLI / OpenAI | 11 |
| 8 | Grok 4.6 | 28.7/105 | 45.8 | n=3 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 10 |
| 9 | Kimi K3 | 21/105 | 44.9 | n=1 (single) | default (default) | Claude Code / OpenRouter / OpenRouter | 9 |
| 10 | Gemini 3.8 Flash | 18/105 | 40.7 | n=3 (mean) | high (verified ceiling) | Antigravity CLI / Google | 12 |
| 11 | GLM-5.3 | 19/105 | 35.0 | n=1 (single) | max (verified setting) | Claude Code / Z.ai API / Z.ai API | 13 |
| 12 | Claude Opus 5 | 27/105 | 34.8 | n=1 (single) | max (max) | Claude Code / Anthropic | 15 |
| 13 | GPT-6 Luna | 18.3/105 | 34.1 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 14 |
| 14 | Qwen3.8 Max | 25.7/105 | 26.3 | n=3 (mean) | max (verified ceiling) | Claude Code / Alibaba API / Alibaba API | 16 |

Source: [Bug Hunt Bench](https://bughunt.productcompass.pm/) and the pinned [owner scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv) at commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c**. The run configuration details and coverage gaps are in [raw-data.md](raw-data.md).

## Pareto frontier

Undominated on composite cost versus quality: **Claude Opus 5.5, GPT-6.1 Sol, MiMo-V2.6-Pro, MiMo-V2.6-Flash**.

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
| 1 | GPT-6.1 Sol | [73.3, 50.0, ⊘, ⊘, 84.6, 40.0, 80.0, 53.3, 93.3, 80.0, ⊘, 20.0, 93.3, 90.0, 28.6, 92.9] |
| 2 | GPT-5.6 Sol | [40.0, 6.7, 50.0, 54.5, 92.3, 46.7, 46.7, 80.0, 73.3, 73.3, 75.0, 60.0, 100.0, 66.7, 71.4, 85.7] |
| 3 | GPT-6 Astra | [26.7, 66.7, 100.0, 90.9, 61.5, 26.7, 93.3, 26.7, 86.7, 86.7, 100.0, 33.3, 80.0, 90.0, 14.3, 100.0] |
| 4 | GPT-6 Sol | [66.7, 26.7, ⊘, 27.3, 76.9, 20.0, 53.3, 70.0, 60.0, 60.0, ⊘, 73.3, 73.3, 73.3, 57.1, 64.3] |
| 5 | Claude Opus 5.5 | [0.0, 33.3, ⊘, ⊘, 61.5, 100.0, 100.0, 86.7, 100.0, 100.0, ⊘, 100.0, 86.7, 100.0, 78.6, 78.6] |
| 6 | Grok 4.7 | [13.3, 86.7, ⊘, 81.8, 100.0, 86.7, 86.7, 6.7, 46.7, 40.0, ⊘, 66.7, 13.3, 56.7, 50.0, 57.1] |
| 7 | MiMo-V2.6-Pro | [86.7, 73.3, ⊘, ⊘, ⊘, 80.0, 33.3, 93.3, 20.0, 66.7, ⊘, 93.3, 60.0, 56.7, 7.1, 3.6] |
| 8 | MiMo-V2.6-Flash | [100.0, 50.0, ⊘, ⊘, ⊘, 60.0, 73.3, 0.0, 0.0, 0.0, ⊘, 0.0, 0.0, 13.3, 21.4, ⊘] |
| 9 | Kimi K3 | [33.3, 60.0, ⊘, 45.5, 61.5, 33.3, 26.7, 100.0, 53.3, 46.7, 56.2, 86.7, 53.3, 33.3, ⊘, 28.6] |
| 10 | Grok 4.6 | [53.3, 100.0, 33.3, 63.6, 30.8, 53.3, 66.7, 40.0, 26.7, 20.0, 56.2, 40.0, 13.3, 26.7, 42.9, 50.0] |
| 11 | GPT-5.6 Luna | [80.0, 0.0, 0.0, 9.1, 42.3, 13.3, 0.0, 70.0, 33.3, 13.3, 0.0, 13.3, 46.7, 3.3, 85.7, 71.4] |
| 12 | Gemini 3.8 Flash | [60.0, 40.0, 16.7, 100.0, 42.3, 6.7, 40.0, 46.7, 66.7, 53.3, 87.5, 53.3, 26.7, 20.0, 100.0, 3.6] |
| 13 | GLM-5.3 | [46.7, 80.0, 66.7, 36.4, 7.7, 66.7, 60.0, 20.0, 13.3, 26.7, 12.5, 80.0, 33.3, 43.3, 64.3, 21.4] |
| 14 | GPT-6 Luna | [93.3, 13.3, ⊘, 0.0, 23.1, 0.0, 6.7, 60.0, 40.0, 6.7, ⊘, 26.7, 40.0, 3.3, 92.9, 14.3] |
| 15 | Claude Opus 5 | [6.7, 20.0, 83.3, 18.2, 15.4, 93.3, 20.0, 13.3, 80.0, 93.3, 37.5, 46.7, 66.7, 80.0, 35.7, 42.9] |
| 16 | Qwen3.8 Max | [20.0, 93.3, ⊘, 72.7, 0.0, 73.3, 13.3, 33.3, 6.7, 33.3, 25.0, 6.7, 13.3, 43.3, 0.0, 35.7] |

## Coverage decision

The current AA Intelligence Index score-versus-total-benchmark-cost frontier is reconciled into the selected catalog. The primary rank uses each model's available exact-version values and renormalizes its retained priorities per row; the ranking table reports the available-priority percentage and missing metric names. 12 source candidates have no rankable primary score. Dropped candidate dimensions are listed below; missing values remain null rather than receiving zero or neutral scores.

## External benchmark coverage

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) provides the current AA component scores used by this release. [LiveBench](https://livebench.ai/) Instruction Following contributes for rows with an eligible value; its Overall Score and Cost Per Successful Task remain supplemental. [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) remains supplemental under this release's dimension-selection policy. See [raw-data.md](raw-data.md) for source-backed tables.
