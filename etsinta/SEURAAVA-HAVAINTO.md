# Seuraava päätöstä eniten muuttava havainto (kokeen 03 jälkeen)

2026-09-16, Claude. Lähtökohta: `kokeet/03-toistuvuusmittaus.md` (commit `a99edc3`).
Ei uutta teoriaa, ei liiketoimintaideoita, ei kokeen suorittamista. Kaksi uutta
tarkistettua faktaa tässä kierroksessa: repo `original-private-account/eikaisiina` on **yksityinen**
(GitHub API: `private: true`, 14 päivän näytöt 0, kloonit 0, tähdet 0), ja Docker ei ole
koneella (WordPress-koe vaatisi PHP:n ja WP-CLI:n natiiviasennuksen).

## 1. Mitä koe 03 oikeasti opetti

**FACT (20 havaintoa):**
- 15/20 ladatuinta PyPI-orpoa asentuu lähteestä ja wheelinä ja importoituu Python 3.14:llä.
- 5/20 epäonnistui: puuttuva riippuvuus (django), metapaketti ilman moduulia (protokollan
  artefakti), riippuvuuden poistettu API (pydantic 2 `const`), `pkg_resources` (setuptools ≥ 81),
  ja rakennusvaiheen 5 minuutin aikaraja (scrapbookin riippuvuuspuu lähteestä).
- Viisi eri virheilmoitusta. Yksikään ei toistunut normalisoinnin jälkeen.
- Yhdelläkään otoksen paketilla ei ollut tietoturva-advisoryä.
- Positiivinen kontrolli (html5lib 1.1) epäonnistui odotetusti.

**INFERENCE (orpo Python-ohjelmisto yleisemmin):**
- Latauksilla painotettu orpopopulaatio on pieniä, valmiita apukirjastoja (funcsigs,
  textwrap3, jcs, pip-hello-world). Ne ovat "orpoja" siksi, ettei niissä ole enää mitään
  tehtävää. Tämä on sama havainto kolmannen kerran (npm 1/3, GPT 10/12, nyt 15/20).
- Ne, jotka rikkoutuvat, rikkoutuvat siksi, että **riippuvuus liikkui niiden alta**
  (pydantic 2, setuptools 81, django pinnaamatta), ei oman koodinsa takia. Riippuvuudet
  liikkuvat toisistaan riippumatta, joten rikkoutumiset ovat heterogeenisia.
- Python 3.14 ei ollut yhteinen syy: kieliversio itsessään rikkoi 0/20 (`ast.Str`-tyyppisiä
  ei löytynyt otoksesta), setuptoolsin muutos 1/20.
- Otanta latausten mukaan ei ole otanta rikkoutumisten mukaan. Populaatio "orvot, joista
  käyttäjät valittavat" olisi eri, ja siitä ei ole otantakehikkoa.

**HYPOTHESIS (artefakti-S yleisesti):**
- Uudelleenkäytettävä korjaustieto voi syntyä vain, kun rikkoutumisella on **yhteinen syy**
  (yksi alustamuutos, joka osuu moneen samalla tavalla). Toisistaan riippumaton
  riippuvuusdrifti ei tuota sitä. Tämä on hypoteesi, jonka koe 03 tukee negatiivisesti
  (ei yhteistä syytä → ei toistuvuutta) mutta ei testaa positiivisesti.
- Sama rakenne pätee minkä tahansa artefakti-S:n olemassaoloon: toistuvuus ei ole
  populaation ominaisuus vaan *syyn* ominaisuus. Oikea kysymys ei ole "onko luokassa
  toistuvuutta" vaan "onko luokassa yhteistä syytä".

**Herkkyys K = 1 vs. K = 3.** Lukitun tekstin normalisointi antoi K = 1 (KILL);
esirekisteröidyn skriptin laajempi normalisointi antoi K = 3 (UNKNOWN, laajennus 40:een).
Sisällöllisesti kolme `No module named` -riviä ovat kolme eri korjausta (lisää riippuvuus;
ei mitään korjattavaa; korvaa pkg_resources), joten K = 1 on oikea *korjausmallien*
laskuna. Mutta evidenssiarvon kannalta olennaista on testin erottelukyky: 20 rivin otos ja
kynnys K ≥ 3 havaitsevat vain korjausmallin, jonka osuus populaatiosta on suuruusluokkaa
15 % tai enemmän (CALC: odotusarvo 20 × p ≥ 3 → p ≥ 0,15). **Koe 03 osoittaa, ettei
tässä populaatiossa ole yhtä korjausmallia, jonka osuus on ≥ 15 %.** Se ei osoita, ettei
olisi mallia, jonka osuus on 5 %. Tulos on KILL protokollan mukaan, ja sen tutkimuksellinen
sisältö on "ei hallitsevaa yhteistä syytä", ei "ei mitään toistuvaa".

## 2. WordPress-kokeen informaatioarvo, kirjoitettuna ennen suorittamista

**Hypoteesi, jota se testaisi:** lisäosaekosysteemissä, jossa yksi alusta (WordPress-ydin,
PHP-versio) liikkuu kaikkien alta samaan aikaan, hylätyt mutta asennetut lisäosat
rikkoutuvat yhteisestä syystä (PHP 8.x: poistetut funktiot, dynaamiset ominaisuudet,
jQuery-migraatio), jolloin K ≥ 3.

| Tulos | Mitä muuttaisi | Päätös sen jälkeen |
|---|---|---|
| PASS | Artefakti-S mahdollinen siellä, missä on yhteinen syy. Hypoteesi §1 saisi ensimmäisen positiivisen tuen. Kortti `pakotetut-alustamigraatiot` saisi ensimmäisen evidenssin | Ajetaan paritettu koe B WordPress-luokassa |
| KILL | Toinen ekosysteemi ilman toistuvuutta. Hylätyn ohjelmiston korjaus kuolee kahdella suurimmalla julkisella hakemistolla | Suljetaan korjaushaara; siirrytään ei-artefaktitiloihin |
| UNKNOWN | Laajennus 40:een | Sama kuin edellä yhden laajennuksen jälkeen |

**Kuinka paljon uutta KILL antaisi?** Vähän. Nykyinen evidenssi samaan suuntaan: 80 issuen
otos (omistajat eivät pidä koodia esteenä), npm 1/3 valmiita, GPT 10/12, koe 03 15/20,
WordPress-orvoista 40 %:lla jo fork, ja **vain 15/166 yli 10 k asennuksen WordPress-orvosta
on yhtään avointa tukiketjua** (FACT, `data/orvot/wordpress-orvot-top10000.csv`). Viimeinen
luku kertoo jo, ettei käyttäjiltä tule rikkoutumisilmoituksia, mikä laskee sekä R:n että
"omistaja välittää" -oletuksen ennakkoa. KILL olisi viides havainto samaan suuntaan.
PASS olisi yllättävä ja arvokas, mutta sen ennakko on matala samasta syystä.

**Kustannus:** 0 €, ihmisaikaa 1 - 2 h (PHP + WP-CLI + SQLite-integraatio brew:lla, koska
Dockeria ei ole), tokeneita 0,3 - 0,6 M. Ei lupaa.

**Tuomio:** WordPress on halpa ja luvaton, mutta sen odotettu informaatio on pieni, koska
KILL on todennäköinen ja vahvistaisi jo tiedetyn. Sitä ei valita inertian takia.

## 3. "Jos WordPresskin KILL, artefakti-S kuolee kokonaan" on väärin

**Artefakti-S:n määritelty populaatio:** mikä tahansa koneen käytettävä säilyvä tila, joka
laskee seuraavan tapauksen kustannusta: korjausmallit, testikorpukset, luokittelusäännöt,
prosessikuvaukset lomakkeineen, datarekisterit, käännösmuistit, skannerit.

**Rakenteellisesti erilaiset luokat aineistossa:**

