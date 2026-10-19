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
