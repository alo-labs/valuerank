I'll start by locating the GitHub connector's file-read tool (one minimal lookup), then read all 7 parts.
Now reading all 7 parts in order at the pinned commit.
All 7 parts retrieved and read. Before writing the review, let me spot-check three externally verifiable factual claims the draft makes (AA's GDPval integration transform, Terminal-Bench's published CI whiskers, LiveBench 2.0 suite composition).
0. Read check

The draft's first line, quoted exactly:

# ValueRank methodology — draft r53

All seven parts were opened through the GitHub connector at commit 64bd04f and read to their ends. Last 12 words of each part, in order:

Part 1: "cost per task, not AA's 7:2:1 blended price, not total Index cost."

Part 2: "unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements)."

Part 3: "a bias bound in the identification layer); repetitions are not a bias."

Part 4: "scenario convention (with one published alternative), never evidence; formal bounds are distribution-free."

Part 5: "candidate's cost upper bound); otherwise "not established", with the omitted competitors listed.""

Part 6: "or definite result; every cost check reads C_W, never the Index diagnostic."

Part 7: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."

Every part was read to its end, so the review proceeds.

1. Findings by severity

Critical

None.

High

H1 — The scored basket inherits AA's task multiplicities; no task-mix stress exists anywhere. C_i,W = Σ n_e c_ie uses AA's suite-driven multiplicities (AutomationBench 657 tasks, SciCode 288, Terminal-Bench 66, GDP.pdf 100…), so the implicit weight of each component in the cost score is whatever execution cost AA's evaluation design produces. AA's own methodology page confirms these task counts and shows the components differ by an order of magnitude in size. Why it hurts: the objective is lowest practical cost per unit of value; a coding-heavy buyer and a document-heavy buyer pool these components very differently, and whenever models' relative per-task costs differ across components, their value-score orderings can reverse under a plausible buyer mix. Nothing in the draft probes this: deletion branches (E146/E149) remove whole components, S2 stresses quality weights, prices and cache, and E64 removes the double-priced Terminal-Bench execution — but no branch re-weights task mix. What is new versus the ledger: E42/E64/E149 handle overlap and removal; and the E22 readiness table already publishes spend shares s_ie and HHI_i — so the monitors exist, while no stress branch over n'_e exists. Recommended change: register 2–3 frozen alternative demand profiles per workload version W (e.g. "coding-agent-heavy": shift mass toward DeepSWE/Terminal-Bench equivalents; "document-heavy": toward GDPval/GDP.pdf/LCR), recompute C'_i,W = Σ n'_e c_ie from the already-captured per-component mean costs, re-freeze anchors by the existing freeze rule, and publish rank changes on the E65 common panel as named S2 branches. This is implementable purely from public data and changes neither the O15 target basket nor the headline.
artificialanalysis

H2 — Owner decision challenge (O17): subset-cost rows keep table position, and the distortion is one-directional, live for 3 of 19 rows, and its magnitude is never published. A row missing a component shows a cost that excludes that component's spend, so its S_C is systematically better; the missing component today is the Coding Agent Index — the basket's largest single unit at 303 deployment-equivalent tasks — absent for GPT-6 Astra (xhigh) and both MiMo rows. E86 flags the different anchor/exchange rate and E10 publishes paired bridges, but only for rows where both are evidenced, i.e. precisely not for the 3 rows whose distortion matters; the label "cross-workload ordering not identified" understates that the bias direction is known, not merely unidentifiable. What is new versus what O17/E10 already settled: no score change, no imputation (O19 untouched) — the ask is quantified disclosure. Recommended change: publish beside each subset row (a) the missing component's cohort-median expenditure share s̄_e from the already-computed E22 object, (b) the paired-bridge distribution of full−subset value-score and rank deltas across the 16 fully-evidenced rows as an empirical calibration of "positions induced by dropping this component", and (c) an upgraded flag when the missing share's cohort median exceeds a pre-registered threshold (e.g. 25%). The row keeps its owner-required score and position; readers get the sign and scale of the known bias.

Medium

M1 — The claim "today only Terminal-Bench 4.0 documents one" interval is factually fragile, and GDPval-AA v2.1 is the counterexample. AA's methodology documents that GDPval-AA v2.1 Elo ratings are fitted by Crowd-BT maximum likelihood with sandwich-estimator confidence intervals — arguably a better-documented estimand and method (named model, named estimator) than tbench.ai's bare "The whiskers span the 95% confidence interval". The draft's own machinery already anticipates this: E145/E143/E155 reserve separately named streams for fitted-rating intervals with a documented estimand, and E25's kernel hierarchy has a "published estimate with documented standard error" rung. AA has also publicly estimated a 95% CI below ±1 for the overall Intelligence Index from 10+ repeats on selected models, which the registry's blanket statement "DeepSWE and the AA Index fields publish no interval" should at least footnote. Why it hurts: the S1M/allowlist rationale (E162/E165) is a factual registry claim; if it is stale, the single-interval v1 uncertainty story is under-documented, and a 10%-weight leaf (GDPval) with documented estimation uncertainty gets less uncertainty treatment than a 10% leaf (Terminal-Bench) whose interval is less specified—that inversion is visible to any critical reader of sources. Recommended change: either stand up the reserved fitted-parameter stream for GDPval v2.1 (estimand = fitted rating, published label accordingly), or publish an explicit dated deferral reason (e.g. per-row half-widths not present in the captured payload) as a readiness-table row with a capture task.
tbench
+2

