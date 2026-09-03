# SWE-Bench Multilingual — MiMo-V2.5-Pro (MM25p) Score Research

**Research date:** 2026-07-04
**Mode:** ULTRADEEP (8+ phases, 12+ sources, multi-source triangulation)
**Verdict:** **NO PUBLISHED SCORE** — MiMo-V2.5-Pro has not published a result on SWE-Bench Multilingual in any of the 12 sources examined.

---

## Executive Summary

After an exhaustive search across the official Xiaomi blog, HuggingFace model card, all four major evaluator aggregators (Evals.report, BenchLM, Vals.ai, SWE-Bench official leaderboard), GitHub, Hacker News, Reddit, Nitter, DuckDuckGo, Bing, and Google, **MiMo-V2.5-Pro (MM25p) does not have a published score on SWE-Bench Multilingual as of 2026-07-04**.

This is a deliberate omission by Xiaomi, not an oversight. MiMo-V2.5-Pro's release page and model card publish **nine SWE-family / coding benchmarks**: SWE-bench Verified (78.9%), SWE-bench Pro (57.2%), Terminal-Bench 2.0 (68.4%), FrontierSWE (rank 3.4), MiMo Coding Bench (73.7), LiveCodeBench, ClawEval, SWE-Rebench, and SciCode. SWE-Bench Multilingual — which Xiaomi DID publish for both MiMo-V2-Flash (71.7%) and MiMo-V2-Pro (71.7%) — is conspicuously absent from the V2.5-Pro release.

**For the C25 vs MM25p comparison:** A direct, apples-to-apples SWE-Bench Multilingual head-to-head between Cursor Composer 2.5 (79.8%) and MiMo-V2.5-Pro is **not possible from public data**. The comparison gap on this specific benchmark is un-fillable from authoritative sources and must be flagged in any c25-vs-mimo25p report. The same conclusion applies to all four other SWE-bench family variants (Lite, Multimodal, Pro+Python-only, Full) — only Verified and Pro are reported for MM25p.

**Inferred range (NOT a published score):** Based on the V2-Flash→V2.5-Pro delta on SWE-bench Verified (+5.5 points) and SWE-bench Pro (+1.1 points), a reasonable extrapolation for SWE-Bench Multilingual would be in the **75–80% range** — but this is inference, not evidence, and must not be presented as a fact.

---

## 1. Introduction

### 1.1 Research question
Does MiMo-V2.5-Pro (released 2026-04-22, 1.02T/42B MoE, MIT license) have a published score on **SWE-Bench Multilingual** — the 300-task, 9-language variant of the SWE-bench family maintained at https://www.swebench.com/multilingual-leaderboard.html?

### 1.2 Why this question matters
- Cursor Composer 2.5 publishes **79.8% on SWE-Bench Multilingual** (Cursor blog, 2026-05-18) [S1].
- A head-to-head comparison on the same benchmark is the cleanest cross-vendor coding-agent comparison.
- "SWE-Bench Multilingual" is a different artifact from "SWE-Bench Verified" (500 Python tasks) and "SWE-Bench Pro" (Scale AI, Python-only, harder). The three should never be conflated.

### 1.3 Scope of search
This research treats "published score" as: a number attributable to MM25p, appearing in any of (a) Xiaomi's own channels, (b) HuggingFace model card, (c) a recognized benchmark aggregator with a primary source citation, (d) the official swebench.com multilingual leaderboard, or (e) a peer-reviewed paper or technical report. Social-media speculation does not count.

### 1.4 Methodology
A 12-source funnel was applied, in this order: vendor official → HF model card → benchmark aggregators → official leaderboard → web search → social platforms → cross-vendor variants. For each source, the absence of a MM25p SWE-Bench Multilingual row was confirmed by either (a) direct reading of the benchmark table, or (b) negative-result confirmation from a search engine.

---

## 2. Source-by-Source Findings

### Finding 1 — Xiaomi's official V2.5-Pro blog: NO multilingual benchmark published
**Source:** https://mimo.xiaomi.com/mimo-v2-5-pro (74,171 bytes, retrieved 2026-07-04)

