# Koe 06: kylmä pääsytesti neutraalista lähtötilanteesta (ACCESS)

**Tila: LUONNOS, ODOTTAA GPT:N TUHOAMISYRITYSTÄ. Ei lukittu. Ei käynnistetty.**
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
| R9 | Tilinpäätöksen osto PASS-yrityksestä (Virre 5,02 €) | Tutkimuksen hallinto | ≤ 15 (≤ 3 kpl) | 0,2 h | Populaatiojäsenyyden ja kokoluokan varmennus PASSissa |

Yhteensä: 22 - 73 € ja noin 7 h ennen ensimmäistä viestiä. Se, mitä 1 000 eurolla **ei**
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
osa saavutettavuusmittausta (§7).

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
| PIILOPÄÄOMA | Tapaamisessa tai sopimusvaiheessa kysytään aina samat kaksi kysymystä (`06-viesti.md` §5): tunsiko vastaaja lähettäjän tai oikeushenkilön ennestään; mistä hän tarkisti meidät (sivu, y-tunnus, haku, ei mistään). Vastaus kirjataan. Lisäksi kirjataan spontaanit signaalit: mainitsiko olemassa olevan yrityksen, kysyikö referenssejä, epäilikö tekoälyn kirjoittamaksi tai roskapostiksi |
| AIKA | Omistajan minuutit per askel; mallien käyttö (kyllä/ei, mihin) |

Kokonaismittarit: kontaktoidut N_c (C1 tai A3 tehty), tavoitettuaste C4/N_c,
vastausaste (mikä tahansa vastaus)/N_c, kiinnostusaste R-INT/N_c, PASS-määrä, aika
ensimmäiseen PASSiin, omistajan tunnit askeleittain, eurot, kieltäytymissyiden
jakauma, piilopääomasignaalien määrä.

**Luokittelu:** omistaja kirjaa; Claude luokittelee itsenäisesti samasta raakatekstistä
(vastaukset ja puhelumuistiinpanot ilman nimiä). C4-, R-NO-luokka ja PASS vaativat
molempien saman luokituksen; erimielisyys kirjataan "epäselvä" eikä laske kumpaankaan.

## 9. PASS / FAIL / UNKNOWN (lukitaan L1:ssä, ei muuteta sen jälkeen)

**ACCESS PASS:** vähintään yksi yritys, jolle kaikki seuraavat ovat tosia:
1. Kuuluu lukittuun otokseen (K06-001 - 120 tai varalta korvattu ennen yhteydenottoa)
   eikä ole poissulkukoodilla merkitty; PRH:n tilinpäätöksestä (5,02 €) tarkistetaan,
   että yritys on aktiivinen ja sen liikevaihto on ≥ 0,5 M€ viimeisellä tilikaudella
   (populaation ostointensiivisyyden vähimmäisvarmistus; jos alle, tulos on
   PASS-PIENI ja se raportoidaan erikseen, ei lasketa PASSiksi).
2. Aineisto on vastaanotettu ja täyttää §5:n vähimmäisvaatimuksen. Tarkistus rajataan:
   tiedoston avaus, sarakkeiden olemassaolo, rivimäärä, päivämääräväli, loppusumma.
   Ei toimittajakohtaista tarkastelua, ei tuplahakua, ei mitään analyysiä. Tarkistus
   kirjataan (rivimäärä, kuukaudet, summa suuruusluokkana).
3. Käsittely- ja salassapitosopimus allekirjoitettu (§5 i), tekoälykäsittely mukana.
4. Palkkioehdot allekirjoitettu (§5 ii): 20 % vain toteutuneesta ja vahvistetusta.
5. Piilopääomatarkistus: vastaaja ilmoittaa, ettei tuntenut lähettäjää eikä
   oikeushenkilöä ennestään. Jos tunsi, tapaus on PIILOPÄÄOMA-AVUSTEINEN eikä PASS
   (LAHTORESURSSISAANTO §3).
6. Reitti kirjataan: miten tuntematon henkilö olisi saanut saman (kehikko, viesti,
   askel, aika, eurot).

PASS ei tarkoita, että mekanismi tuottaa rahaa. Se tarkoittaa, että portti G1 on
ylitetty kerran neutraalisti. Seuraava askel PASSin jälkeen: koe 07 (analyysi)
suunnitellaan ja lukitaan ennen aineiston avaamista; sopimus velvoittaa meidät
tekemään analyysin, joten koe 07 ei ole vapaaehtoinen.

**ACCESS FAIL (reittikohtainen):** 0 PASSia, kun (a) molemmat aallot on ajettu
(N_c ≥ 100), (b) tavoitettuaste C4/N_c ≥ 50 %, (c) takaraja ohi. Falsifioi
hypoteesin: *"Tuore brändi, oikea oikeushenkilö, läpinäkyvät ehdot ja suomenkielinen
kylmä sähköposti + puhelu tuottavat ensimmäisen data + tulospalkkio -asiakkaan
120 yrityksen otoksesta suomalaisista ostointensiivisistä osakeyhtiöistä 9 viikossa."*
CALC: 0/120 → onnistumisasteen 95 %:n yläraja noin 2,5 % (kolmen sääntö); 0/60 → 5 %.

