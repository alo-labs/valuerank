# Internal review I85 — Claude Opus 5.5 (effort max) on draft r144

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r144`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…moves the register with the chart capture in the swing replay, dates it by the capture, and lists the new build-stopping gates in the manifest. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "the manifest. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1880): O45–O103, E247–E270, I29–I84 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i84-claude-opus-5.5-max.md`, and how the ledger resolved it:
  - M1 became `check_captured_footnotes` and `chart_footnote`;
  - L1 moved the register to the swing bridge's "cohort" class;
  - L2 became `plan_admission.check_change_flags` and the reworded OpenAI evidence;
  - L3 became the O97 and E144 wording;
  - L4 became the manifest rule, E63, the AGENTS.md capture step and the register's bundle instant;
  - Q1 became O103.
- `draft-r144.md`, every line (1–174), as 19 sequential character-range chunks covering all 297,878 characters.
- A sentence-level diff of `draft-r143.src.md` against `draft-r144.src.md`. The hand-written changes are:
  - the title;
  - on line 55, the OpenAI change-detection sentence and the O97 follower sentences;
  - E144's fixture list (line 58);
  - E183's register sentence with O103 (line 116);
  - E63 (in the Governance paragraph, line 152);
  - the r144 history entry.
- The HEAD commit (c66f6f0) diff: `value_v3.py`, `plan_admission.py`, `swing_bridge.py`, three test files, the registry and the generated outputs.
- Code read for the paths involved:
  - in `value_v3.py`: `assemble` (lines 790–910), `configuration_family`, `classify_footnote`, `chart_footnote`, `check_captured_footnotes`, `aa_cost_caveat`, `caveat_factor`, `configuration`, `configurations_from_scores`, the manifest rules, `SAMPLING_TASKS`, the E147 and E154 build stops, `EVIDENCE_FILES` and `SOURCE_INSTANTS`;
  - in `plan_admission.py`: `SPLIT_TYPES`, `splitting`, `check_change_flags`, `applies`;
  - in `plan_routes.py`: the module head, `evidence_grade`, `donor`, `evidence_date`, `expiry_status`, `measurement_objects`, `report_covers`, `pair_replaces`, `effective_measurement`, `rebase_lower_of`, `_rebased`, `rebase_transfer` and `route_candidates` (with the I83 L2 dedupe);
  - `swing_bridge.py`, all of it;
  - in `build_scores.py`: `plotted_name_state`, `check_rendered_path`, the capture checks in `main` and the `build_tracks` call;
  - `frontier.parse_tooltip`; the footnote rendering in `publication.py` and `site/viewmodel.py`; `site/evidence.route_grade`; the `Kernel` class in `scenarios.py`; the task counts in `basket.py`;
  - the three AA capture scripts (`capture_aa.py`, `capture_coding_agents.py`, `scripts/capture-aa-cost-charts.js`) for note handling, and `docs/refresh-and-release.md`.
- Data read or queried:
  - `data/scores.json`, both rankings: rows, `intervals.api.bars[0]`, manifest, workloads and anchors, exchange rates, admission, valuation-gate outcomes, evidence bundle, `planAllowanceCells`;
  - `data/aa_frontier_capture.json` (all three point lists, every footnote, the metadata) and `data/aa_reconciliation_inventory.json` (every `sourceFootnote`);
  - `data/aa/aa_footnote_register.json`;
  - `data/plan_cost_routes.json`: all 137 routes, the 13 stored change flags, `partitionSplits`, `changeDetection` and the search log;
  - `data/plan_reports.json`, `data/swe_tracks.json` (sources and the cutoff-day row) and `data/v3_frozen*.json`;
  - the model-page, Coding Agent Index and cost-chart captures, searched for pricing-caveat text (none is recorded);
  - the r144 wording in `methodology.md`, `README.md`, `scores.md`, `raw-data.md` and `site/data/*.json`.
