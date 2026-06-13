"""Generate a Markdown feature dictionary template for market prediction work."""

from __future__ import annotations

import argparse
from pathlib import Path


FEATURE_GROUPS = {
    "price": "index OHLCV, ETFs, futures, sectors, factor indices",
    "volatility": "VIX, VVIX, VIX futures, MOVE, implied/realized volatility, skew, tail risk",
    "credit": "IG/HY/CCC spreads, CDS, bank CDS, leveraged loans, CLOs, commercial paper, lending standards",
    "rates": "Fed funds, SOFR, 3M, 2Y, 5Y, 10Y, 30Y, real rates, breakevens, term premium, curve",
    "liquidity": "central bank balance sheets, reserves, RRP, TGA, repo, Treasury depth, ETF discounts, dollar liquidity, cross-currency basis",
    "macro": "GDP, CPI, PCE, PPI, payrolls, unemployment, claims, wages, retail, industrial production, PMI, ISM, permits, confidence, inventories",
    "earnings": "EPS, revenue, margins, revisions, surprises, calls, buybacks, cash-flow quality",
    "positioning": "margin debt, CFTC COT, CTA, risk parity, vol-control funds, ETF flows, OI, gamma, short interest",
    "breadth": "advance-decline, highs/lows, percent above 20/50/200d MA, equal/cap weight, small/large, cyclical/defensive, high-beta/low-vol",
    "news_text": "central banks, FOMC, calls, announcements, ratings, filings, headlines, geopolitics, social, search, narratives",
    "onchain_crypto": "BTC/ETH, funding, OI, liquidations, stablecoins, exchange flows, active addresses, whale wallets, DeFi liquidations",
    "alternative_data": "card spending, air traffic, hotels, ports, hiring, app activity, e-commerce, rent, used cars, invoices, sentiment",
}

FEATURE_TRANSFORMS = ("level", "change", "acceleration", "percentile", "cross_signal", "divergence")


def build_markdown() -> str:
    rows = [
        "# Feature Dictionary",
        "",
        "| feature_name | group | provider_id | source | frequency | transform | known_at_timestamp | lag_policy | missing_value_policy | regime_notes | notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for group, examples in FEATURE_GROUPS.items():
        for transform in FEATURE_TRANSFORMS:
            rows.append(
                f"| `{group}__source__measure__window__{transform}` | `{group}` | TBD | TBD | TBD | `{transform}` | TBD | TBD | TBD | TBD | Examples: {examples}. |"
            )
    rows.extend(
        [
            "",
            "Every feature must be point-in-time safe and must map to exactly one group.",
            "Important indicators should include level, change, acceleration, percentile, cross_signal, and divergence variants.",
            "A feature is usable only when `known_at_timestamp <= forecast_timestamp`.",
        ]
    )
    return "\n".join(rows) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a feature dictionary Markdown template.")
    parser.add_argument("--output", "-o", default="feature_dictionary.md", help="Output Markdown file.")
    args = parser.parse_args()

    output = Path(args.output)
    output.write_text(build_markdown(), encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
