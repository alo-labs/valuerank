# Internal review I67 — Claude Opus 5.5 (effort low) on draft r126

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r126`
- Last line of the draft (line 174): the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r126 (sixty-sixth internal review, the first at Opus 5.5 low, and owner decision O84) splits every Kimi plan at a change detected on any of them, states that the route-to-cell check compares observers, and corrects two wordings. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "corrects two wordings. Every change is recorded with its rationale in the ledger."

What I read:
- `reviewer-prompt.md` and `ledger-brief.md`.
- `ledger.md` from "## Internal review I28" to the end, with close reading of O71–O84, E269–E270, the O71 outcome and the I60–I66 resolutions.
- `AGENTS.md` in full.
- `review-i66-claude-opus-5.5-low.md`.
- `draft-r126.md` in full, in five chunks (lines 1–39, 40–59, 60–84, 85–114 and 115–174).

What I verified:
- `python3 -m valuerank.draft_figures check` exits 0.
- `tests/test_plan_reports_provenance.py`, `tests/test_plan_admission.py` and `tests/test_draft_figures.py` pass, run with bytecode and cache off.
- `git status` was clean before I wrote this file.
- **Bars.** `barCurrency` reach counts (7/5/3 of 9 and 13/9/5 of 16) match the draft. So do the bar levels (63.5/53.3/64.9 and 49.2/38.0/58.6). The headline-bar setters are Gemini 4 Argon (high) in the max-effort ranking and MiMo-V2.6-Pro in the AI Coding Daily ranking. confirmed/possibleQualifierN is 4/5 and 8/9 (line 128).
- **Plan rows.**
  - `planRows`: 27 and 51 rows. API fallback: 2 and 3. Assumption grade: 14 and 48 (line 15).
  - The "possibly-superseded" flag is on 21 and 44 rows. The "valuation basis unverified" flag is on 25 and 48 rows (Output 1 and the limitations).
- **Quality weights.** The source shares 66/34 and 78/22 match the leaf table, and software engineering sums to 60 in both rankings. The exchange-rate pairs (3.04/4.06, 2.44/3.25, 2.83/3.77, 1.85/2.46) are consistent with ÷0.75.
- **Admission code and registry.**
  - `valuerank/plan_admission.py`: `evaluate` and `check_routes`. The I66 L2 change is present: the route is matched against any passing cell for its plan and model, and `admittingObservers` is sorted.
  - `partitionSplits` in `data/plan_cost_routes.json`: the Kimi entry cites O84. `o72Application` reads "O72-O84".
  - `planAllowanceCells`: 52 cells in each ranking, none passes. 24 cells read "not a listed plan".
  - I re-ran `plan_admission.evaluate` with every plan treated as listed and global. None of the 24 cells passes (the closest is Kimi Allegretto (legacy, CN), month: one firm report).

Not verified: live web pages, the paywalled SemiAnalysis article, the Monte Carlo outputs and the full test suite. I did not re-derive the cohort, the anchors or the MiMo ceilings, because r126 did not change their inputs.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. The cells marked "not a listed plan" are never tested, but the draft says the profile is applied to every cell and that another region's reports count for their own tier (line 55).**

What the draft says (line 55):
- "the build applies the profile below to every model × plan cell that has at least one report … publishes each cell's status".
- "a report on a tier of another region or currency (for example Kimi's China-region plans) counts only for that tier".

What the code does: in `plan_admission.evaluate`, a cell whose plan is not in `listedPlans`, or whose region is not "global", gets the status "not a listed plan". This happens before the O82 unit test, the firm-report count and the concordance test. Today that covers 24 of the 52 cells:
- every Kimi China-region cell (Allegretto, Allegro, Max, Plus, Pro, Ultra, the legacy plan and the ¥199 plan);
- Claude Team Premium;
- the tier-unstated Claude, Google, ChatGPT and MiniMax buckets;
- the legacy MiniMax Token Plans.

So a China-region tier can never admit a route, however many concordant reports it has. That contradicts the "counts only for that tier" sentence. The published status also hides the result the profile would give. It also leaves open whether O71 ("all such first-party plans") means only the plans the Plan ranking lists. The O71 research covered Team and China-region plans.

Why Low: I re-evaluated every such cell as listed and global, and none passes. No route, row or verdict changes today.

What is new: earlier rounds dealt with listed plans (I65 L3 kept "ChatGPT Pro 200 (grandfathered 20x)" listed). None of them dealt with the unlisted and non-global short-circuit.

Change (either):
- (a) Evaluate every cell and publish its profile status. Mark separately "no Plan row: plan not in the Plan ranking's listed plans (fee not registered)".
- (b) Say in line 55 that only listed global plans are evaluated, and narrow the regional sentence to match.

**L2. Output 1 cites E170 for the Plan rows' "unverified valuation basis", but E202's paragraph says no ranked row is unverified (lines 13 and 152).**

What the draft says:
- Output 1: "25 and 48 carry an unverified valuation basis (E170)". The limitations repeat this as the 25 and 48 flags.
- Line 152, under E202/E222: "Today no ranked row is in this state: every ranked row of both rankings is compatible as captured."

Both are true, but of different objects:
- The Plan flag is E138's status "basis not recorded: displayed with the flag 'valuation basis unverified'". It applies to the selected Plan measurement, and it is what `planRows[].flags` counts.
- Line 152's sentence concerns the AA cost basis under the E170 gate's outcome (4).

A reader comparing the two lines sees a contradiction, and a reviewer could read the Plan rows as E222 label-denied rows when they are not.

Change: in Output 1 and the limitations, cite "(E138: the selected Plan measurement's basis is not recorded)". In line 152, say "every ranked row's AA cost is compatible as captured".

**L3. The registry's `o72Application` header says "O72-O84", but its text never states O84.**

Its last clause is O83 ("a provider-documented change splits the partition too"). The Kimi rule appears only in the split's `basis`.

Change: append "a change detected on any Kimi plan splits every Kimi plan (O84)". Alternatively, end the header at O83.

## 2. Methodology design recommendations

1. **Give each cell two statuses (closes L1).** Keep `profileStatus`, the E270/O11/O82 result computed for every cell. Add `planRankingStatus`: listed with a fee, or not listed with the reason (tier unstated, region, team plan). Publishing the profile verdict for China-region and team plans makes O71's "all first-party plans" mandate auditable. It also means a future passing China-region cell shows up as a pass with no listed fee, rather than staying invisible.
2. **Give each flag one cited rule (closes L2).** Have `planRows[].flags` carry the rule ID that raised each flag (E138, E18/O77/O79, O13, O16). Generate Output 1's citations from those IDs, so a count and its rule tag cannot drift apart.
3. **Partition splits by plan, carried over from I66 recommendation 1 and only partly done.** The Kimi split now rests on O84. The four OpenAI announcement splits still carry no `plans` field, so they apply to every OpenAI plan by default. Making `plans` explicit, even where it lists every plan, would let the build check each split against its announcement's scope.

## 3. Questions for the owner

- **Q1 (L1).** Does O71's "all such first-party plans" include plans the Plan ranking does not list, such as Kimi's China-region tiers and Claude Team Premium?
  - If yes, should a passing cell on such a plan add a Plan row (which needs its fee registered), or only be published as evidence?
  - If no, the draft should say that only listed global plans are evaluated.

## 4. Verdict

No Critical, High or Medium finding; three Lows. The figure check exits 0, and the plan-admission, provenance and figure tests pass.

r126 implements O84 and the I66 changes as the ledger describes:
- the observer-only route-to-cell wording, and the any-passing-cell match;
- the dates;
- "most plan rows … possibly superseded or expired";
- "priced and dated".

The Low findings are:
- L1: a cell-evaluation short-circuit the draft does not describe;
- L2: a rule citation that reads as a contradiction;
- L3: a registry summary missing O84.

None changes a score, rank, label, cell status or gate outcome today. Under O56 this is a clean round.

VERDICT: NO FURTHER FEEDBACK
