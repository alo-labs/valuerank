1. Findings by severity
Critical

None.

High

The Omniscience quality formula can penalize replacing an abstention with a correct answer. Issue: The draft correctly reproduces AA’s conditional hallucination-rate denominator, but the resulting composite 
𝑧
=
(
2
𝐴
+
𝑁
)
/
3
z=(2A+N)/3 is not monotone in answer quality. AA defines hallucination rate as incorrect divided by all non-correct responses, so this is a property of the composite—not an extraction error.
paste.txt
artificialanalysis
 Consider two hypothetical records on the same 100 questions:
Record	Correct	Incorrect	Not attempted	Accuracy 
𝐴
A	Non-hallucination 
𝑁
N	Reliability score 
𝑧
z
Before	98	1	1	98	50	82
After one abstention becomes correct	99	1	0	99	0	66
Why it hurts the objective: A configuration that answers one additional question correctly, with no additional incorrect answer, loses 16 reliability points. With the specified 10% quality weight and 75% quality contribution to value, it loses 1.2 headline value points, holding everything else fixed. That violates a basic interpretation of “value delivered.” Concrete change: Keep the conditional hallucination rate as a diagnostic, but migrate the scored reliability leaf to a monotone function of the published outcome counts. A straightforward candidate is the normalized AA-Omniscience Index, subject to confirming its treatment of partial answers in the pinned source implementation. AA describes that index as rewarding correct answers, penalizing incorrect answers and treating abstention neutrally.
artificialanalysis
 New argument relative to the ledger: This is not a repetition of the rejected claim that AA’s hallucination denominator should be reconstructed over all questions. AA’s denominator is correctly implemented. The new issue is that combining that conditional rate with accuracy creates a demonstrable dominance reversal. Correct source replication does not establish that the composite is suitable for ValueRank.

Medium

S0 mixes measurement uncertainty with a change of pricing specification. Issue: The scenario section explicitly places “first-party list vs cross-provider median” price-basis draws inside the cost simulation feeding S0. Elsewhere, the registry treats the price rule as a versioned methodological choice, and S0 is named “measurement.”
paste.txt
 Why it hurts the objective: A user reading S0 cannot distinguish uncertainty in the measured cost under the chosen rule from sensitivity to choosing a different purchasing or valuation rule. This is particularly consequential when the same price primitives also value Plan consumption. Concrete change: Fix the primary price rule in S0 and S1. Put first-party-versus-median comparisons in named S2 specification branches, retaining shared price primitives and all demand–cost identities within each branch. Actual uncertainty in an observed price can remain in S0 when its evidence and interpretation support that treatment. New argument relative to the ledger: E34 already makes this separation for cache-policy variation; E83 already preserves primitive identities. Neither resolves the explicit placement of alternative price rules in S0. The change is a layer-classification correction, not another request for price sensitivity.

The registered kernel alternatives do not test mixed kernel assignments. Issue: E112 requires the scenario-supported label to pass every registered specification, but the current description identifies a primary uniform specification and an endpoint-heavy alternative without explicitly requiring mixed assignments across separately uncertain inputs. A natural implementation would therefore test “all uniform” and “all arcsine” only.
paste.txt
 Why it hurts the objective: Candidate quality, reference quality and competitor qualification can enter the qualifying-and-cheapest event in opposing directions. Changing their kernels together can offset effects that appear when only one uncertainty block changes. Passing the two global specifications does not establish robustness to those mixed assignments. Concrete change: Define kernel assignments over independent dependency blocks, not individual duplicated fields. For each label event, evaluate the mixed uniform/arcsine assignments for its relevant blocks when tractable. Otherwise publish the tested assignment set and label the result “supported under the registered kernel checks,” without implying broader distributional robustness. Keep shared primitives shared. New argument relative to E112/E119: The concern is not the choice of arcsine or its parameters. It is the untested combination space between the two adopted marginal kernel families.

Low

None.

2. Methodology design recommendations
Priority 1 — Add outcome-monotonicity tests before changing the reliability leaf

Add executable acceptance tests for every outcome-based quality transform:

Replacing an incorrect answer with a correct answer cannot reduce quality.

Replacing an abstention with a correct answer cannot reduce quality.

Replacing an incorrect answer with an abstention cannot reduce quality when abstention is intended to be preferable to hallucination.

Boundary cases—including zero non-correct responses—must satisfy the same rules.

For a candidate replacement, let 
𝐼
O
m
n
i
I
Omni
	​

 be AA’s published Omniscience Index on its documented 
