#!/usr/bin/env python3
"""Build the four whitepaper figures as SVG from the specs in FIGURES-v2.0.md.

  python3 build_figures.py

Standard library only. Writes figure-1-anatomy.svg, figure-2-business-brand.svg,
figure-3-where-tools-fit.svg, and figure-4-root-file-and-consumption.svg next to
this file. Palette and type follow the brand system: background #0a0a0a,
foreground #f6f6f6, muted #b8b8b8, accent #b7a8ff, border #2b2b2b; Space Grotesk
for titles, Inter for labels, IBM Plex Mono for file names and key-value pairs.
Each family carries a fallback (Inter, Menlo) for machines without the faces.

Every id is prefixed per figure (f1-, f2-, ...) because build.py inlines all
four SVGs into one HTML document, where ids are global.
"""
import math
import re
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).parent

BG, FG, MUTED, ACCENT, BORDER = "#0a0a0a", "#f6f6f6", "#b8b8b8", "#b7a8ff", "#2b2b2b"
DISPLAY = "'Space Grotesk', Inter, sans-serif"
SANS = "Inter, sans-serif"
MONO = "'IBM Plex Mono', Menlo, monospace"


# ---------------------------------------------------------------- primitives

def text(x, y, s, size, family=SANS, fill=FG, weight=400, anchor="start", italic=False):
    style = ' font-style="italic"' if italic else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{style}>{escape(s)}</text>'
    )


def rect(x, y, w, h, stroke=BORDER, fill="none", rx=8, dash=None, sw=1.0):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    )


def line(x1, y1, x2, y2, stroke=MUTED, sw=1.0, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'
    )


def arrow_marker(fid, fill=FG):
    return (
        f'<marker id="{fid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{fill}"/></marker>'
    )


def tw(s, size, mono=False):
    """Rough rendered width; good enough to size boxes and knockouts."""
    return len(s) * size * (0.6 if mono else 0.56)


def svg(w, h, title, body):
    label = escape(title, {'"': "&quot;"})
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-label="{label}">\n'
        f'<rect width="{w}" height="{h}" fill="{BG}"/>\n' + "\n".join(body) + "\n</svg>\n"
    )


def node(x, y, w, h, title, subs=(), title_family=SANS, title_size=14, rule=False):
    out = [rect(x, y, w, h)]
    if rule:
        out.append(line(x + 1, y + 8, x + 1, y + h - 8, ACCENT, 2))
    ty = y + 25 if subs else y + h / 2 + title_size * 0.36
    weight = 500 if title_family == MONO else 400
    out.append(text(x + 14, ty, title, title_size, title_family, FG, weight))
    for i, s in enumerate(subs):
        out.append(text(x + 14, ty + 19 + i * 17, s, 11, MONO, MUTED))
    return out


# ------------------------------------------------------ figure 1: the anatomy

