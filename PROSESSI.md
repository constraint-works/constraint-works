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

Uusi löydös ajetaan ensin 10M-rakennetestin läpi (`etsinta/SUUREN-VIPUVAIKUTUKSEN-TEORIA.md`
§6): BASELINE → CAPTURE → HUMAN → SCARCITY → STATE → FEEDBACK → VALUE → CAPITAL → CEILING →
FALSIFIER → EV. Yksi tappo riittää hylkäykseen. Kolme UNKNOWNia peräkkäin tarkoittaa, että
mitataan ennen arviointia. Vain läpäissyt löydös saa kortin ja pisteet. Baseline on aina
asiakkaan halvin hänen omilla rajoitteillaan hyväksyttävä vaihtoehto, ei tekemättä
jättäminen. (Lisätty 2026-09-16, perustelu teoriassa ja GPT:n ristiinarviossa.)

## Pisteytys (1 - 5 jokaiseen)

| Kriteeri | Kysymys |
|---|---|
| `aika_ekaan_euroon` | Kuinka nopeasti tulee ensimmäinen euro. 5 = alle viikko. |
| `tuplaus` | Todennäköisyys, että 1 000 € → 2 000 € tätä kautta 90 päivässä. |
| `skaala` | Voiko tämä realistisesti olla osa 10 M€ polkua. 5 = kyllä yksin. |
| `ai_etu` | Kuinka paljon tekoäly muuttaa peliä. 5 = mahdotonta ilman. |
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
