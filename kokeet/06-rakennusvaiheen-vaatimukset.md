# Koe 06: rakennusvaiheen R1 - R7 tekniset ja juridiset edellytykset

2026-09-17, Claude. Valmistelua lukituksen jälkeen. **Ei ostettu mitään, ei luotu tilejä,
ei nimetty brändiä, ei yhteydenottoja.** Tämä dokumentti ei muuta lukittua protokollaa
(`ee116d4`). Yksi poikkeamaehdotus (P1) on kirjattu §8:aan päätettäväksi. Merkinnät
FACT / INFERENCE / UNKNOWN.

## 1. R1 Brändin nimi ja .fi-verkkotunnus

**Tekninen:** .fi-tunnus rekisteröidään välittäjän kautta; haltijaksi oikeushenkilö
(y-tunnus). Hinta 12 - 27 €/v (FACT, markkinavertailu). DNS välittäjällä tai
Cloudflaressa (0 €).

**Juridinen ja metodologinen:**
- FACT (Traficom): kun haltija on yritys, fi-verkkotunnushaku näyttää julkisesti
  yrityksen nimen ja yhteystiedot. Olemassa oleva yritys näkyy siis verkkotunnuksen
  haltijana. Tämä on oikeushenkilösäännön mukaista (yritys näkyy siellä, missä
  oikeushenkilön kuuluu näkyä) ja sama tieto on sivun alatunnisteessa. Ei poikkeama.
- Brändin nimi on markkinointinimi. FACT (PRH): laki ei tunne markkinointinimeä;
  rekisteröimätöntä nimeä saa käyttää, PRH suosittelee aputoiminimeä suojaksi
  (60 €, hallituksen päätös). **Ei rekisteröidä:** 60 € ei muuta mitattavaa
  parametria, ja oikeushenkilö tunnistetaan joka viestissä. Riski: nimeä ei ole
  suojattu. Hyväksyttävä kokeen ajaksi.
- Nimen ehdot (johdettu säännöistä): ei sisällä omistajan nimeä, olemassa olevan
  yrityksen nimeä tai sen osaa, "Constraint", "eikaisiina" tai muuta tutkimukseen
  viittaavaa; ei sekoitettavissa olemassa olevaan recovery-alan toimijaan tai
  rekisteröityyn toiminimeen/tavaramerkkiin (tarkistus: PRH nimipalvelu, YTJ-haku,
  fi-verkkotunnushaku, EUIPO/PRH tavaramerkkihaku; kaikki 0 €); kuvaava ja neutraali
  suomeksi; ei väitä kokoa, ikää tai tiimiä.
- Omistajan tarkistettava: kattaako olemassa olevan yrityksen kaupparekisteriin
  merkitty toimiala tämän palvelun (yleistoimialalauseke riittää). UNKNOWN Claudelle.

**Tarvitaan omistajalta:** nimen valinta (Claude voi tuottaa 10 ehdokasta
saatavuustarkistuksineen yksityiseen hakemistoon, ei repoon), välittäjän valinta,
rahankäyttölupa 12 - 27 €.

## 2. R2 Sähköposti, SPF, DKIM, DMARC

**Vaatimukset:** oma verkkotunnus, DKIM-allekirjoitus, käsin lähetys webmailista tai
tavallisesta asiakasohjelmasta, EU-palvelin mieluiten, ei massapostitustyökalua.

| Vaihtoehto | Hinta | Huomio |
|---|---|---|
| Zoho Mail Forever Free | 0 € | FACT (toissijaiset): oma verkkotunnus, 5 käyttäjää, vain selain; saatavuus uusille EU-tileille ristiriitainen lähteissä (UNKNOWN). DKIM-tuki ilmaistasolla UNKNOWN, tarkistettava rekisteröityessä |
| Zoho Mail Lite | n. 1 €/kk (toissijainen) | DKIM, IMAP |
| Välittäjän oma sähköposti (webhotelli) | n. 2 - 5 €/kk (UNKNOWN tarkka) | Suomalainen palvelin; jaettu IP voi heikentää toimitettavuutta |
| Proton / Fastmail / Google Workspace | 4 - 7 €/kk (UNKNOWN tarkka) | Hyvä toimitettavuus; budjetin sisällä 3 kk |

Suositus: halvin vaihtoehto, jossa DKIM on varmasti käytössä; budjetin yläraja 21 € /
3 kk pätee. Valinta ei vaikuta mittareihin, kunhan SPF + DKIM + DMARC ovat kunnossa.

**DNS-tietueet (tehdään, kun verkkotunnus on):** SPF `v=spf1 include:<palveluntarjoaja>
-all`; DKIM palveluntarjoajan avaimella; DMARC `v=DMARC1; p=quarantine;
rua=mailto:dmarc@<verkkotunnus>` (FACT toissijaiset 2026: p=none heikentää
toimitettavuutta vasta yli n. 100 viestiä/pv; meillä ≤ 15/pv, silti quarantine);
MX; ei seurantaa. Lähetystahti lukittu: 5 → 15/pv.

