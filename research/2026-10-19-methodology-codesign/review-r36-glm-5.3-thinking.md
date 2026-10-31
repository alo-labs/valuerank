This file is a methodology review task for the "ValueRank" draft — I'll verify the key factual claims about Artificial Analysis's measurement practices via web search before writing the structured review.
The draft's key verifiable claims about AA's measurement practices check out so far — the Coding Agent Index cost is a pooled per-task-attempt average, Index cost excludes repeats, GDPval Elo is frozen at evaluation. Let me verify the remaining factual claims: LiveBench 2.0's suite composition, AA's IFBench coverage, and tbench.ai's harness heterogeneity.
artificialanalysis
+2
Reviewed draft r35 against its stated objective. The AA-side factual claims I could check externally all hold: AA's Coding Agent Index cost is a pooled per-task-attempt average, Index cost is computed on tokens used across evaluations excluding repeats, the Index comprises DeepSWE v1.1 + Terminal-Bench 4.0 + SWE-Atlas-QnA (66 and 124 tasks respectively), AA-Omniscience scores +1 correct / −1 incorrect / 0 abstention over 6,000 questions, GDPval Elo is frozen at evaluation for index stability, and LiveBench 2.0 indeed has no instruction-following category (Agentic, Reasoning, Coding, Browser Use, Data Analysis, Research, Design). Findings below.
livebench
+9

1. Findings by severity

Critical

None.

High

H1 — The Plan basis has no active path to a single identified M_W, and the draft contains no prioritized mechanism to create one. The data note states no Plan route has an identified M_W today. Transport identification (E44/E84) requires a workload-pass demand object d_iW that reconciles to C_i,W, and the draft's only named sources for demand evidence are third-party saturation measurements and end-user receipts — scarce, workload-mismatched, and outside ValueRank's control. Meanwhile the Plan basis carries the objective's differentiating claim (subscription-plan economics), and its heaviest machinery (E105 multiple certification, E115 window-semantics identification, E54/E80 funding-aware capacity) is currently vacuous. The E61 "exploratory" label discloses the state, but the state is structural, not transient: as written, nothing in the methodology can plausibly move any route to identified. Concrete change: make demand-object construction a first-class versioned pipeline from AA's own published telemetry — AA publishes per-model token usage for its evaluations segmented by token category — assembling d_ie for the seven admitted AA Index components, enforcing the E84 identity p·d_ie = C_i,e, and publishing the demand registry. M_W identification then reduces to quota-capacity evidence (B_w), which public plan documentation plus receipts can bound, activating the "publicly evidenced additive capacity model" transport class already in the E67 taxonomy.
artificialanalysis
+1

Medium

M1 — The Terminal-Bench quality leaf compares model+harness stacks across models, with no cross-harness diagnostic. tbench.ai's leaderboard is organized as model×agent rows, with the same model appearing under multiple agents at different resolution rates. The pre-registered "vendor-neutral harness first" preference still yields a leaf where model A is scored under one harness and model B under another whenever coverage differs. This partially measures harness rather than model on a 10% SWE leaf. Unlike Bug Hunt (stress branch E19, explicit model+harness disclosure), TB has no corresponding check. Concrete change: publish a restricted same-harness TB variant (single named default harness; rows without it missing) alongside the primary leaf, with a Kendall τ_b between the two orderings on their common panel, and mark the primary leaf "harness-mixed" per row wherever the preference could not be satisfied uniformly.
tbench

M2 — The realized cost–quality tradeoff is set by cohort extremes, and the influence flag is one-sided. The exchange rate is 100β·ln2 / ((1−β)·ln(c_H/c_L)) with anchors at reference min÷2 and max×2, so the anchor log-range — effectively a second cost-weight parameter — is determined by the two most extreme rows and shifts with every anchor migration, while β = 25% is presented as fixed. The same models can exchange rank between anchor versions with no model-level change; the clip and 5-point-swing gates only catch large effects. Separately, the influence flag fires only when cost's share is under 10%, never when quality's share is correspondingly negligible. Concrete change: (a) flag symmetrically (e.g., cost share > 90% → "quality not discriminating"); (b) publish the realized exchange-rate series across anchor versions beside the existing c_H/c_L sensitivity curve; (c) add a named diagnostic re-anchoring on trimmed reference costs (e.g., 10th/90th percentile with the same padding), reported as rank shifts only, without changing the primary anchor.

Low

L1 — E72 overclaims with "anytime-valid". The α/16-per-look Clopper–Pearson rule over 16 pre-declared looks is a Bonferroni union-bound procedure, valid for the declared per-event guarantee, not an anytime-valid interval in the sequential-testing sense (valid under continuous monitoring). Rename to "repeated-look-adjusted", or adopt a confidence-sequence construction if continuous monitoring is actually intended.

