# Coding Agent ValueRank - Research Provenance

Last updated: July 28, 2026

## Objective

Refresh `/coding-agents/` for the v1.3 publish using Artificial Analysis' Coding Agent benchmark as the basis, then Terminal Bench 2.1.

## Primary Sources

| Source | URL | Role |
|---|---|---|
| Artificial Analysis Coding Agents | https://artificialanalysis.ai/agents/coding-agents | Cohort, AA Index, component scores, cost, time |
| Terminal Bench 2.1 | https://www.tbench.ai/leaderboard/terminal-bench/2.1 | Official secondary terminal benchmark |

## Extraction Notes

Artificial Analysis embeds row data in Next.js RSC payloads (`benchmarkRows`) rather than a conventional static HTML table. Playwright hydration was required; plain HTTP fetch returns the shell only. Extracted row objects include:

- `agentName` / `display.agent` / `display.model`
- `indexScore`
- `mean.costUsd` / `mean.agentWallTimeSec`
- `evals[]` component rewards (DeepSWE, Terminal-Bench v2, SWE-Atlas-QnA)

Terminal Bench 2.1 exposes an HTML table that can be read directly. At verification time it contained **17** rows.

Evidence snapshots: `.refresh/v1.3/coding-agents/` and `.refresh/v1.3/tb21/`.

## Formula Confirmation

```text
Overall = 0.25 * CostNorm + 0.60 * AAIndexNorm + 0.15 * TB2.1Norm
```

TB2.1 missing → neutral 50 after normalization (unchanged).
