0. Read check

Read both listed parts to their ends through the GitHub connector, at commit 8e532e4891e1759c825d0fed89e1ae32fbc9eea1. This review covers only those parts; rules they cite elsewhere are treated as defined, not missing.

Part 1

First line:

ValueRank methodology — draft r166

Last 12 words:

applying O145 moved the release cutoff (O65) and re-captured every source.

Part 2

First line:

Two rankings (owner decisions O52, O53, O54): ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52). No benchmark outside AA covers the cohort at exact effort (research/2026-10-23-swe-benchmarks/reports/SWE benchmark candidates.md), so ValueRank publishes two rankings, each over the cohort configurations that have its complete leaf set (Quality): the max-effort ranking (no rule limits it to one effort per family; it holds one configuration per family at the vendor's top effort only because LiveBench 2.0 and Vals run each model once, at its top effort, O54; today 9 configurations from 9 of the 15 cohort families, plotted and retained), which leads on the site and in the README (O54), and the AI Coding Daily ranking (mostly high and medium efforts; today 20). Configurations in both rankings today: 4 (DeepSeek V4.1 Flash 1017 (max), GPT-6 Luna (max), Gemini 4 Argon (high) and MiMo-V2.6-Pro), so 25 of the 37 are ranked at least once. Each ranking has its own leaf table and weights (O55), frozen anchors, quality bars, scenario run, basket admission and diagnostics, scored by the same engine (E253, E254); values compare within a ranking only. Common-leaf diagnostic ranking (owner decision O121, 2026-10-29): because the two leading rankings cannot rank the cheaper efforts that LiveBench, Vals and AI Coding Daily never run, a third ranking scores every cohort configuration with AA's leaves and Bug Hunt, at any effort, on the ten leaves the leading rankings share, at the weights O121 set for its ten leaves, O55's before O61's amendment (FrontierCode 25, Terminal-Bench 20, Bug Hunt 15 and the seven leaves outside software engineering). Today it ranks 33 configurations, 8 of them ranked in neither leading ranking: Claude Haiku 5.5 (low), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh) and GPT-6.1 Terra (low). It has its own frozen anchors, quality bars, basket admission and scenario run, but it is diagnostic: it earns no interval or scenario label, its gates are disclosed but never hold the release, a configuration ranked only there stays listed (not ranked) in ValueRank, and a model page never makes it its home. For each bar position and basis it publishes its displayed-record cheapest row beside each leading ranking's answer at the same position (each ranking's bar levels are its own), with whether they differ (scores.json v3Tracks.common.leadingComparison). Admission per ranking (owner decision O57, implementing E254): O15 and E140 admit a component when its exact cost covers two-thirds of "the cohort"; with two rankings this is two-thirds of the ranking's own cohort rows, because each ranking is scored on its own rows and anchors. The choice changes the result: today the Coding Agent Index v2.0 is priced for 8 of the max-effort ranking's 9 rows, so it is admitted there, while under a whole-cohort reading it would have stayed pending (the counts at the decision are in the ledger, O57). Per-ranking full set (E255): a cohort configuration is ranked in every ranking whose full set it has, and it is excluded from ValueRank, listed under O38 with its searches, only when it lacks both leading rankings' sets (the common-leaf diagnostic ranking may still rank it; today 12: Claude Haiku 5.5 (low), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (low), GPT-6 Astra (xhigh), GPT-6 Luna (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (low), Gemini 4 Carbon (high), MiMo-V2.6-Flash and MiniMax-M3.1-Flash (max)). Each ranking also lists the cohort configurations without its own set, with their missing leaves (today 28 beside the max-effort ranking and 17 beside the AI Coding Daily ranking). Every missing (configuration, added leaf) pair carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py).

Last 12 words:

after the search is listed, not ranked (O36).

Correction to the requested word count: that ending contains only eight whitespace-separated words. The last 12 words are:

configuration missing a leaf after the search is listed, not ranked (O36).

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low
L1. E234’s cross-source adjustment needs an explicit sign convention

Issue: Part 2’s “Bar results without the fills” specifies a sensitivity with each third-party fill “lowered by its leaf’s measured cross-source mean offset.” The same section reports Cognition’s mean offset against AA as −1.5 points. “Lowered by” a signed negative offset is ambiguous: subtracting −1.5 raises the fill, whereas lowering it by the offset’s magnitude reduces it. These are different sensitivity experiments. Source: part 2, “Gap-fill checks (E234)” and “Bar results without the fills (E234, extended).”

Why it hurts the objective: This diagnostic is meant to show whether cross-source measurement differences change the cheapest-above-bar answer. An ambiguous adjustment direction makes that answer implementation-dependent. The draft reports no current gap fills, so this is a prospective reproducibility defect rather than evidence of an incorrect current ranking.

Concrete change: Define the offset and transformation algebraically. Distinguish a signed AA-scale correction from a conservative downward stress; do not describe both as “lowered by the mean offset.”

What is new relative to the ledger: This does not repeat the adopted request for a cross-source check or removal sensitivity. It identifies a sign ambiguity in the stated transformation, exposed by the currently reported negative offset.

L2. E240’s description of the search population still equates cohort membership with current plotted membership

Issue: Part 2’s “Open-web discovery (E240)” says, parenthetically, “every cohort configuration is plotted on or near the frontier, O51.” Part 1’s O145 amendment explicitly adds configurations no longer plotted on or near the frontier, and part 2 elsewhere correctly says retained rows are “ranked, searched and listed like any other.” The intended rule is recoverable, but the local description is false under the current cohort definition. Source: part 1, “Cohort and configuration,” O145; part 2, E240 and “Frontier-families population.”

Why it hurts the objective: The open-web search is the safeguard against incorrectly treating exact-configuration evidence as missing. Its population should be unambiguous, especially for retained configurations whose evidence can determine whether they remain in a leading ranking. I am not claiming the build currently omits these searches; this is a specification inconsistency.

Concrete change: Replace the parenthetical with “every cohort configuration, whether currently plotted or retained under O145.” Make the E240 check explicitly range over every listed cohort configuration missing a required leaf, independent of inclusion route.

What is new relative to the ledger: O145’s retention policy is already adopted. This finding concerns a surviving pre-retention universal statement in the search specification, not a proposal to change retention.

2. Methodology design recommendations
Priority 1 — Make the existing cross-source sensitivity executable without interpreting prose

For leaf 
𝑏
b, define the common exact-configuration comparison panel 
𝑃
𝑏
P
b
	​

 and the signed offset:

Δ
𝑏
=
1
∣
𝑃
𝑏
∣
∑
𝑗
∈
𝑃
𝑏
(
𝑧
𝑗
𝑏
t
h
i
r
d
−
𝑧
𝑗
𝑏
A
A
)
.
Δ
b
	​

=
∣P
b
	​

∣
1
	​

j∈P
b
	​

∑
	​

(z
jb
third
	​

−z
jb
AA
	​

).

Then choose and name the intended diagnostic:

AA-scale alignment:

𝑧
𝑖
𝑏
a
l
i
g
n
e
d
=
𝑧
𝑖
𝑏
t
h
i
r
d
−
Δ
𝑏
.
z
ib
aligned
	​

=z
ib
third
	​

−Δ
b
	​

.

A negative offset raises the third-party score toward AA’s observed scale.

Downward-offset stress:

𝑧
𝑖
𝑏
d
o
w
n
=
𝑧
𝑖
𝑏
t
h
i
r
d
−
∣
Δ
𝑏
∣
.
z
ib
down
	​

=z
ib
third
	​

−∣Δ
b
	​

∣.

This always lowers the score, but it is a stress test, not a signed bias correction.

Apply the leaf’s registered domain after the transformation, recompute quality with the ranking’s existing weights, and retain the frozen bars. Publish the chosen transformation name, panel IDs, offset and resulting cheapest-row changes.

This uses the exact-model-and-effort public comparison data already required by E234/O153. It needs no additional benchmark, imputation, provider quota or owner-weight change. The reviewed section already supplies the necessary comparison machinery; the recommendation resolves only its transformation semantics.

Priority 2 — Express search coverage as a set invariant over the amended cohort

Let:

𝐶
𝑡
=
𝑃
𝑡
∪
𝑇
𝑡
C
t
	​

=P
t
	​

∪T
t
	​

: current cohort, consisting of currently plotted configurations and O145-retained configurations;

𝐿
𝑟
L
r
	​

: the required leaf set for ranking 
𝑟
r;

𝐴
𝑖
𝑟
A
ir
	​

: leaves with admitted exact-configuration evidence for configuration 
𝑖
i in ranking 
𝑟
r.

Require the logged missing-evidence search population to cover:

𝐺
𝑡
=
⋃
𝑟
{
(
𝑖
,
𝑏
)
:
𝑖
∈
𝐶
𝑡
,
  
𝑏
∈
𝐿
𝑟
∖
𝐴
𝑖
𝑟
}
.
G
t
	​

=
r
⋃
	​

{(i,b):i∈C
t
	​

,b∈L
r
	​

∖A
ir
	​

}.

For every pair in 
𝐺
𝑡
G
t
	​

, require the existing registered-source search, open-web discovery record, candidate resolution and applicable recency check. A single search artifact can satisfy several rankings where the configuration, leaf and relevant search conditions are identical.

This formalizes the existing O145/E240 intent rather than adding a research stage. In the public output, report search coverage separately for plotted and retained configurations, so a future cohort amendment cannot silently change the operational search population.

3. Questions for the owner

None. Both findings can be resolved as specification clarifications without reopening the binding policy decisions.

4. Verdict

VERDICT: HAS FEEDBACK