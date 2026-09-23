#!/usr/bin/env python3
"""PDF-DATAPACK v1.1 -- MODULE A (TRANSCRIBE).

Reads the supplied PDFs and writes one markdown transcript per document.
Values are copied from the PDF text layer exactly as extracted; nothing is
rounded, converted, merged across documents or completed.

Usage: python3 module_a_transcribe.py <pdf_dir> <out_dir>
"""
import collections
import json
import re
import sys
from pathlib import Path

import pymupdf

# ---------------------------------------------------------------- documents
# doc_id, file, first page, last page (physical pages of the supplied file),
# caption regex override (None = default)
DOCS = [
    ("D1", "City Data Combined .pdf", 1, 25, None),
    ("D2", "City Data Combined .pdf", 26, 149, None),
    ("D3", "City Data Combined .pdf", 150, 158, None),
    ("D4", "f42db3bf-en.pdf", 1, 140,
     r"^(?P<kind>Figure|Table)\s+(?P<num>[A-Z]?\.?\d+(?:\.\d+)*)\.\s"),
    ("D5", "Oxford_Economics_2026_Global_Cities_Index.pdf", 1, 155, None),
    ("D6", "GHSL_UCDB_R2024.pdf", 1, 633, None),
    ("D7", "wcr2024_-_full_report.pdf", 1, 373, None),
]

# Identification strings are quoted verbatim from the cited page; Module A
# checks that each quote occurs on that page and marks it NOT FOUND otherwise.
DOC_IDENT = {
    "D1": {"title": ("Global Innovation Index 2025 Ranking of World’s Top 100 Innovation Clusters", 1),
           "author_publisher": ("© WIPO, 2025", 25), "publication_date": ("2025", 25)},
    "D2": {"title": ("World Urbanization Prospects 2025 Summary of Results", 28),
           "author_publisher": ("Department of Economic and Social Affairs Population Division", 28),
           "publication_date": ("New York, 2025", 28)},
    "D3": {"title": ("Statistical release: BIS residential property price statistics in Q1 2026", 150),
           "author_publisher": ("BIS", 150), "publication_date": ("27 August 2026", 150)},
    "D4": {"title": ("OECD Regions and Cities at a Glance 2024", 4),
           "author_publisher": ("OECD Publishing, Paris", 4), "publication_date": ("OECD (2024)", 4)},
    "D5": {"title": ("OXFORD ECONOMICS GLOBAL CITIES INDEX", 1),
           "author_publisher": ("© 2026 Oxford Economics Ltd.", 155), "publication_date": ("2026", 1)},
    "D6": {"title": ("Stats in the City – the GHSL Urban Centre Database 2025", 1),
           "author_publisher": ("European Commission, Joint Research Centre", 2),
           "publication_date": ("Luxembourg: Publications Office of the European Union, 2024", 2)},
    "D7": {"title": ("Cities and Climate Action World Cities Report 2024", 3),
           "author_publisher": ("First published in 2024 by United Nations Human Settlements Programme (UN-Habitat)", 4),
           "publication_date": ("First published in 2024", 4)},
}

CAPTION_RX = re.compile(
    r"^(?P<prefix>Appendix IV\s*-\s*)?(?P<kind>Table|Figure|Map|Graph|Chart)\s+"
    r"(?P<num>[A-Z]?\.?\d+(?:\.\d+)*)(?P<rest>\s*(?:\(continued\)|:\s*Continued)?)"
    r"(?:[\.:\s-]|$)")
LIST_PAGE_RX = re.compile(
    r"^\s*(List of (Boxes|Figures|Tables|Maps|boxes|figures|tables|maps|"
    r"Boxes, Figures, and Tables|Figures and Tables)|Contents|Table of contents)\s*$",
    re.M)
LEADER_RX = re.compile(r"\.{8,}")
END_RX = re.compile(r"^\s*(Sources?|Notes?|Note\s*:|StatLink|Data source|\*\s)", re.I)
NUM_RX = re.compile(r"^[\(\[]?[-–−+]?[$€£]?\d[\d,\.\s]*%?[a-z¹²³⁴⁵*†]?[\)\]]?$|^[-–−]$|^\.\.$|^n/?a$", re.I)
GLOSSARY_RX = re.compile(r"^\s*(Glossary|List of abbreviations|Abbreviations( and acronyms)?|"
                         r"Acronyms( and abbreviations)?|Definitions)\s*$", re.I)


YEAR_RX = re.compile(r"^(19|20)\d\d[a-z*]?$")


def norm_ws(s):
    return re.sub(r"\s+", " ", s).strip()


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def is_num(tok):
    return bool(NUM_RX.match(tok.strip()))


# ---------------------------------------------------------------- geometry
def lines_from_words(words, ytol=None):
    """Group words (x0,y0,x1,y1,text) into printed lines by vertical centre."""
    ws = sorted(words, key=lambda w: ((w[1] + w[3]) / 2, w[0]))
    lines = []
    for w in ws:
        yc = (w[1] + w[3]) / 2
        h = w[3] - w[1]
        tol = ytol if ytol is not None else max(1.5, h * 0.45)
        if lines and abs(lines[-1]["yc"] - yc) <= tol:
            lines[-1]["words"].append(w)
            n = len(lines[-1]["words"])
            lines[-1]["yc"] = (lines[-1]["yc"] * (n - 1) + yc) / n
        else:
            lines.append({"yc": yc, "words": [w]})
    for ln in lines:
        ln["words"].sort(key=lambda w: w[0])
        ln["y0"] = min(w[1] for w in ln["words"])
        ln["y1"] = max(w[3] for w in ln["words"])
    return lines


