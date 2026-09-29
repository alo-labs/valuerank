# Bug Hunt Bench integration record

- **ValueRank release:** v1.9.0
- **Observed:** September 29, 2026
- **Owner snapshot commit:** `0630b120a81363c343ed7dfaf3c6d3be7f7da38c`

## Sources

- Benchmark home: [Bug Hunt Bench](https://bughunt.productcompass.pm/)
- Combined owner scoreboard: [pinned CSV](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/combined-scoreboard.csv)
- Run notes: [pinned methodology notes](https://github.com/phuryn/bug-hunt-bench/blob/0630b120a81363c343ed7dfaf3c6d3be7f7da38c/results/run-notes.md)
- AA DeepSWE source: [Coding Agent Index v1.5, DeepSWE v1.1 chart](https://artificialanalysis.ai/agents/coding-agents?coding-agents-performance-chart=deep-swe-v1.1)

## What the benchmark measures

The owner scoreboard aggregates how many of up to 105 planted bugs an agent configuration fixes across two repositories. Results are stack-level: rows differ in agent CLI, reasoning effort, provider route, and repeat count. The pinned run notes report arithmetic means for repeated configurations, while many rows have one run; the raw-data table preserves those settings and sample counts.

## Cohort match and exclusions

The source roster contains 21 AA-mapped ValueRank candidates. The Bug Hunt snapshot has **16 exact owner results** among them; AA's DeepSWE v1.1 chart shows **25 agent/model configurations over 113 tasks**. The main rank uses the exact intersection: **9 model variants have both a Bug Hunt owner result and an exact AA DeepSWE v1.1 result**. Seven other Bug Hunt results and five models with no Bug Hunt owner row remain outside the composite.

All nine Bug Hunt inputs in the main rank are benchmark-owner results. We found no eligible provider-published Bug Hunt claim for the five models without an owner result. No scores transfer across model versions, reasoning efforts, or composite-agent configurations. For example, the AA chart's Claude Opus 5.5 result is preserved in the source data but is not transferred to the distinct Claude Opus 5 candidate row.

## Main-rank scoring

Bug Hunt Bench is part of the **primary ValueRank score**:

- The 14 retained dimensions have total priority **121**.
- Bug Hunt has priority **20**, for a primary weight of **16.53%**.
- DeepSWE v1.1 has priority **25**, for a weight of **20.66%**.
- Cost has priority **25**, also **20.66%**; it uses complete AA total evaluation-cost data for the nine ranked models. DeepSWE average-task-cost figures are not used in the current score.
- Each benchmark is rank-normalized within the exact nine-model cohort. Rank 1 maps to 100 and rank 9 to 0; exact ties use average rank. The retained dimensions have complete coverage, with no neutral-fill values.
- The companion Bug Hunt emphasis view raises Bug Hunt's priority to **30** (22.90% of its separate composite) across the same nine models.

## Primary rank snapshot

| Rank | Model | ValueRank score | DeepSWE v1.1 pass@1 | Bug Hunt fixed / 105 |
|---:|---|---:|---:|---:|
| 1 | GPT-5.6 Sol | 72.2 | 72 | 43.5 |
| 2 | GPT-6 Astra | 68.8 | 68 | 45 |
| 3 | Grok 4.6 | 55.2 | 65 | 28.7 |
| 4 | Kimi K3 | 51.3 | 68 | 21 |
| 5 | GPT-5.6 Luna | 50.7 | 66 | 31.3 |

The full main ranking and companion emphasis view are in [scores.md](../../scores.md); benchmark inputs and coverage are in [raw-data.md](../../raw-data.md). Machine-readable records are [bug_hunt.json](../../.refresh/v1.4/bug_hunt.json), [aa_deepswe.json](../../.refresh/v1.4/aa_deepswe.json), [scores.json](../../.refresh/v1.4/scores.json), and [coverage_matrix.json](../../.refresh/v1.4/coverage_matrix.json).
