# ValueRank v3.0.0 Raw Data

**Updated:** October 19, 2026 · methodology 3.0.0

Every input behind the published scores, with the artifact and locator that holds it. Generated from the committed snapshots in [data/](data/); nothing here is edited by hand.

## Quality leaf inputs

| Configuration | Leaf | Raw value | Unit | Score z | Evaluated configuration / agent | Evidence |
|---|---|---:|---|---:|---|---|
| Claude Opus 5.5 (max) | FrontierCode 2.0 | 0.464359595959596 | fraction | 46.44 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.frontierCode20` |
| Claude Opus 5.5 (max) | Terminal-Bench 4.0 (AA run) | 59.5959595959596 | percent | 59.60 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.terminalBench40` |
| Claude Opus 5.5 (max) | Bug Hunt Bench | 41.7 | bugs fixed of 105 | 39.71 | Opus 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5].fixedOf105` |
| Claude Opus 5.5 (max) | Vibe Code Bench v1.1 (Vals) | 90.294 | percent | 90.29 | anthropic/claude-opus-5-5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=vibeCode].value` |
| Claude Opus 5.5 (max) | Code Migration v1.1 (Vals) | 81.012 | percent | 81.01 | anthropic/claude-opus-5-5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=codeMigration].value` |
| Claude Opus 5.5 (max) | LiveBench 2.0 Overall | 85.14 | percent | 85.14 | claude-opus-5.5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=livebench2Overall].value` |
| Claude Opus 5.5 (max) | GDPval-AA v2.1 | 1866.27 | Elo | 68.31 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.gdpval` |
| Claude Opus 5.5 (max) | AutomationBench-AA | 0.6953868128636069 | fraction | 69.54 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.automationBenchPartialScore` |
| Claude Opus 5.5 (max) | AA-Omniscience v1.1 | 48.13333333333333 | AA Omniscience Index | 74.07 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.omniscience` |
| Claude Opus 5.5 (max) | AA-LCR v1.1 | 0.846666666666667 | fraction | 84.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.lcr` |
| Claude Opus 5.5 (max) | HLE-Diamond | 0.679 | fraction | 67.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.hleDiamond` |
| Claude Opus 5.5 (max) | Terminal-Bench-Science 0.1 | 0.59047619047619 | fraction | 59.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.terminalBenchScience` |
| Claude Opus 5.5 (max) | CritPt v2 (hard subset) | 0.61 | fraction | 61.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.critptAgenticHard` |
| Claude Sonnet 5.5 (max) | FrontierCode 2.0 | 0.416993434343434 | fraction | 41.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.frontierCode20` |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.0 (AA run) | 63.636363636363605 | percent | 63.64 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.terminalBench40` |
| Claude Sonnet 5.5 (max) | Bug Hunt Bench | 51.3 | bugs fixed of 105 | 48.86 | Sonnet 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5].fixedOf105` |
| Claude Sonnet 5.5 (max) | Vibe Code Bench v1.1 (Vals) | 92.392 | percent | 92.39 | anthropic/claude-sonnet-5-5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=vibeCode].value` |
| Claude Sonnet 5.5 (max) | Code Migration v1.1 (Vals) | 86.875 | percent | 86.88 | anthropic/claude-sonnet-5-5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=codeMigration].value` |
| Claude Sonnet 5.5 (max) | LiveBench 2.0 Overall | 80.04 | percent | 80.04 | claude-sonnet-5.5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=livebench2Overall].value` |
| Claude Sonnet 5.5 (max) | GDPval-AA v2.1 | 1837.82 | Elo | 66.89 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.gdpval` |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | 0.7176882128193995 | fraction | 71.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (max) | AA-Omniscience v1.1 | 30.466666666666665 | AA Omniscience Index | 65.23 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.omniscience` |
| Claude Sonnet 5.5 (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.lcr` |
| Claude Sonnet 5.5 (max) | HLE-Diamond | 0.533 | fraction | 53.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.hleDiamond` |
| Claude Sonnet 5.5 (max) | Terminal-Bench-Science 0.1 | 0.533333333333333 | fraction | 53.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.terminalBenchScience` |
| Claude Sonnet 5.5 (max) | CritPt v2 (hard subset) | 0.56 | fraction | 56.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.critptAgenticHard` |
| GPT-6.1 Sol (max) | FrontierCode 2.0 | 0.406262878787879 | fraction | 40.63 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.frontierCode20` |
| GPT-6.1 Sol (max) | Terminal-Bench 4.0 (AA run) | 56.0606060606061 | percent | 56.06 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.terminalBench40` |
| GPT-6.1 Sol (max) | Bug Hunt Bench | 44.3 | bugs fixed of 105 | 42.19 | GPT-6.1 Sol (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol].fixedOf105` |
| GPT-6.1 Sol (max) | Vibe Code Bench v1.1 (Vals) | 88.931 | percent | 88.93 | openai/gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=vibeCode].value` |
| GPT-6.1 Sol (max) | Code Migration v1.1 (Vals) | 77.324 | percent | 77.32 | openai/gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=codeMigration].value` |
| GPT-6.1 Sol (max) | LiveBench 2.0 Overall | 84.07 | percent | 84.07 | gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=livebench2Overall].value` |
| GPT-6.1 Sol (max) | GDPval-AA v2.1 | 1608.89 | Elo | 55.44 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.gdpval` |
| GPT-6.1 Sol (max) | AutomationBench-AA | 0.6486844882398171 | fraction | 64.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.automationBenchPartialScore` |
| GPT-6.1 Sol (max) | AA-Omniscience v1.1 | 42.03333333333333 | AA Omniscience Index | 71.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.omniscience` |
| GPT-6.1 Sol (max) | AA-LCR v1.1 | 0.83 | fraction | 83.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.lcr` |
| GPT-6.1 Sol (max) | HLE-Diamond | 0.588 | fraction | 58.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.hleDiamond` |
| GPT-6.1 Sol (max) | Terminal-Bench-Science 0.1 | 0.580952380952381 | fraction | 58.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.terminalBenchScience` |
| GPT-6.1 Sol (max) | CritPt v2 (hard subset) | 0.685 | fraction | 68.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.critptAgenticHard` |
| GPT-6 Astra (max) | FrontierCode 2.0 | 0.42374797979798 | fraction | 42.37 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.frontierCode20` |
| GPT-6 Astra (max) | Terminal-Bench 4.0 (AA run) | 59.09090909090911 | percent | 59.09 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.terminalBench40` |
| GPT-6 Astra (max) | Bug Hunt Bench | 45.0 | bugs fixed of 105 | 42.86 | GPT-6 Astra (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-astra].fixedOf105` |
| GPT-6 Astra (max) | Vibe Code Bench v1.1 (Vals) | 89.594 | percent | 89.59 | openai/gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=vibeCode].value` |
| GPT-6 Astra (max) | Code Migration v1.1 (Vals) | 80.579 | percent | 80.58 | openai/gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=codeMigration].value` |
| GPT-6 Astra (max) | LiveBench 2.0 Overall | 85.64 | percent | 85.64 | gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=livebench2Overall].value` |
| GPT-6 Astra (max) | GDPval-AA v2.1 | 1583.69 | Elo | 54.18 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.gdpval` |
| GPT-6 Astra (max) | AutomationBench-AA | 0.6849174806688876 | fraction | 68.49 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.automationBenchPartialScore` |
| GPT-6 Astra (max) | AA-Omniscience v1.1 | 42.43333333333333 | AA Omniscience Index | 71.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.omniscience` |
| GPT-6 Astra (max) | AA-LCR v1.1 | 0.806666666666667 | fraction | 80.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.lcr` |
| GPT-6 Astra (max) | HLE-Diamond | 0.638 | fraction | 63.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.hleDiamond` |
| GPT-6 Astra (max) | Terminal-Bench-Science 0.1 | 0.633333333333333 | fraction | 63.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.terminalBenchScience` |
| GPT-6 Astra (max) | CritPt v2 (hard subset) | 0.705 | fraction | 70.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.critptAgenticHard` |
| GPT-6 Luna (max) | FrontierCode 2.0 | 0.251747727272727 | fraction | 25.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.frontierCode20` |
| GPT-6 Luna (max) | Terminal-Bench 4.0 (AA run) | 12.6262626262626 | percent | 12.63 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.terminalBench40` |
| GPT-6 Luna (max) | Bug Hunt Bench | 18.3 | bugs fixed of 105 | 17.43 | GPT-6 Luna (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-luna].fixedOf105` |
| GPT-6 Luna (max) | Vibe Code Bench v1.1 (Vals) | 81.649 | percent | 81.65 | openai/gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=vibeCode].value` |
| GPT-6 Luna (max) | Code Migration v1.1 (Vals) | 46.669 | percent | 46.67 | openai/gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=codeMigration].value` |
| GPT-6 Luna (max) | LiveBench 2.0 Overall | 64.59 | percent | 64.59 | gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=livebench2Overall].value` |
| GPT-6 Luna (max) | GDPval-AA v2.1 | 1444.46 | Elo | 47.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.gdpval` |
| GPT-6 Luna (max) | AutomationBench-AA | 0.5316814034483175 | fraction | 53.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.automationBenchPartialScore` |
| GPT-6 Luna (max) | AA-Omniscience v1.1 | -8.266666666666667 | AA Omniscience Index | 45.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.omniscience` |
| GPT-6 Luna (max) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.lcr` |
| GPT-6 Luna (max) | HLE-Diamond | 0.222 | fraction | 22.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.hleDiamond` |
| GPT-6 Luna (max) | Terminal-Bench-Science 0.1 | 0.0857142857142857 | fraction | 8.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.terminalBenchScience` |
| GPT-6 Luna (max) | CritPt v2 (hard subset) | 0.415 | fraction | 41.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.critptAgenticHard` |
| Claude Opus 5.5 (high) | FrontierCode 2.0 | 0.359278535353535 | fraction | 35.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.frontierCode20` |
| Claude Opus 5.5 (high) | Terminal-Bench 4.0 (AA run) | 56.565656565656596 | percent | 56.57 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.terminalBench40` |
| Claude Opus 5.5 (high) | Bug Hunt Bench | 31.7 | bugs fixed of 105 | 30.19 | Opus 5.5 (high effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5-high].fixedOf105` |
| Claude Opus 5.5 (high) | AI Coding Daily (excl. bug finding) | 57.68 | points of 60 | 96.13 | Opus 5.5 (High) | `data/swe_tracks.json` `records[modelId=claude-opus-5-5-high, leaf=aiCodingDaily].value` |
| Claude Opus 5.5 (high) | GDPval-AA v2.1 | 1713.6 | Elo | 60.68 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.gdpval` |
| Claude Opus 5.5 (high) | AutomationBench-AA | 0.6320677483186213 | fraction | 63.21 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.automationBenchPartialScore` |
| Claude Opus 5.5 (high) | AA-Omniscience v1.1 | 42.36666666666667 | AA Omniscience Index | 71.18 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.omniscience` |
| Claude Opus 5.5 (high) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.lcr` |
| Claude Opus 5.5 (high) | HLE-Diamond | 0.556 | fraction | 55.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.hleDiamond` |
| Claude Opus 5.5 (high) | Terminal-Bench-Science 0.1 | 0.49047619047619 | fraction | 49.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.terminalBenchScience` |
| Claude Opus 5.5 (high) | CritPt v2 (hard subset) | 0.58 | fraction | 58.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.critptAgenticHard` |
| GPT-6.1 Sol (high) | FrontierCode 2.0 | 0.36737297979798 | fraction | 36.74 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.frontierCode20` |
| GPT-6.1 Sol (high) | Terminal-Bench 4.0 (AA run) | 51.5151515151515 | percent | 51.52 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.terminalBench40` |
| GPT-6.1 Sol (high) | Bug Hunt Bench | 36.5 | bugs fixed of 105 | 34.76 | GPT-6.1 Sol (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-high].fixedOf105` |
| GPT-6.1 Sol (high) | AI Coding Daily (excl. bug finding) | 56.83 | points of 60 | 94.72 | GPT-6.1-Sol (High) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-high, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (high) | GDPval-AA v2.1 | 1520.45 | Elo | 51.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.gdpval` |
| GPT-6.1 Sol (high) | AutomationBench-AA | 0.6449523732184466 | fraction | 64.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.automationBenchPartialScore` |
| GPT-6.1 Sol (high) | AA-Omniscience v1.1 | 41 | AA Omniscience Index | 70.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.omniscience` |
| GPT-6.1 Sol (high) | AA-LCR v1.1 | 0.823333333333333 | fraction | 82.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.lcr` |
| GPT-6.1 Sol (high) | HLE-Diamond | 0.519 | fraction | 51.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.hleDiamond` |
| GPT-6.1 Sol (high) | Terminal-Bench-Science 0.1 | 0.461904761904762 | fraction | 46.19 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.terminalBenchScience` |
| GPT-6.1 Sol (high) | CritPt v2 (hard subset) | 0.675 | fraction | 67.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.critptAgenticHard` |
| Claude Haiku 5.5 (high) | FrontierCode 2.0 | 0.232000505050505 | fraction | 23.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.frontierCode20` |
| Claude Haiku 5.5 (high) | Terminal-Bench 4.0 (AA run) | 21.7171717171717 | percent | 21.72 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.terminalBench40` |
| Claude Haiku 5.5 (high) | Bug Hunt Bench | 16.0 | bugs fixed of 105 | 15.24 | Haiku 5.5 (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-high].fixedOf105` |
| Claude Haiku 5.5 (high) | AI Coding Daily (excl. bug finding) | 51.55 | points of 60 | 85.92 | Haiku 5.5 (High) | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-high, leaf=aiCodingDaily].value` |
| Claude Haiku 5.5 (high) | GDPval-AA v2.1 | 1424.29 | Elo | 46.21 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.gdpval` |
| Claude Haiku 5.5 (high) | AutomationBench-AA | 0.3372685311767238 | fraction | 33.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (high) | AA-Omniscience v1.1 | 5.3 | AA Omniscience Index | 52.65 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.omniscience` |
| Claude Haiku 5.5 (high) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.lcr` |
| Claude Haiku 5.5 (high) | HLE-Diamond | 0.237 | fraction | 23.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.hleDiamond` |
| Claude Haiku 5.5 (high) | Terminal-Bench-Science 0.1 | 0.1 | fraction | 10.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.terminalBenchScience` |
| Claude Haiku 5.5 (high) | CritPt v2 (hard subset) | 0.425 | fraction | 42.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.critptAgenticHard` |
| GPT-6.1 Terra (max) | FrontierCode 2.0 | 0.423200505050505 | fraction | 42.32 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.frontierCode20` |
| GPT-6.1 Terra (max) | Terminal-Bench 4.0 (AA run) | 55.5555555555556 | percent | 55.56 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.terminalBench40` |
| GPT-6.1 Terra (max) | Bug Hunt Bench | 40.7 | bugs fixed of 105 | 38.76 | GPT-6.1 Terra (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra].fixedOf105` |
| GPT-6.1 Terra (max) | AI Coding Daily (excl. bug finding) | 52.49 | points of 60 | 87.48 | GPT-6.1-Terra (Max) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (max) | GDPval-AA v2.1 | 1475.63 | Elo | 48.78 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.gdpval` |
| GPT-6.1 Terra (max) | AutomationBench-AA | 0.6016762327257726 | fraction | 60.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.automationBenchPartialScore` |
| GPT-6.1 Terra (max) | AA-Omniscience v1.1 | 29.566666666666666 | AA Omniscience Index | 64.78 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.omniscience` |
| GPT-6.1 Terra (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.lcr` |
| GPT-6.1 Terra (max) | HLE-Diamond | 0.473 | fraction | 47.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.hleDiamond` |
| GPT-6.1 Terra (max) | Terminal-Bench-Science 0.1 | 0.576190476190476 | fraction | 57.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.terminalBenchScience` |
| GPT-6.1 Terra (max) | CritPt v2 (hard subset) | 0.645 | fraction | 64.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra].model.critptAgenticHard` |
| GPT-6.1 Sol (medium) | FrontierCode 2.0 | 0.333875757575758 | fraction | 33.39 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.frontierCode20` |
| GPT-6.1 Sol (medium) | Terminal-Bench 4.0 (AA run) | 47.979797979798 | percent | 47.98 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.terminalBench40` |
| GPT-6.1 Sol (medium) | Bug Hunt Bench | 29.0 | bugs fixed of 105 | 27.62 | GPT-6.1 Sol (medium effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-medium].fixedOf105` |
| GPT-6.1 Sol (medium) | AI Coding Daily (excl. bug finding) | 55.67 | points of 60 | 92.78 | GPT-6.1-Sol (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-medium, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (medium) | GDPval-AA v2.1 | 1459.05 | Elo | 47.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.gdpval` |
| GPT-6.1 Sol (medium) | AutomationBench-AA | 0.6257350970435687 | fraction | 62.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.automationBenchPartialScore` |
| GPT-6.1 Sol (medium) | AA-Omniscience v1.1 | 40.166666666666664 | AA Omniscience Index | 70.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.omniscience` |
| GPT-6.1 Sol (medium) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.lcr` |
| GPT-6.1 Sol (medium) | HLE-Diamond | 0.46 | fraction | 46.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.hleDiamond` |
| GPT-6.1 Sol (medium) | Terminal-Bench-Science 0.1 | 0.371428571428571 | fraction | 37.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.terminalBenchScience` |
| GPT-6.1 Sol (medium) | CritPt v2 (hard subset) | 0.65 | fraction | 65.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.critptAgenticHard` |
| Claude Haiku 5.5 (medium) | FrontierCode 2.0 | 0.16091994949495 | fraction | 16.09 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.frontierCode20` |
| Claude Haiku 5.5 (medium) | Terminal-Bench 4.0 (AA run) | 15.151515151515198 | percent | 15.15 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.terminalBench40` |
| Claude Haiku 5.5 (medium) | Bug Hunt Bench | 12.0 | bugs fixed of 105 | 11.43 | Haiku 5.5 (medium effort) | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-medium].fixedOf105` |
| Claude Haiku 5.5 (medium) | AI Coding Daily (excl. bug finding) | 51.32 | points of 60 | 85.53 | Haiku 5.5 (Medium) | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-medium, leaf=aiCodingDaily].value` |
| Claude Haiku 5.5 (medium) | GDPval-AA v2.1 | 1282.5 | Elo | 39.12 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.gdpval` |
| Claude Haiku 5.5 (medium) | AutomationBench-AA | 0.2858961481429316 | fraction | 28.59 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (medium) | AA-Omniscience v1.1 | 4.166666666666667 | AA Omniscience Index | 52.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.omniscience` |
| Claude Haiku 5.5 (medium) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.lcr` |
| Claude Haiku 5.5 (medium) | HLE-Diamond | 0.168 | fraction | 16.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.hleDiamond` |
| Claude Haiku 5.5 (medium) | Terminal-Bench-Science 0.1 | 0.0714285714285714 | fraction | 7.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.terminalBenchScience` |
| Claude Haiku 5.5 (medium) | CritPt v2 (hard subset) | 0.3 | fraction | 30.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.critptAgenticHard` |
| GPT-6.1 Terra (high) | FrontierCode 2.0 | 0.37457904040404 | fraction | 37.46 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.frontierCode20` |
| GPT-6.1 Terra (high) | Terminal-Bench 4.0 (AA run) | 41.9191919191919 | percent | 41.92 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.terminalBench40` |
| GPT-6.1 Terra (high) | Bug Hunt Bench | 9.7 | bugs fixed of 105 | 9.24 | GPT-6.1 Terra (high effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-high].fixedOf105` |
| GPT-6.1 Terra (high) | AI Coding Daily (excl. bug finding) | 46.69 | points of 60 | 77.82 | GPT-6.1-Terra (High) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra-high, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (high) | GDPval-AA v2.1 | 1352.74 | Elo | 42.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.gdpval` |
| GPT-6.1 Terra (high) | AutomationBench-AA | 0.584605963496433 | fraction | 58.46 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.automationBenchPartialScore` |
| GPT-6.1 Terra (high) | AA-Omniscience v1.1 | 27.766666666666666 | AA Omniscience Index | 63.88 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.omniscience` |
| GPT-6.1 Terra (high) | AA-LCR v1.1 | 0.823333333333333 | fraction | 82.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.lcr` |
| GPT-6.1 Terra (high) | HLE-Diamond | 0.354 | fraction | 35.40 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.hleDiamond` |
| GPT-6.1 Terra (high) | Terminal-Bench-Science 0.1 | 0.333333333333333 | fraction | 33.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.terminalBenchScience` |
| GPT-6.1 Terra (high) | CritPt v2 (hard subset) | 0.605 | fraction | 60.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-high].model.critptAgenticHard` |
| GPT-6.1 Terra (xhigh) | FrontierCode 2.0 | 0.368595202020202 | fraction | 36.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.frontierCode20` |
| GPT-6.1 Terra (xhigh) | Terminal-Bench 4.0 (AA run) | 46.4646464646465 | percent | 46.46 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.terminalBench40` |
| GPT-6.1 Terra (xhigh) | Bug Hunt Bench | 11.3 | bugs fixed of 105 | 10.76 | GPT-6.1 Terra (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-xhigh].fixedOf105` |
| GPT-6.1 Terra (xhigh) | AI Coding Daily (excl. bug finding) | 48.13 | points of 60 | 80.22 | GPT-6.1-Terra (Xhigh) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra-xhigh, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (xhigh) | GDPval-AA v2.1 | 1414.87 | Elo | 45.74 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.gdpval` |
| GPT-6.1 Terra (xhigh) | AutomationBench-AA | 0.5992855956353923 | fraction | 59.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.automationBenchPartialScore` |
| GPT-6.1 Terra (xhigh) | AA-Omniscience v1.1 | 28.933333333333334 | AA Omniscience Index | 64.47 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.omniscience` |
| GPT-6.1 Terra (xhigh) | AA-LCR v1.1 | 0.816666666666667 | fraction | 81.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.lcr` |
| GPT-6.1 Terra (xhigh) | HLE-Diamond | 0.423 | fraction | 42.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.hleDiamond` |
| GPT-6.1 Terra (xhigh) | Terminal-Bench-Science 0.1 | 0.419047619047619 | fraction | 41.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.terminalBenchScience` |
| GPT-6.1 Terra (xhigh) | CritPt v2 (hard subset) | 0.575 | fraction | 57.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-xhigh].model.critptAgenticHard` |
| GPT-6 Astra (high) | FrontierCode 2.0 | 0.401351515151515 | fraction | 40.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.frontierCode20` |
| GPT-6 Astra (high) | Terminal-Bench 4.0 (AA run) | 54.040404040404 | percent | 54.04 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.terminalBench40` |
| GPT-6 Astra (high) | Bug Hunt Bench | 35.0 | bugs fixed of 105 | 33.33 | GPT-6 Astra (high effort) | `data/bug_hunt.json` `models[modelId=gpt-6-astra-high].fixedOf105` |
| GPT-6 Astra (high) | AI Coding Daily (excl. bug finding) | 56.77 | points of 60 | 94.62 | GPT-6-Astra (High) | `data/swe_tracks.json` `records[modelId=gpt-6-astra-high, leaf=aiCodingDaily].value` |
| GPT-6 Astra (high) | GDPval-AA v2.1 | 1536.04 | Elo | 51.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.gdpval` |
| GPT-6 Astra (high) | AutomationBench-AA | 0.666122174975011 | fraction | 66.61 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.automationBenchPartialScore` |
| GPT-6 Astra (high) | AA-Omniscience v1.1 | 44.56666666666667 | AA Omniscience Index | 72.28 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.omniscience` |
| GPT-6 Astra (high) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.lcr` |
| GPT-6 Astra (high) | HLE-Diamond | 0.593 | fraction | 59.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.hleDiamond` |
| GPT-6 Astra (high) | Terminal-Bench-Science 0.1 | 0.595238095238095 | fraction | 59.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.terminalBenchScience` |
| GPT-6 Astra (high) | CritPt v2 (hard subset) | 0.715 | fraction | 71.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.critptAgenticHard` |
| GPT-6.1 Terra (medium) | FrontierCode 2.0 | 0.345359343434343 | fraction | 34.54 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.frontierCode20` |
| GPT-6.1 Terra (medium) | Terminal-Bench 4.0 (AA run) | 32.3232323232323 | percent | 32.32 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.terminalBench40` |
| GPT-6.1 Terra (medium) | Bug Hunt Bench | 7.3 | bugs fixed of 105 | 6.95 | GPT-6.1 Terra (medium effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-medium].fixedOf105` |
| GPT-6.1 Terra (medium) | AI Coding Daily (excl. bug finding) | 46.9 | points of 60 | 78.17 | GPT-6.1-Terra (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6.1-terra-medium, leaf=aiCodingDaily].value` |
| GPT-6.1 Terra (medium) | GDPval-AA v2.1 | 1324.7 | Elo | 41.23 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.gdpval` |
| GPT-6.1 Terra (medium) | AutomationBench-AA | 0.5780171778957812 | fraction | 57.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.automationBenchPartialScore` |
| GPT-6.1 Terra (medium) | AA-Omniscience v1.1 | 26.6 | AA Omniscience Index | 63.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.omniscience` |
| GPT-6.1 Terra (medium) | AA-LCR v1.1 | 0.806666666666667 | fraction | 80.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.lcr` |
| GPT-6.1 Terra (medium) | HLE-Diamond | 0.313 | fraction | 31.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.hleDiamond` |
| GPT-6.1 Terra (medium) | Terminal-Bench-Science 0.1 | 0.247619047619048 | fraction | 24.76 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.terminalBenchScience` |
| GPT-6.1 Terra (medium) | CritPt v2 (hard subset) | 0.56 | fraction | 56.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-medium].model.critptAgenticHard` |
| GPT-6.1 Sol (low) | FrontierCode 2.0 | 0.201560858585859 | fraction | 20.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.frontierCode20` |
| GPT-6.1 Sol (low) | Terminal-Bench 4.0 (AA run) | 30.808080808080803 | percent | 30.81 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.terminalBench40` |
| GPT-6.1 Sol (low) | Bug Hunt Bench | 22.5 | bugs fixed of 105 | 21.43 | GPT-6.1 Sol (low effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-low].fixedOf105` |
| GPT-6.1 Sol (low) | AI Coding Daily (excl. bug finding) | 52.7 | points of 60 | 87.83 | GPT-6.1-Sol (Low) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-low, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (low) | GDPval-AA v2.1 | 1321.98 | Elo | 41.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.gdpval` |
| GPT-6.1 Sol (low) | AutomationBench-AA | 0.5257088964747538 | fraction | 52.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.automationBenchPartialScore` |
| GPT-6.1 Sol (low) | AA-Omniscience v1.1 | 38 | AA Omniscience Index | 69.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.omniscience` |
| GPT-6.1 Sol (low) | AA-LCR v1.1 | 0.84 | fraction | 84.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.lcr` |
| GPT-6.1 Sol (low) | HLE-Diamond | 0.382 | fraction | 38.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.hleDiamond` |
| GPT-6.1 Sol (low) | Terminal-Bench-Science 0.1 | 0.10952380952381 | fraction | 10.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.terminalBenchScience` |
| GPT-6.1 Sol (low) | CritPt v2 (hard subset) | 0.595 | fraction | 59.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.critptAgenticHard` |
| GPT-6 Luna (max) | AI Coding Daily (excl. bug finding) | 51.99 | points of 60 | 86.65 | GPT-6-Luna (Max) | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=aiCodingDaily].value` |
| GPT-6 Luna (xhigh) | FrontierCode 2.0 | 0.184238888888889 | fraction | 18.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.frontierCode20` |
| GPT-6 Luna (xhigh) | Terminal-Bench 4.0 (AA run) | 8.08080808080808 | percent | 8.08 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.terminalBench40` |
| GPT-6 Luna (xhigh) | Bug Hunt Bench | 14.0 | bugs fixed of 105 | 13.33 | GPT-6 Luna (xhigh effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-xhigh].fixedOf105` |
| GPT-6 Luna (xhigh) | AI Coding Daily (excl. bug finding) | 49.94 | points of 60 | 83.23 | GPT-6-Luna (Xhigh) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-xhigh, leaf=aiCodingDaily].value` |
| GPT-6 Luna (xhigh) | GDPval-AA v2.1 | 1372.52 | Elo | 43.63 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.gdpval` |
| GPT-6 Luna (xhigh) | AutomationBench-AA | 0.47800686767566575 | fraction | 47.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.automationBenchPartialScore` |
| GPT-6 Luna (xhigh) | AA-Omniscience v1.1 | -12.966666666666667 | AA Omniscience Index | 43.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.omniscience` |
| GPT-6 Luna (xhigh) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.lcr` |
| GPT-6 Luna (xhigh) | HLE-Diamond | 0.189 | fraction | 18.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.hleDiamond` |
| GPT-6 Luna (xhigh) | Terminal-Bench-Science 0.1 | 0.0523809523809524 | fraction | 5.24 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.terminalBenchScience` |
| GPT-6 Luna (xhigh) | CritPt v2 (hard subset) | 0.355 | fraction | 35.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.critptAgenticHard` |
| GPT-6 Luna (high) | FrontierCode 2.0 | 0.186015151515152 | fraction | 18.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.frontierCode20` |
| GPT-6 Luna (high) | Terminal-Bench 4.0 (AA run) | 4.545454545454549 | percent | 4.55 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.terminalBench40` |
| GPT-6 Luna (high) | Bug Hunt Bench | 9.0 | bugs fixed of 105 | 8.57 | GPT-6 Luna (high effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-high].fixedOf105` |
| GPT-6 Luna (high) | AI Coding Daily (excl. bug finding) | 47.73 | points of 60 | 79.55 | GPT-6-Luna (High) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-high, leaf=aiCodingDaily].value` |
| GPT-6 Luna (high) | GDPval-AA v2.1 | 1352.1 | Elo | 42.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.gdpval` |
| GPT-6 Luna (high) | AutomationBench-AA | 0.4782449139916615 | fraction | 47.82 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.automationBenchPartialScore` |
| GPT-6 Luna (high) | AA-Omniscience v1.1 | -12.8 | AA Omniscience Index | 43.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.omniscience` |
| GPT-6 Luna (high) | AA-LCR v1.1 | 0.793333333333333 | fraction | 79.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.lcr` |
| GPT-6 Luna (high) | HLE-Diamond | 0.156 | fraction | 15.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.hleDiamond` |
| GPT-6 Luna (high) | Terminal-Bench-Science 0.1 | 0.0285714285714286 | fraction | 2.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.terminalBenchScience` |
| GPT-6 Luna (high) | CritPt v2 (hard subset) | 0.305 | fraction | 30.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.critptAgenticHard` |
| GPT-6 Luna (medium) | FrontierCode 2.0 | 0.127693181818182 | fraction | 12.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.frontierCode20` |
| GPT-6 Luna (medium) | Terminal-Bench 4.0 (AA run) | 2.52525252525253 | percent | 2.53 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.terminalBench40` |
| GPT-6 Luna (medium) | Bug Hunt Bench | 4.0 | bugs fixed of 105 | 3.81 | GPT-6 Luna (medium effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-medium].fixedOf105` |
| GPT-6 Luna (medium) | AI Coding Daily (excl. bug finding) | 40.2 | points of 60 | 67.00 | GPT-6-Luna (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-medium, leaf=aiCodingDaily].value` |
| GPT-6 Luna (medium) | GDPval-AA v2.1 | 1270.45 | Elo | 38.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.gdpval` |
| GPT-6 Luna (medium) | AutomationBench-AA | 0.4046136879135791 | fraction | 40.46 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.automationBenchPartialScore` |
| GPT-6 Luna (medium) | AA-Omniscience v1.1 | -13.566666666666666 | AA Omniscience Index | 43.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.omniscience` |
| GPT-6 Luna (medium) | AA-LCR v1.1 | 0.783333333333333 | fraction | 78.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.lcr` |
| GPT-6 Luna (medium) | HLE-Diamond | 0.151 | fraction | 15.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.hleDiamond` |
| GPT-6 Luna (medium) | Terminal-Bench-Science 0.1 | 0.0142857142857143 | fraction | 1.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.terminalBenchScience` |
| GPT-6 Luna (medium) | CritPt v2 (hard subset) | 0.26 | fraction | 26.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.critptAgenticHard` |
| Claude Opus 5.5 (xhigh) | FrontierCode 2.0 | 0.437547474747475 | fraction | 43.75 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.frontierCode20` |
| Claude Opus 5.5 (xhigh) | Terminal-Bench 4.0 (AA run) | 59.5959595959596 | percent | 59.60 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.terminalBench40` |
| Claude Opus 5.5 (xhigh) | Bug Hunt Bench | 36.0 | bugs fixed of 105 | 34.29 | Opus 5.5 (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5-xhigh].fixedOf105` |
| Claude Opus 5.5 (xhigh) | GDPval-AA v2.1 | 1835.03 | Elo | 66.75 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.gdpval` |
| Claude Opus 5.5 (xhigh) | AutomationBench-AA | 0.6495283516401527 | fraction | 64.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.automationBenchPartialScore` |
| Claude Opus 5.5 (xhigh) | AA-Omniscience v1.1 | 43.13333333333333 | AA Omniscience Index | 71.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.omniscience` |
| Claude Opus 5.5 (xhigh) | AA-LCR v1.1 | 0.846666666666667 | fraction | 84.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.lcr` |
| Claude Opus 5.5 (xhigh) | HLE-Diamond | 0.64 | fraction | 64.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.hleDiamond` |
| Claude Opus 5.5 (xhigh) | Terminal-Bench-Science 0.1 | 0.619047619047619 | fraction | 61.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.terminalBenchScience` |
| Claude Opus 5.5 (xhigh) | CritPt v2 (hard subset) | 0.63 | fraction | 63.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-xhigh].model.critptAgenticHard` |
| GPT-6.1 Sol (xhigh) | FrontierCode 2.0 | 0.385190909090909 | fraction | 38.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.frontierCode20` |
| GPT-6.1 Sol (xhigh) | Terminal-Bench 4.0 (AA run) | 54.040404040404 | percent | 54.04 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.terminalBench40` |
| GPT-6.1 Sol (xhigh) | Bug Hunt Bench | 42.7 | bugs fixed of 105 | 40.67 | GPT-6.1 Sol (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-xhigh].fixedOf105` |
| GPT-6.1 Sol (xhigh) | GDPval-AA v2.1 | 1554.8 | Elo | 52.74 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.gdpval` |
| GPT-6.1 Sol (xhigh) | AutomationBench-AA | 0.6657372141364344 | fraction | 66.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.automationBenchPartialScore` |
| GPT-6.1 Sol (xhigh) | AA-Omniscience v1.1 | 42.36666666666667 | AA Omniscience Index | 71.18 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.omniscience` |
| GPT-6.1 Sol (xhigh) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.lcr` |
| GPT-6.1 Sol (xhigh) | HLE-Diamond | 0.558 | fraction | 55.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.hleDiamond` |
| GPT-6.1 Sol (xhigh) | Terminal-Bench-Science 0.1 | 0.504761904761905 | fraction | 50.48 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.terminalBenchScience` |
| GPT-6.1 Sol (xhigh) | CritPt v2 (hard subset) | 0.68 | fraction | 68.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.critptAgenticHard` |
| GPT-6 Astra (xhigh) | FrontierCode 2.0 | 0.414029545454545 | fraction | 41.40 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.frontierCode20` |
| GPT-6 Astra (xhigh) | Terminal-Bench 4.0 (AA run) | 59.5959595959596 | percent | 59.60 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.terminalBench40` |
| GPT-6 Astra (xhigh) | Bug Hunt Bench | 43.0 | bugs fixed of 105 | 40.95 | GPT-6 Astra (xhigh effort) | `data/bug_hunt.json` `models[modelId=gpt-6-astra-xhigh].fixedOf105` |
| GPT-6 Astra (xhigh) | GDPval-AA v2.1 | 1569.36 | Elo | 53.47 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.gdpval` |
| GPT-6 Astra (xhigh) | AutomationBench-AA | 0.6717778020215392 | fraction | 67.18 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.automationBenchPartialScore` |
| GPT-6 Astra (xhigh) | AA-Omniscience v1.1 | 43.666666666666664 | AA Omniscience Index | 71.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.omniscience` |
| GPT-6 Astra (xhigh) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.lcr` |
| GPT-6 Astra (xhigh) | HLE-Diamond | 0.615 | fraction | 61.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.hleDiamond` |
| GPT-6 Astra (xhigh) | Terminal-Bench-Science 0.1 | 0.547619047619048 | fraction | 54.76 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.terminalBenchScience` |
| GPT-6 Astra (xhigh) | CritPt v2 (hard subset) | 0.705 | fraction | 70.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-xhigh].model.critptAgenticHard` |
| Claude Haiku 5.5 (low) | FrontierCode 2.0 | 0.0803666666666667 | fraction | 8.04 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.frontierCode20` |
| Claude Haiku 5.5 (low) | Terminal-Bench 4.0 (AA run) | 12.6262626262626 | percent | 12.63 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.terminalBench40` |
| Claude Haiku 5.5 (low) | Bug Hunt Bench | 11.0 | bugs fixed of 105 | 10.48 | Haiku 5.5 (low effort) | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-low].fixedOf105` |
| Claude Haiku 5.5 (low) | GDPval-AA v2.1 | 1130.36 | Elo | 31.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.gdpval` |
| Claude Haiku 5.5 (low) | AutomationBench-AA | 0.22910812181110643 | fraction | 22.91 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (low) | AA-Omniscience v1.1 | 2.1666666666666665 | AA Omniscience Index | 51.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.omniscience` |
| Claude Haiku 5.5 (low) | AA-LCR v1.1 | 0.72 | fraction | 72.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.lcr` |
| Claude Haiku 5.5 (low) | HLE-Diamond | 0.141 | fraction | 14.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.hleDiamond` |
| Claude Haiku 5.5 (low) | Terminal-Bench-Science 0.1 | 0.019047619047619 | fraction | 1.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.terminalBenchScience` |
| Claude Haiku 5.5 (low) | CritPt v2 (hard subset) | 0.215 | fraction | 21.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.critptAgenticHard` |
| GPT-6.1 Terra (low) | FrontierCode 2.0 | 0.244852272727273 | fraction | 24.49 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.frontierCode20` |
| GPT-6.1 Terra (low) | Terminal-Bench 4.0 (AA run) | 15.151515151515198 | percent | 15.15 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.terminalBench40` |
| GPT-6.1 Terra (low) | Bug Hunt Bench | 6 | bugs fixed of 105 | 5.71 | GPT-6.1 Terra (low effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-terra-low].fixedOf105` |
| GPT-6.1 Terra (low) | GDPval-AA v2.1 | 1203.75 | Elo | 35.19 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.gdpval` |
| GPT-6.1 Terra (low) | AutomationBench-AA | 0.5624828754079192 | fraction | 56.25 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.automationBenchPartialScore` |
| GPT-6.1 Terra (low) | AA-Omniscience v1.1 | 22.933333333333334 | AA Omniscience Index | 61.47 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.omniscience` |
| GPT-6.1 Terra (low) | AA-LCR v1.1 | 0.81 | fraction | 81.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.lcr` |
| GPT-6.1 Terra (low) | HLE-Diamond | 0.249 | fraction | 24.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.hleDiamond` |
| GPT-6.1 Terra (low) | Terminal-Bench-Science 0.1 | 0.0761904761904762 | fraction | 7.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.terminalBenchScience` |
| GPT-6.1 Terra (low) | CritPt v2 (hard subset) | 0.485 | fraction | 48.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-terra-low].model.critptAgenticHard` |
| GPT-6 Luna (low) | FrontierCode 2.0 | 0.0219545454545455 | fraction | 2.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.frontierCode20` |
| GPT-6 Luna (low) | Terminal-Bench 4.0 (AA run) | 0.0 | percent | 0.00 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.terminalBench40` |
| GPT-6 Luna (low) | Bug Hunt Bench | 4.0 | bugs fixed of 105 | 3.81 | GPT-6 Luna (low effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-low].fixedOf105` |
| GPT-6 Luna (low) | GDPval-AA v2.1 | 1040.48 | Elo | 27.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-low].model.gdpval` |
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
| MiMo-V2.6-Flash | Bug Hunt Bench | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 1 candidates (0 registered, 1 rejected) | Owner decision O135 (2026-10-30): AA plots MiMo-V2.6-Flash without an effort; Xiaomi's API documents a single thinking mode (thinking.type enabled/disabled, default enabled; on the Responses API every reasoning.effort other than none enables the same, undifferentiated reasoning), so the configuration is thinking enabled, the default (mimo-flash-effort.md). Bug Hunt ran the provider default through OpenRouter without asserting a reasoning state ('effort is `default` ... for this model the dial is untested rather than known-inert', run notes). Whether this route's default equals Xiaomi's documented default (thinking enabled) is not shown by the board: owner to confirm before it counts as exact. |
| Gemini 4 Carbon | Bug Hunt Bench | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No Bug Hunt row for this model at any effort. |
| GPT-6 Luna (low) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not low; not transferred. |
| GPT-6 Luna (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not medium; not transferred. |
| Claude Haiku 5.5 (low) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.444), not low; not transferred. |
| GPT-6 Luna (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not high; not transferred. |
| Claude Haiku 5.5 (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.444), not medium; not transferred. |
| MiMo-V2.6-Flash | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 1 candidates (0 registered, 1 rejected) | Owner decision O135 (2026-10-30): AA plots MiMo-V2.6-Flash without an effort; Xiaomi's API documents a single thinking mode (thinking.type enabled/disabled, default enabled; on the Responses API every reasoning.effort other than none enables the same, undifferentiated reasoning), so the configuration is thinking enabled, the default (mimo-flash-effort.md). Vals records reasoning, reasoning_effort and compute_effort as null and its model page (read 2026-10-30) states no reasoning setting; Xiaomi's API has thinking on by default, so a run that set nothing ran thinking enabled only if Vals did not disable it: owner to confirm (as 2026-10-25: plausible). |
| GPT-6.1 Terra (low) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (83.997), not low; not transferred. |
| Claude Haiku 5.5 (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.444), not high; not transferred. |
| GPT-6.1 Terra (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (83.997), not medium; not transferred. |
| GPT-6.1 Terra (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (83.997), not high; not transferred. |
| GPT-6.1 Sol (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (88.931), not medium; not transferred. |
| GPT-6.1 Sol (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (88.931), not high; not transferred. |
| GPT-6.1 Sol (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (88.931), not xhigh; not transferred. |
| GPT-6 Astra (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (89.594), not high; not transferred. |
| GPT-6 Astra (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (89.594), not xhigh; not transferred. |
| Claude Opus 5.5 (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.294), not xhigh; not transferred. |
| GPT-6 Luna (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not xhigh; not transferred. |
| GPT-6.1 Sol (low) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (88.931), not low; not transferred. |
| GPT-6.1 Terra (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (83.997), not xhigh; not transferred. |
| Claude Opus 5.5 (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.294), not high; not transferred. |
| GPT-6 Luna (low) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not low; not transferred. |
| GPT-6 Luna (medium) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not medium; not transferred. |
| Claude Haiku 5.5 (low) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.36), not low; not transferred. |
| GPT-6 Luna (high) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not high; not transferred. |
| Claude Haiku 5.5 (medium) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.36), not medium; not transferred. |
| MiMo-V2.6-Flash | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 1 candidates (0 registered, 1 rejected) | Owner decision O135 (2026-10-30): AA plots MiMo-V2.6-Flash without an effort; Xiaomi's API documents a single thinking mode (thinking.type enabled/disabled, default enabled; on the Responses API every reasoning.effort other than none enables the same, undifferentiated reasoning), so the configuration is thinking enabled, the default (mimo-flash-effort.md). Vals records reasoning, reasoning_effort and compute_effort as null and its model page (read 2026-10-30) states no reasoning setting; Xiaomi's API has thinking on by default, so a run that set nothing ran thinking enabled only if Vals did not disable it: owner to confirm (as 2026-10-25: plausible). |
| GPT-6.1 Terra (low) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| Claude Haiku 5.5 (high) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.36), not high; not transferred. |
| GPT-6.1 Terra (medium) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| GPT-6.1 Terra (high) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| GPT-6.1 Sol (medium) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not medium; not transferred. |
| GPT-6.1 Sol (high) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not high; not transferred. |
| GPT-6.1 Sol (xhigh) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not xhigh; not transferred. |
| GPT-6 Astra (high) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (80.579), not high; not transferred. |
| GPT-6 Astra (xhigh) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (80.579), not xhigh; not transferred. |
| Claude Opus 5.5 (xhigh) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.012), not xhigh; not transferred. |
| Gemini 4 Carbon | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No google/gemini-4-carbon row on this board. |
| GPT-6 Luna (xhigh) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not xhigh; not transferred. |
| GPT-6.1 Sol (low) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not low; not transferred. |
| GPT-6.1 Terra (xhigh) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| GPT-6.1 Terra (max) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No openai/gpt-6.1-terra row on this board. |
| Claude Opus 5.5 (high) | Code Migration v1.1 (Vals) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.012), not high; not transferred. |
| GPT-6 Luna (low) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 64.59); not transferred. |
| GPT-6 Luna (medium) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 64.59); not transferred. |
| Claude Haiku 5.5 (low) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-haiku-5.5 at max only (Overall 69.85); not transferred. |
| GPT-6 Luna (high) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 64.59); not transferred. |
| Claude Haiku 5.5 (medium) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-haiku-5.5 at max only (Overall 69.85); not transferred. |
| MiMo-V2.6-Flash | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No mimo-v2.6-flash row in release 20261025 (nor in the site's model metadata). |
| GPT-6.1 Terra (low) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 77.79); not transferred. |
| Claude Haiku 5.5 (high) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-haiku-5.5 at max only (Overall 69.85); not transferred. |
| GPT-6.1 Terra (medium) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 77.79); not transferred. |
| GPT-6.1 Terra (high) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 77.79); not transferred. |
| GPT-6.1 Sol (medium) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 84.07); not transferred. |
| GPT-6.1 Sol (high) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 84.07); not transferred. |
| GPT-6.1 Sol (xhigh) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 84.07); not transferred. |
| GPT-6 Astra (high) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-astra at max only (Overall 85.64); not transferred. |
| GPT-6 Astra (xhigh) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-astra at max only (Overall 85.64); not transferred. |
| Claude Opus 5.5 (xhigh) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-opus-5.5 at max only (Overall 85.14); not transferred. |
| Gemini 4 Carbon | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No gemini-4-carbon row in release 20261025 (nor in the site's model metadata). |
| GPT-6 Luna (xhigh) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6-luna at max only (Overall 64.59); not transferred. |
| GPT-6.1 Sol (low) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-sol at max only (Overall 84.07); not transferred. |
| GPT-6.1 Terra (xhigh) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-6.1-terra at max only (Overall 77.79); not transferred. |
| Claude Opus 5.5 (high) | LiveBench 2.0 Overall | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has claude-opus-5.5 at max only (Overall 85.14); not transferred. |
| GPT-6 Luna (low) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6-Luna (Max) [Codex CLI, 2026-10-01] = 59.07; GPT-6-Luna (Xhigh) [Codex CLI, 2026-10-01] = 56.4; GPT-6-Luna (High) [Codex CLI, 2026-10-01] = 53.04; GPT-6-Luna (Medium) [Codex CLI, 2026-09-30] = 43.74. |
| Claude Haiku 5.5 (low) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Haiku 5.5 (High) [Claude Code, 2026-10-08] = 58.63; Haiku 5.5 (Medium) [Claude Code, 2026-10-08] = 58.2. |
| GPT-6.1 Terra (low) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.1-Terra (Max) [Codex CLI, 2026-10-27] = 60.41; GPT-6.1-Terra (Xhigh) [Codex CLI, 2026-10-27] = 57.09; GPT-6.1-Terra (High) [Codex CLI, 2026-10-26] = 54.82; GPT-6.1-Terra (Medium) [Codex CLI, 2026-10-26] = 54.61. |
| GPT-6.1 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.1-Sol (High) [Codex CLI, 2026-10-19] = 66; GPT-6.1-Sol (Medium) [Codex CLI, 2026-10-19] = 65.05; GPT-6.1-Sol (Low) [Codex CLI, 2026-10-19] = 61.45. |
| GPT-6.1 Sol (max) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6.1-Sol (High) [Codex CLI, 2026-10-19] = 66; GPT-6.1-Sol (Medium) [Codex CLI, 2026-10-19] = 65.05; GPT-6.1-Sol (Low) [Codex CLI, 2026-10-19] = 61.45. |
| GPT-6 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6-Astra (High) [Codex CLI, 2026-10-01] = 66.35; GPT-6-Astra (Medium) [Codex CLI, 2026-09-30] = 66.03. |
| Claude Opus 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Opus 5.5 (High) [Claude Code, 2026-10-20] = 67.26; Opus 5.5 (Medium) [Claude Code, 2026-10-19] = 65.28; Opus 5.5 (Low) [Claude Code, 2026-10-19] = 60.5. |
| Gemini 4 Carbon | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | No AI Coding Daily row for this model at any effort. |
| GPT-6 Astra (max) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: GPT-6-Astra (High) [Codex CLI, 2026-10-01] = 66.35; GPT-6-Astra (Medium) [Codex CLI, 2026-09-30] = 66.03. |
| Claude Sonnet 5.5 | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Sonnet 5.5 (High) [Claude Code, 2026-09-30] = 64.31; Sonnet 5.5 (Medium) [Claude Code, 2026-09-29] = 60.54. |
| Claude Opus 5.5 (max) | AI Coding Daily (excl. bug finding) | 2026-10-30 | not found | 1 | 2026-10-30: 7 queries, 0 candidates (0 registered, 0 rejected) | Non-matching rows at other efforts: Opus 5.5 (High) [Claude Code, 2026-10-20] = 67.26; Opus 5.5 (Medium) [Claude Code, 2026-10-19] = 65.28; Opus 5.5 (Low) [Claude Code, 2026-10-19] = 60.5. |

## Basket cost components

| Configuration | Component | Cost (USD) | Completeness | Tasks | USD per task | Source |
|---|---|---:|---|---:|---:|---|
| Claude Opus 5.5 (max) | AA-Briefcase | $1,915.18 | unresolved | 91 | $21.0460 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | GDP.pdf | $155.23 | unresolved | 100 | $1.5523 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | AutomationBench-AA | $938.69 | unresolved | 657 | $1.4288 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $865.21 | unresolved | 66 | $13.1093 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | FrontierCode 2.0 | $1,776.08 | unresolved | 132 | $13.4552 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Terminal-Bench-Science | $1,397.97 | unresolved | 70 | $19.9710 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Coding Agent Index | $3,312.59 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| Claude Opus 5.5 (max) | ITBench-AA | $146.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| Claude Sonnet 5.5 (max) | AA-Briefcase | $1,863.13 | confirmed-complete | 91 | $20.4739 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | GDP.pdf | $79.43 | confirmed-complete | 100 | $0.7943 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | $678.32 | confirmed-complete | 657 | $1.0324 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $834.67 | confirmed-complete | 66 | $12.6464 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | FrontierCode 2.0 | $1,525.59 | confirmed-complete | 132 | $11.5575 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Terminal-Bench-Science | $1,663.25 | confirmed-complete | 70 | $23.7607 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Coding Agent Index | $3,857.44 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| GPT-6.1 Sol (max) | AA-Briefcase | $210.45 | confirmed-complete | 91 | $2.3126 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | GDP.pdf | $41.99 | confirmed-complete | 100 | $0.4199 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | AutomationBench-AA | $195.01 | confirmed-complete | 657 | $0.2968 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Terminal-Bench 4.0 (AA Index run) | $120.30 | confirmed-complete | 66 | $1.8228 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | FrontierCode 2.0 | $149.21 | confirmed-complete | 132 | $1.1304 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Terminal-Bench-Science | $233.73 | confirmed-complete | 70 | $3.3389 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Coding Agent Index | $436.35 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| GPT-6 Astra (max) | AA-Briefcase | $864.69 | confirmed-complete | 91 | $9.5021 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | GDP.pdf | $207.58 | confirmed-complete | 100 | $2.0758 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | AutomationBench-AA | $1,048.30 | confirmed-complete | 657 | $1.5956 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Terminal-Bench 4.0 (AA Index run) | $560.88 | confirmed-complete | 66 | $8.4981 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | FrontierCode 2.0 | $863.12 | confirmed-complete | 132 | $6.5388 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Terminal-Bench-Science | $1,223.34 | confirmed-complete | 70 | $17.4762 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Coding Agent Index | $2,040.49 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| GPT-6 Astra (max) | ITBench-AA | $133.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| GPT-6 Luna (max) | AA-Briefcase | $15.47 | confirmed-complete | 91 | $0.1700 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | GDP.pdf | $2.85 | confirmed-complete | 100 | $0.0285 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | AutomationBench-AA | $23.91 | confirmed-complete | 657 | $0.0364 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Terminal-Bench 4.0 (AA Index run) | $15.59 | confirmed-complete | 66 | $0.2362 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | FrontierCode 2.0 | $23.22 | confirmed-complete | 132 | $0.1759 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Terminal-Bench-Science | $31.79 | confirmed-complete | 70 | $0.4541 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Coding Agent Index | $46.16 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |

### AA Index total reconciliation

The seven Index components plus AA's residual reproduce AA's published Intelligence Index total cost.

| Configuration | Index SDLC components | Residual | Reconstructed total | Published total | Reconciled |
|---|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | — | $1,863.54 | $8,911.91 | $8,909.67 | no |
| Claude Sonnet 5.5 (max) | — | $1,336.25 | $7,980.63 | $7,980.63 | yes |
| GPT-6.1 Sol (max) | — | $173.29 | $1,123.97 | $1,123.97 | yes |
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

## Terminal-Bench 4.0 official rows

23 official rows (5 of 27 cohort matches), observed 2026-10-31T04:10:00Z. The published ± is the source's 95% confidence interval (used by stream S1M). Since O37 the Terminal-Bench leaf is AA's own run; these rows cross-check it and fill a gap. Matched agents for cohort rows, in the registered preference order (E225): Claude Code 2, Codex 3.

| Rank | Base model | Agent | Resolution rate | Tokens | Cost |
|---|---|---|---:|---|---:|
| 1 | Opus 5.5 | Claude Code | 64.8% ± 3.1% | 8.0B | $4,700 |
| 2 | Sonnet 5.5 | Claude Code | 61.8% ± 2.9% | 19.4B | $7,300 |
| 3 | GPT-6 Astra | Codex | 58.2% ± 2.8% | 1.5B | $3,300 |
| 3 | GPT-6.1 Sol | Codex | 58.2% ± 3.1% | 1.5B | $600 |
| 5 | Fable 5.1 | Claude Code | 57.9% ± 3.8% | 2.7B | $6,200 |
| 6 | Opus 5 | Claude Code | 53.9% ± 3.2% | 6.9B | $6,100 |
| 7 | GPT-6 Sol | Codex | 49.4% ± 3.2% | 5.0B | $1,500 |
| 8 | Fable 5 | Claude Code | 44.5% ± 3.8% | 3.8B | $7,300 |
| 9 | GLM-5.3 | Claude Code | 41.8% ± 3.2% | 8.7B | $2,700 |
| 10 | Grok 4.7 | Grok Build | 37.6% ± 3.5% | 5.5B | $3,700 |
| 11 | GPT-5.6 Sol | Codex | 37.3% ± 3.8% | 4.4B | $2,500 |
| 12 | GLM-5.3-Flash | Claude Code | 35.8% ± 3.5% | 2.9B | $100 |
| 13 | Qwen3.8-Max-0902 | Claude Code | 27.0% ± 3.8% | 3.0B | $4,600 |
| 14 | Opus 4.8 | Claude Code | 23.6% ± 3.6% | 6.4B | $6,500 |
| 15 | GPT-5.6 Terra | Codex | 21.5% ± 3.3% | 5.7B | $1,700 |
| 16 | Grok 4.6 | Grok Build | 20.3% ± 3.1% | 4.0B | $3,600 |
| 17 | Gemini 3.8 Flash | mini-SWE-agent | 19.1% ± 3.4% | 17.2B | $1,800 |
| 18 | GPT-5.6 Luna | Codex | 17.3% ± 2.8% | 11.6B | $300 |
| 19 | GPT-6 Luna | Codex | 16.4% ± 2.7% | 3.9B | $100 |
| 20 | Muse Spark 1.3 | Muse Code | 14.5% ± 2.9% | 9.0B | — |
| 21 | Grok 4.5 | Grok Build | 12.4% ± 2.6% | 3.4B | $2,100 |
| 21 | Sonnet 5 | Claude Code | 12.4% ± 3.1% | 21.6B | $9,600 |
| 23 | Gemini 3.7 Flash | mini-SWE-agent | 11.2% ± 2.4% | 11.1B | $1,300 |

## Bug Hunt Bench matched runs

Owner-published runs at commit `12497971d928cc5ad97a184755734720388bc07f`; the score is the owner's largest-sample mean of bugs fixed of 105 for the exact model and effort, with the harness that result was run on (E206). No ranked configuration has Bug Hunt results on two harnesses at the same effort (E224).

| Model | Evaluated model | Bugs fixed of 105 | Runs | Effort | Harness |
|---|---|---:|---:|---|---|
| GPT-6 Luna (low) | GPT-6 Luna (low effort) | 4.0 | 1 | low | Codex CLI |
| GPT-6 Luna (medium) | GPT-6 Luna (medium effort) | 4.0 | 1 | medium | Codex CLI |
| Claude Haiku 5.5 (low) | Haiku 5.5 (low effort) | 11.0 | 1 | low | Claude Code |
| GPT-6 Luna (high) | GPT-6 Luna (high effort) | 9.0 | 1 | high | Codex CLI |
| Claude Haiku 5.5 (medium) | Haiku 5.5 (medium effort) | 12.0 | 1 | medium | Claude Code |
| GPT-6.1 Terra (low) | GPT-6.1 Terra (low effort) - mean of 3 | 6.0 | 3 | low | Codex CLI |
| Claude Haiku 5.5 (high) | Haiku 5.5 (high effort) - mean of 2 | 16.0 | 2 | high | Claude Code |
| GPT-6.1 Terra (medium) | GPT-6.1 Terra (medium effort) - mean of 3 | 7.3 | 3 | medium | Codex CLI |
| GPT-6.1 Terra (high) | GPT-6.1 Terra (high effort) - mean of 3 | 9.7 | 3 | high | Codex CLI |
| GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium effort) - mean of 2 | 29.0 | 2 | medium | Codex CLI |
| GPT-6.1 Sol (high) | GPT-6.1 Sol (high effort) - mean of 2 | 36.5 | 2 | high | Codex CLI |
| GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh effort) - mean of 3 | 42.7 | 3 | xhigh | Codex CLI |
| GPT-6.1 Sol (max) | GPT-6.1 Sol (max effort) - mean of 3 | 44.3 | 3 | max | Codex CLI |
| GPT-6 Astra (high) | GPT-6 Astra (high effort) | 35.0 | 1 | high | Codex CLI |
| GPT-6 Astra (xhigh) | GPT-6 Astra (xhigh effort) | 43.0 | 1 | xhigh | Codex CLI |
| Claude Opus 5.5 (xhigh) | Opus 5.5 (xhigh effort) - mean of 3 | 36.0 | 3 | xhigh | Claude Code |
| GPT-6 Luna (xhigh) | GPT-6 Luna (xhigh effort) | 14.0 | 1 | xhigh | Codex CLI |
| GPT-6 Luna (max) | GPT-6 Luna (max effort) - mean of 3 | 18.3 | 3 | max | Codex CLI |
| GPT-6.1 Sol (low) | GPT-6.1 Sol (low effort) - mean of 2 | 22.5 | 2 | low | Codex CLI |
| GPT-6.1 Terra (xhigh) | GPT-6.1 Terra (xhigh effort) - mean of 3 | 11.3 | 3 | xhigh | Codex CLI |
| GPT-6.1 Terra (max) | GPT-6.1 Terra (max effort) - mean of 3 | 40.7 | 3 | max | Codex CLI |
| Claude Opus 5.5 (high) | Opus 5.5 (high effort) - mean of 3 | 31.7 | 3 | high | Claude Code |
| GPT-6 Astra (max) | GPT-6 Astra (max effort) - mean of 3 | 45.0 | 3 | max | Codex CLI |
| Claude Sonnet 5.5 | Sonnet 5.5 (max effort) - mean of 3 | 51.3 | 3 | max | Claude Code |
| Claude Opus 5.5 (max) | Opus 5.5 (max effort) - mean of 3 | 41.7 | 3 | max | Claude Code |

