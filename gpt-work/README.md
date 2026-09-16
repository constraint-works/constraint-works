# GPT Work: ensimmäinen ristiinarvio

2026-09-15. Erillinen GPT-haara. Clauden tutkimuksia ei ole muokattu.

## Jatko 16.9.2026

[JATKO-C.md](JATKO-C.md) vastaa Clauden vastaristiinarvioon ja korjaa oman liian tiukan aineistopysäytyksen. Julkinen tekninen esikoe oli mahdollinen: 12 ennalta valitusta PyPI-kohteesta 10 rakentui ilman korjausta ja kaksi jäi versionvalinnan ulkopuolelle. Tunnettu html5lib-kontrolli epäonnistui lähderakennuksessa. Tämä ei mittaa AI:n varannon hyötyä eikä asiakkaiden maksuhalukkuutta. Mukana ovat protokolla, ajettava skripti ja raakadata. Raportti haastaa myös kääntäjän tutkintoportin, Peppol-testivarannon ja yhteisostojen ansaintalogiikkaa.

## Lukujärjestys

1. [RISTIINARVIO.md](RISTIINARVIO.md): Claude vastaan GPT, pääväitteen falsifiointi, lähde- ja laskukorjaukset.
2. [YO-WORK-B.md](YO-WORK-B.md): orpojen kohteiden kymmenen osuman koe ja Work A:n kolmen haaran porttipäätökset.
3. [UUDET-MEKANISMIT.md](UUDET-MEKANISMIT.md): primitivit, kolme avointa mekanismia, generaattorin kentät ja 0 €:n seuraava koe.
4. [WORK-A.md](WORK-A.md): alkuperäinen riippumaton raportti muuttamattomana.

## Mitä saatiin aikaan

- Luettu yhteinen repo snapshotista `296e5b3f65d2a5ede9d423a5c81c984ec97e0a1d`, myös 25 mahdollisuuskorttia ja työkalut.
- Tarkastettu olennaisia väitteitä julkisista ensisijaisista lähteistä. Toimittajien tulosväitteet merkitty itse ilmoitetuiksi.
- Mitattu yhden orpojen tuotteiden hakuproxyn laatu: kymmenen luettua osumaa, kaksi ei-tuotetta, kaksi dokumentoitua vaihtoehtoista selitystä hiljaisuudelle ja kuusi tuntematonta. Ei populaatioestimaattia.
- Erotettu tulo, asiakkaan säästö, oikeus, toistuva kassavirta ja kasautuva etu.
- Avattu kolme uutta mekanismia. Yhtään kaupallisesti validoitua mahdollisuutta ei vielä vahvistettu.

**Pääjohtopäätös, INFERENCE:** niukkuuden omistus on liian lavea selitys rahavirralle. Olennaista on pääsy hyväksyttyyn suoritukseen, neuvoteltu korvaus ja säilyvä tila joka parantaa seuraavaa tapausta. Uusi todennettu tieto voi syntyä työn tuloksena eikä vain omaisuuskaupalla. Tämäkään kehys ei todista meille etua.

**Ensimmäisen kierroksen koe-ehdotus (aineistopysäytys korjattu yllä olevassa jatkossa):** sama AI uuden tapauksen ratkaisemiseen aiemmista tapauksista kertyneen testivarannon kanssa ja ilman sitä. Protokolla, falsifiointirajat ja aineistovaatimukset ovat uusissa mekanismeissa. Ostajan hyväksymä luvallinen aineisto puuttuu. Ulkopuoliseen yhteydenottoon tarvitaan omistajan hyväksyntä käyttäjän ohjeen mukaisesti.

## Aineisto ja toistaminen

- [Orpojen kohteiden proxy-otos](data/orphan-proxy-audit.json): haku, järjestys, lähdepolut, README-blobien SHA:t ja luokittelu. Hakutulokset voivat muuttua.
- [Mekanismikortit](data/mechanism-cards.json): kaikki kaupalliset portit näkyvästi UNKNOWN. Nämä eivät ole asiakasliidejä.
- [check_evidence.py](check_evidence.py): paikallinen aineistotarkistus ja laskelmat. Ei verkkoyhteyttä tai ulkoisia toimia.

Ajo: `python3 gpt-work/check_evidence.py`.

Alkuperäisen Work A:n SHA-256: `38bc3240efe8ae6b3e9a82ae8c5a30cbe67a767543094e6a5cdbffe3884c7f7a` (49 657 tavua). Sen sisältöä ei normalisoitu tässä vuorossa.

## Rajat

Käteiskulu 0 €. Ei ulkopuolisia yhteydenottoja, sopimuksia, hankintoja, sitovia rekisteröitymisiä tai tuotantojärjestelmien muutoksia. Julkisten lähteiden perusteella ei laskettu keksittyjä onnistumistodennäköisyyksiä tai 10 miljoonan arvostusta. Kaikissa uusissa mekanismeissa pääsy, maksuhalukkuus tai uudelleenkäytettävä etu on vielä osoittamatta.

Tämä on valittujen haarojen aineisto- ja lupaportti, ei julistus että uusia julkisesti tutkittavia kysymyksiä ei olisi olemassa.
