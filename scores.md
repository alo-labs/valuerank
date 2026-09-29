# ValueRank v1.9.0 Scores

**Updated:** September 29, 2026 · **Cohort:** 9 · **Retained dimensions:** 14 · **Default cost basis:** API Costs (AA total evaluation cost)

API Costs uses the AA total evaluation cost in USD; Plan Costs divides that same value by the highest eligible subscription Value Multiple. The site switcher recalculates the main rank and cost-based charts using the selected basis.

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | AA eval-cost penalty (lower better) |
|---:|---|---:|---:|---:|---:|
| 1 | GPT-5.6 Sol | 72.2 | 78.0 | 2 | 47.63 |
| 2 | GPT-6 Astra | 68.8 | 80.3 | 1 | 52.28 |
| 3 | Grok 4.6 | 55.2 | 50.1 | 4 | 26.62 |
| 4 | Kimi K3 | 51.3 | 54.9 | 3 | 50.28 |
| 5 | GPT-5.6 Luna | 50.7 | 37.8 | 7 | 4.40 |
| 6 | Gemini 3.8 Flash | 50.1 | 40.4 | 6 | 22.31 |
| 7 | GLM-5.3 | 37.5 | 31.0 | 9 | 34.41 |
| 8 | Claude Opus 5 | 36.5 | 46.0 | 5 | 100.00 |
| 9 | Qwen3.8 Max | 27.6 | 31.6 | 8 | 67.83 |

## Bug Hunt Emphasis Ranking

Bug Hunt is included in the main **9-model primary ranking** at **16.53%**. The companion emphasis view uses the same cohort and increases Bug Hunt's weight to **22.90%** by re-ranking the other retained dimensions within those models.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
| 1 | GPT-5.6 Sol | 43.5/105 | 73.4 | n=2 (mean) | max (max) | Codex CLI / OpenAI | 1 |
| 2 | GPT-6 Astra | 45/105 | 71.2 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 2 |
| 3 | Grok 4.6 | 28.7/105 | 55.8 | n=3 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 3 |
| 4 | GPT-5.6 Luna | 31.3/105 | 52.5 | n=3 (mean) | max (max) | Codex CLI / OpenAI | 5 |
| 5 | Kimi K3 | 21/105 | 49.3 | n=1 (single) | default (default) | Claude Code / OpenRouter / OpenRouter | 4 |
| 6 | Gemini 3.8 Flash | 18/105 | 46.3 | n=3 (mean) | high (verified ceiling) | Antigravity CLI / Google | 6 |
| 7 | Claude Opus 5 | 27/105 | 37.5 | n=1 (single) | max (max) | Claude Code / Anthropic | 8 |
| 8 | GLM-5.3 | 19/105 | 35.6 | n=1 (single) | max (verified setting) | Claude Code / Z.ai API / Z.ai API | 7 |
| 9 | Qwen3.8 Max | 25.7/105 | 28.4 | n=3 (mean) | max (verified ceiling) | Claude Code / Alibaba API / Alibaba API | 9 |

Source: [Bug Hunt Bench](https://bughunt.productcompass.pm/) and the pinned [owner scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv) at commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c**. The run configuration details and coverage gaps are in [raw-data.md](raw-data.md).

## Pareto frontier

Undominated on composite cost versus quality: **GPT-6 Astra, Gemini 3.8 Flash, GPT-5.6 Sol, Grok 4.6, GPT-5.6 Luna**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
| Cost | 20.66% | lower |
| Non-Hallucination | 4.96% | higher |
| Instruction Following (LiveBench) | 4.13% | higher |
| DeepSWE v1.1 | 20.66% | higher |
| [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 4.96% | higher |
| [AutomationBench-AA](https://artificialanalysis.ai/evaluations/automationbench-aa) | 4.13% | higher |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 3.31% | higher |
| [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 3.31% | higher |
| [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 3.31% | higher |
| [GPQA Diamond (legacy)](https://artificialanalysis.ai/evaluations/gpqa-diamond) | 3.31% | higher |
| [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 3.31% | higher |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 2.48% | higher |
| [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 4.96% | higher |
| [Bug Hunt Bench](https://bughunt.productcompass.pm/) | 16.53% | higher |

## Normalized dimension matrix

Dimension order is the order in weights above:

[costComposite, omniNonHallucination, livebenchInstructionFollowing, deepswePassAt1, gdpvalV21, automationBenchAA, aaLcr, omniAccuracy, hle, gpqaDiamond, scicode, critpt, intelligenceIndex, bugHuntFixedOf105]

| Rank | Model | Normalized dimensions |
|---:|---|---|
| 1 | GPT-5.6 Sol | [50.0, 12.5, 50.0, 100.0, 50.0, 62.5, 87.5, 75.0, 75.0, 75.0, 75.0, 100.0, 75.0, 87.5] |
| 2 | GPT-6 Astra | [25.0, 62.5, 87.5, 81.2, 25.0, 100.0, 25.0, 100.0, 87.5, 100.0, 25.0, 87.5, 100.0, 100.0] |
| 3 | Grok 4.6 | [75.0, 100.0, 62.5, 37.5, 62.5, 87.5, 50.0, 25.0, 12.5, 56.2, 37.5, 6.2, 25.0, 62.5] |
| 4 | Kimi K3 | [37.5, 50.0, 37.5, 81.2, 37.5, 37.5, 100.0, 50.0, 50.0, 56.2, 100.0, 62.5, 37.5, 25.0] |
| 5 | GPT-5.6 Luna | [100.0, 0.0, 0.0, 56.2, 12.5, 0.0, 75.0, 37.5, 0.0, 0.0, 12.5, 50.0, 0.0, 75.0] |
| 6 | Gemini 3.8 Flash | [87.5, 37.5, 100.0, 56.2, 0.0, 50.0, 62.5, 62.5, 62.5, 87.5, 62.5, 25.0, 12.5, 0.0] |
| 7 | GLM-5.3 | [62.5, 75.0, 25.0, 12.5, 75.0, 75.0, 12.5, 12.5, 25.0, 12.5, 87.5, 37.5, 50.0, 12.5] |
| 8 | Claude Opus 5 | [0.0, 25.0, 12.5, 25.0, 100.0, 25.0, 0.0, 87.5, 100.0, 37.5, 50.0, 75.0, 87.5, 50.0] |
| 9 | Qwen3.8 Max | [12.5, 87.5, 75.0, 0.0, 87.5, 12.5, 37.5, 0.0, 37.5, 25.0, 0.0, 6.2, 62.5, 37.5] |

## Coverage decision

The score is zero-gap across all retained dimensions for the 9 exact-match models. 12 models remain in the 21-model source roster without a primary rank because they lack exact eligible Bug Hunt results. Dropped candidate dimensions are listed below; missing values remain null rather than receiving neutral scores.

## External benchmark coverage

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) provides the current AA component scores used by this release. [LiveBench](https://livebench.ai/) Instruction Following is included in the primary score; its Overall Score and Cost Per Successful Task are supplemental views. [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) remains supplemental because coverage is incomplete in the exact-match cohort. See [raw-data.md](raw-data.md) for source-backed tables.
