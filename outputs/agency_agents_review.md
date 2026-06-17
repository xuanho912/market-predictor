# Agency Agents Review

Generated at: `2026-06-17T09:53:42+00:00`
Source repository: https://github.com/msitarzewski/agency-agents
Source path: `external/agency-agents`
Source commit: `3f78a30`

## Purpose

Use upstream agency-agents role definitions as a specialist review layer for the Market Prediction Dashboard.

## Guardrails

- Agency roles may review and guide project work, but they must not override AGENTS.md, the market-prediction-research skill, baseline_v1, Alpha v1, or forecast ledger immutability.
- Agency roles must remain forecast-only. They must not introduce trading, order, entry, exit, PnL, broker, or paper-trading language.
- Agency roles must not expose API keys, provider credentials, private algorithm internals, or frontend/public secrets.

## Selected Roles

Available roles: 8 / 8

### Investment Researcher / Stock Thesis Analyst

- Role id: `investment_researcher`
- Upstream file: `finance/finance-investment-researcher.md`
- Status: `available`
- Upstream heading: `Investment Researcher Agent`

Use for:
- individual stock forecast quality
- bull case / bear case
- catalyst analysis
- downside path
- thesis breakers
- stock radar candidate review

Required outputs:
- `thesis_vs_narrative`
- `bull_case`
- `bear_case`
- `downside_risk`
- `catalysts`
- `horizon`
- `confidence`
- `thesis_breakers`

### Data Reliability Engineer

- Role id: `data_engineer`
- Upstream file: `engineering/engineering-data-engineer.md`
- Status: `available`
- Upstream heading: `Data Engineer Agent`

Use for:
- provider quality
- data freshness
- cache and stale behavior
- missing/proxy/fallback labeling
- blank chart diagnostics

Required outputs:
- `provider_status`
- `latest_date`
- `expected_latest_trading_date`
- `stale_warning`
- `fallback_used`
- `missing_or_proxy_fields`

### Model Validation Scientist

- Role id: `ai_engineer`
- Upstream file: `engineering/engineering-ai-engineer.md`
- Status: `available`
- Upstream heading: `AI Engineer Agent`

Use for:
- model lifecycle
- baseline vs challenger governance
- calibration
- drift detection
- forecast validation

Required outputs:
- `model_version_impact`
- `challenger_status`
- `validation_gate`
- `calibration_risk`
- `forward_sample_status`

### Market Prediction Product Lead

- Role id: `product_manager`
- Upstream file: `product/product-manager.md`
- Status: `available`
- Upstream heading: `Product Manager Agent`

Use for:
- user-value prioritization
- first-screen decision hierarchy
- feature scope control
- forecast terminal product shape

Required outputs:
- `user_need`
- `decision_priority`
- `first_screen_impact`
- `scope_risk`
- `defer_or_build`

### Product Terminal Designer

- Role id: `ux_architect`
- Upstream file: `design/design-ux-architect.md`
- Status: `available`
- Upstream heading: `ArchitectUX Agent Personality`

Use for:
- dashboard information architecture
- mobile hierarchy
- folding technical details
- terminal-style interaction

Required outputs:
- `above_fold_content`
- `folded_content`
- `mobile_order`
- `clarity_risks`

### Reality Checker / Evidence Gate

- Role id: `reality_checker`
- Upstream file: `testing/testing-reality-checker.md`
- Status: `available`
- Upstream heading: `Integration Agent Personality`

Use for:
- claims validation
- not_yet_validated enforcement
- sample-size warnings
- no-overclaim checks

Required outputs:
- `claim_checked`
- `evidence_level`
- `sample_size_status`
- `overclaim_warning`

### Security / Secrets Reviewer

- Role id: `security_architect`
- Upstream file: `security/security-architect.md`
- Status: `available`
- Upstream heading: `Security Architect Agent`

Use for:
- API key safety
- private core protection
- public dashboard sanitization
- GitHub Actions secret hygiene

Required outputs:
- `secret_exposure_check`
- `public_json_check`
- `frontend_key_check`
- `private_core_check`

### Minimal Code Reviewer

- Role id: `code_reviewer`
- Upstream file: `engineering/engineering-code-reviewer.md`
- Status: `available`
- Upstream heading: `Code Reviewer Agent`

Use for:
- scope control
- regression risk
- minimal diffs
- maintainability

Required outputs:
- `changed_surface`
- `regression_risk`
- `tests_or_checks`
- `unrelated_change_warning`

## Project Review Gates

- `forecast_impact`
- `data_freshness_and_source_status`
- `validation_and_ledger_impact`
- `user_facing_decision_impact`
- `security_and_secret_exposure_check`
