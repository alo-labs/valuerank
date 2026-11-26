0. Read check

Read all three listed files to their ends at commit 2ca6c729a3f1a11bd08f5d669f5977875b087381. This review covers only parts 4–6 and treats rules cited from elsewhere as defined there.

Part 4

First line begins: “- Plan cost input (full-utilisation effective cost, labelled) = API cost input ÷ Value Multiple of the selected route.” The remainder of that same, unusually long line runs through the Plan-route selection, capacity and token-mix rules, ending “API-fallback rows are shown but excluded from Plan frontier and bar outputs.”

Last 12 words: “for other Claude models; the transfers keep their assumption label and caution.”

File SHA: a67938b476807c91e4424c93cf06121d9e852c88.

Part 5

First line: empty.

First nonempty line begins: “Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V]”.

Last 12 words: “is diagnostic; a transfer from a lapsed report donor, which is diagnostic.”

File SHA: b260d73018fa627620fed208a51b54ba4c8ac1bc.

Part 6

First line begins: “- Quota schema: the registry stores each plan's limit-schema version”. The same line continues through funding-aware capacity and multiple certification, ending “A schema change moves the route to the possibly-superseded stage.”

Last 12 words: “Plan rows resting on an owner assumption, by kind (marked †, E242).”

File SHA: e831914b90aa05d7994bb792bc062666ea7e038a.

The first lines of parts 4 and 6 are entire, multi-thousand-character paragraphs; their quoted openings and endings above identify those lines without reproducing substantial portions of the review material.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. An unstated measurement effort becomes an “exact-effort” evidence advantage through a naming convention

Issue: E246 binds a SemiAnalysis measurement that states no effort to AA’s bare-name configuration, currently the max configuration. That row then receives the comparator’s highest measurement grade; other efforts receive the lower O88 same-model grade. Yet the section explicitly acknowledges that SemiAnalysis states no effort. The naming convention establishes a deterministic attachment, not evidence that the measured execution used that effort. This matters because evidence grade precedes the comparison multiple in E85. Consequently, the convention can determine which measurement object wins against a report alternative. (Part 4, E85; part 6, E246 and GPT routes.)

Why it hurts the objective: the methodology otherwise carefully distinguishes observed facts from assumptions. Here, an assumed attachment can acquire a stronger evidence-priority status than the public measurement supports.

What is new relative to the ledger: this is not a request to remove O88 routes, reject effort-invariant allowances, or revisit the existing cross-effort sensitivity. The additional issue is the interaction between E246’s editorial attachment and E85’s selection precedence: an unspecified effort can create an “exact” evidence-grade advantage.

Concrete change:

Preserve E246’s deterministic route attachment and all owner-authorised figures.

Record measurement_effort = unspecified separately from bound_configuration.

Reserve “controlled measurement of the exact configuration” for measurements whose effort is documented.

Where effort is unspecified, give all permitted same-model efforts the same measurement grade, or publish a selector sensitivity that removes only the unsupported exact-effort advantage.

If owner policy requires the current grade distinction, label this an Owner decision challenge rather than presenting the attachment as observed exact-effort evidence.

M2. The exploratory-headline threshold depends on the number of plan rows, rather than solely on evidence coverage

Issue: E61 retains the “workload-unmatched: exploratory” headline while fewer than half of Plan rows have identified target-workload multiples. But O48 creates one row per configuration and plan, and the section includes providers with different numbers of plan tiers. The threshold therefore weights a configuration according to how many plans its provider sells. Adding tiers can change the headline’s status without improving identification for any previously represented configuration. (Part 4, per-plan comparator; part 6, identification yield and tier-specific MiMo routes.)

Why it hurts the objective: the headline purports to summarise evidential adequacy, but its denominator partly measures the product catalogue. A provider with several closely related tiers can disproportionately determine whether the whole Plan ranking appears exploratory.

What is new relative to the ledger: this is not the already-adopted request to count joint Plan evidence. It concerns the decision denominator used to switch the headline label, not the publication of evidence counts.

