0. Read check

I read all 16 parts to their end through the GitHub connector, one file per part, in order. No part failed to load. I did not use web search, because the call budget went to the 16 reads. The review therefore rests on the draft's own text, and I have not independently verified its claims about outside benchmarks or plan quotas. I cite no external sources.

First line: "# ValueRank methodology — draft r188"

Final sentence of each part:

"A change of AA chart or field is a versioned methodology migration, never a silent refresh."

"…; a family with an excluded primary may have other efforts ranked." (the closing clause of a long "Today the excluded configurations…" sentence)

"Both priced executions stay in the basket as the owner listed them; the overlap is disclosed."

"These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status."

"Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution."

The part ends mid-sentence at the file boundary: "…so a wrongly scoped provisional report cannot fail a cell;". Part 7 continues it.

"Evidence rules unchanged except for two owner exceptions, the O46 MiMo quota ceilings and the O76 speed-mode conversion of a user report (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

"Domain validity is separate from evidence completeness."

The part ends inside the leaf table. The last cell reads "hidden-test pass rate (%), anchors 0–100; Vals' standard error recorded".

"Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias."

"Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support."

"The population is the ranking's ranked rows that are not provisional and have a displayed quality (every leaf of the ranking, O36; a listed row never sets a bar), ordered by displayed quality ascending, then configuration ID."

"Ranked configurations only (owner decision O43)… the summary says these outputs compare ranked configurations only and names the listed configurations."

"A new observed price under an unchanged price rule is a data refresh; changing a rule is a methodology migration; a benchmark-version change triggers a comparability review with dual-run where feasible."

The part ends mid-sentence at the file boundary: "…(scores.json aaStateReconciliation, E322, on reviewer 87);". Part 16 continues it.

"Revision history: omitted from this review copy (not normative); it is in draft-r188.md in the same folder of the repository."

The parts omit the revision history, so I could not check that section.

1. Findings by severity

Critical

The Plan half of the objective cannot be delivered on a routine refresh cycle.

Evidence. Every measured Plan multiple is one paywalled SemiAnalysis analysis published 2026-10-06. The article is not in the evidence bundle, so it has no content hash (part 5).

Already superseded. The draft's own change records already flag every one of these routes as possibly superseded. They include Anthropic's meter changes and OpenAI's 2026-10-29 doubling of every Pro tier's limits (parts 6–7).

No replacement. The staged report search admitted no concordant pair for any cohort model and plan.

Decay. From the draft's dates, the age trigger fires 2026-11-06 (tomorrow), expiry is 2027-01-05, and demotion to API fallback is 2027-02-04.

Result. 21 of 27 and 60 of 67 plan rows are flagged. No route has an identified M_W. The remaining rows are O46 provider quota ceilings or API fallback.

Why it hurts. Objective (a), subscription-plan economics, is answered only by arithmetic on stale numbers. It decays to API cost within about three months unless the owner acts. The draft is honest about this, but the data pipeline does not meet the "refreshable routinely" constraint.

Change. Add an owner-run controlled saturation protocol (R1 below). Without it, the Plan ranking should carry a standing "no current evidence" banner once the age trigger fires.

High

The leading ranking cannot answer the "lowest cost" question.

Owner decision challenge to O36, O121 and O172.

Coverage. The max-effort ranking ranks 9 of 37 cohort configurations. The common-leaf ranking ranks 33, but it earns no labels.

What is missing. The cheapest rendered-frontier points sit outside the leading ranking's anchors: GPT-6 Luna (low) is 7.10× below the low anchor, and Claude Haiku 5.5 (low) is 1.53× below. Whether a configuration is ranked depends on whether Vals, LiveBench or Bug Hunt happened to run it at the top effort.

Why it hurts. The set of "cheapest above a bar" candidates is selected by third-party run policy, not by value. Four retained rows and the exclusion of the low-effort efforts bias the answers toward expensive top-effort runs.

New argument. The draft already contains coverage-tolerant machinery (E35 formal bounds, E221 u*) and switched it off for all rankings. Re-enable it for the common-leaf ranking (R4) and let that ranking earn labels.

The cost basket does not track what the quality leaves measure, and the response is to withhold labels.

Owner decision challenge to O15 and O182/O183.

