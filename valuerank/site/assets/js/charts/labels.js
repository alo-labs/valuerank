// Collision-safe model labels for scatter charts. Everything here is pure: the
// caller supplies axis geometry and (for the repair pass) measured boxes, so the
// logic runs unchanged in Node tests and in the browser.

const clamp = (value, low, high) => Math.max(low, Math.min(high, value));
const positive = (value, fallback) => Number(value) || fallback;

export const labelLines = (value) => String(value ?? '')
  .replace(/<br\s*\/?\s*>/gi, '\n')
  .replace(/<[^>]*>/g, '')
  .split('\n');

export const normalizeLabel = (value) => String(value ?? '')
  .replace(/<br\s*\/?\s*>/gi, '')
  .replace(/<[^>]*>/g, '')
  .replace(/\s+/g, ' ')
  .trim();

/**
 * Axis geometry from a rendered Plotly graph div (`gd._fullLayout`), or null
 * while the plot has no layout. `env.measureText(line, fontSize)` is optional.
 */
export function readGeometry(gd, env = {}) {
  const full = gd && gd._fullLayout;
  if (!full) return null;
  const { xaxis: xa, yaxis: ya } = full;
  if (!xa || !ya || !xa._length || !ya._length) return null;
  const axis = (a) => ({ type: a.type, offset: a._offset, length: a._length, l2p: (value) => a.l2p(value) });
  return {
    width: full.width || 1100,
    height: full.height || 520,
    x: axis(xa),
    y: axis(ya),
    dark: Boolean(env.dark),
    measureText: env.measureText,
  };
}

function labelBox(pointX, pointY, ax, ay, labelWidth, labelHeight, xanchor, yanchor) {
  const anchorX = pointX + ax;
  const anchorY = pointY + ay;
  let left = anchorX - labelWidth / 2;
  let top = anchorY - labelHeight / 2;
  if (xanchor === 'left') left = anchorX;
  else if (xanchor === 'right') left = anchorX - labelWidth;
  if (yanchor === 'top') top = anchorY;
  else if (yanchor === 'bottom') top = anchorY - labelHeight;
  return { left, right: left + labelWidth, top, bottom: top + labelHeight };
}

const overlapArea = (a, b) => Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) *
  Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));

function pointGapSquared(box, point) {
  const dx = point.x - clamp(point.x, box.left, box.right);
  const dy = point.y - clamp(point.y, box.top, box.bottom);
  return dx * dx + dy * dy;
}

const pointGap = (box, point) => Math.sqrt(pointGapSquared(box, point));

// Labels stay beside their dots: no label box may end more than MAX_GAP pixels from its marker's edge.
const DEFAULT_MAX_GAP = 18;
const REACH_TOLERANCE = 1e-6;
const RING_STEPS = [0, 2, 4, 6, 9, 12, 16, 20, 26, 32, 40];
const shiftOf = (value) => Number(value) || 0;

// 24 compass directions; the anchor keeps the label box on the far side of the offset point from the dot.
const DIRECTIONS = Array.from({ length: 24 }, (_, index) => {
  const angle = -Math.PI / 2 + (index * Math.PI) / 12;
  const ux = Math.cos(angle);
  const uy = Math.sin(angle);
  return { ux, uy, xa: ux > 0.18 ? 'left' : ux < -0.18 ? 'right' : 'center', ya: uy > 0.18 ? 'top' : uy < -0.18 ? 'bottom' : 'middle' };
});

/**
 * The distances a label may keep from its dot. `reach` is the largest centre-to-box distance allowed:
 * the marker radius plus `maxGap`, never less than the adjacent distance itself.
 */
function resolveReach(options) {
  const fontSize = positive(options.fontSize, 9);
  const markerRadius = positive(options.markerRadius, 11);
  const labelGap = positive(options.labelGap, Math.max(3, fontSize * 0.45));
  const adjacentRadius = positive(options.adjacentRadius, markerRadius + labelGap);
  const maxGap = positive(options.maxGap, DEFAULT_MAX_GAP);
  return { fontSize, markerRadius, adjacentRadius, reach: Math.max(markerRadius + maxGap, adjacentRadius) };
}

/** Ring distances from the adjacent radius out to the cap, closest first. Requested radii are clamped into that range. */
function ringRadii(adjacentRadius, reach, requestedRadii) {
  return [...new Set([adjacentRadius, reach, ...RING_STEPS.map((step) => adjacentRadius + step), ...requestedRadii]
    .map(Number)
    .filter(Number.isFinite)
    .map((radius) => clamp(radius, adjacentRadius, reach)))].sort((a, b) => a - b);
}

