0. Read check

Read all four listed parts to their ends, in order, at commit 8cbc853b5cf9f5665ee354d68fae165ab1566856. This is a sectional review only. References below identify the part and governing rule in the files read.

Part 6

First line:

Value Multiple = API-priced usage a plan delivers over a stated fee period ÷ fee for that period. Each multiple records fee period, workload, model/effort, token categories (input, cache read/write, reasoning, output), valuation price list and date, shared usage pools, whether capacity was exhausted and which rate-limit windows bound it. Valuation compatibility (E138, applying E106 and E123): each measurement records its valuation basis — already on the row's valuation basis (E170: the tariff in force at the release valuation timestamp V, or, for a row whose AA cost applied a price not in force at V, that applied price under O29): it continues to the workload-identification checks, and an otherwise eligible workload-unmatched measurement stays scored under O16; revalued from a compatible public consumption ledger: it continues with the revalued multiple; on a different basis that cannot be revalued: diagnostic-only (E106 case 4), supplying neither an official score nor an anchor observation; basis not recorded: displayed with the flag "valuation basis unverified" until the registry records it, never interval-eligible (O7 excludes established mismatches; a missing record is not treated as one). The absence of a token ledger alone never decides price-basis compatibility (fixture: two routes with the same measured multiple, one on the release basis and one on an unreconcilable older basis, receive different official-admission outcomes). Where M_W is unidentified (E32) the row is excluded from Plan interval outputs. No extrapolation of short bursts to a billing period unless the controlled measurement establishes it; a report's meter fraction measures the allowance of its own window (E270); a 5-hour figure pools only with 5-hour figures of the same plan and model and never converts to a billing period, so it never admits a route (owner decision O82, 2026-10-28, replacing O80's exception), and a weekly allowance converts to a month at 52/12 weeks (4.333…; reviewer 77); usage is never extrapolated. Evidence rules unchanged except for two owner exceptions, the O46 MiMo quota ceilings and the O76 speed-mode conversion of a user report (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

Last 12 words:

value; no epsilon is introduced. Domain validity is separate from evidence completeness.

Part 7

First line:

Scoring with frozen, per-basis anchors in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); anchor object (E20), identified by anchor version, basis and workload hash (the hash covers the workload's component set only, so two rankings' workloads with the same components share a hash but are different anchor objects with different references and anchors, and equal hashes imply no comparability across rankings): reference configuration ids and frozen costs, the references chosen by the registered anchor-panel policy (E160) — distinct from workload admission even where it coincides: the ranked configurations with complete cost evidence (exact cost, no AA missing- or declined-task marker) on every component of the workload at the freeze cutoff (on the main workload, the admission reference panel), on the Plan basis the plan rows of the same configurations whose displayed Plan cost is measured (a controlled measurement or concordant reports; owner decision O157, 2026-11-01, on reviewer 78, amending E160 and E253): owner assumptions and API-cost fallbacks are scored on those anchors and flagged (O13, O16) but are outside the Plan clip-gate population (scores.json gates.clip.plan[].outsideGate), because API fallbacks cost an order of magnitude more than plan routes and, as references, had stretched the Plan anchor range until every measured row sat in a narrow band of cost scores (at r160 the max-effort Plan high anchor was twice one API fallback; the O12 dual run against the r160 anchors is published in data/v3_dual_run*.json, anchor version v3-2026-11-01-a3); at least two references, otherwise that workload's anchors are unavailable and its configurations get no cost score (the main workload must meet the minimum, or freezing fails); anchor availability after the valuation gate (E184): a reference must also pass the valuation-basis gate (E170 outcome 1 or 2) at its freeze; a frozen anchor object keeps its references when one later fails the gate (as with any evidence lost after freezing), and a new freeze leaves out a row whose AA cost omits a pricing term (O94); a subset workload left with fewer than two eligible references takes the unavailable state above; and a main-workload migration whose new workload would have fewer than two eligible references is deferred — the release publishes on the current anchor version and admitted set, the component that would have been admitted stays pending with the reason "anchor migration unavailable — insufficient valuation-eligible references", and the release is not held (O29), because anchors from the old workload are never relabelled for a new one; a workload migration is atomic across bases — both bases share the workload object and E160's reference configurations (the Plan references are the measured plan rows of the same configurations, O48, O157); because O157 needs at least two measured plan rows, the two bases' availability can differ, so the migration requires both, at least two complete-evidence API references and at least two measured Plan references on the main workload, and otherwise the freeze stops and the previous anchor objects stay in force for both bases (E304, on reviewer 80; fixtures: two API references with one measured Plan reference, and with none, each stopping the freeze); the shared eligibility is complete cost evidence on every component, an E170 outcome of 1 or 2 for the configuration's AA cost and, from the next freeze, no O94 pricing omission, and the selected Plan evidence's own valuation status (E138) governs Plan interval eligibility, never anchor eligibility, because E160's Plan anchors are the measured plan rows (O157), and the rows they do not cover are scored on them, flagged and outside the clip gate; each freeze publishes a row-level anchor-eligibility table (complete evidence, valuation-gate outcome, eligibility and exclusion reason); the first freeze of a new methodology version that cannot anchor its main workload is not released and the previous version's release stays live (a versioned migration completes only with its anchors, O12), while a subset workload takes the unavailable state; fixtures: a superseded row inside a frozen anchor panel leaves the anchor unchanged; a freeze excludes superseded and unverified rows; a deferred migration keeps the prior workload and lists the pending component; a first freeze short of references is refused; IDs and costs stay frozen, evidence lost after freezing never rebuilds an anchor, and any population or rule change is a new anchor version with an old/new bridge (fixtures: reordered input rows give identical anchors; an unresolved component removes a row from the population; a subset workload below the minimum leaves its rows unscored without disturbing the main gates); c_L = min reference cost ÷ 2 and c_H = max reference cost × 2 (a fixed ln 2 log padding, so the reference cohort itself never clips); units; expected clipping (none for the reference cohort). A first-release fixture on the actual reference cohort must pass without re-anchoring. Dollars always displayed; unclipped values kept. Clip gate (single governing gate): per basis and anchor object, hold the release (O12) when more than max(1, 10% of n) rows clip, where n is the number of ranked rows scored on that anchor object (ranked rows on its workload with a positive cost on that basis; a subset workload is gated on its own anchor object), or when any such ranked row lies beyond an anchor by more than a factor of 2. Listed rows beyond the anchors (O58): a listed configuration (E259) is not in the gate's population and never holds a release, because it has no rank and no label; the gate output discloses each listed row whose cost lies outside its workload's anchors, with its basis, side, factor, whether it passes the factor-2 limit, and whether it is a point on AA's rendered frontier (the E197 entrant case, now visible rather than held). Today, in the max-effort ranking, API: GPT-6 Luna (low) 7.10 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (medium) 1.54 below the low anchor (rendered-frontier point); Claude Haiku 5.5 (low) 1.53 below the low anchor (rendered-frontier point); Plan: Claude Haiku 5.5 (low) 70.65 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (low) 59.81 below the low anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (medium) 38.91 below the low anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (high) 24.11 below the low anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (xhigh) 15.85 below the low anchor (past the factor-2 limit); GPT-6 Luna (medium) 13.01 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (high) 8.36 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (xhigh) 6.22 below the low anchor (past the factor-2 limit); Gemini 4 Carbon (high) 4.74 above the high anchor (rendered-frontier point, past the factor-2 limit); GPT-6.1 Terra (low) 4.27 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6.1 Terra (medium) 2.40 below the low anchor (rendered-frontier point, past the factor-2 limit); Kimi K3.1 Pro (max) 2.24 above the high anchor (past the factor-2 limit); GPT-6.1 Sol (low) 2.13 below the low anchor (past the factor-2 limit); GPT-6.1 Terra (high) 1.76 below the low anchor (rendered-frontier point); Claude Opus 5.5 (medium) 1.39 below the low anchor; GPT-6.1 Sol (medium) 1.32 below the low anchor (rendered-frontier point); GPT-6.1 Terra (xhigh) 1.31 below the low anchor; Claude Opus 5.5 (high) 1.05 below the low anchor. In the AI Coding Daily ranking, API: GPT-6 Luna (low) 2.30 below the low anchor (rendered-frontier point, past the factor-2 limit); Plan: Claude Haiku 5.5 (low) 16.58 below the low anchor (rendered-frontier point, past the factor-2 limit); GPT-6 Luna (low) 14.03 below the low anchor (rendered-frontier point, past the factor-2 limit); Gemini 4 Carbon (high) 8.17 above the high anchor (rendered-frontier point, past the factor-2 limit); Claude Haiku 5.5 (xhigh) 3.72 below the low anchor (past the factor-2 limit); Claude Haiku 5.5 (max) 2.25 below the low anchor (past the factor-2 limit); GPT-6.1 Terra (low) 1.06 below the low anchor (rendered-frontier point). Gate scope (E262): every gate runs per ranking on that ranking's own anchor objects and rows; both rankings publish together, so a hold in either holds the release, and the release record names the held rankings (scores.json releaseHold). A held release (E200) is still built. Its manifest names each clipped row, including a frontier entrant, with its unclipped cost and score and the flag "off-anchor scale, release held", and the entrant stays in the reconciliation inventory. That output is published with the dual run that clears the hold. Re-anchoring path (E197): the gate's remedy is pre-built. Anchors stay over a ranking's ranked rows (listed rows are disclosed, O58); a newly ranked row beyond them that holds the gate is cleared only by the O12 versioned re-freeze with its dual run, and the gate output names that remedy (owner decision O120, 2026-10-29). The freeze command re-freezes on the release's evidence, and the dual-run command scores that same evidence on the previous and the new anchor objects. It publishes each row's cost score, value and rank under both, and each bar's result under both bar objects (O12), so a cheaper entrant beyond the low anchor can clear the gate within one release cycle as a versioned migration. Re-freeze at the moved cutoff (owner decision O47, E247, E253): AA published FrontierCode results after the 2026-10-21 cutoff, and the owner chose "Move cutoff now": the release cutoff moved to that day's new capture instant, every AA source was re-captured and the anchors were re-frozen. No dual run was possible, because the main workload changed (Coding Agent Index v1 left the basket when AA replaced it with v2.0), so this is a workload migration (E184) and the engine refuses to score on the previous anchors; the previous anchor object is kept as v3-frozen-2026-10-21-before-o47.json. AA data after the cutoff (owner decision O65, 2026-10-25): AA data read after the release cutoff is never merged into a pinned capture; it moves the cutoff, every AA source is re-captured and the anchors are re-frozen. On 2026-10-25 this moved the cutoff from 2026-10-23T06:26:23Z (the safety-refusal counts of O63 had been read later that day) to the new capture instant; the re-capture added Kimi K3.1 Pro as a rendered-frontier vertex. Because the main workload of each ranking did not change, a dual run on the previous and the new anchors was possible and is published (data/v3_dual_run.json, data/v3_dual_run_aicd.json; the previous objects are kept as v3-frozen-2026-10-23-before-o65.json and v3-frozen-aicd-2026-10-23-before-o65.json). Board re-read (owner decision O68, 2026-10-25): with the cutoff moved, every board either ranking uses was re-read (Vals' two boards, AI Coding Daily with its hidden older rows, Bug Hunt Bench's scoreboard and LiveBench 2.0's 2026-10-23 release in full; tbench.ai's Terminal-Bench 4.0 leaderboard and Cognition's FrontierCode board re-read and found unchanged, so their 2026-10-23 captures stand), each kept only when its own last update predates the cutoff's day (O60); every reviewed match is kept, the build stops if a matched row vanished or changed effort, and on 2026-10-25 the only changes were Kimi K3.1 Pro's new rows and LiveBench's new release (research/2026-10-25-board-reread/). Re-capture under Intelligence Index v5 (owner decision O132, 2026-10-30): AA published Intelligence Index v5.0 around 2026-10-27, after the 2026-10-25 cutoff, and the owner chose to re-capture under v5 now: under O65 the cutoff moved to 2026-11-01T06:10:00Z, every AA source was re-captured (the chart at 2026-11-01T05:53:05Z), the leaves were mapped to their v5 successors (O136) and the basket re-decided (O137), and every ranking's anchors were re-frozen on the v5 cohort (anchor versions below). As at O47, the main workload of each ranking changed (GDPval-AA, SciCode and AA-LCR left the basket; FrontierCode 2.0 and Terminal-Bench-Science joined it), so this is a workload migration (E184) with no dual run on the previous anchors; the previous anchor objects are kept in research/2026-10-30-v5-recapture/previous-anchors/, and the published dual-run files still describe the O65 move of 2026-10-25. Every board was re-read on 2026-11-01 for the 37-configuration cohort (O68, O145; research/2026-11-01-recapture/third-party/), and earlier on 2026-10-30 (research/2026-10-30-v5-recapture/third-party/): LiveBench had withdrawn its 2026-10-23 release, so its 2026-10-25 release is pinned (O139); Vals, Bug Hunt and AI Coding Daily added GPT-6.1 Terra rows (Vals also Gemini 4 Carbon) and changed no other cohort value; tbench.ai was unchanged; and no board row is dated after the v5 chart capture. E247's freeze at O47 over the 29-configuration cohort (anchor version v3-2026-10-23, API 4.19 to 12,078 USD on 27 references at O47) was replaced before any release by one frozen object per ranking (E253): the max-effort ranking's version string is v3-2026-11-01-a3 and the AI Coding Daily ranking's is v3-2026-11-01-a3-aicd, each padded (c_L = cheapest reference ÷ 2, c_H = dearest × 2) per workload and basis, with every anchor object's references and anchors in scores.json workloads. Today a cost doubling is worth 3.11 value points (offset by 4.14 quality points) on the max-effort API basis and 5.31 (7.08) on its Plan basis, and 2.71 (3.61) on the AI Coding Daily API basis and 4.11 (5.48) on its Plan basis.

