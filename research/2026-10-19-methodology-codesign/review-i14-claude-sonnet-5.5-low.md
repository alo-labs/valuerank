# Internal review I14 — Claude Sonnet 5.5, effort low, on draft r73

(Saved from the subagent's report; the reviewer read all 926 folded lines.)

## 0. Read check
- First line: "# ValueRank methodology — draft r73"
- Last 12 words of the last line: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."

I read all 926 lines of the draft and the condensed ledger. I grepped the full ledger only for terms I suspected were already decided. I did not run the implementation, and I did not use web search. Most claims are internal to the project or concern 2026 data, so I could not check them externally. I did check the arithmetic the draft states:
- The arcsine fixture gives 86.7% (Monte Carlo 0.8672).
- The uniform fixture gives 91.5%.
- The ladder positions, the Omniscience and Bug Hunt test vectors, the old (2A+N)/3 counterexamples and the Clopper–Pearson endpoints are all correct.
- The E210 category-mix bound derives correctly.
- The exchange-rate figures (2.74 and 1.73 value points per cost doubling) imply anchor ratios of about 558 and 22,500. Both are consistent with the stated low anchors and the $13,400 Plan upper anchor.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

1. **AGENTS.md requires two things the draft never states.**
   - **Allocation regime.** AGENTS.md says SemiAnalysis results must preserve "exact model, plan, workload, publication date and allocation regime". "Allocation regime" appears nowhere in the draft or the ledger. The measurement object E111 lists route, partition, workload, valuation basis and dates, but no allocation regime. Without it, two faithful implementations can pool or compare SemiAnalysis measurements taken under different allocation regimes.
   - **Direct owner links.** AGENTS.md requires "direct owner links in the reconciliation inventory". The draft records "artifact, field locator, published value" per observation and one repository URL for Bug Hunt. It never requires a direct owner URL per observation or per configuration.
   - **Fix.** Add `allocation_regime` (as published by SemiAnalysis) to the E111 measurement object and to comparability record E102. Add `owner_url` to every scored-observation record and to the reconciliation inventory, with a build check that it is non-empty.

2. **The report search has no age gate, although every other input has one.**
   - **Where.** The Report window paragraph (E213) says the search cutoff is 2026-10-08, 13 days before V, and the window is disclosed as "not searched" afterwards.
   - **Asymmetry.** The cohort capture must be at most 7 days old (E211), the chart and model-page snapshots at most 7 days apart (E217), and the snapshot and price records at most 45 days old (E216). Report discovery is a disclosure only. Reports dated 10-09 to 10-21 can be missed, and that decides whether a report route reaches two concordant sources (O11/O32). The draft says "reports admitted before lapse at 30 days" but lets discovery lag silently.
   - **New argument.** The ledger (M3) chose disclosure over a gate. A gate costs one build check and removes the failure mode. A route that passes or fails on the 13 undiscovered days is not reproducible.
   - **Fix.** Require V minus search cutoff to be at most 7 days, matching E211, or fail the build. If a longer lag is accepted, require a dated owner note.

3. **Bug Hunt record selection (E206) has no tie-break, and the leaf table contradicts it.**
   - **Missing tie-break.** E206 picks the largest-sample mean over every harness and route. It does not say what happens when two records share the largest N, for example a mean of 3 on one CLI and a mean of 3 on another for the same model and effort. Two implementations will disagree.
   - **Contradiction.** The leaf table (line 436) and the E29 estimand say "exact model, effort and harness". E206 selects the harness by sample size. The leaf's harness is therefore an output of selection, not a match key.
   - **Fix.** Add a total order, for example largest N, then most recent report date, then harness name. Reword the leaf table to "the exact model and effort, harness chosen by E206 and recorded".

4. **The "Frontier and near families differ on purpose" bullet misstates the provisional rule.**
   - **Where.** Lines 125-126 say a frontier family ranked at a point lacking DeepSWE or Bug Hunt results "is then flagged provisional".
   - **Contradiction with the rule.** Under the provisional rule (lines 464-465), a missing Bug Hunt leaf alone leaves coverage at 90%, observed SWE weight at 50, and DeepSWE present. That row is not provisional. Only a missing DeepSWE, or coverage below 70%, makes a row provisional.
   - **Why it matters.** Provisional status excludes a row from unique-cheapest labels and from the bar population, so the prose misleads about who can be labelled.
   - **Fix.** Change the sentence to "flagged provisional when the provisional rule fires (for example no DeepSWE)".

5. **Confirmed-cheapest is close to unreachable by construction, and the published answer is a large "possible" set.**
   - **The mechanism.** A confirmed cheapest requires every cheaper row that can possibly qualify to be strictly dearer. Possible qualification gives missing leaves the full 0–100 domain (O25, E198b). A cheap row with 70% coverage clears a bar of 56.7 whenever its displayed quality is at least about 38, so cheap, low-coverage rows almost always possibly qualify. Today: 21 possible qualifiers against 5 confirmed (E201b).
   - **Why it hurts.** The "cheapest above a bar" output cannot answer its own question. The only substitute is E203's displayed-record cheapest, which the draft labels "not a claim".
   - **Not a challenge to O25.** This concerns the missing-leaf domain, which is structural, not the published-record target.
   - **Fix.** See design recommendation 1.

**Low**

6. **E216's 45-day snapshot limit is dead.** E211 requires the chart capture to be at most 7 days old, and E217 requires the snapshot to be within 7 days of the chart. That bounds the snapshot at 14 days at V, so the snapshot half of E216 never binds. State this, or tighten E216 to 14 days and keep 45 days for price records only.

7. **Cost status list conflicts with the E209 scale.** The sentence "Statuses: complete (published record) / confirmed incomplete" (lines 172-174) lists two statuses, while the next clause and E209 define four (complete, unresolved, confirmed incomplete, missing). Delete the two-status list or point to E209.

8. **Terminal-Bench row choice is not reproducible from the draft.** "A pre-registered agent preference (vendor-neutral harness first)" names no ordered list and no tie-break. State the order, or cite the registry field that holds it.

9. **Precedence rule E191 is fragile.** "Later-numbered record governs" is weak because the draft itself shows E numbers are not chronological (E202 was tagged E198; E170 was added at r53). Keep the rule only as a last resort. Require that each of the two conflicting records states which governs. Make that a build lint, since the draft says such a conflict is a defect.

## 2. Methodology design recommendations

1. **Add a labelled "observed-range" variant of the bar interval outputs (priority 1).**
   - **Change.** Besides the full 0–100 domain, publish K_r and confirmed/possible cheapest again with each missing leaf bounded by the cohort's observed min/max for that leaf. The draft already defines this "sensitivity band" in the Quality section but does not apply it to the bar outputs.
   - **Labelling.** Call it "sensitivity, not evidence", and keep it out of Θ and out of every label (O19, O25 are untouched).
   - **Benefit.** It shows readers how much of the 21-versus-5 gap is pure missing-leaf ignorance. It is implementable from existing data.

2. **Publish a coverage-matched bar result.** Compute the headline bar answer on the full-coverage rows only (a subset population), with the same H. This is deterministic, uses no new evidence, and turns the displayed-record cheapest into a result with a stated population.

3. **Report Plan anchor sensitivity next to the Plan exchange rate.**
   - **Observation.** The Plan span of about 22,500 times mixes divided costs (about $0.61) with an API-fallback upper anchor ($13,400, Grok 4.7). The frontier-families diagnostic cuts the upper anchor to $7,257 and moves the slope from 1.73 to 2.02, a 17% change in Plan cost's influence.
   - **Suggestion.** Print that slope range in the headline next to E196, not only in a diagnostic. The inclusion rule (E160) can stay.

4. **Pair the report-search age gate with a "reports not searched" count in the claim.** Where a route's O11 status depends on the discovery gap, flag it "discovery-sensitive" instead of leaving it to a prose disclosure.

## 3. Questions for the owner

1. **Owner decision challenge: the two-thirds admission gate.** AGENTS.md says each basket component is "admitted once its exact-configuration cost is captured", and O17 already scores rows missing a component on a labelled subset. E26/E95 additionally require two-thirds jointly complete coverage. As a result FrontierCode (15 of 37 rows) and ITBench-AA (9 of 37) stay out of cost although FrontierCode carries 10% of quality. Do you intend "captured" to mean two-thirds coverage? If instead any capture admits the component, FrontierCode would enter cost now and 22 rows would be scored on subsets.
2. Should Bug Hunt ties between harnesses at equal N break toward the most recent report, or toward the vendor-neutral harness? (Finding 3.)
3. May the observed-range sensitivity (recommendation 1) appear in the published summary beside the bar results, given it is outside the published-record target of O25?

## 4. Verdict
VERDICT: HAS FEEDBACK
