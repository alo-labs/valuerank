import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildCollisionSafeLabelAnnotations, createRepairIO, labelLines, normalizeLabel, readGeometry, repairCollisionSafeLabelAnnotations } from '../../../valuerank/site/assets/js/charts/labels.js';
import { createPlotDiv } from './_fixtures.mjs';

const geometry = (over = {}) => ({
  width: 1000, height: 600, dark: false, measureText: (line) => line.length * 5,
  x: { type: 'linear', offset: 50, length: 800, l2p: (v) => v * 8 },
  y: { type: 'linear', offset: 50, length: 500, l2p: (v) => 500 - v * 5 },
  ...over,
});

// Plotly annotations: xshift is positive to the right, yshift is positive UP.
const dotOf = (annotation, geo) => ({ x: geo.x.offset + annotation.x * geo.x.length, y: geo.y.offset + (1 - annotation.y) * geo.y.length });
const boxOf = (annotation, geo, fontSize = 9, safety = 1.15) => {
  const px = dotOf(annotation, geo);
  const lines = labelLines(annotation.text);
  const w = Math.ceil((Math.max(...lines.map((l) => geo.measureText(l))) + 7) * safety);
  const h = Math.ceil((lines.length * fontSize * 1.35 + 5) * safety);
  const cx = px.x + annotation.xshift;
  const cy = px.y - annotation.yshift;
  const left = annotation.xanchor === 'left' ? cx : annotation.xanchor === 'right' ? cx - w : cx - w / 2;
  const top = annotation.yanchor === 'top' ? cy : annotation.yanchor === 'bottom' ? cy - h : cy - h / 2;
  return { left, right: left + w, top, bottom: top + h };
};
const distanceToBox = (box, point) => Math.hypot(point.x - Math.max(box.left, Math.min(box.right, point.x)), point.y - Math.max(box.top, Math.min(box.bottom, point.y)));
const MARKER = 11;
const MAX_GAP = 18;
const EPS = 1e-6;
/** Pixels between the marker edge and the nearest edge of the label box. */
const edgeGap = (annotation, geo, markerRadius = MARKER) => distanceToBox(boxOf(annotation, geo), dotOf(annotation, geo)) - markerRadius;
const assertArrowless = (annotation) => {
  assert.equal(annotation.showarrow, false, annotation.text);
  ['ax', 'ay', 'axref', 'ayref', 'arrowhead', 'arrowsize', 'arrowwidth', 'arrowcolor', 'standoff', 'startstandoff'].forEach((key) => assert.equal(key in annotation, false, `${annotation.text} has ${key}`));
  assert.equal(Number.isFinite(annotation.xshift) && Number.isFinite(annotation.yshift), true, `${annotation.text} is positioned with xshift/yshift`);
};
const assertWithinCap = (annotations, geo, { markerRadius = MARKER, maxGap = MAX_GAP } = {}) => annotations.forEach((annotation) => {
  assertArrowless(annotation);
  const gap = edgeGap(annotation, geo, markerRadius);
  assert.ok(gap <= maxGap + EPS, `${annotation.text} sits ${gap.toFixed(2)}px from its marker (cap ${maxGap})`);
  assert.ok(gap >= -EPS, `${annotation.text} covers its own marker (${gap.toFixed(2)})`);
});
const overlaps = (a, b) => a.left < b.right && a.right > b.left && a.top < b.bottom && a.bottom > b.top;

test('label text helpers strip markup', () => {
  assert.deepEqual(labelLines('<b>A</b><br>B<br/>C'), ['A', 'B', 'C']);
  assert.deepEqual(labelLines(null), ['']);
  assert.equal(normalizeLabel(' <b>A</b><br>  B '), 'A B');
  assert.equal(normalizeLabel(undefined), '');
});

test('readGeometry needs a rendered layout', () => {
  assert.equal(readGeometry(null), null);
  assert.equal(readGeometry({}), null);
  assert.equal(readGeometry({ _fullLayout: { xaxis: {}, yaxis: {} } }), null);
  assert.equal(readGeometry({ _fullLayout: { xaxis: { _length: 1 } } }), null);
  const gd = createPlotDiv();
  const geo = readGeometry(gd, { dark: true, measureText: () => 1 });
  assert.deepEqual([geo.width, geo.height, geo.x.offset, geo.x.length, geo.x.type, geo.dark], [1000, 600, 50, 800, 'linear', true]);
  assert.equal(geo.x.l2p(2), 16);
  const bare = createPlotDiv({ layout: { xaxis: { _length: 1, _offset: 0, l2p: (v) => v }, yaxis: { _length: 1, _offset: 0, l2p: (v) => v } } });
  const defaults = readGeometry(bare);
  assert.deepEqual([defaults.width, defaults.height, defaults.dark], [1100, 520, false]);
});

