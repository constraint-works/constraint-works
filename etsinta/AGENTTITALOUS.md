# Agenttitalous 0 → 1

Tutkimuskysymys: mitä tapahtuu taloudelle, kun toimija voi havaita mahdollisuuden,
arvioida sen, tehdä työn, ostaa palveluita toisilta agenteilta, vastaanottaa maksun ja
aloittaa seuraavan tehtävän ohjelmallisesti lähes ilman ihmisen marginaalikustannusta?

Kolme osaa: rakennuspalikat datalla, nollaeuron agentin matka ja red team. Lopussa tuomio
ja kysymys, johon vaihdoin kesken tutkimuksen.

---

## 1. Rakennuspalikat (tilanne 2026-09-16)

| Suunta | Mikä on olemassa | Todellinen tila | Lähde |
|---|---|---|---|
| **agentti → raha** | Superteam Earn agent API: AGENT_ALLOWED / AGENT_ONLY -listaukset, agentti submittaa, ihminen lunastaa | Toimii. Palkkiot 500 - 5 000 USDC. Noin 80 % ihmisfeedin bountyista estää agentit. AGENT_ONLY-määrä tuntematon ilman avainta | skill.md, gigs.sh |
| **raha → agentti** | Virtuals Revenue Network: "jopa 1 M USD/kk agenteille, jotka myyvät ACP:n kautta" (helmikuu 2026). Recall-kilpailut, Bittensor-emissiot, Olas-staking | Tukirahaa, ei kysyntää. Jakokaava julkaisematta. Bittensor ja Olas vaativat tokenin ostoa | prnewswire, docs |
| **agentti → agentti** | x402 (HTTP 402 + USDC), Virtuals ACP, Googlen A2A, MCP | **Lähes tyhjä.** x402: 135,7 M USD raakavolyymista 89 % oli wash-, testi- tai sisäistä siirtoa; aitoa noin 15 M USD koko elinkaarella, noin 28 000 USD/päivä. x402 Bazaar -markkinapaikka: 112 API:a, kuukausitulo 24 USD, 0 ulkopuolista tuottajaa, joilla tuloja | Artemis 7/2026, CoinDesk 3/2026, x402bazaar.org |
| **agentti → palvelu → raha** | Julkaise API, agentit maksavat per kutsu | Tarjonta on, kysyntää ei. Ks. yllä | x402bazaar.org |
| **agentti → pääoma → toiminta → tuotto** | Agenttilompakot (Coinbase AgentKit, Privy), Olas Predict -agentit, Recall-trading-agentit, PNP Exchange (agentti luo ennustemarkkinoita Solanalla) | Infra valmis. Tuotto vaatii, että agentin strategia voittaa markkinan. Sitä ei ole ratkaistu | docs |
| **identiteetti ja maine** | ERC-8004: identiteetti-, maine- ja validointirekisterit, mainnet 1/2026 | **Ontto.** Yli 170 000 rekisteröityä agenttia, mutta vain 3 - 15 % ilmoittaa toimivan palvelun. 59 - 91 % arvioijista on sybil-koordinoituja. 98,7 - 100 % mainepalautteista ilman maksutodistetta. Maineen manipulointi maksaa 0,003 - 0,055 USD | arXiv 2606.26028 |
| **koordinointi** | Virtuals ACP (18 000 agenttia, 12,3 M "commerce memoa"), Olas mech-verkosto | Memojen määrä ei kerro rahasta. "aGDP 470 M USD" on tokenarvoa, ei maksuja | agenteconomy.to |

Yhteenveto: **putket ovat valmiit, vesi puuttuu.** Jokainen suunta on rakennettu, mutta
aito kysyntä on lähes kokonaan tukirahaa tai wash-volyymia. Ainoa kohta, jossa oikea
maksaja maksaa oikeasta työstä agentille, on Superteamin agenttikaista, ja sekin on
ekosysteemin markkinointibudjettia.

---

## 2. Nollaeuron agentti: kuinka pitkälle ennen kuin ihminen on pakollinen?

Oletus: yksi täysin luvallinen agentti, 0 €, verkkoyhteys, pääsy malleihin.

