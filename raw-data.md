# ValueRank v3.1.0 Raw Data

**Updated:** November 26, 2026 · methodology 3.1.0

Every input behind the published scores, with the artifact and locator that holds it. Generated from the committed snapshots in [data/](data/); nothing here is edited by hand.

## Quality leaf inputs

| Configuration | Leaf | Raw value | Unit | Score z | Evaluated configuration / agent | Evidence |
|---|---|---:|---|---:|---|---|
| GPT-6.1 Sol (max) | FrontierCode 2.0 | 0.406262878787879 | fraction | 40.63 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.frontierCode20` |
| GPT-6.1 Sol (max) | Terminal-Bench 4.1 (AA run) | 56.565656565656596 | percent | 56.57 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.terminalBench41` |
| GPT-6.1 Sol (max) | Bug Hunt Bench | 109.6 | bugs fixed, planted plus unplanted (O163, O170) | 78.74 | GPT-6.1 Sol (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol].fixedOf105 + models[modelId=gpt-6.1-sol].extras` |
| GPT-6.1 Sol (max) | Vibe Code Bench v1.1 (Vals) | 75.101 | percent | 75.10 | openai/gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=vibeCode].value` |
| GPT-6.1 Sol (max) | Code Migration v1.1 (Vals) | 77.324 | percent | 77.32 | openai/gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=codeMigration].value` |
| GPT-6.1 Sol (max) | LiveBench 2.0 Overall | 81.17 | percent | 81.17 | gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=livebench2Overall].value` |
| GPT-6.1 Sol (max) | GDPval-AA v2.1 | 1607.38 | Elo | 55.37 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.gdpval` |
| GPT-6.1 Sol (max) | GDP.pdf (AA) | 0.31 | fraction | 31.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.gdpPdfAllPass` |
| GPT-6.1 Sol (max) | AutomationBench-AA | 0.6486844882398171 | fraction | 64.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.automationBenchPartialScore` |
| GPT-6.1 Sol (max) | AA-Omniscience v1.1 | 42.03333333333333 | AA Omniscience Index | 71.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.omniscience` |
| GPT-6.1 Sol (max) | AA-LCR v1.1 | 0.83 | fraction | 83.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.lcr` |
| GPT-6.1 Sol (max) | HLE-Diamond | 0.588 | fraction | 58.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.hleDiamond` |
| GPT-6.1 Sol (max) | Terminal-Bench-Science 0.1 | 0.580952380952381 | fraction | 58.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.terminalBenchScience` |
| GPT-6.1 Sol (max) | CritPt v2 (hard subset) | 0.695 | fraction | 69.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.critptAgenticHard` |
| Claude Sonnet 5.5 (max) | FrontierCode 2.0 | 0.419350252525253 | fraction | 41.94 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.frontierCode20` |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.1 (AA run) | 65.1515151515151 | percent | 65.15 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.terminalBench41` |
| Claude Sonnet 5.5 (max) | Bug Hunt Bench | 77.6 | bugs fixed, planted plus unplanted (O163, O170) | 55.75 | Sonnet 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5].fixedOf105 + models[modelId=claude-sonnet-5-5].extras` |
| Claude Sonnet 5.5 (max) | Vibe Code Bench v1.1 (Vals) | 80.88 | percent | 80.88 | anthropic/claude-sonnet-5-5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=vibeCode].value` |
| Claude Sonnet 5.5 (max) | Code Migration v1.1 (Vals) | 86.875 | percent | 86.88 | anthropic/claude-sonnet-5-5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=codeMigration].value` |
| Claude Sonnet 5.5 (max) | LiveBench 2.0 Overall | 76.79 | percent | 76.79 | claude-sonnet-5.5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=livebench2Overall].value` |
| Claude Sonnet 5.5 (max) | GDPval-AA v2.1 | 1837.82 | Elo | 66.89 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.gdpval` |
| Claude Sonnet 5.5 (max) | GDP.pdf (AA) | 0.258 | fraction | 25.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.gdpPdfAllPass` |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | 0.7176882128193995 | fraction | 71.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (max) | AA-Omniscience v1.1 | 30.466666666666665 | AA Omniscience Index | 65.23 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.omniscience` |
| Claude Sonnet 5.5 (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.lcr` |
| Claude Sonnet 5.5 (max) | HLE-Diamond | 0.533 | fraction | 53.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.hleDiamond` |
| Claude Sonnet 5.5 (max) | Terminal-Bench-Science 0.1 | 0.533333333333333 | fraction | 53.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.terminalBenchScience` |
| Claude Sonnet 5.5 (max) | CritPt v2 (hard subset) | 0.59 | fraction | 59.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.critptAgenticHard` |
| Claude Opus 5.5 (max) | FrontierCode 2.0 | 0.468989141414141 | fraction | 46.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.frontierCode20` |
| Claude Opus 5.5 (max) | Terminal-Bench 4.1 (AA run) | 59.09090909090911 | percent | 59.09 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.terminalBench41` |
| Claude Opus 5.5 (max) | Bug Hunt Bench | 50.7 | bugs fixed, planted plus unplanted (O163, O170) | 36.42 | Opus 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5].fixedOf105 + models[modelId=claude-opus-5-5].extras` |
| Claude Opus 5.5 (max) | Vibe Code Bench v1.1 (Vals) | 78.49 | percent | 78.49 | anthropic/claude-opus-5-5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=vibeCode].value` |
| Claude Opus 5.5 (max) | Code Migration v1.1 (Vals) | 81.012 | percent | 81.01 | anthropic/claude-opus-5-5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=codeMigration].value` |
| Claude Opus 5.5 (max) | LiveBench 2.0 Overall | 83.44 | percent | 83.44 | claude-opus-5.5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=livebench2Overall].value` |
| Claude Opus 5.5 (max) | GDPval-AA v2.1 | 1866.27 | Elo | 68.31 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.gdpval` |
| Claude Opus 5.5 (max) | GDP.pdf (AA) | 0.262 | fraction | 26.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.gdpPdfAllPass` |
| Claude Opus 5.5 (max) | AutomationBench-AA | 0.6953868128636069 | fraction | 69.54 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.automationBenchPartialScore` |
| Claude Opus 5.5 (max) | AA-Omniscience v1.1 | 48.13333333333333 | AA Omniscience Index | 74.07 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.omniscience` |
| Claude Opus 5.5 (max) | AA-LCR v1.1 | 0.846666666666667 | fraction | 84.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.lcr` |
| Claude Opus 5.5 (max) | HLE-Diamond | 0.679 | fraction | 67.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.hleDiamond` |
| Claude Opus 5.5 (max) | Terminal-Bench-Science 0.1 | 0.59047619047619 | fraction | 59.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.terminalBenchScience` |
| Claude Opus 5.5 (max) | CritPt v2 (hard subset) | 0.68 | fraction | 68.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.critptAgenticHard` |
| GPT-6 Astra (max) | FrontierCode 2.0 | 0.42374797979798 | fraction | 42.37 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.frontierCode20` |
| GPT-6 Astra (max) | Terminal-Bench 4.1 (AA run) | 59.09090909090911 | percent | 59.09 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.terminalBench41` |
| GPT-6 Astra (max) | Bug Hunt Bench | 100 | bugs fixed, planted plus unplanted (O163, O170) | 71.84 | GPT-6 Astra (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-astra].fixedOf105 + models[modelId=gpt-6-astra].extras` |
| GPT-6 Astra (max) | Vibe Code Bench v1.1 (Vals) | 77.535 | percent | 77.53 | openai/gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=vibeCode].value` |
| GPT-6 Astra (max) | Code Migration v1.1 (Vals) | 80.579 | percent | 80.58 | openai/gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=codeMigration].value` |
| GPT-6 Astra (max) | LiveBench 2.0 Overall | 84.25 | percent | 84.25 | gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=livebench2Overall].value` |
| GPT-6 Astra (max) | GDPval-AA v2.1 | 1587.03 | Elo | 54.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.gdpval` |
| GPT-6 Astra (max) | GDP.pdf (AA) | 0.31 | fraction | 31.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.gdpPdfAllPass` |
| GPT-6 Astra (max) | AutomationBench-AA | 0.6849174806688876 | fraction | 68.49 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.automationBenchPartialScore` |
| GPT-6 Astra (max) | AA-Omniscience v1.1 | 42.43333333333333 | AA Omniscience Index | 71.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.omniscience` |
| GPT-6 Astra (max) | AA-LCR v1.1 | 0.806666666666667 | fraction | 80.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.lcr` |
| GPT-6 Astra (max) | HLE-Diamond | 0.638 | fraction | 63.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.hleDiamond` |
| GPT-6 Astra (max) | Terminal-Bench-Science 0.1 | 0.633333333333333 | fraction | 63.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.terminalBenchScience` |
| GPT-6 Astra (max) | CritPt v2 (hard subset) | 0.705 | fraction | 70.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.critptAgenticHard` |
| GPT-6 Luna (max) | FrontierCode 2.0 | 0.251747727272727 | fraction | 25.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.frontierCode20` |
| GPT-6 Luna (max) | Terminal-Bench 4.1 (AA run) | 12.6262626262626 | percent | 12.63 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.terminalBench41` |
| GPT-6 Luna (max) | Bug Hunt Bench | 41.0 | bugs fixed, planted plus unplanted (O163, O170) | 29.45 | GPT-6 Luna (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-luna].fixedOf105 + models[modelId=gpt-6-luna].extras` |
| GPT-6 Luna (max) | Vibe Code Bench v1.1 (Vals) | 65.315 | percent | 65.31 | openai/gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=vibeCode].value` |
| GPT-6 Luna (max) | Code Migration v1.1 (Vals) | 46.669 | percent | 46.67 | openai/gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=codeMigration].value` |
| GPT-6 Luna (max) | LiveBench 2.0 Overall | 60.42 | percent | 60.42 | gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=livebench2Overall].value` |
| GPT-6 Luna (max) | GDPval-AA v2.1 | 1443.09 | Elo | 47.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.gdpval` |
| GPT-6 Luna (max) | GDP.pdf (AA) | 0.228 | fraction | 22.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.gdpPdfAllPass` |
| GPT-6 Luna (max) | AutomationBench-AA | 0.5316814034483175 | fraction | 53.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.automationBenchPartialScore` |
| GPT-6 Luna (max) | AA-Omniscience v1.1 | -8.266666666666667 | AA Omniscience Index | 45.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.omniscience` |
| GPT-6 Luna (max) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.lcr` |
| GPT-6 Luna (max) | HLE-Diamond | 0.222 | fraction | 22.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.hleDiamond` |
| GPT-6 Luna (max) | Terminal-Bench-Science 0.1 | 0.0857142857142857 | fraction | 8.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.terminalBenchScience` |
| GPT-6 Luna (max) | CritPt v2 (hard subset) | 0.425 | fraction | 42.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.critptAgenticHard` |
| GPT-6.1 Sol (high) | FrontierCode 2.0 | 0.36737297979798 | fraction | 36.74 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.frontierCode20` |
| GPT-6.1 Sol (high) | Terminal-Bench 4.1 (AA run) | 51.010101010101 | percent | 51.01 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.terminalBench41` |
| GPT-6.1 Sol (high) | Bug Hunt Bench | 76.5 | bugs fixed, planted plus unplanted (O163, O170) | 54.96 | GPT-6.1 Sol (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-high].fixedOf105 + models[modelId=gpt-6.1-sol-high].extras` |
| GPT-6.1 Sol (high) | AI Coding Daily (excl. bug finding) | 74.83 | points of 80 | 93.54 | GPT-6.1-Sol (High) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-high, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (high) | GDPval-AA v2.1 | 1521.54 | Elo | 51.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.gdpval` |
| GPT-6.1 Sol (high) | GDP.pdf (AA) | 0.32 | fraction | 32.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.gdpPdfAllPass` |
| GPT-6.1 Sol (high) | AutomationBench-AA | 0.6449523732184466 | fraction | 64.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.automationBenchPartialScore` |
| GPT-6.1 Sol (high) | AA-Omniscience v1.1 | 41 | AA Omniscience Index | 70.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.omniscience` |
| GPT-6.1 Sol (high) | AA-LCR v1.1 | 0.823333333333333 | fraction | 82.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.lcr` |
| GPT-6.1 Sol (high) | HLE-Diamond | 0.519 | fraction | 51.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.hleDiamond` |
| GPT-6.1 Sol (high) | Terminal-Bench-Science 0.1 | 0.461904761904762 | fraction | 46.19 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.terminalBenchScience` |
| GPT-6.1 Sol (high) | CritPt v2 (hard subset) | 0.685 | fraction | 68.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.critptAgenticHard` |
| GPT-6.1 Sol (medium) | FrontierCode 2.0 | 0.333875757575758 | fraction | 33.39 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.frontierCode20` |
| GPT-6.1 Sol (medium) | Terminal-Bench 4.1 (AA run) | 47.979797979798 | percent | 47.98 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.terminalBench41` |
| GPT-6.1 Sol (medium) | Bug Hunt Bench | 59.5 | bugs fixed, planted plus unplanted (O163, O170) | 42.74 | GPT-6.1 Sol (medium effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-medium].fixedOf105 + models[modelId=gpt-6.1-sol-medium].extras` |
| GPT-6.1 Sol (medium) | AI Coding Daily (excl. bug finding) | 73.94 | points of 80 | 92.42 | GPT-6.1-Sol (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-medium, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (medium) | GDPval-AA v2.1 | 1463.95 | Elo | 48.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.gdpval` |
| GPT-6.1 Sol (medium) | GDP.pdf (AA) | 0.3 | fraction | 30.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.gdpPdfAllPass` |
| GPT-6.1 Sol (medium) | AutomationBench-AA | 0.6257350970435687 | fraction | 62.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.automationBenchPartialScore` |
| GPT-6.1 Sol (medium) | AA-Omniscience v1.1 | 40.166666666666664 | AA Omniscience Index | 70.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.omniscience` |
| GPT-6.1 Sol (medium) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.lcr` |
| GPT-6.1 Sol (medium) | HLE-Diamond | 0.46 | fraction | 46.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.hleDiamond` |
| GPT-6.1 Sol (medium) | Terminal-Bench-Science 0.1 | 0.371428571428571 | fraction | 37.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.terminalBenchScience` |
| GPT-6.1 Sol (medium) | CritPt v2 (hard subset) | 0.67 | fraction | 67.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.critptAgenticHard` |
| Claude Opus 5.5 (high) | FrontierCode 2.0 | 0.359278535353535 | fraction | 35.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.frontierCode20` |
| Claude Opus 5.5 (high) | Terminal-Bench 4.1 (AA run) | 56.0606060606061 | percent | 56.06 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.terminalBench41` |
| Claude Opus 5.5 (high) | Bug Hunt Bench | 42.4 | bugs fixed, planted plus unplanted (O163, O170) | 30.46 | Opus 5.5 (high effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5-high].fixedOf105 + models[modelId=claude-opus-5-5-high].extras` |
| Claude Opus 5.5 (high) | AI Coding Daily (excl. bug finding) | 75.85 | points of 80 | 94.81 | Opus 5.5 (High) | `data/swe_tracks.json` `records[modelId=claude-opus-5-5-high, leaf=aiCodingDaily].value` |
| Claude Opus 5.5 (high) | GDPval-AA v2.1 | 1708.61 | Elo | 60.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.gdpval` |
| Claude Opus 5.5 (high) | GDP.pdf (AA) | 0.288 | fraction | 28.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.gdpPdfAllPass` |
| Claude Opus 5.5 (high) | AutomationBench-AA | 0.6320677483186213 | fraction | 63.21 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.automationBenchPartialScore` |
| Claude Opus 5.5 (high) | AA-Omniscience v1.1 | 42.36666666666667 | AA Omniscience Index | 71.18 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.omniscience` |
| Claude Opus 5.5 (high) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.lcr` |
| Claude Opus 5.5 (high) | HLE-Diamond | 0.556 | fraction | 55.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.hleDiamond` |
| Claude Opus 5.5 (high) | Terminal-Bench-Science 0.1 | 0.49047619047619 | fraction | 49.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.terminalBenchScience` |
| Claude Opus 5.5 (high) | CritPt v2 (hard subset) | 0.595 | fraction | 59.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.critptAgenticHard` |
| GPT-6.1 Terra (max) | FrontierCode 2.0 | 0.42075101010101 | fraction | 42.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.frontierCode20` |
| GPT-6.1 Terra (max) | Terminal-Bench 4.1 (AA run) | 56.565656565656596 | percent | 56.57 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.terminalBench41` |
| GPT-6.1 Terra (max) | Bug Hunt Bench | 88.7 | bugs fixed, planted plus unplanted (O163, O170) | 63.72 | GPT-6.1 Terra (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra].fixedOf105 + models[modelId=gpt-6.1-terra].extras` |
| GPT-6.1 Terra (max) | AI Coding Daily (excl. bug finding) | 69.19 | points of 80 | 86.49 | GPT-6.1-Terra (Max) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (max) | GDPval-AA v2.1 | 1474.92 | Elo | 48.75 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.gdpval` |
| GPT-6.1 Terra (max) | GDP.pdf (AA) | 0.286 | fraction | 28.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.gdpPdfAllPass` |
| GPT-6.1 Terra (max) | AutomationBench-AA | 0.6016762327257726 | fraction | 60.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.automationBenchPartialScore` |
| GPT-6.1 Terra (max) | AA-Omniscience v1.1 | 29.566666666666666 | AA Omniscience Index | 64.78 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.omniscience` |
| GPT-6.1 Terra (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.lcr` |
| GPT-6.1 Terra (max) | HLE-Diamond | 0.473 | fraction | 47.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.hleDiamond` |
| GPT-6.1 Terra (max) | Terminal-Bench-Science 0.1 | 0.576190476190476 | fraction | 57.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.terminalBenchScience` |
| GPT-6.1 Terra (max) | CritPt v2 (hard subset) | 0.68 | fraction | 68.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.critptAgenticHard` |
| GPT-6.1 Terra (high) | FrontierCode 2.0 | 0.37457904040404 | fraction | 37.46 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.frontierCode20` |
| GPT-6.1 Terra (high) | Terminal-Bench 4.1 (AA run) | 42.9292929292929 | percent | 42.93 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.terminalBench41` |
| GPT-6.1 Terra (high) | Bug Hunt Bench | 16.4 | bugs fixed, planted plus unplanted (O163, O170) | 11.78 | GPT-6.1 Terra (high effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-high].fixedOf105 + models[modelId=gpt-6.1-terra-high].extras` |
| GPT-6.1 Terra (high) | AI Coding Daily (excl. bug finding) | 61.46 | points of 80 | 76.83 | GPT-6.1-Terra (High) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra-high, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (high) | GDPval-AA v2.1 | 1354.59 | Elo | 42.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.gdpval` |
| GPT-6.1 Terra (high) | GDP.pdf (AA) | 0.28 | fraction | 28.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.gdpPdfAllPass` |
| GPT-6.1 Terra (high) | AutomationBench-AA | 0.584605963496433 | fraction | 58.46 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.automationBenchPartialScore` |
| GPT-6.1 Terra (high) | AA-Omniscience v1.1 | 27.766666666666666 | AA Omniscience Index | 63.88 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.omniscience` |
| GPT-6.1 Terra (high) | AA-LCR v1.1 | 0.823333333333333 | fraction | 82.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.lcr` |
| GPT-6.1 Terra (high) | HLE-Diamond | 0.354 | fraction | 35.40 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.hleDiamond` |
| GPT-6.1 Terra (high) | Terminal-Bench-Science 0.1 | 0.333333333333333 | fraction | 33.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.terminalBenchScience` |
| GPT-6.1 Terra (high) | CritPt v2 (hard subset) | 0.615 | fraction | 61.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.critptAgenticHard` |
| GPT-6.1 Terra (xhigh) | FrontierCode 2.0 | 0.368595202020202 | fraction | 36.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.frontierCode20` |
| GPT-6.1 Terra (xhigh) | Terminal-Bench 4.1 (AA run) | 46.4646464646465 | percent | 46.46 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.terminalBench41` |
| GPT-6.1 Terra (xhigh) | Bug Hunt Bench | 28.3 | bugs fixed, planted plus unplanted (O163, O170) | 20.33 | GPT-6.1 Terra (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-xhigh].fixedOf105 + models[modelId=gpt-6.1-terra-xhigh].extras` |
| GPT-6.1 Terra (xhigh) | AI Coding Daily (excl. bug finding) | 63.7 | points of 80 | 79.62 | GPT-6.1-Terra (Xhigh) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra-xhigh, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (xhigh) | GDPval-AA v2.1 | 1416.62 | Elo | 45.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.gdpval` |
| GPT-6.1 Terra (xhigh) | GDP.pdf (AA) | 0.266 | fraction | 26.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.gdpPdfAllPass` |
| GPT-6.1 Terra (xhigh) | AutomationBench-AA | 0.5992855956353923 | fraction | 59.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.automationBenchPartialScore` |
| GPT-6.1 Terra (xhigh) | AA-Omniscience v1.1 | 28.933333333333334 | AA Omniscience Index | 64.47 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.omniscience` |
| GPT-6.1 Terra (xhigh) | AA-LCR v1.1 | 0.816666666666667 | fraction | 81.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.lcr` |
| GPT-6.1 Terra (xhigh) | HLE-Diamond | 0.423 | fraction | 42.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.hleDiamond` |
| GPT-6.1 Terra (xhigh) | Terminal-Bench-Science 0.1 | 0.419047619047619 | fraction | 41.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.terminalBenchScience` |
| GPT-6.1 Terra (xhigh) | CritPt v2 (hard subset) | 0.605 | fraction | 60.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.critptAgenticHard` |
| GPT-6.1 Terra (medium) | FrontierCode 2.0 | 0.345359343434343 | fraction | 34.54 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.frontierCode20` |
| GPT-6.1 Terra (medium) | Terminal-Bench 4.1 (AA run) | 31.818181818181802 | percent | 31.82 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.terminalBench41` |
| GPT-6.1 Terra (medium) | Bug Hunt Bench | 14.6 | bugs fixed, planted plus unplanted (O163, O170) | 10.49 | GPT-6.1 Terra (medium effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-medium].fixedOf105 + models[modelId=gpt-6.1-terra-medium].extras` |
| GPT-6.1 Terra (medium) | AI Coding Daily (excl. bug finding) | 62.57 | points of 80 | 78.21 | GPT-6.1-Terra (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra-medium, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (medium) | GDPval-AA v2.1 | 1324.62 | Elo | 41.23 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.gdpval` |
| GPT-6.1 Terra (medium) | GDP.pdf (AA) | 0.284 | fraction | 28.40 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.gdpPdfAllPass` |
| GPT-6.1 Terra (medium) | AutomationBench-AA | 0.5780171778957812 | fraction | 57.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.automationBenchPartialScore` |
| GPT-6.1 Terra (medium) | AA-Omniscience v1.1 | 26.6 | AA Omniscience Index | 63.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.omniscience` |
| GPT-6.1 Terra (medium) | AA-LCR v1.1 | 0.806666666666667 | fraction | 80.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.lcr` |
| GPT-6.1 Terra (medium) | HLE-Diamond | 0.313 | fraction | 31.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.hleDiamond` |
| GPT-6.1 Terra (medium) | Terminal-Bench-Science 0.1 | 0.247619047619048 | fraction | 24.76 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.terminalBenchScience` |
| GPT-6.1 Terra (medium) | CritPt v2 (hard subset) | 0.565 | fraction | 56.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.critptAgenticHard` |
| GPT-6.1 Sol (low) | FrontierCode 2.0 | 0.201560858585859 | fraction | 20.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.frontierCode20` |
| GPT-6.1 Sol (low) | Terminal-Bench 4.1 (AA run) | 30.808080808080803 | percent | 30.81 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.terminalBench41` |
| GPT-6.1 Sol (low) | Bug Hunt Bench | 46.5 | bugs fixed, planted plus unplanted (O163, O170) | 33.41 | GPT-6.1 Sol (low effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-low].fixedOf105 + models[modelId=gpt-6.1-sol-low].extras` |
| GPT-6.1 Sol (low) | AI Coding Daily (excl. bug finding) | 70.8 | points of 80 | 88.50 | GPT-6.1-Sol (Low) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-low, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (low) | GDPval-AA v2.1 | 1322.31 | Elo | 41.12 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.gdpval` |
| GPT-6.1 Sol (low) | GDP.pdf (AA) | 0.27 | fraction | 27.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.gdpPdfAllPass` |
| GPT-6.1 Sol (low) | AutomationBench-AA | 0.5257088964747538 | fraction | 52.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.automationBenchPartialScore` |
| GPT-6.1 Sol (low) | AA-Omniscience v1.1 | 38 | AA Omniscience Index | 69.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.omniscience` |
| GPT-6.1 Sol (low) | AA-LCR v1.1 | 0.84 | fraction | 84.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.lcr` |
| GPT-6.1 Sol (low) | HLE-Diamond | 0.382 | fraction | 38.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.hleDiamond` |
| GPT-6.1 Sol (low) | Terminal-Bench-Science 0.1 | 0.10952380952381 | fraction | 10.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.terminalBenchScience` |
| GPT-6.1 Sol (low) | CritPt v2 (hard subset) | 0.625 | fraction | 62.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.critptAgenticHard` |
| GPT-6 Luna (max) | AI Coding Daily (excl. bug finding) | 68.02 | points of 80 | 85.03 | GPT-6-Luna (Max) | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=aiCodingDaily].value` |
| Claude Haiku 5.5 (high) | FrontierCode 2.0 | 0.232000505050505 | fraction | 23.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.frontierCode20` |
| Claude Haiku 5.5 (high) | Terminal-Bench 4.1 (AA run) | 22.727272727272698 | percent | 22.73 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.terminalBench41` |
| Claude Haiku 5.5 (high) | Bug Hunt Bench | 20 | bugs fixed, planted plus unplanted (O163, O170) | 14.37 | Haiku 5.5 (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-high].fixedOf105 + models[modelId=claude-haiku-5-5-high].extras` |
| Claude Haiku 5.5 (high) | AI Coding Daily (excl. bug finding) | 69.78 | points of 80 | 87.22 | Haiku 5.5 (High) | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-high, leaf=aiCodingDaily].value` |
| Claude Haiku 5.5 (high) | GDPval-AA v2.1 | 1423.04 | Elo | 46.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.gdpval` |
| Claude Haiku 5.5 (high) | GDP.pdf (AA) | 0.172 | fraction | 17.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.gdpPdfAllPass` |
| Claude Haiku 5.5 (high) | AutomationBench-AA | 0.3372685311767238 | fraction | 33.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (high) | AA-Omniscience v1.1 | 5.3 | AA Omniscience Index | 52.65 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.omniscience` |
| Claude Haiku 5.5 (high) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.lcr` |
| Claude Haiku 5.5 (high) | HLE-Diamond | 0.237 | fraction | 23.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.hleDiamond` |
| Claude Haiku 5.5 (high) | Terminal-Bench-Science 0.1 | 0.1 | fraction | 10.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.terminalBenchScience` |
| Claude Haiku 5.5 (high) | CritPt v2 (hard subset) | 0.45 | fraction | 45.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.critptAgenticHard` |
| GPT-6 Astra (high) | FrontierCode 2.0 | 0.401351515151515 | fraction | 40.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.frontierCode20` |
| GPT-6 Astra (high) | Terminal-Bench 4.1 (AA run) | 54.5454545454545 | percent | 54.55 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.terminalBench41` |
| GPT-6 Astra (high) | Bug Hunt Bench | 75.0 | bugs fixed, planted plus unplanted (O163, O170) | 53.88 | GPT-6 Astra (high effort) | `data/bug_hunt.json` `models[modelId=gpt-6-astra-high].fixedOf105 + models[modelId=gpt-6-astra-high].extras` |
| GPT-6 Astra (high) | AI Coding Daily (excl. bug finding) | 75.24 | points of 80 | 94.05 | GPT-6-Astra (High) | `data/swe_tracks.json` `records[modelId=gpt-6-astra-high, leaf=aiCodingDaily].value` |
| GPT-6 Astra (high) | GDPval-AA v2.1 | 1538.22 | Elo | 51.91 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.gdpval` |
| GPT-6 Astra (high) | GDP.pdf (AA) | 0.31 | fraction | 31.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.gdpPdfAllPass` |
| GPT-6 Astra (high) | AutomationBench-AA | 0.666122174975011 | fraction | 66.61 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.automationBenchPartialScore` |
| GPT-6 Astra (high) | AA-Omniscience v1.1 | 44.56666666666667 | AA Omniscience Index | 72.28 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.omniscience` |
| GPT-6 Astra (high) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.lcr` |
| GPT-6 Astra (high) | HLE-Diamond | 0.593 | fraction | 59.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.hleDiamond` |
| GPT-6 Astra (high) | Terminal-Bench-Science 0.1 | 0.595238095238095 | fraction | 59.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.terminalBenchScience` |
| GPT-6 Astra (high) | CritPt v2 (hard subset) | 0.715 | fraction | 71.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.critptAgenticHard` |
| GPT-6 Luna (xhigh) | FrontierCode 2.0 | 0.184238888888889 | fraction | 18.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.frontierCode20` |
| GPT-6 Luna (xhigh) | Terminal-Bench 4.1 (AA run) | 8.08080808080808 | percent | 8.08 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.terminalBench41` |
| GPT-6 Luna (xhigh) | Bug Hunt Bench | 26.0 | bugs fixed, planted plus unplanted (O163, O170) | 18.68 | GPT-6 Luna (xhigh effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-xhigh].fixedOf105 + models[modelId=gpt-6-luna-xhigh].extras` |
| GPT-6 Luna (xhigh) | AI Coding Daily (excl. bug finding) | 65.94 | points of 80 | 82.42 | GPT-6-Luna (Xhigh) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-xhigh, leaf=aiCodingDaily].value` |
| GPT-6 Luna (xhigh) | GDPval-AA v2.1 | 1374.09 | Elo | 43.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.gdpval` |
| GPT-6 Luna (xhigh) | GDP.pdf (AA) | 0.186 | fraction | 18.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.gdpPdfAllPass` |
| GPT-6 Luna (xhigh) | AutomationBench-AA | 0.47800686767566575 | fraction | 47.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.automationBenchPartialScore` |
| GPT-6 Luna (xhigh) | AA-Omniscience v1.1 | -12.966666666666667 | AA Omniscience Index | 43.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.omniscience` |
| GPT-6 Luna (xhigh) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.lcr` |
| GPT-6 Luna (xhigh) | HLE-Diamond | 0.189 | fraction | 18.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.hleDiamond` |
| GPT-6 Luna (xhigh) | Terminal-Bench-Science 0.1 | 0.0523809523809524 | fraction | 5.24 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.terminalBenchScience` |
| GPT-6 Luna (xhigh) | CritPt v2 (hard subset) | 0.37 | fraction | 37.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.critptAgenticHard` |
| Claude Haiku 5.5 (medium) | FrontierCode 2.0 | 0.16091994949495 | fraction | 16.09 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.frontierCode20` |
| Claude Haiku 5.5 (medium) | Terminal-Bench 4.1 (AA run) | 15.151515151515198 | percent | 15.15 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.terminalBench41` |
| Claude Haiku 5.5 (medium) | Bug Hunt Bench | 16.0 | bugs fixed, planted plus unplanted (O163, O170) | 11.49 | Haiku 5.5 (medium effort) | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-medium].fixedOf105 + models[modelId=claude-haiku-5-5-medium].extras` |
| Claude Haiku 5.5 (medium) | AI Coding Daily (excl. bug finding) | 68.75 | points of 80 | 85.94 | Haiku 5.5 (Medium) | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-medium, leaf=aiCodingDaily].value` |
| Claude Haiku 5.5 (medium) | GDPval-AA v2.1 | 1282.93 | Elo | 39.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.gdpval` |
| Claude Haiku 5.5 (medium) | GDP.pdf (AA) | 0.152 | fraction | 15.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.gdpPdfAllPass` |
| Claude Haiku 5.5 (medium) | AutomationBench-AA | 0.2858961481429316 | fraction | 28.59 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (medium) | AA-Omniscience v1.1 | 4.166666666666667 | AA Omniscience Index | 52.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.omniscience` |
| Claude Haiku 5.5 (medium) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.lcr` |
| Claude Haiku 5.5 (medium) | HLE-Diamond | 0.168 | fraction | 16.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.hleDiamond` |
| Claude Haiku 5.5 (medium) | Terminal-Bench-Science 0.1 | 0.0714285714285714 | fraction | 7.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.terminalBenchScience` |
| Claude Haiku 5.5 (medium) | CritPt v2 (hard subset) | 0.305 | fraction | 30.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.critptAgenticHard` |
| GPT-6 Luna (high) | FrontierCode 2.0 | 0.186015151515152 | fraction | 18.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.frontierCode20` |
| GPT-6 Luna (high) | Terminal-Bench 4.1 (AA run) | 5.05050505050505 | percent | 5.05 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.terminalBench41` |
| GPT-6 Luna (high) | Bug Hunt Bench | 18.0 | bugs fixed, planted plus unplanted (O163, O170) | 12.93 | GPT-6 Luna (high effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-high].fixedOf105 + models[modelId=gpt-6-luna-high].extras` |
| GPT-6 Luna (high) | AI Coding Daily (excl. bug finding) | 63.26 | points of 80 | 79.08 | GPT-6-Luna (High) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-high, leaf=aiCodingDaily].value` |
| GPT-6 Luna (high) | GDPval-AA v2.1 | 1350.13 | Elo | 42.51 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.gdpval` |
| GPT-6 Luna (high) | GDP.pdf (AA) | 0.182 | fraction | 18.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.gdpPdfAllPass` |
| GPT-6 Luna (high) | AutomationBench-AA | 0.4782449139916615 | fraction | 47.82 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.automationBenchPartialScore` |
| GPT-6 Luna (high) | AA-Omniscience v1.1 | -12.8 | AA Omniscience Index | 43.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.omniscience` |
| GPT-6 Luna (high) | AA-LCR v1.1 | 0.793333333333333 | fraction | 79.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.lcr` |
| GPT-6 Luna (high) | HLE-Diamond | 0.156 | fraction | 15.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.hleDiamond` |
| GPT-6 Luna (high) | Terminal-Bench-Science 0.1 | 0.0285714285714286 | fraction | 2.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.terminalBenchScience` |
| GPT-6 Luna (high) | CritPt v2 (hard subset) | 0.31 | fraction | 31.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.critptAgenticHard` |
| GPT-6 Luna (medium) | FrontierCode 2.0 | 0.127693181818182 | fraction | 12.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.frontierCode20` |
| GPT-6 Luna (medium) | Terminal-Bench 4.1 (AA run) | 2.52525252525253 | percent | 2.53 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.terminalBench41` |
| GPT-6 Luna (medium) | Bug Hunt Bench | 4.0 | bugs fixed, planted plus unplanted (O163, O170) | 2.87 | GPT-6 Luna (medium effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-medium].fixedOf105 + models[modelId=gpt-6-luna-medium].extras` |
| GPT-6 Luna (medium) | AI Coding Daily (excl. bug finding) | 55.03 | points of 80 | 68.79 | GPT-6-Luna (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-medium, leaf=aiCodingDaily].value` |
| GPT-6 Luna (medium) | GDPval-AA v2.1 | 1270.63 | Elo | 38.53 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.gdpval` |
| GPT-6 Luna (medium) | GDP.pdf (AA) | 0.138 | fraction | 13.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.gdpPdfAllPass` |
| GPT-6 Luna (medium) | AutomationBench-AA | 0.4046136879135791 | fraction | 40.46 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.automationBenchPartialScore` |
| GPT-6 Luna (medium) | AA-Omniscience v1.1 | -13.566666666666666 | AA Omniscience Index | 43.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.omniscience` |
| GPT-6 Luna (medium) | AA-LCR v1.1 | 0.783333333333333 | fraction | 78.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.lcr` |
| GPT-6 Luna (medium) | HLE-Diamond | 0.151 | fraction | 15.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.hleDiamond` |
| GPT-6 Luna (medium) | Terminal-Bench-Science 0.1 | 0.0142857142857143 | fraction | 1.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.terminalBenchScience` |
| GPT-6 Luna (medium) | CritPt v2 (hard subset) | 0.275 | fraction | 27.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.critptAgenticHard` |
| GPT-6.1 Sol (xhigh) | FrontierCode 2.0 | 0.385190909090909 | fraction | 38.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.frontierCode20` |
| GPT-6.1 Sol (xhigh) | Terminal-Bench 4.1 (AA run) | 53.5353535353535 | percent | 53.54 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.terminalBench41` |
| GPT-6.1 Sol (xhigh) | Bug Hunt Bench | 99.4 | bugs fixed, planted plus unplanted (O163, O170) | 71.41 | GPT-6.1 Sol (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-xhigh].fixedOf105 + models[modelId=gpt-6.1-sol-xhigh].extras` |
| GPT-6.1 Sol (xhigh) | GDPval-AA v2.1 | 1562.07 | Elo | 53.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.gdpval` |
| GPT-6.1 Sol (xhigh) | GDP.pdf (AA) | 0.318 | fraction | 31.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.gdpPdfAllPass` |
| GPT-6.1 Sol (xhigh) | AutomationBench-AA | 0.6657372141364344 | fraction | 66.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.automationBenchPartialScore` |
| GPT-6.1 Sol (xhigh) | AA-Omniscience v1.1 | 42.36666666666667 | AA Omniscience Index | 71.18 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.omniscience` |
| GPT-6.1 Sol (xhigh) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.lcr` |
| GPT-6.1 Sol (xhigh) | HLE-Diamond | 0.558 | fraction | 55.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.hleDiamond` |
| GPT-6.1 Sol (xhigh) | Terminal-Bench-Science 0.1 | 0.504761904761905 | fraction | 50.48 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.terminalBenchScience` |
| GPT-6.1 Sol (xhigh) | CritPt v2 (hard subset) | 0.695 | fraction | 69.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.critptAgenticHard` |
| Claude Fable 5.2 (high) | FrontierCode 2.0 | 0.491275757575758 | fraction | 49.13 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.frontierCode20` |
| Claude Fable 5.2 (high) | Terminal-Bench 4.1 (AA run) | 60.1010101010101 | percent | 60.10 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.terminalBench41` |
| Claude Fable 5.2 (high) | Bug Hunt Bench | 59.5 | bugs fixed, planted plus unplanted (O163, O170) | 42.74 | Fable 5.2 (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=claude-fable-5-2-high].fixedOf105 + models[modelId=claude-fable-5-2-high].extras` |
| Claude Fable 5.2 (high) | GDPval-AA v2.1 | 1718.56 | Elo | 60.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.gdpval` |
| Claude Fable 5.2 (high) | GDP.pdf (AA) | 0.218 | fraction | 21.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.gdpPdfAllPass` |
| Claude Fable 5.2 (high) | AutomationBench-AA | 0.7135975994544773 | fraction | 71.36 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.automationBenchPartialScore` |
| Claude Fable 5.2 (high) | AA-Omniscience v1.1 | 64.03333333333333 | AA Omniscience Index | 82.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.omniscience` |
| Claude Fable 5.2 (high) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.lcr` |
| Claude Fable 5.2 (high) | HLE-Diamond | 0.738 | fraction | 73.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.hleDiamond` |
| Claude Fable 5.2 (high) | Terminal-Bench-Science 0.1 | 0.7 | fraction | 70.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.terminalBenchScience` |
| Claude Fable 5.2 (high) | CritPt v2 (hard subset) | 0.73 | fraction | 73.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-high].model.critptAgenticHard` |
| Claude Opus 5.5 (xhigh) | FrontierCode 2.0 | 0.442261111111111 | fraction | 44.23 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.frontierCode20` |
| Claude Opus 5.5 (xhigh) | Terminal-Bench 4.1 (AA run) | 59.5959595959596 | percent | 59.60 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.terminalBench41` |
| Claude Opus 5.5 (xhigh) | Bug Hunt Bench | 49.3 | bugs fixed, planted plus unplanted (O163, O170) | 35.42 | Opus 5.5 (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5-xhigh].fixedOf105 + models[modelId=claude-opus-5-5-xhigh].extras` |
| Claude Opus 5.5 (xhigh) | GDPval-AA v2.1 | 1835.95 | Elo | 66.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.gdpval` |
| Claude Opus 5.5 (xhigh) | GDP.pdf (AA) | 0.266 | fraction | 26.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.gdpPdfAllPass` |
| Claude Opus 5.5 (xhigh) | AutomationBench-AA | 0.6495283516401527 | fraction | 64.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.automationBenchPartialScore` |
| Claude Opus 5.5 (xhigh) | AA-Omniscience v1.1 | 43.13333333333333 | AA Omniscience Index | 71.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.omniscience` |
| Claude Opus 5.5 (xhigh) | AA-LCR v1.1 | 0.846666666666667 | fraction | 84.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.lcr` |
| Claude Opus 5.5 (xhigh) | HLE-Diamond | 0.64 | fraction | 64.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.hleDiamond` |
| Claude Opus 5.5 (xhigh) | Terminal-Bench-Science 0.1 | 0.619047619047619 | fraction | 61.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.terminalBenchScience` |
| Claude Opus 5.5 (xhigh) | CritPt v2 (hard subset) | 0.675 | fraction | 67.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.critptAgenticHard` |
| Claude Fable 5.2 (xhigh) | FrontierCode 2.0 | 0.475810858585859 | fraction | 47.58 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.frontierCode20` |
| Claude Fable 5.2 (xhigh) | Terminal-Bench 4.1 (AA run) | 61.616161616161605 | percent | 61.62 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.terminalBench41` |
| Claude Fable 5.2 (xhigh) | Bug Hunt Bench | 65.7 | bugs fixed, planted plus unplanted (O163, O170) | 47.20 | Fable 5.2 (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-fable-5-2-xhigh].fixedOf105 + models[modelId=claude-fable-5-2-xhigh].extras` |
| Claude Fable 5.2 (xhigh) | GDPval-AA v2.1 | 1752.56 | Elo | 62.63 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.gdpval` |
| Claude Fable 5.2 (xhigh) | GDP.pdf (AA) | 0.214 | fraction | 21.40 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.gdpPdfAllPass` |
| Claude Fable 5.2 (xhigh) | AutomationBench-AA | 0.7416293165236524 | fraction | 74.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.automationBenchPartialScore` |
| Claude Fable 5.2 (xhigh) | AA-Omniscience v1.1 | 64.76666666666667 | AA Omniscience Index | 82.38 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.omniscience` |
| Claude Fable 5.2 (xhigh) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.lcr` |
| Claude Fable 5.2 (xhigh) | HLE-Diamond | 0.758 | fraction | 75.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.hleDiamond` |
| Claude Fable 5.2 (xhigh) | Terminal-Bench-Science 0.1 | 0.676190476190476 | fraction | 67.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.terminalBenchScience` |
| Claude Fable 5.2 (xhigh) | CritPt v2 (hard subset) | 0.735 | fraction | 73.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2-xhigh].model.critptAgenticHard` |
| Claude Fable 5.2 (max) | FrontierCode 2.0 | 0.487597222222222 | fraction | 48.76 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.frontierCode20` |
| Claude Fable 5.2 (max) | Terminal-Bench 4.1 (AA run) | 61.616161616161605 | percent | 61.62 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.terminalBench41` |
| Claude Fable 5.2 (max) | Bug Hunt Bench | 82.7 | bugs fixed, planted plus unplanted (O163, O170) | 59.41 | Fable 5.2 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-fable-5-2].fixedOf105 + models[modelId=claude-fable-5-2].extras` |
| Claude Fable 5.2 (max) | GDPval-AA v2.1 | 1830.14 | Elo | 66.51 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.gdpval` |
| Claude Fable 5.2 (max) | GDP.pdf (AA) | 0.242 | fraction | 24.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.gdpPdfAllPass` |
| Claude Fable 5.2 (max) | AutomationBench-AA | 0.7642233832611831 | fraction | 76.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.automationBenchPartialScore` |
| Claude Fable 5.2 (max) | AA-Omniscience v1.1 | 66.76666666666667 | AA Omniscience Index | 83.38 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.omniscience` |
| Claude Fable 5.2 (max) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.lcr` |
| Claude Fable 5.2 (max) | HLE-Diamond | 0.802 | fraction | 80.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.hleDiamond` |
| Claude Fable 5.2 (max) | Terminal-Bench-Science 0.1 | 0.733333333333333 | fraction | 73.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.terminalBenchScience` |
| Claude Fable 5.2 (max) | CritPt v2 (hard subset) | 0.765 | fraction | 76.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-2].model.critptAgenticHard` |
| GPT-6 Astra (xhigh) | FrontierCode 2.0 | 0.414029545454545 | fraction | 41.40 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.frontierCode20` |
| GPT-6 Astra (xhigh) | Terminal-Bench 4.1 (AA run) | 60.1010101010101 | percent | 60.10 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.terminalBench41` |
| GPT-6 Astra (xhigh) | Bug Hunt Bench | 96.0 | bugs fixed, planted plus unplanted (O163, O170) | 68.97 | GPT-6 Astra (xhigh effort) | `data/bug_hunt.json` `models[modelId=gpt-6-astra-xhigh].fixedOf105 + models[modelId=gpt-6-astra-xhigh].extras` |
| GPT-6 Astra (xhigh) | GDPval-AA v2.1 | 1571.28 | Elo | 53.56 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.gdpval` |
| GPT-6 Astra (xhigh) | GDP.pdf (AA) | 0.322 | fraction | 32.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.gdpPdfAllPass` |
| GPT-6 Astra (xhigh) | AutomationBench-AA | 0.6717778020215392 | fraction | 67.18 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.automationBenchPartialScore` |
| GPT-6 Astra (xhigh) | AA-Omniscience v1.1 | 43.666666666666664 | AA Omniscience Index | 71.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.omniscience` |
| GPT-6 Astra (xhigh) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.lcr` |
| GPT-6 Astra (xhigh) | HLE-Diamond | 0.615 | fraction | 61.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.hleDiamond` |
| GPT-6 Astra (xhigh) | Terminal-Bench-Science 0.1 | 0.547619047619048 | fraction | 54.76 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.terminalBenchScience` |
| GPT-6 Astra (xhigh) | CritPt v2 (hard subset) | 0.71 | fraction | 71.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.critptAgenticHard` |
| Claude Haiku 5.5 (xhigh) | FrontierCode 2.0 | 0.299334090909091 | fraction | 29.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.frontierCode20` |
| Claude Haiku 5.5 (xhigh) | Terminal-Bench 4.1 (AA run) | 28.7878787878788 | percent | 28.79 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.terminalBench41` |
| Claude Haiku 5.5 (xhigh) | Bug Hunt Bench | 25.0 | bugs fixed, planted plus unplanted (O163, O170) | 17.96 | Haiku 5.5 (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5].fixedOf105 + models[modelId=claude-haiku-5-5].extras` |
| Claude Haiku 5.5 (xhigh) | GDPval-AA v2.1 | 1523.13 | Elo | 51.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.gdpval` |
| Claude Haiku 5.5 (xhigh) | GDP.pdf (AA) | 0.182 | fraction | 18.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.gdpPdfAllPass` |
| Claude Haiku 5.5 (xhigh) | AutomationBench-AA | 0.35953889773428194 | fraction | 35.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (xhigh) | AA-Omniscience v1.1 | 7.833333333333333 | AA Omniscience Index | 53.92 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.omniscience` |
| Claude Haiku 5.5 (xhigh) | AA-LCR v1.1 | 0.783333333333333 | fraction | 78.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.lcr` |
| Claude Haiku 5.5 (xhigh) | HLE-Diamond | 0.288 | fraction | 28.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.hleDiamond` |
| Claude Haiku 5.5 (xhigh) | Terminal-Bench-Science 0.1 | 0.180952380952381 | fraction | 18.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.terminalBenchScience` |
| Claude Haiku 5.5 (xhigh) | CritPt v2 (hard subset) | 0.475 | fraction | 47.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.critptAgenticHard` |
| GPT-6.1 Terra (low) | FrontierCode 2.0 | 0.244852272727273 | fraction | 24.49 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.frontierCode20` |
| GPT-6.1 Terra (low) | Terminal-Bench 4.1 (AA run) | 15.151515151515198 | percent | 15.15 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.terminalBench41` |
| GPT-6.1 Terra (low) | Bug Hunt Bench | 11 | bugs fixed, planted plus unplanted (O163, O170) | 7.90 | GPT-6.1 Terra (low effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-low].fixedOf105 + models[modelId=gpt-6.1-terra-low].extras` |
| GPT-6.1 Terra (low) | GDPval-AA v2.1 | 1204.89 | Elo | 35.24 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.gdpval` |
| GPT-6.1 Terra (low) | GDP.pdf (AA) | 0.256 | fraction | 25.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.gdpPdfAllPass` |
| GPT-6.1 Terra (low) | AutomationBench-AA | 0.5624828754079192 | fraction | 56.25 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.automationBenchPartialScore` |
| GPT-6.1 Terra (low) | AA-Omniscience v1.1 | 22.933333333333334 | AA Omniscience Index | 61.47 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.omniscience` |
| GPT-6.1 Terra (low) | AA-LCR v1.1 | 0.81 | fraction | 81.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.lcr` |
| GPT-6.1 Terra (low) | HLE-Diamond | 0.249 | fraction | 24.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.hleDiamond` |
| GPT-6.1 Terra (low) | Terminal-Bench-Science 0.1 | 0.0761904761904762 | fraction | 7.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.terminalBenchScience` |
| GPT-6.1 Terra (low) | CritPt v2 (hard subset) | 0.505 | fraction | 50.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.critptAgenticHard` |
| Claude Haiku 5.5 (low) | FrontierCode 2.0 | 0.0803666666666667 | fraction | 8.04 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.frontierCode20` |
| Claude Haiku 5.5 (low) | Terminal-Bench 4.1 (AA run) | 12.6262626262626 | percent | 12.63 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.terminalBench41` |
| Claude Haiku 5.5 (low) | Bug Hunt Bench | 13.0 | bugs fixed, planted plus unplanted (O163, O170) | 9.34 | Haiku 5.5 (low effort) | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-low].fixedOf105 + models[modelId=claude-haiku-5-5-low].extras` |
| Claude Haiku 5.5 (low) | GDPval-AA v2.1 | 1130.34 | Elo | 31.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.gdpval` |
| Claude Haiku 5.5 (low) | GDP.pdf (AA) | 0.112 | fraction | 11.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.gdpPdfAllPass` |
| Claude Haiku 5.5 (low) | AutomationBench-AA | 0.22910812181110643 | fraction | 22.91 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (low) | AA-Omniscience v1.1 | 2.1666666666666665 | AA Omniscience Index | 51.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.omniscience` |
| Claude Haiku 5.5 (low) | AA-LCR v1.1 | 0.72 | fraction | 72.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.lcr` |
| Claude Haiku 5.5 (low) | HLE-Diamond | 0.141 | fraction | 14.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.hleDiamond` |
| Claude Haiku 5.5 (low) | Terminal-Bench-Science 0.1 | 0.019047619047619 | fraction | 1.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.terminalBenchScience` |
| Claude Haiku 5.5 (low) | CritPt v2 (hard subset) | 0.215 | fraction | 21.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.critptAgenticHard` |
| GPT-6 Luna (low) | FrontierCode 2.0 | 0.0219545454545455 | fraction | 2.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.frontierCode20` |
| GPT-6 Luna (low) | Terminal-Bench 4.1 (AA run) | 0.0 | percent | 0.00 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.terminalBench41` |
| GPT-6 Luna (low) | Bug Hunt Bench | 13.0 | bugs fixed, planted plus unplanted (O163, O170) | 9.34 | GPT-6 Luna (low effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-low].fixedOf105 + models[modelId=gpt-6-luna-low].extras` |
| GPT-6 Luna (low) | GDPval-AA v2.1 | 1040.73 | Elo | 27.04 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.gdpval` |
| GPT-6 Luna (low) | GDP.pdf (AA) | 0.09 | fraction | 9.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.gdpPdfAllPass` |
| GPT-6 Luna (low) | AutomationBench-AA | 0.12049187272690505 | fraction | 12.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.automationBenchPartialScore` |
| GPT-6 Luna (low) | AA-Omniscience v1.1 | -18.1 | AA Omniscience Index | 40.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.omniscience` |
| GPT-6 Luna (low) | AA-LCR v1.1 | 0.74 | fraction | 74.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.lcr` |
| GPT-6 Luna (low) | HLE-Diamond | 0.102 | fraction | 10.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.hleDiamond` |
| GPT-6 Luna (low) | Terminal-Bench-Science 0.1 | 0.00952380952380952 | fraction | 0.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.terminalBenchScience` |
| GPT-6 Luna (low) | CritPt v2 (hard subset) | 0.095 | fraction | 9.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.critptAgenticHard` |

## Leaf gap fills and searches (O36)

Leaves a ranked configuration takes from beyond its primary source, in the order a newer AA capture, another party's run of the same benchmark on the exact configuration, then the model provider's published result (O36/O37). Tbench.ai Terminal-Bench rows used as gap fills are in the leaf inputs above with their agent.

| Configuration | Leaf | Value | Unit | Source type | Publisher | Evaluated configuration | Benchmark version | Metric (E237) | Source |
|---|---|---:|---|---|---|---|---|---|---|

Exhaustive searches for the leaves a cohort configuration still lacks (each within 7 days of the cutoff; the configuration is listed, not ranked). The sources searched are in [data/leaf_evidence.json](data/leaf_evidence.json).

| Configuration | Leaf | Searched | Result | Sources checked | Open-web discovery (E240) | Notes |
|---|---|---|---|---:|---|---|
| Muse Ember (xhigh) | Bug Hunt Bench | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No Muse Ember row, and no mention of the name, in benchmark.json, the combined scoreboard, runs, coverage or run notes at 3be9acd. The board's Meta rows are Muse Spark 1.2/1.3 and Muse Wonder (Full) 1.0, other models; none is transferred (O36). |
| Muse Ember (max) | Bug Hunt Bench | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No Muse Ember row, and no mention of the name, in benchmark.json, the combined scoreboard, runs, coverage or run notes at 3be9acd. The board's Meta rows are Muse Spark 1.2/1.3 and Muse Wonder (Full) 1.0, other models; none is transferred (O36). |
| MiMo-V2.6-Flash | Bug Hunt Bench | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 1 candidates (0 registered, 1 rejected) | Owner decision O135 (2026-10-30): AA plots MiMo-V2.6-Flash without an effort; Xiaomi's API documents a single thinking mode (thinking.type enabled/disabled, default enabled; on the Responses API every reasoning.effort other than none enables the same, undifferentiated reasoning), so the configuration is thinking enabled, the default (../../2026-10-30-v5-recapture/third-party/mimo-flash-effort.md; Xiaomi docs last read 2026-11-01, ../../2026-11-01-recapture/third-party/mimo/; not re-read on 2026-11-26). Bug Hunt ran the provider default through OpenRouter without asserting a reasoning state ('effort is `default` ... for this model the dial is untested rather than known-inert', run notes). The board does not show that this route's default is Xiaomi's documented default (thinking enabled), so the run stays unmatched (owner decision O140, 2026-10-30). |
| GPT-6 Luna (low) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (65.315), not low; not transferred. |
| GPT-6 Luna (medium) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (65.315), not medium; not transferred. |
| Claude Haiku 5.5 (low) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (76.586), not low; not transferred. |
| GPT-6 Luna (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (65.315), not high; not transferred. |
| Claude Haiku 5.5 (medium) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (76.586), not medium; not transferred. |
| Muse Ember (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (63.962), not xhigh; not transferred. |
| GPT-6.1 Terra (medium) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.52), not medium; not transferred. |
| GPT-6.2 Sol (low) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (79.483), not low; not transferred. |
| GPT-6.1 Terra (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.52), not high; not transferred. |
| GPT-6.1 Sol (medium) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.101), not medium; not transferred. |
| GPT-6.2 Sol (medium) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (79.483), not medium; not transferred. |
| GPT-6.2 Sol (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (79.483), not high; not transferred. |
| GPT-6.2 Sol (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (79.483), not xhigh; not transferred. |
| GPT-6.2 Astra (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (78.567), not high; not transferred. |
| GPT-6.2 Astra (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (78.567), not xhigh; not transferred. |
| Claude Fable 5.2 (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at high (83.519), not xhigh; not transferred. |
| Claude Fable 5.2 (max) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at high (83.519), not max; not transferred. |
| Gemini 4 Neon (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at xhigh (80.228), not high; not transferred. |
| GPT-6.2 Astra (medium) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (78.567), not medium; not transferred. |
| Gemini 4 Neon (medium) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at xhigh (80.228), not medium; not transferred. |
| GPT-6.1 Terra (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.52), not xhigh; not transferred. |
| Claude Haiku 5.5 (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (76.586), not xhigh; not transferred. |
| GPT-6 Luna (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (65.315), not xhigh; not transferred. |
| GPT-6.1 Terra (low) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.52), not low; not transferred. |
| Claude Haiku 5.5 (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (76.586), not high; not transferred. |
| GPT-6.1 Sol (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.101), not high; not transferred. |
| GPT-6.1 Sol (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.101), not xhigh; not transferred. |
| GPT-6 Astra (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.535), not high; not transferred. |
| GPT-6 Astra (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.535), not xhigh; not transferred. |
| Claude Opus 5.5 (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (78.49), not xhigh; not transferred. |
| GPT-6.1 Sol (low) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (75.101), not low; not transferred. |
| Claude Opus 5.5 (high) | Vibe Code Bench v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (78.49), not high; not transferred. |
| GPT-6 Luna (low) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not low; not transferred. |
| GPT-6 Luna (medium) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not medium; not transferred. |
| Claude Haiku 5.5 (low) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.36), not low; not transferred. |
| GPT-6 Luna (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not high; not transferred. |
| Claude Haiku 5.5 (medium) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.36), not medium; not transferred. |
| Muse Ember (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No meta/muse-ember row on this board. |
| Muse Ember (max) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No meta/muse-ember row on this board. |
| GPT-6.1 Terra (medium) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| GPT-6.2 Sol (low) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-sol row on this board. |
| GPT-6.1 Terra (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| GPT-6.1 Sol (medium) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not medium; not transferred. |
| GPT-6.2 Sol (medium) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-sol row on this board. |
| GPT-6.2 Sol (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-sol row on this board. |
| GPT-6.2 Sol (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-sol row on this board. |
| GPT-6.2 Sol (max) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-sol row on this board. |
| GPT-6.2 Astra (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-astra row on this board. |
| GPT-6.2 Astra (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-astra row on this board. |
| GPT-6.2 Astra (max) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-astra row on this board. |
| Claude Fable 5.2 (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at high (83.265), not xhigh; not transferred. |
| Claude Fable 5.2 (max) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at high (83.265), not max; not transferred. |
| Gemini 4 Neon (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No google/cobalt-c-high-1p00 row on this board. The board lists no Gemini 4 Neon row. |
| Gemini 4 Carbon | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No google/gemini-4-carbon row on this board. |
| Gemini 4 Neon (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No google/cobalt-c-high-1p00 row on this board. The board lists no Gemini 4 Neon row. |
| GPT-6.2 Astra (medium) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.2-astra row on this board. |
| Gemini 4 Neon (medium) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No google/cobalt-c-high-1p00 row on this board. The board lists no Gemini 4 Neon row. |
| GPT-6.1 Terra (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| Claude Haiku 5.5 (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.36), not xhigh; not transferred. |
| GPT-6 Luna (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not xhigh; not transferred. |
| GPT-6.1 Terra (low) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| Claude Haiku 5.5 (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.36), not high; not transferred. |
| GPT-6.1 Sol (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not high; not transferred. |
| GPT-6.1 Sol (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not xhigh; not transferred. |
| GPT-6 Astra (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (80.579), not high; not transferred. |
| GPT-6 Astra (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (80.579), not xhigh; not transferred. |
| Claude Opus 5.5 (xhigh) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.012), not xhigh; not transferred. |
| GPT-6.1 Sol (low) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not low; not transferred. |
| GPT-6.1 Terra (max) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| Claude Opus 5.5 (high) | Code Migration v1.1 (Vals) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.012), not high; not transferred. |
| GPT-6 Luna (low) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 60.42); not transferred. |
| GPT-6 Luna (medium) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 60.42); not transferred. |
| Claude Haiku 5.5 (low) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-haiku-5.5 at max only (Overall 68.94); not transferred. |
| GPT-6 Luna (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 60.42); not transferred. |
| Claude Haiku 5.5 (medium) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-haiku-5.5 at max only (Overall 68.94); not transferred. |
| Muse Ember (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No muse-ember row in release 20261106 (nor in the site's model metadata). |
| Muse Ember (max) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No muse-ember row in release 20261106 (nor in the site's model metadata). |
| GPT-6.1 Terra (medium) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 78.57); not transferred. |
| GPT-6.2 Sol (low) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.2-sol at max only (Overall 80.31); not transferred. |
| GPT-6.1 Terra (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 78.57); not transferred. |
| GPT-6.1 Sol (medium) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 81.17); not transferred. |
| GPT-6.2 Sol (medium) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.2-sol at max only (Overall 80.31); not transferred. |
| GPT-6.2 Sol (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.2-sol at max only (Overall 80.31); not transferred. |
| GPT-6.2 Sol (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.2-sol at max only (Overall 80.31); not transferred. |
| GPT-6.2 Astra (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.2-astra at max only (Overall 84.87); not transferred. |
| GPT-6.2 Astra (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.2-astra at max only (Overall 84.87); not transferred. |
| Claude Fable 5.2 (max) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench has Claude Fable 5.2 at xhigh only (Overall 84.88). Its notes.json states that the max-effort run scored 84.2 overall (against 84.9 at xhigh) but publishes no row or category scores for that run, so the weighted Overall cannot be rebuilt and no value is entered; the stated figure is carried as siteNoteOverallAtMax for the owner's decision (it is the same Overall metric at the same effort, but it is a note, not a table row). |
| Claude Fable 5.2 (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-fable-5.2 at xhigh only (Overall 84.88); not transferred. |
| Gemini 4 Neon (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gemini-4-neon at xhigh only (Overall 87.44); not transferred. |
| GPT-6.2 Astra (medium) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.2-astra at max only (Overall 84.87); not transferred. |
| Gemini 4 Neon (medium) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gemini-4-neon at xhigh only (Overall 87.44); not transferred. |
| GPT-6.1 Terra (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 78.57); not transferred. |
| Claude Haiku 5.5 (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-haiku-5.5 at max only (Overall 68.94); not transferred. |
| GPT-6 Luna (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 60.42); not transferred. |
| MiMo-V2.6-Flash | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | No mimo-v2.6-flash row in release 20261106 (nor in the site's model metadata). |
| GPT-6.1 Terra (low) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 78.57); not transferred. |
| Claude Haiku 5.5 (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-haiku-5.5 at max only (Overall 68.94); not transferred. |
| GPT-6.1 Sol (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 81.17); not transferred. |
| GPT-6.1 Sol (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 81.17); not transferred. |
| GPT-6 Astra (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-astra at max only (Overall 84.25); not transferred. |
| GPT-6 Astra (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-astra at max only (Overall 84.25); not transferred. |
| Claude Opus 5.5 (xhigh) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-opus-5.5 at max only (Overall 83.44); not transferred. |
| GPT-6.1 Sol (low) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 81.17); not transferred. |
| Claude Opus 5.5 (high) | LiveBench 2.0 Overall | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-opus-5.5 at max only (Overall 83.44); not transferred. |
| GPT-6 Luna (low) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6-Luna (Max) [Codex CLI, 2026-11-14] = 73.06; GPT-6-Luna (Xhigh) [Codex CLI, 2026-11-14] = 70.75; GPT-6-Luna (High) [Codex CLI, 2026-11-14] = 67.33; GPT-6-Luna (Medium) [Codex CLI, 2026-11-14] = 56.7. |
| Claude Haiku 5.5 (low) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Haiku 5.5 (High) [Claude Code, 2026-11-13] = 76.3; Haiku 5.5 (Medium) [Claude Code, 2026-11-14] = 75.84. |
| Muse Ember (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Muse Ember 1.0 (Max) [OpenCode, 2026-11-14] = 64.52. |
| GPT-6.2 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.2-Sol (High) [Codex CLI, 2026-11-20] = 83.53; GPT-6.2-Sol (Medium) [Codex CLI, 2026-11-18] = 83.1; GPT-6.2-Sol (Low) [Codex CLI, 2026-11-18] = 83.08. |
| GPT-6.2 Sol (max) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.2-Sol (High) [Codex CLI, 2026-11-20] = 83.53; GPT-6.2-Sol (Medium) [Codex CLI, 2026-11-18] = 83.1; GPT-6.2-Sol (Low) [Codex CLI, 2026-11-18] = 83.08. |
| GPT-6.2 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.2-Astra (High) [Codex CLI, 2026-11-18] = 84.48; GPT-6.2-Astra (Medium) [Codex CLI, 2026-11-18] = 84.06. |
| GPT-6.2 Astra (max) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.2-Astra (High) [Codex CLI, 2026-11-18] = 84.48; GPT-6.2-Astra (Medium) [Codex CLI, 2026-11-18] = 84.06. |
| Claude Fable 5.2 (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Fable 5.2 (Medium) [Claude Code, 2026-11-13] = 84.7. |
| Claude Fable 5.2 (max) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Fable 5.2 (Medium) [Claude Code, 2026-11-13] = 84.7. |
| Claude Fable 5.2 (high) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Fable 5.2 (Medium) [Claude Code, 2026-11-13] = 84.7. |
| Gemini 4 Carbon | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Gemini 4 Carbon (Medium) [Antigravity, 2026-11-25] = 80.49. |
| Claude Opus 5.5 (max) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Opus 5.5 (High) [Claude Code, 2026-11-13] = 84.95; Opus 5.5 (Medium) [Claude Code, 2026-11-13] = 83.15; Opus 5.5 (Low) [Claude Code, 2026-11-13] = 78.19. |
| GPT-6.1 Sol (max) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.1-Sol (High) [Codex CLI, 2026-11-13] = 83.86; GPT-6.1-Sol (Medium) [Codex CLI, 2026-11-13] = 83.04; GPT-6.1-Sol (Low) [Codex CLI, 2026-11-13] = 78.8. |
| Claude Haiku 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Haiku 5.5 (High) [Claude Code, 2026-11-13] = 76.3; Haiku 5.5 (Medium) [Claude Code, 2026-11-14] = 75.84. |
| GPT-6.1 Terra (low) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.1-Terra (Max) [Codex CLI, 2026-11-13] = 77.67; GPT-6.1-Terra (Xhigh) [Codex CLI, 2026-11-13] = 71.99; GPT-6.1-Terra (High) [Codex CLI, 2026-11-13] = 69.31; GPT-6.1-Terra (Medium) [Codex CLI, 2026-11-14] = 68.22. |
| GPT-6.1 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.1-Sol (High) [Codex CLI, 2026-11-13] = 83.86; GPT-6.1-Sol (Medium) [Codex CLI, 2026-11-13] = 83.04; GPT-6.1-Sol (Low) [Codex CLI, 2026-11-13] = 78.8. |
| GPT-6 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6-Astra (High) [Codex CLI, 2026-11-13] = 84.25; GPT-6-Astra (Medium) [Codex CLI, 2026-11-13] = 83.89. |
| Claude Opus 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Opus 5.5 (High) [Claude Code, 2026-11-13] = 84.95; Opus 5.5 (Medium) [Claude Code, 2026-11-13] = 83.15; Opus 5.5 (Low) [Claude Code, 2026-11-13] = 78.19. |
| GPT-6 Astra (max) | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6-Astra (High) [Codex CLI, 2026-11-13] = 84.25; GPT-6-Astra (Medium) [Codex CLI, 2026-11-13] = 83.89. |
| Claude Sonnet 5.5 | AI Coding Daily (excl. bug finding) | 2026-11-26 | not found | 1 | 2026-11-26: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Sonnet 5.5 (High) [Claude Code, 2026-11-13] = 80.58; Sonnet 5.5 (Medium) [Claude Code, 2026-11-13] = 75.44. |
| Muse Ember (xhigh) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Muse Ember (xhigh) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Muse Ember (max) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Muse Ember (max) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (low) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (low) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (medium) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (medium) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (high) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (high) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (xhigh) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (xhigh) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (max) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Sol (max) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (high) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (high) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (xhigh) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (xhigh) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (max) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (max) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Gemini 4 Neon (xhigh) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Gemini 4 Neon (xhigh) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Gemini 4 Carbon | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Gemini 4 Neon (high) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Gemini 4 Neon (high) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (medium) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| GPT-6.2 Astra (medium) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Gemini 4 Neon (medium) | AA-LCR v1.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |
| Gemini 4 Neon (medium) | GDPval-AA v2.1 | 2026-11-26 | not found | 1 | 2026-11-26: 4 queries, 3 candidates (0 registered, 3 rejected) | AA's Intelligence Index v5.0.2 no longer runs this evaluation; its page carries it only for models evaluated before the change. |

## Basket cost components

| Configuration | Component | Cost (USD) | Completeness | Tasks | USD per task | Source |
|---|---|---:|---|---:|---:|---|
| GPT-6.1 Sol (max) | AA-Briefcase | $210.45 | confirmed-complete | 91 | $2.3126 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | GDP.pdf | $41.99 | confirmed-complete | 100 | $0.4199 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | AutomationBench-AA | $195.01 | confirmed-complete | 657 | $0.2968 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Terminal-Bench 4.1 (AA Index run) | $120.30 | confirmed-complete | 66 | $1.8228 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | FrontierCode 2.0 | $149.21 | confirmed-complete | 132 | $1.1304 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Terminal-Bench-Science | $233.73 | confirmed-complete | 70 | $3.3389 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Coding Agent Index | $485.12 | confirmed-complete | — | — | AA Coding Agent Index v2.1 cost to run (mean API cost per task) x 322 tasks |
| Claude Sonnet 5.5 (max) | AA-Briefcase | $1,863.13 | confirmed-complete | 91 | $20.4739 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | GDP.pdf | $79.43 | confirmed-complete | 100 | $0.7943 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | $678.32 | confirmed-complete | 657 | $1.0324 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.1 (AA Index run) | $834.67 | confirmed-complete | 66 | $12.6464 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | FrontierCode 2.0 | $1,525.59 | confirmed-complete | 132 | $11.5575 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Terminal-Bench-Science | $1,663.25 | confirmed-complete | 70 | $23.7607 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Coding Agent Index | $3,670.34 | confirmed-complete | — | — | AA Coding Agent Index v2.1 cost to run (mean API cost per task) x 322 tasks |
| Claude Opus 5.5 (max) | AA-Briefcase | $1,915.18 | confirmed-complete | 91 | $21.0460 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | GDP.pdf | $155.23 | confirmed-complete | 100 | $1.5523 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | AutomationBench-AA | $938.69 | confirmed-complete | 657 | $1.4288 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Terminal-Bench 4.1 (AA Index run) | $865.21 | confirmed-complete | 66 | $13.1093 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | FrontierCode 2.0 | $1,776.08 | confirmed-complete | 132 | $13.4552 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Terminal-Bench-Science | $1,397.97 | confirmed-complete | 70 | $19.9710 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Coding Agent Index | $4,061.44 | confirmed-complete | — | — | AA Coding Agent Index v2.1 cost to run (mean API cost per task) x 322 tasks |
| Claude Opus 5.5 (max) | ITBench-AA | $146.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| GPT-6 Astra (max) | AA-Briefcase | $864.69 | confirmed-complete | 91 | $9.5021 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | GDP.pdf | $207.58 | confirmed-complete | 100 | $2.0758 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | AutomationBench-AA | $1,048.30 | confirmed-complete | 657 | $1.5956 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Terminal-Bench 4.1 (AA Index run) | $560.88 | confirmed-complete | 66 | $8.4981 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | FrontierCode 2.0 | $863.12 | confirmed-complete | 132 | $6.5388 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Terminal-Bench-Science | $1,223.34 | confirmed-complete | 70 | $17.4762 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Coding Agent Index | $2,455.41 | confirmed-complete | — | — | AA Coding Agent Index v2.1 cost to run (mean API cost per task) x 322 tasks |
| GPT-6 Astra (max) | ITBench-AA | $133.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| GPT-6 Luna (max) | AA-Briefcase | $15.47 | confirmed-complete | 91 | $0.1700 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | GDP.pdf | $2.85 | confirmed-complete | 100 | $0.0285 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | AutomationBench-AA | $23.91 | confirmed-complete | 657 | $0.0364 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Terminal-Bench 4.1 (AA Index run) | $15.59 | confirmed-complete | 66 | $0.2362 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | FrontierCode 2.0 | $23.22 | confirmed-complete | 132 | $0.1759 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Terminal-Bench-Science | $31.79 | confirmed-complete | 70 | $0.4541 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Coding Agent Index | $61.88 | confirmed-complete | — | — | AA Coding Agent Index v2.1 cost to run (mean API cost per task) x 322 tasks |

### AA Index total reconciliation

The seven Index components plus AA's residual reproduce AA's published Intelligence Index total cost.

| Configuration | Index SDLC components | Residual | Reconstructed total | Published total | Reconciled |
|---|---:|---:|---:|---:|---|
| GPT-6.1 Sol (max) | — | $173.29 | $1,123.97 | $1,123.97 | yes |
| Claude Sonnet 5.5 (max) | — | $1,336.25 | $7,980.63 | $7,980.63 | yes |
| Claude Opus 5.5 (max) | — | $1,863.54 | $8,911.91 | $8,909.67 | yes |
| GPT-6 Astra (max) | — | $893.27 | $5,661.18 | $5,661.18 | yes |
| GPT-6 Luna (max) | — | $23.22 | $136.06 | $136.06 | yes |

## DeepSWE v1.1 AA chart configurations (withdrawn by AA, not scored)

AA withdrew DeepSWE v1.1 from its Coding Agent Index (v2.0, October 2026) and the owner dropped it as a quality leaf in favour of FrontierCode (O49); this is AA's last capture, kept for the record. The AA chart published 42 DeepSWE v1.1 configurations across 113 tasks, observed 2026-10-17T19:26:26Z. Each keeps its displayed agent, model and effort; only exact matches enter a score.

| # | Agent | Evaluated model variant | Effort | pass@1 | ValueRank match | Note |
|---:|---|---|---|---:|---|---|
| 1 | Antigravity CLI | Gemini 4 Argon | high | 78.8% | Exact: gemini-4-argon | Exact variant: chart model Gemini 4 Argon (high) matches the roster display name 'Gemini 4 Argon' at effort high. |
| 2 | Muse Code | Muse Wonder Full | max | 77.0% | Exact: muse-wonder-full | Exact variant: chart model Muse Wonder Full (max) matches the roster display name 'Muse Wonder Full' at effort max. |
| 3 | Muse Code | Muse Wonder | max | 75.8% | Exact: muse-wonder | Exact variant: chart model Muse Wonder (max) matches the roster display name 'Muse Wonder' at effort max. |
| 4 | Codex | GPT-6.1 Sol | xhigh | 73.2% | Exact: gpt-6.1-sol-xhigh | Exact variant: chart model GPT-6.1 Sol (xhigh) matches the roster AA short name 'GPT-6.1 Sol' at effort xhigh. |
| 5 | Muse Code | Muse Spark 1.3 | xhigh | 73.2% | Exact: muse-spark-1-3-xhigh | Exact variant: chart model Muse Spark 1.3 (xhigh) matches the roster AA short name 'Muse Spark 1.3' at effort xhigh. |
| 6 | Devin Fusion CLI | Claude Opus 5.5 Max + GPT-6 Luna High | not shown | 72.6% | not in roster | No ValueRank roster model has this chart model name. It is a composite agent configuration. |
| 7 | Grok Build | Grok 4.7 | xhigh | 72.6% | Exact: grok-4.7 | Exact variant: chart model Grok 4.7 (xhigh) matches the roster display name 'Grok 4.7' at effort xhigh. |
| 8 | Codex | GPT-5.6 Sol | max | 72.3% | Exact: gpt-5.6-sol | Exact variant: chart model GPT-5.6 Sol (max) matches the roster display name 'GPT-5.6 Sol' at effort max. |
| 9 | Claude Code | Sonnet 5.5 | max | 72.0% | Exact: claude-sonnet-5-5 | Exact variant: chart model Sonnet 5.5 (max) matches the roster display name 'Claude Sonnet 5.5' at effort max. |
| 10 | Codex | GPT-6.1 Sol | medium | 72.0% | Exact: gpt-6.1-sol-medium | Exact variant: chart model GPT-6.1 Sol (medium) matches the roster AA short name 'GPT-6.1 Sol' at effort medium. |
| 11 | Muse Code | Muse Spark 1.3 | max | 71.7% | Exact: muse-spark-1-3 | Exact variant: chart model Muse Spark 1.3 (max) matches the roster display name 'Muse Spark 1.3' at effort max. |
| 12 | Codex | GPT-6.1 Sol | high | 70.5% | Exact: gpt-6.1-sol-high | Exact variant: chart model GPT-6.1 Sol (high) matches the roster AA short name 'GPT-6.1 Sol' at effort high. |
| 13 | Codex | GPT-6.1 Sol | max | 69.6% | Exact: gpt-6.1-sol | Exact variant: chart model GPT-6.1 Sol (max) matches the roster display name 'GPT-6.1 Sol' at effort max. |
| 14 | Codex | GPT-6 Sol | max | 69.0% | Exact: gpt-6-sol | Exact variant: chart model GPT-6 Sol (max) matches the roster display name 'GPT-6 Sol' at effort max. |
| 15 | Claude Code | Opus 5.5 | max | 68.4% | Exact: claude-opus-5-5 | Exact variant: chart model Opus 5.5 (max) matches the roster display name 'Claude Opus 5.5' at effort max. |
| 16 | Claude Code | Sonnet 5.5 | xhigh | 68.4% | Exact: claude-sonnet-5-5-xhigh | Exact variant: chart model Sonnet 5.5 (xhigh) matches the roster AA short name 'Claude Sonnet 5.5' at effort xhigh. |
| 17 | Kimi Code CLI | Kimi K3 | not shown | 68.4% | effort unconfirmed | The chart row shows no effort; the roster's selected configuration is max, so the variant cannot be confirmed and no result is transferred. |
| 18 | Codex | GPT-6 Astra | max | 67.6% | Exact: gpt-6-astra | Exact variant: chart model GPT-6 Astra (max) matches the roster display name 'GPT-6 Astra' at effort max. |
| 19 | Codex | GPT-6.1 Sol | low | 67.6% | Exact: gpt-6.1-sol-low | Exact variant: chart model GPT-6.1 Sol (low) matches the roster AA short name 'GPT-6.1 Sol' at effort low. |
| 20 | Devin Fusion CLI | GPT-6 Astra XHigh + SWE-2 Medium | not shown | 67.3% | not in roster | No ValueRank roster model has this chart model name. It is a composite agent configuration. |
| 21 | Claude Code | Sonnet 5.5 | high | 66.7% | Exact: claude-sonnet-5-5-high | Exact variant: chart model Sonnet 5.5 (high) matches the roster AA short name 'Claude Sonnet 5.5' at effort high. |
| 22 | Codex | GPT-5.6 Luna | max | 66.4% | Exact: gpt-5.6-luna | Exact variant: chart model GPT-5.6 Luna (max) matches the roster display name 'GPT-5.6 Luna' at effort max. |
| 23 | Antigravity SDK | Gemini 3.8 Flash | high | 65.8% | Exact: gemini-3.8-flash | Exact variant: chart model Gemini 3.8 Flash (high) matches the roster display name 'Gemini 3.8 Flash' at effort high. |
| 24 | Claude Code | Sonnet 5.5 | medium | 65.5% | Exact: claude-sonnet-5-5-medium | Exact variant: chart model Sonnet 5.5 (medium) matches the roster AA short name 'Claude Sonnet 5.5' at effort medium. |
| 25 | Grok Build | Grok 4.6 | xhigh | 64.9% | Exact: grok-4.6-xhigh | Exact variant: chart model Grok 4.6 (xhigh) matches the roster AA short name 'Grok 4.6' at effort xhigh. |
| 26 | Claude Code | Fable 5.1 | max | 64.3% | Exact: claude-fable-5-1 | Exact variant: chart model Fable 5.1 (max) matches the roster display name 'Claude Fable 5.1' at effort max. AA labels this configuration 'with fallback'; the marker is recorded but does not affect matching. |
| 27 | Codex | GPT-6 Luna | max | 63.7% | Exact: gpt-6-luna | Exact variant: chart model GPT-6 Luna (max) matches the roster display name 'GPT-6 Luna' at effort max. |
| 28 | Devin Fusion CLI | Claude Fable 5.1 XHigh + SWE-2 Medium | not shown | 63.1% | not in roster | No ValueRank roster model has this chart model name. It is a composite agent configuration. |
| 29 | Claude Code | Opus 5 | max | 62.5% | Exact: claude-opus-5 | Exact variant: chart model Opus 5 (max) matches the roster display name 'Claude Opus 5' at effort max. |
| 30 | Claude Code | Sonnet 5.5 | low | 61.9% | Exact: claude-sonnet-5-5-low | Exact variant: chart model Sonnet 5.5 (low) matches the roster AA short name 'Claude Sonnet 5.5' at effort low. |
| 31 | Claude Code | Step 5 Preview | not shown | 61.9% | not in roster | No ValueRank roster model has this chart model name. |
| 32 | Opencode | GLM-5.3 | max | 61.4% | Exact: glm-5.3 | Exact variant: chart model GLM-5.3 (max) matches the roster display name 'GLM-5.3' at effort max. |
| 33 | Muse Code | Muse Spark Open | xhigh | 60.2% | not in roster | No ValueRank roster model has this chart model name. |
| 34 | Codex | DeepSeek V4 Pro 0813 | max | 57.2% | Exact: deepseek-v4-pro | Exact variant: chart model DeepSeek V4 Pro 0813 (max) matches the roster AA short name 'DeepSeek V4 Pro 0813' at effort max. |
| 35 | Codex | DeepSeek V4 Flash 0731 | max | 54.3% | Exact: deepseek-v4-flash | Exact variant: chart model DeepSeek V4 Flash 0731 (max) matches the roster AA short name 'DeepSeek V4 Flash 0731' at effort max. |
| 36 | Claude Code | Qwen3.8 Max | not shown | 51.0% | Exact: qwen3.8-max | Exact variant: chart model Qwen3.8 Max (no effort) matches the roster display name 'Qwen3.8 Max' at effort no effort. |
| 37 | Claude Code | Haiku 5.5 | xhigh | 49.0% | Exact: claude-haiku-5-5 | Exact variant: chart model Haiku 5.5 (xhigh) matches the roster display name 'Claude Haiku 5.5' at effort xhigh. |
| 38 | Claude Code | Haiku 5.5 | medium | 47.5% | Exact: claude-haiku-5-5-medium | Exact variant: chart model Haiku 5.5 (medium) matches the roster AA short name 'Claude Haiku 5.5' at effort medium. |
| 39 | Claude Code | Haiku 5.5 | high | 46.3% | Exact: claude-haiku-5-5-high | Exact variant: chart model Haiku 5.5 (high) matches the roster AA short name 'Claude Haiku 5.5' at effort high. |
| 40 | Claude Code | Haiku 5.5 | max | 46.0% | Exact: claude-haiku-5-5-max | Exact variant: chart model Haiku 5.5 (max) matches the roster AA short name 'Claude Haiku 5.5' at effort max. |
| 41 | Claude Code | Haiku 5.5 | low | 45.4% | Exact: claude-haiku-5-5-low | Exact variant: chart model Haiku 5.5 (low) matches the roster AA short name 'Claude Haiku 5.5' at effort low. |
| 42 | Mirror | Beam 1.0 | not shown | 39.8% | not in roster | No ValueRank roster model has this chart model name. |

## Terminal-Bench 4.1 official rows

54 official rows (12 of 45 cohort matches), observed 2026-11-26T13:24:53Z. The published ± is the source's 95% confidence interval (used by stream S1M). Since O37 the Terminal-Bench leaf is AA's own run; these rows cross-check it and fill a gap. Matched agents for cohort rows, in the registered preference order (E225): Claude Code 2, Codex 3.

| Rank | Base model | Agent | Resolution rate | Tokens | Cost |
|---|---|---|---:|---|---:|
| 1 | Copilot Fusion | GitHub Copilot | 71.2% ± 2.9% | 3.3B | $2,000 |
| 2 | Opus 5.5 | Claude Code | 65.8% ± 3.1% | 8.0B | $4,700 |
| 2 | Fable 5.2 | Claude Code | 65.8% ± 2.8% | 15.7B | $16,500 |
| 4 | Gemini 4 Carbon | Antigravity CLI | 64.5% ± 3.2% | 3.8B | $1,400 |
| 5 | Sonnet 5.5 | Claude Code | 63.9% ± 3.0% | 19.4B | $7,300 |
| 6 | GPT-6.2 Astra | Codex | 62.1% ± 2.3% | 1.1B | $1,400 |
| 7 | GPT-6.2 Sol | Codex | 61.5% ± 2.8% | 1.1B | $300 |
| 8 | Gemini 4 Neon | Antigravity CLI | 61.2% ± 2.8% | 3.2B | $1,900 |
| 9 | GPT-6.1 Sol | Codex | 60.9% ± 3.0% | 1.5B | $600 |
| 10 | GPT-6 Astra | Codex | 60.3% ± 2.8% | 1.5B | $3,300 |
| 11 | Kimi K3.1 Pro | Claude Code | 59.7% ± 4.2% | 3.2B | $1,100 |
| 12 | Fable 5.1 | Claude Code | 57.6% ± 3.3% | 2.3B | $4,900 |
| 13 | Gemini 4 Hydrogen | Antigravity CLI | 56.4% ± 3.0% | 3.6B | $800 |
| 14 | Gemini 4 Argon | Antigravity CLI | 55.5% ± 2.8% | 2.8B | $1,100 |
| 15 | Opus 5 | Claude Code | 53.3% ± 3.1% | 6.9B | $6,100 |
| 15 | GPT-6.1 Terra | Codex | 53.3% ± 3.1% | 8.5B | $900 |
| 17 | GPT-6 Sol | Codex | 50.3% ± 3.2% | 5.0B | $1,500 |
| 18 | Muse Wonder | Muse Code | 47.0% ± 3.8% | 5.5B | $2,500 |
| 19 | Fable 5 | Claude Code | 44.8% ± 3.8% | 3.8B | $7,300 |
| 20 | GLM-5.3 | Claude Code | 41.2% ± 3.3% | 8.7B | $2,700 |
| 21 | Haiku 5.5 | Claude Code | 40.0% ± 3.6% | 12.1B | $1,000 |
| 22 | Grok 4.7 | Grok Build | 38.8% ± 3.6% | 5.5B | $3,700 |
| 23 | GPT-5.6 Sol | Codex | 38.5% ± 3.8% | 4.4B | $2,500 |
| 23 | DeepSeek V4.1 Flash 1017 | Claude Code | 38.5% ± 3.8% | 8.2B | $200 |
| 25 | Hy4 | Claude Code | 37.9% ± 3.5% | 5.3B | $300 |
| 26 | GLM-5.3-Flash | Claude Code | 37.0% ± 3.6% | 8.2B | $400 |
| 27 | Muse Ember | Muse Code | 30.6% ± 3.8% | 8.1B | $200 |
| 28 | Mistral Large 4 | Claude Code | 27.6% ± 3.9% | 5.8B | $700 |
| 29 | Qwen3.8-Max-0902 | Claude Code | 27.0% ± 3.9% | 3.0B | $4,600 |
| 29 | MiMo V2.6 Pro | mini-swe-agent | 27.0% ± 3.6% | 7.8B | $300 |
| 31 | Opus 4.8 | Claude Code | 23.6% ± 3.6% | 6.4B | $6,500 |
| 32 | Kimi K3 | Claude Code | 23.0% ± 3.7% | 4.9B | $1,900 |
| 33 | Ember-1 | mini-swe-agent | 21.8% ± 3.5% | 11.9B | $4,700 |
| 34 | GPT-5.6 Terra | Codex | 21.5% ± 3.3% | 5.7B | $1,700 |
| 35 | Grok 4.6 | Grok Build | 19.7% ± 3.1% | 4.0B | $3,600 |
| 36 | Hy4 Preview | Claude Code | 19.1% ± 3.1% | 6.0B | $700 |
| 37 | Gemini 3.8 Flash | mini-SWE-agent | 18.2% ± 3.4% | 17.2B | $1,800 |
| 38 | GPT-5.6 Luna | Codex | 17.6% ± 2.9% | 11.6B | $300 |
| 39 | MiMo V2.6 Flash | mini-swe-agent | 16.1% ± 3.4% | 9.9B | $200 |
| 40 | GPT-6 Luna | Codex | 15.2% ± 2.7% | 3.9B | $100 |
| 41 | Muse Spark 1.3 | Muse Code | 14.8% ± 3.0% | 9.0B | — |
| 42 | Inkling Small 2 | mini-swe-agent | 13.0% ± 2.8% | 27.5B | $1,000 |
| 43 | Gemini 3.7 Flash | mini-SWE-agent | 12.4% ± 2.5% | 11.1B | $1,300 |
| 43 | Grok 4.5 | Grok Build | 12.4% ± 2.6% | 3.4B | $2,100 |
| 45 | Sonnet 5 | Claude Code | 12.1% ± 3.0% | 21.6B | $9,600 |
| 46 | Hy4 Flash | mini-swe-agent | 11.8% ± 2.8% | 4.5B | $0 |
| 47 | MiniMax M3 | mini-swe-agent | 7.6% ± 2.8% | 16.5B | $1,100 |
| 48 | DeepSeek V4 Pro 0813 | Claude Code | 6.7% ± 2.5% | 3.8B | $700 |
| 49 | Beam 1.0 | mini-swe-agent | 6.4% ± 1.7% | 4.1B | $200 |
| 50 | Gemini 3.1 Pro | Antigravity CLI | 2.7% ± 1.7% | 7.9B | $3,700 |
| 51 | GPT-5.4 Mini | Codex | 1.8% ± 1.3% | 4.2B | $700 |
| 52 | Inkling Small | mini-swe-agent | 0.9% ± 0.9% | 0.4B | $0 |
| 53 | Nemotron 3.5 Super VL | mini-swe-agent | 0.3% ± 0.6% | 3.3B | $200 |
| 54 | Inkling | mini-swe-agent | 0.0% ± 0.0% | 1.4B | $1,000 |

## Bug Hunt Bench matched runs

Owner-published runs at commit `3be9acdb221b8127e181fa20f0c5a87647d7550e`; the record is the owner's largest-sample mean for the exact model and effort, and the leaf (owner decisions O163 and O170) is its planted bugs fixed (of 105, the board's own score) plus the genuine unplanted bugs it fixed, as a percentage of the live board's largest planted plus largest unplanted counts over every run, recomputed at every release, with the harness that result was run on (E206). No ranked configuration has Bug Hunt results on two harnesses at the same effort (E224).

| Model | Evaluated model | Planted bugs fixed of 105 | Unplanted bugs fixed | Leaf (sum, O163) | Runs | Effort | Harness |
|---|---|---:|---:|---:|---:|---|---|
| GPT-6 Luna (low) | GPT-6 Luna (low effort) | 4.0 | 9.0 | 13.0 | 1 | low | Codex CLI |
| GPT-6 Luna (medium) | GPT-6 Luna (medium effort) | 4.0 | 0.0 | 4.0 | 1 | medium | Codex CLI |
| Claude Haiku 5.5 (low) | Haiku 5.5 (low effort) | 11.0 | 2.0 | 13.0 | 1 | low | Claude Code |
| GPT-6 Luna (high) | GPT-6 Luna (high effort) | 9.0 | 9.0 | 18.0 | 1 | high | Codex CLI |
| Claude Haiku 5.5 (medium) | Haiku 5.5 (medium effort) | 12.0 | 4.0 | 16.0 | 1 | medium | Claude Code |
| GPT-6.1 Terra (medium) | GPT-6.1 Terra (medium effort) - mean of 3 | 7.3 | 7.3 | 14.6 | 3 | medium | Codex CLI |
| GPT-6.2 Sol (low) | GPT-6.2 Sol (low effort) - mean of 3 | 36.0 | 28.7 | 64.7 | 3 | low | Codex CLI |
| GPT-6.1 Terra (high) | GPT-6.1 Terra (high effort) - mean of 3 | 9.7 | 6.7 | 16.4 | 3 | high | Codex CLI |
| GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium effort) - mean of 2 | 29.0 | 30.5 | 59.5 | 2 | medium | Codex CLI |
| GPT-6.2 Sol (medium) | GPT-6.2 Sol (medium effort) - mean of 3 | 45.7 | 49.3 | 95.0 | 3 | medium | Codex CLI |
| GPT-6.2 Sol (high) | GPT-6.2 Sol (high effort) - mean of 3 | 49.7 | 52.7 | 102.4 | 3 | high | Codex CLI |
| GPT-6.2 Sol (xhigh) | GPT-6.2 Sol (xhigh effort) - mean of 3 | 49.0 | 52.3 | 101.3 | 3 | xhigh | Codex CLI |
| GPT-6.2 Sol (max) | GPT-6.2 Sol (max effort) - mean of 3 | 54.7 | 56.0 | 110.7 | 3 | max | Codex CLI |
| GPT-6.2 Astra (high) | GPT-6.2 Astra (high effort) - mean of 5 | 59.6 | 76.2 | 135.8 | 5 | high | Codex CLI |
| GPT-6.2 Astra (xhigh) | GPT-6.2 Astra (xhigh effort) - mean of 5 | 60.2 | 72.0 | 132.2 | 5 | xhigh | Codex CLI |
| GPT-6.2 Astra (max) | GPT-6.2 Astra (max effort) - mean of 3 | 62.7 | 60.0 | 122.7 | 3 | max | Codex CLI |
| Claude Fable 5.2 (xhigh) | Fable 5.2 (xhigh effort) - mean of 3 | 49.0 | 16.7 | 65.7 | 3 | xhigh | Claude Code |
| Claude Fable 5.2 (max) | Fable 5.2 (max effort) - mean of 3 | 58.0 | 24.7 | 82.7 | 3 | max | Claude Code |
| Claude Fable 5.2 (high) | Fable 5.2 (high effort) - mean of 2 | 43.0 | 16.5 | 59.5 | 2 | high | Claude Code |
| Gemini 4 Neon (xhigh) | Gemini 4 Neon (xhigh effort, Antigravity CLI 1.5.16) - mean of 3 | 61.0 | 42.0 | 103.0 | 3 | xhigh | Antigravity CLI |
| Gemini 4 Carbon | Gemini 4 Carbon (high effort, Antigravity CLI) - mean of 3 | 57.3 | 25.0 | 82.3 | 3 | high | Antigravity CLI |
| Gemini 4 Neon (high) | Gemini 4 Neon (high effort, Antigravity CLI 1.5.16) - mean of 3 | 56.0 | 36.3 | 92.3 | 3 | high | Antigravity CLI |
| Claude Opus 5.5 (max) | Opus 5.5 (max effort) - mean of 3 | 41.7 | 9.0 | 50.7 | 3 | max | Claude Code |
| GPT-6.2 Astra (medium) | GPT-6.2 Astra (medium effort) - mean of 3 | 50.3 | 62.7 | 113.0 | 3 | medium | Codex CLI |
| Gemini 4 Neon (medium) | Gemini 4 Neon (medium effort, Antigravity CLI 1.5.16) - mean of 3 | 48.3 | 20.7 | 69.0 | 3 | medium | Antigravity CLI |
| GPT-6.1 Sol (max) | GPT-6.1 Sol (max effort) - mean of 3 | 44.3 | 65.3 | 109.6 | 3 | max | Codex CLI |
| GPT-6.1 Terra (xhigh) | GPT-6.1 Terra (xhigh effort) - mean of 3 | 11.3 | 17.0 | 28.3 | 3 | xhigh | Codex CLI |
| Claude Haiku 5.5 (xhigh) | Haiku 5.5 (xhigh effort) - mean of 3 | 18.3 | 6.7 | 25.0 | 3 | xhigh | Claude Code |
| GPT-6 Luna (xhigh) | GPT-6 Luna (xhigh effort) | 14.0 | 12.0 | 26.0 | 1 | xhigh | Codex CLI |
| GPT-6.1 Terra (low) | GPT-6.1 Terra (low effort) - mean of 3 | 6.0 | 5.0 | 11.0 | 3 | low | Codex CLI |
| Claude Haiku 5.5 (high) | Haiku 5.5 (high effort) - mean of 2 | 16.0 | 4.0 | 20.0 | 2 | high | Claude Code |
| GPT-6.1 Sol (high) | GPT-6.1 Sol (high effort) - mean of 2 | 36.5 | 40.0 | 76.5 | 2 | high | Codex CLI |
| GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh effort) - mean of 3 | 42.7 | 56.7 | 99.4 | 3 | xhigh | Codex CLI |
| GPT-6 Astra (high) | GPT-6 Astra (high effort) | 35.0 | 40.0 | 75.0 | 1 | high | Codex CLI |
| GPT-6 Astra (xhigh) | GPT-6 Astra (xhigh effort) | 43.0 | 53.0 | 96.0 | 1 | xhigh | Codex CLI |
| Claude Opus 5.5 (xhigh) | Opus 5.5 (xhigh effort) - mean of 3 | 36.0 | 13.3 | 49.3 | 3 | xhigh | Claude Code |
| GPT-6 Luna (max) | GPT-6 Luna (max effort) - mean of 3 | 18.3 | 22.7 | 41.0 | 3 | max | Codex CLI |
| GPT-6.1 Sol (low) | GPT-6.1 Sol (low effort) - mean of 2 | 22.5 | 24.0 | 46.5 | 2 | low | Codex CLI |
| GPT-6.1 Terra (max) | GPT-6.1 Terra (max effort) - mean of 3 | 40.7 | 48.0 | 88.7 | 3 | max | Codex CLI |
| Claude Opus 5.5 (high) | Opus 5.5 (high effort) - mean of 3 | 31.7 | 10.7 | 42.4 | 3 | high | Claude Code |
| GPT-6 Astra (max) | GPT-6 Astra (max effort) - mean of 3 | 45.0 | 55.0 | 100.0 | 3 | max | Codex CLI |
| Claude Sonnet 5.5 | Sonnet 5.5 (max effort) - mean of 3 | 51.3 | 26.3 | 77.6 | 3 | max | Claude Code |

## Plan routes

Route evidence as of 2026-11-26. Full allocation regimes, workloads and notes are in [data/plan_cost_routes.json](data/plan_cost_routes.json).

| Plan | Eligible configurations | Monthly fee | Value Multiple | Evidence | Source model | Source date | Source |
|---|---|---:|---:|---|---|---|---|
| ChatGPT Plus $20 · GPT-6.1 Sol | GPT-6.1 Sol (max) | $20.00 | 10.55× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · GPT-6 Astra | GPT-6 Astra (max) | $20.00 | 8.1× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | gpt-5.6-sol | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | gpt-5.6-luna | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | gpt-5.5 | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | gpt-6-sol | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (max) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (xhigh) | $20.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (high) | $20.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (medium) | $20.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (low) | $20.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · GPT-6.1 Sol | GPT-6.1 Sol (max) | $100.00 | 10.55× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · GPT-6 Astra | GPT-6 Astra (max) | $100.00 | 13.22× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | gpt-5.6-sol | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | gpt-5.6-luna | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | gpt-5.5 | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | gpt-6-sol | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (max) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (xhigh) | $100.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (high) | $100.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (medium) | $100.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (low) | $100.00 | 10.55× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · GPT-6.1 Sol | GPT-6.1 Sol (max) | $200.00 | 10.42× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · GPT-6 Astra | GPT-6 Astra (max) | $200.00 | 14.485× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | gpt-5.6-sol | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | gpt-5.6-luna | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | gpt-5.5 | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | gpt-6-sol | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (max) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (xhigh) | $200.00 | 10.42× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (high) | $200.00 | 10.42× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (medium) | $200.00 | 10.42× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (low) | $200.00 | 10.42× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · GPT-6.1 Sol | GPT-6.1 Sol (max) | $500.00 | 10.772× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · GPT-6 Astra | GPT-6 Astra (max) | $500.00 | 13.91× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | gpt-5.6-sol | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | gpt-5.6-luna | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | gpt-5.5 | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | gpt-6-sol | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (max) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (xhigh) | $500.00 | 10.772× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (high) | $500.00 | 10.772× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (medium) | $500.00 | 10.772× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · same-model measurement, another effort (O88, O90) | GPT-6.1 Sol (low) | $500.00 | 10.772× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · Opus 5.5 | Claude Opus 5.5 (max) | $20.00 | 58.9× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $100 · Opus 5.5 | Claude Opus 5.5 (max) | $100.00 | 57.25× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Opus 5.5 | Claude Opus 5.5 (max) | $200.00 | 58.63× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $100 · Fable 5.1 | claude-fable-5-1 | $100.00 | 12.73× | Controlled account measurement / workload projection | Fable 5.1 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Fable 5.1 | claude-fable-5-1 | $200.00 | 12.425× | Controlled account measurement / workload projection | Fable 5.1 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| MiMo Token Plan Lite $6 · quota ceiling (provider-derived) | mimo-v2-6-pro | $6.00 | 0.984× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Standard $16 · quota ceiling (provider-derived) | mimo-v2-6-pro | $16.00 | 0.99× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Pro $50 · quota ceiling (provider-derived) | mimo-v2-6-pro | $50.00 | 1.0944× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Max $100 · quota ceiling (provider-derived) | mimo-v2-6-pro | $100.00 | 1.1808× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Lite $6 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $6.00 | 0.9567× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Standard $16 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $16.00 | 0.9625× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Pro $50 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $50.00 | 1.064× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Max $100 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $100.00 | 1.148× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| Claude Pro $20 · common Claude assumption | claude-opus-5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-fable-5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-opus-4.8 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-sonnet-5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (xhigh) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Sonnet 5.5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-haiku-5-5-max | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (high) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (medium) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (low) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-sonnet-5-5-xhigh | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-sonnet-5-5-high | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-sonnet-5-5-medium | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | claude-sonnet-5-5-low | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-opus-5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-fable-5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-opus-4.8 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-sonnet-5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (xhigh) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Sonnet 5.5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-haiku-5-5-max | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (high) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (medium) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (low) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-sonnet-5-5-xhigh | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-sonnet-5-5-high | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-sonnet-5-5-medium | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | claude-sonnet-5-5-low | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-opus-5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-fable-5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-opus-4.8 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-sonnet-5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (xhigh) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Sonnet 5.5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-haiku-5-5-max | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (high) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (medium) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (low) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-sonnet-5-5-xhigh | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-sonnet-5-5-high | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-sonnet-5-5-medium | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | claude-sonnet-5-5-low | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · same-model measurement, another effort (O88, O90) | Claude Opus 5.5 (high) | $20.00 | 58.9× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · same-model measurement, another effort (O88, O90) | Claude Opus 5.5 (high) | $100.00 | 57.25× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · same-model measurement, another effort (O88, O90) | Claude Opus 5.5 (high) | $200.00 | 58.63× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · same-model measurement, another effort (O88, O90) | Claude Opus 5.5 (xhigh) | $20.00 | 58.9× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · same-model measurement, another effort (O88, O90) | Claude Opus 5.5 (xhigh) | $100.00 | 57.25× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · same-model measurement, another effort (O88, O90) | Claude Opus 5.5 (xhigh) | $200.00 | 58.63× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · same-model measurement, another effort (O88, O90) | claude-opus-5-5-medium | $20.00 | 58.9× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · same-model measurement, another effort (O88, O90) | claude-opus-5-5-medium | $100.00 | 57.25× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · same-model measurement, another effort (O88, O90) | claude-opus-5-5-medium | $200.00 | 58.63× | Same-model measurement from another effort (owner decisions O88, O90) | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (low) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (low) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (low) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (low) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (medium) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (medium) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (medium) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (medium) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (high) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (high) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (high) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (high) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Terra (low) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Terra (low) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Terra (low) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Terra (low) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Terra (medium) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Terra (medium) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Terra (medium) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Terra (medium) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Terra (high) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Terra (high) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Terra (high) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Terra (high) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Terra (xhigh) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Terra (xhigh) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Terra (xhigh) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Terra (xhigh) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Terra (max) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Terra (max) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Terra (max) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Terra (max) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (xhigh) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (xhigh) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (xhigh) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (xhigh) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (high) | $20.00 | 8.1× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (high) | $100.00 | 13.22× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (high) | $200.00 | 14.485× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (high) | $500.00 | 13.91× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (xhigh) | $20.00 | 8.1× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (xhigh) | $100.00 | 13.22× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (xhigh) | $200.00 | 14.485× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · same-model measurement, another effort (O88, O90) | GPT-6 Astra (xhigh) | $500.00 | 13.91× | Same-model measurement from another effort (owner decisions O88, O90) | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | gpt-5.6-luna-low | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | gpt-5.6-luna-low | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | gpt-5.6-luna-low | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | gpt-5.6-luna-low | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| OpenCode Go $10 · DeepSeek V4.1 Flash · published dollar limit ($100 a month) | deepseek-v4-1-flash-1017 | $10.00 | 10× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · Gemini 4 Argon · published dollar limit ($30 a month) | gemini-4-argon | $10.00 | 3× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · Claude Haiku 5.5 (xhigh) · published dollar limit ($15 a month) | Claude Haiku 5.5 (xhigh) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · Claude Haiku 5.5 (high) · published dollar limit ($15 a month) | Claude Haiku 5.5 (high) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · Claude Haiku 5.5 (low) · published dollar limit ($15 a month) | Claude Haiku 5.5 (low) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · Claude Haiku 5.5 (max) · published dollar limit ($15 a month) | claude-haiku-5-5-max | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · Claude Haiku 5.5 (medium) · published dollar limit ($15 a month) | Claude Haiku 5.5 (medium) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · GPT-6 Luna (max) · published dollar limit ($15 a month) | GPT-6 Luna (max) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · GPT-6 Luna (high) · published dollar limit ($15 a month) | GPT-6 Luna (high) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · GPT-6 Luna (low) · published dollar limit ($15 a month) | GPT-6 Luna (low) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · GPT-6 Luna (medium) · published dollar limit ($15 a month) | GPT-6 Luna (medium) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · GPT-6 Luna (xhigh) · published dollar limit ($15 a month) | GPT-6 Luna (xhigh) | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · Kimi K3.1 Pro · published dollar limit ($15 a month) | kimi-k3-1-pro | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| OpenCode Go $10 · MiMo-V2.6-Pro · published dollar limit ($15 a month) | mimo-v2-6-pro | $10.00 | 1.5× | Published dollar limit (owner decisions O198 and O203; the plan's terms, read after the release cutoff, not a measurement) | — | 2026-11-11 | [Source](https://opencode.ai/docs/console/go/) |
| Claude Max 5x $100 · common Claude assumption | Claude Fable 5.2 (max) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Fable 5.2 (high) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Fable 5.2 (xhigh) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Fable 5.2 (max) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Fable 5.2 (high) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Fable 5.2 (xhigh) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Opus 5.5 · two end-user reports (O218) | Claude Opus 5.5 (max) | $200.00 | 54.21× | end user report | — | 2026-11-16 | [Source](https://www.reddit.com/r/ClaudeCode/comments/1xy4zwk/) |

### Plan amounts and their lineage

Each routed row's amount with what it measures, how it was derived and which objects it comes from (E166, E168); API-fallback rows have none.

| Configuration | Amount (USD per fee period) | Measures | Derivation | Workload | Cash object | Measurement object |
|---|---:|---|---|---|---|---|
| GPT-6.1 Sol (max) | $5,386 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | chatgpt-pro500-gpt61sol-semianalysis:month cash | chatgpt-pro500-gpt61sol-semianalysis |
| Claude Opus 5.5 (max) | $1,178 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | claude-pro-opus55-semianalysis:month cash | claude-pro-opus55-semianalysis |
| GPT-6 Astra (max) | $2,897 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | chatgpt-pro200-gpt6astra-semianalysis:month cash | chatgpt-pro200-gpt6astra-semianalysis |
| Claude Sonnet 5.5 (max) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-claude-sonnet-5-5-common-opus55-assumption:month cash | claude-pro-claude-sonnet-5-5-common-opus55-assumption |
| GPT-6 Luna (max) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-gpt-6-luna-common-gpt-assumption:month cash | chatgpt-pro500-gpt-6-luna-common-gpt-assumption |

## Evidence bundle

Bundle hash `41d81f9cbf397403dee750f3485747efac16b2a228f22295b6ed52611c8f136d`: every published output is rebuilt from these artifacts at the pinned publication clock (npm run verify:docs), never from live pages.

| Key | Artifact | SHA-256 | Captured | Extractor |
|---|---|---|---|---|
| snapshot | `data/aa/aa_v432_snapshot.json` | `2727a938d8c1e6fff241c49954f59354eaf31f854a41a64e5e4963b97eed5f82` | 2026-11-26T02:59:01Z | valuerank.capture_aa |
| bugHunt | `data/bug_hunt.json` | `29ae7a755efbaa46903a0e173f463485b415f0e311536eb0551be7f2459287c6` | 2026-11-26 | editorial capture of the owner's published results (source commit recorded) |
| tb4 | `data/tb4.json` | `34fb702147ad22d84904bcfc025f8d3565a71ad2669ae7c3065dc67d047c1b8a` | 2026-11-26T03:11:03.572Z | scripts/scrape-tb4.js, then valuerank.build_tb4 |
| codingAgents | `data/aa/coding_agents_capture.json` | `cbb2125c7f9873951bd3df701ab953c322eaf1d61bd7354dbd267af4da6793a2` | 2026-11-26T03:00:03Z | valuerank.capture_coding_agents |
| costCharts | `data/aa/cost_charts_capture.json` | `9eabf83e763820aa30a28abda408c557b95c120bfce34fe276bfbd3583e30ff4` | 2026-11-26T03:00:47.681Z | scripts/capture-aa-cost-charts.js |
| configurationMap | `data/v3_configuration_map.json` | `33d4fc30f72ff340554750ba413d803775754c05e14b486baf20fa2f75b3d563` | 2026-11-26 | editorial pinning from the research capture |
| codingAgentsManifest | `data/aa/coding_agents_manifest.json` | `f2bd40f9096ae1e79f033524cbe0feb07dfffb40c044e97a2c62e78515c4b242` | 2026-11-26 | editorial manifest of every AA Coding Agent Index row, reviewed at each capture (O64) |
| frontierCapture | `data/aa_frontier_capture.json` | `69a062faea329e408166def17d8de4e2404f621a33c100f1d5e889b18935a705` | 2026-11-26T02:18:20Z | browser capture of AA's Intelligence Index vs cost chart from public tooltips (frontier membership, E195; unevaluated cheaper siblings, E201) |
| roster | `data/aa_mapping.json` | `bbdddb3a6775ccd470c6cceb9c4eceab0f6a6779ca79c58cb95665fbc5f2d8e7` | 2026-11-26T02:18:20Z | editorial roster: every configuration AA plots on its rendered frontier or within 3 Index points of it (O51) |
| bugHuntScoreboard | `data/bug_hunt_scoreboard.json` | `e319bcaf9437ee330bea87d378d358698737097e7849aae129257aa0f42c8737` | 2026-11-26T03:03:40Z | the owner's combined scoreboard at the pinned commit (O31 roster check) |
| planRoutes | `data/plan_cost_routes.json` | `7d483391afc3f69cb37af17535b3540aa7ee162216f751486dccac9f6209ed0a` | 2026-11-26 | editorial Plan evidence registry |
| priceRecords | `data/price_records.json` | `0c32e22ffec53a7ad9939927c8016a975c74e8b05d9ee05fe29f920cd1007ae5` | 2026-11-26T13:45:00Z | editorial E141 price-record registry (superseded and promotional tariffs) |
| leafEvidence | `data/leaf_evidence.json` | `634150d417abddc730c879ef23fe06a47227752dada50d8cae9baccbd78e44f6` | 2026-11-26 | editorial supplementary leaf evidence and the exhaustive-search log (O36) |
| cognitionFrontierCode | `data/cognition_frontiercode.json` | `b1901aef26f065b3df1eb95508c13f45e87b003f33f46dda9c11526534d2b5a8` | 2026-11-26 | Cognition's FrontierCode leaderboard data (https://cognition.com/data/frontiercode-leaderboard/data.json), captured unchanged (O37) |
| sweTracks | `data/swe_tracks.json` | `4bce48b8ef0cb9dcd2e198fbd47e7f58b8d22019ce298ac02a977619ce502cae` | 2026-11-26T13:18:00Z | research/2026-10-23-swe-benchmarks/build_swe_tracks.py from the verified coverage captures (O53-O55) |
| planReports | `data/plan_reports.json` | `6d942f199a56a053e44d79c60da2ef60c5532cd5931fa4f422719c1eaafbfee5` | 2026-11-24 | editorial table of every O71 user report with the facts E270 needs; the build derives admission from it (O81) |
| aaPreviousCapture | `data/aa/aa_previous_capture.json` | `e3f458870a662e0c7fff03c35cf0dda9f1c3f6728588ff1c836bd420fa726329` | 2026-11-01T05:57:26Z | valuerank.capture_aa: digest of the model-page capture this one replaced (I60) |
| fallbackPrices | `data/fallback_prices.json` | `3ab915c9d8ad8a357d7dbcc326dd39a2af64e89b5ef312477d68ea3f3cf50ea9` | 2026-11-01T11:59:15Z | editorial capture of the list API prices of AA's named fallback models (O158 sensitivity only) |
| sourceRereads | `data/source_rereads.json` | `c982efc6c6080bd7b224d5b0e4dd7c92efbd0f6bad9f3630799273b096b4ab95` | 2026-11-26 | editorial record of the O68 re-reads, each 'unchanged' result verified against the re-read file |
| aaFootnotes | `data/aa/aa_footnote_register.json` | `ccc742e1cca305fa88b80b48d7f46e89392cee8225353f8daa88ec5e174d59a4` | 2026-11-26T02:18:20Z | editorial register of every AA note the captures record (the chart's footnotes, and from O103 the model pages, Coding Agent Index and cost charts), by exact text, each classified once (O100, O103) |
| anchors | `data/v3_frozen.json` | `be41344428122d2523923c9a3a0829b4b2719b0bde3525ebb51056048cab246d` | 2026-11-26 | valuerank.value_v3 freeze |
| anchors:aicd | `data/v3_frozen_aicd.json` | `585e7324873c5356b5909f27649eff930acbb981fb9b1bd640c068c00ba9ddd0` | 2026-11-26 | valuerank.value_v3 freeze |
| anchors:common | `data/v3_frozen_common.json` | `0dc3f29120fea4cd96456fb5e751aea7742c559dad512a659832b573ff467326` | 2026-11-26 | valuerank.value_v3 freeze |


## AA intelligence and total-cost comparison

Observed 2026-11-26T02:18:20Z; Artificial Analysis Intelligence Index v5.0. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 155 catalog models selected; 136 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 155 models, plotted 136 eligible points, and displayed 20 frontier points. Public metric/export gaps are shown explicitly. All 8 distinct frontier model families are required in the main ranking using exact selected configurations; 4 are included. Other effort configurations remain separate comparison entries. 11 plotted configurations from 9 families lie within 3 Index points of the rendered frontier; 5 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 10 (rounded) | $9.09 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 18 (rounded) | $39.55 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 19 (rounded) | $39.60 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 21 (rounded) | $62.58 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 25 (rounded) | $72.70 | Observed AA frontier | Primary ranked | None |
| [Muse Ember (xhigh)](https://artificialanalysis.ai/models/muse-ember-xhigh) | muse-ember-xhigh | 34 (rounded) | $95.73 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| [Muse Ember (max)](https://artificialanalysis.ai/models/muse-ember) | muse-ember | 36 (rounded) | $117.12 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no Bug Hunt Bench, GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.1 Terra (medium)](https://artificialanalysis.ai/models/gpt-6-1-terra-medium) | gpt-6-1-terra-medium | 38 (rounded) | $190.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6.2 Sol (low)](https://artificialanalysis.ai/models/gpt-6-2-sol-low) | gpt-6-2-sol-low | 41 (rounded) | $224.22 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.1 Terra (high)](https://artificialanalysis.ai/models/gpt-6-1-terra-high) | gpt-6-1-terra-high | 43 (rounded) | $266.79 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 46 (rounded) | $388.57 | Observed AA frontier | Primary ranked | None |
| [GPT-6.2 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-2-sol-medium) | gpt-6-2-sol-medium | 52 (rounded) | $405.17 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.2 Sol (high)](https://artificialanalysis.ai/models/gpt-6-2-sol-high) | gpt-6-2-sol-high | 55 (rounded) | $552.68 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.2 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-2-sol-xhigh) | gpt-6-2-sol-xhigh | 56 (rounded) | $698.10 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.2 Sol (max)](https://artificialanalysis.ai/models/gpt-6-2-sol) | gpt-6-2-sol | 57 (rounded) | $1,108.28 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.2 Astra (high)](https://artificialanalysis.ai/models/gpt-6-2-astra-high) | gpt-6-2-astra-high | 60 (rounded) | $2,006.78 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.2 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-2-astra-xhigh) | gpt-6-2-astra-xhigh | 62 (rounded) | $2,483.62 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| [GPT-6.2 Astra (max)](https://artificialanalysis.ai/models/gpt-6-2-astra) | gpt-6-2-astra | 62 (rounded) | $4,530.46 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), GDPval-AA v2.1, AA-LCR v1.1 |
| [Claude Fable 5.2 (xhigh)](https://artificialanalysis.ai/models/claude-fable-5-2-xhigh) | claude-fable-5-2-xhigh | 62 (rounded) | $11,741.62 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals); AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Claude Fable 5.2 (max)](https://artificialanalysis.ai/models/claude-fable-5-2) | claude-fable-5-2 | 65 (rounded) | $22,191.42 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 23 (rounded) | $85.74 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 35 (rounded) | $192.70 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6.1 Terra (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-terra-xhigh) | gpt-6-1-terra-xhigh | 45 (rounded) | $400.18 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 55 (rounded) | $1,123.97 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6.2 Astra (medium)](https://artificialanalysis.ai/models/gpt-6-2-astra-medium) | gpt-6-2-astra-medium | 57 (rounded) | $1,456.80 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [Gemini 4 Neon (medium)](https://artificialanalysis.ai/models/gemini-4-neon-medium) | gemini-4-neon-medium | 55 (rounded) | $1,865.54 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [Gemini 4 Neon (high)](https://artificialanalysis.ai/models/gemini-4-neon-high) | gemini-4-neon-high | 60 (rounded) | $3,694.62 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall, GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [Claude Fable 5.2 (high)](https://artificialanalysis.ai/models/claude-fable-5-2-high) | claude-fable-5-2-high | 62 (rounded) | $7,105.77 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Gemini 4 Neon (xhigh)](https://artificialanalysis.ai/models/gemini-4-neon) | gemini-4-neon | 62 (rounded) | $7,787.91 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), GDPval-AA v2.1, AA-LCR v1.1; AI Coding Daily ranking: no GDPval-AA v2.1, AA-LCR v1.1 |
| [Gemini 4 Carbon (high)](https://artificialanalysis.ai/models/gemini-4-carbon) | gemini-4-carbon | 60 (rounded) | $8,239.69 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Code Migration v1.1 (Vals), AA-LCR v1.1; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding), AA-LCR v1.1 |
| [Claude Opus 5.5 (max)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 59 (rounded) | $8,909.67 | Near AA frontier (within 3 Index points) | Primary ranked | None |
