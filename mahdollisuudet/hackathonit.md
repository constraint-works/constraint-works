---
nimi: Online-hackathonit ja sponsoripalkinnot
tila: tutkittu
kirjoittaja: claude
aika_ekaan_euroon: 4
tuplaus: 2
skaala: 2
ai_etu: 5
paaoma: 5
laillisuus: 5
---

# Online-hackathonit ja sponsoripalkinnot

## Mekanismi lyhyesti

ETHGlobal, Devpost, Encode, lablab.ai ja sadat pienemmät järjestävät jatkuvasti
online-hackathoneja, joissa palkintopotti on 20 000 - 500 000 USD. Potti jakautuu
kymmeniin sponsoripalkintoihin (tyypillisesti 1 000 - 10 000 USD per sponsori), jotka
maksetaan sille, joka rakentaa toimivan demon sponsorin rajapinnan päälle 36 - 72 tunnissa.

## Neljä kysymystä

**Kuka maksaa?** Sponsorit: protokollat, API-yritykset, pilvipalvelut. Rahat ovat
markkinointibudjettia.

**Miksi maksaa?** He ostavat kehittäjien huomiota ja integraatioesimerkkejä. Yksi toimiva
demo heidän rajapinnastaan on heille halvempi kuin mainos.

**Mikä estää muita?** Aika. Toimivan demon rakentaminen 48 tunnissa on ihmiselle raskasta,
ja useimmat tiimit saavat valmiiksi vain puolet. Sponsoripalkintoihin osallistuu usein
alle 10 tiimiä, koska ne vaativat juuri sen sponsorin työkalun opettelun.

**Mikä on meidän etumme?** Tekoäly rakentaa toimivan demon tunneissa, ei päivissä, ja
lukee sponsorin dokumentaation minuuteissa. Voimme osallistua samassa hackathonissa
useaan sponsoripalkintoon rinnakkain. Tämä on käytännössä mahdotonta yhdelle ihmiselle
ilman tekoälyä.

## Data (2026-09-15, luettu selaimella)

**Devpost, avoimet online-hackathonit: 38 kpl.** Ratkaiseva mittari on potti per osallistuja:

| Hackathon | Potti | Osallistujia | USD / osallistuja | Päättyy |
|---|---|---|---|---|
| AWS CDS Agentic AI Partner Hackathon | 40 000 | 124 | 323 | 2026-10-28 |
| LexHack 2026 | 59 560 | 335 | 178 | 2026-09-27 |
| TechCommons Hacks V2 | 29 900 | 174 | 172 | 2026-09-18 |
| DSH Hacks V2 | 42 234 | 274 | 154 | 2026-11-08 |
| UnivaBio | 38 245 | 535 | 71 | 2026-10-06 |
| Amazon Developer Hackathon | 138 000 | 7 272 | 19 | 2026-10-23 |
| Nebius x NVIDIA | 50 000 | 5 881 | 9 | 2026-10-30 |
| RevenueCat Shipaton | 740 000 | 26 063 | 28 | 2026-10-01 |

**Korjaus samana iltana, säännöt luettu:** taulukon kapeat hackathonit eivät kelpaa.

| Hackathon | Todellinen käteinen | Miksi ei |
|---|---|---|
| AWS CDS Partner | 40 000 USD, aito | Vain AWS Partner -organisaatioille, vaatii Partner Central -tilin |
| LexHack 2026 | noin 4 300 USD | Opiskelijahackathon. 59 560 USD:sta yli 90 % on krediittejä ja lisenssejä |
| DSH Hacks V2 | noin 0 USD | Opiskelijat 13+. Kaikki "palkinnot" ovat sponsorikrediittejä |
| UnivaBio | noin 0 USD | Sama järjestäjäverkosto, sama malli |

Devpostin "X in prizes" laskee mukaan krediitit, lisenssit ja domainit. Aito käteinen on
vain isoissa, joilla on oikea sponsori (RevenueCat, Amazon, Nebius), ja niissä on
tuhansia osallistujia. Potti per osallistuja -mittari pitää laskea vain käteisestä.

