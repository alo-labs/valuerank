# Internal review I88 — Claude Opus 5.5 (effort max) on draft r147

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r147`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…and carries O107 into the comparator, lifecycle and eligibility text. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "eligibility text. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1918): owner decisions O45–O108, editor decisions E247–E270, reviews I29–I87 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` and `docs/refresh-and-release.md`, in full.
- `review-i87-claude-opus-5.5-max.md`, and how the ledger resolved it:
  - M1 became the two derived dates (`changeDetectedOn`, `blockingChangeOn`) and the new `blocking_change`;
  - L1 became the blocking-date check on every flagged route;
  - L2 became the O107 wording in comparator key (2), the O73 sentence, E92, the E212 table's comparison cell and the README legend;
  - L3 became `appliesTo` on chart-level pricing notes;
  - L4 became O108 and `basket_label`;
  - L5 became the metering-only figure and profile rule 11;
  - L6 became the manifest's gate list and the O103 instant in the register and refresh document.
- `draft-r147.md`, every line (1–174), as 19 sequential chunks of at most 16,000 characters covering all 301,738 characters.
- A sentence-level diff of `draft-r146.src.md` against `draft-r147.src.md`. The hand-written changes are the title, comparator key (2) (line 51), the O73 sentence (line 55), E183's O108, chart-level-note and basket-label clauses (line 116), E92's O107 clause (line 135), E18's two-date clause (line 152), the E212 table's comparison cell (line 159) and the r147 history entry.
- The HEAD commit bedcc89 diff: `plan_admission.py`, `plan_routes.py`, `value_v3.py`, `draft_figures.py`, `emit_docs.py`, three test files, the registry, the footnote register, AGENTS.md, the refresh document, the generated documents and the site.
- Code read:
  - `plan_admission.py` lines 1–135 (`splitting`, `check_change_flags`, `check_change_records`, `applies`);
  - `plan_routes.py` lines 40–780: `blocking_change`, `grade_rank`, `post_change_ranks`, `evidence_date`, `expiry_status`, `change_flagged`, the same-model and lower-of checks, `report_stage`, `measurement_objects`, `measurement_span`, `in_fault_window`, `report_covers`, `pair_replaces`, `effective_measurement`, `measurement_eligible`, `rebase_lower_of`, `_rebased`, `rebase_transfer`, `route_candidates`, `admission_table` and the comparator;
  - in `value_v3.py`: `assemble`, `assemble_for_release`, `plan_variants`, `_gated_box`, `classify_footnote`, `chart_footnote`, `NOTE_SURFACES` and `check_surface_notes`, `check_capture_twins`, `check_captured_footnotes`, `page_notes`, `basket_label`, `chart_notes`, `chart_level_notes`, `combined_note_class`, `aa_cost_caveat`, `valuation_gate`, `interval_outputs`, `withheld_label`, the manifest rules, `load_documents`, `build_tracks` and `build`;
  - `basket.CHART_COMPONENTS`; `draft_figures.registry_figures`; `emit_docs.FLAG_LEGEND`.
- Data read or queried:
  - `data/scores.json`, both rankings: rows, plan rows and their flags, admission, workloads and anchors, interval outputs, rank separability, `familyPrimary`, `frontierCodeCrossSource`, `sourceClocks` and the manifest;
  - `data/v3_frozen.json` and `data/v3_frozen_aicd.json` (bar references and anchors);
  - `data/plan_cost_routes.json`: the 137 routes by kind and change fields, the typed partition records, the profile rules, `sourceEvidence.semianalysis.changeDetection` and `o72Application`;
  - `data/price_records.json`; `data/aa_frontier_capture.json` (190 points, 19 frontier and 11 near entries, footnotes); `data/aa/coding_agents_capture.json`; `data/aa/cost_charts_capture.json`; `data/aa/aa_footnote_register.json`; `data/v3_configuration_map.json`; `data/swe_tracks.json`; `data/source_rereads.json`.
- The O71 record: the plan-allowances README, the stage-2 Anthropic notes (Q3, "October changes") and the stage-3 run manifest.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0 in the repository.
- 1,635 Python tests pass in a scratch clone of HEAD (e2e and js excluded); none is skipped.
- The repository's `git status` was clean before I wrote this file.

