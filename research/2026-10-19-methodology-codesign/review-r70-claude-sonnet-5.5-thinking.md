0. Read check

First line of the draft: # ValueRank methodology — draft r152

All 13 parts were read through the GitHub connector, each to its end. The last 12 words of each part:

"carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py)."

"their own subset (the seven Index evaluations), flagged "subset cost" (O17, E254)."

"on the Plan basis the workload question is the M_W identification status."

"for other Claude models; the transfers keep their assumption label and caution."

"(no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

"value; no epsilon is introduced. Domain validity is separate from evidence completeness."

"Daily on a harness chosen per model) are disclosed as a limitation."

"predictive run-to-run variation, and only interpretations the public evidence supports are published."

"with a displayed quality, ordered by displayed quality ascending, then configuration ID."

"says these outputs compare ranked configurations only and names the listed configurations."

"or definite result; every cost check reads C_W, never the Index diagnostic."

"article changes nothing until the owner selects it (AGENTS.md; Plan cost, E238)."

"normative); it is in draft-r152.md in the same folder of the repository."

Part 13 says the revision history is omitted from this review copy, so it was not reviewed. I ran no web searches because the tool budget went to the 13 reads, so every finding below rests on the draft's own text and arithmetic. No external facts are cited.

1. Findings by severity

Critical

None.

High

None.

Medium

Owner decision challenge (O52, O53, O54): the leading ranking structurally leaves out the cheapest frontier points.

Issue: the max-effort ranking ranks 9 of 30 cohort configurations and the AI Coding Daily ranking 16. The draft says LiveBench 2.0 and Vals run each model once at its top effort, so cheaper efforts are structurally unranked. The draft also lists the cheapest rendered-frontier points as unranked. These include GPT-6 Luna (low/medium/high) and the Claude Haiku 5.5 efforts, shown as listed rows below the anchors in the clip-gate list.

Why it hurts: the objective is the lowest cost for the value delivered among frontier models. A "cheapest above the bar" answer drawn from 9 top-effort rows cannot see cheap-effort configurations, which are the likeliest to win that question. E201c and O43 disclose this, and the indicative values are labelled "not comparable". Disclosure is not coverage. Part 2 states that only MiMo-V2.6-Flash and MiniMax-M3.1-Flash lack Bug Hunt. The other excluded rows lack only the added leaves.

New argument, if O53 already weighed this: the ten-leaf set that O49 left (FrontierCode, Terminal-Bench, Bug Hunt and the seven non-SWE leaves) would cover about 28 of 30 rows. Any decision to drop it should state the bar-result cost of that coverage loss.

Change: publish a third, diagnostic-only coverage ranking on the ten common leaves, with its own frozen ladder. Beside each bar, print whether its cheapest qualifier differs from the two leading rankings' cheapest qualifier. Keep it out of the headline and out of labels.

The "software engineering 60%" claim overstates SWE emphasis in the max-effort ranking, and the overlap policy is inconsistent.

Issue: the leaf table files LiveBench 2.0 Overall (15 points) under "Software engineering (60%)". It is the mean of seven categories (Long Agentic, Reasoning, Coding, Browser, Data Analysis, Research, Design) with weights 2, 1, 1.5, 1, 1, 1, 1.5.

Arithmetic from the draft's own weights: coding-specific leaves (FrontierCode 15, Terminal-Bench 11, Bug Hunt 8, Vibe Code 5, Code Migration 6) total 45. Adding LiveBench's Coding and Long Agentic share, 15 × 3.5/9 ≈ 5.8, gives about 51. That is not 60, and AI Coding Daily's four leaves really are 60.

Overlap: AI Coding Daily's bug-finding column is excluded because it overlaps Bug Hunt. LiveBench's Coding and Long Agentic categories overlap FrontierCode and Terminal-Bench, yet they stay in.

Why it hurts: the objective weighs real SWE work against general capability. The two rankings differ in true SWE share, and the max-effort ranking's SWE tilt is misreported. The hierarchical weight draw (Dirichlet on the 0.60 group) also treats LiveBench as SWE.

Change: print a "coding-specific share" per ranking, using the formula above with LiveBench decomposed by its own category weights. Put LiveBench in its own "agentic and general" group in the leaf table and the Dirichlet hierarchy. Add a named sensitivity that re-weights LiveBench to its coding-adjacent share only. Keep the owner's 15-point weight; this changes labelling, not scores.

The coding-agent cost component prices each model's vendor harness, and the draft does not say whether the quality leaf comes from the same execution.

Issue: Coding Agent Index rows are "agent - model (effort)", for example Codex or Claude Code. That index is the largest cost component where admitted; the draft's coding-share diagnostic is said to be far higher in a ranking that admits it. E227 and E19 treat harness effects only on the quality side. The same-execution contract (E68) covers only the Terminal-Bench cross-check. The draft does not state whether the FrontierCode quality field is the Coding Agent Index run or a different AA run.

Why it hurts: if a vendor agent is more token-hungry, the model is charged for the harness, and the cost score (25% of value) moves with it. The draft's leave-one-component-out family (E172) shows sensitivity to removal but cannot separate model from harness.

