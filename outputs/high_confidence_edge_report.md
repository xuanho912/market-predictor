# High Confidence Edge Report

Generated at: `2026-11-24T06:33:43.277626+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `216`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `216`, gate `stronger_evidence`
- 5d: completed `216`, gate `stronger_evidence`
- 10d: completed `216`, gate `stronger_evidence`
- 20d: completed `216`, gate `stronger_evidence`
- 60d: completed `216`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.5`, avg `0.002783`, median `0.003885`, mae `0.021665`
- 5d: sample `80`, hit `0.575`, avg `0.007633`, median `0.00438`, mae `0.025945`
- 10d: sample `80`, hit `0.675`, avg `0.019184`, median `0.013222`, mae `0.035234`
- 20d: sample `80`, hit `0.5625`, avg `0.018671`, median `0.014932`, mae `0.044063`
- 60d: sample `80`, hit `0.675`, avg `0.052464`, median `0.067623`, mae `0.083034`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.004212`, median `0.009959`, mae `0.020899`
- 5d: sample `8`, hit `0.5`, avg `0.002741`, median `0.000889`, mae `0.021678`
- 10d: sample `8`, hit `0.5`, avg `0.004312`, median `0.000121`, mae `0.02457`
- 20d: sample `8`, hit `0.875`, avg `0.026908`, median `0.033112`, mae `0.027608`
- 60d: sample `8`, hit `0.75`, avg `0.086299`, median `0.134256`, mae `0.099932`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.004212`, median `0.009959`, mae `0.020899`
- 5d: sample `8`, hit `0.5`, avg `0.002741`, median `0.000889`, mae `0.021678`
- 10d: sample `8`, hit `0.5`, avg `0.004312`, median `0.000121`, mae `0.02457`
- 20d: sample `8`, hit `0.875`, avg `0.026908`, median `0.033112`, mae `0.027608`
- 60d: sample `8`, hit `0.75`, avg `0.086299`, median `0.134256`, mae `0.099932`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004212, 'median_return': 0.009959, 'mean_absolute_return': 0.020899, 'max_adverse_excursion': -0.026721, 'max_favorable_excursion': 0.043484}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002741, 'median_return': 0.000889, 'mean_absolute_return': 0.021678, 'max_adverse_excursion': -0.027012, 'max_favorable_excursion': 0.05891}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004312, 'median_return': 0.000121, 'mean_absolute_return': 0.02457, 'max_adverse_excursion': -0.034557, 'max_favorable_excursion': 0.06525}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.026908, 'median_return': 0.033112, 'mean_absolute_return': 0.027608, 'max_adverse_excursion': -0.002799, 'max_favorable_excursion': 0.056142}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.086299, 'median_return': 0.134256, 'mean_absolute_return': 0.099932, 'max_adverse_excursion': -0.030956, 'max_favorable_excursion': 0.162502}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.002624, 'median_return': -6.1e-05, 'mean_absolute_return': 0.02175, 'max_adverse_excursion': -0.05525, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.008177, 'median_return': 0.004484, 'mean_absolute_return': 0.026419, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.020836, 'median_return': 0.016658, 'mean_absolute_return': 0.036419, 'max_adverse_excursion': -0.088606, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.017756, 'median_return': 0.006559, 'mean_absolute_return': 0.045891, 'max_adverse_excursion': -0.087865, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.048705, 'median_return': 0.065834, 'mean_absolute_return': 0.081157, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.355869}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.425}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009664, 'median_return': 0.010671, 'mean_absolute_return': 0.028357, 'max_adverse_excursion': -0.047619, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.016872, 'median_return': 0.021712, 'mean_absolute_return': 0.034208, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.030184, 'median_return': 0.044681, 'mean_absolute_return': 0.049884, 'max_adverse_excursion': -0.088606, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.035272, 'median_return': 0.031569, 'mean_absolute_return': 0.055637, 'max_adverse_excursion': -0.071567, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.097366, 'median_return': 0.113901, 'mean_absolute_return': 0.110389, 'max_adverse_excursion': -0.05129, 'max_favorable_excursion': 0.355869}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 0.000489, 'median_return': -0.001603, 'mean_absolute_return': 0.019434, 'max_adverse_excursion': -0.05525, 'max_favorable_excursion': 0.054095}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.004554, 'median_return': 0.002462, 'mean_absolute_return': 0.02319, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.083508}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.015517, 'median_return': 0.011855, 'mean_absolute_return': 0.030351, 'max_adverse_excursion': -0.049389, 'max_favorable_excursion': 0.107737}, '20d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.013137, 'median_return': 0.003056, 'mean_absolute_return': 0.040205, 'max_adverse_excursion': -0.087865, 'max_favorable_excursion': 0.136797}, '60d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.037497, 'median_return': 0.063683, 'mean_absolute_return': 0.073916, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.156899}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.009664`, median `0.010671`, mae `0.028357`
- 5d: sample `20`, hit `0.65`, avg `0.016872`, median `0.021712`, mae `0.034208`
- 10d: sample `20`, hit `0.7`, avg `0.030184`, median `0.044681`, mae `0.049884`
- 20d: sample `20`, hit `0.7`, avg `0.035272`, median `0.031569`, mae `0.055637`
- 60d: sample `20`, hit `0.8`, avg `0.097366`, median `0.113901`, mae `0.110389`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `0.000489`, median `-0.001603`, mae `0.019434`
- 5d: sample `60`, hit `0.55`, avg `0.004554`, median `0.002462`, mae `0.02319`
- 10d: sample `60`, hit `0.6667`, avg `0.015517`, median `0.011855`, mae `0.030351`
- 20d: sample `60`, hit `0.5167`, avg `0.013137`, median `0.003056`, mae `0.040205`
- 60d: sample `60`, hit `0.6333`, avg `0.037497`, median `0.063683`, mae `0.073916`

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
- 3d: sample `60`, hit `0.45`, avg `0.000489`, median `-0.001603`, mae `0.019434`
- 5d: sample `60`, hit `0.55`, avg `0.004554`, median `0.002462`, mae `0.02319`
- 10d: sample `60`, hit `0.6667`, avg `0.015517`, median `0.011855`, mae `0.030351`
- 20d: sample `60`, hit `0.5167`, avg `0.013137`, median `0.003056`, mae `0.040205`
- 60d: sample `60`, hit `0.6333`, avg `0.037497`, median `0.063683`, mae `0.073916`

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
- 3d: sample `80`, hit `0.5`, avg `0.002783`, median `0.003885`, mae `0.021665`
- 5d: sample `80`, hit `0.575`, avg `0.007633`, median `0.00438`, mae `0.025945`
- 10d: sample `80`, hit `0.675`, avg `0.019184`, median `0.013222`, mae `0.035234`
- 20d: sample `80`, hit `0.5625`, avg `0.018671`, median `0.014932`, mae `0.044063`
- 60d: sample `80`, hit `0.675`, avg `0.052464`, median `0.067623`, mae `0.083034`

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
- 3d: sample `80`, hit `0.5`, avg `0.002783`, median `0.003885`, mae `0.021665`
- 5d: sample `80`, hit `0.575`, avg `0.007633`, median `0.00438`, mae `0.025945`
- 10d: sample `80`, hit `0.675`, avg `0.019184`, median `0.013222`, mae `0.035234`
- 20d: sample `80`, hit `0.5625`, avg `0.018671`, median `0.014932`, mae `0.044063`
- 60d: sample `80`, hit `0.675`, avg `0.052464`, median `0.067623`, mae `0.083034`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
