# ValueRank site: information architecture and UX critique, with an improvement plan

Status: accepted 2026-10-18, in progress. Audited against the deployed v1.9.6 site (local preview of `site/`), desktop at 1024×768 and phone at 375×812, plus the DOM and generator source.

## 1. Verdict

ValueRank has an unusually strong evidence base and a defensible method, but the site presents them as one 20,500-pixel scroll in which the answer, the proof and the audit trail compete for the same screen. A visitor who wants "which model gives me the most for my money, and why" has to read a 112-word hero paragraph, decode a 2,600-pixel table whose cells contain sentences, and discover that the two most decision-relevant tables (frontier comparison, plan candidates) sit below the FAQ and outside the navigation. The ingredients of a world-class value benchmark are present; the architecture that would make them legible is not.

## 2. Scorecard

| Area | Grade | Evidence |
|---|---|---|
| Answer clarity (first 5 seconds) | D | Hero is 1,012 px tall on desktop and 1,738 px on phone before any ranking; lead paragraph is 112 words of method jargon ("renormalized per model; priority coverage"). The podium answers "who is #1" but not "for whom" or "why". |
| Information architecture | D | Single page with 8 sections plus 2 un-navigable appendices (2,400 words). Three top-level "modes" (LLM Models, Coding Agents, TB 4) where one is a frozen 2026-07 snapshot presented as a peer and one is a single benchmark view. No model pages, no permalinks, no search, no compare. |
| Ranking table usability | C- | 16 rows occupy 2,579 px (139–228 px each) because coverage notes, route evidence and sub-scores are written into cells. 8 columns, 12–13 px text, 5 ad-hoc cost tiers ("Near-Budget", "Mid-Range", "Expensive"). On a phone the table is 1,006 px wide inside a 375 px viewport. |
| Trust and provenance | B- | Every number is traceable, but provenance lives in prose and appendices. Evidence class (owner-measured, provider claim, modelled, user assumption) is not a visible badge on the number it qualifies; "Provisional assumption" rows sit beside controlled measurements with equal visual weight. |
| Consistency | C | Two different "primary" rankings now exist: the site opens on the Plan basis (Claude Opus 5.5 first) while README and scores.md lead with the API basis (GPT-6.1 Sol first). A FAQ still asks "Why is Claude ranked so low?" on a page where Claude is #1. Units differ by column and basis (USD per Index run versus USD per Index point). |
| Mobile | D | Section links collapse to width 0 with no menu, so there is no in-page navigation at all; 114 interactive targets under 44 px; cost-basis control is 140 px tall; charts render at 293 px wide; total page height 27,977 px. |
| Accessibility | C- | Section titles are `div`s, so there is no h2 structure; no skip link; 42 of 67 table headers lack `scope`; 8 Plotly charts have no text alternative; table text at 12–13 px. |
| Performance and robustness | C | 267 KB HTML with 4,259 DOM nodes, Plotly 2.27 from a CDN for scatter charts, `lucide@latest` unpinned from unpkg (a moving dependency on a site that already survived one supply-chain incident). Charts are lazily rendered, which is good. |
| Content and copy | C | Insight cards include "V1.9.6 RELEASE" and FAQ entries are release notes ("Is Claude Opus 5.5 included?"). Raw Data & Coverage runs 1,506 words on the home page. Good: the methodology is honest about gaps and nothing is neutral-filled. |
| Generator and maintainability | C | `site/index.html` is both template and output, patched in place by regex guards; every copy change needs a matching guard. Fine for one page, hostile to a multi-page site. |

## 3. What is wrong, specifically

