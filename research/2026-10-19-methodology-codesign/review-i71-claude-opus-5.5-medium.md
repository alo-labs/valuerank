# Internal review I71 — Claude Opus 5.5 (effort medium) on draft r130

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r130`
- Last line of the draft (line 174): the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r130 (seventieth internal review, the third at Opus 5.5 medium) carries O88 into the registry's GPT rule and AGENTS.md, gives the O88 rows their own flag and amount type (Opus 5.5's other efforts included), and states the O86 failure status as the formula. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "the formula. Every change is recorded with its rationale in the ledger."

What I read:
- `reviewer-prompt.md` and `ledger-brief.md`.
- `ledger.md` from "## Internal review I28" to the end: O45–O88, E247–E270, I29–I70 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` in full.
- `review-i70-claude-opus-5.5-medium.md`.
- `draft-r130.md`, every line (1–174), as a line-tagged copy folded at 1,500 characters (314 segments).
- The diff of `draft-r130.src.md` against `draft-r129.src.md`. It changes E242's † sentence, the Assumptions bullet, E106 case (1), the GPT routes bullet, E167's transfers-off set and the history entry. I also read the file list of the r130 commit (4559e61).

What I verified:
- **Checks and tests.**
  - `python3 -m valuerank.draft_figures check` exits 0.
  - These tests pass, run with bytecode and the pytest cache off: `tests/test_plan_reports_provenance.py`, `test_plan_admission.py`, `test_plan_routes.py`, `test_draft_figures.py`, `test_swe_tracks_selection.py` and `test_value_v3.py`.
  - `git status` was clean before I wrote this file.
- **O88 in the route data** (`data/plan_cost_routes.json`).
  - 33 routes carry `sameModelAcrossEfforts`, all labelled "same-model assumption (O88)":
    - GPT-6.1 Sol at four efforts;
    - GPT-6 Astra at two efforts;
    - Claude Opus 5.5 at xhigh, high and medium.
  - Each GPT-6 Luna effort still takes O45's lower-of figure (Plus 8.1).
  - `gptApplication` now states O88 (I70 M1 fixed). It renders into methodology.md line 163, and AGENTS.md's GPT bullet matches it.
  - `o72Application` states O86–O88. The ceiling derivation no longer carries a review label.
- **Plan rows** (`planRows` in `data/scores.json`).
  - Max-effort ranking, 27 rows: 10 owner-named transfers, 4 O46 ceilings, 11 controlled measurements and 2 API fallbacks.
  - AI Coding Daily ranking, 51 rows: 26 owner-named transfers, 18 O88 same-model rows, 4 ceilings and 3 fallbacks.
  - `diagnostics.rankSeparability.planAssumedRouteRows` holds 14 and 48 rows, so the 48 includes the 18 O88 rows.
  - The O88 rows carry the flag "same-model assumption across efforts (O88)" (`plan_routes.plan_cost`) and the amount kind "assumed API-equivalent consumption (same-model assumption across efforts, O88)" (`value_v3.AMOUNT_KINDS`).
- **Report cells** (`planAllowanceCells`). 52 cells and 28 listed; none passes. The Google AI Pro / Gemini 4 Argon cell reads "fails: largest lower bound 1.35× the smallest upper bound (O86 allows 1.20×)": 11.4 ÷ 8.47, with the provisional report included (I70 L3 fixed). The docstring and comment in `plan_admission.py` state the formula. `data/plan_reports.json` has 107 rows and 93 `notTabulated` entries. Both O71 research directories exist with their stage records.
- **Bars and counts.**
  - The headline bar setters are Gemini 4 Argon (high) at 63.54 in the max-effort ranking and MiMo-V2.6-Pro at 49.24 in the AI Coding Daily ranking, matching E201b.
  - The reach counts match bar currency's: 7/5/3 of 9 and 13/9/5 of 16, which agree with the ladder positions 2/4/6 for n = 9 and 3/7/11 for n = 16.
  - possibleQualifierN and confirmedQualifierN are 5/4 and 9/8.
  - The other counts check: 9 + 16 − 4 = 21 ranked at least once, 9 excluded, 21 and 14 listed, admission thresholds 6 and 11.
  - The lifecycle dates (2026-11-05, 2027-01-05, 2027-02-04 from 2026-10-06) check out.
