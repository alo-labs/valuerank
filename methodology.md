# ValueRank Methodology

**Version:** v1.1  
**Updated:** June 12, 2026

## Cohort Rule

v1.1 ranks only the current [DeepSWE](https://deepswe.datacurve.ai/) model roster, excluding:

- `Grok-Build-0.1`
- `Gemini 3 Flash`
- `Claude Opus 4.6`

Ranked cohort:

- GPT-5.5
- Claude Opus 4.8
- GPT-5.4
- Claude Opus 4.7
- Claude Sonnet 4.6
- Gemini 3.5 Flash
- GPT-5.4 Mini
- Kimi K2.6
- MiniMax M3
- MiMo-V2.5-Pro
- GLM 5.1
- Gemini 3.1 Pro
- DeepSeek V4-Pro

## Zero-Gap Rule

v1.1 still removes the old neutral-fill system entirely.

- Every retained dimension must have a genuine current score for all 13 ranked models.
- If even one ranked model is genuinely missing from a benchmark, that benchmark is excluded.
- v1.1 therefore has **zero missing benchmark cells** and uses **no neutral 50 placeholders**.

## Scored Dimensions

ValueRank v1.1 still uses 15 fully covered dimensions:

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

Where `n = 13` for every retained benchmark in v1.1.

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

Active scored dimensions still use primary sources:

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
  - AA-Omniscience Hallucination Rate
  - Humanity's Last Exam
  - GPQA Diamond
  - SciCode
  - IFBench
  - CritPt

## Artificial Analysis Extraction Rule

Artificial Analysis benchmark leaderboards often expose only a visible top slice in the rendered results list. v1.1 therefore derives the retained AA benchmark dimensions directly from current rendered Artificial Analysis model pages.

Concrete v1.1 rule:

- 12 cohort rows were visible on the current `GPT-5.5 (xhigh)` model page.
- The missing `GPT-5.4 mini (xhigh)` row was filled from its own current model page.
- No retained-dimension value was inferred from third-party articles, screenshots, or older generations.

This remains primary-source extraction from Artificial Analysis' own current rendered pages.

## Official-First Excluded-Benchmark Audit

The benchmark-gap audit now runs in two stages:

1. Check the official benchmark-owner source first.
2. If the official source is missing models, stale, or does not publish a current leaderboard, check current secondary implementations.

A benchmark remains excluded unless a **currently published implementation** contains **all 13 ranked ValueRank models**.

Current exclusions verified during the v1.1 audit:

- `APEX-Agents`
  - Official source: [Mercor APEX-Agents leaderboard](https://www.mercor.com/apex/apex-agents-leaderboard/) still misses `Kimi K2.6`, `MiniMax M3`, `MiMo-V2.5-Pro`, `GLM 5.1`, and `DeepSeek V4-Pro`.
  - Secondary sources: [Artificial Analysis APEX-Agents-AA](https://artificialanalysis.ai/evaluations/apex-agents-aa) still misses `Claude Opus 4.8`, `Claude Opus 4.7`, `MiniMax M3`, and `GLM 5.1`; [LLM Stats APEX-Agents](https://llm-stats.com/benchmarks/apex-agents) publishes only `Gemini 3.1 Pro`, `Kimi K2.6`, and `MiniMax M3`.
  - Result: excluded.
- `ITBench`
  - Official source: [IBM Research ITBench Kaggle benchmark](https://www.kaggle.com/benchmarks/ibm-research/itbench) does not contain any of the 13 current ValueRank model names exactly as ranked here.
  - Secondary source: [Artificial Analysis ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa) still misses `Claude Opus 4.8`, `GPT-5.4`, and `MiniMax M3`.
  - Result: excluded.
- `MMMU-Pro`
  - Official source: [MMMU benchmark site](https://mmmu-benchmark.github.io/) publishes a current leaderboard, but it still misses `GPT-5.5`, `Claude Opus 4.8`, `Claude Opus 4.7`, `Gemini 3.5 Flash`, `GPT-5.4 Mini`, `Kimi K2.6`, `MiniMax M3`, `MiMo-V2.5-Pro`, `GLM 5.1`, and `DeepSeek V4-Pro`.
  - Secondary sources: [Artificial Analysis MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro) and [LLM Stats MMMU-Pro](https://llm-stats.com/benchmarks/mmmu-pro) both remain incomplete. LLM Stats is the closest secondary pass, but it still misses `Claude Opus 4.8`, `Claude Opus 4.7`, `MiMo-V2.5-Pro`, `GLM 5.1`, and `DeepSeek V4-Pro`.
  - Result: excluded.
- `MMLU-Pro`
  - Official source: [TIGER-Lab MMLU-Pro leaderboard](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) still misses `GPT-5.5`, `Claude Opus 4.8`, `Claude Opus 4.7`, `Gemini 3.5 Flash`, `GPT-5.4 Mini`, `Kimi K2.6`, `MiniMax M3`, `MiMo-V2.5-Pro`, `GLM 5.1`, and `DeepSeek V4-Pro`.
  - Secondary sources: [Kaggle MMLU-Pro](https://www.kaggle.com/benchmarks/open-benchmarks/mmlu-pro) and [LLM Stats MMLU-Pro](https://llm-stats.com/benchmarks/mmlu-pro) remain incomplete as well.
  - Result: excluded.
- `LiveCodeBench`
  - Official source: [LiveCodeBench official site](https://livecodebench.github.io/) is still the original paper-era leaderboard and does not contain the current 13-model cohort.
  - Secondary sources: [Kaggle LiveCodeBench](https://www.kaggle.com/benchmarks/open-benchmarks/livecodebench), [Artificial Analysis LiveCodeBench](https://artificialanalysis.ai/evaluations/livecodebench), and [LLM Stats LiveCodeBench](https://llm-stats.com/benchmarks/livecodebench) all remain incomplete.
  - Result: excluded.
- `Global-MMLU-Lite`
  - Official source: [Cohere Labs Global-MMLU-Lite Kaggle benchmark](https://www.kaggle.com/benchmarks/cohere-labs/global-mmlu-lite) currently contains only `Gemini 3.5 Flash` and `Claude Opus 4.8` from the ValueRank cohort.
  - Secondary sources do not close the gap.
  - Result: excluded.
- `AIME 2025`
  - Official source: the benchmark owner publishes the exam itself, not a current full frontier-model leaderboard.
  - Secondary sources: [Kaggle AIME 2025](https://www.kaggle.com/benchmarks/open-benchmarks/aime-2025) currently contains only `GPT-5.5`, `Claude Opus 4.8`, and `Gemini 3.5 Flash` from the ValueRank cohort; [Artificial Analysis AIME 2025](https://artificialanalysis.ai/evaluations/aime-2025) remains incomplete as well.
  - Result: excluded.
- `MATH-500`
  - Official source: the benchmark owner publishes the dataset and benchmark definition, not a current full frontier-model leaderboard.
  - Secondary sources: [Kaggle MATH-500](https://www.kaggle.com/benchmarks/open-benchmarks/math-500) is the strongest current alternative but still reaches only `6 of 13` ValueRank models; [Artificial Analysis MATH-500](https://artificialanalysis.ai/evaluations/math-500) remains incomplete.
  - Result: excluded.

Result: after rerunning the audit under the official-first rule and checking current secondary implementations, v1.1 still keeps the same 15-dimension zero-gap benchmark set. The only scored change in this release is the removal of `Claude Opus 4.6` from the cohort and the resulting 13-model renormalization.
