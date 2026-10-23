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

## Owner decisions (2026-10-21, after internal review I6)
- O33. Every evidenced effort is ranked as its own row. A configuration in AA's catalog with an exact AA DeepSWE result and a matched exact Bug Hunt result is ranked, even when another effort of the same model is already ranked. This supersedes the one-configuration-per-family part of E193 and O30. The frontier and near rules still decide which configuration carries the frontier or near inclusion reason. Asked because I6's H1 showed that the stated reason for not evaluating siblings (missing evidence) was false for GPT-6.1 Sol, Claude Haiku 5.5 and Claude Sonnet 5.5 (both results at five efforts each) and for Muse Spark 1.3 (two). Not chosen: unranked diagnostic rows; listing only. Implementation follows in r66.
- O34. The cheapest-above-the-bar output publishes a quartile ladder. The levels are the lower quartile, the lower median (the headline bar) and the upper quartile of the non-provisional cohort's displayed quality, each at zero-based position floor((n − 1)k/4), frozen with the anchor version. Bar policy "quality-quartile-ladder" v3. Implemented: pre-release re-freeze (anchors unchanged); today's levels are 50.0 (GPT-5.6 Luna), 58.3 (GPT-6 Sol) and 61.3 (GPT-6.1 Sol). Not chosen: the single median bar.

## O33 implementation (2026-10-21)
- Added 14 configurations as their own rows: GPT-6.1 Sol (xhigh, high, medium, low), Claude Haiku 5.5 (max, high, medium, low), Claude Sonnet 5.5 (xhigh, high, medium, low), Muse Spark 1.3 (xhigh), and Grok 4.6 (xhigh).
  - Grok 4.6 (xhigh) was found because the scoreboard parser now also reads a bare effort ("(xhigh) seq").
  - Each has its AA page captured on 2026-10-21 (Index and cost match the chart capture), an exact DeepSWE row, and a Bug Hunt record on the owner's largest-sample mean for its own effort and route.
  - Spot-checked against the pinned scoreboard: GPT-6.1 Sol (xhigh) 42.7 (mean of 3), Claude Haiku 5.5 (medium) 12 (single run), Claude Sonnet 5.5 (low) 19.0 (mean of 3), Muse Spark 1.3 (xhigh) 20.3, Grok 4.6 (xhigh) 28.7.
- Sibling rows are named "Family (effort)". Only the family's primary row carries the frontier or near inclusion reason; a sibling shows the tier of its own plotted point.
- The build:
  - fails on any evidenced configuration missing from the roster;
  - fails on any rostered evidenced configuration without its matched Bug Hunt record;
  - no longer checks a single retained effort per family, which O33 supersedes.
  - E201 now lists only unranked cheaper siblings.
- Plan routes: GPT-6.1 Sol siblings join the owner-named ChatGPT common-assumption routes, graded as assumptions because SemiAnalysis names GPT-6.1 Sol without an effort. Claude siblings join the shared Claude assumption routes. Muse Spark 1.3 (xhigh) and Grok 4.6 (xhigh) fall back to API cost.
- Pre-release re-freeze under the same anchor version: 33 references; low anchors API $66.43 → $35.76 and Plan $2.48 → $0.61; high anchors unchanged; ladder 48.06 / 56.70 / 60.88 over 35 configurations.
  - The dual run (old against new anchors) moved 27 rows on at least one basis.
  - GPT-6.1 Sol (xhigh) now leads both bases (API 60.6, Plan 60.9).
  - Cost's share of value variance: API 82% → 47%, Plan 64% → 61%.
  - Cohort 37, scored 36, roster 49.
- Also fixed (AGENTS.md exact variants):
  - The legacy composite now takes a Terminal-Bench row only at the configuration's own effort. Claude Opus 5 (max) had been given Opus 5 (xhigh)'s 0.539, and Grok 4.6 (medium) the high row's value.
  - The unranked grok-4.6 (medium) record no longer holds the xhigh Bug Hunt run, which belongs to grok-4.6-xhigh.
- Open, recorded for the owner summary:
  - GPT-6.1 Sol (max)'s ChatGPT route is graded measured although SemiAnalysis states no effort (pre-existing).
  - Several sibling Bug Hunt values rest on one or two runs (Haiku medium and low single runs; GPT-6.1 Sol low runs 31 and 14).

## Internal review I6 (Claude Sonnet 5.5, effort low, on r65) — adopted, modified or rejected
- H1 → O33 (owner). Its (a) is moot: evidenced siblings are now ranked, and E201 lists only unranked cheaper siblings, for the right reason.
- Recommendation 2 (several bars) → O34 (owner).
- M1 (adopted): cohort, scored and bar-population rows are defined once (37, 36 and 35 today), and "ranked rows" elsewhere means cohort rows.
- M2 (adopted): every near point publishes its cost ratio to the frontier for information only (it never gates inclusion), and a near family is deferred only by a dated, reasoned roster decision kept in the reconciliation inventory.
- L1 (adopted): E184's panel sizes are stated for both freezes.
- L2 (adopted): the "non-tautology" sentence now names the property that matters (a level is never a configuration).
- Recommendation 3 (one counts object beside the headline): partly met by the README scope line (cohort and scored counts); not adopted further.

## Internal review I7 (Claude Sonnet 5.5, effort low, on r66) — adopted, modified or rejected
- H1 (adopted): the bar policy now states the O34 positions, zero-based floor((n − 1)k/4) for k = 1, 2, 3, as elements of the order (never interpolated), frozen together, all unavailable when n < 2, published in the order k = 2, 1, 3, with the fixture n = 35 → 9th, 18th and 26th ascending values. "v2 pins one bar" is replaced by policy version 3. The reviewer's owner question (elements or interpolated percentiles) is already settled by O34's option text; not re-asked.
- M1 (adopted): "21 of the 23 cohort rows" → "35 of the 37". The proposed prose-count lint is not adopted; the README's counts are generated, and the draft is regenerated from the ledger at each re-freeze.
- M2 (adopted, modified): the valuation outcome (4) becomes E202. E191 now says an E number names one decision record, a record holding several rules labels them, and an amendment cites the record it amends. The other reuses the reviewer lists (E177, E182, E184) are records with several labelled rules or later amendments; not renumbered.
- M3 (adopted as E203): each bar and basis publishes the displayed-record cheapest row (lowest-cost scored, non-provisional main-workload row whose displayed quality reaches the bar, ties listed, count of rows reaching it), labelled "displayed record on the headline scale, not a claim". Implemented in `value_v3.displayed_cheapest` and printed in the README. Today API headline: GPT-6.1 Sol (medium), $531.56, 17 rows reach it.
- L1 (adopted): the brief's coding share is now 53% over 33 rows.
- L2 (adopted, E203): the summary prints the median basket share carried by admitted components with no quality leaf (AA-Briefcase, GDP.pdf; 15%). ITBench-AA is not admitted, so it is not in the share. No score changes (O6, O15).

## Internal review I8 (Claude Sonnet 5.5, effort low, on r67) — adopted, modified or rejected
- M1 (adopted as E204; new argument beyond I5 L1): the draft assumed AA's line starts at the cheapest plotted point. The build now stops, naming the point, when any plotted point lies left of the path's first vertex (chart x, 0.5 px tolerance), until the owner records a dated, reasoned decision for it. Today none does (GPT-6 Luna (low), $10.63, is the cheapest of 189 points). The reviewer's Q2 (include or exclude such a point) becomes an owner question only if the check ever fires; not asked now.
- M2 (adopted as E206): the Bug Hunt record selection is now executable. Key: roster name (version suffix only), exact effort token or documented single-mode equivalent, harness and route. Rule: the owner's largest-sample published mean at that name and effort over every harness and route, unless the record states a selection reason. `check_bug_hunt_selection` verifies every matched record against the pinned scoreboard; all pass today (Gemini 4 Argon high: Antigravity CLI mean of 3 over the single Gemini CLI run). Records read from run notes under names the scoreboard does not label with an effort keep their recorded effort status. No effort-synonym table: tokens match exactly, by AGENTS.md.
- M3 (adopted, modified, as E205): a one-row-per-family diagnostic recomputes the ladder and anchors from each family's primary row (frontier or near configuration; for retention-only families the highest-Index evidenced effort, then the lower cost) and publishes exchange rates and rank changes on both bases. Influence statistics are not recomputed (the exchange rate and rank changes carry the effect). Today: 24 families, 22 bar-population rows, ladder 58.3 / 50.0 / 60.9 against 56.7 / 48.1 / 60.9; API exchange rate 3.04 against 2.74 (23 rows move, largest 6), Plan 2.02 against 1.73 (16 rows, largest 4).
- M4 / R2 (rejected): a "confirmed among full-coverage rows" label would make the claim's universe depend on which leaves benchmark publishers happened to run, and readers would take it for a cohort-wide claim. O25 makes the interval outputs over the cohort the claim; E201 publishes confirmedQualifierN, E38 lists omitted competitors, and E203 gives the displayed record.
- L1 (adopted): "the v2 frozen level" → "a frozen bar level" in the E50 note.
- L2 / Q1 (rejected, already decided): E98 fixes the operational form of O11's ±20% with the same 80/120 fixture; the reviewer adds no new argument.
- L3 (rejected): E74 already publishes the joint intervals and the upper-bound rank sensitivity, which shows any rank an L-bound row loses against an unidentified one; nothing is identified today.
- L4 / R5 (rejected): `methodology.md` is the published short methodology; the draft is the normative record with its decision trail, by design.

## Owner decision (2026-10-21, after internal review I9)
- O35. Fable 5.1 is not a donor-error gauge. Asked whether to publish a diagnostic rescoring the transfer-dependent Claude Plan rows with Fable 5.1's measured Max multiples (12.4–12.7x against Opus 5.5's 57–59x), the owner answered: "Fable use is indeed much limited in Claude." The gap reflects Fable's own tighter allowance, so it does not measure how far the Opus 5.5 transfers could miss for other Claude models. No such diagnostic is published; the transfers keep their assumption label and the AGENTS.md caution.

