1. Findings by severity
Critical

None.

High

The clipping gate can reject the initial reference cohort by construction. Issue: Cost anchors are the reference cohort’s 1st and 99th percentiles, but the cost section holds a release when at least two rows clip. With 19 distinct reference costs and interpolated percentiles, the minimum lies below the 1st-percentile anchor and the maximum above the 99th-percentile anchor: two rows necessarily clip. The governance section separately specifies a greater-than-10% clipping gate without defining whether its denominator is per basis or combined.
paste.txt
 Why it hurts the objective: A correctly populated first release can fail its own release gate. Repeated re-anchoring to fix expected tail clipping would also undermine the intended frozen exchange rate. Change: Specify the percentile estimator, clipping denominator and one governing threshold. If retaining interpolated percentile anchors, distinguish expected reference-tail clipping from subsequent anchor saturation. For example, hold when more than 10% of rows clip on either basis, or when a clipped row exceeds a separately specified extrapolation tolerance. Two of 19 rows would still fail that example, so the initial anchor construction must explicitly accommodate the chosen threshold. What is new: This is an initialization contradiction between the adopted anchor construction and release gates—not another request to introduce frozen anchors or clipping checks.

The price-cancellation release test is too broad. Issue: The test says shared price changes cancel when the numerator and AA cost share a price basis. A shared price list alone is insufficient: cancellation also depends on the relationship between the measured consumption mix and the target workload mix. The draft expressly permits those mixes to differ.
paste.txt
 Let target-workload token quantities be 
𝑥
x, measured subscription consumption be 
𝑢
u, prices be 
𝑝
p, and gross fee be 
𝐹
F. Then:

𝐶
P
l
a
n
,
𝑊
=
𝑝
⊤
𝑥
(
𝑝
⊤
𝑢
)
/
𝐹
=
𝐹
𝑝
⊤
𝑥
𝑝
⊤
𝑢
.
C
Plan,W
	​

=
(p
⊤
u)/F
p
⊤
x
	​

=F
p
⊤
u
p
⊤
x
	​

.

A common scalar increase in every price cancels. A relative change in input, output or cache prices generally does not. This distinction matters because AA calculates costs using category-specific token prices and usage.
artificialanalysis
 Why it hurts the objective: An implementation could incorrectly suppress genuine Plan-cost changes, or reject a correct repricing result as a failed release test. Change: Replace the existing test with three tests:

Uniform price scaling cancels.

Arbitrary category-price changes cancel when measured consumption is proportional to the target-workload token vector.

Otherwise, category repricing changes effective Plan cost according to the ratio above, with transport identification rechecked.

What is new: This identifies a missing condition in an adopted executable test, rather than repeating the already adopted requirement to align price lists.

The matched-cost blocker can veto an otherwise robust value recommendation for an economically irrelevant cost reversal. Issue: Any separated reversal between basket-cost ordering and matched-cost ordering blocks certification—even if the candidate remains decisively better in value under both cost definitions.
paste.txt
 For example, suppose candidate A has a 20-point common-support quality advantage. Basket costs are A = $100 and B = $110; matched costs are A = $11 and B = $10. The cost reversal triggers the blocker regardless of whether that approximately 10% cost disadvantage could possibly offset A’s quality advantage under the frozen exchange rate. Why it hurts the objective: The blocker tests agreement between two cost rankings, not whether the workload choice changes the value decision. It can withhold “recommended” precisely when the recommendation is insensitive to that choice. Change: Keep the reversal warning, but make the certification blocker margin-based. Block when the candidate’s value advantage fails under an explicitly defined matched-workload sensitivity—not merely when cost order changes. Give that alternative workload its own frozen calibration; do not insert per-task matched costs directly into total-basket anchors. What is new: E3/E6 and the later blocker already adopt coverage and cost-shape checks. This is a new counterexample showing that the reversal condition can reject a recommendation without demonstrating recommendation sensitivity. It challenges an editor rule, not O15’s scored basket.

Medium

The frontier output lacks governing joint-state definitions. Issue: “Definite” and “possible” frontier membership are promised, but the normative section does not define their quantifiers. In contrast, pairwise recommendations and cheapest-above-bar outputs have executable definitions.
paste.txt
 Why it hurts the objective: With shared prices, quota pools and benchmark uncertainty, marginal rectangles do not determine frontier membership. A candidate may be able to escape each rival separately, yet have no single admissible state in which it escapes all rivals. Change: Define dominance and frontier membership over the declared joint admissible set; see Section 2. Publish “unevaluable” where the target cost lacks an admissible domain, rather than forcing a definite/possible classification. What is new: Bound-aware frontiers were adopted previously. The remaining issue is the missing joint-state executable definition, not the absence of uncertainty bounds.

