# Koe 06: kylmä pääsytesti neutraalista lähtötilanteesta (ACCESS)

**Tila: LUKITTU 2026-09-17 versiona `ee116d4` (GPT: APPROVED FOR LOCK). Ei käynnistetty.**
Lukitus kattaa: testattava portti ja hankintapaketti (§1), populaatio K1 - K8 (§4),
data- ja sopimusvaatimukset (§5), otanta (§6), askeleet ja aikataulu (§7), mittarit,
nimittäjäketju ja piilopääomasääntö (§8), PASS/FAIL/UNKNOWN (§9), budjettirajat
(§10), AI-attribuution kirjaustapa (§11) sekä `06-viesti.md`:n V1, M1, P1, tapaamisrunko
ja Q1 - Q3. Tämän jälkeen sisällöllisiä muutoksia ei tehdä; jos poikkeama on pakko
tehdä, se kirjataan päätöslokiin ennen toimeenpanoa ja tulos raportoidaan
poikkeaman kanssa. Vain lukituslistan (§14) tila ja lokit päivittyvät.
Laadittu 2026-09-16 (Claude). Ei yhteydenottoja, ei rahaa, ei verkkotunnusta, ei tilejä,
ei otosta. Korvaa supersedatun koe 05:n (`05-paasytesti-protokolla.md`), jonka rakennetta
ei ole peritty. Markkinavalinta: `etsinta/KOE06-MARKKINAVERTAILU.md`. Viestit:
`06-viesti.md`. Otanta: `06-otantakehikko.py`, `06-otos.py`, `06-kehikko-tiivistelma.json`.
Loki: `06-loki-pohja.md`.

**Mahdollisuus:** `mahdollisuudet/ostoreskontran-takaisinperinta.md` (recovery audit,
data + tulospalkkio -perhe; sama kuin Workin finalisti A ja GPT:n YO-WORK-B §2).
**Alkaa:** aikaisintaan 2026-10-05, vasta GPT:n arvion, korjausten, lukituksen ja omistajan
käynnistysluvan jälkeen. **Päättyy viimeistään:** 2026-12-28 (tulos kirjattu 2026-12-31).
**Budjetti:** enintään 120 € ulos maksettavaa (haaran raja 200 €), omistajan aikaa
enintään 35 h. **Onnistumisen ehto:** §9.

## 1. Mitä koe testaa, ja vain sen

**Tutkimuskysymys:** voiko lähtötilanteessa tuntematon mutta uskottava toimija hankkia
kylmästi markkinalta yritysasiakkaan, joka antaa aidon käyttökelpoisen ostolaskudatan
analysoitavaksi ja hyväksyy etukäteen tulospohjaisen maksuoikeuden, ilman kokeen
ulkopuolelta perittyä verkostoa, mainetta, asiakkuuksia, yleisöä tai muuta pääomaa?

**Testattava portti (G1, "kylmä ensiportti"):** neutraalista lähtötilanteesta kokeen
aikana rakennettu uskottavuus riittää siihen, että ennalta määritellyn populaation
yritys **samanaikaisesti** (a) luovuttaa vähintään 24 kuukauden ostolasku- ja
maksuaineiston koneluettavana, (b) allekirjoittaa käsittely- ja salassapitoehdot, jotka
sallivat määritellyn analyysin, ja (c) allekirjoittaa palkkioehdon: 20 % toteutuneesta
ja asiakkaan vahvistamasta takaisin saadusta rahasta, muutoin 0 €.

Portti on recovery audit -mekanismin ensimmäinen aito portti. Aiempi mittaus
(14 tapausta, KEHIKON-TUHOAMISYRITYS-V3) ja kolme riippumatonta tutkimuslinjaa
osoittavat, että pääsy dataan ja sopimukseen on tämän perheen tyypillinen
katkeamiskohta. Sitä ei ole koskaan mitattu neutraalisti.

**Koe testaa yhtä lukittua hankintapakettia (acquisition bundle), ei kaikkia
pääsyreittejä.** Paketti: tuore brändi ilman referenssejä + oikea oikeushenkilö
alatunnisteessa + 20 %:n tulospalkkio vain toteutuneesta + pyyntö ≥ 24 kk
ostolasku- ja maksuaineistosta + tekoälykäsittely sopimuksessa näkyvissä + kylmä
sähköposti yleisosoitteeseen, yksi muistutus ja puhelu + §4:n populaatio + suomi.
Jokainen osa on lukittu, eikä koe erota, mikä osa ratkaisi tuloksen. Tulos koskee
tätä pakettia. Se ei yksin sano mitään muista recovery-ACCESS-reiteistä
(sisääntuleva, tilitoimistokumppani, maksettu mainonta, alustat, suositukset, kiinteä
hinta, muu populaatio tai markkina), eikä siitä, toimisiko sama paketti eri
kokoonpanolla.

**Mitä koe ei testaa:** onko aineistossa virheitä, saadaanko rahaa takaisin, maksaako
asiakas, mikä on virhetaso, skaalautuuko, kannattaako mekanismi. Kokeen aikana
ei analysoida yhtään laskua, ei rakenneta recovery-työkalua, ei arvioida
palautussummia, ei kontaktoida toimittajia, ei käytetä rahaa analyysiin, eikä
myöhempää taloudellista tulosta lasketa ACCESS-tulokseksi. Jos aineisto tulee, se
avataan vain §9:n muototarkistukseen, ja varsinainen analyysikoe (koe 07) lukitaan
erikseen ennen aineiston avaamista.

## 2. Lähtöresurssisääntö tässä kokeessa

Sallittu syöte: 1 000 € (tästä enintään 120 €), kaksi frontier-mallia, tietokone,
internet, yhden ihmisen aika ja tavallinen osaaminen (suomi, kirjoittaminen, puhelin,
tavalliset ohjelmistot), sekä kaikki, mikä rakennetaan kokeen aikana.

Ei sallittu pääsyn, luottamuksen tai jakelun lähteenä: omistajan verkosto, nimen
tunnettuus, olemassa olevan yrityksen historia, asiakkaat, referenssit tai maine,
omistajan henkilökohtaiset tilit (LinkedIn, HN, GitHub), Constraint Worksin yleisö tai
kontaktit, koe 04:n sisääntulevat yhteydenotot.

