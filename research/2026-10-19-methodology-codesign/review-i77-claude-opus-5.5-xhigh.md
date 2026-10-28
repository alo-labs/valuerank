# Internal review I77 — Claude Opus 5.5 (effort xhigh) on draft r136

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r136`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r136 (seventy-sixth internal review, the second clean one at Opus 5.5 high, and owner decision O91) removes controlled measurements taken in an acknowledged fault window from the official selection, denies scenario labels to rows on an unverified valuation basis, and lets transfers and O88 routes inherit their donor's change flag. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "change flag. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end: O45–O91, E247–E270, I29–I76 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i76-claude-opus-5.5-high.md`, and how the ledger resolved it:
  - L1, L2 and L4 were adopted.
  - L3 became owner decision O91.
  - Recommendation 3 was adopted through O91; recommendations 1 and 2 were recorded, not adopted.
- `draft-r136.md`, every line (1–174), in sequential chunks of at most 24,000 characters. The long lines were read whole: 28, 34, 43, 47, 51, 53, 55, 58, 63, 67, 98, 102, 106, 114–115, 135–136, 143, 152 and the revision history on 174.
- A word diff of r135 against r136, for both `draft-r136.md` and `draft-r136.src.md`. The body changed on lines 13–15, 17, 19, 55, 61, 63, 115, 169 and 174. Of these, only the O91 sentence on line 55 and the L115 wording are hand-written; the rest are generated figures.
- The code and data diff of HEAD (080ccaa): `plan_routes.py`, `value_v3.py`, `draft_figures.py`, `emit_docs.py`, the registry, AGENTS.md, the tests and the generated documents and site data.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- The full Python suite passes: 1,615 tests in `tests/` (excluding `e2e` and `js`), run with bytecode and the pytest cache off. The 12 core files (plan reports, admission, routes, figures, SWE tracks, value_v3, emit_docs main, publication, plan view, site units, templates and golden) account for 587 of them.
- `git status` was clean before I wrote this file.

**Arithmetic, recomputed from `data/scores.json` for both rankings**
- Every displayed quality is the weighted mean of its leaves with the `quality.TRACKS` weights.
- Every API cost score is 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L)) on its own workload's anchors.
- Every value is 0.25 × S_C + 0.75 × Q̄.
- Every anchor is the cheapest reference ÷ 2 and the dearest × 2.
- Every plan row's cost is the API basket cost ÷ its multiple (or the API cost on fallback). Its value follows on the Plan anchors.
- Every rank is the competition rank. GPT-6.1 Sol (max) on Plus and on Pro 100 tie at 7.
- There were no mismatches.
- The exchange rates on line 63 follow from the anchors: 3.04 / 2.44 (max-effort) and 2.83 / 1.85 (AI Coding Daily).
- The value-variance allocations on line 19 recompute as 106% / 27% and −96% / −19%.

**r136's generated figures**
- Plan rows: 24 for 9 configurations and 43 for 16.
- API-fallback rows: 2 and 3.
- Rows flagged possibly superseded or expired: 18 and 36. Rows on an unverified valuation basis: 18 and 36.
- Owner assumptions: 13 (9 transfers, 4 ceilings) and 25 (21 transfers, 4 ceilings).
- Separability: 0 of 8 and 1 of 15 API pairs; the AI Coding Daily Plan count is over 19 pairs of different configurations.
- The n = 60 reading (4.43→3.25 and 4.41→3.21), the GDPval wide reading (2.77/2.76 and 4.44/4.43) and the E242 tolerances (1.876 and 2.193 max-effort) all match.
- No configuration's plan rows straddle a band in either ranking.

**O91 in the build**
- `in_fault_window` makes 18 registry routes diagnostic: the 2 SemiAnalysis ChatGPT Pro 500 measurements, 10 transfers and 6 O88 routes.
- 11 plan rows leave the rankings: 3 max-effort and 8 AI Coding Daily.
- Each published admission entry for those routes is case 5.

