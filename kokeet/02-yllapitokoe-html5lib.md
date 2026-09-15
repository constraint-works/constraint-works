# Koe 02: Ylläpitokoe – html5lib-python

Mittaus 2026-09-16 klo 01:26–01:35 EEST, kokonaiskesto n. 9 min seinäkelloaikaa (komentoaikaa 5 min, loput agentin päättelyä). Budjetti oli 25 min; työ valmistui ennen sitä. Kaikki työ tehtiin scratchpad-hakemistossa; mitään ei pushattu, ei avattu PR:iä, ei otettu yhteyttä kehenkään. Patchi on tallessa: `scratchpad/ylläpitokoe/fix_pkg_resources_ast_str.patch`.

Merkinnät: **FACT** = mitattu/luettu lähteestä, **CALCULATION** = laskettu FACT-luvuista, **INFERENCE** = päättely, **UNKNOWN** = ei saatu selville.

## Tavoite

Mitata empiirisesti, kuinka suuren osan hylätyn mutta laajasti käytetyn avoimen lähdekoodin paketin todellisesta ylläpitotyöstä AI-agentti pystyy tekemään yksin, ja mikä jää jäljelle, mitä se ei voi tehdä.

## Kohde (faktat lähteineen)

**Korjaus lähtöoletukseen.** Tehtävänannossa sanottiin "viimeisin PyPI-julkaisu 2017-12". Se on väärin: `html5lib 1.1` julkaistiin PyPI:hin **2020-06-22** (FACT, `pypi.org/pypi/html5lib/json`). Versio 1.0.1 on joulukuulta 2017. "Hylätty" pitää silti paikkansa alla olevin mittarein.

| Mittari | Arvo | Luokka | Lähde |
|---|---|---|---|
| Viimeisin PyPI-julkaisu | 1.1, 2020-06-22 (wheel `py2.py3-none-any` + sdist) | FACT | PyPI JSON |
| Viimeisin commit `master`-haaraan | 2024-02-21 (Ł. Langa, "Constant phases #567") | FACT | `git log` |
| Repo `pushed_at` | 2026-04-21 (dependabot-haara, ei master) | FACT | `gh api repos/...` |
| Arkistoitu | ei | FACT | `gh api` |
| Tähtiä | 1 223 | FACT | `gh api` |
| Avoimia issueita (ilman PR:iä) | 80 | FACT | `gh api issues?state=open` |
| Avoimia PR:iä | 20 | FACT | `gh api pulls?state=open` |
| Vanhin avoin PR | #38, 2013-05-04 | FACT | `gh api` |
| Uusin avoin PR | #603, 2026-09-08 | FACT | `gh api` |
| "Please make a new release" -issue | #577, avattu 2024-01-24, avoinna, 9 kommenttia | FACT | `gh api issues/577` |
| PyPI-metadatan maintainer | James Graham, (sähköposti poistettu) | FACT | PyPI JSON |
| PyPI-omistajatilit | ei saatu (pypi.org-sivun scrape epäonnistui) | UNKNOWN | – |
| Kuka teki 1.1-julkaisucommitin | Sam Sneddon (gsnedders), 2020-06-23 | FACT | `git log` |
| Latauksia / kk | ~30 M oli tehtävänannon oletus; pypistats vastasi HTTP 429, ClickPy ei vastannut | UNKNOWN | – |
| Python 3.14 -tuki | ei: `setup.py` kaatuu (`ast.Str` poistettu) | FACT | tämä koe |
| Rakentuu uusimmalla setuptoolsilla (84.0.0) | ei: `pkg_resources` poistettu setuptools ≥ 81 | FACT | tämä koe |
| `python_requires` | `>=2.7, !=3.0–3.4` (Python 2 yhä tuettu paperilla) | FACT | setup.py |
| Testiriippuvuus `pytest-expect` | ylläpitämätön vuodesta 2016 | FACT | issue #538 |
| CI viimeiset ajot masterissa | 2026-04: 1 success, 2 failure (dependabot pytest-päivitys) | FACT | `gh api actions/runs` |

