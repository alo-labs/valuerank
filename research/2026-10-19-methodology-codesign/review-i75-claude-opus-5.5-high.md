# Internal review I75 — Claude Opus 5.5 (effort high) on draft r134

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r134`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r134 (seventy-fourth internal review, the second at Opus 5.5 high) places O88 routes in E106 case (3) and the measured-only view, labels them as measurements in every published table, checks each same-model flag against its donor in the build, and says that SemiAnalysis states no effort. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "no effort. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end: O45–O90, E247–E270, I29–I74 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i74-claude-opus-5.5-high.md`, and how the ledger resolved it (M1 and L1–L4 adopted).
- `draft-r134.md`, every line (1–174), in sequential chunks. The long lines (51, 55, 58, 98, 152 and the 24 KB revision history on 174) were read whole.
- A word-level diff of r133 against r134. The body changed on lines 1, 58, 59 and 174 only.
- The code and data diff of HEAD (1d0c0cf): `plan_routes.py`, `publication.py`, `value_v3.py`, `emit_docs.py`, `methodology.md`, `data/scores.json`, the site data and the new test.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- Nine test files pass, 429 tests in all, with bytecode and the pytest cache off: `test_plan_reports_provenance.py`, `test_plan_admission.py`, `test_plan_routes.py`, `test_draft_figures.py`, `test_swe_tracks_selection.py`, `test_value_v3.py`, `test_emit_docs_main.py`, `test_publication.py` and `test_plan_view.py`.
- `git status` was clean before I wrote this file.

**Plan rows (`planRows`)**
- Max-effort ranking: 27 rows, made up of 11 controlled, 10 transfers, 4 ceilings and 2 fallbacks.
- AI Coding Daily ranking: 51 rows, made up of 18 controlled O88 rows, 26 transfers, 4 ceilings and 3 fallbacks.
- These match Output 1, the separability bullet and the limitations: 14 of 27 and 30 of 51 rows rest on an owner assumption; 2 and 3 are fallbacks; 21 and 44 are possibly superseded; 21 and 44 have an unverified valuation basis.

**O88 routes against their donors**
- All 33 routes have the same plan, multiple and source model as their donor.
- Each donor is a SemiAnalysis controlled measurement.
- All 33 carry an allocation regime.

**The new build check**
- `check_same_model_routes` passes on the real registry, with and without families.
- A probe on an in-memory copy (no file changed) shows it accepts an O88 route whose multiple I set to 99× (finding L2).

**Admission table**
- `admission_table` gives an O88 route case 3 with `crossEffort: true`, and gives a transfer case 2.
- A route on a "different" valuation basis is classified as case 4 before its grade is read, whatever its kind (finding L3).

**Measured-only view**
- Specification id `9182e20c…`.
- Max-effort ranking: 3 exact rows, each with `crossEffort: false`.
- AI Coding Daily ranking: 5 rows, all with `crossEffort: true`.
- The E164 calibration is evaluated in both rankings. The official anchor provenance names transfers at the low end and fallbacks at the high end.

**Scenario exclusions**
- Max-effort ranking: 10 transfers in each of the five owner-assumptions-off streams. The 4 ceiling rows are MiMo-V2.6-Pro's, which sit on the subset workload and so are outside the panel (E266).
- AI Coding Daily ranking: 26 transfers and 4 ceilings, each with a reason naming its kind.

**Bars**
- Setters: the max-effort ranking's headline bar is Gemini 4 Argon (high) and its lower quartile is MiMo-V2.6-Pro; the AI Coding Daily ranking's headline bar is MiMo-V2.6-Pro.
- possibleQualifierN / confirmedQualifierN at the headline bar are 5 / 4 (max-effort) and 9 / 8 (AI Coding Daily).
- Bar reach is 7/5/3 of 9 and 13/9/5 of 16, as line 123 states.
- E205's family-primary headline bars are 63.5 and 52.8.

**Separability**
- API: 8 and 15 adjacent pairs. Plan: 10 and 19, plus 16 and 31 same-configuration pairs.
- The narrow AI Coding Daily reading gives 3.25 (API) and 3.21 (Plan).
- The wide GDPval-AA reading gives 2.77 and 4.44.

**Report evidence**
- `planAllowanceCells`: 52 cells, 28 of them listed. None passes; Google AI Pro fails at 1.35×.
- `plan_reports.json` has 107 rows and 93 `notTabulated`.
- Both O71 research directories are present.
- `source_rereads.json` is present.

**Published surfaces**
- README.md, methodology.md, scores.md and raw-data.md describe the O88 routes as same-model measurements.
- `site/data/rankings-aicd.json` grades the 23 selected O88 route views "measured".
- `site/data/plans.json`, the plans page and five model pages grade them "Assumption" (finding L1).

