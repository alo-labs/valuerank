// ValueRank Pareto chart: quality against the cost score of the active basis.
import { baseLayout, costText, emptySpec, finite, makeSpec, nameOf, pick, renderSpec, resolveOptions } from './common.js';
import { FRONTIER_COLOR, axisWith, developerColor, frontierRing } from './theme.js';

export function buildPareto(models, options) {
  const opts = resolveOptions(options);
  const { basis, costLabel, tokens } = opts;
  const rows = (models ?? []).filter((m) => finite(m.quality) && finite(pick(m.costDims, basis)) && finite(pick(m.overall, basis)));
  const label = `Scatter chart of quality (vertical) against ${costLabel} score (horizontal) for ${rows.length} models, ${opts.basisLabel}.`;
  if (!rows.length) return emptySpec(opts, label, 'No models with a quality score and a cost score are available.');

  const x = (m) => pick(m.costDims, basis);
  const isFrontier = (m) => Boolean(pick(m.pareto, basis));
  const frontier = rows.filter(isFrontier).sort((a, b) => x(a) - x(b));
  const dominated = rows.filter((m) => !isFrontier(m));
  const custom = (m) => [m.name, pick(m.overall, basis), costText(m, basis)];
  const hover = `<b>%{customdata[0]}</b><br>Quality: %{y:.1f}<br>${costLabel} score: %{x:.1f}<br>Overall: %{customdata[1]}<br>%{customdata[2]}`;
  const traces = [
    {
      x: dominated.map(x), y: dominated.map((m) => m.quality), mode: 'markers', type: 'scatter', name: 'Dominated',
      marker: { size: 11, color: dominated.map((m) => developerColor(m.developer)), opacity: 0.55 },
      customdata: dominated.map(custom), hovertemplate: `${hover}<extra></extra>`, showlegend: true,
    },
    {
      x: frontier.map(x), y: frontier.map((m) => m.quality), mode: 'markers', type: 'scatter', name: 'Pareto frontier',
      marker: { size: 14, color: FRONTIER_COLOR, line: { width: 2, color: frontierRing(tokens) } },
      customdata: frontier.map(custom), hovertemplate: `${hover}<extra>Frontier</extra>`, showlegend: true,
    },
    {
      x: frontier.map(x), y: frontier.map((m) => m.quality), mode: 'lines', type: 'scatter', name: 'frontier-curve',
      line: { shape: 'spline', dash: 'dot', color: '#94a3b8', width: 2 }, hoverinfo: 'skip', showlegend: false,
    },
  ];
  const quality = rows.map((m) => m.quality);
  const base = baseLayout(opts, `ValueRank Pareto frontier: quality vs ${costLabel}`);
  const layout = {
    ...base,
    xaxis: axisWith(base.xaxis, `${costLabel} score (0–100, higher is cheaper)`, { type: 'linear', range: [0, 105], autorange: false, tickvals: [0, 20, 40, 60, 80, 100] }),
    yaxis: axisWith(base.yaxis, 'Quality sub-score (0–100)', { range: [Math.max(0, Math.min(...quality) - 8), Math.min(100, Math.max(...quality) + 8)], autorange: false }),
    annotations: [],
    legend: { orientation: 'h', y: -0.18 },
    margin: { ...base.margin, r: 88, b: 96 },
  };
  const names = frontier.map(nameOf);
  return makeSpec(opts, {
    traces, layout, label,
    summary: `Quality against ${costLabel} score for ${rows.length} models on the ${opts.basisLabel}. ${names.length ? `Pareto frontier: ${names.join(', ')}.` : 'No model is on the frontier.'}`,
    labels: {
      points: rows.map((m) => ({ id: m.slug, label: nameOf(m), x: x(m), y: m.quality, frontier: isFrontier(m) })),
      options: { fontSize: 9, markerRadius: 11, safety: 1.12 }, dark: tokens.dark,
    },
  });
}

export const renderPareto = (container, data, options, plotly) => renderSpec(container, buildPareto(data, options), options, plotly);
