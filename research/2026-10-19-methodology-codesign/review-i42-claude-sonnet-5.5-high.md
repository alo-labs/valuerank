# Internal review I42 — Claude Sonnet 5.5 (effort high) on draft r100

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r100"
- Last line of the draft (the folded copy's final line, 949): "configuration (O54, E252). Instruction following has no weight while Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read in full: `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (through I41 and O59/O60), the whole folded draft (949 lines, in chunks of at most 250 lines), the root `AGENTS.md` as it stands in the repository (it already carries O57–O60 and the O58 clause), and the previous review `review-i41-claude-sonnet-5.5-medium.md` (so as not to repeat its points).
- Checked against repository data and code, not only against prose:
  - `data/scores.json` (max-effort ranking `v3`, AI Coding Daily ranking `v3Tracks.aicd`): rank separability (medians, adjacent and same-configuration pair counts, correlation grids, bands, tolerances, the n = 60 sensitivity), exchange rates, anchors, cost-influence and variance allocations, bar ladders, bar currency, displayed-record and noise-margin cheapest rows, admission objects, basket readiness (Coding Agent Index task-equivalents 258.9 to 297.2, 5 of 7 below 290, 869 of 870 attempts, coding share and unrewarded share medians), clip gates and `listedBeyondAnchors`, `listedIndicative` values, FrontierCode and Terminal-Bench cross-source panels, gap-fill sensitivity and bars, the one-row-per-family diagnostic, drift, `aaPlottedNames`, the cohort object, `releaseHold`.
  - `valuerank/value_v3.py` (`rank_separability`, `rank_bands`, `costTolerance`), `valuerank/publication.py` (the "added after selection" label), and that the research artifacts and identifiers the draft cites exist (`v3-frozen-2026-10-21-before-o47.json`, `add_track_searches.py`, the Subscription usage report issue form, `check_open_web`, `MIN_ALLOCATION_ROWS`, `costed_bar_ladder`, `sourceClocks`).
- Recomputed by hand and found correct (beyond what I41 listed):
  - the cohort decomposition: 29 = Haiku 5 + Opus 4 + Sonnet 2 + GPT-6 Luna 5 + GPT-6.1 Sol 4 + GPT-6 Astra 3 + six single-point families, and 18 frontier plus 11 near points (Haiku 3, Opus 3, Sonnet 1, Luna 5, Sol 4, MiMo 2 on the line);
  - the two rankings' leaf weights (60 + 20 + 10 + 10 in each; 18 + 14 + 10 + 5 + 6 + 5 + 2 and 21 + 17 + 12 + 10), the 72 / 28 and 78 / 22 source shares, the 14 and 11 leaf counts;
  - the 255 and 127 feasible alternatives, the ⌈2N/3⌉ thresholds 6 and 10, the two admission fixtures, the Clopper–Pearson endpoints;
  - the Plan rows resting on a transfer or ceiling (3 Sonnet + 3 Haiku + 4 Luna + 4 MiMo = 14 of 27; 48 of 50), the same-configuration pair counts 15 and 30 (27 − 9 would be 18 and 50 − 15 would be 35 if plan rows were contiguous, so the draft's "bands built forward only" straddle note for GPT-6 Luna (max) and GPT-6.1 Sol (medium) is exactly what the bands show), and that no configuration's own plan rows span its separation threshold (largest span 2.04 against 3.02);
  - the fixtures of the category-mix bound (the ratio product), the interior-witness tests, the 91.5 % uniform figure, and the lifecycle dates;
  - the one-row-per-family diagnostic (E205): ladders 49.8 / 60.7 / 61.1 (7 rows) and 42.8 / 49.2 / 52.8 (5 rows), exchange rates 2.95 against 2.83 and 2.10 against 1.89, the 8-row and 7-row moves.

I found no Critical, High or Medium finding. The draft's figures, its counts and its rules agree with the build and with AGENTS.md. Five Low observations follow; one of them (L1) is a stale phrase that I did not see in the ledger.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

None.

I looked specifically for what made earlier rounds non-clean: a "today" figure that is stale or wrong, a rule that disagrees with the build, a contradiction with AGENTS.md or an owner decision, and a rule two faithful implementers would resolve differently. I also looked for remnants of withdrawn rules (retention O30/O31/O33, DeepSWE, TiboTattle, the 27-row cohort); the only remnants are labelled history. Two things I examined and found sound:

- The per-pair separability test crosses anchor objects (MiMo-V2.6-Pro and DeepSeek V4.1 Flash 1017 are on the subset workload, the other seven rows on the main workload). I recomputed the API ordering: the two cross-object adjacent pairs have gaps of 0.79 and 1.97 against thresholds of 3.06 and 2.93, so neither is separable, and the single separable pair (GPT-6 Astra (max) against Claude Haiku 5.5 (max), 3.18 against 3.01) lies inside the main workload. The printed count therefore does not depend on a cross-object comparison today (see L4 for the wording).
- The E242 tolerance (2.35 and 5.28) and the 2^(threshold ÷ doubling) formula are right for the main-workload exchange rate that the build uses (see L3 for the subset rows).

**Low**

- **L1. A stale example in the E238 sentence contradicts O40 two sentences later.** In the Plan cost input bullet (folded lines 276–278) the draft says: "a change to the article at the same URL (for example a model's multiples added) is a scoped change detection (E18), its new measurements stay diagnostic until the owner re-selects the revised analysis". The next sentence, "Exact measurement added after selection (owner decision O40)", says that when the selected article adds an exact per-(plan, model) measurement it "replaces that model's transfer at once", and only "every other change to the article stays diagnostic". A model's multiples added to the article are exactly the O40 case, so the example names the opposite outcome. The first sentence entered at r85 (I25 M3) as an editorial answer; O40 was decided at r86 and the example was not revised. The precedence statement on page one (an owner decision governs an editor decision; a rule that amends another governs) resolves the clash in favour of O40, and the build implements O40 (`publication.py` labels "added after selection"), so no ranking is affected. But the example, read alone, invites the wrong implementation, and the weekly watch exists precisely to catch this event. Recommendation: replace the example with a case that really stays diagnostic ("for example a restated figure, a changed allocation note or an unrelated section") and add "except an exact per-(plan, model) measurement, which O40 below handles". Optionally add one fixture: the article adds a Sonnet 5.5 Pro multiple, which replaces the Opus-donor transfer on the same release, while a restated Opus 5.5 figure stays diagnostic.

- **L2. The Terminal-Bench cross-source panel is per ranking while the FrontierCode panel is cohort-wide.** E260 (I35 L3) moved the FrontierCode AA-against-Cognition comparison to every cohort configuration with both results "so both rankings use one panel and one offset". E229's Terminal-Bench agreement (AA's run against tbench.ai) is still taken over each ranking's own rows: 5 rows (τ_b 0.74) in the max-effort ranking and one row, GPT-6 Luna (max), so "undefined (panel too small)", in the AI Coding Daily ranking (`terminalBenchSameHarness.agreement.panel`). The five exact-effort tbench.ai matches belong to the same cohort and the same AA run whichever ranking is read, so the AI Coding Daily ranking prints "undefined" for a comparison that the cohort can make. It is a diagnostic and changes no score (O8, E229), and the draft states each panel correctly; the inconsistency is only in the panel policy. Recommendation: extend E260's reasoning to E229, estimate the Terminal-Bench agreement over every cohort configuration with both an AA run and an exact tbench.ai row, and print the same figure beside both rankings (today 0.74 on 5), or say in E229 why the Terminal-Bench panel stays per ranking.

- **L3. The E242 tolerance is stated as one number per basis, but a ranking has two exchange rates on the Plan and API bases.** The max-effort ranking scores MiMo-V2.6-Pro and DeepSeek V4.1 Flash 1017 on the subset workload, whose anchors give a different rate (Plan: $1.63 to $3,715.87 gives 25·ln 2 ÷ ln(2,280) = 2.24 value points per cost doubling against 2.44 on the main workload; API about 3.03 against 3.04). The build divides the median threshold by the basis's main-workload rate (`exchange[basis]`), giving 2.35, and prints it beside the Plan bands. The four MiMo rows are the ones marked † for the O46 ceiling and all sit on the subset workload, where the same arithmetic gives about 2.5. The draft says "value points per cost doubling" without naming the anchor object (E86 does say that subset rows use a different rate). The difference is small and the figure is a tolerance, not an estimate, so this is wording. Recommendation: say that the printed tolerance uses the main-workload rate and add one clause that a † row on the subset workload has its own (a slightly larger) tolerance, or print both.

- **L4. The separability and band statistics do not say that they range over adjacent pairs that can cross anchor objects.** E86 and the O17 label say "orderings across W and W_S are not identified", and the dispersion convention (E180) allows a whole-table statistic only as "displayed-table dispersion". The rank-separability count, the median threshold and the noise bands are whole-table statistics too: a band can contain rows from both anchor objects (API band 1–3 holds GPT-6.1 Sol (max) with the two subset-workload rows), and a pair is declared separable or not from a value gap across anchor objects. Today no separable pair crosses objects (see above), and an inseparable cross-object pair is a safe statement, so nothing misleads; but the same principle that governs the dispersion label would put a clause here. Recommendation: one sentence in the separability paragraph: "adjacent pairs and bands may span the two anchor objects of the max-effort ranking; a gap across objects is read on the displayed scale (O17), and today no separable pair crosses them".

- **L5. "Replaced by an end-user measurement as soon as one exists" does not say whether one report suffices.** AGENTS.md (O46) and the draft (E261, the MiMo bullet) say a tier's ceiling is replaced "by an end-user measurement for the exact model and tier as soon as one exists". The draft also says single-source routes are diagnostics (O11: a measured route needs a controlled measurement or at least two independent concordant reports within ±20 %) and its comparator grade list ranks only controlled measurements, concordant reports and owner-named transfers; it does not place the ceiling. A faithful implementer who finds one MiMo-V2.6 report could (a) replace the ceiling at once with a diagnostic-only route, which would send the row to API-cost fallback (O13), or (b) keep the ceiling until the report partition passes O11. Nothing arises today (no end-user report exists, and the 2026-10-22 research found none), and the draft's own grade list suggests (b), so I rate it Low. Recommendation: add to the MiMo bullet "an end-user measurement replaces the ceiling when it is an admitted route under O11; a single report is a diagnostic and the ceiling stays", and list the ceiling beside the owner-named transfer at grade 3 of the comparator. If the owner means (a), AGENTS.md would say so (see Question 1).

## 2. Methodology design recommendations

In priority order, all optional; none is needed for a clean round.

1. **Fix the E238 example (L1).** It is the only item that can lead a reader to the wrong Plan behaviour, and it is one phrase plus an optional fixture.
2. **Make the cross-source panels uniform (L2).** One cohort-wide panel for FrontierCode and Terminal-Bench, printed beside both rankings, removes the "undefined on 1 row" line and lets the AI Coding Daily ranking carry the 0.74 that the same AA run supports.
3. **Name the anchor object where a statistic is whole-table (L3, L4).** A single clause each; no number changes.
4. **State the single-report case for MiMo (L5)** once the owner confirms the reading.
5. **Carry forward, not for this round:**
   - The figure lint recommended in I39 (design 2): a test that every "today" number in the draft is generated from `scores.json`. This round I re-derived about forty such figures by hand and every one matched; a lint would turn that into a standing check and make the draft's long "today" passages safe to maintain.
   - The Bug Hunt √N sensitivity and the DeepSeek V4.1 Flash 1017 harness tie (7 runs each: DeepSeek's harness 42.7, Claude Code 39.1), already recorded for the owner.
   - The revision history above the body and the single long Output 1 bullet (I38 L4, I41 L2) stay presentation items for the final editorial pass.

## 3. Questions for the owner

1. For a MiMo-V2.6 tier, when exactly one end-user report of an API-priced billing period is found, should it replace the O46 quota ceiling at once (a diagnostic-only single-source route would then send the row to API-cost fallback), or should the ceiling stay until two independent concordant reports pass O11? My L5 recommendation assumes the second reading; the first would change the wording of the MiMo bullet and of the comparator's grade list.

## 4. Verdict

VERDICT: NO FURTHER FEEDBACK
