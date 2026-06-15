---
name: market-prediction-research
description: Use this skill whenever working on market prediction, macro risk modeling, pullback forecasting, crisis early warning, bounce detection, forecast signal validation, feature engineering, financial time-series backtesting, or point-in-time market data pipelines. This skill forces the agent to define labels first, separate horizons and regimes, use credit/liquidity/options/breadth data, prevent leakage, and validate with walk-forward probability calibration. This project is a Market Prediction Dashboard, not a Trading Bot.
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

Do not add broker integration, order placement, simulated execution workflows, portfolio-accounting reports, position-management rules, or execution recommendations.

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
- Save every forecast observation, including pending, skipped, failed, and completed outcomes.
- If a future change uses a different feature set, threshold, model, label, or regime rule, create a new version such as `alpha_v2`. Do not contaminate `alpha_v1`.

Current frozen research candidate:

- `bounce_probability_top_decile_v1` can only be treated as a research alpha candidate.
- `bounce_probability_top_decile_v1` means a long-bounce / mean-reversion candidate, not a long-term market direction call.
- `down_probability` and `crash_probability` failed current validation as standalone forecast signals and must not be used as order triggers or execution recommendations.
- Volatility is the strongest current information source, with small credit contribution, but both require forward validation before they can be treated as reliable forecast inputs.

## 19. Keep Product Language Forecast-Only

This project is a Market Prediction Dashboard, not a Trading Bot. The dashboard must answer what market path is more probable and why; it must not tell the user how to execute orders, manage positions, size positions, or connect to brokers.

Use these terms:

- forecast signal
- forecast start date
- forecast horizon
- scenario validation
- forward return tracking
- prediction accuracy
- primary scenario hit rate
- high-confidence forecast validation
- invalidation condition
- risk condition

Avoid or remove these terms unless explicitly discussing something out of scope:

- order-simulation workflows
- execution-oriented signals
- position-management rules
- order-risk rules
- simulated portfolio accounting
- execution strategies
- execution recommendations
- actionable order recommendations

The first screen must directly answer:

- current most likely probability path
- second most likely path
- primary path probability
- primary versus secondary probability gap
- model confidence
- supporting evidence
- conflicting evidence
- invalidation conditions
- future horizons to observe

## 20. Use Historical Analogs As Context, Not Proof

When a user asks to "let history train the model", "learn from similar history", or "find markets like today", prefer a Historical Analog Engine over any model that memorizes history.

Hard rules:

- Use historical samples for similar-scenario retrieval, conditional distributions, and explanation only.
- Do not use historical analog results as a post-hoc reason to retune thresholds, labels, features, regimes, horizons, or model parameters.
- Do not let historical analogs replace the frozen Alpha v1 rule or any forward validation requirement.
- Every analog output must include sample count, average results, worst-case results, shared features, and key differences from the current market.
- Historical similarity does not imply the future must repeat.
- If sample count is low, or the regime is crisis/high-volatility with few analogs, output a low-sample warning and avoid strong conclusions.
- Any analog-derived signal must be versioned separately and forward validated before being treated as a reliable forecast component.

For Alpha v1:

- Historical analogs may answer whether current `bounce_probability_top_decile_v1` conditions look similar to prior successful bounce environments.
- Output `historical_support = supportive` only as contextual support.
- Output `historical_support = weak_or_conflicting` when samples are weak, mixed, sparse, or risk conditions differ.
- Never upgrade Alpha v1 to confirmed alpha because historical analogs look good.

## 21. Apply Wardley Mapping Before Building

Use the project Wardley strategy before adding non-trivial work. Read `docs/wardley_strategy.md` when changing product direction, adding data providers, adding dashboard modules, or restructuring deployment.

Core principle:

```text
Build what creates unique market-prediction judgment.
Buy, rent, or reuse commodity infrastructure.
```

The final user is the owner of this project. The user need is not a chat tool or an engineering demo. The page must directly answer:

- Is there edge today?
- Is the market more like bounce, downside continuation, sideways chop, or recovery?
- Which symbol has the strongest signal?
- What are the simulated future paths for SPY / QQQ / IWM / DIA?
- Do historical analogs support or conflict with the current setup?
- What is the biggest risk?
- What invalidates the forecast?
- What is current model confidence?

Classify every new feature:

- Genesis / Custom: self-build only when it improves prediction, explanation, or validation quality.
- Product / Rental: use providers, APIs, managed services, or existing libraries.
- Commodity / Utility: keep low priority and avoid custom engineering.
- Do Not Build: reject work that distracts from prediction quality.

Self-build focus:

- Market State Engine
- Edge / No Edge
- Historical Analog explanations
- Signal Agreement
- Confidence Score
- Simulated Path Weighting
- Predictor Ensemble
- Invalidation Conditions
- Daily Market Brief judgment quality
- High-confidence signal validation

Use or rent:

- Finnhub API
- FRED API
- Yahoo / Stooq fallback
- CBOE / options feeds when available
- Cloudflare Pages / GitHub Actions
- mature chart libraries and frontend frameworks

Do not waste time self-building:

- generic data platforms
- charting systems
- login systems
- cloud platforms
- broker execution systems
- deployment architecture that sacrifices prediction quality

Data vendors are not the moat. Finnhub, FRED, CBOE, Yahoo, Stooq, and similar providers exist to improve `data_completeness`, `model_confidence`, `signal_agreement`, `macro_event_risk`, and `simulated_path_weighting`. If a feed is missing, stale, fallback, or rate-limited, say so explicitly. Never pretend unavailable data is available.

Privacy and protection rules:

- Keep core code, Alpha logic, Market Intelligence Engine, Historical Analog Engine, Signal Agreement, and simulated path weighting in the private repo.
- Publish only sanitized dashboard outputs.
- Keep API keys in GitHub Secrets or local environment variables only.
- Never expose keys in code, README, logs, `.env`, `frontend/public`, or `NEXT_PUBLIC_*` provider variables.

If a requested feature is a right-side commodity module, prefer an existing service or library. If it is a left-side judgment module that improves predictive quality, validation quality, or explanation quality, it is worth deeper research.

## 22. Maintain An Immutable Forecast Accuracy Ledger

Every daily production forecast must append or preserve a record in the Forecast Accuracy Ledger. This is prediction accuracy tracking, not paper trading, PnL, or execution simulation.

Hard rules:

- Store `forecast_id`, `forecast_date`, `model_version`, `data_version`, symbol, current price, primary/secondary/risk scenarios, probabilities, edge status, signal confirmation, model confidence, data completeness, strongest predictor, supporting/conflicting evidence, missing data, invalidation conditions, horizon expectations, realized returns, best-matching scenarios, primary-hit flags, path-error fields, and status.
- After a forecast exists, do not rewrite forecast fields because a newer model or cleaner data arrived.
- Model upgrades must create a new `model_version`; they must not mutate historical forecast rows.
- Outcome backfills may update only realized-return fields, best-matching-scenario fields, primary-hit fields, path-error fields, and completion status.
- Score accuracy separately by `3d`, `5d`, `10d`, `20d`, and `60d`. Do not mix horizons.
- If completed samples are below 20, output `insufficient_samples` and keep confidence capped.

## 23. Treat Flow / Positioning As Proxy Until Proven

Flow / positioning improves scenario confirmation only when it is explicitly sourced and labeled.

Hard rules:

- Use real fund-flow, CFTC, dealer-positioning, prime-brokerage, or option-flow feeds only when available and point-in-time safe.
- If using ETF volume, relative volume, factor rotation, sector rotation, HYG/LQD, TLT/UUP, high-beta/low-vol, or equal-weight/cap-weight, label it `proxy`.
- Proxy flow may affect `signal_confirmation_score`, failed-bounce risk, scenario weights, and model confidence only modestly.
- Missing true flow must remain visible in `data_quality_report`.
- Track `flow_confirmed` and `flow_conflicted` forecast buckets in forward validation.
- Do not treat proxy flow as a standalone alpha or execution signal.

