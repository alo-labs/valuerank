# Adversarial critique — DR-CRITIQUE

Ultradeep's three critique cycles are recorded below. These were manual persona-based reviews of the evidence and report, not separate subagent runs. Each cycle used skeptical-practitioner, reviewer, and red-team questions.

## Cycle 1 — Scope and measurement units

- **Skeptical practitioner:** Can an account reader, local estimate, or API price page answer “how many consumer chats did my plan allow”? No; those are distinct data classes.
- **Adversarial reviewer:** Did coding surfaces contaminate chat claims? Yes, the original Mistral Vibe and Grok Build reports were mixed into consumer-plan narrative.
- **Red-team delta:** `unsupported_inference`, medium, loopback=true — separate actual provider quota, local estimate, API spend and crowdsourced reports; remove Vibe/Grok Build usage from chat estimates.
- **Repair:** Reclassified AIRadar as a local estimate; classified OpenUsage as spend/API/coding; retained TiboTattle only as homepage-based Codex discovery; excluded coding-only measurements.

## Cycle 2 — Tier attribution and surface ambiguity

- **Skeptical practitioner:** Are tier labels attributable to the specific poster/commenter? The Gemini Sep 13 image alt text is not; ChatGPT Sep 18 surface is not.
- **Adversarial reviewer:** Did a monthly price silently become a product tier? Yes, Poe's £20/month post does not name its tier.
- **Red-team delta:** `unsupported_inference`, high, loopback=true — attribute only the exact user-stated plan or “not stated”; separate per-commenter HN reports.
- **Repair:** Added per-user tier statements for Grok HN and Mistral Vibe; Poe Sep 26 and Meta/DeepSeek/Gemini ambiguous posters are marked “not stated”; ChatGPT reports remain Plus with the first surface ambiguous.

## Cycle 3 — Source quality and validation

- **Skeptical practitioner:** Are one-user reports representative? No; all are qualitative and non-transferable.
- **Adversarial reviewer:** Did a store listing or README prove the feature works accurately? No; these remain developer claims, not audited telemetry.
- **Red-team delta:** `missing_source_class`, medium, loopback=true — add official Gemini/ChatGPT policies, date-bounded community searches, and separate app classes.
- **Repair:** Added official policy sources and Reddit-first provider searches plus HN/developer gap searches; recorded exact query outcomes; added bibliography, counterevidence register, and claims-evidence table.

**Stopping decision:** No high-severity factual ambiguity remains in the report because unresolved observations are explicitly qualified or excluded. The residual gap is lack of independently audited multi-account data and non-exhaustive public indexing; this is documented in `handoff.md` and the report limitations.
