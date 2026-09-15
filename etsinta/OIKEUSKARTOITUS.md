# Oikeuskartoitus: 20 lunastamatonta lakisääteistä oikeutta

Kysymys jokaisesta ei ole "missä on rahaa" vaan **mikä niukka resurssi antaa juuri tälle
henkilölle tai yritykselle oikeuden rahaan**, ja voiko tekoäly havaita oikeuden ennen kuin
omistaja itse ymmärtää sen. Tila: `todennettu` = luku lähteestä, `arvio` = päättely,
`tuntematon` = ei löytynyt.

## Yhteenvetotaulukko

| # | Oikeus | Niukka resurssi | AI havaitsee ennen omistajaa | Jää lunastamatta | Kitka | Lupa / tiedot | Automatisoitava | Yksittäinen vai generaattori | Tuomio |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Lähdeveron palautus ulkomaisista osingoista | Osakkeiden omistus (pääoma) | Kyllä, välittäjän raportista | 8,4 mrd €/v EU (EK 2017), `todennettu` | Lomakkeet per maa, asuinpaikkatodistus, pienet summat | Valtakirja, Veron todistus, henkilötiedot | Kyllä, palveluita on (institutionaalisille) | **Generaattori**: maa × sijoittaja | **Vahva.** Yksityissijoittajat alipalveltuja |
| 2 | EU261-lentokorvaus | Lippu myöhästyneelle lennolle | Kyllä, lentodata + kalenteri | 3,2 mrd € EU, 5 - 30 % hakee, `todennettu` | Tietämättömyys, yhtiöiden viivyttely | Valtakirja. AVI: ei perintää (AirHelp), Finnair riitautti 2017 | Kyllä, tehty | Yksittäinen | Todellinen, mutta täynnä (AirHelp 35 %, Flightright, Confenta) |
| 3 | Viivästyskorko + 40 € perintäkulukorvaus B2B | Velkoja-asema, myöhässä maksettu lasku | Kyllä, laskutusdatasta | 37 % ei hae (EU), € `tuntematon` | Pelko asiakassuhteesta, ei kitka vaan valinta | Oma saatava: ei lupaa. Toisen lukuun: perintälupa | Kyllä, kirjanpito-integraatio | Generaattori: joka lasku | **Keskivahva** ohjelmistona, jota velkoja käyttää itse |
| 4 | Rajat ylittävä alv-palautus (SME) | Ulkomailla maksettu alv, kuitit | Kyllä, kuludatasta | `tuntematon`, palveluntarjoajat väittävät miljardeja | Lomakkeet, määräajat, per maa | Veron valtuutus, Y-tunnus | Kyllä | Generaattori: maa × yritys | Keskivahva, kilpailtu (VAT IT ym.) |
| 5 | Verovähennykset hakematta (kotitalous, matka, työhuone) | Syntynyt kulu | Kyllä, tiliotteesta ja kuiteista | `tuntematon`; myönnetty 538 M € + 1,5 mrd €/v | Tietämättömyys, vaiva | Suomi.fi-valtuutus, henkilötiedot | Kyllä | Generaattori: joka vähennyssääntö | Keskivahva, tilitoimistot ja sovellukset lähellä |
| 6 | Toimeentulotuen alikäyttö | Kelpoisuus (pienituloisuus) | Kyllä, tulodatasta | 20 - 50 % ei hae, `todennettu` (THL) | Stigma, monimutkaisuus | Arkaluonteiset tiedot, Kela-valtuutus | Osittain | Generaattori: joka etuus | **Ei meille ansaintana.** Menestyspalkkio köyhiltä on väärin. Ilmainen työkalu tai julkinen tilaus |
| 7 | Asumistuen ja takuueläkkeen alikäyttö | Kelpoisuus | Kyllä | `arvio` merkittävä | Sama | Sama | Osittain | Sama | Sama kuin 6 |
| 8 | Kilpailukieltokorvaus (laki 2022) | Kilpailukieltoehto työsopimuksessa | Kyllä, sopimustekstistä | `tuntematon` | Tietämättömyys, pelko työnantajasta | Toimeksianto | Kyllä (havaitseminen), ei (neuvottelu) | Yksittäinen | Kapea, kokeiltava pienesti |
| 9 | Tekijänoikeuskorvaukset tilittämättä | Tekijyys | Kyllä, sisällöntunnistus | ~10 % 150 M €:sta ei välitetä, `arvio` | Rekisteröitymättömyys | Järjestön jäsenyys | Osittain | Generaattori: järjestö × tekijä | Keskiheikko, pieniä summia |
| 10 | Potilasvahingot | Vahinko (arkaluonteinen) | Kyllä, potilastiedoista | 10 800 ilmoitusta/v, 24 % korvataan; ilmoittamatta `tuntematon` | Tietämättömyys, raskaus | Terveystiedot, asianajo | Ei | Yksittäinen | **Hylätty.** Terveystiedot, juristit hoitavat |
| 11 | Rautatiematkustajan hyvitys (EU 2021/782) | Lippu | Kyllä, VR:n viivedata | `tuntematon`, VR hyvittää osin automaattisesti | Pieni summa | Valtakirja | Kyllä | Yksittäinen | Heikko, summat 5 - 30 € |
| 12 | Matkatavarakorvaus (Montreal, ~1 600 €) | Kadonnut laukku | Osittain | `tuntematon` | Todistelu | Valtakirja | Osittain | Yksittäinen | Heikko volyymi |
| 13 | Ryhmäkannesovinnot (USA, EU-asukkaat) | Tuotteen käyttö | Kyllä, sähköpostista | `tuntematon` | Tietämättömyys | Henkilötiedot | Kyllä, "Payout" tekee | Generaattori: joka sovinto | Keskiheikko Suomesta |
| 14 | Palkkasaatavat, lomakorvaukset, ylityöt | Työsuhde | Kyllä, palkkalaskelmasta | `tuntematon` | Pelko | Toimeksianto, liitot | Osittain | Generaattori | Heikko, liitot hoitavat |
| 15 | GDPR-korvaukset (art. 82) | Rekisteröity | Kyllä, tietomurtoilmoituksista | Suomessa lähes 0 maksettu | Oikeusprosessi | Toimeksianto | Ei | - | **Hylätty.** Ei rahaa Suomessa |
| 16 | Sähkön ja viestintäpalvelun vakiokorvaus keskeytyksistä | Sopimus | Kyllä | Maksetaan lain mukaan automaattisesti | - | - | - | - | **Hylätty.** Ei jää lunastamatta |
| 17 | Vuokravakuuden palautus, laittomat korotukset | Vuokrasopimus | Kyllä | `tuntematon` | Riita | Toimeksianto | Ei | Yksittäinen | Heikko |
| 18 | Dieselgate-tyyppiset joukkokorvaukset | Auton omistus | Kyllä, rekisteristä | `tuntematon` | Oikeusprosessi | Asianajo | Ei | Yksittäinen | Heikko, juristit |
| 19 | Vakuutuskorvaukset hakematta (matka, henki) | Vakuutus + tapahtuma | Osittain | `tuntematon` | Tietämättömyys | Arkaluonteista | Osittain | Generaattori | Tuntematon, tutkittava |
| 20 | EU- ja kansalliset yritystuet hakematta | Y-tunnus + toimiala | Kyllä, tukiehdoista | `tuntematon` | Byrokratia | Y-tunnus, valtuutus | Osittain | Generaattori: joka tuki | Keskiheikko, hidasta |

