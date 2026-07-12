# Contributing to the Vibegraph specification

Thanks for your interest in improving the vibegraph. This is an open convention — the more people build on it, the more useful it becomes.

## Ways to contribute

- **Use it and report friction.** The most valuable contribution early on is telling us where the spec is unclear, where a template field is confusing, or where a consuming tool didn't behave as expected. Open an issue.
- **Improve the templates.** If a Core document or module template could prompt a better answer, propose an edit.
- **Add integrations.** Built something that produces or consumes vibegraphs — an exporter, an MCP server, a "load vibegraph" import? Open an issue to have it listed.
- **Sharpen the spec.** Clarifications, corrections, and well-argued additions to `SPEC.md` are welcome.

## How to propose a change

1. **Open an issue first** for anything beyond a typo, so we can discuss direction before you invest time.
2. **Fork, branch, and open a pull request** against `main`. Keep PRs focused — one concern per PR.
3. **Explain the "why."** A change to a shared convention affects everyone who builds on it; motivation matters as much as the diff.

## What we optimize for

- **Human readability.** If a change makes a vibegraph harder for a person to read and edit by hand, it's probably the wrong change.
- **Zero-adoption value.** Nothing in the spec should require a specific platform to be useful.
- **Privacy by default.** Changes must not weaken the deny-by-default permission model.
- **Backward compatibility.** Follow [semver](https://semver.org). Breaking changes need a strong justification and a MAJOR version bump.

## Scope changes to the spec version

Proposed changes are versioned per [`CHANGELOG.md`](CHANGELOG.md):

- **PATCH** — clarifications, typo fixes, wording.
- **MINOR** — new optional fields, new suggested modules, additive guidance.
- **MAJOR** — anything that breaks an existing valid vibegraph.

## Licensing of contributions

By contributing, you agree that your contributions are licensed under the same terms as the repository: **MIT** for templates, schema, and code; **CC-BY 4.0** for specification prose and documentation. You retain copyright to your contributions; you grant Raizen Labs, LLC and downstream users the rights described by those licenses.

## Trademarks

*Vibegraph™* and *Vibeclone™* are trademarks of Raizen Labs, LLC. Contributing to this repository does not grant trademark rights. Please don't use the marks in a way that implies official endorsement of a third-party product. See [`SPEC.md` §8](SPEC.md#8-licensing).

## Code of conduct

Be decent. Assume good faith, critique ideas rather than people, and keep discussion focused on making the convention better. Maintainers may remove comments or contributions that are abusive, off-topic, or in bad faith.

---

Questions that aren't a bug or proposal? Reach out at **hello@vibegraph.ai**.
