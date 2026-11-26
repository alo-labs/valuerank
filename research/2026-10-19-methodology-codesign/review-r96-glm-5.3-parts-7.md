0. Read check

Part 7 (draft-r178-part-7-of-15.md) — read to its end.

First line: "- Assumptions: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, a transfer with its donor measurement identified; neither identifies M_W."

Final sentence: "Domain validity is separate from evidence completeness."

Part 8 (draft-r178-part-8-of-15.md) — read to its end (it ends mid-table, inside the LiveBench 2.0 leaf row).

First line: "- Scoring with frozen, per-basis anchors in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1);"

Final sentence: "the release's weighted mean of the seven category scores to two decimals (its _overall_weights: Long Agentic 2, Coding 1.5, Design 1.5, the others 1), as LiveBench's site computes it, anchors 0–100 |"

Both parts were read to their end; the review proceeds. Where I checked external facts, I cite web sources; all other statements refer to the two draft parts.

1. Findings by severity

Critical

None.

High

The O71 end-user meter fits are acknowledged but never evaluated, while the Plan headline's "workload-unmatched: exploratory" label is declared structural. Part 7 (E131 token ontology) states that no admitted source provides category-specific burn evidence, and immediately notes that "the O71 record lists two end-user meter fits, for Claude Max and for Kimi's China-region tiers, not yet evaluated against those rules." This hurts the objective directly: the Plan ranking is a headline output, its exploratory label is the methodology's own admission that the cost side is not identified, and candidate public evidence that could point- or set-identify M_W for at least one route is sitting in the repository unevaluated, with no scheduled evaluation and no recorded reason. Recommendation: run the staged evaluation of both fits against E44/E105/O11 at the next release; publish a per-fit admission record (fit form, token count, workload compatibility, verdict); if one passes, update the identification yield (E61) and the label; if neither passes, record the failing rule so the "structural until such evidence exists" claim is itself evidence-backed rather than open-ended.

Medium

Plan anchor reference panels are structurally tiny, with no leave-one-out stability diagnostic. O157 sets Plan anchors over measured plan rows only (minimum two, E160/E184), and E164/E249 already concede the calibration is "unavailable" below two complete-evidence reference rows. Every Plan cost score and the Plan exchange rate (5.31 value points per cost doubling in the max-effort ranking) rests on what may be two or three references; one donor demotion or report expiry can move the entire Plan cost scale through a re-freeze. The draft has leave-one-component-out (E172) and leave-selected-out (E179) precedents but nothing for anchor references. Recommendation: publish a leave-one-reference-out sensitivity per basis and ranking: recompute c_L, c_H, the exchange rate and adjacent-rank orderings with each reference removed; flag when any single removal moves the exchange rate by more than 20% or reverses a headline-adjacent pair.

Bug Hunt scale maxima (O170) have no provenance disclosure, and the registered stress is magnitude-only. P_max and U_max are taken "over every run on the live board, any model or harness," recomputed each release, and O173 registers only a ±10% magnitude stress plus the swing class. A single anomalous run on an unusual harness (for example, an agent that mass-fixes unplanted defects via broad refactoring) can rescale every cohort row's z with no new evidence about those rows, and nothing in the published bugHuntScale says which run set each maximum. This hurts the objective because an 8%-weight (max-effort) / 12%-weight (AICD) leaf silently moves on out-of-cohort evidence. Recommendation: publish beside bugHuntScale the provenance of each maximum (run id, model, effort, harness, date, run count), and add a scale variant restricted to runs on E206-eligible harnesses (or cohort rows) as a sensitivity — this refines O170's disclosure without overturning the owner decision.

Ranked Plan rows excluded from the clip-gate population get weaker disclosure than unranked listed rows. O58 gives listed rows a full beyond-anchor record (basis, side, factor, factor-2 pass, rendered-frontier marker), and part 8 publishes a long such list. But O157's owner-assumption and API-fallback Plan rows — scored on anchors built from measured rows they may sit far beyond (the draft's own rationale says fallbacks cost an order of magnitude more) — appear only as outsideGate membership in scores.json. Their cost scores saturate at 0, so value-score differences among them collapse to quality only, and a reader of the Plan ranking cannot see how far off-anchor they are. Recommendation: extend the O58 disclosure fields to every outside-gate Plan row, and display the unclipped cost score beside the clipped one in the row output (the data release already keeps unclipped values).

Value scores are not comparable across bases or rankings, and the draft does not say so at the point of consumption. Because anchors are per-basis and per-ranking while quality (75%) is shared (O10), a cost doubling is worth 3.11 points (max-effort API), 5.31 (max-effort Plan), 2.71 (AICD API) and 4.11 (AICD Plan). These exchange rates are published, but a consumer comparing a value score of 80 in one ranking against 78 in another will misread the difference, since the same quality gap is worth different cost multiples in each. Recommendation: print a one-line comparability statement and the per-basis exchange rate beside each headline table (not only in scores.json), mirroring how the O8 exchange-rate disclosure is handled.