**Oikeushenkilö:** omistajan olemassa oleva yritys on sopimus-, käsittely- ja
laskutusosapuoli (oikeushenkilösääntö, LAHTORESURSSISAANTO §6). Se näkyy tietosuoja-
selosteessa, sopimuksissa, laskulla ja sivun alatunnisteessa y-tunnuksella. Sen nimeä,
ikää, referenssejä tai historiaa ei mainita viesteissä, puheluissa eikä sivulla
muuten kuin alatunnisteen ja sopimusten oikeushenkilötietona. Yhteydenotot lähtevät
vain uuden brändin verkkotunnukselta (päätös 2026-09-16).

**Henkilön nimi:** lähettäjä on oikea henkilö oikealla nimellään, koska oikeushenkilön ja
lähettäjän tunnistettavuus on lain vaatimus (SVPL 203 §) ja pseudonyymi kylmä tarjous
olisi harhaanjohtava. Nimi on piilopääomaa vain, jos vastaanottaja tuntee sen. Se
mitataan (§8, piilopääomasignaalit) ja tapaus suljetaan pois PASSista, jos vastaanottaja
tunsi henkilön tai yrityksen ennestään.

**Brändi B ja verkkotunnus eivät tule tähän julkiseen repoon.** Jos vastaanottaja hakee
brändin nimeä ja löytää tutkimusrepon, koe on paljastunut ja Constraint Worksin
tutkimusyleisö vuotaa kaupalliseen kokeeseen. Brändin nimi, verkkotunnus ja otoslista
säilytetään repon ulkopuolella; repoon tulee vain niiden SHA-256-tiivisteet ja
lukumäärät. Julkinen sivu ei linkitä tutkimukseen, eikä tutkimus brändiin. Koe 04:n
julkaisut eivät mainitse koe 06:n brändiä.

## 3. Mitä rakennetaan ennen yhteydenottoja, ja mikä siitä on mekanismin kustannusta

| # | Rakennettava | Mekanismin kustannus vai tutkimuksen hallintoa | € | Omistajan aika | Mitä parametria muuttaa |
|---|---|---|---|---|---|
| R1 | Brändin nimi ja .fi-verkkotunnus | Mekanismi (kuka tahansa tarvitsee) | 12 - 27 (FACT: Traficom 12 €, välittäjät 13,20 - 24 €) | 0,5 h | Ilman tätä sähköpostikanavaa ei ole; verkkotunnuksen ikä 0 on toimitettavuuden lähtötila, joka mitataan |
| R2 | Sähköpostilaatikko verkkotunnuksella, SPF, DKIM, DMARC | Mekanismi | 0 - 21 (ilmainen taso tai n. 1 - 7 €/kk × 3 kk; UNKNOWN tarkka) | 1 h | Toimitettavuus (bounce, roskaposti); FACT 2026-vaatimukset: SPF+DKIM+DMARC, roskapostiaste < 0,3 % |
| R3 | Yhden sivun verkkosivu (staattinen, 0 € isännöinti): mitä, miten palkkio toimii, mitä dataa, miten suojataan, kuka (nimi + oikeushenkilö alatunnisteessa), sopimuspohjat ladattavina, tietosuojaseloste, markkinointikielto-osoite. Lause: "Palvelu on uusi. Emme esitä referenssejä." | Mekanismi | 0 | 2 h | Uskottavuus ilman mainetta: läpinäkyvyys korvaa referenssit. Sivun olemassaolo on ehto, jonka vastaanottaja voi tarkistaa |
| R4 | Sopimuspohjat: (i) aineiston käsittely- ja salassapitosopimus (GDPR-käsittelysopimus + salassapito), (ii) palkkioehdot | Mekanismi | 0 (mallien laatimat; **ei juristin tarkastusta**, koska 200 - 500 € ylittäisi rajan; riski kirjattu §12) | 1 h tarkistus | Portin (b) ja (c) toteutettavuus; asiakkaan koettu riski |
| R5 | Esimerkkiraportti synteettisellä aineistolla (2 sivua) | Mekanismi | 0 | 0,5 h | Näyttää, mitä asiakas saa; ei väitä löydöksiä |
| R6 | Prepaid-puhelinliittymä brändille | Mekanismi (identiteetin erottelu; numerohaku ei saa johtaa olemassa olevaan yritykseen) | n. 10 (UNKNOWN tarkka) | 0,5 h | Puhelinvaiheen tavoittavuus ja identiteetin neutraalius |
| R7 | Toimitettavuustesti: viesti kolmeen omaan testilaatikkoon (Gmail, Outlook, kotimainen) ennen aaltoa 1 | Tutkimuksen hallinto | 0 | 0,2 h | Erottaa "meni roskapostiin" hylkäyksestä |
| R8 | Otantakehikko, otos, tiivisteet, lokipohja, toinen luokittelija | Tutkimuksen hallinto | 0 | 1 h | Otoksen lukitus ja tuloksen tarkistettavuus |

Yhteensä: 22 - 58 € ja noin 7 h ennen ensimmäistä viestiä. Jokaisen rakennettavan
kohdalla kirjataan mitattu aika ja mallien käyttö (§11). Se, mitä 1 000 eurolla **ei**
voi rakentaa: referenssejä, ikää, arvioita, tunnettua nimeä, suositteluja,
lakimiehen tarkastamia sopimuksia. Koe mittaa, riittääkö läpinäkyvyys + oikea
oikeushenkilö + selkeä riskitön ehto korvaamaan ne ensimmäisessä sopimuksessa.

## 4. Populaatio ja otantakehikko (lukittu tässä, rakennettu 2026-09-16)

**Populaatio:** suomalaiset osakeyhtiöt, jotka täyttävät kaikki:
K1 yhtiömuoto osakeyhtiö (ei julkinen osakeyhtiö); K2 kaupparekisterissä, ei konkurssia,
saneerausta tai selvitystilaa; K3 arvonlisäverovelvollinen liiketoiminnasta; K4
työnantajarekisterissä; K5 ennakkoperintärekisterissä; K6 y-tunnus rekisteröity
viimeistään 2021-06-30; K7 päätoimiala TOL 2025 kaksinumerotasolla 10 - 33
(teollisuus), 41 - 43 (rakentaminen), 46 (tukkukauppa), 49 - 53 (kuljetus ja
varastointi); K8 Verohallinnon verovuoden 2024 julkisissa tiedoissa maksuunpannut verot
yhteensä ≥ 10 000 €.

**Perustelut:** K3 - K5 rajaavat aktiiviset, palkkaa maksavat yritykset; K6 takaa, että
24 kk ostohistoriaa on; K7 rajaa ostolaskuintensiivisiin toimialoihin, joissa
toimittajia on paljon (tuplamaksut ja hintapoikkeamat ovat mahdollisia); K8 on ainoa
ilmainen kokoproxy (CALC: 10 000 € veroa ≈ 50 000 € verotettavaa tuloa 20 %:n
kannalla). Toiminimet ja henkilöyhtiöt on suljettu pois, koska niiden yhteystieto on
luonnollisen henkilön ja vaatisi SVPL 200 §:n suostumuksen. Tilitoimistot (69.2),
rahoitus (64 - 66) ja kiinteistöala (68) eivät kuulu toimialarajaukseen.