1. **The page answers the wrong question first.** The hero explains how ValueRank works before it says what it found. A benchmark site's first screen should state the finding, who it is for, and the single most important caveat, then invite the reader deeper.
2. **One scroll, three audiences.** Decision makers (which model, which plan), analysts (how was it scored), and auditors (show me the source row) share one page. The result is that none of them is served well: the decision maker reads method prose, the auditor scrolls 16,000 px to the plan evidence table.
3. **The table is a document, not an instrument.** Rows carry coverage sentences, route evidence and sub-scores inline. There is no filtering, no column choice, no compare, no export of ValueRank's own data (the only CSV link is to an external scoreboard), and no stable link to a model.
4. **Evidence grades are invisible at the point of use.** The methodology's best feature, exact-variant evidence with explicit fallbacks, is expressed as prose. A measured value, a provider claim and a user assumption should look different wherever they appear.
5. **Two rankings, one word "primary".** Plan basis on the site versus API basis in the documents will be read as a contradiction. Either one basis is canonical and the other is a view, or both are first-class with distinct names.
6. **Navigation does not reflect the content.** "TB 4" is a single benchmark page sitting beside the whole ranking; "Coding Agents" is an archived snapshot; the two newest and most valuable sections (frontier comparison, plan candidates) have no navigation entry; on phones there is no navigation.
7. **The site is heavy for what it shows.** Eight interactive charts, most of them variants of the same scatter, on a page that is already long. The information in Rank Displacement, Cost Impact and Version History belongs on a changelog and model pages, not on the landing page.

## 4. Target information architecture

```
/                       Answer page. "Best value today" with Plan/API toggle, three use-case picks
                        (best overall value, best quality regardless of cost, best budget), a compact
                        16-row table (rank, model, score, quality, cost, evidence badge), one Pareto chart.
/rankings/              The instrument. Full table with column picker, filters (provider, plan route,
                        evidence grade, coverage), compare (2–4 models), CSV/JSON export, sharable view state in the URL.
/models/<slug>/         One page per model. Score breakdown by dimension with source, date and evidence badge
                        per value; selected AA variant; plan routes and effective costs; rank history; missing metrics.
/plans/                 Subscription value. Routes, multiples, evidence class, the "USD per Index point" worked
                        example, and the candidate comparison that today sits below the FAQ.
/benchmarks/            Source registry: DeepSWE v1.1, Bug Hunt, LiveBench, Terminal-Bench 4.0 (the current
                        TB4 page becomes /benchmarks/terminal-bench-4/), AA components; coverage matrix.
/methodology/           How scoring works with a worked example for one model; limitations; FAQ (questions only,
                        no release notes).
/changelog/             Version history, rank changes per release, what changed in sources and weights.
/data/                  Downloads and stable JSON for every table (static files, documented schema).
/archive/coding-agents-v0.3/   The frozen coding-agents snapshot, with an archive banner and a link to /benchmarks/.
```

Design principles for every page: the answer before the method; every number one click from its source, date and evidence grade; progressive disclosure (summary, detail, evidence); one unit per column; the same component for the same concept everywhere.

## 5. The core experience, redesigned

- **Answer page.** Headline states the finding in plain language ("On a subscription, Claude Opus 5.5 delivers the most Index points per plan dollar among frontier models; at API rates, GPT-6.1 Sol does"). Beneath it: three picks with one-sentence reasons, the basis toggle, the compact table, the Pareto chart. Total height target: under 4,000 px on desktop.
- **Ranking table as an instrument.** Dense rows (about 56 px), numbers right-aligned in a monospace face, evidence badge per row, coverage shown as a small bar with the missing metrics in a hover or expander, cost in one unit per basis with the unit in the header. Sorting, filtering, column choice, compare and export are standard; the selected state lives in the URL so a view can be shared.
- **Evidence badges.** Four grades rendered the same way everywhere: Owner-measured, Provider claim, Modelled, Assumption. The plan candidate table, the model pages and the ranking table all use them; the legend lives once in methodology.
- **Model pages.** The audit trail becomes a feature: each dimension lists value, source link, observation date, evidence grade and the exact evaluated variant. This is where "never transferred between variants" becomes visible and credible.
- **Plan value explained once, well.** A worked example in /plans/: allowance multiple, Index run cost, cost per Index point, and what the number does and does not claim. Provisional assumptions (MiMo 1.5×, common GPT multiples) are visually flagged as such.
- **Mobile first for the answer page.** Cards instead of a wide table on phones, a real menu, 44 px targets, 16 px base text; the full table remains available with horizontal scroll and a sticky model column.