| Luokka | Esimerkki projektista | Toistuvuus | Tila |
|---|---|---|---|
| a. Koodikorjausmallit alustamigraatioissa | PyPI (koe 03), WordPress, Manifest V3 | Vain jos yhteinen syy | PyPI: KILL. Muut: mittaamatta |
| b. Prosessiartefaktit oikeuksien lunastuksessa | Lähdeveron lomake per maa, EU261-menettely | **Rakenteellisesti 100 %**: sama lomake jokaiselle Sveitsin osingolle | Toistuvuus ei ole kysymys; kysymys on valtakirja ja kaappaus |
| c. Data-artefaktit | Orpolistat, AKR-kieliparit, CWS-otos | Toistuvuus on skannerin ominaisuus | Toimii; kaupallinen arvo UNKNOWN |
| d. Todennus- ja testikorpukset | GPT:n näyttövaranto | Vaatii saman perheen tapauksia | Mittaamatta |
| e. Käännösmuistit ja sanastot | Auktorisoitu kääntäminen | Korkea samassa asiakirjatyypissä | Vaatii kielitaidon |

PyPI ja WordPress ovat molemmat luokkaa a, ja jopa sen alaluokkaa "hylätty ohjelmisto
julkisessa hakemistossa". WordPressin KILL tappaisi enintään luokan a tässä alaluokassa.
Luokassa b toistuvuus on olemassa määritelmällisesti, eikä yksikään ohjelmistokoe voi
tappaa sitä. **Koko haaraa ei voi tappaa yhdellä kokeella, koska "artefakti-S" on
ominaisuus, ei mekanismi.** Se voidaan tappaa vain luokka kerrallaan, ja luokissa b - e
tappava kysymys ei ole toistuvuus vaan kaappaus tai kyky. Väite rajataan: *"artefakti-S
hylätyn ohjelmiston korjauksessa"* on se, mikä kuolisi.

## 4. Vaihtoehdot, jotka eivät perustu hylätyn ohjelmiston korjaamiseen

Tutkimuskysymys: missä pieni määrä ihmisen ja frontier-mallin työtä muuttaa oikeutta,
pääsyä, koordinaatiota, informaatiota tai muuta tilaa niin, että seuraavan kierroksen
talous paranee? Aineistosta nousevat mekanismiluokat, joilla on jo kortti tai muistio ja
ratkaisematon kriittinen oletus:

| | Mekanismiluokka | Ratkaisematon oletus | Halvin havainto | Raha | Ihmisaika | PASS / KILL muuttaisi |
|---|---|---|---|---|---|---|
| W | Alustamigraation korjausmallit (WordPress) | Yhteinen syy tuottaa K ≥ 3 | Koe 03:n protokolla WP-listalle | 0 € | 1 - 2 h + 0,5 M tokenia | PASS: koe B. KILL: viides samansuuntainen havainto |
| Y | **Yleisötila** (maine yleisönä, ainoa 0 euron ei-artefaktitila) | Tuottaako todennettu julkinen loki lukijoita ja yhteydenottoja; tila on nyt täsmälleen 0, koska repo on yksityinen | Repo julkiseksi + yksi englanninkielinen tiivistelmä yhteen ennalta valittuun kanavaan; GitHubin traffic-rajapinta mittaa 14 pv | 0 € | omistaja 1 h (julkaisupäätös, tiivistelmän tarkistus, postaus) | PASS: jakelu on olemassa, kylmä yhteydenotto vältetään myöhemmissä kokeissa. KILL: yleisösilmukka kuollut tässä koossa; jokainen myöhempi mekanismi vaatii luvallisen kylmän yhteydenoton |
| V | **Valtakirjatila** (oikeuksien lunastus, luokka b) | Tuottaako yksi onnistunut lunastus toisen valtakirjan; onko yksittäinen palautus yli kustannuksen | Yksi tuttu, jolla on ulkomaisia osinkoja: lasketaan palautettava summa raportista, haetaan Veron todistus, täytetään yhden maan lomake; mittarit tunnit, euro, tuliko toinen henkilö | 0 € (todistus maksuton, UNKNOWN maakohtaiset maksut) | omistaja 2 h + tuttu 1 h + palautuksen odotus 2 - 6 kk | PASS: ensimmäinen todennettu valtakirja, silmukka A elää. KILL: lunastus ei kata vaivaa tai toista ei tule |
| P | Pätevyysportit (auktorisoitu kääntäjä, luokka e) | Onko omistajalla tai lähipiirillä tutkintotason harvinainen kieli | Yksi kysymys omistajalle | 0 € | 5 min | PASS: kortti elää, tutkintoon marraskuussa 2027 (2026 ilmoittautuminen päättynyt, FACT GPT). KILL: kortti kuolee meille, säilyy mekanismina |
| O | Omistajan maksuhalukkuus migraatiosta (luokka a:n kysyntäpuoli) | Vastaavatko orpojen omistajat ja maksavatko | Ennen yhteydenottoa: 15/166 avointa tukiketjua on jo havainto kysynnän puutteesta | 0 € | 0 h (jo mitattu) | Nykyinen luku on lähes KILL: käyttäjät eivät valita, joten omistajilla ei ole painetta |