**Kehikko (FACT):** 9 492 yritystä (`06-kehikko-tiivistelma.json`, SHA-256 kehikko-
tiedostosta tiivistelmässä). Kehikkotiedosto (nimet, y-tunnukset) on repon ulkopuolella.
Suppilo ja jakaumat: `etsinta/KOE06-MARKKINAVERTAILU.md` §4.

**Mitä kehikko ei sisällä:** ostovolyymia (ei julkista ilmaista lähdettä; PRH:n
digitilinpäätösdata kattaa n. 5 % ja vain tuloslaskelma/tase), yhteystietoja (YTJ:ssä
verkkosivu 38,4 %:lla, ei sähköposteja eikä puhelimia). Yhteystiedon löytyminen on
osa saavutettavuusmittausta (§7). **Populaatio on K1 - K8 eikä mitään muuta.**
Otannan jälkeen ei lisätä populaatioehtoja (esim. liikevaihtorajaa). PASS-yrityksen
ostovolyymi kuvataan aineiston loppusummasta suuruusluokkana (§9 kohta 2) ja
raportoidaan mekanismin relevanssin arvioimiseksi; se ei ole PASS-ehto.

## 5. Mitä data ja mikä oikeus oikeasti tarvitaan

**Data (vähimmäisvaatimus, "käyttökelpoinen aineisto"):** per ostolasku rivi, jossa
toimittaja (nimi tai tunnus), laskun numero, laskun päivä, summa (brutto tai netto +
alv), ja per maksutapahtuma päivä, summa ja kytkentä laskuun (viite tai laskunumero);
hyvityslaskut mukana, jos niitä on. Vähintään 24 peräkkäistä kuukautta, joiden loppu on
enintään 3 kk ennen toimitusta. Muoto: CSV/Excel-vienti kirjanpito-ohjelmasta
(Procountor: ostojen raportointi → Export to Excel; Netvisor: ostoreskontraraportit)
tai vastaava. Asiakas toteaa kirjallisesti, että vienti kattaa koko ostoreskontran,
ei osajoukkoa. Tilitoimiston tekemä vienti asiakkaan pyynnöstä kelpaa.

**Ei tarvita:** rajapintaintegraatiota, pankkitunnuksia, sopimuksia toimittajien
kanssa, pääsyä kirjanpito-ohjelmaan. Ne olisivat suurempi luottamuspyyntö kuin
portti vaatii.

**Oikeus:** (i) **Aineiston käsittely- ja salassapitosopimus:** me käsittelijänä
asiakkaan lukuun; käsittelyn tarkoitus rajattu ostolaskujen poikkeamien tunnistamiseen;
alikäsittelijät nimetty (pilvitallennus EU:ssa, tekoälyrajapinta ilman datan säilytystä
tai koulutuskäyttöä); aineistoa ei käytetä muiden asiakkaiden hyväksi eikä mallien
opettamiseen; poisto 90 päivää loppuraportista; salassapito molemmin puolin;
asiakas voi keskeyttää milloin tahansa. Tekoälykäsittely on sopimuksessa näkyvissä,
koska ilman sitä "riittävä oikeus käyttää dataa määriteltyyn analyysiin" ei täyty.
(ii) **Palkkioehdot:** palkkio 20 % rahasta, jonka asiakas tosiasiassa saa takaisin
(hyvityslasku, palautus tai kuittaus) meidän kirjallisesti yksilöimämme löydöksen
perusteella 12 kuukauden sisällä raportista; asiakas vahvistaa summan (tiliote tai
hyvityslasku); lasku 14 pv vahvistuksesta; ei palkkiota epäillystä, laskennallisesta
tai tulevasta säästöstä; asiakas hoitaa yhteydenotot toimittajiin itse (ei perintää
toisen lukuun); ei yksinoikeutta; ei vähimmäispalkkiota; ei kuluja. Molemmat
allekirjoitetaan sähköisesti tai sähköpostivahvistuksella nimellä ja asemalla.

## 6. Otanta ja lukitus (sample lock, kuten koe 03)

1. **Lukitus L0 (tehty 2026-09-16):** kehikko rakennettu ja sen SHA-256 kirjattu.
2. **Lukitus L1 (GPT:n arvion ja korjausten jälkeen, ennen mitään yhteydenottoa):**
   `06-otos.py` arpoo kehikosta **150** yritystä ilman takaisinpanoa siemenellä, joka on
   lukituspäivä muodossa YYYYMMDD. Tuloste (nimet) tallennetaan repon ulkopuolelle;
   repoon committoidaan siemen, otoksen SHA-256, ja jakaumat (toimiala, verobandi,
   ikä, maakunta). Tässä vaiheessa kukaan ei ole katsonut nimiä.
3. **Poissulkukierros (heti L1:n jälkeen, ennen yhteystietojen hakua):** omistaja lukee
   150 nimeä ja merkitsee poissuljettavat koodilla: X-TUTTU (tuntee omistajan,
   hallituksen jäsenen tai kirjanpitäjän), X-ASIAKAS (olemassa olevan yrityksen nykyinen
   tai entinen asiakas/toimittaja), X-KONSERNI (sama konserni tai omistaja kuin
   olemassa olevalla yrityksellä), X-K04 (otti yhteyttä Constraint Worksiin koe 04:ssä),
   X-DUPL (sama yritys kahdesti tai selvä rekisterivirhe). Poissulkujen määrä ja koodit
   committoidaan; nimet ei. Poissulkuja ei saa tehdä muusta syystä (esim. "liian iso",
   "ei kiinnosta"). Jos poissulkuja on yli 15, se kirjataan piilopääomahavaintona
   (omistajan verkosto ulottuu kehikkoon) ja otos täydennetään varalistalta.
4. **Järjestys:** otoksen 150 rivin arvottu järjestys on käsittelyjärjestys. Rivit
   K06-001 - 060 ovat aalto 1, K06-061 - 120 aalto 2, K06-121 - 150 vara. Vara-rivejä
   käytetään vain korvaamaan ennen yhteydenottoa poissuljetut, järjestyksessä.
   Yhteydenoton jälkeen ketään ei korvata.
