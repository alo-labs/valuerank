# Internal review I84 — Claude Opus 5.5 (effort max) on draft r143

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r143`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…puts the label blockers, interval boxes and bar levels in the scenario input hash, and drops a follower that duplicates a pair the configuration already sees. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "already sees. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1869): O45–O102, E247–E270, I29–I83 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i83-claude-opus-5.5-max.md`, and how the ledger resolved it:
  - M1 became O100, the exact-text footnote register;
  - L1 became the wider `scenario_hash`;
  - L2 became the follower dedupe and the `requiredVariant` drop in `_rebased`;
  - L3 became the limit-or-price wording;
  - Q1 became O101, Q2 became O100 and Q3 became O102.
- `draft-r143.md`, every line (1–174), as 19 sequential character-range chunks covering all 296,573 characters.
- A sentence-level diff of `draft-r142.src.md` against `draft-r143.src.md`. The hand-written changes are:
  - the title;
  - on line 55, the amended O77 sentence and the O102 clause;
  - line 116 (O100);
  - lines 152 and 159 (O101);
  - the r143 history entry.
- The HEAD commit (0008020) diff: `value_v3.py`, `plan_routes.py`, `swing_bridge.py`, the new `data/aa/aa_footnote_register.json`, the registry, three test files and the generated outputs.
- Code read for the paths involved:
  - in `value_v3.py`: `assemble`, `classify_footnote`, `aa_cost_caveat`, `caveat_factor`, `_gated_box`, `api_boxes`, `scenario_hash`, `run_scenarios`, `label_exclusions`, `bar_labels`, `blocker_safe`, `attach_scenarios`, `EVIDENCE_FILES`, `SOURCE_INSTANTS`, `evidence_bundle`, `configuration`, `build` and `main`;
  - in `plan_routes.py`: lines 35–160, 394–436 and 482–840 (`report_covers` through `plan_cost`);
  - `swing_bridge.py`, all of it;
  - `plan_admission.py`, the split typing;
  - in `build_scores.py`: the inventory and capture checks (`capture_row_matches`, `near_frontier_selection`, `configuration_tiers`, `frontier_tiers`, the `build_tracks` call);
  - `aa_reconciliation.py`, lines 1–200;
  - `frontier.parse_tooltip`;
  - `scripts/capture-aa-cost-charts.js`, its marker handling;
  - `docs/refresh-and-release.md`, §1.
- Data read or queried:
  - `data/scores.json` (both rankings: rows, intervals, bars, scenario labels, manifest, evidence bundle);
  - `data/plan_cost_routes.json` (all 137 routes, `changeDetection`, typed `partitionSplits`, profile rules, search log);
  - `data/aa_frontier_capture.json` and `data/aa_reconciliation_inventory.json` (every footnote field);
  - `data/aa/aa_footnote_register.json`, `data/aa/coding_agents_manifest.json`, `data/price_records.json`;
  - note fields in `aa_v432_snapshot.json`, `coding_agents_capture.json` and `cost_charts_capture.json`;
  - `research/2026-10-23-refresh/aa-chart-tooltips.json`.
- The O71 record, spot-checked against draft line 55: the stage-3 handoff, research plan, `run_manifest.json` (no search-cli, no helper agents), the research report's verdict, and the 2026-10-25 search-log entry (providers, stages, sources reached and unreachable). It matches.

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- 1,626 Python tests pass (e2e and js excluded), run in a scratch clone of HEAD.
- `git status` was clean before I wrote this file.

**Reproduction.** In the scratch clone at the pinned clock (`VALUERANK_NOW=2026-10-25T09:56:47Z`), these rebuild byte for byte:
- every `data/*.json` (`build_scores`);
- README.md, methodology.md, scores.md, raw-data.md and `data/figures.json`;
- the whole `site/` tree.

`python3 -m valuerank.value_v3 scenarios` also regenerates both scenario files byte for byte (52 s).

**r143's changes, probed** (probe scripts are in my scratchpad; nothing in the repository was changed):
- **Scenario hash (I83 L1).** I gave GPT-6.1 Sol (max) a registered 2× pricing-omission note. The max-effort scenarios turn "stale", the release is held (`releaseHold.heldRankings = ['max']`), and the AI Coding Daily scenarios stay current. The hash covers the bars, the widened boxes (an O98 box hashes as null), and the blocked and claimed sets that `bar_labels` reads.
- **Dedupe and `requiredVariant` (I83 L2).** I added a synthetic GPT-6.1 Sol pair on ChatGPT Plus, registered under (xhigh) with `requiredVariant` "xhigh". GPT-6.1 Sol (high), (medium) and (xhigh) each see one candidate, the pair itself. GPT-6.1 Sol (max) selects the pair over its flagged measurement ("higher evidence grade", O78). The GPT-6 Luna lower-of transfer re-takes 5.099 and names the pair.
- **O102.** At a release day of 2027-02-10, with an Opus 5.5 pair on Claude Pro, the demoted measurement is diagnostic. The pair is selected for Claude Opus 5.5 (max), (high) and (medium). The Sonnet and Haiku transfers follow it at 30.4959 and age with the pair.
- **O100.** The register stops the build on an unregistered note typed into the inventory, even for an excluded configuration (GPT-6 Luna (low)). But see M1.

