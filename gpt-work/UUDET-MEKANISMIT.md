# Taloudelliset primitivit ja avoin tutkimuskierros

2026-09-15 · GPT Work. Alla ei ole lista todistetuista liiketoiminnoista. Mekanismien olemassaolo, meille pääsy ja kasautuva etu ovat eri väitteitä.

## 1. Pienimmät hyödylliset rakennuspalikat

**INFERENCE:** Oikeus, luottamus, pääoma ja historia eivät ole saman tason käsitteitä. Oikeus määrittää sallittuja toimia. Luottamus vaikuttaa arvioituun riskiin. Pääoma siirtää ostovoimaa ajassa. Historia on havaintojen varanto. Pelkkä nimiluettelo ei vielä generoi mahdollisuuksia.

Seuraava on työhypoteesi hyödyllisestä jaottelusta, ei todistettu ainut oikea talousteoria.

| Primitiivi | Operatiivinen kysymys | Mitä AI muuttaa | Mitä pelkkä kopioitu malli ei tuota |
|---|---|---|---|
| Maksukykyinen tavoite ja vaihtoehdot | Kuka haluaa minkä muutoksen ja mitä tekisi ilman meitä? | Tarpeen ja vaihtoehtojen löytämistä | Ostajan budjettia tai maksuhalukkuutta |
| Toteutuskelpoinen muunnos | Millä panoksilla muutos saadaan aikaan? | Suunnittelua, ohjelmointia, optimointia | Fyysistä suoritetta tai toimivaa prosessia oletusarvoisesti |
| Päätös- ja poissulkuvalta | Kuka saa sallia, estää, vaihtaa tai käyttää? | Oikeuksien tulkinnan avustamista | Omistajan suostumusta, lupaa tai valtuutusta |
| Hyväksyttävä näyttö | Kuka ratkaisee että tulos on oikea? | Ehdotusten ja testien tekemistä | Todellista mittausta tai riippumattoman hyväksyjän päätöstä |
| Arvonjako ja maksun toteutuminen | Mikä antaa meille korvauksen ja milloin se maksetaan? | Sopimusvaihtoehtojen valmistelua ja seurantaa | Vastapuolen sitoutumista tai neuvotteluvoimaa |
| Aika, epävarmuus ja vastuu | Kuka kantaa odotuksen, epäonnistumisen ja häntäriskin? | Joitain ennuste- ja valvontakustannuksia | Tasekapasiteettia tai jo aiheutunutta vahinkoa |
| Säilyvä tila ja palaute | Mikä ensimmäisestä suorituksesta muuttaa seuraavaa? | Tiedon jalostamista ja uudelleenkäyttöä | Historiaa todellisista hyväksytyistä suorituksista |

**INFERENCE:** Rahavirran vastaanottajan määrää näiden yhteispeli ja vastapuolten vaihtoehdot. ”Me tuotimme eniten arvoa” ei yksin määritä korvausta. ”Meillä on oikeus” ei yksin määritä että oikeudella on ostaja.

**HYPOTHESIS:** Kiinnostavin halvan AI:n vaikutus voi olla halpa ehdotusten tuotanto yhdistettynä kalliiseen mutta uudelleenkäytettävään palautteeseen. Jokainen oikea koe synnyttää informaatiota jota seuraava mallikutsu ei ilman koetta tiedä. Etu katoaa jos palautteen saa kuka tahansa yhtä halvalla, sen uudelleenkäyttö on kielletty tai tehtävät eivät toistu.

## 2. Generaattori on porttiketju

Älä aloita toimialalistasta. Etsi jokin näistä ristiriidoista:

1. Maksukykyinen tarve on olemassa mutta yksittäisen ostajan määrä ei kata kiinteää kustannusta.
2. Ratkaisuja voi generoida halvalla mutta niiden kelpoisuuden osoittaminen on kallista ja toistuvaa.
3. Resurssi on yhdelle kustannus ja toiselle tuotantopanos mutta yhteensopivuutta ei ole osoitettu.
4. Sama hyväksytty havainto voisi ratkaista usean maksajan ongelman mutta tiedon laillinen uudelleenkäyttö on järjestämättä.

