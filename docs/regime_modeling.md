# Regime Modeling

Market regime is a first-stage inference that changes feature interpretation, model selection, and probability calibration.

## Regimes

- `bull_trend`: persistent upward trend, healthy breadth, contained volatility.
- `bear_trend`: falling trend, weak breadth, failed rallies.
- `sideways`: range-bound market with mean reversion.
- `panic`: rapid selloff, volatility spike, forced de-risking.
- `oversold_bounce`: rebound setup after extreme selling pressure.
- `topping`: index strength with weakening breadth, credit, leadership, or earnings.
- `bottoming`: selling pressure exhausted and internals repairing.
- `recovery`: improving risk appetite after a drawdown or recession scare.
- `liquidity_crunch`: funding, repo, dollar liquidity, or market depth stress dominates.
- `credit_stress`: credit spreads, banks, loans, or funding conditions deteriorate.
- `crisis_mode`: synchronized equity, credit, liquidity, banking, and macro stress.

## Indicator Interpretation

Examples:

- RSI near 30 in `bull_trend` can increase bounce probability.
- RSI near 30 in `crisis_mode` can indicate downside continuation.
- VIX falling during a low-quality rebound is not enough if VVIX, credit, and banks do not confirm.
- Equity strength during `topping` is weaker evidence if breadth and credit diverge.

## Storage

Persist:

- hard regime label
- regime probabilities
- regime model version
- features used for regime detection
- timestamp and known-at rules

Task models should store which regime input they used.