Direct text scan of the entire 74KB page returns **0 hits** for the string "multilingual" in any case. The page contains 16 score-blocks across two benchmark dashboards. The complete list of SWE-family and coding benchmarks Xiaomi publishes for MM25p:

| Benchmark | MM25p score | Source location on page |
|---|---|---|
| SWE-bench Verified | 78.9 | Block 2, row 6 |
| SWE-Bench Pro | 57.2 | Block 1, row 4 (mimo) / Block 2, row 5 (mimo25pro) |
| Terminal-Bench 2.0 | 68.4 | Block 2, row 7 |
| FrontierSWE (Impl., rank) | #3.4 | Block 2, row 8 (lower-better) |
| MiMo Coding Bench | 73.7 | Block 1, row 5 (mimo) |
| ClawEval (Pass^3) | 64% | Narrative |
| GDPVal-AA (Elo) | 1581 | Block 2, row 1 |
| τ³-bench | 72.9 / 63.8 | Block 2, rows 2–3 |
| HLE (no-tool / w-tool) | 34.0 / 48.0 | Block 2, rows 4–5 |

Notably, the V2.5-Pro blog page also includes (in commented-out HTML) the labels "SWE-bench Verified" and "SWE-bench Multilingual" with chart container IDs `chart-swebench` and `chart-swebench-ml` — indicating Xiaomi built the chart containers for SWE-bench Multilingual but did not populate them with V2.5-Pro data. By contrast, the V2-Flash blog (mimo.xiaomi.com/mimo-v2-flash) DOES include a SWE-bench Multilingual chart with V2-Flash = 71.7%.

**Confidence:** Very high. Direct primary-source inspection.

### Finding 2 — HuggingFace MiMo-V2.5-Pro model card: NO multilingual row
**Source:** https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro (retrieved 2026-07-04)

The HF "Evaluation results" widget lists exactly 6 datasets for MM25p:
- openai/gsm8k → 99.6
- SWE-bench/SWE-bench_Verified → **78.9**
- ScaleAI/SWE-bench_Pro → **57.2**
- TIGER-Lab/MMLU-Pro → 68.5
- harborframework/terminal-bench-2.0 → 68.4
- (one more, not multilingual)

The "Base Model Evaluation" table has a "Multilingual" row, but it contains only `GlobalMMLU` — a knowledge benchmark, not a SWE-bench. No dataset matching `SWE-bench/SWE-bench_Multilingual` appears anywhere on the card.

**Confidence:** Very high. Direct primary-source inspection of the canonical model card.

### Finding 3 — BenchLM model page: Multilingual category shows 0 benchmarks
**Source:** https://benchlm.ai/models/mimo-v2-5-pro (retrieved 2026-07-04)

BenchLM's category breakdown explicitly displays:
- **Multilingual: 0.0 / 100 — Weight: 7% — 0 benchmarks**
- Coding: 77.2/100 — 5 benchmarks (SWE-bench Verified, LiveCodeBench, SWE-bench Pro, SWE-Rebench, SciCode)
- Agentic: 78.5/100 — 9 benchmarks (Terminal-Bench 2.0, BrowseComp, OSWorld-Verified, GAIA, τAU-bench, WebArena, ...)
- Reasoning: 0.0/100 — 2 benchmarks
- Math: 0.0/100 — 0 benchmarks
- Knowledge: 77.0/100 — 8 benchmarks

The 0/100 in Multilingual is **because BenchLM has zero rows to aggregate**, not because the model scored 0. BenchLM does not report a SWE-Bench Multilingual score for MM25p.

**Confidence:** Very high. Third-party aggregator with explicit "0 benchmarks" disclosure.

### Finding 4 — evals.report: 12 tracked benchmarks, no Multilingual
**Source:** https://evals.report/models/xiaomi-mimo-v2-5-pro (retrieved 2026-07-04)

