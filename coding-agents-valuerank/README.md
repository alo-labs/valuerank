# Coding Agent ValueRank - v1.3

Last updated: July 28, 2026

## What Changed

v1.3 refreshes the Artificial Analysis coding-agent cohort and remaps Terminal Bench 2.1 against the official 17-row leaderboard. The formula is unchanged from v0.2:

```text
Overall = 0.25 * CostNorm + 0.60 * AAIndexNorm + 0.15 * TB2.1Norm
```

Missing Terminal Bench 2.1 coverage still receives neutral TB2.1 normalization (50).

The old two-list design, Terminal-Bench 2.0 plus SWE-bench Verified, remains retired for this page. The unit of comparison is an agent harness plus model/settings variant.

## Current Top 5

| Rank | Agent Variant | Overall | Quality | CostNorm | AA | TB2.1 |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Codex + GPT-5.6 Terra (max) | 71.5 | 83.1 | 36.6 | 90.2 | 54.8 |
| 2 | Codex + GPT-5.5 (xhigh) | 69.5 | 87.8 | 14.6 | 85.4 | 97.6 |
| 3 | Codex + GPT-5.6 Sol (high) | 69.5 | 86.1 | 19.5 | 95.1 | 50.0 |
| 4 | Codex + GPT-5.6 Sol (xhigh) | 69.1 | 88.0 | 12.2 | 97.6 | 50.0 |
| 5 | Claude Code + Opus 5 (high) | 68.6 | 84.1 | 22.0 | 92.7 | 50.0 |

Cohort size: **42** Artificial Analysis rows with published index + mean API cost. TB2.1 family coverage: **22/42**.

## Source Hierarchy

1. Artificial Analysis Coding Agents: https://artificialanalysis.ai/agents/coding-agents
2. Terminal Bench 2.1: https://www.tbench.ai/leaderboard/terminal-bench/2.1

Artificial Analysis is the basis because it provides one current coding-agent cohort plus index score, component scores, cost, token use, and wall time. Terminal Bench 2.1 is secondary; family-level aliases map effort variants when the official board publishes only one row per agent+model family.

## Files

| File | Role |
|---|---|
| `methodology.md` | Scoring formula, source hierarchy, alias rules |
| `raw-data.md` | Extracted AA cohort + TB2.1 source rows |
| `scores.md` | Computed ranking table |
| `benchmarks.md` | Included / retired benchmark landscape |
| `insights.md` | Practical conclusions from the ranking |
| `profiles.md` | Per-harness notes |
| `limitations.md` | Coverage and interpretation caveats |
| `research.md` | Provenance and extraction notes |
