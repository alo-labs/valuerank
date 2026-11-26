# Internal review I86 — Claude Opus 5.5 (effort max) on draft r145

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r145`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…checks the chart capture's duplicate entries against each other, and replays the footnote register as a method input. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "method input. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1892): owner decisions O45–O105, editor decisions E247–E270, reviews I29–I85 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` and `docs/refresh-and-release.md`, in full.
- `review-i85-claude-opus-5.5-max.md`, and how the ledger resolved it:
  - L1 became O105 (availability records flag without splitting);
  - L2 became `check_surface_notes`, the refresh-document capture step and the swing bridge's method input;
  - L3 became `check_capture_twins`;
  - L4 became the E63, manifest and register texts;
  - L5 became O104.
- `draft-r145.md`, every line (1–174), as 24 sequential chunks of about 16,000 characters covering all 298,990 characters.
- A sentence-level diff of `draft-r144.src.md` against `draft-r145.src.md`. The hand-written changes are:
  - the title;
  - line 55's O83/O105 clause and its O104 clause;
  - line 59's O104 parenthesis;
  - E183's O103 and twin sentences (line 116);
  - E18's typed-record parenthesis and E63's second list (line 152);
  - the r145 history entry.
- The HEAD commit 0fdd675 diff: `plan_admission.py`, `plan_routes.py`, `swing_bridge.py`, `value_v3.py`, five test files, the registry, the register and the generated documents.
- Code read:
  - `plan_admission.py`, all of it;
  - in `plan_routes.py` (lines 35–830): the grade keys, `evidence_grade`, `donor`, `evidence_date`, `expiry_status`, `change_flagged`, the same-model and lower-of checks, `measurement_objects`, `measurement_span`, `in_fault_window`, `report_covers`, `pair_replaces`, `effective_measurement`, `rebase_lower_of`, `_rebased`, `rebase_transfer`, `route_candidates` and the comparator;
  - `swing_bridge.py`, all of it;
  - in `value_v3.py`: `assemble` (lines 776–940), `classify_footnote`, `chart_footnote`, `check_surface_notes`, `check_capture_twins`, `check_captured_footnotes`, `aa_cost_caveat`, `configuration`, `load_documents`, `evidence_bundle` and the CLI;
  - in `build_scores.py`: `plotted_name_state`, `check_rendered_path`, `near_frontier_selection` and the `build_tracks` call;
  - in `draft_figures.py`: `registry_figures`, `check` and `main`;
  - the three AA capture scripts, for note handling;
  - the task counts in `basket.py` and `value_v3.SAMPLING_TASKS`.
- Data read or queried:
  - `data/scores.json`, both rankings: rows, displayed quality, interval bars, manifest, scenario status, `planAllowanceCells` and the evidence bundle;
  - the bar references in `data/v3_frozen*.json`;
  - `data/aa_frontier_capture.json`: the keys of all 190 points and of the 30 list entries, and every footnote;
  - `data/aa/aa_footnote_register.json`;
  - the three AA capture files: top-level fields and row shapes;
  - `data/plan_cost_routes.json`: 137 routes by provider, kind and flag, `partitionSplits`, `accountingFaultDays`, the profile rules, `changeDetection`, the search log and `o72Application`;
  - `data/plan_reports.json`: every OpenAI report's date, unit, window and flags;
  - `data/v3_scenarios*.json`;
  - the two O71 record directories, checked against the 2026-10-25 search-log entry.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0 in the repository.
- 1,631 Python tests pass in a scratch clone of HEAD (e2e and js excluded).
- The repository's `git status` was clean before I wrote this file.

**Reproduction.** In the clone at the pinned clock (`VALUERANK_NOW=2026-10-25T09:56:47Z`), these regenerate byte for byte:
- `build_scores`;
- `emit_docs`;
- the site build;
- the figures manifest;
- both scenario files (53 s).

**Probes** (scripts in `/tmp/claude-0/-home-user/7939c829-13d8-5c69-90ae-0a2a9460135a/scratchpad/i86/probes/`, run against the clone or in memory; nothing in the repository changed):