FAIL **ei** falsifioi: recovery audit -mekanismiperhettä; muita pääsyreittejä
(sisääntuleva, tilitoimistokumppani, maksettu mainonta, alustat, suositukset
ensimmäisen asiakkaan jälkeen); muita markkinoita; muita tarjousmuotoja (kiinteä
hinta, pilottimaksu); pidempää aikaikkunaa tai suurempaa otosta; eikä sitä, että
sama reitti toimisi vakiintuneelle toimijalle. Kieltäytymissyiden jakauma kertoo,
mikä portin osa petti (huomio, luottamus vai tarjous), ja se kirjataan seuraavan
kokeen syötteeksi.

**UNKNOWN, kolme muotoa:**
- **CHANNEL UNKNOWN:** tavoitettuaste < 40 % aallon 1 D21:nä tai < 50 % lopussa.
  Koe ei erota tarjouksen hylkäystä tavoittamattomuudesta. Kirjataan tuoreen
  verkkotunnuksen ja yleisosoitteiden rajoitteena. Jatko päätetään erikseen
  (varamarkkina Ruotsi tai kirjekanava vaatisi uuden budjettipäätöksen).
- **ACCESS UNKNOWN:** 0 PASSia mutta A6-jatkon jälkeen vähintään yksi R-CONTRACT tai
  R-DATA (portti puoliksi auki: sopimus ilman aineistoa tai aineisto ilman
  sopimusta). Ei uusia yhteydenottoja; tapaus seurataan 2027-01-31 asti ja tulos
  päivitetään kerran.
- **INCOMPLETE:** omistajan 35 h täyttyi tai takaraja ohitettiin ennen kuin
  molemmat aallot ehtivät A3:een. Kirjataan kapasiteettirajoitteena, ei tuloksena.

**Mitä nollatulos ei saa tehdä:** yhden markkinan, yhden viestiversion ja yhden
kanavayhdistelmän FAIL ei tapa mekanismiperhettä. Se tappaa vain yllä kursivoidun
hypoteesin. Perheen tappamiseen tarvittaisiin vähintään kaksi riippumatonta reittiä
FAIL-tuloksella samasta populaatiosta.

## 10. Budjetti ex ante

| Erä | € (yläraja) | Mihin porttiin tai parametriin vaikuttaa |
|---|---|---|
| .fi-verkkotunnus 1 v | 27 | Sähköpostikanavan olemassaolo; identiteetin neutraalius (ei olemassa olevan yrityksen verkkotunnus) |
| Sähköposti 3 kk | 21 | Toimitettavuus (SPF/DKIM/DMARC); bounce- ja tavoitettuaste |
| Prepaid-liittymä | 10 | Puhelinvaiheen tavoitettuaste; identiteetin erottelu numerohaussa |
| Sivun isännöinti | 0 | Uskottavuus (tarkistettavuus) |
| Sopimuspohjat, tietosuojaseloste, esimerkkiraportti | 0 | Portit (b) ja (c) |
| PRH-tilinpäätökset ≤ 3 | 15 | PASS-ehdon 1 varmennus |
| Varaus DNS/virhe | 10 | |
| **Yhteensä** | **≤ 83, katto 120** | |

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

**Mitä mallit tekevät, mitä yksi ihminen ei realistisesti tekisi samassa ajassa:**
(1) kehikon rakennus kahdesta avoimesta massadatasta (463 805 + 384 627 riviä,
liitos, suodatus) alle tunnissa; ihmiselle päiviä tai maksullinen tietopalvelu;
(2) sopimuspohjien, tietosuojaselosteen ja sivun luonnostelu tunneissa; ihmiselle
päiviä tai lakimies; (3) yhteystietojen haku 120 yritykselle avustettuna; (4)
kieltäytymissyiden ja vastausten riippumaton toinen luokittelu.

**Mitä mallit vain nopeuttavat:** viestin kirjoittaminen (ihminen kirjoittaisi saman
hitaammin), lokin pito, aikataulun seuranta, esimerkkiraportti.

**Mitä mallit eivät tee:** puhelut, tapaamiset, allekirjoitus, luottamuksen
synnyttäminen ihmisenä. Jos PASS syntyy vasta askeleessa A3 tai A4, ratkaiseva askel
oli ihmisen; mallien osuus oli infrastruktuuri ja valmistelu.

