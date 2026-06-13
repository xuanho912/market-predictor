# Model Layers And Scores

Use this reference before adding model code, API outputs, or scoring logic.

## Four Model Layers

### A. Long-Term Vulnerability Model

Forecast horizon: 6-24 months.

Inputs:

- credit/GDP
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

- financial system vulnerability score
- future 12-month crisis probability
- currently most vulnerable sectors

### B. Medium-Term Pullback Risk Model

Forecast horizon: 2-12 weeks.

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

- future 20-day max drawdown probability
- future 60-day max drawdown probability
- expected drawdown
- risk source decomposition

### C. Short-Term Trigger Model

Forecast horizon: 1-5 days.

Inputs:

- option gamma
- 0DTE
- volume
- order book depth
- news shock
- key data calendar
- premarket futures
- volatility term structure
- ETF creations/redemptions
- sector rotation
- flows

Outputs:

- sharp drop probability
- sharp rebound probability
- intraday volatility range
- key trigger levels

### D. Bottom Bounce Model

Forecast horizon: 10/20 days.

Inputs:

- drawdown depth
- panic intensity
- VIX percentile
- Put/Call percentile
- credit spread changes
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
- whether it is only a dead-cat bounce
- whether it may form a medium-term bottom

## Core Score Weights

`pullback_risk_score`:

- valuation overheat: 15%
- momentum extension: 15%
- breadth deterioration: 15%
- VIX/options risk: 10%
- positioning crowding: 15%
- rates up: 10%
- dollar strength: 5%
- earnings downgrades: 10%
- news/event risk: 5%

`crisis_risk_score`:

- credit/GDP gap: 15%
- credit spreads: 20%
- bank stress: 15%
- funding market stress: 15%
- non-bank leverage: 10%
- dollar liquidity: 10%
- macro recession risk: 10%
- policy response lag: 5%

`bounce_quality_score`:

- drawdown depth: 10%
- panic extreme: 15%
- volume expansion: 10%
- breadth repair: 15%
- credit spread stabilization: 20%
- VIX reversal: 10%
- policy/liquidity improvement: 10%
- bad-news resilience: 10%
