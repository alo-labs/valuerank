# ValueRank Methodology

**Version:** v0.9  
**Updated:** June 12, 2026

## Cohort Rule

v0.9 ranks the models listed on [DeepSWE](https://deepswe.datacurve.ai/), excluding **Grok-Build-0.1** and **Gemini 3 Flash** by user instruction.

Ranked v0.9 cohort:

- GPT-5.5
- Claude Opus 4.8
- GPT-5.4
- Claude Opus 4.7
- Claude Sonnet 4.6
- Gemini 3.5 Flash
- Claude Opus 4.6
- GPT-5.4 Mini
- Kimi K2.6
- MiniMax M3
- MiMo-V2.5-Pro
- GLM 5.1
- Gemini 3.1 Pro
- DeepSeek V4-Pro

## Scored Dimensions

ValueRank v0.9 uses 20 dimensions:

1. Cost
2. IFBench
3. AA-Omniscience Hallucination Rate
4. Terminal-Bench 2.1
5. SWE-bench Verified
6. SWE-bench Pro
7. LiveCodeBench v4
8. DeepSWE
9. Artificial Analysis Index
10. Speed
11. Tau2-Bench
12. OSWorld
13. BrowseComp
14. LCR / RULER
15. HLE
16. GPQA Diamond
17. MMLU-Pro
18. AIME 2025
19. SciCode
20. AA-Omniscience Index

## Weights

| Dimension | Weight |
|---|---:|
| Cost | 25% |
| IFBench | 12% |
| AA-Omniscience Hallucination Rate | 6% |
| Terminal-Bench 2.1 | 6% |
| SWE-bench Verified | 5% |
| SWE-bench Pro | 4% |
| LiveCodeBench v4 | 5% |
| DeepSWE | 5% |
| Artificial Analysis Index | 5% |
| Speed | 5% |
| Tau2-Bench | 4% |
| OSWorld | 4% |
| BrowseComp | 3% |
| LCR / RULER | 2% |
| HLE | 2% |
| GPQA Diamond | 2% |
| MMLU-Pro | 2% |
| AIME 2025 | 1% |
| SciCode | 1% |
| AA-Omniscience Index | 1% |

Macro-balance:

- Cost: 25%
- Reliability: 18% (`IFBench` 12% + `AA-Omniscience Hallucination Rate` 6%)
- Code / agentic coding: 25%
- Production / agentic operation: 24%
- Intelligence: 8%

## Normalization

Each dimension is rank-normalized:

`((n - rank) / (n - 1)) * 100`

Where `n` is the number of models with real data on that benchmark.

- Best real score gets `100`
- Worst real score gets `0`
- Missing data gets neutral `50`
- For AA-Omniscience Hallucination Rate, the **lowest raw hallucination rate ranks first**

### Cost construction

v0.9 now builds the raw cost input in three steps before applying the normal ValueRank rank-normalization:

1. Normalize current Artificial Analysis eval cost onto a `0–100` scale, where the highest-cost model in the ranked cohort is `100`.
2. Normalize current **DeepSWE average cost per task** onto a `0–100` scale, where the highest-cost model in the ranked cohort is `100`.
3. Add the two `0–100` components and renormalize the `0–200` total back to a `0–100` composite-cost scale.

Lower composite cost is better. That composite-cost raw value is then rank-normalized into the `Cost` dimension used in ValueRank scoring.

## Quality Score

The Quality Score removes the 25% composite-cost term and renormalizes the remaining 19 dimensions to 100%.

## Source Policy

v0.9 refreshes unstable data from primary sources:

- DeepSWE for DeepSWE pass@1
- Terminal-Bench 2.1 leaderboard for current terminal-agent results where exact model matches exist
- Vals SWE-bench Verified leaderboard for current exact model matches
- Scale SWE-bench Pro public leaderboard where current public rows exist
- Ai2 IFBench / Artificial Analysis publication for exact IFBench model scores
- OSWorld-Verified official results workbook
- Artificial Analysis evaluation pages for GPQA Diamond, HLE, SciCode, RULER/LCR, AA-Omniscience Index, and AA-Omniscience Hallucination Rate
- Artificial Analysis model pages for current eval cost, speed, and intelligence-index values
- DeepSWE for both pass@1 and average-cost-per-task values used in the composite cost construction

## Alias Rule

Several current primary leaderboards publish a model family only as a public reasoning-profile row, for example:

- `GPT-5.5 (xhigh)`
- `Claude Opus 4.8 (Adaptive Reasoning, Max Effort)`
- `Gemini 3.1 Pro Preview`
- `DeepSeek V4 Pro (Reasoning, Max Effort)`
- `MiniMax-M3`
- `GLM-5.1 (Reasoning)`

ValueRank is family-level, not reasoning-profile-level. v0.9 therefore allows a source row to map back to the ranked family when all of the following are true:

1. The source row is clearly the same model family with only a suffix, punctuation variant, or public preview/profile label.
2. ValueRank does not separately rank another sibling profile from that same family.
3. The benchmark host itself uses that profile row as the current public representative result.

This rule is used to reduce artificial missingness, but it is not extended across materially different model versions. For example, `Gemini 3 Pro Preview` is not treated as `Gemini 3.1 Pro`.

## Remaining Missing-Data Rule

Where no exact current row or allowed family-level alias exists for a model-dimension pair, ValueRank marks the cell missing and assigns neutral `50.0`. v0.9 does not infer benchmark values from secondary commentary, screenshots, or adjacent model generations.
