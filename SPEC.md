# The Vibegraph Specification

**Version 2.0.0** · August 2026 · [vibegraph.md](https://vibegraph.md)

This document defines the vibegraph format: its file tree, the master file, the per-document schema, the permission model, and the conventions by which AI systems consume a vibegraph. It is written to be read by humans building a vibegraph by hand, and by developers building tools that produce or consume one. The Vibegraph Whitepaper v1.5 describes this version of the specification, and the application at [vibegraph.ai](https://vibegraph.ai) is its reference implementation.

The specification prose is licensed CC-BY 4.0; the templates and schema files are MIT. See [Licensing](#8-licensing).

> **Terminology.** The key words used throughout (a *vibegraph*, its *Core Identity*, its *Branding*, its *Orbits*, and the *elements* inside a brand document) are defined in the whitepaper and summarized in [§1](#1-overview). Where this document says an implementation **MUST**, **SHOULD**, or **MAY** do something, those words carry their ordinary specification meaning (roughly: required, recommended, optional).

---

## Table of contents

1. [Overview](#1-overview)
2. [File tree and naming](#2-file-tree-and-naming)
3. [The master file](#3-the-master-file)
4. [Document schema](#4-document-schema)
5. [The three parts](#5-the-three-parts)
6. [Security & the permission model](#6-security--the-permission-model)
7. [How AI systems consume a vibegraph](#7-how-ai-systems-consume-a-vibegraph)
8. [Licensing](#8-licensing)
9. [Versioning](#9-versioning)

---

## 1. Overview

A **vibegraph** is a set of Markdown files that codifies one person's identity and working context in a form AI systems can consume. A vibegraph represents a unique individual; the businesses that person owns are represented as business brands inside it.

It has three parts:

- **Core Identity**: *who you are.* Personality (a two-part assessment: the Big Five and the Enneagram, reconciled in an integrated reading) and Ikigai (purpose). Small, stable, and safe to share with any AI tool.
- **Branding**: *how you present.* One brand document per brand, composed of the brand's words (Brand Context, twelve elements) and its look (Brand Visuals, eight elements). The owner's personal brand is always present once built; business brands the owner operates sit beside it.
- **Orbits**: *your personal domain context.* Self-defined domains (health, finances, career, operations, and so on) containing the documents, data, and protocols of a life or business. Orbits are where depth and sensitivity live. In an exported vibegraph they appear as pointer documents; the content itself stays home in the owner's own tools, which is the permission model made structural (see [§6](#6-security--the-permission-model)).

A vibegraph is **plain Markdown at its simplest**: a handful of files you can read, edit, and paste anywhere. Implementations MAY layer encryption, hosting, and access control on top, but a bare folder of Markdown is a valid, complete vibegraph.

Brand documents carry a **kind**: `personal` (exactly one, the owner's) or `business` (zero or more). The two kinds share the same structure and differ in which instruments populate their foundations (see [§5](#5-the-three-parts)). A standalone organization-owned vibegraph is not defined in this version; if added later, it will arrive as a MAJOR revision.

### Design goals

1. **Human-readable.** If you can read Markdown, you can read and edit a vibegraph. No tooling required.
2. **Useful with zero adoption.** Value arrives the moment the owner pastes it into an existing AI tool. No platform needs to support anything.
3. **Portable and owner-controlled.** A vibegraph is a file format, not a service. It moves across tools, models, and vendors unchanged.
4. **Private by default.** The shareable parts travel; the orbits stay home unless the owner deliberately serves them.
5. **Extensible.** Start with the Core Identity and Branding; add orbits only when a real use case demands one.

---

## 2. File tree and naming

A vibegraph is delivered as a flat directory (canonically zipped as `<owner-slug>-vibegraph.zip`) whose files are named after their owner:

```
jordan-lee-vibegraph.zip
├── jordan-lee.vibegraph.md      # REQUIRED: the master file, read first
├── jordan-lee.vibegraph.pdf     # OPTIONAL: human-readable rendering
├── jordan-lee.personality.md    # Core Identity
├── jordan-lee.ikigai.md         # Core Identity
├── jordan-lee.brand.md          # Branding: the personal brand
├── acme-studio.brand.md         # Branding: one per business brand (optional)
├── brand-kit-checklist.md       # OPTIONAL: asset to-do list, for humans
├── assets/                      # OPTIONAL: generated brand assets
│   └── logo-1.png …
└── orbits/                      # OPTIONAL: one pointer document per orbit
    ├── health.md
    └── finances.md
```

Rules:

- **The master file MUST exist** and is named `<owner-slug>.vibegraph.md`. It is the file an AI or tool reads first (see [§3](#3-the-master-file)).
- **Names are lowercase-hyphenated slugs** of the owner's and brands' display names (`Jordan Lee` becomes `jordan-lee`). Producers MUST reject, at input time, any name whose slug is empty, collides with another brand's slug, collides with the owner's slug, or claims a reserved name. The reserved slugs are `assets`, `orbits`, and `vibegraph`. A producer MUST NOT silently rename at export time.
- **Every document is optional except the master.** A vibegraph exports whatever has been built so far; the master links exactly what exists. A Core-and-Branding-only vibegraph is valid and useful.
- **One brand document per brand.** The personal brand is `<owner-slug>.brand.md`; each business brand is `<brand-slug>.brand.md`. A brand document composes the brand's Context and Visuals into a single file.
- **Orbits are pointer documents.** `orbits/<orbit-slug>.md` records that the orbit exists, what it covers, and which external tool holds its content. Orbit content itself is NOT exported by default (see [§5.4](#54-orbits) and [§6](#6-security--the-permission-model)).

> **Compatibility.** Version 1.0 of this specification defined a nested tree (`core/` and `modules/`) with per-concept filenames (`brand-positioning.md`, `brand-aesthetics.md`). Consumers MAY accept that layout as a v1.0 vibegraph, and SHOULD treat a `modules/` directory as synonymous with `orbits/`. Producers MUST emit the v2.0 tree.

---

## 3. The master file

`<owner-slug>.vibegraph.md` is the orchestrator: the top of the food chain. An AI handed only this file knows what else exists and what to read first.

### 3.1 Front matter

```yaml
---
vibegraph_version: 2.0          # REQUIRED: spec version this vibegraph targets
owner: "Jordan Lee"             # REQUIRED: the person's display name
updated: "2026-08-11"           # REQUIRED: ISO 8601 date of last change
---
```

| Field | Required | Values | Notes |
|---|---|---|---|
| `vibegraph_version` | Yes | string | The spec version. `2.0` for this document; consumers SHOULD accept any `2.x`. |
| `owner` | Yes | string | The person's display name. |
| `updated` | Yes | ISO 8601 date | Last modification of any part of the vibegraph. |

### 3.2 Body

The body opens with a title (`# <Owner> | Vibegraph`), a one-paragraph orientation stating what a vibegraph is, and a **read order**: a numbered list linking every other file in the tree, each with a one-line note. The read order is the contract: every file in the export MUST appear in it, and every entry MUST link to a file that exists.

```markdown
# Jordan Lee | Vibegraph

This is a vibegraph: a structured, portable identity for AI tools to consume.
This file is the top of the food chain: every file in this export is linked
below. Read them in order.

## Read order

1. [jordan-lee.personality.md](jordan-lee.personality.md) | Personality profile: how I think and operate.
2. [jordan-lee.ikigai.md](jordan-lee.ikigai.md) | Purpose: what I am here to do, and why.
3. [jordan-lee.brand.md](jordan-lee.brand.md) | Personal brand: voice, positioning, visuals.
4. [orbits/finances.md](orbits/finances.md) | Orbit: finances (obsidian).
```

Separators in generated prose are `:` and `|`, never an em dash.

---

## 4. Document schema

Every Markdown document in a vibegraph carries YAML front matter identifying what it is, followed by an ordinary Markdown body.

```yaml
---
section: brand                   # REQUIRED: what kind of document this is
kind: personal                   # brand documents: "personal" | "business"
brand: "Jordan Lee"              # brand documents: the brand's display name
updated: "2026-08-11"            # REQUIRED: ISO 8601
---
```

| `section` value | File | Additional fields |
|---|---|---|
| `personality` | `<owner>.personality.md` | `owner` |
| `ikigai` | `<owner>.ikigai.md` | `owner` |
| `brand` | `<slug>.brand.md` | `kind` (`personal` \| `business`), `brand` (display name) |
| `orbit` | `orbits/<slug>.md` | `orbit` (display name), `target_tool` (e.g. `obsidian`, `notion`) |

Two OPTIONAL fields extend the schema for hand-built and hosted vibegraphs that carry orbit *content* rather than pointers:

| Field | Values | Meaning |
|---|---|---|
| `visibility` | `private` \| `scoped` \| `public` | Who may see this document. See [§6](#6-security--the-permission-model). Absent means: exported documents are shareable by construction; orbit content held outside the export is private by default. |
| `scope` | list of tool/agent identifiers | Required when `visibility: scoped`; the allow-list of consumers. |

The **body** of each document is ordinary Markdown, structured for a reader: headings, short lists, plain statements. Write it the way you'd want an AI to read it back: declarative and specific. "I write in second person, short sentences, no hedging" beats "professional but approachable."

---

## 5. The three parts

### 5.1 Personality (`<owner>.personality.md`)

A full personality assessment in two parts, plus their reconciliation:

- **The Big Five (OCEAN)**, administered through a research-grade inventory (the reference implementation uses the public-domain IPIP-NEO-120): dimensional scores and facet notes. Dimensional data is what a machine consumer can use.
- **The Enneagram**: type, wing, and the motivational patterns (core desire and fear, stress and growth directions) that trait scores alone do not capture.
- **The integrated reading**: a written interpretation reconciling the two instruments, in the owner's own words after review. This is the part most AI consumers actually use; the scores remain for tools that want them.

Owners MAY import results from assessments taken elsewhere rather than retaking them.

### 5.2 Ikigai (`<owner>.ikigai.md`)

Purpose and meaning through a four-pillar structure (inspired by Kowalski's "Ikigai 2.0" treatment): what you love, what the world needs from you, what you are naturally good at, and what you can be paid for; the synthesis of where they meet; and a single Ikigai statement the rest of the vibegraph builds on.

### 5.3 Brand documents (`<slug>.brand.md`)

One document per brand, composing two halves:

**Brand Context** (the brand in words), twelve elements: Brand Name · Slogans & Taglines · Unique Value Proposition · Purpose-Vision-Mission · Core Values · Tone & Voice · Messaging & Narratives · Keywords & Phrases · Bio (Short/Long) · Achievements & Awards · Inspiration & Influence · Online Presence.

**Brand Visuals** (the brand in pictures), eight elements: Symbols & Logos · Color Palette · Typography · Iconography · Brand Imagery · Illustration Style · Visual Elements · Photography. Visual elements are concrete artifacts (hex values, type pairings, generated assets under `assets/`, referenced from the document) rather than vague direction.

A **personal** brand document (`kind: personal`) is built from the owner's Core Identity. A **business** brand document (`kind: business`) uses the organizational instrument set defined in the whitepaper (Aaker's brand personality dimensions, a Jungian brand archetype, and the Golden Circle with mission/vision/values) in place of the personal psychology, and keeps the same Context and Visuals structure.

### 5.4 Orbits (`orbits/<slug>.md`)

Orbits are owner-defined. The framework suggests a starting taxonomy; rename, merge, split, and invent freely.

**Personal (suggested):** Health & Wellness · Relationships · Finances · Career · Notes & Ideas · Time Management · Skills · Tech Stack · Goals

**Business (suggested):** Relationships (CRM) · Finances · Operations · Skills (Playbooks/SOPs) · Management · Brand Templates · Goals · Notes & Ideas · Tech Stack

This is a life-domain / operating-system taxonomy: closer to Johnny Decimal or PARA's "Areas" than to Zettelkasten's emergent linking, chosen deliberately because agents need stable, addressable, individually-permissionable domains. A vibegraph does not replace a personal knowledge management practice; it sits in front of it as the permissioned, machine-facing layer.

In an exported vibegraph, an orbit document is a **pointer**: front matter naming the orbit and its `target_tool`, and a body describing what the orbit covers and where its content lives (an Obsidian vault, a Notion workspace, a folder of files). Implementations that *serve* orbit content live (hosted vaults, MCP servers) MUST apply the permission model in [§6](#6-security--the-permission-model) to every item they serve.

---

## 6. Security & the permission model

A complete vibegraph is a concentrated dossier. The format is built to be **local-first and private by default**, and the v2.0 tree encodes the first permission decision structurally: the export contains the shareable parts (Core Identity and Branding) and only *pointers* to the orbits. Private content does not travel by default, so it cannot leak from a file it was never in.

### 6.1 Visibility levels

For implementations that hold or serve orbit content (hand-built vibegraphs that inline it, hosted services, MCP servers), every item is one of:

| Level | Meaning |
|---|---|
| `private` | Never exposed to any external tool or agent. The default for all orbit content. |
| `scoped` | Exposed only to the agents/tools named in that item's `scope` list, for stated purposes. |
| `public` | Freely shareable. Appropriate for most Core Identity and Branding content. |

Rules:

- **Deny by default.** Anything without an explicit setting is `private` if it is orbit content, shareable-by-construction if it is part of the exported core tree.
- **`scoped` requires a `scope`.** A `scoped` item with an empty `scope` is treated as `private`.

### 6.2 Guidance for consuming tools

Implementations that serve a vibegraph to agents (for example, over MCP: see [§7](#7-how-ai-systems-consume-a-vibegraph)) **SHOULD**:

- Grant access **per-agent and per-orbit**, never as a blanket over the whole vibegraph.
- **Never expose the full graph as a single surface.** An agent requests the sections it needs; it does not receive everything.
- **Log every read**, so the owner can always answer "what has this tool actually seen?"
- Treat `private` as inviolable and `scoped` as an allow-list, not a hint.

The rationale is the current reality of prompt-injection: a compromised or manipulated agent cannot leak what it was never granted. Tight scoping is the mitigation. An agent that was never given the `finances` orbit cannot exfiltrate it, however thoroughly it is compromised.

### 6.3 Hosting postures

- **Local (reference posture).** Files on hardware the owner controls. Only deliberately-exposed items ever leave the machine. The owner is responsible for device security.
- **Hosted.** A managed service SHOULD move toward zero-knowledge, client-side encryption (keys derived on-device, never transmitted; provider stores ciphertext it cannot read). This is out of scope for the *format* but is the recommended destination for any service built on it; a service that has not reached it SHOULD state plainly what it can and cannot read.

Blockchain storage and zero-knowledge *proofs* are explicitly **not** part of v2. Verifiable Credentials / selective disclosure are a plausible future extension and are noted on the roadmap, not required here.

---

## 7. How AI systems consume a vibegraph

Four consumption modes, in increasing order of sophistication. Only the first is required to get value; the rest are amplifiers.

1. **Direct context.** Paste or attach the export: the master file plus the Core Identity and brand documents. Works today, everywhere. The canonical mode.
2. **Persistent workspace context.** Load the same files into a persistent surface (a Claude Project, a custom GPT's instructions/knowledge, or an equivalent) so every conversation there starts calibrated.
3. **Live access over MCP.** Serve the vibegraph through a [Model Context Protocol](https://modelcontextprotocol.io) server so an agent can request exactly the section or orbit it needs at runtime, subject to the permission model in [§6](#6-security--the-permission-model). This is where per-item scoping does its real work.
4. **Seeding memory layers.** Load a vibegraph as seed context into an AI memory system to solve its cold-start problem with a verified, owner-authored foundation. The memory layer is the substrate; the vibegraph is the schema.

For a consumer, the minimal correct behavior is: **read the master file first**, follow its read order, respect the visibility of everything, and load only what the task needs.

> **For toolmakers:** a vibegraph is structured Markdown. If your product accepts text, it already supports vibegraphs. Deeper support (a "load vibegraph" import that parses the master file and honors visibility, or an MCP client that requests documents by `section`) is welcome and straightforward.

---

## 8. Licensing

This project uses a deliberate dual license so the convention can spread freely while implementations stay honest:

- **Templates, schema files, and any code** → **MIT** ([`LICENSE`](LICENSE)). Copy them, ship them, build products on them.
- **Specification prose and documentation** (this file, the README narrative, the whitepaper text) → **CC-BY 4.0** ([`LICENSE-docs`](LICENSE-docs)). Quote it and adapt it; keep attribution.

The goal is adoption. An identity standard that isn't open isn't a standard. Spreading `vibegraph.md` as a convention is the point, so the low-friction license choices are intentional.

**Trademarks are separate from copyright.** *Vibegraph™* and *Vibeclone™* are trademarks of Raizen Labs, LLC. The open licenses above cover the specification and templates; they do not grant rights to the trademarks. You can build, fork, and ship freely; please don't use the marks in ways that imply official endorsement or that would confuse users about the source of a product.

---

## 9. Versioning

The specification follows [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH`.

- **MAJOR**: breaking changes to required structure or field meaning.
- **MINOR**: backward-compatible additions (new optional fields, new suggested orbits).
- **PATCH**: clarifications and corrections with no schema impact.

Version 2.0.0 is a MAJOR release: it replaces v1.0's nested `core/` + `modules/` tree with the flat, owner-named tree in [§2](#2-file-tree-and-naming), renames the third part from Knowledge Base to Orbits, splits the brand layer's naming into Brand Context and Brand Visuals, and makes the personality layer a two-part assessment. Consumers MAY continue to accept v1.0 vibegraphs per the compatibility note in §2.

A vibegraph declares the version it targets via `vibegraph_version` in its master file. Consumers SHOULD accept any vibegraph whose MAJOR matches a version they support. Changes are recorded in [`CHANGELOG.md`](CHANGELOG.md).

---

<div align="center">

Part of **[The Vibegraph](https://vibegraph.md)**. Build the guided way at **[vibegraph.ai](https://vibegraph.ai)**.

</div>
