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
    table_sort_script = f'<script id="site-table-sort">\n{TABLE_SORT_JS}\n</script>'
    source, script_count = re.subn(r'<script id="site-table-sort">[\s\S]*?</script>', lambda _match: table_sort_script, source, count=1)
    if script_count == 0:
        source, body_count = re.subn(r"</body>", lambda _match: table_sort_script + "\n</body>", source, count=1)
        if body_count != 1:
            raise SystemExit(f"shared table-sort injection failed in {path}")
    path.write_text(source)