def figure1():
    W, H = 1200, 800
    b = [f"<defs>{arrow_marker('f1')}</defs>"]
    b.append(text(600, 56, "Maya Okafor", 26, DISPLAY, FG, 500, "middle"))
    b.append(text(600, 80, "one person", 13, SANS, MUTED, 400, "middle"))
    b.append(line(600, 92, 600, 127, FG, 1.5, marker="f1-arrow"))
    b.append(rect(440, 130, 320, 64, ACCENT, BG, 10, sw=1.5))
    b.append(text(600, 160, "VIBEGRAPH.md", 18, MONO, FG, 500, "middle"))
    b.append(text(600, 181, "root file · read first", 12, SANS, MUTED, 400, "middle"))

    xs = [44 + i * 284 for i in range(4)]
    top, rh, bus = 330, 440, 236
    b.append(line(600, 194, 600, bus))
    b.append(line(xs[0] + 130, bus, xs[3] + 130, bus))
    labels = [
        ("kind: identity", "scope: public · when: always"),
        ("kind: brand", "scope: public"),
        ("kind: area", "scope: scoped/private"),
        ("kind: source/memory/project/agent", "scope: scoped"),
    ]
    for x, (l1, l2) in zip(xs, labels):
        cx = x + 130
        b.append(line(cx, bus, cx, top))
        w = max(tw(l1, 10.5, True), tw(l2, 10.5, True)) + 16
        b.append(rect(cx - w / 2, 258, w, 44, "none", BG, 4, sw=0))
        b.append(text(cx, 276, l1, 10.5, MONO, MUTED, 400, "middle"))
        b.append(text(cx, 292, l2, 10.5, MONO, MUTED, 400, "middle"))

    titles = ["identity core", "brands", "areas", "components"]
    for i, x in enumerate(xs):
        b.append(rect(x, top, 260, rh, BORDER, "none", 12, dash="6 4" if i == 3 else None))
        b.append(text(x + 20, top + 34, titles[i], 15, SANS, FG, 600))
    b.append(text(xs[3] + 20, top + 54, "registered, not stored", 12, SANS, MUTED))
    foot = top + rh - 20

    # identity core
    x = xs[0] + 16
    b += node(x, top + 56, 228, 84, "personality", ["Big Five · Enneagram", "other instruments"])
    b += node(x, top + 156, 228, 48, "integrated reading")
    b += node(x, top + 220, 228, 66, "Ikigai", ["four pillars · one statement"])
    b.append(text(xs[0] + 20, foot, "identity/maya-okafor.md", 11, MONO, MUTED))

    # brands: the business brand is inset under the personal brand, accent rule
    x = xs[1] + 16
    b += node(x, top + 56, 228, 84, "maya-okafor.brand.md", ["personal · 12 + 8", "when: always"], MONO, 12.5)
    b += node(x + 16, top + 156, 212, 100, "delivery-os.brand.md",
              ["business", "foundations + 12 + 8", "when: on-task"], MONO, 12.5, rule=True)
    b.append(text(xs[1] + 20, foot, "brands/", 11, MONO, MUTED))

    # areas
    x = xs[2] + 16
    areas = [("career/", "scope: scoped · on-task"), ("skills/", "scope: scoped · on-task"),
             ("finances/", "scope: private · on-grant")]
    for i, (name, sub) in enumerate(areas):
        b += node(x, top + 56 + i * 68, 228, 56, name, [sub], MONO, 13)
    b.append(text(xs[2] + 20, foot, "areas/<area>/index.md", 11, MONO, MUTED))

    # components
    x = xs[3] + 16
    comps = [("Obsidian vault", "kind: source"), ("Claude memory", "kind: memory"),
             ("site repo", "kind: project"), ("writing agent", "kind: agent")]
    for i, (name, sub) in enumerate(comps):
        b += node(x, top + 76 + i * 68, 228, 56, name, [sub], SANS, 13.5)
    b.append(text(xs[3] + 20, foot, "components.md", 11, MONO, MUTED))

    return svg(W, H, "Figure 1: the anatomy of a vibegraph", b)


# ------------------------------------------- figure 2: a nested business brand

