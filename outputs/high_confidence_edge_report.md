# High Confidence Edge Report

Generated at: `2026-10-02T01:52:54.966590+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `68`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `68`, gate `moderate_evidence`
- 5d: completed `68`, gate `moderate_evidence`
- 10d: completed `68`, gate `moderate_evidence`
- 20d: completed `68`, gate `moderate_evidence`
- 60d: completed `68`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.001575`, median `0.001405`, mae `0.015593`
- 5d: sample `60`, hit `0.4833`, avg `-0.00683`, median `-0.001562`, mae `0.018735`
- 10d: sample `60`, hit `0.5167`, avg `-0.006713`, median `0.001607`, mae `0.022297`
- 20d: sample `60`, hit `0.6167`, avg `0.005032`, median `0.015416`, mae `0.036314`
- 60d: sample `60`, hit `0.8167`, avg `0.041368`, median `0.05019`, mae `0.071549`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.014621`, median `-0.01091`, mae `0.021041`
- 5d: sample `20`, hit `0.3`, avg `-0.012087`, median `-0.011925`, mae `0.024016`
- 10d: sample `20`, hit `0.5`, avg `-0.000732`, median `0.004306`, mae `0.042644`
- 20d: sample `20`, hit `0.5`, avg `0.008981`, median `0.034151`, mae `0.060048`
- 60d: sample `20`, hit `0.85`, avg `0.086922`, median `0.114377`, mae `0.100133`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001851`, median `0.003898`, mae `0.010758`
- 5d: sample `8`, hit `0.625`, avg `-0.000166`, median `0.009651`, mae `0.011554`
- 10d: sample `8`, hit `0.625`, avg `0.011474`, median `0.014793`, mae `0.017948`
- 20d: sample `8`, hit `1.0`, avg `0.036437`, median `0.034024`, mae `0.036437`
- 60d: sample `8`, hit `1.0`, avg `0.04395`, median `0.05019`, mae `0.04395`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001851`, median `0.003898`, mae `0.010758`
- 5d: sample `8`, hit `0.625`, avg `-0.000166`, median `0.009651`, mae `0.011554`
- 10d: sample `8`, hit `0.625`, avg `0.011474`, median `0.014793`, mae `0.017948`
- 20d: sample `8`, hit `1.0`, avg `0.036437`, median `0.034024`, mae `0.036437`
- 60d: sample `8`, hit `1.0`, avg `0.04395`, median `0.05019`, mae `0.04395`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001851, 'median_return': 0.003898, 'mean_absolute_return': 0.010758, 'max_adverse_excursion': -0.031857, 'max_favorable_excursion': 0.016338}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000166, 'median_return': 0.009651, 'mean_absolute_return': 0.011554, 'max_adverse_excursion': -0.026896, 'max_favorable_excursion': 0.013193}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011474, 'median_return': 0.014793, 'mean_absolute_return': 0.017948, 'max_adverse_excursion': -0.01411, 'max_favorable_excursion': 0.036168}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.036437, 'median_return': 0.034024, 'mean_absolute_return': 0.036437, 'max_adverse_excursion': 0.013156, 'max_favorable_excursion': 0.059335}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.04395, 'median_return': 0.05019, 'mean_absolute_return': 0.04395, 'max_adverse_excursion': 0.005833, 'max_favorable_excursion': 0.075909}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.005168, 'median_return': -0.003676, 'mean_absolute_return': 0.017644, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.009031, 'median_return': -0.009444, 'mean_absolute_return': 0.021, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.007072, 'median_return': 0.000397, 'mean_absolute_return': 0.028432, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.002639, 'median_return': 0.010829, 'mean_absolute_return': 0.042893, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.053735, 'median_return': 0.065995, 'mean_absolute_return': 0.082555, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.167846}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.175}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_minus_secondary': -0.65, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.004837, 'median_return': -0.003649, 'mean_absolute_return': 0.016955, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.008144, 'median_return': -0.00693, 'mean_absolute_return': 0.020055, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.005218, 'median_return': 0.001607, 'mean_absolute_return': 0.027384, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.006019, 'median_return': 0.015416, 'mean_absolute_return': 0.042248, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.825, 'avg_return': 0.052756, 'median_return': 0.059131, 'mean_absolute_return': 0.078695, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.167846}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.004837`, median `-0.003649`, mae `0.016955`
- 5d: sample `80`, hit `0.4375`, avg `-0.008144`, median `-0.00693`, mae `0.020055`
- 10d: sample `80`, hit `0.5125`, avg `-0.005218`, median `0.001607`, mae `0.027384`
- 20d: sample `80`, hit `0.5875`, avg `0.006019`, median `0.015416`, mae `0.042248`
- 60d: sample `80`, hit `0.825`, avg `0.052756`, median `0.059131`, mae `0.078695`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.004837`, median `-0.003649`, mae `0.016955`
- 5d: sample `80`, hit `0.4375`, avg `-0.008144`, median `-0.00693`, mae `0.020055`
- 10d: sample `80`, hit `0.5125`, avg `-0.005218`, median `0.001607`, mae `0.027384`
- 20d: sample `80`, hit `0.5875`, avg `0.006019`, median `0.015416`, mae `0.042248`
- 60d: sample `80`, hit `0.825`, avg `0.052756`, median `0.059131`, mae `0.078695`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.004837`, median `-0.003649`, mae `0.016955`
- 5d: sample `80`, hit `0.4375`, avg `-0.008144`, median `-0.00693`, mae `0.020055`
- 10d: sample `80`, hit `0.5125`, avg `-0.005218`, median `0.001607`, mae `0.027384`
- 20d: sample `80`, hit `0.5875`, avg `0.006019`, median `0.015416`, mae `0.042248`
- 60d: sample `80`, hit `0.825`, avg `0.052756`, median `0.059131`, mae `0.078695`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.004837`, median `-0.003649`, mae `0.016955`
- 5d: sample `80`, hit `0.4375`, avg `-0.008144`, median `-0.00693`, mae `0.020055`
- 10d: sample `80`, hit `0.5125`, avg `-0.005218`, median `0.001607`, mae `0.027384`
- 20d: sample `80`, hit `0.5875`, avg `0.006019`, median `0.015416`, mae `0.042248`
- 60d: sample `80`, hit `0.825`, avg `0.052756`, median `0.059131`, mae `0.078695`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### risk_path_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
