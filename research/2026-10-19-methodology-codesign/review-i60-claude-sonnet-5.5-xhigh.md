# Internal review I60 — Claude Sonnet 5.5 (effort xhigh) on draft r118

## 0. Read check

- First line of the draft: `# ValueRank methodology — draft r118`
- Last line of the folded copy (line 1013): `AA's page at the capture and discloses moves (E90 amended), enforces O69's row dates in the build, pins LiveBench's displayed date, retires the inert pre-O51 roster deferrals and records Kimi K3.1 Pro's O66 assumption among the limitations. Every change is recorded with its rationale in the ledger.`
- Last 12 words of the last paragraph: "the limitations. Every change is recorded with its rationale in the ledger."

What else I read: the brief, `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" to the end (O45–O69, E247–E268, I29–I59), the root `AGENTS.md`, my own I59 review, and all 1013 folded lines of the draft in chunks. I also read the code that carries O65–O69 (`value_v3.py` source clocks and capture gates, `research/2026-10-23-swe-benchmarks/build_swe_tracks.py`, `research/2026-10-25-board-reread/rebuild_coverage.py`, `quality.py`, `draft_figures.py`).

What I checked against data and code (all of it passed unless a finding below says otherwise):

- `python3 -m valuerank.draft_figures check` exits 0. I resolved all 187 distinct placeholders (235 uses) against their context. None resolves to the wrong field, and I found no unmarked current figure. The two Medium findings below are hand-written statements about what AA and the Bug Hunt owner publish. They are neither a wrong placeholder nor an unmarked figure, so they lie outside the check's reach by design.
- O65: the frontier chart (09:53:28Z), the Coding Agent Index (09:55:06Z), the cost charts (09:55:32Z) and the 62 model pages (09:56:47Z) are all at or before `observedAt`. The anchor versions are `v3-2026-10-25` and `v3-2026-10-25-aicd`. Both `before-o65` anchor files and both dual-run files exist, and the dual-run "current" values equal the scores now published. The post-cutoff stop in `assemble` covers the Coding Agent Index and cost-chart captures (see L1 for the chart).
- Cohort: I recomputed it from `data/aa_frontier_capture.json` with the AGENTS.md rule (19 vertices, 11 near points with the capture's names, 13 families, 8 frontier and 5 near-only). I also rechecked the near-family primaries (three Astra points at gap 3, so the lower cost picks high), the 9 + 16 − 4 = 21 ranked rows and the 9 excluded.
- O66: `OWNER_STATED_EFFORT` carries Kimi K3.1 Pro at max. The records are Vals max 84.894, LiveBench max, AI Coding Daily "Kimi K3.1 Pro (Max)" 54.63 (= 18.55 + 18.33 + 17.75) and Bug Hunt 36.0 of 105 (runs 36, 42, 30). The High row is unused.
- O67: Kimi's weighted Overall is 641.6 / 9 = 71.29 from `_overall_weights` (Long Agentic 2, Coding 1.5, Design 1.5, others 1). The S1T SD code equals the draft's formula. Old and new `swe_tracks.json` differ only in the LiveBench values of the nine max-effort configurations and Kimi's three new records, which is what the draft says O68 found.
- O68: tbench.ai's 2026-10-25 scrape equals the pinned one (text and rows identical). Cognition's `data.json` equals the pinned file byte for byte (same sha256 `ff00407…`; its re-read HTTP `Last-Modified` is 2026-10-23T21:44:27Z).
- O69: `check_row_date` stops a row dated after the cutoff's day. A cutoff-day row needs a recorded instant before the cutoff. The only such row is Kimi K3.1 Pro (Max) in AI Coding Daily, and it is disclosed in `swe_tracks.json` and in the draft's figure.
- Arithmetic: ladder positions and reach counts (7/5/3 of 9; 13/9/5 of 16), qualifier counts (4 of 5; 8 of 9), exchange rates (3.04 and 2.44 from the anchors 62.86 / 18,703 and 5.84 / 7,116), the noise margins against the thresholds (3.7 ≈ 2.76/0.75; 5.9 ≈ 4.43/0.75), the FrontierCode fill effect (21% × 2.6 = 0.55; 21% × 11.6 = 2.44), 14 of 27 and 48 of 51 assumption plan rows, the 66/34 and 78/22 source shares, the 255 and 127 feasible alternatives, and the fixtures' numbers (91.5% uniform, 86.7% arcsine by simulation, the dominance, interior-witness and admission examples).
- The GDPval move of 54 of 61 pages (−0.83 to +4.10 Elo, Opus 5.5 unchanged at 1866.27) is right as a count. Its interpretation is M1.

## 1. Findings by severity

### Critical

None.

### High

None.

### Medium

**M1. E90's amended premise, that the page's GDPval-AA Elo is "the value AA's pinned Intelligence Index version integrates", is contradicted by the pinned captures (folded lines 479, 490–494; also `value_v3.py:209`).**

The draft says three things:

- The leaf is the Elo "as AA's model page publishes it at the release's capture, the value AA's pinned Intelligence Index version integrates".
- The leaf table row reads "Elo as integrated in the pinned Index version".
- The rating moved for 54 of 61 pages between the 2026-10-23 and 2026-10-25 captures with "no Index version change", "so the freeze is not relied on".

The same label is published as every row's provenance: `"AA GDPval-AA v2.1 Elo as integrated in the pinned Index (E90)"`.

The captures say the opposite. I compared `data/aa/aa_v432_snapshot.json` at the 2026-10-25 cutoff with the committed versions of 2026-10-23 (commit 2e2d8f6, 61 pages) and 2026-10-17 (commit 04a1ff4, 49 common pages):

| Quantity | 10-23 → 10-25 (61 common pages) | 10-17 → 10-23 (49 common pages) |
|---|---|---|
| `model.gdpval` moved | 54 pages, up to +4.10 Elo | 41 pages |
| `intelligenceIndexEvaluations[gdpval-aa].score` moved | 53 pages | not tested |
| `intelligenceIndexEvaluations[aa-briefcase].score` moved | 55 pages | not tested |
| `model.intelligenceIndex` changed | 0 pages | 0 pages |

For example, GPT-6.1 Sol (max) went from 1592.1 to 1596.2 Elo and its Index stayed 51.8332597011541 to every digit the page serves.

The seven pages whose rating did not move are GLM-5.3, Claude Opus 5.5 (max), Claude Sonnet 5.5 (max), Muse Spark 1.3, Muse Wonder, Muse Wonder Full and DeepSeek V4.1 Flash 1017 (max). GDPval-AA carries roughly a tenth of the Index (a least-squares fit of the Index on the ten evaluation scores across the 61 pages gives about 0.13 per z point; the fit is not exact, so I do not claim the formula). A move of +4.10 Elo is +0.205 z, so if the Index integrated the displayed rating, GPT-6.1 Sol's Index would shift by about 0.02 to 0.03, which is visible at that precision.

So the displayed Elo drifts while the Index total never moves, in three captures over eight days. That is what AA's own methodology says (a rating is frozen at a configuration's addition), and the draft quotes it on line 491. The displayed Elo is therefore not shown to be what the Index integrates, and "so the freeze is not relied on" is false for AA's Index.

I59 M1 asked which value the leaf is. I59 Q1 asked the owner whether it should be the model-page value at each cutoff or the value AA froze at addition. The editor closed both by asserting that the page value is the integrated value. The capture does not support that assertion, so the premise of the closure is gone.

Effect: the rule "score the page's Elo at the capture" is clear and executable, and it moves no value by more than about 0.02 points per release (0.205 z × 10% × 0.75 = 0.015). Against the 2026-10-17 capture the cohort rows have drifted by at most 2.35 Elo (GPT-6.1 Sol (max)). The problem is the stated fact. The leaf definition, the provenance string the site and `scores.json` publish, and the E90 rationale all assert something the data refute. A reader or the owner relying on that sentence would think ValueRank's GDPval z equals AA's own Index input. It does not, and the gap accumulates with every refit.

Recommended change:

- Delete the "value the Index integrates" clause and the "so the freeze is not relied on" clause.
- Define the leaf as "the Elo AA's model page displays at the capture (the leaderboard value, which AA refits as models join)".
- State the measured fact that the page's own Index total did not move while the Elo did.
- Change the label in the leaf table and in `value_v3.py:209` to "Elo as displayed on AA's model page at the capture".
- Generate the "54 of 61", the range and the largest z and value effects from a retained previous-capture hash (I59 recommendation 1), together with a build figure "pages whose Elo moved while the Index total did not".
- Put Q1 to the owner again with this evidence (Q1 below).

**M2. Two statements about what the sources publish are false for the pinned captures, and the draft's own conditional rules are therefore not honoured (folded lines 557–558, 561–564, 569–571 against 824–826).**

*(a) The GDPval-AA interval is captured.*

- The draft says "the captured v1 payload does not carry it".
- It says the registry lists the interval as "published, not captured" with a capture task (`value_v3.SOURCE_INTERVALS` and `scores.json` `v3.sourceIntervals`).
- It says "the captured AA Index fields carry no interval".
- It says S1T uses "SD 13.3 Elo for every row", with "each row's own displayed interval would replace the single width once captured".

In fact every model page in the pinned snapshot carries `model.gdpvalInterval` `{lower, upper}`:

- 0 of 49 pages in the 2026-10-17 snapshot,
- 61 of 61 in the 2026-10-23 re-capture (O47),
- 62 of 62 now.

The cohort rows' half-widths are 19.5 to 26.3 Elo. GPT-6.1 Sol (max) is 1574–1619, Claude Opus 5.5 (max) 1840–1892, DeepSeek V4.1 Flash 1017 (max) 1725–1767. No code reads the field, as `grep` over `valuerank/` shows. E174 was true when written (2026-10-20) and became false at the 2026-10-23 re-capture (O47), the first AA re-capture after it.

The draft's own rules now bite twice:

- The interval must be "published beside the leaf as a source interval of unstated level" (line 564). It is not.
- S1T's single ±26 Elo width must be replaced by the row's own interval (line 558). Two faithful implementers would resolve this differently: one keeps the built single width, the other follows "once captured".

Scores are untouched. The "wide" sensitivity in the draft moves the medians in the second decimal (2.77 against 2.76; 4.44 against 4.43).

*(b) Bug Hunt run values are public and captured.* Line 570 says "Bug Hunt's owner publishes run means and counts, not run values". Line 824 (E29) says the estimand uses "owner-published means and run-level results where public". The data side with E29:

- `data/bug_hunt.json` carries `runScores` and `observedRange` on 25 of 54 matched records (Kimi K3.1 Pro 36, 42, 30; GPT-6.1 Sol (max) 44, 42, 47).
- The owner's run notes list the run values. The statement dates from E162 (2026-10-19), but `runScores` has been in the repository since 2026-10-17.

So the draft contradicts itself, and the justification for "every other leaf stays at reporting precision" is wrong as written. The conclusion (no repeatability stream in v1) can stand as a design choice, but not on the premise that the values are not published.

Class and fix: this is the stale hand-written external fact the figure check cannot reach (ledger I46 L5, I48 L6), not a defect of a placeholder or of the lint. A test can reach it. Every registry statement of the form "not captured / carries no / publishes no" should be asserted against the key set of the pinned snapshot or of `bug_hunt.json`, so that a field that appears fails the build until the sentence is updated. Concretely:

- Set the registry status to "captured, level unstated".
- Publish each row's interval beside the leaf.
- Decide S1T's SD (per row from the page interval, still analyst-derived because the level is unstated).
- Reword the Bug Hunt clause to "publishes run values; not used in any v1 stream (E29)".

### Low

**L1. E217 says no AA capture "is taken after the release cutoff, and the build fails otherwise" (lines 877–878), but the chart capture is not in that loop.** `assemble` tests the Coding Agent Index and cost-chart stamps against the cutoff. The chart is only tested for the 7-day gap, and `aa_reconciliation` accepts a capture dated up to one hour after `now` (`age < -1/24`). It is 3 minutes before the cutoff today, so nothing is wrong. Either add the chart to the loop or say "except the chart, with a one-hour tolerance".

**L2. The O69 instant is a hand-typed constant with false precision and an unarchived basis (`CUTOFF_DAY_ROWS`; the `cutoffDayRow` string).** The leaf record says "placed at 2026-10-25T00:58:00Z (the board showed 'tested 9 hours ago' at 2026-10-25T09:58Z)". The committed parse holds "10 hours ago" from the 10:43–10:44Z read, and the 09:58Z reading is not in the repository. A relative age is a bound, not a minute. Record the bound the archived read supports (tested no later than 10:44:11Z minus 9.5 hours, and not before the date tag's UTC midnight), say it is a bound, and cite the archived file. The cutoff is more than 8 hours later either way, so the outcome is unchanged.

**L3. The scope of the O69 clause is wider than its enforcement (lines 874–875).** The text says "a row dated on the cutoff's day". `check_row_date` is called only for AI Coding Daily, the one board whose rows are parsed with a test date. Bug Hunt records carry `reportedOn`, and nothing tests them against the cutoff's day. Either say "an AI Coding Daily row" or run the same test over every record that carries a date. No such Bug Hunt row exists today (the newest is 2026-10-23).

**L4. E90 promises a disclosure item the capture cannot supply (line 493).** The refresh disclosure lists "the anchor model". E181's anchor is "DeepSeek V4.1 Flash (max)" at 1600, which is not one of the 62 captured pages (the captured DeepSeek rows are V4.1 Flash 1017, V4 Pro and V4 Flash). Either capture the anchor's page or drop the item.

**L5. "Its indicative Plan value" has the wrong antecedent after O65 (lines 313–314).** The sentence names MiniMax and Kimi K3.1 Pro and then says "its indicative Plan value is its API cost on the Plan anchors". Kimi K3.1 Pro is ranked in the AI Coding Daily ranking (rank 5 of 16 on API), so its Plan value there is a ranked API-cost row (O13), and an indicative value only beside the max-effort ranking. Say which.

**L6. The evidence bundle's `capturedAt` stamps lag or mislead for derived and editorial artifacts, though line 864 says "each artifact's capture time is in the evidence bundle".**

- `tb4` shows `2026-10-25T09:56:47Z` (the pinned build clock) although the tbench.ai scrape is `2026-10-23T05:35:48Z`.
- `bugHunt` shows `2026-10-23` although the file holds Kimi's record read on 2026-10-25.
- `leafEvidence` shows `2026-10-23` although its search log holds searches dated 2026-10-25.

`sourceClocks` is right for O59 and O60, so no rule is affected. The bundle row should carry the source's own instant. The same fix would let `sourceClocks` print the O68 re-reads of tbench.ai and Cognition (2026-10-25, unchanged). Today they leave no trace in `scores.json`, and Cognition prints "source updated 2026-10-22T22:28:12Z" although the re-read header says 2026-10-23T21:44:27Z with identical content.

**L7. The Kimi row in the Coding Agent Index manifest gives a thinner reason than its neighbour.** `Kimi Code CLI - Kimi K3` is registered as "model outside the cohort (O51)". That is true, but the DeepSeek row says "a different release … not the ranked …" (E188). A K3 row beside the ranked K3.1 Pro is exactly the name trap the closed-world manifest exists for, so say "a different model version, not Kimi K3.1 Pro".

## 2. Methodology design recommendations

1. **Make the GDPval leaf honest (M1), highest priority.**
   - Keep the page-Elo rule, but remove the false premise.
   - Add a retained previous-capture artifact (hash in the bundle) and the build figures `gdpvalMovement` (pages moved, range, largest |Δz| and |Δvalue| over ranked rows) and `gdpvalIndexInvariance` (pages whose Elo moved while the Index total did not).
   - Generate the E90 sentence from them.
   - If the owner prefers the Index-integrated value, pin each configuration's rating at its first capture. That equals the addition-time rating AA says it freezes, it is reproducible from the committed history, and it makes the leaf immune to later refits.
2. **Verify "not captured / publishes no" statements against the pinned data (M2).**
   - Add a registry test that reads the key set of the model-page snapshot, `bug_hunt.json` and the other pinned artifacts, and fails when a field the draft calls absent appears.
   - It would have caught `gdpvalInterval` on 2026-10-23.
   - Pair it with a per-source "fields captured but unused" list in the registry, so an unused field is a visible decision.
3. **Use the captured GDPval interval at the level the draft allows.**
   - Read each row's interval into S1T as a per-row SD (half-width ÷ 1.96, still labelled analyst-derived because the level is unstated).
   - Publish the interval beside the leaf outside every stream, as E174 requires.
   - Keep the single-width ±26 reading as the labelled "wide" sensitivity.
   - Expected effect on the printed separability medians: below 0.01 value points.
4. **Publish a Bug Hunt run-spread diagnostic (optional).** Report, per matched record with `runScores`, the run SD and range beside the binomial plug-in SD S1T uses. It would show whether S1T's 105-bug reading under- or over-states run-to-run spread without adding a stream (E29 already allows it as measurement evidence).
5. **Derive evidence-bundle stamps from the sources.** One field per artifact: the source's own capture instant, and `reReadAt` and `reReadResult` for the O68 re-reads. This closes L6 and makes O68's "re-read every board" auditable from `scores.json`.
6. **Generalise the O69 check (L3).** Give `sourceClocks` an optional `rowDates` summary for every board whose rows carry dates (AI Coding Daily `tested`, Bug Hunt `reportedOn`) and test them with the same function. This was I59 recommendation 2, adopted only for the one board that has dates.

## 3. Questions for the owner

- **Q1 (E90, restated with new evidence).** Across three AA captures (2026-10-17, 10-23, 10-25) the model page's GDPval-AA Elo drifts (41 and then 54 pages moved, up to 4.10 Elo) while every page's Intelligence Index total stays identical to the last digit. Should the GDPval leaf be (a) the Elo the model page displays at each release cutoff (what the build does; the leaf can differ from AA's own Index input by the accumulated drift, today at most 2.35 Elo = 0.12 z for a cohort row since 10-17), or (b) the Elo displayed when the configuration was first captured, which is what the unchanged Index total points to? The answer changes only the label and the pinning rule; no ranking changes today.

## 4. Verdict

Two Medium findings (M1, M2) and seven Low. O65–O69 are implemented faithfully in the draft, the data and the code. The Mediums are stale or unsupported hand-written statements about what AA and the Bug Hunt owner publish, not defects in a rule or a figure, but a round with a Medium is not clean (O56).

VERDICT: HAS FEEDBACK
