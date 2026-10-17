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

function pointGap(box, point) {
  return Math.hypot(point.x - clamp(point.x, box.left, box.right), point.y - clamp(point.y, box.top, box.bottom));
}

function candidateOffsets(adjacentRadius, requestedRadii, candidateStep) {
  const directions = Array.from({ length: 24 }, (_, index) => {
    const angle = -Math.PI / 2 + (index * Math.PI) / 12;
    const ux = Math.cos(angle);
    const uy = Math.sin(angle);
    return { ux, uy, xa: ux > 0.18 ? 'left' : ux < -0.18 ? 'right' : 'center', ya: uy > 0.18 ? 'top' : uy < -0.18 ? 'bottom' : 'middle' };
  });
  const steps = [0, 4, 8, 14, 22, 32, 46, 64, 86, 114, 148, 190, 240, 300, 380];
  const radii = [...new Set([
    ...steps.map((step) => adjacentRadius + step),
    ...requestedRadii.map((radius) => Math.max(adjacentRadius, Number(radius))),
  ].filter(Number.isFinite))].sort((a, b) => a - b);
  const maxRadius = Math.max(...radii, adjacentRadius + 160);
  const offsets = [];
  const add = (ax, ay, xa, ya) => {
    const radius = Math.hypot(ax, ay);
    if (radius >= adjacentRadius - 1 && radius <= maxRadius + 1) offsets.push({ ax, ay, xa, ya, radius });
  };
  radii.forEach((radius) => directions.forEach((d) => add(d.ux * radius, d.uy * radius, d.xa, d.ya)));
  const edge = candidateStep * 0.35;
  for (let ax = -maxRadius; ax <= maxRadius; ax += candidateStep) {
    for (let ay = -maxRadius; ay <= maxRadius; ay += candidateStep) {
      add(ax, ay, ax > edge ? 'left' : ax < -edge ? 'right' : 'center', ay > edge ? 'top' : ay < -edge ? 'bottom' : 'middle');
    }
  }
  return offsets.sort((a, b) => a.radius - b.radius);
}

/**
 * Greedy-plus-compaction label placement in pixel space.
 * points: [{id?, label, x, y, frontier?}] in data coordinates.
 * geometry: see readGeometry. Returns Plotly annotation objects (paper-anchored).
 */
