# vibegraph.md specification

**Version 2.0** · September 2026 · [vibegraph.md](https://vibegraph.md)

This document defines the file convention for a vibegraph: the reference layout, VIBEGRAPH.md (the root file), the typed link schema, scopes and when rules, the node files, the handoff stanza, how AI systems consume a vibegraph, and the acceptance test. It is written for people building a vibegraph by hand and for developers building tools that produce, serve, or consume one. The [whitepaper](whitepaper/vibegraph-whitepaper.md) explains the reasoning; [vibegraph.ai](https://vibegraph.ai) is one builder that exports this layout; [`examples/maya-okafor.vibegraph/`](examples/maya-okafor.vibegraph) is a complete worked example.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** carry their usual specification meaning: required, forbidden, recommended, discouraged, optional.

Specification prose is CC-BY 4.0; templates, schema, and code are MIT. See [Licensing](#11-licensing).

---

## Table of contents

1. [Overview](#1-overview)
2. [The reference layout](#2-the-reference-layout)
3. [The root file: VIBEGRAPH.md](#3-the-root-file-vibegraphmd)
4. [The typed link schema](#4-the-typed-link-schema)
5. [Node files](#5-node-files)
6. [The handoff stanza and placement modes](#6-the-handoff-stanza-and-placement-modes)
7. [Scopes, grants, and serving](#7-scopes-grants-and-serving)
8. [How AI systems consume a vibegraph](#8-how-ai-systems-consume-a-vibegraph)
9. [The acceptance test](#9-the-acceptance-test)
10. [Conformance checklist](#10-conformance-checklist)
11. [Licensing](#11-licensing)
12. [Versioning](#12-versioning)

---

## 1. Overview

A **vibegraph** is the network of identity, context, knowledge, and memory that governs how AI thinks, writes, and acts for one person, and any businesses they own or operate.

Every vibegraph has five elements, anchored to one person:

- **The identity core.** A human-authored statement of who the person is: personality (the Big Five, the Enneagram, and any other instruments the owner has taken, reconciled in an integrated reading) and purpose (a four-pillar Ikigai). Small, stable, and safe to share.
- **Brands.** One personal brand built from the identity core, and any business brands the owner operates. Each brand has twelve Brand Context elements (its words) and eight Brand Visuals elements (its look). A business brand adds organizational foundations.
- **Areas.** Domains of knowledge and working context the owner adds when a use case demands one (career, skills, goals, finances; on the business side CRM, operations, playbooks and SOPs, templates). Each area is a folder with its own scope.
- **Components.** The tools that already hold parts of the graph: a notes app, a memory layer, a project with its own AGENTS.md, a skill, an agent. Registered, not stored.
- **The root file.** VIBEGRAPH.md. It names the owner, links every node with a kind, a scope, and a when rule, and states the read order. Any agent reads it first.

A vibegraph is plain markdown at its simplest. Implementations MAY add hosting, encryption, and access control, but a folder of markdown files that follows this document is a complete, valid vibegraph.

### 1.1 Design goals

1. **Human-readable.** If you can read markdown, you can read and edit a vibegraph. No tooling required.
2. **Useful with zero adoption.** Value arrives the moment the owner pastes the core into any AI tool.
3. **One person per vibegraph.** A vibegraph represents exactly one human. Business brands nest inside their owner's vibegraph. Nothing in this specification pools graphs across people.
4. **Nothing exposed by omission.** Every link carries a scope. Anything without one is private.
5. **Portable.** Files, not a service. A vibegraph moves across tools, models, and vendors unchanged.

A standalone organizational vibegraph (a company with no human anchor) is not defined in this version.

---

## 2. The reference layout

```
maya-okafor.vibegraph/                 zip: maya-okafor.vibegraph.zip
├── VIBEGRAPH.md                       REQUIRED. Root file. Fixed name. Read first.
├── AGENTS.md                          OPTIONAL. The handoff stanza only.
├── CLAUDE.md                          OPTIONAL. The same stanza (Claude Code reads CLAUDE.md).
├── README.md                          OPTIONAL. What this is, the paste test, how to add an area.
├── identity/
│   └── maya-okafor.md                 REQUIRED. The identity core.
├── brands/
│   ├── maya-okafor.brand.md           The personal brand: 12 + 8.
│   ├── delivery-os.brand.md           A business brand: foundations + 12 + 8.
│   └── assets/
│       └── README.md                  Where the visual assets live, plus any asset files.
├── areas/
│   ├── README.md                      OPTIONAL. How to add an area.
│   ├── career/index.md                One folder per area, each with an index.md.
│   ├── skills/
│   │   ├── index.md
│   │   └── client-kickoff.SKILL.md    Skills in SKILL.md form.
│   ├── goals/index.md
│   └── finances/index.md
└── components.md                      Registry of tools that hold parts of the graph.
```

Rules:

- **The folder** is named `<owner-slug>.vibegraph`. When zipped, the archive is `<owner-slug>.vibegraph.zip` and contains the folder.
- **VIBEGRAPH.md MUST exist** at the root of the folder with exactly that name, capitalized, to match AGENTS.md and CLAUDE.md.
- **The identity file MUST exist** at `identity/<owner-slug>.md`, and the root file's `identity` front matter MUST point to it. It is named after the person, not `identity.md`, so a folder can hold two people's files side by side without collision.
- **Brand files** live in `brands/` and carry the `.brand.md` suffix. The personal brand is `brands/<owner-slug>.brand.md`. Each business brand is `brands/<brand-slug>.brand.md`. A vibegraph has at most one personal brand.
- **Brand assets** live in `brands/assets/`. When the folder exists it MUST contain a `README.md` that lists every visual asset location for every brand (see [§5.4](#54-brandsassetsreadmemd)). Asset files MAY sit beside it; external assets are recorded as locations.
- **Areas** are folders in `areas/`, one per area, each with an `index.md`. An area MAY hold any number of further files, linked from its `index.md`. The skills area holds procedures as `<name>.SKILL.md` files.
- **Components** are registered in `components.md` at the root (see [§5.6](#56-componentsmd)). A component's content is never copied into the vibegraph.
- **Slugs** are lowercase, hyphenated forms of display names (`Maya Okafor` becomes `maya-okafor`). A producer MUST reject, at input time, a slug that is empty, that collides with another brand's slug or with the owner's slug, or that claims a reserved name: `vibegraph`, `identity`, `brands`, `assets`, `areas`, `components`, `readme`, `agents`, `claude`. A producer MUST NOT rename a slug at export time.
- **Reachability.** Every markdown file in the folder MUST be reachable by following relative links from VIBEGRAPH.md, except the fixed-name helper files `AGENTS.md`, `CLAUDE.md`, `README.md`, and `areas/README.md`. Every relative link MUST resolve to a file that exists.
- **Partial vibegraphs are valid.** A producer exports what has been built. The minimal vibegraph is VIBEGRAPH.md plus the identity file; the minimal useful one adds the personal brand.

---

## 3. The root file: VIBEGRAPH.md

VIBEGRAPH.md is the orchestrator. An agent handed only this file knows who it emulates, what exists, what to read first, and what it may not read.

### 3.1 Front matter

```yaml
---
vibegraph: "2.0"
owner: Maya Okafor
identity: identity/maya-okafor.md
updated: 2026-09-30
---
```

| Field | Required | Value |
|---|---|---|
| `vibegraph` | Yes | The specification version this vibegraph targets, as a quoted string. `"2.0"` for this document. |
| `owner` | Yes | The person's display name. |
| `identity` | Yes | Relative path to the identity file. |
| `updated` | Yes | ISO 8601 date of the last change to any part of the vibegraph. |

Producers MAY add further fields. Consumers MUST ignore fields they do not recognize.

### 3.2 Body

The body has, in this order:

1. A title: `# <Owner>'s vibegraph`.
2. The orientation, which SHOULD be these three sentences verbatim:

   ```
   Read this file first. It tells you who you emulate and where everything else lives.
   Read entries marked `when: always` before any task. Read `when: on-task` entries only when the
   task needs them. Never read `scope: private` entries unless the owner has granted them for this session.
   ```

3. `## Identity`: exactly one entry, the identity file.
4. `## Brands`: one entry per brand file, the personal brand first. Omitted when there are no brands.
5. `## Areas`: one entry per area, linking the area's `index.md`. Omitted when there are no areas.
6. `## Components`: a link to `components.md`, followed by one summary entry per component (entries without a link target, see [§4.1](#41-entry-grammar)). Omitted when there are no components.
7. `## Read order`: a numbered list. The identity file first, the personal brand second, then the rule for everything else. It SHOULD end with `nothing else without a grant`.

### 3.3 Complete example

```markdown
---
vibegraph: "2.0"
owner: Maya Okafor
identity: identity/maya-okafor.md
updated: 2026-09-30
---

# Maya Okafor's vibegraph

Read this file first. It tells you who you emulate and where everything else lives.
Read entries marked `when: always` before any task. Read `when: on-task` entries only when the
task needs them. Never read `scope: private` entries unless the owner has granted them for this session.

## Identity
- [Maya Okafor](identity/maya-okafor.md) · kind: identity · scope: public · when: always

## Brands
- [Maya Okafor (personal brand)](brands/maya-okafor.brand.md) · kind: brand · type: personal · scope: public · when: always
- [Delivery OS](brands/delivery-os.brand.md) · kind: brand · type: business · scope: public · when: on-task (any Delivery OS writing, design, or publishing)

## Areas
- [Career](areas/career/index.md) · kind: area · scope: scoped · when: on-task (resume, bio, client applications)
- [Skills](areas/skills/index.md) · kind: area · scope: scoped · when: on-task (any repeatable workflow)
- [Goals](areas/goals/index.md) · kind: area · scope: scoped · when: on-task (planning, prioritization)
- [Finances](areas/finances/index.md) · kind: area · scope: private · when: on-grant

## Components
See [components.md](components.md). Summary:
- Obsidian vault "Notes" · kind: source · scope: scoped · locator: ~/Notes
- Claude memory · kind: memory · scope: scoped · seeded from this vibegraph on 2026-09-30
- Delivery OS site repo · kind: project · scope: scoped · locator: github.com/deliveryos/site (has its own AGENTS.md)
- Writing agent · kind: agent · reads: identity, brands, areas/skills · never: areas/finances

## Read order
1. identity/maya-okafor.md
2. brands/maya-okafor.brand.md
3. the brand or area the task names
4. nothing else without a grant
```

---

## 4. The typed link schema

### 4.1 Entry grammar

Every entry in the root file is one markdown list item on one line:

```
entry    = "- " target *( " · " segment )
target   = markdown-link | name
segment  = pair | note
pair     = key ": " value [ " (" hint ")" ]
```

- The separator is a middle dot (U+00B7) with one space on each side. Parsers SHOULD tolerate extra whitespace around it.
- `target` is a markdown link to a relative path for identity, brand, and area entries, and a plain name for component summary entries.
- A `segment` that is not a `key: value` pair is a note for people. Parsers MUST ignore notes.
- A `hint` in parentheses after a value names the tasks or conditions it applies to, for example `when: on-task (any Delivery OS writing, design, or publishing)`.

The line is deliberately plain: readable by a person, greppable by a script, parseable by an agent without a JSON schema.

### 4.2 Keys

| Key | On | Required | Values |
|---|---|---|---|
| `kind` | every entry | Yes | `identity`, `brand`, `area`, `source`, `memory`, `project`, `skill`, `agent` |
| `scope` | identity, brand, and area entries; component summaries SHOULD | Yes | `public`, `scoped`, `private` |
| `when` | identity, brand, and area entries | Yes | `always`, `on-task`, `on-grant` |
| `type` | brand entries | Yes | `personal`, `business` |
| `locator` | component entries | No | Where the component lives: a path, URL, or repository |
| `reads` | agent components | No | Comma-separated node paths the agent may read |
| `never` | agent components | No | Comma-separated node paths the agent must not read |

**kind** names what the node is: `identity` (the identity file), `brand` (a brand file), `area` (an area folder), `source` (an external knowledge store), `memory` (an external memory layer), `project` (a repository or workspace with its own AGENTS.md), `skill` (a SKILL.md procedure), `agent` (an agent or vibeclone that consumes the graph).

**scope** names who may read the node: `public` (safe to share with any tool), `scoped` (exposed to named tools or purposes), `private` (never exposed without an explicit grant).

**when** names when to read it: `always` (before any task), `on-task` (only when the task needs it, with the tasks named in the hint), `on-grant` (only after the owner grants it for the session).

**type**, on brands only: `personal` or `business`.

### 4.3 Rules

- **Deny by default.** An entry without a `scope` MUST be treated as `private`. An entry without a `when` MUST be treated as `on-grant`.
- **Private means on-grant.** An entry with `scope: private` MUST carry `when: on-grant`.
- **Always means public.** An entry with `when: always` SHOULD carry `scope: public`.
- **The identity entry** SHOULD be `scope: public · when: always`.
- **The personal brand** SHOULD be `type: personal · scope: public · when: always`. **Business brands** SHOULD be `type: business · when: on-task` with a hint naming the business's tasks, so the founder's voice governs by default and the business governs its own work.
- **Areas** SHOULD be `scoped` or `private`, never `public` unless the owner says so.
- **The root file is authoritative.** When a node file's front matter disagrees with its root file entry, the root file wins.

---

## 5. Node files

Every node file MAY begin with YAML front matter mirroring its root file entry, followed by an ordinary markdown body. Write bodies the way you want an AI to read them back: declarative and specific. "I write in second person, short sentences, no hedging" beats "professional but approachable."

| File | Front matter |
|---|---|
| `identity/<owner-slug>.md` | `kind: identity`, `owner`, `scope`, `when`, `updated` |
| `brands/<slug>.brand.md` | `kind: brand`, `type`, `brand` (display name), `owner`, `scope`, `when`, `updated` |
| `areas/<area>/index.md` | `kind: area`, `area` (display name), `scope`, `when`, `updated` |
| `components.md` | `owner`, `updated` |

### 5.1 The identity file

The identity file holds the identity core. Producers SHOULD use these headings, in this order:

```markdown
# <Owner>

## Rules
## Personality
### Big Five
### Enneagram
### Other instruments
### Integrated reading
## Purpose
### Ikigai
### Ikigai statement
```

- **Rules** state how an AI working for or as the owner should use the file: voice, what to lead with, what never to do. It comes first because it is the part every consumer needs.
- **Big Five**: the instrument used (the reference is the public-domain IPIP-NEO-120), the five domain scores on that instrument's own scale with their level, and facet notes. Dimensional scores are what a machine can use.
- **Enneagram**: type, wing, core desire, core fear, and the stress and growth patterns.
- **Other instruments**: any further assessment the owner has taken (16personalities, CliftonStrengths, DISC, HEXACO, and so on). Each is recorded as a named source with the figures and scale words exactly as its document printed them. A producer MUST NOT convert another instrument's result onto the Big Five or Enneagram scale.
- **Integrated reading**: the written interpretation that reconciles every instrument, in the owner's own words after review: where they agree, where they pull against each other, and what the combination means for how the owner works, decides, and communicates. This is the section most consumers use.
- **Ikigai**: four pillars kept distinct (what I love, what the world needs from me, what I am naturally good at, what I can be paid for) and where they meet. **Ikigai statement**: the single sentence the rest of the vibegraph builds on.

A section with no content yet MAY be omitted.

### 5.2 Brand files

A brand file composes one brand. Producers SHOULD use these headings, in this order:

```markdown
# <Brand name>

## Foundations                (business brands only)
### Brand Personality
### Archetype
### Golden Circle
### Mission, Vision, Values
### AI Instruction

## Brand Context
### Brand Name
### Taglines & Slogans
### Unique Value Proposition
### Purpose-Vision-Mission
### Core Values
### Tone & Voice
### Messaging & Narratives
### Keywords & Phrases
### Bio (Short/Long)
### Achievements & Awards
### Inspiration & Influence
### Online Presence

## Brand Visuals
### Symbols & Logos
### Color Palette
### Typography
### Iconography
### Brand Imagery
### Illustration Style
### Visual Elements
### Photography
```

**Brand Context** is the brand in words. Each element is a small artifact with a defined shape: core values as decision filters with the behavior that proves them, a value proposition in one sentence, messaging as repeatable statements each paired with the story that makes it believable. **Taglines & Slogans** lists the durable tagline first, then situational slogans.

**Brand Visuals** is the brand in pictures, recorded as concrete artifacts: hex values, typeface names and weights, a described logo, imagery and photography rules. The section SHOULD open with a link to `assets/README.md`. This specification records and links visuals; it does not require any tool to produce them.

**Foundations** appear only in business brands, in place of the identity core that a personal brand is built from:

- **Brand Personality**: Jennifer Aaker's five dimensions (Sincerity, Excitement, Competence, Sophistication, Ruggedness), each with a level and how it shows up, plus a one-line brand personality.
- **Archetype**: a primary and optional secondary Jungian archetype, why, and how it shows up.
- **Golden Circle**: Why, How, What. The Why SHOULD be checked against the owner's own purpose in the same vibegraph.
- **Mission, Vision, Values**: the conventional statements, with values as a table.
- **AI Instruction**: how an AI should write and design for the business, including how its voice relates to the founder's.

In a business brand, **Messaging & Narratives** also carries the category point of view and the audience, and **Bio (Short/Long)** carries the boilerplates the business repeats. **Visual Elements** also names the templates the business produces repeatedly.

### 5.3 Brand Visuals asset locations

Each Brand Visuals element records two things: its value, and where its assets live. A location is one of:

| Locator kind | Example |
|---|---|
| `url` | `https://maya-okafor.example/brand/photos` |
| `figma` | a Figma file or frame link |
| `drive` | a shared drive folder link |
| `local-path` | `~/vibegraph/brands/assets/wordmark.svg` |
| `upload` | a file inside `brands/assets/`, linked relatively |

### 5.4 `brands/assets/README.md`

Lists every asset location for every brand, one section per brand, as a table with the columns Element, Asset, Location, Locator kind, and Tool. Files inside `brands/assets/` are linked relatively; external locations are written as plain text or absolute URLs.

### 5.5 Areas

An area is a folder with an `index.md`. The index names the area, states what it covers, and links or locates its contents. Areas are where depth and sensitivity live, so they SHOULD be `scoped` or `private` and stay home when the core travels. A producer that does not host area content SHOULD export areas as scaffolds: an `index.md` with front matter and a short description of what belongs there.

Suggested areas, to rename, merge, and extend freely:

- **Personal:** career, skills, goals, finances, health, relationships, notes and ideas.
- **Business:** relationships and CRM, finances, operations, playbooks and SOPs, management routines, templates, goals.

The skills area holds procedures as `<name>.SKILL.md` files in the SKILL.md format, so harnesses that already read that format load them directly.

### 5.6 `components.md`

The registry of tools that already hold parts of the graph. One table row per component:

| Column | Required | Value |
|---|---|---|
| Name | Yes | The component as the owner calls it, for example `Obsidian vault "Notes"` |
| kind | Yes | `source`, `memory`, `project`, `skill`, `agent` |
| scope | Yes | `public`, `scoped`, `private`; producers SHOULD default to `scoped` |
| locator | No | Path, URL, or repository |
| seeded | No | ISO date the owner seeded the component from this vibegraph |
| notes | No | Free text; for agents, what it reads and never reads |

Every component in `components.md` SHOULD have a summary entry under `## Components` in the root file, and the reverse.

Common placements: note apps and knowledge stores (Obsidian, Logseq, Notion, Tana) are `source`; memory layers and platform memory (Mem0, Zep, Letta, ChatGPT memory, Claude memory) are `memory`; repositories and agent folders with AGENTS.md or CLAUDE.md are `project`; SKILL.md files are `skill`; a vibeclone or any agent that reads the graph is `agent`. Outward-facing clone platforms consume only the public slice of the core.

---

## 6. The handoff stanza and placement modes

### 6.1 The handoff stanza

Put this in AGENTS.md, and the same text in CLAUDE.md, in any repository or workspace the owner works in. A producer that writes AGENTS.md or CLAUDE.md MUST write these four lines byte for byte:

```markdown
## Who you emulate
Before starting, read `VIBEGRAPH.md` (in this repo, or at `~/vibegraph/VIBEGRAPH.md`).
It defines the person and brands this work belongs to. Follow its read order and scopes.
Do not read entries marked `scope: private` unless they have been granted for this session.
```

Both files are needed: Codex, Cursor, Copilot, and Gemini CLI read AGENTS.md; Claude Code reads CLAUDE.md. Where a repository already has either file, the stanza is appended to it.

### 6.2 Placement modes

- **Standalone.** The vibegraph lives in its own folder, conventionally `~/vibegraph/`, and repositories point to it with the stanza.
- **Embedded.** The core (VIBEGRAPH.md, the identity file, and the brand files) is copied into a project that needs it, and the areas stay home. Links to areas that are not present in the project remain in the root file; consumers MUST treat a missing linked file as not granted, not as an error.

The root file is the same in both modes.

---

## 7. Scopes, grants, and serving

A complete vibegraph is a concentrated dossier. The scope vocabulary in [§4](#4-the-typed-link-schema) is its permission model.

### 7.1 Rules for every consumer

- **Deny by default.** Anything without a scope is private.
- **Scoped means named.** A `scoped` node is exposed only to the tools or purposes the owner has named. A `scoped` node with no grant behaves as `private`.
- **Private is inviolable.** A consumer MUST NOT read a `private` node without a grant from the owner for the current session.
- **Load only what the task needs.** Read `when: always` nodes first, `on-task` nodes when the task names them, and nothing else.

### 7.2 Serving a vibegraph

An implementation that serves a vibegraph to agents (for example, over the [Model Context Protocol](https://modelcontextprotocol.io)):

- MUST serve the same layout this document defines, rendered from the same source as any export, so the hosted graph and the local graph are the same shape.
- MUST hold grants per client and per node. A client's default grant SHOULD be the nodes marked `scope: public` and `when: always`.
- MUST omit from the served root file every entry the client is not granted.
- MUST log every read (client, node path, kind, scope, time) and make the log visible to the owner, so the owner can always answer "what has this tool actually seen?"
- SHOULD map kinds to resource types, so a client can request `identity`, `brand`, or `area` nodes by kind.
- MUST NOT expose the whole graph as a single undifferentiated resource.

Write-back is not defined in this version.

The rationale is prompt injection, which can be contained but not eliminated: a manipulated agent cannot leak a node it was never granted.

### 7.3 Hosting postures

- **Local (reference posture).** Files on hardware the owner controls. Only the nodes the owner deliberately exposes leave the machine.
- **Hosted.** A hosted service SHOULD state plainly what it can and cannot read. Client-side, zero-knowledge encryption is the recommended destination for hosted storage; a service MUST NOT describe itself as zero-knowledge until it is.

---

## 8. How AI systems consume a vibegraph

Four modes, in increasing order of sophistication. Only the first is required to get value.

1. **Direct context.** Paste VIBEGRAPH.md, the identity file, and one brand file into any chat, or attach them. Works today, in every AI product. The canonical mode.
2. **Persistent workspace context.** Load the same files into a persistent surface (a Claude Project, a custom GPT, project instructions) so every conversation there starts calibrated.
3. **Live access over MCP.** Serve the layout under [§7.2](#72-serving-a-vibegraph): kinds become resource types, scopes become grants, when rules set what a client sees before asking, and every read is logged.
4. **Seeding memory layers.** Load the core as seed context into a memory system to solve its cold start with an owner-authored foundation that observation then extends. The memory layer is the substrate; the vibegraph is the schema.

The minimal correct consumer behavior: read VIBEGRAPH.md first, follow its read order, respect every scope, and load only what the task needs.

> **For toolmakers:** a vibegraph is structured markdown. If your product accepts text, it already supports vibegraphs. Deeper support (an import that parses the root file and honors scopes, or an MCP client that requests nodes by kind) is welcome and straightforward.

---

## 9. The acceptance test

Open a fresh session in any model. Paste VIBEGRAPH.md, the identity file, and one brand file. Ask for a piece of work the owner does often. The output should sound like the owner on the first generation. If it does not, the core is incomplete, not the tool.

---

## 10. Conformance checklist

A producer's export conforms to this specification when:

1. `VIBEGRAPH.md` exists at the root of `<owner-slug>.vibegraph/`, with exactly that name.
2. Its front matter has `vibegraph`, `owner`, `identity`, and `updated`, and `identity` points to a file that exists.
3. The body has `## Identity` with one entry and `## Read order`, and every other section present is one of `## Brands`, `## Areas`, `## Components`, in that order.
4. Every entry carries `kind`; identity, brand, and area entries carry `scope` and `when`; brand entries carry `type`.
5. Every `scope: private` entry carries `when: on-grant`.
6. Every relative link in every file resolves to a file that exists.
7. Every markdown file is reachable from VIBEGRAPH.md, except `AGENTS.md`, `CLAUDE.md`, `README.md`, and `areas/README.md`.
8. There is at most one `type: personal` brand, and brand slugs are unique, differ from the owner's slug, and claim no reserved name.
9. If `brands/assets/` exists, it contains `README.md`.
10. Every area folder contains `index.md`.
11. If `AGENTS.md` or `CLAUDE.md` exists, it contains the handoff stanza in [§6.1](#61-the-handoff-stanza) byte for byte.

JSON Schemas for the front matter of the root file and the node files are in [`schema/`](schema).

---

## 11. Licensing

- **Templates, schema files, and code:** MIT ([`LICENSE`](LICENSE)). Copy them, ship them, build products on them.
- **Specification prose and documentation** (this file, the README, the whitepaper text): CC-BY 4.0 ([`LICENSE-docs`](LICENSE-docs)). Quote and adapt it; keep attribution.

"vibegraph" is a common noun and carries no trademark. Anyone can build a vibegraph by hand, and anyone can build products that produce, serve, or consume one without asking. An identity standard that is not open is not a standard.

---

## 12. Versioning

This document is version 2.0, and a vibegraph that targets it declares `vibegraph: "2.0"` in its root file.

Versions are `MAJOR.MINOR`:

- **MAJOR** for breaking changes to required structure or field meaning.
- **MINOR** for backward-compatible additions: new optional fields, new suggested areas, new component placements.
- Clarifications and corrections that change no structure are made in place and recorded in the changelog without a new number.

Consumers SHOULD accept any vibegraph whose MAJOR version matches one they support. Changes are recorded in [`CHANGELOG.md`](CHANGELOG.md).

---

<div align="center">

**[vibegraph.md](https://vibegraph.md)** is the open framework for a vibegraph. Build the center of yours the guided way at **[vibegraph.ai](https://vibegraph.ai)**.

</div>
