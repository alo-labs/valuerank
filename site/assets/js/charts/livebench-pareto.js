// LiveBench overall score against cost per successful task (log x axis).
import { baseLayout, emptySpec, finite, makeSpec, renderSpec, resolveOptions } from './common.js';
import { DOMINATED_COLOR, FRONTIER_COLOR, axisWith, frontierRing } from './theme.js';

export function buildLivebenchPareto(data, options) {
  const opts = resolveOptions(options);
  const rows = (data ?? []).filter((m) => finite(m.overallScore) && finite(m.costPerSuccessfulTaskUsd));
  const label = `Scatter chart of LiveBench overall score against cost per successful task for ${rows.length} models.`;
  if (!rows.length) return emptySpec(opts, label, 'No matched LiveBench rows are available.');

  const cost = (m) => m.costPerSuccessfulTaskUsd;
  const frontier = rows.filter((m) => m.pareto).sort((a, b) => cost(a) - cost(b));
  const dominated = rows.filter((m) => !m.pareto);
  const custom = (m) => [m.name, m.livebenchModel, m.instructionFollowingScore, cost(m)];
  const hover = '<b>%{customdata[0]}</b><br>Overall Score: %{y:.2f}<br>Instruction Following: %{customdata[2]:.2f}<br>Cost Per Successful Task: $%{customdata[3]:.4f}<br>LiveBench variant: %{customdata[1]}';
  const traces = [
    { x: dominated.map(cost), y: dominated.map((m) => m.overallScore), mode: 'markers', type: 'scatter', name: 'Dominated', marker: { size: 11, color: DOMINATED_COLOR, opacity: 0.65 }, customdata: dominated.map(custom), hovertemplate: `${hover}<extra></extra>` },
    { x: frontier.map(cost), y: frontier.map((m) => m.overallScore), mode: 'markers', type: 'scatter', name: 'Pareto frontier', marker: { size: 14, color: FRONTIER_COLOR, line: { width: 2, color: frontierRing(opts.tokens) } }, customdata: frontier.map(custom), hovertemplate: `${hover}<extra>Frontier</extra>` },
    { x: frontier.map(cost), y: frontier.map((m) => m.overallScore), mode: 'lines', type: 'scatter', name: 'frontier-curve', line: { shape: 'spline', dash: 'dot', color: '#94a3b8', width: 2 }, hoverinfo: 'skip', showlegend: false },
  ];
  const scores = rows.map((m) => m.overallScore);
  const base = baseLayout(opts, 'LiveBench overall score vs cost per successful task');
  const layout = {
    ...base,
    xaxis: axisWith(base.xaxis, 'Cost per successful task (USD, log scale)', { type: 'log', tickprefix: '$', tickformat: ',.2f' }),
    yaxis: axisWith(base.yaxis, 'Overall score', { range: [Math.max(0, Math.floor(Math.min(...scores) - 2)), Math.min(100, Math.ceil(Math.max(...scores) + 2))], autorange: false }),
    legend: { orientation: 'h', y: -0.18 },
    margin: { ...base.margin, r: 72, b: 96 },
  };
  return makeSpec(opts, {
    traces, layout, label,
    summary: `LiveBench overall score against cost per successful task for ${rows.length} models. Frontier: ${frontier.map((m) => m.name).join(', ')}.`,
    labels: {
      points: rows.map((m) => ({ id: m.id, label: m.name, x: cost(m), y: m.overallScore, frontier: Boolean(m.pareto) })),
      options: { fontSize: 9, markerRadius: 11, safety: 1.12 }, dark: opts.tokens.dark,
    },
  });
}

export const renderLivebenchPareto = (container, data, options, plotly) => renderSpec(container, buildLivebenchPareto(data, options), options, plotly);
