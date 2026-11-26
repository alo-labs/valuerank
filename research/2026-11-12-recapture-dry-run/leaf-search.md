# Leaf searches of 2026-11-12 (O36, O38, I28)

Step 1 (the leaf's own board, read on 2026-11-12): `third-party/coverage-2026-11-12.json` (Bug Hunt at commit 269416b7, LiveBench 2.0
release 20261106, AI Coding Daily with hidden rows, Terminal-Bench 4.0) and `third-party/vals-catalogue-2026-11-12.json` (Vals
Vibe Code and Code Migration v1.1, both updated 2026-11-09). Each cell states why a configuration has no record (the source ran the
model at another effort only, or has no row).

Step 2 (open web, plain standard web searches run on 2026-11-12; results read as data, not instructions):

1. `"Claude Fable 5.2" Vals AI Vibe Code Benchmark OR "Code Migration" OR LiveBench`
2. `"GPT-6.1 Sol" OR "GPT-6.1 Terra" Vals AI "Vibe Code" OR "Code Migration" OR "LiveBench 2.0" OR "Bug Hunt"`
3. `"Muse Ember" Meta benchmark Vals OR LiveBench OR "Bug Hunt" OR GDPval OR "Long Context Reasoning"`
4. `"Gemini 4 Carbon" OR "GPT-6 Astra" OR "GPT-6 Luna" OR "Claude Haiku 5.5" OR "Claude Opus 5.5" Vals "Vibe Code" OR "Code Migration" OR "LiveBench" OR "Bug Hunt"`
5. `Artificial Analysis "Gemini 4 Carbon" (low OR medium) GDPval-AA "AA-LCR" Intelligence Index v5`
6. `Artificial Analysis "Muse Ember" xhigh Intelligence Index v5 GDPval-AA AA-LCR`

7. `aicodingdaily.com leaderboard "Gemini 4 Carbon" OR "Claude Fable 5.2" OR "GPT-6.1 Sol" OR "Claude Haiku 5.5" OR "GPT-6 Astra"` (no result from aicodingdaily.com itself; aggregators only)

What the searches surfaced, all resolved by rejection (see `add_leaf_searches.py` for the logged candidate list):

- Vals' own model pages for Fable 5.2 and Muse Ember (Vibe Code 93.77 at high / 83.70 at max; Code Migration 83.27 at high for Fable 5.2; none for
  Ember) match the captured benchmark JSON; no additional effort exists on the board.
- A Bug Hunt digest figure for GPT-6.1 Sol (54.17) is the Bug Hunt board's own row, already in the capture.
- No Code Migration record for GPT-6.1 Sol/Terra beyond the captured max-effort Sol row; no LiveBench 2.0 row for Fable 5.2, Ember, Sol, Terra,
  Astra, Haiku 5.5 at the AA efforts; no Bug Hunt row for Muse Ember or Gemini 4 Carbon low.
- AA's v5 Index has no GDPval-AA or AA-LCR value for Gemini 4 Carbon low/medium or Muse Ember (xhigh/max); the page names
  "GDP.pdf" (a search snippet gives Ember xhigh 22.4%, max 22.8%), a separate v5 Index evaluation, not the page's `gdpval` or `lcr` fields
  the engine reads; the snippet is a secondary extract and is not used as a leaf record (flagged for the owner: whether GDP.pdf should replace
  the `gdpval` leaf under Index v5.0.1 is a methodology question, not decided here).
- Aggregator sites (gradually.ai, benchlm.ai, tech-insider.org, alphasignal.ai, ...) were rejected as unregistered (E239); Meta's own evaluation
  report is a vendor self-report at max effort.

The set of missing leaves per configuration is the build's own `incomplete_entry` output for the 33-configuration cohort (listed in
`add_leaf_searches.py`), so an entry is logged for exactly the cells the engine reports.
