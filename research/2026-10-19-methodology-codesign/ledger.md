## Panel
Six Perplexity Pro models, Search mode, Thinking on: GPT-6.1 Sol, Gemini 3.8 Flash, Claude Sonnet 5.5, Kimi K3, GLM 5.3, Grok 4.7. Reviews r01 (GPT-6.1 Sol) and r03 (Claude Sonnet 5.5) ran with Thinking off; from r04 on, Thinking is verified on before sending.

## Owner decisions (2026-10-19)
- O1. Two buyers ranked separately: API buyers and Plan (native subscription) buyers.
- O2. Headline stays a weighted value score (cost 25%, quality 75%), plus a cost–quality frontier and "cheapest above a quality bar" views.
- O3. Plan basis keeps the full-utilisation Value Multiple model (no monthly-demand scenarios); it is labelled as full-utilisation effective cost.
- O4. Owner-authorised assumed multiples stay in the official Plan ranking, labelled; a measured-only Plan view is added.

## Reviewer 1 (GPT-6.1 Sol) — adopted
- Never give a value score without a cost; publish missing-data bounds and a provisional flag (instead of a mandatory common panel, which would conflict with the no-exclusion/no-imputation policy).
- Document the exact AA cost field; publish AA tokens-used as a separate diagnostic.
- Frozen, versioned anchors for cost and quality normalisation (no cohort-relative scaling); quality on raw magnitudes, not ranks.
- Deterministic configuration-selection rule and configuration manifest; plan-route compatibility check.
- Remove AA Intelligence Index from quality (overlap with components and cost denominator); keep as diagnostic. Clarify DeepSWE ≠ Coding Agent Index.
- Move output tokens/s to diagnostics; group Omniscience accuracy and non-hallucination as one reliability measure.
- Non-overlapping quality hierarchy (SWE 60 / professional 20 / reliability+IF 10 / long-context+science 10).
- Rank bands, leave-one-out and cost-weight sensitivity; evidence-expiry rules; score-change decomposition.
- Cost–quality frontier and cheapest-above-threshold views.

## Reviewer 1 (GPT-6.1 Sol) — rejected or modified
- Remove assumed multiples from the official ranking: rejected by owner (O4); measured-only view added instead.
- Monthly-demand Plan scenarios: rejected by owner (O3).
- Dollars per successful task: deferred; only DeepSWE/TB4 publish matched cost and success for some rows; may be shown as a diagnostic where matched.
- Headline as cheapest-above-threshold: owner kept the weighted score as headline (O2).

## Owner decisions (2026-10-19, after round-1 input 2)
- O5. Cost input is AA total run cost (API) and total ÷ Value Multiple (Plan); USD per AA Index point is a diagnostic only.
- O6. SWE leaf weights diversified: DeepSWE 30, Bug Hunt 10, FrontierCode 10, Terminal-Bench 10 (share of quality).
- O7. Assumed Plan multiples cover only the owner-named model-to-model transfers; effort/surface/workload/price-basis mismatches are unmatched and excluded from the official Plan ranking.

## Round-1 input 2 (Perplexity default "Best" router — NOT Gemini 4 Argon; the model switch silently failed because Gemini 4 Argon is not on the owner's plan) — adopted on merit or by owner decision
- Versioned source contract registry; AA chart/field change = methodology migration.
- Cost not divided by AA Index (O5).
- Bound-aware frontier and threshold outputs (confirmed/possible; candidate sets).
- Value Multiple provenance fields; repricing on AA's price list where receipts exist; no burst extrapolation.
- Route-level Plan computation; API-fallback rows excluded from Plan winner/frontier/threshold claims.
- Bug Hunt 10%, FrontierCode 10% (O6); whole-run bootstrap.
- Explicit leaf formulas (GDPval transform, Omniscience (2A+N)/3, science children 1.25% each).
- Three separate uncertainty layers with joint propagation; no transitive tie groups.
- Claim scope statement.

## Round-1 input 2 (Perplexity default, not a panel model) — rejected
- "AA's frontier now plots cost per task, not total cost": contradicted by ValueRank's 2026-10-17 capture (chart "Intelligence Index vs. Cost to Run Artificial Analysis Intelligence Index", unit "USD to run all Intelligence Index evaluations"). The source contract still requires re-verification each refresh.

## Owner decisions (after reviewer 3)
- O8. No quality floor for the headline; disclose the implied cost/quality exchange rate instead.

## Reviewer 3 (Claude Sonnet 5.5) — adopted
- Per-basis frozen cost anchors (API $50–$20,000; Plan $1–$2,000) with a clip-rate release gate; unclipped values kept.
- Coverage = observed share of total quality weight; provisional unless ≥70% coverage and ≥2 SWE leaves (rows stay ranked per cohort policy, flagged, and excluded from "unique cheapest" claims).
- Plan route chosen on the multiple's lower bound; tier/fee part of route identity.
- Share of quality weight by source; leave-AA-out as a headline robustness column.
- Leaf anchors from chance/baseline to documented ceilings; effective-weight and correlation reports.
- Mandatory workload cross-check (cost per solved task vs AA-cost rank agreement).
- Implied exchange-rate disclosure (O8).
- Separately labelled min/max sensitivity band for missing leaves.
- Quality bars defined by reference configurations.
- 30-day soft expiry with change detection; price-list date and price-vs-token decomposition.
- Joint scenario simulation as uncertainty engine (results labelled as scenario shares, not probabilities); unique-cheapest only at ≥90% of scenarios.
- Release gates; grader identity in the registry; documented reason for the Omniscience 2:1 blend.

## Reviewer 3 (Claude Sonnet 5.5) — rejected
- Separate list for provisional rows: conflicts with the fixed cohort policy that every frontier/near-frontier family is in the primary ranking; flagged instead.
- Precision-aware weight shrinkage: rejected for the headline (weights stay fixed and published); leaf noise is carried by the measurement layer instead.

## Owner decisions (after reviewer 4)
- O9. O5 retained: cost input stays AA total run cost. Rationale: an end-to-end software project draws on nearly all the kinds of work AA benchmarks (knowledge, documents, professional, agentic, terminal, science, long context), so the whole-suite bill is the intended price; it is not reweighted to ValueRank's quality mix.
- O10. One quality vector for both bases (Bug Hunt stays in both); harness difference disclosed.

## Reviewer 4 (Grok 4.7, Thinking) — adopted
- Matched per-task cost and cost per solved task as diagnostics; >3-place divergence from the total-cost rank flags the row and blocks the "recommended" label (O5/O9 kept for the score).
- Leader rule: "recommended" only for non-provisional, non-dominated rows that lead in ≥90% of measurement scenarios with transfers off and AA included, and on identification bounds.
- Provisional also when DeepSWE (≥20% leaf) is missing or observed SWE weight <40%.
- Scenario engine draws identification bounds; results per stratum, not averaged; Dirichlet α_i = 50·w_i.
- Full utilisation = minimum across simultaneously binding limit windows; fee = amount paid for the measured period; category-specific multiples when available, otherwise mix-distance flag.
- Leaf fixes: GPQA a_low 25; FrontierCode headline field + blocker pass rate; Bug Hunt interval from repo/repeat range (no bug-level bootstrap); TB4 leaf clarified as the independent tbench.ai leaderboard.
- Exchange rate per basis; within-cohort spread of cost vs quality.
- Registry fields: repeat inclusion, cache-rate date, price rule, fallback tokens, Elo anchor identity, judge panel; decomposition by price/cache/token/method/cohort; suppress leave-AA-out below 40% identified weight.

## Reviewer 4 (Grok 4.7, Thinking) — rejected
- Replace total cost with matched per-task cost: rejected by owner (O9).
- Basis-specific quality vectors: rejected by owner (O10).
- "Live AA chart is cost per task": ValueRank's 2026-10-17 capture is the total-cost chart; both fields exist and both are now recorded in the registry.
- Exclude mix-unmatched Plan routes outright: modified to a visible "mix-unmatched" flag, since no current multiple publishes category-level rates and exclusion would empty the Plan view.
- Near-Pareto band on unrounded Index: rejected; the fixed cohort policy specifies the public rounded Index.
- Add AA-Briefcase to the professional group: deferred; with O9 its work is priced in the cost bill, and the owner's quality weights are kept stable this round.

## Owner decisions (after reviewer 5)
- O11. Official Plan ranking admits a measured route only via a controlled saturation measurement or ≥2 independent concordant reports (±20%); single-source routes are diagnostics. Owner-named transfers (O4/O7) remain labelled assumptions.
- O12. A failed release gate holds the release (fix or versioned re-anchor with dual-run comparison).
- Answers to reviewer 5: AA per-evaluation cost per task is public and ingested; per-run costs are not, so token-use variance is parametric where needed. Controlled Plan measurements come only from SemiAnalysis. Reset balances count only if measured as spendable. S0 uses the renormalised composite over observed leaves.

## Reviewer 5 (Kimi K3, Thinking) — adopted
- Cost layer in the scenario engine (price basis, cache rate, token-use variance) coupled with AA-run leaves via a shared serving-snapshot draw.
- Multiple admission rule (O11), source count and sampling basis per multiple.
- Attempts reconciliation per leaf with bias bounds.
- Cumulative strata S0/S1/S2 defined; declared draw kernels.
- Quota-schema registry: windows, reset balances, bundled-credit subtraction.
- Matched-cost diagnostic re-weighted by ValueRank leaf weights; independent-first cross-check (tbench.ai).
- GDPval logistic sensitivity; per-row effective weights; mix tolerance L1 > 0.30; 45-day cost freshness; gate failure = hold (O12).

## Owner decisions (after reviewer 6)
- O13. Plan routes past the 90-day hard expiry plus a 30-day grace are demoted to diagnostic-only; models fall back to API cost (flagged).
- O14. The SWE cost companion (c_SWE) is diagnostic only; it does not affect the "recommended" label.
- Answers to reviewer 6: SemiAnalysis per-(plan, model) measurements replace owner-named transfers where they exist (existing AGENTS.md policy). The Dirichlet kernel's intent is moderate perturbation around nominal weights. 17 of 19 ranked rows have matched DeepSWE token/success or TB4 cost/success data.

## Reviewer 6 (GLM 5.3, Thinking) — adopted
- c_SWE companion and priced-mix coverage (43.75%) as diagnostics (O14).
- Dirichlet α_i = max(50·w_i, 10); realised CV published.
- Pool scope per quota window; directional bias bounds for cross-pool transfers; measurements replace transfers.
- Credit-netting rule for multiples.
- Hard-expiry demotion (O13).
- Cross-check statistics: defined matched subset, n ≥ 8, Kendall τ-b with bootstrap CI.
- Report independence definition, geometric-mean pooling, step-based meters preferred.
- Omniscience rationale corrected (2:1 is a ValueRank choice; AA uses 1:1); AA field definitions pinned.
- "Recommended" also requires an S2 majority with transfers off; conditioning stated on the label.
- Non-discriminating leaves (SD(z) < 3); Bug Hunt run count per row; published RNG seed and scenario outputs; F and M·F disclosure per Plan route.

## Clarifications recorded after reviewer 7 (consistent with earlier owner answers)
- Weight sensitivity tests modest perturbation around 60/20/10/10, not alternative buyer preferences.
- "Recommended" requires an interval certificate (worst-case over the joint admissible set); scenario support is a separate, weaker label.
- Plan multiples use gross cash fee; net-of-credit is a diagnostic.
- Only the reweighted matched-cost divergence (with an economic ratio threshold) blocks certification; per-benchmark cost per solve and c_SWE are diagnostics (O14).

## Reviewer 7 (Gemini 3.8 Flash, Thinking) — adopted
- Critical: the α floor recentred weights (SWE 60%→33%); replaced by a hierarchical Dirichlet preserving group and within-group means.
- Gross-cash multiple convention with receipts reconciliation; route publishes cash fee, credits, eligible and excluded consumption.
- Deterministic certification (interval arithmetic / pairwise constrained optimisation) with three labels: interval-certified, scenario-supported, not identified.
- Benchmark-specific common-panel cross-checks (no pooling across benchmarks); only the reweighted matched-cost flag blocks, now also requiring a material cost-ratio gap.
- Source removal, GDPval mapping and transfers as named stress-test branches; S2 core branch defined; leave-AA-out marked "not identifiable" below 40%.
- Attempts: evaluation repetitions separated from deployment attempt policy; only the latter reconciled.
- Frozen route selection with declared tie-break; best-eligible-route ranking and route sensitivity published.
- Pinned reference configurations for quality bars with three qualification relations.

## Note on r07 (Gemini 3.8 Flash) first attempt
- The first Gemini 3.8 Flash run received an unedited copy of r05 because a draft edit failed; it was discarded (kept as r07-INVALID in scratch) and the review re-run on the corrected r06.

# Round 2 begins (all six panel models again, Thinking on)

## Editor decisions after round-2 reviewer 8 (owner may override)
- E1. Certification set fixes nominal weights, primary price rule, frozen route and linear GDPval map; specification robustness is published separately.
- E2. With transfers off, transfer-dependent Plan routes are unevaluable for certification (not replaced by API cost).
- E3. The matched-cost blocker requires ≥40% priced quality-weight coverage on a common panel; otherwise "cross-check unidentified" and the row cannot be certified.

## Reviewer 8 (GPT-6.1 Sol, round 2, Thinking) — adopted
- Normative definitions section: coverage, observed-only vs full-composite scores, certification set and pairwise margins, certified cheapest with conditional joint comparisons, multi-pool Plan capacity (harmonic formula only for a common additive budget), matched-cost blocker formula and coverage rule, dependence registry fields with stress branches, Bug Hunt pooled-run estimand, provenance fields, separated versioning, release tests.

## Editor decisions after round-2 reviewer 9 (owner may override)
- E4. Two certificate scopes: "certified among directly evidenced routes" and "certified across all eligible native Plan routes".
- E5. The matched-cost blocker is an API cost-shape check only; the Plan workload check is the M_AA-mix identification status.
- E6. The matched-cost panel may use any leaf with exact-variant per-task cost (incl. DeepSWE tokens × price list, FrontierCode), not only AA-index leaves; a feasibility matrix is published.

## Reviewer 9 (Claude Sonnet 5.5, round 2, Thinking) — adopted
- Critical: certification uses only an identified AA-mix multiple; M_observed vs M_AA-mix with identification mechanism; unidentified target-mix Plan cost cannot be certified.
- Certificate scope labels and per-row identification/eligibility release fields (E4).
- Plan blocker split (E5); certification-feasibility matrix with pre-fixed panel rule (E6).
- certificate_role per uncertain input; no zero uncertainty for missing repeatability; monotonicity tests.
- Reset-phase attainability with a time-indexed LP where windows and billing periods misalign.
- Superseded prose removed (Bug Hunt interval, serving-snapshot coupling); normative definitions govern.

## Owner decisions (after round-2 reviewer 10)
- O15. The scored API cost becomes an SDLC cost basket replacing total Index cost: Coding Agent Index (incl. DeepSWE), FrontierCode, ITBench-AA, MMMU-Pro, AA-Briefcase, GDPval-AA, GDP.pdf, AutomationBench-AA, Terminal-Bench 4.0, SciCode, AA-LCR; excluded HLE, Omniscience, CritPt. Supersedes O5/O9 for the scored cost (total Index cost becomes a diagnostic).
- O16. Plan rows without an identified AA-mix multiple keep being scored, flagged "workload-unmatched"; certification still requires an identified multiple.
- Feasibility check (2026-10-19): AA total Index cost = Σ cost per task × fixed task counts (Briefcase 91, GDPval 220, GDP.pdf 100, AutomationBench 657, Terminal-Bench 66, SciCode 288, LCR 100, HLE 2158, CritPt 70, Omniscience 6000), exact to <0.002% for all rows; Coding Agent Index page exposes per-configuration costUsd; FrontierCode/MMMU-Pro cost charts need browser capture; ITBench-AA cost source not yet located. Basket is phased by capture.

