# City Data — PDF-DATAPACK v1.1 (lossless extraction for machine analysis)

This folder holds the output of **"Run PDF-DATAPACK on [the 4 uploaded archives] with scope FULL"**.
It was run as a split run:

1. **Module A (transcribe)** read the PDFs and wrote one anchored markdown transcript per document. These are frozen in `module_a_transcripts/`.
2. **Module B (structure)** read **only** those transcripts and wrote the JSON data pack in `module_b_datapack/`. The script `tools/module_b_structure.py` never opens a PDF, so the quarantine is structural. The pack is marked "degraded mode: no".

Nothing here is analysis. No values are rounded, converted, filled in, or adjudicated. Every loss is declared in `extraction_gaps`.

## Documents (doc_id in supply order)

| doc_id | Source file (upload part) | Physical pages | Title (verbatim, anchored) |
|---|---|---|---|
| D1 | `City Data Combined .pdf` (part 1) | 1–25 | Global Innovation Index 2025 Ranking of World's Top 100 Innovation Clusters `[D1-p1]` (WIPO) |
| D2 | `City Data Combined .pdf` (part 1) | 26–149 | World Urbanization Prospects 2025 Summary of Results `[D2-p28]` (UN DESA) |
| D3 | `City Data Combined .pdf` (part 1) | 150–158 | Statistical release: BIS residential property price statistics in Q1 2026 `[D3-p150]` |
| D4 | `f42db3bf-en.pdf` (part 2) | 1–140 | OECD Regions and Cities at a Glance 2024 `[D4-p4]` |
| D5 | `Oxford_Economics_2026_Global_Cities_Index.pdf` (part 3) | 1–155 | OXFORD ECONOMICS GLOBAL CITIES INDEX `[D5-p1]` |
| D6 | `GHSL_UCDB_R2024.pdf` (part 3) | 1–633 | Stats in the City – the GHSL Urban Centre Database 2025 `[D6-p1]` (EC JRC) |
| D7 | `wcr2024_-_full_report.pdf` (part 4) | 1–373 | Cities and Climate Action World Cities Report 2024 `[D7-p3]` (UN-Habitat) |

The combined PDF contains three separately published reports, so it is split into D1–D3. Numbers are never merged across documents.

Source file SHA-256 hashes (so the analyst can confirm they are auditing the same files):

```
e755c96a450586061da857eeee5a56537dcff1186d9a4a7d81a0d24a94f3b229  City Data Combined .pdf
e059238b9c81709826b047e41cd6db5dcee20e5533c459a8cbeecf06c8ad89b1  f42db3bf-en.pdf
85114589924608b3d29e426abe0e32457a1a30b31b706f5bb2fa79ca7b3ae92b  Oxford_Economics_2026_Global_Cities_Index.pdf
93eae10d69dd9c5174fe9fb348495250f6d3e7b73987873c483e689893b51cc5  GHSL_UCDB_R2024.pdf
106dc4f3f91d6390efae26ea507bef4b091c65d64289de9e084608f539fb43ad  wcr2024_-_full_report.pdf
```

The PDFs themselves are not committed (about 140 MB).

## Folder layout

```
City Data/
├── README.md                          this file
├── module_a_transcripts/D1..D7_transcript.md
│     metadata + document identification, running headers noted once,
│     every page in order ([Dn-pN]), tables ([Dn-Tk]) as markdown with
│     footnotes ([Dn-Tk-fnM]), figures ([Dn-Fk]) with caption + printed
│     labels, glossary pages flagged, A7 checklist, declared gaps
├── module_b_datapack/datapack.json    the frozen JSON data pack (schema v1.1)
├── module_b_datapack/B4_verification_report.md
└── tools/module_a_transcribe.py, tools/module_b_structure.py (reproducible pipeline)
```

## Locator convention (stable across transcript and JSON)

- `[D2-p119]`: document D2, **physical** page 119 of the supplied source file. D1–D3 use the page numbers of the combined PDF.
- `[D2-T5]`: table 5 of D2, numbered in document order. A multi-page table keeps one ID, and each later page is marked `[D2-T5 continued → p120]`.
- `[D2-T5-r4c2]`: row 4, column 2 of that table.
  - r1 is the header row. Body rows are numbered r2, r3, … continuously across continuation pages; header rows repeated on those pages are not counted.
  - In the JSON, `rows[X-2][Y-1]` is cell rXcY, and `row_pages[X-2]` gives the page it came from.
- `[D2-F3]`: figure, map or graph 3 of D2.

## Reconciliation line (§7)

```
transcript values: 48915 | JSON values: 48915 | gaps declared: 200 | N = M ± G
```

"Values" are non-empty table cells: the header row once per table, plus all body rows. N is counted directly from the transcript markdown by an independent routine; M is counted from the JSON. Prose numbers are anchored per page in the transcripts but are not table values.

## Completeness and B4 results

