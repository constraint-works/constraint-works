# Etsintäkierros 2: ei bountyja, ei hackathoneja, ei kilpailuja

Kysymys: missä raha liikkuu ilman, että kukaan yrittää palkata meitä tekemään ennalta
määriteltyä tehtävää?

## Miten ajattelin

Kierroksen 1 kortit olivat kaikki samaa mekanismia: joku on kirjoittanut "tee X, saat Y".
Se on helpoin löytää ja siksi kilpailluin. Kierroksella 2 kävin läpi rahavirtoja
järjestelmän tasolla ja kysyin jokaisesta: onko tässä kohta, jossa raha jää liikkumatta
kitkan, väsymyksen tai lukemisen määrän takia?

Rahavirrat, jotka kävin läpi, ja mihin ne johtivat:

| Virta | Mihin johti | Kortti |
|---|---|---|
| Lakisääteiset velvoitteet, joita ei lunasteta | kitka estää, kone poistaa kitkan | `oikeudet-lunastamatta` (generaattori) |
| Julkinen kulutus | pienhankinnoissa 0 - 3 tarjoajaa | `julkiset-pienhankinnat` |
| Protokollakannustimet | vahtitehtävät pienillä ketjuilla | `protokolla-vahtitehtavat` |
| Agenteille tarkoitettu raha | uusi kategoria, kilpailu vasta alkamassa | `agenttinatiivit-taloudet` |
| Agenttien oma kulutus | x402, agentit ostavat palveluita | `x402-palvelut` |
| Delegoitu pääoma | ainoa iso vipu, mutta luvanvaraista | `delegoitu-paaoma` (hylätty) |
| Hintaerot tavaramarkkinoilla | jo kortti kierrokselta 1 | `hinta-arbitraasi-kaytetyt` |
| Informaatioepäsymmetria arvopapereissa | lisensoitua tai jo botitettua | ei korttia |
| Käyttämättömät resurssit (laskenta, tila) | tuotto pientä, ei älyä | ei korttia |
| Rahan luonti (luotto, tokenit) | vaatii pankin tai ostajia | ei korttia |

## Mitä opin kierroksella

**Suurin vipu on aina toisten rahassa, ja se on aina säänneltyä.** Delegoitu pääoma on
ainoa mekanismi, jossa 1 000 € voi liikuttaa miljoonaa. Sääntely on siinä juuri siksi.
Projekti ei mene sinne ilman selvää lupaa.

**Kitka on parempi este kuin osaaminen.** Kilpailuissa este on osaaminen, ja tekoäly
tasaa sen kaikille. Lunastamattomissa oikeuksissa este on kitka, ja kitkan poistaminen
skaalautuu. Se on generaattori, koska oikeuksia on satoja.

**Agenttinatiivi raha on ainoa, jossa kilpailijat eivät ole ihmisiä.** Muualla
kilpailemme ihmisten kanssa, joilla on samat mallit. Agenttitalouksissa kilpailemme
agenttien kanssa, ja niitä on vielä vähän.

## Generaattorit

Yksittäisen mahdollisuuden sijaan kolme konetta, jotka tuottavat mahdollisuuksia:

1. **Oikeuskone.** Käy läpi lainsäädäntöä ja sopimusehtoja ja etsii korvausvelvoitteita,
   joiden lunastusaste on matala. Jokainen löytö on oma mahdollisuutensa.
2. **Uutuuskone.** Seuraa uusia alustoja, rajapintoja ja kannustinohjelmia (agentti-API:t,
   uudet ketjut, uudet protokollat) ja hälyttää, kun jokin on alle 90 päivää vanha.
   Uusi tarkoittaa kilpailematonta.
3. **Kitkakone.** Etsii prosesseja, joissa raha jää liikkumatta, koska lomake on liian
   pitkä, määräaika liian lyhyt tai yksittäinen summa liian pieni. Sama periaate kuin
   oikeuskone, mutta yksityisissä sopimuksissa.

Nämä kolme ovat tämän kierroksen tärkein tuotos. Ne eivät ole vielä koodia.
