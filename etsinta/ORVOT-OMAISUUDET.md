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
| Orpoja 5 000 ladatuimmasta | **1 674 (33,5 %)** | **959 (19,2 %)**, varmennettu PyPI:stä (ecosyste.ms sanoi 1 116) |
| Orpojen osuus latauksista | **30,0 %** (211 mrd/kk) | 8,1 % (11,6 mrd/kk) |
| Viimeinen julkaisu yli 5 v sitten | 802 | 347 |
| Yksi ylläpitäjä | 1 042 | 717 |
| Tunnettu haavoittuvuus (advisory) | 99 | 21 |
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
haki kauppasivulta "Updated"-päivän ja nykyisen käyttäjämäärän ositetulle satunnais-
otokselle, 130 laajennusta per luokka (tammikuun 2025 käyttäjämäärän mukaan). Tulos
`data/orvot/cws-otos-390.json` (CALC, FACT-sivuista 2026-09-16):

| Luokka (käyttäjiä 2025-01) | n | Poistettu kaupasta | Elossa | Orpo 2 v | Orpo 1 v | Käyttäjämuutos, orvot | Käyttäjämuutos, päivitetyt |
|---|---|---|---|---|---|---|---|
| 10 k - 100 k | 130 | 36 (28 %) | 94 | 41 (44 %) | 54 | 0 % (mediaani) | 0 % |
| 100 k - 1 M | 130 | 28 (22 %) | 102 | 33 (32 %) | 47 | 0 % | 0 % |
| 1 M+ | 130 | 27 (21 %) | 103 | 19 (18 %) | 38 | **-60 %** (n=37) | 0 % (n=63) |

- **23 % laajennuksista, joilla oli yli 10 000 käyttäjää tammikuussa 2025, on poistettu
  kaupasta 20 kuukaudessa.** Niillä oli yhteensä 98 M käyttäjää (mediaani 100 k).
  Ajoitus sopii Manifest V2 -poistoon: Chrome esti MV2-laajennukset heinäkuussa 2025 ja
  poisti listaukset 2026-08-31 (FACT, developer.chrome.com). Osuus MV2:sta on INFERENCE,
  aineistossa ei ole manifest-versiota.
- Elossa olevista 31 % ei ole päivitetty 2 vuoteen. Yhteensä 160 M käyttäjää, mutta
  kärki on yritysten "valmiita" laajennuksia (Google Drive Launcher 94 M, Webex 22 M,
  Zoom 6 M, Google Drawings vuodelta 2015). Sama valmis ≠ hylätty -ilmiö kuin npm:ssä.
- **Orvot menettävät käyttäjiä vain suurimmassa luokassa.** Yli miljoonan käyttäjän
  laajennukset ilman päivitystä vuoteen: mediaanimuutos -60 %. Pienemmissä luokissa
  kaupan pyöristys (10 k, 100 k) piilottaa muutoksen. Käyttäjät siis lähtevät hitaasti,
  eivät heti.
- Ekstrapolaatio koko aineistoon (CALC, karkea): 9 640 laajennusta yli 10 k käyttäjällä
  → noin 2 200 poistettu, 7 400 elossa, joista noin 2 300 orpoa (2 v). Yksityis-
  henkilöiden osuutta ei mitattu.

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
`data/orvot/maintainer-wanted-avoimet-top100.csv`. 40 avointa + 40 suljettua luettu
kokonaan kommentteineen: `data/orvot/maintainer-wanted-luokittelu-80.md`. Tulos kohdassa 3.

### WordPress.org-lisäosat (julkinen rajapinta, 10 000 suosituinta)

Skripti `tyokalut/haku/hae_orvot_wordpress.py`, data `data/orvot/wordpress-orvot-top10000.csv`
(CALC, FACT-rajapinnasta 2026-09-16):

| | |
|---|---|
| Ei päivitystä 2 v | **2 354 (23,5 %)**, yhteensä 8,47 M aktiivista asennusta |
| Ei päivitystä 3 v | 1 872 (18,7 %), 5,67 M asennusta |
| Orpoja, joilla yli 10 k asennusta | **166**, joista 153 yksityishenkilön tai pienen tekijän (3,84 M asennusta) |
| Orpoja, joilla yli 100 k asennusta | 8 |
| Orpoja, joilla hakemiston varoitus "ei testattu 3 viimeisellä pääversiolla" | 2 353 / 2 354 |
| Virallinen luovutuskanava, tagi "adopt-me" | **17 lisäosaa, 3 210 asennusta yhteensä** |

