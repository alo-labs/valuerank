# ValueRank methodology — draft r03

## Objective and claim scope

AA's Pareto frontier of Intelligence Index vs. total USD cost to run its Intelligence Index does not answer the question ValueRank exists for: **which frontier AI model is actually lowest cost for the value it delivers in practice**, once (a) subscription-plan economics are considered and (b) benchmarks geared to real software-engineering work are weighed alongside general capability. ValueRank serves two buyers, ranked separately: **API buyers** (pay per token, incl. third-party agents) and **Plan buyers** (provider subscription apps/CLIs: Claude Code, Codex, ChatGPT, SuperGrok…).

Claim scope: "value among AA-selected frontier and near-frontier configurations, under the published benchmark mix and evidence". Not a market-wide optimum across all configurations and workloads.

## Outputs

1. **Headline**: value score per basis = 0.25 × cost score + 0.75 × quality score (owner decision). The implied exchange rate is printed beside it (with the anchors below, doubling API cost ≈ −2.9 value points ≈ 3.9 quality points), together with cost-weight slider results in the main table. No quality floor (owner decision); provisional rows are flagged.
2. **Cost–quality frontier** per basis, bound-aware: "definite" vs "possible" frontier members.
3. **Cheapest above a quality bar**, with bars defined by named reference configurations (e.g. "at least the quality of the median definite-frontier model"), not raw numbers; bound-aware: a model is "confirmed qualifying" if its lower quality bound ≥ bar, "possibly qualifying" if only its upper bound is. A uniquely cheapest recommendation is named only if its worst-case cost beats every possibly-qualifying candidate's best-case cost; otherwise a candidate set is published.
4. **Diagnostics**: USD per AA Index point, AA Intelligence Index, AA tokens used to run the suite, output speed, raw values, evidence grades, measured-only Plan view.

## Source contract (versioned registry)

Machine-readable registry per release: AA chart identity, filters and snapshot timestamp (current: "Intelligence Index vs. Cost to Run Artificial Analysis Intelligence Index", x-axis "Cost to Run Intelligence Index (USD)", unit "USD to run all Intelligence Index evaluations", captured 2026-10-17); cost field, unit and accounting (as AA defines it, including any cache pricing AA applies); per model: version, effort, fallback, serving route and per-benchmark stack; per benchmark: version, raw metric, population, attempts, aggregation, source revision/commit, observation and retrieval dates; explicit missingness reason (not evaluated / incompatible variant / no public evidence / withdrawn). A change of AA chart or field is a versioned methodology migration, never a silent refresh.

## Cohort and configuration (fixed policy)

- AA rendered Pareto families as observed plus near-frontier families (rounded Index within 3 points of the frontier's best at equal or lower cost); 19 families now.
- Configuration rule: the configuration AA plots on (or nearest to) the frontier; manifest records model/version, effort, fallback, and per-benchmark harness/tool limits. Exact-variant evidence only; harness differences shown as separate stack evidence. Missing stays missing.

## Cost (25% of the value score)

- **API cost input** = AA total USD to run the full Intelligence Index suite (token efficiency × list price). Not divided by the AA Index (that would let AA's own capability mix count a second time next to ValueRank quality); USD per Index point is a diagnostic only.
- **Plan cost input (full-utilisation effective cost, labelled)** = API cost input ÷ Value Multiple of the selected route. Computed per model–plan **tier**–surface–configuration route (tier and fee are part of route identity and published). To avoid winner's-curse bias, the route is chosen on the **lower bound** of each multiple's range (point value where only a point exists), after joining access conditions and evidence. API-fallback rows are shown but excluded from Plan winner, frontier and threshold claims.
- **Value Multiple** = API-priced usage a plan delivers over a stated fee period ÷ fee for that period. Each multiple records fee period, workload, model/effort, token categories (input, cache read/write, reasoning, output), valuation price list and date, shared usage pools, whether capacity was exhausted and which rate-limit windows bound it. Where public token receipts exist, the numerator is repriced on the same price list as AA cost; otherwise the original valuation basis is kept and flagged. No extrapolation of short bursts to a billing period unless the controlled measurement establishes it. Evidence rules unchanged (no provider marketing quotas; end-user API-priced reports or SemiAnalysis controlled measurements).
- **Assumptions**: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; common GPT multiple; MiMo 1.5×) stay in the official Plan ranking, labelled, with donor measurement identified. Any other mismatch (effort, surface, workload, price basis) is "unmatched" and excluded from the official Plan ranking. A measured-only Plan view is published.
- **Scoring with frozen, per-basis anchors** in total-USD units: S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1). API: c_L = $50, c_H = $20,000 (cohort spans ~$110–$8,700). Plan: c_L = $1, c_H = $2,000 (native routes span ~$3–$860 because Claude multiples are ~57–59×). Anchors are scaling constants from a frozen reference cohort's 1st/99th percentiles, versioned separately from data refreshes; dollars always displayed and unclipped values kept in the data release. Release gate: fail if more than 10% of rows sit at a clip bound on either basis.

## Quality (75% of the value score)

