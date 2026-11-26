0. Read check

Read all three listed parts to their ends at commit dd5e4a17a6dbdbbbeb61b45f926213e2966f3642. The quotations below refer to the file contents, excluding the connector’s download-status message.

Part 1 — draft-r187-part-1-of-16.md

First line:

ValueRank methodology — draft r187

Final sentence:

A change of AA chart or field is a versioned methodology migration, never a silent refresh.

Part 2 — draft-r187-part-2-of-16.md

First line: empty.

First non-empty line:

Cohort and configuration (fixed policy)

Final sentence:

Today the excluded configurations (O38: neither ranking's set) are frontier-family primaries Claude Opus 5.5 (xhigh), GPT-6 Astra (xhigh), Gemini 4 Carbon (high) and MiMo-V2.6-Flash; near-family primaries none; frontier families' near points none; non-primary points on the rendered frontier Claude Haiku 5.5 (low), GPT-6 Luna (low), GPT-6.1 Sol (xhigh) and GPT-6.1 Terra (low); near families' other near points none; and configurations retained one release under O145 Claude Haiku 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (low) and MiniMax-M3.1-Flash (max) (six classes that partition the excluded set; the build checks it); a family with an excluded primary may have other efforts ranked.

Part 3 — draft-r187-part-3-of-16.md

First line:

Configuration rule (E188, amended by E193 and E251): a family is AA's model identity, the plotted model name without its effort and fallback qualifiers; it must equal the selected catalog model's display name, and MiMo-V2.6-Pro and MiMo-V2.6-Flash are separate families.

Final sentence:

Both priced executions stay in the basket as the owner listed them; the overlap is disclosed.

Scope: this review covers only these three files. References below identify their sections directly; the connector returned no citation identifiers.

1. Findings by severity
Critical

None.

High

None.

Medium

Owner decision challenge — keeping subset-workload rows ranked does not require assigning them a cross-workload ordinal position.

Issue: The draft expressly says subset-workload rows use different anchor objects, excludes cross-workload pairs from separability calculations, and permits whole-table dispersion only under the label “displayed-table dispersion.” Nevertheless, the headline gives these rows ordinal positions among main-workload rows. Today this affects MiMo-V2.6-Pro in the max-effort ranking: its cost excludes the admitted Coding Agent Index component, while the other eight configurations’ main workload includes it.
Source: part 1, “Rank separability,” “Noise band,” and “Dispersion convention”; part 3, “Capture status.”

Why it hurts the objective: An ordinal position communicates an ordering even where the accompanying methodology declines to compare the rows’ uncertainty because their workload and anchor objects differ. That is a stronger problem than uncertainty about an otherwise common estimand: the displayed positions order different cost experiments.

What is new relative to the ledger: This is not a request to remove subset rows, withhold their scores, impute their missing costs, or reverse O17/O117. The new argument is that the existing workload restrictions on uncertainty and dispersion should also govern the presentation of ordinal position. “Stays ranked” can mean ranked within its evidenced workload, without creating a total ordering across workloads.

Concrete change: Keep every subset row scored and visible in the same headline table, but assign ranks within workload strata. Publish workloadId, anchorObjectId, and rankWithinWorkload; show “subset workload—no cross-workload rank” in place of a global ordinal position. If the owner requires a global ordinal column, label it “mixed-workload display order,” not an unqualified value rank.

Low

“Cohort row” has a local definition that conflicts with its use in the configuration rule.

Issue: Part 2’s “Counts, defined once” defines a cohort row of a ranking as a configuration ranked in that ranking and says the broader cohort configurations are never called rows of a ranking. Part 3 then says every plotted on/near configuration “is a cohort row, ranked in every ranking whose full set it has.” Some such configurations have neither ranking’s complete set.
Source: part 2, “Counts, defined once”; part 3, “Configuration rule.”

Why it hurts the objective: The distinction controls an operational denominator: component admission uses the ranking’s cohort-row count. An implementer reading the configuration rule independently could count the broader plotted cohort rather than the eligible configurations in the ranking.

Concrete change: Replace the part 3 sentence with:

Every plotted on/near configuration is a cohort configuration. It is a cohort row of each ranking whose full benchmark set it has.

Apply the same terminology to “cohort row” in part 2’s one-release-retention paragraph: use “cohort configuration” before ranking eligibility is established. This is a wording repair, not a proposed change to membership or admission policy.

2. Methodology design recommendations
Priority 1 — Make workload identity part of the ranking key

Implement the medium finding with a typed ranking object:

RankKey
⁡
=
(
ranking
,
 basis
,
 workloadId
,
 anchorObjectId
)
.
RankKey=(ranking, basis, workloadId, anchorObjectId).

Within each key, sort by the existing value score:

𝑉
𝑖
=
0.25
𝑆
𝐶
,
𝑖
+
0.75
𝑄
𝑖
.
V
i
	​

=0.25S
C,i
	​

+0.75Q
i
	​

.

This changes neither weights nor evidence rules. It requires no new public data: the draft already identifies workloads, anchor objects and subset rows.

For the headline:

Present the main-workload ranking first.

Keep subset-workload rows immediately below it in the same table, with their own rank or “only evidenced row” status.

Preserve their scores, missing-component flags and identical-subset comparisons.

Do not interpret positions across strata as pairwise value comparisons.

Add a regression test: a row with a different workloadId must never enter another stratum’s ordinal ranking. This extends the separation already required for noise bands and adjacent-rank separability.
Source basis: part 1, “Rank separability” and “Noise band”; part 3, “Capture status.”

Priority 2 — Give the population vocabulary distinct machine-readable names

Retain the draft’s existing populations but eliminate the overloaded word “row” before ranking admission:

Object	Meaning
cohortConfigurationIds	All plotted or retained cohort configurations
rankedConfigurationIds[ranking]	Configurations with that ranking’s full leaf set
scoredConfigurationIds[ranking]	Ranked configurations with a value score
mainWorkloadConfigurationIds[ranking]	Configurations on the main workload and its anchor object
planRowIds[ranking]	Configuration–plan records

Compute component-admission denominators directly from rankedConfigurationIds[ranking], not from a separately maintained count:

𝑛
a
d
m
i
t
,
𝑟
=
⌈
2
 
∣
rankedConfigurationIds
[
𝑟
]
∣
3
⌉
.
n
admit,r
	​

=⌈
3
2∣rankedConfigurationIds[r]∣
	​

⌉.

The formula already follows O57; the recommendation is to make the naming and derivation prevent the prose conflict from becoming an implementation ambiguity. Add a documentation check that flags unqualified “cohort row” outside a ranking-specific context.
Source basis: part 2, “Admission per ranking” and “Counts, defined once.”

I recommend no changes to the fixed cohort rule, exact-variant evidence policy, Value Multiple numerator rules, or the owner-set weights on the evidence in these three parts. The draft already discloses the principal limitations surrounding Plan identification, benchmark-noise interpretation, agent-cost boundaries and incomplete coverage; I have not relisted those adopted decisions as fresh findings.

3. Questions for the owner

Does O117’s requirement that subset rows “stay ranked” require a global ordinal position across different workload and anchor objects, or would within-workload ranks in the same headline table satisfy it? The answer determines whether Priority 1 is a presentation clarification or requires an owner-policy amendment.

4. Verdict

VERDICT: HAS FEEDBACK