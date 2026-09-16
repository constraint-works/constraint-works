# Kehikon tuhoamisyritys: commit f5d26a7 (Structural Test v2.1, kolmen parin pilotti, 14 tapauksen väite)

2026-09-16, Claude. Viimeinen teoriakierros ennen mittaamista. Kohde on oma edellinen
commitini. Sääntö: en puolusta sitä. Merkinnät FACT / CALC / INFERENCE / HYPOTHESIS / UNKNOWN.

Havainto heti alkuun (FACT): commit `f5d26a7` jätti PROSESSI.md:n viittaamaan vanhaan
11-kohtaiseen testiin, vaikka päätösloki sanoo, että v2.1 korvaa sen. Prosessi ja loki
ovat ristiriidassa toisen kerran samana päivänä. Korjataan tässä commitissa siihen
muotoon, joka tämän hyökkäyksen jälkeen jää voimaan.

## 1. Structural Test v2.1 kysymys kerrallaan

### Q1 VALINTA

**Mitä mittaa:** havaitun ostopäätöksen ja nimetyn vaihtoehdon kokonaiskustannuksen.
**Mitä olettaa:** että maksaja on nimettävissä ennen tarjousta, että vaihtoehto on
havaittavissa ja että valinta voidaan havaita. Valinnan havaitseminen vaatii tarjouksen,
ja tarjous vaatii tässä projektissa lähes aina omistajan luvan yhteydenottoon.

**Hylkäysehto liian vahva:** "maksaja ei valitse" tappaa yhdellä kieltävällä
vastauksella (n = 1). Yksi väärä maksaja tai väärä hinta riittää tappoon.

**UNKNOWN liian helppo:** "valintaa ei ole vielä havaittu" pätee jokaiseen
käynnistämättömään mekanismiin. **Q1:llä ei ole erottelukykyä ennen käynnistystä.** Se
on käynnistyksen jälkeinen mittari, joka on puettu esikarsinnaksi.

**Väärä positiivinen:** valinta havaittu innokkaassa kohortissa. Se on Q3:n tehtävä, joten
Q1 ei ole riippumaton.
**Väärä negatiivinen:** maksaja ≠ valitsija (julkinen hankinta, vakuutus, B2B2C).
"Maksaja ei valitse" on rakenteellisesti totta ja silti mekanismi voi toimia.
**Riippumattomuus:** ei. Q1 on Q3:n ensimmäinen kohortti.
**Hintakatto-oletusarvo** on normatiivinen sääntö, ei testi. Se ei kuulu taulukkoon.

### Q2 OSUUS

**Mitä mittaa:** onko laillinen reitti meille jäävään arvoon olemassa tai optiona.
**Mitä olettaa:** että oikeudet ovat binäärisiä (saa / ei saa). Todellisuudessa oikeus on
lähes aina saatavissa jollain hinnalla, joten "oikeutta ei voi saada" on harvoin FACT ja
useimmiten "ei ole vielä kysytty" → UNKNOWN.

**Hylkäysehto liian vahva:** "raja umpeutui" on itse asetettu raja. Mekanismi pidetään
hengissä asettamalla antelias raja. Ei ulkoista ankkuria.
**UNKNOWN liian helppo:** "optio voimassa, pilotti ajamatta" on pysyvä tila, ellei
kukaan pakota pilottia. Kukaan ei pakota.
**Väärä positiivinen:** GPT:n huomautus pätee yhä: "sopimus" kattaa kaiken laillisen
ansainnan, joten lineaarinen palvelu läpäisee Q2:n. Se on hyväksyttävää (Q2 ei mittaa
skaalaa), mutta silloin Q2 on lähes sama kuin "maksaja nimetty" eli Q1.
**Väärä negatiivinen:** kaappaus työsuhteen tai yritysoston kautta (tila johtaa
palkkaukseen tai ostoon) ei ole "oikeus, sopimus tai omistus" ennakolta nimettävässä
muodossa. Pieni luokka, mutta olemassa.
**Riippumattomuus:** optiopilotti on Q6:n mittaus; osuus on Q3:n talouden rivi.

### Q3 KOHORTTI 2

**Mitä mittaa:** koko nettotalouden seuraavassa kohortissa. Tämä on oikeasti *koko testi*:
Q1 (valinta kohortissa 2), Q4 (ylläpidon kulmakerroin) ja Q5:n kestävyysosa (kilpailijan
AI kohortissa 2) ovat sen rivejä. Muut kysymykset ovat Q3:n osajoukkoja tai edellytyksiä.

**Eri kanava sekoittaa kaksi asiaa.** Kyllä. Mekanismi, jonka luonnollinen jakelu on yksi
kanava (hakemisto, yksi yhteisö), näyttää huonolta kohortissa 2 vain siksi, että se
pakotettiin kanavaan, jossa se ei toimi. Vaatimus mittasi kanavan vaihdon kustannusta,
ei skaalautuvuutta. Rakennettu esimerkki: lisäosa, jonka käyttäjät tulevat hakemistosta
0 €:n hankintakululla; kohortti 2 "eri kanavasta" (mainonta) maksaa 40 €/asiakas ja
talous kääntyy negatiiviseksi. Mekanismi on hyvä, testi tappaa. **Korjaus:** kohortti 2 =
sama kanava, myöhempi aika, ei meidän valitsemamme (seuraavat N järjestyksessä tai
satunnaisotos kanavan sisältä). Eri kanava on *diagnostiikka* kanavariippuvuudelle, ei
tappo.

