0. Read check

I opened all 14 parts through the GitHub connector, in order, at commit 07c82f1afe262b76aa1dfc5b226035db67653563, and read every returned file to its end. Part 13 ends mid-sentence; part 14 supplies its continuation.

Draft’s first line:

ValueRank methodology — draft r162

Final sentence of each part, in order:

1.

Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

2.

Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

3.

These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status.

4.

Fable 5.1 is not a donor-error gauge (owner decision O35, 2026-10-21): Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

5.

A schema change moves the route to the possibly-superseded stage.

6.

Domain validity is separate from evidence completeness.

7.

GPQA Diamond retired at this quality version (E48): AA no longer evaluates new frontier models on it (no value for 10 of 19 cohort rows in the 2026-10-17 snapshot) |

8.

Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

9.

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

10.

Each bar table publishes every row's displayed margin to H beside its interval statuses.

11.

Feasibility prerequisite (E79): before any decision, the decision's full constraint component (all connected shared variables and identities) must have a certified feasible witness checked against the original constraints; certified infeasible → "inconsistent evidence", no frontier or bar labels for the affected output, release-blocking for that output with the conflicting records listed; feasibility unresolved → "unresolved", no confirmed or definite label (fixtures: individually valid intervals whose shared identity has an empty intersection; a feasible outer box whose original constrained set is empty — neither may produce a confirmed, definite or certified-possible result).

12.

