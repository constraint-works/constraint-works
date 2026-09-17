# Koe 06: rakennusvaiheen R1 - R7 tekniset ja juridiset edellytykset

2026-09-17, Claude. Valmistelua lukituksen jälkeen. **Ei ostettu mitään, ei luotu tilejä,
ei nimetty brändiä, ei yhteydenottoja.** Tämä dokumentti ei muuta lukittua protokollaa
(`ee116d4`). P1 on ratkaistu (§8). Omistajan päätökset 2026-09-17: rahankäyttölupa ≤ 68 €
(verkkotunnus, sähköposti, prepaid), katto 120 €; vastuukatto 5 000 € ei hyväksytty (§4b). Merkinnät
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
- **Toimialatarkistus tehty 2026-09-17 (FACT, PRH Virre, julkinen haku, 0 €):**
  oikeushenkilön kaupparekisteriin merkitty toimiala sisältää yleislausekkeen "kaikki
  laillinen liiketoiminta", joka kattaa palvelun. Ei estettä. Rekisteröity
  päätoimiala on eri alalta kuin tämä palvelu; y-tunnuksen tarkistava vastaanottaja voi
  nähdä epäsuhdan. Symmetrisen piilopääomasäännön mukaan se on koehenkilön rajoite,
  ei mekanismin ominaisuus: kirjataan Q2/Q3-vastauksista ja spontaaneista maininnoista,
  ei korjata rekisterimuutoksella (olisi infrastruktuurin optimointia ja maksaisi).
  Yksityiskohdat yksityisessä hakemistossa.

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
- **Vastuu:** ks. §4b. Aiempi 5 000 €:n luonnosluku on poistettu (omistaja ei
  hyväksynyt; se ei ollut johdettu mistään).

## 4b. Vastuulauseke: PÄÄTETTY 2026-09-17, vaihtoehto A (GPT:n pre-D0-tarkistus, omistaja)

**Päätös:** ei euromääräistä vastuukattoa; vastuu välittömistä vahingoista; välilliset
vahingot rajattu pois; poikkeukset tahallisuus, törkeä huolimattomuus, salassapito ja
tietosuoja. Ei muuteta ilman konkreettista juridista ristiriitaa. Alla vertailu, johon
päätös perustui.

Lähtötiedot (FACT): ei vastuuvakuutusta (ei budjetissa); palvelun hinta asiakkaalle voi
olla 0 €; käsiteltävä aineisto on luottamuksellista; sopimusosapuoli on omistajan
olemassa oleva yritys, joten riski kohdistuu siihen. Juristia ei käytetä (lukittu).

| | Lauseke | Asiakkaan näkökulma (vaikutus ACCESS-porttiin) | Omistajan riski | Vaatiiko keksityn luvun |
|---|---|---|---|---|
| A | Ei euromääräistä kattoa; vastuu välittömistä vahingoista; välilliset rajattu pois paitsi tahallisuus, törkeä huolimattomuus, salassapito ja tietosuoja | Uskottavin "riskittömät ehdot" -paketin kanssa; ei herätä kysymyksiä | Suurin: välitön vahinko rajaamaton | Ei |
| B | Ei vastuulauseketta lainkaan (yleinen sopimusoikeus) | Lyhin sopimus; asiakas ei huomaa eroa A:han | Suurempi kuin A: myös välilliset vahingot tuottamuksesta | Ei |
| C | Katto sidottu sopimuksen arvoon (alan yleinen käytäntö, esim. IT-ehdoissa) | Sopimuksen arvo voi olla 0 € → katto 0 € → näyttää vastuun välttelyltä; heikentää porttia | Pienin | Ei, mutta katto on käytännössä nolla tai vaatii vähimmäisluvun (= keksitty luku) |
| D | Kiinteä eurokatto | Riippuu luvusta | Rajattu | **Kyllä.** Ainoa ei-mielivaltainen ankkuri olisi vakuutuksen korvausmäärä, eikä vakuutusta ole |
| E | Vastuuvakuutus + katto vakuutusmäärään | Vahvin luottamussignaali | Pienin todellinen | Ei, mutta maksaa (UNKNOWN, tyypillisesti satoja euroja/v) → ylittää budjetin ja olisi uusi rahankäyttöpäätös |

