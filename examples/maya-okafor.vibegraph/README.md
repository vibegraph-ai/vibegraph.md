# Maya Okafor's vibegraph (worked example)

A complete vibegraph in the [vibegraph.md reference layout](../../SPEC.md#2-the-reference-layout). Maya Okafor is fictional: a solo operations consultant who runs a business brand, Delivery OS. Every name, number, and link here is invented for the example.

A vibegraph is the network of identity, context, knowledge, and memory that governs how AI thinks, writes, and acts for one person, and any businesses they own or operate. This folder holds the center of Maya's: her identity core, her personal brand, her business brand, four areas, and a registry of the tools that already hold the rest.

## What is here

| File | What it is |
|---|---|
| [VIBEGRAPH.md](VIBEGRAPH.md) | The root file. Any agent reads it first. |
| [identity/maya-okafor.md](identity/maya-okafor.md) | The identity core: rules, personality, purpose. |
| [brands/maya-okafor.brand.md](brands/maya-okafor.brand.md) | The personal brand: 12 Brand Context and 8 Brand Visuals elements. |
| [brands/delivery-os.brand.md](brands/delivery-os.brand.md) | The business brand: foundations, then the same 12 and 8. |
| [brands/assets/README.md](brands/assets/README.md) | Where every visual asset lives. |
| [areas/](areas/README.md) | Career, skills, goals, and finances, each with its own scope. |
| [components.md](components.md) | The tools that hold parts of the graph. |
| [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md) | The four-line handoff that sends agents to VIBEGRAPH.md. |

## The paste test

Open a fresh session in any model. Paste `VIBEGRAPH.md`, `identity/maya-okafor.md`, and `brands/maya-okafor.brand.md`. Ask for something Maya writes every week, for example: "Draft this Tuesday's newsletter intro about why a kickoff checklist beats a kickoff call." The draft should sound like Maya on the first try: calm, specific, dry, no exclamation points. If it does not, the core is incomplete, not the tool.

## Make it yours

1. Copy this folder and rename it `<your-name>.vibegraph`.
2. Rename `identity/maya-okafor.md` and `brands/maya-okafor.brand.md` to your own slug, and update the links in `VIBEGRAPH.md`.
3. Replace Maya's content with yours, starting with the identity file. A rough core beats an empty one.
4. Delete `brands/delivery-os.brand.md` and its line in `VIBEGRAPH.md` if you have no business, or rewrite it for yours.
5. Run the paste test.

The blank starting point is in [`templates/your-name.vibegraph/`](../../templates/your-name.vibegraph).

## Add an area

Create `areas/<area-slug>/index.md` with front matter (`kind: area`, `area`, `scope`, `when`), describe what belongs there, and add one line under `## Areas` in `VIBEGRAPH.md`. Areas are scoped or private by default. See [areas/README.md](areas/README.md).
