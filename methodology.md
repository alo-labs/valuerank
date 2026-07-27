# ValueRank Methodology

**Version:** v1.3.1
**Updated:** July 28, 2026

## Cohort Rule

v1.3.1 ranks **17** models from the current [DeepSWE](https://deepswe.datacurve.ai/) Best roster (source updated July 25, 2026; roster size 18). Historical exclusions that remain off-roster: `Grok-Build-0.1`, `Gemini 3 Flash`, `Claude Opus 4.6`. `Grok 4.5` is ranked (it is on DeepSWE Best).

**Changelog vs v1.3:** `Kimi K2.7 Code` removed from the ranked cohort so Cost can restore the AA+DeepSWE composite (AA Index total eval cost unpublished for that model).

Ranked cohort (n=17):

- Grok 4.5
- Kimi K3
- Muse Spark 1.1
- GPT-5.6 Terra
- GPT-5.6 Sol
- Claude Opus 5
- GPT-5.6 Luna
- GPT-5.5
- Gemini 3.6 Flash
- GLM-5.2
- Gemini 3.1 Pro
- Claude Fable 5
- GPT-5.4
- Gemini 3.5 Flash
- Claude Opus 4.8
- Claude Sonnet 5
- Claude Sonnet 4.6

## Ranked-cohort exclusion

**Kimi K2.7 Code** is on the DeepSWE Best roster but **not ranked** in ValueRank v1.3.1:

- Reason: no published AA Intelligence Index **total eval cost** on [https://artificialanalysis.ai/models/kimi-k2-7-code](https://artificialanalysis.ai/models/kimi-k2-7-code).
- Evidence: [`.refresh/v1.3/aa-kimi-k27-cost-search.md`](.refresh/v1.3/aa-kimi-k27-cost-search.md) (search verdict NOT FOUND, 2026-07-28).
- DeepSWE pass@1 / avg cost remain in [raw-data.md](raw-data.md) as a non-ranked appendix row.

## Zero-Gap Rule

- Every retained dimension must have a genuine current score for all **17** ranked models.
- If even one ranked model is genuinely missing from a benchmark, that benchmark is excluded.
- v1.3.1 has **zero missing benchmark cells** and uses **no neutral 50 placeholders** on the main product.

## Scored Dimensions

ValueRank v1.3.1 uses **12** fully covered dimensions:

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

Dropped vs v1.2 (incomplete AA coverage for newest DeepSWE models — still incomplete after excluding Kimi K2.7 Code): IFBench, Terminal-Bench Hard, τ²-Bench Telecom.

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

`((n - rank) / (n - 1)) * 100` with `n = 17`.

- Best → 100, worst → 0, ties average ranks.
- For Hallucination, lower raw rate is better.
- For Cost, lower composite cost is better.

## Cost Construction

Composite AA+DeepSWE (restored in v1.3.1):

1. Normalize AA Intelligence Index **total eval cost** onto 0–100 (highest-cost ranked model = 100; higher cost = higher penalty).
2. Normalize DeepSWE Best-row average cost per task onto 0–100 the same way.
3. Average the two penalties → composite cost scale.
4. Rank-normalize that composite (lower better) for the Cost dimension.

## Quality Score

Quality removes the Cost term and renormalizes remaining non-cost dimensions to 100%.

## Source Policy

- DeepSWE for pass@1 and avg cost.
- Artificial Analysis model pages for retained AA metrics.
- Official-first gap audit for excluded benchmarks (see raw-data.md).
