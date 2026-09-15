# eikaisiinä

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
