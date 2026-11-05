# Internal review I89 — Claude Opus 5.5 (effort max) on draft r148

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r148`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…which move the Claude routes' label date to 2026-10-07 and change no score, label or cell verdict. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "cell verdict. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1929): owner decisions O45–O109, editor decisions E247–E270, reviews I29–I88 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` and `docs/refresh-and-release.md`, in full.
- `review-i88-claude-opus-5.5-max.md`, and how the ledger resolved it:
  - M1 became O109, built as `note_sources` and `admitted_note_class`;
  - L1 became `check_register_subjects`;
  - L2 became the E212 interval cell, "by the release cutoff" in E18 and E92, the E63 and manifest citations, the history counts and the `o72Application` label;
  - L3 became the null-label stop in `basket_label`;
  - L4 became two typed 2026-10-07 Anthropic records, adopted as "data changed".
- `draft-r148.md`, every line (1–174), as 22 sequential chunks of at most 15,000 characters covering all 302,690 characters.
- `draft-r148.src.md` where a sentence's source mattered (line 55, the E269 outcome).
- A sentence-level diff of `draft-r147.src.md` against `draft-r148.src.md`. The hand-written changes are the title, E183's O109 clause and the two new checks (line 116), E92's "by the release cutoff" (line 135), E18's and E63's clauses (line 152), the E212 interval cell (line 159) and the history entries.
- The HEAD commit 2c98629: `value_v3.py`, two test files, `plan_cost_routes.json`, `scores.json`, the generated documents, `site/data/plans.json`, AGENTS.md and the ledger.
- Code read:
  - in `value_v3.py`: `assemble`, `assemble_for_release`, `note_sources`, `admitted_note_class`, `basket_label`, `chart_notes`, `chart_level_notes`, `check_register_subjects`, `combined_note_class`, `classify_footnote`, `chart_footnote`, `check_surface_notes`, `aa_cost_caveat`, `caveat_factor`, `anchor_population`, `agent_record_for`, `row_components`, `configuration`, `configurations_from_scores`, `build_tracks`, `build` and the manifest rules;
  - `plan_admission.py` lines 1–140 (`splitting`, `check_change_flags`, `check_change_records`, `applies`, `window`, `partition`);
  - `plan_routes.measurement_span` and `in_fault_window`;
  - `draft_figures.registry_figures` and `REGISTRY_FACTS`;
  - `basket.admission_panel`;
  - the AA cost caveat paths in `emit_docs.py` and `site/viewmodel.py`.
- Data read or queried:
  - `data/scores.json`, both rankings: rows, plan rows and their flags, admission, workloads and anchors, rank separability, the FrontierCode cross-source panel, bar currency, interval bars, `planAllowanceCells` and the manifest; also its r147→r148 diff;
  - `data/plan_cost_routes.json`: the 13 controlled measurements' change fields, the eight typed records, the fault days, `sourceEvidence.semianalysis.changeDetection` and `o72Application`;
  - `data/plan_reports.json` (the Claude Max and Pro rows); `data/aa/aa_footnote_register.json`; `data/aa/cost_charts_capture.json`; `data/aa/coding_agents_capture.json` and its manifest; `data/v3_configuration_map.json`; `data/price_records.json`; the Claude Haiku 5.5 rows' model pages.
