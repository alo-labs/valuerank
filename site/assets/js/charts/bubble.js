// Speed x quality x cost bubble chart (bubble area follows how costly a model is).
import { baseLayout, costText, emptySpec, finite, makeSpec, nameOf, pick, renderSpec, resolveOptions } from './common.js';
import { axisWith, tierColor } from './theme.js';

export function buildBubble(models, options) {
  const opts = resolveOptions(options);
  const { basis, costLabel, tokens } = opts;
  const rows = (models ?? []).filter((m) => finite(m.speed) && finite(m.quality) && finite(pick(m.costDims, basis)));
  const label = `Bubble chart of speed percentile against quality for ${rows.length} models; bubble size shows ${costLabel}.`;
  if (!rows.length) return emptySpec(opts, label, 'No numeric speed values are available for this cohort.');

  const speeds = rows.map((m) => m.speed);
  const minSpeed = Math.min(...speeds);
  const maxSpeed = Math.max(...speeds);
  const percentile = (m) => ((m.speed - minSpeed) / (maxSpeed - minSpeed || 1)) * 100;
  const costliness = (m) => 100 - pick(m.costDims, basis);
  const maxCost = Math.max(...rows.map(costliness)) || 1;
  const traces = rows.map((m) => ({
    x: [percentile(m)], y: [m.quality], mode: 'markers', name: nameOf(m), showlegend: false,
    marker: { size: 10 + (costliness(m) / maxCost) * 30, color: tierColor(m.tier), opacity: 0.8, line: { color: 'rgba(255,255,255,0.15)', width: 1 } },
    hovertemplate: `<b>${m.name}</b><br>Speed: ${m.speed.toFixed(1)} tok/s<br>Speed percentile score: ${percentile(m).toFixed(1)}<br>Quality: ${m.quality.toFixed(1)}<br>${costLabel}: ${pick(m.costDims, basis).toFixed(1)}<br>${costText(m, basis)}<extra></extra>`,
  }));
  const qualities = rows.map((m) => m.quality);
  const yMin = Math.max(0, Math.floor(Math.min(...qualities) - 5));
  const yMax = Math.min(100, Math.ceil(Math.max(...qualities) + 5));
  const mid = (yMin + yMax) / 2;
  const note = (x, y, text, color) => ({ x, y, xref: 'x', yref: 'y', text, font: { color, size: 9 }, showarrow: false });
  const base = baseLayout(opts, `Speed × quality × ${costLabel} (numeric AA speed only)`);
  const layout = {
    ...base,
    xaxis: axisWith(base.xaxis, `Speed percentile (${minSpeed.toFixed(1)}–${maxSpeed.toFixed(1)} tok/s)`, { range: [-5, 105] }),
    yaxis: axisWith(base.yaxis, 'Quality sub-score', { range: [yMin, yMax] }),
    shapes: [
      { type: 'line', x0: 50, x1: 50, y0: yMin, y1: yMax, line: { color: tokens.dim, dash: 'dot', width: 1.5 } },
      { type: 'line', x0: -5, x1: 105, y0: mid, y1: mid, line: { color: tokens.dim, dash: 'dot', width: 1.5 } },
    ],
    annotations: [
      note(25, yMax - 1, 'Slow, high quality', '#6b7280'),
      note(80, yMax - 1, '<b>Production sweet spot</b>', '#22c55e'),
      note(80, yMin + 1, 'Fast and cheap', '#6b7280'),
      note(25, yMin + 1, 'Avoid', '#6b7280'),
    ],
  };
  const fastest = rows.reduce((best, m) => (m.speed > best.speed ? m : best));
  return makeSpec(opts, {
    traces, layout, label,
    summary: `Speed percentile against quality for ${rows.length} models, bubble size by ${costLabel}. Fastest: ${nameOf(fastest)} at ${fastest.speed.toFixed(1)} tok/s.`,
    labels: {
      points: rows.map((m) => ({ id: m.slug, label: nameOf(m), x: percentile(m), y: m.quality })),
      options: { fontSize: 9, markerRadius: 24, safety: 1.12 }, dark: tokens.dark, base: layout.annotations,
    },
  });
}

export const renderBubble = (container, data, options, plotly) => renderSpec(container, buildBubble(data, options), options, plotly);
