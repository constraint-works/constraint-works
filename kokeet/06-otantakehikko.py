#!/usr/bin/env python3
"""Koe 06: otantakehikon rakennus julkisista lähteistä. Ei valitse yrityksiä.

Syötteet (ladataan erikseen, eivät tule repoon):
  YTJ:  https://avoindata.prh.fi/opendata-ytj-api/v3/all_companies  (ZIP -> data_YYYYMMDD.json)
  Vero: https://www.vero.fi/.../yhteisö_tuloverotus_julk_2024.csv    (ISO-8859-1, ';')

Tuloste:
  --kehikko <polku>   kehikon CSV repon ULKOPUOLELLE (y-tunnus, nimi, tol, kunta, rek.pvm, vero)
  stdout              vain lukumäärät ja jakaumat (nämä saa committoida)
  --tiivistelma <polku>  sama JSON-muodossa (repoon)

Kriteerit (lukittu protokollassa kokeet/06-kylma-paasytesti-protokolla.md §4):
  K1 yhtiömuoto osakeyhtiö (companyForms type 16), ei julkinen (OYJ)
  K2 kaupparekisterissä, ei konkurssia/saneerausta/selvitystilaa (companySituations tyhjä)
  K3 arvonlisäverovelvollinen liiketoiminnasta (registeredEntries register 6, type 80, ei endDate)
  K4 työnantajarekisterissä (register 7, ei endDate)
  K5 ennakkoperintärekisterissä (register 5, ei endDate)
  K6 y-tunnus rekisteröity viimeistään 2021-06-30 (>= 5 v toimintaa ennen lukitusta)
  K7 päätoimiala TOL 2025 kaksinumerotasolla joukossa TOIMIALAT
  K8 Veron 2024 julkisissa tiedoissa maksuunpannut verot >= 10 000 €
  K9 poissulku: TOL 64-66 (rahoitus), 68 (kiinteistö), 69.2 (tilitoimistot ei kehikossa, ks. protokolla)
"""
import argparse, csv, io, json, sys, zipfile, collections, hashlib, datetime

TOIMIALAT = (
    [f"{i:02d}" for i in range(10, 34)]   # C teollisuus 10-33
    + ["41", "42", "43"]                 # F rakentaminen
    + ["46"]                             # G tukkukauppa
    + ["49", "50", "51", "52", "53"]     # H kuljetus ja varastointi
)
RAJAPVM = "2021-06-30"
VEROKYNNYS = 10000.0

def stream_objects(fh, chunk=1 << 20):
    """Iteroi JSON-taulukon objektit ilman koko tiedoston lataamista muistiin."""
    dec = json.JSONDecoder()
    buf = fh.read(chunk)
    i = buf.index('[') + 1
    while True:
        while i < len(buf) and buf[i] in ' \r\n\t,':
            i += 1
        if i >= len(buf) or buf[i] == ']':
            more = fh.read(chunk)
            if not more:
                return
            buf = buf[i:] + more
            i = 0
            continue
        try:
            obj, end = dec.raw_decode(buf, i)
        except json.JSONDecodeError:
            more = fh.read(chunk)
            if not more:
                return
            buf = buf[i:] + more
            i = 0
            continue
        yield obj
        i = end

def lue_vero(polku):
    verot = {}
    with open(polku, encoding="latin-1", newline="") as f:
        r = csv.reader(f, delimiter=";")
        next(r)
        for row in r:
            if len(row) < 6:
                continue
            try:
                verot[row[1].strip()] = float(row[5].replace(",", "."))
            except ValueError:
                pass
    return verot

