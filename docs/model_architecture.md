# Model Architecture

The MVP uses layered rule models with ML-ready interfaces. Production models should replace each rule layer with walk-forward trained and calibrated estimators.

## A. Long-Term Vulnerability Model

Goal: predict 6-24 month systemic risk.

Inputs:

- credit/GDP gap
- leverage
- valuation
- debt maturity structure
- real estate prices
- corporate debt burden
- bank capital
- lending standards
- rate increase magnitude
- credit spreads

Outputs:

- `financial_system_vulnerability_score`
- `crisis_probability_12m`
- `most_vulnerable_sectors`

## B. Medium-Term Pullback Risk Model

Goal: predict 2-12 week pullback risk.

Inputs:

- momentum
- market breadth
- valuation percentile
- rate changes
- dollar changes
- VIX
- credit spreads
- flows
- positioning
- earnings revisions
- news sentiment

Outputs:

- 20-day max drawdown probability
- 60-day max drawdown probability
- expected drawdown
- risk source decomposition

## C. Short-Term Trigger Model

Goal: predict 1-5 day sharp decline or sharp rebound.

Inputs:

- option gamma
- 0DTE
- volume
- order book depth
- news shocks
- key data calendar
- premarket futures
- volatility term structure
- ETF creations/redemptions
- sector rotation
- flows

Outputs:

- sharp drop probability
- sharp rebound probability
- intraday range
- key trigger levels

## D. Bottom Bounce Model

Goal: predict 10-day and 20-day rebound probabilities.

Inputs:

- drawdown depth
- panic intensity
- VIX percentile
- Put/Call percentile
- credit-spread changes
- breadth repair
- volume climax
- ETF redemption climax
- short covering
- policy change
- rate decline
- dollar decline
- bad-news resilience

Outputs:

- 10-day bounce probability
- 20-day bounce probability
- whether it is likely a dead-cat bounce
- whether it may form a medium-term bottom

## MVP Model Families

First-stage MVP:

- rules-based score models
- `LogisticRegression`
- `RandomForestClassifier`
- `HistGradientBoostingClassifier`
- `CalibratedClassifierCV`

Every model must emit calibrated probabilities and persist forecast records before realized outcomes are known.

## Regime-Aware Ensemble

The backend includes separate model slots under `backend/app/services/models/regime_models/`:

- `bull_model`
- `bear_model`
- `panic_model`
- `recovery_model`
- `high_vol_model`

The ensemble first identifies market regime, selects the matching model, blends it with a fallback cross-asset risk model, and emits up/down/sideways probabilities. Production ML models should replace these rule slots without changing the API contract.

## Probability Calibration

Use `backend/app/services/models/calibration.py` for:

- Platt scaling
- isotonic regression
- Brier-score optimization
- Brier score
- log loss
- calibration curves

When the system emits `down_probability = 0.70`, realized down frequency in the matching validation bucket should be close to 70%.
