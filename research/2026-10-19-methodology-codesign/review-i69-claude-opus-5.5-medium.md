# Internal review I69 — Claude Opus 5.5 (effort medium) on draft r128

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r128`
- Last line of the draft (line 174): the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r128 (sixty-eighth internal review, the first at Opus 5.5 medium, and owner decisions O86 and O87) replaces the whole-range concordance test with the common-value test, pools allowance reports across reasoning efforts, labels the O46 MiMo ceilings as ceilings valued at release prices, and corrects four wordings. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "four wordings. Every change is recorded with its rationale in the ledger."

What I read:
- `reviewer-prompt.md` and `ledger-brief.md`.
- `ledger.md` from "## Internal review I28" to the end. This covers O45–O87, E247–E270, I29–I68 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` in full.
- `review-i68-claude-opus-5.5-medium.md`.
- `draft-r128.md`, every line. I read it as a folded copy in 600-character segments (593 segments, lines 1–174). I also diffed it against r127, which shows changes to Output 1, E196, line 55 (O85 to O87) and the S1T list.

What I verified:
- **Checks and tests.**
  - `python3 -m valuerank.draft_figures check` exits 0.
  - `tests/test_plan_reports_provenance.py`, `tests/test_plan_admission.py` and `tests/test_draft_figures.py` pass. I ran them with bytecode and cache off.
  - `git status` was clean before I wrote this file.
- **Admission code.** I read `valuerank/plan_admission.py` in full (`model_of`, `cell_key`, `evaluate`, `check_routes`) and checked it against O86 and O87. I recomputed `planAllowanceCells` from `data/scores.json`: 52 cells, none passing.
  - The Google AI Pro / Gemini 4 Argon cell has two firm reports and one provisional report:
    - alpler: 8.47
    - faheem: 11.4–13.4
    - ansofteng: 7.84–9.04 (provisional)
  - It fails at 11.4 ÷ 8.47 = 1.35×.
  - `tests/test_plan_admission.py` lines 61 and 108 assert the 1.25× and 1.35× failures.
- **O87 and the route data.**
  - The configuration-map IDs as `model_of` maps them. It reads `qwen3.8-max` as `qwen3.8`.
  - The SemiAnalysis and common-assumption GPT and Claude routes in `data/plan_cost_routes.json`.
  - The MiMo ceiling routes and their plan rows in `scores.json` (`planRows`, `rows[].plan`, including the E166 `amount` object).
- **Rendered figures.**
  - Output 1 counts:
    - 21 of 27 and 44 of 51 plan rows, which is the plan rows less the API-fallback rows and the 4 ceiling rows per ranking.
    - 2 and 3 API-fallback rows.
  - Value-variance allocations:
    - max-effort: API cost 1.060 / quality −0.060; Plan cost 0.214.
    - AI Coding Daily: API cost −0.956; Plan cost −0.253.
    - These match "106% API and 21% Plan … −96% API and −25% Plan".
  - Exchange rates: 3.04 / 4.06 and 2.83 / 3.77.
  - Separable adjacent pairs: 0 of 8 and 1 of 15.
- **AA price record.** I checked AA's MiMo-V2.6-Pro price record in `data/aa/aa_v432_snapshot.json` (input 0.435, output 0.87, cache hit 0.0036 USD per million tokens).

Not verified: live web pages, the paywalled SemiAnalysis article, the Monte Carlo outputs and the full test suite.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. The draft states O86's concordance test in two forms that are not equivalent. On today's data the plain-language form admits a route that the formula and the build refuse.**

The definition (line 55): "a set of range-valued reports passes the margin when one value lies within it of every report's range, that is when the largest lower bound is at most 1.20× the smallest upper bound". AGENTS.md (Value scoring) gives only the first form: "Concordant means one value lies within 1.20× of every report's range (O86)". The docstring and the comment in `plan_admission.py` repeat both forms as if they were one.

The two forms differ:
- **"One value v lies within 1.20× of every range [Lᵢ, Uᵢ]"** means Lᵢ/1.2 ≤ v ≤ 1.2·Uᵢ for every i. Such a v exists exactly when max L ≤ **1.44** × min U.
- **The formula** that the code (`largest_lower > CONCORDANCE * smallest_upper`), the tests and the ledger's O86 entry use is max L ≤ **1.20** × min U. It says that some band [v, 1.2v] meets every range. It is not a common value within 1.20× of each range.
- The formula implies the plain-language form, but not the reverse. The "that is" is therefore false for every set whose ratio lies between 1.20 and 1.44.

This is not hypothetical:
- The one listed cell with two firm reports, Google AI Pro / Gemini 4 Argon, is at 1.35×.
- Under AGENTS.md's wording, v = 10 lies within 1.20× of all three ranges (8.47 → [7.06, 10.16]; 11.4–13.4 → [9.50, 16.08]; 7.84–9.04 → [6.53, 10.85]). The cell would pass with value √(8.47 × 12.4) ≈ $10.2 per week.
- That would give the API-fallback rows of Gemini 4 Argon (high), in both rankings, a report route on a listed plan.
- The build and the O86 ledger entry say this cell fails ("changes no verdict … fails at 1.35×").
- The test fixture at line 61 (point reports 100 and 125 fail at 1.25×) also passes under the plain-language reading, since v = 110 is within 1.20× of both.

