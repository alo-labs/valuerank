1. Findings by severity

I did not run web searches for this review, so the review is not source-cited. I could not check how specific benchmarks, quotas or cost fields work from the draft alone. The arithmetic below uses only the draft's own numbers.

Critical

C1. Shared cost anchors will clip the Plan basis.

With c_L = $50 and c_H = $20,000, S_C ≈ 87 at the cheapest API row ($110) and ≈ 14 at the dearest ($8,700).

Plan cost is API cost ÷ Value Multiple. A multiple of 5–10× or more puts many Plan rows near or below $50, so S_C clips at 100.

Clipped rows are indistinguishable on cost, so the Plan headline would be driven by quality alone exactly where Plan economics matter most.

Change: set Plan anchors separately, from the observed Plan-cost range (versioned, frozen). Add a release test: fail the release if more than 10% of rows sit at a clip bound on either basis.

C2. The "provisional" rule lets thin rows into the headline.

DeepSWE is 30 of the 60 SWE points, so a row with only DeepSWE has exactly 50% SWE coverage. Whether that passes "<50%" depends on boundary wording.

Renormalising over available leaves lets a row scored only on easy or saturated leaves outrank a fully covered row.

Change: define coverage as the share of total quality weight observed, not of one group. Require at least 70% total coverage and at least 2 SWE leaves for an unflagged headline rank. Rank provisional rows in a separate list.

High

H1. Selecting the best Plan route biases the result upward.

