# Internal review I61 — Claude Sonnet 5.5 (effort xhigh) on draft r120

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r120`
- Last line of the draft (line 174 of 174, the revision-history paragraph, 19,035 characters, beginning "Revision history: r16–r24 fixed…"). It ends: `…r120 (owner decisions O71 and O72) records the three-stage plan-allowance research over every cohort provider's first-party plans, which admitted no new route, keeps the owner-authorised routes and API fallback elsewhere, and moves the search cutoff to that search. Every change is recorded with its rationale in the ledger.`
- Last 12 words of the last paragraph: "that search. Every change is recorded with its rationale in the ledger."

What I read: `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" to the end (O45–O72, E247–E268, I29–I60, the O71 research outcome and O72), the root `AGENTS.md`, `review-i60-claude-sonnet-5.5-xhigh.md`, and every line of `draft-r120.md` in chunks (a 1,024-line folded copy; line numbers below are those of the 174-line published file). I diffed r119 against r120 (the changes are the Plan-allowance paragraph at line 55, the revision-history tail and the figures it feeds) and read the O71 record: `research/2026-10-25-plan-allowances/` (README, stage-1 files and assessment, the stage-2 notes and report) and `research/2026-10-25-plan-allowances-sb-deep-research/` (decision record, handoff, run manifest, validation logs).

What I checked against data and code (it passed unless a finding says otherwise):

- `python3 -m valuerank.draft_figures check` exits 0, and `tests/test_draft_figures.py` passes (21 tests).
- Cohort: I recomputed the 11 near points from `data/aa_frontier_capture.json` (190 plotted points, 19 vertices, rule F(c) − 3 on the rounded tooltip Index). They equal the capture's 11 names exactly. The family counts (13 families, 8 frontier, 5 near-only), the nine excluded configurations and their five classes partition, and 21 ranked at least once all match.
- Ladders and counts: the bar levels from the displayed qualities (53.27 / 63.54 / 64.94 over 9 rows at zero-based positions 2, 4, 6; 38.00 / 49.24 / 58.61 over 16 rows at 3, 7, 11), the reach counts 7/5/3 and 13/9/5, the bar setters (Gemini 4 Argon (high); MiMo-V2.6-Pro), possible/confirmed qualifiers 5/4 and 9/8, thresholds ⌈2N/3⌉ = 6 and 11, 255 and 127 feasible admission subsets, Coding Agent Index coverage 8 of 9 and 3 of 16, ITBench-AA 2 of 9 and 0 of 16.
- Separability: medians 2.762 / 2.763 (max-effort API / Plan) and 4.431 / 4.425 (AI Coding Daily), the wide-GDPval readings 2.772 / 4.438, the n = 60 readings 3.251 / 3.245 with 1 of 15 and 1 of 20 separable, the E242 tolerances 1.88 / 2.19 / 2.96 / 5.26, the noise margins 3.70 and 5.87, 14 of 27 and 48 of 51 assumption plan rows, 27 and 51 plan rows, source shares 66/34 and 78/22, leaf counts 13 and 11, the exchange rates against the anchors (3.04 → 4.06 quality points).
- Code against text: S1T's per-row GDPval SD (`gdpval_row_sd`, half-width ÷ 1.96) and the ±26 wide reading; `check_row_date` (N − ½ hours bound, cutoff-day rows), `check_bug_hunt_dates`, `check_source_clocks`; the chart capture inside the post-cutoff loop of `assemble` (I60 L1 is fixed); the E218 search-age and "latest all-provider search" gates; the O46 ceiling recomputation (all eight routes, `capturedOn` 2026-10-23); `GRADE = controlled 3 > reports 2 > assumption 1` and the comparator tuple (relevant to M1).
- O70/E90: `diagnostics.gdpvalMovement` (61 common pages, 54 moved, 0 Index totals moved, −0.83 to +4.10 Elo; ranked maximum 0.205 z = 0.0154 value points in the max-effort ranking and 0.192 z = 0.0144 in the AI Coding Daily ranking).
- O71/O72: the new search-log entry in `data/plan_cost_routes.json` (scope, reached and unreachable lists, `searchCutoff` 2026-10-25, no `singleProvider` mark) against the draft paragraph at line 55; the decision record, stage-1 assessment and stage-2 report against the draft's statement that no model × tier passes O11 over its comparability partition (it holds); the research directories exist at the cited paths.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. O72's sentence "A route switches to user reports once two concordant reports exist for the exact model and tier" contradicts the comparator's grade key for the three exact SemiAnalysis routes (line 55 against line 51; the same sentence is published in `site/data/plans.json` `o72Application`).**

The new sentence in the Plan-allowance paragraph (line 55) is general: any route, once two concordant in-window reports exist for the exact model and tier, "switches to user reports". AGENTS.md says the same ("Until two concordant user reports exist, the owner-authorised routes stay"). The draft's comparator says otherwise for exact controlled routes:

- Key 2 of the E85 comparator orders "controlled measurement of the exact model > ≥ 2 concordant end-user reports > owner-named transfer", and line 51 says "a controlled measurement outranks a report partition for the same route through the grade key".
- The code agrees: `plan_routes.GRADE = {"controlled": 3, "reports": 2, "assumption": 1, "diagnostic": 0}`, and `tests/test_plan_routes.py:193` asserts that a controlled route beats a report route even with a lower multiple.
- The fixture at the end of the same paragraph (line 55) covers only a lapsed report pair ("the controlled route stays and the report route is diagnostic"). A current concordant pair against an exact controlled measurement is covered only by key 2, which keeps the controlled route.

So the two statements give opposite answers in one case. The case is not hypothetical:

- In the max-effort ranking, 11 of 27 plan rows are `controlled` exact SemiAnalysis routes: Claude Opus 5.5 (max) on three plans, GPT-6.1 Sol (max) on four, GPT-6 Astra (max) on four. These are the rows whose Plan value is least assumption-dependent. (The AI Coding Daily ranking has none, so there the sentence is right: a report pair outranks a transfer.)
- The O71 record names the nearest cell to passing: Claude Pro × Opus 5.5, where the pre-10-08 reports ($321 and $302 per week, a ratio of 1.06) are concordant and the cell fails only because of #124 (about $1,266 per week) and one range-valued report. When #124 or the range leaves the window, or the owner rules on outliers (the stage-3 handoff, step 4), this exact route will face the question at the next refresh.
- E191 makes the owner decision govern an editor decision. If O72 is read literally, key 2 (E85/E93), line 51 and the fixture are overridden for Anthropic and OpenAI. If O72 means only transfers, ceilings and API-cost rows, the sentence is wrong as written. The draft cannot be executed unambiguously until one reading is chosen, and the owner's earlier "highest eligible Value Multiple" rule (key 3) offers a third.

Recommended change: ask the owner (Q1 below) and then state the rule per route class. For example: "A transfer, an O46 ceiling (O62) or an API-cost row is replaced by a concordant report pair for the exact model and tier. An exact controlled measurement stays ahead of a report pair (key 2) unless the owner decides otherwise." Add a fixture for a current concordant pair against an exact controlled route, and make AGENTS.md, the site text and the ledger carry the same sentence.

### Low

**L1. Nothing records that E18's change-detection stage was run for the SemiAnalysis routes after the O71 research, although the research found its triggers (lines 53, 152, 159).**

E18 and the lifecycle table make a route "possibly superseded" when scoped change detection shows a change since measurement, or when ≥ 2 independent end-user reports describe an undocumented limit change. The O71 notes document, after SemiAnalysis's measurement of 2026-10-06:

- Anthropic's own help-article update of 2026-10-07 (Max plans gained monthly API credits covering `claude -p`).
- Four user reports (three in claude-code #102667, one in a Reddit thread) of a weekly meter that moves faster per token from 2026-10-17, two of them with per-token readings, and no Anthropic statement.
- A SemiAnalysis post on X of 2026-10-22 (second-hand, via cellcog.ai): "an A/B test … DECREASES your monthly API-value by ~20%" on some accounts.
- An OpenAI support e-mail, quoted by a blogger, acknowledging a Pro 200 → Pro 500 entitlement error corrected on 2026-10-16.

The stage-2 summary says "Every provider changed its allowances or metering during October 2026."

Against that, `plan_cost_routes.json` has no `changeDetectedOn` on any route, the published route record shows only `evidenceDate` 2026-10-06 (no stage), and the active-rules manifest (16 entries per ranking) has no entry for the Plan evidence lifecycle or change detection, although line 152 says it "lists every gate, flag and rule". Line 53 says the route is Current until 2026-11-05 and possibly superseded "by age" afterwards, which reads as if age were the only clock.

The effect is small. The stage changes only a label and, in Plan interval outputs that are unevaluable today, a blocker status. A 20–40% allowance change is well inside the E242 tolerance (2.19× in the max-effort Plan ranking, 5.26× in the AI Coding Daily ranking). So this is Low, but it is a normative step with no recorded outcome.

Recommended change: record per provider and plan, at each release, the E18 outcome. Either set `changeDetectedOn` with the evidence IDs, or write "not triggered: <reason>", for example that one GitHub thread is one upstream source (E223). Add a manifest entry. Say in line 53 what was evaluated. Note the SemiAnalysis post of 2026-10-22 for the first run of the weekly watch (Monday 2026-10-26).

**L2. The evidence bundle still has null or stale capture times, although line 152 says "each artifact's capture time is in the evidence bundle (for a derived or editorial file, its source's own latest instant)" and line 28 says the bundle lists "capture time" for every artifact.**

I60 L6 was fixed for three artifacts (`tb4`, `bugHunt`, `leafEvidence`). In `scores.json` `evidenceBundle`, five of the 19 rows still show `capturedAt: null`: `frontierCapture` (the artifact that defines the cohort; its instant is the file's `captured_at`, 2026-10-25T09:53:28Z, a key missing from `CAPTURE_FIELDS`), `codingAgentsManifest` (`capture`), `roster`, `cognitionFrontierCode` (the instant sits in `leafEvidence.cognitionCapture`) and `sourceRereads` (`reReadAt`). `planRoutes` shows `2026-10-08` (its `asOf`), although the file now holds the 2026-10-25 search entry and the 2026-10-26 O72 note. No gate reads these stamps (O59–O60 use `sourceClocks`; E211 and E217 use the capture files), so no output is wrong.

Recommended change: derive each stamp from the artifact's own instant field, fail the build on a null, and give `planRoutes` its latest search or capture date.

**L3. The O71 procedure is not checkable by the build and its refresh cadence is unstated (line 55).**

- The new log entry is one free-text entry. It has no `stages`, no `providers` and no `queries` count (an earlier entry had one, and line 55 promises "queries, sources reached and sources unreachable" per stage, twice). "All-provider" is still the absence of a `singleProvider` mark (I54 L4). O71 makes that mark consequential, because a full all-provider search now takes three stages and is tempting to shorten.
- In the source, only the date is a placeholder. "That three-stage search" is typed, so if a later stage-1-only entry becomes the latest unmarked search the sentence will go on saying "three-stage".
- Stage 3 ran degraded: its run manifest records `research_type: default`, the host fallback instead of search-cli, and no helper agents, with X, YouTube pages and Zhihu unreachable. The draft lists the unreachable sources but not the degraded mode.
- E218 requires an all-provider search within 7 days of every release, and O71 says to run stages 2 and 3 whenever stage 1 leaves a cell short of two reports. Read together, every release needs all three stages for nearly every cell. The draft does not say whether that is intended.

Recommended change: add `providers` and `stages[]` (each with queries, reached, unreachable, outcome per cell) to the entry and fail an unmarked entry that omits a cohort provider or a stage. Generate "three-stage" from `stages`. Say the cadence (Q3 and recommendation 2).

**L4. The operative reading of O11 that produced the O71 verdicts lives only in the research notes, and it is stricter than, or absent from, E98, E102, E107 and E139 (lines 53 and 55).**

The stage-2 report applies seven eligibility conditions and reporting rules: a dollar figure tied to a meter fraction or full exhaustion ("lower bounds do not count"), a range-valued report must pass "for its whole range", monthly = weekly × 4.33, OpenAI Fast-mode figures × 2.5, a tier inferred by the researcher is only provisional, accounting-bug days are excluded. Stage 3 records the stage-2 reading as "user_confirmed" in its run manifest.

The draft has none of these rules. E139 says the opposite on the first point ("O11 still admits concordant reports without a saturation requirement", labelled "observed-usage multiple; full utilisation not established"). E98 gives the margin only for point values. Line 57 forbids extrapolating "short bursts to a billing period", while the research normalises weekly reports to months.

So "found no model and tier … agreeing within the O11 margin" holds under the research's reading. A later editor who applies the draft's rules to a new report file could reach a different answer. No score depends on it today (the owner kept the authorised routes), but the report path is the only way a route can ever switch.

Recommended change: write the reading into E102/E107 as a versioned report-eligibility profile (recommendation 3), including the range rule, which decides the nearest Claude Pro cell once #124 is resolved.

**L5. "No public source provides it today" (line 58) is too strong for the O71 record.**

The sentence says M_W becomes identified only with category-specific burn evidence for the plan's meters, and "no public source provides it today". The O71 notes cite two public sources of that kind:

- A fitted per-model, per-category meter-rate document for four Claude Max 20x accounts (`claude-usage-tracker`, docs/findings/2026-10-05-rates-in-five-hour-unit.md), with a cache-read credit of about 0.4–1% of an input token.
- A Kimi CN tier test (okarin, locdd mirror of LINUX DO 3069671) that fits uncached, cache and output weights per 5-hour window from the provider's usage endpoint at 0.01-point precision and gives a pool of 24.84 windows.

Neither is a controlled measurement admitted under E44 or E105, and Kimi's USD-to-CN tier mapping is unconfirmed, so the Plan headline's "exploratory" label need not change. But the sentence is a hand-written statement about what sources publish, the class I60 M2 asked to test.

Recommended change: "no source admitted under E44/E105 provides it; the O71 record lists two end-user fits (Claude Max, Kimi CN tiers) not yet evaluated against those rules."

**L6. The absence-marker check is narrower than r119's description of it.**

The revision history (line 174) says r119 "tests every statement that a source publishes or the capture carries no field against the pinned data". The check matches one regular expression (`not captured`, `carries/publishes/captures no`, `does not carry/publish/capture`, `not published`, `publishes only`). Absence statements outside it are typed and unmarked, for example:

- "no public source provides it today" (line 58, L5)
- "AA does not state its scale factor" (line 80)
- "no source publishes IFBench for the cohort" (line 67)
- "no Plan measurement publishes repeats today" (line 105)
- "(DeepSeek sells no first-party plan)" (line 55)
- "but not per-evaluation category splits" (line 58)

Each is true or defensible today, which is why none has been caught. The point is the claim, not the examples: the revision history overclaims, and the class is open.

Recommended change: say "each registered absence statement", and widen the pattern to `no|none|not` within a few words of publish/provide/state/document/sell, with a registered test for each hit.

**L7. Known limitations (line 167) omit O72's consequence.**

They list the MiMo ceilings but not that Google, Kimi, MiniMax and DeepSeek rows take API cost on the Plan basis. Today that is 2 of 27 plan rows in the max-effort ranking and 3 of 51 in the AI Coding Daily ranking (Gemini 4 Argon, DeepSeek, Kimi K3.1 Pro). It also omits that routed and unrouted rows differ in kind (a 57–59× or 8–15× multiple against none), so Plan-basis order mixes route availability with value. Line 13 describes the Plan ranking as "displayed arithmetic on owner-named transfers, the O46 quota ceilings and measured multiples" and does not mention the fallback rows.

Recommended change: add a limitation sentence with generated counts and name the fallback rows beside line 13.

**L8. Wording left behind by O65 and O70.**

- Line 152: "With E211 and E217 together the model-page snapshot is at most 14 days old in practice" predates O65. The next sentence says the snapshot defines the cutoff, so its age at the cutoff is 0.
- Lines 86 and 152 promise that the registry records "rating snapshot ID, anchor identity and fit revision" and an "integration-freeze status". The data holds none of these (`rows[].quality.leaves.gdpval` has the interval, the level note and the evidence locator). AA publishes no fit revision or freeze flag, and E90 no longer relies on a freeze. Keep what exists (the capture's hash and instant and the previous-capture digest) and drop the rest.
- Line 86: "0.21 z points, 0.015 value points in the max-effort ranking and 0.014 in the AI Coding Daily ranking" gives the max-effort z beside both values. The AI Coding Daily largest move is 3.84 Elo = 0.19 z. Render each ranking's z with its value.

## 2. Methodology design recommendations

Prioritised. All use public data that can be refreshed routinely.

1. **Settle the precedence of evidence classes once, as a table (M1).** Rows: exact controlled measurement, concordant report pair, owner-named transfer, O46 ceiling, API fallback. For each: what replaces it and under which decision. Put it in the comparator section, generate the AGENTS.md and site sentences from it, and add fixtures for a current concordant pair against an exact controlled route and against a transfer.
2. **Make the O71 outcome a computed object.** Add `data/plan_allowance_cells.json` with one record per (cohort model × first-party plan tier × comparability partition): eligible report IDs and observers, normalised values, the ratio of largest to smallest, verdict and reason, and the hash of the eligibility profile used. The build fails when a cohort model × tier cell has no record, or when an all-provider log entry lacks `providers` or `stages`. The line-55 sentences ("no model and tier…", the provider list, "three-stage") and the Known-limitations counts become placeholders. This is the E265 route and removes L3, L5 and L7 as a class. For the cadence, run stage 1 every release as a scripted crawl over fixed public sources (Fei2411/real-api-pricing structured issues, Hacker News Algolia, the arctic-shift Reddit mirror, and the anthropics/claude-code and openai/codex issue trackers). Run stages 2 and 3 when stage 1 yields a candidate pair (two eligible reports within 1.5×) or the prior record's partition boundary changes, and at a fixed interval otherwise (owner call, Q3).
3. **Versioned report-eligibility profile (extends E102/E107/E139).** Register the rules the O71 verdicts used: range-valued reports (publish the verdict under both whole-range and midpoint; say which governs), unit normalisation (4.33 weeks per month; the Fast-mode factor, both published), lower bounds and non-saturating reports (reconcile with E139), provisional tier inference, provider-acknowledged accounting-bug days, aggregator exclusion. Hash the profile into the bundle so a refresh reproduces the verdicts.
4. **Owner decision challenge (O11 as operationalised by E98/E107): publish a robust-core companion beside the strict concordance test.** E107 judges every eligible report of a partition together. The O71 record shows how much rests on single reports: in each near-miss cell one report decides (Claude Pro: #124 at 4× every other measurer, which stage 3 itself says "a future owner ruling on outlier handling would flip"; Gemini 4 Argon on AI Pro: one Low-effort report at 12.3 against 8.40 and 8.47; GPT-6 Astra on Pro $100: 480 against 330). New argument, not in the ledger: the record is as concentrated as a rule can be, and the strict rule leaves route switching dependent on one unverifiable post. Proposal: keep the strict result as the only one that can admit a route, and publish beside it the largest subset within 1.20× that has ≥ 2 independent observers and ≥ 2/3 of eligible reports, with the excluded reports and reasons. It changes no eligibility, score or label (consistent with O19/O25) and shows the owner when an outlier ruling would matter.
5. **A per-release change-detection ledger for Plan evidence (L1).** For each (provider, plan): documentation sections diffed with dates, provider statements, independent user reports of an undocumented change, and the E18 outcome. Show the stage in the route record and list the lifecycle in the active-rules manifest.
6. **A named S2 "allocation arm" sensitivity for Claude routes.** SemiAnalysis's own post of 2026-10-22 gives a second arm (−20% weekly budget, +19% five-hour window) on the same plan. Scale the Claude plan multiples by 0.8 as a labelled specification stress, outside Θ (O19) and never a label, and print the rank changes next to the E242 tolerance. At the max-effort Plan exchange rate (2.44 value points per cost doubling) a 0.8× multiple moves a Claude row by about 0.8 value points against a median separation threshold of 2.76, which is a useful thing to publish. A user-measured post-10-17 ratio (aggregator and user figures, 0.4–0.6× of SemiAnalysis's implied weekly value) belongs in the diagnostics only, with its source type.
7. **Close the evidence-bundle and absence-check classes (L2, L6).** Derive stamps from the artifact's own fields and fail on a null. Widen the absence pattern and keep a registry test per claim.

## 3. Questions for the owner

- **Q1 (O72 precedence).** When two concordant in-window user reports later exist for a model × tier that already has an exact SemiAnalysis measurement (today Claude Opus 5.5 (max), GPT-6.1 Sol (max), GPT-6 Astra (max), 11 of the max-effort ranking's 27 plan rows), which prices the row: (a) the SemiAnalysis measurement, as the comparator's grade key has it, (b) the user reports, as O72's wording reads, or (c) the higher multiple, the owner's earlier highest-eligible rule? The answer sets the sentence in M1, the comparator and the fixtures.
- **Q2 (outliers).** Should E107's all-eligible-reports concordance test stay as the only admission test, or may ValueRank publish the robust-core companion of recommendation 4 (no effect on eligibility)? If strict only, recommendation 4 drops.
- **Q3 (cadence).** Must every release repeat all three O71 stages for every cell, or stage 1 every release with stages 2 and 3 on a candidate pair or at a fixed interval (recommendation 2)? E218's 7-day gate makes this a real cost, so the draft should say which.

## 4. Verdict

One Medium finding (M1) and eight Low. O70 and the r119 fixes are implemented faithfully in the draft, the data and the code, and the O71 and O72 text matches the research record on every checkable fact. The Medium is a contradiction introduced by r120's new sentence, between O72's wording and the comparator in the same paragraph, that the draft cannot resolve without an owner answer. A round with a Medium is not clean (O56).

VERDICT: HAS FEEDBACK
