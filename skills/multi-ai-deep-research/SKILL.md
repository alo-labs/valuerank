---
name: multi-ai-deep-research
description: Dispatch deep-research tasks across multiple LLM models in parallel, each following the deep-research methodology, then consolidate outputs into a single comprehensive report. Use when you need multi-model research with citation tracking, evidence persistence, and structured report generation.
argument-hint: "<research-question> [--profile ocg-standard|ocg-lite] [--mode quick|standard|deep|ultradeep] [--out <dir>]"
user-invocable: true
version: 1.0.0
---

# /multi-ai-deep-research — Multi-Model Deep Research

Dispatch the same deep-research task to N LLM models in parallel. Each model independently follows the deep-research methodology (8-phase pipeline). Results are consolidated into a single comprehensive report with cross-model triangulation.

**What this skill does:**
1. Dispatches the user's research question to N LLM models in parallel
2. Each model follows the deep-research methodology (SCOPE, PLAN, RETRIEVE, TRIANGULATE, SYNTHESIZE, CRITIQUE, REFINE, PACKAGE)
3. Captures each model's full research output
4. Consolidates findings across models (dedup claims, resolve conflicts, merge sources)
5. Produces a single comprehensive report with cross-model verification

---

## Usage

```
/multi-ai-deep-research "<research-question>" [--profile ocg-standard|ocg-lite] [--mode quick|standard|deep|ultradeep] [--out <dir>]
```

### Inputs

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `research-question` | YES | — | The research question sent to every model verbatim. Use `@file.md` to inline a multi-line prompt. |
| `--profile` | NO | `ocg-lite` | Model profile: `ocg-standard` (6 models, highest quality) or `ocg-lite` (5 models, budget-friendly). |
| `--mode` | NO | `ultradeep` | Deep-research mode: `quick` (3 phases), `standard` (6 phases), `deep` (8 phases), `ultradeep` (8+ phases). |
| `--out` | NO | `./.runs/multi-ai-deep-research/<timestamp>/` | Output directory for all artifacts. |

### Profiles

#### OCG-Lite (default, budget-friendly)

| Model | Notes |
|-------|-------|
| `opencode-go/minimax-m3` | Budget-friendly |
| `opencode-go/qwen3.7-plus` | Mid-tier |
| `opencode-go/deepseek-v4-flash` | Flash-tier |
| `opencode-go/kimi-k2.7-code` | Code-specialized |
| `opencode-go/mimo-v2.5` | Non-pro tier |

#### OCG-Standard (highest quality)

| Model | Notes |
|-------|-------|
| `opencode-go/minimax-m3` | Budget-friendly |
| `opencode-go/qwen3.7-max` | Top-tier |
| `opencode-go/deepseek-v4-pro` | Pro-tier |
| `opencode-go/glm-5.2` | GLM |
| `opencode-go/kimi-k2.6` | Kimi |
| `opencode-go/mimo-v2.5-pro` | Pro tier |

### Modes (deep-research phases)

| Mode | Phases | Duration | Use when |
|------|--------|----------|----------|
| `quick` | SCOPE, RETRIEVE, PACKAGE | 2-5 min | Initial exploration |
| `standard` | SCOPE, PLAN, RETRIEVE, TRIANGULATE, OUTLINE REFINEMENT, SYNTHESIZE, PACKAGE | 5-10 min | Standard research |
| `deep` | SCOPE, PLAN, RETRIEVE, TRIANGULATE, OUTLINE REFINEMENT, SYNTHESIZE, CRITIQUE, REFINE, PACKAGE | 10-20 min | Critical decisions |
| `ultradeep` | All 8+ phases | 20-45 min | Comprehensive review |

---

## Dispatch Mechanics

This skill uses **Mechanism 2** from silver-multi-ai: `opencode run --model <provider/model>`.

```bash
OUT=./.runs/multi-ai-deep-research/$(date +%Y%m%d-%H%M%S)
mkdir -p "$OUT"

MODE="ultradeep"  # or from --mode argument

# Create the deep-research prompt for each model
PROMPT="You are a deep-research agent. Follow the deep-research skill methodology.

FIRST: Read the deep-research skill files:
- /Users/shafqat/.agents/skills/deep-research/SKILL.md
- /Users/shafqat/.agents/skills/deep-research/reference/methodology.md

MODE: ${MODE}

RESEARCH QUESTION: <user's question>

Follow the 8-phase pipeline (SCOPE, PLAN, RETRIEVE, TRIANGULATE, OUTLINE REFINEMENT, SYNTHESIZE, CRITIQUE, REFINE, PACKAGE) in ${MODE} mode.

TOOLS TO USE (in order of preference):
1. ctx_fetch_and_index(url, source) — Fetch and index web content (PRIMARY)
2. ctx_batch_execute(commands, queries) — Run multiple commands in parallel
3. gh CLI — Search GitHub issues, discussions, repos (gh search issues/discussions/code/repos)
4. websearch/webfetch — Fallback for Reddit, HN, Twitter/X, general web
5. search-cli — If installed (npm install -g search-cli)

Write your findings to: ${OUT}/<model-slug>-report.md

Output contract:
- Executive Summary
- Main Analysis with cited findings
- Sources/Bibliography (complete)
- Methodology Appendix
- sources.jsonl, evidence.jsonl, claims.jsonl (if in deep/ultradeep mode)"

# Dispatch to each model in parallel
for model in opencode-go/minimax-m3 opencode-go/qwen3.7-plus opencode-go/deepseek-v4-flash; do
  slug=$(echo "$model" | cut -d/ -f2)
  npx -y opencode-ai run \
    --model "$model" \
    --title "deep-research-${slug}" \
    --dangerously-skip-permissions \
    "$PROMPT" \
    > "$OUT/${slug}.md" 2> "$OUT/${slug}.err" &
done

wait
echo "Outputs in $OUT/"
```