**The I76 fixes**
- `bar_labels` drops an unverified-basis (E222) row from the candidates.
- `change_flagged` reads `donorChangeDetectedOn`. I probed it on the real registry: the Sonnet transfers, the GPT-6.1 Sol (xhigh) O88 routes and the GPT-6 Luna transfers are now flagged.
- `check_same_model_routes` compares the fee.

**Other checks**
- Today's scenario labels are unchanged from I76: max-effort GPT-6.1 Sol (max) at the headline and DeepSeek V4.1 Flash 1017 (max) at the lower quartile; AI Coding Daily Claude Haiku 5.5 (medium) and Claude Opus 5.5 (medium).
- Every ranked row of both rankings is "compatible as captured", reconciles its Index total (relative error ≤ 2 × 10⁻¹⁶) and has no partial component and no provider-claimed leaf.
- The only gap fills are AI Coding Daily's two Cognition FrontierCode fills.
- `planAllowanceCells` has 52 cells (28 listed) and none passes; Google AI Pro fails at 1.35×.
- The frozen anchor files equal `scores.json` `workloads`.

**Probes.** All were in memory only; no file was changed.
- `change_flagged` with a change dated after the release day (finding L2).
- `in_fault_window` with no date, and with a publication date after the window (finding L1).
- A hypothetical re-freeze of the max-effort Plan anchors without the O91-excluded references (finding L3).

**Not verified:** live web pages, the paywalled SemiAnalysis article and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. O91 changes this release's Plan tables, but the specification states it in a single clause inside the user-report eligibility profile. The governing classification, lifecycle, transition-reason and manifest rules do not carry it, and no published output says why a route left.**

*What r136 does today.*
- `plan_routes.in_fault_window` makes 18 routes diagnostic: SemiAnalysis's two ChatGPT Pro 500 measurements, 10 owner-named transfers and 6 O88 routes resting on them.
- 11 plan rows leave the Plan rankings: 27 → 24 max-effort and 51 → 43 AI Coding Daily.
- GPT-6.1 Sol (max)'s representative row moves from Pro 500 at 10.772× to Plus at 10.55×.

*Where the draft states O91.*
- One clause on line 55 states it. The clause sits inside the list of conditions under which a *user report* counts ("Report eligibility profile (O71 v1, E270)").
- A generated figure names the two measurements beside it.

*Where the governing text leaves it out.*
- **E106 (line 58)** is the table "Other sections refer to … rather than restating admission".
  - Its case (3), "measurement whose target-workload transport is unidentified, exact-route or an O88 route … → displayed and scored", describes the faulted Pro 500 measurement exactly.
  - Its case (5) is a closed list: "source-count, comparability (E102), concordance or expiry rules". O91 is not in it.
  - E106's predicate OfficialDisplayEligible defers to "the owner's evidence … policies", so a careful reader can reach O91 through it. But no case holds the result. A reader who applies the cases displays and scores the 11 rows the build removes.
- **E142 (line 152)** promises that "an eligibility-transition reason ('the evidence expired') is published separately from the comparator's selection reason". O91 is an eligibility transition, but no reason is published:
  - The candidate carries `faultWindow` (`plan_routes.py` line 477).
  - `_row_json` (`value_v3.py` line 2563) drops it from `rows[].plan.admission`. `faultWindow` occurs 0 times in `scores.json`.
  - The entry for `chatgpt-pro500-gpt61sol-semianalysis` reads only `case 5`, `officialDisplayEligible false`, `expiry "possibly-superseded"`. That is the same expiry as the selected Plus route beside it.
- **E212 (lines 154–164)** is "one table for the stages above". It has a row for O32's out-of-window reports but none for an O91 exclusion.
- **E63 (line 152)** says the active-rules manifest "lists its gates, flags and rules with their status" so readers see which rules bound. Its 20 entries have none for O91, although O91 fired.
- **Other sentences are now silently partial:**
  - line 59: GPT-6.1 Sol and GPT-6 Astra "take their own SemiAnalysis figure on every ChatGPT plan";
  - line 55: under O72 "the owner-authorised routes stay (the SemiAnalysis selection …)";
  - Known limitations (line 169) does not say that ChatGPT Pro 500 has no Plan row today.

