# What we measured about "abandoned" software before trying to make money from it

*Draft for omistaja's approval. Not published. Every number below is marked FACT in the
repository and links to the script or data file that produced it. Written 2026-09-16.*

## Why we looked

We are running a small open research project with a deliberately extreme question: how
much economic leverage can one person, two frontier AI models and 1,000 euros of
experimental capital get, legally? We do not claim any answer yet. The repository is the
full log, including the dead ends and the disagreements between the two models, which
review each other's work.

One early hypothesis was that "orphaned" digital assets, software with users but no
maintainer, had become valuable because AI makes maintenance nearly free. Before building
anything, we measured. The measurements killed the hypothesis, and the way they killed it
seemed worth sharing, because most of these numbers do not exist anywhere else.

## Chrome extensions: a quarter disappeared in 20 months

We took a public snapshot of the Chrome Web Store from January 2025 (203,746 extensions)
and drew a stratified random sample of 390 extensions that then had more than 10,000
users: 130 each from the 10k–100k, 100k–1M and 1M+ bands. In September 2026 we fetched
each store page.

- 91 of 390 (23%) are gone from the store. In January 2025 they had 98 million users
  between them (median 100,000).
- Of the 299 still listed, 93 (31%) had not been updated in two years. Most of the
  largest ones are corporate "finished" extensions, not abandoned ones.
- Among 1M+ extensions not updated in a year, the median user count fell 60% in the
  period (n=37). In smaller bands the store's rounding hides any change.

The timing overlaps Chrome's removal of Manifest V2 listings, but the dataset has no
manifest field, so that attribution is an inference, not a measurement.

## "Looking for maintainer": nobody wants money, and volunteers are not the bottleneck

GitHub search returns 1,066 open and 1,242 closed issues titled "looking for maintainer"
or similar. We read 40 open and 40 closed threads in full, including every comment.

- Owners who asked for money: 1 of 80. Owners who offered to sell: 0 of 80. Three
  explicitly declined money ("my bottleneck really isn't money").
- 35 of 40 open threads offered to hand the project over for free. Volunteers turned up
  in 38 of 40 (median about six people). Access was actually granted in 18 of 40.
- In the 31 closed threads where a new maintainer took over, 12 were prior contributors,
  13 were outsiders, 6 were mixed teams. Outsiders succeeded when they were a company, a
  known ecosystem figure, or had submitted pull requests first.
- Stated reasons for leaving: moved to other technology or stopped using it (13), no time
  (11), owner vanished (5), burnout, illness or death (4). Not one said maintenance was
  too expensive.
- In 2026 the same LLM-style volunteer boilerplate ("issue triage and reproduction, earn
  trust progressively") appeared in six of the sampled repositories on the same day from
  one account. In one thread users asked whether it was a bot. The AI-assisted "I'll take
  over maintenance" offer is already recognized as spam.

## One maintenance experiment: the code was fine, the button was missing

We timed an AI agent maintaining html5lib (last PyPI release 2020, 80 open issues, 20
open pull requests). In nine minutes and about 82,000 tokens it got 17,499 tests passing
on Python 3.14; the only breakage was packaging (`pkg_resources`, `ast.Str`) and the fix
took 13 seconds of command time. The same fix already existed in three open, mergeable
pull requests from volunteers, dated 2025–2026. A "please make a new release" issue has
been open since January 2024 with no reply from anyone holding release rights. The AI's
marginal contribution to the code was zero. The scarce input was a human with the
publish button.

## Orphaned PyPI packages mostly work

We sampled 20 packages at random (seed committed before looking) from the 959 most
downloaded PyPI packages with no release in two years and over 100,000 monthly downloads,
then tried a source build, import and wheel install on Python 3.14 in a clean
environment with a five-minute cap and no fixes.

- 15 of 20 built, installed and imported.
- 5 failed, each for a different reason: an undeclared Django dependency, a metapackage
  with no importable module, a removed pydantic 2 argument, `pkg_resources`, and one
  build that exceeded the cap.
- No single failure pattern appeared more than once. The pre-registered rule for
  "reusable fix knowledge exists" required at least three, so the branch was killed.

Of the 5,000 most downloaded npm packages, 1,674 (33.5%) have had no release in two
years, and they account for 30% of downloads. Most are finished utilities. "No commits"
is not "abandoned". (A data caveat: the aggregator we used had stale release dates for 11
of 30 sampled PyPI packages, so we re-verified all 1,116 against PyPI directly; 959 held.)

## WordPress: the directory owns the users

Among the 10,000 most popular WordPress.org plugins, 2,354 had no update in two years
(8.5 million active installs). Of the 166 with over 10,000 installs, 66 (40%) already
have a maintained replacement with a similar name in the directory, and in 59 cases the
replacement is already bigger. The official "adopt-me" tag lists 17 plugins with 3,210
installs combined. Users move to the fork; ownership never changes hands.

## Small assets for sale are not cheap

On one micro-startup marketplace, 39 public listings and 6 completed sales showed
asking prices around five times annual revenue for assets earning a few hundred dollars
a year, with a floor near 1,000 dollars. Six realized sales ranged 1.7x to 8.6x. There
is no bargain where there is a market.

## One unrelated number we found on the way

Finland's public register of authorized translators lists 1,381 people across 91
language pairs. Ukrainian to Finnish: 6. Somali to Finnish: 0. About 46,000 Ukrainians
currently hold temporary protection in Finland. We have no eligible language pair
ourselves, so this is an observation, not a plan.

## What we concluded, and what we didn't

The bottleneck in every case we measured was rights, trust or demand, never the cost of
writing code and never the 1,000 euros. We have not found a mechanism that passes our
own pre-registered test, and we have not made a euro. The repository contains the
scanners, the raw samples, the pre-registered protocols and both models' attempts to
destroy each other's reasoning, in Finnish.

If any of these numbers is wrong, the data files are there to check.
