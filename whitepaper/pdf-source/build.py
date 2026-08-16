#!/usr/bin/env python3
"""Build The-Vibegraph-Whitepaper-v1.5.pdf from the markdown source.

Reads ../The-Vibegraph-Whitepaper-v1.5.md, renders it as two print-styled
HTML documents (cover.html without a footer, body.html with the running
footer and page numbers starting at 1 on the Introduction, as v1.0
numbered), prints both with puppeteer-core driving the installed Chrome
(render.js), and merges them with pypdf.

  python3 build.py

Requires: the `markdown` and `pypdf` packages, `npm install` in this
directory (puppeteer-core), Google Chrome, and the Inter font installed.
Body serif is Charter (macOS system); Menlo stands in for the
Adobe-activated IBM Plex Mono inside the figures.
"""
import re
import subprocess
from pathlib import Path

import markdown
from pypdf import PdfWriter

HERE = Path(__file__).parent
WHITEPAPER = HERE.parent
MD = WHITEPAPER / "The-Vibegraph-Whitepaper-v1.5.md"
PDF_OUT = WHITEPAPER / "The-Vibegraph-Whitepaper-v1.5.pdf"
NODE = "/opt/homebrew/opt/node@22/bin/node"

COVER_BODY = """
<section class="cover">
  <div class="cover-top">
    <span class="cover-eyebrow">WHITEPAPER</span>
    <span class="cover-eyebrow right">VERSION 1.5</span>
  </div>
  <hr class="cover-rule"/>
  <div class="cover-main">
    <h1 class="cover-title">The Vibegraph<span class="tm">™</span></h1>
    <p class="cover-tagline">Your Vibes, Codified.</p>
    <p class="cover-desc">An open framework for codifying human identity and
    personal brand as structured, portable AI context: digital DNA any AI can
    read today, and the protocol for an agent that operates as its
    creator&rsquo;s clone, a Vibeclone.</p>
  </div>
  <div class="cover-bottom">
    <hr class="cover-rule"/>
    <div class="cover-meta">
      <div><p>August 2026</p><p>Ryan Charleston</p></div>
      <div class="right"><p>vibegraph.ai</p><p>vibegraph.md</p></div>
    </div>
  </div>
</section>
"""

CSS = """
* { box-sizing: border-box; }
html { font-size: 10.4pt; }
body {
  font-family: Charter, Georgia, serif;
  color: #1a1a1c; line-height: 1.62; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
/* ---- cover ---- */
.cover { height: 232mm; display: flex; flex-direction: column; }
.cover-top { display: flex; justify-content: space-between; margin-top: 10mm; }
.cover-eyebrow { font-family: Menlo, monospace; font-size: 8.2pt; letter-spacing: 0.35em; color: #52525b; font-weight: 600; }
.cover-rule { border: none; border-top: 1.6px solid #1a1a1c; margin: 3mm 0 0 0; }
.cover-main { margin-top: 42mm; }
.cover-title { font-size: 34pt; margin: 0; font-weight: 700; letter-spacing: -0.01em; }
.cover-title .tm { font-size: 11pt; vertical-align: super; font-weight: 400; }
.cover-tagline { font-style: italic; font-size: 13.5pt; margin: 4mm 0 0 0; }
.cover-desc { max-width: 152mm; font-size: 11pt; margin-top: 16mm; }
.cover-bottom { margin-top: auto; }
.cover-bottom .cover-rule { border-top: 1px solid #d4d4d8; }
.cover-meta { display: flex; justify-content: space-between; margin-top: 3mm; font-size: 9.5pt; }
.cover-meta p { margin: 0 0 1.2mm 0; }
.cover-meta .right { text-align: right; color: #52525b; }
/* ---- body ---- */
h2 { font-size: 16.5pt; margin: 0 0 3mm 0; break-before: page; }
h2::before { content: ""; display: block; width: 11mm; border-top: 1.4px solid #1a1a1c; margin-bottom: 7mm; padding-top: 2mm; }
h2:first-child { break-before: auto; }
h3 { font-size: 12pt; margin: 7mm 0 2mm 0; page-break-after: avoid; }
/* A subsection that fits on one page never splits: it moves whole to the
   next page instead of stranding its heading or leaving a gap. Chrome
   ignores the rule for chunks taller than a page, which then flow. */
.keep { break-inside: avoid-page; }
p { margin: 0 0 3.2mm 0; text-align: justify; hyphens: auto; }
strong { font-weight: 700; }
hr { border: none; margin: 0; }
blockquote {
  margin: 6mm 6mm 6mm 8mm; padding-left: 6mm;
  border-left: 2px solid #1a1a1c; font-style: italic; font-size: 11.2pt;
  page-break-inside: avoid;
}
blockquote p { text-align: left; }
code { font-family: Menlo, monospace; font-size: 8.8pt; background: #f4f4f5; padding: 0.5pt 3pt; border-radius: 3px; }
a { color: inherit; text-decoration: none; }
ul, ol { margin: 0 0 3.2mm 0; padding-left: 7mm; }
li { margin-bottom: 1.4mm; }
table {
  border-collapse: collapse; width: 100%; margin: 4mm 0 5mm 0;
  font-family: Inter, sans-serif; font-size: 8.6pt; line-height: 1.45;
  page-break-inside: avoid;
}
th { text-align: left; border-top: 1.4px solid #1a1a1c; border-bottom: 1px solid #1a1a1c; padding: 2mm 3mm 2mm 0; }
td { border-bottom: 1px solid #e4e4e7; padding: 2mm 3mm 2mm 0; vertical-align: top; }
figure { margin: 6mm 0; page-break-inside: avoid; }
figure svg { width: 100%; height: auto; }
figcaption { font-style: italic; font-size: 9.3pt; color: #52525b; text-align: center; margin-top: 2mm; }
.colophon { margin-top: 10mm; font-style: italic; font-size: 9pt; color: #52525b; }
"""