function candidateOffsets(adjacentRadius, reach, requestedRadii, candidateStep) {
  const offsets = [];
  ringRadii(adjacentRadius, reach, requestedRadii).forEach((radius) => DIRECTIONS.forEach((d) => offsets.push({ ax: d.ux * radius, ay: d.uy * radius, xa: d.xa, ya: d.ya, radius })));
  const edge = candidateStep * 0.35;
  for (let ax = -reach; ax <= reach; ax += candidateStep) {
    for (let ay = -reach; ay <= reach; ay += candidateStep) {
      const radius = Math.hypot(ax, ay);
      if (radius >= adjacentRadius - 1 && radius <= reach) {
        offsets.push({ ax, ay, xa: ax > edge ? 'left' : ax < -edge ? 'right' : 'center', ya: ay > edge ? 'top' : ay < -edge ? 'bottom' : 'middle', radius });
      }
    }
  }
  return offsets.sort((a, b) => a.radius - b.radius);
}

/**
 * Greedy-plus-compaction label placement in pixel space.
 * points: [{id?, label, x, y, frontier?}] in data coordinates.
 * geometry: see readGeometry. Returns arrowless Plotly annotation objects (paper-anchored, positioned
 * with xshift/yshift, where yshift is positive upward). Every label stays within `options.maxGap`
 * pixels (default 18) of its marker's edge; when the neighbourhood is crowded labels overlap
 * slightly rather than travelling further from their dots.
 */