Normalisation on raw magnitudes with frozen, versioned anchors: z = 100 × clip((x − a_low)/(a_high − a_low), 0, 1); a_low = chance/baseline level, a_high = documented ceiling where one exists, else 100%; rounded inputs treated as rounding ranges; unclipped z kept in the data release. Each release publishes **effective weights** (w_i × SD(z_i), normalised), the leaf rank-correlation matrix and the **share of quality weight by data source** (today ≈75% AA-run: DeepSWE, FrontierCode, GDPval, AutomationBench, Omniscience, LCR, HLE, GPQA, SciCode, CritPt; ≈25% independent: Bug Hunt, Terminal-Bench, LiveBench). A group whose effective weight drifts more than ±50% from nominal is flagged. AA Intelligence Index and output speed are diagnostics, not quality.

| Group | Leaf | Share of quality | Leaf formula |
|---|---|---:|---|
| Software engineering (60%) | DeepSWE v1.1 (AA; pass@1 avg of 3 attempts, 113 tasks; a component of AA's Coding Agent Index) | 30% | % pass@1, anchors 0–100 |
| | Bug Hunt Bench (2 TypeScript repos, 105 planted bugs; model+harness) | 10% | fixed/105, anchors 0–105; whole-run bootstrap |
| | AA FrontierCode 1.1 (repo code changes, tests + rubric) | 10% | %, anchors 0–100 |
| | Terminal-Bench 4.0 | 10% | % resolved, anchors 0–100 |
| General professional work (20%) | GDPval-AA v2.1 (Elo) | 10% | z = 100 × clip((E − 500)/2000, 0, 1) (AA's published integration transform, verified at implementation) |
| | AutomationBench-AA | 10% | %, 0–100 |
| Reliability & instruction following (10%) | AA-Omniscience | 5% | z = (2A + N)/3, A = accuracy %, N = non-hallucination % (2:1 mirrors AA's emphasis on accuracy over abstention; AA's own Omniscience index recorded for comparison) |
| | LiveBench Instruction Following | 5% | %, 0–100 |
| Long context & science (10%) | AA-LCR v1.1 | 5% | %, 0–100 |
| | HLE, GPQA Diamond, SciCode, CritPt | 1.25% each | %, 0–100 |

- Missing data: quality renormalised over a row's available leaves (fixed leaf weights; no imputation). **Coverage** = observed share of total quality weight. A row is **provisional** (still ranked, per cohort policy, but flagged and excluded from "unique cheapest" claims) unless coverage ≥ 70% and at least 2 SWE leaves are observed. Identification bounds L (missing at 0) and U (missing at 100) are the formal interval; a separately labelled **sensitivity band** sets missing leaves to the cohort's observed min/max for that leaf (sensitivity analysis, not imputation). A row without a cost gets no value score.

## Uncertainty (three separate layers, one scenario engine)

A joint scenario simulation (N = 10,000) is the single engine: each scenario draws leaf values from their measurement intervals, multiples from their ranges, a weight vector from a Dirichlet centred on nominal weights (concentration ≈ 50), a source-drop flag (incl. drop-AA) and the owner-authorised transfer on/off flag; shared multiples and price lists are drawn once per scenario. Results are published per layer as scenario shares (e.g. share of scenarios with rank ≤ 3, on the frontier, qualifying at a bar), labelled as scenario frequencies, not probabilities. A "unique cheapest" is named only when it holds in ≥ 90% of scenarios. Layers:

- **Measurement**: published intervals, rounding ranges, task- or run-clustered resampling where per-task/per-run data exist.
- **Identification**: missing-data bounds; unmeasured Plan quantities (multiple ranges).
- **Specification**: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (**leave-AA-out is a headline robustness column**), cost-weight slider, owner-authorised transfer on/off.
- **Workload cross-check (mandatory)**: where DeepSWE or Terminal-Bench 4.0 publish matched cost and success, compute cost per solved task and report its rank agreement with the AA-cost ranking; Spearman < 0.7 puts a warning on the headline and any model moving more than 3 places is flagged.
Shared dependencies move together (one multiple, price update or benchmark version affects all its rows jointly). Robust pairwise orderings are published only when they survive the declared joint scenarios; overlap is not treated as transitive tie groups.

## Governance

Evidence classes (measured / claim / estimate / assumption); provider claims never overwrite independent measurements. Plan evidence carries a 30-day soft expiry with change detection (a plan whose published limits or pricing page changed since measurement is flagged "possibly superseded") and a 90-day hard expiry (flagged stale, not replaced). Each row stores its AA price-list date; score changes are decomposed into price change vs token-use change vs method vs cohort. Release gates: fail on clip rate > 10%, an unversioned AA chart/field change, or any score swing > 5 points without an attributed cause. The registry records grader identity and version for rubric-graded leaves (FrontierCode, GDPval-AA).

## Known limitations

Full-utilisation Plan cost overstates value for light users; AA cost uses AA's token mix; Bug Hunt covers two repositories; DeepSWE/Bug Hunt/TB measure model+harness stacks; suite is primarily English text.