def grid_extract(words, region):
    """Word-position grid. Returns dict(rows, header_rows, flags, ok, reason)."""
    x0r, y0r, x1r, y1r = region
    ws = [w for w in words if (w[0] + w[2]) / 2 >= x0r and (w[0] + w[2]) / 2 <= x1r
          and (w[1] + w[3]) / 2 >= y0r and (w[1] + w[3]) / 2 <= y1r]
    if not ws:
        return None
    lines = lines_from_words(ws)
    # data lines: lines with >= 1 numeric word
    numeric_lines = [i for i, ln in enumerate(lines)
                     if any(is_num(w[4]) and not YEAR_RX.match(w[4]) for w in ln["words"])]
    text_table = len(numeric_lines) < 2
    first_data = 1 if text_table else numeric_lines[0]
    if first_data == 0:
        first_data = 0
    body = lines[first_data:] if not text_table else lines[1:]
    if not body:
        body = lines
    # column gaps from word coverage of body lines
    xs0 = min(w[0] for w in ws)
    xs1 = max(w[2] for w in ws)
    res = 0.5
    n = int((xs1 - xs0) / res) + 2
    cover = [0] * n
    for ln in body:
        for w in ln["words"]:
            a = int((w[0] - xs0) / res)
            b = int((w[2] - xs0) / res) + 1
            for k in range(max(a, 0), min(b, n)):
                cover[k] = 1
    # gaps: runs of zero coverage wider than min_gap
    heights = sorted(w[3] - w[1] for w in ws)
    fh = heights[len(heights) // 2]
    min_gap = max(2.0, fh * 0.25)
    gaps = []
    k = 0
    while k < n:
        if cover[k] == 0:
            s = k
            while k < n and cover[k] == 0:
                k += 1
            if (k - s) * res >= min_gap and s > 0 and k < n:
                gaps.append(xs0 + (s + k) / 2 * res)
        else:
            k += 1
    bounds = [xs0 - 1] + gaps + [xs1 + 1]
    ncol = len(bounds) - 1
    rows = []
    merged_note = False
    hdr_n = first_data if not text_table else 1
    for li, ln in enumerate(lines):
        cells = [[] for _ in range(ncol)]
        spans = {}
        # segments: consecutive words separated by normal spaces
        segs = []
        for w in ln["words"]:
            if segs and w[0] - segs[-1][2] < min_gap and (li < hdr_n or not any(
                    segs[-1][2] <= g <= w[0] for g in gaps)):
                segs[-1] = (segs[-1][0], segs[-1][1], w[2], w[3], segs[-1][4] + " " + w[4])
            else:
                segs.append(tuple(w[:5]))
        for sg in segs:
            ov = {}
            for c in range(ncol):
                o = min(sg[2], bounds[c + 1]) - max(sg[0], bounds[c])
                if o > 0:
                    ov[c] = o
            if not ov:
                cols = [min(range(ncol), key=lambda c: abs((bounds[c] + bounds[c + 1]) / 2 - (sg[0] + sg[2]) / 2))]
            else:
                # columns substantially covered by this printed string
                cols = [c for c, o in ov.items() if o >= 0.5 * (bounds[c + 1] - bounds[c])]
                if len(cols) < 2:
                    cols = [max(ov, key=ov.get)]
            if len(cols) == 1:
                cells[cols[0]].append(sg[4])
            else:
                # a printed string spanning several detected columns
                for c in cols:
                    cells[c].append(sg[4] + " [merged in source]")
                merged_note = True
        rows.append([" ".join(c) for c in cells])
    hdr = first_data if not text_table else 1
    # printed lines just above the first data row that are set at wrapped-line
    # pitch and only carry first-column text belong to that data row, not the header
    if not text_table and hdr >= 2:
        dp0 = [lines[i + 1]["yc"] - lines[i]["yc"] for i in range(hdr, len(lines) - 1)]
        if dp0:
            base0 = sorted(dp0)[len(dp0) // 2]
            k = hdr
            while k - 1 >= 1 and lines[k]["yc"] - lines[k - 1]["yc"] < 0.8 * base0 and \
                    rows[k - 1][0] and not any(rows[k - 1][1:]):
                k -= 1
            hdr = k
    # ---- join wrapped cell text: a printed line set tighter than the table's
    # normal row pitch belongs to the neighbouring row (verbatim text joined)
    ycs = [ln["yc"] for ln in lines]
    isnum = [any(is_num(x) and not YEAR_RX.match(x) for x in " ".join(r).split()) for r in rows]
    body_idx = list(range(hdr, len(rows)))
    joined = 0
    if len(body_idx) >= 3:
        pitches = [ycs[i + 1] - ycs[i] for i in body_idx[:-1]]
        dp = [ycs[i + 1] - ycs[i] for i in body_idx[:-1] if isnum[i] and isnum[i + 1]]
        if len(dp) >= 2 and not text_table:
            base = sorted(dp)[len(dp) // 2]
            tight = 0.8 * base
        else:
            base = min(pitches) if pitches else 0
            tight = 1.3 * base
        groups = [[body_idx[0]]]
        for i in body_idx[1:]:
            pch = ycs[i] - ycs[groups[-1][-1]]
            prev_has_num = any(isnum[k] for k in groups[-1])
            if pch < tight and not (isnum[i] and prev_has_num):
                groups[-1].append(i)
            else:
                groups.append([i])
        # a text-only line tight to BOTH neighbours: attach to the closer one
        new_rows = rows[:hdr]
        for g in groups:
            if len(g) > 1:
                joined += len(g) - 1
            new_rows.append([" ".join(rows[k][c] for k in g if rows[k][c]).strip() for c in range(ncol)])
        rows = new_rows
    ok = ncol >= 2 and len(rows) >= 2
    return {"rows": rows, "header_lines": hdr, "ncol": ncol, "ok": ok, "joined": joined,
            "text_table": text_table, "merged": merged_note,
            "y0": lines[0]["y0"], "y1": lines[-1]["y1"],
            "first_line": " ".join(w[4] for w in lines[0]["words"]).strip()}


def collapse_header(g):
    """Join multi-line header vertically per column (verbatim strings kept)."""
    h = g["header_lines"]
    rows = g["rows"]
    if h == 0:
        return [[""] * g["ncol"]], rows, h
    if h == 1:
        return rows[:1], rows[1:], h
    head = [" ".join(r[c] for r in rows[:h] if r[c]).strip() for c in range(g["ncol"])]
    return [head], rows[h:], h


# ---------------------------------------------------------------- document
class Doc:
    def __init__(self, doc_id, pdf, a, b, cap_rx):
        self.id = doc_id
        self.pdf = pdf
        self.a, self.b = a, b
        self.cap_rx = re.compile(cap_rx) if cap_rx else CAPTION_RX
        self.tables = []
        self.figures = []
        self.gaps = []
        self.hidden_pages = []

    def pages(self):
        return range(self.a - 1, self.b)


def running_lines(d, doc):
    """Header/footer strings (digits normalised) on >= 25% of pages."""
    cnt = collections.Counter()
    npg = 0
    for i in doc.pages():
        pg = d[i]
        H = pg.rect.height
        npg += 1
        seen = set()
        for b in pg.get_text("blocks"):
            if b[6] != 0:
                continue
            if b[3] < H * 0.09 or b[1] > H * 0.92:
                for ln in b[4].split("\n"):
                    key = re.sub(r"\d+", "#", ln.strip())
                    key = re.sub(r"\b[ivxlcdm]+\b$", "#", key)
                    if key:
                        seen.add(key)
        cnt.update(seen)
    return {k for k, v in cnt.items() if v >= max(3, npg * 0.25)}, cnt, npg


def norm_run(s):
    k = re.sub(r"\d+", "#", s.strip())
    return re.sub(r"\b[ivxlcdm]+\b$", "#", k)


def words_from_trace(spans_tr, horizontal_only=False):
    """Words (x0,y0,x1,y1,text) assembled from visible texttrace spans."""
    words = []
    for t in spans_tr:
        if horizontal_only and abs(t["dir"][0] - 1) > 0.01:
            continue
        cur, bb = "", None
        size = t["size"] or 8
        prev = None
        for ch in t["chars"]:
            c = chr(ch[0])
            cb = ch[3]
            gap = prev is not None and (cb[0] - prev[2] > size * 0.25 or cb[0] < prev[0] - 0.5
                                        or abs(cb[3] - prev[3]) > size * 0.5)
            if c.isspace() or gap:
                if cur.strip():
                    words.append((bb[0], bb[1], bb[2], bb[3], cur))
                cur, bb = "", None
                if c.isspace():
                    prev = cb
                    continue
            cur += c
            bb = cb if bb is None else (min(bb[0], cb[0]), min(bb[1], cb[1]), max(bb[2], cb[2]), max(bb[3], cb[3]))
            prev = cb
        if cur.strip():
            words.append((bb[0], bb[1], bb[2], bb[3], cur))
    return words


def split_word_chars(t):
    """Split a trace span's chars into words (same rule as words_from_trace);
    whitespace chars are returned as their own groups."""
    out, cur, prev = [], [], None
    size = t["size"] or 8
    for ch in t["chars"]:
        c = chr(ch[0])
        cb = ch[3]
        gap = prev is not None and (cb[0] - prev[2] > size * 0.25 or cb[0] < prev[0] - 0.5
                                    or abs(cb[3] - prev[3]) > size * 0.5)
        if c.isspace() or gap:
            if cur:
                out.append(cur)
            cur = []
            if c.isspace():
                out.append([ch])
                prev = cb
                continue
        cur.append(ch)
        prev = cb
    if cur:
        out.append(cur)
    return out


def iou(a, b):
    ix = min(a[2], b[2]) - max(a[0], b[0])
    iy = min(a[3], b[3]) - max(a[1], b[1])
    if ix <= 0 or iy <= 0:
        return 0.0
    inter = ix * iy
    ua = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
    return inter / ua if ua > 0 else 0.0


def visible_trace(pg):
    """(visible_trace_spans, n_hidden_spans) or (None, 0) if nothing is hidden.

    A drawn text span is treated as not displayed when (a) render mode is
    invisible / opacity 0, (b) it lies outside the page, (c) its characters are
    removed by a clip path (MuPDF TEXT_CLIP), or (d) an opaque filled shape is
    painted over it later AND the rendered page confirms it: the span area shows
    no ink, or its ink is explained by another, uncovered span at the same spot.
    """
    try:
        tr = pg.get_texttrace()
    except Exception:
        return None, 0
    covers = []
    for dr in pg.get_drawings():
        if dr.get("fill") is None or (dr.get("fill_opacity") or 1) < 0.99:
            continue
        r = dr["rect"]
        if r.width < 2 or r.height < 2:
            continue
        if min(dr["fill"]) < 0.95:
            continue  # only opaque near-white paint is treated as a cover-up
        covers.append((dr["seqno"], (r.x0, r.y0, r.x1, r.y1), dr["fill"]))
    clipset = set()
    for b in pg.get_text("rawdict", flags=pymupdf.TEXTFLAGS_RAWDICT | pymupdf.TEXT_CLIP)["blocks"]:
        for ln in b.get("lines", []):
            for sp in ln["spans"]:
                for ch in sp["chars"]:
                    clipset.add((round(ch["origin"][0], 1), round(ch["origin"][1], 1)))
    pr = pg.rect
    info = []  # (t, status) status: vis / hid / cov(fill)
    for t in tr:
        txt = "".join(chr(c[0]) for c in t["chars"])
        if not txt.strip():
            continue
        bb = t["bbox"]
        cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
        if t["type"] == 3 or t.get("opacity", 1) == 0:
            info.append((t, "hid", None))
            continue
        if not (pr.x0 <= cx <= pr.x1 and pr.y0 <= cy <= pr.y1):
            info.append((t, "off", None))
            continue
        # match by glyph origin only (ligatures expand to several chars at one origin)
        kept = [c for c in t["chars"] if chr(c[0]).isspace() or
                (round(c[2][0], 1), round(c[2][1], 1)) in clipset]
        nk = len([c for c in kept if not chr(c[0]).isspace()])
        if nk == 0:
            info.append((t, "off", None))
            continue
        clipped = nk < len([c for c in t["chars"] if not chr(c[0]).isspace()])
        if clipped:
            t = dict(t)
            t["chars"] = kept
        cov = None
        for sq, r, fill in covers:
            if sq > t["seqno"] and r[0] <= cx <= r[2] and r[1] <= cy <= r[3]:
                cov = fill
                break
        info.append((t, "cov" if cov is not None else ("clip" if clipped else "vis"), cov))
    if not any(st in ("hid", "cov") for _, st, _ in info):
        # only clipped / off-page text: MuPDF's clip-aware extraction (TEXT_CLIP,
        # mediabox clip) already excludes it, so the normal reading-order path is used
        return None, sum(1 for _, st, _ in info if st in ("off", "clip"))
    pix = None
    sc = 2.0
    vis, nh = [], 0
    # boxes of characters that are not painted over (used to explain ink)
    free_boxes = []
    for t, st, _ in info:
        if st in ("vis", "clip"):
            for wc in split_word_chars(t):
                wc = [c for c in wc if not chr(c[0]).isspace()]
                if wc:
                    free_boxes.append((min(c[3][0] for c in wc), min(c[3][1] for c in wc),
                                       max(c[3][2] for c in wc), max(c[3][3] for c in wc)))

    def has_ink(bb, fill):
        x0, y0 = max(0, int(bb[0] * sc)), max(0, int(bb[1] * sc))
        x1, y1 = min(pix.width, int(bb[2] * sc) + 1), min(pix.height, int(bb[3] * sc) + 1)
        smp = pix.samples
        vals = [smp[yy * pix.stride + xx] for yy in range(y0, y1) for xx in range(x0, x1)]
        return bool(vals) and max(vals) - min(vals) > 60

    for t, st, fill in info:
        if st in ("hid", "off"):
            nh += 1
            continue
        if st == "clip":
            nh += 1
            vis.append(t)
            continue
        if st == "vis":
            vis.append(t)
            continue
        # painted over: decide per whole word (never per character) -- keep a
        # word if the rendered page shows contrast (ink) inside its box that no
        # other, uncovered word at the same spot explains
        if pix is None:
            pix = pg.get_pixmap(dpi=144, colorspace=pymupdf.csGRAY)
        kept, lost = [], 0
        for wchars in split_word_chars(t):
            if all(chr(c[0]).isspace() for c in wchars):
                kept += wchars
                continue
            wb = (min(c[3][0] for c in wchars), min(c[3][1] for c in wchars),
                  max(c[3][2] for c in wchars), max(c[3][3] for c in wchars))
            wcx, wcy = (wb[0] + wb[2]) / 2, (wb[1] + wb[3]) / 2
            cov = any(sq > t["seqno"] and r[0] <= wcx <= r[2] and r[1] <= wcy <= r[3]
                      for sq, r, f in covers)
            if not cov:
                kept += wchars
                continue
            # ink test only guards against blend-mode paint: a word counts as
            # displayed if its box shows contrast AND no free (uncovered) word
            # overlaps it; any overlap means the ink may come from that other word
            other = any(iou(u, wb) > 0 for u in free_boxes)
            if has_ink(wb, None) and not other:
                kept += wchars
            else:
                lost += 1
        if lost:
            nh += 1
        if any(not chr(c[0]).isspace() for c in kept):
            t = dict(t)
            t["chars"] = kept
            vis.append(t)
    return (vis, nh) if nh else (None, 0)


def blocks_from_words(words, W):
    """Line-level pseudo-blocks (used only on pages that contain hidden text)."""
    out = []
    for half in (None,):
        pass
    for ln in lines_from_words(words):
        ws = ln["words"]
        # split a printed line at wide gaps (column boundaries)
        cur = [ws[0]]
        for w in ws[1:]:
            if w[0] - cur[-1][2] > 18:
                out.append(cur)
                cur = [w]
            else:
                cur.append(w)
        out.append(cur)
    segs = []
    for ws in out:
        segs.append({"bbox": (min(w[0] for w in ws), min(w[1] for w in ws),
                              max(w[2] for w in ws), max(w[3] for w in ws)),
                     "text": " ".join(w[4] for w in ws)})
    # merge printed lines into paragraph blocks (same left edge, small leading)
    blocks = []
    for sg in sorted(segs, key=lambda z: (z["bbox"][1], z["bbox"][0])):
        h = sg["bbox"][3] - sg["bbox"][1]
        tgt = None
        for bl in reversed(blocks[-6:]):
            if (abs(bl["bbox"][0] - sg["bbox"][0]) < 3 and 0 <= sg["bbox"][1] - bl["bbox"][3] < h * 0.9
                    and not CAPTION_RX.match(sg["text"]) and not END_RX.match(sg["text"])):
                tgt = bl
                break
        if tgt is None:
            blocks.append(dict(sg))
        else:
            tgt["text"] += "\n" + sg["text"]
            b0 = tgt["bbox"]
            tgt["bbox"] = (min(b0[0], sg["bbox"][0]), b0[1], max(b0[2], sg["bbox"][2]), sg["bbox"][3])
    return blocks


def column_of(bbox, W):
    x0, _, x1, _ = bbox
    if x1 - x0 > W * 0.55:
        return None  # full width
    return 0 if (x0 + x1) / 2 < W / 2 else 1


def read_blocks(pg, run_set, cap_rx, tp=None):
    """Text blocks in reading order. Blocks are split before any line that
    starts a caption or a Source/Note line so those become their own blocks."""
    W, H = pg.rect.width, pg.rect.height
    out = []
    removed = []
    for b in pg.get_text("dict", textpage=tp)["blocks"]:
        if b.get("type") != 0:
            continue
        cur = []
        for ln in b["lines"]:
            text = "".join(sp["text"] for sp in ln["spans"])
            bb = ln["bbox"]
            if not text.strip():
                continue
            if (bb[3] < H * 0.09 or bb[1] > H * 0.92) and (
                    norm_run(text) in run_set or re.fullmatch(r"\s*[ivxlcdm\d]+\s*", text)):
                removed.append(text.strip())
                continue
            starts = bool(cap_rx.match(text.strip()) or CAPTION_RX.match(text.strip())
                          or END_RX.match(text))
            if starts and cur:
                out.append(cur)
                cur = []
            cur.append((bb, text))
        if cur:
            out.append(cur)
    blocks = []
    for cur in out:
        x0 = min(c[0][0] for c in cur); y0 = min(c[0][1] for c in cur)
        x1 = max(c[0][2] for c in cur); y1 = max(c[0][3] for c in cur)
        blocks.append({"bbox": (x0, y0, x1, y1), "text": "\n".join(c[1] for c in cur)})
    return order_blocks(blocks, W), removed


def order_blocks(blocks, W):
    blocks = sorted(blocks, key=lambda bl: bl["bbox"][1])
    ordered, band = [], []
    for bl in blocks:
        col = column_of(bl["bbox"], W)
        if col is None:
            band.sort(key=lambda z: (column_of(z["bbox"], W) or 0, z["bbox"][1]))
            ordered += band
            band = []
            ordered.append(bl)
        else:
            band.append(bl)
    band.sort(key=lambda z: (column_of(z["bbox"], W) or 0, z["bbox"][1]))
    ordered += band
    return ordered


def is_prose(text):
    lines = [l for l in text.split("\n") if l.strip()]
    words = text.split()
    if len(words) < 12 or not lines:
        return False
    avg = sum(len(l) for l in lines) / len(lines)
    low = sum(1 for w in words if w[:1].islower())
    return avg > 35 and low > len(words) * 0.4


def is_list_page(text):
    return bool(LIST_PAGE_RX.search(text)) or len(LEADER_RX.findall(text)) >= 4


def ruled_regions(pg):
    """Ruled tables (vector lines) that pass basic quality checks."""
    regs = []
    try:
        tabs = pg.find_tables().tables
    except Exception:
        return regs
    for t in tabs:
        rows = t.extract()
        if len(rows) < 3 or t.col_count < 2:
            continue
        cells = [c for r in rows for c in r]
        filled = [c for c in cells if c not in (None, "")]
        first_col = [r[0] for r in rows if r and r[0] not in (None, "")]
        if len(filled) < 0.4 * len(cells) and not (len(rows) >= 10 and len(first_col) >= 0.8 * len(rows)):
            continue
        x0, y0, x1, y1 = t.bbox
        if (x1 - x0) < 120 or (y1 - y0) < 30:
            continue
        regs.append(tuple(t.bbox))
    return regs


def overlap(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def transcribe(pdf_dir, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    summary = {}
    opened = {}
    only = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
    for doc_id, fname, a, b, cap in DOCS:
        if only and doc_id not in only:
            continue
        d = opened.setdefault(fname, pymupdf.open(str(pdf_dir / fname)))
        doc = Doc(doc_id, fname, a, b, cap)
        run_set, run_cnt, npg = running_lines(d, doc)
        md = []
        meta = d.metadata or {}
        md.append(f"# {doc_id} — MODULE A transcript (PDF-DATAPACK v1.1)\n")
        md.append("## Metadata\n")
        md.append(f"- doc_id: {doc_id}")
        md.append(f"- source_file: {fname}")
        md.append(f"- source_physical_pages: {a}-{b} (anchors `[{doc_id}-pN]` use the physical page number N of the source file)")
        md.append(f"- page_count: {b - a + 1}")
        md.append(f"- pdf_metadata_title: {meta.get('title') or '[not set in file]'}")
        md.append(f"- pdf_metadata_author: {meta.get('author') or '[not set in file]'}")
        md.append(f"- pdf_metadata_creationDate: {meta.get('creationDate') or '[not set in file]'}")
        md.append("- ocr_pages: [] (no page is a scanned image of text; see skipped-page lines for image-only pages)")
        md.append("- title / author_publisher / publication_date: quoted verbatim in `## Document identification` below, each with the page anchor it is copied from.")
        md.append("\n## Document identification\n")
        for fld, (quote, pno) in DOC_IDENT[doc_id].items():
            ptxt = norm_ws(d[pno - 1].get_text())
            ok = norm_ws(quote) in ptxt
            md.append(f"- {fld}: \"{quote}\" [{doc_id}-p{pno}]" + ("" if ok else " [NOT FOUND on cited page]"))
        md.append("\n## Running headers/footers (noted once, removed from page bodies)\n")
        for k in sorted(run_set):
            md.append(f"- `{k}` (on {run_cnt[k]} of {npg} pages; `#` = page-number digits)")
        if not run_set:
            md.append("- none detected")
        md.append("\n## Pages\n")
        tcount = 0
        fcount = 0
        open_table = None  # table continuing to next page
        label_to_table = {}
        label_to_fig = {}
        list_pages = []
        for i in doc.pages():
            pg = d[i]
            p = i + 1
            W, H = pg.rect.width, pg.rect.height
            anchor = f"[{doc_id}-p{p}]"
            vis, nhid = visible_trace(pg)
            if vis is None and nhid:
                doc.gaps.append({"location": f"[{doc_id}-p{p}]",
                                 "what": f"{nhid} text spans lie outside the page or are clipped away by a clip path (not displayed); excluded by clip-aware extraction",
                                 "reason": "OUT-OF-SCOPE"})
            if vis is None:
                tp = pg.get_textpage(flags=pymupdf.TEXTFLAGS_DICT | pymupdf.TEXT_CLIP)
                blocks, _ = read_blocks(pg, run_set, doc.cap_rx, tp)
                dd = pg.get_text("dict", textpage=tp)
                rot = set()
                for bno, b in enumerate(dd["blocks"]):
                    for lno, ln in enumerate(b.get("lines", [])):
                        if abs(ln["dir"][0] - 1) > 0.01:
                            rot.add((b["number"], lno))
                words_all = [w[:5] for w in pg.get_text("words", textpage=tp)
                             if (w[5], w[6]) not in rot]
            else:
                words_all = words_from_trace(vis, horizontal_only=True)
                blocks = [bl for bl in blocks_from_words(words_from_trace(vis), W)
                          if not ((bl["bbox"][3] < H * 0.09 or bl["bbox"][1] > H * 0.92)
                                  and (norm_run(bl["text"]) in run_set
                                       or re.fullmatch(r"\s*[ivxlcdm\d]+\s*", bl["text"])))]
                blocks = order_blocks(blocks, W)
                doc.gaps.append({"location": f"[{doc_id}-p{p}]",
                                 "what": f"{nhid} text spans present in the PDF text layer but not displayed (invisible render mode, or painted over by an opaque shape drawn later) were excluded; page text rebuilt from displayed spans only",
                                 "reason": "OUT-OF-SCOPE"})
                doc.hidden_pages.append(p)
            H = pg.rect.height
            # drop running header/footer words (they are noted once in the metadata)
            keep = []
            for ln in lines_from_words(words_all):
                txt = " ".join(w[4] for w in ln["words"])
                if (ln["y1"] < H * 0.09 or ln["y0"] > H * 0.92) and (
                        norm_run(txt) in run_set or re.fullmatch(r"[ivxlcdm\d]+", txt.strip())):
                    continue
                keep += ln["words"]
            words_all = keep
            fullt = "\n".join(bl["text"] for bl in blocks)
            if not fullt.strip():
                nimg = len(pg.get_images())
                why = "image-only page (illustration/photo, no text layer)" if nimg or len(pg.get_drawings()) > 5 else "blank"
                md.append(f"### {anchor}\n\n[{doc_id}-p{p}: skipped — {why}]\n")
                open_table = None
                continue
            listp = is_list_page(fullt)
            if listp:
                list_pages.append(p)
            glossary = any(GLOSSARY_RX.match(bl["text"].split("\n")[0]) for bl in blocks)
            # ------------------------------------------------ captions
            caps = []
            if not listp:
                for bi, bl in enumerate(blocks):
                    first = bl["text"].split("\n")[0].strip()
                    m = doc.cap_rx.match(first)
                    if not m:
                        continue
                    if len(bl["text"]) > 900:
                        continue  # prose sentence that starts with "Table 2 ..."
                    after = first[m.end():].lstrip(" \t:.-–")
                    if after[:1].islower() or re.match(r"(and|or|to|in|shows?|presents?|summari[sz]es?)\b", after):
                        continue  # in-text reference, e.g. "Table 2 identifies ..."
                    kind = m.group("kind")
                    label = f"{m.groupdict().get('prefix') or ''}{kind} {m.group('num')}".strip()
                    caps.append({"bi": bi, "kind": kind, "label": label, "bbox": bl["bbox"],
                                 "text": bl["text"],
                                 "cont": bool(re.search(r"continued", bl["text"].split("\n")[0], re.I))})
            # ------------------------------------------------ regions
            regions = []  # dict(kind, bbox, cap)
            ends = [bl for bl in blocks if END_RX.match(bl["text"])]
            cap_tops = sorted(c["bbox"][1] for c in caps)
            for c in caps:
                cx0, cy0, cx1, cy1 = c["bbox"]
                col = column_of(c["bbox"], W)
                # vertical end: next caption, or first Source/Note block below (inclusive)
                nxt = [t for t in cap_tops if t > cy0 + 1]
                yend = min(nxt) if nxt else H * 0.93
                if col is not None:
                    other = [bl for bl in blocks if column_of(bl["bbox"], W) == 1 - col
                             and bl["bbox"][1] < yend and bl["bbox"][3] > cy1 and is_prose(bl["text"])]
                    if not other:
                        col = None
                if col is None:
                    hx0, hx1 = 0, W
                else:
                    hx0, hx1 = (0, W / 2) if col == 0 else (W / 2, W)
                endb = [e for e in ends if e["bbox"][1] >= cy1 - 1 and e["bbox"][1] < yend
                        and (col is None or column_of(e["bbox"], W) in (None, col))]
                src_y = min(e["bbox"][1] for e in endb) if endb else None
                ybody_end = src_y if src_y is not None else yend
                regions.append({"cap": c, "bbox": (hx0, cy1 + 0.1, hx1, ybody_end - 0.1),
                                "notes": [e for e in endb if e["bbox"][1] < yend and (
                                    not nxt or e["bbox"][1] < min(nxt))]})
            # uncaptioned ruled tables
            ruled = ruled_regions(pg)
            for rb in ruled:
                if any(overlap(rb, r["bbox"]) for r in regions):
                    continue
                regions.append({"cap": None, "bbox": rb, "notes": []})
            # continuation of an open table from the previous page (no caption here)
            if open_table is not None and not caps:
                endb = [e for e in ends if e["bbox"][1] > H * 0.1]
                yend = min(e["bbox"][1] for e in endb) - 0.1 if endb else H * 0.93
                cand = (0, H * 0.02, W, yend)
                gc = grid_extract(words_all, cand)
                if gc is not None:
                    hc, _, _ = collapse_header(gc)
                    hw = set(norm_ws(" ".join(hc[0])).split())
                    ow = set(open_table["header_norm"].split())
                    same_head = bool(hw and ow) and len(hw & ow) / len(hw | ow) >= 0.6
                    headless = gc["header_lines"] == 0 and abs(gc["ncol"] - open_table["ncol"]) <= 1
                    if same_head or headless:
                        regions = [r for r in regions if not overlap(r["bbox"], cand)]
                        regions.insert(0, {"cap": None, "bbox": cand, "notes": endb,
                                           "continues": open_table})
            # ------------------------------------------------ emit
            regions.sort(key=lambda r: (r["cap"]["bbox"][1] if r["cap"] else r["bbox"][1]))
            used_blocks = set()
            region_out = []
            new_open = None
            for r in regions:
                c = r["cap"]
                is_fig = c is not None and c["kind"] in ("Figure", "Map", "Graph", "Chart")
                if c is not None:
                    used_blocks.add(c["bi"])
                for nb in r["notes"]:
                    used_blocks.add(id(nb))
                rb = r["bbox"]
                inside = [bi for bi, bl in enumerate(blocks)
                          if bi not in used_blocks and id(bl) not in used_blocks
                          and (c is None or bi != c["bi"])
                          and (bl["bbox"][0] + bl["bbox"][2]) / 2 >= rb[0]
                          and (bl["bbox"][0] + bl["bbox"][2]) / 2 <= rb[2]
                          and (bl["bbox"][1] + bl["bbox"][3]) / 2 >= rb[1]
                          and (bl["bbox"][1] + bl["bbox"][3]) / 2 <= rb[3]]
                if is_fig:
                    lab = c["label"]
                    if c["cont"] and lab in label_to_fig:
                        fid = label_to_fig[lab]
                        cont = True
                    else:
                        fcount += 1
                        fid = f"{doc_id}-F{fcount}"
                        label_to_fig.setdefault(lab, fid)
                        cont = False
                    printed = [blocks[bi]["text"] for bi in inside]
                    for bi in inside:
                        used_blocks.add(bi)
                    nums = sum(1 for t in printed for tok in t.split() if is_num(tok))
                    ftxt = []
                    ftxt.append(f"#### [{fid}] FIGURE{' (continued)' if cont else ''} — page {p}")
                    ftxt.append("caption_verbatim:")
                    ftxt.append("```text\n" + c["text"] + "\n```")
                    ftxt.append("printed_text_in_figure_area_verbatim:")
                    ftxt.append("```text\n" + ("\n".join(printed) if printed else "") + "\n```")
                    if nums == 0:
                        ftxt.append("[VISUAL-ONLY-NO-DATA] no numeric data labels are printed in the text layer of the figure area; values not read off axes.")
                    else:
                        ftxt.append("[AMBIGUOUS: printed labels transcribed as text lines; label-to-value pairing not machine-resolved]")
                    for nb in r["notes"]:
                        ftxt.append("figure_notes_verbatim:")
                        ftxt.append("```text\n" + nb["text"] + "\n```")
                    doc.figures.append({"id": fid, "page": p, "label": lab, "cont": cont,
                                        "visual_only": nums == 0})
                    region_out.append((rb[1] if c is None else c["bbox"][1], "\n".join(ftxt)))
                    continue
                # ---------------- table
                g = grid_extract(words_all, rb)
                cont_from = r.get("continues")
                if c is None and cont_from is None and g is not None:
                    # uncaptioned ruled region: accept only a real table (text header
                    # row with >= 2 labels, no prose paragraph inside)
                    head_cells = [x for x in (g["rows"][0] if g["rows"] else []) if x and not is_num(x)]
                    prose_inside = any(is_prose(blocks[bi]["text"]) and len(blocks[bi]["text"].split()) >= 60
                                       for bi in inside) or (
                        (rb[2] - rb[0]) * (rb[3] - rb[1]) > 0.85 * W * H)
                    if len(head_cells) < 2 or g["header_lines"] < 1 or prose_inside:
                        continue
                if c is not None and c["cont"] and c["label"] in label_to_table:
                    cont_from = label_to_table[c["label"]]
                if g is None:
                    if c is not None:
                        doc.gaps.append({"location": anchor, "what": f"{c['label']}: no text found in table area",
                                         "reason": "VISUAL-ONLY"})
                    continue
                if cont_from is not None:
                    tid = cont_from["id"]
                    tt = cont_from
                    tt["pages"].append(p)
                else:
                    tcount += 1
                    tid = f"{doc_id}-T{tcount}"
                    tt = {"id": tid, "pages": [p], "label": c["label"] if c else None,
                          "header_first": None}
                    doc.tables.append(tt)
                    if c is not None:
                        label_to_table.setdefault(c["label"], tt)
                for bi in inside:
                    used_blocks.add(bi)
                head, body, hl = collapse_header(g)
                out = []
                if cont_from is not None:
                    out.append(f"[{tid} continued → p{p}]")
                    out.append(f"#### [{tid}] TABLE (continued) — page {p}")
                else:
                    out.append(f"#### [{tid}] TABLE — page {p}")
                if c is not None:
                    out.append("title_verbatim:")
                    out.append("```text\n" + c["text"] + "\n```")
                elif cont_from is None:
                    out.append("title_verbatim:")
                    out.append("```text\n[no caption printed in source]\n```")
                flags = []
                if g["text_table"]:
                    flags.append("[AMBIGUOUS: header extent — no numeric rows; first printed line taken as header]")
                if hl > 1:
                    flags.append(f"header: {hl} printed header lines joined vertically per column (strings verbatim) [AMBIGUOUS: header words are placed in the column under which they are printed; labels printed across several columns (e.g. a year over a group of columns) sit in one of them]")
                if g.get("joined"):
                    flags.append(f"{g['joined']} wrapped printed lines joined into their row's cells (line pitch tighter than the table's row pitch; text verbatim, joined with a space)")
                if g["merged"]:
                    flags.append("cells marked `[merged in source]` hold one printed string spanning several columns")
                if hl == 0:
                    flags.append("no header printed in this table area (header row left blank; all printed lines are body rows)")
                if g["ncol"] < 2:
                    flags.append("[AMBIGUOUS: no column structure detected — content kept as single-column rows]")
                out.append("table_flags: " + ("; ".join(flags) if flags else "none"))
                out.append("")
                out.append("| " + " | ".join(esc(x) for x in head[0]) + " |")
                out.append("|" + "---|" * len(head[0]))
                for row in body:
                    out.append("| " + " | ".join(esc(x) for x in row) + " |")
                out.append("")
                nfn = tt.setdefault("nfn", 0)
                for nb in r["notes"]:
                    nfn += 1
                    out.append(f"[{tid}-fn{nfn}]")
                    out.append("```text\n" + nb["text"] + "\n```")
                tt["nfn"] = nfn
                if cont_from is None:
                    tt["header_norm"] = norm_ws(" ".join(head[0]))
                    tt["ncol"] = g["ncol"]
                region_out.append((rb[1] if c is None else c["bbox"][1], "\n".join(out)))
                # table open to next page if it runs to page bottom without Source/Note
                if not r["notes"] and rb[3] >= H * 0.85 and g["y1"] > H * 0.8:
                    new_open = tt
            open_table = new_open
            # prose blocks (not inside regions)
            items = []
            for bi, bl in enumerate(blocks):
                if bi in used_blocks or id(bl) in used_blocks:
                    continue
                items.append((bl["bbox"][1], bi, bl["text"]))
            md.append(f"### {anchor}\n")
            if listp:
                md.append("[LIST/CONTENTS PAGE — transcribed verbatim; used as completeness checklist]\n")
            if glossary:
                md.append(f"[GLOSSARY/DEFINITIONS PAGE {anchor}]\n")
            # prose (reading order) first, then this page's table/figure blocks in vertical order
            regs_sorted = sorted(region_out, key=lambda z: z[0])
            emitted = [("P", text) for _, _, text in items]
            md.append("```text")
            md.append("\n\n".join(t for _, t in emitted) if emitted else "")
            md.append("```\n")
            for _, rtext in regs_sorted:
                md.append(rtext)
                md.append("")
        # ------------------------------------------------ A7 self-verification
        md.append("\n## A7 self-verification checklist\n")
        body = "\n".join(md)
        page_heads = re.findall(r"^### \[" + doc_id + r"-p(\d+)\]", body, re.M)
        skipped = re.findall(r"\[" + doc_id + r"-p(\d+): skipped — ([^\]]+)\]", body)
        md.append(f"- Pages: {doc.b - doc.a + 1} in range p{doc.a}–p{doc.b}; page anchors emitted in order: {len(page_heads)} "
                  f"({'complete' if len(page_heads) == doc.b - doc.a + 1 else 'INCOMPLETE'}).")
        md.append(f"- Skipped pages (no text layer): {', '.join('p' + a + ' (' + b + ')' for a, b in skipped) or 'none'}.")
        lab_rx = re.compile(r"(Table|Figure|Map|Graph)\s+([A-Z]?\.?\d+(?:\.\d+)*)(?:\s*[:.\t]|\s+-?\s*[A-Z])")
        listed = {"Table": set(), "Figure": set()}
        for lp in list_pages:
            seg = body.split(f"### [{doc_id}-p{lp}]", 1)[1].split("\n### [", 1)[0]
            for m in lab_rx.finditer(seg):
                listed["Table" if m.group(1) == "Table" else "Figure"].add(f"{m.group(1)} {m.group(2)}")
        t_lab = {re.sub(r"^Appendix IV\s*-\s*", "", t["label"]) for t in doc.tables if t["label"]}
        f_lab = {f["label"] for f in doc.figures}
        unc = sum(1 for t in doc.tables if not t["label"])
        miss_t = sorted(listed["Table"] - t_lab)
        miss_f = sorted(listed["Figure"] - f_lab)
        md.append(f"- Tables: document's own list names {len(listed['Table'])}; captioned tables found in body: {sum(1 for t in doc.tables if t['label'])}; "
                  f"uncaptioned ruled tables detected: {unc}; transcribed table IDs: {len(doc.tables)}. "
                  f"Listed but not transcribed as a table block: {', '.join(miss_t) or 'none'}.")
        md.append(f"- Figures/maps/graphs: document's own list names {len(listed['Figure'])}; figure IDs transcribed: "
                  f"{len(doc.figures)} ({sum(1 for f in doc.figures if f['cont'])} continuation blocks). "
                  f"Listed but not found as a caption: {', '.join(miss_f) or 'none'}.")
        for lab in miss_t:
            doc.gaps.append({"location": f"{doc_id} list of tables", "what": f"{lab}: named in the document's list but no matching caption block was found in the body; its content, if present, is transcribed in the page text",
                             "reason": "NOT FOUND"})
        for lab in miss_f:
            doc.gaps.append({"location": f"{doc_id} list of figures", "what": f"{lab}: named in the document's list but no matching caption block was found in the body",
                             "reason": "NOT FOUND"})
        md.append("- Every table value sits inside an anchored table block (`[Dn-Tk]`, cell `rXcY`); all other printed text (including numbers in prose and in figure areas) sits inside a page-anchored block `[Dn-pN]` or figure block `[Dn-Fk]`.")
        md.append("- Values copied as extracted from the PDF text layer: no rounding, no unit conversion, no reformatting; precision kept as displayed.")
        md.append("- Contradictions: none resolved (none adjudicated in this module).")
        md.append("- Causal verbs: none in text added by this module (markup and flags only); source text is quoted verbatim and may itself contain such words.")
        md.append(f"- Hidden/undisplayed text excluded on pages: {', '.join('p' + str(x) for x in doc.hidden_pages) or 'none'} (details in the JSON `extraction_gaps`).")
        md.append("- Scanned pages: none (every text page has a text layer); `[OCR-SOURCE]` not used.")
        md.append("\n## Extraction gaps declared by Module A\n")
        for g in doc.gaps:
            md.append(f"- GAP | {g['location']} | {g['what']} | {g['reason']}")
        if not doc.gaps:
            md.append("- none")
        (out_dir / f"{doc_id}_transcript.md").write_text("\n".join(md), encoding="utf-8")
        print(doc_id, "tables", len(doc.tables), "figures", len(doc.figures), "list pages", list_pages)
    if only:
        return
    (out_dir / "_module_a_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")


if __name__ == "__main__":
    transcribe(Path(sys.argv[1]), Path(sys.argv[2]))