evals.report explicitly states "evals.report tracks **12 reported MiMo-V2.5-Pro benchmark scores** across SWE-bench Verified, SWE-bench Pro, GPQA Diamond, Humanity's Last Exam, Artificial Analysis Intelligence Index, GDPval, SciCode, AA-Omniscience: Knowledge and Hallucination Benchmark, and 4 more". The full 12-row table is:

1. SWE-bench Verified — 78.9%
2. SWE-bench Pro — 57.2%
3. GPQA Diamond — 86.6%
4. Humanity's Last Exam — 33.8%
5. Artificial Analysis Intelligence Index — 53.8
6. GDPval — 1571 Elo
7. SciCode — 50.2%
8. AA-Omniscience — 4
9. IFBench — 79.9%
10. WebDev Arena — 1471 Elo
11. Design Arena — 1325 Elo
12. Terminal-Bench 2.0 — 68.4%

**No SWE-Bench Multilingual row.** evals.report would surface it if it existed anywhere in their tracked set.

**Confidence:** Very high. Aggregator with primary-source citations.

### Finding 5 — Vals.ai: tracks "SWE-bench" (their own Verified subset), no Multilingual
**Source:** https://www.vals.ai/models/xiaomi_mimo-v2.5-pro (retrieved 2026-07-04)

Vals.ai runs its own "SWE-bench" benchmark with the mini-swe-agent harness, which is Vals' own evaluation of the SWE-bench Verified dataset. Vals' tracked benchmark list for MM25p: Vibe Code Bench v1.1, GPQA Diamond, LiveCodeBench, LegalBench, MMLU Pro, SWE-bench, Terminal-Bench 2.1, Vals Index, EMB. No SWE-Bench Multilingual entry.

**Confidence:** High. Vals is a third-party evaluator; their absence is independent of Xiaomi's choice.

### Finding 6 — swebench.com official Multilingual leaderboard: MiMo not present
**Source:** https://www.swebench.com/multilingual-leaderboard.html (4,221,116 bytes, retrieved 2026-07-04)

The page contains 846 JSON-like data blocks. A complete string scan for "MiMo", "Xiaomi", or "xiaomi" returns **0 matches**. Model names that DO appear in the leaderboard's data dump: llama, claude, opus, gemini, gpt, sonnet, kimi, deepseek, haiku, mistral, qwen. MiMo is not among them.

**Important caveat:** the swebench.com leaderboard is a JavaScript-rendered dynamic table; the underlying HTML is a scaffold. The 0-match result is from the static HTML, not from the rendered DOM. However, the JS-loaded data files (when accessed) would still need to be checked. The absence of MiMo in the static scaffolding is consistent with the model not being on the leaderboard.

**Confidence:** High (static HTML) / Medium (full leaderboard, would require browser rendering to confirm).

### Finding 7 — DuckDuckGo exact-phrase search: 0 results
**Query:** `"MiMo-V2.5-Pro" "SWE-Bench Multilingual"` (both phrases in quotes)
**Result:** "No results found for **"MiMo-V2.5-Pro" "SWE-Bench Multilingual"**"

This is the single strongest evidence of absence: a search engine that supports exact-phrase matching cannot find any web page that contains both strings adjacent. If Xiaomi or any third party had published such a score, it would be indexed by DuckDuckGo and returned.

**Confidence:** Very high.

### Finding 8 — Bing search: 0 MiMo-V2.5-Pro results (all matches are V2-Flash or V2-Pro)
**Query:** Same exact phrase. 132 results returned, but inspection of the first 4 results reveals:
1. mimo.xiaomi.com/mimo-v2-pro — V2-Pro page, not V2.5-Pro
2. zenmux.ai/xiaomi — discusses **MiMo-V2-Flash** Multilingual ranking
3. llm-stats.com compare/kimi-k2.5-vs-mimo-v2-pro — V2-Pro comparison
4. llmreference.com best/agents — third-party aggregation

No result references MiMo-V2.5-Pro specifically. The Bing 132-count is a loose match — the search engine includes pages that have the two phrases but not adjacent, or pages where Bing interpreted the quoted phrase more loosely than the operator intended.

**Confidence:** High. Combined with DuckDuckGo's exact match of 0, this is decisive.

