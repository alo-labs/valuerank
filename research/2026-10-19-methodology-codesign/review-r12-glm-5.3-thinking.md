1. Findings by severity
Critical

None.

High

Subset-cost scoring has no executable normalization rule. Issue: O17 requires a row with missing basket costs to be compared with other rows on its identical subset. However, the governing cost formula uses frozen anchors in total-workload USD. The draft does not specify how those anchors change for a subset, which reference configurations must have that subset evidenced, or how subset scores remain comparable with full-basket scores in the primary ranking.
paste.txt
 Why it hurts the objective: Applying full-basket anchors to a smaller basket rewards missing costs. Re-estimating anchors from the current subset cohort instead makes the score cohort-relative, conflicting with the frozen-anchor policy. Independently calibrated subset scores can also encode different cost–quality exchange rates despite appearing in one ordered table. Recommended change: Preserve O17, but define a versioned subset workload 
𝑊
𝑆
W
S
	​

, a corresponding frozen-reference anchor pair, and a calibration bridge to the full workload. Publish the actual exchange rate and calibration status for every subset row. Where no public-data bridge is identifiable, keep the required score and ranking position but explicitly label the position “cross-workload ordering not identified.” What is new: This does not reopen the decision to score subset rows. It identifies the missing normalization and cross-workload comparability contract created by that decision.

The 5% unidentified-input gate can permit unsupported pairwise certificates. Issue: Pairwise certification blocks an unbounded unidentified input only when its nominal weight is at least 5%. Yet the science leaves individually weigh 1.25%, and pairwise renormalization increases their retained contribution. The draft does not say how smaller unidentified inputs enter the minimization when they lack an admissible bound. This concerns retained, observed leaves with unidentified uncertainty—not missing leaves already dropped from common support.
paste.txt
 Why it hurts the objective: Several individually small unidentified inputs can collectively exceed the claimed winning margin. A certificate cannot establish a positive worst-case margin if consequential uncertainty is omitted solely because each input falls below a leaf-weight threshold. Recommended change: Make certificate validity margin-based rather than threshold-based. Every retained input must either have an admissible constraint or receive the worst-case effect allowed by its documented score domain. If no defensible domain or constraint exists, the comparison is unidentified. The 5% rule may remain an additional disclosure trigger, but not permission to omit smaller uncertainty. What is new: Earlier decisions introduced input roles and the 5% gate. This finding identifies the aggregate-small-input loophole and its amplification by E8’s pairwise renormalization.

“Undefeated” is not sufficient for a positive-margin certificate. Issue: The directed-matrix definition calls an “undefeated candidate” certified against each listed competitor. In a partially identified graph, however, having no incoming certified-loss edges does not imply having outgoing certified-win edges against everyone. Two mutually unevaluable candidates can both be undefeated without either being certified superior. The later all-competitor positive-margin definition is stronger, but the normative section contains both formulations.
paste.txt
 Why it hurts the objective: An implementation based on graph indegree could issue recommendations because comparisons are missing, not because superiority is established. Recommended change: Define certification explicitly as an outgoing-edge requirement:

Certified
⁡
(
𝑖
;
𝐽
)
  
⟺
  
⋀
𝑗
∈
𝐽
∖
{
𝑖
}
[
gates
⁡
𝑖
𝑗
∧
inf
⁡
𝜃
∈
Θ
𝑖
𝑗
Δ
𝑖
𝑗
(
𝜃
)
>
0
]
.
Certified(i;J)⟺
j∈J∖{i}
⋀
	​

[gates
ij
	​

∧
θ∈Θ
ij
	​

inf
	​

Δ
ij
	​

(θ)>0].

Report “undefeated” separately as a graph diagnostic. Distinguish certified win, certified loss, evaluated but unresolved, and unevaluable comparisons. What is new: This accepts pair-specific common support, possible cycles, and scoped exclusions. It addresses the distinction between absence of a loss and evidence of a win.

Scenario-supported leadership lacks a joint event definition. Issue: “Leads in ≥90% of S0 scenarios” is not fully defined once every pair can use different common-support leaves. There may be no scalar quality score whose ranking reproduces those pairwise comparisons. Moreover, beating each competitor in 90% of scenarios separately does not establish beating all competitors simultaneously in 90% of scenarios.
paste.txt
 Why it hurts the objective: Implementations could report materially different scenario-supported leaders from identical draws. Marginal pairwise frequencies can overstate the frequency of actually leading the comparison set. Recommended change: Define the leadership event in each shared scenario:

