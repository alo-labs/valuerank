# Internal review I68 — Claude Opus 5.5 (effort medium) on draft r127

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r127`
- Last line of the draft (line 174): the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r127 (sixty-seventh internal review, the second clean one at Opus 5.5 low, and owner decision O85) tests report cells on unlisted plans as evidence only and separates the Plan measurement's valuation status (E138) from the AA cost's (E170). Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "cost's (E170). Every change is recorded with its rationale in the ledger."

What I read:
- `reviewer-prompt.md` and `ledger-brief.md`.
- `ledger.md` from "## Internal review I28" to the end. This covers O45–O85, E247–E270, I29–I67 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md` in full.
- `review-i67-claude-opus-5.5-low.md`.
- `draft-r127.md`, every line. I read it in a folded copy, 400-character segments, lines 1–174. I also diffed it against r126 and checked the hand-typed "today" sentences in `draft-r127.src.md`.

What I verified:
- **Checks and tests.** `python3 -m valuerank.draft_figures check` exits 0. `tests/test_plan_reports_provenance.py`, `tests/test_plan_admission.py` and `tests/test_draft_figures.py` pass, run with bytecode and cache off. `git status` was clean before I wrote this file.
- **Cohort.** I recomputed the near set from `data/aa_frontier_capture.json` with the F(c) rule and rounded tooltips. It gives 11 near points, identical to the capture's list, so the cohort is 30. GPT-6 Astra (high) is the near primary by the cost tie-break. The first vertex is $10.63, which is also the cheapest of 190 points.
- **Max-effort rows.** There are 9, one per family. MiMo-V2.6-Pro is the only subset row. The Coding Agent Index is priced for 8 of the 9, against a threshold of 6. There are 255 and 127 feasible alternatives. ITBench is 2 of 9 and 0 of 16.
- **Bars.**
  - Ladders: 53.27 / 63.54 / 64.94 and 38.00 / 49.24 / 58.61, at zero-based positions 2/4/6 and 3/7/11.
  - Reach counts: 7/5/3 and 13/9/5. confirmed/possibleQualifierN is 4/5 and 8/9.
  - E205 family-primary headline bars: 63.5 and 52.8. I recomputed both from the primaries. GPT-6 Astra (max) is correctly not a primary after O65.
- **Exchange rates and allocations.** The exchange rates match ÷0.75. The value-variance allocations are max-effort API cost 106% / quality −6%, max-effort Plan 21%, AI Coding Daily API −96% and Plan −25%.
- **Plan rows.**
  - Max-effort: 27 rows, of which 2 are API fallback, 14 assumption, 11 controlled, 21 possibly superseded and 25 "valuation basis unverified".
  - AI Coding Daily: 51 rows, of which 3 are API fallback, 48 assumption, 44 possibly superseded and 48 unverified.
  - The O46 ceilings recompute from credits × rate ÷ fee.
- **Admission code.** `valuerank/plan_admission.py` (`evaluate`, `check_routes`) matches E270, O82, O83 and O85 as worded, except for the point in M1. It gives 52 cells, 24 of them unlisted, and none passes.
- **Source clocks.** Vals, LiveBench, AI Coding Daily and Bug Hunt were captured at 2026-10-25T10:44:11Z from boards updated before the cutoff day. The O69 bound for the Kimi K3.1 Pro row is 01:14:11Z (read at 10:44:11Z, "10 hours ago"). `select_aicd` (E268) matches the draft.
- **O71 records.** I read the decision record of `research/2026-10-25-plan-allowances-sb-deep-research/` and the per-cell report table `data/plan_reports.json`.

Not verified: live web pages, the paywalled SemiAnalysis article, the Monte Carlo outputs and the full test suite.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. The report cells pool efforts and file the reports under another configuration's ID. This contradicts E107, the route key and E246, and it moves allowance evidence across efforts.**

What the draft says:
- E107 (line 53): "a report that does not name the exact model and effort, or mixes models, is excluded from every model route and kept only as a provider- and plan-level diagnostic, as AGENTS.md requires".
- Line 53 also sets the route key: "plan × limit-schema version × purchase cohort × surface × model × effort".
- E246 (line 59): a SemiAnalysis figure that names no effort binds to the model's max row "and to no other effort".
- E270 (line 55): a report counts when it "names the exact model and tier". No effort test.

