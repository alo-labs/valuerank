0. Read check

All three listed parts were read to their ends, in order, at commit fe13eb3d27b3cb9f2386f1955752f4052ba7d52e. This review covers only those parts and treats their references to rules elsewhere as defined.

Part 10

First line:

Uncertainty (three separate layers, one scenario engine)

Final sentence:

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

Source: Part 10.

Part 11

First line:

Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress.

Final sentence:

The current ladders are in Output 3 and scores.json barCurrency.

Source: Part 11.

Part 12

First line:

Fewer than two population configurations pin no bar: all three bars, and every output that reads them, are published as unavailable.

Final sentence:

Ranked configurations only (owner decision O43): a family listed under O38 with an indicative value (O41) is not a competitor in any frontier or bar output; each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations.

Source: Part 12.

1. Findings by severity
Critical

None.

High

None.

Medium

None.

Low

S1T’s prescribed output description has not fully inherited its mixed-target interpretation. Issue: Part 10 explicitly characterises S1T as a mixed-target dispersion stress: Bug Hunt uses a single-run dispersion approximation, Vals supplies published standard errors, GDPval-AA supplies an assumed interpretation of a fitted-rating interval, and other leaves use task-count approximations. Part 11’s E155 description nevertheless starts with “published-record leaf values redrawn with task-sampling noise from each leaf’s published task count” and mentions GDPval-AA as the exception. That description does not faithfully identify the Bug Hunt and Vals inputs. Part 10 · Part 11 Why it hurts the objective: Readers of generated outputs could interpret the noise bands as uncertainty of published mean performance, despite the more careful methodological contract explicitly rejecting that interpretation. Concrete change: Generate the short description from the actual target classes present in the stream. For the current design, use:

Mixed-target performance dispersion stress: task-count approximations, published standard errors, an assumed fitted-rating interval interpretation, and Bug Hunt single-run dispersion; independent-task and other registered approximations apply. Not a common confidence interval for published mean performance.

What is new: This is not a request to undo O39, O142, E326 or E330. It is a propagation defect between the adopted interpretation and the separately prescribed output wording.

E226 switches between “cohort rows” and “ranked rows” when explaining why its common-leaf diagnostic is inactive. Issue: E226 selects leaves available for at least 90% of “cohort rows,” but concludes that no leaf is dropped because every “ranked row” has every leaf under O36. Those are not the same population: these parts distinguish listed configurations from ranked configurations and exclude the former from ranking claims. Completeness of ranked rows does not, by itself, establish 90% coverage of cohort rows. Part 12 Why it hurts the objective: A diagnostic intended to reveal availability-driven selection can become tautological if its denominator silently changes to the already complete ranking panel. Conversely, a cohort-wide calculation may legitimately drop a leaf even while every ranked row has it. Concrete change: Declare E226’s denominator explicitly and publish its row IDs and leaf coverage counts. If it is cohort-wide, replace the O36-based explanation with the computed coverage result. If it is ranking-wide, label it a within-ranking completeness diagnostic and distinguish it from O121’s broader common-leaf ranking. What is new: This does not challenge O36, O121 or O172, or request another ranking. It identifies an unresolved population distinction inside E226’s own specification.

2. Methodology design recommendations

Prioritise executable interpretation checks over additional uncertainty machinery. The draft already requires target profiles, allowlists and generated descriptions. Extend those existing objects with a machine-readable set of interpretation classes:

text
reporting_precision
published_estimate_uncertainty
conventional_task_count_approximation
single_run_dispersion
specification_stress

Derive each output description from the classes actually present, rather than maintaining an independent explanatory sentence. A stream containing single_run_dispersion must not receive an unqualified “precision of published estimates” description. This implements finding 1 without new data collection or changes to scores, kernels or owner policy.

Give E226 a reproducible population object. Store:

text
population_rule
population_ids
population_hash
coverage_threshold = 0.90
observed_count_by_leaf
selected_leaf_ids
comparison_panel_ids

For declared population 
𝑃
P, implement:

𝐵
c
o
m
m
o
n
=
{
𝑏
:
∑
𝑖
∈
𝑃
1
[
𝑧
𝑖
𝑏
 observed
]
∣
𝑃
∣
≥
0.90
}
.
B
common
	​

={b:
∣P∣
∑
i∈P
	​

1[z
ib
	​

 observed]
	​

≥0.90}.

Keep the leaf-selection population distinct from the panel on which rank changes are calculated. Add a fixture where every ranked row is complete but sufficiently many listed cohort rows lack one leaf: the diagnostic must follow its declared denominator, not infer inactivity from O36.

These are consistency improvements, not proposals to add weights, change the fixed cohort policy, transfer evidence between variants, or admit marketing quotas as measured consumption. The sectional evidence does not justify another substantive scoring redesign.

3. Questions for the owner

None. The two corrections can be resolved by making the existing interpretation and population contracts internally consistent.

4. Verdict

VERDICT: HAS FEEDBACK