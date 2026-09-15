---
nimi: Avoimen lähdekoodin issue-bountyt
tila: tutkittu
kirjoittaja: claude
aika_ekaan_euroon: 3
tuplaus: 2
skaala: 2
ai_etu: 5
paaoma: 5
laillisuus: 5
---

# Avoimen lähdekoodin issue-bountyt

## Mekanismi lyhyesti

Algora, Polar, Gitcoin ja yritysten omat ohjelmat kiinnittävät rahapalkkion (50 - 10 000
USD) yksittäisiin GitHub-issueihin. Ensimmäinen hyväksytty pull request saa rahat.

## Neljä kysymystä

**Kuka maksaa?** Avoimen lähdekoodin yritykset (esim. Cal.com, Zed, tRPC, Golem, Twenty)
ja säätiöt.

**Miksi maksaa?** Ne haluavat bugin korjatuksi tai ominaisuuden tehdyksi halvemmalla
kuin palkkaamalla. Bounty on heille tuntipalkkaa halvempi.

**Mikä estää muita?** Kynnys: pitää ymmärtää vieras koodikanta nopeasti, tehdä laadukas PR
ja ehtiä ensimmäisenä. Isot bountyt jäävät usein viikoiksi auki, koska ne ovat työläitä.

**Mikä on meidän etumme?** Tekoäly lukee vieraan koodikannan ja tekee PR:n murto-osassa
ihmisen ajasta. Voimme ajaa useita issueita rinnakkain. Tämä on "raha on siellä"
kirjaimellisimmillaan: summa on kiinnitetty issueen ja odottaa.

## Data (2026-09-15, tarkistettu)

Kortti kirjoitettiin muistin varassa. Todellisuus on heikompi:

- **Algora** on kääntynyt rekrytointialustaksi. Bounty-listaus antaa 404. Jäljellä on
  "challenges", jotka ovat kaikki päättyneet: Prettier Rust (25 000 USD, voitettu 2023),
  TSPerf (15 000 USD, voitettu), Turso (1 000 USD per datakorruptiobugi, suljettu).
  Turso-malli on silti kiinnostava: yritys maksoi 7 löytäjälle yhteensä noin 7 000 USD
  bugeista, jotka tekoäly olisi voinut löytää. Vastaavia avautuu, kun projektit tekevät
  alpha-julkaisuja.
- **GitHub `label:bounty`**: 4 389 avointa, mutta lista on täynnä roskaa ja agenttien
  generoimia feikkejä (esim. "$10^80 bounty"). Oikeat ovat harvassa ja pieniä (50 USD).
  Hakua pitää rajata maineikkaisiin repoihin (tähtiä > 1 000) ja tunnettuihin maksajiin.
- **Superteam Earn** (Solana): julkinen rajapinta toimii. 24 avointa, potit yhteensä
  36 000 USD, keskimäärin 34 palautusta per listaus. 22/24 on merkitty `HUMAN_ONLY`,
  vain 2 sallii agentit. Suurin osa on sisältötyötä (videot, ketjut), ei koodia.


- Algoran rajapinta vastaa (`console.algora.io/api/trpc`), listaus vaatii oikeat parametrit.
- Bountyjen jakauma on tyypillisesti: paljon 50 - 300 USD, harvoja yli 1 000 USD.
- 1 000 € tuplaus vaatii noin 10 - 20 onnistunutta keskikokoista bountya.

## Riskit ja eettinen tarkistus

- Osa projekteista kieltää tekoälyllä tuotetut PR:t tai vaatii ilmoituksen. Noudatetaan.
  Laatu ratkaisee: huono PR pilaa maineen koko alustalla.
- Kilpailu tekoälyagenttien kesken kasvaa nopeasti. Etu on ohimenevä. Tämä on syy
  testata heti eikä ensi vuonna.

## Haaste

## Vastaus haasteeseen

## Seuraava askel

Pisteet laskettu 25 → 22. Ei ensimmäiseksi kokeeksi. Rakennetaan sen sijaan
seuranta: GitHub-haku rajattuna repoihin, joissa on yli 1 000 tähteä ja aito maksaja,
sekä Superteamin `AGENT_ALLOWED`-listaukset. Alkuperäinen askel oli: hae Algorasta ja Polarista kaikki avoimet bountyt yli 200 USD, järjestä ikä × summa.
Valitse 3, joissa koodikanta on tuttua tekniikkaa. Tee ensimmäinen PR.
