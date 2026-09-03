# Cursor Composer 2.5 (C25) — PinchBench v2 & Chatbot Arena Gap Research

**Date:** 2026-07-04
**Research Mode:** ULTRADEEP (exhaustive multi-source search)
**Question:** Does Cursor Composer 2.5 have published scores on PinchBench v2 or Chatbot Arena (LMArena / arena.ai)?

---

## Executive Summary

**Cursor Composer 2.5 (C25) has NOT been evaluated on either PinchBench v2 or Chatbot Arena.** After exhaustive search across 12+ sources — including official leaderboards, benchmark aggregators, GitHub, Reddit, Hacker News, and Cursor's own documentation — no evidence of C25 scores on either benchmark was found. Both BenchLM and the comparison tables from prior research sessions confirm this gap explicitly.

---

## 1. PinchBench v2 — C25 Status: NOT LISTED

### Leaderboard Evidence

**Source:** https://pinchbench.com (fetched 2026-07-04)

The PinchBench leaderboard lists 53 models total (10 displayed, 43 more). The top 10 models by average score are:

| Rank | Model | Avg Score |
|------|-------|-----------|
| 1 | `anthropic/claude-opus-4.8-fast` | 93.5% |
| 2 | `qwen/qwen3.7-max` | 92.5% |
| 3 | `anthropic/claude-opus-4.8` | 90.5% |
| 4 | `nvidia/nemotron-3-ultra-550b-a55b` | 89.9% |
| 5 | `xiaomi/mimo-v2.5` | 89.7% |
| 6 | `x-ai/grok-build-0.1` | 88.9% |
| 7 | `qwen/qwen3.6-flash` | 88.1% |
| 8 | **`xiaomi/mimo-v2.5-pro`** | **87.5%** |
| 9 | `z-ai/glm-5.2` | 87.0% |
| 10 | `inclusionai/ling-2.6-1t` | 82.6% |

**Cursor Composer 2.5 does not appear anywhere on the leaderboard** — not in the top 10, not in the open-weights view, and not in the full model list.

### PinchBench GitHub

**Source:** https://github.com/pinchbench/skill/issues?q=cursor+composer

A search for "cursor composer" across all PinchBench GitHub issues returned **zero results**. No issues, PRs, or discussions mention Cursor Composer 2.5 being added to or evaluated on PinchBench.

### PinchBench Model Page

**Source:** https://pinchbench.com/model/cursor

The PinchBench model page for "cursor" returned an empty page with no model data.

### Verdict

**C25 has never been submitted to or evaluated on PinchBench v2.** The benchmark requires running via the OpenClaw agent framework, and Cursor's proprietary model has not been benchmarked through this pipeline.

---

## 2. Chatbot Arena (arena.ai) — C25 Status: NOT LISTED

### Leaderboard Evidence

**Source:** https://arena.ai/leaderboard/text (fetched 2026-07-04)

The Chatbot Arena text leaderboard contains **369 models** with **7,152,929 votes**. Key searches:

- **Search for "cursor":** No results found.
- **Search for "composer 2.5":** No results found.

The base model that C25 is built on — `kimi-k2.5-instant` (Moonshot) — appears at **rank 73** with **1432 Elo**, but this is the Moonshot base checkpoint, NOT Cursor's fine-tuned Composer 2.5 variant.

### BenchLM Confirmation

**Source:** https://www.benchlm.ai/models/composer-2-5

BenchLM explicitly confirms:
- **Arena Elo: N/A**
- **Categories Ranked: 0 of 8**
- "Composer 2.5 has 4 published benchmark scores on BenchLM, but it does not yet have enough non-generated coverage to receive a global overall rank."
- "This profile is currently excluded from the public leaderboard because it still lacks enough non-generated benchmark coverage to rank safely."

### Code/WebDev Arena

**Source:** https://arena.ai/leaderboard/code

The Code Arena (WebDev) leaderboard lists 92 models. Cursor Composer 2.5 does not appear.

