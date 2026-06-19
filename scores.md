# ValueRank v1.2 Scores

**Version:** v1.2
**Updated:** June 20, 2026

## Final Ranking

v1.2 shrinks the ranked cohort from 13 to 8 current DeepSWE-listed models, adds Claude Fable 5, renames Kimi from K2.6 to K2.7 Code, and renormalizes the full score over the new 8-model cohort.

| Rank | Model | Overall | Quality | Quality Rank | Missing Dims |
|---|---|---:|---:|---:|---:|
| 1 | Gemini 3.1 Pro | 59.1 | 59.8 | 3 | 0 |
| 2 | Gemini 3.5 Flash | 59.0 | 50.2 | 6 | 0 |
| 3 | Claude Fable 5 | 57.6 | 76.5 | 1 | 0 |
| 4 | GPT-5.5 | 56.9 | 66.2 | 2 | 0 |
| 5 | GPT-5.4 | 56.7 | 51.9 | 5 | 0 |
| 6 | Claude Opus 4.8 | 46.1 | 56.6 | 4 | 0 |
| 7 | Kimi K2.7 | 38.5 | 18.2 | 8 | 0 |
| 8 | Claude Sonnet 4.6 | 26.2 | 20.7 | 7 | 0 |

## Removed Models (v1.1 Scores)

The following models were ranked in v1.1 (n=13) but are no longer on the DeepSWE leaderboard, so they are excluded from v1.2 (n=8). Their v1.1 scores are preserved here for reference. **Not directly comparable to v1.2** — normalization denominator changed from 13 to 8.

| Model | v1.1 Rank | v1.1 Overall | v1.1 Quality | v1.1 Composite Cost |
|---|---:|---:|---:|---:|
| MiMo-V2.5-Pro | 3 | 58.1 | 44.2 | $7.04 |
| MiniMax M3 | 4 | 56.0 | 52.4 | $18.32 |
| DeepSeek V4-Pro | 9 | 48.0 | 36.3 | $14.22 |
| Claude Opus 4.7 | 11 | 39.0 | 52.0 | $100.00 |
| GLM 5.1 | 10 | 40.0 | 36.7 | $25.82 |
| GPT-5.4 Mini | 12 | 36.5 | 29.3 | $18.95 |

## Pareto Frontier

Undominated on composite cost vs. quality (6 models):

- Gemini 3.1 Pro
- Gemini 3.5 Flash
- Claude Fable 5
- GPT-5.5
- GPT-5.4
- Kimi K2.7

Dominated models: Claude Opus 4.8, Claude Sonnet 4.6.

## Normalized Dimension Matrix

Dimension order:

`[Cost, IF, Halluc, TermHard, DeepSWE, GDP, Tau2, LCR, OmniAcc, HLE, GPQA, Sci, CritPt, AAI, Spd]`

| Model | Normalized dimensions |
|---|---|
| Gemini 3.1 Pro | `[57.1, 100.0, 71.4, 42.9, 0.0, 0.0, 85.7, 71.4, 85.7, 71.4, 100.0, 85.7, 42.9, 14.3, 71.4]` |
| Gemini 3.5 Flash | `[85.7, 85.7, 42.9, 0.0, 42.9, 28.6, 71.4, 28.6, 71.4, 28.6, 57.1, 28.6, 28.6, 42.9, 100.0]` |
| Claude Fable 5 | `[0.0, 42.9, 57.1, 100.0, 100.0, 100.0, 100.0, 42.9, 100.0, 100.0, 71.4, 100.0, 100.0, 100.0, 0.0]` |
| GPT-5.5 | `[28.6, 71.4, 14.3, 85.7, 85.7, 71.4, 42.9, 100.0, 57.1, 57.1, 85.7, 57.1, 85.7, 71.4, 42.9]` |
| GPT-5.4 | `[71.4, 57.1, 0.0, 57.1, 57.1, 57.1, 14.3, 85.7, 42.9, 42.9, 35.7, 71.4, 71.4, 57.1, 85.7]` |
| Claude Opus 4.8 | `[14.3, 14.3, 100.0, 71.4, 71.4, 85.7, 57.1, 14.3, 28.6, 85.7, 35.7, 42.9, 57.1, 85.7, 57.1]` |
| Kimi K2.7 | `[100.0, 28.6, 28.6, 14.3, 28.6, 14.3, 28.6, 0.0, 0.0, 14.3, 14.3, 14.3, 14.3, 0.0, 28.6]` |
| Claude Sonnet 4.6 | `[42.9, 0.0, 85.7, 28.6, 14.3, 42.9, 0.0, 57.1, 14.3, 0.0, 0.0, 0.0, 0.0, 28.6, 14.3]` |
