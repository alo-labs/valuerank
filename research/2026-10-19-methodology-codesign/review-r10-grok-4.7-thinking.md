I'll review the draft against its objective and check the public measurement sources it depends on.
The draft’s buyer-facing labels do not yet identify lowest cost for the work being scored. Plan scores can be filled with the wrong workload’s multiple, and the “recommended” certificate is not a well-defined comparison.

1. Findings by severity
Critical

Official Plan cost substitutes an agentic multiple for the scored workload. The normative rule scores Plan cost with M_AA-mix when identified, otherwise M_observed. SemiAnalysis, the only named controlled source, defines value on a (plan, model, workload) tuple, prices an agentic mix from its own September usage, and states that Artificial Analysis Intelligence Index tasks are not representative of that work. Its public method also measures input, cache-write, cache-read, and output separately, and treats cache reads as free when the meter does not move after 500M tokens. Dividing the Index bill by an agentic headline multiple (the draft’s ~57–59× band; public restatements put a $200 Claude plan near 58.6× on Opus 5.5) is not a conservative bound. It is a biased point estimate, and cache-heavy Index runs can be mis-ranked by a large factor. That fails the Plan half of the objective even when the row is honestly left uncertified. Change: the official Plan value score exists only with an identified M_AA-mix. Build it from public per-category meter rates times that configuration’s Index category token counts, then the normative window minimum (λ = min_w λ_w). If either side is missing, leave Plan value blank and keep M_observed in a workload-labelled diagnostic. Do not let owner-named transfers or the ~57–59× anchor rationale become row numerators.
newsletter.semianalysis
+1

“Recommended” has no single comparison set, and expiry writes API prices into the Plan ranking. The outputs section requires a worst-case lead over every other row. The normative section has two scopes, and says an undefined comparison is not a positive margin. With transfers off, transfer-only routes are unevaluable and must not be replaced by API cost. O13 then demotes expired routes to diagnostic-only and puts flagged API cost back into the official Plan ranking, while an earlier rule excludes API-fallback rows from Plan winner, frontier, and threshold claims. Those rules cannot be executed together. One reading certifies nobody whenever any transfer or expired row exists; the other crowns an API price as a Plan recommendation. Change: map the headline word “recommended” only to “interval-certified among directly evidenced routes.” Exclusions are listed, not failed margins. After hard expiry, the route leaves the official Plan ranking; the family is “no eligible Plan route,” not an API substitute. Keep O13’s demotion, but drop the API fallback.

The certificate’s missing-leaf bounds are not a usable joint test. Q^L = p·Q̄ and Q^U = p·Q̄ + 100(1−p) let a leaf missing on either row move by 100 points in opposite directions. At 90% coverage, an 80 vs 70 observed lead becomes Q^L − Q^U = −1 (a 0.75 value-point loss) before cost. At 75% coverage, an 85 vs 70 lead becomes −13.75 quality points, about −10.3 value points. The whole API cohort’s cost-score spread is only about 18 value points (S_C ≈ 86.8 at $110 vs 13.9 at $8,700). Shared missingness cancels in a real comparison; this bound does not, so interval-certified will usually be empty. Buyers will then use rank 1. Scenario-supported makes that worse: it requires a 90% lead on S0, which is the renormalized observed-only score, a different estimand from the certificate. Change: certify each pair only on leaves observed for both, with common-support weight at least 70% and the existing SWE gates. Drop pair-missing leaves from that difference and publish the dropped weight. Do not put [0, 100] fills inside Θ_cert. Compute scenario-supported on that same common-support estimand, not on S0.

High

Bug Hunt’s unit and anchors disagree. The measurement is pooled fixed/105, a 0–1 ratio, but the leaf anchors are 0–105. The general z formula then maps a real run to about 0, or a count is fed into a ratio, depending on the implementer. A 10% leaf that collapses changes the headline. Change: set x to bugs fixed, z = 100 × x/105, and add a release vector (52/105 → 49.52). Keep repository differences as sensitivity, as already specified.
benchlm

