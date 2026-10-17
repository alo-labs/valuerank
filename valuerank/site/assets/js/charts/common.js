// Helpers shared by the chart modules: option resolution, accessible summaries
// and the thin render pipeline (plot, then place collision-safe labels).
import { themeTokens, plotlyLayout, plotlyTitle, PLOTLY_CONFIG } from './theme.js';
import { buildCollisionSafeLabelAnnotations, createRepairIO, readGeometry, repairCollisionSafeLabelAnnotations } from './labels.js';

export const finite = (value) => typeof value === 'number' && Number.isFinite(value);

/** A per-basis object ({api, plan}) or a plain value, read for `basis`. */
export const pick = (value, basis) => (value !== null && typeof value === 'object' ? (value[basis] ?? null) : (value ?? null));

const DEFAULT_COST_LABELS = { api: 'API cost', plan: 'Plan cost' };

export function resolveOptions(options = {}) {
  const basis = options.basis === 'api' ? 'api' : 'plan';
  const dark = Boolean(options.dark);
  return {
    ...options,
    basis,
    dark,
    costLabel: options.costLabel ?? options.bases?.[basis]?.costLabel ?? DEFAULT_COST_LABELS[basis],
    basisLabel: options.bases?.[basis]?.label ?? `${basis === 'api' ? 'API' : 'Plan'} ranking`,
    tokens: options.tokens ?? themeTokens({ dark }),
    dimensions: options.dimensions ?? [],
    categories: options.categories ?? {},
  };
}

export const money = (value, digits = 2) => (finite(value) ? `$${value.toLocaleString('en-US', { minimumFractionDigits: digits, maximumFractionDigits: digits })}` : '—');

/** One-line cost description in the unit of the active basis. */
export function costText(model, basis) {
  const cost = model.cost ?? {};
  return basis === 'api' ? `${money(cost.apiUsd, 0)} per Index run` : `${money(cost.planUsdPerPoint, 3)} per Index point`;
}

export const baseLayout = (opts, title, titleSize) => ({
  ...plotlyLayout(opts.tokens),
  title: { text: title, font: plotlyTitle(opts.tokens, titleSize) },
});

export function makeSpec(opts, { traces, layout, label, summary, labels, empty }) {
  return { traces, layout, config: PLOTLY_CONFIG, label, summary, labels, empty };
}

export const emptySpec = (opts, label, message) => makeSpec(opts, { traces: [], layout: {}, label, summary: message, empty: message });

export function announce(container, spec) {
  container.setAttribute('role', 'img');
  container.setAttribute('aria-label', spec.label);
  const target = container.parentNode?.querySelector('[data-chart-summary]');
  if (target) target.textContent = spec.summary;
}

export const defaultRaf = (callback) => setTimeout(callback, 0);

/** Plot the spec, then place and repair labels when the spec asks for them. */
export async function renderSpec(container, spec, options, plotly) {
  announce(container, spec);
  if (spec.empty) {
    container.textContent = spec.empty;
    return false;
  }
  await plotly.newPlot(container, spec.traces, spec.layout, spec.config);
  if (!spec.labels) return true;
  const geometry = readGeometry(container, { dark: spec.labels.dark, measureText: options?.measureText });
  if (!geometry) return true;
  const annotations = buildCollisionSafeLabelAnnotations(spec.labels.points, geometry, spec.labels.options);
  const base = spec.labels.base ?? [];
  const relayout = (items) => plotly.relayout(container, { annotations: [...base, ...items] });
  await relayout(annotations);
  const io = createRepairIO(container, annotations, { relayout: () => relayout(annotations), raf: options?.raf ?? defaultRaf });
  await repairCollisionSafeLabelAnnotations(annotations, io, spec.labels.options);
  return true;
}

/** Frontier of points that maximise both `x` and `y` (higher is better on each). */
export function frontierIds(rows, idOf, xOf, yOf, xBetter = 'higher') {
  const sign = xBetter === 'higher' ? -1 : 1;
  const sorted = [...rows].sort((a, b) => sign * (xOf(a) - xOf(b)) || yOf(b) - yOf(a));
  let best = -Infinity;
  const ids = new Set();
  sorted.forEach((row) => {
    if (yOf(row) > best) { ids.add(idOf(row)); best = yOf(row); }
  });
  return ids;
}

export const nameOf = (model) => model.shortName ?? model.name;

/** " (cost weight 18.9%)" when the caller supplies a weight, else nothing. */
export const weightSuffix = (opts) => (finite(opts.costWeightPct) ? ` (cost weight ${Number(opts.costWeightPct.toFixed(1))}%)` : '');
