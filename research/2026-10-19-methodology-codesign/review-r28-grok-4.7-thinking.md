1. Findings by severity
Critical

None.

High

The provisional-row exclusion is not enforced consistently across unique-cheapest outputs. Issue: The missing-data section excludes provisional rows from “unique cheapest” bar results. The normative confirmed-cheapest definition implements this restriction, but the scenario-supported-cheapest definition does not. Consequently, a provisional singleton that qualifies in every scenario satisfies the scenario-supported-cheapest definition with frequency 100%, although it cannot receive the confirmed-cheapest label. The existing provisional-singleton fixture checks only confirmed cheapest.
paste.txt
 Why it hurts the objective: A scenario-supported-cheapest label could become a second path to a unique-winner claim for a configuration whose quality evidence fails the draft’s minimum coverage requirements. This is a cross-definition inconsistency, not a request to remove provisional rows from the ranking. Concrete change: Require not provisional(i) for both confirmed-cheapest and scenario-supported-cheapest labels. Continue publishing provisional rows’ qualifying-and-cheapest scenario frequencies and possible-cheapest membership, but without a unique-cheapest label. Add a provisional-singleton fixture for the scenario-supported output.

Medium

The route comparator is not a total ordering for unidentified routes. Issue: E85 explicitly allows unidentified routes into the comparator, but its third comparison key defines only a point value or the lower bound of a set-identified interval. It supplies no comparison value for an unidentified route. This matters immediately: the ledger says no Plan route currently has an identified target-workload multiple. Two unidentified routes with equal evidence grades therefore reach an undefined comparison key.
paste.txt
 Why it hurts the objective: Independent implementations could select different official routes—one comparing observed multiples, another skipping the key, another treating missing values as zero. Because the selected route determines the displayed Plan cost and remains frozen inside scenarios, this ambiguity can change the headline ranking. Concrete change: Define an explicit identification-class-specific comparison key. For unidentified routes, either skip the multiple comparison and proceed to gross cash and route ID, or explicitly compare their displayed observed multiples under a declared comparability condition. Publish regression fixtures covering unidentified-versus-unidentified routes, including different original valuation bases. New relative to E85/E88: This finding does not challenge evidence priority or the dominance pre-filter. It identifies an undefined branch in the adopted comparator.

The workload-demand contract mixes per-task and per-pass units. Issue: E44 describes 
𝑥
𝑖
𝑊
x
iW
	​

 as category tokens “per deployment-equivalent task,” while E84 requires 
𝑝
r
e
l
e
a
s
e
⋅
𝑥
𝑖
𝑊
=
𝐶
𝑖
,
𝑒
p
release
	​

⋅x
iW
	​

=C
i,e
	​

, a component-indexed cost. Elsewhere, the capacity formula treats its demand vector as tokens per unit of the complete workload, and E84’s Coding Agent Index example uses 303 times pooled category-token means. These are different aggregation levels unless an explicit conversion is supplied.
paste.txt
 Why it hurts the objective: A transport implementation could reconcile a per-task vector against a per-component total or use component demand as complete-workload demand. The resulting capacity could be wrong by a task multiplicity while still passing an incompletely specified unit check. Concrete change: Define separate per-task, component-pass and workload-pass demand objects, with explicit aggregation identities. Require the capacity solver to accept only the workload-pass object. New relative to E44/E84: This is not a request to add demand evidence or reconciliation; both are already adopted. It resolves the dimensional inconsistency within those contracts.

Low

None.

2. Methodology design recommendations
Priority 1 — Make cheapest-label eligibility one executable predicate

Define:

UniqueLabelEligible
⁡
(
𝑖
)
=
BarCompetitorEligible
⁡
(
𝑖
)
∧
¬
Provisional
⁡
(
𝑖
)
.
UniqueLabelEligible(i)=BarCompetitorEligible(i)∧¬Provisional(i).

Use this predicate in both unique-cheapest label functions. Keep it separate from possible-cheapest membership and descriptive scenario frequencies.

Add these fixtures:

Fixture	Required result
Non-provisional singleton, always qualifying	May receive either unique-cheapest label when its respective conditions hold
Provisional singleton, always qualifying	No unique-cheapest label; descriptive event frequency may be 100%
Provisional competitor is cheaper than a non-provisional candidate	Competitor still prevents the candidate’s unique-cheapest claim when it qualifies
Two equal-cost qualifiers	Neither receives a unique-cheapest label

The third fixture is important: withholding a label from a provisional row must not remove that row as a competitor. That preserves the draft’s existing distinction between being ranked, competing, and being eligible for a unique label.
paste.txt

