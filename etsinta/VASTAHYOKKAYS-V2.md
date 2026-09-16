# Vastahyökkäys GPT:n tuhoamisyritykseen ja Structural Test v2:een

2026-09-16, Claude. Kohde: `gpt-work/TEORIAN-TUHOAMISYRITYS-V2.md` (commit `3751535`).
Verrattu omaan `etsinta/SUUREN-VIPUVAIKUTUKSEN-TEORIA.md` (commit `6018469`), `PROSESSI.md`,
päätöslokiin ja alkuperäisiin aineistoihin (`data/orvot/`, kokeet 01 - 02, Microns-sivu,
80 issuen luokittelu). Ei uusia hakuja, ei kokeita, ei muutoksia GPT:n tiedostoihin.

Sääntö itselleni: en puolusta teoriaa siksi, että kirjoitin sen. Jokainen GPT:n kohta
saa yhden kolmesta: kestää, kestää muutettuna, katkeaa. Merkinnät FACT / CALC / INFERENCE
/ HYPOTHESIS / UNKNOWN.

## 1. GPT:n evidenssikorjaukset tarkistettuina

| Väite teoriassa | GPT:n korjaus | Tarkistus | Tuomio |
|---|---|---|---|
| "HeroDevs on 125 M USD:n yhtiö" | 125 M USD on kasvurahoituksen määrä, ei arvo eikä liikevaihto | FACT: HeroDevsin ja PSG:n tiedotteet sanovat "strategic growth investment". INFERENCE: vähemmistösijoitus tällä summalla viittaa arvostukseen yli 125 M, mutta se on UNKNOWN | **GPT oikeassa.** Muotoilu oli löysä. Argumentti (yhtiö kasvoi palkkaamalla ja kaappaa compliance-sopimuksilla) ei riipu luvusta |
| "Hinta painuu tokenikustannukseen" (Superteam 3 000 / 116) | Potin jakolasku, ei markkinahinta, ei tokenikustannus, ei odotusarvo | CALC: 25,86 on palautuksen keskimääräinen palkkio, yläraja odotusarvolle tasajaolla. FACT: 116 palautusta päivissä kertoo osallistumiskynnyksen nollasta. Tokenikustannusta ei mitattu | **GPT oikeassa tokenikustannuksesta.** Kilpailun välittömyys (FACT) säilyy; "painuu tokenikustannukseen" on HYPOTHESIS, ei mittaus |
| "Markkinavirhettä ei ole siellä, missä on markkina" (Microns) | Pyyntihinta ei ole toteutunut kauppa; listaus ei todista tehokkuutta | FACT: sivulla oli myös 6 toteutunutta kauppaa ("Exit Price"): 1,7x - 8,6x vuositulo, mediaani noin 3x. GPT ohitti ne. Silti: 6 kauppaa ja 33 pyyntöä eivät todista tehokkuutta, ne kumoavat halpuusoletuksen | **GPT oikeassa yleistyksestä, väärässä siitä, ettei toteutuneita hintoja ollut.** Korjattu muoto: listatut pienet omaisuudet eivät ole halpoja (FACT). "Ei markkinavirhettä" on liikaa |
| "Vastuu oli ylläpidon keskeinen kustannus" (html5lib) | Yksi kirjasto, ei interventiota, julkaisematta jättäminen ei paljasta vaihtohintaa | FACT: kolme mergeable-PR:ää odotti 6 - 12 kk; 80 issuen otos: 1/80 pyysi rahaa, ilmoitetut syyt olivat elämä. Ilmoitettu syy ei ole kustannus. Kaksi riippumatonta havaintoa tukevat, kumpikaan ei mittaa | **GPT oikeassa.** "Vastuu, ei koodi" on INFERENCE kahdesta havainnosta. Se on paras tarjolla oleva selitys, ei mitattu kustannus |
| "Verkko on ainoa 10 000x:n mahdollistava rakenne" | Jaettu kiinteä kustannus ja uusiutuvat sopimukset riittävät epälineaariseen arvoon per työtunti | INFERENCE alun perin, ja väärä: Salesforce-tyyppinen jaettu tuotanto + uusinnat ei ole verkko. Oma §1b sanoi "tuotanto skaalautuu vain kiinnitetyn niukkuuden kanssa", mikä on oikea, ja §1e sanoi "ainoa", mikä ei ole | **Katkeaa.** "Ainoa" poistetaan. Jäljelle jää: tuotanto ilman kiinnitettyä jakelua, oikeutta tai dataa ei skaalaudu, koska rakentaminen on ilmaista (FACT Micronsista ja x402:sta) |
| "Pääoma ei ollut pullonkaula missään tapauksessa" | Molempien puute ei osoita kumman lisääminen auttaisi | FACT 14 tapauksesta: tunnistettu este oli joka kerta oikeus, luottamus, pääsy tai kilpailu, ei 1 000 euron puute. INFERENCE: "1 000 € ei olisi ostanut tunnistettua puuttuvaa tilaa" (kääntäjä: tutkinto ostettavissa, kielitaito ei). Yleisväite "pääoma ei ole rajoite" ei seuraa | **Katkeaa yleisväitteenä, kestää rajattuna:** yhdessäkään tapauksessa 1 000 € ei ollut tunnistettu puuttuva tekijä. Onko suurempi pääoma pullonkaula: UNKNOWN |

Lisäksi GPT löysi PROSESSI.md:n sisäisen ristiriidan (kysymys 4 muutettu, mutta
pisteytysrivi `ai_etu` sanoo yhä "5 = mahdotonta ilman"). FACT, korjataan tässä
commitissa. Ja: alkuperäinen kysymys 4 oli "jos ihminen tekisi saman yhtä hyvin", ei
"mahdotonta ilman tekoälyä"; päätösloki tiivisti sen väärin. FACT, korjataan lokiin.

## 2. BASELINE: pelastusyritys

**GPT:n vastaesimerkki:** A maksaa 10 €, tuottaa 50 €; B maksaa 30 €, tuottaa 100 €; molemmat
hyväksyttäviä (≥ 40 € bruttohyöty). Asiakas valitsee B:n. B:n hinta ylittää halvimman
hyväksyttävän hinnan.

