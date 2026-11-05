# Internal review I76 — Claude Opus 5.5 (effort high) on draft r135

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r135`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r135 (seventy-fifth internal review, the first clean one at Opus 5.5 high after the restart) grades O88 routes as measured on the site, checks each same-model route's multiple and allocation regime against its donor, marks cross-effort rows in the measured-only tables, and extends E106 case (4), the displayed multiple and the E164 provenance list to every route kind. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "route kind. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end: O45–O90, E247–E270, I29–I75 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i75-claude-opus-5.5-high.md`, and how the ledger resolved it. L1–L4 were adopted. Recommendation 1 was adopted for route badges; recommendations 2 and 3 were recorded, not adopted.
- `draft-r135.md`, every line (1–174), in sequential chunks. The long lines (28, 34, 51, 53, 55, 57, 58, 63, 98, 135, 136, 152 and the revision history on 174) were read whole.
- A word diff of r134 against r135, for both the published draft and `draft-r135.src.md`. The body changed on lines 1, 51, 57, 58 and 174 only.
- The code and data diff of HEAD (5af313c): `plan_routes.py`, `value_v3.py`, `emit_docs.py`, `site/evidence.py`, `site/viewmodel.py`, the badge partial, `format.js`, scores.md, the site data and the tests.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- Eleven test files pass, 555 tests in all, with bytecode and the pytest cache off: `test_plan_reports_provenance.py`, `test_plan_admission.py`, `test_plan_routes.py`, `test_draft_figures.py`, `test_swe_tracks_selection.py`, `test_value_v3.py`, `test_emit_docs_main.py`, `test_publication.py`, `test_plan_view.py`, `test_site_viewmodel_units.py` and `test_site_templates.py`.
- `git status` was clean before I wrote this file.

**Arithmetic, recomputed from `data/scores.json`, for both rankings**
- Every row's API cost score is S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L)) on its own workload's anchors.
- Every row's value is 0.25 × S_C + 0.75 × Q̄. Every plan row's cost is the API basket cost ÷ its multiple (or the API cost on fallback), and its score and value follow the same formulas on the Plan anchors.
- Every anchor is cheapest reference ÷ 2 and dearest × 2.
- Every displayed quality is the weighted mean of its leaves with the `quality.TRACKS` weights. Max-effort: FC 15, TB 11, BH 8, Vibe 5, Migration 6, LiveBench 15 and the seven common leaves. AI Coding Daily: FC 21, TB 17, BH 12, AICD 10 and the seven common leaves.
- There were no mismatches.
- The exchange rate of 3.04 value points per doubling on the max-effort API basis follows from those anchors (ratio 297.5).

**Admission**
- Max-effort ranking: 8 components admitted, Coding Agent Index v2.0 priced for 8 of 9 rows, threshold 6, 255 feasible alternatives.
- AI Coding Daily ranking: 7 admitted, threshold 11, 127 feasible alternatives.
- Both match lines 31, 43 and 46.

**The I75 fixes**
- The site, `plans.json` and the five model pages now grade all 33 O88 routes "measured", as `rankings-aicd.json` already did. The badge reads "Measured".
- `_plan_evidence` names an O88 anchor setter "same-model measurement from another effort".
- scores.md marks the five AI Coding Daily calibration references ‡.
- `check_same_model_routes` now refuses a route whose multiple or allocation regime differs from its donor's. The new fixtures cover both.
- No route records `valueMultipleLower`/`Upper`, so leaving the range out of that check has no effect today.

**Plan evidence**
- `planAllowanceCells` holds 52 cells, 28 of them listed. None passes; Google AI Pro fails at 1.35×.
- `plan_reports.json` has 107 rows and 93 `notTabulated`.
- The registry has 13 SemiAnalysis routes, all dated 2026-10-06 with no stated measurement window.
- The change-detection outcomes and partition splits match line 55.