def figure2():
    W, H = 1200, 720
    b = [f"<defs>{arrow_marker('f2', MUTED)}</defs>"]
    b.append(rect(24, 24, 1152, 672, BORDER, "none", 14))
    b.append(text(56, 70, "Maya Okafor's vibegraph", 22, DISPLAY, FG, 500))

    cols = [
        (64, "personal brand", "when: always", "foundation: identity core",
         ["Big Five · Enneagram", "other instruments", "Ikigai"]),
        (636, "business brand: Delivery OS", "when: on-task", "foundations",
         ["Aaker's five dimensions", "archetype", "Golden Circle + mission, vision, values"]),
    ]
    for x, head, when, ftitle, flist in cols:
        cx = x + 250
        b.append(text(x, 114, head, 15, SANS, FG, 600))
        b.append(text(x, 134, when, 11, MONO, ACCENT))
        b.append(rect(x, 150, 500, 120))
        b.append(text(x + 18, 177, ftitle, 13, SANS, FG, 600))
        for i, s in enumerate(flist):
            b.append(text(x + 18, 201 + i * 20, s, 11.5, MONO, MUTED))
        b.append(line(cx, 270, cx, 314, MUTED, 1.2, marker="f2-arrow"))
        b.append(rect(x, 318, 500, 60))
        b.append(text(x + 18, 343, "Brand Context", 14, SANS, FG, 600))
        b.append(text(x + 18, 363, "12 elements · the brand in words", 11, MONO, MUTED))
        b.append(line(cx, 378, cx, 402, MUTED, 1.2, marker="f2-arrow"))
        b.append(rect(x, 406, 500, 60))
        b.append(text(x + 18, 431, "Brand Visuals", 14, SANS, FG, 600))
        b.append(text(x + 18, 451, "8 elements · the brand in pictures", 11, MONO, MUTED))

    # the shared Why between the two foundations
    b.append(line(564, 210, 636, 210, MUTED, 1.2, dash="2 4"))
    b.append(line(600, 210, 600, 276, MUTED, 1.2, dash="2 4"))
    label = "shared Why, checked against each other"
    pw = tw(label, 12) + 28
    b.append(rect(600 - pw / 2, 276, pw, 26, BORDER, BG, 13))
    b.append(text(600, 293, label, 12, SANS, MUTED, 400, "middle", italic=True))

    # business areas strip under the right column
    x = 636
    b.append(line(x + 250, 466, x + 250, 510, MUTED, 1.2, marker="f2-arrow"))
    b.append(text(x, 496, "business areas", 12, SANS, FG, 600))
    b.append(rect(x, 514, 500, 56))
    cx = x + 16
    for chip in ["CRM", "operations", "playbooks and SOPs", "templates"]:
        w = tw(chip, 11, True) + 22
        b.append(rect(cx, 530, w, 24, BORDER, "none", 6))
        b.append(text(cx + w / 2, 546, chip, 11, MONO, MUTED, 400, "middle"))
        cx += w + 10

    b.append(line(24, 612, 1176, 612, BORDER))
    b.append(text(600, 656, "personal · when: always | business · when: on-task "
                  "(any Delivery OS writing, design, or publishing)", 11, MONO, MUTED, 400, "middle"))
    return svg(W, H, "Figure 2: a business brand inside its owner's vibegraph", b)


# ---------------------------------------------- figure 3: where existing tools fit

CX = CY = 500
RING = 390
CHIP_H = 22


def polar(r, deg):
    a = math.radians(deg)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def in_wedge(px, py, a0, a1, rmin, rmax, pad, excl):
    dx, dy = px - CX, py - CY
    r = math.hypot(dx, dy)
    if r < rmin or r > rmax:
        return False
    u0 = (math.cos(math.radians(a0)), math.sin(math.radians(a0)))
    u1 = (math.cos(math.radians(a1)), math.sin(math.radians(a1)))
    if u0[0] * dy - u0[1] * dx < pad or u1[0] * dy - u1[1] * dx > -pad:
        return False
    return not any(ex <= px <= ex + ew and ey <= py <= ey + eh for ex, ey, ew, eh in excl)


def row_interval(y, a0, a1, rmin, rmax, excl):
    best, start = None, None
    for x in range(0, 1002, 2):
        ok = x <= 1000 and all(
            in_wedge(x, yy, a0, a1, rmin, rmax, 8, excl)
            for yy in (y - CHIP_H / 2, y, y + CHIP_H / 2)
        )
        if ok and start is None:
            start = x
        elif not ok and start is not None:
            if best is None or (x - 2 - start) > (best[1] - best[0]):
                best = (start, x - 2)
            start = None
    return best


def chip_w(s):
    return tw(s, 12) + 20


