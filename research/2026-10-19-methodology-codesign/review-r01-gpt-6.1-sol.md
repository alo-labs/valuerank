1. Findings by severity
Critical

Plan scores violate the fixed exact-variant evidence policy. Issue: Applying Opus’s multiple to other Claude models, a common GPT multiple across variants, or an unsupported provisional multiple transfers evidence or imputes a missing value. Labelling it “assumption” does not resolve that conflict. Why it hurts the objective: These substitutions directly drive the subscription advantage—the principal distinction ValueRank adds to AA. SemiAnalysis explicitly measures the (plan, model, workload) tuple because subscription-credit ratios differ from API-price ratios.
newsletter.semianalysis
 Recommended change: Remove transferred and unsupported multiples from the official ranking. Keep them only in a separate, unranked scenario view. Admit controlled projections only for the exact measured variant and supported workload. Distinguish “no subscription route exists” from “route exists but eligible evidence is missing”; neither establishes a measured plan cost.

Available-dimension renormalisation makes the leaderboard compare different definitions of quality. Issue: A model missing DeepSWE and Bug Hunt is assessed without the two highest-priority dimensions, while competitors bear those dimensions’ outcomes. Scoring a model without cost on quality alone also changes its quality weight from 75% to 100%. Why it hurts the objective: Missing evidence can improve placement, and a high rank need not demonstrate software-engineering value or affordability. Publishing coverage does not repair the comparison. Recommended change: Require a common, versioned evidence panel for official ordinal comparisons. Keep every eligible family visible, but mark incomplete rows “insufficient comparable evidence,” rather than excluding them from the cohort or inventing values. Publish missing-data bounds and shared-panel comparisons separately. Never issue an overall value rank without cost.

The Plan formula treats maximum utilisation as actual subscriber economics. Issue: Dividing API cost by the highest eligible multiple implicitly amortises a subscription over the usage supporting that multiple. It ignores whether a user consumes enough work to justify the fee and whether their schedule permits that consumption. Why it hurts the objective: The best plan at saturation can be poor value for a light user. SemiAnalysis’s results use an assumed token mix and measurements across short-window, weekly and sometimes model-specific meters; they are not a workload-independent monthly discount.
newsletter.semianalysis
 Recommended change: Rank plans by explicit monthly workload scenarios, including the full fee, attainable capacity and overflow cost. Retain the current calculation only as a labelled “full-utilisation effective-cost scenario,” with workload compatibility stated.

High

The default score is a preference index, not a direct measure of lowest cost per delivered value. Issue: An additive 75/25 score permits quality to compensate for cost according to arbitrary normalisation ranges. Meanwhile, dividing cost by Intelligence Index already rewards intelligence before quality receives its separate 75%. Why it hurts the objective: The winner need not minimise dollars per useful outcome. Cost divided by a composite index point also lacks an established interpretation as cost per completed task. Recommended change: Lead with cost–quality frontiers and “cheapest meeting a quality threshold.” Add dollars per successful task only where matched cost and success measurements exist. Retain the weighted score as a secondary preference tool, not the definitive lowest-cost answer.

The AA cost definition needs reconciliation with the current public source. Issue: The draft calls AA cost “total USD cost” and “token efficiency,” without identifying the exact source field. AA currently distinguishes total cost from its displayed weighted cost per task; the latter incorporates input, cache-hit, cache-write, reasoning and answer prices, with benchmark weighting.
artificialanalysis
 Why it hurts the objective: Total-suite cost and weighted per-task cost are not interchangeable. Dollar cost also combines token consumption and price rather than measuring token efficiency alone. Recommended change: Audit the imported field, units, suite version and weighting before accepting the reported USD/point range or placements. Preserve the owner’s rendered-frontier cohort rule; reconcile and document the cost field without recomputing membership. Publish token consumption separately from monetary cost.

Cohort-relative normalisation can change preferences when no existing model changes. Issue: Quality ranks discard performance gaps; cost min–max scaling changes with the cohort’s endpoints. Adding a cheap or expensive model can therefore change the effective cost–quality trade-off between existing models. Why it hurts the objective: Readers can mistake a cohort-composition effect for a change in practical value. Small benchmark differences can also receive large rank-score differences. Recommended change: Use raw benchmark magnitudes with frozen, published transformations and cost anchors. Version anchor changes separately from routine data refreshes.

Model, agent stack and access route are not consistently joined. Issue: Evidence may be exact within each source yet still describe different systems: an AA configuration, a provider-native coding agent, an owner harness and a subscription product. Selecting one family configuration is also unspecified. Why it hurts the objective: An exact model name alone does not establish that subscription users receive the evaluated effort, fallback behaviour, tools or harness. Recommended change: Publish a deterministic configuration-selection rule and a configuration manifest. Treat incompatible harness results as separate stack evidence, not interchangeable measurements. Require plan-route compatibility before attaching a subscription discount to evaluated quality. AA’s coding methodology explicitly specifies agent tooling and execution restrictions, illustrating why this matters.
artificialanalysis