Current-basket coverage is not a sufficient measure of phasing readiness. Issue: Under common-basket phasing, an evaluation remains pending until exact costs exist for every ranked row. The draft publishes “basket coverage,” but does not specify its denominator or require disclosure of how much scored cost comes from each included evaluation. One difficult-to-price row can therefore delay a major software-engineering component for the entire cohort.
paste.txt
 Why it hurts the objective: A basket can be complete relative to its current version while still pricing little of the software-engineering work that motivates ValueRank. AA’s published Index composition itself spans different task families; completeness of an available subset is not evidence of alignment with ValueRank’s intended workload.
artificialanalysis
 Change: Keep the adopted phasing policy, but publish a readiness table against the full O15 target basket: inclusion status, missing configurations, task multiplicity, cost availability, priced quality weight and per-model share of basket expenditure. Do not summarize these into one unlabeled coverage percentage. What is new: Priced-quality coverage and a certification-feasibility matrix are already adopted. This adds target-basket readiness and expenditure concentration, which those diagnostics do not establish.

A repeatability stress allowance needs an explicit certification interpretation. Issue: For a single-run Bug Hunt result, the draft separates observed evidence from a repeatability stress allowance. Elsewhere, missing repeatability can be an unidentified quantity or a labeled stress allowance, while every retained input must enter certification through an admissible constraint or domain. It remains unclear when an analyst-selected repeatability allowance qualifies as a certificate constraint rather than specification-only stress.
paste.txt
 Why it hurts the objective: Two implementations could certify different leaders from identical public evidence simply by assigning different roles to an arbitrary allowance. Change: Require every such allowance to state whether it is an assumed certification bound or a sensitivity-only parameter. If no defensible repeatability bound exists, use the documented score domain for certification, or mark the comparison unevaluable if the estimand itself is undefined. A narrow analyst stress band must not acquire evidentiary status merely by being registered. What is new: E11 already requires all retained uncertainty to be included. This finding concerns which constraints are admissible evidence, not whether small-weight uncertainty may be omitted.

Low

The document retains conflicting executable-looking formulas after declaring governing replacements. Issue: The draft retains the harmonic multiple, marginal qualification wording and full-composite value certificate alongside their governing replacements. Some are marked superseded, but they still resemble implementation instructions.
paste.txt
 Why it hurts the objective: Independent implementers can produce different outputs while each appears to follow a normative paragraph. Change: Maintain one executable specification per output. Move superseded formulas into a non-normative change log and generate prose formula references from the specification. What is new: Earlier reviewers resolved the substantive formulas. This is a remaining implementation and maintenance problem caused by retaining the superseded forms.

2. Methodology design recommendations
Priority 1 — Make release initialization and tests executable

Define a versioned anchor object containing:

Reference configuration IDs and frozen costs.

Percentile estimator and interpolation convention.

Anchor values, units, workload hash and basis.

Clipping denominator and threshold.

Expected reference-tail clipping.

Maximum permitted distance beyond an anchor.

Add a first-release fixture using the actual reference cohort. It must pass without discretionary re-anchoring. Preserve O12: failure of the corrected governing gate still holds the release.
paste.txt

Replace the broad price-cancellation assertion with the three conditional tests in Finding 2. Include a two-category fixture with different measured and target mixes, so relative-price changes cannot accidentally be treated as invariant.

Priority 2 — Test workload sensitivity against the recommendation margin

Retain the official O15 basket and 25:75 score. For the matched-cost sensitivity, define an alternative workload:

𝐶
𝑖
,
a
l
t
=
∑
𝑏
∈
𝐵
𝑞
𝑏
𝑐
𝑖
𝑏
,
C
i,alt
	​

=
b∈B
∑
	​

q
b
	​

c
ib
	​

,

where 
𝑞
𝑏
q
b
	​

 are frozen, published task quantities derived from the selected priced-leaf weighting convention. Give this workload a separately versioned anchor pair and calculate:

Δ
𝑖
𝑗
,
a
l
t
=
0.25
𝜅
a
l
t
ln
⁡
 ⁣
(
𝐶
𝑗
,
a
l
t
𝐶
𝑖
,
a
l
t
)
+
0.75
(
𝑄
𝑖
(
𝑖
𝑗
)
−
𝑄
𝑗
(
𝑖
𝑗
)
)
.
Δ
ij,alt
	​

=0.25κ
alt
	​

