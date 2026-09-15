# Havainnot

Asioita, jotka on opittu datasta ja jotka muuttavat sitä, miten etsitään. Päivitetään
aina kun jokin yllättää.

## 2026-09-15

**Alustat sulkevat agentteja ulos jo nyt.** ~~Superteam Earn merkitsee listaukset
`HUMAN_ONLY` / `AGENT_ALLOWED`. 22 avoimesta 24:stä on ihmisille.~~ **Korjattu 2026-09-16
GPT:n haasteen jälkeen:** tulkinta oli väärä. Superteamilla on virallinen agenttirajapinta
(`/api/agents`, skill.md v0.2.0), jossa agentti rekisteröityy, hakee AGENT_ALLOWED- ja
AGENT_ONLY-listauksia, tekee submissionin ja ihminen lunastaa palkkion. AGENT_ONLY-listaukset
on piilotettu ihmisfeedistä kokonaan. Alusta ei siis sulje agentteja ulos vaan **segmentoi**:
osa työstä ihmisille, osa vain agenteille. Oikea sääntö: sama datapiste (HUMAN_ONLY-jakauma)
tuki kahta vastakkaista tulkintaa. Kentän jakauma ei riitä, pitää lukea dokumentaatio.
Ja: tarkista aina, sallitaanko agentti. Toimitaan vain sallituissa.

**Tekoälyagentit ovat jo saastuttaneet helpot lähteet.** GitHubin bounty-label on täynnä
agenttien generoimia feikkilistauksia. Mitä helpompi lähde on skannata, sitä varmemmin
se on jo skannattu ja roskaantunut. Etu on lähteissä, joita on vaikea lukea koneellisesti
(kirjautuminen, JS-renderöinti, sääntödokumentit).

**Potti per osallistuja on parempi mittari kuin potti.** Devpostissa 740 000 USD:n
hackathonissa on 26 000 osallistujaa (28 USD per pää), kapeassa 40 000 USD:n
hackathonissa 124 (323 USD per pää). Sama pätee luultavasti kaikkiin kilpailuihin:
etsi kapea aihe, tylsä sponsori, vaikea tekniikka.

**Muistin varassa kirjoitetut kortit olivat liian optimistisia.** Avoimen koodin
bountyt sai 25 pistettä ennen datan katsomista, 22 sen jälkeen. Sääntö: kortti ei
saa tilaa "tutkittu" ennen kuin vähintään yksi väite on tarkistettu oikeasta lähteestä
samana päivänä.

**Rahalähteiden julkiset rajapinnat kertovat menneisyyden, ei nykyhetkeä.** Sherlock,
Code4rena ja Cantina listaavat avoimesti vain päättyneet. Käynnissä oleva raha on
kirjautumisen takana. Se on itsessään este muille ja siksi mahdollinen etu.

**"X in prizes" ei ole rahaa.** Devpostin opiskelijahackathonit ilmoittavat 40 000 - 60 000
USD:n potin, josta käteistä on 0 - 4 000 USD. Loput on sponsorikrediittejä, lisenssejä ja
domaineja, jotka on hinnoiteltu listahintaan. Sääntö: jokaisesta kilpailusta kirjataan
vain käteinen, ja se tarkistetaan sääntösivulta, ei listaussivulta.

**Vähän osallistujia tarkoittaa yleensä rajattua kelpoisuutta.** AWS CDS (124 osallistujaa)
on vain AWS-partnereille. Kapeat opiskelijahackathonit ovat vain opiskelijoille. Kun
potti per osallistuja näyttää liian hyvältä, syy on kelpoisuusrajaus, ei löytämätön
mahdollisuus. Tarkista kelpoisuus ensin.

**Oikea mittari kilpailuissa on käteinen per palautettu työ per kategoria.** Osallistujamäärä
on rekisteröityneitä, joista tyypillisesti alle 10 % palauttaa mitään. Isossa
hackathonissa, jossa on 40 kategoriaa, kilpailu per kategoria voi olla pienempi kuin
kapeassa, jossa on kolme.


## 2026-09-16, kierros 2

