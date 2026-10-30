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
- [ ] Model pages captured (v5 fields).
- [ ] Coding Agent Index page and ITBench-AA cost chart re-captured.
- [ ] Engine: leaf map (O136), basket (O137), nine-evaluation cost identity.
- [ ] Third-party leaves for new configurations (GPT-6.1 Terra, Gemini 4 Carbon), O36 searches; O135 Flash efforts.
- [ ] Plan routes: Anthropic Max/Ultra rename (2026-10-30), report window at the new cutoff.
- [ ] Re-freeze anchors and bars; draft r156.
