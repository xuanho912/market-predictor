# Modeling Plan

Do not use one model for all market questions. Build separate tasks by label family, horizon, and market regime.

## Regime-Specific Modeling

First estimate `market_regime`, then train or condition task models on regime. Supported regimes:

- `bull_trend`
- `bear_trend`
- `sideways`
- `panic`
- `oversold_bounce`
- `topping`
- `bottoming`
- `recovery`
- `liquidity_crunch`
- `credit_stress`
- `crisis_mode`

Use one or more approaches:

- first-stage regime classifier
- separate models by regime
- regime interaction terms
- mixture-of-experts with regime probabilities
- regime-specific calibration curves

Do not assume that an indicator has the same sign across regimes.

## Horizon-Specific Model Families

### 1 Day

Primary signal groups:

- options and volatility
- order book or intraday liquidity
- news and event text
- premarket futures
- fund flow proxies

Models:

- calibrated logistic regression
- gradient boosting with strict timestamp controls
- event-aware classifiers

### 1 Week

Primary signal groups:

- technical structure
- positioning
- VIX and volatility term structure
- breadth
- ETF flows

Models:

- gradient boosting
- regularized logistic models
- regime-conditional ensembles

### 1 Month

Primary signal groups:

- market breadth
- credit spreads
- interest-rate changes
- dollar liquidity
- earnings revisions
- flows

Models:

- tree ensembles
- generalized additive models
- calibrated survival or hazard-style models for drawdowns

### 3-12 Months

Primary signal groups:

- credit
- liquidity
- macro
- valuation
- policy path

Models:

- slow-moving macro risk models
- dynamic factor models
- calibrated ensemble classifiers

### 1-3 Years

Primary signal groups:

- debt
- leverage
- credit cycle
- valuation bubbles
- real estate
- banking system stress

Models:

- low-frequency regime models
- early-warning crisis classifiers
- scenario and stress-testing models

## Probability Calibration

Every model must output calibrated probabilities. Preferred methods:

- Platt scaling for small datasets
- isotonic regression when enough validation data exists
- beta calibration for skewed probabilities
- rolling recalibration by walk-forward split

Store both raw and calibrated probabilities.

Calibrate by horizon and, where sample size allows, by regime. A crisis-mode probability calibration curve should not be reused unchanged for bull-trend pullbacks.

## Explanation Requirements

Every prediction should produce:

- top bullish drivers
- top bearish drivers
- top bounce drivers
- top crisis drivers
- changed-since-last-forecast summary
- confidence and caveats

Explanations must reference model evidence, not certainty.

## Separate Model Families

Build separate model families for:

- normal pullback
- downside continuation
- crisis warning
- oversold bounce
- dead-cat bounce risk
- durable bottoming
- trend reversal

Do not collapse ordinary pullback and systemic crisis labels into one binary "down" model.
