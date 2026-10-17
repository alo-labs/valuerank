// Terminal-Bench 4.0: resolution rate against total cost with the Pareto frontier (log x axis).
import { emptySpec, finite, frontierIds, makeSpec, renderSpec, resolveOptions } from './common.js';
import { DOMINATED_COLOR, FRONTIER_COLOR, FONT_FAMILY, frontierRing } from './theme.js';

export function buildTb4(data, options) {
  const opts = resolveOptions(options);
  const { tokens } = opts;
  const rows = (data ?? []).filter((r) => finite(r.costUsd) && r.costUsd > 0 && finite(r.resolutionRatePct));
  const label = `Scatter chart of Terminal-Bench 4.0 resolution rate against total cost for ${rows.length} official rows.`;
  if (!rows.length) return emptySpec(opts, label, 'No Terminal-Bench 4.0 rows are available.');

  const ids = frontierIds(rows, (r) => r.model, (r) => r.costUsd, (r) => r.resolutionRatePct, 'lower');
  const frontier = rows.filter((r) => ids.has(r.model)).sort((a, b) => a.costUsd - b.costUsd);
  const dominated = rows.filter((r) => !ids.has(r.model));
  const custom = (r) => [r.baseModel, r.agent, r.resolutionRatePct, r.uncertaintyPct, r.tokens, r.rankLabel, r.model];
  const hover = '<b>%{customdata[0]}</b><br>Resolution: %{customdata[2]:.1f}% ± %{customdata[3]:.1f}%<br>Cost: $%{x:,.0f}<br>Agent: %{customdata[1]}<br>Tokens: %{customdata[4]}<br>Rank: %{customdata[5]}<br>Variant: %{customdata[6]}';
  const traces = [
    { x: dominated.map((r) => r.costUsd), y: dominated.map((r) => r.resolutionRatePct), mode: 'markers', type: 'scatter', name: 'Official rows', marker: { size: 11, color: DOMINATED_COLOR, opacity: 0.65 }, customdata: dominated.map(custom), hovertemplate: `${hover}<extra></extra>` },
    { x: frontier.map((r) => r.costUsd), y: frontier.map((r) => r.resolutionRatePct), mode: 'markers', type: 'scatter', name: 'Pareto frontier', marker: { size: 15, color: FRONTIER_COLOR, line: { width: 2, color: frontierRing(tokens) } }, customdata: frontier.map(custom), hovertemplate: `${hover}<extra>Frontier</extra>` },
    { x: frontier.map((r) => r.costUsd), y: frontier.map((r) => r.resolutionRatePct), mode: 'lines', type: 'scatter', name: 'frontier-curve', line: { shape: 'spline', dash: 'dot', color: '#94a3b8', width: 2 }, hoverinfo: 'skip', showlegend: false },
  ];
  const best = Math.max(...rows.map((r) => r.resolutionRatePct));
  const axis = { gridcolor: tokens.grid, zeroline: false };
  const layout = {
    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)', font: { family: FONT_FAMILY, color: tokens.text },
    margin: { l: 64, r: 24, t: 28, b: 80 }, hovermode: 'closest',
    xaxis: { ...axis, type: 'log', title: { text: 'Total cost (USD, log scale)' }, tickprefix: '$', tickformat: ',.0f' },
    yaxis: { ...axis, title: { text: 'Resolution rate (%)' }, range: [0, Math.max(64, Math.round(best * 1.1))], ticksuffix: '%' },
    legend: { orientation: 'h', y: -0.18 },
  };
  return makeSpec(opts, {
    traces, layout, label,
    summary: `Terminal-Bench 4.0 resolution rate against total cost, ${rows.length} official rows. Frontier: ${frontier.map((r) => r.baseModel).join(', ')}.`,
    labels: {
      points: rows.map((r) => ({ id: r.model, label: r.baseModel, x: r.costUsd, y: r.resolutionRatePct, frontier: ids.has(r.model) })),
      options: { fontSize: 9, markerRadius: 12, safety: 1.12 }, dark: tokens.dark,
    },
  });
}

export const renderTb4 = (container, data, options, plotly) => renderSpec(container, buildTb4(data, options), options, plotly);
