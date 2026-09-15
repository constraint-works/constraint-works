---
nimi: Pysyvät bug bounty -ohjelmat (Immunefi)
tila: tutkittu
kirjoittaja: claude
aika_ekaan_euroon: 2
tuplaus: 2
skaala: 4
ai_etu: 4
paaoma: 5
laillisuus: 5
---

# Pysyvät bug bounty -ohjelmat (Immunefi)

## Mekanismi lyhyesti

175 protokollaa pitää auki pysyvän potin, yhteensä noin 110 M USD maksimipalkkioita.
Kriittinen löytö maksaa 1 - 15 M USD, keskivakava 5 000 - 50 000 USD.

## Neljä kysymystä

**Kuka maksaa?** Protokollan kassa.

**Miksi maksaa?** Löydön ostaminen on halvempaa kuin hakkeroiduksi tuleminen.

**Mikä estää muita?** Koodi on auditoitu monesti. Löydöt ovat harvinaisia ja vaativat
syvää ymmärrystä. Ensimmäinen raportoija saa rahat.

**Mikä on meidän etumme?** Rinnakkainen, väsymätön lukeminen. Erityisesti äskettäin
päivittynyt koodi on vähiten tutkittua.

## Data

- `tyokalut/haku/hae_immunefi.py` listaa kaikki ohjelmat, päivityspäivät ja maksimit.
- 30 ohjelmaa maksaa vähintään 1 M USD kriittisestä.

## Riskit ja eettinen tarkistus

- Raportoidaan vain ohjelman kautta, ei koskaan hyödynnetä. Ei testata mainnetissä
  ellei ohjelma nimenomaan salli.
- Todennäköisyys yhdelle löydölle on matala, mutta odotusarvo voi silti olla korkea.
  Tämä on lottokuponki, jossa älykkyys parantaa kertoimia.

## Haaste

## Vastaus haasteeseen

## Seuraava askel

Ei ensimmäiseksi testiksi: liian hidas ja epävarma. Pidetään taustalla: ajetaan
rinnakkaisia lukijoita kun muut kokeet odottavat tuloksia.
