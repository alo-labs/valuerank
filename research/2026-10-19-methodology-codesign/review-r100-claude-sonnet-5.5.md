0. Read check

I read all 15 parts through the GitHub connector at commit f48b9230…, one file read per part, each to its end. Before the first read I made one tool-listing call and one schema call, because the connector protocol requires the schema before a call. I used no web search. The review rests on the draft's own text and numbers, so I cite no external sources.

First line: # ValueRank methodology — draft r182

Final sentences, in order. Where a sentence is very long I quote only its closing clause, marked with "…".

"A change of AA chart or field is a versioned methodology migration, never a silent refresh."

"…a family with an excluded primary may have other efforts ranked."

"Both priced executions stay in the basket as the owner listed them; the overlap is disclosed."

"These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status."

"…the transfers keep their assumption label and caution."

"…a transfer from a lapsed report donor, which is diagnostic."

"…GPT-6 Astra (max)'s selected route moved from ChatGPT Plus to a higher plan under O45."

"AA Intelligence Index and output speed are diagnostics, not quality."

"…repetitions are not a bias."

"Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support."

"The current ladders are in Output 3 and scores.json barCurrency."

"…the summary says these outputs compare ranked configurations only and names the listed configurations."

"A benchmark-version change triggers a comparability review with dual-run where feasible."

"…a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);" This part ends mid-sentence, and part 15 continues it with "a point without a captured page is captured within the window, its common revision unverified."

"Revision history: omitted from this review copy (not normative); it is in draft-r182.md in the same folder of the repository."

All 15 parts were read to their ends. The revision history is excluded from the parts. I did not count characters, so I cannot confirm the 345,330 total.

1. Findings by severity
Critical

None.

High

H1. The AI Coding Daily ranking prices mostly non-coding work but scores coding quality.

The draft says the Coding Agent Index is pending there (7 of 20 rows against a threshold of 14), so its basket holds no coding-agent unit. Its coding share is "far lower" than the max-effort ranking's, which already spans 16–74% (Cost bullet; Known limitations).

The AI Coding Daily quality vector is 60% software engineering, and its coding-specific share is 60%.

The cost basket there is the six Index SDLC evaluations. Briefcase, GDP.pdf and AutomationBench (657 tasks) carry no coding quality leaf. Only FrontierCode 2.0 and Terminal-Bench 4.0 (plus Terminal-Bench-Science) match the quality side.

The draft's own E41 check shows the consequence. Basket-cost rank against Terminal-Bench cost-per-resolved-task rank has τ_b 0.35 on 20 rows, below the 0.5 threshold, and the warning only rides along on labels (O160).

This is new against the ledger's rejection of "basket is mostly office work" (I4 M1). That rejection rested on a coding share of 53% over 33 rows under the pre-v5 basket. The v5 basket (O137) plus the pending Coding Agent Index removes that basis for this ranking.

Why it hurts: the question is cost "for the value it delivers in practice". Here the cost axis largely prices work the quality axis does not credit, and the cost allocation is already −55% on the API basis.

Change (Owner decision challenge to O15/O137, for this ranking only): until the Coding Agent Index is admitted, publish the component-wise cost score of §2 item 1 as a first-class column beside the headline, not only as a leave-one-out diagnostic. Print the ranking's coding cost share (E200) in the headline, as it already is for the max-effort ranking.

H2. Owner decision challenge (O54, O121, O172): the leading ranking cannot see the cheap end of the frontier.

The max-effort ranking has 9 rows from 9 of 15 families. It ranks one effort per model only because LiveBench and Vals run one effort per model.

Its own listed rows include rendered-frontier points far outside its anchors. GPT-6 Luna (low) is 7.10× below the low anchor on API cost, GPT-6 Luna (medium) 1.54× and Claude Haiku 5.5 (low) 1.53×. Plan gaps reach 70×.

"Cheapest above a bar" in that ranking is therefore an answer among the dearer efforts by construction. The bars come from a 9-row ladder (positions 2, 4 and 6), and only 2 of 6 adjacent API ranks are separable.

O143 and O172 mitigate this by printing a pointer and the common-leaf answer. The common-leaf ranking covers 33 rows with ten leaves at the same 60% software-engineering weight, but it carries no labels by policy.

Change: lead the site and README with the ranking that covers the question, which is the common-leaf ranking. The 34% independent-board weight in the max-effort ranking is a validation benefit, so keep it as the "independent-boards" companion. If the owner keeps O54, the headline must say in one sentence that the leading ranking excludes the frontier's cheapest efforts. Today that appears only in listed-row detail.

Medium

M1. Ordinal rank stays the primary output although the draft shows it is mostly noise (O152; new argument).

The draft reports 0 of 19 adjacent AI Coding Daily ranks and 2 of 6 max-effort ranks as separable.

The median thresholds, 3.3 to 4.5 value points, equal about 1.2–1.6 cost doublings. The cost exchange rate is 2.71–3.11 points per doubling on the API basis.

The threshold also omits cost noise, run-to-run variance and harness variance, and the draft says its net direction is unknown.

The noise-band rule is forward-only and order-dependent. It says adjacent rows in different bands may also be inseparable.

Change: add the order-independent credible rank of §2 item 2. It uses pairwise frequencies the engine already computes (E96).

M2. Bug Hunt gives about half its scale to unrequested fixes (O163/O170; Owner decision challenge).

The draft's own fixture has board maxima of 57 planted and 65.3 unplanted fixes. Unplanted fixes are therefore about 53% of the leaf's ceiling.

Unplanted fixes are judged by the maintainer's LLM judge, have no answer key or ceiling (the draft says so), and are modelled as Poisson.

Real software-engineering value does not clearly reward unrequested edits. Scope creep is a cost in practice.

The leaf is weighted 8%, 12% and 15% across the three rankings. It is the only independent leaf in the common-leaf ranking, it rests on two TypeScript repositories, and its means often have small N.

Change: publish a planted-only variant of the leaf as a standing sensitivity with value and rank changes. The pre-O163 leaf is already computed. Consider capping unplanted credit, for example at the planted ceiling's share.

M3. Plan evidence cannot be reproduced from public data, which conflicts with the "public data, refreshed routinely" constraint.

Every controlled measurement comes from one paywalled article. The draft says the article is not captured in the bundle and has no content hash (E238).

The build only needs a hand re-read every 30 days (O130).

Report intake depends on proprietary "Deep Research" stages (Claude, Silver Bullet), and Reddit, X (HTTP 402) and YouTube were unreachable.

E159's promise to rebuild from the bundle "without consulting live pages" therefore holds only for a transcription.

Change: add an evidence class "attested transcription (non-reproducible)". Record the reader, access method, date and a hash of the transcribed table. Print that class beside every Plan figure, not only in E238. Keep the Plan headline labelled exploratory until at least one measured route is reproducible from a public artifact.

M4. The specification has no independent check that it is unambiguous.

It is about 345k characters with more than 330 editor rules. It states that conflicts between rules happen and are defects, and it resolves them by "later-numbered record governs".

Rule density now exceeds what a public reader or a second implementer can verify.

Change: split a normative core of roughly 30k characters. It would define the cost basket, anchors, leaf z-scores, weights and value score, with all gates and diagnostics in an appendix. Add a second, independently written reference scorer, about 300 lines, as a CI check. It must reproduce scores.json from the evidence bundle. Disagreements are specification bugs.

M5. Anchors are cohort-derived, so the scale resets at nearly every release.

Anchors are c_L = min/2 and c_H = max×2 over reference rows. They are re-frozen at O47, O65, O132 and a3→a4.

O47 and O132 had no computable dual run. Value scores are therefore not comparable across releases. Even ranks have lacked a bridge twice in two weeks.

Change: snap anchors outward to a 1–2–5 dollar grid, as in §2 item 3. Small cohort changes would stop forcing re-freezes, the clip gate would fire less often, and an old-versus-new bridge would be computable more often.

Low

L1. Cross-check coverage. The E41 workload check uses Terminal-Bench only, since DeepSWE left. AA publishes cost per task and scores for FrontierCode 2.0 and Terminal-Bench-Science too. Add them as separate panels (never pooled), so a 0.35 warning can be attributed.

L2. Group label. The 60% "software engineering" group includes LiveBench Overall at 15%, whose categories are only 3.5/9 coding-related. The coding-specific share is 51%, so about 9 points of "SWE" weight is general capability that overlaps AA's reasoning and research leaves. The share is already printed, so I suggest renaming the group "software and agentic work" in the headline.

L3. Bar level. The bar is an element of the ordered population (O34), so the setter sits exactly at H and its interval always straddles it. The draft says this explicitly (E201b: 4 against 5 confirmed against possible qualifiers). Midpoint bars between adjacent order statistics would remove that artefact without changing the ladder's intent (Owner decision challenge to O34).

