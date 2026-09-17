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

## 2026-09-16 · Koe 04 lukittu AUDIENCE/ACCESS-erottelulla; salaisuustarkistus tehty; kääntäjäkortti hylätty meille

**Päätös (omistaja):** koe 04 tehdään seuraavaksi, WordPress jätetään ajamatta. Protokolla
korjattu omistajan ohjeen mukaan: AUDIENCE (U: 500 / 50) ja ACCESS (I: asiallinen yhteydenotto,
neljän ehdon määritelmä, kaksi itsenäistä luokittelijaa) mitataan ja tulkitaan erikseen;
yhdistetty päätösmatriisi lukittu. `kokeet/04-yleisotila-protokolla.md`.

**Salaisuustarkistus (FACT):** ei avaimia historiassa, `.env` ei koskaan committoitu.
Julkistuessa paljastuu commit-tekijän sähköposti (poistettu) (27 commitia) ja
kolmansien julkisia sähköposteja johdetuissa datatiedostoissa (WordPress-tekijäkenttä,
yksi CWS-tarjoaja, yksi PyPI-maintainer). Näkyvyyttä ei muutettu; odottaa omistajan päätöstä.

**Julkaisuteksti:** `etsinta/JULKAISU-1.md`, englanti, vain FACT-luvut, odottaa hyväksyntää.

**Kääntäjäkortti:** omistajan kielet suomi, englanti, ruotsi; ei tutkintokelpoisuutta
harvinaisessa parissa. Kortti hylätty meille, mekanismi säilyy generaattorin syötteenä.

**Pysähdys:** koetta ei suoriteta ennen omistajan hyväksyntää tekstille ja julkistukselle.

## 2026-09-16 · Pseudonyymi identiteetti, git-historia uudelleenkirjoitettu

**Päätös (omistaja):** projekti julkaistaan identiteetillä "eikaisiina", ei henkilön
nimellä. Historia uudelleenkirjoitettu filter-repolla (31 commitia), nimi, sähköposti,
paikalliset polut ja kolmansien sähköpostit poistettu, 14 SHA-viittausta korjattu,
pakotettu GitHubiin. Raportti `kokeet/04-sanitointi.md`. Repo yhä yksityinen.

**Jäljellä ennen julkistusta:** repon sijainti käyttäjätilin alla (siirto organisaatioon
"eikaisiina" on omistajan päätös), vanhojen commit-objektien poisto GitHubista (tukipyyntö),
paikallisen varmuuskopion käsittely. Koe 04 odottaa omistajan hyväksyntää.

## 2026-09-16 · Ristiinarvio Workin tutkimukseen, agenttipalkkaus-luokka, koe 05 lukittu

**Päätökset (uudet, evidenssiin perustuvat):**
1. Workin finalisti A (rahasaatava) on sama mekanismi kuin kortti
   `ostoreskontran-takaisinperinta`; se säilyy palvelumekanismina. Finalistit B (SEC-
   palkkio) ja C (tekninen parannus) eivät saa koetta: B on optio ilman toistettavuutta ja
   SEC:n 2020-sääntö sulkee pois "reasonably apparent" -analyysin; C:n vipu kuuluu
   kustannuspohjan omistajalle. Ks. `etsinta/RISTIINARVIO-WORK.md`.
2. Agentti → raha → ihminen -luokka: yhtään dokumentoitua suljettua positiivista silmukkaa
   ei löytynyt (Vend 1 tappio, Vend 2 palkkaus kielletty, Truth Terminal ihmisneuvosto,
   RentAHuman 12,2 % valmistuu). Luokitellaan skaalauskertoimeksi, ei mekanismiksi.
   Botto on ainoa AI-ansaittu silmukka ja sen kone on yleisötila.
3. **Koe 05, pääsytesti omassa verkostossa, lukittu** (0 €, omistaja 1 - 2 h, ≤ 3 pyyntöä,
   PASS Y ≥ 1, KILL 0/3). Se dominoi koe 04:ää seuraavana havaintona, koska se testaa
   suoraan estettä, johon 14 tapausta ja kolme tutkimuslinjaa osoittavat. Koe 04 säilyy
   rinnakkaisena ja lukittuna; kumpikaan ei odota toista.
4. Teoriaan kolme tarkennusta, ei rakennemuutosta: SEC 21F-4(b)(3) esimerkkinä liikkuvasta
   baselinesta; Botto yleisötilan näyttönä; agenttipalkkaus kertoimena.