Release tests: Omniscience vector above; Bug Hunt vector above; Index reconciliation (C_6 + C_HLE-Diamond + C_Omniscience + C_CritPt v2 reproduces AA's total within the E209 tolerance, the task counts taken from the registered v5 evaluations; the residual never enters C_W); Coding Agent Index fixtures (E82): the scored cost equals AA's pooled per-task-attempt mean × 290 (v2.0, O50); the raw telemetry sum and sum ÷ mean are preserved as diagnostics without requiring equality to 290 (fixture with unequal telemetry coverage, where mean × 290 differs from the sum and the row still scores and passes completeness); completeness has two predicates: a Coding Agent Index cost is complete when AA's missing- or declined-task markers are absent (O27), and an Index SDLC component cost also needs its row's Index reconstruction to pass (E209); aggregate/component exclusivity (an exactly reconciled decomposition leaves basket cost unchanged); repetition invariance (averaging extra evaluation repetitions does not multiply workload cost); workload migration changes W's hash and invalidates unreviewed Plan transport; basket persistence (a new cohort row with missing costs does not change W's hash); single clip predicate (all gate consumers call one function, with integer-boundary fixtures for several cohort sizes); split invariance (partitioning an execution family into accounting subcomponents leaves its pass cost and C^match unchanged; splitting a quality reporting leaf never creates or duplicates an execution-family weight — E55); kernel completeness (every stochastic input has executable parameters); price tests (E23): uniform price scaling cancels in Plan cost; arbitrary category-price changes cancel when measured consumption is proportional to the target-workload token vector; otherwise category repricing changes Plan cost by (p·x / p·u) and triggers a transport identification recheck (two-category fixture with different measured and target mixes); restoring a missing leaf moves correctly from S0 to S1; transfers-off never silently becomes API fallback in an interval output or a scenario panel (E167); a tighter quota cannot increase computed capacity; window-semantics fixtures above; adding an unrelated row cannot change common-panel diagnostics except via declared cohort-dependent quantities; a frozen bar does not force its setter as the answer (at freeze at least two population configurations reach H on displayed quality; E192), and each bar result publishes its count of R_W configurations that can qualify (E198a); cheapest fixtures (non-provisional and provisional singletons, unique cheapest, equal-cost tie → both in K_r; no self-comparison); interior-witness possible-frontier fixture (E43); completeness statuses (an AA declined- or missing-task marker → confirmed incomplete; an Index reconstruction that misses AA's total → unresolved; otherwise confirmed complete; the Coding Agent Index cost equals the per-task metric × 290); completeness (an AA-marked incomplete component fails FullCost and removes the row from R_W without changing its displayed score); session-start fixture (a schedule whose second burst starts a new session after the first session ends is feasible; capacity results carry a feasible schedule); interval decision statuses (an unresolved solve is never certified); widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic.

The last complete sentence is:

Each capture publishes the rendered-frontier entrants and exits against the previous capture, and the reconciliation report lists every frontier and near row with its rank status.

The file then ends with this incomplete sentence:

Today the capture, AA's first under Intelligence Index v5.0, was taken at 2026-11-01T05:53:05Z, before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

14.

Revision history: omitted from this review copy (not normative); it is in draft-r162.md in the same folder of the repository.

The review below concerns the specification as read, not an audit of its implementation or the underlying benchmark captures. References identify the supplied parts and governing rules.

1. Findings by severity
Critical

None.

High
H1. O163 makes Bug Hunt unbounded, but the composite still declares every leaf to be on 0–100

Issue: Part 7 explicitly defines Bug Hunt as an unscaled sum with no ceiling and gives a valid score of 109.6. Part 10’s normative definitions nevertheless state that “z and u are on 0–100,” and bound every missing leaf by 
[
0
,
100
]
[0,100]. Part 7 also retains a general normalization formula that clips normalized leaves to 100.

Why it hurts the objective: Different conforming-looking implementations can now produce different quality scores, bars and ranks. More importantly, a valid observed Bug Hunt score can exceed the formal upper bound used when that same observation is unavailable. That breaks the intended interpretation of evidence-unavailability bounds and can invalidate the evidence-loss tests.

The nominal 8%, 12% and 15% Bug Hunt weights also cease to represent bounded allocations of quality points. This is not necessarily wrong, but the methodology must distinguish a coefficient from a maximum contribution.

Concrete change:

Explicitly exempt Bug Hunt from the generic clipping formula and 0–100 domain.

Give each leaf a registered raw domain, transformed domain and missing-evidence domain.

Under O163 unchanged, Bug Hunt’s missing-evidence domain must allow an unbounded upper end unless a defensible finite bound is documented.

Make every bounds, deletion, indicative-value and validation consumer read those registered domains.

State that total quality is not necessarily bounded by 100 under O163.

What is new: This is a propagation defect introduced by the recent O163 transformation, not a repetition of an earlier objection to Bug Hunt’s weight, harness or repository coverage. It can be fixed without challenging the owner’s plain-sum decision.

H2. O157 invalidates the assertion that API and Plan anchor availability cannot differ

Issue: Part 7 correctly requires at least two measured Plan reference rows under O157. It then says workload migration is atomic across bases and that “their availability cannot differ.” But a complete, valuation-eligible API reference panel does not imply that even one configuration has an eligible measured Plan route.

Why it hurts the objective: A routine loss of measured Plan evidence—for example, all relevant measurements becoming diagnostic after grace—can leave the API basket fully anchorable while the Plan basket is not. The draft does not give one consistent operational result: defer the API workload migration, hold both bases, or publish API scores with unavailable Plan scores.

Concrete change: Define availability separately:

𝐴
A
P
I
(
𝑊
)
=
1
{
∣
𝑃
A
P
I
(
𝑊
)
∣
≥
2
}
,
𝐴
P
l
a
n
(
𝑊
)
=
1
{
∣
𝑃
P
l
a
n
,
m
e
a
s
u
r
e
d
(
𝑊
)
∣
≥
2
}
.
A
API
	​

(W)=1{∣P
API
	​

(W)∣≥2},A
Plan
	​

(W)=1{∣P
Plan,measured
	​

(W)∣≥2}.

Then state the migration rule explicitly. Preserving atomic migration is possible: require both predicates and defer migration when either fails. Remove the assertion that one implies the other, and add fixtures for sufficient API references but zero or one measured Plan reference.

What is new: This is a consequence of O157’s measured-only Plan anchor panel. It is not a request to restore assumptions or API fallbacks as Plan anchor setters.

Medium
M1. The “mean-preserving” S1T alternative is not mean-preserving after clipping

Issue: Part 9 describes O154’s alternative as a Beta draw recentered on the published score and then clipped to 0–100. Recentering preserves the mean before clipping, not generally afterward.

For example, when the published score is zero, recentering a non-degenerate Beta draw gives a zero-mean variable with positive and negative values. Clipping its negative values to zero leaves a strictly positive mean. The corresponding problem occurs at 100.

Why it hurts the objective: The alternative is intended to distinguish sensitivity to Jeffreys shrinkage from sampling dispersion. Boundary clipping reintroduces a mean shift, so comparisons cannot be interpreted as removing that shift alone.

Concrete change: Either:

Rename it “recentered-and-clipped alternative” and publish its actual post-clipping mean shift; or

Implement a genuinely mean-preserving bounded kernel.

For 
0
<
𝑝
<
1
0<p<1, a straightforward option is:

𝑋
∼
Beta
⁡
(
𝜅
𝑝
,
𝜅
(
1
−
𝑝
)
)
,
X∼Beta(κp,κ(1−p)),

with a registered concentration rule. At 
𝑝
=
0
p=0 or 
1
1, a bounded distribution with that exact mean must be a point mass. State that boundary tradeoff rather than promising both positive spread and exact mean preservation.

What is new: O154 was adopted to expose shrinkage sensitivity; this finding concerns whether its specified alternative actually performs that function. It does not challenge O142’s primary Jeffreys kernel.

M2. The workload cross-check contradicts the draft’s qualified interpretation of separability

Issue: Part 1 says the net direction of the separability approximation is not established: shared-task correlation and attempt averaging can narrow it, while omitted uncertainty sources can widen it. Part 10 instead concludes that because cost noise is omitted, “the threshold is a lower bound on the true one.”

Why it hurts the objective: Readers receive conflicting interpretations of the uncertainty beside the primary ordinal ranking. Omitting cost variation alone does not establish a lower bound after simultaneously changing task dependence, attempt treatment and covariance assumptions.

Concrete change: Replace the lower-bound assertion with:

The threshold omits cost variation. Its net direction relative to a fully paired deployment-level comparison is not established.

If a narrower conditional statement is wanted, specify the assumptions under which adding an independent cost-noise term increases variance. Generate both passages from the same interpretation object.

What is new: The draft already acknowledges the ambiguity correctly in Part 1. The finding is the contradictory stronger claim in Part 10, not a request for another uncertainty diagnostic.

Low
L1. Several “current” explanations still describe states that the draft itself has superseded

Issue: Examples include:

Part 8 says Kimi K3.1 Pro and MiMo-V2.6-Pro left the cohort and that their rules stand “for [their] return,” although O145 has already retained them and they are ranked in the current release.

Part 13 calls the November 1 chart capture AA’s “first under Intelligence Index v5.0,” while Parts 7 and 14 describe earlier v5 captures.

Part 2 says no gap-fill offset exists “since O136 retired FrontierCode’s,” although O153 has reinstated the FrontierCode cross-source comparison.

Why it hurts the objective: These do not necessarily change scores, but they obscure which evidence state and diagnostics a buyer is actually reading.

Concrete change: Separate historical transition notes from current-state statements, and extend E265’s checks beyond counts to predicates such as retained membership, active cross-source checks and capture chronology.

What is new: These are specific stale explanations remaining after the adopted figure-rendering and retention changes, not a general request to adopt figure generation again.

2. Methodology design recommendations
Priority 1 — Make leaf domains executable, not implicit

Implement one leaf specification consumed by scoring, intervals, scenarios and documentation:

text
leaf_id
raw_domain
transform_id
transformed_domain
missing_evidence_domain
rounding_rule
sampling_kernel_id
maximum_contribution_status

For O163 unchanged:

text
transformed_domain = [0, +infinity)
missing_evidence_domain = [0, +infinity)
maximum_contribution_status = unbounded

Add fixtures using the draft’s own 109.6 example:

The observed value remains 109.6 everywhere.

No generic clipping path changes it to 100.

Removing the observation cannot produce an upper bound below 109.6.

A missing Bug Hunt observation is not assigned a finite sampling law without an explicit convention; bounds-only is acceptable.

Documentation states whether a composite has a finite upper bound.

This preserves exact-variant evidence and O163 while restoring consistency across the mathematical machinery.

Priority 2 — Turn anchor availability into a two-basis state machine

Publish separate API and measured-Plan reference counts for each proposed workload.

API anchorable	Plan anchorable	Required explicit outcome
Yes	Yes	Migration may proceed, subject to existing gates
Yes	No	Defer atomic migration, or use an explicitly owner-approved separate-publication rule
No	Yes	Defer atomic migration
No	No	Defer migration; retain the previous valid release as specified

Distinguish failure to create a new anchor object from later evidence expiry under an already frozen object. The draft already says frozen references persist after evidence loss; the state machine should preserve that distinction.

No new public data is required: this uses the existing completeness, valuation and route-admission records.

Priority 3 — Validate the realized moments of every advertised sampling alternative

For each kernel, publish:

Intended mean.

Actual analytical mean where available.

Actual post-transformation mean.

Boundary mass.

Whether clipping changes the mean.

The resulting composite mean shift at nominal weights.

For the current recentered-and-clipped alternative, the actual post-clipping shift—not just the initial Jeffreys shift—is the relevant diagnostic. Add explicit tests at 0%, 100% and near-boundary scores.

This improves O154’s existing sensitivity rather than introducing another stream.

Priority 4 — Generate interpretation statements from one uncertainty contract

Extend the existing stream manifests with a shared field such as:

text
direction_relative_to_full_paired_uncertainty = not_established

Use it for the separability summary, workload-cross-check discussion and noise-band explanation. Keep distinct:

Reporting-precision robustness.

Task-sampling approximation.

Omitted cost variation.

Unmeasured deployment and harness variation.

This addresses M2 without changing weights, labels or the owner-selected estimand.

Priority 5 — Add semantic document checks for amended policies

Extend E265 with targeted assertions:

A currently retained configuration cannot be described as awaiting cohort return.

An active source comparison cannot be described as retired.

A capture cannot be called the first of a benchmark version when an earlier registered capture uses that version.

A leaf’s prose domain must match its executable domain.

Anchor-availability prose must match the registered reference predicates.

These checks are routine-refresh compatible and require no additional benchmark measurements.

3. Questions for the owner

With O163 unchanged, is an unbounded Bug Hunt contribution—and consequently a potentially greater-than-100 quality composite—intentional? This determines whether the remedy is purely domain propagation or an “Owner decision challenge” proposing a bounded transformation.

If a proposed workload has enough eligible API references but fewer than two eligible measured Plan references, should atomic migration defer both bases, or may the API basis migrate while Plan scoring remains unavailable? O157 makes this a reachable policy state.

4. Verdict

The draft has substantial safeguards against evidence transfer, unsupported Plan claims and misleading cross-workload comparisons. My remaining material feedback concerns consistency: O163 has not been propagated through the score domains, O157 leaves an anchor-availability contradiction, and two uncertainty descriptions claim properties their specified procedures do not establish. These are specification findings; I have not verified whether the implementation already handles them differently.

VERDICT: HAS FEEDBACK