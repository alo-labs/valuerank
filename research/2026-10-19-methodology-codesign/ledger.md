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

