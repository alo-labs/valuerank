# Release re-capture of 2026-11-01 (owner decision O145)

On 2026-11-01 the owner decided (O145) that a configuration which leaves AA's rendered frontier and near gap stays a cohort row
for one more release, flagged "left cohort", and chose to apply it now. The release cutoff therefore moved (O65) to
2026-11-01T06:10:00Z, after every capture below, and every source was re-captured.

## Captures (all public pages, no sign-in; web content treated as data)
- AA chart (`chart-capture.json`, `capture_chart.mjs`), 2026-11-01T05:53:05Z: 89 of 89 models selected, 82 circles, one Pareto path
  of 18 vertices, unchanged from 2026-10-30; one far-off point moved (Nemotron 3.5 Super VL $482.18 → $462.70). The rendered
  frontier and near gap give the same 27 configurations.
- Cohort (`cohort.json`): the 27 plus the ten configurations of the 2026-10-25 release's cohort that left at the v5 re-capture:
  Claude Haiku 5.5 (xhigh), Claude Haiku 5.5 (max), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017,
  Gemini 4 Argon, GPT-5.6 Luna (low), Kimi K3.1 Pro, MiMo-V2.6-Pro, MiniMax-M3.1-Flash. AA still plots nine of them; GPT-5.6 Luna
  (low) is no longer plotted and its page has no v5 value (its AA leaves carry logged O36 searches,
  `gpt-5.6-luna-low-search.md`).
- Model pages: 37 (`aa-pages.json`, and `data/aa/aa_v432_snapshot.json` via `python3 -m valuerank.capture_aa` at 05:57:26Z).
- Cost charts with every model selected (`capture_cost_charts_all.js`): FrontierCode 78 of 78, ITBench-AA 45 of 45; Coding Agent
  Index page (`python3 -m valuerank.capture_coding_agents`).
- Third-party boards re-read 06:00–06:03Z (`third-party/`, README there): Bug Hunt, Vals and tbench.ai unchanged; LiveBench's
  release 2026-10-25 edited in place on 2026-10-30 (O147); AI Coding Daily unchanged for the cohort.

## Build
`build_inputs.py` (frontier capture, inventory with `retainedRows`, extract, mapping), `build_third_party.py`,
`research/2026-10-23-swe-benchmarks/build_swe_tracks.py` and `add_track_searches.py`, `extend_livebench.py`, `build_agent_manifest.py`,
`python3 -m valuerank.build_aa_metrics` and `build_tb4`, then `refreeze.py` (previous anchors in `previous-anchors/`) and `regen.sh`.
Owner decisions on the re-read: O147 (LiveBench edit), O148 (MiniMax-M3.1-Flash at max), O149 (MiMo-V2.6-Flash on Vals).
