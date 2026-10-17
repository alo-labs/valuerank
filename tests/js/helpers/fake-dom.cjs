'use strict';

// Minimal DOM stand-in for the leaderboard reader. It implements only the
// selectors and properties that the page-side code reads, so tests can run
// that code in Node with the same inputs Playwright would supply in a page.

const ROW_SELECTOR = 'table tr, [role="row"]';
const CELL_SELECTOR = 'th, td, [role="cell"]';
const ANCHOR_SELECTOR = 'a[href]';
const SCRIPT_SELECTOR = 'script';

function buildElement(spec) {
  return { innerText: spec.innerText, textContent: spec.textContent, href: spec.href };
}

function buildRow(spec) {
  const cells = (spec.cells ?? []).map(buildElement);
  return {
    querySelectorAll: (selector) => (selector === CELL_SELECTOR ? cells : []),
  };
}

function buildFakeDocument(page = {}) {
  const index = {
    [ROW_SELECTOR]: (page.rows ?? []).map(buildRow),
    [ANCHOR_SELECTOR]: (page.anchors ?? []).map(buildElement),
    [SCRIPT_SELECTOR]: (page.scripts ?? []).map(buildElement),
  };
  return {
    title: page.title ?? '',
    body: { innerText: page.bodyText },
    querySelectorAll: (selector) => index[selector] ?? [],
  };
}

function buildFakeLocation(page = {}) {
  return { href: page.finalUrl };
}

// Installs the given globals for the duration of `action`, then restores the
// previous descriptors (or removes the property when it was absent).
function withGlobals(values, action) {
  const saved = Object.keys(values).map((key) => [key, Object.getOwnPropertyDescriptor(globalThis, key)]);
  for (const key of Object.keys(values)) {
    Object.defineProperty(globalThis, key, { value: values[key], configurable: true, writable: true });
  }
  try {
    return action();
  } finally {
    for (const [key, descriptor] of saved) {
      if (descriptor) {
        Object.defineProperty(globalThis, key, descriptor);
      } else {
        delete globalThis[key];
      }
    }
  }
}

module.exports = { buildFakeDocument, buildFakeLocation, withGlobals };
