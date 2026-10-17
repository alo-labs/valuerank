# ValueRank documentation

Start with the published ranking in the repository root (`README.md`, `methodology.md`, `scores.md`, `raw-data.md`) and the site at https://alo-labs.github.io/valuerank. The guides below are for people who change the pipeline, run a refresh or review the evidence.

| Guide | Read it when you want to |
|---|---|
| [Repository layout](repository-layout.md) | Find where code, data, output, tests and research live, including the map from the pre-2026-10-17 layout |
| [Architecture](architecture.md) | Understand the stages, what each reads and writes, and why outputs are reproducible |
| [Development guide](development.md) | Set up a machine, run the checks, preview the site, fix common errors |
| [Testing](testing.md) | Learn what the suites cover, how coverage is measured and what cannot be tested automatically |
| [Refresh and release](refresh-and-release.md) | Capture new sources, bump the version, verify and publish |
| [OCG versus Composer 2.5 methodology](ocg-c25-comparison-methodology.md) | Follow the separate subscription value comparison study |

Policy that binds every refresh (model inclusion, exact-variant evidence, subscription-allowance evidence) lives in `AGENTS.md` at the repository root. Dated research ledgers under `research/` are immutable records; they are not maintained as current documentation.
