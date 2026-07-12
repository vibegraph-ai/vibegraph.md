# Changelog

All notable changes to the Vibegraph specification are documented here. The format
follows [Keep a Changelog](https://keepachangelog.com), and the spec follows
[Semantic Versioning](https://semver.org).

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
- A complete fictional worked example (`examples/personal-avery-quinn`).
- Dual licensing: MIT for templates/schema/code, CC-BY 4.0 for specification prose.

[1.0.0]: https://vibegraph.md
