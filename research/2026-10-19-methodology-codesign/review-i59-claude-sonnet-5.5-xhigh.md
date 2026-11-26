# Internal review I59 — Claude Sonnet 5.5 (effort xhigh) on draft r117

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r117`
- Last line of the folded copy (line 1009): `is published, keeps O60 board-level with the cutoff-day row disclosed, and generates the effort equivalents from the registries. Every change is recorded with its rationale in the ledger.`
- Last 12 words of the last paragraph: "the registries. Every change is recorded with its rationale in the ledger."

What else I read: `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" to the end (O45–O69, E247–E268, I29–I58), the root `AGENTS.md`, and all 1009 folded lines of the draft in chunks. I took a sentence-level diff of `draft-r116.src.md` against `draft-r117.src.md` (about seventeen changed sentences plus the revision history), so I know exactly what r117 changed.

What I checked against data and code (all of it passed unless a finding below says otherwise):

- `python3 -m valuerank.draft_figures check` exits 0 with no output.
- O65: the frontier chart (09:53:28Z), the Coding Agent Index capture (09:55:06Z), the cost charts (09:55:32Z) and the 62 model pages (09:56:47Z) are all at or before the cutoff in `scores.json` `observedAt`. The anchor versions are `v3-2026-10-25` and `v3-2026-10-25-aicd`. The two `before-o65` anchor files and both dual-run files exist.
- I recomputed the cohort from `data/aa_frontier_capture.json` with the AGENTS.md rule: 19 rendered vertices, 11 near points (the same 11 names as the capture), 30 rows, 13 families (8 with frontier points, 5 near-only). I also recomputed the near-family primaries (all three GPT-6 Astra points are at gap 3, so the lower cost picks high), the five-class partition of the 9 excluded rows, "first vertex = cheapest of 190 points = $10.63", and the rounded-Index ties (38 x3, 56 x2).
- O66: `exact_match.EFFORT_EQUIVALENTS` and `value_v3.OWNER_STATED_EFFORT` carry Kimi K3.1 Pro at max. The records are Vals `reasoning_effort` max (84.894), LiveBench model metadata max, AI Coding Daily "Kimi K3.1 Pro (Max)" 54.63 (= 18.55 + 18.33 + 17.75, bug column excluded) and Bug Hunt 36.0 of 105 (mean of 3, max). The High row is not used.
- O67: I recomputed Kimi's weighted Overall as 641.6 / 9 = 71.29 with the `_overall_weights` of `categories-20261023.json` (Long Agentic 2, Coding 1.5, Design 1.5, others 1). The S1T SD code (`value_v3.py` around line 2461) equals the draft's formula. `quality.TRACKS` weights are 15 / 11 / 8 / 5 / 6 / 15 and 21 / 17 / 12 / 10, each with the 40 other points (sums to 100).
- O68: the tbench.ai rows of 2026-10-25 equal the pinned scrape (24 of 24 rows identical). Vals, AI Coding Daily (64 rows with hidden ones), Bug Hunt and LiveBench were rebuilt in `research/2026-10-25-board-reread/`.
- O69: every `sourceClocks` entry passes O59 and O60. The only row dated on the cutoff's day is Kimi K3.1 Pro (Max) in AI Coding Daily (`tested` 2026-10-25, "10 hours ago" in the 10:44:11Z capture).
- Figures recomputed from the data: ladders 53.27 / 63.54 / 64.94 (n = 9) and 38.00 / 49.24 / 58.61 (n = 16); bar reach 7 / 5 / 3 and 13 / 9 / 5; qualifier counts 4 against 5 and 8 against 9, with the bar setters Gemini 4 Argon (high) and MiMo-V2.6-Pro; E205 headline bars 63.5 and 52.8 (I rebuilt the family-primary populations by hand); cost allocations (-96% API and -25% Plan in AI Coding Daily, 106% API in max-effort); 14 of 27 and 48 of 51 assumption plan rows; admission 8 of 9 and 3 of 16 with 255 and 127 feasible alternatives; the 66/34 and 78/22 source shares; the exchange rates; and the arithmetic of the normative fixtures (ladder positions for n = 9, 15, 32, the Clopper–Pearson endpoints, the 91.5% uniform figure, the dominance and interior-witness examples, the admission-enumeration examples).

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. E90's standing rule and the sentence r117 added to it contradict each other, so the draft does not say which GDPval-AA value the leaf is (folded lines 490–494).**

The paragraph says four things in a row:

1. The leaf is "AA's published GDPval-AA v2.1 Elo as integrated in the pinned Intelligence Index version, which AA freezes at a configuration's addition".
2. The new sentence says that between the 2026-10-23 and 2026-10-25 captures the published Elo "moved for 54 of 61 captured pages ... no Index version change, which reads as AA's refit of the shared fit as new models joined".
3. The same sentence says "the release scores the 2026-10-25 values".
4. The standing rule that follows says "If AA publishes a refitted rating that differs from the frozen one, the release flags the divergence, keeps the Index-integrated value until the owner decides, and publishes the other value as a diagnostic".

