"""Shared ValueRank static-site header template and injector."""

from __future__ import annotations

import html
import re
from pathlib import Path


HEADER_CSS = r"""
/* Shared ValueRank header: keep this block identical across publication pages. */
.vr-site-header {
  position: fixed; inset: 0 0 auto 0; z-index: 1000; height: 64px;
  display: flex; align-items: center; gap: 18px; padding: 0 24px;
  background: var(--nav-bg, rgba(248,249,252,.94));
  border-bottom: 1px solid var(--border, #e2e8f0);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  color: var(--text-primary, #0f172a);
}
.vr-site-header a { color: inherit; }
.vr-nav-brand { display: flex; align-items: center; flex-shrink: 0; }
.vr-nav-brand-link { display: flex; align-items: center; gap: 10px; text-decoration: none; }
.vr-nav-logo { font-weight: 800; letter-spacing: -.02em; font-size: 1.1rem; }
.vr-nav-badge { padding: 2px 8px; border-radius: 999px; background: var(--accent, #4f46e5); color: #fff; font: 600 11px/1.5 var(--font-mono, 'IBM Plex Mono', monospace); }
.vr-mode-switcher { display: flex; align-items: center; gap: 4px; }
.vr-mode-btn { padding: 6px 10px; border-radius: 8px; color: var(--text-secondary, #475569); text-decoration: none; font-size: 13px; white-space: nowrap; }
.vr-mode-btn:hover, .vr-mode-btn:focus-visible { background: var(--accent-a08, rgba(79,70,229,.08)); color: var(--accent, #4f46e5); }
.vr-mode-btn.active { background: var(--accent-a12, rgba(79,70,229,.12)); color: var(--accent, #4f46e5); font-weight: 700; }
.vr-nav-links { display: flex; align-items: center; gap: 14px; margin-left: auto; }
.vr-nav-links a { color: var(--text-secondary, #475569); font-size: 12px; text-decoration: none; }
.vr-nav-links a:hover, .vr-nav-links a:focus-visible { color: var(--accent, #4f46e5); }
.vr-nav-meta { color: var(--text-dim, #94a3b8); font-size: 11px; white-space: nowrap; }
.vr-theme-toggle { width: 32px; height: 32px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; border: 1px solid var(--border, #e2e8f0); border-radius: 8px; background: transparent; color: var(--text-secondary, #475569); cursor: pointer; }
.vr-theme-toggle svg { width: 16px; height: 16px; }
.vr-theme-toggle .icon-moon { display: none; }
[data-theme="dark"] .vr-theme-toggle .icon-sun { display: none; }
[data-theme="dark"] .vr-theme-toggle .icon-moon { display: block; }
@media (max-width: 1180px) { .vr-nav-links { display: none; } }
@media (max-width: 820px) { .vr-site-header { gap: 8px; padding: 0 14px; } .vr-mode-switcher { overflow-x: auto; } .vr-mode-btn { padding-inline: 7px; } .vr-nav-meta { display: none; } }
.vr-sortable thead th { cursor: pointer; user-select: none; }
.vr-sortable thead th:hover, .vr-sortable thead th:focus-visible { color: var(--accent, #4f46e5); }
.vr-sortable thead th[aria-sort="ascending"], .vr-sortable thead th[aria-sort="descending"] { color: var(--accent, #4f46e5); }
.vr-sort-indicator { display: inline-block; margin-left: 4px; color: var(--text-dim, #94a3b8); font-size: .9em; }
"""