"Best route chosen after joining evidence and multiple" is a max over noisy estimates (winner's curse). It also rewards whichever plan tier has the most favourable, possibly the most recently measured, multiple.

Change: pre-register a default route per model, or pick the route on the multiple's lower bound. Publish the route's tier and fee. Propagate the multiple's interval through the Monte Carlo (see section 2).

H2. "Independent" quality is mostly AA-sourced.

Cost and the leaves for DeepSWE, FrontierCode, GDPval-AA, AutomationBench-AA, Omniscience, LCR and probably HLE, GPQA, SciCode and CritPt appear to be AA-run. That is roughly 75% or more of quality weight, plus the whole cost axis. Removing the Index from quality removed only the arithmetic double count, not the common-source dependency.

Shared harness, grader and scaffold choices therefore move cost and quality together.

Change: report "share of quality weight by source" on every release, and make leave-one-source-out (drop AA) a headline robustness column, not just a specification-layer item.

H3. Anchors of 0–100 give the leaves unequal effective weights.

Nominal shares are not the weights that matter. A saturated leaf (GPQA, and possibly LiveBench IF) has a tiny spread across the cohort. A hard leaf with low scores (HLE, CritPt, Terminal-Bench) spreads over a narrow part of its range. Spread, not nominal share, determines influence on ranking.

Change: publish effective weight = nominal weight × cohort SD of z, and a rank-correlation matrix between leaves. Set each anchor from a floor (chance level or baseline) to a documented ceiling (human or noise ceiling), versioned and frozen. If the effective weight of any group drifts more than ±50% from nominal, flag it.

H4. The cost axis measures a different workload from the quality axis.

AA's suite cost reflects AA's token mix. The SWE-heavy quality (60%) comes from multi-turn agentic runs, where cost is dominated by cache reads, tool loops and context growth. The objective is value "in practice" for engineering work.

I know this was partly deferred (dollars per successful task). The new argument is that it should be a mandatory specification-layer check, not a diagnostic. Where DeepSWE or Terminal-Bench 4.0 publish matched cost and success, compute a SWE-cost score and report rank agreement with the AA-cost ranking. A low Spearman correlation (for example below 0.7) should trigger a warning on the headline.

H5. The 25/75 headline hides an implied exchange rate. (Owner decision challenge, O2.)

Under the log cost score, doubling cost costs 100·ln2/ln(400) ≈ 11.6 cost points, which is 2.9 value points, or the equivalent of 3.9 quality points. Nothing in the draft tells readers this.

The objective is "lowest cost for the value delivered", which is closer to the threshold view than to a compensatory score. A model can score well by being cheap but weak.

Change: keep the headline if the owner insists, but print the implied trade-off ("2× cost ≈ 3.9 quality points") beside it. Show the cost-weight slider results in the main table. Consider a floor so that no row below the lowest bar gets a headline rank.

Medium

M1. Missing-at-0 and missing-at-100 bounds will be too wide to be useful.

A row missing 30% of weight has a 30-point-wide quality interval. "Confirmed qualifying" will rarely fire, and candidate sets will balloon.

Change: keep the worst-case bounds as the formal identification interval. Add a sensitivity band that replaces missing leaves with the cohort's observed min and max for that leaf. This is a sensitivity analysis, not imputation, so it stays within policy. Label it separately.

M2. The quality bars of 50, 60 and 70 are uninterpretable.

They depend entirely on anchors and weights.

Change: define bars as the quality score of named reference configurations (for example, "at least as good as the median definite-frontier model").

M3. Fixed weight on small, noisy leaves.

Bug Hunt is 10% on 105 bugs across two repositories, and it measures model plus harness. Fixed weight ignores precision.

Change: use precision-aware shrinkage. For example, w_i' = w_i / (1 + σ_i²/τ²), with τ² set as a policy constant, then renormalise within the group. At minimum, cap a leaf's contribution to the quality uncertainty at its nominal share.

M4. Multiple provenance and the staleness window.

A 90-day expiry is long for subscription quotas, which providers change without notice.

Change: add change-detection triggers. Flag any plan whose published limits or pricing page changed since measurement as "possibly superseded", with a 30-day soft expiry.

M5. Price-list drift and cache assumptions.

AA cost uses AA's price list at capture. Providers change list, cache and batch prices between captures.

Change: store the price-list date per row, and decompose score changes into "price change" versus "token-use change".

Low

L1. Omniscience as (2A+N)/3 is a custom blend. Check how it relates to AA's own Omniscience metric, and record the reason for the 2:1 choice.

L2. The log cost score is symmetric. A reader may assume $50 and $20,000 are meaningful. Say that they are purely scaling constants.

L3. Clipping loses information. Keep unclipped raw z in the data release.

L4. The registry should include grader identity and version for rubric-graded leaves (FrontierCode, GDPval-AA).

2. Methodology design recommendations

Priority order:

Joint Monte Carlo as the single uncertainty engine.

Draw N = 10,000 scenarios. Each scenario draws:

leaf values from their measurement intervals;

multiples from their intervals (log-normal, or uniform on a range);

a weight vector from a Dirichlet centred on the nominal weights, with concentration of about 50;

a source-drop flag;

the transfer on/off flag.

Publish P(rank ≤ k), P(on frontier) and P(qualifies at bar b). Declare a "unique cheapest" only if P ≥ 0.9.

Dependency handling is automatic, because shared multiples and price lists are drawn once per scenario.

Coverage and publication gate.

Coverage = observed quality weight. Require coverage ≥ 0.70, at least 2 SWE leaves and a cost for a headline rank. Other rows go on a provisional list.

Anchor calibration.

For each leaf: a_low = chance or baseline, a_high = documented ceiling. For cost, a_low and a_high come from the 1st and 99th percentile of a frozen reference cohort, separately for API and Plan.

Re-anchor only on a major version, with a score-change decomposition.

Effective-weight report.

Effective weight_i = w_i · SD(z_i) / Σ_j w_j · SD(z_j). Publish it with the leaf correlation matrix and the share of quality weight by data source.

Route selection for Plan.

Choose the route by max over lower-bound-adjusted value (for example, the 25th percentile of the multiple's distribution). Publish tier, fee period, binding rate-limit window and the evidence date.

Cost-workload cross-check.

Where matched cost and success exist (DeepSWE, Terminal-Bench 4.0), compute cost per solved task. Report rank agreement with AA-cost ranking and flag any model whose rank differs by more than 3 places between the two.

Release hygiene.

Fail the release on:

any clip-rate above 10%;

an AA field change;

a swing of more than 5 points from an unexplained cause.

3. Questions for the owner

What share of quality weight, and which leaves, are produced by AA rather than by independent sources? The answer determines how prominent the leave-AA-out view must be.

Are Value Multiples available across plan tiers (for example, $20 versus $200 plans) for the same model? If so, is the fee tier part of the route identity, or is one tier fixed per provider? This decides the H1 route-selection design.

Is a Plan multiple above about 10× plausible in the evidence you hold? If so, per-basis anchors (C1) are mandatory, not optional.

Is the headline meant for a reader who trades quality for cost at a fixed exchange rate, or for one who has a minimum quality requirement? The answer decides whether H5 needs a floor or only disclosure.

4. Verdict

VERDICT: HAS FEEDBACK