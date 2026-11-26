0. Read check

Both listed parts were read through their ends at commit 5917e61757433bf61ca45bbb5cb030200bb8f863. The first physical line of each file is a long paragraph; the opening quotations below identify those lines but abbreviate their continuation.

Part 5 — draft-r172-part-5-of-14.md

First line, opening: “Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V], and for each model × plan cell it ends instead at that cell's latest staged search, so it never claims days nobody searched”

Last 12 words: “diagnostic; a transfer from a lapsed report donor, which is diagnostic.”

Part 6 — draft-r172-part-6-of-14.md

First line, opening: “- Quota schema: the registry stores each plan's limit-schema version: windows (e.g. 5-hour and weekly) with their semantics — session-anchored (starts at first use), fixed reset (calendar or account reset time) or sliding”

Last 12 words: “selected route moved from ChatGPT Plus to a higher plan under O45.”

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The report-archive grandfathering rule exempts historical reports discovered in future releases, not just the existing evidence stock

Issue: Part 5 introduces archived report copies “from the release after the 2026-11-01 cutoff,” but then grandfathers “reports dated on or before that cutoff.” That exemption is keyed to the report’s date rather than whether the report had already entered the evidence record. Consequently, a report first discovered in a later release can avoid the archive requirement merely because its measurement or publication date precedes the cutoff. This matters particularly because the same part defines a report’s effective date as its measurement-window end where available. The staged search can therefore discover previously unknown, old-dated material after the archive policy begins without requiring a preserved copy. The existing not archived flag discloses this, but does not close the admission exception. Part 5, “Archived report copies” and report-date rules

Why it hurts the objective: The stated purpose of the archive requirement is to keep admitted report pairs auditable when pages or mirrors change or disappear. A report’s age does not establish that it was captured before the requirement existed. The present wording permits new admissions without the evidence preservation that future releases otherwise require.

Concrete change: Grandfather a frozen inventory of report records already present at the 2026-11-01 release, identified by stable report IDs and a manifest hash. Require an archive for every report first added after that release, regardless of its measurement or publication date. Preserve the existing not archived disclosure for the frozen inventory.

Ledger distinction: This does not repeat the adopted recommendation to archive reports. The new argument concerns the temporal key used to implement that recommendation: historical report date versus pre-existing registry membership. If O165 intentionally grants an indefinite exemption to every pre-cutoff-dated report, this recommendation is an Owner decision challenge to that exemption’s scope.

Low

None.

2. Methodology design recommendations
Priority 1 — Make the archive transition inventory-based and testable

Implement the archive transition with three separate concepts:

Field	Meaning
observationDate	The existing evidence date used for windows and ageing
firstRecordedRelease	The first immutable release containing the report record
archiveGrandfathered	Membership in the frozen pre-policy report inventory

For releases after the transition, use:

ArchiveRequirementMet
⁡
(
𝑟
)
=
FrozenLegacyMember
⁡
(
𝑟
)
  
∨
  
ValidArchive
⁡
(
𝑟
)
.
ArchiveRequirementMet(r)=FrozenLegacyMember(r)∨ValidArchive(r).

A valid archive should retain the fields already specified in part 5: page or mirror URL, fetch instant, SHA-256 of the fetched bytes, and quoted allowance span. This recommendation adds no new research stage, source class, quota evidence, or model-to-model transfer; it only makes the existing archival requirement’s boundary reproducible. Part 5, “Archived report copies”

Add fixtures for:

A legacy inventory member without an archive: grandfathered and flagged.

An old-dated report first recorded after the transition without an archive: cannot contribute to admission.

An old-dated report first recorded after the transition with a valid archive: proceeds through the ordinary eligibility rules.

A newly created record claiming a legacy report ID but changing its observer, source or allowance span: fails the legacy-manifest check.

No additional design changes are recommended from these two parts. In particular, I am not reopening the already-decided workload-unmatched Plan scoring, cross-effort routes, donor lifecycle, report-concordance rule, or token-price brackets. Part 6 explicitly separates displayed measurements from target-workload identification and gives unidentified routes no Plan interval eligibility; the absence of identified 
𝑀
𝑊
M
W
	​

 is therefore an acknowledged limitation here, not a newly missing rule. Part 6, “Plan admission decision table” and “Identification yield”

3. Questions for the owner

Does O165 intend to grandfather only report records already collected by the 2026-11-01 release, or every report with an observation date on or before that cutoff—even when first discovered later? The former needs a wording and validation correction; the latter makes M1 an Owner decision challenge rather than an implementation clarification.

4. Verdict

VERDICT: HAS FEEDBACK