**Turvallisuustiedotteet** (FACT, `gh api /advisories?ecosystem=pip&affects=html5lib`):

| GHSA | Vakavuus | Haavoittuva alue | Tila |
|---|---|---|---|
| GHSA-v9v9-xffq-rwr4 | medium | < 0.999999999 (2016) | korjattu julkaistussa 1.1:ssä |
| GHSA-8f6m-gfq9-g33v | medium | < 0.99999999 (2016) | korjattu julkaistussa 1.1:ssä |

Ei yhtään julkaisematonta tietoturvakorjausta masterissa (FACT). Sen sijaan issue #584 (2024-10) pyytää `SECURITY.md`-tiedostoa, koska tutkijalla on ilmoitettava löydös eikä kanavaa – kukaan ei ole vastannut (FACT).

**Haarautuma:** `html5lib-modern` 1.2 julkaistu PyPI:hin 2024-09-25, `requires_python >= 3.8` (FACT, PyPI JSON). Yhteisö on siis jo kiertänyt julkaisuoikeuksien puutteen forkilla.

## Mitä tehtiin (ajastetut vaiheet)

Ajat ovat kumulatiivista komentoaikaa kokeen alusta (FACT, `date`-leimat).

| # | Vaihe | Kesto | Tulos |
|---|---|---|---|
| 1 | Klooni (depth 50), PyPI-, repo-, PR- ja advisory-haut | 0:00–0:31 | ks. Kohde |
| 2a | venv (Python 3.14.6) + `pip install -e . -r requirements-test.txt` | 0:31–0:34 | **EPÄONNISTUI**: `ModuleNotFoundError: pkg_resources` build-ympäristössä (setuptools 84.0.0) |
| 2b | Kierto: testiriippuvuudet suoraan, `pytest` ilman asennusta | 0:34–1:13 | **EPÄONNISTUI**: `conftest.py` importtaa `pkg_resources`; lisäksi testidata-submoduuli puuttui |
| 2c | Submoduuli (`--depth 1`), `setuptools<81` pinnattu → baseline-testiajo | 1:13–1:47 | 17 499 passed, 0 failed, 15 885 skipped, 683 xfailed, 9,5 s |
| 3 | Korjaus: `pkg_resources` pois `setup.py`:stä ja `conftest.py`:stä, `ast.Str` → `ast.Constant`; verifiointi setuptools 84:llä + testit + wheel-build | 2:30–3:17 (itse korjaus **13 s** komentoaikaa, n. 1 min päättelyineen) | `pip install -e .` OK, 17 499 passed, wheel rakentuu |
| 4 | Vertailu avoimiin PR:iin, omistaja- ja latausluvut, 15 issuen otanta | 3:17–5:00 | ks. Tulokset |
| 5 | Raportin kirjoitus | 5:00–~9:00 | tämä tiedosto |

Vaiheessa 3 tehdyn patchin sisältö (FACT, `git diff --stat`: 2 tiedostoa, +28/−65):
- `setup.py`: poistettu `pkg_resources`-importit ja koko `_markerlib`/`MarkerEvaluation`-kiertotie (tarkoitettu setuptools < 18.5:lle, v. 2015); `isinstance(a.value, ast.Str)` → `ast.Constant` + `str`-tarkistus.
- `html5lib/tests/conftest.py`: `pkg_resources.Requirement/working_set/evaluate_marker` korvattu `importlib.metadata` + `packaging`-kirjastolla (pytestin oma riippuvuus) apufunktiossa `_requirement_satisfied`. `--update-xfail`-polku testattu: raportoi oikein "Need genshi>=0.7.1".

## Tulokset (numerot)

**Testisuite Python 3.14.6:lla**

| Tila | passed | failed | skipped | xfailed | aika | luokka |
|---|---|---|---|---|---|---|
| Ennen korjausta, setuptools 84 | – | – | – | – | ei käynnisty (collection error) | FACT |
| Ennen korjausta, setuptools 80.10 | 17 499 | 0 | 15 885 | 683 | 9,5 s | FACT |
| Korjauksen jälkeen, setuptools 84 | 17 499 | 0 | 15 885 | 683 | 8,1 s | FACT |

Skipatut 15 885 ovat lxml/genshi-puurakentajien testejä, joita ei asennettu (INFERENCE markkereista). Itse kirjasto on siis **täysin terve** modernilla Pythonilla; rikki on vain pakkaus- ja testi-infra (FACT).

**Kuka kärsii rikkinäisestä buildista?** PyPI:n 1.1 sisältää universaalin wheelin, joten tavallinen `pip install html5lib` toimii yhä (FACT). Rikki ovat: asennus gitistä/sdististä, distrojen paketointi (Fedora/Debian/NixOS – PR:ien tekijät hroncok, hrnciar, Mic92, loqs ovat distropaketoijia, INFERENCE käyttäjänimistä) ja jokainen, joka rakentaa lähteestä Python 3.14:llä.

**Ratkaiseva havainto: korjaukseni oli jo olemassa – kolmesti.**

| Avoin PR | Päiväys | Sisältö | Reviewt | Mergeable |
|---|---|---|---|---|
| #589 | 2025-09-13 | `ast.Str` → Python 3.14 | 0 | kyllä |
| #592 | 2026-02-09 | `pkg_resources` puuttuu → setup.py | 3 | kyllä |
| #594 | 2026-03-16 | `pkg_resources` pois setup.py + conftest | 0 | kyllä |
| #600 | 2026-06-29 | pytest ≥ 9.1 -yhteensopivuus | 0 | kyllä |

(FACT, `gh pr view`.) Sama pätee chardet-varoitukseen: issue #601 ja kaksi PR:ää (#602, #603). AI:n marginaalinen lisäarvo *koodin* tuottamisessa oli tässä tapauksessa nolla – yhteisö oli tehnyt saman 6–12 kk aiemmin. Puuttuva resurssi on merge- ja julkaisuoikeus, ei koodi.

**15 issuen otanta** (FACT: numerot, otsikot, päiväykset; INFERENCE: luokitus). Luokat: (a) AI korjaa yksin, (b) vaatii ihmisen suunnittelupäätöksen, (c) vaatii julkaisuoikeudet, (d) vanhentunut/epäkelpo.

| Issue | Vuosi | Otsikko (lyh.) | Luokka | Huom. |
|---|---|---|---|---|
| #601 | 2026 | chardet.universaldetector deprecation | a (+c) | PR:t #602/#603 valmiina |
| #588 | 2025 | ast.Str poistettu Py3.14 | a (+c) | korjattu tässä kokeessa; PR #589 valmiina |
| #584 | 2024 | Create SECURITY.md | b | tarvitsee ihmisen vastaanottamaan haavoittuvuusilmoituksia |
| #538 | 2021 | pytest-expect ylläpitämätön | a (+c) | korvattavissa xfail-listalla, iso mekaaninen muutos |
| #450 | 2020 | Testaa narrow-UCS2 Py2.7 | d | Python 2 EOL |
| #434 | 2020 | Prescan-bugi: toinen charset | a (+c) | spec-pohjainen bugikorjaus + testi |
| #368 | 2017 | refactor support.py | d | "en tiedä mitä pitäisi refaktoroida" |
| #338 | 2017 | lxml-serialisoija menee elementin ohi | b | 13 kommenttia, API-käyttäytymisen valinta |
| #266 | 2016 | defusedxml-dokumentaatio | a (+c) | dokumentaatio |
| #200 | 2015 | Tyyppistubit + mypy | b | typing-strategian valinta |
| #152 | 2014 | CSS-sanitoija oikealla parserilla | b | uusi riippuvuus, tietoturvakriittinen |
| #107 | 2013 | Paremmat virheilmoitukset | a (+c) | |
| #87 | 2013 | Rivi/sarake tokeneihin | b | API-suunnittelu |
| #73 | 2013 | xml:lang ei käsitellä | a (+c) | spec-pohjainen |
| #56 | 2013 | Päivitä nykyiseen parser-speciin | b | jatkuva, laaja; vaatii omistajan linjauksen |

Jakauma (CALCULATION): **a = 7/15 (47 %)**, **b = 6/15 (40 %)**, **d = 2/15 (13 %)**. Luokka (c) ei ole vaihtoehto vaan kerros: **kaikki 7 a-luokan korjausta (100 %) ovat hyödyttömiä käyttäjille ilman julkaisua**, ja julkaisu on ollut jumissa 2024-01 lähtien (#577). Avoimet issuet painottuvat vanhoihin: 10/15 otannasta on vuosilta 2013–2017 (FACT).

**Tämän kokeen kulutus** (FACT konteksti-laskurista, ±10 %): n. 82 000 tokenia, 9 min seinäkelloa, 1 patch (+28/−65 riviä), 0 pushia.

## Mitä AI ei voinut tehdä

Jokainen kohta on tila, jossa työ pysähtyi tai olisi pysähtynyt riippumatta agentin kyvykkyydestä:

1. **Mergetä mihinkään.** 20 mergeable-tilassa olevaa PR:ää odottaa henkilöä, jolla on write-oikeus `html5lib`-organisaatioon. AI voi tuottaa 21:nnen (FACT: PR:t; INFERENCE: oikeudet).
2. **Julkaista PyPI:hin.** Vaatii PyPI-projektin omistaja-/maintainer-tilin, 2FA:n (pakollinen PyPI:ssä) ja joko API-tokenin tai trusted publishing -konfiguraation GitHub Actionsiin. Repo:ssa ei ole julkaisu-workflowta (FACT: `.github/workflows/` sisältää vain `python-tox.yml`). Omistajatilit: UNKNOWN; metadatan maintainer James Graham, 1.1:n julkaisi gsnedders.
3. **Saada oikeuksia.** Oikeuksien siirto vaatii nykyisen omistajan aktiivisen toimen tai PyPI:n PEP 541 -prosessin (ihmisten välinen, kuukausia). Ei ole "maintainer wanted" -issuea (FACT: haku `maintainer in:title` → vain suljettu #444 vuodelta 2020); on vain #577 "Please make a new release", johon kukaan oikeuksien haltija ei ole vastannut (FACT: kommentoijat ovat ulkopuolisia).
4. **Toimia tietoturvakontaktina.** #584: tutkija haluaa ilmoittaa löydöksen. Vastaanotto, embargo, CVE-koordinointi ja korjausjulkaisu vaativat ihmisen, jolla on sekä oikeudet että vastuu.
5. **Tehdä design-päätöksiä omistajan puolesta.** 6/15 otannan issueista (Python 2 -tuen pudotus PR #580, six:n poisto #581, CSS-sanitoija #152, spec-päivityksen laajuus #56). AI voi ehdottaa; päätös sitoo kaikkia riippuvia paketteja (esim. pandas `html` extra vaatii `html5lib>=1.1`, FACT).
6. **Ihmisreview.** Kaikki tässä tehty on verifioitu vain testisuitella. Pakkausmuutokset (setup.py) vaikuttavat distroihin, joita testit eivät kata.
7. **Mitata latauksia luotettavasti.** Pypistats ja ClickPy eivät vastanneet rate limitin takia – pieni asia, mutta osoittaa, että osa ylläpitäjän tilannekuvasta jää ilman ihmistä UNKNOWN-tilaan.

## Arvio jatkuvasta ylläpitokustannuksesta

Lähtöluvut (FACT): uusia issueita+PR:iä n. 16 kpl / 12 kk (#588 → #603, 2025-09 → 2026-09) eli **~1,3 kpl/kk**; dependabot-päivityksiä muutama/kk; uusi Python-versio kerran vuodessa; pytest-major noin kerran vuodessa.

Tämän kokeen yksikkökustannus (FACT): n. 82 k tokenia ja 9 min yhdelle "kloonaa, aja testit, korjaa yksi asia, kirjoita raportti" -kierrokselle.

Kuukausiarvio AI-agentille (CALCULATION FACT-luvuista, oletukset INFERENCE):

| Työ | Kertoja/kk | Tokenia/kerta | Tokenia/kk |
|---|---|---|---|
| Uuden issuen/PR:n triage + testiajo | 1–2 | 30–80 k | 50–160 k |
| Bugikorjaus tai yhteensopivuuskorjaus + testit | 0,5–1 | 80–200 k | 50–200 k |
| Dependabot/CI-vihreänä pito | 2–4 | 20–40 k | 50–150 k |
| Kvartaaleittain: uusi Python/pytest, changelog, julkaisuvalmistelu | 0,33 | 150–300 k | 50–100 k |
| **Yhteensä** | | | **~0,2–0,6 M tokenia/kk** |

Rahaksi muutettuna suuruusluokka on kympeistä muutamaan kymmeneen euroon kuukaudessa mallihinnoittelusta riippuen (INFERENCE; ei laskettu tarkalla hinnastolla). Se on merkityksetön verrattuna toiseen kustannuserään:

**Ihmistyö, jota ei voi korvata (INFERENCE):** 1–3 h/kk henkilöltä, jolla on merge- ja julkaisuoikeudet: PR-review-nappien painaminen, `git tag` + PyPI-julkaisu, tietoturvailmoitusten vastaanotto, design-päätökset (40 % issueista). Ja kertaluonteisesti: oikeuksien hankkiminen, joka on kestänyt tässä projektissa jo 2,5 vuotta (#577) ilman tulosta – yhteisö forkkasi sen sijaan (`html5lib-modern`).

Nollaeuron agenttitalouden kannalta: tämän paketin ylläpito on AI:lle **tokenien osalta lähes ilmaista** mutta **oikeuksien osalta mahdotonta**. Kustannus ei ole laskentaa vaan luottamus.

## Johtopäätös

1. **Koodi ei ollut pullonkaula.** html5lib on 17 499 testin verran terve Python 3.14:llä. Ainoa rikkinäinen osa oli pakkausinfra, ja sen korjaus vei agentilta 13 sekuntia komentoaikaa. Sama korjaus oli jo kolmessa avoimessa PR:ssä vapaaehtoisilta (FACT).
2. **Pullonkaula on julkaisuoikeus, ja sitä AI ei voi hankkia.** 20 mergeable-PR:ää, 2,5 vuotta vanha julkaisupyyntö, vastaamaton tietoturvakontaktipyyntö. Mikään näistä ei muutu lisäämällä agentteja – ne muuttuvat vain, jos oikeuksien haltija palaa tai PEP 541 -siirto tehdään.
3. **Työn jakauma 15 issuen otannassa:** 47 % AI voi tehdä yksin, 40 % vaatii ihmisen päätöksen, 13 % on vanhentunutta – ja 100 % AI:n tekemästä on arvotonta ilman ihmisen julkaisunappia.
4. **Ylläpitokustannus AI:lla on n. 0,2–0,6 M tokenia/kk** (CALCULATION/INFERENCE), eli suuruusluokkaa halvempi kuin yhden ihmistunnin hinta. Ihmisen 1–3 h/kk jää silti välttämättömäksi ja on ainoa niukka resurssi.
5. **Korjaus tehtävänantoon:** viimeisin julkaisu on 2020-06 (1.1), ei 2017-12; latausluvut jäivät UNKNOWN-tilaan (rate limit). "30 M/kk" on käsittelemätön oletus, ei mitattu.
6. **Yleistys (INFERENCE):** "orpojen pakettien" ylläpito ei ole AI:lle koodiongelma vaan pääsyongelma. Arvokas tuote ei ole patchi vaan *luotettu ihminen, jolla on oikeudet ja joka käyttää agenttia* – ja sellainen ihminen tarvitsee 1–3 h/kk, ei työpäiviä. Se on kokeen tärkein luku.
