# Internal review I87 — Claude Opus 5.5 (effort max) on draft r146

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r146`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…compares the chart capture's twins over every field and keys the O103 gate to an instant. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "an instant. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1905): owner decisions O45–O107, editor decisions E247–E270, reviews I29–I86 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` and `docs/refresh-and-release.md`, in full.
- `review-i86-claude-opus-5.5-max.md`, and how the ledger resolved it:
  - M1 became `exclusion` reading only splitting records;
  - L1 became O106 (`combined_note_class`) and chart- and index-level notes in the O103 gate;
  - L2 became `measurement_eligible`;
  - L3 became `check_change_records` and, with O107, `changeKind` and `blocking_change`;
  - L4 became the twin check over the union of fields and the O103 gate keyed to an instant;
  - L5 became the E63, line 55, line 59, `o72Application` and bundle-description texts.
- `draft-r146.md`, every line (1–174), as 20 sequential chunks of at most 16,000 characters covering all 300,411 characters.
- A sentence-level diff of `draft-r145.src.md` against `draft-r146.src.md`. The hand-written changes are:
  - the title;
  - line 55's O104 clause;
  - line 59's lower-of sentence;
  - E183's O103 and O106 sentences (line 116);
  - E18's O107 and derived-flag clauses, and E63's first list (line 152);
  - the r146 history entry.
- The HEAD commit 052b75a diff: `plan_admission.py`, `plan_routes.py`, `value_v3.py`, four test files, the registry, AGENTS.md, the refresh document, the generated documents and the site.
- Code read:
  - `plan_admission.py`, all of it;
  - `plan_routes.py` lines 1–700 and `route_selection`: `blocking_change`, `grade_rank`, `post_change_ranks`, `evidence_grade`, `donor`, `evidence_date`, `expiry_status`, `valuation_status`, `change_flagged`, the same-model and lower-of checks, `report_stage`, `measurement_objects`, `measurement_span`, `in_fault_window`, `report_covers`, `pair_replaces`, `effective_measurement`, `measurement_eligible`, `rebase_lower_of`, `_rebased`, `rebase_transfer`, `route_candidates` and `admission_table`;
  - in `value_v3.py`: `assemble`, `_gated_box`, `classify_footnote`, `chart_footnote`, `NOTE_SURFACES`, `check_surface_notes`, `check_capture_twins`, `check_captured_footnotes`, `page_notes`, `record_notes`, `chart_notes`, `combined_note_class`, `aa_cost_caveat`, `caveat_factor`, `interval_outputs`, `withheld_label`, the manifest rules, `load_documents`, `evidence_bundle`, `configuration`, `build_tracks`, `build` and the CLI;
  - `draft_figures.registry_figures`; `build_scores` where it loads documents and calls `build_tracks`; `swing_bridge`'s method-input handling; `quality.TRACKS`; `site/evidence.py`; `frontier.py`'s gap fields; `build_swe_tracks.select_aicd` and `check_row_date`.
- Data read or queried:
  - `data/scores.json`, both rankings: rows, plan rows and their flags, admission matrices, exchange rates, bar currency, interval bars, rank separability, GDPval movement, cross-source and drift diagnostics, and the manifest;
  - `data/plan_cost_routes.json`: the 137 routes by kind and flag, the typed partition records, the profile rules, the fault days, the change-detection record, the search log and `o72Application`;
  - `data/plan_reports.json`: its schema and listed plans;
  - `data/aa_frontier_capture.json`: the keys of all 190 points and of the 30 list entries;
  - the Coding Agent Index and cost-chart captures (structure and labels);
  - `data/aa/aa_footnote_register.json`;
  - the cost-chart labels in `data/v3_configuration_map.json`;
  - the release dates in `data/aa/aa_v432_snapshot.json`.
- The O71 record:
  - both directories' indexes;
  - the stage-3 run manifest's fallback note;
  - `stage1-anthropic.md` and `stage1-deepseek-minimax.md`;
  - the stage-2 Anthropic notes, Q3 (October changes).

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0 in the repository.
- 1,635 Python tests pass in a scratch clone of HEAD (e2e and js excluded).
- The repository's `git status` was clean before I wrote this file.

