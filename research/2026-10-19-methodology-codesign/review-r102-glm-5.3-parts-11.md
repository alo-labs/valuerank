0. Read check

Read both requested parts to their ends at commit 5c2ab13991d61e5a15c418407e9c9e95db001918. This review covers only those parts.

Part 11

First line:

Uncertainty (three separate layers, one scenario engine)

Final sentence:

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

Source: part 11.

Part 12

First line:

Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress.

Final sentence:

The population is the ranking's ranked rows that are not provisional and have a displayed quality (every leaf of the ranking, O36; a listed row never sets a bar), ordered by displayed quality ascending, then configuration ID.

Source: part 12.

1. Findings by severity
Critical

None.

High

None.

Medium

S1T’s mean-shift audit explicitly covers the binomial alternative, but not the other clipped-normal kernels. Issue: Part 11 specifies normal draws clipped to 0–100 for non-binomial leaves, including Bug Hunt, and explicitly requires reporting the realised mean shift after clipping for the recentred binomial alternative. The stated diagnostic does not establish the equivalent audit for every clipped-normal leaf. Part 12 then uses the resulting mixed-target stress to describe performance dispersion. Source: part 11 Source: part 12 Why it hurts the objective: Clipping a symmetric normal near a boundary changes both its mean and its endpoint mass. Consequently, an S1T ordering or noise-margin result can reflect a systematic kernel-induced movement as well as added dispersion. That distinction matters particularly for Bug Hunt: its scores use the live board-normalisation denominator, while its kernel approximates single-run dispersion rather than uncertainty in the published mean. This is not a criticism of that adopted target; it is a request to expose the additional effect of bounding its kernel. Concrete change: Extend samplingMeanShift to every bounded performance kernel, recording its published centre, realised mean, displacement, lower/upper endpoint masses, and quality-weighted displacement. Publish the nominal-weight composite’s expected displacement beside S1T’s separability and noise-margin results. What is new relative to the ledger: E303 already recognises post-clipping displacement for the recentred binomial alternative. This finding concerns the other normal kernels and their aggregate effect, not a request to revisit O142, O154, or the accepted mixed-target interpretation.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the kernel-displacement audit universal

Keep the adopted primary kernels and scores unchanged. Add the following deterministic diagnostic to each S1T leaf kernel 
𝐾
𝑖
𝑏
K
ib
	​

:

Δ
𝑖
𝑏
=
𝐸
𝐾
𝑖
𝑏
[
𝑍
𝑖
𝑏
]
−
𝑧
𝑖
𝑏
.
Δ
ib
	​

=E
K
ib
	​

	​

[Z
ib
	​

]−z
ib
	​

.

For a normal kernel implemented as clipping, define the operation explicitly:

𝑍
𝑖
𝑏
=
min
⁡
(
100
,
max
⁡
(
0
,
𝑋
𝑖
𝑏
)
)
,
𝑋
𝑖
𝑏
∼
𝑁
(
𝑧
𝑖
𝑏
,
𝜎
𝑖
𝑏
2
)
.
Z
ib
	​

=min(100,max(0,X
ib
	​

)),X
ib
	​

∼N(z
ib
	​

,σ
ib
2
	​

).

Also record:

Pr
⁡
(
𝑋
𝑖
𝑏
≤
0
)
Pr(X
ib
	​

≤0);

Pr
⁡
(
𝑋
𝑖
𝑏
≥
100
)
Pr(X
ib
	​

≥100);

the kernel’s resulting mean and variance.

This distinguishes clipping, which creates endpoint atoms, from conditioning a normal to remain inside the interval. Part 11 already requires kernel objects to describe truncation and dependency details, so this extends an existing registry rather than introducing another uncertainty layer. Source: part 11

Priority 2 — Attribute the aggregate shift without adding another ranking

For each fully observed row, calculate:

Δ
𝑖
𝑄
=
∑
𝑏
𝑤
𝑏
100
Δ
𝑖
𝑏
.
Δ
i
Q
	​

=
b
∑
	​

100
w
b
	​

	​

Δ
ib
	​

.

Publish this as “kernel-induced expected quality displacement”, with the largest contributing leaves. Do not interpret it as evidence of improvement or subtract it from the official score.

Beside each S1T separability or noise-margin output, distinguish:

systematic displacement introduced by the declared kernels;

dispersion around their resulting means.

This uses only the already captured scores, weights and kernel parameters. It needs no new benchmark runs, private telemetry, transferred evidence or analyst buyer profile. It also preserves the draft’s separation between published-record interval outputs and scenario-only performance stresses. Source: part 12

3. Questions for the owner

None.

4. Verdict

The reviewed sections carefully distinguish published-record bounds, scenario conventions, performance dispersion, Plan transport and blocker eligibility. My remaining finding is a narrow extension of the existing clipping audit: expose the displacement introduced by every bounded performance kernel, not only the binomial alternative.

VERDICT: HAS FEEDBACK