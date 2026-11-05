# Internal review I80 — Claude Opus 5.5 (effort xhigh) on draft r139

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r139`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r139 (seventy-ninth internal review, the second at Opus 5.5 xhigh, and owner decisions O94 and O95) has a row whose AA cost omits a pricing term compete over a cost range without labels or anchor membership, lets a lower-of transfer follow a replacing report pair, dates a change against the earliest possible measurement date and an unstated report window as its meter period, and shows route flags beside the Plan bars' cheapest rows and every ranking's release gates. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "release gates. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end. That covers O45–O95, E247–E270, I29–I79 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i79-claude-opus-5.5-xhigh.md`, and how the ledger resolved it. M1 became O94. L5/Q2 became O95. L1, L2, L3 and L4 are recorded as adopted.
- `draft-r139.md`, every line (1–174), in sequential chunks: 1–17, 18–30, 31–40, 41–50, 51–52, 53–54, 55, 56–57, 58, 59–62, 63–66, 67–87, 88–97, 98, 99–105, 106–116, 117–134, 135, 136, 137–147, 148–151, 152 (two halves), 153–173 and 174 (seven 4,000-character segments).
- A sentence-level diff of `draft-r138.src.md` against `draft-r139.src.md`. The hand-written changes are:
  - E92's blocker list (O94);
  - the E170 summary sentence (O94);
  - the GPT bullet (O95);
  - the report-table sentence (the unstated window as the meter period);
  - the r139 history entry.
- The HEAD commit's code, data and test diff:
  - `value_v3.py`: `_gated_box`, `aa_cost_caveat`, `caveat_factor`, `anchor_eligibility`, `interval_outputs`, `withheld_label`, `bar_labels` and the measured-only `faultWindow`;
  - `plan_routes.py`: `post_change_ranks`, `change_flagged`, `measurement_span`, `effective_measurement`, `rebase_lower_of`, `check_lower_of_routes` and `route_candidates`;
  - `plan_admission.window`;
  - `emit_docs.py`;
  - tests, README.md, scores.md, methodology.md and the site data.
- Unchanged code read for context:
  - in `value_v3.py`: `api_boxes`, `plan_boxes`, `freeze`, `anchor_population`, `frontier_anchor_diagnostic`, `family_primary_diagnostic`, `cost_removal`, `_measured_only_view`'s calibration, `_comparison`, `blocker_safe` and `plan_variants`;
  - in `plan_routes.py`: `donor`, `evidence_date`, `expiry_status`, `measurement_objects` and `report_date`.
- Data read or queried:
  - `data/scores.json` (both rankings) and the r138 `data/scores.json`, from `git show HEAD~1`;
  - `data/plan_cost_routes.json` (`evidencePolicy`, `changeDetection`) and `data/plan_reports.json`;
  - `data/aa_frontier_capture.json`, README.md, scores.md and methodology.md.
- The O71 record, spot-checked: the Google AI Pro rows against `research/2026-10-25-plan-allowances/stage1-google.md`.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- All 1,620 collected Python tests pass (e2e and js excluded; bytecode writing and the pytest cache off).
- `git status` was clean before I wrote this file.

**Arithmetic, recomputed independently from `data/scores.json` and `quality.TRACKS`.** There is no mismatch in 9 + 16 rows or 27 + 51 plan rows.
- Displayed quality.
- Cost scores on each row's own workload anchors.
- API and Plan values and competition ranks.
- Every anchor, each the cheapest reference ÷ 2 and the dearest × 2.
- Exchange rates: 3.04 (4.06), 2.44 (3.25), 2.83 (3.77) and 1.85 (2.46).
- Cost's value-variance allocation: 106% / 21% and −96% / −25%.

**Generated figures**
- Plan rows: 27 and 51.
- API-fallback rows: 2 and 3.
- Rows flagged possibly superseded or expired: 21 and 44.
- Fault-window rows: 3 and 8.
- Unverified-basis rows: 21 and 44.
- Assumption kinds: 10 + 4 and 26 + 4.
- Separability medians: 2.76 and 4.43 (API), and tolerances.
- Noise margins: 3.7 and 5.9.
- Bar ladders and E205 ladders, and bar-currency counts (7/5/3 and 13/9/5).
- Admission: 255 and 127 feasible alternatives.
- The O58 list of listed rows beyond the anchors.

