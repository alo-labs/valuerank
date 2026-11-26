# Internal review I83 — Claude Opus 5.5 (effort max) on draft r142

## 0. Read check

- **First line of the draft:** `# ValueRank methodology — draft r142`
- **Last line of the draft (line 174):** the revision-history paragraph. It begins "Revision history: r16–r24 fixed the published-record interval target…" and ends "…r142 (eighty-second internal review, the second clean one at Opus 5.5 xhigh, and owner decisions O98 and O99) takes a follower's figure from the comparator's own selection for its donor model, keys report coverage by AA family, rebases an O88 follower by the pair's whole record, lets a factorless AA cost caveat compete over [C, ∞), and splits report partitions only at limit or price changes. Every change is recorded with its rationale in the ledger."
- **Last 12 words of the last paragraph:** "price changes. Every change is recorded with its rationale in the ledger."

### What I read

- `reviewer-prompt.md` and `ledger-brief.md`, in full.
- `ledger.md` from "## Internal review I28" to the end (lines 1170–1857): O45–O99, E247–E270, I29–I82 and the O71 research outcome.
- `/home/user/valuerank/AGENTS.md`, in full.
- `review-i82-claude-opus-5.5-xhigh.md`, and how the ledger resolved it:
  - L1 became `effective_measurement` running the comparator for the donor model, families-keyed `report_covers`, `requiredVariant` ignored for report routes, and the report-donor stage in `expiry_status`.
  - L2 became the whole-object `_rebased`, `crossEffort` read from the candidate, `rebasedFrom` in `plan_cost`, and O97–O99 in `o72Application`.
  - L3 became O98, back-reference and "(5x)" factors, "higher pricing" dropped from the omission test, factors below 1 ignored, and the O29 unconstructible test restricted to candidates.
  - L4 was adopted (line 35, E64(b)).
  - Q1 became O98 and Q2 became O99.
- `draft-r142.md`, every line (1–174), in 26 sequential chunks of at most 16,000 characters. Lines 152 and 174 were each read in two parts.
- A sentence-level diff of `draft-r141.src.md` against `draft-r142.src.md`. The hand-written changes are lines 35, 55, 106, 116 and 135, the title and the r142 history entry.
- The HEAD commit (7bfa819) diff. It touches:
  - `plan_routes.py`, `value_v3.py`, `plan_admission.py` and `draft_figures.py`;
  - three test files, AGENTS.md and the ledger;
  - the published data. In `scores.json` only the partition indices, the O94 rule text and the hashes changed, so no score moved.
- Code read in full for the paths involved:
  - `plan_routes.py`, all of it;
  - `plan_admission.py`, all of it;
  - in `value_v3.py`: `assemble`, `plan_variants`, `_gated_box`, the caveat reader (`_sentences`, `_is_caveat`, `_factors`, `caveat_factor`), `blocker_domain`, `api_candidates`, `plan_candidates`, `interval_outputs` (the unconstructible set), `route_alternatives`, `scenario_panel`, `scenario_hash`, `run_scenarios`, `bar_labels`, `blocker_safe`, `attach_scenarios`, `configuration` and `configurations_from_scores`;
  - in `intervals.py`: `Box`, `frontier`, `_possibly_cheapest` and `cheapest_above_bar`;
  - the `build_tracks` call in `build_scores.py`;
  - `docs/refresh-and-release.md`.
- Data read or queried:
  - `data/scores.json` (both rankings);
  - `data/plan_cost_routes.json` (all 137 routes, `evidencePolicy`, the typed partition records, `changeDetection`, `o72Application`, the search log);
  - `data/plan_reports.json` through `planAllowanceCells`;
  - the AA footnote fields in `aa_frontier_capture.json` and both reconciliation files;
  - `data/price_records.json`;
  - both scenario files;
  - `methodology.md` line 167;
  - `site/data/plans.json`.
- The O71 record, spot-checked against the draft's line 55: the stage-3 handoff and research plan (search-cli unavailable, no helper agents) and the 2026-10-25 search-log entry (providers, stages, sources reached and unreachable).

### What I verified

**Checks and tests**
- `python3 -m valuerank.draft_figures check` exits 0.
- 1,626 Python tests pass (e2e and js excluded), run in a scratch git copy of HEAD.
- `git status` was clean before I wrote this file.