test('no points or no geometry yields no annotations', () => {
  assert.deepEqual(buildCollisionSafeLabelAnnotations([], geometry()), []);
  assert.deepEqual(buildCollisionSafeLabelAnnotations(null, geometry()), []);
  assert.deepEqual(buildCollisionSafeLabelAnnotations([{ label: 'A', x: 1, y: 1 }], null), []);
  const invalid = [{ label: '', x: 1, y: 1 }, { label: 'A', x: NaN, y: 1 }, { x: 1, y: 1 }, { label: 'L', x: -5, y: 1 }];
  assert.deepEqual(buildCollisionSafeLabelAnnotations(invalid, geometry({ x: { ...geometry().x, type: 'log' } })), []);
});

test('an isolated point gets an arrowless adjacent label in paper coordinates', () => {
  const geo = geometry();
  const [a] = buildCollisionSafeLabelAnnotations([{ label: 'Solo', x: 50, y: 50 }], geo);
  assertWithinCap([a], geo);
  assert.equal(a.xref, 'paper');
  assert.ok(Math.abs(a.x - 0.5) < 1e-9 && Math.abs(a.y - 0.5) < 1e-9);
  assert.equal(a.font.color, '#0f172a');
  assert.equal(a.align, a.xanchor === 'right' ? 'right' : a.xanchor === 'center' ? 'center' : 'left');
  assert.ok(edgeGap(a, geo) <= 5, 'an uncrowded label hugs its marker');
});

test('log axes map values through log10 and frontier/dark colours apply', () => {
  const geo = geometry({ dark: true, x: { type: 'log', offset: 50, length: 800, l2p: (v) => (v + 2) * 100 } });
  const [a, b] = buildCollisionSafeLabelAnnotations([{ label: 'F', x: 10, y: 50, frontier: true }, { label: 'N', x: 1000, y: 10 }], geo);
  assert.equal(a.font.color, '#34d399');
  assert.equal(b.font.color, '#e2e8f0');
  assert.ok(Math.abs(a.x - (300 / 800)) < 1e-9);
  assertWithinCap([a, b], geo);
});

test('custom colours and options override the defaults; estimate works without measureText', () => {
  const geo = geometry({ measureText: undefined });
  const [a] = buildCollisionSafeLabelAnnotations([{ label: 'Two<br>lines', x: 50, y: 50, frontier: true }, { label: 'Z', x: 1, y: 1 }], geo, {
    fontSize: 12, safety: 1.5, markerRadius: 5, labelPad: 2, labelGap: 2, adjacentRadius: 9, radii: [30, 'x'], candidateStep: 10,
    textColor: 'red', frontierColor: 'green',
  });
  assert.equal(a.font.size, 12);
  assert.equal(a.font.color, 'green');
  assert.equal('arrowcolor' in a, false, 'there are no leader lines to colour');
  const [b] = buildCollisionSafeLabelAnnotations([{ label: 'Q', x: 50, y: 50 }], geo, { textColor: 'red' });
  assert.equal(b.font.color, 'red');
});

test('every label in a crowded group is arrowless and within the proximity cap of its marker', () => {
  const geo = geometry();
  const points = Array.from({ length: 14 }, (_, i) => ({ label: `Model ${i}`, x: 40 + (i % 4), y: 40 + Math.floor(i / 4), frontier: i % 5 === 0 }));
  const annotations = buildCollisionSafeLabelAnnotations(points, geo, { markerRadius: MARKER });
  assert.equal(annotations.length, points.length);
  assertWithinCap(annotations, geo);
});

test('labels are positioned with xshift/yshift and carry no leader-line fields', () => {
  const geo = geometry();
  const annotations = buildCollisionSafeLabelAnnotations([{ label: 'A', x: 10, y: 10 }, { label: 'B', x: 11, y: 10 }, { label: 'C', x: 12, y: 10, frontier: true }], geo);
  annotations.forEach(assertArrowless);
});

