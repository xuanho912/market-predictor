# High Confidence Edge Report

Generated at: `2026-11-20T20:25:23.519747+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `212`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `212`, gate `stronger_evidence`
- 5d: completed `212`, gate `stronger_evidence`
- 10d: completed `212`, gate `stronger_evidence`
- 20d: completed `212`, gate `stronger_evidence`
- 60d: completed `212`, gate `stronger_evidence`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `-0.001387`, median `0.011008`, mae `0.030368`
- 5d: sample `80`, hit `0.6875`, avg `-0.00066`, median `0.012713`, mae `0.03439`
- 10d: sample `80`, hit `0.5875`, avg `-0.001016`, median `0.016492`, mae `0.049236`
- 20d: sample `80`, hit `0.65`, avg `0.00017`, median `0.025905`, mae `0.073549`
- 60d: sample `80`, hit `0.6`, avg `0.026128`, median `0.049972`, mae `0.108556`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.004738`, median `-0.00201`, mae `0.016205`
- 5d: sample `8`, hit `0.5`, avg `-0.002973`, median `0.004366`, mae `0.015597`
- 10d: sample `8`, hit `0.375`, avg `-0.018604`, median `-0.007679`, mae `0.042621`
- 20d: sample `8`, hit `0.375`, avg `-0.046429`, median `-0.001131`, mae `0.077688`
- 60d: sample `8`, hit `0.5`, avg `0.017696`, median `0.052255`, mae `0.058448`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.004738`, median `-0.00201`, mae `0.016205`
- 5d: sample `8`, hit `0.5`, avg `-0.002973`, median `0.004366`, mae `0.015597`
- 10d: sample `8`, hit `0.375`, avg `-0.018604`, median `-0.007679`, mae `0.042621`
- 20d: sample `8`, hit `0.375`, avg `-0.046429`, median `-0.001131`, mae `0.077688`
- 60d: sample `8`, hit `0.5`, avg `0.017696`, median `0.052255`, mae `0.058448`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.004738, 'median_return': -0.00201, 'mean_absolute_return': 0.016205, 'max_adverse_excursion': -0.052423, 'max_favorable_excursion': 0.030238}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.002973, 'median_return': 0.004366, 'mean_absolute_return': 0.015597, 'max_adverse_excursion': -0.039693, 'max_favorable_excursion': 0.020014}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.018604, 'median_return': -0.007679, 'mean_absolute_return': 0.042621, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.046429, 'median_return': -0.001131, 'mean_absolute_return': 0.077688, 'max_adverse_excursion': -0.222293, 'max_favorable_excursion': 0.061413}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.017696, 'median_return': 0.052255, 'mean_absolute_return': 0.058448, 'max_adverse_excursion': -0.053355, 'max_favorable_excursion': 0.109145}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': -0.001014, 'median_return': 0.013397, 'mean_absolute_return': 0.031942, 'max_adverse_excursion': -0.131419, 'max_favorable_excursion': 0.061209}, '5d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': -0.000403, 'median_return': 0.012885, 'mean_absolute_return': 0.036478, 'max_adverse_excursion': -0.213746, 'max_favorable_excursion': 0.079752}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.000938, 'median_return': 0.019024, 'mean_absolute_return': 0.049971, 'max_adverse_excursion': -0.205195, 'max_favorable_excursion': 0.126019}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.005347, 'median_return': 0.030297, 'mean_absolute_return': 0.073089, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.197508}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.027065, 'median_return': 0.049972, 'mean_absolute_return': 0.114124, 'max_adverse_excursion': -0.331416, 'max_favorable_excursion': 0.391299}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3875}, '5d': {'sample_size': 80, 'hit_rate': 0.3125}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.4}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': -0.001387, 'median_return': 0.011008, 'mean_absolute_return': 0.030368, 'max_adverse_excursion': -0.131419, 'max_favorable_excursion': 0.061209}, '5d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': -0.00066, 'median_return': 0.012713, 'mean_absolute_return': 0.03439, 'max_adverse_excursion': -0.213746, 'max_favorable_excursion': 0.079752}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': -0.001016, 'median_return': 0.016492, 'mean_absolute_return': 0.049236, 'max_adverse_excursion': -0.205195, 'max_favorable_excursion': 0.126019}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.00017, 'median_return': 0.025905, 'mean_absolute_return': 0.073549, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.197508}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.026128, 'median_return': 0.049972, 'mean_absolute_return': 0.108556, 'max_adverse_excursion': -0.331416, 'max_favorable_excursion': 0.391299}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.005151`, median `0.008733`, mae `0.018707`
- 5d: sample `20`, hit `0.75`, avg `0.009668`, median `0.0127`, mae `0.017531`
- 10d: sample `20`, hit `0.45`, avg `-0.002291`, median `-0.007679`, mae `0.039124`
- 20d: sample `20`, hit `0.65`, avg `5.1e-05`, median `0.025065`, mae `0.052893`
- 60d: sample `20`, hit `0.6`, avg `0.030526`, median `0.067551`, mae `0.068787`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.000451`, median `0.011008`, mae `0.026579`
- 5d: sample `60`, hit `0.7`, avg `0.001444`, median `0.0127`, mae `0.029828`
- 10d: sample `60`, hit `0.6`, avg `0.000342`, median `0.016492`, mae `0.044127`
- 20d: sample `60`, hit `0.6667`, avg `0.006425`, median `0.030297`, mae `0.062191`
- 60d: sample `60`, hit `0.6`, avg `0.027034`, median `0.052255`, mae `0.089593`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.000451`, median `0.011008`, mae `0.026579`
- 5d: sample `60`, hit `0.7`, avg `0.001444`, median `0.0127`, mae `0.029828`
- 10d: sample `60`, hit `0.6`, avg `0.000342`, median `0.016492`, mae `0.044127`
- 20d: sample `60`, hit `0.6667`, avg `0.006425`, median `0.030297`, mae `0.062191`
- 60d: sample `60`, hit `0.6`, avg `0.027034`, median `0.052255`, mae `0.089593`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `-0.001387`, median `0.011008`, mae `0.030368`
- 5d: sample `80`, hit `0.6875`, avg `-0.00066`, median `0.012713`, mae `0.03439`
- 10d: sample `80`, hit `0.5875`, avg `-0.001016`, median `0.016492`, mae `0.049236`
- 20d: sample `80`, hit `0.65`, avg `0.00017`, median `0.025905`, mae `0.073549`
- 60d: sample `80`, hit `0.6`, avg `0.026128`, median `0.049972`, mae `0.108556`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `-0.001387`, median `0.011008`, mae `0.030368`
- 5d: sample `80`, hit `0.6875`, avg `-0.00066`, median `0.012713`, mae `0.03439`
- 10d: sample `80`, hit `0.5875`, avg `-0.001016`, median `0.016492`, mae `0.049236`
- 20d: sample `80`, hit `0.65`, avg `0.00017`, median `0.025905`, mae `0.073549`
- 60d: sample `80`, hit `0.6`, avg `0.026128`, median `0.049972`, mae `0.108556`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