## 6. Roadmap

| Phase | Scope | Done when | Effort |
|---|---|---|---|
| 0. Quick wins (no IA change) | Rewrite hero to answer-first (under 40 words); cut the FAQ to real questions and fix the stale "ranked so low" entry; add nav entries for the frontier and plan sections; pin `lucide` to a version; add h2 headings, skip link, `scope` on headers, aria labels on charts; state the basis explicitly in README ("API basis primary; Plan basis on the site"). | Lighthouse accessibility ≥ 90; nav reaches every section; copy reviewed. | 2–3 days |
| 1. Generator and design system | Replace in-place patching with a small template-driven static generator (one layout, shared components for table, badge, chart, evidence drawer) fed by `data/*.json`; keep `npm run verify:docs` byte-identity for the new output. | All pages produced from templates; `site/` no longer edited by hand or regex; tests at 100% retained. | 4–6 days |
| 2. Answer page and rankings instrument | New home page per section 5; `/rankings/` with filters, compare, export, URL state; evidence badges. | Home under 4,000 px desktop; table rows ≤ 64 px; CSV/JSON export of the committed scores; share link reproduces a view. | 5–7 days |
| 3. Model, plan and benchmark pages | `/models/<slug>/` for all 28 roster models; `/plans/` with worked example; `/benchmarks/` registry with TB4 moved under it; coding-agents archived with banner. | Every score cell links to a model page section that shows source, date and grade; old URLs redirect. | 5–7 days |
| 4. Mobile, performance, accessibility | Card layout on phones, menu, target sizes, 16 px text; swap Plotly for a lighter chart layer (or load Plotly only on chart pages); initial HTML under 150 KB. | Lighthouse performance and accessibility ≥ 90 on phone; no horizontal page scroll; charts have text alternatives. | 3–4 days |
| 5. Changelog, data and growth | `/changelog/` with rank deltas per release; `/data/` with documented JSON; Open Graph cards per page; sitemap and structured data. | Each release publishes a changelog entry automatically from `ranking_history`; every page shares with a correct card. | 2–3 days |

Phases 0 and 1 unblock everything else; phases 2 and 3 are the product; 4 and 5 make it durable.

## 7. How success is measured

- Time to first answer: the finding, the basis and the top pick are visible without scrolling on desktop and within one screen on a phone.
- Provenance: 100% of numbers on ranking, plan and model pages carry a source, a date and an evidence grade reachable in one interaction (checked by a test over the generated pages).
- Usability: the full table has filter, sort, compare and export; a shared URL reproduces the view; phone users can navigate to every section.
- Quality gates: Lighthouse ≥ 90 for performance and accessibility on both form factors; initial HTML under 150 KB; no unpinned third-party script.
- Consistency: one canonical ranking per basis, named the same way on the site, in README and in scores.md.

## 8. Decisions (taken 2026-10-18)

1. **Canonical basis.** The site opens on the Plan basis; README.md and scores.md keep the API basis as their primary table. Both rankings are first-class and are always named "Plan ranking" and "API ranking"; the word "primary" alone is retired.
2. **Coding agents v0.3** is archived at `/archive/coding-agents-v0.3/` with a banner; `/coding-agents/` redirects there.
3. **Charts** stay on Plotly, loaded lazily when a chart scrolls into view; the answer page carries one chart.
4. **Model pages** cover all 28 roster candidates, because the unranked candidates are where evidence gaps are most instructive.
5. **Shareable views.** Every filter, slider, toggle, sort, column choice, comparison and chart tab is reflected in the URL query string, so a copied URL reproduces the exact view; only the theme is remembered locally.
6. **Phase 0** is delivered through the new generator rather than by patching the legacy single page twice.