export function buildCollisionSafeLabelAnnotations(points, geometry, options = {}) {
  if (!geometry || !Array.isArray(points) || !points.length) return [];
  const { x: xa, y: ya } = geometry;
  const { fontSize, markerRadius, adjacentRadius, reach } = resolveReach(options);
  const safety = positive(options.safety, 1.15);
  const labelPad = positive(options.labelPad, Math.max(4, fontSize * 0.55));
  const dark = geometry.dark;
  const textColor = options.textColor ?? (dark ? '#e2e8f0' : '#0f172a');
  const frontierColor = options.frontierColor ?? (dark ? '#34d399' : '#047857');

  const coordinate = (axis, value) => {
    const numeric = Number(value);
    if (!Number.isFinite(numeric) || (axis.type === 'log' && numeric <= 0)) return NaN;
    return axis.type === 'log' ? axis.l2p(Math.log10(numeric)) : axis.l2p(numeric);
  };
  const estimateSize = (label) => {
    const lines = labelLines(label);
    const widest = geometry.measureText
      ? Math.max(...lines.map((line) => geometry.measureText(line, fontSize)))
      : Math.max(1, ...lines.map((line) => line.length)) * fontSize * 0.6;
    return { wPx: Math.ceil((widest + 7) * safety), hPx: Math.ceil((lines.length * fontSize * 1.35 + 5) * safety) };
  };

  const items = points.map((point, idx) => {
    const label = point.label ?? '';
    const px = { x: xa.offset + coordinate(xa, point.x), y: ya.offset + coordinate(ya, point.y) };
    if (label === '' || !Number.isFinite(px.x) || !Number.isFinite(px.y)) return null;
    return {
      idx, label, px, onFront: Boolean(point.frontier), size: estimateSize(label),
      paper: { x: (px.x - xa.offset) / xa.length, y: 1 - (px.y - ya.offset) / ya.length },
    };
  }).filter(Boolean);
  if (!items.length) return [];

  const offsets = candidateOffsets(adjacentRadius, reach, Array.isArray(options.radii) ? options.radii : [], Math.max(6, Number(options.candidateStep) || 8));
  items.forEach((item) => {
    item.isolation = items.reduce((nearest, other) => (other === item ? nearest : Math.min(nearest, Math.hypot(item.px.x - other.px.x, item.px.y - other.px.y))), Infinity);
  });

  // Labels and markers only interact with items near enough for a candidate inside the cap to reach them:
  // a label box lies within `item.span` of its dot, so two boxes can meet only if their dots are closer than the sum.
  items.forEach((item) => { item.span = reach + Math.hypot(item.size.wPx, item.size.hPx); });
  items.forEach((item) => {
    const distanceTo = (other) => Math.hypot(item.px.x - other.px.x, item.px.y - other.px.y);
    item.near = items.filter((other) => other !== item && distanceTo(other) <= item.span + other.span + 2 * labelPad);
    item.markers = [item, ...items.filter((other) => other !== item && distanceTo(other) <= item.span + markerRadius)];
  });
  // `slots[item.idx]` is the placement currently chosen for an item (undefined until it has one).
  const overlapsLabels = (item, box, slots) => item.near.some((other) => {
    const p = slots[other.idx];
    return p && !(box.right + labelPad < p.box.left || box.left - labelPad > p.box.right || box.bottom + labelPad < p.box.top || box.top - labelPad > p.box.bottom);
  });
  const overlapTotal = (item, box, slots) => item.near.reduce((total, other) => total + (slots[other.idx] ? overlapArea(box, slots[other.idx].box) : 0), 0);
  const markerReach = markerRadius * markerRadius;
  const markerPenalty = (item, box) => item.markers.reduce((total, other) => {
    const squared = pointGapSquared(box, other.px);
    return total + (squared < markerReach ? markerRadius - Math.sqrt(squared) + 1 : 0);
  }, 0);
  // Labels must sit inside the plot area, not merely inside the figure (which includes the axis margins).
  const area = { left: xa.offset + 2, right: xa.offset + xa.length - 2, top: ya.offset + 2, bottom: ya.offset + ya.length - 2 };
  const inBounds = (box) => box.left >= area.left && box.right <= area.right && box.top >= area.top && box.bottom <= area.bottom;
  const spillCost = (box) => Math.max(0, area.left - box.left) + Math.max(0, box.right - area.right) + Math.max(0, area.top - box.top) + Math.max(0, box.bottom - area.bottom);

  // Preference inside the cap: the closest in-bounds slot that is clear of other labels and markers; failing
  // that, the slot with the least spill, label overlap and marker coverage (slight overlap beats distance).
  function findPlacement(item, slots) {
    let bestValid = null;
    let bestInvalid = null;
    for (const offset of offsets) {
      if (bestValid && offset.radius > bestValid.gap + 10) break;
      const { ax, ay, xa: xanchor, ya: yanchor, radius } = offset;
      const box = labelBox(item.px.x, item.px.y, ax, ay, item.size.wPx, item.size.hPx, xanchor, yanchor);
      const gap = pointGap(box, item.px);
      const inChart = inBounds(box);
      const markerCost = markerPenalty(item, box);
      const candidate = { ax, ay, xa: xanchor, ya: yanchor, box, gap, radius, score: gap + radius * 0.01 };
      if (inChart && markerCost === 0 && !overlapsLabels(item, box, slots)) {
        if (!bestValid || candidate.score < bestValid.score) bestValid = candidate;
      } else {
        candidate.score = spillCost(box) * 1e6 + overlapTotal(item, box, slots) * 1000 + markerCost * 100 + gap + radius * 0.01;
        if (!bestInvalid || candidate.score < bestInvalid.score) bestInvalid = candidate;
      }
    }
    return bestValid ?? bestInvalid;
  }

  const invalid = (entry, slots) => overlapsLabels(entry.item, entry.box, slots) || markerPenalty(entry.item, entry.box) !== 0;
  function placeInOrder(order) {
    const slots = [];
    const placed = order.map((item) => {
      slots[item.idx] = { item, ...findPlacement(item, slots) };
      return slots[item.idx];
    });
    for (let pass = 0; pass < 8; pass += 1) {
      let changed = false;
      placed.forEach((current, index) => {
        const next = findPlacement(current.item, slots);
        if (next.gap < current.gap - 0.25 || (Math.abs(next.gap - current.gap) <= 0.25 && next.radius < current.radius) || invalid(current, slots)) {
          slots[current.item.idx] = { item: current.item, ...next };
          placed[index] = slots[current.item.idx];
          changed = true;
        }
      });
      if (!changed) break;
    }
    return placed;
  }
  const arrangementScore = (placed) => {
    const slots = [];
    placed.forEach((entry) => { slots[entry.item.idx] = entry; });
    const gaps = placed.map((entry) => entry.gap);
    const worst = Math.max(...gaps);
    const overlap = placed.reduce((total, entry) => total + entry.item.near.reduce((sum, other) => (other.idx > entry.item.idx ? sum + overlapArea(entry.box, slots[other.idx].box) : sum), 0), 0);
    return gaps.reduce((total, gap) => total + gap * gap, 0) + worst * worst * 2 + overlap * 50 +
      placed.reduce((count, entry) => count + (invalid(entry, slots) ? 1 : 0), 0) * 1e9;
  };

  const byName = (l, r) => l.label.localeCompare(r.label);
  const orderings = [
    items.slice().sort((l, r) => (l.onFront !== r.onFront ? (l.onFront ? -1 : 1) : l.isolation - r.isolation || byName(l, r))),
    items.slice().sort((l, r) => r.isolation - l.isolation || byName(l, r)),
    items.slice().sort((l, r) => l.px.x - r.px.x || l.px.y - r.px.y || byName(l, r)),
    items.slice().sort((l, r) => l.px.y - r.px.y || l.px.x - r.px.x || byName(l, r)),
  ];
  let best = null;
  let bestScore = Infinity;
  orderings.forEach((order) => {
    const candidate = placeInOrder(order);
    const score = arrangementScore(candidate);
    if (score < bestScore) { best = candidate; bestScore = score; }
  });

  return best.map(({ item, ax, ay, xa: xanchor, ya: yanchor }) => ({
    x: item.paper.x,
    y: item.paper.y,
    xref: 'paper',
    yref: 'paper',
    text: item.label,
    showarrow: false,
    align: xanchor === 'right' ? 'right' : xanchor === 'center' ? 'center' : 'left',
    xanchor,
    yanchor,
    font: { size: fontSize, color: item.onFront ? frontierColor : textColor, family: 'IBM Plex Sans, sans-serif' },
    bgcolor: 'rgba(0,0,0,0)',
    bordercolor: 'rgba(0,0,0,0)',
    borderwidth: 0,
    borderpad: 0,
    captureevents: false,
    // Pixel offsets above are screen-down; Plotly's yshift is positive upward.
    xshift: ax,
    yshift: 0 - ay,
  }));
}

