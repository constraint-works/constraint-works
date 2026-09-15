#!/usr/bin/env python3
"""Orpojen pakettien skanneri. Hakee ecosyste.ms-rajapinnasta rekisterin ladatuimmat
paketit ja merkitsee ne, joiden viimeinen julkaisu on yli N vuotta vanha mutta joilla
on yhä latauksia ja riippuvia paketteja.

Käyttö:
  python3 tyokalut/haku/hae_orvot_paketit.py npmjs.org 30      # 30 sivua x 100 = 3000 pakettia
  python3 tyokalut/haku/hae_orvot_paketit.py pypi.org 30
Tulos: tyokalut/haku/data/orvot/<rekisteri>.jsonl (raaka), yhteenveto stdoutiin.
"""
import json, sys, time, urllib.request, urllib.parse
from pathlib import Path
from datetime import datetime, timezone, timedelta

REK = sys.argv[1] if len(sys.argv) > 1 else "npmjs.org"
SIVUT = int(sys.argv[2]) if len(sys.argv) > 2 else 10
RAJA_VUOTTA = 2
ULOS = Path(__file__).resolve().parent / "data" / "orvot" / f"{REK}.jsonl"
ULOS.parent.mkdir(parents=True, exist_ok=True)
NYT = datetime.now(timezone.utc)
RAJA = NYT - timedelta(days=365 * RAJA_VUOTTA)

def hae(url):
    for yritys in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "eikaisiina-tutkimus/0.1"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(3 * (yritys + 1))
    return None

rivit = []
with ULOS.open("w") as f:
    for sivu in range(1, SIVUT + 1):
        url = (f"https://packages.ecosyste.ms/api/v1/registries/{REK}/packages"
               f"?sort=downloads&order=desc&per_page=100&page={sivu}")
        data = hae(url)
        if not data:
            print(f"sivu {sivu}: ei dataa", file=sys.stderr); break
        for p in data:
            rivi = {k: p.get(k) for k in ["name", "downloads", "downloads_period",
                    "latest_release_published_at", "first_release_published_at",
                    "dependent_packages_count", "dependent_repos_count", "repository_url",
                    "status", "versions_count", "licenses", "funding_links", "critical"]}
            rivi["maintainers_n"] = len(p.get("maintainers") or [])
            rm = p.get("repo_metadata") or {}
            rivi["repo_archived"] = rm.get("archived")
            rivi["repo_pushed_at"] = rm.get("pushed_at")
            rivi["repo_stars"] = rm.get("stargazers_count")
            rivi["repo_open_issues"] = rm.get("open_issues_count")
            rivi["advisories_n"] = len(p.get("advisories") or [])
            f.write(json.dumps(rivi) + "\n")
            rivit.append(rivi)
        print(f"sivu {sivu}: {len(data)} pakettia, yhteensä {len(rivit)}", file=sys.stderr)
        time.sleep(0.5)

def pvm(s):
    if not s: return None
    try: return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception: return None

orvot = [r for r in rivit if pvm(r["latest_release_published_at"]) and pvm(r["latest_release_published_at"]) < RAJA]
print(f"\n{REK}: {len(rivit)} ladatuinta pakettia, joista {len(orvot)} ({100*len(orvot)/max(1,len(rivit)):.1f} %) "
      f"ilman julkaisua {RAJA_VUOTTA} vuoteen")
lat_kaikki = sum(r["downloads"] or 0 for r in rivit)
lat_orvot = sum(r["downloads"] or 0 for r in orvot)
print(f"lataukset/kk: kaikki {lat_kaikki:,}, orvot {lat_orvot:,} ({100*lat_orvot/max(1,lat_kaikki):.1f} %)")
print(f"orvoista advisoryja: {sum(1 for r in orvot if r['advisories_n'])}, "
      f"arkistoitu repo: {sum(1 for r in orvot if r['repo_archived'])}, "
      f"1 ylläpitäjä: {sum(1 for r in orvot if r['maintainers_n']==1)}, "
      f"funding-linkki: {sum(1 for r in orvot if r['funding_links'])}")
orvot.sort(key=lambda r: -(r["downloads"] or 0))
print("\ntop 40 orpoa latauksilla:")
for r in orvot[:40]:
    print(f"  {r['name']:<40} {r['downloads'] or 0:>14,}/kk  viim.julk {str(r['latest_release_published_at'])[:10]}  "
          f"dep_pkgs {r['dependent_packages_count']:>7}  dep_repos {r['dependent_repos_count'] or 0:>9}  "
          f"maint {r['maintainers_n']}  adv {r['advisories_n']}  arkistoitu {r['repo_archived']}")
