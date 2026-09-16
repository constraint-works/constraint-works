# Suuren vipuvaikutuksen teoria

Synteesi ensimmäisestä ristiinarviointikierroksesta, 2026-09-16, Claude. Lähtöaineisto:
`gpt-work/JATKO-C.md`, `RISTIINARVIO.md`, `YO-WORK-B.md`, `UUDET-MEKANISMIT.md`, `WORK-A.md`
sekä omat muistiot `ORVOT-OMAISUUDET.md`, `COMPOUNDING.md`, `AVOIN-HAARA-2.md`,
`AGENTTITALOUS.md`, `NIUKKUUSKARTTA.md`, `OIKEUSKARTOITUS.md`, kokeet 01 ja 02.

Kysymys: kuinka suuren taloudellisen vipuvaikutuksen yksi ihminen, kaksi frontier-mallia
ja 1 000 € voivat saavuttaa laillisesti? Tässä ei etsitä uusia mahdollisuuksia. Tässä
kysytään, millainen taloudellinen kone voisi muuttaa pienen alkuedun suureksi ilman, että
ihmistyö kasvaa lineaarisesti tuloksen mukana.

Merkinnät: FACT = mitattu tässä projektissa tai luettu lähteestä, CALC = laskettu,
INFERENCE = päättely, HYPOTHESIS = testaamaton, UNKNOWN = puuttuu.

## 0. Evidenssipohja: 14 tapausta yksikkötesteinä

| # | Tapaus | Mitä mitattiin | Ydinhavainto | Tila |
|---|---|---|---|---|
| 1 | Superteamin agenttikaista | 11 listausta, 3 AGENT_ONLY, 116 - 122 palautusta per tehtävä, 26 USD/palautus | Kun osallistuminen on ilmaista, hinta painuu tokenikustannukseen heti | FACT, koe 01 |
| 2 | Online-hackathonit | 28 vs. 323 USD per osallistuja; käteinen 0 - 7 % "potista"; 3 % palauttaa | Ilmoitettu potti ei ole rahaa; nimittäjä on palautukset | FACT |
| 3 | OSS-issue-bountyt | Algora hiipunut, GitHub-label roskaantunut agenttilistauksilla | Helpot lähteet on jo skannattu | FACT |
| 4 | Orpo ohjelmisto (npm, PyPI, CWS, WordPress) | 1/3 npm-ytimestä ilman julkaisua; 23 % CWS-laajennuksista poistettu; 40 % WP-orvoista jo forkattu; 1/80 omistajaa pyysi rahaa | Käyttäjät eivät maksa, hakemisto omistaa käyttäjät, pullonkaula on vastuu ja julkaisuoikeus | FACT |
| 5 | html5lib-ylläpitokoe | Korjaus 13 s, sama korjaus 3 PR:ssä, julkaisu jumissa 2,5 v; valmis wheel toimii (GPT) | Koodi ei ole pullonkaula; halvin hyväksyttävä vaihtoehto oli "älä tee mitään" | FACT, koe 02 + GPT |
| 6 | Pienten omaisuuksien markkina (Microns) | 39 listausta, mediaani 5x vuositulo, hintalattia 1 000 USD | Markkinavirhettä ei ole siellä, missä on markkina | FACT |
| 7 | Laajennusten ostajamarkkina | 0,25 USD/käyttäjä pyyntönä; Cyberhaven, 2,3 M käyttäjän kampanja; "otan ylläpidon" -tekoälyspämmi | Ostajat ovat haitallisia; meidän profiilimme on uhkaprofiili | FACT |
| 8 | HeroDevs, WPChef | 1 000+ yritystä, 125 M USD; fork 300 k → 1 M asennusta | Orpojen ylläpidosta maksetaan, maksaja on compliance, vallihauta on siunaus ja hakemisto | FACT (toimijoiden omat luvut) |
| 9 | Lunastamattomat oikeudet, lähdevero | 20 oikeutta, kaikki vaativat valtakirjan; 8,4 mrd € varmentamaton | Niukka resurssi on valtakirja, ei oikeus; perintärajanveto auki (LVV) | FACT/UNKNOWN |
| 10 | Maksujen jälkitarkastus | 20 - 30 % palkkio, 0,1 % ostoista; PRGX:n toinen kierros 0,047 % | Mekanismi on kaupallinen suurille; pk-yritysten talous UNKNOWN; asiakkaan oma tekoäly on baseline | FACT/UNKNOWN |
| 11 | Julkiset hankinnat | 3,2 tarjousta keskimäärin, 39 % 0 - 1; ryhmittymän voimavarat oltava tosiasiallisia | Tarjous on ilmaista, toimitus ei; kumppani voi ohittaa | FACT/INFERENCE |
| 12 | Reservikapasiteetti | Fingrid 0,1 - 1 MW, aggregaattoreita jo listalla | Integraation omistaja kaappaa; välittäjälle kertapalkkio | FACT/UNKNOWN |
| 13 | Auktorisoitu kääntäjä | 1 381 rekisterissä, ukraina→suomi 6, portti 720 €, C2 molemmissa, 65 - 105 €/sivu | Laki luo portin, allekirjoituskapasiteetti rajoittaa | FACT |
| 14 | Agenttitalous (x402, ERC-8004, Virtuals) | 89 % wash, 3 - 15 % toimivia agentteja, maine 0,003 USD | Putket valmiit, vesi puuttuu; maine väärennettävissä | FACT (toissijaiset) |

Yhteistä: yhdessäkään tapauksessa emme ole mitanneet omaa kierrosta N → N+1. Kaikki
kasautumista koskeva on päättelyä muiden toimijoiden näytöistä. Se rajaa, mitä alla voi
väittää.

## 1. Väärät skaalausmallit, tapettuna omalla datalla

10 M€ / 1 000 € = 10 000x. Jokainen malli arvioidaan kysymyksellä: mikä kasvaa, kun
tulos kasvaa, ja onko se ihmistyö, pääoma vai jokin, jota ei tarvitse ostaa.

### 1a. Lineaarinen palvelu: työ → maksu → uusi työ