Last 12 words:

| points of 60; z = 100 × points / 60 |

Part 8

First line:

| General professional work (20%) | GDPval-AA v2.1 (Elo as displayed on AA's model page at the capture; E90, O70) | 10% | 10% | 10% | z = 100 × clip((E − 500)/2000, 0, 1) (AA's published integration transform "clamp((Elo − 500) / 2000)", artificialanalysis.ai/methodology/intelligence-benchmarking, verified 2026-10-19 (E129)); specification-layer sensitivity (E181): logistic win probability against AA's pinned scale anchor, z = 100 / (1 + 10^((E_A − E)/400)) with E_A = 1600 (DeepSeek V4.1 Flash (max), AA's anchor, pinned on 2026-10-19 from AA's methodology page; a change of AA's anchor is a versioned re-pinning, not a silent move) and the conventional Elo scale of 400 points per tenfold odds (AA does not state its scale factor), published as rank changes on the common panel with every other input fixed |

Last 12 words:

a bias bound in the identification layer); repetitions are not a bias.

Part 9

First line is blank:

The first nonblank line is:

Uncertainty (three separate layers, one scenario engine)

Last 12 words:

not separable" and its S0 result is not described as target-workload support.

1. Findings by severity
Critical

None.

High

None.

Medium

The LiveBench uncertainty specification confuses a binomial observation model with the distribution of the published category scores. Issue: Part 9 describes LiveBench Overall as a weighted mean of seven binomial category shares, using category counts that include only four Reasoning parts and three Data Analysis parts. Part 8 says those parts contain several short questions, and treats the retained counts as an assumed wide reading. However, “part” scores containing several questions need not be binary. Applying the binomial Jeffreys construction to a fractional category score creates pseudo-successes rather than a posterior derived from binary observations. The draft already correctly treats other bounded, nonbinary metrics using a variance-bound approximation, making LiveBench’s treatment internally inconsistent. This concerns the likelihood, not merely the previously adopted task-count bracket. (Parts 8–9, E264, O142 and the S1T specification.) Why it hurts the objective: S1T helps contextualise ordinal ranks. Readers should be able to distinguish a posterior supported by binary outcomes from a conventional uncertainty kernel for an aggregate bounded score. Halving the assumed counts changes scale but does not resolve the observation-model mismatch. Concrete change: Record each LiveBench category’s scoring unit and outcome type. Use the Beta posterior only for categories documented as binary proportions. For categories scored as bounded question or part averages, use the already-defined bounded-score approximation, explicitly labelled conventional, unless captured per-unit outcomes support resampling. Preserve the existing count bracket and recentred alternative.