**Reproduction.** In the clone at the pinned clock (`VALUERANK_NOW=2026-10-25T09:56:47Z`), these regenerate byte for byte:
- `build_scores`;
- `emit_docs`;
- the site build;
- the figures manifest;
- both scenario files (54 s).

**Probes.** The scripts are in `/tmp/claude-0/-home-user/7939c829-13d8-5c69-90ae-0a2a9460135a/scratchpad/i87/probes/`. Each ran against a second scratch clone or in memory; nothing in the repository changed.

| Probe | Result |
|---|---|
| A: an Anthropic availability record before the 2026-10-17 limit record, with and without a synthetic post-change report pair | the build forces the masked state; O78 and E228 are lost (M1) |
| B0–B1: the published captures, then post-O103 basket captures with every `notes` list empty | unchanged results |
| B2, B3: no `notes` list at the Coding Agent Index level, or on a cost chart | the build stops |
| B4: a registered 2× omission on the record "Codex - GPT-6.1 Sol (max)" | GPT-6.1 Sol (max) becomes an O94 row and a blocker |
| B5: a factorless omission on the FrontierCode cost chart itself | every row on that chart becomes an O94 row over [C, ∞) (Q1) |
| B6: an unregistered note on a Coding Agent Index row | the build stops |
| B7: a post-O103 snapshot with a 3× omission on Gemini 4 Argon's page | Gemini 4 Argon (high) becomes an O94 row in both rankings |
| B8, B9: a 2× omission on a relabelled, or unchanged, FrontierCode chart row | relabelled: silently ignored; unchanged: an O94 row (L4) |
| B10, B11: the registered Haiku sentence recorded beneath the FrontierCode chart, or at the Coding Agent Index level | every row on the surface becomes an O94 row at 5× (L3) |
| C: GPT-6 Astra's ChatGPT Plus measurement unreconcilable, or with divisor 0 | GPT-6 Luna's lower-of transfer takes GPT-6.1 Sol's 10.55 and stays eligible; with both co-donors unreconcilable it keeps Astra and is diagnostic |
| D: a footnote on a frontier entry but not on its point, and the reverse | both stop the build |
| E: a Xiaomi availability record, with and without a hand-set flag on a MiMo ceiling route | without: no flag; with: an E228 blocker (L1) |
| F: two concordant weekly OpenAI reports spanning metering days and an availability record | the cell passes (I86 M1 fixed) |
| O103 boundary | a cost-chart capture at 09:56:47Z on 2026-10-25 passes; one at 09:56:48Z stops |

**Figures recomputed from the underlying data (all match):**
- the frozen bars (53.3 / 63.5 / 64.9 and 38.0 / 49.2 / 58.6) and their setters (Gemini 4 Argon (high) and MiMo-V2.6-Pro at the headline bars);
- the reach counts (7/5/3 and 13/9/5);
- the qualifier counts at the headline bars (4 against 5, and 8 against 9);
- the exchange rates (3.04, 2.44, 2.83, 1.85) and their quality offsets;
- the Plan-row counts:
  - 27 and 51 rows;
  - 2 and 3 fallbacks;
  - 21 and 44 flagged;
  - 3 and 8 in a fault window;
  - 21 and 44 on an unverified basis;
  - 14 (10 + 4) and 30 (26 + 4) on an owner assumption;
- the separability counts (0 of 8, 1 of 15) and the E242 tolerance;
- the cohort (30: 19 + 11, from 13 families: 8 + 5);
- the rendered-frontier Index ties, and the first vertex as the cheapest of the 190 points ($10.63);
- the Coding Agent Index and ITBench-AA coverage (8 of 9 and 3 of 16; 2 of 9 and 0 of 16);
- the GDPval-AA movement (54 of 61 pages, −0.83 to +4.10, and 0.21 z / 0.015 and 0.19 z / 0.014);
- the FrontierCode cross-source figures (τ_b 0.77, 2.6, 11.6);
- the source shares (66/34, 78/22) and the drift flag;
- the leaf weights of both rankings;
- line 55's search stages, providers and unreachable sources, against the search log.

