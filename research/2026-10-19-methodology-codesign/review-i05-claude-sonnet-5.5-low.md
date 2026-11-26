# Internal review I5 — Claude Sonnet 5.5, effort low, on draft r64

(Saved from the subagent's report; the reviewer read all 819 folded lines.)

## 0. Read check
First line: "# ValueRank methodology — draft r64".
The physical last line (819) is just "(E95, E101)." The last 12 words of the final sentence are: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."
I read all 819 lines in three chunks (1–300, 301–600, 601–819) and read ledger-brief.md first. I did not consult the full ledger.md. I ran no web searches, because the factual claims are 2026-dated AA, SemiAnalysis and Bug Hunt data I cannot verify from public pages. I checked internal arithmetic only. These checks passed:
- 52/105 = 49.52.
- The Omniscience vectors.
- Output tokens 37,901,142 = 13,409,872 + 24,491,270.
- The exchange-rate formula.
- The three-uniform fixture (P(ΣU ≥ 80) ≈ 91.5%).
- 91+220+…+6000 as ten evaluations.

## 1. Findings by severity

**Critical**
None.

**High**

H1. The report window rule contradicts itself (E194 against O32, lines 233–238, with E151 at 185–189).
- Line 235–236 says an earlier-admitted report "thereafter ages under E151/O13 instead of being re-tested against later windows."
- Lines 236–238 (O32) say that report "no longer counts once it is outside the current window", and the 41-day fixture drops the route to diagnostic.
- Both cannot hold. Under O32, a report-based route lives about 30 days. That makes the 30-day soft expiry, the 90-day hard expiry, the 30-day grace and "pooled-evidence clocks" (line 185–189) unreachable for report partitions.
- The draft does not say what happens to a transfer whose donor is report-based, or to a SemiAnalysis controlled measurement. Controlled measurements are not "reports", so the draft presumably intends E151/O13 to govern them alone.
- Two faithful implementations will differ on whether a route survives its second month.
- The same paragraph is also garbled. The fixture's closing ")" sits mid-sentence, before "and exclusion reason codes", which leaves the inclusion-rules parenthesis unbalanced.
- Fix: state one rule. At each release the partition is rebuilt from reports dated inside the current window only. Older reports stay as diagnostics, and E151 clocks apply only to controlled measurements and to transfer donors.
- Delete "instead of being re-tested against later windows."
- Add a fixture for a route that has a current controlled measurement plus a lapsed report pair.
- Say explicitly that a report-donor transfer follows the donor's O32 status.

**Medium**

M1. The window rule does not implement the AGENTS.md clause that excludes measurements outside the preceding month "when the report isolates them" (line 234–235).
- The draft dates a whole report by its measurement window's end. A report covering, for example, 50 days with per-day or per-week breakdowns is therefore admitted whole, although the isolated out-of-window part should be excluded.
- Fix: where a report isolates per-period measurements, keep only the sub-measurements inside the window and recompute the report's multiple from those. Where it does not isolate them, admit the whole report by its end date and flag it "window-straddling".
- Add one fixture.

M2. The bar compares unlike quantities and makes confirmed qualification nearly unreachable for any row with missing leaves (lines 582–588, 601–606).
- Q̄ is a displayed, renormalised, observed-only quality. Qualification tests the full-composite lower bound Q_i^L, with missing leaves at 0.
- A row with coverage p qualifies confirmed only if its displayed quality is at least Q̄/p. For example, 90% coverage needs at least 64.8 against Q̄ = 58.28. The lower-median bar-setter itself can confirm only at 100% coverage.
- So the interval "cheapest" label is in effect restricted to full-coverage rows. That is an eligibility rule nowhere stated as one.
- E198 publishes possibleQualifierN, which is the wrong count. It counts rows that could qualify, not rows that can ever be labelled.
- Fix: also publish confirmedQualifierN and the number of R_W rows at 100% coverage beside every bar result.
- Fix: print a one-line plain-language warning when confirmedQualifierN < 2, since the label is then vacuous.

M3. Retention for several efforts contradicts the Bug Hunt rule (line 89 against lines 104 and 106).
- Line 89 handles "a family with both results at several efforts" and cites Muse Spark 1.3 (max, Index 48, over xhigh, Index 45).
- Line 104 says "Bug Hunt publishes one configuration per model, so a family has at most one such configuration", and O30 repeats this.
- Either the Muse Spark example, or the one-configuration premise, is wrong. If Bug Hunt does cover two efforts for a model, line 104 is false. If not, line 89 is dead text and the example is misleading.
- Fix: reconcile against the Bug Hunt scoreboard and delete whichever statement is false.

M4. Counts and definitions around the 23-row cohort are inconsistent.
- Line 92 says Muse Wonder Full has "no value score and no rank", but line 91 says 23 configurations "are ranked" and line 129 says "20 of 23 ranked rows".
- The admission threshold ⌈2N/3⌉ (line 149) and the bar population (line 582) use "ranked cohort size". It is not stated whether a row that can never carry a cost counts in N, or is in the bar population (21 = 23 − 2 provisional only if it does).
- Line 165 says W_S "covers all 19 rows". The seven Index evaluations are complete for 21 rows (line 131), so 19 is the W (full-basket) count. This is a stale or mislabelled number.
- Fix: define "ranked" versus "scored", define N explicitly, and regenerate the counts from the build.

M5. The cost boundary overstates AA's metering (lines 117 and 304 against 802–805).
- The draft says AA prices "the token counts reported by each model's API provider".
- The registry rule (E176) says the metering basis may be provider-reported or AA's canonical-tokenizer fallback, and is "not published per configuration" as of 2026-10-20.
- Cross-model cost comparisons therefore rest on an unknown mix. The headline cost label should not assert provider-reported counts.
- Fix: reword lines 117 and 304 to "provider-reported counts or AA's tokenizer fallback (basis not published per configuration; metering mix printed)".

M6. The cheapest-above-bar claim ignores cheaper same-family efforts (E38 scope; new argument).
- The ledger rejected scoring siblings and a sibling-evidence diagnostic.
- I am not proposing either. The bar output is exactly where a lower-effort sibling might undercut the winner.
- E38's "omitted competitors" list names only ranked rows outside R_W, so unranked plotted siblings are invisible to the "extends to the selected cohort" statement.
- Fix: add one count line per bar result, "n same-family plotted configurations with lower AA total cost were not evaluated (no exact SDLC evidence)". It uses only the public chart and needs no scoring.

M7. SemiAnalysis labelling is incomplete against AGENTS.md.
- AGENTS.md requires "controlled subscription-account measurements with workload projections".
- The draft says "controlled saturation measurement" and sets capacity status "established".
- Fix: carry the "workload projection" qualifier in the E139 status and the E166 amount label, so the established capacity is not read as a measured one.

**Low**
- L1. The cohort rule (line 684) leaves F(c) undefined when no rendered-frontier vertex costs ≤ c, for example a plotted point left of the first vertex. State the outcome (frontier-adjacent by construction, or error).
- L2. "Lower-median" (line 581) is undefined for odd n. Write "the ⌈n/2⌉-th value of the ascending order".
- L3. Identifier collisions make "E-number" citations ambiguous:
  - E198 is used for both the bar counts and valuation outcome (4).
  - E177, E182 and E184 each appear twice in the ledger brief.
  - "case 4" (E106) and "outcome (4)" (E170) are both used in running prose.
- L4. "Undated report ages with the route" (line 186) conflicts with "else its publication date" (line 235). Pick one.
- L5. The family-qualifier grammar (line 101) is by example only. Specify the stripping regex or list, since the family key drives cohort membership.

## 2. Methodology design recommendations (prioritised)
1. Resolve O32 and E151 into a single partition lifecycle (H1). It is the only item where today's published Plan routes can flip depending on the reader.
2. Split the specification into a live core and a dormant appendix. Every Plan frontier and bar output is vacuous today, because no route has an identified M_W (line 59). Yet roughly a third of the Normative text covers the capacity LP, schedule contract, E105/E80 payment certification, semantics identification and the transport certificates. Mark these "dormant until the first identified route" and give each an executable golden fixture. This reduces the chance that two faithful implementations diverge on code that has never run against real data.
3. Publish a "label reach" table per bar: |R_W|, possibleQualifierN, confirmedQualifierN, full-coverage rows, and unevaluated same-family siblings (M2, M6). The reader can then see whether a "cheapest above the bar" claim is non-vacuous.
4. Ship a reference implementation test harness covering the numeric fixtures already in the text (Omniscience, Bug Hunt, uniform and arcsine, closed-form Clopper–Pearson endpoints). Have each release assert them.
5. Add the window-straddling trim for reports (M1), so the AGENTS.md "preceding month" rule is applied exactly.

## 3. Questions for the owner
1. O32: do you intend report-based Plan routes to lapse to diagnostic after 30 days without fresh reports? That means the 90-day expiry applies only to controlled measurements and transfer donors that are measurements. The answer decides the fix in H1.
2. Bar: is it intended that confirmed "cheapest" labels are effectively limited to full-coverage rows (M2)? If not, should qualification use the displayed observed-only quality, or a stated coverage-adjusted level?

## 4. Verdict
VERDICT: HAS FEEDBACK
