# Landing page (GitHub Pages)

This folder holds the [vibegraph.md](https://vibegraph.md) landing page.

- `index.html` — the single-page site (agents.md-style).
- `CNAME` — points the `vibegraph.md` custom domain at GitHub Pages.
- `whitepaper/` — the published whitepaper PDF, linked from the site and README.

## Enabling Pages
In the repo settings → Pages: set **Source = Deploy from a branch**,
**Branch = `main`**, **Folder = `/docs`**. Then add `vibegraph.md` as the custom
domain (the `CNAME` file already declares it) and point the domain's DNS at GitHub
Pages per GitHub's docs.
