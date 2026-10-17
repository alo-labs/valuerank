// Rank displacement between the quality-only rank and the overall rank on the active basis.
import { baseLayout, emptySpec, finite, makeSpec, nameOf, pick, renderSpec, resolveOptions, weightSuffix } from './common.js';
import { axisWith } from './theme.js';

const UP = '#22c55e';
const DOWN = '#ef4444';
const SAME = '#64748b';
const places = (n) => `${n} place${n === 1 ? '' : 's'}`;

export function buildDisplacement(models, options) {
  const opts = resolveOptions(options);
  const { basis, costLabel, tokens } = opts;
  const rows = (models ?? [])
    .filter((m) => finite(pick(m.rank, basis)) && finite(m.qualityRank) && finite(pick(m.overall, basis)))
    .sort((a, b) => pick(a.overall, basis) - pick(b.overall, basis));
  const label = `Bar chart of rank displacement for ${rows.length} models, ${opts.basisLabel}.`;
  if (!rows.length) return emptySpec(opts, label, 'No ranked models are available.');

  const disp = rows.map((m) => m.qualityRank - pick(m.rank, basis));
  const wording = (d) => (d > 0 ? `Cost bonus: rises ${places(d)}` : d < 0 ? `Cost penalty: falls ${places(-d)}` : 'No change');
  const trace = {
    y: rows.map(nameOf), x: disp, type: 'bar', orientation: 'h',
    marker: { color: disp.map((d) => (d > 0 ? UP : d < 0 ? DOWN : SAME)), opacity: 0.85 },
    text: disp.map((d) => (d > 0 ? `+${d}` : `${d}`)), textposition: 'outside', textfont: { size: 11, color: '#94a3b8' },
    hovertemplate: rows.map((m, i) => `<b>${m.name}</b><br>Quality rank: #${m.qualityRank}<br>Overall rank: #${pick(m.rank, basis)}<br>${wording(disp[i])}<extra></extra>`),
  };
  const base = baseLayout(opts, `Rank displacement: quality rank vs ${opts.basisLabel}${weightSuffix(opts)}`);
  const layout = {
    ...base,
    xaxis: axisWith(base.xaxis, `Places gained (right) or lost (left) once ${costLabel} is weighted`, {
      zeroline: true, zerolinecolor: tokens.dim, zerolinewidth: 2, range: [Math.min(-3, Math.min(...disp) - 1.5), Math.max(3, Math.max(...disp) + 1.5)],
    }),
    yaxis: axisWith(base.yaxis, ''),
    margin: { ...base.margin, l: 90, b: 80 },
    shapes: [{ type: 'line', x0: 0, x1: 0, y0: -0.5, y1: rows.length - 0.5, line: { color: tokens.dim, width: 2, dash: 'dot' } }],
    annotations: [
      { xref: 'paper', x: 0.98, xanchor: 'right', yref: 'paper', y: 1.02, text: 'Cost bonus (rose) →', font: { color: UP, size: 10 }, showarrow: false },
      { xref: 'paper', x: 0.02, xanchor: 'left', yref: 'paper', y: 1.02, text: '← Cost penalty (fell)', font: { color: DOWN, size: 10 }, showarrow: false },
    ],
  };
  const rises = disp.filter((d) => d > 0).length;
  const falls = disp.filter((d) => d < 0).length;
  return makeSpec(opts, {
    traces: [trace], layout, label,
    summary: `Cost weight lifts ${rises} and lowers ${falls} of ${rows.length} models relative to their quality-only rank on the ${opts.basisLabel}.`,
  });
}

export const renderDisplacement = (container, data, options, plotly) => renderSpec(container, buildDisplacement(data, options), options, plotly);
