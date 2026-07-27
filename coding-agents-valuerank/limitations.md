# Coding Agent ValueRank - Limitations

Last updated: July 28, 2026

## 1. Terminal Bench 2.1 Coverage Is Incomplete

Only 22 of 42 Artificial Analysis cohort rows have a direct or family-level Terminal Bench 2.1 match. The remaining rows use neutral TB2.1 normalization. This avoids inventing data, but it also means the ranking is partially based on incomplete secondary coverage — especially for Opus 5 and GPT-5.6 Sol.

## 2. Effort Settings Are Not Separately Verified on TB2.1

Terminal Bench 2.1 often publishes one row per agent + model family (for example `Claude Code + Opus 4.8`), while Artificial Analysis distinguishes multiple effort settings. ValueRank uses a family-level alias rule. That is defensible for coverage, but it cannot prove that each effort setting would receive the exact same Terminal Bench 2.1 score.

## 3. AA Cost Is API Cost, Not Subscription Cost

Artificial Analysis reports mean pay-per-token API cost per task. Real product pricing (Cursor subscriptions, Claude Max, Codex plans) can diverge. ValueRank inherits AA's cost definition for cross-agent comparability.

## 4. Rank-Percentile Normalization Is Cohort-Relative

CostNorm, AAIndexNorm, and covered TB2.1Norm are computed inside this publish's cohort. Adding or removing variants changes other rows' normalized scores even if their raw metrics are unchanged.

## 5. Snapshot Timing

Artificial Analysis and Terminal Bench 2.1 update on independent cadences. This publish freezes both sources on July 28, 2026.
