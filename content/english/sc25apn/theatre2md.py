#!/usr/bin/env python3
import argparse
import re
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import html
import pandas as pd

# --------------------------
# Configuration
# --------------------------
TZNAME = "America/Chicago"                 # St. Louis
TZ = ZoneInfo(TZNAME)
YEAR = 2025                                # SC25
CONF_MONTH = 11                            # November
CONF_DATES = set(range(16, 22))            # Nov 16–21 inclusive
ICS_DIR = Path("ics")                      # Local output directory for .ics
ICS_URL_PREFIX = "/sc25/theatreics"                     # URL prefix used in Markdown links (no leading slash = relative)
LOCATION_STR = "AWS Booth #2207 in SC25 Expo"
TITLE_FMT = "{partner} Builder Session @ AWS Booth Theatre #2207 — {pod}"
DESCRIPTION_FMT = "Builder session in the AWS Booth Theatre at SC25 in St. Louis."
EMPTY_CELL_DISPLAY = ""                    # or "—"

_MONTH_TOKENS = {"no", "nov"}

# Accepts "No-17 10.00-11.00", "Nov-17 3pm-4pm", "Nov 17 11:30 a.m.-12:15 p.m."
TIME_PAT = re.compile(
    r"""
    ^\s*
    (?P<mon>[A-Za-z]{2,3})[-\s]?(?P<day>\d{1,2})
    \s+
    (?P<start>\d{1,2}(?:[:\.]\d{2})?)\s*(?P<start_ampm>[AaPp]\.?\s*[Mm]\.?)?
    \s*[-–]\s*
    (?P<end>\d{1,2}(?:[:\.]\d{2})?)\s*(?P<end_ampm>[AaPp]\.?\s*[Mm]\.?)?
    \s*$
    """,
    re.VERBOSE,
)

def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")

def parse_slot(cell: str) -> tuple[datetime, datetime]:
    if not isinstance(cell, str):
        raise ValueError(f"Time cell must be string, got {type(cell)}: {cell!r}")

    m = TIME_PAT.match(cell.strip())
    if not m:
        raise ValueError(f"Unrecognized time format: {cell!r}")

    mon = m.group("mon").lower()
    day = int(m.group("day"))
    if mon not in _MONTH_TOKENS and not mon.startswith("no"):
        raise ValueError(f"Month token not recognized as November: {mon!r}")

    def parse_time_token(token: str, ampm_raw: str | None) -> datetime:
        token = token.replace(".", ":").strip()
        if ":" not in token:
            token = token + ":00"
        hour, minute = map(int, token.split(":"))
        if ampm_raw:
            ampm = re.sub(r"[^aApPmM]", "", ampm_raw).lower()
            if ampm.startswith("p") and hour < 12:
                hour += 12
            elif ampm.startswith("a") and hour == 12:
                hour = 0
        return datetime(YEAR, CONF_MONTH, day, hour, minute, tzinfo=TZ)

    start_dt = parse_time_token(m.group("start"), m.group("start_ampm"))
    end_dt = parse_time_token(m.group("end"), m.group("end_ampm"))
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)
    return start_dt, end_dt

def ics_datetime(dt: datetime) -> str:
    return dt.strftime("%Y%m%dT%H%M%S")

def write_ics(ics_path: Path, uid: str, summary: str, description: str, start: datetime, end: datetime, location: str):
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//SC25 Demo Schedule//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
        f"DTSTART;TZID={TZNAME}:{ics_datetime(start)}",
        f"DTEND;TZID={TZNAME}:{ics_datetime(end)}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
        f"LOCATION:{location}",
        "END:VEVENT",
        "END:VCALENDAR",
        "",
    ]
    ics_path.parent.mkdir(parents=True, exist_ok=True)
    ics_path.write_text("\n".join(lines), encoding="utf-8")

def format_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    md = []
    md.append("| " + " | ".join(headers) + " |")
    md.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        md.append("| " + " | ".join(r) + " |")
    return "\n".join(md) + "\n"