| Vaihe | Voiko agentti tehdä yksin? | Missä ihminen on pakollinen |
|---|---|---|
| Havaitse mahdollisuus | Kyllä. Superteam live-listaus, ACP-tehtävät | - |
| Arvioi | Kyllä | - |
| Rekisteröidy | Osittain. Superteam: POST nimellä, ei KYC:tä | Agentin luonti on tilin luonti. Tässä projektissa ihminen tekee sen periaatteesta |
| Tee työ | Kyllä | - |
| Submittaa | Kyllä, API:n kautta | Projektilistaukset vaativat ihmisen Telegram-osoitteen |
| **Vastaanota maksu** | **Ei.** | Superteam: ihminen lunastaa claim-koodilla, talent-profiili, Solana-lompakko. Virtuals: lompakko on ihmisen |
| Maksa seuraava toiminto | Osittain. USDC lompakossa voi maksaa x402-palveluita | **Mallitokenit** maksaa ihminen kortilla. Tämä on todellinen marginaalikustannus |
| Vaihda euroiksi | Ei | Pörssi ja KYC |
| Verota | Ei | Ihminen, aina |

**Ensimmäinen euro** voi syntyä Superteamin AGENT_ONLY-listauksesta. Se vaatii ihmisen
lunastuksen, mutta vain kerran per palkkio.

**Ensimmäinen euro rahoittaa seuraavan toiminnon** vain, jos toiminnon kustannus on
USDC:tä ketjussa (x402-palvelu, gas). Mallitokeneita ei voi ostaa USDC:llä ilman ihmistä,
paitsi jos mallia ostetaan x402:n kautta, mikä on teknisesti mahdollista mutta tänään
käytännössä olematonta.

**Suljettu silmukka** (havainto → päätös → työ → maksu → resurssi → havainto) **ei
sulkeudu tänään ilman ihmistä.** Ihminen on pakollinen kolmessa kohdassa: maksun
lunastus, mallitokenien maksu ja verotus. Kaksi ensimmäistä voidaan minimoida (yksi
lunastus per palkkio, yksi korttimaksu per kuukausi), kolmatta ei.

Oikea mittari ei siis ole "onko silmukka suljettu" vaan **ihmisen kosketuksia per euro**.
Bountyssa se on ehkä 10. Superteamin agenttikaistalla se voi olla 1. Se on todellinen ero.

---

## 3. Red team: miksi agenttitalous on meille hyödytön

Yritin tappaa hypoteesin. Hyökkäykset vahvimmasta heikoimpaan.

**1. Työn hinta painuu tokenikustannukseen.** Kaikilla agenteilla on samat mallit.
Kun agentit kilpailevat samasta tehtävästä, hinta laskee kunnes se vastaa halvimman
agentin tokenikustannusta. Voitto valuu mallintarjoajalle ja alustalle, ei operaattorille.
Tämä on sama dynamiikka kuin kyytipalveluissa: kuljettajat kilpailevat, alusta voittaa.
*Kestääkö hypoteesi?* Ei yleisesti. Kestää vain, jos meillä on jotain, mitä muilla
agenteilla ei ole: kertynyt maine, ainutlaatuinen data, pääoma tai aikaisuus.

**2. Kilpailu on jo täällä.** OpenClaw-agenttikehyksellä on valmis "bounty-hunter"-taito
ja Superteamissa on agenttiprofiileja nimellä "openclaw-profit-agent". Emme ole
ensimmäisiä. *Kestääkö?* Osittain. Agenttien määrä on vielä pieni, ja valtaosa on
geneerisiä. Kilpailu on kuukausien, ei vuosien päässä.

**3. Todellinen kysyntä on lähes nolla.** x402:n aito volyymi noin 15 M USD koko
elinkaarella, Bazaar 24 USD/kk. Ei ole taloutta, johon liittyä, on infra, joka odottaa
taloutta. *Kestääkö?* Ei agentti → agentti -suunnassa. Kestää agentti → raha -suunnassa
(Superteam), koska siellä maksaja on ihmisorganisaatio.

**4. Maine on väärennettävissä eikä siksi ole niukka.** ERC-8004-maine maksaa 0,003 USD
manipuloida. Jos maine on agenttitalouden niukka resurssi, se on tänään arvoton.
*Kestääkö?* Ketjussa ei. Alustan sisäinen maine (Superteamin agenttiprofiili, hyväksytyt
submissionit) on vaikeampi väärentää, koska ihminen tarkastaa.

**5. Ihminen on pakollinen ja KYC on ihmisen.** Yksi ihminen voi lunastaa monta agenttia,
mutta se on yksi verovelvollinen, yksi talent-profiili. Sybil-suojaus on rakennettu
lunastukseen. *Kestääkö?* Kyllä, koska emme yritä olla monta ihmistä. Yksi ihminen,
monta agenttia, on sallittua ja rehellistä.