If the 2026-10-25 values are a refit that differs from what AA froze, rule 4 requires keeping the earlier value, flagging and publishing the new one as a diagnostic. That is the opposite of sentence 3. If the model-page `gdpval` field (the pinned field the engine reads, `pages[model.slug=…].model.gdpval`) is not the frozen Index-integrated value, sentence 1 is false for the field the build actually reads. In that case the rule's trigger can never fire on a re-capture, because every re-capture replaces the value. Two faithful implementers would diverge the next time AA moves the ratings: one scores the cutoff capture (as built), the other holds the previous release's values and files the movement as a diagnostic. No ranking changes today (the effect is under 0.02 value points), but this paragraph is the only place that defines what the GDPval leaf is.

This is not the I58 L5 point. I58 asked for a disclosure line and r117 supplied one. The added line now exposes that the premise and the rule were written for a different situation (two AA surfaces disagreeing at one capture), not for movement between captures.

Recommended change:

- Say which AA surface the pinned field reads and that its value at the cutoff is the leaf.
- Mark "AA freezes the Elo at a configuration's addition" as AA's documentation, not observed on the model page.
- Define "the frozen one" (the Index-integrated value, or the value at the previous release's cutoff).
- Restate the flag condition as a between-release movement that the build computes.
- Generate "54 of 61", the Elo range and the largest z/value effect from a retained previous-capture hash. They are hand-typed in a dated sentence, which the figure check does not reach.

### Low

**L1. The E90 effect bound is on the wrong side of its own boundary (line 492).** "under 0.2 z points ... for any row" is stated for a move of up to +4.10 Elo. z = 100 × ΔE / 2000, so +4.10 Elo is 0.205 z points (0.0154 value points). The statement holds only if the largest mover is not a ranked row, and the draft does not say so. Compute the bound over the ranked rows from the retained capture and state it, or say "about 0.2".

**L2. The O69 clause has no stated failing case and no mechanical test (lines 873–875).** "A row dated on the cutoff's day stands when the board's own last update predates that day and the row's age places it before the cutoff instant" is a faithful transcription of O69. Three things are left open:

- It does not say what happens to a row whose age places it after the cutoff instant. O60 is a board-level test, so that row would also stand, which makes the age clause a disclosure trigger only.
- Nothing in the code looks at row dates (`check_source_clocks` is board-level). The disclosure sentence is a hand-typed "today" fact outside the figure check, so a later refresh with another cutoff-day row, or without Kimi's, would leave it stale.
- The evidence record carries only `tested: 2026-10-25`. The relative-age reading that places the row before the cutoff ("10 hours ago" in the 10:44:11Z capture, in the committed HTML) is not in `swe_tracks.json`, and the draft sends the reader to the ledger for it.

The wording "whose date tag falls on the cutoff's day and is inferred from the board's relative age" also reads as if the tag itself were inferred. The tag (`datetime="2026-10-25"`) is explicit; the placement before the cutoff instant is what comes from the relative age. Owner question Q2.

**L3. LiveBench's "source updated" date is not the date the draft says it pins (lines 444–446, 870–872).** The draft says the registry pins the source's displayed release and update dates (E175). `sourceClocks` prints 2026-10-24 for LiveBench. That is the CSV's HTTP `Last-Modified` (24 Oct 2026 15:27:14 GMT), hard-coded as `updated="2026-10-24"` in `rebuild_coverage.py`. The page displays "Last updated 23 October 2026" (a constant in the site bundle). O60 passes with either date, and the later one is the conservative choice, but print both and say which one O60 reads. Otherwise "the source's own last-update date" means different things for Vals and AI Coding Daily (displayed) and LiveBench (a header).

**L4. "All 61 Vals boards ... every board re-read in full on 2026-10-25" overstates the re-read (lines 496–497).** `vals-catalogue-2026-10-25.json` enumerates 61 slugs on 2026-10-25, but only the two boards that feed leaves were re-read. The rest carry "not captured: feeds no ValueRank leaf". Line 428 is accurate ("Vals' two boards"). Reword line 496 to match.

**L5. The report search predates Kimi K3.1 Pro (lines 312–316).** The 2026-10-21 all-provider search lists "Kimi" among the searched providers. K3.1 Pro first appears in the 2026-10-25 capture (its Bug Hunt row is dated 2026-10-23), so no search could have covered it. Its only Plan row is the API-cost fallback. The draft already says MiniMax "joins the next search" for the same reason; say the same for Kimi K3.1 Pro. Related: "Known limitations" (lines 944–945) names MiMo-V2.6-Pro's owner-stated effort (O54) but not Kimi K3.1 Pro's (O66), on which its Bug Hunt, AI Coding Daily, Vals and LiveBench leaves rest.

**L6. The Haiku cost-caveat dates are stale (line 884).** "on 2026-10-17 and again on 2026-10-23" is hand-typed. The 2026-10-25 capture still carries the note (`aaCostCaveat` is set on every Haiku row in scores.json: Haiku (max) in the max-effort ranking, Haiku (high) and (medium) in the AI Coding Daily ranking). Render the observation dates from the captures, or drop the dates.

**L7. The reconciliation inventory carries 18 inert "defer" roster decisions with pre-O51 reasons.** `data/aa_reconciliation_inventory.json` `rosterDecisions` holds 18 entries, all `defer`, re-stamped `reviewedAt` 2026-10-25T09:56:00Z. Their text says, for example, that the Claude Haiku 5.5 family "is represented in the primary ranking by its selected configuration (claude-haiku-5-5-xhigh)" and that GPT-6 Luna (high) and GPT-6.1 Sol (high) are "alternate configuration[s]". Under O51 and the draft (line 147, "nothing is chosen among a family's efforts") each is a cohort row, several are ranked in the AI Coding Daily ranking, and the Haiku xhigh row is excluded, not ranked.

The report ignores them: every `rosterDecision` is null and the deferred lists are empty, because they apply only to rows with no roster match. They are the one record class AGENTS.md names for deferral ("a dated, reasoned roster decision"), so the artifact now says 18 rows are deferred while the draft says none is. This is the kind of stale label the ledger has parked for the release tidy-up (I46 L6, I49). I list it because the O65 refresh re-stamped them. Delete them, or reword them, and add a gate that a roster decision cannot name a configuration that maps to a roster entry.

**L8. `family_groups` in the frontier capture omits Kimi K3.1 Pro.** `data/aa_frontier_capture.json` has `universe.model_families: 8` but seven `family_groups` (no Kimi K3.1 Pro). Nothing reads the field, but the file is a bundled capture artifact. Add the group.

**L9. Wording and record.**

- Line 871 has a stray space before the semicolon ("last-update date ;").
- Lines 314–315 repeat "SuperGrok Heavy ... SuperGrok Heavy's is for Grok 4.7".
- The r117 revision-history entry (line 1008) omits two adopted I58 changes: the GDPval-AA move disclosure (L5) and the pinned LiveBench URL (L7).
- `tests/test_tracks.py` line 42 still says LiveBench Overall "is the mean of seven categories" (the test uses unit weights, so it passes).
- The generated `methodology.md` cohort paragraph cites "(O54)" for AA's effort-less configurations including Kimi K3.1 Pro (that is O66).

## 2. Methodology design recommendations

1. **Make the GDPval leaf definition match the pinned field (M1, L1).** Add a retained "previous capture" artifact (hash in the evidence bundle) and a build figure `gdpvalMovement` = rows moved, minimum and maximum ΔElo, and the maximum |Δz| and |Δvalue| over ranked rows on each ranking (|Δvalue| = 0.75 × 0.10 × ΔE × 100 / 2000). Render the E90 sentence from it. Define the flag as "any ranked row moved by more than X between releases", with X chosen so that today's movement is below it. Then decide, in the same sentence, whether a flagged move holds the old value or merely discloses (Q1).
2. **Make the O69 disclosure mechanical (L2).** Extend `sourceClocks` with `rowsOnCutoffDay`: every record whose own date tag (AI Coding Daily `tested`, Bug Hunt `reportedOn`, any Vals or LiveBench row date) falls on date(V), plus the capture instant and the board's relative-age text where the board states one. Generate the specification sentence from it with a placeholder, and have the check fail when a cutoff-day row is not in the sentence. State the outcome for a row whose age places it after the cutoff.
3. **Print the date O60 reads for each board (L3).** Add `updatedBasis` (displayed text / HTTP Last-Modified / board metadata) to each `sourceClocks` entry, so the conservative choice for LiveBench is visible.
4. **Evidence-bundle hygiene on every cutoff move (L7, L8).** Add a gate that a `rosterDecisions` entry never names a configuration that maps to a roster entry, and that `family_groups` count equals `universe.model_families`. Both are one-line checks and stop the artifact from re-asserting pre-O51 text at each refresh.
5. **Cheap, optional, and not adopted unless the owner wants it:** a build figure for the gap between each board's stated update date and its newest row date (AI Coding Daily is the only board with row dates; today the gap is +1 day). The owner already chose to disclose rather than test row dates in O69; this would only make the disclosure data-driven.

## 3. Questions for the owner

- **Q1 (E90).** The AA model-page GDPval-AA Elo moved for 54 of 61 pages between 2026-10-23 and 2026-10-25 with no Index version change. For each release, should the leaf be the model-page value at that cutoff (what the build does), or the value AA froze at the configuration's addition, with later movement only disclosed? The answer decides whether E90's "keeps the Index-integrated value until the owner decides" rule is rewritten around a between-release flag or kept as written.
- **Q2 (O69).** For a row dated on the cutoff's day whose age places it after the cutoff instant, should it still stand (O60 board-level only, the age clause only triggering disclosure) or should the build stop? Today no such row exists, so no score depends on the answer.

## 4. Verdict

VERDICT: HAS FEEDBACK
