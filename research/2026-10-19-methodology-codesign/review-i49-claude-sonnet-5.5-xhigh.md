# Internal review I49 — Claude Sonnet 5.5 (effort xhigh) on draft r107

## 0. Read check

- First line of the draft (folded copy, line 1): `# ValueRank methodology — draft r107`
- Last line (folded line 963): `ranking, prints the AI Coding Daily ranking's displayed record, companions, separability and indicative values in scores.md, and corrects the sign explanation for allocations above 100%. Every change is recorded with its rationale in the ledger.`
- Last 12 words of the last paragraph: "above 100%. Every change is recorded with its rationale in the ledger."
- Read in full: `reviewer-prompt.md`, the whole folded draft (963 lines, in chunks), `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (line 1428), and the repository-root `AGENTS.md` (40 lines, current copy; I judged the draft against it, not an older one).
- Opened to check rules and figures: `data/scores.json` (both rankings), `data/aa_frontier_capture.json`, `data/plan_cost_routes.json`, `data/leaf_evidence.json`, `data/swe_tracks.json`, `data/tb4.json`, `research/.../open-web-discovery-2026-10-23.json`, `research/.../draft-r107.src.md` (placeholders), `valuerank/emit_docs.py`, `valuerank/value_v3.py` (bands, source clocks, open-web check), `valuerank/draft_figures.py`, and the generated `README.md`, `scores.md`, `methodology.md`, `raw-data.md`. `python3 -m valuerank.draft_figures check` exits 0.
- Re-derived from data and found correct: the cohort (29 = 18 frontier + 11 near; 7 + 5 = 12 families; 189 plotted points; the first vertex GPT-6 Luna (low) $10.63 equals the cheapest plotted point; every near gap), the two bar ladders (54.23 / 64.26 / 65.00 at zero-based positions 2, 4, 6 of 9; 38.0 / 49.2 / 57.2 at 3, 7, 10 of 15), bar reach (7, 5, 3 and 12, 8, 5), qualifier counts (4 against 5, 7 against 8), the plan-row counts (27 and 50) and assumed-route counts (14 and 48) by a route census, the admission arithmetic (⌈2N/3⌉ = 6 and 10; 255 and 127 feasible alternatives), the exchange rates from the anchor ratios (3.04 / 4.06 and 2.44 / 3.25), one full quality composite (Claude Opus 5.5 (max) 67.91 against 67.92 published) and value (0.25 × 12.17 + 0.75 × 67.92 = 53.98), the retained-weight figures of every deletion branch, the lifecycle dates (2026-11-05, 2027-01-05, 2027-02-04), the E77 closed-form endpoints, the 70%-coverage fixture (91.5% uniform, 86.7% arcsine; Monte Carlo), the Omniscience vectors, and the admission fixtures.
- Stale or wrong current figures in the draft: none found. Every figure I tested resolves to the right field. The one wrong published figure below (M1) is in `scores.md`, which the draft cites but does not quote, so it is a defect in the emitter, not in a placeholder and not in the draft check (the check never reads the generated documents).

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

**M1. The E227 "harness by leaf" line is published for the wrong population, and omits the one leaf whose harness varies per model.**
- Where: draft, Normative "Harness stress branch (E19, premise corrected by E227)" (folded lines 752–755); published in `scores.md` "Diagnostics" (line 1100) and "AI Coding Daily ranking: diagnostics" (line 626).
- Issue: the draft says each release publishes "how many cohort rows each agent or harness scores on, per leaf", and "cohort rows" is per ranking (Counts, defined once). Both rankings print the same Bug Hunt counts, "Codex CLI 10, Claude Code 7, Antigravity CLI 1, Claude Code / Anthropic-compatible shim 1, DeepSeek Harness / DeepSeek API 1" (total 20), beside "Terminal-Bench: mini-SWE-agent 9" (max-effort, 9 rows) and "15" (AI Coding Daily, 15 rows). "Codex CLI 10" cannot be right for a nine-row ranking. Recomputed from `scores.json` over each ranking's own rows: max-effort Claude Code 3, Codex CLI 3, DeepSeek Harness 1, Antigravity CLI 1, shim 1 (9); AI Coding Daily Codex CLI 8, Claude Code 4, shim 1, Antigravity 1, DeepSeek Harness 1 (15). Cause: `emit_docs.harness_by_leaf_text` takes Terminal-Bench from the ranking's rows but loops over `facts.scores["models"]` filtered by `rankingEligible` (the 20 configurations ranked in either ranking) for Bug Hunt. Second defect on the same line: the AI Coding Daily ranking's line lists no AI Coding Daily harness, although that leaf is the one the draft says varies per model ("named on each record"). It cannot be produced as drafted: `swe_tracks.json` holds the per-record harness only in free text (`note`: "Tested 2026-10-08 with Claude Code"), and `rows[].quality.leaves.aiCodingDaily.harness` carries the generic string "varies by model: Claude Code, Codex CLI, OpenCode, Devin, DeepSeek's harness".
- Why it hurts: this is the only published disclosure of the harness mix behind the model-plus-harness leaves (E19, E29). A reader of the max-effort ranking is told nine rows ran Bug Hunt on ten Codex CLI runs; the AI Coding Daily harness mix is not disclosed at all.
- Change: count every leaf over the ranking's own rows (a test that each count line sums to at most the ranking's row count); parse the AI Coding Daily harness into a structured per-record field in `swe_tracks.json` and print it; add Vals and LiveBench as "one harness for every model" so every leaf of the ranking has a line.

**M2. The draft still promises output that the cited document does not carry (the I47 M1 / I48 M1 class). The I48 check resolves `scores.json` field names, not what the named document prints.**
- (a) Clear defect. Output 1, noise-band bullet (folded 38–40): "Each release's bands are printed beside the ranks (README.md for the leading ranking, scores.md for the other; …)". `README.md` prints the "Noise band (Plan / API)" column for both rankings (max-effort table, every-plan table, AI Coding Daily table). `scores.md` prints no band column for either ranking, and its AI Coding Daily noise paragraph (line 144) still says "The noise band column groups each row …" with no such column beside it. Change the pointer to README.md for both rankings, or print the column in scores.md (the dangling sentence is then true).
- (b) Cost, token mix (folded 268–269): "Each selected route's mix status is printed with it (scores.md; …)". The scores.md "Plan route selection" table has no mix-status column; only a per-status count line in Diagnostics ("1 selected routes: mix not reported …; 6 selected routes: mix unidentified …"). The per-route status is in `rows[].plan.mixCheck` only.
- (c) Cost capture status (folded 176–177): the Coding Agent Index "task-equivalents and attempts beside the 290 required are diagnostics, raw-data.md and scores.json `rows[].cost.componentsDetail`". `raw-data.md` prints "—" for the Coding Agent Index tasks and no task-equivalents or attempts; they are only in `scores.json` (`componentsDetail.coding-agent-index.detail`).
- (d) Output 3 and the Cohort frontier-families bullet (folded 59–60, 134–135): "the (published) summary names the frontier-families bar (E199) beside the headline bar". README does not mention it; scores.md prints it as a diagnostics line (618, 1092), not beside the headline bar.
- (e) Claim contract (folded 721–726): E51 says the displayed wording is "confirmed within the declared evidence set", and E38 that every frontier and bar result states whether it "extends to the selected cohort … otherwise 'not established'". The generated summary says "(confirmed)", and no emitter or `scores.json` field produces an extension statement (no match for "extends" or "extension" in `valuerank/` or `scores.json`). The ledger treats the "Not evaluable on this workload: …" clause as E38's omitted-competitor list, but that clause is not attached to the bar claims: the max-effort README says "Cheapest at or above quality 54.2: GPT-6.1 Sol (max) (confirmed)" while two ranked rows that reach 54.2 cost less per basket run on their own workload (MiMo-V2.6-Pro $136.13, DeepSeek V4.1 Flash 1017 (max) $324.12, against $1,233.11).
- Why it hurts: the draft is the specification of what the published pages say. Two faithful implementers fix (a) in opposite directions (edit the pages, or edit the draft). The owner's E265 instruction was to remove this recurring class at its source; the field-name check cannot see (a)–(e).
- Severity: Medium on the ledger's precedent (I47 M1 and I48 M1 were Medium for the same reason). Only (a) is plainly false; (b)–(e) are lesser instances of the same gap and can be settled in the same pass.
- Change: see recommendation 1 (a pointer manifest that the check verifies against the documents), and correct (a)–(e) as recommended there.

**Low**

**L1. Misquotation of AGENTS.md (folded 242–243).** The draft says "v3's AGENTS.md says 'the selected subscription route'". The current AGENTS.md has no such phrase (it was removed in the O45–O48 amendment; it now reads "a subscription route's Value Multiple … the route on each plan chosen by the official comparator"). I48 L1 waited for "the next AGENTS.md amendment", which has already happened. A misquote of the binding file invites doubt about the comparator's authority. Quote the current sentence.

**L2. "Evidence rules unchanged (no provider marketing quotas; …)" (folded 326) contradicts the MiMo quota ceilings (O46).** AGENTS.md makes O46 an explicit exception to the numerator rule, and the draft says so in the next bullet. The first sentence, read alone, forbids what the second adopts. Add "except the O46 quota ceilings".

**L3. O59 and O60 name six sources, not the closed set AGENTS.md states (folded 837–840).** AGENTS.md: "Every non-AA quality source". The draft's parenthetical lists the Vals boards, LiveBench, AI Coding Daily, Bug Hunt, tbench.ai and Cognition; the third source in the leaf order, a model provider's published result, has no capture clock. No row uses one today (the draft says so at the provider-claimed-leaf bullet), so no score is affected; say whether a provider document carries a clock before the first one is admitted.

**L4. "Epoch MirrorCode (3 configurations at O53)" (folded 434).** The MirrorCode coverage (3) came from the O55 follow-up; the "3 of 29" at O53 is Surge's Complex Constraints. Cite O55's follow-up.

**L5. Single-leaf sources (folded 585–586).** "a single-leaf source (Bug Hunt Bench; AI Coding Daily in its ranking) coincides with its leaf's branch" omits LiveBench 2.0 Overall, which the previous sentence calls a single-leaf source since O61. Add it.

**L6. The explanation of a plan-row band straddle does not describe today's straddlers (folded 38–39).** The draft says a configuration's later plan row can fall in the next band "when a row of another configuration started that band (today GPT-6 Astra (max) … and GPT-6.1 Sol (medium) …)". In `diagnostics.rankSeparability.plan.bands` the later band is started by the straddling configuration's own row in both cases: max-effort Astra (max) on ChatGPT Plus (56.78) is alone in band 21–21 (separable from Haiku's 59.83, the first row of band 11–20: a gap of 3.05 against a median threshold of 2.87); AI Coding Daily Sol (medium) on ChatGPT Pro 100 opens band 12–24, 0.06 below its own Pro 500 row, which sits in band 1–11. The same-configuration exception tests only the band's first row (`value_v3._separable`), so the real condition is "a later plan row separable from the first row of the band that holds its earlier rows". State that condition; it also shows the band edge can split two rows of one configuration that are 0.06 apart.

**L7. Stale labels in data and generated pages that the draft's own statements contradict.**
- `value_v3.SOURCE_DATES` (line 386) and `scores.json` `sourceDates` still label LiveBench 2.0 "retired quality source (O26)" with `observedOn` 2026-10-20, while O61 made LiveBench 2.0 Overall a 15% leaf and the draft says the registry pins the dates "with the capture date" (captured 2026-10-23T07:58:31Z).
- `raw-data.md` line 488: "(13 of 51 cohort matches)"; 51 is the roster-row count in `data/tb4.json`, not the 29-configuration cohort.
- `README.md` and `methodology.md`: "Every near-frontier family is ranked or is explicitly deferred by a dated, reasoned roster decision", while MiniMax-M3.1-Flash, a near-only family, is listed under O38 and "0 deferred" (AGENTS.md and the draft both allow the O38 listing).
These do not change a score; fix them in the release tidy-up the ledger already plans.

## 2. Methodology design recommendations

Prioritised.

1. **Verify the pointers against the documents, and replace the per-sentence pointers by one table.** The draft has about fifteen "(README.md for the leading ranking, scores.md for the other; scores.json `…`)" parentheticals; they are the source of I47 M1, I48 M1 and M2 above. Add one "Where each output is printed" table to the draft (output, document, heading or column, `scores.json` field), generated from a manifest `data/doc_contract.json`. Each manifest entry names a literal marker that must appear in the named document (for example the column "Noise band" in README.md's AI Coding Daily table, the heading "Frontier-families bar" in scores.md). Extend `draft_figures check` to fail when a marker is missing. Per-sentence pointers then say "see the output table". This removes the class at the source, as E265 asked, and it would have caught M2 (a), (b), (c), (d).
2. **Population test for per-ranking count lines.** In the emitter tests, assert that every count keyed to "cohort rows" is computed over the ranking's `v3.rows` (never `scores.models` filtered by `rankingEligible`), and that a per-leaf count line sums to the number of rows with that leaf. This catches M1 and the same pattern in `selected_agents_text` and `cross_harness_text` (raw-data.md), which also loop over the union of both rankings; state in the draft that those two raw-data lines are union counts, or make them per ranking.
3. **Carry the E38 scope into the headline bar sentence.** Where a ranked row that clears a bar is not evaluable on the bar's workload, name it with its subset-workload basket cost and say that the cheapest-above-the-bar claim does not extend to it (ordering across workloads is not identified). Today this is DeepSeek V4.1 Flash 1017 (max) and MiMo-V2.6-Pro in the max-effort ranking, MiMo-V2.6-Pro being the API leader. This realises E38's "extends to the selected cohort: not established" in a form the README can carry; then either implement E51's wording or amend it to "(confirmed)" so the draft states what is published.
4. **Structured harness per record.** Parse AI Coding Daily's "Tested … with <harness>" note once into a `harness` field (and Bug Hunt's already has one), so E227, the harness stress branch (E19) and the leaf table's "named on each record" are executable.
5. **Housekeeping in one pass:** L1–L7 above; none needs an owner decision.

## 3. Questions for the owner

None. M1 and M2 are conformance defects with a clear fix; the E51 wording question (implement it or amend it) is an editor choice that changes no score.

## 4. Verdict

VERDICT: HAS FEEDBACK
