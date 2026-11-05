0. Read check

Part 13 (draft-r160-part-13-of-14.md), read to its end.

First line: ## Governance

Last 12 words: "DeepSeek V4.1 Flash 1017 and MiniMax-M3.1-Flash, both then new to the chart;"

Part 14 (draft-r160-part-14-of-14.md), read to its end.

First line: "the capture's comparison record is in data/aa_frontier_capture.json." (the part opens mid-sentence, continuing part 13's closing sentence about the cohort capture)

Last 12 words: "(not normative); it is in draft-r160.md in the same folder of the repository."

Both listed parts were read to their end.

1. Findings by severity

Critical

None.

High

Mutually inconsistent coverage figures in Known limitations (part 14). The draft states that the max-effort ranking ranks "9 of the 27 cohort configurations", the AI Coding Daily ranking 20, and "12 are in neither", while the two-ranking agreement check reads "undefined (panel too small) on a panel of 4". These cannot all be true: with a 27-row cohort, 12 in neither implies 15 covered, so the two rankings would share 9 + 20 − 15 = 14 configurations — above E41's floor of eight, so the τ_b check would be published, not undefined on a panel of 4. With a 37-row cohort the arithmetic closes exactly (9 + 20 − (37 − 12) = 4 shared, matching the named panel of DeepSeek V4.1 Flash 1017 (max), Gemini 4 Argon (high), GPT-6 Luna (max) and MiMo-V2.6-Pro), and the ledger records O145 as applied at the 2026-11-01 cutoff with a 37-configuration cohort, fed by the capture part 13 dates at 2026-11-01T05:53:05Z. So the "27" is almost certainly stale (O132's cohort). Why it hurts: coverage disclosure is a core honesty output of the ranking, any reader can check the naive sum (9 + 20 + 12 = 41 mentions over a claimed 27 rows), and it directly contradicts E265's promise that every current-release figure is rendered from data/scores.json and linted — the draft's own rule says a stale figure found after E265 is a bug in the check to be fixed. Concrete change: correct the cohort figure, and add a build invariant that computes cohort, both rankings' ranked counts, the shared count and the "neither" count from one scores.json object and asserts cohort = |union| + neither and shared = ranked₁ + ranked₂ − |union|, so these figures can never disagree; then investigate why the E265 lint passed (a stale field resolved cleanly, or the sentence escaped the lint's sentence classes).

Medium

Expired and fault-window Plan routes deny labels with no staleness hull (Owner decision challenge to O118/O119). The lifecycle table has in-grace (91–120 day) routes and accounting-fault routes compete as blockers "that can deny another row a label but earn none", at their published record. New argument: the draft already gives API-cost uncertainty explicit hulls for exactly parallel situations — O94 rows compete over [C, factor × C], O98 over [C, ∞), E185 publishes current-tariff bounds, and E276 puts shared tariff factors on blockers — but a Plan row whose evidence is 91–120 days old blocks at a single point, even though the expiry itself is the signal that the record may no longer hold. With 21 of 27 and 60 of 67 plan rows flagged possibly-superseded or expired, Plan label outcomes may be dominated by stale blockers. And the failure direction is not the safe one: if the expired row's price rose after measurement, the labeled row's "cheapest above bar" claim was true and is wrongly withheld. Concrete change: an expired or fault-window Plan blocker denies a label only if it still undercuts the labeled row at the upper end of a staleness hull — the E185 Plan bound P ∈ [P·min r ÷ max r, P·max r ÷ min r] where tariff records allow, else a disclosed drift factor per day expired capped at the grace end — or, more simply, end blocker status at the 90-day expiry rather than carrying it through grace.

The O112/O131 reset exclusion makes OpenAI Plan rows structurally unrepairable (Owner decision challenge to O112/O131). Part 14 records that OpenAI's global meter resets come about every two days, so only readings wholly between two resets count, weekly readings almost always span one, and the draft itself concedes flagged OpenAI routes are unlikely ever to be replaced by a report pair before demotion at 121 days — their only exits are a new controlled measurement or a provider announcement. New argument: O110's own principle treats a change dated inside a measurement's span as part of the measured regime, because that is the regime the user actually experienced; a periodic, publicly documented global reset is likewise part of every user's regime, so a reading spanning resets is representative of typical use, not contaminated evidence. Excluding it admits only sub-two-day windows and creates a coverage bias in the Plan view (OpenAI rows drift to flagged → no labels → API-cost fallback, mispricing ChatGPT plans relative to providers with friendlier meters), which is worse than a conservative flag. Concrete change: admit reset-spanning readings when every spanned reset instant is documented in the registry (the O83/O99 record taxonomy already has a "reset" type, and the reset dates are already listed), treated as part of the regime per the O110 logic, flagged "measured across documented meter resets", still subject to O11 independence, O85 and O86 concordance; or, if the exclusion stands, publish a per-provider repairability disclosure beside the Plan table so readers see which rows can never be repaired under current rules.

Low

