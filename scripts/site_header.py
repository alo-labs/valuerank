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
    """Replace the first page nav and install/refresh the shared header CSS."""

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
    path.write_text(source)