def aktiivinen(entries, register, type_=None):
    for e in entries or []:
        if str(e.get("register")) == register and not e.get("endDate"):
            if type_ is None or str(e.get("type")) == type_:
                return True
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ytj", required=True, help="all_companies ZIP tai purettu JSON")
    ap.add_argument("--vero", required=True)
    ap.add_argument("--kehikko", required=True, help="kehikko-CSV repon ulkopuolelle")
    ap.add_argument("--tiivistelma", required=True, help="lukumäärä-JSON repoon")
    a = ap.parse_args()

    verot = lue_vero(a.vero)
    if a.ytj.endswith(".zip"):
        z = zipfile.ZipFile(a.ytj)
        name = [n for n in z.namelist() if n.endswith(".json")][0]
        fh = io.TextIOWrapper(z.open(name), encoding="utf-8")
    else:
        fh = open(a.ytj, encoding="utf-8")

    n = collections.Counter()
    tol2 = collections.Counter()
    verobandit = collections.Counter()
    kunnat = collections.Counter()
    ikaluokat = collections.Counter()
    rivit = []
    for c in stream_objects(fh):
        n["kaikki"] += 1
        forms = [f for f in (c.get("companyForms") or []) if not f.get("endDate")]
        if not any(str(f.get("type")) == "16" for f in forms):
            continue
        n["K1_oy"] += 1
        if str(c.get("tradeRegisterStatus")) != "1" or str(c.get("status")) != "2":
            continue
        if c.get("companySituations"):
            continue
        n["K2_rekisterissa_ei_tilanteita"] += 1
        re_ = c.get("registeredEntries")
        if not aktiivinen(re_, "6", "80"):
            continue
        n["K3_alv"] += 1
        if not aktiivinen(re_, "7"):
            continue
        n["K4_tyonantaja"] += 1
        if not aktiivinen(re_, "5"):
            continue
        n["K5_ennakkoperinta"] += 1
        rek = (c.get("businessId") or {}).get("registrationDate") or "9999"
        if rek > RAJAPVM:
            continue
        n["K6_ika"] += 1
        mbl = c.get("mainBusinessLine") or {}
        tol = str(mbl.get("type") or "")
        if tol[:2] not in TOIMIALAT:
            continue
        n["K7_toimiala"] += 1
        yt = (c.get("businessId") or {}).get("value", "")
        v = verot.get(yt)
        if v is None:
            n["K8_ei_verotiedoissa"] += 1
            continue
        if v < VEROKYNNYS:
            continue
        n["K8_vero_>=kynnys"] += 1
        nimi = next((x["name"] for x in c.get("names", []) if str(x.get("type")) == "1" and not x.get("endDate")), "")
        addr = (c.get("addresses") or [{}])[0]
        kunta = next((p.get("municipalityCode") for p in addr.get("postOffices", []) if p.get("languageCode") == "1"), "")
        tol2[tol[:2]] += 1
        verobandit["10-50k" if v < 50000 else "50-250k" if v < 250000 else ">250k"] += 1
        kunnat[kunta] += 1
        ika = 2026 - int(rek[:4])
        ikaluokat["5-9" if ika < 10 else "10-19" if ika < 20 else "20+"] += 1
        rivit.append([yt, nimi, tol, kunta, rek, f"{v:.2f}", "1" if c.get("website") else "0"])

    rivit.sort()
    with open(a.kehikko, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["y_tunnus", "nimi", "tol2025", "kunta", "rekisteroity", "verot_2024", "www_ytj"])
        w.writerows(rivit)
    h = hashlib.sha256(open(a.kehikko, "rb").read()).hexdigest()
    tiiv = {
        "luotu": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"),
        "kriteerit": {"toimialat": TOIMIALAT, "rekisteroity_viimeistaan": RAJAPVM, "verokynnys_eur": VEROKYNNYS},
        "suppilo": dict(n),
        "kehikko_n": len(rivit),
        "kehikko_sha256": h,
        "www_ytj_osuus": round(sum(1 for r in rivit if r[6] == "1") / max(1, len(rivit)), 3),
        "tol2_jakauma": dict(sorted(tol2.items())),
        "verobandit": dict(verobandit),
        "ikaluokat": dict(ikaluokat),
        "kunnat_top10": kunnat.most_common(10),
    }
    with open(a.tiivistelma, "w", encoding="utf-8") as f:
        json.dump(tiiv, f, ensure_ascii=False, indent=1)
    print(json.dumps(tiiv, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