Change: publish each row's Coding Agent Index agent and a flag for whether it equals the quality leaf's execution. Estimate a harness cost effect from models that AA lists under two or more agents, with log C(m,a) = α_m + h_a, as E19 does for tbench.ai. Publish the rank change under C_adj = C·exp(−h_a), or "unevaluable" when no model appears under two agents. This is stress only.

Low

O112, O82 and O32 together make OpenAI report evidence nearly unattainable.

Part 5 lists nine OpenAI global meter resets between 2026-10-07 and 2026-10-24, about one every two days. Any weekly-meter reading that spans one is excluded, a 5-hour figure never admits a route, and only reports from the last 30 days count.

So the flagged SemiAnalysis GPT routes (possibly superseded since 2026-10-11) have almost no path to replacement by a report pair (O78, O92, O93) before demotion at age 121 (2027-02-04). Under the draft's own rules, every OpenAI plan row stays a flagged, label-denying blocker until then.

Change: accept readings that lie wholly between two recorded resets, and record the segment. Allow a report that states pre-reset and post-reset values separately, in the way E201a already does for window-straddling reports.

Owner decision challenge (O64, O100, O103): classification gates stop the whole release. A new Coding Agent Index row, a new AA footnote, a new Terminal-Bench agent or a Bug Hunt equal-N tie stops the build until an editor acts. This conflicts with "refreshed routinely".

Change: separate integrity gates (hash, reconciliation, identity), which keep stopping the build, from classification gates. For classification gates, publish with the unclassified row listed as "unregistered, excluded from cohort", and require registration before the next release. The previous release stays live either way.

S1T's binomial treatment has a known direction for non-binary leaves. AutomationBench-AA partial score, FrontierCode (tests plus rubric) and AI Coding Daily judged points are per-task scores in. For a given mean, p(1−p)/n is the maximum possible variance, so the plug-in SD for these leaves is an upper bound, not "direction not established". Separately, LiveBench's SD uses 2026-10-14 task counts for the 2026-10-23 release. Say so in the separability statement, and mark each leaf's bound direction (upper bound versus approximation).
0

Interval-label vocabulary reads stronger than the evidence.

Under O25, interval outputs are robust only to reporting precision. Today 0 of 8 adjacent max-effort ranks and 1 of 15 AI Coding Daily ranks separate under benchmark noise.

"Definite" and "confirmed" will therefore be issued on gaps far inside the draft's own noise. The claim-contract wording helps, but headline tables use the bare terms.

Owner decision challenge (O25), with a new argument: print the O44 noise-margin companion in the same cell as any confirmed or definite label, and use "record-stable" as the table term.

2. Methodology design recommendations

Prioritised:

Coverage-complete companion ranking (finding 1).

Leaves: FrontierCode 25, Terminal-Bench 20, Bug Hunt 15 and the seven non-SWE leaves at O55 weights.

Rows: cohort rows with exact Bug Hunt.

Anchors and ladder: its own anchors and H_k = sorted quality at zero-based position floor((n−1)k/4).

Output: for each bar, the displayed-record cheapest row, compared with the same bar's answer in the two leading rankings.

Use: diagnostic only, with no label and no mixing of values across rankings.

Honest SWE share (finding 2).

Formula: SWE_coding = Σ w(FC, TB, BH, Vibe, CM) + w_LB × (w_Coding + w_LongAgentic)/Σ w_c.

Today, in the max-effort ranking, this is about 51 on the draft's weights.

Publish it beside "60%". Reuse the existing drift and spread diagnostics with LiveBench as its own group.

Harness-aware cost stress (finding 3).

Data: AA's Coding Agent Index row labels, which already carry the agent.

Estimator: a fixed-effects regression of log C on model and agent for models with two or more agents.

Uncertainty: report the estimator's interval, and print "unevaluable" otherwise.

Status: a named S2 branch, outside Θ.

Reset-segmented report admission (finding 4).

Rule: define segments between recorded resets. A report counts if its meter window sits inside one segment.

Scaling: keep the draft's meter-fraction scaling to the segment's own window (E270), with no extrapolation across windows.

Tiered release gates (finding 5). Classify each gate once as integrity or classification, and publish the classification list in the active-rules manifest.

Label cell content (finding 7). Each label cell shows the label, the reporting-precision basis, the nearest competitor's pair separability at ρ = 0, and the noise-margin companion.

3. Questions for the owner

Was a coverage-complete ten-leaf ranking weighed against the two-ranking design at O53? If yes, what was the deciding cost? If no, would you accept it as a diagnostic-only third ranking? The answer changes recommendation 1.

Do you intend "software engineering 60%" to count all of LiveBench 2.0 Overall, which includes Reasoning, Browser, Data Analysis and Research? If yes, the label should say "agentic and general professional work". If no, finding 2's decomposed weighting applies.

Is the Coding Agent Index's vendor agent meant to be part of the configuration being costed, so that harness cost is deliberately charged to the model? The answer decides whether finding 3 is a disclosure or a correction.

4. Verdict

VERDICT: HAS FEEDBACK