# Consolidation Rules — multi-ai-deep-research

How to consolidate outputs from multiple deep-research agents into a single comprehensive report.

---

## Overview

After all N models complete their deep-research pipelines, the consolidation phase:

1. **Deduplicates** sources, claims, and evidence across models
2. **Resolves conflicts** when models disagree
3. **Aggregates** confidence scores and ratings
4. **Produces** a single consolidated report with cross-model verification

---

## Source Deduplication

### Rules

| Rule | Description | Example |
|------|-------------|---------|
| **URL match** | Exact URL match (normalized) | `https://cursor.com/blog/composer-2-5` == `https://cursor.com/blog/composer-2-5/` |
| **Domain + path** | Same domain + path, ignore query params | `https://example.com/page?a=1` == `https://example.com/page?b=2` |
| **Title + author** | Same title + author (fuzzy match) | "Composer 2.5 Blog" by Cursor == "Introducing Composer 2.5" by Cursor |

### Normalization

1. Strip trailing slashes
2. Remove query parameters (except for known tracking params like `utm_*`)
3. Lowercase domain
4. Remove `www.` prefix
5. Normalize Unicode

### Output

Each deduped source gets a canonical ID: `[S1]`, `[S2]`, etc.

---

## Claim Deduplication

### Rules

| Rule | Description | Example |
|------|-------------|---------|
| **Semantic similarity** | First 10 words fuzzy match (>80% similarity) | "Terminal-Bench 2.0 shows C25 at 69.3%" ≈ "C25 scores 69.3% on Terminal-Bench 2.0" |
| **Entity + metric** | Same entity + same metric | "C25: 69.3% Terminal-Bench" == "Composer 2.5: 69.3% Terminal-Bench" |
| **Quote match** | Exact quote match (>50 chars) | Same verbatim quote from same source |

### Output

Each deduped claim gets a canonical ID: `[C1]`, `[C2]`, etc.

---

## Conflict Resolution

### Score Conflicts

When models report different scores for the same metric:

| Rule | Description | Use when |
|------|-------------|----------|
| **Median** | Take the median score | Numeric scores (percentages, Elo) |
| **Most recent** | Take the most recent score | Time-sensitive data |
| **Most authoritative** | Take the score from the most authoritative source | Official vs. aggregated |
| **Present all** | Show all scores with attribution | No clear winner |

### Claim Conflicts

When models make contradictory claims:

| Rule | Description | Use when |
|------|-------------|----------|
| **Evidence-weighted** | Prefer claims with stronger evidence | Claims with citations vs. unsupported |
| **Consensus** | Present the majority view | 3+ models agree |
| **Present all** | Show all viewpoints with model attribution | Legitimate disagreement |
| **Flag as uncertain** | Mark as uncertain, no resolution | Insufficient evidence |

### Source Conflicts

When models cite conflicting sources:

| Rule | Description | Use when |
|------|-------------|----------|
| **Primary > Secondary** | Prefer primary sources over secondary | Official docs vs. blog posts |
| **Verified > Unverified** | Prefer verified sources | Official leaderboards vs. community |
| **Multiple independent** | Require ≥2 independent sources | High-confidence claims |

---

## Confidence Aggregation

### Per-Model Confidence

Each model reports confidence for each claim: `high`, `medium`, `low`.

### Cross-Model Confidence

| Agreement | Confidence | Description |
|-----------|------------|-------------|
| 5/5 models agree | **very high** | Near-certain |
| 4/5 models agree | **high** | Strong consensus |
| 3/5 models agree | **medium** | Majority agreement |
| 2/5 models agree | **low** | Weak consensus |
| 1/5 models agree | **very low** | Single source |

### Confidence Boosting

- **Multiple independent sources:** +1 confidence level
- **Primary source citation:** +1 confidence level
- **Cross-model triangulation:** +1 confidence level

---

## Evidence Ledger

### Structure

```jsonl
{
  "claim_id": "C1",
  "claim": "Terminal-Bench 2.0: C25 scores 69.3%",
  "source_url": "https://cursor.com/blog/composer-2-5",
  "source_type": "primary",
  "verdict": "verified",
  "confidence": "high",
  "models_citing": ["minimax-m3", "qwen3.7-plus", "deepseek-v4-flash"],
  "quote": "Composer 2.5 achieves 69.3% on Terminal-Bench 2.0",
  "locator": "paragraph 5"
}
```

### Verdict Values

| Verdict | Description |
|---------|-------------|
| `verified` | Source supports the claim |
| `wrong` | Source contradicts the claim |
| `uncertain` | Verifier couldn't determine |
| `not_found` | Source doesn't mention the claim |

---

## Output Schemas

### `consolidated.md` Schema

```markdown
# [Topic] — Multi-Model Deep Research

**Date:** [date]
**Profile:** [ocg-standard|ocg-lite]
**Mode:** [quick|standard|deep|ultradeep]
**Models:** [list of models]

---

## Executive Summary

[200-400 word summary]

---

## Cross-Model Findings

### Finding 1: [Topic]
[Consolidated finding]

| Model | Finding | Confidence | Source |
|-------|---------|------------|--------|
| minimax-m3 | ... | high | [S1] |
| qwen3.7-plus | ... | medium | [S2] |

**Consensus:** [agreement summary]

---

## Source Registry

[All sources, deduped]

---

## Limitations & Caveats

[Disagreements, gaps]

---

## Methodology

[How consolidation was done]

---

## Bibliography

[Complete bibliography]
```

### `claims.jsonl` Schema

```jsonl
{
  "claim_id": "C1",
  "claim": "Terminal-Bench 2.0: C25 scores 69.3%",
  "entity": "C25",
  "metric": "Terminal-Bench 2.0",
  "value": "69.3%",
  "sources": ["S1", "S2", "S3"],
  "models_agreeing": 5,
  "confidence": "very high",
  "verdict": "verified"
}
```

### `sources.jsonl` Schema

```jsonl
{
  "source_id": "S1",
  "url": "https://cursor.com/blog/composer-2-5",
  "title": "Introducing Composer 2.5",
  "author": "Cursor",
  "date": "2026-05-18",
  "source_type": "primary",
  "reliability": "high",
  "models_citing": ["minimax-m3", "qwen3.7-plus", "deepseek-v4-flash"]
}
```

---

## Conflict Documentation

### `conflicts.md` Structure

```markdown
# Cross-Model Conflicts

## Conflict 1: [Topic]

**Claim:** [conflicting claim]
**Models:** [list of models]
**Resolution:** [how it was resolved]

| Model | Position | Evidence |
|-------|----------|----------|
| minimax-m3 | [position] | [evidence] |
| qwen3.7-plus | [position] | [evidence] |

**Rationale:** [why this resolution was chosen]
```

---

## Quality Checks

Before finalizing the consolidated report, verify:

- [ ] All sources are deduped (no duplicate URLs)
- [ ] All claims are deduped (no semantic duplicates)
- [ ] All conflicts are documented in `conflicts.md`
- [ ] All claims have ≥1 source citation
- [ ] High-confidence claims have ≥2 independent sources
- [ ] No unsupported factual claims pass delivery
- [ ] Bibliography is complete (every citation, no placeholders)
