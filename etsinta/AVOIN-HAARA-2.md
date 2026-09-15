# Avoin haara 2: raha järjestelmänä (yövuoro 1)

Tehtävä: unohda bountyt, hackathonit, agenttityö, lunastamattomat oikeudet, orvot ohjelmistot
ja nykyiset hypoteesit. Yksi ihminen, kaksi frontier-mallia, enintään 1 000 €, kaikki
laillista. Missä raha liikkuu jo, mikä sääntö ratkaisee kuka sen saa, ja missä tekoäly
muuttaa sitä mekanismia?

## Yön yleistys, josta lähdin

Orpojen omaisuuksien mittaus (`ORVOT-OMAISUUDET.md`) päättyi yhteen lauseeseen:
**tekoäly tekee työn ilmaiseksi, ja arvo siirtyy portteihin: oikeuksiin, luottamukseen,
pääsyyn ja vastuuseen.** html5lib: koodi 13 sekuntia, julkaisunappi 2,5 vuotta jumissa.

Kysymys avoimelle haaralle on siis: **missä on portti, jonka yksi ihminen saa halvalla,
jonka takana työ on nyt ilmaista, ja jonka läpi raha jo virtaa?**

Portin pitää olla (1) laillinen ja henkilökohtainen (ei ostettavissa, ei sybil), (2)
hankittavissa alle 1 000 eurolla tai ajalla, (3) sellainen, että sen haltija allekirjoittaa
ja kantaa vastuun, ja työn tekee kone.

## Kandidaatit ja mittaukset

### 1. Auktorisoitu kääntäjä (allekirjoitus tuotteena)

**Mekanismi:** Viranomaiset (Migri, tuomioistuimet, PRH, yliopistot) vaativat asiakirjoista
auktorisoidun kääntäjän vahvistaman käännöksen. Auktorisointi saadaan Opetushallituksen
tutkinnolla (kerran vuodessa marraskuussa, maksu 570 €, FACT oph.fi ja kieliasiantuntijat.fi)
tai käännöstieteen maisterintutkinnolla. Hinta asiakkaalle 65 - 105 €/sivu (FACT, useat
toimistot 2025 - 2026). Kääntäjä on juridisesti vastuussa vahvistamastaan käännöksestä
(FACT, SKTL:n ohjeet), ja saa vahvistaa toisen tekemän käännöksen tarkistettuaan sen.
Konekäännöksen käytöstä ei ole kieltoa (UNKNOWN: ei löytynyt ohjetta puolesta eikä vastaan).

**Tarjonta, mitattu (FACT, akr.opintopolku.fi:n julkinen rajapinta 2026-09-16, data
`data/akr-kieliparit-2026-09-16.json`):** rekisterissä **1 381 kääntäjää, 91 kieliparia**.
Englanti→suomi 259, suomi→ruotsi 170, venäjä→suomi 142. Mutta maahanmuuton kielissä:

| Kieli | →suomi | suomi→ |
|---|---|---|
| arabia | 6 | 11 |
| ukraina | **6** | 2 |
| persia | 1 | 5 |
| turkki | 5 | 6 |
| kiina | 1 | 1 |
| somali | **0** | 2 |
| kurdi, vietnam, thai, albania, pašto, urdu, swahili, tigrinja | **0** | 0 |

Tilapäisen suojelun hakemuksia 2025: 12 018, ukrainalaisia tilapäisen suojelun piirissä noin
46 000 (FACT, Migri). Ukrainan kielestä suomeen on **kuusi** auktorisoitua kääntäjää koko maassa.

**Portti:** tutkinto, 570 €, kerran vuodessa, yhteen suuntaan kerrallaan. Se on täsmälleen
"alle 1 000 €" -portti. Auktorisointi 5 vuotta kerrallaan.

**Tekoälyn rooli:** kääntää, kääntäjä tarkistaa ja vahvistaa. Sama rakenne kuin HeroDevs:
vastuu on tuote, työ on kone.

**Red team:**
- Tutkinto mittaa henkilön omaa käännöstaitoa kieliparissa. omistajan kielitaito ratkaisee,
  mihin pariin tämä on edes mahdollista (UNKNOWN). Harvinaisissa pareissa tarvitaan
  natiivitason osaaminen. Tämä ei ole "kuka tahansa + tekoäly" -portti, vaan
  "kielitaitoinen + tekoäly".
- Läpäisyaste UNKNOWN (haetaan). Jos alle 30 %, 570 € on arpa.
- Kysyntä per kielipari UNKNOWN euroina. Ukrainalaisia Suomessa kymmeniä tuhansia;
  tutkintotodistukset, syntymätodistukset, avioliittotodistukset.
- Eettinen raja: hinnoittelu ei saa hyödyntää hätää. Markkinahinta 65 - 105 €/sivu on
  vakiintunut; tekoälyn kanssa marginaali on suuri, ja sen voi jakaa asiakkaan kanssa.
- Kilpailu: käännöstoimistot, joilla on harvinaisten kielten auktorisoituja freelancereita.
  Rekisteri sanoo, että heitä on 0 - 6 per kieli. Se on niukkuus, ei kilpailu.

**Tuomio:** Vahvin tämän yön "outo mutta todennettu" -löytö avoimessa haarassa. Ei
kymmenen miljoonan mekanismi, mutta puhdas esimerkki mekanismista: laki luo portin,
portin hinta on 570 €, portin takana työ muuttui ilmaiseksi, tarjonta on lähes nolla.
**Yleisempi muoto:** etsi rekisterit, joissa lakisääteinen pätevyys on henkilökohtainen,
halpa ja harva, ja työ konemaista. Kortti: `mahdollisuudet/auktorisoitu-kaantaja.md`.

### 2. EU:n vastuuhenkilöroolit (vastuu palveluna)

GDPR 27 art. edustaja (ei-EU-yrityksille, 199 - 1 500 €/v), GPSR:n vastuuhenkilö
(2024-12 alkaen kaikille EU:n ulkopuolisille kuluttajatuotteiden myyjille, 150 - 2 750 €/v),
AI Act 22 art. valtuutettu edustaja (siirretty joulukuuhun 2027, FACT asetus 2026/1744),
CRA:n edustaja (vapaaehtoinen, 2027). Kiinalaisia myyjiä on 50 % Amazonin myyjistä
(FACT, Marketplace Pulse 2025).

**Portti:** EU:ssa oleva oikeushenkilö, joka suostuu vastuuseen. Halpa. **Mutta** hinta on
jo painunut 199 euroon vuodessa, mikä kertoo, että työ oli jo nolla ja hinta on pelkkää
vastuuta, jota kukaan ei oikeasti kanna (150 €/v vastuuhenkilö ei maksa tuotevahinkoa).
Tekoäly ei muuta tätä. **Hylätään mekanismina, säilytetään havaintona:** sääntely tuottaa
uusia portteja aikataululla (AI Act 2027, CRA 2027), ja ensimmäinen kuukausi jokaisen
portin avautuessa on ainoa hetki, jolloin hinta ei ole vielä 199 €.

### 3. Konkurssipesien omaisuusmyynnit (laillinen orpo-omaisuus)

Pesänhoitaja myy ohjelmistoja, domaineja, asiakasrekistereitä ja liiketoimintoja
selvällä omistusoikeudella, nopeasti ja ilman luottamusongelmaa, joka tappoi
orpo-ohjelmistot. Huutokaupat.com:lla on konkurssipesien oma kategoria: **602 ilmoitusta** 2026-09-16
(FACT, luettu selaimella). Ensimmäiset 40 kohdetta olivat kaikki fyysisiä: laboratorio-
laitteita, mattoja, polkupyöriä, huoneistoja. Ei yhtään ohjelmistoa, domainia tai
asiakasrekisteriä. Digitaalinen omaisuus myydään ilmeisesti pesänhoitajan suoralla
kaupalla, ei julkisessa huutokaupassa (INFERENCE). **Hylätään julkisena lähteenä**;
säilytetään ajatus: pesänhoitajille suunnattu "ostamme ohjelmistot ja domainit" -kanava
olisi mahdollinen, mutta se vaatii suhteita, ei skanneria.

### 4. Ostoreskontran takaisinperintä pk-yrityksille

Kortti kirjoitettu: `mahdollisuudet/ostoreskontran-takaisinperinta.md`. Puhtain "arvotonta,
koska tarkastus vaati työtä" -tapaus: raha on jo väärässä paikassa, suuryrityksille
palvelu on olemassa (20 - 30 % palkkio, 0,1 % ostoista), pk-yrityksille ei. Portti:
pääsy kirjanpitodataan. Ensimmäinen asiakas vaatii omistajalta suhteen.

### 5. Julkisten rekisterien virheet (kiinteistövero)

Kiinteistöveroa 2 429 M € vuonna 2025 (FACT, vero.fi). Ammattilaisten tarkastuksissa
palautus keskimäärin 7 % verosta, oikaisu 3 vuotta taaksepäin (toissijainen: Sustera
/ Rakennusmaailma). Yksittäiselle omakotitalolle 100 - 300 € kertaluonteisesti, liian
pieni palveluksi, riittävä itsepalvelutyökaluksi, jolla ei ole tuloa. Isot kiinteistöt
ovat jo konsulttien hallussa. **Hylätään ansaintana**, kirjataan oikeuskartoitukseen
kohdaksi 21.

### Generaattorin ensimmäinen ajo: kolme pätevyysrekisteriä

| Rekisteri | Portin hinta | Tarjonta | Hinta per suorite | Työn konemaisuus | Huomio |
|---|---|---|---|---|---|
| Auktorisoidut kääntäjät (OPH) | 570 €, tutkinto 1×/v (toissijainen: kieliasiantuntijat.fi) | 1 381, maahanmuuttokielissä 0 - 6 (FACT) | 65 - 105 €/sivu (FACT) | Korkea: kone kääntää, ihminen tarkistaa | Vaatii kielitaidon. Vahvin |
| Energiatodistuksen laatijat (Varke, ent. ARA) | Pätevyystentti, hinta UNKNOWN | 1 199 perustaso + 79 ylempi (FACT, mutta vuoden 2013 luku) | 229 - 600 €/todistus (FACT, hinnastot 2025 - 2026) | Keskitaso: laskenta konemaista, olemassa olevassa rakennuksessa vaaditaan katselmus paikan päällä | Pakollinen myynnissä ja vuokrauksessa. Tarjonta ei ole niukka |
| Auktorisoidut teollisoikeusasiamiehet (PRH-lautakunta) | Tutkinto + vuosi kokemusta + ylempi korkeakoulututkinto (FACT) | UNKNOWN | Tuntilaskutus, satoja €/h | Korkea: hakemusten laadinta | Portti liian korkea yhdelle ihmiselle ilman alan taustaa |

Ensimmäinen ajo vahvistaa kriteerin: portin pitää olla **halpa, henkilökohtainen ja harva**.
Energiatodistus on halpa mutta ei harva. Patenttiasiamies on harva mutta ei halpa.
Auktorisoitu kääntäjä harvinaisessa kielessä on kaikkea kolmea, mutta vain sille, jolla
on kieli.

## Mitä avoin haara opetti

1. **Portti, jonka hinta on jo painunut nollaan, ei ole portti** (EU-edustajat 199 €/v).
   Etsi portteja, joissa hinta on vielä korkea *ja* tarjonta on harva. Auktorisoitu
   kääntäjä ukrainasta: 6 henkilöä, 65 - 105 €/sivu.
2. **Henkilökohtainen pätevyys on paras portti**, koska sitä ei voi ostaa, kopioida eikä
   sybilöidä, ja tekoäly ei voi suorittaa tutkintoa. Se on niukkuuskartan "oikeudellinen
   asema" (9 p), ja se oli alitutkittu.
3. **Generaattori:** käy läpi kaikki Suomen lakisääteiset henkilökohtaiset pätevyysrekisterit
   (auktorisoidut kääntäjät, tilintarkastajat, LKV, vakuutusedustajat, patenttiasiamiehet,
   isännöitsijät, oikeustulkit, energiatodistuksen laatijat, sähköpätevyydet, asbestikartoittajat,
   tulityökortit...) ja mittaa jokaisesta: tutkinnon hinta, tarjonta per erikoisala, työn
   konemaisuus, hinta per suorite. Rekisterit ovat julkisia rajapintoja, kuten tänään nähtiin.
   Tämä on seuraavan kierroksen ensimmäinen tehtävä.