**Reproduction.** In the clone at the pinned clock (`VALUERANK_NOW=2026-10-25T09:56:47Z`), these regenerate byte for byte: `build_scores`, `emit_docs`, the site build, the figures manifest and both scenario files (54 s).

**Probes.** The scripts are in `/tmp/claude-0/-home-user/7939c829-13d8-5c69-90ae-0a2a9460135a/scratchpad/i88/probes/`. Each ran against its own scratch clone or in memory; nothing in the repository changed.

| Probe | Result |
|---|---|
| P1: a registered 2× pricing omission on Claude Opus 5.5 (max)'s row of the ITBench-AA cost chart (ITBench-AA is pending in both rankings) | Claude Opus 5.5 (max) becomes an O94 row and a blocker in the max-effort ranking; the API qualifier counts at the headline, lower and upper bars fall from 4, 6 and 2 to 3, 5 and 1; the row is marked `leavesAtNextFreeze`, and a freeze preview drops it from the references and moves the max-effort API high anchor from 18,703.43 to 17,862.56 USD (M1) |
| P2: a registered 2× pricing omission on GPT-6 Luna (max)'s Coding Agent Index record (the index is admitted in the max-effort ranking and pending in the AI Coding Daily ranking) | GPT-6 Luna (max) becomes an O94 row in both rankings; in the AI Coding Daily ranking the lower bar's possible-cheapest set changes from {GPT-6 Luna (max), GPT-6 Luna (xhigh)} to {MiMo-V2.6-Pro, GPT-6 Luna (xhigh)}, confirmed and possible qualifiers fall from 10 and 11 to 9 and 10, and the row leaves that ranking's references at the next freeze (M1) |
| P3: an Anthropic availability record dated 2026-10-01 on the three Claude plans, before the 2026-10-17 limit record | flags left at 2026-10-17: the build stops; label 2026-10-01 without a blocking date: the build stops; label 2026-10-01 with `blockingChangeOn` 2026-10-17: the gates pass and the E228 blockers are unchanged (21 of 27 and 44 of 51 plan rows, every Claude plan row among them). At function level a report pair dated 2026-10-20/21 outranks the measurement and one dated 2026-10-10/12 does not; an availability-only flag blocks nothing (I87 M1 is closed) |
| P4: the ITBench-AA chart row "GPT-6 Astra (max)" relabelled "GPT-6 Astra (Max)" | the build stops (`basket_label`) |
| P5: a new ITBench-AA chart row "GPT-6.1 Sol (max)" carrying a registered 2× pricing omission, while the configuration map's label for that configuration is null | the build passes; the row gets no ITBench-AA cost (coverage stays 2 of 9) and no O94 class (L3) |
| P6: a chart-level pricing note whose `appliesTo` is `["claude-haiku-5-5-max"]`, `["claude-haiku-5.5-max"]` or `["Claude Haiku 5.5"]` | the first applies to that row; the typo and the family name apply to no row, and the build does not stop (L1) |

