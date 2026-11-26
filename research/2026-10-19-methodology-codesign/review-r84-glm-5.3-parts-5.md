0. Read check

Both listed parts were read through their ends at commit 8e532e4891e1759c825d0fed89e1ae32fbc9eea1, in order. Their opening lines are exceptionally long; the opening quotations below are excerpts of those lines, not reproductions of the complete lines.

Part	First-line opening	Last 12 words
5	“Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V], and for each model × plan cell it ends instead at that cell's latest staged search”	“is diagnostic; a transfer from a lapsed report donor, which is diagnostic.”
6	“Quota schema: the registry stores each plan's limit-schema version: windows (e.g. 5-hour and weekly) with their semantics”	“Plan rows resting on an owner assumption, by kind (marked †, E242).”
1. Findings by severity
Critical

None.

High

None.

Medium

The monthly research restriction and seven-day search-age gate lack an operationally compatible refresh rule. Issue: Part 5 says O164 permits the three research stages over each model × plan cell “at most once per calendar month” unless a registered change, new model or new plan makes another search unavoidable. It also says E218 requires the latest all-provider search to be no more than seven days old and fails the build otherwise. A narrower supplementary search explicitly cannot advance that all-provider cutoff. Consequently, in an otherwise unchanged month, a release more than seven days after its all-provider search cannot satisfy both rules: repeating the search breaches the monthly restriction; reusing it breaches E218. The present release happens to sit exactly on the seven-day boundary, but that does not establish a workable subsequent refresh cycle. Why it hurts the objective: A routinely refreshed public ranking needs a defined path for publishing unchanged evidence as well as changed evidence. This interaction can unnecessarily stop refreshes of the entire ranking, despite no deterioration in its underlying measurements. Concrete change: Separate the monthly three-stage allowance investigation from a lightweight release-time freshness check. Keep the former monthly; require the latter within seven days of each release. Publish their separate dates and coverage, and specify which detected events trigger renewed three-stage research. What is new relative to the ledger: This is not a request to reverse O164’s monthly cadence or weaken evidence admission. It identifies the scheduling conflict between that newly adopted cadence and the retained E218 all-provider freshness gate.

Low

None.

2. Methodology design recommendations
Priority 1 — Separate discovery freshness from allowance-investigation freshness

Implement two explicitly different records:

Record	Required contents	Cadence
Allowance investigation	Model × plan coverage; three ordered stages; queries; report artifacts; unreachable sources; searchedThrough	Monthly, plus O164’s exception triggers
Release freshness check	Provider plan pages and announcements checked; registered changes; new models/plans; affected cells; check timestamp	Within seven days of each release

Use independent gates:

FreshnessCheckAge
⁡
(
𝑉
)
≤
7
 calendar days
FreshnessCheckAge(V)≤7 calendar days

and

InvestigationCurrent
⁡
(
𝑐
)
=
MonthlyCoverageValid
⁡
(
𝑐
)
∧
¬
UnresolvedResearchTrigger
⁡
(
𝑐
)
.
InvestigationCurrent(c)=MonthlyCoverageValid(c)∧¬UnresolvedResearchTrigger(c).

The monthly-validity convention should be explicit—calendar month or a specified maximum age—not inferred from “last month.”

Preserve O161: the lightweight check must not advance a cell’s report-admission searchedThrough date unless it actually performs the required report research. Likewise, it must not imply that intervening user reports were searched.

Publish four fields together:

releaseFreshnessCheckedOn

allowanceInvestigationCompletedOn

searchedThrough

unsearchedReportDays

This resolves the scheduling conflict without changing report concordance, numerator eligibility, donor ageing, route precedence or exact-variant evidence policy.

Priority 2 — Add a no-change scheduling fixture

Add a build fixture covering two releases in the same calendar month, more than seven days apart, with no new model, plan or registered change.

The expected outcome should demonstrate that:

The monthly three-stage investigation is reused.

A current release freshness check satisfies the release gate.

Existing measurements continue ageing from their observation dates.

The report-admission window remains bounded by the actual staged search.

No report route gains evidence merely because a provider page was checked.

This tests the interaction of the rules rather than each clock independently.

3. Questions for the owner

Is the intended release schedule limited to one release per month, or must the methodology support releases more than seven days after the monthly all-provider investigation when no research-triggering change has occurred? That determines whether the appropriate correction is the two-clock design above or an explicit publication-schedule restriction.

4. Verdict

VERDICT: HAS FEEDBACK