test('the proximity cap is the maxGap option (default 18) and never undercuts the adjacent distance', () => {
  const geo = geometry();
  const cluster = Array.from({ length: 10 }, (_, i) => ({ label: `Cluster ${i}`, x: 40 + (i % 2) * 0.1, y: 40 + (i % 3) * 0.1 }));
  assertWithinCap(buildCollisionSafeLabelAnnotations(cluster, geo), geo);
  assertWithinCap(buildCollisionSafeLabelAnnotations(cluster, geo, { maxGap: 8 }), geo, { maxGap: 8 });
  // A cap below the distance the label needs to clear its marker still places the label beside the marker.
  const tight = buildCollisionSafeLabelAnnotations(cluster, geo, { maxGap: 1 });
  tight.forEach((annotation) => {
    assertArrowless(annotation);
    assert.ok(edgeGap(annotation, geo) <= 4.1, `${annotation.text} stays at the adjacent distance`);
  });
});

test('requested radii beyond the cap are clamped to it', () => {
  const geo = geometry();
  const cluster = Array.from({ length: 10 }, (_, i) => ({ label: `Cluster ${i}`, x: 40 + (i % 2) * 0.1, y: 40 + (i % 3) * 0.1 }));
  assertWithinCap(buildCollisionSafeLabelAnnotations(cluster, geo, { radii: [200, 400] }), geo);
});

test('eight points inside a 12px circle keep every label within the cap, overlapping if they must', () => {
  const geo = geometry();
  const points = Array.from({ length: 8 }, (_, i) => {
    const angle = (i * Math.PI) / 4;
    return { label: `Model ${i}`, x: 50 + (6 * Math.cos(angle)) / 8, y: 50 + (6 * Math.sin(angle)) / 5, frontier: i === 0 };
  });
  const annotations = buildCollisionSafeLabelAnnotations(points, geo);
  assert.equal(annotations.length, 8);
  assertWithinCap(annotations, geo);
});

test('labels may overlap each other inside the cap rather than travel far from their dots', () => {
  const geo = geometry();
  const points = Array.from({ length: 12 }, (_, i) => ({ label: `Stack ${i}`, x: 50, y: 50 }));
  const annotations = buildCollisionSafeLabelAnnotations(points, geo);
  assertWithinCap(annotations, geo);
  const boxes = annotations.map((a) => boxOf(a, geo));
  const crowded = boxes.some((box, i) => boxes.some((other, j) => j !== i && overlaps(box, other)));
  assert.ok(crowded, 'twelve identical dots cannot all be clear of each other inside the cap');
});

test('points at the chart edge and stacked duplicates still produce an annotation each', () => {
  const geo = geometry({ width: 120, height: 90 });
  const points = [{ label: 'Corner', x: 0, y: 100 }, { label: 'Corner2', x: 0, y: 100 }, { label: 'Far', x: 99, y: 0 }, { label: 'Far2', x: 99, y: 0 }, { label: 'Far3', x: 99, y: 0 }];
  const annotations = buildCollisionSafeLabelAnnotations(points, geo);
  assert.equal(annotations.length, 5);
  assertWithinCap(annotations, geo);
});

test('near-edge placement spills are costed when no in-bounds slot exists', () => {
  const geo = geometry({ width: 20, height: 12 });
  const annotations = buildCollisionSafeLabelAnnotations([{ label: 'Huge label that cannot fit', x: 2, y: 100 }, { label: 'Other huge label here', x: 3, y: 100 }], geo);
  assert.equal(annotations.length, 2);
  assertWithinCap(annotations, geo);
});

const area = (geo) => ({ left: geo.x.offset, right: geo.x.offset + geo.x.length, top: geo.y.offset, bottom: geo.y.offset + geo.y.length });
const assertInsidePlot = (annotation, geo) => {
  const box = boxOf(annotation, geo);
  const plot = area(geo);
  assert.ok(box.left >= plot.left && box.right <= plot.right, `${annotation.text} spills horizontally: ${JSON.stringify(box)}`);
  assert.ok(box.top >= plot.top && box.bottom <= plot.bottom, `${annotation.text} spills vertically: ${JSON.stringify(box)}`);
};

test('labels at the plot edges stay inside the plot area and within the cap', () => {
  const geo = geometry();
  const edges = [
    { label: 'Left edge', x: 0, y: 50 }, { label: 'Right edge', x: 100, y: 50 },
    { label: 'Top edge', x: 50, y: 100 }, { label: 'Bottom edge', x: 50, y: 0 },
    { label: 'Top left', x: 0, y: 100 }, { label: 'Bottom right', x: 100, y: 0 },
  ];
  const annotations = buildCollisionSafeLabelAnnotations(edges, geo);
  assert.equal(annotations.length, edges.length);
  assertWithinCap(annotations, geo);
  annotations.forEach((annotation) => assertInsidePlot(annotation, geo));
});