**Reproduction.** In a scratch export of HEAD at the pinned clock (2026-10-25T09:56:47Z), these rebuild byte for byte:
- every `data/*.json` (`build_scores`);
- README.md, methodology.md, scores.md, raw-data.md and `data/figures.json`;
- the whole `site/` tree.

New against I82, which left the scenario draws unverified: `python3 -m valuerank.value_v3 scenarios` regenerates `v3_scenarios.json` and `v3_scenarios_aicd.json` byte for byte. So E159's scenario reproducibility holds, and today's scenario labels are current.

**r142's figures and registry**
- R_W is 7 and 14 (`intervals.api.universe`). The blockers are Claude Haiku 5.5 (max), and (high) and (medium).
- The metering-only records are OpenAI at 2026-10-16, 2026-10-20 and 2026-10-23, all typed "metering". The splits that remain are Anthropic "limit", OpenAI 2026-10-11 "price" and Kimi "limit".
- O99 changes no verdict. Every eligible OpenAI report predates 2026-10-11, so every OpenAI cell fails, under four splits or one.
- `o72Application` and methodology.md line 167 now carry O97–O99, and AGENTS.md states O98 and O99.

**r142 code, probed on the real registry plus synthetic report pairs** (scripts are in my scratchpad):
- An Opus 5.5 pair on Claude Pro with `requiredVariant` none, "max" and "high". Claude Opus 5.5 (max), (high) and (medium) and the Sonnet transfer all take 30.496×.
- A GPT-6.1 Sol pair on ChatGPT Plus (5.0 and 5.2):
  - the O88 followers take the pair's grade, its flag and its own E166 amount ($102.00, the pair's recorded numerator, which fixes I82 L2);
  - the lower-of transfer re-takes the lower effective figure, names the pair and publishes `rebasedFrom`.

So the donor's row and its followers now agree on the figure in every case I tried.

**O98, end to end.** A factorless rephrasing of the Haiku note keeps the three blockers. The outputs stay "evaluated" with the baseline's labels, `scores.json` stays valid JSON with no Infinity, and the O94 rule reads "no factor stated: [C, ∞), O98".

**Two further end-to-end rebuilds** (M1 and L1 below).

**Not verified:** live pages and the paywalled SemiAnalysis article.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. r142's narrowed AA caveat reader fails open on ordinary phrasings of the same caveat. The row then silently stops being an O94 blocker: it regains a label O94 forbids, loses its "AA cost caveat" disclosure and stays in the anchor population at the next freeze.**

*What the draft says.*
- Line 116 (E183): a note counts as an O94 caveat "through a sentence naming a price or cost figure that is not reflected, included or counted, or is excluded or omitted".
- Line 135 (E92): such a row "is never an anchor reference from the next re-freeze" and earns no label.
- Line 152 (E141): the note "is shown on the row as 'AA cost caveat'".

*What the code does.* Every one of these consequences hangs on one predicate, `aa_cost_caveat`. It feeds:
- the blocker sets in `interval_outputs` and `bar_labels`;
- `_gated_box`;
- `withheld_label`;
- `leavesAtNextFreeze`;
- `rows[].aaCostCaveat` (the README and site flag);
- the manifest rule.

The predicate needs a pricing term plus `AA_OMISSION` = `not (currently )?(reflected|included|counted) | exclud(es|ed|ing) | omit(s|ted)?`. r142 removed the `higher pricing` alternative. Probes:

| Phrasing (the same 5× caveat) | r141 reader | r142 reader |
|---|---|---|
| the real note ("…which are not currently reflected; …") | caveat, 5× | caveat, 5× |
| "…on longer-context inputs, which our cost figures do not currently reflect" | caveat, 5× | **no caveat** |
| "…which are not yet reflected in cost figures" | caveat, 5× | **no caveat** |
| "…which isn't reflected in our cost figures" | caveat, 5× | **no caveat** |
| "Our cost figures don't include Claude Haiku 5.5's 5x higher pricing on longer-context inputs." | caveat, 5× | **no caveat** |
| "Gemini 4 Argon pricing is 2x higher for prompts above 200k tokens; this is not yet reflected in cost figures." | no caveat | **no caveat** |

