# Internal review I81 — Claude Opus 5.5 (effort xhigh) on draft r140

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r140`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r140 (eightieth internal review, at Opus 5.5 xhigh, and owner decision O96) defers the O94 anchor exclusion to the next freeze so the anchor diagnostics are unchanged, writes O94 into E183, E186 and the anchor rules, makes every transfer follow its donor's replacing report pair, dates changes against the earliest possible measurement day in the expiry clock too, and publishes each O94 row's factor and cost range. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "cost range. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1834). That covers O45–O96, E247–E270, I29–I80 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i80-claude-opus-5.5-xhigh.md`, and how the ledger resolved it:
  - M1 became the next-freeze-only anchor exclusion.
  - L1–L5 are recorded as adopted.
  - Q1 became O96.
- `draft-r140.md`, every line (1–174), in sequential chunks: 1–17, 18–30, 31–40, 41–46, 47–50, 51, 52–54, 55, 56–57, 58, 59–62, 63, 64–87, 88–97, 98, 99–105, 106–116, 117–134, 135, 136–147, 148–151, 152 (two halves), 153–173 and 174 (three segments).
- A sentence-level diff of `draft-r139.src.md` against `draft-r140.src.md`. The hand-written changes are:
  - line 47 (O94 eligible until the next freeze);
  - the GPT bullet (O96);
  - E184 (a new freeze leaves out O94 rows);
  - E183's B_W;
  - E186;
  - E92/E228 (the earliest-day rule);
  - the fault-window sentence under the lifecycle table;
  - the r140 history entry.
- The HEAD commit (b3c51c2) diff: `plan_routes.py`, `value_v3.py`, `emit_docs.py`, both test files, AGENTS.md, the registry, README.md, scores.md, methodology.md and raw-data.md.
- Code read in full for the functions involved:
  - `plan_routes.py`: `grade_rank`, `post_change_ranks`, `evidence_grade`, `donor`, `evidence_date`, `expiry_status`, `change_flagged`, `check_same_model_routes`, `check_lower_of_routes`, `measurement_objects`, `measurement_span`, `in_fault_window`, `effective_measurement`, `rebase_lower_of`, `_rebased`, `rebase_transfer`, `route_candidates`, `admission_table`, `route_selection` and `plan_cost`;
  - `value_v3.py`: `_gated_box`, `aa_cost_caveat`, `caveat_factor`, `blocker_domain`, `api_boxes`, `plan_boxes`, `anchor_eligibility`, `anchor_population`, `freeze`, `assemble_for_release`, `interval_outputs`, `withheld_label`, `subset_interval_outputs`, `_comparison`, `displayed_cheapest`, `cost_removal`, `plan_amount`, `bar_labels`, `blocker_safe`, `configuration` and the route-candidate assembly;
  - `plan_admission.check_routes` and `anchors.anchor_object`.
- Data read or queried:
  - `data/scores.json` (both rankings);
  - `data/v3_frozen.json` and `data/v3_frozen_aicd.json`;
  - `data/v3_scenarios*.json` (their input hashes match scores.json);
  - `data/plan_cost_routes.json` (the Claude Pro routes, `evidencePolicy`, `o72Application` and `accountingFaultDays`);
  - `data/plan_reports.json` (107 rows, 93 `notTabulated`);
  - `data/source_rereads.json`;
  - the footnotes in `data/aa_frontier_capture.json`;
  - README.md, scores.md and methodology.md.
- The O71 record, spot-checked: the Google AI Pro cell (largest lower bound 11.4 ÷ smallest upper bound 8.47 = 1.35×) against `research/2026-10-25-plan-allowances/stage1-google.md`.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- 1,621 Python tests pass (e2e and js excluded; bytecode writing and the pytest cache off).
- `git status` was clean before I wrote this file.

**Arithmetic, recomputed independently from `data/scores.json` and `quality.TRACKS`.** There is no mismatch anywhere:
- displayed quality (9 + 16 rows);
- cost scores on each row's own workload anchors;
- API and Plan values and competition ranks (27 + 51 plan rows);
- every anchor, each the cheapest reference ÷ 2 and the dearest × 2, on all three workloads;
- exchange rates: 3.04 (4.06), 2.44 (3.25), 2.83 (3.77) and 1.85 (2.46).

**I80 M1 is resolved.**
- `diagnostics.frontierAnchors` rebuilds from 8 and 16 references. Its exchange rates equal the frozen ones and no rank changes on either basis, so line 36 is true.
- The E199 bar result equals the primary headline bar: the same confirmed and possible cheapest, and possibleQualifierN 5 / 9, confirmedQualifierN 4 / 8.
- The AI Coding Daily E205 Plan change (2.04 against 1.85) is a family-primary effect. No Claude family primary is ranked there, so it is not O94.