**Bundlaus-hylkäysehto:** "bundlaus halvempi kuin meidän hinta" tappaa jokaisen
ohjelmistopalvelun, koska jollakin isolla on aina tekninen kyky. Tekninen kyky ei ole
strateginen käyttäytyminen. Hylkäykseen pitäisi osoittaa (a) kannustin (bundlaajan
liikevaihto, jota meidän tuotteemme uhkaa tai täydentää), (b) vierekkäisyys (ominaisuus
sopii bundlaajan tuotteeseen), (c) perustaso (onko bundlaaja tehnyt näin ennen). Ja
silloinkin oikea käsittely on **lyhyempi odotettu elinaika Q3:n taloudessa**, ei tappo.
Katkeaa tappona, siirtyy riskitekijäksi.

**"Yhteinen häntä pysäyttää kaiken":** jokaisella mekanismilla on yhteinen riippuvuus
(laki, alusta, mallintarjoaja). Tappo on liian vahva; oikea muoto on todennäköisyys ×
tappio horisontilla. Katkeaa tappona.

**"Kohortti 2 negatiivinen" vs. GPT:n E5:** GPT sanoi oikein, että etupainotteinen
investointi voi olla osa kannattavaa polkua. Q3:n tappo on ristiriidassa sen kanssa,
jonka hyväksyin edellisessä commitissa. Katkeaa: negatiivinen kohortti 2 tappaa vain,
jos se ylittää ennalta asetetun oppimisbudjetin.

**UNKNOWN liian helppo:** "kohorttia 2 ei ole" pätee kaikkeen ennen käynnistystä.
**Väärä positiivinen:** kohortti 2 positiivinen, kohortti 3 romahtaa (kahden pisteen
ekstrapolaatio). **Väärä negatiivinen:** ks. eri kanava ja oppimisbudjetti.
**Riippumattomuus:** Q3 *on* testi; muut ovat sen rivejä. Se on rakenteellinen löydös,
ei vika: kuuden kysymyksen lista on yksi kysymys ja viisi osoitinta siihen.

### Q4 TILA

**Mitä mittaa:** nimetyn artefaktin kausaalisen vaikutuksen A/B-asetelmassa.
**Mitä olettaa:** että S on artefakti, joka voidaan poistaa. Yleisö-, sopimus- ja
luottamustyyppistä tilaa ei voi poistaa vastafaktuaalissa. **Q4 rajaa teorian
hiljaisesti artefakti-S:ään.** Se on merkittävä kaventuminen, jota ei sanottu ääneen:
kolme neljästä §2:n "oikeasti kasautuvasta" tilasta (jakelu, maine yleisönä,
eksklusiivinen oikeus) jää Q4:n ulkopuolelle pysyvään UNKNOWNiin.

**"S:n käyttö ei kasva volyymin mukana" on uusi P2 ja se katkeaa.** Rakennettu
vastaesimerkki: S on hyväksyttyjen korjausten kirjasto; jokainen uusi tapaus vaatii
ihmisen 5 min konsultaation (käyttö kasvaa lineaarisesti volyymin mukana) ja säästää
60 min. Nettotalous paranee joka tapauksessa; ehto tappaisi sen kirjaimellisesti.
Tarkoitettu sisältö ("S:ää ei tarvitse rakentaa uudelleen per yksikkö") on tilan
määritelmä, ei lisäehto. Poistetaan; jäljelle jää nettovaikutus.

**"Takaisinmaksutoistot ≤ todennettu jäljellä oleva kysyntä"** tappaa väärin kolmessa
tilanteessa: (a) kysyntä kasvaa (todennettu = tilannekuva), (b) kysyntää voi hankkia
(hankintakulu kuuluu Q3:een, ei tappoon), (c) sama S toimii viereisessä luokassa
(esim. sama pakkauskorjaus PyPI:ssä ja conda-forgessa). Ja se laskee kysynnän kahdesti
(Q3 ja Q4). **Korjaus:** tappo vain, jos takaisinmaksu ylittää koko luokan kysynnän
(TAM-katto) *ja* viereistä luokkaa ei ole nimetty; muuten UNKNOWN, joka ratkaistaan Q3:ssa.

**Vastafaktuaali on aikasidonnainen:** "sama tekoäly ilman S:ää" pätee vain samalla
malliversiolla. Seuraava malliversio voi sisältää S:n (koulutusdata) tai tehdä sen
tarpeettomaksi. Q4:n tulos vanhenee malliversion mukana. Ei tappo, mutta kirjattava.

**Väärä positiivinen:** S auttaa harjoitusjoukon kaltaisissa tapauksissa, jotka on
valittu samasta projektista (vuoto). **Väärä negatiivinen:** S:n hyöty näkyy vasta
tapauksessa 10+ (rakennuskulun amortisointi), 12 tapausta ei näytä sitä.
**Riippumattomuus:** nettovaikutus on Q3:n rivi; takaisinmaksu on Q3:n rivi.

### Q5 VIPU

