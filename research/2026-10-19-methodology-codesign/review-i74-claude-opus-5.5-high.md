# Internal review I74 — Claude Opus 5.5 (effort high) on draft r133

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r133`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r133 (seventy-third internal review, the first at Opus 5.5 high, and owner decision O90) counts an O88 route as measured evidence ranked between an exact-effort measurement and reports, and publishes the current wording of the Plan anchor panel rule. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "panel rule. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end: O45–O90, E247–E270, I29–I73 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i73-claude-opus-5.5-high.md`, and how the ledger resolved it (L1–L3 adopted; L4 and Q2 answered by O90).
- `draft-r133.md`, every line (1–174). I read a line-tagged copy in 14 sequential chunks of about 24 KB each.
- A word-level diff of r132 against r133. The body changed on lines 1, 13, 15, 16, 51, 55, 58, 59, 98, 105, 106, 114, 152, 154, 159 and 164.
- The code and data diff of HEAD (a26458a): `plan_routes.py`, `value_v3.py`, `draft_figures.py`, `emit_docs.py`, AGENTS.md and the tests.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- These seven test files pass, 417 tests in all, with bytecode and the pytest cache off: `test_plan_reports_provenance.py`, `test_plan_admission.py`, `test_plan_routes.py`, `test_draft_figures.py`, `test_swe_tracks_selection.py`, `test_value_v3.py` and `test_emit_docs_main.py`.
- `git status` was clean before I wrote this file.

**Plan rows** (`planRows`)
- Max-effort ranking: 27 rows, made up of 11 controlled, 10 transfers, 4 ceilings and 2 fallbacks.
- AI Coding Daily ranking: 51 rows, made up of 18 O88 rows graded "controlled", 26 transfers, 4 ceilings and 3 fallbacks.
- Flags: 21 and 44 rows are possibly superseded; 21 and 44 have an unverified valuation basis. 18 rows carry "same-model measurement from another effort (O88, O90)".
- These match lines 13, 15 and 169: 14 of 27 and 30 of 51 rows rest on an owner assumption.

**O88 routes against their donors**
- All 33 O88 routes have the same plan as their donor.
- Each has the same multiple and the same source model as its donor.
- Each donor is a SemiAnalysis measurement and is not itself a transfer.

**Comparator**
- `grade_rank` gives an O88 route `CROSS_EFFORT` = 2.75.
- `dominance_filter` uses `grade_rank`, so an O88 route can never set aside an exact-effort measurement.
- `post_change_ranks` demotes a flagged O88 route to 1.5.

**Scenario files**
- The owner-assumptions-off Plan panels are 13 rows (max-effort) and 21 rows (AI Coding Daily: 18 O88 rows and 3 fallbacks).
- The exclusions are 10 and 30 rows, each with a reason naming its kind, in S1, S2, S1 endpoint-heavy, S1M and S1T.

**Measured-only view**
- Its specification string reads "…controlled (exact effort, or the same model at another effort, O90)…", and its ID hash changed with it (3d83f764… → 9182e20c…).
- The AI Coding Daily view now has 5 rows, all O88: Claude Opus 5.5 (high), Claude Opus 5.5 (medium), GPT-6.1 Sol (high), GPT-6.1 Sol (medium) and GPT-6 Astra (high).
- Its E164 calibration is now evaluated: 2 reversals, largest value change 5.76.
- The official anchor provenance names an owner-named transfer for the low anchor and an API-cost fallback for the high anchor.

**Anchor policy**
- The published `anchorPolicy.planRule` carries the new wording in both rankings.
- The frozen objects keep the old text.

**Report evidence**
- `planAllowanceCells`: 52 cells, 28 of them listed. None passes; Google AI Pro fails at 1.35×.
- `plan_reports.json` has 107 rows and 93 `notTabulated`.
- Both O71 research directories are present.

**Admission table**
- Published `rows[].plan.admission` moved the 18 O88 routes from case 2 (in HEAD~1) to case 3.
- `plan_routes.admission_table('gpt-6.1-sol-high', …)` returns case 3 for all four of its routes.

**Published documents**
- I grepped README.md, methodology.md, scores.md, raw-data.md and the site data for O88, "same-model", "Provisional assumption" and the assumption enumerations.

**Not verified:** live web pages, the paywalled SemiAnalysis article and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. After O90, the governing admission table (E106) no longer classifies an O88 route. Its text attaches the O88 description to case (1), "→ not exact-route evidence, excluded", and E113's admission text, which r133 did not change, reads as excluding O88 routes from the measured-only view. The build and O90 do the opposite.**

