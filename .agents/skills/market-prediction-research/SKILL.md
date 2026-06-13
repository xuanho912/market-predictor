---
name: market-prediction-research
description: Use this skill whenever working on market prediction, macro risk modeling, pullback forecasting, crisis early warning, bounce detection, trading signal validation, feature engineering, financial time-series backtesting, or point-in-time market data pipelines. This skill forces the agent to define labels first, separate horizons and regimes, use credit/liquidity/options/breadth data, prevent leakage, and validate with walk-forward probability calibration.
---

# Market Prediction Research

Use this skill to keep market prediction work leakage-safe, probability-based, regime-aware, horizon-specific, and auditable.

## 1. Define Labels Before Data

Any prediction task must define target labels before adding indicators. Include at least:

- `future_return_1d`, `future_return_3d`, `future_return_5d`, `future_return_10d`, `future_return_20d`, `future_return_60d`
- `trend_label`: `up` / `down` / `sideways`
- `pullback_5d`, `pullback_20d`, `pullback_60d`
- `downside_continuation_10d`, `downside_continuation_20d`
- `bounce_5d`, `bounce_10d`, `bounce_20d`
- `trend_reversal_20d`, `trend_reversal_60d`
- `crash_risk_60d`, `crash_risk_120d`, `systemic_crisis_180d`

Before adding a feature, write the label definition, horizon, threshold, timestamp convention, validation metric, and expected base rate. Read `references/label_definitions.md` when implementing labels.

## 2. Decompose Market Risk Into Four Layers

For every drawdown, crisis, or bounce analysis, separate:

- Vulnerability: valuation, leverage, credit expansion, debt, crowded positioning, earnings quality, bank and non-bank risk.
- Trigger: CPI, payrolls, central bank decisions, rate jumps, dollar liquidity tightening, geopolitics, bank failures, fund liquidation, mega-cap earnings breaks, policy/regulatory changes, FX and commodity shocks.
- Amplifier: forced liquidation, option gamma, CTA/risk-parity/vol-control selling, ETF redemptions, credit spread widening, collateral decline, thinner liquidity.
- Confirmation: moving-average breakdowns, breadth deterioration, credit widening, VIX rise, high-yield/bank/small-cap underperformance, dollar strength, safe-haven strength, high-volume declines and weak-volume rebounds.

Map every explanation to at least one layer. Read `references/market_prediction_framework.md` for the full workflow.

## 3. Model By Horizon

Do not use one model for all horizons:

- 1 day: options, order book, news, premarket futures, flows, volatility.
- 1 week: technical structure, positioning, VIX, breadth, ETF flows.
- 1 month: breadth, credit spreads, rates, dollar, earnings revisions, flows.
- 3-12 months: credit, liquidity, macro, valuation, policy path.
- 1-3 years: debt, leverage, credit cycle, valuation bubbles, real estate, banking system.

Choose model families, features, validation windows, and calibration by horizon.

## 4. Model By Market Regime

Identify `market_regime` before interpreting features or training task models. Supported regimes:

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

The same indicator can mean different things in different regimes. Example: `RSI=30` can be a rebound signal during a bull-market pullback, but a downside-continuation signal during crisis selling. Read `references/regime_modeling.md` before adding regime logic.

## 5. Cover Required Data Providers And Feature Groups

Design data providers and feature groups for at least:

- price: index OHLCV, ETFs, futures, sectors, factor indices.
- volatility: VIX, VVIX, VIX futures curve, MOVE, implied/realized volatility, skew, tail risk.
- credit: IG OAS, HY OAS, CCC spreads, CDS, bank CDS, leveraged loans, CLOs, commercial paper spreads, lending standards.
- rates: Fed funds, SOFR, 3M, 2Y, 5Y, 10Y, 30Y, real yields, inflation expectations, term premium, yield curve.
- liquidity: central bank balance sheets, bank reserves, reverse repo, Treasury General Account, repo rates, Treasury market depth, ETF discounts/premiums, dollar liquidity, cross-currency basis.
- macro: GDP, CPI, PCE, PPI, payrolls, unemployment, claims, wages, retail sales, industrial production, PMI, ISM, building permits, consumer confidence, inventories.
- earnings: EPS growth, revenue growth, margins, estimate revisions, earnings surprises, call sentiment, buybacks, cash-flow quality.
- positioning: margin balance, margin debt, CFTC COT, CTA, risk parity, vol-control funds, ETF flows, option open interest, gamma exposure, short interest.
- breadth: advance/decline, new highs/lows, percent above 20/50/200-day moving averages, equal-weight/cap-weight, small/large, cyclical/defensive, high-beta/low-vol.
- news_text: central bank statements, FOMC, earnings calls, company announcements, rating reports, filings, headlines, geopolitics, social media, search trends, narrative shifts.
- onchain_crypto: BTC/ETH, funding rates, open interest, liquidations, stablecoin supply, exchange net flows, active addresses, whale wallets, DeFi liquidations.
- alternative_data: card spending, air traffic, hotels, ports, hiring, app activity, e-commerce, rent, used cars, invoices, sentiment.

