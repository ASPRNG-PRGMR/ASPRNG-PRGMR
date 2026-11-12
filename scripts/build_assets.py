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


def motif(kind, color):
    s = '<g transform="translate(428 45)" stroke-linecap="round" stroke-linejoin="round">'
    if kind == "hashi":
        s += rect(0, 7, 66, 45, BG, color, 4)
        s += path("M33 52V63M18 63H48M66 32H81V60H94", color)
        s += rect(94, 10, 38, 62, BG, color, 5)
        s += path("M101 21H125M101 27H117M8 17H32M8 23H45", color, 1)
        s += circle(113, 64, 2, color)
    elif kind == "kage":
        for i in range(6):
            for j in range(4):
                c = ["#ed8fa0", "#c5f277", "#7caef5"][(i + j) % 3]
                s += rect(i * 22, j * 20, 9, 15, c, "none", 3,
                          f'opacity="{.9 if (i+j)%3 else .45}"')
    elif kind == "senpai":
        s += rect(40, 0, 68, 80, BG, LINE, 5)
        s += rect(22, 10, 68, 80, BG, color, 5)
        for y, length in [(26, 36), (34, 44), (49, 44), (57, 44), (65, 30), (79, 18)]:
            s += path(f"M32 {y}h{length}", color, 2 if y == 26 else 1)
        s += path("M0 38H13M0 48H13M0 58H13", LINE)
    elif kind == "edgecv":
        s += path("M0 24V0H24M102 0H126V24M126 60V84H102M24 84H0V60", color)
        s += rect(29, 16, 66, 52, BG, color, 3)
        s += circle(62, 42, 16, "none", f'stroke="{color}"')
        s += circle(62, 42, 5, color)
        s += path("M62 8V20M62 64V76M17 42H33M91 42H109", color, 1)
    elif kind == "edgerover":
        s += rect(27, 19, 70, 42, BG, color, 7)
        for x in [30, 76]:
            for y in [7, 64]:
                s += rect(x, y, 19, 10, color, "none", 3)
        s += circle(92, 40, 6, color)
        s += path("M109 26Q122 40 109 54M119 17Q140 40 119 63", color, 1)
        s += path("M12 40H0M10 29H4M10 51H4", color, 1)
    elif kind == "bhukavach":
        for i in range(5):
            rx, ry = 16 + i * 12, 8 + i * 7
            s += (f'<ellipse cx="65" cy="42" rx="{rx}" ry="{ry}" transform="rotate(-16 65 42)" '
                  f'fill="none" stroke="{color}" stroke-opacity="{1-i*.14}"/>')
        for x, y in [(14, 16), (100, 12), (118, 60), (34, 74)]:
            s += circle(x, y, 4, color, f'stroke="{BG}" stroke-width="2"')
    return s + '</g>'


PROJECTS = [
    ("hashi", "01 / HARDWARE INTEROP", "HASHI", LIME,
     ["An iPad. A USB cable.", "A real Linux extended display."],
     "PYTHON / C++ / RUST", "HARDWARE-TESTED ALPHA"),
    ("kage", "02 / GRAPHICS RESEARCH", "KAGE", "#8ad8e6",
     ["Text rendering that understands", "the OLED beneath the pixels."],
     "RUST / OPENGL / VULKAN", "RESEARCH SANDBOX"),
    ("senpai", "03 / NATIVE SOFTWARE", "SENPAI", "#c5b3f9",
     ["A native document reader.", "Rust core. Poppler rendering."],
     "RUST / C++ / EGUI", "EARLY DEVELOPMENT"),
    ("edgecv", "04 / EMBEDDED VISION", "EdgeCV", "#8dbbff",
     ["Image classification on an ESP32.", "Camera in. Inference on-device."],
     "ESP32 / TFLITE MICRO", "CLASSIFIER ON HARDWARE"),
    ("edgerover", "05 / ROBOTICS", "EdgeRover", "#f6bb87",
     ["Four wheels. Wireless control.", "Building toward vision following."],
     "ESP32 / ESP-NOW / C++", "BENCH TESTING PENDING"),
    ("bhukavach", "06 / PHYSICAL SENSING", "BhuKavach", "#89dbb7",
     ["A mesh of tilt sensors.", "A picture of the ground moving."],
     "PYTHON / MEMS / TELEMETRY", "SIMULATION VALIDATED"),
]


def card(project):
    slug, category, name, color, lines, stack, status = project
    s = rect(1, 1, 598, 298, BG, LINE, 14)
    s += path("M28 1H140", color, 3)
    s += text(28, 36, category, 15, MUTED, mono=True)
    s += text(26, 96, name, 44, color, 700, extra='letter-spacing="-1"')
    s += motif(slug, color)
    for i, line in enumerate(lines):
        s += text(28, 150 + i * 29, line, 23, WHITE)
    s += circle(33, 210, 3, color)
    s += text(45, 215, status, 16, MUTED, mono=True)
    s += path("M28 238H572", LINE, 1)
    s += text(28, 273, stack, 16, color, mono=True)
    s += path("M551 275L568 258M553 258H568V273", color, 2)
    # Transparent space below each card provides a gutter when GitHub wraps them.
    return svg(600, 316, name, " ".join(lines) + f" {stack}. {status}.", s)


def main():
    ASSETS.mkdir(exist_ok=True)
    (ROOT / "about_me.svg").write_text(header(), encoding="utf-8")
    (ASSETS / "header-mobile.svg").write_text(header(mobile=True), encoding="utf-8")
    for project in PROJECTS:
        (ASSETS / f"{project[0]}.svg").write_text(card(project), encoding="utf-8")
    print("Built desktop and mobile headers + 6 project cards.")


if __name__ == "__main__":
    main()
