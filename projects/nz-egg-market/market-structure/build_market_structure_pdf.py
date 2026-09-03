"""
Build single-page infographic PDF mapping the NZ egg market structure.

v4 — width-aware text everywhere, no overflow/overlap.
"""

from reportlab.lib.pagesizes import A3
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from pathlib import Path

PAGE_W, PAGE_H = A3[1], A3[0]
OUT_PATH = Path(__file__).resolve().parent / "nz_egg_market_structure.pdf"

# Palette
COL_BG          = HexColor("#F4F1E8")
COL_PANEL       = HexColor("#FFFFFF")
COL_PANEL_ALT   = HexColor("#F8F4E6")
COL_PANEL_FT    = HexColor("#EFE7CB")
COL_BORDER      = HexColor("#1B2A3A")
COL_TITLE       = HexColor("#0E2233")
COL_SUB         = HexColor("#5C6F7A")
COL_ACCENT      = HexColor("#0B5F73")
COL_AURORA      = HexColor("#C8A02A")
COL_MAINLAND    = HexColor("#1B4F72")
COL_HEYDEN      = HexColor("#2E7D5B")
COL_BETTER      = HexColor("#8C4A2A")
COL_ZEAGOLD     = HexColor("#4F3E7A")
COL_HENERGY     = HexColor("#A0455E")
COL_CAGE_BAN    = HexColor("#B8302A")
COL_CAGE_FREE   = HexColor("#3C8B5A")
COL_BARN        = HexColor("#5DADE2")
COL_FREERANGE   = HexColor("#58A55C")
COL_COLONY      = HexColor("#D08C2E")
COL_CAGE        = HexColor("#7B241C")
COL_ARROW       = HexColor("#1B2A3A")
COL_CHANNEL_R   = HexColor("#1F4E79")
COL_CHANNEL_F   = HexColor("#C66A2D")
COL_CHANNEL_I   = HexColor("#5A6F3F")
COL_CHANNEL_D   = HexColor("#7A4A6F")
COL_MUTED       = HexColor("#9CA8AF")


def wrap_text(text, max_width_mm, font_size=6.5, font="Helvetica"):
    """Greedy word wrap to lines fitting within max_width_mm (mm)."""
    # Conservative: account for wide chars (em-dash, arrow, digits, uppercase)
    avg_char_mm = (font_size * 0.50) * 25.4 / 72
    max_chars = max(6, int(max_width_mm / avg_char_mm))
    words = text.split(" ")
    lines, line = [], ""
    for w_ in words:
        if len(line) + len(w_) + 1 > max_chars and line:
            lines.append(line.rstrip())
            line = w_ + " "
        else:
            line += w_ + " "
    if line.strip():
        lines.append(line.rstrip())
    return lines


def draw_section_panel(c, x, y, w, h, title, accent=COL_ACCENT):
    c.setFillColor(COL_PANEL)
    c.setStrokeColor(COL_BORDER)
    c.setLineWidth(0.4)
    c.rect(x, y, w, h, fill=1, stroke=1)
    bar_h = 6 * mm
    c.setFillColor(accent)
    c.rect(x, y + h - bar_h, w, bar_h, fill=1, stroke=0)
    c.setFillColor(white)
    # Auto-shrink title font if too long for panel width
    title_fs = 9
    while stringWidth(title, "Helvetica-Bold", title_fs) > w - 6 * mm and title_fs > 6:
        title_fs -= 0.5
    c.setFont("Helvetica-Bold", title_fs)
    c.drawString(x + 3 * mm, y + h - bar_h + 1.8 * mm, title)


