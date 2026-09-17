# Koe 06: sopimuspohjat, tietosuojaseloste ja sivuteksti (LUONNOS, paikkamerkein)

2026-09-17, Claude. Mallien laatima, **ei juristin tarkastama** (lukittu budjettipäätös).
GPT:n tarkistettavaksi ennen D0:aa. Sisältö noudattaa lukittua protokollaa §5 ja
totuudenmukaisuuskorjausta P1 (hyväksytty 2026-09-17: ei nollasäilytyslupausta,
paikallinen pseudonymisointi, ei koulutuskäyttöä, säilytysaika todellisen
palveluntarjoajan mukaan). GPT:n pre-D0-tarkistus `99a62e9`: APPROVED täsmennyksin (vastuulauseke A hyväksytty;
palkkioehtojen kohta 6 selvennetty). Avoinna vain **[P1]**-hakasulkeiden täyttö ennen
D0:aa todellisen palvelun voimassa olevasta dokumentaatiosta, ei arvauksella.
Paikkamerkit: [Brändi], [verkkotunnus], [Oikeushenkilö Oy], [y-tunnus], [osoite], [Nimi],
[Asiakas Oy]. Täytetyt versiot eivät tule tähän repoon.

## 1. Aineiston käsittely- ja salassapitosopimus

**Osapuolet:** [Asiakas Oy], y-tunnus (rekisterinpitäjä, "Asiakas") ja [Oikeushenkilö Oy],
[y-tunnus], joka tarjoaa palvelua nimellä [Brändi] (henkilötietojen käsittelijä,
"Palveluntarjoaja").

1. **Tarkoitus ja kohde.** Palveluntarjoaja käsittelee Asiakkaan toimittamaa
   ostolasku- ja maksuaineistoa yksinomaan tunnistaakseen mahdollisia aiheettomia tai
   virheellisiä maksuja (kahteen kertaan maksetut laskut, käyttämättömät hyvitykset,
   sopimuksesta poikkeavat hinnat ja vastaavat) ja raportoidakseen ne Asiakkaalle.
   Muuhun tarkoitukseen aineistoa ei käytetä.
2. **Aineisto.** Ostolaskujen ja niiden maksujen tiedot noin 24 - 36 kuukaudelta:
   toimittaja, laskun numero ja päivä, summat, maksupäivät ja -summat, viitteet,
   hyvityslaskut. Henkilötietoja voi sisältyä siltä osin kuin toimittaja on
   yksityinen elinkeinonharjoittaja tai aineistossa on yhteyshenkilöiden nimiä.
   Rekisteröidyt: Asiakkaan toimittajien edustajat ja elinkeinonharjoittajat.
   Erityisiä henkilötietoryhmiä ei käsitellä; Asiakas ei toimita palkka-, potilas- tai
   vastaavia tietoja.
3. **Ohjeet.** Palveluntarjoaja käsittelee henkilötietoja vain tämän sopimuksen ja
   Asiakkaan kirjallisten ohjeiden mukaisesti.
4. **Salassapito.** Kaikki aineisto ja siitä ilmenevät tiedot Asiakkaan
   liiketoiminnasta, toimittajista ja hinnoista ovat luottamuksellisia. Niitä ei
   luovuteta kolmansille, ei käytetä muiden asiakkaiden hyväksi eikä mainita
   referenssinä ilman Asiakkaan erillistä kirjallista lupaa. Salassapito jatkuu viisi
   vuotta sopimuksen päättymisestä. Aineistoa käsittelee vain [Nimi].
5. **Turvatoimet.** Aineisto vastaanotetaan Asiakkaan valitsemalla tavalla (suojattu
   linkki tai salattu liite), säilytetään salattuna EU:n alueella sijaitsevassa
   tallennuksessa ja salatulla työasemalla, ei sähköpostissa eikä julkisissa
   palveluissa. Pääsy vain [Nimi].