TABLE_SORT_JS = r"""
(function () {
  function parseNumeric(raw) {
    const text = String(raw || '').replace(/\u00a0/g, ' ').replace(/,/g, '').trim();
    if (!text || /^[-—–]$/.test(text)) return null;
    const match = text.match(/^(?:[$#]\s*)?(-?(?:\d+(?:\.\d+)?|\.\d+))(?:\s*([KMB]))?(?:\s*%|\s*±.*|\s+(?:new|tokens?)|\s*[▲▼])?$/i);
    if (!match) return null;
    const multiplier = { K: 1e3, M: 1e6, B: 1e9 }[(match[2] || '').toUpperCase()] || 1;
    return Number(match[1]) * multiplier;
  }

  function cellValue(cell) {
    const raw = cell?.dataset.sortValue ?? cell?.textContent ?? '';
    const numeric = parseNumeric(raw);
    return numeric == null ? { kind: 'text', value: String(raw).trim().toLocaleLowerCase() } : { kind: 'number', value: numeric };
  }

  function updateIndicators(headers, activeIndex, direction) {
    headers.forEach((header, index) => {
      const active = index === activeIndex;
      header.setAttribute('aria-sort', active ? (direction === 1 ? 'ascending' : 'descending') : 'none');
      const indicator = header.querySelector('.vr-sort-indicator');
      if (indicator) indicator.textContent = active ? (direction === 1 ? '↑' : '↓') : '↕';
    });
  }

  function sortTable(table, headers, index) {
    const body = table.tBodies[0];
    if (!body) return;
    const prior = table._vrSortState;
    const direction = prior && prior.index === index ? -prior.direction : 1;
    const rows = Array.from(body.rows).map((row, originalIndex) => ({ row, originalIndex, value: cellValue(row.cells[index]) }));
    const isEmpty = value => value === '' || value === '—' || value === '–';
    const numericColumn = rows.some(item => item.value.kind === 'number') && rows.every(item => item.value.kind === 'number' || isEmpty(item.value.value));
    rows.sort((left, right) => {
      const leftEmpty = left.value.value === '' || left.value.value === '—' || left.value.value === '–';
      const rightEmpty = right.value.value === '' || right.value.value === '—' || right.value.value === '–';
      if (leftEmpty || rightEmpty) {
        if (leftEmpty && rightEmpty) return left.originalIndex - right.originalIndex;
        return leftEmpty ? 1 : -1;
      }
      const comparison = numericColumn
        ? left.value.value - right.value.value
        : String(left.value.value).localeCompare(String(right.value.value), undefined, { numeric: true, sensitivity: 'base' });
      return comparison === 0 ? left.originalIndex - right.originalIndex : direction * comparison;
    });
    rows.forEach(item => body.appendChild(item.row));
    table._vrSortState = { index, direction };
    updateIndicators(headers, index, direction);
  }

  function prepareTable(table) {
    if (table.dataset.vrTableSortReady === 'true' || table.dataset.vrSortable === 'false') return;
    // The primary ranking table has a richer sorter for filters and the cost slider.
    if (table.querySelector('thead th[data-col]')) return;
    const headerRow = table.tHead?.rows[table.tHead.rows.length - 1];
    const body = table.tBodies[0];
    const headers = headerRow ? Array.from(headerRow.cells).filter(cell => cell.tagName === 'TH') : [];
    if (!body || !headers.length) return;
    table.dataset.vrTableSortReady = 'true';
    table.classList.add('vr-sortable');
    headers.forEach((header, index) => {
      header.setAttribute('tabindex', '0');
      header.setAttribute('role', 'button');
      header.setAttribute('aria-sort', 'none');
      const indicator = document.createElement('span');
      indicator.className = 'vr-sort-indicator';
      indicator.setAttribute('aria-hidden', 'true');
      indicator.textContent = '↕';
      header.appendChild(indicator);
      const activate = () => sortTable(table, headers, index);
      header.addEventListener('click', activate);
      header.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          activate();
        }
      });
    });
  }

  function init() {
    document.querySelectorAll('table').forEach(prepareTable);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
}());
"""


