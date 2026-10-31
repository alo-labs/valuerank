# AA Intelligence Index v5 re-capture (owner decisions O132, O136, O137)

AA published Intelligence Index v5 around 2026-10-27, after the 2026-10-25 release cutoff. On 2026-10-30 the owner chose
to re-capture under v5 now (O132), mapped the leaves to their v5 successors at the same weights (O136) and set the v5
basket (O137). All web content was treated as data; no sign-in, cookie consent beyond declining optional cookies, paid
export or private API was used.

## Chart (`v5-chart-capture.json`, `capture_chart.mjs`)

AA Intelligence Index v5 "Intelligence Index vs. Cost to Run Artificial Analysis Intelligence Index" chart,
https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index?eval-cost=intelligence-vs-total-cost,
captured 2026-10-30T22:15:18Z: headless Chromium 1600 x 1200, optional cookies declined, the chart's model selector set
to Select all (28 of 89 → 89 of 89 models), 82 plotted circles and one dotted Pareto path ("0.1 6") with 18 vertices,
each matching a circle centre exactly. The circles ignore pointer events and sit in a translated group, so each was
hovered at its on-screen centre from a neutral point; all 82 tooltips were read and are distinct.

v5's universe is much smaller than v4.3.2's: 89 catalog models selectable on the chart (v4.3.2: 698), 82 plotted.

## Cohort under O51 (rendered frontier plus the 3-point near gap)

Frontier (18): GPT-6 Luna (low, medium, high), Claude Haiku 5.5 (low, medium, high), MiMo-V2.6-Flash, GPT-6.1 Terra
(low, medium, high), GPT-6.1 Sol (medium, high, xhigh, max), GPT-6 Astra (high, xhigh), Claude Opus 5.5 (xhigh with
fallback), Gemini 4 Carbon (high).

Near (9): GPT-6 Luna (xhigh, max), GPT-6.1 Sol (low), GPT-6.1 Terra (xhigh, max), Claude Opus 5.5 (high with fallback,
max with fallback), GPT-6 Astra (max), Claude Sonnet 5.5 (max with fallback).

Left the cohort (no longer on or within 3 points of the rendered v5 frontier): DeepSeek V4.1 Flash 1017, Gemini 4 Argon,
Kimi K3.1 Pro, MiMo-V2.6-Pro, Claude Haiku 5.5 (max), Claude Sonnet 5.5 (xhigh), Claude Opus 5.5 (medium), MiniMax-M3.1-Flash,
GPT-5.6 Luna (low).

## Progress

- [x] Chart captured and cohort derived.
- [x] Model pages captured (v5 fields), 2026-10-30T22:23:33Z; every page has the v5 successor fields. Task counts from AA's methodology: Briefcase 91, AutomationBench 657, GDP.pdf 100, FrontierCode 2.0 132, Terminal-Bench 4.0 66, Terminal-Bench-Science 70, CritPt v2 hard 40, Omniscience v1.1 3,000, HLE-Diamond 1,000. 24 of 27 pages reconstruct AA's total to 1e-6; the three Claude Opus 5.5 rows miss by 0.03-0.04% (E209: partial component).
- [x] Coding Agent Index page (`npm run capture:basket`) and the cost charts with every model selected (`capture_cost_charts_all.js`: FrontierCode 78 of 78 models, 73 bars; ITBench-AA 45 of 45, 43 bars).
- [x] Engine: leaf map (O136), basket (O137), nine-evaluation cost identity; O103 notes captured on every AA surface; the Coding Agent Index manifest re-registered (AA's new label grammar); FrontierCode cross-source and Cognition fills retired.
- [x] Third-party boards re-read 2026-10-30 (`third-party/`); LiveBench release 2026-10-25 pinned (O139); MiMo-V2.6-Flash matched on AI Coding Daily only (O140).
- [x] Third-party data files rebuilt (`build_third_party.py`, `build_swe_tracks.py`, `add_track_searches.py`); O36 search logs dated 2026-10-30.
- [x] Plan routes: GPT-6.1 Terra's O45 routes, Anthropic Max/Ultra aliases and limit record, report window 2026-10-01 to 2026-10-31, the stale Grok report route excluded (E194); price records re-dated.
- [x] Anchors re-frozen (`refreeze.py`); release cutoff 2026-10-31T04:10:00Z (`regen.sh`); draft r156 written.
- [ ] Tests updated; review copy; push.

## Dual run (O12)
`python3 -m valuerank.value_v3 dual-run --previous previous-anchors/v3_frozen.json --track max` at the cutoff stops with "the admitted main workload changed since the anchors were frozen; this is a workload migration": the v4.3.2 anchors price a different workload (GDPval-AA, SciCode, AA-LCR in; FrontierCode 2.0, Terminal-Bench-Science out), so no dual run is computable. The anchors were re-frozen on the v5 cohort (`refreeze.py`); the previous anchor objects are kept in `previous-anchors/`.
