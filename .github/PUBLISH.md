# Publishing notes

How this repository is published, for maintainers.

## GitHub Pages

Repository settings, Pages: Source = Deploy from a branch, Branch = `main`, Folder = `/docs`. The `docs/CNAME` file declares the `vibegraph.md` custom domain. Enforce HTTPS stays on.

## Repository description and topics

- Description: vibegraph.md: the open framework and file convention for a vibegraph. Defines VIBEGRAPH.md, the root file.
- Topics: vibegraph, agents-md, context, mcp, identity

## Releasing a specification version

1. Work on a branch. Update `SPEC.md`, `CHANGELOG.md`, the example, the templates, and the schema together.
2. If the whitepaper changes, rebuild the figures (`python3 whitepaper/figures/build_figures.py`) and the PDF (`python3 whitepaper/pdf-source/build.py`), then copy the PDF to `docs/whitepaper/vibegraph-whitepaper.pdf`.
3. Check that the example passes the conformance checklist in `SPEC.md` §10.
4. Merge to `main` and tag the merge commit with the version (for example `v2.0`).
5. Confirm GitHub Pages serves the updated `docs/index.html` and the PDF.
6. Capture Wayback Machine snapshots of vibegraph.md, the README, SPEC.md, and the PDF.
7. In Search Console, submit the sitemap and request removal of any PDF URLs that no longer exist.
