#!/usr/bin/env python3
"""WordPress.org-lisäosien orposkanneri. Julkinen rajapinta antaa aktiiviset asennukset,
viimeisen päivityksen ja "tested up to" -version. Hakee suosituimmat N sivua (250/sivu).

Käyttö: python3 tyokalut/haku/hae_orvot_wordpress.py 40   # 10 000 suosituinta
Tulos: tyokalut/haku/data/orvot/wordpress.jsonl ja yhteenveto stdoutiin.
"""
import json, sys, time, urllib.request, urllib.parse
from pathlib import Path
from datetime import datetime, timezone, timedelta

SIVUT = int(sys.argv[1]) if len(sys.argv) > 1 else 10
ULOS = Path(__file__).resolve().parent / "data" / "orvot" / "wordpress.jsonl"
NYT = datetime.now(timezone.utc)

def hae(sivu):
    q = urllib.parse.urlencode({"action": "query_plugins", "request[browse]": "popular",
                                "request[per_page]": 250, "request[page]": sivu,
                                "request[fields][active_installs]": 1, "request[fields][last_updated]": 1,
                                "request[fields][tested]": 1, "request[fields][downloaded]": 1,
                                "request[fields][num_ratings]": 1, "request[fields][support_threads]": 1,
                                "request[fields][support_threads_resolved]": 1, "request[fields][description]": 0,
                                "request[fields][sections]": 0, "request[fields][icons]": 0, "request[fields][banners]": 0})
    url = "https://api.wordpress.org/plugins/info/1.2/?" + q
    for y in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "eikaisiina-tutkimus/0.1"}), timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(3 * (y + 1))
    return None

rivit = []
with ULOS.open("w") as f:
    for s in range(1, SIVUT + 1):
        d = hae(s)
        if not d or not d.get("plugins"): print(f"sivu {s}: tyhjä", file=sys.stderr); break
        for p in d["plugins"]:
            r = {k: p.get(k) for k in ["slug", "name", "version", "author", "active_installs", "downloaded",
                                       "last_updated", "tested", "requires", "rating", "num_ratings",
                                       "support_threads", "support_threads_resolved", "added"]}
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); rivit.append(r)
        print(f"sivu {s}: yhteensä {len(rivit)}", file=sys.stderr); time.sleep(0.5)

def pvm(s):
    try: return datetime.strptime(s[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except Exception: return None

def raportti(rivit, otsikko):
    print(f"\n== {otsikko}: {len(rivit)} lisäosaa")
    for vuotta in (1, 2, 3):
        raja = NYT - timedelta(days=365 * vuotta)
        o = [r for r in rivit if pvm(r["last_updated"] or "") and pvm(r["last_updated"]) < raja]
        print(f"  ei päivitystä {vuotta} v: {len(o)} ({100*len(o)/max(1,len(rivit)):.1f} %), "
              f"aktiivisia asennuksia yhteensä {sum(r['active_installs'] or 0 for r in o):,}")
    raja = NYT - timedelta(days=730)
    o = [r for r in rivit if pvm(r["last_updated"] or "") and pvm(r["last_updated"]) < raja]
    for kynnys in (10_000, 100_000, 1_000_000):
        print(f"  orpoja (2 v) joilla >= {kynnys:,} asennusta: {sum(1 for r in o if (r['active_installs'] or 0) >= kynnys)}")
    print("  orpoja joilla avoimia tukikeskusteluja: ", sum(1 for r in o if (r['support_threads'] or 0) > 0))
    o.sort(key=lambda r: -(r["active_installs"] or 0))
    print("  top 25 orpoa:")
    for r in o[:25]:
        print(f"    {r['slug']:<40} {r['active_installs'] or 0:>10,} asennusta  päiv {str(r['last_updated'])[:10]}  tested {r['tested']}  tuki {r['support_threads']}/{r['support_threads_resolved']}  arv {r['rating']}/{r['num_ratings']}")

raportti(rivit, "WordPress.org popular")