def pack(chips, a0, a1, rmin, rmax, excl, gap=8, pitch=30):
    # Widest chips first, so a long name gets a wide row before short ones use it up.
    chips = sorted(chips, key=chip_w, reverse=True)
    rows = []
    for k in range(-16, 17):
        y = CY + k * pitch
        iv = row_interval(y, a0, a1, rmin, rmax, excl)
        if iv and iv[1] - iv[0] >= 50:
            mid = (iv[0] + iv[1]) / 2
            rows.append((math.hypot(mid - CX, y - CY), y, iv))
    rows.sort()
    placed, i = [], 0
    for _, y, (xs, xe) in rows:
        if i >= len(chips):
            break
        widths, total = [], 0.0
        while i + len(widths) < len(chips):
            w = chip_w(chips[i + len(widths)])
            add = w + (gap if widths else 0)
            if total + add > xe - xs:
                break
            widths.append(w)
            total += add
        x = (xs + xe) / 2 - total / 2
        for w in widths:
            placed.append((chips[i], x, y - CHIP_H / 2, w))
            x += w + gap
            i += 1
    if i < len(chips):
        raise SystemExit(f"figure 3: no room for {chips[i:]}")
    return placed


def arc_path(r, d0, d1):
    x0, y0 = polar(r, d0)
    x1, y1 = polar(r, d1)
    large = 1 if (d1 - d0) % 360 > 180 else 0
    return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f}"


def figure3():
    W, H = 1000, 1000
    b = []
    wedges = [
        ("knowledge stores", "source",
         ["Obsidian", "Logseq", "Anytype", "Notion", "Tana", "Reflect", "Mem", "Capacities",
          "Heptabase", "Notion Business", "Slite", "Guru", "Tettra", "context graphs", "GBrain"]),
        ("memory layers", "memory",
         ["Mem0", "Zep", "Graphiti", "Letta", "Cognee", "Hindsight", "LangMem", "ChatGPT memory",
          "Claude memory", "Codex memory", "Gemini personal intelligence"]),
        ("projects", "project",
         ["AGENTS.md", "CLAUDE.md", "GEMINI.md", "Cursor rules", "AIS-OS", "agent folders"]),
        ("skills", "skill", ["SKILL.md files", "the skills area"]),
        ("agents", "agent", ["a vibeclone · per grant", "GBrain"]),
    ]

    # the public-slice band sits outside the ring on the agent wedge only
    a0_agent = -126 + 72 * 4
    band = (f'<path d="{arc_path(490, a0_agent + 6, a0_agent + 66)} '
            f'L{polar(420, a0_agent + 66)[0]:.1f},{polar(420, a0_agent + 66)[1]:.1f} '
            f'A420,420 0 0 0 {polar(420, a0_agent + 6)[0]:.1f},{polar(420, a0_agent + 6)[1]:.1f} Z" '
            f'fill="{FG}" fill-opacity="0.06" stroke="none"/>')
    b.append(band)

    b.append(f'<circle cx="{CX}" cy="{CY}" r="{RING}" fill="none" stroke="{ACCENT}" stroke-width="1"/>')
    for i in range(5):
        a = -126 + 72 * i
        x0, y0 = polar(112, a)
        x1, y1 = polar(RING, a)
        b.append(line(x0, y0, x1, y1, BORDER, 1))

    for i, (title, kind, chips) in enumerate(wedges):
        a0 = -126 + 72 * i
        a1 = a0 + 72
        twid = tw(title, 14) + tw(f" · {kind}", 14, True)
        # Walk the title out along the wedge's center ray until its box clears the disc.
        r = 150
        while True:
            tx, ty = polar(r, a0 + 36)
            nx = min(max(CX, tx - twid / 2), tx + twid / 2)
            ny = min(max(CY, ty - 12), ty + 8)
            if math.hypot(nx - CX, ny - CY) > 132:
                break
            r += 4
        full = f"{title} · {kind}"
        b.append(
            f'<text x="{tx:.1f}" y="{ty + 5:.1f}" font-family="{SANS}" font-size="14" font-weight="600" '
            f'fill="{FG}" text-anchor="middle">{escape(title)}<tspan font-family="{MONO}" '
            f'font-weight="400" fill="{MUTED}"> · {escape(kind)}</tspan></text>'
        )
        excl = [(tx - twid / 2 - 12, ty - 16, twid + 24, 30)]
        for label, x, y, w in pack(chips, a0, a1, 150, RING - 18, excl):
            b.append(rect(x, y, w, CHIP_H, BORDER, BG, 6))
            b.append(text(x + w / 2, y + 15, label, 12, SANS, MUTED, 400, "middle"))
        assert full

    # clone platforms, outside the ring
    for name, deg in [("Delphi", 180), ("Personal.ai", 196), ("HeyGen", 212), ("ElevenLabs", 227)]:
        px, py = polar(452, deg)
        w = chip_w(name)
        b.append(rect(px - w / 2, py - CHIP_H / 2, w, CHIP_H, BORDER, BG, 6))
        b.append(text(px, py + 4, name, 12, SANS, MUTED, 400, "middle"))

    b.append(f'<defs><path id="f3-ring-label" d="{arc_path(398, -120, -60)}"/>'
             f'<path id="f3-band-label" d="{arc_path(503, a0_agent + 4, a0_agent + 68)}"/></defs>')
    b.append(f'<text font-family="{MONO}" font-size="11" fill="{ACCENT}"><textPath href="#f3-ring-label" '
             f'startOffset="50%" text-anchor="middle">scope: scoped</textPath></text>')
    b.append(f'<text font-family="{MONO}" font-size="10.5" fill="{MUTED}"><textPath href="#f3-band-label" '
             f'startOffset="50%" text-anchor="middle">public slice only</textPath></text>')

    b.append(f'<circle cx="{CX}" cy="{CY}" r="110" fill="{ACCENT}"/>')
    b.append(text(CX, CY - 4, "identity core", 18, DISPLAY, BG, 600, "middle"))
    b.append(text(CX, CY + 20, "+ VIBEGRAPH.md", 18, DISPLAY, BG, 600, "middle"))

    b.append(f'<circle cx="772" cy="954" r="7" fill="{ACCENT}"/>')
    b.append(text(786, 958, "built here", 12, SANS, MUTED))
    b.append(rect(868, 944, 22, 20, BORDER, BG, 6))
    b.append(text(898, 958, "registered", 12, SANS, MUTED))
    return svg(W, H, "Figure 3: where existing tools fit in a vibegraph", b)


