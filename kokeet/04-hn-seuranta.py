#!/usr/bin/env python3
"""Koe 04: HN-postauksen jakelun seuranta julkisesta Firebase-rajapinnasta (ei tiliä).
Käyttö: python3 kokeet/04-hn-seuranta.py <item_id> [tunnit=48] [väli_min=15]
Kirjaa 15 min välein: pisteet, kommentit, dead/flagged-tila, sijoitus topstories-listalla.
Tulos: kokeet/04-hn-seuranta.jsonl. Vaihe D:n ehdot lasketaan lopuksi."""
import json, sys, time, urllib.request
from pathlib import Path
ITEM = int(sys.argv[1]); TUNNIT = float(sys.argv[2]) if len(sys.argv) > 2 else 48; VALI = int(sys.argv[3]) if len(sys.argv) > 3 else 15
ULOS = Path(__file__).resolve().parent / "04-hn-seuranta.jsonl"
API = "https://hacker-news.firebaseio.com/v0"
def get(p):
    with urllib.request.urlopen(f"{API}/{p}.json", timeout=30) as r: return json.load(r)
loppu = time.time() + TUNNIT * 3600
while time.time() < loppu:
    try:
        it = get(f"item/{ITEM}") or {}
        top = get("topstories") or []
        sija = (top.index(ITEM) + 1) if ITEM in top else None
        r = {"aika": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "pisteet": it.get("score"),
             "kommentit": it.get("descendants"), "dead": it.get("dead", False), "deleted": it.get("deleted", False),
             "sija_top": sija, "otsikko": it.get("title")}
    except Exception as e:
        r = {"aika": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "virhe": str(e)[:120]}
    with ULOS.open("a") as f: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(r, flush=True)
    time.sleep(VALI * 60)
rivit = [json.loads(l) for l in ULOS.open()]
a = any((x.get("pisteet") or 0) >= 5 for x in rivit)
b = any(x.get("sija_top") is not None and x["sija_top"] <= 30 for x in rivit)
c = any((x.get("kommentit") or 0) >= 3 for x in rivit)
kuoli_2h = any(x.get("dead") for x in rivit[:max(1, int(120 / VALI))])
print("VAIHE D:", "EPÄONNISTUI (dead/flagged 2 h)" if kuoli_2h else ("LÄPÄISTY" if (a or b or c) else "EPÄONNISTUI (ei jakelua 48 h)"),
      {"pisteet>=5": a, "top30": b, "kommentit>=3": c})
