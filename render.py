"""Draw the front page of THE WORLD TODAY for Monday, 23 November 2026.

Renders a 1024x1024 newspaper front page with one lead story and six
short news cards, using only Pillow and the DejaVu fonts. Deterministic:
no timestamps, no randomness, no network.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36
PAPER = (247, 243, 232)
INK = (18, 18, 18)
ACCENT = (146, 32, 24)
RULE = (120, 110, 95)
MUTED = (90, 84, 72)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load_font(name, size):
    """Load a DejaVu font, falling back to PIL's default font."""
    path = os.path.join(FONT_DIR, name)
    try:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()


SERIF = "DejaVuSerif-Bold.ttf"
SERIF_REG = "DejaVuSerif.ttf"
SANS = "DejaVuSans.ttf"
SANS_BOLD = "DejaVuSans-Bold.ttf"

LEAD_HEADLINE = "EU proposes sweeping Russia sanctions"
LEAD_KICKER = "EUROPE  |  SANCTIONS  |  LEAD STORY"
LEAD_BODY = (
    "The European Commission proposes its 22nd sanctions package against "
    "Russia: about 60 Russian banks cut from SWIFT, curbs on crypto "
    "platforms and payment networks including in third countries, more "
    "than 70 further shadow-fleet vessels listed, a ban on tankers "
    "insured in Russia from EU ports, and a ban on Russian teams and "
    "athletes competing under the Russian flag at EU events. It is a "
    "proposal: it needs unanimous approval by all 27 EU member states "
    "before it takes effect."
)
LEAD_SOURCE = "European Commission / AP  —  23 Nov"

CARDS = [
    {
        "kicker": "MIDDLE EAST",
        "headline": "Iran vows \u201call means\u201d against US blockade",
        "body": (
            "Iran vows to use \u201call means\u201d against the US naval "
            "blockade of the Strait of Hormuz, calling it military "
            "aggression. UKMTO confirmed three tanker attacks near "
            "Khasab, Oman, on 20\u201321 Nov; Iran claims two more "
            "supertankers hit mines on 22 Nov \u2014 unverified."
        ),
        "source": "Reuters / UKMTO",
    },
    {
        "kicker": "EUROPE",
        "headline": "Moscow warns Estonia; Finland summons envoy",
        "body": (
            "Russia warns Estonia\u2019s plan to close the border risks "
            "open war. Finland summons Russia\u2019s ambassador over a "
            "suspected airspace violation by a helicopter, and a "
            "Ukrainian drone strike on the Russian cargo ship Sparta II "
            "in the Gulf of Finland."
        ),
        "source": "Daily Summary of World  —  23 Nov",
    },
    {
        "kicker": "LIBYA",
        "headline": "Sea drones sink Russian corvette off Libya",
        "body": (
            "Suspected Ukrainian naval drones hit the Russian corvette "
            "Merkury at the Benghazi naval base, Libya, on Sunday. "
            "Libyan officials say she was badly damaged and then sank, "
            "10 injured. Kyiv and Moscow have not confirmed it."
        ),
        "source": "AP / Reuters",
    },
    {
        "kicker": "UKRAINE",
        "headline": "Russian drones hit flats near Kyiv",
        "body": (
            "Russian drones struck a five-storey apartment block in Dymer, "
            "north of Kyiv, early Sunday: 2 killed, 11 missing including "
            "2 children."
        ),
        "source": "Al Jazeera / AP",
    },
    {
        "kicker": "TRADE",
        "headline": "EU and Indonesia sign trade deal",
        "body": (
            "The EU and Indonesia sign a trade and investment deal after "
            "a decade of talks; a combined market of 730 million people."
        ),
        "source": "23 Nov reports",
    },
    {
        "kicker": "SCIENCE",
        "headline": "BepiColombo enters Mercury orbit",
        "body": (
            "After an eight-year journey, the Europe\u2013Japan BepiColombo "
            "probe entered orbit around Mercury on 21 Nov \u2014 only the "
            "second mission ever to do so."
        ),
        "source": "ESA / JAXA",
    },
]


