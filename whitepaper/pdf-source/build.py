#!/usr/bin/env python3
"""Build vibegraph-whitepaper.pdf from the markdown source.

Reads ../vibegraph-whitepaper.md, renders it as two print-styled HTML
documents (cover.html without a footer, body.html with the running footer
and page numbers starting at 1 on the Introduction), prints both with
puppeteer-core driving the installed Chrome (render.js), and merges them
with pypdf.

  python3 ../figures/build_figures.py   # when a figure spec changes
  python3 build.py

Requires: the `markdown` and `pypdf` packages, `npm install` in this
directory (puppeteer-core), Google Chrome, and Inter installed. Space
Grotesk and IBM Plex Mono load from Google Fonts at render time; without a
network the pages fall back to Inter and Menlo.
"""
import re
import subprocess
from pathlib import Path

import markdown
from pypdf import PdfWriter

HERE = Path(__file__).parent
WHITEPAPER = HERE.parent
MD = WHITEPAPER / "vibegraph-whitepaper.md"
PDF_OUT = WHITEPAPER / "vibegraph-whitepaper.pdf"
NODE = "/opt/homebrew/opt/node@22/bin/node"

FONTS = (
    "<link rel='stylesheet' href='https://fonts.googleapis.com/css2?"
    "family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500"
    "&display=block'>"
)

COVER_BODY = """
<section class="cover">
  <div class="cover-top">
    <span class="cover-eyebrow">WHITEPAPER</span>
    <span class="cover-eyebrow right">VERSION 3.0</span>
  </div>
  <hr class="cover-rule"/>
  <div class="cover-main">
    <h1 class="cover-title">The vibegraph:<br/>your vibes, codified</h1>
    <p class="cover-desc">A vibegraph is the network of identity, context,
    knowledge, and memory that governs how AI thinks, writes, and acts for one
    person, and any businesses they own or operate.</p>
  </div>
  <div class="cover-bottom">
    <hr class="cover-rule"/>
    <div class="cover-meta">
      <div><p>October 2026</p><p>Ryan Charleston</p></div>
      <div class="right"><p>vibegraph.ai</p><p>vibegraph.md</p></div>
    </div>
  </div>
</section>
"""

SANS = "Inter, sans-serif"
DISPLAY = "'Space Grotesk', Inter, sans-serif"
MONO = "'IBM Plex Mono', Menlo, monospace"

CSS = f"""
* {{ box-sizing: border-box; }}
html {{ font-size: 9.6pt; }}
body {{
  font-family: {SANS};
  color: #1a1a1c; line-height: 1.6; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}}
/* ---- cover ---- */
.cover {{ height: 232mm; display: flex; flex-direction: column; }}
.cover-top {{ display: flex; justify-content: space-between; margin-top: 10mm; }}
.cover-eyebrow {{ font-family: {MONO}; font-size: 8.2pt; letter-spacing: 0.3em; color: #52525b; font-weight: 500; }}
.cover-rule {{ border: none; border-top: 1.6px solid #1a1a1c; margin: 3mm 0 0 0; }}
.cover-main {{ margin-top: 42mm; }}
.cover-title {{ font-family: {DISPLAY}; font-size: 36pt; line-height: 1.05; margin: 0; font-weight: 700; letter-spacing: -0.02em; }}
.cover-desc {{ max-width: 148mm; font-size: 11.5pt; line-height: 1.55; margin-top: 16mm; color: #3f3f46; }}
.cover-bottom {{ margin-top: auto; }}
.cover-bottom .cover-rule {{ border-top: 1px solid #d4d4d8; }}
.cover-meta {{ display: flex; justify-content: space-between; margin-top: 3mm; font-size: 9.5pt; }}
.cover-meta p {{ margin: 0 0 1.2mm 0; }}
.cover-meta .right {{ text-align: right; color: #52525b; font-family: {MONO}; font-size: 9pt; }}
/* ---- body ---- */
h2, h3 {{ font-family: {DISPLAY}; font-weight: 700; letter-spacing: -0.01em; }}
h2 {{ font-size: 17pt; margin: 0 0 3mm 0; break-before: page; }}
h2::before {{ content: ""; display: block; width: 11mm; border-top: 1.4px solid #1a1a1c; margin-bottom: 7mm; padding-top: 2mm; }}
h2:first-child {{ break-before: auto; }}
h3 {{ font-size: 12pt; margin: 7mm 0 2mm 0; page-break-after: avoid; }}
/* A subsection that fits on one page never splits: it moves whole to the
   next page instead of stranding its heading or leaving a gap. Chrome
   ignores the rule for chunks taller than a page, which then flow. */
.keep {{ break-inside: avoid-page; }}
p {{ margin: 0 0 3.2mm 0; text-align: justify; hyphens: auto; }}
strong {{ font-weight: 600; }}
hr {{ border: none; margin: 0; }}
blockquote {{
  margin: 6mm 6mm 6mm 8mm; padding-left: 6mm;
  border-left: 2px solid #b7a8ff; font-family: {DISPLAY}; font-weight: 500; font-size: 12pt;
  page-break-inside: avoid;
}}
blockquote p {{ text-align: left; }}
code {{ font-family: {MONO}; font-size: 8.4pt; background: #f4f4f5; padding: 0.5pt 3pt; border-radius: 3px; }}
pre {{
  font-family: {MONO}; font-size: 7.5pt; line-height: 1.5; background: #f4f4f5;
  padding: 3mm 4mm; border-radius: 3px; margin: 3mm 0 4mm 0;
  white-space: pre-wrap; overflow-wrap: anywhere; page-break-inside: avoid;
}}
pre code {{ background: none; padding: 0; font-size: inherit; }}
a {{ color: inherit; text-decoration: none; }}
ul, ol {{ margin: 0 0 3.2mm 0; padding-left: 7mm; }}
li {{ margin-bottom: 1.4mm; }}
table {{
  border-collapse: collapse; width: 100%; margin: 4mm 0 5mm 0;
  font-size: 8.4pt; line-height: 1.45; page-break-inside: avoid;
}}
th {{ text-align: left; border-top: 1.4px solid #1a1a1c; border-bottom: 1px solid #1a1a1c; padding: 2mm 3mm 2mm 0; font-weight: 600; }}
td {{ border-bottom: 1px solid #e4e4e7; padding: 2mm 3mm 2mm 0; vertical-align: top; }}
figure {{ margin: 6mm 0; page-break-inside: avoid; }}
figure svg {{ width: 100%; height: auto; border-radius: 4px; }}
figcaption {{ font-style: italic; font-size: 8.8pt; color: #52525b; text-align: center; margin-top: 2mm; }}
.colophon {{ margin-top: 10mm; font-style: italic; font-size: 8.6pt; color: #52525b; }}
"""


