# Compounding: mikä niukka resurssi kasvaa jokaisesta kierroksesta

Kysymys jokaiselle mekanismille: kasvaako jokin niukka resurssi jokaisen onnistuneen
kierroksen seurauksena? Jos ei, kyse on työstä, ei silmukasta.

## Mitä orpojen omaisuuksien data sanoo silmukoista

Lähtöhypoteesin silmukka oli:
orpo omaisuus → käyttäjät → kassavirta → lisää omaisuutta → suurempi käyttäjäkunta.

Data (`ORVOT-OMAISUUDET.md`) rikkoo sen kahdesta kohdasta:

1. **Käyttäjät → kassavirta ei toimi.** npm-lataajat ovat koneita. Laajennusten ja
   lisäosien käyttäjät saivat tuotteen ilmaiseksi, ja hylätyn tuotteen muuttaminen
   maksulliseksi on juuri se, mikä ajaa heidät haarautumaan (WordPress: käyttäjät
   siirtyivät `limit-login-attempts-reloaded`-forkkiin, eivät maksaneet alkuperäisestä).
   Ainoat mitatut rahavirrat orpoihin ovat mainosraha (Pixalate: 53 M USD/nelj., 160 k
   sovellusta, pääosin roskaa) ja yritysten compliance-tuki (HeroDevs).
2. **Omaisuus → omaisuus ei kasaudu, koska niukka resurssi ei ole omaisuus.** 80 issuen
   otos: omistajat antavat pois ilmaiseksi. Hankinta ei ole pullonkaula. Pullonkaula on
   omistajan luottamus (pääsy annettiin alle puolessa tapauksista, vaikka vapaaehtoisia
   oli mediaanina kuusi) ja julkaisuoikeus (html5lib: 20 mergeable-PR:ää, 0 julkaisua).

## Silmukka, joka datassa oikeasti näkyy

Kaikki kolme onnistujaa aineistossa toimivat samalla silmukalla:

- **HeroDevs**: maksaa alkuperäisille ylläpitäjille → saa "virallisen jatkajan" aseman →
  yritykset maksavat tuesta → 1 000+ asiakasta → 125 M USD → lisää projekteja.
- **WPChef** (`limit-login-attempts-reloaded`): forkkasi hylätyn lisäosan 2016 → piti
  sen päivitettynä → hakemisto ohjasi käyttäjät → 1 M+ asennusta → maksullinen pilvitaso.
- **Suljettujen issueiden ulkopuoliset ylläpitäjät** (13/31): yritys tai tunnettu hahmo
  tai PR:t ensin → pääsy → aktiivinen repo (11/13 vuoden päästä).

Silmukka on:

**todennettu jatkajuus → seuraava luovutus halvemmalla → enemmän jatkajuuksia → vahvempi
todennettu historia.**

Kasautuva resurssi on **julkinen todiste siitä, että olet jatkanut jotakin hyvin**. Se on
sama resurssi, jonka niukkuuskartta nimesi (todennettu historia, 10/10). Se ei ole
ostettavissa ja se on hidas. Mutta se kasvaa jokaisesta kierroksesta, ja se laskee
seuraavan kierroksen hintaa. Se on aito silmukka.

Tekoälyn rooli silmukassa ei ole "ylläpito ilmaiseksi" vaan **yksi ihminen voi olla
uskottava jatkaja useammalle asialle kuin ennen.** html5lib-koe mittasi sen: tekoäly
tekee koodin (47 % issueista yksin), ihminen tarvitaan 1 - 3 h/kk per projekti
merge-, julkaisu-, tietoturva- ja suunnittelupäätöksiin. Jos se pitää paikkansa
laajemmin, yksi ihminen voi olla vastuullinen ylläpitäjä 20 - 50 projektille, ei 1 - 3:lle.

**Mittari:** vastuullisia jatkajuuksia per ihminen, ja niiden julkinen todennettavuus.
Ei euroja, ei käyttäjiä.

## Missä sama silmukka toimii ilman omistajanvaihdosta

Omistajanvaihdos on silmukan kallein vaihe (luottamus, xz-profiili, käyttäjien
epäluulo, spämmätty "otan ylläpidon" -tarjous). Kolme tapaa kiertää se:

1. **Fork hakemistossa** (WordPress, npm-nimivaihtoehdot): ei tarvitse omistajaa, hakemisto
   jakaa käyttäjät sille, joka päivittää. Kilpailtu mutta todistettu.
2. **Pakotettu migraatio omistajan lukuun** (`mahdollisuudet/pakotetut-alustamigraatiot.md`):
   omistaja pitää omaisuuden ja maksaa työstä. Ei luottamusongelmaa, koska oikeudet
   eivät liiku. Tekoäly tekee työn, omistaja painaa julkaisunappia.
3. **Jatkaja-palvelu omistajan siunauksella** (HeroDevs-malli pienessä koossa): omistaja
   nimeää julkisesti jatkajan, jatkaja julkaisee allekirjoitettuna, loki on julkinen.

Kaikissa kolmessa kasautuu sama resurssi: todennettu jatkajuus.

## Muut projektin silmukat datan valossa

- **Valtakirjasilmukka (A)**: sama rakenne. Ensimmäinen valtakirja kallein, todennettu
  tulos halventaa seuraavan. Vahvistuu.
- **Yleisösilmukka (C)**: tämä repo on jo esimerkki. Yön luvut (23 % laajennuksista
  poistettu 20 kk:ssa, 1/80 omistajaa pyysi rahaa, html5lib:n 20 PR:ää) ovat lukuja,
  joita ei ole missään muualla. Julkaisu tuottaa yleisöä, yleisö tuottaa luottamusta,
  luottamus tuottaa luovutuksia.
- **Datasilmukka (D)**: orpojen skannerit (`hae_orvot_*.py`) ovat generaattori, joka
  paranee joka ajolla, kun tiedetään, mikä ennusti luovutuksen onnistumista.

## Mikä tappaisi tämän

- Jos alkuperäiset omistajat alkavat itse käyttää agentteja ylläpitoon, luovutuksia ei
  tule. Data ei tue: syyt hylkäämiseen olivat elämä (ei aikaa, siirtynyt muualle,
  kuolema), ei kustannus. Agentti ei palauta kiinnostusta.
- Jos alustat alkavat estää omistajanvaihdokset turvallisuussyistä. Mahdollista
  laajennuksissa (Google verifioi jo). Ei todennäköistä avoimessa koodissa.
- Jos "todennettu jatkajuus" ei ole siirrettävissä projektista toiseen (jokainen
  yhteisö vaatii oman historiansa). Osittain totta: WordPress-maine ei auta PyPI:ssä.
  Silmukka on ekosysteemikohtainen, mikä hidastaa sitä mutta ei tapa.
