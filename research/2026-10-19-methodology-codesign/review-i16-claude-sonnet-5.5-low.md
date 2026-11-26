# Internal review I16 — Claude Sonnet 5.5, effort low, on draft r75

(Saved from the subagent's report; the reviewer read all 946 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r75`
Last 12 words of the last line: "until complete exact-variant cost evidence covers two-thirds of ranked rows jointly with the admitted components (E95, E101)." The final 12 words are "two-thirds of ranked rows jointly with the admitted components (E95, E101)."
I read all 946 lines in three chunks and read the ledger brief. I grepped the full ledger for the points below. I did not read the I8–I15 sections end to end.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. Valuation outcome (4) is treated differently from outcome (3), and a cheaper, qualifying row can be ignored.
- Passage: E170 and E202 say an outcome-(4) row "is not a blocker" and is listed as an omitted competitor. E183 says that when a blocker's domain cannot be built, the claims it could affect are "unresolved".
- Prior decision: the ledger (E198/E202, "not a blocker") already settled that the row is not a blocker. I am not re-arguing that.
- New argument: O25 says interval outputs "protect the published record". An outcome-(4) row still has a published AA cost and published quality. If that record is cheaper than the candidate and the row qualifies, a "confirmed cheapest" or "definite" label is false on the very record O25 protects.
- Today it is latent. Fable 5.1 is the outcome-(4) row and costs $11.6k, so it blocks nothing. A cheaper row hitting this outcome later would silently pass.
- The two outcomes are inconsistent. A row whose tariff bound is unavailable makes claims "unresolved". A row whose basis is unverified only appears in a list.
- Change: let an outcome-(4) row compete at its published point as a competitor. It earns no label itself. If its published point would dominate or beat the candidate, the candidate's claim reads "unresolved: unverified-basis competitor". Otherwise keep the current omitted-competitor listing.

M2. The Plan evidence lifecycle table (E212) hides the O32 transition.
- Passage: E212 is described as "one table for the stages". It shows "Possibly superseded" at more than 30 days with "official Plan score unchanged" and "route comparison unchanged". The table lists no demotion for reports before day 120.
- Contradiction: O32 and the E151 note say a report-based route lapses to diagnostic once its reports leave the 30-day window. E142 then sends it to API fallback if nothing else survives.
- Consequence: an implementer who builds from the table keeps an 85-day-old report route scored until day 120. An implementer who builds from O32 drops it at day 31.
- The prose says age stages are unreachable for counting reports. The table does not say that, and a table that claims to be the one lifecycle table must not omit the transition.
- Change: add a row or footnote for report partitions: "out of the report window (O32): diagnostic at day 31, no grace, API fallback unless another candidate survives". State that the age rows apply to controlled measurements, transfers and change-detection triggers only.

M3. Bug Hunt record selection (E206) is worded inconsistently, and the rule makes the leaf unstable.
- Wording: the text says "the match key is the roster name, the effort token and the harness and route". Two sentences later it says the record is the largest-sample mean "over every harness and route". The leaf table says harness and route are "chosen by E206". E29 says "the exact model, effort and harness".
- Two faithful implementations could read the harness as part of the key, giving one record per harness, or as the thing chosen by N. The Gemini 4 Argon example shows the intended reading, which is key = (name, effort) and harness chosen by N.
- Instability: a new run on a different CLI can flip the selected harness for one model. That changes the 10% SWE leaf with no change in the model. Meanwhile Terminal-Bench uses a score-independent harness preference.
- Change: state the key as (roster name, effort) with the harness selected by the rule. Add a stability fixture such as "a later run on a second CLI with N one higher flips the record". Consider an N-weighted pooled mean across harnesses, with the spread published as the harness band. Alternatively use a fixed harness preference list, as Terminal-Bench does.

**Low**

L1. The tie-break "the later-numbered record governs" (E191, header) depends on the order in which numbers were issued, not on decision dates.
- E numbers are reused (E177, E182 and E184 each carry several labelled rules). E198 was renumbered to E202, and E198a/b sub-labels sit beside E201a–c.
- The draft itself says the E-numbers resolve conflicts, but the dated ledger holds the real order.
- Change: record a decision date beside each E number in the published registry, and break ties on date, not on number.

L2. The vertex-tie sentence in the Source contract (E195) conflates two cases.
- "Two circles at one vertex … resolved at capture by hovering each … as the 2026-10-17 capture did for two overlapping circles off the line (GLM-5.2 and GPT-5.5)" mixes an on-vertex tie with an off-line overlap. The next clause, "otherwise the vertex check fails", does not say which case it covers.
- Change: split it into two cases and say what the build does when hovering cannot separate two circles that sit on a vertex.

L3. The term "ranked" is used loosely.
- The Counts paragraph defines "cohort row" as "a ranked configuration" and says "ranked rows means cohort rows". Muse Wonder Full is then "ranked" but has "no rank".
- Several denominators use this phrase: ⌈2N/3⌉, E26 and E160.
- Change: replace "ranked rows" with "cohort rows" in normative text.

L4. Comparator key 3 is still called "the owner's highest-eligible rule".
- The draft says AGENTS.md now reads "the selected subscription route". Key 3 sits below identification class and evidence grade.
- Highest-eligible is therefore a tie-breaker, not the rule. E179 does disclose the gain from selecting the largest of several unidentified multiples.
- Change: rename key 3 to "larger multiple within the same class and grade". Keep the citation to the old AGENTS wording as history only.

L5. The Index-reconstruction gate (E209) marks seven basket components unresolved from a discrepancy that may lie in excluded evaluations.
- It checks all ten Index evaluations against AA's total. A 1.0% gap on Fable 5.1 therefore marks the seven in-basket components unresolved, although the gap may sit in HLE, Omniscience or CritPt.
- Fable also fails outcome (4), so the choice is invisible today. For a future row that fails only this test, a bounded alternative would help.
- Change: publish, for such a row, a cost interval of [C_7 − gap, C_7] as a diagnostic, with the row staying out of the labels.

## 2. Methodology design recommendations (prioritised)
1. Fix M1 and M2 first. Both are small, purely definitional edits and they close real disagreement risk.
2. Add a decision-date column to the E-registry. It makes rule precedence checkable by a script, and the build can fail on a conflict (L1).
3. For Bug Hunt (M3), add a harness-flip regression test and publish the harness choice and N next to each leaf value. This mirrors the Terminal-Bench "harness-mixed" marker.
4. Optional diagnostic, not a score change: a leaf-composition shift. Because displayed quality is renormalised over observed leaves, a row missing a hard leaf (HLE, CritPt) is flattered relative to a row that has it.
   - Publish each row's shift as (cohort mean z of missing leaves) − (row's observed weighted mean), as an informational column.
   - This stays inside the no-imputation rule if it is labelled sensitivity. It complements E219 and E221, which bound the shift but do not estimate it.

I did not re-raise: the "confirmed among full-coverage rows" label (rejected in the ledger, M4/R2), the two-thirds admission rule (answered in the ledger, line 1005), or Fable as donor gauge (O35).

Source checked: the AA-Omniscience Index definition is consistent with the draft's O28 reading, bounded −100 to 100, correct minus incorrect over all questions, and no penalty for abstaining. See https://arxiv.org/pdf/2511.13029v1 and https://artificialanalysis.ai/evaluations/omniscience. The formula text in the secondary listing was garbled, so treat the exact formula as unverified against the paper.
I could not verify the 2026-dated AA, SemiAnalysis, tbench.ai or Bug Hunt facts from the public web.

## 3. Questions for the owner
1. M1: if a ranked row's published AA cost is cheaper than a candidate's and the row qualifies, but its pricing basis is unverified, should the candidate's label be withheld as "unresolved", or is "listed as omitted competitor" enough?
2. M3: should Bug Hunt keep the largest-N harness rule, or switch to a fixed harness preference or an N-weighted pooled mean?

## 4. Verdict
VERDICT: HAS FEEDBACK
