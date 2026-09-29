# ValueRank v1.7.0 Scores

**Updated:** September 29, 2026 · **Cohort:** 21 · **Retained dimensions:** 12 · **Cost mode:** DeepSWE-only

## Final ranking

| Rank | Model | Overall | Quality | Quality Rank | Composite Cost |
|---:|---|---:|---:|---:|---:|
| 1 | Gemini 3.8 Flash | 68.4 | 67.6 | 6 | 8.94 |
| 2 | GPT-6 Astra | 64.7 | 78.7 | 1 | 16.78 |
| 3 | Grok 4.6 | 63.0 | 63.2 | 7 | 13.07 |
| 4 | GLM-5.3 Flash | 59.6 | 40.6 | 14 | 0.91 |
| 5 | Gemini 3.7 Flash | 57.6 | 47.1 | 12 | 7.69 |
| 6 | GPT-5.6 Sol | 57.2 | 72.4 | 3 | 24.47 |
| 7 | Kimi K3 | 56.3 | 68.6 | 5 | 17.61 |
| 8 | Claude Fable 5 | 54.6 | 78.0 | 2 | 50.80 |
| 9 | Qwen3.8 Max | 54.4 | 56.4 | 9 | 14.13 |
| 10 | Claude Opus 5 | 53.9 | 72.3 | 4 | 44.85 |
| 11 | GLM-5.3 | 52.9 | 59.0 | 8 | 15.11 |
| 12 | GPT-5.6 Luna | 51.7 | 33.7 | 16 | 2.31 |
| 13 | Muse Spark 1.2 | 49.0 | 46.2 | 13 | 14.02 |
| 14 | DeepSeek V4 Pro | 48.5 | 31.3 | 17 | 6.33 |
| 15 | Gemini 3.6 Flash | 45.1 | 30.9 | 18 | 8.37 |
| 16 | DeepSeek V4 Flash | 41.7 | 16.5 | 21 | 1.74 |
| 17 | GPT-5.5 | 41.7 | 51.9 | 10 | 27.39 |
| 18 | Gemini 3.5 Flash | 38.6 | 27.3 | 19 | 13.07 |
| 19 | Claude Opus 4.8 | 36.1 | 48.4 | 11 | 50.08 |
| 20 | GLM-5.2 | 29.9 | 22.8 | 20 | 14.85 |
| 21 | Claude Sonnet 5 | 25.2 | 37.1 | 15 | 100.00 |

## Bug Hunt Emphasis Ranking

This is a separate ranking for the **16/21** exact-match cohort. Bug Hunt Bench carries **20.41%** (priority 20 of 98); all existing retained dimensions are re-ranked within these 16 models. The 21-model zero-gap primary ranking above remains unchanged.

