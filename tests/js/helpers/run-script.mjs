import { spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HELPERS = dirname(fileURLToPath(import.meta.url));

export const REPO_ROOT = join(HELPERS, '..', '..', '..');

const PRELOAD_URL = pathToFileURL(join(HELPERS, 'install-fake-playwright.mjs')).href;

// Runs a repository script in a child Node process whose `playwright` import is
// the recording fake. The child inherits NODE_V8_COVERAGE, so its coverage is
// merged into the test-runner report. PLAYWRIGHT_BROWSERS_PATH points at an
// empty directory, so even if the fake were bypassed a real launch would fail
// instead of starting a browser.
export function runScriptWithFakePlaywright({ script, args = [], scenario = {} }) {
  const workdir = mkdtempSync(join(tmpdir(), 'valuerank-js-child-'));
  const scenarioFile = join(workdir, 'scenario.json');
  const logFile = join(workdir, 'calls.jsonl');
  writeFileSync(scenarioFile, JSON.stringify(scenario));
  try {
    const result = spawnSync(process.execPath, [script, ...args], {
      cwd: REPO_ROOT,
      encoding: 'utf8',
      env: {
        ...process.env,
        NODE_OPTIONS: [process.env.NODE_OPTIONS, `--import="${PRELOAD_URL}"`].filter(Boolean).join(' '),
        PLAYWRIGHT_BROWSERS_PATH: join(workdir, 'no-browsers'),
        FAKE_PLAYWRIGHT_SCENARIO_FILE: scenarioFile,
        FAKE_PLAYWRIGHT_LOG: logFile,
      },
    });
    const calls = existsSync(logFile)
      ? readFileSync(logFile, 'utf8').split('\n').filter(Boolean).map((line) => JSON.parse(line))
      : [];
    return { status: result.status, signal: result.signal, stdout: result.stdout, stderr: result.stderr, calls };
  } finally {
    rmSync(workdir, { recursive: true, force: true });
  }
}

export function makeTempDir(prefix) {
  return mkdtempSync(join(tmpdir(), prefix));
}
