0. Read check

Both listed parts were opened through the GitHub connector at commit ce7c11f064d17d1f947ebf5e0389c366df0b335d and read to their end.

Part 1 (research/2026-10-19-methodology-codesign/perplexity/parts-r178/draft-r178-part-1-of-15.md)

First line: "# ValueRank methodology — draft r178"

Final sentence: "Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source."

Part 2 (.../draft-r178-part-2-of-15.md)

First line: "- Two rankings (owner decisions O52, O53, O54): ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52)."

Final sentence: "Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36)."

Both parts read fully; proceeding to the review. (No web search was used: every externally checkable claim in these parts concerns the repository's own October-2026 evidence world, which live web search cannot verify; findings below are internal-consistency and design issues, with the two open factual questions routed to the owner in section 3.)

1. Findings by severity

Critical

None.

High

Third-party board version changes are absorbed as routine re-captures, not migrations (E237). The comparability record stops the build on a missing or different version for gap fills (Bug Hunt, Terminal-Bench), and an AA chart/field change is a versioned methodology migration (E31), but for the added boards — Vals, LiveBench 2.0, AI Coding Daily — "a version change there is a new capture under O59" . This means that if Vals ships Vibe Code v1.2, LiveBench changes a release's structure rather than editing values in place (the O147 pattern), or AI Coding Daily restructures its 60-point columns, the leaf is silently re-captured and scored under the same registered leaf name and weight. That breaks exact-variant comparability across releases — the core of ValueRank's claim scope — and can silently move scores, anchors and bars with no owner decision and no ledger entry. Change: extend E31's migration principle to every registered leaf source: the build hashes each captured board's (benchmark version, metric field, task/column composition) against the registry and stops on any change; the owner then records a migration (new leaf ID, explicit weight-continuity decision, or dated re-registration). Only in-place value edits within the same version (LiveBench 2026-10-30 style, both values recorded) stay absorbed.

Medium

Off-by-one inconsistency between the near-gap rule and the edge diagnostic. The near gap is "rounded Index within 3 points of the frontier's best at equal or lower cost" (inclusive), and the edge diagnostic lists configurations "one rounded Index point inside the edge" — which should mean gap 2 — yet Claude Sonnet 5.5 (max) is simultaneously listed there and described by E193 as "at gap 3" . With an inclusive 3-point integer gap, a row at gap 3 is on the edge, not one point inside it. This hurts because cohort membership is the population every claim ranges over; two stated figures that cannot both be right suggest the rule and the diagnostic compute different gap notions (rounded vs chart-precision), and a reader cannot tell which rows would flip on an AA re-capture. Change: define the gap once (integer difference of rounded Index values), print each edge-diagnostic row's integer gap and flip direction, and state whether E193's primary gap is rounded or chart-precision.

The max-effort ranking's effort claim is unverified per row. Part 2 states the leading ranking "holds one configuration per family at the vendor's top effort" , but O54 takes MiMo-V2.6-Pro's results at high ("its AA configuration"), and Gemini 4 Argon sits at high in the max-effort ranking alongside (max) rows of other families. Unless high is those vendors' documented top effort, the site-default ranking's name and claim scope misdescribe some rows, and buyers comparing "max-effort" configurations are comparing mismatched effort tiers — directly weakening the objective's "value delivered in practice" framing. Change: add a per-row effort-tier column — vendor-documented top effort (yes/no, with the vendor documentation link) vs highest-covered effort — flag rows whose effort was set by benchmark coverage rather than the vendor, and correct the sentence if any row is not at the vendor's top.

Owner decision challenge (O121/O53): the common-leaf ranking's label ban no longer tracks an epistemic boundary. The common-leaf diagnostic ranking covers 33 configurations (8 ranked nowhere else) with its own frozen anchors, bars, basket admission and scenario run, yet "earns no interval or scenario label" . New argument: the ban's plausible rationale — cross-effort comparability — is not respected by the labeled AI Coding Daily ranking, which mixes high and medium efforts and includes MiMo-V2.6-Pro at high. So the labeled/diagnostic boundary now tracks third-party source coverage, not evidence quality, and the objective's question has no official answer for 12 excluded configurations and only a no-label answer for 8 more, while the leading ranking answers it for 9 of 37. Change (owner choice): grant the common-leaf ranking label eligibility under its own already-frozen anchors, or keep O121 but print beside its bar answers "no label by owner policy, not for want of evidence", so readers cannot mistake the policy ban for an evidence gap.

Cost sampling noise is asserted absent rather than tested. The separability threshold draws only the quality SD, on the claim that "AA publishes one cost pass per configuration and no per-task cost dispersion for the Index evaluations", with the net direction "not established" (E340) . But the pinned Coding Agent Index cost is itself a per-task average (mean.costUsd × 290 tasks, O27) , so per-task cost data plausibly exists in AA's raw evaluation dumps; a task-level bootstrap would give a real cost SD for at least the basket's SDLC components. This hurts because the separable count and the E242 transfer tolerance are the methodology's honesty layer, and one side of their noise budget is currently an untested assumption. Change: bootstrap per-task costs (B ≥ 1000) for every component that publishes them, publish the resulting cost SD and a two-sided separability threshold as a diagnostic beside the current one; if the per-task data truly is not public, the existing disclosure stands as the best available.

Low

The parenthetical "(today 6 and 14)" in "Counts, defined once" attaches grammatically to "denominator" but gives the threshold ⌈2N/3⌉; N today is 9 and 20 . Change: "(today N = 9 and 20, so thresholds 6 and 14)".

E214's fallback matching is asymmetric. It covers "record silent on fallback → matches" and "record explicitly 'without fallback' while AA plots 'with fallback' → no match", but not the mirror case (record explicitly "with fallback" while AA plots the model without it) ; exact-variant policy implies no match, but the rule should say so. Change: state that an explicit fallback-state mismatch never matches, in either direction, pending a dated matching decision.

Identical flag counts 21 and 60 appear for both "route flagged possibly superseded" and "valuation basis not recorded" ; the joint count is published (reviewer 78), but the pairwise overlap of these kinds is not, and identical numbers invite a duplication suspicion. Change: publish a per-basis flag-kind overlap matrix in scores.json planRows[].flags.

O145's retention sentence contains a non sequitur. "A retained row is ranked only with every leaf of a ranking, like any cohort row, and so is never retained twice in a row" — the one-release cap is definitional (O145/E306), not a consequence of leaf completeness, and an implementer could misread leaf status as controlling retention length. Change: drop "and so" and cite E306's plotted/retained/out state machine. Relatedly, the E240 rejection-reason list ends with the garbled item "judged against the final release cutoff V after any O65 re-capture moved it, not a score" — clarify what "not a score" rejects.

2. Methodology design recommendations

Prioritised; all implementable from public data refreshed routinely.

Leaf-version migration gate (fixes finding 1). Register a tuple (source, leaf, benchmark version, metric field, task/column composition, aggregation) per leaf in the evidence bundle; at build, hash the captured tuple and diff against the registry. Match → proceed; in-place value edit within the same version → absorb, record both values (O147 pattern); version/metric/composition change → build stop, owner decision recorded as a versioned migration with a new leaf ID and an explicit weight-continuity ruling. This makes "whether a leaf is missing" — already a deterministic function of registry and capture (E239) — extend naturally to "whether a leaf is still the same leaf".

Cost-noise-aware separability diagnostic (fixes finding 5). For each component with published per-task costs, bootstrap the component cost; combine per-row assuming component independence (or report per-component). Since the cost score is linear in ln C between anchors, the row's cost-score SD is ≈ 100·SD(ln C) / ln(c_H/c_L); the value SD becomes √((0.25·SD(S_C))² + (0.75·SD(Q̄))²) and the pair threshold 1.96·√(SD_i² + SD_j²) under ρ = 0. Publish it beside the current quality-only threshold with the E340 caveat resolved into a measured direction for the bootstrappable components.

Per-row effort-tier disclosure (fixes finding 3). A column: effort, "vendor top? (Y/N, link to vendor docs)", "effort set by (vendor top / highest covered)". The ranking header prints how many rows are at vendor-top vs coverage-set effort. This also documents the selection effect that families whose top effort is dominated off the frontier cannot enter the leading ranking at all — currently only implicit in the listed-configuration tables.

One gap definition, published per edge row (fixes finding 2). Define gap = (frontier best rounded Index at equal-or-lower cost) − (row's rounded Index), an integer; the edge diagnostic lists rows with gap ∈ {2, 3, 4} with their integer gap and flip direction on the next capture.

Label-policy alignment (fixes finding 4, owner choice). Minimal version costs nothing: add the sentence "no label by owner policy, not by evidence" beside the common-leaf ranking's bar answers, which O172 already places in each leading headline.

Spec micro-fixes (findings 6–9): the N/threshold parenthetical, the symmetric E214 rule, the flag-overlap matrix, and the O145/E306 wording.

3. Questions for the owner

Is "high" the vendor-documented top effort for MiMo-V2.6-Pro and Gemini 4 Argon (their rows in the max-effort ranking)? If not, would you accept the per-row effort-tier disclosure (recommendation 3) or a ranking rename? (Changes finding 3.)

Does AA's published raw data for the Coding Agent Index v2.0 (and the other basket components) include per-task costs beyond mean.costUsd? This decides whether recommendation 2 is implementable or whether the current E340 disclosure is the ceiling. (Changes finding 5.)

In E237, was "a version change there is a new capture under O59" intended to cover changes in an added board's benchmark version or column composition, or only re-captures of an unchanged version? (Decides whether finding 1 needs a rule or only a wording fix.)

4. Verdict

Parts 1–2 are internally consistent on every count I could check (plan-row flag arithmetic 14+2+11=27 and 42+3+22=67; 9+20−4=25 of 37 ranked; 9 plotted + 6 retained-only families = 15; adjacent-pair counts 8−2=6 and 19; the E183/E209 panel populations all reconcile), and the honesty machinery around the Plan basis and noise disclosure is strong . The material issues are the E237 version-change hole, the gap off-by-one, the unverified effort-tier claim in the leading ranking, and the untested cost-noise assumption.

VERDICT: HAS FEEDBACK