0. Read check

Read all five listed parts to their ends, in order, at commit d3a478e2d45071810c58271131a7bb67b5d61955. Parts 3 and 5 begin with a blank line; I distinguish that literal first line from their first nonblank line below.

Part	First line	Last 12 whitespace-delimited words
1	# ValueRank methodology — draft r171	configurations; applying O145 moved the release cutoff (O65) and re-captured every source.
2	- **Two rankings (owner decisions O52, O53, O54)**: ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52).	configuration missing a leaf after the search is listed, not ranked (O36).
3	Empty line. First nonblank line: ## Cost (25% of the value score)	cost per task, not AA's 7:2:1 blended price, not total Index cost.
4	- **Matched-cost diagnostic (diagnostic only).** C_i^match = Σ_{g∈G} ω_g P_ig over canonical **execution families** g (E55; e.g. FrontierCode, Terminal-Bench as executed by AA): quality-weighted **complete benchmark passes** (E24), with P_ig = cost of one complete deployment-equivalent pass of family g for configuration i (Σ of its accounting subcomponents; published task count × mean cost per attempted task) and frozen diagnostic weights ω_g (Σ ω_g = 1, from the quality weights of the leaves that reference g, fixed with the panel before ranks are examined); a quality leaf references exactly one execution family; model API token charges only (input, cache read/write, reasoning, output × the primary price list; sandbox, environment-setup and verifier compute excluded; E17); where a source cannot separate retry or harness tokens the leaf is not priced for that row; tbench.ai cost columns are never joined.	for other Claude models; the transfers keep their assumption label and caution.
5	Empty line. First nonblank line: **Report window (E194, O32, E201a)**: the report window is the closed day interval [V − 30 days, V], and for each model × plan cell it ends instead at that cell's latest staged search, so it never claims days nobody searched (owner decision O161, on reviewer 79; a report dated after it is excluded as "dated after the cell's latest staged search", and each cell publishes the date as searchedThrough); compared as UTC calendar dates (date(V) − 30 days ≤ d ≤ date(V), with a timestamped E194 date truncated to its UTC date; reports are recorded by date, not time, so for the report window E213's cutoff is V's UTC date, whole: a report dated that day counts whatever its hour), both end days included, so the window spans 31 calendar dates (a report dated exactly 30 days before the cutoff is in, one dated 31 days before is out), published as the registry's reporting window, which is AGENTS.md's "preceding month".	is diagnostic; a transfer from a lapsed report donor, which is diagnostic.

The review below concerns only these five parts. Cross-referenced rules are treated as defined, not as missing. Source locations: part 1, part 2, part 3, part 4, part 5.

1. Findings by severity
Critical

None.

High

None.

Medium

Noise-band membership has conflicting operational descriptions, including an exception that the subsequent qualification appears to withdraw. Issue: Part 1 first says a configuration’s Plan rows are “kept together even when they span more than the threshold” and that a band “extends forward over its other plan rows.” It then says another configuration can start a new band between them, and that the same configuration’s own rows can lie beyond the band’s reach. It expressly reports configurations appearing in multiple bands. These statements do not specify one unambiguous membership algorithm: does configuration identity override the first-row threshold, or not? Why it hurts the objective: These bands are the reader-facing qualification of ordinal value ranks. A band can otherwise appear to mean statistical inseparability while actually encoding a plan-grouping convention. Reproduction of scores does not resolve which interpretation readers should use. Concrete change: Keep statistical band assignment and configuration grouping separate. Define membership solely against the current band’s first row, using the stated pair-specific threshold and shared-quality covariance for same-configuration Plan rows. Show configuration grouping through an identifier or visual connector, not through membership exceptions. Publish a fixture with interleaved Plan rows and widely separated plans of one configuration. What is new relative to O42/E248/E277: This is not a renewed objection to retaining ranks or using noise bands. It identifies contradictory membership instructions in the current wording, including the claimed same-configuration exception and the later admission that it does not keep those rows together. Part 1, “Noise band”.

The monthly research rule states both a minimum research obligation and a maximum frequency, which diverge at calendar boundaries. Issue: Part 5 describes O164 as running the three stages “at most once per calendar month unless” a triggering change occurs. Separately, O167 requires an all-provider three-stage search no more than 31 days old. A maximum frequency is not a requirement to search monthly, and it can conflict with the age gate: a search early in a long month followed by one late in the next month satisfies “once per calendar month” scheduling but can exceed 31 days; conversely, repairing an age failure may require another search in a calendar month without a registered change. Why it hurts the objective: Routine refreshability depends on a scheduler that can always satisfy its release gates. These instructions leave an unnecessary choice between holding a release and violating the stated frequency limit. Concrete change: State that every cell requires a three-stage search at least once in each rolling 31-day interval, with earlier mandatory searches on the existing triggers. If the owner intends a workload-saving calendar-month reuse rule, make it permission to reuse evidence only while the 31-day gate remains satisfied—not a prohibition on additional research. What is new relative to O164/O167: The issue is the interaction between the literal “at most” rule and the later rolling-age gate, not a request to restore three-stage research every release. Part 5, research cadence and two research clocks.

Low

The current two-ranking agreement population is internally inconsistent. Issue: Part 2 explicitly identifies four configurations shared by the leading rankings. The supplied decision ledger describes E288 as computing the two-ranking Kendall agreement from eight shared configurations. That discrepancy is material to the diagnostic’s interpretation, even though the four-row intersection could legitimately reflect a later cohort change. Why it hurts the objective: Agreement between rankings is meaningful only for a named common population. A reader cannot tell whether the statistic uses current shared rows, a historical panel, or a different matching unit. Concrete change: Generate the agreement panel, its count, and its named members from the same current configuration-ID intersection used by the ranking-overlap statement. If E288 intentionally uses a historical panel, label that panel and its date explicitly and stop describing it as the current shared configurations. What is new: This is a population-reconciliation issue, not a request to add the already-adopted agreement diagnostic. Part 2, “Two rankings”.

2. Methodology design recommendations

Make the band algorithm executable without prose exceptions. For rows ordered by displayed value within a workload, let 
𝑓
f be the first row of the current band. Admit row 
𝑗
j only when

∣
𝑉
𝑗
−
𝑉
𝑓
∣
≤
1.96
𝜎
𝑗
2
+
𝜎
𝑓
2
−
2
Cov
⁡
(
𝑉
𝑗
,
𝑉
𝑓
)
.
∣V
j
	​

−V
f
	​

∣≤1.96
σ
j
2
	​

+σ
f
2
	​

−2Cov(V
j
	​

,V
f
	​

)
	​

.

Use the existing independent-task approximation for different configurations. For two plans of the same configuration, their benchmark-quality contribution is shared exactly; benchmark noise therefore supplies no uncertainty to their value difference. Keep the draft’s warning that these bands exclude cost, harness and assumption uncertainty. Do not imply that the resulting bands are equivalence classes: adjacent bands can still contain inseparable pairs, as the draft already acknowledges. This preserves the adopted uncertainty scope and ordinal ranking while eliminating the configuration-membership exception. If changing E248 requires owner approval, the minimum editorial repair is to publish the actual implemented pseudocode and make every preceding description agree with it. Part 1.

Express research scheduling as deadlines rather than calendar-month frequency. For each model–plan cell, publish:

threeStageDue: the last qualifying three-stage search date plus 31 days.

triggeredResearchRequired: whether a registered change, entrant or new plan requires earlier research.

freshnessDue: the last all-provider search or freshness-check date plus seven days.

searchedThrough: unchanged by freshness checks, as already required.

A release passes only if its cutoff meets both deadlines and all triggered research is complete. Additional searches remain permissible. This uses the existing public research logs and preserves the separation between discovery and change monitoring. Part 5.

Give every cross-ranking comparison one generated population object. Define

𝐼
=
𝑅
max-effort
∩
𝑅
AI Coding Daily
I=R
max-effort
	​

∩R
AI Coding Daily
	​


by exact configuration ID, then emit its members, count, matching rule and both rankings’ workload IDs beside the agreement diagnostic. Assert that its count equals the overlap count printed in the cohort narrative. Preserve the existing warning that the rankings’ scores and bar levels are not directly comparable; a shared-panel ordering diagnostic does not erase their different leaf sets or cost workloads. Part 2.

No weight changes, new benchmark requirements, imputed evidence, or provider-marketing allowance numerators are recommended in this sectional pass.

3. Questions for the owner

None.

4. Verdict

The reviewed sections already distinguish displayed Plan arithmetic from supported claims, retain exact-configuration evidence requirements, and disclose the limitations of subset workloads. The remaining feedback concerns deterministic interpretation and refresh scheduling, not reopening those adopted policies.

VERDICT: HAS FEEDBACK