0. Read check

Both listed parts were read through their returned ends at commit 0aedd96ddfb5c1e86ba1487bc7845bfe301e946d, in the requested order. For part 14, the first line is a very long paragraph; the quotation below identifies its opening rather than reproducing that entire paragraph.

Part 13

First line:

Governance

Last 12 words:

before the cutoff (O132 moved the cutoff from the 2026-10-25 capture instant;

Part 14

First-line opening:

O65 had moved it from 2026-10-23T06:26:23Z and O47 from 2026-10-21T05:24:16Z).

Last 12 words:

normative); it is in draft-r163.md in the same folder of the repository.

This is a sectional review of these two parts only. Rules they cite elsewhere are treated as defined there.

1. Findings by severity
Critical

None.

High

None.

Medium

The lifecycle table still specifies the superseded report-window endpoint. Issue: Part 14’s “Report out of window (O32)” row explicitly defines the window as [V − 30 days, V]. The supplied decision ledger says O161 instead makes a cell’s report window end at its latest staged search. These are different admission rules whenever the search precedes the release cutoff. This finding concerns an explicit conflicting statement, not a rule presumed missing from another part. Why it hurts the objective: Report admission can change the selected Plan multiple, whether a report pair exists, and whether a row uses an assumption or API fallback. For example, with a search five days before release, a report 28 days old at search is 33 days old at release: it passes the O161 window but fails the table’s window. Leaving both definitions in the normative methodology makes the evidence selection—and therefore the ranking—dependent on which statement an implementer follows. Concrete change: Replace the table’s release-cutoff window with the cell-specific search window under O161. Preserve the distinction between first admission and O127’s continued counting of previously admitted reports. Generate the displayed window from the same admission object the build evaluates. What is new: O161 already adopts the intended endpoint. The remaining issue is that the lifecycle table in this reviewed revision still prints the old endpoint; this is a consistency correction, not a request to reconsider that decision.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the report window a single executable, displayed object

For each canonical model–plan cell 
𝑐
c, define:

𝑆
𝑐
=
the latest staged-search endpoint specified by O161
,
𝑊
𝑐
=
[
𝑆
𝑐
−
30
 days
,
 
𝑆
𝑐
]
.
S
c
	​

=the latest staged-search endpoint specified by O161,W
c
	​

=[S
c
	​

−30 days,S
c
	​

].

Use that object consistently for first-admission decisions, the lifecycle table, the report registry and published search-coverage disclosures.

The implementation should distinguish:

First admission: apply the cell’s 
𝑊
𝑐
W
c
	​

, alongside the existing independence, partition, concordance and other admission rules.

Previously admitted evidence: apply O127’s retained-evidence lifecycle rather than retrospectively rejecting it because it left the first-admission window.

Release eligibility: continue to apply the release-cutoff rules separately; a search-window endpoint must not silently replace the valuation timestamp or other evidence clocks.

Add boundary fixtures where the search precedes the release by several days, including a report that passes the search-based window but fails the former release-based window. Assert both the admission result and the window printed in the methodology.

No new benchmark, weight, imputation, provider-quota numerator or private data source is needed. This recommendation implements the existing owner decision and resolves the explicit inconsistency identified above.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK