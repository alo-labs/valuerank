1. Findings by severity
Critical

None.

High

Basket admission is not invariant to the representation of execution components.

Issue: E140 maximises the number of admitted components before panel size. That objective can change when the same execution work is represented as one aggregate or several mutually exclusive accounting children. The accounting tree prevents double counting, but it does not stop the selection algorithm from rewarding a finer decomposition. E55’s split-invariance test currently protects workload costs and the matched-cost diagnostic, not admission.
paste.txt

Why it hurts the objective: Two economically equivalent representations of the public evidence can select different scored workloads—and therefore different rankings—without any change in model performance, cost or evidence coverage.

Concrete change: Define a frozen set of canonical admission units, separate from accounting nodes. Count those units in E140; treat an aggregate and its complete decomposition as alternative representations of the same unit. Publish the admission-unit-to-accounting-node mapping and require representation-invariance fixtures.

What is new relative to the ledger: This does not challenge exhaustive enumeration or advocate a different coverage threshold. It identifies a missing invariance property in the objective being enumerated.

Medium

The standing Terminal-Bench cost-removal sensitivity lacks a complete scoring contract.

Issue: E64 requires a standing rank-change column after removing the AA Index-run Terminal-Bench cost. However, E146’s explicit deletion formula governs quality-leaf removal and keeps the primary cost score unchanged. Elsewhere, removing a cost component constitutes a workload migration with its own workload hash, anchor object and Plan-transport revalidation. These provisions do not uniquely specify how to calculate the standing cost-removal column.
paste.txt

Why it hurts the objective: An implementation can obtain different rank changes depending on whether it holds anchors fixed or recalibrates them. On the Plan basis, retaining the old multiple after changing the workload adds a further transport assumption. A supposedly routine robustness column therefore has no single reproducible interpretation.

Concrete change: Register the cost-removal diagnostic separately from quality deletion. Specify the altered workload, anchor treatment, route treatment, Plan-multiple treatment and common comparison panel. Distinguish a fixed-anchor cost-contribution stress from a recalibrated alternative-workload ranking.

What is new relative to the ledger: E146 resolves quality deletion, and E64 already requires the Terminal-Bench column. The remaining issue is the executable definition of that cost-deletion column, not whether to publish it.

Low

None.

2. Methodology design recommendations
Priority 1 — Make admission invariant to accounting decomposition

Retain the current coverage threshold, exhaustive search and lexicographic priorities, but apply them to canonical admission units rather than whichever accounting nodes happen to be present.

Let:

𝑈
U be the versioned set of canonical admission units;

𝐿
(
𝑢
)
L(u) be the required accounting leaves for unit 
𝑢
u;

𝐾
𝑖
𝑢
=
1
K
iu
	​

=1 when configuration 
𝑖
i has complete evidence for the whole unit, either through an accepted aggregate or a complete compatible decomposition.

Then define:

𝑃
(
𝑆
)
=
{
𝑖
:
𝐾
𝑖
𝑢
=
1
 for every 
𝑢
∈
𝑆
}
,
𝑆
⊆
𝑈
.
P(S)={i:K
iu
	​

=1 for every u∈S},S⊆U.

Select 
𝑆
S using the existing priorities:

max
⁡
lex
(
∣
𝑆
∣
,
∣
𝑃
(
𝑆
)
∣
,
published canonical-order preference
)
,
∣
𝑃
(
𝑆
)
∣
≥
⌈
2
𝑁
/
3
⌉
.
lex
max
	​

(∣S∣,∣P(S)∣,published canonical-order preference),∣P(S)∣≥⌈2N/3⌉.

This preserves E140’s intended design while preventing accounting granularity from becoming an implicit workload preference. The required inputs already belong in the public evidence registry and accounting tree; no imputation or additional private measurements are necessary.
paste.txt

Add this regression fixture:

𝑁
=
6
N=6.

Unit A has complete evidence on rows 
{
1
,
2
,
3
,
4
}
{1,2,3,4}.

