# Deep Research Methodology — Multi-Model Adaptation

This file adapts the deep-research 8-phase pipeline for multi-model execution. Each model follows this methodology independently; the consolidation phase merges their outputs.

---

## Phase 1: SCOPE — Research Framing

**Objective:** Define research boundaries and success criteria

**Activities:**
1. Decompose the question into core components
2. Identify stakeholder perspectives
3. Define scope boundaries (what's in/out)
4. Establish success criteria
5. List key assumptions to validate

**UltraDeep Application:** Use extended reasoning to explore multiple framings of the question before committing to scope.

**Output:** Structured scope document with research boundaries

---

## Phase 2: PLAN — Strategy Formulation

**Objective:** Create an intelligent research roadmap

**Activities:**
1. Identify primary and secondary sources
2. Map knowledge dependencies (what must be understood first)
3. Create search query strategy with variants
4. Plan triangulation approach
5. Estimate time/effort per phase
6. Define quality gates

**Graph-of-Thoughts:** Branch into multiple potential research paths, then converge on optimal strategy.

**Output:** Research plan with prioritized investigation paths

---

## Phase 3: RETRIEVE — Parallel Information Gathering

**Objective:** Systematically collect information from multiple sources using parallel execution for maximum speed

**CRITICAL: Execute ALL searches in parallel using a single message with multiple tool calls**

### Query Decomposition Strategy

Before launching searches, decompose the research question into 5-10 independent search angles:

1. **Core topic (semantic search)** — Meaning-based exploration of main concept
2. **Technical details (keyword search)** — Specific terms, APIs, implementations
3. **Recent developments (date-filtered)** — What's new in last 12-18 months
4. **Academic sources (domain-specific)** — Papers, research, formal analysis
5. **Alternative perspectives (comparison)** — Competing approaches, criticisms
6. **Statistical/data sources** — Quantitative evidence, metrics, benchmarks
7. **Industry analysis** — Commercial applications, market trends
8. **Critical analysis/limitations** — Known problems, failure modes, edge cases

### Source Types

| Source Type | Priority | Use when |
|-------------|----------|----------|
| Official docs/blogs | Primary | Model scores, pricing, features |
| Benchmark leaderboards | Primary | Scores, rankings |
| Research papers | Primary | Methodology, technical details |
| News/analysis | Secondary | Context, interpretation |
| Community (Reddit, HN) | Secondary | User experience, edge cases |
| Social media (Twitter/X) | Tertiary | Announcements, reactions |

### Tools

**Primary: `ctx_fetch_and_index(url, source)`**
- Fetches URL content, converts HTML to markdown, persists in searchable knowledge base
- Use for: official docs, blog posts, leaderboard pages, benchmark results
- Returns preview windows; retrieve specific sections via `ctx_search(queries)`

**Secondary: `ctx_batch_execute(commands, queries)`**
- Runs multiple commands in parallel, auto-indexes output
- Use for: multi-URL fetches, GitHub searches, API queries
- Pass `concurrency: 4-8` for I/O-bound work

**Tertiary: `gh` CLI (GitHub)**
- Search issues: `gh search issues "query" --limit 20`
- Search discussions: `gh search discussions "query" --limit 20`
- Search code: `gh search code "query" --limit 20`
- Search repos: `gh search repos "query" --limit 20`

**Fallback: `websearch` / `webfetch`**
- Use when ctx_fetch_and_index fails or for ad-hoc searches
- WebSearch for: Reddit, HN, Twitter/X, general web
- WebFetch for: specific URLs

**Optional: `search-cli` (if installed)**
- Unified CLI aggregating Brave, Serper, Exa, Jina, Firecrawl
- Auto-detects best provider per query type
- JSON output: `search "query" --json`
- Install: `npm install -g search-cli`
- If not available, use the tools above

**Installation note:** If you want to use search-cli, install it first:
```bash
npm install -g search-cli
```

**Output:** Indexed sources with evidence store

---

## Phase 4: TRIANGULATE — Cross-Source Verification

**Objective:** Verify claims across multiple independent sources

**Activities:**
1. For each major claim, find ≥2 independent sources
2. Flag single-source claims as lower confidence
3. Identify contradictions between sources
4. Resolve contradictions with evidence weighting

**Confidence Levels:**

| Sources | Confidence | Description |
|---------|------------|-------------|
| 3+ independent | High | Strong triangulation |
| 2 independent | Medium | Moderate triangulation |
| 1 only | Low | Single source, needs verification |

**Output:** Verified claims with confidence levels

---

## Phase 4.5: OUTLINE REFINEMENT

**Objective:** Refine the report outline based on retrieval results

**Activities:**
1. Update outline with actual findings
2. Remove sections with insufficient evidence
3. Add sections discovered during retrieval
4. Prioritize findings by strength of evidence

**Output:** Refined outline ready for synthesis

---

## Phase 5: SYNTHESIZE — Draft Generation

**Objective:** Write the research report

**Activities:**
1. Write each section following the refined outline
2. Cite all sources inline with bracketed IDs [S1], [S2], etc.
3. Present findings with evidence
4. Note disagreements and uncertainties

**Output:** Complete draft report

---

## Phase 6: CRITIQUE — Red-Teaming (Deep/UltraDeep only)

**Objective:** Challenge the report's claims and structure

**Activities:**
1. Identify unsupported claims
2. Check for logical fallacies
3. Verify all citations are accurate
4. Challenge assumptions
5. Look for missing perspectives

**Output:** List of critique points to address

---

## Phase 7: REFINE — Iterative Improvement (Deep/UltraDeep only)

**Objective:** Address critique points and strengthen the report

**Activities:**
1. Address each critique point
2. Add missing evidence
3. Strengthen weak arguments
4. Remove unsupported claims
5. Update confidence levels

**Output:** Refined report ready for packaging

---

## Phase 8: PACKAGE — Final Output

**Objective:** Produce the final deliverables

**Activities:**
1. Write final report with all sections
2. Generate sources.jsonl (deduped source registry)
3. Generate evidence.jsonl (evidence store)
4. Generate claims.jsonl (claim ledger)
5. Generate run-manifest.json (metadata)
6. Generate HTML preview (if applicable)

**Output Contract:**

**Required sections:**
- Executive Summary (200-400 words)
- Introduction (scope, methodology, assumptions)
- Main Analysis (4-8 findings, 600-2,000 words each, cited)
- Synthesis & Insights (patterns, implications)
- Limitations & Caveats
- Recommendations
- Bibliography (COMPLETE — every citation, no placeholders)
- Methodology Appendix

**Output files:**
- Markdown (primary source of truth)
- `sources.jsonl` — stable source registry with canonical IDs
- `evidence.jsonl` — append-only evidence store with quotes and locators
- `claims.jsonl` — atomic claim ledger with support status
- `run_manifest.json` — query, mode, assumptions, provider config

**Quality standards:**
- 10+ sources, 3+ per major claim (cluster-independent, not just count)
- All factual claims cited immediately [S1], [S2] with evidence backing in `evidence.jsonl`
- Claim-support verification mandatory: no unsupported factual claims pass delivery
- No placeholders, no fabricated citations
- Prose-first (>=80%), bullets sparingly

---

## Multi-Model Adaptation Notes

### Per-Model Independence

Each model follows this methodology independently. Do NOT share state between models during phases 1-7. This ensures:
- Independent verification (triangulation is real, not circular)
- Diverse perspectives (models don't anchor on each other's findings)
- Conflict detection (disagreements surface naturally)

### Consolidation Phase (Post-Phase 8)

After all models complete Phase 8, the consolidation phase:
1. Deduplicates sources, claims, and evidence across models
2. Resolves conflicts using the rules in `consolidation-rules.md`
3. Aggregates confidence scores
4. Produces a single consolidated report

### Mode-Specific Behavior

| Mode | Phases | Per-Model Duration | Consolidation |
|------|--------|-------------------|---------------|
| `quick` | SCOPE, RETRIEVE, PACKAGE | 2-5 min | Basic merge |
| `standard` | All except CRITIQUE, REFINE | 5-10 min | Dedup + conflict resolution |
| `deep` | All 8 phases | 10-20 min | Full + cross-source verification |
| `ultradeep` | All 8+ phases | 20-45 min | Full + evidence ledger |
