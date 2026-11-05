0. Read check

Read both listed parts to their ends at commit 2ca6c729a3f1a11bd08f5d669f5977875b087381, in order.

Part 13 — draft-r169-part-13-of-14.md

First line: “## Governance”

Last 12 words: “before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;”

Part 14 — draft-r169-part-14-of-14.md

First line: “O65 had moved it from 2026-10-23T06:26:23Z and O47 from 2026-10-21T05:24:16Z). Its chart selects 89 catalog models and plots 82, far fewer than v4.3.2's.”

Last 12 words: “normative); it is in draft-r169.md in the same folder of the repository.”

This review concerns only these two parts. References below identify their named rules and sections; rules incorporated from other parts are treated as defined.

1. Findings by severity
Critical

None.

High

None.

Medium

The “One AA state” conclusion is stronger than the synchronization test described.

Issue: Part 13, “One AA state (E217),” specifies that the model-page snapshot, chart, Coding Agent Index and cost-chart captures are within seven days of the snapshot, and concludes that the frontier point, quality evidence and costs therefore “describe one AA state.” Capture proximity alone does not establish that conclusion: a source can change during even a short capture sequence, leaving the cohort selected from one revision and scored from another. O65’s re-capture requirement reduces this risk, but does not itself test whether the re-captured surfaces agree.

Why it hurts the objective: ValueRank’s exact-configuration discipline depends on the cohort-selection record and the scored record belonging to a coherent release. An undetected cross-surface update could change eligibility or value while all individual freshness gates pass.

Concrete change: Retain the existing clocks, but distinguish “capture-window compliant” from “cross-surface reconciled.” Add a release-level reconciliation of overlapping public fields: exact configuration identity, effort and fallback state; displayed Index score and total cost where duplicated; and benchmark/version identifiers where exposed. An unexplained mismatch should trigger re-capture of the affected surfaces. Where public fields cannot establish consistency, say “captured within the permitted window; common source revision unverified,” rather than asserting one AA state.

What is new relative to the ledger: This does not propose another freshness threshold or repeat O65’s refresh requirement. It addresses the logical gap between freshness/re-capture and cross-surface consistency.

Low

The lifecycle’s final explanatory sentence misdescribes previously admitted reports as diagnostics.

Issue: Part 14, immediately below the Plan evidence lifecycle table, says that the age rows apply to “earlier-admitted reports kept as diagnostics.” But the table’s O127 rule expressly says an earlier-admitted report “keeps counting and ages on its own clock,” including periods when it supports an official route.

Why it hurts the objective: This creates avoidable ambiguity about whether admission survives the report window for official scoring or only for diagnostic display.

Concrete change: Replace the phrase with: “previously admitted reports retained under O127; their official or diagnostic status follows the applicable age stage.”

This is a wording correction implementing O127, not a challenge to that decision.

2. Methodology design recommendations

Add a small, machine-readable AA reconciliation object before claiming a common state. Extend the existing evidence bundle rather than creating another research process:

text
aaStateReconciliation:
  capture_ids
  checked_fields
  matching_fields
  unexplained_mismatches
  unavailable_checks
  status: reconciled | mismatch | not_verifiable

Compare only fields that the public surfaces actually share. Use the existing reporting-precision rules for displayed numbers; do not introduce an arbitrary numeric tolerance or impute unavailable values. Recommended handling:

reconciled: overlapping fields agree; publish the captures and checks.

mismatch: re-read the affected surfaces and resolve or explicitly classify the discrepancy before release.

not_verifiable: retain the existing eligibility rules, but publish the narrower capture-window statement.

This is routinely refreshable from the captures already required. It adds a consistency check without changing the cohort policy, quality weights, cost estimand or exact-variant evidence rules.

Make the lifecycle summary explicitly preserve admission separately from age. Correct the sentence identified above and add a documentation fixture covering one previously admitted report pair at ages 31, 91 and 121 days. The fixture should verify that leaving the original admission window does not itself remove admission, while the existing lifecycle still changes official eligibility at the prescribed stages. This tests the presentation of O127 and O13 rather than introducing a new evidence policy.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK