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

## Lisäys 2 (2026-09-16): jakeluportti ennen AUDIENCE-tulkintaa

**Tarkistetut faktat (HN:n oma FAQ ja dokumentoidut käytännöt):**
- FACT: "Do posts by users with more karma rank higher? No." Sijoitus = pisteet jaettuna
  ajan potenssilla; lisäksi liput, väärinkäytösohjelmisto, sivustopainotus ja
  moderointi. Alle 2 viikon tili näkyy vihreänä. Postaus voi kuolla ohjelmallisesti,
  lippujen tai moderaattorin toimesta ([dead], [flagged]).
- FACT: HN:llä on "second-chance pool": moderaattorit voivat nostaa huomiotta jääneen
  postauksen etusivun alaosaan; HN:n mukaan omankin artikkelin saa ehdottaa
  osoitteeseen hn@ycombinator.com.
- Toissijainen: noin 300 - 400 postausta päivässä, etusivulla 30; noin 90 % ei koskaan
  pääse etusivulle; etusivu tuo 10 000 - 30 000 kävijää vuorokaudessa. Etusivulle
  pääsemättömän postauksen kävijämäärää ei ole dokumentoitu; se on pieni ja tulee
  /newest-sivulta. Käyttäjien raportoima virhe "your account is too new to submit this
  site" on olemassa, mutta sen ehdot ovat UNKNOWN.

**Johtopäätös:** ilman jakeluporttia U < 50 mittaisi todennäköisimmin sitä, ettei postaus
saanut jakelua, ei sitä, ettei sisältö kiinnosta. Siksi AUDIENCE tulkitaan kahdessa
vaiheessa. ACCESS-määritelmä ja -kynnykset eivät muutu. U:n kynnykset 500 / 50 eivät
muutu; ne sovelletaan vain jakeluportin läpäisseeseen postaukseen.

**Vaihe D, jakelu (lukittu):** postaus on saanut jakelua, jos 48 tunnin sisällä
täyttyy vähintään yksi: (a) pisteitä ≥ 5, (b) postaus on ollut HN:n topstories-listan
30 ensimmäisen joukossa vähintään yhdellä 15 minuutin välein tehdyllä mittauksella,
(c) kommentteja ≥ 3 muilta kuin postaajalta. Jakelu on epäonnistunut, jos postaus on
[dead] tai [flagged] 2 tunnin kuluessa tai mikään ehdoista (a) - (c) ei täyty 48
tunnissa. Mittaus: `kokeet/04-hn-seuranta.py` (HN:n julkinen Firebase-rajapinta, ei
tiliä, 15 min välein 48 h, tulos `kokeet/04-hn-seuranta.jsonl`).

**Tulkinta:**
- D läpäisty → AUDIENCE tulkitaan alkuperäisillä rajoilla (U ≥ 500 PASS, U < 50 KILL,
  välissä UNKNOWN).
- D epäonnistui → AUDIENCE = **NO DISTRIBUTION** (kanavatulos, ei sisältötulos).
  Sallitut jatkot järjestyksessä, kumpikin kerran: (1) toisen mahdollisuuden pooli:
  omistaja lähettää HN:n ohjeen mukaisen lyhyen viestin osoitteeseen hn@ycombinator.com
  (sallittu HN:n oman FAQ:n mukaan; ei markkinointia, vain linkki ja yksi lause);
  jos moderaattorit nostavat postauksen, D arvioidaan uudelleen 48 h; (2) toinen
  kanava (r/opensource, tuore tili) kuten alkuperäisessä UNKNOWN-haarassa. Jos
  molemmat päättyvät NO DISTRIBUTIONiin, AUDIENCE = UNKNOWN (kanavat eivät antaneet
  jakelua), ei KILL, ja se kirjataan tuoreen identiteetin jakelurajoitteena.
- ACCESS mitataan koko 14 päivän ajan riippumatta D:stä. Pääsy ilman jakelua on
  sallittu tulos (matriisin rivi KILL/PASS pätee muodossa NO DISTRIBUTION / PASS).

**Tilin luonti:** omistaja luo projektin HN-tilin ennen postausta. Tilillä ei tehdä
kommentteja tai äänestyksiä maineen keräämiseksi; nollahistoria on lähtötila. Jos
postaus estyy virheeseen "account is too new to submit this site", virhe kirjataan,
odotetaan 14 päivää ja yritetään kerran uudelleen; sen jälkeen siirrytään toiseen
kanavaan. Postaustyyppi: tavallinen linkki repon julkiseen tiivistelmään, otsikko =
tiivistelmän otsikko, ei "Show HN".

