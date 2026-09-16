# Koe 06: ensimmäisen markkinan valinta kylmälle pääsytestille

2026-09-16, Claude. Ei yhteydenottoja, ei rahaa, ei tilejä, ei verkkotunnusta. Merkinnät
FACT / CALC / INFERENCE / HYPOTHESIS / UNKNOWN. Tarkoitus: valita puhtain ja halvin
markkina kokeelle, joka mittaa, saako tuntematon mutta uskottava toimija kylmästi
yritysasiakkaan, joka antaa ostolaskudatan ja hyväksyy etukäteen tulospalkkion.
Valintaperuste on metodologinen: vähiten ylimääräisiä sekoittavia muuttujia per euro,
ei mukavuus.

## 1. Mitä markkinalta vaaditaan

1. **Otantakehikko**, joka on avoin kenelle tahansa ilmaiseksi tai lähes: yritysrekisteri,
   josta voi rajata aktiiviset, riittävän kokoiset, ostointensiiviset yritykset ilman
   että kokoluokitus vaatii maksullista tietopalvelua.
2. **Laillinen kylmä yhteydenotto** oikeushenkilöille ilman ennakkosuostumusta
   (sähköposti ja/tai puhelin).
3. **Kieli ja toimintaympäristö**, jotka ovat koehenkilölle tavallista osaamista
   (lähtöresurssisääntö: suomi, englanti, ruotsi sallittuja; muu kieli olisi
   negatiivista piilopääomaa, ei mekanismin ominaisuus).
4. **Ostolaskudata** rakenteisena ja asiakkaan itse vietävissä (ei integraatiota).
5. **Sopimus ja tulospalkkio** toteutettavissa ilman lupaa tai lisenssiä.
6. Tietosuoja- ja salassapitovaatimukset tunnetut ja samat kuin muualla EU:ssa.
7. Kustannus 1 000 euron ja haaran 200 euron tappiorajan sisällä.
8. Markkinavalinta ei lisää muuttujaa, jota koe ei voi erottaa mekanismista.

## 2. Vertailu

| | Suomi | Ruotsi | Viro | UK | Alankomaat | Saksa | Tanska | USA |
|---|---|---|---|---|---|---|---|---|
| Kehikko ilmaiseksi | **FACT:** YTJ-massalataus (96 MB zip, päivittäin): yhtiömuoto, TOL 2025, rekisterit (ALV, työnantaja, ennakkoperintä), osoite, rekisteröintipäivä; ei liikevaihtoa. **FACT:** Veron yhteisöjen julkiset verotiedot CSV:nä (2024: 384 627 riviä, 27 MB, CC BY 4.0): verotettava tulo ja maksuunpannut verot per y-tunnus. Yhdistettynä kokoproxy ilmaiseksi | FACT: Bolagsverketin maksuton "värdefulla datamängder" -rajapinta (rekisteröityminen, avaimet); digitaaliset vuosikertomukset. Kokoproxy mahdollinen, vaatii rekisteröinnin | FACT: e-Äriregister, vuosikertomukset julkisia, avoindata-paketteja päivittäin | FACT: Companies House -massa-CSV (n. 2 GB), AccountCategory kokoproxyna (FULL/SMALL/MICRO), mutta kenttä on osin tyhjä | KVK maksullinen; UNKNOWN ilmainen kokoproxy | Handelsregister; Bundesanzeiger-tilinpäätökset; ei massalatausta ilmaiseksi (UNKNOWN) | FACT-tasoinen tieto: CVR-rajapinta ilmainen ja sisältää talouslukuja (toissijainen muistitieto, ei tarkistettu tässä) | Ei kansallista rekisteriä; osavaltioittain; ei kokotietoa |
| Kylmä sähköposti oikeushenkilölle | **FACT (SVPL 917/2014, 202 §):** "Suoramarkkinointia yhteisölle saa harjoittaa, jollei tämä ole sitä nimenomaisesti kieltänyt." Kielto-oikeus ja lähettäjän tunnistettavuus vaaditaan. Yleisosoitteet (info@) turvallisia; nimetyn henkilön työosoite tulkinnanvarainen (HAMK: suostumus; Legalfolks: työtehtäväyhteys) | FACT (MFL 19 §): ei suostumusta juridiselle henkilölle; opt-out-osoite vaaditaan | FACT (ESS): opt-out oikeushenkilöille; lähettäjä tunnistettava | FACT (PECR, ICO): corporate subscribers ilman suostumusta; sole traders ja nimetyt henkilöt voivat olla "individual subscriber" | FACT (Tw 11.7): sallittu oikeushenkilön julkaistuun yleisosoitteeseen, opt-out | **FACT (UWG § 7 Abs. 2):** sähköposti vaatii nimenomaisen ennakkosuostumuksen myös B2B. Vain puhelin "mutmaßliche Einwilligung" | **FACT (MFL § 10):** sähköposti vaatii suostumuksen myös B2B; puhelin yritykselle sallittu | FACT: CAN-SPAM opt-out-malli |
| Kylmä puhelu yritykselle | FACT: kuluttajansuojalain puhelinmyyntirajoitukset koskevat kuluttajia; yritykselle ei vastaavaa kieltomekanismia (toissijaiset lähteet) | Sallittu (toissijainen) | Sallittu (toissijainen) | Sallittu, TPS/CTPS-tarkistus | Sallittu B2B (toissijainen) | Sallittu B2B oletetulla suostumuksella | Sallittu B2B | Sallittu B2B |
| Kieli tavallisena osaamisena | **Kyllä** (suomi) | Kyllä (ruotsi), mutta lähettäjä on ulkomainen toimija | Ei (viro); englanti mahdollinen mutta merkitsee ulkomaista toimijaa | Kyllä (englanti), ulkomainen toimija | Ei | Ei | Ei | Kyllä, ulkomainen toimija, aikaero |
| Ostolaskudata vietävissä | **FACT:** Procountor "Export to Excel" ostojen raportoinnissa; Netvisor ostoreskontra ja raportit. FACT: 353,2 M verkkolaskua 2025, n. 370 000 y-tunnusta verkkolaskuosoitteistossa (Valtiokonttori) | Fortnox/Visma-viennit (INFERENCE) | E-lasku yleinen (INFERENCE) | Xero/Sage-viennit (INFERENCE) | INFERENCE | INFERENCE | INFERENCE | QuickBooks (INFERENCE) |
| Tulospalkkio ilman lupaa | Kyllä: asiakas perii itse, me tuotamme listan; ei perintätoimintaa (OIKEUSKARTOITUS, kortti) | Kyllä (INFERENCE) | Kyllä (INFERENCE) | Kyllä (INFERENCE) | Kyllä (INFERENCE) | Kyllä (INFERENCE) | Kyllä (INFERENCE) | Osavaltiokohtaista (UNKNOWN) |
| Tietosuoja | GDPR; käsittelysopimus; B2B-markkinointi oikeutetulla edulla | GDPR | GDPR | UK GDPR | GDPR | GDPR | GDPR | Osavaltiokohtaista |
| Kustannus kehikko + kanava | **0 € kehikko**, verkkotunnus 12 - 27 €/v (FACT: Traficom 12 €, Zoner 13,20 € 1. vuosi, Louhi 24 €/v), tilinpäätös tarvittaessa 5,02 €/kpl (FACT: Virre) | 0 € kehikko (rekisteröinti), .se-tunnus (UNKNOWN) | 0 € | 0 € kehikko, .co.uk (UNKNOWN) | Maksullinen kehikko | Maksullinen/UNKNOWN | 0 € kehikko | Kehikkoa ei ole |
| Ylimääräinen muuttuja | Pieni markkina; tulospalkkiomallin tuttuus pk-yrityksissä UNKNOWN | **Ulkomainen lähettäjä** (suomalainen Oy ruotsalaisille) | Ulkomainen lähettäjä + kieli | Ulkomainen lähettäjä, valuutta, paikallinen kirjanpitokäytäntö | Kieli | Kanava lain takia vain puhelin + kieli | Kanava vain puhelin + kieli | Ei kehikkoa, aikaero, oikeudellinen hajonta |

## 3. Päätös

**Suomi.** Perustelut järjestyksessä:

1. Ainoa vertailun markkina, jossa **kehikko kokoproxyineen on 0 € ja avoin kenelle
   tahansa** ilman rekisteröitymistä (YTJ + Vero). Rakennettu ja mitattu 2026-09-16:
   9 492 yritystä kriteereillä (`kokeet/06-kehikko-tiivistelma.json`).
2. Sähköposti ja puhelin ovat molemmat laillisia oikeushenkilöille ilman
   ennakkosuostumusta (202 §), joten kanavaa ei sanele laki vaan koe.
3. Kieli on tavallista osaamista. Muu markkina lisäisi muuttujan "ulkomainen
   toimija", jota koe ei voi erottaa "tuntematon toimija" -muuttujasta. Se on
   symmetrisen piilopääomasäännön negatiivinen puoli (LAHTORESURSSISAANTO §3 kohta 3).
4. Ostolaskudata on Suomessa rakenteista ja asiakkaan itse vietävissä, joten
   data-askel ei vaadi integraatiota eikä lupaa.
5. Saksa ja Tanska putoavat lain takia (sähköposti kielletty B2B), Viro, Alankomaat
   kielen takia, USA kehikon puutteen takia. Ruotsi on toiseksi paras ja se
   kirjataan **varamarkkinaksi**, jos Suomen tulos on CHANNEL UNKNOWN (ei tavoiteta)
   eikä FAIL; silloin ulkomaisen toimijan muuttuja hyväksytään tietoisesti.

**Mitä valinta ei kerro:** tulos koskee Suomea. Se ei yleisty markkinoihin, joissa
sähköposti on kielletty tai kehikkoa ei ole. Tulospalkkiomallin tuttuus suomalaisissa
pk-yrityksissä on tuntematon ja se on osa mittausta, ei kontrolli.

## 4. Kehikon rakenne ja suppilo (FACT, ajettu 2026-09-16)

Lähde: YTJ-massalataus 2026-09-16 (463 805 yritystä) ja Veron julkiset verotiedot
verovuosi 2024. Skripti `kokeet/06-otantakehikko.py`.

| Askel | Kriteeri | Jäljellä |
|---|---|---|
| kaikki | | 463 805 |
| K1 | osakeyhtiö (yhtiömuoto 16) | 320 097 |
| K2 | kaupparekisterissä, ei konkurssia/saneerausta/selvitystilaa | 309 203 |
| K3 | arvonlisäverovelvollinen liiketoiminnasta | 191 995 |
| K4 | työnantajarekisterissä | 84 554 |
| K5 | ennakkoperintärekisterissä | 83 275 |
| K6 | y-tunnus rekisteröity viimeistään 2021-06-30 | 65 914 |
| K7 | päätoimiala TOL 2025: 10 - 33, 41 - 43, 46, 49 - 53 | 29 573 |
| K8 | Veron 2024 maksuunpannut verot ≥ 10 000 € | **9 492** |

CALC: yhteisöverokanta 20 % → 10 000 € veroa vastaa noin 50 000 € verotettavaa tuloa.
Se ei ole ostovolyymi. Se on aktiivisuus- ja kokoproxy, joka on ilmainen ja jonka
tuntematon henkilö voisi tehdä samalla tavalla. Ostovolyymi todetaan vasta PASS-
tapauksessa aineistosta itsestään.

Jakaumat: verobandit 10 - 50 k€: 5 673; 50 - 250 k€: 2 887; yli 250 k€: 932.
Ikäluokat: 5 - 9 v: 1 291; 10 - 19 v: 2 818; yli 20 v: 5 383. Toimialat: rakentaminen
41 - 43 yhteensä 3 293; tukkukauppa 46: 1 970; kuljetus 49 - 53: 1 486; teollisuus
10 - 33: 2 743. Verkkosivu YTJ:ssä 38,4 %:lla (loput haetaan yrityksen omilta sivuilta
hakukoneella; se on osa saavutettavuuden mittausta).

176 toimialakriteerin läpäissyttä yritystä puuttui Veron tiedostosta (UNKNOWN syy;
todennäköisesti tilikausi tai verotuksen keskeneräisyys). Ne eivät ole kehikossa.

## 5. Kanavavertailu Suomessa

| Kanava | Laillisuus | Kustannus/120 yritystä | Mitä mittaa | Heikkous |
|---|---|---|---|---|
| Sähköposti yleisosoitteeseen | 202 § | 0 € (verkkotunnus jo laskettu) | Tarjouksen ja tuoreen identiteetin uskottavuus tekstinä | Tuore verkkotunnus: toimitettavuus UNKNOWN; yleisosoitteen seulonta (toissijaiset lähteet: 2026 vaatimukset SPF/DKIM/DMARC, uusi verkkotunnus 5 - 10 viestiä/pv aluksi) |
| Puhelin vaihteeseen | Sallittu yritykselle | 0 € (liittymä) tai prepaid n. 10 € | Erottaa "ei tavoitettu" aidosta hylkäyksestä; ihmisen ääni luottamuksen rakentajana | Omistajan aikaa 5 - 10 min/puhelu; portinvartija |
| Kirje rekisteröityyn osoitteeseen | 202 § (posti) | **FACT: 3,00 €/kirje 2.6.2026 alkaen** → 360 € | Ohittaa roskapostisuodattimen; osoite YTJ:ssä kaikilla | Ylittää haaran 200 €:n rajan; hidas; ei valita |
| LinkedIn | Alustan säännöt | 0 € | | Vaatii profiilihistorian = piilopääoma tai nollaprofiili, jonka viestit eivät mene perille; ei valita |
| Alustat (Fiverr, Upwork, suomalaiset välityspalvelut) | | 0 - maksu | | Suomessa ei tunnistettua pk-talousanalyysin markkinapaikkaa (UNKNOWN); ei valita ensimmäiseksi |

**Valinta:** sähköposti ensisijaisena, yksi muistutus, sitten puhelu vastaamattomille.
Puhelu ei ole toinen koe vaan saman protokollan kolmas askel, jonka tehtävä on
erottaa tavoittamattomuus hylkäyksestä. Tulokset raportoidaan askeleittain.

## Lähteet (tarkistettu 2026-09-16)

- Laki sähköisen viestinnän palveluista 917/2014, 24 luku 200 - 203 § (Finlex; pykälän
  202 sanamuoto HAMK Unlimitedin ja Edilexin sisällysluettelon kautta, koska Finlexin
  sivu ei renderöitynyt noutotyökalulle). https://unlimited.hamk.fi/muut/saako-sahkopostilla-markkinoida/ ; https://www.legalfolks.fi/post/sahkoinen-suoramarkkinointi-milloin-suostumus-tarvitaan
- PRH avoin data, YTJ-rajapinta v3 ja massalataus: https://avoindata.prh.fi/ytj.html ; skeema https://avoindata.prh.fi/opendata-ytj-api/v3/schema?lang=fi ; PRH:n tiedote digitilinpäätöksistä (vain iXBRL, n. 5 % tilinpäätöksistä): https://www.prh.fi/fi/tietoa_prhsta/uutislistaus/tiedotteet/2025/avoin-data-digitilinpaatokset_22.4.2025.html
- Verohallinto, avoin data, yhteisöjen tuloverotuksen julkiset tiedot: https://vero.fi/tietoa-verohallinnosta/tilastot/avoin_dat
- PRH Virre-hinnasto (tilinpäätös 4,00 € + alv = 5,02 €): https://www.prh.fi/virre-hinnasto
- .fi-hinnat: https://www.zoner.fi/verkkotunnus/paljonko-oma-domain-maksaa-2026/ ; https://www.louhi.fi/verkkotunnukset/fi-verkkkotunnus-hintamuutos26/
- Posti, kirjehinnat 2.6.2026: https://www.posti.fi/ajankohtaista-postilla/postimaksut_20260430
- ICO, business-to-business marketing (PECR): https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/
- Companies House bulk data: https://chguide.co.uk/bulk-data/companies
- Ruotsi MFL 19 §: https://lawline.se/answers/skicka-e-post-i-marknadsforingssyfte ; Bolagsverket API: https://bolagsverket.se/apierochoppnadata/hamtaforetagsinformation/vardefulladatamangder/apiforvardefulladatamangder.5513.html
- Viro: https://www.dlapiperdataprotection.com/?t=electronic-marketing&c=EE
- Saksa UWG § 7: https://www.ihk.de/nordwestfalen/recht/rechtsthemen/wettbewerbsrecht/werbung-per-telefon-telefax-oder-e-mail-3614212
- Tanska MFL § 10: https://danskelove.dk/markedsf%C3%B8ringsloven/10
- Alankomaat Tw 11.7: https://maxius.nl/telecommunicatiewet/artikel11.7
- Procountor ostojen raportointi (Export to Excel): https://help.procountor.fi/fi/articles/532428-ostojen-raportointi ; Netvisor ostoreskontra: https://netvisor.fi/tuote/laskutusohjelma/ostolaskut/
- Valtiokonttori, verkkolaskutus 2025: https://www.valtiokonttori.fi/uutinen/suomen-verkkolaskutus-kasvaa-ennatystasolle-mutta-eu-muutokset-ravistelevat-markkinaa-lahivuosina/
- Kylmän sähköpostin vastausasteet (toissijaiset, myyjien omat): Belkins 2026 (0,45 % tiukalla kylmämääritelmällä; omistajat 0,57 %), Instantly 2026 (3,43 % keskimäärin) https://belkins.io/blog/cold-email-response-rates ; https://instantly.ai/cold-email-benchmark-report-2026
- Toimitettavuus 2026 (toissijaiset): https://leadhaste.com/blog/google-microsoft-sender-guidelines ; https://www.topo.io/blog/safe-sending-limits-cold-email