Evidence. The AI Coding Daily like-for-like τ_b is 0.35 (the draft's own warning level is below 0.5), so that ranking's confirmed-cheapest labels are withheld.

Unrewarded cost. Briefcase and GDP.pdf carry a median 15% of basket cost with no quality leaf. SWE-Atlas QnA sits inside the Coding Agent Index cost, anywhere from none to all of it. The Coding Agent Index is 16–74% of a max-effort row's cost, and the vendor-agent effect on that cost cannot be removed (the S2 stress is unevaluable).

Why it hurts. The cost axis partly prices work the quality axis ignores and the agent harness, so it ranks agent and harness cost, not model cost.

Change. Make the quality-weighted matched cost (E55's C^match) the scored cost, or at least the AI Coding Daily ranking's cost, and keep the SDLC basket as a sensitivity (R2).

Anchors move with every re-capture and are set by the two most extreme rows.

Evidence. Anchors were re-frozen at O47, O65, O132 and a1→a4 within about 10 days. Workload changes allow no dual run. The anchors are c_L = min/2 and c_H = max×2. The max-effort API exchange rate implies a ~260× cost range, set by a handful of rows.

Why it hurts. Value scores and bars are not comparable across releases, so the swing gate (>5 points) cannot operate across migrations. The "points per cost doubling" is an artefact of the two outlier references.

New argument. This is a stability problem, not the rejected "equalise influence" recalibration. Use fixed round-number anchors per workload version and absolute bars (R3).

Medium

Interval labels certify only rounding stability, which is nearly vacuous when every row has full coverage.

Owner decision challenge to O25.

Evidence. Today's bar answers are separated by less than the noise margin (3.6 or 5.8 quality points), and 0 of 19 adjacent AI Coding Daily ranks separate.

Why it hurts. "Confirmed cheapest" reads as a strong claim but guards against 0.01-point moves. The O171 screen is only a companion.

Change. Authorise public cheapest wording with a noise-aware test, or rename the interval label "rounding-stable" (R5).

Bug Hunt's leaf composition and gatekeeping.

Owner decision challenge to O163/O170.

Evidence. The draft's own fixture has maxima of 57 planted and 65.3 unplanted fixes, so about 53% of the leaf's scale is unplanted "extras" with no answer key and no ceiling. The benchmark has one owner, two repositories and vendor CLIs. It also gates eligibility: MiMo-V2.6-Flash, MiniMax-M3.1-Flash and Gemini 4 Carbon are unranked for lack of a Bug Hunt row.

Why it hurts. A single outlier run moves every row's score, and over-editing can be rewarded.

Change. See R6 and R4.

Plan evidence discovery is not replicable.

Evidence. A cell passes only if the LLM-driven "staged" search (Claude Deep Research and Silver Bullet Deep Research) found at least one counting report (O124). Several venues were unreachable (X, direct Reddit, YouTube, LINUX DO).

Why it hurts. Admission depends on tool runs that cannot be replayed, which conflicts with the E159 rebuild-from-bundle promise.

Change. See R7.

A flagged route has no direction.

Evidence. OpenAI's 2026-10-29 doubling of every Pro tier's limits is a quantified provider announcement. The routes stay scored at pre-change multiples with no sign of the likely error.

Change. Publish a directional bracket as a sensitivity (R8). It would not be a numerator or a score change.

Low

Cohort cliff. Ten configurations left the plotted set at the v5 re-capture, and about 4 of 9 max-effort rows are retained rows. The cohort rule is fixed policy, so this is an Owner decision challenge to O145 only. A two-release hysteresis would reduce churn.

"Software engineering 60%" overstates coding. LiveBench Overall is 15 of those 60 points, and about 61% of it is non-coding categories. The coding share is 51% and is disclosed (O122). Rename the group "SDLC and agentic work".

Auditability. The spec has hundreds of editor records and a "later-numbered governs" rule. Publish a short normative core (formulas, gates, leaf table) generated from the build, with the rationale ledger separate.

2. Methodology design recommendations

Listed in priority order.

R1: Owner-run Plan measurements.

Run a scripted, fixed workload per plan and model, monthly and after any change record.

Run each to exhaustion with an API-priced token ledger, and publish the receipts.

Compute M_obs = U_obs / F_gross, with U_obs the API-priced delivered consumption.

Run on at least two independent accounts, or pair with SemiAnalysis, to satisfy O11.

Re-measure to replace flagged routes (O78/O93). This makes the Plan basis refreshable from public data and removes the single-source dependence.

R2: Matched cost as the scored cost.

Use C_i = Σ_g ω_g P_ig, with P_ig the one-pass cost of execution family g and ω_g the quality weight of the leaves that reference g.

Compute the cost score on frozen anchors as usual.

Keep the full basket and the leave-one-component-out family as sensitivities.

Gate labels on τ_b between the matched and basket costs, not on cost per solved task.

R3: Stable scales.

Round anchors outward to decades: c_L = 10^⌊log₁₀(min/2)⌋ and c_H = 10^⌈log₁₀(max×2)⌉. They then change only when an extreme crosses a decade.

Add absolute composite bars (50, 60, 70) beside the quartile ladder. This gives a time series of the "cheapest at quality X" cost.

R4: Coverage-tolerant common-leaf ranking.

Allow a row when at least 85% of quality weight is observed.

Use E35's Q^L and Q^U bounds for labels, so a label needs Q^L ≥ H.

Flag partial rows and publish E221's u*.

R5: Noise-aware authorisation.

Require Δ_i = (Q̄_i − H)/√(σ_i² + σ_H²) ≥ 1.96 for the candidate.

Require Δ_j ≤ −1.96 for the m cheaper rows, with Holm correction across those m comparisons.

Otherwise print "rounding-stable only".

R6: Bug Hunt scale.

Make the primary z = 100 × planted / 105, using the fixed key, so there is no live board maximum.

Report unplanted fixes separately, or cap their contribution at about 25% of the leaf.

The O173 ±10% stress then measures nothing new.

R7: Deterministic discovery.

Use fixed collectors: the Hacker News API, Reddit listings, GitHub issue search and a fixed forum list.

Hash and archive the full candidate corpus.

Use the LLM only to triage. Admission should then need two archived observers.

R8: Announced-change bracket.

For a flagged route with a quantified provider announcement, publish M × f for the announced factor f (sensitivity only).

Label it "likely understated" or "likely overstated".

R9: Cost-dispersion stress from public pairs.

Terminal-Bench 4.0 is priced twice, as AA's Index run and inside the Coding Agent Index vendor-agent run (the same 66 tasks).

Compute s = SD(log C_TB,Index − log C_TB,CAI) after removing the median offset.

Use s as a labelled harness-plus-run cost-noise stress in the separability threshold. Today that threshold omits cost noise.

3. Questions for the owner

Is the primary user question "cheapest at a given quality" or "best all-round value"? If the first, R4 should lead and the common-leaf ranking should earn labels.

Will the owner fund monthly controlled Plan measurements (R1), at roughly the cost of the plan fees? If not, the Plan basis should be labelled "no current evidence" once evidence expires.

Is the unplanted-fix reward in Bug Hunt intended to reward over-editing? If not, adopt R6.

4. Verdict

VERDICT: HAS FEEDBACK