5. Yhteystietojen haku (§7) alkaa vasta poissulkukierroksen jälkeen ja vain aallon 1
   riveille; aallon 2 yhteystiedot haetaan vasta, jos aalto 2 käynnistyy.

## 7. Yhteydenotto: kanavat, viestit, muistutukset, aikataulu

**Yhteystiedon haku (per yritys, kirjataan minuutit):** yrityksen oma verkkosivu
hakukoneella (nimi + y-tunnus tai paikkakunta; sivulta varmistetaan y-tunnus tai
nimi + osoite). Käytetään vain **yleisosoitetta** (info@, myynti@, toimisto@, tms.) tai
yhteydenottolomaketta sekä vaihteen numeroa. Nimetyn henkilön osoitetta ei käytetä
ilman, että henkilö on itse pyytänyt materiaalin puhelimessa (silloin lähetys on
pyydetty, ei suoramarkkinointia). Jos yleisosoitetta ei löydy, käytetään lomaketta;
jos ei lomaketta, vain puhelin; jos ei puhelinta, tila C0 (ei kanavaa). Kolmansien
osapuolten yhteystietopalveluja (Fonecta, Finder) saa käyttää vain puhelinnumeron
tarkistukseen, ei osoitteen. Osoitteen lähde kirjataan (lain 203 §:n tunnistettavuus ja
tietosuojaseloste).

**Askeleet, kaikille aallon yrityksille samat (D = päiviä aallon alusta):**

| Askel | Päivä | Sisältö | Ehto |
|---|---|---|---|
| A1 | D0 - D4 | Sähköposti V1 (`06-viesti.md` §1), identtinen kaikille, vain yrityksen nimi vaihtuu. Lähetys käsin brändin laatikosta, enintään 15 viestiä/pv, ei massapostitusta, ei seurantapikseleitä, ei liitteitä, yksi linkki sivulle | Yleisosoite tai lomake löytyi |
| A2 | D7 - D9 | Muistutus M1 (`06-viesti.md` §2), identtinen, vastauksena samaan ketjuun | Ei vastausta, ei bouncea, ei kieltoa |
| A3 | D14 - D21 | Puhelu vaihteeseen, käsikirjoitus P1 (`06-viesti.md` §3), enintään 2 soittoyritystä eri päivinä, ei vastaajaviestiä toisella kerralla. Pyydetään ostolaskuista vastaavaa henkilöä; tarjous esitetään suullisesti; pyydetään lupa lähettää materiaali | Ei vastausta A1:n ja A2:n jälkeen, tai kanavana vain puhelin |
| A4 | tarvittaessa | Tapaaminen (puhelin/video, ≤ 45 min), sama runko kaikille (`06-viesti.md` §4); lähetetään sopimuspohjat samana päivänä | Yritys pyytää |
| A5 | ≤ D42 | Sopimukset allekirjoitettu ja aineisto vastaanotettu | |
| A6 | ≤ D63 | Yksi 21 päivän jatko vain niille, joilla on D42:na sovittu seuraava askel (tapaaminen kalenterissa, sopimus lähetetty, aineisto luvattu päivämäärällä). Ei uusia yhteydenottoja | |

Ei kolmatta sähköpostia, ei kolmatta soittoa, ei LinkedIniä, ei käyntejä, ei lahjoja, ei
alennuksia tai ehtojen muutoksia (20 % ja 0 € -rakenne on kiinteä). Jos yritys pyytää
kiinteää hintaa tai muuta mallia, vastaus on "ei tässä vaiheessa" ja pyyntö kirjataan
(se on havainto tarjouksesta, ei neuvottelu).

**Aallot:**
- Aalto 1 (K06-001 - 060): alkaa S1 ≥ 2026-10-05 (maanantai), edellytykset: koe 04:n
  14 pv ACCESS-ikkuna päättynyt (2026-09-30), GPT:n arvio ja lukitus tehty, R1 - R7
  valmiit, omistajan käynnistyslupa.
- **Kanavadiagnoosi D21 (aalto 1):** tavoitettu (C4, §8) / kontaktoidut < 40 % →
  aalto 2 ei käynnisty; tulos CHANNEL UNKNOWN (§9). Muuten aalto 2 käynnistyy.
- Aalto 2 (K06-061 - 120): alkaa S2 = S1 + 21 pv (≈ 2026-10-26), sama protokolla.
  Ei käynnisty, jos aalto 1 on jo tuottanut PASSin (silloin aalto 2 on vapaaehtoinen
  toisto, joka päätetään erikseen ja kirjataan).
- Kova takaraja: uusia yhteydenottoja ei D0-mielessä 2026-11-16 jälkeen; A5 aallolle
  2 viimeistään 2026-12-07; A6 viimeistään 2026-12-28.

**Toimitettavuus:** ennen A1:tä R7-testi; lähetysmäärä nousee 5 → 15/pv viikon aikana
(toissijaiset 2026-lähteet: uusi verkkotunnus 5 - 10/pv aluksi). Bouncet kirjataan
SMTP-syyn kanssa. Roskapostiin päätymistä ei voi mitata suoraan; puhelinvaihe A3
kysyy "saitteko viestimme" ja kirjaa vastauksen (SAI / EI SAANUT / EI TIEDÄ).

## 8. Mittarit ja kirjaus

Per yritys (`06-loki-pohja.md`, tunnisteet K06-nnn, ei nimiä, ei y-tunnuksia repoon):