6. **Tekoälykäsittely ja alikäsittelijät.** Analyysissä käytetään kaupallisia
   tekoälypalveluja rajapinnan kautta. **[P1]** Luonnollisten henkilöiden nimet ja
   yhteystiedot pseudonymisoidaan paikallisesti ennen tekoälykäsittelyä.
   Tekoälypalvelun tarjoaja ei käytä aineistoa mallien kouluttamiseen.
   Palveluntarjoaja [TEKOÄLYPALVELU] säilyttää syötteitä [SÄILYTYSAIKA JA PERUSTE,
   täsmälleen palveluntarjoajan voimassa olevan dokumentaation mukaan], minkä jälkeen
   ne poistetaan. Käsittelypaikka: [KÄSITTELYPAIKKA]. Alikäsittelijät: (a)
   tallennuspalvelu [nimi, sijainti EU], (b) tekoälypalvelu [TEKOÄLYPALVELU].
   *Täyttöohje (ei sopimustekstiä): hakasulkeet täytetään ennen D0:aa vain sillä
   palveluntarjoajalla, konfiguraatiolla ja säilytysajalla, jota analyysissä todella
   käytetään; lähde ja tarkistuspäivä kirjataan lokiin. Nollasäilytystä ei kirjata,
   ellei se ole todennetusti käytössä.* Siirrot EU:n
   ulkopuolelle tapahtuvat vain komission vakiolausekkeiden tai
   vastaavuuspäätöksen nojalla. Uudesta alikäsittelijästä ilmoitetaan etukäteen, ja
   Asiakas voi vastustaa.
7. **Avustaminen ja tietoturvaloukkaukset.** Palveluntarjoaja avustaa Asiakasta
   rekisteröityjen pyyntöihin vastaamisessa ja ilmoittaa tietoturvaloukkauksesta
   viivytyksettä, viimeistään 24 tunnin kuluessa havaitsemisesta.
8. **Poisto.** Aineisto ja sen kopiot poistetaan 90 päivän kuluessa loppuraportin
   toimittamisesta tai heti Asiakkaan pyynnöstä. Poisto vahvistetaan kirjallisesti.
   Raportti ja palkkiolaskutukseen tarvittavat yksilöinnit säilytetään kirjanpitolain
   vaatiman ajan.
9. **Tarkastusoikeus.** Asiakas voi pyytää selvityksen käsittelystä ja turvatoimista.
10. **Keskeytys.** Asiakas voi keskeyttää työn ja vaatia aineiston poistoa milloin
    tahansa syytä ilmoittamatta. Keskeytys ei synnytä maksuja.
11. **Vastuu.** *(Vaihtoehto A, hyväksytty 2026-09-17: ei euromääräistä kattoa.)*
    Palveluntarjoaja vastaa Asiakkaalle
    sopimusrikkomuksestaan aiheutuneista välittömistä vahingoista. Palveluntarjoaja
    ei vastaa välillisistä vahingoista, kuten saamatta jääneestä voitosta, paitsi jos
    vahinko on aiheutettu tahallisesti tai törkeällä huolimattomuudella tai se johtuu
    salassapito- tai tietosuojavelvoitteiden rikkomisesta. Lauseke ei vaikuta
    rekisteröityjen oikeuksiin.
12. **Laki ja riidat.** Suomen laki; riidat Asiakkaan kotipaikan käräjäoikeudessa.

Hyväksyntä: PDF + sähköpostivahvistus Asiakkaan edustamiseen oikeutetulta henkilöltä
(nimi, asema, päivä).

## 2. Palkkioehdot

1. **Palvelu.** Palveluntarjoaja toimittaa Asiakkaalle kirjallisen raportin, jossa
   jokainen löydös on yksilöity (toimittaja, laskut, summa, perustelu).
2. **Palkkio.** 20 % (+ alv) rahamäärästä, jonka Asiakas tosiasiassa saa takaisin
   raportissa yksilöidyn löydöksen perusteella 12 kuukauden kuluessa raportin
   toimittamisesta: palautus tilille, hyvityslasku tai kuittaus tulevista laskuista.
3. **Ei palkkiota** epäillyistä virheistä, laskennallisista tai tulevista säästöistä,
   löydöksistä, joita Asiakas ei peri tai joita toimittaja ei hyvitä, eikä mistään
   muusta. Ei aloitusmaksua, tuntilaskutusta, vähimmäispalkkiota tai kuluja.
4. **Vahvistus.** Asiakas ilmoittaa saadut palautukset ja vahvistaa summan tiliotteella
   tai hyvityslaskulla. Palkkio laskutetaan vahvistuksen jälkeen, maksuehto 14 pv netto.
5. **Asiakas perii itse.** Asiakas päättää, mitkä löydökset se esittää toimittajille, ja
   hoitaa yhteydenotot. Palveluntarjoaja ei ota yhteyttä toimittajiin eikä peri
   saatavia Asiakkaan lukuun.
6. **Ei yksinoikeutta; keskeytys milloin tahansa.** Asiakas voi keskeyttää palvelun ja
   aineiston käsittelyn milloin tahansa syytä ilmoittamatta ja ilman maksuja. Keskeytys
   ei vaikuta kohdan 2 palkkioon niistä löydöksistä, jotka sisältyvät ennen keskeytystä
   toimitettuun raporttiin: niistä palkkio maksetaan, jos raha palautuu 12 kuukauden
   kuluessa raportin toimittamisesta. Jos raporttia ei ole toimitettu ennen
   keskeytystä, palkkiota ei synny.