| Probe | Result |
|---|---|
| O104 on the real registry: release day 2027-02-10, both ChatGPT Plus measurements demoted, a synthetic GPT-6.1 Sol pair at 11.25, at 6.24, or none | GPT-6 Luna's lower-of transfer follows the pair at both 11.25 and 6.24, and has no Plus route without a pair. This is what O104 requires |
| O104 at the cutoff, with GPT-6 Astra's Plus measurement on an unreconcilable basis (E106 case 4) | GPT-6 Luna's transfer still takes Astra's 8.1 and becomes diagnostic (L2) |
| I85 probe (g) on r145: a registered note on GPT-6.1 Sol (max)'s frontier-list entries only | the build stops ("frontier list entry differs") |
| (g′): as (g), with the point record lacking its `footnote` key | the build completes (L4) |
| A post-O103 cost-chart capture (2026-10-29) without notes | the build stops |
| The same capture taken at 2026-10-28T23:00Z | passes (L4) |
| An unregistered note at a cost chart's evaluation level, every row's `notes` empty | passes (L1) |
| A registered pricing omission on the Coding Agent Index row "Codex - GPT-6.1 Sol (max)" in post-O103 captures | the build completes; the row gets no caveat and stays the confirmed cheapest at the max-effort headline API bar (L1) |
| `plan_admission.exclusion` with metering-only or availability records, on the repository's own fixture and on a synthetic registry | a report on or spanning such a record is excluded as "spans a partition split", and a two-report cell fails (M1) |
| The real report table with `exclusion` reading only limit and price records | 0 of 52 cells and no report's role change: M1 is latent today |

**Other r145 changes**
- `swing_bridge._with_method` unions both registers, current entries first. Value scores never read the register (an O94 row stays ranked at its published cost), so the union cannot move a replayed score.
- The 13 controlled routes' flags rest on the Anthropic 2026-10-17 "limit" and OpenAI 2026-10-11 "price" records.

**Figures and hand-written facts spot-checked** (all match):
- the bar levels (53.3 / 63.5 / 64.9 and 38.0 / 49.2 / 58.6) and the reach counts (7/5/3 and 13/9/5), recomputed from displayed quality;
- the exchange-rate quality offsets (value points ÷ 0.75);
- FrontierCode's fill effect (0.21 × 2.6 = 0.55; 0.21 × 11.6 = 2.44);
- the feasible admission alternatives (255 = 2⁸ − 1; 127 = 2⁷ − 1) and the thresholds ⌈2N/3⌉ (6 and 11);
- the SemiAnalysis clock dates (ages 30, 91 and 121);
- the S1T and accounting-identity task counts;
- the split and metering lists against the registry;
- line 55's search stages, providers and unreachable sources against the search log.

**Not verified:** live AA pages and boards, and the paywalled SemiAnalysis article.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. The admission build still splits report partitions at metering-only (O99) and model-availability (O105) records, contrary to both decisions.**

*Where.*
- `plan_admission.exclusion()` (line 157) excludes a report as "spans a partition split". It does so by calling `partition(report, profile["partitionSplits"])` with every partition record, and `partition()` never reads a record's type.
- `evaluate()` (line 169) passes only `splitting(...)`, the limit and price records, when it numbers partitions and finds the current one.
- The two steps therefore disagree, and the exclusion step decides.

*What the specification says.*
- **Line 55:** "an announcement that changes only how usage is metered is logged without splitting: OpenAI at 2026-10-16, OpenAI at 2026-10-20 and OpenAI at 2026-10-23", and "(a model-availability change flags without splitting, O105)".
- **Line 152 (E18, new in r145):** "a model-availability change flags the plan's routes and splits nothing".
- **AGENTS.md:** a metering-only announcement "does neither (O83, O99, O101)", and an availability change flags a plan's routes "without splitting its report partition (O105)".
- **The module's own docstring:** a "metering" record "is logged and does not split".

*Probes:*

| Case | Result |
|---|---|
| The repository's own fixture (`tests/test_plan_admission.py` `PROFILE`, which holds a 2026-10-20 metering record): an OpenAI Plus report on 2026-10-20 | `partition(…, splitting(…))` is 1, which is what `test_only_limit_and_price_changes_split_partitions` asserts ("no split on the 20th"); but `exclusion()` returns "spans a partition split" |
| Same fixture: two concordant OpenAI Plus reports on 2026-10-20 and 2026-10-21 | the cell fails ("1 non-provisional report(s) in the current partition") instead of passing |
| A registry with OpenAI's three metering records and an availability record (2026-11-05), and two reports: a weekly one ending 2026-10-24 with no stated start (meter period 10-18 to 10-24, so it spans 10-20 and 10-23), and one ending 2026-11-07 | both are excluded as "spans a partition split"; with only limit and price records reaching `exclusion()`, the same cell passes |
| The real table at the cutoff, with `exclusion()` reading only limit and price records | 0 of 52 cells and no report's role change |

