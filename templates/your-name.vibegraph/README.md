# Your vibegraph (template)

A blank vibegraph in the [vibegraph.md reference layout](../../SPEC.md#2-the-reference-layout). For a finished one, see [`examples/maya-okafor.vibegraph/`](../../examples/maya-okafor.vibegraph).

## Fill it in

1. Copy this folder somewhere private (conventionally `~/vibegraph/`) and rename it `<your-name>.vibegraph`. Never commit your own vibegraph to a public repository.
2. Choose your slug: your name in lowercase with hyphens (`Maya Okafor` becomes `maya-okafor`). Rename `identity/your-name.md` and `brands/your-name.brand.md`, and update the paths in `VIBEGRAPH.md`.
3. Fill in the identity file first. A rough core beats an empty one. Delete the guidance quote blocks as you go.
4. Fill in the personal brand.
5. If you own a business, rename `brands/your-business.brand.md` to your business's slug and fill it in. If not, delete the file and its line in `VIBEGRAPH.md`.
6. Register the tools that already hold parts of your graph in `context-sources.md`, with one summary line each under `## Context Sources` in `VIBEGRAPH.md`.
7. Put `AGENTS.md` and `CLAUDE.md` (the four-line handoff) in the repositories you work in.

## The paste test

Open a fresh session in any model. Paste `VIBEGRAPH.md`, your identity file, and your personal brand file. Ask for a piece of work you do often. The output should sound like you on the first generation. If it does not, the core is incomplete, not the tool.

## Add an area

See [areas/README.md](areas/README.md).
