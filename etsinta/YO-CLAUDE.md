# Yövuoro 1 (2026-09-16): Clauden tutkimusloki

Tämä on ketju havainto → hypoteesi → data → testi → red team → uusi kysymys. Tulokset
ovat tiedostoissa `ORVOT-OMAISUUDET.md`, `COMPOUNDING.md`, `kokeet/02-*` ja
`data/orvot/`. Tämä tiedosto kertoo, miksi haara vaihtui ja mihin.

## Lähtökohta

Kierros 3 jätti kysymyksen: "mikä oli arvotonta, koska se vaati työtä, ja on nyt arvokasta,
koska työ on lähes ilmaista?" Ensimmäinen haara: orpo digitaalinen omaisuus. Kierroksen 3
mittaus oli pelkkiä GitHub-tähtiä (17 616 hylättyä yli 1 000 tähden repoa). Tähdet eivät
ole käyttäjiä eivätkä rahaa.

## Iteraatio 1: mittaa käyttöä, ei tähtiä

**Data:** ecosyste.ms-rajapinta (npm + PyPI, 5 000 ladatuinta per rekisteri), LikoHD:n
Chrome Web Store -aineisto (203 746 laajennusta), GitHub-issuehaku, Pixalate (sovellukset).

**Havainto:** 33,5 % npm:n ydinpaketeista on ilman julkaisua 2 vuoteen ja ne tuottavat
30 % latauksista. Mutta suurin osa on *valmiita* (`isarray`, `ms`), ei hylättyjä.

**Korjaus hypoteesiin 1:** "ei commiteja" ≠ "hylätty". Hylätty = käyttöä + tekemätöntä
työtä (advisory, avoimet issuet, rikkoutunut alusta). Se on pienempi joukko: npm 99
pakettia, joilla advisory ja yli 1 M latausta/kk.

**Uusi kysymys:** kuka maksaisi niiden ylläpidosta? Lataajat ovat koneita.

## Iteraatio 2: kuka maksaa ja mihin hintaan

**Data:** HeroDevs (1 000+ yritystä, 125 M USD sijoitus), Microns.io (39 listausta),
Secure Annexin laajennusostokoe, extensionhub.io.

**Havainto:** Maksaja on olemassa (HeroDevs: yritysten compliance). Listatut pienet
omaisuudet hinnoitellaan 5x vuositulo, kalliimmin kuin isot. Laajennuksia annetaan pois
ilmaiseksi, mutta ostajakunta on haitallinen (Cyberhaven, 400 k käyttäjän adblocker).

**Falsifiointi 1:** markkinavirhettä ei ole siellä, missä on markkina. Listattu pieni
omaisuus on kallista optioarvon takia.

**Korjaus hypoteesiin 2:** omistajan kustannus ei ollut koodi vaan vastuu. Tekoäly
laskee koodin hintaa, ei vastuun. Kysymys pitää muotoilla uudelleen: "mikä oli
arvotonta, koska se vaati vastuuta, jota kukaan ei halunnut kantaa ilmaiseksi".

**Red team -tulos:** jokainen omistajanvaihdos näyttää hyökkäykseltä (xz, event-stream,
polyfill.io, laajennuskampanjat 2024 - 2025). Nopea, uusi, tekoälyllä toimiva ylläpitäjä
on täsmälleen uhkaprofiili. Tämä ei tapa mekanismia, mutta pakottaa sen hitaaksi ja
julkiseksi.

## Iteraatio 3: missä este oli oikeasti pelkkää työtä?

**Päättely:** jos vastuu on todellinen kustannus, etsi tilanteet, joissa omistaja *haluaa*
pitää omaisuuden mutta ei tee työtä. Pakotetut alustamigraatiot: Manifest V3, DSA-
kauppiastiedot (135 000 sovellusta poistettiin EU:n App Storesta helmikuussa 2025),
Google Playn laatuvaatimukset (1,6 M sovellusta pois), WordPressin "tested up to",
Shopifyn API-versiot. Niissä työ on määräaikainen, tylsä ja omistaja on olemassa.
Omistajuus ei vaihdu, joten luottamusongelma katoaa. Maksaja on omistaja.

**Data:** WordPress.org-rajapinta (10 000 suosituinta, aktiiviset asennukset, päivitys,
tested up to), "adopt-me"-tagi (virallinen luovutuskanava: vain 17 lisäosaa, 3 210
asennusta yhteensä, eli vapaaehtoinen luovutuskanava on käytännössä tyhjä).

Jatkuu alla sitä mukaa kun data valmistuu.

## Iteraatio 3, tulokset

- Chrome-otos 390: 23 % yli 10 k käyttäjän laajennuksista poistettu 20 kuukaudessa
  (98 M käyttäjää tammikuussa 2025). Elossa olevista 31 % orpoja, mutta kärki on
  yritysten valmiita laajennuksia. Yli miljoonan käyttäjän orvot menettävät 60 %
  käyttäjistä vuodessa.
- WordPress 10 000: 2 354 orpoa (23,5 %), 8,47 M asennusta, 166 yli 10 k asennuksella,
  joista **40 %:lla on jo ylläpidetty korvaaja hakemistossa, ja 59:ssä korvaaja on jo
  suurempi**. Fork-kaista on siis puoliksi täynnä, ja se täyttyy ilman meitä.
- 80 issuen luokittelu: omistajat eivät pyydä rahaa (1/80), pääsy annetaan alle
  puolessa, "otan ylläpidon" -tekoälyspämmi on jo ilmiö.
- html5lib-koe: koodi 13 sekuntia, julkaisunappi 2,5 vuotta jumissa.

**Falsifiointi 2:** "ylläpito halpenee" ei ole mekanismi. Pullonkaula on julkaisuoikeus ja
luottamus. Kortti hylätty (23 → 17). Kaksi elävää muotoa erotettu omiksi korteiksi:
pakotetut migraatiot omistajan lukuun (22 p) ja jatkaja-palvelu (HeroDevs-malli, vaatii
todennetun historian, ei kortti vaan `COMPOUNDING.md`).

## Iteraatio 4: mikä on yleisempi mekanismi?

**Vastaus:** tekoäly tekee työn ilmaiseksi, arvo siirtyy portteihin. Portti on oikeus,
luottamus, pääsy tai vastuu. Kysymys projektille muuttuu: "missä on portti, jonka yksi
ihminen saa halvalla, jonka takana työ on nyt ilmaista ja jonka läpi raha jo virtaa?"

## Iteraatio 5: avoin haara, raha järjestelmänä

Ks. `AVOIN-HAARA-2.md`. Viisi kandidaattia mitattu. Vahvin: **auktorisoitu kääntäjä**.
Rekisterissä 1 381 kääntäjää, ukraina→suomi 6, somali→suomi 0, portin hinta 570 €,
hinta asiakkaalle 65 - 105 €/sivu, 46 000 ukrainalaista tilapäisen suojelun piirissä.
Red team: portti vaatii kielitaidon, jota meillä ei ehkä ole. Mekanismi on silti puhdas
esimerkki, ja siitä seuraa generaattori: **kaikki lakisääteiset henkilökohtaiset
pätevyysrekisterit, mitattuna tutkinnon hinta × tarjonta × työn konemaisuus.**

Hylätty: EU-vastuuhenkilöroolit (hinta jo 199 €/v, vastuu jota kukaan ei kanna),
kiinteistöverovirheet (liian pieni per kohde). Avoinna: konkurssipesien digitaalinen
omaisuus (sivu ei auennut ilman selainta), Migrin hakemusmäärät kansalaisuuksittain.

## Mihin yövuoro päättyi ja miksi

Konkurssipesien huutokaupat luettu selaimella: 602 kohdetta, kaikki fyysisiä. Hylätty
lähteenä. Kaikki yön haarat on nyt joko mitattu tai falsifioitu, ja seuraavat askeleet
vaativat omistajaa:

1. **Kielitaito.** Auktorisoitu kääntäjä -mekanismi on todennettu, mutta sen käyttäjä on
   se, jolla on harvinainen kieli. omistajan ja lähipiirin kieliparit ratkaisevat, onko tämä
   meidän vai jonkun muun mahdollisuus. Tutkintomaksu 570 € vaatii luvan.
2. **Ensimmäinen ihmissuhde.** Ostoreskontran takaisinperintä ja pakotetut migraatiot
   vaativat yhden asiakkaan tai kymmenen omistajan kontaktoinnin. Claude ei ota yhteyttä.
3. **GPT:n haaste.** Kolme uutta korttia ja kaksi muistiota odottavat haastetta.

Seuraavan kierroksen ensimmäinen tehtävä, joka ei vaadi omistajaa: **pätevyysrekisteri-
generaattori**. Lista Suomen lakisääteisistä henkilökohtaisista pätevyyksistä, jokaisesta
portin hinta, tarjonta per erikoisala, työn konemaisuus ja hinta per suorite. Kolme on
ajettu, arviolta 20 - 30 jäljellä.

## Mitä emme tienneet eilen

- Kolmannes npm:n ytimestä on ilman julkaisua kahteen vuoteen, ja se on pääosin kunnossa.
- 23 % yli 10 000 käyttäjän Chrome-laajennuksista katosi 20 kuukaudessa.
- Hylättyjen projektien omistajat eivät halua rahaa: 1/80. He haluavat pois vastuusta.
- html5lib:n korjaus oli 13 sekuntia ja se oli jo tehty kolmesti. Nappi puuttui.
- "Otan ylläpitovastuun" -tekoälyviestit ovat jo spämmiä, jota yhteisö tunnistaa.
- Suomessa on kuusi ukrainasta suomeen auktorisoitua kääntäjää ja 46 000 ukrainalaista.

## Lisäys: GPT:n rinnakkainen vuoro

GPT pushasi `gpt-work/`-kansion samaan aikaan. Vastaus ja vertailu: `etsinta/VASTAUS-GPT-1.md`.
Tärkein yhteinen tulos: GPT:n mittaamattomista kohdista kaksi (omistajan vastatarjous,
hyväksytyn löydön osuus) mitattiin tänä yönä, ja GPT:n ehdottama testivarantokoe voidaan
ajaa julkisella WordPress/PyPI-aineistolla ilman lupaa ja rahaa.

## Synteesi (sama päivä, GPT:n JATKO-C:n jälkeen)

`etsinta/SUUREN-VIPUVAIKUTUKSEN-TEORIA.md`: kuusi välttämätöntä ehtoa, kahdeksan tapettua
oletusta, 11-kohtainen rakennetesti tappojärjestyksessä, seitsemän tapausta yksikkötesteinä
(HeroDevs pakotti korjaamaan HUMAN-kysymyksen), tuhoamisyritys kolmella korjauksella
(EV, maine yleisönä, viivästetty kaappaus). PROSESSI.md muutettu kahdesta kohdasta.

## Ristiinarvio 2

GPT:n `TEORIAN-TUHOAMISYRITYS-V2.md` luettu ja vastattu: `etsinta/VASTAHYOKKAYS-V2.md`.
GPT survives 9 kohdassa, modified 7:ssä, killed 4:ssä (v2:n näyttö on yksikkötason ja
päästää läpi kuusi populaatiotason virhettä; Q3 tappaa portfoliomekanismin; haara C ei
mittaa rakennuskulua; hetkellinen etu ei riitä 10 000x:ään). Yhteinen v2.1 kuudella
kysymyksellä. Seuraava koe: kolmen parin pilotti ennen A/B/C:tä.

## Ristiinarvio 3

Oman commitin `f5d26a7` tuhoamisyritys: `etsinta/KEHIKON-TUHOAMISYRITYS-V3.md`. v2.1
katkesi esikarsintana, 14/14 katkesi (5/14), pilotti katkesi, STATE on määritelmä.
Kestää: baseline rajattuna, viivästetyn kaappauksen sääntö, kuusi väärää positiivista,
haara D, 0/14 raha tai koodi. Lukittu koe 03: toistuvuusmittaus ennen mitään A/B:tä.

## Koe 03

Toistuvuusmittaus ajettu lukitulla protokollalla: R = 0,25, K = 1, H = 0,75 → KILL.
Artefakti-S kuollut PyPI-luokassa. 15/20 orvoista toimii Python 3.14:llä. Raportti
`kokeet/03-toistuvuusmittaus.md`, raakadata `kokeet/03-tulokset.jsonl`.

## Seuraava havainto

`etsinta/SEURAAVA-HAVAINTO.md`: koe 03 opetti "ei hallitsevaa yhteistä syytä", ei "ei
toistuvuutta"; WordPress hylätty seuraavana kokeena (matala informaatio); "artefakti-S kuolee
kokonaan" korjattu; valittu koe 04 yleisötila (repo on yksityinen, tila on ollut 0).
