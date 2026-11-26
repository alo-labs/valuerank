# Internal review I78 — Claude Opus 5.5 (effort xhigh) on draft r137

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r137`
- **Last line of the draft (line 175):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r137 (seventy-seventh internal review, the first at Opus 5.5 xhigh, and owner decision O92) keeps a fault-window measurement selected and flagged until two concordant user reports for its plan replace it, adds that rule to the admission table, the lifecycle table and the release manifest, and dates an undated measurement conservatively. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "measurement conservatively. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end: O45–O92, E247–E270, I29–I77 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i77-claude-opus-5.5-xhigh.md`, and how the ledger resolved it:
  - M1 was adopted with O92.
  - L1, L2 and L5 were adopted.
  - L3 and L4 became moot under O92.
- `draft-r137.md`, every line (1–175), in sequential chunks. The long lines were read whole: 15, 18, 28, 33, 34, 43, 47, 51, 53, 55, 58, 63, 67, 88, 98, 102, 106, 114–115, 135–136, 143, 152 and the revision history on 175.
- Word diffs of r136 against r137, for both `.src.md` and `.md`. The hand-written changes are confined to four places:
  - line 55 (O92);
  - line 58 (E106 case 3);
  - the new lifecycle row;
  - the revision history.
  Everything else that changed is a generated figure (the Pro 500 rows returning).
- The code and data diff of HEAD (92420eb): `plan_routes.py`, `value_v3.py`, `draft_figures.py`, tests, the registry, AGENTS.md, and the generated documents and site data.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- The Python suite passes: 1,615 tests in `tests/` (excluding `e2e` and `js`), run with bytecode writing and the pytest cache off.
- `git status` was clean before I wrote this file.

**Arithmetic, recomputed from `data/scores.json` for both rankings** (no mismatch in any of 9 + 16 rows and 27 + 51 plan rows)
- Every displayed quality is the `quality.TRACKS`-weighted mean of its leaves.
- Every cost score is 100 × clip((ln c_H − ln c)/(ln c_H − ln c_L)) on its own workload's anchors.
- Every value is 0.25 S_C + 0.75 Q̄.
- Every anchor is the cheapest reference ÷ 2 and the dearest × 2. The max-effort main Plan panel has 23 references (8 configurations' plan rows); its subset panel has 27.
- Every plan cost is the API cost ÷ the multiple, or the API cost on fallback.
- Every rank is the competition rank, and each configuration has exactly one representative plan row, whose value equals `planScore`.
- The exchange rates are 3.04 / 2.44 (max-effort) and 2.83 / 1.85 (AI Coding Daily).
- The value-variance allocations recompute as 106% / 21% and −96% / −25%.

**r137's generated figures**
- Plan rows: 27 for 9 configurations and 51 for 16.
- API-fallback rows: 2 and 3.
- Rows flagged possibly superseded or expired: 21 and 44. Rows with an unverified valuation basis: 21 and 44.
- Owner assumptions: 14 (10 transfers, 4 ceilings) and 30 (26 transfers, 4 ceilings).
- Fault-window rows: 3 and 8. All 11 are also possibly superseded.
- Separability:
  - 0 of 8 API pairs and 2 of 10 Plan pairs (16 same-configuration pairs) in the max-effort ranking;
  - 1 of 15 and 1 of 19 (31 same-configuration pairs) in the AI Coding Daily ranking;
  - medians 2.76 / 2.76 and 4.43 / 4.41;
  - noise margins 3.7 and 5.9.
- Noise bands, recomputed from `valueSd` under the O42/E248 rule: they equal the published `[first, last]` ranges on all four bases. The only configuration whose plan rows fall in two bands is GPT-6.1 Sol (medium), in the AI Coding Daily ranking.

**Cohort and bars**
- The cohort recomputes from `data/aa_frontier_capture.json`:
  - 19 path vertices matched at 0 px and rising strictly;
  - 11 near points;
  - 13 families (8 frontier, 5 near only);
  - tooltip ties at 38 (three points) and 56 (two);
  - the first vertex, GPT-6 Luna (low) at $10.63, is also the cheapest of the 190 plotted points, and none lies left of it.
- Admission:
  - the Coding Agent Index is priced for 8 of 9 max-effort rows and 3 of 16 AI Coding Daily rows;
  - 255 and 127 feasible alternatives;
  - panels of 8 and 16; thresholds 6 and 11.
- Bars:
  - ladder 53.27 / 63.54 / 64.94 (headline setter Gemini 4 Argon (high)) and 38.00 / 49.24 / 58.61 (headline setter MiMo-V2.6-Pro);
  - reach 7 / 5 / 3 and 13 / 9 / 5;
  - possible against confirmed qualifiers 5 / 4 and 9 / 8.

**Other figures**
- GDPval movement: 54 of 61 pages moved; the largest ranked move is 0.205 z (0.0154 value) and 0.192 z (0.0144 value).
- FrontierCode cross-check: τ_b 0.766 on a 22-row panel, mean offset 2.60.
- Terminal-Bench cross-check: τ_b 0.738 on 5 rows.
- `planAllowanceCells`: 52 cells (28 listed), none passes; Google AI Pro fails at 1.35×.

**O92 in the build**
- `route_candidates` no longer makes a fault-window candidate diagnostic.
- `plan_cost` adds `FAULT_FLAG`.
- `post_change_ranks` yields a fault-window candidate to a report route on the same plan.
- Both rankings' manifests carry the new rule: 3 of 27 and 8 of 51 rows.
- The Pro 500 admission entries publish `faultWindow` and keep case 3.
- `evidence.faultedRoutes` names the two SemiAnalysis Pro 500 measurements.
- The registry's `asOf` equals its search cutoff (2026-10-25), now checked by the build.

**Probes** (in memory only; no file was changed)
- A change dated before the measurement, against `change_flagged` and `route_selection` (finding L2).
- An undated controlled measurement, and one dated only by `validFrom` (L2).
- A fault-window transfer's comparator key (L1).
- Implied meter windows for the 40 weekly reports with an unstated window (L3).

**Not verified:** live web pages, the paywalled SemiAnalysis article and the Monte Carlo draws themselves.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. O92's yield is missing from the comparator's grade key and from the O73 precedence sentence, and the build implements it by lifting a fault-window transfer to the O78 rank.**

*Where the rule is stated:* line 55 and the new lifecycle row say that a fault-window measurement, and every route resting on it, yields to a concordant report pair for the same plan.

*Where it is missing:*
- **Comparator key (2), line 51.** This is the governing "machine-readable comparator". It still lists one exception only: "except that a controlled measurement flagged by a detected change ranks just below a concordant report pair … (owner decision O78)".
- **The O73 sentence, line 55.** It says an exact measurement "keeps its precedence … unless a detected change flags it and a concordant report pair … is dated after that change (O78)". O92 appears only later in the same paragraph, inside the report-eligibility list.

*In the build:* `post_change_ranks` marks any fault-window candidate of grade `controlled` or `assumption` as `postChangeSuperseded`, and `grade_rank` then returns 1.5.
- For an owner-named transfer (grade 1), this raises the grade.
- Probe: a fault-window transfer on Pro 500, another transfer on Plus and a report route on Pro 500 give comparison tuples (0, 1.5, 10.772, −500), (0, 1, 10.55, −20) and (0, 2, 9.0, −500).
- The reports are still selected, so no selection changes. But the published `comparisonTuples` would show an assumption ranked above other assumptions, which no rule says.

*Status:* latent; no cell passes. This is the same class as I63 L1 (O77–O79 written into the comparator key).

*Change:*
1. Add to key (2): "…and a controlled measurement inside an acknowledged accounting-fault window, with every route resting on it, ranks just below a concordant report pair for the same plan (O91, O92)". Add "or O92" to the O73 sentence.
2. In `post_change_ranks`, mark only candidates whose grade is above the pair's, or set the rank to min(own grade, 1.5). Add a test that a fault-window transfer keeps grade 1.

**L2. The measurement-date predicates still disagree. The adopted I77 fixes each closed one side only.**

*What is new against I77 L1/L2:* L2's fix bounded the change date from above only, and L1's conservative interval was applied to the fault test alone.

(a) **A change dated before the measurement still counts once the route ages.**
- `expiry_status` counts a change only within [evidence date, V].
- `change_flagged` (E228) and the O78 branch of `post_change_ranks` test only that a change exists and that the stage is possibly superseded or expired.
- Probe: measurement published 2026-10-06, change on 2026-10-01, V = 2026-11-20. The route is possibly superseded by age alone. `change_flagged` returns True, so the row is an E228 blocker. A report pair dated 2026-11-10/12 at multiple 5 replaces the measurement at multiple 10 under O78, although no change occurred "since measurement".
- This contradicts the lifecycle row ("not age alone") and the ledger's I77 L2 claim that "age alone never makes an E228 blocker".
- Latent: no route in the registry has a change dated before its evidence date.

(b) **Two dates for one measurement.**
- The fault test dates a measurement without a window by [publication − 30 days, publication], "conservatively".
- E18's "change detected since measurement" (via `expiry_status`) uses the publication date.
- So a change dated between those two dates is "inside" for the fault test but "before the measurement" for change detection. That is conservative on one side only.

(c) **An undated measurement fails closed for faults but open for the clock.**
- A controlled measurement with no window, publication date or `validFrom` is inside every fault window of its provider, but `expiry_status` returns "fresh" at every release (age None).
- Probe at V = 2027-06-01: "fresh" and inside the fault.
- One dated only by `validFrom` is aged by that date but treated as undated by the fault test.
- E151 stops the build on an undated report only.

(d) **Off by one.** "The 30 days ending on its publication date" is coded as publication − 30 days, which spans 31 dates (2026-09-06 to 2026-10-06). E194 counts its window the same way but says so ("spans 31 calendar dates").

*Change:* design recommendation 1, which gives each measurement one span read by every predicate and stops the build on an undated controlled measurement or donor. Then correct the wording in (d).

**L3. An unstated report window is a single day, while an unstated measurement window is now a 30-day interval. The less conservative reading sits on the side that can replace measured evidence.**

*How reports are dated:*
- E270 and O83 exclude a report whose window touches a fault day or spans a split.
- `plan_admission.window` takes `windowStart` or else `windowEnd`, so an unstated window is the report date alone (the I65 L1 transcription convention).
- 40 of the 107 tabulated reports are weekly with an unstated window, and 8 are monthly.
- A meter fraction "measures its own window's allowance" (E270), so the consumption it prices falls in the meter window ending on the report date.

*Probe:* reading each unstated window as the meter window (7 or 30 days ending on the report date) excludes two more reports. Both are GPT-6 Astra on ChatGPT Pro 100: sentrybottale-pro100 (2026-10-18) and mrak-pro100 (2026-10-19). Both touch OpenAI's acknowledged fault days of 2026-10-16/17. No verdict changes: no cell passes, and both reports lie outside the current partition.

*Why it matters now:* r137 made unstated *measurement* windows conservative. Under O78 and O92, a report pair is exactly what replaces a flagged or fault-window measurement. So the point convention is the reading that can let a straddling report displace a controlled measurement.

*New against the ledger:* I65 L1 set the transcription convention; the asymmetry with r137's measurement convention is new.

*Change:* for a meter-fraction report with an unstated window, test faults, splits and the report window over [report date − meter window + 1 day, report date] (failing closed), and keep the E194 observation date unchanged. Otherwise, state why reports keep the point convention.

**L4. The specification counts and prints the other route flags, but not the fault flag.**

*Counts and the manifest:*
- Output 1 (line 25) and the Known limitations count the plan rows on a possibly superseded or expired route and those with an unverified basis. They do not count the 3 and 8 fault-window rows.
- E63's description (line 152) names the Plan lifecycle entry, but not the new fault-window entry that the build publishes and r137's history announces.

*Bar results:*
- The max-effort Plan displayed-record cheapest row is GPT-6.1 Sol (max) on ChatGPT Pro 500 at both the headline and the lower-quartile bar. That row is also the lower-quartile noise-margin companion (E203, O44).
- It is a fault-window row (and possibly superseded). The O63 safety flags are printed beside these results, but no route flag is.

*Measured-only view (E113):* it ranks the same Pro 500 route second. It marks `crossEffort`, but not `faultWindow`.

*Change:*
- Generate a `{track}.planFaultRows` figure and print it in Output 1 and the limitations.
- Name the fault-window entry in E63.
- Print the selected route's change, fault and valuation flags beside each Plan displayed-record result and companion, as O63 is printed.
- Publish `faultWindow` on measured-only entries.

**L5. Plan route flags and the O71–O92 rules reach no human-readable output for the AI Coding Daily ranking, and only partly for the max-effort ranking.**

*Why Low:* this concerns generated documents, which the specification deliberately does not cite (E265, I49 M2). The flags are in `scores.json`, and no score depends on them.

*What a reader sees:*
- **README.** Its Flags column carries no route flag for either ranking, and it never mentions "possibly superseded". At this release, every measured Plan route is flagged possibly superseded, and the representative rows of GPT-6.1 Sol (max), GPT-6 Luna (max) and 7 of the 16 AI Coding Daily configurations rest on a fault-window measurement.
- **scores.md.** It has no Plan route-selection table for the AI Coding Daily ranking, and it prints only the max-effort release manifest. So that ranking's 44 possibly-superseded and 8 fault-window rows appear in no human-readable output. The site's plans page and model pages do not show them either.
- **Policy text.** `emit_docs.POLICY_APPLICATIONS` omits the registry's `o72Application`. As a result, methodology.md (AGENTS.md: "the published summary") never states O72–O86, O89, O91 or O92, apart from one manifest row: the O73 precedence, O78, the O86 formula and the fault window are all missing. O87, O88 and O90 reach it only through the GPT and "Other models" lines. The site embeds the text only in page JSON.
- **Cell verdicts.** `planAllowanceCells` is printed nowhere outside `scores.json`.

*New against the ledger:* I61 M1 and I70 M1 relied on registry texts reaching readers. This one does not.

*Change:* design recommendation 3.

**L6. The lifecycle table presents "Fault window" as a stage, but it is a flag that coexists with an age stage.**

- The table is introduced as "one table for the stages above". All 11 fault-window rows are also "Possibly superseded".
- The table does not say what happens when such a route reaches "Expired" or "Demoted". The engine applies the age rows and keeps the flag until demotion.

*Change:* split the table into exclusive stages (age, or report window) and overlays (detected change, fault window, valuation status). State that a fault-window route follows the age rows and carries the flag until it is replaced or demoted.

## 2. Methodology design recommendations

1. **One evidence-span object, read by every date predicate (L2, L3).**
   - Give every measurement object and report a span `[earliest, latest]`:
     - the stated window;
     - else, for a controlled measurement, [allocation-regime start where it is recorded as a date, otherwise publication − 29 days, publication];
     - else, for a meter-fraction report, [report date − meter window + 1, report date].
   - Define `overlaps(span, fault)`, `spans_split(span, split)` and `changed_since(span, change, V)` once (a change counts when earliest ≤ change ≤ V). Ages run from `latest`, as now.
   - Use them in `in_fault_window`, `on_fault_day`, `partition`, `expiry_status`, `change_flagged` and `post_change_ranks`.
   - Stop the build on a controlled measurement or donor with no span.
   - Today every verdict, selection and flag is unchanged. The SemiAnalysis ChatGPT span would be [2026-09-29, 2026-10-06] once the regime start, now recorded only as text ("Current post-September 29 Codex schedule"), is stored as a date. The two Pro 100 reports above would leave cells that already fail.

2. **One precedence-exception registry (L1).**
   - Register the comparator's grade order and its exceptions once in `plan_routes`, as `OWNER_ASSUMPTIONS` does for I71: O78 (post-change pair), O89 (O88 routes share the donor's precedence) and O92 (fault window).
   - Generate from it `grade_rank`, key (2)'s text, the O73 sentence and the lifecycle cells.
   - Lint AGENTS.md against it.
   - This ends the recurring class "a new owner decision changes the comparator, and one list does not say so" (I63 L1, I72 L1, I73 L2, this L1).

