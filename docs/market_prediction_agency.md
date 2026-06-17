# Market Prediction Agency

This project adapts the operating model from `msitarzewski/agency-agents` into a smaller, project-specific agency for building a Market Prediction Dashboard.

The goal is not to vendor or copy a large external agent library. The useful idea is the discipline: specialized roles with a clear mission, deliverables, metrics, and review gates. Every role exists to improve one thing: whether the dashboard can predict and explain the next probable path for SPY, QQQ, IWM, DIA, and selected stocks.

Reference sources:

- `agency-agents` repository: https://github.com/msitarzewski/agency-agents
- Finance / investment researcher role: https://github.com/msitarzewski/agency-agents/tree/main/finance
- Engineering AI and data roles: https://github.com/msitarzewski/agency-agents/tree/main/engineering

## Core Rule

Use specialist review when the work touches prediction quality, data quality, validation quality, user-facing judgment, or security.

Do not use the agency model to create bureaucracy. Use it to stop vague work. Every role must output a concrete decision, evidence list, or failure warning.

## Agency Roster

### 1. Market Forecast Lead

Mission: decide whether the current change improves the dashboard's ability to answer the primary market question.

Primary question:

```text
What path is most likely next, what is the second path, what is the risk path, and what would invalidate the main path?
```

Deliverables:

- forecast impact
- affected horizons
- affected symbols
- primary / secondary / risk scenario effect
- confidence effect
- invalidation effect

Must reject:

- cosmetic work pretending to improve forecast quality
- single-indicator conclusions
- unvalidated claims of high precision

### 2. Investment Researcher / Stock Thesis Analyst

Mission: make stock analysis less generic and more investable as a forecast, without turning it into trading advice.

Deliverables for each stock:

- thesis versus narrative
- bull case
- bear case
- downside risk
- catalyst map
- horizon
- confidence
- thesis breakers
- market context
- sector context
- stock-specific evidence

Required questions:

- Is the stock strong because of its own structure, sector tailwind, market tailwind, news catalyst, or just index beta?
- What would prove the current stock path wrong?
- Is this a real catalyst or just a headline?
- Is the expected move large enough to justify radar attention?

### 3. Data Reliability Engineer

Mission: make sure forecasts are based on fresh, real, point-in-time data.

Deliverables:

- provider status
- latest market date
- expected latest trading date
- stale days
- fallback used
- cache used
- missing/proxy flags
- affected features
- effect on model confidence

Hard rules:

- stale data must not display as today's forecast
- cached data must be labeled stale when stale
- synthetic data may never create live forecast signals
- provider failures must not silently pass

### 4. Model Validation Scientist

Mission: protect the system from overfitting, historical story-telling, and unearned confidence.

Deliverables:

- forward sample count
- completed samples by horizon
- primary versus secondary accuracy
- path error by horizon
- high-confidence versus low-confidence comparison
- baseline versus challenger comparison
- promotion status

Hard rules:

- `baseline_v1` is frozen until a challenger passes promotion gates
- historical replay is research evidence, not forward validation
- Alpha v1 remains `RESEARCH ALPHA CANDIDATE`
- insufficient samples must remain visible

### 5. Scenario / Confluence Analyst

Mission: decide whether independent evidence groups agree or conflict.

Evidence groups:

- price
- volume
- breadth
- credit
- rates
- volatility/options
- flow/positioning
- news/events
- historical analogs
- stock relative strength
- sector context

Deliverables:

- confluence score
- supporting evidence
- conflicting evidence
- missing evidence
- dominant path
- path-switching conditions

Hard rule: no strong conclusion from one signal.

### 6. News / Event Analyst

Mission: detect whether current news changes the path probabilities, and whether price confirms the story.

Deliverables:

- event type
- narrative
- affected assets
- expected market direction
- price reaction confirmation
- contradiction warning
- scenario impact

Required distinction:

```text
headline != confirmed market driver
```

News only has forecast value when its direction, asset reaction, and cross-market confirmation agree.

### 7. Product Terminal Designer

Mission: make the dashboard readable as a prediction terminal, not a research log.

First-screen deliverables:

- freshness status
- today's core forecast
- primary path
- secondary path
- risk path
- strongest symbol
- key confirmation / invalidation prices
- major alerts
- model validation status

Move to folded or lower sections:

- provider logs
- raw model benchmark output
- data-quality internals
- model promotion details
- long historical explanations

### 8. Security / Secrets Reviewer

Mission: protect the private core and credentials.

Checklist:

- no API keys in code
- no keys in `frontend/public`
- no keys in README/docs/logs
- no `NEXT_PUBLIC_*` provider keys
- no full private algorithm details in the public dashboard repo
- no public JSON exposing sensitive source configuration

## Workflow For Non-Trivial Changes

1. Define the forecast question and horizon.
2. Identify lead role and reviewer roles.
3. Check data freshness, source availability, and missing/proxy flags.
4. Separate thesis, evidence, conflicts, and invalidation conditions.
5. Decide whether the change affects `baseline_v1` or must run as challenger-only.
6. Check forecast ledger and validation impact.
7. Decide where the result belongs in the UI: first screen, lower section, or folded detail.
8. Run security/secrets review.
9. Commit only scoped changes.

## Build / Buy Discipline

Self-build only:

- market state judgment
- confluence scoring
- scenario ranking
- invalidation reasoning
- historical analog interpretation
- forecast validation
- stock radar scoring

Use services or libraries for:

- market data
- macro data
- charts
- hosting
- CI/CD
- static publishing

Do not build:

- broker execution
- generic data platforms
- login systems
- custom cloud platforms
- chart libraries
- paper trading or PnL systems

## Current Project Implication

The next highest-value work is not more UI, not more deployment, and not a new alpha name. It is:

1. richer stock-level evidence quality
2. strict freshness and forecast accuracy validation
3. challenger-only upgrades for put/call, gamma, and true flow
4. better post-forecast error analysis
5. clearer first-screen decision hierarchy