*What a reader of the published outputs sees.*
- `methodology.md` (the published summary) and README never mention O91.
- `raw-data.md`'s route list shows the 18 routes as ordinary evidence.
- The site's model page shows the Pro 500 route as "Diagnostic only" with no reason, beside a "Measured" badge.
- The only trace is scores.md's anchor line, "GPT-6 Luna (max) on ChatGPT Pro 500 (not in the current table)".

*Why Medium.*
- This affects current results, not a latent case: a reader of the governing table, or of any generated document, cannot reproduce or explain why 11 plan rows are gone.
- It is the same class as:
  - I74 M1: E106 did not classify a route kind that a new owner decision had reclassified, on current rows.
  - I70 M1: published policy texts did not state a new owner decision that moved current routes.
- *New against the ledger:* O91 was decided after I76, so this has not been raised before.

*Change.*
1. **E106.** In case (5), add "or a controlled measurement dated inside an acknowledged accounting-fault window for its plan without a recorded resolution (O91); a transfer or O88 route resting on it follows it (E144)". In case (3), add "not excluded by O91".
2. **E142.** Name O91 among the eligibility transitions. Publish on every `rows[].plan.admission` entry and route alternative an `eligibilityTransition` reason code (expired/demoted, lapsed report donor, valuation different, invalid divisor, accounting-fault window with its evidence and days). Add a test that every case-5 entry carries at least one reason.
3. **E212.** Add a lifecycle row "In an acknowledged fault window (O91)":
   - trigger: dated inside a registered fault window, no `faultResolution`;
   - official score: the next eligible candidate on that plan, else no row on that plan;
   - route comparison: excluded;
   - interval eligibility: excluded;
   - label: "accounting-fault window (O91)".
4. **E63.** Add a manifest entry "accounting-fault windows (O91)", fired or vacuous, naming the measurements and the plan rows removed.
5. **Move the clause.** Take the O91 sentence out of the report-eligibility list into E142, leaving a cross-reference. Qualify line 59 and the O72 sentence. Add a limitation that ChatGPT Pro 500 is unranked while O91 holds.
6. **Generated documents and site.** Have `emit_docs` print O91 in the subscription policy, and raw-data.md and the model page mark each such route "excluded: accounting-fault window (O91)".

### Low

**L1. O91's dating can fail open: an undated controlled measurement is never tested.**

*In the code:*
- `in_fault_window` returns `None` when a measurement has neither a window nor a publication date. The new test asserts this (`tests/test_plan_routes.py` line 672: `sourcePublicationDate: None → None`).
- `expiry_status` dates the same record by its `validFrom` fallback. So an undated controlled measurement is never tested against a fault window, yet it still ages normally.
- E151 stops the build on an undated *report*. No check stops it on an undated controlled measurement or donor.
- The test compares strings, so a datetime window start on a fault's last day (e.g. "2026-10-16T13:00Z" against "2026-10-16") sorts after it and misses the fault.

*In O91's own wording:* "the latest it can have been taken" dates a measurement by its publication date. A measurement published after a fault window closed, with no stated window, therefore escapes the rule even if it was taken inside the window (probe: publication 2026-10-20 → not faulted).

*Status:* latent. All 13 controlled routes carry 2026-10-06.

*Change:* stop the build on a controlled measurement (or donor) with neither a window nor a publication date, and parse dates before comparing them. For the publication-date convention, see design recommendation 3.

**L2. `change_flagged` (E228) treats a change dated after the release cutoff as a detected change.**

- `expiry_status` counts a change only when `evidence date ≤ changeDetectedOn ≤ V`. `change_flagged` (`plan_routes.py` line 309) tests only that the date exists and that the stage is possibly superseded or expired.
- Probe:
  - I set `changeDetectedOn` = 2026-11-20 on the Opus Claude Pro route.
  - I built at V = 2026-11-10, where the route is 35 days old and so possibly superseded by age alone.
  - `change_flagged` returned True, so the route becomes an E228 blocker.