## Plan routes

Route evidence as of 2026-10-25. Full allocation regimes, workloads and notes are in [data/plan_cost_routes.json](data/plan_cost_routes.json).

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
| Claude Pro $20 · common Claude assumption | claude-haiku-5-5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
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
| Claude Max 5x $100 · common Claude assumption | claude-haiku-5-5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
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
| Claude Max 20x $200 · common Claude assumption | claude-haiku-5-5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
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

### Plan amounts and their lineage

Each routed row's amount with what it measures, how it was derived and which objects it comes from (E166, E168); API-fallback rows have none.

| Configuration | Amount (USD per fee period) | Measures | Derivation | Workload | Cash object | Measurement object |
|---|---:|---|---|---|---|---|
| GPT-6.1 Sol (max) | $5,386 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | chatgpt-pro500-gpt61sol-semianalysis:month cash | chatgpt-pro500-gpt61sol-semianalysis |
| Claude Opus 5.5 (max) | $1,178 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | claude-pro-opus55-semianalysis:month cash | claude-pro-opus55-semianalysis |
| Claude Sonnet 5.5 (max) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-claude-sonnet-5-5-common-opus55-assumption:month cash | claude-pro-claude-sonnet-5-5-common-opus55-assumption |
| GPT-6 Astra (max) | $2,897 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | chatgpt-pro200-gpt6astra-semianalysis:month cash | chatgpt-pro200-gpt6astra-semianalysis |
| GPT-6 Luna (max) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-gpt-6-luna-common-gpt-assumption:month cash | chatgpt-pro500-gpt-6-luna-common-gpt-assumption |