- **The measured-only view.** `measuredOnlyPlanView` gives the official anchors' provenance. Today the low setters are owner-named transfers and the high setters API fallbacks.

Not verified: live web pages, the paywalled SemiAnalysis article and the Monte Carlo outputs.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. r130 made O88 a third kind of owner assumption, but several enumerations still name only "owner-named transfer" (and sometimes the O46 ceiling).**

r130 split O88 rows from owner-named transfers in the flags, the amount kind, the Assumptions bullet (line 58), E242 (line 16) and E167. The texts that count or describe the assumption set were not updated:

- **Line 15 (separability).** "the summary prints how many Plan rows rest on an owner-named transfer or the O46 quota ceiling, today 14 of 27 … and 48 of 51". The 48 is `planAssumedRouteRows`: 26 transfers + 18 O88 rows + 4 ceilings. So 18 of the rows the sentence counts carry a flag that says they are not owner-named transfers.
- **Published text, same class.**
  - README.md line 123 and the matching scores.md sentence print "for the 48 Plan rows on an owner assumption (an owner-named transfer or an O46 quota ceiling)" (`emit_docs.py` line 1398).
  - The † legend says "rests on an owner assumption (owner-named transfer or O46 quota ceiling)".
  - Yet README rows 106–111 print "same-model assumption (O88)" beside a † band.
- **Line 13 (Output 1).** "displayed arithmetic on owner-named transfers, the O46 quota ceilings, measured multiples … and API-cost fallback rows". This omits the O88 rows, which are 18 of the AI Coding Daily ranking's 51.
- **Line 16 (E242) and line 60 disagree on ceilings.** E242 now marks † for "an owner-named transfer or an O88 same-model assumption" and drops the O46 ceilings. The MiMo bullet (line 60) says the build counts ceiling rows "with the owner-named transfers among the Plan rows resting on an owner assumption (marked †, E242)". The build marks all three kinds.
- **Line 55 (change detection).** The Claude and GPT changes flag "the owner-named transfers from them (E144)". The O88 rows inherit the same flags: 44 flagged rows = 26 + 18.
- **Line 58 (E164).** The provenance list of the official anchor extremes is "controlled measurement / concordant reports / owner-named transfer / API-cost fallback". The code (`value_v3._plan_evidence`) maps every grade other than controlled or reports to "owner-named transfer". Today's anchor setters are true transfers and fallbacks, so nothing is mislabelled now. A ceiling or O88 setter would be.

Why Low: no score, rank, flag or stream membership changes. The build's sets are right; only the prose that names them is wrong. That matches how I70 L1 and L2 were rated.

What is new: these texts were correct before r130, because until r130 O88 rows were flagged "owner-named transfer". The relabelling made them wrong.

Change:
- Define "owner assumption" once: an owner-named transfer, an O88 same-model assumption or an O46 quota ceiling, the three kinds the build grades "assumption".
- Use that term in lines 13, 15, 55 and 60.
- Restore the ceilings to E242.
- Generate `emit_docs`' parenthetical and the † legend from the row flags.
- Make `_plan_evidence` return the row's own kind.

**L2. The draft's route rule still gives Claude Opus 5.5 (high) and (medium) the 2026-10-18 common Claude assumption. The data, the README and r130's own history say O88.**

- Line 59 says: "every other Claude row, including Claude Opus 5.5 (high) and (medium), takes Opus 5.5's figure per plan as the owner-named common Claude assumption (2026-10-18; AGENTS.md), labelled with its donor route".
- The nine Opus 5.5 routes at xhigh, high and medium are now `sameModelAcrossEfforts`, labelled "same-model assumption (O88)", with `assumptionScope` "owner-authorised same-model application across efforts (O88)".
- README rows 106–107 print that label.
- Line 58 defines O88 as "a model's own measured figure serving its other efforts", which covers Opus.
- The r130 history says "(Opus 5.5's other efforts included)".
- So line 58 and line 59 disagree within the specification. The precedence rule settles it (O88 is an owner decision).

The published rule texts have the same gap:
- The registry's `claudeApplication`, rendered as methodology.md's Claude bullet (line 164), does not mention O88 for Opus 5.5's other efforts.
- methodology.md's "Other models" bullet (line 166) lists the effort exceptions as "the explicit common GPT, Claude and MiMo assumptions", without O88.

