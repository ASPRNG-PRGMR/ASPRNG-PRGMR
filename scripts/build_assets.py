#!/usr/bin/env python3
"""Build the profile's self-contained SVG artwork using only the standard library."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BG = "#0b1118"
SURFACE = "#101923"
LINE = "#273442"
WHITE = "#edf4f7"
MUTED = "#a4b4c4"
LIME = "#c5f277"


def text(x, y, value, size=20, color=WHITE, weight=400, mono=False, extra=""):
    family = "'DejaVu Sans Mono', monospace" if mono else "Arial, Helvetica, sans-serif"
    return (f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" '
            f'font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>')


def rect(x, y, w, h, fill=SURFACE, stroke=LINE, rx=8, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" {extra}/>')


def path(d, color=LINE, width=2, extra=""):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" {extra}/>'


def circle(x, y, r, color, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" {extra}/>'


def svg(w, h, title, description, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">\n'
            f'<title id="title">{escape(title)}</title>\n'
            f'<desc id="desc">{escape(description)}</desc>\n{body}\n</svg>\n')


def board(x, y):
    """A circuit diagram: four domains connected to one systems core."""
    s = '<g transform="translate(%s %s)">' % (x, y)
    s += circle(165, 140, 122, "none", f'stroke="{LINE}" stroke-dasharray="3 9"')
    s += circle(165, 140, 86, "none", f'stroke="{LINE}"')
    for d in ["M165 33V96", "M165 184V247", "M35 140H121", "M209 140H295"]:
        s += path(d, LIME)
    for a, b in [(165, 72), (165, 214), (80, 140), (252, 140)]:
        s += circle(a, b, 4, LIME)
    for i in range(5):
        p = 113 + i * 14
        q = 138 + i * 14
        s += path(f"M{q} 86V96M{q} 184V194M111 {p}H121M209 {p}H219", MUTED, 1)
    s += rect(121, 96, 88, 88, "#18251e", "#72984a", 12)
    s += text(165, 148, "ARS", 28, LIME, 700, True, 'text-anchor="middle"')
    nodes = [(104, 0, 122, "FIRMWARE"), (104, 247, 122, "SYSTEMS"),
             (-25, 122, 110, "VISION"), (245, 122, 110, "ROBOTICS")]
    for nx, ny, nw, label in nodes:
        s += rect(nx, ny, nw, 36, BG, LINE, 6)
        s += text(nx + nw / 2, ny + 23, label, 13, MUTED, 400, True, 'text-anchor="middle"')
    return s + '</g>'


def header(mobile=False):
    w, h = (640, 680) if mobile else (1200, 440)
    s = '''<defs>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="#20303b" stroke-opacity=".42"/>
  </pattern>
  <radialGradient id="glow"><stop stop-color="#42612e" stop-opacity=".23"/>
    <stop offset="1" stop-color="#0b1118" stop-opacity="0"/></radialGradient>
</defs>'''
    s += rect(1, 1, w - 2, h - 2, BG, LINE, 18)
    s += rect(2, 2, w - 4, h - 4, "url(#grid)", "none", 18)
    s += f'<ellipse cx="{w - 200}" cy="230" rx="340" ry="250" fill="url(#glow)"/>'
    s += rect(32, 32, 40, 4, LIME, "none", 2)
    s += text(88, 40, "ASPRNG-PRGMR / ENGINEERING LOG", 14, MUTED, mono=True)
    s += text(40, 100, "ARNAB RANJAN SIKDAR", 22, WHITE, 700, extra='letter-spacing="2"')
    s += text(36, 178, "I build across", 64, WHITE, 700, extra='letter-spacing="-2"')
    s += text(36, 251, "the whole stack.", 64, LIME, 700, extra='letter-spacing="-2"')
    if mobile:
        s += text(40, 295, "From the first byte to the physical world.", 21, MUTED)
        s += board(155, 331)
        s += path("M40 640H600", LINE, 1)
        s += text(40, 666, "CURIOUS BY DEFAULT. HANDS ON BY DESIGN.", 14, MUTED, mono=True)
    else:
        s += text(40, 302, "From the first byte to the physical world.", 24, MUTED)
        s += board(800, 65)
        s += path("M40 370H1160", LINE, 1)
        s += text(40, 409, "LOW-LEVEL CURIOSITY. REAL-WORLD SYSTEMS.", 15, MUTED, mono=True)
        s += text(1160, 409, "RUST / C++ / PYTHON / EMBEDDED C", 14, LIME, mono=True,
                  extra='text-anchor="end"')
    return svg(w, h, "Arnab Ranjan Sikdar — systems engineer",
               "I build across the whole stack. From the first byte to the physical world. "
               "Firmware, systems, vision, and robotics.", s)


def main():
    ASSETS.mkdir(exist_ok=True)
    (ROOT / "about_me.svg").write_text(header(), encoding="utf-8")
    (ASSETS / "header-mobile.svg").write_text(header(mobile=True), encoding="utf-8")
    print("Built desktop and mobile headers.")


if __name__ == "__main__":
    main()