ln(
C
i,alt
	​

C
j,alt
	​

	​

)+0.75(Q
i
(ij)
	​

−Q
j
(ij)
	​

).

Publish two separate results:

Basket certificate under the governing workload.

Matched-workload robustness: positive margin, unresolved, reversed or unevaluable.

If cross-workload robustness remains a condition for “recommended,” require a positive conservative alternative margin. A cost-order reversal alone should remain a warning. This preserves the adopted common-panel and exact-variant requirements while making the blocker answer the actual value question.
paste.txt

Priority 3 — Complete the frontier specification

For a fixed basis, workload, comparison set 
𝐽
J and joint admissible set 
Θ
Θ, define:

𝑗
≻
𝜃
𝑖
  
⟺
  
𝐶
𝑗
(
𝜃
)
≤
𝐶
𝑖
(
𝜃
)
∧
𝑄
𝑗
(
𝜃
)
≥
𝑄
𝑖
(
𝜃
)
,
j≻
θ
	​

i⟺C
j
	​

(θ)≤C
i
	​

(θ)∧Q
j
	​

(θ)≥Q
i
	​

(θ),

with at least one strict inequality.

Then define:

D
e
f
i
n
i
t
e
F
r
o
n
t
i
e
r
(
𝑖
)
  
⟺
  
∀
𝜃
∈
Θ
,
  
∄
𝑗
∈
𝐽
∖
{
𝑖
}
:
𝑗
≻
𝜃
𝑖
,
DefiniteFrontier(i)⟺∀θ∈Θ,∄j∈J∖{i}:j≻
θ
	​

i,
P
o
s
s
i
b
l
e
F
r
o
n
t
i
e
r
(
𝑖
)
  
⟺
  
∃
𝜃
∈
Θ
,
  
∄
𝑗
∈
𝐽
∖
{
𝑖
}
:
𝑗
≻
𝜃
𝑖
.
PossibleFrontier(i)⟺∃θ∈Θ,∄j∈J∖{i}:j≻
θ
	​

i.

Use full-composite quality here, as the draft already requires—not pair-specific common-support quality. Preserve shared dependencies and list comparison-set exclusions. Scenario frontier frequencies are a separate output and do not establish either quantified relation.
paste.txt

Priority 4 — Publish a target-workload readiness and concentration table

For every intended O15 component, publish its status against the target basket, not merely the current scored basket. For every scored model, publish:

𝑠
𝑖
𝑒
=
𝑛
𝑒
𝑐
𝑖
𝑒
𝐶
𝑖
,
𝑊
,
𝐻
𝑖
=
∑
𝑒
𝑠
𝑖
𝑒
 
2
.
s
ie
	​

=
C
i,W
	​

n
e
	​

c
ie
	​

	​

,H
i
	​

=
e
∑
	​

s
ie
2
	​

.

The expenditure shares show which task families actually determine cost; 
𝐻
𝑖
H
i
	​

 summarizes concentration. Neither changes the owner’s weights or workload. Both are routinely refreshable from the component costs and multiplicities already required by the registry.
paste.txt

Avoid a new certification cutoff initially. These diagnostics should first establish whether the common basket meaningfully prices the intended work.

Priority 5 — Separate evidence constraints from assumption-conditioned bounds

Extend each uncertainty object with:

constraint_basis: published interval / public repeated runs / structural bound / analyst assumption / score domain.

certificate_use: evidence-bounded / assumption-conditioned / excluded.

estimand: the quantity actually bounded.

Source, version and rationale.

A certificate using an analyst-assumed repeatability bound should say so in its label. Where available, consume published benchmark intervals rather than replacing them with invented ranges: Terminal-Bench publishes 95% intervals, and AA describes sandwich-estimator intervals for its pairwise-rating evaluations. Those intervals still need their stated interpretation preserved; they are not automatically hard bounds on future deployment performance.
tbench
+1

3. Questions for the owner

Is “recommended” intended to require a stable value decision across the basket and matched workload, or agreement between their cost rankings even when the value decision is unchanged? This determines whether the current reversal veto is intentional.

May a certificate rely on an explicitly labeled analyst-assumed repeatability bound, or should certification constraints be limited to public evidence, structural bounds and full score domains? This determines how sparse single-run leaves enter certification.

4. Verdict

The draft has a strong separation of estimands, evidence layers and certificate scopes. The remaining material problems concern initialization, a false price-invariance test, a blocker that need not track value sensitivity, and several under-specified executable rules—not a need to redesign the adopted cohort or scoring policy.

VERDICT: HAS FEEDBACK