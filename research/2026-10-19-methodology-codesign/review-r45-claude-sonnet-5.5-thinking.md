1. Findings by severity
Critical

None.

High

None.

Medium

The rounding-kernel rules do not fully specify the joint law when rounded records are linked by accounting identities.

Issue: E83 requires scenarios to satisfy the original identities, while E25 assigns uniform kernels to rounding intervals. Those instructions are insufficient when several independently published rounded fields constrain the same primitive quantities. For example, if two component costs and their aggregate are all rounded, independently sampling all three generally violates the aggregation identity. Deriving the aggregate instead can violate its published rounding interval. The draft correctly prohibits undeclared rejection sampling, but does not register the joint law that resolves this case.
paste.txt

Why it hurts the objective: Two implementations could use the same records, intervals and seed yet produce different scenario frequencies—or one could find S0 unevaluable where the other silently conditions its draws. This matters because S1 inherits S0 and can authorise a scenario-supported-cheapest label. This is a specification gap, not evidence that an existing numerical result is wrong.
paste.txt

Concrete change: Register an executable joint-rounding object for each connected constraint component: which published fields constrain the component, which quantities are primitives, the probability measure, its parameterisation, and its sampling algorithm. If no joint convention is registered, retain deterministic bounds and withhold the affected scenario frequencies.

What is new relative to the ledger: E83, E108 and E145 already require feasibility and valid targets. This finding concerns the remaining distinction between a feasible set and a uniquely specified sampling law on that set.

The published-record uncertainty claim still promises benchmark-noise scenario outputs that the v1 stream allowlist does not produce.

Issue: The Normative definitions say benchmark noise—including published confidence intervals and run-to-run ranges—is reported through scenario shares. The Bug Hunt section similarly says public run-to-run spread enters scenario shares. However, E145 explicitly excludes fitted-rating intervals and run/task resamples from S0–S2, permits them only in separately named streams, and states that none exists in v1. The governing allowlist is clear; the promised output is not.
paste.txt

Why it hurts the objective: Readers could interpret the uncertainty beside ranks as reflecting benchmark repeatability, even though v1 covers reporting precision, conventional missing-evidence draws and weight stress—not expected-performance or future-run uncertainty. That distinction is consequential for “value in practice.”
paste.txt

Concrete change: Replace the unconditional promises with: “Benchmark repeatability and fitted-parameter uncertainty are outside v1 scenario shares; separately named streams may report them when supported by public evidence.” Print the actual target description beside each headline uncertainty column.

What is new relative to the ledger: This does not reopen E145 or request that run noise enter S0. It identifies residual contradictory output promises after that decision was adopted.

Low

None.

2. Methodology design recommendations
Priority 1 — Complete the joint-rounding sampling contract

For each connected component of rounded evidence, define

𝑃
=
{
𝑣
:
ℓ
≤
𝑣
≤
𝑢
,
 
ℎ
(
𝑣
)
=
0
,
 
𝑔
(
𝑣
)
≤
0
}
.
P={v:ℓ≤v≤u, h(v)=0, g(v)≤0}.

Keep the existing certified-feasibility prerequisite, but separately record whether the component has a registered scenario law. Feasibility alone must not activate sampling.

An implementable design is:

For unconstrained rounding variables, retain the existing uniform kernels.

For affine-linked rounding records, register a specific convention—for example, uniform volume on the feasible polytope in a declared set of free source coordinates.

Mark that joint convention as conventional rounding treatment, not an empirically established error distribution.

Permit exact conditional sampling or rejection sampling only when the resulting law and algorithm are explicitly registered. This follows the draft’s existing prohibition on silently conditioning draws.
paste.txt

If sampling cannot be implemented under the registered resource limits, publish the bounds and “joint rounding law not evaluated,” rather than independent approximations.

Publish fields such as constraint_component_id, free_coordinate_ids, joint_law_id, sampler_version, and sampling_status.

Add a regression fixture with two rounded component costs and one rounded aggregate. Every draw must satisfy all three reporting intervals and the exact accounting identity. Equivalent accounting representations should produce the same distribution of derived workload cost when they represent the same sampling object.

This requires no new provider telemetry: it operates on the public records and accounting constraints already required by the registry.

Priority 2 — Generate uncertainty descriptions from stream manifests

Extend the existing target-profile mechanism so that presentation text cannot contradict it. E143–E145 already provide the necessary foundation.
paste.txt

For v1, generate descriptions along these lines:

Output	Description beside the output
S0	Published-record reporting-precision scenarios
S1	S0 plus conventional missing-evidence scenarios
S2 core	S1 plus hierarchical weight stress
Benchmark repeatability	Not quantified in v1 scenario shares

Use a build-time lint rule: any statement that a source interval or run range “enters scenario shares” must reference an active stream whose allowlist admits that target and sampling level.

This preserves the owner’s published-record estimand and all existing scoring policies. It makes the limits of the uncertainty output explicit, rather than requiring readers to reconcile distant sections.

3. Questions for the owner

None. These changes can be implemented without revisiting the binding owner decisions.

4. Verdict

VERDICT: HAS FEEDBACK