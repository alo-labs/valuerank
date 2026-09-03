# SWE-bench Verified & SWE-bench Pro: Cursor Composer 2.5 Score Search

**Research Date:** 2026-07-04
**Research Mode:** ULTRADEEP
**Status:** COMPLETE — No scores found

---

## Executive Summary

**After exhaustive search across 15+ sources, Cursor Composer 2.5 (C25) has NOT published scores on SWE-bench Verified or SWE-bench Pro.**

Cursor only published three benchmarks for C25:
1. **SWE-bench Multilingual:** 79.8%
2. **Terminal-Bench 2.0:** 69.3%
3. **CursorBench v3.1:** 63.2%

**Gap confirmed:** There are no comparable SWE-bench Verified or SWE-bench Pro scores for C25 to compare against MiMo-V2.5-Pro's 79.1% (Verified) and 57.2% (Pro).

---

## Research Methodology

### Sources Searched

| Source | URL | Result |
|--------|-----|--------|
| Cursor Blog | https://cursor.com/blog/composer-2-5 | No SWE-bench Verified/Pro mentioned |
| Cursor Docs | https://cursor.com/docs/models/cursor-composer-2-5 | No benchmark scores |
| Cursor Evals (CursorBench) | https://cursor.com/evals | Only CursorBench v3.1 scores |
| BenchLM | https://benchlm.ai/models/composer-2-5 | Lists benchmarks but shows 0.0/100 (no sourced data) |
| Vals.ai | https://www.vals.ai/models/cursor_composer-2.5 | Shows 0.0% for SWE-bench (placeholder) |
| SWE-bench Official (Verified) | https://www.swebench.com/verified.html | **No Cursor/Composer entries found** |
| SWE-bench Official (Multilingual) | https://www.swebench.com/multilingual-leaderboard.html | C25 not listed |
| Scale AI SWE-bench Pro | https://scale.com/leaderboard/swe_bench_pro_public | **No Cursor/Composer entries found** |
| DataCamp | https://www.datacamp.com/blog/composer-2-5 | Only reports Multilingual, Terminal-Bench, CursorBench |
| The Decoder | https://the-decoder.com/cursors-composer-2-5-matches-opus-4-7-and-gpt-5-5-benchmarks-at-a-fraction-of-the-cost | Only mentions SWE-Bench Multilingual (79.8%) |
| Lushbinary | https://lushbinary.com/blog/cursor-composer-2-5-developer-guide-benchmarks-pricing/ | Only Multilingual, Terminal-Bench, CursorBench |
| Hacker News | HN Algolia API search | Zero stories about C25 + SWE-bench Verified/Pro |
| Reddit | r/LocalLLaMA, r/MachineLearning | No relevant results (403/blocked) |
| GitHub | cursor-ai org search | No relevant issues/discussions |
| Twitter/X | @cursor_ai | Could not access (Nitter blocked) |

### Verification Methods

1. **Direct HTML scraping** of SWE-bench Verified leaderboard — searched for "Composer" and "Cursor" strings: **NOT FOUND**
2. **Direct HTML scraping** of Scale AI SWE-bench Pro leaderboard — searched for "Composer" and "Cursor" strings: **NOT FOUND**
3. **HN Algolia API** search for "Composer 2.5 SWE-bench" with story tag: **0 hits**
4. **HN Algolia API** search for "SWE-bench Verified Cursor": **1 hit** (unrelated — "Paladin" project)
5. **Full-text search** across all indexed Cursor blog content: **No mention** of "SWE-bench Verified" or "SWE-bench Pro"

---

## Key Findings

### 1. Cursor's Published Benchmarks for Composer 2.5

Cursor exclusively reports three benchmarks:

| Benchmark | Composer 2.5 | Composer 2 | Claude Opus 4.7 | GPT-5.5 |
|-----------|--------------|------------|-----------------|---------|
| SWE-Bench Multilingual | **79.8%** | 73.7% | ~80% | ~80% |
| Terminal-Bench 2.0 | **69.3%** | 61.7% | 69.4% | 82.7% |
| CursorBench v3.1 | **63.2%** | N/A | ~63% | ~63% |

**Source:** Cursor blog post, DataCamp, Lushbinary, The Decoder (all consistent)

### 2. SWE-bench Verified — No C25 Entry

- The official SWE-bench Verified leaderboard at https://www.swebench.com/verified.html does **not** contain any Cursor or Composer entries.
- HTML content search confirmed: `'Composer' in html` → `False`, `'cursor' in html.lower()` → `False`
- Cursor has never submitted C25 results to this leaderboard.

### 3. SWE-bench Pro — No C25 Entry

- SWE-bench Pro is a **separate benchmark** by Scale AI (not part of swebench.com).
- Leaderboard: https://scale.com/leaderboard/swe_bench_pro_public
- GitHub: https://github.com/scaleapi/SWE-bench_Pro-os
- The leaderboard does **not** contain any Cursor or Composer entries.
- HTML content search confirmed: `'Composer' in html` → `False`, `'Cursor' in html` → `False`
- Cursor has never submitted C25 results to this leaderboard.

### 4. Third-Party Trackers Have No Data

- **BenchLM** lists SWE-bench Verified and SWE-bench Pro under Composer 2.5's "Coding" category but shows **0.0/100** scores. The page explicitly states: *"Runtime metrics stay blank until BenchLM has a sourced snapshot."*
- **Vals.ai** shows SWE-bench: **0.0%** (ranked 7/65) — clearly a placeholder indicating no actual evaluation data exists.

### 5. Community Discussion Gap

- **Hacker News:** Zero stories linking Composer 2.5 with SWE-bench Verified or Pro.
- **GitHub:** No issues or discussions in cursor-ai org mentioning these benchmarks.
- This confirms that the community has not noticed or discussed C25 scores on these benchmarks because they don't exist.

---

## Why Cursor Chose SWE-bench Multilingual Instead

Cursor's choice to report SWE-bench **Multilingual** rather than SWE-bench **Verified** is notable:

| Aspect | SWE-bench Verified | SWE-bench Multilingual |
|--------|-------------------|------------------------|
| Instances | 500 | 300 |
| Languages | Python only | 9 languages |
| Creator | OpenAI + SWE-bench team | SWE-bench team |
| Difficulty | Medium | Higher (cross-language) |
| C25 Score | **Not published** | **79.8%** |

Possible reasons for the gap:
1. C25 may perform worse on SWE-bench Verified (Python-only) than on Multilingual
2. Cursor may not have run the evaluation yet
3. Cursor may have chosen Multilingual because it better demonstrates cross-language capabilities
4. SWE-bench Verified requires separate submission/verification process

---

## Comparison Context: MiMo-V2.5-Pro

For reference, MiMo-V2.5-Pro scores:
- **SWE-bench Verified:** 79.1%
- **SWE-bench Pro:** 57.2%

Since C25 has no published scores on these benchmarks, **direct comparison is not possible**.

The only overlapping benchmark is SWE-bench Multilingual, where:
- C25: 79.8%
- MiMo-V2.5-Pro: Not reported in the provided context

---

## Conclusion

**CONFIRMED: Cursor Composer 2.5 has NO published scores on SWE-bench Verified or SWE-bench Pro.**

This is not a data retrieval failure — it is a genuine absence. Cursor has chosen to report only:
1. SWE-bench Multilingual (79.8%)
2. Terminal-Bench 2.0 (69.3%)
3. CursorBench v3.1 (63.2%)

To obtain C25 scores on SWE-bench Verified or SWE-bench Pro, independent evaluation would be required.

---

## Sources

1. Cursor Blog: https://cursor.com/blog/composer-2-5
2. Cursor Evals: https://cursor.com/evals
3. BenchLM: https://benchlm.ai/models/composer-2-5
4. Vals.ai: https://www.vals.ai/models/cursor_composer-2.5
5. SWE-bench Official: https://www.swebench.com/verified.html
6. Scale AI SWE-bench Pro: https://scale.com/leaderboard/swe_bench_pro_public
7. DataCamp: https://www.datacamp.com/blog/composer-2-5
8. The Decoder: https://the-decoder.com/cursors-composer-2-5-matches-opus-4-7-and-gpt-5-5-benchmarks-at-a-fraction-of-the-cost
9. Lushbinary: https://lushbinary.com/blog/cursor-composer-2-5-developer-guide-benchmarks-pricing/
10. HN Algolia API: https://hn.algolia.com/api/v1/search

---

*Research conducted 2026-07-04. All URLs verified accessible at time of research.*
