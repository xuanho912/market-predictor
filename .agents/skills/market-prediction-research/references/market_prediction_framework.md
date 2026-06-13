# Market Prediction Framework

Use this reference when designing research tasks, prediction workflows, or model explanations.

## Required Workflow

1. Define the label and horizon.
2. Define the forecast timestamp and data availability rule.
3. Identify market regime before interpreting indicators.
4. Select features by allowed feature group and required transform.
5. Decide whether the task is normal pullback, crisis risk, bounce, bottoming, or reversal.
6. Split by walk-forward time windows.
7. Train only on past data.
8. Calibrate probabilities on a validation window.
9. Test on unseen future windows.
10. Save every prediction for later audit.
11. Explain probability changes using risk layers and regime context.

## Risk Layers

Vulnerability:

- valuation
- leverage
- credit expansion
- debt burden
- crowded positioning
- earnings quality
- bank and non-bank financial stress

Trigger:

- inflation surprise
- labor surprise
- central bank decision
- rate shock
- dollar liquidity tightening
- geopolitical shock
- bank failure
- forced liquidation
- mega-cap earnings shock
- policy or regulatory change
- FX or commodity shock

Amplifier:

- margin calls
- option gamma
- CTA, risk parity, volatility-control selling
- ETF redemptions
- credit spread widening
- collateral decline
- thin liquidity

Confirmation:

- moving-average breakdown
- breadth deterioration
- VIX rise
- credit stress
- high-yield, bank, or small-cap underperformance
- dollar strength
- safe-haven strength
- heavy downside volume and weak rebound volume

## Regime Context

Always attach a regime to a forecast:

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

Regime changes feature interpretation. RSI, volatility, breadth, credit, and rate signals should be interpreted conditional on regime, not as universal constants.

## Pullback Versus Crisis

Treat an equity-only decline as a possible pullback. Treat synchronized deterioration across equities, credit, funding, banks, and dollar liquidity as crisis risk.

## Bounce Versus Bottom

Treat short-covering rebounds with weak breadth, weak credit, and weak liquidity as bounce risk only. Treat breadth repair, credit stabilization, bank stabilization, policy/liquidity improvement, and bad-news resilience as bottoming evidence.

## Probability Language

Use language like:

- "The calibrated probability increased from 28% to 41%."
- "The model is assigning elevated pullback risk."
- "The main drivers are widening credit spreads and deteriorating breadth."

Do not use language like:

- "The market will crash."
- "This guarantees a reversal."
- "A rally is certain."
