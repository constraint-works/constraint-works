---
nimi: Agenttinatiivit taloudet (raha, joka on tarkoitettu agenteille)
tila: tutkittu (mitattu)
kirjoittaja: claude (GPT:n haasteen pohjalta)
kierros: 2
aika_ekaan_euroon: 2
tuplaus: 1
skaala: 2
ai_etu: 5
paaoma: 4
laillisuus: 4
---

# Agenttinatiivit taloudet

## Mekanismi lyhyesti

Kokonainen kategoria, jossa maksaja on nimenomaan päättänyt maksaa autonomisille tai
puoliautonomisille agenteille. Ihminen on lunastaja, ei tekijä. Tämä on uusi (2025 - 2026)
ja siksi vähemmän kilpailtu kuin ihmisille tarkoitetut potit.

## Neljä kysymystä

**Kuka maksaa?** Alustat ja protokollat, jotka rakentavat agenttitaloutta: Superteam Earn
(Solana-säätiön ekosysteemi), Recall Network, Bittensor-subnetit, Olas, x402-palveluita
ostavat agentit.

**Miksi maksaa?** He tarvitsevat agentteja todistaakseen, että heidän alustansa toimii.
Varhainen agenttiaktiivisuus on heille markkinointia ja verkostovaikutusta. Raha on
tarkoituksella pöydällä, jotta agentit tulisivat.

**Mikä estää muita?** Toistaiseksi vain se, että harva tietää. AGENT_ONLY-listaukset on
piilotettu ihmisfeedistä. Rajapinnat ovat uusia (Superteam v0.2.0), dokumentaatio on
ohutta ja ihmisen pitää silti lunastaa palkkio.

**Mikä on meidän etumme?** Tämä on ainoa kategoria, jossa "tekoäly tekee työn" ei ole
etu vaan pääsyvaatimus. Kilpailijat ovat muita agentteja, eivät ihmisiä.

## Data (2026-09-16)

**Superteam Earn, virallinen agenttirajapinta.** Vahvistettu `earn.superteam.fun/agents`
ja `/skill.md`. Agentti rekisteröityy nimellä, saa API-avaimen ja claim-koodin, hakee
`/api/agents/listings/live`, tekee submissionin, ihminen lunastaa palkkion claim-koodilla.
Julkinen feed näyttää vain HUMAN_ONLY ja AGENT_ALLOWED (22 + 2). AGENT_ONLY-listaukset
näkyvät vain avaimella. **Mitattu 2026-09-16, ks. kokeet/01:** 11 agenttikelpoista listausta koko historiassa,
3 AGENT_ONLY (kaikki helmikuun 2026 lanseerauserää, 116 - 122 palautusta kullakin),
0 avointa agenttitehtävää nyt. Palkkio per palautus 26 USD. Pisteet 21 → 18.

**Recall Network.** Agenttikilpailuja (paper trading, spot, perp). Palkkiot RECALL-tokenina,
1. sija 50 % potista, sitten puolittuu. Pottien koko ja osallistujamäärä eivät selvinneet
dokumentaatiosta.

**Bittensor.** Yli 100 subnetiä, joissa minerit saavat TAO:ta validaattorien pisteytyksen
mukaan. Julkiset arviot 100 - 500 USD/kk per aktiivinen miner. Vaatii GPU:n ja subnetin
rekisteröintimaksun TAO:ssa. Pääomaa sitova, ei nollasta.

**Olas Pearl.** Ajat agenttia läppärillä, staketaat OLAS:ia, saat OLAS-palkkioita
aktiivisuudesta. Konkreettisia lukuja ei julkaista. Vaatii stake-pääoman.

**x402.** HTTP 402 -maksuprotokolla, Linux Foundationin alla huhtikuusta 2026. Yli 100 M
USD neljännesvuosivolyymi Q1/2026, 90 % Basella. AWS AgentCore Payments toukokuusta 2026.
Tämä on toinen suunta: agentit ovat *ostajia*. Ks. kortti `x402-palvelut.md`.

## Riskit ja eettinen tarkistus

- Palkkiot ovat tokeneita (USDC, RECALL, TAO, OLAS). Verotus: pääomatuloa tai ansiotuloa
  lunastushetken euroarvolla. Kirjataan ledgeriin.
- Recall ja Bittensor edellyttävät tokenin ostamista osallistuakseen. Se on pääomaa
  riskissä. Superteam ei vaadi.
- Agentin pitää olla aidosti oma. Ei ohjeiden vastaista automaatiota, ei toisten töiden
  kopiointia (Superteamin code of conduct kieltää muiden submissionien katsomisen).

## Red team (claude, 2026-09-16, ks. etsinta/AGENTTITALOUS.md)

Pisteet laskettu 23 → 21. Syyt: x402:n todellinen volyymi on noin 1 % ilmoitetusta,
ERC-8004-ekosysteemi on empiirisen tutkimuksen mukaan ontto, ja Superteamin agenttikaista
on pieni ja tuettu. Kategoria on todellinen mutta tänään pieni. Se, mikä siinä on
arvokasta, on aikaisuus: maine ja historia kertyvät nyt niille, jotka ovat paikalla.

## Haaste

## Vastaus haasteeseen

## Seuraava askel

1. omistaja rekisteröi agentin (yksi curl, ks. skriptin docstring), tallettaa avaimen `.env`.
2. Ajetaan `superteam_agentti.py live`. Ensimmäinen kova luku: kuinka monta AGENT_ONLY-
   listausta, palkkiot, submissioiden määrä.
3. Jos yksikin sopiva löytyy, se on ehdokas ensimmäiseksi kokeeksi: nollapääoma, tekoäly
   tekee, ihminen lunastaa. Vastaa suoraan kokeen ydinkysymykseen.
