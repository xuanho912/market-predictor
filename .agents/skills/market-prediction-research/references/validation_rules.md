# Validation Rules

Use this reference before writing training, backtesting, or model evaluation code.

## Hard Rules

- Use walk-forward validation.
- Do not shuffle time-series samples.
- Fit preprocessing only on each train window.
- Calibrate only on calibration windows.
- Test only on future windows unseen by training and calibration.
- Store raw and calibrated probabilities.
- Store prediction records before realized labels are known.

## Leakage Checks

Flag code or notebooks that contain:

- `shuffle=True` <!-- audit-ignore: documented prohibited pattern -->
- `train_test_split` without `shuffle=False`
- centered rolling windows
- `.bfill()` on time series <!-- audit-ignore: documented prohibited pattern -->
- `shift(-...)` in feature code
- global scaler fit before splitting
- macro data without release timestamps
- index constituents without point-in-time membership

## Metrics

Probability:

- Brier score
- log loss
- calibration curve
- ECE
- calibration slope

Event:

- AUC
- PR-AUC
- precision
- recall
- F1
- precision by probability bucket
- recall by probability bucket
- false alarm rate
- lead time
- crisis recall

Regime:

- bull market
- bear market
- sideways
- high inflation
- low inflation
- rate hiking
- rate cutting
- crisis
- high volatility
- low volatility
- easing policy
- tightening policy

## Required Bias And Execution Controls

- Use point-in-time data.
- Align macro data by true release timestamps.
- Prevent survivorship bias, future constituents, future index weights, future earnings, and future close leakage.
- Handle rare crisis labels with class weights, threshold analysis, PR-AUC, and crisis recall.
- Include commission, spread, impact, slippage, liquidity limits, and stressed no-fill assumptions in any signal usefulness backtest.

## Feature Importance And Ablation

Every validated model should report:

- permutation importance
- SHAP status or SHAP values when available
- ablation by feature group
- useless features
- unstable features
- regime-specific features
- high-correlation leakage flags against future targets