| Koodi | Merkitys |
|---|---|
| X-* | Poissuljettu ennen yhteydenottoa (koodi §6) |
| C0 | Ei kanavaa: ei yleisosoitetta, ei lomaketta, ei puhelinta |
| C1 | Sähköposti lähetetty (pvm) |
| C1-B | Bounce (SMTP-syy) → ei tavoitettu |
| C2 | Muistutus lähetetty |
| C3 | Puhelu: ei tavoitettu kahdella yrityksellä (vaihde ei vastaa / vastuuhenkilöä ei saada) |
| C4 | **Tavoitettu:** on näyttö, että yrityksen henkilö on lukenut tai kuullut tarjouksen (vastaus mihin tahansa viestiin tai puhelinkeskustelu, jossa tarjous esitettiin) |
| R-NO | Nimenomainen kieltäytyminen; syy sanatarkasti; luokka: LUOTTAMUS (data ulkopuoliselle), HYÖTY (ei usko löytyvän), VAIVA, ON-JO (tekee itse / tilitoimisto / ohjelmisto), POLITIIKKA (ei ulkopuolisia), KIELTO (pyytää markkinointikieltoa; merkitään estolistalle), MUU |
| R-INT | Kiinnostus: pyysi materiaalin, tapaaminen pidetty tai sovittu |
| R-CONTRACT | Molemmat sopimukset allekirjoitettu, aineistoa ei vielä |
| R-DATA | Aineisto vastaanotettu, muototarkistus kesken |
| PASS | §9:n ehdot todennettu |
| VAIHE | Missä askeleessa ratkaiseva myönteinen tai kielteinen vastaus syntyi: A1 / A2 / A3 / A4 |
| PIILOPÄÄOMA | Tapaamisessa tai sopimusvaiheessa kysytään aina samat kolme kysymystä (`06-viesti.md` §5): Q1 tunsiko vastaaja lähettäjän tai oikeushenkilön ennestään; Q2 mistä hän tarkisti meidät (sivu, y-tunnus julkisesta rekisteristä, haku, ei mistään); Q3 vaikuttiko päätökseen jokin oikeushenkilöstä saatu tieto (ikä, liikevaihto, historia, asiakkaat, tuttu). Vastaukset kirjataan sanatarkasti. Lisäksi kirjataan spontaanit signaalit: mainitsiko olemassa olevan yrityksen historian, kysyikö referenssejä, epäilikö tekoälyn kirjoittamaksi tai roskapostiksi. Luokittelusääntö alla |
| AIKA | Omistajan minuutit per askel; mallien käyttö (kyllä/ei, mihin) |

**Piilopääomaluokittelu (objektiivinen sääntö, sovelletaan jokaiseen R-CONTRACT-,
R-DATA- ja PASS-tapaukseen):**
- **Ei kontaminoi:** vastaaja tarkisti oikeushenkilön julkisesta lähteestä (YTJ,
  Virre, Finder, Asiakastieto, hakukone) ja totesi sen olemassa olevaksi, aktiiviseksi
  tai rekisteröidyksi. Olemassa olevan yhtiön käyttö juridisena taustana on sallittu
  (oikeushenkilösääntö), ja sen tarkistaminen on osa sitä, mitä kuka tahansa tekisi.
- **POTENTIAALISESTI PIILOPÄÄOMA-AVUSTEINEN**, jos vähintään yksi täyttyy:
  (a) Q1 = KYLLÄ (tunsi lähettäjän tai oikeushenkilön ennestään, suoraan tai tutun
  kautta); (b) Q3 = KYLLÄ (vastaaja sanoo, että yhtiön ennen koetta kertynyt ikä,
  liikevaihto, historia, asiakkaat, maine tai tuttuus vaikutti päätökseen);
  (c) vastaaja viittaa kirjallisesti tai puhelumuistiinpanon mukaan spontaanisti
  näihin seikkoihin päätöksen perusteena ennen sopimusta tai sen yhteydessä;
  (d) yhteys syntyi kolmannen osapuolen kautta, joka tuntee omistajan.
  (a), (b) ja (d) ovat mekaanisia; (c) vaatii molempien luokittelijoiden saman
  tulkinnan sanatarkasta tekstistä, muuten "epäselvä".
- Tapaus, joka on potentiaalisesti piilopääoma-avusteinen, raportoidaan erikseen eikä
  kelpaa vipuvaikutuksen näytöksi (LAHTORESURSSISAANTO §3). Se ei ole PASS.

**Nimittäjäketju (raportoidaan aina kokonaisuudessaan, jokainen luku erikseen):**

| Taso | Määritelmä | Tunnus |
|---|---|---|
| otos | arvotut rivit aalloissa 1 - 2, poissulut korvattu varalta | N_s (= 120, jos varaa riittää) |
| tavoitettavissa | yleisosoite, lomake tai puhelin löytyi (ei C0) | N_ct |
| kontaktoitu | A1 lähetetty tai A3 yritetty | N_c |
| tavoitettu | C4: näyttö, että yrityksen henkilö luki tai kuuli tarjouksen | N_r |
| kiinnostunut | R-INT | N_i |
| sopimus | R-CONTRACT (molemmat allekirjoitettu) | N_k |
| aineisto | R-DATA | N_d |
| PASS | §9 | N_p |

Jokainen suhdeluku ilmoitetaan nimittäjänsä kanssa (esim. N_r/N_c, N_i/N_r, N_p/N_r).
Hylkäysasteita ei koskaan lasketa kontaktoiduista vaan tavoitetuista: kontaktoitu
mutta ei tavoitettu on kanavatulos, ei tarjouksen hylkäys. Muut mittarit: aika
ensimmäiseen PASSiin, omistajan tunnit askeleittain, eurot, kieltäytymissyiden jakauma
tavoitetuista, piilopääomasignaalien määrä.

**Luokittelu:** omistaja kirjaa; Claude luokittelee itsenäisesti samasta raakatekstistä
(vastaukset ja puhelumuistiinpanot ilman nimiä). C4-, R-NO-luokka ja PASS vaativat
molempien saman luokituksen; erimielisyys kirjataan "epäselvä" eikä laske kumpaankaan.

## 9. PASS / FAIL / UNKNOWN (lukitaan L1:ssä, ei muuteta sen jälkeen)

**ACCESS PASS:** vähintään yksi yritys, jolle kaikki seuraavat ovat tosia:
1. Kuuluu lukittuun otokseen (K06-001 - 120 tai varalta korvattu ennen yhteydenottoa)
   eikä ole poissulkukoodilla merkitty. Populaatio on §4:n K1 - K8; otannan jälkeen ei
   sovelleta muita ehtoja.
2. Aineisto on vastaanotettu ja täyttää §5:n vähimmäisvaatimuksen. Tarkistus rajataan:
   tiedoston avaus, sarakkeiden olemassaolo, rivimäärä, päivämääräväli, loppusumma.
   Ei toimittajakohtaista tarkastelua, ei tuplahakua, ei mitään analyysiä. Tarkistus
   kirjataan (rivimäärä, kuukaudet, ostovolyymi suuruusluokkana: alle 0,5 M€ / 0,5 - 2 M€ /
   yli 2 M€ per 24 kk). Suuruusluokka raportoidaan mekanismin relevanssin kuvaamiseksi;
   se ei vaikuta PASS-tulokseen.
3. Käsittely- ja salassapitosopimus allekirjoitettu (§5 i), tekoälykäsittely mukana.
4. Palkkioehdot allekirjoitettu (§5 ii): 20 % vain toteutuneesta ja vahvistetusta.
5. Piilopääomaluokittelu (§8) antaa "ei kontaminoi". Jos tapaus on potentiaalisesti
   piilopääoma-avusteinen, se raportoidaan erikseen eikä ole PASS.