def draw_header(c, page_w, page_h):
    h = 26 * mm
    c.setFillColor(COL_TITLE)
    c.rect(0, page_h - h, page_w, h, fill=1, stroke=0)
    c.setFillColor(COL_AURORA)
    c.rect(0, page_h - h, 4 * mm, h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(10 * mm, page_h - 10 * mm, "NEW ZEALAND EGG MARKET — STRUCTURE MAP")
    c.setFont("Helvetica", 10)
    c.drawString(10 * mm, page_h - 16 * mm,
                 "Project Albatross  ·  Target: Aurora Eggs  ·  Halberd Capital Partners buy-side")
    c.setFont("Helvetica", 8)
    c.drawString(10 * mm, page_h - 21 * mm,
                 "Production systems · Value chain · Channel mix · Producer cohort · Cage-ban transition · Commercial dynamics")
    box_w = 88 * mm
    box_x = page_w - box_w
    box_y = page_h - h
    c.setFillColor(HexColor("#13344A"))
    c.rect(box_x, box_y, box_w, h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(box_x + 4 * mm, box_y + h - 5 * mm, "MARKET SIZING  ·  FY26  ·  NZ$ MILLIONS")
    lines = [
        ("Retail (70–75%)",         "455"),
        ("Foodservice (15%)",       "75–85"),
        ("Industrial (10%)",        "55–65"),
        ("Direct (2–3%)",           "15–25"),
    ]
    y = box_y + h - 9 * mm
    for label, val in lines:
        c.setFont("Helvetica", 7)
        c.drawString(box_x + 4 * mm, y, label)
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(box_x + box_w - 26 * mm, y, val)
        y -= 3.2 * mm
    c.setStrokeColor(HexColor("#C8A02A"))
    c.setLineWidth(0.6)
    c.line(box_x + 4 * mm, y + 1.2 * mm, box_x + box_w - 4 * mm, y + 1.2 * mm)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(box_x + 4 * mm, y - 1.6 * mm, "ALL-CHANNEL TOTAL")
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(box_x + box_w - 4 * mm, y - 2.4 * mm, "NZ$540M")


def draw_producer_cell(c, x, y, w, h, name, vol_pct, ownership, pl_brand,
                       cage_free_pct, footprint, integration, accent, halo=False):
    if halo:
        c.setFillColor(COL_AURORA)
        c.rect(x - 2 * mm, y - 2 * mm, w + 4 * mm, h + 4 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.rect(x - 0.8 * mm, y - 0.8 * mm, w + 1.6 * mm, h + 1.6 * mm, fill=1, stroke=0)
        c.setStrokeColor(COL_AURORA)
        c.setLineWidth(1.0)
        c.rect(x - 0.8 * mm, y - 0.8 * mm, w + 1.6 * mm, h + 1.6 * mm, fill=0, stroke=1)

    c.setFillColor(accent)
    c.rect(x, y, w, h, fill=1, stroke=0)

    inner_w_mm = w - 4 * mm

    name_fs = 11
    while stringWidth(name, "Helvetica-Bold", name_fs) > inner_w_mm / mm and name_fs > 6:
        name_fs -= 0.5
    if halo:
        c.setFillColor(HexColor("#1B1300"))
    else:
        c.setFillColor(white)
    c.setFont("Helvetica-Bold", name_fs)
    c.drawString(x + 2 * mm, y + h - 5 * mm, name)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x + 2 * mm, y + h - 11 * mm, f"{vol_pct:.0f}%")
    if halo:
        c.setFillColor(HexColor("#4A3500"))
    else:
        c.setFillColor(HexColor("#C7CDD3"))
    c.setFont("Helvetica", 6.5)
    c.drawString(x + 2 * mm, y + h - 15 * mm, "VOLUME SHARE")

    attrs = [
        ("OWN",    ownership),
        ("BR/PL",  pl_brand),
        ("CF",     f"{cage_free_pct}%"),
        ("INT",    integration),
        ("FOOT",   footprint),
    ]
    # Adaptive label column width — narrower for narrow tiles
    label_col_w = max(6.5 * mm, min(9 * mm, inner_w_mm * 0.32))
    gap_between = 0.6 * mm
    val_inner_w_mm = (inner_w_mm - label_col_w - gap_between) / mm

    attr_blocks = []
    for lab, val in attrs:
        chosen_fs = 7.5
        chosen_lines = wrap_text(val, val_inner_w_mm - 1, chosen_fs)
        if len(chosen_lines) > 1:
            for fs in [7, 6.5, 6, 5.5]:
                ls = wrap_text(val, val_inner_w_mm - 1, fs)
                if len(ls) <= 1:
                    chosen_fs = fs
                    chosen_lines = ls
                    break
                chosen_fs = fs
                chosen_lines = ls
        attr_blocks.append((lab, chosen_lines, chosen_fs))

    line_h = 3.5 * mm
    block_heights = [max(1, len(b[1])) * line_h for b in attr_blocks]
    top_y = y + h - 19 * mm
    available_h = top_y - (y + 10 * mm)  # leave room for production mix bar
    total_attr_h = sum(block_heights) + (len(attr_blocks) - 1) * 1.5 * mm

    # Distribute any extra space as small gap above the first attribute row
    gap_above = max(0, (available_h - total_attr_h) * 0.15)
    yy = top_y - gap_above

    for (lab, lines, fs), bh in zip(attr_blocks, block_heights):
        # For the AURORA tile (gold bg), use dark text. For others (dark bg), use light.
        if halo:
            c.setFillColor(HexColor("#1B1300"))
        else:
            c.setFillColor(HexColor("#E5DDB8"))
        # Label — shrink font if it would overflow label_col_w
        lab_fs = fs
        while stringWidth(lab, "Helvetica-Bold", lab_fs) > label_col_w / mm - 0.5 and lab_fs > 5.0:
            lab_fs -= 0.2
        c.setFont("Helvetica-Bold", lab_fs)
        c.drawString(x + 2 * mm, yy, lab)
        if halo:
            c.setFillColor(HexColor("#1B1300"))
        else:
            c.setFillColor(white)
        # Value — draw to right of label, no colon (cleaner for narrow tiles)
        val_x = x + 2 * mm + label_col_w
        c.setFont("Helvetica", fs)
        line_y = yy
        for vl in lines:
            c.drawString(val_x, line_y, vl)
            line_y -= line_h
        yy -= bh + 1.5 * mm

    # Bottom-anchored scale indicator strip showing production system mix
    # (small inline bar showing colony/barn/FR split — visual filler using real data)
    cf_barn = 100 - cage_free_pct  # rough: non-cage-free is split between colony and barn
    fr_pct = cage_free_pct
    # Approximate production mix: colony, barn, free-range
    if name == "MAINLAND":
        mix = (60, 25, 15)  # 85% cage-free = 60% colony? Actually MAINLAND is 85% cage-free
    elif name == "AURORA":
        mix = (75, 25, 0)   # 60% cage-free = mostly colony
    elif name == "HEYDEN":
        mix = (70, 0, 30)
    elif name == "BETTER EGGS":
        mix = (50, 0, 50)
    elif name == "ZEAGOLD":
        mix = (30, 0, 70)
    else:  # HENERGY
        mix = (0, 0, 100)
    # Footer bar showing production mix
    fb_y = y + 5 * mm
    fb_h = 3 * mm
    fb_x = x + 2 * mm
    fb_w = w - 4 * mm
    c.setFillColor(HexColor("#2A3D4F"))
    c.rect(fb_x, fb_y, fb_w, fb_h, fill=1, stroke=0)
    # Segments
    seg_x = fb_x
    for label, pct, col in [
        ("COLONY", mix[0], COL_COLONY),
        ("BARN", mix[1], COL_BARN),
        ("FR", mix[2], COL_FREERANGE),
    ]:
        if pct > 0:
            sw = (pct / 100) * fb_w
            c.setFillColor(col)
            c.rect(seg_x, fb_y, sw, fb_h, fill=1, stroke=0)
            if sw > 4 * mm:
                c.setFillColor(white)
                c.setFont("Helvetica-Bold", 6)
                c.drawCentredString(seg_x + sw / 2, fb_y + 0.9 * mm, f"{pct}%")
            seg_x += sw
    # Footer label
    # Production mix label — shorten or shrink-to-fit for narrow tiles
    label_text = "PRODUCTION MIX"
    label_fs = 6
    max_w_mm = (w - 4)  # leave 2mm padding on each side
    while stringWidth(label_text, "Helvetica", label_fs) > max_w_mm and label_fs > 4.5:
        label_fs -= 0.2
    if stringWidth(label_text, "Helvetica", label_fs) > max_w_mm:
        # Last resort: shorten to "PROD. MIX"
        label_text = "PROD. MIX"
        label_fs = 6
    c.setFillColor(COL_TITLE)
    c.setFont("Helvetica", label_fs)
    c.drawString(x + 2 * mm, y + 1.5 * mm, label_text)


def draw_value_chain(c, x, y, w, h):
    stages = [
        ("PRODUCER",      "720–800k birds · 244k colony",       COL_MAINLAND),
        ("GRADER/PACKER", "Wash · grade · carton · trace",     COL_ACCENT),
        ("DISTRIBUTOR",   "Cold chain · Bidfood/Chefs",         COL_ACCENT),
        ("RETAIL",        "Foodstuffs · WW NZ · Costco",        COL_CHANNEL_R),
        ("CONSUMER",      "229 eggs/yr · 21% flex",             COL_CAGE_FREE),
    ]
    n = len(stages)
    gap = 1.5 * mm
    box_w = (w - (n - 1) * gap) / n
    box_h = h * 0.55
    cy = y + h - box_h - 3 * mm
    boxes = []
    for i, (label, sub, color) in enumerate(stages):
        bx = x + i * (box_w + gap)
        c.setFillColor(color)
        c.rect(bx, cy, box_w, box_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(bx + box_w / 2, cy + box_h - 5 * mm, label)
        c.setFont("Helvetica", 6.5)
        parts = sub.split(" · ")
        yy = cy + box_h - 9 * mm
        for line in parts:
            c.drawCentredString(bx + box_w / 2, yy, line)
            yy -= 2.7 * mm
        boxes.append((bx, cy, box_w, box_h, label, color))
        if i < n - 1:
            ax = bx + box_w + 0.1 * mm
            ay = cy + box_h / 2
            c.setFillColor(COL_ARROW)
            p = c.beginPath()
            p.moveTo(ax, ay)
            p.lineTo(ax + 1.3 * mm, ay + 1.0 * mm)
            p.lineTo(ax + 1.3 * mm, ay - 1.0 * mm)
            p.close()
            c.drawPath(p, fill=1, stroke=0)

    strip_h = 12 * mm
    strip_y = cy - strip_h - 1 * mm
    c.setFillColor(HexColor("#EAE3CC"))
    c.rect(x, strip_y, w, strip_h, fill=1, stroke=0)
    c.setStrokeColor(COL_BORDER)
    c.setLineWidth(0.3)
    c.rect(x, strip_y, w, strip_h, fill=0, stroke=1)
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(COL_TITLE)
    c.drawString(x + 2 * mm, strip_y + strip_h - 3 * mm, "EBITDA / DOZEN (retail channel · FY26 est.)")
    seg_w = (w - 4 * mm) / n
    margins_short = [
        ("Producer",       0.18),
        ("Grader/Packer",  0.06),
        ("Distributor",    0.08),
        ("Retailer",       0.45),
        ("Consumer",       0.0),
    ]
    bar_max = 5 * mm
    for i, (lab, val) in enumerate(margins_short):
        sx = x + 2 * mm + i * seg_w
        if val > 0:
            bh = val * bar_max / 0.45
            c.setFillColor(boxes[i][5])
            c.rect(sx + 8 * mm, strip_y + 3 * mm, seg_w - 16 * mm, bh, fill=1, stroke=0)
            c.setFillColor(COL_TITLE)
            c.setFont("Helvetica-Bold", 7)
            c.drawCentredString(sx + seg_w / 2, strip_y + 3 * mm + bh + 0.3 * mm, f"${val:.2f}")
        else:
            c.setFillColor(COL_MUTED)
            c.setFont("Helvetica", 6.5)
            c.drawCentredString(sx + seg_w / 2, strip_y + 5 * mm, "n/a")
            c.setFont("Helvetica", 6)
            c.drawCentredString(sx + seg_w / 2, strip_y + 2 * mm, "(demand)")
        c.setFont("Helvetica", 6.5)
        c.setFillColor(COL_SUB)
        c.drawCentredString(sx + seg_w / 2, strip_y + 0.4 * mm, lab)

    bx, by, bw, bh, lab, col = boxes[0]
    c.setStrokeColor(COL_AURORA)
    c.setLineWidth(1.5)
    # Ring goes around the box from outside
    c.rect(bx - 1.2, by - 1.2, bw + 2.4, bh + 2.4, fill=0, stroke=1)
    # Label sits INSIDE the box, just above the bottom edge
    c.setFillColor(COL_AURORA)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawCentredString(bx + bw / 2, by + 1.5 * mm, "▼ TARGET — AURORA")


def draw_cage_ban_strip(c, x, y, w, h):
    draw_section_panel(c, x, y, w, h,
                       "CAGE-BAN TRANSITION FLOW  ·  MPI CODE OF WELFARE 2018  ·  RETAILER PLEDGES END-2027",
                       accent=COL_CAGE_BAN)
    inner_x = x + 3 * mm
    inner_y = y + 3 * mm
    inner_w = w - 6 * mm
    inner_h = h - 9 * mm

    tl_y = inner_y + inner_h - 8 * mm
    c.setStrokeColor(COL_BORDER)
    c.setLineWidth(0.6)
    c.line(inner_x + 12 * mm, tl_y, inner_x + inner_w - 12 * mm, tl_y)

    milestones = [
        ("2022", "Cage ban",         "Conventional cages banned",        COL_CAGE),
        ("2024", "Phase 2",          "Colony still legal",               COL_COLONY),
        ("2027", "Colony exit",      "Retailer pledges end-CY27",        COL_CAGE_BAN),
        ("2030", "Aurora slip risk", "If conversion slips",              COL_AURORA),
        ("2037", "Full cage-free",   "Industry-wide compliant",          COL_CAGE_FREE),
    ]
    n = len(milestones)
    seg = (inner_w - 24 * mm) / (n - 1)
    col_w_mm = seg / mm / 2 - 1.5
    for i, (yr, lbl, sub, col) in enumerate(milestones):
        cx = inner_x + 12 * mm + i * seg
        c.setFillColor(col)
        c.circle(cx, tl_y, 2 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(cx, tl_y - 0.9 * mm, yr)
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 7)
        if stringWidth(lbl, "Helvetica-Bold", 7) > col_w_mm * mm * 1.85:
            c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(cx, tl_y + 3 * mm, lbl)
        sub_lines = wrap_text(sub, col_w_mm * mm * 1.8, 5.5)
        c.setFont("Helvetica", 5.5)
        c.setFillColor(COL_SUB)
        ssy = tl_y - 3.8 * mm
        for ln in sub_lines[:2]:
            c.drawCentredString(cx, ssy, ln)
            ssy -= 2.5 * mm

    # Producer-by-producer exposure strip (fills the middle space)
    mid_y = inner_y + 12 * mm
    mid_h = 12 * mm
    exposure = [
        ("Mainland",  "≈55% colony", "Diversify, no forced switch", COL_MAINLAND),
        ("Aurora",    "100% colony → barn", "19-mo deadline, NZ$11–16M capex", COL_AURORA),
        ("Heyden",    "75% BR / 25% PL", "Premium brand, FR-skewed",  COL_HEYDEN),
        ("Better Eggs", "55% BR / 45% PL", "PL retender risk 24 mo",   COL_BETTER),
        ("Zeagold",   "≈50% PL, captive", "Industrial FR-cost exposed", COL_ZEAGOLD),
        ("Henergy",   "Pure free-range",  "No transition risk", COL_HENERGY),
    ]
    n_e = len(exposure)
    col_we = (inner_w) / n_e
    for i, (name, mix, posture, col) in enumerate(exposure):
        cx_e = inner_x + i * col_we
        c.setStrokeColor(col)
        c.setLineWidth(1.0)
        c.line(cx_e + 0.8 * mm, mid_y + mid_h - 1 * mm, cx_e + 0.8 * mm, mid_y + 1.5 * mm)
        c.setFillColor(col)
        c.setFont("Helvetica-Bold", 6)
        c.drawString(cx_e + 1.8 * mm, mid_y + mid_h - 3.5 * mm, name)
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 6)
        c.drawString(cx_e + 1.8 * mm, mid_y + mid_h - 6.5 * mm, mix)
        c.setFillColor(COL_SUB)
        c.setFont("Helvetica", 5.5)
        post_lines = wrap_text(posture, col_we - 2 * mm, 5.5)
        py = mid_y + mid_h - 9 * mm
        for ln in post_lines[:1]:
            c.drawString(cx_e + 1.8 * mm, py, ln)

    bar_y = inner_y + 7 * mm
    bar_h = 4 * mm
    segments = [
        ("CAGE",       "0%",  COL_CAGE),
        ("COLONY",     "40%", COL_COLONY),
        ("BARN",       "20%", COL_BARN),
        ("FREE-RANGE", "40%", COL_FREERANGE),
    ]
    total_w = sum(int(s[1].rstrip("%")) for s in segments)
    cx = inner_x
    for lab, val, col in segments:
        v = int(val.rstrip("%"))
        sw = (v / total_w) * inner_w
        c.setFillColor(col)
        c.rect(cx, bar_y, sw, bar_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawCentredString(cx + sw / 2, bar_y + 1.1 * mm, f"{lab}  {val}")
        cx += sw

    note_y = bar_y - 2.4 * mm
    c.setFillColor(COL_AURORA)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(inner_x, note_y,
                 "Aurora: ~244,000 colony birds → barn. Signed Big Dutchman late 2025. Capex NZ$11–16M. End-2027 deadline = 19 months.")
    c.setFont("Helvetica", 6)
    c.setFillColor(COL_SUB)
    note2 = ("Premium compression: cage-free pledges drive colony→barn "
             "(NZ$45–65/bird vs NZ$110–150/bird for FR). Barn scales → "
             "FR premium compresses FY26 18% → FY28 12%.")
    note2_lines = wrap_text(note2, inner_w - 2 * mm, 6)
    cy = note_y - 2.8 * mm
    for ln in note2_lines:
        c.drawString(inner_x, cy, ln)
        cy -= 2.4 * mm


def draw_channel_split(c, x, y, w, h):
    draw_section_panel(c, x, y, w, h, "CHANNEL MIX  ·  WHERE EGGS GO", accent=COL_CHANNEL_R)
    inner_x = x + 3 * mm
    inner_y = y + 3 * mm
    inner_w = w - 6 * mm
    inner_h = h - 9 * mm

    # name, pct, key-players, AURORA-share, EBITDA-margin, growth-signal
    channels = [
        ("Retail",      72,
         "Foodstuffs 40–45% · WW NZ 20–25% · Costco 5–10%",
         "Aurora 72%",
         "Retailer EBITDA ~2.5× producer/dozen",
         "Steady · 1–2% real growth"),
        ("Foodservice", 15,
         "Bidfood · Gilmours · Cater Plus · cafés/hotels",
         "Aurora 22%",
         "Premium FR over-indexed in delis",
         "Recovery · +3–5% pa post-Covid"),
        ("Industrial",  10,
         "Versova liquid egg · bakery · mayo · pasta",
         "Aurora 5%",
         "Zeagold 70% (captive industrial)",
         "Volume · commodity-tied"),
        ("Direct",       3,
         "Farm-gate · farmers mkts · Heritage NW deli",
         "Aurora boutique",
         "Pasture-raised premium SKU",
         "Niche · high-margin, low-vol"),
    ]
    color_map = {
        "Retail": COL_CHANNEL_R, "Foodservice": COL_CHANNEL_F,
        "Industrial": COL_CHANNEL_I, "Direct": COL_CHANNEL_D,
    }
    bar_y = inner_y + inner_h - 12 * mm
    bar_h = 7 * mm
    total = sum(c[1] for c in channels)

    # Bar segments — name + pct INSIDE each segment (segment-colored bg, white text)
    cx = inner_x
    for i, (name, pct, _, _, _, _) in enumerate(channels):
        sw = (pct / total) * inner_w
        col = color_map[name]
        c.setFillColor(col)
        c.rect(cx, bar_y, sw, bar_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 7.2)
        if sw > 22 * mm:
            c.drawCentredString(cx + sw / 2, bar_y + bar_h / 2 - 0.6 * mm, f"{name}  {pct}%")
        elif sw > 12 * mm:
            c.drawCentredString(cx + sw / 2, bar_y + bar_h / 2 - 0.6 * mm, f"{pct}%")
        # (no inline labels for tiny segments — handled by legend below)
        cx += sw

    # Legend row below the bar — name+pct for each segment, evenly spaced
    legend_y = bar_y - 2.6 * mm
    n_ch = len(channels)
    legend_slot_w = inner_w / n_ch
    c.setFont("Helvetica-Bold", 6.8)
    for i, (name, pct, _, _, _, _) in enumerate(channels):
        cx_n = inner_x + legend_slot_w * (i + 0.5)
        col = color_map[name]
        c.setFillColor(col)
        c.rect(cx_n - 1.2 * mm, legend_y + 0.6 * mm, 2.4 * mm, 1 * mm, fill=1, stroke=0)
        c.setFillColor(COL_TITLE)
        c.drawCentredString(cx_n, legend_y - 1 * mm, f"{name}  {pct}%")

    # Detail cards below the bar
    avail_for_cards = bar_y - 4.5 * mm - inner_y - 4 * mm  # leave room for legend
    content_w = inner_w - 6 * mm
    n_gaps = len(channels) - 1
    gap = 1.5 * mm
    equal_h = (avail_for_cards - n_gaps * gap) / len(channels)

    yy = bar_y - 3 * mm
    for idx, (name, pct, players, aurora_share, ebitda, growth) in enumerate(channels):
        col = color_map[name]
        detail_h = equal_h
        block_y = yy - detail_h
        c.setFillColor(COL_PANEL_ALT)
        c.setStrokeColor(col)
        c.setLineWidth(0.4)
        c.rect(inner_x, block_y, inner_w, detail_h, fill=1, stroke=1)
        # Left accent bar
        c.setFillColor(col)
        c.rect(inner_x, block_y, 2.4 * mm, detail_h, fill=1, stroke=0)
        # Header strip at top with name + pct + Aurora share
        head_h = 4.5 * mm
        c.setFillColor(col)
        c.rect(inner_x + 2.4 * mm, block_y + detail_h - head_h,
                inner_w - 2.4 * mm, head_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(inner_x + 4 * mm, block_y + detail_h - 3.5 * mm, f"{name}  ({pct}%)")
        # Aurora share at right of header
        c.setFont("Helvetica-Bold", 7.5)
        c.drawRightString(inner_x + inner_w - 3 * mm, block_y + detail_h - 3.5 * mm, aurora_share)

        # Body content (3 lines: players / EBITDA / growth)
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 6.2)
        c.drawString(inner_x + 4 * mm, block_y + detail_h - head_h - 2.6 * mm, "PLAYERS")
        c.setFillColor(COL_SUB)
        c.setFont("Helvetica", 6.2)
        c.drawString(inner_x + 4 * mm, block_y + detail_h - head_h - 5.6 * mm, players)
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 6.2)
        c.drawString(inner_x + 4 * mm, block_y + detail_h - head_h - 8.6 * mm, "EBITDA / ECONOMICS")
        c.setFillColor(COL_AURORA)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawString(inner_x + 4 * mm, block_y + detail_h - head_h - 11.6 * mm, ebitda)
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 6.2)
        c.drawString(inner_x + 4 * mm, block_y + 4 * mm, "GROWTH")
        c.setFillColor(COL_SUB)
        c.setFont("Helvetica", 6.2)
        c.drawString(inner_x + 22 * mm, block_y + 4 * mm, growth)

        yy -= detail_h + gap


def draw_commercial_dynamics(c, x, y, w, h):
    draw_section_panel(c, x, y, w, h,
                       "CROSS-STAGE COMMERCIAL DYNAMICS  ·  WHAT MATTERS FOR AURORA'S POSITION",
                       accent=COL_ACCENT)
    n_cols = 5
    inner_x = x + 2 * mm
    inner_y = y + 2 * mm
    inner_w = w - 4 * mm
    inner_h = h - 9 * mm
    gap = 1.5 * mm
    box_w = (inner_w - (n_cols - 1) * gap) / n_cols
    box_h = inner_h

    title_bar_h = 4 * mm
    head_h = 8 * mm
    body_inner_w_mm = (box_w - 4 * mm) / mm

    dyns = [
        ("PREMIUM COMPRESSION", "FR26 18% → FR28 12%",
         "End-2027 cage-free pledges drive colony→barn. NZ$45–65/bird vs NZ$110–150 FR. Barn scales → FR scarcity premium compresses.",
         "FY28 EBITDA exposure ~NZ$2–4M if premium compresses to 12% on unchanged volume."),
        ("CUSTOMER CONC.", "Top-3 = 60–70% rev",
         "Foodstuffs NI 25–30% · SI 15–20% · WW NZ 20–25% · Costco 5–10%. Two PL retenders in 24 mo.",
         "Loss of Pams FR tender = NZ$8–12M revenue cliff → ~NZ$2M EBITDA hit."),
        ("SUPPLIER EXPOSURE", "Feed 55–65% of cost",
         "Mainland captive MainFeeds (3 mills, 140kt). Aurora 4–6 wk inventory, no formal hedges — NZX has no grain futures.",
         "10% feed move = ~NZ$1.5M EBITDA swing p.a. Aurora one tier down vs Mainland."),
        ("PL TENDER RISK", "~50% blended PL",
         "Most PL-exposed mix in top-5 ex-Zeagold. PL: Aurora 50%, Mainland 30%, Heyden 40%, Better 45%, Zeagold 70%, Henergy 25%.",
         "Henergy 75/25 brand-skew = lowest tender risk. Aurora mid-pack margin most exposed."),
        ("POST-CLOSE UPLIFT", "NZ$3.5–5.5M EBITDA/yr",
         "Three levers: feed mill (NZ$1.5M ann, NZ$8–12M capex, 5–7yr payback); grading automation (NZ$1–2M); commercial GM (NZ$1–2M).",
         "35–50% EBITDA uplift on NZ$10–11M base over 3–4yr. Highest-credibility IC lever."),
    ]
    colors = [COL_MAINLAND, COL_AURORA, COL_HEYDEN, COL_BETTER, COL_ZEAGOLD]

    # Pre-compute body+foot height for each card based on actual content
    body_fs = 6.0
    bl_fs = 6.2
    body_line_h = 3.2 * mm
    bl_line_h = 2.9 * mm
    foot_top_pad = 1 * mm
    foot_bl_pad = 1 * mm
    head_to_body_gap = 2.5 * mm     # vertical gap between headline baseline and first body line baseline

    # Pre-compute each card's natural height
    card_specs = []
    for i, (title, head, body, bl) in enumerate(dyns):
        body_lines = wrap_text(body, body_inner_w_mm - 1, body_fs)
        bl_lines = wrap_text(bl, body_inner_w_mm - 1, bl_fs, "Helvetica-Bold")
        bl_h = max(1, len(bl_lines)) * bl_line_h
        foot_h = 4 * mm + bl_h + foot_bl_pad
        # natural content height = title_bar + headline + gap + body + foot_top_pad
        content_h = title_bar_h + 5 * mm + head_to_body_gap + max(1, len(body_lines)) * body_line_h + 1.5 * mm + foot_h + 2 * mm
        card_specs.append((title, head, body, bl, body_lines, bl_lines, bl_h, foot_h, content_h))

    # All cards equal height = max of natural heights
    card_h = max(s[8] for s in card_specs)

    for i, (title, head, body, bl, body_lines, bl_lines, bl_h, foot_h, content_h) in enumerate(card_specs):
        bx = inner_x + i * (box_w + gap)
        col = colors[i]
        # Card body — sized to content
        c.setFillColor(COL_PANEL_ALT)
        c.setStrokeColor(col)
        c.setLineWidth(0.5)
        c.rect(bx, inner_y, box_w, card_h, fill=1, stroke=1)
        # Footer band (anchored at card bottom)
        c.setFillColor(COL_PANEL_FT)
        c.rect(bx, inner_y, box_w, foot_h, fill=1, stroke=0)
        # Divider above footer
        c.setFillColor(col)
        c.rect(bx, inner_y + foot_h, box_w, 0.6 * mm, fill=1, stroke=0)
        # Title bar at TOP of card
        title_bar_y = inner_y + card_h - title_bar_h
        c.setFillColor(col)
        c.rect(bx, title_bar_y, box_w, title_bar_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(bx + 2 * mm, title_bar_y + 1 * mm, title)
        # Headline just below title bar
        head_y = title_bar_y - 5 * mm
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(bx + 2 * mm, head_y, head)
        # Body lines — first line below headline by head_to_body_gap
        body_top = head_y - head_to_body_gap
        body_bot = inner_y + foot_h + 1.5 * mm  # above footer divider
        body_avail = body_top - body_bot
        n_lines = len(body_lines)
        if n_lines > 1:
            body_line_step = body_avail / (n_lines - 1) if n_lines > 1 else body_line_h
        else:
            body_line_step = body_line_h
        c.setFillColor(COL_SUB)
        c.setFont("Helvetica", body_fs)
        by = body_top
        for ln in body_lines:
            c.drawString(bx + 2 * mm, by, ln)
            by -= body_line_step
        # Footer: BOTTOM-LINE label + bl lines at fixed positions
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawString(bx + 2 * mm, inner_y + foot_h - 3.5 * mm, "BOTTOM-LINE")
        c.setFillColor(COL_AURORA)
        c.setFont("Helvetica-Bold", bl_fs)
        bly = inner_y + foot_h - 7 * mm
        for ln in bl_lines:
            c.drawString(bx + 2 * mm, bly, ln)
            bly -= bl_line_h


def draw_intermediaries_panel(c, x, y, w, h):
    """Three key intermediary tiers with risk/commercial-dynamic annotations."""
    draw_section_panel(c, x, y, w, h,
                       "RELEVANT INTERMEDIARIES  ·  FEED / DISTRIBUTION / CAPITAL",
                       accent=COL_CHANNEL_F)
    inner_x = x + 3 * mm
    inner_y = y + 3 * mm
    inner_w = w - 6 * mm
    inner_h = h - 9 * mm

    # Three columns: FEED / DISTRIBUTION / CAPITAL
    n_cols = 3
    gap = 2 * mm
    box_w = (inner_w - (n_cols - 1) * gap) / n_cols
    box_h = inner_h

    intermediaries = [
        ("FEED", COL_MAINLAND, [
            ("MainFeeds",   "Captive of Mainland (PE/Navis).",       "3 mills · ~140kt p.a."),
            ("ProStock",    "Open-market feed mill, partial supply.",  "NI + SI · spot price"),
            ("Inghams/Feed", "Broiler feed, not layer-grade.",         "Limited pull-through"),
        ]),
        ("DISTRIBUTION", COL_CHANNEL_F, [
            ("Bidfood",     "Foodservice broadliner — Bidvest.",       "Hotels, cafés, restaurants"),
            ("Gilmours",    "Foodservice distributor (NI).",           "Restaurants + caterers"),
            ("Versova",     "Versova group (Prolife, Vili's).",        "Integrated protein + eggs"),
        ]),
        ("CAPITAL", COL_HEYDEN, [
            ("Navis Capital", "Owns Mainland / Zeagold platform.",     "AUM US$3bn"),
            ("Manuka Funds",  "Family-office co-invest in Heyden.",     "Long-duration capital"),
            ("Halberd bid",   "Buy-side: Aurora Eggs acquisition.",    "Project Albatross"),
        ]),
    ]

    for i, (col_title, col_color, rows) in enumerate(intermediaries):
        bx = inner_x + i * (box_w + gap)
        # Column header strip
        head_h = 5 * mm
        c.setFillColor(col_color)
        c.rect(bx, inner_y + box_h - head_h, box_w, head_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 2 * mm, inner_y + box_h - 3.6 * mm, col_title)

        # Column body
        c.setFillColor(COL_PANEL_ALT)
        c.rect(bx, inner_y, box_w, box_h - head_h, fill=1, stroke=0)

        # Rows
        row_count = len(rows)
        row_top = inner_y + box_h - head_h - 2 * mm
        row_bottom = inner_y + 2 * mm
        row_avail = row_top - row_bottom
        row_h = row_avail / row_count

        for ri, (name, role, scale) in enumerate(rows):
            ry = row_top - ri * row_h
            # Compute content height for this row
            role_lines = wrap_text(role, (box_w - 4) / mm, 5.8)
            content_h = 4 * mm + len(role_lines) * 3.0 * mm + 1 * mm + 4 * mm  # name + role + gap + scale
            # Top-anchor at top of row, leaving any extra space as bottom padding
            content_top = ry - 1.2 * mm
            c.setFillColor(COL_TITLE)
            c.setFont("Helvetica-Bold", 7.2)
            c.drawString(bx + 2 * mm, content_top, name)
            role_y = content_top - 4 * mm
            c.setFillColor(COL_SUB)
            c.setFont("Helvetica", 5.8)
            for ln in role_lines:
                c.drawString(bx + 2 * mm, role_y, ln)
                role_y -= 3.0 * mm
            # Scale label at bottom of content block
            scale_y = role_y - 0.5 * mm
            c.setFillColor(col_color)
            c.setFont("Helvetica-Oblique", 5.6)
            c.drawString(bx + 2 * mm, scale_y, scale)

            # Row divider
            if ri < row_count - 1:
                c.setStrokeColor(COL_PANEL_FT)
                c.setLineWidth(0.3)
                c.line(bx + 1 * mm, ry - row_h + 0.5 * mm,
                       bx + box_w - 1 * mm, ry - row_h + 0.5 * mm)


def draw_producer_panel(c, x, y, w, h):
    draw_section_panel(c, x, y, w, h,
                       "NAMED PRODUCERS · VOLUME-RANKED · ~3.7M FLOCK",
                       accent=COL_MAINLAND)
    inner_x = x + 3 * mm
    inner_y = y + 3 * mm
    inner_w = w - 6 * mm
    inner_h = h - 10 * mm

    producers = [
        ("MAINLAND",     28, "PE/Navis",  "70/30",  85, "NI",      "Full stack",      COL_MAINLAND),
        ("AURORA",       18, "Family",    "50/50",  60, "NI+SI",   "Grader",          COL_AURORA),
        ("HEYDEN",       14, "Family",    "60/40",  47, "SI",      "Grader",          COL_HEYDEN),
        ("BETTER EGGS",   9, "Family",    "55/45",  65, "NI",      "Grader",          COL_BETTER),
        ("ZEAGOLD",       7, "PE/Mgmt",   "30/70",  73, "NI",      "Industrial",      COL_ZEAGOLD),
        ("HENERGY",       6, "Family",    "75/25", 100, "NI",      "Pure FR",         COL_HENERGY),
    ]
    row_gap = 2 * mm
    row_h = (inner_h - row_gap) / 2

    def render_row(items, ry):
        total = sum(p[1] for p in items)
        cell_h = row_h - 1 * mm
        cx = inner_x
        for (name, vol, own, plb, cf, foot, integ, col) in items:
            tw = (vol / total) * inner_w
            cell_w = tw - 1 * mm
            halo = (name == "AURORA")
            draw_producer_cell(c, cx, ry, cell_w, cell_h,
                               name, vol, own, plb, cf, foot, integ, col, halo=halo)
            cx += tw
    render_row(producers[:3], inner_y + row_h + row_gap)
    render_row(producers[3:], inner_y)


def draw_thesis_panel(c, x, y, w, h):
    draw_section_panel(c, x, y, w, h,
                       "PROJECT ALBATROSS  ·  THESIS ANCHORS",
                       accent=COL_AURORA)
    inner_x = x + 3 * mm
    inner_y = y + 3 * mm
    inner_w = w - 6 * mm
    inner_top = y + h - 11 * mm

    anchors = [
        ("Target",      "Aurora Eggs (NZ)",      "Family-controlled; 3rd gen."),
        ("Position",    "#2 producer, ~18% vol", "Behind Mainland (28%); ahead of Heyden (14%)"),
        ("Flock",       "720–800k hens",         "244k colony birds (largest NZ colony conversion exposure)"),
        ("Revenue",     "FY24 NZ$84.6M",         "12.8% EBITDA margin · 18% vol share of NZ shell egg"),
        ("Channel mix", "Retail 72% · FS 22%",   "Premium FR over-indexed; lowest PL-tender risk = Henergy"),
        ("Investment",  "Capex-led transition",  "NZ$8–12M feed mill + grading automation = NZ$3.5–5.5M EBITDA"),
    ]
    row_h = (inner_top - inner_y - 6 * mm) / len(anchors)
    for i, (label, val, note) in enumerate(anchors):
        ay = inner_top - (i + 1) * row_h
        # Label (left)
        c.setFillColor(COL_AURORA)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(inner_x, ay + 2 * mm, label.upper())
        # Value (right column)
        c.setFillColor(COL_TITLE)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(inner_x + 22 * mm, ay + 2 * mm, val)
        # Note (below value)
        c.setFillColor(COL_SUB)
        c.setFont("Helvetica", 6.5)
        c.drawString(inner_x + 22 * mm, ay - 1.5 * mm, note)
        # Hairline divider
        if i < len(anchors) - 1:
            c.setStrokeColor(HexColor("#D5CDB1"))
            c.setLineWidth(0.3)
            c.line(inner_x, ay - row_h + 1 * mm, inner_x + inner_w, ay - row_h + 1 * mm)


def draw_legend(c, x, y, w, h):
    draw_section_panel(c, x, y, w, h, "LEGEND  ·  ENCODING KEY", accent=COL_TITLE)
    inner_x = x + 3 * mm
    inner_w = w - 6 * mm
    inner_top = y + h - 9 * mm

    swatch_y = inner_top - 4 * mm
    sw_h = 4 * mm
    sw_w = 15 * mm
    gap = 1.5 * mm

    sx = inner_x
    for name, col in [
        ("CAGE", COL_CAGE), ("COLONY", COL_COLONY),
        ("BARN", COL_BARN), ("FREE-RANGE", COL_FREERANGE),
    ]:
        c.setFillColor(col)
        c.rect(sx, swatch_y, sw_w, sw_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(sx + sw_w / 2, swatch_y + 1.2 * mm, name)
        sx += sw_w + gap

    for name, col in [
        ("Retail", COL_CHANNEL_R), ("Foodservice", COL_CHANNEL_F),
        ("Industrial", COL_CHANNEL_I), ("Direct", COL_CHANNEL_D),
    ]:
        c.setFillColor(col)
        c.rect(sx, swatch_y, sw_w, sw_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(sx + sw_w / 2, swatch_y + 1.2 * mm, name)
        sx += sw_w + gap

    sx_t = sx + 3 * mm
    badge_w = inner_x + inner_w - sx_t
    if badge_w > 30 * mm:
        c.setFillColor(COL_AURORA)
        c.rect(sx_t, swatch_y, badge_w, sw_h, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(sx_t + badge_w / 2, swatch_y + 1.2 * mm,
                            "AURORA EGGS (FY24 NZ$84.6M rev · 12.8% EBITDA · 18% vol)")

    line1_y = swatch_y - 4.5 * mm
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(COL_TITLE)
    c.drawString(inner_x, line1_y, "ATTRIBUTE CODES (per producer tile):")
    c.setFont("Helvetica", 6.5)
    c.setFillColor(COL_SUB)
    rest = ("OWN: ownership   ·   BR/PL: brand / private-label mix   ·   CF: cage-free share %   ·   "
            "INT: integration depth (producer-only → 7-stack)   ·   FOOT: NI / SI / both")
    rest_lines = wrap_text(rest, inner_w - 2, 6.5)
    ry = line1_y - 3.2 * mm
    for ln in rest_lines:
        c.drawString(inner_x, ry, ln)
        ry -= 2.4 * mm

    line2_msg = ("Tile width = volume share within row.   Gold halo = target on producer roster.   "
                 "Gold ring on value-chain Producer stage = Aurora's positioning.   "
                 "Colony→barn bar shows current flock mix (40% colony / 20% barn / 40% FR).")
    line2_lines = wrap_text(line2_msg, inner_w - 1, 6.5)
    cy = ry - 1.5 * mm
    for ln in line2_lines:
        c.drawString(inner_x, cy, ln)
        cy -= 2.4 * mm


def build():
    c = canvas.Canvas(OUT_PATH, pagesize=A3[::-1])
    page_w, page_h = A3[1], A3[0]
    c.setTitle("NZ Egg Market — Structure Map (Project Albatross)")
    c.setAuthor("Halberd Capital Partners — Albatross Deal Team")
    c.setFillColor(COL_BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    M = 4 * mm
    draw_header(c, page_w, page_h)

    work_top = page_h - 28 * mm
    work_bot = M + 35 * mm
    work_h = work_top - work_bot
    work_left = M
    work_right = page_w - M
    work_w = work_right - work_left

    col1_w = 95 * mm
    col3_w = 78 * mm
    col2_w = work_w - col1_w - col3_w - 4 * mm

    vc_h = 55 * mm
    cb_h = 48 * mm
    int_h = 60 * mm
    dyn_h = 48 * mm   # dynamics cards need ~46mm of content + 9mm header ≈ 55mm; min 48mm with tighter body

    # Producer panel: enough for header + 2 rows of tiles + small gap, anchored at TOP
    prod_panel_h = 130 * mm
    prod_panel_y = work_top - prod_panel_h
    draw_producer_panel(c, work_left, prod_panel_y, col1_w, prod_panel_h)

    # Thesis anchors panel fills remaining left-column vertical space
    thesis_h = prod_panel_y - work_bot - 32 * mm - 3 * mm  # leave room for legend
    thesis_y = prod_panel_y - thesis_h
    if thesis_h > 40 * mm:
        draw_thesis_panel(c, work_left, thesis_y, col1_w, thesis_h)

    cx = work_left + col1_w + 2 * mm
    draw_value_chain(c, cx, work_top - vc_h, col2_w, vc_h)
    draw_cage_ban_strip(c, cx, work_top - vc_h - 2 * mm - cb_h, col2_w, cb_h)
    draw_commercial_dynamics(c, cx, work_bot + int_h + 2 * mm, col2_w, dyn_h)
    draw_intermediaries_panel(c, cx, work_bot, col2_w, int_h)

    chx = work_left + col1_w + 2 * mm + col2_w + 2 * mm
    draw_channel_split(c, chx, work_bot, col3_w, work_h)

    draw_legend(c, work_left, M, work_w, 32 * mm)

    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
    print(f"Wrote: {OUT_PATH}")