CHART_LABEL_JS = r"""
// Shared collision-safe model-label placement for Plotly scatter charts.
// Callers pass data-space points; the helper handles linear and logarithmic axes.
function buildCollisionSafeLabelAnnotations(points, gd, options) {
  options = options || {};
  if (!gd || !gd._fullLayout || !Array.isArray(points) || !points.length) return [];

  const layout = gd._fullLayout;
  const xa = layout[options.xaxis || 'xaxis'];
  const ya = layout[options.yaxis || 'yaxis'];
  if (!xa || !ya || !xa._length || !ya._length) return [];

  const width = layout.width || 1100;
  const height = layout.height || 520;
  const fontSize = Number(options.fontSize) || 9;
  const safety = Number(options.safety) || 1.15;
  const markerRadius = Number(options.markerRadius) || 11;
  const labelPad = Number(options.labelPad) || Math.max(4, fontSize * 0.55);
  const labelGap = Number(options.labelGap) || Math.max(3, fontSize * 0.45);
  const adjacentRadius = Number(options.adjacentRadius) || markerRadius + labelGap;
  const dark = document.documentElement.getAttribute('data-theme') === 'dark';
  const textColor = options.textColor || (dark ? '#e2e8f0' : '#0f172a');
  const frontierColor = options.frontierColor || (dark ? '#34d399' : '#047857');
  const arrowMuted = options.arrowMuted || (dark ? 'rgba(148,163,184,.75)' : 'rgba(71,85,105,.7)');
  const arrowFrontier = options.arrowFrontier || (dark ? 'rgba(52,211,153,.95)' : 'rgba(4,120,87,.85)');
  const clamp = (value, low, high) => Math.max(low, Math.min(high, value));
  const axisCoordinate = (axis, value) => {
    const numeric = Number(value);
    if (!Number.isFinite(numeric) || (axis.type === 'log' && numeric <= 0)) return NaN;
    return axis.type === 'log' ? axis.l2p(Math.log10(numeric)) : axis.l2p(numeric);
  };
  const labelLines = value => String(value == null ? '' : value)
    .replace(/<br\s*\/?\s*>/gi, '\n')
    .replace(/<[^>]*>/g, '')
    .split('\n');
  const textMeasure = (() => {
    try {
      const canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');
      if (context) {
        context.font = `${fontSize}px IBM Plex Sans, sans-serif`;
        return context;
      }
    } catch (_) {}
    return null;
  })();
  const estimateLabelSize = label => {
    const lines = labelLines(label);
    const maxChars = Math.max(1, ...lines.map(line => line.length));
    const measuredWidth = textMeasure ? Math.max(...lines.map(line => textMeasure.measureText(line).width)) : maxChars * fontSize * 0.6;
    const wPx = Math.ceil((measuredWidth + 7) * safety);
    const hPx = Math.ceil((lines.length * fontSize * 1.35 + 5) * safety);
    return { wPx, hPx };
  };

  const items = points.map((point, idx) => {
    const label = point.label == null ? (point.name == null ? '' : point.name) : point.label;
    const xPx = xa._offset + axisCoordinate(xa, point.x);
    const yPx = ya._offset + axisCoordinate(ya, point.y);
    const valid = label !== '' && Number.isFinite(xPx) && Number.isFinite(yPx);
    if (!valid) return null;
    return {
      idx,
      point,
      label,
      onFront: Boolean(point.frontier || point.onFront),
      px: { x: xPx, y: yPx },
      paper: {
        x: (xPx - xa._offset) / xa._length,
        y: 1 - (yPx - ya._offset) / ya._length,
      },
      size: estimateLabelSize(label),
    };
  }).filter(Boolean);

  const directions = Array.from({ length: 24 }, (_, index) => {
    const angle = -Math.PI / 2 + index * Math.PI / 12;
    const ux = Math.cos(angle);
    const uy = Math.sin(angle);
    return {
      ux,
      uy,
      xa: ux > 0.18 ? 'left' : ux < -0.18 ? 'right' : 'center',
      ya: uy > 0.18 ? 'top' : uy < -0.18 ? 'bottom' : 'middle',
    };
  });
  const radiusSteps = [0, 4, 8, 14, 22, 32, 46, 64, 86, 114, 148, 190, 240, 300, 380];
  const requestedRadii = Array.isArray(options.radii) ? options.radii : [];
  const radii = [...new Set([
    ...radiusSteps.map(step => adjacentRadius + step),
    ...requestedRadii.map(radius => Math.max(adjacentRadius, Number(radius))),
  ].filter(Number.isFinite))].sort((left, right) => left - right);
  const candidateStep = Math.max(6, Number(options.candidateStep) || 8);
  const maxCandidateRadius = Math.max(...radii, adjacentRadius + 160);
  const candidateOffsets = [];
  const addCandidateOffset = (ax, ay, xa, ya) => {
    const radius = Math.hypot(ax, ay);
    if (Number.isFinite(radius) && radius >= adjacentRadius - 1 && radius <= maxCandidateRadius + 1) {
      candidateOffsets.push({ ax, ay, xa, ya, radius });
    }
  };
  radii.forEach(radius => directions.forEach(direction => addCandidateOffset(
    direction.ux * radius,
    direction.uy * radius,
    direction.xa,
    direction.ya,
  )));
  for (let ax = -maxCandidateRadius; ax <= maxCandidateRadius; ax += candidateStep) {
    for (let ay = -maxCandidateRadius; ay <= maxCandidateRadius; ay += candidateStep) {
      const radius = Math.hypot(ax, ay);
      if (radius < adjacentRadius - 1 || radius > maxCandidateRadius) continue;
      addCandidateOffset(
        ax,
        ay,
        ax > candidateStep * 0.35 ? 'left' : ax < -candidateStep * 0.35 ? 'right' : 'center',
        ay > candidateStep * 0.35 ? 'top' : ay < -candidateStep * 0.35 ? 'bottom' : 'middle',
      );
    }
  }
  candidateOffsets.sort((left, right) => left.radius - right.radius);

  items.forEach(item => {
    item.isolation = items.reduce((nearest, other) => {
      if (other.idx === item.idx) return nearest;
      return Math.min(nearest, Math.hypot(item.px.x - other.px.x, item.px.y - other.px.y));
    }, Infinity);
  });
  const priorityOrder = (left, right) => {
    if (left.onFront !== right.onFront) return left.onFront ? -1 : 1;
    return left.isolation - right.isolation || left.label.localeCompare(right.label);
  };

  function labelBox(pointX, pointY, ax, ay, labelWidth, labelHeight, xanchor, yanchor) {
    const anchorX = pointX + ax;
    const anchorY = pointY + ay;
    let left;
    let right;
    let top;
    let bottom;
    if (xanchor === 'left') { left = anchorX; right = anchorX + labelWidth; }
    else if (xanchor === 'right') { right = anchorX; left = anchorX - labelWidth; }
    else { left = anchorX - labelWidth / 2; right = anchorX + labelWidth / 2; }
    if (yanchor === 'top') { top = anchorY; bottom = anchorY + labelHeight; }
    else if (yanchor === 'bottom') { bottom = anchorY; top = anchorY - labelHeight; }
    else { top = anchorY - labelHeight / 2; bottom = anchorY + labelHeight / 2; }
    return { left, right, top, bottom };
  }
  function overlapsLabels(box, placed, skipIndex) {
    return placed.some((placedItem, index) => {
      if (skipIndex != null && index === skipIndex) return false;
      return !(box.right + labelPad < placedItem.box.left ||
        box.left - labelPad > placedItem.box.right ||
        box.bottom + labelPad < placedItem.box.top ||
        box.top - labelPad > placedItem.box.bottom);
    });
  }
  function pointGap(box, point) {
    const nearestX = clamp(point.x, box.left, box.right);
    const nearestY = clamp(point.y, box.top, box.bottom);
    return Math.hypot(point.x - nearestX, point.y - nearestY);
  }
  function markerPenalty(box, ownIndex) {
    return items.reduce((penalty, item) => {
      const nearestX = clamp(item.px.x, box.left, box.right);
      const nearestY = clamp(item.px.y, box.top, box.bottom);
      const distance = Math.hypot(item.px.x - nearestX, item.px.y - nearestY);
      return penalty + (distance < markerRadius ? (markerRadius - distance + 1) : 0);
    }, 0);
  }
  function inBounds(box) {
    return box.left >= 2 && box.right <= width - 2 && box.top >= 2 && box.bottom <= height - 2;
  }
  function spillCost(box) {
    return Math.max(0, 2 - box.left) + Math.max(0, box.right - (width - 2)) +
      Math.max(0, 2 - box.top) + Math.max(0, box.bottom - (height - 2));
  }
  function overlapArea(left, right) {
    const widthOverlap = Math.max(0, Math.min(left.right, right.right) - Math.max(left.left, right.left));
    const heightOverlap = Math.max(0, Math.min(left.bottom, right.bottom) - Math.max(left.top, right.top));
    return widthOverlap * heightOverlap;
  }
  function findPlacement(item, placed, skipIndex) {
    let bestValid = null;
    let bestInvalid = null;
    let firstCandidate = null;
    for (const offset of candidateOffsets) {
      if (bestValid && offset.radius > bestValid.gap + 10) break;
      const { ax, ay, xa, ya, radius } = offset;
      const box = labelBox(item.px.x, item.px.y, ax, ay, item.size.wPx, item.size.hPx, xa, ya);
      const gap = pointGap(box, item.px);
      const inChart = inBounds(box);
      const labelOverlap = placed.reduce((total, placedItem, index) => {
        if (skipIndex != null && index === skipIndex) return total;
        return total + overlapArea(box, placedItem.box);
      }, 0);
      const labelClear = inChart && !overlapsLabels(box, placed, skipIndex);
      const markerCost = labelClear ? markerPenalty(box, item.idx) : 0;
      const valid = labelClear && markerCost === 0;
      const candidate = {
        ax, ay, xa, ya, box, gap, radius,
        adjacent: gap <= adjacentRadius + 1,
        score: gap + radius * 0.01,
      };
      if (!firstCandidate) firstCandidate = candidate;
      if (valid) {
        if (!bestValid || candidate.score < bestValid.score) bestValid = candidate;
      } else {
        candidate.score = labelOverlap * 1000 + markerCost * 100 + (inChart ? 0 : spillCost(box) * 10) + gap + radius * 0.01;
        if (!bestInvalid || candidate.score < bestInvalid.score) bestInvalid = candidate;
      }
    }
    return bestValid || bestInvalid || firstCandidate;
  }

  function placeInOrder(order) {
    const placed = [];
    order.forEach(item => placed.push({ item, ...findPlacement(item, placed, null) }));
    // Greedy placement establishes a safe arrangement; compaction then lets
    // later labels use an open near-point slot blocked by an earlier choice.
    for (let pass = 0; pass < 8; pass += 1) {
      let changed = false;
      for (let index = 0; index < placed.length; index += 1) {
        const current = placed[index];
        const next = findPlacement(current.item, placed, index);
        const currentGap = Number.isFinite(current.gap) ? current.gap : Infinity;
        if (next && (next.gap < currentGap - 0.25 ||
          (Math.abs(next.gap - currentGap) <= 0.25 && next.radius < current.radius))) {
          placed[index] = { item: current.item, ...next };
          changed = true;
        } else if (overlapsLabels(current.box, placed, index) || markerPenalty(current.box, current.item.idx) !== 0) {
          placed[index] = { item: current.item, ...next };
          changed = true;
        }
      }
      if (!changed) break;
    }
    return placed;
  }
  function arrangementScore(placed) {
    const gaps = placed.map(entry => Number.isFinite(entry.gap) ? entry.gap : maxCandidateRadius);
    const maxGap = Math.max(...gaps);
    const invalid = placed.reduce((count, entry, index) => count +
      (overlapsLabels(entry.box, placed, index) || markerPenalty(entry.box, entry.item.idx) !== 0 ? 1 : 0), 0);
    return gaps.reduce((total, gap) => total + gap * gap, 0) + maxGap * maxGap * 2 + invalid * 1e9;
  }
  const orderings = [
    items.slice().sort(priorityOrder),
    items.slice().sort((left, right) => right.isolation - left.isolation || left.label.localeCompare(right.label)),
    items.slice().sort((left, right) => left.px.x - right.px.x || left.px.y - right.px.y || left.label.localeCompare(right.label)),
    items.slice().sort((left, right) => left.px.y - right.px.y || left.px.x - right.px.x || left.label.localeCompare(right.label)),
  ];
  let placed = null;
  let bestScore = Infinity;
  orderings.forEach(order => {
    const candidate = placeInOrder(order);
    const score = arrangementScore(candidate);
    if (!placed || score < bestScore) {
      placed = candidate;
      bestScore = score;
    }
  });

  return placed.map(({ item, ax, ay, xa, ya, adjacent }) => ({
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
    align: xa === 'right' ? 'right' : xa === 'center' ? 'center' : 'left',
    xanchor: xa,
    yanchor: ya,
    font: {
      size: fontSize,
      color: item.onFront ? frontierColor : textColor,
      family: 'IBM Plex Sans, sans-serif',
    },
    bgcolor: 'rgba(0,0,0,0)',
    bordercolor: 'rgba(0,0,0,0)',
    borderwidth: 0,
    borderpad: 0,
    captureevents: false,
    ...(adjacent ? { xshift: ax, yshift: ay } : {
      ax, ay, axref: 'pixel', ayref: 'pixel',
    }),
  }));
}

// Plotly's text metrics can differ from the estimates above after the web font
// loads. Measure the rendered SVG labels once and repack only the labels that
// still collide, keeping the normal point-adjacent placement whenever possible.
async function repairCollisionSafeLabelAnnotations(gd, annotations, options) {
  options = options || {};
  if (!gd || !Array.isArray(annotations) || !annotations.length || typeof Plotly === 'undefined') return annotations;

  const normalize = value => String(value == null ? '' : value)
    .replace(/<br\s*\/?\s*>/gi, '')
    .replace(/<[^>]*>/g, '')
    .replace(/\s+/g, ' ')
    .trim();
  const annotationIndex = new Map();
  annotations.forEach((annotation, index) => annotationIndex.set(normalize(annotation.text), index));
  const readBoxes = () => [...gd.querySelectorAll('g.annotation text')]
    .map(node => {
      const index = annotationIndex.get(normalize(node.textContent));
      if (index == null) return null;
      const rect = node.getBoundingClientRect();
      return { index, rect: { left: rect.left, right: rect.right, top: rect.top, bottom: rect.bottom } };
    })
    .filter(item => item && item.rect.right > item.rect.left && item.rect.bottom > item.rect.top);
  const intersects = (left, right, padding) => left.left < right.right + padding && left.right > right.left - padding &&
    left.top < right.bottom + padding && left.bottom > right.top - padding;
  const overlapPairs = boxes => {
    const pairs = [];
    for (let left = 0; left < boxes.length; left += 1) {
      for (let right = left + 1; right < boxes.length; right += 1) {
        if (intersects(boxes[left].rect, boxes[right].rect, Number(options.repairPad) || 1)) {
          pairs.push([boxes[left], boxes[right]]);
        }
      }
    }
    return pairs;
  };
  const waitForPaint = () => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  let boxes = readBoxes();
  if (boxes.length < annotations.length) return annotations;
  const maxPasses = Number(options.repairPasses) || 5;
  const directions = Array.from({ length: 16 }, (_, index) => {
    const angle = -Math.PI / 2 + index * Math.PI / 8;
    return { x: Math.cos(angle), y: Math.sin(angle) };
  });
  const distances = [0, 4, 10, 16, 24, 34, 48, 68, 96, 132, 174, 224, 284, 352];

  for (let pass = 0; pass < maxPasses; pass += 1) {
    const pairs = overlapPairs(boxes);
    if (!pairs.length) return annotations;
    const conflicting = new Set(pairs.flatMap(pair => pair.map(item => item.index)));
    const rect = gd.getBoundingClientRect();
    const edge = Number(options.repairEdge) || 6;
    const bounds = { left: rect.left + edge, right: rect.right - edge, top: rect.top + edge, bottom: rect.bottom - (Number(options.repairBottom) || 58) };
    if (bounds.bottom <= bounds.top) bounds.bottom = rect.bottom - edge;
    const boxesByIndex = new Map(boxes.map(item => [item.index, item]));
    const maxLabelWidth = Math.max(...boxes.map(item => item.rect.right - item.rect.left));
    const naturalColumns = Math.ceil(Math.sqrt(boxes.length * (bounds.right - bounds.left) / Math.max(1, bounds.bottom - bounds.top)));
    const widthColumns = Math.max(2, Math.floor((bounds.right - bounds.left + 10) / Math.max(1, maxLabelWidth + 10)));
    const gridColumns = Number(options.repairColumns) || Math.min(8, Math.max(2, Math.min(naturalColumns, widthColumns)));
    const gridRows = Math.ceil(boxes.length / gridColumns);
    const cellWidth = (bounds.right - bounds.left) / gridColumns;
    const cellHeight = (bounds.bottom - bounds.top) / gridRows;
    function gridCandidates(box) {
      const candidates = [];
      for (let row = 0; row < gridRows; row += 1) {
        for (let column = 0; column < gridColumns; column += 1) {
          const cellLeft = bounds.left + column * cellWidth;
          const cellTop = bounds.top + row * cellHeight;
          candidates.push({
            left: cellLeft + Math.max(2, (cellWidth - (box.right - box.left)) / 2),
            top: cellTop + Math.max(2, (cellHeight - (box.bottom - box.top)) / 2),
          });
        }
      }
      return candidates;
    }
    function candidatesFor(box) {
      const width = box.rect.right - box.rect.left;
      const height = box.rect.bottom - box.rect.top;
      const candidates = [{ left: box.rect.left, top: box.rect.top }];
      directions.forEach(direction => distances.slice(1).forEach(distance => candidates.push({
        left: box.rect.left + direction.x * distance,
        top: box.rect.top + direction.y * distance,
      })));
      gridCandidates({ right: box.rect.left + width, bottom: box.rect.top + height }).forEach(candidate => candidates.push(candidate));
      return candidates.map(candidate => ({
        left: candidate.left,
        right: candidate.left + width,
        top: candidate.top,
        bottom: candidate.top + height,
      }));
    }
    function inBounds(candidate) {
      return candidate.left >= bounds.left && candidate.right <= bounds.right && candidate.top >= bounds.top && candidate.bottom <= bounds.bottom;
    }
    function place(items, reserved) {
      const placed = reserved.map(item => item.rect);
      const targets = new Map();
      for (const item of items) {
        const candidate = candidatesFor(item).find(box => inBounds(box) && !placed.some(other => intersects(box, other, Number(options.repairPad) || 1)));
        if (!candidate) return null;
        targets.set(item.index, candidate);
        placed.push(candidate);
      }
      return targets;
    }

    const movable = boxes.filter(item => conflicting.has(item.index)).sort((left, right) => left.index - right.index);
    const reserved = boxes.filter(item => !conflicting.has(item.index));
    let targets = place(movable, reserved);
    if (!targets || targets.size !== movable.length) {
      targets = place(boxes.slice().sort((left, right) => left.index - right.index), []);
    }
    if (!targets) return annotations;
    targets.forEach((target, index) => {
      const current = boxesByIndex.get(index);
      if (!current) return;
      const annotation = annotations[index];
      const deltaX = target.left - current.rect.left;
      const deltaY = target.top - current.rect.top;
      if (annotation.showarrow === false) {
        // A rendered collision means the adjacent, arrowless slot was not
        // sufficient; preserve the point connection while moving the label.
        annotation.ax = (Number(annotation.xshift) || 0) + deltaX;
        annotation.ay = (Number(annotation.yshift) || 0) + deltaY;
        annotation.xshift = 0;
        annotation.yshift = 0;
        annotation.xref = annotation.xref || 'paper';
        annotation.yref = annotation.yref || 'paper';
        annotation.axref = 'pixel';
        annotation.ayref = 'pixel';
        annotation.showarrow = true;
      } else {
        annotation.ax = Number(annotation.ax) || 0;
        annotation.ay = Number(annotation.ay) || 0;
        annotation.ax += deltaX;
        annotation.ay += deltaY;
      }
    });
    await Plotly.relayout(gd, { annotations });
    await waitForPaint();
    boxes = readBoxes();
    if (boxes.length < annotations.length) return annotations;
  }
  return annotations;
}
"""


