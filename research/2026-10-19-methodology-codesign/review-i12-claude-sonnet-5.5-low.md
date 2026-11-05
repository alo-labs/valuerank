# Internal review I12 — Claude Sonnet 5.5, effort low, on draft r71

(Saved from the subagent's report; the reviewer read all 910 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r71`
Last 12 words of the last line: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."
I read all 910 lines in three chunks (1–310, 301–610, 601–910) and the condensed ledger. I did not open the full ledger, apart from grepping it for the "highest-eligible" wording (finding 1). I did not read the code. I ran no web searches. The AA, SemiAnalysis, tbench.ai and Bug Hunt facts postdate my knowledge cutoff and I could not verify them. This review covers the draft's internal consistency and arithmetic only.

Checks that passed (no finding):
- The O28 Omniscience vectors.
- The Bug Hunt vector, 52/105 → 49.52.
- The ladder positions for n = 35, and the n = 2, 3 and 4 minimum rule.
- The bar-currency counts 18/27/10.
- The 70%-coverage fixture. I simulated the arcsine case and got 0.8672, matching the draft's "about 86.7%". The uniform case is 91.47% analytically.
- The Clopper–Pearson endpoints and δ = 0.05/16.
- The E152 basis-typing fixture.
- The 303-task and 33-row panel arithmetic.
- The 20 references in the one-row-per-family diagnostic.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

1. **The comparator's key-3 rationale cites AGENTS.md for a rule it does not contain.**
   - Passage: "the owner's highest-eligible Value Multiple rule (AGENTS.md)", and again "because the owner's rule divides the Plan basis by the highest eligible Value Multiple (AGENTS.md)".
   - The repository `AGENTS.md` says only that cost is divided by "the selected subscription route's Value Multiple at full utilisation (O3)". `grep -i highest AGENTS.md` matches only the near-frontier sentence.
   - The ledger (E93, E111, E171) says the rule comes from AGENTS.md. So either the text lives somewhere I could not see, or an editor reading is being presented as owner policy.
   - Why it matters: key 3 decides route choice among unidentified routes, and that choice moves the Plan scores. If the owner never wrote "highest eligible", the key-3 direction is an editor decision, and a reader cannot tell which.
   - Change: cite the exact owner decision ID and date that states "highest eligible". If none exists, relabel key 3 as an editor decision (E85/E93), keep it, and put it on the owner-confirmation list.

2. **"Ranked rows" has two meanings, so the clip-gate threshold is ambiguous.**
   - Passage: "'ranked rows' means cohort rows" (37), but a "scored row … has a value score and a rank" (36, because Muse Wonder Full has no rank).
   - The clip gate holds the release when "more than max(1, 10% of ranked rows) clip", "per basis". Subset-workload rows and Plan rows use different anchor objects.
   - Two faithful builds can use N = 37, 36, the main-workload panel (33), or the basis's scored rows. 10% of 37 and of 36 happen to give the same integer cutoff today, but not at other cohort sizes. The fixture "integer-boundary fixtures for several cohort sizes" cannot be written without a stated denominator.
   - Change: define the clip-gate denominator once. For example, "scored rows on that basis and anchor object", with subset workloads gated against their own anchor object, or excluded. Replace "ranked rows" in the gate, R_W and the 2N/3 text with the defined term (cohort row or scored row).

3. **Precedence between two tagged rules has a gap.**
   - E191 and the preamble say owner beats editor, and "a rule that amends another governs it".
   - They are silent when two editor rules conflict and neither cites the other. With roughly 200 E-tags, many re-tagged or split (E182, E184, E177, E183, E198 and E202 each appear in more than one place in the brief), that case is likely.
   - Concrete example: E163/E187 ("also ranked when…") against E193/E205/O33 for what counts as a family's primary row.
   - Change: add a fallback ("otherwise the later-numbered record governs, and the build's rule-index lint fails on an unresolved conflict"). Generate a rule index (ID, section, amends, status) from the registry and publish it with each release.

4. **Two freshness limits for the same AA capture.**
   - E211 requires the chart and catalog capture to be at most 7 days old at the release cutoff. Governance separately says "AA cost snapshot and price list max age 45 days".
   - If costs come from the same capture, 45 days is dead text. If costs come from a separate capture, the draft does not say which artifact each limit applies to, and a 45-day-old cost joined to a 7-day-old frontier breaks the premise of O29 and E170.
   - Change: name the artifacts. For example, chart and catalog ≤ 7 days, and per-configuration cost pages and price records ≤ N days, each with its own capture time in the evidence bundle. Or delete the 45-day clause if it is superseded.

**Low**

5. **Wording contradiction: "no 'recommended' label" against a "confirmed cheapest" label.**
   - Passage: "There is no 'recommended' label (O22)", while confirmed-cheapest and scenario-supported labels remain.
   - Today the confirmed-cheapest label can go to at most 5 of 21 possible qualifiers (E201b), and a Plan label is structurally unavailable.
   - The headline table is therefore the only claim readers will see for the Plan buyer. The "exploratory" caveat is carried only by a label. It is not repeated as a sentence in the Outputs section where the Plan ranking is introduced.
   - Change: put one line in Outputs item 1: "Plan ranking = displayed arithmetic on owner-named transfers and unidentified observed multiples; no Plan claim is supported today."

6. **Terminal-Bench and "AA-run" share accounting unclear.**
   - "≈80% AA-run … ≈20% independent (Bug Hunt, Terminal-Bench)": the leave-AA-out branch is "not identifiable" while retained weight is 20%.
   - Two of the three Terminal-Bench executions in the cost basket are AA's. State that this overlap is a cost-side exposure only, so it is not read as quality-side independence. Adding the sentence is enough.

## 2. Methodology design recommendations
1. **Publish a machine-generated rule index (priority 1).** It lists each rule ID, section, the rules it amends, the owner or editor source and its status (fired, passed, vacuous). The preamble's precedence statement depends on this index. It also lets two implementers confirm they read the same 200-odd rules. The active-rules manifest (E63) already exists, so this extends it.
2. **Split the document.** Keep a short published methodology of about 6 pages, covering objective, scoring, bar ladder, uncertainty labels and limitations. Move the executable specification (the Normative definitions and all fixtures) to an appendix, with the revision history in the ledger. The current single file, with its dense bracketed editor-decision tags, is hard for an outside reader to audit. That cuts against a public ranking's purpose.
3. **Define denominators in a glossary table.** List every population (cohort row, scored row, bar-population row, R_W, U_W, reference panel, common-workload panel) with today's count. Many findings in earlier rounds came from this ambiguity.

## 3. Questions for the owner
1. Is there a written owner decision, with ID and date, that the Plan route is the highest eligible multiple within evidence grade (finding 1)? If not, confirm or amend comparator key 3.
2. For the clip gate: should the denominator be scored rows on the basis, with subset workloads gated on their own anchors (finding 2)?

## 4. Verdict
VERDICT: HAS FEEDBACK