Concrete change:

Keep the existing route-row yield as a descriptive statistic.

Add a configuration-balanced identification yield, giving each configuration equal total weight across its ranked plans.

Use that balanced yield for the headline threshold, or retain the exploratory headline whenever the headline winner itself is workload-unmatched, regardless of aggregate yield.

Low
L1. The condensed “Value Multiple” definition does not preserve the operative gross-cash denominator

Issue: the quota-schema paragraph defines the primary multiple using subscription cash plus all additional cash required for the usage. The following “Value Multiple” paragraph shortens this to usage divided by “fee for that period.” Read independently, that definition can suggest subscription fee alone. The full operative accounting is clear elsewhere in the same section, so this is a definition-consistency issue, not a missing funding rule. (Part 6, quota schema and Value Multiple.)

Why it hurts the objective: this ratio is the central Plan cost input. Its short definition should remain correct when quoted in a table tooltip, summary or external explanation.

Concrete change: replace the short definition with:

Value Multiple = eligible API-priced consumption delivered during the stated fee period ÷ total gross cash required to obtain that consumption under the recorded purchase policy.

Keep the existing funding-flow and receipt requirements unchanged.

2. Methodology design recommendations

Separate evidence identity from editorial attachment in the route schema. Publish, for each measurement:

text
reported_model
reported_effort
bound_configuration
binding_rule
effort_match_status
comparator_evidence_grade

Use effort_match_status ∈ {documented_exact, unspecified, documented_other}. This makes E246 reproducible without silently converting an unknown effort into an observed match. A selector replay can then report whether removing that grade advantage changes the selected pair, displayed multiple or Plan score. No new private data or measurement campaign is required.

Make the identification headline configuration-balanced and winner-specific. For configurations 
𝑖
=
1
,
…
,
𝑁
i=1,…,N, with ranked plan rows 
𝑃
𝑖
P
i
	​

, publish:

𝑌
b
a
l
a
n
c
e
d
=
1
𝑁
∑
𝑖
=
1
𝑁
∑
𝑝
∈
𝑃
𝑖
1
{
𝑀
𝑖
𝑝
,
𝑊
 is identified
}
∣
𝑃
𝑖
∣
.
Y
balanced
	​

=
N
1
	​

i=1
∑
N
	​

∣P
i
	​

∣
∑
p∈P
i
	​

	​

1{M
ip,W
	​

 is identified}
	​

.

This preserves the current point-/set-identification taxonomy while preventing configurations with many tiers from receiving greater total weight. Beside it, publish:

the existing identified-row fraction;

the fraction of configurations with at least one identified plan;

the headline winner’s identification status.

A practical headline rule is to retain “workload-unmatched: exploratory” if either the balanced yield is below the existing one-half threshold or the displayed winner is unidentified. Scores, eligibility and the fixed owner-authorised routes remain unchanged.

Use one canonical gross-cash definition everywhere. Generate the short Value Multiple definition, route-table tooltip and formula caption from the same definition object. Validate:

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
𝑈
e
l
i
g
i
b
l
e
𝐹
s
u
b
s
c
r
i
p
t
i
o
n
+
𝐹
a
d
d
i
t
i
o
n
a
l
M
observed
	​

=
F
subscription
	​

+F
additional
	​

U
eligible
	​

	​


against the recorded purchase policy and receipts. This is a documentation and consistency improvement to the existing E54/E80/E105 design, not a new capacity assumption.

3. Questions for the owner

Does the selected SemiAnalysis analysis document the effort used for each measured model, independently of AA’s bare-name configuration? If it does, that evidence would resolve M1 for the documented measurements.

Is E61’s one-half threshold intended to describe coverage of purchasable plan rows or coverage of model configurations? If catalogue-weighted coverage is intentional, retain it but name it explicitly; otherwise use the configuration-balanced threshold above.

4. Verdict

VERDICT: HAS FEEDBACK