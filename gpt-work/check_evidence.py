#!/usr/bin/env python3
"""Read local research data, show unresolved commercial gates, reproduce arithmetic.
No network, credentials, spending, contact or writes. Run from any directory.
A passed data check is not validation of source truth or commercial viability.
"""
import json
from pathlib import Path
from decimal import Decimal

ROOT = Path(__file__).resolve().parent

def main():
    audit = json.loads((ROOT / "data/orphan-proxy-audit.json").read_text())
    cards = json.loads((ROOT / "data/mechanism-cards.json").read_text())["cards"]
    cases = audit["cases"]
    excluded = sum(c["classification"] == "PROXY_REJECT" for c in cases)
    unknown = sum(c["classification"] == "UNKNOWN" for c in cases)
    if (len(cases), excluded, unknown) != (10, 4, 6):
        raise ValueError("Audit count differs from the recorded exploratory sample")
    if len({c["repo"] for c in cases}) != len(cases):
        raise ValueError("Duplicate sample repository")
    print(f"Exploratory sample: {len(cases)}; proxy deductions rejected: {excluded}; unresolved: {unknown}")
    required = {"named_payer", "current_cost_evidence", "legal_access", "payment_basis",
                "reuse_right", "observed_second_case_advantage"}
    for card in cards:
        gates = card["commercial_gates"]
        if set(gates) != required:
            raise ValueError(f"Missing or unexpected gates: {card['id']}")
        unresolved = [key for key, value in gates.items()
                      if value["status"] != "FACT" or not value["evidence"]]
        if card["qualified_opportunity"] and unresolved:
            raise ValueError(f"Unsupported opportunity claim: {card['id']}")
        print(f"{card['id']}: unresolved gates {len(unresolved)}/{len(required)}")
    agent_prizes = [3000, 3500, 5000]
    agent_submissions = [116, 117, 122]
    all_prizes = agent_prizes + [5000, 5000, 3000, 1000, 600, 500, 10000, 1000]
    print("Claude table prize total (USD):", sum(all_prizes))
    print("Agent-only prize/submission ratio, NOT own EV:",
          round(sum(agent_prizes)/sum(agent_submissions), 4))
    print("Gallery arithmetic (submitted projects):", 33*24+20)
    print("Projects/registered people ratio, NOT individual completion rate:",
          round(812/51882*100, 4))
    rate = Decimal("11300000") / Decimal("24000000000")
    fee = Decimal("0.25")  # Hypothetical, NOT reported by PRGX.
    print("Vendor case recovery/spend percentage:", rate*100)
    print("Toy fee per EUR 1m spend, NOT forecast:", rate*fee*1000000)
    print("Toy break-even spend for EUR 300 cost, NOT forecast:", Decimal(300)/(rate*fee))

if __name__ == "__main__":
    main()
