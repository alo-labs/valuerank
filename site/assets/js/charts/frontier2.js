// Cost impact: every model at its API and Plan position, joined by a connector.
import { baseLayout, costText, emptySpec, finite, makeSpec, nameOf, pick, renderSpec, resolveOptions } from './common.js';
import { axisWith, developerColor } from './theme.js';

export function buildFrontier2(models, options) {
  const opts = resolveOptions(options);
  const rows = (models ?? []).filter((m) => ['api', 'plan'].every((b) => finite(pick(m.overall, b)) && finite(pick(m.costDims, b))));
  const label = `Dumbbell chart of overall score at API ranking and Plan ranking against cost score for ${rows.length} models.`;
  if (!rows.length) return emptySpec(opts, label, 'No models with both an API and a Plan score are available.');

  const at = (m, b) => ({ x: pick(m.costDims, b), y: pick(m.overall, b) });
  const change = (m) => at(m, 'plan').y - at(m, 'api').y;
  const connectors = rows.map((m) => ({
    x: [at(m, 'api').x, at(m, 'plan').x], y: [at(m, 'api').y, at(m, 'plan').y], mode: 'lines', showlegend: false, hoverinfo: 'skip',
    line: { color: change(m) > 0 ? 'rgba(34,197,94,0.4)' : 'rgba(239,68,68,0.4)', width: 1.5 },
  }));
  const markers = (b, name, symbol, line) => ({
    x: rows.map((m) => at(m, b).x), y: rows.map((m) => at(m, b).y), mode: 'markers', name,
    marker: { size: 10, color: rows.map((m) => developerColor(m.developer)), symbol, opacity: 0.8, line },
    hovertemplate: rows.map((m) => `<b>${m.name}</b><br>${name} overall: ${at(m, b).y}<br>${name} cost score: ${at(m, b).x.toFixed(1)}<br>${costText(m, b)}${b === 'plan' ? `<br>Change: ${change(m) > 0 ? '+' : ''}${change(m).toFixed(1)}` : ''}<extra></extra>`),
  });
  const traces = [
    ...connectors,
    markers('api', 'API ranking', 'circle', { color: 'rgba(255,255,255,0.3)', width: 1 }),
    markers('plan', 'Plan ranking', 'diamond', { color: 'rgba(255,255,255,0.5)', width: 1.5 }),
  ];
  const scores = rows.flatMap((m) => [at(m, 'api').y, at(m, 'plan').y]);
  const base = baseLayout(opts, 'Cost impact: API ranking (○) vs Plan ranking (◆), lines show the change per model', 13);
  const layout = {
    ...base,
    // Cheaper to the left, dearer to the right, as on AA's cost charts.
    xaxis: axisWith(base.xaxis, 'Cost score (cheaper ← · → dearer; 100 = cheapest)', { range: [105, 0] }),
    yaxis: axisWith(base.yaxis, 'Overall score (0–100)', { range: [Math.max(0, Math.floor(Math.min(...scores) - 5)), Math.min(100, Math.ceil(Math.max(...scores) + 5))] }),
    legend: { orientation: 'h', y: -0.15 },
    annotations: [],
  };
  const up = rows.filter((m) => change(m) > 0).length;
  const down = rows.filter((m) => change(m) < 0).length;
  return makeSpec(opts, {
    traces, layout, label,
    summary: `Plan score is higher than API score for ${up} models and lower for ${down}, out of ${rows.length}.`,
    labels: {
      points: rows.map((m) => ({ id: m.slug, label: nameOf(m), x: at(m, 'plan').x, y: at(m, 'plan').y })),
      options: { fontSize: 9, markerRadius: 12, safety: 1.12 }, dark: opts.tokens.dark, base: layout.annotations,
    },
  });
}

export const renderFrontier2 = (container, data, options, plotly) => renderSpec(container, buildFrontier2(data, options), options, plotly);
