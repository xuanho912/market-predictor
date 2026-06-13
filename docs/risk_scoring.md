# Risk Scoring

Risk scores summarize calibrated probabilities across horizons. They are display and triage tools, not substitutes for the underlying model outputs.

## Core Scores

The API must output these three 0-100 scores:

- `pullback_risk_score`
- `crisis_risk_score`
- `bounce_quality_score`

## Pullback Risk Score

Starting weights:

- valuation overheat: 15%
- momentum extension: 15%
- breadth deterioration: 15%
- VIX/options risk: 10%
- positioning crowding: 15%
- rates up: 10%
- dollar strength: 5%
- earnings downgrades: 10%
- news/event risk: 5%

## Crisis Risk Score

Starting weights:

- credit/GDP gap: 15%
- credit spreads: 20%
- bank stress: 15%
- funding market stress: 15%
- non-bank leverage: 10%
- dollar liquidity: 10%
- macro recession risk: 10%
- policy response lag: 5%

## Bounce Quality Score

Starting weights:

- drawdown depth: 10%
- panic extreme: 15%
- volume expansion: 10%
- breadth repair: 15%
- credit spread stabilization: 20%
- VIX reversal: 10%
- policy/liquidity improvement: 10%
- bad-news resilience: 10%

## Legacy Score Inputs

Use calibrated probabilities for:

- `pullback_5d`
- `pullback_20d`
- `pullback_60d`
- `downside_continuation_10d`
- `downside_continuation_20d`
- `trend_reversal_20d`
- `trend_reversal_60d`
- `crash_risk_60d`
- `crash_risk_120d`
- `systemic_crisis_180d`

## Composite Scores

Short-term stress:

```text
0.35 * pullback_5d
+ 0.25 * downside_continuation_10d
+ 0.20 * volatility_stress_probability
+ 0.20 * breadth_break_probability
```

Medium-term drawdown risk:

```text
0.30 * pullback_20d
+ 0.25 * downside_continuation_20d
+ 0.25 * crash_risk_60d
+ 0.20 * credit_liquidity_stress_probability
```

Systemic risk:

```text
0.35 * systemic_crisis_180d
+ 0.25 * crash_risk_120d
+ 0.20 * credit_stress_probability
+ 0.20 * funding_liquidity_stress_probability
```

## Bands

Use bands only after calibration:

- 0-20: low
- 20-40: guarded
- 40-60: elevated
- 60-80: high
- 80-100: extreme

Never display a band without the probability, horizon, and last forecast timestamp.

## Explanation Template

Each score should include:

- current score and previous score
- biggest upward driver
- biggest downward driver
- horizon affected
- evidence strength
- caveat if data is stale or missing
