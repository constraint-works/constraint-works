# Kaista 1 · Bounty (0 € pääomaa)

Mittaa: tuottaako pelkkä äly rahaa ilman pääomaa.

## Kaksi rahan lähdettä

**Pysyvät bounty-ohjelmat (Immunefi).** Protokolla pitää potin auki jatkuvasti.
Löydät haavoittuvuuden tuotantokoodista, raportoit, saat palkkion vakavuuden mukaan.
Ei määräaikaa, ei kilpailua samasta löydöstä paitsi että ensimmäinen raportoija voittaa.
`hae_immunefi.py` listaa kaikki ohjelmat. 2026-09-15: 175 ohjelmaa, maksimipalkkiot
yhteensä noin 110 M USD. Kolmekymmentä ohjelmaa maksaa miljoonan tai enemmän kriittisestä.

**Auditointikilpailut (Sherlock, Code4rena, Cantina).** Määräaikainen kilpailu, kiinteä
potti jaetaan kaikkien löytäjien kesken. Helpompi saada jotain, vaikeampi saada paljon.
Julkiset rajapinnat antavat vain päättyneet kilpailut. Käynnissä olevat vaativat
kirjautumisen tai selaimen. `hae_kilpailut.py` hakee Sherlockin historian, josta näkee
pottien koon ja tahdin.

## Rehellinen arvio

- Kriittinen löytö isosta protokollasta on harvinainen. Koodi on jo auditoitu monesti.
- Realistisin ensimmäinen euro tulee keskivakavasta löydöstä pienemmästä protokollasta
  tai kilpailusta, jossa potti jaetaan. Tyypillisesti 500 - 20 000 USD.
- Etu tekoälystä: jaksaa lukea 50 000 riviä Solidityä väsymättä ja ajaa monta
  rinnakkaista lukijaa eri hypoteeseilla.

## Seuraava askel

1. Valitaan 3 kohdetta: yksi iso (miljoonan potti), kaksi pientä, joiden koodi on
   päivittynyt viimeisen kuukauden aikana (uusi koodi = vähiten auditoitu).
2. Ladataan sopimukset, kartoitetaan hyökkäyspinta.
3. Ajetaan rinnakkaiset agentit eri haavoittuvuusluokilla (reentrancy, oracle,
   access control, laskuvirheet, upgrade-logiikka).
4. Kaikki löydöt kirjataan `loydot/`-kansioon ennen raportointia.
