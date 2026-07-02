# SEO 0 to Hero — Complete A to Z Master Guide

A single-page, self-contained SEO reference covering everything from beginner fundamentals to agency-level workflows — built as one standalone HTML file with custom icons and hand-built charts (no external libraries, no internet connection required after download).

---

## 📁 Folder Structure

```
SEO-Guide-Project/
├── index.html                  ← open this in any browser — the main entry point
├── README.md                   ← this file
├── css/
│   └── style.css               ← all styling (design tokens, layout, components, charts)
├── js/
│   └── main.js                 ← mobile sidebar toggle + scrollspy (active-module highlight)
├── assets/
│   └── README.txt              ← reserved for future images/media (currently empty — icons are inline SVG)
└── build-scripts/
    ├── gen_charts.py           ← Python script used to compute the donut chart SVG arc paths
    └── gen_line.py             ← Python script used to compute the GSC trend line SVG coordinates
```

**Everything is properly separated:**
- `index.html` — structure/markup only
- `css/style.css` — all visual styling, one file, easy to theme
- `js/main.js` — all interactivity, vanilla JS, zero dependencies
- `assets/` — reserved slot for any future images/logos you want to add
- `build-scripts/` — reference-only Python scripts used once during build time to hand-calculate exact SVG coordinates for the charts (not required to run the guide)

The `build-scripts/` folder is included for transparency/reference only — you do **not** need
Python or need to run anything to use the guide; every chart's output is already baked into
`index.html`/`css/style.css`.

### Why the icon sprite stays inside `index.html`
The SVG icon sprite (`<defs><symbol id="i-...">`) is kept inline in `index.html` rather than as
a separate `assets/icons.svg` file on purpose: browsers block `<use href="external-file.svg#id">`
references when a page is opened directly as a local file (`file://...`) due to same-origin
security rules. Keeping the sprite inline means the guide **always works by double-clicking
`index.html`** — no local server required. If you later host this on a real web server, you're
welcome to extract the sprite to `assets/icons.svg` and load it via `fetch()`.

---

## ✅ What's Inside the Guide (15 Modules)

| # | Module | Covers |
|---|--------|--------|
| 1 | SEO Fundamentals | What is SEO, how search engines work, ranking factors, White/Black Hat, On-Page/Off-Page/Technical, Local, International, E-commerce, AI SEO & GEO |
| 2 | Keyword Research | Search intent (informational/commercial/transactional/navigational), short-tail, long-tail, LSI, topical, question, seasonal keywords |
| 3 | Best SEO Tools | 30+ tools across Keyword Research, Competitor Analysis, Technical SEO, Content Optimization, Backlink Analysis, Rank Tracking |
| 4 | Chrome Extensions | 13 extensions with purpose / when-to-use / best-use-case for each |
| 5 | Keyword Finding | Seed keywords, Google Suggestions, PAA, Related Searches, Competitor keywords, Search Console, buyer-intent keywords |
| 6 | Competitor Research | Finding competitors, keyword/backlink/content/link gap analysis |
| 7 | Content SEO | E-E-A-T, NLP & Semantic SEO, Topical Authority, Internal/External linking, FAQ Schema, Content Clusters, Pillar Pages |
| 8 | Technical SEO | Robots.txt, Sitemap, Canonical, Pagination, Indexing, Crawl Budget, Core Web Vitals, Schema, HTTPS, Mobile, Redirects |
| 9 | Link Building | Guest Posting, HARO/Digital PR, Broken Link Building, Skyscraper, Link Reclamation, Citations, Web 2.0, Profile links |
| 10 | Local SEO | Google Business Profile, NAP, Reviews, Citations, Local keywords, Maps ranking |
| 11 | AI SEO / GEO | ChatGPT, Gemini, Claude, Perplexity, AI content optimization, Prompt Engineering, Generative Engine Optimization |
| 12 | Analytics | GA4, Search Console, Bing Webmaster, Looker Studio, Conversion tracking, CTR, Impressions, Avg. Position |
| 13 | Complete SEO Workflow | 12-step process from Niche Selection to Monthly Audit |
| 14 | SEO Checklists | 8 ready checklists — New Website, Blog, Local, WooCommerce, WordPress, Shopify, Technical, Content |
| 15 | Real Case Studies | 6 live-style walkthroughs — keyword research, competitor analysis, article optimization, technical audit, backlink analysis, ranking strategy |

