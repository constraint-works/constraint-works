#!/usr/bin/env python3
"""Superteam Earnin virallinen agenttirajapinta.

Vaatii agentin API-avaimen ympäristömuuttujassa SUPERTEAM_AGENT_KEY (tai .env-tiedostossa).
Rekisteröinnin tekee ihminen (luo tilin), ei tämä skripti:

    curl -s -X POST https://superteam.fun/api/agents -A "Mozilla/5.0" \
      -H "Content-Type: application/json" -d '{"name":"eikaisiina"}'

Vastauksessa apiKey (talleta .env: SUPERTEAM_AGENT_KEY=sk_...) ja claimCode (talleta
turvaan, sillä lunastetaan palkkio ihmisenä).

Käyttö:
  python3 superteam_agentti.py live            agenttikelpoiset listaukset (AGENT_ALLOWED + AGENT_ONLY)
  python3 superteam_agentti.py details <slug>  yhden listauksen koko sopimus
"""
import json, os, sys, urllib.request
from pathlib import Path

BASE = "https://superteam.fun"
DATA = Path(__file__).parent / "data"

def avain():
    k = os.environ.get("SUPERTEAM_AGENT_KEY")
    if not k:
        env = Path(__file__).resolve().parents[2] / ".env"
        if env.exists():
            for r in env.read_text().splitlines():
                if r.startswith("SUPERTEAM_AGENT_KEY="):
                    k = r.split("=", 1)[1].strip().strip('"')
    if not k:
        raise SystemExit("SUPERTEAM_AGENT_KEY puuttuu. Ks. docstring rekisteröinnistä.")
    return k

def hae(polku):
    req = urllib.request.Request(BASE + polku, headers={"Authorization": f"Bearer {avain()}", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    if sys.argv[1] == "live":
        d = hae("/api/agents/listings/live?take=100&deadline=2027-12-31")
        DATA.mkdir(exist_ok=True)
        (DATA / "superteam-agent-live.json").write_text(json.dumps(d, indent=1))
        items = d if isinstance(d, list) else d.get("listings") or d.get("items") or d.get("data") or []
        print(f"{'USD':>7} {'sub':>4} {'access':<14} {'type':<9} {'deadline':<10} slug")
        for x in sorted(items, key=lambda x: -(x.get("rewardAmount") or 0)):
            print(f"{x.get('rewardAmount') or 0:>7,.0f} {(x.get('_count') or {}).get('Submission', '?'):>4} {str(x.get('agentAccess')):<14} {str(x.get('type')):<9} {(x.get('deadline') or '')[:10]:<10} {x.get('slug')}")
        print(f"\n{len(items)} agenttikelpoista listausta")
    elif sys.argv[1] == "details" and len(sys.argv) > 2:
        print(json.dumps(hae(f"/api/agents/listings/details/{sys.argv[2]}"), indent=1, ensure_ascii=False))
    else:
        raise SystemExit(__doc__)

if __name__ == "__main__":
    main()
