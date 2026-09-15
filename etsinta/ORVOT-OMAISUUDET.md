# Orvot digitaaliset omaisuudet: mittaus

Yövuoro 2026-09-16. Kysymys: **onko tässä markkinavirhe?** Voiko tekoäly tehdä hylätyn
mutta niukan resurssin (käyttäjät, jakelu, integraatiot, historia) sisältävän omaisuuden
ylläpidosta niin halpaa, että omaisuus muuttuu jälleen arvokkaaksi?

Merkinnät: FACT = luettu lähteestä tänään, CALC = laskettu omasta datasta, INFERENCE =
päättely, HYPOTHESIS = testaamaton, UNKNOWN = ei löytynyt.

## 1. Kuinka paljon omaisuutta on ja kuinka paljon sillä on käyttöä

### npm ja PyPI (ecosyste.ms-rajapinta, 5 000 ladatuinta pakettia per rekisteri)

Skripti: `tyokalut/haku/hae_orvot_paketit.py`. Data: `data/orvot/*.csv`.
"Orpo" tässä = ei yhtään julkaisua 2 vuoteen (raja 2024-09-16).

| | npm | PyPI |
|---|---|---|
| Orpoja 5 000 ladatuimmasta | **1 674 (33,5 %)** | **1 116 (22,3 %)** |
| Orpojen osuus latauksista | **30,0 %** (211 mrd/kk) | 10,0 % (14,3 mrd/kk) |
| Viimeinen julkaisu yli 5 v sitten | 802 | 418 |
| Yksi ylläpitäjä | 1 042 | 717 |
| Tunnettu haavoittuvuus (advisory) | 99 | 32 |
| Vähintään 50 avointa issuea repossa | 315 | 270 |
| Enintään 15 versiota (pieni, valmis) | 1 006 | 580 |

Kaikki CALC omasta datasta, lähdedata FACT (ecosyste.ms 2026-09-16).

**Tulkinta:** Kolmannes npm:n ydinpaketeista on "orpoja", mutta suurin osa niistä ei ole
hylättyjä vaan **valmiita**: `ms`, `isarray`, `inherits`, `object-assign` (viimeinen
julkaisu 2017, 637 M latausta/kk, 12 624 riippuvaa pakettia). Kymmenen rivin apufunktio ei
tarvitse ylläpitoa. Se on ensimmäinen korjaus lähtöhypoteesiin: **"ei commiteja" ei
tarkoita "hylätty"**. Kierroksen 3 luku 17 616 hylättyä yli 1 000 tähden repoa on
yläraja, ei arvio.

Aidosti hylättyjä (käyttöä + korjaamatta jäänyttä työtä) on pienempi joukko: npm:ssä 99
orpoa, joilla on tunnettu haavoittuvuus ja yli miljoona latausta kuukaudessa
(`node-fetch` 722 M/kk, 3 advisorya, 249 avointa issuea; `html2canvas` 63 M/kk, 1 052
avointa issuea, 1 ylläpitäjä). PyPI:ssä `html5lib` (30 M/kk, viimeinen julkaisu 2017,
2 advisorya, 104 issuea), `weasyprint`-vanha, `opencv-python` (36 M/kk, 31 advisorya).

**Mutta npm-lataukset eivät ole käyttäjiä.** Ne ovat CI-koneita ja riippuvuuspuita.
Yksikään näistä paketeista ei tuota ylläpitäjälleen rahaa lataajilta. Ainoa maksaja on
yritys, jolla on compliance-syy (ks. HeroDevs alla).

### Chrome Web Store

Aineisto: LikoHD/chrome-extentions-list, 203 746 laajennusta, tilanne 2025-01-05 (FACT,
GitHub LFS). Käyttäjämääräjakauma (CALC):

| Käyttäjiä | Laajennuksia |
|---|---|
| yli 1 M | 496 |
| 100 k - 1 M | 1 908 |
| 10 k - 100 k | 7 236 |
| 1 k - 10 k | 19 699 |
| alle 1 k | 174 407 |

Aineistossa ei ole päivityspäivää. Skripti `tyokalut/haku/hae_orvot_laajennukset.py`
hakee kauppasivulta "Updated"-päivän ja nykyisen käyttäjämäärän ositetulle otokselle
(130 per luokka). Tulos: ks. kohta 1b, täydennetään kun ajo valmistuu.

### Mobiilisovellukset

Pixalate Q3 2024 (FACT, toissijainen lähde, Pixalaten oma raportti): **1 014 000 hylättyä
sovellusta** (ei päivitystä 2 vuoteen), joista App Store 682 k, Google Play 332 k, 4,3 M
sovelluksen aineistosta. **160 000 hylättyä sovellusta saa yhä ohjelmallista mainosrahaa,
arviolta 53 M USD vuosineljänneksessä.** Google Play poisti 2024 - 2025 noin 1,6 M
sovellusta laatuvaatimusten takia (TechCrunch 2025-04, Appfiguresin data).

Tämä on ainoa omaisuusluokka, jossa on mitattu **rahaa, joka virtaa hylättyyn omaisuuteen
ilman ylläpitäjää**: 53 M USD / neljännes / 160 k sovellusta = keskimäärin 330 USD per
sovellus per neljännes (CALC, jakauma varmasti erittäin vino).

### "Looking for maintainer" GitHubissa

FACT: 1 066 avointa ja 1 242 suljettua issuea, joiden otsikossa on "looking for
maintainer(s)" tai vastaava (GitHub search 2026-09-16). Top 100 reaktioiden mukaan:
`data/orvot/maintainer-wanted-avoimet-top100.csv`. Aliagentti luokittelee, pyytävätkö
omistajat rahaa ja mitä suljetuissa tapauksissa tapahtui. Tulos kohdassa 3.

## 2. Voiko omistajuuden siirtää laillisesti

| Alusta | Siirto | Mitä säilyy | Kitka | Lähde |
|---|---|---|---|---|
| Chrome Web Store | Kyllä, tukilomake, alkuperäinen omistaja vahvistaa sähköpostilla | Sama laajennus-ID, kaikki käyttäjät, asetukset. Käyttäjille **ei ilmoiteta** | Enintään 7 pv, vastaanottajalla 5 USD kehittäjämaksu | Secure Annex 2025-03 (FACT, kokeiltu käytännössä) |
| App Store | Kyllä, App Store Connect | Bundle ID, arvostelut, arviot, käyttäjät saavat päivitykset | iCloud-kontit, Game Center, Wallet-passit, push-sertifikaatit uusiksi | Apple-dokumentaatio (FACT) |
| Google Play | Kyllä, tukipyyntö | Sovellus, käyttäjät | Molemmilla 25 USD tili + transaktio-ID, ~48 h | Play Console Help (FACT) |
| npm | **Ei nimen kaappausta.** Omistaja voi lisätä ylläpitäjän. npm ei siirrä nimiä pyynnöstä | - | Vain tavaramerkkiriita | npm dispute policy (FACT) |
| PyPI | Omistaja lisää omistajan; PEP 541 -prosessi hylätyille nimille (hidas) | - | - | (muistista, INFERENCE) |
| GitHub-repo | Kyllä, transfer | Tähdet, issuet, uudelleenohjaus | - | (FACT, yleistieto) |

**Johtopäätös: siirto on laillista ja helppoa kaikilla käyttäjäalustoilla.** Chrome-
laajennuksen siirto on niin helppoa ja näkymätöntä, että se on tietoturvaongelma, ei
markkinakitka.

## 3. Pyytävätkö omistajat rahaa vai haluavatko eroon vastuusta

**Laajennukset (FACT, Secure Annex 2025-03-18):** extensionhub.io-markkinapaikalla on
listattu laajennuksia "400 000 käyttäjää 100 000 USD" (0,25 USD/käyttäjä) ja "5 käyttäjää
50 USD". Tutkija tarjosi 50 USD 8 käyttäjän laajennuksesta; kun kansainvälinen maksu
osoittautui hankalaksi, **kehittäjä siirsi laajennuksen ilmaiseksi**. Tutkijan sanoin:
"I wonder how many other extensions have been given away just to relieve a burden."
Samassa artikkelissa: 400 k käyttäjän adblockerin omistaja vaihtui 2024-12-14, ja
2025-01-01 uusi versio alkoi kerätä evästeotsakkeita ja klikkivirtaa.

**Micro-SaaS-markkinapaikka Microns.io (FACT, 2026-09-16, julkiset listaukset):**

| Listaus (laajennukset) | Vuositulo USD | Hintapyyntö USD | Kerroin |
|---|---|---|---|
| Prompt optimizer | 4 141 | 12 000 | 2,9x |
| Reddit post optimizer | 300 | 1 999 | 6,7x |
| TikTok unfollow | 15 | 1 000 | 67x |
| Text-to-prompt | 1 440 | 10 000 | 6,9x |
| Audio equalizer | 12 000 | 100 000 | 8,3x |
| LinkedIn outreach | 21 400 | 77 000 | 3,6x |
| ChatGPT UX | 54 200 | 230 000 | 4,2x |
| Tinder swipe | 32 000 | 110 000 | 3,4x |
| Audio recorder | 720 | 5 000 | 6,9x |

Kaikki 39 luettua listausta (alle 5 k, alle 10 k, laajennukset, etusivu): mediaanikerroin
noin **5x vuositulo**, ja alle 500 USD:n vuositulolla lähes aina hintalattia 1 000 USD.
Myydyt (6 kpl): 1,7x - 8,6x. Vertailu: keskikokoinen SaaS myydään 2 - 4x tuloa
(toissijaiset lähteet, ei varmennettu).

**Tämä on ensimmäinen falsifiointi.** Listatut pienet omaisuudet **eivät ole halpoja**;
ne ovat suhteessa tuloonsa kalliimpia kuin isot. Markkinapaikka hinnoittelee optioarvoa
ja myyjän vaivaa, ei ylläpidon kustannusta. Markkinavirhettä ei ole siellä, missä on
markkina. Jos sitä on, se on **listaamattomassa** omaisuudessa: laajennuksissa, joita
annetaan pois ilmaiseksi, ja projekteissa, joiden omistaja kirjoittaa "looking for
maintainer" -issuen.

**GitHub-issuet:** aliagentin luokittelu, täydennetään.

## 4. Miksi hylätty, ja mitä ylläpito oikeasti vaatii

Todellinen mittaus: `kokeet/02-yllapitokoe-html5lib.md` (aliagentti, 25 min aikaraja,
html5lib 30 M latausta/kk, viimeinen julkaisu 2017). Täydennetään.

## 5. Kuka jo tekee tätä: HeroDevs

FACT (PSG 2025-07, SiliconANGLE 2025-07-24, herodevs.com/pricing): HeroDevs myy
"Never-Ending Support" -tukea elinkaarensa päähän tulleille avoimen lähdekoodin
projekteille (AngularJS, Vue 2, Bootstrap 3, Node.js-vanhat, jQuery, Django-vanhat,
Drupal 7, 50+ muuta). **1 000+ asiakasyritystä, lähes puolet Fortune 100:sta**, 125 M USD
kasvusijoitus PSG:ltä heinäkuussa 2025, 20 M USD rahasto alkuperäisille ylläpitäjille.
Hinta "custom, billed annually".

**Tämä on todiste siitä, että orpo-ohjelmiston ylläpidosta maksetaan.** Mutta maksaja ei
ole käyttäjä vaan **yritys, jolla on compliance-velvoite** (haavoittuvuudet EOL-koodissa
ovat auditointilöydös). Ja HeroDevsin vallihauta ei ole koodi vaan **alkuperäisten
ylläpitäjien siunaus ja rahoitus**: se maksaa projekteille, jotta se saa olla "virallinen"
jatkaja. Niukka resurssi on jälleen luottamus, ei työ.

## 6. Red team: miksi näitä ei jo osteta

**Niitä ostetaan. Ostajat ovat pääosin haitallisia.** Tämä on yön tärkein vastanäyttö.

- FACT: event-stream 2018: ylläpitäjä luovutti npm-oikeudet tuntemattomalle, joka lisäsi
  bitcoin-varkaan (2 M latausta/viikko).
- FACT: xz-utils 2024: monivuotinen sosiaalinen manipulointi yksinäistä, uupunutta
  ylläpitäjää vastaan, takaovi lähes kaikkiin Linux-jakeluihin. OpenSSF ja OpenJS
  julkaisivat varoituksen: "unknown individuals aggressively pursuing maintainer roles".
- FACT: polyfill.io 2024: domain ja projekti myytiin kiinalaiselle Funnullille, joka
  alkoi syöttää haittakoodia 100 000+ sivustolle.
- FACT: Chrome-laajennukset 2024 - 2025: Cyberhaven ja kymmenet muut; Secure Annexin
  seuraamat omistajanvaihdokset, joita seuraa datankeruu; 18 laajennusta, 2,3 M käyttäjää
  yhdessä kampanjassa (GitLab Threat Intel 2025-02); 4,3 M käyttäjää (Register 2025-12).

Seuraukset legitiimille ostajalle:

1. **Hinta on jo asetettu, ja sen asettaa haitallinen käyttö.** 0,25 USD/käyttäjä
   pyyntönä adblockerista on hinta, jonka datankerääjä maksaa. Legitiimi ansainta
   (freemium 0,5 % konversio × 3 USD/kk) ei kilpaile sen kanssa.
2. **Jokainen omistajanvaihdos näyttää hyökkäykseltä.** Turvallisuusyhteisö skannaa
   omistajanvaihdoksia nimenomaan uhkasignaalina (Secure Annex, LayerX, Koi). Uusi
   ylläpitäjä ilman historiaa on xz-kuvio. Kaikki, mikä tekisi meistä tehokkaita
   (uusi tili, tekoälyn tekemät commitit, nopea tahti), on täsmälleen se profiili, jota
   varoitetaan.
3. **Käyttäjät eivät maksa.** npm-lataajat ovat koneita. Laajennusten käyttäjät saivat
   tuotteen ilmaiseksi. Muutos maksulliseksi on juuri se, mikä saa käyttäjät lähtemään
   ja jättämään yhden tähden arvosteluja.
4. **Omistajan kustannus ei ollut koodi.** Kehittäjä, joka antaa laajennuksen pois
   ilmaiseksi, ei tee sitä koska koodaaminen on kallista, vaan koska **vastuu, tuki,
   alustan säännöt ja huomio** ovat kalliita. Tekoäly laskee koodin hintaa. Se ei
   laske vastuun hintaa. Tämä on lähtöhypoteesin toinen korjaus.

## 7. Mitä jää niukaksi, kun koodi on ilmaista

Kaikki kuusi kohtaa palautuvat samaan: **kyky kantaa vastuu uskottavasti**. HeroDevs myy
sitä. Alkuperäinen ylläpitäjä antoi sen pois. Haitallinen ostaja väärinkäyttää sitä.
Käyttäjä ei huomaa sitä ennen kuin se puuttuu.

INFERENCE: Kysymys "mikä oli arvotonta, koska se vaati työtä" on väärin muotoiltu tälle
omaisuusluokalle. Oikea muoto: **"mikä oli arvotonta, koska se vaati vastuuta, jota
kukaan ei halunnut kantaa ilmaiseksi"**. Tekoäly ei muuta sitä suoraan. Se muuttaa sitä
epäsuorasti: jos yksi ihminen voi tekoälyn kanssa kantaa vastuun kymmenestä pienestä
asiasta yhden sijaan, vastuun yksikköhinta laskee. Se on eri mekanismi kuin "ylläpito
halpenee", ja se on mitattavissa: montako asiaa yksi ihminen voi uskottavasti vastata.

## 8. Tuomio (välitila, täydennetään yön aikana)

- Omaisuutta on paljon (FACT): 1 M+ hylättyä sovellusta, ~10 k laajennusta yli 10 k
  käyttäjällä (osuus hylättyjä mitataan), 1/3 npm-ytimestä ilman julkaisuja.
- Siirto on laillista ja helppoa (FACT).
- Omistajat antavat pois ilmaiseksi (FACT, n pieni) tai pyytävät listatuilla markkinoilla
  yli 5x tuloa (FACT).
- Rahaa virtaa hylättyyn omaisuuteen: mainosraha (53 M USD/nelj. 160 k sovellukseen) ja
  compliance-tuki (HeroDevs, 1 000+ yritystä).
- **Markkinavirhe ei ole "ylläpito on kallista".** Se on "vastuu on kallista ja
  luottamus on hidasta". Tekoäly ei poista kumpaakaan. Se voi vain tehdä yhdestä
  ihmisestä vastuullisen useammasta asiasta.
- Mekanismi legitiimille toimijalle on **julkinen, todennettava jatkajuus**: avoin
  lähdekoodi, allekirjoitetut julkaisut, alkuperäisen ylläpitäjän siunaus, julkinen
  loki. Se on hidas ja se on täsmälleen sama niukka resurssi (todennettu historia),
  jonka niukkuuskartta jo nimesi. HeroDevs teki siitä 125 M USD:n yhtiön.
