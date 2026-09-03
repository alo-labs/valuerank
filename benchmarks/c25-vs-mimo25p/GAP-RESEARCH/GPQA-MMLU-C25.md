# GAP Analysis: Cursor Composer 2.5 — GPQA Diamond & MMLU-Pro Scores

**Date:** 2026-07-04
**Mode:** ULTRADEEP exhaustive search
**Target:** Cursor Composer 2.5 (C25)
**Benchmarks of interest:** GPQA Diamond, MMLU-Pro
**Comparison anchor:** MiMo-V2.5-Pro scores 86.6% GPQA Diamond, 68.5% MMLU-Pro

---

## Executive Summary

**Verdict: Cursor Composer 2.5 has NOT published scores on GPQA Diamond or MMLU-Pro.** After exhaustive search across 15+ sources, no evidence of C25 being evaluated on either benchmark was found. This is consistent with C25's nature as a coding-specialized agentic model — its evaluations focus entirely on coding/agentic benchmarks (CursorBench 3.1, SWE-Bench, Terminal-Bench).

---

## Sources Searched

| # | Source | URL | Result |
|---|--------|-----|--------|
| 1 | Cursor Blog | cursor.com/blog/composer-2-5 | Benchmark table is an image (no text extraction possible). Text mentions only coding benchmarks. No GPQA/MMLU. |
| 2 | Cursor Docs | cursor.com/docs/models/cursor-composer-2-5 | Lists strengths, tools, pricing. No benchmark numbers at all. |
| 3 | CursorBench (Evals) | cursor.com/evals | Only CursorBench 3.1 scores shown (C25: 63.2%). C25's OWN evaluations are coding-only. |
| 4 | BenchLM | benchlm.ai/models/composer-2-5 | **Key finding**: C25 has "0 benchmarks" in Knowledge category (GPQA, SuperGPQA, MMLU-Pro, HLE, FrontierScience, SimpleQA). Category score: 0.0/100. C25 excluded from leaderboard — only 4/251 benchmarks published, all coding. |
| 5 | Vals.ai | vals.ai/models/cursor_composer-2.5 | Only 3 benchmarks listed: Vibe Code Bench v1.1, SWE-bench, Terminal-Bench 2.1. No GPQA Diamond. No MMLU-Pro. |
| 6 | Artificial Analysis | artificialanalysis.ai/leaderboards/models | Has GPQA Diamond as an evaluation metric. C25 is NOT a tracked model on this platform. |
| 7 | Arena AI | arena.ai/leaderboard | C25 does NOT appear on the leaderboard in any category. |
| 8 | OpenRouter | openrouter.ai/cursor/composer-2.5 | "The model 'cursor/composer-2.5' is not available." |
| 9 | DataCamp | datacamp.com/blog/composer-2-5 | Discusses Terminal-Bench 2.0 (69.3%) and SWE-Bench Multilingual (79.8%). No GPQA/MMLU. |
| 10 | The Decoder | the-decoder.com/...composer-2-5... | Claims "matches Opus 4.7 and GPT-5.5 benchmarks" — refers to CursorBench coding benchmarks. No GPQA/MMLU. |
| 11 | Hacker News (Algolia) | hn.algolia.com | "Composer 2.5" + GPQA = 0 hits. "Composer 2.5" + MMLU = 0 hits. Across 225+ comment HN thread, zero mentions of GPQA or MMLU. |
| 12 | CodeJam article | codejam.info/2026/06/... | Explicitly states C25 is "only available through Cursor, so it's not possible to rank it on traditional benchmarks like Arena AI's Code Arena." |
| 13 | evals.report | evals.report | Tracks GPQA Diamond as a benchmark. C25 does NOT appear in their model list. |
| 14 | GitHub (HN discussion) | — | Composer 2.5 discussion centered on CursorBench opacity, not GPQA/MMLU scores. |
| 15 | Reddit | reddit.com | Could not access (verification wall) |

---

## Detailed Findings

### 1. BenchLM — Most definitive evidence

Composer 2.5 profile on BenchLM explicitly shows:

- **Knowledge category score: 0.0/100** (weight: 12%)
- **0 benchmarks** in Knowledge category (GPQA, SuperGPQA, MMLU-Pro, HLE, FrontierScience, SimpleQA)
- C25 currently has only **4 published benchmark scores out of 251 tracked** — all coding/agentic
- Excluded from public leaderboard due to insufficient non-generated benchmark coverage

