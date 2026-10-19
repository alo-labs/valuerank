I'll verify the key factual mechanics of the draft (AA cost computation, benchmark scoring rules, plan quota structures) before finalizing the review.
The first round verified AA's cost field, GDPval's Elo transform, Omniscience scoring, Bug Hunt Bench, Terminal-Bench, and Claude plan quota structure. Let me verify the remaining benchmark provenance and the SemiAnalysis plan-measurement assumption.
Verified against public sources: AA's cost-to-run field (token categories, cache pricing, repeats excluded), its price rule, the GDPval-AA Elo transform and anchor, Omniscience scoring, DeepSWE/FrontierCode provenance, Terminal-Bench and Bug Hunt Bench mechanics, Claude plan limit structure, and the SemiAnalysis controlled-measurement protocol. Arithmetic spot-checks also passed: the printed exchange rates are correct (doubling cost = −100·ln2/ln(c_H/c_L) × 0.25 → −2.89 points on API, −2.28 on Plan), and the harmonic category-multiple formula M = (Σ_k t_k/m_k)⁻¹ is correct for shared meters and correctly handles unmetered categories (e.g., unmetered cache reads, which SemiAnalysis treats as free ). Findings below.
tbench
+14

1. Findings by severity

Critical

None.

High

H1 — Cost numerator does not price the work carrying ~56% of quality weight (Owner decision challenge, O5/O9). AA's Intelligence Index v4.3.2 comprises Briefcase, GDPval-AA, AutomationBench-AA, Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-Omniscience and AA-LCR; DeepSWE is a Coding Agent Index component, not an Intelligence Index component, and Bug Hunt, LiveBench IF and GPQA are not AA-index evals. Mapping the draft's leaf weights onto the priced suite: TB4 10 + GDPval 10 + AutomationBench 10 + Omniscience 5 + LCR 5 + HLE/SciCode/CritPt 3.75 = 43.75% of quality weight priced; DeepSWE 30 + Bug Hunt 10 + FrontierCode 10 + LiveBench 5 + GPQA 1.25 = 56.25% unpriced, while the priced suite's Briefcase and GDP.pdf work carries zero quality weight. This is a new argument against O9's stated rationale: "the whole-suite bill is the intended price of a model's work" fails exactly where ValueRank's quality is concentrated — long-horizon SWE trajectories, where per-task costs span two orders of magnitude (FrontierCode alone: $0.09–$12.00 per task ). A model can be token-efficient on the generalist suite yet expensive per unit of SWE value, and the 25% cost term will not see it except through the flag-only matched-cost diagnostic. Change (within fixed policy): publish cost-mix coverage (currently 43.75%) as a standing diagnostic; add a c_SWE companion column built from public per-task/per-run costs AA and others already publish (FrontierCode cost per task, TB4 leaderboard tokens/cost, Bug Hunt per-run cost ); make the >3-place matched-cost flag key off this composite rather than only the II-leaf reweighting.
artificialanalysis
+5

H2 — Dirichlet weight kernel has uncontrolled per-leaf variance. With α_i = 50·w_i, Var(w_i) = w_i(1−w_i)/(α0+1), so the coefficient of variation is CV_i = √((1−w_i)/(51·w_i)): ≈124% for the 1.25% science leaves, 61% for 5% leaves, 42% for 10% leaves, versus 21% for DeepSWE. This is a new argument against Reviewer 4's adopted kernel: the total pseudo-count (α0 = 50) looks moderate, but small leaves get effectively random weights in a large share of scenarios. It hurts the objective because S2 scenario shares and the ≥90% "unique cheapest" rule conflate genuine specification disagreement with near-random draws on small leaves — results become noise-dominated, or everything fails the 90% bar and the robustness columns carry no information. Change: α_i = max(50·w_i, 10) (caps CV at ≈30% for small leaves), or specify an explicit CV target and solve for α_i; publish realized per-leaf CV in the registry as a declared-kernel property.

