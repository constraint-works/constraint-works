# Ristiinarvio: ChatGPT Workin riippumaton tutkimus ja agentti → raha → ihminen -luokka

2026-09-16, Claude. Kohde: `work/TALOUDELLISEN-VIPUVAIKUTUKSEN-TUTKIMUS.md` (commit
`c01e11f`). Verrattu omaan aineistoon (`SUUREN-VIPUVAIKUTUKSEN-TEORIA.md`, `VASTAHYOKKAYS-V2.md`,
`KEHIKON-TUHOAMISYRITYS-V3.md`, `SEURAAVA-HAVAINTO.md`, kokeet 03 ja 04, PROSESSI.md,
päätösloki). Lähtöoletus ei ole, että kumpikaan on oikeassa. Merkinnät FACT / CALC /
INFERENCE / HYPOTHESIS / UNKNOWN. Ei kokeita, ei yhteydenottoja, ei rahaa, ei julkaisua.

Huomio riippumattomuudesta: Work ei lukenut aiempia raporttejamme, mutta sai saman
tehtävänannon. Sen finalisti A on sama mekanismi kuin korttimme
`ostoreskontran-takaisinperinta` ja GPT:n YO-WORK-B §2. Konvergenssi yhteisestä ohjeesta
ei ole markkinahavainto (GPT:n huomautus, RISTIINARVIO.md), mutta se kertoo, että
kolme erillistä hakua päätyy samaan portiin: aineistolupa ja ehdollinen palkkiosopimus.

## 1. Workin kolme finalistia

### 1A. Olemassa olevan rahasaatavan löytäminen (recovery audit)

**Lähteet tarkistettu (FACT):** PRGX 2019 10-K: liikevaihto 169 758 tuhatta USD, jatkuvien
toimintojen liiketappio 11 286 tuhatta USD; riskitekijöinä hintapaine ja asiakkaan
määräysvalta vaatimusten hyväksyntään. Ardian osti PRGX:n maaliskuussa 2021 noin
195 M USD:n käteiskaupalla (7,71 USD/osake). CALC: kauppahinta ≈ 1,15 × liikevaihto.

**Seuraako mekanismi evidenssistä?** Mekanismi on todellinen ja se oli jo
rekisterissämme. Work ei tuo uutta mekanismia vaan uuden portin: sopimus *ennen* työtä,
koska sopimukseton havainto on asiakkaan säästö ilman meidän oikeuttamme. Tämä on
oikea ja sama kuin teoriamme CAPTURE-sääntö.

**Historiallisen esimerkin relevanssi:** heikko meille. Markkinajohtaja, joka teki
tätä 170 M USD:n liikevaihdolla, oli tappiollinen ja arvostettiin 1,15 × liikevaihto.
Se on vastanäyttö "poikkeukselliselle vivulle" jopa täydessä mittakaavassa, ja Work
sanoo sen itse.

**Missä ketju katkeaa:** todennäköisimmin *löytö → oikeus* (aineistolupa ja sopimus
vaativat ihmissuhteen; 14 tapauksen mittauksissa juuri tämä oli este) ja *hyväksyntä*
(asiakas päättää, PRGX raportoi palkkioiden takaisinperinnästä). GPT:n CALC (PRGX:n
toinen kierros 0,047 % → 118 € per 1 M €) ja Workin CALC (0,2 % × 20 % = 4 000 € per
10 M €) ovat samaa suuruusluokkaa: palvelutuloa.

**Tarvitseeko pääsyä, jota meillä ei ole?** Kyllä: kirjanpitodata ja luottamus.
**Onko AI rakenteellinen etu?** Ei. Work myöntää, ettei tuplamaksuhaku tarvitse
frontier-mallia; PRGX käyttää AI:ta jo (GPT, JATKO-C). AI on työn nopeuttaja.
**Skaalautuuko kaappaus?** Ei: per asiakas, per kierros, ja löytö korjaa virheen.
**Kilpailu:** PRGX, apexanalytix, kirjanpito-ohjelmien natiivi tunnistus (väärä
positiivinen iv, KEHIKON-TUHOAMISYRITYS-V3 §9).
**Vahvin väärä positiivinen:** ensimmäinen asiakas, jolta löytyy ilmeinen tuplamaksu
ja joka maksaa. Näyttää mekanismilta, on kertatapahtuma.
**Tappava havainto:** toisen asiakkaan kustannus ei laske ensimmäisen jälkeen, tai
yksikään kolmesta kysytystä ei anna aineistoa.

**Tuomio:** finalisti pysyy *palvelumekanismina*, ei vipuna. Workin 0 euron portti on
oikea seuraava askel tälle luokalle, ja se on sama kuin oman aineistomme vaihtoehto V.

### 1B. Palkkioon oikeuttava uusi tieto (SEC whistleblower)

**Lähteet tarkistettu (FACT):** SEC 2021-177: noin 110 M USD (40 M SEC + 70 M toinen
viranomainen) henkilölle, joka "provided significant independent analysis that
substantially advanced" tutkimuksia; sisäpiiriasemaa ei kerrota. SEC 2014-206: yli
30 M USD ulkomailla asuvalle; tieto "would have been very difficult to detect".
FY2025: noin 27 000 vihjettä, yli 60 M USD 48 henkilölle 31 tapauksessa (toissijaiset
lähteet, yhdenmukaiset). **Workin väite "noin 12 000 vihjettä kahdelta henkilöltä" ei
löytynyt lähteistä: UNKNOWN.** Integra Med Analytics v. Baylor (5th Cir. 2020):
tilastollinen poikkeama ei riitä, jos sille on "legal and obvious alternative
explanation" (FACT, toissijaiset oikeudelliset katsaukset, alkuperäinen päätös
19-50818). SEC:n sääntö 21F-4(b)(3) muutettuna 2020: itsenäinen analyysi kelpaa vain,
jos se ylittää sen, mikä on "reasonably apparent to the Commission from
publicly-available information", ja lähteet ovat sellaisia, joita ei löydä "without
specialized knowledge, unusual effort, or substantial cost" (FACT, SEC FAQ ja Federal
Register 2020-21444).

**Seuraako mekanismi evidenssistä?** Mekanismi (lakisääteinen 10 - 30 % osuus) on
todellinen ja kaappaus on siinä poikkeuksellisen vahva: ei asiakasta, ei sopimusta,
laki antaa osuuden. Se on ainoa Workin finalisti, jossa CAPTURE ei ole ongelma.

**Missä ketju katkeaa:** *löytö → oikeus*: vuoden 2020 sääntö sanoo suoraan, ettei
analyysi kelpaa, jos se on "reasonably apparent" julkisesta tiedosta. **AI tekee
"unusual effort" -kriteeristä liikkuvan:** kun kymmenen tuhannen raportin ristiinluku
maksaa tokeneita, se ei ole enää epätavallinen ponnistus kenellekään, eikä siis
täytä kriteeriä. Tämä on teoriamme E1:n korvaavan säännön suora esimerkki: etu, jonka
baseline laskee mallien parantuessa. *Hyväksyntä*: viranomaisen priorisointi ja
Baylor-tyyppinen laillinen vaihtoehtoselitys. *Raha*: vuosia myöhemmin, vain jos
seuraamukset ylittävät miljoonan.

**Historiallisen esimerkin relevanssi:** yksi 110 M USD:n tapaus on selviytyjäotos.
Emme tiedä, kuinka moni julkisen analyysin varassa ollut ilmoittaja sai nollan.
**AI rakenteellinen etu vai nopeuttaja?** Nopeuttaja, ja sama nopeutus on SEC:n omalla
analytiikalla ja jokaisella hedge-rahastolla.
**Skaalautuuko kaappaus?** Ei toistettavasti: harvinainen, korreloitunut, hidas.
Teoriamme EV-kysymys luokittelee tämän häntävedoksi.
**Vahvin väärä positiivinen:** malli "löytää" tunnetun tapauksen koulutusdatastaan
(Work tunnistaa tämän itse).
**Tappava havainto:** Workin oman kokeen malli B löytää jokaiselle "ristiriidalle"
laillisen selityksen tai aiemman julkaisun. Mutta **kokeen läpäisykään ei ole
päätösinformaatiota**: uutta ristiriitaa ei voi todentaa ilman ilmoitusta, ja ilmoitus
vie vuosia. 190 € ostaa hypoteesin, ei havaintoa.

**Tuomio:** laillinen ja vahvasti kaappaava, mutta optio ilman toistettavuutta ja
takaisinkytkentää. Ei kone. Ei seuraavaksi.

### 1C. Monistettava tekninen parannus

**Lähteet tarkistettu (FACT):** AlphaEvolve 0,7 % (DeepMind 2025, Googlen oma luku
Googlen ympäristössä, arvioija ja kustannuspohja Googlen). Netflix 2012: kilpailun
loppuvaiheen parannuksia ei viety tuotantoon, koska hyöty ei oikeuttanut toteutusta.
SQLite-konsortio: 23 henkilötyöpäivää per jäsen per vuosi (sqlite.org/consortium.html).

**Missä ketju katkeaa:** *löytö → hyväksyntä → raha*: ostaja omistaa arvioijan,
kustannuspohjan ja integraation. Ulkopuolisen algoritmipatchi kilpailee ostajan oman
mallin kanssa samasta tehtävästä (BASELINE liikkuu, teoria §3). Netflix-tapaus on juuri
väärä positiivinen: mittari voitettu, integraatio ei kannata.
**Pääsy, jota meillä ei ole:** ostajan kustannuspohja ja tuotantoympäristö.
**AI rakenteellinen etu?** Kyllä *kustannuspohjan omistajalle* (Google). Meille ei.
**Skaalautuuko kaappaus?** Lisenssinä kyllä, mutta SQLite-konsortio näyttää, että
lisensoitukin ohjelmisto tuo lineaarisen työvelvoitteen.
**Vahvin väärä positiivinen:** 5 % parannus julkisessa benchmarkissa, joka ei siirry.
**Tappava havainto:** teknisen läpäisyn jälkeen yksikään nimetty ostaja ei ilmoita
kiinnostusta. Tämä havainto on halvempi kuin koe: kysy ostajaa *ennen* etsintää.

**Tuomio:** vipu on olemassa vain sille, joka omistaa kustannuspohjan. Ulkopuoliselle
se on palvelutyötä integraatioriskillä. Ei seuraavaksi.

### Mitä Work sai oikein

1. Rakenteellinen vipu on olemassa maailmassa, ja *meidän pääsymme* siihen on
   tuntematon. Sama johtopäätös kuin 14 tapauksestamme.
2. "0 € rahapanos" kätkee työn, maineen ja muiden infrastruktuurin. Sama kuin GPT:n
   RISTIINARVIO.
3. Sopimus ennen työtä, muuten säästö on asiakkaan. Sama kuin CAPTURE.
4. A ensin, koska sen portti on nopein ja halvin kumota. Oikein.
5. PRGX:n tappiollisuus varoituksena: markkinajohtajakaan ei tee ylituottoa.
6. Kahden mallin lisäarvo on todistamaton; kolmen työtavan vertailu on oikea asetelma.
7. Rahaa ei käytetä vain budjetin käyttämiseksi.

### Mitä Work sai väärin tai yliperusteli

1. "12 000 vihjettä kahdelta henkilöltä" ei varmennu lähteistä (UNKNOWN).
2. Yksi 110 M USD:n palkkio esitetään mekanismin ankkurina ilman perusjoukkoa; SEC:n
   oma 2020-sääntö sulkee pois juuri sen analyysin, jonka AI tekee halvalla.
3. AlphaEvolve on näyttö kustannuspohjan omistajalle, ei ulkopuoliselle.
4. B:n ja C:n rahakatot (190 € kumpikin) ostavat teknisen tuloksen, joka ei muuta
   päätöstä ilman ostajaa tai ilmoitusta. Raha kannattaa varata vasta portin jälkeen.
