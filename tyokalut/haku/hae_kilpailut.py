#!/usr/bin/env python3
"""Listaa avoimet ja tulevat auditointikilpailut Sherlockista.

Käyttö: python3 hae_kilpailut.py [--kaikki]
Tallentaa raakadatan data/sherlock.json ja tulostaa taulukon.
"""
import json, sys, time, urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://mainnet-contest.sherlock.xyz/contests?page={}"
UA = {"User-Agent": "Mozilla/5.0 (eikaisiina-tutkimus)"}
DATA = Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)

def hae_kaikki():
    sivu, kaikki = 1, []
    while sivu:
        req = urllib.request.Request(API.format(sivu), headers=UA)
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
        kaikki += d.get("items", [])
        sivu = d.get("next_page")
        time.sleep(0.3)
    return kaikki

def pvm(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d") if ts else "-"

def main():
    nayta_kaikki = "--kaikki" in sys.argv
    kilpailut = hae_kaikki()
    (DATA / "sherlock.json").write_text(json.dumps(kilpailut, indent=1))
    nyt = time.time()
    avoimet = [k for k in kilpailut
               if k.get("status") in ("RUNNING", "CREATED", "UPCOMING", "SHERLOCK_JUDGING") or k.get("ends_at", 0) > nyt]
    lista = kilpailut if nayta_kaikki else avoimet
    lista.sort(key=lambda k: -(k.get("prize_pool") or 0))
    print(f"{'id':>5}  {'status':<18} {'potti':>10}  {'alkaa':<10} {'päättyy':<10}  otsikko")
    for k in lista:
        print(f"{k['id']:>5}  {k.get('status',''):<18} {k.get('prize_pool',0):>10,.0f}  {pvm(k.get('starts_at')):<10} {pvm(k.get('ends_at')):<10}  {k['title'][:50]}")
    yht = sum(k.get("prize_pool") or 0 for k in avoimet)
    print(f"\n{len(kilpailut)} kilpailua yhteensä, {len(avoimet)} avointa/tulevaa, avoimet potit yhteensä {yht:,.0f} USD")

if __name__ == "__main__":
    main()
