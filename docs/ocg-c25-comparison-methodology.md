# OCG Models vs Cursor Pro (Composer 2.5) Comparison Methodology

## Purpose

This document describes the methodology used to compare OpenCode Go (OCG) subscription plans with Cursor Pro's Composer 2.5 (C25) model on a value-per-dollar basis. The goal is to determine which plan delivers more quality work per $20 spent.

## Data Sources

### 1. OpenCode Go (OCG) Plan Structure
- Source: [opencode.ai/docs/go/](https://opencode.ai/docs/go/#usage-limits)
- Plan cost: $10/month (stacked 2x = $20/month)
- Monthly API budget: $60 per plan = $120 stacked
- Time-based limits: 5-hour ($12), weekly ($30), monthly ($60)
- Available models include: GLM-5.2, Kimi K2.7 Code, Kimi K2.6, MiMo-V2.5-Pro, MiniMax M3, Qwen3.7 Max, DeepSeek V4 Pro, and others

### 2. Cursor Pro Plan Structure
- Source: [cursor.com/blog/composer-2-5](https://cursor.com/blog/composer-2-5)
- Plan cost: $20/month
- Monthly API budget: $200 of C25 API-rate value
- Model: Cursor Composer 2.5 (in-house)
- API rates: $0.50/M input, $0.20/M cache, $2.50/M output

### 3. Artificial Analysis Benchmark Data
- Source: [artificialanalysis.ai](https://artificialanalysis.ai/)
- **AA Intelligence Index**: 9-benchmark academic suite (GDPval, HLE, GPQA, τ³-Banking, Terminal-Bench v2.1, SciCode, CritPt, AA-Omniscience, AA-LCR)
- **AA Coding Agent Index**: 3-benchmark coding suite (Terminal-Bench v2, SWE-Pro-Hard-AA, SWE-Atlas-QnA)
- Per-run token usage (answer tokens + reasoning tokens)

## Token Mix Assumptions

The user's actual Cursor usage was captured in a CSV file (usage-events-2026-06-19.csv) showing the following token mix across 986 coding agent events:

| Token type | Share |
|---|---:|
| Fresh input (w/o cache write) | 7.32% |
| Cache read | 92.24% |
| Output | 0.43% |

This mix is used for all blended-rate calculations unless otherwise specified. For some comparisons, a "coding task mix" (50.8% input / 48.9% cache / 0.5% output, derived from AA's C25 data) is used instead.

## Core Formulas

### Blended Rate at Given Mix

```
blended_rate = (input_share × input_price) +
               (cache_share × cache_price) +
               (output_share × output_price)
```

All prices are in USD per million tokens ($/M).

### OCG Tokens per Month

For OCG stacked 2x at $120/month budget:

```
ocg_tokens = (120 / blended_rate) × 1,000,000
```

### Cursor Pro Tokens per Month

For Cursor Pro at $200/month budget:

```
cursor_tokens = (200 / blended_rate) × 1,000,000
```

### Token Efficiency (Score/M)

From AA benchmark data:

```
score_per_million = aa_score / aa_tokens_M
```

Where:
- `aa_score` = AA Intelligence Index or Coding Agent Index score (0-100 scale)
- `aa_tokens_M` = total tokens to complete the benchmark, in millions

### Quality Points per Month

```
quality_points = (ocg_tokens / 1,000,000) × score_per_million
```

## Benchmark Data (Verified via Playwright)

### AA Intelligence Index (per-run token usage)

| Model | Score | Tokens (M) | Score/M |
|---|---:|---:|---:|
| GLM-5.2 (max) | 51.09 | 42.8 | 1.194 |
| MiniMax M3 | 44.44 | 24.0 | 1.852 |
| DeepSeek V4 Pro (Max) | 44.27 | 37.0 | 1.196 |
| Qwen3.7 Max | 45.99 | 102.9 | 0.447 |
| Kimi K2.6 | 42.84 | 35.0 | 1.224 |
| MiMo-V2.5-Pro | 42.24 | 20.5 | 2.060 |
| Kimi K2.7 Code | 41.95 | 17.7 | 2.370 |

### AA Coding Agent Index

| Agent | Score | Tokens (M) | Cost/task | Score/M |
|---|---:|---:|---:|---:|
| Cursor CLI + Composer 2.5 | 52.0 | 3.57 | $0.085 | 14.57 |
| Claude Code + Fable 5 (max w/ fallback) | 77.0 | 14.05 | $11.75 | 5.48 |
| Claude Code + Opus 4.8 (max) | 73.0 | 17.97 | $7.70 | 4.06 |
| Cursor CLI + Composer 2 | 67.0 | 2.93 | $0.043 | 22.87 |
| Claude Code + DeepSeek V4 Pro (high) | 47.0 | 9.74 | $0.272 | 4.83 |

### API Rates (per 1M tokens)

| Model | Input | Cache | Output |
|---|---:|---:|---:|
| MiMo-V2.5-Pro | $0.435 | $0.004 | $0.87 |
| MiniMax M3 | $0.30 | $0.06 | $1.20 |
| Cursor Composer 2.5 | $0.50 | $0.20 | $2.50 |
| GLM-5.2 | $0.50 | $0.10 | $2.00 |
| Kimi K2.6 | $0.60 | $0.12 | $2.40 |
| Kimi K2.7 Code | $0.60 | $0.12 | $2.40 |
| Qwen3.7 Max | $0.80 | $0.16 | $3.20 |
| DeepSeek V4 Pro | $0.55 | $0.14 | $2.20 |

## Comparison Approaches

### Approach 1: Strict Same-Benchmark Comparison

Only compare models that are measured on the same AA benchmark. This is the most rigorous approach but limits which models can be compared directly.

**Within Intelligence Index** (M3, MiMo, GLM-5.2, Qwen3.7 Max, Kimi K2.6, Kimi K2.7 Code, V4 Pro):
- Quality scores and token usage are directly comparable
- Score/M and quality/mo are valid metrics

**Within Coding Agent Index** (C25, V4 Pro, Claude variants, GPT variants):
- Same direct comparability applies
- Note: C25 is the only OCG-equivalent model in this cohort (via Cursor Pro)

### Approach 2: Bridge via Common Model (V4 Pro)

V4 Pro is the only model in AA's data that appears on both benchmarks:
- Intelligence Index: 44.27 score, 37.0M tokens
- Coding Agent Index: 47.0 score, 9.74M tokens

Bridge ratios:
- Quality ratio (coding/overall): 47.0 / 44.27 = 1.062
- Token ratio (coding/overall): 9.74 / 37.0 = 0.263

To estimate a model's performance on the benchmark where it's not measured:
```
estimated_score_on_other = actual_score × bridge_quality_ratio
estimated_tokens_on_other = actual_tokens × bridge_token_ratio
```

**Important caveat**: The V4 Pro bridge assumes V4 Pro's coding/overall ratios are representative of other models. This is a reasonable but unverified assumption.

### Approach 3: Plan-Level Value Comparison

For the final answer, combine plan costs, API rates, and benchmark data:

1. Compute blended rate at the assumed token mix
2. Compute tokens per month at the plan's $ budget
3. Compute quality points per month using Score/M from the relevant benchmark
4. Compare across plans

## Key Findings

### OCG vs Cursor Pro at Cursor Mix (both $20/mo)

| Plan | Blended $/M | Tokens/mo |
|---|---:|---:|
| OCG MiMo stacked 2x | $0.0393 | 3.056B |
| OCG M3 stacked 2x | $0.0825 | 1.455B |
| Cursor Pro (C25) | $0.2318 | 0.863B |

**OCG MiMo gives 3.54× more tokens than Cursor Pro** at Cursor mix, because MiMo's cache rate ($0.004/M) is 50× cheaper than C25's ($0.20/M), and Cursor mix is 92.24% cache.

### Quality Points per Month (Cursor mix)

| Plan | Tokens/mo | Score/M | Quality/mo |
|---|---:|---:|---:|
| OCG MiMo (Intelligence Index) | 3.056B | 2.060 | 6,296 |
| OCG M3 (Intelligence Index) | 1.455B | 1.852 | 2,695 |
| Cursor Pro C25 (Coding Agent Index) | 0.863B | 14.57 | 12,573 |

**C25 wins on quality points per month for coding work** by ~2× over both M3 and MiMo, because of its exceptional coding token efficiency (14.57 Score/M).

### M3 vs C25 (with V4 Pro bridge)

On Coding Agent Index (where C25 is measured):
- C25 (actual): 52.0 score, 3.57M tokens, 14.57 Score/M
- M3 (estimated): 47.2 score, 6.32M tokens, 7.47 Score/M
- C25 wins by 10.2% on quality, 2× on efficiency

On Intelligence Index (where M3 is measured):
- M3 (actual): 44.44 score, 24.0M tokens
- C25 (estimated): 49.0 score, 13.6M tokens
- C25 wins by 10.2% on quality (estimated)

**C25 wins on value for both benchmarks** (M3 does not win over C25 in any plausible comparison).

## Methodology Limitations

1. **Benchmark mismatch**: C25 is only on Coding Agent Index; M3 and MiMo are only on Intelligence Index. Direct comparison requires bridging via V4 Pro, which adds uncertainty.

2. **API rate estimates**: OCG's actual API rates for some models (GLM, Kimi, Qwen, V4 Pro) are estimates from OCG docs. The confirmed rates are for MiMo and M3 (from AA model pages).

3. **M3 Plus / Cursor Pro actual quota**: M3 Plus's "1.7B tokens/month" is a marketing estimate, not a published hard cap. The actual weekly cap (~680M tokens) was back-derived from user data. Cursor Pro's $200 of API value is the published cap.

4. **Token mix sensitivity**: All comparisons assume Cursor mix (92.24% cache). At different mixes (e.g., coding mix at 50% cache), the rankings shift. The user's actual mix from their CSV is the primary assumption.

5. **Score/M as efficiency metric**: The Score/M metric assumes quality is linear in tokens, which may not hold. A model that's 2× more efficient per token might not be 2× more useful for all tasks.

6. **AA data freshness**: AA benchmark scores change over time as models are re-evaluated. The scores used here were current as of June 2026.

7. **No direct head-to-head test**: This analysis is based on indirect comparisons via AA benchmarks. The only way to settle M3 vs C25 definitively is to run both on the same tasks and measure actual cost + quality.

## Reproducibility

All token data and scores were extracted from AA's pages using Playwright (Python 3.9) to render the JavaScript charts. The extracted data is in the local analysis files (aa_overall2.html, kimi_k27.html, aa_coding_chart.html). The Python scripts that computed the comparisons are in /tmp/ (build_final.py, fetch_k27_url.py, etc.).

## Version History

- 2026-06-23: Initial methodology documented after comparing OCG MiMo/M3 stacked 2x vs Cursor Pro (C25)
- Key data points verified: M3 44.44 score / 24.0M tokens, MiMo 42.24 / 20.5M, C25 52 / 3.57M
- Key finding: C25 wins on coding value (2× over M3/MiMo) despite Cursor Pro's lower token volume