Units B and C each have complete evidence on rows 
{
3
,
4
,
5
,
6
}
{3,4,5,6}.

A cannot be jointly admitted with B or C because their joint panel has only two rows.

The current component-count objective selects B+C.

If A is merely represented as three accounting children with identical coverage, a node-count implementation instead selects those three children.

The corrected implementation must select B+C in both representations and publish identical workload costs and admission results.

If the intention is that only the ten named top-level targets can ever count, state that as a normative rule and validate it in the build. That is sufficient; no more elaborate optimisation is needed.

Priority 2 — Give cost-deletion sensitivity its own branch object

Define a versioned cost-deletion object containing:

𝐷
cost
=
(
𝑅
𝐶
,
 
𝑊
−
𝑅
𝐶
,
 anchor policy
,
 route policy
,
 multiple policy
,
 panel rule
)
,
D
cost
	​

=(R
C
	​

, W
−R
C
	​

, anchor policy, route policy, multiple policy, panel rule),

where 
𝑅
𝐶
R
C
	​

 identifies removed execution components—not quality leaves. E146’s quality-deletion object should remain separate. This extends the draft’s existing use of hashed workload, diagnostic and branch objects rather than introducing another evidence regime.
paste.txt

For the standing Terminal-Bench column, publish two explicitly different calculations:

Fixed-anchor contribution stress.

𝐶
𝑖
−
𝑇
𝐵
=
𝐶
𝑖
,
𝑊
−
𝐶
𝑖
,
𝑇
𝐵
,
C
i
−TB
	​

=C
i,W
	​

−C
i,TB
	​

,
𝑉
𝑖
−
𝑇
𝐵
,
f
i
x
e
d
=
0.25
 
𝑆
𝐶
(
𝐶
𝑖
−
𝑇
𝐵
;
𝐴
𝑊
)
+
0.75
 
𝑄
ˉ
𝑖
,
V
i
−TB,fixed
	​

=0.25S
C
	​

(C
i
−TB
	​

;A
W
	​

)+0.75
Q
ˉ
	​

i
	​

,

where 
𝐴
𝑊
A
W
	​

 is the original anchor object. Hold quality fixed and compare ranks on the common evidenced panel. Label this “cost-component removal, original anchors”—a sensitivity of the original scoring system, not a newly calibrated workload ranking.

Alternative-workload comparison. Construct 
𝑊
−
𝑇
𝐵
W
−TB
, apply the existing anchor-construction rule to its evidenced reference panel, and compare baseline and alternative ranks on the same common panel. Publish the changed exchange rate alongside the rank changes so readers can distinguish cost-composition effects from recalibration effects.

For the Plan basis:

Reuse an identified 
𝑀
𝑊
M
W
	​

 only if its public identification mechanism also covers 
𝑊
−
𝑇
𝐵
W
−TB
, or recompute the multiple through that mechanism.

Where that is not established, a calculation retaining the displayed multiple may still appear as a clearly named fixed-multiple arithmetic stress.

Do not describe that arithmetic stress as identified Plan economics for the altered workload.

These distinctions are especially relevant because the draft reports no identified target-workload Plan multiples today. They preserve O16’s displayed scores without silently upgrading the interpretation of the diagnostic.
paste.txt

3. Questions for the owner

Is E140 intended to count only the ten permanently named top-level target components, regardless of how their accounting decomposition changes? An explicit “yes” would reduce the admission recommendation to a normative clarification and regression test.

Should the standing Terminal-Bench removal column measure sensitivity within the original scoring scale, or the ranking under a newly calibrated workload? Both are implementable, but they answer different questions and require different anchor treatment.

4. Verdict

The remaining feedback concerns reproducibility: admission should not depend on accounting representation, and the required cost-removal sensitivity needs one explicit executable interpretation. Neither change requires relaxing the cohort, exact-variant or Value Multiple evidence policies.

VERDICT: HAS FEEDBACK