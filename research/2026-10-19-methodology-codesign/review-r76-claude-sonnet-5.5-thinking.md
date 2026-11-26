0. Read check

First line: "# ValueRank methodology — draft r158"

Each part was opened through the GitHub connector at commit 9677c8e and read to its end. The last 12 words of each part are:

carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py).

or provider declined some tasks on safety grounds") also flags "partial component".

on the Plan basis the workload question is the M_W identification status.

for other Claude models; the transfers keep their assumption label and caution.

no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

set-identified, the Plan headline carries the label "workload-unmatched: exploratory" (O16 scoring unchanged).

(no value for 10 of 19 cohort rows in the 2026-10-17 snapshot)

a bias bound in the identification layer); repetitions are not a bias.

not separable" and its S0 result is not described as target-workload support.

of both rankings has a cost, so the two ladders are equal.

Bug Hunt and AI Coding Daily name the harness on each record).

or definite result; every cost check reads C_W, never the Index diagnostic.

before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

normative); it is in draft-r158.md in the same folder of the repository.

All 14 parts were read to the end. Part 14 omits the revision history, as it states. I did no web search, because of the call budget, so this review contains no external citations.

1. Findings by severity

Critical

None.

High

The leading ranking cannot answer the objective (Owner decision challenge to O52–O54, O121).

Issue: The max-effort ranking leads the site and README but ranks 5 of 27 cohort configurations. Only 1 of 4 adjacent API ranks is separable. LiveBench 2.0 and Vals run each model once, at its top effort, so cheaper efforts that AA plots on its frontier are excluded by construction (GPT-6 Luna low, Haiku 5.5 low, GPT-6.1 Terra low). The lead ranking can therefore never find the cheaper effort of a family. A "cheapest above a bar" answer is biased toward dearer max-effort rows, and E201c only lists the missed siblings.

New argument versus O121: the bias is structural and one-directional. It is not mere incompleteness.

Change: Make the 25-row common-leaf ranking the primary ranking, with the two extended rankings as "broader evidence" views. If the owner keeps the lead, print on every bar answer the cheaper same-family efforts that could not be evaluated, in the headline sentence and not only in uncheckedCheaperSiblings.

Plan transfers ignore the price ratio between models (Owner decision challenge to O4/O7).

Issue: Opus 5.5's measured multiple (57–59×) is applied to Sonnet and Haiku, and the GPT lower-of rule is applied across models. Today 7 of 18 and 38 of 57 Plan rows rest on owner assumptions. O126 records that every Claude and ChatGPT meter counts tokens. If a plan meters raw tokens, the API-dollar value of the allowance scales with the target model's per-token price, so an Opus multiple overstates Haiku roughly by the price ratio. If the meter is cost-weighted, the multiple carries over. Fable's 12.4–12.7× against Opus's 57–59× (O35) already shows multiples are model-specific. The "directional bias bound" for burn coefficients is mentioned but never computed.

Why it hurts: The Plan ranking's cheap-model rows may be inflated by the largest error in the whole Plan pipeline, and the 2^(threshold/points per doubling) tolerance does not bound this.

Change: For every transfer, publish a two-point bracket, M_target ∈ [M_donor × min(1, p_t/p_d), M_donor × max(1, p_t/p_d)]. Here p is the per-token price blended over AA's published Index-wide category mix. Show both values as a named S2 sensitivity (outside Θ, so O19 holds) and mark rows whose rank changes between the two.

New versus the rejected burn-rate challenge: this is a public-price bracket, and it does not claim to identify M_W.

The specification is too large to audit or to keep consistent.

Issue: The draft is 298k characters with more than 280 editor records. Its own header says a conflict between editor rules is "a defect corrected in the next revision". Many rules are declared vacuous: O8 provisional, E219, E221, E226, E201b and E235. Section 2 of this review proposes cutting those out of the normative text. The published headline is a 5-row ranking with 1 of 4 ranks separable. Outsiders cannot check conformance, and each new edit risks an unnoticed conflict.

Change: Split the draft into a core normative spec of roughly 30k characters (cohort, leaves and weights, cost basket, anchors, value formula, bars, headline uncertainty) and a governance appendix. Move every currently vacuous rule to the appendix with its fixture. Ship a conformance test list keyed to the core only. Add a rule that an unamended conflict between two E-records is resolved by the editor before release. "Later-numbered governs" silently picks a winner.

Medium

Anchors on 4–5 references are fragile.

Issue: The max-effort ranking freezes anchors on 4 references, with 4 of 5 rows eligible. The anchors are c_L = min/2 and c_H = max×2, so one row sets each end. The exchange rate (3.11 points per doubling) therefore reflects that row's cost. The 10th/90th-percentile trimmed-anchor diagnostic is meaningless at n = 4.

Change: Add a leave-one-reference-out series of exchange rates and ranks, and a "thin anchor" flag below 8 references. Add a sensitivity that anchors on the six-index-evaluation sub-basket over all 27 cohort rows, since those costs are published for every plotted model. Treat it as a diagnostic only, which respects O120.

The exchange rate is never checked against the market.

Issue: A 25/75 weight with log-cost anchors implies a quality-per-doubling trade, here 4.14 quality points per doubling in the max-effort API ranking and 4.03 in the AI Coding Daily ranking. That trade-off is set by reference span, not by what buyers pay.

Change: Publish the empirical slope as a diagnostic. Estimate Theil–Sen d(Q̄)/d(log₂ C) over the ranked rows, and the same slope for AA's Index against cost over the 82 plotted points. Flag a release when the owner rate is more than 2× or less than 0.5× the empirical slope. This changes no score, so O2 stands.

Context: E196 already shows that realised cost influence is 94% / −37% in the max-effort ranking and −99% / −54% in the AI Coding Daily ranking. The slope check explains why.

The bar ladder is degenerate at small n.

Issue: The max-effort bars are 63.7, 65.2 and 66.2, a 2.5-point span. That is less than the 3.5-point quality noise margin (O44), so three "bars" are statistically one bar. Three of five rows reach the headline bar.

Change: Pin a ladder only when the spacing between adjacent bars is at least the noise margin. Otherwise publish a single bar plus the noise-margin companion. Alternatively pre-register absolute bars (for example 60, 65 and 70 on the quality scale) that are independent of the ranked set.

Cost pays for work the quality side does not credit.

Issue: E203 reports a 15% median share with no leaf (AA-Briefcase, GDP.pdf). ITBench-AA also has no leaf. When the Coding Agent Index is admitted, SWE-Atlas QnA is 124 of its 290 tasks (43% by count) and has no leaf. The cost share is "not separable", so the 15% understates the unrewarded share in exactly the ranking that admits the index.

Change (Owner decision challenge to O15): Add a quality-matched cost basket (components with a quality leaf only) as a standing sensitivity. For the index, publish a bounded range for the QnA share, from 0 up to its task-count share of 43%, and show the rank changes at both ends.

The cohort churns with AA's plot.

Issue: Between the 2026-10-25 and 2026-10-30 captures, 7 frontier vertices entered and 8 left. The cohort fell from 37 to 27 within ten days. Nine configurations left the cohort at the v5 re-capture, among them DeepSeek V4.1 Flash 1017, Kimi K3.1 Pro and MiMo-V2.6-Pro. Rankings are not comparable across releases.

Change (Owner decision challenge to the cohort rule): Keep a configuration ranked for one extra release after it leaves AA's near gap, flagged "left cohort". Alternatively, publish a stability table of rank and value for configurations present in the last two releases.

Low

The wording "most plan rows rest on a route flagged possibly superseded or expired (18 of 18 and 57 of 57)" should read "all". No route is expired at the 2026-10-31 cutoff, since the earliest expiry is 2027-01-05.

Bug Hunt carries 8–15% of quality from a two-repository, 105-bug benchmark run by one maintainer. The standing removal sensitivity exists. Print its rank shift in the headline when it moves any top-3 row.

GDPval-AA uses the displayed Elo at each cutoff (O70), while AA's methodology freezes ratings at addition. Movement is 0.00 today, so there is no impact now. Keep the diagnostic.

The AI Coding Daily sampling unit n = 6 is labelled an assumption. Capture the per-project points before the next release, as the draft already intends.

2. Methodology design recommendations

Listed in priority order:

Primary ranking. Primary = common-leaf ranking (25 rows, FrontierCode 25, Terminal-Bench 20, Bug Hunt 15, plus the seven leaves outside software engineering). Show the extended-leaf rankings as evidence columns with their own bars. Value stays V = 0.25·S_C + 0.75·Q.

Plan transfer bracket.

For each owner-named transfer, compute r = p_target/p_donor with p = Σ_k s_k·p_k. Here s_k are AA's Index-wide category shares and p_k are the first-party list prices.

Publish V_Plan at M_donor·min(1, r) and at M_donor·max(1, r). Print the rank range.

Keep the owner's value as the displayed score.

Plan reading guide. For each Plan row, publish the API-equivalent monthly usage range in which the plan beats API, [F, M·F] with F the fee. The effective price per API dollar delivered is F/U for U in that range, so it ranges from 1 down to 1/M. This extends E166's typed amount, and it is not a utilisation ladder.

Anchor robustness. Publish leave-one-reference-out exchange rates and ranks, with the thin-anchor flag below 8 references. Add the six-index-evaluation, 27-row anchor sensitivity. Publish the empirical slope and a ratio against the owner rate.

Bars.

Pin bars H_k only if H_{k+1} − H_k ≥ 1.96·√2·median(SD_Q).

Otherwise publish one bar with the noise-margin companion.

Use ties and the cheapest-clearing-by-margin row as the headline answer. The margin is currently 3.5 (max-effort) and 5.6 (AI Coding Daily).

Cost-scope sensitivity.

C_matched = Σ over components with a leaf.

Add C_CAI,adj = C_CAI × (1 − f), with f ∈ [0, 124/290].

Publish the ranks for each.

Spec hygiene. Core versus appendix split. A conformance suite covers the core only. Dead rules are archived until a ranked row actually fires them.

3. Questions for the owner

Would you lead with the common-leaf ranking if the extended rankings stay published? Your answer decides whether finding H1 is a policy change or a disclosure change.

Do the Claude and ChatGPT plan meters weight tokens by model price (credit or dollar-denominated), or count raw tokens? Your AGENTS.md authorisation of Opus-to-other-Claude transfers rests on this. Raw-token meters make the price-ratio bracket binding. Cost-weighted meters make it moot.

What range of exchange rate (quality points per cost doubling) do you regard as acceptable? Today it is 3.0–3.2 value points, equal to 3.8–4.3 quality points. This sets the thresholds for the empirical-slope flag.

4. Verdict

VERDICT: HAS FEEDBACK