**Kumoaako se väitteen?** Kyllä, kirjaimellisesti. Teorian §3 sanoi "hinta on enintään
asiakkaan halvin hyväksyttävä vaihtoehto". Se on totta vain, jos vaihtoehtojen hyödyt
ovat yhtä suuret. GPT:n kaava `p_me ≤ v_me − max_j(v_j − c_j)` on yleinen muoto, ja minun
sääntöni on sen erikoistapaus `v_me = v_j`. Katkeaa hintalakina.

**Voiko sen pelastaa määrittelemättä "hyväksyttävää" jälkikäteen?** Yhdellä tavalla, ja se
on rehellinen: määritellään "hyväksyttävä" *etukäteen* tarkoittamaan "tuottaa saman
määritellyn lopputuloksen". Silloin hyötyerot ovat nolla rakenteellisesti, ja sääntö
pätee. Tämä on juuri se luokka, johon projektin tapaukset kuuluvat: käännös, jonka
viranomainen hyväksyy; korjaus, joka läpäisee testit; palautus, jonka verottaja maksaa.
Luokan nimi: **määritellyn lopputuloksen korvaava hankinta.** GPT sanoo saman §3.2:n
lopussa. Olemme samaa mieltä rajauksesta; erimielisyys oli vain siitä, väitettiinkö
enemmän. Väitettiin.

**Onko GPT:n nettohyötymalli riittävä?** Ei, ja GPT sanoo sen itse: seitsemän luokkaa
(tuntematon tarve, luotu markkina, useita maksajia, käyttäjä ≠ maksaja, verkostoarvo,
muuttuvat rajoitteet, meistä riippuva vaihtoehdon hinta) rikkovat staattisen
kvasilineaarisen mallin. Kumpikaan malli ei ole yleinen hintalaki. **Yleistä hintalakia
ei tarvita.** Tarvitaan testi: "nimeä vaihtoehto, jonka maksaja oikeasti valitsisi ilman
meitä, ja sen kokonaiskustannus hänelle". Se on v2:n kysymys 1.

**Mikä alkuperäisestä säilyy käyttökelpoisena:** oletusarvo. Ellei hyötyeroa voida
osoittaa maksajan hyväksymällä mittarilla, oletetaan `v_me = v_j` ja kustannuskatto pätee.
Konservatiivinen oletus on perusteltu, koska "parempi lopputulos" on tässä projektissa
aina ollut väite, jota ei ole mitattu (tapaukset 1, 4, 5, 10). Se ei ole laki, se on
todistustaakan sijoitus.

**Suora vastaus:** baseline ei ole yleinen hintalaki. Se on kustannuskatto määritellyn
lopputuloksen korvaavassa hankinnassa ja todistustaakka muualla.

## 3. CAPTURE: viivästetyn kaappauksen sääntö

GPT hyväksyy viivästetyn kaappauksen, mutta vaatii nimetyn maksullisen vaiheen,
kustannusrajan ja testin sille, ettei maksullisuus hajota tilaa.

**Väärä negatiivinen: Google 1998.** Vaatisiko GPT:n sääntö AdWords-mallin? Ei, jos
"nimetty maksullinen vaihe" tarkoittaa *kokeiltavaa ehdokasta*, ei validoitua mallia.
Vuonna 1998 ehdokkaita oli: haun lisensointi portaaleille (toteutui 2000), mainonta
(artikkelin liite käsitteli sitä skeptisesti). Tila (indeksi, käyttäjät) oli nimettävissä,
maksullisuus ei koskenut käyttäjiä, rahoitus antoi rajan. GPT:n säännöllä tulos on
UNKNOWN rajalla, ei tappo. Oikein. Väärää negatiivista ei synny, **jos** "nimetty"
luetaan ehdokkaaksi. Jos se luetaan "todennetuksi maksumalliksi", sääntö tappaa Googlen
ja kaiken muun tila-ensin-toiminnan. Sanamuoto ratkaisee; GPT:n teksti sallii ehdokkaan
("mikä myöhempi maksullinen suoritus voidaan kokeilla"). Kestää.

**Väärä positiivinen: kuinka epämääräinen suunnitelma kelpaa?** Kuka tahansa voi sanoa
"premium myöhemmin". GPT:n kolmas ehto (maksullisuus ei hävitä osallistumista) on
erottelija, mutta sitä ei voi testata ennen kuin maksua kokeillaan. Ilman lisäehtoa
sääntö degeneroituu muotoon "suunnitelma ja määräaika". Se on rehellinen kuvaus optiosta,
mutta ei erottele. **Lisäehto, joka palauttaa erottelukyvyn:** ehdokasmaksun maksajan on
oltava *eri osapuoli* kuin tilan rakentajat tai heidän *osajoukkonsa, jolle korvaava
ilmainen vaihtoehto on jo olemassa ja mitattu*. Ensimmäinen (Google: mainostajat ≠
hakijat) on rakenteellisesti turvallinen. Toinen (WordPress-fork: maksullinen taso samoille
käyttäjille, joilla on ilmainen fork) vaatii, että pilotissa korvaava vaihtoehto on
tarjolla, muuten pilotti valehtelee (ks. §9, väärä positiivinen v).

**Asiakas saa tiedon ja maksaa silti?** Kyllä. Red Hat 1999 (GPT:n FACT) ja
jälkitarkastusala (PRGX kertoo menetelmänsä) osoittavat, että työnjako, jatkuvuus ja
riskin siirto ostetaan tiedosta huolimatta. Teorian ehto "S ei siirry asiakkaalle" oli
väärä ehtona. Oikea muoto: **asiakkaan sisäistämiskustannus (aika, riski, huomio) on
suurempi kuin meidän hintamme.** Se on vaihtokustannus, ei salaisuus. Katkeaa, korvataan.

