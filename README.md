<div align="center">

# vibegraph.md

### Your vibes, codified.

The open framework and file convention for a vibegraph. It defines VIBEGRAPH.md, the root file every AI reads first.

[Specification](SPEC.md) · [Example](examples/maya-okafor.vibegraph) · [Templates](templates/your-name.vibegraph) · [Whitepaper (PDF)](whitepaper/vibegraph-whitepaper.pdf) · [vibegraph.ai](https://vibegraph.ai)

Published specification: 3.0 · MIT (templates, schema, code) · CC-BY 4.0 (prose)

</div>

---

## What is a vibegraph?

Your vibes (your personality, taste, voice, values, purpose, and aesthetic) are what AI gets wrong about you by default, because nobody wrote them down anywhere a machine could read them.

**A vibegraph is the network of identity, context, knowledge, and memory that governs how AI thinks, writes, and acts for one person, and any businesses they own or operate.**

Everyone who uses AI for real work already has one, spread across a notes app, a folder of documents, a few platform memories, and a great deal that lives only in their head. Two things turn that pile into a vibegraph: a human-authored identity core, and a root file with a fixed name that any agent reads first. Without them, it is context. With them, it is a graph any agent can walk, a permission model you can reason about, and an asset that moves unchanged when a better tool ships.

> Memory layers remember what happened. A vibegraph defines who you are.

## Three things, three roles

| | vibegraph (the noun) | vibegraph.md (the framework) | vibegraph.ai (the app) |
|---|---|---|---|
| What it is | A category term for the network that governs AI for one person and the businesses they own | The open specification and file convention: the root file, the typed link schema, scopes, areas, the handoff | A guided builder for the identity core and brands, which exports this layout |
| Who owns it | Nobody. A common noun | Maintained by Ryan Charleston under MIT and CC-BY 4.0 | Raizen Labs, LLC |
| Analogy | the web | HTML and index.html | a website builder |

You do not need vibegraph.ai to have a vibegraph. Copy the example, replace the owner, and fill it in by hand.

## The layout

```
your-name.vibegraph/
├── VIBEGRAPH.md               root file. Fixed name. Read first.
├── AGENTS.md                  the handoff stanza
├── CLAUDE.md                  the same stanza, for Claude Code
├── identity/your-name.md      the identity core: rules, personality, purpose
├── brands/
│   ├── your-name.brand.md     personal brand: up to 12 Brand Context + 8 Brand Visuals
│   ├── your-business.brand.md business brand: foundations + 12 + 8
│   └── assets/README.md       where the visual assets live
├── context-sources.md         the systems that already hold parts of the graph
└── areas/<area>/index.md      one folder per chosen area, each with its entries
```

The full rules are in [SPEC.md §2](SPEC.md#2-the-reference-layout).

## The root file

Every link in VIBEGRAPH.md carries a kind, a scope, and a rule for when to read it:

```markdown
- [Maya Okafor](identity/maya-okafor.md) · kind: identity · scope: public · when: always
- [Delivery OS](brands/delivery-os.brand.md) · kind: brand · type: business · scope: public · when: on-task (any Delivery OS writing, design, or publishing)
- [Finances](areas/finances/index.md) · kind: area · scope: private · when: on-grant
```

- **kind:** identity · brand · area · source · memory · project · skill · agent
- **scope:** public · scoped · private
- **when:** always · on-task · on-grant

Nothing is exposed by omission. See [SPEC.md §3 and §4](SPEC.md#3-the-root-file-vibegraphmd).

## The handoff

Put this in AGENTS.md, and the same text in CLAUDE.md, in any repository or workspace you work in:

```markdown
## Who you emulate
Before starting, read `VIBEGRAPH.md` (in this repo, or at `~/vibegraph/VIBEGRAPH.md`).
It defines the person and brands this work belongs to. Follow its read order and scopes.
Do not read entries marked `scope: private` unless they have been granted for this session.
```

Codex, Cursor, Copilot, and Gemini CLI read AGENTS.md. Claude Code reads CLAUDE.md. Both files, same four lines.

## The paste test

Open a fresh session in any model. Paste VIBEGRAPH.md, your identity file, and one brand file. Ask for a piece of work you do often. The output should sound like you on the first generation. If it does not, the core is incomplete, not the tool.

## Start

1. **Read the specification.** [SPEC.md](SPEC.md): the layout, the root file, the link schema, scopes, the handoff, serving, and the conformance checklist.
2. **Start from the example.** [`examples/maya-okafor.vibegraph/`](examples/maya-okafor.vibegraph) is a complete vibegraph for a fictional owner with a personal brand and a business brand. Or start blank from [`templates/your-name.vibegraph/`](templates/your-name.vibegraph).
3. **Pass the paste test.** Then add the handoff to your repositories.
4. **Serve it live if you want.** Over MCP, scopes become grants and every read is logged. See [SPEC.md §7](SPEC.md#7-scopes-grants-and-serving).

Want a guided build with an AI coach instead? That is what [vibegraph.ai](https://vibegraph.ai) is for.

## In this repository

| Path | What it is |
|---|---|
| [SPEC.md](SPEC.md) | The specification, version 3.0 |
| [examples/](examples) | The Maya Okafor worked example |
| [templates/](templates) | A blank vibegraph in the reference layout |
| [schema/](schema) | JSON Schemas for the front matter |
| [whitepaper/](whitepaper) | The whitepaper: markdown source, PDF, figures |
| [docs/](docs) | The vibegraph.md site (GitHub Pages) |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose changes |

## A note on privacy

A complete vibegraph is sensitive by nature. There is no global vibegraph: each one represents one person and is private by default. The reference posture is files on hardware you control, areas stay home when the core travels, and anything without a scope is private. Read [SPEC.md §7](SPEC.md#7-scopes-grants-and-serving) before you serve a vibegraph to any agent. Never commit your own vibegraph to a public repository; this repository's `.gitignore` excludes `*.vibegraph/` folders outside `examples/` and `templates/`.

## License

- **Templates, schema, and code:** [MIT](LICENSE)
- **Specification prose and documentation:** [CC-BY 4.0](LICENSE-docs)

Use it, fork it, serve it, and build products that produce or consume it. Spreading the convention is the point.

---

<div align="center">

Maintained by [Ryan Charleston](https://github.com/ryancharleston) · Raizen Labs, LLC · "vibegraph" is a common noun.

</div>