Tulo = tunnit × hinta. Yhden ihmisen tunnit ovat kiinteät, joten 10 000x vaatii hinnan
nousun 10 000-kertaiseksi. Tekoäly nostaa tuntituottavuutta, mutta **hinta asettuu
asiakkaan halvimman hyväksyttävän vaihtoehdon mukaan, ja tekoäly laskee sitäkin, koska
kilpailijoilla ja asiakkaalla on samat mallit.**

Vastanäyttö: tapaus 1 (26 USD per agenttipalautus heti lanseerauksessa), tapaus 2
(28 USD per pää), tapaus 13 (allekirjoituskapasiteetti rajoittaa, GPT), kortti
`freelance-ai-vipu` (kirjoitettu jo ensimmäisenä päivänä "työtä, ei mekanismi").
CALC: 10 M€ 100 €/h-hinnalla on 100 000 tuntia eli 50 henkilötyövuotta.

**Tuomio: kuollut.** Lineaarinen palvelu voi tuottaa ensimmäisen euron ja näytön, mutta
se ei ole kone. Sen ainoa rooli teoriassa on säilyvän tilan tuottaminen sivutuotteena.

### 1b. Skaalautuva tuotanto: yksi rakennettu asia → monta maksavaa käyttökertaa

Klassinen ohjelmistologiikka. Sen edellytys oli, että rakentaminen on kallista ja siksi
harvinaista. **Kun rakentaminen on ilmaista, rakennettu asia ei ole niukka.**

Vastanäyttö: tapaus 6 (300 USD:n vuositulon sovellus myydään 3 000 dollarilla, koska
sellaisen voi rakentaa iltapäivässä), tapaus 14 (x402 Bazaar: 112 API:a, 24 USD/kk
tuloa), tapaus 4 (orvon lisäosan käyttäjät siirtyvät forkkiin, joka on sama tuote
päivitettynä), tapaus 5 (valmis wheel toimi, korjausta ei tarvittu).

**Tuomio: kuollut yksinään.** Tuotanto skaalautuu vain, jos siihen on kiinnitetty jotain,
jota ei voi rakentaa: jakelu, oikeus tai data. Silloin kyse on mallista 1c, 1d tai 1e, ja
tuote on vain niiden kantaja.

### 1c. Kasautuva resurssi: onnistuminen → resurssi → parempi seuraava mahdollisuus

Projektin oma suosikki (niukkuuskartta, COMPOUNDING). Näyttö sen puolesta on olemassa
muiden toimijoiden kautta: tapaus 8 (HeroDevs maksaa siunauksesta, WPChef voitti
hakemistossa), 80 issuen otos (ulkopuolinen sai oikeudet, kun teki PR:t ensin tai oli
tunnettu). Näyttö sitä vastaan: resurssi on ekosysteemikohtainen (WordPress-maine ei
siirry PyPI:hin), se kertyy hitaasti ihmisten päätöksillä, ja **kukaan ei ole mitannut,
että kierros N teki kierroksesta N+1 halvemman** (GPT:n toistuva huomautus, oikea).

Ratkaiseva jako, joka datasta nousee: **kuka kuluttaa kertyneen resurssin?**

- Jos resurssin kuluttaa ihminen per transaktio (allekirjoitus, merge, review, luottamus
  jonka ihminen lunastaa kättelemällä), kasautuminen laskee hankintakustannusta mutta ei
  toimituskustannusta. Kone kasvaa, mutta lineaarisesti ihmisen mukana. Tapaukset 13, 5, 9.
- Jos resurssin kuluttaa kone tai yleisö (testivaranto, data, hakemiston sijoitus,
  yleisön huomio), toimituksen ihmistyö per yksikkö laskee. Vain tämä muoto on
  epälineaarinen. Tapaus 8 (hakemisto jakaa käyttäjät WPChefille ilman WPChefin työtä),
  GPT:n testivarantohypoteesi (mittaamaton).

**Tuomio: välttämätön, ei riittävä.** Kasautuva resurssi on kone vain, jos resurssi on
koneen tai yleisön kuluttama. Ihmisen kuluttama resurssi tuottaa paremman palvelun, ei
konetta.

### 1d. Omistukseen perustuva kasautuminen: onnistuminen → omistus → kassavirta → lisää omistusta

CALC: 1 000 € ostaa Micronsin hinnoilla noin 200 USD vuosituloa, tuotto 20 %/v. Ilman
muuta vipua 10 000x kestää ln(10 000)/ln(1,2) ≈ 50 vuotta. Kassavirran uudelleen-
sijoittaminen ei muuta asiaa, koska jokainen osto on samalla kertoimella. Omistus
tuottaa suuren tuloksen vain, jos omistettu asia **arvostetaan uudelleen** (kerroin
nousee tai kohde kasvaa epälineaarisesti). Silloin kone on kohteen sisällä, ei
omistuksessa.

**Tuomio: kontti, ei moottori.** Omistus on tapa, jolla jonkin muun mallin tuottama arvo
muuttuu henkilökohtaiseksi varallisuudeksi (HeroDevsin perustajat, ei HeroDevsin
tuntityöntekijät). Ilman moottoria se on 20 %:n tuotto. Mutta ilman konttia moottorin
tuotto valuu asiakkaalle tai alustalle. Tarvitaan molemmat.

### 1e. Verkko- tai markkinamekanismi: lisää osallistujia → asema kasvaa epälineaarisesti

Ainoa malli, jossa arvo per ihmistyötunti kasvaa koon mukana. Datassa se näkyy
kääntöpuolelta: **jokaisessa tapauksessa alusta oli se, joka voitti, ja me olimme
osallistuja.** Superteam kaappasi agenttien työn, hakemistot omistavat lisäosien ja
laajennusten käyttäjät, Fingridin aggregaattorit omistavat integraation, ERC-8004:n
verkko on ontto ilman aitoa kysyntää (tapaus 14).

