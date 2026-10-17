'use strict';

// Test double for the `playwright` package. Every call is recorded so tests can
// assert on browser-driving behaviour without launching a real browser.
//
// In-process tests call createFakeChromium() directly. Child-process tests load
// this module through install-fake-playwright.mjs, which configures the scenario
// and call log from environment variables set by run-script.mjs.

const fs = require('node:fs');
const { fileURLToPath } = require('node:url');
const { buildFakeDocument, buildFakeLocation, withGlobals } = require('./fake-dom.cjs');

const PNG_SIGNATURE = Buffer.from('89504e470d0a1a0a', 'hex');

function createFakeChromium({ scenario = {}, record = () => {} } = {}) {
  function createPage() {
    return {
      setDefaultTimeout(timeout) {
        record({ call: 'page.setDefaultTimeout', timeout });
      },
      async goto(url, options) {
        record({ call: 'page.goto', url, options });
        if (scenario.gotoError) {
          throw new Error(scenario.gotoError);
        }
        if (url.startsWith('file://')) {
          // A browser cannot load a missing local file, so fail the same way.
          fs.accessSync(fileURLToPath(url));
        }
      },
      async waitForTimeout(ms) {
        record({ call: 'page.waitForTimeout', ms });
      },
      async evaluate(pageFunction, arg) {
        record({ call: 'page.evaluate' });
        const value = withGlobals(
          { document: buildFakeDocument(scenario.page), location: buildFakeLocation(scenario.page) },
          () => pageFunction(arg),
        );
        // Playwright returns page results as serialized data; mirror that.
        return JSON.parse(JSON.stringify(value));
      },
      async screenshot({ path, type }) {
        record({ call: 'page.screenshot', path, type });
        if (scenario.screenshotError) {
          throw new Error(scenario.screenshotError);
        }
        fs.writeFileSync(path, PNG_SIGNATURE);
      },
      async close() {
        record({ call: 'page.close' });
      },
    };
  }

  return {
    async launch(options) {
      record({ call: 'chromium.launch', options });
      if (scenario.launchError) {
        throw new Error(scenario.launchError);
      }
      return {
        async newPage(options) {
          record({ call: 'browser.newPage', options });
          return createPage();
        },
        async close() {
          record({ call: 'browser.close' });
        },
      };
    },
  };
}

function appendCallRecord(logPath) {
  return (entry) => {
    if (logPath) {
      fs.appendFileSync(logPath, `${JSON.stringify(entry)}\n`);
    }
  };
}

function scenarioFromEnvironment() {
  const scenarioPath = process.env.FAKE_PLAYWRIGHT_SCENARIO_FILE;
  return scenarioPath ? JSON.parse(fs.readFileSync(scenarioPath, 'utf8')) : {};
}

exports.createFakeChromium = createFakeChromium;
exports.chromium = createFakeChromium({
  scenario: scenarioFromEnvironment(),
  record: appendCallRecord(process.env.FAKE_PLAYWRIGHT_LOG),
});
