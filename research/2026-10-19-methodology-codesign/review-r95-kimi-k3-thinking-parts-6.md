All four parts are read in full. Before writing the review, I'll verify two external methodological points that bear on my findings.
0. Read check

All four parts were opened via the GitHub connector (alo-labs/valuerank @ 954f80e) and read to the end. First lines and closing words, in order:

Part 6 (draft-r177-part-6-of-15.md) — first line: "every priced and dated report the O71 record holds for a cohort model, eligible or not, is a row of data/plan_reports.json, copied field by field from the record (provider, plan, model, observer, link, stage, report date, the measurement window only where stated…". Last 12 words: "(no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

Part 7 (draft-r177-part-7-of-15.md) — first line: "- Assumptions: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled…". Last 12 words: "value; no epsilon is introduced. Domain validity is separate from evidence completeness."

Part 8 (draft-r177-part-8-of-15.md) — first line: "- Scoring with frozen, per-basis anchors in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); anchor object (E20)…". Last 12 words: "10% | — | points of 60; z = 100 × points / 60".

Part 9 (draft-r177-part-9-of-15.md) — first line: "| General professional work (20%) | GDPval-AA v2.1 (Elo as displayed on AA's model page at the capture; E90, O70) | 10% | 10% | 10% | z = 100 × clip((E − 500)/2000, 0, 1)…". Last 12 words: "a bias bound in the identification layer); repetitions are not a bias."

All four parts were read to their ends. The parts reviewed cover: Plan report evidence and quota schema (part 6), transfers/admission/anchors-adjacent Plan machinery (part 7), cost anchors, clip gate and quality normalisation with the leaf table (part 8), and the remaining leaves, GDPval estimand, added-leaf matching, Bug Hunt selection and missing-data rules (part 9).

1. Findings by severity

Critical

None.

High

None.

Medium

Concordance is tested over values, not observers (part 6, O71 v1 profile). The profile states "One observer counts once, but every value the observer reports enters the range test," and O86's margin is then applied as largest lower ≤ 1.20 × smallest upper over all values. Adding values can only raise the largest lower and lower the smallest upper, so a single diligent observer who logs heterogeneous sessions (e.g. ranges and ) can single-handedly break concordance for a cell where each observer's own range comfortably overlaps the others' — while a terse observer logging one monthly figure cannot. Why it hurts the objective: route admission under O11 then depends on observer verbosity rather than on whether independent observers agree, which is what the two-source rule is meant to establish. It fails closed (a route is refused, never wrongly admitted), so this is a coverage and consistency defect, not an integrity hole — but it will systematically exclude legitimate report evidence exactly where usage varies within a meter window. The measurement literature treats repeated readings from one rater as requiring aggregation at the rater level before agreement is assessed across raters, not pooled as independent observations. Concrete change: aggregate each observer to a single range [min lower, max upper] (or the observer's own stated aggregate) and apply the O86 1.20× test across the per-observer ranges; record both the per-value and per-observer outcomes in the cell object so the sensitivity is visible. This is implementable from the existing registry, which already keys reports by observer.
pubmed.ncbi.nlm.nih
+5

Owner decision challenge — O170's Bug Hunt scale is a live, silent re-derivation of a leaf anchor (parts 8–9). The Quality section's own rule (reviewer 77) is that leaf anchors "are then frozen with the methodology version like the cost anchors, so a later change to a leaf's anchors is a methodology version with its bridge, never a silent re-derivation" — with Bug Hunt carved out as the single exception: z = 100 × x/(P_max + U_max), recomputed every release from the live board. What is new versus the ledger: (a) the tension with the frozen-anchor bridge rule is not recorded anywhere as a deliberate exception with rationale; (b) P_max and U_max are per-run maxima over any model and harness — extreme order statistics that grow noisily as the board accumulates runs — so every unchanged model's z (8–15% of quality, enough to flip adjacent ranks given the published ~3.3-point separability) drifts downward between releases for reasons unrelated to those models, and the denominator routinely mixes maxima from two different runs and harnesses, a quantity no run is expected to approach; (c) E301's noise model covers a record's own sampling noise, not the scale's sampling noise. Relative-to-max leaderboard normalisation is a known source of cross-release rank instability. Concrete change: freeze P_max + U_max per methodology version with a versioned re-scale and old/new bridge (mirroring the cost-anchor machinery the draft already has), or at minimum compute maxima over per-model best means rather than individual runs, publish a scale-sensitivity (z and rank change if the scale moves ±10%) beside bugHuntScale, and route O170 scale movements through the E177 replay as a named swing cause.
arxiv
+1

Low

