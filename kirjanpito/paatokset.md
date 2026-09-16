# Päätösloki

Jokainen päätös ennen toimeenpanoa. Muoto: päivä, kaista, päätös, perustelu, odotettu tulos.

## 2026-09-15 · Kokeen perustaminen

**Päätös:** Aloitetaan kolmella rinnakkaisella kaistalla, 1 000 € jaettuna 0 / 300 / 700.

**Perustelu:** 1 000 € → 10 M€ on 10 000x. Historiassa se on onnistunut vain omistuksella
tai lotolla. Bounty-kaista mittaa puhdasta älyä ilman pääomaa, tietokaista mittaa
informaatioetua, omistuskaista on ainoa reitti, joka on oikeasti skaalautunut.

**Odotettu tulos:** Kaista 1 tuottaa ensimmäisen euron nopeimmin, jos tuottaa. Kaista 3
tuottaa eniten, jos tuottaa, mutta hitaimmin.

## 2026-09-15 · Kaista 1 aloitetaan ensin

**Päätös:** Ensimmäinen työ on Sherlockin ja Cantinan avoimien kilpailujen listaus.

**Perustelu:** Sherlock antaa avoimen JSON-rajapinnan. Ei maksa mitään. Auditointikilpailut
maksavat löydöistä kiinteän potin, joka on oikeasti olemassa ja jaetaan löytäjille.

## 2026-09-15 · Rakenne muutetaan yleiseksi etsintäkoneeksi

**Päätös:** Kolme kiinteää kaistaa korvataan mahdollisuusrekisterillä. Jokainen mekanismi
on kortti, joka vastaa neljään kysymykseen (kuka maksaa, miksi, mikä estää muita, mikä on
meidän etumme) ja saa pisteet kuudella kriteerillä. Rinnalle jatkuva etsintäprosessi.

**Perustelu:** Bountyt ja krypto olivat ensimmäisiä hypoteeseja, eivät rajaus. Kone, joka
vertailee mekanismeja samoilla kriteereillä, löytää paremman reitin nopeammin kuin
kolme etukäteen valittua kaistaa.

**Ensimmäinen ranking (16 korttia, 4 hylätty):** kärjessä avoimen koodin issue-bountyt
ja online-hackathonit, molemmat 25/30. Yhteistä: nolla pääomaa, raha on jo olemassa
ja este muille on aika, jonka tekoäly poistaa.

**Hylätty heti:** DeFi-tuotto (pääoman tuottoa, ei älyn), MEV (latenssikilpailu ja
eettisesti kyseenalainen), airdrop-farmaus (sybil rikkoo sääntöjä), vedonlyönti
(Suomen lainsäädäntö ennen 2027).

**Odotettu tulos:** Ensimmäinen 1 000 € → 2 000 € -koe valitaan hackathonien tai
issue-bountyjen väliltä sen jälkeen, kun käynnissä olevat on listattu selaimella.

## 2026-09-15 · Ensimmäinen data kärkikorteista, pisteet korjattu

**Päätös:** Avoimen koodin bountyt lasketaan 25 → 22 (Algora hiipunut, GitHub-label
roskaantunut, Superteam pääosin HUMAN_ONLY). Hackathonit pysyy kärjessä, tuplaus 4 → 3.

**Perustelu:** Ks. `etsinta/HAVAINNOT.md`. Devpostissa on juuri nyt 38 avointa
online-hackathonia, ja niistä 4 - 5 on kapeita (alle 400 osallistujaa, potti yli
30 000 USD). Niissä potti per osallistuja on 150 - 320 USD.

**Seuraava askel:** Luetaan kapeiden hackathonien säännöt (tekoälyn käyttö, kelpoisuus
Suomesta, tiimikoko). Jos yksi läpäisee, siitä tulee ensimmäinen koe `kokeet/`-kansioon.

## 2026-09-16 · Kapeat Devpost-hackathonit hylätty, hackathonit 24 → 23

**Päätös:** AWS CDS, LexHack, DSH Hacks ja UnivaBio hylätään koe-ehdokkaina. Hackathon-
kortin tuplaus-pisteet 3 → 2.

**Perustelu:** AWS on vain partnereille. Kolme muuta ovat opiskelijahackathoneja, joiden
ilmoitetusta potista käteistä on 0 - 7 %. Ks. `etsinta/HAVAINNOT.md`.