H3 — Per-model quota sub-pools structurally bias the O4/O7 transfers and route comparability. Claude Max plans carry an all-models weekly limit plus separate per-model weekly limits (Opus tracked and reset separately; Fable has its own weekly limit), shared across Claude and Claude Code. The Opus 5.5 → other-Claude transfer therefore assumes pool equivalence that is demonstrably false on current plans, with a known direction (per-model pools are typically the binding, smaller ones). A "labelled assumption" understates this: it is a structurally biased estimate, and route-to-route multiple comparisons across different pool structures are not like-for-like. Change (transfers stay, per O4): extend the quota schema to record pool scope per window (all-models vs per-model); transfers where donor and target sit in different pool scopes carry a directional bias bound drawn in the identification layer (like the attempts bias); and where SemiAnalysis's per-(plan, model, token type) measurements exist, use the measurement instead of the transfer — O11 already admits it.
newsletter.semianalysis
+2

H4 — Bundled-credit double-count risk in the Value Multiple. The fee subtracts bundled monthly API credits at list value, but if a route's measured numerator includes usage that was paid by those credits (or by the overage "usage credits" available on Max plans ), the same value is counted once in the numerator and once via the reduced denominator, inflating the multiple. Change: specify the numerator as net of credit-paid consumption, or keep the gross fee when credits were spent during the measurement; record which convention each multiple uses in the quota schema.
developersdigest

Medium

M1 — Omniscience blend rationale contradicts AA's published practice. The draft says (2A+N)/3's 2:1 weighting "mirrors AA's emphasis on accuracy over abstention," but AA's Intelligence Index v4 weighted Omniscience Accuracy and Hallucination Rate equally (6.25% each), and the Omniscience Index itself scores +1 for correct, −1 for incorrect, 0 for abstention — a 1:1 accuracy-versus-penalty structure. Since the registry requires a documented reason for the blend, the reason as written is factually wrong, and (2A+N)/3 also rewards abstention twice (N rises when the model abstains). Change: re-justify 2:1 explicitly as a ValueRank choice, or adopt AA's structure; pin AA's exact field definitions for A and N (hallucination rate is conditioned on non-abstentions ) in the registry.
artificialanalysis
+1

M2 — Hard-expired multiples keep feeding the official Plan ranking. Under current rules a single-source route can never earn "recommended" (O11), but a two-source route whose measurements are 4+ months stale can — an asymmetry that misleads, since plan limits demonstrably change mid-cycle (e.g., user-reported quota adjustments and peak-hour changes to 5-hour limits). Change: after the 90-day hard expiry plus a short grace period, demote the route to diagnostic-only (no "recommended," excluded from winner/threshold claims), mirroring the single-source rule.

M3 — Workload cross-check is statistically under-specified. The Spearman < 0.7 gate is computed over the subset of rows with matched cost+success on DeepSWE/TB4 — likely well under 19 rows, where rank correlation is high-variance and the subset is undefined. Change: define the matched subset, set a minimum n (e.g., ≥8; suppress the gate below it), report Kendall τ-b with a bootstrap CI alongside Spearman, and keep the existing per-model >3-place flag as the primary trigger.

M4 — "≥2 independent end-user reports" lacks an independence definition and concordance estimator. Two reports can derive from the same quota-page change or the same power user's post. Change: define independence as distinct observers, non-overlapping measurement periods at least 7 days apart, and no shared upstream source; pool via geometric mean; concordance = max pairwise deviation ≤20% of the pooled value; record each report's sampling basis.

Low

L1 — "Recommended" is conditioned only on measurement scenarios (S0) plus identification bounds. Disclose the conditioning in the label itself, or add a weak S2 stability requirement (e.g., leads in a majority of S2 scenarios with transfers off).

L2 — Low-variance leaves will chronically trip the ±50% effective-weight drift flag. Leaves where the frontier clusters (e.g., HLE) have near-zero SD(z), so their effective weight drifts arbitrarily. Add a "non-discriminating" status (cohort SD(z_i) below a declared threshold) exempt from drift-flag counting but still reported.

L3 — Bug Hunt rows carry unequal run counts (n = 1–5 across the public leaderboard). Record n per row and widen n=1 rows in the measurement layer using the cohort's observed repeat spread. This is row-level precision, distinct from the rejected bug-level bootstrap.
github

2. Methodology design recommendations

Prioritized; all implementable from public data on the existing monthly cadence.

