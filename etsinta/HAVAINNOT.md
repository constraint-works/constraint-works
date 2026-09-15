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
