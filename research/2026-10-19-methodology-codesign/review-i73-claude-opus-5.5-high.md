# Internal review I73 — Claude Opus 5.5 (effort high) on draft r132

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r132`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r132 (seventy-second internal review, the second clean one at Opus 5.5 medium, and owner decision O89) lets an O88 same-model route share its donor's precedence against reports, names every owner-assumption kind in the remaining lists and scenario exclusions, and adds a lint against hand-typed assumption lists. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "assumption lists. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`.
- `ledger.md` from "## Internal review I28" to the end. This covers O45–O89, E247–E270, I29–I72 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` in full.
- `review-i72-claude-opus-5.5-medium.md`.
- `draft-r132.md`, every line (1–174). I read it as a line-tagged copy in 13 sequential chunks of about 24 KB each.
- A line-level diff of r131 against r132. The body changed only on lines 1, 51, 55, 58, 60, 63, 98, 115 and 152.
- The code diff of HEAD (8f1ac41) in `plan_routes.py`, `value_v3.py`, `draft_figures.py`, `emit_docs.py` and their tests.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- These tests pass, 394 in all (bytecode and the pytest cache off):
  - `tests/test_plan_reports_provenance.py`
  - `test_plan_admission.py`
  - `test_plan_routes.py`
  - `test_draft_figures.py`
  - `test_swe_tracks_selection.py`
  - `test_value_v3.py`
- `git status` was clean before I wrote this file.

**Plan rows** (`planRows`)
- Max-effort ranking, 27 rows: 11 controlled, 10 transfers, 4 ceilings and 2 fallbacks. 21 rows are possibly superseded and 21 are unverified.
- AI Coding Daily ranking, 51 rows: 26 transfers, 18 O88 rows, 4 ceilings and 3 fallbacks. 44 rows are possibly superseded and 44 are unverified.
- Both match lines 13, 15 and 169.
- The registry has 137 (model, plan) cells, each with exactly one route.
- Every O88 route carries `sameModelAcrossEfforts` and `donorRouteId`.

**O89**
- `grade_rank` promotes an O88 route to the controlled grade.
- `post_change_ranks` reads `donorChangeDetectedOn`.
- The new fixture covers precedence and the post-change loss.

**Scenario files**
- Exclusion reasons now name each kind: 10 transfers in the max-effort ranking, and 26 / 18 / 4 in the AI Coding Daily ranking, in all five off strata.
- With owner assumptions off, the Plan panels have 13 rows (max-effort) and 3 rows (AI Coding Daily).

**Separability** (`diagnostics.rankSeparability`)
- 0 of 8 and 1 of 15 API pairs separate. Plan: 2 of 10 and 1 of 19, with 16 and 31 same-configuration pairs.
- The narrow AI Coding Daily reading gives 3.25 / 3.21. The wide GDPval reading gives 2.77 / 4.44.
- The noise margins are 3.70 and 5.87.
- The E242 tolerances are 2.19 and 5.24. They reproduce as 2^(2.763/2.44) and 2^(4.413/1.85).

**Allocations and exchange rates**
- Cost allocation is 106% / 21% (max-effort) and −96% / −25% (AI Coding Daily).
- Exchange rates are 3.04 / 4.06 and 2.83 / 3.77 (`exchangeRate`).

**Bars and admission**
- Bars are 53.27 / 63.54 / 64.94 over 9 rows (setters MiMo-V2.6-Pro, Gemini 4 Argon and GPT-6 Astra) and 38.00 / 49.24 / 58.61 over 16.
- Reach counts are 7/5/3 and 13/9/5.
- Qualifiers at the headline bar are 4 of 5 and 8 of 9.
- E205's family-primary headlines are 63.54 and 52.82.
- The admission thresholds are 6 and 11.
- The 4 configurations ranked in both rankings and the 9 excluded configurations, in their 5 classes, check out.

**Other checks**
- `valuationGate` is "compatible as captured" for all 9 and all 16 rows.
- Plan interval outputs are "unevaluable (E61/E67)" in both rankings.
- `planAllowanceCells`: 52 cells, 28 listed, none passing. Google AI Pro fails at 1.35×.
- `plan_reports.json` has 107 rows and 93 `notTabulated`. Both O71 research directories are present.
- tbench.ai has no configuration under two agents, so the harness band is correctly unevaluable.

**Published documents**
- I grepped `methodology.md`, `README.md`, `scores.md`, `raw-data.md`, the frozen anchor objects and `data/plan_cost_routes.json` for residual assumption enumerations.

**Not verified:** live web pages, the paywalled SemiAnalysis article and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. Several published strings still carry the transfer-only enumeration that I72 L2 records as fixed. The r132 lint cannot see them.**

The ledger entry for I72 L2 says "`anchorPolicy.planRule`, the separability bias string and methodology.md's two sentences say 'owner assumptions'". The bias string was fixed. These were not:

1. **`anchorPolicy.planRule` in both rankings, and methodology.md line 108.** Both still print "measured routes, owner-named transfers and API-cost fallbacks alike".
   - *The cause is new:* the published policy is read from the frozen anchor objects (`value_v3.py:2036`, `frozen["anchorPolicy"]`; `data/v3_frozen.json:247`, `data/v3_frozen_aicd.json:207`), not from `ANCHOR_POLICY`. Editing the constant at `value_v3.py:1137` changed nothing that is published, and no check compares the two.
2. **`measuredOnlyPlanView.specification.admission`.** It reads "exact-route measurement candidates … (no transfers, no diagnostics)" and renders into methodology.md line 157 and scores.md line 741. The draft's E113 says "no owner assumption of any kind". The build excludes O88 and ceiling rows: every AI Coding Daily O88 configuration reads "no measured route".
3. **methodology.md line 157, the next sentence** (emit_docs.py line 940). It says "Because the official Plan anchors include transfers and fallbacks". The AI Coding Daily ranking's Plan anchor references include 18 O88 rows and 4 ceiling rows.
4. **The `_measured_calibration` docstring** (`value_v3.py:2183`) still says "owner-named transfers and API-cost fallbacks (E160)".

*Why Low:* this is descriptive text only. The admission, anchors and exclusions the build computes are right.

*Why it matters:* this is the third consecutive round on the assumption-enumeration class (I71 L1, I72 L1–L2, now this). The r132 lint (`draft_figures.ASSUMPTION_LIST`) scans only the draft, and only the phrase "owner-named transfer(s)" listed beside another class.

*Change:*
- Render the anchor policy's descriptive text from a versioned registry, keyed by the frozen object's `policyId`/`version`. Add a check that the frozen object's policy ID and version equal the code's. That way the policy text is never copied into an immutable object.
- Build `D_measured.admission` and the methodology.md sentence from `plan_routes.assumption_kinds_text()`.
- Run the assumption-set lint over the emitted documents and the text fields of scores.json too, not only the draft. Widen its pattern to "transfers and fallbacks", "no transfers" and "owner-authorised transfer".

**L2. The draft still has assumption-set wording outside the new lint's pattern, including one normative rule that covers only transfers.**

1. **Line 152, E170 outcome 3 (normative).** For a row whose AA cost is at a superseded price: "an owner-named transfer needs a donor measurement valued on price records in force during the applied price's effective dates".
   - It is silent on an O88 route, which has the same donor dependence (E144).
   - It is also silent on an O46 ceiling. A ceiling is valued at the price records in force at V (I68 L2), so by construction it sits on a different basis from a superseded-price row. It would need revaluing at the applied price, or be diagnostic-only, as E138 says for an exact measurement.
   - This is latent: every ranked row is "compatible as captured" today.
2. **Line 159, the lifecycle table ("Possibly superseded" row, "Route comparison" cell).** Only "a controlled measurement flagged by a detected change yields to a concordant report pair…" (O78). Under O89 an O88 route yields the same way. E212 calls this table the one table for the stages, but it omits the O89 extension that lines 51 and 55 state.
3. **Line 106 (Specification layer)** still lists "owner-authorised transfer on/off". Line 98, changed in r132, now calls the same branch "the owner assumptions on/off".
4. **Line 114 (Θ).** It says "With transfers off, a Plan route that depends entirely on an owner-authorised transfer is 'unevaluable' in interval outputs". The rule covers any route that rests on an owner assumption. In fact all of them are unevaluable anyway, because no route has an identified M_W.
5. **Line 105.** "Plan transport … and owner-named transfer bounds".
6. **Line 53.** "Owner-named transfers (O4/O7) remain labelled assumptions" (O88 and O46 rows are labelled assumptions too).
7. **Line 58.** "neither identifies M_W" now follows a list of three kinds.

*What is new:* these sentences are not in I72's list. They escape the r132 lint because they use "owner-authorised", use the singular, or name no second evidence class.

*Change:*
- Rewrite item 1 for all three kinds: a donor-based assumption needs its donor on the row's basis; a ceiling is revalued at the applied price or is diagnostic-only.
- Add "(and an O88 route, O89)" to the lifecycle cell.
- Use "owner assumptions" in items 3–7.
- Widen the lint's vocabulary as in L1.

**L3. O89 is implemented and written more broadly than the owner decided. Against an exact measurement it would let an assumption win on multiple size. Latent.**

- **What O89 says:** an O88 route shares its donor's precedence "against reports for the same model and plan".
- **What the code does:** `plan_routes.grade_rank` returns `GRADE["controlled"]` for an O88 route in every comparison.
- **What the draft says:** comparator key (2) states, without that scope, that "an O88 same-model assumption ranks as its donor measurement does".

Suppose the selected analysis adds an exact effort-specific figure for, say, GPT-6.1 Sol (high), as O40's "added after selection" allows (E246 binds an effort-naming figure to that effort).
- The exact measurement and the O88 route would then tie on grade.
- Key 3 would choose the larger multiple.
- The assumption could therefore displace an exact measurement. That contradicts key (2)'s own order ("controlled measurement of the exact model > … > owner assumption"), E106 case (1) ("never exact-route evidence") and O40 ("replaces that model's transfer at once").

Today every (model, plan) cell has exactly one route (137 cells), so nothing differs.

*Change:* give an O88 route an intermediate grade rank, for example 2.5: above concordant reports (2), below an exact controlled measurement (3). O78's post-change demotion (1.5) still applies through the donor's flag. This satisfies O89 exactly. Add a fixture with an O88 route against an exact controlled measurement at the configuration's own effort, and reword key (2) to match. If the owner meant "equal to the donor everywhere", see Q1.

**L4. Cross-effort evidence is still treated asymmetrically outside the comparator. Latent.**

Under O87, a report route can rest entirely on reports at other efforts of the model. It is graded "reports", so:
- it enters the E113 measured-only view as "measured";
- it survives the owner-assumptions-off streams (E167);
- it would count as "concordant reports" in E164's anchor provenance.

An O88 route rests on a controlled measurement at another effort, the evidence O89 now ranks above reports. It is excluded from all three. O89 aligned precedence only, so "measured" in the measured-only view now depends on who measured the other effort, not on whether this effort was measured.

*Why Low:* no cell passes today, so no output differs, and both labels follow owner decisions (O87, O88).

*Change:* record the efforts a report route pools, and label a report route with no report at the configuration's own effort "reports at other efforts (O87)" in the measured-only view and its calibration. Alternatively, ask the owner (Q2).

## 2. Methodology design recommendations

1. **One assumption-vocabulary check over everything published (L1, L2).** The class has now appeared in three rounds. The owner's rule is to remove such a class at its source.
   - Keep the vocabulary in `plan_routes.OWNER_ASSUMPTIONS`.
   - Make `draft_figures` lint every rendered document (README.md, methodology.md, scores.md, raw-data.md) and every free-text field in scores.json and the scenario files, not only the draft.
   - Have it flag set terms ("transfers and fallbacks", "no transfers", "owner-authorised transfer", "transfers off") unless the sentence also names every kind or carries the generated kinds text.
   - Keep policy prose out of frozen objects: they should hold IDs and versions; the text comes from a versioned registry.
2. **A generated precedence table (L3; extends I72 recommendation 2 with something new).** Publish, beside the comparator, the pairwise winner table generated from `grade_rank`/`post_change_ranks` over all evidence kinds: controlled, O88, transfer, ceiling, reports and fallback, each with and without a detected change. A test should assert the intended order: controlled > O88 > reports > other assumptions, with O78's demotion. The O89 scope question then becomes a visible table cell instead of a comparator constant.
3. **Flag a degenerate Plan scenario panel.** With owner assumptions off, the AI Coding Daily ranking's Plan panel is 3 rows, all API-cost fallbacks (DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), Kimi K3.1 Pro). Its S1/S2/S1M/S1T Plan shares are therefore an API-cost ordering of three configurations, and "rank ≤ 3" is trivially 100%. The panel size is printed (I47 L7). A generated flag would make the meaning plain without changing any number: "Plan scenario shares with owner assumptions off describe API-fallback rows only".
4. **Optional: record the efforts pooled on every report route (L4).** This costs one field per route and makes O87's cross-effort reach auditable once a cell passes.

## 3. Questions for the owner

1. **(L3) O89's scope.** Should an O88 same-model route outrank only user reports (sitting between an exact controlled measurement and reports)? Or should it equal its donor in every comparison, so that an effort-specific exact measurement added later would tie with it and be decided by the larger multiple? The answer sets the comparator's grade for O88 routes and the wording of key (2).
2. **(L4) "Measured" across efforts.** Should a report route that rests only on reports at other efforts of the model count as "measured" in the measured-only view and survive the owner-assumptions-off streams? The alternative is to label it, as the O88 route is labelled, as evidence borrowed across efforts. The answer decides whether the measured-only view and E167 need an effort-provenance field.

## 4. Verdict

There are no Critical, High or Medium findings, and four Lows. The figure check exits 0 and 394 tests pass.

r132 adopted I72's three Lows at their main sites:
- O89 in the comparator, with a fixture;
- per-kind exclusion reasons in the scenario files;
- kind-complete lists on the lines I72 named;
- an assumption-list lint for the draft.

The remaining Lows are:
- published strings the fix did not reach, because the anchor policy text lives in the frozen objects (L1);
- assumption-set wording outside the lint's pattern, one sentence of it normative but latent (L2);
- O89 implemented more broadly than decided, latent (L3);
- a latent asymmetry in how cross-effort evidence is labelled (L4).

None changes a score, multiple, flag, stream membership or rank today.

Under O56 this round is clean: the first clean round at the Claude Opus 5.5 high rung.

VERDICT: HAS FEEDBACK
