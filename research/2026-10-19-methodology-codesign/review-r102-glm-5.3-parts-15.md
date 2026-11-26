0. Read check

Read both listed parts to their ends through the GitHub connector, in order, at commit 5c2ab13991d61e5a15c418407e9c9e95db001918. No other repository files were opened.

Part 15

First line:

Release tests. Omniscience vector above; Bug Hunt vector above; Index reconciliation (C_6 + C_HLE-Diamond + C_Omniscience + C_CritPt v2 reproduces AA's total within the E209 tolerance, the task counts taken from the registered v5 evaluations; the residual never enters C_W); Coding Agent Index fixtures (E82): the scored cost equals AA's pooled per-task-attempt mean × 290 (v2.0, O50); the raw telemetry sum and sum ÷ mean are preserved as diagnostics without requiring equality to 290 (fixture with unequal telemetry coverage, where mean × 290 differs from the sum and the row still scores and passes completeness); completeness has two predicates: a Coding Agent Index cost is complete when AA's missing- or declined-task markers are absent (O27), and an Index SDLC component cost also needs its row's Index reconstruction to pass (E209); aggregate/component exclusivity (an exactly reconciled decomposition leaves basket cost unchanged); repetition invariance (averaging extra evaluation repetitions does not multiply workload cost); workload migration changes W's hash and invalidates unreviewed Plan transport; basket persistence (a new cohort row with missing costs does not change W's hash); single clip predicate (all gate consumers call one function, with integer-boundary fixtures for several cohort sizes); split invariance (partitioning an execution family into accounting subcomponents leaves its pass cost and C^match unchanged; splitting a quality reporting leaf never creates or duplicates an execution-family weight — E55); kernel completeness (every stochastic input has executable parameters); price tests (E23): uniform price scaling cancels in Plan cost; arbitrary category-price changes cancel when measured consumption is proportional to the target-workload token vector; otherwise, with x the measured consumption, u the target workload's demand and F the gross cash, M(p) = p·x / F and the Plan cost is P(p) = F·(p·u)/(p·x), so a repricing from p to p′ multiplies it by (p′·u / p·u)·(p·x / p′·x) and triggers a transport identification recheck (E335, correcting the inverted ratio on reviewer 91; asymmetric two-category fixture: doubling the price of a category present only in the measured consumption halves the Plan cost); restoring a missing leaf moves correctly from S0 to S1; transfers-off never silently becomes API fallback in an interval output or a scenario panel (E167); a tighter quota cannot increase computed capacity; window-semantics fixtures above; adding an unrelated row cannot change common-panel diagnostics except via declared cohort-dependent quantities; a frozen bar does not force its setter as the answer (at freeze at least two population configurations reach H on displayed quality; E192), and each bar result publishes its count of R_W configurations that can qualify (E198a); cheapest fixtures (non-provisional and provisional singletons, unique cheapest, equal-cost tie → both in K_r; no self-comparison); interior-witness possible-frontier fixture (E43); completeness statuses (an AA declined- or missing-task marker → confirmed incomplete; an Index reconstruction that misses AA's total → unresolved; otherwise confirmed complete; the Coding Agent Index cost equals the per-task metric × 290); completeness (an AA-marked incomplete component fails FullCost and removes the row from R_W without changing its displayed score); session-start fixture (a schedule whose second burst starts a new session after the first session ends is feasible; capacity results carry a feasible schedule); interval decision statuses (an unresolved solve is never certified); widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic.

Final sentence, ending with a semicolon because the paragraph continues in part 16:

the model-page snapshot, the chart capture, the Coding Agent Index capture and the cost-chart capture are each at most 7 days from the snapshot, the build tests each of the last three against the release cutoff and the snapshot itself defines it (O65), and the build fails otherwise, and capture proximity alone does not show one AA revision, so the chart is also reconciled with the model pages on the fields both publish: each chart point linked to a captured page must carry that page's total Index cost (within 1%) and its displayed Index (the page's unrounded Index within half a display unit), and a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);

