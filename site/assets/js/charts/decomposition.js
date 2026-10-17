// Score decomposition: stacked contribution of each category to a model's overall score.
import { baseLayout, emptySpec, finite, makeSpec, nameOf, pick, renderSpec, resolveOptions, weightSuffix } from './common.js';
import { CATEGORY_COLORS, FALLBACK_COLOR, axisWith } from './theme.js';

const COST_KEY = 'costComposite';

/**
 * Points each category adds to the model's overall score: value x weight over the
 * weights of the dimensions that have a value (the renormalisation rule).
 * When costWeightPct is given the other weights are scaled to fill the rest.
 */
export function contributions(model, dimensions, basis, costWeightPct) {
  const costDim = dimensions.find((d) => d.key === COST_KEY);
  const scale = costWeightPct == null ? 1 : (100 - costWeightPct) / (100 - (costDim?.weightPct ?? 0));
  const totals = Object.fromEntries(dimensions.map((d) => [d.category, 0]));
  const entries = dimensions.map((d) => ({
    category: d.category,
    value: d.key === COST_KEY ? pick(model.costDims, basis) : (model.dims?.[d.key] ?? null),
    weight: d.key === COST_KEY ? (costWeightPct ?? d.weightPct) : d.weightPct * scale,
  })).filter((e) => finite(e.value) && e.weight > 0);
  const available = entries.reduce((sum, e) => sum + e.weight, 0);
  entries.forEach((e) => { totals[e.category] += (e.value * e.weight) / available; });
  return totals;
}

export function buildDecomposition(models, options) {
  const opts = resolveOptions(options);
  const { basis, costLabel } = opts;
  const rows = (models ?? []).filter((m) => finite(pick(m.overall, basis))).sort((a, b) => pick(a.overall, basis) - pick(b.overall, basis));
  const label = `Stacked bar chart of score contribution by category for ${rows.length} models, ${opts.basisLabel}.`;
  if (!rows.length) return emptySpec(opts, label, 'No ranked models are available.');

  const categoryKeys = [...new Set(opts.dimensions.map((d) => d.category))];
  const parts = rows.map((m) => contributions(m, opts.dimensions, basis, opts.costWeightPct));
  const traces = categoryKeys.map((key) => {
    const name = opts.categories[key] ?? key;
    return {
      y: rows.map(nameOf), x: parts.map((p) => Math.round(p[key] * 100) / 100), name, type: 'bar', orientation: 'h',
      marker: { color: CATEGORY_COLORS[key] ?? FALLBACK_COLOR, opacity: 0.9 },
      hovertemplate: `<b>${name}</b>: %{x:.2f} pts<extra>%{y}</extra>`,
    };
  });
  const base = baseLayout(opts, `Score decomposition by category (${costLabel})${weightSuffix(opts)}`);
  const layout = {
    ...base, barmode: 'stack',
    xaxis: axisWith(base.xaxis, 'Score contribution (points)', { range: [0, 100] }),
    yaxis: axisWith(base.yaxis, ''),
    legend: { orientation: 'h', y: -0.16, x: 0, xanchor: 'left', font: { size: 11 } },
    margin: { ...base.margin, l: 90, b: 90 },
  };
  const leader = rows[rows.length - 1];
  return makeSpec(opts, {
    traces, layout, label,
    summary: `${nameOf(leader)} leads with ${pick(leader.overall, basis).toFixed(1)} points on the ${opts.basisLabel}; bars split each score into ${categoryKeys.length} categories.`,
  });
}

export const renderDecomposition = (container, data, options, plotly) => renderSpec(container, buildDecomposition(data, options), options, plotly);
