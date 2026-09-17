# Koe 06, P1: millä tekoälypalvelulla ja missä tallennuksessa asiakasaineisto käsiteltäisiin

2026-09-17, Claude. Päätösmuistio omistajalle ja GPT:lle. Ei ostettu mitään, ei luotu tilejä.
Tausta: totuudenmukaisuuskorjaus P1 vaatii, että sopimuksen kohta 6 (tekoälypalvelu,
säilytyskäytäntö, käsittelypaikka) ja kohta 5 (tallennus) täytetään ennen D0:aa täsmälleen
sen palvelun ja konfiguraation mukaan, jota analyysissä (koe 07) todella käytettäisiin.
Arvauksia ei kirjata. Lähteet ovat palveluntarjoajien omaa dokumentaatiota, luettu
2026-09-17. Merkinnät FACT / INFERENCE / UNKNOWN.

## 1. Miksi kuluttajatilaukset eivät käy

Projektin mallit toimivat tilausten sisällä (päätösloki), mutta asiakkaan luottamuksellista
ostolaskuaineistoa ei voi käsitellä kuluttajatilauksen ehdoilla: sopimus lupaa "ei
koulutuskäyttöä" ja nimetyn alikäsittelijän käsittelysopimuksineen. Se edellyttää
kaupallista rajapintaa (INFERENCE ehdoista; kuluttajaehtoja ei luettu tässä, koska ne eivät
ole vaihtoehto).

## 2. Vaihtoehdot (FACT, palveluntarjoajan dokumentaatio)

| | A. Anthropic Claude API suoraan | B. Claude Amazon Bedrockissa EU-alueella | C. OpenAI API |
|---|---|---|---|
| Koulutuskäyttö | Ei ilman nimenomaista lupaa: "Retained data is never used for model training without your express permission" | Ei; malli ajetaan AWS:n tileillä, joihin mallintarjoajalla ei ole pääsyä: "they don't have access to Amazon Bedrock logs or to customer prompts and completions" | Ei oletuksena: "not used to train or improve OpenAI models (unless you explicitly opt in)" |
| Säilytys oletuksena | Tietosuojakeskus (päivitetty 1.7.2026): "we automatically delete inputs and outputs on our backend within 30 days". Rajapintadokumentaatio: keskustelusisältöä ei oletuksena säilytetä, paitsi "Covered Models" (Fable 5.x, Mythos 5.x), jotka vaativat 30 päivän säilytyksen. Poikkeukset: käyttöehtorikkomukseksi liputettu sisältö enintään 2 v, luokittelupisteet enintään 7 v | "by default, Amazon Bedrock does not store model inputs or outputs"; "no operators of the service can access model input or output". Poikkeus: Claude Fable 5 / 5.1 -malleilla kaikki liikenne säilytetään enintään 30 pv AWS:n sisällä väärinkäytösten tunnistukseen (tila `aws_review`); muilla malleilla, joiden `allowed_modes` sisältää `none`, mitään ei säilytetä | Väärinkäytöslokit enintään 30 pv |
| Nollasäilytys | Vain myynnin kautta hyväksytyille organisaatioille; ei saatavilla Covered Models -malleille | **Oletus** malleille, jotka sallivat tilan `none`; asetettavissa tilitasolla pakottavasti (`data_retention_mode: none`), jolloin säilytystä vaativa malli estetään | Vain hyväksytyille, myynnin kautta |
| Käsittelypaikka | `inference_geo`: vain "global" tai "us"; levossa säilytys vain "us". **EU-vaihtoehtoa ei ole** | Alue valitaan päätepisteellä; EU-alueen sisäinen käsittely mahdollinen; alueiden välinen reititys vain, jos se otetaan käyttöön, ja silloin säilytys tapahtuu käsittelyalueella | EU-residenssi vain hyväksytyille ja erillisellä sopimusmuutoksella, +10 % hinta |
| Käsittelysopimus (GDPR 28 art.) | Anthropic käsittelijänä; siirto Yhdysvaltoihin (vakiolausekkeet; UNKNOWN tarkka mekanismi, tarkistettava DPA:sta) | AWS käsittelijänä; AWS:n GDPR-DPA; EU-alue | OpenAI Ireland / vakiolausekkeet (UNKNOWN, ei tarkistettu) |
| Kustannus ennen koe 07:ää | 0 € (tili ilmainen, käyttö token-pohjainen) | 0 € (AWS-tili ilmainen, käyttö token-pohjainen); vaatii maksukortin tilille | 0 € |
| Mitä sopimukseen voisi totuudenmukaisesti kirjoittaa | "Anthropic, PBC; syötteet poistetaan viimeistään 30 päivän kuluessa, paitsi käyttöehtorikkomukseksi liputettu sisältö; käsittely Yhdysvalloissa tai muualla EU:n ulkopuolella vakiolausekkein" | "Amazon Web Services EMEA SARL, Amazon Bedrock, alue [EU-alue]; syötteitä ja tuloksia ei tallenneta eikä luovuteta mallin kehittäjälle; käsittely EU:ssa" (edellyttää mallia, joka sallii tilan `none`, ja pakotetun `none`-asetuksen) | "OpenAI; lokit enintään 30 pv; käsittely EU:n ulkopuolella" |

## 3. Arvio