Part 16

First line:

a point without a captured page is captured within the window, its common revision unverified. Cohort capture age (E211): the AA chart and catalog capture that defines the cohort is at most 7 days old at the release cutoff. The refresh gate fails on an older capture, and on any near-frontier family that is neither rostered nor deferred by a dated, reasoned roster decision. Every plotted point in the capture keeps its exact model name, effort, fallback state and direct AA owner link, with the capture's observation time, so unscored rows keep them in the reconciliation inventory too. Each capture publishes the rendered-frontier entrants and exits against the previous capture, and the reconciliation report lists every frontier and near row with its rank status. Today the capture, the latest under Intelligence Index v5.0 (the 2026-10-31 capture was the first, O132), was taken at 2026-11-01T05:53:05Z, before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant; O65 had moved it from 2026-10-23T06:26:23Z and O47 from 2026-10-21T05:24:16Z). Its chart selects 89 catalog models and plots 82, far fewer than v4.3.2's. Against the previous capture (2026-10-30T22:15:18Z), on the rendered frontier no vertex entered or left. In the cohort, GPT-6.1 Terra at five efforts, GPT-6.1 Sol at low and Gemini 4 Carbon joined, and DeepSeek V4.1 Flash 1017, Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro, MiniMax-M3.1-Flash, GPT-5.6 Luna at low, Claude Haiku 5.5 at max and xhigh, Claude Sonnet 5.5 at xhigh and Claude Opus 5.5 at medium left the plotted frontier and near set and remain in this release's cohort as retained configurations under O145 (reviewer 88), no longer on or within the near gap of the rendered v5 frontier (O51); the 2026-10-23 capture's near set had grown by DeepSeek V4.1 Flash 1017 and MiniMax-M3.1-Flash, both then new to the chart; the capture's comparison record is in data/aa_frontier_capture.json. Tariff applicability (E141): each price record carries observed_at, effective_from, effective_until (only where publicly established), tariff_status (standard / promotional / grandfathered), applicability_conditions, scheduled_refresh_at (the next known effective boundary, refreshed on schedule independently of page diffs) and a source evidence ID; a release uses the prices applicable at its declared valuation timestamp (a mismatch with the prices AA applied is resolved by E170); a promotion with an unknown end keeps the applicable price in the primary ranking, flagged "promotional tariff", with a named S2 standard-tariff branch only where the standard tariff is publicly documented and the consumption ledger supports repricing; an AA note that its cost omits a tariff component (at O106 the Claude Haiku 5.5 rows: AA's note that their higher long-context pricing is not reflected in AA cost figures; the rows carrying one are listed in scores.json rows[].aaCostCaveat) is shown on the row as "AA cost caveat". Unknown boundaries stay unknown (no assumed dates). Valuation-basis gate (E170; failure action = owner decision O29): the release declares one valuation timestamp V, its release cutoff (the cutoff that also governs evidence clocks, E151). Every scored cost observation names the basis it was actually valued on, not the date ValueRank retrieved it: for an AA cost, the per-category prices AA applied to the exact configuration (its displayed prices at capture, reconciled p·d = C where AA publishes category costs, E157) and the price record they match; for a Plan measurement, the price records of the model line whose consumption it values (E138). A compatibility join of each observation's basis with the price records in force at V (E141) returns exactly one of four outcomes: (1) compatible as captured; (2) compatible after evidenced revaluation, which is exact only when every priced category and band with positive demand in the component moves by one common factor k (then C' = k·C for any demand mix; a category has zero demand only where a published category total shows it) or when E157's valuation sufficiency supplies the component's demand by category and band; (3) AA's applied price not in force at V (O29): the row keeps AA's cost at the price AA applied, flagged "AA cost at superseded price" (or "AA cost at standard price during a promotion", E141) with that price's effective dates, and stays in the value ranking; it earns no interval label of its own and competes in other rows' interval outputs over the hull of its published record and its current-tariff bound below, so it can block but never enable another row's label; its scenario outputs use its published record and carry the flag; it is never a reference in anchor derivation (E160) or in the measured-evidence calibration (E164); and its Plan cost divides only by a multiple valued on the same basis (E138's statuses are evaluated against the row's basis: an exact measurement valued at the new tariff is revalued to the row's basis under outcome 2 or is diagnostic-only; an owner-named transfer or an O88 same-model route needs a donor measurement valued on price records in force during the applied price's effective dates; when no route survives, the row falls back to API cost, flagged, O13). Such a row also publishes the structural current-tariff bounds, with r = price in force at V ÷ applied price over the priced categories and bands with positive demand (for P', positive demand or measured consumption): C' ∈ [C·min r, C·max r], because C'/C is a demand-weighted mean of the r; and, on the Plan basis, P' ∈ [P·min r ÷ max r, P·max r ÷ min r], because M'/M is a consumption-weighted mean of the same ratios (diagnostic only). Bound domain (E185): the ratios need a strictly positive applied price for every category or band that can carry demand; a category free under both the applied tariff and the tariff in force contributes zero to both valuations and is left out of the ratios (its demand constraints are kept), and zero demand is never inferred from zero expenditure at a zero price; a category whose applied price is zero and whose price in force at V is positive (a newly priced category) makes the bound unavailable, since v1 has no public per-component category demand to bound it (E157); a zero price in force at V makes min r = 0, so the API bound starts at 0 (an exactly repriced zero cost is "cost not scoreable (zero)", E109) and the Plan bound has no finite upper end. An unavailable side, or a lower ratio of zero, means the blocker's domain cannot be constructed, and the claims it could affect are "unresolved" (E183); a positive lower ratio with no finite upper end is a domain, [lower, ∞), like O98's factorless caveat, so a decision that a finite witness or the lower bound settles is decided and only the others stay unresolved (E339, on reviewer 95); fixtures: a newly priced category, a price falling to zero, a positive-price change (finite bounds). The release never computes one C/M across two bases, never holds for this reason and never moves V to an earlier date (O29). (4) Valuation basis unverified (E202): AA's cost reconciles with neither its displayed prices nor a registered price record, or AA displays no complete price vector. The row is flagged and stays ranked. It is anchor-ineligible and never earns a label. Competes at its published record (E222): when it has FullCost on W, it competes as a blocker in B_W (E183) at its published point (cost and quality bounds, no tariff hull), so it can deny another row a confirmed label but never receives one; like any blocker's, its own frontier and bar statuses read "withheld". Label denial is a property of the interval box, separate from the coverage-defined provisional status: the row stays in the bar population and the ladder, and UniqueLabelEligible requires both non-provisional and not label-denied (rows on a price not in force, E170 outcome 3, are label-denied the same way); because O25 protects the published record and a cheaper qualifying record must not be ignored; without FullCost it is listed among the unevaluable rows as an omitted competitor (E38). Today no ranked row is in this state: every ranked row's AA cost, in both rankings, is compatible as captured; the Plan measurement's own valuation status is E138's, counted with the Plan rows. In short, an AA basis that cannot be identified is flagged "valuation basis unverified" and never labelled; a band that AA's figure omits under an unchanged tariff stays under E157 (AA cost caveat), not this gate, and its row competes over a cost range without labels (owner decision O94, 2026-10-28). The join is keyed by the observation's basis ID and the IDs of the price records in force at V, so a new or changed price record re-runs it even when no source payload changes (fixtures: a tariff change between AA's valuation and V with the AA payload unchanged, where a uniform k revalues (outcome 2) and a single-category change yields outcome 3; a Plan measurement revalued to the new tariff while the basket cannot be, which never yields a cross-basis C/M; a changed price record with every payload unchanged, which re-runs the join and changes the outcome; both bounds bracket the exactly repriced values for random demand and consumption vectors). Each row publishes, per stratum and branch, its row-level scenario dispersion (E87; the former per-row "own normalised weighted spread" is dropped as undefined without a panel, E136 — the common-panel weighted spread and this decomposition answer the two questions): Var_s(V_i) = β²Var_s(S_C,i) + (1−β)²Var_s(Q_i) + 2β(1−β)Cov_s(S_C,i, Q_i), with the covariance term published separately and labelled scenario dispersion under the declared kernels (bounds-only rows: "no scenario SD defined"); cohort SD notation is reserved for the within-cohort influence diagnostic. Release gates (on failure the release is held — fix the data or re-anchor as a versioned migration with a dual-run comparison; O12): the clip gate defined under Cost, an unversioned AA chart/field change, or any score swing > 5 points that E177 does not attribute. The registry records, per row: chart field name; total cost and cost per task side by side; repeat inclusion; AA cache protocol and date, including its rate provenance (AA values cached input at live measurements of the model's typical cache-hit rate, not the run's one-off rate; the measurement window is not published; E176); price rule (first-party list vs cross-provider median for open weights); token metering basis (provider-reported counts, AA's default, or AA's canonical-tokenizer fallback; "not published per configuration" where AA does not say which, as on 2026-10-20; E176); Elo anchor identity (e.g. GDPval-AA scale pinned to a named reference model), the capture's hash and instant with the previous capture's digest (E90; AA publishes no fit revision or freeze status) and judge-panel/grader versions for rubric-graded leaves. A change of rule in any of these is a methodology migration; a new value under an unchanged rule is a data refresh (see Versioning). Each release prints its metering mix (rows on provider-reported counts, on the fallback, and unstated); where AA publishes the basis per configuration, two rows whose basket costs lie within a factor of 1.10 of each other on different bases carry a comparability caveat (E176). Leave-AA-out is reported as "not identifiable under the coverage rule" when the remaining identified quality weight is under 40% (the case today, with 34% independent weight in the max-effort ranking and 22% in the AI Coding Daily ranking), and is excluded from any denominator. Independent-source checks (E62, split by E66): on the matched panel of rows with every independently executed leaf of the ranking (Bug Hunt with the two Vals boards and LiveBench 2.0 Overall, or Bug Hunt with AI Coding Daily; a Terminal-Bench leaf keeps its named source, and a tbench.ai fill is not counted as an independently executed leaf for the matched panel), two named statistics with configuration-row bootstrap intervals and their model-identity cluster-bootstrap companions (labelled matched-panel sensitivity), each printed with its panel's configuration count and distinct model identities, and with a model-identity cluster-bootstrap companion that resamples an identity with all its matched efforts when one repeats (it coincides otherwise; E329, on reviewer 89): (a) quality agreement — Kendall τ_b between the observed-quality ranking and the independent-only quality ranking, Q_ind = the unweighted mean z of those leaves; (b) quality-substitution value agreement — τ_b between the displayed value ranking and value recomputed with Q_ind in place of quality, cost, anchors, basis and route held fixed (this substitutes quality evidence only; it does not validate costs or Plan multiples). A panel with insufficient rank variation returns "undefined". (c) Disjoint-evidence agreement (E71) — τ_b between AA-executed-only quality and independently-executed-only quality on the same panel, with retained leaves and weights published, labelled a restricted evidence comparison (not an eligible ranking); (a) and (b) share inputs with the composite and are described as such. Descriptive only, no scenario share. Active-rules manifest (E63): each release lists its gates, flags and rules with their status (fired / passed / vacuous / unresolved) so readers can see which rules bound, the build-stopping evidence gates among them (O64, O69, O71, O75, the typed change records behind every flag and split, which must also produce their flags, under O99, O101, O105 and O107, the AA note register with its capture, basket-label and named-row checks under O100, O103, O106, O108 and O109, E195, E204, E225); the gates that stop the build when they fail (the Coding Agent Index manifest, the Terminal-Bench agent list, cutoff-day row dates, the plan search, the typed change records behind every flag and split, the AA note register with its capture checks, and the frontier path checks) are listed together as passed, and the source clocks and freshness gates as their own entry, and the Plan lifecycle entry counts the flagged plan rows. Review convergence (owner decision O56, governance only): for the remaining review rounds (the internal Claude ladder and the Perplexity panel) a round is clean when it raises no finding of medium or higher severity; low-severity findings and design suggestions are considered but do not make a round non-clean, and each internal-ladder rung and each Perplexity model is done after two consecutive clean rounds (O56), a non-clean round being answered with a new draft before the next. SemiAnalysis watch (owner instruction, 2026-10-22): a weekly scheduled task (Mondays 08:51 UTC, report-only) searches the web, SemiAnalysis's newsletter and its X accounts for a new SemiAnalysis subscription-usage analysis;

