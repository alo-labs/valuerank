/**
 * Generate the ValueRank Open Graph share cards (1200×630 PNG) from the published site data.
 * Usage: node scripts/generate-og-cards.mjs   (after `npm run build:site` has written site/data)
 * Requires: playwright (repo root node_modules) and a Chromium build.
 *
 * Writes one card per core page to site/og/<key>.png, one per roster model to
 * site/og/models/<slug>.png and the archive card to site/og/archive.png. The card
 * builders are pure functions; only readPublication, run and main touch files or the browser.
 */
import { mkdirSync, readFileSync, readdirSync, realpathSync, writeFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = dirname(__dirname);
const VIEWPORT = { width: 1200, height: 630 };
const SETTLE_MS = 900;
const SITE_OG = ["site", "og"];

// Tokens mirror the light theme in valuerank/site/assets/css/site.css.
const SHARED_CSS = `
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
  :root {
    --bg: #f6f6fb; --surface: #ffffff; --text: #14152b; --text-muted: #55587a; --border: #dcdceb;
    --accent: #4f46e5; --accent-soft: #e9e8fd;
    --g-measured: #0b6b42; --g-measured-bg: #dff3e8;
    --g-claim: #1c4fa3; --g-claim-bg: #e2edfb;
    --g-estimate: #7a4e00; --g-estimate-bg: #fdf0d2;
    --g-assumption: #7b2a8f; --g-assumption-bg: #f5e4fa;
    --g-missing: #50546b; --g-missing-bg: #eceef4;
    --font-sans: 'IBM Plex Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { width: 1200px; height: 630px; overflow: hidden; background: var(--bg); color: var(--text); font-family: var(--font-sans); }
  .frame {
    position: relative; width: 1200px; height: 630px; padding: 56px 72px 0;
    display: flex; flex-direction: column;
    background: linear-gradient(135deg, #f6f6fb 0%, #ebeafb 100%);
  }
  .frame::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 12px; background: var(--accent); }
  .top { display: flex; align-items: center; justify-content: space-between; }
  .wordmark { font-family: var(--font-mono); font-size: 28px; font-weight: 600; letter-spacing: 0.02em; color: var(--accent); }
  .version {
    font-family: var(--font-mono); font-size: 18px; font-weight: 500; color: var(--accent);
    background: var(--accent-soft); border-radius: 999px; padding: 6px 16px;
  }
  .kicker {
    margin-top: 44px; font-family: var(--font-mono); font-size: 18px; font-weight: 500;
    letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-muted);
  }
  .headline { margin-top: 12px; font-size: 56px; font-weight: 700; line-height: 1.08; letter-spacing: -0.02em; max-width: 1000px; }
  .description { margin-top: 18px; font-size: 24px; line-height: 1.35; color: var(--text-muted); max-width: 1000px; }
  .pills { margin-top: 28px; display: flex; flex-wrap: wrap; gap: 12px; }
  .pill {
    font-family: var(--font-mono); font-size: 18px; font-weight: 500; padding: 8px 16px;
    border-radius: 999px; background: var(--surface); border: 1px solid var(--border); color: var(--text);
  }
  .pill.rank { background: var(--accent-soft); border-color: transparent; color: var(--accent); }
  .pill.g-measured { background: var(--g-measured-bg); border-color: transparent; color: var(--g-measured); }
  .pill.g-claim { background: var(--g-claim-bg); border-color: transparent; color: var(--g-claim); }
  .pill.g-estimate { background: var(--g-estimate-bg); border-color: transparent; color: var(--g-estimate); }
  .pill.g-assumption { background: var(--g-assumption-bg); border-color: transparent; color: var(--g-assumption); }
  .pill.g-missing { background: var(--g-missing-bg); border-color: transparent; color: var(--g-missing); }
  .stats { margin-top: auto; margin-bottom: 92px; display: flex; gap: 20px; }
  .stat {
    flex: 1; min-width: 0; background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
    padding: 18px 22px; box-shadow: 0 1px 2px rgb(20 21 43 / 0.06), 0 4px 16px rgb(20 21 43 / 0.06);
  }
  .stat-value { font-family: var(--font-mono); font-size: 44px; font-weight: 600; line-height: 1.1; color: var(--accent); overflow-wrap: anywhere; }
  .stat-value.long { font-size: 30px; }
  .stat-label { margin-top: 8px; font-size: 18px; color: var(--text-muted); }
  .footer {
    position: absolute; left: 72px; right: 64px; bottom: 0; height: 64px;
    display: flex; align-items: center; justify-content: space-between;
    border-top: 1px solid var(--border); font-family: var(--font-mono); font-size: 17px; color: var(--text-muted);
  }
`;

const HTML_ESCAPES = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
const GRADES = ["measured", "claim", "estimate", "assumption", "missing"];

/** Escapes text for HTML element content and quoted attribute values. */
export function escapeHtml(text) {
  return String(text).replace(/[&<>"']/g, (character) => HTML_ESCAPES[character]);
}

const stat = (value, label) => ({ value, label });

/** Only the known evidence grades become CSS classes; anything else is drawn as "missing". */
function gradeClass(grade) {
  return `g-${GRADES.includes(grade) ? grade : "missing"}`;
}

function formatScore(value) {
  return value === null ? "—" : value.toFixed(1);
}

function formatPercent(value) {
  return `${value.toFixed(1)}%`;
}

function formatUsd(value) {
  return `$${value.toFixed(2)}`;
}

function rankedModels(rankings) {
  return rankings.models.filter((model) => model.rankingEligible);
}

function rankPill(basis, rank) {
  return rank === null ? `${basis} unranked` : `${basis} #${rank}`;
}

// The core pages in catalogue order. Each stats function reads only the publication documents.
const CORE_PAGES = [
  {
    key: "index",
    path: "/",
    kicker: "Overview",
    headline: "Which AI model delivers the most value?",
    description: "Frontier models ranked on measured quality against API and plan cost.",
    stats({ rankings }) {
      const pick = rankings.models.find((model) => model.slug === rankings.picks.plan.value.slug);
      return [
        stat(pick.name, "Top Plan pick"),
        stat(formatScore(pick.overall.plan), "Plan overall"),
        stat(String(rankedModels(rankings).length), "Models ranked"),
      ];
    },
  },
  {
    key: "rankings",
    path: "/rankings/",
    kicker: "Rankings",
    headline: "Every ranked model, on every dimension",
    description: "Filter, sort and compare the full table on either the Plan or the API basis.",
    stats({ rankings }) {
      return [
        stat(`${rankedModels(rankings).length} of ${rankings.models.length}`, "Models ranked"),
        stat(String(rankings.dimensions.length), "Dimensions"),
        stat(formatPercent(rankings.costWeightPct), "Default cost weight"),
      ];
    },
  },
  {
    key: "models",
    path: "/models/",
    kicker: "Roster",
    headline: "The ValueRank model roster",
    description: "Every roster model with its ranks, evidence grade and sourced scores.",
    stats({ rankings }) {
      return [
        stat(String(rankings.models.length), "Roster models"),
        stat(String(rankedModels(rankings).length), "Ranked"),
        stat(String(new Set(rankings.models.map((model) => model.developer)).size), "Developers"),
      ];
    },
  },
  {
    key: "plans",
    path: "/plans/",
    kicker: "Plans",
    headline: "Subscription plan value",
    description: "Allowances and token efficiency, combined into cost per Index point.",
    stats({ plans }) {
      const priced = plans.candidates.filter((candidate) => candidate.planUsdPerPoint !== null);
      const cheapest = Math.min(...priced.map((candidate) => candidate.planUsdPerPoint));
      return [
        stat(formatUsd(cheapest), "Best cost per Index point"),
        stat(String(plans.routes.length), "Plan routes"),
        stat(String(priced.length), "Models priced on a plan"),
      ];
    },
  },
  {
    key: "benchmarks",
    path: "/benchmarks/",
    kicker: "Benchmarks",
    headline: "The benchmarks behind each score",
    description: "Sources, owners, versions, observation dates and coverage for every dimension.",
    stats({ benchmarks }) {
      return [
        stat(String(benchmarks.sources.length), "Benchmark sources"),
        stat(String(benchmarks.aaComponents.length), "Index components"),
        stat(String(benchmarks.coverageMatrix.cohortN), "Cohort models"),
      ];
    },
  },
  {
    key: "tb4",
    path: "/benchmarks/terminal-bench-4/",
    kicker: "Terminal-Bench 4.0",
    headline: "Terminal-Bench 4.0: resolution against cost",
    description: "The official leaderboard, with cohort coverage and labelled provider claims.",
    stats({ tb4 }) {
      return [
        stat(String(tb4.rows.length), "Official rows"),
        stat(String(tb4.frontierCount), "On the frontier"),
        stat(`${tb4.matchedN} of ${tb4.cohortN}`, "Cohort models matched"),
      ];
    },
  },
  {
    key: "methodology",
    path: "/methodology/",
    kicker: "Methodology",
    headline: "How ValueRank scores a model",
    description: "Dimensions, weights, renormalisation, evidence grades and a worked example.",
    stats({ rankings }) {
      return [
        stat(String(rankings.dimensions.length), "Dimensions"),
        stat(formatPercent(rankings.costWeightPct), "Cost weight"),
      ];
    },
  },
  {
    key: "changelog",
    path: "/changelog/",
    kicker: "Changelog",
    headline: "Every ValueRank release",
    description: "Each release with its cohort, dimensions and rank changes, newest first.",
    stats({ changelog }) {
      const [latest] = changelog.versions;
      return [
        stat(latest.version, "Latest release"),
        stat(latest.date, "Released"),
        stat(String(changelog.versions.length), "Releases recorded"),
      ];
    },
  },
  {
    key: "data",
    path: "/data/",
    kicker: "Data",
    headline: "Machine-readable data for every table",
    description: "JSON downloads with their schema and provenance, one document per table.",
    stats({ rankings, dataFileCount }) {
      return [
        stat(String(dataFileCount), "JSON files"),
        stat(String(rankings.models.length), "Model documents"),
      ];
    },
  },
];

const ARCHIVE = {
  kicker: "Archive",
  headline: "Coding Agent ValueRank v0.3",
  description: "Historical coding-agent results on Terminal-Bench 2.1, kept for provenance.",
  pills: ["Archived", "No longer updated"],
  stats: [stat("42", "Agents in the snapshot"), stat("2.1", "Terminal-Bench version"), stat("Jul 2026", "Snapshot month")],
  path: "/archive/coding-agents-v0.3/",
};

/** The facts one core card shows: its path, copy and three numbers taken from the publication. */
export function coreFacts(key, publication) {
  const page = CORE_PAGES.find((candidate) => candidate.key === key);
  if (page === undefined) {
    throw new Error(`no core card for ${key}`);
  }
  return {
    path: page.path,
    kicker: page.kicker,
    headline: page.headline,
    description: page.description,
    stats: page.stats(publication),
  };
}

/** The facts one model card shows: its name and developer, rank pills, evidence grade and three numbers. */
export function modelFacts(model) {
  return {
    slug: model.slug,
    name: model.name,
    developer: model.developer,
    path: `/models/${model.slug}/`,
    grade: model.grade,
    pills: [rankPill("Plan", model.rank.plan), rankPill("API", model.rank.api)],
    stats: [
      stat(formatScore(model.overall.plan), "Plan overall"),
      stat(formatScore(model.overall.api), "API overall"),
      stat(formatScore(model.quality), "Quality"),
    ],
  };
}

function renderCardDocument(frame) {
  return `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>ValueRank share card</title><style>${SHARED_CSS}</style></head><body>${frame}</body></html>`;
}

function header(version) {
  return `<div class="top"><div class="wordmark">ValueRank</div><div class="version">${escapeHtml(version)}</div></div>`;
}

function footer(path) {
  return `<div class="footer"><span>valuerank.alolabs.dev${escapeHtml(path)}</span><span>Open source · Independent</span></div>`;
}

function statHtml({ value, label }) {
  const size = value.length > 10 ? " long" : "";
  return `<div class="stat"><div class="stat-value${size}">${escapeHtml(value)}</div><div class="stat-label">${escapeHtml(label)}</div></div>`;
}

/** The HTML document for one core page card. */
export function renderCoreCard(facts, version) {
  return renderCardDocument(`<div class="frame">${header(version)}
    <div class="kicker">${escapeHtml(facts.kicker)}</div>
    <h1 class="headline">${escapeHtml(facts.headline)}</h1>
    <p class="description">${escapeHtml(facts.description)}</p>
    <div class="stats">${facts.stats.map(statHtml).join("")}</div>
    ${footer(facts.path)}
  </div>`);
}

/** The HTML document for one roster model card. */
export function renderModelCard(facts, version) {
  const pills = facts.pills.map((text) => `<span class="pill rank">${escapeHtml(text)}</span>`);
  pills.push(`<span class="pill grade ${gradeClass(facts.grade)}">Evidence: ${escapeHtml(facts.grade)}</span>`);
  return renderCardDocument(`<div class="frame">${header(version)}
    <div class="kicker">${escapeHtml(facts.developer)}</div>
    <h1 class="headline">${escapeHtml(facts.name)}</h1>
    <div class="pills">${pills.join("")}</div>
    <div class="stats">${facts.stats.map(statHtml).join("")}</div>
    ${footer(facts.path)}
  </div>`);
}

/** The HTML document for the archived coding-agents v0.3 card. */
export function renderArchiveCard(version) {
  const pills = ARCHIVE.pills.map((text) => `<span class="pill">${escapeHtml(text)}</span>`).join("");
  return renderCardDocument(`<div class="frame">${header(version)}
    <div class="kicker">${escapeHtml(ARCHIVE.kicker)}</div>
    <h1 class="headline">${escapeHtml(ARCHIVE.headline)}</h1>
    <p class="description">${escapeHtml(ARCHIVE.description)}</p>
    <div class="pills">${pills}</div>
    <div class="stats">${ARCHIVE.stats.map(statHtml).join("")}</div>
    ${footer(ARCHIVE.path)}
  </div>`);
}

/** The card set for a repository root, in build order: core pages, roster models, then the archive. */
export function buildCards(root, publication) {
  const version = publication.rankings.version;
  const core = CORE_PAGES.map(({ key }) => ({
    id: key,
    out: join(root, ...SITE_OG, `${key}.png`),
    html: renderCoreCard(coreFacts(key, publication), version),
  }));
  const models = publication.rankings.models.map((model) => ({
    id: `model-${model.slug}`,
    out: join(root, ...SITE_OG, "models", `${model.slug}.png`),
    html: renderModelCard(modelFacts(model), version),
  }));
  const archive = { id: "archive", out: join(root, ...SITE_OG, "archive.png"), html: renderArchiveCard(version) };
  return [...core, ...models, archive];
}

function countFiles(dir, extension) {
  let count = 0;
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      count += countFiles(join(dir, entry.name), extension);
    } else if (entry.name.endsWith(extension)) {
      count += 1;
    }
  }
  return count;
}

/** Reads the public documents the cards are drawn from. Throws when one of them is missing. */
export function readPublication(root) {
  const dataDir = join(root, "site", "data");
  const readJson = (...parts) => JSON.parse(readFileSync(join(dataDir, ...parts), "utf8"));
  return {
    rankings: readJson("rankings.json"),
    plans: readJson("plans.json"),
    changelog: readJson("changelog.json"),
    benchmarks: readJson("benchmarks.json"),
    tb4: readJson("benchmarks", "terminal-bench-4.json"),
    dataFileCount: countFiles(dataDir, ".json"),
  };
}

/**
 * Reads the publication, writes each card's HTML into <root>/.tmp/og and screenshots it into site/og.
 * The data is read before the browser starts, so a missing document never launches Chromium.
 * The browser is closed even when a page fails.
 */
export async function run({ root = ROOT, chromium, log = console.log, publication }) {
  const cards = buildCards(root, publication ?? readPublication(root));
  const browser = await chromium.launch({ headless: true });
  try {
    const workDir = join(root, ".tmp", "og");
    mkdirSync(workDir, { recursive: true });
    for (const card of cards) {
      const htmlPath = join(workDir, `${card.id}.html`);
      writeFileSync(htmlPath, card.html);
      const page = await browser.newPage({
        viewport: VIEWPORT,
        deviceScaleFactor: 1,
      });
      await page.goto(`file://${htmlPath}`, { waitUntil: "networkidle" });
      await page.waitForTimeout(SETTLE_MS);
      mkdirSync(dirname(card.out), { recursive: true });
      await page.screenshot({ path: card.out, type: "png" });
      await page.close();
      log(`wrote ${card.out}`);
    }
  } finally {
    await browser.close();
  }
}

async function loadChromium() {
  const { chromium } = await import("playwright");
  return chromium;
}

/** CLI entry: uses the real Playwright browser and reports failures with exit status 1. */
export async function main({ chromium, exit = process.exit, error = console.error, ...options } = {}) {
  try {
    await run({ ...options, chromium: chromium ?? (await loadChromium()) });
  } catch (failure) {
    error(failure);
    exit(1);
  }
}

/** True when argvPath names the file that is executing (symlinks resolved). */
export function isEntryPoint(argvPath, moduleUrl) {
  if (!argvPath) {
    return false;
  }
  try {
    return realpathSync(argvPath) === fileURLToPath(moduleUrl);
  } catch {
    return false;
  }
}

if (isEntryPoint(process.argv[1], import.meta.url)) {
  main();
}
