0. Read check

All three listed parts were opened through the GitHub connector at commit d53cec1 and read to their end.

Part 8 (draft-r154-part-8-of-13.md) — first line: "- Added leaves (owner decisions O53–O55; E252, E256, E257): their evidence is data/swe_tracks.json, built by research/2026-10-23-swe-benchmarks/build_swe_tracks.py from the verified coverage captures …" (line continues through the coverage-capture parenthetical). Last 12 words: "predictive run-to-run variation, and only interpretations the public evidence supports are published."

Part 9 (draft-r154-part-9-of-13.md) — first line: "Results are published per stratum (S0, S1, S2; transfers on/off; leave-AA-out), never averaged into one figure, as scenario shares … labelled as scenario frequencies, not probabilities." Last 12 words: "quality H is. It is selected before any bar outcome is computed."

Part 10 (draft-r154-part-10-of-13.md) — first line: " - Ladder positions (O34): with the population's n displayed qualities in ascending order, bar level H_k (k = 1, 2, 3; …) is the value at zero-based position floor((n − 1)k/4), an element of the order, never an interpolated percentile." Last 12 words: "says these outputs compare ranked configurations only and names the listed configurations."

1. Findings by severity

Critical

None.

High

None. The parts are internally consistent on the checks I could verify arithmetically: the E92 kernel-check fixture (70 observed points at 100, three 10-point missing leaves, bar at 78 → ΣU ≥ 80; uniform ≈ 91.5%, arcsine ≈ 86.7%) is correct; the E152 basis-typing fixture (100 − 20)/4 = 20 is correct; the ladder positions floor((n−1)k/4) for n = 32, 9, 15 and the ⌈n/2⌉ headline claim are correct; E201b's "displayed quality of at least about H/p" follows from Q_i^L = (Σ_observed w·z)/100.

Medium

Owner decision challenge (O44): the noise-margin companion's formula contradicts the framework's own treatment of the bar level, and uses one median SD for all rows. Part 10 defines the margin as 1.96 × √2 × the median per-row analytic quality SD, but E52 (same part) states the frozen level "has no uncertainty of its own" (Q_r(θ) = Q_r(s) = H for every state and scenario), and O25 makes interval outputs robust to reporting precision of the published record — nowhere else is H treated as a noisy quantity. The √2 factor silently re-imports the setter's freeze-time noise that the rest of the machinery excludes. Worse, the single median SD mis-sizes the margin per candidate: rows whose quality is concentrated on small-n leaves get an understated margin, quiet rows an overstated one, so the named "cheapest configuration clearing the bar by the margin" can be the wrong row. The 95% z (1.96) also sits unexplained beside the labels' 90% convention. Why it hurts: this companion is a published reading buyers may act on, and its construction is inconsistent with the deterministic-H contract every label rests on. Change: define the margin per candidate as z_q · SD_i against the fixed H (z_q stated and either aligned with the 90% convention or justified), keep the √2-median variant as a labelled "setter-noise sensitivity," and publish each candidate's SD_i and margin beside the companion.

The scenario-label guarantee is per event and uncorrected across the candidates a bar lists (E77, E198a). Each candidate's ≥ 90% label is certified at per-event error ≤ 0.05 (δ = 0.05/16 per look, Bonferroni over the 16 looks), but a bar that lists several candidates tests each separately, so the family-wise probability that at least one non-supported row carries a label grows with the candidate count and is neither bounded nor quantified — only disclosed beside the candidates. Why it hurts: the label's published wording ("supported under all registered role-group kernel checks") invites a stronger reading than the certificate supports once several candidates compete at one bar. Change: apply Holm–Bonferroni across the candidates of each bar's declared event family (E77 already declares the family and its size in the release manifest, so the correction is mechanical), or at minimum publish a Šidák-style family-wise lower bound beside each label. Cost is at most slightly fewer labels, which the release-gate machinery already tolerates.

LiveBench 2.0 Overall's S1T SD counts parts for the two composite categories, with no narrow counterpart published — an asymmetry against AI Coding Daily's dual reading. Part 8 sets Reasoning (4 tasks) and Data Analysis (3 tasks) to their parts counts as "the wide reading," so within-task clustering (several short questions per task) understates those categories' SDs, and the release's weights w_c then propagate the understatement into LiveBench Overall's leaf SD. Unlike AI Coding Daily, where both the n = 6 and n = 60 readings are published, no task-count reading is published for LiveBench. Why it hurts: the analytic per-row quality SD that this leaf feeds is exactly the quantity the separability threshold and the O44 noise margin use, so robustness figures for LiveBench-heavy rows are optimistic — and the terminology itself now points both ways ("wide reading" means larger variance for AI Coding Daily but larger n here). Change: publish the task-count reading (n = 4 and n = 3) beside the parts reading, add a design-effect sensitivity (inflate the category SD by 1 + (m − 1)ρ over a small ρ grid, labelled conventional), and unify the wide/narrow naming so it always refers to the variance direction.

Low

E268's harness-matching fallback fires silently. When the AI Coding Daily row matching the Bug Hunt record's harness is absent or ambiguous, the record falls back to the latest test date with no flag in the published output (the alternates are carried, but the reason the fallback fired is not). Change: publish a harness_match: matched | recency_fallback field on the leaf's provenance.

The AA-Omniscience S1T SD is not stated as a formula. Part 8 says only "6,000 questions scored +1/0/−1 with shares from AA's accuracy and hallucination rate." The trinomial variance of I = 100(a − h) — (a + h − (a − h)²)/n per question — should be printed in the registry so the leaf's SD is auditable like the others.

GDPval-AA's independent draws ignore shared-matchup covariance, disclosed in prose only. Part 8 acknowledges the fitted Crowd-BT ratings covary through shared matchups but draws them independently. A cheap quantified bound exists: a named one-parameter shared-factor stress that shifts all rows' ratings together within their displayed interval widths, published as a sensitivity. This matters most for pairwise ordering shares (E96's f_ij), where common-opponent correlation is exactly what independent draws miss.

Bar-population reach counts need a one-clause reconciliation. Part 10's E207 counts 16 bar-population rows in the AI Coding Daily ranking against the 15 ranked rows; E243 explains the mechanism (full-benchmark rows without a cost stay in the bar population), but the reach table does not name the extra row or its reason. Add the bar-population row list (or per-row reason) beside barCurrency so the two counts reconcile in the published output.

2. Methodology design recommendations

Prioritised, all implementable from captured public data:

Per-row noise margin (fixes Medium 1). For each bar and basis, publish a margin table: candidate, SD_i (the same analytic per-row SD the separability threshold uses), margin = z_q · SD_i with z_q = 1.2816 (90%, aligned with the label threshold) or 1.96 (95%, stated as a deliberate stricter convention), and the cheapest row clearing H by its own margin. Keep the current 1.96·√2·median-SD figure as a labelled "setter-noise sensitivity" so O44's existing output is preserved as a variant rather than deleted.

Family-wise label control (fixes Medium 2). At label time, take the bar's declared candidate family (already in the release manifest under E77) and run Holm over the per-event p-values implied by the Clopper–Pearson lower bounds; publish per-candidate adjusted lower bounds. Because E77's certificates already record k, n, L and U per event, this is a post-processing step on existing objects with no new sampling.

LiveBench category dual reading (fixes Medium 3). Add to the S1T stream manifest a livebench_category_counts object with both readings (parts vs tasks) per category and the two resulting LiveBench Overall SDs; print both beside every separability figure that uses the leaf, mirroring the AI Coding Daily narrow/wide presentation, and register the design-effect grid as an S1Ttion, and register the design-effect grid as an S1T