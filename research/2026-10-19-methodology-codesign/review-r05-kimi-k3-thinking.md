I reviewed draft r04 against its stated objective — identifying the lowest-cost model for value delivered in practice, separately for API and Plan buyers — and checked the key external facts (AA's cost construction, plan limit mechanics, benchmark cost reporting). The draft is strong on governance and missing-data discipline, but the uncertainty machinery ignores cost noise entirely, and the Plan basis has an evidence-admission gap that a single anecdote can exploit.

1. Findings by severity

Critical

Cost enters the scenario engine as an exact number. The joint simulation draws leaf intervals, multiple ranges, identification bounds, weights, source-drop and transfer flags — but never the API cost input. Yet AA computes cost and score from one pass of one configuration through its evaluation set, so cost carries unquantified token-use variance, and AA itself notes that cost reflects actual token consumption, which varies across runs. Independent reruns show this variance is material: Vals AI's TB4 runs report standard errors across only three runs. Every scenario-conditional claim — the ≥90% leader rule, ≥90% unique-cheapest rule, rank-share columns — is therefore conditional on a noiseless cost axis covering 25% of the headline. Fix: add a cost layer to the measurement stratum (task-clustered resampling of per-evaluation costs, price-basis alternatives, cache-rate range; details in §2), and require cost draws to move jointly with the same model's AA-run leaf draws, since both numbers come from the same serving snapshot.
artificialanalysis
+2

No minimum-evidence threshold for Plan multiples in the official ranking. The evidence policy bans provider marketing quotas but admits a single end-user report as a point value, and route selection then consumes that point directly. Dispersion in such estimates is enormous: the widely believed ceiling for a $200 plan was ~$2,000/month of API-priced tokens (~10×), while SemiAnalysis's controlled saturation measurements found plans far more generous, in the 40–70× range, and the deliverable "value" of a plan varies by model and workload. Since Plan cost = API cost ÷ multiple, one atypical report can halve or double a route's cost and pick the Plan winner. This is new relative to the ledger: reviewers 3 and 4 hardened route selection and full-utilisation arithmetic, but nothing requires evidentiary multiplicity. Fix: official Plan ranking admits a route only on a controlled saturation measurement or ≥2 independent concordant reports (±20%); single-source routes are diagnostics and cannot carry the "recommended" label.
newsletter.semianalysis
+2

High

Attempts accounting between cost and quality is not reconciled per leaf. DeepSWE quality is pass@1 averaged over 3 attempts per task, while AA's run-cost field is computed from tokens "excluding repeats" and DeepSWE cost is published per task. If the cost input prices fewer attempts than the quality score rewards, cost is biased low relative to measured quality — precisely the direction that flatters expensive, flaky models to API buyers, who pay for every attempt. Fix: manifest records attempts-in-quality vs attempts-in-cost per leaf; confirmed mismatches are either scaled or carried as bounded bias draws in the new cost layer.
artificialanalysis
+4

The measurement-only stratum is undefined for rows with missing leaves. The engine "draws leaf values from their measurement intervals … [and] identification bounds for missing leaves," which fuses the measurement and identification layers; but the leader rule conditions on the measurement stratum alone ("≥ 90% of measurement scenarios"), and label-eligible non-provisional rows can still have up to ~30% of quality weight missing. As written, that 90% share is not reproducibly computable. Fix: define strata cumulatively and explicitly — S0 measurement = renormalised composite with missing leaves excluded; S1 adds identification draws; S2 adds specification draws — and publish computable pseudocode.
0

The full-utilisation definition lags 2026 quota mechanics. Claude plans now combine a rolling 5-hour window with weekly caps, shared across chat and Claude Code; Anthropic does not publish exact token numbers; limits were raised in May and again in September 2026 without numeric notice, and a user-deployable "rate-limit reset" balance was added; some tiers now bundle monthly API credits ($100/$200) alongside quota. "Minimum across binding windows" is silent on whether resets count as achievable capacity, and "fee = amount paid" does not allocate a hybrid fee between quota and bundled credits. Fix: registry fields for limit-schema version, reset-balance handling (counted only if spendable on the measured workload), and fee decomposition; the 30-day soft expiry is well-chosen — these 2026 changes are exactly what it must catch.
allthings
+3

Medium

End-user multiple reports carry selection bias. Only saturating power users post receipts; unsaturated users cannot observe their delivered value. The concordance rule in §2 helps; additionally record sampling basis and source count per multiple in the registry and publish both. New argument relative to the existing "end-user API-priced reports" policy: the fixed rule governs what counts as evidence, not how biased samples are handled.

The workload cross-check is only partially independent. DeepSWE cost and success come from the same AA runs already used in cost and quality; prefer the independent tbench.ai leaderboard, which publishes COST and TOKENS columns, or Vals AI's per-test TB4 costs. Also, AA's headline cost-per-task is weighted by Intelligence Index weights, so the matched-cost diagnostic must re-weight per-evaluation costs by ValueRank's leaf weights rather than reuse AA's weighted figure.
tbench
+2

GDPval-AA is ordinal Elo treated as cardinal. The Elo comes from blind pairwise comparisons over 220 tasks; the linear clip (E−500)/2000 hard-codes one cardinalisation. Add a specification-layer sensitivity that maps through a logistic win-probability against the pinned anchor before linearising (anchor identity is already in the registry).
artificialanalysis

Interval draws have no declared kernel. Uniform is exact only for rounding ranges; for repeat-run ranges (e.g. Bug Hunt's repo/repeat range), kernel choice moves tails and therefore moves every ≥90% threshold call.

Cost inputs have no freshness rule. Plan evidence has 30/90-day expiries, but AA snapshot and price-list age have none; with demonstrated 2026 price/limit churn, add a max age (e.g. 45 days) and a change-triggered refresh.
justinmckelvey

Low

Release-gate failure has no defined remedy — when the clip gate or 5-point-swing gate fails, specify hold-release vs re-anchor-as-migration with a dual-run comparison.

Publish per-row effective weights, not only release-level, since per-row renormalisation varies them.

The mix-distance "declared tolerance" has no number — define the metric (e.g. L1 distance on category shares) and the threshold now.

2. Methodology design recommendations

Cost measurement layer (fixes the Critical scenario gap). Model API cost as the sum of per-evaluation costs with three draw components per scenario: task- or run-clustered bootstrap where per-task/per-run costs are published (DeepSWE per-task; TB4 cost columns ); price basis drawn over {first-party list, cross-provider median} mirroring AA's own price rule; cache-hit rate drawn within its manifest range. One shared "serving snapshot" draw couples a model's cost and its AA-run leaf values. Publish 
S
D
(
𝑆
𝐶
)
SD(S
C
	​

) per row and a cost-vs-quality variance decomposition of each value score.
tbench
+4

Multiple admission rule (fixes the Plan evidence gap). A route enters the official Plan ranking only via a controlled saturation measurement (SemiAnalysis-style exhaustion with receipts ) or ≥2 independent reports concordant within ±20%; all multiples keep current provenance fields plus source count and limit-schema version. Leader rule on the Plan basis requires a qualifying route on both sides of its identification bounds.
x

Formal stratum definition with pseudocode. S0 / S1 / S2 as above, so every published scenario share is reproducible from the registry.

Quota-schema registry v1. Window list, reset-balance policy, bundled-credit allocation (subtract credits priced at API list when unmeasured), and schema diffing to power the 30-day change detection.
justinmckelvey
+1

Attempts reconciliation in the manifest. Per leaf: attempts_quality, attempts_cost, and a bias bound when they differ; drawn in the identification layer.

Declared draw kernels. Uniform on rounding ranges; clustered resampling on raw runs where available; triangular on observed-run ranges otherwise. State each in the registry.

Independent-first workload cross-check. Use tbench.ai or Vals AI per-test costs, re-weighted by ValueRank leaf weights; report the dependence caveat alongside Spearman.
tbench
+1

Freshness cadence. Monthly refresh or on-change; cost snapshot max age 45 days; price-list-date diff alerting.

Smalls. GDPval logit sensitivity; per-row effective weights; explicit mix-tolerance; written gate-failure procedures.

3. Questions for the owner

Do your AA data rights permit ingesting per-task/per-run costs? If not, recommendation 1 must fall back to parametric draws, which weakens the Critical fix.

Can you procure controlled saturation measurements for the top Plan routes each cycle, or is end-user reporting the practical ceiling? This determines whether the C2 threshold is binding or vacuous.

Is the intended measurement-stratum treatment of missing leaves the renormalised composite? It determines how the 90% leader rule is computed.

Under current plan terms, are "rate-limit reset" balances spendable on the measured workload? The answer materially changes full-utilisation multiples.
justinmckelvey

When a release gate fails, do you hold the release or re-anchor as a versioned migration? This defines the governance remedy text.

4. Verdict

VERDICT: HAS FEEDBACK