**Not verified:** live pages and the paywalled SemiAnalysis article.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. O100's closed world is closed over a hand-transcribed inventory field, not over the captured chart. A new or reworded AA footnote in the capture builds silently, so the I83 M1 failure (a silently restored label that O94 forbids) is still reachable.**

*What the draft and the record claim.*
- Line 116 (E183): each footnote "is classified once, by its exact text, in a register …, and the build stops on a new or changed footnote until it is classified".
- AGENTS.md line 19 says the same: "the build stops on any new or changed footnote (O100)".
- methodology.md line 167 says the same.
- The ledger's I83 M1 entry: "no rewording can fail open; a changed note stops the build".
- O100 itself calls this "closed world, the O64 pattern".

*What the build actually reads.* `classify_footnote` (value_v3.py 1054, called at 899) receives `configuration["aaNote"]`. That value comes from `scores.json` `models[].aaFrontierFootnote` (build_scores.py 878), which `configuration_tiers` and `frontier_tiers` (489, 505) copy from the reconciliation inventory's `sourceFootnote`. The links between that field and AA's chart are:
- **No comparison with the capture.** `capture_row_matches` (407–425) checks each inventory row against the capture on model name, family, effort, fallback, displayed Index and cost (and, for near rows, the gap). It never checks the footnote.
- **The reconciliation gate checks only the form.** `aa_reconciliation.check_row_identity` (115) only requires `sourceFootnote` to be a non-empty string or null.
- **Nothing reads the capture's note.** No code reads the capture's `footnote` field.
- **The inventory is hand-kept and outside the bundle.** docs/refresh-and-release.md lists it under "Hand-curated snapshots" (line 34). It is not in `EVIDENCE_FILES`. The evidence bundle lists the frontier capture, whose footnote the build never reads. So E159's "every scored observation records its artifact" does not hold for the one field that decides O94 blocker status.
- **The raw tooltips are not kept.** The 2026-10-25 capture keeps only a parsed `footnote` field. The 2026-10-18 and 2026-10-23 refreshes archived their raw tooltips under `research/`; this one did not. The repository's parser (`frontier.parse_tooltip`, line 142) treats only lines starting with "* " as notes and silently ignores any other unrecognised tooltip line, so a note with another marker never reaches the register at all.

O64 differs on exactly this point: `check_agent_manifest(documents["codingAgents"]["configurations"], manifest)` (value_v3.py 785) compares the manifest with the capture itself.

*End to end* (scratch clone, pinned clock):

| Change | Build | Effect |
|---|---|---|
| (a) **Capture only:** GPT-6.1 Sol (max) gets "GPT-6.1 Sol has 2x higher pricing for prompts above 272k tokens which is not currently reflected in cost figures." in `points`, `frontier` and `near_frontier`; inventory untouched | passes, no stop | Only the frontier-capture and bundle hashes change. GPT-6.1 Sol (max) stays the **confirmed cheapest at the max-effort headline bar**, its scenario label stays, the scenarios stay "current", and its `aaCostCaveat` stays null (no "AA cost caveat" on the row). |
| (b) The same note in the inventory plus a register entry (factor 2) | passes | GPT-6.1 Sol becomes a blocker. The headline bar has no confirmed cheapest (possible set empty), the scenarios go stale and the release is held. This is what O94 requires. |
| (c) Capture only: the Haiku note reworded, and a new pricing note on GPT-6 Luna (max) | passes, no stop | No output changes except hashes. |
| (d) A new note typed into the inventory but not registered | stops | The register works over the transcription only. |

The test suite already relies on the gap. `add_near_family` (tests/test_build_scores.py 1082–1091) writes `"sourceFootnote": "note for <slug>"` into the inventory and no footnote into the capture, and `test_near_family_without_overlap_coverage_still_ranks` builds successfully with them.

*Why this is new against the ledger, and why Medium.*
- O100 and I83 M1 are recorded as adopted on the premise that a changed note stops the build. They do not address that the note is read from a transcription the build never ties to the capture.
- The consequence is the one I83 M1 established as Medium, here shown on a real labelled row:
  - a confirmed label that O94 forbids survives;
  - the "AA cost caveat" disclosure is missing;
  - the row stays in the anchor population at the next freeze;
  - nothing is flagged.
