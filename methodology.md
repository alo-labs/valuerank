# ValueRank Methodology

**Version:** v1.2
**Updated:** June 20, 2026

## Cohort Rule

v1.2 ranks only the current [DeepSWE](https://deepswe.datacurve.ai/) leaderboard roster. The DeepSWE roster has **shrunk to 8 models** since v1.1 — five previously ranked models have left the DeepSWE roster and one new model has been added.

Ranked cohort:

- GPT-5.5
- Claude Fable 5  *(NEW in v1.2)*
- Claude Opus 4.8
- GPT-5.4
- Claude Sonnet 4.6
- Gemini 3.5 Flash
- Kimi K2.7 Code  *(was Kimi K2.6 in v1.1)*
- Gemini 3.1 Pro Preview

Models removed from the v1.2 cohort because they are no longer on the DeepSWE leaderboard:

- GPT-5.4 Mini
- MiMo-V2.5-Pro
- MiniMax M3
- GLM 5.1
- DeepSeek V4-Pro

Their v1.1 scores (computed under the v1.1 13-model cohort) are preserved below for historical reference. **These scores are not directly comparable to v1.2** because the normalization denominator (`n`) changed from 13 to 8.

### v1.1 Scores of Models Removed from Cohort

| Model | v1.1 Rank | v1.1 Overall | v1.1 Quality | v1.1 Composite Cost | Pareto (v1.1) |
|---|---:|---:|---:|---:|:---:|
| MiMo-V2.5-Pro | 3 | 58.1 | 44.2 | $7.04 | ✓ |
| MiniMax M3 | 4 | 56.0 | 52.4 | $18.32 | ✗ |
| DeepSeek V4-Pro | 9 | 48.0 | 36.3 | $14.22 | ✗ |
| GLM 5.1 | 10 | 40.0 | 36.7 | $25.82 | ✗ |
| GPT-5.4 Mini | 12 | 36.5 | 29.3 | $18.95 | ✗ |
| Claude Opus 4.7 | 11 | 39.0 | 52.0 | $100.00 | ✗ |

Note: `Claude Opus 4.7` is also listed above — it was removed in v1.1 itself (replaced by Claude Opus 4.8) and is therefore not on the current DeepSWE roster either.

Models still excluded (not on DeepSWE):

- `Grok-Build-0.1`
- `Gemini 3 Flash`
- `Claude Opus 4.6`

## Zero-Gap Rule

v1.2 still removes the old neutral-fill system entirely.

- Every retained dimension must have a genuine current score for all **8** ranked models.
- If even one ranked model is genuinely missing from a benchmark, that benchmark is excluded.
- v1.2 therefore has **zero missing benchmark cells** and uses **no neutral 50 placeholders**.

## Scored Dimensions

ValueRank v1.2 still uses 15 fully covered dimensions:

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

(Weights sum to 101% — preserved verbatim from v1.1 to keep historical continuity; the published "100%" label refers to the user-facing 100-pt score scale, not the literal weight sum.)

## Normalization

Each dimension is rank-normalized:

`((n - rank) / (n - 1)) * 100`

Where `n = 8` for every retained benchmark in v1.2.

- Best score gets `100`
- Worst score gets `0`
- Ties receive the average of the tied ranks
- There are **no missing-data cells**

For AA-Omniscience Hallucination Rate, lower raw hallucination is better.

## Cost Construction

The `Cost` dimension is built in three steps before rank-normalization:

1. Normalize current Artificial Analysis eval cost onto `0–100`, with the highest-cost ranked model set to `100`.
2. Normalize current DeepSWE average cost per task onto `0–100`, with the highest-cost ranked model set to `100`.
3. Average those two penalty terms back onto a single `0–100` composite cost scale.

Lower composite cost is better.

## Quality Score

The Quality Score removes the 25% cost term and renormalizes the remaining 14 non-cost dimensions to 100%.

## Source Policy

Active scored dimensions use primary sources:

- [DeepSWE](https://deepswe.datacurve.ai/) for DeepSWE pass@1 and DeepSWE average cost per task.
- Artificial Analysis model pages for:
  - Artificial Analysis Intelligence Index
  - Speed
  - Eval cost
  - GDPval-AA v2
  - Terminal-Bench v2.1
  - τ²-Bench Telecom
  - AA-LCR
  - AA-Omniscience Accuracy
  - AA-Omniscience Hallucination Rate
  - Humanity's Last Exam
  - GPQA Diamond
  - SciCode
  - IFBench
  - CritPt

## Artificial Analysis Extraction Rule

AA benchmark leaderboards often expose only a visible top slice in the rendered results list. v1.2 derives the retained AA benchmark dimensions directly from current rendered Artificial Analysis model pages.

Concrete v1.2 rule:

- 7 cohort rows were visible on the current `GPT-5.5 (xhigh)` model page.
- The missing `Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)` row was filled from its own current model page at `/models/claude-fable-5`.
- For Gemini 3.5 Flash, the `(high)` variant was used instead of the DeepSWE `[medium]` variant because the `(medium)` variant on AA does not publish GDPval-AA v2, the AA Intelligence Index v4.1, or a complete Terminal-Bench Hard v2.1 score, which would break zero-gap. This matches the v1.1 extraction rule of picking the variant with the most complete benchmark coverage.
- No retained-dimension value was inferred from third-party articles, screenshots, or older generations.

This remains primary-source extraction from Artificial Analysis's own current rendered pages.

## Official-First Excluded-Benchmark Audit

The benchmark-gap audit runs in two stages:

1. Check the official benchmark-owner source first.
2. If the official source is missing models, stale, or does not publish a current leaderboard, check current secondary implementations.

A benchmark remains excluded unless a **currently published implementation** contains **all 8 ranked ValueRank models**.

v1.2 excludes (with current audit results against the n=8 cohort):

- `APEX-Agents`
  - Official source: [Mercor APEX-Agents leaderboard](https://www.mercor.com/apex/apex-agents-leaderboard/) still misses `Claude Fable 5`, `Kimi K2.7 Code`, `Claude Opus 4.8`, and `Claude Sonnet 4.6`.
  - Secondary: [Artificial Analysis APEX-Agents-AA](https://artificialanalysis.ai/evaluations/apex-agents-aa) covers 5 of 8 — still missing `Claude Fable 5`, `Claude Opus 4.8`, and `Kimi K2.7 Code`.
  - Result: excluded.
- `ITBench`
  - Official source: [IBM Research ITBench Kaggle benchmark](https://www.kaggle.com/benchmarks/ibm-research/itbench) does not contain any of the 8 exact ValueRank model names.
  - Secondary: [Artificial Analysis ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) remains incomplete.
  - Result: excluded.
- `MMMU-Pro`
  - Official source: [MMMU benchmark site](https://mmmu-benchmark.github.io/) is the original paper-era leaderboard and does not contain the current ValueRank cohort.
  - Secondary: [Artificial Analysis MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro) and [LLM Stats MMMU-Pro](https://llm-stats.com/benchmarks/mmmu-pro) remain incomplete.
  - Result: excluded.
- `MMLU-Pro`
  - Official source: [TIGER-Lab MMLU-Pro leaderboard](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) does not contain the current ValueRank cohort.
  - Secondary: [Kaggle MMLU-Pro](https://www.kaggle.com/benchmarks/open-benchmarks/mmlu-pro) and [LLM Stats MMLU-Pro](https://llm-stats.com/benchmarks/mmlu-pro) remain incomplete.
  - Result: excluded.
- `LiveCodeBench`
  - Official source: [LiveCodeBench official site](https://livecodebench.github.io/) is the original paper-era leaderboard and does not contain the current ValueRank cohort.
  - Secondary: [Kaggle LiveCodeBench](https://www.kaggle.com/benchmarks/open-benchmarks/livecodebench), [Artificial Analysis LiveCodeBench](https://artificialanalysis.ai/evaluations/livecodebench), and [LLM Stats LiveCodeBench](https://llm-stats.com/benchmarks/livecodebench) remain incomplete.
  - Result: excluded.
- `Global-MMLU-Lite`
  - Official source: [Cohere Labs Global-MMLU-Lite Kaggle benchmark](https://www.kaggle.com/benchmarks/cohere-labs/global-mmlu-lite) does not contain the current ValueRank cohort.
  - Secondary implementations do not close the gap.
  - Result: excluded.
- `AIME 2025`
  - The benchmark owner publishes the exam itself, not a current frontier-model leaderboard.
  - Secondary: [Kaggle AIME 2025](https://www.kaggle.com/benchmarks/open-benchmarks/aime-2025) and [Artificial Analysis AIME 2025](https://artificialanalysis.ai/evaluations/aime-2025) remain incomplete.
  - Result: excluded.
- `MATH-500`
  - The benchmark owner publishes the dataset and benchmark definition, not a current frontier-model leaderboard.
  - Secondary: [Kaggle MATH-500](https://www.kaggle.com/benchmarks/open-benchmarks/math-500) is the strongest current alternative but still covers only a subset of the 8-model cohort.
  - Result: excluded.

Result: after rerunning the audit under the official-first rule and checking current secondary implementations against the 8-model cohort, v1.2 still keeps the same 15-dimension zero-gap benchmark set. The changes in this release are the cohort shrink from 13 to 8 models and the addition of Claude Fable 5.