test('a label at the plot edge sits on the inner side of its dot (yshift is positive upward)', () => {
  const geo = geometry();
  const annotations = buildCollisionSafeLabelAnnotations([
    { label: 'Bottom edge', x: 50, y: 0 }, { label: 'Top edge', x: 50, y: 100 }, { label: 'Left edge', x: 0, y: 50 }, { label: 'Right edge', x: 100, y: 50 },
  ], geo);
  const named = (text) => annotations.find((annotation) => annotation.text === text);
  const [bottom, top, left, right] = ['Bottom edge', 'Top edge', 'Left edge', 'Right edge'].map(named);
  assert.ok(boxOf(bottom, geo).bottom <= dotOf(bottom, geo).y, 'above the bottom-edge dot');
  assert.ok(bottom.yshift > 0, 'Plotly yshift is positive upward');
  assert.ok(boxOf(top, geo).top >= dotOf(top, geo).y, 'below the top-edge dot');
  assert.ok(top.yshift < 0);
  assert.ok(boxOf(left, geo).left >= dotOf(left, geo).x, 'right of the left-edge dot');
  assert.ok(left.xshift > 0);
  assert.ok(boxOf(right, geo).right <= dotOf(right, geo).x, 'left of the right-edge dot');
  assert.ok(right.xshift < 0);
});

test('labels stacked on a plot-edge dot stay inside the plot and within the cap, accepting overlap', () => {
  const geo = geometry();
  const stacked = (x, y) => Array.from({ length: 4 }, (_, i) => ({ label: `Edge ${x}/${y} #${i}`, x, y }));
  const points = [...stacked(100, 50), ...stacked(0, 100), ...stacked(50, 0)];
  const annotations = buildCollisionSafeLabelAnnotations(points, geo);
  assert.equal(annotations.length, 12);
  assertWithinCap(annotations, geo);
  annotations.forEach((annotation) => assertInsidePlot(annotation, geo));
});

test('a crowded small plot keeps every label within the cap instead of compacting them away from their dots', () => {
  const geo = geometry({ width: 300, height: 250, x: { type: 'linear', offset: 50, length: 200, l2p: (v) => v * 2 }, y: { type: 'linear', offset: 50, length: 150, l2p: (v) => 150 - v * 1.5 } });
  let seed = 1;
  const next = () => { seed = (seed * 16807) % 2147483647; return (seed / 2147483647) * 100; };
  const points = Array.from({ length: 12 }, (_, i) => ({ label: `Mdl ${i}`, x: next(), y: next(), frontier: i % 5 === 0 }));
  const annotations = buildCollisionSafeLabelAnnotations(points, geo, { markerRadius: MARKER });
  assert.equal(annotations.length, 12);
  assert.ok(annotations.every((a) => Number.isFinite(a.x) && Number.isFinite(a.y)));
  assertWithinCap(annotations, geo);
});

test('a sparse set of points keeps all labels clear of each other', () => {
  const geo = geometry();
  const points = Array.from({ length: 6 }, (_, i) => ({ label: `Sparse ${i}`, x: 10 + i * 14, y: 20 + (i % 2) * 40 }));
  const annotations = buildCollisionSafeLabelAnnotations(points, geo);
  assertWithinCap(annotations, geo);
  const boxes = annotations.map((a) => boxOf(a, geo));
  for (let i = 0; i < boxes.length; i += 1) for (let j = i + 1; j < boxes.length; j += 1) assert.equal(overlaps(boxes[i], boxes[j]), false, `${i} overlaps ${j}`);
});

const rect = (left, top, w = 40, h = 12) => ({ left, right: left + w, top, bottom: top + h });
const makeIO = (frames, { bounds = { left: 0, right: 1000, top: 0, bottom: 600 }, plot } = {}) => {
  let frame = 0;
  const log = { relayouts: 0, paints: 0 };
  return {
    log,
    readBoxes: () => frames[Math.min(frame, frames.length - 1)].map((entry) => ({ index: entry.index, rect: entry.rect })),
    bounds: () => bounds,
    ...(plot ? { plot: () => plot } : {}),
    relayout: async () => { log.relayouts += 1; frame += 1; },
    waitForPaint: async () => { log.paints += 1; },
  };
};

