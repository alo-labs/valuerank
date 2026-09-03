# multi-ai-deep-research

Multi-model deep research skill. Dispatch the same research task to N LLM models in parallel, each following the deep-research methodology, then consolidate outputs into a single comprehensive report.

---

## Quick Start

```bash
/multi-ai-deep-research "Your research question" --profile ocg-lite --mode ultradeep
```

---

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--profile` | `ocg-lite` | Model profile: `ocg-standard` (6 models) or `ocg-lite` (5 models) |
| `--mode` | `ultradeep` | Research depth: `quick`, `standard`, `deep`, `ultradeep` |
| `--out` | `./.runs/multi-ai-deep-research/<timestamp>/` | Output directory |

---

## Profiles

### OCG-Lite (default, budget-friendly)

- `opencode-go/minimax-m3`
- `opencode-go/qwen3.7-plus`
- `opencode-go/deepseek-v4-flash`
- `opencode-go/kimi-k2.7-code`
- `opencode-go/mimo-v2.5`

### OCG-Standard (highest quality)

- `opencode-go/minimax-m3`
- `opencode-go/qwen3.7-max`
- `opencode-go/deepseek-v4-pro`
- `opencode-go/glm-5.2`
- `opencode-go/kimi-k2.6`
- `opencode-go/mimo-v2.5-pro`

---

## Modes

| Mode | Phases | Duration | Use when |
|------|--------|----------|----------|
| `quick` | SCOPE, RETRIEVE, PACKAGE | 2-5 min | Initial exploration |
| `standard` | + PLAN, TRIANGULATE, OUTLINE, SYNTHESIZE | 5-10 min | Standard research |
| `deep` | + CRITIQUE, REFINE | 10-20 min | Critical decisions |
| `ultradeep` | All 8+ phases | 20-45 min | Comprehensive review |

---

## Output

```
<out-dir>/
├── <model-slug>.md                    # Raw output per model
├── <model-slug>-report.md             # Full research report per model
├── <model-slug>-sources.jsonl         # Per-model sources
├── <model-slug>-evidence.jsonl        # Per-model evidence
├── <model-slug>-claims.jsonl          # Per-model claims
├── consolidated.md                    # Merged report (all models)
├── consolidated.html                  # HTML preview
├── sources.jsonl                      # Deduped sources
├── evidence.jsonl                     # Merged evidence
├── claims.jsonl                       # Merged claims
├── conflicts.md                       # Cross-model conflicts
└── run-manifest.json                  # Metadata
```

---

## Examples

### Benchmark Comparison

```bash
/multi-ai-deep-research "Find ALL benchmarks where BOTH Cursor Composer 2.5 and MiMo-V2.5-Pro have published scores" --profile ocg-lite --mode ultradeep
```

### Technology Comparison

```bash
/multi-ai-deep-research "Compare LangChain vs LlamaIndex for production RAG" --profile ocg-standard --mode deep
```

### Security Analysis

```bash
/multi-ai-deep-research "What are the security implications of LLM agents with tool access?" --profile ocg-lite --mode ultradeep
```

---

## Rules

- [Dispatch Mechanics](rules/dispatch-mechanics.md) — How to launch N parallel LLM processes
- [Consolidation Rules](rules/consolidation-rules.md) — How to merge outputs from multiple models
- [Methodology](rules/methodology.md) — Deep-research 8-phase pipeline (multi-model adaptation)
- [Output Schema](rules/output-schema.md) — Structure of consolidated.md and JSONL files

---

## Examples

- [Benchmark Comparison](rules/examples/benchmark-comparison.md) — C25 vs MM25p comparison
