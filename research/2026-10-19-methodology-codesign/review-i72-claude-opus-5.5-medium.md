# Internal review I72 — Claude Opus 5.5 (effort medium) on draft r131

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r131`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r131 (seventy-first internal review, the first clean one at Opus 5.5 medium) registers the three owner-assumption kinds once in the build and generates every enumeration and count of them. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "of them. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`.
- `ledger.md` from "## Internal review I28" to the end. This covers O45–O88, E247–E270, I29–I71 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` in full.
- `review-i71-claude-opus-5.5-medium.md`.
- `draft-r131.md`, every line (1–174). I read it as a line-tagged copy folded at 3,000 characters (228 segments), in 15 sequential chunks.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- These tests pass, run with bytecode and the pytest cache off:
  - `tests/test_plan_reports_provenance.py`
  - `test_plan_admission.py`
  - `test_plan_routes.py`
  - `test_draft_figures.py`
  - `test_swe_tracks_selection.py`
  - `test_value_v3.py`
- `git status` was clean before I wrote this file. HEAD is ac51b6e.

**Plan rows** (`planRows` in `data/scores.json`)
- Max-effort ranking, 27 rows: 10 owner-named transfers, 4 O46 ceilings, 11 controlled measurements (Opus 5.5, GPT-6.1 Sol and GPT-6 Astra at max) and 2 API fallbacks.
- AI Coding Daily ranking, 51 rows: 26 transfers, 18 O88 rows, 4 ceilings and 3 fallbacks. It has no controlled row, so its measured-only view is empty.
- 21 and 44 rows carry "possibly-superseded", and 21 and 44 carry "valuation basis unverified". These match Output 1, line 15 and the limitations.
- Each row carries `assumptionKind`. `_plan_evidence` now returns the kind's name.
- `plan_routes.OWNER_ASSUMPTIONS` registers the three kinds (I71 L1). E166 and E168 list the O88 amount and the ceiling derivation (I71 L4). Line 59 gives Opus 5.5's other efforts O88 (I71 L2), as do `claudeApplication`/`gptApplication`. E106 case (2) admits all three kinds (I71 L3).
- The O88 multiples check out:
  - GPT-6.1 Sol's other efforts take Plus 10.55.
  - GPT-6 Astra (high) takes Plus 8.1, Pro 100 13.22, Pro 200 14.485 and Pro 500 13.91.
  - GPT-6 Luna takes the lower-of values: 8.1, 10.55, 10.42 and 10.772.

**Separability** (`diagnostics.rankSeparability`)
- 0 of 8 and 1 of 15 API pairs separate, and 2 of 10 and 1 of 19 Plan pairs.
- 16 and 31 pairs are same-configuration pairs.
- The AI Coding Daily n = 60 reading gives 3.25 and 3.21.
- The E242 tolerance reproduces from the exchange rates: 2^(2.76/2.44) = 2.19 and 2^(4.41/1.85) ≈ 5.2.
- The max-effort API exchange rate is 3.04, from anchors 62.86 / 18,703.4 USD: 25·ln2/ln(297.5). The quality offset is 4.06.

**Bars and admission**
- Bars are 53.27 / 63.54 / 64.94 over 9 rows and 38.00 / 49.24 / 58.61 over 16. The reach counts 7/5/3 and 13/9/5 match ladder positions 2/4/6 and 3/7/11.
- The admission alternatives 255 and 127 are consistent with 2⁸ − 1 and 2⁷ − 1: ITBench-AA covers 2 of 9 rows, and the Coding Agent Index 3 of 16.
- The FrontierCode fill effect at the 21% weight checks: 0.21 × 2.6 ≈ 0.55 and 0.21 × 11.6 ≈ 2.44.
- The Omniscience test vectors recompute.

**Report cells and research record**
- `planAllowanceCells` holds 52 cells, 28 of them listed; none passes. Google AI Pro / Gemini 4 Argon fails at 1.35× under O86.
- `data/plan_reports.json` has 107 rows and 93 `notTabulated` entries. Both O71 research directories exist with their stage records.
- The O69 disclosure (`cutoffDayRow`, bounded to before 01:14:11Z) and `sourceClocks` match the draft.

**Scenario files and published documents**
- `data/v3_scenarios*.json`: the transfers-off strata exclude 10 (max-effort) and 48 (AI Coding Daily) Plan rows. This matches the build's `transfer_dependent` (every grade "assumption").
- `methodology.md`, `README.md`, `scores.md`, `valuerank/emit_docs.py` and `valuerank/value_v3.py`: I grepped them for the residual assumption enumerations.

**Not verified:** live web pages, the paywalled SemiAnalysis article and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. The r131 registry did not reach several enumerations in the draft. They still name "owner-named transfer" (sometimes with fallbacks) where the governing set is all three owner-assumption kinds.**

r131 says it "generates every enumeration and count" of the kinds. The counted sentences (lines 13, 15 and 16, E106, E167, E164's provenance list) now do. These remain:

1. **Line 55 (change detection).** The Claude half was fixed: "owner-named transfers and O88 same-model assumptions, E144". The GPT half still says "the SemiAnalysis GPT routes and the transfers from them are possibly superseded from 2026-10-11". The 12 O88 GPT rows are flagged by the same change: GPT-6.1 Sol (high) and (medium), and GPT-6 Astra (high), 4 plans each.
   - *What is new:* I71 L1 named line 55, and the ledger records it adopted, but only one of its two sentences was changed.
2. **Line 60 (MiMo).** It still says "The build counts its rows with the owner-named transfers among the Plan rows resting on an owner assumption (marked †, E242)". It omits the O88 rows.
   - *What is new:* I71 L1 named this line too, and it is unchanged.
3. **Line 59, comparator key (2).** "controlled measurement of the exact model > ≥ 2 concordant end-user reports > owner-named transfer (assumption)". O88 routes and O46 ceilings are graded "assumption" (`plan_routes.evidence_grade`), but the key does not place them.
4. **Line 68 (O73).** "replace only an assumption-based or fallback route (the O40 and O45 shared multiples, the O46 ceilings, API fallback)" omits the O88 routes. They are assumption-based, and the comparator ranks reports above them (see L3).
5. **Line 76 (E164 opening).** "the official Plan anchors include owner-named transfers and API-cost fallbacks (E160)". Line 83 (E160, then E184) says twice "measured routes, owner-named transfers and API-cost fallbacks alike".
   - The AI Coding Daily Plan anchor references are every plan row of its 16 configurations. That includes 18 O88 rows and 4 ceiling rows.
   - The rule ("every plan row of the same configurations") is right; only the enumeration is incomplete.
6. **Line 76 (E113 admission).** It says "no owner-named transfers". The build excludes every assumption grade (`MEASURED_GRADES`).
7. **Line 98 (E167).** It names the transfers-off streams "S1 core, S2 core and S1M". Line 125 and the build also run S1T with transfers off, and scores.md lists "S1, S2, S1 endpoint-heavy, S1M and S1T".

*Why Low:* the sets the build uses are right, and no score, flag or stream membership is wrong. Only the descriptive lists are.

*Change:*
- Render items 1–6 from `plan_routes.assumption_kinds_text()` via a figure, as r131 did for line 15. Alternatively, replace "owner-named transfers" with the defined term "owner assumptions".
- Add S1T to line 98's list.
- To close the class at its source, add a `draft_figures` lint. Outside the history and the O4/O7/E144 definitions, the bare phrase "owner-named transfer(s)" would then be allowed only in a sentence that also names the other two kinds, or carries the kinds figure.

**L2. Published outputs still label O88 and ceiling rows as owner-named transfers.**

- **The scenario files.** `value_v3.TRANSFER_EXCLUSION` is the single reason string for every row excluded in the transfers-off strata: "owner-named transfer: unevaluable with transfers off …". In `data/v3_scenarios_aicd.json`, 22 of the 48 excluded rows get it in each of the five off strata. 18 are O88 rows, among them Claude Opus 5.5 (high) on all three Claude plans, the top Plan rows of that ranking. The other 4 are MiMo ceiling rows. Their own `planRows` flags say otherwise. E167 promises the row is "listed with its reason".
- **methodology.md, line 181.** It says the core streams "run with owner-named transfers off (E167): a row whose selected route is a transfer is unevaluable there". scores.md lines 367 and 966 say it correctly ("owner assumptions off (owner-named transfers, O88 … and O46 …)").
- **methodology.md, line 108, and scores.json `anchorPolicy.planRule`** (`value_v3.py` line 1137). Both print "measured routes, owner-named transfers and API-cost fallbacks alike".
- **The separability `bias` string** (`value_v3.py` line 2713) and methodology.md line 181. Both say "owner-named transfer error on the Plan basis", although README and scores.md now count all three kinds there.

*What is new:* I71 looked at the README, scores.md and the † legend, which r131 fixed. These are generated outputs the r131 sweep did not reach.

*Why Low:* the exclusions themselves are correct (`transfer_dependent` tests the grade). Only the reason text and the descriptions are wrong.

*Change:*
- Make the exclusion reason `f"{OWNER_ASSUMPTIONS[kind][0]}: unevaluable with owner assumptions off (…)"` per row.
- Generate the three methodology.md / planRule / bias strings from `assumption_kinds_text()`.
- Add a test that every excluded row's reason names that row's `assumptionKind`.

**L3. O73 and O88/O87 combine into an effort-dependent precedence. That contradicts O87's premise. It is latent today.**

Under O87, report cells are keyed by model, so one passing cell supports a report route for every configuration of that model. Under O73 the outcome then splits by effort:

- **GPT-6.1 Sol (max):** its SemiAnalysis route is a controlled measurement of the exact model, so it keeps precedence over the reports.
- **GPT-6.1 Sol (high), (medium), etc.:** the O88 route rests on the same SemiAnalysis figure but is graded "assumption" (`evidence_grade`). The comparator therefore ranks the report pair above it.

One model on one plan would then carry two different multiples from two different evidence sources, chosen by effort. That is the opposite of O87/O88's stated premise that "a plan allowance is the same dollars at any reasoning effort".

Today nothing changes:
- No cell passes.
- Every SemiAnalysis route is flagged by a detected change (O77, O79).
- O83's splits leave only post-change reports in the current partition.
- So under O78 a passing pair would outrank both routes alike.

The asymmetry appears only for a controlled measurement that is not flagged, for example a new or re-selected SemiAnalysis analysis.

*Why Low:* latent. No output differs, and it follows from the literal combination of owner decisions.

*Change:* state the intended outcome in line 68 and in the comparator, after the owner question below. One option is that an O88 route takes its donor's precedence against report evidence for the same model and plan. Grading for every other purpose (labels, †, transfers-off) would be unchanged.

## 2. Methodology design recommendations

1. **Close the assumption-kind class at the source (L1, L2).** r131 registered the kinds but left a lint gap. Two additions would make a fourth kind, or a renamed one, unable to leave a stale list:
   - A `draft_figures` rule that flags "owner-named transfer(s)" used as a set term.
   - A unit test that every generated reason, rule and bias string naming an assumption set is built from `OWNER_ASSUMPTIONS`.
2. **One precedence statement per evidence relation (L3).** Publish beside the comparator a small table: "evidence A vs evidence B for the same model and plan → winner". Its rows would be controlled vs reports, O88 vs reports, transfer vs reports, ceiling vs reports, and each with and without a detected change. Generate it from `grade_rank`/`post_change_ranks` with fixtures. The O73/O78/O88 interplay is then visible and testable, rather than inferred from three decisions.
3. **The direction of the ceiling's error (optional, disclosure only).** An O46 ceiling is an upper bound on the usable multiple, since it assumes full use. Its error is one-sided, unlike a transfer's. The E242 tolerance could say that for ceiling rows only overstatement is possible, so the † band's tolerance bounds a one-directional error. No score change.

## 3. Questions for the owner

1. **(L3) The report-precedence asymmetry.** When two concordant user reports for a model and plan pass, should they replace only the configurations whose route is an O88 same-model assumption, while the max configuration keeps the exact SemiAnalysis measurement (the literal O73 + O88)? Or should an O88 route share its donor's precedence, so that every effort of the model keeps the same evidence source and multiple, as O87's effort-invariance premise implies? The answer changes the comparator's grade for O88 routes against report evidence, and line 68's wording.

## 4. Verdict

There are no Critical, High or Medium findings, and three Lows. The figure check exits 0 and the listed tests pass.

r131 fixed I71's four Lows at their main sites:
- one registry of the three owner-assumption kinds;
- counts by kind in lines 13, 15 and 16, E167 and E106;
- Opus 5.5's other efforts under O88 in line 59 and the registry;
- the O88 amount type in E166 and E168.

The remaining Lows are enumerations the sweep missed, in the draft (L1) and in generated outputs (L2), plus one latent precedence question arising from owner decisions O73 and O88 (L3). None changes a multiple, score, flag, stream membership or rank.

Under O56 this round is clean, the second consecutive clean round at the Claude Opus 5.5 medium rung (after I71).

VERDICT: HAS FEEDBACK
