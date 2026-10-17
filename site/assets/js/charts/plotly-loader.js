// Lazy, deduplicated loader for the one pinned Plotly build.
export const PLOTLY_URL = 'https://cdn.plot.ly/plotly-2.27.0.min.js';

const pending = new WeakMap();

/**
 * Resolves with the Plotly global, injecting a single <script> on first use.
 * `documentLike` needs createElement, head.appendChild and defaultView.
 */
export function loadPlotly(documentLike) {
  const win = documentLike.defaultView;
  if (win.Plotly) return Promise.resolve(win.Plotly);
  if (pending.has(documentLike)) return pending.get(documentLike);
  const promise = new Promise((resolve, reject) => {
    const script = documentLike.createElement('script');
    script.src = PLOTLY_URL;
    script.async = true;
    script.onload = () => resolve(win.Plotly);
    script.onerror = () => {
      pending.delete(documentLike);
      reject(new Error(`Could not load ${PLOTLY_URL}`));
    };
    documentLike.head.appendChild(script);
  });
  pending.set(documentLike, promise);
  return promise;
}
