# Internal review I79 — Claude Opus 5.5 (effort xhigh) on draft r138

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r138`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r138 (seventy-eighth internal review, the first clean one at Opus 5.5 xhigh, and owner decision O93) puts the fault rule in the comparator key and the O73 sentence, keeps a change dated before a measurement from superseding it, counts fault-window rows in Output 1, shows route flags in both rankings' tables, and publishes the report-cell verdicts and the post-O71 owner decisions in the generated docs. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "generated docs. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end: O45–O93, E247–E270, I29–I78 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i78-claude-opus-5.5-xhigh.md`, and how the ledger resolved it:
  - L1, L2, L4, L5 and L6 were recorded as adopted. L4 and L5 were adopted only in part (see L3 and L4 below).
  - L3 was rejected with a reason.
  - Q1 became O93.
- `draft-r138.md`, every line (1–174), in sequential chunks: 1–17, 18–30, 31–40, 41–49, 50–51, 52–54, 55, 56–57, 58, 59–62, 63–66, 67–87, 88–97, 98, 99–105, 106–116, 117–134, 135–136, 137–147, 148–151, 152 (two halves), 153–173 and 174 (two halves).
- A sentence-level diff of `draft-r137.src.md` against `draft-r138.src.md`. The hand-written changes are:
  - comparator key (2);
  - the O73 sentence;
  - the fault-window paragraph under the lifecycle table, which replaces the table row;
  - Output 1 and the limitations (`planFaultRows`);
  - the r138 history entry.
- The HEAD commit's code and data diff:
  - `plan_routes.py`: `post_change_ranks`, `change_flagged` and `in_fault_window`;
  - `emit_docs.py`: flag legend, `o72Application` and the report-cell table;
  - `draft_figures.py`;
  - tests, AGENTS.md, README.md, scores.md, methodology.md and `figures.json`.
- Code read:
  - `plan_routes.py` and `plan_admission.py`, in full;
  - in `value_v3.py`: route-candidate setup, `interval_outputs`, `plan_boxes`, `plan_variants` use and the manifest;
  - `site/evidence.py`.
- Data and documents read or queried: `data/plan_cost_routes.json` (routes, `evidencePolicy`, `changeDetection`), `data/plan_reports.json`, `data/swe_tracks.json`, `data/aa_frontier_capture.json`, `data/price_records.json` and `data/scores.json` (both rankings).
- The O71 record, spot-checked:
  - NicoAica's two Max 20x rows against `research_notes/Plan allowance user reports/anthropic.md`;
  - the three Google AI Pro rows against `stage1-google.md`.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- All 1,617 collected Python tests pass (exit 0). I ran them excluding `e2e` and `js`, with bytecode writing and the pytest cache off.
- `git status` was clean before I wrote this file.

**Arithmetic, recomputed independently from `data/scores.json` and `quality.TRACKS`, for both rankings.** There is no mismatch in 9 + 16 rows or 27 + 51 plan rows.
- Displayed quality.
- Cost scores on each row's own workload anchors.
- Values and competition ranks, API and Plan.
- One representative plan row per configuration.
- Anchors, each the cheapest reference ÷ 2 and the dearest × 2. The reference counts are:
  - max-effort: API main 8, Plan main 23, API subset 9, Plan subset 27;
  - AI Coding Daily: API 16, Plan 51.
- Exchange rates: 3.04 (4.06), 2.44 (3.25), 2.83 (3.77) and 1.85 (2.46).

**Generated figures**
- Plan rows: 27 and 51.
- API-fallback rows: 2 and 3.
- Rows flagged possibly superseded or expired: 21 and 44.
- Fault-window rows: 3 and 8. These are the Pro 500 rows of:
  - GPT-6.1 Sol, GPT-6 Astra and GPT-6 Luna (max-effort);
  - GPT-6.1 Sol (high, medium), GPT-6 Astra (high), GPT-6 Luna (max, xhigh, high, medium) and GPT-5.6 Luna (low) (AI Coding Daily).
- Unverified-basis rows: 21 and 44.
- Assumption kinds: 10 + 4 and 26 + 4.
- Separability tolerances: 2^(2.762/3.042) = 1.88 and 2^(2.763/2.439) = 2.19. The Plan bands agree with `valueSd` on spot checks.

