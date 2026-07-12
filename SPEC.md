# The Vibegraph Specification

**Version 1.0** · July 2026 · [vibegraph.md](https://vibegraph.md)

This document defines the vibegraph format: its file layout, the manifest, the per-document schema, the permission model, and the conventions by which AI systems consume a vibegraph. It is written to be read by humans building a vibegraph by hand, and by developers building tools that produce or consume one.

The specification prose is licensed CC-BY 4.0; the templates and schema files are MIT. See [Licensing](#8-licensing).

> **Terminology.** The key words used throughout — a *vibegraph*, its *Core Identity*, its *Knowledge Base*, and *modules* — are defined in the whitepaper and summarized in [§1](#1-overview). Where this document says an implementation **MUST**, **SHOULD**, or **MAY** do something, those words carry their ordinary specification meaning (roughly: required, recommended, optional).

---

## Table of contents

1. [Overview](#1-overview)
2. [File layout](#2-file-layout)
3. [The manifest: `VIBEGRAPH.md`](#3-the-manifest-vibegraphmd)
4. [Document schema](#4-document-schema)
5. [The Core Identity](#5-the-core-identity)
6. [Security & the permission model](#6-security--the-permission-model)
7. [How AI systems consume a vibegraph](#7-how-ai-systems-consume-a-vibegraph)
8. [Licensing](#8-licensing)
9. [Versioning](#9-versioning)

---

## 1. Overview

A **vibegraph** is a directory of Markdown files that codifies a person's or organization's identity and working context in a form AI systems can consume.

It has two parts:

- **Core Identity** (`core/`) — *who you are.* Personality, purpose, and brand. Small, stable, and safe to share with any AI tool. This is the part you paste into a chat.
- **Knowledge Base** (`modules/`) — *what you know and how you operate.* Self-defined modules containing the documents, data, and protocols of your life or business. This is where depth and sensitivity live, so every item is individually permissioned.

A vibegraph is **plain Markdown at its simplest** — a handful of files you can read, edit, and paste anywhere. Implementations MAY layer encryption, hosting, and access control on top (see [§6](#6-security--the-permission-model)), but a bare folder of Markdown is a valid, complete vibegraph.

There are two **types**: `personal` and `business`. They share the same structure and differ in which instruments populate the Core (see [§5](#5-the-core-identity)).

### Design goals

1. **Human-readable.** If you can read Markdown, you can read and edit a vibegraph. No tooling required.
2. **Useful with zero adoption.** Value arrives the moment the owner pastes it into an existing AI tool. No platform needs to support anything.
3. **Portable and owner-controlled.** A vibegraph is a file format, not a service. It moves across tools, models, and vendors unchanged.
4. **Private by default.** Nothing is exposed unless the owner marks it so.
5. **Extensible.** Start with the Core; add modules only when a real use case demands one.

---

## 2. File layout

A vibegraph is a directory. Its name SHOULD end in `.vibegraph` (for example, `avery-quinn.vibegraph`), which lets tools recognize it, but this is a convention, not a requirement.

```
name.vibegraph/
├── VIBEGRAPH.md              # REQUIRED — the manifest / entry point
├── core/                     # REQUIRED — Core Identity
│   ├── personality.md
│   ├── purpose.md
│   ├── brand-positioning.md
│   └── brand-aesthetics.md
└── modules/                  # OPTIONAL — Knowledge Base
    ├── goals.md
    ├── health.md
    └── <anything>.md         # owner-defined
```

Rules:

- **`VIBEGRAPH.md` MUST exist** at the root. It is the file an AI or tool reads first (see [§3](#3-the-manifest-vibegraphmd)).
- **`core/` MUST exist** and SHOULD contain the four Core documents for its type. A Core document MAY be a stub, but the files SHOULD be present so consumers know where to look.
- **`modules/` is OPTIONAL.** A Core-only vibegraph is valid and useful.
- A module MAY be a single `.md` file or a subdirectory containing an `index.md` plus supporting files:

  ```
  modules/
  ├── goals.md                 # simple module — one file
  └── finances/                # rich module — a folder
      ├── index.md             # the module's entry document
      ├── budget.md
      └── statements/…         # supporting files, data, etc.
  ```

- Filenames SHOULD be lowercase kebab-case. Module names are owner-defined; the taxonomy in [§5.3](#53-knowledge-base-modules) is a *suggested starting set*, not a fixed schema.

---

## 3. The manifest: `VIBEGRAPH.md`

`VIBEGRAPH.md` is the entry point. It carries the vibegraph's metadata in YAML front matter and a human- and machine-readable map of the vibegraph in its body. A consumer reads this file first to learn what the vibegraph contains and what it is allowed to see.

### 3.1 Front matter

```yaml
---
vibegraph_version: "1.0"        # REQUIRED — spec version this vibegraph targets
type: personal                  # REQUIRED — "personal" | "business"
owner: "Avery Quinn"            # REQUIRED — display name of the person/org
updated: "2026-07-11"           # REQUIRED — ISO 8601 date of last change
default_visibility: private     # REQUIRED — default for any item lacking its own setting
summary: >                      # OPTIONAL — one-paragraph orientation for a consumer
  Independent brand strategist and writer; warm-but-direct voice;
  helps solo founders sound like themselves in public.
---
```

| Field | Required | Values | Notes |
|---|---|---|---|
| `vibegraph_version` | Yes | string | The spec version. `"1.0"` for this document. |
| `type` | Yes | `personal` \| `business` | Selects the Core instrument set. |
| `owner` | Yes | string | Person or organization name. |
| `updated` | Yes | ISO 8601 date | Last modification of any part of the vibegraph. |
| `default_visibility` | Yes | `private` \| `scoped` \| `public` | Applied to any document that omits its own `visibility`. SHOULD be `private`. |
| `summary` | No | string | A short orientation a tool can surface without reading everything. |

### 3.2 Body

The body of `VIBEGRAPH.md` SHOULD contain, in plain prose and a simple list, a **map** of the vibegraph: what's in the Core, which modules exist, and their visibility. This doubles as the thing an AI reads to orient itself. See [`templates/personal/VIBEGRAPH.md`](templates/personal/VIBEGRAPH.md) for the canonical shape. A minimal body:

```markdown
# Avery Quinn — Vibegraph

> Independent brand strategist & writer. This is my codified identity
> and working context for use with AI tools.

## Core Identity  (visibility: public)
- `core/personality.md` — Big Five profile
- `core/purpose.md` — Ikigai / purpose & meaning
- `core/brand-positioning.md` — positioning, voice, messaging
- `core/brand-aesthetics.md` — visual identity

## Knowledge Base
- `modules/goals.md` — goals (visibility: scoped)
- `modules/finances/` — finances (visibility: private)

## Usage
Load the Core Identity into any AI tool to calibrate it to me.
Modules are private or scoped unless stated otherwise.
```

---

## 4. Document schema

Every document in a vibegraph — Core files and module files — is Markdown with OPTIONAL YAML front matter carrying its metadata and permissions.

```yaml
---
section: core/personality        # REQUIRED for tooling — logical path/id
visibility: public               # OPTIONAL — overrides manifest default
scope: []                        # OPTIONAL — required when visibility is "scoped"
updated: "2026-07-11"            # RECOMMENDED — ISO 8601
---
```

| Field | Applies when | Meaning |
|---|---|---|
| `section` | All documents | A stable logical identifier, usually mirroring the path (`core/purpose`, `modules/goals`). Lets tools reference a part without guessing at filenames. |
| `visibility` | Any document | `private` \| `scoped` \| `public`. Overrides the manifest's `default_visibility`. See [§6](#6-security--the-permission-model). |
| `scope` | `visibility: scoped` | A list of agent/tool identifiers permitted to read this document. Ignored otherwise. |
| `updated` | All documents | Date the document last changed. |

Front matter is OPTIONAL: a document without it inherits the manifest's `default_visibility` and is assumed public-within-the-Core if it lives under `core/`. Tooling SHOULD treat a missing `visibility` on a `modules/` document as the manifest default (normally `private`).

The **body** of each document is ordinary Markdown. Structure it for a reader — headings, short lists, plain statements. Write it the way you'd want an AI to read it back: declarative and specific. "I write in second person, short sentences, no hedging" beats "professional but approachable."

---

## 5. The Core Identity

The Core is the always-relevant half — the part a consumer loads in every interaction. It is deliberately small enough to fit inside a single model context window.

### 5.1 Personal Core

Four documents, built in order because each feeds the next:

| File | What it captures | Grounded in |
|---|---|---|
| `core/personality.md` | Big Five (OCEAN) scores, facet notes, and a plain-language interpretation | Five-Factor Model |
| `core/purpose.md` | Purpose, meaning, and direction | Ikigai 2.0 |
| `core/brand-positioning.md` | Positioning, UVP, values, tone & voice, messaging, bios, keywords | Personal brand strategy |
| `core/brand-aesthetics.md` | Palette (hex), typography, logo/symbol, imagery & photography direction | Visual identity practice |

### 5.2 Business Core

The business Core keeps the same four-slot shape and swaps the instruments, because a company can't take a personality test and ikigai doesn't describe a business:

| File | What it captures | Grounded in |
|---|---|---|
| `core/brand-personality.md` | Aaker's five dimensions + the chosen brand archetype | Aaker (1997); Jungian archetypes |
| `core/purpose.md` | Why / How / What; mission, vision, values | Golden Circle; EOS V/TO |
| `core/brand-positioning.md` | Positioning, UVP, messaging, tone & voice | Brand strategy |
| `core/brand-design.md` | Full design system + templates | Design systems |

The mapping between personal and business Cores:

| Personal | Business | Relationship |
|---|---|---|
| Big Five (OCEAN) | Aaker dimensions + archetype | Replaced — same job, different instrument |
| Ikigai 2.0 | Golden Circle + mission/vision/values | Replaced — same job, shared "Why" |
| Brand positioning | Brand positioning | Carries over |
| Brand aesthetics | Brand design system + templates | Carries over, deepens |

### 5.3 Knowledge Base modules

Modules are owner-defined. The framework suggests a starting taxonomy; rename, merge, split, and invent freely.

**Personal (suggested):** Health & Wellness · Relationships · Finances · Career · Notes & Ideas · Time Management · Skills · Tech Stack · Goals

**Business (suggested):** Relationships (CRM) · Finances · Operations · Skills (Playbooks/SOPs) · Management · Brand Templates · Goals · Notes & Ideas · Tech Stack

This is a **life-domain / operating-system taxonomy** — closer to Johnny Decimal or PARA's "Areas" than to Zettelkasten's emergent linking — chosen deliberately because agents need stable, addressable, individually-permissionable domains. A vibegraph does not replace a personal knowledge management practice; it sits in front of it as the permissioned, machine-facing layer and MAY link out to an Obsidian vault, a Notion workspace, or a folder of files.

---

## 6. Security & the permission model

A complete vibegraph is a concentrated dossier. The format is built to be **local-first and private by default**, and to give the owner per-item control over what any AI agent can see.

### 6.1 Visibility levels

Every item (the manifest default, or any document's `visibility`) is one of:

| Level | Meaning |
|---|---|
| `private` | Never exposed to any external tool or agent. The default. |
| `scoped` | Exposed only to the agents/tools named in that document's `scope` list, for stated purposes. |
| `public` | Freely shareable. Appropriate for most Core Identity content. |

Rules:

- **Deny by default.** Anything without an explicit setting inherits `default_visibility`, which SHOULD be `private`. Nothing is exposed by omission.
- **The Core is designed to be safe at `public`** for most owners; the Knowledge Base SHOULD default everything to `private`.
- **`scoped` requires a `scope`.** A `scoped` document with an empty `scope` is treated as `private`.

### 6.2 Guidance for consuming tools

Implementations that serve a vibegraph to agents (for example, over MCP — see [§7](#7-how-ai-systems-consume-a-vibegraph)) **SHOULD**:

- Grant access **per-agent and per-module**, never as a blanket over the whole vibegraph.
- **Never expose the full graph as a single surface.** An agent requests the sections it needs; it does not receive everything.
- **Log every read**, so the owner can always answer "what has this tool actually seen?"
- Treat `private` as inviolable and `scoped` as an allow-list, not a hint.

The rationale is the current reality of prompt-injection: a compromised or manipulated agent cannot leak what it was never granted. Tight scoping is the mitigation. An agent that was never given the `finances` module cannot exfiltrate it, however thoroughly it is compromised.

### 6.3 Hosting postures

- **Local (reference posture).** Files on hardware the owner controls. Only deliberately-exposed items ever leave the machine. The owner is responsible for device security.
- **Hosted.** A managed service SHOULD use zero-knowledge, client-side encryption (keys derived on-device, never transmitted; provider stores ciphertext it cannot read). This is out of scope for the *format* but is the recommended posture for any service built on it.

Blockchain storage and zero-knowledge *proofs* are explicitly **not** part of v1. Verifiable Credentials / selective disclosure are a plausible future extension and are noted on the roadmap, not required here.

---

## 7. How AI systems consume a vibegraph

Four consumption modes, in increasing order of sophistication. Only the first is required to get value; the rest are amplifiers.

1. **Direct context.** Paste `VIBEGRAPH.md` + the `core/` files into any AI chat, or attach them to a tool that accepts files. Works today, everywhere. The canonical mode.
2. **Persistent workspace context.** Load the Core into a persistent surface — a Claude Project, a custom GPT's instructions/knowledge, or an equivalent — so every conversation there starts calibrated. A vibegraph exports cleanly into these.
3. **Live access over MCP.** Serve the vibegraph through a [Model Context Protocol](https://modelcontextprotocol.io) server so an agent can request exactly the section it needs at runtime, subject to the permission model in [§6](#6-security--the-permission-model). This is where per-item scoping does its real work.
4. **Seeding memory layers.** Load a vibegraph as seed context into an AI memory system to solve its cold-start problem with a verified, owner-authored foundation. The memory layer is the substrate; the vibegraph is the schema.

For a consumer, the minimal correct behavior is: **read `VIBEGRAPH.md` first**, respect the visibility of everything, and load only what the task needs.

> **For toolmakers:** a vibegraph is structured Markdown. If your product accepts text, it already supports vibegraphs. Deeper support — a "load vibegraph" import that parses the manifest and honors `visibility`, or an MCP client that requests sections by `section` id — is welcome and straightforward.

---

## 8. Licensing

This project uses a deliberate dual license so the convention can spread freely while implementations stay honest:

- **Templates, schema files, and any code** → **MIT** ([`LICENSE`](LICENSE)). Copy them, ship them, build products on them.
- **Specification prose and documentation** (this file, the README narrative, the whitepaper text) → **CC-BY 4.0** ([`LICENSE-docs`](LICENSE-docs)). Quote it and adapt it; keep attribution.

The goal is adoption. An identity standard that isn't open isn't a standard. Spreading `vibegraph.md` as a convention is the point — so the low-friction license choices are intentional.

**Trademarks are separate from copyright.** *Vibegraph™* and *Vibeclone™* are trademarks of Raizen Labs, LLC. The open licenses above cover the specification and templates; they do not grant rights to the trademarks. You can build, fork, and ship freely; please don't use the marks in ways that imply official endorsement or that would confuse users about the source of a product.

---

## 9. Versioning

The specification follows [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH`.

- **MAJOR** — breaking changes to required structure or field meaning.
- **MINOR** — backward-compatible additions (new optional fields, new suggested modules).
- **PATCH** — clarifications and corrections with no schema impact.

A vibegraph declares the version it targets via `vibegraph_version` in its manifest. Consumers SHOULD accept any vibegraph whose MAJOR matches a version they support. Changes are recorded in [`CHANGELOG.md`](CHANGELOG.md).

---

<div align="center">

Part of **[The Vibegraph](https://vibegraph.md)**. Build the guided way at **[vibegraph.ai](https://vibegraph.ai)**.

</div>