Jokaisesta osumasta täytetään seuraavat kentät. Tyhjä kriittinen kenttä pysäyttää kaupallisen väitteen, ei muutu optimistiseksi pisteeksi.

| Kenttä | Vaadittava näyttö |
|---|---|
| Kuka maksaa? | Nimetty organisaatio tai tarkasti määritelty ostajarooli, budjettiperuste |
| Miksi raha on olemassa? | Nykyinen kustannus, vältetty tappio tai hyväksytty uusi suorite |
| Nykyinen vastaanottaja | Toimittaja, työntekijä, alusta tai tieto siitä ettei kauppaa synny |
| Miksi nykyinen saa sen? | Kontrolli, näyttö, sopimus, kapasiteetti tai asiakkaan paras vaihtoehto |
| Mikä estää muita? | Konkreettinen pääsy-, todistus-, koordinointi- tai toteutuseste |
| Tarvittava niukka resurssi | Ei sana ”data” vaan nimetty aineisto, lupa, hyväksyntä tai kapasiteetti |
| Laillinen hankinta | Oikeudenhaltija ja tapa saada oikeus ilman oletettua suostumusta |
| Meidän korvaus | Kuka sopii maksusta, mistä tuloksesta ja millä perusteella |
| Kasautuva tila | Mitä ensimmäinen onnistuminen jättää ja miten toinen paranee |
| Tappava vastanäyttö | Etukäteen nimetty havainto joka lopettaa tämän version |
| Seuraava mittaus | Havainto joka erottaa kilpailevat selitykset |

Tekninen minimituotos on [mechanism-cards.json](data/mechanism-cards.json) ja paikallinen tarkistin [check_evidence.py](check_evidence.py). Se ei hae internetistä, ota yhteyttä tai päätä kannattavuudesta. Se estää puuttuvien porttien esittämisen vahvistettuina mahdollisuuksina. Suurta keruujärjestelmää ei rakennettu, koska maksajan ja arvonjaon näyttö puuttuu.

## 3. Avoin kierros: ehdollinen kysyntä luo uuden toimituskelpoisen erän

Tämä kierros aloitettiin ilman bountyja, agenttimarkkinoita, lunastamattomia oikeuksia, maksuauditointia, julkisia hankintoja, reservejä tai orpoja digitaalisia tuotteita.

**Mekanismi:** monella pienellä ostajalla on sama tarve. Tuotannon tai valmistelun kiinteä kustannus estää yksittäisen kaupan. Yhteensopivat ehdolliset tilaukset muuttavat kokonaisuuden toteuttamiskelpoiseksi. Esimerkkialue on erikoisvalmistuksen yhteinen pieni tuotantoerä. Yksi ihminen voisi ensin tehdä pelkän erittelyn ja yhteensopivuuden tarkistuksen, ei ryhtyä valmistajaksi tai vastaanottaa ennakkomaksuja.

