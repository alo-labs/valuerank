0. Read check

Both listed parts were opened through the GitHub connector at commit 5c2ab13991d61e5a15c418407e9c9e95db001918 and read to their ends. Part 5 starts with an exceptionally long single-line paragraph; the opening quotation below is an excerpt of that first line, not a claim to reproduce the entire line. Part 6 begins with a blank line.

Part 5

First line, opening excerpt:

Plan cost input (full-utilisation effective cost, labelled) = API cost input ÷ Value Multiple of the selected route. Computed per model–plan tier–surface–configuration route (tier and fee are part of route identity and published).

Final sentence:

Fable 5.1's Max multiples (12.4–12.7x against Opus 5.5's 57–59x) reflect Fable's own tighter allowance in Claude plans, so they are not used to illustrate how far the Opus 5.5 transfers could miss for other Claude models; the transfers keep their assumption label and caution.

Part 6

First line:

[Blank line.]

The first nonblank line begins:

Report window (E194, O32, E201a): the report window is the closed day interval [V − 30 days, V], and for each model × plan cell it ends instead at that cell's latest staged search, so it never claims days nobody searched

Final sentence, which ends at the part boundary with a semicolon:

Report admission is computed (owner decision O81, 2026-10-26): a passing cell's value is the geometric mean of its non-provisional reports' midpoints (the E33 pool), each midpoint first clipped to the concordance band [largest lower bound ÷ 1.20, 1.20 × smallest upper bound] so a wide report cannot pull the pool beyond what O86 admitted, the band, taken over the same reports as the range test, being published (owner decision O115, 2026-10-29; the symmetric band leaves concordant point reports unchanged, E271), with the observers whose midpoint it moved (bandMoved, on reviewer 95), so a value the band decides is visible; owner decision O159, on reviewer 78: the range test reads the non-provisional reports, plus a provisional report only once its inferred tier or model has been re-checked against them and the check logged with the report (inferenceRechecked), so a wrongly scoped provisional report cannot fail a cell;

The findings below concern only these two parts. They do not treat rules cited elsewhere as missing.

1. Findings by severity
Critical

None.

High

None.

Medium
M1. The timestamp cutoff expressly admits evidence from after that timestamp

Issue: Part 6 defines the release cutoff as the valuation timestamp 
𝑉
V, but explicitly permits a report dated on 
𝑉
V's UTC date “whatever its hour.” Consequently, a report with a known timestamp later than 
𝑉
V can enter a release whose evidence and valuation otherwise stop at 
𝑉
V. This is not merely uncertainty caused by date-only records: the text explicitly truncates timestamped evidence too.

Why it hurts the objective: The rule undermines the release's point-in-time interpretation. A same-day report could reflect a limit change, credit grant or tariff regime that did not exist at the valuation timestamp. Admission and scoped change detection could then operate on different temporal states.

Concrete change: Preserve timestamps where available:

Timestamped reports must satisfy 
𝑡
o
b
s
e
r
v
a
t
i
o
n
≤
𝑉
t
observation
	​

≤V.

Date-only reports from an earlier UTC date remain eligible under the existing window.

Date-only reports dated on 
𝑉
V's date should either await the next release or enter only after the cutoff advances to cover that whole day.

New argument relative to the ledger: This does not reopen the 31-calendar-date window or the two research clocks. It addresses the explicit loss of already-available intraday ordering and its interaction with timestamped valuation.

M2. Part 6 still says API fallbacks enter Plan anchors, contrary to the adopted measured-only anchor policy

Issue: The research-outcome paragraph says providers without an authorised route “use API cost on the Plan anchors (O13).” The supplied decision ledger states that O157 restricts Plan anchors to measured rows. The sentence is therefore a stale operational instruction, not just an omitted explanation.

Why it hurts the objective: Anchor membership changes normalization and potentially every Plan value score. A reader implementing these sections could reasonably include API fallbacks in the Plan reference panel, producing a different ranking from the adopted policy.

