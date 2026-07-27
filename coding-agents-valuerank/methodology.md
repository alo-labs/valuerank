# Coding Agent ValueRank - Methodology

Last updated: July 28, 2026

## Cohort

v1.3 ranks the **42** coding-agent variants exposed by Artificial Analysis' Coding Agent benchmark page that publish both an Index score and mean API cost per task. The unit of comparison is an agent harness plus model/settings variant, not just the base model.

Examples:

| Harness | Variant |
|---|---|
| Claude Code | Opus 5 (max/high/medium/low), Opus 4.8 (*), GLM-5.1 |
| Codex | GPT-5.6 Sol / Terra / Luna (*), GPT-5.5 (medium/xhigh) |
| Cursor CLI | Composer 2.5, Composer 2, GPT-5.5 (medium) |
| Opencode | Opus 4.7 (medium) |

## Source Priority

1. Artificial Analysis Coding Agent Index is the primary benchmark.
2. Terminal Bench 2.1 is the secondary benchmark.
3. Missing Terminal Bench 2.1 coverage is scored as neutral 50 after normalization.

Artificial Analysis already includes Terminal-Bench v2 inside its own index. Terminal Bench 2.1 therefore receives a smaller weight to avoid over-counting terminal performance.

## Artificial Analysis Basis

Artificial Analysis Coding Agent Index v1.3 is a composite of:

| Component | Public Description | Weight in AA Index |
|---|---|---:|
| DeepSWE | Software engineering tasks (Datacurve) | 1/3 |
| Terminal-Bench v2 | Agentic terminal use, 84 tasks | 1/3 |
| SWE-Atlas-QnA | Technical Q&A, 124 tasks | 1/3 |

ValueRank uses the published `indexScore`, component scores, mean API cost per task, and mean agent wall time per task.

## Terminal Bench 2.1 Mapping

Terminal Bench 2.1 publishes rows by agent plus model family. Artificial Analysis often distinguishes effort settings for the same family. v1.3 applies a family-level alias rule when the agent and model family match (effort suffixes in parentheses are ignored for the match).

| Terminal Bench 2.1 Family | ValueRank Rows |
|---|---|
| Codex + GPT-5.5 | Codex + GPT-5.5 (medium), Codex + GPT-5.5 (xhigh) |
| Codex + GPT-5.6 Terra | All Codex Terra effort variants in the AA cohort |
| Codex + GPT-5.6 Luna | All Codex Luna effort variants in the AA cohort |
| Claude Code + Opus 4.8 | All Claude Code Opus 4.8 effort variants |
| Claude Code + Opus 4.7 | Claude Code Opus 4.7 (medium/max) |
| Claude Code + GLM-5.1 | Claude Code + GLM-5.1 |

Rows without an official direct or family-level match receive neutral TB2.1 normalization.

## Normalization

Each dimension is normalized by rank percentile within the v1.3 cohort (average ranks for ties).

| Dimension | Direction | Normalization |
|---|---|---|
| Cost / task | Lower is better | Cheapest row = 100, most expensive row = 0 |
| AA Coding Agent Index | Higher is better | Highest row = 100, lowest row = 0 |
| Terminal Bench 2.1 | Higher is better | Highest covered row = 100; missing rows = 50 neutral |

## Formula

Default cost weight is 25%.

```text
Quality = 0.80 * AAIndexNorm + 0.20 * TB2.1Norm

Overall = costWeight * CostNorm + (1 - costWeight) * Quality

Default:
Overall = 0.25 * CostNorm + 0.60 * AAIndexNorm + 0.15 * TB2.1Norm
```

The website slider lets users vary cost weight from 0% to 50%.

## Retired v0.1 Method

v0.1 published separate Terminal-Bench 2.0 and SWE-bench Verified lists. That design is no longer used for `/coding-agents/` because the current objective is to use Artificial Analysis' coding-agent benchmark as the basis, then Terminal Bench 2.1.