- The ladder treated the same class at the Coding Agent Index link as Medium (I51–I56) until O64 closed it against the capture.
- The refresh procedure (docs §1) tells the editor to capture "any footnote shown on the chart" and to review the O64 manifest after each capture. It says nothing about copying a note into `sourceFootnote` or classifying it.

*Status:* latent. Today the inventory and the capture agree: five Haiku rows carry the same note, and no other row has one.

*Change.*
- Make the capture the only source of the note. Either:
  - read each cohort configuration's footnote from `aa_frontier_capture.json` (by owner URL); or
  - stop the build when the inventory's `sourceFootnote` differs from the capture's `footnote` in either direction, null included.
- Keep the verbatim tooltip text in the capture and have the build re-parse it. Stop on any tooltip line that is not the name, a labelled value, "Click for more info" or a "* " note, and on a trailing "*" with no note line.
- Add the inventory to `EVIDENCE_FILES`, or derive it from the capture.
- Add fixtures (a), (c), an unknown-marker note and a starred name without a note line; each must stop the build.
- Qualify the claim in line 116, AGENTS.md and methodology.md until this holds.

### Low

**L1. The E177 swing replay raises whenever a footnote text first appears between releases. r143 put the register in the "price" class, but the note itself travels with the "cohort" class.**

*Why it fails.*
- `swing_bridge.CLASSES` (line 31) puts `aaFootnotes` in "price".
- The note text is carried by `configurations`, which `apply_class` swaps only in the "cohort" step (line 80).
- The reverse-order replay applies "cohort" first, so the current configurations meet the previous register, and `classify_footnote` raises.
- `bridge` converts only "workload migration" errors (line 152) and re-raises this one.

*Probe* (the test fixtures): A's note is reworded between two releases, and the current register holds both texts (classified once, nothing removed). `sb.bridge` raises "unregistered AA footnote: 'A is plotted with a reworded footnote.'". The forward order would also fail if an editor ever dropped the superseded entry.

*Status:* latent. The gate is "vacuous" in the first v3 release (methodology.md line 208), and `bridge` has no production caller yet. It would first fail at the next release that registers a note, which is the case O100 exists for. The failure is closed (the gate cannot run), and no output is wrong.

*Change.*
- Move `aaFootnotes` to the "cohort" class with `configurations` and `frontierCapture`. A register edit alone never moves a score (O94), so no attribution is lost.
- Add this probe as a fixture.

**L2. O101 is applied by hand, and pre-O101 wording still grounds the GPT flag on "metering".**

*Where the old wording remains.*
- **Draft line 55.** The sentence two sentences after the amended O77 rule still reads: "ChatGPT plans: OpenAI announced changes to subscription usage metering after the measurement (from 2026-10-11: … then longer caching and context reuse), so the SemiAnalysis GPT routes … are possibly superseded from 2026-10-11." That is the reason O101 says flags nothing.
- **The registry's OpenAI outcome** (`sourceEvidence.semianalysis.changeDetection.outcomes[1].evidence`). It cites "owner decision O77: a provider's own announcement of a change to subscription usage metering triggers E18" and lists Days 12, 16 and 19 as evidence.
- **The eight GPT SemiAnalysis routes' `changeDetectionEvidence`.** Each reads "E18/O77: OpenAI announced changes to subscription usage metering … Day 12 … Days 16 and 19".

*Enforcement.*
- Route flags are free-typed `changeDetectedOn` dates.
- Only partition records are typed and checked (`plan_admission.SPLIT_TYPES`, line 67).
- So nothing stops a future metering-only announcement from being entered as a flag.
- Today the flag date (2026-10-11) coincides with the one OpenAI record typed "price", so no output changes.
- A smaller residue: line 55's O83 clause ("a change that flags a route also splits…") would still split at an E18 model-availability change, which O99 says does not split.

*Change.*
- Reword these three places around the Day 7 price change. Days 12, 16 and 19 are logged and flag nothing.
- Derive flags from the typed records (recommendation 3).

**L3. Two draft passages describe mechanics that r143 changed.**