## Mitä niukkuuslinssi paljasti

**Oikeus syntyy aina jostakin, mitä tekoälyllä ei ole.** Neljä lähdettä:

1. **Transaktion todiste**: lippu, lasku, kuitti (2, 3, 4, 5, 11, 12). Tekoäly voi lukea sen, mutta
   ei omistaa.
2. **Pääoman omistus**: osakkeet (1). Oikeus on pääoman sivutuote, ja pääomaa meillä ei ole.
   Mutta sen omistajilla ei ole aikaa. Se on aukko.
3. **Asema**: kelpoisuus, työsuhde, tekijyys, sopimusehto (6, 7, 8, 9, 14).
4. **Vahinko**: potilas, tietomurto (10, 15). Arkaluonteista, juristien aluetta.

**Jokaisessa tapauksessa oikeus toimia vaatii valtakirjan.** Tekoäly voi löytää oikeuden,
mutta vain haltija tai hänen valtuuttamansa voi lunastaa. Meille niukka resurssi ei siis
ole oikeus vaan **valtakirja ja luottamus, jolla se saadaan**. Se on kasautuva: yksi
onnistunut lunastus tuottaa seuraavan valtakirjan halvemmalla.

**Lupakysymys on sama kaikissa:** kun asiakas saa rahan itse ja maksaa menestyspalkkion,
kyse ei todennäköisesti ole perinnästä (AVI:n kanta AirHelpista). Kun raha kulkee meidän
kauttamme, se on perintää ja vaatii luvan. Rakenne ratkaisee. Ohjelmisto, jota asiakas
käyttää itse, ei vaadi mitään.

**Eettinen raja on selvä:** menestyspalkkio on oikein, kun maksaja on yhtiö tai valtio ja
asiakas on varakas tai yritys (1, 3, 4, 5). Se on väärin, kun asiakas on köyhä (6, 7).
Nämä tehdään ilmaiseksi tai julkisella rahalla, tai ei ollenkaan.

## Tuomio

Kolme kestää jatkotutkimuksen: **lähdeveron palautus** (suurin, generaattori, yksityis-
sijoittajat alipalveltuja, lupa selvä valtakirjalla), **B2B-viivästyskorvaus ohjelmistona**
(ei lupaa, integraatio kirjanpitoon, generaattori) ja **verovähennysradar** (generaattori,
mutta lähellä olemassa olevia). Kahdeksan hylätään heti. Loput ovat pieniä tai jonkun
muun aluetta.

Yksikään ei ole "1 000 € → 2 000 € 90 päivässä" -mekanismi. Ne ovat tuotteita, joiden
ensimmäinen euro on kuukausien päässä. Niiden arvo on siinä, että ne kasaavat valtakirjoja
ja dataa, ei ensimmäisessä palkkiossa.