- This contradicts the lifecycle row ("when the trigger is a detected change or the reports (not age alone)") and E144's fixture ("a change detected after the release cutoff ignored").
- I76 L2 made the path reachable for every transfer and O88 route as well.
- *Status:* latent. Every recorded change is on or before V. It matters when a past release is rebuilt at its own cutoff, as E142's fixture requires.
- *Change:* have `change_flagged` and `expiry_status` share one predicate (change within [evidence date, V]). Add the after-cutoff fixture to `test_change_flag_is_inherited_from_the_donor`.

**L3. The frozen max-effort Plan low anchor rests on a row O91 removed, and the published provenance hides why.**

*The anchor and its provenance:*
- `v3-2026-10-25`'s main-workload Plan c_L = $5.835 is `gpt-6-luna@chatgpt-pro-500` ÷ 2. That is the owner-named transfer from the faulted Sol measurement.
- `measuredOnlyPlanView.calibration…officialAnchorProvenance.low` now reads `"evidence": "not in the current table"`. `_plan_evidence` had this as a defensive branch, and O91 now reaches it.
- E164 (line 58) promises the provenance as one of five kinds, and "not in the current table" is none of them. The frozen kind (owner-named transfer) and the reason it left (O91) are lost. Yet E164 exists to show how assumptions shape the anchors.

*Which anchor rule governs:*
- E184 (line 63) says both "evidence lost after freezing never rebuilds an anchor" and "any population or rule change is a new anchor version".
- O91 is a new rule that removed anchor references before any release. The draft does not say which clause governs.
- The 2026-10-21 precedent re-froze pre-release when policy changed.

*Effect:* re-freezing without the Pro 500 references moves c_L to $5.958 (`gpt-6-luna@chatgpt-pro-100` ÷ 2) and the exchange rate from 2.439 to 2.446 points per doubling. The largest value change is 0.066 points, with no order change. The AI Coding Daily and subset anchors are untouched.

*Change:*
- Record each reference's provenance kind in the frozen object at freeze, and publish it with a "left the table: <reason>" note.
- State in E184 which clause covers a pre-release owner rule that removes references (see question 2).

**L4. O91's "recorded resolution" has no evidence standard, so whether the Pro 500 rows return is left to editorial discretion.**

- Line 55 says only "until a recorded resolution shows it unaffected".
- The new fixture's example resolution is "scales with the fee" (`test_plan_routes.py`). That is the evidence the registry already holds:
  - Per dollar, SemiAnalysis's Pro 500 figures are 1.034× and 1.021× Sol's Pro 200 and Pro 100 figures, and 0.960× and 1.052× Astra's.
  - The fault's own signature (an upgraded account that kept the Pro 200 allowance) predicts about 0.40×: 4.17× for Sol and 5.79× for Astra.
  - DhAdaptive's report shows exactly that signature on an upgraded account.
- Yet no `faultResolution` is recorded.
- Because the specification has no test, the same evidence could restore the rows at one release and not at the next.
- *Change:* define the admissible resolutions in the specification and check them in the build (design recommendation 2). Question 1 asks the owner whether today's evidence qualifies.

**L5. Small stale texts.**

- *`plan_routes.admission_table` docstring:* it still ends '"identified" for exact-route measurements with an identified M_W'. The code assigns "identified" to O88 routes too.
  - *New against I76 L4:* the adopted fix changed case 4 but left this last clause.
- *Published subscription policy:* the policy in methodology.md and on the site's plans page is headed "as of 2026-10-08", from the registry's `asOf`. Its text states rules through O88 and O91 (2026-10-28).
- *Ledger O91 entry:* it says GPT-6.1 Sol (max) "is now represented by its Plus and Pro 100 rows". The build's representative is the Plus row alone (comparator key 4, lower gross cash). Pro 100 ties it in value and rank.

## 2. Methodology design recommendations