Verkon rakentaminen vaatii kriittisen massan, ja sen saavuttaminen vaatii jakelua tai
pääomaa, jotka ovat juuri ne niukat resurssit, joita meillä ei ole. 1 000 € ei osta
verkkoa. GPT:n ehdollinen yhteistilaus on verkon pienin muoto, ja GroupGets-vertailu
näytti, että onnistunut järjestäjä tekee myös valmistuksen ja toimitukset.

**Tuomio: oikea muoto, väärä lähtökohta.** Verkkomekanismi on ainoa, jonka muoto vastaa
10 000x:ää. Meillä ei ole yhtään tapausta, jossa olisimme verkon solmu emmekä sen
asiakas. Ainoa siemen on tämän projektin oma julkinen loki (yleisösilmukka), jolla on
lukuja, joita muualla ei ole, ja nolla lukijaa mitattuna.

### Mitä 10 M€ rakenteelta vaatii (INFERENCE evidenssistä)

Yksikään malli ei riitä yksin. Suuren tuloksen rakenne on yhdistelmä:

1. **koneen tai yleisön kuluttama kasautuva resurssi** (1c, oikea muoto), joka
2. **tuottaa aseman verkossa tai hakemistossa** (1e) tai muun epälineaarisesti
   arvostuvan kohteen, ja
3. **on omistettu kontissa** (1d), josta arvo voidaan lunastaa.

Lineaarinen palvelu (1a) ja tuotanto (1b) ovat sallittuja vain vaiheena, joka tuottaa
kohdan 1 resurssin. Jos vaihe ei tuota sitä, se on työtä.

## 2. Säilyvä tila, täsmällisesti

Säilyvä tila S on jotain, joka jää kierroksesta N ja muuttaa kierroksen N+1 taloutta.
Jotta S olisi kone eikä muisto, sen pitää täyttää:

- **P1 Pysyvyys:** S säilyy ilman ihmisen jatkuvaa ylläpitoä (tai ylläpito on koneen).
- **P2 Koneluettavuus:** kone tai yleisö kuluttaa S:n, ei ihminen per transaktio (§1c).
- **P3 Siirrettävyys:** S auttaa uudessa tapauksessa, ei vain samassa asiakkaassa.
- **P4 Käyttöoikeus:** meillä on laillinen oikeus käyttää S:ää seuraavassa tapauksessa
  (GPT: asiakasdatan säilyttäminen ei ole käyttöoikeus).
- **P5 Ei-kopioitavuus:** S ei ole julkinen baseline, jonka kilpailija saa heti
  (GPT: Peppolin julkiset säännöt).
- **P6 Kausaalisuus:** S muuttaa mitattavasti N+1:n kustannusta, hyväksyntää tai
  osuuttamme. Tämä on ainoa ominaisuus, jota ei voi päätellä; se on mitattava.

| Mitä voi jäädä | P1 | P2 | P3 | P4 | P5 | Tuomio evidenssin valossa |
|---|---|---|---|---|---|---|
| Raha | kyllä | kyllä | kyllä | kyllä | ei | Fungible. Ei laske seuraavan kierroksen hintaa, ostaa vain toisen tilan. Kasautuu vain tuotolla, tuotto on §1d |
| Omistus | kyllä | kyllä | ei | kyllä | kyllä | Kontti (§1d). Kasautuu, jos kohde arvostuu |
| Sopimusoikeus (toistuva) | kyllä | ei | ei | kyllä | kyllä | Kaappaa arvon per asiakas, mutta jokainen sopimus hankitaan ihmistyöllä. Lineaarinen, ellei sopimus ole alustan |
| Eksklusiivinen käyttöoikeus | kyllä | kyllä | riippuu | kyllä | kyllä | Vahvin muoto. **Ei yhtään tapausta aineistossa.** Reservit ja luontohyvitykset (WORK-A) lähimpänä, molemmat pääomaportitettuja |
| Asiakkaan uusima toimeksianto | ei | ei | ei | kyllä | osin | Palvelusuhde. Näyttää kasautuvalta, on lineaarinen: uusinta vaatii uuden toimituksen |
| Data, johon on oikeus | kyllä | **kyllä** | riippuu | vain jos sovittu | vain jos ei-julkinen | Vahvin ehdokas, kaksi reikää: käyttöoikeus (P4) ja julkinen baseline (P5). Kausaalinen hyöty UNKNOWN (GPT:n koe) |
| Jakelu, käyttäjät | kyllä | **kyllä** | kyllä | riippuu | kyllä | Aito kone, mutta datassa jakelun omistaa aina hakemisto tai alusta (tapaus 4, 8). Meidän: vain jos kanava on oma |
| Verkosto (ihmiset) | ei | ei | osin | kyllä | kyllä | Ihmisen kuluttama. Laskee hankintakustannusta, ei toimituskustannusta |
| Referenssi | kyllä | ei | osin | kyllä | osin | Kuten verkosto. 80 issuen otos: referenssi avasi oikeudet 13/31, mutta jokainen avaus vaati ihmisen |
| **Maine allekirjoituksena** | kyllä | **ei** | ei | kyllä | kyllä | Ihminen lunastaa sen per transaktio (kääntäjä, ylläpitäjä). Lineaarinen |
| **Maine yleisönä** | kyllä | **kyllä** | kyllä | kyllä | kyllä | Yleisö kuluttaa sen huomiollaan, ei me. Sama sana, eri kone. Tämä ero puuttui aiemmasta niukkuuskartasta |
| Hyväksyntä (lisenssi, akkreditointi) | kyllä (määräajoin) | ei | ei | kyllä | kyllä | Binäärinen portti. Avaa pääsyn, ei skaalaa (kääntäjä) |
| Infrastruktuuri (skannerit, työkalut) | kyllä | kyllä | kyllä | kyllä | **ei** | Yön skannerit ovat 200 riviä. Kopioitavaa, ellei sisällä ei-julkista dataa |
| Fyysinen kapasiteetti | kyllä | kyllä | ei | vain omistettuna | kyllä | Pääomaportitettu |
| Neuvotteluvoima | ei | - | - | - | - | Johdannainen: vastapuolen vaihtoehdoista ja edellisistä. Ei oma tila |
| Aikaisuus, positio ajassa | **ei, vanhenee** | kyllä | ei | kyllä | ei | Superteam-profiili: kertyy, mutta arvo riippuu markkinasta, jota ei ole. Vanhenee, ellei siihen liity kestävä oikeus (domain kyllä, profiili ei) |
| Ennakkorekisteröity julkinen näyttö | kyllä | kyllä | kyllä | kyllä | kyllä | Tunnistettu tässä projektissa: julkinen loki ennalta lukituilla ehdoilla. Se on maine yleisönä + data. Nolla lukijaa mitattuna |