Terminal-Bench is not one exact variant. The official board and other public boards mix agents and cost bases: a full Claude Code run for Opus 5.5 (max) is reported at about $4.7k, while a mini-swe-agent accounting is reported per test. The draft prefers tbench.ai cost columns over AA-run data in the cross-check that can block certification. That joins a vendor-CLI stack to an AA Index bill and can flag, or clear, a row because of harness rather than price. Index v4.3.2 already contains its own Terminal-Bench 4.0 run, at 10% of the Index. Change: API matched-cost uses AA’s exact-variant per-evaluation cost only. tbench.ai may score the Plan leaf only when model, effort, and agent match the frozen route; no best-of-agent join. If the agent does not match, the leaf stays missing.
tbench
+3

Route selection ignores the identification status certification requires. The frozen route maximizes the multiple’s lower bound. Reviewer 9’s rule then refuses certification unless that frozen route has identified M_AA-mix. The official row is therefore the route most likely to be ineligible, while a slightly worse identified route sits in a side table. Change: lexicographic route choice for the official Plan ranking: identified M_AA-mix, then evidence grade, then multiple lower bound, then lower fee. Publish the lower-bound-only route as sensitivity, not as the headline.

Owner decision challenge (O9 / post-reviewer-7 blocker), new argument. Replacing total Index cost was rejected, and this does not reopen that. What is new is the constituent list. Index v4.3.2 prices Briefcase, GDPval-AA, AutomationBench, Terminal-Bench 4.0, SciCode, LCR, Omniscience, HLE, GDP.pdf, and CritPt. It does not price DeepSWE, Bug Hunt, or FrontierCode, which are 50 points of ValueRank quality. Briefcase and GDP.pdf are priced and unscored. The draft’s 43.75% priced-mix figure is the arithmetic result, and it falsifies the rationale that the suite bill is the price of the scored work. A rank-delta of 3 can miss a pairwise reversal of the leader’s cost advantage. Change: keep total Index USD as the scored API cost. Block interval certification when C^match reverses the leader’s pairwise cost order against any eligible rival, not only when rank moves by more than 3. Publish, per row, the share of Index USD spent on evaluations ValueRank does not score.
artificialanalysis

Plan route identity is coarser than the limits SemiAnalysis measured. OpenAI’s $200-plan cut was grandfathered through 29 October 2026, so one public plan name has two multiples. A ~20% account-level A/B test was invisible on the pricing page. The detailed category-rate series is a Tokenomics dashboard, while a public ranking can refresh only artifacts that state numerator, denominator, category rates, window, model, and date. Change: route key = plan × limit-schema version × purchase cohort × surface × model × effort. Page diffs do not clear a route; a new public measurement does. Reject press round-numbers as multiples.
newsletter.semianalysis

Unidentified quality uncertainty does not block a certificate, unlike unidentified Plan cost. Bug Hunt is one round on two repositories, and the draft correctly refuses to treat cohort spread as exact-variant repeatability. If that gap is unidentified and therefore omitted from Θ_cert, a 10% leaf is treated as exact. Change: any scored input with nominal weight ≥ 5% and role unidentified makes that pair uncertifiable unless a pre-registered conservative bound is inside Θ_cert.
benchlm

Medium

The cohort rule is fixed policy but not executable. “Within 3 rounded Index points of the frontier’s best at equal or lower cost” is not in the normative section. Change: let F(c) be the best frontier Index among plotted configs with cost ≤ c. Admit a family when its rounded Index is at least F(c) − 3. Pin the tie-break.

Leave-AA-out is still described as a headline robustness column while the draft itself says it is not identifiable (about 25% independent weight, gate 40%). AA also supplies the entire API cost field. Buyers will read a blank column as a test that was passed. Change: label it not identifiable in the main table until independent weight can clear 40%. Do not put it in a robustness denominator.
artificialanalysis
+1

The S2 “majority” test barely perturbs weights. Group Dirichlet 100 × (0.60, 0.20, 0.10, 0.10) gives the SWE share a standard deviation of about 4.9 points, so an S2 majority will usually copy S1. That matches the owner’s modest-perturbation intent, but the label overclaims weight robustness. Change: publish the maximum rank change under the S2 core branch, and do not treat S2 majority as a separate hurdle.

Two Plan formulas can both be implemented. The cost section’s M = (Σ_k t_k / m_k)^(−1) is not the normative λ = min_w B_w / Σ_k a_wk x_k, and SemiAnalysis’s month is capped by the weekly window, not by summing 5-hour resets. Change: one formula, the normative λ / time-indexed LP, plus a numeric test vector in the release tests. Mark the harmonic expression non-governing.
newsletter.semianalysis

Omniscience is not pinned at count level. AA’s Index is 100 × (c − i) / (c + p + i + a), on [−100, 100], not (2A+N)/3. The 2:1 blend may stay as a ValueRank choice, but public descriptions of non-hallucination disagree. Change: define A and N from (c, p, i, a) in the registry, including whether partial credit is incorrect.
arxiv
+1

The open-weight price rule is not yet a refreshable procedure. AA’s Index cost is first-party list or the median across providers, using input, cache-hit, cache-write, reasoning, and answer tokens, excluding repeats. AA also publishes a 7:2:1 blended price and a separate cost-per-task series. Change: name the provider basket, quote time, and token-class vector. Add a release assertion that the scored field is total Index USD, not cost-per-task and not the blended price.
artificialanalysis
+1

Low

The 10% clip gate is ambiguous on 19 rows (10% is 1.9 rows). Change: fail when at least 2 rows clip on either basis.

The disclosed doubling rates match the anchors: API ln(20000/50) implies −2.89 value points per doubling, about 3.86 quality points; Plan −2.28 and 3.04. GDPval’s (Elo − 500) / 2000 matches AA’s published integration transform. No change on either.
artificialanalysis

2. Methodology design recommendations

Split the estimands in the release schema. For each row and basis store cost_status (identified M_AA-mix / observed-workload only / assumption / expired), comparison_support (common leaf weight), and label (interval-certified among directly evidenced / scenario-supported / not identified). Official sort for Plan claims uses only identified M_AA-mix rows. Assumption-inclusive and measured-workload tables stay secondary.

Make certification a pairwise common-support program. Fix nominal weights, primary price rule, frozen route, and linear GDPval map. For pair (i, j), drop leaves either row lacks; require support ≥ 70%. Shared prices, donor meters, and quota pools move together. Independent inputs take the adverse endpoint. Certify only if the worst-case value margin is positive and the matched-cost pairwise order does not reverse. Publish the binding constraint.

Add a public-evidence checklist before a Plan multiple can be numeric. Required fields: fee, window lengths, purchase cohort, category meter rates with a stated range, Index category token counts, price-list date, and a citable public source. Subscriber-only charts and secondary 57–59× writeups fail the checklist.

Add three release vectors that must match exactly. Bug Hunt 52/105 → 49.52. A two-window plan whose weekly cap binds must not increase when the 5-hour cap is loosened. A shared missing leaf must not change a pairwise margin. A field grab of cost-per-task or the 7:2:1 blended price fails the build.

Report the O9 gap without changing the 25/75 score. Beside priced-mix coverage, print the share of Index USD from unscored evaluations and the pairwise C^match order. That makes the owner rationale testable on each refresh.

3. Questions for the owner

Are per-configuration Index token counts public for input, cache read, cache write, reasoning, and answer? If they are not, official Plan value scores have to be withheld under the rule above. If they are, M_AA-mix can be built now from public category rates.

Should the headline word “recommended” mean “certified among directly evidenced routes,” or “certified across all eligible native Plan routes,” including assumption rows by conservative bounds? The comparison set and the O13 wording depend on that answer.

4. Verdict

VERDICT: HAS FEEDBACK