| doc | pages anchored | tables found / transcribed | figures found / transcribed | document's own list |
|---|---|---|---|---|
| D1 | 25/25 | 6 / 6 | 7 / 7 | — |
| D2 | 124/124 | 8 / 8 | 32 / 32 | list of boxes only |
| D3 | 9/9 | 0 / 0 | 13 / 13 | — |
| D4 | 140/140 | 39 / 39 | 115 / 115 | — |
| D5 | 155/155 | 5 / 5 | 0 / 0 | — |
| D6 | 633/633 | 3 / 3 | 5 / 5 | names 3 tables, 5 figures: all found |
| D7 | 373/373 | 47 / 47 | 108 / 108 | parsed 36 table labels, 106 figure labels: all found |

- B4 spot-checks against the transcript: 5/5 match.
- JSON table rows differ from transcript rows: 0 tables.
- The JSON parses; all required fields are present.
- Causal verbs in text written by the modules: 0.
- A separate QA pass compared 50 cells, including the 10-value `audit_sample`, to the PDF text. All 50 are present on the cited page; two needed whitespace-insensitive matching (a narrow no-break thousands separator, kept verbatim, and a wrapped cell).

JSON contents:

| Field | Count |
|---|---|
| tables | 108 |
| key_metrics | 7,279 |
| time_series | 384 |
| definitions | 756 |
| charts | 279 |
| contradictions_verbatim | 0 |
| extraction_gaps | 200 |
| audit_sample | 10 |

## What was declared rather than silently handled (read before analysis)

- **Hidden text excluded.** D1 pp. 6, 19, 21 and 23 and D7 p. 346 contain old table values that are in the PDF text layer but are **not displayed**. They are painted over by white shapes drawn later, clipped away, or placed off the page. Example: D1 p. 21 carries a stale rounded copy of the Top-100 table ("1,475" next to the displayed "1,474.75").
  - Only displayed text was transcribed.
  - A further 31 pages had clipped or off-page text excluded by clip-aware extraction, such as dot leaders in contents pages and chart labels placed off the page.
  - Each exclusion (36 pages in total) is a gap entry with reason `OUT-OF-SCOPE`.
  - Pixel checks against the rendered page make sure visible text on coloured or transparent backgrounds is not dropped.
- **Figures.**
  - Printed labels and values inside a figure area are kept verbatim in `printed_text_verbatim`. Pairing labels to values is **not** machine-resolved, so `labeled_points` is empty.
  - 148 figures have no data labels in the text layer. That is all 108 raster charts in the OECD report, 38 in D7 and 2 in D1.
  - These are `visual_only: true` with a `VISUAL-ONLY` gap. Values were **not** read off axes, and `observed_shape` was not filled in; this is declared as a gap.
  - Most OECD figures carry a StatLink URL (in the transcript) pointing to their underlying data.
- **Table geometry flags.** Tables are rebuilt from word positions. Every table carries `extraction_flags`:
  - Wrapped cell lines are joined verbatim, based on line pitch.
  - Multi-line headers are joined per column. These are marked `[AMBIGUOUS]` because a label printed across several columns, such as a year over a column group, sits in one column.
  - Strings that span several columns are marked `[merged in source]`.
  - 13 table blocks with no machine-resolvable column structure are kept as single-column rows and flagged.
- **D5 (Oxford Economics)** has no figure captions. Its charts are not registered as figures; their printed labels and values stay in page-anchored prose. The 1,000-city ranking, pp. 115–154, is table `D5-T5`.
- **D6 (GHSL)** is mostly indicator fact sheets. They are transcribed verbatim as page text and also lifted into `definitions`: 491 entries with `attribute_id`, term = Indicator Name, definition = Indicator description.
- **Key metrics** follow the mechanical rule in `_conventions.key_metrics_rule`:
  - (a) Callout boxes are not machine-identifiable, so none are emitted.
  - (b) Tables the document titles key, headline, summary or overview. This includes the WUP annex tables "Key population / built-up / urban indicators…", which is why there are about 6,500 such entries.
  - (c) Every number in the document's own summary section: D2 Key messages, D3 Summary of latest developments, D4 Executive summary, D6 Abstract, D7 Key Findings and Messages.
  - D1 and D5 have no titled summary section.
- **Contradictions.** The mechanical rule (same row and column label in two same-layout tables, with different numbers) found none. Semantic contradiction screening is left to the analyst.

## Handoff

> Run FULL-ANALYSIS on [TOPIC] using [`City Data/module_b_datapack/datapack.json` + `City Data/module_a_transcripts/`].

- The analyst re-verifies `audit_sample` (10 values) against the PDFs and proceeds only on 10/10.
- The pack is frozen. If a defect is found, re-run the defective module with the scripts in `tools/`; do not patch numbers.

## Reproduce

```
pip install pymupdf
python3 tools/module_a_transcribe.py <dir with the 5 PDFs> module_a_transcripts
python3 tools/module_b_structure.py module_a_transcripts module_b_datapack/datapack.json module_b_datapack/B4_verification_report.md
```