---

## Output Structure

```
<out-dir>/
├── <model-slug>.md                    # Raw output per model
├── <model-slug>.err                   # stderr per model
├── <model-slug>-report.md             # Full research report per model
├── <model-slug>-sources.jsonl         # Per-model source registry
├── <model-slug>-evidence.jsonl        # Per-model evidence store
├── <model-slug>-claims.jsonl          # Per-model claim ledger
├── consolidated.md                    # Merged report (all models)
├── consolidated.html                  # HTML preview
├── sources.jsonl                      # Merged source registry (deduped)
├── evidence.jsonl                     # Merged evidence store
├── claims.jsonl                       # Merged claims (with cross-model verification)
├── conflicts.md                       # Cross-model disagreements + resolutions
└── run-manifest.json                  # Inputs, models, timing, mode, profile
```

### `consolidated.md` Structure

```markdown
# [Topic] — Multi-Model Deep Research

**Date:** [date]
**Profile:** [ocg-standard|ocg-lite]
**Mode:** [quick|standard|deep|ultradeep]
**Models:** [list of models]

---

## Executive Summary

[200-400 word summary of findings across all models]

---

## Cross-Model Findings

### Finding 1: [Topic]
[Consolidated finding from all models, with citations]

| Model | Finding | Confidence | Source |
|-------|---------|------------|--------|
| minimax-m3 | ... | high | [url] |
| qwen3.7-plus | ... | medium | [url] |
| deepseek-v4-flash | ... | high | [url] |

**Consensus:** [agreement/disagreement summary]

---

## Source Registry

[All sources cited across all models, deduped]

---

## Limitations & Caveats

[Cross-model disagreement areas, source gaps]

---

## Methodology

- **Profile:** [ocg-standard|ocg-lite]
- **Mode:** [quick|standard|deep|ultradeep]
- **Total agents:** [N]
- **Sources consulted:** [count]
- **Triangulation:** [how conflicts were resolved]

---

## Bibliography

[Complete bibliography from all sources]
```

---

## Consolidation Algorithms

### Deduplication
- **Sources:** Dedup by URL (normalized)
- **Claims:** Dedup by semantic similarity (fuzzy match on first 10 words)
- **Evidence:** Dedup by source URL + quote hash

### Conflict Resolution
- **Score conflicts:** Median across models
- **Claim conflicts:** Present all viewpoints with model attribution
- **Source conflicts:** Prefer primary sources over secondary

### Cross-Model Verification
- **Consensus scoring:** Count models agreeing on each finding
- **Confidence weighting:** Weight by model confidence level
- **Evidence triangulation:** Require ≥2 independent sources for high-confidence claims

---

## Failure Modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `npx opencode-ai run` returns instantly with no output | Model unavailable, network error, or rate-limited | Check stderr; substitute or skip the model |
| Subprocess dies after 2 min with no report | Shell tool's 2-min default timeout | Set explicit `timeout` on bash tool |
| 5/N models return, others missing | One model in API outage | Substitute or skip; flag in `run-manifest.json` |
| All N models return same content (no diversity) | Prompt too narrow, or models from same provider family | Broaden prompt; use diverse provider families |
| MCP rate-limit (9 calls/30s) blocks mid-task | Single-query loops in agent | Pass `queries: [array]` batched |
| Cross-model conflict can't be resolved automatically | Models give incomparable answers | Present all + document "no consensus" in `conflicts.md` |

---

## Task Examples

### Example 1: Research Question
```
/multi-ai-deep-research "What are the best practices for implementing RAG with vector databases?" --profile ocg-lite --mode ultradeep
```

### Example 2: Comparison
```
/multi-ai-deep-research "Compare LangChain vs LlamaIndex for production RAG applications" --profile ocg-standard --mode deep
```

### Example 3: Gap Analysis
```
/multi-ai-deep-research "What are the security implications of LLM agents with tool access?" --profile ocg-lite --mode ultradeep
```

---

## Optional: Install search-cli

For enhanced search capabilities, install `search-cli`:

```bash
npm install -g search-cli
```

This provides:
- Unified CLI aggregating Brave, Serper, Exa, Jina, Firecrawl
- Auto-detects best provider per query type (academic, news, general, people)
- JSON output for structured processing: `search "query" --json`
- Modes: general, news, academic, scholar, patents, people, images, extract, scrape

If not installed, the skill falls back to `ctx_fetch_and_index`, `gh` CLI, and `websearch`/`webfetch`.

---

## See Also

- `silver-multi-ai` — for generic multi-model dispatch (non-research tasks)
- `deep-research` — for single-model deep research
- `find-skills` — to discover other skills