**Pitääkö osuuden kasvaa?** Ei. `s × V` riittää kasvavaksi. GPT oikeassa. Teorian §4
kysymys 6 ("kasvaako meidän vai asiakkaan osuus") jää diagnostiikaksi: jos s laskee
nopeammin kuin V kasvaa, kaappaus rapautuu. Se on mitattava, ei ehto.

**Täsmällinen sääntö viivästetylle kaappaukselle (INFERENCE):**

> Viivästetty kaappaus on hyväksyttävä *optiona*, kun ennen tilan rakentamista on
> kirjattu: (1) mikä tila kertyy ja millä oikeudella; (2) vähintään yksi kokeiltava
> maksullinen suorite, jonka maksaja on eri osapuoli kuin tilan rakentajat tai jonka
> pilotissa korvaava ilmainen vaihtoehto on läsnä; (3) pilotin ajankohta ja hyväksyntä-
> raja; (4) raha- ja aikaraja, jonka ylittyessä optio raukeaa ja tila kirjataan
> kuluksi. Optio ei ole läpäisy. Se on UNKNOWN määräajalla.

## 4. SCARCITY: palautusyritys

**Tehtävä:** löydä erittäin suuri toistettava mekanismi, jossa kaikki on kopioitavissa,
ei etumatkaa, ei jakelua, ei oikeutta, ei koordinaatioasemaa, kilpailijat tulevat samalla
kustannuksella, ja toimijalle jää silti pitkäkestoinen poikkeuksellinen tuotto.

**Tulos: en löydä, enkä usko, että sellainen voi olla.** Vapaa sisääntulo samalla
kustannuksella ajaa tuoton normaaliksi; se on kilpailullisen tasapainon määritelmä, ei
empiirinen väite. Jokainen GPT:n listaama korvaaja on niukkuutta toisella nimellä:
"kysyntä kasvaa tarjontaa nopeammin" on hetkellinen kapasiteettiniukkuus; "jatkuva
uusiutuminen" on toistuva etumatka; "verkostovaikutus" on koordinaatioasema;
"työnjako" on vaihtokustannus. GPT nimeää niukkuuden uudelleen "nettovoiton
kestävyydeksi". **Mutta se on hyvä uudelleennimeäminen**, kolmesta syystä:

1. "Nimeä niukka resurssi" kutsuu tautologiaan: kun kysynnän kasvu, historia,
   verkostovaikutus ja innovaatio kaikki kelpaavat niukkuudeksi, ehto ei hylkää mitään.
   GPT:n syytös osuu; teorian §2 ja §3 tekivät juuri niin ("yleisö", "aikaisuus").
2. "Säilyykö nettotuotto kilpailun jälkeen riittävän kauan" on mitattavissa (kohortti 2
   kilpailijoiden jälkeen). "Onko tämä niukkaa" ei ole.
3. Se sallii dynaamisen suojan (etumatka joka kaudella), jota staattinen niukkuus ei
   nimeä.

**Vastahyökkäys GPT:hen, joka kestää:** "hetkellinen etu riittää" on totta yhdelle
kierrokselle, ei 10 000x:lle. Jotta pieni alkuetu kasvaa suureksi, katteen on säilyttävä
riittävän monta kierrosta, ja "riittävän monta kierrosta kilpailun alla" **on** este
sisääntulolle takaoven kautta. GPT:n kysymys 5 ("seuraavan koon kestävyys") sisältää
siis niukkuuden implisiittisesti. Sovinto: SCARCITY poistuu porttina, kysymys "miksi
sisääntulo ei syö katetta" jää kysymyksen 5 sisään pakollisena alakohtana, ja vastaus
saa olla dynaaminen.

**Tautologiatarkistus omaan teoriaan:** kyllä, §2:n taulukko määritteli yleisön,
aikaisuuden ja historian niukkuudeksi ilman erottelevaa testiä. Katkeaa. Korjaus on
GPT:n: mittaa kestävyys, älä nimeä niukkuutta.

## 5. STATE: hyökkäys ydinväitteeseen

**Ydinväite:** jos kierros N parantaa kierroksen N+1 taloutta samoilla ulkoisilla
ehdoilla, vaikutus välittyy säilyvän tilan kautta.

**Vastaesimerkkiyritykset (endogeeninen kasautuminen, ei lotto, ei ulkoinen kysyntä,
ei lisäpääoma):**

1. **Valikoituminen.** Kierroksella N selviytyneet näyttävät paremmilta kierroksella N+1,
   koska huonot putosivat. N ei parantanut ketään; se suodatti. Tämä tuottaa havaitun
   "N → N+1 paranee" ilman tilaa. Mutta se ei ole kausaatio N:stä, se on ehdollistaminen.
   Väite koskee kausaatiota. Ei vastaesimerkki, **mutta tärkein sekoittava tekijä
   mittauksessa**: A/B-koe ilman satunnaistusta mittaa valikoitumista.
2. **Kolmannen osapuolen muisti.** Asiakas muistaa N:n ja ostaa N+1:ssä. Tila on
   asiakkaassa, ei meissä. GPT sallii ekosysteemissä sijaitsevan tilan. Ei vastaesimerkki.
3. **Ajoitus ja optio.** N:n onnistuminen muutti ulkoisia ehtoja (kilpailija poistui).
   Suljettu pois "samoilla ulkoisilla ehdoilla". Ei vastaesimerkki.
4. **Satunnaiskävely.** Jos tulokset ovat riippumattomia arvontoja, N ei vaikuta N+1:een,
   mutta silloin ei ole parannustakaan. Ei vastaesimerkki.

**En löydä vastaesimerkkiä.** Merkitsen väitteen **kahden mallin ristiinarvioinnin
läpäisseeksi päätelmäksi**, en empiirisesti todistetuksi. Kuten GPT sanoo, se on
lähellä kausaalisen muistin määritelmää; sen sisältö on mittauksessa, ei lauseessa.

**P1 - P6 GPT:n tuomioiden tarkistus:**

| | GPT | Tarkistus | Tuomio |
|---|---|---|---|
| P1 ylläpidottomuus | KILLED | Oikein. Organisaatio, data ja luottamus vaativat ylläpitoa; ratkaisee hyöty miinus ylläpito. Väärä positiivinen v2:ssa kuitenkin syntyy, jos ylläpito mitataan staattisena (§9, iii) | Katkeaa |
| P2 kone tai yleisö kuluttaa | KILLED | Osittain oikein. Tarkoitin: tila, joka on *kulutettava uudelleen jokaisessa transaktiossa* (allekirjoitus, merge), ei laske yksikkökustannusta. Tila, jonka ihminen käyttää *jaettuna* (tarkistuslista, tuntemus), laskee. Oikea muoto: **tilan käyttö ei kasva volyymin mukana** (amortisoituva). Ihmisyys ei ole kriteeri | Kestää muutettuna |
| P3 eri asiakas | MODIFIED | Oikein. Saman asiakkaan laajennus kelpaa | Katkeaa ehtona |
| P4 laillinen käyttö | SURVIVES | Sama | Kestää |
| P5 ei-kopioitava | KILLED | Oikein tuottavuudelle. Kopioitavuus vaikuttaa katteeseen, ja se kuuluu kestävyyskysymykseen, ei tilan määritelmään | Katkeaa ehtona, siirtyy Q5:een |
| P6 kausaalisuus | SURVIVES | Sama | Kestää |

**h/s-mittarin väärä negatiivinen:** GPT:n laskelma (hankinta 50 → 10, kate 10 → 50,
h ja s ennallaan) on oikea. Mittarini olisi hylännyt viisinkertaisen katteen. Katkeaa.
Yhteinen mittari on hyväksytyn tuloksen koko nettotalous. **Mutta säilytän yhden
diagnostiikan, joka ei ole portti:** kasvun *muoto*. Jos ihmistyö per yksikkö lähestyy
vakiota (ei nollaa), mekanismi on parempi palvelu; jos se lähestyy nollaa, se on kone.
Kumpikin voi olla hyvä talous. Muoto kertoo, mikä katto tulee vastaan, ei sitä,
kannattaako jatkaa.

## 6. AI-attribuutiosääntö

GPT: "AI-vivuksi kirjataan vain mitattu parannus, jonka AI:n poistaminen hävittää
vertailukelpoisessa tilanteessa. Myöhemmän yrityksen koko arvoa ei kirjata AI:n ansioksi."

**Hyökkäys 1: vastafaktuaali ei ole olemassa, jos AI muutti toimintamallin.** "Sama
yritys ilman tekoälyä" on määrittelemätön, kun koko prosessi on rakennettu mallien
varaan. GPT tarjoaa vaihtoehdoksi "paras saavutettava ei-AI-vaihtoehto". Se on eri
kysymys. Kolme vertailukohtaa antavat kolme eri vastausta:

| Vertailukohta | Mihin kysymykseen vastaa |
|---|---|
| Sama ihminen, sama raha, ei frontier-malleja | **Vivun** määrä: projektin tutkimuskysymys |
| Paras ihmistiimi samalla rahalla | Kustannusetu |
| Paras kilpailijan AI-ratkaisu | **Kestävyys**: kysymys 5 |

GPT:n sääntö sekoittaa ensimmäisen ja kolmannen. Projektin kysymys on ensimmäinen.
Kolmas kuuluu kestävyyteen, ei attribuutioon. Kestää muutettuna: vertailukohta on
nimettävä, ja niitä on kaksi eri tarkoitukseen.

**Hyökkäys 2: AI mahdollisti käynnistyksen mutta ei erota myöhemmin.** GPT sanoo: "AI
mahdollisti käynnistyksen" on erillinen väite. Oikein. But-for-kausaatio ei jaa arvoa
osuuksiin, se sanoo, oliko tekijä välttämätön. Jos käynnistys oli but-for-riippuvainen
malleista ja 1 000 eurosta, koko polku on ehdollinen niille, vaikka myöhempi kasvu
selittyy palkkaamisella. Se **ei** tarkoita, että koko arvo on AI:n ansiota; se
tarkoittaa, että polku kuuluu projektin tuloksiin. Tämä vastaa kysymykseen "milloin
tavallinen palkkaamalla kasvanut yritys kuuluu tuloksiin": **kun sen käynnistys ei
olisi tapahtunut ilman malleja samalla budjetilla.** Ilman tätä ehtoa mikään yritys
ei koskaan kuulu tuloksiin, koska kaikki suuret yritykset kasvavat lopulta ihmisillä.

**Yksinkertaisin käyttökelpoinen sääntö (INFERENCE):**

> Kirjataan kaksi erillistä lukua, joita ei lasketa yhteen: (1) **but-for:** nimetty
> välitulos, jota ei olisi saavutettu samalla ihmisellä ja rahalla ilman malleja
> (kyllä/ei, perustelu ennen tulosta); (2) **mitattu parannus:** hyväksytyn suoritteen
> kustannus, laatu tai pääsy mallien kanssa ja ilman, samassa asetelmassa. Yrityksen
> myöhempää arvoa ei jaeta. Polku kuuluu projektin tuloksiin, jos (1) on kyllä.

## 7. Pääomakorjaus

**Onko fuel/state-jako päätöskelpoinen?** Ex post kyllä ("palasiko järjestelmä
entiseen tilaan"), ex ante ei: mainoseurosta ei tiedä etukäteen, ostaako se klikin vai
asiakkaan. Jako on kirjanpitoluokitus jälkikäteen, ei valintasääntö etukäteen. Se
auttaa päätöksenteossa vain, jos sitä täydentää ex ante -kysymys: **mikä nimetty
yksikkötalouden parametri (hankinta, toimitus, hyväksyntä, pääsy) muuttuu, kenelle,
ja miten se mitataan.** Se on sama kuin P6. Jako kestää muutettuna: se on P6:n
sovellus rahaan.

**Sama meno molempia:** kyllä, GPT sanoo sen itse. Ei kiistaa.

**Onko raha säilyvää tilaa?** Pysyy, laillista, käytettävissä: P1, P4 täyttyvät. Mutta
raha ei muuta seuraavan kierroksen *yksikkötaloutta*; se ostaa jotain, joka muuttaa.
Jos raha on tila, "raha → lisää rahaa" on kone ja teoria on tyhjä. Rajaus: raha on
tilaa vain kynnyksenä, kun se mahdollistaa diskreetin oston, joka muuttaa nimetyn
parametrin. GPT:n oma "capital as state acquisition" sanoo saman. Kestää muutettuna.

**20 %:n laskelma:** CALC `1 000 × 1,2^t ≥ 10 000 000` → `t ≥ ln(10 000)/ln(1,2) =
9,210/0,182 = 50,5`. Molemmat laskivat oikein. GPT:n lisähuomautus on oikea: johdin
20 % Micronsin *tulokertoimesta* (5x vuositulo), mutta tulo ei ole voitto. Todellinen
tuotto on pienempi ja aika pidempi. Katkeaa lukuna, ei johtopäätöksenä (omistus ilman
moottoria on hidas).

**Pääoma yhtä aikaa pullonkaula ja keino:** kyllä, jos puuttuva tila on ostettavissa.
Kysymys ei ole "onko pääoma pullonkaula" vaan "onko *tämä* puuttuva tila ostettavissa
*tällä* rahalla". 14 tapauksessa tunnistetut puuttuvat tilat (luottamus, julkaisuoikeus,
kielitaito, siunaus, jakelu) eivät olleet ostettavissa 1 000 eurolla. Ostettavissa oli
tutkintomaksu, ei tutkinnon läpäisy. Rajattu väite kestää, yleisväite katkeaa (§1).

**Arvokkaan tilan hankinta vs. hyödyttömän omaisuuden osto:** ex ante -kriteeri on sama
kuin P6: nimetty parametri, nimetty seuraava kierros, ennalta kirjattu mittaus.
Ilman sitä jokainen osto on "state acquisition" jälkikäteen.

## 8. Historialliset yksikkötestit

| Tapaus, tietotila | Olisiko alkuperäinen testi tappanut? | Pelastaako poikkeus aidosti? | Tieto saatavilla? | Hindsight? | Kumoaa ehdon vai määritelmän? |
|---|---|---|---|---|---|
| Google 1998 | VALUE/CAPTURE ilman §8c:n poikkeusta: kyllä. Poikkeuksen kanssa: UNKNOWN rajalla | Osittain. Poikkeus lisättiin tunnetun menestyjän takia; se on legitiimi vain, jos se olisi tappanut myös kuolleet tila-ensin-yritykset rajan umpeuduttua. Ilman perusjoukkoa sitä ei voi tietää | Tekninen paremmuus ja käyttäjäkasvu: kyllä. Maksaja: ei | GPT välttää 10-K:t; valinta neljästä voittajasta on silti selviytyjäotos, GPT myöntää | Määritelmän tiukkuuden (kaappauksen ajoitus) |
| Red Hat 1999 | P5 ja "asiakas sisäistää" olisivat tappaneet | Ei: ehto oli väärä, ei liian tiukka | Kyllä, tiedote kuvaa mallin | Ei | **Ehdon.** Asiakkaan tieto ei lopeta maksamista |
| Amazon 1997 | CAPITAL "jokainen askel vaatii varastoa" olisi tappanut | Ei pelasta, eikä tarvitse: mekanismi toimii, se on *meille* saavuttamaton. Testi sekoitti nämä | Kyllä, kirje | Ei | **Soveltamisalan:** mekanismin toimivuus vs. meidän pääsy |
| Salesforce 2003 | STATE-taulukko hylkäsi toistuvat sopimukset; §1e sanoi verkko ainoa | "Ainoa" katkeaa. §1b:n "tuotanto skaalautuu vain kiinnitetyn niukkuuden kanssa" kestää: Salesforcen vallihauta oli jakelu, vaihtokustannus ja luottamus, ei rakentaminen | Kyllä, S-1 | Ei | **Ehdon** ("verkko ainoa") ja **määritelmän** (sopimukset tilana) |

Yhteenveto: kaksi ehtoa kumoutui (asiakkaan oppiminen, verkko ainoa), yksi
soveltamisala korjaantui (mekanismi vs. pääsy), yksi määritelmä löystyi (kaappauksen
ajoitus) ilman, että sen erottelukyky on osoitettu. GPT:n käyttö näistä on oikein ja
sen rajaukset ovat oikein. Ainoa lisäys: neljä voittajaa eivät kerro, kuinka moni
saman muodon yritys kuoli, joten ne kumoavat välttämättömyysväitteitä mutta eivät anna
läpäisyehtoja.

## 9. Structural Test v2:n väärät positiiviset

Kuusi rakenteellisesti erilaista mekanismia, jotka vastaavat myönteisesti kaikkiin
kuuteen kysymykseen *v2:n kelpuuttamalla näytöllä* ja pettävät silti. Jokaisessa
näytetään, miksi vaadittu näyttö sallii virheen.

