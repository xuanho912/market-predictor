# High Confidence Edge Report

Generated at: `2026-09-16T06:07:15.629152+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `20`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `20`, gate `early_evidence`
- 5d: completed `20`, gate `early_evidence`
- 10d: completed `20`, gate `early_evidence`
- 20d: completed `20`, gate `early_evidence`
- 60d: completed `20`, gate `early_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.000308`, median `0.000766`, mae `0.014502`
- 5d: sample `80`, hit `0.5`, avg `-0.003976`, median `0.000208`, mae `0.016849`
- 10d: sample `80`, hit `0.4125`, avg `-0.005586`, median `-0.007491`, mae `0.026844`
- 20d: sample `80`, hit `0.575`, avg `0.009014`, median `0.009364`, mae `0.034493`
- 60d: sample `80`, hit `0.7375`, avg `0.041106`, median `0.061042`, mae `0.08094`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.000507`, median `0.00234`, mae `0.015536`
- 5d: sample `8`, hit `0.625`, avg `-0.00539`, median `0.003829`, mae `0.018227`
- 10d: sample `8`, hit `0.25`, avg `0.002087`, median `-0.001222`, mae `0.01503`
- 20d: sample `8`, hit `0.875`, avg `0.03836`, median `0.055822`, mae `0.043732`
- 60d: sample `8`, hit `0.875`, avg `0.083903`, median `0.120808`, mae `0.091676`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.000507`, median `0.00234`, mae `0.015536`
- 5d: sample `8`, hit `0.625`, avg `-0.00539`, median `0.003829`, mae `0.018227`
- 10d: sample `8`, hit `0.25`, avg `0.002087`, median `-0.001222`, mae `0.01503`
- 20d: sample `8`, hit `0.875`, avg `0.03836`, median `0.055822`, mae `0.043732`
- 60d: sample `8`, hit `0.875`, avg `0.083903`, median `0.120808`, mae `0.091676`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000507, 'median_return': 0.00234, 'mean_absolute_return': 0.015536, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00539, 'median_return': 0.003829, 'mean_absolute_return': 0.018227, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': 0.002087, 'median_return': -0.001222, 'mean_absolute_return': 0.01503, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.03836, 'median_return': 0.055822, 'mean_absolute_return': 0.043732, 'max_adverse_excursion': -0.02149, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.083903, 'median_return': 0.120808, 'mean_absolute_return': 0.091676, 'max_adverse_excursion': -0.03109, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.000286, 'median_return': 0.000766, 'mean_absolute_return': 0.014388, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.003819, 'median_return': -0.000123, 'mean_absolute_return': 0.016696, 'max_adverse_excursion': -0.052787, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.006438, 'median_return': -0.010456, 'mean_absolute_return': 0.028156, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.005754, 'median_return': 0.00745, 'mean_absolute_return': 0.033467, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.03635, 'median_return': 0.059948, 'mean_absolute_return': 0.079747, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.2625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.475, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.000308, 'median_return': 0.000766, 'mean_absolute_return': 0.014502, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.003976, 'median_return': 0.000208, 'mean_absolute_return': 0.016849, 'max_adverse_excursion': -0.052787, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': -0.005586, 'median_return': -0.007491, 'mean_absolute_return': 0.026844, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.009014, 'median_return': 0.009364, 'mean_absolute_return': 0.034493, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 80, 'hit_rate': 0.7375, 'avg_return': 0.041106, 'median_return': 0.061042, 'mean_absolute_return': 0.08094, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.19145}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.525`, avg `0.000308`, median `0.000766`, mae `0.014502`
- 5d: sample `80`, hit `0.5`, avg `-0.003976`, median `0.000208`, mae `0.016849`
- 10d: sample `80`, hit `0.4125`, avg `-0.005586`, median `-0.007491`, mae `0.026844`
- 20d: sample `80`, hit `0.575`, avg `0.009014`, median `0.009364`, mae `0.034493`
- 60d: sample `80`, hit `0.7375`, avg `0.041106`, median `0.061042`, mae `0.08094`

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
- 3d: sample `80`, hit `0.525`, avg `0.000308`, median `0.000766`, mae `0.014502`
- 5d: sample `80`, hit `0.5`, avg `-0.003976`, median `0.000208`, mae `0.016849`
- 10d: sample `80`, hit `0.4125`, avg `-0.005586`, median `-0.007491`, mae `0.026844`
- 20d: sample `80`, hit `0.575`, avg `0.009014`, median `0.009364`, mae `0.034493`
- 60d: sample `80`, hit `0.7375`, avg `0.041106`, median `0.061042`, mae `0.08094`

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
- 3d: sample `80`, hit `0.525`, avg `0.000308`, median `0.000766`, mae `0.014502`
- 5d: sample `80`, hit `0.5`, avg `-0.003976`, median `0.000208`, mae `0.016849`
- 10d: sample `80`, hit `0.4125`, avg `-0.005586`, median `-0.007491`, mae `0.026844`
- 20d: sample `80`, hit `0.575`, avg `0.009014`, median `0.009364`, mae `0.034493`
- 60d: sample `80`, hit `0.7375`, avg `0.041106`, median `0.061042`, mae `0.08094`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