**Figures recomputed from the underlying data (all match the draft):**
- the frozen bars 53.3 / 63.5 / 64.9 and 38.0 / 49.2 / 58.6 (displayed quality at zero-based positions 2, 4, 6 and 3, 7, 11), with Gemini 4 Argon (high) and MiMo-V2.6-Pro at the headline bars;
- the reach counts 7 / 5 / 3 and 13 / 9 / 5, and the headline qualifier counts 4 against 5 and 8 against 9;
- the exchange rates from the frozen anchors: 3.04 (4.06), 2.44 (3.25), 2.83 (3.77) and 1.85 (2.46);
- the Plan rows: 27 and 51 rows; 2 and 3 API fallbacks with their names; 21 and 44 possibly superseded; 3 and 8 in a fault window; 21 and 44 on an unverified basis; 14 (10 + 4) and 30 (26 + 4) on an owner assumption;
- the noise margins 3.70 and 5.87, the separability counts 0 of 8 and 1 of 15 (medians 2.76, 4.43 and 4.41 Plan), the AI Coding Daily n = 60 reading (3.25 and 3.21), the GDPval-AA wide reading (2.77 and 4.44), and the E242 tolerance as 2^(median ÷ exchange rate);
- E205's one-row-per-family headline bars, 63.5 and 52.8;
- the cohort: 30 configurations (19 + 11) from 13 families (8 + 5); the first vertex, GPT-6 Luna (low) at $10.63, is the cheapest of the 190 points; the 38 and 56 frontier ties; the 11 near points with their gaps;
- the exact cost coverage: Coding Agent Index 8 of 9 and 3 of 16, ITBench-AA 2 of 9 and 0 of 16; 255 and 127 feasible admission subsets;
- the FrontierCode cross-source panel (22 rows, τ_b 0.766, mean offset 2.60, largest 11.60) and its AI Coding Daily effect at weight 21% (0.55 and 2.44 points);
- the Plan evidence clock (last Current day 2026-11-05, expired from 2027-01-05, demoted from 2027-02-04) and the report window (2026-09-25 to 2026-10-25);
- the metering-only figure now lists only the three metering records, and profile rule 11 names all four record types;
- the source clocks: the four sources captured after the cutoff from boards last updated before its day, the AI Coding Daily DeepSeek alternates and Kimi K3.1 Pro's cutoff-day row bound (01:14:11Z).

**Not verified:**
- live AA pages and boards;
- the paywalled SemiAnalysis article;
- Anthropic's help article and launch pages behind L4, beyond what the O71 record states.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. O108 is published as "the ranking's cost workload" but built as "the target basket". A note on a cost that a ranking does not score therefore makes O94 rows in that ranking.**

*What the published texts say.* Every published statement of O108 limits O106 to the cost charts and the index whose cost is in the ranking's cost workload:
- draft line 116 (E183): "counting only the cost charts and index whose cost is in the ranking's cost workload (owner decision O108, 2026-10-28)";
- AGENTS.md: "A registered pricing omission on any AA surface whose cost is in the ranking's cost workload makes the row an O94 row (O106, O108)";
- the registry's `o72Application`, rendered into methodology.md line 167 and `site/data/plans.json`: "O108: O106 counts only the cost charts and index whose cost is in the ranking's cost workload";
- the footnote register's rule: "only charts whose cost is in the ranking's cost workload count".

The draft's own definitions put pending components outside that workload:
- line 43: C_W takes the seven Index evaluations "plus the Coding Agent Index where the ranking admits it";
- line 44: ITBench-AA is "pending capture" in both rankings;
- lines 47 and 169: the Coding Agent Index is pending in the AI Coding Daily ranking, whose basket "holds no coding-agent component".

*What the build does.* `assemble` computes `aaNoteClass` once per configuration, before admission (value_v3.py line 905).
- `chart_notes` and `chart_level_notes` read every chart in `basket.CHART_COMPONENTS`, which is `("itbench-aa",)`: a target component, admitted or not.
- The Coding Agent Index's record notes and index-level notes count whenever the configuration has a record, whatever that ranking admitted.
- Neither function looks at the ranking's admitted set or at the row's own workload. The `chart_notes` docstring ("charts outside the cost workload never count") and the r147 test ("charts outside the basket never count") equate the target basket with the cost workload. The only fixture separates FrontierCode from ITBench-AA; none covers a pending component.

*Probes.*
- **P1:** a 2× omission on the ITBench-AA row of Claude Opus 5.5 (max), a cost neither ranking scores, makes that row an O94 row in the max-effort ranking.
  - It publishes the note as its "AA cost caveat".
  - It becomes a blocker, and the qualifier counts drop at all three bars.
  - It is the dearest API reference, so the next freeze would move the high anchor from 18,703.43 to 17,862.56 USD. Every max-effort row's cost score would change because of a note about a cost the ranking never scores.
- **P2:** a 2× omission on GPT-6 Luna (max)'s Coding Agent Index record makes it an O94 row in the AI Coding Daily ranking too, where that index is pending.
  - The row leaves the lower bar's possible-cheapest set, and MiMo-V2.6-Pro enters it.
  - The row leaves that ranking's anchor references at the next freeze.

*Why Medium.*
- **The build contradicts the owner decision as every published statement gives it.** That statement appears in the normative draft, the binding AGENTS.md, the registry text rendered into methodology.md and the site, and the register's rule. The precedent of I69 M1 and I70 M1 treats such a contradiction as Medium.
- **The two readings differ for every pending component.**
  - ITBench-AA is pending in both rankings. Its chart holds 2 of the 9 max-effort rows, GPT-6 Astra (max) and Claude Opus 5.5 (max), the dearest API reference.
  - The Coding Agent Index is pending in the AI Coding Daily ranking. It has records for 3 of that ranking's 16 rows.
- **The effects reach scores, not only labels.** The row's own labels are denied, a false caveat is published, and anchor references are dropped at the next freeze, which can move a ranking's anchors (P1).
- **It goes live at the next refresh.** O103 makes the captures record exactly these notes from then on, and the refresh document makes extending the capture scripts a precondition.
- **The record is ambiguous at its source.** The ledger's O108 entry glosses "the ranking's cost workload C_W" as "today the Coding Agent Index and ITBench-AA". That is neither ranking's C_W today: ITBench-AA is pending in both, and the index is pending in one.
- **It is latent today.** No capture records a basket-chart or index note yet.

*Not a repeat.* I87 Q1 asked which notes count, and the owner answered with O108. The mismatch between O108's published statement and the code that implements it was introduced in r147.

*Change.* The answer to Q1 decides the fix.
- **If the published statement stands (recommended).** Compute each row's note class inside each ranking after admission, from its own scored workload:
  - the model page and the Intelligence Index chart always count;
  - the Coding Agent Index (record and index notes) counts only while it is in the row's workload, so not in the AI Coding Daily ranking today, nor for a max-effort subset row;
  - ITBench-AA (row and chart notes) counts only once admitted;
  - compute the class after E184's possible re-assembly on pinned components.
  - Fixtures: pending against admitted, main-workload against subset row, and row-level against chart-level note, in both rankings.
- **If the owner meant the target basket.** Restate O108 in the draft, AGENTS.md, `o72Application` and the register's rule as "the target basket's cost charts and index (O15 as amended by O50), admitted or pending". Then say why an omission in a cost a ranking does not score makes its row an O94 row there. O94's premise is "a row whose AA cost AA itself says omits a pricing term".
- **Either way, implement the disclosure O108 promises.** O108 says notes on other charts "are registered and disclosed but change no row". Today such notes are registered but printed nowhere. Publish them per surface, with whether each counted (recommendation 1).

### Low

**L1. A chart-level note's `appliesTo` is matched by exact configuration ID and never validated. A typo, the model's family name or a new effort of the named model therefore escapes O94 silently.**

- `combined_note_class` applies a shared pricing omission only when `model_id in entry["appliesTo"]`. The build stops only when the list is empty (draft line 116: "the build stops on one that lists none").
- Probe P6: with `appliesTo` as `["claude-haiku-5.5-max"]` (a typo) or `["Claude Haiku 5.5"]` (the model the registered sentence names), no row is matched and the build passes.
- The configuration IDs invite such slips. The bare `claude-haiku-5-5` is the xhigh row, while the max row is `claude-haiku-5-5-max`.
- A list written today misses any later cohort effort of the same model.
- The failure is open in the direction O94 closes: the row keeps its labels and its anchor eligibility.
- It is latent: no chart- or index-level note is captured yet.
- Change:
  - stop the build on an `appliesTo` entry that is not a roster configuration ID;
  - better, key `appliesTo` by AA family (`configuration_family`), with an optional effort list, because AA's notes name models.
  - Fixtures: a typo stops the build; a family entry covers all its rows; a new effort is covered.

**L2. O107 text that r147 left behind, and nits.**