*(a) The O97 follower path no longer reaches any cohort row.*
- Under O87 a report pair covers every configuration of its AA family, so the pair is always a candidate wherever an O88 route follows it. r143's dedupe therefore always drops the follower.
- The row selects the pair object itself. Probe: GPT-6.1 Sol (high) publishes the pair's flags ("workload-unmatched", "observed-usage multiple…"), no `REPORT_PAIR_FLAG` and no `rebasedFrom`.
- Line 55 still says an O88 route takes the pair's figure "flagged as following its donor's replacing report pair (O97)" and "under its own identity", and that "every rebased route publishes the donor it was rebased from".
- O97's quoted label ("follows its donor's replacing report pair (O96, O97)") is now unreachable. It is reachable only without a families map, as in the unit test.
- Change: either say that the configuration selects the pair itself, or dedupe the other way (keep the follower, which carries the pair's whole record plus the O97 label, and drop the duplicate pair object).

*(b) E144 does not reflect O102.*
- Line 58 replaces a donor by its effective measurement only "when a report pair replaces that measurement (O95, O96…)".
- Its fixture list still reads "demoted donor → transfer diagnostic", which under O102 holds only when the model has no admitted pair on that plan.
- Change: cite O102 in both places.

**L4. The O100 gate is missing from the build-stopping list and from the refresh procedure.**
- The active-rules manifest's "build-stopping evidence gates (O64, O69, O71, O75, E195, E204, E225)" (scores.json `manifest`; methodology.md line 207) omits O100.
- The draft's E63 list on line 152 omits it too.
- docs/refresh-and-release.md says nothing about classifying a new footnote.
- The bundle stamps the register with its review date (2026-10-28). That is three days after the release cutoff, while line 152 says an editorial file carries "its source's own latest instant" (here the 2026-10-25T09:53:28Z chart capture). The code instead follows its own convention of review dates for editorial files.
- Change: name O100 in the manifest rule, in E63 and in the refresh steps, and make line 152's instant rule match the code.

## 2. Methodology design recommendations

1. **A capture-backed footnote register (M1).**
   - The build reads AA notes only from the chart capture, which keeps verbatim tooltips. It re-parses them, stops on any unrecognised tooltip line, and stops when a note on a cohort configuration is missing from the register.
   - Register entries gain:
     - the capture instant at which each text was first seen, and the configurations it was seen on;
     - a required reason;
     - a check that no text is registered twice (today `next(...)` silently takes the first).
   - The inventory either joins the evidence bundle or is derived from the capture.
   - This finishes what I83 recommendation 1 intended: no editor step can drop a note between AA's page and the classification.
2. **One class for a note and its classification (L1).**
   - Put the register in the swing bridge's "cohort" class with the configurations that carry the notes.
   - Add a fixture in which a note text first appears in the newer release.
3. **One typed change record drives both splits and flags (L2; extends I83 recommendation 4).**
   - Each provider change is one record, typed limit, price or metering, with the plans it covers (the OpenAI records still have no `plans` field; I67 recommendation 3).
   - The build derives each route's `changeDetectedOn`: the earliest limit or price record for its plan dated on or after the measurement's earliest possible day, carried across shared meters by O79 and to every Kimi plan by O84.
   - The build refuses a hand-entered flag that no such record supports.
   - The change-detection prose (draft line 55, the registry outcome and the per-route evidence) is generated from the records, so O99 and O101 cannot drift apart again.
4. **Publish each footnote's classification.**
   - `aaNoteClass` is computed but not published.
   - Add the kind, factor and reason to `rows[]` and to the README's footnote line. A reader can then see that a note was judged "not a pricing omission", and why. Today only pricing omissions show at all.

## 3. Questions for the owner

1. **Scope of O100.**
   - Should the register (and so O94) cover AA's statements that a cost omits a pricing term on every AA surface the basket cost is read from? That means the model pages, the Coding Agent Index page and the per-evaluation cost charts.
   - Today only the Intelligence Index chart's tooltip notes are captured:
     - the cost-chart capture keeps only a declined-tasks boolean;
     - the Coding Agent Index and model-page captures keep no note text.
   - If yes, those captures must also keep note text and stop on new text (recommendation 1 widens). If no, line 116 should say "Intelligence Index chart footnote".

## 4. Verdict

There are no Critical or High findings. There is one Medium and four Lows.

- The figure check exits 0, and 1,626 Python tests pass.
- A clean rebuild of HEAD reproduces every published data file, document and site page byte for byte, and both scenario files too.
- r143's scenario hash, follower dedupe, `requiredVariant` drop and O102 path do what the ledger says in every case I probed.

**The findings:**
- **M1:** the O100 register is closed over the inventory's hand-copied `sourceFootnote`, which the build never compares with the chart capture. A pricing note present only in the capture leaves GPT-6.1 Sol (max) as the confirmed headline-bar cheapest with "current" scenarios and no caveat. This is the I83 M1 consequence, reached through the transcription step.
- **L1:** the swing replay raises on a newly registered note.
- **L2:** O101 is applied by hand, and the pre-O101 GPT flag wording remains.
- **L3:** the O97 follower and E144 text are out of date.
- **L4:** O100 is missing from the build-stopping list and the refresh steps.

Under O56 this round is not clean. It is the second round at the Claude Opus 5.5 max rung, and the rung's clean count stays at zero.

VERDICT: HAS FEEDBACK
