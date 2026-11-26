0. Read check

Read all 14 parts, in order, through the GitHub connector at commit 955a856b2c8c1c60642ae97ff0982a609f8fdd6f, including each part’s end.

Draft’s first line:

ValueRank methodology — draft r156

Last 12 whitespace-delimited words of each part, preserving punctuation and Markdown:

> carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py).

> or provider declined some tasks on safety grounds") also flags "partial component".

> On the Plan basis the workload question is the M_W identification status.

> for other Claude models; the transfers keep their assumption label and caution.

> (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

> no epsilon is introduced. Domain validity is separate from evidence completeness.

> value for 10 of 19 cohort rows in the 2026-10-17 snapshot) |

> a bias bound in the identification layer); repetitions are not a bias.

> not separable" and its S0 result is not described as target-workload support.

> of both rankings has a cost, so the two ladders are equal.

> Bug Hunt and AI Coding Daily name the harness on each record).

> or definite result; every cost check reads C_W, never the Index diagnostic.

> before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

> normative); it is in draft-r156.md in the same folder of the repository.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The current Plan research does not cover the models added by the v5 cohort migration

Issue: Part 5, “Plan-allowance research,” explicitly says that the latest all-provider search, dated October 25, did not search GPT-6.1 Terra or Gemini 4 Carbon by name because both entered later under O132. Nevertheless, the release uses that search as its current O71/O75 research, and Terra receives the O45 transferred figures on all four ChatGPT plans.

Provider coverage is not model coverage: the report-admission rules require an exact model, and a provider-level search cannot establish whether an admissible report pair exists for a subsequently added model.

Why it hurts the objective: The Plan arithmetic can continue using an authorised assumption without completing the procedure intended to discover evidence that would replace it. For Terra, this affects ranked Plan rows now—not merely an excluded configuration’s diagnostic. The six-day search-age disclosure explains the temporal gap, but does not resolve the model-coverage gap.

Concrete change:

Make O71 research coverage an explicit manifest keyed by (model version, plan tier, research stage), with effort pooling applied under O87.

At cohort reconciliation, compare the required cells with the cells actually searched.

Complete all three stages for newly uncovered cells before treating the release’s Plan research as complete.

A new cell can reuse earlier research artifacts only when those artifacts demonstrably searched that exact model and plan; a provider match alone is insufficient.

What is new relative to the ledger: This is not a request to change O71–O75, authorised transfers, report concordance or the seven-day search-age limit. It is the newly documented O132 entrant case in which provider coverage passes while exact-model research coverage is absent.

M2. The specification gives incompatible memberships for the admission, anchor and influence panels

Issue: Part 2, “Counts, defined once,” states:

“The admission reference panel, the anchor references and the common-workload panel for cost influence are the same rows.”

It also reports main-workload FullCost counts of 5 and 15.

Part 3 instead says that the Claude Opus rows fail FullCost because their Index reconstruction is unresolved, giving admission and anchor-reference panels of 4 and 14. It then expressly includes those unresolved rows in the common-workload influence panel because they remain scored on the main workload.

These are different population contracts, not merely different names for the same panel.

Why it hurts the objective: The influence disclosures explain what the nominal 25% cost weight actually does. Using the complete-evidence reference panel versus all scored main-workload rows can change the reported SD ratio, covariance allocation and ordering agreement. A reproducer following Part 2 can obtain different diagnostics from one following Part 3, even with identical evidence.

The governing E209 rules provide a way to resolve the conflict; I am not claiming that the implementation’s published figures are wrong.

Concrete change: Define and render the populations separately:

𝑃
a
d
m
i
t
=
𝑃
𝐾
(
𝑊
)
,
P
admit
	​

=P
K
	​

(W),
𝑃
a
n
c
h
o
r
=
{
𝑖
∈
𝑃
𝐾
(
𝑊
)
:
freeze-time valuation and omission rules pass
}
,
P
anchor
	​

={i∈P
K
	​

(W):freeze-time valuation and omission rules pass},
𝑃
i
n
f
l
u
e
n
c
e
=
{
𝑖
:
ranked and scored on the main workload’s anchor object
}
.
P
influence
	​

={i:ranked and scored on the main workload’s anchor object}.

Apply the Plan-row expansion where O48 requires it. Publish each panel’s IDs and exclusions, rather than asserting their equality. Under the current prose, the API admission/reference counts are 4 and 14, while the influence panel includes all 5 and 15 scored main-workload configurations.

What is new relative to the ledger: E91, E160 and E209 already define the relevant distinctions. The new finding is that the current v5 draft collapses them in its population summary while retaining their incompatible definitions elsewhere. This is a consistency repair, not a proposed policy change.

Low
L1. The release-test specification still contains pre-v5 accounting and superseded completeness wording