- **The E212 table's interval cell (line 159).** It still reads "when the trigger is a detected change or the reports (not age alone), the row competes in the Plan interval outputs as a blocker". r147 corrected the comparison cell of the same row. So the governing lifecycle table now gives one trigger two effects, against E92 (line 135), O107 and the README legend. I87 L2 listed this cell, and its adoption missed it. Write "a detected limit or price change (not a model-availability change, O107) or the reports".
- **"By the cutoff."** E18's two-date clause (line 152) and E92's E228 clause (line 135) omit "by the cutoff". The build applies it: `check_change_records` filters `day <= release_day`, and `change_flagged` and `pair_replaces` ignore later dates. I87 L2 asked for it on line 152.
- **Nits.**
  - E63 (line 152) cites the note register under O100, O103 and O106. The manifest also names O108 and lists the basket-label and `appliesTo` stops.
  - The manifest's "AA cost omits a pricing term (O94, O98)" rule cites neither O106 nor O108.
  - The revision history calls both r144's and r146's rounds "the second at Opus 5.5 max", and I87 "the third". I86 and I87 were the fourth and fifth Opus-max rounds.
  - `o72Application` labels two sentences "O104:".

**L3. ITBench-AA's chart rows are still matched through hand-kept labels. A newly charted cohort configuration with a null label silently loses its cost and its notes.**

- **New argument.** I87 L4 raised the null label for notes. r147 added only the check that a non-null label names a chart row. Since O108, ITBench-AA is the one basket cost chart, and the same null label also decides cost.
  - Probe P5: AA charts GPT-6.1 Sol (max) on ITBench-AA, but the map's label is null. The build passes, the row gets no ITBench-AA cost, and coverage stays 2 of 9.
  - That undercounts E140's two-thirds test. Once ITBench-AA is admitted, the row would be scored on a subset workload.
  - This is the failure I50 H1 found for the Coding Agent Index: a null pin moved a row to the subset workload and changed the leader. It ended only with O64's closed-world manifest.
- It is latent: today's map covers every exact ITBench-AA row (2 of 9; 0 of 16).
- Change: register ITBench-AA chart rows by label in a reviewed manifest, as O64 does for the Coding Agent Index. Stop the refresh on a new, relabelled or vanished row, and derive each configuration's label from the manifest (recommendation 3).

**L4. The E269 change-detection record was evaluated before O105 and leaves two documented Anthropic changes after the measurement unresolved.**

- `sourceEvidence.semianalysis.changeDetection` is dated 2026-10-26. O105, which created the availability type, came on 2026-10-28. Its Anthropic evidence says only that "release notes 2026-09-15..10-25 carry no limit entry".
- The O71 record (stage-2 Anthropic notes, Q3) lists two changes after SemiAnalysis's 2026-10-06 publication:
  - **(a) "Haiku 5.5 launched on 2026-10-07/08".** The registry routes Haiku 5.5 on all three Claude plans, so this is a change to which models the plans offer: an O105 availability record.
  - **(b) An "October 7 update" of the Agent SDK help article,** under which "Max plans gained monthly API credits covering `claude -p`". Bundled credits are in the Value Multiple's numerator (line 56, quota schema), so this is a candidate limit change on Max 5x and Max 20x.
- Neither is recorded as a typed record or rejected with a reason.
- The effect today is only the flag date.
  - The Claude routes' label date would become 2026-10-07.
  - If (b) is typed "limit", the Max routes' blocking date and a partition split would move to 2026-10-07 as well.
  - No score, label or cell verdict changes: the 2026-10-17 change already flags and blocks, and the current partition starts after it.
- *Not a repeat.* I87 M1 proposed recording (a) once two dates existed, and the ledger did not answer it. r147 removed the obstacle. (b) is new.
- Change: re-run E269 under O105, and resolve each candidate as a typed record or a dated rejection with a reason (recommendation 4).

## 2. Methodology design recommendations

1. **Decide each AA note's effect per ranking and per workload, and publish a note audit (M1, Q1).**
   - Map every capture surface to a component: the model page to the Index evaluations, the Coding Agent Index record or index to the Coding Agent Index, and the ITBench-AA row or chart to ITBench-AA.
   - Classify each row inside each ranking after admission: a surface counts when its component is in the row's own scored workload, main or subset. Under the other reading of Q1, the rule is "in the target basket"; either way it is one table, not three code paths.
   - Publish, per release, every registered note: surface, rows it names, class, factor, and whether it counted and why. This also delivers O108's "registered and disclosed".
   - Fixtures: pending against admitted, main against subset row, and row-level against chart-level note, in both rankings.
2. **Key `appliesTo` by AA family and validate it (L1).** A chart- or index-level pricing omission names a model, so it should cover every cohort configuration of that family, optionally restricted to listed efforts. The build stops on an entry that names no roster family or configuration.
3. **Close the ITBench-AA chart as O64 closed the Coding Agent Index (L3).**
   - A reviewed manifest registers each chart row by label, as the exact record of one cohort configuration or not one, with a reason.
   - A new, relabelled or vanished row stops the refresh.
   - Labels are derived from the manifest, and the configuration map keeps only recorded choices among several exact rows, as E267 does for the index.
4. **Give change detection a candidate log, as E240 gave the leaf searches (L4).**
   - Every candidate change goes into one per-release list: from E18's scoped documentation checks, from O77 announcements, and from the O71 record.
   - Each candidate is resolved as a typed record (limit, price, availability or metering) or as a dated rejection with a reason.
   - The build fails on an unresolved candidate, so the registry shows why each documented change did or did not flag a route.
5. **Generate each record type's effects from one table (L2).**
   - The code already holds that table (`SPLIT_TYPES`, `FLAG_ONLY_TYPES`, `LOGGED_TYPES`).
   - Render from it the E212 table's effect cells, the E18 and E92 effect clauses and the README legend.
   - Extend the figure lint so a sentence that gives a detected change a blocking effect must name the blocking set.

## 3. Questions for the owner

1. **Which charts and index does O108 count, for a ranking?**
   - **(a)** Only those whose cost is in that row's scored workload in that ranking. Pending components never count: ITBench-AA in both rankings, and the Coding Agent Index in the AI Coding Daily ranking. This is how the draft, AGENTS.md, the registry and the register state O108.
   - **(b)** The target basket's charts and index (the Coding Agent Index and ITBench-AA) in every ranking, admitted or pending. This is what the build does and what the ledger's parenthetical "today the Coding Agent Index and ITBench-AA" says.

   Under (b), a note on a cost a ranking never scores makes its row an O94 row there and, at the next freeze, can move that ranking's anchors (P1). The answer decides M1's fix.

## 4. Verdict

There are no Critical or High findings. There is one Medium and there are four Lows.

**What holds.**
- The figure check exits 0, and 1,635 Python tests pass.
- A clean rebuild of HEAD reproduces every published data file, document, site page, the figures manifest and both scenario files byte for byte.
- Every current figure I recomputed from the underlying data matches.

**r147 closes I87 as built.**
- **M1:** an availability record before a limit record now gives a label date and a separate blocking date. E228 and O78 keep their effect, and an availability-only flag blocks nothing (P3).
- **L1:** a hand-set flag on a non-controlled route must carry a consistent blocking date.
- **L2:** comparator key (2), the O73 sentence, E92 and the README legend name O107, except one table cell (L2 above).
- **L3:** chart-level notes need `appliesTo`.
- **L4:** a relabelled basket-chart row stops the build (P4).
- **L5 and L6:** the metering figure, rule 11, the manifest's gate list and the O103 instant are corrected.

**The findings.**
- **M1:** O108 is stated as the ranking's cost workload but built as the target basket. Notes on ITBench-AA, pending in both rankings, and on the Coding Agent Index, pending in the AI Coding Daily ranking, make O94 rows. They can move a ranking's anchors at the next freeze (P1, P2). The owner's record is itself ambiguous (Q1).
- **L1:** `appliesTo` fails open on typos, family names and new efforts.
- **L2:** the E212 interval cell and "by the cutoff" lag O107, plus four nits.
- **L3:** ITBench-AA chart labels are still hand-kept, so a null label silently drops a row's cost and notes.
- **L4:** the E269 record predates O105 and leaves two documented Anthropic changes of 2026-10-07/08 unresolved.

Under O56 this round is not clean (one Medium). The Claude Opus 5.5 max rung's clean count stays at zero.

VERDICT: HAS FEEDBACK