**But-for-ehto:** "välitulos, jota ei olisi saavutettu ilman malleja samalla ihmisellä ja
rahalla". Miten tämä tiedetään? Ainoa tapa on ajaa haara ilman malleja, eikä kukaan
aja sitä (omistaja ei käytä kolmea kuukautta ilman malleja). Siksi but-for on aina väite.
Kolme eri asiaa, jotka commit `f5d26a7` antoi sulautua:

| Taso | Mitä se on | Esimerkki projektista | Todistusarvo |
|---|---|---|---|
| Ennakkoon kirjattu hypoteesi | "Ennustamme, ettei tätä saa ilman malleja X tunnissa" | ei yhtään kirjattua | Estää hindsightin, ei todista mitään |
| Havaittu AI-vaikutus | Mitattu ero vertailukelpoisessa suoritteessa | html5lib: 9 min, 82 k tokenia | Todistaa nopeuden, ei välttämättömyyttä |
| Todellinen but-for | Vastafaktuaali ilman malleja | **ei yhtään**; ja html5lib on vastaesimerkki: yhteisön ihmiset tekivät saman korjauksen kolmesti | Ei saatavilla |

html5lib on tärkeä: siinä but-for on **epätosi**. Sama tulos syntyi ilman malleja.
Mallit tekivät sen nopeammin. Q5:n ainoa mitattu tapaus kertoo, että "vipu" oli nopeus,
ei mahdollistaminen. But-for voidaan approksimoida vain kustannusargumentilla: "ilman
malleja tämä maksaisi markkinahinnalla Y € > budjetti" (CALC oletuksilla), ja se on
INFERENCE, jonka vahvuus riippuu siitä, onko Y markkinahinta (käännöstoimiston hinnasto)
vai mielipide.

**Onko Q5 portti lainkaan?** Ei. Se ei vaikuta siihen, kasvaako mekanismi. Se vaikuttaa
siihen, saako projekti kirjata tuloksen omakseen. Se on raportointisääntö, ja sen paikka
on tulosten kirjaamisessa, ei esikarsinnassa. Riippumattomuus: kestävyysosa on Q3:ssa.

### Q6 SEURAAVA HAVAINTO

**Mitä mittaa:** ei mekanismia vaan tutkimusprosessia. Meta-kysymys taulukossa, jonka
muut rivit ovat mekanismikysymyksiä.
**Hylkäysehto:** "määritelmää muutetaan tuloksen jälkeen" on havaittavissa vain, jos
ennakkorekisteröinti on olemassa. Projektissa on nyt yksi (GPT:n public-build-protocol).
**UNKNOWN on pakopaikka:** "ei mitattavissa nykyresursseilla: kirjataan sivuun, ei
tapeta" tarkoittaa, että jokainen kallis mekanismi pysäköidään ikuisesti. Lista kasvaa,
mikään ei kuole. Tämä on täsmälleen se vika, jonka takia pisteytys korvattiin.
**Portfolion tappiobudjetti:** viitataan, mutta sitä ei ole asetettu missään. Ilman
lukua ehto ei ole täytäntöönpantavissa. UNKNOWN, kunnes omistaja asettaa sen.

### Rakenteellinen johtopäätös v2.1:stä

Kolme kuudesta kysymyksestä (Q1, Q3, Q4) vaatii käynnistyksen jälkeistä dataa. Ennen
mittausta ne antavat aina UNKNOWN. Q5 on raportointisääntö, Q6 on prosessisääntö. Vain
Q2 on osittain pöydältä vastattavissa. **v2.1 ei ole esikarsintatesti vaan mittauksen
jälkeinen arviointilomake, joka on nimetty väärin.** Esikarsintaan tarvitaan halpoja
proxyja, jotka voidaan tarkistaa pöydältä. Ne ovat olemassa ja niitä on jo käytetty:
liikkuuko raha jo jollekulle (VALUE-proxy), kuka sen saa nyt ja miksi (baseline-proxy),
onko oikeus tai pääsy hankittavissa ja mihin hintaan (Q2), onko S artefakti, jonka
rakennuskulu on arvioitavissa (Q4-proxy). Ks. §7, v2.2.

## 2. Hyökkäys 14 tapauksen väitteeseen

Väite: "jokaisessa 14 tapauksessa tunnistettu este oli oikeus, luottamus tai pääsy, ei
koodi eikä 1 000 €."

Tarkistus tapaus kerrallaan alkuperäisistä muistioista, este sellaisena kuin se
kirjattiin *silloin*, ei nyt:

| # | Tapaus | Kirjattu este | Oikeus / luottamus / pääsy? | Todellinen luokka |
|---|---|---|---|---|
| 1 | Superteam | 116 - 122 agenttia per tehtävä, 0 avointa tehtävää | **ei** | kilpailu, kysyntä |
| 2 | Hackathonit | käteinen 0 - 7 %, kelpoisuusrajaukset, 3 % palauttaa | osittain (kelpoisuus = pääsy, venytetty) | kysyntä (potti ei ole rahaa), kilpailu |
| 3 | OSS-bountyt | lähde roskaantunut, Algora hiipunut | **ei** | kysyntä, kilpailu |
| 4 | Orpo ohjelmisto | käyttäjät eivät maksa; hakemisto omistaa käyttäjät; uhkaprofiili | osittain (luottamus) | **maksuhalukkuus**, jakelu, luottamus |
| 5 | html5lib | julkaisuoikeus | kyllä | oikeus |
| 6 | Microns | hinnat eivät ole halpoja | **ei** | markkinahinta |
| 7 | Laajennusostajat | omistajanvaihdos näyttää hyökkäykseltä | kyllä | luottamus |
| 8 | HeroDevs | siunaus ja sopimukset (heidän etunsa, ei meidän esteemme) | kyllä, mutta ei este vaan kilpailijan vallihauta | asema |
| 9 | Oikeudet, lähdevero | valtakirja; perintärajanveto | kyllä | luottamus, laki |
| 10 | Jälkitarkastus | pääsy dataan; virhetaso UNKNOWN; asiakkaan oma tekoäly | osittain | pääsy, **kysyntä**, kilpailu |
| 11 | Hankinnat | toimitus on omaa työtä; kumppani ohittaa | **ei** | työ, koordinointi |
| 12 | Reservit | integraation omistaja; vakuudet | osittain | asema, **pääoma** |
| 13 | Kääntäjä | kielitaito tutkintotasolla | **ei** (kyky, ei oikeus) | henkilökohtainen kyky |
| 14 | Agenttitalous | ei aitoa kysyntää, maine väärennettävissä | **ei** | kysyntä |

**FACT korjattuna:** oikeus, luottamus tai pääsy oli kirjattu este **5/14** tapauksessa
(5, 7, 9, 10-osin, 12-osin; 8 on kilpailijan etu). Kysyntä tai maksuhalukkuus oli este
vähintään **5/14** (1, 3, 4, 10, 14). Kilpailu 4/14. Työ tai kyky 2/14 (11, 13).
Pääoma 1/14 (12). Markkinahinta 1/14 (6). "14/14" oli väärin, ja se tuli venyttämällä
"pääsy" kattamaan kelpoisuuden ja "luottamus" kattamaan maksuhalukkuuden.

**Tautologiatarkistus:** kolmikko "oikeus, luottamus, pääsy" kattaa kaiken, mikä ei ole
rahaa, koodia tai kysyntää. Kun kysyntä ja kilpailu jätettiin pois luokittelusta, väite
muuttui muotoon "este ei ollut raha eikä koodi", joka on lähes tautologinen tässä
projektissa: rahaa ei ole vielä käytetty missään tapauksessa, joten se ei ole voinut
olla este; koodia ei ole yritetty myydä missään tapauksessa. **Mikä oikeasti kestää
FACT:ina:** 0/14 tapauksessa este oli 1 000 euron puute, ja 0/14 tapauksessa mallien
koodauskyky. Se on heikompi ja tosi.

**INFERENCE "seuraava löydös kaatuu todennäköisimmin OSUUS-kysymykseen": katkeaa.**
Korjatun luokittelun mukaan yleisin este oli kysyntä tai kilpailu, eli v2.1:n Q1/Q3.
Oikeus- ja luottamusesteet keskittyvät yhteen alaluokkaan: *haltuunotto* (4, 5, 7, 9).
Korjattu ennuste: seuraava löydös kaatuu todennäköisimmin siihen, ettei kukaan maksa
tai että maksaja on jo täynnä tarjoajia; oikeuteen se kaatuu, jos se on haltuunotto.
14 valikoitua tapausta antavat tämänkin vain heikosti: ne valittiin generaattoreilla,
jotka suosivat "raha on jo pöydällä" -tilanteita, joissa kilpailu on rakenteellisesti
todennäköisin este.

## 3. Kolmen parin pilotin tuhoaminen

**Säästö verrattuna mihin?** Commit `f5d26a7` ei sano. Ainoa luettavissa oleva tulkinta:
tapaus 1 rakentaa S:n, tapaukset 2 - 3 käyttävät sitä, ja "säästö" on tapausten 2 - 3
kustannus verrattuna tapaukseen 1. Se on ennen/jälkeen-vertailu, jonka baseline on n = 1.
"Kolme paria" oli väärä sana: ne ovat kolme peräkkäistä tapausta, ei paria.

**Mitä kustannuksen lasku voi tarkoittaa:** ihmisen oppiminen (ympäristö, testiajuri,
työkalut), tehtävien vaikeusero, mallin satunnaisvaihtelu, parempi promptaus, ympäristön
kertaluonteinen pystytys, ja S. Pilotti ei erota näitä. Kokeessa 02 mitattu 82 k tokenia
ja 9 min sisälsi vaiheet "kloonaa, venv, submoduuli, pinnaa setuptools", jotka ovat
ympäristön oppimista, eivät S:ää. Tapauksessa 2 ne olisivat poissa riippumatta S:stä.

**Tilanne A, S arvokas mutta pilotti näyttää nollaa:** tapaukset 2 ja 3 ovat sattumalta
vaikeampia (vaikeusvarianssi kokeen 02 kaltaisissa tehtävissä on suuri: 13 s vs.
tuntien selvitys), tai S:n hyöty ylittää rakennuskulun vasta tapauksessa 8, tai malli
osuu satunnaisesti pitkään harhapolkuun. Helppo rakentaa.

**Tilanne B, S arvoton mutta pilotti näyttää suurta säästöä:** tapaus 1 sisältää
kertaluonteisen ympäristöpystytyksen (kirjataan S:n rakennuskuluksi), operaattori oppii
testiajurin, tapaukset 2 - 3 ovat helpompia, promptit paranevat. Tulos: 60 %:n "säästö"
ilman että S:ää käytettiin lainkaan. Erittäin helppo rakentaa; se on itse asiassa
odotettu tulos.

