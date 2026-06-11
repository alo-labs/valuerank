# ValueRank Methodology

**Version:** v1.0  
**Updated:** June 12, 2026

## Cohort Rule

v1.0 ranks only the current [DeepSWE](https://deepswe.datacurve.ai/) model roster, excluding:

- `Grok-Build-0.1`
- `Gemini 3 Flash`

Ranked cohort:

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

## Zero-Gap Rule

v1.0 removes the old neutral-fill system entirely.

- Every retained dimension must have a genuine current score for all 14 ranked models.
- If even one ranked model is genuinely missing from a benchmark, that benchmark is excluded.
- v1.0 therefore has **zero missing benchmark cells** and uses **no neutral 50 placeholders**.

## Scored Dimensions

ValueRank v1.0 uses 15 fully covered dimensions:

1. Cost
2. IFBench
3. AA-Omniscience Hallucination Rate
4. Terminal-Bench Hard
5. DeepSWE
6. GDPval-AA
7. τ²-Bench Telecom
8. AA-LCR
9. AA-Omniscience Accuracy
10. Humanity's Last Exam
11. GPQA Diamond
12. SciCode
13. CritPt
14. Artificial Analysis Intelligence Index
15. Speed

## Weights

| Dimension | Weight |
|---|---:|
| Cost | 25% |
| IFBench | 12% |
| AA-Omniscience Hallucination Rate | 6% |
| Terminal-Bench Hard | 6% |
| DeepSWE | 7% |
| GDPval-AA | 6% |
| τ²-Bench Telecom | 5% |
| AA-LCR | 4% |
| AA-Omniscience Accuracy | 4% |
| Humanity's Last Exam | 4% |
| GPQA Diamond | 4% |
| SciCode | 4% |
| CritPt | 3% |
| Artificial Analysis Intelligence Index | 6% |
| Speed | 5% |

## Normalization

Each dimension is rank-normalized:

`((n - rank) / (n - 1)) * 100`

Where `n = 14` for every retained benchmark in v1.0.

- Best score gets `100`
- Worst score gets `0`
- Ties receive the average of the tied ranks
- There are **no missing-data cells**

For AA-Omniscience Hallucination Rate, lower raw hallucination is better.

## Cost Construction

The `Cost` dimension is still built in three steps before rank-normalization:

1. Normalize current Artificial Analysis eval cost onto `0–100`, with the highest-cost ranked model set to `100`.
2. Normalize current DeepSWE average cost per task onto `0–100`, with the highest-cost ranked model set to `100`.
3. Average those two penalty terms back onto a single `0–100` composite cost scale.

Lower composite cost is better.

## Quality Score

The Quality Score removes the 25% cost term and renormalizes the remaining 14 non-cost dimensions to 100%.

## Source Policy

v1.0 uses only primary sources for unstable data:

- [DeepSWE](https://deepswe.datacurve.ai/) for DeepSWE pass@1 and DeepSWE average cost per task
- Artificial Analysis model pages for:
  - Artificial Analysis Intelligence Index
  - Speed
  - Eval cost
  - GDPval-AA
  - Terminal-Bench Hard
  - τ²-Bench Telecom
  - AA-LCR
  - AA-Omniscience Accuracy
  - AA-Omniscience Non-Hallucination Rate
  - Humanity's Last Exam
  - GPQA Diamond
  - SciCode
  - IFBench
  - CritPt

## Artificial Analysis Extraction Rule

Artificial Analysis benchmark leaderboards often expose only a visible top slice in the rendered results list. v1.0 therefore derives the 14-model cohort rows directly from current rendered Artificial Analysis **model pages**, which still display benchmark result cards from the same first-party source.

Concrete v1.0 rule:

- For the 11 AA benchmark dimensions above, 13 cohort rows were visible on the current `GPT-5.5 (xhigh)` model page.
- The missing `GPT-5.4 mini (xhigh)` row was filled from its own current model page.
- No values were inferred from third-party articles, screenshots, or older generations.

This is still primary-source extraction from Artificial Analysis' own current rendered pages.

## Current Excluded Benchmark Candidates

The zero-gap rule is stricter than "interesting benchmark" inclusion. A benchmark is eligible if the currently published first-party benchmark data includes **all 14 ranked ValueRank models**, even if the benchmark also includes additional models outside the ValueRank cohort.

Current exclusions verified during the v1.0 audit:

- `APEX-Agents-AA` is excluded. Artificial Analysis currently publishes `15 of 24 models`, but the published evaluated set still misses `Claude Opus 4.8`, `Claude Opus 4.7`, `MiniMax M3`, and `GLM 5.1`.
- `ITBench-AA` is excluded. Artificial Analysis currently publishes `17 of 24 models`, but the published evaluated set still misses `Claude Opus 4.8`, `GPT-5.4`, `Claude Opus 4.6`, and `MiniMax M3`.
- `MMMU-Pro` is excluded. Artificial Analysis currently publishes `17 of 200 models`, but the published evaluated set still misses `Claude Opus 4.8`, `GPT-5.4`, `Claude Opus 4.7`, `Claude Opus 4.6`, `MiniMax M3`, `MiMo-V2.5-Pro`, `GLM 5.1`, and `DeepSeek V4-Pro`.
- `MMLU-Pro` is excluded. Artificial Analysis currently publishes `9 of 345 models`, far below full cohort coverage and missing the entire 14-model ValueRank cohort.
- `LiveCodeBench` is excluded. Artificial Analysis currently publishes `9 of 343 models`, far below full cohort coverage and missing the entire 14-model ValueRank cohort.
- `Global-MMLU-Lite` is excluded. Artificial Analysis currently publishes `11 of 111 models`, but the published evaluated set still misses `GPT-5.5`, `Claude Opus 4.8`, `GPT-5.4`, `Claude Opus 4.7`, `Gemini 3.5 Flash`, `Kimi K2.6`, `MiniMax M3`, `MiMo-V2.5-Pro`, `GLM 5.1`, and `DeepSeek V4-Pro`.
- `AIME 2025` is excluded. Artificial Analysis currently publishes `9 of 269 models`, far below full cohort coverage and missing the entire 14-model ValueRank cohort.
- `MATH-500` is excluded. Artificial Analysis currently publishes `5 of 201 models`, far below full cohort coverage and missing the entire 14-model ValueRank cohort.

Result: after rerunning the audit under the corrected rule, v1.0 still keeps the maximum currently verified zero-gap benchmark set found in current primary sources.