6. Reitti kirjataan: miten tuntematon henkilö olisi saanut saman (kehikko, viesti,
   askel, aika, eurot).

PASS ei tarkoita, että mekanismi tuottaa rahaa. Se tarkoittaa, että portti G1 on
ylitetty kerran neutraalisti. Seuraava askel PASSin jälkeen: koe 07 (analyysi)
suunnitellaan ja lukitaan ennen aineiston avaamista; sopimus velvoittaa meidät
tekemään analyysin, joten koe 07 ei ole vapaaehtoinen.

**ACCESS FAIL (pakettikohtainen):** 0 PASSia, kun (a) molemmat aallot on ajettu,
(b) **tavoitettuja on vähintään 60 (N_r ≥ 60)**, (c) takaraja ohi. FAILin nimittäjä on
tavoitetut, ei kontaktoidut eikä otos: yritys, joka ei todistettavasti lukenut tai
kuullut tarjousta, ei ole hylännyt sitä. Huono toimitettavuus ei siis voi tuottaa
FAILia; se tuottaa CHANNEL UNKNOWNin. Falsifioi hypoteesin: *"§1:n hankintapaketti
tuottaa ensimmäisen data + tulospalkkio -asiakkaan vähintään 60:stä tavoitetusta
yrityksestä, jotka on arvottu §4:n populaatiosta, 9 viikossa."*
CALC (kolmen sääntö): 0/60 tavoitetusta → onnistumisasteen 95 %:n yläraja 5 %
tavoitettua kohden; 0/100 → 3 %. Nollatulos kertoo altistetuista yrityksistä tämän:
niistä, jotka lukivat tai kuulivat tämän tarjouksen, alle 5 % (95 %:n yläraja) eteni
sopimukseen ja aineistoon 9 viikossa. Se ei kerro mitään yrityksistä, joita ei
tavoitettu, eikä siitä, miksi tavoitetut hylkäsivät (kieltäytymissyyt raportoidaan
erikseen, N_r nimittäjänä).

FAIL **ei** falsifioi: recovery audit -mekanismiperhettä; muita pääsyreittejä
(sisääntuleva, tilitoimistokumppani, maksettu mainonta, alustat, suositukset
ensimmäisen asiakkaan jälkeen); muita markkinoita; muita tarjousmuotoja (kiinteä
hinta, pilottimaksu); paketin muita kokoonpanoja; pidempää aikaikkunaa tai
suurempaa otosta; eikä sitä, että sama paketti toimisi vakiintuneelle toimijalle.
Kieltäytymissyiden jakauma kertoo, mikä portin osa petti (huomio, luottamus vai
tarjous), ja se kirjataan seuraavan kokeen syötteeksi.

**UNKNOWN, kolme muotoa:**
- **CHANNEL UNKNOWN:** tavoitettuaste N_r/N_c < 40 % aallon 1 D21:nä (aalto 2 ei
  käynnisty), tai lopussa N_r < 60. Koe ei tällöin erota tarjouksen hylkäystä
  tavoittamattomuudesta riittävällä määrällä. Kirjataan tuoreen verkkotunnuksen ja
  yleisosoitteiden rajoitteena; nimittäjäketju raportoidaan silti kokonaan (tavoitettujen
  joukossa syntyneet R-NO/R-INT kirjataan, mutta niistä ei tehdä FAIL-päätelmää).
  Jatko päätetään erikseen (varamarkkina Ruotsi tai kirjekanava vaatisi uuden
  budjettipäätöksen).
- **ACCESS UNKNOWN:** 0 PASSia mutta A6-jatkon jälkeen vähintään yksi R-CONTRACT tai
  R-DATA (portti puoliksi auki: sopimus ilman aineistoa tai aineisto ilman
  sopimusta). Ei uusia yhteydenottoja; tapaus seurataan 2027-01-31 asti ja tulos
  päivitetään kerran.
- **INCOMPLETE:** omistajan 35 h täyttyi tai takaraja ohitettiin ennen kuin
  molemmat aallot ehtivät A3:een. Kirjataan kapasiteettirajoitteena, ei tuloksena.

**Mitä nollatulos ei saa tehdä:** yhden markkinan, yhden viestiversion ja yhden
kanavayhdistelmän FAIL ei tapa mekanismiperhettä. Se tappaa vain yllä kursivoidun
hypoteesin yhdestä hankintapaketista. Perheen tappamiseen tarvittaisiin vähintään
kaksi riippumatonta pääsyreittiä FAIL-tuloksella samasta populaatiosta.

## 10. Budjetti ex ante

| Erä | € (yläraja) | Mihin porttiin tai parametriin vaikuttaa |
|---|---|---|
| .fi-verkkotunnus 1 v | 27 | Sähköpostikanavan olemassaolo; identiteetin neutraalius (ei olemassa olevan yrityksen verkkotunnus) |
| Sähköposti 3 kk | 21 | Toimitettavuus (SPF/DKIM/DMARC); bounce- ja tavoitettuaste |
| Prepaid-liittymä | 10 | Puhelinvaiheen tavoitettuaste; identiteetin erottelu numerohaussa |
| Sivun isännöinti | 0 | Uskottavuus (tarkistettavuus) |
| Sopimuspohjat, tietosuojaseloste, esimerkkiraportti | 0 | Portit (b) ja (c) |
| Varaus DNS/virhe | 10 | |
| **Yhteensä** | **≤ 68, katto 120** | |

Ei budjetoitu, tietoisesti: juristin tarkastus (200 - 500 €; sopimusriski kirjattu),
kirjeposti (3,00 € × 120 = 360 €), maksettu mainonta, yhteystietodatan osto,
LinkedIn Premium, tokenikulut rajapinnasta (mallit tilausten sisällä, 0 € suunniteltu).
Mitään ei kuluteta ennen lukitusta L1 ja omistajan lupaa. Ledgeriin kirjataan
jokainen euro.

**Omistajan aika (yläraja 35 h):** rakennus 7 h; yhteystiedot 120 × 3 min = 6 h;
lähetys ja muistutus 120 × 3 min = 6 h; puhelut ≤ 100 × 6 min = 10 h; tapaamiset
≤ 5 × 1 h = 5 h; sopimus ja aineisto ≤ 2 × 1 h. Tunnit kirjataan askeleittain, koska ne
ovat mekanismin todellinen kustannus.

## 11. AI-attribuutio, kirjattu etukäteen

