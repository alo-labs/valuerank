# Current validation evidence

## Final expanded-table check

Final packaging verification: manifest and rollup, including all nine phase records, are `completed_with_disclosed_limitations`; each phase has all seven required fields. No obsolete current statements were found in decision, handoff, critique, or outline. Report format and phase gate passed again after final reconciliation. Raw outputs are saved as report-validator.log, citation-validator.log, claim-validator.log, and phase-gate.log. Remaining below references to pending work describe historical checkpoints superseded by this final verification.

Rerun October 7, 2026 after standard SuperGrok incorporation: format PASS (recommended-heading warning only); citations PASS, 14 references, 10 accessible, 4 unresolved HTTP checks ([2]/[3]/[14] 403; [10] 405); strict claims PASS, 14 claims including 12 factual assertions, 0 unsupported factual, 8 partial, 1 needs_review, 5 supported. OpenAI and xAI fee pages were inspected in the built-in browser; automated access failures remain recorded. Read-only consistency check found 10 numeric table rows with exactly four columns each, 21 sources, 18 evidence records, 14 claims, no missing or duplicate source/claim IDs. Standard Grok calculation is 45.25×52÷12÷30 = 6.536111×. Roster check matches all 13 ranked IDs and all six non-Anthropic providers. The audit's Standard omission was repaired. Prior nine-row check details below are historical checkpoints, not final counts.

Assessed 2026-10-07 10:59 UTC. Scripts are from the explicitly authorized Silver Bullet `skills/silver-deep-research/scripts` directory. These are artifact checks, not independent audits of user token ledgers or proof of exhaustive internet coverage.

## Report format

`validate_report.py --report <package>/research_report.md`: PASS after two repair passes. Executive Summary, required sections, language profile, metadata, citations, bibliography, word count, source count, and local links passed. Warning: recommended Counterevidence Register and Claims-Evidence Table headings absent. Counterevidence and claim/evidence ledgers are separate artifacts.

## Citations

`verify_citations.py --report <package>/research_report.md`: PASS, 12 references, 9 URL checks succeeded, 3 unresolved. OpenAI fee references [2] and [3] returned HTTP 403 to the checker; HN [10] returned HTTP 405. The two OpenAI fee pages were independently inspected in the built-in browser. URL accessibility is not source-content verification. No DOI verification applies.

## Claim support

`verify_claim_support.py verify --dir <package> --strict`: PASS after schema repair and factual classification repair. 12 claims; 10 factual; zero factual claims rated unsupported. Ratings: 8 partial, 1 needs_review, 3 supported. The needs_review Z.AI whole-period estimate remains included as a reported estimate with a cross-cutoff interval, mixed models, and non-reproducible public ledger; this checker rating is not overridden by a claim of independent reproduction.

The first schema-compatible pass had zero factual claims and was not accepted as meaningful strict coverage. Numeric assertions and the Heavy observation were then classified factual, retaining calculation/inference labels separately. Evidence `quote` fields contain explicitly marked paraphrases (`verbatim:false`), not invented verbatim statements.

## Arithmetic and structural consistency

Read-only Node inspection: 9 numeric table rows, exactly 4 columns each; 19 sources, 16 evidence records, 12 claims; no missing cited-source/evidence IDs. Recomputed values: Anthropic 50.9167/44.1308/20.3233; OpenAI Plus19.0667/Pro5x15.2967/Pro20x31.72; Heavy5.785; Z.AI5.67611; Kimi4. Provider maxima order: Anthropic, OpenAI, xAI, Z.AI, Moonshot. Rounding agrees with displayed rows.

## Remaining acceptance work

`phase_gate.py --dir <package>`: PASS for all nine phase artifact checks. This verifies expected artifacts exist; it does not prove substantive source coverage. Independent scope audit and reconciliation of all phase/manifest statuses remain pending. Heavy supporting report.md could not be opened because the browser client blocked it. The independently inspected primary page supplies the reported estimate, with that reproduction limit visible.
