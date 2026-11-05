0. Read check

Read all three listed files to their ends, in order, at commit 235647fd1927d0ae24b529a60722e4fd4a5e79ca. This review covers only those sections.

Part 10

First line:

Uncertainty (three separate layers, one scenario engine)

Final sentence:

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

Part 11

First line:

Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress.

Final sentence:

The current ladders are in Output 3 and scores.json barCurrency.

Part 12

First line:

Fewer than two population configurations pin no bar: all three bars, and every output that reads them, are published as unavailable.

Final sentence:

Each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The noise screen and its stated joint counterpart answer different questions

Issue: Part 12’s O171 noise screen uses

Δ
𝑖
=
𝑄
ˉ
𝑖
−
𝐻
𝜎
𝑖
2
+
𝜎
𝐻
2
,
Δ
i
	​

=
σ
i
2
	​

+σ
H
2
	​

	​

Q
ˉ
	​

i
	​

−H
	​

,

explicitly treating the bar setter as noisy. E337 then says that “S1T’s stress frequencies remain the joint reading.” But E52, also in part 12, fixes 
𝑄
𝑟
(
𝑠
)
=
𝐻
Q
r
	​

(s)=H in every scenario, and part 10 defines scenario bar events against that frozen reference. Consequently, S1T’s existing qualifying-and-cheapest frequency does not jointly evaluate the comparisons used by the noise screen: it redraws candidate and competitor quality but not the reference level.

Why it hurts the objective: The methodology correctly distinguishes a published-record claim from benchmark-noise diagnostics. This cross-reference nevertheless invites readers to interpret a fixed-threshold frequency as the joint version of a noisy-reference screen. Those can materially disagree, particularly near a bar, where the methodology already identifies the greatest sensitivity.

Concrete change: Keep the official frozen-bar events unchanged. Either:

remove the claim that existing S1T frequencies provide the screen’s joint reading, and explicitly state the target difference; or

add a separately named S1T diagnostic that draws a shared noisy reference and evaluates all qualification comparisons against that same draw.

New argument relative to the ledger: E337 already addresses the lack of simultaneous coverage across pointwise comparisons. This finding is different: even without claiming confidence coverage, the proposed joint counterpart uses a different reference object. It does not challenge O25, O128, O171 or the frozen-bar policy.

Low

None.

2. Methodology design recommendations
Priority 1: Make the reference treatment part of each noise diagnostic’s executable target

Extend the existing event/target signature with:

text
reference_treatment:
  fixed_frozen_level
  noisy_frozen_reference

reference_evidence_version
reference_dependency_rule

Use fixed_frozen_level for existing interval and scenario bar outputs. Their question remains: “Which configuration qualifies against this fixed published quality level?”

If a joint companion to O171 is desired, register a separate descriptive stress event. With 
𝜖
𝐻
(
𝑠
)
ϵ
H
	​

(s) a reference perturbation centred on zero, define

𝐻
n
o
i
s
e
(
𝑠
)
=
𝐻
+
𝜖
𝐻
(
𝑠
)
,
H
noise
(s)=H+ϵ
H
	​

(s),

and

𝐸
𝑖
(
𝑠
)
=
1
 ⁣
[
𝑄
𝑖
(
𝑠
)
≥
𝐻
n
o
i
s
e
(
𝑠
)
  
∧
  
∀
𝑗
 cheaper than 
𝑖
,
  
𝑄
𝑗
(
𝑠
)
<
𝐻
n
o
i
s
e
(
𝑠
)
]
.
E
i
	​

(s)=1[Q
i
	​

(s)≥H
noise
(s)∧∀j cheaper than i,Q
j
	​

(s)<H
noise
(s)].

Implementation requirements:

Use the same cheaper-row comparison panel as E341.

Draw the reference perturbation once per scenario and share it across all comparisons.

Pin the reference evidence version and kernel explicitly. Do not silently substitute the setter’s latest evidence for the evidence associated with the frozen bar.

When the candidate or competitor is the setter using that same observation, reuse its primitive rather than manufacturing an independent second measurement.

Publish the frequency as a mixed-target noise stress, consistent with E330—not as a confidence probability or an authorising label.

This needs no new benchmark measurements: it can use the captured records and kernels already required by S1T. If the necessary frozen-reference kernel was not retained, mark the new diagnostic unavailable rather than reconstructing it from current data.

Priority 2: Add a reference-target regression fixture

Test a configuration that is itself the bar setter.

Against the fixed published level, its redrawn score may fall above or below 
𝐻
H.

Against the identical noisy observation reused as the reference, its quality difference is exactly zero in every replicate.

The fixture should verify that these events have distinct signatures and descriptions. A release-text lint should reject “joint reading of the noise screen” unless the referenced stream uses the screen’s reference treatment and comparison panel.

The important distinction is target, not additional sampling complexity. The existing fixed-bar S1T output remains useful; it simply should not be presented as the joint counterpart of a different comparison.

3. Questions for the owner

None. The minimum correction is editorial and does not require changing a binding owner decision; the additional joint diagnostic is optional.

4. Verdict

VERDICT: HAS FEEDBACK