*What the draft says now (line 58):*
- Case (1) is "execution-identity incompatibility (… or an effort not the configuration's for evidence other than a plan allowance, without an owner-named transfer; a user-report cell is effort-invariant, O87, and a controlled measurement serves its model's other efforts as an O88 same-model route, measured evidence under O90 that ranks below an exact-effort measurement) → not exact-route evidence, excluded".
- Case (2) now lists only owner-named transfers and O46 ceilings. In r132 it held the O88 routes.
- Cases (3) and (4) speak only of an "exact-route measurement".
- E113's admission is "exact-route measurement candidates of grade controlled or concordant reports".

So the one place where E106 describes an O88 route ends in "not exact-route evidence, excluded". In r132 the same parenthetical said "never as exact-route evidence" and case (2) admitted the route. r133 removed both and placed the route nowhere. A reader of the specification alone, which E106 says is the place every other section defers to, either excludes the 18 rows or cannot classify them. The same reader would also keep them out of E113's view, because the view admits only "exact-route measurement candidates".

*What the build does:*
- `plan_routes.admission_table` grades an O88 route "controlled", so it falls in case 3, "exact-route measurement whose target-workload transport is unidentified".
- The published `rows[].plan.admission` moved the 18 AI Coding Daily O88 routes from case 2 to case 3 in this release.
- The published `measuredOnlyPlanView.specification.admission` now reads "measurement candidates of grade controlled (exact effort, or the same model at another effort, O90) or concordant reports".
- The O88 rows are the whole of the AI Coding Daily measured-only view (5 rows) and of its now-evaluated E164 calibration.

The normative text, the owner decision (O90: the route "enters the measured-only view (E113)") and the published outputs therefore disagree on current results, not on a latent case. This is the same class as I46 M2 (stream membership "as built" not stated in the governing text).

*Change:*
1. In E106, move the O88 sentence out of case (1). Make case (3) read "exact-route measurement, or a measurement of the same model and plan at another effort (O88; measured evidence under O90, ranked by O89 below an exact-effort measurement), whose target-workload transport is unidentified". Keep case (1)'s plan-allowance exception as a plain clause that excludes nothing.
2. Fix E113's admission the same way, using the build's string.
3. Have "Displayed multiple" name the O46 ceiling beside "the authorised transfer".
4. Update the `admission_table` docstring ("2 owner-named transfer" → "2 owner assumption: transfer or ceiling"; case 3 names O88).
5. Add a fixture per E106 case that includes an O88 route (case 3) and a report cell pooled across efforts (O87, case 3). Have the figure lint fail when the draft's E106 case list and the published case numbers disagree on a route kind (see recommendation 2).

### Low

**L1. The published evidence labels still call every O88 route a "Provisional assumption". A second, legacy classifier escaped the single registry of I71.**

- `publication.plan_evidence_label` keys on the registry's legacy `evidenceClass`. All 33 O88 routes still carry `"evidenceClass": "user_assumption"`, `"confidence": "provisional"`, `"provisional": true` and `"numeratorKind": "applied_estimate"`.
- raw-data.md's route table therefore prints, on one line, "ChatGPT Plus $20 · same-model measurement, another effort (O88, O90) | … | **Provisional assumption**" (lines 603–605 and the other O88 rows).
- The site's `plans.json` and the O88 model pages (e.g. `site/data/models/gpt-6-1-sol-high.json`) publish `evidenceLabel: "Provisional assumption"` beside `planFlags: "same-model measurement from another effort (O88, O90)"`.
- methodology.md line 155, which emit_docs writes by hand, still defines the grades as "**controlled** measurements of the exact model, … owner-named **assumptions**". Its E166 list ("measured-workload capacity, observed eligible consumption…, assumed API-equivalent consumption for an owner-named transfer…, or identified target-workload capacity") omits both the O88 and O46 amount kinds the draft's line 152 lists.
- No score or rank changes.

*What is new:* I48 L5 found a stale route-table label for ceilings. This is the cause behind that class: `plan_evidence_label` is a second classifier, and neither the I71 registry nor the I73 lint (which reads only "owner-named transfer" enumerations) can see it.

*Change:*
- Derive `evidenceLabel` from `evidence_grade` and `OWNER_ASSUMPTIONS`, plus an effort-provenance attribute (recommendation 1).
- Give O88 routes their own `evidenceClass` (e.g. `same_model_measurement`) and drop "provisional"/"applied_estimate" from them.
- Generate methodology.md's grade and amount-kind sentences from the same registry.

**L2. The measured-only view and its E164 calibration do not show which measured rows were measured at another effort. In the AI Coding Daily ranking that is every row.**

- `_measured_only_view` gives an O88 row the same status as an exact-effort measurement ("measured, target-workload unmatched").
- `_plan_evidence` maps any "controlled" anchor setter to "controlled measurement", so an O88 anchor extreme would be reported as an exact measurement. This is latent: today's anchor extremes are a transfer and a fallback.
- Today the AI Coding Daily view is 5 of 5 O88 rows. Its evaluated calibration (2 reversals, both between two efforts of one model sharing one multiple) rests entirely on them.
- O90 decided that these rows count as measured. It did not decide that the view should hide their provenance. The official plan rows carry the O88 flag, but the view drops it.

