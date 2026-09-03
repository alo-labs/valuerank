# Final Benchmark Comparison: C25 vs MM25p (Updated with Gap Research)

**Deep Research UltraDeep — July 4, 2026**
**10 agents total: 5 for initial research + 5 for gap research**

---

## Executive Summary

**After exhaustive gap research across 9 benchmarks, NO additional shared benchmarks were found.** Terminal-Bench 2.0 remains the ONLY benchmark with published scores for both models.

---

## Gap Research Results

| Benchmark | Missing Model | Agent Finding | Verdict |
|-----------|:-------------:|---------------|---------|
| **SWE-Bench Multilingual** | MM25p | Exhaustive search across 12+ sources: Xiaomi blog, HF card, BenchLM, Vals.ai, SWE-Bench official leaderboard, GitHub, Reddit, HN. MM25p NOT evaluated. V2-Flash/V2-Pro had 71.7% but V2.5-Pro does not. | **NO SCORE** |
| **SWE-bench Verified** | C25 | Searched Cursor blog, SWE-bench official leaderboard, Scale AI, BenchLM, Vals.ai, DataCamp, The Decoder, HN, GitHub. C25 NOT on leaderboard. | **NO SCORE** |
| **SWE-bench Pro** | C25 | Same sources as above. C25 NOT on Scale AI leaderboard. | **NO SCORE** |
| **GPQA Diamond** | C25 | Searched Cursor blog/docs/evals, BenchLM (shows 0/0 in Knowledge), Vals.ai, Artificial Analysis, Arena AI, HN (0 mentions in 225+ comments). C25 is coding-specialized, no API for independent eval. | **NO SCORE** |
| **MMLU-Pro** | C25 | Same sources as GPQA Diamond. C25 does not publish general knowledge benchmarks. | **NO SCORE** |
| **WildClawBench** | C25 | WildClawBench paper lists 19 models: Claude Opus 4.7, GPT 5.5, Claude Opus 4.6, GPT 5.4, GLM 5.1, DeepSeek V4 Pro, MiMo V2.5 Pro, GLM 5, Gemini 3.1 Pro, MiMo V2 Pro, Qwen3.5 397B, DeepSeek V3.2, GLM 5 Turbo, MiniMax M2.7, Kimi K2.5, MiMo V2 Flash, MiniMax M2.5, Step 3.5 Flash, Grok 4.20 Beta. **C25 NOT in list.** | **NO SCORE** |
| **ClawEval** | C25 | ClawEval paper does not mention Cursor or Composer 2.5. | **NO SCORE** |
| **PinchBench v2** | C25 | PinchBench leaderboard (53 models), C25 absent. GitHub issues: zero results for "cursor composer". | **NO SCORE** |
| **Chatbot Arena** | C25 | Searched all 369 text models and 92 code models on arena.ai — C25 absent. BenchLM explicitly shows "Arena Elo: N/A". | **NO SCORE** |

---

## Why C25 Is Missing from Most Benchmarks

**Structural reason:** C25 is proprietary to Cursor's IDE. It cannot be accessed via API for independent evaluation. Cursor only submits to:
1. **CursorBench 3.1** (proprietary, 63.2%)
2. **SWE-Bench Multilingual** (79.8%)
3. **Terminal-Bench 2.0** (69.3%)

C25 does NOT appear on any open leaderboard (Vals.ai, Arena.ai, PinchBench, WildClawBench, ClawEval, SWE-bench Verified/Pro, GPQA, MMLU, etc.).

---

## Why MM25p Is Missing from SWE-Bench Multilingual