The same paragraph group also keeps the pre-O86 statements without saying they are amended:
- E98 at line 53: "the largest report is at most 20% above the smallest; reports of 100 and 120 pass, 80 and 120 fail".
- E33 at line 53: "max_k x_k / min_k x_k ≤ 1.20 (boundary fixture: 100 and 120 pass, 100 and 120.001 fail)".

For point reports, E98 and E33 agree with the formula, but they contradict the plain-language O86 form (100 and 120.001 would pass under it). For range reports, E98 and E33 are the replaced whole-range test, and nothing marks them as amended.

Why Medium:
- This is the admission rule the owner made executable (O81).
- Its two published statements, one of them in AGENTS.md, give different verdicts on today's only contested cell.
- An agent following AGENTS.md, or a reader reproducing the cells from `plan_reports.json`, would publish a Gemini route that the build refuses.

What is new: O86 dates from 2026-10-28 and no review has examined its wording.

Change:
1. Ask the owner which reading O86 means (Q1). The record, the code and the tests all point to the 1.20 band.
2. If the band is meant, replace the gloss everywhere (draft line 55, AGENTS.md, the `plan_admission.py` docstring and comment, `site/data/plans.json`) with: "the reports concord when some interval spanning a factor of 1.20 meets every report's range, that is, when the largest lower bound is at most 1.20× the smallest upper bound; for point reports this is max ÷ min ≤ 1.20".
3. Cite O86 in E98 and E33 as the range-valued generalisation of their point tests.
4. Add a fixture between the two readings, for example points 100 and 125: they fail under the band and would pass under the common-value-within-1.20× reading.

### Low

**L1. O87 is written in at one place (E270), but three rules that it overrides still state effort-exact report evidence without a note.**

Where the text still says effort-exact:
- E107 (line 53): "a report that does not name the exact model and effort … is excluded from every model route".
- The route key (line 51): "… × model × effort".
- The E106 decision table, case (1) (line 58): "execution-identity incompatibility (effort, surface or model version not the configuration's, without an owner-named transfer) → not exact-route evidence, excluded".

How it resolves: O87 says it amends "E107's report set and the route key". It does not name E106. Under the precedence preamble an owner decision governs, so the outcome is decided. But a reader who applies E106 case (1) to a pooled report route for GPT-6 Astra (high) built from reports at "high, low, ultra" would exclude it. The engine also has a `requiredVariant` effort gate in `route_candidates`. No report route sets it today.

Change:
- Annotate each of the three passages in place, for example "(for report evidence, any effort of the model, O87)".
- Name E106 case (1) in the O87 sentence.

**L2. The O87 model key is a regex, and it misreads a real model name.**

What the code does:
- `model_of` strips a trailing `-(low|medium|high|xhigh|max)` from a configuration ID.
- In `data/v3_configuration_map.json`, `qwen3.8-max` (Qwen3.8 Max, a model name, not an effort) maps to `qwen3.8`.
- The regex also omits `minimal`, which is one of AA's efforts under E267.

Why Low: Qwen is not in the cohort, so nothing changes today. Still, O87 defines the key as "the model", and the specification already has a model identity: E193's family, which is AA's model identity and is checked against the catalog display name.

A related point: each published cell's `modelId` is a configuration ID string. For example, `gemini-4-argon` is the ID of Gemini 4 Argon (high), yet its cell pools low, medium and high reports. I68 M1 asked for model-level cells not to carry a configuration's ID. The ledger's O87 entry does not say whether that was declined.

Change:
- Key cells by the E193 family (or a model field in the configuration map), and fail the build when a report's model has no family.
- Publish the key as `model` (the family name), not as a configuration ID.

**L3. I68 L2 is adopted in the flags, but the ceiling rows still publish "owner-named transfer" and "observed" wording in other fields.**

The ledger says the ceilings "no longer carry … the 'owner-named transfer' flag". The flags are now right. Other published fields of the same rows still use the old wording (for example `rows[].plan` for MiMo-V2.6-Pro in the max-effort ranking):
- E166's `amount.amountKind` is "assumed API-equivalent consumption (owner-named transfer)".
- `amount.derivation` is "authorised assumption: the donor's multiple times this route's cash", with `donorRouteId: null`.
- `amount.interpretationLabel` repeats "owner-named transfer".
- `selectionReason` reads "larger observed multiple (observed-workload multiple — target-workload ordering not identified)", although nothing was observed.

The draft has a matching gap in its enumerations:
- E139's capacity statuses (line 53) do not include the new ceiling status.
- E166's `amount_kind` list (line 152) does not include a ceiling kind.

