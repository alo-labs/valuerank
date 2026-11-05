# Internal review I82 — Claude Opus 5.5 (effort xhigh) on draft r141

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r141`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r141 (eighty-first internal review, at Opus 5.5 xhigh, and owner decision O97) gives the comparator and every route following a donor one replacement test, covering a model's report pairs registered under any of its configurations, has an O88 route that follows a replacing report pair take the pair's grade, reads AA's cost note only for a sentence that names an omitted price, takes the largest stated factor, and decides an unboundable O94 row on every workload. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "every workload. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1845): O45–O97, E247–E270, I29–I81 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i81-claude-opus-5.5-xhigh.md`, and how the ledger resolved it:
  - L1 became `pair_replaces`, `report_covers` and the comparator-ordered choice in `effective_measurement`.
  - L2 became O97.
  - L3 was modified: a sentence-level caveat reading instead of a footnote register.
  - L4 was adopted.
  - Recommendation 3 was deferred.
- `draft-r141.md`, every line (1–174), in 20 sequential chunks of at most 18,000 characters. Lines 152 and 174 were each read across two chunks.
- A sentence-level diff of `draft-r140.src.md` against `draft-r141.src.md`. The hand-written changes are lines 47, 55, 58 (E144, two clauses), 63, 116 (E183), 123, 135 (BlockerSafe reading, E228 earliest day) and the r141 history entry.
- The HEAD commit (37a3ab5) diff. It touches `plan_routes.py`, `value_v3.py`, `publication.py`, `site/viewmodel.py`, the four test files, AGENTS.md and the ledger. No published output (data, site, README, methodology, scores, raw-data) changed in r141.
- Code read in full for the functions involved:
  - `plan_routes.py`: `grade_rank`, `post_change_ranks`, `evidence_grade`, `donor`, `evidence_date`, `expiry_status`, `report_date`, `measurement_objects`, `change_flagged`, `measurement_span`, `in_fault_window`, `model_base`, `report_covers`, `pair_replaces`, `effective_measurement`, `rebase_lower_of`, `_rebased`, `rebase_transfer`, `route_candidates`, `admission_table`, `comparison_tuple`, `dominance_filter`, `_order`, `route_selection` and `plan_cost`.
  - `value_v3.py`: `_gated_box`, `_caveat_sentences`, `aa_cost_caveat`, `caveat_factor`, `blocker_domain`, `api_candidates`, `plan_candidates`, `_boxes`, `interval_outputs`, `withheld_label`, `cost_removal`, `plan_amount`, `_amount_derivation`, `blocker_safe` and the route assembly (lines 785–945).
  - `intervals.frontier`, `cheapest_above_bar` and `_possibly_cheapest`; `plan_admission` (`model_of`, `window`, `partition`, `exclusion`, `evaluate`, `check_routes`); `draft_figures` (the `mainWorkloadRows` figure).
- Data read or queried:
  - `data/scores.json` (both rankings);
  - `data/v3_frozen.json` and `data/v3_frozen_aicd.json`;
  - both scenario files;
  - `data/plan_cost_routes.json` (all 137 routes, `evidencePolicy`, the splits and fault days, `o72Application`);
  - `data/plan_reports.json` through `planAllowanceCells`;
  - `data/swe_tracks.json`, `data/source_rereads.json`, `data/aa_frontier_capture.json` and `data/figures.json`;
  - `methodology.md` line 167.
- The O71 record, spot-checked: the Google AI Pro cell (Muhammed_Alpler 8.47, Faheem_Anis1 11.4–13.4) against `research/2026-10-25-plan-allowances/stage1-google.md`.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- 1,624 Python tests pass (e2e and js excluded; bytecode writing and the pytest cache off).
- `git status` was clean before I wrote this file.

**Reproduction.** I exported HEAD to my scratchpad and ran `build_scores`, then the Python steps of `build:docs`, at the pinned clock (2026-10-25T09:56:47Z). The results match the committed files byte for byte:
- every `data/*.json`;
- README.md, methodology.md, scores.md and raw-data.md;
- `data/figures.json`;
- the whole `site/` tree.

So the r141 code produces exactly the published r140/r141 outputs.

**Arithmetic, recomputed independently.** There is no mismatch anywhere:
- displayed quality from the leaves and `quality.TRACKS` (13 and 11 leaves, each summing to 100), for 9 + 16 rows;
- cost scores on each row's own anchor object;
- API and Plan values and competition ranks (27 + 51 plan rows);
- every anchor (cheapest ÷ 2, dearest × 2);
- the exchange rates 3.04 (4.06) and 2.44 (3.25);
- the bar ladders at zero-based positions 2/4/6 and 3/7/11, and bar reach 7/5/3 and 13/9/5;
- the setters: Gemini 4 Argon (high) and MiMo-V2.6-Pro;
- the Plan flag counts:
  - fallback 2/3;
  - possibly superseded 21/44;
  - fault window 3/8;
  - unverified basis 21/44;
  - owner assumptions 14 (10 + 4) and 30 (26 + 4);
- separability: 0 of 8 and 1 of 15; narrow 3.25/3.21; wide 2.77/4.44;
- the noise margins 3.70 and 5.87;
- the allocations 106%/21% and −96%/−25%;
- the AICD band straddler GPT-6.1 Sol (medium);
- LiveBench's weighted Overall for five rows, from the captured table and `_overall_weights`.

**r141 code**
- `pair_replaces` is shared by `post_change_ranks` and `effective_measurement`.
- I81's probes (a)–(c) now behave as the ledger says.
- O97's grade, flag, evidence label and site grade work as built.
- The narrowed caveat reader returns factor 5 on the real Haiku note.

**Probes.** Scripts are in my scratchpad. They use the repository's functions on the real route registry plus synthetic report routes:
- a GPT-6.1 Sol pair on ChatGPT Plus;
- an Opus 5.5 pair on Claude Pro, with and without `requiredVariant`, at releases 2026-10-25, 2027-01-20 and 2027-02-10;
- six rephrasings of the Haiku note, run through `caveat_factor`;
- one rephrasing rebuilt end to end through `build_scores` in a scratch copy.

**Not verified:** live pages, the paywalled SemiAnalysis article and the scenario draws themselves (their input hashes match).

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. The "one replacement test" still lets a donor model's own row and the routes resting on it take different figures, through two candidate-set differences the r141 fixtures do not cover. Line 55 now states that they cannot differ.**

*What line 55 says.* "One replacement test decides both the donor model's own row and every route resting on it: the comparator's (a flagged change on or after the measurement's earliest possible day, or a fault window), several replacing pairs being ordered by the comparator's keys."

*Why it is not so.* r141 shares the predicate (`pair_replaces`), but the two paths still feed it different candidates.

- **(a) `requiredVariant` on a report route.** The registry's only report route (SuperGrok Heavy) carries `requiredVariant: "xhigh"`, so this is the pattern an editor would copy.
  - `route_candidates` drops a route whose `requiredVariant` is not the configuration's effort.
  - `effective_measurement` deliberately bypasses that filter, by passing the route's own variant as the effort.
  - Probe: real registry plus an Opus 5.5 pair on Claude Pro (30.0 and 31.0, reported 2026-10-20 and 21), registered for `claude-opus-5-5-high` with `requiredVariant: "high"`. `check_routes` would accept it, because it keys by AA family.
    - Claude Opus 5.5 (max) keeps the flagged SemiAnalysis measurement at 58.9×. The admission table classes the pair as case 1, an execution-identity incompatibility. That contradicts E106 case (1)'s O87 carve-out for plan-allowance evidence.
    - Claude Opus 5.5 (high) and (medium), through O88 and O97, and Claude Sonnet 5.5, through the transfer, all take 30.5×.
  - One model therefore carries two multiples (against O89), and its own row keeps a figure O78 says the pair outranks. Without `requiredVariant`, all four rows take 30.5×. This is the I81 L1(b) symptom, back through a different field.
