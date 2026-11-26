Part 1 read. Continuing with part 2.
Part 2 read. Continuing with part 3.
Part 3 read. Continuing with part 4.
Part 4 read. Reading part 5 now.
All five parts read to end. One quick factual check before I write the review.
0. Read check

Part 1 — first line: # ValueRank methodology — draft r159. Last 12 words: "re-capture; applying O145 moved the release cutoff (O65) and re-captured every source."

Part 2 — first line: - **Two rankings (owner decisions O52, O53, O54)**: ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52). Last 12 words: "matrix is published without a synthetic total. The basket itself is unchanged (O15)."

Part 3 — first line: - **Accounting identities.** AA's total Index cost decomposes into its **nine** v5 evaluations (Σ cost per task × task counts: Briefcase 91, AutomationBench 657, GDP.pdf 100, FrontierCode 2.0 132, Terminal-Bench 4.0 66, Terminal-Bench-Science 70, CritPt v2 40, Omniscience 3,000, HLE-Diamond 1,000; … Last 12 words: "on the Plan basis the workload question is the M_W identification status."

Part 4 — first line: - **Plan cost input (full-utilisation effective cost, labelled)** = API cost input ÷ Value Multiple of the selected route. Last 12 words: "for other Claude models; the transfers keep their assumption label and caution."

Part 5 — first line (after one blank line): **Report window (E194, O32, E201a)**: the report window is the closed day interval [V − 30 days, V], compared as UTC calendar dates … Last 12 words: "(no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

All five parts were read to their ends through the connector.

1. Findings by severity

Critical

The Plan half of the stated objective is currently unanswerable under the methodology's own rules, and it is on a known expiry schedule. The objective clause (a) commits ValueRank to subscription-plan economics, but the draft states that no Plan route has an identified M_W, so every Plan frontier and bar output is unevaluable (E61/E67) and the Plan ranking is disclosed as "exploratory arithmetic." The evidence base underneath is worse than "thin": every controlled measurement comes from one SemiAnalysis article dated 2026-10-06; every one of those routes is already flagged possibly superseded by detected changes (OpenAI 2026-10-11, the Claude meter change of 2026-10-17), ages to possibly-superseded on 2026-11-06 regardless, and expires 2027-01-05; and the O71 three-stage pipeline has admitted zero routes across two all-provider searches plus a supplementary entrant search. This is all honestly disclosed, so the harm is not deception — it is that the deliverable promised to Plan buyers does not exist and the pipeline has never once produced an admitted route, which is evidence the admission design may be unreachable rather than merely unlucky. Concrete changes: (i) publish a release-level Plan evidence status block (routes in force, days to donor expiry, passing cells this release, passing cells to date) computed from registry fields that already exist; (ii) make the measured-only Plan view (kept under O22/E164) the first table of the Plan tab and the assumption-based arithmetic the second — both artifacts exist, this is display order, not new machinery; (iii) ask the owner to pre-register the post-expiry Plan policy now, before 2027-01-05, rather than discovering it at the release where the last donor expires (see Q3). Note: the strict all-reports ±20% concordance is owner-fixed (O11/O74), so I recommend around it, not against it — see the O46 generalization in section 2.

High

Rank-separability thresholds draw only quality noise while the same release shows cost carrying most of the value variance. O39's threshold uses SD_i = 0.75 × the quality SD — "cost is not drawn" — yet E196's realized-influence print for the max-effort ranking shows cost's value-variance allocation at 75% on the API basis. Where cost is the dominant term, a separability statement built from quality noise alone understates the true threshold and overstates separability; the printed "1 of 6 adjacent API ranks separate" in the max-effort ranking is optimistic on the methodology's own numbers. This does not repeat any rejected item: S1T/O39/O42 govern benchmark task sampling, and E150's "no benchmark-noise promises" does not cover the cost half of the score — the gap is that cost noise (which O25/O27 already assign to the scenario layer conceptually) never reaches the separability statistic. Change: add an S1C cost-noise stream drawing from the per-task cost data already captured for O27 and the six Index SDLC evaluations (independent-task draws, like S1T, over the 290/132/66-task components), folded into the separability SD and the band rule alongside quality; until it ships, rename the statement "separable under quality-noise only — a lower bound on the true inseparability."

The two leading rankings price configurations on different admitted baskets, with no published bridge for the configurations ranked in both. Under O57/E254 the max-effort ranking admits the Coding Agent Index v2.0 (8 of 9 priced) while the AI Coding Daily ranking prices the same SDLC claim on the six Index evaluations alone (CAI at 7 of 20, pending). Four configurations sit in both rankings and therefore carry two materially different "basket costs" for what both rankings present as the same SDLC-cost question; E86's anchor-applicability machinery exists for W vs W_S but no cross-ranking pairing is published, and "values never compare across rankings" does not stop a reader comparing the displayed dollar figures. Bridge diagnostics are already the methodology's own pattern for workload migrations. Change: publish a paired-bridge table for shared configurations — cost under each admitted set, the delta, and each anchor object's exchange rate — in diagnostics; nothing about admission (owner O57) changes.

