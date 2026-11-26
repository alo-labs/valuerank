# Internal review I32 — Claude Sonnet 5.5 (effort low) on draft r91

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r91".
- Last line of the draft (the folded copy's final line): "Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: `reviewer-prompt.md`; the whole folded draft (915 lines, in chunks); `ledger-brief.md` (opening and owner decisions); `ledger.md` from "Internal review I28" to the end (I28–I31, O56, O57); `AGENTS.md`. I spot-checked the stated figures against the draft itself and against the generated `scores.md` (rank separability 3.01 API / 3.01 Plan, 1 of 8 and 2 of 11).

Checks I ran that came out consistent (no finding):
- The leaf tables sum to 60/20/10/10 in both rankings. Leaf counts are 14 and 11. The AGENTS.md O52–O55 weights match (FrontierCode 18/21, Terminal-Bench 14/17, Bug Hunt 10/12, and so on).
- The independent-weight shares 28% and 22% match the leaf tables.
- The basket-scope retained weight of 86.7% matches.
- The bar ladders match floor((n−1)k/4) for n = 9, 15 and 32. The "rows reaching a bar" counts 5/7/3 and 8/12/5 follow from those positions.
- The ⌈2N/3⌉ thresholds are 6 and 10. The 255 and 127 feasible alternatives equal 2^8−1 and 2^7−1.
- The exchange rates 3.04, 2.44, 2.83 and 1.89 follow from the stated padded anchors and 100·β·ln2/ln(c_H/c_L). The offsets divide by 0.75, and the E242 tolerances 2.35 and 5.28 follow from the stated medians.
- The counts of 20 and 14 listed configurations and the 9 unranked configurations reconcile with 29, 9 and 15, with four overlapping.
- The Plan-row counts (27 and 50), the 22 main-workload plan rows and the 5 subset-only rows reconcile.
- The SemiAnalysis age arithmetic (last Current day 2026-11-05, expiry 2027-01-05, demotion 2027-02-04) is correct.
- The 7-of-9 and 2-of-15 Coding Agent Index coverage counts agree with the 7-of-29 statement, given that the 2 AI Coding Daily rows are among the 7.
- The draft agrees with O57 and AGENTS.md on per-ranking admission, the cohort rule, the ranking structure and the Plan-row rule.

## 1. Findings by severity

**Critical**

None

**High**

None

**Medium**

None

**Low**

- L1. The listed-configuration explanation is incomplete. "Cohort and configuration" says which listed rows are family primaries and names two "also listed" near points (Claude Haiku 5.5 (low) and Claude Sonnet 5.5 (xhigh)). The nine listed configurations are named in the E255 paragraph. Claude Opus 5.5 (xhigh), GPT-6.1 Sol (xhigh) and GPT-6 Luna (low) appear there but are not placed anywhere as frontier non-primary points.
  - Why it hurts: a reader cannot reconcile the nine listed configurations with the four primaries plus two near points, which accounts for six.
  - Change: add one clause saying the remaining three are non-primary rendered-frontier points of ranked families (their primaries Claude Opus 5.5 (max), GPT-6.1 Sol (max) and GPT-6 Luna (max) are ranked).
  - Not Medium: the rule is unambiguous, and only the explanation of today's list is missing.
- L2. In the noise-band paragraph of Outputs item 1, two adjacent parentheticals read "(today no configuration's plan rows span that far) (today, max-effort ranking: …)". The sentence beginning "should one configuration's plan rows ever span…" is also very long.
  - Change: split it, and move the band list to its own sentence.
- L3. The revision-history italic block runs to about 35 lines and keeps being extended. Each revision's rationale is in the ledger, as the ledger already says. The block now exceeds the length of several normative sections and hides the reading rule at the top.
  - Change: keep one line per rung (r16–r60, r61–r79, r80–r91) and point to the ledger. I note that I29 L3 rejected a similar point, so this is offered only as a presentation suggestion with no new argument beyond length; the owner may drop it.
- L4. "Today 5, 7 and 3 of the max-effort ranking's 9 rows reach its headline, lower and upper bars" is placed next to "5 main-workload rows reach 60.7" and "bar currency's 7 of 9". The text explains the 7-versus-5 difference only for the lower bar. A short parenthesis that the headline and upper counts are identical on both populations would prevent a misreading.

## 2. Methodology design recommendations

1. No change to the scoring, admission, ranking or uncertainty rules is recommended. The per-ranking structure is internally consistent and matches the owner decisions in AGENTS.md (O36, O38, O48, O50–O55, O57).
2. Presentation only (lowest priority):
   - add the missing explanation of the nine listed configurations (L1);
   - shorten the revision history (L3);
   - emit the band list as a generated table in the published summary, not inline in a running sentence (L2).
3. Keep generating every "today" figure from the build and not by hand. This round's checks found no stale figure, which is the property the E258 and r89 fixes were meant to secure.

## 3. Questions for the owner

None

## 4. Verdict

VERDICT: NO FURTHER FEEDBACK
