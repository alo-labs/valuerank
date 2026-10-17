// Serves the generated site/ directory for end-to-end tests and manages one
// Chromium instance per test file. Pages are real; the network is local only.
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const SITE_DIR = resolve(fileURLToPath(new URL('../../../site/', import.meta.url)));

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.xml': 'application/xml; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
};

export async function resolveFile(root, urlPath) {
  const clean = normalize(decodeURIComponent(urlPath.split('?')[0])).replace(/^(\.\.[/\\])+/, '');
  let target = join(root, clean);
  if (!target.startsWith(root)) return null;
  try {
    const info = await stat(target);
    if (info.isDirectory()) target = join(target, 'index.html');
    await stat(target);
    return target;
  } catch {
    return null;
  }
}

export function startServer(root = SITE_DIR) {
  const server = createServer(async (request, response) => {
    const file = await resolveFile(root, request.url ?? '/');
    if (!file) {
      response.writeHead(404, { 'content-type': 'text/plain' });
      response.end('not found');
      return;
    }
    response.writeHead(200, { 'content-type': TYPES[extname(file)] ?? 'application/octet-stream' });
    response.end(await readFile(file));
  });
  return new Promise((resolveStarted) => {
    server.listen(0, '127.0.0.1', () => {
      const { port } = server.address();
      resolveStarted({ server, baseUrl: `http://127.0.0.1:${port}`, close: () => new Promise((done) => server.close(done)) });
    });
  });
}

export async function launchBrowser() {
  const { chromium } = await import('playwright');
  const browser = await chromium.launch({ headless: true });
  return {
    browser,
    newPage: async (options = {}) => {
      const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, ...options });
      // Plotly is served from a CDN; block it so tests never touch the network and stay fast.
      await context.route(/^https?:\/\/(?!127\.0\.0\.1)/, (route) => route.abort());
      const page = await context.newPage();
      const errors = [];
      page.on('pageerror', (error) => errors.push(error));
      // Blocked CDN requests (fonts, Plotly) are intentional in this harness and are not page errors.
      page.on('console', (message) => {
        if (message.type() === 'error' && !/Failed to load resource/.test(message.text())) errors.push(new Error(message.text()));
      });
      return { page, context, errors };
    },
    close: () => browser.close(),
  };
}