## Internal review I9 (Claude Sonnet 5.5, effort low, on r68) — adopted, modified or rejected
- M1 (adopted as E209; the reviewer's diagnosis corrected): the code already treats the seven Index components as "unresolved" when AA's ten evaluation costs do not reproduce its published Index total (`basket.index_components`, relative error at most 10⁻⁶). Claude Fable 5.1 fails that test ($13,259.52 against $13,128.86, 1.0%), which is why it is outside P_K. The draft wrongly gave the E170 valuation outcome as the reason. E37's definition now includes the reconstruction test; one status scale (confirmed complete, unresolved, confirmed incomplete, missing) defines K_ie; anchor eligibility is K plus an E170 outcome of 1 or 2, two separate tests. Fable fails both, so the admission panel and the anchor references are both 33 rows.
- M2 (adopted as E208): the token-mix test compares against the nearest point of the basket's own demand region (E124), never AA's Index-wide shares. Implemented: each route inherits its source's published mix (SemiAnalysis reports a cache-heavy mix) and carries a mix status; with the region set-identified and no cache split, the status is "mix unidentified" (23 selected routes) or "mix not reported" (2). The L1 computation itself waits for an identified share vector.
- M3 (adopted as E207, informational): each release publishes every frozen bar's reach in the current population and the ladder the current population would freeze, with a flag when the headline bar leaves the current interquartile range. Lifetime registered: until the next anchor re-freeze or methodology version. Q2 (flag or hold) is an editor default, not an owner question: a hold would gate releases on a sensitivity, which no other diagnostic does.
- M4 / Q1 → O35 (owner): no Fable-based donor-error diagnostic.
- L1 (adopted): E201's three rules are labelled E201a (window-straddling reports), E201b (label reach) and E201c (unevaluated cheaper siblings).
- L2 (adopted, modified): the E151 note now says that under O32 a report partition reaches the 90-day expiry only through a report whose measurement window ended long before its report date and could not be split (E201a); otherwise only "possibly superseded" is reachable for reports. The branches stay, because that case is reachable.
- L3 (adopted): the bar population is defined over "non-provisional cohort rows".

## Internal review I10 (Claude Sonnet 5.5, effort low, on r69) — adopted, modified or rejected
- H1 (adopted as E211, already implemented): the refresh gate (`aa_reconciliation.MAX_AGE_DAYS = 7`) already fails on a capture more than 7 days old at the release clock and on any near family neither rostered nor deferred by a dated, reasoned decision; the capture already carries the vertex entrant/exit diff. The draft now states all three. Q2 (maximum age) is answered by the existing 7-day gate, so it was not put to the owner.
- M1 (adopted as E212): one lifecycle table (current, possibly superseded, expired in grace, demoted) with trigger, official score, comparison, interval eligibility and label, matching `plan_routes.expiry_status` and `plan_boxes`. The reviewer's reading that the soft stage is event-only is corrected: it is age over 30 days or a detected change. "Triggers the 30-day soft expiry" → "moves the route to the possibly-superseded stage".
- M2 (adopted, modified): the stale "exactly … < 0.002%" is replaced. The proposed propagated-rounding tolerance is rejected: AA's page fields are unrounded floats (every cohort row except Fable reproduces its total within about 2 × 10⁻¹⁶), and the reviewer's $10.63 example is a rounded chart tooltip, which the reconciliation does not use. E37 now lists the four statuses.
- M3 (adopted): the report-window rules (E194, O32, E201a) and their fixtures are lifted out of the inclusion-rules parenthesis into their own paragraph.
- L1 (adopted): the leaf table's anchors are the frozen ones; the chance/ceiling rule sets anchors for a new leaf.
- L2 (adopted): the bar level is renamed H (H_k for the ladder; H = H_2 the headline) so it is not confused with a row's displayed quality Q̄_i.
- R1 / Q1 (adopted as E210, inactive today): the category-mix bound M_W ∈ M_obs × [ρ_min/ρ_max, ρ_max/ρ_min] follows from the draft's additive capacity model and is a structural bound under O19, so no owner question is needed. It set-identifies M_W only when the demand region bounds every ρ_k away from 0 and ∞, never for a transfer. Today it is inactive because AA publishes no cache split for the basket and SemiAnalysis's measured mix is 96.6% cache reads. It is not implemented in code until it can bind; the mix status (E208) already reports the region as set-identified.
- R2, R3: covered by E211 and E212.

## Internal review I11 (Claude Sonnet 5.5, effort low, on r70) — adopted, modified or rejected
- M3 (adopted as E213; a real defect): the registry's report window ended on the evidence search cutoff (2026-10-08), 13 days before the release cutoff, while every other gate read the release clock. One release cutoff (the valuation timestamp V) now governs the report window, the evidence stages, the capture age and the valuation gate; `assemble` fails when the window does not end on it. The window is now 2026-09-21 to 2026-10-21. The search cutoff is recorded apart (`evidencePolicy.searchCutoff`), and the summary states that reports dated after it were not searched. No score changes: the one report route (SuperGrok Heavy, 2026-09-25) is in both windows.
- M1 (adopted as E214, modified): AA plots every Claude configuration only "with fallback" (16 points, no twin without it), so a fallback-silent third-party record matches by model and effort. The build now fails if AA ever plots the same model and effort both ways, until a dated matching decision. Q2 becomes an owner question only then.
- M2 (adopted): the unrewarded-share disclosure adds SWE-Atlas QnA (124 of the Coding Agent Index's 303 tasks), which has no quality leaf; its cost share is published as not separable, because AA's capture gives one pooled index cost and no per-sub-benchmark cost.
- M4 (adopted): "observed SWE nominal weight ≥ 40 of the 100 quality points", matching `quality.MIN_SWE_WEIGHT`; DeepSWE (30) plus one other SWE leaf (10) is the minimum.
- L1 (adopted as E215): quartile bars are pinned only from four configurations, when the three positions are distinct; with two or three, only the headline bar.
- L2 (adopted): the 17 vs 18 difference is explained (Muse Wonder Full reaches the headline bar on displayed quality but has no AA cost); E205's population is labelled "one-row-per-family bar population".
- L3 (adopted, modified): E198's two rules are labelled E198a (counts) and E198b (displayed-level test). E184 and E177 each name one rule in the draft (the swing gate cites E177's attribution, not a second rule); not relabelled.
- R1 (rejected): Bug Hunt run counts are already published per row (scores.md, "Runs"), and the leave-one-benchmark-out deletion sensitivity (E146) shows rank changes without Bug Hunt; a per-label flag adds nothing a reader cannot see there.
- R2 (rejected): the README scope line and the counts paragraph already give cohort and scored counts, and E199/E205 isolate the retained rows' effect on the bar and the anchors.
- Q1 (answered from the record, not put to the owner): every cross-model route carries its dated authorisation in `plan_cost_routes.json`: the common ChatGPT routes ("User-selected SemiAnalysis October 7, 2026", valid from 2026-10-08), MiMo's provisional 1.5× ("User instruction in this chat on October 8, 2026"; numerator kind "unavailable", so no provider figure is used) and the Claude routes (2026-10-18).

## Internal review I12 (Claude Sonnet 5.5, effort low, on r71) — adopted, modified or rejected
- 1 (adopted; Q1 answered from the record): the highest-eligible rule is the owner's. AGENTS.md through v2.0.0 (the owner's PR #1, 2026-10-20) said "The Plan basis also divides by the highest eligible Value Multiple"; v3's AGENTS.md says "the selected subscription route", which the comparator selects (E85, E93). The draft now cites that source instead of the current AGENTS.md.
- 2 (adopted; Q2 answered from the code): the clip-gate denominator is n = the rows scored on that anchor object (rows on its workload with a positive cost on that basis), as `anchors.clip_gate` already computes; a subset workload is gated on its own anchor object.
- 3 (adopted, modified): between two editor rules where neither amends the other, the later-numbered record governs, and finding such a conflict is a defect corrected in the next revision. The generated rule index and build lint are not adopted (E63's active-rules manifest exists; I8 L4 rejected the same split).
- 4 (adopted as E216; a real gap): the 45-day limit for the AA model-page snapshot and the price records was stated but not enforced. `assemble` now fails when either is more than 45 days old at the release cutoff; the chart and catalog capture keeps its 7-day gate (E211). Today both are from 2026-10-17.
- 5 (adopted): Outputs item 1 now says the Plan ranking is exploratory displayed arithmetic and that no Plan frontier or bar claim is supported today.
- 6 (adopted): the quality-side Terminal-Bench leaf is tbench.ai's independent run; AA's Terminal-Bench executions are only in the cost basket, a cost-side exposure.
- R1, R2 (rejected): repeats of I8 L4 / I10 R5 without a new argument; methodology.md is the short published version.
- R3 (adopted, modified): the counts paragraph now also gives R_W (33), the admission reference panel (33), the anchor references (33) and the common-workload panel (34).

## Internal review I13 (Claude Sonnet 5.5, effort low, on r72) — adopted, modified or rejected
- M1 (adopted; Q1 answered from the code): a row is scored on W, with W's anchors, when every admitted component has a published cost whatever its E209 status (`basket.row_cost`); FullCost also needs every component confirmed complete. Claude Fable 5.1 is scored on W at $11,580.62 (API rank 30), flagged "partial component", counted in the clip-gate n and the common-workload panel (its 34th row), and kept out of R_W, P_K and the anchor references. The manifest's partial-component rule now names the Index-reconstruction cause too.
- M2 (adopted): the report window is the closed day interval [V − 30 days, V], both end days included (`plan_routes.in_window`); boundary test added (day 30 in, day 31 out).
- M3 (adopted as E217): the chart capture and the model-page snapshot must be at most 7 days apart, or `assemble` fails; today they are 37 minutes apart (18:48:27Z and 19:25:14Z on 2026-10-17).
- M4 (rejected; the reviewer's arithmetic is wrong): 2.74 is the value-point loss per cost doubling, 100 × 0.25 × ln 2 ÷ ln(19,978.30 / 35.76) = 17.33 / 6.33; the quality-point offset is 3.65. The label is correct.
- L1 (rejected): E numbers are assigned in adoption order; a renumbering takes a new, later number (E198's outcome became E202), so "later-numbered" and "later-adopted" coincide.
- L2 (adopted): capture timestamps are printed instead of dates.
- L3 (adopted): an exact tie at a vertex is resolved at capture by hovering and recorded in the capture; otherwise the vertex check fails.
- R1 (rejected): a transfer-multiplier grid is an analyst assumption about the Opus 5.5 donor's error, which O35 just declined in its Fable form; the transfers-off stratum already shows the Plan ranking without any transfer.
- R2 (rejected): E208 forbids AA's Index-wide shares as the basket's demand, and a sensitivity built on them would carry the same mismatch.

## Internal review I14 (Claude Sonnet 5.5, effort low, on r73) — adopted, modified or rejected
- 1 (adopted as E220): every controlled measurement records the allocation regime it was measured under (AGENTS.md); `plan_routes.check_allocation_regimes` fails the build on one without it, and measurements under different regimes are never compared or pooled as one. All nine SemiAnalysis routes carry it. Owner links already exist: the reconciliation inventory's rows carry owner URLs (build-checked), and each scored observation records its source URL (AA page, Bug Hunt run notes, tbench.ai).
- 2 (adopted as E218; new argument over I11 M3: reproducibility of O11 outcomes): the end-user report search must reach to at most 7 days before the release cutoff, or `assemble` fails. The search was rerun on 2026-10-21 by two research agents (web search, Hacker News comments; Reddit and X unreachable from the build environment; DeepSeek has no first-party subscription, Qwen3.8 Max is outside Alibaba's coding plan, Muse Code plans are request-capped provider allowances). No new qualifying report was found; the search log is in `evidencePolicy.searchLog`.
- 3 (adopted): the build already fails when two results share the largest N with different values and no selection reason exists; the draft says so, and the leaf table now says the harness and route are chosen by E206 and recorded. Q2 needs no owner answer: the tie stops the build until a recorded reason picks one.
- 4 (adopted): a frontier family missing Bug Hunt alone is not provisional; the sentence now says provisional only when the provisional rule fires.
- 5 / R1 (adopted as E219; a promised output was missing): the quality section's observed-range sensitivity band was stated but not implemented. `value_v3.observed_range_bars` now recomputes the API bar results with each missing leaf inside the cohort's observed range, labelled "sensitivity, not evidence" and kept out of every label (O19, O25). Today at the headline bar: 17 can qualify against 21, 5 confirmed in both, possible-cheapest 5 rows against 8; no confirmed cheapest under either bound. Q3 needs no owner answer: O19 already allows analyst sensitivities outside labels.
- 6 (adopted): E211 + E217 bound the model-page snapshot at 14 days, so E216's 45 days binds the price records in practice; stated.
- 7 (adopted): the two-status list now points to E209's four statuses.
- 8 (adopted): Terminal-Bench agent order stated: Terminus 2, mini-SWE-agent, OpenHands, then any other agent by name (`exact_match.TB4_AGENT_PREFERENCE`).
- 9 (rejected): repeat of I13 L1; E numbers are assigned in adoption order.
- R2 (rejected): repeat of I8 M4 (a coverage-restricted universe); E219 now shows the missing-leaf effect without narrowing the universe.
- R3 (rejected): the Plan anchor sensitivity is published in E187's diagnostic; the headline already carries E196's influence figures.
- R4: moot under E218.
- Q1 (owner decision challenge to the two-thirds admission rule; answered from the record, not escalated): the two-thirds joint rule is an editor decision (E26, E95, E140) that implements O15's capture phasing ("Basket is phased by capture"); admitting FrontierCode on 15 of 37 rows would put 22 rows on subset workloads. The AGENTS.md wording "admitted once its exact-configuration cost is captured" was the editor's own summary in the v3 release; it now states the two-thirds joint rule (E140).

## Internal review I15 (Claude Sonnet 5.5, effort low, on r74) — adopted, modified or rejected
- M1 (adopted; Q3 answered from the code): one observation date, E194's (window end, else report date, else publication date), used by E151 and by E144 for a report donor. A report with none cannot be admitted: `check_report_window` fails the build on it. Because counting reports lie in the closed window and "more than 30 days" is strict, a counting partition reaches "possibly superseded" only by change detection; the age stages govern controlled measurements, transfers and earlier-admitted reports kept as diagnostics. The r70 parenthesis about reports reaching expiry is replaced.
- M2 (rejected, with a stated consequence): AA's page fields are unrounded (I10 M2). If AA ever rounded, mass reconstruction failures would change the admitted set and W's hash, and scoring against the frozen anchors fails as a workload migration, so the release stops loudly; the draft now says so.
- M3 (rejected; Q1 not escalated): the only measured cross-model Claude pair contradicts the proposed direction. Fable 5.1's API price is 2.5× Opus 5.5's, so a token-weighted allowance would give Fable a 2.5× higher multiple and a cost-weighted one an equal multiple; SemiAnalysis measured 4.7× lower, which O35 attributes to Fable's own tighter allowance. Price does not predict the transfer error, so a price-ratio stress would add an ungrounded assumption; the transfers-off stratum stays the bound.
- M4 / R1 (adopted, modified, as E221): rows that can but need not reach a bar now publish u* = (100·H − Σ_observed w·z) / Σ_missing w with their missing leaves named. Today 16 rows are open at the headline bar; GPT-6.1 Sol (xhigh) needs 27.3 on FrontierCode and Terminal-Bench, DeepSeek V4 Flash 91.3. Re-freezing the bar on full-composite quality is rejected: O34 sets the ladder on displayed quality. Q2 not escalated: O19 already allows non-claim diagnostics.
- L1 (adopted, modified): an editor record never amends or overrides an owner decision. The conflict register is rejected (repeat of I12/I13).
- L2 (adopted): a report that does not name the exact model and effort, or mixes models, is excluded from every model route and kept at provider and plan level (AGENTS.md).
- L3 (adopted): every plotted point keeps its exact name, effort, fallback state and direct AA owner link with the capture time, so unscored inventory rows keep them too.
- L4 (adopted): the E37 completeness sentence is rewritten as a pointer to E209.
- R2: covered by M1. R3: rejected with M3. R4 (adopted): the headline bar is noted as a median over configurations, with E205's 58.3 for one row per family.

## Internal review I16 (Claude Sonnet 5.5, effort low, on r75) — adopted, modified or rejected
- M1 (adopted as E222; new argument from O25 over E202's "not a blocker"; Q1 not escalated, E170/E202 are editor decisions): a row on an unverified basis with FullCost on W now enters R_W at its published point, flagged provisional, so it can deny a confirmed label but never earn one (`value_v3._gated_box`). Without FullCost it stays listed as an omitted competitor. Today Claude Fable 5.1 lacks FullCost (E209), so no result changes.
- M2 (adopted): E212 gains the O32 row (a counting report leaves at day 31 with no grace; the partition is rebuilt and the route turns diagnostic below two concordant reports), and the age rows are stated to cover controlled measurements, transfers and earlier-admitted diagnostic reports only.
- M3 (adopted, modified; Q2 not escalated): E206's key is (roster name, effort); harness and route are chosen by the largest-N rule and recorded. A harness switch from a later larger-N run is published as a leaf-source change with both values (fixture added). A pooled mean across harnesses is rejected (Bug Hunt's estimand is model plus harness, E29), and a fixed harness preference would discard the owner's larger samples.
- L1 (rejected): third repeat of the numbering tie-break point (I13 L1, I14 9).
- L2 (adopted): off-line overlaps and on-vertex ties are separate cases; an on-vertex tie that hovering cannot separate stops the build until the owner decides.
- L3 (adopted): "ranked rows" is replaced by "cohort rows" throughout (5 places).
- L4 (adopted): comparator key 3 is named "the larger multiple within the same identification class and evidence grade", with the v2 AGENTS.md wording kept as history.
- L5 (rejected): a row failing only the reconstruction test is scored on W at its published costs and flagged (E209); a [C_7 − gap, C_7] interval would assign the gap to the basket without evidence of where it lies.
- R4 (rejected): a leaf-composition shift is an estimate of missing leaves from cohort means, which the no-imputation rule forbids even as a column; E219 and E221 bound the effect without estimating it.

## Internal review I17 (Claude Sonnet 5.5, effort low, on r76) — adopted, modified or rejected
- M1 (adopted as E223; new argument: the 7-day gap had no recorded rationale and was not implemented): independence is distinct observers and no shared upstream source (post, thread or derivation). `plan_routes.check_report_independence` fails the build on a pooled set with a missing or repeated observer or a shared upstream source. The calendar gap is dropped: O11 asks for independent reports, and concordance inside the 30-day window already tests agreement. No route pools reports today.
- M2 (adopted, modified, as E224): Bug Hunt's own scoreboard gives the cross-harness evidence a same-harness variant would need. Wherever it reports a ranked configuration's exact effort on two or more harnesses, the largest-sample result per harness is published beside the leaf (`build_scores.bug_hunt_cross_harness`). Today: Gemini 4 Argon (high), Antigravity CLI 40.7 (3 runs) against Gemini CLI 33.0 (1 run). A single-harness restricted variant is not adopted: Bug Hunt runs each family on its vendor CLI, so one declared harness would leave most rows missing.
- L1 (adopted): weights are percent points summing to 100; p_i and both quality equations divide by 100; fixture added (DeepSWE missing, others at 60 → p = 0.70, Q̄ = 60, Q ∈ [42, 72]).
- L2 (adopted): the window compares UTC calendar dates, date(V) − 30 days ≤ d ≤ date(V), a timestamped E194 date truncated to its UTC date (as `plan_routes.in_window` does).
- L3 (adopted): the non-discriminating SD is over the cohort rows that observe the leaf (`diagnostics.non_discriminating`); S_C and S_Q are defined where the influence statistic uses them.

## Internal review I18 (Claude Sonnet 5.5, effort low, on r77) — adopted, modified or rejected
- M1 (adopted, modified, as E225; Q1 not escalated): tbench.ai lists one row per model, effort and agent (no duplicates in the 23 captured rows) and publishes no trial count or submission ID, so a trials/date/ID order cannot be implemented from public data. `exact_match.select_tb4_row` now stops the build when a second row exists for the chosen agent, until a recorded selection names the configuration's row; "by name" is ascending code-point order.
- M2 (adopted; Q2 answered from the code): E222's flag is the interval box's label denial (`intervals.Box.provisional`), separate from the coverage-defined provisional status (`QualitySummary.provisional`); the row stays in the bar population and the ladder, and UniqueLabelEligible needs both. Rows on a price not in force are label-denied the same way.
- M3 (adopted): ages are whole UTC calendar days, date(V) minus the observation date, with strict "more than" thresholds (`plan_routes.age_days`); boundary tests added at 30, 31, 90, 91, 120 and 121.
- L1 (adopted): the window spans 31 calendar dates.
- L2 (rejected): repeat of the generated-prose lint (I7 M1, I12 R1).
- R1 (rejected): repeat of the full-coverage universe (I8 M4, I16 R2); E219 and E221 now cover what it would show.
- R4 (rejected): the README's "What the evidence supports" list already carries these statements, generated from the release data.
- R5 (rejected): the headline table stays the one ranking; E199 and E205 are published diagnostics, and a second equally prominent column would compete with the owner's cohort rule (O1, O33).

## Internal review I19 (Claude Sonnet 5.5, effort low, on r78) — adopted, modified or rejected
- M1 (adopted; new argument: a 45-day price record cannot show a tariff change after it, which is what E170/O29 test): the price records now pass a 7-day gate at V (`value_v3.PRICE_RECORD_MAX_AGE_DAYS`); the model-page snapshot keeps 45 days (14 in practice via E211 and E217). Today the records are from 2026-10-17 (3.4 days).
- M2 (adopted, E225 extended): 13 of the 14 cohort rows with a Terminal-Bench leaf took it from the open alphabetical tail (vendor CLIs). The agent list is now closed and versioned (Terminus 2, mini-SWE-agent, OpenHands, Claude Code, Codex, Grok Build, Muse Code): a candidate row from an unregistered agent stops the build until a registry update places it, so a new submission never switches a leaf by sort order. Each release publishes the count of cohort rows per selected agent (today mini-SWE-agent 1, Claude Code 5, Codex 6, Grok Build 1, Muse Code 1). E206's "published as a leaf-source change" overstated what is built; it now says the switch shows in the per-row harness and in E224's cross-harness list.
- L1 (adopted): the transfer paragraph's age clock is the E194 observation date.
- L2 (adopted, disclosure): labels state that they hold under the registered role-group kernel checks, not under every per-competitor kernel combination. Single-competitor flips are not added: they would change the scenario design for a frontier and bar output that has no confirmed label today.

## Internal review I20 (Claude Sonnet 5.5, effort low, on r79) — adopted, modified or rejected
- H1 (adopted; escalated to the owner, answered by O36 below): renormalising over each row's own leaves is not neutral, because the sparse leaves are the hard ones. Verified with the new common-leaf diagnostic (E226, `value_v3.common_leaf_diagnostic`): without Terminal-Bench and FrontierCode (the leaves fewer than 90% of rows have), 30 API rows move (largest 12, Muse Spark 1.3 xhigh), and 20 rows instead of 18 reach the headline bar; five rows differ by more than one cost doubling's worth (Gemini 3.8 Flash −5.6, Grok 4.7 −5.2, Muse Spark 1.3 xhigh −5.0, GPT-6 Luna −4.6, GPT-5.6 Luna −4.1).
- M1 (adopted, E227): every DeepSWE row and 13 of 14 Terminal-Bench rows run each lab's model in that lab's own agent, so the harness confound covers DeepSWE and Terminal-Bench too, not only Bug Hunt. E19's premise is corrected, the named S2 harness band now covers all three leaves (unevaluable today, as before), and a harness-by-leaf disclosure is published.
- M2 (rejected as stated): the published diagnostic already reads "undefined (panel too small)" for the Terminal-Bench same-harness check; the draft now says so explicitly.
- M3 (adopted as E228): a selected Plan route whose evidence a detected change (or two reports of a limit change) may have superseded now competes as a blocker, so it earns no interval label (`plan_routes.change_flagged`); age alone stays a flag only. No route is identified today.
- L1 (adopted): "S1 core" is the S1 stream on the core specification branch (no named stress branch).
- L2 (adopted): label-denied rows (unverified basis, E222) are treated as blockers, so their own frontier and bar statuses read "withheld".
- L3 (adopted): the E151 parenthesis is split.

## Owner decision (2026-10-21, after internal review I20)
- O36. Quality is computed only on a common benchmark set, so the ranking is fair; Terminal-Bench and FrontierCode stay in it. Owner's words: "Actually, even though limiting, we'll have to compute quality only on benchmarks 100% of rows have. Otherwise the ranking won't be fair." Asked which rows decide the set and how to reweight, the owner answered: "Actually only those models will be in the benchmark, for which a maximal set of benchmarks are available. But thorough deep/extensive search will be undertaken to be 100% sure that a model doesn't really have a benchmark score. Note that AA is not the only source for benchmark scores for a given model-benchmark pair. If the same benchmark is run elsewhere, including the model provider, we'll admit that if there is no other source. In general, these benchmarks are available for most leading models, if search is done extensively." and "TB and FC will not be removed as per my last answer."
  - Reading adopted: every ranked configuration has all eleven leaves at the owner-set weights, so quality is the full weighted mean with no renormalisation. A configuration still missing a leaf after an exhaustive, logged search is not ranked; it stays listed with its missing leaves (AGENTS.md: report missing coverage explicitly; never silently excluded). Leaf sources in order: the source already used (AA, tbench.ai, the Bug Hunt owner); else another independent party running the same benchmark version on the exact configuration; else the model provider's own published result, labelled as a provider claim. Exact-variant rules still hold (no transfer between efforts or versions).
  - This supersedes AGENTS.md's "Missing leaves stay missing, low coverage marks a row provisional" and narrows the frontier-inclusion rule to configurations with the full benchmark set; AGENTS.md is updated to say so.

## Owner decisions (2026-10-21, sources and frontier families under O36)
- O37. Sources for the two sparse leaves. Terminal-Bench: "AA, tbench.ai fills gaps": the leaf is AA's own Terminal-Bench 4.0 run in the Intelligence Index (one harness, mini-SWE-agent, captured for every row), and tbench.ai's vendor-agent rows fill a gap only. FrontierCode: "AA, fill gaps from Cognition or other sources if needed": AA's run first, then Cognition's leaderboard (FrontierCode's author) for the exact effort, then other parties. MiMo-V2.6-Pro DeepSWE: "Admit as provider claim" (Xiaomi's 71.9 for the released checkpoint, labelled).
- O38. MiMo-V2.6-Flash, a required AA frontier family, has no Bug Hunt result for its reasoning configuration after the search (the only run is the Bug Hunt owner's OpenRouter default-route mean, 23.3/105, whose reasoning state the owner never asserted). Asked whether O36 or the frontier-inclusion rule governs, the owner chose "Exclude it (O36 wins)": the family is listed with its missing benchmark and the logged search, not ranked, and AGENTS.md and the reconciliation gate accept such a logged incomplete-evidence exclusion as the only way a frontier family goes unranked; the search is repeated each refresh.
- Search results (2026-10-21, logged in `data/leaf_evidence.json`): FrontierCode filled for Muse Wonder Full and DeepSeek V4 Pro from a newer AA capture, and for GPT-6.1 Sol (xhigh, high, medium, low), Claude Opus 5, GPT-6 Sol, GPT-5.6 Sol and GPT-5.6 Luna from Cognition's leaderboard (exact efforts; data.json captured with its SHA-256). DeepSWE filled for MiMo-V2.6-Pro (provider claim, O37). Not found after search: FrontierCode for Grok 4.6 (xhigh) (xAI publishes High only), DeepSeek V4 Flash (Cognition lists high only; AA's figure is V4.1 Flash), Muse Wonder and Muse Spark 1.3 (xhigh) (Meta's scorecards have no FrontierCode row); Bug Hunt for MiMo-V2.6-Flash. These five are listed, not ranked: cohort 32 (31 with a value score) of 37.
- Implementation (editor decisions):
  - E229: the E125 same-harness diagnostic becomes Terminal-Bench cross-source agreement, AA's run against tbench.ai's rows on their common panel; a row whose leaf is a tbench.ai gap fill counts as harness-mixed. Harness by leaf (E227) reads the leaf's own provenance.
  - E230: the legacy v2 composite applies the O36 exclusion before normalising, so both rankings list the same rows; its finite-quality check for required families is removed (every ranked row has DeepSWE, so it cannot fire).
  - E231: unranked cheaper siblings (O33) are computed over complete rows, so an O36-listed effort counts as unranked.
  - E232: with every ranked row complete, the provisional rule, the observed-range sensitivity (E219), the required missing scores (E221) and the common-leaf diagnostic (E226) report no missing leaf; they stay as standing checks for a release that needs them.
  - Pre-release re-freeze on the 32-row cohort: anchor values unchanged, bar ladder 47.4 / 55.3 / 59.6; the old- and new-bar results are in `dual-run-2026-10-21-o36.json`.
  - E227 completed in code: the harness band's registered rule named Bug Hunt, DeepSWE and Terminal-Bench, but the engine stressed Bug Hunt only. It now stresses every agent-run leaf (Bug Hunt, DeepSWE, and Terminal-Bench only when it is a tbench.ai gap fill, since AA's run uses one harness); the branch stays unevaluable today. S1M widens only a tbench.ai gap fill, so it equals S1 today.
- Draft r80 records O36–O38, E229–E232 and the I20 items not yet in the draft text (E226 common-leaf diagnostic, E227 harness by leaf, E228 change-flagged Plan blocker, "S1 core" defined, label-denied statuses read "withheld", the E151 parenthesis split), and refreshes every figure the smaller cohort changed.

## Internal review I21 (Claude Sonnet 5.5, effort low, on r80) — adopted, modified or rejected
- H1 (adopted as E233 and E234): a row with a provider-claimed leaf now competes like an E222 row and earns no label of its own (`value_v3.provider_claimed`; today MiMo-V2.6-Pro, already subset-scored). Every third-party fill gets a cross-check where AA also reports the same name and effort: FrontierCode against Cognition on 10 rows, τ_b 0.73, Cognition 2.5 points above AA on average and 11.8 at most (Grok 4.7), published as "FrontierCode against Cognition"; and a gap-fill removal sensitivity (API 11 rows move, largest 6 for MiMo-V2.6-Pro; Plan 15, largest 8). The evaluated configuration and harness of each fill were already published in raw-data.md. Owner question 1 (may a provider-claimed row earn a label) is answered by this editor decision; the owner may override.
- M2 (adopted): E26's stale counts corrected (29-row panel, cohort 32; Fable 5.1 the 30th common-workload row at API rank 24, not the 31st the reviewer computed: 29 complete rows plus Fable). The brief gains a current-figures line; historical figures stay dated.
- M3 (rejected; owner decision challenge): O25 fixes the published-record target and the label scope; the README sentence that prints a confirmed label opens with the definition ("anywhere inside the published record's precision and missing-evidence bounds"), and E155 states the excluded noise beside every share table. That the S1 stream collapses towards the displayed record while every row is complete is true and is now visible in the manifest (E235).
- M4 (adopted as E235): the rules O36 leaves inactive are indexed in the Quality section, and the manifest carries one "vacuous" entry for them plus "full benchmark set (O36, O38)" and "provider-claim label denial (E233)".
- L5 (modified): the README now names, right under the ranking, each configuration listed for a missing benchmark, marking a frontier family (MiMo-V2.6-Flash); a separate cost band is not added because the row has no score to show beside the ranked ones.
- L6 (rejected): the ±20% reading is E33 (max/min ≤ 1.20), adopted with O11; no new argument.
- Design 1 (rejected for now): a deterministic weight-flip margin is new machinery; the S2 weight stress is already published, and O25 keeps labels on the published record. Design 2 (rejected): methodology.md is the generated public summary and the manifest lists the rules in force. Design 3 (modified): counts in the draft were refreshed by hand from the build; the published documents are already generated. Design 4: E234. Design 5 (rejected): E199's frontier-only bar is published in scores.md.
- Also fixed while verifying: the swing-attribution bridge (E177) rejected the release bundle because four documents (Bug Hunt scoreboard, Cognition data, frontier capture, roster) had no class; they are now classified, and the test runs the real bundle.
- Draft r81.


## Internal review I22 (Claude Sonnet 5.5, effort low, on r81) — adopted, modified or rejected
- H1 (modified): the reviewer read AGENTS.md as it stood before 2026-10-21; the checked-in AGENTS.md already states O36 and O38. The draft now says "no quality floor on a score; ranking itself requires the full benchmark set (O36, O38), which supersedes O8's ranking of partially covered rows", and that AGENTS.md was amended. (c), showing a listed frontier family's partial-coverage quality in the ranking table, is rejected: the owner ruled that only full-set configurations are compared (O36), and I21 L5 already names the listed rows under the table.
- M1 (rejected with the reason now in the draft): a third-party fill keeps label eligibility because O37 names its source and that source ran the same benchmark version on the exact configuration; a 10%-weight leaf moves quality by a tenth of the offset (0.25 points on average, 1.2 at most), and E234's removal sensitivity shows the result without it. A provider claim is the last source O36 admits and has no such check (E233).
- M2 (adopted): "Plan evidence today": SemiAnalysis published 2026-10-06 (E194 date), Current until 2026-11-05, expiry 2027-01-04, demotion after grace 2027-02-03, each route's allocation regime, and Fable 5.1 scored on its own measured Max routes.
- L1 (adopted): 12 of the 13 matched tbench.ai rows run in the lab's own agent.
- L2 (rejected): the bar is a quality level over the non-provisional cohort rows with a displayed quality; cost is not required (counts defined once, E192), and E233 concerns labels, not bar membership.
- L3 (rejected): E201a already flags window-straddling reports and uses isolated per-period figures where a report publishes them, as AGENTS.md says; no new argument.
- Design 1–2: as H1(c) and M1. Design 3 (rejected for now): a standard-error margin needs a sampling model for every leaf, and only Terminal-Bench publishes one; the leaves without one would need assumed noise, which O25 keeps out of the published-record claims. Design 4 (adopted as E236): the manifest marks S1M dormant while no ranked leaf carries a published interval. Design 5: M2.
- Draft r82.

## Internal review I23 (Claude Sonnet 5.5, effort low, on r82) — adopted, modified or rejected
- M1 (adopted): the sibling list now matches the cohort (Muse Spark 1.3 (xhigh) and Grok 4.6 (xhigh) are listed under O36), and the draft states that a ranked sibling stays ranked by retention when its family's frontier or near configuration is listed under O38 (owner question 1, answered from O33 and O38; none today).
- M2 (adopted): the frontier-families population (E187, E199) is defined as the rows carrying a frontier or near-frontier inclusion reason, each such family's primary row; the nine rows are named, and E205's every-family primary rows are distinguished. This matches the build (`value_v3.configuration`'s frontierFamily flag).
- M3 (adopted as E237): every gap fill carries a comparability record, benchmark version and metric, and the build fails when the version is not the leaf's or the metric is missing (`value_v3.check_comparability`); raw-data.md prints both. The rank band the reviewer asks for is E234's removal sensitivity. Owner question 2 challenges O37 and is not relayed: the owner admitted that claim knowing it is a provider claim, and E233 already denies it labels.
- L1 (adopted): the lifecycle dates give each stage's first day (possibly superseded from 2026-11-06, expired from 2027-01-05, demoted from 2027-02-04).
- L2 (rejected): E216's 45 days is the snapshot's own backstop if E211 or E217 change; it cannot disagree with them.
- L3 (rejected): no release has been published, so the version string names the pre-release freeze; the dual runs record each re-freeze, and the first release freezes the content the string names.
- Design 1 (rejected): the published documents are generated; the draft is the specification and its "today" figures are refreshed from the build each revision. Design 2: E237. Design 3 (rejected for now): Reddit and X are unreachable from the build environment, which the search log records; a recall audit needs those channels. Design 4 (adopted): the label wording states what "confirmed" means while every row is complete.
- Draft r83.

## Internal review I24 (Claude Sonnet 5.5, effort low, on r83) — adopted, modified or rejected
- H1 (adopted as E238, modified): AGENTS.md ties the Anthropic and OpenAI comparison to one analysis the owner selected (2026-10-07), so "latest" means the owner's selection, not publication order. The build now fails when a controlled measurement or a transfer for those providers cites another analysis (`plan_routes.check_selected_analysis`); a newer analysis enters only by the owner's selection and then replaces the old one outright, whatever its multiples. Owner question 2 is answered by AGENTS.md.
- M1 (adopted as a statement of the existing rule): selection precedes the benchmark check; a near family's selected configuration that lacks a leaf is listed under O38 (AGENTS.md: "selected configuration"), never replaced by another effort; another complete evidenced effort stays ranked by retention; the gate needs no roster decision because the configuration is in the roster. Owner question 1 is answered by O38's wording.
- M2 (adopted as E239): a closed per-leaf source registry in `data/leaf_evidence.json`; a fill from an unregistered party stops the build, and a new source enters by a dated registry update.
- M3 (modified): the ranking table now flags "provider-claimed leaf" (README, scores pages and the site). The best-case rank bound for subset rows is rejected: O17 keeps a subset row's table position with its flag, and the flag already says its cross-workload ordering is not identified.
- M4 (adopted): E210's domain ranges over categories with measured or basket demand (ρ = ∞ where the basket has none), with the reviewer's two-category fixture; the bound is not implemented in code because it cannot fire today.
- M5 (adopted): E92 restated once as the full conjunction with blocker(i) (O29, E222, E228, E233).
- L1 (adopted): the 14-against-15 gap is the bar's own configuration, whose displayed quality equals the frozen level; disclosed, not changed (O34).
- L2 (adopted in wording): the offset estimates, not bounds, the fills' effect, and leans favourable. The bias-adjusted variant is not added; the removal sensitivity already shows the result without the fills.
- L3 (rejected): each Bug Hunt harness string already names the shim or API route (E227 and raw-data.md); no new argument for a separate flag.
- Design 5 (rejected): E235 and E236 mark the inactive rules that matter for the published outputs; the Plan identification blocks are dormant by E61/E67, which the summary states.
- Draft r84.

## Internal review I25 (Claude Sonnet 5.5, effort low, on r84) — adopted, modified or rejected
- Owner question 2 was put to the owner (task-sampling stream). Answer: "Add it, labelled". Recorded as O39 below. Owner question 1 (a revised article at the same URL) is answered editorially under M3.
- M1 (adopted): every description of S1M now says it is dormant while no ranked leaf carries a published interval (E236); the Measurement layer bullet says no confidence interval enters any v1 stream today, and S1T is the stream that carries sampling noise.
- M2 (adopted, extending E234): `value_v3.gap_fill_bars` names, for every frozen bar on both bases, the displayed-record cheapest row with the fills as published, removed and with third-party fills lowered by the mean offset. Today the headline and lower bars keep their rows; at the upper bar lowering Cognition's fills moves the cheapest row from GPT-6.1 Sol (high) to GPT-6.1 Sol (xhigh) on both bases. Labels never change.
- M3 (adopted as a rule, modified): the selection is pinned by URL and by the figures transcribed at selection; a change to the article is a scoped change detection whose new measurements stay diagnostic until the owner re-selects, with the clock from the revision date. The article is not captured in the bundle, so no content hash is published.
- L1 (adopted): the cost ratio is the point's total Index cost over the lowest rendered-frontier cost whose plotted (rounded) Index reaches it, as `frontier.frontier_gaps` computes.
- L2 (adopted): the comparability records and cross-checks are the diagnostics.
- L3 (rejected as stated, wording fixed): the harness band already uses every configuration on the captured leaderboard, cohort or not; none is listed under two agents, so it stays unevaluable.
- Design 2: adopted by the owner as O39. Design 3 (rejected): E235 and E236 index the inactive rules that affect the published outputs; the Plan interval machinery is dormant by E61/E67, which the headline states.

## Owner decision (2026-10-21, after internal review I25)
- O39. Benchmark sampling noise. Asked whether to add a non-authorising task-sampling stream, the owner chose "Add it, labelled". Implemented as stream S1T: every observed leaf is redrawn from a normal with its plug-in binomial standard error from the published task count (DeepSWE 113, FrontierCode 1.1 Main 100 per AA's evaluation page, Terminal-Bench 66, AutomationBench-AA 657, AA-LCR 100, SciCode 288, HLE 2,158, CritPt 70, Bug Hunt's 105 bugs), AA-Omniscience from its 6,000 +1/0/−1 questions, and GDPval-AA from AA's displayed rating interval read as a 95% normal interval (SD 13.3 Elo, an assumption marked analyst-derived). Tasks are treated as independent ("independent-task approximation"). It never authorises a label or changes a score. A rank-separability diagnostic prints the median value gap two rows need to separate (today 3.34 API, 3.35 Plan) and how many adjacent ranks separate (0 of 30 on each basis); the README states it beside the ranking. AGENTS.md records O39.
- Draft r85.

## Internal review I26 (Claude Sonnet 5.5, effort low, on r85) — adopted, modified or rejected
- Three questions went to the owner through the questions UI (the reviewer's Q1 and Q2, and its design recommendation 1). Answers recorded as O40–O42 below.
- M1 (adopted): the separability statement says the threshold is conservative and why, and prints separable adjacent ranks at correlations 0, 0.3 and 0.6 (API 0 / 1 / 2, Plan 0 / 3 / 3). A paired bootstrap is not possible: no source publishes task-level outcomes for the cohort.
- M2 (modified): GDPval stays in S1T, labelled analyst-derived, with the wide reading (±26 Elo as one SD) published as a sensitivity; it leaves the count unchanged today (median 3.35 against 3.34). Per-row rating intervals are not yet captured; the draft says each row's own interval replaces the single width once captured.
- M3: owner decision O40.
- M4: owner decision O41.
- L1 (adopted): E238 is scoped to Claude plans and ChatGPT plans for Codex; every OpenAI route in v1 is a Codex plan.
- L2 (adopted as a definition): reports are recorded by date, so the report window's cutoff is V's UTC date, whole.
- L3 (rejected): the ladder positions are elements of the order by owner decision O34; the setter's status is disclosed (E201b).
- Design 1: owner decision O42. Design 2: as M1. Design 3 (rejected): as I21 Design 2 and I25 Design 3. Design 4: as M2.

## Owner decisions (2026-10-21, after internal review I26)
- O40. Asked whether an exact per-(plan, model) measurement added later to the selected SemiAnalysis article replaces the transfer at once or only after re-selection, the owner chose "Replace immediately": it replaces that model's transfer, labelled "added after selection" with its date (`publication.plan_evidence_label`); every other change to the article stays diagnostic until re-selection. AGENTS.md records it.
- O41. Asked whether to show a reduced-leaf value for a listed frontier family, the owner chose "Show it, separated": each listed frontier or near-frontier family shows, apart from the ranking, an indicative value on its remaining leaves (renormalised, no imputation) with its cost on its own workload's frozen anchors, labelled "not ranked, not comparable", with no rank, band or label (`value_v3.listed_indicative`; today MiMo-V2.6-Flash: quality 53.9 over 90% of the weight, API 60.0, Plan 53.2). README prints it under the ranking.
- O42. Asked whether to group ranks into noise bands, the owner chose "Add bands": rows in value order join the current band while not separable from its first row at correlation 0 (`value_v3.rank_bands`); the README's ranking prints "Noise band (Plan / API)" beside the ordinal ranks, and the site offers it as a "Noise band" column. Today API 1–5, 6–11, 12–21, 22–30, 31; Plan 1–8, 9–22, 23–25, 26–27, 28–30, 31.
- Draft r86.

## Internal review I27 (Claude Sonnet 5.5, effort low, on r86) — adopted, modified or rejected
- H1 and H2 went to the owner through the questions UI. Answers recorded as O43 and O44 below.
- M1 (adopted): the independent weight is 10% (Bug Hunt) since O37; leave-AA-out reads 10%; E62's Q_ind is the row's Bug Hunt score, the one independently executed leaf, as `value_v3._independent_quality` already computes (a tbench.ai Terminal-Bench gap fill is not counted: its leaf stays AA-run by its named source); the Terminal-Bench overlap note is corrected.
- M2 (adopted): the separability formula is written with ρ, per adjacent pair, from analytic quality-leaf SDs (cost not drawn); the band rule says every row is inseparable from its band's first row and that adjacent rows in different bands may also be inseparable.
- M3 (adopted): the direction is "not established": shared tasks narrow the threshold, omitted sources (run-to-run and harness variance, AA's single cost run, owner-named transfer error) widen it; the README prints how many Plan rows are on transfers (20).
- L1 (adopted): O39 is named as the one exception to "never assumed normal".
- L2 (rejected): frontier membership is AA's rendered line as observed (AGENTS.md); a plotted point above-left of a mid-line segment would contradict AA's own rendering, and E195 checks the path against the plotted points.
- L3 (rejected): repeat of I23 L2.
- Design 2 (rejected): repeat (I21, I25, I26). Design 3 (adopted): scores.md's Plan route table prints basket runs per fee period (amount ÷ basket API cost), e.g. 0.13 a month for Claude Sonnet 5.5 (max) on Pro, 0.03 for GPT-6 Astra on Plus. Design 4 (adopted): a displayed-record result that changes under E234 is marked fill-sensitive (today the upper bar on both bases).

## Owner decisions (2026-10-21, after internal review I27)
- O43. Asked whether a listed frontier family should count as a label-denying competitor in the bar and frontier claims, the owner chose "Keep it out": listed families stay outside every claim, and the summary states that the outputs compare ranked configurations only, naming the listed families (MiMo-V2.6-Flash today).
- O44. Asked whether each bar should get a companion result the setter's exact position cannot drive, the owner chose "Add margin companion": beside each bar's displayed-record cheapest row the summary names the cheapest configuration whose displayed quality clears the bar by at least the quality noise margin, 1.96 × √2 × the median row's S1T quality SD (today 4.5 points). Today: API GPT-6.1 Sol (xhigh), GPT-6.1 Sol (low), Gemini 4 Argon (high); Plan GPT-6.1 Sol (xhigh), Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (max). The frozen bars are unchanged.
- Draft r87.

## Internal review I28 (Claude Sonnet 5.5, effort low, on r87) — adopted, modified or rejected
- Q1 (answered from the record, no owner question): I27 M3 was adopted, so the direction is "not established"; O42's ledger entry decided bands, not a direction. The Outputs wording "conservative direction" is replaced (M1, adopted).
- H1 (adopted as E240): every logged search for a listed frontier or near-frontier family also logs an open-web discovery step: the queries and every candidate found, each resolved by a dated registry addition or a dated rejection with a reason (different benchmark version, different effort, different model version, not the exact configuration, relay of a registered source, no published method, published after the cutoff, not a score). The build fails on a missing step or an unresolved candidate (`value_v3.check_open_web`). The 2026-10-23 discovery (`open-web-discovery-2026-10-23.json`, 5 to 11 queries per gap) found no unregistered run; it found that AA now shows FrontierCode 1.1 for Muse Wonder (46.47%) and Muse Spark 1.3 (xhigh) (38.63%), first seen after the cutoff, which went to the owner (O47).
- H2 (adopted; Q3 to the owner as O45): the common-GPT rule is stated exactly; its lower-of selection was an implementation choice, not the owner's. E246: a SemiAnalysis figure that names a model without an effort binds to that model's unsuffixed AA row (max), the configuration AA plots under the bare model name, and to no other effort. MiMo's 1.5× was an owner assumption without a measurement; Q2 went to deep research and then to the owner (O46).
- M2 (adopted with the owner's 2026-10-22 instruction): the selected article is paywalled, so a later analysis is detected by a weekly scheduled search of SemiAnalysis's newsletter and its X accounts; "added after selection" is a new (plan, model) row against the figure table transcribed at selection (`plan_cost_routes.json` sourceEvidence.semianalysis, hashed in the evidence bundle).
- M3 (adopted as E243): the counts were already defined once; the draft now says the bar population keeps full-benchmark rows without a cost by choice, and a sensitivity publishes the ladder over scored rows only (`costed_bar_ladder`; today Muse Wonder Full is the one costless row).
- L1 (adopted as E241): S1T's binomial SD uses the proportion (k + ½)/(n + 1), so a 0% or 100% score keeps a positive spread.
- L2 (rejected): repeat of I23 L3; the anchor version string changes with the re-freeze O47 requires, and no version was published before it.
- Design 1 (adopted as E242, not a Fable diagnostic): a Plan band resting on an owner-named transfer is marked †, and the separability statement prints the factor by which a transferred multiple can be wrong before the value moves by the median threshold, 2^(threshold ÷ value points per cost doubling), a tolerance, not an estimate. Design 2 (adopted as E244): a GitHub issue form, "Subscription usage report", collects end-user measurements with the AGENTS.md fields. Design 3 (rejected): repeat (I21, I25, I26, I27). Design 4 (adopted): the summary names the frontier-families bar beside the headline bar.

## Owner decisions (2026-10-22 and 2026-10-23, after internal review I28)
- Weekly SemiAnalysis watch (2026-10-22): asked how to detect a later SemiAnalysis analysis of a paywalled article, the owner asked for a weekly scheduled web search for a new SemiAnalysis article on Claude vs Codex usage, monitoring SemiAnalysis's X accounts as well; created as the scheduled task "SemiAnalysis subscription usage watch" (Mondays 08:51 UTC, report-only, push and email).
- MiMo research (2026-10-22): the owner asked for MiMo-V2.6-Pro and Flash's value multiple to be researched with Silver Bullet's Deep Research workflow, Claude's deep-research skill and Perplexity. Silver Bullet's multi-model dispatch (`skills/multi-ai-deep-research`, opencode-go models) could not run: the environment holds no opencode provider credentials. Claude's deep research (three researchers: official pages, English and Chinese end-user reports) and Perplexity Search with Thinking (GPT-6.1 Sol, Grok 4.7, Gemini 3.8 Flash) agreed: no end-user measurement of a V2.6 billing period exists; Xiaomi prices credits at parity with its API (100M credits = ¥1), so a full quota is worth 0.96–1.24× the fee at day rates. Record: `research/2026-10-23-mimo-token-plans/`.
- O45. Asked whether GPT-6.1 Sol and GPT-6 Astra keep their own SemiAnalysis figures, the owner chose "Own figures first" and added that rows must be per model, per plan. Sol (max) and Astra (max) take their own figure on each ChatGPT plan (Astra's selected route moves from Plus 8.1× to Pro 200 14.485×; Sol's stays Pro 500 10.772×); every other GPT row takes the lower figure per plan as a labelled assumption naming its donor route; every route record names one model and one plan (93 records).
- O46. Asked what the MiMo rows should use, the owner chose "Quota ceiling per tier": each MiMo-V2.6 model takes, per Token Plan tier, the tier's monthly credits valued at Xiaomi's overseas API rate for that model ($1.44 per billion credits for Pro, the cache-hit rate, the lower of $1.44–$1.45; $1.40 for Flash) over the list fee: Pro 0.984 / 0.99 / 1.0944 / 1.1808 and Flash 0.9567 / 0.9625 / 1.064 / 1.148 on Lite / Standard / Pro / Max. Labelled provider-derived, not a measurement; an explicit AGENTS.md exception; replaces the 1.5× assumption.
- O47. Asked how to treat FrontierCode results AA published after the cutoff, the owner chose "Move cutoff now": the release cutoff moves to the new capture instant and every AA source is re-captured; anchors are re-frozen with a dual run.
- O48. Asked whether "per-model, per-plan" meant the Plan ranking itself, the owner chose "Rank every plan": the Plan ranking has one row per configuration and plan. E245 implements it: a plan row is a configuration on one plan whose route is the official comparator's choice among that plan's candidates (E85, E88); a configuration with no eligible route keeps one API-cost row; rows of one configuration share its quality and API cost; the Plan anchors, clip gate, cost influence, identification yield, interval outputs, displayed cheapest rows, separability, bands and scenario shares range over plan rows, with one configuration's plan rows sharing every scenario draw (one dependency group) and counted inseparable only by value; a configuration's own Plan figures (README table, model pages, Plan diagnostics that rebuild anchors or move evidence) are those of its representative row, the plan row of its selected route; the README and site list every plan row.

## Owner decisions (2026-10-23, after the O47 re-capture)
- O49. The re-capture found that AA withdrew DeepSWE from its Coding Agent Index (v2.0 runs FrontierCode 1.1, SWE-Atlas QnA and Terminal-Bench 4.0). Asked what replaces DeepSWE's 20% software-engineering weight, the owner chose "drop DeepSWE in favor of FrontierCode" and, of the redistributions offered, "FC 25 / TB 20 / BH 15": FrontierCode 25%, Terminal-Bench 20%, Bug Hunt 15% (software engineering stays 60%); the other seven leaves keep their weights, so quality has ten leaves. The owner also asked for research into broadening the software-engineering set beyond these three (AI Coding Daily, LiveBench and Surge's Complex Constraints named as must-incorporate, Vals.ai as an example); that research is recorded in `research/2026-10-23-swe-benchmarks/` and its policy question goes to the owner before any leaf is added.
- O50. Asked whether the basket moves to Coding Agent Index v2.0 (290 tasks: FrontierCode 1.1 main 100, SWE-Atlas QnA 124, Terminal-Bench 4.0 66), the owner chose "Migrate to v2.0 now". Under E140 the index is admitted only when its exact-configuration cost covers two-thirds of the cohort jointly with the other components; at the cutoff AA publishes v2.0 cost for 7 of the 27 ranked configurations, so it is pending and the main workload is the seven AA Index SDLC evaluations (E184: the migration is deferred, not forced). ITBench-AA stays a pending chart component (2 of 27).
- O51. Asked why rows outside the frontier and near-frontier families were ranked (O30/O31/O33 retention for DeepSWE and Bug Hunt evidence), the owner asked "Why is that at all required?" and then chose "Frontier + near only": the cohort is the configurations AA plots on, or within the near gap of, its rendered frontier (29 at the cutoff). The retention rules (E163, E187's retention half, O31, O33's evidenced-effort rows) are withdrawn; 27 cohort configurations have the full benchmark set and are ranked; MiMo-V2.6-Flash and MiniMax-M3.1-Flash lack Bug Hunt after the logged search and are listed (O38, O41).

## Editor decisions (2026-10-23, implementing O45–O51)
- E247 (O47 re-freeze): anchor version v3-2026-10-23 over the 29-configuration cohort. API anchors 4.19 / 12,078 USD (27 complete-evidence references); Plan anchors 0.239 / 3,716 USD over plan rows (O48). Bars: headline 48.92 (GPT-6.1 Sol (medium)), lower quartile 32.26, upper quartile 54.99. No dual run is possible: the main workload changed (Coding Agent Index v1 left the basket when AA replaced it with v2.0, which is pending under O50), so this is a workload migration (E184) and the engine refuses to score on the previous anchors; the previous anchor object is kept as `v3-frozen-2026-10-21-before-o47.json`.
- E248 (O48): a configuration's plan rows stay in one noise band. Their order is certain (one configuration, one quality, a cost ratio fixed by the multiples), but a row between them cannot be told apart from either, so a band that starts at one of a configuration's plan rows extends over its other plan rows.
- E249 (O48): the official Plan anchors are set over plan rows, so the measured-evidence calibration (E164) reads each anchor setter's evidence from its plan row. Today: Claude Haiku 5.5 (low) on Claude Pro (owner-named transfer) and Gemini 4 Argon (high) on API-cost fallback.
- E250 (O49): DeepSWE's chart and per-configuration results stay in the raw data as "withdrawn by AA, not scored"; no DeepSWE result enters quality, sampling noise, cohort membership or any diagnostic.
- E251 (O51): the cohort exclusion reason is "not plotted on or within the near gap of AA's rendered frontier"; the E193 family rule (frontier family ranks its highest rendered point, near family its smallest-gap near point) chooses each family's primary for the one-row-per-family diagnostics; other plotted efforts of a family are ranked rows in their own right.

## Owner decision (2026-10-23, after the SWE benchmark research)
- O52. Shown that no benchmark outside AA covers the 29-configuration cohort at exact effort (`research/2026-10-23-swe-benchmarks/reports/SWE benchmark candidates.md`), the owner answered that the cohort does not determine the spread of benchmarks: ValueRank picks the benchmarks, and the configurations that have all of them are ranked, balancing the number of benchmarks against the number of configurations ranked. Surge's Complex Constraints replaces IFBench, which ValueRank used to include; outside software engineering it takes at least 5% of quality. Vals.ai's benchmarks are to be browsed one by one and the ones to include chosen. Next: an exact-effort coverage matrix of the candidate benchmarks over the AA frontier and near-frontier configurations, and the benchmark-set options it supports, go to the owner.
- O53. Shown the coverage grid (addendum to `research/2026-10-23-swe-benchmarks/reports/SWE benchmark candidates.md`), the owner chose "Two rankings": a max-effort ranking (the ten leaves plus LiveBench 2.0 Coding and Long Agentic, Vals Vibe Code Bench v1.1 and Vals Code Migration v1.1; 8 configurations exact today, one per family at its top effort) and an AI Coding Daily ranking (the ten leaves plus AI Coding Daily without its bug-finding column; 14 configurations exact today, mostly high and medium efforts), each ranking the configurations that have its complete set. Surge's Complex Constraints is excluded and its instruction-following weight dropped for now (3 of 29 configurations covered), to be revisited on each refresh.
- O54. Asked whether to use CursorBench 4.0 (13 configurations exact) and Surge's sudo L7 (5, all in the max-effort set), the owner chose to exclude both. Asked which ranking leads, the owner chose the max-effort ranking first (site and README default; the AI Coding Daily ranking is the second view). Asked how MiMo-V2.6-Pro's effort-unlabelled results map, the owner stated that AA's configuration is high: AI Coding Daily's and LiveBench's "high" rows are its exact configuration. E252: Vals records MiMo-V2.6-Pro with reasoning enabled and no level; MiMo-V2.6-Pro exposes thinking as one mode (third-party model configs map only "high"; Xiaomi documents no effort tiers), so Vals' run is the same high configuration, labelled "reasoning enabled; effort taken as high (owner, O54)". MiMo-V2.6-Pro is therefore in both rankings (max-effort 9, AI Coding Daily 15).
- O55. Weights. Max-effort ranking, software engineering 60%: FrontierCode 18, Terminal-Bench 14, Bug Hunt 10, Vals Vibe Code Bench v1.1 5, Vals Code Migration v1.1 6, LiveBench 2.0 Long Agentic 5, LiveBench 2.0 Coding 2. AI Coding Daily ranking, software engineering 60%: FrontierCode 21, Terminal-Bench 17, Bug Hunt 12, AI Coding Daily (60 points, bug finding excluded) 10. The other domains keep their weights in both rankings. Before implementation the owner asked for Epoch MirrorCode, SWE-bench-Live and SWE-PolyBench to be checked for exact-effort coverage.
- O55 follow-up (2026-10-23): Epoch MirrorCode covers 3 cohort configurations, SWE-bench-Live and SWE-PolyBench none at exact version and effort (report addendum); the benchmark sets stand.

## Editor decisions (2026-10-23, implementing O52–O55)
- E253 (O53): each ranking is scored by the same engine on its own leaf table (`quality.TRACKS`), with its own frozen anchors (`v3_frozen.json` for the max-effort ranking, `v3_frozen_aicd.json`, anchor version `v3-2026-10-23-aicd`), quality bars, scenario run (`v3_scenarios_aicd.json`), admission and diagnostics; scores.json carries the leading ranking as `v3` and the other as `v3Tracks.aicd`. Values compare within a ranking only.
- E254 (O53, E140): basket admission is decided within each ranking's ranked rows. The Coding Agent Index v2.0 is priced for 7 of the max-effort ranking's 9 rows, so it is admitted there and DeepSeek V4.1 Flash 1017 and MiMo-V2.6-Pro are scored on their own subset workload, flagged (O17); in the AI Coding Daily ranking it covers 2 of 15 and stays pending.
- E255 (O36, O53): a cohort configuration is ranked in every ranking whose full set it has; it is excluded (listed under O38 with its searches) only when it lacks every ranking's set. Every missing (configuration, added leaf) pair carries a logged search with the coverage research as its open-web step (`research/2026-10-23-swe-benchmarks/add_track_searches.py`).
- E256 (O39): the added leaves' sampling noise is Vals' published standard error for the Vals boards, and the independent-task approximation over LiveBench 2.0's task counts (Coding 29, Long Agentic 18) and AI Coding Daily's six graded projects (an assumption, labelled).
- E257: the added leaves' evidence is `data/swe_tracks.json`, built by `research/2026-10-23-swe-benchmarks/build_swe_tracks.py` from the verified coverage captures; exact configuration only, with MiMo-V2.6-Pro matched at high (O54, E252).

## Owner decision (2026-10-23, review convergence)
- O56. For the remaining review rounds (the internal Claude ladder and the Perplexity panel), a round is clean when it raises no finding of medium or higher severity; low-severity findings and design suggestions are considered but do not make a round non-clean. Asked how this applies, the owner chose per rung: every rung of the internal ladder (Claude Sonnet 5.5 at low, medium, high, xhigh and max effort, then Claude Opus 5.5 at the same efforts) and every Perplexity panel model (GPT-6.1 Sol, Gemini 3.8 Flash, Claude Sonnet 5.5, Kimi K3, GLM 5.3, Grok 4.7) is done after two consecutive clean rounds; a rung's non-clean round is answered with a new draft before its next round.

## Editor decision (2026-10-23, from the r88 drafting)
- E258: (a) On the Plan basis, adjacent plan rows of one configuration are ordered by their plans' multiples alone; they are counted apart (`sameConfigurationAdjacentPairs`), and the separability threshold, its median, the separable count and the E242 transfer tolerance range over adjacent pairs of different configurations, so a configuration's many plan rows no longer pull the median threshold to zero (it had printed a tolerance of 1.0). (b) A publisher of two or more independently run leaves in a ranking is a multi-leaf source with its own leave-one-source-out branch (E146): Vals AI and LiveBench in the max-effort ranking. (c) The S1T task-count list names the added leaves and drops DeepSWE.
- Draft r88 (written from r87 for I28 and O45–O56; about 65 lines changed).

## Internal review I29 (Claude Sonnet 5.5, effort low, on r88) — adopted, modified or rejected
- M1 (adopted): r88 was written before E258, so its Plan separability figures (median 0.00, 16 of 26 and 31 of 49, grid 16/31, tolerance 1.0) and the note that the Vals and LiveBench branches were unpublished were stale; r89 states E258 and the current figures (max-effort Plan median 3.01, 2 of 11, grid 2 / 2 / 2, tolerance 2.35; AI Coding Daily 4.54, 1 of 19, grid 1 / 1 / 1, tolerance 5.28; 15 and 30 same-configuration pairs counted apart).
- L1 (adopted, widened): r88 named Claude Haiku 5.5 (low), Claude Opus 5.5 (medium) and Claude Sonnet 5.5 (xhigh) as near-family primaries; they are near points of frontier families. r89 lists the near families' primaries (GPT-5.6 Luna (low), Gemini 4 Argon (high), GPT-6 Astra (xhigh), DeepSeek V4.1 Flash 1017 (max), MiniMax-M3.1-Flash) and the listed primaries (Claude Haiku 5.5 (xhigh), MiMo-V2.6-Flash, GPT-6 Astra (xhigh), MiniMax-M3.1-Flash).
- L2 (adopted): the noise margin is on the quality scale and the separability threshold on the value scale, hence the ratio of about 1/0.75; one clause says so.
- L3 (rejected): the revision history is the draft's standing record of each revision, kept by convention since r16.
- Round status (O56): not clean (one Medium). Draft r89.

## Internal review I30 (Claude Sonnet 5.5, effort low, on r89) — adopted, modified or rejected
- M1 (adopted): the list of frontier families' near points omitted Claude Haiku 5.5 (max) (gap 3, the Haiku row ranked in the max-effort ranking); r90 adds it.
- L1 (adopted): E254's per-ranking admission is now stated as an editor reading of O15/E140's "two-thirds of the cohort", with its effect (the Coding Agent Index v2.0 covers 7 of the max-effort ranking's 9 rows but 7 of all 29 cohort configurations) and that the owner can reverse it.
- Round status (O56): not clean (one Medium). Draft r90.
- O57 (2026-10-23). Asked whether O15's "two-thirds of the cohort" counts each ranking's rows or all 29 cohort configurations, the owner chose "Per ranking": E254 stands as an owner decision; the Coding Agent Index v2.0 is admitted in the max-effort ranking and pending in the AI Coding Daily ranking.

## Internal review I31 (Claude Sonnet 5.5, effort low, on r90) — adopted, modified or rejected
- Round status (O56): clean (no Medium or higher; four Low). First clean round at the Sonnet-low rung.
- L1 (adopted): E196's headline states how a negative cost allocation prints (as it is, with the sentence that cost then offsets quality; the AI Coding Daily ranking today about −90% API, −26% Plan); the emitter already prints it so.
- L2 (adopted): E248's plan-row band extension is bounded: a row of another configuration separable from the band's first row starts a new band, so the invariant holds for every row of another configuration; today no configuration's plan rows span the threshold.
- L3 (adopted): the re-frozen anchor figures are named as the padded c_L and c_H.
- L4 (resolved by O57): the per-ranking admission reading went to the owner, who chose it; r91 states it as O57.
- Draft r91.

## Internal review I32 (Claude Sonnet 5.5, effort low, on r91) — adopted, modified or rejected
- Round status (O56): clean (no Medium or higher; four Low). Second consecutive clean round: the Sonnet-low rung is complete.
- L1 (adopted): the remaining three listed configurations (Claude Opus 5.5 (xhigh), GPT-6.1 Sol (xhigh), GPT-6 Luna (low)) are placed as non-primary rendered-frontier points of ranked families.
- L2 (adopted): the band sentence is split and today's bands get their own sentence.
- L3 (rejected): repeat of I29 L3 without a new argument.
- L4 (adopted): the bar-reach counts say which population they count and why the interval outputs' lower-bar count is 5 (two rows on the subset workload).
- Draft r92.

## Internal review I33 (Claude Sonnet 5.5, effort medium, on r92) — adopted, modified or rejected
- M1 (adopted as E259; the owner question was not needed): "listed" had two senses. E259: a configuration is *listed beside a ranking* when it lacks that ranking's full set (today 20 and 14) and *excluded* (O38) only when it lacks both (today 9); O41's indicative value is shown beside each ranking for every configuration listed there, on that ranking's leaves and anchors, as the build already does. This applies O41 within each ranking created by O53 and changes no score; r93 also gives MiniMax-M3.1-Flash's indicative values beside MiMo-V2.6-Flash's.
- L1 (adopted): SD_i in the separability formula is named as 0.75 × the row's quality SD, on the value scale.
- L2 (adopted): IFBench's "1 of 19" is dated to O26 (2026-10-19).
- L3 (adopted): MiniMax joins the next end-user report search; its only cohort configuration is excluded, so no Plan row is affected today.
- L4 (adopted): bar triples are given as lower, headline, upper throughout.
- L5 (adopted): the Cost section's per-ranking admission cites O57.
- Round status (O56): not clean (one Medium). Draft r93.

## Internal review I34 (Claude Sonnet 5.5, effort medium, on r93) — adopted, modified or rejected
- M1 (adopted): the AI Coding Daily one-row-per-family ladder was still printed headline-first under the declared lower/headline/upper order; r94 prints 42.8 / 49.2 / 52.8 against the frozen 38.0 / 49.2 / 57.2.
- L1 (adopted): the frontier primary is the dearest of the family's rendered-frontier points, not of all its plotted points (Claude Haiku 5.5 (max), a near point, costs more today).
- L2 (adopted): the O44 margin names its SD as the same per-row analytic quality SD the separability threshold scales by 0.75.
- L3 (adopted): MiniMax's indicative Plan value is its API cost on the Plan anchors; "no Plan row" now reads "no ranked Plan row".
- L4 (adopted): the basket version names the target basket and admission rule; the two rankings' admitted sets share it and differ by components and workload hash.
- L5 (adopted): E240 applies to every cohort configuration listed beside a ranking (E259); a listed configuration gets no rank and no value score in that ranking, only O41's indicative value.
- Round status (O56): not clean (one Medium). Draft r94.

## Internal review I35 (Claude Sonnet 5.5, effort medium, on r94) — adopted, modified or rejected
- M1 (adopted, no owner question needed): E246 is general (a SemiAnalysis figure without an effort binds to the model's max row), but r94 stated it only inside the GPT bullet. r95 states it for Claude: Opus 5.5's measured figures bind to Claude Opus 5.5 (max); Claude Opus 5.5 (high) and (medium), like every other Claude row, take the owner-named common Claude assumption (AGENTS.md, 2026-10-18), as the build already does.
- L1 (adopted): the AI Coding Daily ranking's basket has no coding-agent component, but Terminal-Bench 4.0's Index run is agentic; wording fixed.
- L2 (adopted): AGENTS.md now says admission is counted within each ranking's rows (O57).
- L3 (adopted as E260, code changed): the FrontierCode AA-against-Cognition comparison ranges over every cohort configuration with both results (ranked or listed in the ranking), so both rankings use one panel and one offset; today 7 configurations, τ_b 0.81, mean offset 1.52, largest 6.28. Bar results with lowered fills are unchanged.
- L4 (adopted as E261): an O46 quota ceiling's evidence date is the capture of Xiaomi's tier, fee and rate pages; each refresh that re-captures them renews it; the authorisation does not expire; an end-user measurement replaces it.
- L5 (adopted): indicative costs clip at the frozen anchors like any cost score (Claude Opus 5.5 (max) and Claude Sonnet 5.5 (max) show API cost score 0 beside the AI Coding Daily ranking).
- L6 (adopted): bands are built forward only, so a configuration's plan rows can straddle a band boundary (GPT-6 Luna (max), GPT-6.1 Sol (medium) today).
- Round status (O56): not clean (one Medium). Draft r95.

## Owner decision O58 (2026-10-23): listed rows and the clip gate
- Asked (Questions UI) whether a listed configuration beyond a ranking's anchors (today GPT-6 Luna (low), a rendered-frontier point, 4.75 times below the max-effort ranking's subset-workload low anchor) should be able to hold the release, the owner chose "No — disclose only (Recommended)". The clip gate counts ranked rows only, as the build already did; the gate output discloses every listed row beyond its workload's anchors with basis, side, factor, the factor-2 test and a rendered-frontier marker (scores.json `gates.listedBeyondAnchors`), and methodology.md prints the API list per ranking.

## Internal review I36 (Claude Sonnet 5.5, effort medium, on r95) — adopted, modified or rejected
- M1 (adopted with owner decision O58): the clip gate's population read onto listed rows. r96 says n and the clip test range over ranked rows, adds the O58 disclosure with today's figures, and a fixture shows a listed rendered-frontier row five times below the low anchor disclosed and not holding. Modified: the reviewer's "about 7.5 times" measured GPT-6 Luna (low) against the main workload's low anchor; the row is on the subset workload, whose anchor it lies 4.75 times below.
- L1 (adopted as E262, code changed): gates run per ranking on its own anchor objects and rows; the rankings publish together, so a hold in either holds the release, and scores.json `releaseHold` names the held rankings (none today).
- L2 (adopted): GPT-6 Astra (high) and (max), both at gap 3, named as the remaining near points, completing the 11.
- L3 (adopted): "listed" replaced by "excluded (O38)" for the nine configurations without either ranking's set.
- L4 (adopted): the bar-currency count sentence rewritten.
- Round status (O56): not clean (one Medium). Draft r96.

## Internal review I37 (Claude Sonnet 5.5, effort medium, on r96) — adopted, modified or rejected
- M1 (adopted as E263, code changed): AI Coding Daily's S1T noise is stated as n = 6 (its graded projects) with p = points ÷ 60, the wide reading; the n = 60 narrow reading is computed beside each separability figure (`aicdNarrow`) and printed with the AI Coding Daily ranking (today median threshold 3.2 API and 3.2 Plan against 4.4 and 4.5; 1 of 14 and 1 of 19 adjacent ranks separable either way). The sample SD of the six project scores replaces both once per-project points are captured. The reviewer's leaf-variance-share diagnostic (its recommendation 2) is not adopted now: the narrow reading already shows how much rests on the assumption.
- L1 (adopted): the O44 margin's median is over the ranking's configurations, one value each, the same on both bases (as built).
- L2 (adopted): the O58 "today" list marks every listed row past the factor-2 limit and every rendered-frontier point.
- L3 (adopted): Output 1 names the O46 quota ceilings and measured multiples with unidentified M_W.
- L4 (adopted): an anchor object is identified by anchor version, basis and workload hash; the max-effort subset workload and the AI Coding Daily main workload share a hash but are different anchor objects.
- Round status (O56): not clean (one Medium). Draft r97.

## Internal review I38 (Claude Sonnet 5.5, effort medium, on r97) — adopted, modified or rejected
- M1 (adopted, code changed): the E214 premise was stale; AA plots Claude Haiku 5.5 without "with fallback" (Opus 5.5 and Sonnet 5.5 carry it). r98 states the naming as observed, the matching rule (model and effort; stop on a with/without twin) is unchanged, and the build now reads the plotted-name state from the capture (scores.json `aaPlottedNames`: with fallback, without, no effort) and prints it in methodology.md's cohort section, so it cannot go stale (the reviewer's recommendation 1).
- L1 (adopted): today's drift result stated (AI Coding Daily knowledge group flagged, 4.6% against 10%; max-effort no flag, AA-LCR non-discriminating).
- L2 (adopted, code changed): the value-variance allocation is withheld below three rows (`MIN_ALLOCATION_ROWS`), where a two-row split is fixed by construction; the SD ratio still prints from two rows.
- L3 (adopted): two decimals for the separability medians in the n = 60 sentence.
- L4 (rejected for now): splitting Output 1 into sub-bullets is presentation only; every item in it is consistent with the data, and a restructure would disturb the text later rungs compare against. Revisit in the final editorial pass.
- L5 (adopted): the Terminal-Bench agent list is "observed on the captured leaderboard".
- Round status (O56): not clean (one Medium). Draft r98.

## Owner decisions O59 and O60 (2026-10-23): non-AA source clocks
- Asked (Questions UI) for a maximum capture age for non-AA quality evidence, the owner chose 30 days (O59), matching the report window, over 7 days.
- Asked how to treat a capture taken after the release cutoff, the owner chose "Allow if source predates (Recommended)" (O60): it stands when the source's own last-update date is before the cutoff's day; the build fails otherwise.

## Internal review I39 (Claude Sonnet 5.5, effort medium, on r98) — adopted, modified or rejected
- M1 (adopted with O59 and O60, code changed): the non-AA sources had no capture clock. The engine now records each source's capture instant and last-update date (`sourceClocks`) and fails on a capture older than 30 days or on a post-cutoff capture whose source does not predate the cutoff's day; methodology.md prints the clocks under the leaf table. `data/swe_tracks.json` is re-stamped from the raw captures (Vals 07:58:05Z, LiveBench and AI Coding Daily 07:58:31Z) instead of a nominal 08:00Z; the Bug Hunt scoreboard records its source update (2026-10-19). Today every source passes. Modified: the owner chose 30 days, not the reviewer's suggested 7, and allowed post-cutoff captures of boards that predate the cutoff rather than requiring capture at or before V.
- L1 (adopted): O56 wording says two consecutive clean rounds per rung and per Perplexity model.
- L2 (adopted): C_W includes the Coding Agent Index where admitted.
- L3 (adopted, modified): the noise-margin sentence says the 4.0 and 5.9 are the margin; the median SDs are 1.45 and 2.12 (the reviewer's 2.07 recomputed from 5.87 ÷ (1.96 × √2)).
- L4 (adopted): an explicit "without fallback" record for a model AA plots only with fallback does not match without a dated decision.
- L5 (adopted): the plan-row separation statement is scoped to scenario shares, with a pointer to E258.
- Design recommendations 2–4 (figure lint, Bug Hunt √N sensitivity, DeepSeek harness delta) not adopted this round: recorded for the owner report; the DeepSeek V4.1 Flash 1017 harness tie is already listed for owner review.
- Round status (O56): not clean (one Medium). Draft r99.

## Internal review I40 (Claude Sonnet 5.5, effort medium, on r99) — adopted, modified or rejected
- No Critical, High or Medium finding (VERDICT: NO FURTHER FEEDBACK).
- L1 (adopted): each adjacent pair is tested against its own threshold; the median is a summary.
- L2 (adopted): O59/O60 arithmetic stated (whole UTC days, strict threshold, as E212; a date-only stamp on the cutoff's day is not after it; a post-cutoff capture with no recorded source update fails, already a fixture).
- L3 (adopted): the max-effort ranking holds at most one configuration per family, 9 of the 12 families.
- L4 (adopted, code changed): scores.json's cohort object names the frontier capture as its source and date; the top-level DeepSWE fields carry "withdrawn by AA (O49), kept as raw data, not scored (E250)".
- Round status (O56): clean, the first at this rung. Draft r100.

## Internal review I41 (Claude Sonnet 5.5, effort medium, on r100) — adopted, modified or rejected
- No Critical, High or Medium finding (VERDICT: NO FURTHER FEEDBACK).
- L1 (adopted, code changed): scores.json's cohort counts renamed to what they now are: `rosterN` (AA-mapped roster rows) and `otherPlottedEffortN` (plotted on/near configurations that are not a family primary), replacing `sourceN` and `exactBenchmarkOverlapN` from the withdrawn retention route.
- L2 (rejected for now): moving the revision history below the body is presentation; left for the final editorial pass with I38 L4.
- L3 (adopted): AGENTS.md separates the owner's exclusions (Surge Complex Constraints dropped for now; CursorBench and sudo L7 excluded) from the benchmarks with too few exact configurations.
- Round status (O56): clean, the second consecutive clean round at this rung. The Claude Sonnet 5.5 medium rung is complete; the next rung is Claude Sonnet 5.5 at high effort, on r100 (I41 changed no draft text).

## Owner decision O61 (2026-10-23): LiveBench 2.0 Overall replaces its two categories
- The owner: "instead of just the 2 LB categories, we need to incorporate the LiveBench 'Overall' score, since all its categories are required in SDLC." Asked for its weight, the owner said LiveBench "needs to get more % than AA Intelligence Score's % since LB is a non-contaminated benchmark whereas AA's benchmarks are mostly contaminated", LiveBench preferably within software engineering. Clarified (Questions UI), the owner chose "LB above each AA leaf": the AA component leaves stay, and LiveBench 2.0 Overall enters software engineering at 15, above every single AA leaf. Max-effort ranking only ("Max-effort only (Recommended)"): LiveBench runs each model once at its top effort, so only 6 of the AI Coding Daily ranking's 15 configurations have it.
- Weights, max-effort ranking: FrontierCode 15, Terminal-Bench 11, Bug Hunt 8, Vibe Code 5, Code Migration 6, LiveBench 2.0 Overall 15 (software engineering 60); the other groups unchanged. Source split 66% AA-run, 34% independent.
- LiveBench 2.0 Overall is the plain mean of its seven category scores (Long Agentic, Reasoning, Coding, Browser, Data Analysis, Research, Design) to two decimals, as LiveBench's site computes it with no category filter (function `ot` in the captured bundle main.074b2ee8.js); the values come from the captured release table (2026-10-14, updated 2026-10-18). All 9 max-effort configurations have it.

## Editor decision E264 (2026-10-23): LiveBench 2.0 Overall sampling noise
- The S1T stream reads LiveBench 2.0 Overall as the mean of seven binomial category shares, SD = (100 / 7) × √Σ p̃_c(1 − p̃_c)/n_c, with LiveBench's published task counts (Long Agentic 18, Coding 29, Browser 25, Research 22, Design 25). Reasoning and Data Analysis publish only their parts (4 and 3), each holding several short questions; reading them as 4 and 3 trials overstates their noise (the wide reading, as E263 does for AI Coding Daily). LiveBench becomes a single-leaf source in the deletion branches (E258).

## Owner decision O62 (2026-10-23): replacing an O46 quota ceiling
- Asked (I42 L5) whether one end-user report replaces a MiMo tier's quota ceiling, the owner chose "Same bar as O11 (Recommended)": the ceiling is replaced once the tier's end-user evidence meets the admission rule of any other provider's route; one stray report does not swap it.

## Internal review I42 (Claude Sonnet 5.5, effort high, on r100) — adopted, modified or rejected
- No Critical, High or Medium finding (VERDICT: NO FURTHER FEEDBACK): clean, the first round at this rung. O61 then changed the max-effort ranking's leaves and weights, so the second round runs on r101 and must be clean on the new text.
- L1 (adopted): the E238 example of a change that stays diagnostic no longer cites a model's multiples being added (O40 replaces the transfer at once).
- L2 (adopted, wording): the Terminal-Bench cross-source panel is per ranking, unlike FrontierCode's cohort-wide one (E260); r101 says so, and says why the AI Coding Daily ranking prints it undefined on one row.
- L3 (adopted): the E242 tolerance is quoted for the main workload; the subset-workload rows' tolerance is stated beside it.
- L4 (adopted): separability counts and noise bands span both anchor objects of the max-effort ranking; stated.
- L5 (owner question, answered as O62).

## Editor decision E265 (2026-10-23, owner instruction): remove the stale-figure finding class at its source
- The owner asked that the recurring class of "stale figures in the prose" findings (I29 M1, I34 M1, I38 M1 and several Lows) be eliminated at the source rather than rediscovered each round: "When a pattern of recurring, low-yield findings shows up, eliminate it at the source; don't let later rounds keep rediscovering it."
- From r101 the draft is written as a source, `draft-rNNN.src.md`, whose current-release figures are placeholders (`{{max:PATH|FORMAT}}`, `{{aicd:…}}`, `{{top:…}}` over data/scores.json, and `{{fig:NAME}}` over the figures manifest data/figures.json, both rankings). `python3 -m valuerank.draft_figures render` writes the published `draft-rNNN.md`; `npm run build:docs` rebuilds the manifest; `python3 -m valuerank.draft_figures check` runs in the tests and in `npm run verify:docs` and fails when the published draft is not the rendering of its source against current data, a placeholder does not resolve, the manifest is stale, a sentence that speaks of today carries an unmarked figure or effort-qualified configuration name, or an undated sentence carries an "N of M" count.
- External facts are build figures too: AA's plotted naming (`aaPlottedNames`), cohort and family counts and the primary/near-point lists from the AA capture and roster, which configurations each ranking ranks, lists and excludes, gap-filled rows, clipped indicative rows, O58 rows beyond the anchors, MiMo quota ceilings from the route registry, source-clock instants, and the drift and non-discriminating flags.
- Fewer figures: where a number only illustrates a rule (bands, calibration anchors, harness counts, displayed-cheapest results, noise-margin companions, the E205 ladder, basket shares, indicative values), the text now points to README.md, methodology.md, scores.md or scores.json instead of copying it.
- The sweep found figures that O61 had already made stale in r100 (e.g. the max-effort separability median 3.01 → 2.84 and 1 → 0 separable API pairs, the band straddler GPT-6 Luna (max) → GPT-6 Astra (max), the bar ladder 49.8/60.7/62.1 → 54.2/64.3/65.0, source shares 72/28 → 66/34): all are placeholders now.
- One editorial pass for the deferred presentation Lows: Output 1 is split into labelled sub-bullets (I38 L4) and the revision history moved below the body (I41 L2); the lint does not read the revision history, which records past drafts' figures as they were.
- Guard: this removes the defect class, it does not suppress reviewers. A stale current figure a reviewer still finds is a bug in the check, to be fixed in `valuerank/draft_figures.py` with a test.

## Internal review I43 (Claude Sonnet 5.5, effort high, on r101) — adopted, modified or rejected
- M1 (adopted; defect in the source and in the check): "the max-effort ranking has 14 leaves" was hard-coded and stale (13 since O61). Now a placeholder; the check is widened (E265 amended): a number counting cohort things (configurations, rows, leaves, references, families, points, components), a dollar amount, and an "N against M" count are figures in any sentence not dated before the release day, and a date in a bold rule label or on the release day no longer dates a sentence. The widened check found and the source now renders the cohort counts, the qualifier counts and setters, and the leaf counts.
- M2 (adopted): the dated re-freeze history quoted the pre-O61 max-effort ladder as if current. r102 states that O61 re-froze the max-effort bars on the same anchor version (cost anchors unchanged) and points to Output 3 and `barCurrency` for the current ladders.
- M3 (owner question, answered): the O61 option offered "above every single AA leaf" at 15 while FrontierCode is also 15. Asked (Questions UI), the owner chose "Keep the 15/15 tie": LiveBench 2.0 Overall weighs no less than any single AA leaf and ties FrontierCode; AGENTS.md, the code comment, methodology.md and the draft say so.
- L1 (adopted): the E265 governance text now says what the check enforces, not more.
- L2 (adopted): the exchange-rate and within-cohort-influence definitions moved from the noise-band bullet into the cost-weight disclosure bullet (E60).
- L3 (adopted): E264's formula is written in the draft.
- L4 (adopted): O55 is cited "as amended for the max-effort ranking by O61".
- L5 (adopted): the untested remark that Vibe Code Bench separates little is replaced by a pointer to the published leaf spreads.
- Round status (O56): not clean (three Mediums). Draft r102. The Sonnet high rung's clean count restarts at zero (I42 was clean on r100; I43 is not).

## Internal review I44 (Claude Sonnet 5.5, effort high, on r102) — adopted, modified or rejected
- No Critical, High or Medium finding (VERDICT: NO FURTHER FEEDBACK): clean, the first clean round at this rung after I43.
- L1 (adopted; a defect in the check, fixed): the AI Coding Daily ranking's Plan anchor setters were hand-written and the lint read configuration names only in "today" sentences. The check (E265) now also flags a configuration named with a plan route ("<configuration> on <plan>" or "on API-cost fallback") in any sentence not dated before the release day; the sentence now points to scores.md for each ranking.
- L2 (adopted): Plan anchor references are every plan row of the reference configurations at its displayed Plan cost (O48), in both places.
- L3 (adopted): the rendered-frontier Index ties are a build figure (`aa.frontierIndexTies`), today including Claude Haiku 5.5 (high).
- L4 (adopted): the typographical slip fixed and the duplicate build-check sentence removed.
- L5 (adopted): the Normative section says which definitions are per ranking and which are common.
- L6 (adopted): internal review labels removed from the specification's body (the ledger keeps them).
- Section 2 recommendations: generating the remaining hand-written current-state statements is the E265 path and continues as the check finds them; a flag for ladder bars closer than the noise margin and counting transfers among Plan anchor references are recorded for the owner report, not adopted now.
- Round status (O56): clean, the first at the Claude Sonnet 5.5 high rung. Draft r103.

## Internal review I45 (Claude Sonnet 5.5, effort high, on r103) — adopted, modified or rejected
- No Critical, High or Medium finding (VERDICT: NO FURTHER FEEDBACK).
- L1 (adopted): the display-name convention is stated: the specification writes "Family (effort)", the published tables use AA's display name, which omits the effort where AA does.
- L2 (adopted): E196 also explains an allocation above 100% (the other term then negative).
- L3 (adopted): the clipped indicative rows are given on both bases (new figure `<ranking>.indicativeClipped.plan`).
- L4 (recorded for the owner report): a subset-workload leader carries "(subset cost)" in the headline; adding "cross-workload ordering not identified" to the headline is a presentation choice left to the owner.
- L5 (rejected for now): E248's band extension overlapping another band is not reachable today (no configuration's plan rows span the threshold, a build figure); revisit if that figure stops being "none".
- L6 (recorded): README's "Updated" date is the v3.0.0 release date (`release.DATE`), not the data cutoff; the cutoff is stated beside it. "9 cohort configurations" in the README scope line is the README's wording for cohort rows.
- Round status (O56): clean, the second consecutive clean round at the Claude Sonnet 5.5 high rung (I44, I45). The rung is complete; the next rung is Claude Sonnet 5.5 at xhigh effort, on r104.

## Internal review I46 (Claude Sonnet 5.5, effort xhigh, on r104) — adopted, modified or rejected
- M1 (adopted as E266, docs changed): the scenario panel is the ranking's main-workload rows (as built, E96); a subset-workload row (today DeepSeek V4.1 Flash 1017 (max) and MiMo-V2.6-Pro in the max-effort ranking) gets no scenario share. r105 states it, and scores.md now names such rows above the scenario tables, so a subset-workload API leader is never shown as absent from rank 1 without the reason.
- M2 (adopted): the transfers-off streams remove every Plan row whose selected route rests on an owner assumption — an owner-named transfer or an O46 MiMo quota ceiling, both graded "assumption" by the build — as built; r105 says so.
- L1 (adopted, data changed): the O46 replacement wording in E261, methodology.md (via plan_cost_routes.json `mimoApplication`) and the draft now follows O62 (the O11 admission rule; one report alone does not replace a ceiling).
- L2 (adopted): the display-name sentence attributes the bare names to the roster, not to AA.
- L3 (adopted): the clipped-Plan clause names its rankings.
- L4 (adopted): the "no interval enters any stream" sentence excepts GDPval-AA's interval in S1T.
- L5 (recorded): true hand-written facts outside the figure check's reach (the MiMo-V2.6-Flash and MiniMax-M3.1-Flash Bug Hunt gap) remain; the check grows when one goes stale.
- L6 (recorded): stale notes in data and code comments are left for the release tidy-up; they change no output.
- L7 (adopted): "same rows" is scoped to the main workload.
- Round status (O56): not clean (two Mediums). Draft r105.

## Internal review I47 (Claude Sonnet 5.5, effort xhigh, on r105) — adopted, modified or rejected
- M1 (adopted, docs changed): scores.md printed only the leading ranking's interval outputs, scenario shares, calibration and diagnostics, so the draft's per-ranking pointers did not resolve for the AI Coding Daily ranking and some published statements were wrong for it. scores.md now prints, under the AI Coding Daily ranking, its calibration, interval outputs (with the E201c sibling lists), scenario shares (with the E266 panel note) and diagnostics (with its gap-fill removal sensitivity); the draft's pointers name scores.md under each ranking, or the scores.json field; the site's API basket description says the Coding Agent Index enters "where the ranking admits it".
- L1 (adopted): README's allocation sentence explains an allocation above 100% (quality's term negative) as E196 requires.
- L2 (adopted): the unevaluated-sibling reason reads "lacking its full benchmark set, or not plotted on or near the frontier".
- L3 (adopted): methodology.md states the Coding Agent Index cost as AA's unrounded mean cost per task × 290.
- L4 (adopted): the published transfers-off, separability and † texts name owner assumptions (owner-named transfers and O46 quota ceilings).
- L5 (recorded): the "valuation basis unverified" label is shared by E138 and E202 by design; their reasons are printed beside it.
- L6 (recorded): the subscription-policy prose's O31/O33 history is kept as history in plan_cost_routes.json; tidy at release.
- L7 (adopted): the scenario-panel note prints the panel size, and Output 1 says a subset-workload row has no share.
- Round status (O56): not clean (one Medium). Draft r106.

## Internal review I48 (Claude Sonnet 5.5, effort xhigh, on r106) — adopted, modified or rejected
- M1 (adopted; a recurring class, removed at the source under E265): broken pointers to generated documents were raised twice (I47 M1, I48 M1). The check now enforces two rules: every sentence that sends the reader to README.md, scores.md, methodology.md or raw-data.md also names the scores.json field it reads, and every cited scores.json field resolves in every ranking's section (or the file's root; `<basis>` and `[]` stand for each basis and list item). The docs now print what the pointers promise: scores.md prints, under the AI Coding Daily ranking, its displayed-record results (E203), noise-margin companions (O44), separability statement and indicative values (O41, with the O43 sentence); README's basket and leaf statements say they describe the leading ranking and give each ranking's leaf count; the glossary's "leaf of 20% or more" is ranking-relative.
- M2 (adopted, docs changed): the README explanation of an allocation above 100% had the covariance sign backwards. It now says dearer configurations score higher on quality, so quality differences partly offset cost differences; the draft's E196 parenthetical says the same, so both readers print one explanation.
- L1 (recorded): the AGENTS.md quotation of "the selected subscription route" predates O48's one row per plan; to be aligned at the next AGENTS.md amendment.
- L2 (adopted in part): the AI Coding Daily block in scores.md is labelled per section; reordering the max-effort sections is left for the release tidy-up.
- L3 (recorded): the scenario-panel note counts configurations; the Plan tables' plan rows are named in their own headers.
- L4 (adopted): the provisional-quality glossary no longer names Terminal-Bench as a 20% leaf.
- L5 (recorded): the Plan route table's grade label for O46 ceilings still reads as a transfer; the published streams, † and separability texts now say owner assumption.
- L6 (recorded): two hand-written report-search facts remain outside the check's reach.
- L7 (recorded): release-gate Detail cells describe the rule even when it passes, by design.
- Round status (O56): not clean (two Mediums). Draft r107.

## Internal review I49 (Claude Sonnet 5.5, effort xhigh, on r107) — adopted, modified or rejected
- M1 (adopted, docs changed): the E227 harness line counted Bug Hunt over the configurations ranked in either ranking and omitted AI Coding Daily's harnesses. It now counts each ranking's own rows (today 9 and 15) and reads AI Coding Daily's harness from each record's note, which the evidence now carries in its provenance.
- M2 (adopted; the pointer class removed at the source, E265 amended): pointers to generated documents were the Medium of three rounds (I47, I48, I49), because no check can verify that a document prints what a sentence promises. The specification now cites only scores.json fields, which every generated document is rendered from and which the check resolves in every ranking; the check fails on any mention of README.md, scores.md, methodology.md or raw-data.md in the specification's body. The unproduced "extends to the selected cohort" statement is replaced by "no published claim extends to them".
- Lows (adopted): the AGENTS.md quotation is the current one (O48's "the route on each plan chosen by the official comparator"); the evidence-rules sentence names the O46 exception; LiveBench 2.0 Overall is listed among the single-leaf sources; MirrorCode's count is dated at O55; the band-straddle explanation covers both causes. Recorded: the O59 source list (provider documents are not a captured source type), stale labels in data and generated pages, for the release tidy-up.
- Recommendation (a pointer manifest verified against the generated documents) superseded by the rule above.
- Round status (O56): not clean (two Mediums). Draft r108.

## Internal review I50 (Claude Sonnet 5.5, effort xhigh, on r108) — adopted, modified or rejected
- H1 (adopted, data and engine changed; outputs changed): DeepSeek V4.1 Flash 1017 (max) has an exact Coding Agent Index v2.0 record ("DeepSeek Harness - DeepSeek V4.1 Flash 1017", reasoning effort max), but its pin in `data/v3_configuration_map.json` was null, so it was scored on the subset workload. The pin is set, the capture's stale v1.5 note is corrected, and a new gate (`value_v3.check_agent_pins`) stops the build when a ranked configuration's pin is empty while an exact single-model record exists; the gate caught this row before the pin was fixed. The anchors were re-frozen (four lines of `v3_frozen.json`), and the max-effort API ranking now has DeepSeek V4.1 Flash 1017 (max) first at 60.39 on the main workload (MiMo-V2.6-Pro 60.29, GPT-6.1 Sol (max) 60.16); MiMo-V2.6-Pro is the only subset row. This leader change is a data correction and is reported to the owner. The draft states the cost-source match rule (one model, its effort, no fallback token on AA's agent page, a mixed-model row never exact, a pin recording any choice among single-model agents).
- M1 (adopted, engine changed): the O46 ceilings' evidence clock was the capture date in the draft and Xiaomi's page-update date in the engine. Kept the draft's rule (E261): each ceiling route carries `capturedOn`, which `plan_routes.evidence_date` reads for O46 ceilings only, and the general clock sentence names the exception. Fixtures: pages re-read unchanged renew the clock; pages not re-read age to demotion.
- M2 (adopted, build changed): AI Coding Daily lists DeepSeek V4.1 Flash 1017 (max) twice (DeepSeek Harness 52.24, OpenCode 52.84) and the record took "the first-listed row". The rule is now stated and built (`build_swe_tracks.select_aicd`): the row on the harness of the configuration's Bug Hunt record, else the latest test date, else the build stops; the other rows are published as `alternates` in the record and its provenance, and the E227 harness count reads the record's harness field. The selected value is unchanged (52.24).
- L1 (adopted): stale labels fixed in `basket.py` (nine targets since O50; FrontierCode counted inside the Coding Agent Index), `quality.py` (seven common leaves), `plan_routes.py` (the window ends at the release cutoff, E213) and the MiniMax Bug Hunt note (the search is logged).
- L2 (adopted): E180 states each statistic's minimum panel and status string, as the code has them.
- L3 (adopted): the O44 companion says "none" when no configuration clears the bar by the margin.
- L4 (adopted): see H1.
- L5 (adopted; the check widened, per the owner's rule that a stale figure found after the check exists is a bug in the check): registry facts (report window, search cutoff and gap, last search, report-route dates, SemiAnalysis stage dates, release cutoff, vertex count and match distance, capture comparison) are named figures, and the check fails when one is typed by hand in any sentence that speaks of it, dated or not.
- L6 (adopted): the max-effort ranking's one-configuration-per-family shape is described as a consequence of what LiveBench 2.0 and Vals run, not a rule.
- Recommendations: 1 (pin gate) adopted as above; 2 (selection contract) adopted for AI Coding Daily, the other boards keep E206/E224/E225; 3 (route clock basis field) and 5 (automatic correction bridge) recorded for the release tidy-up.
- Round status (O56): not clean (one High, two Mediums). Draft r109.

## Editor decision E267 (2026-10-23, from I50 H1 and I51 M1): the exact Coding Agent Index record and the pin gate
A Coding Agent Index record is a configuration's exact record when its whole label (agent, one model, an optional effort in either of AA's two forms, an optional "(with fallback)") names the configuration's model identity, with or without the "Claude " prefix, and its effort; a record without an effort is exact for a configuration AA plots without one, and by O54 a MiMo-V2.6-Pro record at high is exact too; a two-model label is never exact. When exact records exist, the configuration's pin must be one of them; an empty or different pin stops the build (`value_v3.parse_agent_label`, `exact_agent_records`, `check_agent_pins`). A pin with no exact record in the capture is inert.

## Editor decision E268 (2026-10-23, from I50 M2 and I51 L5): a board that lists a configuration twice
For AI Coding Daily (the one added-leaf board run on several harnesses): the row whose harness name equals, ignoring case, the configuration's Bug Hunt harness (its name before any " / " route); if none or several match, the latest test date among the matching rows, or among all rows; a remaining tie stops the build. The other rows are published as `alternates` (`build_swe_tracks.select_aicd`).

## Internal review I51 (Claude Sonnet 5.5, effort xhigh, on r109) — adopted, modified or rejected
- M1 (adopted, engine changed; E267): the pin gate missed configurations without an effort, pins naming another label while an exact record exists, and could read a two-model label as exact; its test passed vacuously. The gate now parses the whole label and requires the pin to be an exact record whenever one exists; one fixture per case. The real build passes it unchanged.
- L1 (adopted): the two new rules are E267 and E268; no review label in the body.
- L2 (adopted; the check widened): the capture context matches "captured", and the previous capture date and the window's end are registry facts; the Source contract's capture instants are placeholders. The "at O<n>" exemption is stated in E265's text.
- L3 (adopted): the agent page "may omit" the fallback token; the match ignores it.
- L4 (adopted): E180 says the non-discriminating test leaves a leaf unmarked below two observed rows.
- L5 (adopted; E268): harness names compared by name, ties on the matched harness broken by date among them, no unstated override, scope stated.
- L6 (adopted, data and engine changed): the 2026-10-22 MiMo search is logged as a single-provider search, and the build fails when the search cutoff is not the date of a logged search.
- L7 (adopted in part, engine changed): the build recomputes each O46 ceiling from its recorded credits, rate and fee and fails on a difference; capturing Xiaomi's pages into the evidence bundle is recorded for the release tidy-up.
- L8 (adopted): wording.
- Round status (O56): not clean (one Medium). Draft r110.

## Internal review I52 (Claude Sonnet 5.5, effort xhigh, on r110) — adopted, modified or rejected
- M1 (adopted; the class removed at its source, E267 amended): a pin with no exact record was not checked, and the row was priced from whatever record it named. This was the third round in a row on the Coding Agent Index link (I50 H1, I51 M1, I52 M1), each a gap in a hand-kept pin and its gate. Following the owner's rule for recurring findings, the record is now derived from the capture (`value_v3.agent_record_for`: the configuration's one exact record); the map's Coding Agent Index pins are cleared, and a pin may only record a choice among several exact records. A pin that is not an exact record stops the build whether or not an exact record exists, and several exact records without a pin stop it too. Every pin that named a captured record equalled the derived one, so no score changed (only bundle hashes).
- L1 (adopted, data and engine changed): the search cutoff is defined as the latest all-provider search; the MiMo search is marked `singleProvider`, and the build fails unless the cutoff equals the latest all-provider search in the log.
- L2 (adopted): AA's axis label and the Coding Agent Index total are quoted as captured.
- L3 (adopted): E268's selection has unit tests and a test on the real board (`tests/test_swe_tracks_selection.py`); re-verification inside the engine is recorded for the release tidy-up.
- L4 (adopted in part): the ceiling tolerance is stated; the Lite quota is stored as 4,100,000,000; the editorial `capturedOn` and `check_open_web` dates are recorded for the tidy-up.
- L5 (adopted in part): E267 names the two effort forms, case-sensitive matching and that other forms are not exact; an ITBench-AA pin gate is recorded for when that component is admitted.
- L6 (adopted; the check widened): configuration names in any undated sentence are flagged, rendered with a new `{{name:ID}}` placeholder that fails when the configuration is gone, and the gap-fill bar result is a figure.
- Round status (O56): not clean (one Medium). Draft r111.

## Internal review I53 (Claude Sonnet 5.5, effort xhigh, on r111) — adopted, modified or rejected
- M1 (adopted, engine changed; E267 amended): the draft's label grammar omitted the two-form label that prices GPT-6 Luna (max). The grammar is now stated exactly (agent, model, optional plain effort, optional keyed effort, optional fallback token; both forms must agree), the real label is a fixture, and, at the source of this four-round class, a single-model label for a cohort model that the grammar cannot read now stops the build instead of leaving the row without its record.
- M2 (adopted; a figure): the E189 sentence claimed the 1-row subset stratum shows its SD ratio; it reads "undefined (panel too small)". The sentence now renders each subset stratum's status from the build (`subsetStrata`), which also removes a placeholder keyed by a workload hash.
- M3 (adopted, engine changed; outputs changed): the FrontierCode cross-source check joined Cognition's family-keyed board on the effort-qualified name, so its panel was 7 rows, not the 22 the rule names. It now joins on family and effort: τ_b 0.77, mean offset 2.6 points, largest 11.6; every bar still keeps its row under the fill sensitivities. No score changes (diagnostic only).
- L1 (adopted): the search cutoff is defined as the latest search not marked `singleProvider`, matching the gate, with the routine search's scope stated.
- L2 (rejected): the history sentence keeps its `{{name:...}}` placeholder; if that configuration left the roster the build would ask the editor to rewrite the sentence, which is the intended cost.
- L3 (adopted in part): the excluded rows' missing core leaves are a figure; effort-less names stay outside the name lint because each is also its family's name, which rules cite normatively (O46, O54).
- L4 (adopted): E237's version gate is stated for gap fills; the added boards' versions come with their capture (O59).
- L5 (adopted): the configuration-map rule and comment describe the derived agent record.
- Round status (O56): not clean (three Mediums). Draft r112.