**Johtopäätös:** pilotti ei ole päätöskelpoinen. Sen ainoa validi tuotos on kaksi lukua:
S:n rakennuskulu ja tapauksen suuruusluokkakustannus. Ne ovat hyödyllisiä takaisin-
maksulaskuun, mutta eivät kerro mitään S:n vaikutuksesta. Väite "jos säästöä ei näy edes
ilman kontrolleja, täysi koe on turha" on väärä molempiin suuntiin. Katkeaa.

**Mikä pilotista voidaan pelastaa:** vain jos se muutetaan paritetuksi: sama tapaus
ajetaan kahdesti tuoreessa kontekstissa, S:n kanssa ja ilman, S rakennettu *erillisistä*
harjoitustapauksista ennen ajoa, ympäristöpystytys vakioitu skriptiksi, järjestys
arvottu. Silloin se on vaihtoehto B alla, ei enää "pilotti".

## 4. "Kymmenesosalla hinnasta"

**Mistä luku tuli:** ei laskettu. HYPOTHESIS, joka esitettiin perusteluna. Se ei kelpaa.

**CALC kokeen 02 mitatusta kulutuksesta** (82 000 tokenia ja 9 min seinäkelloa yhdelle
"kloonaa, aja testit, korjaa yksi asia, raportoi" -kierrokselle; oletus: samaa luokkaa
oleva tapaus maksaa 50 - 150 k tokenia riippuen siitä, tarvitaanko selvitystä):

| Mittaus | Ajoja | Tokenia (suuruusluokka) | Ihmisaikaa | Oletukset |
|---|---|---|---|---|
| A: kolmen tapauksen sekventiaalinen pilotti | 3 + S:n rakennus | 0,3 - 0,5 M | 0,5 - 1 h (hyväksyntä, kirjaus) | ei kontrolleja, ei skriptattua roolia |
| B: minimaalinen paritettu koe (3 testitapausta × 2 haaraa, S 3 harjoitustapauksesta) | 6 + 3 + rakennus | 0,8 - 1,2 M | 2 - 3 h (skriptattu rooli, hyväksyntäsuitet, arvonta) | tuoreet kontekstit, vakioitu ympäristö |
| C: toistuvuusmittaus (20 tapauksen juurisyyluokittelu, ei korjauksia) | 20 lyhyttä | 0,2 - 0,4 M (10 - 20 k per tapaus: lue virhe, yritä toistaa aikarajalla) | 1 - 2 h (taksonomia ennalta, tarkistus) | ei S:ää, ei A/B:tä |
| Täysi A/B/C/D (12 testitapausta × 4 haaraa + 8 harjoitustapausta + 2 S:n rakennusta) | 48 + 8 + 2 | 4 - 6 M | 8 - 12 h | GPT §14 + omat muutokset |

Suhde A / täysi: tokeneissa noin 1/12, ihmisajassa noin 1/10. "Kymmenesosa" osui
suunnilleen oikeaan sattumalta, mutta se ei ollut laskettu eikä se ole peruste, koska
A ei tuota päätösinformaatiota (§3). **Eurot: UNKNOWN.** Tämän session tokenihintaa ei
tiedetä (tilaus, ei laskutus per token), joten rahamäärää ei voi johtaa evidenssistä.
Vertailu tehdään tokeneina ja ihmistunteina.

## 5. Kolmen seuraavan mittauksen vertailu

Kriteeri: odotettu päätösinformaatio per token ja per ihmistunti. Ei numeerisia
todennäköisyyksiä, koska niitä ei ole.

**Mikä on epävarmin oletus?** Ei "auttaako S" vaan sitä edeltävä: **onko luokassa
toistuvaa virhettä, josta S ylipäätään voi syntyä.** GPT:n julkinen rakennuskoe antoi
tästä jo yhden negatiivisen havainnon: 12 vanhasta PyPI-paketista 10 rakentui ilman
korjausta, toistuvaa virheluokkaa ei löytynyt. Jos toistuvuutta ei ole, A ja B mittaavat
S:ää, jota ei voi olla olemassa. Se on ainoa oletus, jonka kumoaminen tappaa koko
artefakti-S-haaran yhdellä halvalla havainnolla.

| Vaihtoehto | Mitä ratkaisee | Mitä ei ratkaise | Informaatio / kustannus |
|---|---|---|---|
| A: sekventiaalinen pilotti | S:n rakennuskulun ja tapauskustannuksen suuruusluokan | mitään S:n vaikutuksesta (§3) | matala: halpa mutta lähes nolla päätösinformaatiota |
| B: minimaalinen paritettu | onko S:llä havaittava vaikutus n = 3:ssa | vaikutuksen suuruus luotettavasti; toistuvuus (jos S:ää ei synny harjoitustapauksista, B on turha) | keskitaso: kolme kertaa A:n hinta, mutta ensimmäinen kausaalinen signaali |
| C: toistuvuusmittaus | onko S mahdollinen tässä luokassa; kuinka suuri osa "orvoista" on oikeasti rikki | mitään S:n vaikutuksesta | **korkein**: halvin, testaa edeltävän oletuksen, tappaa tai päästää B:n, tuottaa sivutuotteena "rikki vs. hiljainen" -osuuden, jota kaksi mallia on jo arvaillut |