L2 — Omniscience leaf gives cardinal mid-scale credit for total abstention (Owner decision challenge, O28). The monotonicity defense is ordinal; cardinally, an all-abstaining configuration receives z = 50 on a 10%-weight leaf — five free composite points for zero delivered knowledge, material against adjacent-rank gaps. I note the retired (2A+N)/3 was worse (all-abstention scored 66.7), so this is not a reversion argument. What is new: the kept diagnostics (accuracy, conditional hallucination rate) do not reveal abstention mass, so a reader cannot see how much of any z is abstention-driven. Concrete change: publish abstention share (a/T) and partial share per row beside z — AA exposes the underlying counts — and optionally show z under an abstention-penalised alternative as a named sensitivity, not a replacement.
artificialanalysis
+1

L3 — Data nits. The draft dates LiveBench 2.0 at 2026-10-14; livebench.ai shows release and last update 2026-10-13 — trivial, but the registry should pin the exact release tag. Also, the GDPval transform (E−500)/2000 is asserted as "AA's published integration transform, verified at implementation"; AA documents a fixed normalization range for Elo integration but not its constants on the pages I could check, so the registry pin needs a retrievable citation.
livebench
+1

2. Methodology design recommendations

Demand-object pipeline (from H1) — highest priority. Build D = {d_ie} for all 19 rows on the seven admitted AA Index components from AA's per-category token telemetry; enforce p_release·d_ie = C_i,e per E84 (no rescaling, incompatible rows stay unidentified); publish as a hashed, versioned registry object with the same data-refresh/migration discipline as the workload object. Expected yield: routes with evidenced quota schemas become at minimum set-identified, the E74 lower-bound convention and E105 certification machinery start binding, and the E61 "exploratory" label becomes a data-driven state rather than a structural one.
artificialanalysis

Terminal-Bench same-harness variant (M1). One named default harness (e.g., the vendor-neutral harness AA itself uses for its Index TB run ); restricted leaf plus τ_b versus the preference-selected ordering on the common panel; per-row "harness-mixed" marker. Implementable from the public tbench.ai leaderboard.
tbench
+1

Symmetric influence flag and exchange-rate stability disclosure (M2). Add the >90% cost-share flag; publish the exchange-rate series across anchor versions; trimmed-anchor rank-shift diagnostic. All three are display-level changes to existing statistics, implementable from the registry alone.

Category-price revaluation stress branch (new S2 branch, API basis). Revalue every row's basket token vector under one common synthetic category price vector (cohort-median category prices, or a reference provider's list), holding each row's own token mix fixed; publish rank shifts and the own-price vs common-price cost rank correlation. This separates usage efficiency from provider price structure (cache-write billing, cache-hit discounts ) — distinct from E122 (provider-level median for open weights) and E23 (Plan transport recheck), both of which operate at a different level. Data source: AA's cost-per-task segmentation by token type.
artificialanalysis
+2

Abstention-mass disclosure (L2). Add a/T and partial/T per row beside the Omniscience leaf, with a named abstention-penalised z alternative in the sensitivity layer.

Terminology fix (L1). One-line edit to E72's wording, or a genuine confidence-sequence implementation if the sequential rule is meant to support arbitrary monitoring times.

LiveBench 2.0 cost companion (new, cheap). LiveBench 2.0 publishes a cost-per-successful-task column on its own contamination-refreshed workload; adopt it as an O14-style independent cost companion alongside c_SWE, with the same >50%-deviation flag treatment. Independent of AA execution, so it also strengthens the E62/E66 independent-source checks' cost side.
livebench

3. Questions for the owner

Is an owner-run or commissioned O11-class controlled saturation measurement on (or reconcilable to) the SDLC basket workload within scope, or must Plan numerators remain passively observed public reports? This decides whether recommendation 1 can ever produce a point-identified M_W or only set-identified bounds, and whether the Plan interval machinery will bind in the foreseeable future.

Is the influence flag intentionally one-sided (cost share < 10% only)? If the intent is "cost is not discriminating," is there a reason not to flag the quality-not-discriminating mirror?

For the Terminal-Bench quality leaf, when the vendor-neutral preference cannot be satisfied uniformly across the cohort, does the owner prefer coverage (current design) over comparability (single-harness restriction)? This decides whether the same-harness variant should be a diagnostic or the primary leaf.

Where is AA's GDPval Index-integration transform (the (E−500)/2000 constants) publicly documented, so the registry can pin it with a retrievable citation rather than an implementation-time verification?

4. Verdict

VERDICT: HAS FEEDBACK