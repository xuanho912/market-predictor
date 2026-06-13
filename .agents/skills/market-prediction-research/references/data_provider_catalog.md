# Data Provider Catalog

Design providers with point-in-time metadata: observation timestamp, release timestamp, revision timestamp, known-at timestamp, vendor, symbol, and ingestion timestamp.

## Required Provider Families

- `price`: index OHLCV, ETFs, futures, sector indices, factor indices.
- `volatility`: VIX, VVIX, VIX futures curve, MOVE, implied/realized volatility, skew, tail-risk indicators.
- `credit`: IG OAS, HY OAS, CCC spread, CDS, bank CDS, leveraged loans, CLOs, commercial paper spreads, lending standards.
- `rates`: Fed funds, SOFR, 3M, 2Y, 5Y, 10Y, 30Y, real rates, inflation expectations, term premium, yield curve.
- `liquidity`: central bank balance sheets, reserves, reverse repo, TGA, repo rates, Treasury depth, ETF discount/premium, dollar liquidity, cross-currency basis.
- `macro`: GDP, CPI, PCE, PPI, payrolls, unemployment, claims, wages, retail, industrial production, PMI, ISM, permits, confidence, inventories.
- `earnings`: EPS growth, revenue growth, margins, revisions, surprises, call sentiment, buybacks, cash-flow quality.
- `positioning`: margin balance, margin debt, CFTC COT, CTA, risk parity, vol-control funds, ETF flows, option OI, gamma exposure, short interest.
- `breadth`: advance/decline, highs/lows, percent above 20/50/200d MA, equal/cap weight, small/large, cyclical/defensive, high-beta/low-vol.
- `news_text`: central bank statements, FOMC, earnings calls, announcements, rating reports, filings, headlines, geopolitics, social media, search trends, narrative shifts.
- `onchain_crypto`: BTC/ETH, funding, OI, liquidations, stablecoin supply, exchange net flows, active addresses, whale wallets, DeFi liquidations.
- `alternative_data`: card spending, air traffic, hotels, ports, hiring, app activity, e-commerce, rent, used cars, invoices, sentiment.

## Provider Interface Requirements

Each provider should expose:

- `provider_id`
- `feature_group`
- `frequency`
- `source`
- `point_in_time_policy`
- `revision_policy`
- `publication_lag`
- `coverage_start`
- `symbols_or_series`

If a provider cannot prove point-in-time availability, mark it research-only and exclude it from backtests.
