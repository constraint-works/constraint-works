# Prosessi

Tämä on mahdollisuuksien etsintäkone, ei sijoitussuunnitelma. Kone etsii mekanismeja,
joissa tekoäly antaa poikkeuksellisen vivun, testaa ne pienellä rahalla ja siirtää
resurssit sinne, missä etu on todellinen.

## Ehdoton periaate

Kaikki laillista ja eettisesti puolustettavaa. Ei varastamista, huijaamista,
manipulointia eikä haavoittuvuuden hyödyntämistä ilman lupaa. Bountyissa toimitaan
ohjelman sääntöjen sisällä ja raportoidaan vastuullisesti. Jos mekanismi vaatii
selittelyä, se hylätään.

## Neljä kysymystä

Jokainen mahdollisuus vastaa näihin ennen kuin siihen käytetään euroakaan tai tuntiakaan:

1. **Kuka maksaa?** Konkreettinen taho, ei "markkina".
2. **Miksi maksaa?** Mikä on maksajan oma hyöty. Jos ei ole, raha ei ole kestävää.
3. **Mikä estää muita ottamasta sitä?** Jos ei mikään, se on jo otettu.
4. **Mikä on meidän etumme?** Se osa asiakkaan hyväksyttävyysehdoista, jonka täytämme
   ja jota asiakkaan oma tai kilpailijan tekoäly ei täytä. Edun pitää nojata johonkin,
   jonka baseline ei laske mallien parantuessa: laki, vastuu, oikeus, pääsy, yleisö.
   (Muutettu 2026-09-16: alkuperäinen "tekoälyn pitää tehdä jotain ihmiselle mahdotonta"
   kumoutui evidenssillä, ks. `etsinta/SUUREN-VIPUVAIKUTUKSEN-TEORIA.md` §9.2.)

## Elinkaari

```
hypoteesi → tutkittu → koe → aktiivinen → skaalataan
                ↘ hylätty (syy kirjataan, ei avata uudelleen ilman uutta tietoa)
```

- **hypoteesi**: idea ja neljä kysymystä luonnoksena
- **tutkittu**: kysymyksiin vastattu datalla, pisteytetty, toinen malli haastanut
- **koe**: kokeet/-kansiossa on suunnitelma, budjetti ja onnistumisen ehto
- **aktiivinen**: koe onnistui, mekanismi tuottaa
- **hylätty**: syy kirjattu korttiin

## Rakennetesti ennen pisteytystä

Uusi löydös ajetaan ensin **pöytätestin** läpi (Structural Test v2.2,
`etsinta/KEHIKON-TUHOAMISYRITYS-V3.md` §7): (P1) liikkuuko raha jo, kuka sen saa nyt ja
miksi; (P2) onko oikeus, pääsy ja laillisuus hankittavissa ja mihin hintaan; (P3) onko
kantaja artefakti ja onko luokassa toistuvuutta. Kaikki kolme vaaditaan jatkoon. Vasta
mittauksen jälkeen täytetään mittauslomake (kohortti 2 -nettotalous). Vain sen läpäissyt
löydös saa kortin ja pisteet. Baseline on maksajan halvin hänen rajoitteillaan
hyväksyttävä vaihtoehto määritellyn lopputuloksen hankinnassa; muualla hyötyero on
osoitettava maksajan mittarilla. (Lisätty 2026-09-16, muutettu samana päivänä kolmannen
ristiinarviokierroksen jälkeen; aiemmat versiot teoriassa ja GPT:n V2:ssa.)

## Pisteytys (1 - 5 jokaiseen)

| Kriteeri | Kysymys |
|---|---|
| `aika_ekaan_euroon` | Kuinka nopeasti tulee ensimmäinen euro. 5 = alle viikko. |
| `tuplaus` | Todennäköisyys, että 1 000 € → 2 000 € tätä kautta 90 päivässä. |
| `skaala` | Voiko tämä realistisesti olla osa 10 M€ polkua. 5 = kyllä yksin. |
| `ai_etu` | Kuinka suuri osa hyväksytystä tuloksesta katoaa, jos mallit poistetaan samalla ihmisellä ja rahalla. 5 = välitulos ei synny ilman. (Korjattu 2026-09-16 ristiriidan takia, ks. `etsinta/VASTAHYOKKAYS-V2.md`.) |
| `paaoma` | Kuinka vähän pääomaa sitoo. 5 = nolla. |
| `laillisuus` | 5 = täysin selvä. 3 = tarkistettava. 1 = hylkää. |

Kokonaispisteet = summa. Laillisuus alle 3 hylkää automaattisesti.

## Kaksi mallia, yksi loki

Claude ja GPT työskentelevät samasta repostasta. Kummankin tuotos menee samaan
rekisteriin. Kun toinen kirjoittaa kortin, toinen haastaa sen:

- Haaste kirjoitetaan kortin `## Haaste`-osioon: mikä oletus on heikoin, mikä data
  puuttuu, mikä on todennäköisin syy epäonnistua.
- Kortin kirjoittaja vastaa `## Vastaus haasteeseen`-osioon.
- Jos erimielisyys jää, se ratkaistaan kokeella, ei väittelyllä.
- Kumpikaan ei muokkaa toisen tekstiä. Lisätään, ei poisteta.

## Kokeen säännöt

- Jokaisella kokeella on budjetti euroina ja tunteina, onnistumisen ehto ja päättymispäivä.
- Ehto kirjataan ennen aloitusta. Sitä ei muuteta kesken.
- Tulos kirjataan sellaisenaan. Epäonnistunut koe on yhtä arvokas kuin onnistunut.
- Ihminen painaa aina nappia. Malli ei tee kauppoja eikä siirrä rahaa.

## Ensimmäinen todellinen testi

1 000 € → 2 000 € tavalla, jota emme olisi löytäneet tai pystyneet toteuttamaan ilman
tekoälyä. Vasta sen jälkeen kysytään, onko mekanismi toistettava ja skaalattava.

## Jatkuva etsintä

`etsinta/`-kansiossa on generaattori, joka tuottaa uusia hypoteeseja säännöllisesti,
ja lähdelista, jota skannataan. Hylätyt ideat pysyvät rekisterissä, jotta samaa
ei tutkita kahdesti.