export function buildCollisionSafeLabelAnnotations(points, geometry, options = {}) {
  if (!geometry || !Array.isArray(points) || !points.length) return [];
  const { x: xa, y: ya, width, height } = geometry;
  const fontSize = positive(options.fontSize, 9);
  const safety = positive(options.safety, 1.15);
  const markerRadius = positive(options.markerRadius, 11);
  const labelPad = positive(options.labelPad, Math.max(4, fontSize * 0.55));
  const labelGap = positive(options.labelGap, Math.max(3, fontSize * 0.45));
  const adjacentRadius = positive(options.adjacentRadius, markerRadius + labelGap);
  const dark = geometry.dark;
  const textColor = options.textColor ?? (dark ? '#e2e8f0' : '#0f172a');
  const frontierColor = options.frontierColor ?? (dark ? '#34d399' : '#047857');
  const arrowMuted = options.arrowMuted ?? (dark ? 'rgba(148,163,184,.75)' : 'rgba(71,85,105,.7)');
  const arrowFrontier = options.arrowFrontier ?? (dark ? 'rgba(52,211,153,.95)' : 'rgba(4,120,87,.85)');

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

  const offsets = candidateOffsets(adjacentRadius, Array.isArray(options.radii) ? options.radii : [], Math.max(6, Number(options.candidateStep) || 8));
  items.forEach((item) => {
    item.isolation = items.reduce((nearest, other) => (other === item ? nearest : Math.min(nearest, Math.hypot(item.px.x - other.px.x, item.px.y - other.px.y))), Infinity);
  });

  const overlapsLabels = (box, placed, skip) => placed.some((p, index) => index !== skip &&
    !(box.right + labelPad < p.box.left || box.left - labelPad > p.box.right || box.bottom + labelPad < p.box.top || box.top - labelPad > p.box.bottom));
  const markerPenalty = (box) => items.reduce((total, item) => {
    const distance = pointGap(box, item.px);
    return total + (distance < markerRadius ? markerRadius - distance + 1 : 0);
  }, 0);
  const inBounds = (box) => box.left >= 2 && box.right <= width - 2 && box.top >= 2 && box.bottom <= height - 2;
  const spillCost = (box) => Math.max(0, 2 - box.left) + Math.max(0, box.right - (width - 2)) + Math.max(0, 2 - box.top) + Math.max(0, box.bottom - (height - 2));

  function findPlacement(item, placed, skip) {
    let bestValid = null;
    let bestInvalid = null;
    for (const offset of offsets) {
      if (bestValid && offset.radius > bestValid.gap + 10) break;
      const { ax, ay, xa: xanchor, ya: yanchor, radius } = offset;
      const box = labelBox(item.px.x, item.px.y, ax, ay, item.size.wPx, item.size.hPx, xanchor, yanchor);
      const gap = pointGap(box, item.px);
      const inChart = inBounds(box);
      const labelClear = inChart && !overlapsLabels(box, placed, skip);
      const markerCost = labelClear ? markerPenalty(box) : 0;
      const candidate = { ax, ay, xa: xanchor, ya: yanchor, box, gap, radius, adjacent: gap <= adjacentRadius + 1, score: gap + radius * 0.01 };
      if (labelClear && markerCost === 0) {
        if (!bestValid || candidate.score < bestValid.score) bestValid = candidate;
      } else {
        const overlap = placed.reduce((total, p, index) => total + (index === skip ? 0 : overlapArea(box, p.box)), 0);
        candidate.score = overlap * 1000 + markerCost * 100 + (inChart ? 0 : spillCost(box) * 10) + gap + radius * 0.01;
        if (!bestInvalid || candidate.score < bestInvalid.score) bestInvalid = candidate;
      }
    }
    return bestValid ?? bestInvalid;
  }

  const invalid = (entry, placed, index) => overlapsLabels(entry.box, placed, index) || markerPenalty(entry.box) !== 0;
  function placeInOrder(order) {
    const placed = [];
    order.forEach((item) => placed.push({ item, ...findPlacement(item, placed, null) }));
    for (let pass = 0; pass < 8; pass += 1) {
      let changed = false;
      placed.forEach((current, index) => {
        const next = findPlacement(current.item, placed, index);
        if (next.gap < current.gap - 0.25 || (Math.abs(next.gap - current.gap) <= 0.25 && next.radius < current.radius) || invalid(current, placed, index)) {
          placed[index] = { item: current.item, ...next };
          changed = true;
        }
      });
      if (!changed) break;
    }
    return placed;
  }
  const arrangementScore = (placed) => {
    const gaps = placed.map((entry) => entry.gap);
    const worst = Math.max(...gaps);
    return gaps.reduce((total, gap) => total + gap * gap, 0) + worst * worst * 2 +
      placed.reduce((count, entry, index) => count + (invalid(entry, placed, index) ? 1 : 0), 0) * 1e9;
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

  return best.map(({ item, ax, ay, xa: xanchor, ya: yanchor, adjacent }) => ({
    x: item.paper.x,
    y: item.paper.y,
    xref: 'paper',
    yref: 'paper',
    text: item.label,
    showarrow: !adjacent,
    arrowhead: 0,
    arrowsize: 0.95,
    arrowwidth: 1.3,
    arrowcolor: item.onFront ? arrowFrontier : arrowMuted,
    standoff: 0,
    startstandoff: 0,
    align: xanchor === 'right' ? 'right' : xanchor === 'center' ? 'center' : 'left',
    xanchor,
    yanchor,
    font: { size: fontSize, color: item.onFront ? frontierColor : textColor, family: 'IBM Plex Sans, sans-serif' },
    bgcolor: 'rgba(0,0,0,0)',
    bordercolor: 'rgba(0,0,0,0)',
    borderwidth: 0,
    borderpad: 0,
    captureevents: false,
    ...(adjacent ? { xshift: ax, yshift: ay } : { ax, ay, axref: 'pixel', ayref: 'pixel' }),
  }));
}

const intersects = (a, b, pad) => a.left < b.right + pad && a.right > b.left - pad && a.top < b.bottom + pad && a.bottom > b.top - pad;

/**
 * After the web font loads Plotly's text metrics change. Measure the rendered
 * labels and repack only those that still collide.
 * io: { readBoxes() -> [{index, rect}], bounds() -> rect, relayout(), waitForPaint() }
 * Mutates and returns `annotations`.
 */
export async function repairCollisionSafeLabelAnnotations(annotations, io, options = {}) {
  if (!Array.isArray(annotations) || !annotations.length) return annotations;
  const pad = positive(options.repairPad, 1);
  const maxPasses = positive(options.repairPasses, 5);
  const edge = positive(options.repairEdge, 6);
  const directions = Array.from({ length: 16 }, (_, index) => {
    const angle = -Math.PI / 2 + (index * Math.PI) / 8;
    return { x: Math.cos(angle), y: Math.sin(angle) };
  });
  const distances = [4, 10, 16, 24, 34, 48, 68, 96, 132, 174, 224, 284, 352];
  let boxes = io.readBoxes();
  if (boxes.length < annotations.length) return annotations;

  for (let pass = 0; pass < maxPasses; pass += 1) {
    const pairs = [];
    for (let l = 0; l < boxes.length; l += 1) {
      for (let r = l + 1; r < boxes.length; r += 1) if (intersects(boxes[l].rect, boxes[r].rect, pad)) pairs.push([boxes[l], boxes[r]]);
    }
    if (!pairs.length) return annotations;
    const conflicting = new Set(pairs.flatMap((pair) => pair.map((item) => item.index)));
    const rect = io.bounds();
    const bounds = { left: rect.left + edge, right: rect.right - edge, top: rect.top + edge, bottom: rect.bottom - positive(options.repairBottom, 58) };
    if (bounds.bottom <= bounds.top) bounds.bottom = rect.bottom - edge;
    const boxesByIndex = new Map(boxes.map((item) => [item.index, item]));
    const maxLabelWidth = Math.max(...boxes.map((item) => item.rect.right - item.rect.left));
    const naturalColumns = Math.ceil(Math.sqrt((boxes.length * (bounds.right - bounds.left)) / Math.max(1, bounds.bottom - bounds.top)));
    const widthColumns = Math.max(2, Math.floor((bounds.right - bounds.left + 10) / Math.max(1, maxLabelWidth + 10)));
    const gridColumns = positive(options.repairColumns, Math.min(8, Math.max(2, Math.min(naturalColumns, widthColumns))));
    const gridRows = Math.ceil(boxes.length / gridColumns);
    const cellWidth = (bounds.right - bounds.left) / gridColumns;
    const cellHeight = (bounds.bottom - bounds.top) / gridRows;

    const candidatesFor = (box) => {
      const width = box.rect.right - box.rect.left;
      const height = box.rect.bottom - box.rect.top;
      const candidates = [{ left: box.rect.left, top: box.rect.top }];
      directions.forEach((d) => distances.forEach((distance) => candidates.push({ left: box.rect.left + d.x * distance, top: box.rect.top + d.y * distance })));
      for (let row = 0; row < gridRows; row += 1) {
        for (let column = 0; column < gridColumns; column += 1) {
          candidates.push({
            left: bounds.left + column * cellWidth + Math.max(2, (cellWidth - width) / 2),
            top: bounds.top + row * cellHeight + Math.max(2, (cellHeight - height) / 2),
          });
        }
      }
      return candidates.map((c) => ({ left: c.left, right: c.left + width, top: c.top, bottom: c.top + height }));
    };
    const inside = (c) => c.left >= bounds.left && c.right <= bounds.right && c.top >= bounds.top && c.bottom <= bounds.bottom;
    const place = (items, reserved) => {
      const taken = reserved.map((item) => item.rect);
      const targets = new Map();
      for (const item of items) {
        const found = candidatesFor(item).find((c) => inside(c) && !taken.some((other) => intersects(c, other, pad)));
        if (!found) return null;
        targets.set(item.index, found);
        taken.push(found);
      }
      return targets;
    };

    const byIndex = (l, r) => l.index - r.index;
    let targets = place(boxes.filter((item) => conflicting.has(item.index)).sort(byIndex), boxes.filter((item) => !conflicting.has(item.index)));
    if (!targets) targets = place(boxes.slice().sort(byIndex), []);
    if (!targets) return annotations;
    targets.forEach((target, index) => {
      const current = boxesByIndex.get(index);
      const annotation = annotations[index];
      const deltaX = target.left - current.rect.left;
      const deltaY = target.top - current.rect.top;
      if (annotation.showarrow === false) {
        // An arrowless slot was not enough: keep the point connection and move the label.
        annotation.ax = (Number(annotation.xshift) || 0) + deltaX;
        annotation.ay = (Number(annotation.yshift) || 0) + deltaY;
        annotation.xshift = 0;
        annotation.yshift = 0;
        annotation.axref = 'pixel';
        annotation.ayref = 'pixel';
        annotation.showarrow = true;
      } else {
        annotation.ax = (Number(annotation.ax) || 0) + deltaX;
        annotation.ay = (Number(annotation.ay) || 0) + deltaY;
      }
    });
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
    relayout: () => env.relayout(annotations),
    waitForPaint: () => new Promise((resolve) => env.raf(() => env.raf(resolve))),
  };
}
