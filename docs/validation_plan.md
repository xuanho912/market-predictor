# Validation Plan

Validation quality is the core engineering constraint. A model that performs well only because of leakage is invalid.

## Required Validation

- walk-forward validation only
- no random shuffling of time-series rows
- no global normalization fit on the full dataset
- no centered rolling windows
- no backward fill from future observations
- no macro revision leakage
- no point-in-time universe leakage
- no overlapping-label contamination without purge or embargo analysis
- point-in-time data only
- macro data aligned by true public release timestamp
- no survivorship bias
- no future constituents, future index weights, future earnings, or future close leakage
- no accuracy-only reporting
- execution backtests must include costs and stressed execution assumptions

## Walk-Forward Split

Baseline split:

```text
train:      [start, t0]
calibrate:  (t0, t1]
test:       (t1, t2]
roll forward and repeat
```

The executable validation engine is `backend/app/services/backtesting/walk_forward_engine.py`.

Historical replay must:

- train or estimate model state only on data before forecast day `t`
- predict `t+1`, `t+3`, `t+5`, `t+10`, `t+20`, and `t+60`
- persist each horizon forecast before realized outcomes are attached
- evaluate only after the relevant future horizon has elapsed

Each split must record:

- train start and end
- calibration start and end
- test start and end
- embargo length, if labels overlap
- feature version
- label version
- model version

## Metrics

Probability quality:

- Brier score
- log loss
- calibration curve
- expected calibration error
- calibration slope and intercept
- reliability curve

Decision usefulness:

- AUC
- PR-AUC
- precision and recall by probability bucket
- precision
- recall
- F1
- false alarm rate
- crisis recall
- average lead time before drawdowns
- hit rate by regime

Robustness:

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
- performance by monetary policy regime
- performance by volatility regime
- performance by bull and bear market regimes
- performance before and after major market structure changes

## Feature Importance

Use `backend/app/services/analysis/feature_importance.py` to report:

- top 20 predictive features
- useless features
- unstable features
- regime-specific features
- permutation importance
- SHAP status or SHAP values when available
- feature group ablation
- correlation leakage flags

## Class Imbalance

Financial crises are rare. Crisis models must not learn to always predict no crisis.

Required controls:

- class weights or cost-sensitive learning
- PR-AUC in addition to ROC-AUC
- recall and false-alarm monitoring for crisis buckets
- calibrated probability thresholds selected only on validation windows
- base-rate reporting by regime and horizon

## Execution Cost And Stress Assumptions

Backtests must include:

- commissions
- bid-ask spread
- market impact
- slippage
- liquidity limits
- no-fill or stressed-fill assumptions during extreme markets

This project does not place trades, but any validation of signal usefulness must account for market frictions.

## Backtest Audit Checklist

Before trusting a result, verify:

- Features are shifted so labels do not leak into predictors.
- Macro and fundamental data use release timestamps or vintages.
- The model never sees test-period data during fitting, scaling, feature selection, or calibration.
- Universe membership is point-in-time.
- Index weights and constituents are point-in-time.
- Financial statements and earnings revisions are known-at timestamped.
- Same-day close is not used before the forecast timestamp.
- The same prediction record format is used in research and production.
- The strategy does not assume execution or trading because this project does not automate orders.