**Structural reason:** Xiaomi chose not to submit MM25p to SWE-Bench Multilingual. They submitted to:
- SWE-bench Verified (78.9%)
- SWE-bench Pro (57.2%)
- Terminal-Bench 2.0 (68.4%)
- FrontierSWE (rank #3.4)

The V2-Flash and V2-Pro had 71.7% on SWE-Bench Multilingual, but V2.5-Pro does not report it. The Xiaomi blog page has chart containers for SWE-Bench Multilingual but they are not populated.

---

## ONLY Shared Benchmark: Terminal-Bench 2.0

| Benchmark | C25 Score | MM25p Score | Winner | Same Harness? | Source |
|-----------|:---------:|:-----------:|:------:|:-------------:|--------|
| **Terminal-Bench 2.0** | **69.3%** | **68.4%** | C25 +0.9pp | Yes (Harbor framework) | [Cursor blog](https://cursor.com/blog/composer-2-5), [HF leaderboard](https://huggingface.co/datasets/harborframework/terminal-bench-2.0) |

The 0.9pp gap is within the typical ±2.0–2.9pp confidence interval — the models are **statistically tied**.

---

## Cost Analysis

### Pricing

| Model | Input ($/M tok) | Output ($/M tok) | Context | Architecture |
|-------|:---------------:|:----------------:|:-------:|-------------|
| **C25 Standard** | $0.50 | $2.50 | 200K | Kimi K2.5 proprietary |
| **C25 Fast** (default) | $3.00 | $15.00 | 200K | Kimi K2.5 proprietary |
| **MM25p** | $0.435 | $0.87 | 1M | 1.02T MoE (42B active) |

### Cost per Task on Terminal-Bench 2.0 (Estimated)

Token counts are **not published**. Using the formula: `cost = (input_tokens × input_price + output_tokens × output_price) / 1e6`

| Scenario | Total Tokens | I/O Split | C25 Std | C25 Fast | MM25p |
|----------|:-----------:|:---------:|:-------:|:--------:|:-----:|
| Small (CursorBench-like) | 15,152 | 70/30 | $0.016 | $0.097 | $0.009 |
| Medium | 100,000 | 50/50 | $0.150 | $0.900 | $0.065 |
| Large | 200,000 | 50/50 | $0.300 | $1.800 | $0.131 |
| Output-heavy | 100,000 | 30/70 | $0.190 | $1.140 | $0.074 |

**Key insight:** CursorBench's published $0.55/task at 15,152 tokens implies cache-read/write fees are included. The naive formula gives ~$0.016 — a 34x discrepancy.

### Published Per-Task Costs

| Benchmark | C25 Cost | MM25p Cost | Source |
|-----------|:--------:|:----------:|--------|
| CursorBench 3.1 | **$0.55** | N/A | cursor.com/evals |
| WildClawBench | N/A | **$0.21** | internlm/WildClawBench |
| ClawEval | N/A | **~$0.04** | Xiaomi blog |
| Vals Index avg | N/A | **$0.09** | vals.ai |

---

## Pricing Advantage

| Metric | C25 Std vs MM25p | C25 Fast vs MM25p |
|--------|:----------------:|:-----------------:|
| Input token cost ratio | 1.1x | 6.9x |
| Output token cost ratio | 2.9x | 17.2x |
| Context window | 0.2x (200K vs 1M) | 0.2x |
| Cache hit pricing | N/A | $0.004/M (MM25p) |
| Open weights | No | Yes (MIT) |

---

## Source URLs

| Source | URL |
|--------|-----|
| Cursor Blog | https://cursor.com/blog/composer-2-5 |
| CursorBench 3.1 | https://cursor.com/evals |
| HF MiMo-V2.5-Pro | https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro |
| Terminal-Bench 2.0 (Official) | https://www.tbench.ai/leaderboard/terminal-bench/2.0 |
| Terminal-Bench 2.0 (HF) | https://huggingface.co/datasets/harborframework/terminal-bench-2.0 |
| BenchLM Compare | https://benchlm.ai/compare/composer-2-5-vs-mimo-v2-5-pro |
| Vals.ai C25 | https://www.vals.ai/models/cursor_composer-2.5 |
| Vals.ai MM25p | https://www.vals.ai/models/xiaomi_mimo-v2.5-pro |
| LMArena | https://arena.ai/leaderboard |
| AA Intelligence Index | https://artificialanalysis.ai/leaderboards/models |
| WildClawBench | https://huggingface.co/datasets/internlm/WildClawBench |
| PinchBench | https://pinchbench.com |
| Evals.report | https://evals.report/models/xiaomi-mimo-v2-5-pro |
| Lushbinary Guide | https://lushbinary.com/blog/cursor-composer-2-5-developer-guide-benchmarks-pricing/ |
| DataCamp Analysis | https://www.datacamp.com/blog/composer-2-5 |
| The Decoder | https://the-decoder.com/cursors-composer-2-5-matches-opus-4-7-and-gpt-5-5-benchmarks-at-a-fraction-of-the-cost |
| SWE-Bench Multilingual | https://www.swebench.com/multilingual-leaderboard.html |
| SWE-bench Verified | https://www.swebench.com/ |
| Scale AI SWE-bench Pro | https://scale.com/leaderboard/swe-bench-pro |

---

## Methodology

- **Mode:** UltraDeep (8-phase pipeline)
- **Total agents:** 10 (5 initial + 5 gap research)
- **OCG-Lite models used:** minimax-m3, qwen3.7-plus, deepseek-v4-flash, kimi-k2.7-code, mimo-v2.5
- **Sources consulted:** 28+ primary sources
- **Verification:** Each score cross-checked across ≥2 sources where possible
- **GitHub searches:** Via `gh` CLI for issues/discussions
- **Social media:** Reddit (r/LocalLLaMA, r/MachineLearning), Hacker News, Twitter/X

---

*Report generated by 10 parallel OCG-Lite agents following the deep-research skill with ultradeep mode.*