𝐿
𝑖
(
𝑠
)
=
1
 ⁣
{
Δ
𝑖
𝑗
(
𝑠
)
>
0
 for every 
𝑗
∈
𝐽
∖
{
𝑖
}
}
.
L
i
(s)
	​

=1{Δ
ij
(s)
	​

>0 for every j∈J∖{i}}.

Scenario-supported leadership requires 
1
𝑁
∑
𝑠
𝐿
𝑖
(
𝑠
)
≥
0.90
N
1
	​

∑
s
	​

L
i
(s)
	​

≥0.90. Undefined comparisons must make that event unevaluable for the stated scope, not count as wins. Publish pairwise frequencies separately. What is new: This does not challenge the adopted 90% threshold or common-support estimand. It supplies the missing simultaneous event to which the threshold applies.

Medium

“Maximum rank change” is not identified for some required S2 branches. Issue: The draft requires S2 maximum rank change, permits cyclic pairwise comparisons, and permits source-removal branches that fail coverage. It does not specify whether S2 ranks come from observed-only scores, full-composite scores, or a graph-ranking procedure. Those are different estimands; a common-support tournament need not possess a consistent scalar ordering.
paste.txt
 Why it hurts the objective: A robustness column can appear to describe stability of the certified recommendation while actually describing a different ranking—or omit the branches that most challenge the recommendation without making that limitation visible. Recommended change: Restrict numerical rank-change statistics to an explicitly named scalar-score estimand, within separately evaluable branches. For pairwise recommendation robustness, report changes in win edges, unresolved comparisons, and whether the candidate still beats the entire declared comparison set. Never assign an ordinary rank to an unevaluable branch. What is new: The ledger already separates specification robustness from certification. The remaining issue is defining the robustness output after adopting pair-specific estimands.

The scenario strata do not uniquely locate Plan-multiple uncertainty. Issue: The draft places “unmeasured Plan quantities (multiple ranges)” in identification/S1, while also describing multiple draws in the overall engine and defining S0 as measurement plus cost draws. A directly measured multiple can have measurement uncertainty; a transported 
𝑀
𝑊
M
W
	​

 can additionally have identification uncertainty. Those components are not interchangeable.
paste.txt
 Why it hurts the objective: S0 support could be overstated by holding a noisy measured multiple fixed, or understated by including transport assumptions in a layer described as measurement-only. The current wording allows both interpretations. Recommended change: Store a measured-multiple uncertainty object separately from its workload-transport object. Include receipt, meter and repeat-measurement uncertainty in S0; add transport and assumption bounds in S1. Where the components cannot be separated from public evidence, declare that limitation and avoid presenting the result as a clean measurement-only comparison. What is new: This retains the adopted measurement/identification/specification hierarchy and 
𝑀
𝑊
M
W
	​

 requirement. It specifies how measured and transported uncertainty map into that hierarchy.

Low

None.

2. Methodology design recommendations
Priority 1 — Make recommendation labels executable predicates

Publish one machine-readable result per ordered pair containing:

Comparison-set identifier and certificate scope.

Common-support leaves and retained weight.

Gate results, with failed or unidentified gates distinguished.

Admissible-set definition and minimum margin.

Four-state comparison outcome: certified win, certified loss, unresolved, unevaluable.

S0 pairwise win frequency.

Derive the recommendation label only from positive outgoing certificates against every competitor in the declared set. Derive scenario-supported leadership from the simultaneous event above, using the same scenario identifier across all comparisons. These changes complete the adopted matrix design rather than introduce a replacement ranking system.
paste.txt

Add two regression tests:

Two rows with an unevaluable comparison produce no certificate against each other, even when neither has a certified loss.

A candidate that wins against different rivals in different scenarios does not receive a simultaneous-lead frequency computed from its marginal pairwise frequencies.

Priority 2 — Close the small-input uncertainty loophole

For retained input 
𝑘
k, define its complete contribution to the pairwise value difference as 
𝑔
𝑖
𝑗
𝑘
g
ijk
	​

. Certification requires either:

A documented joint admissible constraint for that contribution; or

A conservative contribution bound derived from the input’s documented domain.

Then evaluate:

𝑚
𝑖
𝑗
=
inf
⁡
𝜃
∈
Θ
𝑖
𝑗
[
0.25
 
Δ
𝑆
𝐶
(
𝜃
)
+
0.75
∑
𝑏
∈
𝐵
𝑖
𝑗
𝑤
𝑏
𝑝
𝑖
𝑗
Δ
𝑧
𝑏
(
𝜃
)
]
.
m
ij
	​

=
θ∈Θ
ij
	​

inf
	​

	​

0.25ΔS
C
	​

(θ)+0.75
b∈B
ij
	​

∑
	​

