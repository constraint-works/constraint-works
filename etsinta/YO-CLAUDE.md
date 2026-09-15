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
