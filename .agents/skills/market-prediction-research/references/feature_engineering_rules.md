# Feature Engineering Rules

Do not feed only raw values. Important indicators must generate six feature types.

## Required Transforms

- `level`: current value at the forecast timestamp.
- `change`: 1d, 5d, 20d, and 60d changes.
- `acceleration`: change in the change rate, such as 5d change minus prior 5d change.
- `percentile`: rolling percentile over 1, 3, 5, and 10 years.
- `cross_signal`: confirmation or non-confirmation across markets.
- `divergence`: disagreement between price and breadth, credit, volatility, bonds, dollar, or banks.

## Divergence Examples

- Equity rises while credit spreads widen: risk divergence.
- Index reaches a new high while fewer stocks reach new highs: breadth divergence.
- Equity bounces while high-yield bonds fail to confirm: weak rebound quality.
- VIX falls while VVIX stays elevated: tail risk remains.
- Bad news worsens but price stops making new lows: bad news may be priced.

## Implementation Rules

- Compute rolling statistics using only past data.
- Fit normalization inside each train window.
- Store transform parameters and windows.
- Keep raw feature, transformed feature, and timestamp metadata separate.
- Test feature direction by regime instead of assuming a universal sign.
