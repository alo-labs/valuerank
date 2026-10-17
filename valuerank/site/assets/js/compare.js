// Pure side-by-side comparison structure.
const MAX_COMPARE = 4;

/** Indexes of the highest non-null values (empty when every value is null). */
export function bestIndexes(values) {
  const max = Math.max(...values.filter((v) => v !== null));
  return values.flatMap((v, i) => (v === max ? [i] : []));
}

/** One row per dimension; `values` follow the order of the selected slugs, `best` lists the winning indexes. */
export function compareRows(models, slugs, dimensions, basis = 'plan') {
  const picked = slugs
    .map((slug) => models.find((m) => m.slug === slug))
    .filter(Boolean)
    .slice(0, MAX_COMPARE);
  const rows = dimensions.map((d) => {
    const values = picked.map((m) => (d.category === 'cost' ? m.costDims[basis] : m.dims[d.key]));
    return { key: d.key, label: d.label, category: d.category, values, best: bestIndexes(values) };
  });
  return { models: picked.map((m) => ({ slug: m.slug, name: m.name, developer: m.developer })), rows };
}