- **B on ainoa vaihtoehto, jolla sopimukseen voi totuudenmukaisesti kirjoittaa sekä "ei
  säilytetä" että "käsittely EU:ssa" ilman myyntitiimin erillishyväksyntää.** Se vastaa
  myös sivun lukittua lausetta "salattu tallennus EU:ssa" hengeltään. Omistajan päätös P1:stä
  kielsi tekemästä nollasäilytyksen *erillishyväksynnästä* kokeen edellytystä; B:ssä
  nollasäilytys on palvelun oletus, ei hyväksyntä, joten se ei ole ristiriidassa päätöksen
  kanssa.
- B:n ehdot, jotka pitää todentaa ennen kuin teksti kirjataan (UNKNOWN nyt): (1) mikä
  Claude-malli, joka sallii tilan `none`, on saatavilla valitulla EU-alueella; (2) että
  pyynnöt ajetaan alueen sisäisesti eikä globaalilla reititysprofiililla; (3) AWS:n DPA:n
  voimassaolo oikeushenkilön tilille. Nämä näkee vain AWS-tililtä. Uusimmat Fable-mallit
  eivät käy B:n nollasäilytystekstillä (30 pv AWS:n sisällä); tuplamaksu- ja hyvityshaku ei
  tarvitse niitä (RISTIINARVIO-WORK: "pelkkä kaksoiskappalehaku ei tarvitse frontier-AI:ta").
- **A on varavaihtoehto**, jos B:n ehdot eivät täyty. Sen teksti on heikompi asiakkaan
  silmissä (30 pv, Yhdysvallat), mikä vaikeuttaa PASSia; se on silti tosi ja sallittu.
- C vaatii myyntihyväksynnän molempiin olennaisiin ominaisuuksiin. Ei suositella.
- Pseudonymisointi (henkilöiden nimet ja yhteystiedot korvataan tunnisteilla paikallisesti
  ennen rajapintakutsua) koskee kaikkia vaihtoehtoja ja on jo lukittu.

## 4. Tallennus (sopimuksen kohta 5)

Halvin tosi ratkaisu (0 €): aineisto vain omistajan työasemalla Suomessa, levyn
täyssalauksella (FileVault) ja lisäksi erillisessä salatussa levykuvassa, jonka avain on
vain omistajalla; ei pilvisynkronointia kyseiselle kansiolle; varmuuskopio vain salattuna
samaan fyysiseen hallintaan. Sopimusteksti: "salattu tallennus Palveluntarjoajan omalla
työasemalla Suomessa; ei pilvitallennusta". Omistajan vahvistettava: FileVault on päällä
(UNKNOWN Claudelle) ja että työaseman iCloud- tai muu synkronointi ei kata kansiota.

## 5a. PÄÄTÖS 2026-09-17 (omistaja)

**Ensisijainen toteutus: B, Amazon Bedrock EU:ssa**, pakollisin ehdoin ennen asiakasdatan
käyttöä: (1) tili/projekti tilassa `data_retention_mode: none`; (2) Claude-malli, joka toimii
tässä tilassa, ei retentionia vaativaa mallia; (3) vain EU Geographic Cross-Region- tai EU
In-Region -inference, global kielletty asiakasdatalle; (4) asetukset testataan API-kutsulla
ilman asiakasdataa ennen sopimuksen täyttämistä (`kokeet/06-p1-bedrock-testi.py`); (5)
sopimukseen kirjataan vasta testatun toteutuksen todellinen malli, retention ja
käsittelyalue; (6) jos jokin ehto ei toteudu, fallback on Anthropicin oma API todellisella
retentionilla; ehtoja ei löysätä Bedrockin saamiseksi toimimaan.

**Tallennus hyväksytty:** paikallinen salattu tallennus, ehdoin FileVault päällä, erillinen
salattu levykuva, ei pilvisynkronointia. Tarkistettu 2026-09-17 (FACT, komentorivi):
FileVault päällä; iCloudin Työpöytä ja Dokumentit -synkronointi pois; Työpöytä ei ole
ohjattu muuhun pilvipalveluun; Time Machine -kohteita ei ole. Levykuva luodaan ennen
ensimmäisen aineiston vastaanottoa (omistaja asettaa salasanan itse).

## 5. Päätettävää (alkuperäinen; ratkaistu kohdassa 5a)

1. Valitaanko B (suositus) vai A? B vaatii omistajalta AWS-tilin luonnin oikeushenkilön
   nimiin (0 €, maksukortti tilille; ei kuluja ennen koe 07:ää). Claude ei luo tilejä.
2. Tallennus kohdan 4 mukaan: kyllä/ei, ja FileVaultin tila.
3. Kun päätös on tehty ja B:n kolme ehtoa todennettu tililtä, Claude täyttää sopimuksen
   kohdat 5 - 6 sanatarkasti, kirjaa lähteet ja päivämäärän lokiin, rakentaa lopullisen sivun
   ja PDF:t, ja GPT tarkistaa täytetyn tekstin ennen D0:aa.

## Lähteet (luettu 2026-09-17)

- Anthropic Privacy Center, "How long do you store my organization's data?" (päivitetty 1.7.2026): https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
- Anthropic, API and data retention: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
- Anthropic, Data residency: https://platform.claude.com/docs/en/manage-claude/data-residency
- AWS, Amazon Bedrock data protection: https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html
- AWS, Amazon Bedrock data retention: https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html
- AWS, Amazon Bedrock abuse detection: https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html
- OpenAI, Data controls in the OpenAI platform: https://developers.openai.com/api/docs/guides/your-data
