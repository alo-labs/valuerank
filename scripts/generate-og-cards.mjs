#!/usr/bin/env node
/**
 * Generate ValueRank Open Graph / WhatsApp share cards (1200×630 PNG).
 * Usage: node scripts/site-generate-og-cards.mjs
 * Requires: playwright (repo root node_modules)
 */
import { chromium } from "playwright";
import { mkdirSync, writeFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = dirname(__dirname);
const TMP = join(ROOT, ".tmp", "og");

const SHARED_CSS = `
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px; height: 630px; overflow: hidden;
    font-family: 'IBM Plex Sans', system-ui, sans-serif;
    background: linear-gradient(135deg, #eef2ff 0%, #f5f3ff 45%, #fdf2f8 100%);
    color: #0f172a;
  }
  .frame {
    width: 1200px; height: 630px; position: relative;
    padding: 56px 64px 0; display: flex; flex-direction: column;
  }
  .brand {
    font-family: 'IBM Plex Mono', monospace; font-weight: 600;
    font-size: 28px; letter-spacing: 0.04em; color: #4f46e5; margin-bottom: 28px;
  }
  .title {
    font-size: 58px; font-weight: 700; line-height: 1.08;
    letter-spacing: -0.02em; color: #0f172a; max-width: 700px;
  }
  .title.compact { font-size: 52px; max-width: 680px; }
  .subtitle {
    margin-top: 16px; font-size: 34px; font-weight: 600;
    color: #4f46e5; letter-spacing: -0.01em; max-width: 680px; line-height: 1.2;
  }
  .desc {
    margin-top: 24px; font-size: 22px; font-weight: 400;
    color: #475569; line-height: 1.45; max-width: 620px;
  }
  .pill-row { margin-top: 32px; display: flex; gap: 14px; align-items: center; flex-wrap: wrap; }
  .pill {
    display: inline-flex; align-items: center; gap: 10px;
    background: rgba(255,255,255,0.85); border: 1px solid rgba(79,70,229,0.18);
    border-radius: 999px; padding: 10px 18px; font-size: 16px; font-weight: 500; color: #334155;
  }
  .dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
  .dot-indigo { background: #4f46e5; }
  .dot-purple { background: #7c3aed; }
  .dot-green { background: #059669; }
  .dot-amber { background: #d97706; }
  .viz {
    position: absolute; right: 56px; top: 90px; width: 380px; height: 340px;
    background: rgba(255,255,255,0.72); border: 1px solid rgba(79,70,229,0.12);
    border-radius: 24px; box-shadow: 0 20px 50px rgba(79,70,229,0.10); overflow: hidden;
  }
  .viz-inner { position: relative; width: 100%; height: 100%; padding: 28px 24px 24px; }
  .viz-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 13px; font-weight: 500;
    color: #64748b; letter-spacing: 0.02em; margin-bottom: 12px;
  }
  .plot {
    position: relative; width: 100%; height: calc(100% - 28px);
    border-left: 2px solid #cbd5e1; border-bottom: 2px solid #cbd5e1;
  }
  .pt {
    position: absolute; width: 14px; height: 14px; border-radius: 50%;
    transform: translate(-50%, 50%);
  }
  .pt.d { background: #a78bfa; opacity: 0.75; }
  .pt.p { background: #059669; box-shadow: 0 0 0 4px rgba(5,150,105,0.18); }
  .pt.i { background: #4f46e5; box-shadow: 0 0 0 4px rgba(79,70,229,0.18); }
  .bar {
    position: absolute; bottom: 0; width: 28px; border-radius: 6px 6px 0 0;
    transform: translateX(-50%);
  }
  .bar.b1 { background: #4f46e5; }
  .bar.b2 { background: #6366f1; opacity: 0.85; }
  .bar.b3 { background: #a78bfa; opacity: 0.8; }
  .axis-x, .axis-y {
    position: absolute; font-family: 'IBM Plex Mono', monospace;
    font-size: 12px; color: #94a3b8;
  }
  .axis-x { bottom: 6px; right: 8px; }
  .axis-y { top: 4px; left: 8px; }
  .footer {
    position: absolute; left: 0; right: 0; bottom: 0; height: 72px;
    background: #1e1b4b; display: flex; align-items: center; justify-content: space-between;
    padding: 0 64px; font-family: 'IBM Plex Mono', monospace; font-size: 18px; color: #e2e8f0;
  }
  .footer .muted { color: #a5b4fc; }
`;

const CARDS = [
  {
    id: "home",
    out: join(ROOT, "site/og.png"),
    html: `
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><style>${SHARED_CSS}</style></head>
<body>
  <div class="frame">
    <div class="brand">ValueRank</div>
    <h1 class="title">ValueRank</h1>
    <div class="subtitle">Frontier models ranked on real-world value</div>
    <p class="desc">Independent rankings from Artificial Analysis &amp; DeepSWE Best.<br>Quality, cost, and value — one score.</p>
    <div class="pill-row">
      <div class="pill"><span class="dot dot-indigo"></span> v1.4.0</div>
      <div class="pill"><span class="dot dot-green"></span> 21 models</div>
    </div>
    <div class="viz" aria-hidden="true">
      <div class="viz-inner">
        <div class="viz-label">Value vs Cost</div>
        <div class="plot">
          <span class="axis-y">Value</span>
          <span class="axis-x">Cost →</span>
          <span class="pt d" style="left:20%; bottom:30%"></span>
          <span class="pt d" style="left:32%; bottom:42%"></span>
          <span class="pt d" style="left:45%; bottom:38%"></span>
          <span class="pt d" style="left:55%; bottom:55%"></span>
          <span class="pt d" style="left:68%; bottom:48%"></span>
          <span class="pt d" style="left:78%; bottom:62%"></span>
          <span class="pt i" style="left:28%; bottom:68%"></span>
          <span class="pt i" style="left:48%; bottom:78%"></span>
          <span class="pt i" style="left:72%; bottom:85%"></span>
        </div>
      </div>
    </div>
    <div class="footer">
      <span>valuerank.alolabs.dev</span>
      <span class="muted">Open source · Independent</span>
    </div>
  </div>
</body></html>`,
  },
  {
    id: "coding-agents",
    out: join(ROOT, "site/coding-agents/og.png"),
    html: `
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><style>${SHARED_CSS}</style></head>
<body>
  <div class="frame">
    <div class="brand">ValueRank</div>
    <h1 class="title compact">Coding Agent ValueRank</h1>
    <div class="subtitle">value per dollar</div>
    <p class="desc">Historical AA Coding Agent Index + Terminal-Bench 2.1 snapshot.<br>Current benchmark data is on the TB4 page.</p>
    <div class="pill-row">
      <div class="pill"><span class="dot dot-indigo"></span> Historical</div>
      <div class="pill"><span class="dot dot-green"></span> 42 agents</div>
    </div>
    <div class="viz" aria-hidden="true">
      <div class="viz-inner">
        <div class="viz-label">Overall vs Cost</div>
        <div class="plot">
          <span class="axis-y">Overall</span>
          <span class="axis-x">Cost →</span>
          <span class="bar b3" style="left:18%; height:42%"></span>
          <span class="bar b2" style="left:32%; height:58%"></span>
          <span class="bar b1" style="left:46%; height:78%"></span>
          <span class="bar b2" style="left:60%; height:64%"></span>
          <span class="bar b3" style="left:74%; height:50%"></span>
          <span class="bar b1" style="left:88%; height:70%"></span>
        </div>
      </div>
    </div>
    <div class="footer">
      <span>valuerank.alolabs.dev/coding-agents</span>
      <span class="muted">Open source · Independent</span>
    </div>
  </div>
</body></html>`,
  },
  {
    id: "tb4",
    out: join(ROOT, "site/tb4/og.png"),
    html: `
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><style>${SHARED_CSS}</style></head>
<body>
  <div class="frame">
    <div class="brand">ValueRank</div>
    <h1 class="title">Terminal-Bench 4.0</h1>
    <div class="subtitle">Score vs Cost</div>
    <p class="desc">Resolution rate (%) vs Cost (USD) with Pareto frontier.<br>Official snapshot from tbench.ai</p>
    <div class="pill-row">
      <div class="pill"><span class="dot dot-purple"></span> Dominated</div>
      <div class="pill"><span class="dot dot-green"></span> Pareto frontier</div>
    </div>
    <div class="viz" aria-hidden="true">
      <div class="viz-inner">
        <div class="viz-label">Accuracy vs Cost</div>
        <div class="plot">
          <span class="axis-y">Acc %</span>
          <span class="axis-x">Cost →</span>
          <span class="pt d" style="left:18%; bottom:22%"></span>
          <span class="pt d" style="left:28%; bottom:38%"></span>
          <span class="pt d" style="left:36%; bottom:48%"></span>
          <span class="pt d" style="left:44%; bottom:42%"></span>
          <span class="pt d" style="left:52%; bottom:55%"></span>
          <span class="pt d" style="left:58%; bottom:62%"></span>
          <span class="pt d" style="left:68%; bottom:58%"></span>
          <span class="pt d" style="left:74%; bottom:70%"></span>
          <span class="pt d" style="left:82%; bottom:66%"></span>
          <span class="pt p" style="left:22%; bottom:58%"></span>
          <span class="pt p" style="left:40%; bottom:72%"></span>
          <span class="pt p" style="left:62%; bottom:82%"></span>
          <span class="pt p" style="left:88%; bottom:88%"></span>
        </div>
      </div>
    </div>
    <div class="footer">
      <span>valuerank.alolabs.dev/tb4</span>
      <span class="muted">Open source · Independent</span>
    </div>
  </div>
</body></html>`,
  },
];

async function main() {
  mkdirSync(TMP, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  try {
    for (const card of CARDS) {
      const htmlPath = join(TMP, `${card.id}.html`);
      writeFileSync(htmlPath, card.html);
      const page = await browser.newPage({
        viewport: { width: 1200, height: 630 },
        deviceScaleFactor: 1,
      });
      await page.goto(`file://${htmlPath}`, { waitUntil: "networkidle" });
      await page.waitForTimeout(900);
      mkdirSync(dirname(card.out), { recursive: true });
      await page.screenshot({ path: card.out, type: "png" });
      await page.close();
      console.log(`wrote ${card.out}`);
    }
  } finally {
    await browser.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