- The O71 record, spot-checked against line 55: the 2026-10-25 search-log entry (stages, providers, sources reached and unreachable, the Silver Bullet stage's degraded mode). It matches.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0, in the repository and again after a rebuild.
- 1,628 Python tests pass (e2e and js excluded), run in a scratch clone of HEAD.
- `git status` was clean before I wrote this file.

**Reproduction.** In the scratch clone at the pinned clock (`VALUERANK_NOW=2026-10-25T09:56:47Z`), these rebuild byte for byte:
- every `data/*.json` (`build_scores`);
- README.md, methodology.md, scores.md, raw-data.md and `data/figures.json`;
- the whole `site/` tree;
- both scenario files (`python3 -m valuerank.value_v3 scenarios`, 56 s).

**r144's footnote gates, probed on the real data** (scratch clone; probe scripts in my scratchpad; nothing in the repository changed):

| Case | Build | Effect |
|---|---|---|
| (a) New pricing note on GPT-6.1 Sol (max) in the capture only, unregistered | stops | "unregistered AA footnote" |
| (b) The same note registered (factor 2), inventory untouched | stops | inventory differs from the capture |
| (c) Registered and copied into the inventory | builds | GPT-6.1 Sol (max) becomes an O94 blocker; the max-effort headline bar has no confirmed or possible cheapest; scenarios "stale"; release held (max). This is what O94 requires. |
| (d) The Haiku note reworded in the capture only (new text registered) | stops | inventory differs from the capture |
| (e) A registered note on the excluded GPT-6 Luna (low), inventory untouched | stops | the cross-check covers all 30 cohort configurations (`build_scores` passes `by_overall + unscored_primary_rows`), wider than the draft's "a row" |
| (f) The inventory drops Claude Haiku 5.5 (max)'s note | stops | inventory differs from the capture |
| (g) A registered note on GPT-6.1 Sol (max)'s `frontier` and `near_frontier` entries only, not on its `points` entry | **builds** | GPT-6.1 Sol (max) stays the confirmed cheapest at the max-effort headline bar, with no caveat and no hold (see L3) |

**Other r144 changes**
- **Matching.** Every one of the 30 cohort configurations matches exactly one captured point by family and effort, so `chart_footnote`'s "no captured point" branch is never taken in production. The only unmatched `scores.json` models are four catalog models outside the cohort.
- **Flags.** All 13 stored route flags rest on a typed record: Anthropic 2026-10-17T13:00Z ("limit") and OpenAI 2026-10-11 ("price"). No route without a donor on a split plan lacks a flag.
- **Swing bridge.** I84 L1's reworded-note replay now passes. A newly appearing registered pricing note replays with zero score steps.
- **Bundle and manifest.** The register's bundle instant is the chart capture's (2026-10-25T09:53:28Z), and every bundle instant is on or before the cutoff day. The manifest rule in `scores.json`, `methodology.md` and `scores.md` matches E63's first list.
- **O97 and O102.** The O97 dedupe and the E144 fixture list match the code.

**Hand-written facts spot-checked against the data** (all match):
- the allocation regimes, the Fable and Opus multiples, the search log's reached and unreachable sources;
- the S1T and accounting-identity task counts, LiveBench's weights and counts;
- E201b's bar setters (Gemini 4 Argon (high), MiMo-V2.6-Pro) with the 4/5 and 8/9 qualifier counts, and R_W of 7 and 14;
- the exchange rates, recomputed from the anchor references (3.042, 2.439, 2.826, 1.848);
- the anchor references (8 and 16 API, 23 and 51 Plan);
- the valuation outcomes (all "compatible as captured"), the O69 cutoff-day bound, and the 52 report cells (none passes; 24 on unlisted plans).

**Not verified:** live AA pages and boards, and the paywalled SemiAnalysis article.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low

**L1. r144's flag gate makes E18's model-availability trigger unrecordable.**

*The conflict.*
- **What E18 says.** E18 still says a model-availability change makes a route "possibly superseded". It says so in two places:
  - Governance, line 152: "scoped change detection — pricing tables, rate-limit documentation sections and model-availability matrices";
  - the registry rule `sourceEvidence.semianalysis.changeDetection.rule`: "scoped documentation change (pricing, rate-limit and model-availability sections)".
- **What the gate accepts.** r144's `plan_admission.check_change_flags` refuses any `changeDetectedOn` without a "limit" or "price" record for the route's provider and plan on that date. The only types are `SPLIT_TYPES = {"limit", "price"}` and `LOGGED_TYPES = {"metering"}`, and `splitting` refuses any other type.

*Consequence.* An editor who detects a model-availability change has three options, and each one breaks a rule:
- **Record the flag:** the build stops.
- **Type the change "limit" or "price" to pass the gate:** it then also splits the report partition, which O99 reserves for limit and price changes.
- **Leave it unrecorded:** the route stays current, keeps O73's precedence and keeps its label eligibility (fail open).

*Why this is new against the ledger.* I84 L2's residue was the opposite direction: the O83 clause would split at an availability flag. r144 removed that by forbidding availability flags in code. It did not amend E18 or the registry rule, so the conflict moved rather than closed.

*Status:* latent. Every SemiAnalysis route already carries an earlier flag. The gate first bites on a route that is not yet flagged: a re-selected analysis, a report route or a new provider.

*Change.* Decide how an availability change is typed (Q2). Either:
- drop model availability from E18's triggers, which matches O101's limit-or-price rule; or
- add an "availability" type that flags without splitting: `check_change_flags` accepts it and `splitting` leaves it out, and line 55's O83 clause ("a change that flags a route also splits…") is qualified to match.

Add a fixture either way.

**L2. O103 has no guard, so the next routine refresh would skip it silently.**

*What O103 requires.* AGENTS.md: "from the next AA capture, also record and register the notes on model pages, the Coding Agent Index and the cost charts (O103)".

*What the repository does.*
- **The scripts.** `capture_aa.py`, `capture_coding_agents.py` and `capture-aa-cost-charts.js` are unchanged since O103 and record no note text. The cost-chart script hard-codes the meaning of AA's "*" marker as `declinedTasks`.
- **The procedure.** `docs/refresh-and-release.md` does not mention O100 or O103.
- **The build.** No check refuses a capture taken after O103 that lacks note fields.
- **Result.** `npm run refresh`, run as documented, produces captures that build. O103 therefore depends on someone remembering it, which is the fail-open class O100 was adopted to close.

*The draft's wording.* E183 says the register "covers the chart footnotes only until the next AA capture also records the notes…". That makes the extension depend on the capture doing it, where O103 requires it.

*A second, prospective defect.* The swing bridge gives each document one class, and r144 put the register in "cohort" with the chart capture. Under O103 the notes would sit in three classes:
- Coding Agent Index and cost-chart notes in "tokenUse" documents;
- model-page notes in snapshot page fields, owned by "benchmarkRecord".

A replay would then meet a new note before the register that classifies it and raise (I84 L1's failure, now across classes). One register cannot travel with notes spread over three classes.

*Status:* latent; no AA capture has been taken since O103.

*Change.*
- Add a gate: when any AA capture is later than O103's date, each of the three captures must carry a verbatim `notes` field per row (an empty list allowed), and every note must be registered.
- Name O100 and O103 in the refresh document's capture steps.
- Split the register by surface, each part in the class of the document whose notes it classifies, or move every note-bearing field into one class. Add a bridge fixture per surface.
- Word E183 as a requirement.

**L3. The capture's two copies of each cohort point are never compared, so a note on one copy passes.**

*Where the copies are read.* `aa_frontier_capture.json` holds each of the 30 cohort points twice: once in `points` and once in `frontier` or `near_frontier`. Different checks read different copies:
- `chart_footnote` reads `points`;
- `check_captured_footnotes` reads all three lists;
- frontier membership, the inventory comparison (`capture_row_matches`: name, family, effort, fallback, Index, cost), the plotted-name state and the cohort counts read the two lists.

No check compares an entry with its twin in `points`.

*Effect.* Probe (g): a registered pricing note on GPT-6.1 Sol (max)'s list entries only, with the inventory untouched, builds. GPT-6.1 Sol (max) stays the confirmed cheapest at the max-effort headline bar, with no "AA cost caveat" and current scenarios. That is I84 M1's consequence, reached through the capture's own duplication.

*Why Low.* It needs an internally inconsistent capture. Both copies come from the same hover pass, and no routine manual step sits between them, unlike the inventory transcription I84 M1 addressed.

*Change.* Require each `frontier` and `near_frontier` entry to equal the `points` entry with the same `url` and `circle_id` on every shared field, footnote included (in `check_rendered_path` or a new capture check), or derive the two lists from `points` at build time.

**L4. Three texts lag r144's gates.**

- **(a) E63 (line 152).** Its first list names the typed change records and the register. Its second list, "the gates that stop the build when they fail (the Coding Agent Index manifest, the Terminal-Bench agent list, cutoff-day row dates, the plan search, the frontier path checks, the source clocks and freshness gates) are listed together as passed", has two problems:
  - it omits both new gates;
  - the source clocks are a separate manifest rule ("source clocks and evidence freshness (O59, O60, O65, E211, E216, E217, E218)"), so they are not listed together.
- **(b) The manifest rule's detail.** It names "the register of AA chart notes covering every captured one (O100)" but not the stop r144 added when a row's inventory note differs from the capture's note.
- **(c) The register's own `rule` string.** `data/aa/aa_footnote_register.json` is a hashed bundle artifact, and its rule still reads "every AA chart footnote on a ranked configuration is registered here". That is narrower than both the build (every captured point) and the draft (every point, and O103's surfaces from the next capture).

*Change.*
- Make E63's second list match the manifest rule, or render it from the manifest.
- Add the inventory check to the rule's detail.
- Update the register's rule text.

**L5. A lower-of transfer reads a demoted, unreplaced measurement (O95 with O102), so a transfer can lose its route when the replacing pair's figure rises.**

*Probe setup.*
- Release day 2027-02-10: both ChatGPT Plus SemiAnalysis measurements are demoted (published 2026-10-06, now at age 127).
- The registry is as committed, plus a synthetic admitted GPT-6.1 Sol report pair on ChatGPT Plus.

*Results:*

| Pair's pooled multiple | GPT-6.1 Sol (max) and (high) | GPT-6 Luna (max)'s lower-of transfer on Plus |
|---|---|---|
| none | no eligible route | donor GPT-6 Astra's demoted 8.10 → diagnostic |
| 11.25 | select the pair | min(11.25 pair, 8.10 demoted Astra) = Astra → diagnostic → **no Plus row** |
| 6.24 | select the pair | min(6.24 pair, 8.10 demoted Astra) = the pair → assumption grade, current → **Plus row at 6.24** |

So a larger measured GPT-6.1 Sol allowance removes GPT-6 Luna's Plus row, and a smaller one keeps it. The same holds for all ten lower-of transfers on the plan (the cohort's GPT-6 Luna efforts and GPT-5.6 Luna (low) among them).

