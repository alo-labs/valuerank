# Cursor Composer 2.5 vs MiMo-V2.5-Pro: Benchmark Comparison

**Research Method:** silver-multi-ai v2.3.0 (OCG-Lite, 4/5 agents)
**Date:** July 4, 2026
**Confidence:** Medium (same benchmark confirmed, cost data estimated)

---

## Executive Summary

4 independent AI agents searched BenchLM.ai, evals.report, Vals.ai, Artificial Analysis, HuggingFace, GitHub, Reddit, Hacker News, Terminal-Bench, SWE-bench, PinchBench, ClawEval, WildClawBench, Cursor blog, and Xiaomi MiMo pages.

**One benchmark comes close:** Terminal-Bench 2.0 — both models tested on the same task using the Harbor framework. Scores are nearly identical (69.3% vs 68.4%). However, **cost-per-task is not directly reported** for either model.

---

## Terminal-Bench 2.0 — The Only Shared Benchmark

| Metric | Composer 2.5 | MiMo-V2.5-Pro |
|--------|--------------|---------------|
| **Score** | 69.3% | 68.4% |
| **Framework** | Harbor (official) | Harbor (official) |
| **Cost per task** | Not directly reported | Not directly reported |
| **Token pricing** | $0.50/M in, $2.50/M out | $0.435/M in, $0.87/M out |

### Why Cost Cannot Be Directly Compared

1. **No token counts published** for either model on Terminal-Bench 2.0
2. **Agent config may differ** — Harbor framework is shared, but the agent wrapper is not specified for MiMo's run
3. **Neither party published per-task token consumption** for this benchmark

### Estimated Cost (From Token Pricing)

| Model | Input Price | Output Price | Estimated Cost Range |
|-------|-------------|--------------|---------------------|
| Composer 2.5 | $0.50/M | $2.50/M | $0.50–$1.00/task |
| MiMo-V2.5-Pro | $0.435/M | $0.87/M | $0.30–$0.60/task |

**Caveat:** These are estimates using different token assumptions, not measured values from the same benchmark run.

---

## CursorBench 3.1 — Cost Data Exists (Composer Only)

| Metric | Composer 2.5 | MiMo-V2.5-Pro |
|--------|--------------|---------------|
| **Score** | 63.2% | ❌ Not tested |
| **Cost per task** | **$0.55** | N/A |
| **Tokens per task** | 15,152 | N/A |
| **Steps per task** | 37 | N/A |

Source: https://cursor.com/cursorbench

This is the ONLY benchmark with published cost-per-task data — but only for Composer 2.5.

---

## SWE-bench Multilingual

| Metric | Composer 2.5 | MiMo-V2.5-Pro |
|--------|--------------|---------------|
| **Score** | 79.8% | 71.7% (BenchLM) |
| **Cost per task** | Not available | Not available |

MiMo's score is from BenchLM's aggregated data, not a direct submission. No cost data.

---

## Benchmarks Where Only One Model Is Tested

| Benchmark | Composer 2.5 | MiMo-V2.5-Pro |
|-----------|--------------|---------------|
| CursorBench v3.1 | 63.2% ($0.55/task) | ❌ |
| SWE-Bench Multilingual | 79.8% | ❌ |
| SWE-Bench Verified | ❌ | 78.9% |
| SWE-Bench Pro | ❌ | 57.2% |
| ClawEval | ❌ | 63.8% (Pass^3) |
| PinchBench | ❌ | 87.5% avg |
| WildClawBench | ❌ | $12.60/60 tasks |
| Chatbot Arena | ❌ | 1466 Elo |
| Vals EMB | ❌ | $0.22/task |

---

## Cost Data Summary

### Composer 2.5

| Source | Metric | Value |
|--------|--------|-------|
| Cursor pricing | Input | $0.50/M |
| Cursor pricing | Output | $2.50/M |
| CursorBench 3.1 | Cost/task | $0.55 |
| CursorBench 3.1 | Tokens/task | 15,152 |

### MiMo-V2.5-Pro

| Source | Metric | Value |
|--------|--------|-------|
| Xiaomi API | Input | $0.435/M |
| Xiaomi API | Output | $0.87/M |
| Vals EMB | Cost/task | $0.22 |
| WildClawBench | Cost/60 tasks | $12.60 (~$0.21/task) |
| AA Intelligence Index | Blended | $0.18/1M |

---

## Files in This Directory

```
benchmarks/c25-vs-mimo25p/
├── README.md                         # Scope and methodology
├── DEEP-RESEARCH-V4.md               # Full initial research report
├── FINAL_COMPARISON_UPDATED.md       # Current consolidated comparison
├── GAP-RESEARCH/                     # Curated focused follow-up research
├── claims.jsonl                      # Claim ledger
├── evidence.jsonl                    # Evidence ledger
├── sources.jsonl                     # Source ledger
├── benchmark_data.json               # Structured benchmark data
└── SOURCES.md                        # Human-readable source list
```

---

## Methodology

- **Skill:** silver-multi-ai v2.3.0 (--lite mode)
- **Dispatch:** Mechanism 2 (`opencode run --model`)
- **Models:** minimax-m3, qwen3.7-plus, deepseek-v4-flash, kimi-k2.7-code, mimo-v2.5
- **Successful:** 4 of 5 (kimi-k2.7-code returned empty)
- **Consolidation:** Cross-agent consensus (all 4 agree on Terminal-Bench 2.0 as closest match)

---

*Report generated via silver-multi-ai OCG-Lite dispatch. See `FINAL_COMPARISON_UPDATED.md` and `GAP-RESEARCH/` for the retained consolidated findings.*