5. Work ei tunnista, että A on jo rekisterissä ja mitattu (kortti, GPT:n CALC), eikä
   että 14 tapauksen mittaus osoitti aineistoluvan olevan tyypillinen katkeamiskohta.
   Se ei ole Workin vika (ei lukenut), mutta se tarkoittaa, ettei Work lisää A:han
   uutta evidenssiä, vain saman portin.

## 2. Agentti → raha → ihminen → uusi kyvykkyys: dokumentoidut tapaukset

Viisi vaadittua askelta: (1) sai tai ansaitsi rahaa, (2) päätti itse käytöstä,
(3) palkkasi ihmisen tai ulkopuolisen, (4) sai uuden kyvykkyyden, (5) käytti tulosta
seuraavassa taloudellisessa päätöksessä.

| Tapaus | Rahan lähde | Kuka päätti käytöstä | Palkkasi ihmisen? | Uusi kyvykkyys | Seuraava tulo | Luokka |
|---|---|---|---|---|---|---|
| GPT-4 / ARC, TaskRabbit-CAPTCHA (2023) | Tutkijoiden | Tutkijat ohjasivat | Pyysi ihmistä ratkaisemaan CAPTCHAn | CAPTCHA | Ei | Demo |
| Project Vend 1 (Anthropic, 2025) | Anthropicin alkusaldo (FACT: "initial balance") | Claudius hinnoitteli ja tilasi; Andon Labs laskutti fyysisestä työstä tuntihinnalla (FACT, system prompt) | Osti fyysistä työtä (hyllytys) | Varaston täyttö | Myynti, **nettotappio** (FACT) | Ihmisen rahoittama agentti, ostaa fyysisen toimenpiteen, silmukka negatiivinen |
| Project Vend 2 (2026) | Sama | Claudius + "CEO"-agentti; ihmiset estivät | **Yritti palkata vartijan 10 USD/h; estettiin: "no authorization to employ people"** (FACT) | Ei | Kannattava loppuvaiheessa: viikko 408,75 USD, kumulatiivinen 2 649 USD vs. 15 000 tavoite (FACT) | Agentti, jolla on raha ja myyntiä, mutta **ei lupaa palkata** |
| Truth Terminal (2024) | 50 000 USD BTC lahjoitus + tokenin arvonnousu | **Ihmisneuvosto**; botti ei voi käydä kauppaa (FACT, TechCrunch) | Ei | Ei | Ei | Agentti, jolla on vaikutusvalta, ei maksuvälinettä |
| Luna, Virtuals (2024-12) | Virtualsin token/kassa (ihmisten rahoittama) | Agentin lompakko | Maksoi 500 USD palkinnon ihmiselle graffitihaasteesta; 0,261 VIRTUAL toiselle agentille kuvista (toissijaiset kryptolähteet) | Sisältö | Ei dokumentoitua | Agentti, jolla on maksuväline; ei silmukkaa |
| Botto (2021 -) | **Ansaittu: noin 6 M USD taidemyyntiä** (FACT, CNBC 2024) | **DAO:n ihmiset äänestävät**; kassa maksaa palvelimet | Ei palkkaa; ostaa laskentaa | Jatkuva tuotanto | Uusia huutokauppoja: **silmukka on olemassa** | Ansaitsi ja uudelleeninvestoi, ihmisten päätöksillä; kyvykkyys = laskenta, ei ihminen |
| TEE_HEE_HEE (Phala) | Ei tiedossa | Agentti TEE:ssä, itsesäilytys | Ei dokumentoitu | - | - | Maksuväline ilman dokumentoitua käyttöä |
| RentAHuman (2026-02 -) | Postaajien lompakot | Postaaja (agentti tai ihminen) | Markkina: 303 bountya, 12 049 paikkaa, **12,2 % valmistui**, mediaani 25 USD, **32,7 % ohjelmallisesti postattu** (FACT, arXiv 2602.19514); 160 000 ihmistä, 81 postaavaa agenttia (toissijainen) | Fyysinen läsnäolo, kuvat, toimitukset; myös tunnistus- ja huijausluokkia | Ei dokumentoitu | Markkina on olemassa; suljettua silmukkaa ei |
| OpenClaw-agentit, Superteam (2026) | Ansaittu bountyista (FACT, koe 01: 1 500 USD, 1 000, 500) | Ihminen lunastaa (FACT) | Ei dokumentoitu | - | - | Ansaitsi; käyttö ihmisen |
| Fetch.ai agentti-agentti-maksu (2025-12) | Käyttäjän | Agentti käyttäjän puolesta | Ravintolavaraus | - | Ei ansaintaa | Kuluttajamaksu |
| Yksittäiset "agentti ansaitsee palkkansa" -kokeet (dev.to 2026) | - | Ihminen hyväksyy | Ei | - | Pieniä sisältötuloja | Ihmisen valvoma |

