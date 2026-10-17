# Scripts

Browser-driven capture and rendering helpers. Everything that computes scores, emits documents or renders the site lives in the `valuerank/` package; see `docs/architecture.md`.

| Script | Purpose | npm entry point |
|---|---|---|
| `scrape-tb4.js` | Capture the client-rendered Terminal-Bench 4.0 leaderboard into `data/tb4-scrape.json` (local-only input for `valuerank.build_tb4`). | `npm run capture:tb4` |
| `generate-og-cards.mjs` | Render the Open Graph share cards (1200×630 PNG) with Playwright from `site/data/`: one per core page (`site/og/<key>.png`), one per roster model (`site/og/models/<slug>.png`) and `site/og/archive.png`. Run it after `npm run build:site`, or use `npm run build:publication`, which does both. | `npm run generate:og` |

Both scripts need the root Node dependencies (`npm ci`) and a Playwright Chromium build (`npx playwright install chromium`).