**Järjestys:** C → (jos läpäisee) B → (jos B näyttää vaikutusta) täysi koe. A on
dominoitu: sen ainoa validi tuotos (rakennuskulu) syntyy B:n sivutuotteena.

## 6. STATE uudelleen

**Onko se enää teoriaa?** Ei. "Jos N kausaalisesti parantaa N+1:tä samoilla ulkoisilla
ehdoilla, vaikutus välittyy säilyvän tilan kautta" on analyyttisesti tosi jokaisessa
kehyksessä, jossa kausaatio ajan yli vaatii kantajan. Se on kausaalisen muistin
määritelmä. GPT sanoi sen, ja se pitää.

**Kaksi mekanismia, jotka molemmat täyttävät STATE-ydinehdon:**

1. **Erittäin suuri:** hakemistossa voittava fork maksullisella tasolla. N (päivitys)
   parantaa N+1:tä (sijoitus ja käyttäjät kasvavat). Kantaja: hakemiston sijoitus.
2. **Huono:** yhden hengen konsultointi, jossa jokainen toimeksianto tuottaa referenssin,
   joka helpottaa seuraavan myyntiä. N parantaa N+1:tä (hankinta halpenee). Kantaja:
   asiakkaiden muisti. Toimitus ei muutu, katto on tunnit.

Molemmat täyttävät ehdon. STATE ei erota niitä. Ero on siinä, *mihin talouden riviin*
kantaja vaikuttaa (jakelu ja käyttäjät vs. hankintakulu) ja *kuinka paljon* suhteessa
volyymiin. Ne ovat suuruuksia, jotka mitataan Q3:ssa. **STATE ei yksin rajaa hakutilaa
lainkaan.** Se on mittausohje: "nimeä kantaja ennen tulosta ja testaa se poistamalla".

**Mikä rajaa hakutilaa:** ei STATE vaan projektin *valittu veto*: "etsitään mekanismeja,
joissa kantaja on artefakti, jonka käytön rajakustannus lähestyy nollaa ja jonka
rakennuskulu on tiedossa". Se ei ole teoreema, se on HYPOTHESIS, jonka projekti on
valinnut, koska vain sitä voi mitata A/B:llä 0 eurolla. Se on rehellinen peruste, ja
se pitää sanoa ääneen: **koeasetelma valitsi teorian, ei päinvastoin.**

## 7. Lopputulos

### SURVIVES (commitin f5d26a7 sisältö, joka kestää)

- Baseline rajattuna: kustannuskatto määritellyn lopputuloksen korvaavassa hankinnassa,
  todistustaakka muualla.
- Viivästetyn kaappauksen neljä kirjausta ja lisäehto (maksaja eri osapuoli tai korvaava
  vaihtoehto läsnä pilotissa).
- SCARCITY:n siirto kestävyyskysymykseen; "hetkellinen etu ei riitä 10 000x:ään".
- Kuusi väärää positiivista GPT:n v2:ssa: näyttö on yksikkö- ja hetkitason, virheet
  populaatio- ja aikatason. Tämä pätee myös v2.1:een itseensä.
- Portfoliomekanismi väärän negatiivisen lähteenä.
- Haara D (S:n rakennuskulu kilpailijalle) täyteen kokeeseen.
- FACT: 0/14 tapauksessa este oli 1 000 euron puute tai mallien koodauskyky.
- FACT: html5lib on tapaus, jossa but-for on epätosi (ihmiset tekivät saman).

### MODIFIED (säilytetään eri muodossa)

- **v2.1 → v2.2:** jaetaan kahtia. *Pöytätesti* (ennen mittausta, kolme kysymystä,
  vastattavissa julkisesta datasta) ja *mittauslomake* (Q1 - Q4 yhdistettynä yhdeksi
  kohortti 2 -talouslaskelmaksi mittauksen jälkeen). Ks. alla.
- Q3: kohortti 2 samasta kanavasta ilman meidän valintaamme; eri kanava diagnostiikaksi;
  bundlaus ja yhteinen häntä riskitekijöiksi (todennäköisyys × tappio), ei tapoiksi;
  negatiivinen kohortti 2 tappaa vain ennalta asetetun oppimisbudjetin yli.
- Q4: "käyttö ei kasva volyymin mukana" poistetaan; takaisinmaksu vs. TAM-katto ja
  viereinen luokka, muuten UNKNOWN; vastafaktuaali kirjataan malliversiolla.
- Q5: raportointisääntö, ei portti. But-for kirjataan kolmella tasolla (ennakkohypoteesi,
  havaittu vaikutus, kustannusargumentti) eikä koskaan "todistettuna".
- Q6: tappiobudjetti on omistajan asetettava luku; "kirjataan sivuun" saa määräajan, jonka
  jälkeen sivuun kirjattu kuolee.
- 14 tapauksen väite: "oikeus, luottamus, pääsy" 5/14; kysyntä tai kilpailu ≥ 5/14.
  Ennuste: seuraava löydös kaatuu kysyntään tai kilpailuun; oikeuteen vain haltuunotossa.
- Pilotti A → vaihtoehto B, ja vasta C:n jälkeen.

### KILLED (ei enää kestä)

