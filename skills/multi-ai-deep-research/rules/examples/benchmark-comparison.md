# Example: Benchmark Comparison — C25 vs MM25p

This example shows how to use the multi-ai-deep-research skill to compare two models across all benchmarks.

---

## Scenario

Compare Cursor Composer 2.5 (C25) and MiMo-V2.5-Pro (MM25p) across all benchmarks where both have published scores.

---

## Command

```bash
/multi-ai-deep-research "Find ALL benchmarks where BOTH Cursor Composer 2.5 (C25) and MiMo-V2.5-Pro (MM25p) have published scores. For each benchmark, provide the exact scores and attempt to calculate or estimate cost-per-task. Search exhaustively across official sources, leaderboards, GitHub, Reddit, HN, and Twitter/X." --profile ocg-lite --mode ultradeep --out ./benchmarks/c25-vs-mimo25p
```

---

## What Happens

### Phase 1: Dispatch (5 models in parallel)

Each model receives the same prompt and independently:

1. **SCOPE:** Defines research boundaries (only benchmarks with BOTH models)
2. **PLAN:** Identifies 14+ primary sources to search
3. **RETRIEVE:** Fetches and indexes all sources in parallel
4. **TRIANGULATE:** Cross-verifies scores across ≥2 sources
5. **OUTLINE REFINEMENT:** Updates outline based on findings
6. **SYNTHESIZE:** Writes the research report
7. **CRITIQUE:** Red-teams the report (ultradeep mode)
8. **REFINE:** Addresses critique points
9. **PACKAGE:** Writes final report + JSONL files

### Phase 2: Consolidation

After all 5 models complete:

1. **Dedup sources:** 28 raw sources → 15 unique
2. **Dedup claims:** 100 raw claims → 45 unique
3. **Resolve conflicts:** 3 conflicts resolved (score disagreements)
4. **Merge evidence:** All evidence items merged with cross-model verification
5. **Produce consolidated report:** Single comprehensive report

---

## Output

```
benchmarks/c25-vs-mimo25p/
├── minimax-m3.md                      # Raw CLI output
├── minimax-m3-report.md               # Full research report
├── minimax-m3-sources.jsonl           # Per-model sources
├── minimax-m3-evidence.jsonl          # Per-model evidence
├── minimax-m3-claims.jsonl            # Per-model claims
├── qwen3.7-plus.md
├── qwen3.7-plus-report.md
├── qwen3.7-plus-sources.jsonl
├── qwen3.7-plus-evidence.jsonl
├── qwen3.7-plus-claims.jsonl
├── deepseek-v4-flash.md
├── deepseek-v4-flash-report.md
├── deepseek-v4-flash-sources.jsonl
├── deepseek-v4-flash-evidence.jsonl
├── deepseek-v4-flash-claims.jsonl
├── kimi-k2.7-code.md
├── kimi-k2.7-code-report.md
├── kimi-k2.7-code-sources.jsonl
├── kimi-k2.7-code-evidence.jsonl
├── kimi-k2.7-code-claims.jsonl
├── mimo-v2.5.md
├── mimo-v2.5-report.md
├── mimo-v2.5-sources.jsonl
├── mimo-v2.5-evidence.jsonl
├── mimo-v2.5-claims.jsonl
├── consolidated.md                    # Merged report
├── consolidated.html                  # HTML preview
├── sources.jsonl                      # Deduped sources
├── evidence.jsonl                     # Merged evidence
├── claims.jsonl                       # Merged claims
├── conflicts.md                       # Cross-model conflicts
└── run-manifest.json                  # Metadata
```

---

## Key Findings (from consolidated.md)

### Only Shared Benchmark: Terminal-Bench 2.0

| Model | Score | Confidence | Source |
|-------|-------|------------|--------|
| C25 | 69.3% | high | [S1] Cursor blog |
| MM25p | 68.4% | high | [S2] HF leaderboard |

**Consensus:** All 5 models agree. C25 +0.9pp (within noise).

### Cost Analysis

| Model | Input ($/M) | Output ($/M) | Context |
|-------|:-----------:|:------------:|:-------:|
| C25 Standard | $0.50 | $2.50 | 200K |
| C25 Fast | $3.00 | $15.00 | 200K |
| MM25p | $0.435 | $0.87 | 1M |

**Consensus:** MM25p is 2.9–17x cheaper on output tokens.

### Gap Analysis

After exhaustive search across 9 benchmarks, NO additional shared benchmarks were found:
- SWE-Bench Multilingual: MM25p not evaluated
- SWE-bench Verified/Pro: C25 not tested
- GPQA Diamond, MMLU-Pro: C25 not tested (coding-only model)
- WildClawBench, ClawEval, PinchBench: C25 not tested
- Chatbot Arena: C25 not ranked

---

## Lessons Learned

1. **Profile matters:** OCG-lite is sufficient for research tasks; OCG-standard adds cost without proportional quality gain
2. **Mode matters:** ultradeep mode catches nuances that quick/standard miss (e.g., the SWE-Bench Multilingual gap)
3. **Consolidation is key:** Single-model research missed the gap analysis; multi-model triangulation found it
4. **Social media search:** GitHub `gh` CLI is more reliable than websearch for finding specific benchmark data
5. **Timeout:** 900s (15 min) per model is sufficient for ultradeep research; adjust as needed

---

## Variations

### Quick Research (2-5 min)

```bash
/multi-ai-deep-research "What is the best vector database for RAG?" --profile ocg-lite --mode quick
```

### Standard Research (5-10 min)

```bash
/multi-ai-deep-research "Compare LangChain vs LlamaIndex" --profile ocg-lite --mode standard
```

### Deep Research (10-20 min)

```bash
/multi-ai-deep-research "What are the security implications of LLM agents?" --profile ocg-standard --mode deep
```

### UltraDeep Research (20-45 min)

```bash
/multi-ai-deep-research "Find ALL benchmarks where BOTH models have scores" --profile ocg-lite --mode ultradeep
```