Vertailu periaatteella odotettu päätösinformaatio / euro / ihmistunti, ilman lukuja:
- **W:** halpa, luvaton, mutta tulos on lähes ennakoitavissa (KILL) ja muuttaa vähän.
- **Y:** halpa, vaatii omistajan päätöksen, ja tulos muuttaa **kaikkien** myöhempien kokeiden
  rakennetta (tarvitaanko kylmää yhteydenottoa vai ei). Testaa tilaa, jota kolme muistiota
  on nimennyt ja jota ei ole koskaan mitattu, koska se on ollut 0 rakenteellisesti. Sen
  ennakko on aidosti epävarma: emme tiedä, kiinnostaako "23 % laajennuksista katosi" tai
  "1/80 pyysi rahaa" ketään.
- **V:** korkein informaatio mekanismista, mutta hidas (kuukausia) ja riippuu tutun
  löytymisestä. Ei poissulkeva Y:n kanssa; voidaan käynnistää rinnalla.
- **P:** halvin kaikista, mutta ratkaisee pienen ja kapasiteettirajoitetun haaran.
- **O:** jo mitattu, ei tarvitse koetta.

**Valinta: Y.** Se on ainoa havainto, joka (1) maksaa 0 €, (2) vie alle tunnin, (3) testaa
ei-artefaktitilaa, jota teoria pitää välttämättömänä ja jota ei ole koskaan mitattu, ja
(4) muuttaa päätöstä molempiin suuntiin: PASS avaa sisääntulevan kanavan kokeille V ja O,
KILL pakottaa jokaisen jatkokokeen luvalliseen kylmään yhteydenottoon ja poistaa
"yleisösilmukan" projektin silmukoista. P kysytään samalla, koska se maksaa 5 minuuttia.
W jää varalle: se ajetaan vain, jos Y on KILL ja halutaan vielä yksi luvaton havainto.

## 5. Koe 04: yleisötilan mittaus (lukittu, ei suoritettu)

**Hypoteesi H4:** projektin todennetut, muualta puuttuvat luvut tuottavat julkisesti
jaettuna lukijoita ja vähintään yhden asiallisen sisääntulevan yhteydenoton 14 päivässä.

**Mitä tila on:** yleisö, joka kuluttaa maineen huomiollaan. Ei-artefakti. Ainoa
vastafaktuaali on nykytila: 0 näyttöä, 0 kloonia, 0 tähteä, repo yksityinen (FACT
2026-09-16). Baseline on siis mitattu ja se on nolla.

**Toimenpide (omistaja suorittaa, Claude valmistelee):**
1. Claude kirjoittaa yhden englanninkielisen tiivistelmän (enintään 900 sanaa) otsikolla,
   joka ei lupaa liiketoimintaa, ja jossa on vain FACT-merkityt luvut lähteineen: 23 %
   yli 10 k käyttäjän Chrome-laajennuksista poistettu 20 kk:ssa (n = 390), 1/80 hylätyn
   projektin omistajaa pyysi rahaa, 15/20 ladatuinta PyPI-orpoa toimii Python 3.14:llä,
   40 % WordPress-orvoista jo forkattu, ukraina→suomi auktorisoituja kääntäjiä 6.
   Ei kehotusta ottaa yhteyttä. Ei tuotetta. Tiivistelmä tallennetaan repoon ennen
   julkaisua (`etsinta/JULKAISU-1.md`) ja se on omistajan hyväksymä.
