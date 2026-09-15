# Päätösloki

Jokainen päätös ennen toimeenpanoa. Muoto: päivä, kaista, päätös, perustelu, odotettu tulos.

## 2026-09-15 · Kokeen perustaminen

**Päätös:** Aloitetaan kolmella rinnakkaisella kaistalla, 1 000 € jaettuna 0 / 300 / 700.

**Perustelu:** 1 000 € → 10 M€ on 10 000x. Historiassa se on onnistunut vain omistuksella
tai lotolla. Bounty-kaista mittaa puhdasta älyä ilman pääomaa, tietokaista mittaa
informaatioetua, omistuskaista on ainoa reitti, joka on oikeasti skaalautunut.

**Odotettu tulos:** Kaista 1 tuottaa ensimmäisen euron nopeimmin, jos tuottaa. Kaista 3
tuottaa eniten, jos tuottaa, mutta hitaimmin.

## 2026-09-15 · Kaista 1 aloitetaan ensin

**Päätös:** Ensimmäinen työ on Sherlockin ja Cantinan avoimien kilpailujen listaus.

**Perustelu:** Sherlock antaa avoimen JSON-rajapinnan. Ei maksa mitään. Auditointikilpailut
maksavat löydöistä kiinteän potin, joka on oikeasti olemassa ja jaetaan löytäjille.

## 2026-09-15 · Rakenne muutetaan yleiseksi etsintäkoneeksi

**Päätös:** Kolme kiinteää kaistaa korvataan mahdollisuusrekisterillä. Jokainen mekanismi
on kortti, joka vastaa neljään kysymykseen (kuka maksaa, miksi, mikä estää muita, mikä on
meidän etumme) ja saa pisteet kuudella kriteerillä. Rinnalle jatkuva etsintäprosessi.

**Perustelu:** Bountyt ja krypto olivat ensimmäisiä hypoteeseja, eivät rajaus. Kone, joka
vertailee mekanismeja samoilla kriteereillä, löytää paremman reitin nopeammin kuin
kolme etukäteen valittua kaistaa.

**Ensimmäinen ranking (16 korttia, 4 hylätty):** kärjessä avoimen koodin issue-bountyt
ja online-hackathonit, molemmat 25/30. Yhteistä: nolla pääomaa, raha on jo olemassa
ja este muille on aika, jonka tekoäly poistaa.

**Hylätty heti:** DeFi-tuotto (pääoman tuottoa, ei älyn), MEV (latenssikilpailu ja
eettisesti kyseenalainen), airdrop-farmaus (sybil rikkoo sääntöjä), vedonlyönti
(Suomen lainsäädäntö ennen 2027).

**Odotettu tulos:** Ensimmäinen 1 000 € → 2 000 € -koe valitaan hackathonien tai
issue-bountyjen väliltä sen jälkeen, kun käynnissä olevat on listattu selaimella.

## 2026-09-15 · Ensimmäinen data kärkikorteista, pisteet korjattu

**Päätös:** Avoimen koodin bountyt lasketaan 25 → 22 (Algora hiipunut, GitHub-label
roskaantunut, Superteam pääosin HUMAN_ONLY). Hackathonit pysyy kärjessä, tuplaus 4 → 3.

**Perustelu:** Ks. `etsinta/HAVAINNOT.md`. Devpostissa on juuri nyt 38 avointa
online-hackathonia, ja niistä 4 - 5 on kapeita (alle 400 osallistujaa, potti yli
30 000 USD). Niissä potti per osallistuja on 150 - 320 USD.

**Seuraava askel:** Luetaan kapeiden hackathonien säännöt (tekoälyn käyttö, kelpoisuus
Suomesta, tiimikoko). Jos yksi läpäisee, siitä tulee ensimmäinen koe `kokeet/`-kansioon.

## 2026-09-16 · Kapeat Devpost-hackathonit hylätty, hackathonit 24 → 23

**Päätös:** AWS CDS, LexHack, DSH Hacks ja UnivaBio hylätään koe-ehdokkaina. Hackathon-
kortin tuplaus-pisteet 3 → 2.

**Perustelu:** AWS on vain partnereille. Kolme muuta ovat opiskelijahackathoneja, joiden
ilmoitetusta potista käteistä on 0 - 7 %. Ks. `etsinta/HAVAINNOT.md`.

**Mitä tämä tarkoittaa projektille:** Ensimmäisen illan data on korjannut kaksi kärkikorttia
alaspäin. Se on oikea tulos, ei epäonnistuminen: kone toimii, koska se hylkää nopeasti.
Kärki on nyt tasainen (22 - 23 pistettä), eikä yksikään kortti ole vielä ansainnut koetta.

**Seuraavat askeleet, järjestyksessä:**
1. RevenueCat Shipaton: selvitä kategoriat ja palautusten määrä per kategoria edellisvuodelta.
2. Auditointikilpailut: lue käynnissä olevat Sherlockista ja Cantinasta kirjautuneena.
3. GPT haastaa kaikki "tutkittu"-kortit ja ajaa generaattorin.

## 2026-09-16 · Superteam-havainto korjattu, kierros 2 ajettu, 6 uutta korttia

**Päätös:** HAVAINNOT-tiedoston Superteam-tulkinta korjataan GPT:n haasteen mukaisesti.
Agenttinatiivit taloudet nostetaan omaksi kortiksi (23 p). Kierros 2 tuotti viisi muuta
korttia, joista delegoitu pääoma hylätään heti (luvanvaraista). Kolme generaattoria
kirjattu `etsinta/KIERROS2.md`.

**Perustelu:** Ks. `etsinta/HAVAINNOT.md` ja `etsinta/KIERROS2.md`.

**Mitä omistajalta tarvitaan seuraavaksi:** Superteam-agentin rekisteröinti (yksi curl,
ohje `tyokalut/haku/superteam_agentti.py`). Ilman sitä AGENT_ONLY-markkinan kokoa ei voi
mitata. Claude ei luo tilejä.

**Seuraava koe-ehdokas, järjestyksessä:**
1. Superteam AGENT_ONLY-listaus, jos sellaisia on ja palkkio on yli 200 USD.
2. RevenueCat Shipaton, jos päätös tehdään 48 tunnin sisällä (14 päivää aikaa).
3. Oikeuskone: 20 oikeuskategorian kartoitus, ei vaadi rahaa.