**Omistajalta tarvitaan:** koe 05:n pyyntötekstin hyväksyntä ja enintään kolme nimeä
omasta verkostosta (eivät tule repoon); erikseen koe 04:n julkaisupäätös.

## 2026-09-16 · Koe 05: ACCESS FAIL rajataan pääsyreittiin, ei mekanismiperheeseen

**Päätös (omistaja):** kolmen oman verkoston henkilön negatiivinen tulos kokeessa 05
tappaa vain hypoteesin "saamme recovery-auditin ensimmäisen oikean aineiston halvasti
nykyisen oman verkoston kautta". Se ei tapa recovery audit / data + success fee
-mekanismiperhettä eikä muita pääsyreittejä. Aiempi luonnos ("perhe sivuun") oli liian
vahva kolmen valikoituneen henkilön otokselle. Lisäksi palkkio lukittu yhteen arvoon,
20 % toteutuneesta ja vahvistetusta takaisin saadusta rahasta, ja koe pidetään
puhtaana pääsytestinä. Protokolla `kokeet/05-paasytesti-protokolla.md`, viesti
`kokeet/05-pyynto.md`.

## 2026-09-16 · Lähtöresurssisääntö; koe 05 superseded; koe 04 säilyy tuoreella tilillä

**Metodologinen päätös (omistaja ja Claude):** ennen koetta kertynyttä henkilökohtaista
pääomaa (verkosto, maine, yritykset, asiakkuudet, data, luvat, yleisöt, tunnusten
historia, portin tavoin toimiva erityispätevyys) ei käytetä pääsyn, luottamuksen tai
jakelun hankintaan. Sääntö kirjattu PROSESSI.md:hen ja perusteltu
`etsinta/LAHTORESURSSISAANTO.md`:ssä. Symmetrinen: koehenkilön erityinen rajoite ei ole
mekanismin KILL.

**Koe 05 (oma verkosto): superseded.** Se olisi mitannut suhdetta, ei mekanismia.
Protokolla ja viesti säilyvät historiassa merkittyinä. Ei suoritettu, ei kontaktoitu.
Samalla peruttu perustelu "koe 05 dominoi koe 04:ää": se nojasi piilopääomaan.

**Auditointi:** kaikki suoritetut kokeet (01 - 03) ja skannaukset olivat neutraaleja.
Kolme aiempaa suunnitelmaa (lähdevero tutulle, jälkitarkastus tutulle, kääntäjän
lähipiiri) luokitellaan piilopääomasta riippuviksi; niiden mitattuja tuloksia ei ole.

**Koe 04 säilyy** seuraavana havaintona yhdellä lisäyksellä: postaus tuoreelta
projekti-tililtä. Mittarit ja kynnykset ennallaan. Sen jälkeen suunnitellaan koe 06:
neutraali kylmä B2B-pääsytesti satunnaisotokselle tuntemattomia yrityksiä, lukitaan
koe 04:n aikana, ei nyt.

**Oikeushenkilö:** sopimus- ja laskutusosapuoleksi uusi toiminimi kokeen aikana tai
olemassa oleva yritys pelkkänä kuorena ilman viittausta historiaan; omistajan päätös,
kirjataan pääsyreittiin. Julkinen loki ei nimeä osapuolia.

## 2026-09-16 · Oikeushenkilösääntö täsmennetty; koe 04 saa jakeluportin

**Päätös (omistaja):** olemassa oleva yritys saa olla oikeushenkilö ja näkyä siellä,
missä oikeushenkilön kuuluu näkyä (tietosuojaseloste, ehdot, sopimus, lasku, footer);
sen goodwillia ei käytetä luottamuksen rakentamiseen. Uutta yritystä ei perusteta
metodologisen puhtauden takia. Kirjattu `etsinta/LAHTORESURSSISAANTO.md` §6.

**Päätös (Claude, omistajan havainnon perusteella, tarkistettu HN:n FAQ:sta):** koe 04:n
AUDIENCE tulkitaan vasta jakeluportin (vaihe D: pisteet ≥ 5, top 30 tai ≥ 3 kommenttia
48 tunnissa; ei dead/flagged 2 tunnissa) jälkeen. Ilman jakelua tulos on NO DISTRIBUTION,
ei KILL; jatkot: HN:n second-chance pool kerran, sitten toinen kanava kerran. U-kynnykset
500/50 ja ACCESS eivät muutu. Seuranta HN:n julkisesta rajapinnasta
(`kokeet/04-hn-seuranta.py`), ei tiliä. Tuoreella tilillä ei kerätä mainetta ennen postausta.

