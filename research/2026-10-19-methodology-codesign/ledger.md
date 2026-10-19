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