**Johdettavissa säännöistä:** C ja D eivät käy (C heikentää lukittua "riskitön ehto"
-pakettia tavalla, jota ei ole preregisteröity; D vaatii keksityn luvun). E vaatii rahaa
yli luvan. Jäljelle jäävät A ja B. Luonnoksessa on **A**, koska se rajaa välilliset
vahingot (omistajan suoja) keksimättä lukua. Tämä on sopimusriskin valinta, jonka
kantaa oikeushenkilö; siksi se jää omistajan vahvistettavaksi GPT:n tarkistuksen
yhteydessä, mutta se ei estä muuta rakennustyötä.

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

## 8. P1: tekoälykäsittelyn säilytyslause (RATKAISTU 2026-09-17)

**Ristiriita (FACT):** lukittu §5 (i) lupasi tekoälykäsittelyn "ilman datan säilytystä";
rajapintojen oletus on rajattu säilytys (Anthropic: 30 pv, koulutuskielto kaupallisissa
ehdoissa, nollasäilytys vain hyväksytyille; OpenAI: 30 pv, nollasäilytys kelpoisille).

**Omistajan päätös:** hyväksytty totuudenmukaisuuskorjauksena. Sopimus ei lupaa
nollasäilytystä, ellei toteutus sitä todella tarjoa; paikallinen pseudonymisointi
ennen tekoälykäsittelyä; ei koulutuskäyttöä säilyy; **"enintään 30 päivää" ei ole
lukittu**, vaan lopullinen teksti vastaa täsmälleen D0:ssa käytettävää
palveluntarjoajaa, rajapintakonfiguraatiota ja säilytyskäytäntöä; nollasäilytyksen
hyväksyntä ei ole kokeen edellytys. Toimeenpantu: protokolla §5 (i), tapaamisrunko
kohta 4, sopimuspohjan kohta 6 (hakasulkein). **Ennen D0:aa:** valitaan yksi
tekoälypalvelu analyysiä varten, luetaan sen voimassa oleva säilytysdokumentaatio,
täytetään hakasulkeet sanatarkasti sen mukaan, kirjataan lähde ja päivä lokiin.

## 9. Rakennusvaiheen tila 2026-09-17 (0 € käytetty)

- [x] Toimialatarkistus: yleislauseke kattaa palvelun (§1)
- [x] 10 brändiehdokasta tarkistettu (.fi whois.fi, YTJ-nimihaku, TMview FI + EUIPO,
      verkkohaku; positiiviset kontrollit ajettu); tulokset vain yksityisessä hakemistossa
- [x] Sivun HTML, tietosuojasivu, käsittely- ja salassapitosopimus, palkkioehdot ja
      synteettinen esimerkkiraportti pohjina yksityisessä hakemistossa; täyttöskripti
      pysähtyy, jos yksikin arvo tai paikkamerkki on täyttämättä; PDF-muunnos testattu
      testiarvoilla (3 PDF:ää syntyi, esimerkkiraportin laskelmat tarkistettu)
- [x] DNS-tietuepohja (SPF `-all`, DKIM, DMARC `p=quarantine`, tiukka kohdistus)
- [x] R7-ohje ja otsaketarkistin (`kokeet/06-r7-otsaketarkistin.py`, savutestattu)
- [x] Osto- ja käyttöönotto-ohje omistajalle (yksityinen)
- [ ] Omistaja: nimen valinta, ostot (≤ 68 €), tilit
- [x] Vastuulauseke: vaihtoehto A hyväksytty (§4b)
- [x] GPT:n pre-D0-tarkistus rakennusvaiheelle `99a62e9`: APPROVED täsmennyksin
      (vastuulauseke A; palkkioehtojen kohta 6 selvennetty; P1 nykyisessä muodossa)
- [ ] P1-hakasulkeiden täyttö ennen D0:aa: tekoälypalvelu, todellinen säilytyskäytäntö ja
      käsittelypaikka sen palvelun ja konfiguraation voimassa olevasta dokumentaatiosta,
      jota todella käytetään; ei arvauksella; lähde ja päivä lokiin
- [ ] R7-testi, X-K04-uusinta, käynnistyslupa (aikaisintaan 2026-10-05)

Huomio koe 07:lle (ei tämän kokeen työtä): P1 sitoo meidät paikalliseen
pseudonymisointiin ennen tekoälykäsittelyä. Pseudonymisointivaihe on rakennettava ja
testattava ennen kuin yhtään asiakasaineistoa analysoidaan; se kuuluu koe 07:n
lukittavaan protokollaan, ei ACCESS-kokeeseen.

## 10. Täsmällinen hankintasuunnitelma (halvin vaihtoehto, joka täyttää lukitut vaatimukset)

| Erä | Valinta | Hinta | Peruste |
|---|---|---|---|
| Verkkotunnus | Välittäjä, jonka .fi-hinta on Traficomin maksu ilman lisää ja DNS-hallinta sisältyy | **12,00 €/v** (FACT: kahdella välittäjällä 12,00 €, laskutetaan viranomaismaksuna ilman alv:a; muut 15 - 26,40 €) | Halvin; vaatimus = omat MX/TXT/CNAME-tietueet |
| Sähköposti | 1) Zoho Mail ilmaistaso EU-datakeskuksessa, jos rekisteröityminen sallii ja DKIM saadaan päälle (FACT: DKIM-ohje ei mainitse tasorajoitusta; saatavuus uusille EU-tileille UNKNOWN). 2) Muuten Zoho Mail Lite, n. 1 USD/käyttäjä/kk vuosilaskutuksella ≈ 11 - 12 €/v | **0 € tai ≈ 12 €** | Halvin, jossa oma verkkotunnus + SPF + DKIM + DMARC; käsin lähetys selaimesta riittää (≤ 15/pv) |
| Puhelin | Prepaid-aloituspaketti (FACT toissijainen: 4,90 €, sis. 5 € saldoa, 0,066 €/min) + lataus tarpeen mukaan | **4,90 € + ≤ 20 € latauksia** | CALC: 100 puhelua × 3 min × 0,066 € ≈ 20 € |
| Sivun isännöinti | Ilmainen staattinen isännöinti uudella, vain tätä varten luodulla tilillä (ei GitHub Pages olemassa olevilla tileillä) | 0 € | Lukittu: 0 € |
| **Yhteensä** | | **≈ 17 - 49 €** (lupa 68 €, katto 120 €) | |

Tilit ja maksut tekee omistaja (Claude ei luo tilejä eikä maksa). DNS-tietueet, sivun
tiedostot ja tarkistusskriptit ovat valmiina yksityisessä hakemistossa.

## 11. Omistajan toimet, järjestyksessä (kaikki muu on valmiina)

1. Valitse brändin nimi kymmenestä tarkistetusta ehdokkaasta (yksityinen hakemisto;
   oletus kirjattu sinne, jos et halua valita).
2. Osta verkkotunnus (12 €), luo sähköpostitili ja isännöintitili, osta prepaid.
   Ohje vaihe vaiheelta yksityisessä hakemistossa (`OSTO-JA-KAYTTOONOTTO-OHJE.md`).
3. Ilmoita Claudelle nimi, verkkotunnus, numero ja sähköpostipalvelun antama
   DKIM-avain → Claude täyttää sivun, PDF:t ja DNS-tietuelistan; omistaja julkaisee.
4. R7-toimitettavuustesti (ohje ja otsaketarkistin valmiina).
5. Vahvista vastuulauseke (§4b, oletus A) GPT:n tarkistuksen jälkeen.
6. Käynnistyslupa S1:lle aikaisintaan 2026-10-05.

## Lähteet (tarkistettu 2026-09-17)

- Traficom, fi-verkkotunnushaku ja julkiset tiedot: https://www.traficom.fi/fi/viestinta/fi-verkkotunnukset/verkkotunnusvalittajalle/whois-palvelu-nayttaa-verkkotunnuksen
- PRH, aputoiminimi: https://www.prh.fi/fi/yrityksetjayhteisot/yritystennimet/aputoiminimi.html
- Anthropic, API and data retention: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention ; https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
- OpenAI, data controls ja EU-residenssi: https://developers.openai.com/api/docs/guides/your-data ; https://openai.com/index/introducing-data-residency-in-europe/
- GDPR 28 artikla: https://www.privacy-regulation.eu/fi/28.htm ; EDPB suuntaviivat 07/2020
- Zoho Mail ilmaistaso (toissijaiset, ristiriitaiset): https://www.zoho.com/mail/custom-domain-email.html
- Prepaid-hinnat (toissijainen): https://liittyma.fi/puhelinliittymat/prepaid-liittyma/
- .fi-välittäjien hintavertailu (välittäjän oma sivu): https://nordweb.fi/verkkotunnus-vertailu
- Zoho DKIM-ohje: https://www.zoho.com/mail/help/adminconsole/dkim-configuration.html
