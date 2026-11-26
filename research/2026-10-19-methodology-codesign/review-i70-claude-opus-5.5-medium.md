# Internal review I70 — Claude Opus 5.5 (effort medium) on draft r129

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r129`
- Last line of the draft (line 174): the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r129 (sixty-ninth internal review, the second at Opus 5.5 medium, and owner decision O88) states O86 as one formula, extends effort-invariance to SemiAnalysis figures for the same model, keys report cells by AA family, and gives O46 ceilings their own amount type and selection reason. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "selection reason. Every change is recorded with its rationale in the ledger."

What I read:
- `reviewer-prompt.md` and `ledger-brief.md`.
- `ledger.md` from "## Internal review I28" to the end: O45–O88, E247–E270, I29–I69 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` in full.
- `review-i69-claude-opus-5.5-medium.md`.
- `draft-r129.md`, every line (lines 1–174), as a line-tagged copy folded at 1,500 characters (315 segments). I also diffed `draft-r129.src.md` against `draft-r128.src.md`. The diff shows the r129 changes: the route key, E98, E139, E107, E33, the eligibility-profile O86 sentence, E106 case (1), the GPT routes bullet (O88), E166's amount kinds and the history entry.

What I verified:
- **Checks and tests.**
  - `python3 -m valuerank.draft_figures check` exits 0.
  - `tests/test_plan_reports_provenance.py`, `tests/test_plan_admission.py`, `tests/test_draft_figures.py` and `tests/test_plan_routes.py` pass (282 tests). I ran them with bytecode and the pytest cache off.
  - `git status` was clean before I wrote this file. HEAD is 95fdac0, the r129 commit.
- **O88 in the route data** (`data/plan_cost_routes.json`, 137 routes).
  - 24 same-model routes:
    - GPT-6.1 Sol at xhigh, high, medium and low on four plans each.
    - GPT-6 Astra at high and xhigh on four plans each.
  - Each takes its own model's SemiAnalysis figure, for example Astra on Pro 200 at 14.485 and Sol on Plus at 10.55. Each is graded `user_assumption` and names its own model's donor route.
  - Every other GPT row still takes O45's lower-of figure. For example GPT-6 Luna (max) on Plus takes Astra's 8.1, and on Pro 200 it takes Sol's 10.42.
- **Plan rows** (`planRows` in `data/scores.json`).
  - Max-effort ranking: 27 rows, of which 14 are assumptions (10 transfers and 4 ceilings), 11 controlled measurements and 2 API fallbacks. 21 rows are flagged possibly superseded and 21 have an unverified valuation basis.
  - AI Coding Daily ranking: 51 rows, of which 48 are assumptions and 3 are fallbacks; 44 / 44.
  - These match Output 1, the separability sentence ("14 of 27 … 48 of 51") and the limitations.
  - GPT-6 Astra (high) selects Pro 200 at 14.485, with Plan value 52.84 and rank 18, as the O88 ledger entry states.
  - The O88 rows are "no measured route" in `measuredOnlyPlanView`, so the build treats them as assumptions.
- **Report cells** (`planAllowanceCells`).
  - 52 cells per ranking, none passing, 28 on listed plans.
  - Cells are keyed by AA family ("GPT-6 Astra", "Gemini 4 Argon"). Each cell publishes the configurations and efforts it pools.
  - The Google AI Pro / Gemini 4 Argon cell fails at 1.35×.
  - I read `valuerank/plan_admission.py` in full, and `value_v3.py` lines 795–815 (the families map).
- **MiMo-V2.6-Pro's ceiling row.** Its `rows[].plan` now carries the I69 L3 changes:
  - capacity status "provider quota ceiling";
  - amount kind "provider quota ceiling: the full quota at API rates";
  - selection reason "larger quota-ceiling multiple".
- **Dates and positions.** The lifecycle dates (2026-11-05, 2027-01-05, 2027-02-04 from the 2026-10-06 publication), the ladder positions for n = 9 and n = 15, and the bar-setter placeholders for E201b.
- **The O71 research directories** exist with their stage records. `data/plan_reports.json` has 107 rows and 93 `notTabulated` entries.

Not verified: live web pages, the paywalled SemiAnalysis article, the Monte Carlo outputs and the full test suite.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. O88 is applied in the route data, the draft and the README, but the published GPT rule and AGENTS.md still state the rule it replaced.**

The draft (line 59) says:
- GPT-6.1 Sol's and GPT-6 Astra's other efforts take their own model's figure per plan, as a same-model assumption (O88);
- every other GPT row takes O45's lower-of figure.