*End to end.* I rebuilt the pinned release in a scratch copy with the Haiku note reworded to "…on longer-context inputs, which our cost figures do not currently reflect; we are working to include this across Artificial Analysis." The build passes, with no stop and no flag:
- The manifest rule reads "passed: no AA cost note names an omitted pricing term".
- Neither ranking has a blocker. R_W grows from 7 to 8 and from 14 to 16.
- In the AI Coding Daily ranking, scores.md now prints at quality 38.0: "Status certified; confirmed cheapest: Claude Haiku 5.5 (medium)". The baseline prints "none". This is exactly the label O94 removed (ledger, O94).
- `aaCostCaveat`, its factor and its range are null on all five Haiku rows. The "AA cost caveat" mentions drop from 3 to 0 in scores.md and from 4 to 1 (the legend) in the README, whose Flags column loses it on all three ranked Haiku rows.
- `anchorEligibility` no longer marks Claude Haiku 5.5 (max) `leavesAtNextFreeze`.
- The scenario section still reads "current" (see L1).

*Why this is new against the ledger.*
- I81 L3 declined a footnote register because "the narrowed reading fails closed on every case I81 tabled". I82 L3 (Low) showed only fail-closed cases.
- O98 has since made the closed direction harmless: a factorless caveat competes over [C, ∞) and every label stays decidable. The reader's only remaining failure mode is therefore the open one, and r142 widened it.
- On calibration, this ladder rated silent misreads of hypothetical AA strings by the Coding Agent Index label reader as Medium (I51 M1, I54 M1, I55 M1, I56 M1), and that class ended in O64's closed world. This is the same class, with an unsound published label as the consequence.
- AA's note itself says AA is "working to include this in cost figures", so a rewording is expected. Other providers' tiered long-context prices invite similar notes in other words.

*Status:* latent; the current note reads correctly.

*Change.* Stop letting a text heuristic decide the default (recommendation 1, Q2):
- Register every captured AA footnote text with a reviewed classification:
  - a pricing caveat with its factor;
  - a pricing caveat without a factor, which competes over [C, ∞) under O98;
  - not a cost caveat, with a reason.
- A new or changed text stops the refresh until it is registered. The capture holds one distinct text today, so the register starts with one entry.
- Keep the reader only as a cross-check that stops the build when it disagrees with the register.
- Until then, at minimum:
  - treat any note sentence that names a price or cost and carries any negation or omission ("not", "n't", "not yet", "no longer", "omit…", "exclud…", "ignor…", "does not account for") as a caveat;
  - restore "higher pricing";
  - add the four phrasings above as fixtures;
  - widen line 116's wording to match.

### Low

**L1. The scenario input hash leaves out the inputs that decide scenario-label candidacy, so a change in blocker status attaches stale scenario labels as "current".**

*What is and is not hashed.* `scenario_hash` covers:
- β, N and the seed;
- the main workload's anchors;
- the harness band;
- the scenario panels (row, coverage-provisional flag, cost and leaf kernels).

`bar_labels` also reads three things that are not hashed:
- the frozen bar references;
- the interval boxes (`api_boxes`, for the candidate list and BlockerSafe);
- the blocked and claimed sets (O29 gate, E222, E233, O94).

`attach_scenarios` decides currency on the hash alone ("scenario outputs current (E72): scenario input hash matches the scored inputs").

*Probe.* In a scratch copy I gave GPT-6.1 Sol (max) an AA note naming a 2× unreflected long-context price.
- The interval outputs update correctly. README line 131 says it is "Competing without a label of its own (E183): … AA's cost omits a pricing term (O94)", and the headline bar has no confirmed cheapest.
- The scenario section keeps the identical input hash and stays "current".
- scores.md still prints, at quality 63.5: "GPT-6.1 Sol (max) | supported under all registered role-group kernel checks | 100.0% to 100.0% | … | yes".

A blocker carrying a scenario-supported label is what E186 forbids ("a blocker is never itself a candidate"), and the E72 rule says "passed".

*Triggers.* Any change in blocker status with an unchanged panel:
- an AA re-capture whose only label-relevant change is a footnote or a displayed price;
- a change to the denial rules without a manual scenario rerun (as with O94 at r139 and E222 at r136);
- a bar re-freeze on unchanged anchors (O61 re-froze bars on the same anchor version).