**6. Tukiraha loppuu.** Virtualsin 1 M USD/kk ja Superteamin agenttikaista ovat
markkinointia. Kun alustat ovat saaneet agenttinsa, raha loppuu. *Kestääkö?* Ei
pitkällä aikavälillä. Mutta projektin ensimmäinen testi on 90 päivää.

**7. Verotus ja kirjanpito.** Tokenipalkkio on Suomessa tuloa lunastushetken arvolla.
Jatkuva toiminta on elinkeinotoimintaa. *Kestääkö?* Kyllä, se on hallinnollista, ei
rakenteellista. Kirjataan ledgeriin, hoidetaan.

**8. Adverse selection.** Työ, joka annetaan agenteille, on työtä, jota ihmiset eivät
halunneet tai jonka arvo on matala. *Kestääkö?* Osittain. Superteamin toolkit-bountyt
(500 - 5 000 USD) eivät ole roskaa. Mutta valtaosa AGENT_ALLOWED-listauksista tänään on
sisältötyötä.

**Tuomio:** Hypoteesi "agenttitalous on paikka, jossa agentti ansaitsee itsenäisesti"
**ei kestä**. Talous on ontto, silmukka ei sulkeudu, ja hinta painuu tokenikustannukseen.

Hypoteesi "agenttikaista on tänään vähemmän kilpailtu bounty-markkina, jossa ihmisen
kosketuksia per euro on yksi" **kestää**, mutta pienenä ja väliaikaisena. Se on koe,
ei strategia.

---

## 4. Kysymys, johon vaihdoin

Alkuperäinen kysymys oli "missä agentti voi ansaita". Tutkimus osoitti, että parempi
kysymys on:

**Mikä on niukka resurssi taloudessa, jossa työn hinta painuu tokenikustannukseen?**

Kun kaikilla on samat mallit, kyvykkyys ei ole niukkaa. Niukkaa on:

1. **Todennettu historia**, jota ei voi ostaa 0,003 dollarilla. Alustan sisäinen, ihmisen
   tarkastama maine. Se kertyy vain ajan kanssa ja vain niille, jotka ovat paikalla ajoissa.
2. **Data, jota muilla ei ole.** Suomalainen, pohjoismainen, toimialakohtainen.
3. **Pääoma**, joka on säänneltyä (ks. delegoitu pääoma, hylätty).
4. **Ihmisen luottamus**, joka lunastaa, allekirjoittaa ja vastaa.

Tästä seuraa projektin kannalta olennainen: **agenttitalouden 0 → 1 -vaiheessa ainoa
asia, jota kannattaa kerätä, on todennettu historia.** Ei rahaa. Raha on tänään pientä.
Historia on halpaa kerätä nyt ja kallista myöhemmin.

Se kääntää myös 10 miljoonan kysymyksen: ei "miten agentti tienaa 10 M€" vaan "kuka
omistaa agentin, jolla on vuoden todennettu historia, kun agenttityön markkina on
oikeasti olemassa". Vastaus voi olla arvokkaampi kuin 90 päivän palkkiot.

---

## 5. Ensimmäinen versio, jos rakennetaan

Pienin koe, joka testaa sen, mikä kestää:

- **Mitä:** yksi agentti Superteamin agenttikaistalla. omistaja rekisteröi (tilin luonti),
  Claude ja GPT tekevät työn, omistaja lunastaa.
- **Mittarit:** (1) AGENT_ONLY-listausten määrä ja palkkiot, (2) tokenikustannus per
  submissio euroina, (3) palkkio per submissio, (4) ihmisen kosketukset per euro,
  (5) hyväksyttyjen submissioiden määrä eli kertyvä historia.
- **Onnistumisen ehto:** palkkio per submissio > tokenikustannus per submissio vähintään
  kolmessa peräkkäisessä tehtävässä. Jos ei, kategoria hylätään tuloksena, ei mielipiteenä.
- **Budjetti:** 0 € pääomaa, tokenikustannukset kirjataan, 20 tuntia ihmisen aikaa.
- **Kesto:** 30 päivää.

Rinnalla, ilman rahaa: Virtualsin ACP-rekisteröinti (yksi rivi koodia), jotta historia
alkaa kertyä sielläkin, vaikka tuloja ei odoteta.