- The O71 record:
  - `stage1-anthropic.md`;
  - the stage-2 Anthropic notes (Q3, its "Last official changes" and October items) and the OpenAI notes (section 4, official changes);
  - stage 3: `research_report.md`, `evidence.jsonl` (the release-note quote) and `raw/hn_batch1.txt` (Anthropic's 2026-10-07 credit post as quoted on HN).

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0 in the repository.
- 1,635 Python tests pass with 100% statement and branch coverage in a scratch clone of HEAD (`pytest --cov`; the e2e and js suites were not run).
- The repository's `git status` was clean before I wrote this file.

**Reproduction.** In a scratch clone at the pinned clock (`VALUERANK_NOW=2026-10-25T09:56:47Z`), these regenerate byte for byte: `build_scores`, `emit_docs`, the site build, the figures manifest and both scenario files (47 s).

**Probes.** The scripts are in `/tmp/claude-0/-home-user/7939c829-13d8-5c69-90ae-0a2a9460135a/scratchpad/i89/probes/`; P1 and P2 reuse I88's scripts. Each probe ran in its own scratch clone or in memory; nothing in the repository changed.

| Probe | Result |
|---|---|
| I88 P1 rerun: a registered 2× pricing omission on Claude Opus 5.5 (max)'s ITBench-AA row (ITBench-AA is pending in both rankings) | no O94 row; qualifier counts unchanged. I88 M1 is closed |
| I88 P2 rerun: a 2× omission on GPT-6 Luna (max)'s Coding Agent Index record | an O94 row and blocker in the max-effort ranking, where the index is admitted, and not in the AI Coding Daily ranking, where it is pending, as O109 says |
| B1: Claude Opus 5.5 (max)'s ITBench-AA map label set to null (one of the chart's two cohort rows) | the build passes; max-effort ITBench-AA coverage falls from 2 to 1 of 9 without a message (L2) |
| B2: new ITBench-AA chart rows "GPT-6.1 Sol (high)", "Kimi K3.1 Pro" and "Claude Sonnet 5.5 (max with fallback)", each with a null map label | the build passes in each case (L2) |
| B3 (controls): GPT-6 Astra (max)'s label set to null; a new "GPT-6.1 Sol (max)" row (I88's P5) | the build stops in both cases |
| D: typed Anthropic records added inside the SemiAnalysis measurements' span (2026-09-28 availability; then also 2026-09-22 limit; then also 2026-09-14 limit) | `check_change_records` then requires the Claude routes' label date to be 2026-09-28, 2026-09-22 and 2026-09-14 respectively (L1) |
| E: `appliesTo` set to `claude-haiku-5.5-max`, `Claude Haiku 5.5`, `claude-haiku-5-5` or `claude-opus-5` | the first two stop the build; the xhigh row's ID and a retired model's ID are accepted (L4) |

**Figures recomputed from the underlying data (all match the draft):**
- **Bars.** The frozen bars are 53.3 / 63.5 / 64.9 (set by MiMo-V2.6-Pro, Gemini 4 Argon (high) and GPT-6 Astra (max)) and 38.0 / 49.2 / 58.6. The reach counts are 7 / 5 / 3 and 13 / 9 / 5, and the headline qualifier counts are 4 against 5 and 8 against 9.
- **Exchange rates** from the frozen anchors: 3.04 (4.06), 2.44 (3.25), 2.83 (3.77) and 1.85 (2.46).
- **Plan rows.**
  - 27 and 51 rows; 2 and 3 API fallbacks;
  - 21 and 44 possibly superseded; 3 and 8 in a fault window; 21 and 44 on an unverified basis;
  - 14 (10 + 4) and 30 (26 + 4) on an owner assumption.
- **Admission.**
  - Max-effort ranking: 8 components on an 8-row panel, threshold 6, 255 feasible alternatives.
  - AI Coding Daily ranking: 7 components on a 16-row panel, threshold 11, 127 feasible alternatives.
  - The Coding Agent Index covers 8 of 9 and 3 of 16; ITBench-AA covers 2 of 9 and 0 of 16.
- **Separability and cohort.** 0 of 8 and 1 of 15 adjacent API pairs separate. The FrontierCode cross-source panel gives τ_b 0.766, a mean offset of 2.60 and a largest offset of 11.60. The cohort is 30 configurations with 8 frontier families.
- **r148's own data change moves no score, rank, label or cell verdict.** The scores.json diff touches only three things: the partition indices of seven Claude Max cells (Theo's Max 20x report now "spans a partition split"), the name of the manifest's O94 rule, and the bundle hashes.

**Not verified:**
- live AA pages and boards;
- the paywalled SemiAnalysis article;
- Anthropic's help article and release notes, beyond the O71 record's quotes.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. The draft's statement of this release's change-detection outcome is stale, and r148's E269 re-evaluation stops short of the record and the dating rule it relies on.**

*(a) Stale text: line 55 still says what was true before r148.* "Change detection at this release (E18, E269, owner decision O77)" says three things:
- the Claude plans are flagged because of user reports of the 2026-10-17 shared-meter change;
- the SemiAnalysis Claude routes "are possibly superseded from 2026-10-17";
- "Anthropic made no announcement".