| Bug Hunt rank | Model | Fixed / 105 | Emphasis score | Runs / aggregation | Effort | Harness / route | Primary rank |
|---:|---|---:|---:|---|---|---|---:|
| 1 | GPT-6 Astra | 45/105 | 71.6 | n=3 (mean) | max (verified ceiling) | Codex CLI / OpenAI | 2 |
| 2 | Grok 4.6 | 28.7/105 | 63.8 | n=3 (mean) | xhigh (verified ceiling) | Grok Build CLI (ACP) / xAI | 3 |
| 3 | GPT-5.6 Sol | 43.5/105 | 63.6 | n=2 (mean) | max (max) | Codex CLI / OpenAI | 6 |
| 4 | Claude Fable 5 | 29/105 | 58.9 | n=1 (single) | max (max) | Claude Code / Anthropic | 8 |
| 5 | Gemini 3.8 Flash | 18/105 | 58.1 | n=3 (mean) | high (verified ceiling) | Antigravity CLI / Google | 1 |
| 6 | Claude Opus 5 | 27/105 | 56.3 | n=1 (single) | max (max) | Claude Code / Anthropic | 10 |
| 7 | GPT-5.6 Luna | 31.3/105 | 55.6 | n=3 (mean) | max (max) | Codex CLI / OpenAI | 12 |
| 8 | Qwen3.8 Max | 25.7/105 | 54.7 | n=3 (mean) | max (verified ceiling) | Claude Code / Alibaba API | 9 |
| 9 | Kimi K3 | 21/105 | 52.6 | n=1 (single) | default (default) | Claude Code / OpenRouter | 7 |
| 10 | GLM-5.3 Flash | 17.7/105 | 50.7 | n=3 (mean) | max (verified ceiling) | Claude Code / Z.ai API | 4 |
| 11 | GLM-5.3 | 19/105 | 50.6 | n=1 (single) | max (verified setting) | Claude Code / Z.ai API | 11 |
| 12 | DeepSeek V4 Flash | 21.7/105 | 39.9 | n=3 (mean) | max (verified ceiling) | Claude Code / DeepSeek API | 16 |
| 13 | DeepSeek V4 Pro | 16/105 | 38.8 | n=1 (single) | max (first-party; effort effect inconclusive) | Claude Code / DeepSeek API | 14 |
| 14 | Muse Spark 1.2 | 14/105 | 38.7 | n=1 (single) | default (default) | Claude Code / OpenRouter | 13 |
| 15 | Claude Opus 4.8 | 15/105 | 29.5 | n=1 (single) | max (max) | Claude Code / Anthropic | 19 |
| 16 | Claude Sonnet 5 | 9/105 | 16.5 | n=1 (single) | max (max) | Claude Code / Anthropic | 21 |