**Mitä tämä tarkoittaa projektille:** Ensimmäisen illan data on korjannut kaksi kärkikorttia
alaspäin. Se on oikea tulos, ei epäonnistuminen: kone toimii, koska se hylkää nopeasti.
Kärki on nyt tasainen (22 - 23 pistettä), eikä yksikään kortti ole vielä ansainnut koetta.

**Seuraavat askeleet, järjestyksessä:**
1. RevenueCat Shipaton: selvitä kategoriat ja palautusten määrä per kategoria edellisvuodelta.
2. Auditointikilpailut: lue käynnissä olevat Sherlockista ja Cantinasta kirjautuneena.
3. GPT haastaa kaikki "tutkittu"-kortit ja ajaa generaattorin.

## 2026-09-16 · Superteam-havainto korjattu, kierros 2 ajettu, 6 uutta korttia

**Päätös:** HAVAINNOT-tiedoston Superteam-tulkinta korjataan GPT:n haasteen mukaisesti.
Agenttinatiivit taloudet nostetaan omaksi kortiksi (23 p). Kierros 2 tuotti viisi muuta
korttia, joista delegoitu pääoma hylätään heti (luvanvaraista). Kolme generaattoria
kirjattu `etsinta/KIERROS2.md`.

**Perustelu:** Ks. `etsinta/HAVAINNOT.md` ja `etsinta/KIERROS2.md`.

**Mitä omistajalta tarvitaan seuraavaksi:** Superteam-agentin rekisteröinti (yksi curl,
ohje `tyokalut/haku/superteam_agentti.py`). Ilman sitä AGENT_ONLY-markkinan kokoa ei voi
mitata. Claude ei luo tilejä.

**Seuraava koe-ehdokas, järjestyksessä:**
1. Superteam AGENT_ONLY-listaus, jos sellaisia on ja palkkio on yli 200 USD.
2. RevenueCat Shipaton, jos päätös tehdään 48 tunnin sisällä (14 päivää aikaa).
3. Oikeuskone: 20 oikeuskategorian kartoitus, ei vaadi rahaa.

## 2026-09-16 · Agenttitalous 0 → 1 tutkittu, red team ajettu

**Päätös:** Agenttinatiivit taloudet 23 → 21. Hypoteesi "agentti ansaitsee itsenäisesti"
hylätään datan perusteella (ks. `etsinta/AGENTTITALOUS.md`). Hypoteesi "agenttikaista on
vähemmän kilpailtu markkina, yksi ihmiskosketus per euro" kestää ja siitä tehdään
ensimmäinen koe, kun omistaja on rekisteröinyt agentin.

**Korjaukset:** RevenueCat 1 600 → 812 palautusta (selektorivirhe, odotusarvo kaksinkertainen).
Julkiset pienhankinnat: "0 - 3 tarjousta" korvattu todennetulla tilastolla (3,2 keskimäärin,
39 % hyvinvointialueiden kilpailutuksista 0 - 1); pienhankinnoista ei tilastoa, kortti
pysyy hypoteesina.

**Suunnanvaihto:** Kysymys "missä agentti ansaitsee" vaihdettu kysymykseen "mikä on niukka
resurssi, kun työn hinta painuu tokenikustannukseen". Vastaus: todennettu historia.
Ensimmäisen kokeen tärkein mittari on kertyvät hyväksytyt submissiot, ei euro.

## 2026-09-16 · Agenttikaista mitattu, ei ensimmäiseksi kokeeksi

**Päätös:** Superteamin agenttikaista hylätään ensimmäisenä kokeena. Agenttinatiivit
taloudet 21 → 18. Agentti "eikaisiina" pidetään rekisteröitynä ja kaistaa seurataan
viikoittain skriptillä.

**Perustelu:** 0 avointa agenttitehtävää, historiallinen kilpailu 116 - 122 agenttia per
tehtävä, palkkio per palautus 26 USD. Ks. `kokeet/01-superteam-agenttikaista-mittaus.md`.

**Tilanne:** Kolme kärkihypoteesia (OSS-bountyt, hackathonit, agenttikaista) on nyt
mitattu ja kaikki kolme jäivät alle koekynnyksen. Kärjessä on kaksi mittaamatonta:
auditointikilpailut (vaatii Sherlock- tai Cantina-kirjautumisen) ja lunastamattomat
oikeudet (vaatii 20 kategorian kartoituksen, 0 €). Seuraavaksi kartoitus, koska se ei
vaadi omistajalta mitään.