Final sentence:

Revision history: omitted from this review copy (not normative); it is in draft-r184.md in the same folder of the repository.

The connector returned file contents but no citation identifiers; section and rule references below identify the supporting passages without inventing citation tokens.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

Independent-source agreement changes leaf weights as well as evidence scope, making disagreement harder to interpret.

Issue: Part 16’s “Independent-source checks,” E62/E66, defines 
𝑄
i
n
d
Q
ind
	​

 as the unweighted mean of independent leaves. Consequently, the quality-substitution statistic changes both which evidence contributes and the relative importance of the retained leaves.

Why it hurts the objective: A weak agreement result does not distinguish sensitivity to independent evidence from sensitivity to a different task weighting. Conversely, strong agreement need not demonstrate robustness under ValueRank’s declared task priorities. The draft correctly says that this does not validate costs or multiples; the remaining ambiguity concerns the quality comparison itself.

Concrete change: Keep the adopted equal-weight diagnostic, but add a weight-preserving companion using the ranking’s original weights renormalized over its independent leaves. Print the two results together, explicitly labelled “equal-weight independent evidence” and “policy-weight-preserving independent evidence.”

New argument relative to the ledger: This does not reopen E62/E66’s adoption, E71’s disjoint comparison, or E329’s clustered uncertainty treatment. It isolates a separate confound introduced by the explicitly unweighted substitution.