## 2026-09-16 · Koe 04 pre-flight: U:n määritelmä, IOE-portti, matriisi, neutraali julkaisu

**Päätökset:** (1) U = GitHubin ylätason 14 päivän `uniques` haettuna T + 14 vrk, ei
päivittäisten uniikkien summa; U_hn referrer-erittelystä täydentävänä. (2) D-portti
korvataan käsitteellä RIITTÄMÄTÖN HAVAITTU ALTISTUS (IOE): altistus havaittu vain, jos
postaus on ollut top 30:ssä vähintään 4 × 15 min; pisteitä ja kommentteja ei käytetä
altistuksen mittarina. (3) Kynnykset arvioitu uudelleen: PASS U ≥ 500; KILL vain, jos
altistus havaittu ja U < 50; muuten UNKNOWN tai IOE. (4) ACCESS-tulos nimetään
"EI HAVAITTU", ei KILL. (5) Julkaisutekstin johtopäätös pehmennetty. (6) Julkaisu ei
tapahdu osoitteesta `original-private-account/eikaisiina`; suunnitelma: uusi käyttäjä `eikaisiina`, uusi
repo, push ilman siirtoa ja ilman historian uudelleenkirjoitusta, vanha repo poistetaan
30 päivän päästä (`kokeet/04-preflight.md`). Tila: NOT READY, kunnes tarkistuslista on tehty.

## 2026-09-16 · Koe 04: toteutuspäätökset (omistaja)

Julkaisuteksti hyväksytty. omistajan olemassa oleva yritys pysyy kaupallisten kokeiden juridisena taustana,
ei ratkaista koe 04:ää varten. Superteam-agentin nimi `eikaisiina` jää (kokeen aikana
syntynyt, ei perittyä pääomaa); claim/profile-linkit varmistetaan. Uusi GitHub-käyttäjä
`eikaisiina` ja uusi yksityinen repo; Claude pushaa historian ja korjaa osoitteet; omistaja
tarkistaa ennen julkistusta; HN-tili ja koe 04 vasta sen jälkeen. Vanhaa repoa ei poisteta
automaattisesti. Tutkimusidentiteetti `eikaisiina` erotetaan tulevista kaupallisista
brändeistä: tutkimusyleisön luottamusta ei käytetä koe 06:ssa. Koe 04:n rakennetta ei enää
muuteta.

## 2026-09-16 · Julkinen tutkimusidentiteetti: Constraint Works

**Päätös (omistaja):** sisäinen projekti `eikaisiina`, julkinen tutkimusidentiteetti
Constraint Works, ensisijainen handle `constraintworks`. Koe 04 tehdään sen kautta. Vanha
yksityinen repo säilyy eikä sitä poisteta. Constraint Worksin yleisöä, mainetta tai
kontakteja ei käytetä koe 06:n kaupallisena lähtöpääomana.

**Toteutus (Claude):** historia uudelleenkirjoitettu tekijäksi `Constraint Works
<noreply@constraintworks.invalid>` (linkittymätön osoite), omistajan yrityksen nimi ja
vanha käyttäjänimi purettu kaikista blobeista, SHA-viittaukset korjattu, skriptit
parametrisoitu, README:hin englanninkielinen otsake. `ConstraintWorks`-organisaatio on
jo olemassa eikä ole tämän kirjautumisen käytettävissä; vapaita vaihtoehtoja on
(`constraint-works` ym.). Blokkeri: GitHub-identiteetin luonti tai pääsy vaatii selaimen.
Koe 04: NOT READY tästä yhdestä syystä. Ks. `kokeet/04-preflight.md`.

## 2026-09-16 · Sähköpostit ja verkkotunnukset: tutkimusidentiteetti vs. koe 06

