# ValueRank methodology co-design (2026-10-19 to 2026-11-22)

This folder is the record of the design of ValueRank's v3 value-scoring methodology, from the first draft to the release draft, reviewed by a panel of AI models and decided by the owner.

## Where things are

| What | File |
|---|---|
| The release draft of the methodology (the generated text, figures resolved from the data) | `draft-r231.md` (and `.src.md`, the source with `{{...}}` placeholders); every earlier revision `draft-rNN.md` is kept |
| Every decision with its rationale (owner decisions O1 to O204, editor decisions E1 to E357+, reviewer by reviewer triage) | `ledger.md` |
| The compact decision list that the reviewers read | `ledger-brief.md` |
| The review panel's records, prompts, outputs and resume state | `perplexity/` (`RESUME.md` has one row per reviewer) |
| Internal Claude review ladder (rounds I1 to I90+) | `review-i*.md` |
| Plan-allowance research (three-stage, one folder per search) | `../2026-10-25-plan-allowances*/`, `../2026-10-31-plan-allowances-v5-entrants/`, `../2026-11-05-plan-allowances/` |
| OpenCode Go plan page, archived with its SHA-256 (O198, O199) | `../2026-11-11-opencode-go/` |
| A dry run of moving the cutoff to 2026-11-12, not adopted (O203) | `../2026-11-12-recapture-dry-run/` |
| A nine-configuration comparison with Pareto charts | `../comparison-2026-11/` |
| Handoff prompt for another session | `HANDOFF.md` |

## What the methodology does

Value is 75% quality and 25% cost, on 0-100 scales, per configuration and basis. Quality is a weighted mean of benchmark leaves for the exact configuration (software engineering 60%). Cost is AA's published cost to run an SDLC basket, scored on a log scale against frozen anchors; on the Plan basis the cost is divided by a subscription route's Value Multiple. Interval outputs, noise bands and scenario shares sit beside the displayed record and never change a score. The draft states each rule with its decision numbers.

## The review

Six models (GPT Sol, Claude Sonnet, Kimi, GLM, Grok and a Gemini) reviewed successive drafts through Perplexity; valid findings became wording or code, owner-decision challenges went to the owner. A model is done when it returns no Medium-or-higher finding in two consecutive rounds (O56). The state at the time of writing is in `perplexity/RESUME.md`.

## Open for the next release

- AA's chart of 2026-11-12 (Index v5.0.1, 122 models) re-cohorts the ranking and thins the max-effort ranking; see `../2026-11-12-recapture-dry-run/`.
- A three-stage plan search for Meta, Claude Fable 5.2 plan cells and the Anthropic and OpenAI changes found by the freshness check.
- Monthly controlled saturation measurements (owner action); the unbuilt O193 path (the API basis migrating alone when Plan references are short).
- Candidates the reviewers raised that were not adopted are listed per round in `ledger.md` ("left candidates").