The release procedure (`docs/refresh-and-release.md`) reruns scenarios only when the build reports them stale.

*Status:* latent. The committed scenario files are current; both regenerate byte for byte.

*Change.*
- Hash the label-eligibility inputs: the blocked and claimed IDs with their reasons, the boxes' cost and quality bounds as used for candidates and BlockerSafe, and the bar references. Alternatively, rerun the scenario command in every refresh (18 s and 36 s here).
- Add a fixture: making a labelled row a blocker marks the scenarios stale.

**L2. With report coverage keyed by AA family (r142), an O88 configuration sees one replacing pair twice, and a pair's `requiredVariant` leaks into its O97 followers.**

*Twin candidates.* `route_candidates` now gives a pair directly to every configuration of its family, and also gives each O88 route of that family rebased onto the same pair (O97).
- Probe: with the GPT-6.1 Sol pair on ChatGPT Plus, GPT-6.1 Sol (high) has two "reports" candidates with the identical tuple (0, 2, 5.099, −20): its rebased O88 route and the pair's own object `chatgpt-plus-gpt61sol-reports#m1`.
- The published selection reason is "route ID tie-break".
- E171's table lists one measurement twice.
- E179 counts `admissiblePairs` 2. Where that plan is the row's own selected route, E179's leave-selected-out choice is the twin at the identical multiple. That defeats E179's stated purpose: "so the gain from selecting the largest of several unidentified observed multiples is visible".

*The `requiredVariant` leak.* `_rebased` overrides `FOLLOWER_IDENTITY` keys only where the follower has them.
- None of the 33 O88 routes has a `requiredVariant` key, while the registry's only report route does ("xhigh").
- A follower rebased onto a pair registered with a variant therefore inherits it. `route_candidates` exempts only routes that were report routes before rebasing, so the follower is dropped.
- Probe: an Opus pair on Claude Pro registered with "max". The E106 table for Claude Opus 5.5 (high) and (medium) shows their O88 routes as case 1 ("execution-identity incompatibility"), which E106 case (1)'s carve-out says they are not. The pair still covers both rows directly, so the figure is unchanged.

*Status:* latent; no figure differs.

*Change.*
- Make one candidate per measurement object. Either key E116's identity of a report-based object by its partition and report IDs, or skip the O97 follower where the pair already covers the configuration.
- Set the follower's `requiredVariant` explicitly in `_rebased`.
- Add a fixture for each.

**L3. O83's unconditional split rule still stands beside O99 in the draft, AGENTS.md, methodology.md and the published registry rule.**

Where it stands:
- **Draft line 55.** The sentence reads "A partition splits only at a change … to the plan's limits or price (O99 …), and a change that flags a route also splits the report partitions for the same plans at its date (O83 …)". Under O77 a metering-only announcement does flag routes: the registry's OpenAI `changeDetection` cites Days 12, 16 and 19 as O77 triggers. The second clause therefore splits on them, and the first does not.
- **AGENTS.md.** It says "A provider announcement or a detected change splits the report partition for the plans it covers … (O83)", and later "Report partitions split only at a change to a plan's limits or price; a metering-only announcement is logged (O99)".
- **methodology.md line 167.** It says "a provider-documented change splits the partition too (O83)" before stating O99.
- **The published registry rule.** `evidencePolicy.reportEligibilityProfile.rules`, rendered on the site's Plans page, still says "a partition splits only at a change E18 detected or a provider documented, at that change's date", with no limit-or-price condition and no metering exception.

The code follows O99, and rule precedence (line 3) resolves the conflict. But line 3 calls such a conflict a defect to correct, and AGENTS.md is the instruction an editor follows when typing a new partition record.

*Change.*
- Qualify the O83 clauses: "a limit or price change that flags a route also splits…".
- Update the registry rule text.
- Generate these sentences from the typed records (recommendation 4).

## 2. Methodology design recommendations