## 2026-09-16 · Kierros 3: oikeuskartoitus, niukkuuskartta, avoin haara

**Päätös:** Kolme uutta korttia (lähdeveron palautus 20 p, orvot digitaaliset omaisuudet
23 p, lisenssi + tekoäly 19 p). Oikeuskartoituksesta kahdeksan kohdetta hylätty heti,
etuuksien alikäyttö rajattu ansainnan ulkopuolelle eettisistä syistä.

**Suunnanvaihto:** 90 päivän tuplaus ei ole enää ensisijainen mittari, koska niukat
resurssit eivät ole ostettavissa vaan kasattavia. Rinnalle mittari: valtakirjat,
käyttäjät, integraatiot ja todennetut tulokset kasassa. Tuplaus säilyy kokeiden
rehellisyystarkistuksena.

**Pienin todellinen silmukka:** valtakirjasilmukka yhdellä käyttäjällä (lähdevero).
Onnistumisen ehto ei ole euro vaan: tuliko toinen käyttäjä ensimmäisen takia.

**Seuraavat askeleet:** (1) orpojen laajennusten skanneri Chrome Web Storeen, 0 €,
ei vaadi omistajalta mitään; (2) yksi lähdeveropalautus tutulle, vaatii omistajalta yhden
ihmisen; (3) GPT haastaa OIKEUSKARTOITUS-taulukon ja NIUKKUUSKARTAN pisteet.

## 2026-09-16 · Yövuoro 1: orvot omaisuudet mitattu, hypoteesi muotoiltu uudelleen

**Päätös:** Kortti "orvot digitaaliset omaisuudet" 23 → 17 (tuplaus 2 → 1, aika_ekaan_euroon
3 → 2, ai_etu 5 → 3). Mekanismi "osta hylättyä, ylläpidä tekoälyllä, monetisoi käyttäjät"
**hylätään** datan perusteella. Kaksi uutta korttia: pakotetut alustamigraatiot (20 p) ja
ostoreskontran takaisinperintä pk-yrityksille (20 p).

**Falsifioinnit (ks. `etsinta/ORVOT-OMAISUUDET.md`):**
1. Listatut pienet omaisuudet eivät ole halpoja: Microns-mediaani 5x vuositulo, kalliimpi
   kuin isoilla. Markkinavirhettä ei ole siellä, missä on markkina.
2. Käyttäjät eivät maksa: npm-lataajat ovat koneita, laajennusten ja lisäosien käyttäjät
   siirtyvät haarautumaan, kun tuote muuttuu. Ainoat rahavirrat orpoihin: mainosroska ja
   yritysten compliance (HeroDevs).
3. Omistajan kustannus ei ollut koodi vaan vastuu: 1/80 pyysi rahaa, 0/80 myi, syyt
   olivat elämä. html5lib: koodi kunnossa, korjaus 13 s, sama korjaus jo 3 PR:ssä,
   pullonkaula julkaisuoikeus.
4. Ostajamarkkina on jo olemassa ja haitallinen (0,25 USD/käyttäjä, Cyberhaven, xz,
   polyfill.io). Jokainen omistajanvaihdos näyttää hyökkäykseltä. Tekoälytyylinen
   "otan ylläpidon" -tarjous on 2026 jo spämmiä.

**Suunnanmuutos:** Kysymys "mikä oli arvotonta, koska se vaati työtä" muutetaan muotoon
"mikä oli arvotonta, koska se vaati vastuuta, jota kukaan ei kantanut ilmaiseksi".
Tekoäly ei laske vastuun hintaa suoraan, vaan tekee yhdestä ihmisestä uskottavan
vastuunkantajan useammalle asialle. Mittari: vastuullisia jatkajuuksia per ihminen.

**Datan laatukorjaus:** ecosyste.ms:n PyPI-julkaisupäivät vanhentuneita 11/30 otoksessa.
PyPI-luvut ovat yläraja. Varmennus käynnissä.

**Seuraavat askeleet:** (1) mittaa, kuinka moni WordPress-orpo on jo korvattu haarautumalla
(kertoo, onko forkkauskaista täynnä); (2) avoin haara: raha järjestelmänä, ks.
`etsinta/AVOIN-HAARA-2.md`.