**Mitä tämä ei poista:** ajoitus ja /newest-sivun satunnaisuus vaikuttavat D:hen
edelleen. Yksi postaus on n = 1. Siksi NO DISTRIBUTION ei koskaan tulkita KILLiksi.

## Lisäys 3 (2026-09-16): pre-flight-korjaukset. Tämä lisäys korvaa lisäyksen 2 D-portin ja alkuperäisen U-määritelmän ja päätösmatriisin.

### U:n määritelmä

FACT (GitHub REST, `GET /repos/{owner}/{repo}/traffic/views`): vastaus sisältää
14 viimeisen päivän `count` ja `uniques` sekä `views`-taulukon päiväkohtaisine
`count`/`uniques`-arvoineen; `per=week` antaa viikkoerittelyn. Dokumentaatio ei määrittele,
miten GitHub tunnistaa uniikin kävijän. Tarkistettu tästä reposta: 14 päivän rivit,
ylätason `uniques` erikseen. `GET .../traffic/popular/referrers` palauttaa 10 suurinta
viittaajaa 14 päivältä kenttineen `referrer`, `count`, `uniques`.

Päiväkohtaisten `uniques`-arvojen summa ei ole 14 päivän uniikkien määrä, koska sama
kävijä voi esiintyä usean päivän luvussa. Siksi:

- **U = ylätason `uniques`, haettuna kerran ajanhetkellä T + 14 vrk (± 6 h), missä T on
  postauksen ajankohta.** Rajapinnan 14 päivän ikkuna kattaa silloin täsmälleen
  postauksen jälkeisen jakson. Baseline ennen T:tä on mitattu: 0. U on GitHubin
  määrittelemä 14 päivän uniikkien kävijöiden määrä repon kaikilla sivuilla, ei
  "uniikkeja lukijoita" eikä "eri ihmisiä" muussa merkityksessä kuin GitHubin.
- **U_hn** (täydentävä, ei päätösmittari) = `referrers`-erittelyn `uniques` viittaajalle
  `news.ycombinator.com` samalla hakuhetkellä. Kertoo, kuinka suuri osa U:sta tuli
  kanavasta. Referrer voi puuttua selainasetusten takia, joten U_hn on alaraja.
- Päivittäiset otokset (`04-mittaa.sh`) jatkuvat taustatietona; niistä ei lasketa U:ta.
- Jos T + 14 vrk -haku epäonnistuu, käytetään lähintä onnistunutta hakua ja kirjataan
  poikkeama. Mittaus 15 vuorokauden jälkeen ei ole hyväksyttävä, koska ikkuna on
  silloin siirtynyt.

### D-portti: RIITTÄMÄTÖN HAVAITTU ALTISTUS (Insufficient Observable Exposure, IOE)

Pisteet ja kommentit ovat reaktioita ja riippuvat sisällöstä, joten ne eivät kelpaa
altistuksen mittariksi. Ainoa suoraan havaittava altistus on **sijoitus HN:n
topstories-listan 30 ensimmäisen joukossa** (etusivu), jonka `04-hn-seuranta.py`
mittaa 15 minuutin välein 48 tuntia. Pisteet, kommentit ja dead/flagged-tila kirjataan,
mutta niitä ei käytetä D:n arviointiin.

- **E** = niiden 15 minuutin mittausten määrä 48 tunnissa, joissa postaus oli top 30:ssä.
  E × 15 min on havaitun etusivualtistuksen alaraja.
- **Altistus havaittu:** E ≥ 4 (vähintään noin tunti etusivulla). Vasta tällöin U
  tulkitaan AUDIENCE-tuloksena.
- **IOE:** E ≤ 3. Merkitys: *meillä ei ole riittävää havaintoa siitä, että sisältö altistui
  tarpeeksi suurelle yleisölle AUDIENCE-tuloksen tulkitsemiseksi.* Se **ei** tarkoita,
  ettei sisältöä näytetty ihmisille: /newest-sivun lukijat ja E:n 1 - 3 mittausta ovat
  altistusta, jota emme voi määrällistää. IOE ei ole KILL eikä NO DISTRIBUTION.
- Dead tai flagged 2 tunnin sisällä kirjataan erikseen ("moderoitu pois"), ja se on IOE:n
  alatapaus.

### AUDIENCE-kynnykset ja niiden perustelu

U:n semantiikka muuttui summasta 14 päivän uniikeiksi, mikä pienentää lukua. Kynnykset
arvioitiin uudelleen eikä säilytetty automaattisesti:

