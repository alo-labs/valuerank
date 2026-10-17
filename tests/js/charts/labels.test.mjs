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

const boxOf = (annotation, geo, fontSize = 9, safety = 1.15) => {
  const px = { x: geo.x.offset + annotation.x * geo.x.length, y: geo.y.offset + (1 - annotation.y) * geo.y.length };
  const lines = labelLines(annotation.text);
  const w = Math.ceil((Math.max(...lines.map((l) => geo.measureText(l))) + 7) * safety);
  const h = Math.ceil((lines.length * fontSize * 1.35 + 5) * safety);
  const ax = annotation.showarrow ? annotation.ax : annotation.xshift;
  const ay = annotation.showarrow ? annotation.ay : annotation.yshift;
  const cx = px.x + ax;
  const cy = px.y + ay;
  const left = annotation.xanchor === 'left' ? cx : annotation.xanchor === 'right' ? cx - w : cx - w / 2;
  const top = annotation.yanchor === 'top' ? cy : annotation.yanchor === 'bottom' ? cy - h : cy - h / 2;
  return { left, right: left + w, top, bottom: top + h };
};
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
  const [a] = buildCollisionSafeLabelAnnotations([{ label: 'Solo', x: 50, y: 50 }], geometry());
  assert.equal(a.showarrow, false);
  assert.equal(a.xref, 'paper');
  assert.ok(Math.abs(a.x - 0.5) < 1e-9 && Math.abs(a.y - 0.5) < 1e-9);
  assert.ok('xshift' in a && !('ax' in a));
  assert.equal(a.font.color, '#0f172a');
  assert.equal(a.align, a.xanchor === 'right' ? 'right' : a.xanchor === 'center' ? 'center' : 'left');
});

test('log axes map values through log10 and frontier/dark colours apply', () => {
  const geo = geometry({ dark: true, x: { type: 'log', offset: 50, length: 800, l2p: (v) => (v + 2) * 100 } });
  const [a, b] = buildCollisionSafeLabelAnnotations([{ label: 'F', x: 10, y: 50, frontier: true }, { label: 'N', x: 1000, y: 10 }], geo);
  assert.equal(a.font.color, '#34d399');
  assert.equal(a.arrowcolor, 'rgba(52,211,153,.95)');
  assert.equal(b.font.color, '#e2e8f0');
  assert.equal(b.arrowcolor, 'rgba(148,163,184,.75)');
  assert.ok(Math.abs(a.x - (300 / 800)) < 1e-9);
});

test('custom colours and options override the defaults; estimate works without measureText', () => {
  const geo = geometry({ measureText: undefined });
  const [a] = buildCollisionSafeLabelAnnotations([{ label: 'Two<br>lines', x: 50, y: 50, frontier: true }, { label: 'Z', x: 1, y: 1 }], geo, {
    fontSize: 12, safety: 1.5, markerRadius: 5, labelPad: 2, labelGap: 2, adjacentRadius: 9, radii: [30, 'x'], candidateStep: 10,
    textColor: 'red', frontierColor: 'green', arrowMuted: 'a', arrowFrontier: 'b',
  });
  assert.equal(a.font.size, 12);
  assert.equal(a.font.color, 'green');
  assert.equal(a.arrowcolor, 'b');
  const [b] = buildCollisionSafeLabelAnnotations([{ label: 'Q', x: 50, y: 50 }], geo, { textColor: 'red' });
  assert.equal(b.font.color, 'red');
});

test('dense clusters end up with non-overlapping labels that keep their points connected', () => {
  const geo = geometry();
  const points = Array.from({ length: 14 }, (_, i) => ({ label: `Model ${i}`, x: 40 + (i % 4), y: 40 + Math.floor(i / 4), frontier: i % 5 === 0 }));
  const annotations = buildCollisionSafeLabelAnnotations(points, geo, { markerRadius: 11 });
  assert.equal(annotations.length, points.length);
  const boxes = annotations.map((a) => boxOf(a, geo));
  for (let i = 0; i < boxes.length; i += 1) for (let j = i + 1; j < boxes.length; j += 1) assert.equal(overlaps(boxes[i], boxes[j]), false, `${i} overlaps ${j}`);
  assert.ok(annotations.some((a) => a.showarrow), 'crowded labels use leader lines');
  assert.ok(annotations.some((a) => !a.showarrow), 'free labels stay adjacent');
});

test('points at the chart edge and stacked duplicates still produce an annotation each', () => {
  const geo = geometry({ width: 120, height: 90 });
  const points = [{ label: 'Corner', x: 0, y: 100 }, { label: 'Corner2', x: 0, y: 100 }, { label: 'Far', x: 99, y: 0 }, { label: 'Far2', x: 99, y: 0 }, { label: 'Far3', x: 99, y: 0 }];
  const annotations = buildCollisionSafeLabelAnnotations(points, geo);
  assert.equal(annotations.length, 5);
});

