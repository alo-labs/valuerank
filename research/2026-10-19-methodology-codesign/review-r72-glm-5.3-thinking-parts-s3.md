0. Read check

Both listed parts were opened through the GitHub connector at commit d53cec126a849e9ff191ee07bcccdbc2ce6b46e7 and read to their end.

Part 3 — first line:

Capture status (per ranking, E254). Coding share (E200): the published summary prints, beside the basket label, the share of basket cost carried by coding and terminal tasks (the Coding Agent Index where admitted, Terminal-Bench 4.0 and SciCode), with its median and range over the full-basket configurations (scores.json diagnostics.basketReadiness for each); it is far higher in a ranking that admits the Coding Agent Index. Unrewarded share (E203): beside it the summary prints the median share of basket cost carried by admitted components with no quality leaf (AA-Briefcase and GDP.pdf), so a reader sees how much of the price buys work the quality side does not credit. Inside the Coding Agent Index v2.0, SWE-Atlas QnA (124 of its 290 tasks) has no quality leaf either; while the index is admitted its cost share is published as not separable, because AA publishes one pooled cost for the index, and it is never omitted from the disclosure; no score changes (O6, O15). Exact model-and-effort cost today: Coding Agent Index v2.0 for 8 of the max-effort ranking's 9 rows and 3 of the AI Coding Daily ranking's 16, each complete under O27 by construction (the cost is AA's per-task mean × 290, and AA's agent page carries no declined-task marker; its blocked and fallback attempts are flagged under O63, not counted as declined); ITBench-AA 2 of 9 and 0 of 16. The seven AA Index SDLC evaluations are confirmed complete for every ranked row of both rankings (each row's ten Index evaluation costs reproduce AA's published total, E209). Under the admission rule, today the max-effort ranking's basket v1 = 8 of the 10 target components (the seven Index evaluations and the Coding Agent Index v2.0) and the AI Coding Daily ranking's 7 of 10 (the seven Index evaluations; the Coding Agent Index v2.0 pending, E254); ITBench-AA is "pending capture" in both. In the max-effort ranking the subset workload rows (MiMo-V2.6-Pro) are each scored on their own subset (the seven Index evaluations), flagged "subset cost" (O17, E254).

Last 12 words: "on the Plan basis the workload question is the M_W identification status."

Part 4 — first line:

Plan cost input (full-utilisation effective cost, labelled) = API cost input ÷ Value Multiple of the selected route. Computed per model–plan tier–surface–configuration route (tier and fee are part of route identity and published). Measurement objects (E111): each controlled measurement and each complete concordant report partition (E107) is a measurement object m = (route ID, partition ID, report IDs, measurement workload, valuation basis, allocation regime, measurement dates, identification object);

Last 12 words: "for other Claude models; the transfers keep their assumption label and caution."

Both parts read to their end; the review proceeds.

1. Findings by severity

Critical

None.

High

The O116 FrontierCode stand-in is unaccounted for in the AI Coding Daily ranking's admission summary. Part 3 defines the admission units as "nine since FrontierCode's cost moved inside the Coding Agent Index v2.0, plus FrontierCode's O116 stand-in, which enters only in the index's place", and O116 mandates a double selection ("selection first without it, then with it in the index's place") in any ranking that has not admitted the index. But the AI Coding Daily admission summary reports only the without-stand-in outcome: "admits 7 on a reference panel of 16 rows … and the Coding Agent Index v2.0 (3 of 16) stays pending", with the pending list naming only the index and ITBench-AA. If the stand-in passes the ⌈2·16/3⌉ = 11 threshold, that ranking's cost workload should be 8 components, not 7 — every AICD cost score would be computed on the wrong basket; if it fails, it must appear in the pending list like the index does. Either way the published admission object is incomplete and the reader cannot verify which basket the AICD ranking's costs are summed over. Change: state the with-stand-in selection outcome for the AI Coding Daily ranking explicitly (admitted count, panel, coverage n/16, or "pending, n/16"), and make the build emit one status line per registered unit per ranking — admitted, pending with coverage, or not-applicable (index admitted) — so no unit can silently vanish from the admission object.

Medium

The report-pooling rule in part 4 omits O115/E271's midpoint clip, producing two divergent pooling rules for range-valued reports. Part 4 states: "concordant reports are then pooled by geometric mean." O115 (adopted, 2026-10-29) says a passing cell "clips each report midpoint to the concordance band [largest lower / 1.20, 1.20 × smallest upper] before pooling (E271)". For point reports the clip is a no-op (concordance already places every x_k inside the band), but for range-valued reports the geometric mean of raw midpoints and the geometric mean of clipped midpoints differ, so an implementer following part 4's sentence and one following E271 produce different displayed Plan scores and different multiples. Change: make the pooling sentence the single normative statement of the composed rule — (i) O86 concordance on unpooled values, (ii) clip each range-valued report's midpoint to the band, (iii) geometric mean of the clipped values — and cross-reference E271 there, or state that E271 governs and E33's sentence is its summary.

