# Koe 01: Superteamin agenttikaistan mittaus

**Mahdollisuus:** mahdollisuudet/agenttinatiivit-taloudet.md
**Alkaa:** 2026-09-16  **Päättyy:** 2026-09-16 (mittaus, ei vielä osallistuminen)
**Budjetti:** 0 €, noin 1 tunti ihmisen aikaa (rekisteröinti), tokenit Clauden sessiosta
**Onnistumisen ehto (kirjattu ennen mittausta):** saadaan kova luku AGENT_ONLY-listausten
määrästä, palkkioista ja kilpailusta. Ehto täyttyi.

## Mitä tehtiin

omistaja rekisteröi agentin "eikaisiina" Superteamin agenttirajapintaan. Avain on `.env`-
tiedostossa, gitin ulkopuolella. Claude ajoi `tyokalut/haku/superteam_agentti.py live`
ja haki kahden avoimen listauksen tiedot.

## Tulos

**Agenttikelpoisia listauksia koko historiassa: 11.** Kolme AGENT_ONLY, kahdeksan
AGENT_ALLOWED. Palkkiot yhteensä 37 600 USD, josta avoinna 11 000 USD.

| Listaus | Access | USD | Palautuksia | Deadline | Tila |
|---|---|---|---|---|---|
| Audit & fix open-source Solana repos | AGENT_ONLY | 3 000 | 116 | 2026-02-15 | voittajat julkaistu |
| Narrative detection & idea generation tool | AGENT_ONLY | 3 500 | 117 | 2026-02-15 | voittajat julkaistu |
| Open innovation track: build anything | AGENT_ONLY | 5 000 | 122 | 2026-02-15 | voittajat julkaistu |
| Superteam Academy (Brasil) | ALLOWED | 5 000 | 153 | 2026-03-05 | julkaistu |
| Imperial AI agent hackathon (UK) | ALLOWED | 5 000 | 65 | 2026-07-06 | julkaistu |
| Not your regular bounty (Jupiter) | ALLOWED | 3 000 | 258 | 2026-05-12 | julkaistu |
| Rebuild backend as Rust programs (Poland) | ALLOWED | 1 000 | 155 | 2026-03-16 | julkaistu |
| Polish ecosystem research content | ALLOWED | 600 | 192 | 2026-03-16 | julkaistu |
| Podcast cover design (Poland) | ALLOWED | 500 | 154 | 2026-03-16 | julkaistu |
| **Colosseum side track, Superteam Vietnam** | ALLOWED | 10 000 | 2 | 2026-10-13 | **avoin** |
| **Road to Colosseum: reflect & share** | ALLOWED | 1 000 | 6 | 2026-10-12 | **avoin** |

**AGENT_ONLY-markkina oli yksi lanseerauserä.** Kaikki kolme julkaistiin helmikuussa 2026
Colosseumin agenttihackathonin (100 000 USD, 2. - 12.2.2026) yhteydessä, ja kaikki
päättyivät 15.2.2026. Sen jälkeen ei yhtään uutta AGENT_ONLY-listausta seitsemään
kuukauteen.

**Kilpailu ei ollut vähäistä.** 116 - 122 agenttipalautusta per 3 000 - 5 000 USD.
Audit-bountyn voittajat: RECTOR (1 500), sterling-rhodes-agentti (1 000), Bob Security
Auditor -agentti (500). Kommenteissa OpenClaw-agentteja, jotka jatkoivat palautuksia
deadlinen jälkeenkin. Palkkio per palautus keskimäärin 26 USD.

**Kaksi avointa listausta eivät ole agenttityötä.** Vietnamin side track vaatii
GTM-suunnitelman, pitch deckin, founder-taustan ja Colosseum-hakemuksen: se on
startup-kilpailu, jossa agentti saa osallistua. Reflect & share vaatii työpajaan
osallistumisen ja X-postaukset: ihmisen läsnäoloa.

**Vahvistus kaistan 1 ideasta.** Ainoa tekninen AGENT_ONLY-tehtävä oli täsmälleen se,
mitä projektin ensimmäinen kortti ehdotti: agentti auditoi avoimen lähdekoodin repoja ja
tekee PR:n. Superteam kokeili sen 116 agentin voimin. Mekanismi on siis todellinen, ja
alusta piti sitä "kokeellisena".

## Vastaukset GPT:n kysymyksiin

1. AGENT_ONLY-mahdollisuuksia: 3 koskaan, 0 nyt. AGENT_ALLOWED: 8 koskaan, 2 nyt.
2. Palkkiot: 500 - 5 000 USD, kokonaisuudessaan 37 600 USD seitsemässä kuukaudessa.
3. Vähemmän kilpailua uutuuden takia: **ei.** 116 - 122 agenttia per tehtävä heti
   lanseerauksessa. Agenttien kynnys osallistua on nolla, joten kilpailu syntyy välittömästi.

## Opittua

- "Uusi = kilpailematon" ei päde agenttimarkkinoilla, koska agentin osallistumiskustannus
  on nolla. Se pätee vain markkinoilla, joissa osallistuminen maksaa ihmisen aikaa.
- Palkkio per palautus (26 USD) on hyvä nimittäjä. Se on samaa luokkaa kuin kohtuullinen
  tokenikustannus per laadukas submissio. Marginaali on ohut jo nyt.
- Agenttiprofiili kertyy silti: rekisteröinti on tehty, historia alkaa siitä. Sitä ei
  pureta.

## Päätös

Superteamin agenttikaista **ei ole ensimmäinen koe.** Ei avoimia agenttitehtäviä, ja
historiallinen kilpailu osoittaa, ettei etua ole. Seurataan skriptillä viikoittain:
jos uusi AGENT_ONLY-tekninen tehtävä ilmestyy, arvioidaan silloin.
