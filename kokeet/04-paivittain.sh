#!/bin/sh
# Koe 04: ajaa liikennemittauksen kerran vuorokaudessa 15 päivää (T+14 vrk -haku sisältyy).
cd "$(dirname "$0")/.." || exit 1
i=0
while [ $i -lt 15 ]; do
  REPO=constraint-works/constraint-works sh kokeet/04-mittaa.sh >> kokeet/04-paivittain.log 2>&1
  i=$((i+1))
  sleep 86400
done
