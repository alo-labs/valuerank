# Internal review I90 — Claude Opus 5.5 (effort max) on draft r149

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r149`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…limits `appliesTo` to the cohort and publishes the notes that count for nothing. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "for nothing. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1940): owner decisions O45–O111, editor decisions E247–E270, reviews I29–I89 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` and `docs/refresh-and-release.md`, in full.
- `review-i89-claude-opus-5.5-max.md`, and how the ledger resolved it:
  - L1 became typed records for 2026-09-14, 2026-09-22 (limit and availability), 2026-09-28 and OpenAI's 2026-09-29, the credit retyping (O111), the span bound (O110) and the generated `evidence.changeDates` figure on line 55;
  - L2 became point-name matching in `basket_label`;
  - L3 became `rows[].aaUncountedNotes`;
  - L4 became new wording in the refresh document, the register's rule and the build-stopping manifest rule, and a cohort-only `appliesTo` check.
- `draft-r149.md`, every line (1–174, 304,655 characters), as 21 sequential chunks of at most 15,000 characters.
- `draft-r149.src.md`, and a sentence-level diff of `draft-r148.src.md` against it. The hand-written changes are the title, line 55 (the E269 outcome, now ending in `{{fig:evidence.changeDates}}`), line 152 (the O111 and O110 clauses in E18) and the r149 history entry.
- The HEAD commit 4031122 ("Draft r149"): `plan_routes.py`, `plan_admission.py`, `value_v3.py`, `draft_figures.py`, the three test files, `plan_cost_routes.json`, the footnote register, `scores.json` (diffed against r148's), the generated documents, `site/data/plans.json`, AGENTS.md and the refresh document.
- Code read:
  - in `plan_routes.py`: `blocking_change`, `grade_rank`, `post_change_ranks`, `expiry_status`, `change_flagged`, `_regime_start`, `measurement_span`, `change_floor`, `in_fault_window`, `report_covers`, `pair_replaces`, `effective_measurement`, `measurement_eligible`, `rebase_lower_of`, `_rebased`, `rebase_transfer`, `route_candidates`, `admission_table`;
  - in `plan_admission.py`: the record-type sets, `splitting`, `check_change_flags`, `check_change_records`, `applies`, `window`, `partition`, `on_fault_day`, `exclusion`;
  - in `value_v3.py`: the start of `assemble`, `classify_footnote`, `chart_footnote`, `check_surface_notes`, `check_register_subjects`, `check_capture_twins`, `check_captured_footnotes`, `basket_label`, `chart_notes`, `chart_level_notes`, `note_sources`, `uncounted_notes`, `admitted_note_class`, `combined_note_class`, `configuration`, `configurations_from_scores`, `build_tracks`, `build`, `main` and the manifest rules;
  - in `build_scores.py`: the cohort rows and the `build_tracks` call;
  - in `draft_figures.py`: `registry_figures`, `REGISTRY_FACTS`, `check` and `main`.
- Data read or queried:
  - `data/plan_cost_routes.json`: the 13 typed records, the fault days, the 13 controlled measurements' new fields and change dates, the 123 transfers and their donors, `sourceEvidence.semianalysis` (with `changeDetection`), `o72Application` and the profile rules;
  - `data/plan_reports.json` and the 38 report cells in `scores.json`;
  - `data/scores.json`, both rankings: plan rows and their flags, manifest rules, `aaUncountedNotes`, listed rows, and its r148→r149 diff;
  - `data/aa/aa_v432_snapshot.json` (release dates), `data/aa_frontier_capture.json`, `data/aa/cost_charts_capture.json`, `data/v3_configuration_map.json`, `data/aa/aa_footnote_register.json`, `data/v3_frozen.json` and `data/v3_frozen_aicd.json`.
- The O71 record:
  - the stage-2 OpenAI notes, §4 (official changes and the "28 days of shipping");
  - the stage-2 Anthropic notes, Q3 (the October changes);
  - the stage-3 `research_report.md` (its reset references);
  - an earlier round's capture of wokey.ai's limits page, the record's source for the 2026-09-22 raise (read as data).

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0 in the repository, and again in a rebuilt clone.
- All 1,637 collected Python tests pass with 100% statement and branch coverage in a scratch clone of HEAD. The e2e and js suites were not run.
- The repository's `git status` was clean before I wrote this file.

**Reproduction.** In a scratch clone at the pinned clock (`VALUERANK_NOW=2026-10-25T09:56:47Z`), `build_scores`, `emit_docs`, the site build, the figures manifest and both scenario runs regenerate every tracked file byte for byte (`git status` empty afterwards).

**Probes.** The scripts are in `/tmp/claude-0/-home-user/7939c829-13d8-5c69-90ae-0a2a9460135a/scratchpad/i90/probes/`. Each probe ran in its own fresh clone or in memory; nothing in the repository changed.

| Probe | Result |
|---|---|
| I89 B1–B3 rerun: null ITBench-AA labels on Claude Opus 5.5 (max) and GPT-6 Astra (max); new chart rows "GPT-6.1 Sol (high)", "Kimi K3.1 Pro", "Claude Sonnet 5.5 (max with fallback)" and "GPT-6.1 Sol (max)" with null labels | the build stops in all six cases. I89 L2 is closed |
| B4: GPT-6.1 Sol (max)'s ITBench-AA label set to "GPT-6 Astra (max)", another configuration's existing row | the build passes; max-effort ITBench-AA coverage rises from 2 to 3 of 9 (L5) |
| E2: the register's `appliesTo` set to `gpt-6-luna-low`, an excluded cohort configuration | `build_scores` passes; `value_v3 scenarios` stops (L6) |
| F(a): `modelLaunchedOn` of the Opus 5.5 Max 20x measurement typed 2026-10-22, after its 2026-10-06 publication | the build stops with "its change flag must be None from the typed change records" (L1) |
| F(b): the same, with the route's flag fields edited as the build demands | the build passes; the Max 20x plan rows (2 and 4) lose "possibly-superseded" (L1) |
| G: r148's sentence "…are possibly superseded from 2026-10-17", a hand-typed "blocking from 2026-10-11" and a "Today…" sentence with a hand-typed label date, each inserted into r149's source | `lint` and `registry_problems` raise nothing (L4) |
| H (in memory): a chart-level note added to the FrontierCode cost chart | `aaUncountedNotes` would list it for GPT-6.1 Sol (high), whose row that chart does not hold (L6) |

**Figures recomputed from the underlying data (all match the draft):**
- **Exchange rates** from the frozen anchors: 3.04 (4.06), 2.44 (3.25), 2.83 (3.77) and 1.85 (2.46).
- **Bars.** The frozen headline and lower-quartile bars are 63.54 (Gemini 4 Argon (high)) and 53.27 (MiMo-V2.6-Pro) in the max-effort ranking, and 49.24 (MiMo-V2.6-Pro) and 38.00 (GPT-6 Luna (xhigh)) in the AI Coding Daily ranking.
- **Plan rows.**
  - 27 and 51 rows; 2 and 3 API fallbacks;
  - 21 and 44 possibly superseded; 21 and 44 on an unverified valuation basis; 3 and 8 in a fault window;
  - 14 (10 transfers + 4 ceilings) and 30 (26 + 4) on an owner assumption.
- **Cohort.** 19 vertices and 11 near points make 30 configurations, from 8 frontier and 5 near-only families. The first vertex, GPT-6 Luna (low) at $10.63, is the cheapest of the 190 plotted points.
- **Change dates.**
  - Every controlled measurement's stored label and blocking date equals the build's derivation, and line 55's list matches: Fable 5.1 from 2026-09-14; Opus 5.5 from 2026-09-28 (blocking from 2026-10-07 on Max, 2026-10-17 on Pro); GPT routes from 2026-10-11.
  - The `modelLaunchedOn` values equal AA's `releaseDate`: Opus 5.5 2026-09-22, GPT-6.1 Sol 2026-09-29, GPT-6 Astra 2026-09-03, Fable 5.1 2026-09-01.
  - `scheduleFrom` 2026-09-29 matches the GPT routes' "Current post-September 29 Codex schedule".
- **r149's data change moves no score, rank, label or cell verdict.** The scores.json diff touches only four things:
  - partitions and exclusions in the Anthropic cells: Theo's Max 20x reading is back in a partition, and Last_Lab_3627, Delicious-Shower8401 and NTRYourWaifu now span a split;
  - the new, empty `aaUncountedNotes` fields;
  - two manifest rule texts;
  - the bundle hashes.

**Not verified:**
- live AA pages and boards;
- the paywalled SemiAnalysis article;
- Anthropic's and OpenAI's posts, beyond the O71 record's quotes.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. O110's span inputs are typed by hand and never checked, and a wrong one makes the build demand that a flag be removed.**

*The code.*
- `_regime_start` is the only reader of `modelLaunchedOn` and `scheduleFrom`.
- No check compares `modelLaunchedOn` with the `releaseDate` that AA's snapshot carries for the measured model, although O110 and line 152 take the launch "from AA's release dates".
- No check requires either bound to fall on or before publication, or the span to be non-empty.
- `scheduleFrom` has no source besides the route's free-text regime.

*Why it matters.*
- `check_change_records` derives each measurement's label date from these fields and stops the build unless the stored flag matches. So a wrong input is not caught; it is enforced.
- **Probe F.** A launch typed 2026-10-22 (for 2026-09-22) makes the build require the Opus 5.5 Max 20x flag to be removed. Once the flag is removed, the build passes, and the Max 20x plan rows (2 and 4) lose "possibly-superseded" and their E228 blocker status. The transfers and O88 routes resting on that measurement lose them with it.
- The same span feeds `in_fault_window`, so an inverted span would also never match a fault window.

*Today.* All four launch dates equal AA's release dates, and `scheduleFrom` matches the regime, so nothing is wrong now. The refresh document says the span is "bounded by its model's launch and stated schedule", but not where an operator takes either date from.

*Change.*
- Derive `modelLaunchedOn` from the snapshot's `releaseDate` for the measurement's source model, or stop the build on a difference.
- Stop the build when either bound postdates publication or the span is empty.
- Give `scheduleFrom` a typed source, as the DevDay record already is for the GPT routes.
- Keep probe F as a fixture, and say in the refresh document where both dates come from.

**L2. The normative text still describes the span as it was before O110, and still treats only limit or price changes as blocking.**

- **E92's earliest day (line 135).** A blocker's change must be "dated on or after the earliest day its measurement can have been taken (its window start, else 29 days before publication…)". Read literally, this counts the 2026-09-14 limit record (after 2026-09-07) against the Opus 5.5 measurements, which O110 and the build exclude. Line 55 gives their blocking dates as 2026-10-07 and 2026-10-17.
- **The fault-window clause (line 55)** still dates a measurement "by its window, else conservatively by the 30 days ending on its publication date". `in_fault_window` now uses the span bounded by O110.
- **Credit omitted.** O111 says a credit grant "flags and blocks like a limit change", and the build blocks the Max routes from the 2026-10-07 credit. The places that define blocking still name only "limit or price":
  - E92 (line 135);
  - comparator key (2) (line 51) and the O73 sentence (line 55);
  - the E212 table's trigger, comparator and interval cells (line 159);
  - E18's own blocking-date sentence (line 152: "the earliest limit or price record from there on");
  - the README flag legend;
  - the registry's profile rule 11 ("each typed limit, price, availability or metering");
  - the docstrings of `blocking_change` and `check_change_records`.
- **A displaced clause (line 152).** "so an earlier availability change never cancels a later limit or price change" now follows the O110 sentence, from which it does not follow. It belongs to the two-date rule before it.
- **Provenance.** The ledger's O110 entry marks the start-day rule ("a change dated on that start day is part of the measured regime") as an "editorial ruling on I89's open case". Line 152 and `o72Application` attribute it to owner decision O110. Under the draft's own precedence rules the two are not equivalent.
- **Citations and dates.**
  - Output 1's flag citation is still "(E18, O77, O79)". I89 L1 asked for O105; O110 and O111 now apply too.
  - The manifest rule "Plan evidence lifecycle and change detection (E18, E151, E269, O77, O79)" was not reached by the I89 L4 adoption, which updated only the build-stopping rule.
  - `o72Application`, rendered in methodology.md and on the site, reads "O72-O111 (2026-10-26 to 2026-10-28)", but O110 and O111 are dated 2026-10-29.

*Why it matters.* By the draft's preamble the Normative definitions govern prose, so E92's stale parenthetical is the text a reader is told to trust. The owner decisions govern by precedence, and no output changes today: every blocking date falls before the cutoff under either reading. But the definitions now disagree with the build on two dates and on which record types block.

*Change.*
- Rewrite E92's parenthetical and the fault-window clause to cite the span O110 bounds, and its change floor.
- Write "limit, price or credit" wherever blocking is defined.
- Move the "so" clause back to the two-date rule.
- Tag the start-day rule correctly: either record the owner's confirmation or give it an E number.
- Fix the citations, the manifest rule and the date range.

**L3. The E269 outcome now says every documented change is recorded, but documented OpenAI changes, OpenAI's meter resets, user-detected Claude changes and the unlisted Claude plans remain unresolved.**

- **The claim.** Line 55 says: "With every documented change recorded and each measurement's span bounded (O110), the flagged measurements are: …".
- **OpenAI's documented changes.**
  - The O71 record's OpenAI notes (§4) list the "28 days of shipping":
    - Day 1: default speeds up by about 50%;
    - Day 2: auto-review made free;
    - Day 3: "a banked reset for all paid accounts";
    - global resets on Days 6, 8, 10, 13, 15, 17/18 and 20.
  - By the registry's own day count (Day 7 = 2026-10-11) these fall between 2026-10-05 and 2026-10-24.
  - None is typed or rejected. `changeDetection`'s OpenAI evidence still lists only Days 7, 12, 16 and 19.
  - Under O111, a reset that grants allowance without changing the meter reads like a credit grant. Typed that way, it would move the GPT routes' label and blocking dates from 2026-10-11 to 2026-10-07.
- **Resets and report readings.**
  - A meter-fraction reading that spans a global reset is not a fraction of one week's allowance. The stage-3 record cites YiwenPang: "after Tibo's reset, 176M tokens used 76% of allowance vs 490M for 100% the previous day".
  - The eligibility profile has no reset class. So mehoney's eligible weekly ChatGPT Plus reading (2026-10-06 to 10-07) spans the Day 3 reset and still enters its cell's range test.
- **User-detected Claude changes.** The Anthropic notes (Q3) report five-hour changes before Claude Pro's 2026-10-17 blocking date:
  - from about 2026-10-09: Cadaverr, jihjun-ai in #102667, and SemiAnalysis's A/B arm;
  - from about 2026-10-13: leolim031 in #101937.

  No result of E18's two-report test is recorded for them, either way.
- **Unlisted Claude plans.**
  - The Anthropic records list Pro, Max 5x and Max 20x only.
  - Yet wokey.ai's tracker, the record's source for the 2026-09-22 raise, says that raise covered "Pro, Max and Team". The 2026-10-07 release note covers "Max and Team" (quoted in I89).
  - O79 says a change to a shared meter flags every plan on it.
  - Because `applies` matches plan names exactly, the O85 cells "Claude Max (tier unstated)", "Claude (plan redacted)" and "Claude Team Premium" sit in partition 0: no split reaches them. kakki-1's tier-unstated Max reading (2026-10-16T18:00 to 10-23T18:00) spans the 2026-10-17T13:00 split; today it is excluded as a lower bound.
- **What the body explains.**
  - The split parenthesis on line 55 still says "OpenAI's is its Day 7 post", but there are now two OpenAI splits.
  - The 2026-09-29 DevDay split, which covers ChatGPT Pro 200 only, is explained nowhere in the body.
  - The generated split list is not in date order.
  - The Claude routes' `changeDetectionEvidence` still cites only the 2026-10-17 reports, which is the registry half of I89 L1(a).

*Why it matters.* Nothing changes today: every route is already flagged and blocked by the cutoff, and every affected cell already fails. But the release text claims a completeness the registry does not have, and readings that span a reset can enter a future admission.

*Not a repeat.* I89 L1(b) named Days 1 and 2, and the ledger records neither a typed record nor a rejection for them. What is new:
- O111's credit type now offers a class for the resets;
- the reset days corrupt the meter readings that span them;
- the 10-09 and 10-13 candidates;
- how far plan-scoped records reach;
- the completeness claim itself, which r149 introduced.

*Change.* See recommendation 2 and questions 1–2. Until then, narrow line 55 to "every change the registry records".

**L4. The figure check still does not guard change dates.**

- E265 (line 152) says that a registry fact of the current release, "the SemiAnalysis stage dates" among them, "is a placeholder in every sentence, dated or not, and the check fails when one is typed by hand".
- A label or blocking date is where the possibly-superseded stage starts. But `REGISTRY_FACTS` holds only the age-stage dates.
- **Probe G.** Three sentences were each inserted into r149's source: r148's own stale sentence ("…are possibly superseded from 2026-10-17"), a hand-typed "blocking from 2026-10-11", and "Today the Claude Max routes are possibly superseded from 2026-10-07". None of them raises anything in `lint` or `registry_problems`.

*New argument.* I89 L1(a) asked for both the generated figure and the check. r149 delivered the figure, so line 55 is right today, but the class E265 exists to remove is still open. By E265's own rule, the gap between its text and the check is a bug in the check.

*Change.* Add each route's label and blocking dates, and the split dates, as registry facts with "superseded", "blocking" and "split" contexts. Use r148's sentence as the fixture.

**L5. A basket-chart label that is not null is never checked against the configuration it belongs to.**

- `basket_label` now computes the configuration's expected chart names (its point name and "Name (effort)"), but uses them only when the label is null.
- A label that names another configuration's row passes, and so do two configurations that share one label.
- **Probe B4.** With GPT-6.1 Sol (max)'s ITBench-AA label set to "GPT-6 Astra (max)", the build passes. Max-effort ITBench-AA coverage rises from 2 to 3 of 9, with GPT-6.1 Sol (max) carrying GPT-6 Astra (max)'s cost.

*Why it matters.*
- This is the class of the Coding Agent Index pins (I50 H1, I51 and I52), where a pin naming another record mispriced a row.
- It is latent while ITBench-AA is pending (the threshold is 6 of 9).
- Once ITBench-AA is admitted, such a slip would change a row's basket cost and the admission count.

*Change.*
- When the chart holds a row in the expected set, require the label to be in that set.
- Stop the build on a label that two configurations share.
- Add one fixture for each.

**L6. The cohort-only `appliesTo` check and the disclosure of uncounted notes, as built.**

- **Two configuration sets.**
  - `build_scores` passes all 30 cohort configurations to `assemble`, so `check_register_subjects` accepts any cohort ID there.
  - `value_v3.main` (freeze, scenarios, dual-run) passes `configurations_from_scores` instead, which keeps only the 21 configurations ranked in at least one ranking.
  - **Probe E2.** `appliesTo: ["gpt-6-luna-low"]` names an excluded cohort configuration. It passes `build_scores` but stops `value_v3 scenarios`, while the register's rule says only that it "must be in the cohort".
- **`aaUncountedNotes`.**
  - Each entry carries only the note's surface and text. It has no registered class, no factor, and no reason the note does not count (a pending component, or a chart outside the basket), all of which I89 L3 asked for.
  - A chart-level note on a pending or non-basket chart is listed for every row with a non-null map label. That includes rows the note's `appliesTo` excludes and rows the chart does not hold. 23 of the map's FrontierCode labels name rows that the FrontierCode cost chart lacks, so (probe H) GPT-6.1 Sol (high) would disclose a FrontierCode chart note.
  - Listed configurations (the O41 indicative rows) do not publish the field.
  - The draft's body never names the field; only the history says the release "publishes the notes that count for nothing".

*Status.* This is latent until O103's captures record notes.

*Change.*
- Pass the same cohort to every command, or derive the known set from the cohort points in the chart capture.
- Give each uncounted note its class, factor and reason.
- Attach a chart-level note only to rows the chart holds and its `appliesTo` includes.
- Publish the field for listed rows too.
- Name `rows[].aaUncountedNotes` beside O108 in the specification.

## 2. Methodology design recommendations

1. **Derive the O110 span from evidence, and publish it (L1, L2).**
   - Take each measurement's launch bound from the AA snapshot's release date for its source model.
   - Give each stated schedule a typed record.
   - Stop the build on a bound after publication or on an empty span.
   - Publish each measurement's span and change floor beside its two dates, in scores.json and in the route view. A reader can then see why 2026-09-14 flags Fable 5.1 but not Opus 5.5.
   - Let E92's definition cite that published object instead of restating a formula.

2. **Keep a typed candidate log for E269, with resets (L3, questions 1–2).**
   - At each release, list every dated provider change that the O71 record and E18's scoped checks surface: announcements, documentation changes, resets and user-detected changes.
   - Resolve each one as a typed record, or as a dated rejection with a reason. Examples: "Day 1: throughput only, not limits or price"; "Sonnet 5.5 cache-read cut: an API tariff, handled by E170".
   - Add a reset type that excludes any report reading spanning a reset, as an accounting-fault day does. If the owner agrees, let it also flag routes like a credit.
   - Let records name plan families ("Claude Max*", "Claude Team*"), so that the O85 cells on the same meter split with them.
   - Fail the build on an unresolved candidate inside a measurement's span or inside the report window.

3. **Close the change-date class in the figure check (L4).** Make each route's label and blocking dates, and the split dates, registry facts, with r148's sentence as the fixture.

4. **Make basket labels closed-world in both directions (L5).** Whenever the chart holds the configuration's own point name, a non-null label must be that name, and no two configurations may share a label.

5. **Use one configuration set, and make the disclosure informative (L6).**
   - Every command assembles the same cohort.
   - `aaUncountedNotes` carries class, factor and reason, and lists a note only for the rows it concerns.
   - Listed rows publish the field too.

6. **Name the Max plans' monthly API credits among the plan features the multiple does not value (Known limitations).**
   - O111 records the credits as a grant: $100 a month on Max 5x and $200 on Max 20x, from 2026-10-07.
   - The selected Max multiples (about 57–59×) predate the grant and value only measured meter consumption.
   - AGENTS.md does not allow a provider-stated amount as the numerator, so the consistent treatment is disclosure.
   - The size is about 1.0× of the fee: roughly 1.7% of the multiple, or under 0.1 value point.

## 3. Questions for the owner

1. **How should a provider's global meter reset be typed?**
   - **Background.** OpenAI's "28 days of shipping" reset the meters of all paid accounts on Days 3, 6, 8, 10, 13, 15, 17/18 and 20, which is 2026-10-07 to 2026-10-24 by the registry's day count.
   - **The options.**
     - (a) As a credit (O111): it flags and blocks routes and splits nothing. This moves the GPT routes' label and blocking dates from 2026-10-11 to 2026-10-07.
     - (b) As a new reset type that excludes every report reading spanning a reset day, as an accounting-fault day does, and flags nothing.
     - (c) Both.
     - (d) Log only.
   - **Stakes.** No score, label or cell verdict changes today. Under (b) or (c), mehoney's eligible weekly ChatGPT Plus reading (2026-10-06 to 10-07) leaves its cell.
2. **Should change records reach the unlisted plans that share a listed plan's meter?**
   - **Background.**
     - O79 flags every plan on a shared meter, and O85 tests every cell.
     - But the Claude records name only Pro, Max 5x and Max 20x, so "Claude Max (tier unstated)", "Claude (plan redacted)" and "Claude Team Premium" are never split.
     - The 2026-09-22 raise and the 2026-10-07 credits covered Team plans too.
   - **Stakes.** No verdict changes today. The answer decides whether recommendation 2 adds plan families.

## 4. Verdict

There are no Critical, High or Medium findings. There are six Lows.

**What holds.**
- The figure check exits 0, and all 1,637 collected Python tests pass at 100% coverage.
- A clean rebuild of HEAD at the pinned clock reproduces every published data file, document, site page, the figures manifest and both scenario files byte for byte.
- Every current figure I recomputed matches.
- Every derived change date matches the registry, and the registry's launch dates match AA's release dates.

**r149 against I89, as built.**
- **L1 is adopted in the data:** typed records, the credit retyping and the O110 bound. Line 55's dates are now generated.
  - Not done: the completeness claim, the OpenAI side and the registry's evidence strings (L3 above), and the check (L4 above).
- **L2 is closed for null labels:** all six probes stop the build. The non-null direction is open (L5 above).
- **L3 is adopted as a field,** with less content and coarser scoping than asked (L6 above).
- **L4 is mostly adopted:** the refresh document, the register's rule and the build-stopping rule are fixed.
  - Still open: the lifecycle rule (L2 above), and the `appliesTo` check, which is cohort-wide in `build_scores` but limited to ranked rows in the `value_v3` commands (L6 above).

**The findings.**
- **L1:** O110's launch and schedule bounds are typed by hand and unchecked, and the build's own derivation check would enforce a wrong one by unflagging routes.
- **L2:** E92's earliest-day definition, the fault-window clause and every "limit or price" blocking definition lag O110 and O111. Line 152 also carries a displaced clause, a provenance tag and stale citations.
- **L3:** line 55 claims every documented change is recorded, but OpenAI's Day 1–3 posts and global resets, user-detected Claude changes and the unlisted Claude plans are unresolved, and readings that span a reset still count.
- **L4:** the figure check does not guard change dates; r148's stale sentence passes it.
- **L5:** a non-null basket label naming another configuration's chart row passes the build.
- **L6:** the `appliesTo` check differs between commands, and `aaUncountedNotes` lacks class, factor and reason and misattributes chart-level notes.

All six are latent or textual. None moves a score, rank, label or cell verdict.

Under O56 this round is clean: it has no Medium or higher finding. I89 was clean too. If the ledger records this round as clean, the Claude Opus 5.5 max rung has two consecutive clean rounds (I89 and I90) and is complete.

VERDICT: HAS FEEDBACK