**Päätös (omistaja):** tutkimusidentiteetin (GitHub, HN) rekisteröintiosoite voi olla mikä
tahansa uusi osoite, kunhan siinä ei ole omistajan nimeä, olemassa olevan yrityksen
verkkotunnusta tai muualla käytettyä osoitetta; se ei näy julkisesti eikä sitä käytetä
yhteydenottoihin. Koe 06:n yhteydenotot lähtevät uuden palvelubrändin omalta, kokeen aikana
hankitulta verkkotunnukselta, **eivät koskaan olemassa olevan yrityksen osoitteesta**, koska
se viittaisi tiettyyn yritykseen jo ensikontaktissa. Yritys näkyy vasta sopimuksessa,
laskulla ja tietosuojaselosteessa (lähtöresurssisäännön oikeushenkilösääntö). Tuoreen
verkkotunnuksen lähetysmaine (SPF, DKIM, DMARC, ikä) on osa sitä, mitä koe 06 mittaa.
Verkkotunnuksen osto on rahankäyttö ja vaatii omistajan luvan.

## 2026-09-16 · Koe 06 suunniteltu: neutraali kylmä pääsytesti, Suomi, protokolla odottaa GPT:n tuhoamisyritystä

**Tila:** protokolla `kokeet/06-kylma-paasytesti-protokolla.md` on LUONNOS, ei lukittu, ei
käynnistetty. Ei rahaa käytetty, ei verkkotunnusta, ei tilejä, ei yhteydenottoja, ei otosta.
Koe 04 jatkuu koskemattomana; koe 06 alkaa aikaisintaan 2026-10-05, koe 04:n 14 päivän
ACCESS-ikkunan jälkeen, jotta sisääntuleva pääsy on kohdistettavissa reittiin.

**Metodologiset päätökset (Claude, johdettu lähtöresurssisäännöstä ja tutkimuskysymyksestä):**
1. **Testattava portti G1:** kokeen aikana rakennettu uskottavuus riittää siihen, että
   ennalta määritellyn populaation yritys samanaikaisesti luovuttaa ≥ 24 kk ostolasku- ja
   maksuaineiston, allekirjoittaa käsittely- ja salassapitosopimuksen (tekoälykäsittely
   näkyvissä) ja palkkioehdon 20 % toteutuneesta ja vahvistetusta palautuksesta. Puhdas
   ACCESS-koe: ei analyysiä, ei recovery-työkalua, ei summa-arvioita, ei toimittajakontakteja.
2. **Markkina: Suomi**, metodologisin perustein (`etsinta/KOE06-MARKKINAVERTAILU.md`):
   ainoa vertailluista, jossa otantakehikko kokoproxyineen on 0 € ja avoin kenelle tahansa
   (YTJ-massalataus + Veron julkiset verotiedot), sähköposti ja puhelin laillisia
   oikeushenkilöille ilman suostumusta (SVPL 202 §), ja kieli tavallista osaamista. Muu
   markkina lisäisi "ulkomainen toimija" -muuttujan, jota ei voi erottaa "tuntematon
   toimija" -muuttujasta. Saksa ja Tanska putoavat lain takia. Varamarkkina: Ruotsi.
3. **Populaatio ja kehikko (FACT, rakennettu):** 9 492 suomalaista osakeyhtiötä
   (ALV-, työnantaja- ja ennakkoperintärekisterissä, ≥ 5 v, TOL 10 - 33 / 41 - 43 / 46 /
   49 - 53, verot 2024 ≥ 10 000 €). Kehikkotiedosto repon ulkopuolella, SHA-256 ja suppilo
   repossa (`kokeet/06-kehikko-tiivistelma.json`). Toiminimet pois (SVPL 200 § vaatisi
   suostumuksen).
4. **Otanta:** 150 riviä siemenellä = lukituspäivä; 60 + 60 + 30 varaa; sample lock L1
   ennen nimien katsomista; poissulut vain viidellä koodilla, määrä committoidaan.
   Yhteydenoton jälkeen ei korvata.
5. **Kanava:** sähköposti yleisosoitteeseen (V1) → muistutus D7 → puhelu D14 - 21
   vastaamattomille. Puhelu on saman protokollan kolmas askel, jonka tehtävä on erottaa
   tavoittamattomuus hylkäyksestä. Ei LinkedIniä, ei kirjeitä (3 €/kpl ylittäisi rajan),
   ei nimettyjen henkilöiden osoitteita ilman pyyntöä.