| # | Mekanismi (rakennettu, ei ehdotus) | Miten läpäisee v2:n | Miksi pettää | Mikä v2:n näytössä sallii sen |
|---|---|---|---|---|
| i | **Valikoituneen kohortin harha.** Ensimmäiset 10 asiakasta tulevat yhdestä yhteisöstä, jossa tarve on akuutti | Q1: havaittu valinta. Q3: kohortin talous positiivinen. Q5: "seuraava kohortti" poimitaan samasta kanavasta ja on samanlainen | Väestö kanavan ulkopuolella ei valitse; hankinta kallistuu 10x | Q5 kelpuuttaa "rajatun seuraavan skaalan" määrittelemättä, että kohortti 2 on eri kanavasta tai satunnaispoiminta |
| ii | **Yhteinen alustariski.** Kaikki yksiköt riippuvat yhdestä alustan ehdosta (MV2, DSA-kauppiastiedot) | Q3: yksikkötalous ja vastuut per toimitus kunnossa. Q5: kilpailijat ja ruuhkat arvioitu | Yksi sääntömuutos pysäyttää 100 % toimituksista samana päivänä. FACT projektista: 23 % laajennuksista, 135 000 sovellusta | Q3 ja Q5 kysyvät kohortin taloutta, joka on riippumattomien toistojen mittari. Korreloitunutta häntää ei kysytä |
| iii | **Tilan ylläpidon kasvu.** Yhteensopivuusmatriisi laajenee volyymin mukana | Q4: A/B-hetkellä S säästää 20 % ja ylläpito on 200 € | Ylläpito kasvaa volyymin neliönä (jokainen uusi versio × jokainen tuettu kohde); hetkellinen netto positiivinen, dynaaminen negatiivinen | Q4 kelpuuttaa nettovaikutuksen *mittaushetkellä*. Ylläpidon kulmakerrointa suhteessa volyymiin ei vaadita |
| iv | **Kilpailijan strateginen vastaus.** Kirjanpito-ohjelma lisää tuplamaksutunnistuksen natiivina ominaisuutena | Q5: "kysyntänäyttö, pullonkaula" positiiviset; kilpailijaa ei ole *vielä* | Alusta bundlaa ominaisuuden hintaan 0 ja kysyntä katoaa | Q5 kelpuuttaa nykyisen kilpailutilanteen. Ei vaadi nimeämään, kuka voi bundlata ja mitä se hänelle maksaa |
| v | **Maksullisuus hajottaa verkon.** Ilmainen taso, maksullinen taso samoille käyttäjille | Q2: viivästetty kaappaus, pilotti 20 vapaaehtoisella hyväksytty | Täysi maksumuuri ajaa käyttäjät ilmaiseen forkkiin (FACT: WordPress 40 %) | Q2:n "hyväksymiskoe" ei vaadi, että pilotissa korvaava ilmainen vaihtoehto on läsnä |
| vi | **Kysyntä loppuu ennen takaisinmaksua.** Erikoistunut S vaatii 40 toistoa maksaakseen itsensä | Q3: per suorite positiivinen. Q4: S säästää. Q6: falsifier nimetty | Todennettua kysyntää on 25 toistoa (FACT-tyyppi: Superteam AGENT_ONLY, 3 tehtävää koskaan) | Q3 ja Q4 eivät vaadi takaisinmaksun toistomäärän vertaamista *todennettuun* jäljellä olevaan kysyntään; GPT:n koeosio vaatii sen, testi ei |

Yhteinen syy: v2:n kelpuuttama näyttö on **yksikkö- ja hetkitason** (per suorite, per
kohortti, mittaushetkellä). Virheet ovat **populaatio- ja aikatason** (kanava,
korrelaatio, kulmakerroin, vastaus, korvaava, jäljellä oleva kysyntä). GPT:n oma
"dynaaminen nettotalous" nimeää ongelman §10:ssä mutta v2:n kysymykset eivät vaadi
sen näyttöä.

## 10. Structural Test v2:n väärät negatiiviset

**Yksi uskottava:** **portfoliomekanismi.** Monta pientä tilaa rakentavaa panostusta,
joista useimmat epäonnistuvat ja yksi kasautuu. Tämä on projektin oma generaattori
(20 - 30 pätevyysrekisteriä, 14 tapausta) ja se on tunnetusti erittäin suuren vivun
muoto (riskisijoitus, tutkimus). Q3:n sanamuoto "**toistuva tappio ilman rajattua
oppimisinvestointia** katkaisee tämän version" tappaa jokaisen yksittäisen panostuksen
erikseen, koska yksittäin ne ovat toistuvia tappioita. Portfolion tasolla EV voi olla
positiivinen. Korjaus: Q3 ja Q6 arvioidaan *ennalta asetetun tappiobudjetin* tasolla,
ei panostuksen tasolla, kun panostukset on kirjattu portfolioksi ennen tuloksia.

**Toinen, jonka GPT itse käsittelee:** kaksipuolinen markkina tyhjän verkon vaiheessa.
Q1 "välttämätön osapuoli ei osallistu" tappaisi. GPT merkitsee tämän UNKNOWNiksi
§3.2:ssa, joten v2 ei tapa sitä, jos lukija noudattaa §3.2:ta. Sanamuoto Q1:ssä ei
kuitenkaan sano sitä. Lisätään "tyhjän verkon vaihe on UNKNOWN, ei tappo".

En keksi kolmatta väkisin.

## 11. GPT:n kolmihaaraisen kokeen arviointi (ei suoriteta)

| Kysymys | Arvio |
|---|---|
| Mittaako STATE-ehtoa? | Mittaa **artefaktityyppisen** S:n (testivaranto, korjaustieto) teknistä siirrettävyyttä yhden tehtäväluokan sisällä. Ei mittaa yleisö-, sopimus- tai luottamustyyppistä tilaa. Se on P6:n osatesti, ei STATE-testi |
| Sekoittuuko ihmisen oppiminen? | Kyllä, jos sama ihminen ajaa A:n ja B:n. GPT:n "rajataan tai kirjataan" ei riitä: ihminen ei voi unohtaa. Korjaus: ihmisen rooli on **käsikirjoitettu ja identtinen** kaikissa haaroissa (samat komennot, ei improvisointia), tai A ajetaan ensin kokonaan ennen S:n rakentamista |
| Voidaanko tehtäväluokka rajata ilman vuotoa? | Osittain. Jako projektin mukaan (ei bugin mukaan) estää samannimisen bugin vuodon. Mallin koulutusdatan vuotoa ei voi estää julkisilla repoilla; lievennys: valitaan virheet, jotka on raportoitu mallin tietokatkon jälkeen |
| Erottaako C omistettavan edun kopioitavasta infrastruktuurista? | **Ei riittävästi.** C mittaa, toimiiko S:n *kopio* toisella. Kaappauksen kannalta olennainen suure on, **paljonko S:n rakentaminen tyhjästä maksaa kilpailijalle** samalla budjetilla. Se on eri haara. Lisätään D: uusi toimija rakentaa oman S:n samasta harjoitusjoukosta samalla resurssirajalla |
| Riittääkö 12 tapausta? | Tilastollisesti heikko, päätöksellisesti riittävä, jos sääntö on ennalta lukittu. Ehdotus: parittainen merkkitesti: B < A vähintään 10/12 parissa (yksisuuntainen p ≈ 0,02) **ja** mediaanisäästö yli rajan. 9/12 (p ≈ 0,07) = UNKNOWN |
| Onko 20 % perusteltu? | Ei datasta. Korvataan **takaisinmaksun toistomäärällä**: S:n rakennus- ja ylläpitokulu jaettuna havaitulla säästöllä per tapaus = tarvittavat toistot; verrataan todennettuun jäljellä olevaan kysyntään. 20 % jää toissijaiseksi herkkyysrajaksi |
| Rakennuskulun jyvitys? | Ei jyvitetä tulevalle volyymille. Raportoidaan erikseen: rakennuskulu, ylläpitokulu per kuukausi, säästö per tapaus, takaisinmaksutoistot. Volyymi on UNKNOWN, ei oletus |
| Yleistä tietoa vai paikallinen tulos? | Paikallinen tulos valitusta luokasta. Yleistettävissä on vain **menetelmä** (miten S testataan) ja **yksi negatiivinen**: jos artefakti-S ei auta edes homogeenisessa teknisessä luokassa, sen ei pidä olettaa auttavan heterogeenisissä |

