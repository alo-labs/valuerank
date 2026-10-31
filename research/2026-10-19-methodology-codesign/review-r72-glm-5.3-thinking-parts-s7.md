0. Read check

Part 7 (draft-r154-part-7-of-13.md, read at commit d53cec1): first line begins — "- Scoring with frozen, per-basis anchors in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); anchor object (E20), identified by anchor version, basis and workload hash…" Last 12 words — "Daily on a harness chosen per model) are disclosed as a limitation."

The part was read to its end (it closes on the completed O10 paragraph ending the Quality section). All content below is reviewed strictly as stated in part 7.

1. Findings by severity

Critical

None.

High

LiveBench leaf has no stated effort-matching rule, in tension with the exact-variant policy. The leaf formula reads "LiveBench's own harness, one run per model at its top effort" with no rule reconciling LiveBench's per-model effort choice with each ranked row's effort configuration. The exact-variant rule (fixed policy: no transfer between efforts) is therefore either silently satisfied or silently violated, and the draft never says which. The risk is concrete, not theoretical: effort labels demonstrably diverge across boards — the tbench.ai board lists rows at mixed efforts (e.g. Opus 5 at xhigh, Grok 4.6 at high, GPT-5.6 Terra at max) with one row per model and agent — and ValueRank itself ranks MiMo-V2.6-Pro at high, its AA configuration (O54), while GPT-6 Astra is ranked at max, not xhigh (O30). If LiveBench ran a model at a setting other than the row's ranked effort, the 15% leaf is an unlabelled cross-effort transfer. Why it hurts: a 15% quality leaf built on non-matching evidence corrupts the 75% quality leg of the value score for affected rows and cannot be flagged because no mismatch detection exists. Recommended change: add a build-checked rule — the leaf is admitted only where LiveBench's run-effort label equals the row's ranked effort under a recorded effort-name mapping table (max/xhigh/high/etc. per provider); otherwise the leaf is missing under an O36-style logged search, or an owner-named labelled transfer (O4/O7 style). One sentence in the leaf formula plus a build check closes it.
tbench
+1

Medium

Plan-basis anchors are set partly on API prices (E160), mixing bases inside the Plan cost score. E160 includes API-cost fallback rows in the Plan anchor panel ("a narrower panel would clip them"). Consequence: c_L and c_H on the Plan basis — which feed the 25% cost leg of Plan value scores — are influenced by per-token API prices rather than subscription economics, so Plan rows' cost scores are comparable only within a mixture. This sits oddly beside the draft's otherwise meticulous valuation-basis typing (E170, E184, E202): every cost observation is typed by basis, yet the Plan anchor panel deliberately mixes them. E164's calibration diagnostic shows the effect but is not published as a score sensitivity. Recommended change: publish a per-release dual-anchor sensitivity — Plan cost scores and value ranks computed with anchors over (a) the full E160 panel and (b) the measured-Plan-only panel — labelled as a diagnostic, exactly as E234 does for FrontierCode sources. This changes no policy (the E160 panel stays) and is implementable from captured data.

Listed rows far outside the anchors can never affect bar or frontier claims, with no cross-family exposure check (Owner decision challenge to O58/E43). The gate output discloses listed rows beyond anchors — today including GPT-6 Luna (low) at 4.75× below the low API anchor and Claude Haiku 5.5 (low) at 3.41× below on Plan, both past the factor-2 limit, several of them rendered-frontier points. Under O58/E43 these rows stay outside every frontier and bar claim. If any listed row's indicative quality (E41) cleared a frozen bar at lower cost than the cheapest ranked qualifier, the published "cheapest above bar" output would be materially incomplete for buyers without any signal. E201 lists unevaluated cheaper same-family configurations only; the cross-family case is uncovered — that is the new argument. Recommended change: extend the E201-style bar output with one line per frozen bar: any listed row whose indicative quality exceeds the bar and whose cost is below the cheapest ranked qualifier, labelled "not ranked, not comparable". No ranking effect, no release hold, purely a claim-exposure bound.

Low

GDPval displayed-Elo drift is a moving target, bounded today but structural (Owner decision challenge to O70). Between the two most recent captures the displayed rating moved on 54 of 61 pages (−0.83 to +4.10 Elo) while Index totals moved on none, so a row's quality score changes between releases with no capability change. Today's largest ranked-row move is 0.21 z points / 0.015 value points — negligible — but drift scales with AA's refits and will increasingly enter cross-release comparisons (E177 swing attribution, O39 separability at ~3.3 value points). The gdpvalMovement diagnostic is good. Recommended change: add a row-level flag when a ranked row's GDPval move exceeds a fixed threshold (e.g. 1 z point) and name it automatically as an E177 cause.