*Is it a defect?* It follows the literal text:
- line 55 says the effective figure is "the replacing pair … else the measurement";
- O95 takes the lower of the effective figures;
- E144 makes a transfer diagnostic whenever its donor is.

But E142 says demoted candidates "leave the official selection", and O95's purpose was that a lower-of transfer follows replacing evidence. The minimum reads a figure that has itself left the selection.

*Status:* latent until 2027-02-04 (unless the owner re-selects an analysis), and only when one of the two measured models has a pair on a plan.

*Change.* Depending on Q1, either:
- take the lower of the **eligible** effective figures (a demoted, unreplaced measurement drops out of the minimum); or
- state the current rule and its consequence in line 55 and E144.

Add both probes as fixtures.

## 2. Methodology design recommendations

1. **One typed change table drives both flags and splits (L1; extends I84 recommendation 3 with the new availability case).**
   - Types: limit, price, availability and metering.
   - Each route's `changeDetectedOn` is derived: the earliest limit, price or availability record for its plan dated on or after the measurement's earliest possible day, carried by O79 and O84.
   - Only limit and price records split partitions.
   - The build checks both directions: no flag without a record, and no record without the flags it implies.
   - The change-detection sentence on line 55 is rendered from the table. Its dates are typed by hand today and were edited in each of r142–r144.
