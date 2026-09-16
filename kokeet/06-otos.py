#!/usr/bin/env python3
"""Koe 06: otoksen arvonta lukitusta kehikosta (lukitus L1). Ei ajeta ennen GPT:n arviota.

Käyttö:
  python3 kokeet/06-otos.py --kehikko <kehikko.csv repon ulkopuolella> \
      --siemen 20261005 --n 150 --otos <otos.csv repon ulkopuolella> \
      --tiivistelma kokeet/06-otos-tiivistelma.json

Otos (nimet, y-tunnukset) EI tule repoon. Repoon committoidaan vain tiivistelmä:
siemen, kehikon ja otoksen SHA-256, jakaumat. Riveille annetaan tunnisteet K06-001 ...
arvotussa järjestyksessä: 001 - 060 aalto 1, 061 - 120 aalto 2, 121 - 150 vara.
"""
import argparse, csv, hashlib, json, random, collections, datetime

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kehikko", required=True)
    ap.add_argument("--siemen", type=int, required=True, help="lukituspäivä YYYYMMDD")
    ap.add_argument("--n", type=int, default=150)
    ap.add_argument("--otos", required=True)
    ap.add_argument("--tiivistelma", required=True)
    a = ap.parse_args()

    with open(a.kehikko, encoding="utf-8", newline="") as f:
        rivit = list(csv.DictReader(f))
    rivit.sort(key=lambda r: r["y_tunnus"])  # deterministinen järjestys ennen arvontaa
    otos = random.Random(a.siemen).sample(rivit, a.n)

    with open(a.otos, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["tunniste", "aalto", "y_tunnus", "nimi", "tol2025", "kunta", "rekisteroity", "verot_2024", "www_ytj", "poissulku", "kanava"])
        for i, r in enumerate(otos, 1):
            aalto = "1" if i <= 60 else "2" if i <= 120 else "vara"
            w.writerow([f"K06-{i:03d}", aalto, r["y_tunnus"], r["nimi"], r["tol2025"], r["kunta"], r["rekisteroity"], r["verot_2024"], r["www_ytj"], "", ""])

    def jak(key, fn=lambda x: x):
        return dict(sorted(collections.Counter(fn(r[key]) for r in otos).items()))
    tiiv = {
        "lukittu": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"),
        "siemen": a.siemen,
        "n": a.n,
        "kehikko_n": len(rivit),
        "kehikko_sha256": sha(a.kehikko),
        "otos_sha256": sha(a.otos),
        "tol2": jak("tol2025", lambda t: t[:2]),
        "verobandit": jak("verot_2024", lambda v: "10-50k" if float(v) < 50000 else "50-250k" if float(v) < 250000 else ">250k"),
        "ikaluokat": jak("rekisteroity", lambda d: "5-9" if 2026 - int(d[:4]) < 10 else "10-19" if 2026 - int(d[:4]) < 20 else "20+"),
        "www_ytj_osuus": round(sum(1 for r in otos if r["www_ytj"] == "1") / a.n, 3),
    }
    with open(a.tiivistelma, "w", encoding="utf-8") as f:
        json.dump(tiiv, f, ensure_ascii=False, indent=1)
    print(json.dumps(tiiv, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