r148's own record says otherwise:
- **The dates.** All five Claude controlled measurements carry `changeDetectedOn` 2026-10-07. Two records set it: the Haiku 5.5 launch (availability, on Pro, Max 5x and Max 20x) and the Max plans' monthly API credits (limit, on Max 5x and Max 20x). Claude Pro alone has a separate `blockingChangeOn`, 2026-10-17. The draft's own history (line 174) says r148 "move[s] the Claude routes' label date to 2026-10-07".
- **The announcement.** The 2026-10-07 credit is an Anthropic announcement. The O71 stage-3 evidence quotes Anthropic's release notes ("Oct 7 monthly API credits for Max and Team"), and the stage-3 HN capture quotes Anthropic's post ("we'll roll out a new monthly API credit to all Max and Team subscribers … Max 5x users will get $100 in credits per month, Max 20x users will get $200").
- **An unexplained split.** Line 55's generated split list now begins "Anthropic at 2026-10-07", but the body never says what that split is. The parenthesis explains only OpenAI's and Kimi's splits.
- **The registry has the same lag.**
  - Each Claude route's `changeDetectionEvidence` still describes only the 2026-10-17 meter reports, although its `changeDetectedOn` is 2026-10-07. I84 L2 updated the GPT routes' strings when their trigger changed.
  - The Anthropic outcome's evidence types the 2026-10-07 credit as a limit change, then says "Anthropic release notes 2026-09-15..10-25 carry no limit entry".

*Why the figure check missed it.* E265 (line 152) says a registry fact of the current release, "the SemiAnalysis stage dates" among them, must be a placeholder in every sentence. Of those stage dates, `draft_figures.REGISTRY_FACTS` holds only the age-stage ones (`semianalysis.supersededFrom` = 2026-11-06 and the rest). It does not hold the change-detection dates that start the possibly-superseded stage earlier. So line 55's dates are typed by hand and unchecked, which is the class E265 exists to remove. By E265's own rule, a stale figure found after the check is a bug in the check.

*(b) Incomplete re-evaluation: the record holds earlier changes that the build's own rule would date.*
- **The rule.** The build dates every SemiAnalysis measurement's possible span as the 30 dates ending on publication: `measurement_span` gives 2026-09-07 to 2026-10-06. `check_change_records` then takes the earliest typed record on or after 2026-09-07 as the label date, and the earliest limit or price record from there as the blocking date.
- **What r148 did instead.** Its re-evaluation (I88 L4) reasoned from the publication date ("a change … after the 2026-10-06 measurement") and recorded only the two 2026-10-07 changes.
- **What the cited record also holds.** The same O71 record lists documented Anthropic changes inside the span:
  - 2026-09-14: weekly limits changed ("a 17% reduction in weekly limits on Claude Code", Anthropic via BleepingComputer);
  - 2026-09-22: five-hour limits raised at the Opus 5.5 launch;
  - the Opus 5.5 (2026-09-22) and Sonnet 5.5 (2026-09-28) launches, in Anthropic's release notes, which are availability changes under O105.

  None of them is a typed record or a dated rejection.
- **What the build would do with them (probe D).** Adding the Sonnet 5.5 launch makes the build require a Claude label date of 2026-09-28. Adding the 2026-09-22 limit record moves it to 2026-09-22, and adding 2026-09-14 moves the label and the blocking date to 2026-09-14 on every Claude plan.
- **The result.** The Sonnet 5.5 launch lies inside the span on any reading, even one that starts the span at Opus 5.5's launch (Q1). So 2026-10-07 is not the date the build's rule gives from the record r148 cites. Under the current convention, the rule also flags a measurement of Opus 5.5 with Opus 5.5's own launch (Q1).
- **OpenAI.** The OpenAI side holds untyped in-span items too: the DevDay plan change of 2026-09-29 (Pro 200 from 20x to 10x), and the "28 days of shipping" Day 1 and Day 2 posts (about 2026-10-05 and 2026-10-06 by the day count the registry uses).
- **Team plans.** The credit post also covers Team plans ("up to $500, pooled"). The new limit record covers only Max 5x and Max 20x, while Claude Team Premium is a tested O85 cell.

*Why it matters.* Today nothing changes:
- every Claude route is already flagged and blocked by the cutoff;
- every Claude cell's current partition starts after 2026-10-17T13:00;
- the published documents print no change date.

The cost is in the record. The specification and the registry give different dates and reasons for one flag. The E269 evaluation, which sets every route's two dates, is not run over the span the build uses. A Kimi- or OpenAI-style change inside a span would be missed the same way.

