0. Read check

Read all 14 parts, in order, through the GitHub connector at commit 47978a9327e760b38ed19e479bf7f31f556f92ae, including each part’s end. Part 13 ends mid-sentence; I identify its last complete sentence and quote its trailing fragment separately.

Draft’s first line:

ValueRank methodology — draft r164

Final sentences, in part order:

> Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

> Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

> These warnings test the API cost shape only; on the Plan basis the workload question is the M_W identification status.

> Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

> A schema change moves the route to the possibly-superseded stage.

> Domain validity is separate from evidence completeness.

Part 7 ends with a table row whose final sentence is:

A configuration the board lists twice takes the row selected as in the added-leaves bullet).

For precise boundary verification, the actual final table-cell text begins with lowercase “a” and reads:

a configuration the board lists twice takes the row selected as in the added-leaves bullet) | — | 10% | — | points of 60; z = 100 × points / 60 |

> Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

> Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

> From four configurations the three positions are distinct. Boundary wording as actually printed:

from four configurations the three positions are distinct.

> Each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations. The actual sentence begins earlier:

A family listed under O38 with an indicative value (O41) is not a competitor in any frontier or bar output; each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

> Every cost check reads C_W, never the Index diagnostic. This is the final clause of the part’s long release-tests sentence; the literal ending is:

widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic.

Last complete sentence:

Each capture publishes the rendered-frontier entrants and exits against the previous capture, and the reconciliation report lists every frontier and near row with its rank status.

Trailing fragment, read to the file’s end:

Today the capture, the latest under Intelligence Index v5.0 (the 2026-10-31 capture was the first, O132), was taken at 2026-11-01T05:53:05Z, before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

> Revision history: omitted from this review copy (not normative); it is in draft-r164.md in the same folder of the repository.

Source references below identify the supplied parts and their section/rule locators. The GitHub connector returned their full text but supplied no citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium

The new Bug Hunt summed leaf needs a covariance sensitivity, not just separate marginal variance assumptions. Issue: O163 changes the leaf to 
𝑋
=
𝑃
+
𝑈
X=P+U, planted fixes plus genuine unplanted fixes. E301’s S1T approximation uses

Var
⁡
(
𝑋
)
≈
105
𝑝
~
(
1
−
𝑝
~
)
+
𝑢
.
Var(X)≈105
p
~
	​

(1−
p
~
	​

)+u.

This implicitly sets the covariance between planted and unplanted fixes to zero. The two outcomes come from the same repository runs and agent execution, but the approximation neither includes their covariance nor publishes a sensitivity for it. The generic disclosures about task independence and omitted harness/run effects do not expose this additional within-leaf assumption.
Source: part 7, Bug Hunt leaf; part 9, S1T; part 12, Bug Hunt estimand E29. Why it hurts the objective: this SD feeds adjacent-rank separability, noise bands and the noise-margin bar companions. An omitted positive or negative covariance changes those reader-facing distinctions even with the displayed score fixed. This is particularly relevant immediately after changing Bug Hunt from one score to a sum of two outcomes. Concrete change: keep O163’s score and E301’s primary approximation, but publish a within-leaf covariance sensitivity:

𝜎
𝑋
2
(
𝜌
)
=
𝑣
𝑃
+
𝑣
𝑈
+
2
𝜌
𝑣
𝑃
𝑣
𝑈
,
σ
X
2
	​

(ρ)=v
P
	​

+v
U
	​

+2ρ
v
P
	​

v
U
	​

	​

,

where 
𝑣
𝑃
=
105
𝑝
~
(
1
−
𝑝
~
)
v
P
	​

=105
p
~
	​

(1−
p
~
	​

), 
𝑣
𝑈
=
max
⁡
(
𝑢
,
0.5
)
v
U
	​

=max(u,0.5), and 
𝜌
∈
{
−
1
,
0
,
1
}
ρ∈{−1,0,1} is explicitly a specification stress, not estimated dependence. Publish whether the separable-pair count, band assignment or bar companion changes. Where the owner’s public run records provide paired planted/unplanted counts, publish their empirical covariance separately without silently importing run-to-run uncertainty into Θ. What is new: this addresses the covariance created by O163’s newly summed outcome, not the already-adopted Bug Hunt harness sensitivity, repository limitation or generic task-correlation grid. It requires no change to O163 and no transfer or imputation.

The self-described executable cohort definition contradicts the retained-cohort policy. Issue: part 12’s “Cohort rule (executable)” says:

the cohort is exactly the plotted configurations on the rendered frontier plus those with rounded Index ≥ F(c) − 3, each its own row; no other configuration enters it.

O145 and E306 instead add one-release retained configurations, and the current draft explicitly includes ten. The precedence rules resolve the policy in favour of O145, but the purported executable definition still defines the wrong set.
Source: part 1, Cohort and configuration; part 12, Cohort rule (executable). Why it hurts the objective: cohort membership controls coverage searches, ranking eligibility and refresh reconciliation. Two implementations following different ostensibly normative definitions can disagree about which configurations must be evaluated. A methodology this dependent on executable contracts should not require a reader to repair its set definition through precedence. Concrete change: distinguish the plotted cohort 
𝑃
𝑡
P
t
	​

 from the complete cohort 
𝐶
𝑡
C
t
	​

:

𝑃
𝑡
=
𝐹
𝑡
∪
𝑁
𝑡
,
𝑇
𝑡
=
𝑃
𝑡
−
1
∖
𝑃
𝑡
,
𝐶
𝑡
=
𝑃
𝑡
∪
𝑇
𝑡
.
P
t
	​

=F
t
	​

∪N
t
	​

,T
t
	​

=P
t−1
	​

∖P
t
	​

,C
t
	​

=P
t
	​

∪T
t
	​

.

Here 
𝑃
𝑡
−
1
P
t−1
	​

 means the preceding release’s plotted cohort, excluding its retained rows. Apply the existing O145/E306 state transition once per exit. Replace “no other configuration enters it” with the explicit union, and test that all capture, roster, search and ranking consumers use the appropriate set. What is new: this is an implementation-contract conflict remaining after adoption of O145/E306, not a challenge to retention or the fixed AA cohort policy.

Low

The S1T generated-description contract still promises a mean-preserving alternative after E303 establishes that clipping prevents exact mean preservation. Issue: part 10’s normative stream description calls O154’s alternative “mean-preserving,” whereas part 9 correctly explains that recentring followed by clipping can shift its mean. E303 already requires the realised shift to be reported.
Source: part 9, S1T and E303; part 10, Joint admissible set Θ / E155 stream descriptions. Why it hurts the objective: the short description is the wording most likely to appear beside the published scenario output; it overstates what the alternative controls. Concrete change: replace “mean-preserving alternative” with “recentred, clipped alternative; realised mean shift reported.” Make the description lint reject “mean-preserving” for a clipped kernel unless the generated kernel object establishes that property. What is new: the statistical correction is already adopted; the remaining defect is its contradictory normative output text.

2. Methodology design recommendations

Prioritise a dependence envelope for the newly summed Bug Hunt outcome. Keep scores, nominal weights and interval claims unchanged. Add the covariance stress above to the existing analytical SD calculation, then report its effects on:

adjacent-pair separation;

the quality noise margin;

displayed noise bands;

each bar’s noise-margin companion.

This is implementable entirely from the planted and unplanted means already captured. The endpoint correlations are stress cases, not claims that either is empirically likely. If the conclusions do not change, one compact “unchanged across the covariance envelope” result is sufficient.

Compile cohort membership from one explicit state-transition object. Extend the existing E306 states into the authoritative executable definition, rather than adding another diagnostic. A release record should expose:

text
plotted_now
plotted_previous_release
retained_now
complete_cohort

Assert:

text
retained_now = plotted_previous_release - plotted_now
complete_cohort = plotted_now ∪ retained_now

Re-entry and subsequent exit should follow E306’s existing once-per-exit rule. Generate the prose definition and current membership counts from the same object. This implements the adopted policy rather than changing cohort selection.

Finish propagating E303 into the published uncertainty vocabulary. Use a kernel property such as mean_treatment = recentered_then_clipped, accompanied by the already-required realised mean shift and clipping rate. Generate descriptions from that property. This avoids fixing the mathematical explanation while leaving a stronger claim in the output contract.

These recommendations do not reopen the adopted cost/quality weights, exact-variant evidence rule, Plan numerator restrictions, full-utilisation estimand, subset-row policy or published-record interpretation of interval labels.

3. Questions for the owner

None.

4. Verdict

The draft is close to methodological convergence. Its separation of displayed arithmetic, published-record interval claims and noise/specification scenarios is substantive, and its exploratory Plan limitation is explicit rather than concealed.

The remaining material feedback concerns one newly introduced uncertainty assumption and one contradictory executable definition. Neither requires changing the binding owner policies, collecting private telemetry or commissioning new benchmark runs.

VERDICT: HAS FEEDBACK