Read `references/data_provider_catalog.md` and `references/feature_groups.md` before adding providers.

## 6. Engineer Six Feature Types

Do not feed only raw values. Important indicators should generate:

- `level`: current value.
- `change`: 1d/5d/20d/60d changes.
- `acceleration`: whether change speed is increasing.
- `percentile`: 1/3/5/10-year historical percentile.
- `cross_signal`: cross-market confirmation or non-confirmation.
- `divergence`: disagreement between price and breadth, credit, volatility, bonds, dollar, or bank stocks.

Required divergence examples:

- Equity up while credit spreads widen means risk divergence.
- Index new highs with fewer stocks making new highs means breadth divergence.
- Equity bounce without high-yield confirmation means weak rebound quality.
- VIX falls while VVIX does not fall means tail risk remains.
- Bad news increases but price stops making new lows can mean bad news is priced.

Read `references/feature_engineering_rules.md` before implementing features.

## 7. Separate Normal Pullbacks From Crises

Normal pullback models and crisis models must be separate. A normal pullback can include equity weakness, VIX rise, and weaker breadth while credit, banks, funding, liquidity, and macro remain functional.

Crisis-warning models require cross-asset deterioration: equities, credit, funding, banks, and dollar liquidity all worsening together. One-sentence rule: when equities alone fall, it may be a pullback; when equities, credit, funding, banks, and dollar liquidity deteriorate together, it looks like crisis risk.

Read `references/pullback_crisis_bounce_rules.md` before building drawdown or crisis models.

## 8. Separate Bounces From Durable Bottoms

Bounce models should not try to find the exact low. They should estimate whether selling pressure is exhausted, leverage has been cleared, credit and liquidity stopped worsening, bad news no longer pushes price to new lows, breadth is repairing, and money is returning to risk assets.

Dead-cat bounce features:

- short-covering-driven rebound
- weak volume
- poor breadth
- credit spreads still widening
- banks not confirming
- only temporary VIX decline
- earnings estimates still falling
- liquidity not improving
- rebound fails at moving-average resistance

More reliable bottoming features:

- panic has been released
- credit spreads stop widening
- VIX spikes then reverses
- breadth clearly repairs
- equal-weight outperforms
- small caps and cyclicals participate
- banks stabilize
- bad news no longer creates new lows
- policy or liquidity turns
- heavy volume followed by sustained absorption
- earnings downgrades slow
- money rotates from safe havens back into risk assets

## 9. Prevent Leakage

For every feature, define `known_at_timestamp`. A feature is usable only when `known_at_timestamp <= forecast_timestamp`.

Prohibit:

- random train/test splits for time series
- centered rolling windows
- backward filling from future values
- fitting scalers, imputers, feature selectors, or calibrators on the full dataset
- macro data without vintage or release timestamp
- survivorship-biased index membership
- using revised data as if it were known historically

Run `scripts/audit_no_leakage.py` on changed research code and docs when practical.

## 10. Use Layered Model Architecture

Implement and preserve four model layers:

- Long-term vulnerability model: 6-24 month systemic risk from credit/GDP, leverage, valuation, debt structure, real estate, corporate debt burden, bank capital, lending standards, rate increases, and credit spreads. Output financial system vulnerability score, 12-month crisis probability, and most vulnerable sectors.
- Medium-term pullback risk model: 2-12 week pullback from momentum, breadth, valuation percentile, rates, dollar, VIX, credit, flows, positioning, earnings revisions, and news sentiment. Output 20d/60d drawdown probabilities, expected drawdown, and risk source breakdown.
- Short-term trigger model: 1-5 day sharp drop or rebound from gamma, 0DTE, volume, depth, news shocks, data calendar, premarket futures, volatility term structure, ETF activity, sector rotation, and flows. Output sharp drop probability, sharp rebound probability, intraday range, and trigger levels.
- Bottom bounce model: 10d/20d rebound from drawdown depth, panic, VIX/put-call percentiles, credit changes, breadth repair, volume climax, ETF redemption climax, short covering, policy change, rate decline, dollar decline, and bad-news resilience. Output 10d/20d bounce probability, dead-cat risk, and medium-term bottom probability.

Read `references/model_layers_and_scores.md` before adding model code.

## 11. Output Three Core Scores

Always output 0-100:

- `pullback_risk_score`
- `crisis_risk_score`
- `bounce_quality_score`

Use the starting weights in `references/model_layers_and_scores.md`. Do not replace these scores with vague commentary.

## 12. Use Strict Validation

Validation must include point-in-time data, true macro release timestamp alignment, no random split, walk-forward validation, regime tests, probability calibration, AUC, PR-AUC, precision, recall, F1, class-imbalance controls, survivorship-bias controls, and realistic execution-cost assumptions.

Read `references/validation_rules.md` before writing training, backtesting, or validation code.

