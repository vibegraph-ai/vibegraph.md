<div align="center">

# The Vibegraph™

### Your Vibes, Codified.

An open framework for codifying human identity and personal brand as structured, portable AI context: digital DNA any AI can read today, and the protocol for an agent that operates as its creator's clone, a Vibeclone.

[vibegraph.md](https://vibegraph.md) · [vibegraph.ai](https://vibegraph.ai) · [Read the whitepaper](whitepaper/The-Vibegraph-Whitepaper-v1.5.pdf)

</div>

---

## What is this?

Every AI tool you use starts from zero. It doesn't know your voice, your values, your goals, or your taste: so it guesses, toward the statistical average. The result is output that could belong to anyone.

A **vibegraph** is a small set of markdown files that fixes the *input* instead of endlessly editing the output. It codifies who you are (your personality, purpose, and brand) in a format any AI tool, agent, or memory layer can read.

Think of it as `AGENTS.md`, but for a person instead of a codebase.

```
jordan-lee-vibegraph.zip
├── jordan-lee.vibegraph.md    # the master file an AI reads first
├── jordan-lee.personality.md  # Core Identity: who you are
├── jordan-lee.ikigai.md       # Core Identity: why
├── jordan-lee.brand.md        # Branding: the personal brand
├── acme-studio.brand.md       # Branding: a business brand (optional)
└── orbits/                    # Orbits: what you know & how you operate
    ├── goals.md
    └── ...
```

## Why it works on day one

You don't need a single platform to adopt anything. Paste your Core Identity into Claude, ChatGPT, Grok, or Gemini and the very next response sounds like *you*. That's the whole thing. Everything else (MCP servers, memory-layer seeding, the guided app) is an amplifier, not a dependency.

## 60-second quickstart

1. **Copy the template.** Grab [`templates/vibegraph/`](templates/vibegraph) and rename the `your-name.*` files to your own name. Your business brands live inside it as `<business>.brand.md` files beside your personal one.
2. **Fill in the Core.** Start with `your-name.personality.md`. Work down. Don't overthink it: a rough Core beats an empty one.
3. **Use it.** Paste the master file plus the personality, ikigai, and brand documents into any AI chat, or attach them to a Claude Project or custom GPT. Ask it to write something in your voice.
4. **Grow it later.** Add `orbits/` for the life or business domains you actually want an agent to know about. Not before.

Want a guided, AI-assisted build with a personality assessment and brand tooling instead of doing it by hand? That's what [**vibegraph.ai**](https://vibegraph.ai) is for.

## See a finished one

A complete reference vibegraph is on the way: see [`examples/`](examples). For now, the [templates](templates) and [SPEC.md](SPEC.md) show the full shape of every section.

## The three parts

| | **Core Identity** | **Branding** | **Orbits** |
|---|---|---|---|
| Answers | *Who is this person?* | *How do they show up?* | *What do they know / how do they operate?* |
| Contents | Personality, ikigai | Personal brand + business brands | Self-defined domains (health, finances, goals, SOPs…) |
| Size | Small, stable | One document per brand | Grows over time |
| Default sharing | Safe to share with any AI | Safe to share with any AI | Gated & permissioned; pointers only in exports |

Personal and business vibegraphs share this structure; the business version swaps the instruments (brand archetype + Aaker dimensions instead of a personality test, Golden Circle instead of Ikigai). See [`SPEC.md`](SPEC.md).

## Read more

- **[SPEC.md](SPEC.md)**: the full specification: file tree, the master file, per-document schema, the permission model, and how AI systems consume a vibegraph.
- **[The whitepaper](whitepaper/The-Vibegraph-Whitepaper-v1.5.pdf)**: the concept, the architecture, security, and use cases (v1.5; [markdown source](whitepaper/The-Vibegraph-Whitepaper-v1.5.md), v1.0 PDF in the same folder).
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: how to propose changes to the spec.
- **[CHANGELOG.md](CHANGELOG.md)**: version history.

## A note on privacy

A complete vibegraph is sensitive by nature. The framework is **local-first and private by default**: your files live on hardware you control, orbit content stays in your own tools, and served content carries `visibility` settings (`private` / `scoped` / `public`). Nothing is shared by omission. Read the security model in [SPEC.md §6](SPEC.md#6-security--the-permission-model) before you serve a vibegraph to any agent.

## License

- **Templates, schema, and code** → [MIT](LICENSE)
- **Specification prose and documentation** → [CC-BY 4.0](LICENSE-docs)

Use it, fork it, build products that consume it. Spreading the convention is the point. See [SPEC.md](SPEC.md) for the licensing rationale.

---

<div align="center">

**Vibegraph™** and **Vibeclone™** are trademarks of Raizen Labs, LLC. Created by [Ryan Charleston](https://ryancharleston.com).

The name is a standard; the code is open. Build with it.

</div>
