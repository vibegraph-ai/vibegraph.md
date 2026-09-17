# Contributing to the vibegraph.md specification

Thanks for your interest in improving vibegraph.md. It is an open convention: the more people build on it, the more useful it becomes.

## Ways to contribute

- **Use it and report friction.** Tell us where the spec is unclear, where a template is confusing, or where a consuming tool did not behave as expected. Open an issue.
- **Improve the templates and the example.** If a template could prompt a better answer, propose an edit.
- **Add integrations.** Built something that produces, serves, or consumes vibegraphs: an exporter, an MCP server, an import? Open an issue to have it listed.
- **Sharpen the spec.** Clarifications, corrections, and well-argued additions to `SPEC.md` are welcome.

## How to propose a change

1. **Open an issue first** for anything beyond a typo, so we can agree on direction before you invest time.
2. **Fork, branch, and open a pull request** against `main`. One concern per pull request.
3. **Explain the why.** A change to a shared convention affects everyone who builds on it; the motivation matters as much as the diff.

## What we optimize for

- **Human readability.** If a change makes a vibegraph harder to read and edit by hand, it is probably the wrong change.
- **Zero-adoption value.** Nothing in the spec should require a specific platform to be useful.
- **Privacy by default.** Changes must not weaken deny by default or the scope model.
- **One person per vibegraph.** Changes must not pool graphs across people.

## Versioning

Changes are recorded in [`CHANGELOG.md`](CHANGELOG.md) and versioned `MAJOR.MINOR`:

- **Clarifications and corrections** change the text in place with a changelog note.
- **MINOR:** new optional fields, suggested areas, or source placements.
- **MAJOR:** anything that breaks an existing valid vibegraph.

## Style

Write "vibegraph" in lowercase, always, and write vibegraph.md and vibegraph.ai in lowercase with the extension. VIBEGRAPH.md, the root file, is capitalized. No em dashes or en dashes; use commas, colons, parentheses, or a vertical bar.

## Licensing of contributions

By contributing, you agree that your contributions are licensed under the same terms as the repository: MIT for templates, schema, and code; CC-BY 4.0 for specification prose and documentation. You keep copyright to your contributions and grant Raizen Labs, LLC and downstream users the rights those licenses describe.

## Code of conduct

Be decent. Assume good faith, critique ideas rather than people, and keep discussion focused on making the convention better. Maintainers may remove comments or contributions that are abusive, off-topic, or in bad faith.

---

Questions that are not a bug or a proposal? Write to **hello@vibegraph.ai**.
