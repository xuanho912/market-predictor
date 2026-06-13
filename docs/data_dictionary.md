# Data Dictionary

Every feature must belong to exactly one feature group. Store point-in-time metadata for all features.

## Required Metadata

- `feature_name`
- `feature_group`
- `provider_id`
- `source`
- `symbol_or_series_id`
- `observation_timestamp`
- `release_timestamp`
- `revision_timestamp`
- `known_at_timestamp`
- `frequency`
- `transform`
- `lookback_window`
- `lag_policy`
- `missing_value_policy`
- `point_in_time_policy`
- `version`

## Required Feature Groups And Provider Coverage

| Group | Required Coverage | Leakage Notes |
| --- | --- | --- |
| price | Index OHLCV, ETFs, futures, sector indices, factor indices. | Use only prices available by forecast close or timestamp. |
| volatility | VIX, VVIX, VIX futures curve, MOVE, implied/realized volatility, skew, tail risk. | Align option data by timestamp and exchange calendar. |
| credit | IG OAS, HY OAS, CCC spread, CDS, bank CDS, leveraged loans, CLOs, commercial paper spreads, lending standards. | Prefer point-in-time spreads; avoid revised aggregates. |
| rates | Fed funds, SOFR, 3M, 2Y, 5Y, 10Y, 30Y, real rates, inflation expectations, term premium, yield curve. | Use release time and market close conventions. |
| liquidity | Central bank balance sheets, bank reserves, reverse repo, Treasury General Account, repo rates, Treasury market depth, ETF discounts/premiums, dollar liquidity, cross-currency basis. | Avoid same-day data if unavailable before forecast time. |
| macro | GDP, CPI, PCE, PPI, payrolls, unemployment, claims, wages, retail sales, industrial production, PMI, ISM, building permits, consumer confidence, inventories. | Store vintage and release timestamp to prevent revision leakage. |
| earnings | EPS growth, revenue growth, margins, estimate revisions, earnings surprises, call sentiment, buybacks, cash-flow quality. | Avoid including post-close results in pre-close forecasts. |
| positioning | Margin balance, margin debt, CFTC COT, CTA, risk parity, vol-control funds, ETF flows, option open interest, gamma exposure, short interest. | Respect publication lag. |
| breadth | Advance/decline, new highs/lows, percent above 20/50/200d MA, equal-weight/cap-weight, small/large, cyclical/defensive, high-beta/low-vol. | Universe must be point-in-time to avoid survivorship bias. |
| news_text | Central bank statements, FOMC, earnings calls, announcements, rating reports, filings, headlines, geopolitics, social media, search trends, narrative shifts. | Use timestamped text only. Deduplicate syndication. |
| onchain_crypto | BTC/ETH, funding rates, open interest, liquidations, stablecoin supply, exchange net flows, active addresses, whale wallets, DeFi liquidations. | Document chain finality and timestamp lag. |
| alternative_data | Card spending, air traffic, hotels, ports, hiring, app activity, e-commerce, rent, used cars, invoices, sentiment. | Vendor timestamp and revision policy must be explicit. |

## Required Feature Transforms

Important indicators should generate:

- `level`: current value.
- `change`: 1d, 5d, 20d, and 60d change.
- `acceleration`: whether the change speed is increasing.
- `percentile`: rolling percentile over 1, 3, 5, and 10 years.
- `cross_signal`: cross-market confirmation or non-confirmation.
- `divergence`: disagreement between price and breadth, credit, volatility, bonds, dollar, or bank stocks.

## Divergence Examples

- Equity up while credit spreads widen is risk divergence.
- Index new highs with fewer stocks making new highs is breadth divergence.
- Equity bounce without high-yield confirmation is poor rebound quality.
- VIX down while VVIX stays elevated means tail risk may remain.
- Bad news worsening while price stops making new lows can mean bad news is priced.

## Feature Naming

Use stable names:

```text
{group}__{source}__{measure}__{window}__{transform}
```

Examples:

- `price__spx__return__20d__change`
- `volatility__vix_vvix__tail_confirmation__1d__cross_signal`
- `credit__hy_oas__spread__20d__change`
- `breadth__spx_members__pct_above_ma__50d__level`
- `credit__spx_hy_oas__risk_divergence__20d__divergence`

## Point-In-Time Rule

A feature is usable at forecast timestamp `t` only if:

```text
known_at_timestamp <= t
```

For macro series, the initial release value and each revision must be separate records. Backtests must use the vintage known at the simulated forecast timestamp.