**Lifecycle dates**
- I checked the SemiAnalysis lifecycle dates by hand: last Current day 2026-11-05, expired 2027-01-05, demoted 2027-02-04.

**Not verified:** live web pages, the paywalled SemiAnalysis article and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. The site still grades the 33 O88 routes "Assumption". Its badge text for that grade reads "Explicitly authorised assumption with no measurement". The I74 L1 fix changed the label, not the grade.**

*Where the grade comes from:*
- `site/viewmodel.py` grades each route in the plans page's route list (line 702) and in each model page's plan list (`_route_view` without a grade, line 600) with `evidence.route_grade(route["evidenceClass"])`.
- All 33 O88 routes still carry the legacy `evidenceClass: "user_assumption"`.

*What a reader sees:*
- `site/data/plans.json` gives every O88 route `"grade": "assumption"`.
- The plans page renders `badge-assumption … >Assumption<` on all 33 routes.
- So do the evidence notes on the five O88 model pages: Claude Opus 5.5 (high) and (medium), GPT-6.1 Sol (high) and (medium), and GPT-6 Astra (high). That is 18 badges. One of them is on the page of the AI Coding Daily Plan leader, Claude Opus 5.5 (high).
- The badge's hover text, from `plan_evidence_label`, says "Same-model measurement from another effort". The visible badge and the legend still say "Assumption — Explicitly authorised assumption with no measurement".
- The same routes are graded "measured" in `rankings-aicd.json` and "measured" in the README's Plan table. So the public outputs now give two grades for one route ID.

*Two adjacent badge issues from the same vocabulary (`partials/badge.html`, `format.js`):*
- The "measured" badge's visible text is "User-measured". It appears on every SemiAnalysis route (18 on the plans page) and now on the O88 rows. AGENTS.md requires SemiAnalysis results to be labelled "controlled subscription-account measurements with workload projections, not individual crowdsourced reports".
- The "estimate" grade, which `ROUTE_GRADES` maps concordant reports to, reads "Modelled — Owner estimate or projection anchored to a measurement". This is latent, because no report route passes today.

*Generated documents:* scores.md's AI Coding Daily section prints the E164 calibration but not the measured-only view table. The view's five rows are all O88 rows, so the `crossEffort` mark that I74 L2 added to scores.json is not shown to a reader of the generated documents. The specification cites only scores.json (E265), so the draft itself is consistent.

*Effect:* no score, rank or flag changes.

*What is new:* I48 L5 and I74 L1 fixed labels; this is the grade field and badge text, which a third legacy classifier (`site/evidence.route_grade`) still decides from `evidenceClass`.

*Change:*
- Grade every route view from the build, using `evidence_grade` with the same-model flag, as `_route_view` already does when it is passed a grade.
- Rename the badges to the methodology's grades: "Controlled measurement", "Controlled measurement, another effort (O88)", "Concordant reports", "Owner assumption: transfer / O46 ceiling", "API fallback".
- Add a site-data lint that every route view's grade equals the build's grade for that route ID (recommendation 1).

**L2. `check_same_model_routes` does not check the multiple, so a mis-typed O88 multiple would be published as a measurement. The E220 regime check does not cover O88 routes.**

*The multiple:*
- I74 L3 asked the check to require an equal multiple. The built check tests the donor's kind, plan, model family, configuration and source model, not the multiple.
- On an in-memory copy of the registry I set `chatgpt-plus-gpt-6.1-sol-xhigh-common-gpt-assumption` to 99×, and the check passed.
- `evidence_grade` would grade that route "controlled". The comparator ranks it at 2.75, it enters the measured-only view and the owner-assumptions-off streams, and the Plan table prints a multiple nobody measured as "same-model measurement".

*The regime:*
- `check_allocation_regimes` (E220) requires a regime only when `valueMultipleKind ∈ CONTROLLED_KINDS`. O88 routes are `user_assumption` by kind but "controlled" by grade since O90, so an O88 route without a regime would pass.
- E220 says every controlled measurement records its regime.

*Status:* latent. All 33 routes equal their donors' multiples and all carry regimes.

*Change:* add to the check that the route's multiple, its `valueMultipleLower`/`Upper` where present, its fee and its allocation regime equal the donor's. Add a fixture for each. Better still, generate the records (recommendation 2).

**L3. Three governing statements still describe exact-route evidence only, while the build treats the other kinds too.**

*E106 case (4):*
- The draft reads "exact-route measurement whose valuation basis cannot be reconciled".
- `admission_table` tests valuation before grade, so a transfer or an O88 route on a "different" basis is case 4 as well.
- E144's own fixture already sends a transfer there ("donor with an unreconciled valuation basis → transfer case 4").