def wrap(draw, text, font, width):
    """Greedy word wrap; returns a list of lines fitting inside width."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        line = words[0]
        for word in words[1:]:
            trial = line + " " + word
            if draw.textlength(trial, font=font) <= width:
                line = trial
            else:
                lines.append(line)
                line = word
        lines.append(line)
    return lines


def text_block(draw, x, y, text, font, fill, width, leading):
    """Draw wrapped text; returns the y just below the last line."""
    for line in wrap(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def draw_card(draw, x, y, w, h, card):
    """Draw one news card inside the box (x, y, w, h)."""
    draw.rectangle([x, y, x + w, y + h], outline=RULE, width=1)
    pad = 13
    cx = x + pad
    cw = w - 2 * pad
    cy = y + 9
    kicker_font = load_font(SANS_BOLD, 15)
    head_font = load_font(SERIF, 21)
    body_font = load_font(SANS, 13)
    src_font = load_font(SANS, 13)
    draw.text((cx, cy), card["kicker"], font=kicker_font, fill=ACCENT)
    cy += 22
    cy = text_block(draw, cx, cy, card["headline"], head_font, INK, cw, 25)
    cy += 3
    # Never let the body run past the source line at the bottom.
    max_lines = max(1, (y + h - 25 - cy) // 17)
    lines = wrap(draw, card["body"], body_font, cw)[:max_lines]
    for line in lines:
        draw.text((cx, cy), line, font=body_font, fill=INK)
        cy += 17
    draw.text((cx, y + h - 23), card["source"], font=src_font, fill=MUTED)


def render():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Masthead
    mast_font = load_font(SERIF, 56)
    title = "THE WORLD TODAY"
    tw = draw.textlength(title, font=mast_font)
    draw.text(((W - tw) / 2, 16), title, font=mast_font, fill=INK)
    draw.line([(MARGIN, 90), (W - MARGIN, 90)], fill=INK, width=3)
    date_font = load_font(SERIF_REG, 23)
    date = "Monday, 23 November 2026"
    dw = draw.textlength(date, font=date_font)
    draw.text(((W - dw) / 2, 98), date, font=date_font, fill=INK)
    draw.line([(MARGIN, 132), (W - MARGIN, 132)], fill=INK, width=1)

    # Lead story
    lx, ly = MARGIN, 146
    lw = W - 2 * MARGIN
    kicker_font = load_font(SANS_BOLD, 18)
    draw.text((lx, ly), LEAD_KICKER, font=kicker_font, fill=ACCENT)
    head_font = load_font(SERIF, 40)
    hy = text_block(draw, lx, ly + 28, LEAD_HEADLINE, head_font, INK, lw, 46)
    body_font = load_font(SANS, 17)
    by = text_block(draw, lx, hy + 6, LEAD_BODY, body_font, INK, lw, 22)
    src_font = load_font(SANS, 14)
    draw.text((lx, by + 5), LEAD_SOURCE, font=src_font, fill=MUTED)
    rule_y = by + 26
    draw.line([(MARGIN, rule_y), (W - MARGIN, rule_y)], fill=INK, width=2)

    # Card grid: 2 columns x 3 rows
    gap = 14
    cw = (W - 2 * MARGIN - gap) // 2
    grid_top = rule_y + 14
    grid_bottom = H - 38
    ch = (grid_bottom - grid_top - 2 * gap) // 3
    for i, card in enumerate(CARDS):
        col = i % 2
        row = i // 2
        x = MARGIN + col * (cw + gap)
        y = grid_top + row * (ch + gap)
        draw_card(draw, x, y, cw, ch, card)

    # Footer
    foot_font = load_font(SERIF_REG, 17)
    foot = "THE WORLD TODAY  —  23 November 2026"
    fw = draw.textlength(foot, font=foot_font)
    draw.text(((W - fw) / 2, H - 30), foot, font=foot_font, fill=MUTED)
    return img


if __name__ == "__main__":
    render().save("entry.png")
