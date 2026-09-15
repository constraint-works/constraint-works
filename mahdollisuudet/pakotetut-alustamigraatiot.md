---
nimi: Pakotetut alustamigraatiot omistajan lukuun
tila: hypoteesi
kirjoittaja: claude
kierros: yövuoro 1
generaattori: kyllä
aika_ekaan_euroon: 3
tuplaus: 2
skaala: 3
ai_etu: 4
paaoma: 5
laillisuus: 5
---

# Pakotetut alustamigraatiot omistajan lukuun

## Mekanismi lyhyesti

Alustat muuttavat sääntöjä julkisella aikataululla: Manifest V3 (Chrome 2025), DSA-
kauppiastiedot (App Store 2025-02, 135 000 sovellusta pois), Google Playn API-tasot ja
laatuvaatimukset (1,6 M sovellusta pois 2024 - 2025), WordPressin "tested up to"
(2 353 suosituinta lisäosaa varoituksella), Shopifyn API-versiot, Python- ja Node-
versiot. Jokainen määräaika orpouttaa omaisuutta, jolla on käyttäjiä ja omistaja, joka
haluaisi pitää sen mutta ei tee tylsää migraatiotyötä. Tekoäly tekee työn, omistaja
painaa julkaisunappia. Oikeudet eivät liiku, joten luottamusongelma katoaa.

## Neljä kysymystä

**Kuka maksaa?** Omaisuuden omistaja, jolla on käyttäjiä ja määräaika.

**Miksi maksaa?** Vaihtoehto on menettää omaisuus (23 % yli 10 k käyttäjän laajennuksista
poistettiin 20 kk:ssa). Määräaika tekee päätöksen puolesta.

**Mikä estää muita?** Ei paljon. Agentit tekevät migraatioita. Etu on **kohdentamisessa**:
skanneri, joka löytää ennen määräaikaa omaisuudet, joilla on käyttäjiä mutta ei
migraatiota, ja ottaa yhteyttä. Se on generaattori: yksi skanneri per alusta per
sääntömuutos.

**Mikä on meidän etumme?** Työ on täsmälleen sitä, minkä tekoäly tekee ilmaiseksi
(html5lib: 13 s). Ihmisen osuus on yhteydenotto ja laskutus. Ei omistajanvaihdosta.

## Data

- `etsinta/ORVOT-OMAISUUDET.md`: MV2-poisto, DSA, Play, WordPress-varoitukset.
- WordPress: 166 orpoa yli 10 k asennuksella, 153 yksityishenkilöiden. Näistä osalla
  omistaja on tavoitettavissa (profiili, sähköposti readme:ssä).
- Manifest V3 -aikataulu: FACT developer.chrome.com. MV2 estetty 2025-07, listaukset
  poistettu 2026-08-31.

## Riskit ja eettinen tarkistus

- Omistajat eivät vastaa (80 issuen otos: 7/40 ei vastannut edes vapaaehtoisille).
- Migraatio voi olla mahdoton (MV2 → MV3 rikkoi adblockerit periaatteessa).
- Hinta: omistaja, joka ei tehnyt 10 tunnin työtä, ei ehkä maksa 200 €. Testattava.
- Kylmä yhteydenotto skannerin perusteella on spämmin rajalla. Sama "generoitu tarjous"
  -ongelma kuin ylläpitotarjouksissa. Ratkaisu: julkinen työkalu, joka näyttää
  omistajalle itselleen, mitä migraatio vaatii, ei massaposti.

## Haaste

## Vastaus haasteeseen

## Seuraava askel

Valitse yksi tuleva määräaika (esim. WordPress 7.2, Google Playn seuraava API-taso,
Python 3.15) ja rakenna skanneri, joka listaa omaisuudet, joilla on käyttäjiä ja jotka
eivät ole migroineet. Ota yhteyttä kymmeneen omistajaan. Mittari: vastausprosentti ja
maksuhalukkuus, ei euro.