What the code and data do:
- `valuerank/plan_admission.py` never reads a report's effort. It keys each cell by (provider, plan, `modelId`, unit, region).
- `data/plan_reports.json` gives every report a `modelId` equal to the ID of the model's unsuffixed configuration, whatever effort the observer stated:
  - `gpt-6.1-sol` is GPT-6.1 Sol (max). It holds reports at medium/low, medium, high and xhigh.
  - `gpt-6-astra` is GPT-6 Astra (max). It holds reports at high, medium, low, "ultra" and "max+medium".
  - `claude-opus-5-5` is Claude Opus 5.5 (max). It holds reports at medium, high, xhigh and high/xhigh, plus 28 reports with no effort.
  - `gemini-4-argon` is Gemini 4 Argon (high). It holds reports at low, medium and high.
- The O71 research decided this pooling on purpose. Its decision record rejected splitting Gemini 4 Argon on AI Pro by effort because "Effort is not a quota-schema change". No ledger entry reconciles that choice with E107.

What this does today:
- The published `planAllowanceCells` attribute the reports to configurations that were not measured. The "GPT-6 Astra on Pro $100" cell, the third-closest O71 cell, holds two high-effort reports (sentrybottale and mrak-) under the ID of GPT-6 Astra (max). GPT-6 Astra (high), the configuration actually measured, has no cell.
- The "closest" Claude Pro cell pairs a high/xhigh report (NTRYourWaifu, $321) with a medium report (kanzakichiya, $302). Under E107 these are two different routes.
- The Gemini cell fails because of a low-effort report against a high-effort configuration.

What this does when a cell passes: `check_routes` would accept a report route for the max row built from other efforts' reports. This is the cross-effort transfer that the fixed exact-variant policy forbids. Meanwhile a route for the configuration actually measured (for example `gpt-6-astra-high` or `gpt-6.1-sol-medium`) could never pass, because no cell is keyed to it.

The draft's own precedence paragraph calls an unamended conflict between two editor rules a defect to be corrected in the next revision.

Why Medium and not Low: this is a normative contradiction in the admission path that the owner made executable (O81). It touches a fixed policy (exact-variant evidence). It also misattributes the published cell evidence today, although no verdict changes because no cell passes.

What is new: no ledger entry has raised it. I61 recommendation 4 mentioned the low-effort Gemini report only as an outlier.

Change: decide one reading (Q1) and make the draft, the table and the code agree.
- (a) **Effort-exact.** Key cells by configuration ID, including effort. Keep reports with no stated or mixed effort as model-level diagnostics (E107). `check_routes` then matches routes by configuration.
- (b) **Effort-pooled.** Declare that an allowance in API-priced dollars is a property of the model and plan. Name the configurations a passing model-level cell may serve, labelled as an owner rule like the 2026-10-18 Claude transfer. Amend E107, the route key and E270 to say so.

Either way, rename the cell IDs so a model-level cell is not published under a configuration's ID.

### Low

**L1. The O85 insertion broke the line 55 sentence, and "listed Plan-ranking plan" is not what the build means by "listed".**

The grammar:
- The sentence now reads "…a cell on a plan the Plan ranking does not list (…) is tested the same way and published as evidence only, supporting no route (owner decision O85, 2026-10-28), and refuses a report route for a cohort model that no passing cell supports."
- The subject of "refuses" has become "a cell". In r126 it was "the build".

The definition:
- The build treats a plan as listed when it is in `data/plan_reports.json` `listedPlans`, a plan with a registered fee. That set includes Google AI Pro and Ultra, the four Kimi global tiers and the three MiniMax tiers.
- The Plan ranking has no row on any of those plans: Gemini 4 Argon (high) and Kimi K3.1 Pro are API-fallback rows.
- So a reader who takes the draft's wording literally would treat Google AI Pro as unlisted.

Change: restore "the build" as the subject of "refuses". Define a listed plan as "a first-party plan whose fee is registered for the Plan ranking (`listedPlans`), whether or not a route is selected on it today".

**L2. The O46 ceiling rows carry two flags that misdescribe them, and Output 1 counts them as "Plan measurements".**

Each of the 4 MiMo-V2.6-Pro ceiling rows in each ranking is flagged as follows:
- "observed-usage multiple; full utilisation not established". `plan_routes.plan_cost` adds this flag for any status other than "capacity established", and a ceiling gets "saturation unverified". But nothing was observed, and a ceiling is by construction the full-quota (upper-bound) value. The route note itself says "A subscriber can realise at most this".
- "valuation basis unverified". Output 1 (line 15) counts these rows among the "25 and 48 [that] carry a Plan measurement whose valuation basis is not recorded (E138)". A ceiling is not a measurement. Its basis, Xiaomi's overseas API rate as read on 2026-10-23, is recorded on the route (`usdPerBillionCredits`, `capturedOn`).

The E166 amount on these rows also reads "the donor's multiple times this route's cash", with no donor.

