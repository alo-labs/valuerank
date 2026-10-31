# Internal review I54 — Claude Sonnet 5.5 (effort xhigh) on draft r112

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r112`
- Last line of the folded copy: `and narrows E237's version gate to gap fills. Every change is recorded with its rationale in the ledger.` (the closing fragment of the revision-history paragraph that begins "r112 (fifty-third internal review) states the agent-label grammar exactly…").
- Last 12 words of the last paragraph: "gap fills. Every change is recorded with its rationale in the ledger."
- Read in full: `reviewer-prompt.md`, the reviewer brief, the folded draft (984 lines, to the end), `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (the I53 entry included), and `AGENTS.md` (project instructions as supplied).
- Checked against code and data (not only the text):
  - `valuerank/value_v3.py` (`parse_agent_label`, `exact_agent_records`, `agent_record_for`, `check_comparability`, `leaf_supplements`, `frontiercode_cross_source`, `assemble`, `source_clocks`), `valuerank/build_scores.py` (E195/E204/E214/E206 gates), `valuerank/draft_figures.py` (`named_figures`, `lint`), `research/2026-10-23-swe-benchmarks/build_swe_tracks.py` (`select_aicd`).
  - `data/scores.json`, `data/aa/coding_agents_capture.json`, `data/cognition_frontiercode.json`, `data/leaf_evidence.json`, `data/swe_tracks.json`, `data/tb4.json`, `data/plan_cost_routes.json`, `data/v3_frozen*.json`, `data/aa_frontier_capture.json`, `data/v3_configuration_map.json`.
  - `tests/test_value_v3.py`, `tests/test_draft_figures.py`.
  - Ran `python3 -m valuerank.draft_figures check` (exit 0) and `pytest tests/test_value_v3.py tests/test_draft_figures.py` (pass). I wrote no file other than this review.
- Verified from the I53 round: the exact two-form label ("Codex - GPT-6 Luna (max) ({'reasoning_effort': 'max'})") reads as GPT-6 Luna at max, and every real label in the capture reads as the draft's grammar says; the FrontierCode join on family and effort gives a 22-row panel (29 cohort configurations less the 7 with only one side), τ_b 0.7662, mean offset 2.60, largest 11.60, identical in both rankings (E260); `excluded.missingCore` is true for all nine excluded rows (each lacks every added leaf of both rankings; MiMo-V2.6-Flash and MiniMax-M3.1-Flash also lack Bug Hunt Bench); E237's narrowing matches `SUPPLEMENT_VERSIONS`. The one I53 item that does not match its description is the unreadable-label build stop (M1 below).
- Spot-checked and found right: the arithmetic fixtures (admission enumeration, bar ladder positions, E201b, E210, Clopper–Pearson endpoints), the SemiAnalysis stage dates, the 31-date report window, the 66/34 and 78/22 source shares, the 3.8 and 5.9 noise margins against the 2.84 and 4.45 thresholds (margin ≈ threshold ÷ 0.75), the exchange-rate series, the bands' straddlers (GPT-6 Astra (max); GPT-6.1 Sol (medium)), the 14 of 27 and 48 of 50 assumption rows, the nine excluded rows, the source clocks (O59/O60), and the capture comparison (near set 9 to 11).

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

**M1. The unreadable-label build stop (E267) is implemented for one case only, so the draft's "never silently dropped" is not true.**

- Issue. The draft says: "A single-model label for a cohort configuration's model that this grammar cannot read stops the build, so a new AA label form is read, never silently dropped." In `agent_record_for` (`valuerank/value_v3.py` lines 633–652) the stop fires only when `parse_agent_label(label) is None` **and** the part after " - " starts with `<model> (`. `parse_agent_label` returns `None` for exactly three inputs: no " - ", a " + " (excluded by the filter), and two effort forms that disagree. So the only single-model label that can stop the build is a disagreeing pair; this is the one fixture (`tests/test_value_v3.py` lines 1825 and 1840–1841). Every other form the grammar cannot read parses to a non-`None` dict whose `model` field carries the unread tail, fails `parsed["model"] in names`, and is dropped with no error. I ran `agent_record_for` for GPT-6 Luna (max) on these labels:

  | Label | Exact? | Build stops? |
  |---|---|---|
  | `Codex - GPT-6 Luna (max) ({'reasoning_effort': 'low'})` | no | **yes** (the only covered case) |
  | `Codex - GPT-6 Luna (x-high)` | no | no |
  | `Codex - GPT-6 Luna (max) (Preview)` (read as effort "Preview") | no | no |
  | `Codex - GPT-6 Luna (max) ({'reasoning_effort': 'max', 'subagents': True})` | no | no |
  | `Codex - GPT-6 Luna ({'reasoning_effort': 'max'}) (max)` (forms in the other order) | no | no |
  | `Codex - GPT-6 Luna (Max)` / trailing space / `GPT-6 Luna max` | no | no |

  AA already prints a non-effort keyed form for another agent in the very capture the build reads (`Claude Code - Step 5 Preview ({'subagents': True})`, `data/aa/coding_agents_capture.json`), so "a new keyed setting on a cohort model" is the realistic next label, not a contrived one.
- Why it matters. This is the fifth round on the Coding Agent Index link (I50 H1, I51 M1, I52 M1, I53 M1, now this), and the draft and the I53 ledger entry both state that the class is closed ("at the source of this four-round class … now stops the build"). It is not: a cohort row whose only record changes form silently loses its exact record, moves to the subset workload (flagged "subset cost", O17) and can reorder the ranking, which is what I50 H1 did to the max-effort API leader. The draft also uses two outcomes for one input without saying which governs: "a disagreeing pair is not exact" (E267) while the code, and the test comment ("a disagreeing pair is unreadable, not skipped"), stop the build on it. Two faithful implementers reading the sentence get different gates, and neither gets the gate the code has.
- Change. State "unreadable" mechanically and implement that sentence: for each cohort model name N (with and without "Claude "), a single-model label whose model part begins with `N (` and that does not read back as exactly N plus the grammar's optional parts stops the build, whether the cause is an unknown parenthesised token, a keyed setting other than `reasoning_effort`, a different order, a case or whitespace difference, or disagreeing effort forms; a label that reads as N at another effort stays a silent non-exact record (it is another configuration's). In code: replace the `parse_agent_label(label) is None` test by `parsed is None or parsed["model"] not in names`; add one fixture per row of the table above. Say in the draft that a disagreeing pair stops the build (not only "is not exact"). Alternatively adopt a closed registry of label shapes with a build stop on any new shape, as E225 does for tbench.ai agents; that removes the predicate and makes "new AA label form" a registry update.

**Low**

**L1. The E189 sentence and its figure describe the API subset stratum only; the Plan basis has a 4-row, one-configuration subset stratum that reads "defined".**

`draft_figures.py` line 210 reads `costInfluence["api"]` only. In `data/scores.json`, `v3.costInfluence.plan.subsetStrata["1453a9a0576b02ea"]` is MiMo-V2.6-Pro's four plan rows with `status: "defined"`, `qualityFlag: true` (quality SD 0), cost share 1.0 and `varianceAllocation` {cost 1.0, quality 0.0}. The sentence says the allocation is "withheld below three rows, where the split is fixed by construction", but this four-row stratum also has a split fixed by construction (one configuration, one quality) and the draft publishes it. The sentence is not false, but it gives the reader no sign that a Plan stratum exists or that its allocation is degenerate. Recommend: render both bases' strata (`{{fig:subsetStrata}}` per basis), and either withhold the allocation when the panel holds fewer than two distinct configurations (E258's reasoning) or say that a one-configuration panel publishes 100%/0% by construction.

**L2. E237's gate does not reach Terminal-Bench provider claims.**

The draft says that for a gap fill (Bug Hunt, FrontierCode, Terminal-Bench) "a missing or different version, or no metric, stops the build". `leaf_supplements` (value_v3.py lines 144–164) calls `check_comparability` on `leafEvidence.supplements` only; the `tb4.json` provider claims are appended afterwards (lines 157–160) and never checked. The one eligible claim there (`deepseek-v41-flash-terminal-bench-40-20260910`) carries `benchmarkVersion: "4.0"`, which would fail the gate's required string "Terminal-Bench 4.0", and its `cohortModelId` is `deepseek-v4-flash`, a catalog model outside the cohort, so nothing is scored on it today. Latent only. Recommend running `check_comparability` on those claims too (with a version-string normalisation), or saying in E237 that the TB provider-claim path is exempt until used.

**L3. The I53 M3 fix (FrontierCode join on family and effort) has no regression fixture.**

`frontiercode_cross_source` is exercised by no unit test: the build fixture feeds an empty Cognition board (`tests/test_value_v3.py` line 620), and `test_draft_figures.py` only reads the rendered figure. The figure check cannot catch a relapse, because it renders whatever `scores.json` holds (7 rows would render as "7 configurations"). Recommend a fixture with two efforts of one family, a fallback-qualified row, and a family absent from the board, asserting the panel and the excluded list; the draft's own convention is that each rule keeps a fixture.

**L4. The search cutoff rests on a hand-set mark that the gate cannot check.**

E218 and `assemble` define the search cutoff as the latest search not marked `singleProvider`, described as "the routine search over every provider whose ranked Plan rows rest on end-user reports or an O46 ceiling". The 2026-10-21 log holds two unmarked entries, each with a narrower scope than "every provider" (xAI, Google, Z.AI, Kimi, MiMo in the first; DeepSeek, Qwen, Meta Muse "follow-up" in the second), so the rule as worded would require the mark on each. Only the pair jointly covers the providers, and a future unmarked entry for one provider would move the cutoff. Recommend recording a `providers` list per entry and having the gate require that the unmarked entries on the cutoff date together cover the providers with ranked end-user or O46 Plan rows (today Google, DeepSeek and Xiaomi, plus MiniMax once it has a ranked row), or define "search" as the set of entries sharing the cutoff date.

**L5. The hand-written clauses beside `{{fig:excluded.missingCore}}` are not tied to it.**

"the other excluded configurations lack the added leaves of both rankings" and the parentheticals about MiMo-V2.6-Flash and MiniMax-M3.1-Flash are true today (I checked all nine excluded rows) but are typed beside a generated figure, so a different grouping would leave them wrong with the check passing. The generator already has the data (`incompleteEvidence[].missing` in both rankings): render the second clause from it, or note the parentheticals as reasons for a specific missing pair.

## 2. Methodology design recommendations

Prioritised.

1. **Make the Coding Agent Index record a total classification, then print it (closes the class behind I50–I54).**
   - Classify every single-model Coding Agent Index label whose model part begins with a cohort model name as exact, other-effort, other-setting (a keyed setting that is not `reasoning_effort`) or unreadable. Unreadable stops the build (M1); other-setting also stops on first sight until a dated registry decision places the setting, as E225 does for tbench.ai agents.
   - Print the classification table with the cohort (e.g. `rows[].cost.codingAgent` = {label, class} plus a list of non-exact labels per model), so a reader and the figures check can see which label priced each row and why a nearby label did not. Today the draft's "none today" for pins is an unsupported hand-written fact; the table would let it be a placeholder.
2. **Guard every engine fix a review has asked for with a fixture, and let the figures check assert the intent, not only the rendering.** Add the cross-source join fixture (L3). Add a check that a rendered panel count equals the number derived independently from the cohort (29 less rows lacking either source), so a regression to the effort-qualified key fails loudly instead of re-rendering a smaller number.
3. **Render per-basis anchors of the "undefined/degenerate" statuses.** The subset-stratum figure should list both bases (L1); the E180 minimum-panel table should state the rule for panels made of one configuration's plan rows, which is where Plan statistics go degenerate (cost share 100%, quality share 0%).
4. **Close the comparability gate for provider claims (L2)** so that E237 reads the same on every fill path, and give the Terminal-Bench claim a normalised version field.
5. **Provider coverage in the search log (L4).** A `providers` list per entry and a coverage check make "all-provider search" a verifiable property, which matters more once MiniMax gains a ranked Plan row.

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: HAS FEEDBACK