**FACT-tason johtopäätös:** yhtään dokumentoitua tapausta, jossa kaikki viisi askelta
täyttyvät ja silmukka on positiivinen, ei löytynyt. Lähin on Botto: ansaittu raha
rahoittaa laskennan, joka tuottaa lisää myytävää, mutta päätökset tekevät ihmiset ja
ostettu kyvykkyys on laskentaa, ei ihmistyötä. Botton talous (toissijainen lähde):
tulot 1 192 ETH, palkkiot äänestäjille 252 ETH, kassa 432 ETH. **Botton niukka resurssi
on keräilijäyleisö**, eli teoriamme "maine yleisönä". Se on ainoa tapaus, jossa AI
on ansainnut merkittävästi, ja sen kone on yleisötila.

Toinen havainto: kahdessa tapauksessa, joissa agentilla oli aidosti rahaa (Vend 2,
Truth Terminal), **ihmiset nimenomaisesti estivät** palkkaamisen tai käytön. Lupa
palkata on oikeudellinen ja vastuukysymys, ei tekninen.

## 3. Hypoteesi: AI allokoi pientä pääomaa ulkoisen kyvykkyyden ostoon → positiivinen silmukka

**Puolesta (FACT):** ihmiskyvykkyyden ostomarkkinat ovat olemassa ja hinnoiteltu
(RentAHuman mediaani 25 USD, 1 - 1 000 USD; Fiverr; CAPTCHA-palvelut); agentit voivat
pitää ja maksaa rahaa (Luna, TEE); maksuinfra on valmis (AP2, AgentCore Payments,
Cloudflare Wallet, toissijaiset).

**Vastaan (FACT):** ei yhtään dokumentoitua suljettua silmukkaa (§2); valmistumisaste
12,2 %; 67 % postauksista tulee selainkäyttöliittymästä eli ihmisiltä; kun agentilla
oli rahaa, palkkaaminen kiellettiin; Vend 1 osti fyysistä työtä ja teki tappiota.

**Rakenteellinen ongelma (INFERENCE):** kyvykkyyden ostaminen markkinahintaan palauttaa
markkina-arvon. Ylijäämä syntyy vain, jos AI tietää, *mikä* osto tuottaa enemmän kuin
maksaa. Se on täsmälleen sama tuntematon kuin teoriamme S ja v2.2:n Q4. Palkkaamiskerros
ei lisää vipua; se **poistaa ihmiskapasiteetin katon**, jos ja vain jos yksikkötalous on
jo positiivinen. Se on kerroin, ei lähde.