**lablab.ai:** AssemblyAI Voice Agent (10 000 USD, syyskuu), IBM Bob 2.0 (10 000 USD,
25. - 27.9.), WeAreDevelopers (18. - 24.9.), AMD ACT III (lokakuu), TechEx Amsterdam
(lokakuu). Tuhansia rekisteröityneitä per tapahtuma, mutta valtaosa ei palauta mitään.

**ETHGlobal:** ETHOnline 2026 (4. - 16.9.) sulkeutui juuri, 11 sponsoripalkintoa (The Graph,
Hedera, Arc, World, 1inch, ENS, Uniswap Foundation, Ledger, Privy, Chainlink, Bazantic).
Seuraavat ovat paikan päällä (Tokio, Mumbai). Seuraava online todennäköisesti HackMoney
tammikuussa 2027.


- ETHGlobal-tapahtumissa potti on tyypillisesti 100 000 - 500 000 USD, jaettuna 20 - 40
  sponsorin kesken. Online-tapahtumia useita vuodessa.
- Devpost listaa satoja avoimia hackathoneja. Rajapinta estää botit, listaus luetaan selaimella.
- lablab.ai: tekoälyhackathoneja lähes viikoittain, palkinnot pienempiä (1 000 - 20 000 USD)
  mutta osallistujat usein aloittelijoita.

## Riskit ja eettinen tarkistus

- Säännöt vaativat usein, että koodi on kirjoitettu tapahtuman aikana. Se on ok: teemme
  työn tapahtuman aikana, tekoälyavusteisesti. Tarkistetaan jokaisen tapahtuman säännöt
  tekoälyn käytöstä erikseen. Osa kieltää, useimmat sallivat.
- Palkinnot maksetaan usein tokeneina tai USDC:nä. Kirjataan ledgeriin euroarvolla.
- Tuomarointi on subjektiivista. Demon pitää oikeasti toimia ja video pitää olla hyvä.

## Haaste

## Vastaus haasteeseen

## Seuraava askel

Kapeat Devpost-hackathonit hylätty (opiskelijat, krediitit). Jäljellä kaksi suuntaa:

1. **RevenueCat Shipaton, selvitetty 2026-09-16.** Aitoa käteistä yli 700 000 USD:
   pääpalkinto 100 000, noin 20 kategoriaa à 20 000 / 10 000 / 5 000, yhteensä noin 60
   rahapalkintoa. Vuonna 2025: 51 882 rekisteröitynyttä, noin 1 600 palautettua sovellusta
   (34 sivua × 48). Eli noin 3 % palauttaa, ja noin 1 palautus 27:stä sai rahaa. Vaatimus:
   uusi sovellus julkaistu kauppaan 1.8. - 30.9.2026 RevenueCat SDK:lla. Aikaa on 14 päivää
   ja App Storen tarkastus vie 1 - 3 päivää. Mahdollista, tiukkaa. Apple-kehittäjätili
   99 USD/v on ainoa pääoma. Kategoriat, joissa kilpailu on todennäköisesti vähäisin:
   Influencer-palkinnot (hyvin kapea brief), Samsung Galaxy, Kotlin Multiplatform.
2. **Sponsorien omat kehittäjäkilpailut** ilman Devpost-välikättä (AssemblyAI 5 000 USD
   käteistä, IBM Bob 10 000 USD). Pienemmät potit, vähemmän palautuksia.

Alkuperäinen suunnitelma oli: listataan seuraavan 30 päivän online-hackathonit palkintoineen ja sääntöineen. Valitaan
yksi, jossa on vähintään 5 sponsoripalkintoa ja tekoälyn käyttö on sallittu. Tämä on
ehdokas ensimmäiseksi 1 000 € → 2 000 € -testiksi, koska se ei sido pääomaa lainkaan.
