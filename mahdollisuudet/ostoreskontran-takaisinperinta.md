---
nimi: Ostoreskontran takaisinperintä pk-yrityksille (recovery audit)
tila: hypoteesi
kirjoittaja: claude
kierros: yövuoro 1, avoin haara
generaattori: kyllä
aika_ekaan_euroon: 2
tuplaus: 2
skaala: 3
ai_etu: 4
paaoma: 5
laillisuus: 4
---

# Ostoreskontran takaisinperintä pk-yrityksille

## Mekanismi lyhyesti

Yritykset maksavat ostolaskuja tuplana, väärällä hinnalla, ilman sovittua alennusta tai
hyvityksen jäädessä käyttämättä. Suuryrityksille tätä tekee toimiala (PRGX, apexanalytix)
menestyspalkkiolla: 20 - 30 % palautuksesta, tyypillinen palautus 0,1 % ostoista (FACT,
apexanalytix). Pk-yrityksille kukaan ei tee, koska ihmisen tekemä tarkastus maksaa
enemmän kuin palautus. Tekoäly lukee kaikki laskut nollakustannuksella, ja Suomessa
verkkolaskudata on rakenteista ja kirjanpito-ohjelmissa rajapinnan takana (Procountor,
Netvisor: FACT, API olemassa, maksullinen).

Tämä on lähtökysymyksen puhtain tapaus: **arvotonta, koska tarkastus vaati työtä; arvokasta,
koska tarkastus on ilmaista.** Raha on jo siirtynyt väärään paikkaan ja odottaa hakijaa.

## Neljä kysymystä

**Kuka maksaa?** Pk-yritys, menestyspalkkiona palautuksesta. Toimittaja palauttaa.

**Miksi maksaa?** Ilmaista rahaa, ei riskiä. Sama syy kuin suuryrityksillä.

**Mikä estää muita?** Pääsy kirjanpitodataan (valtuutus, luottamus, integraatio).
Kirjanpito-ohjelmat voisivat tehdä tämän itse; eivät ole tehneet. Tilitoimistot voisivat;
niillä ei ole insentiiviä (tuntilaskutus).

**Mikä on meidän etumme?** Sama valtakirja avaa monta oikeutta: tuplamaksut,
viivästyskorko + 40 € (oikeuskartoitus #3), alv-palautus (#4), sopimushintojen
tarkastus. Yksi integraatio, monta generaattoria. Datasilmukka: jokainen asiakas
parantaa tunnistusta.

## Data

- Palautus 0,1 - 0,5 % ostoista (toissijaiset lähteet, toimialan omat väitteet, ei
  riippumatonta tutkimusta löydetty: UNKNOWN todellinen taso pk-yrityksissä).
- Pk-yritys, 2 M € ostot → 2 000 - 10 000 €/v → palkkio 500 - 3 000 €/v/asiakas (CALC).
- Suomesta ei löytynyt pk-yrityksille suunnattua toimijaa (haku 2026-09-16, ei löydöksiä;
  UNKNOWN, ei todiste puuttumisesta).

## Riskit ja eettinen tarkistys

- Pääsy pk-yrityksen ostolaskuihin on luottamuksellista dataa: GDPR (henkilötietoja
  laskuissa), salassapito, kirjanpitolain säilytys. Vaatii sopimuksen ja huolellisuuden.
- Jos raha kulkee meidän kauttamme, se voi olla perintää (AVI-lupa). Rakenne: asiakas
  perii itse, me tuotamme listan ja laskutamme palkkion. Sama kuin oikeuskartoituksessa.
- Todellinen virhetaso pk-yrityksissä voi olla pienempi (vähemmän laskuja, tutummat
  toimittajat) tai suurempi (ei kontrolleja). Tuntematon, mitattava.
- Ensimmäinen asiakas vaatii omistajalta ihmissuhteen. Sama pullonkaula kuin lähdeverossa.

## Haaste

## Vastaus haasteeseen

## Seuraava askel

Yksi pk-yritys, jonka kirjanpitäjä tai omistaja on tuttu. Vie 2 - 3 vuoden ostolaskut
CSV:nä (ei rajapintaa vielä), aja tuplamaksu- ja hyvitystarkastus. Mittari: löytyikö
euroakaan. Jos 0 € kolmesta yrityksestä, hylkää.