*Status and likelihood.*
- **Latent today.** Every OpenAI report whose meter period touches 2026-10-20 or 2026-10-23 is already excluded for another reason: an anomaly, a lower bound, or the 10-16/10-17 fault days.
- **It will not stay latent.** O75 re-runs all three O71 stages at every release. An unstated window is the meter's own period ending on the report date (I79 L2). So these readings would be wrongly excluded:
  - any OpenAI weekly reading dated 2026-10-24 to 2026-10-29;
  - any monthly reading dated 2026-11-16 to 2026-11-21.
  
  Each of these spans a metering day without touching the fault days. For scale, the current table holds 16 OpenAI weekly readings dated 2026-09-09 to 2026-10-24.
- **The exposure keeps growing.** Every future metering post adds another such day, and so does every availability record O105 now invites.

*Why Medium.*
- **It contradicts two owner decisions** in the build that O81 makes the authority for admission. One of them, O105, is r145's own, and the r145 text says availability "splits nothing".
- **It is silent.** The published per-report reason (`planAllowanceCells[].reports[].excluded`, and the eligible counts in scores.md) names a split on days the specification lists as non-splitting.
- **It is untested.**
- **It can change an outcome.** An excluded report can be one of the two that O73, O78 or O92 need to replace an assumption, a change-flagged measurement or a fault-window measurement.
- **The trigger is ordinary.** Unlike I85's latent Lows, it needs no unusual external event: the records are already in the registry, and the next release's research will tabulate the reports.

*Same root, smaller effects:*
- (i) `draft_figures.registry_figures` lists every non-splitting record as `evidence.meteringAnnouncements`. Line 55 prints that list after "an announcement that changes only how usage is metered is logged without splitting:". An availability record would therefore be printed as a metering-only announcement.
- (ii) The registry's profile rule, which is also rendered in `site/data/plans.json`, still says partition records are "each typed limit, price or metering".

*Change.*
- In `exclusion()`, test against `splitting(profile["partitionSplits"])`, or compute the splits once in `evaluate()` and pass them in.
- Add fixtures showing that a report on, or spanning, a metering day or an availability record is not excluded and pools in the current partition.
- Render availability records in their own figure.
- Name the availability type in the profile rule.

### Low

**L1. O103's notes are now recorded and registered, but a registered pricing omission on those surfaces never makes the row an O94 row, and chart-level notes escape the gate.**

*What happens.* `check_surface_notes` classifies each note of a post-O103 capture and stops on an unregistered one. It then discards the classification. A row's O94 status comes only from `configuration["aaNote"]`, through `aaNoteClass` and `aa_cost_caveat`. That note is the reconciliation inventory's chart footnote, which `chart_footnote` checks against the chart capture.

*What the specification says.*
- E183 (line 116) puts in B_W "the rows whose AA cost AA says omits a pricing term (O94)", and has every post-O103 capture's notes "registered the same way".
- The register's own rule labels "pricing omission" "(O94)" for every surface.

*Probe* (in memory on the clone):
- Setup: post-O103 captures dated 2026-10-29 with per-row `notes` lists, and a registered pricing omission (factor 2) on the Coding Agent Index row "Codex - GPT-6.1 Sol (max)".
- The build passes the gate. GPT-6.1 Sol (max) gets no AA cost caveat and stays the confirmed cheapest at the max-effort headline API bar. That is I84 M1's consequence, reached through the surfaces O103 added.
- For comparison, in I85's probe (c) the same kind of note on the chart cleared the label and held the release.

*Gaps in the gate's scope.*
- **Only per-row notes are read.** An unregistered note recorded at a cost chart's evaluation level passes when every row's list is empty.
- **The legend is hard-coded.** The cost charts' one chart-level note today, the "*" legend, is hard-coded in `scripts/capture-aa-cost-charts.js` (`DECLINED_NOTE`), so a reworded legend can never reach the register.
- **No script records notes yet.** All three capture scripts still record none. The documented `npm run refresh` therefore now stops at the build, which fails closed as intended. But `docs/refresh-and-release.md` reads as if the captures already do it ("which each capture must record verbatim").

*Why Low.* It is latent: no AA capture has been taken since O103, and AA's one pricing caveat so far is on the chart.

*Change (see Q1).*
- Key each surface note to its configurations:
  - a model page's note to the configurations on that page;
  - a Coding Agent Index row's note through the manifest;
  - a cost-chart row's note through the configuration map.
