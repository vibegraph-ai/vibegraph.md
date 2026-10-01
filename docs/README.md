# The vibegraph.md site (GitHub Pages)

This folder is the [vibegraph.md](https://vibegraph.md) site.

- `index.html`: the single-page site.
- `CNAME`: points the `vibegraph.md` custom domain at GitHub Pages.
- `whitepaper/vibegraph-whitepaper.pdf`: the published whitepaper, linked from the site and the README.
- `whitepaper/index.html`: redirects the folder URL to the PDF.

## Pages settings

Repository settings, Pages: Source = Deploy from a branch, Branch = `v2.0`, Folder = `/docs`. The custom domain is `vibegraph.md` (declared in `CNAME`), with Enforce HTTPS on.

The website references specification 3.0 on the `v3.0` branch. Its published PDF is copied from `v3.0` (`486655e`), alongside the website copy, while preserving the live site assets. The repository root on `v2.0` remains the version 2.0 source.
