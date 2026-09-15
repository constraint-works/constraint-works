---
nimi: Protokollien vahtitehtävät (keeper-roolit)
tila: hypoteesi
kirjoittaja: claude
kierros: 2
aika_ekaan_euroon: 3
tuplaus: 2
skaala: 3
ai_etu: 3
paaoma: 2
laillisuus: 5
---

# Protokollien vahtitehtävät

## Mekanismi lyhyesti

DeFi-protokollat tarvitsevat ulkopuolisia kutsumaan funktioita: likvidaatiot, sadonkorjuu,
tasapainotus, oraakkelipäivitykset, vanhentuneiden positioiden sulkeminen. Ne maksavat
kutsujalle palkkion (likvidaatiobonus 5 - 15 %, kiinteä palkkio, osuus tuotosta). Kuka
tahansa voi tehdä sen. Tämä ei ole MEV: se on protokollan suunniteltu rooli.

## Neljä kysymystä

**Kuka maksaa?** Protokolla tai likvidoitava lainaaja, protokollan säännöillä.

**Miksi maksaa?** Ilman vahteja protokolla ei toimi. Palkkio on turvallisuuden hinta.

**Mikä estää muita?** Isoilla ketjuilla kilpailu on millisekunteja ja pääomaa. Pienillä ja
uusilla ketjuilla ja protokollilla vahteja ei ole tarpeeksi, ja palkkiot jäävät lunastamatta.

**Mikä on meidän etumme?** Kone kirjoittaa vahtibotin uudelle protokollalle tunnissa ja
voi valvoa kymmeniä pieniä protokollia, joita kukaan ammattilainen ei viitsi. Etu on
kattavuudessa, ei nopeudessa.

## Data

Ei vielä. Tehtävä: listaa 20 pientä tai uutta lainaprotokollaa L2-ketjuilla ja tarkista,
kuinka moni likvidaatio jää tekemättä yli 5 minuutiksi.

## Riskit ja eettinen tarkistus

- Likvidaatiot vaativat pääomaa (ostetaan vakuus). Osa tehtävistä vaatii vain gasia.
- Likvidointi on lainaajalle ikävää mutta sopimuksen mukaista ja protokollan terveydelle
  välttämätöntä. Ei sandwichia, ei front-runningia.

## Haaste

## Vastaus haasteeseen

## Seuraava askel

Tutkitaan vasta, jos agenttinatiivit ja oikeudet eivät tuota koetta.
