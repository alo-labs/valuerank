Both parts are now read in full. Before writing the review, I'll run one quick web check on the external facts my findings touch (Elo scale convention, Clopper–Pearson conservatism, and LiveBench's category-weighting practice).
0. Read check

Part 9 (draft-r178-part-9-of-15.md) — read to its end.

First line: | | AI Coding Daily (judged code quality on existing Laravel and React-TS repositories plus edge-case testing over six graded projects; the 10-point bug-finding column is excluded because it overlaps Bug Hunt; harness chosen per model and named on each record: Claude Code, Codex CLI, OpenCode, Devin or DeepSeek's harness; a configuration the board lists twice takes the row selected as in the added-leaves bullet) | — | 10% | — | points of 60; z = 100 × points / 60 |

Final sentence: "Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias."

Part 10 (draft-r178-part-10-of-15.md) — read to its end.

First line: ## Uncertainty (three separate layers, one scenario engine)

Final sentence: "Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support."

Both parts read fully; proceeding to the review.

1. Findings by severity

Critical
None.

High
None.

Medium

The AI Coding Daily leaf's harness confound is disclosed but never quantified. Part 9 states the AICD harness is "chosen per model and named on each record," and E268 even couples row selection to the Bug Hunt harness — so the leaf is a model-plus-harness composite, yet no cross-harness magnitude is published. Bug Hunt has exactly this diagnostic (E224 cross-harness list, e.g. Gemini 4 Argon 40.7 vs 33.0) and FrontierCode has E234's AA-vs-Cognition cross-check; AICD, a 10-point leaf in one of the two leading rankings, has none, even though the alternate rows are already captured in data/swe_tracks.json (alternates). This hurts the objective because a reader cannot judge whether the "exact configuration" comparability claim survives the harness choice. Recommended change: mirror E224 — publish every alternate harness row (harness name, points, test date) beside each AICD leaf that has one, and print the harness spread in leaf points with its value-point and rank effect via the existing E177/E334 replay machinery. No score change; implementable from the already-captured board data each release.

The GDPval-AA drift diagnostic is vacuous by construction and does not measure the estimand gap it names. Part 9 says the leaf "can differ from AA's own Index input by the drift accumulated since a configuration's addition," but the only empirical test is capture-to-capture movement, which today shows 0 of 27 pages moved — so the accumulated-since-addition divergence, the actual bias channel of O70, remains unquantified and the test "tests nothing" whenever consecutive captures are quiet (the draft concedes this in the reviewer-87 parenthetical). Recommended change, leaving O70 untouched: retain each ranked row's displayed Elo at its first ValueRank capture in the provenance record, and publish per row the divergence Δ Elo (first capture → current capture) with its z and value-point effect, plus the count of rows where that divergence exceeds the leaf's S1T SD. This converts a silently unbounded channel into a bounded, published one using only ValueRank's own captures of AA's public pages.

Low

The LiveBench S1T count bracket is one-sided. Part 9/10 read the SD from the kept 2026-10-14 task counts and bracket "the other end halves every category's count (SD × √2)". If the newer releases instead grew the task pool, the true SD is smaller than the published figure and lies outside the bracket. The uncovered direction is conservative (wider SD → fewer separability claims, larger noise margin), so severity is low, but the sentence "statements hold only as far as that bracket allows" overstates what the bracket covers. Recommended change: publish the two-sided bracket [SD/√2, SD/√2 × 2] (doubling and halving the counts) around the kept-count value, and state which direction is conservative; refresh the counts whenever a LiveBench category file publishes them (E264 already reads those files).

E268's fallback selection key inverts E206's philosophy. When no harness matches, the tie-break is "the row with the latest test date among all rows," which can select a smaller-sample row over a better-measured one — the opposite of E206's largest-sample rule for Bug Hunt on the same page. It is deterministic, disclosed and alternates are published, so this is minor. Recommended change: try largest-sample before latest-date in the fallback, or record the sample sizes of the passed-over rows beside the alternates.

Stale rationale figure. The GPQA retirement rationale cites "no value for 10 of 19 cohort rows in the 2026-10-17 snapshot" while the current cohort is 37 configurations. It is historical rationale, not a live claim, but under E265 (every current figure rendered from the build) a date-stamped phrasing would avoid it reading as a current figure.

2. Methodology design recommendations

Prioritised; all implementable from public, routinely refreshable data.

AICD harness-spread diagnostic (from Medium 1), extended to a named S2 stress. Beside each AICD leaf with alternates, publish {harness, points, test date, N where listed}; where a model has ≥ 2 harness rows, add the harness spread to scores.json diagnostics, and register a named S2 stress branch that draws the AICD leaf uniformly across its alternate-harness values — directly analogous to the existing "Bug Hunt harness band" named stress already listed among S2 branches, so the machinery and labelling conventions already exist.

GDPval first-capture divergence table (from Medium 2). Add firstCaptureElo to each row's GDPval provenance (the evidence bundle already retains capture hashes and digests); publish per ranked row Δ Elo, Δ z, Δ value points since first capture, and the share of rows whose divergence exceeds the leaf's S1T SD. Keeps O70's "displayed Elo at each cutoff" scoring rule exactly as is.

Two-sided LiveBench count bracket (from Low 1). Concretely: SD_low = SD_kept/√2 (all counts doubled), SD_high = SD_kept·√2 (all counts halved); print the separability threshold and noise-band contribution at both ends, and label the kept-count value's direction of conservatism.

Replace the Bonferroni–Clopper–Pearson sequential bounds with an alpha-spending or confidence-sequence alternative, dual-run first. The E77 rule (per-look equal-tailed Clopper–Pearson at δ = 0.05/16 over 16 looks) stacks two conservative layers: Clopper–Pearson over-covers by design, and Bonferroni spending is flat rather than matched to the look structure. E127 already concedes the rule is "not an anytime-valid confidence sequence" — what is new here is that a Lan–DeMets spending function or a beta-mixture confidence sequence keeps the identical 16 looks and the identical 90% label standard (lower bound ≥ 0.90) while narrowing the intervals, directly reducing "scenario threshold unresolved" outcomes. Recommended change: implement it as a dual run beside the current bounds for one release (as E197 does for re-anchoring) before any switch, so the label set is compared under both.
wikipedia
+1

3. Questions for the owner

For recommendation 1, should the AICD harness spread stay a leaf-beside diagnostic only, or also become a named S2 stress branch (which changes the stream registry and the S2 output surface)?

For recommendation 2, how many historical AA captures should the evidence bundle retain per row for the first-capture Elo table, and should the divergence be published cohort-wide or for ranked rows only?

4. Verdict

VERDICT: HAS FEEDBACK