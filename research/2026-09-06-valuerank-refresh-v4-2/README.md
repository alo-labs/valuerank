# ValueRank AA v4.2 refresh

Capture date: 2026-09-06

This package records the ValueRank refresh prompted by [Artificial Analysis Intelligence Index v4.2](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2) and the [current Intelligence Index methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).

## Source change

Artificial Analysis v4.2 adds AA-Briefcase and GDP.pdf, removes GPQA Diamond from the composite, increases the private held-out share to 40%, and changes several grading/sampling systems. The current methodology lists ten evaluations: AA-Briefcase, GDPval-AA v2, τ³-Banking, Terminal-Bench v2.1, SciCode, AA-LCR v1.1, AA-Omniscience, Humanity's Last Exam, GDP.pdf, and CritPt. AA-Omniscience is represented by accuracy and non-hallucination components in the extracted source record.

## ValueRank decision record

- The existing complete 21-model DeepSWE Best cohort remains the ranked cohort.
- The AA source extraction is refreshed to v4.2 and records the new AA-Briefcase and GDP.pdf fields in the machine-readable source snapshot.
- The existing ValueRank score keeps its explicitly defined independent dimensions. AA-Briefcase is not added as a second agentic dimension because the composite AA Intelligence Index already incorporates it; GDP.pdf is retained as a source field but cannot pass the zero-gap gate for this cohort.
- GPQA Diamond is retained as a separately labelled legacy ValueRank input for continuity and auditability; it is not described as a v4.2 source-index component.
- Missing source values remain null. No model-family, median, neutral, or selective cost substitution is used.
- AA total evaluation cost is unavailable for GPT-5.5, Claude Opus 4.8, and GLM-5.2 in the captured v4.2 pages. The cost dimension therefore uses the same DeepSWE average-cost-per-task normalization for every model; available AA costs remain published raw data.

## Reproduction

The durable source snapshot is `.refresh/v1.4/aa/aa_v42_snapshot.json`. Run `python3 .refresh/v1.4/build_aa_metrics.py`, then `python3 .refresh/v1.4/build_scores.py`, then `python3 .refresh/v1.4/emit_v14_docs.py` to regenerate the machine-readable outputs and Markdown publication. The snapshot was captured from each first-party Artificial Analysis model page's `currentModel` payload; it does not require an Artificial Analysis API key.