def inline_figures(html: str) -> str:
    """Replace <img src="figures/X.svg"> + trailing <em> caption with an
    inlined, class-namespaced <figure><svg/><figcaption/></figure>."""
    counter = {"n": 0}

    def figure_block(match: re.Match) -> str:
        src, caption = match.group(1), match.group(2)
        counter["n"] += 1
        prefix = f"f{counter['n']}"
        svg = (WHITEPAPER / src).read_text()
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
        svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
        # Both figures export Illustrator's generic class names (.st0, .st1,
        # ...) with DIFFERENT meanings, and SVG <style> is document-global
        # once inlined: without namespacing, figure 2's styles restyle
        # figure 1 (its arrow style landed on the "One person. Three
        # parts." subtitle). Prefix every class per figure.
        svg = re.sub(r"\.st(\d+)", rf".{prefix}-st\1", svg)
        svg = re.sub(r'class="st(\d+)"', rf'class="{prefix}-st\1"', svg)
        svg = svg.replace('id="Layer_1"', f'id="{prefix}-layer"')
        # Illustrator's PostScript-style family names resolve to nothing in
        # Chrome; substitute installed faces. IBM Plex Mono is
        # Adobe-activated only, so Menlo stands in for print.
        svg = svg.replace("IBMPlexMono-Bold, 'IBM Plex Mono'", "Menlo, monospace")
        svg = svg.replace("IBMPlexMono-Medium, 'IBM Plex Mono'", "Menlo, monospace")
        svg = svg.replace("IBMPlexMono, 'IBM Plex Mono'", "Menlo, monospace")
        svg = svg.replace("Inter-SemiBold, Inter", "Inter, sans-serif")
        svg = svg.replace("Inter-Regular, Inter", "Inter, sans-serif")
        svg = svg.replace("Inter-Italic, Inter, sans-serif", "Inter, sans-serif")
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
        f"<title>{title}</title><style>{CSS}</style></head>"
        f"<body>{body}</body></html>"
    )


def main() -> None:
    md_text = MD.read_text()
    # The cover replaces everything up to and including the first rule.
    body_md = md_text.split("\n---\n", 1)[1]
    # sane_lists honors the source's start numbers, keeping the references
    # numbered continuously across their category headings as in v1.0.
    body_html = markdown.markdown(body_md, extensions=["tables", "sane_lists"])
    body_html = inline_figures(body_html)
    body_html = wrap_subsections(body_html)
    # The trademark footer paragraph becomes the colophon.
    body_html = re.sub(
        r"<p><em>(Vibegraph™ and Vibeclone™.*?)</em></p>",
        r'<p class="colophon">\1</p>',
        body_html,
        flags=re.S,
    )

    (HERE / "cover.html").write_text(page("Cover", COVER_BODY))
    (HERE / "body.html").write_text(page("The Vibegraph Whitepaper v1.5", body_html))

    subprocess.run([NODE, str(HERE / "render.js")], check=True)

    writer = PdfWriter()
    for name in ["cover.pdf", "body.pdf"]:
        writer.append(str(HERE / name))
    with open(PDF_OUT, "wb") as f:
        writer.write(f)
    print(f"wrote {PDF_OUT}")


if __name__ == "__main__":
    main()