*Change:* add `effortProvenance` (exact effort / same model at another effort, O88 / reports pooled across efforts, O87) to each measured-view entry. Use the same field for O87 report routes once a cell passes. Extend E164's provenance vocabulary with it.

**L3. Since O90, one hand-set registry boolean decides an evidence grade, and nothing checks it.**

`evidence_grade` returns "controlled" for any `user_assumption` route with `sameModelAcrossEfforts: true` and a controlled source. That one flag now:
- removes the route from the owner-assumption counts and † marks;
- keeps it in the owner-assumptions-off streams and the measured-only view;
- ranks it at 2.75, above concordant reports.

No build check confirms that the donor is the same AA family as the route's configuration, on the same plan, with the same multiple, and is itself a controlled measurement. Before O90 a wrong flag changed only a label; now it upgrades a transfer to measured evidence. All 33 flags are correct today (I checked each against its donor).

*Change:* derive `sameModelAcrossEfforts` from the donor relation (donor's family = the configuration's family, same plan, donor graded controlled and not itself a transfer, equal multiple), or fail the build when the flag and that relation disagree. Add a fixture with a mis-flagged cross-model transfer.

**L4. "From another effort" states something the source does not establish.**

- SemiAnalysis names no effort (`sourceEvidence.semianalysis` records none). E246 binds each bare-model figure to the max row by convention.
- The O88 flag ("same-model measurement from another effort") and comparator key (2)'s split between an "exact-effort" measurement (rank 3) and an O88 route (2.75) therefore rest on that convention, not on a known measurement effort. If SemiAnalysis ran Codex or Claude Code at a default below max, the "exact" row would be the cross-effort one.
- Immaterial today: one route per (model, plan) cell.

*Change:* word the flag and the key (2) clause so they carry the convention, e.g. "same-model measurement (effort not stated by the source; bound to the max row by E246)". Record in E246 that the rank-3/2.75 split is conventional until a source states its effort.

## 2. Methodology design recommendations

1. **One evidence-class classifier for everything published (L1, L2, L3).**
   - Every published grade, evidence label, amount kind, flag and provenance string should come from one function of `(evidence_grade, assumption_kind, effort_provenance)`.
   - Retire the legacy `evidenceClass`/`confidence`/`provisional`/`numeratorKind` fields as classifiers.
   - Add a lint that compares each `evidenceLabel` and route-table cell in scores.json, site data and raw-data.md with that function.
   - This removes, at the source, the label class seen in I48 L5, I70 M1 and here.
2. **A coverage test for E106 (M1).** Keep in code the enumeration of route kinds:
   - exact controlled;
   - O88 controlled;
   - reports at the exact effort;
   - reports pooled across efforts (O87);
   - owner-named transfer;
   - O46 ceiling;
   - API fallback;
   - diagnostic.

   Assert that each maps to exactly one E106 case, and render the draft's case list (or check it) from that table. An owner decision that moves a kind between cases then fails the check until the governing text moves with it.
3. **Effort provenance as a first-class attribute (L2, L4).** Record on every route and report cell whether its allowance evidence was observed at the configuration's effort, at another effort, or at an effort the source does not state. Then publish an exact-effort-only sensitivity of the measured-only view beside the O90 view. Today it would be empty in the AI Coding Daily ranking, which is itself informative.
4. **Derive, do not declare, the O88 relation (L3).** Treat `sameModelAcrossEfforts` like the Coding Agent Index pin after E267: computed from the donor graph, never typed.

## 3. Questions for the owner

None.

## 4. Verdict

There are no Critical or High findings, one Medium and four Lows. The figure check exits 0 and 417 tests pass.

r133 implements O90 and I73 L3 correctly in the comparator, the scenario exclusions, the measured-only view and the counts:
- the O88 routes rank at 2.75;
- the owner-assumptions-off panels keep the 18 O88 rows;
- 30 of 51 AI Coding Daily rows rest on an owner assumption.

**The Medium (M1):** the governing E106 table and E113's admission text were not carried along. As written, the specification attaches the O88 route to the "excluded" case and admits only "exact-route" measurements to the measured-only view. The build and O90 put those 18 routes in case 3 and in the view, and the published case numbers changed in this release.

**The Lows:**
- a legacy classifier still labels O88 routes "Provisional assumption" in raw-data.md and on the site (L1);
- the measured-only view hides effort provenance (L2);
- an unchecked boolean now decides an evidence grade (L3);
- the "another effort" wording rests on E246's convention (L4).

Under O56 this round is not clean (one Medium), so the Opus high rung's count restarts.

VERDICT: HAS FEEDBACK