**Juridinen:** jokaisessa viestissä lähettäjä, oikeushenkilö, osoitteen lähde,
kielto-ohje (V1:ssä ja M1:ssä on; FACT 202 - 203 §). Estolista yksityisessä
hakemistossa. Tilin luo omistaja (Claude ei luo tilejä).

## 3. R3 Verkkosivu

**Tekninen:** yksi staattinen HTML-sivu + tietosuojasivu + kolme PDF:ää. Isännöinti 0 €:
Cloudflare Pages tai välittäjän sivutila. **Ei GitHub Pagesia Constraint Worksin tai
omistajan tilin alla** (yhdistäisi identiteetit). Ei analytiikkaa, ei evästeitä, ei
lomaketta (ei evästebanneria, ei ylimääräistä henkilötietojen keruuta). Claude
kirjoittaa sivun tiedostoina yksityiseen hakemistoon; omistaja julkaisee.

**Sisältö (luonnos `06-sopimuspohjat-luonnos.md` §4):** mitä, miten palkkio toimii,
mitä dataa, miten suojataan, kuka (nimi + oikeushenkilö alatunnisteessa), "palvelu on
uusi, emme esitä referenssejä", sopimuspohjat, tietosuojaseloste, kielto-osoite.

**Juridinen:** tietoyhteiskunnan palvelun tarjoajan tiedonantovelvollisuus (nimi,
osoite, y-tunnus, sähköposti: alatunniste kattaa); tietosuojaseloste GDPR 13 - 14 art.
(markkinointirekisteri: rekisterinpitäjä oikeushenkilö, oikeutettu etu, lähde
yrityksen verkkosivu ja YTJ, säilytys kokeen ajan + 12 kk estolista, vastustamisoikeus).
Markkinointiväitteet: ei lupauksia löydöistä, ei vertailuja, ei referenssejä.

## 4. R4 Sopimuspohjat

Luonnokset: `06-sopimuspohjat-luonnos.md` (paikkamerkein, GPT:n tarkistettavaksi).
- **Käsittely- ja salassapitosopimus:** GDPR 28 art. 3 kohdan pakollinen sisältö
  (kohde, kesto, luonne, tarkoitus, tietotyypit, rekisteröityjen ryhmät,
  dokumentoidut ohjeet, salassapito, turvatoimet, alikäsittelijät, avustaminen,
  poisto/palautus, auditointi). FACT: kirjallinen sopimus on pakollinen, myös
  sähköisenä.
- **Palkkioehdot:** lukitun §5 (ii) mukaiset, ei muutoksia.
- **Allekirjoitus:** Suomessa sopimus on vapaamuotoinen; PDF + sähköpostivahvistus
  nimetyltä, yritystä edustamaan oikeutetulta henkilöltä riittää (protokolla §5).
  Edustamisoikeus tarkistetaan maksuttomasta kaupparekisteriotteesta (FACT: Virre
  0 €). Ei maksullista allekirjoituspalvelua.
- **Vastuu:** ei vastuuvakuutusta (budjetti). Pohjassa vastuunrajoitus: välittömät
  vahingot, enintään 5 000 € (luonnosluku, ei johdettu mistään säännöstä; omistajan ja
  GPT:n arvioitavaksi; palkkioihin sidottu katto olisi nollatuloksessa 0 € eikä
  uskottava), ei koske tahallisuutta, törkeää huolimattomuutta eikä salassapitoa; ei
  rajoita tietosuojavastuuta rekisteröityjä kohtaan. Riski kirjattu; juristia ei käytetä (lukittu).

## 5. R5 Esimerkkiraportti

Synteettinen aineisto (keksityt toimittajat, ei oikeita nimiä), 2 sivua: löydöslista,
perustelu per löydös, asiakkaan toimenpide, palkkion laskentaesimerkki. Merkintä
"esimerkki keksityllä aineistolla". Ei väitä tyypillistä löydösmäärää. 0 €.

## 6. R6 Prepaid-liittymä

FACT (toissijaiset): aloituspaketti 4,90 - 5,90 €, sis. 5 - 7 € saldoa, puhelut n.
0,066 €/min. 100 puhelua × 3 min ≈ 20 € → budjetin 10 € voi ylittyä puheajalla;
kokonaiskatto 120 € kestää sen (R6 yläraja korjataan toteumassa, ei protokollassa).
Prepaid-numero ei näy numerohauissa (INFERENCE). Rekisteröinti: prepaid ei vaadi
tunnistautumista Suomessa (UNKNOWN 2026 tilanne; tarkistetaan ostettaessa).

## 7. R7 Toimitettavuustesti

Kolme testilaatikkoa (Gmail, Outlook.com, kotimainen operaattori). Omistajan
olemassa olevat henkilökohtaiset laatikot kelpaavat vastaanottajiksi (ne eivät näy
kenellekään; ei piilopääomaa). Kirjataan: inbox / roskaposti / ei perillä,
otsakkeista SPF/DKIM/DMARC pass. Toistetaan, jos tulos on roskaposti: korjataan DNS,
ei viestiä (viesti on lukittu).

## 8. Poikkeamaehdotus P1: tekoälykäsittelyn säilytyslause (vaatii päätöksen)

**Ristiriita (FACT):** lukittu §5 (i) sanoo "tekoälyrajapinta ilman datan säilytystä tai
koulutuskäyttöä" ja tapaamisrunko §4 "ilman datan säilytystä palvelussa". Rajapintojen
oletus on kuitenkin 30 päivän säilytys (Anthropic: 30 pv, koulutuskielto
kaupallisissa ehdoissa, nollasäilytys vain hyväksytyille asiakkaille; OpenAI: 30 pv,
nollasäilytys kelpoisille, EU-residenssi myynnin kautta). Nykyisellä sanamuodolla
sopimus ei olisi tosi allekirjoitushetkellä. Tämä on uusi konkreettinen ristiriita,
ei optimointi.

**Ehdotus (pienin muutos, joka tekee lauseesta toden):** korvataan "ilman datan
säilytystä" muotoilulla: *"Luonnollisten henkilöiden nimet ja yhteystiedot
pseudonymisoidaan paikallisesti ennen tekoälykäsittelyä. Tekoälypalvelun tarjoaja ei
käytä aineistoa mallien kouluttamiseen ja voi säilyttää syötteitä enintään 30 päivää
väärinkäytösten valvontaa varten, minkä jälkeen ne poistetaan."* Vaikutus kokeeseen:
hankintapaketin osa "tekoälykäsittely sopimuksessa näkyvissä" säilyy; sanamuoto
muuttuu asiakkaalle hieman varovaisemmaksi (suunta: PASSia vaikeuttava, ei
helpottava). Koskee vain sopimuspohjaa ja tapaamisrungon kohtaa 4, ei V1:tä, M1:tä
eikä P1-puhelukäsikirjoitusta.

Vaihtoehto: hakea nollasäilytystä ennen D0:aa (UNKNOWN saadaanko; ei rahaa, mutta
aikaa). Sopimuspohjaluonnoksessa on P1:n mukainen muotoilu merkittynä; lukittuja
tiedostoja ei ole muutettu.

## 9. Mitä voidaan tehdä ilman rahaa ja päätöksiä (tehty tai tehtävissä heti)

- [x] Sopimuspohjien, tietosuojaselosteen ja sivutekstin luonnokset paikkamerkein
- [ ] GPT:n tarkistus luonnoksille (suositus ennen käyttöä, koska juristia ei ole)
- [ ] Nimiehdokkaat saatavuustarkistuksineen yksityiseen hakemistoon (kun omistaja pyytää)
- [ ] Sivun HTML ja esimerkkiraportti yksityiseen hakemistoon (kun nimi on)
- [ ] X-K04-uusintatarkistus 2026-10-01 jälkeen

## 10. Omistajan päätökset ja rahankäyttö, järjestyksessä

1. **Poissulkukierros:** lue 150 nimeä yksityisestä hakemistosta ja merkitse X-koodit
   (ohje hakemiston `LUE-ENSIN.md`). Ei rahaa. Estää kaiken muun otokseen liittyvän.
2. **P1:** hyväksy tai hylkää säilytyslauseen korjaus (tai päätä hakea nollasäilytystä).
3. **Brändin nimi** (pyydä ehdokkaat tai anna oma) ja toimialatarkistus.
4. **Rahankäyttölupa:** verkkotunnus 12 - 27 €, sähköposti 0 - 21 €, prepaid 5 - 25 €;
   yhteensä enintään 68 €, katto 120 €. Tilit (välittäjä, sähköposti, isännöinti)
   luo omistaja.
5. Käynnistyslupa S1:lle aikaisintaan 2026-10-05, kun R1 - R7 ja X-K04-uusinta on tehty.

## Lähteet (tarkistettu 2026-09-17)

- Traficom, fi-verkkotunnushaku ja julkiset tiedot: https://www.traficom.fi/fi/viestinta/fi-verkkotunnukset/verkkotunnusvalittajalle/whois-palvelu-nayttaa-verkkotunnuksen
- PRH, aputoiminimi: https://www.prh.fi/fi/yrityksetjayhteisot/yritystennimet/aputoiminimi.html
- Anthropic, API and data retention: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention ; https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
- OpenAI, data controls ja EU-residenssi: https://developers.openai.com/api/docs/guides/your-data ; https://openai.com/index/introducing-data-residency-in-europe/
- GDPR 28 artikla: https://www.privacy-regulation.eu/fi/28.htm ; EDPB suuntaviivat 07/2020
- Zoho Mail ilmaistaso (toissijaiset, ristiriitaiset): https://www.zoho.com/mail/custom-domain-email.html
- Prepaid-hinnat (toissijainen): https://liittyma.fi/puhelinliittymat/prepaid-liittyma/
