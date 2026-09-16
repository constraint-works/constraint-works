# Teorian tuhoamisyritys ja Structural Test v2

2026-09-16 · GPT Work · Ei uusia mahdollisuusideoita tai toteutettuja kokeita.

**Arvioitu versio:** [318155c57687c344cb1494ae1124bd8c48b0d399](https://github.com/original-private-account/eikaisiina/commit/318155c57687c344cb1494ae1124bd8c48b0d399). Luettu kokonaan `etsinta/SUUREN-VIPUVAIKUTUKSEN-TEORIA.md` (478 riviä), `PROSESSI.md` ja `kirjanpito/paatokset.md`. Tarkastettu commitin muutokset sekä teorian käyttämää aiempaa aineistoa. Clauden tiedostoja ei muuteta.

Merkinnät: **FACT** lähdehavainto; **CALCULATION** lasku ilmoitetuista oletuksista; **INFERENCE** päättely; **HYPOTHESIS** testattava väite; **UNKNOWN** ratkaisematon. Lähteen väitteen lukeminen on FACT siitä mitä lähde ilmoittaa. Se ei tee väitteen kausaalisesta tulkinnasta faktaa. Alla olevat rakennetestin tuomiot ovat INFERENCEä ellei toisin merkitty.

## 0. Tuomio ennen korjaamista

**Teoria ei selviä universaalina välttämättömien ehtojen testinä. Sen käyttäminen yhden hylkäävän vastauksen porttina on liian vaarallista.** Se sisältää sekä todellisia havaintoja että jälkikäteen sovitettuja määritelmiä. Se sekoittaa kolme eri tavoitetta:

1. suuren yrityksen tai henkilökohtaisen varallisuuden syntyminen
2. aiempien kierrosten aiheuttama taloudellinen kasautuminen
3. nimenomaan AI:n aiheuttama vipuvaikutus meidän lähtöresursseillamme.

Yhden todistaminen ei todista muita. Kasvava liikevaihto ei ole kasvava omistusvarallisuus. AI:n käyttäminen ei osoita AI:n aiheuttaneen kasvua. Suuri yritys ei osoita että se oli käynnistettävissä 1 000 eurolla.

Vahvimmin säilyy rajattu väite: **jos kierros N aiheuttaa kierroksen N+1 paremman talouden samoilla ulkoisilla ehdoilla, vaikutuksen täytyy välittyä jonkin säilyvän tilan kautta.** En löytänyt tästä vahvaa toistettavaa vastaesimerkkiä. Tämä on osittain kausaalisen muistin määritelmä eikä vielä empiirinen talousteoria. Clauden P1–P5-paketti ei seuraa siitä.

## 1. Johtamisen auditointi: mitä todella mitattiin?

### 1.1 Kuusi ratkaisevaa evidenssihyppyä

| Teorian kohta | Havainto | Johtamisen ongelma |
|---|---|---|
| §0/1a: osallistumisen ilmaisuus painaa hinnan tokenikustannukseen | Repo kertoo auditointikilpailun 3 000 USD potista ja 116 palautuksesta | **CALCULATION:** 3 000 / 116 ≈ 25,86 USD. Tämä on potin jakolasku eikä suoritteesta maksettu hinta. Tokenikulujen jakaumaa, osallistujien laatua tai tasapainohintaa ei mitattu. Kolmen kilpailun koko aineistossa vastaava luku on 11 500 / 355 ≈ 32,39 USD. Kumpikaan ei ole meidän odotusarvomme |
| §0/1b: markkinavirhettä ei ole siellä missä on markkina | Micronsin pyyntihinnat ja tulomultiple | Pyyntihinta ei ole toteutunut kauppa. Listaus ei todista tehokkuutta tai poista informaatioeroja. Se voi kumota tietyn halpuusoletuksen |
| §0/1c: vastuu oli kustannus, koodi ei | Yhden kirjaston korjaus ja ylläpitäjien julkisia keskusteluja | Ei ylläpitotyön ja vastuun kustannusten interventiota. Julkaisematta jättäminen ei paljasta omistajan vaihtohintaa. Oma pieni wheel-koe ei osoita kaikkien käyttäjien korjausarvon olevan nolla |
| §7: HeroDevs on 125 M USD:n yhtiö; ihmistyö kasvaa lineaarisesti; kontti tekee arvosta epälineaarisen | Julkinen rahoitustiedote | **FACT:** 125 M USD on kasvurahoituksen määrä. Ei tiedotteen ilmoittama yritysarvo, liikevaihto tai perustajan lunastus. Ihmistyön skaalauslakia ja kannattavuutta se ei mittaa [S1–S2] |
| §1e: jokaisessa tapauksessa alusta voitti | Näkyviä alustoja ja osallistujien vaikeuksia | Alustojen tulosta tai pääoman tuottoa ei ole mitattu. Osallistujan heikko tulos ei todista alustan voittoa. Verkko ei myöskään ole ainoa tapa jakaa kiinteä kustannus monelle käyttökerralle |
| §8–9: häntävedot ovat yleisin 1 000 → 10 M -reitti; pääoma ei ollut rajoite | Ei kattavaa lähtöjoukkoa tai toteutuneita polkuja | **UNKNOWN:** yleisyys ja kausaalinen pääomarajoite. Nämä eivät seuraa negatiivisten hakutulosten otoksesta |

HeroDevsin luku varmennettiin sekä yhtiön tiedotteesta että sijoittajan hakutuloksesta. Sijoittajan sivun suora avaus palautti 403:n. Kyse on saman kaupan osapuolten ilmoituksesta eikä kahdesta riippumattomasta arvonmäärityksestä. Rahoitusmäärän luonne on silti yksiselitteinen. [HeroDevs S1](https://www.herodevs.com/blog-posts/herodevs-announces-125-million-strategic-growth-investment-from-psg), [PSG S2](https://psgequity.com/news/herodevs-announces-125-million-strategic-growth-investment-from-psg).

**CALCULATION:** `10 M€ / 1 000 € = 10 000` on kahden varallisuussumman suhde. Siitä ei seuraa että tuntihinnan pitäisi nousta 10 000-kertaiseksi. Vertailussa puuttuvat aika, työtulojen säästäminen ja muut panokset. Samoin yritysarvo `E = m × tulos` on tuloksen suhteen lineaarinen kun kerroin m on vakio. Yrityksen perustaminen ei itsessään tee arvosta epälineaarista.

### 1.2 Onko tämä jälkikäteen rakennettu teoria?

**INFERENCE: kyllä, siinä on selviä ylisovittamisen tunnusmerkkejä.** Tämä ei tarkoita että kaikki sen ajatukset olisivat vääriä.

- Samat valikoidut tapaukset sekä muodostavat ehdot että vahvistavat ne. Omaa N → N+1-koetta ei ole.
- HeroDevs pakottaa HUMAN-poikkeuksen ja OSS viivästetyn CAPTURE-poikkeuksen. Poikkeusten tekeminen on järkevää hypoteesityötä mutta niiden jälkeen tarvitaan uusia testitapauksia.
- Oma julkinen loki saa ei-kopioitavan tilan statuksen ilman mitattua yleisöä. Julkinen testiaineisto taas hylätään kopioitavana. Tekijyyden todennettava historia voi erota kopioitavasta sisällöstä mutta sen taloudellinen vaikutus on vielä UNKNOWN.
- P1–P5 hylkäävät tavallisia sopimuksia. §7 hyväksyy samat asiakassopimukset HeroDevsin tilaksi. Luokittelu vaihtuu esimerkin menestyksen mukana.
- Prosessin vanha kysymys oli ”ihminen tekisi saman yhtä hyvin”. Päätösloki kuvaa sen muotoon ”mahdotonta ilman tekoälyä”. Ne eivät ole sama ehto. Lisäksi `ai_etu`-pisteytyksessä ”5 = mahdotonta ilman” jäi voimaan. Prosessi on sisäisesti ristiriitainen.
- ”Kolme UNKNOWNia peräkkäin” riippuu kysymysten järjestyksestä. Tiedon määrä ei muutu rivejä siirtämällä.

**Menetelmällinen raja:** seuraavat historialliset stressitapaukset on valittu nimenomaan vaikeiksi vastaesimerkeiksi. Nekään eivät ole satunnainen otos. Niillä voi osoittaa väärän hylkäyksen mutta ei mitata testin yleistä tarkkuutta tai uuden yrityksen onnistumistodennäköisyyttä.

## 2. Kuusi lopullista ehtoa erikseen (§9.1)

### E1. Edun pitää nojata johonkin jonka baseline ei laske mallien parantuessa

**Johtaminen:** havaittu kilpailu ja ilmaiset vaihtoehdot tukevat kilpailuvertailua. Ne eivät osoita ikuisesti mallikehitykseltä suojatun edun välttämättömyyttä.

**Välttämättömyys:** ei. Etu voi uusiutua tai aiempi etu voi tuottaa kassavirtaa ennen rapautumistaan. Myös hinta voi laskea samalla kun määrä ja nettotulos kasvavat. Laki tai yleisö ei takaa hintasuojaa: nekin voivat menettää taloudellisen arvonsa vaikka oikeudellinen asema säilyisi.

**Päällekkäisyys:** SCARCITY, STATE P5 ja CAPTURE käsittelevät samaa kopioinnin tai vaihtamisen vastusta.

**Erottelukyky:** julkiseen ohjelmistoon perustuva toistuva jakelu ja ylläpito voivat jäädä ulos. Hyödytön eksklusiivinen rekisteri voi päästä sisään.

**Falsifioitavuus:** ”jokin jota AI ei laske” ilman aikajännettä ja mittaria voidaan aina pelastaa nimeämällä toteutunut suosio yleisöksi. **Tuomio: KILLED välttämättömänä muuttumattomana suojana.** Kilpailun jälkeisen nettotuoton kestävyys säilyy tutkimuskysymyksenä.

### E2. Kaappausoikeus joka ei siirry asiakkaalle

**Johtaminen:** aineisto tukee vaatimusta erottaa asiakkaan hyöty meidän tulostamme. Se ei osoita että asiakkaan oppiminen tai tiedon siirtyminen lopettaisi toistuvan maksamisen.

**Välttämättömyys:** jokin toteutuva korvaus tarvitaan rahatuloon. Valmis yksinoikeus ja asiakasta huonommassa tietoasemassa pitävä rakenne eivät ole välttämättömiä. Asiakas voi osata asian ja silti ostaa sen työnjaon, ajan tai jatkuvan toimituksen takia.

**Päällekkäisyys:** E4:n kontti on yksi kaappausreitti. ”Sopimus, omistus tai asema” kattaa lähes kaiken laillisen ansainnan jos myös tavallinen yksittäinen ostos lasketaan sopimukseksi.

**Erottelukyky:** tiukka tulkinta hylkää varhaisen ilmaisen tuotteen. Löysä ”kontti joskus myöhemmin” hyväksyy lähes jokaisen yleisötarinan.

**Falsifioitavuus:** vaadi nimetyt kaappauksen vaiheet ja kustannuskatto. **Tuomio: MODIFIED.** Lopullinen arvon saaminen säilyy mutta kaappaus voi syntyä myöhemmin eikä tiedon siirtymistä tarvitse estää.

### E3. Koneen tai yleisön kuluttama säilyvä tila P1–P5

**Johtaminen:** aiemman kierroksen vaikutus tarvitsee välittyvän mekanismin. Aineisto ei johda juuri näitä viittä ominaisuutta. Myyntikustannuksen alenemisen sivuuttaminen on perusteetonta.

**Välttämättömyys:** yleinen kausaalinen tila selviää rajattuun endogeenisen kasautumisen väitteeseen. Ylläpidottomuus, ei-kopioitavuus ja käyttö aina eri asiakkaalla eivät selviä. Ihmisten organisaatio voi olla tilan kantaja.

**Päällekkäisyys:** P2 toistaa HUMANin, P5 SCARCITYn ja P6 FEEDBACKin. P4 on laillisuusraja.

**Erottelukyky:** julkinen toimiva ohjelmisto hylätään ja käyttämätön yksityinen data hyväksytään ennen kausaalista koetta. Hyväksymisasteen nousukaan ei riitä alkuperäiseen h/s-sääntöön vaikka se nostaisi nettotulosta.

**Falsifioitavuus:** nimeä tila ennen tulosta ja poista sen käyttö vastafaktuaalissa. **Tuomio: MODIFIED.** Ydin selviää mutta P1–P5-yhdistelmä ei.

### E4. Kontti josta arvo lunastetaan

**Johtaminen:** omistuksen ja asiakkaan säästön erottelu on tarpeen. Yhtiö ei yksin luo arvoa eikä automaattista kertoimen kasvua.

**Välttämättömyys:** omaan varallisuuteen pitää olla jokin laillinen reitti. Erillinen yritys, alusta tai oikeusportfolio ei ole yleinen välttämättömyys: myös suoraan saatu nettokorvaus kasvattaa varallisuutta. Jos pankkitili hyväksytään kontiksi, ehdosta tulee lähes tautologia.

**Päällekkäisyys:** E2 CAPTURE ja CEILINGin lunastusosa.

**Erottelukyky:** pöytälaatikkoyhtiö läpäisee ilman arvoa. Suuri maksettu tekijänkorvaus voi jäädä ulos jos ”kontti” määritellään liian kapeasti.

**Falsifioitavuus:** jäljitä maksut tai omistusosuus velkojen ja laimentumisen jälkeen. **Tuomio: MODIFIED ja yhdistetään E2:een.** Ei erillistä välttämätöntä ehtoa.

### E5. Positiivinen odotusarvo toistettavasti

**Johtaminen:** yksittäisestä onnistujasta ei voi päätellä oman yrityksen odotusarvoa. Silti tämä on perusteltu projektin valintakriteeri kun tavoite on toistettava ansainta eikä onnekas toteuma.

**Välttämättömyys:** taloudellisesti kestäväksi väitetylle toistettavalle toiminnalle nettotuoton perustelu on tarpeen. Jokaisen kierroksen voitollisuus ei ole. Etupainotteinen investointi voi olla osa kannattavaa polkua.

**Päällekkäisyys:** VALUE, CAPITAL ja CAPTURE syöttävät samaan talouteen. EV ei ole irrallinen viimeinen kyllä/ei-kysymys.

**Erottelukyky:** pelkkä positiivinen EV ei takaa 10 M€:a tai maksukykyä. Tuottojen korrelaatio ja toiminnan loppuminen ennen seuraavaa kierrosta voivat estää toistamisen. Hajautettu toistuva riskinotto ei ole automaattisesti lotto vaikka yksittäiset tulokset olisivat vinoja.

**Falsifioitavuus:** täydet kustannukset, toteutuneet kohortit, rahoitusvaje ja herkkyysraja. Ilman havaintoja EV on UNKNOWN. **Tuomio: SURVIVES tutkimuskriteerinä.** Ei väitetä jo mitatuksi eikä luvata että mikä tahansa positiivinen odotusarvo olisi saavutettava.

### E6. Ei uhkaprofiilia; toiminta julkista ja todennettavaa

**Johtaminen:** haitallisten laajennuskauppojen näyttö tukee tietyn kanavan luottamusongelmaa. Se ei tee julkisuudesta taloudellisen skaalautumisen luonnonlakia.

**Välttämättömyys:** ei. Laillinen yritysten välinen työ voi perustua salassapitoon ja ostajan yksityisesti tekemään tarkistukseen. Alkuperäisen teorian ei-julkinen data on itsekin ristiriidassa ehdottoman julkisuusvaatimuksen kanssa.

**Päällekkäisyys:** laillisuus, luottamus ja pääsy. Epäilyttäväksi tulkitseminen ei ole sama kuin laittomuus tai automaattisesti mahdoton pääsy.

**Erottelukyky:** julkinen hyödytön toiminta läpäisee. Salainen mutta sopimuksellisesti hyväksytty palvelu hylätään.

**Falsifioitavuus:** mitattavissa oleva pääsyn tai hyväksynnän menetys on testattava; ”näyttää uhkalta” ilman vastapuolen havaintoa ei ole. **Tuomio: KILLED universaalina julkisuusvaatimuksena.** Laillisuus säilyy ehdottomana projektirajana ja riittävä luottamus tilanteisena ehtona.

## 3. BASELINE: hyödyllinen vertailu mutta väärä hintalaki

### 3.1 Vastaesimerkki löytyy jo yhdeltä maksajalta

**CALCULATION, rakennettu vastaesimerkki:** vaihtoehto A tuottaa asiakkaalle 50 € hyödyn ja maksaa 10 €. B tuottaa 100 € hyödyn ja maksaa 30 €. Molemmat läpäisevät etukäteen asetetun vähintään 40 € bruttohyödyn vaatimuksen. Asiakas valitsee B:n koska nettohyödyt ovat 40 € ja 70 €. B:n hinta ylittää halvimman hyväksyttävän A:n hinnan. Ei laitonta toimintaa tai irrationaalista asiakasta.

Jos ”hyväksyttävä” muutetaan jälkikäteen tarkoittamaan ”asiakkaan eniten haluama”, vastaväite katoaa määritelmän sisään. Silloin sääntö ei ennusta valintaa.

**INFERENCE, yksinkertaistettu kvasilineaarinen valintamalli:** asiakas valitsee meidät kun

`v_me − p_me ≥ max_j(v_j − c_j)`.

Tästä seuraa `p_me ≤ v_me − max_j(v_j − c_j)` eikä yleisesti `p_me ≤ min_j c_j`. Vasta yhtäläisten hyötyjen tapauksessa hinnan vertailu pelkistyy halvimpaan vaihtoehtoon. Malli olettaa tiedetyt vaihtoehdot ja vertailukelpoisen rahamääräisen hyödyn. Se ei ole kaikkien ihmisten käyttäytymislaki.

### 3.2 Seitsemän vaikeaa luokkaa

| Tilanne | Mikä rikkoo staattisen baselinen? | Mitä silti voidaan testata? |
|---|---|---|
| Asiakas ei tiedä tarvetta | Nykyinen ostoslista ei sisällä uutta hyötyä. Nykyinen toiminta voi olla hyväksyttävää ilman että kysyntä on nolla uuden tiedon jälkeen | Valinta ennen esittelyä ja sen jälkeen sekä pysyvä käyttö. Ei oleta halukkuutta maksaa |
| Markkina luodaan | Uusi käyttötapa muuttaa vertailtavaa lopputulosta | Kokeilun jälkeinen valinta ja uhraus suhteessa asiakkaan muuhun rahaan ja aikaan |
| Useita maksajia | Yksi kokonaishinta peittää eri puolten maksut ja tuet | Kunkin puolen osallistumisehdot ja koko järjestelmän netto |
| Käyttäjä ≠ maksaja | Ilmainen käyttö ei aseta mainostajan tai työnantajan maksua nollaksi | Käyttäjän osallistuminen erikseen maksajan lisähyödystä |
| Verkostoarvo | Hyöty riippuu muiden osallistumisesta. Baseline ei ole toimijasta riippumaton vakio | Koko osallistujajakauma ja kannusteet sekä alkuvaiheen tyhjän verkon ongelma |
| Tuote muuttaa rajoitteita | Ulkoistaminen, rahoitus tai standardi voi muuttaa asiakkaan kapasiteettia ja pääsyä | Ennen/jälkeen mahdollinen toiminta ja muutoskustannus |
| Vaihtoehdon hinta riippuu meistä | Kilpailija alentaa hintaa vasta tulomme vuoksi tai täydentävä tuote halpenee verkon kasvaessa | Kilpailijan mahdollinen vastaus ja hinnoittelun herkkyys. Nykyinen hinta ei ole muuttumaton vastafaktuaali |

**FACT, historiallinen esimerkki:** Googlen 23.10.2000 tiedote kuvaa ilmaisen haun ja erillisen maksullisen avainsanamainonnan. Maksullinen tuote sai varhaisessa beta-vaiheessa mainostajia. Hakijan maksuton vaihtoehto ei ole mainostajan ostaman kontaktin hintakatto. [S3](https://googlepress.blogspot.com/2000/10/google-launches-self-service.html).

**Tarkka soveltamisalue:** halvimman hyväksyttävän vaihtoehdon kokonaiskustannus on vahva vertailu **määritellyn lopputuloksen korvaavissa hankinnoissa**, kun hyväksymisehdot ovat etukäteen tiedossa, vaihtoehdot ovat saavutettavia, olennaiset hyötyerot on vakioitu ja vaihto-, aika- sekä riskikustannukset huomioidaan. Esimerkiksi saman rakennuspolun korjaus vastaan toimiva valmis julkaisu. Silloinkin kyse on kilpailupaineesta eikä mekaanisesta jokaisen kaupan hintayhtälöstä.

**Korjaus myös omaan sääntööni:** tekemättä jättäminen on aito vaihtoehto jos se täyttää ostajan tavoitteen. Se ei ole ainoa baseline eikä sitä pidä poistaa vaihtoehtojoukosta. Uusissa markkinoissa tarvitaan yleisempi osallistumis- ja arvovertailu. Menetetty mahdollisuus käyttää rahaa muualla on aina olemassa mutta sen nimeäminen baselineksi ei tee alkuperäisestä hintalaista totta.

## 4. CAPTURE: tila ensin on mahdollista mutta ei ilmainen optio

**Kyllä: tila voidaan rakentaa ennen toimivaa kaappausta.** Googlen vuoden 1998 prototyyppijulkaisu kuvaa hakuteknologiaa ja hyperlinkkitietokantaa. Vuoden 2000 tiedote kuvaa uuden itsepalvelullisen mainostuotteen. Tämä on dokumentoitu järjestys teknisen tilan ja kyseisen kaappausmuodon välillä. Se ei osoita että kaikki Googlen tulot olivat nolla siihen asti tai että tuleva menestys oli ennustettavissa vuonna 1998. [S4](https://research.google/pubs/the-anatomy-of-a-large-scale-hypertextual-web-search-engine/), [S3](https://googlepress.blogspot.com/2000/10/google-launches-self-service.html).

OSS:n maksava täydentävä palvelu voi myös toimia vaikka asiakas saa koodin ja oppii sen. Red Hatin vuoden 1999 tiedote kuvaa tilausmallia, tukipalveluja ja kumppanien tulonjakoa samalla kun asiakkaalle annetaan teknologian hallintaa. Tämä haastaa ehdon ”S ei siirry asiakkaalle”. Brändi ja toimituskyky voivat säilyä toimittajalla mutta koko hyödyllisen tiedon ei tarvitse pysyä salassa. [S5](https://www.redhat.com/en/about/press-releases/press-revenuegains).

**UNKNOWN:** teorian kaikkia Redis/MongoDB/WordPress-esimerkkejä koskevaa yhteisväitettä ”vuosia, CAPTURE nolla” ei ole tässä varmennettu. Projektin arvo, tekijän palkka ja myöhemmän yrityksen omistus ovat eri suureita. En käytä väitettä todisteena.

Viivästetyn kaappauksen tarkka versio vaatii neljä etukäteistä vastausta:

- mikä tila kertyy ja kenellä on oikeus hyödyntää sitä
- mikä myöhempi maksullinen suoritus voidaan kokeilla
- miksi maksullisuus ei hävitä juuri sitä osallistumista jonka varaan tila rakennettiin
- mikä aika- ja kustannusraja katkaisee odottamisen jos maksureitti ei saa näyttöä.

Ilman näitä viivästetty CAPTURE on UNKNOWN. Se ei ole läpäisy. Asiakkaan oppiminen on uhka vain jos se poistaa maksullisen suorituksen nettolisähyödyn tai vie sen halvemmalle toimijalle. Kestävän kaappauksen ei tarvitse tarkoittaa kasvavaa prosenttiosuutta: pienenevä osuus kasvavasta arvosta voi tuottaa kasvavaa nettotuloa.

## 5. SCARCITY: niukka mikä ja millä aikajänteellä?

**INFERENCE:** tuotannontekijän niukkuus, kilpailijoita hitaammin kopioituva asema ja positiivinen hinta ovat kolme eri asiaa. Lähes rajaton kopioitava resurssi voi olla valtavan tuotannon pohja. Siitä ei seuraa että alkuperäinen tekijä saa taloudellisen tuoton. Mutta erillinen muuttumaton niukka resurssi ei ole tämän aukon ainoa mahdollinen ratkaisu.

- **Kysyntä kasvaa tarjontaa nopeammin:** väliaikainen kapasiteetti- tai koordinointiero voi riittää tuottoon. Jatkuva uusiutuminen voi olla mekanismi. Pysyvä suoja ei seuraa siitä.
- **Verkostovaikutus:** käyttäjien yhteensopivuus ja samanaikainen läsnäolo tuottavat hyötyä. Niukkuus voi syntyä koordinaatiosta eikä olla ostettu alkuresurssi.
- **Ensimmäisen toimijan historia:** historia voi vähentää epävarmuutta tai opettaa organisaatiota. Tämä on STATE-hypoteesi. Aikaisuus yksin ei takaa etua.
- **Standardi tai protokolla:** avoin yhteensopivuus voi kasvattaa kaikkien käyttöä. Standardin tekijän ansainta jää erilliseksi kysymykseksi. Suuri yhteiskunnallinen arvo ei todista kaappausta.
- **Yleisö:** yleisö on usein säilyvää kysyntätilaa ja mahdollisen palautteen kanava. Sen huomio on rajallista mutta ”yleisö = niukkuus” ei ole erillinen selittävä ehto jos kaikki toimiva palaute nimetään niukkuudeksi.

**CALCULATION, vastaesimerkki pysyvälle hintasuojalle:** jos nettokate per suorite puolittuu mutta hyväksytty kysyntä nelinkertaistuu, kokonaiskate kaksinkertaistuu. Tämä ei todista että tällainen kysyntä löytyy meille. Se osoittaa että laskeva baseline ei loogisesti tapa kasvavaa taloutta.

**Tuomio:** SCARCITY poistetaan itsenäisenä välttämättömyytenä. Korvaava kova kysymys on voiko meille jäävä nettotuotto säilyä riittävän kauan kun kopiointi, kilpailijoiden vastaukset ja tilan rapautuminen huomioidaan. Tämä voi perustua hetkelliseen etuun, jatkuvaan kehitykseen, työnjakoon tai syntyvään koordinaatioon. Kaikkien nimeäminen niukkuudeksi ei lisää ennustusvoimaa.

## 6. STATE: mikä selviää tuhoamisyrityksestä?

### 6.1 Vahvin väite jota en saanut kumottua

**En löytänyt vahvaa historiallista toistettavaa vastaesimerkkiä, jossa aiempi onnistuminen itsessään kasvattaa seuraavaa onnistumista mutta mitään vaikuttavaa tilaa ei siirry.** Jos N:n tieto, resurssit, järjestelmä ja vaikutukset todella nollataan sekä ulkoiset panokset vakioidaan, N ei voi aiheuttaa eroa N+1:een.

Tämä tukee kausaalisen tilan tarvetta **endogeenisessa kasautumisessa**. Se ei todista että tilan pitää olla yrityksen yksin omistama, salainen, ylläpidoton tai jokaisen tapahtuman jälkeen suurempi. Verkoston tila voi sijaita asiakkaissa tai ekosysteemissä. Yrityksen pitää silti päästä hyötymään siitä.

**Riippumattomuusraja:** kaksi mallia päätyy tähän mutta toinen on nyt lukenut ensimmäisen teorian ja molemmat saman tehtävänannon. Tämä on ristiinarvioinnin läpäissyt päätelmä eikä kaksi riippumatonta empiiristä toistoa.

### 6.2 Kasvu ilman edellisen kierroksen uutta tilaa

**Rakennettu looginen vastaesimerkki, ei uusi liiketoimintaehdotus:** jo valmis muuttumaton ohjelma suorittaa riippumattomia tehtäviä. Tulokset ja tehtäväkohtainen muisti poistetaan. Ulkoinen kysyntä kasvaa ja vuokrattavaa laskentaa lisätään. Seuraavan kierroksen volyymi voi kasvaa ilman että edellinen suoritus jätti uutta tuottavaa tilaa. Teknologia ja käyttöoikeus olivat olemassa jo ennen ensimmäistä kierrosta.

Tämä rikkoo väitteen ”kaikki kasvu vaatii joka kierroksella kertyvää uutta S:ää” mutta **ei ole vastaesimerkki endogeeniselle kasautumiselle**. Kasvun syy on ulkoinen kysyntä ja lisäpanos. Vastaavasti vakioinen suuri toistuva ylijäämä voi kasvattaa varallisuutta ilman paranevaa yksikkötaloutta. Varallisuus, skaalautuminen ja oppimissilmukka on pidettävä erillään. Raha on tällöin säilyvää tilaa vaikka Claude sulkee sen pois.

### 6.3 P1–P6:n erillinen testi

| Ominaisuus | Tuomio | Peruste ja korjattu mittaus |
|---|---|---|
| P1: ei jatkuvaa ihmisen ylläpitoa | KILLED välttämättömyytenä | Organisaatio ja luottamus voivat tarvita ylläpitoa. Ratkaisee hyöty miinus ylläpito ja rapautuminen, ei nollaylläpito |
| P2: kone tai yleisö kuluttaa, ei ihminen | KILLED välttämättömyytenä | Ihminen voi käyttää yhteistä tietoa monessa päätöksessä. Myös teoriaan hyväksytty palkattu organisaatio kantaa tilaa. Mittaa kaikkien ihmisten työtä ja katetta |
| P3: auttaa eri tapauksessa, ei vain samassa asiakkaassa | MODIFIED | Sama asiakas voi uusia, laajentaa ja tuottaa enemmän katetta olemassa olevan integraation päällä. Toistuva hyöty on tärkeä, asiakasrajan ylitys ei universaali |
| P4: laillinen käyttöoikeus | SURVIVES projektirajana | Omistaminen ei ole välttämätöntä jos käyttö on muuten sallittu. Käyttöluvan laajuus erotetaan datan hallussapidosta |
| P5: ei-kopioitava | KILLED välttämättömyytenä | Julkinen koodi voi vähentää sekä meidän että muiden kustannusta. Se voi olla tuottavaa tilaa vaikkei kilpailuvalli. Kilpailun vaikutus katteeseen arvioidaan erikseen |
| P6: kausaalinen vaikutus | SURVIVES | Pelkkä tallennettu aineisto tai ajallinen korrelaatio ei riitä. Mittaa poistamisen vaikutus koko talouteen samalla laadulla |

**CALCULATION, mittarin väärä negatiivinen:** myyntihinta 100 €, toimitus 40 € ja hankinta 50 € tuottavat 10 € katetta. Jos referenssi laskee hankinnan 10 euroon, kate on 50 €. Toimituksen ihmistyö ja hintaosuus voivat pysyä samoina. Clauden h/s-portti hylkää viisinkertaistuneen katteen. Luvut ovat tarkoituksella rakennettuja, eivät markkinahavaintoja.

Myös hyväksymisasteen nousu voi kasvattaa nettotuloa h:n ja s:n pysyessä samoina. Siksi yhteinen mittari on **hyväksytyn tuloksen koko nettotalous**. Hankintaa, toimitusta ja tilan ylläpitoa ei saa erottaa niin että hyödyllinen muutos katoaa määritelmään.

## 7. HUMAN ja AI-attribuutio

HUMANin korjaus pelastaa tavallisen palkkaamalla kasvavan yrityksen. Se on sallittu valinta mutta samalla teoria lakkaa erottelemasta AI-vipua tavallisesta yrittämisestä. Kate yli palkan ei vielä riitä: perehdytys, laadunvalvonta, johto, etupainotteinen palkkakassa ja asiakashankinta kuuluvat kustannuksiin.

**Yksinkertainen attribution-sääntö:**

> AI-vivuksi kirjataan vain se hyväksytyn tuloksen, kustannuksen tai pääsyn mitattu parannus jonka AI:n poistaminen hävittää vertailukelpoisessa tilanteessa. Myöhemmän yrityksen koko arvoa ei kirjata AI:n ansioksi.

Käytännössä valitaan ensimmäinen taloudellisesti merkityksellinen välitulos ennen mittausta. Verrataan samaa lähtötilaa, laatua ja resurssirajaa AI:n kanssa ja ilman sitä tai parhaaseen saavutettavaan ei-AI-vaihtoehtoon. Lasketaan myös tarkistus- ja virhekulut. Jos AI mahdollistaa ensimmäisen tilan hankinnan budjetissa, voidaan sanoa **AI mahdollisti käynnistyksen**. Väite **AI parantaa edelleen skaalausta** tarvitsee myöhemmän erillisen näytön.

Jos kontrollia ei saada tai tulos selittyy lisähenkilöillä ja rahoituksella, attribuutio on UNKNOWN. Se ei tee yrityksestä huonoa. Se estää tavallisen kasvun nimeämisen todisteeksi projektin AI-hypoteesista. Tämä sääntö ei edellytä että AI tekisi jotain ihmiselle periaatteessa mahdotonta.

## 8. CAPITAL: polttoaine ja tilan hankinta

**Väite ”pääoma ei ole rajoite missään aineiston tapauksessa” on KILLED perustelemattomana yleisväitteenä.** Teoria itse mainitsee eksklusiivisten oikeuksien ja fyysisen kapasiteetin pääomaportit. Se että meillä puuttuu sekä raha että tila ei osoita kumman lisääminen muuttaisi tilannetta.

| Käyttö | Capital as fuel | Capital as state acquisition |
|---|---|---|
| Määritelmä | Maksaa tämän kierroksen suorituksen ilman jäljelle jäävää hyödyllistä muutosta | Ostaa tai rakentaa tulevaa käyttöä, pääsyä, kapasiteettia tai valinnanvaraa |
| Mahdollisia muotoja | tämän ajon laskenta, kertatoimitus, hukkaan menevä huomio | laillinen datalisenssi, siirtyvä omistus, integraatio, säilyvä asiakassuhde, käyttöoikeus, tuotantoväline |
| Ratkaiseva testi | palaako järjestelmä suorituksen jälkeen entiseen tilanteeseen? | mitä tulevaa toimintaa sama raha mahdollistaa verrattuna tilanteeseen jossa ostoa ei tehty? |
| Virhe jonka pitää välttää | kaikki kulut eivät ole turhia | kaikki aktivoitavaksi kutsuttu ei ole arvokasta tai jälleenmyytävää |

Sama meno voi sisältää molempia. Mainonta voi ostaa kertaklikin tai pysyvän asiakassuhteen. Laskenta voi palvella yhtä tilausta tai tuottaa uudelleenkäytettävän artefaktin. Nopeus voi antaa aikaa oppia ja hankkia käyttäjiä ennen kilpailua ilman pysyvää yksinoikeutta.

**FACT:** Amazonin vuoden 1997 kirje kertoo asiakaskannan ja infrastruktuurin investoinneista sekä ulkoisesta rahoituksesta. Kyse ei ollut vain datan tai julkisen näytön ostamisesta. Tämä ei todista pääoman riittävyyttä mutta kumoaa luokittelun jossa muun tilan hankinta ei voi olla kasvumekanismia. [S6](https://www.aboutamazon.com/news/company-news/amazons-original-1997-letter-to-shareholders).

**CALCULATION:** vakioisella 20 %:n nettotuotolla ja täydellä uudelleensijoittamisella `W_t = 1 000 × 1,2^t`. Raja 10 M ylittyy noin 50,52 vuodessa eli kokonaisvuosina vuonna 51. Tämä ei vaadi arvostuskertoimen nousua. Se on hidas ja epärealistiseksi mahdollisesti osoittautuva oletusketju mutta matemaattisesti kasautuva. Micronsin vuositulomultiple ei todista 20 %:n nettotuottoa, koska tulot eivät ole voitto ja ostot sisältävät muita kuluja. Lisäksi teorian esimerkki sekoittaa eurot dollareihin. Projektin aiempi päätös sulkea pois ”raha → lisää samaa työtä” on sallittu tutkimusrajaus. Se ei kuitenkaan todista pääoman uudelleensijoittamisen matemaattista kasautumista olemattomaksi.

**INFERENCE:** raha on fungible mutta ei ilmaiseksi kopioitava. Kilpailijan sama rahamäärä ei poista meidän budjettirajoitteen lievenemistä. Pääoma voi ostaa tilaa ja tilan puute voi johtua pääoman puutteesta. Näitä ei pidä asettaa vastakohdiksi.

**HYPOTHESIS:** 1 000 € voi olla merkityksellinen juuri diskreetin käyttöoikeuden, pienen infrastruktuurin tai tiedollisen option hankinnassa. **UNKNOWN:** mikä sellainen oikeus olisi meille saatavilla ja tuottaisi positiivisen nettovaikutuksen. Tässä ei nimetä uutta ostokohdetta eikä ehdoteta maksua. Ulkoinen rahoitus voi myöhemmin olla mahdollinen mutta se on eri asia kuin jo saatavilla oleva rahoitus ja laimentaa omistajan osuutta.

## 9. Ulkopuoliset historialliset yksikkötestit

Testit käyttävät varhaisessa vaiheessa julkaistua tietoa. Myöhempi menestys kertoo vain että mekanismi kannattaa sisällyttää vastaesimerkkijoukkoon. Se ei ole tietoa jonka olisi saanut syöttää varhaiseen arvioon. Näissäkään havaintoajankohdat eivät kaikki ole perustamispäivä: IPO-vaiheen lähteillä ei teeskennellä tunnettavan aivan ensimmäistä vuotta.

| Mekanismityyppi ja varhainen tietoraja | Tuolloin saatavilla ollut tieto (FACT) | Alkuperäisen testin vaarallinen ratkaisu (INFERENCE) | Mitä testi oikeasti opettaa? |
|---|---|---|---|
| Ilmainen tiedonhakupalvelu → maksullinen toisen osapuolen pääsy. Google 1998 prototyyppi | Julkaistu tekninen arkkitehtuuri ja hakutietokanta [S4]. Vuoden 2000 mainostuotetta ei saa olettaa valmiiksi vuonna 1998 | VALUE/CAPTURE vaatii nimetyn maksajan nyt. Viivästetyn poikkeuksen pitäisi antaa UNKNOWN, ei KILL eikä tulevan menestyksen perusteella PASS | Käyttäjä ja maksaja erotettava. Tekninen tila voi edeltää kaappauksen muotoa. §6:n taulukko ei vielä sisällä §8:n poikkeusta |
| Avoimen ohjelmiston jatkuva tilaus- ja tukipalvelu. Red Hat 1999 | Yhtiö kuvaa maksullista tilausta, kasvavaa palveluorganisaatiota ja teknologian siirtymistä asiakkaan hallintaan [S5] | P5 tai CAPTUREn ”asiakas sisäistää menetelmän” voi tappaa. P1 voi tappaa jatkuvan ylläpidon | Ei todista ettei brändillä olisi merkitystä. Osoittaa että kaiken hyödyllisen S:n salassapito ei ole välttämätöntä |
| Toistuva vähittäiskauppa → asiakassuhteet ja toimitusinfrastruktuuri. Amazon 1997 | Kirje kuvaa uusiutuvia ostoksia, suosittelua, varastoa, toimituskapasiteettia ja rahoitusta [S6] | CAPITALin tappoehto ”jokainen askel vaatii ostoa tai varastoa” hylkää. Pelkän hankinnan paranemisen poissulku hukkaa osan mekanismista | Hyvä yleinen mekanismi voi olla huono meidän 1 000 € aloitukseksi. Yleinen mahdottomuus ja meidän pääsyraja erotettava |
| Jaettu ohjelmistotuotanto ja uusiutuvat asiakassopimukset. Salesforce 2003 S-1 | Yhteinen moniasiakasarkkitehtuuri, myyntipanostukset ja epävarmat uusinnat kuvataan ennen myöhempää suuryritysvaihetta [S7] | STATE-taulukko sulkee toistuvat sopimukset pois ja §1b/1e väittää tuotannon mittakaavan riittämättömäksi ilman verkkomoottoria | Jaettu kiinteä kustannus on eri asia kuin käyttäjien keskinäinen verkostovaikutus. Tuleva uusinta on mitattava eikä oletettava |

Lähteet eivät osoita että jokainen vastaava pieni toimija olisi voittanut. Ne osoittavat ettei kyseisiä mekanismiluokkia saa sulkea pois teorian väittämillä universaaleilla perusteilla. Suuren mittakaavan toteutumisesta on myöhempää julkista näyttöä Red Hatin historiassa sekä Googlen ja Salesforcen vuosiraporteissa [S8–S10]. Näitä ei käytetä varhaisen valinnan syötteenä.

**Rajaus:** nämä historialliset mekanismit eivät osoita että juuri niiden edut kestäisivät tulevan lähes ilmaisen frontier-AI:n maailmassa. Sen sijaan ne kumoavat väitteet yleisestä taloudellisesta välttämättömyydestä. AI-maailmaa koskeva vahvempi väite tarvitsee oman näytön eikä voi saada todistetta pelkästä nykyisten pienten tapausten otoksesta.

## 10. Väärät positiiviset: testin läpäisevä huono talous

Seuraavat ovat tarkoituksella rakennettuja HYPOTHESIS-testisyötteitä. Ne eivät ole uusia mahdollisuusideoita tai markkinahavaintoja.

**Yhteinen läpäisytarina:** hyväksyttävä toimiva tuote, maksava asiakas, sopimusoikeus, delegoitava tai automatisoitu toimitus, yksityinen data/asema, säilyvä tila, etukäteinen A/B-suunnitelma, nimetty budjetti, aluksi rahoitettavissa oleva toimitus, nimetty yhtiö, suuri nimellinen markkina ja alle viikon falsifier. Toiminta on toistuvaa eikä yhden jättivoiton varassa. Tämä täyttää taulukon sanalliset läpäisyehdot.

| Väärä positiivinen | Miksi talous silti pettää? | Mitä rakennetestistä puuttuu? |
|---|---|---|
| Eksklusiivinen aineisto ja maksavia kokeilijoita | **CALCULATION:** 100 € kertamaksu − 20 € toimitus − 120 € hankinta = −40 €. Automaatio ja hieno tila eivät korjaa negatiivista asiakastaloutta | Kaikki hankinta- ja uusintakulut sekä kohortin toteutuva elinkaari. Nimetty maksaja ei riitä |
| Tila säästää jokaisessa seuraavassa toimituksessa | **CALCULATION:** 10 € säästö × 10 toimitusta = 100 € mutta varannon ylläpito maksaa 200 € samalla jaksolla | Tilan nettovaikutus kertymisen ja rapautumisen jälkeen. Positiivinen osamittari ei riitä |
| Maksullisuus suunnitellaan ilmaisen verkon päälle | Maksullinen vaihe poistaa osallistujat tai estää toisen puolen liittymisen. Hyöty ja kaappaus toteutuvat eri maailmoissa | Arvon, osallistumisen ja maksamisen samanaikainen yhteensopivuus |
| Halpa hankinta pienessä innokkaassa kohortissa | Seuraavien kohorttien hankinta kallistuu ja poistuma kasvaa. Ensimmäinen kate ei skaalaudu | Marginaalinen seuraavan kohortin talous ja saavutettava kysyntä. Markkinan kokonaiskoko ei ole meidän kattoarviomme |
| Hyvä yksikkökate mutta sama yhteinen riippuvuus | Yksi alustan ehtomuutos tai yhteinen laatuvirhe pysäyttää kaikki toimitukset. Monet laskut eivät ole riippumattomia toistoja | Yhteisriskit, vastuut ja mahdollisuus rahoittaa seuraava kierros |

**Looginen tarkennus:** jos EV tarkoittaisi jo täydellisesti tunnettua positiivista nettotuottoa kaikkine vaikutuksineen, negatiivisen EV:n mekanismi ei voisi läpäistä sitä. Silloin EV olisi vastauksen sisältävä oraakkeli. Käytännön taulukko ei määritä tällaista mittausta. Väärät positiiviset paljastavat eron sanallisen rakenteen ja todennetun yhteistalouden välillä. Täydellinenkään positiivinen EV ei estä yksittäistä epäonnistumista.

Puuttuva yhteinen ehto on **samanaikaisesti toteutuva dynaaminen nettotalous**: kysyntä, maksaminen, tilan hyöty, hankinta, vastuut ja rahoitus pitää arvioida samassa mekanismissa ja samassa vaiheessa.

## 11. Väärät negatiiviset ja tappojärjestys

Vahvimmat väärän hylkäyksen kohdat ovat:

1. **Hinnoittelu yli halvimman hyväksyttävän vaihtoehdon:** hyötyero riittää. BASELINEn hintalaki väärä.
2. **Asiakassuhde joka parantaa vain hankintaa tai uusintaa:** h/s-portti väärä. Koko kate voi kasvaa.
3. **Avoin siirtyvä tieto ja maksullinen täydentävä suoritus:** ei-kopioitavuus ja asiakkaan oppimisen kielto liian vahvoja.
4. **Varaston tai infrastruktuurin avulla kasvava talous:** pääomaa tarvitseva ei tarkoita huonoa mekanismia. Meille saavuttamattomuus on eri päätös.
5. **Viivästetty kaappaus:** välitön maksajavaatimus voi hylätä liian aikaisin. Silti pelkkä tulevaisuustarina ei oikeuta PASSia.
6. **Hitaasti mitattava hyväksyntä:** ”alle viikossa falsifioitava” on projektin kustannustoive eikä suuren vivun välttämätön ominaisuus. Pitkä testi voidaan jättää projektissa tekemättä ilman että teoria julistaa mekanismin kuolleeksi.

### Miksi VALUE ei voi olla automaattisesti seitsemäs?

Ilman hyödyllistä vaikutusta sopimuksen kaappausoikeuden yksityiskohtainen selvitys voi olla hukkatyötä. CAPTURE voidaan silti joskus tappaa halvalla ennen arvon tarkkaa mittausta jos oikeudellinen tai sopimuksellinen mahdottomuus on jo tiedossa. Siksi VALUE ensin on hyödyllinen oletusjärjestys mutta ei uusi luonnonlaki.

**CALCULATION:** kahden riippumattoman testin i ja j kustannukset ovat c_i ja c_j. Hylkäystodennäköisyydet ovat q_i ja q_j. Järjestyksen i→j odotettu kustannus on `c_i + (1−q_i)c_j`. i kannattaa ensin kun `c_i/q_i ≤ c_j/q_j` positiivisilla q-arvoilla. Tämä perustelee halvan todennäköisen tappajan aloittamisen. Meillä ei ole numeerisia q-arvoja eikä niitä keksitä. Todelliset testit voivat myös riippua toisistaan.

Käytännön järjestys: ensin lyhyt arvo- ja osallistumiskuvaus sekä ilmeiset laillisuus-, pääsy- ja resurssiestot. Sitten halvin avoin oletus jonka ratkaiseminen muuttaa päätöstä. FALSIFIER ja näytön tila kirjataan jokaisen kysymyksen yhteydessä. EV muodostuu kokonaisuudesta eikä viimeisestä lisäkysymyksestä. UNKNOWN ei ole tosi eikä epätosi.

## 12. Lopullinen luokittelu

### A. SURVIVES

- **Kausaalinen säilyvä tila endogeenisessa kasautumisessa:** ei vahvaa vastaesimerkkiä. Tämä ei tarkoita Clauden P1–P5-paketin hyväksymistä.
- **P6:** nimetyn tilan lisävaikutus on erotettava sattumasta, tehtäväerosta ja ulkoisesta kasvusta.
- **Laillinen käyttö:** P4 ja projektin laillisuusraja.
- **Toistettavan nettotuoton ja selviytymisen vaatimus:** E5 projektin valintaperusteena. Toteutunut EV on edelleen UNKNOWN.

### B. MODIFIED

- **BASELINE:** määritellyn korvaavan hankinnan hyötyvakioitu vertailu. Muissa luokissa osapuolikohtainen osallistuminen ja dynaamiset vaihtoehdot.
- **CAPTURE + kontti:** yksi vaatimus laillisesta reitistä meille jäävään arvoon. Viivästetty reitti on mahdollista mutta vaiheistettava ja testattava.
- **STATE:** hyödyllinen vaikutus voi olla hankinnassa, uusinnassa, laadussa, kustannuksessa tai tuotossa. Ylläpidon ja kilpailun vaikutus lasketaan mukaan.
- **HUMAN:** kaikkien ihmisten ja organisaation kustannus. Perustajan aika ei saa olla piilotettu rajaton panos. Erillinen AI-attribuutio.
- **CAPITAL:** polttoaine, tilan hankinta ja ajoituksen rahoitus erotetaan. Meidän pääsyrajamme erotetaan mekanismin toimivuudesta.

### C. KILLED

- muuttumaton AI:lta suojattu niukkuus välttämättömänä ehtona
- halvimman hyväksyttävän vaihtoehdon hinta universaalina hintakattona
- S:n ei-kopioitavuus, ylläpidottomuus ja koneen/yleisön käyttö universaaleina ehtoina
- asiakkaan oppimisen tai tiedon saamisen pitäminen automaattisena kaappauksen loppuna
- erillinen omistuskontti itsenäisenä kasvumoottorina
- verkkomuoto ainoana erittäin suuren vivun rakenteena
- julkisuus ja ”ei uhkaprofiilia” universaalina taloudellisena ehtona
- pääoman merkityksettömyys sekä väite että vain näyttö ja data voivat käynnistää palautteen
- alle viikon falsifier ja kolme peräkkäistä UNKNOWNia yleisinä teoreettisina portteina.

### D. UNKNOWN

- tuottaako meidän hankittavissa oleva S seuraavan kierroksen nettolisähyödyn
- säilyykö hyöty mallien kehittyessä ja kilpailijoiden saadessa saman tiedon
- voimmeko kaapata hyötyä hyväksyttävillä sopimuksilla ja vähäisellä riskillä
- paljonko AI vaikuttaa suhteessa ihmiseen, valmiisiin työkaluihin ja lisäpääomaan
- saavutettava kysyntä, rahoitettavuus, aika ja omistajalle jäävä osuus mahdollisella 10 M€ polulla
- teorian ennusteiden tarkkuus: tähän ei ole riittävää ulkopuolista positiivisten ja negatiivisten tapausten aineistoa.

## 13. Structural Test v2: kuusi kovaa kysymystä

Tämä on tutkimuspäätösten testi eikä sertifikaatti tulevasta 10 M€ tuloksesta. Vastaukset ovat **näyttöä jatkoon / falsifioitu rajattu hypoteesi / UNKNOWN**. Yksi osoitettu välttämättömän lenkin mahdottomuus tappaa kyseisen mekanismin siinä muodossa. Meidän resurssirajamme voi siirtää mekanismin sivuun tekemättä siitä yleisesti mahdotonta.

| # | Kova kysymys | Mitä kelpuutetaan? | Mikä katkaisee tämän version? |
|---|---|---|---|
| 1. ARVO JA OSALLISTUMINEN | Mikä hyväksytty tulos muuttuu paremmaksi ja ketkä käyttäjät sekä maksajat valitsevat sen todellisten vaihtoehtojensa sijasta? | Rajattu suoritus, kaikki olennaiset osapuolet ja havaittava hyöty/valinta. Uuden kysynnän kohdalla testattava käyttöhypoteesi | Mitään lisähyötyä ei synny tai välttämätön osapuoli ei osallistu. Tuntematon kysyntä jää UNKNOWNiksi |
| 2. MEILLE JÄÄVÄ ARVO | Miten maksu tai muu realisoitava korvaus päätyy meille nyt tai nimetyssä myöhemmässä vaiheessa ilman että arvon synty hajoaa? | Oikeus suoritukseen/korvaukseen, maksuvaihe ja netto-osuus. Viivästykselle kulukatto ja hyväksymiskoe | Tarvittavaa oikeutta ei voi saada tai maksullisuus tuhoaa mekanismin. Kontin nimi ei riitä |
| 3. TALOUDELLINEN JATKUVUUS | Voiko seuraavat kierrokset rahoittaa kun kaikki työ, hankinta, ylläpito, virheet, vastuut ja tilan rapautuminen maksetaan? | Kohortin tai suoritteen koko talous, kassavaje, saatavilla oleva rahoitus ja ehdot | Toistuva tappio ilman rajattua oppimisinvestointia tai rahoittamaton pakollinen askel. Suuri kokonaismarkkina ei pelasta |
| 4. KAUSAALINEN VIPU | Mikä toistuvasti käytettävä tai kasvava tila muuttaa seuraavien kierrosten taloutta ja mitä sen poistaminen tekee? Mikä osuus muutoksesta johtuu AI:sta? | Etukäteen nimetty S, laillinen käyttö, vastafaktuaali ja nettovaikutus. Alkuperäinen kiinteä tuotantovipu erotetaan kierrosten kasautumisesta | Väitetty S/AI ei vaikuta vertailussa. Voi jäädä tavallinen hyvä yritys mutta väitetty kasautumis- tai AI-mekanismi kuolee |
| 5. SEURAAVAN KOON KESTÄVYYS | Toimiiko yhteistalous myös seuraavassa kohortissa kilpailijoiden, kopioinnin, ruuhkien ja lisäihmisten jälkeen? | Rajattu seuraava skaala, kysyntänäyttö, pullonkaula ja kasvun omistusvaikutus | Kate tai pääsy katoaa ennen väitettyä mittakaavaa eikä nimettyä korjaavaa mekanismia ole |
| 6. RATKAISEVA NÄYTTÖ | Mikä halvin vielä avoin havainto muuttaa päätöksen ja milloin lopetamme? | Etukäteen rajattu koe, hyväksyjä, kustannus- ja aikaraja sekä tulkinta myönteiselle, kielteiselle ja epäselvälle tulokselle | Väite pelastetaan aina muuttamalla määritelmää tai mikään saavutettava havainto ei muuta päätöstä |

Kysymys 6 kulkee mukana alusta lähtien. Muiden tutkimisjärjestystä vaihdetaan tietokustannuksen perusteella. Erillistä SCARCITY-porttia ei tarvita. Sen hyödyllinen sisältö on kohdassa 5. Erittäin suuren henkilökohtaisen varallisuuden tavoite vaatii lisäksi aikajänteen ja omistusosuuden raportoinnin. Yksi onnistunut kierros ei ole tätä koskeva ennuste.

## 14. Yksi seuraava empiirinen koe: tilan poistaminen ja kopioiminen

**Ei suoritettu. Ei WordPress-koetta, aineiston keruuta tähän kokeeseen, maksua tai yhteydenottoa.** Seuraava on yksi kolmihaarainen koeasetelma. Se on informatiivisempi kuin pelkkä ensimmäisen ja toisen työn kellottaminen.

**Pääkysymys:** parantaako ensimmäisistä tapauksista jäänyt S uusien hyväksyttyjen suoritusten nettotuottavuutta parhaan ilmaisen baselinen päälle? **Toinen saman kokeen kysymys:** vaatiiko hyöty yksityisyyttä vai säilyykö se myös uudella toimijalla joka saa kopion S:stä?

### Lukittava asetelma ennen toteutusta

- Yksi rajattu tekninen tehtäväluokka jossa on dokumentoituja toistettavia virheitä ja etukäteen määriteltävä hyväksytty lopputulos. Ei valintaa pelkän iän tai ”tested up to” -merkinnän perusteella. Ei ostajien maksuhalukkuuden simulointia.
- Lähtöehdoksi vähintään 12 riippumatonta pidätettyä tapausta vähintään kolmesta erillisestä projektista sekä niistä erilliset harjoitustapaukset. Luvut ovat koesuunnittelun käytännöllinen aloitusehto, eivät tilastolliseen voimalaskelmaan perustuva lupaus. Jos sopivaa joukkoa ei ole, protokollaa ei väitetä toteutetuksi.
- S tuotetaan vain harjoitustapauksista. Sen sisältö, kokoamis- ja tarkistustyö sekä ylläpito kirjataan. Testitapausten hyväksyntä lukitaan ennen S:n käyttöä. Ei samaa bugia eri nimillä oppimis- ja testijoukoissa. Julkisten tapausten mahdollista kuulumista mallin koulutusdataan ei voida sulkea pois.
- Sama jäädytetty malli, työkalut, laskentaraja ja parhaat julkiset ohjeet kaikille. Erilliset puhtaat kontekstit ja ympäristöt. Tapaukset ajetaan pareittain kaikissa haaroissa satunnaistetussa järjestyksessä. Hyväksyjä ei tiedä haaraa. Toistuvat ajot arvioivat mallin satunnaisvaihtelua mutta eivät kasvata riippumattomien tapausten määrää.

### Kolme haaraa samassa kokeessa

| Haara | Mitä saa? | Mitä erottaa? |
|---|---|---|
| A: nollattu työmuisti | Paras julkinen baseline ilman harjoittelusta syntynyttä S:ää | Mitä uusi saman AI:n käyttäjä saa jo ilmaiseksi? |
| B: säilynyt tila | Sama baseline sekä harjoitustapauksista muodostettu S | S:n lisävaikutus aiemman kierroksen jälkeen |
| C: kopion saanut uusi toimija | Sama baseline ja täsmälleen sama S mutta ei tekijän muuta keskustelua tai apua | Onko lisäetu kopioitavassa artefaktissa vai muussa historiassa? Tämä ei vaadi ulkoista henkilöä tai julkaisua |

A:lla on sama kokonaisresurssibudjetti julkiseen tiedonhakuun. B:n ja C:n pidempi konteksti, haku sekä epäonnistuneet yritykset lasketaan kustannuksiin. Jos toimittajan ihmisoperaattori on oppinut tehtävän, hänen oppimisensa ei saa vuotaa A:n ja B:n vertailuun: ihmisen apu rajataan ennalta tai kaikki apu kirjataan ja tulos merkitään sekoittuneeksi.

**Ensisijainen mittari:** kokonaiskustannus hyväksyttyä tulosta kohti yhteisellä laatuportilla. Raportoi erikseen ihmisminuutit, konekulut, epäonnistumiset ja S:n rakennuskulu. Älä piilota hylättyjen tehtävien työtä. Älä jaa rakennuskulua hypoteettisille tuhansille asiakkaille: laske takaisinmaksun vaatima toistomäärä havaituista säästöistä ja merkitse sen saavutettavuus UNKNOWNiksi.

**Ennalta ehdotettu käytännöllisen hyödyn raja:** vähintään 20 % alempi kustannus hyväksyttyä tulosta kohti ilman laatuheikennystä. 20 % on päätösraja eikä datasta johdettu luonnonvakio. Raja ja kustannuspainot on hyväksyttävä ennen ajoa. Raportoi tehtäväkohtaiset erot ja epävarmuus projektitasolla. Pieni tai epävarma otos tuottaa UNKNOWNin eikä keinotekoista PASSia. Hyödyn tulee näkyä useammassa kuin yhdessä projektissa.

| Havainto | Tulkinta |
|---|---|
| B ei voita A:ta riittävän tarkasti mitatussa vertailussa | Tämä S ei tuota väitettyä lisävipua. Tappaa paikallisen varantohypoteesin, ei kaikkea säilyvää tilaa |
| B voittaa A:n mutta rakennus/ylläpitokulu ylittää saavutettavan hyödyn | Tekninen siirrettävyys löytyi mutta taloudellinen kasautuminen jäi osoittamatta |
| B ja C voittavat A:n samankaltaisesti | S toimii tuottavana tilana mutta yksityisyys ei selitä etua. P5 ei ole teknisen hyödyn ehto. Meidän kilpailuetumme ja kaappauksemme jäävät UNKNOWNiksi |
| B voittaa C:n | Kokeesta puuttuu jokin tilan osa tai operaattorivaikutus. Ei saa nimetä salaiseksi vallihaudaksi ennen erottelua |
| Erot epävarmoja tai hyväksyntä huononee | Ei näyttöä jatkoon; korjaa mittaus tai hylkää kyseinen toteutus |

**Miksi juuri tämä koe?** Se hyökkää jäljelle jääneen ydinehdon kausaaliseen osaan ja samalla teorian vahvaan mutta huonosti perusteltuun ei-kopioitavuuteen. Yksi korjaus tai kaksi erilaista kellotettua tehtävää ei erota näitä. Koe ei todista maksuhalukkuutta, suuryritystä tai yleistä välttämättömyyslausetta. Se voi silti tappaa täsmällisesti väitteen että meidän nimeämämme S tekee seuraavasta suorituksesta taloudellisesti paremman.

## Lähteet ja tarkistuksen rajat

Ensisijaiset ulkoiset lähteet tarkistettu 16.9.2026. Historiallisten sivujen nykyinen sivupohja ja navigaatio eivät ole historiallista evidenssiä.

- **S1:** [HeroDevsin rahoitustiedote 24.7.2025](https://www.herodevs.com/blog-posts/herodevs-announces-125-million-strategic-growth-investment-from-psg). Varmistaa 125 M USD:n luonteen rahoituksena. Ei arvostusta tai työpanoksen skaalauslakia.
- **S2:** [PSG:n saman kaupan tiedote](https://psgequity.com/news/herodevs-announces-125-million-strategic-growth-investment-from-psg). Hakutulos vahvistaa otsikon ja päivämäärän. Suora avaus 403. Ei riippumaton liiketoiminnan auditointi.
- **S3:** [Googlen AdWords-julkistus 23.10.2000](https://googlepress.blogspot.com/2000/10/google-launches-self-service.html). Ilmainen haku, erillinen mainostaja ja uusi maksullinen itsepalvelu.
- **S4:** [Brin ja Page 1998: The Anatomy of a Large-Scale Hypertextual Web Search Engine](https://research.google/pubs/the-anatomy-of-a-large-scale-hypertextual-web-search-engine/). Tekijöiden julkaisutietue ja abstrakti. Tekninen prototyyppi eikä menestyksen ennuste. Koko paperin mainontaa koskevaan liitteeseen ei nojata tässä.
- **S5:** [Red Hatin 22.9.1999 tulostiedote](https://www.redhat.com/en/about/press-releases/press-revenuegains). Varhaisen tilaus-, tuki- ja kumppanuusmallin kuvaus. Yhtiön oma ilmoitus. Lukujen tarkkuuteen ei rakenneta johtopäätöstä.
- **S6:** [Amazonin alkuperäinen vuoden 1997 osakaskirje](https://www.aboutamazon.com/news/company-news/amazons-original-1997-letter-to-shareholders). Uudelleen julkaistu aikalaiskirje. Investoinnit, uusiutuva kysyntä ja ulkoinen rahoitus. Ei perustamispäivän tietoa.
- **S7:** [Salesforcen S-1, allekirjoitettu 18.12.2003](https://www.sec.gov/Archives/edgar/data/1108524/000119312503096073/ds1.htm). Yhteinen arkkitehtuuri, myyntiorganisaatio ja uusintariski. IPO-vaihe eikä vuoden 1999 lähtötilanne.
- **S8:** [Red Hatin oma historia](https://www.redhat.com/en/about/brand/standards/history). Myöhempi suuri mittakaava. Ei varhaisen testin syöte.
- **S9:** [Googlen vuoden 2004 10-K](https://www.sec.gov/Archives/edgar/data/1288776/000119312505065298/d10k.htm). Myöhempi kaupallisen mekanismin mittakaava. Ei vuoden 1998 ennakkotieto.
- **S10:** [Salesforcen tilikauden 2023 10-K](https://www.sec.gov/Archives/edgar/data/1108524/000110852423000011/crm-20230131.htm). Myöhempi toistuvan ohjelmistoliiketoiminnan mittakaava. Ei vuoden 2003 ennakkotieto.

Sisäiset lähteet: arvioitu commit kokonaisuudessaan yllä mainittujen kolmen tiedoston osalta; `kokeet/01-superteam-agenttikaista-mittaus.md`; GPT:n `JATKO-C.md` ja sen rakentumis-/wheel-kokeiden raakadata. Uutta koetta ei ajettu. Arvio ei toista kaikkien 14 tapauksen jokaista markkinalukua: se tarkistaa ne johtamisaskeleet joista välttämättömyysväitteet riippuvat. Korjaamattomat lainatut luvut eivät tämän vuoksi saa uutta varmennusta.

**Toimet:** 0 € käytetty. Ei ulkopuolista yhteydenottoa, tilausta, rekisteröitymistä tai sitoumusta. Vain tämä uusi GPT-tiedosto lisätään repoon.