*"Displayed multiple":*
- The draft reads "M_W when point-identified, L_W when set-identified (E74), otherwise M_observed or the authorised transfer", which omits the O46 ceiling.
- I74 M1 asked for this (its item 3); the ledger records M1 as adopted but the clause is unchanged.

*The anchor-provenance vocabulary (E164):*
- The draft's list is "controlled measurement / concordant reports / each owner-assumption kind by name / API-cost fallback".
- `value_v3._plan_evidence` would report an O88 anchor setter as "controlled measurement".
- I74 L2's adoption covered the view rows, not this.

*Status:* all three are latent today. No route is on a "different" basis, and neither anchor extreme is an O88 row.

*Change:*
- Case (4): "a measurement, or an owner assumption through its donor, whose valuation basis cannot be reconciled".
- Add "or the O46 ceiling" to "Displayed multiple".
- Add "controlled measurement at another effort (O88)" to E164's provenance list and to `_plan_evidence`.
- Update the `admission_table` docstring's "identified … exact-route" accordingly.

**L4. Comparator key (2) separates its first two grades by "of the exact model", but an O88 route is a measurement of the exact model too.**

- Line 51 reads "controlled measurement of the exact model > a controlled measurement of the same model at another effort".
- Lines 55 and 58 and the revision history state the distinction as "exact-effort".
- I74 L4's adoption (line 59) says the split is between the max row E246 binds the figure to and the model's other configurations.

*Change:* write key (2)'s first term as "controlled measurement of the exact configuration (for SemiAnalysis, the max row E246 binds the figure to)".

## 2. Methodology design recommendations

1. **One grade function for every published surface (L1, L3).**
   - Today three classifiers decide what a reader sees about a route:
     - `plan_routes.evidence_grade` (the comparator, rankings JSON, README);
     - `publication.plan_evidence_label` (labels);
     - `site/evidence.route_grade(evidenceClass)` (badges on the plans page and model pages).
   - `check_allocation_regimes` and `_plan_evidence` add two more legacy decisions.
   - Make `(evidence_grade, sameModelAcrossEfforts, assumption_kind, fallback)` the only input to:
     - every grade;
     - every badge, with the text taken from the same registry as `OWNER_ASSUMPTIONS`;
     - every label;
     - every anchor-provenance string;
     - every gate that asks "is this a controlled measurement".
   - Retire `evidenceClass`, `valueMultipleKind`, `confidence`, `provisional` and `numeratorKind` as classifiers.
   - Add a lint that compares the grade of every route ID that appears in `site/data/*.json`, scores.json and raw-data.md with the build's grade.
   - This class has now been found in I48 L5, I70 M1, I74 L1 and here.

2. **Derive O88 routes; do not store them (L2).** The owner authorisation (O88) is a rule over (donor route, model family, cohort efforts).
   - Generate each O88 record at build time from its donor: plan, fee, multiple and range, dates, allocation regime, source fields and change flag. The registry then holds only the donor and the rule.
   - A drifted multiple or regime then cannot exist, and `check_same_model_routes` reduces to "the donor exists and is controlled".
   - This completes I74 recommendation 4 ("derive, do not declare").

3. **An E106 coverage table in code that includes valuation outcomes (L3).** Enumerate every (route kind × valuation status) pair:
   - route kinds: exact controlled, O88 controlled, reports at the exact effort, reports pooled across efforts (O87), transfer, O46 ceiling, API fallback, diagnostic;
   - valuation statuses: release, revalued, unverified, different.

   Assert each pair's case. Render the draft's case list from the table, or check the list against it. The case (4) and "Displayed multiple" gaps then fail the build instead of waiting for a reviewer.

## 3. Questions for the owner

None.

## 4. Verdict

There are no Critical, High or Medium findings, and four Lows. The figure check exits 0 and 429 tests pass.

r134 carries I74 M1 into the governing text correctly:
- E106 case (3) and E113's admission now name the O88 route, matching the build's case 3 and the view's published admission string;
- the measured-only view marks each row's `crossEffort`;
- raw-data.md, README.md and methodology.md describe O88 routes as same-model measurements.

**The Lows:**
- the site's grade badge, which a legacy classifier still decides, shows "Assumption" on every O88 route on the plans page and on five model pages, and the badge text "User-measured" mislabels SemiAnalysis routes (L1);
- the new same-model check omits the multiple, and the regime gate omits O88 routes (L2, latent);
- E106 case (4), "Displayed multiple" and the E164 provenance list still describe exact-route evidence only (L3, latent);
- one comparator wording (L4).

None changes a score, multiple, flag, stream membership or rank today.

Under O56 this round is clean. It is the first clean round at the Claude Opus 5.5 high rung since the count restarted at I74.

VERDICT: HAS FEEDBACK