def render_header(active: str, meta: str, badge: str = "v1.4.0") -> str:
    """Render the one shared header structure used by all ValueRank pages."""

    active = html.escape(active, quote=True)
    meta = html.escape(meta)
    badge = html.escape(badge)
    modes = [
        ("llm", "/", "LLM Models"),
        ("coding", "/coding-agents/", "Coding Agents"),
        ("tb4", "/tb4/", "TB 4"),
    ]
    mode_links = "\n".join(
        f'    <a class="vr-mode-btn{" active" if active == key else ""}" href="{href}">{label}</a>'
        for key, href, label in modes
    )
    return f'''<nav class="vr-site-header" data-vr-shared-header="true">
  <div class="vr-nav-brand">
    <a class="vr-nav-brand-link" href="/">
      <span class="vr-nav-logo">ValueRank</span>
      <span class="vr-nav-badge">{badge}</span>
    </a>
  </div>
  <div class="vr-mode-switcher">
{mode_links}
  </div>
  <div class="vr-nav-links nav-links">
    <a href="/#rankings">Rankings</a>
    <a href="/#charts">Charts</a>
    <a href="/#methodology">Methodology</a>
    <a href="/#data">Data</a>
    <a href="/#faq">FAQ</a>
  </div>
  <div class="vr-nav-meta">{meta}</div>
  <button class="vr-theme-toggle" id="theme-toggle" aria-label="Toggle theme" title="Toggle light/dark">
    <i data-lucide="sun" class="icon-sun"></i>
    <i data-lucide="moon" class="icon-moon"></i>
  </button>
</nav>'''