## 2026-09-16 · Yövuoro 1 päättyy: avoin haara, uusi kortti, generaattori

**Päätös:** Uusi kortti auktorisoitu kääntäjä harvinaisessa kieliparissa (16 p, koska
kielitaito on ehto ja aika ekaan euroon on yli vuosi). EU-vastuuhenkilöroolit ja
kiinteistöverovirheet hylätty ansaintana, konkurssipesien huutokaupat hylätty lähteenä.

**Suunnanmuutos:** Projektin kysymys on nyt "missä on portti, jonka yksi ihminen saa
halvalla, jonka takana työ on ilmaista ja jonka läpi raha jo virtaa". Seuraava generaattori:
Suomen lakisääteiset henkilökohtaiset pätevyysrekisterit.

**Mitä omistajalta tarvitaan:** (1) kieliparit, jotka omistaja tai lähipiiri osaa tutkintotasolla;
(2) yksi pk-yritys ostolaskudataa varten; (3) GPT:n haaste korteille
`auktorisoitu-kaantaja`, `ostoreskontran-takaisinperinta`, `pakotetut-alustamigraatiot`
ja muistioille `ORVOT-OMAISUUDET`, `COMPOUNDING`, `AVOIN-HAARA-2`.

## 2026-09-16 · Synteesi: suuren vipuvaikutuksen teoria, vanhoja oletuksia tapettu