Koko tutkimuksen kohde on "yksi ihminen + kaksi mallia + 1 000 €". Tästä kokeesta
halutaan myöhemmin sanoa jotain mallien vaikutuksesta ilman keinotekoista A/B-koetta,
joka puolittaisi otoksen ja heikentäisi pääkokeen evidenssiä.

**Mitä mitataan (FACT-tason kirjaus):** jokaisesta mallien tekemästä tai avustamasta
työvaiheesta kirjataan mitattu aika (mallin ajo ja omistajan tarkistus erikseen) ja
kustannus (0 € tilausten sisällä; rajapintakulut, jos niitä syntyy): (1) kehikon
rakennus kahdesta avoimesta massadatasta (463 805 + 384 627 riviä, liitos, suodatus;
mitattu 2026-09-16: skriptin laatiminen ja ajo yhdessä istunnossa, ajo 7 s);
(2) sopimuspohjien, tietosuojaselosteen ja sivun luonnostelu; (3) yhteystietojen
haku 120 yritykselle; (4) viestien ja lokin laadinta; (5) vastausten riippumaton
toinen luokittelu. Lisäksi kirjataan, mitä mallit eivät tee: puhelut, tapaamiset,
allekirjoitus, luottamuksen synnyttäminen ihmisenä. Jos PASS syntyy vasta askeleessa
A3 tai A4, ratkaiseva askel oli ihmisen; mallien osuus oli infrastruktuuri ja
valmistelu. Kirjataan myös negatiivinen vaikutus: vastaanottajien maininnat "tekoälyn
kirjoittama" tai "roskaposti".

**Mitä ei väitetä:** ihmisen vastafaktuaalista aikaa tai kustannusta ilman malleja
ei mitata, koska kontrollia ei ajeta. Kaikki "ilman malleja olisi vienyt X"
-lausumat ovat INFERENCE, eivät tulos, ja ne merkitään sellaisiksi, jos niitä
esitetään. Tämän kokeen tulos on mitattu AI-avusteinen aika ja kustannus per
työvaihe, ei vipukerroin.

**Mikä lopputulos ei riitä osoittamaan AI-vipua:** PASS osoittaa, että tuntematon
toimija näillä työkaluilla ylitti portin mitatulla ajalla ja rahalla. Se ei osoita,
ettei sama ihminen ilman malleja olisi ylittänyt sitä. FAIL ei osoita, että mallit
olivat hyödyttömiä, eikä PASS, että ne olivat välttämättömiä. Attribuutioväite
rajataan: "portin rakennus ja yhteydenotto maksoivat mallien kanssa X tuntia
ihmisaikaa ja Y euroa" (mitattu) sekä "vastaajat mainitsivat / eivät maininneet
tekoälyä" (mitattu). Vipukertoimen arviointi jää myöhempään, erikseen suunniteltuun
vertailuun, jos sellainen joskus tehdään.

## 12. Hyökkäys omaa protokollaa vastaan

| Uhka | Mekanismi | Korjaus tässä protokollassa | Jäännösriski |
|---|---|---|---|
| Piilopääoma: omistajan nimi | Vastaanottaja hakee nimen ja löytää olemassa olevan yrityksen tai ammatillisen historian | Nimi pakollinen (203 §, rehellisyys); kolme piilopääomakysymystä jokaisessa tapaamisessa; §8:n luokittelusääntö (Q1 = KYLLÄ tai Q3 = KYLLÄ tai spontaani viittaus → potentiaalisesti piilopääoma-avusteinen, ei PASS) | Hiljainen vaikutus (haki, ei sano, ei myönnä Q3:ssa) jää mittaamatta. Hyväksytty ja raportoidaan rajoitteena |
| Piilopääoma: oikeushenkilön ikä | Alatunnisteen y-tunnus paljastaa yrityksen iän ja liikevaihdon YTJ:stä/Finderistä; tuntematon henkilö uudella Oy:llä näyttäisi eri | Oikeushenkilösääntö sallii; pelkkä tarkistus julkisesta rekisteristä ei kontaminoi (§8); ei mainita ikää tai historiaa; Q3 kysyy suoraan, vaikuttiko historia | Todellinen jäännöskonfoundi; sen suunta on PASSia suosiva. Jos Q3 = KYLLÄ tai vastaaja viittaa spontaanisti historiaan, tulos on potentiaalisesti piilopääoma-avusteinen |
| Piilopääoma: omistajan myynti- tai puhelintaito | Tavallinen osaaminen säännön mukaan | Käsikirjoitus P1 kiinteä; poikkeamat kirjataan | Ihmisen ääni on osa mekanismia, ei konfoundi |
| Valikoituminen: poissulut | Omistaja voi sulkea pois "vaikeita" yrityksiä | Vain viisi koodia; määrä committoidaan; > 15 kirjataan havaintona | Koodien väärinkäyttö ei ole tarkistettavissa ulkoa; luottamus omistajaan |
| Valikoituminen: kehikko | K8 suosii kannattavia; yhteystiedon löytyminen suosii digitaalisia | Raportoidaan C0-osuus ja jakaumat; FAIL koskee tätä populaatiota | Tulos ei yleisty tappiollisiin tai verkossa näkymättömiin yrityksiin |
| Kanava: tuore verkkotunnus | Viestit roskapostiin; tulos mittaa suodatinta | R7-testi, hidas nousu, DMARC; A3 kysyy "saitteko"; CHANNEL UNKNOWN -sääntö | Roskapostiin menoa ei voi mitata suoraan; puhelinvaihe on korjaus |
| Kanava: yleisosoitteen seulonta | Vaihde/assistentti ei välitä | A3 pyytää vastuuhenkilöä | Osa hylkäyksistä on portinvartijan, ei päättäjän |
| Kanava: ajoitus | Loka-marraskuu, tilinpäätöskiireet | Kirjataan; ei korjata | n = 1 ajankohta |
| Markkina | Suomi pieni; tulospalkkio vieras | Rajattu johtopäätös; varamarkkina kirjattu | Ei yleisty |
| Liian heikko PASS | Osittainen CSV + suullinen "ok" | Kuusi ehtoa; 24 kk + maksut; molemmat sopimukset allekirjoitettu; kaksi luokittelijaa | "Käyttökelpoinen" ei tarkoita "virheitä sisältävä"; PASS-yrityksen ostovolyymi voi olla pieni (raportoidaan suuruusluokkana, ei PASS-ehto) |
| Liian vahva KILL | Yksi markkina tappaisi perheen | FAIL rajattu kursivoituun hypoteesiin yhdestä paketista; nimittäjä tavoitetut (N_r ≥ 60), ei otos; perheen tappo vaatii kaksi reittiä | Houkutus tulkita FAIL laajemmin; päätösloki sitoo |
| Jälkikäteinen populaatioehto | Otannan jälkeen lisätty raja (esim. liikevaihto) muuttaisi populaation | Populaatio on K1 - K8, lukittu ennen otantaa; §4 kieltää lisäehdot | Ei |
| Väärä positiivinen 1 | Yritys haluaa ilmaisen tarkastuksen eikä aio maksaa | PASS on porttitulos, ei tulo; palkkioehto allekirjoitettu; maksukäyttäytyminen on koe 07:n asia | PASS ≠ raha, sanottu §9 |
| Väärä positiivinen 2 | Yritys sanoo kyllä uteliaisuudesta tai kokeilunhalusta | Tarjous esitetään kaupallisena palveluna, ei tutkimuksena; sopimus on aito ja velvoittaa meidät | Uteliaisuus on aito syy ostaa; ei konfoundi |
| Väärä positiivinen 3 | PASS syntyy omistajan puhelinvaiheessa, ja tulkitaan "kylmä sähköposti toimii" | VAIHE kirjataan; tulos raportoidaan askeleittain | Ei |
| Väärä positiivinen 4 | Tutkimusrepo löytyy brändin nimellä; vastaaja auttaa "tutkimusta" | Brändi ja verkkotunnus eivät tule repoon; sivu ei linkitä tutkimukseen | Jos vuotaa, koko koe merkitään kontaminoituneeksi |
| Väärä positiivinen 5 | Vastaaja on itse myyjä (tilitoimisto, ohjelmistotalo) ja haluaa kumppanuuden | Ei PASS: populaatio on ostaja; kirjataan R-INT-MUU | Ei |
| Väärä negatiivinen | Sopimuspohjat ilman juristia pelottavat | Pohjat lyhyet, selkokieliset, ladattavissa etukäteen; kieltäytymissyy LUOTTAMUS/sopimus kirjataan erikseen | Todellinen; raportoidaan |
| Kaksi koetta samaan aikaan | Koe 04:n sisääntuleva sekoittuu | S1 vasta 2026-10-01 jälkeen; X-K04-poissulku; eri identiteetit | Koe 04:n myöhäiset yhteydenotot kirjataan koe 04:lle, ei tähän |
| Tutkimusetiikka | Vastaanottajat eivät tiedä olevansa kokeessa | Tarjous on aito ja velvoittava; julkinen raportti ei nimeä ketään; markkinointikieltoa kunnioitetaan välittömästi | Hyväksytty: sama kuin mikä tahansa uuden palvelun lanseeraus |