2. omistaja muuttaa repon julkiseksi. Ennen sitä Claude ajaa salaisuustarkistuksen
   (`git log -p | grep` avaimille) ja omistaja vahvistaa, ettei repossa ole henkilötietoja,
   joita hän ei halua julkaista. `.env` on gitignoressa (FACT).
3. omistaja postaa tiivistelmän **yhteen** ennalta valittuun kanavaan. Kanava lukitaan
   tässä: Hacker News, "Show HN" ei sovi (ei tuote), joten tavallinen linkkipostaus
   repon README:hen tai tiivistelmään. Perustelu: kanava, jossa avoimen lähdekoodin
   ylläpidon ja laajennusten turvallisuuden luvut ovat relevantteja, ja jossa 0 €
   riittää. Vain yksi postaus, yksi kerta. Ei ristiinpostausta, ei uudelleenpostausta.
4. Mittaus 14 päivää postauksesta GitHubin traffic-rajapinnasta (`gh api
   repos/original-private-account/eikaisiina/traffic/views` ja `/clones`, päivittäin, koska rajapinta
   säilyttää vain 14 päivää) sekä repon issuet, tähdet, forkit ja omistajan sähköposti.

**Mittarit (lukittu):**
- U = uniikit näyttäjät 14 päivässä (traffic/views.uniques).
- S = tähdet 14 päivässä.
- I = asialliset sisääntulevat yhteydenotot (issue, sähköposti tai viesti, jossa
  toinen osapuoli tarjoaa dataa, tapausta, yhteistyötä tai korjausta lukuihin; ei
  spämmi, ei pelkkä "kiinnostavaa"). omistaja luokittelee, Claude kirjaa perustelun.

**Tulkinta (lukittu ennen julkaisua):**
- **PASS:** I ≥ 1 tai U ≥ 500. Yleisötila on olemassa; kokeet V ja O suunnitellaan
  sisääntulevan kanavan varaan; toinen julkaisu sallitaan aikaisintaan 30 päivän päästä.
- **KILL:** U < 50 ja I = 0. Yleisösilmukka kuollut tässä koossa ja tällä sisällöllä;
  poistetaan projektin silmukoista; jatkokokeet vaativat luvallisen kylmän yhteydenoton.
  Toista julkaisua ei tehdä ilman uutta evidenssiä.
- **UNKNOWN:** 50 ≤ U < 500 ja I = 0. Yksi toinen kanava sallitaan kerran (lukitaan
  silloin etukäteen), sen jälkeen ei enää.

**Tappiobudjetti:** 0 € tästä 200 eurosta. Ihmisaika: omistaja enintään 1 h + 14 × 2 min
lukemiseen. Claude: tiivistelmä ja päivittäinen mittaus.

**Riskit ja rajat:** yksi postaus on n = 1 kanavasta; kanavan algoritmi on satunnainen.
Siksi KILL-raja on matala (50) ja PASS-raja vaatii joko yhteydenoton tai selvän
lukijamäärän. Julkaisu on peruuttamaton siltä osin, että repo on luettu; sen sisältö on
omistajan päätös. Tiivistelmä ei saa sisältää mitään, mikä kutsuu haitallisia ostajia
(laajennusten ostomarkkinan yksityiskohdat kerrotaan lähteiden tasolla, ei ohjeena).

**Mitä koe ei kerro:** kestääkö yleisö, muuttuuko se rahaksi, toimiiko se suomeksi.
Se kertoo vain, onko tila nollasta poikkeava, kun se kerran yritetään käynnistää.

**Rinnalla, ei koe:** kysymys P omistajalle (kieliparit). Vastaus kirjataan päätöslokiin.
