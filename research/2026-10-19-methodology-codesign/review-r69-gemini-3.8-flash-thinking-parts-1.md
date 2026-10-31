0. Read check

Part 1:

First line: # ValueRank methodology — draft r151

Last 12 words: carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py).

Part 2:

First line: - **Full benchmark set (owner decisions O36, O38)**: a cohort configuration is ranked in a ranking only when it has every leaf of that ranking for the exact configuration, so every row of a ranking is scored on the same benchmarks at that ranking's owner-set weights (O55, as amended for the max-effort ranking by O61).

Last 12 words: on their own subset (the seven Index evaluations), flagged "subset cost" (O17, E254).

Part 3:

First line: - **Cost completeness (E37, as set by O27).** Per row and component the registry stores component identity, the AA field and its aggregation (unit, operator, repetition treatment), required / executed task counts and attempt counts where published, completeness status and reason.

Last 12 words: on the Plan basis the workload question is the M_W identification status.

All three listed parts were read to their end.

1. Findings by severity
Critical

None

High

Finding 1: Disconnection between coding quality and coding cost in the AI Coding Daily ranking (O50, E148, E254).

Issue: Under O50 and E148, FrontierCode cost was bundled into the Coding Agent Index v2.0 unit and eliminated as an independent target component. In the AI Coding Daily ranking, the Coding Agent Index v2.0 is priced for only 3 of 16 rows and remains pending capture. Consequently, the admitted cost basket consists solely of the seven general Artificial Analysis Index evaluations, where coding tasks represent only 354 out of 1,522 tasks (23.3%). Meanwhile, the quality vector for AI Coding Daily allocates 60% of quality to software engineering leaves (FrontierCode 21%, Terminal-Bench 17%, Bug Hunt 12%, AI Coding Daily 10%). Because frontier coding cost is unrepresented in the cost basket, cost variance exhibits an inverted relationship with quality, yielding an extreme value-variance allocation of -96% on the API basis.

Why it hurts the objective: ValueRank aims to measure lowest cost for practical value, specifically balancing software engineering workloads against general capability. When 60% of quality measures coding proficiency but coding agent cost is excluded from the cost basket, the resulting ranking penalizes coding capability and rewards models that happen to be cheap on general office benchmarks.

Concrete change: Amend E148 to add an aggregate decomposition rule: when an aggregate unit (Coding Agent Index v2.0) fails the two-thirds cohort admission threshold in a given ranking, any underlying component with independently published exact cost telemetry (such as FrontierCode 1.1 Main) is admitted as an independent unit for that ranking if it satisfies the admission threshold on its own.

Finding 2: Contradiction in Plan noise-band partitioning across configurations (E248).

Issue: Section 1 states that on the Plan basis a band starting at one of a configuration's plan rows "extends over its other plan rows, because a row between them cannot be told apart from either although their own order is certain (E248)." Two sentences later, the text states that bands are built forward in value order only, "so a configuration's plan rows can fall in more than one band, either because a row of another configuration started the next band between them or because its own rows lie beyond the band's reach from its first row."

Why it hurts the objective: These two statements define mutually incompatible grouping rules. If an intermediate configuration can start a new band between two plan rows of an existing configuration, the first configuration's band does not extend over its other plan rows.

Concrete change: Harmonize E248 by specifying that a band greedily absorbs subsequent plan rows of the same configuration only while no intervening configuration starts a new band and all included rows remain within the separation threshold from the band anchor.

Finding 3: Interleaving subset-workload rows into the unified ordinal headline ranking (Owner decision challenge on O17, E10, E190).

Issue: A row missing an admitted cost component (such as MiMo-V2.6-Pro on the max-effort ranking) is scored on its available subset 
𝑊
𝑆
W
S
	​

 using a separate anchor object with a distinct cost-doubling exchange rate. The draft explicitly notes that "cross-workload ordering not identified" and that "orderings across W and W_S are not identified." Despite this mathematical non-identifiability, the row is placed into the primary ordinal rank ladder (ranks 1 to 9), and rank separability thresholds are computed across adjacent pairs that mix anchor objects.

Why it hurts the objective: Presenting an integrated ordinal ranking where adjacent rows are evaluated on non-commensurate cost scales misleads buyers about relative value.

Concrete change: Display subset-workload rows with an unassigned ordinal rank marker (—) or segregate them into an adjacent subset-workload stratum within the table, rather than giving them an integrated ordinal rank among full-basket rows.

Medium

Finding 4: Conflicting small-panel status specifications for Value-Variance Allocation (E180 vs E189/E196).

Issue: Under E180, the dispersion convention specifies that the value-variance allocation statistic requires at least three rows and is "otherwise withheld (null)." In the subsequent paragraph under E196, the text states that the max-effort ranking's 1-row API subset stratum "reads 'undefined (panel too small)'."

Why it hurts the objective: Discrepancies between literal schema types (null versus string) impair machine validation and downstream parsers reading scores.json.

Concrete change: Standardize the normative definition in E180: specify that the JSON representation in scores.json is null, while the human-readable presentation string is "undefined (panel too small)".

Finding 5: High unrewarded task share in Coding Agent Index v2.0 (O50, E203).

Issue: Coding Agent Index v2.0 contains 290 tasks, of which SWE-Atlas QnA accounts for 124 tasks (42.8%). ValueRank includes no quality leaf for SWE-Atlas QnA, and Artificial Analysis reports only a single pooled cost across the 290 tasks.

Why it hurts the objective: Nearly 43% of the coding agent cost reflects token expenditure on a benchmark that awards zero quality points, penalizing models that run extensive reasoning on SWE-Atlas without crediting their performance.

Concrete change: Add an explicit diagnostic tracking the estimated cost impact of SWE-Atlas QnA or request that Artificial Analysis expose sub-evaluation task costs so SWE-Atlas can be separated if unmeasured on quality.

Low

Finding 6: Double-counting of Terminal-Bench tasks in the max-effort cost basket (O24).

Issue: In the max-effort ranking, Terminal-Bench 4.0 is priced twice: once within Coding Agent Index v2.0 (66 tasks) and once as the stand-alone Artificial Analysis Index run (66 tasks).

Why it hurts the objective: While disclosed under O24, counting the identical benchmark execution twice overweights Terminal-Bench relative to other software engineering tasks in the cost metric.

Concrete change: Formulate a scheduled transition rule under O24 to retire the stand-alone Terminal-Bench cost run once Coding Agent Index v2.0 achieves stable multi-release capture across the cohort.

2. Methodology design recommendations

Implement conditional component decomposition for composite admission units (Priority 1):
When an aggregate unit fails the two-thirds cohort threshold, evaluate its constituent benchmarks against the threshold. If a constituent has verified standalone pricing, admit it under a temporary child workload ID (
𝑊
decomposed
W
decomposed
	​

) until the full aggregate achieves quorum.

Disclose a coding-matched cost sensitivity index alongside 
𝐶
𝑖
,
𝑊
C
i,W
	​

 (Priority 2):
Because general office benchmarks dominate the seven Index evaluations, compute a coding-only cost index 
𝐶
code
=
Terminal-Bench
+
SciCode
C
code
	​

=Terminal-Bench+SciCode (and FrontierCode when admitted). Publish the rank shifts under 
𝐶
code
C
code
	​

 to provide software engineering buyers with an undistorted cost-value view.

Refine Plan noise-band construction grammar (Priority 3):
Adopt a deterministic two-pass algorithm for Plan noise bands: build standard forward value bands across all plan rows; then, if multiple plan rows of a single configuration fall into adjacent bands without any intervening distinct configuration, merge those adjacent bands.

3. Questions for the owner

If Coding Agent Index v2.0 remains below the two-thirds threshold in the AI Coding Daily ranking across upcoming releases, should FrontierCode 1.1 Main be readmitted as a standalone cost admission unit to eliminate the -96% cost-variance inversion?

Should subset-workload configurations (such as MiMo-V2.6-Pro on 
𝑊
𝑆
W
S
	​

) retain ordinal rank integers in the headline table, or should they be assigned a non-ordinal status marker to reflect that cross-workload orderings are unidentifiable?

4. Verdict

VERDICT: HAS FEEDBACK