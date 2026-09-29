# ValueRank v1.7.0 Raw Data

**Version:** v1.6.0 · **Updated:** September 29, 2026 · **DeepSWE source update:** September 22, 2026 · **AA source:** [Artificial Analysis Intelligence Index v4.3.2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)

All 21 current DeepSWE Best models are retained. Raw AA values keep their source units: Elo fields remain Elo, and ratio fields are shown as percentages. The machine-readable files preserve fractions where applicable. **Gemini 3.7 Flash** has an AA Intelligence Index estimate; it is labelled in the matrix. Benchmark-owner results, estimates, and provider claims remain source-typed.

## Selected AA pages

| Model | AA slug | AA effort | Source |
|---|---|---|---|
| Gemini 3.8 Flash | gemini-3-8-flash | high | [page](https://artificialanalysis.ai/models/gemini-3-8-flash) |
| GPT-6 Astra | gpt-6-astra-xhigh | xhigh | [page](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) |
| Grok 4.6 | grok-4-6-medium | medium | [page](https://artificialanalysis.ai/models/grok-4-6-medium) |
| GLM-5.3 Flash | glm-5-3-flash | max | [page](https://artificialanalysis.ai/models/glm-5-3-flash) |
| Gemini 3.7 Flash | gemini-3-7-flash-medium | medium | [page](https://artificialanalysis.ai/models/gemini-3-7-flash-medium) |
| GPT-5.6 Sol | gpt-5-6-sol | max | [page](https://artificialanalysis.ai/models/gpt-5-6-sol) |
| Kimi K3 | kimi-k3 | max | [page](https://artificialanalysis.ai/models/kimi-k3) |
| Claude Fable 5 | claude-fable-5 | max | [page](https://artificialanalysis.ai/models/claude-fable-5) |
| Qwen3.8 Max | qwen3-8-max | not stated | [page](https://artificialanalysis.ai/models/qwen3-8-max) |
| Claude Opus 5 | claude-opus-5 | max | [page](https://artificialanalysis.ai/models/claude-opus-5) |
| GLM-5.3 | glm-5-3 | max | [page](https://artificialanalysis.ai/models/glm-5-3) |
| GPT-5.6 Luna | gpt-5-6-luna | max | [page](https://artificialanalysis.ai/models/gpt-5-6-luna) |
| Muse Spark 1.2 | muse-spark-1-2 | xhigh | [page](https://artificialanalysis.ai/models/muse-spark-1-2) |
| DeepSeek V4 Pro | deepseek-v4-pro | max | [page](https://artificialanalysis.ai/models/deepseek-v4-pro) |
| Gemini 3.6 Flash | gemini-3-6-flash | high | [page](https://artificialanalysis.ai/models/gemini-3-6-flash) |
| DeepSeek V4 Flash | deepseek-v4-flash | max | [page](https://artificialanalysis.ai/models/deepseek-v4-flash) |
| GPT-5.5 | gpt-5-5 | xhigh | [page](https://artificialanalysis.ai/models/gpt-5-5) |
| Gemini 3.5 Flash | gemini-3-5-flash | high | [page](https://artificialanalysis.ai/models/gemini-3-5-flash) |
| Claude Opus 4.8 | claude-opus-4-8 | max | [page](https://artificialanalysis.ai/models/claude-opus-4-8) |
| GLM-5.2 | glm-5-2 | max | [page](https://artificialanalysis.ai/models/glm-5-2) |
| Claude Sonnet 5 | claude-sonnet-5 | max | [page](https://artificialanalysis.ai/models/claude-sonnet-5) |

## AA source input matrix

| # | Model | Effort | DeepSWE pass@1 | DeepSWE avg cost | AA-Briefcase Elo | GDPval-AA v2.1 | AutomationBench-AA | AA Terminal-Bench 4.0 | AA Terminal-Bench 2.1 legacy | τ³-Banking legacy | SciCode | GDP.pdf all-pass | AA-LCR v1.1 | HLE | GPQA legacy | CritPt | Omni Accuracy | Omni Non-Hallucination | AA Index | AA eval cost | Speed tok/s |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Gemini 3.8 Flash | high | 74.0% ± — | $2.36 | 1201.59 | 1412.0 | 59.93% | 19.70% | — | 44.95% | 56.60% | 21.00% | 81.33% | 47.82% | 95.25% | 18.29% | 54.60% | 44.82% | 40.93 | $1622.73 | 238.7 |
| 2 | GPT-6 Astra | xhigh | 74.0% ± — | $4.43 | 1543.68 | 1516.5 | 67.18% | 59.60% | — | 43.09% | 55.67% | 32.20% | 80.00% | 54.59% | 96.26% | 31.43% | 61.85% | 51.68% | 52.39 | $3802.98 | 51.2 |
| 3 | Grok 4.6 | medium | 67.0% ± — | $3.45 | 1487.28 | 1604.8 | 63.15% | 13.13% | — | 44.33% | 55.90% | 17.80% | 81.00% | 42.12% | 93.54% | 17.71% | 41.93% | 76.00% | 42.84 | $1936.75 | 63.7 |
| 4 | GLM-5.3 Flash | max | 63.0% ± — | $0.24 | 1452.46 | 1640.8 | 60.37% | 32.83% | — | 47.22% | 51.62% | 15.40% | 80.00% | 39.85% | 91.21% | 15.43% | 27.50% | 72.37% | 41.81 | $280.28 | 49.2 |
| 5 | Gemini 3.7 Flash | medium | 65.0% ± — | $2.03 | — | 1339.6 | — | — | — | 35.46% | 59.84% | — | 83.00% | 38.97% | 92.12% | 9.43% | 54.00% | 34.13% | 39.62 (estimated) | $— | 286.6 |
| 6 | GPT-5.6 Sol | max | 73.0% ± — | $6.46 | 1487.42 | 1587.9 | 60.08% | 39.90% | — | 44.33% | 57.06% | 27.20% | 84.00% | 49.49% | 94.14% | 32.29% | 59.40% | 7.80% | 46.97 | $3464.84 | 86.9 |
| 7 | Kimi K3 | max | 69.0% ± — | $4.65 | 1505.22 | 1524.0 | 58.27% | 12.63% | — | 45.98% | 59.49% | 22.00% | 88.67% | 46.90% | 93.54% | 23.43% | 47.58% | 46.80% | 43.59 | $3658.07 | — |
| 8 | Claude Fable 5 | xhigh | 70.0% ± — | $13.41 | 1540.79 | 1595.4 | 54.07% | 42.42% | — | 38.14% | 61.00% | 24.00% | 82.33% | 55.47% | 92.63% | 28.57% | 65.35% | 36.36% | 49.63 | $11160.86 | 62.9 |
| 9 | Qwen3.8 Max | xhigh | 57.0% ± — | $3.73 | 1626.21 | 1667.7 | 56.19% | 38.89% | — | 47.84% | 52.08% | 22.80% | 80.33% | 43.10% | 92.83% | 17.71% | 31.68% | 71.16% | 45.42 | $4934.79 | 38.2 |
| 10 | Claude Opus 5 | max | 74.0% ± — | $11.84 | 1673.33 | 1707.9 | 56.57% | 48.99% | — | 42.06% | 56.37% | 21.60% | 79.33% | 54.87% | 93.23% | 29.14% | 60.87% | 39.18% | 50.78 | $7274.74 | 59.2 |
| 11 | GLM-5.3 | max | 69.0% ± — | $3.99 | 1512.03 | 1643.6 | 62.20% | 41.92% | — | 50.31% | 59.03% | 11.20% | 79.67% | 42.26% | 91.72% | 19.14% | 33.85% | 70.45% | 44.78 | $2503.48 | 86.8 |
| 12 | GPT-5.6 Luna | max | 67.0% ± — | $0.61 | 1341.78 | 1443.1 | 50.21% | 11.62% | — | 31.13% | 53.59% | 24.00% | 83.67% | 39.48% | 91.11% | 20.57% | 42.73% | 7.42% | 37.32 | $319.93 | 118.2 |
| 13 | Muse Spark 1.2 | xhigh | 55.0% ± — | $3.70 | 1333.32 | 1481.6 | 40.61% | 7.07% | — | 34.85% | 57.41% | 17.40% | 79.00% | 45.46% | 90.40% | 17.71% | 45.38% | 66.71% | 39.58 | $1385.40 | 240.1 |
| 14 | DeepSeek V4 Pro | max | 63.0% ± — | $1.67 | 1257.69 | 1441.4 | 56.71% | 14.14% | — | 39.59% | 51.04% | 11.40% | 80.33% | 41.01% | 92.83% | 18.00% | 49.10% | 5.17% | 36.00 | $1122.27 | 83.9 |
| 15 | Gemini 3.6 Flash | high | 47.0% ± — | $2.21 | 950.46 | 1264.7 | 53.02% | 7.07% | — | 29.90% | 53.36% | 17.40% | 80.00% | 40.82% | 92.83% | 10.57% | 49.97% | 44.37% | 33.98 | $1036.81 | 185.4 |
| 16 | DeepSeek V4 Flash | max | 53.0% ± — | $0.46 | 1256.59 | 1426.6 | 53.97% | 12.12% | — | 39.38% | 50.35% | 11.00% | 79.67% | 38.55% | 90.81% | 16.57% | 40.38% | 8.30% | 34.33 | $474.19 | 226.7 |
| 17 | GPT-5.5 | xhigh | 67.0% ± — | $7.23 | 1137.18 | 1335.9 | 47.30% | 14.65% | — | 38.97% | 55.79% | 21.20% | 84.33% | 45.78% | 93.54% | 27.14% | 57.95% | 10.98% | 38.36 | $5294.36 | 96.2 |
| 18 | Gemini 3.5 Flash | high | 36.0% ± — | $3.45 | 871.90 | 1184.8 | 42.08% | 6.57% | — | 32.16% | 53.94% | 19.80% | 73.33% | 42.68% | 92.22% | 13.14% | 51.40% | 37.83% | 32.60 | $2172.43 | 196.3 |
| 19 | Claude Opus 4.8 | max | 59.0% ± — | $13.22 | 1320.80 | 1438.3 | 45.59% | 21.72% | — | 34.23% | 54.40% | 22.80% | 77.67% | 48.66% | 92.02% | 20.86% | 48.83% | 60.75% | 41.79 | $6873.86 | 52.8 |
| 20 | GLM-5.2 | max | 44.0% ± — | $3.92 | 1230.23 | 1357.5 | 28.40% | 1.01% | — | 34.64% | 51.16% | 10.40% | 78.33% | 41.15% | 89.49% | 20.86% | 24.33% | 73.70% | 33.71 | $2097.29 | 79.5 |
| 21 | Claude Sonnet 5 | max | 54.0% ± — | $26.40 | 1359.19 | 1449.2 | 36.51% | 14.14% | — | 37.32% | 54.28% | 13.20% | 82.00% | 41.29% | 91.11% | 16.86% | 40.05% | 60.63% | 38.16 | $6998.25 | 76.8 |

## [LiveBench](https://livebench.ai/) external component

[LiveBench](https://livebench.ai/) release **2026_06_25** supplies the four-task Instruction Following mean and its seven-category Overall Score. Cost is the official **Cost Per Successful Task** field. The pinned table matches **21/21** ranked models and includes **1 official supplemental model** outside that cohort: **Claude Fable 5.1**.

| Model | LiveBench variant | Instruction Following | Overall Score | Cost Per Successful Task |
|---|---|---:|---:|---:|
| GPT-6 Astra | gpt-6-astra-max | 75.58 | 82.16 | $0.7359 |
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

LiveBench Pareto frontier (Overall Score vs Cost Per Successful Task): **DeepSeek V4 Flash, GLM-5.3 Flash, Gemini 3.7 Flash, Kimi K3, GPT-5.5, GPT-5.6 Sol, GPT-6 Astra, Claude Fable 5.1**.

## [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) external component

The current official [Terminal-Bench 4.0](https://www.tbench.ai/leaderboard/terminal-bench/4.0) snapshot contains **15 rows** and overlaps **11/21** ranked models. It replaces the old standalone TB2.1 publication; the AA source matrix above keeps its v2.1 field only as explicit AA-source provenance.

| Rank | Model | Agent | Resolution rate | Tokens | Cost |
|---:|---|---|---:|---:|---:|
| 1 | GPT-6 Astra | Codex | 58.2% ± 2.8% | 1.5B | $3,300 |
| 2 | Fable 5.1 | Claude Code | 57.9% ± 3.8% | 2.7B | $6,200 |
| 3 | Opus 5 | Claude Code | 53.9% ± 3.2% | 6.9B | $6,100 |
| 4 | Fable 5 | Claude Code | 44.5% ± 3.8% | 3.8B | $7,300 |
| 5 | GLM-5.3 | Claude Code | 41.8% ± 3.2% | 8.7B | $2,700 |
| 6 | Grok 4.7 | Grok Build | 37.6% ± 3.5% | 5.5B | $3,700 |
| 7 | GPT-5.6 Sol | Codex | 37.3% ± 3.8% | 4.4B | $2,500 |
| 8 | Opus 4.8 | Claude Code | 23.6% ± 3.6% | 6.4B | $6,500 |
| 9 | GPT-5.6 Terra | Codex | 21.5% ± 3.3% | 5.7B | $1,700 |
| 10 | Grok 4.6 | Grok Build | 20.3% ± 3.1% | 4.0B | $3,600 |
| 11 | Gemini 3.8 Flash | mini-SWE-agent | 19.1% ± 3.4% | 17.2B | $1,800 |
| 12 | GPT-5.6 Luna | Codex | 17.3% ± 2.8% | 11.6B | $300 |
| 13 | Grok 4.5 | Grok Build | 12.4% ± 2.6% | 3.4B | $2,100 |
| 13 | Sonnet 5 | Claude Code | 12.4% ± 3.1% | 21.6B | $9,600 |
| 15 | Gemini 3.7 Flash | mini-SWE-agent | 11.2% ± 2.4% | 11.1B | $1,300 |

## Provider claims (separate from benchmark-owner results)

The ledger contains **1 ranking-eligible provider claim** and separately records claims that fail version, implementation, or evaluated-variant checks. The eligible DeepSeek value is a V4.1-Flash Terminal-Bench 4.0 claim for the current `deepseek-v4-flash` API alias; it is not a direct result for the retired V4 Flash model. Google’s GDP.pdf and AutomationBench claims remain audit-only because the model card does not establish the selected medium effort and exact AA component implementation.

| Benchmark and version | Cohort model | Evaluated model | Provider value | Status | Source type | Source | Caveat |
|---|---|---|---:|---|---|---|---|
| Terminal-Bench 4.0 | deepseek-v4-flash | DeepSeek V4.1-Flash | 31.20% | Ranking eligible | model_provider_claim | [provider source](https://api-docs.deepseek.com/updates/) | The provider reports TB4.0 for V4.1-Flash and says the deepseek-v4-flash API name is temporarily routed to it. This is a current-route claim, not a direct measurement of the retired V4 Flash model version. Remove the claim when the benchmark owner publishes a result for the mapped current route. |
| GDP.pdf not stated by provider | gemini-3.7-flash | Gemini 3.7 Flash | 34.00% | Audit only | model_provider_claim | [provider source](https://deepmind.google/models/model-cards/gemini-3-7-flash/) | The provider material does not state the effort variant, while the selected Artificial Analysis cohort URL is the medium variant; retain the claim for audit but do not transfer it into that variant's value. |
| AutomationBench Provider private set; AA version not stated | gemini-3.7-flash | Gemini 3.7 Flash | 30.40% | Audit only | model_provider_claim | [provider source](https://deepmind.google/models/model-cards/gemini-3-7-flash/) | The provider identifies a private AutomationBench set but does not establish equivalence to Artificial Analysis's AutomationBench-AA implementation or state the effort variant; retain for audit without transferring it into the selected medium variant. |

## [Bug Hunt Bench](https://bughunt.productcompass.pm/) external component

The owner scoreboard reports planted bugs fixed out of **105** across two repositories. This ValueRank snapshot is pinned to [scoreboard commit 0630b120a81363c343ed7dfaf3c6d3be7f7da38c](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv); the corresponding [run notes](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/run-notes.md) describe the harnesses, routes, and aggregation. Sixteen cohort rows match exactly and enter a separate emphasis ranking. Five rows have no eligible result and stay excluded from that alternate score.

| Model | Fixed / 105 | Runs / aggregation | Evaluated model | Effort and status | Harness | Route | Match status and note |
|---|---:|---|---|---|---|---|---|
| GPT-6 Astra | 45.0 | 3 / mean | GPT-6 Astra (max effort) - mean of 3 | max (verified ceiling) | Codex CLI | OpenAI | Matched: Owner-published mean of three runs. |
| Gemini 3.8 Flash | 18.0 | 3 / mean | Gemini 3.8 Flash - mean of 3 | high (verified ceiling) | Antigravity CLI | Google | Matched: Owner-published mean of three runs. |
| Claude Opus 5 | 27.0 | 1 / single | Opus 5 (max effort) | max (max) | Claude Code | Anthropic | Matched: Single official run; treat as one draw. |
| GPT-5.6 Sol | 43.5 | 2 / mean | GPT-5.6 Sol (max effort) - mean of 2 | max (max) | Codex CLI | OpenAI | Matched: Use the owner-published mean of two identical-configuration runs. |
| Claude Fable 5 | 29.0 | 1 / single | Fable 5 (max effort) | max (max) | Claude Code | Anthropic | Matched: Single official run; treat as one draw. |
| GLM-5.3 | 19.0 | 1 / single | GLM-5.3 (max effort, Z.ai API) | max (verified setting) | Claude Code / Z.ai API | Z.ai API | Matched: Single official run; treat as one draw. |
| Kimi K3 | 21.0 | 1 / single | Kimi K3 | default (default) | Claude Code / OpenRouter | OpenRouter | Matched: Only one owner result is available, at the route's default setting. |
| Grok 4.6 | 28.7 | 3 / mean | Grok 4.6 (xhigh) seq - mean of 3 | xhigh (verified ceiling) | Grok Build CLI (ACP) | xAI | Matched: Sequential repo runs; owner-published mean of three runs. |
| GPT-5.6 Luna | 31.3 | 3 / mean | GPT-5.6 Luna (max effort) - mean of 3 | max (max) | Codex CLI | OpenAI | Matched: Owner-published mean of three runs. |
| GPT-5.5 | — | None / None | None | None (None) | None | None | owner_result_missing: No Bug Hunt owner result or matching provider-published claim was found by the focused search as of the snapshot. |
| Gemini 3.7 Flash | — | None / None | None | None (None) | None | None | variant_mismatch: The owner has Gemini 3.7 Flash high-effort rows, but this cohort row selects the Gemini 3.7 Flash medium variant. No value is transferred across the variant. |
| GLM-5.3 Flash | 17.7 | 3 / mean | GLM-5.3 Flash (max effort, Z.ai API) - mean of 3 | max (verified ceiling) | Claude Code / Z.ai API | Z.ai API | Matched: Owner-published mean of three runs. |
| DeepSeek V4 Pro | 16.0 | 1 / single | DeepSeek V4-Pro (max effort, DeepSeek API) | max (first-party; effort effect inconclusive) | Claude Code / DeepSeek API | DeepSeek API | Matched: Single official run. The run notes say the high-versus-max effort probe on Pro was inconclusive. |
| Claude Opus 4.8 | 15.0 | 1 / single | Opus 4.8 (max effort) | max (max) | Claude Code | Anthropic | Matched: Single official run; treat as one draw. |
| Qwen3.8 Max | 25.7 | 3 / mean | Qwen3.8-Max (max effort, Alibaba API) - mean of 3 | max (verified ceiling) | Claude Code / Alibaba API | Alibaba API | Matched: Owner-published mean of three runs on Alibaba's own endpoint. |
| Muse Spark 1.2 | 14.0 | 1 / single | Muse Spark 1.2 (default effort, OpenRouter) | default (default) | Claude Code / OpenRouter | OpenRouter | Matched: The alternative 17/105 xhigh row mixes Meta-direct and OpenRouter routes across its two repository legs; the run notes identify 14/105 as the single-route row. |
| Claude Sonnet 5 | 9.0 | 1 / single | Sonnet 5 (max effort) | max (max) | Claude Code | Anthropic | Matched: Single official run; treat as one draw. |
| DeepSeek V4 Flash | 21.7 | 3 / mean | DeepSeek V4.1 Flash (max effort) - mean of 3 | max (verified ceiling) | Claude Code / DeepSeek API | DeepSeek API | Matched: Current API alias match; this is a V4.1 Flash result, not a retired V4 Flash result. |
| Gemini 3.6 Flash | — | None / None | None | None (None) | None | None | owner_result_missing: No Bug Hunt owner result or matching provider-published claim was found by the focused search as of the snapshot. |
| GLM-5.2 | — | None / None | None | None (None) | None | None | owner_result_missing: No Bug Hunt owner result or matching provider-published claim was found by the focused search as of the snapshot. |
| Gemini 3.5 Flash | — | None / None | None | None (None) | None | None | owner_result_missing: No Bug Hunt owner result or matching provider-published claim was found by the focused search as of the snapshot. |

The selected Gemini 3.7 Flash AA cohort is medium effort, so the Bug Hunt high-effort row is excluded. Muse Spark 1.2's xhigh row mixes Meta-direct and OpenRouter routes across the repository legs; the owner run notes identify the 14/105 OpenRouter row as the single-route result used here. A focused provider-source check found no matching provider-published Bug Hunt result for the five uncovered models. The owner results are used wherever an exact match exists; provider claims remain source-typed and are replaced when the owner publishes a result.

## Cost construction

Cost mode: **DeepSWE-only**. AA total evaluation cost is available for **20/21** models; missing AA costs are **Gemini 3.7 Flash**. No selective substitution is used.

| Model | AA cost penalty | DeepSWE cost penalty | Composite cost |
|---|---:|---:|---:|
| Gemini 3.8 Flash | — | 8.94 | 8.94 |
| GPT-6 Astra | — | 16.78 | 16.78 |
| Grok 4.6 | — | 13.07 | 13.07 |
| GLM-5.3 Flash | — | 0.91 | 0.91 |
| Gemini 3.7 Flash | — | 7.69 | 7.69 |
| GPT-5.6 Sol | — | 24.47 | 24.47 |
| Kimi K3 | — | 17.61 | 17.61 |
| Claude Fable 5 | — | 50.80 | 50.80 |
| Qwen3.8 Max | — | 14.13 | 14.13 |
| Claude Opus 5 | — | 44.85 | 44.85 |
| GLM-5.3 | — | 15.11 | 15.11 |
| GPT-5.6 Luna | — | 2.31 | 2.31 |
| Muse Spark 1.2 | — | 14.02 | 14.02 |
| DeepSeek V4 Pro | — | 6.33 | 6.33 |
| Gemini 3.6 Flash | — | 8.37 | 8.37 |
| DeepSeek V4 Flash | — | 1.74 | 1.74 |
| GPT-5.5 | — | 27.39 | 27.39 |
| Gemini 3.5 Flash | — | 13.07 | 13.07 |
| Claude Opus 4.8 | — | 50.08 | 50.08 |
| GLM-5.2 | — | 14.85 | 14.85 |
| Claude Sonnet 5 | — | 100.00 | 100.00 |

## Supplemental Artificial Analysis coverage

These fields are preserved for future analysis but remain outside the primary score because they are incomplete across the current cohort or are not separate ValueRank dimensions. AA-Briefcase and GDP.pdf are current v4.3.2 source components represented in the raw matrix; GPQA Diamond is retained as an explicitly labelled legacy ValueRank input. LiveBench and Terminal-Bench 4.0 remain coverage fields under the no-imputation policy. Bug Hunt Bench feeds only the separate matched-cohort emphasis ranking.

| Field | Available | Missing models | Role |
|---|---:|---|---|
| mlcrOverall | 18/21 | gpt-6-astra, grok-4.6, gemini-3.7-flash | Supplemental / not scored |
| harveyLab | 11/21 | gpt-6-astra, gemini-3.8-flash, glm-5.3, grok-4.6, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, qwen3.8-max, muse-spark-1.2, deepseek-v4-flash | Supplemental / not scored |
| apexAgents | 5/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, grok-4.6, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash | Supplemental / not scored |
| mmmuPro | 12/21 | claude-fable-5, glm-5.3, grok-4.6, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, muse-spark-1.2, deepseek-v4-flash, glm-5.2 | Supplemental / not scored |
| livecodebench | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| aime25 | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| analystAgent | 8/21 | gpt-6-astra, gemini-3.8-flash, glm-5.3, grok-4.6, gpt-5.6-luna, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, qwen3.8-max, muse-spark-1.2, deepseek-v4-flash, gemini-3.6-flash, glm-5.2 | Supplemental / not scored |
| automationBenchPartialScore | 20/21 | gemini-3.7-flash | Supplemental / not scored |
| enterpriseOpsGym | 15/21 | gpt-6-astra, gemini-3.8-flash, grok-4.6, qwen3.8-max, deepseek-v4-flash, gemini-3.6-flash | Supplemental / not scored |
| itBenchSre | 9/21 | gpt-6-astra, claude-opus-5, claude-fable-5, grok-4.6, gemini-3.7-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash | Supplemental / not scored |
| briefcaseRubricPassRate | 20/21 | gemini-3.7-flash | Supplemental / not scored |
| briefcaseTotalCost | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| tauBanking | 21/21 | none | Supplemental / not scored |
| terminalBenchV21 | 0/21 | gpt-6-astra, gemini-3.8-flash, claude-opus-5, gpt-5.6-sol, claude-fable-5, glm-5.3, kimi-k3, grok-4.6, gpt-5.6-luna, gpt-5.5, gemini-3.7-flash, glm-5.3-flash, deepseek-v4-pro, claude-opus-4.8, qwen3.8-max, muse-spark-1.2, claude-sonnet-5, deepseek-v4-flash, gemini-3.6-flash, glm-5.2, gemini-3.5-flash | Supplemental / not scored |
| livebenchOverall | 21/21 | none | Supplemental / not scored |
| livebenchInstructionFollowing | 21/21 | none | Supplemental / not scored |
| livebenchCostPerSuccessfulTask | 21/21 | none | Supplemental / not scored |
| terminalBenchV4 | 12/21 | Kimi K3, GPT-5.5, GLM-5.3 Flash, DeepSeek V4 Pro, Qwen3.8 Max, Muse Spark 1.2, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | Supplemental / not scored |
| bugHuntFixedOf105 | 16/21 | GPT-5.5, Gemini 3.7 Flash, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | Separate Bug Hunt emphasis ranking |

## Dropped primary candidate

| Dimension | Missing model | Treatment |
|---|---|---|
| Terminal-Bench 4.0 | Kimi K3, GPT-5.5, GLM-5.3 Flash, DeepSeek V4 Pro, Qwen3.8 Max, Muse Spark 1.2, Gemini 3.6 Flash, GLM-5.2, Gemini 3.5 Flash | incomplete cohort coverage; values remain null and are not neutral-filled |
| AutomationBench-AA | Gemini 3.7 Flash | incomplete cohort coverage; values remain null and are not neutral-filled |
| Speed | Kimi K3 | incomplete cohort coverage; values remain null and are not neutral-filled |

Missing values are intentionally represented as null; no old-version, model-family, median, or neutral-fill substitution is used.

## Machine-readable artifacts

- [.refresh/v1.4/deepswe.json](.refresh/v1.4/deepswe.json): current DeepSWE extraction
- [.refresh/v1.4/aa_metrics.json](.refresh/v1.4/aa_metrics.json): decoded current AA model payloads
- [.refresh/v1.4/scores.json](.refresh/v1.4/scores.json): normalized scores and rankings
- [.refresh/v1.4/coverage_matrix.json](.refresh/v1.4/coverage_matrix.json): primary and supplemental availability
- [.refresh/v1.4/livebench.json](.refresh/v1.4/livebench.json): pinned LiveBench task/category/cost snapshot and Pareto data
- [.refresh/v1.4/tb4.json](.refresh/v1.4/tb4.json): normalized official Terminal-Bench 4.0 rendered leaderboard
- [.refresh/v1.4/bug_hunt.json](.refresh/v1.4/bug_hunt.json): pinned Bug Hunt scoreboard, exact matches, and exclusions
- [research/2026-09-29-valuerank-refresh-v4-3-2/README.md](research/2026-09-29-valuerank-refresh-v4-3-2/README.md): v4.3.2 source-change, evidence, and scoring record
- [.refresh/v1.4/provider_claims.json](.refresh/v1.4/provider_claims.json): provider claim values, source URLs, eligibility, and caveats
- [.refresh/v1.4/deepswe-browser-2026-09-29.json](.refresh/v1.4/deepswe-browser-2026-09-29.json): built-in browser DeepSWE snapshot
- [.refresh/v1.4/tb4-browser-2026-09-29.json](.refresh/v1.4/tb4-browser-2026-09-29.json): built-in browser Terminal-Bench snapshot