I68 raised the E166 amount. What is new is that its adoption left these fields unchanged.

Change:
- Add an amount kind "provider-derived quota ceiling (O46)" with derivation "credits × recorded rate".
- Give the ceiling routes a selection reason without "observed".
- Add both statuses to the draft's E139 and E166 lists.

**L4. O87's premise is applied to report evidence but not to the controlled measurement of the same model, so one model's other efforts receive a different, lower multiple.**

O87 is an owner decision, so this is not a defect; I label it Low and put it to the owner as Q2.

O87 rests on "a plan's allowance is the same dollars at any effort". E246 and O45 still treat other efforts of a measured model as an assumption:
- **Claude:** Claude Opus 5.5 (high) and (medium) take Opus 5.5's own figure. It is graded "assumption", marked †, and dropped in the transfers-off streams.
- **GPT:** other efforts of GPT-6 Astra and GPT-6.1 Sol take the lower of the two models' figures, not their own model's. Today:
  - GPT-6 Astra (high) takes 10.42 on Pro 200 against Astra's measured 14.485, 28% lower.
  - It takes 10.55 on Pro 100 against 13.22.
  - GPT-6.1 Sol (medium) takes 8.1 on Plus against Sol's 10.55.

The result:
- Two concordant reports of Astra at any effort would serve Astra (high) as measured evidence.
- SemiAnalysis's controlled measurement of Astra serves it only as a lower-of assumption from another model.

What is new: O87 postdates E246 and O45, and its stated premise bears directly on them.

Change: none without the owner (Q2). If the owner extends the premise, the GPT lower-of rule would apply only across models, and same-model other-effort rows would be labelled "same model, other effort (O87 premise)" instead of a transfer.

## 2. Methodology design recommendations

1. **State O86 once, exactly, and test the boundary (closes M1).**
   - Use one sentence: "some interval spanning a factor of 1.20 meets every report's range (max L ≤ 1.20 · min U)".
   - Add a property test in `tests/test_plan_admission.py` that brute-forces the definition on random range sets and compares it with the closed form. This catches any future gloss or code that drifts to the 1.44 reading.
   - Cite O86 in E98 and E33.
2. **Derive the allowance-cell key from the model identity, not from the ID string (closes L2).** Read the family or model from the configuration map (E193), publish it as `model`, and have `check_routes` map a route's configuration through the same table. A new model named "…-max" or "…-high" then cannot merge with or split from another model.
3. **Finish the ceiling typing (closes L3).** Give O46 ceilings their own E166 amount kind, derivation and interpretation label, and a selection reason that names the larger ceiling, not an "observed" multiple. Optionally, have the build join the ceiling's recorded rate and capture date (`usdPerBillionCredits`, `capturedOn`) against the price record in force at V. Today "valuation basis: release" is an editorial field, not an E170 join outcome.
4. **If the owner extends O87's premise (Q2):** regrade same-model other-effort routes from controlled measurements as "same model, other effort". Keep them out of the transfers-off streams only if the owner wants them treated as assumptions. Keep O45's lower-of rule for cross-model GPT rows alone.

## 3. Questions for the owner

- **Q1 (M1).** O86 says reports concord when "one value lies within 1.20× of every report's range". Does that mean that some 20% band touches every report's range (largest lower bound ≤ 1.20 × smallest upper bound, as the ledger, the build and the tests apply it)? Or does it mean that one value is within a factor 1.20 of each range on either side (largest lower bound ≤ 1.44 × smallest upper bound)? Under the second reading, Gemini 4 Argon on Google AI Pro passes today (1.35×) and replaces its API fallback with a report route of about $10.2 per week.
- **Q2 (L4).** O87 holds that a plan allowance is the same dollars at any reasoning effort. Should that premise also let a SemiAnalysis measurement serve its own model's other efforts as the same model's evidence? Under that reading:
  - Claude Opus 5.5 (high) and (medium) would carry Opus 5.5's figure as "same model, other effort", not as the common Claude assumption.
  - GPT-6 Astra and GPT-6.1 Sol's other efforts would take their own model's figure instead of the lower of the two (for example 14.485 instead of 10.42 for GPT-6 Astra (high) on Pro 200).
  - Or does E246/O45's max-only binding stay for controlled measurements?

## 4. Verdict

One Medium and four Lows. The figure check exits 0, and the provenance, admission and figure tests pass.

Every rendered figure I checked matches `data/scores.json`:
- Output 1's plan-row counts and the allocations in the E196 clause;
- the exchange rates and the separability counts.

r128 implements O87's effort-pooled cells and the I68 changes in the build, apart from the E166 amount labels on the ceiling rows (L3).

The Medium (M1) is that O86's concordance rule is stated in two inequivalent forms, the 1.20 band and a common value within 1.20× of each range. The draft equates them with "that is", and AGENTS.md gives only the looser form. On today's data the looser form admits the Google AI Pro / Gemini 4 Argon cell that the build refuses.

Under O56 this round is not clean.

VERDICT: HAS FEEDBACK
