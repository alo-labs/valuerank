## Panel
Six Perplexity models, Search mode, Thinking on: GPT-6.1 Sol, Gemini 3.8 Flash, Claude Sonnet 5.5, Kimi K3, GLM 5.3, Grok 4.7. Round 1 = reviewers 1–7, round 2 = 8–12 so far. (The full ledger with every adopted item is in the repository; this is the condensed version.)

## Owner decisions (binding; argue only as "Owner decision challenge")
- O1 API and Plan buyers ranked separately. O2 Headline = weighted value score (cost 25%, quality 75%) plus frontier and cheapest-above-bar views. O3 Plan = full-utilisation Value Multiple, labelled. O4/O7 Only owner-named model-to-model transfers stay as labelled assumptions; other mismatches are unmatched and excluded from the official Plan ranking; a measured-only Plan view is published.
- O5/O9 superseded by O15 for the scored cost (total Index cost and USD per Index point are diagnostics).
- O6 SWE leaves: DeepSWE 30, Bug Hunt 10, FrontierCode 10, Terminal-Bench 10 (share of quality). O8 No quality floor; exchange rate disclosed. O10 One quality vector for both bases.
- O11 Official Plan routes need a controlled saturation measurement or ≥2 independent concordant reports (±20%). O12 Failed release gate holds the release. O13 Routes past 90-day expiry + 30-day grace are diagnostic-only (API-cost fallback, flagged). O14 c_SWE is diagnostic only.
- O15 Scored API cost = SDLC cost basket (Coding Agent Index incl. DeepSWE, FrontierCode, ITBench-AA, MMMU-Pro, Briefcase, GDPval, GDP.pdf, AutomationBench, Terminal-Bench 4.0, SciCode, LCR; excluded HLE, Omniscience, CritPt), phased by capture. O16 Plan rows without identified M_W are scored and flagged; certification needs identification. O17 A row missing a basket component is scored on its subset, flagged, compared on the identical subset.

## Editor decisions (owner may override)
- E1. Certification set fixes nominal weights, primary price rule, frozen route and linear GDPval map; specification robustness is published separately.
- E2. With transfers off, transfer-dependent Plan routes are unevaluable for certification (not replaced by API cost).
- E3. The matched-cost blocker requires ≥40% priced quality-weight coverage on a common panel; otherwise "cross-check unidentified" and the row cannot be certified.
- E4. Two certificate scopes: "certified among directly evidenced routes" and "certified across all eligible native Plan routes".
- E5. The matched-cost blocker is an API cost-shape check only; the Plan workload check is the M_AA-mix identification status.
- E6. The matched-cost panel may use any leaf with exact-variant per-task cost (incl. DeepSWE tokens × price list, FrontierCode), not only AA-index leaves; a feasibility matrix is published.
- E7. "Recommended" = interval-certified among directly evidenced routes.
- E8. Common-support quality is renormalised within each pair (keeps 25:75 on retained evidence; 1/p_ij published).
- E9. The basket prices one deployment-equivalent pass per task (evaluation repetitions excluded, as in AA's totals).
- E10. Subset calibration contract: each used subset is a versioned workload W_S with frozen subset anchors from reference configurations evidenced on it; paired full/subset results are published; the row keeps its O17 score and position, labelled "cross-workload ordering not identified" (answers GLM Q1 from O17's "flagged" wording).
- E11. Certificate validity is margin-based: every retained input enters through an admissible constraint or its documented domain worst case; no constraint and no domain = unevaluable. The 5% rule is only a disclosure trigger.
- E12. Plan uncertainty split: measurement object (S0) vs transport object (S1); "not separable" label where public evidence cannot split them.
- E13. Robustness outputs are named estimands; "S2 maximum rank change" means displayed-score rank; pairwise recommendation robustness is reported as edge changes (answers GLM Q2).

## Rejected or modified claims (do not repeat without a new argument)
- "AA's frontier plots cost per task": rejected; the captured chart is total cost to run the Index (both fields recorded).
- Remove assumed multiples / monthly-demand scenarios / cheapest-above-threshold as headline / basis-specific quality vectors / separate list for provisional rows / exclude mix-unmatched routes / withhold unidentified Plan scores / expired routes leave the table: rejected or modified by owner decisions above.
- Precision-aware weight shrinkage: rejected (weights fixed; noise in measurement layer). Near-Pareto on unrounded Index: rejected (policy uses rounded). Dirichlet α floor: replaced by hierarchical Dirichlet (floor recentred weights).

## Adopted, by reviewer (headlines only)
- R1 GPT-6.1 Sol: frozen anchors, raw-magnitude quality, Index removed from quality, 60/20/10/10 hierarchy, bands and sensitivity, frontier views.
- R2 (default router, not a panel model): source registry, bound-aware frontier, multiple provenance, explicit leaf formulas, three uncertainty layers.
- R3 Claude Sonnet 5.5: per-basis anchors with clip gate, coverage/provisional rule, leave-AA-out, workload cross-check, scenario engine, 90% rule.
- R4 Grok 4.7: matched-cost diagnostics, leader rule, binding-window full utilisation, leaf fixes, registry fields.
- R5 Kimi K3: cost layer in scenarios, admission rule, attempts reconciliation, S0/S1/S2, quota schema, GDPval logistic sensitivity.
- R6 GLM 5.3: pool scope, credit netting, expiry demotion, cross-check statistics, report independence.
- R7 Gemini 3.8 Flash: hierarchical Dirichlet, gross-cash multiple, deterministic certification, stress branches, frozen route.
- R8 GPT-6.1 Sol: normative definitions section and release tests.
- R9 Claude Sonnet 5.5: certification only with identified multiple, certificate scopes, certificate_role, time-indexed LP.
- R10 Grok 4.7: pairwise common support, Bug Hunt unit fix, lexicographic route choice, executable cohort rule.
- R11 Kimi K3: M_W transport to the scored workload, governing pairwise formula, Omniscience denominator, workload object.
- R12 GLM 5.3: outgoing-edge certification, simultaneous scenario leadership, margin-based validity, subset calibration, Plan measurement/transport split, named robustness estimands.