6. **PASS** vaatii kuusi ehtoa (otos, aineisto ≥ 24 kk + maksut, käsittelysopimus,
   palkkioehto, piilopääomatarkistus kysymyksin, reitti kirjattu) ja PRH-tilinpäätöksellä
   varmistetun liikevaihdon ≥ 0,5 M€ (muuten PASS-PIENI). **FAIL** on reittikohtainen ja
   vaatii tavoitettuasteen ≥ 50 % ja N_c ≥ 100; se falsifioi vain hypoteesin "tuore brändi +
   suomalainen kylmä sähköposti/puhelu → ensimmäinen data + tulospalkkio -asiakas 120:stä
   9 viikossa", ei mekanismiperhettä. **UNKNOWN** kolmessa muodossa: CHANNEL (tavoitettu
   < 40 % D21 tai < 50 % lopussa), ACCESS (sopimus ilman aineistoa tai päinvastoin),
   INCOMPLETE (35 h täyttyi).
7. **Identiteetti:** uusi brändi B omalla .fi-verkkotunnuksella; olemassa oleva yritys vain
   oikeushenkilönä alatunnisteessa, sopimuksissa ja laskulla; lähettäjä oikealla nimellään
   (SVPL 203 §). **Brändin nimi, verkkotunnus ja otoslista eivät tule tähän julkiseen
   repoon** (vain SHA-256), jotta vastaanottajan haku ei löydä tutkimusrepoa eikä Constraint
   Worksin yleisö vuoda kokeeseen. Tarjous esitetään kaupallisena palveluna, ei tutkimuksena;
   sopimus velvoittaa meidät tekemään analyysin PASSin jälkeen (koe 07 lukitaan erikseen).
8. **Budjetti ex ante:** ≤ 83 €, katto 120 € (verkkotunnus, sähköposti, prepaid,
   PRH-tilinpäätökset); omistajan aika ≤ 35 h. Juristin tarkastus (200 - 500 €) tietoisesti
   pois; riski kirjattu. Ei kulutettu vielä mitään.
9. **AI-attribuutio** kirjattu etukäteen ilman A/B:tä: mitattavat tunnit ja but-for-arvio;
   PASS ei osoita mallien välttämättömyyttä eikä FAIL niiden hyödyttömyyttä.
10. **Oma hyökkäys** tehty (§12): seitsemän korjausta ennen GPT:tä; jäännöskonfoundina
    oikeushenkilön y-tunnuksesta pääteltävä ikä (sääntö sallii; uutta yritystä ei perusteta).

**Suurin jäljelle jäävä riski:** oikeushenkilön ikä ja omistajan nimi voivat vaikuttaa
hiljaisesti (vastaanottaja hakee, ei sano). Mitataan kysymyksin ja spontaanein signaalein,
ei voida sulkea pois.

**Seuraavaksi:** GPT:n riippumaton tuhoamisyritys protokollaan ja viesteihin; korjaukset;
lukitus L1; omistajan lupa rahankäyttöön ja brändin nimelle; käynnistys aikaisintaan
2026-10-05.

## 2026-09-17 · Koe 06: GPT:n tuhoamisyritys (READY AFTER CORRECTIONS), kuusi korjausta tehty

**Tila:** protokolla yhä LUONNOS. Ei L1-otantaa, ei rahaa, ei brändin nimeä, ei
käynnistystä. GPT tarkistaa korjausdiffin ennen lukitusta.

**Korjaukset (korvaavat edellisen merkinnän kohdat 6, 8 ja 9 siltä osin kuin ristiriita):**
1. Liikevaihtoraja ≥ 0,5 M€ poistettu PASS-ehdosta; se olisi ollut otannan jälkeinen
   populaatioehto. Populaatio on K1 - K8 ja lukittu ennen otantaa. PASS-PIENI poistettu.
   PRH-tilinpäätösosto (15 €) poistettu; budjetti ≤ 68 €, katto 120 €. Ostovolyymi
   kuvataan PASS-aineiston loppusummasta suuruusluokkana, ei PASS-ehtona.
2. Nimittäjäketju eksplisiittiseksi: otos N_s → tavoitettavissa N_ct → kontaktoitu N_c →
   tavoitettu N_r → kiinnostunut N_i → sopimus N_k → aineisto N_d → PASS N_p. FAIL vaatii
   N_r ≥ 60 (tavoitetut, ei kontaktoidut eikä otos); aiempi "N_c ≥ 100 ja C4/N_c ≥ 50 %"
   ja "120 yrityksen otoksesta" poistettu. Huono toimitettavuus tuottaa CHANNEL UNKNOWNin,
   ei FAILia. Nollatulos kertoo: tavoitetuista alle 5 % (95 %:n yläraja) eteni sopimukseen
   ja aineistoon; ei mitään tavoittamattomista.
