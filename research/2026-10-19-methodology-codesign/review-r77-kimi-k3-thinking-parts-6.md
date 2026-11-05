I've read part 6. One possible integrity question came up — let me verify I'm seeing complete files by checking the part sizes in the directory before I certify the read check (single verification call so the read check is honest).
Part 8 read complete. Now part 9.
0. Read check

All four listed parts were opened through the GitHub connector (get_file_contents, commit a9de2d3) and each came back with a clean terminating sentence — nothing appears truncated:

Part 6 (draft-r159-part-6-of-14.md, SHA a7546727). First line: - **Assumptions**: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, a transfer with its donor measurement identified; neither identifies M_W. Last 12 words: "value; no epsilon is introduced. Domain validity is separate from evidence completeness."

Part 7 (draft-r159-part-7-of-14.md, SHA 9e9a11f3). First line: - **Scoring with frozen, per-basis anchors** in total-USD units, each ranking freezing its own anchor objects over its own cohort rows (E253): S_C = 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L), 0, 1); **anchor object (E20)**, identified by anchor version, basis and workload hash… Last 12 words: "(no value for 10 of 19 cohort rows in the 2026-10-17 snapshot)".

Part 8 (draft-r159-part-8-of-14.md, SHA 696778ea). First line: - **GDPval temporal estimand (E90, owner decision O70, 2026-10-25)**: the leaf is the GDPval-AA v2.1 Elo that AA's model page displays at the release's capture, the leaderboard value, which AA refits as models join. Last 12 words: "a bias bound in the identification layer); repetitions are not a bias."

Part 9 (draft-r159-part-9-of-14.md, SHA c331419a). First line: ## Uncertainty (three separate layers, one scenario engine). Last 12 words: "transport not separable" and its S0 result is not described as target-workload support."

All four parts were read to their ends; nothing is missing. Reading the full sections in the connector output (not snippets) is also how I verified the internal arithmetic I rely on below: the weight tables sum to 100 in all three columns, the coding-specific share (60 − 15 + 15×3.5/9 ≈ 51%) checks out, the token-ontology identity (13,409,872 + 24,491,270 = 37,901,142) checks out, the 52/105 → 49.52 test vector checks out, and the cost-doubling/quality-offset pair (3.11 value points vs 3.11/0.75 = 4.14 quality points) is internally consistent.

1. Findings by severity

Critical

None

High

None

Medium

O46 ceiling recompute tolerance is stated twice, 10× apart (part 6). The MiMo-quota-ceiling bullet says the build "fails when the stored multiple differs by more than 0.0005 (the multiples are stored to four decimals)", and later in the same bullet says "the stored multiple must recompute within 5 × 10⁻⁵, half a unit of its fourth decimal". Half a unit of the fourth decimal is 5 × 10⁻⁵, so the first figure (0.0005, five units) contradicts the second (5 × 10⁻⁵) in the normative text of a build-stop gate. Why it hurts: under the loose reading, a stored ceiling could silently drift by up to five units of its last stored decimal — opponent-visible because these ceilings are scored Plan multiples (O125) — before the gate fires; under the tight reading, the draft overstates tolerance to operators and auditors. Either the build or the document is wrong, and this round cannot tell which. Concrete change: pick 5 × 10⁻⁵ (consistent with four-decimal storage and the "half a unit" rationale), state it once as a registry constant (plan_ceiling_recompute_tol), have the build print the tolerance actually applied in scores.json, and fix the contradictory sentence.

Low

E246's "(max)" apposition conflicts with the bare-name effort rules it must coexist with (parts 6 and 8). Part 6 binds an effort-unstated SemiAnalysis figure to "that model's unsuffixed AA row (max), the configuration AA plots under the bare model name". Part 8 shows the two are not equivalent: AA plots MiMo-V2.6-Pro, MiMo-V2.6-Flash and MiniMax-M3.1-Flash without an effort, and their documented configurations are high (O54), thinking-enabled (O135/O140) and max (O148) respectively. If SemiAnalysis ever publishes an effort-unstated figure for such a model, E246 as written binds it to "(max)" — a configuration that may not exist in the roster — with no build stop. Latent today (every SemiAnalysis figure binds to GPT/Claude max rows), but silent and score-moving if triggered. Concrete change: drop the "(max)" apposition; bind to the configuration AA plots under the bare model name whatever its effort, resolve that effort through the existing O135 research path, record it on the route, and stop the build when the resolution is ambiguous. This is a new argument about E246, not a repeat: the conflict was created by O54/O66/O135/O148, which postdate the binding rule as originally stated.

GDPval movement diagnostic compares consecutive captures only (part 8). E90 as operationalised compares each capture with the digest of the one it replaced; the draft itself concedes the leaf "can differ from AA's own Index input by the drift accumulated since a configuration's addition", but nothing measures that cumulative divergence. Why it hurts: a slow refit that moves a rating 0.5 Elo per refresh is invisible to a consecutive-capture check even as it materially reorders a 10% leaf (200 Elo = 10 z points). Concrete change: since first-capture hashes are already retained in the evidence bundle, publish each row's cumulative Elo movement since first capture beside the consecutive-capture move, with an informational flag (e.g., cumulative move above 20 Elo) in gdpvalMovement.