- Take a row's O94 factor as the largest registered factor across all surfaces (O98 applies when any note states none).
- Extend the gate to document-, page- and chart-level notes.
- Extend the capture scripts before the next refresh, recording the legend's text verbatim, and say so in the refresh document.

**L2. O104's "eligible" drops only demoted figures, so a co-donor the comparator excludes for another reason stays in the minimum.**

*The gap.* `rebase_lower_of` keeps a measurement unless `expiry_status(…) == "demoted"`. But `route_candidates` also grades a measurement diagnostic for two other reasons:
- its valuation basis cannot be reconciled (`valuation_status == "different"`, E106 case 4);
- its multiple is not a valid divisor (E109).

*Probe* (real registry at the cutoff). With GPT-6 Astra's ChatGPT Plus measurement marked unreconcilable (`valuationBasisReconciled: false`):
- GPT-6 Astra (max) correctly loses its Plus route.
- GPT-6 Luna's lower-of transfer still takes Astra's 8.1, inherits the mismatch and becomes diagnostic, leaving no Plus row.
- Yet GPT-6.1 Sol's 10.55 is eligible.

O104 and line 55 both say "the lower of its plan's eligible effective figures". This is I85 L5's non-monotonicity, reached through a second exclusion.

*Status: latent.* Every measurement's basis is "unverified", not "different". The case would arise if one GPT model's API price changed in a way its measurement could not be revalued.

*Change.* Use one eligibility predicate in both the comparator and the rebase (recommendation 2), with this case as a fixture.

**L3. Change records can support flags, but nothing makes a record produce its flags, so an O105 availability record is inert on its own.**

*The one-way check.* `check_change_flags` refuses a stored `changeDetectedOn` that has no typed record. Nothing checks the other direction: that a record produces the flags it implies.

*Why O105 makes this matter.*
- An availability record splits nothing, so its only effect is to flag the plan's routes.
- The build never derives that flag from the record. Recording an availability change without also hand-editing each affected route's `changeDetectedOn` therefore changes nothing: no "possibly superseded" label, no E228 blocker and no O78 path.
- Likewise, a limit or price record splits partitions but flags no route unless the routes are edited separately.

*Today:* consistent. The 13 controlled routes carry flags matching the Anthropic 2026-10-17 and OpenAI 2026-10-11 records, and their transfers inherit them.

*Not a repeat.* I85 recommendation 1 proposed the reverse check, and the ledger records no decision on it. The new argument is O105: it created a record type whose whole effect is the flag.

*Change.* Either derive each route's flag from the records, or check the reverse direction. A derived flag would be the earliest applicable limit, price or availability record on or after the measurement's earliest possible day, carried to other plans by O79 and O84.

**L4. Two edges of r145's capture checks.**

- **(a) The twin check compares only the keys both copies carry.**
  - `check_capture_twins` compares `set(entry) & set(twin)`.
  - In probe (g′), a registered pricing note on GPT-6.1 Sol (max)'s `frontier` and `near_frontier` entries, with the `points` record lacking a `footnote` key, builds.
  - `chart_footnote` reads the point, finds no note, and the row keeps its labels.
  - All 190 points carry the key today, so this needs a capture whose two copies differ in schema.
  - Change: compare over the union of keys, minus the list-specific ones (`order`, `tier`, `intelligence_gap`, `cost_ratio`, `nearest_frontier_*`).
- **(b) The O103 gate tests a calendar day.**
  - `check_surface_notes` skips any capture with `capturedAt[:10] <= "2026-10-28"`, so a capture taken on the decision day, after the decision, escapes.
  - Probe: cost charts captured at 2026-10-28T23:00Z without notes pass.
  - O103 binds "the next AA capture", which means any capture later than the 2026-10-25 captures.
  - Change: key the gate to that instant rather than to a calendar day.

**L5. Wording that lags r145.**

- **(a)** E63's first list (line 152) names the typed change records "under O99 and O101" and the register "under O100". The manifest rule now also names O103 and O105.
- **(b)** Line 59 says the lower-of transfer re-takes the lower of the eligible figures "when a report pair replaces a measured figure under O78 or O92". That is too narrow:
  - O104 applies whether or not a pair replaces anything;
  - the case it was decided for (both measurements demoted, one with a pair) is O102's, not O78's or O92's;
  - the registry's `o72Application` keeps the same narrow wording: "O95: … when a report pair replaces its donor".