The route data and the README's Plan table follow this. The README labels GPT-6.1 Sol (high), GPT-6.1 Sol (medium) and GPT-6 Astra (high) "same-model assumption (O88)".

Two governing texts were not updated:
1. **The registry's rule text** `evidencePolicy.gptApplication` (`data/plan_cost_routes.json`). It is rendered as the GPT bullet of `methodology.md` (line 163) and into `site/data/plans.json`. It still says: "every other GPT row (other GPT models and GPT-6.1 Sol at xhigh, high, medium and low …) takes, per plan, the lower of the two reported model-conditional figures". It does not mention GPT-6 Astra's other efforts at all.
2. **AGENTS.md's GPT bullet** (Subscription allowance section). It still says: "every other GPT row, including other efforts of those models, takes per plan the lower of the two reported figures". r129 added O88 to the "Match reported API-priced usage" bullet two lines above it, so AGENTS.md now contradicts itself on the one point O88 decided.

Why Medium:
- The published methodology summary and the repository's binding instructions give a different multiple for 24 routes than the build uses and the README prints beside them. Examples:
  - GPT-6 Astra (high) on Pro 200: 10.42 under the stale text, 14.485 under O88. Its Plan value moves from 52.05 to 52.84.
  - GPT-6.1 Sol's other efforts on Plus: 8.1 under the stale text, 10.55 under O88.
- An agent that follows AGENTS.md's GPT bullet when it refreshes routes would revert O88.
- A reader of methodology.md would find the rule contradicted by the table below it.
- This is the class I69 M1 was rated Medium for: AGENTS.md states a rule the build does not apply.

What is new: O88 dates from 2026-10-28 and arrived with r129. No review has seen these texts since.

Change:
- Rewrite `gptApplication` as: "GPT-6.1 Sol and GPT-6 Astra keep their own SemiAnalysis figures on every ChatGPT plan (O45); each model's other efforts take that model's own figure per plan as a labelled same-model assumption (O88, 2026-10-28; an allowance is effort-invariant, O87); every other GPT model takes, per plan, the lower of the two figures as a labelled user assumption naming its donor route (O45)."
- Replace the AGENTS.md bullet's "including other efforts of those models" with the same O88 sentence.
- Regenerate methodology.md and the site.
- Close the class at its source (recommendation 1). r128 left a stale `gptApplication`-type text for O86 (I69 M1), and r129 leaves one for O88. Hand-kept rule prose in the registry and AGENTS.md is not covered by the E265 check.

### Low

**L1. E106 case (1) cites O88 as making other-effort plan evidence compatible, but O88's routes are assumptions. The draft's lists of assumptions do not name them.**

What r129 says:
- Case (1) of E106 now reads: "… an effort not the configuration's for evidence other than a plan allowance …; a plan allowance is effort-invariant, O87, O88".
- Read with the table's own preamble ("every route is classified once"), SemiAnalysis's Astra figure is then compatible evidence for GPT-6 Astra (high). Nothing in the table sends it to case (2).
- Taken literally, it becomes exact-route evidence under case (3). It would then take comparator grade "controlled measurement of the exact model" and enter the measured-only view (E113).

What O88 and the build do:
- O88 says "a labelled same-model assumption". The build grades the route `assumption`, flags it "owner-named transfer (assumption)", lists the row as "no measured route", and removes it in the transfers-off streams.

Other places that do not name the O88 routes:
- The Assumptions bullet (line 58) says that "only the owner-named model-to-model transfers … and the owner's MiMo quota ceilings stay in the official Plan ranking". An O88 route is neither.
- E167 (line 98) defines the assumption set as "an owner-named transfer, or an O46 MiMo quota ceiling".
- E242's † set has the same gap.

The outcome is decided by O88 and the build. But the draft's governing table and its two enumerations no longer describe it.

Change:
- In case (1), cite O87 for user reports only.
- Add to case (2): "an O88 same-model figure is an owner-named assumption".
- Name "the O88 same-model assumptions" in the Assumptions bullet, E167 and E242.

**L2. O88 rows carry two labels, and O88's general premise is labelled differently for Claude.**

