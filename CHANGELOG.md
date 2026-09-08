# Changelog

## 2.0.0 - 2026-09-08

### Renamed and repositioned
- Reframed the project as **Universal SEO · AEO · GEO Skill** so users understand the outcome before installation.
- Generalized the skill for SaaS, ecommerce, local, publishing, marketplace, healthcare/YMYL, education, real estate, B2B, docs, jobs, events, AI marketplaces and general sites.

### Architecture
- Reduced the runtime to a **zero-dependency Python standard-library core**.
- Adopted a lightweight router: load only the relevant reference and vertical playbook.
- Kept the deterministic one-page audit fast and added bounded site mode.

### Audit quality
- Added separate SEO, AEO, GEO/citation-quality, technical, content, schema and conversion guidance.
- Added severity + confidence + evidence + correction + validation expectations.
- Added vague/unsupported claim detection and citation-quality guidance.
- Added category detection and category-specific playbooks.
- Added controlled correction lifecycle and explicit review-only high-risk SEO changes.

### Security
- Added private/reserved-network target blocking, bounded fetch size/timeouts/crawl size and untrusted-content handling.
- Core requires no credentials and does not inspect environment variables.
- Core performs no production writes, shell execution or dynamic code execution.

### Documentation
- Rebuilt README around user outcomes, before/after expectations, quick start, example findings, limitations and security.
