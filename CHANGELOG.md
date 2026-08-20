# Changelog

All notable changes to the Vibegraph specification are documented here. The format
follows [Keep a Changelog](https://keepachangelog.com), and the spec follows
[Semantic Versioning](https://semver.org).

## [Unreleased]

### Changed (breaking)
- The Brand Context element **Slogans & Taglines** is renamed **Taglines &
  Slogans**, and its `## ` heading in the brand document changes to match. The
  durable brand line and the situational campaign lines are different things,
  and the tagline leads. A consumer that matches the old heading exactly will
  not find the section; consumers MAY treat `Slogans & Taglines` as a v2.0.0
  synonym.
- Awaiting a version number: the whitepaper still carries the old name in its
  v1.5 edition and picks this up in v2.0.

## [2.0.0] — 2026-08-11

The flat-tree release: the specification now describes the format the reference
application (vibegraph.ai) actually exports, and adopts the whitepaper v1.5
naming.

### Changed (breaking)
- The nested `core/` + `modules/` tree is replaced by a flat, owner-named tree:
  `<owner>.vibegraph.md` (master, read first), `<owner>.personality.md`,
  `<owner>.ikigai.md`, `<owner>.brand.md`, `<brand>.brand.md` per business
  brand, `assets/`, and `orbits/` pointer documents. Delivered as
  `<owner-slug>-vibegraph.zip`.
- The master file replaces `VIBEGRAPH.md`: front matter plus an explicit,
  link-checked read order covering every file in the export.
- **Knowledge Base is renamed Orbits**; `modules/` becomes `orbits/`.
  Consumers MAY treat `modules/` as a v1.0 synonym.
- Brand Positioning and Brand Aesthetics are renamed **Brand Context** (twelve
  elements) and **Brand Visuals** (eight elements), composed into one brand
  document per brand.
- The personality layer is a two-part assessment: the Big Five (IPIP-NEO-120)
  joined by the Enneagram, reconciled in an integrated reading.

### Added
- Slug rules: lowercase-hyphenated names, input-time collision rejection, and
  the reserved slugs `assets`, `orbits`, `vibegraph`.
- Orbit pointer documents (`section: orbit`, `target_tool`): exported
  vibegraphs carry the shareable parts and pointers; orbit content stays in
  the owner's own tools, making the first permission decision structural.
- Optional `brand-kit-checklist.md` and `<owner>.vibegraph.pdf`.
- A compatibility note for accepting v1.0 trees.

[2.0.0]: https://vibegraph.md

## [1.0.0] — 2026-07-11

The first public release of the Vibegraph specification.

### Added
- Two-part architecture: **Core Identity** (`core/`) and **Knowledge Base** (`modules/`).
- The `VIBEGRAPH.md` manifest convention with YAML front matter
  (`vibegraph_version`, `type`, `owner`, `updated`, `default_visibility`, `summary`).
- Per-document schema with `section`, `visibility`, `scope`, and `updated` fields.
- Personal Core instrument set: Big Five (OCEAN), Ikigai 2.0, brand positioning,
  brand aesthetics.
- Business Core instrument set: Aaker's five dimensions + brand archetype,
  Golden Circle + mission/vision/values, brand positioning, brand design system.
- Suggested module taxonomies for personal and business vibegraphs.
- Deny-by-default permission model with `private` / `scoped` / `public` visibility.
- Guidance for AI consumption: direct context, persistent workspace context,
  live access over MCP, and memory-layer seeding.
- Personal and business templates.
- Personal and business templates with inline guidance (a complete worked example follows with the vibegraph.ai app).
- Dual licensing: MIT for templates/schema/code, CC-BY 4.0 for specification prose.

[1.0.0]: https://vibegraph.md