**FACT:** Kickstarterin all-or-nothing-malli osoittaa toimivan ehdollisen rahoitusmekanismin olemassaolon: alle tavoitteen jäävä kampanja ei veloita tukijoita. **INFERENCE:** tämä ei osoita että ehdollisten teollisten tilausten järjestäjä saisi katetta tai että alustatoiminta olisi meille sopiva. [Kickstarter](https://help.kickstarter.com/en-us/articles/16236582-why-is-funding-all-or-nothing)

| Generaattorin kysymys | Tämän mekanismin vastaus |
|---|---|
| Maksaja ja raha | HYPOTHESIS: pienostajat maksavat tarvitsemastaan toimituksesta jonka yksikköhinta laskee yhteisessä erässä |
| Nykyinen vastaanottaja | Valmistaja saa nykyiset kannattavat erät; pienet erät jäävät ostamatta tai ostetaan kalliilla |
| Este | Eri spesifikaatiot, aikataulut ja luottamus siihen että muutkin osallistuvat |
| Niukka resurssi | Yhteensopivat todelliset tarpeet sekä valmistajan hyväksymä erittely |
| Laillinen pääsy | Ostajien lupa tarpeen käsittelyyn ja myöhemmin selkeät ehdolliset tilaukset; ei oletettua valtuutusta |
| Meidän osuus | UNKNOWN: maksaako ostaja tai valmistaja erän kokoamisesta vai ohittavatko ne meidät? |
| Kasautuminen | HYPOTHESIS: uudelleenkäytettävät speksit ja toimitushistoria vähentävät seuraavan erän sovitustyötä; uusi ostaja voi parantaa erän toteutumista muillekin |
| Vahvin vastaväite | Ensimmäisen tutustuttamisen jälkeen ostajat tilaavat suoraan. Räätälöinti palauttaa jokaisen erän erilliseksi projektiksi |

**CALCULATION, symbolinen:** jos yhteisen erän kiinteä kustannus on F ja muuttuva kustannus c per yksikkö, n identtisen yksikön tekninen keskihinta on F/n + c ennen koordinointia, riskiä ja katteita. AI voi laskea koordinointia mutta ei itsessään pienennä F:ää. Malli ei takaa järjestäjän osuutta säästöstä.

**Kevyt generaattori:** yhdistä julkaistut minimierät ja nimettömiksi tehdyt todelliset tarve-erittelyt, tunnista yhteinen spesifikaatio ja aikataulu. Julkinen minimitilaus yksin ei riitä. Tässä ei saatu yhtään ostajien vahvistamaa erää. UNKNOWN.

**Tapporaja:** kaksi tarvetta eivät ole yhteensopivia ilman kallista räätälöintiä tai kukaan ei hyväksy järjestäjän korvausta vaikka laskennallinen säästö olisi tosi. **Seuraava portti:** luvalliset tarvetiedot ja ei-sitova valmistusarvio. Yhteydenottoa tai tilausta ei tehty.

## 4. Avoin kierros: hyväksyttävä näyttö tekee ehdotuksesta myytävän

**Mekanismi:** lähes ilmainen älykkyys tuottaa paljon ehdotuksia. Ostajan hyväksymää näyttöä niiden toimivuudesta ei synny samalla määrällä. Toimija joka hallitsee toistettavaa arviointia voi löytää ja osoittaa parannuksia. Ensimmäinen hyväksytty poikkeamatapaus täydentää testiympäristöä, joka parantaa seuraavan ratkaisun laatua.

**FACT, toimijan raportti:** AlphaEvolve käyttää ohjelmallista arviointia algoritmien kehittämiseen. Google Cloud kuvaa samaa perusmenetelmää myös palveluna. Kaksi saman yritysryhmän julkaisua eivät ole riippumaton varmennus tulosluvuille. [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-on-google-cloud/)

**INFERENCE:** kiinnostava niukkuus ei tässä ole lisää mallikutsuja vaan pätevä arvioija ja palautteen kattavuus. Ehdotusten halvettua arviointipullonkaula voi kasvaa. Arviointikin voi automatisoitua ja sen saatavuus voi poistaa edun. Siksi ”myydään testejä” ei vielä riitä.

| Generaattorin kysymys | Vastaus |
|---|---|
| Maksaja | HYPOTHESIS: järjestelmän omistaja jonka nykyinen prosessi kuluttaa mitattavasti aikaa, energiaa tai materiaalia |
| Miksi raha on olemassa | Toteutunut resurssikulutus tai virhekorjaus, ei abstrakti AI-budjetti |
| Nykyinen vastaanottaja | Sisäinen kehitys, nykyinen ohjelmisto-/laitevalmistaja tai kulutuksen myyjä |
| Miksi nykyinen saa sen | Pääsy järjestelmään, luotettu mittaus ja käyttöönoton valta |
| Este | Julkinen benchmark ei vastaa ostajan todellista hyväksyntää |
| Niukka resurssi | Edustava testi, todelliset virhe-esimerkit ja ostajan hyväksymä mittari |
| Laillinen hankinta | Read-only-analyysi asiakkaan luvalla ja erikseen sovittu anonymisoitujen testisääntöjen uudelleenkäyttö |
| Meidän korvaus | UNKNOWN: ennalta sovittu todentamis- tai tuloskorvaus; ei seuraa löydöstä automaattisesti |
| Kasautuminen | HYPOTHESIS: hyväksytyt testit ja ratkaisut toimivat myös seuraavassa ympäristössä |
| Vahvin vastaväite | Asiakas voi ajaa saman optimoinnin itse. Osaaminen ja aineisto eivät siirry. Parannus johtuu testin ylisovittamisesta |

**Kevyt generaattori:** etsi julkisia teknisiä migraatioita ja toistuvia yhteensopivuusongelmia vain niiltä alueilta joissa toimivuus voidaan ratkaista suorittamalla tai mittaamalla. Lisää maksajan nykyinen kustannus vasta asiakkaan näytöstä. Julkinen issue ei ole tilaus. Ensimmäinen kokeellinen kohde voi olla turvallinen tiedosto-/rajapintamuunnos offline-kopioilla. Ei tuotannon muuttamista, henkilötietoja tai turvallisuuskriittisen järjestelmän optimointia.

**Tapporaja:** halvin samaa AI:ta käyttävä vertailu läpäisee saman sokkotestin samalla työllä tai kertynyt testivaranto ei auta uutta tapausta. **Seuraava kysymys:** jääkö uudelleenkäytettävästä näytöstä hyötyä sen jälkeen kun asiakaskohtainen data poistetaan?

## 5. Avoin kierros: fyysisen resurssin todistettu korvaavuus

**Mekanismi:** yhdelle yritykselle ylijäämä on kustannus, toiselle yhteensopiva materiaali korvaa ostettavan panoksen. Ilmoitusten yhdistäminen ei riitä. Arvo syntyy vasta kun laatu, määrä, ajankohta, kuljetus ja sallittu käyttötapa sopivat. AI voi laskea teknisten kuvausten vertailun kustannusta mutta ei osoittaa näytteen laatua.

**FACT:** Motivan ylläpitämä Materiaalitori on jo maksuton markkinapaikka materiaaleille, sivuvirroille ja palveluille. Sen opastus erottaa myös tuotteiden uudelleenkäytön jätteiden kierrätyksestä. **INFERENCE:** yleinen uusi ilmoitusalusta ei ole tässä perusteltu. Julkinen ilmoitus ei myöskään ole todiste säästöstä tai meidän palkkiostamme. [Motiva](https://www.motiva.fi/tietopankki/materiaalitori-maksuton-markkinapaikka-kiertotalouden-tekijoille/), [Materiaalitorin opastus](https://info-materiaalitori.fi/materiaalihaku/uusiokaytto-ja-kierratys/)

| Generaattorin kysymys | Vastaus |
|---|---|
| Maksaja | HYPOTHESIS: luovuttaja vältetystä kustannuksesta tai käyttäjä hankinnan säästöstä; valittava yksi todellinen maksaja |
| Nykyinen vastaanottaja | Nykyinen käsittely-/logistiikkatoimija tai neitseellisen materiaalin toimittaja |
| Este | Laadun epävarmuus, toimitusrytmi, kuljetus, sääntely ja vastuu |
| Niukka resurssi | Käyttäjän hyväksymä erittely sekä todennettu eräkohtainen vastaavuus |
| Laillinen hankinta | Haltijan lupa tiedolle ja tarvittaessa näytteelle; roolin ja aineen luokituksen tarkistus ennen kauppaa |
| Meidän korvaus | UNKNOWN: hyväksytyn korvaavuuden selvitysmaksu tai sopimukseen perustuva välitysosuus |
| Kasautuminen | HYPOTHESIS: kelpoisuusmatriisi nopeuttaa seuraavaa samanlaista erää ja käyttäjää |
| Vahvin vastaväite | Jokainen erä vaatii uuden laboratorionäytön. Kuljetus tai vastuu syö hyödyn. Osapuolet jatkavat suoraan |

**CALCULATION, symbolinen:** yhteinen enimmäissäästö = vältetty käsittely + vältetty vaihtoehtoinen hankinta − lisäkuljetus − testaus − käsittelymuutos − lisäriski. Meidän liikevaihtomme on tästä vain erikseen sovittu osuus. Kielteinen yhteissäästö tappaa tapauksen ennen palkkiokeskustelua.

**Kevyt generaattori:** yksi materiaaliluokka, rajattu etäisyys ja käyttäjän tarkka kelpoisuuserittely. Tuota mahdollinen pari ja puuttuvat kentät. Älä koskaan päättele kelpoisuutta pelkästä materiaalinimestä. Tässä ei haettu tai vahvistettu yhtään toteuttamiskelpoista kaupallista paria. Julkinen markkinapaikka oli havainto mekanismin infrastruktuurista.

**Päätös:** fyysisen toiminnan rahoittamista ei jatketa tällä budjetilla. Paperilla tehtävä yhden korvaavuuden arvio voisi olla pieni koe jos valmiit mittaustiedot saadaan luvalla. Ilman niitä lisähaku antaa lisää ilmoituksia mutta ei ratkaise toteutuskelpoisuutta.

## 6. Kolmen mekanismin yhteinen red team

**INFERENCE:** kaikissa on sama vaara: voimme luoda suurta yhteistä hyötyä ja silti saada vain pienen kertamaksun. Kysyntälista voidaan ohittaa, testikirjasto kopioida ja materiaalipari ottaa suoraan haltuun. Pelkkä kontaktiverkosto ei ole omistettu rahavirta.

**HYPOTHESIS:** vahvempi yhdistelmä on toistuva yhteensopivuusongelma + hyväksytty näyttö + lupa käyttää samaa ratkaisua uudelleen + jakelureitti samanlaisiin ongelmiin. Jokainen komponentti pitää osoittaa erikseen. Yksinoikeutta ei tarvita ensimmäiseen tuloon mutta ilman toistuvaa hyötyä talous palautuu palvelutyöksi.

**Vastaväite tähänkin:** jos yhteensopivuus on riittävän standardi uudelleenkäyttöön, sen automatisoi myös nykyinen toimittaja. Mahdollisuusalue on kapea: tarpeeksi yhteistä uudelleenkäyttöön, tarpeeksi paikallista ja muuttuvaa ettei yleinen ratkaisu poista kaikkea arvoa. Tämä on HYPOTHESIS, ei löydetty markkinarako.

## 7. Konkreettinen ensimmäinen koe: syntyykö ensimmäisestä tapauksesta etua seuraavaan?

Valinta on **informaation arvoon perustuva INFERENCE**, ei väite parhaasta liiketoiminnasta. Näyttövarannon testi erottaa kasautumisen kertatyöstä ja soveltuu myöhemmin useaan haaraan.

**Hypoteesi H:** luvallisesti säilytettävät, hyväksytyistä tapauksista muodostetut testit parantavat uusien saman perheen tapausten ratkaisemista samalla AI:lla ilman vastaavaa ihmistyön kasvua.

**Tarvittava lähtöaineisto:** yksi organisaation omistama, henkilötiedoton offline-yhteensopivuusongelma, nykyinen ratkaisu, todellinen kustannusperuste ja erillinen saman perheen uusi tapaus. Aineiston haltijan täytyy sallia käyttö. Tämän vuoron julkisessa aineistossa ei ollut tällaista ostajan hyväksymää kokonaisuutta. omistaja voi toimittaa jo luvallisen aineiston; vaihtoehto on hänen erikseen hyväksymänsä yhteydenotto. Kokeen tutkimusversio ei lupaa tulosta tai tarjoa tuotantopalvelua.

**Suunnitelma, ei vielä ajettu:**

1. Lukitse ostajan hyväksymä oikeellisuuskriteeri ja nykyinen vertailuratkaisu ennen omia tuloksia. Nimeä kriittiset virheet. Älä rakenna arvioijaa vain oman ratkaisun vahvuuksille.
2. Erota ajallisesti vanhat kehitystapaukset ja aidosti uudet testit. Deduplikoi. Jos riippumattomia tapauksia ei ole, tulos on vain demo.
3. Tee ensimmäisistä tapauksista geneerinen testivaranto ilman asiakkaan salaisuuksia. Kirjaa tähän käytetty aika.
4. Vertaa uusiin tapauksiin A: sama AI ilman varantoa ja B: sama AI varannon kanssa. Pidä malli, kokonaisresurssiraja ja hyväksymisohje samoina. Vaihtele suoritusjärjestystä ja arvioi tuotokset sokkona jos aineisto sen sallii.
5. Mittaa hyväksytyt tulokset, kriittiset virheet, ihmisen minuutit, laskennan kustannus ja varannon huolto. Kirjaa myös A:n etu jos sellainen löytyy. Ei valikoituja parhaita ajoja.
6. Tarkista erikseen että geneeristä varantoa saa käyttää toisen asiakkaan yhteydessä. Anonymisointi ei yksin ratkaise sopimus- tai liikesalaisuusoikeuksia.
7. Vasta teknisen näytön jälkeen selvitetään halukkuus maksaa. Mitattu säästö ei ole meidän tuloamme. Mahdollinen kaupallinen jatko tarvitsee uuden nimenomaisen hyväksynnän.

**Ehdotetut ennakkorajat, eivät datasta johdettuja:** käteiskulu 0 €, työ enintään yksi rajattu työpäivä. Hyväksymisrajan läpäisy ilman kriittisiä virheitä ja vähintään 25 % pienempi ihmistyö B:ssä molemmissa kahdessa peräkkäisessä uudessa testierässä. Testierien vähimmäiskoko ja mielekäs 25 % -raja on vahvistettava aineiston haltijan kanssa ennen ajoa. Pienestä otoksesta ei tehdä tilastollista yleistystä.

**Tapporaja:** vertailu on yhtä hyvä, kriittinen virhe jää huomaamatta, varantoa ei voi käyttää uudelleen tai jokainen uusi tapaus vaatii yhtä paljon käsityötä. Yksi epäonnistuminen tappaa tämän toteutuksen tämän testin perusteella, ei yleistä palautteen arvoa koskevaa teoriaa.

**Mitä opitaan:** onnistuminen tukee teknistä uudelleenkäyttöä. Epäonnistuminen erottaa aineiston heikkouden, standardityökalun riittävyyden ja asiakaskohtaisuuden jos loki on kunnollinen. Kumpikaan tulos ei yksin osoita kysyntää, maksuhalukkuutta tai 10 miljoonan skaalaa.

**1 000 €:** en suosittele maksullista koetta ennen tämän ilmaisen portin läpäisyä. Lähteet eivät vielä osoita tiettyä ostettavaa mittausta joka ratkaisisi epävarmuuden paremmin kuin luvallinen olemassa oleva aineisto. Rahaa ei käytetä vain siksi että budjetti on olemassa.

## 8. Miksi tähän kierrokseen syntyy pysäytysportti

**FACT:** Repo- ja lähdetutkimus, proxy-otos, laskelmat ja testisuunnitelma tehtiin. Ulkopuolisille ei lähetetty viestejä, uusia taloudellisia palveluja ei avattu, sopimuksia ei tehty eikä maksuja toteutettu.

**INFERENCE:** Valittujen jatkohypoteesien seuraava erottava havainto koskee ostajan oikeaa aineistoa, hyväksyntää tai maksuhalukkuutta. Sitä ei voi korvata uusilla yleisillä markkinakuvauksilla. Tämä on näiden haarojen lupaan tai luvalliseen aineistoon liittyvä portti, ei väite että julkinen tieto tai koko tutkimusavaruus olisi käytetty loppuun.

omistajan seuraava konkreettinen päätös voi olla yhden yllä kuvatun henkilötiedottoman aineiston luovuttaminen tai rajatun tiedustelun hyväksyminen. En pyydä ostamaan omaisuutta tai sitoutumaan palveluun. En ole valinnut todistetusti voittavaa mekanismia: olen erottanut mekanismin teknisen, kaupallisen ja kasautumista koskevan testin toisistaan.
