0. Read check

Read both listed parts to their ends at commit 8e532e4891e1759c825d0fed89e1ae32fbc9eea1, in order.

Part	First line	Last 12 words
9	## Uncertainty (three separate layers, one scenario engine)	not separable" and its S0 result is not described as target-workload support.
10	- **Specification**: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress.	on the headline's position or a neighbour; from four configurations the three positions are distinct.

Source files: part 9 and part 10.

1. Findings by severity
Critical

None.

High

None.

Medium

The recalibrated cost-deletion branch gives an overbroad anchor-population instruction. Issue: E64/E149 calculation (b) says alternative-workload anchors are rebuilt “from every row with a cost on W∖TB.” E172 applies the same design to every admitted basket unit. Having a cost is a weaker condition than passing the anchor-reference policies already adopted in E184 and, for Plan anchors, O157. The wording therefore creates an executable-specification conflict: a literal implementation can include incomplete-cost, valuation-ineligible or non-measured Plan references when recalibrating the sensitivity’s anchors. Part 10 explicitly frames these definitions as normative, rather than merely illustrative. Source: part 10 Why it hurts the objective: the branch is intended to distinguish cost-composition effects from recalibration effects. Silently changing reference-evidence eligibility adds a third effect and can make a weakly evidenced row determine the apparent exchange rate. Concrete change: replace “every row with a cost” with an explicit call to the existing anchor-eligibility procedure, evaluated on the reduced workload and separately by basis. Publish the resulting reference IDs and exclusions. If recalibration lacks the required references, mark that calculation unavailable while retaining the original-anchor arithmetic stress. What is new relative to the ledger: this does not request a new anchor policy. It identifies a local instruction that bypasses the adopted policy in the standing sensitivity family.

Low

The AI Coding Daily variance explanation states strict overstatement where the stated reasoning establishes only an upper bound. Issue: part 9 says that six trials of the points share “overstate the variance of a mean of six bounded project scores.” Under the section’s independent-task approximation, the bounded-score argument establishes that this variance is no greater than the Bernoulli-envelope calculation; equality is possible. Elsewhere in the same paragraph, the draft correctly calls the analogous treatment an “upper bound.” Source: part 9 Why it hurts the objective: “overstate” can be read as establishing actual conservatism relative to the unknown project-score distribution. The draft has established an envelope under an independence assumption, not measured the amount of conservatism. Concrete change: write “upper-bounds the independent-project variance under the bounded-score model.” Keep the existing wide/narrow sensitivity and proposed replacement with captured per-project scores.

2. Methodology design recommendations

Prioritise one anchor-construction function for primary and sensitivity workloads. For reduced workload 
𝑊
′
=
𝑊
∖
𝑅
𝐶
W
′
=W∖R
C
	​

, construct the reference set as

𝐽
𝑊
′
,
𝑏
=
{
𝑖
:
AnchorEligible
⁡
(
𝑖
,
𝑊
′
,
𝑏
)
}
,
J
W
′
,b
	​

={i:AnchorEligible(i,W
′
,b)},

where 
𝑏
b is API or Plan and AnchorEligible invokes the existing completeness, valuation and basis-specific evidence rules. Then apply the existing padding and anchor formula—not a separate “has a cost” rule. Each sensitivity output should carry:

Reduced-workload ID and removed component.

Reference IDs, evidence-status exclusions and reference count.

Anchor values and resulting exchange rate.

Common comparison panel.

Recalibration status, including an explicit insufficient-reference outcome.

Add a regression fixture in which an inexpensive row has a published cost but fails anchor eligibility: it may participate wherever existing ranking rules allow, but must not set the reduced-workload anchor. This preserves the two-calculation decomposition already specified in E149/E172. Source: part 10

Make the bounded-score variance contract explicit without changing the owner-selected noise design. For independent project scores 
𝑋
𝑗
∈
[
0
,
1
]
X
j
	​

∈[0,1], with 
𝑛
n projects and average mean 
𝑝
p, the envelope underlying the current explanation is

Var
⁡
 ⁣
(
1
𝑛
∑
𝑗
=
1
𝑛
𝑋
𝑗
)
≤
𝑝
(
1
−
𝑝
)
𝑛
.
Var(
n
1
	​

j=1
∑
n
	​

X
j
	​

)≤
n
p(1−p)
	​

.

Describe the implemented Jeffreys-adjusted plug-in calculation separately from this theoretical envelope: it substitutes 
𝑝
~
p
~
	​

 for an unknown mean and remains a conventional approximation. Once the six project scores are captured, implement the already-proposed sample-SD calculation and retain the envelope as a sensitivity, rather than describing the current calculation as demonstrably overstating actual noise. This is a precision improvement to the existing design, not a challenge to O142 or O154. Source: part 9

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK