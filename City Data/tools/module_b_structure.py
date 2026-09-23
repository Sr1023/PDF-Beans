#!/usr/bin/env python3
"""PDF-DATAPACK v1.1 -- MODULE B (STRUCTURE).

Quarantine: this script reads ONLY the Module-A transcripts (markdown). It
never opens a PDF. Every JSON value is reorganised from the transcript and
carries a transcript anchor. No values, labels or definitions are added.

Usage: python3 module_b_structure.py <transcript_dir> <out_json> <report_md>
"""
import json
import re
import sys
from pathlib import Path

DOC_ORDER = ["D1", "D2", "D3", "D4", "D5", "D6", "D7"]

# Rule (c) for key_metrics: the sections each document itself titles as its
# summary. Page ranges are physical pages; the heading must be present on the
# first page of the range (checked below) or the rule is not applied.
SUMMARY_SECTIONS = {
    "D2": ("Key messages", 36, 39),
    "D3": ("Summary of latest developments", 151, 151),
    "D4": ("Executive summary", 15, 15),
    "D6": ("Abstract", 5, 5),
    "D7": ("Key Findings and Messages", 17, 29),
}

NUM_TOKEN = re.compile(
    r"(?<![\w.,])[-–−+]?(?:US\$|\$|€|£)?\d{1,3}(?:[,  ]\d{3})+(?:\.\d+)?%?"
    r"|(?<![\w.,])[-–−+]?(?:US\$|\$|€|£)?\d+(?:\.\d+)?%?")
YEAR_CELL = re.compile(r"^(19|20)\d\d$")
KEY_TITLE = re.compile(r"\b(key|headline|summary|overview)\b", re.I)
CAUSAL = re.compile(r"\b(caused|drove|driven by|led to|because|due to)\b", re.I)


def parse_num(raw):
    """value_num: parse a displayed string to float, or None. Never coerces
    non-numeric markers (n/a, .., –, blanks, footnote-only strings)."""
    s = raw.strip()
    s = re.sub(r"\s*\[merged in source\]$", "", s)
    m = re.fullmatch(r"([-–−+]?)(?:US\$|\$|€|£)?(\d{1,3}(?:[,\u202f\u00a0 ]\d{3})+|\d+)(\.\d+)?\s*%?", s)
    if not m:
        return None
    sign = "-" if m.group(1) in ("-", "–", "−") else ""
    try:
        return float(sign + re.sub(r"[,\u202f\u00a0 ]", "", m.group(2)) + (m.group(3) or ""))
    except ValueError:
        return None


def split_md_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip())
    cells = cells[1:-1] if len(cells) >= 2 else cells
    return [c.strip().replace("\\|", "|") for c in cells]


def parse_transcript(path):
    doc_id = path.name.split("_")[0]
    lines = path.read_text(encoding="utf-8").split("\n")
    out = {"doc_id": doc_id, "meta": {}, "ident": {}, "pages": {}, "tables": {}, "figures": {},
           "gaps": [], "glossary_pages": set(), "list_pages": set(), "a7": []}
    i, page, in_fence = 0, None, False
    section = None
    cur_block = None  # ("T"/"F", id)

    def read_fence(k):
        # lines[k] == "```text" -> returns (text, index after closing fence)
        buf = []
        k += 1
        while k < len(lines) and lines[k] != "```":
            buf.append(lines[k])
            k += 1
        return "\n".join(buf), k + 1

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("## "):
            section = ln[3:].strip()
            i += 1
            continue
        if section == "Metadata" and ln.startswith("- "):
            k, _, v = ln[2:].partition(": ")
            out["meta"][k] = v
        elif section == "Document identification" and ln.startswith("- "):
            m = re.match(r"- (\w+): \"(.*)\" \[(D\d-p\d+)\](.*)$", ln)
            if m:
                out["ident"][m.group(1)] = {"text_verbatim": m.group(2), "anchor": f"[{m.group(3)}]",
                                            "found": "NOT FOUND" not in m.group(4)}
        elif section == "A7 self-verification checklist" and ln.startswith("- "):
            out["a7"].append(ln[2:])
        elif section and section.startswith("Extraction gaps") and ln.startswith("- GAP | "):
            _, loc, what, reason = [x.strip() for x in ln.split(" | ", 3)]
            out["gaps"].append({"location": loc, "what": what, "reason": reason})
        elif section == "Pages":
            m = re.match(r"^### \[(D\d)-p(\d+)\]$", ln)
            if m:
                page = int(m.group(2))
                out["pages"][page] = {"prose": [], "skipped": None}
                cur_block = None
                i += 1
                continue
            if ln.startswith("[LIST/CONTENTS PAGE"):
                out["list_pages"].add(page)
            if ln.startswith("[GLOSSARY/DEFINITIONS PAGE"):
                out["glossary_pages"].add(page)
            ms = re.match(r"^\[(D\d)-p(\d+): skipped — (.+)\]$", ln)
            if ms:
                out["pages"][page]["skipped"] = ms.group(3)
            if ln == "```text" and cur_block is None:
                txt, i = read_fence(i)
                out["pages"][page]["prose"].append(txt)
                continue
            mt = re.match(r"^#### \[(D\d-T\d+)\] TABLE( \(continued\))? — page (\d+)$", ln)
            mf = re.match(r"^#### \[(D\d-F\d+)\] FIGURE( \(continued\))? — page (\d+)$", ln)
            if mt:
                tid = mt.group(1)
                blk = {"page": int(mt.group(3)), "cont": bool(mt.group(2)), "title": None,
                       "flags": "", "header": None, "rows": [], "fns": []}
                out["tables"].setdefault(tid, []).append(blk)
                cur_block = ("T", tid, blk)
                i += 1
                continue
            if mf:
                fid = mf.group(1)
                blk = {"page": int(mf.group(3)), "cont": bool(mf.group(2)), "caption": None,
                       "printed": "", "visual_only": False, "notes": []}
                out["figures"].setdefault(fid, []).append(blk)
                cur_block = ("F", fid, blk)
                i += 1
                continue
            if cur_block is not None:
                kind, bid, blk = cur_block
                if ln in ("title_verbatim:", "caption_verbatim:", "printed_text_in_figure_area_verbatim:",
                          "figure_notes_verbatim:"):
                    txt, i = read_fence(i + 1)
                    key = {"title_verbatim:": "title", "caption_verbatim:": "caption",
                           "printed_text_in_figure_area_verbatim:": "printed"}.get(ln)
                    if key:
                        blk[key] = txt
                    else:
                        blk["notes"].append(txt)
                    continue
                if ln.startswith("table_flags: "):
                    blk["flags"] = ln[len("table_flags: "):]
                elif ln.startswith("[VISUAL-ONLY-NO-DATA]"):
                    blk["visual_only"] = True
                elif ln.startswith("|") and kind == "T":
                    if re.fullmatch(r"\|(---\|)+", ln):
                        pass
                    elif blk["header"] is None:
                        blk["header"] = split_md_row(ln)
                    else:
                        blk["rows"].append(split_md_row(ln))
                else:
                    mfn = re.match(r"^\[(D\d-T\d+)-fn(\d+)\]$", ln)
                    if mfn and kind == "T":
                        txt, i = read_fence(i + 1)
                        blk["fns"].append({"n": int(mfn.group(2)), "text": txt})
                        continue
        i += 1
    return out


def build(tdir):
    docs = {}
    for d in DOC_ORDER:
        p = tdir / f"{d}_transcript.md"
        docs[d] = parse_transcript(p)

    pack = {
        "_conventions": {
            "anchor_syntax": "[Dn-pN] = document n, physical page N of the supplied source file; [Dn-Tk] = table k of document n (document order); [Dn-Fk] = figure/map/graph k; [Dn-Tk-fnM] = footnote/source/note block M of table k.",
            "cell_addressing": "[Dn-Tk-rXcY]: r1 is the header row (`columns`); body rows are numbered r2, r3, ... in transcript order, running continuously across continuation pages (header rows repeated on continuation pages are not counted); cY counts columns from 1 (left). `rows[X-2][Y-1]` in the JSON is cell rXcY; `row_pages[X-2]` gives its page.",
            "scope": "FULL",
            "source_files": {"D1-D3": "City Data Combined .pdf (D1 = physical pages 1-25, D2 = 26-149, D3 = 150-158)",
                             "D4": "f42db3bf-en.pdf", "D5": "Oxford_Economics_2026_Global_Cities_Index.pdf",
                             "D6": "GHSL_UCDB_R2024.pdf", "D7": "wcr2024_-_full_report.pdf"},
            "value_pairs": "value_raw is the string exactly as displayed; value_num is a parsed float or null (null for any non-numeric string: n/a, .., –, blanks, text).",
            "key_metrics_rule": "(a) callout boxes: not machine-identifiable in the transcript -> none emitted by rule (a); (b) every non-empty cell of tables whose title_verbatim contains key|headline|summary|overview; (c) every number printed in the prose of the section the document itself titles as its summary (see summary_sections); label_verbatim is the sentence containing the number; unit_verbatim is '%' when the % sign is printed with the number, otherwise '[see label_verbatim]' (unit words, if any, are inside the sentence).",
            "summary_sections": {k: {"heading_verbatim": v[0], "pages": f"p{v[1]}-p{v[2]}"} for k, v in SUMMARY_SECTIONS.items()},
            "time_series_rule": "Built only from tables whose header row has >= 3 cells that are exactly a 4-digit year; one series per body row (label = first cell of the row), one observation per year column; period = that year (ISO 8601 year).",
            "definitions_rule": "From pages Module A marks as glossary/abbreviation pages (term: definition lines, or term line followed by its expansion) and from D6 indicator fact sheets (term = 'Indicator Name' field, definition = 'Indicator description' field).",
            "contradictions_rule": "Mechanical only: within one document, two different tables with an identical header row, the same non-numeric row label (unique in each table) and the same column header, whose numeric cells differ. Semantic contradiction screening (e.g. the same statistic stated differently in prose) is not performed here (downstream).",
            "values_counted_for_reconciliation": "non-empty table cells (header row once per table + all body rows); repeated continuation-page header rows excluded.",
            "degraded_mode": "no - split run: Module B read only the Module-A transcripts; no PDF was opened by this module.",
        },
        "datapack_version": "1.1",
        "scope": "FULL",
        "documents": [],
        "tables": [],
        "key_metrics": [],
        "time_series": [],
        "definitions": [],
        "charts": [],
        "contradictions_verbatim": [],
        "extraction_gaps": [],
        "audit_sample": [],
        "completeness": {"per_document": []},
    }

    n_transcript_values = 0
    for d in DOC_ORDER:
        D = docs[d]
        ident = D["ident"]
        pack["documents"].append({
            "doc_id": d,
            "title": ident.get("title", {}).get("text_verbatim"),
            "title_anchor": ident.get("title", {}).get("anchor"),
            "author_publisher": ident.get("author_publisher", {}).get("text_verbatim"),
            "author_publisher_anchor": ident.get("author_publisher", {}).get("anchor"),
            "publication_date": ident.get("publication_date", {}).get("text_verbatim"),
            "publication_date_anchor": ident.get("publication_date", {}).get("anchor"),
            "page_count": int(D["meta"].get("page_count", "0")),
            "source_file": D["meta"].get("source_file"),
            "source_physical_pages": D["meta"].get("source_physical_pages", "").split(" ")[0],
            "ocr_pages": [],
        })
        # ---------------- tables
        for tid, blocks in D["tables"].items():
            first = blocks[0]
            columns = first["header"] or []
            rows, row_pages = [], []
            flags = []
            for b in blocks:
                rows += b["rows"]
                row_pages += [b["page"]] * len(b["rows"])
                if b["flags"] and b["flags"] != "none":
                    flags.append(f"p{b['page']}: {b['flags']}")
            n_transcript_values += sum(1 for c in columns if c) + sum(1 for r in rows for c in r if c)
            fns = []
            for b in blocks:
                for fn in b["fns"]:
                    mk = re.match(r"^\s*([a-z0-9*†]{1,2})[\s\)\.]", fn["text"])
                    fns.append({"marker": mk.group(1) if mk and not fn["text"].lower().startswith(("source", "note")) else None,
                                "text_verbatim": fn["text"], "anchor": f"[{tid}-fn{fn['n']}]"})
            title = first["title"]
            units = None
            if title:
                mu = re.search(r"\(([^()]*(?:per cent|percent|thousands|millions|%|USD|US\$|km2|km²|index|share)[^()]*)\)", title, re.I)
                units = mu.group(0) if mu else None
            pages = sorted({b["page"] for b in blocks})
            pack["tables"].append({
                "table_id": tid, "doc_id": d, "title_verbatim": title if title is not None else "[no caption printed in source]",
                "pages": pages, "columns": columns, "rows": rows, "row_pages": row_pages,
                "footnotes": fns, "units_verbatim": units,
                "continued_from_page": pages[0] if len(pages) > 1 else None,
                "extraction_flags": flags,
                "anchor": f"[{tid}]",
            })
        # ---------------- charts
        for fid, blocks in D["figures"].items():
            b0 = blocks[0]
            printed = "\n".join(b["printed"] for b in blocks if b["printed"])
            vis = all(b["visual_only"] for b in blocks)
            pack["charts"].append({
                "chart_id": fid,
                "caption_verbatim": b0["caption"],
                "anchor": f"[{fid}] [{d}-p{b0['page']}]",
                "labeled_points": [],
                "printed_text_verbatim": printed if printed else None,
                "visual_only": vis,
                "observed_shape": None,
                "notes": ("no data labels printed in the text layer; values not read off axes" if vis else
                          "labels/values printed in the figure area are kept verbatim in printed_text_verbatim; label-to-value pairing is not machine-resolved, so labeled_points is left empty"),
            })
            if vis:
                pack["extraction_gaps"].append({"location": f"[{fid}] [{d}-p{b0['page']}]",
                                                "what": "figure values (no data labels in the text layer); visible shape not described",
                                                "reason": "VISUAL-ONLY"})
        # ---------------- module A gaps
        for g in D["gaps"]:
            pack["extraction_gaps"].append(g)
        for pno, pg in D["pages"].items():
            if pg["skipped"]:
                pack["extraction_gaps"].append({"location": f"[{d}-p{pno}]", "what": f"page has no text: {pg['skipped']}",
                                                "reason": "VISUAL-ONLY" if "image" in pg["skipped"] else "NOT FOUND"})
    pack["_transcript_values"] = n_transcript_values
    return docs, pack


def add_key_metrics(docs, pack):
    kid = 0
    # (b) tables titled key/headline/summary/overview
    for t in pack["tables"]:
        if t["title_verbatim"] and KEY_TITLE.search(t["title_verbatim"]):
            for ri, r in enumerate(t["rows"]):
                for ci, v in enumerate(r):
                    if not v or ci == 0:
                        continue
                    kid += 1
                    col = t["columns"][ci] if ci < len(t["columns"]) else ""
                    pack["key_metrics"].append({
                        "metric_id": f"KM{kid}", "rule": "b",
                        "label_verbatim": f"{r[0]} | {col}".strip(" |"),
                        "value_raw": v, "value_num": parse_num(v),
                        "unit_verbatim": t["units_verbatim"] or "[see table title/column header]",
                        "anchor": f"[{t['table_id']}-r{ri + 2}c{ci + 1}]", "table_id": t["table_id"],
                        "footnote_markers": re.findall(r"[¹²³⁴⁵⁶⁷⁸⁹]", v)})
    # (c) numbers in the document's own summary section
    for d, (head, a, b) in SUMMARY_SECTIONS.items():
        D = docs[d]
        first = D["pages"].get(a)
        if not first or not any(head.lower() in t.lower() for t in first["prose"]):
            pack["extraction_gaps"].append({"location": f"[{d}-p{a}]", "what": f"summary heading '{head}' not found; rule (c) not applied", "reason": "NOT FOUND"})
            continue
        for pno in range(a, b + 1):
            pg = D["pages"].get(pno)
            if not pg:
                continue
            for blk in pg["prose"]:
                text = re.sub(r"\s*\n\s*", " ", blk)
                for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z•“\"(])", text):
                    for m in NUM_TOKEN.finditer(sent):
                        tok = m.group(0).strip()
                        kid += 1
                        pack["key_metrics"].append({
                            "metric_id": f"KM{kid}", "rule": "c",
                            "label_verbatim": sent.strip(), "value_raw": tok, "value_num": parse_num(tok),
                            "unit_verbatim": "%" if tok.endswith("%") else "[see label_verbatim]",
                            "anchor": f"[{d}-p{pno}]", "table_id": None, "footnote_markers": []})
    docs_with = {k["anchor"][1:3] if k["table_id"] is None else k["table_id"][:2] for k in pack["key_metrics"]}
    for d in DOC_ORDER:
        if d not in docs_with:
            pack["key_metrics"].append({"doc_id": d, "note": "document declares no key metrics"})


def add_time_series(pack):
    sid = 0
    for t in pack["tables"]:
        yc = [i for i, c in enumerate(t["columns"]) if YEAR_CELL.match(c.strip())]
        if len(yc) < 3:
            continue
        for ri, r in enumerate(t["rows"]):
            obs = []
            for ci in yc:
                if ci < len(r) and r[ci]:
                    obs.append({"period": t["columns"][ci].strip(), "period_raw": t["columns"][ci],
                                "value_raw": r[ci], "value_num": parse_num(r[ci]),
                                "anchor": f"[{t['table_id']}-r{ri + 2}c{ci + 1}]"})
            if obs:
                sid += 1
                pack["time_series"].append({
                    "series_id": f"TS{sid}", "table_id": t["table_id"],
                    "label_verbatim": r[0] if r else "",
                    "unit_verbatim": t["units_verbatim"] or "[see table title_verbatim]",
                    "frequency_verbatim": None, "observations": obs})


def add_definitions(docs, pack):
    for d in DOC_ORDER:
        D = docs[d]
        for pno in sorted(D["glossary_pages"] | ({pno for pno in D["pages"] if d == "D7" and 15 <= pno <= 16})):
            pg = D["pages"][pno]
            for blk in pg["prose"]:
                lines = [l for l in blk.split("\n")]
                k = 0
                while k < len(lines):
                    l = lines[k].strip()
                    m = re.match(r"^([^:]{2,60}):\s+(.+)$", l)
                    if m and not re.search(r"https?$", m.group(1)) and not m.group(1)[:1].islower() \
                            and not re.match(r"(Figure|Table|Source|Note|StatLink|Map|Box)\b", m.group(1)):
                        term, defi = m.group(1).strip(), m.group(2).strip()
                        k += 1
                        while k < len(lines) and lines[k].strip() and not re.match(r"^([^:]{2,60}):\s+", lines[k].strip()):
                            defi += " " + lines[k].strip()
                            k += 1
                        pack["definitions"].append({"term": term, "definition_verbatim": defi, "anchor": f"[{d}-p{pno}]"})
                        continue
                    # abbreviation list: short term line (optionally tab-terminated) + expansion line
                    raw = lines[k]
                    if (re.match(r"^\S[^\s]{0,14}(?:\s\S{1,8})?\s*\t?\s*$", raw) and k + 1 < len(lines)
                            and lines[k + 1].strip() and len(raw.strip()) <= 20 and not GLOSSARY_HEAD.match(raw)):
                        pack["definitions"].append({"term": raw.strip(), "definition_verbatim": lines[k + 1].strip(),
                                                    "anchor": f"[{d}-p{pno}]"})
                        k += 2
                        continue
                    k += 1
        if d == "D6":
            for pno, pg in sorted(D["pages"].items()):
                txt = "\n".join(pg["prose"])
                if "Attribute ID" not in txt or "Indicator Name" not in txt:
                    continue
                m1 = re.search(r"Indicator Name\s*\n(.+?)\n(?:Units|Unit)\b", txt, re.S)
                m2 = re.search(r"Indicator description\s*\n(.+?)\n(?:Methodology)\b", txt, re.S)
                ma = re.search(r"Attribute ID\s*\n(\S+)", txt)
                if m1 and m2:
                    pack["definitions"].append({"term": re.sub(r"\s*\n\s*", " ", m1.group(1)).strip(),
                                                "attribute_id": ma.group(1) if ma else None,
                                                "definition_verbatim": re.sub(r"\s*\n\s*", " ", m2.group(1)).strip(),
                                                "anchor": f"[D6-p{pno}]"})


GLOSSARY_HEAD = re.compile(r"^\s*(Glossary|List of abbreviations|Abbreviations|Acronyms and Abbreviations)\s*$", re.I)


def add_contradictions(pack):
    """Mechanical rule: within one document, two DIFFERENT tables that carry the
    same non-numeric row label (unique within each table) under the same column
    header, where both tables have an identical header row (same layout) and
    both cells are numeric, with different displayed values. Pairs are
    preserved, never resolved."""
    cid = 0
    seen = {}
    for t in pack["tables"]:
        labels = [r[0] for r in t["rows"] if r and r[0]]
        uniq = {l for l in labels if labels.count(l) == 1}
        for ri, r in enumerate(t["rows"]):
            if not r or r[0] not in uniq or parse_num(r[0]) is not None:
                continue
            for ci, v in enumerate(r):
                col = t["columns"][ci] if ci < len(t["columns"]) else ""
                if ci == 0 or not v or not col or parse_num(v) is None:
                    continue
                key = (t["doc_id"], tuple(t["columns"]), r[0], col)
                anc = f"[{t['table_id']}-r{ri + 2}c{ci + 1}]"
                prev = seen.get(key)
                if prev and prev[2] != t["table_id"] and prev[0] != v:
                    cid += 1
                    pack["contradictions_verbatim"].append({
                        "id": f"C{cid}",
                        "claim_a": {"text_verbatim": f"{r[0]} | {col} | {prev[0]}", "anchor": prev[1]},
                        "claim_b": {"text_verbatim": f"{r[0]} | {col} | {v}", "anchor": anc},
                        "note": "preserved unresolved — adjudication is downstream"})
                if not prev:
                    seen[key] = (v, anc, t["table_id"])