def inline_figures(html: str) -> str:
    """Replace <img src="figures/X.svg"> + trailing <em> caption with an
    inlined <figure><svg/><figcaption/></figure>. build_figures.py already
    prefixes every id per figure, so the four SVGs can share one document."""

    def figure_block(match: re.Match) -> str:
        src, caption = match.group(1), match.group(2)
        svg = (WHITEPAPER / src).read_text()
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
        return f"<figure>{svg}<figcaption>{caption}</figcaption></figure>"

    return re.sub(
        r'<p><img[^>]*src="([^"]+)"[^>]*/?></p>\s*<p><em>(.*?)</em></p>',
        figure_block,
        html,
        flags=re.S,
    )


def wrap_subsections(html: str) -> str:
    """Wrap each h3 plus its content (up to the next heading) in a .keep
    div, so a subsection that fits a page moves whole instead of leaving a
    heading stranded above a gap."""
    parts = re.split(r"(?=<h[23])", html)
    out = []
    for part in parts:
        if part.startswith("<h3"):
            out.append(f'<div class="keep">{part}</div>')
        else:
            out.append(part)
    return "".join(out)


def page(title: str, body: str) -> str:
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>{title}</title>{FONTS}<style>{CSS}</style></head>"
        f"<body>{body}</body></html>"
    )


def main() -> None:
    md_text = MD.read_text()
    # The cover replaces everything up to and including the first rule.
    body_md = md_text.split("\n---\n", 1)[1]
    # sane_lists honors the source's start numbers, keeping the references
    # numbered continuously across their category headings.
    body_html = markdown.markdown(
        body_md, extensions=["tables", "sane_lists", "fenced_code"]
    )
    body_html = inline_figures(body_html)
    body_html = wrap_subsections(body_html)
    # The authorship paragraph at the end becomes the colophon.
    body_html = re.sub(
        r"<p><em>(Authored by .*?)</em></p>",
        r'<p class="colophon">\1</p>',
        body_html,
        flags=re.S,
    )

    (HERE / "cover.html").write_text(page("Cover", COVER_BODY))
    (HERE / "body.html").write_text(page("vibegraph whitepaper 3.0", body_html))

    subprocess.run([NODE, str(HERE / "render.js")], check=True)

    writer = PdfWriter()
    for name in ["cover.pdf", "body.pdf"]:
        writer.append(str(HERE / name))
    writer.add_metadata({"/Title": "The vibegraph: your vibes, codified", "/Author": "Ryan Charleston"})
    with open(PDF_OUT, "wb") as f:
        writer.write(f)
    print(f"wrote {PDF_OUT}")


if __name__ == "__main__":
    main()