Issue: Part 12’s “Release tests” still requires:

“C_7 + HLE + Omniscience + CritPt reproduces AA’s total”

The current v5 accounting identity in Part 2 instead uses the six Index SDLC evaluations plus HLE-Diamond, Omniscience and CritPt v2. The same release-test paragraph says missing- or declined-task markers “alone determine completeness,” although E209 also requires successful Index reconstruction for those six components.

Why it hurts the objective: These are the stated acceptance tests for reproducibility. Leaving old benchmark/accounting identities in that section makes the test contract misleading, even though the governing rules elsewhere are clearer. Benchmark identity includes its dataset and scoring method, not just its label; the public-data contract should preserve that distinction through migrations.
honeyhive

Concrete change: Generate the accounting test from the registered v5 execution population, and replace the blanket marker-only statement with separate predicates for Index components and the Coding Agent Index.

What is new relative to the ledger: This concerns remnants left by the O132/O136/O137 migration, not a challenge to the adopted accounting or completeness policy.

2. Methodology design recommendations
Priority 1 — Make research completeness cohort-dependent, not merely provider- and date-dependent

Implement M1 as a deterministic coverage gate:

R
e
s
e
a
r
c
h
C
o
m
p
l
e
t
e
(
𝑉
)
=
⋀
𝑐
∈
𝐶
𝑉
⋀
𝑝
∈
𝑃
(
𝑐
)
⋀
𝑠
∈
{
w
e
b
,
C
l
a
u
d
e
D
R
,
S
i
l
v
e
r
B
u
l
l
e
t
D
R
}
C
o
v
e
r
e
d
(
𝑐
,
𝑝
,
𝑠
,
𝑉
)
.
ResearchComplete(V)=
c∈C
V
	​

⋀
	​

p∈P(c)
⋀
	​

s∈{web,ClaudeDR,SilverBulletDR}
⋀
	​

Covered(c,p,s,V).

Here:

𝐶
𝑉
C
V
	​

 is the current cohort’s model identities, with efforts pooled only as O87 permits.

𝑃
(
𝑐
)
P(c) contains the first-party plans requiring research under the existing policy.

Covered requires a logged exact-model search or an explicitly reusable exact-model artifact, not merely that the provider appeared in a research run.

Run this check after cohort reconciliation and before publishing route selection. Publish uncovered cells and their cause—new entrant, new plan or missing stage.

This uses existing public searches and artifacts. It does not require new measurements, inferred allowances or a change to the transfer policy.

Priority 2 — Give every diagnostic an explicit population object

Implement M2 with a small typed panel registry. Each panel should carry:

panel_id and membership hash;

ranking, basis, workload and anchor-object IDs;

membership predicate;

configuration or plan-row IDs;

exclusions with reasons.

Each diagnostic should reference its panel object directly. Documentation should render both counts and the membership relationship from those objects.

Add semantic assertions, beyond E265’s rendering checks:

Admission-panel members satisfy K for every admitted component.

Anchor references satisfy the freeze-time anchor predicate.

Influence-panel members share the applicable workload and anchor object.

Unresolved-cost rows remain in the influence panel when E209 requires, but never enter the complete-evidence panel.

Any sentence asserting panel equality is emitted only when the membership sets are equal.

The useful improvement is not another diagnostic; it is making the existing diagnostics unambiguously reproducible.

Priority 3 — Compile accounting acceptance tests from the versioned registry

For each accounting population, generate:

𝐶
a
g
g
r
e
g
a
t
e
=?
∑
𝑒
∈
r
e
g
i
s
t
e
r
e
d
 
c
h
i
l
d
r
e
n
𝑛
𝑒
𝑐
𝑒
.
C
aggregate
	​

=
?
e∈registered children
∑
	​

n
e
	​

c
e
	​

.

Keep the declared source-precision tolerance and aggregate/component exclusivity rules. Generate the corresponding documentation and fixtures from the same registered child list.

For completeness, retain the distinction already adopted:

Index SDLC component: exact published cost, no missing/declined marker, and successful Index reconstruction.

Coding Agent Index: O27’s published metric and its own missing/declined-task rules; raw telemetry-sum reconciliation remains diagnostic.

This prevents the next benchmark migration from leaving a correct governing rule beside an obsolete acceptance test.

I recommend no changes here to the fixed cohort policy, exact-variant matching, headline weights, Plan utilisation estimand or Value Multiple numerator rules.

3. Questions for the owner

None.

4. Verdict

The remaining material feedback concerns one uncovered research obligation created by the latest cohort migration and one contradictory population contract. Neither requires reopening the owner’s economic or ranking policies. The accounting-test remnants are a lower-severity migration cleanup. These findings are based on the complete draft; I have not independently audited the implementation or evidence bundle.

VERDICT: HAS FEEDBACK