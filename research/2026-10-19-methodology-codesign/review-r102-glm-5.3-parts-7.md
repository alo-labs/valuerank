0. Read check

Both listed parts were read through their ends at commit 5c2ab13991d61e5a15c418407e9c9e95db001918, in order. Their first physical lines are unusually long, paragraph-length lines. Below I quote their openings rather than reproduce those entire paragraphs; the final sentences are quoted in full.

Part 7

First line, opening:

owner decision O176, 2026-11-03, on reviewer 96: the band that clips the value reads the admitting (non-provisional) reports only, so no provisional report, re-checked or not, can move a cell's value, and the band over every report is published beside it (allReportsBand), and a report route must name the same observers as a passing cell for its plan and model (the build compares observers, not report values);

Final sentence:

Evidence rules unchanged except for two owner exceptions, the O46 MiMo quota ceilings and the O76 speed-mode conversion of a user report (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

Part 8

First line, opening:

Assumptions: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, a transfer with its donor measurement identified; neither identifies M_W.

Final sentence:

Domain validity is separate from evidence completeness.

Source scope: the two GitHub connector file reads only. No other parts, repository searches, raw URLs, or external factual lookups informed this review.

1. Findings by severity
Critical

None.

High

None.

Medium

E246 converts an unstated measurement effort into an apparently exact-effort measurement. Issue: Part 8 says that a SemiAnalysis figure naming a model without an effort “binds to the configuration AA plots under the bare model name,” currently its max configuration. It then classifies other efforts as measurements “from another effort,” while acknowledging that “SemiAnalysis states no effort.” E106 distinguishes exact-effort measurements from O88 cross-effort measurements, and the measured-only view preserves that distinction. The source therefore does not establish the origin effort that these labels assert. Choosing the destination configuration for a record does not establish which configuration the source measured. Why it hurts the objective: The ranking aims to distinguish configurations using exact-variant evidence. Here, a catalog naming convention supplies execution provenance that the measurement did not report. This can also affect route selection: E106 explicitly says O88 measurements rank below exact-effort measurements. Thus the binding can be more than a cosmetic label. Concrete change: Separate measurement provenance from authorized applicability:

Record the source effort as not_reported.

Preserve the owner-authorized use of the figure across the model’s configurations.

Label every affected row “same-model measurement; source effort not reported,” rather than treating max as the measured origin.

Do not award exact-effort precedence unless public evidence actually names or establishes that effort.

When effort evidence becomes available, update provenance and rerun the comparator.

What is new relative to the ledger: This does not reopen O88/O90’s authorization to use same-model measurements across efforts, nor O146’s cross-effort sensitivity. It addresses E246’s separate inference that an unspecified source effort was max, and the consequent exact-versus-cross-effort precedence distinction.

Low

None.

2. Methodology design recommendations
Priority 1 — Make evidence provenance and route applicability separate typed objects

Implement the finding above with two records:

text
measurement:
  model
  source_effort: named_effort | not_reported
  source_effort_evidence
  measurement_object_id

route:
  target_configuration
  measurement_object_id
  applicability_basis:
    exact_effort | O88_same_model | owner_named_transfer | O46_ceiling
  effort_relation:
    same | different | unknown

The governing invariant should be:

ExactEffortEvidence
  
⟺
  
source effort is publicly established
∧
source effort
=
target effort
.
ExactEffortEvidence⟺source effort is publicly established∧source effort=target effort.

A bare model-name match can establish the model identity, but should not independently establish the effort.

For a measurement with unreported effort, retain its permitted displayed multiple and measured-consumption provenance under O88/O90. Keep its effort relation unknown. This preserves the owner’s substantive scoring policy without presenting an editorial binding as an observation.

Priority 2 — Add a comparator regression fixture for unknown effort

Use a synthetic model with two target configurations and two otherwise equally eligible measurements:

Measurement A names the model but does not state effort.

Measurement B explicitly names the target effort.

Test that:

A remains available through the authorized same-model path.

A does not become exact-effort evidence merely because the target is AA’s bare-name configuration.

B receives the comparator’s exact-effort precedence when the remaining keys are equal.

Renaming which AA catalog row carries the bare name does not change A’s source provenance.

The measured-only view reports A’s effort as unknown, without claiming that its other target configurations were measured “at another effort.”

This requires only public-source metadata and routine build tests. It adds no measurement burden, imputation, new benchmark, or change to the cost/quality weights.

3. Questions for the owner

None. The provenance correction can preserve the authorized same-model route policy and its displayed multiples.

4. Verdict

The sections provide detailed controls for report admission, valuation compatibility, evidence aging, funding-aware capacity, and workload identification. My remaining material concern is narrower: an unstated source effort should remain unknown, even when policy authorizes using its measurement for a named target configuration.

VERDICT: HAS FEEDBACK