---

## 📊 Charts Included (7 total — all pure SVG/CSS, zero dependencies)

1. **Google Ranking Factors** — horizontal bar breakdown (conceptual weighting)
2. **SEO's 3 Core Pillars** — donut (On-Page / Off-Page / Technical)
3. **Search Intent Distribution** — vertical bar chart
4. **Core Web Vitals Thresholds** — segmented range bars (Good / Needs Improvement / Poor) for LCP, INP, CLS
5. **Link Building Tactics** — dual bar chart (Impact vs. Effort) across 8 tactics
6. **Local SEO Ranking Signals** — donut (GBP / Reviews / Citations / On-Page / Behavioral)
7. **GSC Performance Trend** — 12-month line/area chart (Clicks vs. Impressions)

> ⚠️ **Note on chart data:** Google does not publish exact ranking-factor percentages. All
> weightings shown are **illustrative / conceptual**, meant for teaching relative priority —
> not official Google figures. This is also labeled directly on each chart in the guide.

---

## 🎨 Design System

| Token | Value | Usage |
|---|---|---|
| `--paper` | `#F7F2E7` | Background |
| `--panel` | `#FFFFFF` | Cards / panels |
| `--ink` | `#15202E` | Primary text |
| `--muted` | `#5B6472` | Secondary text |
| `--coral` | `#FF5A3C` | Primary accent |
| `--teal` | `#0E9C90` | Secondary accent |
| `--amber` | `#E39B33` | Tertiary accent |
| `--navy-deep` | `#0E1A2B` | Dark contrast blocks |

**Fonts:** Fraunces (headings/display), Inter (body text), JetBrains Mono (labels, data, module numbers) — loaded from Google Fonts. This is the *only* external dependency; everything else (icons, charts, layout) is self-contained.

**Signature element:** each module is numbered with a circular "SERP position badge," echoing the ranking-position concept that's central to SEO itself.

---

## 🖼 Icons

All icons are built from a single inline SVG `<symbol>` sprite defined at the top of the HTML file (`<defs>` block) and reused via `<use href="#i-...">` throughout — this keeps every icon visually consistent, lightweight, and infinitely color-customizable via `currentColor`/fill overrides, with no image files or external icon library needed.

---

## 🛠 How to Customize

- **Change colors:** edit the CSS custom properties (`:root { --coral: ...; }`) at the top of `css/style.css` — every icon, chart, and accent updates automatically.
- **Edit chart data:** each chart is plain HTML/CSS (bar widths as `%`) or inline SVG (`<path>`/`<polyline>` points) inside `index.html` — search for the relevant `<div class="chart-panel">` block and adjust values directly. No build step required.
- **Add a module:** copy an existing `<section class="module" id="mX">` block in `index.html`, update the `id`, position badge number, and content, then add a matching link inside `<nav id="sideNav">` in the sidebar.
- **Edit mobile menu / scroll behavior:** all interactivity lives in `js/main.js` — it's plain vanilla JavaScript, no build tools, no npm install needed.
- **Recompute a donut/line chart:** the two scripts in `build-scripts/` show the exact math (arc-path generation, point normalization) used to hand-place the SVG coordinates, in case you want to regenerate a chart with different data.

---

## 🌐 Compatibility

- Works fully offline after the first load (only Google Fonts requires internet — the guide still works without it, just falls back to system fonts).
- No JavaScript frameworks, no canvas, no external chart libraries — pure HTML/CSS/SVG for all visuals, with a small vanilla-JS file (`js/main.js`) handling only the mobile menu and scroll-highlighting — so it renders identically in any modern browser, any device, any preview pane.
- On mobile/narrow screens, tap the **☰ Modules** button (top-left) to open the sidebar navigation.
- Just three linked files (`index.html`, `css/style.css`, `js/main.js`) — easy to host on any static server, drop into a CMS, or open directly by double-clicking `index.html`.

---

*Built as a complete beginner-to-agency-level SEO reference — 2026.*
