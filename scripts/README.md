# Scripts

Browser-driven capture and rendering helpers. Everything that computes scores, emits documents or renders the site lives in the `valuerank/` package; see `docs/architecture.md`.

| Script | Purpose | npm entry point |
|---|---|---|
| `scrape-tb4.js` | Capture the client-rendered Terminal-Bench 4.0 leaderboard into `data/tb4-scrape.json` (local-only input for `valuerank.build_tb4`). | `npm run capture:tb4` |
| `generate-og-cards.mjs` | Render the Open Graph share cards (1200×630 PNG) into `site/` with Playwright. Three cards today: `site/og.png` (home), `site/coding-agents/og.png` and `site/tb4/og.png`. Per-page cards for the generated site are not produced yet; see `docs/site-experience-plan.md`, phase 5. | `npm run generate:og` |

Both scripts need the root Node dependencies (`npm ci`) and a Playwright Chromium build (`npx playwright install chromium`).