3. Kirjattu, että koe testaa yhtä lukittua hankintapakettia (tuore brändi + 20 % + ≥ 24 kk
   data + tekoälykäsittely + ei referenssejä + kylmä sähköposti/puhelu + populaatio K1 - K8
   + suomi), ei kaikkia recovery-ACCESS-reittejä. FAIL nimetty pakettikohtaiseksi.
4. V1:stä poistettu väite "Suurille yrityksille tätä on tehty pitkään tulospalkkiolla.
   Pk-yrityksille ei juuri kukaan." Tarjous ei tarvitse sitä.
5. Piilopääomasääntö objektiiviseksi: julkinen rekisteritarkistus (YTJ, Virre, Finder,
   Asiakastieto) ei kontaminoi, koska oikeushenkilön käyttö juridisena taustana on
   sallittu. Potentiaalisesti piilopääoma-avusteinen, jos Q1 = KYLLÄ (tunsi ennestään),
   Q3 = KYLLÄ (yhtiön ennen koetta kertynyt historia vaikutti), spontaani viittaus
   historiaan päätöksen perusteena (kaksi luokittelijaa) tai yhteys omistajan tuntevan
   kolmannen kautta. Uusi Q3 lisätty viesteihin ja lokiin.
6. AI-attribuutiosta poistettu mittaamattomat vastafaktuaaliväitteet ("ihmiselle päiviä",
   "maksullinen tietopalvelu", "lakimies"). Kirjataan vain mitattu AI-avusteinen aika ja
   kustannus per työvaihe; ihmisen vastafaktuaali on INFERENCE, ei tulos.

**Ristiriitatarkistus:** markkinavertailu (§4 "ostovolyymi todetaan aineistosta"),
viesti, lokipohja ja tämä loki tarkistettu; vanhat muotoilut poistettu tai korvattu.

## 2026-09-17 · Koe 06 lukittu (`ee116d4`, GPT APPROVED FOR LOCK); L1-otos arvottu; poissulkukierros osittain

**Lukitus:** protokolla, kynnykset, viestit, populaatio, hankintapaketti, budjettirajat ja
mittarit lukittu versiona `ee116d4`. Protokollaa ei avata uudelle optimointikierrokselle
ilman uutta konkreettista ristiriitaa; poikkeamat kirjataan tähän lokiin ennen toimeenpanoa.

**L1 (FACT):** `06-otos.py`, siemen 20260917, 150 riviä ilman takaisinpanoa kehikosta
(9 492; SHA-256 varmistettu ennen arvontaa). Otoksen SHA-256
`ca5f23732937ac8232dd7c59b3eb9e180bdf5e809e918012e7d0e44f4c216245`. Nimet ja y-tunnukset
repon ulkopuolella pysyvässä yksityisessä hakemistossa; `.gitignore` estää otos- ja
kehikkotiedostojen päätymisen repoon. Nimiä ei katsottu ennen arvontaa eikä Claude ole
katsonut niitä arvonnan jälkeen.

**Poissulkukierros:** mekaaninen osa tehty (X-DUPL 0, X-K04 0 tilanteessa 2026-09-17).
Omistajan osa (X-TUTTU, X-ASIAKAS, X-KONSERNI) vaatii omistajan lukevan 150 nimeä; se on
ensimmäinen kohta, jota Claude ei voi tehdä. Korvaukset varalta ja aggregaatit kirjataan
sen jälkeen.

**Ei tehty:** ei yhteydenottoja, ei verkkotunnusta, ei rahaa, ei brändin nimeä, ei D0:aa.
Koe 04 koskematon.

## 2026-09-17 · Koe 06: rakennusvaiheen edellytykset selvitetty; poikkeamaehdotus P1 odottaa päätöstä

**Tehty (0 €, ei tilejä, ei brändiä):** `kokeet/06-rakennusvaiheen-vaatimukset.md` (R1 - R7:n
tekniset ja juridiset edellytykset, omistajan päätöslista) ja
`kokeet/06-sopimuspohjat-luonnos.md` (käsittely- ja salassapitosopimus GDPR 28 art.
sisällöllä, palkkioehdot lukitun §5 (ii) mukaan, tietosuojaseloste, sivuteksti;
paikkamerkein, GPT:n tarkistettavaksi, ei juristia).

