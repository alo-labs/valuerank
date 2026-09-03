# Sonar-Style Code Quality Benchmarks — Quick Reference

**Date:** 2026-06-19

## The 7 Static-Analysis-Quality Benchmarks (Sonar's 5 dimensions)

| # | Benchmark | URL | Updated | Sonar Dimensions | Models | Source Type |
|---|-----------|-----|---------|------------------|--------|-------------|
| 1 | **Sonar LLM Leaderboard** ⭐ | [sonarsource.com/.../leaderboard](https://www.sonarsource.com/the-coding-personalities-of-leading-llms/leaderboard/) | 2026-06-03 | **5/5** (all) | 70 | Industry leaderboard (canonical) |
| 2 | **Sabra et al. (SonarQube paper)** ⭐ | [arxiv:2508.14727](https://arxiv.org/abs/2508.14727) | 2025-08-20 | **5/5** (all) | 5 | Sonar-published academic paper |
| 3 | **SmellBench** | [arxiv:2606.05574](https://arxiv.org/abs/2606.05574) | 2026-06-04 | **3/5** (Correctness + Maintainability + Reliability) | 6 LLMs + 2 agents | Academic benchmark |
| 4 | **StetsonMathCS/LLM-Benchmarking-Suite** | [github.com/StetsonMathCS/LLM-Benchmarking-Suite](https://github.com/StetsonMathCS/LLM-Benchmarking-Suite) | 2026-06-19 | **4/5** (Correctness, Security, Reliability, Maintainability) | 13 | OSS benchmark |
| 5 | **svetkis/ai-code-review-benchmark** | [github.com/svetkis/ai-code-review-benchmark](https://github.com/svetkis/ai-code-review-benchmark) | 2026-06-19 | **2/5** (Reliability, Maintainability) | 10+ via OpenRouter | OSS benchmark |
| 6 | **CyberSecEval 4 (Meta)** | [github.com/facebookresearch/PurpleLlama](https://github.com/facebookresearch/PurpleLlama/tree/main/CybersecurityBenchmarks) | 2025-12-15 | **1/5** (Security only) | 4 families | OSS benchmark |
| 7 | **LLM Security Guard (CyberKatsu)** | [github.com/CyberKatsu/llm-security-guard](https://github.com/CyberKatsu/llm-security-guard) | 2026-06-14 | **1/5** (Security only) | 15+ | OSS benchmark |

## Sonar's 5 Quality Dimensions

- **Correctness** — Functional pass rate (% of tasks where code passes all tests). Higher is better.
- **Complexity** — Cyclomatic + cognitive complexity per KLOC. Lower is better.
- **Security** — Vulnerabilities per MLOC (injection, path traversal, insecure crypto). Lower is better.
- **Reliability** — Bugs per MLOC (null deref, resource leak, incorrect logic). Lower is better.
- **Maintainability** — Code smells per MLOC (duplications, long methods, poor naming, style). Lower is better.

## ValueRank 13 Models — Coverage Across 7 Benchmarks

| ValueRank Model | Coverage | Tier |
|-----------------|----------|------|
| **Claude Opus 4.8** | **7/7** | 1 — Full |
| **Claude Opus 4.7** | **7/7** | 1 — Full |
| **Claude Sonnet 4.6** | **7/7** | 1 — Full |
| Gemini 3.1 Pro | 5/7 | 2 — Strong |
| GPT-5.5 | 5/7 | 2 — Strong |
| GPT-5.4 | 5/7 | 2 — Strong |
| Gemini 3.5 Flash | 5/7 | 2 — Strong |
| GPT-5.4 Mini | 5/7 | 2 — Strong |
| MiniMax M3 | 1/7 (Sonar only) | 3 — Minimal |
| GLM 5.1 | 1/7 (Sonar only) | 3 — Minimal |
| MiMo-V2.5-Pro | 0/7 | 4 — None |
| Kimi K2.6 | 0/7 | 4 — None |
| DeepSeek V4-Pro | 0/7 | 4 — None |

## Lowest Common Denominator

The 3 models in **all 7** static-analysis-quality benchmarks:

1. **Claude Opus 4.7** (ValueRank #11, score 39.0)
2. **Claude Opus 4.8** (ValueRank #7, score 51.8)
3. **Claude Sonnet 4.6** (ValueRank #13, score 32.6)

For these 3 models, we can build a Sonar-style quality score with ≥1 source benchmark per Sonar dimension.

## Recommended Scoring Formula

```
Quality_Score = 0.30·Correctness + 0.15·(1-Complexity) + 0.25·(1-Security) + 0.15·(1-Reliability) + 0.15·(1-Maintainability)
```

(Weights approximate Sonar's public methodology; normalize each dimension to 0-1, lower-better dims inverted.)

## Key Insight: Only 2 Benchmarks Cover All 5 Sonar Dimensions

Both come from Sonar:

1. **Sonar LLM Leaderboard** (industry, 70 models, current as of 2026-06-03)
2. **Sabra et al. paper** (Sonar-published, 5 models, Aug 2025)

**Every other benchmark is a partial-subset measurement.** For the missing dimensions, you'll need to either:
- Use family-level inference (with downgrade factor)
- Run the benchmark yourself with these models
- Use SonarQube directly to generate the missing numbers (the Sabra et al. methodology is reproducible and well-documented)

## Rejected Benchmarks (don't measure Sonar 5 dimensions)

❌ SWE-bench — functional correctness only
❌ LiveCodeBench — correctness only
❌ BigCodeBench — correctness only
❌ LLM-Stats — composite aggregator
❌ Artificial Analysis — composite aggregator
❌ DevQualityEval (Symflower) — correctness + reliability only, no static analysis
❌ CoRe — static-analysis reasoning tasks, no Sonar 5-dim leaderboard
❌ codejudge (khaitha, yashgarg4) — execution-first, single composite "quality" score
❌ TheColliery (CoalMine etc.) — agent tooling, not model benchmark
❌ chris-santiago/llm-preamble — research project, no leaderboard
❌ EduardoNicacio/LLMBenchmark — SQL/.NET-specific, 20 LLMs

## Files in Working Directory

- [`benchmarks.md`](benchmarks.md) — Full research with detailed per-benchmark breakdowns
- [`dimension-summary.md`](dimension-summary.md) — This file (quick reference)
- `QUALITY_coverage_matrix_v3.json` — Machine-readable cross-reference matrix
- `/Users/shafqat/Documents/AI_Code_Quality_Benchmarks_Research_20260619/` — Raw research artifacts
