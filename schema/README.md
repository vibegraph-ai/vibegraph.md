# Schema

Machine-readable JSON Schemas (Draft 2020-12) for validating vibegraph files.

- **`vibegraph-manifest.schema.json`** — validates the YAML front matter of a
  `VIBEGRAPH.md` manifest.
- **`vibegraph-document.schema.json`** — validates the optional front matter of any
  Core or module document.

These describe the **front matter only** — the Markdown body of each file is free-form
by design. The schemas are a convenience for tool authors; a vibegraph is valid if it
follows [SPEC.md](../SPEC.md), and hand-authored vibegraphs need no validation to work.

Licensed MIT, like the rest of the schema and templates.