2. Methodology design recommendations

Prioritize the weight-preserving independent-source companion. For ranking 
𝑟
r, let 
𝐽
𝑟
J
r
	​

 be its independently executed leaves, 
𝑤
𝑟
𝑗
w
rj
	​

 its existing quality weights, and 
𝑧
𝑖
𝑗
z
ij
	​

 the already normalized leaf records. Define:

𝑄
𝑖
𝑟
i
n
d
,
p
o
l
i
c
y
=
∑
𝑗
∈
𝐽
𝑟
𝑤
𝑟
𝑗
𝑧
𝑖
𝑗
∑
𝑗
∈
𝐽
𝑟
𝑤
𝑟
𝑗
.
Q
ir
ind,policy
	​

=
∑
j∈J
r
	​

	​

w
rj
	​

∑
j∈J
r
	​

	​

w
rj
	​

z
ij
	​

	​

.

Compute the existing quality-agreement and quality-substitution-value-agreement statistics again using this companion. Hold the matched panel, costs, routes, anchors and bootstrap samples identical to those used for the adopted equal-weight results. Publish:

Retained leaves and normalized weights.

Equal-weight and policy-weight-preserving 
𝜏
𝑏
τ
b
	​

, side by side.

Their difference, described as weighting sensitivity—not an independent validation statistic.

The existing configuration-row and model-identity cluster-bootstrap intervals, retaining the draft’s undefined-status handling.

This needs no new public source, exact-variant transfer, imputation, buyer profile or release gate. It reuses the evidence already required by part 16.

No additional material design changes are warranted from these two parts. In particular, the reviewed passages already distinguish scoring from interval eligibility, consumption from established capacity, published-record protection from scenario dispersion, and tariff incompatibility from incomplete price evidence. I would not reopen those adopted distinctions.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK