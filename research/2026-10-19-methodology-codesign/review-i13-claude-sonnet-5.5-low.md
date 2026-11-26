# Internal review I13 — Claude Sonnet 5.5, effort low, on draft r72

(Saved from the subagent's report; the reviewer read all 918 folded lines.)

## 0. Read check
First line: "# ValueRank methodology — draft r72"
Last 12 words of last line: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."

I read all 918 lines. I used no web search. Every point below comes from the draft's internal logic. I grepped ledger.md for the 45-day freshness gate, the search cutoff and the 34-row panel. The first two are already adopted (E216, E213), so I do not repeat them.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. Which workload and anchor object does an "unresolved" row use? (Fable 5.1, Cost completeness and Admission sections, E209/E170 outcome 4)
- The draft says Fable's seven Index components are "unresolved" and it fails K, so it is not in R_W or P_K.
- Fable is also not on the 35-row subset workload W_S ("35 of 37": the cohort minus Fable and Muse Wonder Full).
- Yet the common-workload panel for cost influence has 34 rows, against R_W = 33 and anchor references = 33. The ledger (R3) adopted the 34 but the draft never says who the 34th row is. Fable is the only candidate.
- Fable is "ranked" and scored, but the draft never says which cost it is scored on. It could be the published but unreconciled Index costs plus the Coding Agent Index cost on W, or some other subset. It also does not say which anchor object applies, or whether Fable counts in the clip-gate n ("rows on its workload with a positive cost").
- Two faithful implementations can disagree on Fable's cost and score, on n, and on the influence statistic.
- Fix: add one definition: "scored on W" means every admitted component has a published, domain-valid cost whatever its E209 status. Name the rows that satisfy it today (33 K rows plus Fable = 34). Say whether rows with an unresolved component are flagged on W or have their own subset. Also say how the unresolved Fable cost enters the displayed cost.

M2. Window length and inclusivity (E194/E213 passage, "30 days ending on the release cutoff")
- The draft gives "2026-09-21 to 2026-10-21" and calls it 30 days. Both ends inclusive is 31 calendar days. AGENTS.md says "preceding month".
- A report dated exactly 30 days before the cutoff is in or out depending on how the implementer reads it. This decides O11's source count and concordance.
- Fix: state the rule as an interval, for example [V − 30 d, V] with a closed or half-open end. Add boundary fixtures at day 30 and day 31, like the existing 100/120/120.001 concordance fixtures.

M3. Different clocks for one score table
- The chart and catalog capture that defines the cohort has a 7-day gate. The AA model-page snapshot has a 45-day gate. That snapshot supplies costs, prices and every AA-run leaf (about 80% of the quality weight).
- Nothing bounds the gap between the two captures. The Index-total reconciliation catches cost drift on a row, but not drift in DeepSWE, FrontierCode, GDPval, LCR or Omniscience values.
- AA changed the roster and the vertices within 10 days (the entrant diff in the draft: 4 vertices entered in 10 days). So a frontier point from the chart and a leaf from a 40-day-old model page can describe different AA states.
- Fix: add a gate on the capture-time gap between chart and model page, for example at most 7 days. Alternatively, require a per-row leaf-vs-chart check on the fields the two artifacts share. List any row captured outside the gap as "mixed AA state".

M4. Inconsistent "points per cost doubling" figures (Cohort section, E205 paragraph)
- It says "API value points per cost doubling are 3.04 against 2.74 frozen". The defined exchange rate is the quality points that offset a doubling: 100·β·ln2 / ((1−β)·ln(c_H/c_L)).
- A value-point loss per doubling is 100·β·ln2 / ln(c_H/c_L), which is three times smaller (1−β = 0.75).
- The numbers are labelled "value points", but 3.04 and 2.74 match the quality-point offset only if ln(c_H/c_L) ≈ 7.6 or 8.4. I could not confirm the scale from anchors the draft gives.
- A reader cannot tell which quantity is quoted.
- Fix: label the quantity using the E196 terms ("quality points that offset a cost doubling"), or print both.

**Low**

L1. The precedence tie-break is unreliable (preamble). "Later-numbered record governs" assumes E numbers follow time. The draft itself says E198 was renumbered E202, and records were added out of order (E182/E183/E177, E170/E185/E186). Use "the record with the later adoption date, and its number only as a final tie-break".

L2. The capture age "4 days" for the model-page snapshot and "3.4 days" for the chart capture are both given for 2026-10-17. Print the capture timestamps, not dates, so the gates are reproducible.

L3. The one-point-per-vertex check in E195 fails if two plotted points share identical coordinates, for example an exact cost-and-Index tie. State the tie handling (family key, then name, as for the cohort rule) so the build neither fails nor picks arbitrarily.

## 2. Methodology design recommendations

1. **Transfer-multiple stress for the Plan table.** This is an Owner decision challenge to the transfer arithmetic, not to the transfers themselves.
   - The Plan ranking for most Claude rows rests on Opus 5.5's 57–59x applied to other Claude models. O35 bans a Fable-based gauge, and O19 keeps analyst allowances out of interval outputs but permits sensitivity. The draft offers only "transfers on/off".
   - Publish, as analyst sensitivity only and outside every interval output, the Plan ranks under a transfer multiplier k on a fixed grid (for example 1, 0.5, 0.25, 0.1). Report where each transferred row's rank and Plan score cross the nearest measured row.
   - This does not use Fable as evidence. It shows readers how fragile the Plan ordering is to the one assumption driving it.
   - I did not find this in the ledger by keyword (haircut, transfer stress). If it was decided, ignore this.

2. **Index-mix proxy as a Plan-cost sensitivity.**
   - Today 23 of 25 Plan routes are "mix unidentified" and the category-mix bound is inactive. E208 forbids AA's Index-wide shares as a substitute for the basket's demand region. That rule is right for labels.
   - Add a clearly named sensitivity column that rescales each controlled-measurement multiple by the ratio of cache and uncached shares between the measurement and AA's Index-wide mix. It would sit outside Θ and every interval output, like the other analyst sensitivities.
   - It would show whether the cache-heavy measurement mix (SemiAnalysis: 96.6% cache reads) drives the Plan ordering. The draft currently reports only "mix unidentified".

3. **Tighten reproducibility (M1–M3).** These are the changes most likely to make two implementations diverge: the definition of "scored on W", the window boundary, and the capture-gap gate.

## 3. Questions for the owner
1. Is Fable 5.1 intended to be scored on the main workload W with its unreconciled Index costs (the 34th panel row), or on a separate subset? The answer fixes the clip-gate n and the influence panel, and so changes M1's recommended wording.
2. May analyst-labelled transfer multipliers or an Index-mix proxy appear as sensitivities, outside intervals, without breaching O19 and O35? This decides recommendations 1 and 2.

## 4. Verdict
VERDICT: HAS FEEDBACK