**Cohort, recomputed from the capture**
- 19 path vertices, each matched to one circle at 0 px, rising strictly.
- 11 near points, with gaps 1/1/1/1/2/3/3/3/3/3/3.
- 13 families: 8 frontier and 5 near-only.
- Tooltip ties at 38 (three points) and 56 (two).
- The first vertex is the cheapest of the 190 plotted points, and none lies left of it.

**Plan evidence**
- `planAllowanceCells`: 52 cells, 28 of them listed, none passing. Google AI Pro fails at 11.4 ÷ 8.47 = 1.35×.
- The current-partition contents of every cell.
- NicoAica's straddling Max 20x measurement splits at 2026-10-17T13:00Z exactly as `partition()` reads the instant.
- The fault days and partition splits in the registry match the draft's list.
- `evidence.faultedRoutes` names the two SemiAnalysis Pro 500 measurements.

**Fixtures in the text**
- The ladder positions for n = 32, 9 and 15.
- The arcsine kernel fixture: 86.8% by a 2-million-draw Monte Carlo, against the draft's "about 86.7%".
- The E89, E43, E50, E95/E140, E148 and E152 fixtures.
- The Omniscience vectors.
- DeepSeek's LiveBench weighted Overall, 666.2 / 9 = 74.02.

**Generated documents**
- README's Flags column and legend.
- The scores.md report-cell table.
- The AI Coding Daily interval and scenario-label sections.
- methodology.md's new `o72Application` line.
- Both release manifests.

**Not verified:** live pages, the paywalled SemiAnalysis article and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. A row whose AA cost AA itself says omits a 5× tariff term is fully label-eligible. Today that cost decides two labels, one frontier status and an anchor.**

*The source's own warning.* AA's model page carries this note on every Claude Haiku 5.5 row: "Claude Haiku 5.5 has 5x higher pricing on longer-context inputs which are not currently reflected; we are working to include this in cost figures across Artificial Analysis". It is in `rows[].aaCostCaveat` for Haiku 5.5 (max), (high) and (medium). The build already knows what the note means: those rows carry `valuation.providerBillingRule = "banded tariff not reflected in AA's cost (AA cost caveat)"` and `tariffCorrectedValuation = "unidentified: billing-band allocation unavailable"` (E157).

*The other record defects all deny labels.* The label-eligibility predicate (E92, line 135) denies labels whenever the published record is known not to be the configuration's economics at V or its exact evidence:
- a price not in force (O29);
- an unverified valuation basis (E202, E222);
- a provider-claimed leaf (E233);
- a change-flagged Plan route (E228).

O29 also keeps such a row out of the anchor references (E184). The omitted-band case is routed away from the valuation gate ("a band that AA's figure omits under an unchanged tariff stays under E157 (AA cost caveat), not this gate", line 152). But nothing then denies its labels or bounds its cost, so it competes and earns labels as if its cost were complete.

*What this decides in the AI Coding Daily ranking today (scores.json `v3Tracks.aicd`):*

1. **The lower-quartile bar's interval label.** At quality 38.0, the status is certified and `confirmedCheapest` = Claude Haiku 5.5 (medium), at $45.91. The only cheaper-or-close possible qualifier is the bar's own configuration, GPT-6 Luna (xhigh), at $49.41.
2. **The scenario label at the same bar.** scores.md's label table gives "Claude Haiku 5.5 (medium) — supported under all registered role-group kernel checks — Label: yes".
3. **A frontier status.** GPT-6 Luna (xhigh)'s possible-frontier membership is "disproved", with `possibleBlockedBy` = Claude Haiku 5.5 (medium) alone.
4. **The Plan anchor.** The official Plan low anchor, c_L = 0.390, is Haiku (medium) on Claude Pro ($0.78) ÷ 2. This is the setter the E164 calibration names.

*Why the omission could matter.* All three of the first statuses turn on a 7.6% cost margin (49.41 / 45.91). On Haiku 5.5 (medium)'s Index tokens and AA's displayed prices:
- output carries about $26.9 of the $56.36 Index cost;
- input-side categories carry about 52%.

