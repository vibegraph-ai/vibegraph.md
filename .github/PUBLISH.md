# How to publish this repo

These are one-time setup steps to get `vibegraph.md` live on GitHub + GitHub Pages.

## 1. Create the org and repo
- Create the GitHub organization **`vibegraph-ai`** (if not already done).
- Create a new **public** repository under it named **`vibegraph.md`**.
  Final URL: `https://github.com/vibegraph-ai/vibegraph.md`
- Do NOT initialize it with a README (this repo already has one).

## 2. Push this repo
From inside this folder:

```bash
git init
git add .
git commit -m "Vibegraph specification v1.0"
git branch -M main
git remote add origin https://github.com/vibegraph-ai/vibegraph.md.git
git push -u origin main
```

## 3. Turn on GitHub Pages
Repo → **Settings → Pages**:
- **Source:** Deploy from a branch
- **Branch:** `main`  ·  **Folder:** `/docs`
- Save. The `docs/CNAME` file already declares the `vibegraph.md` custom domain.

## 4. Point the domain
At your DNS provider for **vibegraph.md**, add the records GitHub Pages specifies
(four `A` records to GitHub's IPs for the apex, or a `CNAME` to
`vibegraph-ai.github.io` for a subdomain). Then enable **Enforce HTTPS** in Pages
settings once the certificate provisions.

## 5. Day-one evidence (trademark)
The same day you publish, capture:
- `https://vibegraph.md` in the Wayback Machine (web.archive.org/save)
- the GitHub repo URL in the Wayback Machine
- keep the published whitepaper PDF with its date

These, plus your first real use in commerce, are your trademark evidence file.

## 6. Cross-link
- Confirm the site footer and README point to `github.com/vibegraph-ai/vibegraph.md`.
- When `vibegraph.ai` (the app) is live, confirm it links back here to the spec.