# --------------------------------------- figure 4: root file and consumption

ROOT_LINES = [
    "---",
    'vibegraph: "2.0"',
    "owner: Maya Okafor",
    "identity: identity/maya-okafor.md",
    "updated: 2026-09-30",
    "---",
    "# Maya Okafor's vibegraph",
    "Read this file first. It tells you who you",
    "emulate and where everything else lives.",
    "## Identity",
    "- [Maya Okafor](identity/maya-okafor.md)",
    "    · kind: identity · scope: public · when: always",
    "## Brands",
    "- [Maya Okafor (personal brand)]",
    "    (brands/maya-okafor.brand.md)",
    "    · kind: brand · type: personal",
    "    · scope: public · when: always",
    "- [Delivery OS](brands/delivery-os.brand.md)",
    "    · kind: brand · type: business",
    "    · scope: public · when: on-task",
    "## Areas",
    "- [Career](areas/career/index.md)",
    "    · kind: area · scope: scoped · when: on-task",
    "- [Finances](areas/finances/index.md)",
    "    · kind: area · scope: private · when: on-grant",
    "## Components",
    '- Obsidian vault "Notes" · kind: source',
    "- Claude memory · kind: memory",
    "## Read order",
    "1. identity/maya-okafor.md",
    "2. brands/maya-okafor.brand.md",
    "3. the brand or area the task names",
    "4. nothing else without a grant",
]


def root_line(x, y, s):
    color = MUTED if s == "---" else FG
    weight = 500 if s.startswith("#") else 400
    parts = re.split(r"\b(kind|scope|when|type):", s)
    spans = [escape(parts[0])]
    for key, rest in zip(parts[1::2], parts[2::2]):
        spans.append(f'<tspan fill="{ACCENT}">{key}:</tspan>{escape(rest)}')
    return (f'<text x="{x}" y="{y:.1f}" font-family="{MONO}" font-size="10.5" fill="{color}" '
            f'font-weight="{weight}" xml:space="preserve">{"".join(spans)}</text>')


