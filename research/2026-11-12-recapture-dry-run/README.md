# 2026-11-12 re-capture (owner decision O202: move the release cutoff, O65)

Status: **captures, cohort, third-party boards, leaf searches, price-record review and engine fixes are done and committed on `o202-cutoff-move`;
the real build, scenarios, docs, tests and draft-r228 CHECK_OK are NOT done.** The real build stops at the plan-allowance gates (O71/O167), which only
a three-stage search can satisfy, and the fork was told not to run the ladder.

New cutoff instant V' = **2026-11-12T18:00:00Z** (after every AA capture, board read, leaf search and price review of this folder; `regen.sh` pins it).

## Done
- AA: frontier chart (Index v5.0.1, 122 models, `chart-capture.json`), 33 model pages (`aa_v432_snapshot.json`, 2026-11-12T17:28:04Z), Coding Agent Index,
  cost charts (FrontierCode 83, ITBench 45), footnote register/manifests, mapping, reconciliation inventory (`rosterChanges`, `observedIndexVersion`).
- Cohort: 33 configurations (`cohort.json`, `cohort-diff.json`, `roster-diff.json`).
- Boards re-read (O68): Bug Hunt at 269416b7, Vals Vibe Code and Code Migration (updated 2026-11-09), LiveBench 2.0 release 20261106, AI Coding Daily (71 rows),
  Terminal-Bench 4.0; OpenCode Go page re-fetched and re-hashed (`opencode-go/`, unchanged).
- O36/O38: 110 leaf-search entries dated 2026-11-12 (`add_leaf_searches.py`, `leaf-search.md`), seven plain web searches logged with their candidates.
- O167 freshness check logged in `data/plan_cost_routes.json` (`log_freshness_check.py`): changes found for OpenAI, Meta, Anthropic (Fable 5.2).
- O130 SemiAnalysis re-read logged; E213 window set to 2026-10-13..2026-11-12; E216 price-record review (`data/price_records.json`).
- Engine: identity maps, `fetch_livebench` COHORT_MAP, E218 ignores freshness-check entries (needs a unit test for 100% coverage).

## Not done (next steps, in order)
1. Three-stage plan-allowance search (O164/O167) for Meta, OpenAI (December shared limit, Pro statements) and Claude Fable 5.2 on the Claude plans; log it in
   `searchLog` so `check_o71_search`, `check_freshness` and `check_o71_coverage` pass. Real-build error today: "the all-provider search of 2026-11-05 omits Meta (O71)",
   "the freshness check of 2026-11-12 found a Anthropic change with no three-stage search after it (O167)", and uncovered cells Claude Fable 5.2 on Claude Pro / Max 5x / Max 20x.
2. Queued plan reports (douflou #106375, ricardoraposo #97074, smaug42 and sergiokapone #105621/#101937, x2v aiplans 2026-11-04 + artifact) are NOT admitted: the four
   GitHub issues have no byte-exact archive (O165; this session cannot fetch them) and x2v (archived, sha256 512bb066...) needs partition-level transcription together with
   route re-derivation; do both inside step 1.
3. Plan routes for new cohort models by O40/O45/O72, then `VALUERANK_NOW=2026-11-12T18:00:00Z bash research/2026-11-12-recapture/regen.sh`.
4. Add a unit test for the E218 `freshnessCheck` exclusion; full test procedure; docs; pinned clock and test literals; re-pin Bug Hunt consumers if needed.
5. Owner decisions listed in the fork report (LiveBench pin 20261106 vs 20261025 (O139), Index v5.0.1 naming, Gemini 4 Carbon introductory price, GDP.pdf vs `gdpval` leaf).

`DRY-RUN-ranking-diff-NOT-PUBLISHABLE.md` is the per-track before/after from a scratch build with the O71/O167 gates bypassed; it is informational only.