## Editor decisions after round-2 reviewer 10
- E7. "Recommended" = interval-certified among directly evidenced routes.

## Reviewer 10 (Grok 4.7, round 2, Thinking) — adopted
- Pairwise common-support certification (≥70% common weight; no [0,100] fills in Θ_cert); scenario-supported on the same estimand; S2 as max rank change, not a hurdle.
- Unidentified inputs ≥5% weight block pair certification unless a pre-registered bound exists.
- Bug Hunt unit fix (z = 100·x/105, test vector 52/105 → 49.52).
- TB4 quality row by pre-registered agent preference, never best-of-agent; matched cost uses AA exact per-evaluation cost only.
- Lexicographic Plan route choice; finer route key; page diffs flag, measurements clear.
- Pairwise matched-cost reversal against the leader blocks certification.
- Executable cohort rule; Omniscience count-level definitions; single governing Plan formula with test; clip gate ≥ 2 rows; scored-field release assertion.

## Reviewer 10 (Grok 4.7) — rejected or modified
- Withhold Plan scores without identified AA-mix multiple: modified by owner (O16) — scored and flagged; certification only with identification.
- Expired routes leave the Plan ranking entirely: O13 kept (API-cost fallback, flagged, excluded from Plan claims).

## Owner decisions (after round-2 reviewer 11)
- O17. A row missing a basket component's cost is scored on its available subset, flagged "subset cost — not comparable for certification", with its cost compared against the cohort on the identical subset.