Source: [Bug Hunt Bench](https://bughunt.productcompass.pm/) and the pinned [owner scoreboard](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv) at commit **0630b120a81363c343ed7dfaf3c6d3be7f7da38c**. See [raw-data.md](raw-data.md) for all cohort rows and configurations.

## Pareto frontier

Undominated on composite cost versus quality: **GPT-6 Astra, Gemini 3.8 Flash, Gemini 3.7 Flash, GLM-5.3 Flash**.

## Weights

| Dimension | Weight | Direction |
|---|---:|---|
| Cost | 32.05% | lower |
| Non-Hallucination | 7.69% | higher |
| Instruction Following (LiveBench) | 6.41% | higher |
| DeepSWE | 8.97% | higher |
| [GDPval-AA v2.1](https://artificialanalysis.ai/evaluations/gdpval-aa) | 7.69% | higher |
| [AA-LCR v1.1](https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning) | 5.13% | higher |
| [AA-Omniscience Accuracy](https://artificialanalysis.ai/evaluations/omniscience) | 5.13% | higher |
| [HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam) | 5.13% | higher |
| [GPQA Diamond (legacy)](https://artificialanalysis.ai/evaluations/gpqa-diamond) | 5.13% | higher |
| [SciCode](https://artificialanalysis.ai/evaluations/scicode) | 5.13% | higher |
| [CritPt](https://artificialanalysis.ai/evaluations/critpt) | 3.85% | higher |
| [AA Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | 7.69% | higher |

## Normalized dimension matrix

Dimension order is the order in weights above:

[costComposite, omniNonHallucination, livebenchInstructionFollowing, deepswePassAt1, gdpvalV21, aaLcr, omniAccuracy, hle, gpqaDiamond, scicode, critpt, intelligenceIndex]

| Rank | Model | Normalized dimensions |
|---:|---|---|
| 1 | Gemini 3.8 Flash | [70.0, 50.0, 100.0, 95.0, 25.0, 65.0, 75.0, 75.0, 95.0, 70.0, 50.0, 50.0] |
| 2 | GPT-6 Astra | [35.0, 60.0, 80.0, 95.0, 60.0, 40.0, 95.0, 90.0, 100.0, 50.0, 95.0, 100.0] |
| 3 | Grok 4.6 | [62.5, 100.0, 55.0, 60.0, 80.0, 60.0, 30.0, 40.0, 80.0, 60.0, 35.0, 65.0] |
| 4 | GLM-5.3 Flash | [100.0, 90.0, 0.0, 42.5, 85.0, 40.0, 5.0, 15.0, 25.0, 15.0, 15.0, 60.0] |
| 5 | Gemini 3.7 Flash | [80.0, 25.0, 95.0, 50.0, 15.0, 80.0, 70.0, 5.0, 40.0, 95.0, 0.0, 45.0] |
| 6 | GPT-5.6 Sol | [25.0, 10.0, 50.0, 85.0, 70.0, 90.0, 85.0, 85.0, 90.0, 75.0, 100.0, 85.0] |
| 7 | Kimi K3 | [30.0, 55.0, 45.0, 72.5, 65.0, 100.0, 45.0, 70.0, 80.0, 90.0, 75.0, 70.0] |
| 8 | Claude Fable 5 | [5.0, 30.0, 90.0, 80.0, 75.0, 75.0, 100.0, 100.0, 50.0, 100.0, 85.0, 90.0] |
| 9 | Qwen3.8 Max | [50.0, 85.0, 65.0, 30.0, 95.0, 52.5, 10.0, 55.0, 60.0, 20.0, 35.0, 80.0] |
| 10 | Claude Opus 5 | [15.0, 40.0, 25.0, 95.0, 100.0, 20.0, 90.0, 95.0, 70.0, 65.0, 90.0, 95.0] |
| 11 | GLM-5.3 | [40.0, 80.0, 35.0, 72.5, 90.0, 27.5, 15.0, 45.0, 30.0, 85.0, 55.0, 75.0] |
| 12 | GPT-5.6 Luna | [90.0, 5.0, 5.0, 60.0, 45.0, 85.0, 35.0, 10.0, 17.5, 30.0, 60.0, 25.0] |
| 13 | Muse Spark 1.2 | [55.0, 75.0, 70.0, 25.0, 55.0, 15.0, 40.0, 60.0, 5.0, 80.0, 35.0, 40.0] |
| 14 | DeepSeek V4 Pro | [85.0, 0.0, 15.0, 42.5, 40.0, 52.5, 55.0, 25.0, 60.0, 5.0, 45.0, 20.0] |
| 15 | Gemini 3.6 Flash | [75.0, 45.0, 75.0, 10.0, 5.0, 40.0, 60.0, 20.0, 60.0, 25.0, 5.0, 10.0] |
| 16 | DeepSeek V4 Flash | [95.0, 15.0, 20.0, 15.0, 30.0, 27.5, 25.0, 0.0, 10.0, 0.0, 20.0, 15.0] |
| 17 | GPT-5.5 | [20.0, 20.0, 40.0, 60.0, 10.0, 95.0, 80.0, 65.0, 80.0, 55.0, 80.0, 35.0] |
| 18 | Gemini 3.5 Flash | [62.5, 35.0, 85.0, 0.0, 0.0, 0.0, 65.0, 50.0, 45.0, 35.0, 10.0, 0.0] |
| 19 | Claude Opus 4.8 | [10.0, 70.0, 60.0, 35.0, 35.0, 5.0, 50.0, 80.0, 35.0, 45.0, 67.5, 55.0] |
| 20 | GLM-5.2 | [45.0, 95.0, 10.0, 5.0, 20.0, 10.0, 0.0, 30.0, 0.0, 10.0, 67.5, 5.0] |
| 21 | Claude Sonnet 5 | [0.0, 65.0, 30.0, 20.0, 50.0, 70.0, 20.0, 35.0, 17.5, 40.0, 25.0, 30.0] |

## Coverage decision

The score is zero-gap across all retained dimensions. The dropped candidate dimensions are listed below with their missing cohort rows; their values remain null rather than being replaced by a neutral score.

## External benchmark supplements

[Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) provides the current AA component scores used by this release. [LiveBench](https://livebench.ai/) provides the four-task Instruction Following view and the Overall Score versus Cost Per Successful Task Pareto analysis; [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) provides the current standalone terminal-agent leaderboard. Bug Hunt Bench supplies a separately weighted matched-cohort emphasis ranking with exact configuration details. See [raw-data.md](raw-data.md) for the source-backed tables.