Plan anchors inherit the API reference panel's configuration set, and the gate population counts plan rows, not configurations (part 7 O157/E160, part 8). Plan anchor references are "the measured plan rows of the same configurations" as the API references, so the Plan anchor range reflects which configurations happen to have complete API cost evidence, not the dispersion of measured plan costs; and because O48 creates one row per configuration × plan, a provider selling four tiers contributes four times the gate population of a single-plan provider. The O58 disclosure shows the symptom: roughly nineteen listed Plan rows sit beyond the anchors, several 15–70× below c_L, so future admissions of listed rows will predictably trip the clip gate and force re-freeze cycles, and the Plan exchange rate (5.31 points per doubling today) is panel-composition-sensitive. E321 already publishes configuration-balanced identification yield for the same reason; this finding extends that argument to anchors and the clip gate, which the ledger does not record. Concrete change: publish a Plan-anchor coverage diagnostic (share of cohort and listed plan rows inside [c_L, c_H] per ranking), count the clip gate's n over configurations rather than plan rows, and consider allowing Plan references from measured plan rows of any ranked configuration at the next versioned freeze (E304's atomicity only requires both minima, two per basis).

The GDPval estimand check is logically uninformative in three of four cells (part 9, O70/E90). The draft is candid that the displayed Elo "is not shown to be the value AA's Intelligence Index integrates" and that the capture comparison is the only empirical test — but by its own account the test says something only when a page's Elo moves while its Index total does not; "no movement, or movement on both, tests nothing." So the diagnostic can never bound the discrepancy that actually matters, and a synchronised AA refit would pass it silently. Concrete change: state plainly that the estimand match is unverifiable from public captures in general, and instead publish an envelope bound per configuration — the observed Elo drift since that configuration's addition to AA's board, converted to z and value points — as the disclosure of how wrong the leaf could be, rather than relying on the 2×2 capture test. Low because the owner chose the displayed Elo (O70), today's measured movement is 0.00, and GDPval carries 10% of quality.

E268 couples the Bug Hunt and AI Coding Daily leaves through harness matching (part 9). Selecting the AICD record by equality with the configuration's Bug Hunt harness means an E206 Bug Hunt record switch (e.g. a larger-N run appearing on a second CLI) changes the AICD leaf with no new AICD evidence, and the two leaves' movements become correlated by construction — which the E81 covariance allocation and leaf rank-correlation matrix will then read as genuine leaf agreement. E334 attributes the induced change separately, which fixes the accounting but not the induced correlation. Concrete change: pre-register a per-model AICD harness preference (the E225 closed-list pattern already exists for Terminal-Bench agents) independent of the Bug Hunt record, or at minimum publish the count of rows where the coupling binds and a decorrelated sensitivity.

Band-dominated report cells carry manufactured precision (part 6, O115/O86). For coarse range reports the pass band can be wide: reports and pass O86 (90 ≤ 120), the clip band is, both midpoints (55, 245) are clipped into it, and the pooled geometric mean ≈ 94.9 is determined almost entirely by the clip rather than by the reports. The route then displays a point value whose precision the evidence does not have. Concrete change: when clipping moves any midpoint, flag the cell "band-dominated," publish the pre-clip and post-clip midpoints, and carry the band width into the route's scenario-layer uncertainty instead of scoring only the pooled point.
alphasignal
+5

2. Methodology design recommendations

Prioritised, all implementable from data the registry already holds:

Observer-level concordance unit (fixes finding 1). Admission rule: cell passes if, after reducing each observer to [min lower, max upper] over their reports in the current partition, the largest per-observer lower ≤ 1.20 × smallest per-observer upper, with ≥2 non-provisional observers. One line of registry logic on existing fields; removes the verbosity dependence from O11 admission.

Versioned Bug Hunt scale with bridge (fixes finding 2). Freeze (P_max + U_max) at each methodology version, re-scale only by a versioned freeze that publishes old/new z for every ranked row (the draft's dual-run pattern applied to one leaf), and use per-model best means as the maxima inputs. Adds cross-release comparability to 8–15% of quality at near-zero cost.

Plan-anchor coverage and configuration-balanced gating (fixes finding 3). New published diagnostic: per ranking, share of ranked, listed, and cohort plan rows inside the Plan anchors; clip-gate n counted over configurations. This converts the current long O58 disclosure list into a tracked metric the owner can set a threshold against (e.g. schedule a re-freeze when coverage drops below a level), instead of discovering the problem one entrant at a time.

Estimand-gap envelope for GDPval-AA (fixes finding 4). Per configuration, publish drift_since_addition = |Elo_now − Elo_at_first_capture|, its z and value-point equivalents, and the maximum over ranked rows. This is a defensible upper-envelope disclosure computed from captures the evidence bundle already stores.

Pre-registered AICD harness preference list (fixes finding 5). A versioned registry list (model → harness preference order), closed like E225's agent list; Bug Hunt record changes then never move another leaf.

Band-domination flag and uncertainty transport (fixes finding 6). Cell-level boolean when O115 clipping binds, with the band width passed to the scenario stream as the route's draw range.

3. Questions for the owner

Is O86's concordance unit intended to be the observer or the individual reported value? (Determines whether finding 1 is a correction or a clarification; the current text asserts both.)

Should O170's scale be permanently live, or live only until the next methodology version freeze? (Determines whether recommendation 2 is a freeze-with-bridge or merely the robust-maxima and sensitivity publications.)

May Plan anchor references be drawn from measured plan rows of configurations outside the API reference panel at the next versioned freeze, provided E304's both-bases minima hold? (Determines whether recommendation 3's reference change is available or only its diagnostics.)

4. Verdict

VERDICT: HAS FEEDBACK