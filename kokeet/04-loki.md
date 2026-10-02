# Koe 04: loki

| Aika (UTC) | Tapahtuma | Lähde |
|---|---|---|
| 2026-09-16T19:45Z | Repo `constraint-works/constraint-works` muutettu julkiseksi (omistaja). Kuvaus tyhjä. | GitHub API: private=false |
| 2026-09-16T19:43Z | HN-tili `constraintworks` luotu (omistaja). Karma 1, ei postauksia, ei kommentteja. | HN API user/constraintworks |
| 2026-09-16T19:45Z | Baseline-liikenne mitattu ennen postausta: ks. `04-traffic.jsonl` ensimmäinen rivi (odotus: 0). | `04-mittaa.sh` |

Postaus (T), item-id, 48 h altistusseuranta ja T + 14 vrk -mittaus kirjataan tähän.
| 2026-09-16T19:47:19Z | **Postaus T.** HN item 49731952, tili `constraintworks`, otsikko "What we measured about \"abandoned\" software before trying to make money from it", linkki JULKAISU-1.md. | HN API item/49731952 |
| 2026-09-16T19:51Z | 48 h altistusseuranta käynnistetty (15 min välein, `04-hn-seuranta.jsonl`) ja päivittäinen liikennemittaus 15 vrk (`04-traffic.jsonl`). Irralliset prosessit tällä koneella; vaativat koneen olevan päällä. U haetaan erikseen T + 14 vrk. | `04-hn-seuranta.py`, `04-paivittain.sh` |
| 2026-09-18T18:12Z | **48 h altistusseuranta päättyi.** 44 mittausta suunnitellusta noin 192:sta (kone nukkui välillä; pisin aukko noin 9 h, 17.9. 21:39Z - 18.9. 06:37Z). Jokaisessa mittauksessa pisteet 1, kommentit 0, ei dead/deleted, ei top 30:ssä. **E = 0** (FACT mitatuilta hetkiltä; aukkojen ajalta UNKNOWN). | `04-hn-seuranta.jsonl` |
| 2026-10-01T11:00Z | **Poikkeama: T + 14 vrk -haku (2026-09-30T19:47Z ± 6 h) jäi tekemättä** (kone ei ollut päällä). Lähin onnistunut haku on tämä, T + 14,63 vrk (15,2 h myöhässä, alle 15 vrk): ylätason `uniques` 24, U_hn 5. Ikkuna oli siirtynyt (17. - 30.9.), joten postauspäivä 16.9. (40 päiväuniikkia) on pudonnut pois. | `04-traffic.jsonl` |
| 2026-10-02T08:16Z | Lopputarkistus (taustatieto, ei U): HN item 49731952 pisteet 1, kommentit 0; tilin karma 1. Repo: issuet 0, PR:t 0, discussions 0 (ei käytössä), tähdet 0, forkit 0, watchers 0. Päivittäinen mittaussilmukka pysäytetty (ikkuna ohi). | HN API, GitHub API |
| 2026-10-02T09:45Z | **Projektisähköpostin tarkistus (omistajan kirjautuneessa selaimessa):** kaikki viestit 16.9. - 2.10.: vain GitHubin ja sähköpostipalvelun automaattiviestejä; roskaposti tyhjä. Yhteydenottoja 0. **ACCESS = EI HAVAITTU on lopullinen** (I = 0, epäselviä 0). | postilaatikko |
| 2026-10-02T10:00Z | **Second-chance-pyyntö lähetetty** (omistaja, projektisähköpostista osoitteeseen hn@ycombinator.com; yksi lause ja linkki, lukitun matriisin IOE / EI HAVAITTU -rivin mukaan, kerran). Lähetysaika on omistajan ilmoitus, noin ± 10 min. Jos postaus nostetaan, siitä alkaa uusi 48 h D-mittaus; seurannan toteutus odottaa omistajan hyväksyntää. | omistajan ilmoitus |

## Tulos (kirjattu 2026-10-02)

**AUDIENCE = IOE** (riittämätön havaittu altistus). **ACCESS = EI HAVAITTU** (sähköpostikanava
tarkistettu 2026-10-02: 0 yhteydenottoa).

- **U (protokollan poikkeamasäännön mukaan) = 24**, U_hn = 5 (FACT, haku 2026-10-01T11:00Z).
  Luku aliarvioi postauksen jälkeisen jakson, koska ikkuna ei enää kata postauspäivää.
- Parempi arvio jakson uniikeista: **63 - 66**. Alaraja 63 = ylätason `uniques` hauissa
  22., 24. ja 29.9. (FACT; ikkuna 10. - 23.9., U_hn 30). Yläraja 66 = päiväuniikkien
  summa 16. - 30.9. (CALCULATION: 40 + 17 + 5 + 0 + 1 + 1 + 1 + 0 + 0 + 1 + 0 × 5).
  Haku 29.9. palautti saman 10. - 23.9. -ikkunan kuin 24.9.; syy UNKNOWN.
- Tulkinta ei riipu siitä, kumpaa lukua käytetään: E = 0 ≤ 3 ja U < 500 → IOE.
- E:n mittaus kattoi 44 / noin 192 hetkeä. INFERENCE: etusivukäynti aukkojen aikana on
  epätodennäköinen, koska pisteet pysyivät 1:ssä koko ajan ja ovat 1 yhä 2.10.
- Kloonien uniikit (100) ylittävät katselujen uniikit (63) (FACT). INFERENCE: suuri osa
  klooneista on automaattisia; niitä ei tulkita kiinnostukseksi.
- ACCESS: I = 0, epäselviä 0 julkisissa kanavissa (FACT 2026-10-02). Sähköpostikanava:
  tarkistettu 2026-10-02, 0 yhteydenottoa (FACT).

**Mitä ei voida päätellä:** mitään sisällön kiinnostavuudesta. Postaus ei saanut
mitattavaa altistusta, joten tulos on kanavatulos (tuore tili, ei jakelua).

**Lukitun matriisin mukainen jatko (IOE / EI HAVAITTU):** second-chance pool kerran
(omistajan viesti hn@ycombinator.com), sitten toinen kanava kerran; jos yhä IOE →
AUDIENCE UNKNOWN. Kumpikin vaatii omistajan toimen, joten päätös on omistajalla.