- v2.1 esikarsintatestinä: kolme kuudesta kysymyksestä ei ole vastattavissa ennen
  mittausta, yksi on raportointisääntö, yksi on prosessisääntö.
- "Jokaisessa 14 tapauksessa este oli oikeus, luottamus tai pääsy": 5/14.
- "Seuraava löydös kaatuu todennäköisimmin OSUUS-kysymykseen".
- "S:n käyttö ei kasva volyymin mukana" ehtona.
- "Eri kanava tai satunnaispoiminta" tappoehtona; "bundlaus halvempi" tappoehtona;
  "yhteinen häntä pysäyttää kaiken" tappoehtona; "kohortti 2 negatiivinen" tappoehtona
  ilman oppimisbudjettia.
- Kolmen parin pilotti päätöskelpoisena mittauksena; "kymmenesosalla hinnasta"
  perusteluna (ei laskettu; laskettuna suhde on oikea mutta merkityksetön).
- STATE löytöheuristiikkana. Se on mittausohje.

### UNKNOWN (aineisto ei ratkaise)

- Onko *missään* luokassa toistuvaa virhettä, josta artefakti-S voi syntyä (yksi
  negatiivinen havainto: GPT:n 12 pakettia).
- Mikä on tokenin hinta euroina tässä projektissa; siis kokeiden rahakustannus.
- Portfolion tappiobudjetti (omistajan luku).
- Yleisö-, sopimus- ja luottamustilan vaikutus: ei vastafaktuaalia, ei mittausta,
  mahdollisesti ei koskaan A/B-mitattavissa.
- Onko seuraava malliversio jo sisäistänyt sen S:n, jota mittaamme.

### Structural Test v2.2

**Pöytätesti** (ennen mittausta, julkisesta datasta, kaikki kolme vaaditaan jatkoon):

| # | Kysymys | Hyväksyttävä näyttö | Hylkäys | UNKNOWN |
|---|---|---|---|---|
| P1 | **Liikkuuko raha jo, ja kuka sen saa nyt ja miksi?** | Nimetty nykyinen saaja (toimittaja, alusta, "kukaan": raha jää lunastamatta) ja lähteestä luettu syy, miksi hän saa sen | Rahaa ei liiku kenellekään eikä ole lakisääteistä tai sopimuksellista velvoitetta maksaa | Saaja tiedossa, syy ei |
| P2 | **Onko oikeus, pääsy ja laillisuus hankittavissa, ja mihin hintaan?** | Nimetty oikeus tai pääsy, sen hankintareitti ja hinta (raha, aika, kyky); perintä-, lupa- ja tietosuojarajat tarkistettu | Reitti vaatii kykyä, lupaa tai suhdetta, jota ei voi hankkia projektin resursseilla, tai laillisuus alle 3 | Reitti tiedossa, hinta ei |
| P3 | **Onko kantaja artefakti, ja onko luokassa toistuvuutta?** | Nimetty S, sen rakennuskulun arvio ja toistuvuusmittaus (§8:n koe tai vastaava): vähintään yksi virheluokka, jossa ≥ 3 tapausta 20:stä | Toistuvuutta ei ole, tai S on yleisö/sopimus/luottamus, jota ei voi mitata poistamalla: kirjataan *ei-mitattavaksi haaraksi* määräajalla, ei jatkoon | Toistuvuutta ei ole vielä mitattu |

**Mittauslomake** (pilotin tai kohortti 2:n jälkeen, yksi laskelma):

Kohortti 2 -nettotalous: valinta ja vaihtoehdon kustannus maksajalle, hankinta,
toimitus, ylläpidon kulmakerroin, S:n vastafaktuaalinen vaikutus (malliversio kirjattu),
takaisinmaksutoistot vs. TAM ja viereinen luokka, riskitekijät todennäköisyys × tappio
(yhteinen riippuvuus, nimetty bundlaaja kannustimineen), oppimisbudjetti, meille jäävä
osuus. Tappo: netto negatiivinen yli oppimisbudjetin. Raportointi erikseen: but-for
kolmella tasolla.

### Kolme vastausta

**1. Onko v2.1 riittävän hyvä lukittavaksi?** Ei. Se on mittauksen jälkeinen lomake,
joka esitettiin esikarsintana. Lukitaan v2.2: pöytätesti ennen mittausta, lomake sen
jälkeen. Pöytätesti on lukittavissa nyt; lomakkeen rivit lukitaan, kun ensimmäinen
kohortti on olemassa.

**2. Onko kolmen tapauksen pilotti informaatiotehokkain?** Ei. Se ei tuota
päätösinformaatiota S:stä (§3). Informaatiotehokkain on toistuvuusmittaus (C), koska
se testaa oletuksen, jota A ja B edellyttävät, ja sillä on jo yksi negatiivinen
havainto vastassaan.

**3. Pienin koe, joka pitäisi tehdä seuraavaksi:** toistuvuusmittaus. Suunnitelma alla.

## 8. Lukittava koesuunnitelma: koe 03, toistuvuusmittaus

Tarkoitus: selvittää, onko "orpo mutta rikki" -luokassa toistuvaa virhettä, josta
uudelleenkäytettävä korjaustieto (artefakti-S) voi syntyä. Ei korjata mitään. Ei
A/B:tä. Ei WordPress-migraatioita. Ei yhteydenottoja, ei rahaa.