## 13. Require Feature Importance And Ablation

Every validated model must include:

- permutation importance
- feature group ablation
- unstable feature detection
- regime-specific feature importance
- correlation leakage checks against future targets

Do not trust a model only because headline metrics look good. If removing credit, liquidity, options, or breadth features does not change performance, investigate whether the model is learning a shortcut, leakage, or a weak signal.

## 14. API Output Must Be Predictive

Frontend and API outputs must include:

- current `market_regime`
- horizon forecasts for 1d/3d/5d/10d/20d/60d with up/down/sideways probabilities, expected return, p50 upside/downside, and confidence
- `pullback_risk_score`
- `crisis_risk_score`
- `bounce_probability`
- `bounce_quality_score`
- `downside_continuation_probability`
- `trend_reversal_probability`
- `dead_cat_bounce_risk`
- `top_reasons`
- `historical_similar_days`
- current risk source breakdown

Do not produce dashboard-only output that lacks forward probabilities.

## 15. Keep MVP Boundaries

First-stage MVP scope:

- symbols: `SPY`, `QQQ`, `IWM`, `DIA`
- automatic data refresh path
- automatic feature generation
- automatic labels
- rules score model
- `LogisticRegression`, `RandomForest`, `HistGradientBoosting`, `CalibratedClassifierCV`
- walk-forward backtest
- mobile PWA dashboard
- Codex Skill, AGENTS.md, README, Docker one-command startup

Do not add broker integration, order placement, or automated trading.

## 16. Use Walk-Forward Probability Calibration

Validation must use walk-forward splits:

```text
train -> calibrate -> test -> roll forward
```

Report probability metrics, not only accuracy:

- Brier score
- log loss
- calibration curve
- expected calibration error
- precision and recall by probability bucket
- false alarm rate
- crisis recall and lead time

## 17. Persist Forecast Records

Every production prediction must be saved with:

- forecast timestamp
- label and horizon
- regime
- model version
- feature snapshot version
- raw probability
- calibrated probability
- up/down/sideways probabilities
- bounce probability
- crash probability
- actual future return when realized
- error metrics when realized
- explanation drivers
- realized label when available
- future scoring metrics when available

Never let the frontend become the source of prediction logic. The mobile app only displays backend outputs.

## 18. Freeze Alpha Candidates Before Forward Validation

When an alpha candidate is found, freeze the rule before doing any further evaluation. Do not keep tuning thresholds, features, labels, regimes, or model parameters on the same historical sample.

Hard rules:

- Freeze the signal name, version, threshold definition, eligible symbols, horizons, validation start date, and prohibited uses.
- Treat any post-hoc alpha as a research candidate until it passes forward validation.
- Compare every candidate with simple baselines such as RSI oversold, VIX spike, drawdown, simple mean reversion, and random same-frequency signals.
- Never call one historical backtest a confirmed alpha.
- Save every live signal, including pending, skipped, failed, and completed observations.
- If a future change uses a different feature set, threshold, model, label, or regime rule, create a new version such as `alpha_v2`. Do not contaminate `alpha_v1`.

Current frozen research candidate:

- `bounce_probability_top_decile_v1` can only be treated as a research alpha candidate.
- `bounce_probability_top_decile_v1` means a long-bounce / mean-reversion candidate, not a long-term market direction call.
- `down_probability` and `crash_probability` failed current validation as trading signals and must not be used as active trade triggers.
- Volatility is the strongest current information source, with small credit contribution, but both require forward validation before paper trading.

## 19. Use Historical Analogs As Context, Not Proof

When a user asks to "let history train the model", "learn from similar history", or "find markets like today", prefer a Historical Analog Engine over any model that memorizes history.

Hard rules:

- Use historical samples for similar-scenario retrieval, conditional distributions, and explanation only.
- Do not use historical analog results as a post-hoc reason to retune thresholds, labels, features, regimes, horizons, or model parameters.
- Do not let historical analogs replace the frozen Alpha v1 rule or any forward validation requirement.
- Every analog output must include sample count, average results, worst-case results, shared features, and key differences from the current market.
- Historical similarity does not imply the future must repeat.
- If sample count is low, or the regime is crisis/high-volatility with few analogs, output a low-sample warning and avoid strong conclusions.
- Any analog-derived signal must be versioned separately and forward validated before research or trading use.

For Alpha v1:

- Historical analogs may answer whether current `bounce_probability_top_decile_v1` conditions look similar to prior successful bounce environments.
- Output `historical_support = supportive` only as contextual support.
- Output `historical_support = weak_or_conflicting` when samples are weak, mixed, sparse, or risk conditions differ.
- Never upgrade Alpha v1 to confirmed alpha because historical analogs look good.

## Non-Negotiable Summary

Always enforce: label-first design, walk-forward validation, regime-aware modeling, credit + liquidity + options + breadth inputs, no future leakage, no random train-test split, probability output with calibration, feature ablation, horizon-specific models, and persistent prediction logs for backtesting.
