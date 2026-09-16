#!/bin/sh
# Koe 04: päivittäinen liikennemittaus. Ajetaan kerran päivässä 14 päivää postauksesta.
cd "$(dirname "$0")/.." || exit 1
d=$(date -u +%Y-%m-%dT%H:%M:%SZ)
v=$(gh api repos/original-private-account/eikaisiina/traffic/views 2>/dev/null)
c=$(gh api repos/original-private-account/eikaisiina/traffic/clones 2>/dev/null)
r=$(gh api repos/original-private-account/eikaisiina --jq '{stars: .stargazers_count, forks: .forks_count, watchers: .subscribers_count, private: .private}')
printf '{"aika":"%s","views":%s,"clones":%s,"repo":%s}\n' "$d" "${v:-null}" "${c:-null}" "$r" >> kokeet/04-traffic.jsonl
tail -1 kokeet/04-traffic.jsonl | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['aika'], 'views', d['views'] and d['views'].get('uniques'), 'clones', d['clones'] and d['clones'].get('uniques'), d['repo'])"
