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
    w, h = (640, 800) if mobile else (1200, 520)
    s = '''<defs>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="#20303b" stroke-opacity=".42"/>
  </pattern>
  <radialGradient id="glow"><stop stop-color="#42612e" stop-opacity=".23"/>
    <stop offset="1" stop-color="#0b1118" stop-opacity="0"/></radialGradient>
</defs>
<style>
  .cursor { animation: blink 1.2s step-end infinite; }
  @keyframes blink {
    0%, 49% { opacity: 1; }
    50%, 100% { opacity: 0; }
  }
  @media (prefers-reduced-motion: reduce) {
    .cursor { animation: none; }
  }
</style>'''
    s += rect(1, 1, w - 2, h - 2, BG, LINE, 18)
    s += rect(2, 2, w - 4, h - 4, "url(#grid)", "none", 18)
    s += f'<ellipse cx="{w - 200}" cy="230" rx="340" ry="250" fill="url(#glow)"/>'

    # Rounded title bar, with a square lower edge like a terminal window.
    s += rect(2, 2, w - 4, 48, SURFACE, "none", 17)
    s += rect(2, 26, w - 4, 24, SURFACE, "none", 0)
    s += path(f"M2 50H{w - 2}", LINE, 1)
    for x, color in [(28, "#e68d87"), (50, "#e5bf78"), (72, "#a9cf83")]:
        s += circle(x, 26, 6, color)
    s += text(w / 2, 31, "arnab@workbench:~", 16, MUTED, mono=True,
              extra='text-anchor="middle"')
    s += text(w - 24, 31, "bash", 13, MUTED, mono=True, extra='text-anchor="end"')

    s += text(40, 94, "$", 20, LIME, mono=True)
    s += text(66, 94, "whoami", 20, MUTED, mono=True)
    s += text(40, 133, "Arnab Ranjan Sikdar", 30, WHITE, 700)
    s += text(36, 207, "I build across", 64, WHITE, 700, extra='letter-spacing="-2"')
    s += text(36, 277, "the whole stack.", 64, LIME, 700, extra='letter-spacing="-2"')

    s += text(40, 328, "$", 20, LIME, mono=True)
    s += text(66, 328, "cat interests", 20, MUTED, mono=True)
    s += text(40, 364, "firmware / systems / vision / robotics", 21, WHITE, mono=True)
    if mobile:
        s += board(155, 412)
        footer_y = 730
    else:
        s += text(40, 401, "From the first byte to the physical world.", 22, MUTED)
        s += board(800, 126)
        footer_y = 450
        s += text(w - 40, footer_y + 42, "RUST / C++ / PYTHON / EMBEDDED C", 14, MUTED,
                  mono=True, extra='text-anchor="end"')

    s += path(f"M40 {footer_y}H{w - 40}", LINE, 1)
    s += text(40, footer_y + 42, "arnab@workbench:~ $", 20, LIME, mono=True)
    s += rect(270, footer_y + 25, 11, 21, LIME, "none", 1, 'class="cursor"')
    return svg(w, h, "Arnab Ranjan Sikdar — systems engineer",
               "A terminal window introducing Arnab Ranjan Sikdar with whoami and cat interests. "
               "I build across the whole stack: firmware, systems, vision, and robotics.", s)


def main():
    ASSETS.mkdir(exist_ok=True)
    (ROOT / "about_me.svg").write_text(header(), encoding="utf-8")
    (ASSETS / "header-mobile.svg").write_text(header(mobile=True), encoding="utf-8")
    print("Built desktop and mobile headers.")


if __name__ == "__main__":
    main()
