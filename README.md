# eikaisiinä

Julkinen koe: kuinka paljon äly lisää pääomaa, kun lähtöpotti on 1 000 € ja
kaikki suunnittelu tulee tekoälyltä. Pitkän matkan tavoite 10 000 000 €.

## Säännöt

1. Kaikki laillista. Ei huijausta, ei sisäpiiritietoa, ei toisten rahoja.
2. Ihminen painaa aina nappia. Tekoäly ei tee kauppoja eikä siirrä rahaa.
3. Jokainen euron liike kirjataan `kirjanpito/ledger.csv`-tiedostoon.
4. Jokainen päätös ja sen perustelu kirjataan `kirjanpito/paatokset.md`-tiedostoon
   ennen toimeenpanoa, ei jälkikäteen.
5. Tulos julkaistaan sellaisenaan, kasvoi potti tai ei.

## Kaistat

| Kaista | Pääoma | Mitä mittaa |
|---|---|---|
| 1. Bounty | 0 € | Tuottaako pelkkä äly rahaa ilman pääomaa |
| 2. Tieto | 300 € | Onko mallilla informaatioetua ennustemarkkinoilla |
| 3. Omistus | 700 € | Ainoa historiallinen 10 000x-reitti: oma tuote |

## Mittarit

- Potin arvo euroina, päivitetään viikoittain
- Tunnit käytetty per kaista
- Euroa per tunti per kaista

## Rakenne

```
kirjanpito/       ledger.csv, paatokset.md, viikkoraportit
kaista1-bounty/   haku- ja analyysiputki auditointikilpailuihin
kaista2-tieto/    ennustemarkkinamalli
kaista3-omistus/  tuote
```
