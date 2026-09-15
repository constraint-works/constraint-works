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