*Not a repeat.* Part (a) was introduced by r148: I88 L4 was adopted as "data changed" only. Part (b) concerns changes that I88 L4 did not list.

*Change.*
- **Generate the outcome.**
  - Render line 55's outcome from `changeDetection` and the typed records: per provider and plan, the trigger records with their type and basis, the label date and the blocking date.
  - Generate each route's `changeDetectionEvidence` from the same records.
  - Add each provider's label and blocking dates to `REGISTRY_FACTS`, with a fixture in which a hand-typed "possibly superseded from 2026-10-17" fails the check.
- **Re-run E269 over each measurement's whole span** (recommendation 2 and Q1). Resolve every documented change in it as a typed record or as a dated rejection with a reason. Extend the 2026-10-07 limit record to the Team plans the post names, or reject that extension with a reason.
- Add O105 to the flag citation in Output 1 (line 13: "(E18, O77, O79)").

**L2. The new null-label stop (I88 L3) builds the chart name from the roster name and the effort, so it can fire for only 6 of the 30 cohort configurations.**

*The code.* `basket_label` stops the build only when the chart holds `f"{name} ({effort})"`. That string misses three forms:
- **Names that already carry the effort.** The roster name carries the effort for every non-primary row and for GPT-5.6 Luna (low), so "GPT-6.1 Sol (high)" becomes "GPT-6.1 Sol (high) (high)" (14 rows that AA plots without fallback).
- **Fallback rows.** AA's cost charts name every Claude Opus 5.5 and Sonnet 5.5 row "(effort with fallback)" (6 rows).
- **Effort-less families.** Four families are plotted without an effort, giving "Kimi K3.1 Pro (None)" (4 rows).

Checked against AA's chart names (the map's FrontierCode labels), the string matches only six configurations: DeepSeek V4.1 Flash 1017 (max), GPT-6.1 Sol (max), Gemini 4 Argon (high), GPT-6 Astra (max), GPT-6 Luna (max) and Claude Haiku 5.5 (xhigh). That is 5 of the 21 ranked configurations. The unit fixture uses the name "A" with effort "max", the one form that works.

*Probes (the real build, each in its own clone).*
- **B1.** With Claude Opus 5.5 (max)'s label set to null, the build passes. Max-effort ITBench-AA coverage falls from 2 to 1 of 9, with no message. Claude Opus 5.5 (max) is one of the chart's two cohort rows.
- **B2.** New chart rows "GPT-6.1 Sol (high)", "Kimi K3.1 Pro" and "Claude Sonnet 5.5 (max with fallback)" with null labels all pass.
- **B3.** Only the controls stop the build: GPT-6 Astra (max), and I88's "GPT-6.1 Sol (max)" probe.

*Why it matters.*
- **The specification overstates the guard.** Line 116 states without condition that "a chart row named as a cohort configuration must have that configuration's label". The history says r148 "checks … unlabelled chart rows", and the manifest lists the basket-chart labels among its passed gates.
- **The likely failure is the one the guard was added for.** AA charts an existing cohort configuration, and the map's label defaults to null. The row then silently loses its ITBench-AA cost, and with it its notes once the component is admitted. That undercounts E140's two-thirds test, or, after admission, moves the row to a subset workload, which is the I50 H1 failure.
- **It is latent.** ITBench-AA is pending in both rankings, and under O109 its notes count for nothing yet.

*New argument.* The guard adopted for I88 L3 is vacuous for 24 of the 30 cohort configurations by construction. Taking the family name instead of the roster name would fix only the first 14; the 10 fallback and effort-less rows would still escape. This is the third round on basket-chart labels (I87 L4, I88 L3). Each fix was a text heuristic that missed AA's forms, as the Coding Agent Index labels did from I50 to I56, until O64 closed that list.

*Change.*
- **Close the ITBench-AA chart as O64 closed the Coding Agent Index.**
  - Register every chart row by AA's label in a reviewed manifest, as the exact record of one cohort configuration or as not one, with a reason.
  - Stop the refresh on a new, relabelled or vanished row.
  - Derive each configuration's label from the manifest, and drop the name construction.
- **Short of that**, match through AA's plotted naming (family, effort and fallback state, as `aaPlottedNames` records it), add one fixture per form, and narrow the line 116 wording to what the build checks.

