# Internal review I20 — Claude Sonnet 5.5, effort low, on draft r79

(Saved from the subagent's report; the reviewer read all 972 folded lines.)

## 0. Read check
- First line: `# ValueRank methodology — draft r79`
- Last line (line 972, a fragment completing the sentence on line 971): `(E95, E101).` The last 12 words of the document are: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
- I read all 972 lines in three chunks, plus the ledger brief. I consulted the full ledger only for the points below.
- I ran no web searches. Every finding rests on the draft's own text and on read-only inspection of `data/scores.json`, `data/aa_deepswe.json` and `data/tb4.json`. I created, edited and deleted nothing.

## 1. Findings by severity

### Critical
None.

### High

**H1. Missing-leaf renormalisation is not neutral: the sparse leaves are the hardest ones, so rows that publish them are penalised in the headline value score and in the bar.**

- **Passages.** "Missing data: displayed quality renormalised over a row's available leaves (fixed leaf weights; no imputation)" (Quality section). The bar H is defined on displayed quality (E198b).
- **Data** (`data/scores.json`, `v3.rows`, 37 rows):
  - Leaf coverage: Terminal-Bench 14 of 37, FrontierCode 23 of 37, DeepSWE 35, Bug Hunt 36, all other leaves 37.
  - Each sparse leaf's z sits well below the same row's other observed leaves: Terminal-Bench by 13.9 points on average, FrontierCode by 9.1, Bug Hunt by 26.3.
  - I recomputed quality on the leaves that nearly every row has, dropping only Terminal-Bench and FrontierCode, with the draft's weights.
  - The 10 rows that have both leaves score 3.1 quality points lower on the displayed basis than on the common-leaf basis. The 10 rows that have neither are unchanged.
  - At the draft's exchange rate, 3.1 quality points offsets about 0.85 cost doublings, or roughly 2.3 value points.
  - API value ranks, recomputed with the same 0.25/0.75 weights and the stored cost scores, move by up to 12 places. Muse Spark 1.3 (xhigh) goes from 29 to 17. Other moves are 5 to 7 places (DeepSeek V4 Flash, Muse Wonder, Grok 4.6, Gemini 3.8 Flash, the Haiku 5.5 efforts).
  - The number of rows reaching the headline bar H = 56.7 goes from 18 to 20.
- **Why it hurts the objective.** Publishing a harder benchmark result lowers a model's rank, and withholding it raises the rank. Rows compared against one another, and against H, are measured on different leaf sets.
- **What the draft already offers and why it falls short.** The leave-one-benchmark-out branches (E146) remove a leaf for all rows. E221's u* reports a per-row break-even. Neither publishes the direction and size of the effect per row, so a reader cannot see this as a systematic bias.
- **Change** (a diagnostic only; scores and O8 "missing stays missing" are untouched):
  1. Publish a "leaf-availability effect" column. For each row, show displayed quality minus quality on the leaf set observed by at least 90% of cohort rows. Add each sparse leaf's mean gap to the row's other leaves. Flag rows where the effect exceeds 1 doubling-equivalent (3.65 quality points at β = 0.25).
  2. Publish the value ranks and the bar reach under that common-leaf quality, beside the primary ones, on the E65 common panel.
  3. Say in the headline that missing-harder-leaf rows are advantaged.

### Medium

**M1. E19 states a false premise, and the draft's own text contradicts it. The harness confound covers all of the 60% SWE group, not only Bug Hunt.**

- **Passages.**
  - E19 (Normative definitions): "Bug Hunt runs on vendor CLIs while DeepSWE and Terminal-Bench run in controlled harnesses."
  - Cost section: the Coding Agent Index runs "under vendor agents".
  - Terminal-Bench leaf: 12 of the 14 rows are scored on Claude Code, Codex, Grok Build or Muse Code.
  - Known limitations: "DeepSWE/Bug Hunt/TB measure model+harness stacks."
- **Data.**
  - Every DeepSWE row (35) is a vendor or lab agent: Claude Code 14, Codex 12, Muse Code 4, Grok Build 2, Antigravity CLI 1, Antigravity SDK 1, Opencode 1.
  - Terminal-Bench: Codex 6, Claude Code 5, Muse Code 1, Grok Build 1, mini-SWE-agent 1.
  - So each lab's model is scored in that lab's own agent, and the harness is confounded with the provider on 50 of the 60 SWE quality points.
- **Why it hurts.** The only stress band, "Bug Hunt harness band", is applied to the 10-point leaf. The 40 points on DeepSWE and Terminal-Bench get no harness stress, and E19's premise would lead a reader to believe they are controlled.
- **Change.**
  1. Correct the E19 sentence.
  2. Extend the pre-registered S2 harness band, which already uses tbench.ai same-model cross-agent spreads, to the DeepSWE and Terminal-Bench leaves.
  3. Publish a leaf × agent confound table showing the share of quality weight by agent. State that the Plan basis is meant to reflect vendor harnesses, while the API basis includes third-party agents (Objective section).

**M2. The same-harness Terminal-Bench diagnostic (E125) is vacuous today, and the draft does not say so.**

- **Passage.** E125 uses "one named default harness (Terminus 2; rows without it missing)".
- **Data.**
  - The published agent counts (mini-SWE-agent 1, Claude Code 5, Codex 6, Grok Build 1, Muse Code 1) contain no Terminus 2 row.
  - In `scores.json`, `terminalBenchSameHarness.panel` is empty and `restricted` is `{}`.
  - All 14 Terminal-Bench rows are marked "harness-mixed".
  - The draft presents τ_b "on their common panel" as if it is evaluable.
- **Change.** State "undefined (empty panel)" in the active-rules manifest. Replace the fixed default with a rule that picks the harness with the most cohort rows, and declare the statistic undefined below 8 rows. Or publish a cross-agent list for Terminal-Bench like E224 does for Bug Hunt. Do not call the leaf "checked for harness" while the check has no panel.

**M3. The "possibly superseded" stage merges a routine trigger with a warning trigger, and neither changes the interval eligibility of an identified multiple (E212 table).**

- **Passage.** Trigger "more than 30 days old, a scoped change detected since measurement, or ≥ 2 independent reports of an undocumented limit change". All three leave score, route comparison and interval eligibility "unchanged" until the 90 + 30 day demotion.
- **Why it hurts.** Age alone is the benign, routine case. A detected change in rate-limit or pricing tables, or two reports of an undocumented limit change, is positive evidence that the identified M_W (bound to a quota-schema version, Plan measurement vs transport) is stale. An interval label (confirmed or definite) built on that multiple could stay published for up to 120 days. This is new relative to the ledger's M1 (E212): the ledger records that the soft stage is "age or a detected change" but does not discuss treating the two differently.
- **Change.** Keep age-only "possibly superseded" as it is. For change-detected or limit-change-reported triggers, withhold Plan interval labels (not the displayed score) until a new public measurement or the owner records that the change does not affect the route. Moot today (no identified M_W), but it is a rule that will bind.

### Low

**L1. "S1 core" is used normatively but never defined.** E100 authorises the label only in "stratum S1 core", E167 lists "S1 core, S2 core and S1M", and E186 repeats it. The strata list defines only S0, S1, and "S2 core branch". "Results per stratum (S0, S1, S2; transfers on/off ...)" implies S1 core = S1 with transfers off and nominal weights, but nothing says so. Two implementations could authorise labels from different streams. Add one sentence defining S1 core.

**L2. Frontier membership is undefined for a label-denied row (E222, E170 outcome 4).** DefiniteFrontier and PossibleFrontier are defined for i ∈ R_W, and an outcome-4 row with FullCost enters R_W "at its published point". The text says the row "never earns a label" and, for B_W rows, "earns none" of "labels and memberships". It does not say whether an outcome-4 row can be shown as definite or possible frontier. Moot today because Fable 5.1 lacks FullCost, but implementations would differ. State that denied rows get membership statuses marked "label-denied" or none.

**L3. The E151 clause (Source contract / Plan cost input) is a run-on parenthesis.** It opens "(a report's observation date is its E194 date … leaving the window)" and then continues "before a partition is pooled, each report is classified by its own clock". Split it into two sentences. As written, a reader can take "reports past expiry and grace leave the partition" as applying to counting reports, which the next sentence says never reach an age stage.

## 2. Methodology design recommendations (prioritised)
1. **Leaf-availability disclosure** (H1). Add a common-leaf quality, value rank and bar-reach panel beside the primary ones, and a per-row "evidence-set effect" in quality points and cost-doubling equivalents. It needs no new data and no score change. It would show which headline ranks depend on a row's choice or luck of publishing the harder leaves.
2. **Harness confound as a first-class disclosure** (M1, M2). Publish quality weight by agent per leaf, extend the tbench.ai cross-agent stress band to the DeepSWE and Terminal-Bench leaves, and make the same-harness check data-driven (the most common harness among cohort rows, or a cross-agent list) rather than naming an agent that no cohort row used.
3. **Separate age from change in the Plan lifecycle** (M3). Interval labels depend on whether the identified multiple is still valid. The lifecycle table should say so.
4. **Self-check cheaply.** Add the three unit-checks below to the release tests: S1 core definition (L1), denied-row membership (L2), and a warning in the active-rules manifest when a diagnostic's panel is empty (M2).

## 3. Questions for the owner
1. Does the owner accept a diagnostic (no score change) that reports each row's leaf-availability effect and a common-leaf ranking, or does "missing stays missing" extend to not showing a comparison on a common leaf set? If the latter, H1 becomes an Owner decision challenge that I would restate as a request to flag, in the headline, that rows lacking Terminal-Bench and FrontierCode are advantaged.
2. Should API-buyer quality (third-party agents included) be allowed to use a different harness treatment from Plan-buyer quality (vendor apps)? O10 fixes one quality vector for both bases, so a harness-specific vector would be an Owner decision challenge. A harness stress band for DeepSWE and Terminal-Bench needs no such change.

## 4. Verdict
VERDICT: HAS FEEDBACK