## 24. Use Baseline / Challenger Model Governance

The active frozen production model is `baseline_v1`. This name refers to the current combination of scenario ranking, signal confirmation, historical analogs, FRED rates/credit, breadth/internal resonance, VIX term / VVIX / SKEW, flow proxy, Forecast Accuracy Ledger, and Historical Replay Benchmark.

Hard rules:

- Do not rewrite pre-freeze forecast rows to rename them. Historical rows must keep their original `model_version`.
- New production forecasts must use `model_version = baseline_v1` until a challenger is promoted.
- Any new data source, predictor, scenario weighting rule, or confidence rule must first run as a challenger / shadow model.
- A challenger can be registered as blocked if required point-in-time data is unavailable. Do not generate fake challenger forecasts from missing put/call, gamma, true flow, or macro-event data.
- Historical replay can produce research priority, but it cannot promote a model to active.
- Promotion requires forward validation gates by horizon: 3d >= 20, 5d >= 20, 10d >= 30, 20d >= 50, and 60d >= 50 completed samples, preferably 100+ for 60d.
- A challenger must beat `baseline_v1` on a majority of relevant metrics: primary hit rate, primary-vs-secondary spread, mean/median path error, high-confidence accuracy, signal-confirmation top bucket, edge-status performance, calibration quality, and adverse-path control.
- If a challenger improves one horizon but degrades others, keep it as a shadow model.
- Valid promotion statuses are `blocked_missing_required_data`, `insufficient_forward_evidence`, `historical_only_not_validated`, `promotion_candidate`, and `active_model`.

## 25. Define High Precision And Stable Alpha Conservatively

Read `docs/forecast_accuracy_definition.md` and `docs/stable_alpha_definition.md` before claiming precision or alpha quality.

Hard rules:

- High precision does not mean every daily forecast is right. It means the system can identify `NO_EDGE`, and high-evidence buckets beat low-evidence buckets in forward validation.
- Stable alpha does not mean one historical replay or one backtest worked. It requires enough forward-only samples, multiple-symbol checks, horizon checks, regime checks, confidence validation, and overfit controls.
- The dashboard and reports must output `not_yet_validated` until the evidence gates are met.
- `Alpha v1` remains `RESEARCH ALPHA CANDIDATE` until forward-only evidence satisfies the stable alpha definition.
- Do not use historical replay, historical analogs, or data-source additions as a shortcut to high precision or stable alpha.

## 26. Require Multi-Source Confluence

Multi-source confluence is mandatory for any strong market forecast. A single indicator is never enough.

The core confluence stack is:

- price structure
- volume structure
- breadth / internal resonance
- credit conditions
- volatility and options structure
- flow / positioning
- news and event intelligence
- historical analogs

Hard rules:

- Treat every individual indicator as evidence, not as a conclusion.
- Do not call a forecast `STRONG_EDGE`, `HIGH_CONVICTION`, `Trend Repair`, `Bounce Setup`, or `Risk Expansion` unless multiple independent evidence groups point in the same direction.
- Always show supporting evidence and conflicting evidence side by side.
- If price, volume, breadth, credit, volatility, flow, news, and historical analogs disagree, reduce confidence, mark `mixed` / `NO_EDGE`, or keep the module as shadow evidence.
- If data is missing, stale, proxy-only, or unvalidated, cap confidence and display the limitation.
- Multi-source confluence must feed forecast confirmation, scenario ranking, failed-bounce risk, risk-expansion risk, trend-repair probability, forecast price levels, and the Daily Market Brief.
- Confluence itself must be forward validated. A better-looking explanation is not proof of alpha.

## Non-Negotiable Summary

Always enforce: label-first design, walk-forward validation, regime-aware modeling, multi-source confluence, credit + liquidity + options + breadth inputs, no future leakage, no random train-test split, probability output with calibration, feature ablation, horizon-specific models, persistent prediction logs for backtesting, and Wardley Mapping build-vs-buy discipline.