[
−
100
,
100
]
[−100,100] scale. A transparent normalization is

𝑧
O
m
n
i
=
𝐼
O
m
n
i
+
100
2
.
z
Omni
	​

=
2
I
Omni
	​

+100
	​

.

AA publishes this index separately from accuracy and the conditional hallucination rate. Its documented purpose is to reward factual recall while penalizing incorrect guessing relative to abstention. Confirm the pinned scoring implementation, especially partial-answer treatment, before adopting the transform.
artificialanalysis
+1

Keep the reliability group at 10%; publish the existing transform versus the replacement on the same evidenced panel, with score and rank bridges. This changes neither the cohort nor the exact-variant evidence policy.

One limitation should be explicit: under this normalization, all-abstention performance maps to 50, not zero. That is a consequence of the chosen utility interpretation, not a data error. If that interpretation is unacceptable, use an explicitly owner-approved monotone utility over the published outcome counts instead.

Priority 2 — Make scenario-layer membership executable

Add a registry field such as uncertainty_layer, validated against the primitive’s role:

Primitive or change	Governing treatment
Reporting precision or supported measurement variation under the primary rule	S0
Missing evidence or structurally identified transport uncertainty	S1
Alternative price rule, cache policy, quality mapping or preference weights	S2
No supported sampling mechanism and no accepted convention	Bounds-only

The draft already contains most of the necessary metadata. The additional requirement is a build-time check that prevents a methodological alternative from silently entering a measurement-labelled stratum.
paste.txt

For Plan branches, continue deriving all quantities from the branch’s common primitives:

𝐶
𝑖
,
𝑊
=
𝑝
⊤
𝑑
𝑖
,
𝑊
,
𝑀
𝑖
,
𝑊
=
𝑈
𝑖
(
𝑝
,
𝑑
,
quota
,
funding
)
𝐹
𝑖
.
C
i,W
	​

=p
⊤
d
i,W
	​

,M
i,W
	​

=
F
i
	​

U
i
	​

(p,d,quota,funding)
	​

.

Where compatible transport establishes 
𝑈
𝑖
=
𝜆
𝑖
𝐶
𝑖
,
𝑊
U
i
	​

=λ
i
	​

C
i,W
	​

, derive—not separately sample—

𝐶
𝑖
,
𝑊
P
l
a
n
=
𝐶
𝑖
,
𝑊
𝑀
𝑖
,
𝑊
=
𝐹
𝑖
𝜆
𝑖
.
C
i,W
Plan
	​

=
M
i,W
	​

C
i,W
	​

	​

=
λ
i
	​

F
i
	​

	​

.

This preserves E83/E84 while making the interpretation of each stratum cleaner.

Priority 3 — Specify the kernel-assignment object

Extend the kernel registry with:

kernel_block_id: the primitive or jointly sampled dependency block.

admissible_kernel_families: the registered alternatives for that block.

assignment_id: the selected family for every relevant block.

assignment_coverage: exhaustive / selected stress assignments.

event_relevant_blocks: blocks that can affect the particular label event.

For 
𝐵
B independently assignable blocks with two registered families, the exhaustive assignment set has 
2
𝐵
2
B
 members. Reduce this only through documented irrelevance, equivalence or a valid worst-case argument—not because the global alternatives happen to pass.

Use the existing sequential threshold procedure for each tested event–assignment pair. If computation prevents exhaustive coverage, disclose that limitation rather than treating an incomplete assignment search as a failure of evidence. This recommendation uses the draft’s existing intervals and dependency records; it requires no additional private data.
paste.txt

3. Questions for the owner

Must the scored reliability leaf retain AA’s exact 2:1 accuracy/conditional-non-hallucination transform, or may it migrate to a monotone utility while retaining the 10% group weight? The ledger fixes the group allocation and source substitution, but does not clearly make that transform immutable.

Does “kernel-robust” mean passing the explicitly registered global specifications only, or robustness across mixed assignments of the registered kernel families? The former needs narrower wording; the latter needs an expanded executable assignment contract.

4. Verdict

The draft’s evidence, identification and claim-scope protections are extensive. The remaining material issues concern the meaning of the scored quality function and the interpretation of scenario robustness—not a need to reopen the fixed cohort, exact-variant evidence or Value Multiple numerator policies. The monotonicity failure is the highest-priority correction because it can directly reverse an otherwise unambiguous improvement in delivered quality.

VERDICT: HAS FEEDBACK