const PLOT = { left: 100, right: 900, top: 50, bottom: 450 };
const REACH = MARKER + MAX_GAP;
/** Paper coordinates of a pixel position inside a plot rectangle. */
const paperAt = (plot, px, py) => ({ x: (px - plot.left) / (plot.right - plot.left), y: 1 - (py - plot.top) / (plot.bottom - plot.top) });
/** An arrowless label that sits to the right of the dot at (px, py), as the placement pass would leave it. */
const labelAt = (plot, text, px, py, over = {}) => ({
  text, ...paperAt(plot, px, py), xref: 'paper', yref: 'paper', showarrow: false, xanchor: 'left', yanchor: 'middle', xshift: 15, yshift: 0, ...over,
});
const sidePlot = (px, py, w = 40, h = 12) => rect(px + 15, py - h / 2, w, h);
const dotIn = (plot, annotation) => ({ x: plot.left + annotation.x * (plot.right - plot.left), y: plot.top + (1 - annotation.y) * (plot.bottom - plot.top) });
/** Measured boxes that follow the annotations' xshift/yshift as Plotly would re-render them. */
const liveIO = (anns, rects, { plot = PLOT, bounds } = {}) => {
  const base = anns.map((a) => ({ x: a.xshift ?? 0, y: a.yshift ?? 0 }));
  const log = { relayouts: 0, paints: 0 };
  const current = () => rects.map((r, index) => {
    const dx = (anns[index].xshift ?? 0) - base[index].x;
    const dy = -((anns[index].yshift ?? 0) - base[index].y);
    return { index, rect: { left: r.left + dx, right: r.right + dx, top: r.top + dy, bottom: r.bottom + dy } };
  });
  return {
    log,
    current,
    readBoxes: current,
    bounds: () => bounds ?? { left: plot.left - 100, right: plot.right + 100, top: plot.top - 50, bottom: plot.bottom + 100 },
    ...(plot ? { plot: () => plot } : {}),
    relayout: async () => { log.relayouts += 1; },
    waitForPaint: async () => { log.paints += 1; },
  };
};
const assertRepairedWithinCap = (anns, io, plot = PLOT) => io.current().forEach(({ index, rect: box }) => {
  assert.equal(anns[index].showarrow, false, `${anns[index].text} stays arrowless`);
  ['ax', 'ay', 'axref', 'ayref'].forEach((key) => assert.equal(key in anns[index], false, `${anns[index].text} gained ${key}`));
  const gap = distanceToBox(box, dotIn(plot, anns[index])) - MARKER;
  assert.ok(gap <= MAX_GAP + EPS, `${anns[index].text} ended ${gap.toFixed(2)}px from its marker`);
});

test('repair leaves annotations alone when nothing collides or boxes are missing', async () => {
  const anns = [{ text: 'A' }, { text: 'B' }];
  assert.deepEqual(await repairCollisionSafeLabelAnnotations([], makeIO([[]])), []);
  assert.equal(await repairCollisionSafeLabelAnnotations(null, makeIO([[]])), null);
  const clear = makeIO([[{ index: 0, rect: rect(0, 0) }, { index: 1, rect: rect(200, 200) }]]);
  await repairCollisionSafeLabelAnnotations(anns, clear);
  assert.equal(clear.log.relayouts, 0);
  const short = makeIO([[{ index: 0, rect: rect(0, 0) }]]);
  await repairCollisionSafeLabelAnnotations(anns, short);
  assert.equal(short.log.relayouts, 0);
});

test('repair moves only colliding labels with xshift/yshift and never adds a leader line', async () => {
  const anns = [labelAt(PLOT, 'A', 300, 200), labelAt(PLOT, 'B', 310, 204), labelAt(PLOT, 'C', 600, 400)];
  const before = [{ index: 0, rect: sidePlot(300, 200) }, { index: 1, rect: sidePlot(310, 204) }, { index: 2, rect: sidePlot(600, 400) }];
  const untouched = { ...anns[2] };
  const io = liveIO(anns, before.map((entry) => entry.rect));
  await repairCollisionSafeLabelAnnotations(anns, io);
  assert.equal(io.log.relayouts, 1);
  assert.equal(io.log.paints, 1);
  assert.deepEqual(anns[2], untouched, 'a non-colliding label is untouched');
  assert.ok(anns[0].xshift !== 15 || anns[0].yshift !== 0 || anns[1].xshift !== 15 || anns[1].yshift !== 0, 'a colliding label moved');
  assertRepairedWithinCap(anns, io);
  const [one, two] = io.current();
  assert.equal(one.rect.left < two.rect.right + 1 && one.rect.right > two.rect.left - 1 && one.rect.top < two.rect.bottom + 1 && one.rect.bottom > two.rect.top - 1, false, 'the pair is separated');
});

