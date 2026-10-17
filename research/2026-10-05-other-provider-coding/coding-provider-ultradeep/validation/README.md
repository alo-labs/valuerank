# Validation record

All commands below used the supported local LeanCTX CLI route (`/Users/shafqat/.local/bin/lean-ctx -c "..."`) from the ValueRank checkout.

| Check | Command | Result |
|---|---|---|
| Package data validator | `/Users/shafqat/.local/bin/lean-ctx -c "node validate-coding-provider-package.js"` | Pass; prior addendum audit and new package crosswalk/count/hash/tier/class checks have no errors. |
| Silver Bullet phase gate | `/Users/shafqat/.local/bin/lean-ctx -c "python3 /Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research/scripts/phase_gate.py --dir coding-provider-ultradeep --mode ultradeep"` | Pass; all nine Ultradeep phase artifact gates pass. |
| Silver Bullet report validation | `/Users/shafqat/.local/bin/lean-ctx -c "python3 /Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research/scripts/validate_report.py --report coding-provider-ultradeep/research_report.md"` | Pass; all checks passed. |
| Silver Bullet citation verification | `/Users/shafqat/.local/bin/lean-ctx -c "python3 /Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research/scripts/verify_citations.py --report coding-provider-ultradeep/research_report.md"` | Pass; 19/19 URLs verified, 0 suspicious, 0 unverified. |
| Silver Bullet claim support | `/Users/shafqat/.local/bin/lean-ctx -c "python3 /Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research/scripts/verify_claim_support.py verify --dir coding-provider-ultradeep"` | Pass; 8 claims, 0 unsupported factual claims. |

Raw command output is in the adjacent `.log` files. The shared LeanCTX MCP `ctx_execute` probe separately returned `agent capacity reached 15/15 live workers`; local CLI validation nevertheless completed. The repository alias/skill access problem was corrected before the package was built. The phase gate was run, but no `/sb ultradeep` orchestration command was invoked; the phase workflow is evidenced by its artifacts and the passing gate, not by an orchestration invocation.

After adding explicit tier and reporter fields to the canonical evidence ledger, the package validator, Ultradeep phase gate, report validator, citation verifier, and claim-support verifier were rerun on 2026-10-05. The latest invocation results are summarized in [evidence-tier-revalidation.md](evidence-tier-revalidation.md); the original `.log` files above are preserved from the first full package validation.

These automated checks establish schema-like integrity, artifact presence, citation URL accessibility, report quality checks, and claim/evidence ID support. They do not authenticate user identities, independently verify account screenshots, or make the anecdotal usage representative. Search no-hit results remain bounded to returned results. The retained exact query log has 47 strings; a small earlier official-document search set had its literals omitted from the captured handoff transcript.
