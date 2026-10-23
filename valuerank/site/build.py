"""Generate the multi-page static site under ``site/`` from the ``data/`` snapshots.

The generator has three layers: view models (``valuerank.site.viewmodel``)
turn snapshots into the structures described in ``docs/site-data-contract.md``;
Jinja templates (``valuerank/site/templates``) turn view models into pages;
this module orchestrates both, copies the static assets and writes the public
JSON files, redirect stubs, the archived legacy page, the sitemap and robots.txt.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from xml.sax.saxutils import escape

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

PACKAGE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = PACKAGE_DIR / "templates"
ASSETS_DIR = PACKAGE_DIR / "assets"
BASE_URL = "https://valuerank.alolabs.dev"


def jinja_env(templates_dir: Path = TEMPLATES_DIR) -> Environment:
    """A strict, autoescaping Jinja environment over the site templates."""

    return Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render(env: Environment, template_name: str, context: dict) -> str:
    return env.get_template(template_name).render(**context)


def copy_assets(source: Path, target: Path) -> list[Path]:
    """Mirror ``source`` into ``target``, removing whatever was there before."""

    if target.exists():
        shutil.rmtree(target)
    copied = []
    for path in sorted(source.rglob("*")):
        if path.is_file():
            destination = target / path.relative_to(source)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
            copied.append(destination)
    return copied


def write_page(out_dir: Path, site_path: str, html: str) -> Path:
    """Write ``html`` for the site path ``/a/b/`` at ``out_dir/a/b/index.html``."""

    path = out_dir.joinpath(*[part for part in site_path.split("/") if part]) / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    return path


def write_json(path: Path, document) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def write_redirect(env: Environment, out_path: Path, *, target: str, title: str, canonical: str) -> Path:
    """Write a meta-refresh stub; the template reads ``page.target``, ``page.title`` and ``page.canonical``."""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render(env, "redirect.html", {"page": {"target": target, "title": title, "canonical": canonical}}))
    return out_path


OG_IMAGE_META = re.compile(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*(")')


def archive_legacy_page(env: Environment, source: Path, out_path: Path, *, archive_date: str, archive_href: str, note: str, og_image: str | None = None) -> Path:
    """Copy a retired static page under ``archive/`` with a banner after its ``<body>`` tag.

    With ``og_image`` set, the page's ``og:image`` and ``twitter:image`` tags point at that share card.
    """

    html = source.read_text()
    match = re.search(r"<body\b[^>]*>", html)
    if match is None:
        raise ValueError(f"legacy page has no <body> tag: {source}")
    banner = render(env, "archive_banner.html", {"page": {"archiveDate": archive_date, "archiveHref": archive_href, "note": note}})
    archived = html[: match.end()] + "\n" + banner + html[match.end() :]
    if og_image is not None:
        archived = OG_IMAGE_META.sub(lambda tag: tag.group(1) + escape(og_image, {'"': "&quot;"}) + tag.group(2), archived)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(archived)
    return out_path


def write_sitemap(out_dir: Path, base_url: str, site_paths: list[str], *, lastmod: str) -> Path:
    unique = sorted(set(site_paths), key=site_paths.index)
    entries = "".join(
        f"  <url><loc>{escape(base_url + path)}</loc><lastmod>{escape(lastmod)}</lastmod></url>\n" for path in unique
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "sitemap.xml"
    path.write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + entries + "</urlset>\n")
    return path


def write_robots(out_dir: Path, base_url: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "robots.txt"
    path.write_text(f"User-agent: *\nAllow: /\nSitemap: {base_url}/sitemap.xml\n")
    return path


# --- page catalogue -----------------------------------------------------------

from valuerank.paths import DATA, ROOT, SITE  # noqa: E402  (after helpers, before main)
from valuerank.release import DATE, VERSION  # noqa: E402
from valuerank.site import export, viewmodel  # noqa: E402

NAV = [
    {"key": "rankings", "label": "Rankings", "href": "/rankings/"},
    {"key": "models", "label": "Models", "href": "/models/"},
    {"key": "plans", "label": "Plans", "href": "/plans/"},
    {"key": "benchmarks", "label": "Benchmarks", "href": "/benchmarks/"},
    {"key": "methodology", "label": "Methodology", "href": "/methodology/"},
    {"key": "changelog", "label": "Changelog", "href": "/changelog/"},
    {"key": "data", "label": "Data", "href": "/data/"},
]

LEGACY_CODING_AGENTS = PACKAGE_DIR / "legacy" / "coding-agents-v0.3.html"
ARCHIVE_PATH = "/archive/coding-agents-v0.3/"
ARCHIVE_CARD = "/og/archive.png"
REDIRECTS = {
    "/tb4/": ("/benchmarks/terminal-bench-4/", "Terminal-Bench 4.0 has moved"),
    "/coding-agents/": (ARCHIVE_PATH, "The coding-agents snapshot is archived"),
}


def site_context(bundle) -> dict:
    rankings = bundle.rankings
    return {
        "version": VERSION,
        "publishDate": DATE,
        "observedAt": rankings["observedAt"],
        "nav": NAV,
        "baseUrl": BASE_URL,
        "basis": rankings["bases"],
        "defaultBasis": rankings["defaultBasis"],
        "costWeightPct": rankings["costWeightPct"],
        "modelCount": sum(1 for model in rankings["models"] if model["rankingEligible"]),
        "rosterCount": len(rankings["models"]),
        "dimensionCount": len(rankings["dimensions"]),
    }


# One boot module per page type (assets/js/pages/); pages without behaviour of their own share static.js.
SCRIPTS = {
    "index": ["/assets/js/pages/index.js"],
    "rankings": ["/assets/js/pages/rankings.js"],
    "benchmarks": ["/assets/js/pages/benchmarks.js"],
    "tb4": ["/assets/js/pages/tb4.js"],
    "changelog": ["/assets/js/pages/changelog.js"],
}
STATIC_SCRIPTS = ["/assets/js/pages/static.js"]


def page_meta(path: str, title: str, description: str, key: str, og_image: str | None = None) -> dict:
    """Per-page metadata. The share card is ``/og/<key>.png`` unless ``og_image`` names another card."""

    return {
        "key": key,
        "scripts": SCRIPTS.get(key, STATIC_SCRIPTS),
        "path": path,
        "title": title,
        "description": description,
        "canonical": BASE_URL + path,
        "ogImage": BASE_URL + (og_image or f"/og/{key}.png"),
    }


def pages(bundle) -> list[tuple[str, str, dict]]:
    """Return ``(site_path, template_name, page)`` for every generated page."""

    version = VERSION
    n = sum(1 for model in bundle.rankings["models"] if model["rankingEligible"])
    catalogue = [
        ("/", "index.html", viewmodel.index_page(bundle), "index",
         f"ValueRank {version}: which AI model delivers the most value for software engineering and DevOps",
         f"{n} frontier models ranked for software engineering and DevOps work: measured coding, debugging and terminal quality against API and subscription-plan cost, with every number traced to its source."),
        ("/rankings/", "rankings.html", viewmodel.rankings_page(bundle), "rankings",
         f"Rankings · ValueRank {version}",
         "Filter, sort, compare and export the full ValueRank table; every view has a shareable URL."),
        ("/models/", "models.html", viewmodel.models_page(bundle), "models",
         f"All models · ValueRank {version}",
         "Every model in the ValueRank roster with its Plan and API rank, evidence grade and a page of sourced scores."),
        ("/plans/", "plans.html", viewmodel.plans_page(bundle), "plans",
         f"Subscription plan value · ValueRank {version}",
         "How subscription allowances and token efficiency combine into cost per Intelligence Index point."),
        ("/benchmarks/", "benchmarks.html", viewmodel.benchmarks_page(bundle), "benchmarks",
         f"Benchmark sources · ValueRank {version}",
         "The benchmarks behind each dimension, their owners, versions, observation dates and coverage."),
        ("/benchmarks/terminal-bench-4/", "benchmark_tb4.html", viewmodel.tb4_page(bundle), "tb4",
         "Terminal-Bench 4.0: resolution rate versus cost · ValueRank",
         "The official Terminal-Bench 4.0 leaderboard against run cost, with ValueRank cohort coverage and labelled provider claims."),
        ("/methodology/", "methodology.html", viewmodel.methodology_page(bundle), "methodology",
         f"Methodology · ValueRank {version}",
         "How ValueRank scores models: dimensions, weights, renormalisation, evidence grades and limitations, with a worked example."),
        ("/changelog/", "changelog.html", viewmodel.changelog_page(bundle), "changelog",
         f"Changelog · ValueRank {version}",
         "Every ValueRank release with its cohort, dimensions and rank changes."),
        ("/data/", "data.html", viewmodel.data_page(bundle), "data",
         f"Data downloads · ValueRank {version}",
         "Machine-readable JSON for every table on the site, with its schema and provenance."),
    ]
    # O53: every ranking other than the leading one has its own rankings page.
    for track, other in bundle.extras.get("tracks", {}).items():
        catalogue.append((viewmodel.TRACK_PATHS[track], "rankings.html", viewmodel.rankings_page(other), "rankings",
                          f"{other.rankings['track']['label']} · ValueRank {version}",
                          f"The {other.rankings['track']['label']}: {viewmodel.TRACK_LEADS[track]}"))
    result = []
    for path, template, page, key, title, description in catalogue:
        page = dict(page)
        page.update(page_meta(path, title, description, key))
        result.append((path, template, page))
    for slug in sorted(bundle.models):
        page = dict(viewmodel.model_page(bundle, slug))
        path = f"/models/{slug}/"
        page.update(page_meta(path, f"{page['name']} · ValueRank {version}", f"How {page['name']} scores on every ValueRank dimension, with sources, dates and evidence grades.", "model", f"/og/models/{slug}.png"))
        result.append((path, "model.html", page))
    return result


def remove_stale_model_pages(out_dir: Path, keep: set[str]) -> list[Path]:
    """Delete generated model pages whose model left the roster."""

    removed = []
    models_dir = out_dir / "models"
    if models_dir.exists():
        for child in sorted(models_dir.iterdir()):
            if child.is_dir() and child.name not in keep:
                shutil.rmtree(child)
                removed.append(child)
    return removed


def main(*, root: Path = ROOT, data: Path = DATA, out: Path | None = None, templates_dir: Path = TEMPLATES_DIR, assets_dir: Path = ASSETS_DIR) -> int:
    out_dir = root / "site" if out is None else out
    env = jinja_env(templates_dir)
    bundle = viewmodel.build_bundle(data)
    site = site_context(bundle)

    written = []
    for path, template, page in pages(bundle):
        written.append(write_page(out_dir, path, render(env, template, {"site": site, "page": page})))
    remove_stale_model_pages(out_dir, set(bundle.models))
    written += export.export_public_data(data, out_dir / "data")
    written += copy_assets(assets_dir, out_dir / "assets")
    for legacy_path, (target, title) in REDIRECTS.items():
        written.append(write_redirect(
            env, out_dir.joinpath(*legacy_path.strip("/").split("/")) / "index.html",
            target=target, title=title, canonical=BASE_URL + target,
        ))
    written.append(archive_legacy_page(
        env, LEGACY_CODING_AGENTS, out_dir.joinpath(*ARCHIVE_PATH.strip("/").split("/")) / "index.html",
        archive_date="2026-10-18", archive_href="/benchmarks/",
        note="This coding-agents v0.3 snapshot (July 2026, Terminal-Bench 2.1) is kept for provenance and is no longer updated. Current results live in the ValueRank rankings and the Terminal-Bench 4.0 benchmark page.",
        og_image=BASE_URL + ARCHIVE_CARD,
    ))
    written.append(write_sitemap(out_dir, BASE_URL, [path for path, _template, _page in pages(bundle)] + [ARCHIVE_PATH], lastmod=bundle.rankings["observedAt"][:10]))
    written.append(write_robots(out_dir, BASE_URL))
    print(json.dumps({"version": VERSION, "pages": len([1 for _ in pages(bundle)]), "files": len(written), "out": str(out_dir.relative_to(root)) if out_dir.is_relative_to(root) else str(out_dir)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