Using the Index-wide split as a proxy for the basket, a 5× surcharge on about 4% of the input-side spend erases the margin (0.076 ≈ 4 × 0.037 × 0.52). AA-LCR (long-context reasoning) and multi-turn agentic tasks such as Briefcase, GDPval and Terminal-Bench are in the basket. So the "confirmed" claim and the 100% scenario label are not robust to a term the source says is missing.

*What is new against the ledger:*
- E141 and E157 (reviewers 41 and 47) decided only how the caveat is shown and that the tariff-corrected cost stays unidentified.
- E170 kept the case out of the valuation gate.
- No entry examines label eligibility or anchor eligibility for such a row.
- The interval and scenario labels above are current outputs, not latent ones.

*Why this is Medium.* A published claim ("confirmed cheapest", the interval output the draft calls "the claim") and a scenario label are issued on a cost the build itself records as unidentified. One frozen anchor also rests on it. This weakens the objective's "actually lowest cost" for the second ranking. It is not High: the claim is scoped to the published record (O25, E51), and the size of the omission is unknown.

*Change.* Recommended: (a). Minimum: (b).

(a) **Compete over a current-tariff hull, as O29 does.** Add a row to B_W (E183) when its AA cost carries an AA-stated omitted tariff term in force at V (E157 `tariffCorrectedValuation` = "unidentified" because of a banded tariff).
- Its cost domain is the hull of its published cost and the E170 current-tariff bound, with r = banded price ÷ applied price over the input-side categories with positive demand. With the 5× band and no zero-demand evidence (E185), that gives C' ∈ [C, 5C].
- The provider's band price is public, from its own price page.
- It competes, can deny but never earn a label, and is not an anchor reference at the next freeze. The frozen anchors persist until then (E184).
- Today:
  - Haiku (medium) and (high) earn no AI Coding Daily labels;
  - the lower-quartile bar has no confirmed cheapest: GPT-6 Luna (xhigh) is possible, and Haiku (medium) is a blocker over its hull;
  - GPT-6 Luna (xhigh) becomes a certified possible-frontier member;
  - the AI Coding Daily Plan low-anchor setter is disclosed as caveated until the re-freeze.

(b) **If the owner prefers not to widen Θ:** label-deny such rows at their published point, as E222 does (compete, deny, never earn, "withheld" own statuses). Print "AA cost caveat" beside every frontier, bar and scenario result that names a caveated row.

Either way, add the case to E92's blocker list and to E184's anchor eligibility, with a fixture: a caveated row 7% cheaper than the next possible qualifier yields no confirmed label. See Q1.

### Low

**L1. The new "change dated before the measurement" rule compares with the latest possible measurement date, not the earliest.**

*What r138 does.* r138 makes `change_flagged` and `post_change_ranks` ignore a change dated before `evidenceDate`, as `expiry_status` already did.

*Why that end is wrong.* For a measurement with no window, `evidenceDate` is its publication date. That is the latest date it can have been taken, while the fault test dates the same measurement by the 30 days ending on publication (`in_fault_window`). So a change dated after the measurement but before its publication is treated as "before the measurement". It then never flags the route (E18, E228) and never lets a post-change pair replace it (O78).

*Example.* SemiAnalysis measures in late September, the provider changes metering on 2026-10-03, and the article appears on 2026-10-06. The registry text even bounds the ChatGPT measurements' start: "post-September 29 Codex schedule".

*What is new against I78 L2.* I78 L2 asked for a change to count when *earliest* ≤ change ≤ V. The adopted code uses the publication date, which makes the gap one-sided in the anti-conservative direction for undated measurements.

*Status:* latent; no change is dated before 2026-10-06 today.

*Change.* In `expiry_status`, `change_flagged` and `post_change_ranks`, compare the change with the measurement's earliest date. That is the window start, else the same 30-day span the fault test uses, or a recorded regime-start date (2026-09-29 for the ChatGPT routes, now text only). Add the fixture above.

**L2. The point convention for unstated report windows defeats O83 and O78 for meter-fraction reports.**

I78 L3 was rejected on the ground that "reading an unstated report window as 30 days would exclude reports on evidence they do not give". That proposal was not 30 days. It was the meter's own window: 7 days for a weekly meter.

*What is new:* the convention's interaction with O83 and O78.
- E270 (line 57) says a meter fraction "measures the allowance of its own window". A weekly reading on day D therefore prices consumption since the account's last weekly reset, inside [D − 6, D]. That is evidence the report gives by construction.
- Under the point convention, a weekly reading dated the day after a split counts wholly after it (`partition()`). It also "postdates" the change for O78 (`earliest_report`). Yet up to six of its seven metered days may precede the change.
- That is what O83 forbids: "a report from before the split never counts after it".
- At this release OpenAI's current partition is 2026-10-24 to 2026-10-25. Any unstated-window weekly OpenAI reading dated in it would count as post-split, although almost all of its window precedes the 2026-10-23 split.

*Status:* latent; no such report is in the table.

*Change.* For a meter-fraction report with an unstated window, run the fault, split, window and O78 tests on [D − meter window + 1 day, D], failing closed. Keep the E194 observation date unchanged. Otherwise, state in E270 why O83 does not apply to meter windows.

**L3. I78 L4 is recorded as adopted, but three of its four changes are absent.**

The ledger (I78 L4) records Output 1, the limitations and the manifest rule. Not done, and not recorded as declined:

*Route flags beside the Plan displayed-record results and companions.* Today the max-effort Plan displayed-record cheapest row at the headline and lower-quartile bars is GPT-6.1 Sol (max) on ChatGPT Pro 500. So is the lower-quartile noise-margin companion. That row is change-flagged and inside the fault window. README (lines 135–137) prints only the O63 safety flags beside these results, and `displayedCheapest` carries no route flags.

*`faultWindow` on measured-only entries.* The measured-only view ranks the same Pro 500 route second, with `crossEffort` but no fault marker.

*E63's description (line 152).* It names the Plan lifecycle entry but not the fault-window manifest entry that both manifests now publish.

*Change.* Do them, or record in the ledger that they were declined and why.

**L4. Several generated statements overstate or mis-cite the rules r138 added.**

(a) **README's "route possibly superseded" legend** reads "it stays selected and earns no interval label (E228)".
- Under the lifecycle table and `change_flagged`, a route possibly superseded by *age alone* is no blocker.
- The same README label is also printed for "expired" routes.
- It is true today only because every flag has a detected change.

(b) **The fault-window wording.** README's "fault window" legend and both manifests' details say the rows yield "to two concordant user reports for the plan".
- Under O93, the six transfer rows that carry the flag yield only to their own model's pair (or their donor's replacement; see L5). These are GPT-6 Luna (max) in both rankings, and GPT-6 Luna (xhigh, high, medium) and GPT-5.6 Luna (low) in the AI Coding Daily ranking.
- AGENTS.md and the draft's lifecycle paragraph already say "for that plan and model".

(c) **methodology.md's new "Plan evidence after the O71 search" line** (`o72Application`):
- it is headed "O72-O92", omits O93's per-model scope, and ends "for that plan";
- it cites "(O80, O82)" for "never converts", but O80 allowed a conversion and O82 withdrew it.

(d) **I78 L5's remainder is still open.** The AI Coding Daily release manifest and Plan route-selection table remain absent from scores.md.

*Change.* Generate the legend from the lifecycle predicates. Name O93 in `o72Application` and in the manifest detail. Cite O82 alone. Add the AI Coding Daily manifest.

**L5. O93's "or their donor's route is replaced" has no defined effect in the draft or the build.**

O93 (ledger) says that other models' routes on the plan, and the transfers and O88 routes resting on them, "keep the fault flag until they get their own pair or their donor's route is replaced".

*What the build does.* It sets `faultWindow` from the donor *measurement* (`in_fault_window` over `[route, donor]`). Under E144 that donor is immutable, so the flag never depends on the donor model's selection.
- Take an admitted GPT-6.1 Sol pair on Pro 500. It would replace Sol's own routes.
- It would leave GPT-6 Luna's Pro 500 transfer resting on the faulted Sol measurement, flagged, and on the same multiple (O45's lower-of rule reads SemiAnalysis figures).

*Two readings.*
- If "the donor's route is replaced" means the donor *measurement* is superseded by naming (E144), the build is right, and the draft should say so.
- If it means the donor model's selection, the build does not implement it, and the transfer's multiple question arises: does the transfer keep resting on the faulted measurement?

*Status:* latent; no cell passes. See Q2.

## 2. Methodology design recommendations

