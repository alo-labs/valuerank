0. Read check

Both listed parts were opened through the GitHub connector at commit ce7c11f064d17d1f947ebf5e0389c366df0b335d and read to their end.

Part 3 (research/2026-10-19-methodology-codesign/perplexity/parts-r178/draft-r178-part-3-of-15.md)

First line: ## Cost (25% of the value score)

Final sentence: "Release assertion: the scored field is the basket sum, not cost per task, not AA's 7:2:1 blended price, not total Index cost."

Part 4 (research/2026-10-19-methodology-codesign/perplexity/parts-r178/draft-r178-part-4-of-15.md)

First line (opening of the single-line bullet): "- Matched-cost diagnostic (diagnostic only). C_i^match = Σ_{g∈G} ω_g P_ig over canonical execution families g (E55; e.g. FrontierCode, Terminal-Bench as executed by AA): quality-weighted complete benchmark passes (E24), with P_ig = cost of one complete deployment-equivalent pass of family g for configuration i …"

Final sentence: "Priced-mix coverage (share of quality weight whose leaves are priced in the basket) is published each release."

Both parts read fully; proceeding to the review of the cost section (part 3) and the matched-cost / Plan cost section (part 4).

1. Findings by severity

Critical

None.

High

Agent-deployment cost confound in the only ranking that admits the Coding Agent Index (Owner decision challenge, O123/O15). The draft states the vendor agent is "part of the configuration being costed" while the FrontierCode and Terminal-Bench quality leaves come from AA's own model runs, and that the index's cost share s_i spans 16–74% of basket cost in the max-effort ranking. The registered remedy (the S2 stress fitting log C = α_m + h_a) is explicitly "unevaluable while no model is listed under two agents (today: unevaluable)", and the draft itself concedes public evidence gives "no bound on an upward counterfactual." Why it hurts: up to three-quarters of the 25% cost component measures which *agent harness* ran the tasks (retry behaviour, harness token overhead), not the model, while the 75% quality component measures the bare model — so cross-model value-score comparisons in the leading ranking embed an unmeasured, unbounded agent effect, and cheapest-above-bar answers can turn on the agent rather than the model. Concrete change: add a bracket sensitivity that needs no duplicate listings — recompute value scores, ranks and bar answers with the Coding Agent Index component scaled by λ ∈ {0.5, 0.75, 1.5, 2}, i.e. C′_i = C_i + (λ−1)·A_i pushed through the clipped cost-score function with the row's own anchor object (per E323, never read off the share), publishing Δrank per row and which frontier/bar labels survive, as diagnostics.agentCostBracket. This is implementable from existing public data and refreshes routinely; the α_m/h_a decomposition remains the right tool once a two-agent model exists.

Medium

The 10⁻⁶ Index-reconciliation tolerance demotes three ranked rows over a 0.03–0.04% residual whose cause is unregistered (Owner decision challenge, O141/E209). The Claude Opus 5.5 rows reproduce AA's published total to within 0.03–0.04% — far below any cost materiality next to the 4.5-point quality noise margin — yet each becomes "unresolved", loses FullCost, interval eligibility and anchor references, and "its cause stays unregistered." Why it hurts: the completeness gate treats a sub-basis-point discrepancy as structural while O27/O25 classify far larger telemetry imprecision as cost precision in the scenario layer — an internal inconsistency that shrinks the interval-output population and the anchor pool (7 of 8 and 18 of 20 panels) for no reader-visible reason, and an unregistered cause can recur silently on other rows. Concrete change: (a) register the cause by reconciling the published Index total against AA's per-evaluation surfaces — per the catalog definition, totals are token prices times "tokens used across evaluations (excluding repeats)", so check whether the total includes a repeat, a non-costed run, or an evaluation outside the nine; (b) if the residual stays unexplained, add a materiality band (e.g. relative error ≤ 0.1% ⇒ "complete, residual disclosed", kept in K and FullCost, residual published in indexReconciliation), reserving "unresolved" for residuals that can no longer be defended as precision. Displayed costs stay as published either way.
artificialanalysis
+1

