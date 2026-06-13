# Feature Groups

Every indicator must map to exactly one group. Important indicators should produce feature variants for `level`, `change`, `acceleration`, `percentile`, `cross_signal`, and `divergence`.

| Group | Required Coverage | Main Uses |
| --- | --- | --- |
| price | index OHLCV, ETFs, futures, sectors, factor indices | trend, pullback, bounce, reversal |
| volatility | VIX, VVIX, VIX futures curve, MOVE, implied/realized volatility, skew, tail risk | short-horizon risk, panic, crash warning |
| credit | IG OAS, HY OAS, CCC spreads, CDS, bank CDS, leveraged loans, CLOs, commercial paper spreads, lending standards | crisis, credit stress, systemic risk |
| rates | Fed funds, SOFR, 3M, 2Y, 5Y, 10Y, 30Y, real yields, inflation expectations, term premium, yield curve | policy regime, valuation pressure, liquidity |
| liquidity | central bank balance sheets, bank reserves, reverse repo, TGA, repo rates, Treasury depth, ETF discounts, dollar liquidity, cross-currency basis | amplification, funding stress |
| macro | GDP, CPI, PCE, PPI, payrolls, unemployment, claims, wages, retail sales, industrial production, PMI, ISM, permits, confidence, inventories | slow-cycle risk and policy path |
| earnings | EPS growth, revenue growth, margins, revisions, surprises, call sentiment, buybacks, cash-flow quality | medium-term equity risk |
| positioning | margin balance, margin debt, CFTC COT, CTA, risk parity, vol-control funds, ETF flows, OI, gamma exposure, short interest | crowded trade and forced-flow risk |
| breadth | advance/decline, highs/lows, percent above 20/50/200d MA, equal/cap weight, small/large, cyclical/defensive, high-beta/low-vol | trend confirmation and fragility |
| news_text | central bank statements, FOMC, earnings calls, announcements, ratings, filings, headlines, geopolitics, social, search, narratives | triggers and fast regime shifts |
| onchain_crypto | BTC/ETH, funding, OI, liquidations, stablecoins, exchange net flows, active addresses, whale wallets, DeFi liquidations | crypto stress and liquidity spillover |
| alternative_data | card spending, air traffic, hotels, ports, hiring, app activity, e-commerce, rent, used cars, invoices, sentiment | early fundamental changes |

## Feature Contract

Each feature should declare:

- name
- group
- source
- provider
- frequency
- transform
- lookback window
- release lag
- known-at timestamp
- missing-value policy
- expected direction by label and regime, if known

## Naming

Use:

```text
{group}__{source}__{measure}__{window}__{transform}
```

Examples:

- `credit__hy_oas__spread__20d__change`
- `breadth__nyse__new_highs__252d__percentile`
- `volatility__vix_vvix__tail_confirmation__1d__cross_signal`
- `price__spx_credit__risk_divergence__20d__divergence`