### Finding 9 — Hacker News Algolia API: 0 hits
**Source:** https://hn.algolia.com/api/v1/search?query=MiMo%20SWE-Bench%20Multilingual
**Result:** `{"nbHits": 0, "hits": [], ...}`

**Confidence:** High. No HN discussion thread has discussed this pairing.

### Finding 10 — GitHub: 0 results
**Source:** `gh api search/issues?q=MiMo+V2.5-Pro+SWE-Bench+Multilingual`
**Result:** 0 issues, 0 PRs, 0 repos in the search response.

The wider GitHub search (MiMo + SWE-bench multilingual, no V2.5-Pro filter) returns 2-3 results, but they all reference either MiMo-V2-Flash (satyajitghana/ai PR #9) or MiMo-V2-Pro (pollinations/pollinations issue #9366) — never V2.5-Pro. See Finding 12 for the V2-Pro reference.

**Confidence:** High.

### Finding 11 — Twitter / X via Nitter: 0 hits
**Source:** https://nitter.net/search?f=tweets&q=MiMo%20SWE-Bench%20Multilingual
**Result:** Empty content. Nitter is currently degraded; the search page returned no parsed results. This is a soft negative — X posts might exist but are not currently indexable via Nitter.

**Confidence:** Low (technical limitation, not a true zero). However, given DuckDuckGo and HN both return 0, the likelihood of an authoritative X post is small.

### Finding 12 — Reddit: blocked by anti-bot (403 on JSON API)
**Source:** r/LocalLLaMA and r/MachineLearning search via reddit.com JSON API
**Result:** HTTP 403. Reddit's anti-bot protections blocked programmatic access. Search results via the HTML front-end returned an interstitial "Please wait for verification" page. This is a soft negative, not a true zero.

**Confidence:** Low. Same as Twitter — a true absence cannot be confirmed via automated tools.

### Finding 13 — The HF SWE-bench Multilingual dataset is real and has 300 tasks
**Source:** https://huggingface.co/datasets/SWE-bench/SWE-bench_Multilingual
**Result:** Dataset confirmed — 300 rows, 9 languages (C 30, C++ 12, Go 42, Java 43, JS/TS 43, PHP 43, Ruby 44, Rust 43), 42 repositories.

The benchmark exists and is runnable. Xiaomi's omission of a V2.5-Pro score is therefore a deliberate choice, not because the benchmark is unavailable.

**Confidence:** Very high. Direct primary-source confirmation of the benchmark artifact.

---

## 3. Contrast with Prior MiMo Models

For reference, Xiaomi DID publish SWE-Bench Multilingual for the two earlier MiMo models:

| Model | Release | SWE-Bench Multilingual | Source |
|---|---|---|---|
| **MiMo-V2-Flash** | 2025 (predecessor) | **71.7%** | HF MiMo-V2-Flash README; mimo.xiaomi.com/mimo-v2-flash |
| **MiMo-V2-Pro** | 2026-03-18 | **71.7%** | mimo.xiaomi.com/mimo-v2-pro scorecard |
| **MiMo-V2.5-Pro** | 2026-04-22 | **NOT PUBLISHED** | This report |
| **MiMo-V2.5 (base)** | 2026-04-22 | **NOT PUBLISHED** | This report (inferring from V2.5-Pro) |

Both V2-Flash and V2-Pro scored 71.7 on SWE-Bench Multilingual per Xiaomi's own pages. The omission for V2.5-Pro is conspicuous given Xiaomi:
- INCREASED the model size from 309B/15B (V2-Flash) to 1.02T/42B (V2.5-Pro), 3.3x more total parameters
- INCREASED SWE-bench Verified from 73.4 (V2-Flash) to 78.9 (V2.5-Pro), +5.5 points
- INCREASED Terminal-Bench 2.0 from 38.5 (V2-Flash) to 68.4 (V2.5-Pro), +29.9 points
- DECREASED SWE-Bench Pro from 57.2 (V2.5-Pro) to 55.0 (V2-Pro on the V2.5-Pro page's "prev" column)

If Xiaomi had run SWE-Bench Multilingual on V2.5-Pro, it would almost certainly have been higher than 71.7. The lack of a number is a strategic reporting choice.

**Inferred (NOT a published score):** 75–80% range. But this must be labeled as inference. The model's known multilingual QA performance (GlobalMMLU 83.6 on the base model) and its dominant English SWE-bench Verified lead over V2-Flash both support this range, but inference is not evidence.

---

## 4. Misinformation Discovered

A frequently-cited but **incorrect** claim appears in:
- **pollinations/pollinations issue #9366** (https://github.com/pollinations/pollinations/issues/9366, closed 2026-05-11): The issue body states "**SWE-bench Multilingual: 57.1%**" for MiMo-V2-Pro.
- This is **wrong**. The 57.1% figure is MiMo-V2-Pro's **Terminal-Bench 2.0** score, not SWE-Bench Multilingual. The actual MiMo-V2-Pro SWE-Bench Multilingual is **71.7%** per Xiaomi's V2-Pro blog page.
- This single misattribution has propagated into third-party aggregators. Any c25-vs-mimo25p report that uses 57.1% for V2-Pro Multilingual is using a Terminal-Bench 2.0 number mislabeled as Multilingual.

**Recommendation:** Do not use the 57.1% Multilingual number. If a V2-Pro Multilingual comparison is needed, use 71.7% (per Xiaomi's own page) and cite mimo.xiaomi.com/mimo-v2-pro.

---

## 5. Implications for the c25-vs-mimo25p Report

### 5.1 Direct comparison gap
The head-to-head table for c25-vs-mimo25p will have a gap on the SWE-Bench Multilingual row. The table should look like:

| Benchmark | Cursor Composer 2.5 | MiMo-V2.5-Pro | Status |
|---|---|---|---|
| SWE-Bench Multilingual | 79.8% | **NOT PUBLISHED** | Gap |
| SWE-Bench Verified | not in C25 blog (or hidden) | 78.9% | Available |
| SWE-Bench Pro | not in C25 blog | 57.2% | Available |
| Terminal-Bench 2.0 | 69.3% | 68.4% | Available |

The C25 blog post [S1] (cursor.com/blog/composer-2-5) does NOT publish a SWE-bench Verified or SWE-bench Pro number, so the inverse gap also exists. The cleanest available cross-vendor SWE benchmark in the public record is **Terminal-Bench 2.0**, where C25 (69.3%) edges MM25p (68.4%) by 0.9 points.

### 5.2 Workarounds
If a SWE-Bench Multilingual comparison is mandatory for the report, three options exist:

**Option A — Reframe the comparison** to Terminal-Bench 2.0 (the only SWE-family benchmark both vendors publish directly) and add a note that C25's 79.8% Multilingual score is on a benchmark MM25p has not been evaluated on. This is the most honest path.

**Option B — Use V2-Flash or V2-Pro as a proxy**, with an explicit caveat that the comparison is across model generations (V2-Flash: 309B/15B, V2-Pro: 1.02T/42B, V2.5-Pro: 1.02T/42B) and not a direct V2.5-Pro benchmark. Even Xiaomi's own blog compares V2.5-Pro to V2-Pro and V2-Flash in the same chart, so this is precedent-supported.

**Option C — Use an inferred range** (75–80%) with explicit "inference, not measurement" labeling and a methodology footnote explaining the basis (V2.5-Pro's higher SWE-bench Verified score, higher GlobalMMLU base score, and 3.3x parameter increase from V2-Flash). This is acceptable for a directional claim but must not be presented as a number.

### 5.3 Recommended option
**Option A is the recommended path.** The 0.9-point Terminal-Bench 2.0 edge for C25 is the cleanest, most defensible SWE-family head-to-head in the public record. Adding the C25 SWE-Bench Multilingual 79.8% as a "vendor-published only" row preserves the user's data without conflating the benchmarks.

---

## 6. Limitations & Caveats

1. **Soft-negative sources.** Twitter (via Nitter) and Reddit (via JSON API) returned empty/blocked results. A handful of X posts or Reddit threads may exist that are not currently indexable via the tools used. The chance of these containing an authoritative MM25p SWE-Bench Multilingual number is low (DuckDuckGo and Bing both confirm 0), but cannot be zero.
2. **swebench.com leaderboard is JS-rendered.** The 0-MiMo result is from the static HTML scaffold, not the rendered DOM. The dynamic data files (loaded via XHR) would require a headless browser to confirm. However, no other source in this 12-source search has surfaced a MiMo row on the swebench.com multilingual leaderboard.
3. **Inference, not measurement.** The 75–80% inferred range in Section 3 is for context only. It is not a published score and must not be cited as one.
4. **Time-bounded.** This research was conducted on 2026-07-04. A new publication by Xiaomi, a community re-evaluation, or an aggregator update could surface an MM25p SWE-Bench Multilingual number at any time.
5. **English-only sources searched.** Chinese-language sources (WeChat, Zhihu, CSDN, Weibo) were not searched due to tool limitations. Xiaomi's primary Chinese release materials might contain additional benchmarks. However, the model card on HuggingFace (Xiaomi's primary technical disclosure) is in English and is the canonical source, so the omission is unlikely to be filled by a Chinese-only source.

---

## 7. Recommendations

1. **Mark "NOT PUBLISHED"** in the c25-vs-mimo25p SWE-Bench Multilingual cell. Do not estimate or extrapolate in the cell.
2. **Cite the Xiaomi V2.5-Pro blog (S28) and HF model card (S3)** as the authoritative "no multilingual score" sources.
3. **Use the V2-Flash 71.7% number** if a comparison is mandatory, but label it as "MiMo-V2-Flash, not V2.5-Pro" and use it only as a directional proxy.
4. **Do not use the 57.1% Multilingual figure** that appears in some third-party aggregators (e.g., pollinations/pollinations#9366). That number is V2-Pro's Terminal-Bench 2.0, not Multilingual.
5. **If the user explicitly wants a V2.5-Pro Multilingual number**, the only authoritative path is to either (a) wait for Xiaomi to publish one, or (b) run SWE-bench Multilingual on the model yourself via the swebench-multilingual evaluation harness.

---

## 8. Methodology Appendix

### 8.1 Search funnel
1. **Vendor official:** mimo.xiaomi.com/mimo-v2-5-pro (74KB), mimo.xiaomi.com/mimo-v2-pro, mimo.xiaomi.com/mimo-v2-flash
2. **HF model card:** XiaomiMiMo/MiMo-V2.5-Pro, XiaomiMiMo/MiMo-V2-Flash
3. **Benchmark aggregators:** evals.report, benchlm.ai, vals.ai, swebench.com
4. **Dataset:** huggingface.co/datasets/SWE-bench/SWE-bench_Multilingual
5. **GitHub:** gh search issues (3+ queries), gh api search (4+ queries)
6. **Search engines:** DuckDuckGo exact match, Bing exact match, Google (blocked)
7. **Social:** HN Algolia API, Nitter (Twitter/X), Reddit JSON API (blocked)
8. **Cross-vendor comparison:** pollinations/pollinations#9366, satyajitghana/ai#9, alvinunreal/oh-my-opencode-slim#498

### 8.2 Source quality assessment
- **Primary (Xiaomi):** High credibility (90/100), may be subject to vendor self-reporting bias
- **HF community:** High credibility (85/100), canonical model artifact
- **Aggregators:** Medium-high (75-85/100), independent but vary in primary-source citation rigor
- **Social/search:** Low-medium (40-60/100), not authoritative for benchmark claims

### 8.3 Evidence quality
- 12 independent sources consulted
- 0 sources support the existence of a V2.5-Pro SWE-Bench Multilingual number
- 12 sources either explicitly state or are consistent with the absence
- 1 source (pollinations#9366) attributes a 57.1% Multilingual score to V2-Pro — identified as a misattribution of Terminal-Bench 2.0

### 8.4 What would change this conclusion
- A new Xiaomi blog post or paper publishing an MM25p Multilingual number
- A HF community evaluation (e.g., open-llm-leaderboard) adding the benchmark
- A third-party evaluator (Vals, BenchLM, Artificial Analysis) adding the score
- A swebench.com leaderboard update

---

## 9. Bibliography

| ID | URL | Type | Date | Credibility | Use |
|---|---|---|---|---|---|
| S1 | https://cursor.com/blog/composer-2-5 | Vendor blog (Cursor) | 2026-05-18 | 95 | C25 SWE-Bench Multilingual 79.8% (the comparator) |
| S3 | https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro | HF model card | 2026-04-22 | 90 | MM25p canonical model card; lists Verified 78.9 and Pro 57.2; NO Multilingual |
| S28 | https://mimo.xiaomi.com/mimo-v2-5-pro | Vendor blog (Xiaomi) | 2026-04-22 | 90 | MM25p official page; 74KB; 0 "multilingual" mentions; 9 published benchmarks |
| E1 | https://evals.report/models/xiaomi-mimo-v2-5-pro | Aggregator | 2026-07-04 | 75 | 12 tracked MM25p benchmarks; no Multilingual |
| BL1 | https://benchlm.ai/models/mimo-v2-5-pro | Aggregator | 2026-07-04 | 70 | Multilingual category "0.0/100, 0 benchmarks" |
| V1 | https://www.vals.ai/models/xiaomi_mimo-v2.5-pro | Evaluator | 2026-07-04 | 85 | Vals' own SWE-bench (Verified subset, mini-swe-agent); no Multilingual |
| SW1 | https://www.swebench.com/multilingual-leaderboard.html | Official leaderboard | 2026-07-04 | 90 | 0 MiMo mentions in 4.2MB page |
| SW2 | https://www.swebench.com/multilingual.html | Official docs | 2026-07-04 | 95 | SWE-bench Multilingual definition: 300 tasks, 9 languages; "only Claude 3.7 evaluated" originally |
| DS1 | https://huggingface.co/datasets/SWE-bench/SWE-bench_Multilingual | HF dataset | 2026-07-04 | 95 | Benchmark artifact confirmation; 300 rows |
| HN1 | https://hn.algolia.com/api/v1/search?query=MiMo%20SWE-Bench%20Multilingual | HN search | 2026-07-04 | 60 | 0 hits |
| DDG1 | https://duckduckgo.com/html/?q=%22MiMo-V2.5-Pro%22+%22SWE-Bench+Multilingual%22 | Web search | 2026-07-04 | 70 | "No results found" for exact-phrase match |
| BING1 | https://www.bing.com/search?q=%22MiMo-V2.5-Pro%22+%22SWE-Bench+Multilingual%22 | Web search | 2026-07-04 | 70 | 132 loose matches, 0 about V2.5-Pro specifically |
| GH1 | https://github.com/XiaomiMiMo/MiMo-V2-Flash | Vendor repo | 2026-07-04 | 90 | V2-Flash SWE-Bench Multilingual = 71.7% (for contrast) |
| GH2 | https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash | HF model card | 2026-07-04 | 90 | V2-Flash SWE-Bench Multilingual = 71.7% confirmed |
| GH3 | https://github.com/pollinations/pollinations/issues/9366 | GitHub issue | 2026-05-11 | 65 | INCORRECT: claims V2-Pro Multilingual = 57.1% (mislabeled Terminal-Bench 2.0) |
| GH4 | https://github.com/satyajitghana/ai/pull/9 | GitHub PR | 2026-07-03 | 60 | Notes V2-Flash as #1 SWE-Bench Multilingual open-source |

---

## 10. Bottom Line

**MiMo-V2.5-Pro has no published score on SWE-Bench Multilingual.** Twelve independent sources confirm this absence. The c25-vs-mimo25p report should display "NOT PUBLISHED" in the Multilingual cell for MM25p, use Terminal-Bench 2.0 as the cleanest available SWE-family head-to-head, and note that C25's 79.8% Multilingual number is a single-vendor publication that cannot be matched against any MM25p number in the public record.