Overlapping benchmarks obscure the intended weighting. Issue: Intelligence Index is included alongside many of its constituents, and it also enters the cost denominator. AA’s current composite includes GDPval-AA, AutomationBench, Terminal-Bench, SciCode, HLE, CritPt, Omniscience and LCR.
artificialanalysis
 Why it hurts the objective: Nominal weights do not describe total influence, and general-intelligence evidence is counted through several paths. Recommended change: Use a non-overlapping hierarchy. Keep Intelligence Index as a diagnostic if its components are scored separately. Also explicitly distinguish DeepSWE from Coding Agent Index: AA’s current Coding Agent Index combines three benchmarks, rather than being another name for DeepSWE.
artificialanalysis

Medium

Uncertainty and source quality do not affect how confidently winners are presented. Issue: Tenths-of-a-point scores and deterministic tiebreakers imply precision despite small task sets, rounded inputs and heterogeneous evidence. Why it hurts the objective: A nominal winner may reflect sampling noise, a particular account or an unauditable claim. SemiAnalysis itself reports measurement ranges and observed account-level limit variation.
newsletter.semianalysis
 Recommended change: Publish uncertainty intervals where supported, sensitivity ranges otherwise, and unresolved rank bands. Keep independent measurements, provider claims and end-user claims distinguishable; publish a measured-only comparison rather than inventing confidence penalties.

Output tokens per second is not completion speed, and non-hallucination is not unconditional reliability. Issue: Decode speed omits the volume of reasoning, tool calls and overhead required to finish work. Omniscience’s hallucination rate is conditional on non-correct responses, so its complement rewards abstention behaviour rather than directly measuring successful answers.
artificialanalysis
+1
 Why it hurts the objective: These dimensions can reward behaviour different from fast, useful completion. Recommended change: Prefer matched end-to-end completion time where public; otherwise label tokens/s narrowly and keep it outside outcome quality. Group Omniscience accuracy and uncertainty management under one explicit reliability budget, displaying both definitions.

Low

Edge cases and reproducibility contracts are underspecified. Issue: Normalisation is undefined for one observed quality value or identical cost endpoints. The draft also lacks explicit refresh, expiry and historical-reproduction rules. Why it hurts the objective: Routine updates can silently change scoring behaviour or preserve stale subscription economics. Recommended change: Add deterministic edge-case handling, dated source snapshots, parser tests, evidence-expiry rules and a per-release score-change decomposition. Publish the selection manifest and raw data alongside the methodology.

2. Methodology design recommendations
1. Separate eligibility, evidence and ranking

Keep the fixed family cohort intact. Assign each row independent statuses:

Cohort eligibility: the observed AA frontier or qualifying near-frontier evidence.

Configuration identity: model/version, effort, fallback, harness and tool restrictions.

Quality comparability: complete common panel or incomplete.

API-cost availability.

Subscription route and eligible multiple availability.

An incomplete row remains visible but does not receive an unsupported official placement. Provider claims should not overwrite independent measurements; retain both and show any discrepancy.

For each observation, publish benchmark version, source, run date, retrieval date, configuration, sample size, precision and evidence class. Refresh public leaderboards and prices routinely; expire plan evidence after a stated period without silently replacing it with an assumption.

2. Make the primary answer conditional on demonstrated quality

For each fixed workload profile 
𝑤
w, publish:

𝑖
∗
(
𝑞
,
𝑤
)
=
arg
⁡
min
⁡
𝑖
:
𝑄
𝑖
≥
𝑞
𝐶
𝑖
(
𝑤
)
i
∗
(q,w)=arg
i:Q
i
	​

≥q
min
	​

C
i
	​

(w)

This answers “which model is cheapest while meeting this quality requirement?” Publish several predefined thresholds and the full cost–quality frontier.

Where a public source reports matched task cost 
𝐶
𝑖
𝑏
C
ib
	​

 and success probability 
𝑝
𝑖
𝑏
p
ib
	​

, additionally report:

𝐷
𝑖
𝑏
=
𝐶
𝑖
𝑏
𝑝
𝑖
𝑏
D
ib
	​

=
p
ib
	​

C
ib
	​

	​


Interpret this as observed spend per successful outcome across comparable attempts—not guaranteed retry cost or production productivity. Include failed-attempt spend, and do not combine cost from one harness with success from another.

Where those measurements are unavailable, say so. AA-suite cost remains a useful proxy, not a measured software-engineering bill.

3. Replace a universal Plan discount with demand scenarios

For monthly demand 
𝑁
N, exact route 
𝑝
p, workload 
𝑤
w, fee 
𝐹
𝑝
F
p
	​

, attainable capacity 
𝐾
𝑖
𝑝
(
𝑤
)
K
ip
	​

(w), and matched API cost per work unit 
𝑎
𝑖
(
𝑤
)
a
i
	​

(w):

𝐶
𝑖
𝑝
m
o
n
t
h
(
𝑁
,
𝑤
)
=
𝐹
𝑝
+
𝑎
𝑖
(
𝑤
)
max
⁡
{
0
,
𝑁
−
𝐾
𝑖
𝑝
(
𝑤
)
}
C
ip
month
	​