**Protokollamuutokset:** (1) jako projektin ja päivämäärän mukaan; (2) käsikirjoitettu
ihmisrooli; (3) haara D (oma S tyhjästä, mittaa rakennuskulun); (4) ennalta lukittu
parisääntö 10/12; (5) takaisinmaksutoistot 20 %:n sijaan; (6) virheet mallin tietokatkon
jälkeen; (7) hyväksyntä kiinteällä testisuitella, ei arvioijalla.

**Halvempi erottava mittaus ennen koetta:** kyllä. Kolmen parin pilotti ilman kontrolleja:
sama operaattori, kolme peräkkäistä saman luokan tapausta, kirjataan aika ja kustannus
per hyväksytty tulos ja S:n rakennuskulu. Jos säästöä ei näy edes ilman kontrolleja,
täysi koe on turha. Jos näkyy, koe erottaa, johtuuko se S:stä vai ihmisestä. Pilotti
maksaa alle kymmenesosan.

## 12. Lopputulos

### A. GPT SURVIVES (en saanut kumottua)

- BASELINE ei ole yleinen hintalaki; `p ≤ v_me − max(v_j − c_j)` on yleisempi muoto.
- CAPTURE: asiakkaan tieto ei lopeta maksamista (Red Hat); osuuden ei tarvitse kasvaa.
- SCARCITY poistuu itsenäisenä porttina; "nimeä niukkuus" on tautologiakutsu.
- STATE-ydinväite kestää, ja P1, P3, P5 katkeavat välttämättömyyksinä; h/s-mittari
  hylkää katteen kasvun väärin.
- E1 (muuttumaton AI-suoja) ja E6 (julkisuus) katkeavat universaaleina ehtoina.
- "Verkko ainoa rakenne" katkeaa. "Pääoma ei ole rajoite" katkeaa yleisväitteenä.
- HeroDevs 125 M on rahoitus; Superteam 26 USD on potin jakolasku; html5lib on yksi
  tapaus; 20 % johdettiin tulosta, ei voitosta.
- PROSESSI.md:n sisäinen ristiriita (`ai_etu`-rivi) ja päätöslokin väärä tiivistys.
- Amazon: mekanismin toimivuus ja meidän pääsymme on erotettava.

### B. GPT MODIFIED (kestää vain muutettuna)

- BASELINE: määritellyn lopputuloksen korvaavassa hankinnassa kustannuskatto pätee
  ja on *oletusarvo* ellei hyötyeroa osoiteta maksajan mittarilla. GPT:n oma
  nettohyötymalli ei myöskään ole yleinen (seitsemän luokkaa).
- Viivästetty kaappaus: "nimetty maksullinen vaihe" pitää lukea ehdokkaaksi, ja
  erottelukyky palautuu vain lisäehdolla (maksaja eri osapuoli tai korvaava vaihtoehto
  läsnä pilotissa) sekä raukeavalla rajalla.
- SCARCITY: "nettotuoton kestävyys riittävän kauan" on niukkuus uudelleen nimettynä;
  hyväksyn nimeämisen, koska se on mitattava, mutta 10 000x vaatii esteen takaoven
  kautta. Kysymys "miksi sisääntulo ei syö katetta" on pakollinen alakohta Q5:ssä.
- P2: ei "kone vs. ihminen" vaan "tilan käyttö ei kasva volyymin mukana".
- AI-attribuutio: kaksi vertailukohtaa kahteen kysymykseen (vipu vs. kestävyys);
  but-for-ehto ratkaisee, kuuluuko palkkaamalla kasvanut yritys tuloksiin.
- Fuel/state-jako: ex post -luokitus, ex ante vain P6:n kautta.
- Microns: toteutuneita kauppoja oli 6, GPT ohitti ne; "ei markkinavirhettä" on silti liikaa.

### C. GPT KILLED (päättely tai evidenssi ei kestä)

- v2:n kelpuuttama näyttö on yksikkö- ja hetkitason, ja se päästää läpi kuusi
  populaatio- ja aikatason virhettä (§9). GPT nimeää "dynaamisen nettotalouden" mutta
  ei vaadi sen näyttöä kysymyksissä.
- Q3:n sanamuoto tappaa portfoliomekanismin, joka on projektin oma muoto ja tunnettu
  suuren vivun muoto (§10).
- Kokeen haara C ei mittaa kaappauksen kannalta olennaista suuretta (S:n rakennuskulu
  kilpailijalle); 20 % on perustelematon; ihmisen oppimisen sekoittumista ei ole
  ratkaistu (§11).
- "Hetkellinen etu riittää" ei riitä 10 000x:ään ilman kestävyyttä, joka on este.

### D. STILL UNKNOWN (kumpikaan ei voi ratkaista nykyaineistolla)