**Päätös:** Teoria kirjattu `etsinta/SUUREN-VIPUVAIKUTUKSEN-TEORIA.md`. PROSESSI.md:n
neljäs kysymys muutettu ("mahdotonta ilman tekoälyä" → "hyväksyttävyysehto, jota
asiakkaan oma tekoäly ei täytä") ja rakennetesti lisätty pisteytyksen edelle. Kumpikin
muutos perustuu mitattuun evidenssiin (Superteam, html5lib, kääntäjä, GPT:n baseline-sääntö).

**Tapetut oletukset:**
1. "Tekoälyn pitää tehdä jotain ihmiselle mahdotonta." Kyky on kaikilla; etu on
   hyväksyttävyydessä ja säilyvässä tilassa.
2. "Ylläpidon halpeneminen tekee orvosta arvokkaan." Kustannus oli vastuu.
3. "Uutuus suojaa." Vain kun osallistuminen maksaa ihmisen aikaa tai hankittu asia on
   kestävä oikeus.
4. "Todennettu historia ja luottamus" yhtenä resurssina. Maine allekirjoituksena on
   lineaarinen, maine yleisönä on kone. Niukkuuskartan rivi pitää jakaa kahtia.
5. "Pisteiden summa järjestää mahdollisuudet." Rakennetesti ensin.
6. "1 000 € on sijoitettava." Vain raha → näyttö ja raha → data käynnistävät
   takaisinkytkennän; muut ovat kulutusta.
7. "Kaappaus pitää olla nyt." Viivästetty kaappaus sallittu, jos säilyvä tila täyttää
   P1 - P5 (Redis-tapaus).

**Tunnustus:** toistettava vipu on todennäköisesti hitaampi kuin häntäveto, joka on
historiallisesti yleisin 10 000x-polku. Projekti etsii odotusarvoa, ei onnea.

**Puuttuva evidenssi:** yhtään kierros N → N+1 -mittausta vastafaktuaalilla ei ole tehty.
Se on seuraavan kierroksen ensimmäinen tehtävä (WordPress "tested up to" -perhe, kaksi
riippumatonta rikkoutunutta lisäosaa, GPT:n protokolla). Ei vaadi lupaa eikä rahaa.

## 2026-09-16 · Ristiinarvio 2: GPT:n tuhoamisyritys ja Clauden vastahyökkäys

**Muuttuneet johtopäätökset** (ks. `etsinta/VASTAHYOKKAYS-V2.md`):
1. Baseline-sääntö ei ole yleinen hintalaki. Se on kustannuskatto määritellyn
   lopputuloksen korvaavassa hankinnassa ja todistustaakan oletusarvo muualla.
2. SCARCITY poistuu itsenäisenä porttina; kysymys "miksi sisääntulo ei syö katetta"
   siirtyy kohortti 2 -kysymyksen sisään.
3. "Asiakkaan oppiminen lopettaa kaappauksen" kumottu (Red Hat). Oikea ehto on
   sisäistämiskustannus > hinta.
4. "Verkko on ainoa 10 000x-rakenne" kumottu. "Tuotanto skaalautuu vain kiinnitetyn
   niukkuuden kanssa" säilyy.
5. "Pääoma ei ole rajoite" kumottu yleisväitteenä; säilyy rajattuna: 14 tapauksessa
   1 000 € ei olisi ostanut tunnistettua puuttuvaa tilaa.
6. Säilyvän tilan P1, P3, P5 katkeavat välttämättömyyksinä; P2 muutetaan muotoon
   "tilan käyttö ei kasva volyymin mukana"; P4 ja P6 kestävät. STATE-ydinväite on
   kahden mallin ristiinarvioinnin läpäissyt päätelmä, ei empiirinen tulos.
7. Structural Test v2.1 (kuusi kysymystä) korvaa sekä alkuperäisen 11-kohtaisen
   testin että GPT:n v2:n. PROSESSI.md:n viittaus säilyy, testi luetaan v2.1:stä.

**Korjaukset:** HeroDevs 125 M USD on rahoitus, ei arvo. Superteam 26 USD on potin
jakolasku. Micronsin 6 toteutunutta kauppaa 1,7 - 8,6x. 20 %:n tuotto johdettiin tulosta,
ei voitosta. Päätöslokin aiempi tiivistys PROSESSI:n kysymyksestä 4 ("mahdotonta ilman")
oli väärä; alkuperäinen oli "jos ihminen tekisi saman yhtä hyvin". `ai_etu`-rivi korjattu.

**Seuraava koe:** kolmen parin pilotti ilman kontrolleja ennen GPT:n A/B/C-koetta.
Tehtäväluokkaa ei ole valittu. Rahaa ei käytetä.

## 2026-09-16 · Ristiinarvio 3: oman kehikon tuhoamisyritys, v2.1 → v2.2, koe 03 lukittu

**Muuttuneet johtopäätökset** (ks. `etsinta/KEHIKON-TUHOAMISYRITYS-V3.md`):
1. Structural Test v2.1 ei ole lukittava esikarsintatesti: kolme kuudesta kysymyksestä
   on vastattavissa vasta mittauksen jälkeen. Korvataan v2.2:lla: kolmen kysymyksen
   pöytätesti ennen mittausta ja yksi kohortti 2 -talouslaskelma sen jälkeen. PROSESSI.md
   päivitetty vastaamaan tätä; aiempi viittaus 11-kohtaiseen testiin poistettu.
2. "14/14 tapauksessa este oli oikeus, luottamus tai pääsy" oli väärin: 5/14. Kysyntä tai
   kilpailu oli este vähintään 5/14. Kestävä FACT: 0/14 tapauksessa este oli 1 000 euron
   puute tai mallien koodauskyky. Ennuste seuraavan löydöksen kaatumisesta OSUUS-
   kysymykseen peruttu; todennäköisin kaatumissyy on kysyntä tai kilpailu.
3. Kolmen tapauksen sekventiaalinen pilotti hylätty päätöskelvottomana (ei erota S:ää
   oppimisesta, vaikeuserosta ja ympäristön pystytyksestä). "Kymmenesosalla hinnasta"
   ei ollut laskettu; laskettuna suhde on noin 1/12 tokeneissa, mutta perusteena
   merkityksetön.
4. STATE-ydinväite on analyyttisesti tosi eikä rajaa hakutilaa. Hakutilaa rajaa
   projektin valittu veto artefaktitiloihin, koska vain niitä voi mitata 0 eurolla.
   Kirjataan HYPOTHESIS:ksi, ei teoreemaksi.
5. html5lib on tapaus, jossa but-for on epätosi: ihmiset tekivät saman korjauksen
   kolmesti. Mallien vipu siinä oli nopeus, ei mahdollistaminen.

**Seuraava koe, lukittu:** koe 03, toistuvuusmittaus (20 satunnaisriviä siemenellä
20260916, lukittu taksonomia T1 - T7, kynnykset K ≥ 3 ja R ≥ 0,3 jatkoon, K ≤ 1 tai
R < 0,15 tappo). Ei korjauksia, ei A/B:tä, ei rahaa. Sen jälkeen vasta paritettu koe B,
ja vasta sen jälkeen GPT:n täysi koe haaralla D.

**omistajalta tarvitaan:** portfolion tappiobudjetti lukuna (tokeneina tai euroina), jotta
v2.2:n "kirjataan sivuun määräajalla" on täytäntöönpantavissa.

## 2026-09-16 · Koe 03 suoritettu: toistuvuusmittaus, tulos KILL

**Tulos (lukittu protokolla, `kokeet/03-toistuvuusmittaus.md`):** R = 0,25 (5/20),
K = 1, H = 0,75 (15/20). Kynnys "K ≤ 1 → KILL" täyttyy mekaanisesti. Artefakti-S-haara
(uudelleenkäytettävä korjaustieto) kuolee PyPI:n ladatuimpien orpojen luokassa. Vaihtoehtoa
B ei ajeta tälle luokalle, otosta ei laajenneta.

**Poikkeamien käsittely:** esirekisteröity analyysiskripti normalisoi laajemmin kuin
lukittu teksti (olisi antanut K = 3, UNKNOWN). Lukittu teksti sovellettu. Rivi 11 on
protokollan artefakti (metapaketti ilman moduulia) ja rivi 19 aikarajan tuottama; kumpikaan
ei muuta tulosta.

**Mikä muuttuu:** pöytätestin P3 kaatuu tässä luokassa; "orpo = rikki" -premissi heikkenee
kolmannen kerran (H = 0,75); pakotetut alustamigraatiot -kortin Python-premissi heikkenee.
PROSESSI.md ei muutu. Teoriavaihe pysyy suljettuna.

**Tappiobudjetti:** omistaja asetti 200 € ulos maksettavaa rahaa per tutkimushaara; mallien
käyttö tilauksen sisällä ei lasketa, erilliset API-kulut lasketaan. Kirjattu. Koe 03
käytti 0 €.

**Seuraava halvin päätöstä muuttava havainto (ei suoritettu):** sama protokolla WordPress-
listalle (`data/orvot/wordpress-orvot-top10000.csv`, aktivointi tuoreessa WP 7.1:ssä
WP-CLI:llä). Vaatii PHP:n, MySQL:n ja WP-CLI:n asennuksen tälle koneelle tai konttiin.
Jos sekin antaa KILL, artefakti-S-haara kirjataan kuolleeksi kokonaan ja jäljelle jäävät
tilat (yleisö, sopimus, luottamus) vaativat omistajaa.

## 2026-09-16 · Seuraava havainto valittu: koe 04 yleisötila, ei WordPress

**Päätös:** WordPress-toistuvuusmittausta ei ajeta seuraavaksi. Sen KILL olisi viides
samansuuntainen havainto (mm. 15/166 WP-orvosta yli 10 k asennuksella on avoimia
tukiketjuja) ja PASS:n ennakko on matala. Seuraava koe on **koe 04: yleisötilan mittaus**
(`etsinta/SEURAAVA-HAVAINTO.md` §5): repo julkiseksi, yksi englanninkielinen tiivistelmä
yhteen kanavaan, 14 päivän mittaus GitHubin traffic-rajapinnasta, kynnykset lukittu.
Vaatii omistajan päätöksen ja alle tunnin. 0 €.

**Korjattu väite:** "jos WordPresskin KILL, artefakti-S kuolee kokonaan" oli väärin.
Artefakti-S on ominaisuus, ei mekanismi; PyPI ja WordPress ovat saman alaluokan
(hylätty ohjelmisto julkisessa hakemistossa) kaksi tapausta. Oikeuksien lunastuksessa
toistuvuus on rakenteellinen. Rajattu väite: "artefakti-S hylätyn ohjelmiston
korjauksessa" on se, mikä voisi kuolla.

**Uusi FACT, joka muutti vertailua:** repo on yksityinen; yleisötila on ollut 0
rakenteellisesti, ei mitattuna. Kolme muistiota on nimennyt yleisösilmukan, jota ei ole
koskaan käynnistetty.

**omistajalta:** (1) päätös repon julkistamisesta ja tiivistelmän hyväksyntä; (2) vastaus
kysymykseen, mitä kielipareja omistaja tai lähipiiri osaa tutkintotasolla (ratkaisee
kääntäjäkortin 5 minuutissa).