**L3. O108's "registered and disclosed" is still not implemented, and O109 widens what goes undisclosed.**

*What O108 promises.* Notes on other charts "are registered and disclosed but change no row". O109 adds a second class of notes that count for nothing: a pending component's notes (ITBench-AA in both rankings, the Coding Agent Index in the AI Coding Daily ranking). Such a note starts to count the moment its component is admitted. If it is a registered pricing omission, the row then becomes an O94 row, and its anchor membership ends at the next freeze.

*What the build publishes.*
- r148 computes `aaNoteSources` per row and surface, but scores.json publishes only `aaCostCaveat`, its factor and its cost range.
- A registered note that does not count is printed nowhere.
- The register lists note texts with no rows or surfaces.

*Not a repeat.* I88 M1's last bullet asked for this disclosure. The ledger's I88 entry adopts O109 and says nothing about it. Two things are new:
- O109's pending class makes the disclosure forward-looking;
- the per-surface data now exists in the build and is dropped only at output.

*Status.* It is latent until O103's captures record notes, which happens at the next refresh.

*Change.*
- Publish `rows[].aaNotes` in both rankings: per surface, the text, class and factor, whether the note counted, and the reason when it did not (a non-basket chart, a pending component, or an `appliesTo` list that excludes the row).
- Print the notes that did not count beside the O94 rule in scores.md.

**L4. Wording that lags O105–O109, and one residual in the `appliesTo` check.**

- **The refresh document** still says "a pricing omission registered on any of them makes the row an O94 row (O106)". Since O108 and O109, only the chart footnote, the model page and the components admitted to the ranking's workload count. The operator reads this at the next refresh, the one at which O103 first records these notes.
- **The footnote register's `rule`** has three gaps:
  - it cites O106 and O108 but not O109;
  - it says "only charts whose cost is in the ranking's cost workload count", which leaves out the index;
  - it does not say that `appliesTo` must name known configurations.
- **The manifest.**
  - The rule "Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79)" omits O105 and O107, although Claude Pro's label date now rests on an availability record.
  - The "build-stopping evidence gates" rule omits O109, which the draft's E63 cites.
- **The `appliesTo` check.** `check_register_subjects` accepts any configuration-map ID. The map holds 50 IDs, retired models such as `claude-opus-5` among them. So `appliesTo: ["claude-haiku-5-5"]`, the xhigh row's ID written for the max row (the slip I88 L1 named), still passes (probe E). Check the IDs against the cohort configurations and the models AA's chart rows name, or key the list by family with an optional effort list (I88 recommendation 2).

## 2. Methodology design recommendations

1. **Generate the change-detection outcome; never type it (L1a).**
   - Line 55's per-provider paragraph, each route's `changeDetectionEvidence` and the manifest's lifecycle rule should be rendered from one source: `changeDetection` plus the typed records (type, plans, date and basis).
   - Add each provider's and plan's label and blocking dates to `REGISTRY_FACTS`, so a hand-typed change date fails the check the way a hand-typed age-stage date already does.
2. **Date each measurement's possible span from public evidence, and log every candidate change inside it (L1b, Q1).**
   - Earliest possible day = the latest of:
     - the stated window start;
     - publication − 29 days;
     - the measured model's launch on the plan (Opus 5.5: 2026-09-22);
     - a schedule or regime the measurement says it ran under (the GPT routes record "Current post-September 29 Codex schedule").
   - Record it as `measurementWindow.start` with its evidence, so that change detection, fault windows and O78 all read it.
   - The measured model's own launch, and the regime the measurement names, are never a change "since" the measurement.
   - Then keep the candidate log I88 recommended. Each release lists every dated change found by E18's scoped checks, O77 announcements and the O71 record, and resolves each as a typed record or a dated rejection with a reason (for example, "Sonnet 5.5 cache-read price: an API tariff, handled by E170"). The build fails on an unresolved candidate inside any measurement's span.
3. **Close the ITBench-AA chart (L2).** Use a reviewed row manifest keyed by AA's label, the O64 pattern. Derive labels from it, and stop on new, relabelled or vanished rows. Remove the `f"{name} ({effort})"` heuristic. This ends a class that has now taken three rounds.
4. **Publish where each AA note sits and whether it counted (L3).**
   - Per row and ranking: the surface, the text, the class, the factor, and whether the note counted and why. This delivers O108's disclosure.
   - It also gives warning of O94 transitions at admission, since a pending component's pricing note turns into anchor exits at the next freeze.
