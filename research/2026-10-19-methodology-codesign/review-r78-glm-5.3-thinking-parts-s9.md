0. Read check

Part 9 (draft-r160-part-9-of-14.md) — first line: ## Uncertainty (three separate layers, one scenario engine) — last 12 words: not separable" and its S0 result is not described as target-workload support.

Part 10 (draft-r160-part-10-of-14.md) — first line: - **Specification**: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress. — last 12 words: both rankings has a cost, so the two ladders are equal.

Both parts were read to their end. Part 9 covers the scenario engine (S0/S1/S2, S1T, S1M, kernels, sequential testing, the measurement taxonomy and the Plan measurement/transport split); part 10 covers specification and deletion branches, the workload cross-check, the normative Θ/frontier/bar definitions.

1. Findings by severity

Critical

None.

High

None.

Medium

S1T's Jeffreys draws shift leaf means, differentially across rows, by up to ~12 points at small n (Owner decision challenge on O142). Part 9 draws binomial leaves from Beta(k + ½, n − k + ½), whose mean (k + ½)/(n + 1) the draft itself notes "sits slightly toward 50%". The shift is not uniformly slight: it is 100·((k+½)/(n+1) − k/n), which at the draft's own registered counts reaches ≈ 12.5 points for a 100% score on LiveBench's Data Analysis (n = 3), ≈ 10 points for Reasoning (n = 4), and ≈ 6 points for a 90% score on AI Coding Daily's wide reading (n = 6). Because leaders' leaves sit near 100% and mid-pack rows near 50%, the redraw systematically compresses the top of the panel, biasing S1T's pairwise ordering shares and adjacent-rank separability statements — and it does so asymmetrically, since the non-binary leaves' normal draws keep the published mean exactly. What is new versus O142's adoption record: the magnitude at the draft's own small-n leaves, and the mean asymmetry between binomial and non-binomial leaves. Recommended change: keep the Jeffreys draw (E241's positive spread at 0/100 is worth preserving) but register a mean-preserving alternative kernel via the existing E25 alternative_kernel_id — e.g. a draw with E[draw] = published score and the Jeffreys spread (a truncated normal centred on the score with SD from the Jeffreys posterior, or the Beta posterior recentred) — publish both, and print the per-leaf mean shift beside every S1T output so "slightly" becomes a number.

The AI Coding Daily ranking's failed workload cross-check (τb = 0.35 on 20) carries only a README warning with no attribution. Part 10 reports the pre-registered E41 threshold breach as a standing warning. This hurts the objective because the AI Coding Daily ranking is the broader headline ranking, and a near-zero Kendall τ-b between its basket-cost order and Terminal-Bench cost-per-resolved-task order means the cost term of its value score is weakly aligned with any per-task efficiency reading — and a reader cannot tell whether the divergence comes from O15's fixed task multiplicities, the O116 FrontierCode stand-in cost (the Coding Agent Index is still pending in that ranking), or genuine per-task cost differences. Recommended change: publish an attribution diagnostic built only from already-captured data: (a) leave-one-component-out τ_b on the same panel I_b, reusing the registered E172/E149 cost family; (b) the five largest rank inversions with each row's component-cost shares; (c) the same τ_b under the O116 selection-with-index variant once the index is admitted, so the warning can name which explanation the data supports.