1. **A closed-world register for AA footnotes (M1, Q2).**
   - The design is the one O64 applied to Coding Agent Index rows. Each captured footnote text (hashed) maps to a reviewed classification, a factor (or none, which means [C, ∞) under O98), a reason and a date.
   - The build stops on a new, changed or vanished text.
   - The present reader becomes a cross-check that stops on disagreement.
   - This removes the last free-text heuristic that decides label eligibility. That class has now recurred in I80 L2, I81 L3, I82 L3 and here, and E265's owner rule is to remove a recurring class at its source.
   - With O98, a register entry costs nothing in soundness: an uncertain classification can always be "caveat, no factor".
2. **Hash every input that decides a scenario label (L1).**
   - Add these to `scenario_hash`:
     - the blocked and claimed sets with their reasons (O29, E222, E233, O94);
     - the interval boxes that `bar_labels` reads;
     - `frozen["barReferences"]`.
   - Alternatively, make the refresh always rerun the scenario command.
   - Either way, E72's "current" then means what it says.
3. **One candidate per measurement object (L2).**
   - Under O87 and r142, the report pair itself covers every configuration of its family. The O97 follower is then the same object under another route ID.
   - Deduplicate by the object's partition and report IDs (E116) before E88, E85, E171 and E179 see the candidates.
   - Never carry a pair's `requiredVariant` onto a follower.
4. **One typed source for the split rule (L3).**
   - Render the split sentence in the registry rule, methodology.md and AGENTS.md from the typed `partitionSplits` records and `SPLIT_TYPES`, as `OWNER_ASSUMPTIONS` does for the assumption kinds.
   - Extend the assumption-list lint so that an "(O83)" split sentence without the limit-or-price condition fails.

## 3. Questions for the owner

1. **O77 versus O99 for a metering-only announcement.**
   - O99 treats such an announcement as leaving the allowance unchanged, so it does not split report partitions. O77 still lets it flag the controlled measurement as possibly superseded, which also makes the row an E228 blocker.
   - O78 lets a report pair replace a flagged measurement only when every report postdates the change, and E107 forbids a searched-for subset.
   - So a route flagged only by a metering-only announcement could be replaced only after every concordant pre-announcement report has left the 30-day window, because those reports pool with the post-announcement ones.
   - Nothing turns on this today: the GPT routes are flagged from the price-typed Day 7 post, which still splits.
   - Should a metering-only announcement (a) neither split nor flag, (b) flag and split, or (c) flag without splitting, as now, accepting that delay?
2. **Footnote register.** Should every AA footnote text be registered with a reviewed classification, so that a new or changed note stops the refresh until it is classified (O64's pattern)? The cost is one review per new note text. The gain is that no wording AA chooses can silently create or remove an O94 blocker (M1).
3. **Demoted donor.**
   - When a donor measurement is demoted (past expiry and grace) and its model has an admitted report pair on that plan, r142's followers take the pair, because the comparator selects it as the only eligible route.
   - O96 defines the effective figure as "the replacing report pair when one replaces the measurement under O78 or O92, else the measurement". Read that way, a demoted donor leaves its transfers diagnostic (E144).
   - Line 3 says an editor record never amends an owner decision.
   - Should the routes resting on a demoted measurement follow its model's pair (amend O96), or fall back as before? This stays latent until 2027-02-04 and needs a pair.

## 4. Verdict

There are no Critical or High findings. There is one Medium and three Lows.

- The figure check exits 0, and 1,626 Python tests pass.
- A clean rebuild of HEAD reproduces every published data file, document and site page byte for byte, and now both scenario files too.
- r142's comparator-selected donor figure, AA-family report coverage, whole-object O97 rebase, `rebasedFrom`, O98 box and typed O99 splits do what the ledger says for every case I probed. The donor's row and its followers agree on the figure, and the O97 amount is the pair's.

**The findings:**
- **M1:** the narrowed caveat reader fails open on ordinary wordings. A full rebuild with one such wording silently restores the confirmed label O94 removed from Claude Haiku 5.5 (medium) and drops the O94 disclosures and anchor exit. The ladder has treated this class (a silent misread of AA strings) as Medium before.
- **L1:** the scenario hash does not cover label eligibility.
- **L2:** twin candidates and a `requiredVariant` leak from r142's family coverage.
- **L3:** O83's wording stands beside O99.

Under O56 this round is not clean. It is the first round at the Claude Opus 5.5 max rung.

VERDICT: HAS FEEDBACK
