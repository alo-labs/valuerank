0. Read check

Both listed parts were read through their ends at commit 5917e61757433bf61ca45bbb5cb030200bb8f863, in the requested order.

Part	First line	Last 12 words
9	## Uncertainty (three separate layers, one scenario engine)	not separable" and its S0 result is not described as target-workload support.
10	- **Specification**: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress.	on quality). The current ladders are in Output 3 and scores.json `barCurrency`.

Scope: this is a sectional review of these two files only. Rules attributed to other sections are treated as defined there.

. Findings by severity
Critical

None.

High
H1. The claim that a pricing-omission factor cannot affect another row’s membership test is false for PossibleFrontier

Issue. Part 10’s normative Frontier definition says that a recorded pricing-omission factor changes only the affected row’s interval range and scenario draw, “never another row’s label or membership test,” because the domains start at the published cost. But the same section defines PossibleFrontier through an existential quantifier over the entire admissible set. The upper endpoint of a blocker’s cost range can therefore determine another row’s possible membership.

A minimal counterexample, with all other inputs fixed:

Candidate 
𝑖
i: cost 10, quality 60.

Pricing-omission blocker 
𝑗
j: published cost 5, quality 70.

Factor 1 gives 
𝐶
𝑗
=
5
C
j
	​

=5: 
𝑗
j always dominates 
𝑖
i, so 
𝑖
i is not possibly on the frontier.

Factor 4 gives 
𝐶
𝑗
∈
[
5
,
20
]
C
j
	​

∈[5,20]: at 
𝐶
𝑗
=
20
C
j
	​

=20, neither dominates the other, so 
𝑖
i is possibly on the frontier.

The shared lower endpoint determines the adverse case for definite membership in this example, but does not determine possible membership. This follows directly from the definitions in the reviewed part 10.

Why it hurts the objective. The prose licenses an implementation shortcut that could suppress legitimate possible-frontier results or leave them unchanged when new public pricing evidence should change them. That compromises the distinction between “definite” and “possible,” which is central to the draft’s published-record uncertainty design.

Concrete change. Replace the blanket invariance statement with:

Holding all other constraints fixed, an O94 blocker’s unchanged published-cost lower endpoint preserves its adverse cost case for definite-frontier and confirmed-cheapest tests. Its upper endpoint can affect existential outputs, including PossibleFrontier; those outputs must evaluate the full admissible domain.

Add the two-factor example above as a regression fixture. Keep O114’s published-cost scenario treatment separate.

What is new relative to the ledger: this does not challenge O94, O98, O114 or E276. It identifies a quantifier-specific error in the claim that the upper endpoint cannot affect any membership test.

Medium

None.

Low
L1. The uncertainty taxonomy contradicts the active-stream description about published intervals

Issue. Part 9’s Measurement taxonomy says that “no source confidence interval enters any v1 stream today except GDPval-AA’s displayed rating interval.” Earlier in the same part, S1T explicitly uses the two Vals boards’ published standard errors. A standard error is not itself a confidence interval, so that sentence can be read narrowly as correct; however, the following statement that “other estimation uncertainty … [is] not quantified” is too broad, because those standard errors are explicitly used to model estimation uncertainty. Part 10’s generated uncertainty descriptions likewise say “other benchmark repeatability and fitted-parameter uncertainty” is not quantified without clearly enumerating the active Vals exception. See part 9 and part 10.

Why it hurts the objective. Readers cannot readily distinguish which uncertainty is source-supported, which is a task-count approximation, and which remains unquantified. The detailed stream specification is substantially clearer than its summary.

Concrete change. Generate the taxonomy summary from the same active-target manifest used for stream descriptions. Explicitly list Vals’ published-standard-error kernels alongside GDPval-AA’s assumed interval interpretation, task-count approximations and Bug Hunt’s single-run dispersion approximation.

What is new relative to the ledger: E155 already requires manifest-generated descriptions; this finding concerns the remaining narrative summary that does not accurately summarize the active kernels.

2. Methodology design recommendations
Priority 1 — Make blocker tests explicitly quantifier-aware

For frontier outputs, retain the existing definitions but make their computational requirements explicit:

DefiniteFrontier
⁡
(
𝑖
)
  
⟺
  
∄
 
(
𝜃
,
𝑗
)
:
𝜃
∈
Θ
,
 
𝑗
∈
𝑈
𝑊
∖
{
𝑖
}
,
 
𝑗
≻
𝜃
𝑖
.
DefiniteFrontier(i)⟺∄(θ,j):θ∈Θ, j∈U
W
	​

∖{i}, j≻
θ
	​

i.
PossibleFrontier
⁡
(
𝑖
)
  
⟺
  
∃
 
𝜃
∈
Θ
:
∀
𝑗
∈
𝑈
𝑊
∖
{
𝑖
}
,
 
¬
(
𝑗
≻
𝜃
𝑖
)
.
PossibleFrontier(i)⟺∃θ∈Θ:∀j∈U
W
	​

∖{i}, ¬(j≻
θ
	​

i).

These are different feasibility problems. The possible-membership test needs one jointly feasible state in which no competitor dominates; it cannot generally be reduced to testing blockers only at their minimum costs. This is an implementation clarification of the formulas already present in part 10, not a new ranking policy.

Add regression fixtures checking that, with fixed membership and other constraints:

Increasing a blocker’s cost upper bound can create possible membership.

It does not remove already possible membership.

An unchanged adverse lower endpoint does not by itself improve definite membership in the simple independent-cost case.

A scenario stream using O114’s published cost remains unchanged when only that upper bound changes.

This requires no additional data collection.

Priority 2 — Publish one generated kernel inventory beside the uncertainty outputs

Use the existing registered kernel and target objects to render a compact table:

Field	Purpose
Leaf and stream	Identify exactly where the kernel operates
Target	Published-score uncertainty, fitted-rating uncertainty, single-run dispersion, or specification convention
Public input	Task count, published standard error, displayed interval, or count decomposition
Assumed interpretation	State the approximation without presenting it as source documentation
Dependence treatment	Identify independent draws, shared primitives and registered dependence stresses
Output use	Scenario shares, noise bands, separability or noise margin; never interval certification unless separately eligible

The detailed ingredients already exist in part 9. The recommendation is to make this inventory the single source for both the short taxonomy and the longer stream descriptions, preventing the inconsistency in L1 without introducing another sensitivity analysis. Part 9

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK