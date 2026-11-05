# Internal review I51 — Claude Sonnet 5.5 (effort xhigh) on draft r109

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r109".
- Last line of the draft: "check now covering them in dated sentences too. Every change is recorded with its rationale in the ledger."
- Last 12 words of its last paragraph: "sentences too. Every change is recorded with its rationale in the ledger."
- Also read: the reviewer brief and `reviewer-prompt.md`; the whole folded draft (972 lines) and, for placeholders, `draft-r109.src.md`; `ledger-brief.md`; `ledger.md` from "Internal review I28" to the end (including "Internal review I50"); `AGENTS.md`.
- Code and data opened to check the I50 changes and the draft's executable claims: `valuerank/value_v3.py` (`check_agent_pins`, `_AGENT_LABEL`, `assemble`, `check_source_clocks`, `configurations_from_scores`, `rank_separability`, `sampling_sd`, `quality_sd`), `valuerank/plan_routes.py` (`evidence_date`, `expiry_status`), `research/2026-10-23-swe-benchmarks/build_swe_tracks.py` (`select_aicd`), `valuerank/draft_figures.py` (`registry_figures`, `REGISTRY_FACTS`, `registry_problems`, `lint`, `dated`), `valuerank/diagnostics.py`, `valuerank/anchors.py`; `data/v3_configuration_map.json`, `data/aa/coding_agents_capture.json`, `data/plan_cost_routes.json`, `data/swe_tracks.json`, `data/bug_hunt.json`, `data/aa_frontier_capture.json`, `data/scores.json`, `README.md`, and the AI Coding Daily capture parse.
- Executed (read-only): `python3 -m valuerank.draft_figures check` (clean), `tests/test_draft_figures.py` and `tests/test_plan_routes.py` (pass), and synthetic calls to `check_agent_pins` (below). No repository file other than this review was written.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. The Coding Agent Index pin gate does not implement the exact-record predicate the draft states, so "a missing pin can never move a row onto a subset workload" is false in three reproducible cases.**

Where: Cost section, "Cost-source match (I50)" (draft lines 171-174); code `value_v3.check_agent_pins` and `_AGENT_LABEL`. The draft defines an exact record as one that "names one model whose identity and effort equal the configuration's", says a two-model record "is never exact", and says the build stops "when a cohort row's pin is empty while an exact record exists". It then claims the gate makes a silent move to a subset workload impossible. That was the High of I50, so the guarantee has to hold. I checked it against the code and the capture. Every pin that has an exact record in today's capture matches it (all eight rows that carry a record), so no ranking changes now. The gate nevertheless has these gaps:

- (a) Effort-less configurations are invisible to it. The regex requires a parenthesised effort and the comparison is `(keyed or plain) == configuration["effort"]`, which is never true when the effort is `None`. AA plots MiMo-V2.6-Pro, MiMo-V2.6-Flash and MiniMax-M3.1-Flash without an effort (`aaPlottedNames`), and AA's agent page already lists effort-less records ("Claude Code - Qwen3.8 Max", "Kimi Code CLI - Kimi K3"). `check_agent_pins([{"id": "mimo-v2-6-pro", "family": "MiMo-V2.6-Pro", "effort": None}], {}, {"Claude Code - MiMo-V2.6-Pro": {}})` does not stop (nor does a "… (high)" record). Under the draft's predicate "Claude Code - MiMo-V2.6-Pro" is an exact record of an effort-less configuration. MiMo-V2.6-Pro is already the one subset row of the max-effort ranking, so I50 H1's failure would repeat unseen. The draft also never says how O54's "taken at high" applies to a cost record named "MiMo-V2.6-Pro (high)".
- (b) A dangling pin passes. Any non-empty pin satisfies the gate, whether or not it names a captured record. The map already holds eight pins that name no record in the current capture (the Sol high, medium and xhigh rows, the Haiku xhigh, high, medium and low rows, and Sonnet xhigh; benign today because no exact record exists for them). The captured labels also vary in form within one capture ("Codex - GPT-6.1 Sol (max)" against "Codex - GPT-6 Luna (max) ({'reasoning_effort': 'max'})"). If AA changes a label's form, the pin dangles, an exact record exists, the gate is silent, and the row falls to the subset workload. I confirmed the silence with a pin spelled with the keyed suffix against a capture holding "Codex - GPT-6.1 Sol (max)". "Pin is empty" is the narrower test; the failure the draft wants to exclude is "pin is not an exact record while one exists".
- (c) A two-model label can be treated as exact. `[^+]+?` stops the match only when a "+" comes before the first parenthesis. "Codex - GPT-6 Luna (max) + GPT-6 Sol (max)" parses as GPT-6 Luna (max). With the real `family` field, an empty pin on GPT-6 Luna (max) then stops the build for a record the draft calls never exact, and the only way to unblock is to pin that mixed record. `test_an_empty_agent_pin_with_an_exact_record_stops_the_build` includes this label to cover the case, but it passes vacuously: its `luna` fixture has no `family`, and the second call raises at `ds` before `luna` is reached. With `family` set, the first call raises.