Low

The two statements about what data/v3_dual_run*.json currently holds conflict. The O157/E160 paragraph says the dual-run files "now hold the latest, the O163 anchor objects against the O170 re-freeze, anchor version v3-2026-11-01-a4," while the O132 paragraph says "the published dual-run files still describe the O65 move of 2026-10-25." Both cannot describe the current file set. Recommendation: reconcile the O132 paragraph (name the a4 dual run as current, or clarify the file naming/suffix convention) so the release record is internally auditable.

The OpenAI December 2026 shared-allowance change is correctly registered but has no due-date mechanism. The draft records the announcement (help center updated 2026-10-31, per the draft's capture; press coverage dates the help-center update to November 2) with per-plan sizes not yet published, deferring everything to the release at which it takes effect. External reporting confirms the sizes and reset schedule are indeed unpublished so far. Recommendation: give evidencePolicy.announcedChanges entries a nextCheck field so each release re-checks for published per-plan sizes and reset rules before December — otherwise the effective release must re-research under deadline, and O83's record typing (limit, reset) will be guesswork.
notebookcheck
+2

The O46 paragraph states the recompute tolerance (5 × 10⁻⁵, half a unit of the fourth stored decimal) and the ceiling formula twice in the same paragraph. Editorial only; collapse to one statement to avoid divergent copies on future edits.

The quality source-share statistic counts a leaf as AA-run even where a row's Terminal-Bench value is a tbench.ai gap fill. The share is computed "by the leaf's named source," and harness-mixed rows are marked (E229; today none). Vacuous today, but when a gap fill appears the 66%/34% split will overstate AA's share. Recommendation: add a reallocated source share (gap-filled rows moved to the filling party) as a sensitivity, computed only when at least one gap fill exists.

External checks that support the draft as written: LiveBench 2.0's Overall is indeed its own weighted mean of seven suites with Long Agentic 2×, Coding and Design 1.5×, others 1×, matching the leaf formula; and tbench.ai publishes one row per model and agent with cost and token columns, consistent with E225's one-row-per-model/effort/agent build check.
tbench
+2

2. Methodology design recommendations

Prioritized, all implementable from refreshable public data:

Evaluate the O71 meter fits now (addresses the High finding). Add to the release checklist: for each recorded fit (Claude Max, Kimi China-region tiers), publish an admission record against E44/E105 — fit functional form, metered token count, measured workload, capture date, verdict — and if admitted, recompute E61 yield, identificationYield.configurationBalancedYield, and the E321 label threshold. This is the single cheapest change that could upgrade the Plan headline's epistemic status.

Leave-one-reference-out anchor sensitivity. For each basis × ranking and each anchor reference row r: freeze anchors on references \ {r}; publish Δ(ln c_H − ln c_L), the new exchange rate (25 × ln 2 / Δln range, in value points per doubling), and the count of adjacent rank reversals among ranked rows; flag any single reference whose removal moves the exchange rate by more than 20%. Model it on E172's leave-one-component-out object so it slots into the existing diagnostic family.

O58-parity disclosure for outside-gate Plan rows. Extend the listed-row record schema (basis, side, factor, factor-2 pass, rendered-frontier marker) to rows in gates.clip.plan[].outsideGate, and surface the unclipped cost score in the Plan row output so saturated rows are interpretable.

Bug Hunt scale provenance and restricted variant. Publish bugHuntScale.maximaProvenance (planted and unplanted maxima: run id, model, effort, harness, date, N) and a companion scale z′ = 100·x/(P_max′ + U_max′) where the maxima range only over E206-eligible harnesses, printed beside the O173 ±10% stress.

Headline comparability footer. Beside each headline ranking and basis: "Value scores are comparable only within this ranking and basis; one cost doubling = X value points; one quality point = Y× cost." Data already computed; this is presentation only.

Announced-change due dates. Add nextCheck to evidencePolicy.announcedChanges entries and a build note when a check is overdue, so the December OpenAI change (and any like it) is re-researched on schedule rather than at effect time.

3. Questions for the owner

Are the two O71 meter fits (Claude Max; Kimi's China-region tiers) scheduled for E44/E105 evaluation, and does either fit publish enough (metered token count plus a described workload) to point-identify rather than merely set-identify M_W? The answer determines whether recommendation 1 is a label-changing event or a record-closing one.

Is O157's exclusion of owner-assumption and API-fallback Plan rows from the clip-gate population intended to limit only the hold, or also their anchor-distance disclosure? If the former, recommendation 3 is a pure disclosure addition; if the latter, it needs an owner decision.

Should the O170 board-wide maxima stay board-wide by intent (i.e., is a non-cohort run on any harness an acceptable scale-setter), or would restricting provenance disclosure to E206-eligible harnesses be acceptable? This decides whether recommendation 4 stays a sensitivity or becomes the primary scale.

4. Verdict

VERDICT: HAS FEEDBACK