2. **Make O103 self-enforcing before the next capture (L2).**
   - A capture-format version: every AA capture after O103 carries verbatim notes per row and per surface.
   - A build stop when one does not.
   - Per-surface registers that move with their documents in the swing replay, with a bridge fixture for a new note on each surface.
   - The cost-chart script records the asterisk note's text instead of hard-coding its meaning, so a reworded asterisk note reaches the register.
3. **One normal form for the chart capture (L3).** Derive `frontier` and `near_frontier` from `points` at build time, or assert field-by-field equality, so that every consumer reads one record per point.
4. **A lower-of rule over eligible evidence (L5, subject to Q1).** Take the minimum over the effective figures that are still eligible. Fixtures: (i) both measurements demoted with one pair; (ii) the pair above and below the demoted co-donor.
5. **Generate E63's gate list from the manifest (L4)** with a figure placeholder, so the prose cannot lag a new gate again.

## 3. Questions for the owner

1. **Lower-of with a demoted co-donor (L5).** On a plan where both measured GPT models' SemiAnalysis figures are demoted and only one has an admitted report pair, should a lower-of transfer (O45, O95):
   - take the lower of the **eligible** figures, and so follow the pair; or
   - stay diagnostic while the other model's demoted, unreplaced figure is lower (the current behaviour, under which a more generous pair removes the transfer's route)?