E84's demand–cost reconciliation demands exact equality while recording a residual with no tolerance or decision rule. Part 10 requires p_release · d_ie = C_i,e and records cost_reconciliation_residual, but never states what residual is admissible or what happens when it is nonzero-but-small. This hurts because public token means and price digits are rounded: an exact-equality rule will either spuriously fail the first genuine M_W identification (the one thing the Plan ranking entirely lacks today) or leave "compatible" undecidable, and the draft's own principle elsewhere (E141's 10⁻⁶ tolerance) shows the build needs a number. Recommended change: define the admissible band — exact to 10⁻⁶ relative when the demand object derives from the cost's own source, and ≤ half of the source's last published digit when it comes from another public page — enumerate the compatibility_status outcomes for each side of the band, and add a fixture with a rounded token mean landing inside and outside it.

Low

The bar-setter property is asserted from the wrong premise. Part 10 claims "a frozen level is never a configuration, so no bar returns its setter by construction". The property does not follow from the level's ontology: the ladder level is some population row's displayed quality, so whether that setter can qualify depends entirely on the strictness of the qualification inequality (≥ H lets a complete-leaved setter qualify weakly at exactly H; > H never does), and part 10 states that inequality nowhere. Recommended change: record the strictness explicitly in the E156 policy object and add a fixture showing a complete-leaved setter under it.

E155's S1T label misdescribes one varied target. The printed S1T description — "published-record leaf values redrawn with task-sampling noise (independent-task approximation)" — does not name GDPval-AA's fitted-rating interval draw, which O39 reads as a 95% normal interval and which is not task sampling. The per-stream target object would disclose it, but the fixed E155 text printed beside every uncertainty output would not. Recommended change: amend the E155 S1T string to name the GDPval-AA draw and its analyst-derived kernel mark.

The O98 justification is imprecise. Part 10 says the [C, ∞) domain for a factor-less pricing omission "is sound because every label test reads a competitor's lower cost, so the factor only narrows possible memberships". Since both [C, factor×C] and [C, ∞) contain the published cost as their lower end, the recorded factor changes no other row's label or membership test at all; its only effects are the O94 row's own interval range and its O114 scenario draw. Recommended change: reword so the register does not imply the factor participates in competitors' membership tests.

2. Methodology design recommendations

Mean-preserving alternative for S1T binomial leaves (highest priority, pairs with the first Medium finding). Register, beside the O142 Jeffreys draw, an alternative kernel with E[draw] = published score and the same spread: x = p + (Beta_draw − (k+½)/(n+1)), clipped to the leaf domain only where it exits it (and the clip rate published), or a truncated normal at the score with the Jeffreys SD. Publish scenario shares under both, per the existing E25 alternative-kernel convention, and print the maximum per-leaf mean shift 100·((k+½)/(n+1) − k/n) with each S1T table. At the current counts this is ≈ 12.5 points (LiveBench Data Analysis at 100%), ≈ 6 points (AI Coding Daily wide reading at 90%), and ≈ 0.1 points at HLE-Diamond's n = 1,000, so readers can see exactly where the shrinkage matters. Spot-check of the underlying n's: Terminal-Bench 4.0's 66 tasks and HLE-Diamond's 1,000 questions both match the draft's figures, so the n registry is accurate and the fix is purely a kernel change.
hub.harborframework
+2

Attribution package for the failed cross-check. On the AI Coding Daily panel (n = 20), compute leave-one-component-out τ_b over the E172 cost family, the top-five rank inversions with component-cost shares, and the O116 with-index variant — all from captured data, all beside the existing README warning, in scores.json under the existing diagnostics.workloadCrossCheck object.

Numeric reconciliation tolerance for E84, as specified in the Medium finding, with the two-source distinction (same-source exact; cross-source bounded by published precision).

Bar-qualification strictness in the policy object (a one-line addition to E156: qualify ⇔ full-composite bound strictly above H, or weakly above, with the setter fixture).

Two wording amendments: the E155 S1T description (name the GDPval-AA draw) and the O98 parenthetical (the factor affects only the O94 row's own outputs).

3. Questions for the owner

On O142: given the measured mean shifts at n = 3–6 (up to ~12 points at the leaf level, feeding LiveBench 2.0 Overall and the AI Coding Daily ranking's S1T shares), would you accept publishing a mean-preserving alternative kernel beside the Jeffreys draw, or is the Jeffreys draw alone intended to stand?

On E84: is the reconciliation intended to be exact only when the demand object derives from the cost's own source, with a bounded residual allowed for cross-source demand objects — or exact in all cases? The answer determines the tolerance design in recommendation 3.

On the workload cross-check: should the τ_b attribution diagnostic be a published release artifact beside the ranking, or research-record only? The answer determines whether recommendation 2 changes the README warning itself.

4. Verdict

VERDICT: HAS FEEDBACK