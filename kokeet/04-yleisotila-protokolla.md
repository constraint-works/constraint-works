# Koe 04: yleisötilan mittaus, lukittu protokolla (AUDIENCE / ACCESS)

Lukittu 2026-09-16 ennen julkaisua. Ei suoritettu. Korvaa `etsinta/SEURAAVA-HAVAINTO.md`
§5:n yhdistetyn PASS-ehdon omistajan ohjeen mukaisesti: koe mittaa kahta eri askelta
erikseen. Kynnyksiä ei muuteta tulosten jälkeen.

## Hypoteesit

- **H4a AUDIENCE:** projektin todennettujen lukujen julkaiseminen synnyttää mitattavaa
  ulkopuolista huomiota 14 päivässä.
- **H4b ACCESS:** huomio muuttuu oma-aloitteiseksi yhteydenotoksi tai muuksi pääsyksi,
  jota meillä ei ennen julkaisua ollut.

Baseline (FACT 2026-09-16): repo yksityinen, 14 pv näytöt 0, uniikit 0, kloonit 0,
tähdet 0, forkit 0, sisääntulevat yhteydenotot 0.

## Toimenpide (vaiheet ja kuka tekee)

1. Claude: salaisuustarkistus koko historiasta, raportti omistajalle. **Tehty, ks. §Salaisuustarkistus.**
2. omistaja: hyväksyy julkaisutekstin `etsinta/JULKAISU-1.md` sellaisenaan tai muokattuna.
   Muokattu versio committoidaan ennen julkaisua.
3. omistaja: muuttaa repon julkiseksi. Claude ei muuta näkyvyyttä.
4. omistaja: yksi postaus Hacker Newsiin (linkkipostaus repon `etsinta/JULKAISU-1.md`:hen
   tai README:hen; ei "Show HN"). Otsikko = tekstin otsikko. Postausaika kirjataan
   (UTC) tiedostoon `kokeet/04-loki.md`. Yksi postaus, ei uudelleenpostausta.
5. Claude: mittaa päivittäin 14 päivää `kokeet/04-mittaa.sh`:llä (GitHub traffic-
   rajapinta säilyttää 14 päivää; päivittäinen keruu estää katkokset). Tulokset
   `kokeet/04-traffic.jsonl`.
6. omistaja: välittää jokaisen sisääntulevan viestin (issue, sähköposti, HN-vastaus, muu)
   Claudelle luokiteltavaksi. Molemmat luokittelevat itsenäisesti (§ACCESS).

## AUDIENCE: mittari ja tulkinta (lukittu)

- **U** = `traffic/views.uniques` summattuna 14 päivältä postauksesta (päivittäinen
  keruu; päällekkäiset päivät deduplikoidaan päivämäärän mukaan).
- Toissijaiset, kirjataan mutta eivät ratkaise: HN-pisteet ja -kommentit, tähdet S,
  forkit, kloonien uniikit.
- **PASS:** U ≥ 500. **KILL:** U < 50. **UNKNOWN:** 50 ≤ U < 500.
- UNKNOWN sallii yhden toisen kanavan kerran. Se lukitaan nyt: Reddit r/opensource,
  sama teksti, sama otsikko. Toinen 14 päivän jakso mitataan erikseen; U2 tulkitaan
  samoilla rajoilla; sen jälkeen ei kolmatta kanavaa ilman uutta evidenssiä.

## ACCESS: määritelmä, mittari ja tulkinta (lukittu)

**Asiallinen yhteydenotto** on viesti, joka täyttää **kaikki** neljä ehtoa:

1. **Oma-aloitteinen ja osoitettu meille:** tulee ilman että me olemme pyytäneet sitä
   (teksti ei sisällä kehotusta ottaa yhteyttä), kanavana GitHub issue, discussion, PR,
   sähköposti omistajalle, HN-kommentti, joka on suunnattu kirjoittajalle, tai muu
   yksityisviesti. Julkinen kommentti yleisölle ei riitä, ellei se sisällä kohtaa 3.