**O94 outputs**
- `aaCostCaveatFactor` is 5.0 on all three Claude Haiku 5.5 rows.
- The published cost ranges are $966.92–4,834.60, $70.85–354.24 and $45.91–229.55.
- `leavesAtNextFreeze` is set on the same three rows.
- The manifest has an O94 entry and an amended fault-window entry.
- In the interval outputs the Haiku rows are blockers.
- Scenario labels:
  - max-effort ranking: GPT-6.1 Sol (max) at 63.54 and DeepSeek V4.1 Flash 1017 (max) at 53.27;
  - AI Coding Daily ranking: Claude Opus 5.5 (medium) at 58.61, and none at 49.24 or 38.0.
- `expiry_status` now uses the earliest-day rule. In a probe, a change dated 2026-09-07 flags an undated measurement published 2026-10-06, and a change dated 2026-09-01 does not.

**Plan evidence**
- `planAllowanceCells`: 52 cells, 28 listed, none passing.

**Probes** (scripts in my scratchpad, using the repository's functions on the real route registry plus synthetic report routes):
- O96 with an admitted Opus 5.5 report pair on Claude Pro, under three registration variants;
- a change dated before a measurement's earliest possible day;
- the AA-footnote parser on six plausible notes;
- a next-freeze anchor preview.

**Not verified:** live pages, the paywalled SemiAnalysis article and the scenario draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. O96 made `effective_measurement` the donor rule for every transfer and O88 route. It is not the replacement predicate the comparator uses, so a donor model's own row and the routes resting on it can end up with different figures.**

*What the rules say.* O96 says every route resting on a donor measurement takes "the replacing report pair when one replaces the measurement under O78 or O92, else the measurement".

*How the comparator decides for the donor model's own row* (`post_change_ranks`). O78 replaces the measurement only when all of these hold:
- the measurement is flagged (expiry possibly superseded or expired);
- the change is not dated before the earliest day the measurement can have been taken (I78 L2, I79 L1, E228);
- the report route is a candidate for that configuration (its `modelIds` contain the configuration ID).

*How the routes resting on it decide* (`rebase_transfer` → `effective_measurement`). The function returns the first report route in registry order that:
- is on the same plan;
- lists the donor's configuration ID;
- has reports that all postdate the change.

It applies no expiry test and no earliest-day test.

*Probes.* Each case fails silently. None raises an error.
- **(a) A change dated before the measurement.** The donor is published 2026-10-06 with no window, so its earliest day is 2026-09-07. The change is recorded on 2026-09-01. A report pair dated 2026-10-20 and 2026-10-21 (5.0 and 5.1) is admitted. The release is 2026-10-25.
  - The donor model's row keeps the measurement at 10.0: expiry fresh, not flagged. That is correct under E228.
  - The transfer resting on it is rebased to the pair, at 5.05.
- **(b) A report route that does not list the donor's configuration.** The real registry is used, plus a synthetic Opus 5.5 pair on Claude Pro (30.0 and 31.0, dated after the 2026-10-17 change). The route is registered for `claude-opus-5-5-high` only. `check_routes` accepts it, because it maps the configuration to its AA family (O87).
  - Claude Opus 5.5 (max) keeps 58.9, flagged.
  - Claude Opus 5.5 (high) takes the pair, at 30.5.
  - Every Claude transfer (Sonnet 5.5, Haiku 5.5) keeps 58.9.

  One model therefore carries two multiples, against O89, and no transfer follows its donor, against O96. Registered for `claude-opus-5-5`, which is the configuration the cells name today, every route follows.
- **(c) Several report routes for one plan and model** (for example two passing units, I66 L2). The transfers take the first route in registry order. The donor's own row takes the larger multiple (comparator key 3).

*What is new against I80 L4.* I80 L4 raised the missing date checks and the registry-order choice. The ledger adopted only the base-route id. O96 has since widened the function's reach: it used to apply to the 40 lower-of transfers only, and now it decides every owner-named transfer and every O88 route. Case (b), the configuration-ID versus family key, is new.

*Status:* latent, because no report cell passes. But these are the first rules to fire when one does.

*Change.*
- Compute the effective figure from the comparator itself: per (provider, plan, model family), take the donor configuration's selected measurement object after `post_change_ranks`.
- Key report routes by family (the `families` map that `check_routes` already receives), or generate report routes from passing cells for every cohort configuration of the model.
- Break ties in comparator order.
- Add fixtures for (a), (b) and (c).

**L2. An O88 route that follows its donor to a report pair keeps the O88 grade, flag and amount type, although its figure is now the users' report pair.**

*The probe.* The real registry is used, with the Opus pair registered for `claude-opus-5-5`. Claude Opus 5.5 (high) on Claude Pro then selects its O88 route with:
- the pair's multiple, 30.5;
- grade "controlled", which ranks 2.75 (O90's cross-effort rank, above reports);
- the flag "same-model measurement from another effort (O88, O90)";
- the E166 amount kind "API-equivalent consumption measured on the same model at another effort";
- E106 case (3) with `crossEffort`, and the site's "Measured" badge.

When a report route also lists Opus (high), the comparator picks the O88 route over it although both carry the identical multiple. The published selection reason is "higher evidence grade".

*Why that is wrong.* The published provenance claims a SemiAnalysis measurement where the figure is the users' report pair. Values and ranks are unaffected, because the multiple is the same.

*Status:* latent.

*Change.* A route rebased under O95 or O96 takes its effective donor's grade and evidence label, for example "follows its donor's replacing report pair (O96)", or yields to the report route. Q1 asks the owner which.

**L3. The AA cost-note reading that O94 rests on can now fail open. r140 widened the factor parser.**

`aa_cost_caveat` treats any chart footnote containing "cost", "price" or "pricing" as an omitted pricing term. The r140 regex reads the first "N x/×/times higher/more/the". I ran it on six notes:

| Note | Read as caveat | Factor | Problem |
|---|---|---|---|
| Haiku's real note ("5x higher pricing on longer-context inputs…") | yes | 5.0 | correct |
| "…used 3x more tokens than its predecessor; its cost figure reflects this" | yes | 3.0 | spurious factor |
| "Pricing shown is for the batch API, which is 2x the speed…" | yes | 2.0 | spurious factor |
| "…1.5x higher output pricing … and 4x higher input pricing beyond 200k" | yes | 1.5 | understated: the admissible box is [C, 4C], not [C, 1.5C], so a narrower blocker box can admit a label E183 would deny |
| "Prices double beyond 200k tokens…" | yes | none | unresolved: fails closed, correctly |
| "…declined some tasks on safety grounds; cost is for completed tasks only" | yes | none | a completeness note (E37) read as O94: labels withheld and outputs unresolved |

I80 L2 cases produced "no factor", which fails closed. The widened parser turns several of them into a wrong but plausible factor, which fails open.

*Two smaller gaps in the same path.*
- The new `unconstructible` test requires `row["cost"]["workload"] == mainWorkload` whatever workload is being evaluated. A no-factor row on the subset workload is therefore silently dropped from the E190 subset output: `_gated_box` returns None and the row is listed as unevaluable. It is not made unresolved. The test also ignores whether the row's Plan route is interval-eligible (E183).
- `blocker_safe` returns False for any O29 or O94 row outside the main-workload boxes. That withholds every scenario label of the ranking, which is over-conservative.

*Status:* latent. The capture holds one footnote today, Haiku's.

*Change.*
- Use a reviewed register of chart footnotes, by exact text, each either "omitted pricing term, factor k" or "not a pricing omission", and stop the build on a new or changed footnote. This follows the O64 pattern.
- Where a note lists several factors, take the largest.
- Decide boxes and the unconstructible status with one predicate per (basis, workload).

**L4. Normative text not brought up to date, and one new inaccurate clause.**

1. **The fault-window sentence on line 55 still reads as in r138.** It says a measurement and every transfer on it stay flagged "until two concordant user reports for that plan admit a route, which then replaces it… (owner decisions O91 and O92)". It does not give O93's per-model scope or the O95/O96 follow-through. The ledger records I80 L5(d) as adopted for line 55, but only the manifest detail and the lifecycle sentence changed.
2. **E144 (line 58) contradicts O96.** It says a transfer names an "immutable donor measurement-object ID" and that a newer measurement "replaces the old donor only by being named". O96 rebases the effective donor at release time without any naming. I80 Q1 quoted exactly this clause; O96 answered it, but E144 was not amended. The owner decision governs, so no output is wrong.
3. **New in r140: line 47 says E64's rebuild uses "this rule", but it does not.** The clause says the diagnostics "that rebuild anchors by this rule (E64, E187, E205)" keep O94 rows. `cost_removal` (E64(b), and E172 through it) does not use the E160 rule. It builds anchors from every row with a cost on W∖TB, via `anchors.anchor_object`, without the completeness or valuation-gate tests. The clause is true for O94 today but false as a statement about the rule.
4. **E92/E228 (line 135) is one day off.** It dates an undated measurement's earliest day "30 days before publication". The code (`measurement_span`) and line 55 use the 30 dates ending on publication, which is publication − 29 days.
5. **Line 123's explanation of the counts is incomplete.** It explains why the interval counts can be lower than bar-currency reach only by subset-workload rows. In the AI Coding Daily ranking the lower-bar gap (13 against possibleQualifierN 11) is entirely the two O94 blockers, which are now B_W, not R_W. This is the remainder of I80 L1, which the ledger records as adopted.
6. **The BlockerSafe reading names the wrong cause for O94.** The E186 / `BLOCKER_UNRESOLVED` reading "superseded-price blocker unresolved" is also printed when the blocker is an O94 row.
7. **Line 63's eligibility sentence omits O94.** "The shared eligibility is complete cost evidence on every component and an E170 outcome of 1 or 2" leaves out the next-freeze O94 test, although the clause just before it states that test.

*Change:* amend each passage as described. For item 3, either say "E187 and E205" or give E64 and E172 the E160 population, which was I80's recommendation 3.

## 2. Methodology design recommendations

1. **One effective-donor function (L1, L2).**
   - The effective figure of a measured route on a plan is whatever the comparator selects for that model's donor configuration: the replacing pair, or the measurement.
   - Computed once per (provider, plan, model family) and read by O78, O92, O95 and O96 alike, it makes the donor's own row and its followers agree by construction.
   - A follower inherits the effective donor's grade, label, flags and amount type. Each plan row publishes `effectiveDonor` beside `rebasedFrom`.
   - Generate report routes from passing cells for every cohort configuration of the model (O87), so the outcome cannot depend on which configuration IDs an editor lists.
2. **A closed-world register of AA chart footnotes (L3).**
   - Register footnotes by exact text, each mapped to {omitted pricing term: factor k (the largest stated)} or {not a pricing omission, with a reason}.
   - Stop the build on an unregistered or changed footnote, as O64 does for Coding Agent Index rows.
   - This removes the keyword and regex heuristics, and with them the fail-open cases above.
3. **A next-freeze preview diagnostic.**
   - It rebuilds each anchor object with `anchor_population(..., freezing=True)`, rescores every row on it and runs the clip gate, labelled "effect of the next re-freeze (O94)".
   - What is new against I80's recommendation 1: since r140 the frontier-families diagnostic equals the primary outputs, so no published output now shows O94's pending effect.
   - Recomputed today, AI Coding Daily Plan basis:
     - c_L moves from $0.390 to $0.961;
     - the exchange rate moves from 1.85 to 2.04;
     - 31 of 51 plan rows change rank, by up to 7 places, across 12 configurations;
     - Claude Haiku 5.5 (medium)'s three plan rows would clip by factors 1.20–1.23. That is within the allowance (3 ≤ 5 rows, each under the factor-2 limit).
   - The max-effort ranking's anchors and the AI Coding Daily API anchors do not move.

## 3. Questions for the owner

1. **The grade of an O88 route after O96 (L2).** O89 and O90 rank an O88 route as a measurement (2.75, above reports) because it reuses SemiAnalysis's measurement of the same model. Under O96 the route takes the users' report pair once that pair replaces the measurement. Should it then:
   - (a) keep the O88 grade and label (as built);
   - (b) take the report pair's grade, labelled as following its donor's pair (recommended); or
   - (c) give way to the report route itself on every configuration of the model (O87)?

## 4. Verdict

There are no Critical, High or Medium findings, and four Lows.
- The figure check exits 0, and 1,621 Python tests pass.
- Quality, cost scores, anchors, values, ranks and exchange rates recompute exactly in both rankings.
- The I80 Medium is resolved: the frontier-families anchor diagnostic now equals the primary outputs, as line 36 says.
- O94's factor, range, manifest entry and blocker treatment, and the earliest-day expiry rule, do what the ledger says.

**The Lows:**
- L1 and L2 are latent defects in the code that makes routes follow their donor (O96, O78, O89).
- L3 is the AA-note heuristic that O94 depends on, now able to fail open.
- L4 is stale or inaccurate wording.

Under O56 this round is clean: no Medium or higher. It is the first clean round at the Claude Opus 5.5 xhigh rung since the restart at I80.

VERDICT: HAS FEEDBACK