**Mikä lopputulos ei riitä osoittamaan AI-vipua:** PASS osoittaa, että tuntematon
toimija näillä työkaluilla ylitti portin. Se ei osoita, ettei sama ihminen ilman
malleja olisi ylittänyt sitä; vastafaktuaalia ei ajeta. But-for-arvio tehdään
kirjatuista tunneista: paljonko rakennus- ja hakuaika olisi ollut ilman malleja
(arvio, merkitään INFERENCE). Myös negatiivinen vaikutus mitataan: jos vastaanottajat
mainitsevat "tekoälyn kirjoittama" tai "roskaposti", se kirjataan mallien
kustannuksena. FAIL ei osoita, että mallit olivat hyödyttömiä, eikä PASS, että ne
olivat välttämättömiä. Attribuutioväite rajataan: "mallit laskivat portin rakennuksen
kustannuksen X tunnista Y tuntiin" (mitattu) ja "mallit eivät vaikuttaneet
hyväksymisasteeseen tunnistettavasti" tai "vaikuttivat" (vain jos vastaajat mainitsevat).

## 12. Hyökkäys omaa protokollaa vastaan

| Uhka | Mekanismi | Korjaus tässä protokollassa | Jäännösriski |
|---|---|---|---|
| Piilopääoma: omistajan nimi | Vastaanottaja hakee nimen ja löytää olemassa olevan yrityksen tai ammatillisen historian | Nimi pakollinen (203 §, rehellisyys); piilopääomakysymykset jokaisessa tapaamisessa; tunsi ennestään → ei PASS; spontaanit maininnat kirjataan | Hiljainen vaikutus (haki, ei sano) jää mittaamatta. Hyväksytty ja raportoidaan rajoitteena |
| Piilopääoma: oikeushenkilön ikä | Alatunnisteen y-tunnus paljastaa yrityksen iän ja liikevaihdon YTJ:stä/Finderistä; tuntematon henkilö uudella Oy:llä näyttäisi eri | Oikeushenkilösääntö sallii; ei mainita ikää; kirjataan, jos vastaaja viittaa siihen | Todellinen jäännöskonfoundi; sen suunta on PASSia suosiva. Jos PASS syntyy ja vastaaja mainitsee yrityksen historian, tulos merkitään PIILOPÄÄOMA-AVUSTEINEN |
| Piilopääoma: omistajan myynti- tai puhelintaito | Tavallinen osaaminen säännön mukaan | Käsikirjoitus P1 kiinteä; poikkeamat kirjataan | Ihmisen ääni on osa mekanismia, ei konfoundi |
| Valikoituminen: poissulut | Omistaja voi sulkea pois "vaikeita" yrityksiä | Vain viisi koodia; määrä committoidaan; > 15 kirjataan havaintona | Koodien väärinkäyttö ei ole tarkistettavissa ulkoa; luottamus omistajaan |
| Valikoituminen: kehikko | K8 suosii kannattavia; yhteystiedon löytyminen suosii digitaalisia | Raportoidaan C0-osuus ja jakaumat; FAIL koskee tätä populaatiota | Tulos ei yleisty tappiollisiin tai verkossa näkymättömiin yrityksiin |
| Kanava: tuore verkkotunnus | Viestit roskapostiin; tulos mittaa suodatinta | R7-testi, hidas nousu, DMARC; A3 kysyy "saitteko"; CHANNEL UNKNOWN -sääntö | Roskapostiin menoa ei voi mitata suoraan; puhelinvaihe on korjaus |
| Kanava: yleisosoitteen seulonta | Vaihde/assistentti ei välitä | A3 pyytää vastuuhenkilöä | Osa hylkäyksistä on portinvartijan, ei päättäjän |
| Kanava: ajoitus | Loka-marraskuu, tilinpäätöskiireet | Kirjataan; ei korjata | n = 1 ajankohta |
| Markkina | Suomi pieni; tulospalkkio vieras | Rajattu johtopäätös; varamarkkina kirjattu | Ei yleisty |
| Liian heikko PASS | Osittainen CSV + suullinen "ok" | Kuusi ehtoa; 24 kk + maksut; molemmat sopimukset allekirjoitettu; kaksi luokittelijaa; tilinpäätösvarmennus | "Käyttökelpoinen" ei tarkoita "virheitä sisältävä" |
| Liian vahva KILL | Yksi markkina tappaisi perheen | FAIL rajattu kursivoituun hypoteesiin; perheen tappo vaatii kaksi reittiä | Houkutus tulkita FAIL laajemmin; päätösloki sitoo |
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
PASS-PIENI erotettu PASSista; (6) tarjous kaupallisena, ei tutkimuksena; (7) FAIL
sidottu tavoitettuasteeseen ≥ 50 %.

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
- [ ] GPT:n tuhoamisyritys tähän protokollaan ja `06-viesti.md`:hen
- [ ] Korjaukset kirjattu; kynnykset §9 lukittu (ei muuteta sen jälkeen)
- [ ] L1: otos arvottu siemenellä, SHA-256 ja jakaumat committoitu, nimet repon ulkopuolella
- [ ] Poissulkukierros tehty, koodit ja määrä committoitu
- [ ] Omistajan lupa rahankäyttöön (≤ 120 €) ja brändin nimelle (nimi ei repoon)
- [ ] R1 - R7 valmiit; R7-toimitettavuustesti kirjattu
- [ ] Koe 04:n ACCESS-ikkuna päättynyt (≥ 2026-10-01)
- [ ] Omistajan käynnistyslupa → S1 kirjataan lokiin
