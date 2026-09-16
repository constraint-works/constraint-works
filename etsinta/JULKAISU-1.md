# What we measured about "abandoned" software before trying to make money from it

## Why we looked

This is an independent, pseudonymous experiment with a deliberately extreme question: how much economic leverage can one person, two frontier AI models and 1,000 euros of experimental capital get, legally? We claim no answer yet. The repository is the full log, including the disagreements between the two models, which review each other's work. The author's identity is not part of the project.

One early hypothesis was that "orphaned" digital assets, software with users but no maintainer, had become valuable because AI makes maintenance nearly free. Before building anything, we measured. The measurements killed the hypothesis.

## Chrome extensions: a quarter disappeared in 20 months

From a public January 2025 snapshot of the Chrome Web Store (203,746 extensions) we drew a stratified random sample of 390 extensions that then had over 10,000 users, 130 each from the 10k–100k, 100k–1M and 1M+ bands, and fetched each store page in September 2026.

- 91 of 390 (23%) are gone from the store. In January 2025 they had 98 million users between them (median 100,000).
- Of the 299 still listed, 93 (31%) had not been updated in two years; the largest are corporate "finished" extensions, not abandoned ones.
- Among 1M+ extensions not updated in a year, the median user count fell 60% (n=37).

The timing overlaps Chrome's removal of Manifest V2 listings; the dataset has no manifest field, so that is an inference.

## "Looking for maintainer": nobody wants money

GitHub search returns 1,066 open and 1,242 closed issues titled "looking for maintainer" or similar. We read 40 open and 40 closed threads in full.

- Owners who asked for money: 1 of 80. Owners who offered to sell: 0 of 80.
- 35 of 40 open threads offered the project for free. Volunteers appeared in 38 of 40 (median about six). Access was actually granted in 18 of 40.
- Of 31 closed threads with a new maintainer, 12 were prior contributors, 13 outsiders, 6 mixed. Outsiders succeeded when they were a company, a known ecosystem figure, or had submitted pull requests first.
- Stated reasons for leaving: moved on or stopped using it (13), no time (11), owner vanished (5), burnout, illness or death (4). Not one said maintenance was too expensive.
- In 2026 the same LLM-style volunteer boilerplate appeared in six sampled repositories on the same day from one account; in one thread users asked whether it was a bot. The AI-assisted "I'll take over maintenance" offer is already treated as spam.

## One maintenance experiment: the code was fine, the button was missing

We timed an AI agent maintaining html5lib (last PyPI release 2020, 80 open issues, 20 open pull requests). In nine minutes and about 82,000 tokens it had 17,499 tests passing on Python 3.14; the only breakage was packaging (`pkg_resources`, `ast.Str`) and the fix took 13 seconds. The same fix already existed in three open, mergeable pull requests from volunteers. A "please make a new release" issue has been open since January 2024 with no reply from anyone holding release rights. The AI's marginal contribution to the code was zero. The scarce input was a human with the publish button.

## Orphaned PyPI packages mostly work

We sampled 20 packages at random (seed committed before looking) from the 959 most downloaded PyPI packages with no release in two years and over 100,000 monthly downloads, then tried a clean source build, import and wheel install on Python 3.14 with a five-minute cap and no fixes.

- 15 of 20 built, installed and imported.
- 5 failed, each differently: an undeclared Django dependency, a metapackage with nothing to import, a removed pydantic 2 argument, `pkg_resources`, and one build over the cap.
- No failure pattern repeated. Our pre-registered rule for "reusable fix knowledge exists" required at least three, so that branch was killed.

Of the 5,000 most downloaded npm packages, 1,674 (33.5%) have had no release in two years and account for 30% of downloads. "No commits" is not "abandoned".

## WordPress: the directory owns the users

Among the 10,000 most popular WordPress.org plugins, 2,354 had no update in two years (8.5 million active installs). Of the 166 with over 10,000 installs, 66 (40%) already have a maintained, similarly named replacement in the directory, and in 59 cases it is already bigger. The official "adopt-me" tag lists 17 plugins, 3,210 installs combined. Users move to the fork; ownership never changes hands.

## Small assets for sale are not cheap

On one micro-startup marketplace, 39 listings showed asking prices around five times annual revenue for assets earning a few hundred dollars a year; six realized sales ranged 1.7x to 8.6x.

## One unrelated number

Finland's public register of authorized translators lists 1,381 people across 91 language pairs. Ukrainian to Finnish: 6. Somali to Finnish: 0. About 46,000 Ukrainians hold temporary protection in Finland. This is an observation, not a plan.

## What we concluded

Across the cases we measured, the recurring constraints were rights, trust and demand rather than the cost of writing code or the €1,000 budget. We have not found a mechanism that passes our own pre-registered test, and we have not made a euro. The repository holds the scanners, raw samples and pre-registered protocols, in Finnish. If a number is wrong, the data files are there to check.