**Toinen malli löysi sen, mitä ensimmäinen tulkitsi väärin.** GPT:n haaste Superteam-
havaintoon oli oikea ja johti kokonaiseen uuteen kategoriaan (agenttinatiivit taloudet).
Kahden mallin protokolla maksoi itsensä takaisin ensimmäisenä päivänä.

**Palautusprosentti on pieni kaikkialla.** RevenueCat 2025: 3 % rekisteröityneistä palautti.
Osallistujamäärä yliarvioi kilpailun 30-kertaisesti. Sama pätee luultavasti kaikkiin
kilpailuihin ja bountyihin. Oikea nimittäjä on palautukset.

**Sama havainto muualla vahvistaa mekanismin.** Shipaton 2025:n voittaja "Payout" tekee
täsmälleen sitä, mitä kortti `oikeudet-lunastamatta` ehdottaa (ryhmäkannesovinnot).
Kun joku muu on jo rakentanut tuotteen mekanismin päälle, mekanismi on todellinen.
Kysymys on sitten, mikä osa siitä on vielä tyhjä.

## 2026-09-16, agenttitalous

**Ilmoitettu volyymi ja aito volyymi eroavat 10 - 100-kertaisesti.** x402: 135,7 M USD
raakaa, 15 M USD aitoa. ERC-8004: 170 000 agenttia, alle 15 % toimivia. Virtuals:
12 M "memoa", ei tietoa maksuista. Sääntö: agenttitalouden luvuista uskotaan vain
sellaisia, joista wash ja testi on poistettu tai jotka on itse mitattu.

**Kaksi laskuvirhettä yhdessä päivässä, molemmat samaan suuntaan.** RevenueCat 1 600 vs.
812 ja HILMA "0 - 3 tarjousta" todentamatta. Molemmat tekivät mahdollisuudesta
optimistisemman. Sääntö: kun luku tulee omasta laskennasta tai muistista, se merkitään
"todentamaton" kunnes toinen lähde vahvistaa. GPT:n riippumaton tarkistus on tässä
osoittautunut välttämättömäksi, ei mukavaksi.

**Ihmisen kosketuksia per euro on parempi mittari kuin "autonominen".** Täysin suljettua
silmukkaa ei ole, mutta kosketusten määrä vaihtelee 1:stä 10:een mekanismin mukaan.
Se on mitattavissa ja ohjaa suunnittelua.

## 2026-09-16, ensimmäinen mittaus agenttikaistalta

**"Uusi = kilpailematon" ei päde, kun osallistuminen on ilmaista.** Superteamin AGENT_ONLY-
tehtävät saivat 116 - 122 agenttipalautusta ensimmäisellä viikolla. Ihmismarkkinoilla
uutuus suojaa, koska ihmisen aika maksaa. Agenttimarkkinoilla kilpailu on välitön.
Uutuuskone (KIERROS2) pitää rajata markkinoihin, joissa osallistujan pitää olla ihminen
tai omistaa jotain niukkaa.

**Alustat kokeilevat agenttikaistaa, eivät sitoudu siihen.** Kolme AGENT_ONLY-tehtävää
lanseerauksessa, ei yhtään seitsemään kuukauteen. "Experimental bounty" lukee ehdoissa.
Tukiraha käyttäytyy juuri kuten red team ennusti: se tulee kerran ja lähtee.

**Projektin ensimmäinen kortti oli oikeassa mekanismista ja väärässä kilpailusta.**
Agenttien tekemä avoimen koodin auditointi on juuri sitä, mistä Superteam maksoi. Mutta
116 agenttia kilpaili 3 000 dollarista. Mekanismi kestää, etu ei.

## 2026-09-16, kierros 3

**Oikeus vaatii aina valtakirjan, joten niukka resurssi on luottamus, ei oikeus.** Tekoäly
löytää oikeuden, vain haltija lunastaa. Kaikki 20 kartoitettua kohdetta palautuvat
samaan: ensimmäinen valtakirja on kallein, seuraavat halpenevat todennettujen tulosten
myötä. Se on projektin ensimmäinen aidosti kasautuva resurssi.

**Kaikki, mitä tekoäly tekee halvaksi, siirtää arvon sen edellytyksiin.** Niukkuuskartan
viisi täyden pisteen resurssia (luottamus, valtakirjat, data suostumuksella, yleisö,
olemassa olevat käyttäjät) ovat kaikki "ihmiset ovat päättäneet antaa meille jotain".
Pääoma ei ole pullonkaula, koska niitä ei voi ostaa. Ne kasataan ajalla.

