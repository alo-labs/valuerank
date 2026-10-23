# Internal review I52 — Claude Sonnet 5.5 (effort xhigh) on draft r110

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r110".
- Last line of the folded draft: "and settles its ties; ties the search cutoff to the search log and recomputes the O46 ceilings in the build; and brings the AA capture instants under the figures check. Every change is recorded with its rationale in the ledger."
- Last 12 words of its last paragraph (the revision history): "figures check. Every change is recorded with its rationale in the ledger."
- Read in full: `reviewer-prompt.md`, the reviewer brief, the folded draft (977 lines, in chunks to the end), `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (E267, E268 and I51 included), and `AGENTS.md`.
- Code and data opened to check rules and figures: `valuerank/value_v3.py` (`parse_agent_label`, `exact_agent_records`, `check_agent_pins`, `assemble` including the search-log and O46 gates, `check_leaf_searches`, `check_open_web`, `check_source_clocks`, `rank_separability`, `rank_bands`, `sampling_sd`, `evidence_bundle`), `valuerank/draft_figures.py` (lint, `REGISTRY_FACTS`, `registry_problems`, `pointer_problems`), `valuerank/basket.py`, `valuerank/plan_routes.py` (`evidence_date`, `expiry_status`), `research/2026-10-23-swe-benchmarks/build_swe_tracks.py` (`select_aicd`), the tests for these gates, and `data/` (`scores.json`, `figures.json`, `aa/coding_agents_capture.json`, `aa/cost_charts_capture.json`, `v3_configuration_map.json`, `plan_cost_routes.json`, `aa_frontier_capture.json`, `swe_tracks.json`, `leaf_evidence.json`, the AI Coding Daily board capture, the open-web discovery record). I also listed the scheduled tasks to check the SemiAnalysis watch.

Checked and found correct (no finding):

- `python3 -m valuerank.draft_figures check` returns clean; the pytest files for the figure check, the tracks and the E267, E218 and O46 gates pass.
- E267 against the real capture: the 24 Coding Agent Index labels parse as the draft says. Eight of the 29 cohort configurations have an exact record (Sonnet 5.5 max, DeepSeek V4.1 Flash 1017 max, Opus 5.5 max, GPT-6.1 Sol max, Gemini 4 Argon high, GPT-6 Astra max, Haiku 5.5 max, GPT-6 Luna max) and each of the eight is pinned to it; the gate passes on the real data. That reproduces "8 of the max-effort ranking's 9 rows" and "3 of the AI Coding Daily ranking's 15" (DeepSeek, Gemini, Luna). "Codex - DeepSeek V4.1 Flash" (no 1017) and the Devin "+" labels are correctly not exact.
- E268 against the board: 62 captured rows for 61 models; only "Deepseek-V4.1-Flash-1017 (Max)" is listed twice (DeepSeek Harness 18.07 + 18.67 + 15.5 = 52.24 tested 2026-10-18; OpenCode 52.84 tested 2026-10-17). The Bug Hunt record's harness is "DeepSeek Harness / DeepSeek API", so the rule picks 52.24, as the draft and `swe_tracks.json` say. The board's non-bug columns are 20 + 20 + 20 = 60.
- Search log: four entries (2026-10-08, two on 2026-10-21, and the single-provider MiMo entry of 2026-10-22); the cutoff 2026-10-21 passes the gate. O46: the eight ceiling routes recompute to the stored multiples (largest difference 0.00003) and to the figures the draft prints.
- Arithmetic: the cost score and value of all 24 ranked API rows and all 77 Plan rows reproduce from the frozen anchors (0 mismatches); the noise bands, the band straddlers (GPT-6 Astra max; GPT-6.1 Sol medium) and the separability counts reproduce from `valueSd`; the exchange-rate pairs (3.04/4.06 and 2.83/3.77) follow from the anchor ratios; the cohort re-derived from the 189-point capture is 18 frontier + 11 near with the stated gaps, from 12 families (7 and 5); the leaf weights sum to 100 in both rankings (66/34 and 78/22 source split); the ladder positions for n = 9, 15 and 32 and the E215 minimum are right; the stage dates (2026-11-05, 2026-11-06, 2027-01-05, 2027-02-04) follow from 2026-10-06; the weekly SemiAnalysis task is enabled with cron `51 8 * * 1`.
- I found no stale or wrong current figure that a placeholder resolves wrongly. Two quoted AA strings are slightly off (Low L2); that is a gap in the check, not a wrong placeholder.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

**M1. The Coding Agent Index pin gate is one-sided, and the draft's "A pin with no exact record in the current capture is inert" is not what the engine does.**
Where: Cost section, "Cost-source match (E267)" (folded lines 172–176); `value_v3.check_agent_pins` (`if exact and pin not in exact`) and `assemble` (`agent_records.get(labels.get(basket.CODING_AGENT_INDEX))`).
Issue: I51 M1 closed the case "an exact record exists but the pin is empty or names another label". The mirror case is open. When a configuration has no exact record, the gate does not look at the pin at all, and `assemble` prices the row from whatever record the pin names. I ran the gate on the real capture and map with three hypothetical pins: GPT-6.1 Sol (high) pinned to "Codex - GPT-6.1 Sol (max)" (another effort), GPT-6 Luna (high) pinned to the two-model "Devin Fusion CLI - Claude Opus 5.5 Max + GPT-6 Luna High", and Claude Opus 5.5 (high) pinned to "Claude Code - Opus 5.5 (max)". The gate passes all three, and each row would then carry another effort's, or a mixed run's, Coding Agent Index cost into its basket. The draft says such a pin is "inert", so a faithful implementer who reads it literally ignores the pin and scores the row on the subset workload, while the engine as built prices from it. This is exact-variant evidence ("do not transfer benchmark results between reasoning efforts", AGENTS.md; E267's own rule) and a pin is editorial data that the E267 gate exists to police.
Why it hurts: the rule E267 states is not the rule that runs, and the unguarded direction changes a configuration's cost, anchors and value if a pin is ever mis-set. Today no pin is in that state (every pin is an exact record, or names a label the capture does not contain, such as the GPT-6.1 Sol (high) and (medium) pins), so no ranking moves.
Change: make the gate two-sided and say so. For every configuration the pin must be an exact record when one exists; when none exists it must be empty or name a label that is absent from the capture (a pre-registered label that becomes exact if AA publishes it). A pin naming an existing label that is not the configuration's exact record stops the build. Replace the "inert" sentence with that rule, and add a fixture per case (other effort, other model, two-model label, absent label).

**Low**

**L1. The search cutoff's definition and its example disagree, and the gate cannot tell a single-provider search from an all-provider one.** Folded lines 301–306 define the cutoff as "the last date end-user reports were searched", then say the cutoff is the "last all-provider search" (2026-10-21) although the logged MiMo search of 2026-10-22 is also a search of end-user reports. The gate (`searched not in {entry["searchedOn"] …}`) accepts any logged date, and `scope` is free text, so a refresh could set the cutoff to a single-provider entry and publish "reports dated after it were not searched" while other providers were last searched weeks earlier. That defeats E218's stated purpose ("never depends on undiscovered days"). Add a boolean such as `allProviders` to each log entry, require the cutoff to be the date of an entry that has it, and write "the last all-provider search" in the definition.

**L2. Two quoted AA strings differ from the capture, and the check does not compare quoted strings.** Folded line 72 quotes the x-axis as "Cost to Run Intelligence Index (USD)"; `aa_frontier_capture.json` records "Cost to Run Intelligence Index (USD, Log Scale)". Folded line 81 quotes "Total Cost Across the Coding Agent Index"; the capture and `capture_coding_agents.py` record "Total Cost Across the Artificial Analysis Coding Agent Index". Both are hand-typed, so this is a gap in the check, not a wrong placeholder. Quote the stored strings through placeholders (`x_axis`, `costFields.total`) or drop the quotation marks.

**L3. E268 is enforced only in a research script, with no fixture, while the draft says "stops the build".** `select_aicd` lives in `research/2026-10-23-swe-benchmarks/build_swe_tracks.py`, which regenerates `data/swe_tracks.json` by hand. No test calls it (the harness-match, latest-date and tie branches are unexercised), and `npm run verify` cannot notice a stale selection because the board capture is not in the evidence bundle; contrast E206, where "the build checks every matched record against the pinned scoreboard". The heading "A board that lists a configuration twice" is also wider than the rule (AI Coding Daily only), so a duplicate on a Vals or LiveBench board has no stated handling. Say "the extractor stops", add fixtures for the four branches, and either add the board's rows to the bundle with an engine-side re-derivation or state that the selection is attested at extraction.

**L4. O46 gate details are unstated or untidy.** (a) The body says the build "recomputes" the ceilings but not the tolerance the gate uses (0.0005). (b) The Lite tier's `quotaCredits` is stored as 4,099,999,999, not 4,100,000,000, in both Lite routes (Pro and Flash; absorbed by the tolerance, but visible in the route data; the test uses 4,100,000,000). (c) An O46 ceiling's clock is `capturedOn`, an editorial field; Xiaomi's pages are not in the bundle, so "pages re-read" cannot be verified by the build. The draft discloses this for the SemiAnalysis article ("not captured in the evidence bundle") but not for Xiaomi's pages; say so beside the clock rule. (d) E240 asks for "a dated registry addition or a dated rejection", but `check_open_web` requires a reason and no date.

**L5. E267 omits details the parser depends on, and the pin gate covers one of two pinned sources.** The draft does not say that effort appears in two label forms ("(max)" and "({'reasoning_effort': 'max'})"), that the two must agree, or that the comparison is case-sensitive; I checked that "(Max)", "[max]" and "(max, fallback)" labels parse as non-exact without any signal. A new label format would therefore be silently non-exact, which is the I50 H1 failure again. The same map pins ITBench-AA chart rows with no gate (today 2 of 9 and 0 of 15 are right, but ITBench-AA's admission depends on those pins). Also, "the pin records the choice" for several single-model agents has no selection criterion. State the grammar, stop the build on a record whose model part contains a cohort family name but does not parse as exact, and extend the gate to the chart pins.

**L6. Some current-state facts are still hand-typed outside the check's reach.** Folded line 856 says the 2026-10-23 capture's near set "grew by DeepSeek V4.1 Flash 1017 (max) and MiniMax-M3.1-Flash, both new to the chart" (true: the capture's comparison record says so). The sentence has no "today", and a date on the release day does not date it, yet the lint reads effort-qualified names only in "today" sentences. Likewise "today every bar of both rankings keeps its row in all three" (folded line 125) is true (`gapFillBars`) but unchecked. This is the known class of I46 L5; a `capture.nearAdded` figure and a `gapFillBars.survivesAll` figure would remove both.

## 2. Methodology design recommendations

1. Make the Coding Agent Index pin a two-sided, closed check (M1, L5). For each configuration: pin ∈ exact records, or (no exact record and the pin is empty or absent from the capture). Fail on any capture label that contains a cohort family name but does not parse as exact, on a contradictory effort pair, and on a two-model label that names a cohort model. Apply the same check to the ITBench-AA chart pins. This is cheap and removes the I50 H1 / I51 M1 class entirely.
2. Give each search-log entry a machine-readable scope (`allProviders`, `providers[]`) and let only an all-provider entry set the search cutoff (L1). The weekly SemiAnalysis task already shows how a scoped search is described.
3. Move the E268 selection under the same assurance as E206: put the AI Coding Daily board rows in the evidence bundle, re-derive the record and its `alternates` in the engine, and cover the four branches (single row, harness match, latest date, unbreakable tie) with fixtures (L3).
4. Print AA-quoted strings and registry labels from the capture instead of typing them (L2), and add `capture.nearAdded` and `gapFillBars` survival to the figure manifest (L6).
5. For O46, add Xiaomi's tier, fee and rate pages to the bundle (already recorded for the release tidy-up) so that "pages re-read" is a hash change, not a date edit, and store the quota as the page states it (L4).

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: HAS FEEDBACK