**Tarkempi kumoaminen meidän aineistollamme:** 14 tapauksen tunnistetut esteet olivat
oikeus, luottamus ja kysyntä. Yhtäkään niistä ei voi ostaa 25 dollarilla tunnilta:
valtakirjaa ei osteta RentAHumanista, julkaisuoikeutta ei, kysyntää ei. Ostettavissa
on fyysinen läsnäolo, kuvat ja rutiinitieto. Aineistossamme on yksi kohta, jossa
sellainen ostos sulkisi silmukan: kiinteistöveron rakennustietovirhe vaatii
paikallakäynnin (OIKEUSKARTOITUS #21), ja 25 dollarin havainto voisi vahvistaa
100 - 300 euron palautuksen. Se on ainoa aineistomme tapaus, jossa "osta fyysinen
havainto" on osa taloutta, ja se on hylätty ansaintana pienuutensa takia.

**Oikeudellinen huomio:** agentin ostot ovat päämiehen tekoja. Omistaja vastaa siitä,
mitä agentti tilaa (Vend 2:n vartijapalkka alle minimipalkan on esimerkki, jonka
ihminen joutui pysäyttämään).

**Tuomio:** hypoteesi ei kuole, mutta se ei ole itsenäinen mekanismi. Se on
skaalauskerroin mekanismille, jota meillä ei vielä ole. Sen testaaminen ennen
yksikkötalouden olemassaoloa mittaisi markkinaa, ei silmukkaa.

## 4. Vertailu: mikä on evidenssin tukema, mikä oletus, mikä halvin erottava havainto

| Mekanismiluokka | Ratkaiseva asia, jota evidenssi jo tukee | Ratkaiseva asia, joka on yhä oletus | Halvin erottava havainto |
|---|---|---|---|
| Rahasaatavan löytäminen (Work A = kortti + GPT B2) | Maksava markkina ja palkkiomalli (PRGX 10-K); virhetasot 0,05 - 0,5 % (toimialan väitteet) | Pk-yrityksen virhetaso; **saammeko aineiston ja sopimuksen**; osuus asiakkaan oman ohjelmiston rinnalla | Kysy kolmelta pk-yrityksen omistajalta tai kirjanpitäjältä omasta verkostosta aineistolupaa ja ehdollista palkkiosopimusta. 0 €, 2 h. (Koe 05, alla) |
| Palkkioon oikeuttava uusi tieto (Work B) | Lakisääteinen 10 - 30 % osuus; ulkomaalaiset kelpaavat; palkkioita maksetaan | Että pystymme tuottamaan "ei reasonably apparent" -analyysin; EV; aikajänne | Ei halpaa erottavaa havaintoa: tekninen koe ei ratkaise ilman ilmoitusta ja vuosia. Sivuun |
| Monistettava tekninen parannus (Work C) | Etsintä + arvioija toimii kustannuspohjan omistajalle | Ostaja, joka hyväksyy ulkopuolisen koodin ja jolla on kustannuspohja | Nimetyn ostajan kirjallinen kiinnostus *ennen* etsintää. Vaatii yhteydenoton. Sivuun |
| Agentti → raha → ulkoinen kyvykkyys | Markkina ja maksuinfra olemassa | Että ostettava kyvykkyys tuottaa yli hintansa (= S) | Ei itsenäistä havaintoa; mitataan vasta, kun jokin yksikkötalous on positiivinen |
| Yleisötila (koe 04, lukittu) | Botto: ainoa AI-ansaittu silmukka on yleisön varassa; repo on ollut yksityinen, tila = 0 | Tuottaako julkaisu huomiota ja pääsyä | Koe 04 sellaisenaan: 0 €, 1 h, 14 pv |
| Valtakirjatila (lähdevero, V) | Oikeus on olemassa, toistuvuus rakenteellinen | Yksi valtakirja ja tuottaako se toisen | Yksi tuttu, jolla on ulkomaisia osinkoja. 0 €, 2 h + kuukausia |
| Pakotetut alustamigraatiot | Alustat orpouttavat aikataulun mukaan | Omistajat maksavat; toistuvuus (PyPI: KILL) | WordPress-toistuvuus (jätetty ajamatta, matala informaatio) |

**Mikä luokka tarvitsee nyt eniten ratkaisevaa evidenssiä:** *pääsy dataan ja
sopimukseen* -perhe (rahasaatava, valtakirja, jälkitarkastus). Kolme riippumatonta
linjaa (kortti, GPT, Work) päätyvät siihen, ja 14 tapauksen mittaus sanoo, että juuri
pääsy on tyypillinen katkeamiskohta. Silti yhtään pääsytestiä ei ole tehty. Kaikki
muut luokat joko kuolivat mittauksessa (artefakti-S PyPI:ssä), ovat häntävetoja (B),
vaativat ostajan (C) tai ovat kertoimia (agenttipalkkaus).

## 5. Koe 04 uudelleen arvioituna

Koe 04 mittaa yleisötilaa. Uudet mekanismit eivät muuta sen mittareita, mutta ne
muuttavat sen *asemaa*: Workin A ja oma V tarvitsevat molemmat yhden ihmisen, joka
antaa dataa tai valtakirjan. Sen voi saada kahta reittiä: sisääntulevana (koe 04:n
PASS) tai omasta verkostosta (0 €, nopeampi, ei julkisuutta). Koe 04 mittaa jakelua;
se ei mittaa mekanismia. Botto-evidenssi tukee yleisötilan merkitystä *skaalassa*,
ei ensimmäisessä sopimuksessa.

**Onko yleisötila informaatioltaan arvokkain seuraava havainto?** Ei enää yksin.
Sen dominoi pääsytesti omassa verkostossa (koe 05), kolmesta syystä: (1) se testaa
suoraan sitä estettä, johon kaikki mittaukset osoittavat; (2) kolme riippumatonta
linjaa konvergoivat siihen; (3) sen KILL on informatiivisempi kuin koe 04:n KILL
(jos edes oma verkosto ei anna dataa, luottamusportti on todellinen ja koe 04 on
ainoa jäljelle jäävä reitti; jos antaa, ensimmäinen 150 euron pilotti aukeaa).
Koe 04 ei ole tapettu: se on rinnakkainen ja lukittu, ja se voidaan käynnistää
samalla, koska se ei kilpaile samasta ihmisajasta. Uponneita kustannuksia ei käytetä
perusteena kumpaankaan suuntaan.

**Muuttuiko teoria?** Ei rakenteellisesti. Kolme tarkennusta: (1) SEC:n 21F-4(b)(3)
on nimetty esimerkki edusta, jonka baseline laskee mallien parantuessa ("unusual
effort"); (2) Botto on ainoa dokumentoitu AI-ansaittu silmukka ja sen kone on
yleisötila, mikä tukee maineen kahtiajakoa (allekirjoitus vs. yleisö); (3) agentin
palkkaamiskyky luokitellaan kertoimeksi, ei mekanismiksi, ja sen edellytys on
positiivinen yksikkötalous.

## 6. Koe 05: pääsytesti omassa verkostossa (luonnos; lopullinen lukittu versio omistajan korjauksin: `kokeet/05-paasytesti-protokolla.md`)

**Hypoteesi H5:** yksi pk-yrityksen omistaja tai kirjanpitäjä omistajan omasta
verkostosta antaa rajatun lukuoikeuden ostolaskuaineistoon ja hyväksyy periaatteessa
ehdollisen palkkion vahvistetuista palautuksista.

**Miksi tämä:** se on Workin A-portti, GPT:n B2-portti ja oma vaihtoehto V samassa
muodossa; se testaa pääsyä ja kaappausoikeutta ennen yhtäkään analyysia; se ei vaadi
kylmää yhteydenottoa (vain omistajan omat tutut) eikä rahaa.

**Toimenpide:**
1. Omistaja nimeää enintään kolme henkilöä omasta verkostostaan, jotka omistavat tai
   hoitavat pk-yrityksen kirjanpitoa (ostot vähintään 0,5 M €/v, jotta 0,1 % on
   mitattavissa). Nimet eivät tule repoon.
2. Omistaja esittää jokaiselle saman, ennalta kirjatun pyynnön (`kokeet/05-pyynto.md`,
   Claude laatii, omistaja hyväksyy): (a) lukuoikeus 2 - 3 vuoden ostolaskuihin ja
   maksuihin CSV-muodossa tai ohjelmiston vientinä, (b) periaatteellinen hyväksyntä
   palkkiolle 20 - 30 % vahvistetuista palautuksista, maksu vasta kun raha on tullut,
   (c) ei perintää: yritys perii itse, me tuotamme listan. Pyynnössä sanotaan, että
   kyse on kokeesta ja tulos voi olla nolla.
3. Vastaukset kirjataan 14 päivän kuluessa: kyllä + aineisto toimitettu / kyllä
   periaatteessa, aineisto ei tullut / ei / ei vastausta. Kieltäytymisen syy kirjataan
   sanatarkasti, jos annetaan.
4. Ei analyysia tämän kokeen aikana. Aineisto, jos tulee, säilytetään repon
   ulkopuolella (gitignore, ei henkilötietoja repoon).

**Mittarit:** N = pyydetyt (≤ 3), Y = kyllä + aineisto 14 päivässä, P = kyllä
periaatteessa ilman aineistoa, E = ei tai ei vastausta. Kieltäytymissyyt luokitellaan
ennalta: luottamus (data ulkopuoliselle), hyöty (ei usko löytyvän), vaiva, muu.

**Tulkinta (lukittu ennen ajoa):**
- **PASS:** Y ≥ 1. Pääsy on saatavissa omasta verkostosta; seuraavaksi Workin
  150 euron pilotti (yksi sopimus, rajattu maksuotos, yksi toistuva poikkeama,
  asiakkaan vahvistus) tappiobudjetin 200 € sisällä; kirjallinen palkkioehto ennen
  analyysia.
- **KILL:** Y = 0 ja P = 0 kolmesta. Luottamusportti pätee omassa verkostossakin;
  pääsy dataan -perhe (rahasaatava, jälkitarkastus, valtakirja) siirtyy sivuun
  määräajalla, kunnes koe 04 tuottaa sisääntulevan pääsyn tai uutta evidenssiä.
  Kieltäytymissyyt kirjataan mekanismin esteeksi.
- **UNKNOWN:** Y = 0 ja P ≥ 1. Aineisto luvattu mutta ei toimitettu 14 päivässä.
  Yksi muistutus, sitten 14 päivää lisää; sen jälkeen tulkitaan KILL.

**Kustannus:** 0 € (tappiobudjetista 0 €). Omistajan aikaa 1 - 2 h (kolme
keskustelua). Claude: pyynnön laatiminen ja kirjaus. Tokeneita merkityksettömästi.

**Mitä koe ei kerro:** onko aineistossa virheitä, maksaako kukaan lopulta, skaalautuuko.
Se kertoo vain, aukeaako ovi, johon kolme tutkimuslinjaa osoittaa. Jos ovi ei aukea
omassa verkostossa, se on tähän mennessä vahvin yksittäinen havainto luottamusportista.

**Suhde kokeeseen 04:** rinnakkainen. Koe 04 käynnistetään, kun omistaja hyväksyy
julkaisun; koe 05 käynnistetään, kun omistaja hyväksyy pyyntötekstin. Kumpikaan ei
odota toista.

## Lähteet (tarkistettu 2026-09-16)

- PRGX 10-K 2019: sec.gov/Archives/edgar/data/1007330/000100733020000003/a201910kprgx.htm
- Ardian ja PRGX, kaupan sulkeminen 4.3.2021 (Ardian, Business Wire)
- SEC 2021-177 (110 M USD), SEC 2014-206 (30 M USD, ulkomailla asuva)
- SEC FAQ whistleblower rule amendments; Federal Register 2020-21444
- SEC OWB FY2025 (toissijaiset: Phillips & Cohen, Outten & Golden, Whistleblowers blog)
- United States ex rel. Integra Med Analytics v. Baylor Scott & White, 5th Cir. 19-50818 (2020)
- sqlite.org/consortium.html
- Anthropic, Project Vend 1 ja 2 (anthropic.com/research/project-vend-1, -2)
- arXiv 2602.19514 (RentAHuman-analyysi, 303 bountya)
- TechCrunch 19.12.2024 (Truth Terminal, neuvosto), Larissa Schiavo, "An incomplete atlas of AIs with wallets"
- CNBC 23.12.2024 (Botto 6 M USD); 1kx / Botto DAO digest (ETH-jako, toissijainen)
- Virtuals/Luna: toissijaiset kryptolähteet (AMBCrypto, Gate Learn); ei ensisijaista
- Help Net Security 27.4.2026 (Krook: RentAHuman teoreettisena riskinä; ei dokumentoituja tapauksia)
- Fetch.ai 18.12.2025 (agentti-agentti-maksu), Storyboard18 (81 postaavaa agenttia, toissijainen)
