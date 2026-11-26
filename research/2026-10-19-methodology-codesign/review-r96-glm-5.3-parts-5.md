Both parts are read. Before writing the review, one quick web check on the real-world facts these parts lean on (plan meters and the speed-mode multiplier cited under O76, and Anthropic's shared weekly meter).
0. Read check

Part 5 (draft-r178-part-5-of-15.md, read to its end; the file ends at the split boundary, mid-bullet, on a semicolon):
theregister

First line (opening sentence of the file's first line): "- Admission rule for the official Plan ranking (O11): a measured route enters only via a controlled saturation measurement with receipts (e.g. SemiAnalysis, labelled a controlled subscription-account measurement with workload projections, so an "established" capacity is a projection on the measured workload, never an individual end-user observation) or ≥ 2 independent end-user reports concordant within ±20% (operationally, E98: the largest report is at most 20% above the smallest; reports of 100 and 120 pass, 80 and 120 fail; for range-valued reports O86 compares the largest lower bound with the smallest upper bound)."

Final sentence as delivered: "owner decision O159, on reviewer 78: the range test and the band read the non-provisional reports, plus a provisional report only once its inferred tier or model has been re-checked against them and the check logged with the report (inferenceRechecked), so a wrongly scoped provisional report can neither fail a cell nor move its value, and the band over every report is published beside it (allReportsBand), and a report route must name the same observers as a passing cell for its plan and model (the build compares observers, not report values);"

Part 6 (draft-r178-part-6-of-15.md, read to its end):
reddit

First line (opening sentence): "every priced and dated report the O71 record holds for a cohort model, eligible or not, is a row of data/plan_reports.json, copied field by field from the record (provider, plan, model, observer, link, stage, report date, the measurement window only where stated (an unstated window is the meter's own period ending on the report date: 7 days for a weekly figure, 30 for a monthly one, its day for a 5-hour one), unit, the observer's full value range, and its flags), and a provenance test checks every row's link, observer and values against the record files;"

Final sentence: "Evidence rules unchanged except for two owner exceptions, the O46 MiMo quota ceilings and the O76 speed-mode conversion of a user report (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

Both parts read fully; proceeding to the review. As a positive external check before the findings: the change log in these parts corroborates against public sources — the 2026-09-14 Anthropic weekly-limit change matches the end of the documented May 13–September 13 weekly-limits promotion, the 2026-10-17 undocumented change matches contemporaneous user reports and SemiAnalysis's own A/B-test detection, the shared weekly cap across web and Claude Code supports the O79 shared-meter flag, and SemiAnalysis's method (run requests, track the meter, price tokens at API rates) matches the draft's characterization of it.
reddit
+5

1. Findings by severity

Critical — None.

High

The value's clipping band and the admission test read the same report set, but the pool excludes provisional reports — so a provisional report can move an official Plan value it is barred from contributing to. O81 defines the cell value as the geometric mean of non-provisional midpoints, "each midpoint first clipped to the concordance band", and states the band is "taken over the same reports as the range test"; O159 puts re-checked provisional reports inside that range test and band. A re-checked provisional report can therefore (a) fail the cell via the range test and (b) extend or shrink the band and clip a non-provisional midpoint, moving the published route value — while part 6 says it "cannot be one of the two reports that admit a route" and it contributes no midpoint. This hurts the objective because, once the first end-user route is admitted, a second-class report (e.g., a form submission with a re-checked inferred tier) can shift a ranked configuration's Plan cost without ever being admitted evidence, and the same ambiguity lets two builds silently diverge on which band clips. Change: state the value band's report set explicitly; my recommendation is non-provisional-only for the value band (Section 2.1), with the admission test and the published allReportsBand unchanged.
theregister
+1

Reports whose windows span a split are excluded outright, which in change-dense periods starves O11's end-user admission arm exactly when it is most needed. The registry records nine split days in the seven weeks to this release (Anthropic 09-14, 09-22, 10-09, 10-17, 10-30; OpenAI 09-29, 10-11, 10-29; Kimi 10-24), and the rule excludes any report "whose window spans a split or touches an accounting-fault day". A weekly Anthropic report ending 10-10–10-16 is dead on the 10-09 split; one ending 10-18–10-24 is dead on the 10-17 instant split; an OpenAI weekly report ending 10-12–10-18 is dead on 10-11. A 30-day report inside the current window cannot avoid a split at all. This hurts the objective because O78's replacement mechanism — a post-change concordant pair outranking a flagged SemiAnalysis measurement — requires post-change reports to survive, and the exclusion rule kills most of precisely those. The result is structural dependence on the single controlled source, weakening the refresh-robustness the methodology is built around. Change (it respects O99's ban on pooling across a change, so I present it as a recommendation; if the outright exclusion was itself intended, this is an owner decision challenge to that intent): mirror E201a's per-period isolation — where a report isolates per-period readings, admit only its post-split periods into the post-split partition, recomputed by the report's own aggregation and flagged "measured across a split"; reserve full exclusion for reports that cannot be isolated.
theregister
+1

Medium

Two unreconciled dating conventions for windowless controlled measurements. Part 5 sets SemiAnalysis's E194 observation date to its publication date (2026-10-06), driving the aging clocks and window membership; part 6 dates the same class of measurement "by its window, else conservatively by the 30 days ending on its publication date" for the fault-window, split and O110 tests. Both statements coexist; nowhere does the draft say which test reads which date. They materially diverge: the fault-window flag on the two chatgpt-pro500 routes only arises under the conservative span [2026-09-06, 2026-10-06], which also spans the 09-29 split. This hurts the objective because a build implementer must guess, and either error changes official Plan selection under O91/O92 (over-flagging healthy measurements or under-flagging ones measured inside fault windows). Change: give each windowless controlled measurement a dating object — observationDate, spanStart, spanEnd, spanBasis: "conservative" — plus a one-line registry table mapping each test (report window, aging, splits, fault windows, O110) to the field it reads, with a build check that spanEnd = observationDate.
theregister
+1

O87's effort-pooling justification conflates the meter's denomination with the valuation's denomination (new argument beyond O146's sensitivity). The text justifies pooling across efforts because "a plan's allowance is the same dollars at any effort". That addresses the allowance, but the multiple's numerator is API-priced consumption by token category (input, cache read/write, reasoning, output). On a tokens or credits meter — the only ones O126 permits for cross-effort routes — the same metered allowance yields different API value when the category mix shifts, and effort shifts the mix (longer reasoning chains, denser agentic cache reads). What is new versus O146, which brackets this as a sensitivity: the bias is systematic per workload class, not symmetric noise, so it belongs on the route as a label, not only in a scenario. Change: attach E208's token-mix status (measured mix vs the route configuration's basket demand region) to every O87 pooled cell and O88 route; "mix unidentified / mix not reported" routes carry the label "effort-pooled; token mix not established" beside their multiple.
reddit

Owner decision challenge — O76's speed-mode conversion uses a single multiplier where the provider publishes funding-flow-specific ones. The draft converts speed-mode reports at "OpenAI Fast 2.5×, Ultrafast 8×". Those are the included-allowance consumption rates; for consumption funded by purchased additional credits OpenAI publishes 2× (Fast) and 6× (Ultrafast), explicitly warning that the multipliers differ by funding source and do not indicate processing speed. A credits-funded speed-mode report converted at 2.5×/8× overstates standard-equivalent consumption by 25–33%, and since E54/E80 already type funding flows and purchased cash enters the gross-cash denominator, the error lands directly in M — large relative to the ±20% concordance band. This hurts the objective because O76 is the one place a provider figure scales a measured numerator, and the wrong flow's multiplier turns a measurement into a mis-measurement. Change: record each report's funding flow at intake (the intake form already collects excluded consumption with its funding source), convert at the matching multiplier, and keep mixed-flow reports as diagnostics or publish the [credits-multiplier, allowance-multiplier] bracket as the cell's range; the registry should also record which windows the multiplier applies to, since users report fast mode drawing down the 5-hour window at its multiplier too.
theregister
+2

Low

The OpenAI split of 2026-10-29 is recorded but its cause is unnamed where the registry describes OpenAI's splits. Part 6's split list names three OpenAI dates but explains only two ("its Day 7 post… and, for ChatGPT Pro 200 only, its 2026-09-29 DevDay plan change"); part 5 implies the 10-29 split is the end of the legacy Pro $200 allocation. Splits are load-bearing (they exclude reports and partition history), so an unexplained split is unauditable in a public methodology. Change: a build check that every recorded split names a typed cause and plan scope — an E100-style register for splits — stopping on an unexplained one.
theregister
+1

E223's "no shared upstream source" has no operational detector. Independence is the backbone of O11's second arm, but detection currently rests on the discovery procedure noticing a shared thread. O165's archive now gives every admitted report a hashed artifact, making detection implementable. Change: cluster archived artifacts by perceptual hash (images) and exact quoted spans; a near-duplicate pair across two observers in one partition fails E223, stops the build, and is published.
theregister

Plans whose schema exposes only sub-billing windows can never pass O11, and the draft never says so per plan. O82 correctly bars 5-hour figures from admitting a route; the consequence — such plans stay permanently on their controlled measurement or fallback — is visible only by inference, so readers cannot distinguish "no one reported" from "no one can ever qualify". Change: derive a per-plan admissibleWindowUnits field from the quota schema, publish it with each cell's status, and print "end-user admission structurally unavailable" beside the evidence source where it applies.
theregister
+1

2. Methodology design recommendations

Prioritized; 1–5 implement the findings above, 6–8 are cheap additions.

Two-band rule (fixes finding 1). Admission range test over all re-checked reports with band 
𝐵
𝑎
𝑙
𝑙
=
[
max
⁡
𝑘
lower
𝑘
/
1.20
,
 
1.20
⋅
min
⁡
𝑘
upper
𝑘
]
B
all
	​

=[max
k
	​

lower
k
	​

/1.20, 1.20⋅min
k
	​

upper
k
	​

] as today. Cell value 
=
exp
⁡
(
mean
𝑘
ln
⁡
(
clip
(
mid
𝑘
,
𝐵
𝑛
𝑝
)
)
)
=exp(mean
k
	​

ln(clip(mid
k
	​

,B
np
	​

))) over non-provisional reports only, where 
𝐵
𝑛
𝑝
B
np
	​

 is the same formula computed over non-provisional reports alone. Publish allReportsBand (B_all) and valueBand (B_np) with bandMoved observers keyed to B_np.

Split-period isolation (fixes finding 2). Registry editorial step (parallel to E201a) records a spanning report's per-period readings; only post-split periods enter the post-split partition, recomputed by the report's own aggregation, flagged "measured across a split". Full exclusion reserved for non-isolable reports. Fixture: weekly report 10-05–10-12 across the 10-11 split isolates 10-12 → admissible in the post-split partition.

Funding-flow-aware speed conversion (fixes finding 5). Intake field fundingFlow ∈ {allowance, credits, mixed}; multiplier table {allowance: {fast: 2.5, ultrafast: 8}, credits: {fast: 2, ultrafast: 6}}, re-captured each release under an O59-style age limit; mixed flows disclose the split or stay diagnostics with a published bracket.
xenospectrum

Dating object and test-to-date map (fixes finding 3). One registry object per windowless controlled measurement and a table assigning each test its date field; build check on consistency.

Token-mix label on pooled-effort cells (fixes finding 4). Reuse E208 statuses and O146's bracket; a label, never a score change.

Split-cause register with build check (fixes finding 6).

Perceptual-hash independence detector over archived artifacts (fixes finding 7).

admissibleWindowUnits publication (fixes finding 8).

3. Questions for the owner

Should a re-checked provisional report be able to move a passing cell's value through the clipping band (current mechanics), or should the value band read non-provisional reports only? (Determines whether finding 1 is a one-line clarification or a retained design needing a label.)

Under O99/O83, is the outright exclusion of split-spanning reports intended, or may an isolable post-split period count in the post-split partition under the O11 test?

For O76: do you accept funding-flow-specific multipliers (credits-funded consumption converted at 2×/6× per the provider's speed-settings documentation ), or should credits-funded speed-mode reports remain diagnostics?
xenospectrum

4. Verdict

VERDICT: HAS FEEDBACK