def inject_header(path: Path, active: str, meta: str, badge: str = "v1.4.0") -> None:
    """Replace the first page nav and install/refresh shared header behavior."""

    source = path.read_text()
    source, nav_count = re.subn(r"<nav\b[^>]*>[\s\S]*?</nav>", render_header(active, meta, badge), source, count=1)
    if nav_count != 1:
        raise SystemExit(f"shared header injection expected one nav in {path}, found {nav_count}")
    style = f'<style id="site-header-style">\n{HEADER_CSS}\n</style>'
    source, style_count = re.subn(r'<style id="site-header-style">[\s\S]*?</style>', style, source, count=1)
    if style_count == 0:
        source, head_count = re.subn(r"</head>", style + "\n</head>", source, count=1)
        if head_count != 1:
            raise SystemExit(f"shared header CSS injection failed in {path}")
    chart_label_script = f'<script id="site-chart-labels">\n{CHART_LABEL_JS}\n</script>'
    source, chart_count = re.subn(
        r'<script id="site-chart-labels">[\s\S]*?</script>',
        lambda _match: chart_label_script,
        source,
        count=1,
    )
    if chart_count == 0:
        source, head_count = re.subn(r"</head>", lambda _match: chart_label_script + "\n</head>", source, count=1)
        if head_count != 1:
            raise SystemExit(f"shared chart-label injection failed in {path}")
    table_sort_script = f'<script id="site-table-sort">\n{TABLE_SORT_JS}\n</script>'
    source, script_count = re.subn(r'<script id="site-table-sort">[\s\S]*?</script>', lambda _match: table_sort_script, source, count=1)
    if script_count == 0:
        source, body_count = re.subn(r"</body>", lambda _match: table_sort_script + "\n</body>", source, count=1)
        if body_count != 1:
            raise SystemExit(f"shared table-sort injection failed in {path}")
    path.write_text(source)
