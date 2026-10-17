// Loaded with `--import` into child processes. Every import or require of the
// `playwright` package resolves to the recording fake instead of the real
// browser automation library, so child runs never start a browser.
import { registerHooks } from 'node:module';

const FAKE_PLAYWRIGHT = new URL('./fake-playwright.cjs', import.meta.url).href;

registerHooks({
  resolve(specifier, context, nextResolve) {
    if (specifier === 'playwright') {
      return { url: FAKE_PLAYWRIGHT, format: 'commonjs', shortCircuit: true };
    }
    return nextResolve(specifier, context);
  },
});
