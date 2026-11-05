0. Read check
Part 4

First line: - **Plan cost input (full-utilisation effective cost, labelled)** = API cost input ÷ Value Multiple of the selected route.

Last 12 words: for other Claude models; the transfers keep their assumption label and caution.

Part 5

First line: **Report window (E194, O32, E201a)**: the report window is the closed day interval [V − 30 days, V], compared as UTC calendar dates (date(V) − 30 days ≤ d ≤ date(V), with a timestamped E194 date truncated to its UTC date; reports are recorded by date, not time, so for the report window E213's cutoff is V's UTC date, whole: a report dated that day counts whatever its hour), both end days included, so the window spans 31 calendar dates (a report dated exactly 30 days before the cutoff is in, one dated 31 days before is out), published as the registry's reporting window, which is AGENTS.md's "preceding month".

Last 12 words: (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

Part 6

First line: - **Assumptions**: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, a transfer with its donor measurement identified; neither identifies M_W.

Last 12 words: value; no epsilon is introduced. Domain validity is separate from evidence completeness.

1. Findings by severity
Critical

Contradiction between E130 Coding Agent Index demand multiplier (290) and binding decision O27 (303 tasks)

Issue: Part 6 specifies in E130 (Accounting populations) that Coding Agent Index demand variables are defined as 
𝑑
𝑖
𝐴
=
290
×
compatible pooled category means
d
iA
	​

=290×compatible pooled category means. However, owner decision O27 explicitly establishes that Coding Agent Index cost is computed as AA's documented per-task cost metric 
×
303
×303 tasks.

Why it hurts the objective: Under E157 (Tariff-aware valuation), token demand must reconcile to benchmark cost: 
𝑝
⋅
𝑑
𝑖
𝑒
=
𝐶
𝑖
𝑒
p⋅d
ie
	​

=C
ie
	​

. Scaling category demand by 290 tasks while scaling benchmark cost by 303 tasks produces an inescapable 
∼
4.3
%
∼4.3% structural deficit (
290
/
303
≈
0.957
290/303≈0.957). This causes the demand-reconciliation validator to fail, rendering target-workload transport and price-demand consistency mathematically impossible for any configuration with Coding Agent Index telemetry.

Concrete change: Amend E130 in Part 6 to read: 
𝑑
𝑖
𝐴
=
303
×
compatible pooled category means
d
iA
	​

=303×compatible pooled category means, aligning the demand variable task count directly with O27.

E88 dominance pre-filter omits the plan scope, causing cross-plan elimination that contradicts O48

Issue: In Part 4, E88 defines the dominance pre-filter as: "before the comparator, a route 
𝑏
b is removed when another admissible route 
𝑎
a for the same configuration, workload and valuation basis has an evidence grade at least 
𝑏
b's and identified multiples (point or set) with 
𝐿
𝑎
>
𝑈
𝑏
L
a
	​

>U
b
	​

". It omits restricting the filter to candidates for the same plan.

Why it hurts the objective: Owner decision O48 and Part 6 (E245) mandate ranking "one row per configuration and plan" and evaluating the comparator among "that plan's candidates". If E88 operates across different plans for the same model, an identified higher-tier route with a large Value Multiple (e.g., Claude Max 20x, 
𝑀
≈
57
M≈57) will certifiably dominate and prune the candidate routes of lower tiers (e.g., Claude Pro, 
𝑀
≈
20
M≈20), because 
𝐿
Max20x
>
𝑈
Pro
L
Max20x
	​

>U
Pro
	​

. This strips lower-tier plans of their admissible routes and collapses the multi-plan ranking that O48 instituted.

Concrete change: Amend E88 in Part 4 to state: "before the comparator, a route 
𝑏
b is removed when another admissible route 
𝑎
a for the same configuration, plan, workload and valuation basis has an evidence grade at least 
𝑏
b's and identified multiples (point or set) with 
𝐿
𝑎
>
𝑈
𝑏
L
a
	​

>U
b
	​

".

High

Timestamped partition split format (Anthropic at 2026-10-17T13:00:00Z) clashes with date-only report schema

Issue: In Part 5, the registry split list records Anthropic at 2026-10-17T13:00:00Z alongside calendar-day splits (Anthropic at 2026-10-09, OpenAI at 2026-10-11). In the same section, the draft states: "reports are recorded by date, not time" and "a split given as a date covers that whole day, so a report measured on it, or one whose window spans a split... is excluded".

Why it hurts the objective: Because data/plan_reports.json records reports with calendar dates rather than sub-day timestamps, an evaluation script parsing 2026-10-17T13:00:00Z either fails date-type validation or cannot determine whether a report dated 2026-10-17 occurred before or after 13:00:00 UTC. If the rule "a split given as a date covers that whole day" does not syntactically match an ISO timestamp string, reports on that day could bypass exclusion; conversely, if parsed strictly, the schema inconsistency breaks automated build pipelines.

Concrete change: Normalize the split record in the text and registry to Anthropic at 2026-10-17, or explicitly specify that any timestamped split truncates to its UTC calendar date and excludes all reports dated on that UTC date.

Concordance rule O86 permits arbitrarily wide uninformative reports to pass and distort geometric pooling

Issue: Part 5 defines range-valued concordance under O86 as 
max
⁡
𝑘
𝐿
𝑘
/
min
⁡
𝑘
𝑈
𝑘
≤
1.20
max
k
	​

L
k
	​

/min
k
	​

U
k
	​

≤1.20. This only checks whether the highest lower bound does not exceed 
1.20
×
1.20× the lowest upper bound. It imposes no upper bound constraint on 
max
⁡
𝑘
𝑈
𝑘
max
k
	​

U
k
	​

 or lower bound constraint on 
min
⁡
𝑘
𝐿
𝑘
min
k
	​

L
k
	​

.

Why it hurts the objective: A user report providing an un