Concrete change: Replace the sentence with:

Providers without an eligible Plan route retain API-cost fallback rows for displayed Plan-basis scoring under O13; API-fallback rows do not enter the measured-only Plan anchor panel under O157.

Also make the release's anchor-membership assertion explicitly reject fallback routes.

New argument relative to the ledger: O157 itself needs no reconsideration. The finding is that this particular surviving sentence contradicts its implementation.

Low
L1. Report eligibility and the requirement for a build failure are conflated

Issue: Part 5 says a report lacking all admissible observation dates “cannot be admitted, and the build fails on it.” The same section otherwise describes a discovery object containing included and excluded reports with exclusion reasons.

Why it hurts the objective: Routine public-source research will encounter incomplete candidate reports. If merely recording an undated candidate stops a release, the exclusion register becomes operationally hazardous and creates an incentive not to record failed candidates. If the intended meaning is “the build fails when such a report is admitted,” the wording should say so.

Concrete change: Distinguish candidate validation from admitted-evidence validation:

An undated discovered candidate is excluded with missing_observation_date.

An admitted report without a valid observation date stops the build.

A malformed evidence record that cannot be represented in the exclusion register stops the build separately.

This is a clarification of the existing exclusion procedure, not a proposal to loosen admission.

2. Methodology design recommendations
Priority 1 — Use a typed temporal-admission predicate

Keep the adopted calendar-date window, but separate window membership from point-in-time availability:

Admit
⁡
(
𝑟
,
𝑉
)
=
InCellWindow
⁡
(
𝑟
,
𝑉
)
∧
AvailableByCutoff
⁡
(
𝑟
,
𝑉
)
∧
OtherwiseEligible
⁡
(
𝑟
,
𝑉
)
.
Admit(r,V)=InCellWindow(r,V)∧AvailableByCutoff(r,V)∧OtherwiseEligible(r,V).

Implement AvailableByCutoff from public records:

Evidence precision	Cutoff test
Known observation/publication timestamp	Relevant timestamp must not exceed 
𝑉
V
Date only, before date(
𝑉
V)	Pass the temporal-availability test
Date only, same date as 
𝑉
V	Defer unless the release cutoff covers the completed day

Publish datePrecision, the original timestamp where present, and temporalAdmissionReason. This preserves the existing search-window policy while preventing known future evidence from leaking into a release.

Priority 2 — Assert Plan anchor membership from selected evidence type

The anchor builder should consume the same selected route–measurement object used for scoring, rather than infer eligibility from the existence of a Plan score.

A minimal assertion is:

𝑖
∈
𝐴
P
l
a
n
  
⟹
  
MeasuredEligible
⁡
(
𝑖
)
∧
¬
APIFallback
⁡
(
𝑖
)
.
i∈A
Plan
	​

⟹MeasuredEligible(i)∧¬APIFallback(i).

Here MeasuredEligible should use the already-adopted O157 definition and existing valuation/completeness rules; it should not introduce a new definition of measured evidence. Publish the selected object ID and anchor inclusion reason beside each reference row. This makes the contradiction identified in M2 detectable without changing the owner's anchor policy.

Priority 3 — Separate discovery records from admitting records

Use three explicit states:

discovered_excluded: retained for audit, with reason codes.

eligible_not_selected: valid evidence retained for comparator and alternative-route disclosures.

admitting_selected: evidence that actually supports the selected route.

Apply release-stopping date, independence and archive assertions to the appropriate states, rather than to the undifferentiated collection of everything found. This operationalizes the draft's existing inclusion/exclusion machinery and resolves L1 without admitting weaker evidence.

No changes to the 75% quality / 25% cost policy, exact-variant restrictions, fixed cohort policy, authorised transfers, quota-ceiling exception, or strict all-reports concordance are recommended in this sectional review.

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK