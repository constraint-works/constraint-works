# Koe 04: sanitointi ja git-historian uudelleenkirjoitus (2026-09-16)

Tehty omistajan päätöksellä: projekti julkaistaan pseudonyymillä projekti-identiteetillä
"eikaisiina", ei henkilön nimellä. Repo on edelleen yksityinen. Ei julkaistu.

## Mitä tehtiin (FACT)

1. Varmuuskopio koko historiasta paikalliseen peiliin ennen muutoksia (ei repossa).
2. `git filter-repo` ajettiin koko historiaan (31 commitia): kaikkien commitien author ja
   committer korvattu muodolla `eikaisiina <eikaisiina@users.noreply.github.com>`.
   Kaikkiin blobeihin sovellettiin korvaussäännöt: omistajan koko nimi → "eikaisiina";
   etunimen kaikki taivutusmuodot → "omistaja"-muodot; henkilökohtainen sähköposti ja
   verkkotunnus → "(poistettu)"; paikalliset hakemistopolut, joissa käyttöjärjestelmän
   käyttäjänimi näkyi → neutraalit polut; kolmen kolmannen osapuolen sähköpostiosoitteet
   johdetuissa datatiedostoissa → "(sähköposti poistettu)".
3. Uudelleenkirjoituksen jälkeen 14 vanhaan commit-SHA:han perustuvaa viittausta
   tiedostoissa korjattiin filter-repon commit-mapista (GPT:n ja Clauden muistiot,
   kokeen 03 raportti, GPT:n protokolla-JSON).
4. Repo-paikallinen git-tekijä asetettu projekti-identiteetiksi tuleville commiteille.
5. Uusi historia pakotettu GitHubiin (`push --force`).

## Tarkistus uudessa historiassa (FACT)

- Etunimi, sukunimi, henkilökohtainen sähköposti tai verkkotunnus: 0 osumaa blobeissa,
  commit-viesteissä, tiedostonimissä ja tekijätiedoissa.
- Sähköpostiosoitteet koko historiassa: vain projekti-identiteetin noreply-osoite,
  Clauden Co-Authored-By-osoite, yksi organisaatio-osoite (extensions@chromium.org, Chromen
  oma laajennus, ei henkilö) ja yksi regex-artefakti ("+@socket.io", ei osoite).
- Tekijät: 31/31 commitia `eikaisiina`. GitHub näyttää ne linkittämättöminä.

## Rikkoutuneet sisäiset viittaukset

- 14 SHA-viittausta korjattu (lista commitissa). Kaikki vanhat SHA:t on korvattu
  vastaavilla uusilla samalla pituudella.
- GPT:n `public-build-protocol.json`: kenttä `source_commit` päivitettiin uuteen SHA:han,
  joten GPT:n JATKO-C:ssä kirjaama tiedoston SHA-256 (4cab3b33…) ei enää vastaa tiedostoa.
  Tämä on uudelleenkirjoituksen seuraus ja on kirjattu tähän; protokollan sisältö ei muuttunut.
- GPT:n READMEssä kirjattu WORK-A.md:n SHA-256 (38bc3240…) ei vastaa tiedostoa
  **ennen eikä jälkeen** uudelleenkirjoituksen (ennen: 552a5e76ecd80735…, jälkeen: 552a5e76ecd80735…, tiedosto
  ei muuttunut). Poikkeama oli olemassa jo aiemmin (todennäköisesti GPT laski hashin
  toisesta tavumuodosta). Ei tämän toimenpiteen aiheuttama.

## Jäljelle jäävät deanonymisointiriskit (INFERENCE)

1. **Repon sijainti:** `github.com/original-private-account/eikaisiina`. Käyttäjänimi "original-private-account" näkyy
   URL:ssä ja viidessä tiedostossa (mittausskripti, protokolla, GPT:n linkit). Jos tili
   yhdistyy henkilöön (profiili, muut repot), pseudonymiteetti murtuu. Korjaus vaatii
   GitHub-organisaation tai -tilin luomisen nimellä "eikaisiina" ja repon siirron sinne
   ennen julkistamista; sen jälkeen "original-private-account" korvataan tiedostoissa. Claude ei luo tilejä.
2. **Vanhat commitit GitHubissa:** vanha HEAD `71a7e79` on yhä haettavissa suoralla
   SHA-osoitteella (tarkistettu rajapinnasta), vaikka se ei ole enää missään haarassa.
   GitHub poistaa irralliset objektit vasta roskienkeruussa, ja pyynnöstä tukipalvelu
   voi poistaa ne heti. Riski on pieni (SHA pitää tietää), mutta olemassa, kunnes
   objektit on poistettu.
3. **Commit-aikaleimat** ovat +0300 (Suomi). Projekti on sisällöltään suomalainen, joten
   tämä ei lisää tietoa.
4. **Superteam:** agentti "eikaisiina" on rekisteröity Superteamiin; lunastusprofiili on
   omistajan. Repossa ei ole tunnistetta, mutta Superteamin puolella agentti yhdistyy
   ihmiseen. Ei repon ongelma, mutta yhdistettävissä, jos joku hakee agentin nimeä.
5. **Kirjoitustyyli ja sisältö:** suomenkieliset muistiot, paikalliset lähteet ja
   projektin kuvaus rajaavat tekijän suomalaiseksi. Ei henkilöön asti.
6. **Paikallinen varmuuskopio** vanhasta historiasta on koneella scratchpad-hakemistossa,
   ei repossa. Se pitää poistaa tai säilyttää tietoisesti.
7. Muistiinpanot, jotka Claude pitää projektin ulkopuolella, sisältävät omistajan nimen.
   Ne eivät ole repossa eivätkä julkaistavia.

## Mitä ei muutettu

- GitHub-käyttäjänimet 80 issuen luokittelussa ja datatiedostoissa (julkisia, alkuperäisten
  issueiden kirjoittajia).
- WordPress-lisäosien tekijöiden nimet tekijäkentässä (julkisia hakemistotietoja);
  vain sähköpostiosoitteet poistettiin.
- Koe 04:n AUDIENCE/ACCESS-mittarit ja kynnykset.