Per-configuration token-metering basis is unknown, weakening cross-row cost comparability (part 3, Cost boundary bullet). The draft states AA prices "provider-reported token counts or, where those are unavailable, counts from its canonical tokenizer (the basis is not published per configuration)". Rows may therefore be costed on different metering bases; a third-party canonical tokenizer can differ from provider metering by materially more than the 0.04% the Opus rows are being penalised for. Why it hurts: the value score's 25% cost leg and every cheapest-above-bar answer assume rows' costs are comparable; an unknown per-row basis mix is an undisclosed comparability risk that E176's printed metering mix does not resolve, since the mix shows token categories, not which counting basis each row used. Concrete change: add per-row basis classification to the E216 model-page capture checklist (ask or infer from AA's surfaces); until it is known, publish a symmetric cost-scale stress (±10% on rows with unknown basis) reporting whether any bar answer or adjacent-rank ordering flips, reusing the existing separability / noise-margin machinery (O128, E277).

Low

Matched-cost diagnostic thresholds are uncalibrated. R_i > 1.5, a >3-place rank difference, and the 40% priced-weight floor are stated without a rationale tied to the published separability threshold. Why it hurts: a diagnostic whose firing rule is disconnected from the noise/separability scale can either cry wolf on separable noise or miss material reversals. Concrete change: derive the rank threshold from the value-point separability equivalent (the ~3.3-point figure under E277's basis) or document why the fixed values were chosen, in the E103 diagnostic object's publication.

Subset-stratum label inconsistency (part 3, E190). "The max-effort ranking's 4-row Plan subset stratum reads 'undefined (one configuration)'." If the four rows are plan rows of one configuration, the label should say so (e.g. "undefined — one configuration across 4 plans"); if they are four configurations, the label is wrong. Concrete change: make the dispersion-status string carry both counts.

O40's "replaces that model's transfer at once" overstates detection latency. Detection runs through the per-release O130 figure-table re-read plus a weekly report-only search, so replacement actually occurs at the first release whose re-read finds the new row. Concrete change: state the latency bound in the O40 sentence so a reader does not infer continuous monitoring.

2. Methodology design recommendations

Prioritised, all implementable from routinely refreshable public data:

Agent-cost bracket sensitivity (pairs with the High finding). For each row i in a ranking admitting the Coding Agent Index: C′_i(λ) = C_i + (λ−1)·A_i for λ ∈ {0.5, 0.75, 1.5, 2}; recompute the clipped cost score against the row's frozen anchor object, the value score (25/75), ranks, and each bar/frontier label; publish per-row Δrank, the set of flipped labels, and the λ at which each flips (diagnostics.agentCostBracket). This complements E172's leave-one-out (which only tests λ = 0) and E323's one-sided removal bound with a two-sided mid-range stress; it requires no evidence that does not already exist.

Reconciliation residual registry with a materiality band (pairs with Medium finding 1). Keep E209's four statuses, but add: (a) a deterministic reconciliation step comparing the published Index total against the sum over all surfaces AA publishes for the row (the catalog's token-price definition gives the checkable identity — prices × tokens used, repeats excluded), logging the cause class (repeat, non-listed evaluation, rounding); (b) a band: relative residual ≤ 0.1% ⇒ status "complete, residual disclosed", row keeps FullCost and interval eligibility, residual and its sign stay in indexReconciliation. Reserve "unresolved" above the band.
artificialanalysis

Metering-basis disclosure and stress (pairs with Medium finding 2). Extend the E216 capture to record, per configuration, whether AA's cost used provider-reported counts or the canonical tokenizer wherever any AA surface discloses it; print a per-row basis flag (rows[].cost.meteringBasis: reported | tokenizer | unknown); run the ±10% symmetric cost-scale stress on unknown-basis rows and publish label survival beside the existing noise companions (O171, E337's pointwise framing).

Calibrate the matched-cost diagnostic to the separability scale. Replace the fixed 3-place threshold with the equivalent of the published separability threshold in value points, and state the 1.5× and 40% rationales inside the E103 object so future readers can audit them.

Two low-cost label fixes. Carry configuration-and-plan counts in E190's dispersion strings; reword O40's "at once" as "at the first release whose re-read detects it (≤ one release cycle, weekly report-only watch in between)".

3. Questions for the owner

Does AA disclose, on any surface currently captured (or capturable under E216), which configurations' Index costs use provider-reported token counts versus the canonical tokenizer, and any per-evaluation cost total for the Claude Opus 5.5 Index run that would let the 0.03–0.04% residual be registered? A yes converts recommendations 2 and 3 from sensitivities into direct registrations and changes their priority.

For the max-effort ranking's Plan subset stratum, are the four rows one configuration across four plans, or four configurations? The answer determines whether the E190 label is a wording fix or a build defect.

4. Verdict

VERDICT: HAS FEEDBACK