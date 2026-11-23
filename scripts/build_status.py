"""Build the Integration Status page and the Excel workbook from the CSV files.

Source of truth: docs/data/endpoints-reviewed.csv (edit this, then rerun).
Outputs:
  docs/integration-status.md
  docs/data/gocare-endpoints-review.xlsx

Usage (from the repo root):  python scripts/build_status.py
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"
REVIEWED = DATA / "endpoints-reviewed.csv"
ORIGINAL = DATA / "endpoints-original.csv"
PAGE = ROOT / "docs" / "integration-status.md"
XLSX = DATA / "gocare-endpoints-review.xlsx"

STATUSES = [
    ("Live", "Used on the website today.", "C6EFCE"),
    ("In testing", "Works, but not released to customers yet.", "FFEB9C"),
    ("Needs frontend", "Backend works; the website does not call it yet.", "DDEBF7"),
    ("Built, not working in tested env", "Code exists, but it failed or was missing on the environment that was tested.", "FCE4D6"),
    ("Built, off by default", "Code exists behind a feature flag that is off.", "EDEDED"),
    ("Not built", "No code found.", "F4B6B6"),
]


def read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if (r.get("#") or "").strip().isdigit()]


def md_cell(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ")


def code(text: str) -> str:
    return f"`{text}`" if text else ""


def build_page(rows: list[dict[str, str]]) -> str:
    counts = Counter(r["Reviewed status"] for r in rows)
    changed = [r for r in rows if r["Reviewed status"] != reported_status(r)]
    out = [
        "# Integration Status",
        "",
        "Status of every GoCare AI endpoint, based on the endpoint testing sheet and checked against the code "
        "in `Adwat/GoCare-Agents` and `Adwat/Gocare-Product-Recommendation-System` (branches `dev` and `test`) on 21 Nov 2026.",
        "",
        "**Downloads:** [Excel workbook](data/gocare-endpoints-review.xlsx) · "
        "[Reviewed sheet (CSV)](data/endpoints-reviewed.csv) · [Original testing sheet (CSV)](data/endpoints-original.csv)",
        "",
        "## Summary",
        "",
        f"**{counts['Live']} of {len(rows)}** endpoints are live, and all of them are internal catalog tools "
        "(audit, enhancement, duplicate detection). **No customer-facing AI is live yet:** the chat and everything "
        "inside it is in testing, and the recommendation endpoints are not called by the website.",
        "",
        "| Status | Count | Meaning |",
        "|---|---|---|",
    ]
    for name, meaning, _ in STATUSES:
        out.append(f"| {name} | {counts.get(name, 0)} | {meaning} |")
    out += [f"| **Total** | **{len(rows)}** | |", ""]

    out += [
        "## Release status by branch",
        "",
        "Before anything is called \"in production\", agree which branch and environment production is:",
        "",
        "| Repo | `main` | `test` | `dev` |",
        "|---|---|---|---|",
        "| GoCare-Agents | v0.1 (16 Nov 2025) | v0.5.4 (23 Sep 2026) | v0.5.4+ (29 Oct 2026) |",
        "| Recommendation System | v1.4.0 (31 Dec 2025) | v1.8.0 (21 Aug 2026) | v1.8.0+ (29 Oct 2026) |",
        "",
        "In both repos, the production deploy workflow (`deploy-prod.yml`, on `test` and `dev`) runs on pushes to `main`. "
        "But it has never been merged into `main`, which is still v0.1 and v1.4.0. So production is deployed some "
        "other way, and the repos can't tell you which version it runs. The testing sheet doesn't say which environment "
        "was tested either, which is the likely reason some built endpoints showed as missing.",
        "",
        "## Changes from the original sheet",
        "",
        "| # | Feature | Sheet said (exists / correct / on website) | Reviewed status | Why |",
        "|---|---|---|---|---|",
    ]
    for r in changed:
        said = f"{r['Reported: endpoint exists?']} / {r['Reported: correct result?']} / {r['Reported: used on website?']}"
        out.append(f"| {r['#']} | {md_cell(r['Feature'])} | {md_cell(said)} | **{r['Reviewed status']}** | {md_cell(r['Code check (21 Nov 2026)'])} |")
    out += ["", "Rows #3, #4, #5 and #9 are missing from the original sheet. Confirm whether they were dropped or merged.", ""]

    for name, meaning, _ in STATUSES:
        group = [r for r in rows if r["Reviewed status"] == name]
        if not group:
            continue
        out += [f"## {name} ({len(group)})", "", meaning, "",
                "| # | Feature | Endpoint | Code check | Next action | Owner |",
                "|---|---|---|---|---|---|"]
        for r in group:
            out.append(
                f"| {r['#']} | {md_cell(r['Feature'])} | {code(r['Method'] + ' ' + r['Endpoint'])} | "
                f"{md_cell(r['Code check (21 Nov 2026)'])} | {md_cell(r['Next action'])} | {md_cell(r['Owner']) or '—'} |"
            )
        out.append("")
    out += [
        "## How to update this page",
        "",
        "Edit `docs/data/endpoints-reviewed.csv`, then run `python scripts/build_status.py`. "
        "The script rebuilds this page and the Excel workbook.",
        "",
    ]
    return "\n".join(out)


def reported_status(r: dict[str, str]) -> str:
    web = r["Reported: used on website?"].strip().lower()
    if web == "yes":
        return "Live"
    if web == "on testing":
        return "In testing"
    if web.startswith("need frontend"):
        return "Needs frontend"
    return "Not built"


THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HEAD_FILL = PatternFill("solid", start_color="1F3864")
HEAD_FONT = Font(name="Arial", bold=True, color="FFFFFF")
BODY_FONT = Font(name="Arial", size=10)
INPUT_FILL = PatternFill("solid", start_color="FFFF00")


def write_table(ws, header: list[str], rows: list[list[str]], widths: dict[int, int]) -> None:
    ws.append(header)
    for c in ws[1]:
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
        c.alignment = Alignment(wrap_text=True, vertical="center")
    for row in rows:
        ws.append([int(v) if i == 0 and v.isdigit() else v for i, v in enumerate(row)])
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.font, c.border = BODY_FONT, BORDER
            c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, w in widths.items():
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "C2"
    ws.auto_filter.ref = ws.dimensions


def build_xlsx(rows: list[dict[str, str]], original: list[dict[str, str]]) -> None:
    wb = Workbook()

    # --- Reviewed sheet -----------------------------------------------------
    ws = wb.active
    ws.title = "Reviewed"
    header = list(rows[0].keys())
    write_table(ws, header, [[r[h] for h in header] for r in rows],
                {1: 5, 2: 26, 3: 14, 4: 8, 5: 34, 6: 11, 7: 11, 8: 14, 9: 22, 10: 55, 11: 45, 12: 14, 13: 12, 14: 40, 15: 45})
    n = len(rows) + 1
    status_col = get_column_letter(header.index("Reviewed status") + 1)
    dv = DataValidation(type="list", formula1="=Legend!$A$2:$A$%d" % (len(STATUSES) + 1), allow_blank=False)
    ws.add_data_validation(dv)
    dv.add(f"{status_col}2:{status_col}{n}")
    for name, _, color in STATUSES:
        ws.conditional_formatting.add(
            f"{status_col}2:{status_col}{n}",
            FormulaRule(formula=[f'${status_col}2="{name}"'], fill=PatternFill("solid", start_color=color)),
        )
    for col in ("Owner", "Target date"):
        letter = get_column_letter(header.index(col) + 1)
        for r in range(2, n + 1):
            ws[f"{letter}{r}"].fill = INPUT_FILL
        ws[f"{letter}1"].fill = PatternFill("solid", start_color="7F6000")

    # --- Summary sheet ------------------------------------------------------
    sm = wb.create_sheet("Summary", 0)
    sm["A1"] = "GoCare AI endpoints: reviewed status"
    sm["A1"].font = Font(name="Arial", bold=True, size=14)
    sm["A2"] = "Counts update automatically from the Reviewed sheet (column %s)." % status_col
    sm["A2"].font = Font(name="Arial", italic=True, size=9, color="595959")
    sm.append([])
    sm.append(["Status", "Count", "Share"])
    for c in sm[4]:
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
    first = 5
    for i, (name, _, color) in enumerate(STATUSES):
        r = first + i
        sm[f"A{r}"] = name
        sm[f"B{r}"] = f"=COUNTIF(Reviewed!${status_col}$2:${status_col}${n},A{r})"
        sm[f"C{r}"] = f"=IF($B${first + len(STATUSES)}=0,0,B{r}/$B${first + len(STATUSES)})"
        sm[f"C{r}"].number_format = "0%"
        sm[f"A{r}"].fill = PatternFill("solid", start_color=color)
    tot = first + len(STATUSES)
    sm[f"A{tot}"] = "Total"
    sm[f"B{tot}"] = f"=SUM(B{first}:B{tot - 1})"
    sm[f"C{tot}"] = f"=IF(B{tot}=0,0,B{tot}/B{tot})"
    sm[f"C{tot}"].number_format = "0%"
    sm[f"A{tot + 1}"] = "Check: rows in Reviewed sheet"
    sm[f"B{tot + 1}"] = f"=COUNTA(Reviewed!$A$2:$A${n})"
    for row in sm.iter_rows(min_row=first, max_row=tot + 1, max_col=3):
        for c in row:
            c.border = BORDER
            c.font = Font(name="Arial", bold=(c.row == tot))
    sm[f"A{tot + 3}"] = "Customer-facing AI live: none. The chat is in testing and recommendations need frontend work."
    sm[f"A{tot + 3}"].font = Font(name="Arial", bold=True, color="C00000")
    sm.column_dimensions["A"].width = 34
    sm.column_dimensions["B"].width = 10
    sm.column_dimensions["C"].width = 10

    # --- Legend -------------------------------------------------------------
    lg = wb.create_sheet("Legend")
    lg.append(["Status", "Meaning"])
    for c in lg[1]:
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
    for name, meaning, color in STATUSES:
        lg.append([name, meaning])
        lg.cell(lg.max_row, 1).fill = PatternFill("solid", start_color=color)
    lg.append([])
    lg.append(["How to fill", "Yellow cells (Owner, Target date) on the Reviewed sheet are for you to fill. "
               "Pick Reviewed status from the dropdown. Example: Owner = Shams, Target date = 2026-12-05."])
    lg.append(["Source", "Original testing sheet by Shams Abdelhalim; code check on 21 Nov 2026 against the "
               "dev and test branches of Adwat/GoCare-Agents and Adwat/Gocare-Product-Recommendation-System."])
    for row in lg.iter_rows():
        for c in row:
            if c.row > 1:
                c.font = Font(name="Arial", size=10, bold=c.column == 1)
            c.alignment = Alignment(wrap_text=True, vertical="top")
    lg.column_dimensions["A"].width = 30
    lg.column_dimensions["B"].width = 90

    # --- Original, unchanged -----------------------------------------------
    og = wb.create_sheet("Original (Shams)")
    oh = list(original[0].keys())
    write_table(og, oh, [[r[h] for h in oh] for r in original],
                {1: 5, 2: 26, 3: 14, 4: 8, 5: 34, 6: 11, 7: 11, 8: 14, 9: 50, 10: 50})

    wb.save(XLSX)


def main() -> None:
    rows, original = read(REVIEWED), read(ORIGINAL)
    PAGE.write_text(build_page(rows), encoding="utf-8")
    build_xlsx(rows, original)
    print(f"wrote {PAGE.relative_to(ROOT)} and {XLSX.relative_to(ROOT)} ({len(rows)} endpoints)")


if __name__ == "__main__":
    main()