**Today's scenario labels**
- Max-effort: GPT-6.1 Sol (max) at the headline bar and DeepSeek V4.1 Flash 1017 (max) at the lower quartile.
- AI Coding Daily: Claude Haiku 5.5 (medium) at the lower quartile and Claude Opus 5.5 (medium) at the upper quartile.
- Every ranked row of both rankings is "compatible as captured" at the valuation gate.

**Probes.** These were run on in-memory fixtures only; no file was changed.
- `bar_labels` with an E222 row (finding L1).
- `change_flagged` on real transfer, O88 and exact candidates (finding L2).

**Not verified:** live web pages, the paywalled SemiAnalysis article, and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. An unverified-basis row (E222) can still receive a scenario-supported cheapest label. Only the interval path denies it one.**

*What the draft says:*
- E92 (line 135) defines one predicate, UniqueLabelEligible = bar competitor ∧ ¬provisional ∧ ¬blocker. A blocker includes "a row … on an unverified valuation basis (E222)". The predicate "is used by both unique-cheapest labels and by the interval frontier and bar labels".
- E222 (line 152) says such a row "can deny another row a confirmed label but never receives one".

*What the build does:*
- The interval path agrees. `_gated_box` marks the row's box label-denied, and `interval_outputs` lists it among the blockers.
- The scenario-label path does not:
  - `value_v3.bar_labels` (line 2991) removes only O29 rows (`GATE_NOT_IN_FORCE`) and provider-claimed rows from the candidates.
  - The candidates come from `intervals.cheapest_above_bar(...)["possibleCheapest"]`, which keeps label-denied boxes. That is correct for K_r.
  - The scenario panel sets `RowInputs.provisional` from the coverage rule alone (`row["summary"].provisional`, line 2866).
  - So `scenario_supported_cheapest` (scenarios.py line 391) computes `uniqueLabelEligible: True` for the unverified row.

*Probe:* I used the `test_value_v3` fixture world and set row `a`, then row `b`, to "valuation basis unverified".
- `interval_outputs` lists each as a blocker.
- `bar_labels` keeps each as a scenario candidate, and every kernel assignment reports `uniqueLabelEligible: True`.
- Each is refused only because its frequency happens to be low in the fixture. A row whose frequency reached 90% would be labelled.
- The existing test `test_unverified_and_change_flagged_rows_compete_without_labels` checks only the interval outputs.

*Status:* latent. Every ranked row of both rankings is "compatible as captured" today, and four scenario labels are issued.

*Change:*
- Build one `label_denied(row, basis)` function (O29, E222, E228, E233) and use it in both `interval_outputs` and `bar_labels`. Recommendation 1 below describes it.
- Add a fixture: an E222 row at a 100% scenario frequency gets no label, and its reading is "frequency only (label-denied row)".

**L2. A transfer or O88 route resting on a change-flagged donor is not an E228 blocker. The spec says its row takes the donor's stage and flag.**

*What the draft says:*
- E144 (line 57): a transfer "inherits the donor's … change-detection flags".
- The lifecycle table (line 153): "A transfer or an O88 same-model route takes its donor's stage". When the trigger is a detected change, the row "competes in the Plan interval outputs as a blocker that can deny another row a label but earns none (E228)".
- O89 (line 55): an O88 route "shares its donor's change flag".
- E92 includes E228 in blocker(i).

*What the build does:*
- `plan_routes.change_flagged` (line 309), which `interval_outputs` uses to collect the Plan blockers, reads only the route's own `changeDetectedOn`.
- No transfer (82) and no O88 route (33) carries that field. Only the 13 SemiAnalysis donors do.
- On the real registry at the cutoff, `change_flagged` gives:
  - `claude-pro-claude-sonnet-5-5-common-opus55-assumption` (expiry "possibly-superseded", `donorChangeDetectedOn` 2026-10-17): False.
  - `chatgpt-plus-gpt-6.1-sol-xhigh-common-gpt-assumption` (O88, donor flagged 2026-10-11): False.
  - `claude-pro-opus55-semianalysis`: True.