Priority 2 — Complete the route comparator without implying unidentified transport is known

My preferred completion is to skip the multiple key for unidentified routes:

𝐾
(
𝑟
)
=
{
(
class
,
grade
,
𝑀
𝑊
,
−
𝐹
g
r
o
s
s
,
ID
)
,
	
point-identified
,


(
class
,
grade
,
𝐿
𝑊
,
−
𝐹
g
r
o
s
s
,
ID
)
,
	
set-identified
,


(
class
,
grade
,
constant
,
−
𝐹
g
r
o
s
s
,
ID
)
,
	
unidentified
.
K(r)=
⎩
⎨
⎧
	​

(class,grade,M
W
	​

,−F
gross
	​

,ID),
(class,grade,L
W
	​

,−F
gross
	​

,ID),
(class,grade,constant,−F
gross
	​

,ID),
	​

point-identified,
set-identified,
unidentified.
	​


Here, higher class, grade and multiple are preferred; lower cash and the declared stable ID ordering break ties. The constant means that unidentified routes do not acquire an invented target-workload comparison multiple.

Publish an additional selection-reason field, for example:

Unidentified routes tied on evidence grade; selected by lower measured-period gross cash.

Continue using the selected route’s observed multiple for the owner-required displayed score. This preserves O16 while making route selection executable and avoiding a hidden claim that different observed-workload multiples identify target-workload ordering. The draft already distinguishes these two multiples, so the change requires no new public data.
paste.txt

Priority 3 — Make transport aggregation dimensionally explicit

Use the following objects:

𝑡
𝑖
𝑒
t
ie
	​

: category-token vector per deployment-equivalent task of component 
𝑒
e, under its documented aggregation and telemetry-support convention.

𝑛
𝑒
n
e
	​

: frozen task multiplicity.

𝑑
𝑖
𝑒
=
𝑛
𝑒
𝑡
𝑖
𝑒
d
ie
	​

=n
e
	​

t
ie
	​

: category-token vector per component pass.

𝑑
𝑖
𝑊
=
∑
𝑒
∈
𝑊
𝑑
𝑖
𝑒
d
iW
	​

=∑
e∈W
	​

d
ie
	​

: category-token vector per complete workload pass.

Then require:

𝑝
r
e
l
e
a
s
e
⊤
𝑑
𝑖
𝑒
=
𝐶
𝑖
𝑒
,
𝑝
r
e
l
e
a
s
e
⊤
𝑑
𝑖
𝑊
=
𝐶
𝑖
𝑊
.
p
release
⊤
	​

d
ie
	​

=C
ie
	​

,p
release
⊤
	​

d
iW
	​

=C
iW
	​

.

Where the published aggregation is not representable by an ordinary per-task mean, store a directly evidenced component-pass vector and its aggregation operator instead of forcing the first identity.

For additive capacity, use:

𝜆
𝑤
=
𝐵
𝑤
𝑎
𝑤
⊤
𝑑
𝑖
𝑊
,
𝑀
𝑊
=
𝜆
 
𝐶
𝑖
𝑊
𝐹
g
r
o
s
s
,
λ
w
	​

=
a
w
⊤
	​

d
iW
	​

B
w
	​

	​

,M
W
	​

=
F
gross
	​

λC
iW
	​

	​

,

with 
𝜆
λ measured in complete workload-equivalent passes per fee period.

Add machine-checkable units to every vector and scalar. A fixture should reject a per-task vector supplied where a workload-pass vector is required, even when its numerical entries happen to satisfy another constraint. This strengthens the existing reconciliation contract without changing O27’s published-cost convention or admitting unsupported token evidence.
paste.txt

3. Questions for the owner

Should provisional status prohibit the scenario-supported-cheapest label as well as confirmed cheapest? The prose currently implies yes; the normative scenario definition currently permits it. Your answer determines whether to amend the predicate or narrow the prose.
paste.txt

When two admissible routes both have unidentified 
𝑀
𝑊
M
W
	​

 and equal evidence grades, should selection prefer lower gross cash, or a larger observed multiple when those observed multiples have a demonstrably comparable measurement basis? This determines the missing comparator branch.
paste.txt

4. Verdict

The remaining feedback concerns consistency between executable definitions, rather than a need to redesign the objective or revisit settled owner decisions. Resolve the provisional-label rule, complete the unidentified-route comparator, and make demand-vector units explicit before treating r27 as implementation-complete.
paste.txt

VERDICT: HAS FEEDBACK