Why Low and not Medium (unlike I70 M1): the multiple is the same either way (Opus 5.5's own 58.9 / 57.25 / 58.63). Both readings grade the route "assumption", mark it † and remove it in transfers-off. Only the label and the governing citation differ.

Change:
- In line 59, give Opus 5.5's other efforts their own clause: "Claude Opus 5.5's other efforts take Opus 5.5's own figure per plan as an O88 same-model assumption; every other Claude model takes it as the owner-named common Claude assumption (2026-10-18)".
- Add the same sentence to `claudeApplication`.
- Name O88 in the "Other models" exception list.

**L3. The E106 table, which "every route is classified once" by, no longer has a case that admits an O88 route.**

In r130, case (1) reads: "… without an owner-named transfer; … a controlled measurement serves its model's other efforts only as an O88 same-model assumption, graded "assumption", never as exact-route evidence) → not exact-route evidence, excluded".

- Case (2) admits only "owner-named transfer".
- r130 itself says an O88 route is not an owner-named transfer: it has a distinct flag, a distinct amount kind and a separate item in the Assumptions bullet.
- Read literally, an O88 route therefore lands in case (1), whose outcome is "excluded", or in no case at all.
- The build displays and ranks these 18 rows. O88, an owner decision, governs E106 under the precedence rule.

What is new against I70 L1, which the ledger records as adopted: under r129 the O88 route was arguably not "an effort not the configuration's" (a plan allowance is effort-invariant). r130's explicit split from "owner-named transfer", together with the case-(1) wording, now points the table to exclusion.

Change: case (2) should read "owner-named transfer or O88 same-model assumption → display-eligible only through its labelled assumption path, never identifies M_W". Case (1) should say that the same-model route is classified under case (2).

**L4. E166's and E168's enumerations do not list the build's O88 amount kind or derivation.**

- The r130 history says the O88 rows have "their own … amount type".
- E166 (line 152) still lists five amount kinds. `value_v3.AMOUNT_KINDS` has six; the new one is "assumed API-equivalent consumption (same-model assumption across efforts, O88)".
- E168's derivation list ("direct observation / solver projection / authorised assumption / valid multiplication") omits the ceiling's "quota ceiling: the tier's credits at the provider's API rate". The O88 derivation text ("authorised assumption: the same model's measured multiple …") fits the existing "authorised assumption" category.
- This is the same pattern I69 L3 fixed for the ceiling in E139 and E166.

Change: add the sixth kind to E166, and "quota ceiling" to E168's derivation list.

## 2. Methodology design recommendations

1. **One registered assumption taxonomy (closes L1–L4 at the source).**
   - Hold the three assumption kinds (`transfer`, `sameModel`, `ceiling`) in one code constant with their flag, amount kind, label and E106 case.
   - Derive from it `AMOUNT_KINDS`, the `plan_cost` flags, `_plan_evidence` and every published parenthetical ("an owner-named transfer, an O88 same-model assumption or an O46 quota ceiling").
   - Add a `draft_figures` figure, `assumptionKinds`, so the draft's enumerations render from it.
   - Then a fourth kind, should the owner add one, cannot leave stale lists behind. That is the E265 principle applied to categories rather than numbers.
2. **Publish the composition beside each assumption count.** Next to `planAssumedRouteRows`, publish counts per kind (today 10 / 0 / 4 and 26 / 18 / 4). A reader can then see that 18 of the AI Coding Daily ranking's assumed rows carry the model's own measured allowance, which is a stronger premise than a cross-model transfer. That matters when reading the E242 tolerance.

## 3. Questions for the owner

None. O88's wording ("a figure measured for a model serves every effort of that model") already covers Opus 5.5, and the ledger records that reading (I70 L2).

## 4. Verdict

There are no Critical, High or Medium findings, and four Lows. The figure check exits 0 and the listed tests pass.

r130 carried O88 into the registry's GPT rule and AGENTS.md (I70 M1), stated O86's formula in code and in the published status (I70 L3), and cleaned `o72Application` and the ceiling derivation (I70 L4).

The Lows all come from r130's new third assumption kind: the descriptive enumerations, the Opus 5.5 sentence, the E106 table and E166 still name only the earlier kinds. None changes a multiple, score, flag or stream.

Under O56 this round is clean, the first clean round at the Opus 5.5 medium rung (I68, I69 and I70 were not clean).

VERDICT: HAS FEEDBACK