The generic “single governing” clip-gate definition does not incorporate the new Plan population exception. Issue: The beginning of part 7 explicitly excludes owner-assumption and API-fallback rows from the Plan clip-gate population under O157. Later in the same first line, the “single governing gate” defines 
𝑛
n as every ranked row with a positive cost on the anchor object, and the factor-of-two trigger applies to “any such ranked row.” Those generic definitions include the very rows excluded earlier. Owner precedence resolves the intended policy, so this is not a missing policy or a challenge to O157; it is a remaining inconsistency in the operative definition. (Part 7, E160/O157 and “Clip gate (single governing gate)”.) Why it hurts the objective: An independent implementation can calculate the clipping fraction with the wrong denominator or incorrectly hold a release because an assumption or fallback lies far outside the measured Plan anchors. Concrete change: Define one explicit gate population and use it in both triggers:

𝐺
𝑏
,
𝑊
=
{
𝑖
:
 
𝑖
 is ranked and scored on 
(
𝑏
,
𝑊
)
,
 
𝐶
𝑖
,
𝑏
>
0
,
 and 
𝑖
 passes the basis-specific gate-population rule
}
.
G
b,W
	​

={i: i is ranked and scored on (b,W), C
i,b
	​

>0, and i passes the basis-specific gate-population rule}.

