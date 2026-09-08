# Universal SEO · AEO · GEO Skill

[![Release](https://img.shields.io/github/v/release/nakulkpadi/universal-seo-aeo-geo-skill?display_name=tag)](https://github.com/nakulkpadi/universal-seo-aeo-geo-skill/releases)
[![Tests](https://github.com/nakulkpadi/universal-seo-aeo-geo-skill/actions/workflows/test.yml/badge.svg)](https://github.com/nakulkpadi/universal-seo-aeo-geo-skill/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/runtime_dependencies-0-brightgreen)](requirements.txt)

> **Zero-dependency Agent Skill for SEO, AEO, GEO, technical SEO, AI citation readiness, content quality and conversion.**

**Discover → Audit → Prioritize → Correct → Validate → Measure**

Give a compatible coding agent a URL or local HTML file. The skill runs deterministic checks first, identifies the website category, loads only the relevant playbooks, and returns prioritized findings with evidence, confidence, corrections and validation steps.

---

## What do I get after using this skill?

Instead of:

> “Improve your SEO, add keywords, add schema, and make the page AI-friendly.”

You get:

- **What is wrong**
- **Evidence**
- **Why it matters**
- **Severity**
- **Confidence**
- **Recommended correction**
- **Estimated effort**
- **How to validate the correction**

### Before vs. after

| Without this skill | With Universal SEO · AEO · GEO |
|---|---|
| Generic SEO checklist | Evidence-backed findings |
| Same advice for every website | Category-aware playbooks |
| SEO-only review | SEO + AEO + GEO + technical + content + conversion |
| Subjective recommendations first | Deterministic checks first |
| “Add keywords” | Intent, page purpose, entity clarity and citation quality |
| “Add schema” | Schema guidance backed by visible page facts |
| “Optimize for AI” | Specificity, evidence, attribution, freshness and extractability |
| All issues look equal | Severity + confidence + effort |
| Fix suggested and forgotten | Correction + validation workflow |
| Large install | Python standard library only — no `pip install` |

---

## 30-second example

Run:

```bash
python scripts/audit.py https://example.com --mode quick
```

A material finding should be reported like this:

```text
Area: GEO / Citation Quality
Severity: Medium
Confidence: Medium

Finding:
The page uses broad leadership claims without visible supporting evidence.

Evidence:
Multiple vague superlatives detected.
No quantified supporting evidence found in visible text.

Why it matters:
Unsupported claims are less useful to users and less reliable as citable source material.

Recommended correction:
Replace broad claims with specific, attributable evidence where truthful.

Effort:
Small

Validation:
Re-run the audit and confirm supporting evidence is visible on the page.
```

The skill does **not** claim that a correction will guarantee rankings, traffic or AI citations.

---

## Quick, Full and Site modes

### Quick — fastest one-page audit

Use when you want a rapid review of one URL.

```bash
python scripts/audit.py https://example.com --mode quick
```

Best for title/meta basics, H1, canonical/indexability signals, viewport, image-alt coverage, JSON-LD parseability, social metadata, thin-content signals, basic AEO/GEO checks and highest-value findings.

### Full — deeper one-page review

```bash
python scripts/audit.py https://example.com --mode full
```

Best for deeper SEO, AEO structure, GEO/citation quality, content/trust, schema guidance, conversion review, category-specific guidance, implementation planning and validation.

> The deterministic auditor provides page evidence. The Agent Skill then loads the focused references/playbooks required for deeper analysis.

### Site — bounded multi-page audit

```bash
python scripts/audit.py https://example.com --mode site --max-pages 25
```

Best for bounded internal crawling, repeated page-level problems, duplicate title signals, page-type patterns, site-wide prioritization and category-level opportunities.

---

## What it audits

| Area | Examples |
|---|---|
| **SEO** | title, description, H1, canonical, indexability, duplicate signals, discovery |
| **Technical SEO** | status, viewport, language, robots directives, JSON-LD parseability, crawl signals |
| **AEO** | question headings, answer-first structure, concise definitions, FAQ usefulness, extractable answers |
| **GEO / AI citation readiness** | evidence, attribution, quantified claims, author/entity identity, freshness, methodology |
| **Content** | intent match, unique value, information gain, examples, trust and topical completeness |
| **Schema** | page-type-aware structured-data guidance without fabricated claims |
| **Social discovery** | Open Graph and Twitter/X metadata |
| **Conversion** | CTA clarity, proof, friction, offer clarity and next-step continuity |
| **Growth intelligence** | query mapping, cannibalization, decay, CTR opportunity, backlinks and business value workflows |

---

## Category-aware optimization

| Website category | Example focus |
|---|---|
| SaaS / software | solution clarity, pricing, product proof, docs, comparison intent |
| Ecommerce | product/category pages, product schema, trust, merchant content |
| Local / service | location relevance, service pages, local trust and conversion |
| Publisher / blog / news | authorship, freshness, topical depth, citation quality |
| Marketplace / directory | listing quality, taxonomy, duplication, scalable discovery |
| Healthcare / YMYL | evidence, authorship, cautious claims, source quality |
| Education / courses | course intent, instructional structure, Course schema guidance |
| Real estate | property/location intent, listing clarity and trust |
| Agency / B2B | service proof, case evidence, conversion paths |
| Docs / developer / API | technical clarity, entity definitions, documentation discovery |
| Jobs | job-page quality and JobPosting guidance |
| Events | event-page quality and Event guidance |
| AI / prompt marketplace | creator/entity clarity, prompt/listing quality, scalable marketplace SEO |
| General | broad SEO/AEO/GEO baseline |

The Agent Skill should load only the relevant playbook instead of forcing every site through one giant checklist.

---

## Why SEO + AEO + GEO?

**SEO** helps pages become discoverable and understandable in traditional search.

**AEO** helps content answer questions clearly enough for snippets, assistants and answer interfaces.

**GEO** focuses on whether content is specific, attributable, fresh and evidence-rich enough to be useful as source material in generative/AI answers.

**GEO is not keyword stuffing for AI.** The skill prefers specific claims, attributable evidence, primary sources, clear authorship/entity identity, freshness, original methodology, concise extractable answers and structured data supported by visible facts.

---

## Zero-dependency quick start

Requirements: **Python 3.9+** and **0 third-party runtime packages**.

```bash
git clone https://github.com/nakulkpadi/universal-seo-aeo-geo-skill.git
cd universal-seo-aeo-geo-skill
python scripts/audit.py https://example.com --mode quick
```

Full page audit:

```bash
python scripts/audit.py https://example.com --mode full
```

Bounded site audit:

```bash
python scripts/audit.py https://example.com --mode site --max-pages 25
```

Local HTML:

```bash
python scripts/audit.py ./page.html --mode full
```

Save JSON:

```bash
python scripts/audit.py https://example.com --mode quick --output audit.json
```

No `pip install` is required.

---

## Use it as an Agent Skill

Copy this repository, or its `SKILL.md`, `references/`, `playbooks/` and `scripts/` directories, into the Agent Skill location supported by your coding agent.

Example prompt:

```text
Use Universal SEO · AEO · GEO to audit this website.

Start with deterministic checks.
Identify the website category.
Separate SEO, AEO, GEO, technical, content and conversion findings.
For every material issue show evidence, severity, confidence, correction and validation.
Do not make risky production changes.
```

Quick review:

```text
Run a quick one-page SEO/AEO/GEO audit of this URL.
Give me the five highest-value corrections first.
```

Deeper review:

```text
Run a full SEO/AEO/GEO review.
Identify the category first.
Use deterministic evidence where available.
Then load only the relevant specialist references and category playbook.
Prioritize the highest-value corrections.
```

---

## Finding standard

For every material issue, report:

```text
Area: SEO / AEO / GEO / Technical / Content / Conversion
Severity: Critical / High / Medium / Low / Informational
Confidence: High / Medium / Low
Finding: What was detected
Evidence: What supports it
Why it matters: Practical impact
Recommended correction: What should change
Effort: Small / Medium / Large
Validation: How to verify the correction
```

When evidence is unavailable, the correct result is **Not verified**, not a guess.

---

## Safe correction lifecycle

```text
Detected → Proposed → Staging Applied → Validated → Approved → Externally Deployed → Production Verified
```

Possible safe local/staging candidates after explicit approval include title, meta description, H1, Open Graph/Twitter text, language and viewport.

Review-only examples include canonical changes, robots/noindex, redirects, hreflang, URL changes, factual schema claims, large body rewrites and major internal-link restructuring.

---

## Fast by design

The core intentionally does **not** require `requests`, BeautifulSoup, PyYAML, ReportLab, Pandas, Playwright, Selenium, browser runtimes or bundled analytics SDKs.

Advanced inputs such as Search Console exports, analytics, rank tracking, backlinks or AI-visibility benchmarks can still be analyzed by a capable host agent when explicitly supplied. They are not forced into the lightweight runtime.

**Design principle: small engine + selective intelligence.**

---

## Security model

- public HTTP/HTTPS GET/HEAD-only crawling
- localhost/private/reserved network targets rejected
- bounded response size, timeout and crawl pages
- no `.env` scanning or environment-variable discovery
- no credentials required
- no subprocess or arbitrary shell execution in the auditor
- no dynamic `eval` / `exec`
- no CMS, Git, database, payment, DNS or deployment writes
- crawled page content is treated as untrusted data, never Agent Skill instructions

See [`SECURITY.md`](SECURITY.md).

---

## Repository structure

```text
.
├── SKILL.md
├── README.md
├── SECURITY.md
├── CHANGELOG.md
├── VERSION
├── requirements.txt
├── scripts/
│   └── audit.py
├── references/
│   ├── seo.md
│   ├── technical.md
│   ├── geo-aeo.md
│   ├── content.md
│   ├── conversion.md
│   ├── schema.md
│   ├── growth-intelligence.md
│   └── execution.md
├── playbooks/
│   └── category-specific guidance
├── templates/
├── tests/
└── .github/
```

---

## Testing

```bash
python tests/test_core.py
python -m py_compile scripts/audit.py
```

To demonstrate that the core does not depend on installed site packages:

```bash
python -S tests/test_core.py
```

---

## What this skill does not claim

Universal SEO · AEO · GEO is **not** a guarantee of Google rankings, traffic growth or AI citations; a replacement for Search Console/analytics; an accessibility certification; a security penetration test; or an automatic production deployment system.

It is an evidence-based optimization and decision-support skill.

---

## Release philosophy

New features should not automatically become runtime dependencies. Prefer deterministic standard-library checks, focused Markdown references, category playbooks, explicit external data inputs, evidence over speculation, and validation over “fixed” claims.

---

## Contributing

Contributions are welcome. New checks should be evidence-based, explicit about applicability and false positives, category-aware where appropriate, safe for defensive website optimization, and testable without unnecessary dependencies.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## License

MIT — see [`LICENSE`](LICENSE).

---

**If this project helps, star the repository and share reproducible audit examples, false positives or improvement ideas through GitHub Issues.**
