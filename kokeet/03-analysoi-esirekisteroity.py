#!/usr/bin/env python3
"""Koe 03 -analyysi, kirjoitettu ennen tulosten näkemistä. Lukittu taksonomia ja mittarit.
T1 pakkaus/rakennusinfra; T2 kielen/ajoympäristön versio; T3 riippuvuuden poistettu/muuttunut API;
T4 vain testi-/kehitysinfra rikki, tuote toimii; T5 toiminnallinen virhe ajossa; T6 korjaamaton advisory (toimii);
T7 ei toistettavissa: toimii. Sääntö: virheilmoituksen ensimmäinen rivi ratkaisee; kaksi sopii -> pienempi numero."""
import json, re, sys, csv
T1 = re.compile(r"(setuptools|pkg_resources|distutils|build backend|setup\.py|pyproject|wheel|metadata-generation-failed|Preparing metadata|Building wheel|build dependencies|egg_info|No matching distribution|Could not find a version|yanked|no source distribution|does not appear to be a Python project)", re.I)
T2 = re.compile(r"(ast\.Str|ast\.Num|\bimp\b|asyncore|asynchat|distutils\b.*Python|SyntaxError|removed in Python|no longer supported|python_requires|Requires-Python|invalid syntax|collections\.Mapping|collections\.MutableMapping|cgi module|unittest\.makeSuite)", re.I)
T3 = re.compile(r"(cannot import name|ImportError|ModuleNotFoundError|AttributeError: module|has no attribute|TypeError: .*got an unexpected keyword|DeprecationWarning)", re.I)
def luokka(t, advisoryja):
    if t.get("kontrolli"): pass
    if t.get("tila") == "onnistui":
        return "T6" if int(advisoryja or 0) > 0 else "T7"
    v = t.get("virhe", "") or ""
    vaihe = t.get("vaihe", "")
    # T1: rakennus-/asennusvaihe; T2/T3 importissa tai rakennuksessa virheilmoituksen mukaan
    if T2.search(v): return "T2"   # sääntö: pienempi numero voittaa, mutta T1 vain jos ilmoitus on rakennusinfra
    if T1.search(v) or vaihe in ("1_lahdeasennus", "3_wheel"): return "T1"
    if T3.search(v): return "T3"
    return "T5"
def normalisoi(v):
    v = re.sub(r"\d+(\.\d+)*", "N", v)             # versionumerot ja luvut
    v = re.sub(r"(/[^\s'\"]+)+", "/P", v)           # polut
    v = re.sub(r"'[^']*'", "'X'", v)                 # nimet lainausmerkeissä
    return v.strip()[:160]
if __name__ == "__main__":
    rows = [json.loads(l) for l in open("./kokeet/03-tulokset.jsonl")]
    adv = {r["nimi"]: r["advisoryja"] for r in csv.DictReader(open("./kokeet/03-otos.csv"))}
    otos = [r for r in rows if not r.get("kontrolli")]
    kontrolli = [r for r in rows if r.get("kontrolli")]
    for r in otos: r["T"] = luokka(r, adv.get(r["nimi"], 0)); r["norm"] = normalisoi(r.get("virhe", "") or "")
    for r in kontrolli: r["T"] = luokka(r, 2); r["norm"] = normalisoi(r.get("virhe", "") or "")
    n = len(otos)
    R = sum(1 for r in otos if r["T"] in ("T1","T2","T3","T4","T5","T6")) / n
    H = sum(1 for r in otos if r["T"] == "T7") / n
    from collections import Counter
    mallit = Counter(r["norm"] for r in otos if r["T"] in ("T1","T2","T3"))
    K = max(mallit.values()) if mallit else 0
    print(f"n={n}  R={R:.2f}  K={K}  H={H:.2f}")
    print("luokat:", dict(Counter(r["T"] for r in otos)))
    print("korjausmallit (T1-T3):"); [print(f"  {c}× {m}") for m, c in mallit.most_common()]
    if K >= 3 and R >= 0.30: tulos = "PASS -> vaihtoehto B"
    elif K <= 1 or R < 0.15: tulos = "KILL"
    else: tulos = "UNKNOWN -> laajennus 40 riviin"
    print("TULKINTA:", tulos)
    print("\nkontrolli:", [(r["nimi"], r.get("versio"), r.get("vaihe"), r.get("tila"), r["T"], r.get("virhe","")[:120]) for r in kontrolli])
    json.dump({"R": R, "K": K, "H": H, "tulkinta": tulos, "rivit": otos, "kontrolli": kontrolli}, open("./kokeet/03-analyysi.json", "w"), ensure_ascii=False, indent=1)