Medium

The SWE-Atlas QnA unrewarded-share disclosure presents an assumption as a bound. Part 3 prints the QnA share as "bounded by its task-count share (0 to 124/290 ≈ 43% of the index's cost, a reading that assumes no task costs more than another)." Absent the equal-cost assumption, the defensible interval is 0–100% of the pooled CAI cost — any task could cost any fraction. The methodology elsewhere is strict about not promoting assumptions to bounds (O19, E169, E210 inactive while structural inputs are missing); this sentence does exactly that. Change: print the assumption-free interval 
[
0
,
𝐶
CAI
]
[0,C
CAI
	​

] and the equal-cost point estimate (~43%) explicitly labelled "assumes equal per-task cost," one-line spec change to E203's disclosure.

Ordinal ranks remain the primary presentation despite the methodology's own finding that adjacent ranks are mostly noise. The AI Coding Daily ranking prints 0 of 19 separable adjacent pairs and the max-effort ranking 1 of 6, yet the headline leads with ordinal positions; the O42 bands that encode the honest granularity sit beside them. The logic of O22 (drop the "recommended" label to avoid overclaiming) extends to display hierarchy without touching O2's ordinal ranks: make the noise band the default visual grouping on the site and README and keep ordinal rank as a secondary column. Ranks stay, per owner policy; only salience changes.

Low

Weekly-to-monthly conversion constant "4.33" is convention-dependent and below the methodology's own precision bar. 4.33 is the 52/12 (364-day-year) convention; the plain-year average is 4.345 and the Gregorian average 4.348. The spread across conventions is ~0.3–0.4% — immaterial to current Plan results (zero admitted report routes) but the document holds accounting identities to 10⁻⁶ (E209). Change: state the exact convention (e.g., 52/12) as a rational in the registry rather than a rounded decimal.
calctide

Cohort boundary sits on rounded-Index values with no marginal-membership diagnostic. O129 (owner-fixed) keeps the near gap on AA's plotted Index, and part 1 notes rounded tooltip ties; a configuration at gap 3 vs 4 can flip on ±0.5-point rounding of either side. Change: at capture, publish a "marginal cohort" list — configurations within one rounded point of the near-gap boundary and whether unrounded membership would differ — as a capture diagnostic; it changes nothing about membership.

2. Methodology design recommendations

Prioritized, all implementable from public, routinely refreshable data:

S1C cost-noise stream (feeds finding H1). For each admitted component, draw per-task costs from the captured per-task cost fields (CAI per-task costs under O27; Index SDLC per-task costs from AA's evaluation payloads) under the same independent-task convention as S1T; sum to C_i,W, score through the frozen anchors, and combine with S1T in the scenario shares and the adjacent-pair separability SD. Publish the separability statement with cost noise on and off so the effect is visible.

Plan evidence runway + generalized quota ceilings (feeds C1). (a) The status block described above. (b) Extend the O46 pattern — quota-implied ceiling = documented quota × recorded API rate ÷ fee, flagged "provider-derived, optimistic end" per O125 — to any provider whose public docs state a hard quota convertible at a public rate, each priced under the release's price records per the O46 precedent. This gives every Plan row a bounded, flagged, refreshable upper anchor from public data instead of API-cost fallback, and never competes with measured routes under the existing comparator (it sits below report pairs by grade definition). This rides on an existing owner exception rather than asking for a new policy from scratch.

Cross-ranking paired-cost bridge (feeds H2). As specified above; reuse E86's paired full/subset presentation format so readers already know how to read it.

Correct the E203 interval presentation (M1). Assumption-free range plus labelled point estimate.

Band-primary display (M2). Layout-only; bands already exist (O42/E248) and the separability statement already accompanies them.

3. Questions for the owner

May the O46 quota-ceiling treatment be generalized to any provider with a documented hard quota and public API rate (flagged like O125), or is MiMo's ceiling meant to remain a one-off exception? This determines whether the Critical finding's remedy is "bounded estimates everywhere" or "API fallback until measured routes exist."

Do AA's captured payloads contain per-task cost dispersion (per-task cost lists or SDs) for the CAI and Index SDLC components? If yes, S1C is buildable as specified; if no, the interim fix for H1 is the "quality-noise-only lower bound" relabel.

At the first release after the SemiAnalysis donors expire (2027-01-05), is the Plan basis intended to keep publishing assumption-only rows under O13 indefinitely, or should a policy change be drafted before that date? The answer decides whether recommendation C1(iii) is a status block or a redesign.

4. Verdict

VERDICT: HAS FEEDBACK