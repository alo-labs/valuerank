# DR-OUTLINE: findings map tied to evidence

Evidence is cited by the first eight hex characters of `evidence_id`; `S<n>` is the source display number. Core-claim labels (C1 to C28) are defined in `triangulation.md`. This file was revised in DR-REFINE (2026-10-17) after the second retrieval pass (S92 to S131, 55 new evidence rows).

## Adaptation from the research plan

The plan's eight angles are kept. Triangulation changed the emphasis in four ways, each driven by evidence in hand.

1. **Assumption A3 is partly refuted.** Wokey (S52) and RemakeBench (S53, S107) maintain dated plan-allowance measurements, so the plan-allowance section is organised around measurement classes and their conflicts (X1 to X3, X16), not around "posts versus rankings". Evidence: 5111682e, 52ceba1b, 53a223b7, f157c276.
2. **Assumption A4 splits.** Dating is common (nine of twelve aggregators), variant labelling is a minority practice (three of twelve), imputation policy is rare (two), and evidence-class grading is not found. The provenance section compares practices with counts. Evidence: c6e57b1d, d7c705fd, 473fb9be, 12b04552, e595b5bf, 59a69c9a.
3. **Artificial Analysis dependence is a first-order finding, stated with a count.** Five of the twelve aggregators in report Table 2 take AA cost or the AA index; seven do not (corrected from "most inherit"). Evidence: f14c55f8, 92b36303, 7fca5fa3, 9d51c84e, 04e2b86b, b4fc294d, 31ef13c9.
4. **Non-US coverage is thin.** The SuperCLUE cost quadrant is secondary-only; Chinese vendor coding plans were read in the second pass; OpenCompass and HELM cost treatment is a gap. Evidence: 0f67abb0, 952aa8d4, 7ff0e0b5, 0e7df606, 5f750617.

## Refine changes (DR-REFINE)