GPT rows:
- `planLabel` reads "same-model assumption (O88)".
- `flags`, `amount.amountKind` and `amount.interpretationLabel` read "owner-named transfer" (for example GPT-6 Astra (high)'s `rows[].plan` in the AI Coding Daily ranking).
- The route IDs still end in `-common-gpt-assumption`.

Claude rows:
- The ledger's O88 entry is general: "a figure measured for a model serves every effort of that model, as a labelled same-model assumption naming its donor route".
- Claude Opus 5.5 (high) and (medium) are that case. They are still labelled "common Claude assumption", in the draft (line 59) and in `planLabel`. The multiples are identical, so no value changes.

A smaller point: in line 59, "Every other effort of those two models" follows a sentence about Claude Opus 5.5. "Those two models" therefore reads as ambiguous; it means GPT-6.1 Sol and GPT-6 Astra, two sentences earlier.

Change:
- Give same-model routes one flag and amount kind: "same-model assumption (O88), donor named".
- Ask the owner whether the Claude same-model rows take the O88 label (Q1).
- Name the two GPT models in that sentence.

**L3. The O86 gloss that I69 M1 corrected in the draft survives in code and in a published status string.**

- `valuerank/plan_admission.py` still says "one value lies within 1.20× of every report's range": in the module docstring (line 12) and in the comment at line 150. That is the 1.44× reading that I69 M1 showed is wrong.
- The published cell status in `scores.json` reads "fails: no common value within 1.20× (1.35× apart)".
- For the Gemini 4 Argon cell this phrase is false on its natural reading. v = 10 lies within 1.20× of all three ranges. What fails is the band test: 11.4 ÷ 8.47 = 1.35 > 1.20.
- The verdict is right. Only its stated reason is wrong.

What is new: the status string. I69 named the docstring but not the published string, and the ledger's I69 M1 entry records the draft and AGENTS.md as fixed, not the code.

Change:
- Make the status read "fails: largest lower bound is 1.35× the smallest upper bound (limit 1.20×, O86)", and update the two test assertions.
- Replace the docstring and comment with the formula.

**L4. Two registry texts are stale or carry review labels.**

- `evidencePolicy.o72Application` is headed "Owner decisions O72-O88", but its text stops at O85. O86's concordance test, O87's effort pooling and O88 are not stated in it.
- The O46 ceiling amounts publish `derivation: "quota ceiling: the tier's credits at the provider's API rate (I69 L3)"`. That puts an internal review label into published data. I44 L6 removed review labels from the specification's body for this reason.

Change:
- Add O86–O88 to `o72Application`.
- Cite O46 in place of "I69 L3".

## 2. Methodology design recommendations

1. **Bring hand-written rule prose under a check (closes M1 and L4, and the class behind I69 M1).**
   - Today E265 checks figures, and `{{absent:…}}` checks absence claims. Owner-decision rule texts in the registry (`gptApplication`, `o72Application`, `mimoApplication`, `reportEligibilityProfile.rules`) and in AGENTS.md are checked by nothing.
   - Register, for each owner decision that amends a rule, the registry keys and AGENTS.md bullets that state that rule. A test should fail when one of them does not cite the amending decision. For example, every text that states the GPT effort rule must cite O88 once O88 exists.
   - Better still, generate `gptApplication` from the route data's structure: own-figure models, same-model efforts and lower-of rows.
2. **Type O88 routes once (closes L1 and L2).** Give them a grade sub-type `same_model_assumption`, and use it everywhere:
   - the flag, the amount kind and the E106 case (2);
   - the † count (E242);
   - the transfers-off set (E167);
   - the Assumptions bullet.

   Keep them ranked below user reports by the grade key, as O73 requires.
3. **State the verdict reason the test actually applies (closes L3).** Publish each cell's `largestLower`, `smallestUpper` and their ratio beside the status. A reader can then reproduce O86 without parsing a sentence.

## 3. Questions for the owner

- **Q1 (L2).** O88 says a SemiAnalysis figure for a model serves every effort of that model, as a same-model assumption. Should Claude Opus 5.5 (high) and (medium) be labelled that way too, with Opus 5.5's own figure as an O88 same-model assumption? Today they carry the "common Claude assumption" label of 2026-10-18. Values are unchanged either way. The answer decides whether the O88 label covers both providers or GPT only.

## 4. Verdict

One Medium and four Lows. The figure check exits 0, and the provenance, admission, route and figure tests pass.

The r129 changes to the draft match the data:
- O86 is stated as one formula;
- the cells are keyed by family;
- the ceilings have their own status, amount kind and selection reason;
- the counts in Output 1 match.

The Medium (M1) is that O88 reached the route data, the draft and the README, but not the registry's GPT rule text. That text renders into methodology.md and the site, and still gives GPT-6.1 Sol's other efforts the lower-of figure and omits GPT-6 Astra's. Nor did O88 reach AGENTS.md's GPT bullet, which now contradicts AGENTS.md's own O88 sentence.

Under O56 this round is not clean.

VERDICT: HAS FEEDBACK