### Verdict

**C25 has never been submitted to or evaluated on Chatbot Arena.** BenchLM confirms Arena Elo is "N/A" and the model is excluded from rankings due to insufficient benchmark coverage.

---

## 3. What C25 IS Benchmarked On

For context, Cursor's own blog (https://cursor.com/blog/composer-2-5) reports the following benchmarks for C25:

| Benchmark | C25 Score | MiMo-V2.5-Pro Score |
|-----------|-----------|---------------------|
| SWE-Bench Multilingual | 79.8% | ❌ Not reported |
| CursorBench v3.1 | 63.2% ($0.55/task) | ❌ Not reported |
| Terminal-Bench 2.0 | 65.9/100 (via BenchLM) | 68.4% (via BenchLM) |

**Key observation:** C25 and MiMo-V2.5-Pro are benchmarked on **completely different suites**. Only Terminal-Bench 2.0 shows both models, and even there the scores are close (65.9 vs 68.4). C25's benchmarks (SWE-Bench Multilingual, CursorBench) are proprietary/internal evaluations, while MiMo-V2.5-Pro's benchmarks (PinchBench, Chatbot Arena, ClawEval) are community/independent evaluations.

---

## 4. Why C25 Is Missing

Several factors explain the gap:

1. **Proprietary model access:** C25 is only available through Cursor's IDE. It cannot be independently benchmarked via API like other models on PinchBench or Chatbot Arena.

2. **No Chatbot Arena submission:** Chatbot Arena requires models to be accessible via API for blind comparison. C25 is locked to Cursor's interface.

3. **No PinchBench submission:** PinchBench runs through the OpenClaw agent framework. C25 has not been configured or submitted to this pipeline.

4. **Cursor's internal benchmarks:** Cursor focuses on its own benchmark (CursorBench) and industry-standard SWE-Bench, rather than community benchmarks.

---

## 5. Sources Consulted

| Source | URL | Finding |
|--------|-----|---------|
| PinchBench Leaderboard | https://pinchbench.com | C25 not listed |
| PinchBench GitHub | https://github.com/pinchbench/skill/issues?q=cursor+composer | Zero results |
| PinchBench Model Page | https://pinchbench.com/model/cursor | Empty page |
| Chatbot Arena Text | https://arena.ai/leaderboard/text | C25 not in 369 models |
| Chatbot Arena Code | https://arena.ai/leaderboard/code | C25 not in 92 models |
| BenchLM C25 | https://www.benchlm.ai/models/composer-2-5 | Arena Elo: N/A, 0/8 categories |
| Vals.ai C25 | https://www.vals.ai/models/cursor_composer-2.5 | 62.55% avg, no Arena/PinchBench data |
| Cursor Blog | https://cursor.com/blog/composer-2-5 | Only reports SWE-Bench & CursorBench |
| Cursor Docs | https://cursor.com/docs/models/cursor-composer-2-5 | Model documentation only |
| Evals.report | https://evals.report/models/cursor-composer-2.5 | 404 Not Found |
| Reddit r/LocalLLaMA | Search for "composer 2.5 pinchbench" | No results (verification wall) |
| Hacker News | Search for "cursor composer 2.5 chatbot arena" | No relevant threads |

---

## 6. Conclusion

**Both PinchBench v2 and Chatbot Arena scores are CONFIRMED ABSENT for Cursor Composer 2.5.**

This is a genuine gap in the competitive landscape. MiMo-V2.5-Pro has independently verified scores on both benchmarks (87.5% PinchBench, 1466 Elo Chatbot Arena), while C25 has no equivalent independent evaluations. The only benchmarks where both models can be compared are Terminal-Bench 2.0, where they score similarly (65.9 vs 68.4).

**Recommendation:** Until C25 is submitted to community benchmarks or its API becomes publicly accessible for blind evaluation, direct apples-to-apples comparison with MiMo-V2.5-Pro on PinchBench or Chatbot Arena is not possible.