p
ij
	​

w
b
	​

	​

Δz
b
	​

(θ)
	​

.

No retained contribution disappears because its nominal weight is small. A bounded score domain can support a conservative certificate calculation without imputing a missing score or inventing repeatability evidence.

For genuinely unknown repeatability, document that the domain bound is conservative and potentially uninformative. That is preferable to treating missing uncertainty as zero, which the draft already prohibits.
paste.txt

Priority 3 — Implement a public-data subset calibration contract

For each actually used subset 
𝑆
S:

Hash its components and task multiplicities as 
𝑊
𝑆
W
S
	​

.

Compute subset costs for the frozen reference configurations with complete public evidence on 
𝑆
S.

Apply the same predeclared percentile convention to obtain frozen 
𝑐
𝐿
,
𝑆
c
L,S
	​

 and 
𝑐
𝐻
,
𝑆
c
H,S
	​

.

Publish paired full/subset costs, resulting scores, exchange rates and rank differences wherever both are evidenced.

Preserve the subset-comparability limitation in the table, not merely in the downloaded registry.

This does not prove that different workloads are equivalent. It makes their calibration inspectable while retaining O17’s subset scoring. Do not fill missing component costs to construct the bridge.
paste.txt

The source adapter should also distinguish total run cost from weighted cost per task by field identity and accounting metadata. AA publicly describes both a total evaluation-run cost excluding repeats and a weighted per-task metric, so field names cannot safely be treated as interchangeable. This supports the existing source contract; it is not a reason to overturn the owner’s captured total-cost evidence.
artificialanalysis
+1

Priority 4 — Split Plan evidence into measurement and transport objects

Use two linked records:

𝑀
o
b
s
e
r
v
e
d
=
ℎ
(
𝐷
r
e
c
e
i
p
t
s
,
𝑃
,
𝐹
)
,
𝑀
𝑊
=
𝑇
(
𝑀
o
b
s
e
r
v
e
d
,
𝑊
,
capacity evidence
)
.
M
observed
	​

=h(D
receipts
	​

,P,F),M
W
	​

=T(M
observed
	​

,W,capacity evidence).

The first record contains observed consumption, gross cash, valuation prices and measurement uncertainty. The second contains the workload hash, quota schema, transport mechanism and identification constraints.

For an identified Plan route:

S0 varies measured quantities under the declared measurement law while holding the nominal transport specification fixed.

S1 additionally varies admissible transport and other identification quantities.

Certification uses the conservative joint admissible set, not the scenario distribution.

For a route whose transport is unidentified, preserve the owner-required displayed score and flag, but do not describe its observed-workload S0 result as target-workload support. This follows the draft’s existing distinction between 
𝑀
o
b
s
e
r
v
e
d
M
observed
	​

 and 
𝑀
𝑊
M
W
	​

.
paste.txt

Priority 5 — Give robustness outputs explicit estimand names

Publish separate columns for:

Displayed-score rank sensitivity.

Full-composite scenario-rank sensitivity.

Pairwise recommendation robustness.

Branch evaluability and exclusion reasons.

For source-removal branches, show the retained quality weight and gates before any rank statistic. Keep the adopted “leave-AA-out not identifiable” result where the coverage rule fails rather than constructing an alternative ranking.
paste.txt

Do not change the GDPval transformation solely to resolve these implementation gaps. AA documents GDPval-AA as a pairwise-comparison rating, with its rating scale anchored to a named model; the linear and logistic mappings therefore remain distinct scoring specifications, as the draft already recognizes.
artificialanalysis
+1

Priority 6 — Consolidate the governing specification before implementation

Generate the prose formulas and release checks from a single schema or executable specification. In particular, remove or replace:

“Undefeated” as a synonym for certified.

Unqualified references to S2 “rank.”

Ambiguous placement of multiple ranges across S0/S1.

The description of Omniscience non-hallucination as conditioned on non-abstentions.

The last item is a wording correction, not a new formula recommendation: AA defines hallucination as incorrect divided by all non-correct responses, including partial and not-attempted responses. The draft’s count-level normative formula already matches that definition.
paste.txt
artificialanalysis

3. Questions for the owner

For O17, is a subset row’s position intended to support a substantive comparison against full-basket rows, or is it a required display position whose cross-workload ordering may explicitly remain unidentified? This determines whether a calibration bridge is sufficient or the shared ordering itself requires an owner-decision challenge.

Must “S2 maximum rank change” describe the displayed scalar ranking, or the robustness of the pairwise recommendation? These require different outputs when common-support comparisons cycle or become unevaluable.

4. Verdict

VERDICT: HAS FEEDBACK