WordPress on paras aineisto, koska asennukset ovat oikeita sivustoja (ei koneita) ja
omistajat ovat usein yksityishenkilöitä. Ja siinä on valmis luonnollinen koe:
**`limit-login-attempts`** (Automattic, 300 k asennusta, viimeinen päivitys 2023-04) vs.
sen haarautuma **`limit-login-attempts-reloaded`** (WPChef, lisätty 2016, 1 M+ asennusta,
päivitetty 2026-09-10, maksullinen pilvitaso). Sama kuvio: `search-and-replace` (WP Media,
100 k, orpo) vs. `better-search-replace` (WP Engine, 1 M). **Käyttäjät siirtyivät
haarautumaan ilman omistajanvaihdosta.** Hakemisto, ei omistaja, hallitsee käyttäjiä.

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

**GitHub-issuet (FACT, 40 avointa + 40 suljettua luettu kokonaan):**

| | Avoimet (n=40) | Suljetut (n=40) |
|---|---|---|
| Omistaja pyysi rahaa | 1 (poetry2nix: "open for contract work" yhtenä vaihtoehtona) | 0 |
| Omistaja tarjosi myyntiä | 0 | 0 |
| Omistaja tarjosi luovutusta ilmaiseksi | 35 | - |
| Vapaaehtoisia ilmoittautui | 38 (mediaani ~6 henkilöä) | - |
| Pääsy oikeasti annettu | 18 (+2 osittaista) | 31 uusi ylläpitäjä |
| Uusi ylläpitäjä aiempi contributor / ulkopuolinen | 12 / 6 | 12 / 13 (+6 sekatiimi) |
| Käyttäjät tarjosivat rahaa | 6 | 15 ketjussa raha esillä |
| Raha johti mihinkään | 0 | 0 |
| Omistaja mainitsi luottamuksen/vetoamisen | 5 | 5 |
| xz tai event-stream mainittu | 0 | 0 |
| Repo aktiivinen 12 kk sisällä | 22 | 32 |

Havainnot:
- **Omistajat eivät halua rahaa, he haluavat eroon vastuusta.** 1/80 pyysi rahaa, 0/80
  myi. Kolme torjui rahan nimenomaisesti ("my bottleneck really isn't money").
- **Vapaaehtoisia on enemmän kuin luovutuksia.** Yleisin malli on "aloita PR:illä,
  katsotaan kuukauden päästä" (14/40), ja se kynnys jää usein ylittämättä. Pullonkaula
  on omistajan huomio ja luottamus, ei tarjonta.
- **Ulkopuolinen onnistuu, kun se on yritys tai tunnettu hahmo, tai kun se teki ensin
  forkin/PR:t.** Suljetuissa 13/31 uusista ylläpitäjistä oli ulkopuolisia, näistä 5
  yrityksiä (Software Mansion ×2, Quantstack, antfu, Infinite Red).
- **Yhteisöfork korvasi alkuperäisen 9/40 avoimessa tapauksessa** (eslint-plugin-node →
  eslint-plugin-n, kafkajs → charon, razzle → dazzle). Sama kuin WordPressissä.