7. **Ei takuuta löydöksistä.** Tulos voi olla nolla.
8. Suomen laki; riidat Asiakkaan kotipaikan käräjäoikeudessa.

## 3. Tietosuojaseloste (markkinointi ja yhteydenotot)

Rekisterinpitäjä: [Oikeushenkilö Oy], [y-tunnus], [osoite]; palvelu [Brändi];
yhteys: tietosuoja@[verkkotunnus].
- **Mitä ja miksi:** yritysten yleiset yhteystiedot (yrityksen nimi, y-tunnus,
  toimiala, yleinen sähköpostiosoite, vaihteen numero) ja yhteydenpidon aikana
  saadut yhteyshenkilön nimi ja työyhteystiedot, palvelun tarjoamiseksi yrityksille.
- **Peruste:** oikeutettu etu (yritysten välinen suoramarkkinointi; sähköisen
  viestinnän palveluista annetun lain 202 §). Sopimusvaiheessa sopimus.
- **Lähteet:** Yritys- ja yhteisötietojärjestelmän avoin data, Verohallinnon julkiset
  tiedot, yrityksen omat verkkosivut.
- **Säilytys:** yhteydenottotiedot enintään 12 kuukautta viimeisestä yhteydenotosta;
  kieltäytyneiden osoite estolistalla, jotta uusia viestejä ei lähetetä.
- **Luovutukset:** ei luovuteta. Käsittelijät: sähköpostipalvelu [nimi, sijainti].
- **Oikeudet:** oikeus vastustaa suoramarkkinointia milloin tahansa (vastaus
  "ei viestejä" riittää), oikeus saada pääsy tietoihin, oikaista ja poistaa ne, ja
  oikeus tehdä valitus tietosuojavaltuutetulle (tietosuoja.fi).
- Sivusto ei käytä evästeitä eikä analytiikkaa.

## 4. Verkkosivun teksti (yksi sivu)

**[Brändi]: ostolaskujen tarkastus tulospalkkiolla**

Tarkastamme yrityksenne 2 - 3 vuoden ostolaskut ja maksut ja etsimme rahaa, joka on
maksettu turhaan: kahteen kertaan maksetut laskut, käyttämättä jääneet hyvitykset,
sopimuksesta poikkeavat hinnat.

**Maksatte vain, jos rahaa tulee takaisin.** Palkkio on 20 % summasta, joka palautuu
tilillenne tai hyvitetään teille. Ei aloitusmaksua, ei tuntilaskutusta, ei palkkiota
epäillyistä virheistä. Jos mitään ei löydy, ette maksa mitään.

**Miten se toimii.** 1. Sovimme ehdoista kirjallisesti (pohjat alla). 2. Toimitatte
ostolaskujen ja maksujen viennin kirjanpito-ohjelmasta (Excel tai CSV). 3. Saatte
raportin, jossa jokainen löydös on perusteltu. 4. Te päätätte, mitä esitätte
toimittajillenne, ja hoidatte yhteydenotot. 5. Laskutamme vasta, kun raha on
palautunut ja olette vahvistaneet summan.

**Miten aineistoa suojataan.** Kirjallinen käsittely- ja salassapitosopimus. Salattu
tallennus EU:ssa. Aineistoa käsittelee yksi nimetty henkilö. Analyysissä käytetään
tekoälypalvelua: henkilöiden nimet pseudonymisoidaan ennen käsittelyä, aineistoa ei
käytetä mallien kouluttamiseen, ja palveluntarjoajan säilytysaika on kirjattu
sopimukseen **[P1]**. Aineisto poistetaan 90 päivän kuluessa raportista tai heti
pyynnöstänne. Tietojanne ei käytetä muiden
asiakkaiden hyväksi eikä referenssinä.

**Kuka.** [Nimi]. Palvelu on uusi. Emme esitä referenssejä; siksi ehdot ovat
teille riskittömät.

**Asiakirjat:** käsittely- ja salassapitosopimus (PDF) · palkkioehdot (PDF) ·
esimerkkiraportti keksityllä aineistolla (PDF) · tietosuojaseloste

Yhteys: [sähköposti], [puhelin]. Jos ette halua meiltä viestejä: [kielto-osoite].

Alatunniste: [Brändi] on [Oikeushenkilö Oy]:n palvelu. Y-tunnus [y-tunnus]. [osoite].
