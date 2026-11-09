# Codex prompt: ValueRank comparison and Pareto charts for nine model-efforts

Prepared 2026-11-09 for the owner. Run it in a local Codex session with model GPT-6.1 Terra at high effort, in a checkout of this repository on branch `claude/wizardly-volta-2ppc48` (commit this file's branch tip or later). Everything between the fences is the prompt. The outputs go to this folder. Nothing in the prompt changes published data.

Review notes (what was checked against the repository before saving): scores.json track names and row fields, the Plan-cost rule (`cost = api_cost / multiple`, `valuerank/value_v3.py`, reproduced for GPT-6.1 Sol max: 1387.03 / 10.772 = 128.76), the OpenCode Go records in `data/plan_cost_routes.json` (`excludedRoutes`), the existing Pareto helper `valuerank/site/viewmodel.py pareto_set` (`valuerank/frontier.py` works on Artificial Analysis points, not on score rows), and that the common-leaves track is a diagnostic ranking (O121) that earns no interval or scenario label.

```text
You are working in a local checkout of the ValueRank repository (alo-labs/valuerank, branch claude/wizardly-volta-2ppc48). Model: GPT-6.1 Terra, high effort. Today is 2026-11-09. The data cutoff of the published scores is 2026-11-01T06:10:00Z.

GOAL
Produce a proper ValueRank comparison, with Pareto charts, of exactly these nine model-efforts:
 1. DeepSeek V4.1 Flash 1017
 2. Claude Haiku 5.5 High
 3. Claude Haiku 5.5 XHigh
 4. Claude Haiku 5.5 Max
 5. GPT-6 Luna Max
 6. GPT-6.1 Terra Low
 7. GPT-6.1 Terra Medium
 8. Claude Sonnet 5.5 Medium
 9. Claude Opus 5.5 Low
"Proper" means: every number comes from the repository's own scoring data and engine; every number is traced to its source; what is missing is stated as missing. Never invent, interpolate or estimate a score for a configuration the repository does not hold. Names in the repo use the form "GPT-6 Luna (max)", "GPT-6.1 Terra (low)", "Claude Haiku 5.5 (xhigh)"; "Luna 6 Max" in this prompt means "GPT-6 Luna (max)".

HARD RULES
- Read-only on published data. Do not edit anything under data/, site/, docs/, scores.md, raw-data.md, methodology.md, AGENTS.md or any file under research/ except the new folder. Do not run npm run build:* or valuerank.build_scores in place. Do not commit, push, open a PR, or change git history or branches.
- Write only into research/comparison-2026-11/ (it exists; this prompt file is in it, leave that file as is). For any what-if that needs the engine, work on a copy of the repository or of data/ under /tmp and say so in the report.
- Run no model benchmarks and call no paid APIs. Do not use, read or print credentials, tokens, cookies, ~/.config files or environment secrets. Reading public web pages is allowed only where a step below says so. Anything you cannot establish from the repository or those pages is reported as "not established".
- Read AGENTS.md and docs/development.md first and follow the repo's conventions. Use absolute dates.
- Do not install packages. If matplotlib or an SVG-to-PNG renderer is unavailable, write the SVG by hand, skip the PNG, and say so in method-log.md.

STEP 1 - LOCATE EACH CONFIGURATION
Source: data/scores.json. Tracks:
 - max-effort main track: scores["v3"]["rows"] (API ranks scores["v3"]["intervals"]["api"], Plan ranks ["plan"]);
 - AI Coding Daily track: scores["v3Tracks"]["aicd"]["rows"];
 - common-leaves track: scores["v3Tracks"]["common"]["rows"]. This one is a diagnostic ranking (O121): "computed like the leading rankings for comparison, but it earns no interval or scenario label and its gates never hold the release". Say so wherever you use it.
Also read scores["v3"]["planRows"] (Plan-basis rows, one per configuration and plan), data/v3_configuration_map.json, data/aa_mapping.json and data/leaf_evidence.json.
Build a table: for each of the nine, which tracks hold it, under which row id and name. Known from a first look, which you must confirm and not trust: the common track holds seven of the nine (all except Sonnet 5.5 Medium and Opus 5.5 Low); Terra Low and Haiku XHigh appear only in the common track; the cohort holds Sonnet 5.5 as an unlabelled "Claude Sonnet 5.5" row and "Claude Sonnet 5.5 (xhigh)", and Opus 5.5 at max, xhigh, high and medium. Check what effort the unlabelled Sonnet 5.5 row represents in the repository's data (aa_mapping.json, v3_configuration_map.json, the AA snapshots in data/aa/) and report it; do not assume it is Medium.

STEP 2 - COMPARE THE SEVEN SCORED ONES
For each scored configuration, in each track where it appears, report from the row: displayed quality with lower/upper and coverage, status and provisional reasons; per-leaf z scores (quality.leaves); API cost, cost score, value and rank (row["api"]); Plan route ID, multiple, grade (controlled / assumption / user_assumption / fallback), Plan cost, value and rank (row["plan"], row["planScore"]); and flags (agentSafety, aaCostCaveat, subset cost, partial components).
Then, on the common-leaves track (the only one holding all seven), make one side-by-side table ordered by API value and a second ordered by Plan value. Quality intervals in the rows are the published-record precision, not sampling uncertainty; do not present them as confidence intervals. For pairwise separability, read the stored diagnostics of the track you are using (scores["v3"]["diagnostics"]["rankSeparability"] for the main track; the "diagnostics" and "intervals" entries inside scores["v3Tracks"][<track>] for the others) and quote what they say about the minimum separable difference and the adjacent pairs. Only call valuerank/value_v3.py rank_separability yourself if the stored output lacks what you need, and then on a /tmp copy. Do not claim an ordering the engine does not support; when two configurations are closer than the stated separable difference, say "not separable".
Show how the ordering changes between API basis and Plan basis, with one sentence per mover (for example: DeepSeek takes the owner-stated OpenCode Go route at 3.0x, an unmeasured provider usage tier; the Haiku rows use an assumed Opus 5.5 multiple of 58.9x on Claude Pro; the Terra and Luna rows reuse the GPT-6.1 Sol multiple of 10.77x on ChatGPT Pro 500). The Plan row shown for a configuration is the route the official comparator chose among its plans; list the other plans' rows from scores["v3"]["planRows"] where they exist so the choice is visible.

STEP 3 - THE TWO UNSCORED ONES
For Sonnet 5.5 Medium and Opus 5.5 Low: state exactly which leaf measurements the scorer needs (see valuerank/value_v3.py and data/leaf_evidence.json) and which are missing for that exact effort. Check data/aa/*.json, data/aa_metrics.json and data/aa_mapping.json for any captured data on those efforts. If, and only if, a complete set of leaf measurements for that exact effort already exists in the repository, run the engine on a /tmp copy to produce a clearly labelled "diagnostic, not published" row. Otherwise do not score them. Give the nearest scored stand-ins (Opus 5.5 Medium; Sonnet 5.5 default and XHigh) in a separate table headed "stand-ins, not the requested efforts", and do not plot them in the Step 5 charts except as grey reference points labelled as stand-ins.

STEP 4 - CAVEATS TO STATE
- Plan multiples are owner-authorised or assumed, not measured, except where the route grade is "controlled" (SemiAnalysis, 2026-10-06). The draft methodology calls the Plan ranking exploratory arithmetic: target-workload multiples are unidentified.
- Keep API basis and Plan basis separate; never rank them together.
- DeepSeek's best plan is OpenCode Go (owner statement, 2026-11-09; owner decision O195 puts third-party plans in scope, but the three-stage plan research for them has not been run). Use OpenCode Go as DeepSeek's Plan row instead of the API-cost fallback:
  * The repo holds: data/plan_cost_routes.json, excludedRoutes, OpenCode Go entries with price $10, excluded on 2026-10-08 as provider-published internal usage allocations, not measured end-user consumption: ids opencode-go-usage-30 (deepseek-v4-flash, $30 of usage, multiple 3.0), opencode-go-usage-15 (deepseek-v4-pro and others, multiple 1.5) and opencode-go-usage-60 (other models). The repo has no record of "OpenCode Go Plus".
  * Compute DeepSeek's Plan cost with the repo's own rule: Plan cost = API cost / multiple (valuerank/value_v3.py, around line 2377; check it first on a row that exists: GPT-6.1 Sol max, 1387.03 / 10.772 = 128.76), using the 3.0 multiple of the deepseek-v4-flash tier. For the common and AI Coding Daily tracks (API cost $446) that gives about $149; for the main track ($531) about $177. Quality and API cost are unchanged.
  * Label that row "owner-stated best plan; provider-published usage tier, not a measured multiple; whether the cohort model DeepSeek V4.1 Flash 1017 maps to the deepseek-v4-flash tier is unconfirmed". Never call it controlled or measured.
  * Also report DeepSeek's API-cost-fallback Plan row (what scores.json holds) beside it, and show how far each other configuration's Plan rank moves because of the OpenCode Go assumption.
  * Look at OpenCode's public pricing and usage pages for the current OpenCode Go and Go Plus price and the usage allowance stated for DeepSeek models. Report what you find with URL and fetch date, labelled "not verified against the repo's evidence rules". Give a computed row for Go Plus only if its DeepSeek allowance is stated in dollars of usage; otherwise report "allowance not stated". Nothing you find replaces the 3.0 multiple in the main tables.
  * Do not edit data/plan_cost_routes.json or any route file. This is a what-if in the report only.
- State which numbers are scores of a displayed record on a published release and which are what-ifs you computed.

STEP 5 - PARETO CHARTS
Use the repository's own frontier rule, not a new one: valuerank/site/viewmodel.py pareto_set(rows, workload, basis) (a point is on the Pareto set if no other point has cost <= and quality >= with at least one strict). valuerank/frontier.py works on Artificial Analysis points and is not the right helper for score rows.
Axes: x = cost in USD on a log scale (lower is better); y = displayed quality (higher is better). Use row["api"]["costUsd"] for the API basis and row["planScore"]["costUsd"] for the Plan basis, and workload = row["cost"]["workload"] of the track.
For each chart compute two things and show both: (a) the frontier among the plotted nine (or seven) points only, and (b) whether each point is on the Pareto set of its full track (all rows of that track on the same workload, via pareto_set). A configuration can be on frontier (a) and off frontier (b); say so.
Charts (all from rows that exist; never plot a point you have not read from the data):
 A. API basis, common-leaves track.
 B. Plan basis, common-leaves track. Use three markers for route grade "controlled", "assumption", and "owner-stated, unmeasured" (DeepSeek on OpenCode Go); add DeepSeek's API-fallback Plan point as a hollow marker joined to its OpenCode Go point by a thin line.
 C. API basis on the max-effort track and on the AI Coding Daily track, as two small multiples with the same axes style, for whichever of the nine appear there.
For every chart: label each point with configuration and effort; draw the frontier as a step line through frontier members only; dim the dominated points; state in the caption the track, workload ID, basis, cutoff date (2026-11-01T06:10:00Z), the source file, and that quality is the displayed record (published-record precision, not sampling uncertainty) and that Plan multiples are owner-authorised or assumed unless the grade is "controlled". Under each chart list the frontier members and dominated points in text, and which neighbouring pairs the stored diagnostics call "not separable".
Produce self-contained SVG (no external fonts or network, readable on light and dark backgrounds) and, if a renderer exists, a PNG at 2x of each. Name them pareto-api-common, pareto-plan-common and pareto-api-by-track in research/comparison-2026-11/. Open each rendered image and check that no label overlaps another or runs off the edge; fix and re-render until none does.
Add the chart data (configuration, track, basis, cost, quality, onFrontierAmongPlotted, onFullTrackParetoSet, dominatedBy) to comparison.json under "pareto", each with a "source".

STEP 6 - SELF-CHECK BEFORE FINISHING
Write a short script (kept in research/comparison-2026-11/check_comparison.py) that reloads data/scores.json and re-derives every number in comparison.json that is not a what-if, and asserts equality with the stored value; run it and record the result in method-log.md. Re-derive the Pareto sets with pareto_set and assert they match the charts' data. List any number you could not re-derive.

OUTPUTS (all in research/comparison-2026-11/)
 1. comparison.md: the tables, the Pareto charts embedded by relative link, a reading of the results (five sentences at most), the caveats, and a "Discrepancies" section for anything in the repository that contradicts this prompt.
 2. comparison.json: all numbers and the Pareto data, each with a "source" (file path plus locator) and a "kind" of "published" or "what-if".
 3. pareto-api-common.svg/.png, pareto-plan-common.svg/.png, pareto-api-by-track.svg/.png.
 4. check_comparison.py and method-log.md (every command you ran with exit status, every file you read that changed a conclusion, and anything you skipped and why).
Finish by printing the paths of all files and a five-line summary. Do not claim a result you did not compute.
```