test('old intent: a whole-plot grid repack when conflicts cannot be moved alone; now unresolvable collisions stay within the cap', async () => {
  const anns = [labelAt(PLOT, 'Wide 0', 300, 200, { xshift: 0, yshift: 0 }), labelAt(PLOT, 'Wide 1', 310, 202, { xshift: 0, yshift: 0 }), labelAt(PLOT, 'Small', 800, 400, { xshift: 0, yshift: 0 })];
  const frame = [rect(250, 150, 200, 100), rect(260, 152, 200, 100), rect(520, 400, 40, 12)];
  const io = liveIO(anns, frame);
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPasses: 3, repairPad: 2, repairEdge: 4 });
  assert.equal(io.log.relayouts, 0, 'nothing is moved away from its dot to make room');
  assert.deepEqual(anns.map((a) => [a.xshift, a.yshift]), [[0, 0], [0, 0], [0, 0]]);
});

test('repair gives up when no arrangement fits, and stops when boxes vanish mid-way', async () => {
  const anns = [{ text: 'A' }, { text: 'B' }];
  const crowded = [{ index: 0, rect: rect(0, 0, 900, 500) }, { index: 1, rect: rect(10, 10, 900, 500) }];
  const impossible = makeIO([crowded]);
  await repairCollisionSafeLabelAnnotations(anns, impossible);
  assert.equal(impossible.log.relayouts, 0);
  const placed = [labelAt(PLOT, 'A', 300, 200), labelAt(PLOT, 'B', 310, 204)];
  const vanish = makeIO([[{ index: 0, rect: sidePlot(300, 200) }, { index: 1, rect: sidePlot(310, 204) }], [{ index: 0, rect: sidePlot(300, 200) }]], { plot: PLOT });
  await repairCollisionSafeLabelAnnotations(placed, vanish);
  assert.equal(vanish.log.relayouts, 1);
});

test('repair stops after the pass limit and tolerates a degenerate bottom bound', async () => {
  const anns = [labelAt(PLOT, 'A', 300, 30), labelAt(PLOT, 'B', 310, 34)];
  const same = [{ index: 0, rect: sidePlot(300, 30) }, { index: 1, rect: sidePlot(310, 34) }];
  const io = makeIO([same, same, same], { bounds: { left: 0, right: 1000, top: 0, bottom: 60 } });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPasses: 2 });
  assert.equal(io.log.relayouts, 2);
});

test('repair never moves a label beyond the cap from its dot, even when every nearby candidate collides', async () => {
  const dots = Array.from({ length: 14 }, (_, i) => ({ x: 480 + (i % 3) * 3, y: 240 + (i % 4) * 2 }));
  const anns = dots.map((dot, i) => labelAt(PLOT, `Crowd ${i}`, dot.x, dot.y));
  const io = liveIO(anns, dots.map((dot) => sidePlot(dot.x, dot.y)));
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPasses: 8 });
  assert.ok(io.log.relayouts >= 1, 'something was moved');
  assertRepairedWithinCap(anns, io);
});

test('repair keeps labels near an edge dot inside the plot and within the cap', async () => {
  const dots = [{ x: 108, y: 60 }, { x: 110, y: 64 }, { x: 890, y: 440 }, { x: 888, y: 444 }];
  const anns = dots.map((dot, i) => labelAt(PLOT, `Edge ${i}`, dot.x, dot.y, i < 2 ? { xshift: 15 } : { xshift: -15, xanchor: 'right' }));
  const rects = dots.map((dot, i) => (i < 2 ? sidePlot(dot.x, dot.y) : rect(dot.x - 15 - 40, dot.y - 6)));
  const io = liveIO(anns, rects);
  await repairCollisionSafeLabelAnnotations(anns, io, { repairEdge: 4 });
  assertRepairedWithinCap(anns, io);
  io.current().forEach(({ rect: box }) => assert.ok(box.left >= PLOT.left && box.right <= PLOT.right && box.top >= PLOT.top && box.bottom <= PLOT.bottom));
});