2. **Tunnistettava henkilö tai organisaatio:** profiili, nimi tai osoite, johon voi vastata.
3. **Konkreettinen sisältö, vähintään yksi:**
   (a) tarjoaa dataa tai tapauksen, jota meillä ei ole (esim. "ylläpidän X:ää, tässä
   mitä tapahtui", pääsy aineistoon, lukuja toisesta ekosysteemistä);
   (b) korjaa jonkin tekstin FACT-luvun lähteellä;
   (c) pyytää protokollan ajamista omaan populaatioonsa tai ehdottaa yhteistä koetta
   nimetyllä seuraavalla askeleella;
   (d) tarjoaa maksullista tai maksutonta toimeksiantoa, jossa on nimetty seuraava askel
   (tapaaminen, aineisto, sopimusluonnos).
4. **Ei poissulkevaa luokkaa:** ei spämmi, ei meille suunnattu myynti, ei rekrytointi,
   ei pelkkä kysymys, johon repo jo vastaa, ei yleinen kehu tai kritiikki ilman kohtaa 3.

**Ei ole asiallinen yhteydenotto:** tähti, fork, watch, HN-upvote, kommentti tyyliin
"kiinnostavaa" tai "väärin", linkin jakaminen edelleen, kysymys ilman kohtaa 3, viesti,
jossa kohta 3 on ehdollinen ("jos joskus..."), tai viesti, jonka omistaja ja Claude
luokittelevat eri tavalla.

- **I** = niiden viestien määrä, jotka **molemmat** luokittelijat itsenäisesti merkitsevät
  asiallisiksi. Erimielisyydet kirjataan luokkaan "epäselvä" perusteluineen eivätkä laske.
- **PASS:** I ≥ 1. **KILL:** I = 0 ja epäselviä 0 14 päivän jälkeen (tai toisen kanavan
  jälkeen, jos AUDIENCE oli UNKNOWN). **UNKNOWN:** I = 0 ja epäselviä ≥ 1.
- Viestit, jotka tulevat 14 päivän jälkeen, kirjataan mutta eivät muuta tulosta.

## Yhdistetty päätösmatriisi (lukittu)

| AUDIENCE | ACCESS | Tulkinta | Päätös |
|---|---|---|---|
| PASS | PASS | Molemmat tilat syntyivät | Kokeet V (valtakirja) ja O (omistajat) suunnitellaan sisääntulevan kanavan varaan; toinen julkaisu aikaisintaan 30 pv päästä |
| PASS | KILL | Huomio ilman pääsyä | Yleisötila on olemassa mutta ei muutu pääsyksi tällä sisällöllä; ei uutta postausta; jatkokokeet luvallisella kylmällä yhteydenotolla; kirjataan, ettei "yleisö → pääsy" toteutunut |
| KILL | PASS | Pääsy ilman huomiota | Pääsy on todellinen (n ≥ 1) ja käsitellään sellaisenaan; yleisösilmukka kirjataan kuolleeksi tässä koossa |
| KILL | KILL | Kumpikaan ei syntynyt | Yleisösilmukka poistetaan projektin silmukoista; jokainen jatkokoe vaatii luvallisen kylmän yhteydenoton; ei uutta julkaisua ilman uutta evidenssiä |
| UNKNOWN | mikä tahansa | Toinen kanava kerran | Mittaus toistetaan r/opensource-postauksella; sen jälkeen tulkinta yllä olevilla riveillä |

## Salaisuustarkistus (tehty 2026-09-16, koko git-historia, FACT)

- `.env` ei ole koskaan ollut commitissa. `tyokalut/haku/data/` ei ole koskaan ollut commitissa.
- Avainkuvioita (`gho_`, `ghp_`, `sk-`, AWS, xoxb, PEM, Bearer, api_key=arvo) ei löydy
  yhdestäkään commitista. Ainoa osuma on Superteam-skriptin ohjeteksti "SUPERTEAM_AGENT_KEY=sk_...",
  joka on muotoesimerkki, ei avain.
- Superteam-agentin nimi "eikaisiina" mainitaan kokeessa 01. Agentin id, avain ja claim-koodi
  eivät ole repossa.
- **Julkistuessa paljastuu:** jokaisen 27 commitin tekijä "eikaisiina <(poistettu)>"
  (23 kpl) ja "original-private-account <(poistettu)>" (4 kpl). Sähköposti on git-metadataa, ei
  tiedostoissa. Sen poistaminen vaatisi historian uudelleenkirjoituksen, joka muuttaisi
  kaikki commit-SHA:t, joihin GPT:n ja Clauden tiedostot viittaavat. **Suositus: ei
  uudelleenkirjoitusta; omistaja päättää, kelpaako osoite julkiseksi.**
- Kolmansien osapuolten julkisia sähköposteja johdetuissa datatiedostoissa: WordPress-
  lisäosien tekijäkenttä (`(sähköposti poistettu)`, 3 riviä), yksi Chrome-laajennuksen
  tarjoajakenttä, yksi PyPI-metadatan maintainer-osoite kokeen 02 raportissa. Kaikki
  alkuperäisistä julkisista lähteistä. Ehdotus, jos omistaja haluaa: tekijäsarake poistetaan
  `wordpress-orvot-top10000.csv`:stä ja `cws-otos-390.json`:sta ennen julkistusta (yksi
  commit). Ei tehty ilman lupaa.
- GitHub-käyttäjänimiä 80 issuen luokittelussa: julkisia, alkuperäisten issueiden
  kirjoittajia. Ei henkilötietoja niiden lisäksi.
- AKR-data sisältää vain kieliparien lukumääriä, ei nimiä.
- Muistiot sisältävät omistajan etunimen, projektin tavoitteen (1 000 € → 10 M€) ja
  motiivit sekä GPT:n ja Clauden koko päättelyn. Nämä ovat julkaisun sisältö, eivät vuoto.
- Memory-tiedostot (`~/.claude/...`) eivät ole repossa.

## Kustannus

0 € tappiobudjetista. omistaja: enintään 1 h ennen julkaisua + 14 × 2 min. Claude: teksti,
päivittäinen mittaus, luokittelu.

## Mitä koe ei kerro

Kestääkö yleisö, muuttuuko pääsy rahaksi, toimiiko suomeksi, olisiko toinen otsikko tai
kanava tuottanut eri tuloksen. Yksi postaus on n = 1 kanavan sisällä.


## Lisäys 2026-09-16 (lähtöresurssisääntö; ei muuta mittareita eikä kynnyksiä)

Postaus tehdään tuoreelta, projektia varten luodulta Hacker News -tililtä, ei omistajan
olemassa olevilta tileiltä. UNKNOWN-tapauksen toinen kanava samoin tuoreelta Reddit-
tililtä. Tilin luo omistaja. Nollakarma on neutraali lähtötila; alustan mahdollinen
tuoreen tilin rajoitus kirjataan osana mittausta. Repo-linkki on projektin, ei henkilön.
Perustelu: `etsinta/LAHTORESURSSISAANTO.md` §5 ja §10.
