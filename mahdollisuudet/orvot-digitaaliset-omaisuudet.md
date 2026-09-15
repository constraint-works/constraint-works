---
nimi: Orvot digitaaliset omaisuudet, joilla on käyttäjiä
tila: hylätty
kirjoittaja: claude
kierros: 3
generaattori: kyllä
aika_ekaan_euroon: 2
tuplaus: 1
skaala: 4
ai_etu: 3
paaoma: 4
laillisuus: 5
---

# Orvot digitaaliset omaisuudet, joilla on käyttäjiä

## Mekanismi lyhyesti

Ks. `etsinta/AVOIN-HAARA.md`, kohta 1. Ostetaan tai otetaan laillisesti vastaan
hylättyjä sovelluksia, laajennuksia, uutiskirjeitä ja projekteja, joilla on käyttäjiä.
Ylläpito on tekoälyllä lähes ilmaista, käyttäjät ovat niukkoja.

## Neljä kysymystä

**Kuka maksaa?** Käyttäjät (maltillinen maksullinen taso) tai ristiinmarkkinoinnin
kautta seuraava tuote.

**Miksi maksaa?** Työkalu, jota he jo käyttävät, jatkaa toimintaansa ja paranee.

**Mikä estää muita?** Kukaan ei etsi näitä systemaattisesti, koska ylläpito oli tähän
asti kannattamatonta. Löytäminen vaatii skannausta.

**Mikä on meidän etumme?** Ylläpidon hinta. Omaisuus, jonka arvo omistajalle on 0,
on meille positiivinen. Ja skanneri on generaattori.

## Data (2026-09-16, GitHub-rajapinta)

- Repoja, joilla on yli 1 000 tähteä, ei arkistoitu, ei yhtään commitia kahteen vuoteen:
  **17 616**. Yli 200 tähteä: 104 389.
- Niistä Chrome-laajennuksia (topic): 35 yli 1 000 tähden, 153 yli 200 tähden.
- Avoimia "looking for maintainer" -issueita: **3 835**.

Tähdet eivät ole käyttäjiä, mutta korreloivat. Kohteita on siis kymmeniä tuhansia, ja
kukaan ei skannaa niitä systemaattisesti ylläpidon näkökulmasta. Chrome Web Storen ja
App Storen vastaava luku on vielä hakematta (ei julkista rajapintaa, vaatii selaimen).

## Riskit ja eettinen tarkistus

- Omistus siirtyy sopimuksella, käyttäjille ilmoitetaan. Ei tietojen myyntiä, ei
  haitallista koodia (laajennusten kaappaus haittaohjelmiin on tunnettu rikos, ja sen
  varjo on tämän mekanismin suurin maineriski). Toimitaan avoimesti.
- Alustariski: Manifest V2 -laajennukset ovat kuolleet, vanhat iOS-sovellukset vaativat
  uudelleenrakennuksen.

## Hylkäyksen syy (2026-09-16, Claude)

Mitattu yövuorossa 1, ks. `etsinta/ORVOT-OMAISUUDET.md`. Omaisuutta on paljon ja siirto on
laillista, mutta (1) käyttäjät eivät maksa ja siirtyvät haarautumaan, (2) listattu omaisuus
on kallista (5x tulo), (3) listaamaton annetaan pois ilmaiseksi mutta pullonkaula on
omistajan luottamus ja julkaisuoikeus, ei koodi, (4) ostajamarkkina on haitallisten
hallussa ja jokainen omistajanvaihdos näyttää hyökkäykseltä. Mekanismi elää kahdessa
muodossa, jotka ovat omat korttinsa: `pakotetut-alustamigraatiot` ja jatkaja-palvelu
(HeroDevs-malli, vaatii todennetun historian, ks. `etsinta/COMPOUNDING.md`).

## Haaste

## Vastaus haasteeseen

## Seuraava askel

Skanneri Chrome Web Storeen ja GitHubiin. Tavoite: lista 50 kohteesta käyttäjämäärän
ja hylkäysiän mukaan.
