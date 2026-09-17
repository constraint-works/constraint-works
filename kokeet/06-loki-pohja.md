# Koe 06: lokipohja (täytetään vasta käynnistyksen jälkeen; ei nimiä, ei y-tunnuksia)

Koodit: `06-kylma-paasytesti-protokolla.md` §8. Raakatekstit (vastaukset,
puhelumuistiinpanot) säilytetään repon ulkopuolella nimettöminä; tänne vain koodit,
päivät ja sanatarkat kieltäytymissyyt ilman tunnistetietoja.

## Tapahtumaloki

| pvm (UTC) | tapahtuma | € | omistajan min | lähde |
|---|---|---|---|---|
| | L1: otos arvottu, siemen, SHA-256 | 0 | | `06-otos-tiivistelma.json` |
| | Poissulkukierros: X-TUTTU n, X-ASIAKAS n, X-KONSERNI n, X-K04 n, X-DUPL n; korvattu varalta n | 0 | | |
| | R1 - R7 valmiit; R7-toimitettavuustesti: Gmail / Outlook / kotimainen → inbox/roskaposti | | | |
| | S1: aallon 1 ensimmäinen viesti | | | |

## Yrityskohtainen taulukko

| Tunniste | Aalto | Kanava (yleisosoite / lomake / vain puhelin / C0) | Yhteystiedon haku min | A1 pvm | C1-B bounce | A2 pvm | A3 pvm, yritykset | "Saitteko viestin" | C4 tavoitettu | Vastausluokka (R-NO/R-INT/R-CONTRACT/R-DATA/PASS) | R-NO-luokka | Kieltäytymissyy sanatarkasti | VAIHE | Piilopääoma Q1 / Q2 / Q3 | Spontaanit signaalit; kolmas osapuoli | Piilopääomaluokka (ei kontaminoi / potentiaalisesti avusteinen / epäselvä) | Ostovolyymi suuruusluokka (vain R-DATA/PASS) | Omistajan min | Claude-luokitus | Epäselvä? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K06-001 | 1 | | | | | | | | | | | | | | | | | | | |

## Kanavadiagnoosi D21 (aalto 1)

N_s = , N_ct = , N_c = , N_r = , N_r/N_c = , C0 = , C1-B = , C3 = . Päätös: aalto 2 käynnistyy (N_r/N_c ≥ 40 %) / CHANNEL UNKNOWN.

## Nimittäjäketju (lopussa; jokainen luku erikseen, suhdeluvut nimittäjineen)

| Taso | Aalto 1 | Aalto 2 | Yhteensä |
|---|---|---|---|
| N_s otos (poissulut korvattu) | | | |
| N_ct tavoitettavissa (kanava löytyi) | | | |
| N_c kontaktoitu | | | |
| N_r tavoitettu (C4) | | | |
| N_i kiinnostunut (R-INT) | | | |
| N_k sopimus (R-CONTRACT) | | | |
| N_d aineisto (R-DATA) | | | |
| N_p PASS | | | |
| N_r/N_c, N_i/N_r, N_p/N_r | | | |

## Kokonaismittarit (lopussa)

| Mittari | Aalto 1 | Aalto 2 | Yhteensä |
|---|---|---|---|
| Vastaus mihin tahansa / N_c | | | |
| PASS / potentiaalisesti piilopääoma-avusteinen / epäselvä | | | |
| Kieltäytymissyyt tavoitetuista (N_r nimittäjä): LUOTTAMUS / HYÖTY / VAIVA / ON-JO / POLITIIKKA / KIELTO / MUU | | | |
| Omistajan tunnit: rakennus / haku / lähetys / puhelut / tapaamiset / sopimus | | | |
| Eurot | | | |
| Piilopääomasignaalit (kpl) | | | |
| "Tekoäly"/"roskaposti"-maininnat (kpl) | | | |

## Tulos

ACCESS PASS / ACCESS FAIL (pakettikohtainen, nimittäjä N_r ≥ 60) / CHANNEL UNKNOWN / ACCESS UNKNOWN / INCOMPLETE.
Perustelu §9:n ehdoilla. Reitti (miten tuntematon olisi saanut saman). AI-attribuutio §11:n mukaan: mitattu AI-avusteinen aika ja kustannus per työvaihe, vastaajien maininnat tekoälystä. Ei vastafaktuaaliväitteitä ilman INFERENCE-merkintää.