test('near-edge placement spills are costed when no in-bounds slot exists', () => {
  const geo = geometry({ width: 20, height: 12 });
  const annotations = buildCollisionSafeLabelAnnotations([{ label: 'Huge label that cannot fit', x: 2, y: 100 }, { label: 'Other huge label here', x: 3, y: 100 }], geo);
  assert.equal(annotations.length, 2);
});

const rect = (left, top, w = 40, h = 12) => ({ left, right: left + w, top, bottom: top + h });
const makeIO = (frames, { bounds = { left: 0, right: 1000, top: 0, bottom: 600 } } = {}) => {
  let frame = 0;
  const log = { relayouts: 0, paints: 0 };
  return {
    log,
    readBoxes: () => frames[Math.min(frame, frames.length - 1)].map((entry) => ({ index: entry.index, rect: entry.rect })),
    bounds: () => bounds,
    relayout: async () => { log.relayouts += 1; frame += 1; },
    waitForPaint: async () => { log.paints += 1; },
  };
};

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

test('repair moves only colliding labels and keeps the point connection', async () => {
  const anns = [
    { text: 'A', showarrow: false, xshift: 4, yshift: -3 },
    { text: 'B', showarrow: true, ax: 10, ay: 20 },
    { text: 'C', showarrow: false },
  ];
  const before = [{ index: 0, rect: rect(100, 100) }, { index: 1, rect: rect(110, 102) }, { index: 2, rect: rect(500, 400) }];
  const after = [{ index: 0, rect: rect(100, 100) }, { index: 1, rect: rect(300, 100) }, { index: 2, rect: rect(500, 400) }];
  const io = makeIO([before, after]);
  await repairCollisionSafeLabelAnnotations(anns, io);
  assert.equal(io.log.relayouts, 1);
  assert.equal(io.log.paints, 1);
  assert.equal(anns[2].showarrow, false, 'non-colliding label untouched');
  const moved = anns.slice(0, 2);
  assert.ok(moved.every((a) => a.showarrow === true && 'ax' in a));
  assert.equal(anns[0].xshift, 0);
  assert.equal(anns[0].axref, 'pixel');
});

test('repair falls back to a full grid when conflicting labels cannot be moved alone', async () => {
  const anns = Array.from({ length: 3 }, (_, i) => ({ text: String(i), showarrow: false }));
  const frame = [{ index: 0, rect: rect(100, 100, 400, 190) }, { index: 1, rect: rect(110, 102, 400, 190) }, { index: 2, rect: rect(520, 400, 40, 12) }];
  const io = makeIO([frame, [{ index: 0, rect: rect(0, 0) }, { index: 1, rect: rect(100, 0) }, { index: 2, rect: rect(200, 0) }]], { bounds: { left: 0, right: 700, top: 0, bottom: 640 } });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairColumns: 3, repairPasses: 2, repairPad: 2, repairEdge: 4, repairBottom: 30 });
  assert.ok(io.log.relayouts >= 1);
});

test('repair gives up when no arrangement fits, and stops when boxes vanish mid-way', async () => {
  const anns = [{ text: 'A' }, { text: 'B' }];
  const crowded = [{ index: 0, rect: rect(0, 0, 900, 500) }, { index: 1, rect: rect(10, 10, 900, 500) }];
  const impossible = makeIO([crowded]);
  await repairCollisionSafeLabelAnnotations(anns, impossible);
  assert.equal(impossible.log.relayouts, 0);
  const vanish = makeIO([[{ index: 0, rect: rect(100, 100) }, { index: 1, rect: rect(110, 102) }], [{ index: 0, rect: rect(100, 100) }]]);
  await repairCollisionSafeLabelAnnotations(anns, vanish);
  assert.equal(vanish.log.relayouts, 1);
});

test('repair stops after the pass limit and tolerates a degenerate bottom bound', async () => {
  const anns = [{ text: 'A', showarrow: true }, { text: 'B', showarrow: true }];
  const same = [{ index: 0, rect: rect(100, 100) }, { index: 1, rect: rect(110, 102) }];
  const io = makeIO([same, same, same], { bounds: { left: 0, right: 1000, top: 0, bottom: 60 } });
  await repairCollisionSafeLabelAnnotations(anns, io, { repairPasses: 2 });
  assert.equal(io.log.relayouts, 2);
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
  await io.relayout();
  await io.waitForPaint();
  assert.equal(calls[0], annotations);
});
