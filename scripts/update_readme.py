import json
import os
import re
import sys
import urllib.request
from datetime import date, datetime

BASE = "https://smet.cz/nrd/data"
MANIFEST_URL = os.environ.get("MANIFEST_URL", BASE + "/manifest.json")
README_PATH = os.environ.get("README_PATH", "README.md")
DAYS_SHOWN = 14
START = "<!-- NRD-STATS:START -->"
END = "<!-- NRD-STATS:END -->"


def fetch_manifest():
    request = urllib.request.Request(
        MANIFEST_URL,
        headers={"User-Agent": "(GitHub Actions; README statistics)"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def links(stem):
    return (
        f"[TXT]({BASE}/{stem}.txt) · "
        f"[JSON]({BASE}/{stem}.json) · "
        f"[GZIP]({BASE}/{stem}.txt.gz)"
    )


def pretty_day(iso):
    d = date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def build_block(manifest):
    agg = manifest["aggregates"]
    today, d7, d30, d90 = agg["today"], agg["7d"], agg["30d"], agg["90d"]
    generated = datetime.strptime(manifest["generated_at"], "%Y-%m-%dT%H:%M:%SZ")
    stamp = f"{generated.strftime('%B')} {generated.day}, {generated.year} at {generated.strftime('%H:%M')} UTC"

    lines = [
        START,
        f"**{today['count']:,}** new domains seen so far today, {pretty_day(today['date'])} (UTC).",
        "",
        "| Window | Covers (UTC) | Domains | Download |",
        "| :-- | :-- | --: | :-- |",
        f"| **Today** | {today['date']}, still collecting | {today['count']:,} | {links('today')} |",
        f"| **Last 7 days** | {d7['from']} to {d7['to']} | {d7['count']:,} | {links('7d')} |",
        f"| **Last 30 days** | {d30['from']} to {d30['to']} | {d30['count']:,} | {links('30d')} |",
        f"| **Last 90 days** | {d90['from']} to {d90['to']} | {d90['count']:,} | one file per day, see below |",
        "",
        f"Daily average over the last 90 closed days: **{d90['daily_avg']:,}** domains.",
        "",
        "### Recent days",
        "",
        "| Date (UTC) | Day | Domains | Download |",
        "| :-- | :-- | --: | :-- |",
    ]
    for entry in manifest["days"][:DAYS_SHOWN]:
        iso = entry["date"]
        weekday = date.fromisoformat(iso).strftime("%A")
        status = " (open)" if iso == today["date"] else ""
        lines.append(f"| {iso}{status} | {weekday} | {entry['count']:,} | {links('daily/' + iso)} |")
    lines += [
        "",
        f"<sub>Numbers refreshed automatically from [manifest.json]({BASE}/manifest.json), last written {stamp}. "
        f"{len(manifest['days'])} days are available in total.</sub>",
        END,
    ]
    return "\n".join(lines)


def main():
    manifest = fetch_manifest()
    block = build_block(manifest)
    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(readme):
        sys.exit("Markers not found in README, nothing changed.")
    updated = pattern.sub(lambda _: block, readme, count=1)
    if updated != readme:
        with open(README_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(updated)
        print("README updated.")
    else:
        print("README already current.")


if __name__ == "__main__":
    main()