What is new: I48 L5 recorded the "transfer" grade label and I64 noted that no route records a `valuationBasis`. Neither raised the capacity flag or the "measurement" wording.

Change:
- Give O46 ceilings their own capacity status, "provider-derived quota ceiling (not a measurement)".
- Record their valuation basis as the captured Xiaomi rate, or say in Output 1 "carry a Plan multiple whose valuation basis is not recorded (E138; for the O46 ceilings, not reconciled to AA's prices)".

**L3. The E196 "today" clause omits the max-effort ranking's above-100% allocation (line 20).**

The rule covers "a negative allocation (or one above 100%…)", but the example names only the AI Coding Daily ranking (−96% API, −25% Plan).

Today the max-effort API allocation is 106% to cost and −6% to quality (`costInfluence.api.commonWorkload.varianceAllocation`). This is the same case, with quality's term the negative one, and it is on the leading ranking.

The clause is true but chosen by hand.

Change: generate the list of every ranking and basis whose allocation lies outside [0, 1].

**L4. The S1T list still calls LiveBench 2.0 Overall "the mean of its seven categories" (line 98).**

Line 88 (E264 as amended by O67) and methodology.md both describe the weighted formula. I58 M4 required every LiveBench description to say "weighted". This sentence is the one left.

Change: "the weighted mean of its seven category shares, with the release's weights (O67)".

**L5. `valuerank/plan_routes.py` defines `CONTROLLED_KINDS` twice (lines 39 and 294).**

The second definition drops `"controlled_measurement"`. Because Python reads the global at call time, `evidence_grade` (line 125) and `measurement_capacity_status` (line 208) use the narrower set.

A route of kind `controlled_measurement` would therefore not grade as controlled, would not count as having established capacity, and would fall outside the E220 allocation-regime check.

Why Low: no route uses that kind today.

Change: keep one definition, or rename the E220 set.

## 2. Methodology design recommendations

1. **Effort-keyed allowance cells (closes M1 under reading (a)).**
   - Cell key = (provider, plan, configuration ID including effort, unit, region).
   - Add a model-level diagnostic cell, (provider, plan, model, unit), that holds every report including no-effort and mixed-effort ones. Publish it with the label "model-level; not a configuration route".
   - If the owner prefers reading (b), publish both cells. The configuration cell admits; the model-level cell shows how far pooling would change the verdict.
2. **Show the post-change evidence beside each "possibly-superseded" flag.** For each controlled route flagged by a detected change, publish the in-window reports for the same plan and model dated after the split: count, range, and implied multiple against the selected one. This is diagnostic only and changes no precedence (O73, O78).
   - Today the one non-provisional post-split Claude Max 20x report (NicoAica, $182–212/week, about 4× a month) sits beside a selected Opus 5.5 Max 20x multiple of about 59×.
   - The only post-split Claude Pro report (K45SLE, $210–300/week, provisional) is consistent with the selected Pro figure.
   - A reader now sees only the flag, not whether the flagged multiple is contradicted or confirmed.
3. **Typed flags for the O46 ceilings (closes L2).** Give the ceilings their own capacity status, valuation-basis record and E166 amount kind ("provider-derived quota ceiling"), so that no published string calls them transfers, observations or measurements.
4. **Generate the hand-chosen examples (closes L3).** Two "today" examples are true but pick their subject by hand: the E196 allocation clause, and the rankings named in some flag sentences. Render the subject from the data, as E265 does for figures.

## 3. Questions for the owner

- **Q1 (M1).** O71 asks for two user reports "for the exact model and tier". Does "exact model" mean the configuration at its stated effort, as E107 and the route key say? Or does it mean the model across efforts, treating an allowance in API-priced dollars as effort-invariant, as the O71 research applied it?
  - If across efforts: which configurations may a route from a passing model-level cell serve? Every effort of the model, labelled as an owner assumption? Or only the configuration whose effort the reports name?

## 4. Verdict

One Medium and five Lows. The figure check exits 0, and the provenance, admission and figure tests pass.

Every rendered figure I checked matches `data/scores.json` and my recomputations:
- the cohort, the bars and the reach counts;
- the plan-row counts, the allocations and the exchange rates;
- the O46 ceilings, the source clocks and the O69 bound.

r127 implements O85 and the I67 changes as recorded.

The Medium (M1) is a contradiction between E107/E246 and E270/`plan_admission` over whether allowance reports are effort-exact. Today it misattributes the published cell evidence. Once a cell passes, it would admit cross-effort evidence to the max configuration.

Under O56 this round is not clean.

VERDICT: HAS FEEDBACK