def figure4():
    W, H = 1400, 760
    b = [f"<defs>{arrow_marker('f4')}</defs>"]

    b.append(rect(40, 40, 420, 680, BORDER, BG, 12))
    b.append(text(62, 74, "VIBEGRAPH.md", 14, MONO, FG, 500))
    b.append(text(438, 74, "root file", 12, SANS, MUTED, 400, "end"))
    b.append(line(40, 90, 460, 90, BORDER))
    for i, s in enumerate(ROOT_LINES):
        b.append(root_line(62, 116 + i * 17.8, s))

    lanes = {"paste": 100, "workspace": 235, "mcp": 400, "seed": 680}
    for n, (key, label) in enumerate([("paste", "1. paste"), ("workspace", "2. workspace"),
                                      ("mcp", "3. MCP"), ("seed", "4. seed")]):
        y = lanes[key]
        b.append(text(490, y - 12, label, 16, DISPLAY, FG, 500))
        b.append(line(462, y, 654, y, FG, 1.5, marker="f4-arrow"))

    # 1. paste
    y = lanes["paste"]
    b.append(rect(660, y - 28, 320, 56))
    for i in range(3):
        b.append(f'<circle cx="{676 + i * 11}" cy="{y - 13}" r="3" fill="{MUTED}"/>')
    b.append(text(716, y - 9, "any chat", 13.5, SANS, FG))
    b.append(text(676, y + 16, "root + identity + one brand", 11, MONO, MUTED))

    # 2. workspace
    y = lanes["workspace"]
    b += node(660, y - 28, 320, 56, "Claude Project · custom GPT", ["set once per workspace"], SANS, 13.5)

    # 3. MCP
    y = lanes["mcp"]
    b.append(rect(660, y - 46, 360, 92, ACCENT, BG, 10, sw=1.2))
    b.append(text(678, y - 18, "MCP server", 15, DISPLAY, FG, 500))
    for i, s in enumerate(["scopes become grants", "kinds become resource types", "every read logged"]):
        b.append(text(678, y + 2 + i * 16, s, 11, MONO, MUTED))
    clients = [("Claude", "grant: public + skills"), ("ChatGPT", "grant: public"),
               ("Cursor", "grant: public + project")]
    for i, (name, grant) in enumerate(clients):
        cy = y - 80 + i * 80
        b.append(line(1020, y, 1096, cy, FG, 1.5, marker="f4-arrow"))
        b.append(rect(1100, cy - 28, 200, 56))
        b.append(text(1114, cy - 6, name, 13.5, SANS, FG))
        pw = tw(grant, 10, True) + 16
        b.append(rect(1114, cy + 4, pw, 18, ACCENT, "none", 9))
        b.append(text(1114 + pw / 2, cy + 16.5, grant, 10, MONO, ACCENT, 400, "middle"))

    b.append(line(840, y + 46, 840, 528, MUTED, 1.2, dash="3 4"))
    b.append(rect(660, 530, 640, 82))
    b.append(text(676, 552, "read log", 12, SANS, FG, 600))
    log = [
        "2026-09-30 14:02  claude   read identity/maya-okafor.md       (public)",
        "2026-09-30 14:05  chatgpt  read brands/maya-okafor.brand.md   (public)",
        "2026-09-30 14:09  cursor   read brands/delivery-os.brand.md   (public)",
    ]
    for i, s in enumerate(log):
        b.append(f'<text x="676" y="{570 + i * 15}" font-family="{MONO}" font-size="10" fill="{MUTED}" '
                 f'xml:space="preserve">{escape(s)}</text>')

    # 4. seed
    y = lanes["seed"]
    b += node(660, y - 28, 380, 56, "memory layer", ["substrate; the vibegraph is the schema"], SANS, 13.5)

    return svg(W, H, "Figure 4: the root file and the four consumption modes", b)


def main():
    out = {
        "figure-1-anatomy.svg": figure1(),
        "figure-2-business-brand.svg": figure2(),
        "figure-3-where-tools-fit.svg": figure3(),
        "figure-4-root-file-and-consumption.svg": figure4(),
    }
    for name, body in out.items():
        (HERE / name).write_text(body)
        print(f"wrote {name}")


if __name__ == "__main__":
    main()