const finalBox = (annotation, before, box) => {
  const dx = annotation.xshift - before.xshift;
  const dy = -(annotation.yshift - before.yshift);
  return { left: box.left + dx, right: box.right + dx, top: box.top + dy, bottom: box.bottom + dy };
};

test('repair flips or clamps measured labels that spill out of the plot, leaving the rest alone', async () => {
  const anns = [
    labelAt(PLOT, 'Flip left', 100, 250, { xshift: -15, xanchor: 'right' }),
    labelAt(PLOT, 'Straddle', 100, 350, { xshift: 3, yshift: -4 }),
    labelAt(PLOT, 'Flip down', 500, 450, { xshift: 0, yshift: -20, xanchor: 'center', yanchor: 'top' }),
    labelAt(PLOT, 'Flip right', 820, 150, { xshift: 20, xanchor: 'left' }),
    labelAt(PLOT, 'Fine', 280, 250),
  ];
  const before = [
    { index: 0, rect: rect(45, 244) },
    { index: 1, rect: rect(70, 344) },
    { index: 2, rect: rect(480, 452) },
    { index: 3, rect: rect(840, 144, 100) },
    { index: 4, rect: sidePlot(280, 250) },
  ];
  const initial = anns.map((a) => ({ xshift: a.xshift, yshift: a.yshift }));
  const clean = before.map((entry, i) => ({ index: i, rect: rect(100 + i * 100, 100) }));
  const io = makeIO([before, clean], { plot: PLOT });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPad: 0 });
  assert.equal(io.log.relayouts, 1);
  assert.equal(anns[0].xshift, -15 + 70, 'flipped to the other side of the point');
  assert.equal(anns[0].yshift, 0);
  assert.equal(anns[1].xshift, 3 + 30, 'a label straddling the edge is clamped');
  assert.equal(anns[1].yshift, -4);
  assert.equal(anns[2].yshift, -20 + 16, 'flipped above the bottom edge (a screen move of -16 is a yshift of +16)');
  assert.equal(anns[2].xshift, 0);
  assert.equal(anns[3].xshift, 20 - 140, 'flipped left of the right edge');
  assert.deepEqual([anns[4].xshift, anns[4].yshift], [15, 0], 'a label inside the plot is untouched');
  anns.slice(0, 4).forEach((annotation, i) => {
    assert.equal(annotation.showarrow, false);
    assert.equal('ax' in annotation, false);
    const box = finalBox(annotation, initial[i], before[i].rect);
    assert.ok(box.left >= PLOT.left && box.right <= PLOT.right && box.top >= PLOT.top && box.bottom <= PLOT.bottom, annotation.text);
    assert.ok(distanceToBox(box, dotIn(PLOT, annotation)) - MARKER <= MAX_GAP + EPS, `${annotation.text} stays within the cap`);
  });
});

test('repair clamps labels wider or taller than the room the mirror image has', async () => {
  const anns = [
    labelAt(PLOT, 'Wide', 500, 120, { xshift: 0, yshift: 0, xanchor: 'center', yanchor: 'bottom' }),
    labelAt(PLOT, 'Tall', 500, 250, { xshift: 20, yshift: 0, yanchor: 'middle' }),
  ];
  const spilled = [{ index: 0, rect: rect(60, 100, 900, 12) }, { index: 1, rect: rect(520, 20, 40, 500) }];
  const io = makeIO([spilled, [{ index: 0, rect: rect(100, 100) }, { index: 1, rect: rect(300, 300) }]], { plot: PLOT });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPad: 0 });
  assert.equal(anns[0].xshift, 40, 'too wide for either side: pinned to the left edge');
  assert.equal(anns[1].yshift, -30, 'too tall for either side: pinned to the top edge (screen +30 is yshift -30)');
});

test('repair leaves a spilling label alone when pulling it inside the plot would still leave it beyond the cap', async () => {
  const anns = [labelAt(PLOT, 'Far', 500, 250, { xshift: 0, yshift: 0, xanchor: 'center', yanchor: 'middle' })];
  const io = makeIO([[{ index: 0, rect: rect(20, 244) }]], { plot: PLOT });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPad: 0 });
  assert.equal(io.log.relayouts, 0);
  assert.deepEqual([anns[0].xshift, anns[0].yshift], [0, 0]);
});

test('repair without a plot rectangle has nothing to clamp to', async () => {
  const legacyAnns = [{ text: 'A', x: 0, y: 0.5, showarrow: false }];
  const legacy = makeIO([[{ index: 0, rect: rect(-20, 244) }]]);
  await repairCollisionSafeLabelAnnotations(legacyAnns, legacy);
  assert.equal(legacy.log.relayouts, 0, 'without a plot rectangle there is nothing to clamp to');
});

test('repair nudges a label that barely spills instead of flipping it across its point', async () => {
  const anns = [labelAt(PLOT, 'Near', 156, 238, { xshift: 0, yshift: 0 })];
  const io = makeIO([[{ index: 0, rect: rect(98, 232) }], [{ index: 0, rect: rect(100, 232) }]], { plot: PLOT });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPad: 0 });
  assert.deepEqual([anns[0].xshift, anns[0].yshift], [2, 0]);
});

test('repair packs colliding labels inside the plot area when one is known', async () => {
  const plot = { left: 100, right: 700, top: 100, bottom: 300 };
  const anns = [labelAt(plot, 'A', 290, 156), labelAt(plot, 'B', 300, 160)];
  const stacked = [{ index: 0, rect: rect(300, 150) }, { index: 1, rect: rect(310, 152) }];
  const io = liveIO(anns, stacked.map((entry) => entry.rect), { plot });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairEdge: 4 });
  assert.equal(io.log.relayouts, 1);
  io.current().forEach(({ rect: box }) => {
    assert.ok(box.left >= plot.left + 4 && box.right <= plot.right - 4 && box.top >= plot.top + 4 && box.bottom <= plot.bottom - 4, JSON.stringify(box));
  });
  assertRepairedWithinCap(anns, io, plot);
});

test('without a plot rectangle the dot is derived from the rendered box and the annotation anchors', async () => {
  // Four colliding labels with every anchor combination; each dot is (400, 300) in screen space.
  const make = (text, xanchor, yanchor, xshift, yshift) => ({ text, showarrow: false, xanchor, yanchor, xshift, yshift });
  const anns = [make('L', 'left', 'middle', 15, 0), make('R', 'right', 'top', -15, -15), make('C', 'center', 'bottom', 0, 15), { text: 'N', showarrow: false, xshift: 5 }];
  const rects = [rect(415, 290, 80, 20), rect(305, 315, 80, 20), rect(360, 265, 80, 20), rect(365, 290, 80, 20)];
  const io = liveIO(anns, rects, { plot: null, bounds: { left: 0, right: 1000, top: 0, bottom: 700 } });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPad: 8 });
  assert.ok(io.log.relayouts >= 1);
  io.current().forEach(({ index, rect: box }) => {
    assert.equal(anns[index].showarrow, false);
    assert.ok(distanceToBox(box, { x: 400, y: 300 }) - MARKER <= MAX_GAP + EPS, `${anns[index].text} stays within the cap`);
  });
  const boxes = io.current().map((entry) => entry.rect);
  assert.ok(boxes.some((box, i) => box !== rects[i] && (box.left !== rects[i].left || box.top !== rects[i].top)), 'at least one label was moved');
});

test('createRepairIO reads annotation text boxes from the rendered SVG', async () => {
  const annotations = [{ text: '<b>A</b>' }, { text: 'B' }];
  const div = createPlotDiv({
    boxes: [
      { text: 'A', rect: { left: 1, right: 11, top: 1, bottom: 5 } },
      { text: 'zzz', rect: { left: 1, right: 11, top: 1, bottom: 5 } },
      { text: 'B', rect: { left: 5, right: 5, top: 1, bottom: 5 } },
    ],
    rect: { left: 0, right: 10, top: 0, bottom: 10 },
  });
  const calls = [];
  const io = createRepairIO(div, annotations, { relayout: (a) => { calls.push(a); return Promise.resolve(); }, raf: (cb) => cb() });
  assert.deepEqual(io.readBoxes(), [{ index: 0, rect: { left: 1, right: 11, top: 1, bottom: 5 } }]);
  assert.deepEqual(io.bounds(), { left: 0, right: 10, top: 0, bottom: 10 });
  assert.deepEqual(io.plot(), { left: 50, right: 850, top: 50, bottom: 550 }, 'the plot area is the figure minus its margins');
  await io.relayout();
  await io.waitForPaint();
  assert.equal(calls[0], annotations);
});