For Plan, exclude the O157 assumption and fallback rows; for API, retain the stated ranked-row population. Set 
𝑛
=
∣
𝐺
𝑏
,
𝑊
∣
n=∣G
b,W
	​

∣, and evaluate both the clipping count and factor-of-two condition exclusively over 
𝐺
𝑏
,
𝑊
G
b,W
	​

.

Low

One current-status sentence contradicts the adopted retention rule. Issue: Part 8 first says MiniMax-M3.1-Flash is taken at max under O148, then says it “left the cohort at the v5 re-capture.” Part 7 describes the subsequent 37-configuration cohort under O145, and the supplied ledger specifies retention for one release after frontier/near-gap exit. The sentence appears to preserve an earlier historical status without identifying it as historical. (Part 8, “Added leaves,” O135/O148; part 7, O145 recapture description.) Why it hurts the objective: Readers can mistake an eligible retained configuration for a configuration outside the release’s comparison universe. Concrete change: Replace the sentence with the current build-derived state, distinguishing “left the plotted frontier/near set” from “left the cohort.” If historical context is useful, include the relevant cutoff and its subsequent retained status.

2. Methodology design recommendations

Prioritise a typed observation-model field for every S1T leaf and LiveBench subcategory. Extend the existing kernel object rather than adding a new uncertainty layer:

