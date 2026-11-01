0. Read check

Read all five listed parts to their ends through the GitHub connector, in order, at commit 8cbc853b5cf9f5665ee354d68fae165ab1566856. Parts 3 and 5 begin with an empty line; I preserve that distinction rather than substitute their first non-empty lines.

Part	First line	Last 12 words
1	# ValueRank methodology — draft r165	configurations; applying O145 moved the release cutoff (O65) and re-captured every source.
2	- **Two rankings (owner decisions O52, O53, O54)**: ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52).	a leaf after the search is listed, not ranked (O36).
3	[empty line]	the Plan basis the workload question is the M_W identification status.
4	- **Plan cost input (full-utilisation effective cost, labelled)** = API cost input ÷ Value Multiple of the selected route. Computed per model–plan **tier**–surface–configuration route (tier and fee are part of route identity and published).	transfers keep their assumption label and caution.
5	[empty line]	identify M_W. A schema change moves the route to the possibly-superseded stage.

Correction to the requested read-check extraction: the connector returned the full text, but the exact twelve-word tails for parts 2–4 are as follows:

Part 2: missing a leaf after the search is listed, not ranked (O36).

Part 3: on the Plan basis the workload question is the M_W identification status.

Part 4: models; the transfers keep their assumption label and caution.

The findings below concern only these five parts. References identify the part and named subsection; the connector did not supply citation IDs.

1. Findings by severity
Critical

None.

High

None.

Medium

The release’s stated Plan-research execution does not demonstrate compliance with O75’s “every release” requirement. Issue: Part 5, “Plan-allowance research,” states that O75 requires all three research stages “every release … over every cell.” It then identifies the last complete all-provider search as 2026-10-25 and the subsequent 2026-10-31 search as supplementary coverage for two entrants. The current release cutoff is 2026-11-01. The separate seven-day freshness test establishes that the older search is recent enough; it does not establish that this release ran the required procedure. Why it hurts the objective: Plan-route selection depends on finding replacement evidence after limit and price changes. The draft describes several such changes, including the 2026-10-30 Claude change. A recent historical search and an entrant-only supplement do not establish that the existing model–plan cells were searched after those developments. This is an execution-contract inconsistency, not a proposal to change the already-adopted search design. Concrete change: Bind O75 coverage to a release-specific research-run ID. For every required model–plan cell, require records for the three stages associated with that release. Keep the seven-day rule as a separate freshness condition. If O75 actually permits reusing a prior release’s search, that needs an explicit owner amendment—not an interpretation inferred from E218. New argument relative to the ledger: E278 already addresses missing entrant coverage. This finding concerns reuse of earlier research for existing cells despite the distinct “every release” requirement.
Source: Part 5, “Plan-allowance research,” “Research coverage is keyed by model and plan,” and “Search age.”

Low

The current missing-evidence explanation contradicts the ledger’s adopted MiMo–Vals matching decision. Issue: Part 2 says that MiMo-V2.6-Flash’s Vals records state no reasoning setting and “both stay unmatched to its thinking-enabled configuration, O140.” The supplied ledger says O149 subsequently matches MiMo-V2.6-Flash on Vals. The passage presents the older outcome as current rather than historical. Why it hurts the objective: Readers cannot tell whether a missing leaf reflects an actual evidence gap or stale matching prose. Even if the configuration remains excluded because Bug Hunt is missing, its published coverage explanation should not misstate which other leaves are available. Concrete change: Replace the superseded Vals statement with the current O149 disposition, identifying the Vals leaves it covers and its registered matching basis. Keep the Bug Hunt mismatch separate. Generate the prose from the same configuration–leaf matching records used for the missing-leaf list. New argument relative to the ledger: This does not reopen O140 or O149. It identifies a current explanatory paragraph that still reports the superseded outcome.
Source: Part 2, “Indicative value for a listed family,” compared with O149 in the supplied decision ledger.

2. Methodology design recommendations

Prioritise a release-scoped Plan-research compliance object. Implement the Medium finding using a public manifest such as:

text
release_id
research_run_id
required_cells[]
cell:
    canonical_model_id
    canonical_plan_id
    stage_1_record
    stage_2_record
    stage_3_record
    searched_through
    unreachable_sources[]

Define the execution gate separately from freshness:

ResearchComplete
⁡
(
𝑟
)
=
⋀
𝑐
∈
𝐶
𝑟
⋀
𝑠
∈
{
1
,
2
,
3
}
RecordedForRelease
⁡
(
𝑟
,
𝑐
,
𝑠
)
.
ResearchComplete(r)=
c∈C
r
	​

⋀
	​

s∈{1,2,3}
⋀
	​

RecordedForRelease(r,c,s).

Then apply E218’s existing age check independently. Supplementary research may fill required cells, but should not silently make an older all-provider run a new release’s run. This requires only the research records the draft already says it publishes; it adds no private-data dependency.

Generate current matching explanations from the evidence map. Extend the existing build-generated current-figure discipline to matching dispositions:

text
configuration_id
leaf_id
disposition: matched | unmatched | missing
governing_decision
source_record_id
mismatch_reason
superseded_decision

The rendered missing-evidence paragraph should use only the active disposition. Historical decisions can remain in the ledger, but should not be rendered as current coverage outcomes. Add a regression fixture for MiMo-V2.6-Flash: Vals follows O149, while Bug Hunt retains its separately governed disposition. This is an implementation repair, not a recommendation to loosen exact-variant evidence or transfer scores between efforts.

I recommend no change to the fixed cohort rule, headline weights, full-utilisation policy, or numerator-admission policy on the evidence in these sections.

3. Questions for the owner

Does O75 require a newly executed three-stage search for every required cell on every release, or may a previous release’s completed search be reused while it remains within seven days? The answer determines whether the current release needs additional research execution or an explicit policy amendment.

4. Verdict

The reviewed sections clearly distinguish displayed Plan arithmetic from supported claims, preserve exact-configuration quality evidence, and disclose the limitations of subset workloads. The remaining material concern is whether the release’s documented research execution satisfies its own binding refresh requirement; the MiMo–Vals passage also needs a current-state correction.

VERDICT: HAS FEEDBACK