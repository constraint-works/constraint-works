#!/usr/bin/env python3
"""Mahdollisuusrekisteri. Lukee mahdollisuudet/*.md-kortit ja tulostaa ranking-taulukon.

Käyttö:
  python3 tyokalut/rekisteri.py            ranking, hylätyt pois
  python3 tyokalut/rekisteri.py --kaikki   myös hylätyt
  python3 tyokalut/rekisteri.py --uusi slug "Nimi"   luo kortin pohjan
"""
import re, sys
from pathlib import Path

JUURI = Path(__file__).resolve().parent.parent
KORTIT = JUURI / "mahdollisuudet"
KRITEERIT = ["aika_ekaan_euroon", "tuplaus", "skaala", "ai_etu", "paaoma", "laillisuus"]

POHJA = """---
nimi: {nimi}
tila: hypoteesi
kirjoittaja: 
aika_ekaan_euroon: 0
tuplaus: 0
skaala: 0
ai_etu: 0
paaoma: 0
laillisuus: 0
---

# {nimi}

## Mekanismi lyhyesti

## Neljä kysymystä

**Kuka maksaa?**

**Miksi maksaa?**

**Mikä estää muita?**

**Mikä on meidän etumme?**

## Data

## Riskit ja eettinen tarkistus

## Haaste

## Vastaus haasteeseen

## Seuraava askel
"""

def lue(p):
    t = p.read_text()
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    meta = {}
    if m:
        for rivi in m.group(1).splitlines():
            if ":" in rivi:
                k, v = rivi.split(":", 1)
                meta[k.strip()] = v.strip()
    for k in KRITEERIT:
        try: meta[k] = int(meta.get(k, 0))
        except ValueError: meta[k] = 0
    meta["summa"] = sum(meta[k] for k in KRITEERIT)
    meta["tiedosto"] = p.name
    if meta["laillisuus"] < 3 and meta["tila"] != "hylätty":
        meta["tila"] = "hylätty (laillisuus)"
    return meta

def main():
    if len(sys.argv) >= 4 and sys.argv[1] == "--uusi":
        slug, nimi = sys.argv[2], " ".join(sys.argv[3:])
        p = KORTIT / f"{slug}.md"
        if p.exists(): raise SystemExit(f"{p} on jo olemassa")
        p.write_text(POHJA.format(nimi=nimi)); print("luotu", p); return
    kaikki = "--kaikki" in sys.argv
    kortit = [lue(p) for p in sorted(KORTIT.glob("*.md")) if not p.name.startswith("_")]
    if not kaikki:
        kortit = [k for k in kortit if not k["tila"].startswith("hylätty")]
    kortit.sort(key=lambda k: -k["summa"])
    print(f"{'pist':>4}  {'tila':<20} {'eka€':>4} {'x2':>3} {'skl':>3} {'ai':>3} {'pää':>3} {'lak':>3}  nimi")
    for k in kortit:
        print(f"{k['summa']:>4}  {k['tila'][:20]:<20} {k['aika_ekaan_euroon']:>4} {k['tuplaus']:>3} {k['skaala']:>3} {k['ai_etu']:>3} {k['paaoma']:>3} {k['laillisuus']:>3}  {k.get('nimi','?')}  ({k['tiedosto']})")
    print(f"\n{len(kortit)} korttia. Sarakkeet: aika ekaan euroon, tuplaus 90 pv, skaala 10M, ai-etu, pääoman keveys, laillisuus.")

if __name__ == "__main__":
    main()