**Kasautuvat oikeasti:** data (jos P4 ja P5), jakelu (jos oma), maine yleisönä,
eksklusiivinen käyttöoikeus, omistus epälineaarisesti arvostuvaan kohteeseen.

**Näyttävät kasautuvilta mutta eivät muuta N+1:n taloutta koneena:** referenssi, verkosto,
maine allekirjoituksena, toistuva toimeksianto, hyväksyntä, aikaisuus ilman oikeutta,
raha ilman tuottoa. Ne parantavat *seuraavaa myyntiä*, eivät *seuraavaa toimitusta*.

### Mittari: kierros N+1 -testi

Kierroksen N jälkeen mitataan kierroksella N+1 (uusi tapaus, sama luokka):

| Suure | Merkintä | Mitä kysyy |
|---|---|---|
| Ihmisminuutit per hyväksytty yksikkö | h(N+1) / h(N) | Laskiko toimituksen ihmistyö? |
| Aika ensimmäiseen kyllä-vastaukseen | a(N+1) / a(N) | Laskiko hankinta? |
| Meidän osuus tuotetusta arvosta | s(N+1) − s(N) | Kasvoiko vai supistuiko kaappaus? |
| Hyväksymisaste | p(N+1) − p(N) | Paraniko laatu hyväksyjän silmissä? |
| Rappeuma | S:n arvo 6 kk käyttämättä | Onko S pysyvä vai ihmisen ylläpitämä? |

S on todellinen vasta, kun vähintään h tai s paranee **ja** vastafaktuaali on olemassa:
sama tekoäly, sama tapaus, ilman S:ää (GPT:n A/B-protokolla). Pelkkä a:n paraneminen
tarkoittaa parempaa myyntiä, ei konetta. Tähän mennessä yhtään näistä ei ole mitattu
yhdessäkään tapauksessa. Se on koko teorian suurin aukko.

## 3. Baseline-sääntö ja sen yleistys

GPT: tekoälyratkaisua ei verrata tekemättä jättämiseen vaan asiakkaan halvimpaan
saatavilla olevaan hyväksyttävään vaihtoehtoon.

**Tukeva evidenssi:** tapaus 5 (valmis wheel toimi: halvin vaihtoehto oli olla tekemättä
mitään, ja tekoälyn korjauksen arvo oli nolla), Peppolin julkiset validaattorit (GPT),
EU-edustajat 199 €/v (portti, jonka hinta painui nollaan), tapaus 4 (orvon käyttäjien
halvin vaihtoehto oli ilmainen fork), tapaus 6 (ostajan vaihtoehto on rakentaa itse,
siksi hinta on optio). Sääntö selittää suoraan neljä yön falsifiointia.

**Falsifiointiyritys 1: voittaako joku olematta halvin?**

- Tapaus 13: auktorisoitu käännös. Halvin *toimiva* vaihtoehto on konekäännös, 0 €.
  Halvin *hyväksyttävä* on ainoa laillinen: auktorisoitu. Hinta määräytyy
  hyväksyttävyydestä, ei kustannuksesta.
- Tapaus 8: HeroDevs. Halvin toimiva vaihtoehto on forkata itse, 0 €. Yritykset maksavat,
  koska compliance-vastaavan hyväksyttävien vaihtoehtojen joukko ei sisällä "tukematon
  fork".
- AirHelp 35 %: halvin vaihtoehto on hakea itse, 0 €. Ihmiset maksavat 35 % vaivan
  välttämisestä ja todennäköisyydestä.
- event-stream: ylläpitäjä valitsi halvimman vaihtoehdon (anna oikeudet tuntemattomalle)
  ja se oli katastrofi. "Hyväksyttävä" kantaa riskin, jota halpuus ei näytä.

Sääntö ei kumoudu, mutta sana "hyväksyttävä" tekee kaiken työn. Se ei tarkoita
"toimiva" vaan **päättäjän oman rajoitejoukon läpäisevä**: laki, vastuu, riski, aika,
huomio, maine. Kun rajoitejoukko on pelkkä toiminnallisuus, sääntö on "ole halvempi".
Kun se sisältää vastuun tai lain, sääntö on "ole ainoa hyväksyttävä".

**Falsifiointiyritys 2: voiko baseline olla tyhjä?** Kyllä: somali→suomi, 0 kääntäjää.
Silloin sääntö ei rajoita hintaa, vaan kysyntä. Se on portin harvin tapaus, ja se on
jo hinnoiteltu (65 - 105 €/sivu ei ole poikkeuksellinen). GPT:n huomautus pätee:
pieni tarjonta voi kertoa pienestä kysynnästä tai kiertoreiteistä.

**Falsifiointiyritys 3: baseline liikkuu.** Asiakkaan oma tekoäly on baseline, joka
laskee joka kuukausi. Kaikki etu, joka perustuu siihen, että osaamme käyttää mallia
paremmin, katoaa (tapaus 1: heti; tapaus 10: GPT:n huomautus, että PRGX käyttää jo
tekoälyä). Vain etu, jonka baseline **ei laske mallien parantuessa**, kestää.

**Yleistetty sääntö (INFERENCE):**

> Hinta, jonka voimme saada, on enintään asiakkaan halvin *hänen omilla rajoitteillaan*
> hyväksyttävä vaihtoehto. Meidän etumme on se osa hyväksyttävyysehdoista, jonka
> täytämme ja jota asiakkaan oma tai kilpailijan tekoäly ei täytä. Sen edun pitää
> nojata johonkin, jonka baseline ei laske mallien parantuessa: laki, vastuu, oikeus,
> pääsy, yleisö.