**Päätökset (johdettu säännöistä):** aputoiminimeä ei rekisteröidä (60 € ei muuta
mitattavaa parametria; oikeushenkilö tunnistetaan joka viestissä); verkkotunnuksen
haltijana näkyvä olemassa oleva yritys on oikeushenkilösäännön mukainen; sivua ei
isännöidä GitHub Pagesissa minkään olemassa olevan tilin alla; sivulla ei evästeitä,
analytiikkaa eikä lomaketta.

**Poikkeamaehdotus P1 (EI toimeenpantu, vaatii omistajan ja GPT:n päätöksen):** lukittu
§5 (i) ja tapaamisrunko §4 lupaavat tekoälykäsittelyn "ilman datan säilytystä". FACT:
rajapintojen oletus on 30 päivän säilytys; nollasäilytys vaatii erillisen hyväksynnän.
Lause ei olisi tosi allekirjoitushetkellä. Ehdotus: paikallinen pseudonymisointi + "ei
koulutuskäyttöä, säilytys enintään 30 pv väärinkäytösvalvontaan". Suunta PASSia
vaikeuttava. Lukittuja tiedostoja ei muutettu.

**Pysähdys:** seuraavat askeleet vaativat omistajaa: poissulkukierros (150 nimeä), P1,
brändin nimi, rahankäyttölupa (≤ 68 €, katto 120 €).

## 2026-09-17 · Koe 06: poissulkukierros valmis, 0 poissulkua

Omistaja luki otoksen 150 nimeä: X-TUTTU 0, X-ASIAKAS 0, X-KONSERNI 0; mekaaninen osa
X-DUPL 0, X-K04 0. Ei korvauksia varalta. Lopullinen rakenne: K06-001 - 060 aalto 1,
061 - 120 aalto 2, 121 - 150 käyttämätön vara. Lukitun otoksen SHA-256 ennallaan.
Piilopääomahavainto: omistajan verkosto ei ulotu otokseen (0/150), eli protokollan
§6 kynnys "yli 15 poissulkua" ei lähelläkään. X-K04 uusitaan ennen D0:aa. Yhteystietojen
haku (aalto 1) on protokollan mukaan nyt sallittu, mutta sitä ei aloiteta ennen kuin
R1 - R7 ja päätökset P1, brändin nimi ja rahankäyttölupa on tehty, jotta haun ja
ensimmäisen viestin väli jää lyhyeksi.

## 2026-09-17 · Koe 06: P1 toimeenpantu totuudenmukaisuuskorjauksena; rahankäyttölupa; vastuukatto hylätty; rakennusvaihe valmis omistajan ostoihin asti

**Omistajan päätökset:**
1. **P1 hyväksytty.** Lukittu §5 (i) ja tapaamisrungon kohta 4 lupasivat tekoälykäsittelyn
   "ilman datan säilytystä"; se ei olisi ollut tosi (rajapintojen oletus on rajattu
   säilytys). Korjattu: paikallinen pseudonymisointi ennen tekoälykäsittelyä; ei
   koulutuskäyttöä; säilytysaika ja käsittelypaikka kirjataan sopimukseen täsmälleen D0:ssa
   käytettävän palveluntarjoajan, konfiguraation ja säilytyskäytännön mukaan; "enintään
   30 päivää" ei ole lukittu; nollasäilytyksen hyväksyntä ei ole kokeen edellytys. Tämä on
   protokollan mukainen poikkeama (kirjattu ennen toimeenpanoa), ainoa lukituksen jälkeinen
   sisältömuutos. V1, M1, puhelukäsikirjoitus, Q1 - Q3, kynnykset ja populaatio ennallaan.
   Vaikutussuunta: PASSia vaikeuttava tai neutraali.
2. **Rahankäyttölupa ≤ 68 €** verkkotunnukseen, sähköpostiin ja prepaid-numeroon; halvin
   lukitut vaatimukset täyttävä vaihtoehto; katto 120 € ennallaan; loput 52 € vain uudella
   perustellulla luvalla.
3. **5 000 €:n vastuukatto ei hyväksytty** (perustelematon luonnosluku). Poistettu.
   Vaihtoehdot A - E perusteluineen: `06-rakennusvaiheen-vaatimukset.md` §4b. Säännöistä
   johdettuna jäljelle jäävät A (ei eurokattoa, välilliset vahingot rajattu) ja B (ei
   lauseketta); luonnoksessa A, koska se ei vaadi keksittyä lukua. Vahvistus omistajalta
   GPT:n tarkistuksen yhteydessä.

