# OpenCode Go re-fetch, 2026-11-26 (O198, third-party plan)

Instruction: re-fetch https://opencode.ai/docs/console/go/ , save the page with its SHA-256 and instant, and say whether its per-model monthly dollar limits or listed models changed against `research/2026-11-11-opencode-go/`. No multiples are recomputed here.

## Saved copies (byte-exact, `raw/`)

| File | URL | Fetch instant (UTC) | Bytes | SHA-256 |
|---|---|---|---|---|
| `raw/opencode-go-docs.html` | https://opencode.ai/docs/console/go/ | 2026-11-26T03:10:58Z (HTTP `date` header 03:10:58 GMT; Cloudflare `cf-cache-status: HIT`, `max-age=300`) | 78,448 | `40c238db6cfc8ae3dcb3ecef1c309af1e1a376bebd2ca12cf7b85228a971379c` |
| `raw/opencode-go-docs.md` | https://opencode.ai/docs/console/go.md (the page's markdown source) | 2026-11-26T03:11:17Z | 22,430 | `cfbf5f77b6016fc732e9c7e8b98ff1703e77e70e6fdcfd597a5afce32a0b9b85` |
| `raw/opencode-console-models.html` | https://opencode.ai/docs/console/models/ (the page the Go page now sends readers to for the model list) | 2026-11-26T03:11:17Z | 104,409 | `29990757262dbb00a2563eb9034ad1f431058bd4222082c8c0ed42fec0553f15` |
| `raw/go-v1-models.json` | https://opencode.ai/inference/go/v1/models (model list API; the Go page says it holds "Go's monthly usage limits") | 2026-11-26T03:11:17Z | 49,432 | `d49d1038b073755d87567b0febf56e3015e66c89b16a9920437f50d5b23ccc8f` |

Previous copy for comparison: `research/2026-11-11-opencode-go/raw/opencode-go-docs.html` (fetched 2026-11-11T11:56:17Z, SHA-256 `1c2a1a4742b9b065c648967113bfc5bdc3be983ca41d219c9040846158c49d4b`, 98,416 bytes). Response headers of the new fetches are in `raw/*headers.txt`.

## Finding 1: the Go docs page no longer carries the per-model limit table or the model list

The 2026-11-11 page printed three tables (Go, Go Plus, Go Teams) with "Monthly limit" per model and a "current list of models". The 2026-11-26 page does not. It says "See the current list of models" (link to `/docs/console/models/`, which holds prices and ids but no Go limits) and "See the model list API for every field in the response, including Go's monthly usage limits" (`/inference/go/v1/models`, field `go.monthly_usage`). The per-model monthly dollar limits are therefore read from the model list API, whose values equal the old docs table row for 23 of its 37 rows (identical on all three plans; 3 rows differ, 7 are new with limits, 2 free rows report null for "Unlimited" and 2 free models are new; see Finding 2), which supports it being the same source of record. The Go page text states the same rules as before: the five-hour limit is 20% and the weekly limit 50% of the monthly allowance, and each model's monthly limit "shows how much usage your plan covers if you use only that model over the month".

## Finding 2: limits and listed models that changed (per-model monthly dollar limit, Go / Go Plus / Go Teams)

Machine-readable: `go-limits-comparison.json` (all 37 API rows, old and new values).

| Model | 2026-11-11 table | 2026-11-26 API | Change |
|---|---|---|---|
| GLM-5.3 | $15 / $120 / $20 | $200 / $400 / $205 | limit raised (about 13x on Go); not a cohort model |
| Kimi K3.1 Pro | $15 / $60 / $20 | $60 / $120 / $65 | limit raised (4x on Go); not in the cohort |
| LongCat | "LongCat 2.5 Free", unlimited, free for a limited time; LongCat-2.0 $60 / $240 / $65 | "LongCat-2.5" $60 / $240 / $65 (paid) | free tier replaced by a paid entry; LongCat-2.0 gone |
| Qwen4 Max | not listed | $15 / $60 / $20 | model added |
| Hy4 flash Free, HungerG Free | not listed | free, `monthly_usage` null | models added |
| Jev 1.14, Gemini Decision 1, GPT 6 Luna Decision, text-embedding-3-small, Qwen3 Embedding 8B, Gemini Embedding 2 | not listed | $10 / $40 / $15 each | decision and embedding models added (listed at list price, no Go discount) |
| GLM-5.2, MiMo-V2.5, MiMo-V2.5-Pro | $60 / $180 / $65; $60 / $120 / $65; $15 / $60 / $20 | not listed | models removed |

Every other model the old table priced (23 of the 37 API rows, including all three cohort models) has identical limits on Go, Go Plus and Go Teams. Beam Free and Iceman Contributor Free were "Unlimited, limited time" in the table and report `monthly_usage: null` in the API (still free).

## Finding 3: the cohort models OpenCode Go lists

| Cohort model | Go page 2026-11-11 | Go API 2026-11-26 | Changed |
|---|---|---|---|
| GPT-6 Luna (listed "GPT 6 Luna" before) | $15 / $60 / $20; $0.10 in, $0.50 out, $0.01 cache read, $0.125 cache write per 1M (up to 272K tokens) | $15 / $60 / $20; same rates (`cost` object, with the over-272K override $0.20 / $0.75) | no |
| Claude Haiku 5.5 | $15 / $60 / $20; $0.10 / $0.50 / $0.01 / $0.125 (up to 100K tokens) | $15 / $60 / $20; same rates (override over 100K: $0.50 / $2.50) | no |
| MiMo-V2.6-Flash | $60 / $120 / $65; $0.14 in, $0.28 out, $0.0028 cache read | $60 / $120 / $65; same rates | no |

Not listed on OpenCode Go at all: Claude Fable 5.2, Opus 5.5, Sonnet 5.5; GPT-6.2 Sol, GPT-6.2 Astra, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Astra; Gemini 4 Neon, Gemini 4 Carbon (Gemini 4 Argon is listed, $30 / $120 / $35, not a cohort model now); Muse Ember (only Muse Spark 1.2 and 1.3 Contributor are listed, $60 / $120 / $65).

So for the cohort: no per-model monthly dollar limit changed and no cohort model was added or removed since 2026-11-11.

## Finding 4: plan terms and other text that changed on the page

- Go Teams price line: "$20/member/month" became "$20/member/month, 2-member minimum" ($40/month; "the second seat covers the next member who joins at no extra charge"). Go ($10/month) and Go Plus ($40/month) prices are unchanged.
- "Go and Go Plus are for workspaces with a single member" became "Go and Go Plus cover the member who subscribes and the workspace's API keys. Other members you invite use free models or the workspace balance."
- Gemini 4 Argon: "The 50% discount applies through November 30, 2026"; the model API carries a price multiplier of 2 from 2026-12-01 (`cost.multipliers` date gte 2026-12-01). Argon is not a cohort model.
- DeepSeek off-peak/peak handling is now in the API (`cost.multipliers`, factor 2 on Mon-Fri 01:00-04:00 and 06:00-10:00 UTC) instead of two table rows; the limit is the same $100.
- New sections: Decision models, Embedding models, a usage endpoint, "Why some models have lower usage".

## Not compared

Go Plus and Go Teams are not Plan-basis plans (AGENTS.md), so their changes are listed only for completeness. The plan's terms at the 2026-11-01 cutoff were not observed (owner decision O203 already notes this); this re-fetch does not change that.
