# Scripts

Browser-driven capture and rendering helpers. Everything that computes scores
or emits documents lives in the `valuerank/` package; see `docs/architecture.md`.

| Script | Purpose | npm entry point |
|---|---|---|
| `scrape-tb4.js` | Capture the client-rendered Terminal-Bench 4.0 leaderboard into `data/tb4-scrape.json` (local-only input for `valuerank.build_tb4`). | `npm run capture:tb4` |
| `generate-og-cards.mjs` | Render the committed Open Graph share cards (`site/**/og.png`) with Playwright. | `npm run generate:og` |

Both scripts need the root Node dependencies (`npm ci`) and a Playwright
Chromium build (`npx playwright install chromium`).
