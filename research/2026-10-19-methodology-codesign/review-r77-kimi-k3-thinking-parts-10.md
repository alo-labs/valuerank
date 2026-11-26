All three parts were read in full via the GitHub connector at the pinned commit, each in a single read with no truncation.

0. Read check

Part 10 — first line: - **Specification**: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking... Last 12 words: "of both rankings has a cost, so the two ladders are equal."

Part 11 — first line: - **Noise-margin companion (owner decision O44, kept over a per-candidate margin as O128, 2026-10-30)**: because each bar is a configuration's own displayed quality (O34), the cheapest row at a bar can be its setter... Last 12 words: "maximum (with consumption-dependent payments the multiple ratio is not assumed ≤ 1)."

Part 12 — first line: - **Harness stress branch (E19, premise corrected by E227).** Bug Hunt runs on vendor CLIs, AI Coding Daily on a harness chosen per model, and tbench.ai's matched rows mostly on vendor agents... Last 12 words: "or definite result; every cost check reads C_W, never the Index diagnostic."

All three listed parts were read to their ends.

1. Findings by severity

Critical

None.

High

None.

Medium

The mandatory workload cross-check (part 10, E41) can go silently dark exactly when the ranking is smallest. The rule suppresses the statistic below n = 8 rows in I_b, but the text never says the suppression itself must be published with the panel size. With the max-effort ranking at 9 ranked rows and the Coding Agent Index priced on 7 (O50/E140 status), the matched cost panel likely sits at n = 7 today — the "mandatory" check is probably suppressed right now with no reader-visible trace. Additionally, the small-n regime uses a model-row bootstrap, and at n ≈ 8–10 Kendall-τ inference is known to be unreliable — Bayesian/default Kendall tests are documented as liberal at n = 10. Why it hurts the objective: the cross-check is ValueRank's only direct guard that the cost basket agrees with per-task cost efficiency; a silently suppressed guard looks identical to a passing one in the published output. Concrete change: publish the suppression state and n alongside the statistic whenever it is suppressed; at 8 ≤ n < 12 use an exact permutation interval for the E41 threshold test instead of, or beside, the bootstrap, and name the procedure change in the stream manifest.
arxiv

The harness-stress band (E19, part 12) is anchored to the wrong task family and its unevaluability condition looks stale. The band stresses Bug Hunt and AI Coding Daily leaves but is estimated solely "from same-model cross-agent spreads on the tbench.ai leaderboard… unevaluable while none of them is listed under two agents." Two problems: (i) public Terminal-Bench leaderboards do list the same model under two or more agents — the TB 2.1 board lists five models each under a vendor CLI and Terminus 2, with spreads of 2.8–8.1 points, and June 2026 captures show GPT-5.5 at 83.4 under Codex CLI versus 78.2 under Terminus 2 — so if the current capture reports unevaluable, the build should disclose which same-model-two-agent pairs were searched; (ii) even when evaluable, Terminal-Bench-task harness spreads (median best-worst harness gap around 13.6 points for well-covered models ) are a questionable estimator for the harness sensitivity of Bug Hunt and AI Coding Daily, different task families — yet the registry already contains direct Bug Hunt cross-harness evidence (E224: Gemini 4 Argon 40.7 vs 33.0) that the band does not use. Why it hurts: an S2 stress that is meant to bound harness confounding either silently does nothing (unevaluable) or imports a band calibrated on the wrong task distribution, biasing the displayed stress for the two leaves that most need it. Concrete change: publish the list of same-model-two-agent pairs found per capture; pool the tbench pairs with the registered Bug Hunt cross-harness pairs (E224), estimating a band per stressed leaf and publishing which source(s) fed each band.
dev
+1

Low

Owner decision challenge (O128; new argument). The O44 noise-margin companion uses 1.96√2 × median analytic quality SD — an equal-variance, independence assumption. The correct threshold for the difference of two independent estimates is 1.96√(SD₁² + SD₂²), and treating fixed non-overlap logic against a common margin mismeasures significance when variances are unequal (with equal variance, CI non-overlap corresponds to a 0.0056-level test, not 0.05). The ledger records O128 as rejecting a per-candidate margin; what is new here is that I do not propose replacing the global margin — only a per-answer annotation: beside each companion, print the companion row's own SD and the pairwise margin against the bar-relevant comparison, flagged when the pair margin exceeds the O44 global margin. Cost: one extra field in displayedCheapest.<basis>.bars[]; zero change to any label or bar.
eng.auburn
+2

Owner decision challenge (O129; new argument). The cohort's near-gap admission (O51) is computed on rounded tooltip Index, while the rendered-path vertices are read strictly from unrounded chart coordinates (E195) and a left-of-line point stops the build at 0.5 px tolerance (E204). The ledger rejects recalculating the gap on the unrounded Index; what is new is the narrower point that the asymmetry is un-audited — membership can silently flip on AA's display precision while sub-pixel issues elsewhere are build-stoppers. Concrete change: a build check that perturbs each boundary configuration's rounded Index by one display unit in each direction and asserts admission is unchanged, publishing any configuration whose membership flips (a rounding-neighbourhood check), without changing the O129 membership rule.

The E221 "what would settle a row" u* is published at point values only. Since u* is monotone in the observed leaves' values, the reporting-precision interval on the observed leaves maps to an interval on u*; publishing u* as a two-point range would match the published-record-precision contract the rest of the outputs follow. Utterly cheap to compute; flagged only because every other released statistic in these parts carries its precision treatment and this one quietly does not.

2. Methodology design recommendations

Cross-check publication contract (highest priority, feeds finding M1). Register a workloadCrosscheck output that always prints per benchmark: n in I_b, the statistic (or "suppressed, n = k"), the resampling method used, and the matched panel's configuration list. At 8 ≤ n < 12, add an exact permutation interval; document the threshold behaviour switch in the stream manifest so the pre-registered E41 threshold stays honest at small n.

Pooled harness-band estimator (feeds finding M2). Band per stressed leaf b: over all registered same-model pairs (m, h₁, h₂) with public results on a task family F, Δ̂_F = median |score(m, h₁) − score(m, h₂)|; the Bug Hunt band pools its own cross-harness pairs (E224) with the tbench estimate, the AI Coding Daily band uses tbench plus any AICD cross-harness pairs found in the E84 staged searches. Publish pairs used per capture; the build stops when an expected pair disappears. This remains a stress band, never in Θ, consistent with E19's registration.

Pairwise-noise annotation on the O44 companion (owner decision challenge, diagnostic only): per companion answer, print rowSD, pairMargin = 1.96·√(SD_companion² + SD_reference²), and a one-word flag when pairMargin > global margin. No label, bar, or margin rule changes.

Rounding-neighbourhood admission check (owner decision challenge): for each configuration within one display unit of F(c) − 3, assert membership stability under ±1 display-unit perturbation of the tooltip value; log and publish flips. Half a dozen lines of build code.

u* precision band (E221): publish [u_L, u_U] induced by the observed leaves' published-precision intervals, with the naming of missing leaves unchanged.

3. Questions for the owner

When the E41 workload cross-check is suppressed (n < 8), is anything published today — a suppression marker or panel size — anywhere in the release output? If yes, finding M1 drops to Low and recommendation 1 shrinks accordingly.

On the current tbench.ai capture, is the E19 band evaluable, and if so, which same-model-two-agent pairs fed it? If evaluable, the stale-condition half of finding M2 drops and only the task-family transfer argument stands.

4. Verdict

VERDICT: HAS FEEDBACK