1. **Derive label eligibility from record-defect statuses (M1).**
   - Build E92's `blocker(i)` from the row's own status fields:
     - valuation-gate outcome 3 or 4;
     - `tariffCorrectedValuation` = "unidentified" because of a banded tariff;
     - provider-claimed leaf;
     - change-flagged Plan route.
   - Do not keep a hand list in `interval_outputs`.
   - Add a test that every status marking the published record as not the configuration's economics at V denies labels and anchor-reference eligibility.
   - For caveated rows, give the cost domain the E170 current-tariff hull, from the provider's published band price, and compete in B_W (E183).
   - This also closes the "one label-denial function" recommendation recorded after I76, with a concrete case it missed.

2. **One measurement span read by every date predicate (L1, L2).**
   - Give every measurement object and report a span [earliest, latest]:
     - the stated window;
     - else, for a controlled measurement, the recorded regime start or publication − 29 days, through publication;
     - else, for a meter-fraction report, [D − meter window + 1, D].
   - Have `expiry_status`, `change_flagged`, `post_change_ranks`, `in_fault_window`, `on_fault_day`, `partition` and O78's `earliest_report` read only that span. A change counts when earliest ≤ change ≤ V, and a report postdates a change only when its earliest day does.
   - No verdict, selection or flag changes today.

3. **Finish the route-flag disclosure (L3, L4).**
   - Print each Plan displayed-record result's and companion's route flags beside the O63 flags.
   - Add `faultWindow` to measured-only entries.
   - Add the AI Coding Daily manifest to scores.md.
   - Generate every legend sentence from the predicate it describes, and test it against the lifecycle table's cells.

## 3. Questions for the owner

1. **M1. A source-stated omitted price term.** AA says Claude Haiku 5.5's published cost omits its 5× long-context input price. Should such a row:
   - (a) compete over a current-tariff hull with no label of its own, like an O29 row (recommended);
   - (b) be label-denied at its published point, like E222; or
   - (c) keep labels on its published record under O25, with "AA cost caveat" printed beside every claim that names it?

   Today the answer decides the AI Coding Daily lower-quartile bar's confirmed and scenario labels (Claude Haiku 5.5 (medium)), GPT-6 Luna (xhigh)'s frontier status, and whether that ranking's Plan low anchor stays a caveated row at the next re-freeze.

2. **L5 and O93. A transfer resting on a fault-window measurement.** Take GPT-6 Luna's Pro 500 transfer, whose donor is SemiAnalysis's Sol measurement. If a GPT-6.1 Sol report pair on Pro 500 replaces Sol's own route, should the transfer:
   - (a) keep the faulted donor, multiple and flag until GPT-6 Luna's own pair arrives (what the build does);
   - (b) keep its multiple but drop the flag; or
   - (c) re-point to another donor?

   If (a), only the O93 wording changes. If (b) or (c), `route_candidates` needs a donor-replacement rule.

## 4. Verdict

There are no Critical or High findings, one Medium and five Lows.
- The figure check exits 0, and all 1,617 Python tests pass.
- The quality, cost-score, anchor, plan-cost, value, rank, exchange-rate, cohort, admission, report-cell and flag-count figures recompute exactly in both rankings.
- r138's changes do what the ledger says for I78 L1, L2 and L6 and for O93's comparator scope.

**The Medium:**
- M1: Claude Haiku 5.5 rows carry AA's own note that their cost omits a 5× long-context price. They are nevertheless label-eligible and anchor-eligible. Today one of them holds the AI Coding Daily lower-quartile bar's confirmed and scenario labels on a 7.6% cost margin, disproves GPT-6 Luna (xhigh)'s frontier membership and sets that ranking's Plan low anchor.

**The Lows:**
- L1: the pre-measurement change exemption uses the publication date, the latest possible measurement date.
- L2: the point convention for unstated windows lets a weekly meter reading count wholly after an O83 split or O78 change.
- L3: three parts of I78 L4 are not done, though the ledger records it as adopted.
- L4: the new legends and methodology text overstate E228 and omit O93.
- L5: O93's donor-replacement clause has no defined effect.

Under O56 this round is not clean (one Medium). The Claude Opus 5.5 xhigh rung's clean count restarts.

VERDICT: HAS FEEDBACK
