#!/usr/bin/env python3
"""Koe 06, P1: Amazon Bedrock -toteutuksen todentaminen ILMAN asiakasdataa.

Todentaa omistajan ehdot 1 - 4 (päätös 2026-09-17):
  1. tilin data retention -tila on `none` valitulla EU-alueella
  2. valittu Claude-malli toimii tilassa `none` (allowed_modes sisältää "none")
  3. kutsu tehdään vain EU-alueen sisäisellä tai EU Geographic Cross-Region -päätepisteellä
     (ei koskaan global-profiililla)
  4. yksi harmiton testikutsu onnistuu näillä asetuksilla

Avain luetaan ympäristömuuttujasta BEDROCK_API_KEY. Avainta ei tulosteta eikä tallenneta.
Tulos kirjoitetaan JSON-tiedostoon ilman salaisuuksia. TESTAAMATON ennen tilin luontia:
päätepisteet ja polut ovat AWS:n dokumentaatiosta (data-retention.html, luettu 2026-09-17);
jos rajapinta poikkeaa, skripti tulostaa raakavirheen eikä arvaa.

Käyttö:
  BEDROCK_API_KEY=... python3 kokeet/06-p1-bedrock-testi.py --alue eu-north-1 --tulos <polku.json>
"""
import argparse, json, os, sys, urllib.request, urllib.error, datetime

def kutsu(method, url, key, body=None):
    req = urllib.request.Request(url, method=method, data=(json.dumps(body).encode() if body is not None else None))
    req.add_header("x-api-key", key); req.add_header("Content-Type", "application/json")
    req.add_header("anthropic-version", "2023-06-01")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode() or "{}"), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, {"virhe": e.read().decode()[:600]}, dict(e.headers or {})
    except Exception as e:
        return 0, {"virhe": repr(e)}, {}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alue", required=True, help="EU-alue, esim. eu-north-1, eu-central-1, eu-west-1")
    ap.add_argument("--tulos", required=True)
    ap.add_argument("--malli", default="", help="pakota tietty malli-id; muuten valitaan ensimmäinen, joka sallii tilan none")
    a = ap.parse_args()
    if not a.alue.startswith("eu-"):
        sys.exit("Ehto 3: vain EU-alue sallitaan.")
    key = os.environ.get("BEDROCK_API_KEY")
    if not key:
        sys.exit("BEDROCK_API_KEY puuttuu ympäristöstä.")
    base = f"https://bedrock-mantle.{a.alue}.api.aws"
    tulos = {"aika": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"), "alue": a.alue, "paatepiste": base, "ehdot": {}}

    # Ehto 1: aseta ja lue retention-tila
    s, b, _ = kutsu("PUT", base + "/v1/data_retention", key, {"mode": "none"})
    s2, b2, _ = kutsu("GET", base + "/v1/data_retention", key)
    tulos["ehdot"]["1_retention_none"] = {"put": [s, b], "get": [s2, b2], "ok": s2 == 200 and b2.get("mode") == "none"}

    # Ehto 2: mallit ja niiden allowed_modes
    s3, b3, _ = kutsu("GET", base + "/v1/models", key)
    mallit = []
    for m in (b3.get("data") or b3.get("models") or []):
        mid = m.get("id", "")
        if "claude" not in mid.lower():
            continue
        dr = m.get("data_retention") or {}
        if not dr:  # listaus ei välttämättä sisällä kenttää; hae mallikohtaisesti
            _, bm, _ = kutsu("GET", base + "/v1/models/" + mid, key)
            dr = bm.get("data_retention") or {}; m = {**m, **bm}
        mallit.append({"id": mid, "status": m.get("status"), "mode": dr.get("mode"), "allowed_modes": dr.get("allowed_modes")})
    kelpaavat = [m for m in mallit if m["allowed_modes"] and "none" in m["allowed_modes"] and m["status"] != "unavailable" and "global" not in m["id"].lower()]
    valittu = a.malli or (kelpaavat[0]["id"] if kelpaavat else "")
    tulos["ehdot"]["2_malli_sallii_none"] = {"http": s3, "claude_mallit": mallit, "kelpaavat": [m["id"] for m in kelpaavat], "valittu": valittu,
                                             "ok": bool(valittu) and any(m["id"] == valittu for m in kelpaavat)}

    # Ehto 3: päätepiste on EU-alueen; malli-id ei ole global-profiili
    tulos["ehdot"]["3_vain_eu"] = {"paatepiste_eu": a.alue.startswith("eu-"), "malli_ei_global": bool(valittu) and "global" not in valittu.lower(),
                                    "ok": a.alue.startswith("eu-") and bool(valittu) and "global" not in valittu.lower()}

    # Ehto 4: harmiton testikutsu (ei asiakasdataa)
    if valittu:
        s4, b4, h4 = kutsu("POST", base + "/v1/messages", key, {"model": valittu, "max_tokens": 16,
                           "messages": [{"role": "user", "content": "Vastaa yhdellä sanalla: OK"}]})
        teksti = "".join(x.get("text", "") for x in (b4.get("content") or []) if isinstance(x, dict))
        tulos["ehdot"]["4_testikutsu"] = {"http": s4, "vastaus": teksti[:40], "virhe": b4.get("virhe"),
                                          "otsakkeet_alue": {k: v for k, v in h4.items() if "region" in k.lower() or "amzn" in k.lower()},
                                          "ok": s4 == 200 and bool(teksti)}
    else:
        tulos["ehdot"]["4_testikutsu"] = {"ok": False, "virhe": "ei kelpaavaa mallia"}

    tulos["kaikki_ok"] = all(v.get("ok") for v in tulos["ehdot"].values())
    tulos["johtopaatos"] = ("Bedrock-toteutus todennettu: kirjaa sopimukseen tämä malli, retention none ja tämä alue."
                            if tulos["kaikki_ok"] else "Ehdot eivät täyty: EI löysätä ehtoja. Fallback: Anthropicin oma API todellisella retentionilla.")
    json.dump(tulos, open(a.tulos, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v.get("ok") for k, v in tulos["ehdot"].items()}, ensure_ascii=False), "| kaikki_ok:", tulos["kaikki_ok"])
    print(tulos["johtopaatos"])

if __name__ == "__main__":
    main()
