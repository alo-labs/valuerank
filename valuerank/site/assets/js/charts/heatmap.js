// Dimension heatmap (models x dimensions); also the data-section variant via options.height.
import { baseLayout, emptySpec, finite, makeSpec, nameOf, pick, renderSpec, resolveOptions } from './common.js';
import { CATEGORY_COLORS, axisWith } from './theme.js';

const COLORSCALE = [[0, '#1e3a8a'], [0.15, '#2563eb'], [0.35, '#93c5fd'], [0.5, '#cbd5e1'], [0.65, '#fcd34d'], [0.85, '#f59e0b'], [1, '#b45309']];
const COST_KEY = 'costComposite';

export function buildHeatmap(models, options) {
  const opts = resolveOptions(options);
  const { basis, costLabel, tokens } = opts;
  const rows = (models ?? []).filter((m) => finite(pick(m.overall, basis))).sort((a, b) => pick(b.overall, basis) - pick(a.overall, basis));
  const columns = [
    { label: costLabel, full: opts.dimensions.find((d) => d.key === COST_KEY)?.fullLabel ?? costLabel, category: 'cost', weight: opts.costWeightPct ?? opts.dimensions.find((d) => d.key === COST_KEY)?.weightPct ?? 0, value: (m) => pick(m.costDims, basis) },
    ...opts.dimensions.filter((d) => d.key !== COST_KEY).map((d) => ({ label: d.label, full: d.fullLabel ?? d.label, category: d.category, weight: d.weightPct, value: (m) => m.dims?.[d.key] ?? null })),
  ];
  const labelText = `Heatmap of normalised scores for ${rows.length} models across ${columns.length} dimensions, ${opts.basisLabel}.`;
  if (!rows.length) return emptySpec(opts, labelText, 'No ranked models are available.');

  const x = columns.map((c) => c.label);
  const y = rows.map(nameOf);
  const z = rows.map((m) => columns.map((c) => (finite(c.value(m)) ? c.value(m) : null)));
  const missingCount = z.flat().filter((v) => v === null).length;
  const underlay = {
    type: 'heatmap', z: z.map((r) => r.map(() => 0)), x, y, zmin: 0, zmax: 1, showscale: false, hoverinfo: 'skip',
    colorscale: [[0, tokens.missing], [1, tokens.missing]],
  };
  const data = {
    type: 'heatmap', z, x, y, colorscale: COLORSCALE, zmin: 0, zmax: 100, hoverongaps: false,
    customdata: rows.map((m, r) => columns.map((c, k) => ({
      model: m.name, dim: c.full, score: z[r][k] === null ? 'Not available' : z[r][k].toFixed(1), weight: c.weight.toFixed(2), missing: z[r][k] === null,
    }))),
    hovertemplate: '<b>%{customdata.model}</b> — %{customdata.dim}<br>Score: %{customdata.score}<br>Dimension weight: %{customdata.weight}%<extra></extra>',
    showscale: true, colorbar: { title: { text: 'Score' }, thickness: 12, len: 0.8, tickfont: { color: '#94a3b8', size: 10 } },
  };
  const shapes = [];
  const groups = [];
  columns.forEach((c, i) => {
    if (i > 0 && columns[i - 1].category !== c.category) shapes.push({ type: 'line', xref: 'x', yref: 'paper', x0: i - 0.5, x1: i - 0.5, y0: 0, y1: 1, line: { color: tokens.grid, width: 2 } });
    if (groups.length && groups[groups.length - 1].key === c.category) groups[groups.length - 1].end = i;
    else groups.push({ key: c.category, start: i, end: i });
  });
  const groupNotes = groups.map((g) => ({
    x: (g.start + g.end) / 2, y: -0.08, xref: 'x', yref: 'paper', text: `<b>${opts.categories[g.key] ?? g.key}</b>`,
    font: { color: CATEGORY_COLORS[g.key] ?? '#94a3b8', size: 10 }, showarrow: false,
  }));
  const cellNotes = rows.flatMap((m, r) => columns.map((c, k) => {
    const value = z[r][k];
    const color = value === null ? 'rgba(148,163,184,0.9)' : value < 28 ? 'rgba(255,255,255,0.9)' : 'rgba(0,0,0,0.72)';
    return { x: c.label, y: nameOf(m), xref: 'x', yref: 'y', text: value === null ? '⊘' : value.toFixed(0), showarrow: false, font: { size: 9, color, family: 'IBM Plex Mono, monospace' } };
  }));
  const base = baseLayout(opts, `Normalised score matrix (${rows.length} models × ${columns.length} dimensions)`);
  const height = Number(opts.height);
  const layout = {
    ...base,
    xaxis: axisWith(base.xaxis, '', { side: 'top', tickangle: -30, tickfont: { ...base.xaxis.tickfont, size: 10 } }),
    yaxis: axisWith(base.yaxis, '', { autorange: 'reversed', tickfont: { ...base.yaxis.tickfont, size: 11 } }),
    margin: { t: 100, r: 80, b: 100, l: 90 },
    shapes, annotations: [...groupNotes, ...cellNotes],
    height: Number.isFinite(height) ? height : undefined,
  };
  return makeSpec(opts, {
    traces: [underlay, data], layout, label: labelText,
    summary: `Normalised scores (0–100) for ${rows.length} models across ${columns.length} dimensions. ${missingCount ? `Cells without data: ${missingCount}.` : 'Every cell has a value.'}`,
  });
}

export const renderHeatmap = (container, data, options, plotly) => renderSpec(container, buildHeatmap(data, options), options, plotly);