**Not verified:**
- live AA pages and boards;
- the paywalled SemiAnalysis article;
- which date Anthropic's own documentation gives for Claude Haiku 5.5's arrival on the Claude plans (the O71 record dates the launch to 2026-10-07/08 and AA's catalog to 2026-10-07).

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. An earlier model-availability record cancels a later limit or price change's E228 and O78 effects.**

*Where.*
- **The rule.** `plan_admission.check_change_records` (new in r146, lines 95–116) requires each controlled measurement to carry exactly one change date. That date is the earliest typed limit, price or availability record dated on or after the earliest day the measurement can have been taken, and by the cutoff. The route must also carry `changeKind: "availability"` exactly when only availability records fall on that date.
- **What reads it.** `plan_routes.blocking_change` (lines 53–57) returns no change for a route marked availability. Three things read `blocking_change`:
  - the comparator's O78 test (`post_change_ranks`, line 82);
  - the E228 test (`change_flagged`, line 332);
  - every transfer's and O88 route's inherited flag (`route_candidates`, line 644).
- **The draft.** Line 152 (E18) states the same rule: "every controlled measurement on a plan a record covers carries the earliest such record dated on or after the earliest day it can have been taken, and the build stops on a missing or extra flag".

*What goes wrong.*
- Take an availability record that falls between a measurement's earliest possible day and its first limit or price record.
- The build then forces the route's flag to the availability date, marked availability-only.
- The later limit or price change has no E228 effect and gives no report pair O78 precedence.
- The stored fields cannot hold both records, and the build refuses every other state.

*Not a repeat.* I86 L3 proposed one derived date when every flag acted alike. O107, answered afterwards, gave availability flags a different effect, so one date no longer suffices.

*Probes* (real registry at the cutoff):
- The added record is an Anthropic availability record dated 2026-10-01, on the three Claude plans.
- The synthetic pair is a concordant report pair for Claude Opus 5.5 on Claude Max 5x, dated 2026-10-20 and 2026-10-21, after the 2026-10-17 limit change. It is what an admitted cell would supply.

| State | The build's change gates (`check_change_flags`, `check_change_records`) | Max 5x selection, Claude Opus 5.5 (max) and (high), with the pair | E228 blocker without a pair (15 Claude plan rows of both rankings) |
|---|---|---|---|
| As published | passes | the report pair (O78) | yes, all 15 |
| Record added, flags left at 2026-10-17 | stops: "its change flag must be 2026-10-01" | — | — |
| Record added, flags at 2026-10-01 without `changeKind` | stops: "changeKind must be 'availability'" | — | — |
| Record added, flags as the build requires (2026-10-01, availability) | passes | the SemiAnalysis measurement and its O88 route | none |

*Why Medium.*
- **It contradicts O78 and E228 as O107 scopes them.** O107 makes an availability flag label-only. It does not say an availability record cancels a limit or price change. The lifecycle table, E92 and comparator key (2) all give that change its effect.
- **The build forces it, silently.** An editor who records an availability change, as O105 and E18 ask, can only reach the masked state. Every route still prints "possibly superseded", so nothing visible changes.
- **It defeats the case O78 was decided for.** O78 lets a report pair dated after the 2026-10-17 Claude meter change outrank SemiAnalysis's measurement. One earlier availability record on the Claude plans disables that for every Claude plan row in both rankings, and removes their E228 blocker status.
- **The trigger is already in the project's evidence.**
  - E18's scoped detection covers "model-availability matrices", and O105 records such a change with type "availability".
  - The O71 record (stage-2 Anthropic notes, Q3) says: "Haiku 5.5 launched on 2026-10-07/08". AA's catalog dates Claude Haiku 5.5 to 2026-10-07. That is one day after SemiAnalysis's publication and ten days before the limit record.
  - The Claude plans offer Haiku 5.5: the registry holds its Claude Pro and Max transfers.
  - The registry's change-detection outcome is dated 2026-10-26, before O105. The next release's per-release evaluation (E269) would record the launch, and that produces the masked state.
- **It is untested.** `test_change_records_produce_their_route_flags` puts its availability record on another provider. No fixture puts an availability record before a limit or price record on the same plan.
- **It is latent today.** No availability record exists, no report cell passes, and the Plan interval outputs are unevaluable.

*Change.*
- Give each route two dates, derived from the typed records over the same span (on or after the earliest possible day, by the cutoff):
  - a **label date**: the earliest limit, price or availability record, read by `expiry_status`;
  - a **blocking date**: the earliest limit or price record, read by `blocking_change`, and so by E228, O78, O89 and the donor inheritance.
- Restate E18 (line 152) to match.
- Add fixtures for:
  - availability before limit: the label from the first date, E228 and O78 from the second;
  - limit before availability;
  - both on one day.
- Then record the Haiku 5.5 availability change on the Claude plans.

### Low

**L1. Change flags are derived only for controlled measurements. O105 therefore flags no O46 ceiling or report route, and a flag set by hand on one escapes O107.**

- `check_change_records` skips every route that is not a controlled measurement.
  - Transfers and O88 routes inherit their donor's flag, which is right.
  - O46 quota-ceiling routes (no donor) and report routes inherit nothing.
- O105 says an availability change flags "the plan's routes", and draft line 152 repeats it.
- Probe E (the MiMo Token Plan Lite ceiling route; a Xiaomi availability record dated 2026-10-24):
  - **with no route flag**, the build's change gates pass and the route stays "fresh", so O105's label is missing;
  - **with a flag set by hand on the route**, the change gates pass too. `check_change_flags` finds the supporting record, and nothing requires `changeKind` on a non-controlled route. The row then reads "possibly superseded", and `change_flagged` makes it an E228 blocker, contrary to O107.
- Draft line 152's "the build stops on a missing or extra flag" holds only for controlled measurements.
- Change: derive the label and blocking dates for every route kind (M1; recommendation 1), and refuse a stored flag on any route whose flags are derived or inherited.

**L2. O107's exception is written only into E18 (line 152). The governing definitions still give every detected change E228 and O78 effects.**

- **Line 51, comparator key (2):** "a controlled measurement flagged by a detected change dated after it ranks just below a concordant report pair for the same plan whose reports all postdate that change (owner decision O78)".
- **Line 55, the O73 sentence:** "unless a detected change flags it and a concordant report pair for the same model and tier is dated after that change, which then outranks it".
- **Line 135, E92's predicate:** blocker(i) holds for a Plan row "whose selected route a detected change … may have superseded (E228)".
- **Line 159, the E212 table:** "when the trigger is a detected change or the reports (not age alone), the row competes in the Plan interval outputs as a blocker".
- **README's flag legend:** "earns no interval label when the trigger is a detected change rather than age alone (E228)".

Owner precedence resolves the conflict. But E92 and E212 are declared the single governing predicate and table. Line 152's derived-flag sentence also omits "by the cutoff", which the build applies.

Change: write "a detected limit or price change" (or "a detected change other than a model-availability change, O107") in each, and add "by the cutoff" to line 152.

**L3. A chart- or index-level note has no subject, so a registered note about one model makes every row on that surface an O94 row.**

*What happens.*
- `record_notes` adds the Coding Agent Index's own notes to every configuration that has a record.
- `chart_notes` adds a cost chart's own notes to every configuration with a row on it.
- The register is keyed by text alone.
- The one registered omission names a single model: "Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis." It speaks of cost figures across AA, so AA could plausibly print it beside the cost charts or the index too.

*Probes* (post-O103 captures; that sentence recorded beneath the FrontierCode cost chart in B10, or at the Coding Agent Index level in B11):
- The build does not stop, because the text is already registered.
- Every row on the surface becomes an O94 row at 5×:
  - in the max-effort ranking, 8 (B10) or 7 (B11) rows become new O94 rows, so all 8 main-workload rows are blockers;
  - in the AI Coding Daily ranking, 5 (B10) or 3 (B11) rows become new O94 rows.
- Each such row publishes Haiku's sentence as its own "AA cost caveat".
- No main-workload max-effort row can earn an interval label.
- At the next re-freeze no max-effort main-workload row is an eligible reference, so that workload cannot be anchored (E160). The release continues on the frozen anchors (E184).

*Why it matters.* O94's premise is "a row whose AA cost AA itself says omits a pricing term". A sentence about Haiku says nothing about GPT-6.1 Sol's cost. The failure is closed for labels, but the published caveats are false and the re-freeze is blocked.

*Status: latent.* No capture records chart-level notes yet.

*Change.*
- Record on each pricing-omission entry the models it names, or "every row on the surface".
- Apply a chart- or index-level note only to the rows of the models it names.
- Stop the build on a chart- or index-level omission whose subject is not recorded.

**L4. O106 on cost-chart rows relies on hand-kept labels, which no closed-world check covers.**

- `chart_notes` finds a configuration's row by its label in `v3_configuration_map.json`.
- The "configuration map coverage" rule only checks that an entry exists. The O64 manifest closes the Coding Agent Index, not the cost charts.
- Probes B8 and B9 (a registered 2× omission on the FrontierCode cost chart's GPT-6.1 Sol row):
  - with the label unchanged, GPT-6.1 Sol (max) becomes an O94 row and a blocker (B9);
  - with the row relabelled "GPT-6.1 Sol (Max)", the build passes and the row keeps its labels (B8).
- The same miss occurs for a newly charted effort whose map label is null, for example GPT-6 Astra (high) on the FrontierCode chart.
- Since O50 the FrontierCode chart is outside the basket, so no cost check would notice a relabel.
- Low: it needs a relabel and a row-level note together, and a model-level omission usually appears on other surfaces too.
- Change: register cost-chart rows by label, as the O64 manifest does (a cohort configuration's row, or not one, with a reason), and stop on a new, relabelled or vanished row.

**L5. Two side effects of I86 M1 remain.**

*Not a repeat.* The ledger's adoption of I86 M1 changed `exclusion` only. Items (i) and (ii) of that finding were neither adopted nor rejected. The new argument: r146 makes an availability record produce route flags, so these two texts would now contradict the flags printed in the same release.

- **(a) The figure.** `draft_figures.registry_figures` (line 295) sets `evidence.meteringAnnouncements` to every record that does not split. Line 55 prints it after "an announcement that changes only how usage is metered is logged without splitting:". An availability record would therefore be published as a metering-only announcement.
- **(b) The rule text.** Profile rule 10 in the registry, also rendered in `site/data/plans.json`, still says partition records are "each typed limit, price or metering".

Change: one figure per type (a new `evidence.availabilityChanges`), and "limit, price, availability or metering" in rule 10.

**L6. Text that lags r146.**

- **(a) The manifest.**
  - Draft line 152's E63 sentence says the build-stopping gates include "the typed change records behind every flag and split, which must also produce their flags, under O99, O101, O105 and O107, the AA note register with its capture checks under O100, O103 and O106".
  - The build's rule (`value_v3.py` line 2209; `scores.json` `manifest`) still reads "build-stopping evidence gates (O64, O69, O71, O75, O99, O100, O101, O103, O105, E195, E204, E225)". Its detail names neither O106, O107 nor the new reverse check.
  - The rule "AA cost omits a pricing term (O94, O98)" (line 2200) does not cite O106.
- **(b) The O103 date.**
  - The register's rule text (`data/aa/aa_footnote_register.json`) and step 1 of `docs/refresh-and-release.md` say notes are required "from the first capture after 2026-10-28".
  - The build (`O103_AFTER`) and draft line 116 apply the requirement to every capture later than the 2026-10-25 release captures (I86 L4b).
  - So a capture taken from 2026-10-26 to 2026-10-28 is gated, although the procedure says otherwise. A test docstring (`tests/test_value_v3.py` line 2163) carries the old date too.

## 2. Methodology design recommendations

1. **Derive Plan change flags in the build, from one table of record-type effects (M1, L1, L5).**
   - The table lists each type's effects once:
     - limit and price records split, print the label and block;
     - availability records only print the label (O105, O107);
     - metering records are logged (O99, O101).
   - For every route, the build derives a label date and a blocking date from the records that apply to its plan over its measurement span:
     - controlled measurements and O46 ceilings directly;
     - report routes through their reports;
     - transfers and O88 routes through their donors.
   - Remove the stored `changeDetectedOn` and `changeKind` fields, or check them in both directions on every route.
   - The figures (`evidence.partitionSplits`, `evidence.meteringAnnouncements` and a new `evidence.availabilityChanges`) read the same table.
   - A parametrised test runs one record of each type, and each ordering of two types on one plan, through `exclusion`, `evaluate`, the derived flags, `post_change_ranks`, `change_flagged` and the figures.
   - New argument beyond I86's recommendation 1: O107 added a fourth effect (label only), and r146 implemented it as a stored per-route mark that cannot represent two records with different effects.
2. **Give every note in the register a subject and a scope (L3, Q1).**
   - Subject: the models the note names, or "every row on the surface".
   - Scope: either "the model's prices", which reaches every surface, or "one evaluation's execution", which reaches only rows whose C_W includes that evaluation (if the owner chooses (b) in Q1).
   - The build stops on a pricing omission without both fields.
   - Fixtures: B10 and B11's model-named note at chart level, and a chart-wide note.
3. **Close the cost-chart rows as O64 closed the Coding Agent Index (L4).**
   - A reviewed manifest registers each cost-chart row by chart and label, as a cohort configuration's row or not one.
   - A new, relabelled or vanished row stops the refresh.
   - `chart_notes` reads the manifest instead of the configuration map.
4. **Generate the manifest's gate names and the refresh document's O103 scope from the code (L6).** Build the gate list from the gate functions that actually run, and the O103 sentence from `O103_AFTER`, so a new decision updates the published text with the code.

## 3. Questions for the owner

1. **Which AA notes can make a row an O94 row (O106)?**
   - Today a pricing omission on a cost chart whose cost does not enter the ranking's C_W still makes every row on that chart an O94 row. Two such charts exist: FrontierCode, outside the basket since O50, and ITBench-AA while it is pending.
   - Probe B5: one factorless omission recorded on the FrontierCode cost chart itself makes all 9 max-effort rows and 7 of the 16 AI Coding Daily rows O94 rows. Those it reaches without a stated factor compete over [C, ∞). No main-workload max-effort row can then earn an interval label, and the next re-freeze cannot anchor that workload.
   - Which should follow?
     - **(a)** Any registered omission on any surface holding the row, as O106 reads today.
     - **(b)** Model pages, the Intelligence Index chart and notes the register scopes to the model's prices count everywhere. An omission scoped to one evaluation counts only where that evaluation's cost is in the ranking's C_W.
   - The answer decides recommendation 2's scope field.

## 4. Verdict

There are no Critical or High findings. There is one Medium and there are six Lows.

**What holds.**
- The figure check exits 0, and 1,635 Python tests pass.
- A clean rebuild of HEAD reproduces every published data file, document, site page, the figures manifest and both scenario files byte for byte.
- Every current figure I recomputed from the underlying data matches.

**r146 closes I86 as built:**
- **M1:** `exclusion` reads only splitting records. A report on, or spanning, metering or availability records now pools (probe F).
- **L1:**
  - O106's combined class reaches model pages, Coding Agent Index records and the index, and cost-chart rows and charts (B4, B5, B7);
  - the O103 gate stops on a missing chart- or index-level list (B2, B3) and on an unregistered note (B6).
- **L2:** a co-donor the comparator excludes leaves the lower-of minimum. GPT-6 Luna's Plus transfer takes GPT-6.1 Sol's 10.55 when Astra's figure is unreconcilable or not a valid divisor (probe C).
- **L3:**
  - change records now produce the controlled measurements' flags (with M1's gap);
  - an availability-only flag blocks no label and gives no pair precedence.
- **L4:**
  - the twin check covers the union of fields (probe D);
  - the O103 gate stops a capture taken one second after the 2026-10-25 release captures.
- **L5:** E63, lines 55 and 59, `o72Application` and the bundle description are updated.

**The findings:**
- **M1:** each controlled route stores one change date and one kind. So an availability record dated before a limit or price change cancels that change's E228 and O78 effects, and the build forces this state. The O71 record already documents such a record for the Claude plans: the Haiku 5.5 launch on 2026-10-07/08.
- **L1:** flags are derived only for controlled measurements. O46 ceiling and report routes get no O105 flag, and a hand-set one escapes O107.
- **L2:** O107's exception is missing from comparator key (2), the O73 sentence, E92, the E212 table and README's legend.
- **L3:** a chart- or index-level note has no subject, so a note about one model makes every row on the surface an O94 row.
- **L4:** O106 on cost-chart rows depends on map labels that no closed-world check covers.
- **L5:** I86 M1's figure and rule-text side effects remain.
- **L6:** the manifest and the O103 date text lag r146.

Under O56 this round is not clean (one Medium). The Claude Opus 5.5 max rung's clean count stays at zero.

VERDICT: HAS FEEDBACK
