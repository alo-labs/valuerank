# Method log

Date: 2026-11-10 (Australia/Sydney). Candidate: branch `claude/wizardly-volta-2ppc48`, commit `9902e1b1cfa52c633fbf058a35720d947c4e65f4`. The tracked score snapshot is v3.0.0, observed 2026-11-01T06:10:00Z.

The first checkout was `main` at `b4ca0b75384a5761ea5eb29b31c067963dd946ba`, with older v1.9.8 data. GitHub's branch search found the intended branch. A no-credential-helper clone in `/tmp/valuerank-comparison-20261110`, local fetch, and `git switch claude/wizardly-volta-2ppc48` all exited 0. The user explicitly directed the switch after the earlier prompt forbade changing branches. The original untracked comparison draft and Optimax ledger were preserved. No pull, commit, push, PR, model benchmark, or in-place build was performed.

The scoring engine is copied into a temporary directory before what-if extraction and checking. The source `scores.json` contains a non-standard nonfinite number; strict output JSON converts nonfinite values to null and documents this in metadata. The checker compares published fields with the captured scores, not the primary benchmark data from which the scores were built.

OpenCode's [Go documentation](https://opencode.ai/docs/console/go/) was fetched on 2026-11-10. Its dollar limits are provider-published limits, not measured user consumption. The page does not identify the 1017 snapshot. Its peak prices equal the captured AA input/output/cache-read prices; the two price bases cannot be converted without assumptions about usage and token categories.

## Validation

- Extractor: `rtk env PYTHONDONTWRITEBYTECODE=1 python3 research/comparison-2026-11/test_extract_comparison.py`, exit 0, 2 tests. The executor reported a prior behavioral red run (2 assertion failures), then green. The orchestrator observed the green run only.
- Chart renderer: `rtk env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_render_pareto` from this directory, exit 0, 5 tests. The executor reported behavioral red runs before fixes; the orchestrator observed green and visually inspected all three 2× PNGs.
- Independent checker: `rtk env PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -p no:cacheprovider -q research/comparison-2026-11/test_check_comparison.py`, exit 0, 4 tests. Executor reported two behavioral red failures before implementation; after a passing baseline, the checker was refactored to import from a temporary copy, and a further temporary-copy test was added retrospectively.
- `rtk env PYTHONDONTWRITEBYTECODE=1 .venv/bin/python research/comparison-2026-11/check_comparison.py`, exit 0: captured records, frozen-anchor what-ifs, ranks and Pareto sets match. The checker does not validate prose, figure rendering, or rerun original benchmarks.
- Some delegated exploratory Python calls omitted the explicit `PYTHONDONTWRITEBYTECODE=1` setting; the executors reported that project imports occurred only from a temporary copy or that only standard library modules were imported. This deviation is not retroactive TDD evidence.

Optimax controller records are in `model-perf/shafqatevo-model-perf.csv`, authorized by the user's instruction to give Optimax precedence over the prompt. Subagent launches were prepared; the host did not supply independent effective model/effort receipts, so their assessments were excluded from performance windows. The host-selected orchestrator was not changed.

The report's 14 published track rows and 21 pairwise differences were independently checked against comparison.json at displayed precision. Individual chart-neighbour separability was not computed; the stored track-wide median cannot establish it. The temporary checkout was removed after the workspace switch.

Final `rtk git status --short` (exit 0):

```text
?? model-perf/
?? research/comparison-2026-11/check_comparison.py
?? research/comparison-2026-11/comparison.json
?? research/comparison-2026-11/comparison.md
?? research/comparison-2026-11/evidence-notes.md
?? research/comparison-2026-11/extract_comparison.py
?? research/comparison-2026-11/method-log.md
?? research/comparison-2026-11/optimax-advisor-request.json
?? research/comparison-2026-11/optimax-executor-high.json
?? research/comparison-2026-11/optimax-executor-medium.json
?? research/comparison-2026-11/pareto-api-by-track.png
?? research/comparison-2026-11/pareto-api-by-track.svg
?? research/comparison-2026-11/pareto-api-common.png
?? research/comparison-2026-11/pareto-api-common.svg
?? research/comparison-2026-11/pareto-plan-common.png
?? research/comparison-2026-11/pareto-plan-common.svg
?? research/comparison-2026-11/render_pareto.py
?? research/comparison-2026-11/test_check_comparison.py
?? research/comparison-2026-11/test_extract_comparison.py
?? research/comparison-2026-11/test_render_pareto.py
```

This log records consequential commands and reported test outcomes; it is not a complete transcript of all tool calls.
