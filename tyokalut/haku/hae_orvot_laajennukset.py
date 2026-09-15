#!/usr/bin/env python3
"""Chrome Web Store -orpojen skanneri. Ottaa laajennus-ID-listan (LikoHD-aineisto, tammikuu 2025,
sarakkeet id,name,...,userCount,...) ja hakee jokaisen laajennuksen kauppasivulta nykyisen
käyttäjämäärän ja "Updated"-päivän. Tulos: JSONL + yhteenveto.

Käyttö:
  python3 tyokalut/haku/hae_orvot_laajennukset.py <mini.csv> <otos per luokka> [vain-yhteenveto]
Otanta ositettu: 10k-100k, 100k-1M, 1M+ käyttäjää (tammikuun 2025 luvut).
"""
import csv, json, random, re, sys, time, urllib.request, html
from pathlib import Path
from datetime import datetime, timezone, timedelta

csv.field_size_limit(10**9)
LAHDE = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 100
ULOS = Path(__file__).resolve().parent / "data" / "orvot" / "cws-otos.jsonl"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
KUUKAUDET = {m: i for i, m in enumerate(["January","February","March","April","May","June","July",
             "August","September","October","November","December"], 1)}

def num(x):
    try: return int(float(x))
    except: return 0

def hae(eid):
    url = f"https://chromewebstore.google.com/detail/{eid}"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            t = r.read().decode("utf-8", "ignore"); status = r.status
    except urllib.error.HTTPError as e:
        return {"id": eid, "status": e.code}
    except Exception as e:
        return {"id": eid, "status": "err", "virhe": str(e)[:80]}
    ulos = {"id": eid, "status": status}
    m = re.search(r'<div class="QDHp8e">Updated</div><div>([A-Za-z]+) (\d{1,2}), (\d{4})</div>', t)
    if m:
        ulos["paivitetty"] = f"{m.group(3)}-{KUUKAUDET.get(m.group(1),0):02d}-{int(m.group(2)):02d}"
    m = re.search(r'<div class="QDHp8e">Version</div><div class="nBZElf">([^<]+)</div>', t)
    if m: ulos["versio"] = html.unescape(m.group(1))
    m = re.search(r'([\d,\.]+)\s*users', t)
    if m: ulos["kayttajat"] = num(m.group(1).replace(",", ""))
    m = re.search(r'<div class="QDHp8e">Offered by</div><div[^>]*>([^<]+)</div>', t)
    if m: ulos["tarjoaja"] = html.unescape(m.group(1))[:80]
    ulos["established"] = "Established publisher" in t
    ulos["featured"] = ">Featured<" in t
    m = re.search(r'([\d\.]+) out of 5', t)
    if m: ulos["arvosana"] = float(m.group(1))
    m = re.search(r'([\d,\.]+K?) ratings', t)
    if m: ulos["arvosteluja"] = m.group(1)
    return ulos

if __name__ == "__main__":
    rows = list(csv.DictReader(open(LAHDE, encoding="utf-8", errors="ignore")))
    luokat = {"10k-100k": (10_000, 100_000), "100k-1M": (100_000, 1_000_000), "1M+": (1_000_000, 10**12)}
    random.seed(20260916)
    otos = []
    for nimi, (a, b) in luokat.items():
        ehdokkaat = [r for r in rows if a <= num(r["userCount"]) < b]
        for r in random.sample(ehdokkaat, min(N, len(ehdokkaat))):
            otos.append({"luokka": nimi, "id": r["id"], "nimi": r["name"][:80], "kayttajat_2025_01": num(r["userCount"]),
                         "tekija": r.get("author", "")[:60], "versio_2025_01": r.get("version", "")})
    print(f"otos {len(otos)} laajennusta", file=sys.stderr)
    with ULOS.open("w") as f:
        for i, o in enumerate(otos):
            o.update(hae(o["id"]))
            f.write(json.dumps(o, ensure_ascii=False) + "\n"); f.flush()
            if i % 25 == 0: print(f"{i}/{len(otos)}", file=sys.stderr)
            time.sleep(0.8)
    print("valmis", file=sys.stderr)