- **Uusi ilmiö 2026:** sama LLM-tyylinen vapaaehtoisboilerplate ("issue triage and
  reproduction… earn trust progressively", "maintenance lane") postattiin samana päivänä
  kuuteen otoksen repoon samalta tililtä; yhdessä ketjussa käyttäjät kysyivät, onko
  kyseessä botti. **Tekoälypohjainen "otan ylläpidon" -tarjous on jo spämmiä**, ja se
  laskee jokaisen uuden tarjoajan uskottavuutta. Meidän suunnittelemamme lähestymistapa
  on siis jo kilpailtu ja jo epäluulon kohde.

## 4. Miksi hylätty, ja mitä ylläpito oikeasti vaatii

**Miksi hylätty (FACT, 80 issuen otos):** siirtynyt muuhun tekniikkaan tai ei käytä
itse 13, ei aikaa (työ, perhe) 11, omistaja kokonaan kadonnut 5, uusi työ 2, burnout 2,
kuolema tai terveys 2, yhtiö lopetti resursoinnin 1. Ei yhtään "ylläpito on liian
kallista". Syy on elämä, ei kustannus.

**Mitä ylläpito vaatii, mitattu:** `kokeet/02-yllapitokoe-html5lib.md`. html5lib
(PyPI, viimeinen julkaisu 2020-06, master 2024-02, 80 avointa issuea, 20 avointa PR:ää).
Tulos 9 minuutissa ja 82 000 tokenilla:
- 17 499 testiä vihreänä Python 3.14:llä. Rikki oli vain pakkausinfra (`pkg_resources`,
  `ast.Str`), korjaus 13 sekuntia komentoaikaa.
- **Sama korjaus oli jo kolmessa avoimessa, mergeable-tilaisessa PR:ssä** (2025-09,
  2026-02, 2026-03). Tekoälyn lisäarvo koodissa oli nolla.
- "Please make a new release" -issue avoinna 2024-01 lähtien, 9 kommenttia, ei vastausta
  oikeuksien haltijalta. Tietoturvatutkijan SECURITY.md-pyyntö vastaamatta.
- 15 issuen otanta: 47 % tekoäly korjaa yksin, 40 % vaatii ihmisen suunnittelupäätöksen,
  13 % vanhentunut. **100 % tekoälyn korjauksista on hyödyttömiä ilman julkaisuoikeutta.**
- Yhteisö kiersi ongelman forkilla: `html5lib-modern` 1.2 PyPI:ssä 2024-09.
- Jatkuva ylläpito tekoälyllä: 0,2 - 0,6 M tokenia/kk (kympeistä kymmeniin euroihin).
  Ihmisen 1 - 3 h/kk merge-, julkaisu-, tietoturva- ja suunnittelupäätöksiin on ainoa
  niukka osa.

**Johtopäätös:** orpojen pakettien ylläpito ei ole tekoälylle koodiongelma vaan
pääsyongelma. Tuote ei ole patchi vaan luotettu ihminen, jolla on oikeudet ja agentti.

**Datan laatuhuomio:** ecosyste.ms:n julkaisupäivä oli PyPI:ssä vanhentunut 11/30
satunnaisotoksessa (7/30 ei enää orpo), npm:ssä 1/30. Kaikki 1 116 PyPI-orpoa varmennettiin
PyPI:n omasta rajapinnasta: 959 (86 %) oli yhä orpoja, taulukon PyPI-luvut on korjattu.
npm-luvut ovat ecosyste.ms:n, otosvirhe 1/30. html5lib:n oikea viimeinen
julkaisu on 2020-06-22, ei 2017-12.

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

## 8. Tuomio

- Omaisuutta on paljon (FACT): 1 M+ hylättyä sovellusta, noin 2 300 elossa olevaa
  orpolaajennusta yli 10 k käyttäjällä (ekstrapolaatio 390 otoksesta), 2 354 orpoa
  WordPress-lisäosaa 8,5 M asennuksella, 1/3 npm-ytimestä ilman julkaisuja (pääosin valmiita).
- Siirto on laillista ja helppoa (FACT).
- Omistajat antavat pois ilmaiseksi (FACT, 80 issuen otos: 1 pyysi rahaa, 0 myi) tai
  pyytävät listatuilla markkinoilla yli 5x tuloa (FACT, 39 listausta).
- Hakemisto omistaa käyttäjät: 40 % yli 10 k asennuksen WordPress-orvoista on jo korvattu
  ylläpidetyllä haarautumalla (FACT, `data/orvot/wordpress-orvot-korvaajat.csv`), ja
  html5lib:n käyttäjät siirtyivät `html5lib-modern`-forkkiin. Fork-kaista täyttyy ilman meitä.
- Rahaa virtaa hylättyyn omaisuuteen: mainosraha (53 M USD/nelj. 160 k sovellukseen) ja
  compliance-tuki (HeroDevs, 1 000+ yritystä).
- **Markkinavirhe ei ole "ylläpito on kallista".** Se on "vastuu on kallista ja
  luottamus on hidasta". Tekoäly ei poista kumpaakaan. Se voi vain tehdä yhdestä
  ihmisestä vastuullisen useammasta asiasta.
- Mekanismi legitiimille toimijalle on **julkinen, todennettava jatkajuus**: avoin
  lähdekoodi, allekirjoitetut julkaisut, alkuperäisen ylläpitäjän siunaus, julkinen
  loki. Se on hidas ja se on täsmälleen sama niukka resurssi (todennettu historia),
  jonka niukkuuskartta jo nimesi. HeroDevs teki siitä 125 M USD:n yhtiön.