- `post_change_ranks` already reads `donorChangeDetectedOn` for O88 routes (the O89 fix). So the inheritance is implemented for O78 but not for E228.
- The test at `test_plan_routes.py:568` asserts that a route without its own field is not flagged, which is exactly how a transfer looks.

*Status:* latent. Transfers never identify M_W (E106 case 2), so they never reach Plan R_W. The practical gap is an O88 route once its donor has an identified M_W. Today no Plan row is interval-evaluable.

*Change:* have `change_flagged` use the donor's change date (the `donorChangeDetectedOn` the candidate already carries) for every route that has a donor. Add a fixture with an O88 route on a flagged donor, given an identified M_W, which becomes a Plan blocker.

**L3. No rule covers a controlled measurement taken inside a provider-acknowledged accounting-fault window. E270 screens only user reports.**

*The fault and the measurement:*
- The registry records a ChatGPT Pro 500 fault window of 2026-09-29..2026-10-16 (`reportEligibilityProfile.accountingFaultDays`). It rests on an OpenAI support e-mail: Pro 200 → Pro 500 upgrades "kept the allowance from your previous plan … We corrected the error on October 16".
- SemiAnalysis's Pro 500 figures (GPT-6.1 Sol 10.772×, GPT-6 Astra 13.91×) were measured under "the post-September 29 Codex schedule" and published on 2026-10-06. They therefore lie wholly inside that window.
- E270 excludes any report "on a day of a provider-acknowledged accounting fault", and the build applied this to DhAdaptive's Pro 500 report of 2026-10-09.
- E269 records OpenAI's E18 outcome and notes that the entitlement error was corrected. It does not record whether the selected measurement was taken on an affected upgraded account.

*Why it matters:* this Pro 500 figure is used in several places.
- It is GPT-6.1 Sol (max)'s selected route.
- It is a measured-only view row in the max-effort ranking.
- It is the O88 figure for GPT-6.1 Sol's other efforts.
- Through O45's lower-of rule, it is the multiple of GPT-6 Luna (max) on Pro 500, which sets the max-effort ranking's official Plan low anchor.

*Why it is probably unaffected, and still Low:*
- The figures are internally consistent with a correct Pro 500 entitlement. Per dollar, Pro 500 matches Pro 200 and Pro 100 for both models: Sol 10.42 / 10.55 / 10.772, Astra 14.485 / 13.22 / 13.91. An upgraded account holding Pro 200's allowance would show roughly 0.4× of that.
- The routes are already flagged possibly superseded from 2026-10-11 (O77).

*Change:*
- Record in E269, per controlled measurement, whether any acknowledged fault window overlaps its measurement and how it was resolved (here: the per-dollar consistency, and whether SemiAnalysis's account was an upgrade, if stated).
- Have the build fail when a controlled measurement overlaps a registered fault window on its plan without such a resolution.
- Question 1 asks what an unresolved overlap should do.

**L4. Four small stale or incomplete texts.**

- *Line 115 ("Plan measurement vs transport"):* it still reads "The Plan headline score uses M_W where identified, else M_observed (owner assumptions labelled by kind; O16 flag)". r135 completed E106's "Displayed multiple" (M_observed, the O88 same-model figure, the authorised transfer or the O46 quota ceiling), but this sentence omits the O88 figure. Point it to E106's list.
- *`plan_routes.admission_table` docstring (lines 469–472):* it still says case 4 is an "exact-route measurement on an unreconciled price basis" and that "identified" is for "exact-route measurements". The draft and the code now put every route kind, or its donor, in case 4, and an O88 route can be identified. I75 L3 asked for this docstring update.
- *`docs/site-data-contract.md` (line 9) and `docs/site-experience-plan.md` (line 61):* they still say the `measured` badge reads "User-measured". The site now says "Measured".
- *`check_same_model_routes`:* it compares the multiple and the regime but not `planPriceUsd`. The O88 record's own fee feeds comparator key (4) and the E166 amount M × F_gross. All 33 fees equal their donors' today.

  *What is new against the recorded I75 recommendation 2:* the fee is the one copied field that still reaches a published number.

  *Change:* add the fee to the equality check, or derive the record (recommendation 2).

## 2. Methodology design recommendations

1. **One label-denial function for every label path (L1, L2).**
   - Make `label_denied(row, basis) → reasons` the single implementation of blocker(i). It would cover O29 not-in-force, E222 unverified basis, E233 provider-claimed leaf, and E228 change-flagged on the Plan basis, with the flag inherited from the donor through E144 and O89.
   - Call it from `interval_outputs`, from `bar_labels` and its `blocker_safe` input, and from any future Plan scenario label.
   - Feed its result into the scenario panel's eligibility, which then stops reading `summary.provisional` alone.
   - Add a parametrised test over (blocker reason × label path: interval frontier, interval bar, scenario bar) asserting that no label is issued and the row still competes.
   - This is the label-side counterpart of I75's one-grade-function recommendation. Today two of the four blocker reasons are enforced in one path only.

2. **Derive the inherited fields of donor-backed routes in one place (L2, L4).**
   - Transfers and O88 routes now inherit from their donor in five places: the evidence date, the expiry stage, O78's change date, valuation compatibility and capacity status.
   - E228's flag and the fee are still read from the route's own record.
   - Add `effective(route, field)` to resolve these fields through the donor for every donor-backed route, and have `change_flagged`, `gross_cash` and the E166 amount use it.
   - Have the build check that no donor-backed route stores a value for an inherited field that differs from its donor's.

3. **Fault windows apply to every measurement object (L3).**
   - Hold accounting-fault windows in the registry as provider facts, not as report-eligibility details.
   - Test every measurement object (controlled, report, donor of a transfer) against them, with a recorded resolution: unaffected with a reason, flagged, or excluded.
   - Then E270's report rule and E18's controlled-measurement rule read one table.

## 3. Questions for the owner

1. **A controlled measurement inside an acknowledged fault window (L3).** When a provider acknowledges an accounting fault on a plan and that window covers a selected controlled measurement (today SemiAnalysis's ChatGPT Pro 500 figures, measured between 2026-09-29 and 2026-10-06 against a Pro 500 fault window of 2026-09-29..10-16), should the measurement:
   - (a) stay selected with an extra flag and a recorded resolution, as E18 flags a detected change; or
   - (b) be treated like a report on a fault day and leave the official selection until it is shown to be unaffected?

   Under (b) the GPT-6.1 Sol rows and the GPT Pro 500 transfers would fall to their next eligible route, and the max-effort ranking's Plan low-anchor setter would change at the next freeze.

## 4. Verdict

There are no Critical, High or Medium findings, and four Lows. The figure check exits 0, 555 tests pass, and the value, cost-score, anchor, plan-cost and quality arithmetic recomputes exactly in both rankings.

r135 carries I75 into the text and the build correctly:
- the site grades the 33 O88 routes "measured" everywhere;
- the same-model check refuses a changed multiple or regime;
- `_plan_evidence` names an O88 anchor setter;
- E106 case (4), "Displayed multiple" and the E164 list cover every route kind;
- comparator key (2) separates the exact configuration from another effort.

**The Lows:**
- L1 (latent): the scenario-label path does not deny a label to an E222 unverified-basis row.
- L2 (latent): E228's blocker test does not inherit a donor's detected change for transfers and O88 routes.
- L3: no rule covers a controlled measurement inside an acknowledged fault window. The Pro 500 figures are probably unaffected, but this is unrecorded.
- L4: four stale or incomplete texts.

None changes a score, rank, multiple, flag or label today.

Under O56 this round is clean. With I75, it is the second consecutive clean round at the Claude Opus 5.5 high rung.

VERDICT: HAS FEEDBACK