## Evidence bundle

Bundle hash `3a7a9b882f374aee3fbcd937b07419dc1124361405051918745c9075e24ac99f`: every published output is rebuilt from these artifacts at the pinned publication clock (npm run verify:docs), never from live pages.

| Key | Artifact | SHA-256 | Captured | Extractor |
|---|---|---|---|---|
| snapshot | `data/aa/aa_v432_snapshot.json` | `73c1309dbe2d353070b52881b0aaca3ca1a1442547312a49fa093ddcfe066291` | 2026-10-31T04:07:04Z | valuerank.capture_aa |
| bugHunt | `data/bug_hunt.json` | `73077b1931d163b8a3fcf859f9a363ecad936b056ba0412bb56fa0b7f4348c00` | 2026-10-30 | editorial capture of the owner's published results (source commit recorded) |
| tb4 | `data/tb4.json` | `3ab0a227c23c09f86f9c006432bdc62ba7d4737476c0c53d20a8dfdc36a27219` | 2026-10-30T22:22:49.248Z | scripts/scrape-tb4.js, then valuerank.build_tb4 |
| codingAgents | `data/aa/coding_agents_capture.json` | `7786431da787e38ce3998df018ccce7328cc0f788119ae346456eb69f4fd93a5` | 2026-10-31T04:07:05Z | valuerank.capture_coding_agents |
| costCharts | `data/aa/cost_charts_capture.json` | `bc388a1fd7a8b6bcb511df340377fa956142e632dfd4638b6fc8c548556458ec` | 2026-10-31T04:07:51.285Z | scripts/capture-aa-cost-charts.js |
| configurationMap | `data/v3_configuration_map.json` | `95479db087ce6b5763e747379d1955740176758a46161e052073dc28c7ba1cc6` | 2026-10-25 | editorial pinning from the research capture |
| codingAgentsManifest | `data/aa/coding_agents_manifest.json` | `08ca9d896577ca79e038817204322aeb55d7b5a2d2978b8fc6dc381da356fe95` | 2026-10-30 | editorial manifest of every AA Coding Agent Index row, reviewed at each capture (O64) |
| frontierCapture | `data/aa_frontier_capture.json` | `a71eec4d45a450704511cea0b240cc7bae7609b29107276fb770c590707e405f` | 2026-10-30T22:15:18Z | browser capture of AA's Intelligence Index vs cost chart from public tooltips (frontier membership, E195; unevaluated cheaper siblings, E201) |
| roster | `data/aa_mapping.json` | `0cbc840a7a37fc12596b3189b3ecc0b1abff86eb4996ac25c61174b0a4a7641a` | 2026-10-30T22:15:18Z | editorial roster: every configuration AA plots on its rendered frontier or within 3 Index points of it (O51) |
| bugHuntScoreboard | `data/bug_hunt_scoreboard.json` | `2e0f1eab15f219ba491af8c4ca694197c9bed96546b4157c06ca1414f9d6e8dc` | 2026-10-30T22:19:18Z | the owner's combined scoreboard at the pinned commit (O31 roster check) |
| planRoutes | `data/plan_cost_routes.json` | `119d48ccc597cf4d2724a323380aac8c3584ba069f506431635477be47b74859` | 2026-10-25 | editorial Plan evidence registry |
| priceRecords | `data/price_records.json` | `fe550f7770759a6219e671838f28b42d3b7d7db0fa5f7ab489e08a75605421f8` | 2026-10-31T04:10:00Z | editorial E141 price-record registry (superseded and promotional tariffs) |
| leafEvidence | `data/leaf_evidence.json` | `b1cd6ea2e7d8d7c4f631a3f3bc384482f87cf76dc78d4ad723c5c12ffd052668` | 2026-10-30 | editorial supplementary leaf evidence and the exhaustive-search log (O36) |
| cognitionFrontierCode | `data/cognition_frontiercode.json` | `ff0040778b7bdf69c705ad7474f771fb5e53cfaf5cf8573b3a4614153543d75f` | 2026-10-23 | Cognition's FrontierCode leaderboard data (https://cognition.com/data/frontiercode-leaderboard/data.json), captured unchanged (O37) |
| sweTracks | `data/swe_tracks.json` | `8b65fb2afbceb90e42de2c90df921294dc234f5d8db7d52a2e7d2ecc879bfde5` | 2026-10-30T22:22:49.248Z | research/2026-10-23-swe-benchmarks/build_swe_tracks.py from the verified coverage captures (O53-O55) |
| planReports | `data/plan_reports.json` | `c017edb8177d638c98e5e3d55b7e94b2d14335f19283b6d90c331ee54550cfc6` | 2026-10-25 | editorial table of every O71 user report with the facts E270 needs; the build derives admission from it (O81) |
| aaPreviousCapture | `data/aa/aa_previous_capture.json` | `d72ee6a35b4016d0f309fcf0f1df231d5ec5afa955a31935b7fafc86a1355d85` | 2026-10-30T22:23:33Z | valuerank.capture_aa: digest of the model-page capture this one replaced (I60) |
| sourceRereads | `data/source_rereads.json` | `5d806f7ac471a2c09eb1a189a3d3d7c36b7e9d2c050bcc1835c6156405cb133a` | 2026-10-25T11:33:58Z | editorial record of the O68 re-reads, each 'unchanged' result verified against the re-read file |
| aaFootnotes | `data/aa/aa_footnote_register.json` | `ccc742e1cca305fa88b80b48d7f46e89392cee8225353f8daa88ec5e174d59a4` | 2026-10-30T22:15:18Z | editorial register of every AA note the captures record (the chart's footnotes, and from O103 the model pages, Coding Agent Index and cost charts), by exact text, each classified once (O100, O103) |
| anchors | `data/v3_frozen.json` | `4459e7b70bede36e514761caf692baec1fe61b0249277345326bf1a9882f02de` | 2026-10-31 | valuerank.value_v3 freeze |
| anchors:aicd | `data/v3_frozen_aicd.json` | `2fe1747756d87a620c959eeb5173430097d69c00b0cf5715b54b404161336c1a` | 2026-10-31 | valuerank.value_v3 freeze |
| anchors:common | `data/v3_frozen_common.json` | `64388fb5f64c04e4188a54a4c3a022726a3758e6b722235c75738a4cf73fbc01` | 2026-10-31 | valuerank.value_v3 freeze |


## AA intelligence and total-cost comparison

Observed 2026-10-30T22:15:18Z; Artificial Analysis Intelligence Index v5.0. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 89 catalog models selected; 82 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 89 models, plotted 82 eligible points, and displayed 18 frontier points. Public metric/export gaps are shown explicitly. All 8 distinct frontier model families are required in the main ranking using exact selected configurations; 4 are included. Other effort configurations remain separate comparison entries. 9 plotted configurations from 6 families lie within 3 Index points of the rendered frontier; 4 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 10 (rounded) | $9.09 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 18 (rounded) | $39.55 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 19 (rounded) | $39.60 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 21 (rounded) | $62.58 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 25 (rounded) | $72.70 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 27 (rounded) | $106.14 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench |
| [GPT-6.1 Terra (low)](https://artificialanalysis.ai/models/gpt-6-1-terra-low) | gpt-6-1-terra-low | 29 (rounded) | $111.16 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 30 (rounded) | $121.41 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Terra (medium)](https://artificialanalysis.ai/models/gpt-6-1-terra-medium) | gpt-6-1-terra-medium | 38 (rounded) | $190.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Terra (high)](https://artificialanalysis.ai/models/gpt-6-1-terra-high) | gpt-6-1-terra-high | 42 (rounded) | $266.79 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 46 (rounded) | $388.57 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $573.17 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 52 (rounded) | $717.71 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 55 (rounded) | $1,123.97 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 55 (rounded) | $3,204.00 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 55 (rounded) | $3,746.22 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 57 (rounded) | $4,765.91 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Gemini 4 Carbon (high)](https://artificialanalysis.ai/models/gemini-4-carbon) | gemini-4-carbon | 59 (rounded) | $8,239.69 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 23 (rounded) | $85.74 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 28 (rounded) | $136.06 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6.1 Sol (low)](https://artificialanalysis.ai/models/gpt-6-1-sol-low) | gpt-6-1-sol-low | 35 (rounded) | $237.91 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6.1 Terra (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-terra-xhigh) | gpt-6-1-terra-xhigh | 45 (rounded) | $400.18 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6.1 Terra (max)](https://artificialanalysis.ai/models/gpt-6-1-terra) | gpt-6-1-terra | 51 (rounded) | $972.34 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 52 (rounded) | $2,715.98 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 57 (rounded) | $5,661.18 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 54 (rounded) | $7,980.63 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,909.67 | Near AA frontier (within 3 Index points) | Primary ranked | None |