Fix the weight kernel (H2). Set α_i = max(50·w_i, 10), or declare a CV cap of ~30% and solve α_i = (1−w_i)/(CV²·(1+w_i)) approximately per leaf; publish realized CV per leaf per release. This is a one-line change to the scenario engine and materially improves the interpretability of every S2 output, the ≥90% unique-cheapest rule, and the robust pairwise orderings.

Add the cost-mix coverage and c_SWE companion diagnostics (H1). Coverage_priced = Σ w_i over leaves present in AA's Intelligence Index (43.75% today), published per release and re-derived whenever AA's index composition changes. c_SWE = Σ over SWE leaves of (cost per task × task count), using AA's published FrontierCode cost per task, AA's DeepSWE data, tbench.ai/Snorkel TB4 run costs, and Bug Hunt per-run cost. Flag a row when c_SWE/c_II deviates more than 50% from the cohort median. This does not touch the O5 input; it makes the O9 rationale testable per model instead of asserted.
artificialanalysis
+4

Extend the quota schema with pool scope and add transfer bias bounds (H3). Fields: per window (5-hour, weekly), pool scope ∈ {all-models, per-model:<name>}; per-model weekly sub-limits recorded as separate windows. Transfers (O4/O7) where donor and target models sit in different scopes get an identification-layer bias draw whose sign and rough magnitude come from the published pool ratios (e.g., Max's Opus-only vs all-models weekly limits ). Prefer SemiAnalysis per-(plan, model) rates over transfers wherever they exist.
newsletter.semianalysis
+2

Credit netting rule (H4). Value Multiple = (API-priced usage net of credit-paid consumption) ÷ (fee − bundled credits at list value), or gross fee if credits were spent; convention recorded per multiple.

Hard-expiry demotion (M2). 90-day expiry + 30-day grace → route becomes diagnostic-only; the Plan view's row count may shrink, which is the correct behavior for a ranking that claims routine refresh.

Cross-check statistics upgrade (M3). Minimum n = 8 matched rows; Kendall τ-b with 1,000-resample bootstrap CI; Spearman retained as secondary; per-model >3-place flag unchanged.

Independence criteria and pooled estimator for end-user reports (M4). As specified in M4; also record whether each report's meter readings were step-based (the SemiAnalysis protocol reads meters after every request and converges to ±5% ) — step-based reports should be preferred over self-declared token totals.
explainx

Omniscience rationale fix (M1). Either adopt z = A − I (AA's +1/−1/0 structure ) or keep (2A+N)/3 with a corrected rationale: "ValueRank penalizes wrong guesses less than AA because capability, not calibration, is the target of the quality vector."
artificialanalysis

Non-discriminating leaf status (L2). If cohort SD(z_i) < 3 points, mark the leaf non-discriminating: excluded from drift-flag counting, still scored, reported in diagnostics.

Deterministic scenario engine. Fix and publish the RNG seed and draw order per release; publish per-stratum scenario outputs (S0/S1/S2, transfers on/off, leave-AA-out) as data files so the "scenario shares" are reproducible by third parties.

Plan buyer utility disclosure. Per route, publish F (fee) and M·F (full-utilisation capacity in API-priced USD) — both already computed. This addresses the O3 light-user limitation at zero additional data cost: a buyer whose monthly API-priced demand exceeds F benefits from the plan up to the M·F capacity ceiling, and the table now says so without scenarios.

3. Questions for the owner

Where SemiAnalysis has published per-(plan, model) rates, will you prefer the measurement over the O4/O7 transfer, and accept directional bias bounds on remaining cross-pool transfers? (Determines whether H3 is a schema change or a ranking change.)

Is the Dirichlet kernel's intent "50 pseudo-observations total" or "moderate perturbation around nominal weights"? (The α floor in recommendation 1 is a no-op under the second intent but a spec change under the first.)

How many of the 19 cohort rows currently have matched cost+success on DeepSWE or Terminal-Bench 4.0? (If fewer than 8, the Spearman gate is not estimable and M3's minimum-n rule changes the release checklist.)

Will you accept demoting hard-expired Plan routes to diagnostic-only even if it temporarily empties the official Plan ranking?

Should the c_SWE companion column remain diagnostic-only, or should it be allowed to block the "recommended" label like the existing matched-cost divergence flag?

4. Verdict

VERDICT: HAS FEEDBACK