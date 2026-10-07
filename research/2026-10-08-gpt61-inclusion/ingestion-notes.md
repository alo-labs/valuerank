# GPT-6.1 Sol inclusion: ingestion contract

Date: October 8, 2026. Publication version: v1.9.6.

## Selected identity

ValueRank model ID: `gpt-6.1-sol`. Display name: `GPT-6.1 Sol`.
Artificial Analysis slug: `gpt-6-1-sol`. Evaluated effort: `max`.
Source URL: https://artificialanalysis.ai/models/gpt-6-1-sol.

The existing `gpt-6-sol` row remains a separate generation. The new row does
not inherit its scores, source records, or LiveBench match.

## Required source capture

The retained browser capture in `.refresh/v1.4/aa/aa_v432_snapshot.json`
uses these exact identifiers and metadata structure:

```json
{
  "id": "gpt-6.1-sol",
  "url": "https://artificialanalysis.ai/models/gpt-6-1-sol",
  "model": {
    "slug": "gpt-6-1-sol",
    "effort": { "slug": "max" }
  },
  "capture": {
    "captureMode": "public-rendered",
    "observedAt": "actual capture timestamp",
    "precision": "actual displayed precision",
    "method": "actual public browser capture method"
  }
}
```

This is an identity and metadata contract, not a benchmark payload. Populate
model fields only from the selected profile's observed public values. Retain
missing source values as null; do not copy scores from GPT-6 Sol or GPT-6.1 Sol
at another effort. Per-metric source URLs and precision may be supplied as
`capture.metricSourceUrls` and `capture.metricPrecision`.

`build_aa_metrics.py` now checks the expected slug and effort configured for
this row before ingesting metrics. Extraction metadata retains `captureMode`
from the capture, or from the `aa_extract.json` roster entry. The selected
profile is now retained and ready for the primary agent's regeneration.

## Related benchmark contracts

The primary agent owns the exact max DeepSWE and Bug Hunt records. Their
source records must match the same generation and evaluated effort. The
ingestion worker has not copied or fabricated either benchmark result.

LiveBench's strict cohort dictionary includes `gpt-6.1-sol: None`, preserving
an explicit missing match for the pinned release. A verified exact max match
can replace it when available; another generation or effort cannot supply it.

## Subscription routes

The new model is included in all four existing common GPT assumptions:
ChatGPT Plus 8.1x, Pro 100 10.55x, Pro 200 10.42x, and Pro 500 10.772x.
Each route retains its existing source model, controlled-account workload
projection evidence, allocation regime, and provisional cross-model
assumption labels. This addition creates no new measured allowance claim.

## Reconciliation and execution status

The exact max capture was appended to the source snapshot at
`2026-10-07T16:23:48Z` (October 8 in Sydney), using public observations supplied
by the primary agent and frontier worker. The raw Briefcase Elo is 1564;
GDPval-AA v2.1 Elo is 1575; total AA benchmark cost is USD 1081.55. The profile
cost per task of USD 0.72 is retained in a separate display field. No raw Elo
was inferred from the normalized displays.

The cached-input price of USD 0.10/M is derived from the observed USD 2/M
input price and 95% cache discount. Its formula and source are retained in
capture metadata, distinguishing it from a directly displayed price.

Only the GPT-6.1 Sol max deferral was removed. Medium, high, and xhigh remain
deferred. The source snapshot now contains 28 pages.

The ingestion worker's CUA session reported the built-in browser unavailable;
its enabled browser inventory contained external Edge browsers. It consumed
the primary agent's built-in browser observations and retained their provenance
without switching browsers. The standalone retained row is
`research/2026-10-08-gpt61-inclusion/gpt61-snapshot-entry.json`.

The primary agent performs independent source review, regeneration, and
publication. No tests, builds, network fetches, or score regeneration were
run by this ingestion worker.