## Editor decisions after reviewer 11 (owner may override)
- E8. Common-support quality is renormalised within each pair (keeps 25:75 on retained evidence; 1/p_ij published).
- E9. The basket prices one deployment-equivalent pass per task (evaluation repetitions excluded, as in AA's totals).

## Reviewer 11 (Kimi K3, round 2, Thinking) — adopted
- Critical: Plan transport targets the versioned scored workload W (M_W), bound to workload hash, price list and quota schema; old AA-suite transport qualifies only if it covers W.
- Governing pairwise common-support certificate formula; directed certification matrix; cycles allowed; full-composite bounds only for frontier/threshold outputs.
- Omniscience denominator corrected to AA's definition (N = 100[1 − i/(i+p+a)]); test vector.
- Workload object: unique execution components, aggregate/component exclusivity, frozen membership per version, migration bridge.
- Matched-cost blocker reads C_W; either blocker fails certification; reversal defined with interval separation.
- Exchange rates computed from active anchors; additional release tests.

## Editor decisions after reviewer 12 (owner may override)
- E10. Subset calibration contract: each used subset is a versioned workload W_S with frozen subset anchors from reference configurations evidenced on it; paired full/subset results are published; the row keeps its O17 score and position, labelled "cross-workload ordering not identified" (answers GLM Q1 from O17's "flagged" wording).
- E11. Certificate validity is margin-based: every retained input enters through an admissible constraint or its documented domain worst case; no constraint and no domain = unevaluable. The 5% rule is only a disclosure trigger.
- E12. Plan uncertainty split: measurement object (S0) vs transport object (S1); "not separable" label where public evidence cannot split them.
- E13. Robustness outputs are named estimands; "S2 maximum rank change" means displayed-score rank; pairwise recommendation robustness is reported as edge changes (answers GLM Q2).

## Reviewer 12 (GLM 5.3, round 2, Thinking) — adopted
- Certified = certified outgoing win against every competitor; "undefeated" is a diagnostic; four-state pair outcome; per-pair machine-readable record.
- Simultaneous scenario-leadership event L_i(s) for the 90% rule; undefined comparisons are not wins.
- E10–E13; Omniscience prose wording aligned with AA's hallucination definition; three new release tests.
- Source adapter keys total run cost vs weighted cost per task by field identity (already in the source contract; reaffirmed).

## Editor decisions after reviewer 13 (owner may override)
- E14. Pairwise cost term = 0.25 κ_W [ln C_j,W − ln C_i,W], κ_W fixed per release/basis from full-workload anchors, unclipped; subset-cost rows have no certifiable edges.
- E15. Workday-feasible Plan multiple (40-hour week LP) published as a diagnostic; full utilisation stays the scored estimand (O3).
- E16. Pair SWE gate made explicit: ≥2 common SWE leaves and ≥40% common SWE weight; not loosened.
- E17. Matched-cost c_ib counts model API token charges only; unseparable harness/retry tokens leave the leaf unpriced for that row.
- E18. Soft-expiry change detection is scoped to pricing, rate-limit and model-availability sections; ≥2 independent user reports of an undocumented limit change also trigger it (answers Gemini Q1).
- E19. Harness-mismatch stress branch for Bug Hunt from tbench.ai same-model cross-agent spreads (S2 stress only).
- Answer to Gemini Q2: a model lacking exact-variant DeepSWE stays ranked and provisional (not certifiable) until that run exists, whatever its margin elsewhere — the existing provisional rule, consistent with no transfer between variants.

## Reviewer 13 (Gemini 3.8 Flash, round 2, Thinking) — adopted
- Critical: certificate exchange rate fixed across pairs (E14). Duty-cycle concern adopted as a diagnostic (E15) — scoring change would challenge O3.
- E16–E19.

## Reviewer 13 (Gemini 3.8 Flash) — rejected
- Loosen pair SWE gate to 30% and one anchor: rejected; loosening a gate to produce more certificates weakens the evidence behind "recommended".
- Omniscience N = 100(1 − i/total): rejected; the leaf follows AA's own hallucination definition (incorrect ÷ non-correct), and abstention is already penalised through accuracy A at 2/3 weight. The cited examples are not non-monotonic.
- Within-group Dirichlet α = 200 × w for uniform CV: rejected; the reviewer's premise is off (science leaves are 12.5% of their group, so α = 6.25 gives CV ≈ 37% on a 1.25% leaf, i.e. ±0.46 weight points); Dirichlet CV necessarily varies with share, and realised per-leaf CV is already published.

# Round 3 begins

## Owner decisions (after round-3 reviewer 14)
- O18. Certification is blocked by a value-margin workload check: an edge must also hold when cost is computed on the matched priced-leaf workload (own frozen anchors); a cost-order reversal alone is a published warning.
- O19. Certification constraints are limited to published intervals, public repeated runs, structural bounds and full score domains; analyst-assumed allowances (e.g. repeatability bands) are sensitivity-only.

## Editor decisions after reviewer 14 (owner may override)
- E20. Anchor object: c_L = reference min ÷ 2, c_H = reference max × 2 (reference cohort never clips); one governing clip gate per basis (hold if > max(1, 10% of rows) clip or any row is beyond an anchor by > 2×); first-release fixture must pass.
- E21. Definite/possible frontier defined over the joint admissible set with full-composite quality.
- E22. Target-basket readiness table with per-model expenditure shares and HHI (diagnostic).
- E23. Price-cancellation release test split into uniform-scaling, proportional-mix and category-repricing cases.
- Superseded formulas (harmonic token-mix multiple, full-composite value certificate, 5% blocking rule in the summary) removed from governing text.

## Reviewer 14 (GPT-6.1 Sol, round 3, Thinking) — adopted
- All findings: clip-gate initialisation contradiction (E20), price-test condition (E23), value-margin blocker (O18), frontier quantifiers (E21), readiness/concentration (E22), repeatability constraint basis (O19), superseded formulas removed.

## Owner decisions (after round-3 reviewer 15)
- O20. The O18 alternative-workload value check uses API costs and blocks API certification only; on the Plan basis it is a labelled API-economics diagnostic, and Plan certification relies on identified M_W (never reused for W_alt).
- O21. Frozen headline contest: the comparison set J is generated by a published eligibility algorithm before margins are computed and is identical for every candidate; a pair-level gate failure or unevaluable comparison keeps the rival in J and prevents certification; restricted results only as "certified within the named evaluation panel".

## Editor decisions after reviewer 15 (owner may override)
- E24. W_alt = quality-weighted complete benchmark passes (C_alt = Σ w'_b × one-pass cost), invariant to task granularity; C^match ≡ C_alt (one construction for check and warnings); split/merge invariance tests.
- E25. Draw-kernel objects with a declared hierarchy; interval-only inputs get a conventional kernel plus an endpoint-heavy alternative; no defensible kernel → bounds-only; unspecified kernel fails the build.
- E26. Basket admission against a frozen named reference panel (≥ two-thirds of ranked rows at admission); admitted membership frozen per W; later missingness → O17/E10 without changing W's hash. Supersedes the every-ranked-row phasing.
- E27. Typed per-pair certificate record (basis, workload hashes, cost estimands, multiple id, alternative-check role).
- Data note (2026-10-19 capture): Coding Agent Index = DeepSWE v1.1 (113) + SWE-Atlas QnA (124) + Terminal-Bench v4 (66) = 303 tasks; AA's total = mean cost per task × 303 (one pass, repeats averaged); 40 priced configurations; exact model+effort match for 16 of 19 ranked rows. Terminal-Bench 4.0 is priced twice (AA harness and vendor agent harness) per O15, overlap disclosed.

## Reviewer 15 (Claude Sonnet 5.5, round 3, Thinking) — adopted
- Plan basis of the alternative check (O20); execution-unit contract for W_alt (E24); frozen contest (O21); kernel objects (E25); admission/persistence state machine (E26); legacy two-row clip sentence removed (left behind by a faulty r14 edit); typed certificate record (E27); five integration tests.

## Owner decisions (after round-3 reviewer 16)
- O22. Drop the entire "recommended" feature. Removed with it: the leader rule, pairwise certification and certification matrix, the frozen contest (O21), the matched-workload value blocker (O18/O20), pair-level gates (E8, E14, E16), certificate scopes (E4, E7) and the typed certificate record (E27). Kept: the weighted value-score ranking, frontier and cheapest-above-a-bar outputs with their interval logic, scenario shares, diagnostics. O19's constraint basis now governs the remaining interval outputs.
- O23. MMMU-Pro is dropped from the SDLC cost basket.
- O24. Both priced Terminal-Bench executions stay (AA Index run and the Coding Agent Index's vendor-agent run); overlap disclosed.

## Editor decisions after reviewer 16 (owner may override)
- E28. Accounting identities split: AA's Index total decomposes into ten evaluations; C_W uses the seven SDLC ones; HLE + Omniscience + CritPt is a reconciliation residual, never in C_W. Coding Agent Index cost = AA's published "Total Cost" (sums.costUsd), task count included stored, missing telemetry recorded (not imputed), "partial component" flag; chart totals rounded to USD 1 are rounding intervals; AA's "*" (declined tasks) flags partial component.
- E29. Bug Hunt estimand = mean of published runs for the exact model/effort/harness; public repeated runs are measurement evidence; single-run rows use the full score domain in interval outputs (O19).
- E30. Plan LP encodes each window's recorded semantics (session-anchored / fixed reset / sliding; unknown → conservative sliding), model-specific sub-caps and burn coefficients (never borrowed); burst fixtures.
- E31. Pinned source fields (AutomationBench-AA automationBenchPartialScore; Omniscience accuracy and hallucinationRate; GPQA gpqa legacy series; Coding Agent Index sums.costUsd; Bug Hunt runs).
- E32. A multiple that cannot be repriced on the release price list leaves M_W unidentified (score kept under O16, flagged "valuation basis differs", excluded from Plan interval outputs).
- E33. Report concordance is checked on unpooled reports (max/min ≤ 1.20) before geometric pooling.
- E34. AA cost embeds AA's cache protocol; cache-rate variation is an S2 stress branch, not an S0 redraw.
- E35. Formal quality bounds Q^L/Q^U = min/max of the full composite over the joint admissible set; outputs cite only the joint normative tests.
- E36. Expired-route API fallback rows (O13) are labelled "cross-estimand ordering not identified" and excluded from Plan interval outputs.
- Exchange rate split into two named quantities (anchor rate; within-cohort influence) with a flag when cost's influence share < 10%.

## Reviewer 16 (Grok 4.7, round 3, Thinking) — adopted
- Index-vs-basket accounting split (E28); unrepriceable multiples (E32); window semantics and sub-caps (E30, partly); Omniscience wording corrected (AA's Index uses 2:1 too — the r06-era "AA uses 1:1" statement was wrong; verified in data/aa_metrics.json weights 10%/5%); Bug Hunt estimand (E29); exchange-rate split; joint bounds (E35); pinned fields (E31); expired-row label (E36); concordance (E33); group renamed "Long context, science & knowledge"; cache stress (E34).
- Critical findings on the contest and the value blocker became moot with O22.

## Reviewer 16 (Grok 4.7) — rejected or modified
- "The only legal 5-hour constraint is sliding": modified (E30). Claude-style 5-hour windows are session-anchored (start at first use); a sliding constraint is stricter and is used only when semantics are unknown. The burst fixture holds under both.
- O4/O7 challenge (drop transfers across models with different burn rates): no change. Transfers stay labelled assumptions that never identify M_W (so they are already excluded from interval outputs); the owner authorised them knowing allowances are model-specific (AGENTS.md, 2026-10-18). Fable is not in the ranked roster.
- "The Coding Agent Index publishes no documented total": incorrect; AA publishes "Total Cost Across the Artificial Analysis Coding Agent Index" (sums.costUsd), equal to per-task mean × tasks included.
- MMMU-Pro "would swamp the basket at question-level multiplicity": incorrect (the basket sums each evaluation's total cost, USD 4–186 for MMMU-Pro); the owner dropped MMMU-Pro anyway (O23).
- Retire pending components after two releases: rejected; pending components do not enter C_W and are visible in the readiness table, so retiring them only adds workload churn.
- Drop GPQA as "no current AA series": rejected; AA still publishes a GPQA Diamond evaluation page and per-model values (field gpqa, present for current models); pinned as a legacy series.
- Bug Hunt single-run rows "unidentified, pair unevaluable": modified; under O19 the full score domain is an admissible constraint (E11), so the row is bounded, not unevaluable.

## Editor decisions after reviewer 17 (owner may override)
- E37. Cost completeness predicates: per component required / executed / cost-observed task counts; CompleteCostEvidence and FullCost(i, W). Displayed score keeps AA's published totals with a "partial component (k of n tasks priced)" flag; interval outputs require FullCost (verified 2026-10-19: Coding Agent Index totals are complete for 13 of the 16 matched rows; Gemini 4 Argon 302/303 tasks, GPT-6.1 Sol 301.6, Qwen3.8 Max 301.3).
- E38. Cheapest-above-a-bar quantifies over j ∈ R_W∖{i} (no self-comparison); ties prevent a unique label and go to the candidate set (answers Kimi Q1: no separate co-cheapest label); every frontier/bar result publishes its universe and whether it extends to the selected cohort (answers Kimi Q2: certify the named evaluable set, and state the cohort extension separately); two-stage evidence-loss test.
- E39. Plan capacity schedule contract: published grid and boundary treatment; session-start variables or schedule enumeration; conservative feasible schedule when semantics are insufficient; every identified capacity result carries a feasible schedule, else a lower/upper interval.
- E40. Interval outputs use a deterministic decision procedure (extreme-point search over shared factors, monotone bounds), statuses certified / disproved / unresolved / unevaluable, tolerance and witnesses; never Monte Carlo.
- E41. Workload cross-check warning pre-registered at τ_b < 0.5; "uncertain agreement" when the interval spans 0.5.
- E42. Task-family overlap matrix beside the expenditure HHI.

## Reviewer 17 (Kimi K3, round 3, Thinking) — adopted
- Critical: confirmed-cheapest self-comparison fixed (E38). Partial-telemetry eligibility (E37), scope fields (E38), session-start schedule contract (E39), interval decision procedure (E40), cross-check threshold (E41), overlap matrix (E42).
- Note: the first Kimi run (r17) failed in the browser driver before answering; the review was re-run on the same prompt.

## Editor decisions after reviewer 18 (owner may override)
- E43. E40's extreme-point search replaced by decision-specific feasibility: exact monotone extremes when no shared factor exists; certified interval branch-and-bound over shared factors otherwise (unresolved at depth limit); exact strict inequalities; witnesses re-checked; interior-witness release test.
- E44. Workload-demand evidence object x_iW (category token vectors) required for additive-capacity transport; optimise capacity over the feasible demand set when only partial token data are public; a dollar total never identifies x.
- E45. Possible-cheapest set K_r defined (cheapest among qualifiers in at least one common admissible state; ties allowed); outputs: confirmed unique cheapest, certified K_r members, unresolved, provisional status.
- E46. Uncertainty objects carry estimand, randomness_unit, constraint_target, coverage_claim, supporting evidence; declared target = expected performance over repeated executions of the fixed published suite under the stated deployment policy (answers GLM Q2); observed ranges keep their observed-range meaning.
- E47. Completeness statuses: confirmed complete / unresolved / confirmed incomplete. AA's Coding Agent Index fields are unrounded floats with explicit per-component attempt counts (answers GLM Q1: no explicit cost-observed counts or task identifiers), so T = n·μ at source precision over the fixed n-task set confirms completeness; chart totals rely on AA's declined-tasks marker.
- Answer to GLM Q3: category token vectors are partly public (AA Index evaluations: input, cacheable input, reasoning and answer tokens per evaluation; Coding Agent Index: mean input, output and cache tokens per task). No current Plan route identifies M_W by any mechanism, so every route is "workload-unmatched" today (O16).
- Answer to GLM Q4: the implementation will follow E43 (no endpoint-only search).
- Singleton cheapest fixture corrected (provisional singleton gets no confirmed label).

## Reviewer 18 (GLM 5.3, round 3, Thinking) — adopted
- All findings (E43–E47, fixture fix).
- Note: the first GLM run timed out waiting for Perplexity's model button (page slow to render); the driver now waits up to 60 s and the review was re-run on the same prompt.

## Owner decisions (after round-3 reviewer 19)
- O25. Interval outputs (definite/possible frontier, confirmed/possible cheapest above a bar) protect the **published record**: benchmark results and costs as published for each exact configuration, robust to reporting precision and missing evidence. Run-to-run noise, published confidence intervals and cost-variance kernels are reported only through the scenario shares. Supersedes E46's declared target for Θ; O19's exclusion of analyst assumptions stands.

## Editor decisions after reviewer 19 (owner may override)
- E48. GPQA Diamond retired at this quality version: AA no longer evaluates new frontier models on it (no value for 10 of the 19 ranked rows in the 2026-10-17 snapshot: Opus 5.5, Sonnet 5.5, Haiku 5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna, Grok 4.7, Gemini 4 Argon, both MiMo rows). Science leaves HLE, SciCode, CritPt take 5/3% each (group 10% unchanged). This corrects the reviewer-16 rejection, which wrongly said the series was present for current models.
- E49. Target-compatibility gate: an interval narrows a Θ variable only when its constraint target is that published-record variable (or a public justified mapping exists); confidence intervals and run ranges stay in the scenario layer.
- E50. Solver dependencies compiled from the full decision equations; a bar's reference quality is a shared variable; breakpoint enumeration or certified branch-and-bound; three-row regression test; separate proof obligations for witnesses and infeasibility.
- E51. Claim contract per interval result (decision, target, universe, evidence-set coverage, solver status, cohort extension, certificate); wording "confirmed within the declared evidence set".
- E52. Reference-quality object: a pinned reference keeps defining the bar after losing cost or Plan eligibility (answers Gemini Q2: yes); it competes only if in R_W; never silently substituted.
- Answer to Gemini Q1 (cost estimand): under O25 the interval target is the published deployment-equivalent cost of the fixed workload; future-pass variability is a scenario-layer quantity.

## Reviewer 19 (Gemini 3.8 Flash, round 3, Thinking) — adopted
- Bar-threshold counterexample (E50), target-compatibility gate (E49, resolved by O25), certificate vs coverage (E51), reference object (E52), cost estimand (O25).
- Note: the first Gemini run failed because Perplexity's home page did not render its composer; the driver now reloads with backoff and the review was re-run on the same prompt.

# Round 3 complete (reviewers 14–19). Every panel model returned HAS FEEDBACK on its draft; round 4 starts with GPT-6.1 Sol on draft r19.

# Round 4 begins (reviewer 20 onward)

## Owner decisions (after round-4 reviewer 20)
- O26. LiveBench instruction following is retired (LiveBench 2.0, released 2026-10-14, has no instruction-following suite; verified on livebench.ai 2026-10-19: categories Agentic, Reasoning, Coding, Browser Use, Data Analysis, Research, Design). AA-Omniscience takes the reliability group's full 10%. Independent (non-AA-executed) quality weight becomes ≈20%.

## Editor decisions after reviewer 20 (owner may override)
- E53. Completeness unit stays the task support of the deployment-equivalent pass (E9); attempt coverage (e.g. 905 of 909 attempts) is published as a precision diagnostic and enters only the scenario layer (O25). Modifies reviewer 20's attempt-level eligibility proposal, which would leave no row eligible because AA publishes no per-attempt cost telemetry (answers GPT Q3: the capture documents per-component attempt counts, aggregate totals and means only).
- E54. Funding-aware Plan capacity: purchase policy per route (default: conditional on the measured additional cash — answers GPT Q1), non-overlapping funding flows, shared limits bind combined flows; unidentified when payment-to-capacity relationships are not public.
- E55. Matched cost over canonical execution families with frozen diagnostic weights; quality leaves reference one family; split invariance restated (fixes the algebraic contradiction in the r19 test).
- E56. Capacity results publish feasible lower bound, relaxed upper bound, grid resolution and optimality scope; point capacity only when the bounds coincide; otherwise the interval enters Θ.
- E57. Exposure vectors by dataset origin, execution organisation, harness and grader, computed from admitted evidence; leave-AA-out by execution organisation.
- E58. Scenario targets and sampling levels per stochastic input; expected-performance uncertainty kept separate from run-to-run variation.
- Answer to GPT Q2: no current LiveBench instruction-following artifact exists for the cohort (resolved by O26).

## Reviewer 20 (GPT-6.1 Sol, round 4, Thinking) — adopted
- LiveBench source finding (O26), funding-aware capacity (E54), matched-cost invariance (E55), capacity bounds (E56), scenario targets (E58), exposure vectors (E57).

## Reviewer 20 (GPT-6.1 Sol) — modified
- Attempt-level completeness as an eligibility gate: modified (E53). Under E9 the estimand is one deployment-equivalent pass with repetitions averaged; missing repetitions change the precision of a task's mean, not the support of the pass, and under O25 precision belongs to the scenario layer. Attempt coverage is published.

## Editor decisions after reviewer 21 (owner may override)
- E59. The headline names the active basket version and components ("SDLC basket v1: 7 AA Index SDLC evaluations + Coding Agent Index; pending FrontierCode, ITBench-AA").
- E60. Anchor exchange rate and within-cohort cost influence printed beside the first table, with a sensitivity curve over c_H/c_L; the 10% influence flag is informational (answers Sonnet Q3: β is fixed by O2).
- E61. Plan identification-yield table per route; Plan headline labelled "workload-unmatched: exploratory" while fewer than half of Plan rows have an identified M_W (answers Sonnet Q1: today no route has an identified M_W, so the label applies).
- E62. Independent-source rank check (Kendall τ_b vs a ranking from independently executed leaves only, bootstrap interval) beside the "not identifiable" leave-AA-out note.
- E63. Active-rules manifest per release (fired / passed / vacuous / unresolved).
- E64. Standing sensitivity columns: drop the AA Index-run Terminal-Bench cost; leave Bug Hunt out; worked attempts-reconciliation example.
- Answer to Sonnet Q2: the first release ships as "SDLC basket v1" with its composition named (E59), not as a full ten-component basket.

## Reviewer 21 (Claude Sonnet 5.5, round 4, Thinking) — adopted or modified
- Adopted: basket labelling (E59), identification yield (E61), independent-source check (E62), active-rules manifest (E63), cost-weight disclosure (E60), overlap and Bug Hunt sensitivity (E64).
- Corrected premise: "only one basket component is admissible" — incorrect; the seven Index SDLC evaluations (19/19) and the Coding Agent Index (16/19) are admitted (8 of 10 target components). The draft's capture-status wording was ambiguous and is fixed.
- No change: the 30-day soft expiry already fires on detected change and acts as a backstop; the Omniscience reconstruction is already tested against AA's published fields each release.

## Owner decisions (after round-4 reviewer 22)
- O27. The Coding Agent Index cost record is AA's documented cost-to-run metric (average pay-per-token API cost per task — a pooled per-task-attempt average that excludes missing telemetry, per AA's coding-agents methodology page, verified 2026-10-19) × the 303 required tasks. A component is incomplete only where AA itself marks tasks missing or declined (e.g. the chart "*" marker); unseen telemetry gaps and unequal attempt coverage are cost precision (scenario layer). Supersedes the T = n·μ completeness certificate (E47) and resolves reviewer 22's two High findings.

## Editor decisions after reviewer 22 (owner may override)
- E65. Paired-panel rank changes: baseline and branch ranks on their common evaluable panel, with panel size, exclusions, scores, retained weight and workload hash; release-wide changes labelled as including composition effects.
- E66. E62 split into two named checks on one matched panel: quality agreement (observed quality vs independent-only quality) and quality-substitution value agreement (value with Q_ind, cost held fixed; not a validation of costs or multiples). Answers Grok Q2: both questions are published, named separately.
- E67. Plan identification taxonomy: point-identified / set-identified (finite positive interval) / unidentified, with representation recorded; point- and set-identified routes are eligible; yield counts them separately.
- Answer to Grok Q1: AA documents its coding-agent cost, tokens and time as pooled per-task-attempt averages that exclude missing telemetry (artificialanalysis.ai/methodology/coding-agents-benchmarking, 2026-10-19); sums.costUsd is not documented and is kept as a diagnostic.

## Reviewer 22 (Grok 4.7, round 4, Thinking) — adopted
- Aggregation and chart-marker findings resolved by O27; paired panels (E65); E62 estimands (E66); Plan taxonomy (E67).

## Editor decisions after reviewer 23 (owner may override)
- E68. Same-execution contract for cost per solved task (shared observation key; Terminal-Bench uses the AA-priced execution's resolved fraction — answers Kimi Q2).
- E69. The scored Plan capacity target is token-equivalent (API-priced) capacity, as AGENTS.md defines Plan value; completed-pass capacity is a diagnostic from task-level schedules where public, else "not identified" (answers Kimi Q1 from the existing definition, no owner change).
- E70. Full-utilisation wording aligned with the governing formula (maximum eligible consumption under all evidenced constraints; binding and slack limits published).
- E71. Disjoint-evidence agreement: AA-executed-only vs independently-executed-only quality, labelled a restricted evidence comparison.
- E72. Monte Carlo precision: standard errors per published frequency; anytime-valid interval; pre-registered expansion to 160,000 scenarios; "scenario threshold unresolved" otherwise.

## Reviewer 23 (Kimi K3, round 4, Thinking) — adopted
- All findings (E68–E72).

## Editor decisions after reviewer 24 (owner may override)
- E73. Constrained evidence model: the primitive-variable constraint graph is authoritative; box reductions only with a decision-specific proof; outer enclosures prune, original constraints certify; infeasible-favourable-state fixture.
- E74. A set-identified M_W enters the displayed score at its lower bound (lower-capacity-bound convention), also for Plan anchors; joint cost and value intervals and upper-bound rank sensitivity published (answers GLM Q1, consistent with the existing lower-bound route rule).
- E75. Plan numerator eligibility ledger: delivered execution under the declared policy, including permitted retries, counts; failed/rejected requests, platform overhead and evaluation-only repetitions do not; unseparable receipts → bound or unidentified transport (answers GLM Q2 from the existing "eligible usage delivered" definition).
- E76. Completed-work diagnostic in workload-equivalent passes on identical support; restricted-support diagnostic otherwise.
- E77. Sequential Monte Carlo rule: 16 looks to 160,000; Clopper–Pearson at α/16, α = 0.05 per published event; met / not met / continue / unresolved (answers GLM Q3: per event, family declared).
- E78. "Configuration" terminology, configuration IDs and per-leaf execution manifests.

## Reviewer 24 (GLM 5.3, round 4, Thinking) — adopted
- All findings (E73–E78).

## Editor decisions after reviewer 25 (owner may override)
- E79. Feasibility prerequisite: a certified feasible witness for each decision's full constraint component before any label; infeasible → "inconsistent evidence" (release-blocking for that output); unresolved → no confirmed or definite label; two empty-set fixtures.
- E80. Consumption-dependent payments: joint representation; purchases fixed by the route's declared purchase policy (answers Gemini Q1); maximise eligible consumption, gross cash at the solution, minimum-cash tie-break; unbounded or unestablished → unidentified.
- E81. "Effective weights" renamed normalised weighted spread; a signed covariance allocation on a declared common complete panel is added.
- E82. Coding Agent Index fixtures aligned with O27 (scored cost = pooled mean × 303; sum and sum ÷ mean are diagnostics; AA markers alone decide completeness).
- Answer to Gemini Q2: the solver is being implemented in valuerank/intervals.py alongside the review; it will include the E79 prerequisite.

## Reviewer 25 (Gemini 3.8 Flash, round 4, Thinking) — adopted
- All findings (E79–E82).

# Round 4 complete (reviewers 20–25). Every panel model returned HAS FEEDBACK; round 5 starts with GPT-6.1 Sol on draft r25.

# Round 5 (reviewer 26 onward)

## Editor decisions after reviewer 26 (owner may override)
- E83. Scenarios sample the primitive variables of the constrained evidence model and derive costs, capacities, multiples and scores; identity and feasibility checks per scenario; no undeclared rejection sampling; fixtures.
- E84. Demand–cost reconciliation contract for the Plan demand vector (same aggregation and telemetry support as the scored cost; never rescaled; otherwise transport unidentified).
- E85. Executable route comparator: point > set > unidentified; controlled measurement > concordant reports > owner-named transfer; comparison multiple (point or lower bound); lower gross cash under the declared purchase policy; route ID (answers GPT Q1 and Q2).
- E86. Per-row workload ID, anchor-object ID and applicable exchange rate; subset rows marked; slider keeps row-specific anchors.
- E87. Row-level scenario dispersion per stratum with a separate covariance term; cohort SD reserved for the influence diagnostic.

## Reviewer 26 (GPT-6.1 Sol, round 5, Thinking) — adopted
- All findings (E83–E87).

## Editor decisions after reviewer 27 (owner may override)
- E88. Route-dominance pre-filter before the E85 comparator: drop route b when an admissible route a for the same configuration, workload and basis has grade ≥ b's and identified multiples with L_a > U_b (a sufficient condition under any joint constraints); unidentified routes neither filter nor are filtered; dropped routes stay in the release data with the reason; the official route is "evidence-priority selected". Answers Sonnet Q1 without escalation: evidence-grade priority stands because AGENTS.md keeps exact measured routes ahead of shared assumptions; identification precision no longer overrides certified dominance.
- E89. Separability condition for the monotone-corner shortcut: exact only when no shared factor and no row-local coupling (row feasible set = product of its C and Q ranges); row-local coupled primitives are branched over like shared factors; unsupported constraint classes return unresolved; Sonnet's three-configuration fixture (i dominated for every t although its box corner is undominated) must return disproved. v1 rows draw C and Q from distinct published records, asserted per release.
- E90. GDPval temporal estimand: AA's published GDPval-AA v2.1 Elo as integrated in the pinned Index version (frozen at a configuration's addition; AA methodology verified 2026-10-19). Verified that AA's leaderboard showed the same values on 2026-10-19 (Opus 5.5 1866, GPT-6.1 Sol 1594, Gemini 4 Argon 1624; 2026-10-17 snapshot 1866.27, 1593.85, 1623.99), so one published record exists today. Registry adds rating snapshot ID, fit or anchor revision and freeze status; refresh decomposition adds "benchmark-record update". Answers Sonnet Q2 without escalation because the two records coincide; if AA ever publishes a differing refitted rating, the release flags it, keeps the Index-integrated value and the question goes to the owner.
- E91. Within-cohort cost influence computed on the declared common-workload panel (main W and anchor object, same rows for both SDs, panel size and exclusions shown); subset strata separately; whole-table value only as "displayed-table dispersion"; zero denominator → undefined. The 10% flag uses the common-workload statistic.

## Reviewer 27 (Claude Sonnet 5.5, round 5, Thinking) — adopted
- All findings (E88–E91).

## Editor decisions after reviewer 28 (owner may override)
- E92. One eligibility predicate for both unique-cheapest labels: UniqueLabelEligible(i) = bar competitor ∧ ¬provisional; provisional rows still compete and can block; their scenario frequencies and K_r membership are published without a unique label; scenario fixtures added. Answers Grok Q1 without escalation: the draft's prose already excludes provisional rows from unique-cheapest results, so the normative scenario definition is aligned with it.
- E93. Comparator key 3 for unidentified routes = the observed multiple (lower bound where ranged), labelled "observed-workload multiple — target-workload ordering not identified"; routes record measurement workload, valuation basis and fee period; public token ledgers are revalued at the release price list, otherwise the multiples are compared as published with the basis difference stated; selection-reason field; unidentified-vs-unidentified fixtures. Answers Grok Q2 from the owner's AGENTS.md rule that the Plan basis divides by the highest eligible Value Multiple (Grok preferred skipping the multiple; that would contradict the owner rule).
- E94. Demand objects with units: t_ie per task, d_ie = n_e t_ie per component pass (or an evidenced component-pass vector with its aggregation operator), d_iW = Σ d_ie per workload pass; p·d_ie = C_ie and p·d_iW = C_iW; the capacity solver accepts only d_iW; λ in workload passes per fee period; units fixture.

## Reviewer 28 (Grok 4.7, round 5, Thinking) — adopted
- All findings (E92–E94).

## Editor decisions after reviewer 29 (owner may override)
- E95. One deterministic admission panel per workload version: candidates in descending exact-cost coverage (target order breaks ties); a component is admitted only if the rows complete on it and on every earlier-admitted component still number ≥ two-thirds of the ranked rows; that set is the reference panel; admission object published with marginal and joint coverage; fixture for two components that pass alone but not together. Answers Kimi Q2 without escalation: E26 already names one panel per W ("W's frozen, named reference panel").
- E96. Rank events: declared panel per series fixed before the draws (size named); branch exclusions change the declared panel, never the per-scenario denominator; competition ranks as in the displayed table (ties may put more than k rows at rank ≤ k, disclosed); pairwise win / tie / loss published separately; E65 common panels for baseline-vs-branch frequency changes. Answers Kimi Q3 without escalation: the displayed table already uses competition ranks.
- E97. Delivery is not outcome: "failed request" = no delivered execution; delivered, policy-permitted execution is eligible whether the task passes or fails (incl. model-generated refusals and permitted retries), matching the API basket's support; record fields and fixtures. Answers Kimi Q1 without escalation (E75 was an editor decision; this states its intended meaning).
- E98. Concordance stated exactly: the largest report at most 20% above the smallest (O11's "±20%" kept, with the operational form beside it); boundary fixtures 100/120 pass, 100/120.001 and 80/120 fail.
- E99. A one-leaf quality group takes within-group weight exactly one with no draw (already so in code); fixture.

## Reviewer 29 (Kimi K3, round 5, Thinking) — adopted
- All findings (E95–E99).

## Editor decisions after reviewer 30 (owner may override)
- E100. The scenario-supported-cheapest label is authorised only in the S1 core branch (full-composite quality with identification draws, nominal weights, transfers off, primary kernels); other strata and branches publish the event as a frequency only (S0: "observed-leaves qualifying-and-cheapest frequency"); 70%-coverage fixture; every label carries a decision target signature (quality equation, workload hash, basis, reference object, stratum, branch, route-selection version, panel ID, kernel version). Answers GLM Q1 without escalation: one designated full-composite branch, because the bar's normative definition is full-composite and S2's weight draws are a sensitivity around the owner's nominal weights.
- E101. Component admission tests complete cost evidence (exact cost without AA's missing- or declined-task marker), not exact-cost availability; matrices A_ie and K_ie and both joint panels P_A(W), P_K(W) are published; only P_K is called complete; declined-marker fixture. Answers GLM Q2 without escalation (E26/E95 are editor decisions; the complete-evidence predicate aligns admission with interval-output eligibility).
- E102. Report comparability before concordance: fee period and gross-cash accounting, route and limit schema, eligible-consumption treatment, valuation basis (repriced where receipts permit) and measurement workload must match; otherwise reports stay separate objects; report IDs and comparability failures published.
- E103. The matched-cost diagnostic is a versioned object D (families, weights, leaf-to-family map, price rule, panel rule); changes to D create a new version with an old/new bridge on the common panel.
- E104 (editor correction found while implementing). The source contract still named `sums.costUsd` as the Coding Agent Index cost; corrected to `mean.costUsd` × 303 under O27, with `sums.costUsd` as a reconciliation diagnostic.

## Reviewer 30 (GLM 5.3, round 5, Thinking) — adopted
- All findings (E100–E103).

## Editor decisions after reviewer 31 (owner may override)
- E105. Multiple certification under consumption-dependent payment: capacity bounds convert to M_W bounds only with fixed positive gross cash; otherwise the interval must enclose M* = U*/F* at the consumption-optimal, minimum-cash solution over admissible states (deterministic payment function: bound U/f(U) on a certified domain containing U*; schedule- or funding-dependent: certify the optimum and the tie-break or use conservative joint bounds; else unidentified); published fields; U = 10, F = 1 vs U = 20, F = 10 fixture.
- E106. One Plan admission decision table (OfficialDisplayEligible, TargetTransportIdentified, PlanIntervalEligible; five cases) replaces the residual "any other mismatch … excluded" sentence, which contradicted O16; displayed multiple M_W / L_W / M_observed or the authorised transfer; one fixture per case.

## Reviewer 31 (Gemini 3.8 Flash, round 5, Thinking) — adopted
- All findings (E105–E106).

# Round 5 complete (reviewers 26–31). Every panel model returned HAS FEEDBACK; round 6 starts with GPT-6.1 Sol on draft r31.

# Round 6 (reviewer 32 onward)

## Editor decisions after reviewer 32 (owner may override)
- E107. Versioned report set E_r,t before concordance (pre-registered discovery and cutoff, inclusion and exclusion reasons); concordance on every eligible report of a comparability partition together, never a searched-for passing subset; schema partitions only on public evidence of a schema change; failing partition → diagnostic-only; source count = distinct measurement objects; 100/110/150 fixture. Answers GPT Q1 without escalation: O11 requires the reports to be concordant, and a complete set that fails is not concordant; a different measurement regime is recognised only through E102 comparability or an evidenced schema change.
- E108. Certification grammar: primitive domains and original constraints, documented equivalence-preserving reductions, independently checked certificates; v1 classes = boxes, exact rational affine, separable monotone transforms, documented corner reductions; nonlinear equalities only with validated existence certificates; otherwise unresolved; x² = 2 fixtures.
- E109. Numerical-domain contract (finite non-negative component costs; log scoring only for 0 < c < ∞; anchors 0 < c_L < c_H < ∞; divisors finite and strictly positive). Answers GPT Q2 without escalation: a published zero workload cost is outside the supported scope (no cost or value score, flagged, excluded from anchors, never best value, no epsilon); the owner may extend the scope later.
- E110. Quality clipping audit per leaf (raw-domain validity, anchor position, clipping amount, affected weight, action); saturation disclosed; domain violations block the release; both in the manifest.

## Reviewer 32 (GPT-6.1 Sol, round 6, Thinking) — adopted
- All findings (E107–E110).

## Panel note (2026-10-19)
- Perplexity renamed the Sonnet picker entry from "Sonnet 5.5" to "Claude Sonnet 5.5"; the first round-6 Sonnet send failed with "model not selectable" and was resent with the new label (verified model: Sonnet 5.5 Thinking).

## Editor decisions after reviewer 33 (owner may override)
- E111. Measurement objects: each controlled measurement and each complete concordant report partition is a measurement object; the comparator selects among route–measurement pairs; magnitude decides only at key 3 after identification and grade, per the owner's highest-eligible Value Multiple rule (AGENTS.md), labelled; controlled outranks reports via the grade key; alternatives and rank sensitivity published; four fixtures. Answers Sonnet Q1 from the owner's rule and the E85 order (identification, grade, then the highest eligible multiple) rather than recency, without escalation.
- E112. The scenario-supported label must meet the threshold under every pre-registered kernel specification in S1 core (primary uniform and the E25 endpoint-heavy alternative, including missing-leaf domains), each by the E77 sequential rule; otherwise "primary-kernel frequency ≥ 90%; kernel-sensitive"; frequency range published; Sonnet's 97.9% vs 87.5% fixture. Answers Sonnet Q2 without escalation: E100 was an editor decision, and E25 already makes the alternative kernel mandatory.
- E113. Measured-only Plan view D_measured: controlled or concordant-report candidates only, selector rerun, identified vs unmatched statuses kept distinct, no API fallback ("no measured route"), official Plan anchors, E65 comparison with the official ranks. Answers Sonnet Q3 without escalation.
- E114. Drift flag defined exactly: D_g from d_b = w_b SD(z_b) on one common complete panel over the eligible leaf set B*, nominal shares renormalised over B*, thresholds 0.5 W_g and 1.5 W_g, "not estimable" otherwise; covariance allocation kept separate.

## Reviewer 33 (Claude Sonnet 5.5, round 6, Thinking) — adopted
- All findings (E111–E114).

## Editor decisions after reviewer 34 (owner may override)
- E115. Window semantics as identification: a set S_r of publicly admissible mechanisms; bounds L_r = min over s of verified lower bounds and U_r = max over s of relaxed upper bounds enclose the E105 multiple under every s; point only when they coincide; otherwise "semantics unresolved; conservative achievable capacity only", one-sided diagnostic, M_W unidentified; two fixtures. Answers Grok's owner question without escalation: E106 and E67 already fix the display — an unidentified M_W displays M_observed, and the conservative capacity is a one-sided diagnostic.
- E116. Comparator keys end with route ID then a canonical measurement-object ID; selected pair ID published; permutation-invariance fixture.
- E117. Workday diagnostic calendar: same fee period, balances, purchase policy, reset phase and semantics; availability indicator A(t) from a versioned calendar (IANA zone, weekdays, hours, fee-period bounds, partial days); workday maximum consumption ≤ full maximum regression test.
- E118. Zero observed quality (p_i = 0): "quality not scoreable — no observed leaves", no displayed quality or value score, never zero; the row stays in the cohort.
- E119 (editor correction found while implementing E112). E25's endpoint-heavy alternative is the arcsine law Beta(½, ½) on the same interval (as implemented); the E112 fixture used a two-point law (87.5%), which no pre-registered kernel produces. The fixture now uses a reference at 78: about 91.5% (uniform) vs 86.7% (arcsine), verified by simulation and in tests/test_scenarios.py.

## Reviewer 34 (Grok 4.7, round 6, Thinking) — adopted
- All findings (E115–E118).

## Owner decision (2026-10-19, answering Kimi K3 round 6)
- O28. The reliability leaf (AA-Omniscience, 10% of quality) is scored with AA's Omniscience Index: z = (I + 100)/2, I = 100 × (correct − incorrect) ÷ all questions (partial answers and abstentions count zero). Replaces (2A + N)/3 with AA's conditional hallucination rate, which is not monotone (98/1/1 → 82, 99/1/0 → 66). Accuracy and the conditional hallucination rate stay diagnostics; I is reconciled as 100 [A − h (1 − A)] each release (verified on the 2026-10-17 snapshot: GPT-6 Astra xhigh 43.42 = 100 × (0.6185 − 0.4832 × 0.3815)). The ledger's earlier rejection of a related claim ("the cited examples are not non-monotonic", reviewer 15 era) was wrong for this case.

## Editor decisions after reviewer 35 (owner may override)
- E121. Kernel assignments per event-relevant dependency block (candidate, reference, competitors); the registered check is block-exhaustive over the 2³ uniform/arcsine assignments, each by the E77 rule; label wording "supported under the registered kernel checks (block-exhaustive over candidate, reference and competitors)"; registry fields. Answers Kimi Q2 without escalation (E112 is an editor decision; per-input exhaustive assignment is intractable and is not claimed).
- E122. S0 and S1 use the primary price rule only; first-party vs cross-provider median is a named S2 branch with shared price primitives; uncertainty_layer field validated at build time.
- E123 (editor correction while answering Kimi). E106 case 4 and E93's "compared as published" clause conflicted with owner decision O7 (price-basis mismatches are unmatched and excluded from the official Plan ranking); O16 relaxed only the workload case. A measurement on another price basis now enters only after revaluation at the release price list from a public token ledger; otherwise it is diagnostic-only.

## Reviewer 35 (Kimi K3, round 6, Thinking) — adopted
- All findings (O28, E121, E122); E123 corrects E93/E106 against O7.

## Editor decisions after reviewer 36 (owner may override)
- E124. Plan identification roadmap and demand registry: AA publishes per-evaluation cost and output tokens per task and Index-wide category totals, not per-evaluation category splits, so the basket demand vector is set-identified (D_iW from component cost identities, per-component output tokens and Index-wide totals; never rescaled). M_W needs category-specific burn evidence or a workload-compatible controlled measurement, which no public source provides; the "exploratory" label is structural and the missing evidence is listed per route. GLM's pipeline is adopted as the registry; it cannot by itself identify M_W. Answer to GLM Q1 (not escalated as a methodology question): an owner-run measurement is admissible under O11 and the AGENTS.md numerator rules; commissioning one is an operational choice, raised with the owner in the session summary.
- E125. Same-harness Terminal-Bench diagnostic (default harness Terminus 2; τ_b against the primary ordering; per-row "harness-mixed" marker); the primary leaf keeps the pre-registered preference. Answers GLM Q3 without escalation (O6 names the tbench.ai leaf; the harness preference is an editor rule).
- E126. Symmetric influence flag (> 90% cost share → "quality not discriminating"), exchange-rate series across anchor versions, trimmed-anchor rank-shift diagnostic. Answers GLM Q2 without escalation.
- E127. E72 wording corrected: repeated-look-adjusted (Bonferroni over 16 declared looks), not anytime-valid.
- E128. Omniscience disclosure: unanswered-or-partial share (1 − A)(1 − h) per row (split where AA publishes counts) and the named sensitivity z_pen = max(0, I). Owner decision challenge to O28 noted; O28 unchanged.
- E129. Citations: GDPval transform cited to AA's methodology page (verified 2026-10-19, answering GLM Q4); LiveBench 2.0 cited by title and capture date because livebench.ai publishes no release date (GLM's 2026-10-13 and the ledger's 2026-10-14 could not be confirmed).
- Not adopted: a category-price revaluation branch (per-component category telemetry is not public and E84 forbids rescaling) and a LiveBench 2.0 cost companion (exact-variant coverage for the ranked configurations not yet captured; listed as a candidate diagnostic).

## Reviewer 36 (GLM 5.3, round 6, Thinking) — adopted with the two exceptions above
- E124–E129.

## Editor decisions after reviewer 37 (owner may override)
- E130. Demand accounting populations: the ten Index executions conserve against AA's Index-wide category totals with the three excluded evaluations as residual demand; the Coding Agent Index is its own population (no public category telemetry today); d_iW = Σ_S d_ie + d_iA; registry fields and three fixtures. Answers Gemini Q1: the implementation already kept the populations separate (the registry lists the Coding Agent Index among components without token telemetry and uses Index totals only for Index evaluations); the draft now states it.
- E131. Token ontology: exclusive canonical coordinates; AA's output tokens are inclusive of reasoning and answer (verified 37,901,142 = 13,409,872 + 24,491,270); subtraction only with matching support; three independent validations; equal-price fixture.
- E132. E121 defined over dependency blocks: blocks partition primitives, roles map onto blocks, merged when they share primitives, 2^B assignments over the non-empty blocks (eight in v1 when the role blocks are distinct), restricted coverage disclosed, assignment-set version named; four fixtures. Answers Gemini Q2 without escalation: exhaustive over non-overlapping dependency blocks (the v1 code already merges coincident blocks).

## Reviewer 37 (Gemini 3.8 Flash, round 6, Thinking) — adopted
- All findings (E130–E132).

# Round 6 complete (reviewers 32–37). Every panel model returned HAS FEEDBACK; round 7 starts with GPT-6.1 Sol on draft r37.

# Round 7 (reviewer 38 onward)

## Editor decisions after reviewer 38 (owner may override)
- E133. Kernel-check object: dependency components, kernel-switch groups, mapping, roles, exact assignment list, coverage, execution status; v1 switches by role group (candidate, reference, competitors) — competitor components are not exhaustively varied — and the label reads "supported under all registered role-group kernel checks"; resource-limit overruns withhold the label. Answers GPT Q1 without escalation: role-group switching keeps the check tractable (exhaustive switching would need up to 2^16 assignments for 16 rows) and the claim is narrowed to match.
- E134. Token-use variance: rounding draws and public paired observations only in S0; analyst ranges only in a named S2 stress branch; otherwise "not quantified"; build rejects S0 primitives derived from analyst conventions. Answers GPT Q2 without escalation: no exact-configuration evidence supports a parametric range today (the implementation draws cost from rounding intervals only).
- E135. E77 certification requires IID replicates from a fixed law per event and assignment; other designs publish descriptive frequencies only.
- E136. The undefined per-row "own normalised weighted spread" is dropped (common-panel spread and row-level scenario dispersion remain).

## Reviewer 38 (GPT-6.1 Sol, round 7, Thinking) — adopted
- All findings (E133–E136).

## Editor decisions after reviewer 39 (owner may override)
- E137. One governing kernel-check definition (consolidating E112, E121, E132, E133): dependency components → role switch groups (merged when roles share a component) → A = {uniform, arcsine}^G → published assignment list and hash; label iff UniqueLabelEligible and every assignment completed with its E77 lower bound ≥ 0.90; distinct outcomes (withheld, threshold unresolved, kernel-sensitive, not supported); fixture with several competitor components in one group. The superseded E121/E132 enumeration and "block-exhaustive" label text are removed.
- E138. Valuation compatibility consolidated into the admission rule: release basis → workload checks (O16 applies); revalued from a public ledger → continues; different and not revaluable → diagnostic-only (E106 case 4); basis not recorded → displayed with "valuation basis unverified", never interval-eligible. The stale "keeps the original valuation basis under O16" sentence is removed. Partly adopted: Sonnet proposed treating an unknown basis as not display-eligible; that would remove every current Plan route for missing metadata although O7 excludes only established mismatches, so unknown bases are flagged instead and the registry is to record them.

## Reviewer 39 (Claude Sonnet 5.5, round 7, Thinking) — adopted (E138 partly, reason above)
- E137, E138.

## Editor decisions after reviewer 40 (owner may override)
- E139. Measurement capacity status per measurement object (capacity established / observed usage, capacity not established / saturation unverified) with saturation and balance evidence; reports without established capacity are labelled "observed-usage multiple; full utilisation not established"; concordance never upgrades the status; fixed-cash attainable-consumption lower bound, E105 otherwise. Answers Grok Q1 without escalation: O11 admits concordant reports without a saturation requirement; adding one would change an owner decision, so the status is disclosed instead.
- E140. Basket admission by exhaustive enumeration of component subsets (2¹⁰ today) with |P(S)| ≥ ⌈2N/3⌉, maximising component count, then panel size, then target order; selected set, objective tuple and feasible alternatives published; Grok's counterexample as fixture; replaces E95's greedy order; current outcome unchanged (verified: eight components, 16-row panel). Answers Grok Q2 without escalation: O15 lists the components without priorities, so the count objective applies.

## Reviewer 40 (Grok 4.7, round 7, Thinking) — adopted
- All findings (E139–E140).

## Editor decisions after reviewer 41 (owner may override)
- E141. Effective-dated tariff records (observed_at, effective_from/until, tariff_status, applicability_conditions, scheduled_refresh_at, source evidence ID); prices applicable at the valuation timestamp; promotional flag and a documented-standard-tariff S2 branch; AA cost caveats shown per row (verified on the 2026-10-17 snapshot: Claude Haiku 5.5's long-context surcharge is not reflected in AA cost). Kimi's example could not be verified: AA's Gemini 4 Argon page (2026-10-19) shows standard Google prices ($2 / $10 per 1M tokens) and only a 95% cache discount, no launch discount.
- E142. Release-time route order: classify eligibility and expiry, drop diagnostic candidates, dominance filter, comparator, API fallback only when nothing survives; eligibility-transition reason; five fixtures. Answers Kimi Q1 without escalation: O13's fallback describes the effect when a demoted route leaves no eligible candidate; selecting a surviving eligible candidate is the comparator's ordinary rule (the implementation already behaves this way).
- E143. Scenario target profiles in every stream and decision signature, with build-time compatibility validation; v1 profiles: S0 reporting precision, S1 + conventional identification of missing leaves, S2 + weight-specification stress.

## Reviewer 41 (Kimi K3, round 7, Thinking) — adopted
- All findings (E141–E143).

## Editor decisions after reviewer 42 (owner may override)
- E144. Transfer provenance: a transfer names its donor measurement and inherits the donor's observation date, valuation compatibility, capacity status, expiry stage and change flags; authorising or editing a transfer never restarts the clock; a transfer is diagnostic-only whenever its donor is; an owner assumption without a donor (MiMo 1.5×) ages from its authorisation date; evidence age runs from the observation date (measurement window end, else publication date), never from a record's check date. Verified defect: the implementation aged the Claude common transfers from their 2026-10-18 authorisation record while their donor measurement dates from 2026-10-06, so they would have outlived the donor by 12 days; the transfers now name their donors (data) and inherit them (code, eight fixtures). Answers GLM Q1 without escalation: O13 governs all Plan evidence, and the 2026-10-18 authorisation applies Opus 5.5's measured multiples without a freshness exception.
- E145. Target profiles become an executable allowlist with precedence over the generic sampling text: v1 S0 = reporting precision only; S1 + conventional identification; S2 + weight stress; fitted-rating intervals and run ranges only in separately named streams (none in v1); build rejects violations; permitted and varied targets published per stream. The stale "drawn in S0" for repeat-measurement uncertainty and "measurement intervals" wording are corrected. Answers GLM Q2 without escalation: E122/E134/E143 already fixed v1 S0 as reporting precision, consistent with O25's published-record target; the implementation already drew only rounding intervals.
- E146. Deletion branches defined algebraically (remove R globally, renormalise remaining observed weights; zero denominator → unevaluable; primary cost, route and anchors kept; < 40% retained nominal weight → "not identifiable under the coverage rule"); evidence unavailability is a separately named branch. Implemented: one branch per leaf plus leave-AA-out (not identifiable today, 20% retained), common-panel rank changes and τ_b per basis.
- E147. Dependency components compiled per decision and stream from the primitives actually varied; role groups linked by a component switch together; components and hash published; the build fails when the compiled graph differs from the registered kernel-check object (v1: singleton components).

## Reviewer 42 (GLM 5.3, round 7, Thinking) — adopted
- All findings (E144–E147).

## Editor decisions after reviewer 43 (owner may override)
- E148. Admission units are exactly O15's ten named targets, each counted once whatever its accounting representation; unit evidence enters only at unit level (accepted aggregate or a composed complete decomposition), raw accounting children are rejected by the build, and a new unit is a basket migration; Gemini's six-row fixture added. Answers Gemini Q1 without escalation: O15 names the components, E140 already enumerated 2¹⁰ subsets of them, and the implementation already counted the Coding Agent Index as one unit.
- E149. E64's standing Terminal-Bench cost-removal column defined as a cost-deletion object separate from quality deletion, with two named calculations — original anchors (sensitivity of the published scale) and recalibrated anchors for W∖TB (exchange rate published) — and the Plan basis labelled a fixed-multiple arithmetic stress. Answers Gemini Q2 without escalation: E64 is an editor decision and both readings answer different questions, so both are published. Implemented (it had not been computed before).

## Reviewer 43 (Gemini 3.8 Flash, round 7, Thinking) — adopted
- All findings (E148–E149). Round 7 is complete; round 8 starts on r43.

# Round 8 (reviewer 44 onward)

## Editor decisions after reviewer 44 (owner may override)
- E150. The sequential interval names its parameters: per-look error allocation δ = 0.05/16, confidence 1 − δ = 0.996875, equal tails, Beta-quantile endpoints with the k = 0 and k = n cases, SciPy's confidence_level = 1 − δ; certificates record per_look_error, confidence_level, tail_allocation, k, n, L, U; closed-form endpoint fixture. Verified: the implementation already passed the error allocation (alpha / looks) to an equal-tailed construction; only the wording and certificate were missing.
- E151. Pooled Plan evidence ages by contributor: each report's own clock first, demoted reports leave before pooling, the complete surviving partition is re-tested, and the partition stage is its most advanced contributor's; contributors, exclusions and stages are published. Implemented, including the case where expiry leaves fewer than two reports (pooled evidence becomes diagnostic).
- E152. The cost-removal arithmetic is typed by basis (A, m, P = A/m; removal before division; each scored only on its own basis' anchors; fallback rows take the API cost); the 100/20/4 fixture. Verified: the implementation already divided after subtracting; the fixture now guards it.
- E153. Dispersion boundary cases: insufficient panel, no eligible leaves and zero dispersion are distinct statuses with no drift flag; the normalised weighted spread and the covariance allocation (E81), required by the draft but not yet computed, are now implemented on the common complete panel.

## Reviewer 44 (GPT-6.1 Sol, round 8, Thinking) — adopted
- All findings (E150–E153).

## Editor decisions after reviewer 45 (owner may override)
- E154. Joint rounding law: compiled constraint components of rounded records with registered joint-law objects; singletons keep independent kernels; derived quantities from drawn primitives (the basket cost is now the exact part plus each rounded component's own draw — previously one uniform on the summed interval, harmless only while at most one rounded component entered); affine-linked components use a registered polytope convention and exact sampler, otherwise bounds and "joint rounding law not evaluated". Verified: v1 admitted costs are unrounded at source, so all v1 components are singletons and aggregates are validation identities only.
- E155. Benchmark repeatability and fitted-parameter uncertainty are stated as outside v1 scenario shares (the contradictory "reported through the scenario shares" and Bug Hunt "enters the scenario shares" sentences are replaced); uncertainty descriptions come from the stream manifests (the scenario file now carries them and the not-quantified list); a release-text lint is required for the docs build.

## Reviewer 45 (Claude Sonnet 5.5, round 8, Thinking) — adopted
- All findings (E154–E155).

## Editor decisions after reviewer 46 (owner may override)
- E156. Bar-selection policy object recorded with the anchor version and published in the scores (policy ID and version, mode, cutoff, population rule, order, lower median, empty-population rule, lifetime, population, reference IDs); the population now excludes provisional rows (no current effect: both definite-frontier rows are non-provisional, so gpt-6-luna stays the reference and the re-freeze left every anchor unchanged). Answers Grok Q1 without escalation: bars stay stable within an anchor version and are re-selected only at a versioned re-freeze, the same lifecycle as the anchors themselves (O12 migrations), which the implementation already followed.

## Reviewer 46 (Grok 4.7, round 8, Thinking) — adopted
- All findings (E156).

## Editor decisions after reviewer 47 (owner may override)
- E157. Tariff-aware valuation contract (valuation_sufficiency, billing_rule_id, tariff_allocation_support): AA's category-linear valuation is reconcilable from category totals; a banded provider tariff needs band-allocated demand or a request ledger, otherwise tariff-corrected valuation and dependent transport stay unidentified and the displayed AA cost is kept with its caveat. Implemented per row (Claude Haiku 5.5 carries the banded-tariff status from AA's own caveat; other rows "not recorded").
- E158. Cost boundary: the headline cost is labelled contestant-model API token cost for the basket, not operating cost; per-component boundary matrix with documented exclusions only (verified on AA's methodology page 2026-10-19: AA prices provider-reported token counts; GDP.pdf excludes judge calls, PDF preparation and OCR); no synthetic operating-cost total. Answers Kimi Q1 without escalation: AGENTS.md defines token efficiency as AA's total cost to run the benchmarks, so the claim is limited to contestant-model token spend; extending it would need a new owner decision.
- E159. Evidence bundle: hashes, capture times and extractors of every input artifact plus the anchor object, a bundle hash, and per-observation artifact locators with the published value; rebuild from the bundle without live pages (already enforced by verify:docs in CI). Answers Kimi Q2 without escalation: the repository already commits the captured payloads and rebuilds offline; the hashes and locators make that auditable per observation.

## Reviewer 47 (Kimi K3, round 8, Thinking) — adopted
- All findings (E157–E159).

## Editor decisions after reviewer 48 (owner may override)
- E160. Anchor-panel policy object recorded with the anchors: complete-cost-evidence configurations on every workload component (the admission reference panel on the main workload), Plan anchors from the same configurations at their displayed Plan cost including transfers and API fallbacks, minimum two references (unavailable subset anchors leave those rows unscored; the main workload must meet it), frozen IDs and costs, a rule or population change is a new anchor version. Verified: the re-freeze changed no anchor (16 references on the main workload, 19 on the subset). Answers GLM Q1 without escalation: O13 and O16 score fallback and transfer rows in the Plan table, and the clip gate would hold a release whose Plan anchors excluded them.
- E161. Stream events name their quality equation and event label (S0 observed-only score frontier; S1 and S2 full-composite frontier); S0-to-S1 differences are reported as a change of target plus identification draws; the scenario file and decision signatures carry the fields.

## Reviewer 48 (GLM 5.3, round 8, Thinking) — adopted
- All findings (E160–E161). The first submission of this prompt (130,745 characters) was silently not accepted by Perplexity's composer; the draft's revision-history paragraph and the brief's index were condensed (124,938 characters) and the review was rerun.

## Editor decision after the editor's own verification (owner may override)
- E162. Expected-performance stream S1M: tbench.ai documents its ± as a 95% confidence interval (accuracy_ci95_half_width, with n_trials; verified on the leaderboard page 2026-10-19), so "none in v1" (E145, E155) was wrong for Terminal-Bench, and O25 says published confidence intervals are reported through scenario shares. S1M = S1 plus that interval as an interval-only expected-performance input (uniform with arcsine alternative, clipped); other leaves publish no interval (Bug Hunt's owner publishes run means and counts only); S1M never authorises labels. Implemented and published beside S1.

## Editor decision after the docs rewrite (owner may override)
- E163. Cohort statement corrected. The draft said "19 families now"; the data show 10 frontier or near-frontier families (7 on the rendered frontier, 3 near it) plus 9 configurations retained from earlier releases for exact DeepSWE and Bug Hunt evidence (GPT-5.6 Sol, GPT-6 Sol, Grok 4.7, Gemini 3.8 Flash, Claude Opus 5, GLM-5.3, DeepSeek V4 Flash, Qwen3.8 Max, DeepSeek V4 Pro; inclusion reasons are recorded per row in scores.json). The status quo is kept and stated (claim scope and Cohort), each row publishes its inclusion route, and narrowing the cohort to frontier and near-frontier families is left to the owner as a versioned migration.

## Editor decisions after reviewer 49 (owner may override)
- E164. Measured-evidence calibration diagnostic for the measured-only Plan view: the official Plan anchors include owner-named transfers and API-cost fallbacks (E160), so assumptions can reorder measured-only rows through the exchange rate (V_i − V_j = 25·ln(C_j/C_i)/ln(c_H/c_L) + 0.75·ΔQ, verified). Each workload's measured-only rows with complete cost evidence form measured anchors (min/2, max×2; unavailable below two references); rows, routes, costs and quality are held fixed; both anchor objects and exchange rates, rank changes, pairwise reversals, the largest value change and the provenance of each official anchor extreme are published. Not a second ranking; never validates M_W. Current result: main workload measured anchors $58.84–$339.19 (ratio 5.8 against the official 5404.5, whose extremes are Claude Haiku 5.5 via an owner-named transfer and Grok 4.7 via API-cost fallback); Claude Opus 5.5 and GPT-6.1 Sol swap order (largest value change 2.82 points); the subset workload has one measured row (unavailable).
- E165. S1M interpretation contract: a confidence interval is not a distribution and Terminal-Bench's captured documentation does not establish the interval's estimand, method, sampling unit or treatment of repeated trials, so S1M is a conventional range sensitivity inside the interval (no tail mass) labelled "conventional CI-range sensitivity (endpoint-conditioned; no tail model)"; "expected-performance uncertainty" is permitted only for a source-derived kernel with all four documented. The S1M kernel target is renamed "published-interval range (conventional)" (S1M's allowlist no longer admits "expected performance"), the contract is published with the scenario outputs, and the not-quantified list is aligned.

## Reviewer 49 (Gemini 3.8 Flash, round 8, Thinking) — adopted
- M1 (E165) and M2 (E164). Delivery changed: Perplexity's weekly file-upload limit now blocks long pastes (they become paste.txt uploads) and typed queries are capped at 40,000 characters; its GitHub connector truncates a file after about 27,900 characters (Gemini refused a first, truncated read of the whole file). Drafts are therefore read from the public repository at a pinned commit as parts of at most 20,000 characters (review-input/), with the condensed ledger inline, and every review must open with a read check (the draft's first line and the last 12 words of each part); Gemini's matched all seven parts.

## Round 9 (draft r49, read from review-input/ at commit 9a89e37)
- Reviewer 50 (GPT-6.1 Sol, Thinking): VERDICT: NO FURTHER FEEDBACK. Read check passed (first line and each part's last 12 words; part 5's first quoted word reads "Q." for "i." in both this and the next review, a rendering artifact of that formula line, with the other eleven words exact).
- Reviewer 51 (Claude Sonnet 5.5, Thinking): VERDICT: NO FURTHER FEEDBACK. Read check passed.
- Reviewer 52 (Grok 4.7, Thinking): VERDICT: NO FURTHER FEEDBACK. Read check passed (part 5 quoted from its 11th-to-last word).
- Reviewer 53 (Kimi K3, Thinking): VERDICT: NO FURTHER FEEDBACK. Read check passed (raw-URL fetches failed; the connector parts were used).
- Reviewer 54 (GLM 5.3, Thinking): VERDICT: NO FURTHER FEEDBACK. Read check passed.

## Implementation audit against r49 (editor, while round 9 ran)
- E155 release-text lint was specified but not implemented: added (scenarios.lint_release_text); the Markdown emitter refuses to publish a sentence that puts a source interval or run range into scenario shares unless it names an admitting stream (S1M, for intervals) or states the target is outside the shares. The published documents pass.
- E134 and E154 guards were specified but not explicit: kernels now record their parameter derivation and S0 rejects one derived only from an analyst convention; rounded cost records are compiled into components under the sampling identities (none in v1) and a multi-record component without a registered joint law fails the build. No output changes (every admitted basket cost is unrounded; the scenario file records the joint-law registry).

## Editor decisions after reviewer 55 (owner may override)
- E166. Typed Plan amount: Governance required every Plan row to publish "full-utilisation capacity M × F", but E139 admits measurements whose capacity is not established, transfers are assumptions and the multiple's denominator is gross cash (verified in r49). Each Plan row now publishes the fee period, subscription and declared additional cash (F_gross) and the selected multiple's amount M × F_gross with amount_kind generated from the selected measurement object (measured-workload capacity / observed eligible consumption, capacity not established / assumed API-equivalent consumption for an owner-named transfer, donor named / identified target-workload capacity bound to W), the capacity and valuation statuses and a generated interpretation label; API-fallback rows publish none. Implemented in the scores (plan.amount), scores.md, the model pages and the data contract; today the Opus 5.5, GPT-6.1 Sol and GPT-6 Astra routes read measured-workload capacity, every other routed row reads assumed consumption.
- E167. Transfers off is selected-evidence removal: on the Plan basis the primary selected pair stays fixed and a row whose pair is an owner-named transfer is unevaluable in the transfers-off streams (S1 core, S2 core, S1M), listed with its reason and left out of the declared panel before the draws, never reselected or replaced by API cost; reselection is the measured-only view; S0 keeps the displayed record. The engine had run every Plan stream with transfers in (an implementation gap the finding exposed): the core Plan panels now hold 9 rows (7 transfer-dependent rows excluded), and the model pages and scores.md show those streams as unevaluable with the reason.

## Reviewer 55 (Gemini 3.8 Flash, round 9, Thinking) — adopted
- Medium (E166) and Low (E167). The first attempt stopped at Perplexity's tool-call budget after parts 1 and 2 (Gemini stopped as instructed); the retry, with a note to spend tool calls only on the seven parts, passed the read check.

## Editor decisions after reviewer 56 (owner may override)
- E168. Amount lineage: E166 multiplied the selected multiple by the route's recorded cash, which for an identified target-workload multiple under consumption-dependent payment mixes the target solution's multiple with the measurement's cash (verified: measured U = 60 at cash 20, target U* = 100 at cash 50, M_W = 2, product 40 matches neither). Every amount now records amount_target, workload, measurement object, capacity solution, cash object, purchase policy and derivation; M × F reproduces an amount only within one object (the measurement record, or fixed cash for a target solution); a target-workload capacity comes from the capacity solver (or fixed cash) and is otherwise not published. No published amount changes in v1 (no route is identified on the basket, and every recorded numerator equals multiple × fee); raw-data.md lists each amount's lineage.

## Reviewer 56 (GPT-6.1 Sol, round 10, Thinking) — adopted
- H1 (E168). Read check passed.

## Editor decision after reviewer 57 (owner may override)
- E169. Two summaries aligned with their governing definitions (verified in r51): the interval procedure's opening "Θ = per-row input boxes × shared-factor box" now says primitive domains have a box enclosure and Θ is E73's constrained set (a product box replaces it only under a decision-specific equivalence proof); the uncertainty "Measurement" layer is restated as a taxonomy that names only what v1 quantifies (reporting precision in S0, conventional Terminal-Bench CI-range sensitivity in S1M). Wording only; the implementation already certifies against the constraints.

## Reviewer 57 (Claude Sonnet 5.5, round 10, Thinking) — adopted
- Both Low findings (E169). Read check passed.


## Owner decision (2026-10-20, answering Grok 4.7 round 10)
- O29. When a provider's price for a configuration changes after AA valued its cost (or AA has not re-priced it) and the cost cannot be re-priced exactly from public evidence, the release publishes with the row flagged: AA's cost stays at the price AA applied, labelled "AA cost at superseded price" with that price's dates; the row stays ranked but is left out of interval outputs and cost anchors, and its Plan cost uses only a multiple valued on the same price list. Not chosen: holding the release; valuing the whole release at an earlier date. The question said this matches the existing AA cost caveat; the match is publish-and-flag. AA-cost-caveat rows (a band AA's figure omits under an unchanged tariff, E157) were and remain interval-eligible; O29's exclusions apply to prices not in force at the release valuation timestamp.

## Editor decisions after reviewer 58 (owner may override)
- E170. Valuation-basis gate (Grok M1; failure action O29). The release valuation timestamp V is its release cutoff. Every scored cost observation names the basis it was valued on (AA: the per-category prices AA applied, its displayed prices at capture, reconciled p·d = C where category costs are published; Plan: the price records of the measured model line). A join with the price records in force at V gives one outcome: compatible as captured; compatible after evidenced revaluation (exact only for a common factor k across every priced category and band with positive demand, or with E157 band and category demand); or applied price not in force at V (O29). Editor's reading of O29's "left out of interval outputs": the row earns no interval label of its own and competes in others' interval outputs over the hull of its published record and its structural current-tariff bound, so it can block but never enable a label (as provisional rows under E92). Current-tariff bounds are published as diagnostics: C' in [C·min r, C·max r] (C'/C is a demand-weighted mean of the price ratios r) and P' in [P·min r/max r, P·max r/min r] (M'/M is a consumption-weighted mean of the same ratios). The join is keyed by basis ID and the IDs of the price records in force at V, so a changed price record re-runs it with unchanged payloads. Four fixtures. "Release price list" in E93, E106 and E138 now reads "the row's valuation basis (E170)".
- E171. Route-alternative table (Grok L1). The undefined "best-eligible-route ranking" (from r07) is removed. Every admissible route-measurement pair is published with identification class, evidence grade, measurement workload, valuation status, displayed multiple and the displayed Plan value score it would give, comparison tuple, dominance or exclusion reason, and whether its comparison with the selected pair is identified on W. Grok's second owner question is answered from AGENTS.md: the owner's highest-eligible Value Multiple rule is comparator key 3, so no distinct economic selector exists.

## Reviewer 58 (Grok 4.7, round 10, Thinking) — adopted
- M1 (O29, E170) and L1 (E171). Read check passed (raw-URL fetches failed; the connector reads were used). Grok's first owner question went to the owner (O29); the second is answered by E171.

## Editor decisions after reviewer 59 (owner may override)
- E172. Leave-one-component-out cost family (Kimi H1, modified): the E149 cost-deletion object, with both named calculations and E152 basis typing, is registered once per admitted basket unit (the Coding Agent Index is one unit) and published per basis as rank changes on the common panel with each recalibrated exchange rate. With the matched-cost diagnostic (a quality-weighted mix of complete passes) and the E22 expenditure shares, it shows how far the ranking depends on AA's task multiplicities. Analyst-chosen buyer profiles are not registered: no public source supplies alternative multiplicities, and O15 fixes the scored ones. Kimi's first owner question is answered by O15: the scored multiplicities are fixed, and registered deletion branches are diagnostics under existing governance.
- E173. Missing-share disclosure (Kimi H2, partially adopted; O17 unchanged). Each subset row publishes, per missing component, its expenditure share among rows evidenced on both W and W_S (median and range) beside the E10 paired full/subset summary. Verified on 2026-10-17: the Coding Agent Index's share of the full basket is 9%-63%, median 40%, across the 16 full rows; the subset rows are GPT-6 Astra (xhigh), MiMo-V2.6-Pro and MiMo-V2.6-Flash. Premise corrected: a subset row is scored against W_S anchors from the reference configurations evidenced on W_S, so the direction of its subset effect depends on its unobserved share relative to theirs; it is not known to favour the row. E10 already publishes the paired full/subset bridge for every row evidenced on both, which is the empirical calibration asked for. The threshold flag is not adopted (no public basis for the threshold; the row already carries "cross-workload ordering not identified"). Kimi's third question is answered by O17 and E10: positions are kept and the disclosure is presentation.
- E174. GDPval-AA intervals (Kimi M1). The claim "today only Terminal-Bench 4.0 documents one" was wrong. Verified 2026-10-20: AA's methodology fits GDPval-AA v2.1 ratings "to a Crowd-BT model via maximum likelihood estimation" and computes "confidence intervals using the sandwich estimator", and the GDPval-AA leaderboard shows a per-configuration "CI" (e.g. -26/+26 for Claude Opus 5.5 (Max, Default Fallback)) without stating its level. The captured v1 payload carries no GDPval interval (answering Kimi's second question). The registry lists it as "published, not captured" with a capture task; once captured it enters S1M only if its level is documented, otherwise it is published beside the leaf outside every stream. Kimi's "95% CI below ±1 for the Index" was not found on AA's methodology page and is not recorded. "AA Index fields publish no interval" now reads "the captured AA Index fields carry no interval".
- E175. Source dates (Kimi M2). livebench.ai, rendered 2026-10-20, shows "Release 2026-10-14" and "Last updated 18 October 2026" (Kimi's 13 October does not match the page). The draft's "the page publishes no release date" was wrong. The registry now pins each source's displayed release and update dates with the capture date (amends E129). No lint is added.
- E176. Metering and cache provenance (Kimi M3). Verified on AA's methodology page (2026-10-20): AA uses "the token counts reported by each model's API provider where available", with "a canonical-tokenizer fallback" otherwise, and combines token counts "with live measurements of the model's typical cache hit rate" rather than the run's one-off measurement. The registry's "fallback-token treatment" becomes the token metering basis (provider-reported / canonical-tokenizer fallback / not published per configuration, today's state). The cache protocol records its rate provenance (window unpublished). Each release prints its metering mix. Where the basis is published per configuration, rows within a cost factor of 1.10 on different bases carry a comparability caveat. The score bridge gains an "AA cache-rate update" cause (changed cache-read share with unchanged token totals and prices).
- E177. Swing attribution (Kimi L2, modified). The bridge replays the build from the two releases' evidence bundles in the declared order. Per row it publishes each step's change, the order-dependence term and the replay residual. A change is attributed only when the residual is within 1e-6 points and every step carrying more than 5 points names the changed bundle fields or the versioned method or cohort change behind it. Kimi's rule (hold when the residual exceeds 5 points, or when the only label is "decomposition unavailable") is modified: the residual must be numerically zero, and a named benchmark-record update stays attributed (E90), so an AA refit does not hold a release by itself.

## Reviewer 59 (Kimi K3, round 10, Thinking) — adopted or modified
- H1 (E172, modified), H2 (E173, partial), M1 (E174), M2 (E175), M3 (E176), L2 (E177, modified). Read check passed (seven parts at 64bd04f).
- L1 (utilisation ladder, cost at u = 0.25-1 of capacity): not adopted. Owner decision O3 keeps full utilisation and excludes demand scenarios, and E166's typed Plan amount already lets a light user apply their own utilisation.
- No owner question was needed: Kimi's three questions are answered by O15, the captured payload and O17/E10.

## Editor decisions after reviewer 60 (owner may override)
- E174 amended (GLM Medium 1, premise corrected). GLM said AA's methodology states a 95% level, and ties counted as half-wins, for the GDPval-AA intervals. The page's raw text (2026-10-20) shows otherwise. The GDPval-AA v2.1 section says only that ratings are fitted "to a Crowd-BT model via maximum likelihood estimation" with "confidence intervals using the sandwich estimator". The 95% level and the half-win ties belong to the AA-Briefcase section. E174 now quotes both and says documentation counts wherever the source publishes it, which answers GLM's first owner question without the owner. GDPval-AA therefore stays outside S1M until its level is documented.
- E178. Basket-scope quality branch (GLM Medium 2; O10 and O15 unchanged). A registered E146 deletion branch removes the leaves whose benchmarks O15 excludes from the cost basket (AA-Omniscience, HLE, CritPt; 13.3% of nominal quality weight; retained 86.7%). It is published with rank changes and tau_b on the common panel and labelled "quality restricted to the cost basket's scope". Not adopted: GLM's optional value score against total Index cost, which would be a second ranking on the cost basis O15 replaced; usd per Index point stays a diagnostic (O5/O15). GLM's second owner question is not needed: the O10/O15 pairing is the owner's design, and the branch is published either way.
- E179. Selection summary (GLM Medium 3, modified; the owner's highest-eligible rule unchanged). Each row's route-alternative table (E171) states its number of admissible pairs and unidentified pairs. It also states its leave-selected-out choice: the comparator's pick with the selected pair removed, with that pair's displayed multiple and value score. This is the informative part of the proposed jackknife (dropping any other pair leaves the selection unchanged). Not adopted: the "maximum of more than three candidates" flag (arbitrary threshold; the count is published).
- Editorial (GLM Lows): "5/3% each" now reads "1⅔% each (5% split across three leaves)". Known limitations and the Plan-row text now state that the Value Multiple values only the measured workload's API-equivalent consumption, not other plan features.
- Noted, no change: GLM's roadmap (admit independent SWE leaves such as SWE-bench Verified to raise the 20% independent share). Any new leaf enters only through E26 admission as a versioned quality migration, and its weight is an owner decision (O6).

## Reviewer 60 (GLM 5.3, round 10, Thinking) — adopted or modified
- Medium 2 (E178), Medium 3 (E179, modified), both Lows (editorial). Medium 1 was rejected on its premise and E174 was reworded to prevent the confusion. Read check passed. GLM re-executed the draft's numerical fixtures and all verified.

## Editor decisions after reviewer 61 (owner may override)
- E180. Dispersion convention (Gemini High 1, modified). Every cohort SD and variance (within-cohort influence, non-discriminating threshold, drift spreads, covariance allocation) is the population statistic over the declared panel (divisor n), and a panel of fewer than two rows is "undefined (insufficient panel)". Gemini's n-1 estimator is not adopted: the panel is the population being described, not a sample, and the implementation already uses the population statistic. Scenario dispersion (E87) is the population variance over scenarios.
- E177 amended (Gemini High 2). The swing gate compares rows ranked in both releases. New rows are published as "cohort admission (no prior score)" and departed rows as "cohort exit"; this gate holds neither.
- Gemini Medium 1 (editorial). "leave-AA-out is a headline robustness column" contradicted E146. It now reads as a registered branch that is not identifiable at 20% independent weight, with independent-source robustness reported by the E62 matched-panel statistics.
- E181. GDPval-AA logistic sensitivity formula (Gemini Medium 2): z = 100 / (1 + 10^((E_A - E)/400)), with E_A = 1600 (DeepSeek V4.1 Flash (max), AA's pinned anchor, verified on AA's methodology page 2026-10-20) and the conventional Elo scale (AA does not state its scale factor). It is published as rank changes on the common panel. Gemini's owner question (bar reference or Elo anchor) is answered from the draft's own text ("vs the pinned anchor model"): it is AA's scale anchor, not an owner matter. The sensitivity was specified but not implemented; implementation is queued.
- E128 amended (Gemini Medium 3). The unanswered-or-partial share is 0 when A = 1 (h undefined) and (p + a)/T where counts are published.
- E179 amended (Gemini Low 1). With a single admissible pair, the leave-selected-out choice reads "none: the row would fall back to API cost (O13)".
- E182. Asymmetric intervals (Gemini Low 2). When an interval, as published or after domain clipping, is not centred on the published point, the S1M kernel puts half its mass on each side (uniform per side, with an arcsine alternative per side), so the point stays the median. All v1 Terminal-Bench intervals are symmetric and unclipped at current scores.

## Reviewer 61 (Gemini 3.8 Flash, round 10, Thinking) — adopted or modified
- High 1 (E180, modified), High 2 (E177), Medium 1 (editorial), Medium 2 (E181), Medium 3 (E128), Low 1 (E179), Low 2 (E182). The first attempt stopped at Perplexity's tool-call limit after parts 1-2, having spent calls on tool setup and failing raw-URL fetches. The retry dropped the raw URLs and told Gemini to start with part 1; it read all seven parts and passed the read check.

# Round 10 complete (reviewers 56-61). Every panel model returned HAS FEEDBACK on its draft; round 11 starts with GPT-6.1 Sol on draft r56.

# Round 11 (reviewer 62 onward)

## Editor decisions after reviewer 62 (owner may override)
- E183. Competitor universe (GPT High). E170's "block but never enable" rule is now written into the governing predicates. B_W holds the rows whose AA cost is on a price not in force at V. Each enters with the hull of its published record and its current-tariff bound as an outer admissible domain, and on the Plan basis only where its own route is interval-eligible on its basis. Competitors range over U_W = R_W ∪ B_W, while definite and possible frontier membership, K_r membership and confirmed cheapest go to rows of R_W only. A blocker whose domain cannot be built makes the affected claims "unresolved". Six fixtures. The implementation already competed such rows over the hull and withheld their labels; its output now names them as "blockers", separate from the universe.
- E182 amended (GPT Medium). The published point must lie inside the transformed interval, or the build fails. A zero-length side is a point mass at the point (half the mass when the point is an endpoint), a point interval is a point mass, and atoms are published in the kernel object. The implementation validates the point and draws zero-length sides as atoms.

## Reviewer 62 (GPT-6.1 Sol, round 11, Thinking) — adopted
- High (E183) and Medium (E182 amended). Read check passed. The prompt no longer lists raw URLs.

## Editor decision after reviewer 63 (owner may override)
- E184. Anchor availability after the valuation gate (Sonnet High). E160's two-reference minimum, E170's anchor exclusion and O29's no-hold rule are reconciled from existing rules, so the owner is not asked:
  - A reference must pass the gate (outcome 1 or 2) at its freeze.
  - A frozen anchor keeps its references when one later fails the gate (E160: evidence lost after freezing never rebuilds an anchor).
  - A subset workload short of references takes E160's existing unavailable state.
  - A main-workload migration that would be short of references is deferred. The release publishes on the current anchor version and admitted set, and the would-be component stays pending with a stated reason. The release is not held (O29), and old-workload anchors are never relabelled.
  Sonnet's owner question (publish without a ranking, or delay, when no prior anchor exists) needs no answer. The v3 main workload is frozen, so only a migration can lack a prior anchor, and deferral keeps the ranking (the owner's core requirement). Reaching the case at all needs 12 or more of the 13 or more admission-panel rows to fail the gate.

## Reviewer 63 (Claude Sonnet 5.5, round 11, Thinking) — adopted
- High (E184). Read check accepted with a note: part 7's quoted words stop six words before its end ("…of ranked rows jointly"), a counting slip. The review cites part 7's Governance content, and the part is 14,000 characters, far below the connector's truncation point.

## Editor decisions after reviewer 64 (owner may override)
- E185. Bound domain (Grok Medium). The E170 ratio bounds need a strictly positive applied price for every category that can carry demand.
  - A newly priced category (applied price 0, positive price in force at V) makes the bound unavailable, because v1 has no public per-component category demand (E157). Grok's constrained-demand optimisation therefore has nothing to optimise over in v1.
  - A zero price in force gives min r = 0: the API bound starts at 0 and the Plan bound has no finite upper end.
  - In both cases the blocker's domain cannot be built, and the claims it could affect are "unresolved" (E183).
  - Implemented: reconciliation accepts free cache categories, valuation_gate types the bound, blocker_domain refuses unconstructible domains, and interval outputs turn unresolved.
- E184 amended (Grok Low).
  - A workload migration is atomic across bases. Both bases share the workload object and E160's reference configurations (the Plan references are the same configurations at their displayed Plan cost), so availability cannot differ. Grok's owner question (API migrates while Plan stays) therefore cannot arise and needs no owner answer.
  - A first freeze of a new methodology version that cannot anchor its main workload is not published; the previous version stays live (O12). A subset workload takes the unavailable state.
  - Implemented: assemble_for_release defers a gained component when the new workload cannot be anchored, with an "anchor migration (E184)" manifest rule and the deferred components in the output.
- E177 implemented (valuerank/swing_bridge.py). The replay classes are method and clock, price, token use (with the cache-rate label), benchmark record, Plan evidence and cohort. Every evidence document belongs to exactly one class. A replay the current anchors cannot score is a migration governed by its dual-run comparison.

## Reviewer 64 (Grok 4.7, round 11, Thinking) — adopted
- Medium (E185) and Low (E184 amended). Read check passed.

## Reviewer 65 (Kimi K3, round 11, Thinking)
- VERDICT: NO FURTHER FEEDBACK on draft r59. Read check passed (seven parts at 01b3ed8).

## Editor decisions after reviewer 66 (owner may override)
- E186. Blocker safety (GLM High). The scenario draws keep a superseded-price row at its published record, so the scenario-supported label also requires BlockerSafe(i): no blocker can qualify at the bar and be no dearer than the candidate anywhere in its E183 hull domain. Otherwise the frequency is published with "scenario frequency passes; superseded-price blocker unresolved" and no label, and a blocker is never a candidate. Implemented (blocker_safe in bar_labels).
- E185 amended (GLM Medium 1). A category free under both tariffs contributes zero to both valuations and is left out of the ratios. Zero demand is never inferred from zero expenditure at a zero price. The implementation already behaved this way (ratios run over categories with positive Index cost); a fixture now covers it.
- E184 clarified (GLM Medium 2, rejected as proposed). GLM proposed requiring each reference to pass the Plan evidence's valuation check too. That would leave the Plan anchors with no references today (every Plan route is "valuation basis unverified"), and E160 deliberately builds Plan anchors from the same configurations at their displayed Plan cost so that the whole displayed Plan table stays unclipped. Shared eligibility is therefore complete cost evidence plus an E170 outcome of 1 or 2. The Plan evidence's own valuation status governs Plan interval eligibility (E138), never anchor eligibility, and E164's measured-evidence calibration shows the effect. Each freeze and release publishes a row-level anchor-eligibility table (implemented).

## Reviewer 66 (GLM 5.3, round 11, Thinking) — adopted or modified
- High (E186), Medium 1 (E185 amended), Medium 2 (E184 clarified; intersection not adopted). Read check passed at 01b3ed8.

# Process change (owner, 2026-10-20)
- Before each further Perplexity round, the same review runs inside Claude Code: Claude Sonnet 5.5 at Low, Medium, High, XHigh and Max effort, then Claude Opus 5.5 at the same five levels. Each level is repeated until it returns no further feedback, and the feedback is folded into the draft, before the next level starts. The Perplexity multi-AI round resumes only after Opus 5.5 Max has no further feedback. Convergence still requires all six Perplexity panel models to return NO FURTHER FEEDBACK on the same draft. Internal reviews are numbered I1, I2, ….

# Internal review ladder (owner process, 2026-10-20)

## Internal review I1 (Claude Sonnet 5.5, effort low, on r60) — adopted, modified or rejected
- E187 (H1). The retention rule is now stated as implemented in build_scores: a tracked-catalog configuration with both an exact AA DeepSWE result and a matched exact Bug Hunt result is ranked, and leaves when either stops being exact or is withdrawn. So retention is not path-dependent; the draft's "ranked in earlier releases" wording was misleading. Retained rows can set anchor extremes (verified: Grok 4.7, retained, sets the Plan upper anchor on 2026-10-17), so a frontier-families anchor diagnostic now rebuilds each basis's anchors from frontier and near-frontier references and publishes rank changes. Narrowing the cohort stays the open owner question (b).
- E188 (H2). The configuration rule is stated as implemented (frontier.family_selection, build_scores.frontier_tiers):
  - frontier family: highest-Index rendered-frontier point, then lower total cost, then name;
  - near-frontier family: smallest Index gap, then lower cost, then name;
  - the alternatives are published.
- E189 (M1, modified). The SD ratio stays as the flag's statistic (E60, E91, E126). Beside it, the common-workload panel publishes the value-variance allocation Cov(0.25 S_C, V)/Var(V) and Cov(0.75 Q, V)/Var(V), plus the tau of the cost-only and quality-only orderings against the value ordering. On 2026-10-17 the API cost allocation is 80% against an SD ratio of 55%, and the quality-only tau is 0.03: cost decides most of the API ordering, a fact now visible.
- E190 (M2). Frontier and bar outputs are also published on each subset workload over every row with full cost there (today the seven Index SDLC evaluations, all 19 rows). They carry the workload label; the main-workload outputs stay primary, and Plan subset outputs are unevaluable (no identified multiple).
- E191 (M5). Every O- or E-tagged rule is normative wherever it appears. Owner decisions govern editor decisions, and an amending rule governs the rule it amends.
- M4 (editorial). Bug Hunt is published by its maintainer (Bug Hunt Bench, github.com/phuryn/bug-hunt-bench, Product Compass); ValueRank does not run it. "Independent" is defined as executed by a party other than AA. This answers I1's first owner question from the data.
- L1, L2 (editorial). Slider results are sensitivity columns, and headline ranks always use 25%. The bar policy pins one bar in v1.
- E155 caption (from recommendation 3). Each scenario-share table states that it excludes benchmark sampling noise beyond S1M and fitted-rating uncertainty.
- Not adopted:
  - M3, the owner decision challenge to O12. A clip hold is resolved by a versioned re-freeze in the same release cycle, so no entrant is excluded; O12 stands.
  - The S1T task-resampling stream. A binomial task model is an analyst assumption without a documented estimand (E145, E155).
  - The bar ladder. More bars change the registered bar policy (E156); this is noted as a possible owner question.

## Internal review I2 (Claude Sonnet 5.5, effort low, on r61) — adopted, modified or rejected
- E192 (H1, adopted). The bar was tautological. v1 pinned a non-provisional API definite-frontier configuration r. Any other row confirmed cheapest at r's quality would have to dominate r in every θ, contradicting r's definite membership, and a 90% scenario share contradicts it the same way. Verified on the build: the 2026-10-19 freeze pinned GPT-6 Luna (max), and the API output was "GPT-6 Luna (max), confirmed".
  - The bar is now a quality level, policy "median-quality-level" v2: the lower-median displayed quality of the non-provisional ranked configurations, frozen with the anchor version (2026-10-19: 16 configurations, Q̄ = 52.09, GLM-5.3's displayed quality).
  - Fewer than two population configurations pin no bar; with two or more, at least two reach Q̄ at freeze (non-tautology).
  - The reference object is the constant level on both bases and every workload. The median configuration has no special role, and kernel checks run over candidate and competitor groups (an empty reference group takes no letter).
  - A pre-release correction: no v3 release was published, so data/v3_frozen.json's bar fields were migrated in place. A re-freeze on the same evidence reproduced every anchor exactly; only the bar fields changed.
  - Result: API main workload "not unique; possibly GPT-6.1 Sol (max), GPT-5.6 Luna (max), DeepSeek V4 Flash (max), DeepSeek V4 Pro (max)". No scenario label (frequency ranges 15–39%).
  - Taken as an editor decision rather than I2's Q3 to the owner: O2's "cheapest-above-bar view" is kept, and only its defect is fixed.
- E193 (M1, modified). The configuration rule was misstated: GPT-5.6 Luna is ranked at max, its near point is low, and E188's near rule would pick low.
  - Family = AA model identity: the plotted name without effort and fallback qualifiers, equal to the catalog display name. The MiMo Pro and Flash models are separate frontier families.
  - A frontier family ranks its highest point on the rendered line; along the strictly rising line that is also its dearest, so a rounded-Index tie never decides it.
  - A near family ranks the configuration retention already ranks, else its smallest-gap near point (AGENTS.md: "the family's selected configuration may differ from the near configuration").
  - Built and enforced: build_scores fails when the tracked catalog ranks any other configuration. Verified on all 10 families.
  - Ranking every rendered-frontier point is rejected: AGENTS.md requires one selected configuration per family. Scoring alternatives is rejected too, because their exact-configuration SDLC evidence is not captured; they stay in the reconciliation inventory.
  - The "worse-value point" argument is rejected as a selection rule: choosing the configuration by its score would select on the outcome.
- E194 (M2, adopted). The report window is the 30 days ending on the evidence search cutoff, the registry's reportingWindow (2026-09-08 to 2026-10-08), which is AGENTS.md's "preceding month".
  - A report's date is its measurement window's end, else its report date, else its publication date.
  - A report admitted earlier records admittedOn and ages under E151/O13.
  - The build fails on a newly admitted report dated outside the window. The current Grok 4.7 SuperGrok Heavy report, 2026-09-25, passes.
  - I2's alternative, letting O13's 90 days replace the window, would change AGENTS.md policy and is not adopted.
- E195 (M3, modified). Frontier membership extraction is now registered: the rendered Pareto path's vertices matched to circle centres (0.5 px tolerance; on 2026-10-17 all 18 matched at 0 px). The build checks that the points equal the vertices and that the path rises strictly in chart coordinates.
  - I2's proposed "non-dominated in (cost, Index)" check on rounded values is rejected: it would fail on the real capture (GPT-6 Luna (max) and MiMo-V2.6-Flash both display 38), and AGENTS.md forbids recomputing membership from rounded values.
- E196 (L1, adopted as disclosure). The README scope line and lead, and the site's methodology lead, state the 25% weight as nominal with cost's value-variance allocation beside it (80% API, 63% Plan).
  - Recalibrating anchors to equalise influence is not adopted: the weight is owner policy, and the anchors are frozen evidence ranges.
  - Whether "25%" is meant as nominal weight or as influence goes to the owner in the final summary (I2 Q1).
- E197 (L2, adopted). The re-anchoring path is pre-built: `python3 -m valuerank.value_v3 dual-run --previous <old v3_frozen.json>` scores the same evidence on both anchor objects and writes data/v3_dual_run.json, with per-row cost score, value and rank and per-bar results under both versions (O12). The clip clause itself stays (I1 M3).
- M4 (conditional Plan frontier on observed-workload multiples): not adopted.
  - Interval outputs need an identified M_W (E32, E49, O19).
  - The exploratory Plan ranking (O16) and the measured-only Plan view already give Plan buyers scored, flagged results.
- I2 Q2 (one row per family) and Q4 (report window) are answered from AGENTS.md (E193, E194). Q3 is resolved by E192.

## Owner decision (2026-10-21, after internal review I3)
- O30. A near-frontier family ranks its configuration with an exact AA DeepSWE result and a matched exact Bug Hunt result when it has one (several: the highest Index, then the lower cost; today at most one, because Bug Hunt publishes one configuration per model); otherwise its smallest-gap near point. Asked because I3's H1 exposed a live case: GPT-6 Astra was ranked at xhigh (smallest-gap near point; no DeepSWE, Bug Hunt or Terminal-Bench result; 40% coverage, provisional) while GPT-6 Astra (max), also a near point (gap 3), has exact DeepSWE (67.6%), Bug Hunt (45/105, mean of 3), Terminal-Bench 4.0 and Coding Agent Index, FrontierCode and ITBench-AA costs; GPT-5.6 Luna was already ranked at max under the same logic. Not chosen: always the smallest-gap near point (GPT-5.6 Luna would drop to low and lose its evidence); keeping a catalog-dependent roster.
  - Applied: AA's GPT-6 Astra (max) page captured 2026-10-21 (Index 52.67, total cost $5,324.10, matching the chart capture) and swapped into the snapshot with its own capture time; roster, extract, configuration map re-pointed to max; DeepSWE mapping re-run offline on the 2026-10-17 capture (GPT-6 Astra (max) now exact_variant). The build enforces O30 (a near family with both results must rank that effort).
  - Result: GPT-6 Astra (max) has all 11 quality leaves (coverage 100%, not provisional) and full basket cost $6,107.09; Plan rank 10, API rank 14.
  - Pre-release re-freeze (anchor version v3-2026-10-21): 17 anchor references, anchor values unchanged, no rank changes (dual run: dual-run-2026-10-21-o30.json); the bar level moved from 52.09 (GLM-5.3) to 56.70 (Grok 4.7) because the population grew to 17. The release instant was re-stamped to 2026-10-21T05:24:16Z (AA reconciliation passes).
  - Found while checking: the legacy v1 composite used GPT-6 Astra's max-effort Bug Hunt result for the xhigh row (v3 did not). The legacy build now applies the same exact-effort check (exact_bug_hunt).

## Internal review I3 (Claude Sonnet 5.5, effort low, on r62) — adopted, modified or rejected
- H1 (adopted through O30): the precedence is now stated. The tracked catalog holds one configuration per family, so the family rule decides each frontier or near family's configuration and retention can never add a second row.
- E198 (M1, adopted): the non-tautology claim is restated as a property of the bar's construction (at freeze, at least two population configurations reach Q̄ on displayed quality). Every bar result publishes possibleQualifierN, the number of R_W configurations that can possibly qualify, with "comparison vacuous" below two. Today: 11 on the API main workload, 13 on the subset workload. The release-test wording is corrected ("does not force its setter").
- E198 (M2, adopted): the bar is labelled a displayed-quality level whose labels test full-composite bounds, and each bar table gives every row's displayed margin to Q̄.
- E194 clarified (M3): "admitted" means passing the inclusion rules whatever the source count. A sole in-window report can pool later with a newer in-window report while both are inside E151/O13 expiry (45-day fixture). This follows E194's design: the window governs entry and O13 governs retention.
- E198 (M4, adopted as an editor decision; I3 Q3 answered): "valuation basis unverified" is E170's outcome (4). The row is ranked and flagged, anchor- and interval-ineligible, and not a blocker, because no current-tariff hull can be built for it. It is listed as unevaluable, so cohort-extension claims list it as an omitted competitor (E38). No row has this outcome today.
- L1 (fixed): the r62 edit had left a doubled fragment in the bar definition's opening sentence. The Q_r ≡ Q̄ notation is kept, because it is defined.
- L2 (adopted): Outputs states that the Plan frontier and bar outputs are unevaluable today.
- L3 (adopted as disclosure, E198): the 90% rule's bound holds per event and is not corrected across a bar's candidates. The label table says so.
- Not adopted:
  - Recommendation 1 (a claims-supported table): the README's "What the evidence supports" section and the manifest already give each basis's evaluable and unevaluable rows, and E198 adds the qualifier count.
  - Recommendation 2 (sibling diagnostic): siblings cannot have matched Bug Hunt results, because Bug Hunt publishes one configuration per model. Their AA Index and cost are already in the reconciliation inventory.

## Owner decisions (2026-10-21, after internal review I4)
- O31. Retention is checked over every model in AA's selected catalog that has both an exact AA DeepSWE result and a matched exact Bug Hunt result, and the build fails if one is missing from the roster. Asked because I4's H1 showed the retained set was reproducible only from a hand-maintained roster.
  - Verified gap: Claude Fable 5.1 (max), Muse Spark 1.3 (max), Muse Wonder (max) and Muse Wonder Full (max) each had an exact DeepSWE result (2026-10-17 capture) and a Bug Hunt result at the pinned commit aec97617, but were not in the roster.
  - Not chosen: keeping the curated roster; narrowing to the policy cohort.
  - Applied: AA pages for the four were captured 2026-10-21. Bug Hunt runs: Fable 5.1 43/105 (single run); Muse Spark 1.3 32.2 (mean of 5, Meta API); Muse Wonder 31.7 (mean of 3); Muse Wonder Full 42.0 (mean of 2). Superseded and other-effort rows were added to excludedResults. Identity of "Muse Wonder 1.0" with AA's "Muse Wonder" rests on the owner's run notes and AA's release date (2026-10-12).
  - Fable 5.1 takes SemiAnalysis's exact measured Max 5x (12.73×) and Max 20x (12.425×) routes and no Pro route (Fable is unavailable on Pro), replacing the shared Opus 5.5 assumption as AGENTS.md requires once a measurement exists.
  - The Bug Hunt owner's full scoreboard is captured (data/bug_hunt_scoreboard.json, sha256 recorded). It and the roster file are in the evidence bundle, and the build check (unrostered_evidence) now fails on any unrostered DeepSWE configuration with a scoreboard row at the same effort.
  - Results: 23 ranked configurations; 13 retained. Muse Wonder Full has no AA cost, so it has no value score and no rank (shown with quality 67.7). Claude Fable 5.1's AA category costs do not reconcile with its displayed prices (output 98.0% and input 102.3% of AA's token totals at those prices; the per-evaluation costs sum 1.0% above AA's total), so its gate is E170 outcome (4), valuation basis unverified. It is ranked and flagged, and outside interval outputs and anchors.
  - Pre-release re-freeze: anchor values unchanged, 19 references, Q̄ = 58.28 (GPT-6 Sol) over 21 configurations, no rank changes (dual-run-2026-10-21-o31.json).
- O32. Only reports dated in the current 30-day window count toward O11's two-report minimum and concordance; older reports stay visible as diagnostics until they expire. This is AGENTS.md's "preceding month" read strictly. It supersedes r63's "admitted reports keep counting" clarification of E194. Implemented in plan_routes (measurement_objects and route_candidates take the release's window).

## Internal review I4 (Claude Sonnet 5.5, effort low, on r63) — adopted, modified or rejected
- H1 → O31.
- H2 (adopted as E199): the frontier-families diagnostic also recomputes the bar over frontier and near-frontier configurations and publishes the cheapest-above-the-bar result at that level (today quality 60.9 over 8 configurations; GPT-6.1 Sol (max) confirmed cheapest). The frozen bar stays primary. I3 Q2 (making the policy-cohort bar primary) would challenge E163 and was not put to the owner, because the sensitivity answers it.
- Found while implementing H2: build_scores never passed the frontier-family flag to the v3 engine, so the E187 diagnostic had used every row (19 references). It now uses 8. With retained rows excluded, the Plan upper anchor is $7,257 rather than the frozen $13,400. Fixed with a shared value_v3.configuration helper.
- M1 (modified, E200): the premise is wrong. Coding and terminal tasks (Coding Agent Index, Terminal-Bench 4.0, SciCode) carry a median 56% of basket cost (35% to 74% over 19 full-basket rows), not a minority. The share is now printed beside the basket label. The Owner decision challenge to O15's composition is not adopted. The c_SWE standing column is not adopted (O14 keeps c_SWE diagnostic).
- M2 → O32.
- M3 (adopted as E200 text): a held release is still built; its manifest names each clipped row with its unclipped values and the flag "off-anchor scale, release held", and that output is published with the clearing dual run.
- L1 (adopted): the influence example is marked illustrative and generated each release.
- L2 (adopted): the frontier versus near asymmetry is stated as intentional.
- Also fixed (AGENTS.md "a configuration without a cost gets no value score"):
  - The legacy composite's blend() scored a cost-less row on quality alone. Muse Wonder Full would have been legacy rank 1. It now gets no overall score (rankingStatus "unranked_no_cost").
  - The changelog and README handle rows without a rank.
- README flags gain "valuation basis unverified" and "no cost".

- Follow-up fixes (test update run): scores.md printed "None" for a missing rank (now a dash, workload a dash for a no-cost row); short_flags now follow the legend order; README scope reads "23 cohort configurations (22 with a value score)"; the site flags a no-cost row "No cost" instead of "Subset cost"; the O31 roster check accepts only a version-number suffix, so "Muse Wonder Full 1.0" cannot be read as a version of "Muse Wonder".

## Internal review I5 (Claude Sonnet 5.5, effort low, on r64) — adopted, modified or rejected
- H1 (adopted): r64 still had r63's sentence letting earlier-admitted reports age under E151/O13, which contradicts O32. It is removed, and the parenthesis is repaired.
  - Under O32, each release rebuilds report partitions from in-window reports only, so a report-based route lapses without fresh reports.
  - E151/O13 clocks govern controlled measurements and transfers.
  - A transfer whose donor is a report partition follows the donor's O32 status (implemented in route_candidates, with a test). Report dates are computed one way everywhere (report_stage uses report_date).
  - I5 Q1 is answered by O32.
- M1 (adopted, E201): a counted report whose measurement window starts before the report window is flagged window-straddling (windowStraddlingReportIds). Where a report isolates per-period figures, the registry records only the in-window periods and the multiple recomputed from them, as an editorial step.
- M2 (modified, E201): the observation is right. Confirmed qualification uses the full-composite lower bound with missing leaves at 0, so confirmed labels in practice go to full-coverage rows. This is O25's published-record target, not a hidden rule, so I5 Q2 is answered by O25. Each result now publishes confirmedQualifierN beside possibleQualifierN (today 5 against 12).
- M3 (adopted): "Bug Hunt publishes one configuration per model" was false. The scoreboard has five efforts with both results for GPT-6.1 Sol, Claude Haiku 5.5 and Claude Sonnet 5.5, and two for Muse Spark 1.3. The build now:
  - orders evidenced efforts from the full scoreboard and AA's chart points (highest Index, then the lower cost);
  - enforces this for every non-frontier roster model, ranked or not.
  - Found by the new test: a roster model tracked at an effort without both results had silently dropped out of the cohort. No current model does.
- M4 (adopted): the "cohort" (23) and the "scored" rows (22) are defined. N for ⌈2N/3⌉ counts every cohort row. The bar population counts every non-provisional cohort row with a displayed quality. W_S covers 21 of 23 rows (the stale "19" is corrected).
- M5 (adopted): the cost boundary now says AA prices provider-reported counts or its canonical-tokenizer fallback (basis not published per configuration; E176).
- M6 (adopted, E201): each possibly-cheapest row lists the same-family configurations AA plots at a lower total Index cost; they are not evaluated because one configuration per family is ranked. Today: GPT-6.1 Sol's four lower efforts and DeepSeek V4 Flash (high). The chart capture is now in the evidence bundle.
- M7 (adopted): SemiAnalysis results are labelled controlled subscription-account measurements with workload projections in O11's text; the site's route label already says so.
- L1, L2 and L5 (adopted): F(c) is undefined left of the first frontier point (no near status there); "lower median" means the ⌈n/2⌉-th ascending value; the family key strips the trailing parenthesised qualifier and must equal the catalog display name.
- L4 (adopted): see H1.
- Not adopted:
  - L3 (identifier collisions): an E-number names an editor decision record that may cover several items and later amendments. The record makes each one traceable.
  - Recommendation 2 (dormant appendix): editorial restructuring with no change in behaviour; the dormant definitions already have executable tests.
  - Recommendation 4 (harness for the numeric fixtures): the test suite already asserts them.
