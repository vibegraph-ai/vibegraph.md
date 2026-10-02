# The vibegraph.md site (GitHub Pages)

This folder is the [vibegraph.md](https://vibegraph.md) site.

- `index.html`: the single-page site.
- `CNAME`: points the `vibegraph.md` custom domain at GitHub Pages.
- `whitepaper/vibegraph-whitepaper.pdf`: the published whitepaper, linked from the site and the README.
- `whitepaper/index.html`: redirects the folder URL to the PDF.

## Pages settings

Repository settings, Pages: Source = Deploy from a branch, Branch = `main`, Folder = `/docs`. The custom domain is `vibegraph.md` (declared in `CNAME`), with Enforce HTTPS on.


## Website analytics

`docs/assets/analytics.js` loads the official PostHog browser snippet for Raizen Labs project 580968 (US Cloud). Its project token is public by design. Personal API keys must never appear in this file. Tracking only starts on HTTPS `vibegraph.md` and `www.vibegraph.md`. Localhost, GitHub Pages preview hosts and Vercel preview hosts remain inert.

The shared page head loads this script. PostHog captures pageviews, page exits, referrers, campaign parameters, device information and web vitals according to the existing project settings. `outbound_link_clicked` and `file_download_clicked` record destination host/path without destination query strings, fragments, link text or form values. PDF downloads are clicks, not proof that someone read the file. Direct PDF requests do not run JavaScript. Session replay, console recording and broad interaction autocapture stay disabled.

The three sites use the same project. Filter `$host` in Web Analytics to separate them. Anonymous visitors on unrelated root domains are not automatically identified as the same person. No signup or purchase conversion is inferred from a link click.

Run `node --test scripts/analytics.test.mjs` to check production-host gating, duplicate initialization and link event behavior. After release, visit the live site and confirm its `$pageview` and link events in PostHog before calling production tracking verified.
