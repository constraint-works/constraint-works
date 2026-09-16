> **SUPERSEDED 2026-09-16.** Tämä protokolla käytti omistajan olemassa olevaa verkostoa
> pääsyn hankintaan ja rikkoo lähtöresurssisääntöä (`etsinta/LAHTORESURSSISAANTO.md`).
> Sitä ei suoritettu eikä ketään kontaktoitu. Säilytetään historiassa. Korvaava neutraali
> pääsytesti suunnitellaan koe 06:na koe 04:n jälkeen.

# Koe 05: pääsytesti omassa verkostossa, lukittu protokolla

Lukittu 2026-09-16 omistajan korjausten jälkeen. Korvaa `etsinta/RISTIINARVIO-WORK.md`
§6:n luonnoksen. Ei suoritettu. Ei yhteydenottoja ennen omistajan hyväksyntää.

## Mitä koe ratkaisee, ja vain sen

**Saammeko oikean ostolaskuaineiston ja etukäteen sovitun oikeuden 20 prosenttiin
toteutuneesta palautuksesta?**

Koe testaa yhtä pääsyreittiä: omistajan nykyisen oman verkoston kautta saatavaa
luottamusta ja aineistolupaa. Se ei testaa recovery-mekanismia, virhetasoa,
palautussummia eikä mitään muuta pääsyreittiä.

## Mitä kokeen aikana ei tehdä

Ei analysoida laskuja. Ei rakenneta työkalua. Ei käytetä tekoälyä aineistoon. Ei
etsitä virheitä. Ei arvioida potentiaalista palautussummaa. Ei käytetä rahaa. Jos
aineisto tulee, se tallennetaan repon ulkopuolelle koskemattomana, ja varsinainen
analyysikoe suunnitellaan ja lukitaan erikseen ennen kuin aineistoa avataan.

## Kohdejoukko

Omistaja valitsee enintään kolme henkilöä, jotka omistavat tai hoitavat pk-yrityksen
kirjanpitoa. Nimiä ja yrityksiä ei kirjata repoon. Kokeessa käytetään tunnisteita
**K05-A, K05-B, K05-C**. Kohdejoukko lukitaan ennen ensimmäistä yhteydenottoa
(omistaja ilmoittaa Claudelle "kolme valittu", ei nimiä). Kieltäytynyttä tai
vastaamatonta ei korvata uudella henkilöllä kokeen aikana.

## Tarjouksen sisältö, identtinen kaikille

- Pieni kokeellinen selvitys; tulos voi olla nolla.
- Pyydetään lukuoikeus 2 - 3 vuoden ostolaskuaineistoon (laskut ja maksut, CSV tai
  kirjanpito-ohjelman vienti).
- Tarkoitus on myöhemmin etsiä mahdollisia rahallisia virheitä tai takaisin saatavia
  maksuja.
- Asiakkaalle ei synny kustannusta, jos mitään ei saada takaisin.
- **Palkkio: 20 % toteutuneesta ja vahvistetusta takaisin saadusta rahasta.** Ei
  palkkiota epäillystä virheestä, teoreettisesta säästöstä, tunnistetusta poikkeamasta
  eikä summasta, jota asiakas ei tosiasiassa saa takaisin.
- Yritys perii tai hakee itse; me tuotamme vain listan ja perustelut (ei perintää
  toisen lukuun).
- Tässä vaiheessa kysytään vain halukkuutta osallistua.

Viesti: `kokeet/05-pyynto.md`. Sitä ei muuteta henkilöiden välillä.

## Mittarit

Per henkilö kirjataan: pyyntöpäivä, vastaus (kyllä ja aineisto toimitettu / kyllä
periaatteessa, aineisto ei tullut / ei / ei vastausta), aineiston saapumispäivä,
kieltäytymisen syy sanatarkasti jos annettu, luokiteltuna ennalta: luottamus (data
ulkopuoliselle), hyöty (ei usko löytyvän), vaiva, muu.

- **Y** = henkilöt, jotka hyväksyvät 20 %:n periaatteen *ja* toimittavat soveltuvan
  aineiston 14 päivän sisällä pyynnöstä.
- **P** = hyväksyvät periaatteessa, aineisto ei käytössä 14 päivässä.
- **E** = ei tai ei vastausta.

"Soveltuva aineisto" = vähintään 24 kuukauden ostolaskut ja niiden maksutapahtumat
koneluettavassa muodossa. Osittainen aineisto (alle 24 kk tai vain laskut ilman
maksuja) kirjataan P:ksi.

## Tulkinta (lukittu ennen ajoa)

- **PASS:** Y ≥ 1. Pääsyportti on ylitetty ainakin yhdessä oikeassa tapauksessa.
  Seuraava koe saa testata varsinaista recovery-mekanismia; se suunnitellaan ja
  lukitaan erikseen ennen aineiston avaamista, tappiobudjetin 200 € sisällä.
- **ACCESS FAIL:** Y = 0 kolmesta protokollan mukaisen jakson jälkeen. Tappaa **vain**
  hypoteesin "saamme recovery-auditin ensimmäisen oikean aineiston halvasti nykyisen
  oman verkoston kautta". Se **ei** tapa recovery audit / data + success fee
  -mekanismiperhettä eikä muita pääsyreittejä (sisääntuleva koe 04:n kautta,
  kirjanpitäjäkumppani, luvallinen kylmä yhteydenotto). Kieltäytymissyyt kirjataan
  pääsyreitin esteinä. ACCESS FAILia ei muuteta jälkikäteen yleiseksi KILLiksi.
- **UNKNOWN:** Y = 0 ja P ≥ 1. Sallitaan yksi ennalta määritelty muistutus (sama
  viesti lyhyesti: "vieläkö kiinnostaa, aineiston voi toimittaa näin") ja toinen
  14 päivän jakso. Jos aineisto ei sittenkään ole käytössä, tulos kirjataan
  ACCESS FAILiksi tälle pääsyreitille.

Otos on kolme valikoitunutta henkilöä. Tulos ei ole estimaatti mistään
populaatiosta; se on yhden oven avaus- tai sulkeutumishavainto.

## Kustannus ja aikaraja

0 € tappiobudjetista. Omistajan aikaa 1 - 2 h (kolme keskustelua) + mahdollinen
muistutus. Claude: viestin laadinta, kirjaus, päivämäärien seuranta. Koe päättyy
viimeistään 28 päivää ensimmäisestä pyynnöstä (14 + muistutus + 14).

## Kirjaus

`kokeet/05-loki.md`: K05-A/B/C, päivämäärät, vastausluokka, kieltäytymissyy
luokiteltuna, ei nimiä, ei yrityksiä, ei aineiston sisältöä. Aineisto ei tule
repoon (gitignore).

## Suhde muihin kokeisiin

Rinnakkainen koe 04:n kanssa. Kumpikaan ei odota toista. Workin 150 euron
analyysipilotti voidaan suunnitella vasta PASSin jälkeen.