E268's date fallback can switch a configuration's AI Coding Daily record between releases without a recorded reason (part 8). When no harness match selects a duplicate row, "the row with the latest test date" wins. A board adding a newer row on a different harness then changes the leaf value between releases with no editor selection event — exactly the failure mode E206 forbids for Bug Hunt (largest-sample mean; any deviation needs a recorded reason; equal-N tie stops the build). Impact is low because alternates are published, but the change is silent in the record itself. Concrete change: require a recorded selection reason whenever the selected row's harness differs from the previous release's selection, and fail the build on a date-tie, mirroring E206.

New quality leaves get derived anchors but no stated freeze/version discipline (part 7). Cost anchors are versioned, frozen, eligibility-gated and bridged (E184/E253); quality anchors are "the frozen ones" and "for a new leaf they are set by this rule" (a_low = chance/baseline, a_high = documented ceiling) without saying the new leaf's anchors enter the versioned anchor object at introduction. If a mid-version leaf is ever re-authored (e.g., a successor benchmark with a different documented ceiling), normalisation could shift between releases without an anchor version change or bridge. Concrete change: extend the anchor-version record to cover every leaf's anchors, frozen at introduction, with the same old/new bridge rule as cost anchors.

Editorial (part 7): the "today" exchange-rate sentence for the AI Coding Daily ranking ("2.71 (3.61) and 1.98 (2.63)") drops the API/Plan basis labels that the max-effort sentence carries, leaving which number is which to inference from order. One-word fix per number.

2. Methodology design recommendations

Prioritised; everything here is implementable from routinely refreshable public data and adds nothing outside the fixed owner policies.

Single-constant gate arithmetic (from the Medium finding). Define every build-gate tolerance once in the registry (tolerances.plan_ceiling_recompute = 5e-5, tolerances.swing_attribution = 1e-6, etc.), reference the constant by name in prose, and have the build echo the constant it applied into the evidence bundle. This removes the whole class of "two normative numbers" defects, not just this instance.

Per-leaf variance decomposition of the S1T separability threshold (part 9). S1T draws LiveBench 2.0 Overall from seven category binomials whose counts include Reasoning = 4 and Data Analysis = 3 effective tasks ("the wide reading"). Publish, beside each separability figure, each leaf's contribution to scenario value variance (
𝑤
𝑙
2
 
V
a
r
(
𝑧
𝑙
𝑑
𝑟
𝑎
𝑤
)
w
l
2
	​

Var(z
l
draw
	​

), with LiveBench decomposed per category). Readers currently see "0 of 29 adjacent ranks separable" but cannot tell how much of that is driven by two categories with n = 3–4 inside a 15% leaf. The print is pure arithmetic over inputs already in the registry; it also pre-positions the switch to question-level counts if LiveBench ever publishes them (keep the wide reading primary until then — the pessimism is the honest choice and I do not challenge O142).

Cumulative GDPval drift ledger (from the Low finding). Per row: first-capture Elo, current Elo, cumulative move in Elo/z/value points, flag above 20 Elo. This turns E90's concession ("can differ by drift since addition") into a number and costs nothing beyond reading stored capture hashes.

Harness-selection provenance symmetry (from the Low finding). Apply E206's discipline — key, preference rule, recorded reason for any deviation, build stop on ties — uniformly to every added-leaf board with duplicate rows (today only AI Coding Daily via E268). One shared selection object in data/swe_tracks.json with selection_rule_id and selection_reason covers both.

Quality-anchor versioning (from the Low finding). Freeze every leaf's anchors at introduction inside the ranking's versioned anchor object, with the same bridge and "previous version stays live" policy E184 gives cost anchors. This closes the one normalisation surface not covered by the anchor machinery.

Deliberately not recommended (checked against the ledger first): nothing on Jeffreys-posterior shrinkage at small n (O142 is owner policy, adopted with the shrinkage question already in view), nothing on the abstain-all Omniscience score of 50 or the logistic-vs-linear GDPval mapping (O28/E128/E181 cover both as named sensitivities), no weight redistribution for non-discriminating leaves such as AA-LCR (rejected family of arguments), and no second-confidence-level treatment of GDPval's unstated-level interval (the draft's E174/S1T split with the wide-reading sensitivity is already the right conservative posture, and the rejected "AA states a 95% level" claim is correctly not resurrected).

3. Questions for the owner

Which O46 ceiling tolerance is intended — 5 × 10⁻⁵ (half a unit of the fourth stored decimal) or 0.0005? The fix and the gate's behaviour both depend on the answer.

Should quality-leaf anchors be frozen and versioned at leaf introduction (mirroring E184 for cost anchors), or is re-derivation at each introduction acceptable? Recommendation 5 stands or falls on this.

4. Verdict

The four parts are in strong shape: the admission case order, transfer provenance, anchor machinery, weight arithmetic, and the three-layer uncertainty engine are internally coherent, heavily fixture-backed, and consistent with every owner decision I could check against them; verified arithmetic matched everywhere. The one Medium is a normative-number contradiction in a build gate that must be resolved before this section is clean.

VERDICT: HAS FEEDBACK