**Perusjoukko (lukittu):** kaksi jo kerättyä julkista listaa, `data/orvot/pypi.org-orvot-top5000.csv`
(959 riviä, varmennettu PyPI:stä) ja `data/orvot/wordpress-orvot-top10000.csv` (2 354
riviä). Suorittaja valitsee listan säännöllä: se lista, jonka rivillä on koneellisesti
toistettava epäonnistumissignaali (PyPI: lähdeasennus tai import Python 3.14:llä
puhtaassa venvissä; WordPress: aktivointi tuoreessa WordPress 7.1 -asennuksessa WP-CLI:llä
ilman virhettä). Jos molemmat ovat toteutettavissa, valitaan PyPI, koska siitä on jo
GPT:n 12 tapauksen esihavainto, johon tulos voidaan verrata. Valinta kirjataan ennen
ensimmäistä ajoa.

**Otanta (lukittu):** 20 riviä satunnaisesti siemenellä 20260916 niistä riveistä, joilla
lataukset (PyPI) tai aktiiviset asennukset (WordPress) ovat vähintään 100 000 kuukaudessa
/ yhteensä. Otos kirjataan tiedostoon ennen yhdenkään rivin tarkastelua. Lisäksi
positiivinen kontrolli: html5lib 1.1 lähdeasennuksena (tunnettu virhe).

**Toimenpide per rivi (aikaraja 5 min konetta, ei korjausyrityksiä):**
1. PyPI: `python3.14 -m venv`, `pip install --no-binary :all: <paketti>==<viimeisin>`;
   jos onnistuu, `python -c "import <moduuli>"`; jos onnistuu, `pip install <paketti>`
   (wheel) ja import. WordPress: `wp plugin install <slug> --activate` tuoreessa 7.1:ssä,
   sitten `wp plugin list` ja PHP-virheloki.
2. Kirjataan: onnistui / epäonnistui missä vaiheessa / virheilmoituksen ensimmäinen rivi.
3. Luokitellaan **ennalta lukitulla taksonomialla**, yksi luokka per rivi:
   T1 pakkaus- tai rakennusinfra (setuptools, pkg_resources, distutils, build backend);
   T2 kielen tai ajoympäristön versio (poistettu API, syntaksi: esim. `ast.Str`, `imp`,
   PHP 8 -yhteensopimattomuus); T3 riippuvuuden poistettu tai muuttunut API; T4 vain
   testi- tai kehitysinfra rikki, tuote toimii; T5 toiminnallinen virhe ajossa;
   T6 korjaamaton tietoturva-advisory (paketti toimii); T7 ei toistettavissa: toimii.
   Luokitussääntö: virheilmoituksen ensimmäinen rivi ratkaisee; jos kaksi luokkaa
   sopii, valitaan pienempi numero. Tämä sääntö ei muutu tulosten jälkeen.
4. Kirjataan, olisiko T1 - T3 -tapauksen korjaus **sama korjausmalli** kuin toisella saman
   luokan tapauksella: sama virheilmoitus (normalisoitu: versionumerot ja polut
   poistettu) = sama korjausmalli. Ei arviota "melko sama".

**Mittarit (lukittu):**
- R = niiden rivien osuus, jotka epäonnistuvat (T1 - T6) / 20.
- K = suurin yksittäinen korjausmalli (samaksi normalisoitu virheilmoitus) T1 - T3:ssa,
  lukumääränä.
- H = T7:n osuus (orpo mutta ei rikki).

**Tulkinta (lukittu ennen ajoa):**
- **PASS → vaihtoehto B:** K ≥ 3 ja R ≥ 0,3. Artefakti-S on mahdollinen; B ajetaan
  K:n korjausmallilla, harjoitustapaukset K:n sisältä, testitapaukset K:n ulkopuolelta
  mutta samasta taksonomialuokasta.
- **KILL:** K ≤ 1 tai R < 0,15. Luokassa ei ole toistuvaa korjattavaa; artefakti-S-haara
  kuolee tässä luokassa; ei B:tä, ei täyttä koetta. Toinen lista voidaan ajaa samalla
  protokollalla kerran; jos sekin KILL, artefakti-S-haara kirjataan kuolleeksi ja
  projekti siirtyy ei-artefaktitiloihin, jotka vaativat omistajaa.
- **UNKNOWN:** K = 2 tai 0,15 ≤ R < 0,3. Otos laajennetaan 40 riviin samalla
  siemenellä kerran. Sen jälkeen ei laajenneta.
- Sivutuote riippumatta tuloksesta: H kirjataan ORVOT-muistioon lukuna, joka korvaa
  arvailun "valmis vs. hylätty".

**Kustannus (CALC, ei euroja):** 20 - 40 riviä × 10 - 20 k tokenia = 0,2 - 0,8 M tokenia;
ihmisaikaa 1 - 2 h (protokollan tarkistus, otoksen lukitus, tuloksen luku). Konetta
5 min × 20 - 40 = alle 4 h taustalla.

**Mitä koe ei kerro:** auttaako S (se on B:n tehtävä), maksaako kukaan, siirtyykö
korjaustieto luokkien välillä. Se kertoo vain, onko mitattavaa.

**Ennakkorekisteröinti:** tämä tiedosto commitissa ennen ajoa. Siemenen, kynnysten ja
taksonomian muutos tuloksen jälkeen mitätöi tuloksen.