1. **One eligibility-transition record per route–measurement pair (M1).**
   - Have `route_candidates` return `transitions: [code, evidence]` instead of collapsing every exclusion into `grade = "diagnostic"`.
   - The codes would be `expired`, `demoted`, `lapsed-report-donor`, `valuation-different`, `invalid-divisor` and `accounting-fault-O91`.
   - From this single record:
     - E106 derives its case;
     - E142 publishes the reason;
     - E212 counts the rows per stage;
     - E63 reports fired or vacuous;
     - the site and raw-data mark each route.
   - A parametrised test (transition code × published surface) keeps them in step. This is the transition-side counterpart of the grade function adopted at I75.

2. **A typed, build-checked `faultResolution` (L4, question 1).**
   - Admit three resolution kinds:
     - (a) the measurer states that the account was not affected (e.g. a fresh subscription);
     - (b) the provider states it;
     - (c) a signature test: the faulted plan's per-dollar multiple lies within O11's 1.20 factor of the same source's multiples for the same model on unaffected plans, while the fault's documented signature (here, the previous plan's allowance at the new fee) lies outside it.
   - Store the kind, the evidence, the comparison plans, the ratios and the threshold. Have the build recompute (c).
   - Today (c) gives ratios of 0.96–1.05 against a signature of 0.40.

3. **Date a controlled measurement for O91 by an interval, not a point (L1).** *Owner decision challenge (O91's "latest it can have been taken").*
   - Use the stated window. Otherwise use [the start of the recorded allocation regime or schedule, the publication date]; for SemiAnalysis's ChatGPT routes that is [2026-09-29, 2026-10-06].
   - Test the whole interval against each fault window, and stop the build when neither end is known.
   - Today the result is identical. The interval reading closes the case of a measurement published after a fault ends.

4. **One change-date predicate (L2).** `changed_at_release(route, donor, V)` = a change date within [evidence date, V]. Use it in `expiry_status`, `change_flagged` and `post_change_ranks`.

5. **Anchor references keep their provenance (L3).**
   - At each freeze, store every reference's evidence kind, so a reference that later leaves the table still reports what set the anchor and why it left.
   - Decide once whether a pre-release owner rule that removes references re-freezes the anchors (as the 2026-10-21 pre-release re-freezes did) or counts as evidence lost after freezing.

## 3. Questions for the owner

1. **O91 resolution (L4).** SemiAnalysis's ChatGPT Pro 500 multiples per dollar are 0.96–1.05× its own Pro 100 and Pro 200 multiples for the same models. An upgraded account under the acknowledged fault would show about 0.40×, as DhAdaptive's report does. Should this signature test count as the recorded resolution under O91?
   - If yes, `faultResolution` is recorded on both measurements and the Pro 500 rows return: 27 and 51 plan rows, with GPT-6.1 Sol (max) back on Pro 500 at 10.772× (Plan value 62.61).
   - If no, which evidence would count: the measurer's or the provider's statement only?
2. **Pre-release anchors (L3).** Before the first v3 release, should the max-effort Plan anchors be re-frozen without the O91-excluded references, or should O91 count as evidence lost after freezing, so the frozen anchors stand?
   - A re-freeze moves c_L from $5.84 to $5.96 and changes values by at most 0.07 points, with no order change.
   - Either way, E184 should say which clause applies.

## 4. Verdict

There are no Critical or High findings, one Medium and five Lows. The figure check exits 0, 1,615 tests pass, and the value, cost-score, anchor, plan-cost, quality and rank arithmetic recomputes exactly in both rankings. r136 carries I76's three code fixes correctly, and the O91 exclusion itself is implemented as decided.

**M1.** O91 removes 18 routes and 11 plan rows today, but it is written only into the user-report eligibility list. It is missing from:
- E106's case table, which would still display and score those rows;
- E142's published transition reasons;
- the E212 lifecycle table;
- the E63 manifest;
- every generated document, so no published output says why ChatGPT Pro 500 has no row.

**The Lows:**
- L1: O91's dating fails open for undated measurements.
- L2: E228's flag counts a change dated after the cutoff.
- L3: the frozen Plan low anchor rests on a removed row whose provenance is lost.
- L4: no evidence standard for an O91 resolution.
- L5: stale texts.

Under O56 this round is not clean. It is the first round at the Claude Opus 5.5 xhigh rung.

VERDICT: HAS FEEDBACK