- **PASS: U ≥ 500** riippumatta E:stä. Perustelu: 500 GitHubin uniikkia kävijää 14
  päivässä tuoreelle repolle, jonka baseline on 0, on selvä signaali riippumatta
  reitistä. Toissijaiset lähteet raportoivat etusivun tuovan 10 000 - 30 000 kävijää
  vuorokaudessa ja noin 35 - 40 kävijää minuutissa sijalla 17; 500 on siitä murto-osa,
  joten raja ei vaadi etusivumenestystä, vain havaittavan kiinnostuksen.
- **KILL: E ≥ 4 ja U < 50.** Perustelu: jos postaus oli vähintään tunnin etusivulla,
  altistus oli tuhansia näyttöjä (INFERENCE toissijaisista luvuista), ja alle 50
  uniikkia kävijää tarkoittaa, että altistuneet eivät klikanneet. Se on sisältötulos.
  KILL koskee tätä sisältöä, kanavaa ja identiteettiä, ei yleisötilaa yleensä.
- **UNKNOWN: E ≥ 4 ja 50 ≤ U < 500.** Sallii toisen kanavan kerran.
- **IOE: E ≤ 3 ja U < 500.** AUDIENCE ei tulkittavissa.

Luvut 500 ja 50 ovat päätösrajoja, eivät datasta johdettuja vakioita. Muutos edelliseen:
KILL vaatii nyt havaitun altistuksen; ilman sitä alhainen U on IOE.

### ACCESS

Määritelmä ja mittari I ennallaan (neljä ehtoa, kaksi itsenäistä luokittelijaa).
Tulosnimet: **ACCESS PASS** (I ≥ 1) ja **ACCESS EI HAVAITTU** (I = 0 ja epäselviä 0
14 päivässä). Jälkimmäinen tarkoittaa vain, ettei tämä julkaisu tuottanut
oma-aloitteista pääsyä 14 päivässä; se ei tarkoita, ettei pääsyä voi rakentaa.
Epäselviä ≥ 1 ja I = 0 → ACCESS UNKNOWN.

### Korjattu päätösmatriisi

| AUDIENCE | ACCESS | Mitä voidaan päätellä | Mitä ei voida päätellä | Päätös |
|---|---|---|---|---|
| PASS | PASS | Tuore identiteetti sai sekä huomiota että pääsyä tällä sisällöllä | Kestävyys, rahaksi muuttuminen | Pääsy käsitellään; koe 06 suunnitellaan sisääntulevan reitin rinnalle; toinen julkaisu aikaisintaan 30 pv |
| PASS | EI HAVAITTU | Huomio syntyi, pääsyä ei 14 päivässä | Että huomio ei voi muuttua pääsyksi (aikaikkuna oli 14 pv, n = 1) | Ei uutta postausta; koe 06 (neutraali kylmä reitti) seuraavaksi |
| KILL | PASS | Altistuneet eivät klikanneet, mutta joku otti yhteyttä | Yleisötilan mahdottomuus | Pääsy käsitellään; yleisöreitti sivuun tällä sisällöllä |
| KILL | EI HAVAITTU | Tämä sisältö, kanava ja identiteetti eivät tuottaneet kumpaakaan | Että projekti ei voi rakentaa yleisöä muulla sisällöllä tai kanavalla | Yleisöreitti sivuun määräajalla; koe 06 seuraavaksi |
| UNKNOWN | mikä tahansa | Kiinnostusta oli, määrä ei ratkaise | - | Toinen kanava kerran (r/opensource, tuore tili), sitten tulkinta uudelleen |
| IOE | PASS | Pääsy syntyi ilman mitattavaa altistusta | Mitään yleisöstä | Pääsy käsitellään; AUDIENCE jää tulkitsematta |
| IOE | EI HAVAITTU | Ei riittävää havaintoa altistuksesta; pääsyä ei 14 päivässä | Mitään sisällön kiinnostavuudesta | Second-chance pool kerran (HN:n FAQ:n mukainen viesti hn@ycombinator.com), jos nostetaan → uusi 48 h D-mittaus; muuten toinen kanava kerran; jos yhä IOE → AUDIENCE UNKNOWN, kirjataan tuoreen identiteetin jakelurajoitteena |

Yleissääntö: yhdestäkään rivistä ei päätellä mitään mekanismista, rahasta tai
yleisötilan yleisestä mahdollisuudesta. Kaikki tulokset koskevat tätä sisältöä, tätä
kanavaa, tätä identiteettiä ja 14 päivän ikkunaa.
