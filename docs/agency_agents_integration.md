# Agency Agents Integration

This project directly uses `msitarzewski/agency-agents` as a Git submodule at:

```text
external/agency-agents
```

The integration is intentionally narrow. The upstream repository provides role definitions and review practices. It does not replace this project's market-prediction rules, `baseline_v1`, Alpha v1, forecast ledger, data freshness gates, or validation standards.

## Why Use It

The upstream repository describes agents as specialized, deliverable-focused roles with concrete workflows and success metrics. That is useful for this project because the dashboard now has multiple hard domains:

- market forecasting
- stock research
- data reliability
- model validation
- confluence analysis
- news/event interpretation
- terminal UI hierarchy
- secrets protection

## How It Is Wired

The selected upstream roles are listed in:

```text
config/agency_agents_manifest.json
```

The adapter script reads that manifest and the upstream submodule:

```bash
python scripts/agency_agents_adapter.py
```

It writes:

```text
outputs/agency_agents_review.md
frontend/public/agency-agents-review.json
```

These outputs are review artifacts only. They do not change forecasts.

## Selected Upstream Roles

The adapter currently maps these upstream roles into project-specific review roles:

- `finance/finance-investment-researcher.md` -> Investment Researcher / Stock Thesis Analyst
- `engineering/engineering-data-engineer.md` -> Data Reliability Engineer
- `engineering/engineering-ai-engineer.md` -> Model Validation Scientist
- `product/product-manager.md` -> Market Prediction Product Lead
- `design/design-ux-architect.md` -> Product Terminal Designer
- `testing/testing-reality-checker.md` -> Reality Checker / Evidence Gate
- `security/security-architect.md` -> Security / Secrets Reviewer
- `engineering/engineering-code-reviewer.md` -> Minimal Code Reviewer

## Guardrails

Agency roles can review and sharpen work, but they must not:

- change `Alpha v1 threshold = 0.32534311`
- overwrite or mutate old forecast records
- replace `baseline_v1`
- promote a challenger without forward validation gates
- introduce trading, order, entry, exit, PnL, broker, or paper-trading language
- expose API keys or provider secrets
- put prediction logic in the frontend

## How To Use It In Practice

Before a non-trivial change, pick a lead role and reviewers:

```text
Lead: Investment Researcher
Reviewers: Data Reliability Engineer, Model Validation Scientist, Security Reviewer
```

Then produce role-specific outputs before coding:

- forecast impact
- data impact
- validation impact
- user-facing decision impact
- security / secrets impact

For example, a stock analysis improvement must answer:

- What is the stock thesis?
- What is the bear case?
- What is the downside path?
- What catalyst could move it tomorrow?
- What breaks the thesis?
- Is market context supportive or hostile?
- Is sector context supportive or hostile?
- Are data sources fresh, stale, missing, or proxy-only?

## Updating The Submodule

Use:

```bash
git submodule update --init --recursive
git -C external/agency-agents pull --ff-only
python scripts/agency_agents_adapter.py
```

Then review the generated files before committing.