/** Moves an annotation by (dx, dy) screen pixels. Plotly's xshift is positive rightward and yshift positive upward. */
function shiftAnnotation(annotation, dx, dy) {
  annotation.xshift = shiftOf(annotation.xshift) + dx;
  annotation.yshift = shiftOf(annotation.yshift) - dy;
}

/**
 * Where the label's dot is in screen space. With a plot rectangle it follows from the annotation's paper
 * coordinates; otherwise it is recovered from the rendered box, the annotation's anchors and its shifts.
 */
function dotOf(annotation, rect, plot) {
  if (plot) return { x: plot.left + annotation.x * (plot.right - plot.left), y: plot.top + (1 - annotation.y) * (plot.bottom - plot.top) };
  const anchorX = annotation.xanchor === 'left' ? rect.left : annotation.xanchor === 'right' ? rect.right : (rect.left + rect.right) / 2;
  const anchorY = annotation.yanchor === 'top' ? rect.top : annotation.yanchor === 'bottom' ? rect.bottom : (rect.top + rect.bottom) / 2;
  return { x: anchorX - shiftOf(annotation.xshift), y: anchorY + shiftOf(annotation.yshift) };
}

/** One axis of a measured label: clamp into [low, high]; if that would cover its point, flip to the far side when that fits. */
function insideRange(start, size, anchor, low, high) {
  if (start >= low && start + size <= high) return start;
  const clamped = clamp(start, low, high - size);
  if (anchor < clamped || anchor > clamped + size) return clamped;
  const mirrored = 2 * anchor - (start + size);
  return mirrored >= low && mirrored + size <= high ? mirrored : clamped;
}

/**
 * Pulls measured labels that spill out of the plot area back inside, unless that would carry a label
 * beyond `reach` from its dot. Returns true when any annotation moved.
 */
function keepInsidePlot(annotations, boxes, plot, reach) {
  let moved = false;
  boxes.forEach(({ index, rect }) => {
    const annotation = annotations[index];
    const dot = dotOf(annotation, rect, plot);
    const left = insideRange(rect.left, rect.right - rect.left, dot.x, plot.left, plot.right);
    const top = insideRange(rect.top, rect.bottom - rect.top, dot.y, plot.top, plot.bottom);
    if (left === rect.left && top === rect.top) return;
    const target = { left, right: left + rect.right - rect.left, top, bottom: top + rect.bottom - rect.top };
    if (pointGap(target, dot) > reach + REACH_TOLERANCE) return;
    shiftAnnotation(annotation, left - rect.left, top - rect.top);
    moved = true;
  });
  return moved;
}

const intersects = (a, b, pad) => a.left < b.right + pad && a.right > b.left - pad && a.top < b.bottom + pad && a.bottom > b.top - pad;

/**
 * After the web font loads Plotly's text metrics change. Measure the rendered
 * labels and repack only those that still collide, each within the proximity
 * cap (`maxGap`, default 18px from the marker edge) of its own dot. A label with
 * no free slot inside the cap stays where it is; labels never travel further to escape a collision.
 * io: { readBoxes() -> [{index, rect}], bounds() -> rect, plot?() -> rect, relayout(), waitForPaint() }
 * `plot()` is the plot-area rectangle; when present every label is also kept inside it.
 * Mutates (xshift/yshift only, never an arrow) and returns `annotations`.
 */
export async function repairCollisionSafeLabelAnnotations(annotations, io, options = {}) {
  if (!Array.isArray(annotations) || !annotations.length) return annotations;
  const pad = positive(options.repairPad, 1);
  const maxPasses = positive(options.repairPasses, 5);
  const edge = positive(options.repairEdge, 6);
  const { adjacentRadius, reach } = resolveReach(options);
  const radii = ringRadii(adjacentRadius, reach, []);
  let boxes = io.readBoxes();
  if (boxes.length < annotations.length) return annotations;
  const plot = io.plot ? io.plot() : null;
  if (plot && keepInsidePlot(annotations, boxes, plot, reach)) {
    await io.relayout();
    await io.waitForPaint();
    boxes = io.readBoxes();
    if (boxes.length < annotations.length) return annotations;
  }

  for (let pass = 0; pass < maxPasses; pass += 1) {
    const pairs = [];
    for (let l = 0; l < boxes.length; l += 1) {
      for (let r = l + 1; r < boxes.length; r += 1) if (intersects(boxes[l].rect, boxes[r].rect, pad)) pairs.push([boxes[l], boxes[r]]);
    }
    if (!pairs.length) return annotations;
    const conflicting = new Set(pairs.flatMap((pair) => pair.map((item) => item.index)));
    const rect = io.bounds();
    const bounds = plot
      ? { left: plot.left + edge, right: plot.right - edge, top: plot.top + edge, bottom: plot.bottom - edge }
      : { left: rect.left + edge, right: rect.right - edge, top: rect.top + edge, bottom: rect.bottom - positive(options.repairBottom, 58) };
    if (bounds.bottom <= bounds.top) bounds.bottom = rect.bottom - edge;

    // Slots around the label's own dot, closest first; the cap holds by construction (ring radius <= reach).
    const candidatesFor = (box) => {
      const width = box.rect.right - box.rect.left;
      const height = box.rect.bottom - box.rect.top;
      const dot = dotOf(annotations[box.index], box.rect, plot);
      return radii.flatMap((radius) => DIRECTIONS.map((d) => ({ radius, ...labelBox(dot.x, dot.y, d.ux * radius, d.uy * radius, width, height, d.xa, d.ya) })))
        .map((c) => ({ ...c, travel: Math.hypot(c.left - box.rect.left, c.top - box.rect.top) }))
        .sort((l, r) => l.radius - r.radius || l.travel - r.travel);
    };
    const inside = (c) => c.left >= bounds.left && c.right <= bounds.right && c.top >= bounds.top && c.bottom <= bounds.bottom;
    // Every label counts as an obstacle at its current (or already chosen) position while the others are placed.
    const positions = new Map(boxes.map((item) => [item.index, item.rect]));
    const blocked = (c, own) => [...positions].some(([index, other]) => index !== own && intersects(c, other, pad));
    let moved = false;
    boxes.filter((item) => conflicting.has(item.index)).sort((l, r) => l.index - r.index).forEach((item) => {
      if (!blocked(item.rect, item.index)) return;
      const found = candidatesFor(item).find((c) => inside(c) && !blocked(c, item.index));
      if (!found) return;
      shiftAnnotation(annotations[item.index], found.left - item.rect.left, found.top - item.rect.top);
      positions.set(item.index, found);
      moved = true;
    });
    if (!moved) return annotations;
    await io.relayout();
    await io.waitForPaint();
    boxes = io.readBoxes();
    if (boxes.length < annotations.length) return annotations;
  }
  return annotations;
}

/**
 * Browser glue for the repair pass: reads rendered SVG labels from `gd`.
 * env: { relayout(annotations) -> Promise, raf(cb) }.
 */
export function createRepairIO(gd, annotations, env) {
  const index = new Map();
  annotations.forEach((annotation, i) => index.set(normalizeLabel(annotation.text), i));
  return {
    readBoxes: () => [...gd.querySelectorAll('g.annotation text')].map((node) => {
      const i = index.get(normalizeLabel(node.textContent));
      if (i === undefined) return null;
      const { left, right, top, bottom } = node.getBoundingClientRect();
      return { index: i, rect: { left, right, top, bottom } };
    }).filter((item) => item && item.rect.right > item.rect.left && item.rect.bottom > item.rect.top),
    bounds: () => gd.getBoundingClientRect(),
    plot: () => {
      const { left, top } = gd.getBoundingClientRect();
      const size = gd._fullLayout._size;
      return { left: left + size.l, right: left + size.l + size.w, top: top + size.t, bottom: top + size.t + size.h };
    },
    relayout: () => env.relayout(annotations),
    waitForPaint: () => new Promise((resolve) => env.raf(() => env.raf(resolve))),
  };
}