Workload-hash semantics are confusing (E253). The draft notes the max-effort subset workload and the AI Coding Daily main workload "share hash 1453a9a0576b02ea but are different anchor objects," warning that equal hashes imply no comparability. If two genuinely different workloads hash identically, the reader cannot tell what the hash covers (cost components? cohort? basis-independent core?). Recommended change: one sentence stating the exact field set the workload hash is computed over, in the anchor-object definition.

Zero-cost rows are silently outside the clip gate, and a zero-cost reference would break the log anchors. The gate population is "ranked rows … with a positive cost on that basis," so a free plan (E185's unbounded case) drops out of n without statement. Worse, E160's reference panel requires "complete cost evidence," not positive cost — a zero-cost Plan reference would make c_L = 0 and ln c_L undefined in S_C. Recommended change: state that gate n excludes zero-cost rows, and add a build check that anchor references must have positive cost on their basis.

tbench.ai cross-check reports τb only, with no level offset. E229's cross-source agreement for Terminal-Bench publishes τ_b (0.74 on 5 rows) but no mean offset, unlike the FrontierCode analogue (E234: τ_b 0.73, Cognition +2.5 mean). A rank correlation on 5 rows cannot detect a uniform level shift, which is precisely what harness mixing causes; the tbench.ai board structure (model, agent, resolution rate, cost per row) supports the computation directly. Recommended change: publish the AA-vs-tbench.ai mean offset on the matched panel beside τ_b.
tbench

Verified without findings (so the owner can see these were checked): the Omniscience non-monotonicity example is arithmetically correct under N = abstention share among non-correct (98/1/1 → 82, 99/1/0 → 66), and the unanswered-or-partial share (1 − A)(1 − h) is algebraically consistent; the AI Coding Daily and Bug Hunt test vectors (52/105 → 49.52) check out; weight tables sum to 60/40/100 per ranking, the AA-run shares (66/34 and 78/22) recompute correctly, and the 51% coding-specific share matches 45 + 15 × (3.5/9); the LiveBench per-release data-file pattern (dated table files, one set per release) matches how LiveBench structures its published data, and GDPval-AA being an Elo aggregated from blind pairwise comparisons matches AA's design, consistent with the leaf's treatment.
artificialanalysis
+1

2. Methodology design recommendations

Prioritised, all implementable from captured public data:

LiveBench effort-match gate (highest priority, closes the High finding). Add to the leaf formula: leaf admitted iff effort_label(livebench_row) == effort_label(ranked_row) under a versioned effort-name mapping table stored in the registry; mismatch → missing leaf with a logged search (O36 pattern) or an owner-named labelled transfer. Build check fails on an unmapped effort label.

Plan dual-anchor sensitivity. Per release, publish Plan cost scores, value scores and ranks under the E160 panel and under a measured-Plan-only panel, with the row-level deltas and the number of rows whose rank changes. This is the E164 calibration promoted to a routine published sensitivity, and it quantifies exactly how much the fallback rows' API prices move the Plan ranking.

Cross-family listed-row bar-exposure listing. For each frozen bar H_k, list listed rows with indicative quality (E41) above H_k and cost below the cheapest ranked qualifier, labelled "not ranked, not comparable." Bounds the exposure of O58/E43 without touching the ranking.

tbench.ai mean-offset diagnostic. Beside E229's τ_b, publish the mean resolution-rate difference (tbench.ai − AA) on the matched panel, per ranking, mirroring E234. Where the matched panel is ≥5 rows, also publish it split by agent to support the E225 agent-preference rule.

Anchor-domain guards. Build checks: anchor references must have positive cost on their basis (log-domain safety); gate output states zero-cost rows are excluded from n.

GDPval drift row flag. Flag any ranked row whose displayed-Elo move exceeds 1 z point since the previous capture; feed the flag into E177's named-cause list so small-step swings stay attributed.

Workload-hash scope sentence in the E20/E253 anchor-object definition (what the hash covers and why two different workloads can share it).

3. Questions for the owner

For each row currently ranked in the max-effort ranking, does LiveBench 2.0's per-model "top effort" run use the same effort setting as the row's ranked configuration (including MiMo-V2.6-Pro at high and GPT-6 Astra at max)? If yes, a one-line statement plus a build check disposes of the High finding; if no, the choice between a missing leaf and a labelled transfer changes my recommendation.

Do any of today's listed rows beyond the anchors (e.g. GPT-6 Luna (low), Claude Haiku 5.5 (low)) exceed any frozen bar on their indicative E41 values? If none do, recommendation 3 is cosmetic; if one does, it is material to the cheapest-above-bar claim.

4. Verdict

VERDICT: HAS FEEDBACK