3. **Route flags as generated disclosure, per ranking (L4, L5).**
   - In README, a "Plan route flags" column with one short code per flag, and one generated sentence per ranking. Today that sentence reads: "every measured Plan route at this release is flagged possibly superseded; N rows rest on a measurement inside an acknowledged accounting-fault window".
   - In scores.md, the AI Coding Daily Plan route-selection table and its release manifest.
   - In methodology.md, `o72Application` added to `POLICY_APPLICATIONS`.
   - The `planAllowanceCells` verdict table in raw-data.md.
   - Route flags beside the E203/O44 Plan results.
   - A test that every flag in `rows[].plan.flags` appears in some human-readable document for each ranking.

4. **Lifecycle table as stages plus overlays (L6).** Each overlay row states what it changes (comparison, interval eligibility, label) and that it combines with any stage.

## 3. Questions for the owner

1. **O92's scope when reports arrive.** O92 keeps SemiAnalysis's Pro 500 measurement "until two user measurements of Pro 500 exist". The build reads this per model.
   - An admitted GPT-6.1 Sol pair on Pro 500 would replace only GPT-6.1 Sol's Pro 500 routes (its max row and its O88 rows).
   - GPT-6 Astra's Pro 500 measurement would keep the fault flag. So would the GPT-6 Luna and GPT-5.6 Luna transfers resting on the Sol measurement, which also keep that faulted donor (E144).

   Is that the intent? Or should an admitted pair for any model on Pro 500 also lift the fault *flag* (not the multiple) from the other models' Pro 500 routes?
   - If plan-level: I would recommend a build-derived, plan-scoped `faultCleared`.
   - If per model: only the L1 wording changes.