M2 — Registry fact error: "the page publishes no release date" for LiveBench 2.0. livebench.ai currently displays "Release 2.0 … 2026-10-13" and "Last updated 13 October 2026 — the latest release", and the suite list (Agentic, Reasoning, Coding, Browser Use, Data Analysis, Research, Design) confirms the premise of O26 (no instruction-following suite). Why it hurts: the versioned registry's authority rests on faithful source metadata; a visible, checkable misstatement about a pinned source erodes the whole evidence-bundle contract (E159). Recommended change: record the source's own release/updated dates in the registry alongside the title-and-capture-date pin, and add a registry lint that flags "source publishes no date" assertions when a date field exists.
livebench

M3 — The basket mixes two token-metering bases row-by-row, and the cache series has no identity in the valuation gate. AA's methodology states Index costs use provider-reported token counts where available and an o200k canonical-tokenizer fallback otherwise (contrast: performance benchmarking uses the tokenizer for everyone), and that cache cost combines token counts with separately live-measured typical cache-hit rates rather than the run's one-off measurement. Why it hurts: (i) two rows' basket costs may rest on different metering bases — provider self-report vs. tokenizer reconstruction — which E157's tariff/ontology machinery does not capture (it maps categories, not measurement origin), and (ii) E170's valuation-basis gate joins price records at V, but the cache-hit-rate vintage feeding AA's cost is a separate unpublished-timeseries input; the registry stores only "AA cache protocol and date" (a single date), not the series span. Recommended change: per-row registry fields token_metering_basis (provider-reported / tokenizer-fallback / unknown) and cache_series_id (with the live-measurement window AA documents); publish a per-release count by metering basis and a comparability caveat where a close cost ordering crosses bases. This extends E158's boundary record along an axis public documentation already supplies.
artificialanalysis

Low

L1 — No utilisation axis on the Plan basis (distinct from E15's workday diagnostic, which restricts when consumption may occur, not how much purchased capacity is used). Full-utilisation cost overstates value for light users, as Known limitations admits; but C_Plan(u) = (C_W / M_displayed) ÷ u for u ∈ {0.25, 0.5, 0.75, 1.0} is pure arithmetic on already-published quantities and would make the exploratory Plan headline honest for non-saturating buyers at zero new-evidence cost. Recommended change: publish these rescaled-cost columns, labelled an arithmetic identity, never identified Plan economics.

L2 — The score-swing gate can be satisfied vacuously. The gate fires only on a swing ">5 points without an attributed cause", yet the declared sequential bridge attributes every swing by construction (with a "decomposition unavailable" fallback label for interaction effects), so the gate's discriminating power depends on a quantity — the bridge's unexplained remainder — that is never published. Recommended change: require the bridge to output its interaction remainder per row and fire the gate on |remainder| above a pre-registered threshold or on fallback attribution, so "attributed" is falsifiable.

2. Methodology design recommendations

Prioritised; all are refreshable from public data.

Task-mix stress branches (from H1). Per workload version W, register a frozen set of profiles Π = {n^(p)} of alternative multiplicities over the admitted components (and the Coding Agent Index as one unit, per E148). For each profile: C_i^(p) = Σ_e n_e^(p) · c_ie using published per-component mean costs; anchors re-frozen by the E160 rule on the same reference panel; output = rank changes and the exchange rate on the E65 common panel, labelled "alternative task mix (specification stress), not the scored workload". Profiles declared before ranks are inspected; weights of profiles never traded against the headline.

GDPval fitted-rating stream (from M1). If the captured GDPval payload carries per-configuration CI half-widths: a named stream with target profile "fitted-parameter uncertainty of the frozen v2.1 rating", kernel anchored on the published sandwich SE (E25 rung 3), z-scale draws clipped to the clamped domain, published beside S1M with its own event names (E161) and never authorising the E100 label. If the payload lacks half-widths: a readiness row "documented but not captured" with a capture task and date, so the E162 claim can be re-asserted as "only Terminal-Bench interval captured".

Metering-provenance layer (from M3). Add token_metering_basis, cache_series_id (with measurement window), and a release-level "metering mix" line ("n of 19 basket costs on provider-reported tokens, m on tokenizer fallback, k unknown"); pairwise value/cost orderings separated by less than a pre-registered margin and crossing metering bases are published with a comparability caveat. Extends E157/E158; no scoring change.

Utilisation ladder columns (from L1). C_Plan(u) = (C_W ÷ M_displayed) ÷ u at u ∈ {0.25, 0.5, 0.75, 1}, type-stamped per E166 (amount_kind = displayed-multiple arithmetic), excluded from all interval outputs and from the anchor object (E160 unchanged).

Bridge remainder gate (from L2). Publish, per row, the sequential bridge's residual after the declared ordering (price → token use → benchmark record → method → cohort); optionally also publish the average of the two reversal orderings as an interaction summary. Gate: hold the release when the residual exceeds 5 points or the only output label is "decomposition unavailable", replacing today's effectively unfalsifiable "unattributed swing" trigger.

3. Questions for the owner

Are the frozen task multiplicities n_e inside O15's basket decision (fixed policy), or is a registered alternative-mix S2 branch permissible under existing stream governance? The answer determines whether recommendation 1 is a branch registration or an owner decision.

Does the captured GDPval-AA v2.1 payload contain per-configuration CI half-widths (or only the methodology's statement that sandwich CIs are computed)? The answer decides whether recommendation 2 produces a v1 stream or only a readiness-table entry.

Does O17 require subset-cost rows to hold position rules regardless of the missing component's cohort spend share — i.e., is the H2 disclosure package acceptable as pure presentation, or would you also consider a prominence-thresholded display treatment? Only the disclosure is proposed here, but the answer fixes whether the threshold flag in H2(c) is in scope.

4. Verdict

VERDICT: HAS FEEDBACK