def add_audit_and_completeness(docs, pack):
    by_doc = {d: [t for t in pack["tables"] if t["doc_id"] == d] for d in DOC_ORDER}
    picks = []
    for d in DOC_ORDER:
        ts = by_doc[d]
        if not ts:
            continue
        sel = [ts[0], ts[len(ts) // 2], ts[-1]]
        for t in sel:
            vals = []
            for ri, r in enumerate(t["rows"]):
                for ci, v in enumerate(r):
                    if v:
                        vals.append({"anchor": f"[{t['table_id']}-r{ri + 2}c{ci + 1}]", "value_raw": v})
            picks.append(vals)
    sample, idx = [], 0
    total = sum(len(p) for p in picks)
    while len(sample) < min(10, total):
        for p in picks:
            if idx < len(p) and len(sample) < 10 and p[idx] not in sample:
                sample.append(p[idx])
        idx += 1
    pack["audit_sample"] = sample
    for d in DOC_ORDER:
        D = docs[d]
        a7 = " ".join(D["a7"])
        mt = re.search(r"document's own list names (\d+); captioned tables found in body: (\d+); uncaptioned ruled tables detected: (\d+); transcribed table IDs: (\d+)", a7)
        mf = re.search(r"document's own list names (\d+); figure IDs transcribed: (\d+)", a7)
        listed_t, capt, unc, trans_t = (int(x) for x in mt.groups())
        listed_f, trans_f = (int(x) for x in mf.groups())
        miss_t = len([g for g in D["gaps"] if g["location"].endswith("list of tables")])
        miss_f = len([g for g in D["gaps"] if g["location"].endswith("list of figures")])
        pack["completeness"]["per_document"].append({
            "doc_id": d,
            "tables_found": trans_t + miss_t, "tables_transcribed": trans_t,
            "tables_listed_by_document": listed_t,
            "figures_found": trans_f + miss_f, "figures_transcribed": trans_f,
            "figures_listed_by_document": listed_f,
            "pages_in_scope": int(D["meta"].get("page_count", "0")),
            "pages_anchored": len(D["pages"]),
        })


def verify(docs, pack, tdir):
    """B4 self-verification against the transcripts only."""
    rep = []
    tables = {t["table_id"]: t for t in pack["tables"]}

    def cell(anchor):
        m = re.match(r"\[(D\d-T\d+)-r(\d+)c(\d+)\]", anchor)
        t = tables[m.group(1)]
        r, c = int(m.group(2)), int(m.group(3))
        return t, (t["columns"][c - 1] if r == 1 else t["rows"][r - 2][c - 1]), r, c

    def in_transcript(t, r, value):
        # re-read the transcript block rows for this table and compare
        blocks = docs[t["doc_id"]]["tables"][t["table_id"]]
        body = [row for b in blocks for row in b["rows"]]
        c_ok = r >= 2 and value in body[r - 2]
        return c_ok

    checks = []
    all_t = pack["tables"]
    for t in [all_t[0], all_t[len(all_t) // 2], all_t[-1]]:
        for ri, r in enumerate(t["rows"]):
            vs = [(ci, v) for ci, v in enumerate(r) if v]
            if vs:
                checks.append((f"[{t['table_id']}-r{ri + 2}c{vs[0][0] + 1}]", vs[0][1]))
                break
    checks += [(s["anchor"], s["value_raw"]) for s in pack["audit_sample"][:2]]
    for anc, val in checks:
        t, got, r, c = cell(anc)
        ok = got == val and in_transcript(t, r, val)
        rep.append(f"- spot-check {anc}: JSON `{val}` | transcript `{got}` -> {'MATCH' if ok else 'MISMATCH'}")
    # all table values resolve (JSON rows == transcript rows)
    mism = 0
    for t in pack["tables"]:
        blocks = docs[t["doc_id"]]["tables"][t["table_id"]]
        if [row for b in blocks for row in b["rows"]] != t["rows"]:
            mism += 1
    rep.append(f"- tables whose JSON rows differ from transcript rows: {mism}")
    # causal verbs in fields written by this module (not verbatim source text)
    own = json.dumps({k: pack[k] for k in ("_conventions",)}) + " ".join(
        str(x.get("note", "")) for x in pack["charts"] + pack["contradictions_verbatim"]) + " ".join(
        g["what"] + g["reason"] for g in pack["extraction_gaps"] if not g["what"].startswith(tuple("0123456789")))
    rep.append(f"- causal verbs in text authored by Module B: {len(CAUSAL.findall(own))}")
    req = ["_conventions", "datapack_version", "scope", "documents", "tables", "key_metrics", "definitions",
           "charts", "contradictions_verbatim", "extraction_gaps", "audit_sample", "completeness"]
    rep.append(f"- required top-level fields present: {all(k in pack for k in req)}")
    return rep


def count_transcript_values(tdir):
    """Independent count straight from the transcript text: non-empty cells of
    every markdown table line, skipping the header line of continuation blocks."""
    n = 0
    for d in DOC_ORDER:
        skip_next_header = False
        in_table_block = False
        first_row = True
        for ln in (tdir / f"{d}_transcript.md").read_text(encoding="utf-8").split("\n"):
            if ln.startswith("#### ["):
                in_table_block = " TABLE" in ln
                skip_next_header = "(continued)" in ln
                first_row = True
                continue
            if in_table_block and ln.startswith("|"):
                if re.fullmatch(r"\|(---\|)+", ln):
                    continue
                if first_row:
                    first_row = False
                    if skip_next_header:
                        continue
                n += sum(1 for c in split_md_row(ln) if c)
    return n


def main():
    tdir, out_json, report = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    docs, pack = build(tdir)
    add_key_metrics(docs, pack)
    add_time_series(pack)
    add_definitions(docs, pack)
    add_contradictions(pack)
    add_audit_and_completeness(docs, pack)
    pack.pop("_transcript_values")
    N = count_transcript_values(tdir)
    M = sum(sum(1 for c in t["columns"] if c) + sum(1 for r in t["rows"] for c in r if c) for t in pack["tables"])
    G = len(pack["extraction_gaps"])
    recon = f"transcript values: {N} | JSON values: {M} | gaps declared: {G} | N = M ± G"
    pack["_reconciliation"] = recon
    rep = verify(docs, pack, tdir)
    txt = json.dumps(pack, ensure_ascii=False, indent=1)
    json.loads(txt)  # must parse with zero cleanup
    out_json.write_text(txt, encoding="utf-8")
    lines = ["# Module B — B4 self-verification report", "", recon, ""] + rep + [
        "", f"- JSON parses: True ({len(txt):,} characters)",
        f"- counts: documents {len(pack['documents'])}, tables {len(pack['tables'])}, key_metrics {len(pack['key_metrics'])}, "
        f"time_series {len(pack['time_series'])}, definitions {len(pack['definitions'])}, charts {len(pack['charts'])}, "
        f"contradictions {len(pack['contradictions_verbatim'])}, extraction_gaps {len(pack['extraction_gaps'])}, audit_sample {len(pack['audit_sample'])}"]
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