5. **Give bundled-credit grants their own record type (Q2).**
   - A grant of API credits outside the subscription meter (Max 5x $100 and Max 20x $200 a month, from 2026-10-07) changes the plan's full value but not the meter that user reports read.
   - A type that flags and blocks the routes whose multiples omit the credits, but does not split meter-reading partitions, would keep, for example, Theo's 2026-10-08 Max 20x reading poolable. The editor's "limit" typing excludes that reading as spanning the split.

## 3. Questions for the owner

1. **Should a controlled measurement's possible span start no earlier than the measured model's public launch on the plan, and no earlier than the schedule the measurement says it ran under?**
   - **Today.** The span is the 30 dates ending on publication: 2026-09-07 to 2026-10-06 for every SemiAnalysis route. Under that span, recording the O71 record's documented Anthropic changes moves every Claude label and blocking date to 2026-09-14. The Opus 5.5 launch on 2026-09-22 would also flag the measurements of Opus 5.5 itself. Recording OpenAI's DevDay plan change would flag the ChatGPT routes it covers from 2026-09-29, although those routes record that they were measured under the post-September 29 schedule.
   - **With the bound** (Opus 5.5 from 2026-09-22, the GPT routes from 2026-09-29), the 2026-09-14 change, the measured model's own launch and the DevDay schedule are rejected with that reason. The Sonnet 5.5 launch (2026-09-28, availability) then sets the Claude label date. Two cases still need a ruling:
     - the five-hour raise announced at the Opus 5.5 launch falls on the bound itself;
     - Fable 5.1's measurements keep the 30-day span unless Fable's own launch is later.
   - **Stakes.** No score, label or cell verdict changes either way today. The answer decides what recommendation 2 records.
2. **Is a bundled API-credit grant a limit change that also splits the report partitions (r148's editorial typing), or a flagging and blocking change that leaves meter-reading partitions whole?**
   - **Today.** The split at 2026-10-07 excludes Theo's weekly Max 20x reading (dated 2026-10-08) as spanning the split. Per Anthropic's post, the credits are API credits for the Claude Platform, not a change to the meter that reading measures.
   - **Stakes.** No verdict changes today, because the current partition starts after 2026-10-17T13:00. The answer decides recommendation 5 and the type of the 2026-10-07 Max record.

## 4. Verdict

There are no Critical, High or Medium findings. There are four Lows.

**What holds.**
- The figure check exits 0, and 1,635 Python tests pass at 100% coverage.
- A clean rebuild of HEAD at the pinned clock reproduces every published data file, document, site page, the figures manifest and both scenario files byte for byte.
- Every current figure I recomputed matches.

**r148 against I88, as built.**
- **M1 is closed.** P1 and P2 rerun as O109 requires: a pending component's note changes nothing, and an admitted one makes an O94 row in its ranking only. The class is computed after E184's possible re-assembly.
- **L1 is closed for unknown IDs.**
- **L2 is closed:** the E212 cell, "by the release cutoff", the E63 and manifest citations, the history counts and the `o72Application` label.
- **L3 is closed only for the "Name (effort)" form**, which covers 6 of the 30 cohort configurations (L2 above).
- **L4 is closed in the data but not in the draft's outcome text,** and its re-evaluation stopped short of the measurement span the build uses (L1 above).

**The findings.**
- **L1:** the E269 outcome on line 55 is stale against r148's own registry and history; the figure check does not cover change dates; and the re-evaluation omits documented in-span changes that the build's rule would date earlier.
- **L2:** the null-label stop matches AA's chart naming for 6 of 30 configurations, so a null label on Claude Opus 5.5 (max)'s charted row passes silently.
- **L3:** O108's promised disclosure of the notes that do not count is still missing.
- **L4:** wording lags in the refresh document, the register's rule and the manifest, and the `appliesTo` check accepts any map ID.

All four are latent or textual. None moves a score, rank, label or cell verdict.

Under O56 this round is clean, with no Medium or higher finding. I86, I87 and I88 were not clean, so this is the first clean round at the Claude Opus 5.5 max rung since I85, and the rung's clean count becomes one.

VERDICT: HAS FEEDBACK
