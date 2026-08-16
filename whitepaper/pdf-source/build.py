#!/usr/bin/env python3
"""Build The-Vibegraph-Whitepaper-v1.5.pdf from the markdown source.

Reads ../The-Vibegraph-Whitepaper-v1.5.md, renders it into a print-styled
HTML document (cover page, editorial serif body, mono eyebrows, the two
figures inlined as SVG), and prints it to PDF with headless Chrome.

  python3 build.py

Requires: the `markdown` package, Google Chrome, and the Inter font
installed. Body serif is Charter (macOS system). Running footers and page
numbers are left to the design pass: headless Chrome cannot place content
in the page margin boxes.
"""
import re
import subprocess
from pathlib import Path

import markdown

HERE = Path(__file__).parent
WHITEPAPER = HERE.parent
MD = WHITEPAPER / "The-Vibegraph-Whitepaper-v1.5.md"
HTML_OUT = HERE / "The-Vibegraph-Whitepaper-v1.5.html"
PDF_OUT = WHITEPAPER / "The-Vibegraph-Whitepaper-v1.5.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

COVER = """
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
@page { size: letter; margin: 20mm 24mm 22mm 24mm; }
* { box-sizing: border-box; }
html { font-size: 10.4pt; }
body {
  font-family: Charter, Georgia, serif;
  color: #1a1a1c; line-height: 1.62; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
/* ---- cover ---- */
.cover { height: 236mm; display: flex; flex-direction: column; page-break-after: always; }
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
h2 { font-size: 16.5pt; margin: 9mm 0 3mm 0; page-break-after: avoid; }
h2::before { content: ""; display: block; width: 11mm; border-top: 1.4px solid #1a1a1c; margin-bottom: 7mm; }
h3 { font-size: 12pt; margin: 7mm 0 2mm 0; page-break-after: avoid; }
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
    inlined <figure><svg/><figcaption/></figure>."""

    def figure_block(match: re.Match) -> str:
        src, caption = match.group(1), match.group(2)
        svg = (WHITEPAPER / src).read_text()
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
        svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
        # Illustrator exports PostScript-style family names Chrome cannot
        # resolve; substitute faces that are actually installed. IBM Plex
        # Mono is Adobe-activated only, so Menlo stands in for print.
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


def main() -> None:
    md_text = MD.read_text()
    # The cover replaces everything up to and including the first rule.
    body_md = md_text.split("\n---\n", 1)[1]
    # sane_lists honors the source's start numbers, keeping the references
    # numbered continuously across their category headings as in v1.0.
    body_html = markdown.markdown(body_md, extensions=["tables", "sane_lists"])
    body_html = inline_figures(body_html)
    # The trademark footer paragraph becomes the colophon.
    body_html = re.sub(
        r"<p><em>(Vibegraph™ and Vibeclone™.*?)</em></p>",
        r'<p class="colophon">\1</p>',
        body_html,
        flags=re.S,
    )

    html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>The Vibegraph Whitepaper v1.5</title><style>{CSS}</style></head>"
        f"<body>{COVER}{body_html}</body></html>"
    )
    HTML_OUT.write_text(html)

    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={PDF_OUT}",
            HTML_OUT.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
    print(f"wrote {PDF_OUT}")


if __name__ == "__main__":
    main()