No procedure or cadence is stated for detecting a revision of the selected paywalled SemiAnalysis article at the same URL. E238 correctly says a same-URL change is scoped change detection (E18) with new measurements staying diagnostic until re-selection, and the transcription is hashed in the evidence bundle. But the only scheduled watching described is "a weekly scheduled search of the web, SemiAnalysis's newsletter and its X accounts (report-only)" — i.e., detection of later analyses, not of in-place figure changes to the selected one; and "the article itself is not captured in the evidence bundle, so no content hash is published." Without a re-read step, a revised figure for an already-measured model, or an O40 "added after selection" row, can go undetected indefinitely, and the E151 clocks that should restart from a revision date never do. This hurts the objective because the entire Plan evidence layer (currently 100% SemiAnalysis) keys its staleness and change-detection machinery off that article's state. Change: add a weekly re-transcription step: a reader with access re-reads the article's figure table, the build diffs the transcription against the hashed plan_cost_routes.json sourceEvidence.semianalysis entry, and any diff is logged and treated as E18 scoped change detection; publish a "last checked, no change" log entry each week so the negative results are auditable.

Comparator key 1 does not state the identification class of assumption-graded routes, creating a latent conflict with O73. Key 1 ranks identification class (point > set > unidentified) before key 2 ranks evidence grade (controlled measurement > O88 route ≥ ≥2 concordant reports > owner assumption). An owner-named transfer or an O46 quota ceiling carries a point-valued multiple; a report pair that only establishes a lower bound (E139: observed-usage multiple, capacity not established) is at best set-identified. If assumption-graded routes are classified point-identified, key 1 selects the transfer over the measured reports — directly contradicting O73's rule that "reports replace only assumption or fallback routes." If they are classified unidentified, the design is consistent, but the draft never says which. Change: publish a small mapping table in the comparator spec — route grade × identification class — and state explicitly that owner-named transfers and O46 ceilings are unidentified at key 1 (they identify nothing about M_W; their point value enters only at key 3 as the observed/named multiple), which preserves O73 and the owner's highest-eligible rule.

Low

The admission object does not publish the enumeration unit count, so the "feasible alternatives" figures (255 and 127) cannot be audited. The counts are the only published trace of the 2ⁿ enumeration, and n itself is ranking-dependent (nine units where the index is admitted, ten with the O116 stand-in where it is not). Change: add the unit count and the enumeration size (2ⁿ − 1) to the published admission object per ranking.

E139's measurement_capacity_status is written as a slash-separated run-on ("capacity established … / eligible delivered consumption observed, capacity not established / saturation unverified / provider quota ceiling, full use of the quota assumed …"), which reads ambiguously — it is unclear whether "eligible delivered consumption observed" is a status or a preamble to "capacity not established." A build-checked enum list with one name per status would remove the parsing ambiguity for implementers.

2. Methodology design recommendations

Prioritized:

Comparator grade/class table (fixes Medium 3). Add to the E85 comparator spec a two-column mapping: for each evidence grade (controlled measurement; O88 cross-effort; ≥2 concordant reports; owner transfer; O46 ceiling), its fixed key-1 class — measured point / measured set / unidentified — with assumption-graded routes pinned to "unidentified". This is a one-table change, implementable from existing data, and removes the O73 conflict without touching the owner's key-3 highest-eligible rule.

Standing selected-article watch protocol (fixes Medium 2). A weekly job with three outputs: (a) the new-analysis search already described; (b) a re-transcription diff of the selected article's figure table against the hashed sourceEvidence.semianalysis record; (c) a dated negative-result log line ("checked YYYY-MM-DD, no change") stored with the release evidence. Any (b) diff emits an E18 event with the changed (plan, model) cells enumerated, demoting exactly those measurements to diagnostic pending re-selection. All of this is refreshable from the authorized source and auditable from the evidence bundle.

Per-unit admission manifest (fixes High 1). Extend the admission object from "admitted components + pending list" to a full unit-status manifest: for each registered unit (the nine targets plus the O116 stand-in where applicable), one row with status ∈ {admitted, pending, excluded-by-selection}, coverage n/N, and panel membership. The build fails if a registered unit has no row in any ranking's manifest. This turns the O116 double selection from prose into a checkable artifact.

Single normative pooling sentence (fixes Medium 1). Consolidate E33/O86/O115/E271 into one rule stated once and referenced everywhere: concordance test on unpooled values → clip range midpoints to the concordance band → geometric mean of clipped values; point reports pass through the clip unchanged (provably inside the band under concordance).

3. Questions for the owner

What identification class (key 1) do you intend for owner-named transfers and O46 quota ceilings — point-identified or unidentified? (If point-identified, O73's report-replacement rule is unreachable whenever the competing report pair is only set-identified, and I would push the grade/class table in recommendation 1.)

Should the FrontierCode O116 stand-in be in the AI Coding Daily basket at this release, and what was the with-stand-in selection outcome (admitted at 8 components, or pending below the 11-row threshold)? This determines whether the AICD cost workload is currently correct as published.

Is there any existing step that re-reads the paywalled selected article itself (as opposed to searching for later analyses), and if so at what cadence? If not, do you accept recommendation 2's weekly re-transcription diff?

4. Verdict

VERDICT: HAS FEEDBACK