# Decision record

## Decision

Do not publish or use a numeric Codex community allowance value from this package. The only eligible source is the TiboTattle homepage, and its 2026-10-05 capture showed a checking/loading state without a numeric value or sample count.

## Basis

- Scope and one-month cutoff: scope.md, research-plan.md.
- Homepage observation and distinctions: evidence.jsonl entries mapped from legacy E01–E04 and E28.
- Claim support and caveats: claims.jsonl, triangulation.md.
- Three adversarial review loops: critique.md.
- Validation: see exact logs in validation/.

## Guardrails for future refreshes

1. Use only https://tibotattle.com/ for a numeric Codex crowd allowance result.
2. Keep a retrieval timestamp and exact chart/unit/sample labels.
3. Exclude synthetic demonstrations and values from discovery sources.
4. Apply a rolling one-month cutoff to empirical user reports.
5. Record the exact plan tier for every user datapoint or mark it “not stated.”
6. Do not interpret a loading state as evidence that an estimate has never existed.

## Unresolved

- The current page can change after capture.
- No independent audit of TiboTattle contributions was performed.
- App discovery is bounded, not exhaustive.
- The SB run_manifest.schema.json and SKILL.md output-session field lists conflict; see workflow_record.json and validation/manifest-contract.log.
