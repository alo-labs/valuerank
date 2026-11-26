0. Read check

Both listed parts were read through their ends at commit 5917e61757433bf61ca45bbb5cb030200bb8f863.

draft-r172-part-1-of-14.md

First line: # ValueRank methodology — draft r172

Last 12 words: configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

draft-r172-part-2-of-14.md

First line:

Two rankings (owner decisions O52, O53, O54): ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52). No benchmark outside AA covers the cohort at exact effort (research/2026-10-23-swe-benchmarks/reports/SWE benchmark candidates.md), so ValueRank publishes two rankings, each over the cohort configurations that have its complete leaf set (Quality): the max-effort ranking (no rule limits it to one effort per family; it holds one configuration per family at the vendor's top effort only because LiveBench 2.0 and Vals run each model once, at its top effort, O54; today 9 configurations from 9 of the 15 cohort families, plotted and retained), which leads on the site and in the README (O54), and the AI Coding Daily ranking (mostly high and medium efforts; today 20). Configurations in both rankings today: 4 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Luna (max), Gemini 4 Argon (high) and MiMo-V2.6-Pro), so 25 of the 37 are ranked at least once. Each ranking has its own leaf table and weights (O55), frozen anchors, quality bars, scenario run, basket admission and diagnostics, scored by the same engine (E253, E254); values compare within a ranking only.

Last 12 words: configuration missing a leaf after the search is listed, not ranked (O36).

Scope: the findings below concern only these two parts. Rules attributed to later sections are treated as defined there, not missing.

1. Findings by severity
Critical

None.

High

None.

Medium

The retention diagnostic overstates the counterfactual it implements. Issue: Part 2, “Frontier-families population,” says that rebuilding anchors and bars without retained rows shows “what the ranking would read without the retained rows.” But the same part makes basket admission depend on the ranking’s own row population, with threshold 
⌈
2
𝑁
/
3
⌉
⌈2N/3⌉. Removing retained rows can therefore change component admission, workload membership and the eligible reference panel—not merely the anchors and quality-bar population. Why it hurts the objective: A reader could attribute a change in the cheapest-above-bar answer solely to temporary retention when the published diagnostic holds a retention-dependent workload fixed. This matters because the objective is a cost–value comparison, and changing the admitted cost workload can change the comparison itself. Concrete change: Describe the existing output as a “retained-row removal diagnostic, conditional on the published workload and component admissions.” Remove the unrestricted claim that it reproduces the ranking without retention. If a full counterfactual is desired, separately rerun admission, workload construction, reference eligibility, anchors and bars after removing retained rows. New relative to the ledger: This does not challenge O145 or repeat the adopted requirement to exclude retained rows from frontier-family diagnostics. It identifies an interaction between that diagnostic and O57’s endogenous admission denominator.

Low

The common-leaf bar comparison needs a clearer interpretation of differing answers. Issue: Part 2 compares the common-leaf diagnostic’s cheapest row with each leading ranking’s answer “at the same position,” while explicitly acknowledging that each ranking has its own bar level. The quality formulas also differ. Consequently, a differing answer combines changes in benchmark composition, eligibility, bar construction and potentially cost-workload admission. Why it hurts the objective: The comparison is useful as an alternative specification, but it cannot isolate whether broader configuration coverage exposes a cheaper substitute. A simple “answers differ” indicator risks inviting that interpretation. Concrete change: Label it “alternative-ranking answer comparison—not a coverage effect.” Beside each comparison, print both bar levels, quality-formula IDs, workload hashes and eligible configuration counts. Do not compare raw quality-point levels across the different formulas as though they were the same threshold. New relative to the ledger: O121 already establishes this diagnostic and its same-position comparison. The additional point is attribution: its differences should not be presented as evidence about coverage alone.

2. Methodology design recommendations

Make the retention diagnostic explicitly conditional. Keep the present calculation, but attach a machine-readable counterfactual contract:

text
removed_population: retained configurations
recomputed: reference selection, anchors, quality bars, displayed answers
held_fixed: benchmark definitions, weights, component admissions, cost observations
interpretation: population/reference sensitivity conditional on published workload

Include only calculations actually recomputed. This is a small, implementable correction requiring no new external data. A separate full-pipeline diagnostic could use:

𝑅
−
=
𝑅
∖
𝑅
r
e
t
a
i
n
e
d
,
𝑡
−
=
⌈
2
∣
𝑅
−
∣
3
⌉
,
R
−
=R∖R
retained
	​

,t
−
=⌈
3
2∣R
−
∣
	​

⌉,

followed by the existing admission and workload rules applied to 
𝑅
−
R
−
. Publish admitted-component additions/removals before reporting changed answers. Keep it diagnostic, with no release hold or change to official scores.

Separate alternative-specification comparisons from coverage comparisons. Preserve O121’s existing output. Add an explicit attribution status rather than implying a causal decomposition:

text
comparison_type: alternative specification
changed_dimensions:
  - quality formula
  - eligible configurations
  - frozen bar
  - admitted workload, when different
coverage_effect_identified: false

If a coverage-only diagnostic is later needed, use the common-leaf specification throughout: one common-leaf quality formula, one frozen common-leaf bar, one admitted workload and one anchor object. Compare the cheapest qualifying row over:

configurations eligible for a selected leading ranking; and

all configurations eligible for the common-leaf diagnostic.

This isolates the effect of expanding the candidate set under that diagnostic specification. It does not establish that excluded configurations would qualify under the leading ranking’s unavailable benchmark results, and should say so. Where the common workload lacks exact cost evidence, report the comparison as unevaluable rather than substitute a different workload.

Neither recommendation changes the fixed cohort policy, exact-variant requirements, official weights, Plan evidence rules or the primacy of the leading rankings.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK