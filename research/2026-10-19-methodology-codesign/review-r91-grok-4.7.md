0. Read check

I opened all 14 parts through the GitHub connector, in order, at commit 42533a0b6af2b57612ce33182f67fa5e8787de21, and read each returned file to its end.

First line:

ValueRank methodology — draft r173

Final sentence of each part, in order:

> Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

> Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

> Release assertion: the scored field is the basket sum, not cost per task, not AA's 7:2:1 blended price, not total Index cost.

> The transfers keep their assumption label and caution. Correction to preserve the exact source wording: the final sentence is:

Fable 5.1 is not a donor-error gauge (owner decision O35, 2026-10-21): Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

> Fixtures: two concordant reports 41 days apart, neither admitted earlier, where the older one leaves the partition and the route is diagnostic; a model with a current controlled measurement and a lapsed report pair, where the controlled route stays and the report route is diagnostic; a transfer from a lapsed report donor, which is diagnostic.

> GPT-6 Astra (max)'s selected route moved from ChatGPT Plus to a higher plan under O45.

> AA Intelligence Index and output speed are diagnostics, not quality.

> Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

> Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

> The population is the non-provisional cohort rows with a displayed quality, ordered by displayed quality ascending, then configuration ID.

> The summary says these outputs compare ranked configurations only and names the listed configurations. The exact final sentence, including its preceding clause, is:

Each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

> Widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic. This is the closing clause of the part’s final, semicolon-delimited “Release tests” sentence, which begins:

Release tests. Omniscience vector above; Bug Hunt vector above; Index reconciliation …

> One AA state (E217): the model-page snapshot, the chart capture, the Coding Agent Index capture and the cost-chart capture are each at most 7 days from the snapshot, the build tests each of the last three against the release cutoff and the snapshot itself defines it (O65), and the build fails otherwise, and capture proximity alone does not show one AA revision, so the chart is also reconciled with the model pages on the fields both publish: each chart point linked to a captured page must carry that page's total Index cost (within 1%) and its displayed Index (the page's unrounded Index within half a display unit), and a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87); The part ends at that semicolon; the sentence continues in part 14.

> Revision history: omitted from this review copy (not normative); it is in draft-r173.md in the same folder of the repository.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. E23 states the category-repricing relationship in the inverse direction

Issue: Part 12’s release tests state:

otherwise category repricing changes Plan cost by (p·x / p·u)

With 
𝑥
x denoting measured consumption and 
𝑢
u the target workload’s demand, this is the reciprocal of the ratio in effective Plan cost. It also does not specify whether “changes … by” means the new cost, a multiplicative change, or a difference.

From the draft’s own definitions, holding measured consumption, workload demand and gross cash fixed,

𝑀
(
𝑝
)
=
𝑝
⋅
𝑥
𝐹
,
𝑃
(
𝑝
)
=
𝑝
⋅
𝑢
𝑀
(
𝑝
)
=
𝐹
𝑝
⋅
𝑢
𝑝
⋅
𝑥
.
M(p)=
F
p⋅x
	​

,P(p)=
M(p)
p⋅u
	​

=F
p⋅x
p⋅u
	​

.

Consequently, between price vectors 
𝑝
p and 
𝑝
′
p
′
,

𝑃
(
𝑝
′
)
𝑃
(
𝑝
)
=
𝑝
′
⋅
𝑢
𝑝
⋅
𝑢
𝑝
⋅
𝑥
𝑝
′
⋅
𝑥
.
P(p)
P(p
′
)
	​

=
p⋅u
p
′
⋅u
	​

p
′
⋅x
p⋅x
	​

.

Why it hurts the objective: This is a normative release-test requirement concerning exactly the distinction ValueRank needs to preserve: subscription consumption valued at API prices is not cash paid, and its valuation depends on token mix. Public usage accounting likewise distinguishes API-equivalent value from the subscription invoice. A reversed fixture could accept the wrong direction of a repricing effect while appearing to validate the Plan arithmetic.
stackspend

Concrete change: Replace the quoted requirement with the two equations above, define every symbol locally, and add an asymmetric two-category fixture:

𝐹
=
10
F=10, 
𝑥
=
(
100
,
0
)
x=(100,0), 
𝑢
=
(
0
,
10
)
u=(0,10).

At 
𝑝
=
(
1
,
1
)
p=(1,1): 
𝑀
=
10
M=10, 
𝑃
=
1
P=1.

At 
𝑝
′
=
(
2
,
1
)
p
′
=(2,1): 
𝑀
′
=
20
M
′
=20, 
𝑃
′
=
0.5
P
′
=0.5.

Doubling the price of the category present only in measured consumption halves the displayed effective cost; it does not double it.

What is new relative to the ledger: This is not another request for category telemetry, a category-revaluation branch, or a change to the valuation gate. It identifies an inverted relationship in an existing mandatory test. I have reviewed the specification, not the implementation, so I am not asserting that the executable test currently contains the same inversion.

Low
L1. E151 retains an obsolete statement about previously admitted reports never reaching age stages

Issue: Part 4 says:

a counting report never reaches an age stage: only change detection can make a counting partition "possibly superseded".

The surrounding text and the lifecycle table correctly apply O127: previously admitted reports keep counting outside the admission window and age like measurements. The quoted sentence is therefore false for precisely those reports.

Why it hurts the objective: A maintainer implementing report pooling from that paragraph could incorrectly prevent age-based transitions for an admitted partition, keeping old Plan evidence current indefinitely. The later rules resolve the intended policy, but the specification should not require precedence reasoning to discover it.

Concrete change: Replace the sentence with:

A newly admitted report is at most 30 calendar days old at admission. Reports retained under O127 subsequently age through the ordinary lifecycle; a partition takes its most advanced contributor’s stage.

What is new relative to the ledger: O127 and the two-clock design are already adopted. This finding concerns an unreconciled assertion left in their operative explanation, not a proposal to change either decision.

2. Methodology design recommendations

Prioritise an algebraic consistency test for Plan valuation. Implement M1 as a property test over positive price, measured-consumption and workload-demand vectors:

𝑃
(
𝑝
)
 
(
𝑝
⋅
𝑥
)
=
𝐹
 
(
𝑝
⋅
𝑢
)
.
P(p)(p⋅x)=F(p⋅u).

Test the repricing ratio separately, including asymmetric category changes and uniform scaling. This directly tests the relationship rather than relying only on examples of cancellation. It requires no additional public evidence and changes no owner policy.

Generate the report-lifecycle explanation from the same state model as the lifecycle table. Keep two explicit report attributes:

Admission status: newly eligible, previously admitted, or not admitted.

Evidence stage: current, possibly superseded, expired in grace, or demoted.

Generate the prose describing their interaction from that model, or add a documentation assertion forbidding the claim that counting reports cannot age. This is a narrow consistency improvement to O127/E151, not additional lifecycle machinery.

Keep these repairs separate from a methodology migration. Neither recommendation changes weights, cohorts, evidence admission, the scored workload, anchors or the published-record target. Treat them as corrections to the executable specification and documentation. If the implementation already satisfies the corrected equations and lifecycle transitions, report that explicitly and leave scores unchanged; if it does not, publish the affected-row replay under the existing attribution rules.

3. Questions for the owner

None.

4. Verdict

The draft’s major limitations are extensively disclosed, and the ledger already addresses most obvious objections. I have no new material challenge to its fixed cohort policy, exact-variant rule, evidence hierarchy or owner-selected ranking design. The remaining material finding is the inverted E23 repricing requirement; the report-age sentence is a smaller consistency repair.

VERDICT: HAS FEEDBACK