1. Findings by severity

I read draft r20 against its objective: the lowest-cost frontier model for the value it delivers, ranked separately for API buyers and Plan buyers. The main problem is that the specification is far more precise than the evidence it can run on. Today the scored cost basket has one admissible component and the official Plan evidence is thin. I have not repeated anything in the ledger as rejected or adopted unless I say what is new.

Critical

The scored cost is, for now, a single-benchmark cost, and the objective is an SDLC-wide claim.

The issue: only the Coding Agent Index is admissible today. Three of its 16 priced rows are partial, and three of 19 rows have none. The draft's own capture status gives 16/19 for the Coding Agent Index, 11/19 for FrontierCode and 7/19 for ITBench-AA. The headline ranking is therefore ranked on one agentic-coding cost, and the text still describes it as a ten-component "SDLC cost basket".
paste.txt

Why it hurts: cost carries 25% of the value score. Unpriced rows get "subset cost" labels, and under O17 those rows are not comparable across the workload. Rows that are unevaluable for the frontier and bar outputs still sit in the headline table.

Recommendation: print the active basket name in the headline, for example "Basket v1 = Coding Agent Index only", and put the target basket in the readiness table only. Add a release rule that the headline says "SDLC basket" only once admission has happened for at least the Coding Agent Index plus one non-coding component. This respects the O15 and E26 fixed policy because it changes labelling, not admission.

This is an Owner decision challenge only if you want a faster path. Compare against AA's own full-Index cost for all 19 rows as a labelled secondary column, which the draft already keeps as a diagnostic.

Plan scores can be ranked while transport is unidentified, and the interval outputs then exclude them.

The issue: the Plan basis keeps rows with no identified M_W (O16). The frontier and bar outputs then drop them (E21, E32). For most Plan rows the interval machinery will say "unevaluable".

Why it hurts: the Plan buyer gets a headline rank with no frontier, no bar answer and no robustness. I cannot see from the draft how many Plan rows will ever be identified. The funding-aware capacity program (E54) and the time-indexed LP (E39, E56) need quota semantics that providers publish only partially. Provider help pages describe a 5-hour session limit plus a weekly limit, and docs describe the 5-hour window as rolling. They give no burn coefficients per model.
support.claude
+1

Recommendation: publish an identification-yield table each release (identified, bounded, unidentified) per Plan route. Add a rule that the Plan headline is labelled "exploratory" when fewer than half the Plan rows are identified. The draft already has the label machinery, so this adds one threshold.

High

Quality weights can become dominated by the AA-run source while the independent-source check is unusable.

The issue: about 80% of quality weight is AA-run. Leave-AA-out is "not identifiable" because only about 20% independent weight remains, under the 40% threshold. The robustness column that should detect source dependence is therefore permanently blank.
paste.txt

Recommendation: lower the identifiability threshold to a stated value that today's weight can meet, or replace leave-AA-out with a leave-source-out run using only the independent leaves, reported as a rank correlation (Spearman or Kendall) with the full ranking and no scenario share. A permanently empty headline column gives no assurance.

The cost score is anchored on the reference cohort, so the exchange rate shifts with who is in the reference panel.

The issue: c_L = min reference cost ÷ 2 and c_H = max reference cost × 2. The exchange rate is −100·β·ln2 / ln(c_H/c_L) points per cost doubling. With a wide cost spread (the Index lists models from about $0.04 to $3.25 per task, a ratio of roughly 80x, in AA's own numbers ), a doubling costs only a few points, so cost barely matters.
artificialanalysis

Why it hurts: 25% nominal weight can shrink to a very small effective weight. The draft flags a release when cost's within-cohort influence is under 10% but never changes β.

Recommendation: report the cost-doubling-to-quality-points figure beside the very first table, and add a sensitivity curve over c_H/c_L. This is a disclosure change and does not touch the weights.

The spec has too many rules whose failure is invisible to the reader.

The issue: E-numbers run to E58, the Normative section is dense, and many fixtures are only listed. A consumer cannot tell which rules actually bind for this release.

Recommendation: add a one-page per-release "active rules" manifest that lists, for each rule, whether it fired, was vacuous or was unresolved. Without it the methodology cannot be audited.

Medium

Terminal-Bench is counted three times. It appears in the AA Index run, the Coding Agent Index run and the tbench.ai quality leaf. The draft discloses the overlap (O24). The new point is that the cost basket then double-charges Terminal-Bench behaviour while the quality score rewards it once. Report the sensitivity of the ranking to dropping the Index-run Terminal-Bench cost, so readers see the size of the effect.

The AA cost definition excludes repeats and uses AA's token and cache protocol. AA states its cost uses input, cache hit, cache write, reasoning and answer token prices, and excludes repeats. Your DeepSWE quality leaf uses pass@1 averaged over 3 attempts, which fits that cost definition. For the Plan basis, though, real users do retry. The attempts-reconciliation text handles this as a bias bound, but I would add a worked example in the release so readers can see the size.
artificialanalysis

Bug Hunt carries 10% of quality from two repositories and vendor CLIs. The harness band is stress-only, not in Θ. It is the only SWE leaf not run in a controlled harness. Show its effective weight and the ranking with and without it, as a standing column, not only as a stress branch.

Low

The 30-day soft expiry for Plan evidence is short compared with how often providers change limits. Trigger on detected change only (the draft already does), and treat the time-based expiry as a backstop.

The Omniscience reconstruction (2A + N)/3 replaces AA's own integration. The test vector is good. Add a check that your reconstruction matches AA's published field for every row each release.

2. Methodology design recommendations

Priority order:

Basket labelling and the identification-yield table (findings 1 and 2). Cheap, and it makes the claim match the evidence.

A single "what binds" manifest per release (finding 5). It lists active gates, unresolved solver statuses and vacuous rules.

An independent-source rank check. Compute Kendall τ between the full value ranking and a ranking from only the independent leaves (Bug Hunt and Terminal-Bench). Publish it with a bootstrap interval over models. This replaces the blank leave-AA-out column.

Cost-weight disclosure. Publish the effective cost weight, 0.25·SD(S_C) / (0.25·SD(S_C) + 0.75·SD(S_Q)), as a headline number with the doubling rate, not a footnote.

Overlap sensitivity. Rank with Terminal-Bench cost removed from one execution, and report the maximum rank change.

Where Plan capacity is concerned, keep the LP and its bounds, but start with the two windows that providers document (session and weekly), as the release tests already do.

3. Questions for the owner

How many Plan rows do you expect to have an identified M_W in the first public release? If the answer is under about half, I would change the Plan headline to an exploratory label (finding 2).

Is the first public release meant to carry the full SDLC label, or are you willing to ship it as "Coding Agent Index basket v1"? This decides whether finding 1 is Critical or Medium.

Does the 10% cost-influence flag have a consequence when it fires, or is it purely informational? If it fires, β is not changed, so cost might be effectively decorative.

4. Verdict

VERDICT: HAS FEEDBACK