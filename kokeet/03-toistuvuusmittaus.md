# Koe 03: toistuvuusmittaus (PyPI-orvot, Python 3.14)

**Protokolla:** lukittu commitissa `71a760a` (`etsinta/KEHIKON-TUHOAMISYRITYS-V3.md` §8).
**Otos:** lukittu commitissa `07bab91` ennen yhdenkään rivin tarkastelua (`kokeet/03-otos.csv`).
**Ajo:** 2026-09-16 klo 14:46 - 15:00, `kokeet/03-aja.py`, raakadata `kokeet/03-tulokset.jsonl`.
**Analyysiskripti:** `kokeet/03-analysoi-esirekisteroity.py`, kirjoitettu ennen tulosten
näkemistä. Sen ja lukitun tekstin poikkeamat kirjattu alla; lukittu teksti ratkaisee.
**Raha:** 0 €. Ei yhteydenottoja. Mallien käyttö tilauksen sisällä.

## Perusjoukon valinta (kirjattu ennen ajoa, FACT)

Lukittu sääntö: se lista, jolla on koneellisesti toistettava epäonnistumissignaali; jos
molemmat toteutettavissa, PyPI. WordPress-signaali ei ollut toteutettavissa: `wp`, `php`
ja `mysql` puuttuvat koneelta. PyPI toteutettavissa: `python3.14` 3.14.6. **Valinta:
`data/orvot/pypi.org-orvot-top5000.csv`**, 959 riviä, joista lataukset ≥ 100 000/kk: 959.
Otos: 20 riviä, `random.Random(20260916).sample(...)`, kirjattu ja committoitu ennen ajoa.

## Toimenpide per rivi (FACT, protokollan mukaan)

Tuore venv `python3.14`, `pip install --no-binary :all: <paketti>==<PyPI:n info.version>`,
onnistuessa `python -c "import <moduuli>"` (moduulinimi `importlib.metadata.packages_distributions()`
-käänteishausta, ilman tulosta paketin nimi `-`/`.` → `_`), onnistuessa wheel-asennus tuoreeseen
venviin ja import. Aikaraja 5 min konetta per rivi, ei korjausyrityksiä. Virheilmoituksen
ensimmäinen rivi = ensimmäinen rivi, joka sisältää Error/Exception/failed/No module named.

## Kaikki 20 havaintoa + kontrolli (FACT)

| # | Paketti | Versio | Viimeinen vaihe | Tila | Kesto s | Virheilmoituksen ensimmäinen rivi | Luokka (lukittu teksti) |
|---|---|---|---|---|---|---|---|
| 1 | sparqlwrapper | 2.0.0 | wheel-import | onnistui | 13,3 | | T7 |
| 2 | backports.tarfile | 1.2.0 | wheel-import | onnistui | 6,1 | | T7 |
| 3 | textwrap3 | 0.9.2 | wheel-import | onnistui | 3,6 | | T7 |
| 4 | rstr | 3.2.2 | wheel-import | onnistui | 4,1 | | T7 |
| 5 | sphinxcontrib-jquery | 4.1 | wheel-import | onnistui | 33,7 | | T7 |
| 6 | telepath | 0.3.1 | lähde-import | epäonnistui | 2,3 | `ModuleNotFoundError: No module named 'django'` | T3 |
| 7 | s3cmd | 2.4.0 | wheel-import | onnistui | 8,9 | | T7 |
| 8 | spacy-loggers | 1.0.5 | wheel-import | onnistui | 3,7 | | T7 |
| 9 | funcsigs | 1.0.2 | wheel-import | onnistui | 3,6 | | T7 |
| 10 | python-lsp-jsonrpc | 1.1.2 | wheel-import | onnistui | 7,4 | | T7 |
| 11 | enum-compat | 0.0.3 | lähde-import | epäonnistui | 2,3 | `ModuleNotFoundError: No module named 'enum_compat'` | T3 |
| 12 | graphql-server-core | 2.0.0 | wheel-import | onnistui | 7,1 | | T7 |
| 13 | openapi-schema-pydantic | 1.2.4 | lähde-import | epäonnistui | 134,8 | `raise PydanticUserError('`const` is removed, use `Literal` instead', code='removed-kwargs')` | T3 |
| 14 | jcs | 0.2.1 | wheel-import | onnistui | 4,0 | | T7 |
| 15 | forbiddenfruit | 0.1.4 | wheel-import | onnistui | 3,5 | | T7 |
| 16 | pip-hello-world | 0.1 | wheel-import | onnistui | 3,7 | | T7 |
| 17 | azure-mgmt-machinelearningcompute | 0.4.1 | lähde-import | epäonnistui | 31,8 | `ModuleNotFoundError: No module named 'pkg_resources'` | T1 |
| 18 | pytest-shard | 0.1.2 | wheel-import | onnistui | 7,8 | | T7 |
| 19 | scrapbook | 0.5.0 | lähdeasennus | epäonnistui (aikaraja 300 s) | 299,2 | (tyhjä: aikaraja ylittyi rakennusvaiheessa) | T1 |
| 20 | pyro-api | 0.1.2 | wheel-import | onnistui | 4,0 | | T7 |
| K | html5lib (positiivinen kontrolli) | 1.1 | lähdeasennus | epäonnistui | 1,9 | `error: subprocess-exited-with-error` (pipin kääre; taustalla pkg_resources, koe 02) | T1 |