- **(b) A demoted donor.** `effective_measurement` tests the change only when `expiry_status` is "possibly-superseded" or "expired". The comparator needs no test at all once the measurement is "demoted", because the measurement is then diagnostic and the pair is the only eligible route.
  - Probe: the same pair, reported five and four days before each release.
    - At 2027-01-20 (age 106, expired) every row follows the pair at 30.5×.
    - At 2027-02-10 (age 127, demoted) the Opus rows take 30.5×, but Claude Sonnet 5.5 on Claude Pro has no eligible route and falls back to API cost: its transfer's donor is demoted and is not treated as replaced.
  - O96 ("takes its donor model's effective figure… No row keeps a superseded figure") and E144 ("a transfer is diagnostic-only whenever its donor is") point different ways here. The code decides between them through an incidental expiry-stage test, and the result flips on one day. This is latent until 2027-02-04 and needs a pair.
- **(c) Identification class.** The comparator ranks identification class (key 1) before the O78 grade demotion (key 2). An identified, change-flagged measurement therefore keeps the donor's own row against an unidentified pair. `effective_measurement` replaces it unconditionally. This is far-latent: no route has an identified M_W.
- **(d) Coverage by ID text.** `report_covers` matches configurations by stripping an effort suffix from the ID (`model_base`). `plan_admission.model_of` keys cells by AA family and says "never by parsing the ID" (I69 L2). The two agree for every configuration in today's map. But `qwen3.8-max` would cover any future `qwen3.8-*` configuration, a model of another family.

*Status:* latent; no report cell passes.

*Change.*
- Make (a) unreachable: ignore `requiredVariant` for report routes (O87), or refuse it in `check_routes`.
- Decide replacement independently of the measurement's later demotion. Better still, take the effective figure from the comparator's own selection for the donor configuration (recommendation 1).
- Key `report_covers` by the families map the build already passes to `check_routes`.
- Add fixtures for (a) and (b).

**L2. An O88 route that follows its donor to a report pair (O97) keeps the SemiAnalysis measurement's provenance in its published amount and admission-table entry, and O97 is missing from the published summary.**

*Probe.* Real registry plus a GPT-6.1 Sol pair on ChatGPT Plus (5.0 and 5.2, reported 2026-10-18 and 19). For GPT-6.1 Sol (xhigh), the selected follower has grade "reports", the O97 flag and a 5.099× multiple. However:
- **E166 amount (`plan_amount`).** The amount is **$211.00**, with the derivation "measurement record: its recorded numerator U_obs = M_obs x F_obs (applied estimate)". But 5.099 × $20 = $101.98.
  - `_rebased` overrides only the donor ID, the multiple, the source model and the class.
  - The route keeps SemiAnalysis's `apiEquivalentUsd`, `numeratorKind`, `measurementWindow`, `sourcePublicationDate` and `measurementWorkload`.
  - So the published amount and workload describe a different object from the multiple, against E168: "M × F reproduces an amount only within one object". The rebased owner-named transfer is correct, at $101.98, because its kind multiplies.
- **Admission table (E106).** `admission_table` publishes `crossEffort: true` for the follower. It reads the unrebased registry route, so the E106 table still marks the row as measured at another effort.
- **E144 (line 58, new in r141).** The text says the transfer "publishes the ID it was rebased from". `rebasedFrom` is set on the internal route dict, but no output carries it: neither `plan_cost`, the row's `plan` block nor the docs.
- **The published summary.** AGENTS.md says the follower takes the pair's "grade and provenance" (O97). But the registry's `o72Application`, which `methodology.md` line 167 and the site render, ends at O96 ("Owner decisions O72-O96"). The published methodology summary does not state O97.

*Status:* the first three are latent. The fourth is current text.

*Change.*
- Rebase by substituting the pair's measurement object as a whole: numerator, kind, workload, window, dates and capacity status. Do not override four keys.
- Read `crossEffort` from the candidate's route.
- Publish `rebasedFrom`, or drop the clause from E144.
- Add a fixture asserting that a rebased route's E166 amount equals the pair's M × F.
- Add O97 to `o72Application`.

**L3. The narrowed AA caveat reader fails closed on ordinary rephrasings of the one real note. That silently removes every API interval claim in both rankings, although the stated factor never decides a label.**

*New against the I81 L3 resolution.* The ledger kept the reader because it "fails closed on every case I81 tabled". It also fails closed when AA splits this very caveat across two clauses. `caveat_factor` requires every caveat sentence to carry a factor. Results:

| Phrasing (same 5× caveat) | Factor read |
|---|---|
| the real note (one sentence, then "we are working to include this…") | 5.0 |
| "…has 5x higher pricing on longer-context inputs. These prices are not included in our cost figures." | none |
| "…which are not currently reflected. This is not included in cost figures yet." | none |
| "Long-context inputs are priced 5x higher; this pricing is not reflected." | none |
| "…has higher pricing (5x) on longer-context inputs which is not reflected." | none |
| "Inputs above 200k tokens cost 5x more and are not reflected in cost figures." | 5.0 |

*End-to-end test.* I rebuilt with the second phrasing in a scratch copy. The note sits in `aa_reconciliation_inventory.json` and `aa_reconciliation_report.json`. The result:
- every API interval output turns "unresolved": the max-effort main workload, its subset workload and the AI Coding Daily main workload;
- so are their confirmed cheapest results (GPT-6.1 Sol (max), DeepSeek V4.1 Flash 1017 (max), Claude Opus 5.5 (medium)) and their definite-frontier results;
- `aaCostCaveatFactor` and the cost range turn null;
- there is no hold and no build stop;
- the reason string reads "a blocker's current-tariff domain cannot be constructed (E183, E185)", which names the O29 mechanism, not O94.

AA's own note says it is "working to include this in cost figures", so a text change is expected.

*Why the cliff is unnecessary.* The upper end of an O94 box never decides a label.
- `intervals.frontier` disproves a definite membership with a competitor's `c_low`.
- `cheapest_above_bar` confirms cheapest against rivals' `c_low`.
- `blocker_safe` tests `box.c_low`.
- Only possible-frontier membership and K_r (`_possibly_cheapest`) read a competitor's `c_high`.

A missing factor therefore leaves every label decidable at the published cost C, and only possible memberships depend on it.