def main():
    ap = argparse.ArgumentParser(description="Generate Markdown + ICS for demo schedule.")
    ap.add_argument("excel_path", help="Path to the Excel schedule file")
    ap.add_argument("--sheet", default=0, help="Sheet name or index (default: first sheet)")
    args = ap.parse_args()

    excel_path = Path(args.excel_path)
    sheet = int(args.sheet) if str(args.sheet).isdigit() else args.sheet

    df = pd.read_excel(excel_path, sheet_name=sheet, header=0)
    df_cols = [str(c).strip() for c in df.columns]
    df.columns = df_cols

    time_col = df_cols[0]
    pod_cols = df_cols[1:]

    slots = []
    for idx, row in df.iterrows():
        start_dt, end_dt = parse_slot(str(row[time_col]))
        slots.append((idx, start_dt, end_dt))

    slots.sort(key=lambda x: x[1])
    idx_order = [i for i, _, _ in slots]
    start_by_idx = {i: s for i, s, _ in slots}
    end_by_idx = {i: e for i, _, e in slots}
    pos_by_idx = {idx: pos for pos, idx in enumerate(idx_order)}

    ICS_DIR.mkdir(parents=True, exist_ok=True)
    cell_link: dict[tuple[int, str], str] = {}

    for pod in pod_cols:
        current_partner_norm = None
        current_partner_raw = None
        run_start_idx = None
        run_end_idx = None

        def close_run():
            if run_start_idx is None:
                return
            start_dt = start_by_idx[run_start_idx]
            end_dt = end_by_idx[run_end_idx]
            partner = current_partner_raw
            pod_name = pod

            date_slug = start_dt.strftime("%Y%m%d")
            end_date_slug = end_dt.strftime("%Y%m%d")
            start_slug = start_dt.strftime("%H%M")
            end_slug = end_dt.strftime("%H%M")
            pod_slug = slugify(pod_name)
            partner_slug = slugify(partner)

            if end_date_slug != date_slug:
                base = f"{date_slug}-{start_slug}_to_{end_date_slug}-{end_slug}"
            else:
                base = f"{date_slug}-{start_slug}-{end_slug}"

            ics_filename = f"{base}-{pod_slug}-{partner_slug}.ics"
            ics_path = ICS_DIR / ics_filename
            ics_url = f"{ICS_URL_PREFIX.rstrip('/')}/{ics_filename}"

            summary = TITLE_FMT.format(partner=partner, pod=pod_name)
            description = DESCRIPTION_FMT.format(partner=partner, pod=pod_name)
            uid = f"{base}-{pod_slug}-{partner_slug}@sc25"
            write_ics(
                ics_path=ics_path,
                uid=uid,
                summary=summary,
                description=description,
                start=start_dt,
                end=end_dt,
                location=LOCATION_STR,
            )

            start_pos = pos_by_idx[run_start_idx]
            end_pos = pos_by_idx[run_end_idx]
            for pos in range(start_pos, end_pos + 1):
                row_idx = idx_order[pos]
                cell_link[(row_idx, pod_name)] = ics_url

        for row_idx in idx_order:
            cell_val = df.loc[row_idx, pod]
            partner_raw = "" if pd.isna(cell_val) else str(cell_val).strip()
            partner_norm = partner_raw.lower()

            if partner_norm and current_partner_norm is None:
                current_partner_norm = partner_norm
                current_partner_raw = partner_raw
                run_start_idx = run_end_idx = row_idx
            elif partner_norm and partner_norm == current_partner_norm:
                run_end_idx = row_idx
            else:
                if current_partner_norm is not None:
                    close_run()
                if partner_norm:
                    current_partner_norm = partner_norm
                    current_partner_raw = partner_raw
                    run_start_idx = run_end_idx = row_idx
                else:
                    current_partner_norm = None
                    current_partner_raw = None
                    run_start_idx = run_end_idx = None

        if current_partner_norm is not None:
            close_run()

    headers = ["Time"] + pod_cols
    rows_md = []

    for row_idx in idx_order:
        start_dt = start_by_idx[row_idx]
        end_dt = end_by_idx[row_idx]
        time_label = f"{start_dt.strftime('%b %d %H:%M')}–{end_dt.strftime('%H:%M')} ({TZNAME})"

        md_row = [time_label]
        for pod in pod_cols:
            cell_val = df.loc[row_idx, pod]
            partner = "" if pd.isna(cell_val) else str(cell_val).strip()
            if not partner:
                md_row.append(EMPTY_CELL_DISPLAY)
                continue
            safe_partner = html.escape(partner)
            link = cell_link.get((row_idx, pod))
            md_row.append(f"[{safe_partner}]({link})" if link else safe_partner)
        rows_md.append(md_row)

    md_table = format_markdown_table(headers, rows_md)
    out_md = Path(excel_path.stem + ".md")
    out_md.write_text(md_table, encoding="utf-8")
    print(f"Wrote Markdown: {out_md.resolve()}")
    print(f"Wrote ICS files to: {ICS_DIR.resolve()}")
    print(f"ICS URL prefix used: {ICS_URL_PREFIX}")

if __name__ == "__main__":
    main()