**Cohort, recomputed from the capture**
- 19 strictly rising vertices.
- 11 near points.
- 13 families.
- First vertex at $10.63, the cheapest of 190 points.

**O94 effects** (`intervals.api` of both rankings):
- the AI Coding Daily lower-quartile bar has no confirmed cheapest;
- GPT-6 Luna (max) and (xhigh) are its possible cheapest;
- GPT-6 Luna (xhigh)'s definite membership is disproved by Claude Haiku 5.5 (medium);
- the scenario label at quality 38.0 goes to no one.

**Plan evidence**
- `planAllowanceCells`: 52 cells, 28 listed, none passing.
- Google AI Pro fails at 11.4 ÷ 8.47 = 1.35×.
- Report units are week / 5h / month, matching `METER_DAYS`.

**Probes** (scripts in my scratchpad, using the repository's own test helpers):
- an undated measurement with a change dated between its earliest and latest possible dates;
- an O95 rebase where the replacing pair is the plan's lowest figure;
- an O94 caveat that states no factor.

**Not verified:** live pages, the paywalled SemiAnalysis article and the scenario draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. O94's anchor clause was put into the shared anchor-population function. A published diagnostic now reports O94's next-freeze effect as a frontier-family effect, and the specification says the opposite.**

*What the draft says.* Line 36 defines the frontier-families anchor diagnostic (E187): it "rebuilds each basis's anchors and exchange rate from the cohort rows that carry a frontier or near-frontier inclusion reason". It then states: "Under O51 every cohort row carries such a reason, so both diagnostics equal the primary outputs today (scores.json `diagnostics.frontierAnchors`)".

*What the build now does.*
- r139 implements O94's "never an anchor reference from the next re-freeze" inside `anchor_eligibility`, so `anchor_population` drops the three Claude Haiku 5.5 rows ("AA cost omits a pricing term (O94)").
- `freeze` reads that function, which is what O94 asks for. But so do `frontier_anchor_diagnostic` (E187) and `family_primary_diagnostic` (E205).
- In the AI Coding Daily ranking:
  - E187 now rebuilds from 14 references, not 16. All 16 ranked rows are frontier or near-frontier rows (O51).
  - Its Plan anchors become c_L = 0.961 against the frozen 0.390. The low setter moves from Claude Haiku 5.5 (medium) on Claude Pro to GPT-5.6 Luna (low) on ChatGPT Pro 500.
  - Its Plan exchange rate becomes 2.04 against 1.85.
  - 10 configurations change rank, the largest by 3 (GPT-6 Luna (high)).
- In r138's `scores.json` the same diagnostic had 16 references and no rank change.

*What the published documents now say.* scores.md prints: "anchors rebuilt from the 14 frontier and near-frontier references move API no rank changes …; Plan 10 rows move; largest move 3 (GPT-6 Luna (high)) (value points per cost doubling 2.04 vs 1.85 frozen)".
- This attributes to the frontier-family restriction a Plan sensitivity that is entirely O94's exclusion of two frontier-family rows.
- Line 36 asserts equality.
- In the max-effort ranking the reference set also shrinks (8 to 7), but Claude Haiku 5.5 (max) is not an extreme, so the numbers are unchanged.

*The anchor-rebuilding diagnostics now disagree.* `cost_removal` (E64(b)), whose recalibrated anchors line 106 says are "rebuilt by the freeze rule", still rebuilds from every row. Claude Haiku 5.5 (medium) remains a reference there: 16 references, Plan c_L 0.281. So two diagnostics that both claim the freeze rule now use different populations.

*The normative eligibility text omits O94.*
- Line 47 says "Anchor eligibility is K on every admitted component **and** an E170 outcome of 1 or 2, two separate tests".
- Line 63 says "the shared eligibility is complete cost evidence on every component and an E170 outcome of 1 or 2".
- Neither names O94, yet the published `diagnostics.anchorEligibility` marks three rows ineligible for it.
- The frozen `anchorPolicy.populationRule` text names neither the valuation gate nor O94.

*Why Medium.* A current published diagnostic misattributes a 10-configuration rank sensitivity, and a "today" statement of the specification is contradicted by the build. The ledger has consistently rated that class Medium (I38 M1, I46 M1, I48 M2, I58 M1). It is not High: no score, rank or label changes.

*What is new against the ledger.* O94's effect statement ("no score or rank changes") lists the label effects only. Neither O94 nor the r139 ledger entry examines its effect on the diagnostics that rebuild anchors.

*Change.*
1. **Compare like with like in E187 and E205.** Take their references from the frozen anchor object's references, restricted to the diagnostic's population. They then equal the primary outputs today, as line 36 says.
2. **Publish the O94 effect under its own name.** Add a "next-freeze preview" diagnostic that rebuilds anchors with today's freeze rule (`anchor_population`, which drops O29, E202 and O94 rows) and runs the clip test. Today, in the AI Coding Daily ranking:
   - Plan c_L moves from $0.390 to $0.961;
   - 10 configurations move;
   - Claude Haiku 5.5 (medium)'s three plan rows would clip, by factors 1.20–1.23. That is 3 of the 5.1 rows the gate allows, so there is no hold.
3. **One reference-population function.** Make E64(b), E172, E187 and E205 call a single function, so "rebuilt by the freeze rule" means one thing.
4. **Write O94 into the eligibility text.** Add it as a third anchor-eligibility test on lines 47 and 63, and in the published anchor-policy text.
5. **Generate line 36's claim.** Render "equal / differ" from `diagnostics.frontierAnchors` as a figure, so it cannot go stale.

### Low

**L1. O94 is written into E92 only. E183's competitor set, E186's blocker safety, Θ and E198a's counts still describe O29 rows alone.**

*The definitions that omit O94.*
- Line 116 (E183) defines B_W as "the rows whose AA cost is on a price not in force at V (E170 outcome 3)", with "a row of B_W earns none (O29)".
- Line 135 (E186) requires BlockerSafe "for every b ∈ B_W" over "b's E183 hull domain".
- Line 114 lists Θ's variables without O94's [C, kC] range.

*The conflict.* An O94 row has FullCost, so under these definitions it is in R_W, competing at its published record and eligible for memberships. E92's parenthesis (line 135) says otherwise.
- The build follows E92: `_gated_box` widens the box and `bar_labels` requires BlockerSafe.
- Precedence (owner over editor) resolves the conflict, but the formal definitions no longer state the rule they govern.
- README and scores.md label the O94 rows "Competing without a label of its own (E183)".

*The counts.*
- E198a (line 121) counts "R_W configurations that can possibly qualify". The build excludes every blocker, so at the AI Coding Daily lower-quartile bar possibleQualifierN fell from 13 to 11 and confirmedQualifierN from 12 to 10. Yet both Haiku rows can qualify and do compete.
- Line 123 explains the gap between bar-currency reach (13) and the interval count (11) only by subset-workload rows, and that ranking has none.

*Change.*
- Define B_W as the O29 rows (current-tariff hull) together with the O94 rows ([C, kC]), and state E186 and Θ over that set.
- Either count blockers in possibleQualifierN, naming them, or redefine it as "label-eligible rows that can possibly qualify" and extend line 123's explanation.

**L2. An O94 caveat that states no factor fails open in the interval outputs: the row drops out of competition, and another row can gain a confirmed label.**

*What the build does.* `_gated_box` returns `None` for a caveat without a parsable factor. `interval_outputs` then lists the row as "unevaluable" and evaluates the rest. The `unconstructible` → "unresolved" branch covers only O29 rows.

*Probe* (`test_value_v3.scored()`, bar `median-quality`):

| Row a's caveat | Possible cheapest | Confirmed cheapest |
|---|---|---|
| none | {a, b} | none |
| 5× caveat | {b} | none (a blocks) |
| caveat without a factor | {b} | **b** |

*Why that is wrong.*
- It breaks line 116's rule: "A blocker whose domain cannot be constructed makes every claim it could affect 'unresolved', never leaving it out".
- It also breaks line 148's release test: "widening Θ cannot … create a confirmed result". An unbounded cost is wider than [C, 5C].
- The ledger's "(fail closed)" holds only for the caveated row itself.
- The scenario path does the opposite. `blocker_safe` returns False whenever any blocked row lacks a box, which withholds every scenario label in the ranking.

*Why it is likely to trigger.* The factor regex reads only "N x higher pricing" with an ASCII x. "5× higher pricing", "twice the price" or a band phrased differently would all be read as stating no factor. `aa_cost_caveat` also treats any AA note containing "cost", "price" or "pricing" as an omitted-term caveat.

*Status:* latent. Today's only footnote is Haiku's "5x".

*Change.*
- Send a no-factor caveat to the unresolved branch, as `unconstructible` does for O29 rows, and add a fixture asserting that no other row's label strengthens.
- Register AA's cost notes by exact text in a reviewed list, each with its factor recorded editorially. Stop the build on an unregistered note, as O64 does for agent rows, instead of relying on keyword and regex heuristics.

**L3. The adopted I79 L1 (date a change against the earliest possible measurement date) is not effective in the pipeline, and the specification body does not state it.**

*What the build does.* `change_flagged` and `post_change_ranks` now read `earliestEvidenceDate`. But both still require `candidate["expiry"] in {"possibly-superseded", "expired"}`, and `expiry_status` still tests `evidence_date(source) <= changed`, where `evidence_date` is the latest date (publication).

*Probe through `route_candidates`.* An undated measurement published 2026-10-06, a change dated 2026-10-01 and a release on 2026-10-25 give:
- expiry "fresh" and `earliestEvidenceDate` 2026-09-07;
- `change_flagged` False;
- a report pair dated 2026-10-20/21 does not outrank it (O78).

With the change dated 2026-10-08, the route is flagged.

*Why the test passes anyway.* The new assertion in `test_a_change_dated_before_the_measurement_never_supersedes_it` sets `expiry="possibly-superseded"` by hand. The rule therefore takes effect only once the route is past 30 days old, so its behaviour depends on age.

*The specification.*
- The body never states the earliest-date rule. The lifecycle trigger "a scoped change detected since measurement" (line 159) and the E144 clock (line 58, "Evidence age everywhere runs from the E194 observation date") read as the latest date.
- Only the r139 history entry claims the change.

*Status:* latent. Every recorded change postdates 2026-10-06.

*Change.*
- Have `expiry_status` read `measurement_span(...)[0]` for change detection.
- State the earliest-date rule in the lifecycle table's trigger cell and in E144.
- Replace the hand-set fixture with one built through `route_candidates`.

**L4. O95's rebase stops the build in its main case: when the replacing report pair is the plan's lowest figure.**

*What the build does.* `rebase_lower_of` sets `donorRouteId` to the lowest effective figure's id. When that figure is a report pair, the id is a measurement-object id (`"<route>#m1"`). `donor()` then raises "names an unknown donor measurement", inside `route_candidates`.

*Probe.* Sol at 10, Astra at 14 and a replacing Sol pair at about 12.1 give donor `sol-reports#m1` and a ValueError.

*Why the test misses it.* The O95 test only covers the branch where the other controlled figure (Astra, 14) is the lower one.

*Real cases.*
- On ChatGPT Pro 500 the lower-of donor is Sol's 10.772 against Astra's 13.91, so any admitted Sol pair below 13.91 stops the build.
- On Plus, any Astra pair below Sol's 10.55 does.

*A second gap.* `effective_measurement` applies neither the change-date checks of `change_flagged` (a change after V, or before the earliest date, is ignored there) nor a deterministic choice among several qualifying report routes. It takes the first in registry order.

*Status:* latent (no cell passes), and it fails loudly, so nothing wrong is published. But it would hold the first release in which O95 fires.

*Change.*
- Resolve donors in the measurement-object registry, or store the route ID and partition, so a transfer can rest on a pooled report object.
- Add the "pair is lowest" fixture.
- Reuse the `post_change_ranks` predicate in `effective_measurement`.

**L5. Disclosure gaps around O94 and O93.**

(a) **The caveat is not printed where the caveated row is named.** It is not printed beside the displayed-record (E203) results and companions that name a caveated row, although the O63 and route flags are (line 124). In scores.md the AI Coding Daily lower-quartile displayed cheapest is "Claude Haiku 5.5 (medium) ($45.91 …)" on API and "$0.78" on Plan, with no caveat. Nor is it printed in the E164 anchor provenance, "Official Plan anchors are set by Claude Haiku 5.5 (medium) on Claude Pro".

(b) **No row publishes its factor or range.** There is no factor, no [C, kC] cost range and no value range. `valuationGate.factor` and `bounds` are null, unlike O29's published current-tariff bounds (line 152). At 5C, Claude Haiku 5.5 (medium)'s AI Coding Daily API value would be:
- cost score 75.7 → 49.5;
- value 47.7 → 41.2;
- rank 11 → 15 of 16.

Claude Haiku 5.5 (high) would go from rank 9 to rank 15.

(c) **The active-rules manifest has no O94 entry** (E63, line 152), although O94 binds today: it removes an AI Coding Daily confirmed label and a scenario label.

(d) **Two passages still omit O93's per-model scope and O95's transfer rule.** I79 L4(b) was recorded as adopted, but:
- the manifest's fault-window detail still reads "yield to two concordant user reports for the plan";
- line 55 still says a fault-window measurement and every transfer on it stay flagged "until two concordant user reports for that plan admit a route, which then replaces it".

*Change.*
- Print "AA cost caveat" beside those lines.
- Publish `caveatFactor`, the cost range and the value range per basis on each O94 row.
- Add a manifest entry "AA cost omits a pricing term (O94)" listing its rows.
- Name O93 and O95 in the manifest detail and on line 55.

## 2. Methodology design recommendations

1. **One anchor-reference function with a declared purpose (M1).**
   - "Same panel as the frozen anchors" (E187, E205) and "today's freeze rule" (the freeze itself, a next-freeze preview, E64(b), E172) are two named calls of one function.
   - Each diagnostic's published label names which call it uses.
   - The preview diagnostic also runs the clip gate. That is how the owner sees in advance what O94 does at the next re-freeze (today: three Claude Haiku 5.5 (medium) plan rows clip inside the allowance).

2. **Make O94 a first-class evidence status (L1, L2, L5).**
   - A reviewed register of AA cost notes, by exact text, with the editorially recorded factor; an unregistered note stops the build.
   - B_W defined as the union of O29 hulls and O94 ranges.
   - A caveat with no factor sent to "unresolved".
   - Each caveated row's [C, kC] cost range and value range on both bases printed beside its rank, the analogue of E170's current-tariff bounds.

3. **One measurement span for every date predicate (L3, L4).**
   - `expiry_status`, `change_flagged`, `post_change_ranks`, `effective_measurement` and `in_fault_window` all read `measurement_span`.
   - O95's effective figure is computed by the same predicate the comparator uses.
   - Transfers may rest on pooled report objects.

## 3. Questions for the owner

1. **Single-donor transfers after a replacing report pair** (the common Claude assumption, and any other owner-named transfer with one donor).
   - *The asymmetry.* O95 makes a GPT lower-of transfer follow its donor's replacing report pair. E144 keeps a single-donor transfer on its named donor measurement until an editor names a new one.
   - *Today's exposure.* The Claude routes are change-flagged from 2026-10-17 (O79). An admitted Claude Opus 5.5 pair dated after that change would replace Opus's own routes (O78, and O89 for its other efforts). But the 10 + 26 Sonnet and Haiku transfer rows would keep the superseded SemiAnalysis figure, flagged, until they age out.
   - Should such a transfer:
     - (a) keep its named donor (as now);
     - (b) follow the donor model's replacing figure, as O95 does for lower-of transfers (recommended for consistency); or
     - (c) become diagnostic (API fallback) once its donor has been outranked for its own model?

## 4. Verdict

There are no Critical or High findings, one Medium and five Lows.
- The figure check exits 0, and all 1,620 Python tests pass.
- Quality, cost scores, anchors, values, ranks, exchange rates, allocations, cohort, admission, report cells, flag counts and the O94 label effects recompute exactly in both rankings.
- O95, the I79 L2 meter-period window, the README legends and the AI Coding Daily manifest do what the ledger says for the cases they test.

**The Medium:**
- M1: O94's "never an anchor reference" was implemented in the shared anchor-population function. As a result:
  - the published frontier-families diagnostic (E187) in the AI Coding Daily ranking now reports 10 Plan rank changes (2.04 against 1.85 value points per cost doubling) under a frontier-family label, while the draft says it equals the primary outputs;
  - E64's "freeze rule" rebuild still keeps the caveated rows;
  - the anchor-eligibility definitions on lines 47 and 63 omit O94.

**The Lows:**
- L1: E183, E186, Θ and E198a still describe O29 blockers only, and the counts exclude O94 rows.
- L2: a caveat without a parsable factor drops its row and can create another row's confirmed label (latent).
- L3: the earliest-date rule of I79 L1 is gated by an `expiry_status` that still uses the latest date, and is absent from the body.
- L4: O95's rebase stops the build when the replacing pair is the lowest figure (latent).
- L5: caveat, factor, manifest and O93 wording gaps in the disclosures.

Under O56 this round is not clean (one Medium). The Claude Opus 5.5 xhigh rung's clean count stays at zero.

VERDICT: HAS FEEDBACK