- **(c)** Neither line 55 nor line 59 states O104's fallback: with no eligible figure left, the transfer keeps its stored donor and is diagnostic with it.
- **(d)** The evidence bundle still describes the register as an "editorial register of AA chart footnotes" (`EVIDENCE_FILES`, printed in raw-data.md).

## 2. Methodology design recommendations

1. **One typed change table drives every effect (M1, L3).**
   - Define one map of record types to effects: limit and price split and flag, availability flags, metering is logged.
   - Every consumer reads that map: `exclusion`, `evaluate`, `check_change_flags`, the route flags (derived, or checked in both directions) and the figures (`evidence.partitionSplits`, `evidence.meteringAnnouncements` and a new `evidence.availabilityChanges`).
   - A parametrised test runs one record of each type through every consumer.
   - This removes M1's class at its source: O99 and O105 each reached two consumers of the record list and missed the third.
2. **One plan-evidence eligibility predicate (L2).**
   - `plan_routes.ineligibility(measurement, …)` returns the reason a measurement is ineligible, or none. The reasons are: demoted, valuation basis different, invalid divisor, or a lapsed report donor.
   - `route_candidates`, `effective_measurement` and `rebase_lower_of` all share it.
   - Fixtures: a demoted co-donor and a case-4 co-donor.
3. **Treat notes as row evidence across surfaces (L1, Q1).**
   - Keep a note inventory keyed by surface, locator and configuration.
   - A row's O94 factor is the largest registered pricing-omission factor over every surface; O98 applies when any such note is factorless.
   - The gate covers document-, page-, chart- and row-level notes.
   - The capture scripts record every note verbatim before the next refresh, the cost-chart legend included.
   - Fixtures: one per surface, plus a replay fixture for a note that first appears off the chart.
4. **Make the capture checks schema-level (L4).** Compare twins over the union of their non-list-specific keys, and key the O103 gate to an instant.
5. **Generate E63's lists from the manifest rules (L5),** so a new gate updates the prose with it.

## 3. Questions for the owner

1. **O103's surfaces and O94 (L1).** AA may print a note on a model page, the Coding Agent Index or a cost chart that the register classifies as a "pricing omission". Which should follow?
   - The note makes the row an O94 row exactly as a chart footnote does: it competes over [C, kC], where k is the largest stated factor across surfaces, and earns no label.
   - Those surfaces are registered for disclosure only, and O94 stays based on the chart.
2. **What an availability flag does (O105).** O105 flags the plan's routes on an availability change while noting that the allowance itself did not change. Which should follow?
   - The flag also makes the row an E228 blocker in Plan interval outputs and lets a later concordant report pair outrank the measurement (O78), as a limit or price flag does.
   - The flag only prints the "possibly superseded" label.

   Today each route stores only a date, so every flag acts alike. A "label only" answer needs the record's type carried onto the route (recommendation 1).

## 4. Verdict

There are no Critical or High findings. There is one Medium and there are five Lows.

**What holds.**
- The figure check exits 0, and 1,631 Python tests pass.
- A clean rebuild of HEAD reproduces every published data file, document, site page and the figures manifest byte for byte, and both scenario files too.

**r145 closes I85 as built:**
- **L1:** availability records pass the flag gate and stay out of `splitting`.
- **L2:** a post-O103 capture without notes stops the build, and the register replays as a method input.
- **L3:** probe (g) now stops the build.
- **L4:** the manifest and register texts are updated.
- **L5:** under O104, GPT-6 Luna follows the GPT-6.1 Sol pair at both 11.25 and 6.24 on the real registry.

**The findings:**
- **M1:** `plan_admission.exclusion` still treats metering-only (O99) and availability (O105) records as splits, so a report on or spanning them is excluded and a cell that should pass fails. This is latent today (0 of 52 cells), but the next release's research will meet it.
- **L1:** O103 notes are registered, but a registered pricing omission off the chart never reaches the row's O94 status, and chart-level notes escape the gate.
- **L2:** O104's eligibility drops only demoted figures.
- **L3:** change records do not produce their flags, so an availability record does nothing on its own.
- **L4:** the twin check reads only shared keys, and the O103 gate tests a calendar day.
- **L5:** E63, line 59 and the bundle description lag r145.

Under O56 this round is not clean (one Medium). I85 was the first clean round at the Claude Opus 5.5 max rung, so the rung's clean count returns to zero.

VERDICT: HAS FEEDBACK
