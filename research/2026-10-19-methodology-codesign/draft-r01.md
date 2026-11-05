# ValueRank methodology — draft r01

## Objective

Artificial Analysis (AA) publishes a Pareto frontier of Intelligence Index vs. total USD cost to run its Intelligence Index benchmarks. That frontier does not answer the question ValueRank exists for: **which frontier AI model is actually lowest cost for the value it delivers in practice**, once (a) subscription-plan economics are considered and (b) benchmarks geared to real software-engineering work are weighed alongside general capability. ValueRank serves two buyers, ranked separately: **API buyers** (developers and automated workloads paying per token, including via third-party agents) and **Plan buyers** (people using a provider's subscription apps/CLIs, e.g. Claude Code, Codex, ChatGPT, SuperGrok).

## Outputs (headline + views)

1. **Headline**: a value score per basis (API, Plan) = 25% cost score + 75% quality score (owner decision), with rank bands.
2. **Cost–quality frontier** per basis: models not dominated on (cost per point, quality score).
3. **Cheapest above a quality bar**: for published quality thresholds (e.g. quality ≥ 50, 60, 70), the cheapest model on each basis.
4. **Diagnostics**: AA Intelligence Index, output speed, tokens used to run the AA suite, per-dimension raw values, evidence grades.

## Cohort and configuration (fixed policy)

- Every model family on AA's rendered Intelligence-Index-vs-total-cost Pareto line as observed, plus every near-frontier family (rounded Index within 3 points of the frontier's best Index at equal or lower cost). Current cohort: 19 families.
- **Configuration rule**: each family's selected configuration is the one AA plots on (or nearest to) the frontier; a configuration manifest records model/version, reasoning effort, fallback behaviour and, per benchmark, the evaluated harness/agent and tool limits. Evidence is exact-variant only: no transfer between versions, efforts or harnesses; harness differences are shown as separate stack evidence.
- Missing values stay missing (no zero/mean/neutral fill).

## Cost (25% of the value score, both bases)

- **Source field**: AA "Cost to Run Artificial Analysis Intelligence Index" (total USD for the full suite at list prices, including reasoning tokens). The suite version and retrieval date are recorded. AA's total tokens used to run the suite are published alongside as a diagnostic (token consumption separated from price).
- **API basis**: AA total suite cost ÷ AA Intelligence Index = USD per Index point.
- **Plan basis (full-utilisation effective cost, labelled as such)**: API USD per point ÷ highest eligible Value Multiple. It assumes the subscriber uses the plan's full allowance; it is not a monthly-bill estimate. A plan route is eligible only if it gives access to the selected model; effort mismatches are flagged. Models with no route fall back to API (flagged).
- **Value Multiple** = API-priced usage a plan delivers ÷ fee. Evidence rules unchanged (no provider marketing quotas as numerator; end-user API-priced reports or SemiAnalysis controlled measurements). Owner-authorised assumptions (e.g. Opus 5.5's measured multiples applied to other Claude models) stay in the Plan ranking, labelled "assumption", and a **measured-only Plan view** is published alongside.
- **Scoring with frozen anchors** (no longer cohort-relative): S_C = 100 × clip((ln c_H − ln c) / (ln c_H − ln c_L), 0, 1), with versioned anchors c_L and c_H (e.g. $1 and $300 per point) shared by both bases. Anchor changes are versioned separately from data refreshes. Actual dollars are always displayed.

## Quality (75% of the value score)

Non-overlapping hierarchy (AA Intelligence Index removed as a quality dimension because its components are scored directly and it already divides cost; kept as diagnostic). Output tokens/s moved to diagnostics (it is decode speed, not completion time).

| Group (share of quality) | Dimension | Share of quality |
|---|---|---:|
| Software engineering (60%) | DeepSWE v1.1 (AA, pass@1 over 3 attempts, 113 tasks; note: one component of AA's Coding Agent Index) | 30% |
| | Bug Hunt Bench (planted bugs fixed /105, model+harness) | 20% |
| | Terminal-Bench 4.0 | 10% |
| General professional work (20%) | GDPval-AA v2.1 | 10% |
| | AutomationBench-AA | 10% |
| Reliability & instruction following (10%) | AA-Omniscience (accuracy and non-hallucination reported together; scored on accuracy-weighted reliability) | 5% |
| | LiveBench Instruction Following | 5% |
| Long context & science (10%) | AA-LCR v1.1 | 5% |
| | HLE, GPQA Diamond, SciCode, CritPt (equal shares) | 5% |

- **Normalisation on raw magnitudes with frozen anchors** instead of ranks: z = 100 × clip((x − a_low)/(a_high − a_low), 0, 1) per benchmark, anchors published and versioned (for % metrics, typically 0 and 100 or a stated floor/ceiling; for Elo-like metrics, a frozen bounded transform). Rounded inputs are treated as rounding ranges.
- **Missing data**: quality is renormalised over a row's available dimensions (no imputation, fixed policy). Each row also publishes identification bounds — L = score with missing dimensions at 0, U = with missing at 100 — and is marked **provisional** when its software-engineering group coverage is below 50% or bounds overlap a neighbour's rank. A row without a cost gets no value score (quality shown separately).

## Robustness and transparency

- Rank bands from: rounding ranges, published benchmark intervals, task bootstrap where per-task data exist, Value Multiple ranges, leave-one-benchmark-out and leave-one-source-out rankings, and cost-weight sensitivity (slider). No probabilities without a statistical basis.
- Evidence classes shown per value: measured / claim / estimate / assumption; provider claims never overwrite independent measurements (both shown).
- Edge cases: single observed value or identical endpoints are handled by the frozen anchors. Plan evidence expires after a stated period (e.g. 90 days) and is then flagged stale, not silently replaced. Each release publishes a score-change decomposition (data vs. method vs. cohort).

## Known limitations

- Value Multiples are sparse and workload-specific; full-utilisation Plan cost overstates value for light users.
- AA cost uses list prices and AA's token mix; caching/batch discounts are not modelled.
- Bug Hunt and DeepSWE measure model+harness stacks.
