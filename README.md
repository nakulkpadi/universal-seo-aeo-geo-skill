# Universal SEO · AEO · GEO Skill

### Zero-dependency website optimization for Google Search, answer engines, AI discovery, technical SEO, content quality and conversion

**Engineered by Nakul.Kapdi**

**Discover → Audit → Prioritize → Correct → Validate → Measure**

Universal SEO · AEO · GEO Skill is an open-source Agent Skill that turns a compatible coding agent into a category-aware website optimization reviewer. It combines deterministic page checks with focused playbooks for search visibility, answer-engine readiness, AI citation quality, technical SEO, content, schema, conversion and growth.

It is designed to answer a simple question before users install it:

> **What will I actually get after using this skill?**

You get an evidence-based audit that explains **what is wrong, why it matters, how confident the finding is, what to change, how much effort it takes, and how to verify the correction**.

## Before vs. after

| Without this skill | With Universal SEO · AEO · GEO |
|---|---|
| Generic “improve SEO” checklist | Evidence-backed page/site findings |
| Same advice for every website | Category-aware SaaS, ecommerce, local, publisher, YMYL and other playbooks |
| SEO only | SEO + AEO + GEO/citation readiness + technical + conversion |
| Subjective recommendations first | Deterministic checks first |
| “Add keywords” | Search intent, page purpose, entity clarity and citation-quality guidance |
| “Add schema” | Schema only when visible page facts support it |
| “AI optimize this page” | Specificity, evidence, attribution, freshness and extractable-answer analysis |
| Every issue treated equally | Severity + confidence + effort + validation |
| Fix suggested and forgotten | Controlled correction lifecycle with re-validation |
| Large framework/install | Python standard library only — no `pip install` |

## What it audits

| Area | Examples |
|---|---|
| SEO | title, description, H1, canonical, indexability, internal discovery, duplicate signals |
| Technical | HTTP status, viewport, language, robots directives, JSON-LD parseability, bounded crawl signals |
| AEO | question headings, answer-first structure, concise definitions, FAQ usefulness, extractable answers |
| GEO / AI citation readiness | evidence, attribution, quantified claims, author/entity identity, freshness, methodology |
| Content | intent match, unique value, information gain, examples, trust and topical completeness |
| Schema | page-type-aware structured-data recommendations without fabricated claims |
| Social discovery | Open Graph and Twitter/X metadata |
| Conversion | CTA clarity, proof, friction, offer clarity and next-step continuity |
| Growth intelligence | workflows for query mapping, cannibalization, decay, CTR opportunity, backlinks and business value |

## Supported website categories

- SaaS and software
- Ecommerce
- Local and service businesses
- Publishers, blogs and news
- Marketplaces and directories
- Healthcare / YMYL
- Education and courses
- Real estate
- Agencies and B2B
- Documentation / developer / API sites
- Job sites
- Event sites
- AI / prompt marketplaces
- General websites

The skill loads only the relevant playbook instead of forcing every website through one giant checklist.

## Why SEO + AEO + GEO?

**SEO** helps pages become discoverable and understandable in traditional search.

**AEO (Answer Engine Optimization)** helps content answer questions clearly enough for snippets, assistants and answer interfaces.

**GEO (Generative Engine Optimization)** focuses on whether content is specific, attributable, fresh and evidence-rich enough to be useful as a source in generative/AI answers.

This project does not promise rankings, AI citations or traffic. It helps improve the technical and content signals that can support those outcomes.

## Zero-dependency quick start

Requirements: **Python 3.9+**.

No third-party Python packages are required.

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

## Use as an Agent Skill

Copy the repository (or the `SKILL.md`, `references/`, `playbooks/` and `scripts/` folders) into the skills directory supported by your coding agent.

Example prompt:

```text
Use Universal SEO · AEO · GEO to audit this website.

Start with deterministic checks.
Identify the website category.
Separate SEO, AEO, GEO, technical, content and conversion findings.
For every material issue show evidence, severity, confidence, correction and validation.
Do not make risky production changes.
```

For a quick page review:

```text
Run a quick one-page SEO/AEO/GEO audit of this URL.
Give me the five highest-value corrections first.
```

For a pre-release review:

```text
Audit the changed pages before release.
Propose safe corrections, validate local/staging changes,
and keep canonical, robots, redirects and factual schema claims review-only.
```

## What results look like

A finding should look like:

```text
Area: GEO / Citation Quality
Severity: Medium
Confidence: Medium

Finding:
The page makes multiple “best/leading” claims without visible supporting evidence.

Evidence:
Broad superlatives detected; no quantified evidence found in visible text.

Why it matters:
Unsupported claims are less trustworthy for users and less useful as citable source material.

Correction:
Replace broad claims with specific, attributable evidence where truthful.

Validation:
Re-audit the page and confirm the claims are supported by visible evidence.
```

## Fast by design

The core auditor is intentionally small and deterministic:

- one standard-library Python audit engine;
- no `requests`;
- no BeautifulSoup;
- no PyYAML;
- no browser runtime;
- no bundled analytics SDK;
- no automatic third-party scanner installation.

Advanced data such as Search Console, analytics, rank tracking, backlinks or AI-visibility benchmarks can still be analyzed by the host agent when explicitly supplied. They are not forced into the lightweight core.

## Repository structure

```text
.
├── SKILL.md
├── README.md
├── SECURITY.md
├── CHANGELOG.md
├── VERSION
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
└── tests/
```

## Security model

The core is intentionally constrained:

- public HTTP/HTTPS GET/HEAD only;
- localhost/private/reserved network targets rejected;
- bounded response size, timeouts and crawl pages;
- no `.env` or environment-variable discovery;
- no credentials required;
- no subprocess or shell execution in the auditor;
- no dynamic `eval`/`exec`;
- no CMS, Git, database, payment, DNS or deployment writes;
- crawled text is treated as untrusted data.

See `SECURITY.md`.

## What this skill does not claim

This skill is not:
- a guarantee of Google rankings;
- a guarantee of inclusion/citation in AI answers;
- a replacement for Search Console, analytics or field Core Web Vitals data;
- an accessibility certification;
- a security penetration test;
- an automatic production deployment system.

When evidence is unavailable, the correct result is **Not verified**, not a guess.

## Testing

```bash
python tests/test_core.py
python -m py_compile scripts/audit.py
```

The test suite checks the zero-dependency auditor on local HTML and validates JSON output.

## Release philosophy

The project deliberately follows:

**small engine + selective intelligence**

New features should not automatically become runtime dependencies. Prefer focused Markdown references, explicit data inputs and deterministic standard-library checks.

## Contributing

Contributions are welcome. Please keep checks:
- evidence-based;
- category-aware where appropriate;
- explicit about false positives;
- safe for defensive website optimization;
- testable without unnecessary dependencies.

## License

MIT.

---

If this project helps, star the repository and share real audit examples or false positives through GitHub Issues.
