# eikaisiinä

**Constraint Works** is the public research identity of this project. English summary of
the measured results: [`etsinta/JULKAISU-1.md`](etsinta/JULKAISU-1.md). The rest of the
repository is in Finnish: memos, pre-registered protocols, raw samples and both AI models'
cross-reviews. The author's identity is not part of the project.

Tutkimusprojekti: onko olemassa laillisia mekanismeja, joissa tekoäly antaa
poikkeuksellisen suuren taloudellisen vivun. Lähtöpääoma 1 000 €. Tavoite 10 000 000 €.
Ensimmäinen todellinen testi: 1 000 € → 2 000 € tavalla, joka ei onnistuisi ilman tekoälyä.

Tehdään yhdessä Clauden ja GPT:n kanssa. Mallit haastavat toisiaan. Hypoteesi ei ole
"tämä onnistuu" vaan "selvitetään avoimesti, onnistuuko".

## Ehdoton periaate

Kaikki laillista ja eettisesti puolustettavaa. Ei varastamista, huijaamista, manipulointia
eikä haavoittuvuuden hyödyntämistä ilman lupaa.

## Rakenne

```
PROSESSI.md        säännöt, neljä kysymystä, pisteytys, kahden mallin protokolla
GPT-OHJE.md        mistä toinen malli aloittaa
mahdollisuudet/    yksi kortti per mekanismi, myös hylätyt
kokeet/            yksi tiedosto per koe: budjetti, ehto, loki, tulos
kirjanpito/        ledger.csv (jokainen euro), paatokset.md (jokainen päätös)
etsinta/           lähdelista ja uusien mekanismien generaattori
tyokalut/          rekisteri.py (ranking), haku/ (datahaut)
```

## Käyttö

```
python3 tyokalut/rekisteri.py            ranking
python3 tyokalut/rekisteri.py --kaikki   myös hylätyt
python3 tyokalut/haku/hae_immunefi.py    pysyvät bountyt
python3 tyokalut/haku/hae_kilpailut.py   auditointikilpailujen historia
```

## Tilanne

Ks. `kirjanpito/paatokset.md` ja `python3 tyokalut/rekisteri.py`.

Yövuoro 1 (2026-09-16): orvot digitaaliset omaisuudet mitattu ja hylätty mekanismina
(`etsinta/ORVOT-OMAISUUDET.md`), hypoteesi muotoiltu uudelleen: tekoäly tekee työn
ilmaiseksi ja arvo siirtyy portteihin (oikeus, luottamus, pääsy, vastuu). Avoin haara
löysi puhtaan esimerkin: auktorisoitu kääntäjä harvinaisessa kielessä
(`etsinta/AVOIN-HAARA-2.md`). Loki: `etsinta/YO-CLAUDE.md`.

```
python3 tyokalut/haku/hae_orvot_paketit.py npmjs.org 50     npm/PyPI-orvot (ecosyste.ms)
python3 tyokalut/haku/hae_orvot_wordpress.py 40             WordPress-orvot (julkinen API)
python3 tyokalut/haku/hae_orvot_laajennukset.py <csv> 130   Chrome Web Store -otos
```
