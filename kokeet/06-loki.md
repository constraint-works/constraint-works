# Koe 06: loki

Pohja ja koodit: `06-loki-pohja.md`, protokolla `06-kylma-paasytesti-protokolla.md` (lukittu
`ee116d4`). Ei nimiä, ei y-tunnuksia. Otos ja kehikko repon ulkopuolella.

## Tapahtumaloki

| pvm (UTC) | tapahtuma | € | omistajan min | lähde |
|---|---|---|---|---|
| 2026-09-16 | L0: kehikko rakennettu, 9 492 yritystä, SHA-256 `996a7c25…` | 0 | 0 | `06-kehikko-tiivistelma.json` |
| 2026-09-17 | GPT: tuhoamisyritys `2ab7a25` → READY AFTER CORRECTIONS; korjaukset `ee116d4` → APPROVED FOR LOCK | 0 | 0 | päätösloki |
| 2026-09-17T07:34Z | Protokolla, viestit, kynnykset, populaatio, paketti, budjettirajat ja mittarit lukittu versiona `ee116d4` | 0 | 0 | protokolla otsikko |
| 2026-09-17T07:34Z | **L1: otos arvottu.** `06-otos.py`, siemen 20260917, 150 riviä ilman takaisinpanoa, kehikon SHA-256 varmistettu committoitua vastaan ennen arvontaa (täsmää). Otoksen SHA-256 `ca5f23732937ac8232dd7c59b3eb9e180bdf5e809e918012e7d0e44f4c216245`. Rakenne: K06-001 - 060 aalto 1, 061 - 120 aalto 2, 121 - 150 vara. Nimiä ei katsottu ennen arvontaa; Claude ei ole katsonut nimiä arvonnan jälkeenkään (vain koneelliset tarkistukset) | 0 | 0 | `06-otos-tiivistelma.json` |
| 2026-09-17 | Poissulkukierros, mekaaninen osa: X-DUPL 0 (ei toistuvia y-tunnuksia eikä nimiä otoksessa; kehikossa 0 toistuvaa y-tunnusta). X-K04 0: koe 04:ssä ei sisääntulevia yhteydenottoja 2026-09-17 (0 issuea, 0 HN-kommenttia). X-K04 tarkistetaan uudelleen ennen D0:aa, koska koe 04 jatkuu 2026-09-30 asti | 0 | 0 | GitHub API, HN API |
| 2026-09-17 | Poissulkukierros, omistajan osa (X-TUTTU, X-ASIAKAS, X-KONSERNI): ODOTTAA. Tarkistustiedosto ja ohje yksityisessä hakemistossa repon ulkopuolella | 0 | | |
| 2026-09-17 | **Poissulkukierros valmis (omistaja).** Omistaja luki 150 nimeä: X-TUTTU 0, X-ASIAKAS 0, X-KONSERNI 0. Yhteensä kaikilla koodeilla 0/150 (X-DUPL 0, X-K04 0). Ei korvauksia varalta. Lopullinen rakenne: K06-001 - 060 aalto 1, 061 - 120 aalto 2, 121 - 150 vara (käyttämätön). Tarkistustiedostossa 0 merkintää (koneellinen tarkistus); lukitun otoksen SHA-256 ennallaan `ca5f2373…`. Omistajan aikaa ei mitattu (omistaja ilmoittaa minuutit, jos muistaa). X-K04 tarkistetaan vielä kerran ennen D0:aa | 0 | ei mitattu | omistajan ilmoitus |
| 2026-09-17 | Omistajan päätökset: P1 hyväksytty totuudenmukaisuuskorjauksena (ei nollasäilytyslupausta; pseudonymisointi; ei koulutuskäyttöä; säilytysaika D0:n todellisen palvelun mukaan); rahankäyttölupa ≤ 68 € (verkkotunnus, sähköposti, prepaid), katto 120 €; 5 000 €:n vastuukatto ei hyväksytty | 0 | | omistaja |
| 2026-09-17 | Rakennusvaihe (mallit, 0 €): toimialatarkistus OK; 10 brändiehdokasta tarkistettu; sivu-, tietosuoja-, sopimus- ja esimerkkiraporttipohjat + täyttöskripti + DNS-pohja + R7-välineet valmiina yksityisessä hakemistossa. AI-attribuutio (§11, mitattu): yksi malli-istunto saman päivän aikana; omistajan aikaa 0 min näihin vaiheisiin | 0 | 0 | `06-rakennusvaiheen-vaatimukset.md` §9 |

Otoksen jakaumat (`06-otos-tiivistelma.json`): toimialat 43: 32, 46: 38, 41: 13, 49: 14,
25: 16, muut teollisuus 29, muut kuljetus/varastointi 6, 42: 2; verobandit 10 - 50 k€: 94,
50 - 250 k€: 43, yli 250 k€: 13; ikä 5 - 9 v: 25, 10 - 19 v: 36, yli 20 v: 89; verkkosivu
YTJ:ssä 41,3 %. Vertailu kehikkoon (59,8 / 30,4 / 9,8 % verobandit; 13,6 / 29,7 / 56,7 %
ikä; 38,4 % www): otos vastaa kehikkoa satunnaisvaihtelun rajoissa (CALC, ei testattu).

## Yrityskohtainen taulukko

Avataan vasta poissulkukierroksen jälkeen (protokolla §6 kohta 5).
