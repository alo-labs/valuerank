# Implementation handoff

## Delivered

- `.refresh/v1.4/` contains the DeepSWE extraction, AA first-party payload extraction, coverage matrix, score matrix, ranking summary, and reproducible build scripts.
- Root publication artifacts (`README.md`, `methodology.md`, `raw-data.md`, `scores.md`, and `site/index.html`) are generated for v1.4.0.
- The dated research ledger contains the source register, evidence spans, report, claims, critique, decisions, and validation outputs.

## Reproduction path

From `/Users/shafqat/valuerank`:

```sh
python3 .refresh/v1.4/build_deepswe_v14.py
python3 .refresh/v1.4/build_aa_metrics.py
python3 .refresh/v1.4/build_scores.py
python3 .refresh/v1.4/emit_v14_docs.py
```

The scripts are deliberately separated by source extraction, normalization/scoring, and publication emission so a future refresh can replace one source without hand-editing the generated site.

## Release gates

1. Run the four Silver deep-research validators and retain their logs under `validation/`.
2. Validate JSON shape, 21-row alignment, 13 retained dimensions, zero-gap coverage, and null Speed handling.
3. Run `git diff --check` and inspect the staged file list for secrets, malware residue, ignored raw HTML, or temporary tool data.
4. Refresh Graphify after the final code changes; graph output remains local/ignored and is not a source artifact.
5. Commit and push only the verified tracked artifacts.

## Future refresh checklist

- Capture the DeepSWE update date and current Best roster.
- Resolve each roster family to one AA page and exact effort variant.
- Decode `currentModel` and record raw page snapshots outside Git when they are transient.
- Recompute coverage before scoring; preserve nulls and drop incomplete dimensions.
- Re-run report claim support and citation validation.
- Compare the new ranking with the prior published version and document changes.
