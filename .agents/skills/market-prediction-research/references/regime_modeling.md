# Regime Modeling

Identify regime before model training and before explaining indicators.

## Supported Regimes

- `bull_trend`: rising trend, broad participation, contained volatility.
- `bear_trend`: falling trend, weak breadth, rallies fail.
- `sideways`: range-bound price action, mean reversion dominates.
- `panic`: rapid selloff, volatility spike, forced-flow behavior.
- `oversold_bounce`: rebound after extreme selling pressure.
- `topping`: index strength with deteriorating breadth, credit, or leadership.
- `bottoming`: selling pressure exhausted and internals repair.
- `recovery`: improving risk appetite after drawdown or recession scare.
- `liquidity_crunch`: funding and market-depth stress dominate.
- `credit_stress`: credit spreads, banks, loans, or funding markets deteriorate.
- `crisis_mode`: synchronized equity, credit, liquidity, banking, and macro stress.

## Interpretation Rule

The same indicator can change sign by regime. Examples:

- RSI near 30 in `bull_trend` can support bounce probability.
- RSI near 30 in `crisis_mode` can be downside continuation.
- Rising VIX in `sideways` can be noise; rising VIX with widening credit in `credit_stress` is systemic.
- Falling yields in `bull_trend` can be supportive; falling yields with bank underperformance can mean recession or funding stress.

## Modeling Pattern

Use one or more of:

- explicit regime classifier as the first-stage model
- separate models per regime
- regime interaction terms
- mixture-of-experts with regime probabilities
- regime-conditioned calibration curves

Store both the hard regime label and regime probabilities when possible.
