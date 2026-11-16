# Newly Registered Domains (NRD) Feed

[![Uptime](https://incidents.betterstack.com/status-badges/v1/monitor/34dkg.svg)](https://smet.betteruptime.com/)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![No API key](https://img.shields.io/badge/API%20key-not%20required-brightgreen.svg)](https://smet.cz/nrd/)
[![History](https://img.shields.io/badge/history-90%20days-informational.svg)](https://smet.cz/nrd/data/manifest.json)
[![Formats](https://img.shields.io/badge/formats-TXT%20%C2%B7%20JSON%20%C2%B7%20GZIP-lightgrey.svg)](#formats)

A free list of newly registered domains, updated several times a day and published by [smet.cz](https://smet.cz/) as plain files. Every file is a single HTTPS GET: no key, no signup, no client library.

The feed covers more than 1,600 effective TLDs and keeps 90 days of history. It is built for threat hunting, phishing detection, brand protection, typosquatting monitoring, DNS blocklists and research.

This repository does not store the lists themselves. It documents the feed and links to the live files, and the numbers below are refreshed from the feed's manifest throughout the day.

## Live numbers

<!-- NRD-STATS:START -->
**124,464** new domains seen so far today, November 16, 2026 (UTC).

| Window | Covers (UTC) | Domains | Download |
| :-- | :-- | --: | :-- |
| **Today** | 2026-11-16, still collecting | 124,464 | [TXT](https://smet.cz/nrd/data/today.txt) · [JSON](https://smet.cz/nrd/data/today.json) · [GZIP](https://smet.cz/nrd/data/today.txt.gz) |
| **Last 7 days** | 2026-11-10 to 2026-11-16 | 2,096,956 | [TXT](https://smet.cz/nrd/data/7d.txt) · [JSON](https://smet.cz/nrd/data/7d.json) · [GZIP](https://smet.cz/nrd/data/7d.txt.gz) |
| **Last 30 days** | 2026-10-18 to 2026-11-16 | 10,688,149 | [TXT](https://smet.cz/nrd/data/30d.txt) · [JSON](https://smet.cz/nrd/data/30d.json) · [GZIP](https://smet.cz/nrd/data/30d.txt.gz) |
| **Last 90 days** | 2026-08-18 to 2026-11-15 | 34,776,473 | one file per day, see below |

Daily average over the last 90 closed days: **386,405** domains.

### Recent days

| Date (UTC) | Day | Domains | Download |
| :-- | :-- | --: | :-- |
| 2026-11-16 (open) | Monday | 124,464 | [TXT](https://smet.cz/nrd/data/daily/2026-11-16.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-16.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-16.txt.gz) |
| 2026-11-15 | Sunday | 259,544 | [TXT](https://smet.cz/nrd/data/daily/2026-11-15.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-15.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-15.txt.gz) |
| 2026-11-14 | Saturday | 311,461 | [TXT](https://smet.cz/nrd/data/daily/2026-11-14.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-14.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-14.txt.gz) |
| 2026-11-13 | Friday | 335,538 | [TXT](https://smet.cz/nrd/data/daily/2026-11-13.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-13.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-13.txt.gz) |
| 2026-11-12 | Thursday | 348,130 | [TXT](https://smet.cz/nrd/data/daily/2026-11-12.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-12.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-12.txt.gz) |
| 2026-11-11 | Wednesday | 364,537 | [TXT](https://smet.cz/nrd/data/daily/2026-11-11.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-11.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-11.txt.gz) |
| 2026-11-10 | Tuesday | 353,282 | [TXT](https://smet.cz/nrd/data/daily/2026-11-10.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-10.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-10.txt.gz) |
| 2026-11-09 | Monday | 265,342 | [TXT](https://smet.cz/nrd/data/daily/2026-11-09.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-09.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-09.txt.gz) |
| 2026-11-08 | Sunday | 584,643 | [TXT](https://smet.cz/nrd/data/daily/2026-11-08.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-08.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-08.txt.gz) |
| 2026-11-07 | Saturday | 374,863 | [TXT](https://smet.cz/nrd/data/daily/2026-11-07.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-07.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-07.txt.gz) |
| 2026-11-06 | Friday | 404,806 | [TXT](https://smet.cz/nrd/data/daily/2026-11-06.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-06.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-06.txt.gz) |
| 2026-11-05 | Thursday | 383,294 | [TXT](https://smet.cz/nrd/data/daily/2026-11-05.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-05.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-05.txt.gz) |
| 2026-11-04 | Wednesday | 402,543 | [TXT](https://smet.cz/nrd/data/daily/2026-11-04.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-04.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-04.txt.gz) |
| 2026-11-03 | Tuesday | 322,992 | [TXT](https://smet.cz/nrd/data/daily/2026-11-03.txt) · [JSON](https://smet.cz/nrd/data/daily/2026-11-03.json) · [GZIP](https://smet.cz/nrd/data/daily/2026-11-03.txt.gz) |

<sub>Numbers refreshed automatically from [manifest.json](https://smet.cz/nrd/data/manifest.json), last written November 16, 2026 at 04:10 UTC. 91 days are available in total.</sub>
<!-- NRD-STATS:END -->

## Quick start

Today's list is a plain text file with one domain per line, so any HTTP client works.

**curl**

```bash
curl -s --compressed https://smet.cz/nrd/data/today.txt | head
```

**wget**

```bash
wget https://smet.cz/nrd/data/7d.txt.gz
```

**Python**

```python
import requests

domains = set(requests.get("https://smet.cz/nrd/data/today.txt").text.splitlines())
print(len(domains))
```

**PowerShell**

```powershell
Invoke-WebRequest https://smet.cz/nrd/data/today.txt -OutFile today.txt
```

Swap `today` for `7d` or `30d` to widen the window, and `.txt` for `.json` or `.txt.gz` to change the format.

## Files and URLs

Everything lives under one base URL: `https://smet.cz/nrd/data/`

| Path | What it holds |
| :-- | :-- |
| [`today.txt`](https://smet.cz/nrd/data/today.txt) | Domains first seen on the current UTC day. Grows through the day. |
| [`7d.txt`](https://smet.cz/nrd/data/7d.txt) | The current UTC day and the six before it. |
| [`30d.txt`](https://smet.cz/nrd/data/30d.txt) | The current UTC day and the 29 before it. |
| `daily/YYYY-MM-DD.txt` | One UTC day. Kept for 90 days. A closed day never changes. |
| [`manifest.json`](https://smet.cz/nrd/data/manifest.json) | Every available file, with its date and count. |

Each domain appears in exactly one daily file, on the day it was first published. The 7-day and 30-day files combine those days, so their counts are unique domains.

## Formats

| Extension | Content |
| :-- | :-- |
| `.txt` | One registered domain per line. Lowercase ASCII, internationalized names in punycode (`xn--`). Sorted in byte order and deduplicated, so `comm` and `join` work directly with `LC_ALL=C`. |
| `.json` | The same list in a `domains` array, with `date`, `count`, `generated_at`, `license` and `attribution` alongside it. |
| `.txt.gz` | The TXT file compressed with gzip, served as `application/gzip`. Use it when you want to store the files compressed. |

```json
{
  "date": "2026-11-08",
  "count": 584643,
  "generated_at": "2026-11-08T20:12:19Z",
  "license": "CC-BY-4.0",
  "license_url": "https://creativecommons.org/licenses/by/4.0/",
  "attribution": "smet.cz (https://smet.cz/nrd/)",
  "domains": ["example.com", "example.net", "new-domain.example"]
}
```

Responses are compressed in transit (zstd, brotli or gzip, negotiated from `Accept-Encoding`), so plain `.txt` is already cheap to download. The 30-day JSON is large and has to be parsed whole. To stream, read `30d.txt` or `30d.txt.gz` line by line.

## The manifest

[`manifest.json`](https://smet.cz/nrd/data/manifest.json) lists every file that exists right now. Read it first: it gives you today's date, the valid days for history and every count, so nothing has to be guessed.

```bash
curl -s https://smet.cz/nrd/data/manifest.json | jq -r '.days[].date' | head -3
```

## Polling for new domains

Every file carries `ETag` and `Last-Modified`. Send the value back and an unchanged file answers `304` with no body, so frequent polling costs almost nothing.

```bash
curl -s --compressed -R -z today.txt -o today.txt https://smet.cz/nrd/data/today.txt
```

To get only what is new since your last check, keep the previous copy and diff against it:

```bash
export LC_ALL=C
curl -s --compressed -o next.txt https://smet.cz/nrd/data/today.txt
comm -13 today.txt next.txt
mv next.txt today.txt
```

A complete poller that also handles the switch to a new UTC day is in the [documentation](https://smet.cz/docs/nrd.md).

## Backfilling history

Closed days never change, so fetch each one once and take the dates from the manifest instead of generating them.

```bash
mkdir -p nrd
curl -fsS https://smet.cz/nrd/data/manifest.json | jq -r '.days[1:][].date' |
while read -r day; do
  [ -f "nrd/$day.txt.gz" ] && continue
  curl -fsS -o "nrd/$day.txt.gz" "https://smet.cz/nrd/data/daily/$day.txt.gz"
  sleep 2
done
```

The first entry in `days` is the open day, which is still growing, so the loop starts at the second.

## Watching for lookalike domains

A simple brand watch: filter new domains through a pattern of your names and their common misspellings.

```bash
curl -s --compressed https://smet.cz/nrd/data/today.txt | grep -E 'acme|acrne|acme-?(login|secure|support)'
```

## What people use it for

| Use case | How the feed helps |
| :-- | :-- |
| **Phishing detection** | Flag mail and web traffic that points at domains only hours or days old. |
| **Threat hunting** | Enrich alerts and logs with domain age, and hunt for freshly registered infrastructure. |
| **Brand protection** | Catch lookalike and typosquatting registrations soon after they become visible. |
| **DNS blocklists** | Build a "young domains" list for a resolver or firewall from the 7-day or 30-day file. |
| **Fraud prevention** | Treat signups and payments tied to brand new domains with extra care. |
| **Research** | Measure registration volume, TLD trends and naming patterns over 90 days. |

## HTTP details

| | |
| :-- | :-- |
| Method | `GET`, or `HEAD` for headers only |
| Authentication | None |
| CORS | `access-control-allow-origin: *`, so browser code can fetch the files directly |
| Compression | zstd, br or gzip |
| Validators | `ETag` and `Last-Modified` on every file |
| Caching | `cache-control: public, max-age=3600` |

| Status | Meaning |
| :-- | :-- |
| `200` | The file, in full. A URL never returns a partial file. |
| `304` | Not modified since your copy. |
| `404` | No such file: a day outside the last 90, or one that has not started yet. |
| `429` | Too many requests in a short burst. Wait a few seconds and retry. |

When fetching history, space requests a couple of seconds apart. Describing your use case in the `User-Agent` is optional and helps improve the service, for example `ExampleBot/1.0 (+https://example.com; brand protection)`.

## About the data

<details>
<summary><b>What counts as a new domain?</b></summary>
<br>
The list is best read as "domains that just became visible to the internet". For security, brand protection and research that is usually the more useful definition, because it marks the point where a domain can actually be put to use.
</details>

<details>
<summary><b>How are entries dated?</b></summary>
<br>
Entries are deduplicated, normalized to lowercase punycode and dated by first appearance in the collection. For zones without public registration data, that date can trail the actual registration by a short interval.
</details>

<details>
<summary><b>When does a new day start?</b></summary>
<br>
Nothing resets at midnight. Today's files switch to the new UTC day on the first update after 00:00, a few hours in. Until then they hold the previous day, so check the date in <code>today.json</code>, the manifest or the <code>Last-Modified</code> header.
</details>

<details>
<summary><b>How complete is the list?</b></summary>
<br>
It is built for the broadest coverage practically achievable. Some zones do not publish their registration data, so no provider can claim a complete picture. Within those limits, the feed captures as much of each day's registrations as possible.
</details>

<details>
<summary><b>Will the URLs change?</b></summary>
<br>
URLs and formats will not change. New fields may be added to the JSON, but existing ones keep their names and meaning.
</details>

<details>
<summary><b>What personal data is in the feed?</b></summary>
<br>
None. The feed contains domain names only. Registrant names, emails and phone numbers are not collected.
</details>

## License and attribution

The data is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). It is free for commercial and non-commercial use with visible attribution to smet.cz, linked to https://smet.cz/ where the medium allows. Redistribution is permitted with that attribution carried along.

Credit smet.cz in your product's UI, documentation or README. Please do not put smet.cz in `User-Agent` strings. Every JSON file carries `license`, `license_url` and `attribution`, so the terms travel with the data.

Registry sources include CISA (CC0), Afnic, Traficom (CC BY 4.0) and Internetstiftelsen (CC BY 4.0).

## Removal requests

Want a domain taken out of the feed? Any entry is removed on request through [smet.cz/contact](https://smet.cz/contact).

## Links

- Feed home: https://smet.cz/nrd/
- Documentation for humans: https://smet.cz/docs/nrd/
- Documentation for LLMs: https://smet.cz/docs/nrd.md
- Manifest: https://smet.cz/nrd/data/manifest.json
- Blog: https://smet.cz/blog

---

<sub>Made in the EU with GDPR compliance by design.</sub>
