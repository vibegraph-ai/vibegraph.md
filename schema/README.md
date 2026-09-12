# Schema

JSON Schemas (Draft 2020-12) for the front matter of vibegraph files.

- **`vibegraph-root.schema.json`** validates the front matter of `VIBEGRAPH.md`, the root file (SPEC.md §3.1).
- **`vibegraph-node.schema.json`** validates the optional front matter of an identity file, a brand file, or an area index (SPEC.md §5).

They cover front matter only. The markdown bodies and the root file's link lines are defined in [SPEC.md](../SPEC.md), and §10 there is the conformance checklist. A hand-built vibegraph needs no validation to work; the schemas are a convenience for tool authors.

Licensed MIT, like the templates and code.
