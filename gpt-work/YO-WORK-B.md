# Yövuoro B: vanhojen haarojen falsifiointi

2026-09-15 · GPT Work · tutkimus ja porttipäätökset, ei toteutettu liiketoiminta.

Luokitus: **FACT** = lähteessä havaittu asia, jonka rajoitus kerrotaan; **CALCULATION** = nimetyistä syötteistä laskettu; **INFERENCE** = päätelmä; **HYPOTHESIS** = koeteltava väite; **UNKNOWN** = ratkaisematta. Toimittajan oma ilmoitus on fakta ilmoituksen olemassaolosta, ei riippumattomasti varmennettu tulos. NO-GO tarkoittaa tässä tutkimusmuodon hylkäystä projektin seuraavana toteutuksena.

## 1. Orpo digitaalinen omaisuus

### Taloudellinen hyökkäys

**INFERENCE:** Jos AI poistaa aidosti ylläpidon kustannuksen, se nostaa myös nykyisen omistajan jatkamisoption arvoa. Meille siirtyy etua vain jos omistajalla on eri vaihtoehtoiskustannus, rajoite, tavoite tai kyky kuin meillä. ”Hän ei ehdi koodata” on heikko selitys maailmassa jossa koodaus on lähes ilmaista. ”Hän ei enää halua kantaa vastuuta ja meillä on halvempi yhteinen infrastruktuuri” on parempi mutta vaarallinen: vastuu voi olla juuri omaisuuden negatiivinen arvo.

Ylläpito = koodi + infrastruktuuri/API + tietoturva + asiakastuki + jakelun säilyttäminen + alustaehtojen noudattaminen + virheiden seuraukset. **HYPOTHESIS:** AI laskee näistä vain osaa ratkaisevasti. Kustannuksia ei tässä mitattu yhdestäkään ostettavasta kohteesta.

**CALCULATION, symbolinen:** ostajan enimmäishinta on odotettujen nettokassavirtojen nykyarvo vähennettynä siirrolla ja vastuiden hinnalla. Kauppa on mahdollinen vain jos tämä ylittää myyjän luopumishinnan. AI:n yhteinen kustannussäästö voi nostaa molempia eikä siksi takaa ostajan ylijäämää. Tätä identiteettiä ei pidä naamioida kohteen arvonmääritykseksi ilman kassavirtadataa.

### Tehty 0 € lukukoe

**FACT:** GitHub-haku `topic:chrome-extension stars:>1000 archived:false pushed:<2024-09-16`, ensimmäiset 10 palautettua osumaa, oletusjärjestys. Luin kaikkien kymmenen README:n. Otos ei ole satunnainen. Luokittelu syntyi lukemisen aikana eikä ole ennakkorekisteröity testi. Tarkoitus oli koetella väitettä että tämä haku löytää hylättyä käyttäjäjakelua. Hakutyökalun vastaus ei näyttänyt kokonaismäärää, joten alkuperäisiä kymmenien tuhansien lukuja ei varmennettu.

| Osuma | README-havainto | Tulkinta |
|---|---|---|
| wong2/chatgpt-google-extension | Päivitykset lopetettu yrityskaupan takia | Dokumentoitu vaihtoehtoinen selitys: yrityskauppa |
| interstellard/chatgpt-advanced | Julkinen päivitys päättynyt, uudet toiminnot tarvitsevat taustapalvelun/tunnisteita | Dokumentoitu vaihtoehtoinen selitys: kehitys ei kokonaan julkista |
| EmailThis/extension-boilerplate | Laajennuksen rakentamisen pohja | Ei oma kuluttajatuote käyttäjäkantana |
| stefanbuck/awesome-browser-extensions-for-github | Linkkikokoelma | Ei oma asennettu käyttäjäkanta |
| alyssaxuu/omni | Tuote ja tukimahdollisuus näkyvät | UNKNOWN: ei näyttöä kaupasta tai siirtyvästä tulosta |
| hcfyapp/crx-selection-translate | Tuotteen sivu- ja tukilinkit | UNKNOWN |
| bilibili-helper/bilibili-helper-o | Laajennusprojekti | UNKNOWN |
| tulios/json-viewer | Laajennusprojekti | UNKNOWN |
| uku/Unblock-Youku | Laajennus ja palveluriippuvuuksia | UNKNOWN |
| EdgeTranslate/EdgeTranslate | Tuote ja vapaaehtoinen tuki | UNKNOWN |