5. **A1 is restated with a definition of "combine"** (quality measure, plan-derived cost, joined ranked figure) and a partial-combinations table (RemakeBench: "There is no aggregate score"; Klu: subscription-only model in a footnote). Evidence: 76be258a, eaceded4, 2bde0a91, c1866a94, 909140e0.
6. **The Max 20x spread compares like with like**: four allowance measurements (1.7 times); the ml0x consumed-workload figure is kept separate; the OpenAI $200 figures are lined up by date and plan label. Evidence: 5111682e, b32605eb, 638d773c, 98008266, 2edf813b, 14b6f5f0, 1080b94f, 98972d5b, 8dc04381.
7. **Three findings are added** (F8 plan families beyond Claude and Codex; F9 ValueRank's plan formula tested; F10 reuse terms) and the old F8 becomes F11 with a partial-combinations table and a "where ValueRank is weaker" paragraph.
8. **Recommendation 4 is corrected** (API basis is AA total cost over all attempts, not divided by successes) and the recommendations gain a sensitivity test, a licence check, archiving and explicit withdrawal triggers.
9. **Limitations moves ahead of Recommendations**, and carries a disposition table for lead-scan pages and the claim-support counts.

## Report structure and evidence map

| Section | Purpose | Evidence ids (prefixes) | Core claims |
|---|---|---|---|
| Executive Summary | answer, assumption verdicts, decision risk | all below | C1 to C28 |
| Introduction | question, definition of combine, scope, method in brief, baseline | cabcc834 | C20 |
| F1 Landscape map and taxonomy | five site families, overlap categories, business models | 914291b0, 15d3a9b9, 4af6f42f, 1ab603f6, 53a223b7, 5df0deae, 0f67abb0, ab48edab | C1, C2, C18 |
| F2 API price-performance aggregators and formulas | formula table with AA-derived column, leaders can differ, AA dependence count, staleness | 15d3a9b9, d0d37a3c, bb6276e7, 86ac17e3, 4af6f42f, 446c1d01, 970e3151, 562e8998, 40ddcda8, 04e2b86b, 4398bc75, 9d51c84e, 7a21bae0, 9d1cd4ef, f14c55f8, 92b36303, 7fca5fa3, d9c7238c, b84150a1 | C2, C3, C4, C6, C13 |
| F3 Cost per task and benchmark-owner views | AA, Aider, Terminal-Bench, Vals, HAL, LiveBench (definition unconfirmed), cost per success, failed-attempt spend | 914291b0, 9844fd34, 74d45988, d7c705fd, 4a2e26df, 588860ca, 5df0deae, 6e694250, e3f14e77, af55e562, 8d9dcf1e, 4ccdfabd, b4fc294d, 31ef13c9 | C5, C7, C15, C19 |
| F4 Subscription-plan allowance measurement | five classes, like-for-like Max 20x table, consumed workload separate, OpenAI by date, regularities | 2e78f470, 78455d48, 5111682e, 52ceba1b, 53a223b7, 638d773c, 98008266, efe28642, 2edf813b, b32605eb, 98972d5b, 8dc04381, 1080b94f, 14b6f5f0, e85fd81e, dfe9a829, a5cec89b, c36ddee6, 122468a8, 2c407573, 1ab603f6, 4be107a3 | C8, C9, C10, C11, C21, C28 |
| F5 Provenance and evidence practices | counted practices, uncertainty markers, partial analogue | c6e57b1d, d7c705fd, 473fb9be, 12b04552, ab48edab, e595b5bf, 52ceba1b, 59a69c9a, 7fe4c798, 29fb5308 | C12, C13, C18 |
| F6 Research and critique | academic base for cost-aware ranking and its limits | c618e708, ce5df1a5, d98b684f, 98126ceb, 5cbc378b, 4a431957, 55bf436e, 4882375a, b3eca6ac | C14, C15 |
| F7 Non-US views | SuperCLUE (attributed, manually checked), OpenCompass, HELM | 0f67abb0, a91b5530, 952aa8d4, 5723b6cd, 77e281ff, 03c1402e, 09479d4e | C16 |
| F8 Plan families beyond Claude and Codex | Copilot, Cursor, Chinese vendor plans, consumer guides, community posts | 7e6f689e, de844f80, 05ba2e58, ee4b9fc2, 6556af8e, b2dcae7e, b2d3102b, 0e7df606, 5f750617, 9ac64ac2, 8f989096, adfc367e, fe1d6275, 98972d5b, b32605eb | C22, C23, C24, C28 |
| F9 ValueRank's plan formula tested | workload dependence, highest-eligible selection, paywalled numerator, model-specific allowance | cabcc834, abe197f7, 3aa1df58, ac9a641a, ac96d9e5, 5111682e, 14b6f5f0, 03fd0f2c, ee31ae11, 2e78f470 | C21, C27 |
| F10 Reuse terms of the upstream data | AA terms and API attribution, WhatLLM note, LiveBench licence | 66405636, 26221e56, 5ec475e6, 44865d85, d6fce15d | C26 |
| F11 Where ValueRank overlaps, is alone, is weaker | partial combinations, uniqueness bounds, trade-offs | cabcc834, 74d45988, c1866a94, 13640ab8, 76be258a, 2bde0a91, 473fb9be, e595b5bf, 52ceba1b | C1, C12, C20, C25 |
| Comparative landscape, verdicts, head-to-head | condensed register | triangulation.md section 4 | all |
| Counterevidence Register | statements tested and effects | see report | C1, C3, C9, C10, C26 |
| Limitations and gaps | unread pages, single-sourced claims, claim-support counts | triangulation.md section 3 | all |
| Recommendations | positioning, sensitivity test, API-basis disclosure, licence check, triggers | derived; each item names its evidence | C10, C11, C15, C19, C21, C26, C27 |

## Claims that must be hedged in prose

- Any precise Claude Max 20x or OpenAI allowance (C10): give a dated range and the measurement class; keep consumed workload separate.
- RemakeBench's allowance: one account, one window, plan string "Pro", Medium confidence.
- SemiAnalysis headline multiples (S46 secondary; primary partly paywalled); cache statement "on some plans", established for Anthropic only.
- SuperCLUE quadrant (secondary-only); LMArena price display (D4 relays); LiveBench cost-file definition (undocumented); evidence-class grading absence (three searches, one listing).
- Reasoning-overhead magnitudes (vendor claims).
- "Alone" statements about ValueRank (C20) and A1: bounded to this search, flagged for conflict of interest, dependent on the definition of combine.
- The ValueRank plan-formula findings (C27) are the analyst's inference; the licence position (C26) is stated as what the terms say, not as legal advice.