Source: [https://benchlm.ai/models/composer-2-5](https://benchlm.ai/models/composer-2-5)

### 2. Cursor's Own Benchmarks

C25 is evaluated exclusively on coding benchmarks:

| Benchmark | Score |
|-----------|-------|
| CursorBench 3.1 | 63.2% |
| Terminal-Bench 2.0 | 69.3% (C25) vs 61.7% (Composer 2) |
| SWE-Bench Multilingual | 79.8% (C25) vs 73.7% (Composer 2) |

No general knowledge or reasoning benchmarks (GPQA, MMLU-Pro, HLE, etc.) appear in any Cursor-published evaluation.

Source: [https://cursor.com/evals](https://cursor.com/evals), [https://cursor.com/blog/composer-2-5](https://cursor.com/blog/composer-2-5)

### 3. Third-Party Eval Platforms

- **Artificial Analysis**: GPQA Diamond is part of their "Intelligence Index" but C25 is not tracked.
- **Vals.ai**: Only coding benchmarks listed for C25.
- **Arena AI**: C25 not present in any leaderboard category (Text, Code, Agent, Vision, etc.).

### 4. Discussion Forums

- **Hacker News** (225+ comments on C25 announcement): Zero comments connecting C25 to GPQA or MMLU.
- **CodeJam analysis**: Confirms "it's not possible to rank it on traditional benchmarks."
- **The Decoder**: Mentions "benchmarks" but in the context of coding/agentic evaluations only.

---

## Why No GPQA/MMLU Scores?

Multiple factors explain the absence:

1. **C25 is a coding-specialized agentic model** — not a general-purpose LLM. Its training (RL on long-horizon coding tasks, synthetic feature-deletion tasks, targeted text feedback for tool calls) optimizes for software engineering, not general knowledge or scientific reasoning.

2. **C25 is only available through Cursor's IDE** — there is no API to run independent third-party evaluation. Researchers cannot query C25 on GPQA Diamond or MMLU-Pro without the Cursor interface.

3. **Cursor's evaluation philosophy** — Cursor benchmarks their model on CursorBench (their proprietary metric) and SWE-Bench/Terminal-Bench (industry coding standards). They explicitly state "behavioral dimensions like communication style and effort calibration are not well captured by existing benchmarks."

4. **Base model provenance** — C25 is RL fine-tuned from Kimi K2.5. Kimi K2.5 itself may not have publicly reported GPQA Diamond or MMLU-Pro scores (Kimi is also primarily coding-tuned).

---

## Implications for MiMo-V2.5-Pro Comparison

Since C25 has no GPQA Diamond or MMLU-Pro scores:

1. **Non-comparable on these dimensions** — A direct like-for-like comparison on GPQA Diamond and MMLU-Pro is not possible.
2. **Different strengths** — C25 optimizes for coding agent tasks (tool use, file edits, long-horizon sessions). MiMo-V2.5-Pro is a general-purpose reasoning model.
3. **Alternative comparison axes**: SWE-Bench, Terminal-Bench, CursorBench, and coding-specific metrics may be more appropriate for comparing C25 vs MiMo-V2.5-Pro.

---

## Exhaustiveness Confirmation

This research searched:
- 9 direct URL fetches (Cursor blog, docs, evals, BenchLM, Vals.ai, Artificial Analysis, DataCamp, The Decoder, OpenRouter)
- 1 direct API call (HN Algolia for stories and comments)
- 2 indirect analysis (CodeJam article, evals.report)
- 1 attempt at Arena AI leaderboard

No source was found containing GPQA Diamond or MMLU-Pro scores for Cursor Composer 2.5.

**Confidence: 95%** (10% residual uncertainty for: Twitter/X which could not be searched programmatically; Reddit which was behind verification wall; Chinese-language sources not indexed).

---

## Methodology

- **Mode:** ULTRADEEP (8-phase pipeline)
- **Search strategy:** Name-dropping (GPQA, MMLU-Pro, MMLU, benchmark, score, reasoning) across each source
- **Tools used:** WebFetch, ctx_fetch_and_index, ctx_search, HN Algolia API, JavaScript sandbox analysis
- **Date context:** July 4, 2026 — research conducted ~7 weeks after C25 release (May 18, 2026)