**CALCULATION:** 2/10 osumaa ei ollut oma asennettu tuote. Kahdessa muussa README dokumentoi vaihtoehtoisen historiallisen syyn julkisen kehityksen päättymiselle. Niiden nykyistä aktiivisuutta tai myöhempää hylkäämistä ei tarkistettu. Neljä osumaa siis torjuu suoran proxy-päättelyn, ei todista neljää nykyään aktiivista tai myyntikelvotonta tuotetta. Kuusi muuta eivät ole kuusi mahdollisuutta vaan kuusi selvittämätöntä. Ei populaatioestimaattia, luottamusväliä tai ennustetta. Havainto ei todista ettei ensimmäinen tuote voisi joskus tulla uudelleen myyntiin. Se todistaa että sen repo-hiljaisuus ei yksin osoita hylkäämistä.

Lähdepolut ja README-blobien SHA:t: [data/orphan-proxy-audit.json](data/orphan-proxy-audit.json). Kaksi suoraa vastaesimerkkiä: [yrityskauppa](https://github.com/wong2/chatgpt-google-extension/blob/main/README.md), [julkisen kehityksen rajaus](https://github.com/interstellard/chatgpt-advanced/blob/main/README.md).

### Siirtyykö niukka resurssi?

**FACT:** Chrome Web Storen virallinen ohje sisältää menettelyn kohteen siirtämiseksi toiselle kehittäjälle. Tämä vahvistaa teknisen siirtoreitin olemassaolon. Se ei vahvista myyjän halukkuutta, hintaa, käyttäjien pysyvyyttä tai oikeutta vaihtaa tuotteen tarkoitusta. [Chrome](https://developer.chrome.com/docs/webstore/register)

**FACT:** Google Play kuvaa käyttäjien, lataustilastojen, arvostelujen ja tilausten siirtymistä sovellussiirrossa sekä erillisiä raportointi- ja integraatiotöitä. Tätä ei saa yleistää sellaisenaan Chromeen. [Google Play](https://support.google.com/googleplay/android-developer/answer/6230247?hl=en)

**FACT:** Chromen käyttäjädataehdot rajoittavat tietojen käyttöä ja siirtoa. Yrityskauppa ei anna yleistä oikeutta myydä käyttäjien selaustietoja tai hyödyntää niitä vapaasti toiseen tarkoitukseen. **INFERENCE:** kymmenen tuotteen käyttäjälukuja ei voi summata tavoitettavaksi myyntikanavaksi ilman aktiivisuutta, päällekkäisyyksiä, käyttötarkoitusta ja lupia koskevaa näyttöä. [Chrome user data](https://developer.chrome.com/docs/webstore/program-policies/user-data-faq)

### Parempi versio

**HYPOTHESIS:** Älä osta yleisöä. Ratkaise sama kallis yhteensopivuus- tai turvallisuusongelma usealle organisaatiolle, joiden vanha riippuvuus on jo käytössä. Yksi hyväksytty korjaus voi palvella useaa maksajaa. Kasautuva varanto on testit, korjaukset ja näyttö yhteensopivuudesta. Ostettava omistus ei ole välttämätön lähtökohta.

**FACT:** HeroDevs myy kaupallista tukea elinkaarensa päättäneille avoimen lähdekoodin riippuvuuksille. **INFERENCE:** mekanismi on siis jo kaupallinen eikä tyhjä markkina. Yhden henkilön ympärivuorokautinen vastuu olisi heikko lähtökohta. Ensimmäisen kokeen pitäisi rajautua offline-yhteensopivuusnäyttöön ilman tuotantotakuuta. [HeroDevs](https://www.herodevs.com/)

**Portti:** yleinen tähtiin perustuva ostoskanneri NO-GO. Kohdekohtainen tutkimus jatkuu vain jos julkisesti tai luvallisesti voidaan osoittaa aktiivinen kysyntä, siirtokelpoisuus, kokonaiskulut ja omistajan todellinen luopumisperuste. Tässä otoksessa yhtään tällaista tapausta ei vahvistettu. Omistajakontakteja ei tehty.

## 2. Jo tarkastettujen maksujen jälkitarkastus

### Vahvin vastanäyttö hylkäämiselle

**FACT, myyjän tapauskuvaus:** PRGX raportoi 1.7.2026 julkaistussa päivittäistavaratukun tapauksessa 11,3 miljoonan dollarin lisäpalautuksia 24 miljardin dollarin tarkastetusta kulutuksesta 12 kuukaudessa ensimmäisen auditoijan jälkeen. Asiakasta ei nimetä. Tulosta ei saatu riippumattomasti varmennettua. Tämä on riittävä syy olla väittämättä että toinen kierros olisi aina tyhjä. [PRGX case](https://www.prgx.com/case-study/2nd-pass-audit-recovers-11m-grocery-distributor/)

**CALCULATION:** 11,3m / 24 000m = 0,0470833 %. Jos täysin hypoteettisesti sama osuus löytyisi pienemmältä asiakkaalta ja palkkio olisi 25 %, miljoonan euron tarkastettu volyymi tuottaisi 117,71 € liikevaihtoa. Kuuden tunnin työn laskennallinen kustannus 50 €/h olisi 300 €. Nollakatteen volyymi tällä lelulaskelmalla olisi noin 2,55m €. Ei ennuste: toimiala, sopimukset, tarkastuksen rajaus, valuutta, palkkio ja löydösten jakauma eivät siirry tällä jakolaskulla pk-yrityksiin. Myös myynti, aineiston puhdistus ja riitautukset puuttuvat.

**FACT:** PRGX kertoo käyttävänsä AI:ta ja ihmisten validointia. Sen FAQ kuvaa toteutuneeseen palautukseen sidottua palkkiota ja kuukausia kestävää prosessia. **INFERENCE:** AI:n käyttö tai success fee ei yksin erota meitä nykyisestä vastaanottajasta. [PRGX AI](https://www.prgx.com/expertise-powered-by-ai/), [FAQ](https://www.prgx.com/resources/faqs/)

### Ensimmäinen pullonkaula

**UNKNOWN:** Saammeko yhden riittävän aineiston, sopimusperusteen löydölle ja hyväksytyn palautuksen pienemmällä kokonaiskustannuksella kuin asiakas tai nykyinen tarkastaja? Pelkkä laskurivien poikkeama ei ole saatava.

**HYPOTHESIS:** Kasautuva etu voisi syntyä toimialakohtaisesta hyväksymis- ja hylkäysperusteiden varannosta, jota saa laillisesti käyttää uudelleen sekä kanavasta joka tuo samanmuotoista aineistoa. Portfolion jokainen onnistuminen voi parantaa tarkkuutta ja vähentää käsittelyä seuraavalle asiakkaalle. Yleinen räätälöity analyysi ei vielä tee tätä.

**Vahvin vastaväite:** löydökset ovat asiakaskohtaisia ja luottamuksellisia. Myyjäkohtainen suhde ratkaisee enemmän kuin malli. Yksi palautus ei saa tuottaa kannustetta perusteettomiin vaatimuksiin.

**Päätös:** yleinen toinen AI-tarkastus NO-GO kasautumistarinalle. Rajattu toistuva virheluokka jatkohypoteesina. Seuraava oikea testi vaatii luvallisen historiallisen aineiston ja tietoa jo ratkaistuista hyväksynnöistä. Ei satunnaisen synteettisen laskuaineiston demoa markkinanäytöksi.

## 3. Hankinta yhdistettynä todelliseen toimituskykyyn

**FACT:** Julkisten hankintojen neuvontayksikön ohje sallii ryhmittymän ja muiden voimavaroihin tukeutumisen mutta edellyttää niiden tosiasiallista käytettävyyttä. Ammatilliseen kokemukseen nojaavan toimijan on suoritettava vastaava osuus. Ohjeessa kuvataan myös tapauskohtaisia näyttö- ja vastuukysymyksiä. **Rajaus:** ohjeen mainitsemia tuomioistuinratkaisuja ei tässä saatu kokonaisina tarkastettavaksi Finlexistä. [Hankinnat.fi](https://www.hankinnat.fi/eu-hankinta/ehdokkaiden-ja-tarjoajien-soveltuvuus/tarjouskilpailuun-osallistuminen-ryhmittymana-ja)

**INFERENCE:** AI:n kirjoittama tarjous ei luo toimituskapasiteettia tai tee kumppanin referenssistä meidän omaisuuttamme. Jos toimittaja tekee kaiken olennaisen, se voi seuraavassa kilpailussa ohittaa meidät. Jos me kannamme sopimusvastuun, 1 000 € voi olla väärä riskibudjetti vaikka tarjouksen tekeminen olisi ilmaista.

**HYPOTHESIS:** Kapea toistettava toimituskokonaisuus voi muodostaa kasautuvan kyvykkyyden: todellinen hyväksytty toimitus → yhteiset laadunvarmistusmenetelmät ja näyttö → pienempi seuraava toimitusriski → parempi pääsy. Tämä vaatii meidän oman osuuden olevan tarpeellinen ja taloudellisesti korvattu.

**Vahvin vastaväite:** referenssi parantaa kilpailukelpoisuutta vain tiettyyn rajaan. Sen jälkeen jokainen voitto lisää samassa suhteessa työtä ja vastuuta. Se on kasvava palveluyhtiö, ei vielä positiivinen takaisinkytkentä.

**Päätös:** yleinen tarjouskirjoitus/ryhmittely NO-GO. En rakenna 30 ilmoituksen skanneria ennen tietoa yhdestä aidosta toimitusmallista, kustannuksista, vastuunkantajasta ja kumppanin halusta maksaa koordinaatiosta. Nämä tiedot vaativat luvallisen kumppaniaineiston tai hyväksytyn yhteydenoton. Tarjouksia ei jätetty.

## 4. Olemassa olevan jouston saattaminen reservimarkkinoille

**FACT:** Fingridin ohjeessa markkinoille osallistumiseen kuuluu tuotekohtainen tekninen kelpoisuus, tietoliikenne, sopimukset ja operatiivisia velvoitteita. Minimitarjous on tuotteesta riippuen 0,1 tai 1 MW. Aggregointi ja palveluntarjoajat mahdollistavat pienempien resurssien yhdistämistä. Sopimuksen maksuttomuus ei tarkoita toiminnan kustannuksettomuutta. [Fingrid](https://www.fingrid.fi/sahkomarkkinat/reservit/reservimarkkinat/)

**FACT:** Fingridin toimijaluettelossa on jo useita aggregointi- ja muita palveluja tarjoavia yrityksiä. Luettelon BSP-osa oli päivitetty 27.8.2026 ja palveluntarjoajaosa 21.8.2026. **INFERENCE:** markkinapääsyn myyminen ei ole tyhjä välittäjärooli. [Toimijaluettelo](https://www.fingrid.fi/globalassets/dokumentit/fi/sahkomarkkinat/reservit/reservimarkkinatoimijat.pdf)

**UNKNOWN:** Maksaisiko nykyinen aggregaattori meille toistuvaa osuutta ja mistä lisäarvosta? Jääkö asiakassopimus meille? Kuka maksaa liitynnän? Miten osuus käyttäytyy asiakkaan vaihtaessa toimijaa? Julkinen tuottopotentiaali ei vastaa näihin.

**HYPOTHESIS:** Yhden laitetyypin valmis integraatio ja käyttökelpoisuuden ennustaminen voisi laskea seuraavan kohteen aktivoinnin kustannusta. Toistuva oikeus osaan kassavirrasta voisi muodostaa portfolion. Kumpaakaan ei syntyisi pelkästä yhteystiedon välityksestä.

**Vahvin vastaväite:** integraation ja operoinnin omistava aggregaattori saa suurimman edun. Meidän portfolio-oikeutemme on neuvoteltava eikä seuraa resurssin löytämisestä. Kiinteä prosenttiosuuskaan ei yksin tee seuraavaa kohdetta halvemmaksi hankkia.

**Päätös:** oma BSP-toiminta ei saa toteutussuositusta tällä pääomalla ja näytöllä. Kertapalkkiovälitys NO-GO kasautumishypoteesina. Seuraava portti olisi nykyisen toimijan kirjallinen kaupallinen malli ilman sitoutumista. Sitä ei hankittu, koska yhteydenotto vaatii omistajan luvan. Hintasarjojen lisäanalyysi ei ratkaise tätä pullonkaulaa.

## 5. Mitä oikeastaan pitäisi kasautua?

**HYPOTHESIS, malli:** S(t+1) = (1 − d) S(t) + g(onnistuminen). S on laillisesti säilyvä ja uudelleen käytettävä varanto, d sen vanheneminen. Tämä ei ole estimoitu malli. Se pakottaa nimeämään varannon ja testaamaan, muuttaako se seuraavan tapauksen kustannusta, laatua tai neuvotteluasemaa. Myös huolto- ja vastuuvelka pitää vähentää.

| Mahdollinen varanto | Todiste kasautumisesta | Helppo väärä positiivinen |
|---|---|---|
| Hyväksytyt virhe- ja testitapaukset | Samalla AI:lla varannon kanssa parempi sokkotulos uusissa tapauksissa | Lisää talletettua dataa ilman laatuhyötyä |
| Referenssit | Muuten suljettu tarjous tai asiakkaan luottamus avautuu | Tyytyväisyyslausunto joka ei muuta ostoa |
| Sopimukset | Jatkuva korvaus säilyy ja seuraavan hankinnan kustannus laskee | Jokainen uusi asiakas vaatii yhtä paljon työtä |
| Käyttäjät/jakelu | Uuden hyväksytyn tuotteen hankinta halpenee todellisella konversiolla | Lataukset tai GitHub-tähdet |
| Kapasiteettiverkosto | Uusi jäsen parantaa olemassa olevien toteutumisastetta | Yhteystietolista ilman käytettävyyttä |
| Pääoma | Mahdollistaa uuden aiemmin suljetun mittakaavan tai ehdon | Raha käytetään vain useampiin työtunteihin |

**INFERENCE:** Kymmenen miljoonan arvostus ei seuraa liikevaihdosta tai käyttäjäluvusta ilman omistusta, katetta, jatkuvuutta ja ostajaa. En laske tavoitearvoa kuvitteellisella kerroinluvulla.

## 6. Kierrosten jatkamisloki

Jokaisessa rivissä vastataan seitsemään jatkokysymykseen. Tämä kirjaa toteutuneen suunnanmuutoksen, ei väitä kaikkien haarojen ratkenneen.

| Löytö | Seuraus | Yleinen mekanismi / muu esiintymä | Vahvin vastaväite | Ratkaiseva data | Aiemmin kysymättä / seuraava arvokkain kysymys |
|---|---|---|---|---|---|
| Yhteinen niukkuusohje | Konvergenssin todistusvoima alas | Yhteinen kehys / sijoitusnarratiivit | Itsenäinen päättely voi silti olla oikea | Ennen kontaktia versioidut väitteet + ulkoinen näyttö | Miten erotamme mallien yhteisen vinouman? Siirry havaintoihin |
| 2 ei-tuotetta + 2 vaihtoehtoista selitystä / 10 | Ei laajaa orphan-skanneria | Välillisen mittarin sekoittuminen / kuolleet verkkosivut | Parempi haku voi toimia | Aktiivisuus, myyntihalu, kulut, siirtoreitti | Mikä omistajan luopumisen syy kestää halvan AI:n? |
| Alustasiirto mahdollinen | Ei kategorista siirtoestettä | Tekninen oikeus ≠ taloudellinen säilyvyys / sovelluskaupat | Retentio voi olla hyvä | Kohteen ennen/jälkeen käyttökohortit | Kuka voi käyttää käyttäjädataa mihinkin? |
| Toinen auditoija löytää lisää | Jälkiauditointia ei tapeta kokonaan | Eri havaintojoukot / laadunvalvonta | Myyjän valikoitu menestystarina | Luvallinen holdout ja hyväksymisnäyttö | Parantaako löydöskanta seuraavaa asiakasta vai vain samaa? |
| Hankinta vaatii oikeaa kapasiteettia | Paperikoordinaatio alas | Kelpoisuus sidottu suoritukseen / sertifioitu toimitus | Koordinaatio voi olla itsessään arvokasta | Kumppanin kustannus ja meidän välttämätön osuus | Miksi kumppani ei ohita meitä seuraavaksi? |
| Reservivälittäjiä jo paljon | Ei uutta skanneria | Portinvartijan neuvotteluvoima / rahoituksen jakelijat | Erikoiskanava voi olla arvokas | Ei-sitova ansaintamalli ja integraatiokulut | Kenelle ensimmäinen asiakassuhde oikeasti jää? |
| AI voi tuottaa uuden todennetun ratkaisun | Omistuksen lisäksi endogeeninen tieto | Kokeellinen palaute / teollinen optimointi | Asiakas omistaa tuloksen tai kopioi | Historiavarannon ablaatio samalla mallilla | Voiko hyväksyttävä näyttö siirtyä seuraavaan tapaukseen? |
| Ilmainen materiaalimarkkinapaikka jo olemassa | Pelkkä matching alas | Ilmoitus ≠ toteutuskelpoisuus / yhteiset tuotantoerät | Laboratorio ja logistiikka syövät edun | Eritelty laatu, etäisyys ja vältetty kustannus | Voiko hyväksytty korvaavuus toistua ilman fyysistä vastuuta? |

Avoin kierros ja konkreettinen seuraava testiprotokolla: [UUDET-MEKANISMIT.md](UUDET-MEKANISMIT.md). Lähteet tarkastettu tämän vuoron aikana 15.9.2026. Tuntemattomia ei korvata lisäpisteillä.
