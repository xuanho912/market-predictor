# Research Framework

This project predicts probabilities, not certainties. Every forecast must answer:

- What is the target label?
- What is the horizon?
- What data was known at the forecast timestamp?
- What regime is being modeled?
- What probability was emitted?
- Why did the model produce that probability?
- How will the prediction be audited after realization?

## Core Prediction Families

- trend: up, down, sideways
- pullback: short and medium horizon drawdowns after an advance
- downside continuation: additional losses after an existing decline
- bounce: reflexive recovery after oversold or stressed conditions
- trend reversal: durable change in trend direction
- crash risk: high-magnitude drawdown probability
- systemic crisis: broad stress across equity, credit, funding, and macro channels

## Market Regimes

Identify market regime before interpreting indicators:

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

The same indicator can mean different things by regime. For example, RSI near 30 in a bull-market pullback can support a bounce probability, while RSI near 30 in crisis selling can be downside continuation.

## Four-Layer Risk Decomposition

Analyze every major decline, crisis warning, or bounce setup through four layers.

### 1. Vulnerability

Structural conditions that make the market fragile:

- valuation
- leverage
- credit expansion
- debt burden
- crowded positioning
- earnings quality
- bank and non-bank financial risk

### 2. Trigger

Events that can turn fragility into realized market stress:

- CPI and inflation surprises
- nonfarm payrolls and labor shocks
- central bank decisions
- interest-rate jumps
- dollar liquidity tightening
- geopolitical shocks
- bank failures
- forced fund liquidation
- mega-cap earnings breaks
- policy and regulatory changes
- FX and commodity shocks

### 3. Amplifier

Mechanisms that turn a selloff into a cascade:

- margin calls
- option gamma
- CTA, risk parity, and volatility-control deleveraging
- ETF redemptions
- credit-spread widening
- collateral price declines
- thin liquidity

### 4. Confirmation Signal

Observable evidence that risk is being priced:

- index breaks below moving averages
- market breadth deterioration
- widening credit spreads
- VIX and volatility term-structure stress
- high-yield bonds, banks, and small caps underperforming
- stronger dollar
- defensive or safe-haven asset strength
- heavy volume on declines and weak volume on rebounds

## Forecast Record

Every production forecast should store:

- forecast timestamp
- market universe
- label and horizon
- regime
- model version
- feature snapshot version
- raw probability
- calibrated probability
- risk score
- top positive and negative drivers
- explanation text
- realized label, once known
- scoring metrics, once known

The stored record is the source of truth for future model accountability.

## Pullback Versus Crisis

Normal pullbacks usually involve equity weakness, VIX rising, and breadth deterioration while credit spreads, banks, funding markets, liquidity, and macro data remain functional.

Crisis warnings require synchronized deterioration across equities, credit, funding, banks, dollar liquidity, market depth, and policy stress. Rule: equities alone falling may be a pullback; equities, credit, funding, banks, and dollar liquidity worsening together is crisis risk.

## Bounce Versus Durable Bottom

Bounce models should estimate selling-pressure exhaustion rather than the exact low.

Dead-cat bounces tend to be short-covering driven, weak in volume and breadth, unconfirmed by credit and banks, fragile near moving-average resistance, and unsupported by liquidity or earnings revisions.

More reliable bottoms tend to show credit stabilization, VIX spike-and-reversal, breadth repair, equal-weight and small-cap participation, bank stabilization, bad-news resilience, policy or liquidity improvement, sustained absorption after high volume, slower earnings downgrades, and rotation from safe havens back to risk assets.