(N,w)=F
p
	​

+a
i
	​

(w)max{0,N−K
ip
	​

(w)}

This formula assumes overflow can legally and technically use the matched API route. Otherwise label the scenario infeasible beyond capacity.

If eligible evidence supplies only an API-equivalent multiple 
𝑀
𝑖
𝑝
(
𝑤
)
M
ip
	​

(w), define capacity in API-dollar units:

𝐵
𝑖
𝑝
(
𝑤
)
=
𝐹
𝑝
𝑀
𝑖
𝑝
(
𝑤
)
B
ip
	​

(w)=F
p
	​

M
ip
	​

(w)

Use it only with the supported workload mix and temporal assumptions. Publish low-demand, regular-use and saturation scenarios; choose the cheapest evidenced route separately for each. SemiAnalysis’s public methodology supports this workload-specific interpretation, but not arbitrary extrapolation to other models or schedules.
newsletter.semianalysis

No provider quota enters the numerator. Provider documentation can establish fee, access conditions and permitted interfaces.

4. Adopt a transparent, non-overlapping quality hierarchy

A reasonable initial default, subject to owner validation:

Quality group	Weight within quality	Implementation
Software-engineering outcomes	60%	DeepSWE 30%, Bug Hunt 20%, Terminal-Bench 10%
General professional work	20%	GDPval-AA 10%, AutomationBench-AA 10%
Reliability and instruction compliance	10%	Omniscience reliability 5%, instruction following 5%
Long-context and scientific capability	10%	LCR 5%; HLE, GPQA, SciCode and CritPt share 5%

These are proposed priorities, not empirically established user utilities. Keep AA Intelligence Index and decode speed as diagnostics.

Use percentage-point magnitudes directly where meaningful. For Elo-like metrics, use win probability against a frozen reference configuration when the necessary public reference data exist. Otherwise freeze and publish a bounded transformation; do not treat raw Elo as percentage accuracy.

Choose a common scoring panel before each methodology release. If the full panel lacks sufficient exact evidence, publish a narrower, explicitly named comparison rather than silently redistributing each row’s weights.

5. Preserve missingness while exposing its consequences

For fixed weights summing to one and observed normalised values 
𝑧
𝑖
𝑗
∈
[
0
,
100
]
z
ij
	​

∈[0,100], publish:

𝐿
𝑖
=
∑
𝑗
∈
𝑂
𝑖
𝑤
𝑗
𝑧
𝑖
𝑗
,
𝑈
𝑖
=
𝐿
𝑖
+
100
∑
𝑗
∉
𝑂
𝑖
𝑤
𝑗
L
i
	​

=
j∈O
i
	​

∑
	​

w
j
	​

z
ij
	​

,U
i
	​

=L
i
	​

+100
j∈
/
O
i
	​

∑
	​

w
j
	​


These are identification bounds, not imputed scores: missing cells remain missing. Only claim a robust ordering where the relevant bounds separate. Shared-panel comparisons can supplement these bounds but should not be stitched into a supposedly common global score.

6. Quantify robustness without manufacturing precision

Bootstrap tasks when public per-task outcomes exist; cluster repeated attempts by task rather than treating all attempts as independent.

Use published intervals when available.

Treat rounded values as rounding ranges, not exact measurements.

Show plan measurement ranges, account differences and age separately from benchmark sampling uncertainty.

Publish leave-one-benchmark-out and leave-one-source-out rankings.

Show sensitivity to cost weight, workload demand and eligible multiple ranges.

If probabilities lack a defensible statistical basis, publish scenario rank ranges instead of “probability of being best.”

If retaining the weighted preference score, use frozen cost anchors:

𝑆
𝐶
(
𝑐
)
=
100
 
c
l
i
p
(
ln
⁡
𝑐
𝐻
−
ln
⁡
𝑐
ln
⁡
𝑐
𝐻
−
ln
⁡
𝑐
𝐿
,
0
,
1
)
S
C
	​

(c)=100clip(
lnc
H
	​

−lnc
L
	​

lnc
H
	​

−lnc
	​

,0,1)

Use the same anchors across API and Plan views for the same cost unit. Show actual dollars prominently; clipped scores must not conceal differences beyond the anchors.

3. Questions for the owner

Is the target buyer a human using native coding subscriptions, a developer running a third-party agent, or an automated API workload? This determines which subscription routes can support the objective.

Should the headline identify the cheapest option above a quality threshold, or the winner of a preference-weighted score? These are different optimisation objectives.

Which monthly demand levels and usage schedules should the default Plan scenarios represent?

What rule currently selects each family’s effort and fallback configuration, and must it remain identical between API and Plan views?

Does Bug Hunt publish exact configurations, task definitions, verifiers and per-task outcomes? Its defensible headline weight depends on auditability.

Which exact AA cost field produced the stated USD/point range, and is that the field underlying the archived rendered frontier?

4. Verdict

VERDICT: HAS FEEDBACK