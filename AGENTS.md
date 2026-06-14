# AGENTS.md

This repository is a Market Prediction Dashboard and market trend prediction engine, not a normal indicator dashboard and not a Trading Bot. When working here, Codex must follow these rules first.

Strategic principle: build only what creates unique market-prediction judgment; buy, rent, or reuse commodity infrastructure. See `docs/wardley_strategy.md` before adding non-trivial features.

1. The core product is a market trend prediction engine for forward trend, pullback, crisis risk, downside continuation, bounce, and reversal probabilities.
2. Every prediction must be probabilistic. Do not write or hard-code claims such as "must rise", "must fall", or "certain crisis".
3. Every model, feature, label, backtest, and explanation must actively avoid future functions, data leakage, survivorship bias, and macro data revision leakage.
4. Every training and backtest workflow must use time-series walk-forward validation. Randomly shuffling time-series samples is prohibited.
5. Every prediction must be persisted as a historical record so future realized outcomes can audit forecast quality.
6. Every model must output explanations: why bullish, why bearish, why bounce, why crisis, and which evidence changed the probability.
7. Every new indicator must be assigned to exactly one of these groups: price, volatility, credit, rates, liquidity, macro, earnings, positioning, breadth, news_text, onchain_crypto, or alternative_data.
8. Do not build automated execution, broker connections, order placement, simulated order execution, position-management rules, portfolio-accounting reports, or execution recommendations.
9. The mobile frontend is only a presentation layer. Prediction logic must not be hard-coded in the frontend.
10. README.md must explain how to run locally, deploy, update data, train models, and validate models.
11. Every prediction and model must identify market regime first: bull_trend, bear_trend, sideways, panic, oversold_bounce, topping, bottoming, recovery, liquidity_crunch, credit_stress, or crisis_mode.
12. Every important indicator must generate level, change, acceleration, percentile, cross_signal, and divergence features when data allows.
13. Normal pullbacks, crisis warnings, dead-cat bounces, and durable bottoms must be modeled separately.
14. Data provider design must cover price, volatility, credit, rates, liquidity, macro, earnings, positioning, breadth, news_text, onchain_crypto, and alternative_data categories.
15. The model architecture must remain layered: long-term vulnerability, medium-term pullback risk, short-term trigger, and bottom bounce.
16. The API must output predictions with probabilities, confidence, risk scores, explanations, similar historical days, and risk source breakdowns.
17. First-stage MVP scope is SPY, QQQ, IWM, DIA with no broker integration, no order placement, no simulated execution workflow, and no automated execution.
18. The validation engine must replay historical predictions with walk-forward prior-window data and store horizon-level rows in `predictions_log`.
19. Feature importance must include permutation importance, feature group ablation, instability checks, regime-specific features, and correlation leakage checks.
20. Probability calibration must include Platt scaling, isotonic regression, Brier-score optimization, Brier score, log loss, and calibration curves.
21. Before adding a feature, classify it with the Wardley strategy filter: Genesis / Custom, Product / Rental, Commodity / Utility, or Do Not Build.
22. Self-build focus is limited to modules that directly improve prediction quality, explanation quality, or validation quality: Market State Engine, Signal Agreement, Historical Analog Engine, Edge / No Edge, predictor ensemble, simulated path weighting, confidence calibration, high-confidence signal validation, invalidation conditions, and Daily Market Brief judgment.
23. Product / Rental inputs such as Finnhub, FRED, Yahoo, Stooq, CBOE/options feeds, Cloudflare Pages, and GitHub Actions should be integrated through APIs or managed services. Do not treat data vendors or deployment platforms as the moat.
24. Commodity / Utility work such as hosting, deployment, chart libraries, CI/CD, frontend framework choice, generic caching infrastructure, and authentication must stay low priority unless it blocks the dashboard from being usable.
25. Do not self-build a generic data platform, charting system, login system, cloud platform, broker system, or any deployment architecture that sacrifices prediction quality.
26. Core code, Alpha logic, Market Intelligence Engine, Historical Analog Engine, Signal Agreement, and simulated path weighting must remain private. Public outputs may show results only, not keys or full algorithmic details.
27. API keys must remain in GitHub Secrets or local environment variables only. Never commit keys, `.env`, public JSON secrets, logs with keys, or `NEXT_PUBLIC_*` provider keys.
28. The final page must answer without user prompting: whether there is forecast edge today, current market state, strongest symbol, primary/secondary/risk probability paths, historical analog support or conflict, largest risk, invalidation conditions, model confidence, and which horizons need observation.
29. Alpha v1 must be described as a forecast signal / bounce scenario input, not an execution input. Use forecast start date, forecast horizon, scenario validation, forward return tracking, prediction accuracy, invalidation condition, and risk condition language.

Before adding a feature, define the label, horizon, regime interpretation, point-in-time data availability, validation window, probability calibration method, prediction logging path, and Wardley classification. If the feature is a right-side commodity module, prefer a managed service, API, or existing library over custom engineering.
