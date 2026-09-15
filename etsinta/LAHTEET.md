# Lähteet, joita skannataan jatkuvasti

Tila: `auto` = skripti hakee, `selain` = vaatii selaimen tai kirjautumisen, `käsin` = luetaan.

| Lähde | Mitä | Tila | Skripti |
|---|---|---|---|
| immunefi.com/bug-bounty | pysyvät bountyt, maksimit, päivityspäivät | auto | `tyokalut/haku/hae_immunefi.py` |
| mainnet-contest.sherlock.xyz | auditointikilpailut, historia | auto (vain päättyneet) | `tyokalut/haku/hae_kilpailut.py` |
| code4rena.com/api/v1/audits | auditointikilpailut | auto (vain päättyneet) | - |
| cantina.xyz/api/v0/competitions | auditointikilpailut | auto (vain päättyneet) | - |
| audits.sherlock.xyz, code4rena.com, cantina.xyz | käynnissä olevat kilpailut | selain | - |
| console.algora.io/api/trpc | avoimen koodin bountyt | auto (parametrit selvitettävä) | - |
| polar.sh | avoimen koodin bountyt | selain | - |
| ethglobal.com/events | hackathonit ja sponsoripalkinnot | selain | - |
| devpost.com/hackathons | hackathonit | selain (403 botille) | - |
| lablab.ai/event | tekoälyhackathonit | selain | - |
| gamma-api.polymarket.com/markets | ennustemarkkinat, hinnat, likviditeetti | auto | - |
| kaggle.com/competitions | ML-kilpailut | selain (API vaatii avaimen) | - |
| hackerone.com/directory/programs | web2-bountyt | selain | - |
| esp.ethereum.foundation, app.optimism.io/retro-funding, gitcoin.co | grantit | käsin | - |

| packages.ecosyste.ms/api/v1 | npm/PyPI-pakettien lataukset, julkaisut, riippuvuudet (PyPI-päivät vanhentuneita, varmenna) | auto | `tyokalut/haku/hae_orvot_paketit.py` |
| api.wordpress.org/plugins/info/1.2 | lisäosien asennukset, päivitys, tested up to, adopt-me | auto | `tyokalut/haku/hae_orvot_wordpress.py` |
| chromewebstore.google.com/detail/<id> | laajennuksen käyttäjät ja Updated-päivä (palvelinrenderöity) | auto (hidas) | `tyokalut/haku/hae_orvot_laajennukset.py` |
| akr.opintopolku.fi/akr/api/v1/translator | auktorisoidut kääntäjät kielipareittain | auto | - |
| github.com search "looking for maintainer" | luovutettavat projektit | auto (gh) | - |
| microns.io, extensionhub.io | pienten digitaalisten omaisuuksien hintapyynnöt | selain/curl | - |

## Lähteitä, joita ei ole vielä katsottu

- Suomen lakisääteiset henkilökohtaiset pätevyysrekisterit (generaattori, ks. AVOIN-HAARA-2)
- Huutokaupat.com konkurssipesät (JS-sivu, vaatii selaimen)
- tilastot.migri.fi (JS, hakemukset kansalaisuuksittain ja kielittäin)

- Sponsorien omat kehittäjäohjelmat (Stripe, Cloudflare, Vercel, Supabase): kehittäjäpalkinnot
- Business Finland, EU-hankkeet: julkinen innovaatioraha (hidas, byrokraattinen)
- Superteam Earn (Solana-ekosysteemin bountyt ja kilpailut)
- Replit, Cursor, Lovable, Bolt: alustojen omat rakentajakilpailut
- Kilpailut, joissa palkinto on omistus eikä raha (accelerator-ohjelmat)