## 4. Verdict

There are no Critical, High or Medium findings, and six Lows. The figure check exits 0, and 1,615 tests pass. The quality, cost-score, anchor, plan-cost, value, rank, band and separability arithmetic recomputes exactly in both rankings, as do the cohort, admission, bar and diagnostic figures I checked. O92 is implemented as decided: the Pro 500 rows are back and flagged, and the rule is in E106 case (3), the lifecycle table, both manifests and the admission entries.

**The Lows:**
- L1: O92's yield is not in comparator key (2) or the O73 sentence, and the code lifts a fault-window transfer to rank 1.5.
- L2: the change predicates still count a pre-measurement change once the route ages; the measurement has two dates; an undated measurement is "fresh" forever; the lookback spans 31 dates.
- L3: unstated report windows are points while unstated measurement windows are intervals.
- L4: the fault flag is missing from Output 1, the limitations, E63 and the Plan displayed-record results.
- L5: route flags and the O72–O92 rules reach no human-readable output for the AI Coding Daily ranking, and methodology.md omits `o72Application`.
- L6: the lifecycle table treats an overlay as a stage.

Every Low is latent or a disclosure gap; no score, rank, route or claim changes.

Under O56 this round is clean. It is the first clean round at the Claude Opus 5.5 xhigh rung, after I77.

VERDICT: HAS FEEDBACK