*Smaller points in the same path.*
- `AA_OMISSION` also treats "higher pricing" alone as an omission. Line 116 names only "does not reflect" (with the ledger's "not reflected, included or counted, or excluded or omitted").
- A stated factor below 1 is silently clipped to 1 (`max(1.0, factor)`).
- The O29 half of `unconstructible` is still not restricted to the boxes' candidates, although the ledger says "the unconstructible test now uses the same candidate set as the boxes". An O29 row that could not compete on a workload or basis still makes that output unresolved.

*Status:* latent; the real note reads correctly today.

*Change.* Either:
- use the half-line [C, ∞) for a factorless caveat (recommendation 2; this touches O94's fail-closed clause, Q1); or
- stop the refresh on any changed footnote text (I81's register).

In either case:
- name O94 in the reason string;
- restrict the O29 half to the candidates;
- align line 116 with the "higher pricing" term.

**L4. Line 35's "R_W" count includes the O94 rows that E183 and line 123 place outside R_W.**

- Line 35 says: "R_W on the API main workload (cohort rows with FullCost) 8 in the max-effort ranking … and 16 in the AI Coding Daily ranking; the admission reference panel, the anchor references and the common-workload panel for cost influence are the same rows". The figure is `{track}.mainWorkloadRows`, a count of main-workload rows.
- E183 (line 116) puts the O94 rows in B_W, "rows … that would otherwise belong to R_W".
- r141's line 123 says the interval outputs "count R_W, the main-workload rows with FullCost that are not blockers … the O94 rows among them, which compete in B_W instead".
- The published interval universe is 7 and 14.

So "Counts, defined once" now contradicts both the definition and the figure next to it. The 8 and 16 are the admission and anchor-reference panels, not R_W.

A related wording point: line 106's E64(b) still says W∖TB is scored "on anchors rebuilt by the freeze rule from its evidenced reference panel". r141's line 47 now correctly says E64 and E172 rebuild from every row with a cost on the reduced workload; `cost_removal` applies the padding rule only, without the E160/E184 eligibility tests.

*Change.*
- Print R_W from the interval universe, as a new figure.
- Call the 8 and 16 "main-workload rows with FullCost (the admission and anchor-reference panels)".
- Say "rebuilt with the ln 2 padding from every row with a cost on W∖TB" on line 106.

## 2. Methodology design recommendations

1. **Take the effective donor figure from the comparator's selection, not only from a shared predicate (L1).**
   - For each (provider, plan, AA family), run the donor configuration's own route selection once. Its selected measurement object, whether the pair or the measurement, is the effective figure that O95, O96 and O97 read.
   - Report routes then enter both paths through one candidate set: AA-family coverage (O87), no `requiredVariant` on report routes, one treatment of demoted donors.
   - The donor's row and its followers then agree by construction. A fixture can assert that equality over every plan.
   - What is new against I81's recommendation 1: r141 shared the predicate, and the probes show that the predicate alone is not enough while the candidate sets differ (`requiredVariant`, diagnostic status, identification key).
2. **Give a factorless O94 caveat the half-line [C, ∞), and say in E183 that the stated factor only tightens possible memberships (L3).**
   - Every label test (definite frontier, confirmed cheapest, BlockerSafe) reads a competitor's lower cost, which is the published cost C.
   - With [C, ∞), a rephrased or factorless note leaves every claim decidable and still sound: an infinitely dear blocker never removes a possible membership.
   - The parsed factor then only narrows possible memberships and K_r, and a misread factor can never create a label.
   - This needs the owner, because O94 says a factorless note leaves the row "without an interval box (fail closed)" (Q1).
3. **Rebase by object, not by key (L2).**
   - A rebased route should reference the pair's measurement object and inherit, as one record:
     - its E166 amount and numerator;
     - its workload, window and dates;
     - its capacity status, valuation basis and stage.
   - It should publish `rebasedFrom` and an `effectiveDonor`.
   - One fixture should compare every published field of a rebased route with the pair's own candidate.
4. **Publish, per provider, the admissible report window at the cutoff.**
   - Today OpenAI's current partition starts on 2026-10-24, after four announcement splits in 13 days (2026-10-11, 16, 20 and 23), and Kimi's starts on 2026-10-25.
   - With I79 L2's meter-period rule, a weekly reading without a stated window covers the 7 days ending on its report date. So:
     - for OpenAI, no such reading can count before one dated 2026-10-30;
     - for Kimi, none before 2026-10-31.
   - The O71 search for those cells is therefore structurally unable to admit a route at this release.
   - The summary should state per provider "current partition since X; earliest admissible weekly reading Y", so readers can see that the absence of report routes for OpenAI and Kimi is structural, not evidential.

## 3. Questions for the owner

1. **O94 factorless notes (L3, recommendation 2).** When AA's note says its cost omits a surcharge but states no factor that the reader can attach, should the row compete over [C, ∞)? With that domain, labels are still decided at its published cost, which is the only end any label test reads. The alternative is that it keeps making every output it touches "unresolved", as O94 says today. A two-clause rephrasing of the current Haiku note would remove every API interval claim in both rankings.
2. **Announcement splits (O77, O83; recommendation 4).** Should a provider announcement that changes how usage is metered, but not the plan's limits or price, split the report partition? Examples are OpenAI's Day 16 and Day 19 cache-retention posts. Today such announcements block every OpenAI weekly reading for a week after each one. If the answer is "only limit changes split", each split record needs a typed basis, and the build would split only on that type.

## 4. Verdict

There are no Critical, High or Medium findings, and four Lows.
- The figure check exits 0, and 1,624 Python tests pass.
- A clean rebuild of HEAD reproduces every published data file, document and site page byte for byte.
- Quality, cost scores, anchors, values, ranks, exchange rates, bars and Plan counts recompute exactly in both rankings.
- r141's shared replacement predicate, report-route coverage, O97 grade and narrowed caveat reader do what the ledger says for the cases it tested.

**The Lows:**
- L1 shows two further ways the donor's row and its followers can disagree: `requiredVariant` and a demoted donor.
- L2 shows that an O97 follower still publishes the measurement's amount and admission-table cross-effort mark, and that O97 is missing from the published summary.
- L3 shows that the caveat reader fails closed on plausible rephrasings, with an outsized effect that the label logic does not need.
- L4 is a count line that contradicts E183.

All are latent, except the o72Application omission and the line 35 and line 106 wording.

Under O56 this round is clean. With I81 it is the second consecutive clean round at the Claude Opus 5.5 xhigh rung.

VERDICT: HAS FEEDBACK