L4. Claim wording. Interval and scenario labels certify stability only to rounding of the published record (O25). Pair every label in the README with its O171 screen status ("passes the screen", "contested" or "rounding-stable only"), so a label is not read as statistical confidence.

L5. Task-correlation assumption. The ρ = 0 assumption in the separability threshold is unresolved, and the grid (0, 0.3, 0.6) is arbitrary. Estimate ρ from a board with public per-task results, such as the tbench.ai per-task data, and publish it as an empirical anchor for the grid.

2. Methodology design recommendations

Priority order, most important first.

Component-wise log-cost score, with quality-matched weights (Owner decision challenge to O15; offer as a sensitivity column first).

For each execution family g (FrontierCode 2.0, Terminal-Bench 4.0, Terminal-Bench-Science, Coding Agent Index, and so on), compute the cost score S_C,g = 100·clip((ln c_H,g − ln c_ig)/(ln c_H,g − ln c_L,g), 0, 1), with anchors per family built by the existing ln 2 padding rule.

Use weights ω_g taken from the quality leaves that reference the family (E55's mapping). Define S_C = Σ_g ω_g S_C,g / Σ_g ω_g over the available families, and V = 0.25·S_C + 0.75·Q.

The cost score is already linear in ln c, so this is the weighted geometric-mean cost. It makes cost shares track quality shares, removes dependence on AA's arbitrary task multiplicities (AutomationBench 657 against Briefcase 91), and handles missing components by renormalising, as quality already does.

It removes the 2^n admission enumeration, the subset workloads (O17/E10) and the forced migrations (the v5 migration lost GDPval-AA, SciCode and LCR costs). Quality-less costs (Briefcase, GDP.pdf, the SWE-Atlas share of the index) drop out of scoring but stay in the diagnostics.

The cost: per-family anchors, and Coding Agent Index agent confounding (O123) stays.

Credible rank and tier.

Define the credible rank as r_i = 1 + #{j : f_ji^> ≥ 0.90}, where f_ji^> is the S1T share of scenarios in which j outscores i. The pairwise win, tie and loss shares already exist (E96).

Print the median rank and a 5–95% rank interval beside it. Keep the sort order and the displayed ordinal rank. Report the tier count at ρ = 0, 0.3 and 0.6, and publish MC standard errors per E72.

Because the threshold omits cost noise, label the tiers "quality-noise tiers".

Snapped anchors.

Use c_L = 10^(⌊log10(min/2)·3⌋/3) and c_H = 10^(⌈log10(max·2)·3⌉/3), a 1–2–5 style grid.

Keep the clip gate and the dual run (O12). Re-freeze only when a ranked row leaves the snapped range. Publish the exchange rate per doubling, now 3.11 and 2.71 API points.

Bug Hunt.

Standing sensitivity: planted-only, and unplanted capped at min(U, λ·P) with λ = 0.5.

Publish the share of the leaf's variance coming from the unplanted part per release.

Keep the ±10% scale stress (O173).

Cohort-recall diagnostic using AA data alone.

AA's nine Index leaves exist for all 82 plotted points. Score every plotted point on those nine leaves, with cost on the same basket, and report how many top-k and cost-quality-frontier members fall outside the cohort.

This leaves the cohort rule untouched (fixed policy). It tests whether the AA-Index-based cohort loses configurations that matter to ValueRank's own objective.

Attribution panels. Add FrontierCode 2.0 and Terminal-Bench-Science cost-per-resolved-task panels to E41. Report τ_b by panel and name the component with the largest leave-out change.

Reproducibility.

Build the reference scorer and the normative core (M4).

Add the attested-transcription class and print it beside each Plan figure (M3).

Make the evidence-class column part of planRows.

3. Questions for the owner

What is the AI Coding Daily ranking's coding share of basket cost (E200 median and range, diagnostics.basketReadiness)? If it is below about 40%, H1 stands as High and recommendation 1 should become the AI Coding Daily headline cost. If it is 50% or more, H1 drops to Medium.

Is O163's unplanted credit meant to reward beneficial extra fixes? If the maintainer's judge also checks for regressions or scope creep, M2 weakens to Low. If not, a capped or planted-only primary leaf is the better choice.

Would you accept the component-wise score of recommendation 1 as a sensitivity column for one release before deciding on O15?

4. Verdict

VERDICT: HAS FEEDBACK