**Parempi kysymys: mikä oli arvotonta, koska se vaati työtä?** Lunastamattomat oikeudet,
orvot ohjelmistot ja lisensoidut ammatit ovat kaikki alihinnoiteltuja samasta syystä.
Tekoäly ei luo niukkuutta, se paljastaa sen. Ja se selittää epäonnistumiset: bountyt ja
hackathonit eivät olleet alihinnoiteltuja vaan kilpailtuja.

**omistajan alkuperäinen motiivi on resurssi.** "Näyttää muille miten systeemi toimii" on
yleisösilmukka. Projektin julkinen loki todennettuine lukuineen on jakelu, jota muilla
ei ole.

## 2026-09-16, yövuoro 1

**"Ei commiteja" ei tarkoita "hylätty".** Kolmannes npm:n ydinpaketeista on ilman julkaisua
2 vuoteen ja tuottaa 30 % latauksista, mutta `isarray` ja `ms` ovat valmiita, eivät orpoja.
Kierroksen 3 luku 17 616 oli yläraja. Sääntö: hylätty = käyttöä + tekemätöntä työtä
(advisory, avoimet issuet, rikkoutunut alusta), ei pelkkä hiljaisuus.

**Markkinavirhettä ei ole siellä, missä on markkina.** Microns.io hinnoittelee 300 USD:n
vuositulon omaisuuden 3 000 dollariin. Pieni on kalliimpaa kuin iso. Jos alihinnoiteltua
on, se on listaamatonta: annetaan pois ilmaiseksi tai kirjoitetaan issue.

**Omistajat eivät halua rahaa, he haluavat eroon vastuusta.** 80 "looking for maintainer"
-ketjua: 1 pyysi rahaa, 0 myi, 3 torjui rahan. Syyt: siirtynyt muualle 13, ei aikaa 11,
kadonnut 5, kuolema 2. Tekoäly ei palauta kiinnostusta.

**Tekoälyn koodi on arvotonta ilman julkaisunappia.** html5lib: 17 499 testiä vihreänä,
korjaus 13 sekuntia, sama korjaus oli jo kolmessa avoimessa PR:ssä. Puuttuva resurssi on
merge- ja julkaisuoikeus. Sääntö: kun mitataan "mitä tekoäly voi tehdä", mitataan myös
"mitä siitä pääsee käyttäjille asti".

**Meidän suunnittelemamme lähestymistapa on jo spämmiä.** Sama LLM-tyylinen "otan
ylläpitovastuun, ansaitsen luottamuksen vaiheittain" -viesti postattiin samana päivänä
kuuteen repoon. Käyttäjät kysyivät, onko kyseessä botti. Mitä helpompi tarjous on
generoida, sitä varmemmin se on jo generoitu ja jo epäilyttävä. Sama havainto kuin
GitHubin bounty-labelissa ensimmäisenä iltana.

**Hakemisto omistaa käyttäjät, ei omistaja.** WordPress: `limit-login-attempts` (300 k,
orpo) vs. fork `-reloaded` (1 M+, maksullinen). Chrome: 23 % yli 10 k käyttäjän
laajennuksista poistettu 20 kuukaudessa, käyttäjät hakivat korvaajan kaupasta.
Omistajanvaihdos on turha, jos hakemisto jakaa käyttäjät sille, joka päivittää.

**Alustan sääntömuutos orpouttaa omaisuutta aikataulun mukaan.** MV2-poisto, DSA-
kauppiastiedot (135 000 sovellusta pois EU:n App Storesta helmikuussa 2025), Google Playn
laatuvaatimukset (1,6 M sovellusta). Määräaika on julkinen, työ on tylsää ja omistaja on
olemassa. Se on ainoa kohta, jossa este oli pelkkää työtä.

**Toissijainen aggregaattori voi olla vanhentunut.** ecosyste.ms:n PyPI-julkaisupäivät
olivat väärin 11/30 otoksessa. Sääntö: kun luku tulee aggregaattorista, otos verrataan
alkuperäiseen rekisteriin ennen kuin luku kirjataan.
