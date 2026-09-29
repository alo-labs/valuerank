# Bug Hunt Bench integration record

- **ValueRank release:** v1.7.0
- **Observed:** September 29, 2026
- **Owner snapshot commit:** `0630b120a81363c343ed7dfaf3c6d3be7f7da38c`

## Sources

- Benchmark home: https://bughunt.productcompass.pm/
- Combined owner scoreboard pinned to this refresh: https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv
- Run notes pinned to this refresh: https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/run-notes.md
- DeepSeek model alias claim used to validate the current `deepseek-v4-flash` route: https://api-docs.deepseek.com/updates/

## What the benchmark measures

The owner scoreboard aggregates whether agentic model-and-harness configurations fixed up to 105 planted bugs across two repositories. It is a stack-level benchmark: the rows use different agent CLIs, reasoning efforts, provider routes, and repeat counts. The pinned run notes report arithmetic means for repeated configurations and show that many configurations have a single run. The raw-data table retains the configuration and sample details; close results with `n=1` should be treated as noisy.

## Cohort match and exclusions

The scoreboard snapshot has **16 exact eligible matches out of the 21-model ValueRank cohort**. All values are benchmark-owner results. When the owner has no row, ValueRank's provider-claim policy permits an exact-version, exact-evaluated-model provider claim, kept visibly distinct and replaced by the owner result later. The focused provider-source audit located no matching Bug Hunt claim for the five uncovered cohort entries.

- `gemini-3.7-flash`: the owner result is for high effort; this ValueRank cohort selects medium effort, so the value is not transferred.
- `muse-spark-1.2`: an xhigh result with 17/105 mixes Meta-direct and OpenRouter routes between repository legs. The run notes identify the single-route OpenRouter default-effort row at 14/105, which is retained in the source ledger.
- `deepseek-v4-flash`: the owner result is 21.7/105 for DeepSeek V4.1 Flash via the current API alias. DeepSeek's provider update states the alias temporarily routes to V4.1 Flash; that alias mapping is recorded and is not presented as a measurement of the retired V4 Flash model.
- `gpt-5.5`, `gemini-3.6-flash`, `glm-5.2`, and `gemini-3.5-flash`: no benchmark-owner result or exact provider claim was located. These four, plus the Gemini 3.7 Flash effort mismatch, make up the five uncovered models.

## Scoring decision

Bug Hunt Bench is high-weight in a separate matched-cohort emphasis ranking:

- Existing retained dimension priorities sum to **78**.
- Bug Hunt receives priority **20**; the alternate composite total is **98**.
- Bug Hunt's alternate-ranking weight is **20.4082%** (20.41% in the rendered docs), second only to Cost at 25.5102%.
- Each retained existing dimension is re-ranked within the same 16 models before combining with Bug Hunt. This prevents a partial-cohort benchmark from changing the 21-model zero-gap primary ranking.
- Rank 1 maps to 100 and rank 16 to 0; exact ties receive the average tied rank. The final composite sorts by score, then lower cost, then model name.

## Result snapshot

The leading Bug Hunt emphasis ranks are:

| Rank | Model | Owner result | Runs | Emphasis score | Primary ValueRank rank |
|---:|---|---:|---:|---:|---:|
| 1 | GPT-6 Astra | 45.0/105 | 3, mean | 71.6 | 2 |
| 2 | Grok 4.6 | 28.7/105 | 3, mean | 63.8 | 3 |
| 3 | GPT-5.6 Sol | 43.5/105 | 2, mean | 63.6 | 6 |
| 4 | Claude Fable 5 | 29/105 | 1, single | 58.9 | 8 |
| 5 | Gemini 3.8 Flash | 18/105 | 3, mean | 58.1 | 1 |

The complete 16-row ranking and every row's effort, harness, route, and repeat count are in [scores.md](../../scores.md) and [raw-data.md](../../raw-data.md). Machine-readable inputs and outputs are [bug_hunt.json](../../.refresh/v1.4/bug_hunt.json), [scores.json](../../.refresh/v1.4/scores.json), and [coverage_matrix.json](../../.refresh/v1.4/coverage_matrix.json).