Yhdelläkään otoksen paketilla ei ollut advisoryä (`kokeet/03-otos.csv`), joten T6 ei
tullut kyseeseen; onnistuneet ovat T7.

## Luokitteluperusteet (lukittu teksti: "virheilmoituksen ensimmäinen rivi ratkaisee; kaksi sopii → pienempi numero")

- **6 telepath:** import vaatii djangon, jota lähdeasennus ei tuonut. Ensimmäinen rivi ei
  nimeä rakennusinfraa (T1) eikä kieliversiota (T2); se on riippuvuuden puuttuminen
  ajossa. Esirekisteröity skripti luokitteli `ModuleNotFoundError` → T3. Sovellettu T3.
  Huomio: on tulkittavissa myös puuttuvaksi riippuvuusmäärittelyksi (pakkaus), mutta
  ensimmäinen rivi ei sano sitä.
- **11 enum-compat:** paketti on metapaketti ilman importoitavaa moduulia (asentaa
  `enum34`:n vanhoille Pythoneille). Importnimi-sääntö tuotti `enum_compat`, jota ei ole.
  Protokollan mukaan tämä on epäonnistuminen importissa → T3 (esirekisteröity sääntö).
  **Protokollan artefakti:** paketti toimii tarkoitetusti. Kirjataan, ei muuteta.
- **13 openapi-schema-pydantic:** pydantic 2 poisti `const`-argumentin. Lukittu teksti:
  T3 "riippuvuuden poistettu tai muuttunut API". Esirekisteröity regex ei tunnistanut
  riviä ja olisi antanut T5. **Teksti ratkaisee: T3.** Ei vaikuta R:ään eikä H:hon;
  vaikuttaa K:hon vain siten, että rivi kuuluu T1 - T3 -joukkoon (yksittäinen malli).
- **17 azure-mgmt-machinelearningcompute:** `pkg_resources` nimetty T1:ssä eksplisiittisesti. T1.
- **19 scrapbook:** rakennusvaihe ylitti 5 min (riippuvuuspuu: papermill, pandas ym.
  lähteestä). Epäonnistui vaiheessa 1 → T1 (rakennusinfra). Ei virheriviä, koska
  prosessi katkaistiin. **Huomio:** tämä on aikarajan tuottama epäonnistuminen, ei
  todennettu rikkoutuminen. Protokolla ei erottele; kirjataan T1.

## Mittarit lukitulla tavalla (CALC)

- **R** = (T1 - T6) / 20 = (2 + 0 + 3 + 0 + 0 + 0) / 20 = **5/20 = 0,25**
- **K** = suurin yksittäinen korjausmalli T1 - T3:ssa, normalisointi "versionumerot ja
  polut poistettu": viisi eri virheilmoitusta (django, enum_compat, PydanticUserError,
  pkg_resources, tyhjä) → jokaista 1 → **K = 1**
- **H** = T7 / 20 = **15/20 = 0,75**

**Esirekisteröidyn skriptin poikkeama:** skripti korvasi lisäksi lainausmerkeissä olevat
nimet `'X'`:llä, jolloin kolme `No module named` -riviä yhdistyivät ja K olisi 3 →
"UNKNOWN, laajennus 40 riviin". Lukittu teksti sallii vain versionumeroiden ja polkujen
poiston. **Sovellettu lukittua tekstiä: K = 1.** Skriptin tulos kirjataan
herkkyystarkasteluna, ei tuloksena. Sisällöllisesti kolme `No module named` -riviä eivät
ole sama korjausmalli: yksi on puuttuva riippuvuus (django), yksi metapaketin
importnimi (enum_compat), yksi setuptoolsin poisto (pkg_resources). Lukitun tekstin
tiukempi normalisointi oli tässä oikeassa.

## Tulos kynnyksillä (mekaanisesti)

- PASS vaatii K ≥ 3 ja R ≥ 0,30: **ei täyty** (K = 1, R = 0,25).
- KILL, jos K ≤ 1 tai R < 0,15: **K = 1 täyttyy.**
- **TULOS: KILL.** Artefakti-S-haara kuolee tässä luokassa (PyPI:n ladatuimmat orvot,
  Python 3.14 -yhteensopivuus). Vaihtoehtoa B ei ajeta tälle luokalle. Otosta ei
  laajenneta (laajennus kuului vain UNKNOWN-tulokseen).
- Protokollan mukaan toinen lista (WordPress) voidaan ajaa samalla protokollalla kerran.
  Se ei ollut toteutettavissa tällä koneella. Ei ajettu.

**Herkkyys (ei muuta tulosta):** jos rivi 11 luetaan protokollan artefaktiksi ja rivi 19
aikarajaksi eikä rikkoutumiseksi, R = 3/20 = 0,15 ja K = 1 → KILL. Jos skriptin
laajempi normalisointi hyväksyttäisiin, K = 3 ja R = 0,25 → UNKNOWN. Kumpikaan
ei tuota PASSia.

**Sivutuote H:** 15/20 ladatuimmista PyPI-orvoista (ei julkaisua 2 vuoteen, ≥ 100 k
latausta/kk) asentuu ja importoituu Python 3.14:llä sekä lähteestä että wheelinä.
GPT:n esikokeessa 10/12 rakentui. Yhdistettynä (eri otannat, sama suunta): "orpo" on
tässä luokassa pääosin "valmis", ei "rikki".

## Mitä tulos muuttaa nykyisessä kehikossa (vasta tuloksen jälkeen)

1. **Pöytätestin P3 kaatuu PyPI-orpoluokassa.** Toistuvaa korjattavaa ei ole; viisi
   epäonnistumista ovat viisi eri syytä. Uudelleenkäytettävää korjaustietoa ei voi syntyä
   luokasta, jossa jokainen rikkoutuminen on erilainen. Haara suljetaan tässä luokassa.
2. **"Orpo = rikki" -premissi heikkenee kolmannen kerran** (npm 1/3 valmiita, GPT 10/12,
   nyt 15/20). ORVOT-muistioon kirjataan H = 0,75 arvion "valmis vs. hylätty" tilalle.
3. **Pakotetut alustamigraatiot -kortin Python-versiopremissi heikkenee:** Python 3.14
   rikkoi lähteestä 2/20 (pkg_resources, aikaraja) ja riippuvuuden API-muutos 1/20.
   Kortti ei kuole (WordPress- ja Manifest-tapaukset mittaamatta), mutta PyPI ei ole
   sen todiste.
4. **Kehikko itse toimi:** pöytätesti tappoi haaran alle tunnissa ja 0 eurolla, ennen
   yhtään A/B:tä. Se oli tarkoitus. Ei muutosta PROSESSI.md:hen.
5. **Ei muutosta STATE-, CAPTURE- tai BASELINE-päätelmiin:** koe ei mitannut niitä.

## Mitä koe ei kerro

Auttaako artefakti-S jossain toisessa luokassa (WordPress, npm, Manifest V3), maksaako
kukaan, mitä T7-pakettien 75 % tarkoittaa niiden käyttäjille. Otos on 20, eikä
tulos yleisty muihin ekosysteemeihin.
