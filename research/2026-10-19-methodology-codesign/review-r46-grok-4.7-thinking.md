1. Findings by severity
Critical

None.

High

None.

Medium

Quality-bar reference selection is not yet an executable, outcome-independent policy.

Issue: The draft carefully defines how a pinned reference configuration determines qualification, how its uncertainty propagates, and what happens when its cost evidence disappears. However, it does not specify how the reference identities are initially selected. “Named reference configurations” and the example of a “median definite-frontier model” leave the number of bars, selection population, median ordering, tie-breaking, and empty-frontier fallback unspecified. Freezing an identity after selection does not make that selection reproducible.
paste.txt

Why it hurts the objective: “Cheapest above a bar” is the output that most directly answers the buyer’s cost question without relying on the headline score’s cost–quality exchange rate. Its answer nevertheless depends on the chosen bar. Selecting references after inspecting cheapest configurations could favour particular results while satisfying all subsequent solver and uncertainty requirements.

Concrete change: Publish a versioned bar-selection policy before examining bar winners. Either name reference configuration IDs editorially in advance, or define an executable selection algorithm with explicit fallback and tie rules. Record the selection cutoff and candidate population separately from the resulting reference-quality object.

What is new: E50 and E52 address reference dependence, uncertainty, and continued applicability; E100 addresses label signatures. This finding concerns the earlier selection of the reference itself, not those already-adopted protections.
paste.txt

Low

None.

2. Methodology design recommendations
Priority 1 — Complete the bar-selection contract

Add a reference-selection object alongside the existing reference-quality object:

text
bar_policy_id
bar_policy_version
selection_mode
selection_cutoff
selection_population_rule
selection_order
selection_positions_or_named_ids
tie_rule
empty_population_rule
reference_configuration_ids
reference_quality_object_ids

Two implementable designs preserve the current methodology:

Editorially named references, committed in advance.

Publish exact configuration IDs before calculating the release’s bar winners.

Keep the identities fixed over a declared reference-policy period.

Replace an identity only through an explicit policy revision, publishing old-bar and new-bar results on the common evaluable panel.

Preserve E52: losing cost evidence does not invalidate an otherwise evaluable reference quality expression.
paste.txt

Deterministically selected references.

Define the selection population precisely—for example, the API main-workload definite-frontier configurations that are non-provisional.

Specify the ordering used to choose a median; “median frontier configuration” alone is insufficient because frontier membership does not define a unique ordering.

Specify the lower or upper median for an even-sized population, configuration-ID tie-breaking, and what happens if the population is empty.

Generate and publish the reference IDs before evaluating cheapest-above-bar events.

The first design is simpler and more stable across releases. The second adapts to the cohort but makes the bar itself move with evidence and frontier membership. Neither requires additional measurements, imputation, relaxed exact-variant rules, or provider quota claims.

Add these regression fixtures:

Reordering the input files leaves selected references unchanged.

Recomputing cheapest-above-bar outcomes cannot change selected reference IDs.

An empty selection population produces the declared fallback or an unavailable bar—not an improvised reference.

Reference replacement produces an explicit reference-policy transition, distinguishable from a configuration’s quality or cost change.

Preserve the existing uncertainty target and owner decisions

I would not change the 25/75 headline weights, O27 cost-completeness convention, subset scoring, exploratory Plan scoring, or published-record interval target on the evidence supplied. Their limitations are already explicitly addressed by owner decisions and the adopted disclosure and eligibility rules. Recommending their removal would repeat settled points rather than identify a new methodological defect.
paste.txt

In particular, the draft explicitly states that no Plan route currently has an identified target-workload multiple and that v1 scenario shares do not quantify benchmark repeatability. Those are important limitations, but they are not undisclosed gaps that require another equivalent warning or uncertainty mechanism.
paste.txt

3. Questions for the owner

Should quality bars remain anchored to stable buyer reference configurations across releases, or deliberately track the current cohort? That choice determines whether advance-named identities or an adaptive deterministic selection rule is preferable.

4. Verdict

VERDICT: HAS FEEDBACK