outcome_type: binary / bounded fractional / count / fitted rating.

sampling_unit: question / part / project / task / run.

likelihood_status: source-supported / conventional approximation.

effective_count_basis: source count and release, or explicitly retained assumption.

Have the compiler reject a binary-posterior kernel for a bounded-fractional observation unless a recorded justification supports that interpretation. This implements the distinction already present for FrontierCode, AutomationBench and AI Coding Daily, without changing scores, weights, exact-variant admission or the owner’s uncertainty-layer policy. (Parts 8–9, E25, E58, E263–E264 and O142.)

Compile the clip-gate population once and render all normative gate descriptions from it. Publish, per anchor object, the included IDs, excluded IDs with reasons, denominator, clipped count and maximum excursion. Add regression fixtures where:

an excluded API fallback lies more than twice above the Plan high anchor but cannot hold the release;

an excluded transfer lies below the low anchor but cannot alter the gate denominator;

a measured Plan row crosses the factor-of-two threshold and does hold the release.

This is implementation alignment with O157, not a proposal to change the gate’s thresholds or anchor policy. (Part 7, O157, E262 and the clip-gate definition.)

Render cohort-state statements from the same retained/plotted classification used by reconciliation. Use distinct statuses for plotted-frontier, plotted-near, retained-this-release and outside-cohort. Historical explanatory prose should name its cutoff. This prevents a stale sentence from contradicting the otherwise build-derived current release. (Parts 7–8, O145/O148.)

3. Questions for the owner

None. These changes can be implemented without revisiting the binding policy decisions.

4. Verdict

VERDICT: HAS FEEDBACK