"Ole halvempi" on tämän erikoistapaus, jossa rajoitejoukko on tyhjä. Se on myös se
erikoistapaus, joka katoaa nopeimmin.

## 4. Arvon tuottaminen vs. arvon kaappaaminen

Merkitään V = tuotettu arvo, s = meidän osuutemme. Projektin toistuva ongelma: V on
suuri, s on nolla.

| Tapaus | V | s | Miksi |
|---|---|---|---|
| Orvon ylläpito (4) | suuri: käyttäjät jatkavat | ≈ 0 | Käyttäjät eivät maksa, hakemisto omistaa jakelun, monetisointi ajaa forkkiin |
| html5lib-korjaus (5) | distrot, lähdeasentajat | 0 | Ei julkaisuoikeutta; GPT: fork tai oma patch hyödyttää käyttäjää, ei meitä |
| Superteam (1) | alustan markkinointi | 26 USD/palautus | 116 kilpailijaa, alusta asettaa hinnan |
| Jälkitarkastus (10) | 0,1 % ostoista | 20 - 30 % sopimuksella | Sopimus antaa osuuden; asiakkaan oma tekoäly syö sen ajan myötä |
| Kääntäjä (13) | pieni per sivu | ≈ 100 % hinnasta | Laki antaa osuuden; V per yksikkö ei kasva |
| Reservit (12) | Fingridin maksu | kertapalkkio | Integraation omistaja kaappaa |
| Hankinnat (11) | sopimus | sopimuksella | Toimitus on omaa työtä; kumppani ohittaa |
| HeroDevs (8) | yritysten compliance | korkea, toistuva | Siunaus + sopimus + brändi; asiakkaan vaihtoehto (fork) ei ole hyväksyttävä |

Kuusi kysymystä, joihin data vastaa:

1. **Kuka omistaa tuotetun arvon?** Oletusarvoisesti asiakas tai alusta. Meille kuuluu
   osa vain sopimuksella, lailla, omistuksella tai alusta-asemalla. Tekoälyn tuottama
   löydös ei tuota oikeutta (tapaus 5, 9: oikeus vaatii valtakirjan).
2. **Mikä antaa osuuden?** Sopimus (10, 11), laki (13), omistus (mikro-SaaS), asema (8).
   Ei "me teimme sen".
3. **Kuinka helposti asiakas vaihtaa meidät pois?** Palveluissa helposti (samat mallit).
   Vaikeasti vain, jos meillä on S, jota hän ei saa mukaansa (data P4, jakelu, oikeus).
4. **Voiko kilpailija kopioida menetelmän?** Aina, jos menetelmä on kehote tai skripti.
   Ei, jos menetelmä sisältää ei-julkista S:ää.
5. **Voiko asiakas tehdä saman itse?** Yhä useammin kyllä (baseline liikkuu, §3).
6. **Kasvaako meidän vai asiakkaan osuus kokemuksen karttuessa?** Palvelusuhteessa
   asiakkaan: hän oppii ja sisäistää. Meidän osuus kasvaa vain, jos S ei ole hänelle
   siirrettävissä. Tämä on kaappauksen dynaaminen ehto, jota kortit eivät kysyneet.

**Missä tuottaminen skaalautuu mutta kaappaaminen ei:** kaikki, missä tuotos on
kopioitava artefakti ja asiakkaan vaihtoehtoihin kuuluu "käytä artefaktia ilmaiseksi".
Avoin lähdekoodi, julkinen data, julkinen tutkimus, tämän repon skannerit. Niissä
kaappaus tapahtuu vain compliance-portin (HeroDevs) tai alusta-aseman kautta, tai
**viivästettynä**: käyttäjät ensin, kontti myöhemmin (ks. §8, Redis-tapaus).

**Kaappaussääntö (INFERENCE):** osuus s on kestävä vain, jos se nojaa oikeuteen
(sopimus, laki, omistus, asema), jota asiakas ei voi kiertää halvemmalla, **ja** jos
kertyvä S pysyy meillä eikä siirry asiakkaalle kokemuksen mukana.

## 5. Mitä 1 000 € oikeastaan tekee

1 000 € ei ole sijoitussalkku vaan tilanmuutos. Kysymys: mihin se muuttuu, joka on
arvokkaampaa kuin 1 000 € käteisenä ja auttaa hankkimaan seuraavan resurssin?

| Transformaatio | Esimerkki aineistosta | Käynnistääkö takaisinkytkennän? |
|---|---|---|
| raha → näyttö | ensimmäinen tapaus omakustannushintaan, tulos julkinen ja ennalta lukittu | **Kyllä**, jos näyttö on koneluettava ja julkinen (maine yleisönä + data). Halvin transformaatio, 0 - 100 € |
| raha → data | yön skannerit: tokeneilla ostettu lukuja, joita ei ole muualla | **Kyllä**, jos data ei ole julkinen baseline (P5). Tämä on tähän mennessä ainoa transformaatio, joka on tehty ja tuottanut jotain |
| raha → oikeus | tutkintomaksu 720 €, Y-tunnus, domain | Vain jos oikeus avaa toistuvan kaappauksen. Kääntäjä: kapasiteettirajoitettu, ei silmukkaa. Domain: kestävä ja siirrettävä, mutta arvo riippuu jakelusta |
| raha → omistus | Microns: 1 000 € ≈ 200 USD vuosituloa | **Ei.** 20 %:n tuotto ilman moottoria |
| raha → pääsy | HILMA-avain, rekisterien maksulliset rajapinnat, Procountor-API | Kyllä, jos pääsy tuottaa ei-julkista dataa. Muuten kulu |
| raha → jakelu | mainonta | Ei ilman tuotetta, joka pitää käyttäjät. Ostettu huomio ei kasaudu |
| raha → kapasiteetti | laskenta, GPU | Vain jos kapasiteetti muuttuu dataksi tai näytöksi |
| raha → nopeus | rekisteröinnit, aikaisuus | Vanhenee. Superteam: uutuus ei suojaa, kun osallistuminen on ilmaista. Suojaa vain, jos aikaisin hankittu asia on kestävä oikeus |
| raha → luottamus | vakuutus, escrow, kehittäjätilin ikä ja badge (5 USD + kuukaudet), yritys | Halpa ja portittava, mutta ihmisen kuluttama (§2). Käynnistää silmukan vain yhdessä näytön kanssa |
| raha → optio | protokollan ennakkorekisteröinti, koeasetelma | Pieni, mutta tekee näytöstä uskottavan |

