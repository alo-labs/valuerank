#!/usr/bin/env node
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const outDir = path.join(__dirname, 'screenshots');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  for (const [name, url] of [
    ['main', 'http://127.0.0.1:8765/'],
    ['coding-agents', 'http://127.0.0.1:8765/coding-agents/'],
    ['tb21', 'http://127.0.0.1:8765/tb21/'],
  ]) {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    await page.waitForTimeout(1500);
    const shot = path.join(outDir, `${name}-1280.png`);
    await page.screenshot({ path: shot, fullPage: false });
    const text = await page.evaluate(() => document.body.innerText.slice(0, 500));
    console.log(name, 'shot', shot, 'head', JSON.stringify(text.slice(0, 200)));
  }
  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