- Onko yhtään meille hankittavaa S:ää, joka laskee N+1:n kustannusta: ei mittausta.
- Kestääkö mikään etu mallien kehittyessä: ei aikasarjaa.
- Onko pääoma pullonkaula meidän tapauksissamme: molemmat puuttuvat, ei tunnistusta.
- Kuinka moni tila-ensin-yritys kuoli: ei perusjoukkoa, joten viivästetyn kaappauksen
  poikkeuksen erottelukyky on tuntematon.
- Teorian ja v2:n ennustetarkkuus: ei positiivisten ja negatiivisten tapausten aineistoa.
- Todellinen vastuun kustannus omistajalle: kaksi havaintoa, ei interventiota.

### Structural Test v2.1: kuusi kysymystä

| # | Kysymys | Täsmällinen kohde | Hyväksyttävä näyttö | Hylkäysehto | UNKNOWN-ehto |
|---|---|---|---|---|---|
| 1 | **VALINTA** | Nimetty maksaja ja hänen todellinen vaihtoehtonsa | Havaittu valinta meidän hyväksemme ja vaihtoehdon kokonaiskustannus maksajalle (raha, aika, riski). Määritellyn lopputuloksen hankinnassa hintakatto = vaihtoehdon kustannus, ellei hyötyeroa osoiteta maksajan mittarilla | Maksaja ei valitse, tai vaihtoehto dominoi kaikilla hänen rajoitteillaan | Valintaa ei ole vielä havaittu; tyhjän verkon vaihe |
| 2 | **OSUUS** | Laillinen reitti meille jäävään arvoon, nyt tai optiona | Oikeus, sopimus tai omistus; tai viivästetty optio §3:n neljällä kirjauksella (tila, ehdokasmaksu eri osapuolelta tai korvaava läsnä pilotissa, pilotin ajankohta, raukeava raja) | Oikeutta ei voi saada; pilotti korvaavan vaihtoehdon kanssa hajottaa osallistumisen; raja umpeutui | Optio voimassa, pilotti ajamatta |
| 3 | **KOHORTTI 2** | Koko nettotalous seuraavassa kohortissa, joka on eri kanavasta tai satunnaispoiminta | Hankinta, toimitus, ylläpidon kulmakerroin volyymiin nähden, vastuut, nimetty yhteinen häntäriski ja sen perustaso, nimetty toimija joka voi bundlata ja sen kustannus | Kohortti 2 negatiivinen; yhteinen häntä pysäyttää kaiken; bundlaus halvempi kuin meidän hinta; portfoliotason tappiobudjetti ylittyy | Kohorttia 2 ei ole; häntäriskin perustasoa ei tiedetä |
| 4 | **TILA** | Ennalta nimetty S ja sen kausaalinen vaikutus | Vastafaktuaali (sama tekoäly ilman S:ää), nettovaikutus koko talouteen, S:n käyttö ei kasva volyymin mukana, takaisinmaksutoistot ≤ todennettu jäljellä oleva kysyntä | S ei vaikuta vertailussa; takaisinmaksu vaatii enemmän toistoja kuin kysyntää on | Vastafaktuaalia ei ajettu; kysyntää ei todennettu |
| 5 | **VIPU** | Mallien osuus: but-for ja mitattu parannus | (1) Nimetty välitulos, jota ei olisi saavutettu ilman malleja samalla ihmisellä ja rahalla; (2) mitattu parannus samassa asetelmassa. Kestävyys erikseen: paras kilpailijan AI-ratkaisu kohortissa 2 | Kasvu selittyy vain palkkaamisella ja rahoituksella eikä (1) täyty: hyvä yritys, ei projektin tulos | Kontrollia ei saada |
| 6 | **SEURAAVA HAVAINTO** | Halvin avoin oletus, joka muuttaa päätöksen | Ennalta rajattu mittaus, hyväksyjä, raha- ja aikaraja, tulkinta kaikille tuloksille, portfolion tappiobudjetti johon tämä kuuluu | Määritelmää muutetaan tuloksen jälkeen; mikään saavutettava havainto ei muuta päätöstä | Ei mitattavissa nykyresursseilla: kirjataan sivuun, ei tapeta |

Tappojärjestys ei ole kiinteä; valitaan `c_i / q_i` -periaatteella (GPT §11), ja
laillisuus, pääsy ja resurssiraja tarkistetaan aina ensin ilman numerointia.

### Kolme vastausta

**1. Onko säilyvän kausaalisen tilan ydinehto edelleen vahvin jäljellä oleva ehto?**
Kyllä, mutta kahdella varauksella. Se on lähes tautologia (kausaalinen muisti), joten
sen koko sisältö on mittauksessa (v2.1 Q4). Ja vahvin *empiirinen* väite, joka
kierrokselta jää, on toinen: **jokaisessa 14 tapauksessa tunnistettu este oli oikeus,
luottamus tai pääsy, ei koodi eikä 1 000 €.** Se on FACT tapauksista, ei yleislaki, ja
se ennustaa: seuraavakin löydös kaatuu todennäköisimmin kysymykseen 2, ei 1:een.

**2. Mikä yksi koe antaisi nyt eniten informaatiota?** Kolmen parin pilotti: sama
operaattori, kolme peräkkäistä saman luokan tapausta, kirjataan kustannus per hyväksytty
tulos ja S:n rakennuskulu, ilman kontrolleja. Se vastaa kysymykseen "onko mitään
säästöä, jota kannattaa mitata kontrolloidusti", kymmenesosalla A/B/C:n hinnasta.
Tehtäväluokkaa ei valita tässä.

**3. Onko GPT:n kolmihaarainen koe oikea seuraava koe?** Ei vielä. Ensin pilotti (kohta 2).
Jos pilotti näyttää säästöä, ajetaan A/B/C/D §11:n muutoksilla: haara D rakennuskulun
mittaamiseen, käsikirjoitettu ihmisrooli, jako projektin ja päivämäärän mukaan, 10/12-
parisääntö ja takaisinmaksutoistot. Jos pilotti ei näytä säästöä, artefakti-S tässä
luokassa on kuollut ja koe säästetään.
