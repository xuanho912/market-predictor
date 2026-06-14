# High Confidence Edge Report

Generated at: `2026-06-14T07:14:05.880654+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Conclusion: `not_enough_strong_edge_samples`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001175`, median `0.001558`
- 5d: sample `80`, hit `0.5875`, avg `0.000734`, median `0.003005`
- 10d: sample `80`, hit `0.4875`, avg `0.001104`, median `-0.0004`
- 20d: sample `80`, hit `0.5875`, avg `0.002376`, median `0.009112`
- 60d: sample `80`, hit `0.475`, avg `0.00681`, median `-0.003049`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`

### RISK_WARNING
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.002698`, median `0.003538`
- 5d: sample `8`, hit `0.5`, avg `0.003863`, median `0.006133`
- 10d: sample `8`, hit `0.625`, avg `0.004889`, median `0.00903`
- 20d: sample `8`, hit `0.375`, avg `-0.021094`, median `-0.014517`
- 60d: sample `8`, hit `0.75`, avg `0.035988`, median `0.069306`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.008716`, median `-0.009383`
- 5d: sample `8`, hit `0.375`, avg `-0.00719`, median `-0.004438`
- 10d: sample `8`, hit `0.375`, avg `-0.001836`, median `-0.007011`
- 20d: sample `8`, hit `0.625`, avg `0.003391`, median `0.020068`
- 60d: sample `8`, hit `0.5`, avg `-0.006235`, median `0.012092`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.475}}`
- primary_vs_secondary: `{'status': 'proxy_only', 'note': 'Primary vs secondary path closeness needs forward realized paths; current report uses historical analog direction as a proxy.', 'primary_scenario_hit_rate': {'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.475}}}`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