Why it matters: this is the failure class of the last round's High, and the draft states a total guarantee that the code does not give (the "two faithful implementers" test: the draft's predicate and the shipped gate differ on effort-less rows, on pins that name no record, and on two-model labels).

Why Medium and not High: no ranked row is affected today, and each case needs an AA relabel or a new AA record.

Change: (1) one function `exact_agent_records(configuration, records)` used by both the gate and the matching. It parses the full label, anchored at both ends, splits on " + " first (more than one model means not exact), handles the effort-less case (a record with no effort belongs to an effort-less configuration; state O54's high for MiMo-V2.6-Pro), and ignores a trailing "(with fallback)". (2) The gate becomes: if `exact_agent_records` is non-empty, the pin must be one of them (a recorded choice when there are several), else the build stops; an empty set with an empty pin is fine. (3) Fixtures that set `family`, and one per case above. (4) Reword "can never" to what the gate enforces.

### Low

**L1. Two new rules carry review labels, not decision numbers.** "Cost-source match (I50)" and "A board that lists a configuration twice (I50)" are the only I-labels in the body. This contradicts I44 L6 (adopted: internal review labels removed from the specification's body; r103 history says so). It also leaves the two rules outside the preamble's scheme ("every rule tagged with an owner (O) or editor (E) number is normative wherever it appears"; the later-numbered editor record governs). Give them E-numbers (next free E267 and E268) and drop "(I50)" from the body.

**L2. Registry facts are still hand-typed in the Source contract, and the check cannot see them.** Draft line 71: "captured 2026-10-23T05:27:39Z for the release cutoff O47 set, previously 2026-10-17" is typed in the source. These are `aa.capturedAt` and `aa.previousCapture`. They are correct today, so nothing is stale. This is a defect in the source and in the check, the E265 guard class that I50 L5 claimed to have closed. The `REGISTRY_FACTS` context for `aa.capturedAt` is `\bcapture\b`, which does not match "captured"; `aa.previousCapture` and `evidence.windowEnd` are not listed at all. The lint also exempts any sentence containing "at O<n>" (`dated()`), which E265's text does not mention. Use placeholders; make the context `capture\w*`; add the two keys; state the "at O<n>" exemption or drop it (see recommendation 3).

**L3. "AA's agent page omits the fallback token" is contradicted by the capture.** `Claude Code - Fable 5.1 (max) (with fallback)` carries it (Fable is outside the cohort; the Opus, Sonnet and Haiku records omit it). The code matches by prefix, so behaviour is right. Reword to "may omit, and the match ignores a trailing fallback token".

**L4. E180's minimum-panel sentence is not accurate for the non-discriminating threshold.** The draft says it "needs two rows and otherwise reads 'undefined (panel too small)'". `diagnostics.non_discriminating` silently leaves a leaf unmarked below two observed rows and prints no status. I checked the other strings and minimums against the code and they match (cost-influence status, `INSUFFICIENT_PANEL`, `agreement(min_rows=3)`, `CROSSCHECK_MIN_ROWS = 8`, `MIN_ALLOCATION_ROWS = 3`, `DRIFT_MIN_ROWS = 3`). I50 L2 said "as the code has them". No ranking effect; no row of either ranking is below the minimum.

**L5. The AI Coding Daily duplicate-row rule is under-specified at its edges.** Today only DeepSeek V4.1 Flash 1017 (max) is affected, and both criteria agree on DeepSeek Harness (Bug Hunt record harness; latest test date 2026-10-18 against OpenCode 2026-10-17), so no value changes.
- (i) "stops the build until a recorded reason picks one": `select_aicd` raises with no override field (Bug Hunt has `selectionReason`; tbench.ai says "record which one"), so there is nothing to record into.
- (ii) With two or more rows on the Bug Hunt harness the code falls back to the latest date over all rows, not among the matched-harness rows, which reverses the stated priority.
- (iii) Harness names are compared as casefolded strings across two vocabularies: Bug Hunt's Gemini rows read "Antigravity CLI" while AI Coding Daily's Gemini row reads "Antigravity", and Bug Hunt has "Grok Build CLI (ACP)". A future duplicate on such a model would skip rule 1 silently.
- (iv) The sentence sits in the bullet that also covers Vals and LiveBench, which have neither a per-row test date nor a harness choice, and no code reads duplicates for them (I50's recommendation 2 kept them out).
- (v) The first criterion leans on the Bug Hunt record, itself an editor tie-break "recorded for owner review".
Say AI Coding Daily only; add an override field; define harness equivalence once.

**L6. The E218 search gate reads a free-standing date.** `assemble` checks `evidencePolicy.searchCutoff` only; nothing ties it to a `searchLog` entry, although the draft defines it as "the last date end-user reports were searched" (`draft_figures` reads `max(searchedOn)` separately for the text). A hand-edited date passes with no search. The MiMo end-user search of 2026-10-22, which the draft cites, is not in the log. Derive `searchCutoff` from the log, or fail when they differ.

**L7. The O46 ceiling clock is a hand-set field with no backing artifact and no recomputation.** `capturedOn` renews the clock and the draft says each re-read "recomputes the ceiling". The code never recomputes it: `quotaCredits` and `usdPerBillionCredits` are read nowhere. I recomputed all eight records (credits × rate ÷ fee) and they agree with `valueMultiple` today. The Xiaomi pages are not in the evidence bundle (E159). A ceiling's clock can therefore be restarted by editing a date, which is the editorial restart E144 forbids elsewhere. Have the build recompute and fail on a mismatch, capture the pages into the bundle, or say `capturedOn` is an editor attestation. (The ceiling rows' flag text still reads "owner-named transfer (assumption)", which I48 L5 recorded.)

**L8. Wording.** "In the max-effort ranking MiMo-V2.6-Pro are scored on their own subset workload" (the figure now renders one name; "are"); "on a 8-row panel" (should be "an 8-row panel").

### Checked and sound (no finding)

- Pins against the capture: every cohort row with an exact record is pinned to it (including DeepSeek V4.1 Flash 1017 (max)); "DeepSeek V4.1 Flash" (Codex) is correctly not matched to the 1017 release; the max-effort ranking's Coding Agent Index count (8 of 9; 3 of 15 in the AI Coding Daily ranking) and the admission numbers (255 and 127 alternatives, thresholds 6 and 10) follow.
- The O46 clock: `evidence_date` reads `capturedOn` for `provider_quota_ceiling` routes only, the engine reports 2026-10-23, and the fixtures in `test_plan_routes.py` cover renew and age-to-demotion.
- The AI Coding Daily choice is carried into the leaf provenance with its alternates (52.24 chosen, 52.84 OpenCode).
- The max-effort API leader after the pin fix (DeepSeek 60.39, MiMo-V2.6-Pro 60.29, GPT-6.1 Sol (max) 60.16) matches scores.json; I recomputed DeepSeek's value from the frozen anchors (410.04 → cost score 67.07, quality 58.16, value 60.39).
- Cohort rule: I recomputed the near set from the capture (11 near points, same gaps as the draft). Bar ladders, bar reach (7/5/3 and 12/8/5), source shares (66/34 and 78/22), separability counts (0 of 8 and 1 of 14), plan-row counts (27 and 50) and the transfer/ceiling counts (14 and 48), exchange rates and the E242 tolerances match the data. The SemiAnalysis stage dates are correct.
- `draft_figures check` passes; I found no stale current figure, and no placeholder resolving to the wrong field.

## 2. Methodology design recommendations

1. **One exact-record predicate for cost sources (closes M1).** Parse each captured label once into `(agent, models[], effort|None, fallback|None)`. Define `exact_agent_records(configuration, records) = {r : len(r.models) == 1 ∧ r.model ∈ names(configuration) ∧ r.effort == configuration.effort}`, with the effort-less case defined and O54's high stated for MiMo-V2.6-Pro. Gate: `E = exact(...)`; stop if `E ≠ ∅ ∧ pin ∉ E` (a recorded choice when `|E| > 1`). Use the same function for matching, so the gate and the scoring can never disagree. Add a test per failure mode with real `family` fields. A fixture that asserts the third mixed-label case stops nothing is worth more than another that asserts a stop.
2. **Derive clocks and checks instead of declaring them.** `searchCutoff = max(searchLog.searchedOn)` with a fail on mismatch; a ceiling's multiple recomputed in the build from `quotaCredits`, `usdPerBillionCredits` and the fee, failing on a mismatch; the Xiaomi page captures in the bundle with their capture instants, with `capturedOn` read from the bundle entry.
3. **Make the registry-fact check complete by construction (E265).** The context-regex design misses by one inflection ("captured"). Replace it for current-release timestamps and ISO instants with a literal scan: after stripping placeholders from the source body, no manifest registry value of the form `YYYY-MM-DDTHH:MM:SSZ` may appear anywhere, and a bare registry date may appear only inside a sentence that carries an "at O<n>" or an explicit historical marker. Add a mutation test that types each registry value into the source and expects a failure. This removes the class instead of widening one regex per round.
4. **Decision-record hygiene.** Number every new rule (E267 cost-source match, E268 board duplicate selection), keep review labels in the ledger only (I44 L6), and give each a one-line fixture list in the draft like its neighbours.
5. **A selection-contract object for boards.** `swe_tracks.json` record: `{"selection": {"rule": "bugHuntHarness|latestTested", "reason": null|"…", "alternates": […]}}`; the builder accepts a reason as the override (the way Bug Hunt does) and records which rule fired. Include a harness-equivalence table (Antigravity CLI ≡ Antigravity; Codex CLI ≡ Codex) or compare on a normalised harness key.
6. **State minimum-panel behaviour once.** Either print a status when the non-discriminating test has fewer than two rows, or remove it from E180's list. Keep the string table next to the code (`diagnostics.py`, `anchors.py`) as the single source and render the sentence from it.

## 3. Questions for the owner

None. All recommendations are editor-level; none changes a ranking rule or an owner decision.

## 4. Verdict

VERDICT: HAS FEEDBACK