**Johtopäätös:** takaisinkytkennän voi käynnistää vain raha → näyttö ja raha → data, ja
nekin vain, jos tulos on julkinen, ennalta lukittu ja ei-kopioitava. Kaikki muut
transformaatiot ovat kulutusta tai kontin ostamista ilman moottoria. Tämä vastaa GPT:n
kantaa: rahaa ei käytetä siksi, että budjetti on olemassa.

## 6. 10M-rakennetesti

Ei pisteytystä. Jokainen kysymys joko läpäistään, tapetaan tai jää UNKNOWN. Yksi
"tappaa" riittää. Kolme UNKNOWNia peräkkäin tarkoittaa, ettei löydöstä voi arvioida,
vaan ensin mitataan. Järjestys on tappojärjestys: halvimmat tappajat ensin.

| # | Kysymys | Läpäisee | Tappaa |
|---|---|---|---|
| 1 | **BASELINE** Voittaako ratkaisu käyttäjän halvimman *hänen rajoitteillaan* hyväksyttävän vaihtoehdon, myös hänen oman tekoälynsä ja ilmaisen julkisen baselinen? | Nimetty vaihtoehto, nimetty rajoite, jota se ei täytä ja me täytämme | Vaihtoehto on "älä tee mitään" ja se toimii; tai etu on vain mallin käyttötaito |
| 2 | **CAPTURE** Mikä oikeus antaa meille osuuden, ja siirtyykö osuus meille vai asiakkaalle kokemuksen karttuessa? | Sopimus, laki, omistus tai asema, ja S, joka ei siirry asiakkaalle | Osuus perustuu siihen, että teimme työn; tai asiakas sisäistää menetelmän |
| 3 | **HUMAN** Laskeeko ihmistyö per hyväksytty yksikkö koon kasvaessa, tai voiko lisäihmisen ostaa katteesta menettämättä kaappausta? | h(N+1) < h(N) tai kate > palkka ja kaappaus ei nojaa henkilöön | Jokainen yksikkö vaatii saman ihmisen saman määrän (allekirjoitus, merge) |
| 4 | **SCARCITY** Mikä estää saman edun välittömän kopioinnin, ja näyttääkö meidän toimintamme jo tunnetulta väärinkäytöltä? | Ei-julkinen S, oikeus tai asema; toiminta on julkista ja todennettavaa | Etu on kehote, skripti tai julkinen data; tai profiilimme on uhkaprofiili (7) |
| 5 | **STATE** Mitä onnistumisesta jää (§2 P1 - P5)? | Nimetty S, joka on pysyvä, koneen tai yleisön kuluttama, siirrettävä, laillisesti käytettävä, ei-kopioitava | Jää vain raha, referenssi tai maine allekirjoituksena |
| 6 | **FEEDBACK** Onko kierros N+1 -testi suunniteltu, ja onko vastafaktuaali (sama tekoäly ilman S:ää) mahdollinen? | Mittari ja A/B nimetty ennen ajoa | Kasautuminen on tarina, jota ei voi mitata |
| 7 | **VALUE** Syntyykö todellista arvoa, jonka joku nimetty maksaa, eikä vain säästöä, joka jää asiakkaalle? | Nimetty maksaja ja budjettiperuste | Maksaja on "markkina" tai tukiraha, joka loppuu (1, 14) |
| 8 | **CAPITAL** Vaatiiko kasvu enemmän pääomaa kuin mekanismi tuottaa? | Kasvu rahoittuu kassavirrasta tai ei vaadi pääomaa | Jokainen askel vaatii ostoa, vakuutta tai varastoa (12, luontohyvitykset) |
| 9 | **CEILING** Mikä lopulta pysäyttää, ja missä on kontti, josta arvo lunastetaan? | Katto on markkinan koko, ei ihminen; kontti (yritys, alusta, oikeusportfolio) nimetty | Katto on yhden ihmisen tunnit tai allekirjoitukset; konttia ei ole |
| 10 | **FALSIFIER** Mikä yksi havainto tappaisi tämän nopeasti ja halvalla? | Nimetty, alle viikossa mitattava | Ei nimettävissä |

Lisäys, jota tehtävänanto ei pyytänyt mutta data vaatii: **EV.** Onko tulos toistettava
odotusarvo vai häntäveto? Tappaa: mekanismi tuottaa 10 M€ vain, jos yksi epätodennäköinen
tapahtuma toteutuu. Tämä erottaa vivun arpajaisista (§8).

## 7. Testi vanhoilla löydöksillä

| Tapaus | Ensimmäinen tappaja | Kommentti |
|---|---|---|
| Superteamin agenttikaista | SCARCITY (116 agenttia, sama malli), sitten CAPTURE | Läpäisee VALUE:n hetkellisesti (tukiraha). Testi tappaa oikein ja nopeasti |
| Orpo ohjelmisto (haltuunotto) | CAPTURE (käyttäjät eivät maksa), SCARCITY (uhkaprofiili) | STATE olisi jakelu, mutta hakemisto omistaa sen. Oikein |
| Maksujen jälkitarkastus pk-yrityksille | BASELINE UNKNOWN (asiakkaan oma tekoäly, kirjanpito-ohjelma), CAPTURE dynaaminen (osuus siirtyy asiakkaalle) | Ei tapa, ei läpäise: kolme UNKNOWNia (baseline, virhetaso, käyttöoikeus dataan). Ensin mittaus. Oikein |
| Julkiset hankinnat | HUMAN (toimitus on omaa työtä), CAPTURE (kumppani ohittaa) | Tappaa, ellei toimitus ole tuote. Oikein |
| Reservikapasiteetti | CAPTURE (integraation omistaja), CAPITAL (vakuudet, 0,1 - 1 MW) | Tappaa välittäjäversion. Oikein |
| Auktorisoitu kääntäjä | HUMAN (allekirjoitus per sivu), CEILING (yksi ihminen) | Läpäisee BASELINE, CAPTURE, SCARCITY, VALUE. Tappaa HUMAN:issa. Oikein: hyvä palvelu, ei kone |
| **HeroDevs-tyyppinen jatkajapalvelu** | HUMAN: ihminen kantaa vastuun per projekti | **Järjetön tulos.** HeroDevs on 125 M USD:n yhtiö, jossa ihmiset kantavat vastuun. Testi tappaisi sen |

