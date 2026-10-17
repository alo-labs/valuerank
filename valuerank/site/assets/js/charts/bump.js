// Version history bump chart: rank by release. Only recorded ranks are drawn; a
// missing version breaks the line instead of being interpolated.
import { baseLayout, emptySpec, finite, makeSpec, nameOf, pick, renderSpec, resolveOptions } from './common.js';
import { axisWith, developerColor } from './theme.js';

/**
 * versions: changelog.versions (newest first). A version may carry `ranks`
 * ({slug: rank}) and/or `rankChanges` ([{slug, from, to}]). The current ranking
 * of the active basis closes the newest version.
 */
export function rankHistory(versions, models, basis) {
  const chronological = [...versions].reverse();
  const labels = chronological.map((v) => v.version);
  const ranks = new Map();
  const series = (slug) => {
    if (!ranks.has(slug)) ranks.set(slug, labels.map(() => null));
    return ranks.get(slug);
  };
  chronological.forEach((v, i) => {
    Object.entries(v.ranks ?? {}).forEach(([slug, rank]) => { series(slug)[i] = rank; });
    (v.rankChanges ?? []).forEach((change) => { series(change.slug)[i] = change.to; });
  });
  chronological.forEach((v, i) => {
    (v.rankChanges ?? []).forEach((change) => {
      if (i > 0 && change.from != null && series(change.slug)[i - 1] === null) series(change.slug)[i - 1] = change.from;
    });
  });
  models.forEach((m) => {
    const rank = pick(m.rank, basis);
    if (finite(rank)) series(m.slug)[labels.length - 1] = rank;
  });
  return { labels, ranks };
}

export function buildBump(data, options) {
  const opts = resolveOptions(options);
  const { basis } = opts;
  const { versions = [], models = [] } = data ?? {};
  const label = `Line chart of model rank across ${versions.length} versions, ${opts.basisLabel}.`;
  if (!versions.length) return emptySpec(opts, label, 'No version history is available.');

  const { labels, ranks } = rankHistory(versions, models, basis);
  const plotted = models.filter((m) => (ranks.get(m.slug) ?? []).some((r) => r !== null));
  const current = (m) => pick(m.rank, basis);
  const traces = plotted.map((m) => {
    const top3 = finite(current(m)) && current(m) <= 3;
    const color = developerColor(m.developer);
    return {
      x: labels, y: ranks.get(m.slug), mode: 'lines+markers', name: nameOf(m), showlegend: false, connectgaps: false,
      line: { color, width: top3 ? 2.5 : 1.5 }, marker: { size: top3 ? 10 : 7, color, symbol: 'circle' }, opacity: top3 ? 1 : 0.65,
      hovertemplate: `<b>${m.name}</b><br>%{x}: rank #%{y}<extra></extra>`,
    };
  });
  const maxRank = Math.max(1, ...plotted.flatMap((m) => ranks.get(m.slug).filter((r) => r !== null)));
  const base = baseLayout(opts, `Ranking history — ${labels[0]} to ${labels[labels.length - 1]}`);
  const layout = {
    ...base,
    xaxis: axisWith(base.xaxis, 'Version', { categoryorder: 'array', categoryarray: labels }),
    yaxis: axisWith(base.yaxis, 'Rank', {
      range: [maxRank + 0.5, 0.5], autorange: false,
      tickvals: Array.from({ length: maxRank }, (_, i) => i + 1), ticktext: Array.from({ length: maxRank }, (_, i) => `#${i + 1}`),
    }),
    margin: { ...base.margin, r: 90 },
    annotations: plotted.filter((m) => finite(current(m))).map((m) => ({
      x: 1.012, y: current(m), xref: 'paper', yref: 'y', text: nameOf(m), showarrow: false, xanchor: 'left', yanchor: 'middle',
      font: { size: 9, color: '#94a3b8', family: 'IBM Plex Sans, sans-serif' },
    })),
  };
  return makeSpec(opts, {
    traces, layout, label: `Line chart of rank by version for ${plotted.length} models across ${labels.length} versions, ${opts.basisLabel}.`,
    summary: `Rank history of ${plotted.length} models from ${labels[0]} to ${labels[labels.length - 1]} on the ${opts.basisLabel}. Gaps mean no recorded rank for that version.`,
  });
}

export const renderBump = (container, data, options, plotly) => renderSpec(container, buildBump(data, options), options, plotly);
