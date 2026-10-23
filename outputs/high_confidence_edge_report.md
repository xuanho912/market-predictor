# High Confidence Edge Report

Generated at: `2026-10-23T01:28:27.032835+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `128`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `128`, gate `stronger_evidence`
- 5d: completed `128`, gate `stronger_evidence`
- 10d: completed `128`, gate `stronger_evidence`
- 20d: completed `128`, gate `stronger_evidence`
- 60d: completed `128`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00638`, median `0.007259`, mae `0.010069`
- 5d: sample `20`, hit `0.75`, avg `0.008271`, median `0.012091`, mae `0.01658`
- 10d: sample `20`, hit `0.75`, avg `0.009135`, median `0.019466`, mae `0.022195`
- 20d: sample `20`, hit `0.75`, avg `0.01744`, median `0.015404`, mae `0.024099`
- 60d: sample `20`, hit `0.6`, avg `0.014627`, median `0.038268`, mae `0.05583`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00389`, median `0.002296`, mae `0.016809`
- 5d: sample `60`, hit `0.5167`, avg `0.001909`, median `0.000989`, mae `0.018829`
- 10d: sample `60`, hit `0.6333`, avg `0.008981`, median `0.009975`, mae `0.024228`
- 20d: sample `60`, hit `0.7`, avg `0.018154`, median `0.024811`, mae `0.033694`
- 60d: sample `60`, hit `0.7833`, avg `0.044808`, median `0.054522`, mae `0.058582`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.007954`, median `0.007259`, mae `0.008245`
- 5d: sample `8`, hit `0.5`, avg `0.00142`, median `0.00774`, mae `0.017534`
- 10d: sample `8`, hit `0.625`, avg `-0.005397`, median `0.012215`, mae `0.025972`
- 20d: sample `8`, hit `0.625`, avg `0.009106`, median `0.015404`, mae `0.016554`
- 60d: sample `8`, hit `0.625`, avg `0.00634`, median `0.004698`, mae `0.061732`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.007954`, median `0.007259`, mae `0.008245`
- 5d: sample `8`, hit `0.5`, avg `0.00142`, median `0.00774`, mae `0.017534`
- 10d: sample `8`, hit `0.625`, avg `-0.005397`, median `0.012215`, mae `0.025972`
- 20d: sample `8`, hit `0.625`, avg `0.009106`, median `0.015404`, mae `0.016554`
- 60d: sample `8`, hit `0.625`, avg `0.00634`, median `0.004698`, mae `0.061732`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.00638, 'median_return': 0.007259, 'mean_absolute_return': 0.010069, 'max_adverse_excursion': -0.013293, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008271, 'median_return': 0.012091, 'mean_absolute_return': 0.01658, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.009135, 'median_return': 0.019466, 'mean_absolute_return': 0.022195, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.01744, 'median_return': 0.015404, 'mean_absolute_return': 0.024099, 'max_adverse_excursion': -0.021537, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.014627, 'median_return': 0.038268, 'mean_absolute_return': 0.05583, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.099148}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.007954, 'median_return': 0.007259, 'mean_absolute_return': 0.008245, 'max_adverse_excursion': -0.001166, 'max_favorable_excursion': 0.020779}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00142, 'median_return': 0.00774, 'mean_absolute_return': 0.017534, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.03068}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.005397, 'median_return': 0.012215, 'mean_absolute_return': 0.025972, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009106, 'median_return': 0.015404, 'mean_absolute_return': 0.016554, 'max_adverse_excursion': -0.020103, 'max_favorable_excursion': 0.03107}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.00634, 'median_return': 0.004698, 'mean_absolute_return': 0.061732, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.096597}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.00413, 'median_return': 0.004243, 'mean_absolute_return': 0.015889, 'max_adverse_excursion': -0.035175, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.003731, 'median_return': 0.00381, 'mean_absolute_return': 0.018348, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.010621, 'median_return': 0.010559, 'mean_absolute_return': 0.02347, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.018961, 'median_return': 0.019987, 'mean_absolute_return': 0.032933, 'max_adverse_excursion': -0.064325, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.040699, 'median_return': 0.049051, 'mean_absolute_return': 0.057467, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.174756}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 15, 'both_miss': 5}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.025, 'both_hit': 15, 'both_miss': 5}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.2, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.3, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.425, 'both_hit': 12, 'both_miss': 8}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.006617, 'median_return': 0.007259, 'mean_absolute_return': 0.014467, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.005874, 'median_return': 0.00971, 'mean_absolute_return': 0.018481, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.044543}, '10d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.009337, 'median_return': 0.011727, 'mean_absolute_return': 0.024383, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.020483, 'median_return': 0.024811, 'mean_absolute_return': 0.030581, 'max_adverse_excursion': -0.064325, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.030101, 'median_return': 0.048296, 'mean_absolute_return': 0.05587, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.117712}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001802, 'median_return': -0.007802, 'mean_absolute_return': 0.017097, 'max_adverse_excursion': -0.035175, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.003624, 'median_return': -0.005024, 'mean_absolute_return': 0.017624, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.008066, 'median_return': 0.009975, 'mean_absolute_return': 0.02173, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.010453, 'median_return': 0.005863, 'mean_absolute_return': 0.033439, 'max_adverse_excursion': -0.055489, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.058748, 'median_return': 0.05455, 'mean_absolute_return': 0.063967, 'max_adverse_excursion': -0.037128, 'max_favorable_excursion': 0.174756}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.006617`, median `0.007259`, mae `0.014467`
- 5d: sample `60`, hit `0.6333`, avg `0.005874`, median `0.00971`, mae `0.018481`
- 10d: sample `60`, hit `0.65`, avg `0.009337`, median `0.011727`, mae `0.024383`
- 20d: sample `60`, hit `0.75`, avg `0.020483`, median `0.024811`, mae `0.030581`
- 60d: sample `60`, hit `0.7`, avg `0.030101`, median `0.048296`, mae `0.05587`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001802`, median `-0.007802`, mae `0.017097`
- 5d: sample `20`, hit `0.4`, avg `-0.003624`, median `-0.005024`, mae `0.017624`
- 10d: sample `20`, hit `0.7`, avg `0.008066`, median `0.009975`, mae `0.02173`
- 20d: sample `20`, hit `0.6`, avg `0.010453`, median `0.005863`, mae `0.033439`
- 60d: sample `20`, hit `0.85`, avg `0.058748`, median `0.05455`, mae `0.063967`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00638`, median `0.007259`, mae `0.010069`
- 5d: sample `20`, hit `0.75`, avg `0.008271`, median `0.012091`, mae `0.01658`
- 10d: sample `20`, hit `0.75`, avg `0.009135`, median `0.019466`, mae `0.022195`
- 20d: sample `20`, hit `0.75`, avg `0.01744`, median `0.015404`, mae `0.024099`
- 60d: sample `20`, hit `0.6`, avg `0.014627`, median `0.038268`, mae `0.05583`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.006729`, median `0.007259`, mae `0.013605`
- 5d: sample `40`, hit `0.6`, avg `0.004826`, median `0.007324`, mae `0.017296`
- 10d: sample `40`, hit `0.625`, avg `0.008673`, median `0.0076`, mae `0.021303`
- 20d: sample `40`, hit `0.825`, avg `0.023658`, median `0.028264`, mae `0.029`
- 60d: sample `40`, hit `0.75`, avg `0.041848`, median `0.065295`, mae `0.065373`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00638`, median `0.007259`, mae `0.010069`
- 5d: sample `20`, hit `0.75`, avg `0.008271`, median `0.012091`, mae `0.01658`
- 10d: sample `20`, hit `0.75`, avg `0.009135`, median `0.019466`, mae `0.022195`
- 20d: sample `20`, hit `0.75`, avg `0.01744`, median `0.015404`, mae `0.024099`
- 60d: sample `20`, hit `0.6`, avg `0.014627`, median `0.038268`, mae `0.05583`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.006729`, median `0.007259`, mae `0.013605`
- 5d: sample `40`, hit `0.6`, avg `0.004826`, median `0.007324`, mae `0.017296`
- 10d: sample `40`, hit `0.625`, avg `0.008673`, median `0.0076`, mae `0.021303`
- 20d: sample `40`, hit `0.825`, avg `0.023658`, median `0.028264`, mae `0.029`
- 60d: sample `40`, hit `0.75`, avg `0.041848`, median `0.065295`, mae `0.065373`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001802`, median `-0.007802`, mae `0.017097`
- 5d: sample `20`, hit `0.4`, avg `-0.003624`, median `-0.005024`, mae `0.017624`
- 10d: sample `20`, hit `0.7`, avg `0.008066`, median `0.009975`, mae `0.02173`
- 20d: sample `20`, hit `0.6`, avg `0.010453`, median `0.005863`, mae `0.033439`
- 60d: sample `20`, hit `0.85`, avg `0.058748`, median `0.05455`, mae `0.063967`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00638`, median `0.007259`, mae `0.010069`
- 5d: sample `20`, hit `0.75`, avg `0.008271`, median `0.012091`, mae `0.01658`
- 10d: sample `20`, hit `0.75`, avg `0.009135`, median `0.019466`, mae `0.022195`
- 20d: sample `20`, hit `0.75`, avg `0.01744`, median `0.015404`, mae `0.024099`
- 60d: sample `20`, hit `0.6`, avg `0.014627`, median `0.038268`, mae `0.05583`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.004512`, median `0.004569`, mae `0.015124`
- 5d: sample `80`, hit `0.575`, avg `0.0035`, median `0.00381`, mae `0.018267`
- 10d: sample `80`, hit `0.6625`, avg `0.009019`, median `0.010559`, mae `0.02372`
- 20d: sample `80`, hit `0.7125`, avg `0.017976`, median `0.019238`, mae `0.031295`
- 60d: sample `80`, hit `0.7375`, avg `0.037263`, median `0.048421`, mae `0.057894`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00638`, median `0.007259`, mae `0.010069`
- 5d: sample `20`, hit `0.75`, avg `0.008271`, median `0.012091`, mae `0.01658`
- 10d: sample `20`, hit `0.75`, avg `0.009135`, median `0.019466`, mae `0.022195`
- 20d: sample `20`, hit `0.75`, avg `0.01744`, median `0.015404`, mae `0.024099`
- 60d: sample `20`, hit `0.6`, avg `0.014627`, median `0.038268`, mae `0.05583`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.004512`, median `0.004569`, mae `0.015124`
- 5d: sample `80`, hit `0.575`, avg `0.0035`, median `0.00381`, mae `0.018267`
- 10d: sample `80`, hit `0.6625`, avg `0.009019`, median `0.010559`, mae `0.02372`
- 20d: sample `80`, hit `0.7125`, avg `0.017976`, median `0.019238`, mae `0.031295`
- 60d: sample `80`, hit `0.7375`, avg `0.037263`, median `0.048421`, mae `0.057894`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.004512`, median `0.004569`, mae `0.015124`
- 5d: sample `80`, hit `0.575`, avg `0.0035`, median `0.00381`, mae `0.018267`
- 10d: sample `80`, hit `0.6625`, avg `0.009019`, median `0.010559`, mae `0.02372`
- 20d: sample `80`, hit `0.7125`, avg `0.017976`, median `0.019238`, mae `0.031295`
- 60d: sample `80`, hit `0.7375`, avg `0.037263`, median `0.048421`, mae `0.057894`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00638`, median `0.007259`, mae `0.010069`
- 5d: sample `20`, hit `0.75`, avg `0.008271`, median `0.012091`, mae `0.01658`
- 10d: sample `20`, hit `0.75`, avg `0.009135`, median `0.019466`, mae `0.022195`
- 20d: sample `20`, hit `0.75`, avg `0.01744`, median `0.015404`, mae `0.024099`
- 60d: sample `20`, hit `0.6`, avg `0.014627`, median `0.038268`, mae `0.05583`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00638`, median `0.007259`, mae `0.010069`
- 5d: sample `20`, hit `0.75`, avg `0.008271`, median `0.012091`, mae `0.01658`
- 10d: sample `20`, hit `0.75`, avg `0.009135`, median `0.019466`, mae `0.022195`
- 20d: sample `20`, hit `0.75`, avg `0.01744`, median `0.015404`, mae `0.024099`
- 60d: sample `20`, hit `0.6`, avg `0.014627`, median `0.038268`, mae `0.05583`

### risk_path_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00389`, median `0.002296`, mae `0.016809`
- 5d: sample `60`, hit `0.5167`, avg `0.001909`, median `0.000989`, mae `0.018829`
- 10d: sample `60`, hit `0.6333`, avg `0.008981`, median `0.009975`, mae `0.024228`
- 20d: sample `60`, hit `0.7`, avg `0.018154`, median `0.024811`, mae `0.033694`
- 60d: sample `60`, hit `0.7833`, avg `0.044808`, median `0.054522`, mae `0.058582`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
