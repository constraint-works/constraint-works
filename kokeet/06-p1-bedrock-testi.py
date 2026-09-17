#!/usr/bin/env python3
"""Koe 06, P1: Amazon Bedrock -toteutuksen todentaminen ILMAN asiakasdataa.

Todentaa omistajan ehdot 1 - 4 (päätös 2026-09-17) bedrock-runtime-päätepisteellä:
  1. tilin data retention -tila on `none` valitulla EU-alueella (Control Plane API)
  2. valittu Claude-malli toimii tilassa `none`: kun tila on `none`, säilytystä vaativa malli
     palauttaa ValidationExceptionin, joten onnistunut kutsu todistaa ehdon (AWS:n dokumentaatio,
     data-retention.html: "Amazon Bedrock will block the request and return an error")
  3. kutsu tehdään vain EU Geographic Cross-Region -profiililla (id alkaa "eu.") EU-alueen
     päätepisteessä; "global."-profiilit hylätään
  4. yksi harmiton testikutsu per ehdokasmalli, ei asiakasdataa

Avain luetaan ympäristömuuttujasta AWS_BEARER_TOKEN_BEDROCK (tai BEDROCK_API_KEY). Avainta ei
tulosteta eikä tallenneta. Tulos JSON-tiedostoon ilman salaisuuksia ja ilman tilinumeroa.

Käyttö:
  AWS_BEARER_TOKEN_BEDROCK=... python3 kokeet/06-p1-bedrock-testi.py --alue eu-north-1 --tulos <polku.json>
"""
import argparse, json, os, sys, urllib.request, urllib.error, urllib.parse, datetime, re

EHDOKKAAT = ["eu.anthropic.claude-sonnet-4-6", "eu.anthropic.claude-sonnet-5",
             "eu.anthropic.claude-haiku-4-5-20251001-v1:0", "eu.anthropic.claude-opus-4-8"]

def kutsu(method, url, key, body=None):
    req = urllib.request.Request(url, method=method, data=(json.dumps(body).encode() if body is not None else None))
    req.add_header("Authorization", "Bearer " + key); req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, {"virhe": re.sub(r"\d{12}", "<tili>", e.read().decode()[:500])}
    except Exception as e:
        return 0, {"virhe": repr(e)[:300]}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alue", required=True); ap.add_argument("--tulos", required=True)
    ap.add_argument("--mallit", default=",".join(EHDOKKAAT))
    a = ap.parse_args()
    if not a.alue.startswith("eu-"): sys.exit("Ehto 3: vain EU-alue sallitaan.")
    key = os.environ.get("AWS_BEARER_TOKEN_BEDROCK") or os.environ.get("BEDROCK_API_KEY")
    if not key: sys.exit("Avain puuttuu ympäristöstä (AWS_BEARER_TOKEN_BEDROCK).")
    cp = f"https://bedrock.{a.alue}.amazonaws.com"; rt = f"https://bedrock-runtime.{a.alue}.amazonaws.com"
    t = {"aika": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"), "alue": a.alue, "ehdot": {}}

    s1, b1 = kutsu("PUT", cp + "/data-retention", key, {"mode": "none"})
    s2, b2 = kutsu("GET", cp + "/data-retention", key)
    t["ehdot"]["1_retention_none"] = {"put": [s1, b1], "get": [s2, b2], "ok": s2 == 200 and b2.get("mode") == "none"}

    mallit = [m.strip() for m in a.mallit.split(",") if m.strip()]
    hylatyt = [m for m in mallit if not m.startswith("eu.")]
    t["ehdot"]["3_vain_eu"] = {"paatepiste": rt, "profiilit": mallit, "hylatyt_ei_eu": hylatyt, "ok": not hylatyt}

    kokeet = {}
    for m in [x for x in mallit if x.startswith("eu.")]:
        s, b = kutsu("POST", f"{rt}/model/{urllib.parse.quote(m, safe='')}/converse", key,
                     {"messages": [{"role": "user", "content": [{"text": "Vastaa yhdellä sanalla: OK"}]}], "inferenceConfig": {"maxTokens": 16}})
        teksti = "".join(c.get("text", "") for c in (((b.get("output") or {}).get("message") or {}).get("content") or []))
        kokeet[m] = {"http": s, "vastaus": teksti[:40], "virhe": b.get("virhe"), "ok": s == 200 and bool(teksti)}
    t["ehdot"]["2_ja_4_mallit_tilassa_none"] = {"kokeet": kokeet, "toimivat": [m for m, r in kokeet.items() if r["ok"]],
                                               "ok": t["ehdot"]["1_retention_none"]["ok"] and any(r["ok"] for r in kokeet.values())}
    t["kaikki_ok"] = all(v.get("ok") for v in t["ehdot"].values())
    t["johtopaatos"] = ("Todennettu: sopimukseen kirjataan yksi toimivista malleista, retention none, EU-profiili ja tämä alue."
                        if t["kaikki_ok"] else "Ehdot eivät täyty. Ehtoja EI löysätä. Fallback: Anthropicin oma API todellisella retentionilla.")
    json.dump(t, open(a.tulos, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v.get("ok") for k, v in t["ehdot"].items()}), "| kaikki_ok:", t["kaikki_ok"]); print(t["johtopaatos"])

if __name__ == "__main__":
    main()
