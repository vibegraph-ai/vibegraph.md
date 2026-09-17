# Changelog

All notable changes to the vibegraph.md specification are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com).

## [3.0] (October 10, 2026)

Context Sources and Areas become two concepts with a stated relationship, areas ship only when chosen and carry typed entries, and a vibegraph can be built for a business by someone who took no instruments.

### Added
- **`role`** in the root file and identity file front matter: `owner`, `staff`, or `agency`; absent means `owner`.
- **Area entries:** every `areas/<slug>/index.md` lists its contents under `## Entries` in the root file's entry grammar, with `scope`, `when`, a required **`access`** route (`file`, `link`, `mcp`, `ask`), and an optional **`in`** naming the context source that holds it.
- **The recommended area vocabulary:** nine personal areas and five business areas, with `area:` still free text.
- **A `slug` column** in `context-sources.md`, which `in:` refers to.
- **Optional identity sections:** Personality and Purpose may be absent; Rules and the title are enough.
- **Optional brand elements**, in fixed order; a personal-use brand file with seven Brand Context elements is valid.
- **Conformance rules 10 to 12:** `access` from the closed set, `in` naming a registered slug, unique lowercase-hyphenated slugs.
- **A fourth orientation sentence** in the root file, stating how sources and areas relate.
- The rule that a vibegraph never carries a credential (§4.3, §7.1).

### Changed
- **Components are now Context Sources:** `components.md` is `context-sources.md`, `## Components` is `## Context Sources`, and the section sits before `## Areas`.
- **Areas ship only when chosen.** No fixed scaffold; no `areas/` folder when there are none.
- `context-sources` joins the reserved names.
- Version 3.x.

### Removed
- The always-present career, skills, and goals scaffolds.
- The `components.md` name and the `## Components` section.

### Migration
For a hand-maintained 2.0 vibegraph:
- Bump `vibegraph:` to `"3.0"` in the root file's front matter.
- Rename `components.md` to `context-sources.md`, and add its `slug` column.
- Rename `## Components` to `## Context Sources` in the root file, and move it before `## Areas`.
- Add `## Entries` to each area's `index.md`, with `scope`, `when`, and `access` on every line.
- Keep only the areas you actually use; drop the rest, and drop `areas/` entirely if none remain.

## [2.0] (September 30, 2026)

The reference layout release. The specification now describes a vibegraph as five elements anchored to one person (the identity core, brands, areas, components, and the root file) and matches the whitepaper of the same version.

### Added
- **The reference layout:** `<owner-slug>.vibegraph/` with `VIBEGRAPH.md`, `identity/<owner-slug>.md`, `brands/<slug>.brand.md`, `brands/assets/README.md`, `areas/<area>/index.md`, `components.md`, and optional `AGENTS.md`, `CLAUDE.md`, and `README.md`.
- **VIBEGRAPH.md, the root file:** a fixed, capitalized name; front matter `vibegraph`, `owner`, `identity`, `updated`; the orientation; Identity, Brands, Areas, Components, and Read order sections.
- **The typed link schema:** every root file entry is one markdown line with `kind`, `scope`, `when`, and on brands `type`, separated by a middle dot.
- **Scopes** `public`, `scoped`, `private`, deny by default, and **when rules** `always`, `on-task`, `on-grant`.
- **Areas:** owner-defined domains as folders with their own index and scope.
- **Components:** a registry of tools that already hold parts of the graph, with kinds `source`, `memory`, `project`, `skill`, `agent`.
- **The handoff stanza:** four lines for AGENTS.md and CLAUDE.md, written byte for byte by producers, and the standalone and embedded placement modes.
- **Other instruments** in the identity file, recorded as named sources with their own figures and scale words, never converted.
- **Brand Visuals as recorded elements:** values plus asset locations (`url`, `figma`, `drive`, `local-path`, `upload`) listed in `brands/assets/README.md`.
- **Business brand Foundations:** Brand Personality, Archetype, Golden Circle, Mission, Vision, Values, and AI Instruction.
- **Serving rules:** the same layout served per client under grants, private entries omitted, every read logged.
- **The acceptance test** and a **conformance checklist** for producers.
- **The worked example** `examples/maya-okafor.vibegraph/` and a blank template `templates/your-name.vibegraph/`.
- JSON Schemas `schema/vibegraph-root.schema.json` and `schema/vibegraph-node.schema.json`.

### Changed
- The Brand Context element order leads with **Taglines & Slogans** (the durable tagline first, then situational slogans).
- Brand files group their elements under `## Brand Context` and `## Brand Visuals`, with each element as a `###` heading.
- Version numbers are `MAJOR.MINOR`, aligned with the whitepaper.

### Removed
- The owner-named master file and the flat owner-named tree of the 2.0.0 draft.
- The earlier third part for domain context and its pointer documents. Areas replace it.

## [2.0.0-draft] (August 11, 2026, superseded, never released as an export to a user)

A draft that described a flat, owner-named tree: an `<owner>.vibegraph.md` master file with a link-checked read order, separate personality, Ikigai, and brand documents, an assets folder, and pointer documents for a third part holding domain context. It introduced Brand Context and Brand Visuals as the names of the brand's two halves and the Big Five plus Enneagram personality layer. There is no tag for this draft. It was superseded by 2.0 before any user received an export in its layout.

## [1.0.0] (July 11, 2026)

The first public release.

### Added
- A two-part architecture: a core identity (`core/`) and a part for domain context (`modules/`).
- The `VIBEGRAPH.md` manifest convention with YAML front matter.
- A per-document schema with `section`, `visibility`, `scope`, and `updated` fields.
- Personal and business core instrument sets.
- A deny-by-default permission model with `private`, `scoped`, and `public` visibility.
- Guidance for AI consumption: direct context, persistent workspace context, live access over MCP, and memory-layer seeding.
- Personal and business templates with inline guidance.
- Dual licensing: MIT for templates, schema, and code; CC-BY 4.0 for specification prose.
