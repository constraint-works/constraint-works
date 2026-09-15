#!/usr/bin/env python3
"""Purkaa Immunefin julkisesta sivusta kaikki pysyvät bug bounty -ohjelmat.

Nämä eivät ole kilpailuja vaan pysyviä potteja: raha on olemassa ja maksetaan
sille, joka löytää haavoittuvuuden. Tallentaa data/immunefi.json ja tulostaa taulukon.
"""
import json, re, urllib.request
from pathlib import Path

URL = "https://immunefi.com/bug-bounty/"
UA = {"User-Agent": "Mozilla/5.0 (eikaisiina-tutkimus)"}
DATA = Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)

def hae():
    req = urllib.request.Request(URL, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        html = r.read().decode()
    # RSC-payload: JSON on escapattu merkkijonon sisään. Poimitaan bounties-taulukko.
    i = html.find('\\"bounties\\":[')
    if i < 0:
        raise SystemExit("bounties-taulukkoa ei löytynyt, sivun rakenne muuttunut")
    j = i + len('\\"bounties\\":')
    # etsi taulukon loppu laskemalla sulkuja
    syv, k = 0, j
    while True:
        c = html[k]
        if c == "[": syv += 1
        elif c == "]":
            syv -= 1
            if syv == 0: break
        k += 1
    raaka = html[j:k+1].encode().decode("unicode_escape")
    return json.loads(raaka)

def main():
    ohjelmat = hae()
    (DATA / "immunefi.json").write_text(json.dumps(ohjelmat, indent=1, ensure_ascii=False))
    ohjelmat.sort(key=lambda o: -(o.get("maxBounty") or 0))
    print(f"{'max USD':>12}  {'kyc':<4} {'päivitetty':<10}  {'projekti':<28} teknologiat")
    for o in ohjelmat:
        tek = ",".join(t if isinstance(t, str) else t.get("name", "") for t in (o.get("technologies") or []))[:40]
        print(f"{o.get('maxBounty') or 0:>12,}  {str(o.get('kyc'))[:1]:<4} {(o.get('updatedDate') or '')[:10]:<10}  {o.get('project','')[:28]:<28} {tek}")
    yht = sum(o.get("maxBounty") or 0 for o in ohjelmat)
    print(f"\n{len(ohjelmat)} ohjelmaa, maksimipalkkiot yhteensä {yht:,} USD")

if __name__ == "__main__":
    main()
