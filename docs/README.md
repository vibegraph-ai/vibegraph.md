# The vibegraph.md site (GitHub Pages)

This folder is the [vibegraph.md](https://vibegraph.md) site.

- `index.html`: the single-page site.
- `CNAME`: points the `vibegraph.md` custom domain at GitHub Pages.
- `whitepaper/vibegraph-whitepaper.pdf`: the published whitepaper, linked from the site and the README.
- `whitepaper/index.html`: redirects the folder URL to the PDF.

## Pages settings

Repository settings, Pages: Source = Deploy from a branch, Branch = `v2.0`, Folder = `/docs`. The custom domain is `vibegraph.md` (declared in `CNAME`), with Enforce HTTPS on.

The website references specification 3.0 on the `v3.0` branch. Its published PDF is copied from `v3.0` (`486655e`), alongside the website copy, while preserving the live site assets. The repository root on `v2.0` remains the version 2.0 source.


## Website analytics

`docs/assets/analytics.js` loads the official PostHog browser snippet for Raizen Labs project 580968 (US Cloud). Its project token is public by design. Personal API keys must never appear in this file. Tracking only starts on HTTPS `vibegraph.md` and `www.vibegraph.md`. Localhost, GitHub Pages preview hosts and Vercel preview hosts remain inert.

The shared page head loads this script. PostHog captures pageviews, page exits, referrers, campaign parameters, device information and web vitals according to the existing project settings. `outbound_link_clicked` and `file_download_clicked` record destination host/path without destination query strings, fragments, link text or form values. PDF downloads are clicks, not proof that someone read the file. Direct PDF requests do not run JavaScript. Session replay, console recording and broad interaction autocapture stay disabled.

The three sites use the same project. Filter `$host` in Web Analytics to separate them. Anonymous visitors on unrelated root domains are not automatically identified as the same person. No signup or purchase conversion is inferred from a link click.

Run `node --test scripts/analytics.test.mjs` to check production-host gating, duplicate initialization and link event behavior. After release, visit the live site and confirm its `$pageview` and link events in PostHog before calling production tracking verified.

## Search discovery

`robots.txt` allows crawling and advertises `https://vibegraph.md/sitemap.xml`. The sitemap lists the homepage and published whitepaper PDF. Keep the redirecting, noindex `/whitepaper/` landing page out of the sitemap. Update the sitemap when adding or removing public canonical pages. Google Search Console uses a DNS-verified domain property, so no browser tracking script is needed.

## Newsletter

The Context Layer section sits immediately below the hero in `index.html` and uses the framework site's monochrome tokens. Copy and status messages are in its markup. `assets/newsletter.js` handles validation, pending, retry and confirmation states. Only HTTPS vibegraph.md and www.vibegraph.md send requests; local and review hosts remain inert. The server-only Beehiiv integration runs at `https://vibegraph.ai/api/subscribe/`, with exact origin restrictions and source attribution. Deploy that service's allowlist update before releasing this page. No API keys belong in this repository.

Run `node --test tests/newsletter.cjs`, `node tests/site-behavior.cjs` and `node --test scripts/analytics.test.mjs` from the repository root. Inspect the newsletter in desktop/mobile and light/dark themes. A successful request means Beehiiv received it; subscribers may still need to confirm their email.