2. **Model-availability changes (L1).** When a provider documents a change to which models a plan offers, should it:
   - flag the plan's routes without splitting the report partition (a new "availability" type);
   - count as a limit change that both flags and splits; or
   - be dropped from E18's triggers, matching O101's rule that only limit or price changes flag?

## 4. Verdict

There are no Critical, High or Medium findings. There are five Lows.

- The figure check exits 0, and 1,628 Python tests pass.
- A clean rebuild of HEAD reproduces every published data file, document and site page byte for byte, and both scenario files too.
- r144 closes I84 M1 as built. A note in the capture alone stops the build, and so does a capture that disagrees with the inventory, on all 30 cohort configurations. A registered pricing note carried into the inventory makes the row a blocker, clears the confirmed label and holds the release, as O94 requires.
- r144 also closes I84 L1 (the reworded-note replay passes), L2 (every stored flag rests on a typed limit or price record, and the GPT evidence cites the Day 7 price change) and L4 (manifest, E63 and bundle instant).

**The findings:**
- **L1:** the new flag gate leaves E18's model-availability trigger unrecordable.
- **L2:** O103 has no guard, and the swing bridge cannot carry one register across three classes.
- **L3:** the capture's duplicated point records are never compared.
- **L4:** E63, the manifest detail and the register's rule text lag r144.
- **L5:** a lower-of transfer reads a demoted, unreplaced co-donor, which makes its route non-monotone in the replacing pair's figure.

Under O56 this round is clean. It is the third round at the Claude Opus 5.5 max rung (I83 and I84 were not clean) and the first clean one, so the rung's clean count becomes one.

VERDICT: HAS FEEDBACK
