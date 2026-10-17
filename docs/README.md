# ValueRank documentation

Start with the published ranking in the repository root (`README.md`, `methodology.md`, `scores.md`, `raw-data.md`) and the site at https://valuerank.alolabs.dev. The guides below are for people who change the pipeline or the site, run a refresh or review the evidence.

| Guide | Read it when you want to |
|---|---|
| [Repository layout](repository-layout.md) | Find where code, data, output, tests and research live, including the generated site layout and the map from the pre-2026-10-17 layout |
| [Architecture](architecture.md) | Understand the stages, what each reads and writes, the site generator, and why outputs are reproducible |
| [Development guide](development.md) | Set up a machine, run the checks, build and preview the site, fix common errors |
| [Testing](testing.md) | Learn what the suites cover, how coverage is measured and what cannot be tested automatically |
| [Refresh and release](refresh-and-release.md) | Capture new sources, bump the version, verify and publish |
| [Site experience plan](site-experience-plan.md) | Read the site audit, the target information architecture, the decisions taken on 2026-10-18 and the phase plan |
| [Site data contract](site-data-contract.md) | Change a public JSON file under `site/data/`, a page view model, a template or a URL parameter |
| [OCG versus Composer 2.5 methodology](ocg-c25-comparison-methodology.md) | Follow the separate subscription value comparison study |

Policy that binds every refresh (model inclusion, exact-variant evidence, subscription-allowance evidence) lives in `AGENTS.md` at the repository root. Dated research ledgers under `research/` are immutable records; they are not maintained as current documentation.