Korjattu tämän hyökkäyksen perusteella ennen GPT:tä: (1) brändi pois julkisesta
reposta; (2) puhelinvaihe lisätty erottamaan tavoittamattomuus hylkäyksestä; (3)
CHANNEL UNKNOWN erotettu FAILista; (4) piilopääomakysymykset pakollisiksi; (5)
tarjous kaupallisena, ei tutkimuksena.

Korjattu GPT:n tuhoamisyrityksen (commit `2ab7a25`, READY AFTER CORRECTIONS) perusteella
2026-09-17: (6) liikevaihtoraja poistettu PASS-ehdosta, populaatio lukittu K1 - K8:aan
ennen otantaa, PASS-PIENI ja PRH-tilinpäätösosto poistettu; (7) nimittäjäketju
otos → tavoitettavissa → kontaktoitu → tavoitettu → kiinnostunut → sopimus → aineisto
→ PASS eksplisiittiseksi, FAIL nimittäjänä tavoitetut (N_r ≥ 60), hypoteesi muotoiltu
tavoitetuista; (8) koe kirjattu yhden lukitun hankintapaketin testiksi; (9) V1:n
väite suuryritysten ja pk-yritysten käytännöistä poistettu; (10) piilopääomasääntö
objektiiviseksi: julkinen rekisteritarkistus ei kontaminoi, ennen koetta kertyneen
historian vaikutus kontaminoi (Q1/Q3/spontaani/kolmas osapuoli); (11) AI-attribuutiosta
poistettu mittaamattomat vastafaktuaaliväitteet, kirjataan vain mitattu AI-avusteinen
aika ja kustannus.

Ei korjattu, tietoisesti: y-tunnuksen paljastama yrityksen ikä (sääntö sallii;
uuden yrityksen perustaminen hylätty omistajan päätöksellä); n = 1 viestiversio
(A/B puolittaisi otoksen); juristin puute.

## 13. Suhde muihin kokeisiin

- **Koe 04** jatkuu koskemattomana. Koe 06 alkaa vasta sen ACCESS-ikkunan jälkeen.
  Koe 04:n kautta tuleva pääsy on reitti R1 ja käsitellään koe 04:ssä, ei tässä.
- **Koe 05** superseded; sen 20 %:n palkkio ja "puhdas pääsytesti" -periaate säilyvät,
  mutta populaatio, kanava, otanta, kynnykset ja identiteetti on rakennettu uudelleen.
- **Koe 07** (analyysi) lukitaan vain PASSin jälkeen ja ennen aineiston avaamista;
  sen budjetti on erillinen haara.

## 14. Lukituksen tarkistuslista

- [x] L0: kehikko rakennettu, SHA-256 ja suppilo committoitu (2026-09-16)
- [x] GPT:n tuhoamisyritys tähän protokollaan ja `06-viesti.md`:hen (commit `2ab7a25`: READY AFTER CORRECTIONS, kuusi korjausta)
- [x] Korjaukset tehty 2026-09-17 (§12 kohdat 6 - 11)
- [x] GPT tarkisti korjausdiffin `ee116d4`: APPROVED FOR LOCK; protokolla lukittu 2026-09-17
- [x] L1: otos arvottu siemenellä 20260917, SHA-256 ja jakaumat committoitu (`06-otos-tiivistelma.json`), nimet repon ulkopuolella
- [ ] Poissulkukierros: mekaaninen osa tehty 2026-09-17 (X-DUPL 0, X-K04 0 koe 04:n tilanteessa 2026-09-17); omistajan osa (X-TUTTU, X-ASIAKAS, X-KONSERNI) odottaa; koodit ja määrä committoidaan sen jälkeen
- [ ] Omistajan lupa rahankäyttöön (≤ 120 €) ja brändin nimelle (nimi ei repoon)
- [ ] R1 - R7 valmiit; R7-toimitettavuustesti kirjattu
- [ ] Koe 04:n ACCESS-ikkuna päättynyt (≥ 2026-10-01)
- [ ] Omistajan käynnistyslupa → S1 kirjataan lokiin
