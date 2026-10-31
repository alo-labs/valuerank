0. Read check

Part 1 (research/2026-10-19-methodology-codesign/perplexity/parts-r154/draft-r154-part-1-of-13.md)

First line: # ValueRank methodology — draft r154

Last 12 words: "carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py)."

Part 2 (research/2026-10-19-methodology-codesign/perplexity/parts-r154/draft-r154-part-2-of-13.md)

First line: - **Full benchmark set (owner decisions O36, O38)**: a cohort configuration is ranked in a ranking only when it has every leaf of that ranking for the exact configuration, so every row of a ranking is scored on the same benchmarks at that ranking's owner-set weights… (line continues)

Last 12 words: "or provider declined some tasks on safety grounds") also flags "partial component"."

Both parts were read to their end. All findings below are drawn only from these two parts.

1. Findings by severity

Critical

None.

High

Safety-fallback flag is deliberately withheld from interval and scenario labels (O63, part 2, Cost section). The draft states that a Coding Agent Index row where safety refusals triggered blocked or fallback attempts is flagged, "the flag is printed beside each bar's displayed-record result and noise-margin companion whose cheapest row carries it (the interval and scenario labels do not print it)." A fallback attempt means another model's tokens are inside the row's mean.costUsd-based cost, so the row's cost is not purely the named configuration's cost — biased in an unknown direction, plausibly favourable (a cheaper fallback finishing tasks). Under the objective ("lowest cost for the value it delivers in practice"), the label is exactly the claim surface, and today the displayed-record result that does carry the flag is the informational one, not the claim. Concrete change: print the agentSafety flag (or its short form) with every interval and scenario label whose earning row carries it, or make a fallback-blocked row label-ineligible on the E233/E222 pattern (compete, never earn) — the weaker disclosure fix is sufficient and cheaper.

The near-gap cohort boundary is computed on rounded Index values while frontier membership is checked on unrounded chart coordinates (part 1, Cohort; part 2, Fallback/E195 context). Part 1: the near rule is "rounded Index within 3 points of the frontier's best at equal or lower cost", and the draft itself notes rounded tooltip ties exist today (three configurations display 38; two display 56), with "the near rule's rounded-Index gaps... measured against these points." E195 in contrast requires frontier membership to be read strictly from the rendered path in chart coordinates, "never on rounded values," and the E209 reconciliation uses unrounded page fields at 10⁻⁶ relative error. A configuration whose true gap is 2.5–3.5 sits on a knife edge that AA's integer rounding can flip with any re-capture, changing cohort membership, N, the admission threshold ⌈2N/3⌉, anchors and bars — the eligibility set that defines who can answer the objective at all. Concrete change: where AA's raw page fields permit, compute the near gap on unrounded values as the normative rule (rounded tooltips as fallback only), and in all cases publish a boundary diagnostic listing every configuration whose rounded gap is exactly 3 with its unrounded gap where known.

Medium

The claim-scope sentence carries no Plan-basis caveat (part 1, Objective and claim scope). The scope reads "value among the configurations ranked in one ranking... under that ranking's published benchmark mix and evidence," but the same page states that on the Plan basis 14 of 27 and 30 of 51 rows rest on owner assumptions, 21 and 44 on possibly superseded or expired routes, and "no Plan frontier or bar claim is supported (E61, E67)." A reader quoting only the claim scope — the top-level contract — can over-claim the Plan ranking. Concrete change: extend the claim scope with a per-basis qualifier ("on the Plan basis, no frontier or bar claim is supported; the Plan ranking is exploratory arithmetic") and mirror it as a machine-readable per-basis field in scores.json.

The O116 FrontierCode stand-in is a scored cost input read from chart labels rounded to USD 1 (part 2, Cost). Every other cost input is governed by unrounded page fields (E209's 10⁻⁶ test; ITBench chart totals are explicitly "treated as rounding intervals"). The stand-in that currently prices the whole AI Coding Daily ranking's cost column is "FrontierCode 1.1, AA's total-cost chart, labels rounded to USD 1" — a different precision regime feeding the value score. Also, while the stand-in is active the AI Coding Daily basket is not the O15 SDLC basket: it omits SWE-Atlas QnA (124 tasks) and the index's vendor-agent Terminal-Bench run, which is only implied by "in the index's place." Concrete change: treat the stand-in's rounding as an interval like ITBench's (or read an unrounded field if AA publishes one), publish the maximum value-score effect of USD-1 rounding through the anchor exchange rate, and state beside the AI Coding Daily cost column that the basket omits the index's non-FrontierCode tasks while the stand-in is active.

The coding-agent confound is buried in scores.json (O123, part 2). Cost is measured under vendor agents while quality leaves come from AA's model runs, and the S2 harness stress is "unevaluable while no model is listed under two agents (today: unevaluable)" — so today the confound is entirely unquantified and invisible in the published tables ("Each row publishes its agent and that execution flag (scores.json rows[].codingAgent)"). For a reader asking which configuration is cheapest for the value delivered, the agent identity is part of the cost's meaning. Concrete change: print the agent name beside each headline cost figure, not only in scores.json.

The E242 † mark on Plan bands is ambiguous about membership (part 1, Transfer tolerance). "A Plan band resting on an owner assumption... is marked †" does not say whether the mark fires when any band member rests on an assumption or only when the band's defining (first) row does. A band whose first row is measured but which contains an assumption row would be unmarked under the narrow reading, understating uncertainty exactly where assumption rows hide. Concrete change: one sentence fixing the semantics — recommend "any member row" as the conservative reading — and a build check that the count of † bands is reproducible.

Owner decision challenge — the near gap is keyed to AA's general Intelligence Index while software engineering is 60% of quality (O51/O122). The draft's own common-leaf diagnostic (O121) exists because the leading rankings cannot rank cheaper efforts, which shows the cohort/ranking structure limits answering "lowest cost for value" outside the top. But the admission criterion itself is general-capability-based: a configuration that is SWE-frontier at its cost yet more than 3 general-Index points below the frontier best is excluded from every ranking, whatever its SWE evidence. What is new here is not the rejected "rank unranked alternatives" argument but the mismatch of axes: the cohort gate uses the one composite (general Index) that ValueRank's own quality vector deliberately down-weights to 40%. Concrete change (no ranking change, implementable from public data): a diagnostic listing catalog configurations that would enter the near gap under an SWE-weighted composite gap at O55 weights, published beside the cohort, so the owner can see the cost of the fixed rule each release.

Low

The active release cutoff V is never stated in these sections (part 1, Source contract). The registry text says the chart was "captured 2026-10-25T09:53:28Z for the release cutoff O65 set," and every age gate (≤ 7 days, 30-day windows, ≤ 45 days) keys on V, yet parts 1–2 never print V's timestamp, so a reader cannot verify any capture-age or window rule. Concrete change: print V (and the separately recorded search cutoff, E213) in the source contract of every release.

The common-leaf diagnostic ranking (O121) publishes bar answers beside the leading rankings' without a stated noise companion (part 1, Cohort). It has its own anchors, bars and scenario run, but nothing in these parts says it prints rank separability or noise bands. Since its purpose is exactly to compare its "displayed-record cheapest row beside each leading ranking's answer at the same position," an unsuspecting reader can read a difference between its answer and a leading ranking's as signal when the leading rankings themselves report "0 of 8" and "1 of 15" adjacent ranks separable. Concrete change: give the common-leaf ranking the same separability statement (or state explicitly that its answers are not separability-checked), printed with the comparison table.

2. Methodology design recommendations

Prioritised:

Label-level safety disclosure (fixes High-1). Add to the label grammar: any interval or scenario label earned by a row with agentSafety blocked+fallback > 0 carries the flag token (e.g. "†fallback: <model names>, <n> attempts"), sourced from the already-captured hardStopAttemptCount/fallbackAttemptCount sums. Zero scoring change; pure output grammar. Alternative (stronger, owner's call): make such rows E233-style — deny, never earn.

Unrounded near-gap rule with boundary diagnostic (fixes High-2). Normative gap = unrounded Index difference where AA's page fields supply it; fallback = rounded tooltip. Publish cohort.boundaryRows: every configuration whose rounded gap equals exactly 3, with unrounded gap and membership under both readings; a flip between readings is a disclosed diff, never a silent change.

Per-basis claim scope (fixes Medium-1). scores.json claimScope[basis] = {frontierClaims: bool, barClaims: bool, exploratory: bool} derived from the existing E61/E67 conditions, printed in the README claim-scope sentence. Keeps the Plan table honest without touching O3/O72 policy.

Stand-in precision and composition note (fixes Medium-2). Model the FrontierCode chart total as a ±USD 0.5 rounding interval feeding the cost score through the anchor log-scale (an interval on ln C, exactly the E182 pattern); print the omitted-tasks note beside the AI Coding Daily cost column; when the Coding Agent Index is admitted, the E184/O12 dual run already governs the migration.

Visible agent column (fixes Medium-3). Render rows[].codingAgent in the headline cost table, next to the existing execution flag; no new capture needed.

† semantics fix (fixes Medium-4). One definitional sentence plus a build assertion; make the conservative "any member row" reading normative.

SWE-composite near-gap diagnostic (supports Medium-5, owner decision challenge). A read-only table: catalog configurations ranked by SWE-weighted composite at their plotted cost, marking those within 3 composite points of the SWE-composite frontier best at equal or lower cost but outside the current cohort. Refreshable each release from the same AA captures.

Print V and the search cutoff in the source contract (fixes Low-1); add a separability caveat to the O121 comparison table (fixes Low-2). Both are single-line output additions.

3. Questions for the owner

Should a row whose Coding Agent Index attempts were finished by fallback models be able to earn an interval/scenario label at all (E233 pattern), or is label-level flagging enough? The answer decides between the two variants of recommendation 1.

Is the near gap's use of rounded displayed Index a deliberate capture-procedure constraint ("public chart and tooltips only") or an accident of the current rule? If deliberate, is the boundary diagnostic in recommendation 2 acceptable as the permanent mitigation?

Does AA publish an unrounded FrontierCode total-cost field anywhere its raw data exposes (as it does for the Index accounting fields under E209)? If yes, recommendation 4's interval treatment can be replaced by an exact read.

Intended semantics of the E242 † band mark: any member row resting on an assumption, or only the band's first row?

On the near-gap anchor (Medium-5): is keying cohort admission to AA's general Intelligence Index — the composite ValueRank down-weights to 40% of quality — a deliberate scope choice, or would the SWE-composite gap diagnostic be admitted as a standing disclosure?

4. Verdict

VERDICT: HAS FEEDBACK