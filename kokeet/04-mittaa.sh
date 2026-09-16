#!/bin/sh
# Koe 04: päivittäinen liikennemittaus. Ajetaan kerran päivässä 14 päivää postauksesta.
# U = ylätason views.uniques haettuna T+14 vrk (±6 h); päivittäiset rivit ovat taustatietoa.
# Repo-osoite REPO-muuttujassa; oletus on Constraint Works -identiteetin repo.
cd "$(dirname "$0")/.." || exit 1
REPO="${REPO:-constraint-works/constraint-works}"  # julkinen tutkimusrepo (Constraint Works)
d=$(date -u +%Y-%m-%dT%H:%M:%SZ)
v=$(gh api repos/$REPO/traffic/views 2>/dev/null)
c=$(gh api repos/$REPO/traffic/clones 2>/dev/null)
ref=$(gh api repos/$REPO/traffic/popular/referrers 2>/dev/null)
r=$(gh api repos/$REPO --jq '{stars: .stargazers_count, forks: .forks_count, watchers: .subscribers_count, private: .private}')
printf '{"aika":"%s","views":%s,"clones":%s,"referrers":%s,"repo":%s}\n' "$d" "${v:-null}" "${c:-null}" "${ref:-null}" "$r" >> kokeet/04-traffic.jsonl
tail -1 kokeet/04-traffic.jsonl | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['aika'], 'views', d['views'] and d['views'].get('uniques'), 'clones', d['clones'] and d['clones'].get('uniques'), d['repo'])"
