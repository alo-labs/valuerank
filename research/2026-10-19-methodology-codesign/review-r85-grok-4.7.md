0. Read check

I opened all 14 parts through the GitHub connector, in order, at commit c8b0dd4e0b1a5f337e974e14eec67fb057272832, and read each returned file to its end. The review below concerns the draft’s specification; I did not independently execute its build or validate its underlying evidence bundle.

First line, exactly:

ValueRank methodology — draft r167

Final sentences, in part order:

> Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

> Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

> These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status.

> Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

> Fixtures: two concordant reports 41 days apart, neither admitted earlier, where the older one leaves the partition and the route is diagnostic; a model with a current controlled measurement and a lapsed report pair, where the controlled route stays and the report route is diagnostic; a transfer from a lapsed report donor, which is diagnostic.

> The build counts its rows among the Plan rows resting on an owner assumption, by kind (marked †, E242).

Part 7 ends with a table row rather than a prose paragraph. Its final sentence, inside that row, is:

Cross-source agreement (E229, amending E125): AA's leaf is compared with tbench.ai's matched rows (Kendall τ_b on their common panel, per ranking, with the mean offset tbench.ai minus AA beside it, since a rank correlation cannot see a uniform level shift; today τ_b 0.74 and offset +1.7 points on 5 rows in the max-effort ranking and undefined (panel too small) on the AI Coding Daily ranking's 1), and a row whose leaf is a tbench.ai gap fill is marked "harness-mixed" (today, max-effort ranking: none; AI Coding Daily ranking: none)

> Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

> Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

> Ladder minimum (E215): with two or three, only the headline bar is pinned, because floor((n − 1)k/4) puts the quartile bars on the headline's position or a neighbour; from four configurations the three positions are distinct.

> Ranked configurations only (owner decision O43): a family listed under O38 with an indicative value (O41) is not a competitor in any frontier or bar output; each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

> Release tests. Omniscience vector above; Bug Hunt vector above; Index reconciliation (C_6 + C_HLE-Diamond + C_Omniscience + C_CritPt v2 reproduces AA's total within the E209 tolerance, the task counts taken from the registered v5 evaluations; the residual never enters C_W); Coding Agent Index fixtures (E82): the scored cost equals AA's pooled per-task-attempt mean × 290 (v2.0, O50); the raw telemetry sum and sum ÷ mean are preserved as diagnostics without requiring equality to 290 (fixture with unequal telemetry coverage, where mean × 290 differs from the sum and the row still scores and passes completeness); completeness has two predicates: a Coding Agent Index cost is complete when AA's missing- or declined-task markers are absent (O27), and an Index SDLC component cost also needs its row's Index reconstruction to pass (E209); aggregate/component exclusivity (an exactly reconciled decomposition leaves basket cost unchanged); repetition invariance (averaging extra evaluation repetitions does not multiply workload cost); workload migration changes W's hash and invalidates unreviewed Plan transport; basket persistence (a new cohort row with missing costs does not change W's hash); single clip predicate (all gate consumers call one function, with integer-boundary fixtures for several cohort sizes); split invariance (partitioning an execution family into accounting subcomponents leaves its pass cost and C^match unchanged; splitting a quality reporting leaf never creates or duplicates an execution-family weight — E55); kernel completeness (every stochastic input has executable parameters); price tests (E23): uniform price scaling cancels in Plan cost; arbitrary category-price changes cancel when measured consumption is proportional to the target-workload token vector; otherwise category repricing changes Plan cost by (p·x / p·u) and triggers a transport identification recheck (two-category fixture with different measured and target mixes); restoring a missing leaf moves correctly from S0 to S1; transfers-off never silently becomes API fallback in an interval output or a scenario panel (E167); a tighter quota cannot increase computed capacity; window-semantics fixtures above; adding an unrelated row cannot change common-panel diagnostics except via declared cohort-dependent quantities; a frozen bar does not force its setter as the answer (at freeze at least two population configurations reach H on displayed quality; E192), and each bar result publishes its count of R_W configurations that can qualify (E198a); cheapest fixtures (non-provisional and provisional singletons, unique cheapest, equal-cost tie → both in K_r; no self-comparison); interior-witness possible-frontier fixture (E43); completeness statuses (an AA declined- or missing-task marker → confirmed incomplete; an Index reconstruction that misses AA's total → unresolved; otherwise confirmed complete; the Coding Agent Index cost equals the per-task metric × 290); completeness (an AA-marked incomplete component fails FullCost and removes the row from R_W without changing its displayed score); session-start fixture (a schedule whose second burst starts a new session after the first session ends is feasible; capacity results carry a feasible schedule); interval decision statuses (an unresolved solve is never certified); widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic.

Part 13 ends mid-sentence, and part 14 continues it. I read through the actual end of part 13. Its last complete sentence is:

Each capture publishes the rendered-frontier entrants and exits against the previous capture, and the reconciliation report lists every frontier and near row with its rank status.

Its exact trailing fragment is:

Today the capture, the latest under Intelligence Index v5.0 (the 2026-10-31 capture was the first, O132), was taken at 2026-11-01T05:53:05Z, before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

> Revision history: omitted from this review copy (not normative); it is in draft-r167.md in the same folder of the repository.

The quotations above preserve wording while omitting inline Markdown emphasis used by the source.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

Specification inconsistency: the S1T paragraph still describes LiveBench categories as binomial after E311 explicitly withdrew that interpretation.

Issue: Part 8 correctly says LiveBench’s fractional category scores supply an independent-score variance bound, with a normal kernel, and that no binomial likelihood or Beta posterior is claimed. Part 9 subsequently describes LiveBench Overall as “each a binomial share of its published task count” inside the long S1T sampling prescription. E311 governs, so this is not a reason to change the adopted method, but the conflicting description remains.

Why it hurts the objective: A reproducer could reasonably classify LiveBench as one of O142’s Beta-drawn leaves rather than as an aggregate normal-kernel leaf. That would change the scenario law while leaving the point ranking unchanged. Adding independent variances is justified under the declared independence approximation, but it does not make fractional observations Bernoulli trials.
stat.yale
+1

Concrete change: Replace the LiveBench clause in Part 9 with a direct reference to the E256/E311 weighted-category normal-kernel definition. Explicitly exclude LiveBench, FrontierCode, AutomationBench and AI Coding Daily from the binomial-leaf allowlist.

What is new: E311’s statistical distinction is already adopted. This finding concerns the surviving contradictory instruction elsewhere in r167, not a request to reconsider E311.

The Index-reconciliation explanation attributes the residual to the wrong sum.

Issue: Part 3 first defines reconciliation over all nine v5 evaluations, then says “the six components sum above AA’s total.” Those are different quantities: the nine-evaluation reconstruction and the six-evaluation SDLC subtotal.

Why it hurts the objective: The current wording makes the completeness decision harder to audit. A small excess in the reconstructed nine-evaluation total does not establish that the six SDLC evaluations alone exceed the complete Index total. The draft need not identify the faulty evaluation, but it should identify which arithmetic identity failed.

Concrete change: Say: “The reconstructed nine-evaluation total exceeds AA’s published Index total by 0.03–0.04%; the affected row’s six scored Index components are therefore marked unresolved under E209.” Render the sign and percentage from the reconstruction object.

What is new: This does not challenge O141’s tolerance or E209’s conservative completeness treatment; it corrects the explanation of the observed failure.

An older description of removal-diagnostic anchor populations survives E317.

Issue: Part 3 says E64 and E172 “rebuild anchors from every row with a cost on the reduced workload.” Part 10 now correctly requires the registered E160/E184 eligible population, and measured Plan rows only under O157, with unavailable results below two eligible references.

Why it hurts the objective: “Every row with a cost” is materially broader than “eligible references.” Following the earlier sentence would mix the effect of component removal with an unintended change in valuation eligibility or Plan evidence provenance.

Concrete change: Replace the Part 3 parenthesis with a reference to E317, stating that reduced-workload eligibility is recomputed and that O94 rows remain excluded at a new diagnostic freeze.

What is new: E317 already supplies the right design. The remaining defect is the unamended earlier description, not the absence of an anchor-eligibility policy.

2. Methodology design recommendations

These are implementation-level refinements to existing decisions, not proposals for another ranking, new benchmark weights, evidence transfer, or synthetic allowances.

Priority 1 — Generate every sampling prescription from one executable leaf-type registry

The remaining LiveBench contradiction suggests that stream descriptions should be generated at the same granularity as numerical figures.

For each leaf, register:

text
observation_type
sampling_unit
effective_n_source
kernel_family
kernel_parameter_function
domain
active_streams
alternative_kernel
interpretation

Use explicit types such as:

Binary task outcome → O142 Jeffreys Beta kernel.

Bounded fractional task score → declared normal approximation using the independent-score variance bound.

Published estimate with standard error → registered source-supported approximation.

Fitted rating with unstated interval level → the separately labelled O39 approximation.

Bug Hunt planted-plus-unplanted count → E301/E309’s registered count construction.

For LiveBench, preserve the adopted formula:

𝜎
L
B
=
100
∑
𝑐
𝑤
𝑐
∑
𝑐
𝑤
𝑐
2
𝑝
~
𝑐
(
1
−
𝑝
~
𝑐
)
𝑛
𝑐
.
σ
LB
	​

=
∑
c
	​

w
c
	​

100
	​

c
∑
	​

w
c
2
	​

n
c
	​

p
~
	​

c
	​

(1−
p
~
	​

c
	​

)
	​

	​

.

Describe it as conditional on independent category/task contributions and the registered task-count assumptions—not as a source-established standard error or a binomial posterior. The omission of covariance terms follows from the independence approximation; in general those terms belong in the variance of an aggregate.
stat.yale
+1

Tests should establish that:

LiveBench cannot enter the Beta sampler.

Halving every category count multiplies the pre-clipping SD by 
2
2
	​

.

The generated prose, stream manifest and actual sampler name the same kernel and unit.

Any difference between analytic pre-clipping SD and simulated post-clipping dispersion is labelled rather than silently equated.

This preserves E311 and the existing sensitivity bracket.

Priority 2 — Generate reconciliation explanations from typed accounting objects

Extend E265’s figure rendering to include the identity being described, not just its result.

Each reconciliation should expose:

text
identity_id
included_component_ids
reconstructed_total
published_total
signed_residual
relative_residual
tolerance
status
affected_scored_component_ids

The prose generator can then distinguish:

Nine-evaluation Index reconstruction.

Six-evaluation scored SDLC subtotal.

Coding Agent Index mean-times-task-count construction.

Raw telemetry-sum diagnostic.

This is routinely refreshable from the public captures already required. It changes neither the workload nor completeness policy, but prevents a valid conservative flag from acquiring an unsupported explanation.

Priority 3 — Extend the normative-conflict check beyond numerical figures

E191 already resolves precedence; use that resolution to eliminate competing operational descriptions.

For anchor-building consumers, make the executable population definition the shared object:

References
⁡
=
EligibleRows
⁡
(
ranking
,
basis
,
𝑊
,
freeze policy
)
.
References=EligibleRows(ranking,basis,W,freeze policy).

The primary freeze, reduced-workload diagnostics and measured-evidence calibration should each declare their policy explicitly rather than restating eligibility in prose.

A useful regression fixture would include:

A complete, valuation-compatible API row.

A row with a published but unresolved component.

An O94 pricing-omission row.

A measured Plan row.

An assumption-based Plan row.

An API-fallback Plan row.

Assert each consumer’s reference IDs and exclusion reasons. In particular, a reduced-workload diagnostic must not silently revert to “all rows with costs.”

No new public-data collection is needed for these recommendations.

3. Questions for the owner

None.

The remaining corrections follow the owner/editor decisions already in force; their resolution does not require changing the objective, weights, cohort rule, exact-variant policy or Plan numerator policy.

4. Verdict

Within its explicitly restricted claim scope, the draft now distinguishes displayed value arithmetic from identified Plan economics, published-record interval claims from benchmark-noise scenarios, and main-workload comparisons from subset-workload ordering. I found no remaining medium-or-higher issue that warrants reopening the adopted methodology.

The remaining feedback is limited to internal specification consistency and reproducibility safeguards. This is not an independent verification that the implementation or captured evidence satisfies every stated gate.

VERDICT: HAS FEEDBACK