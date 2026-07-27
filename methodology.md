# ValueRank Methodology

**Version:** v1.3
**Updated:** July 28, 2026

## Cohort Rule

v1.3 ranks the **full current [DeepSWE](https://deepswe.datacurve.ai/) Best roster** (**18 models**, source updated July 25, 2026). Historical exclusions that remain off-roster: `Grok-Build-0.1`, `Gemini 3 Flash`, `Claude Opus 4.6`. `Grok 4.5` is ranked (it is on DeepSWE Best).

Ranked cohort:

- Kimi K3
- Grok 4.5
- Muse Spark 1.1
- GPT-5.6 Terra
- GPT-5.6 Sol
- Claude Opus 5
- GPT-5.6 Luna
- GPT-5.5
- Claude Fable 5
- GLM-5.2
- Gemini 3.6 Flash
- GPT-5.4
- Claude Opus 4.8
- Gemini 3.1 Pro
- Kimi K2.7 Code
- Gemini 3.5 Flash
- Claude Sonnet 5
- Claude Sonnet 4.6

## Zero-Gap Rule

- Every retained dimension must have a genuine current score for all **18** ranked models.
- If even one ranked model is genuinely missing from a benchmark, that benchmark is excluded.
- v1.3 has **zero missing benchmark cells** and uses **no neutral 50 placeholders** on the main product.

## Scored Dimensions

ValueRank v1.3 uses **12** fully covered dimensions:

1. Cost
2. Hallucination
3. DeepSWE
4. GDPval-AA
5. AA-LCR
6. Omni Acc
7. HLE
8. GPQA
9. SciCode
10. CritPt
11. AA Intelligence Index
12. Speed

Dropped vs v1.2 (incomplete AA coverage for newest DeepSWE models): IFBench, Terminal-Bench Hard, τ²-Bench Telecom.

## Weights

Relative v1.2 priorities are preserved among retained dimensions and renormalized to 100%:

| Dimension | Weight |
|---|---:|
| Cost | 32.05% |
| Hallucination | 7.69% |
| DeepSWE | 8.97% |
| GDPval-AA | 7.69% |
| AA-LCR | 5.13% |
| Omni Acc | 5.13% |
| HLE | 5.13% |
| GPQA | 5.13% |
| SciCode | 5.13% |
| CritPt | 3.85% |
| AA Intelligence Index | 7.69% |
| Speed | 6.41% |

## Normalization

`((n - rank) / (n - 1)) * 100` with `n = 18`.

- Best → 100, worst → 0, ties average ranks.
- For Hallucination, lower raw rate is better.
- For Cost, lower composite cost is better.

## Cost Construction

DeepSWE-only (AA Intelligence Index total eval cost unpublished for Kimi K2.7 Code; zero-gap forbids partial AA cost)

1. Take DeepSWE Best-row average cost per task for each model.
2. Scale onto 0–100 with the highest-cost ranked model at 100.
3. Rank-normalize that penalty for the Cost dimension.

When AA Index total eval cost returns for every cohort member, v1.x can restore the AA+DeepSWE composite average used in v1.1–v1.2.

## Quality Score

Quality removes the Cost term and renormalizes remaining non-cost dimensions to 100%.

## Source Policy

- DeepSWE for pass@1 and avg cost.
- Artificial Analysis model pages for retained AA metrics.
- Official-first gap audit for excluded benchmarks (see raw-data.md).