Self-contradictory wording in E62 (part 14). The matched-panel rule says "a tbench.ai Terminal-Bench gap fill is not counted, its leaf staying AA-run by its named source" — but a tbench.ai-filled leaf is by definition not AA-run (O37/E37 assign tbench.ai as the gap-filler). As written the clause asserts both. Recommend rewording to: "the leaf keeps its named source; a tbench.ai fill is not counted as an independently executed leaf for the matched panel."

"GPT-6 Luna (max)" in the τb panel list appears nowhere else. Every other reference in these parts and the ledger is GPT-5.6 Luna (part 13 says GPT-5.6 Luna at low left the cohort; O30 ranks GPT-5.6 Luna at max). If this is a rendering typo, the E265 configuration-name lint has a hole; verify the name against scores.json and, if wrong, fold the fix into the High finding's lint repair.

Scenario-engine determinism rests on weaker guarantees than the text implies. The draft pins "Python's random module, the Mersenne Twister, under the Python versions the build is tested on", which is a pragmatic mitigation; however, per the Python documentation, only random() with a compatible seeder is guaranteed to produce the same sequence across Python versions — most of the module's other algorithms and seeding functions are explicitly subject to change between versions, a difference also observed historically for randint while random() stayed stable. Since O142 draws S1T leaves from a Beta posterior (a betavariate-class sampler) and other leaves use clipped normals, version drift could silently change published scenario shares on a Python upgrade. The archived per-stratum data files already protect published results; recommend additionally deriving every sampler from random.random() only (in-repo inverse-CDF or Box–Muller transforms) and recording the exact Python version beside the seed in the evidence bundle. If threads are ever used, note that random.gauss has a documented same-value race under concurrent calls; normalvariate is the thread-safe alternative.
docs.python
+1

Freshness asymmetry for the AA model-page snapshot (E216). The snapshot gate is 45 days while non-AA quality sources are held to 30 days (O59). Under O65 the snapshot is minutes old, so this binds only if the two are ever decoupled — but if they are, AA per-configuration costs and leaf values could be 50% staler than the non-AA leaves they sit beside. Consider aligning to 30 days or recording the rationale for 45.

2. Methodology design recommendations

Prioritised, all implementable from public data refreshed routinely:

Coverage-arithmetic invariant (fixes the High finding). One scores.json object holds cohort_n, ranked_max, ranked_aicd, shared (the same field the τ_b panel uses) and neither; the build asserts cohort_n = ranked_max + ranked_aicd − shared + neither and fails otherwise; every Known-limitations coverage sentence renders from that object; the E265 lint gains a rule that any "N of M" cohort count in a today-sentence must match the invariant's fields. This makes the class of inconsistency found structurally impossible rather than lint-hunted.

Staleness hull for expired/fault-window Plan blockers (the O118 challenge). Blocker denial cost C_block = max(C_published, U), where U is the upper end of the E185 Plan bound P·max r ÷ min r when tariff records permit, else C_published × (1 + d)^min(days_expired, 30) with d disclosed and calibrated from the observed frequency of typed limit/price change records (O83/O99) in the registry. Inputs are entirely the records the change-detection stage already collects; the hull is printed beside the denial so the label semantics ("denied even under the blocker's most expensive plausible current cost") are explicit.

Reset-regime admission test (the O112/O131 challenge). A reading spanning resets is admissible when (i) every spanned reset instant is a registered typed "reset" record, (ii) the report states its aggregation window, and (iii) O11 independence, O85 cell coverage and O86 concordance pass as usual; it carries the flag "measured across documented meter resets". If the owner keeps the exclusion, publish instead a per-provider × lifecycle-stage matrix (extending the E212 table and the aggregated 21/27, 60/67 counts) plus a repairability column, so the structural bias is at least visible per provider in the Plan view.

RNG hardening (the Low finding). Implement all scenario samplers on top of random.random() alone — the one primitive Python guarantees version-stable — with in-repo transforms (Box–Muller for normals, inverse-CDF or a documented rejection sampler for Beta draws); record seed, draw order and the exact Python version in the evidence bundle and in each released per-stratum data file header.
docs.python

Small-panel two-ranking agreement output. When the shared panel is below E41's floor, publish, beside "undefined (panel too small)", the named panel's per-row value ranks in both rankings and a concordant-pair count (for k = 4, the 6 pairs, each marked concordant/discordant). τ_b on four items takes very few attainable values, so a pair-level table conveys strictly more information at zero methodological cost, and it is purely descriptive like the τ_b it supplements.

3. Questions for the owner

For the current release, which figure is authoritative — the "27 cohort configurations" sentence, or the "12 are in neither" and panel-of-4 figures (the ledger's O145 record says 37 applied)? The answer determines whether the fix is a data refresh, an E265 lint repair, or both.

For the O118 challenge: does the change-record registry show any provider actually changing a plan limit or price while a route sat expired-in-grace in a past release? A zero history would weaken the drift-hull design and favour the cheaper "end blocker status at 90 days" option.

Is "GPT-6 Luna (max)" a distinct configuration, or a rendering of GPT-5.6 Luna (max)? If it is a typo, the configuration-name lint needs the same repair as the figure lint in the High finding.

4. Verdict

VERDICT: HAS FEEDBACK