**Tehty (Claude, 0 €):** toimialatarkistus (PRH Virre: yleislauseke kattaa palvelun;
rekisteröity päätoimiala on eri alalta, mikä voi näkyä vastaanottajalle epäsuhtana:
symmetrisen piilopääomasäännön mukaan koehenkilön rajoite, kirjataan Q2/Q3:sta, ei
korjata rekisterimuutoksella); 10 brändiehdokasta tarkistettu neljällä menetelmällä
positiivisin kontrollein (tulokset vain yksityisessä hakemistossa); hankintasuunnitelma
≈ 17 - 49 €; sivu-, tietosuoja-, sopimus- ja esimerkkiraporttipohjat, täyttöskripti,
DNS-pohja, R7-ohje ja otsaketarkistin.

**Pysähdys:** seuraava askel vaatii omistajan kirjautumista, tilien luontia ja maksamista
(verkkotunnus, sähköposti, prepaid, isännöinti) sekä nimen valinnan. Rinnalla GPT:n
viimeinen pre-D0-tarkistus sopimuspaketille.

## 2026-09-17 · Koe 06: GPT:n pre-D0-tarkistus `99a62e9` APPROVED täsmennyksin

1. **Vastuulauseke: vaihtoehto A hyväksytty** (GPT ja omistaja): ei euromääräistä kattoa;
   vastuu välittömistä vahingoista; välilliset rajattu pois; poikkeukset tahallisuus,
   törkeä huolimattomuus, salassapito ja tietosuoja. Ei muuteta ilman konkreettista
   juridista ristiriitaa.
2. **Palkkioehtojen kohta 6 selvennetty:** palvelun ja käsittelyn voi keskeyttää milloin
   tahansa ilman maksuja; ennen keskeytystä toimitettuun raporttiin sisältyvien löydösten
   20 %:n palkkioehto säilyy 12 kuukautta raportin toimittamisesta; ilman toimitettua
   raporttia palkkiota ei synny. Capture-rakenne (20 % vain toteutuneesta ja
   vahvistetusta) ennallaan.
3. **P1 hyväksytty nykyisessä muodossa.** Hakasulkeet täytetään ennen D0:aa vain todella
   käytettävän palvelun ja konfiguraation voimassa olevasta dokumentaatiosta.
4. Ensimmäistä viestiä ei lähetetä ennen 2026-10-05 eikä ennen viimeistä X-K04-tarkistusta.
   Verkkotunnusta ei osteta ennen omistajan nimivalintaa.

## 2026-09-17 · Koe 06: brändi B lukittu; tavaramerkkitarkistuksen menetelmäkorjaus

**Päätös (omistaja):** brändin nimi valittu kymmenestä ehdokkaasta ja lukittu koe 06:een.
Nimi ja verkkotunnus vain yksityisessä hakemistossa. Repoon suolattu SHA-256 (paljas
tiiviste lyhyestä nimestä olisi arvattavissa; suola julkaistaan kokeen päätyttyä):
brändi `f4f7621f…5fbce4`, verkkotunnus `1d73f565…fc0a0c` (täydet arvot `06-loki.md`).
Poikkeama protokollan sanamuodosta "SHA-256": suolattu, tiukempi, todennettavissa jälkikäteen.

**Uusintatarkistus ennen hankintaa (FACT):** .fi vapaa, YTJ 0, EUIPO 0, PRH:n kansallinen
tavaramerkkirekisteri 0, verkkohaku ei osumia; jokaisessa positiivinen kontrolli.

**Falsifiointi omasta työstä:** aiempi TMview-tarkistus oli pätemätön (haku ei suorittunut,
kontrolli oli lataustila). Raportoin sen aiemmin läpäistynä; se oli väärin. Korjattu
virallisilla rekistereillä valitun nimen osalta. Opetus: kontrollin pitää osoittaa
positiivinen sisältö (nimetty rivi), ei pelkkää "ei tyhjä" -tilaa.

**Palveluntarjoajat valittu etukäteen (halvin lukitut vaatimukset täyttävä):** verkkotunnus
12,00 €/v välittäjältä, jolla DNS-hallinta sisältyy; sähköposti Zoho Mail EU (ilmaistaso, jos
tarjolla, muuten Mail Lite vuosilaskutuksella); prepaid-aloituspaketti 4,90 €; sivun isännöinti
ilmaisella staattisella palvelulla, joka tukee juuriverkkotunnusta ilman nimipalvelimien
siirtoa. Ei ostettu vielä mitään.
