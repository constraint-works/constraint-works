# Koe 04: pre-flight, pseudonyymi julkaisuinfrastruktuuri

2026-09-16. Ei suoritettu. Ei tilejä luotu, ei repoa siirretty, ei julkaistu.

## Mitä nykyinen tila paljastaa (FACT, tarkistettu rajapinnasta)

| Kohde | Tila | Riski |
|---|---|---|
| Repo-osoite `github.com/original-private-account/eikaisiina` | Yksityinen | Käyttäjänimi on URL:ssä. Jos repo julkaistaan tässä osoitteessa, projekti on triviaalisti yhdistettävissä tiliin |
| Tili `original-private-account` | name, bio, company, blog, location, email, twitter: tyhjät; 2 julkista repoa; 0 seuraajaa; luotu 2026-02 | Profiili itsessään ei nimeä henkilöä. Kaksi muuta julkista repoa: UNKNOWN, yhdistävätkö ne henkilöön |
| Commit author/committer | 31/31 `eikaisiina <eikaisiina@users.noreply.github.com>` | Ei paljasta. Jos GitHubiin luodaan käyttäjä `eikaisiina`, GitHub linkittää tämän vanhan noreply-muodon osoitteen siihen automaattisesti |
| Tiedostot, joissa `original-private-account` | 5 tiedostoa, 9 riviä (SEURAAVA-HAVAINTO, TEORIAN-TUHOAMISYRITYS-V2 [GPT:n linkki], 04-mittaa.sh, 04-sanitointi, 04-yleisotila-protokolla) | Korjattava ennen julkaisua uudella commitilla |
| Tags, releases, issues, PR:t, wiki, discussions | 0, 0, 0, wiki pois, discussions pois; yksi haara `main`; 2 refiä | Ei jäänteitä |
| Vanhat commit-objektit (esim. `f036303`) | Yhä haettavissa suoralla SHA:lla vanhassa reposta | Poistuvat, kun vanha repo poistetaan |
| Commit-aikaleimat | +0300 | Rajaa Suomeen; sisältö on jo suomalainen |
| Superteam-agentti "eikaisiina" | Rekisteröity omistajan lunastusprofiiliin | Jos agenttinimi on Superteamissa julkinen ja yhdistyy ihmisprofiiliin, nimi "eikaisiina" on haettavissa. UNKNOWN, onko julkinen. Vaihtoehdot: agentin uudelleennimeäminen (jos rajapinta sallii) tai riskin hyväksyminen |
| Muistiinpanot Clauden puolella | Repon ulkopuolella | Ei julkaistavia |

## Puhtain ratkaisu ja mitä se rikkoo

**Suositus: uusi tili ja uusi repo, ei siirtoa, ei historian uudelleenkirjoitusta.**

1. Omistaja luo projektisähköpostin (ilmainen palveluntarjoaja tai oma verkkotunnus,
   ei henkilökohtaista osoitetta) ja GitHub-käyttäjätilin `eikaisiina` sillä. Käyttäjätili,
   ei organisaatio, jotta olemassa olevat commitit linkittyvät siihen noreply-osoitteen
   kautta. Profiiliin ei nimeä, ei sijaintia, ei linkkejä.
2. Uusi tyhjä repo `eikaisiina/eikaisiina`, yksityisenä.
3. Nykyinen historia pushataan sinne sellaisenaan: SHA:t säilyvät, GPT:n ja Clauden
   SHA-viittaukset pysyvät voimassa.
4. Yksi uusi commit: `original-private-account` → `eikaisiina` viidessä tiedostossa. GPT:n tiedostossa
   muutetaan vain linkin osoite, sisältö ei muutu; commit-viesti kertoo sen.
5. Vanha repo `original-private-account/eikaisiina` pysyy yksityisenä tutkimuksen alkuperäisenä
   GitHub-kontekstina vähintään koko kokeen ajan; sitä ei poisteta automaattisesti
   (omistajan päätös 2026-09-16). Vanhat irralliset objektit jäävät siten haettaviksi
   suoralla SHA:lla yksityisessä reposta, mikä vaatii kirjautumisen ja on hyväksytty
   jäännösriski. **Ei siirtoa (transfer)**, koska siirto loisi pysyvän uudelleenohjauksen
   vanhasta osoitteesta uuteen, ja vanha osoite sisältää käyttäjänimen.
6. Repon kuvaus, README:n ensimmäinen kappale ja kaikki badge- ja remote-viittaukset
   tarkistetaan uudessa reposta ennen julkistusta (nyt: ei badgeja, ei homepagea).
7. Vasta sitten: repo julkiseksi, HN-tili projektisähköpostilla, postaus.

Mitä tämä rikkoo: GPT:n V2-tiedoston linkki muuttuu (host), mikä korjataan kohdassa 4;
Clauden paikallinen remote vaihdetaan; `04-mittaa.sh` ja seuranta osoittavat uuteen
repoon. SHA:t eivät muutu. Historiaa ei kirjoiteta uudelleen.

Vaihtoehto B (siirto): nopeampi, mutta jättää uudelleenohjauksen. Ei suositella.
Vaihtoehto C (historian uudelleenkirjoitus): ei tarvita, koska tekijätiedot ovat jo
neutraalit.

## Jäljellä olevat pseudonymiteettiriskit suunnitelman jälkeen

1. Superteam-agentin nimi (UNKNOWN, onko julkinen ja linkitettävissä).
2. Tilin `original-private-account` kaksi muuta julkista repoa: jos niissä on henkilöön viittaavaa sisältöä
   ja joku vertaa tyyliä tai aiheita, yhdistäminen on mahdollista mutta ei triviaalia.
3. Kirjoitustyyli ja sisältö rajaavat tekijän suomalaiseksi tekoälytutkimuksesta
   kiinnostuneeksi henkilöksi. Hyväksytty.
4. GitHubin sisäinen data (IP, laskutus) yhdistää tilit; ei julkista.
5. Projektisähköpostin verkkotunnus, jos oma: WHOIS-suojaus tarvitaan. Ilmainen
   palveluntarjoaja välttää tämän.
6. Jos HN-tili tai Reddit-tili luodaan omistajan aiemmin käyttämästä IP-osoitteesta,
   alustat voivat sisäisesti yhdistää tilit; ei julkista.

## Tarkistuslista ennen nappia (kaikki omistajan toimia, ellei toisin mainita)

- [ ] Projektisähköposti luotu
- [ ] GitHub-käyttäjä `eikaisiina` luotu, profiili tyhjä
- [ ] Uusi yksityinen repo `eikaisiina/eikaisiina`, historia pushattu (Claude voi tehdä pushin, kun remote on olemassa ja omistaja antaa oikeuden)
- [ ] `original-private-account` → `eikaisiina` -commit uudessa reposta (Claude)
- [x] Julkaisuteksti hyväksytty (omistaja 2026-09-16, commit a34f79c)
- [x] Superteam-agentin nimi jää: syntynyt kokeen aikana, ei perittyä pääomaa. Varmistettava vain, etteivät claim/profile-linkit johda henkilöllisyyteen (omistaja tarkistaa Superteamin puolella)
- [ ] HN-tili luotu projektisähköpostilla, ei kommentteja
- [ ] Repo julkiseksi (omistaja)
- [ ] Postaus, item-id Claudelle, seuranta 48 h + 14 pv

## Omistajan päätökset 2026-09-16 (lukittu)

- JULKAISU-1.md hyväksytty sellaisenaan.
- omistajan olemassa oleva yritys pysyy myöhempien kaupallisten kokeiden juridisena taustana; ei ratkaista
  koe 04:ää varten.
- Superteam-agentin nimi `eikaisiina` jää: se on syntynyt tämän kokeen aikana ja on
  projektin itse rakentamaa historiaa. Henkilöllisyyteen johtavat claim/profile-linkit
  varmistetaan erikseen.
- Uusi GitHub-käyttäjä `eikaisiina` (jos vapaa) uudella projektisähköpostilla: ei bioa,
  kuvaa, seuraamisia tai muuta historiaa. Sen alle uusi yksityinen repo. Claude pushaa
  nykyisen historian ja tekee viisi osoitekorjausta. Omistaja tarkistaa uuden repon ennen
  julkiseksi muuttamista. Vasta sen jälkeen HN-tili ja koe 04.
- Vanhaa repoa ei poisteta automaattisesti; se säilyy yksityisenä vähintään koko kokeen ajan.
- **Identiteettien erottelu:** `eikaisiina` (GitHub, HN) on tutkimusprojektin identiteetti.
  Mahdollinen recovery-palvelu rakennetaan myöhemmin omaksi uudeksi brändikseen
  omistajan olemassa olevan yrityksen alle. Tutkimusyleisöstä syntyvää luottamusta ei käytetä myöhemmässä
  kylmässä B2B-kokeessa (koe 06). Tämä on lähtöresurssisäännön sovellus kokeen sisällä:
  kokeen aikana rakennettu maine on sallittua, mutta se kirjataan reitiksi, ja koe 06
  mittaa pääsyn rakentamista ilman sitä.

## Seuraava konkreettinen askel (omistaja)

1. Projektisähköposti. 2. GitHub-käyttäjä `eikaisiina`. 3. Tyhjä yksityinen repo
`eikaisiina/eikaisiina`. 4. Ilmoitus Claudelle → push, osoitekorjaukset, tarkistusraportti.

## Päivitys 2026-09-16: julkinen tutkimusidentiteetti on Constraint Works

**Omistajan päätös:** sisäinen projekti on edelleen `eikaisiina`; julkinen kansainvälinen
tutkimusidentiteetti on **Constraint Works**, ensisijainen GitHub-handle `constraintworks`.
Koe 04 tehdään tämän nollasta rakennetun identiteetin kautta. Vanha yksityinen repo jää
alkuperäiseksi tutkimuskontekstiksi eikä sitä poisteta. Constraint Worksin kautta syntyvää
yleisöä, mainetta tai kontakteja ei käytetä koe 06:n kaupallisena lähtöpääomana.

**Tehty (Claude, ilman tilejä):**
1. Historia uudelleenkirjoitettu toisen kerran: kaikki 41 commitia tekijänä
   `Constraint Works <noreply@constraintworks.invalid>`. `.invalid`-verkkotunnusta ei voi
   kukaan omistaa (RFC 2606), joten osoite ei koskaan linkity mihinkään tiliin, ei
   myöskään vahingossa vieraaseen käyttäjään, toisin kuin `<nimi>@users.noreply.github.com`,
   jonka GitHub linkittää sen käyttäjänimen haltijaan.
2. Historiasta purettu omistajan yrityksen nimi (kolme riviä, omistajan oma muotoilu, joka
   oli kopioitu sellaisenaan) ja vanhan tilin käyttäjänimi kaikista blobeista.
3. Neljä SHA-viittausta korjattu commit-kartasta. Aiempi varmuuskopio ennen tätä
   uudelleenkirjoitusta on paikallisessa peilissä (ei repossa).
4. `04-mittaa.sh`: repo-osoite `REPO`-muuttujassa, oletus `constraint-works/eikaisiina`.
5. README: englanninkielinen otsake, joka nimeää Constraint Worksin ja linkittää
   julkaisutekstiin.
6. GPT:n V2-tiedostossa vain commit-linkin host vaihdettu; sisältö ennallaan.
7. Paikallinen git-tekijä asetettu Constraint Worksiksi.

**Tarkistettu GitHubista (FACT):**
- `ConstraintWorks` on **jo olemassa organisaationa** (luotu 2026-07-22, ei repoja, ei
  julkisia jäseniä, tyhjä profiili). Kirjautunut tili ei ole sen jäsen, joten repoa ei voi
  luoda sinne tällä kirjautumisella. UNKNOWN, kenen organisaatio se on.
- Vapaana ovat sekä käyttäjänä että organisaationa: `constraint-works`,
  `constraintworks-research`, `constraintworksresearch`, `constraint-works-research`,
  `constraintworkslab`. Skriptien oletus on `constraint-works`.
- Organisaatiota ei voi luoda REST-rajapinnalla tavallisella tilillä; käyttäjätiliä ei
  voi luoda ollenkaan ilman selainta. Claude ei luo tilejä eikä pyydä tunnisteita.
- HN-käyttäjänimi `constraintworks` on vapaa (HN:n julkinen rajapinta palauttaa null).
- Superteam: julkista agenttisivua ei löytynyt kokeilluista poluista (404 tai 500).
  Claim/profile-linkitys jää omistajan tarkistettavaksi Superteamin kirjautuneella puolella.
- Vanha tili kuuluu yhteen organisaatioon, jonka jäsenyys ei ole julkinen. Se ei näy
  uudessa identiteetissä, koska uutta repoa ei siirretä vaan pushataan uuteen paikkaan.

**Kaksi reittiä eteenpäin (omistaja valitsee sen, joka on mahdollinen):**
- **A.** Jos omistaja hallitsee organisaatiota `ConstraintWorks` toisella kirjautumisella:
  lisää vanha tili organisaation jäseneksi (yksityinen jäsenyys, ei julkinen) ja luo
  sinne tyhjä yksityinen repo `eikaisiina`, tai anna jäsenelle oikeus luoda repoja.
  Sen jälkeen Claude pushaa ja vaihtaa `REPO`-oletukseksi `ConstraintWorks/eikaisiina`.
- **B.** Muuten: luo selaimessa uusi GitHub-käyttäjä `constraint-works` (tai muu vapaa
  muoto) projektisähköpostilla, ilman biota, kuvaa tai seuraamisia, ja sen alle tyhjä
  yksityinen repo `eikaisiina`. Lisää vanha tili collaboratoriksi (yksityinen) tai
  kirjaudu `gh auth login` -komennolla uudella tilillä selaimen kautta. Claude pushaa.

Kummassakin tapauksessa: ei siirtoa (transfer), ei uudelleenohjausta, vanha repo pysyy
yksityisenä ja ennallaan.

**Varmuuskopio:** uudelleenkirjoitettu historia pushataan vanhaan yksityiseen repoon
haaralle `cw-migration`. Vanhan repon `main` säilyy koskemattomana alkuperäisenä
kontekstina.

**Tila: NOT READY.** Ainoa todellinen blokkeri on GitHub-identiteetin luonti tai siihen
pääsy (reitti A tai B), joka vaatii selaimen. Kaikki muu on tehty.