**Korjaus testiin HeroDevs-tapauksen takia.** Alkuperäinen HUMAN-kysymys oli "kasvaako
ihmistyö lineaarisesti". HeroDevsissä kasvaa, ja silti perustajille syntyi suuri tulos.
Miksi: (a) kate riittää ostamaan lisäihmisen (compliance-hinta), (b) kaappaus ei nojaa
yhteen henkilöön vaan brändiin ja sopimuksiin, (c) kontti (yritys) muuttaa lineaarisen
liikevaihdon epälineaariseksi omistajan arvoksi kertoimen kautta. Siksi HUMAN-kysymys on
taulukossa jo korjatussa muodossa ("tai voiko lisäihmisen ostaa katteesta menettämättä
kaappausta") ja CEILING kysyy konttia. **Teorian rajaus:** "yksi ihminen" on projektin
lähtötila, ei mekanismin ehto. Mekanismi saa kasvaa palkkaamalla, kunhan kate ja
kaappaus kestävät sen. Se, mitä yksi ihminen ei saa olla, on jokaisen yksikön
allekirjoittaja.

Korjattu testi antaa jatkajapalvelulle: BASELINE läpäisee (fork ei ole compliance-
hyväksyttävä), CAPTURE läpäisee sopimuksella, HUMAN läpäisee vain katteella, SCARCITY
läpäisee siunauksella (ei-kopioitava), STATE = siunaus + asiakassopimukset + brändi,
FEEDBACK UNKNOWN meille, CAPITAL läpäisee, CEILING = EOL-ohjelmistojen määrä, kontti =
yritys. Eli: kone on olemassa, mutta se on rakennettu, eikä meillä ole sen siunausta.

## 8. Teorian tuhoamisyritys

Etsin mekanismeja, jotka ovat kasvaneet erittäin suuriksi mutta rikkovat ehtoja.

**8a. Häntävedot: arpajaiset, varhainen krypto, meemiosakkeet.** Rikkovat VALUE:n,
STATE:n ja FEEDBACK:in ja ovat silti historiallisesti *yleisin* tapa, jolla 1 000 € on
muuttunut 10 M€:ksi. Teoria ei kata niitä, ja se on tunnustettava: **johdetut ehdot
kuvaavat toistettavaa vipua, eivät onnea.** Toistettava vipu on todennäköisesti hitaampi
kuin onnekas veto. Se ei tee teoriaa vääräksi, mutta se tekee siitä rehellisemmän: emme
etsi nopeinta polkua 10 M€:oon, vaan polkua, jonka odotusarvo on positiivinen. Lisätty
kysymys EV testiin.

**8b. Sisällöntuottaja, jolla on yleisö.** Tekee videoita lineaarisesti, tulot kasvavat
epälineaarisesti yleisön mukana. Rikkooko HUMAN:in? Ei: yleisö kuluttaa maineen, ei
tuottaja (§2, maine yleisönä). Mutta se rikkoi *alkuperäisen* niukkuuskarttani, jossa
"todennettu historia ja luottamus" oli yksi rivi. Maine allekirjoituksena ja maine
yleisönä ovat eri koneet. Korjattu §2:een. Tämä vahvistaa yleisösilmukan: tämän
projektin julkinen loki on ainoa aineiston asia, jonka kuluttaa yleisö eikä me.

**8c. Avoimen lähdekoodin perustajat (Redis, MongoDB, WordPress itse).** Tuottivat arvoa
ilmaiseksi vuosia, CAPTURE oli nolla. Alkuperäinen CAPTURE-kysymys ("mikä oikeus antaa
osuuden nyt") olisi tappanut ne vuonna 1. Ne kasvoivat, koska S (käyttäjät, jakelu,
brändi) oli kestävä ja siirrettävä, ja kontti rakennettiin myöhemmin. **Korjaus:**
CAPTURE hyväksyy viivästetyn kaappauksen, jos S täyttää P1 - P5 ja kontti on uskottavasti
rakennettavissa. Tämä on tärkeä tälle projektille: julkinen loki ja skannerit ovat
viivästettyä kaappausta, ja niiden S pitää arvioida P1 - P5:llä, ei tuloilla.

**8d. Domainien ja oikeuksien varhaiset ostajat.** Ostivat halvalla ennen uudelleen-
hinnoittelua. Rikkooko "aikaisuus vanhenee"? Ei: aikaisuus toimi, koska hankittu asia
oli kestävä ja siirrettävä oikeus (domain), ei profiili. Täsmennys §2:een tehty. Mutta se
on osin häntäveto (8a): tuotto riippui uudelleenhinnoittelusta, jota ei voinut tietää.

**8e. Alustat ja aggregaattorit.** Sopivat malliin 1e. Eivät riko teoriaa, mutta
osoittavat, ettei aineistossamme ole yhtään tapausta, jossa olisimme solmu.

**8f. Vipu toisten pääomalla (rahastot, delegoitu pääoma).** Suurin historiallinen vipu,
hylätty päivänä 1 luvanvaraisena. Rikkoo CAPITAL-kysymyksen oletuksen, että pääoma on
meidän: pääoma voi olla lainattua, jos oikeus (lupa) siihen on. Se palauttaa asian
§3:een: lupa on portti, jonka baseline ei laske. Teoria kattaa sen, mutta projekti ei
mene sinne.

**8g. Petos, sybil, pyramidit.** Kasvavat suuriksi, rikkovat laillisuuden. Rajattu ulos
lähtökohtaisesti, ja niiden olemassaolo selittää §4:n havainnon: ne ovat kaappausta ilman
tuottamista, ja siksi ne tuhoavat luottamuksen, jota me tarvitsemme (tapaus 7).

**Tuhoamisyrityksen tulos:** teoria selvisi kolmella korjauksella (EV, maine yleisönä,
viivästetty kaappaus) ja yhdellä tunnustuksella (toistettava vipu on hitaampi kuin onni).
Yksikään suureksi kasvanut laillinen, toistettava mekanismi ei rikkonut korjattua
ehtojoukkoa. Se ei todista teoriaa oikeaksi. Se todistaa, ettei aineisto vielä kumoa sitä.

## 9. Vastaukset kolmeen kysymykseen

### 9.1 Mitä ominaisuuksia erittäin suureksi kasvavan mekanismin täytyy sisältää?

Evidenssin perusteella (INFERENCE, ei todistus) välttämättömiä tai lähes välttämättömiä:

1. **Etu nojaa johonkin, jonka baseline ei laske mallien parantuessa:** laki, vastuu,
   oikeus, pääsy tai yleisö. Ei mallin käyttötaitoon.
2. **Kaappausoikeus:** sopimus, laki, omistus tai asema, joka ei siirry asiakkaalle
   kokemuksen mukana. Viivästetty kaappaus sallittu, jos S on kestävä.
3. **Koneen tai yleisön kuluttama säilyvä tila** (P1 - P5), joka laskee seuraavan
   yksikön ihmistyötä tai nostaa osuutta. Ihmisen kuluttama tila tuottaa palvelun.
4. **Kontti**, josta arvo lunastetaan: yritys, alusta tai oikeusportfolio.
5. **Positiivinen odotusarvo toistettavasti**, ei häntäveto.
6. **Ei uhkaprofiilia:** toiminta on julkista ja todennettavaa, koska halvan tekoälyn
   maailmassa epäluulo on oletus.

Kaikki kuusi täyttyvät aineistossa vain muiden rakentamissa koneissa (HeroDevs,
hakemistot, alustat). Meidän tapauksistamme yksikään ei täytä kohtaa 3 mitatusti.

### 9.2 Mitkä ominaisuudet näyttivät tärkeiltä mutta eivät ole?

- **"Tekoälyn pitää tehdä jotain ihmiselle mahdotonta"** (PROSESSI, kysymys 4). Ei.
  Tekoälyn kyky on kaikilla. Etu on hyväksyttävyysehdoissa ja tilassa, ei kyvyssä.
  Tämä muutetaan prosessiin.
- **Uutuus ja aikaisuus.** Suojaa vain, kun osallistuminen maksaa ihmisen aikaa tai
  hankittu asia on kestävä oikeus. Agenttimarkkinoilla ei suojaa lainkaan.
- **Potin koko, latausten määrä, tähdet, käyttäjämäärä.** Kaikki osoittautuivat
  välillisiksi mittareiksi, jotka eivät kerro maksajasta eivätkä kaappauksesta.
- **Referenssi ja maine allekirjoituksena.** Parantavat myyntiä, eivät konetta.
- **Ylläpidon halpeneminen.** Omistajan kustannus ei ollut ylläpito vaan vastuu.
- **90 päivän tuplaus.** Mittaa palvelua, ei konetta. Säilyy vain rehellisyys-
  tarkistuksena.
- **Pisteytys summana.** Peittää tappavan portin (GPT). Rakennetesti ensin, pisteet
  vasta läpäisseille.
- **Pääoma pullonkaulana.** 1 000 € ei ole rajoite missään aineiston tapauksessa;
  rajoite on S:n puute.

### 9.3 Millä testillä seuraava löydös tapetaan tai päästetään jatkoon?

§6:n rakennetesti tappojärjestyksessä: BASELINE → CAPTURE → HUMAN → SCARCITY → STATE →
FEEDBACK → VALUE → CAPITAL → CEILING → FALSIFIER → EV. Yksi tappo riittää. Kolme UNKNOWNia
peräkkäin tarkoittaa mittausta ennen arviointia. Läpäissyt löydös saa vasta sitten
kortin ja pisteet.

## 10. Mikä evidenssi puuttuu, jotta teoria olisi enemmän kuin päättely

Teoria voidaan johtaa, mutta sen ydinehto (kohta 3, koneen kuluttama S laskee N+1:n
ihmistyötä) on **mittaamaton kaikissa omissa tapauksissamme.** Puuttuu:

1. Yksi kierros N → N+1 -mittaus vastafaktuaalilla. GPT:n esikoe näytti, ettei julkisesta
   PyPI-otoksesta löytynyt toistuvaa virheluokkaa, joten aineisto pitää valita
   dokumentoidun rikkoutuneen käyttöpolun mukaan, ei iän. Kandidaatti: WordPressin
   "tested up to" -perhe, jos siitä löytyy kaksi riippumatonta rikkoutunutta lisäosaa.
2. Yksi mitattu baseline oikealta asiakkaalta: mikä hänen halvin hyväksyttävä
   vaihtoehtonsa on ja mitä se maksaa hänelle. Vaatii omistajan luvan yhteydenottoon.
3. Yksi mitattu kaappauksen dynamiikka: siirtyykö osuus ajan myötä meille vai
   asiakkaalle. Vaatii kaksi toimitusta samalle asiakkaalle.
4. Yleisösilmukan ensimmäinen mittaus: onko tällä lokilla lukijoita ja tuottaako se
   yhteydenoton. Nolla euroa, mutta vaatii julkaisun, joka on omistajan päätös.

Ilman kohtaa 1 teoria on johdonmukainen kuvaus muiden koneista. Kohta 1 on ainoa, jonka
voi tehdä ilman lupaa, ja se on seuraavan kierroksen ensimmäinen tehtävä.
