0. Read check

Read all three listed parts to their ends at commit 2ca6c729a3f1a11bd08f5d669f5977875b087381. Review scope is parts 1–3 only; cited rules governing other sections are treated as defined, not missing.

Part 1

First line: # ValueRank methodology — draft r169

Last 12 words: “configurations; applying O145 moved the release cutoff (O65) and re-captured every source.”

Part 2

First line: - **Two rankings (owner decisions O52, O53, O54)**: ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52).

Last 12 words: “configuration missing a leaf after the search is listed, not ranked (O36).”

Part 3

First line: empty.

First non-empty line: ## Cost (25% of the value score)

Last 12 words: “on the Plan basis the workload question is the M_W identification status.”

Source locators below identify the connector-read part and section. The connector returned file contents and blob SHAs, but no citation IDs.

1. Findings by severity
Critical

None.

High

None.

Medium

The claimed bound on unmeasured agent overhead is not a general bound. Issue: Part 3 states: “The Coding Agent Index's share of a ranked row's basket cost bounds how much an unmeasured agent overhead can move it.” The share bounds the reduction in total basket dollars obtained by removing that component’s entire observed cost. It does not, without additional restrictions, bound an upward counterfactual cost change, an agent-normalised cost difference, or movement in value points or ordinal rank. Why it hurts the objective: The draft correctly identifies a cost–quality deployment mismatch: vendor-agent token consumption enters cost, while the corresponding agent’s quality does not enter the quality leaves. Calling its exposure “bounded” without specifying the quantity and direction overstates how far the published evidence contains that mismatch. This matters especially when the affected component contributes 16–74% of basket cost. Concrete change: Replace the sentence with a directional dollar statement. If 
𝐴
𝑖
A
i
	​

 is the observed Coding Agent Index component and 
𝐶
𝑖
C
i
	​

 is total basket cost, define 
𝑠
𝑖
=
𝐴
𝑖
/
𝐶
𝑖
s
i
	​

=A
i
	​

/C
i
	​

. Removing some or all of that component, while leaving every other component unchanged, reduces basket cost by at most 
𝑠
𝑖
s
i
	​

. State explicitly that public evidence supplies no general bound on the upward counterfactual or on rank movement. Translate any specified component adjustment through the actual clipped score function rather than treating its cost share as a value-score bound. What is new relative to the ledger: This does not challenge O123, request a new harness model, or repeat the adopted diagnostic. It identifies a mathematical limitation in the additional “bounds how much” interpretation. Source: part 3, “Cost,” first bullet, “Coding agent”; blob 12f2896bb89ca9d560cf660b45f36a83e0683593.

Low

The subset-output paragraph conflates the subset-origin stratum with the comparison population. Issue: E190 says subset-workload frontier and bar outputs cover “every row with FullCost on 
𝑊
𝑆
W
S
	​

.” Its immediate parenthesis then describes a “1-row API subset stratum” and “4-row Plan subset stratum.” Those counts describe configurations whose primary score uses the subset workload, not necessarily all configurations evaluable on that workload. Main-workload configurations with complete evidence for the six shared components can also be evaluated on 
𝑊
𝑆
W
S
	​

. Why it hurts the objective: A reader can mistake a meaningful same-workload comparison for a singleton comparison. Conversely, an implementation could mistakenly reuse the singleton stratum as the competitor population. The underlying rule is present; the problem is ambiguity between two different populations, not a missing comparison rule. Concrete change: Separate and name:

subset-origin rows: rows whose headline score uses 
𝑊
𝑆
W
S
	​

 because a main-workload component is missing;

subset-evaluable rows: all ranking configurations with FullCost on 
𝑊
𝑆
W
S
	​

, subject to the existing valuation and blocker rules.

Attach the singleton dispersion statuses only to the first population. Print the comparison-population counts separately beside the subset frontier and bar outputs. What is new relative to the ledger: E190 already supplies the intended comparison rule, and E180/E277 already define stratum diagnostics. This finding concerns their juxtaposition in this paragraph, not a request to adopt those rules again. Source: part 3, “Missing component for a row,” E190 and the adjacent subset-calibration contract; blob 12f2896bb89ca9d560cf660b45f36a83e0683593.

2. Methodology design recommendations
1. Make the agent-cost exposure statement exact

Keep O123’s official scores and existing harness sensitivity unchanged. Define the transparent accounting identity

𝐶
𝑖
(
𝑘
)
=
𝐶
𝑖
−
𝐴
𝑖
+
𝑘
𝐴
𝑖
=
𝐶
𝑖
[
1
+
𝑠
𝑖
(
𝑘
−
1
)
]
,
C
i
	​

(k)=C
i
	​

−A
i
	​

+kA
i
	​

=C
i
	​

[1+s
i
	​

(k−1)],

where 
𝑘
k is a multiplier applied only to the observed Coding Agent Index component.

This yields precise interpretations:

𝑘
=
1
k=1: published cost.

𝑘
=
0
k=0: accounting endpoint removing the entire component—not an estimate of agent-free execution cost.

0
≤
𝑘
≤
1
0≤k≤1: basket-cost reduction no larger than 
𝑠
𝑖
s
i
	​

.

𝑘
>
1
k>1: no finite evidence-based upper bound unless the evidence independently bounds 
𝑘
k.

Any displayed value or rank effect should come from replaying this cost through the row’s applicable anchor object and clipping rule. Do not assign probabilities to 
𝑘
k or admit it to interval outputs without qualifying evidence.

This sharpens the existing disclosure without adding a workload assumption, transferring benchmark results, changing weights, or creating an unsupported official uncertainty interval.

Source: part 3, “Coding agent,” “Workload object W,” and “Anchor applicability”; blob 12f2896bb89ca9d560cf660b45f36a83e0683593.

2. Publish separate membership lists for subset diagnostics and subset comparisons

For each subset workload, expose two explicitly named ID lists:

𝑂
𝑊
𝑆
=
{
𝑖
:
row 
𝑖
 uses 
𝑊
𝑆
 for its headline score
}
,
O
W
S
	​

	​

={i:row i uses W
S
	​

 for its headline score},
𝐸
𝑊
𝑆
=
{
𝑖
:
FullCost
⁡
(
𝑖
,
𝑊
𝑆
)
}
.
E
W
S
	​

	​

={i:FullCost(i,W
S
	​

)}.

Apply existing valuation eligibility and blocker handling to 
𝐸
𝑊
𝑆
E
W
S
	​

	​

 when constructing its frontier and bar comparison objects. Use 
𝑂
𝑊
𝑆
O
W
S
	​

	​

 only where a diagnostic specifically describes the subset-origin stratum.

Add a regression fixture with one subset-origin row and several main-workload rows complete on the subset. Assert that the subset comparison includes the eligible main-workload rows, while the subset-origin dispersion diagnostic remains a singleton.

This is a clarification and implementation check for E190, not a proposed change to O17/O117 or to the owner-required mixed-workload headline ordering.

Source: part 3, “Missing component for a row,” E190, and “Cost completeness”; blob 12f2896bb89ca9d560cf660b45f36a83e0683593.

3. Questions for the owner

None.

4. Verdict

The reviewed sections state the restricted claim scope, separate API and Plan buyers, disclose the present lack of supported Plan frontier/bar claims, and preserve exact-configuration evidence. My remaining feedback concerns the precision of one quantitative assurance and the distinction between two subset populations—not a challenge to the fixed cohort, evidence, or weighting policies.

VERDICT: HAS FEEDBACK