# High Confidence Edge Report

Generated at: `2026-10-23T08:52:45.285791+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002639`, median `0.001558`, mae `0.017119`
- 5d: sample `40`, hit `0.425`, avg `-0.001122`, median `-0.005024`, mae `0.017818`
- 10d: sample `40`, hit `0.6`, avg `0.008139`, median `0.007543`, mae `0.02107`
- 20d: sample `40`, hit `0.75`, avg `0.020164`, median `0.028264`, mae `0.03367`
- 60d: sample `40`, hit `0.875`, avg `0.063908`, median `0.068046`, mae `0.069441`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006391`, median `0.011229`, mae `0.01619`
- 5d: sample `20`, hit `0.7`, avg `0.007971`, median `0.017768`, mae `0.020852`
- 10d: sample `20`, hit `0.7`, avg `0.010664`, median `0.019956`, mae `0.030545`
- 20d: sample `20`, hit `0.6`, avg `0.014134`, median `0.010428`, mae `0.033743`
- 60d: sample `20`, hit `0.6`, avg `0.006608`, median `0.011393`, mae `0.036864`

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
- 3d: sample `8`, hit `0.625`, avg `0.007945`, median `0.022721`, mae `0.019182`
- 5d: sample `8`, hit `0.375`, avg `0.003897`, median `-0.006798`, mae `0.018469`
- 10d: sample `8`, hit `0.75`, avg `0.018665`, median `0.020918`, mae `0.022259`
- 20d: sample `8`, hit `0.875`, avg `0.035119`, median `0.031658`, mae `0.0375`
- 60d: sample `8`, hit `1.0`, avg `0.071928`, median `0.092646`, mae `0.071928`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.00638, 'median_return': 0.007259, 'mean_absolute_return': 0.010069, 'max_adverse_excursion': -0.013293, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008271, 'median_return': 0.012091, 'mean_absolute_return': 0.01658, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.009135, 'median_return': 0.019466, 'mean_absolute_return': 0.022195, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.01744, 'median_return': 0.015404, 'mean_absolute_return': 0.024099, 'max_adverse_excursion': -0.021537, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.014627, 'median_return': 0.038268, 'mean_absolute_return': 0.05583, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.099148}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.007945, 'median_return': 0.022721, 'mean_absolute_return': 0.019182, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.003897, 'median_return': -0.006798, 'mean_absolute_return': 0.018469, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.018665, 'median_return': 0.020918, 'mean_absolute_return': 0.022259, 'max_adverse_excursion': -0.011849, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.035119, 'median_return': 0.031658, 'mean_absolute_return': 0.0375, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.071928, 'median_return': 0.092646, 'mean_absolute_return': 0.071928, 'max_adverse_excursion': 0.025315, 'max_favorable_excursion': 0.103268}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.004131, 'median_return': 0.004569, 'mean_absolute_return': 0.014673, 'max_adverse_excursion': -0.035175, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.003456, 'median_return': 0.004149, 'mean_absolute_return': 0.018244, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007947, 'median_return': 0.010559, 'mean_absolute_return': 0.023882, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.016071, 'median_return': 0.016838, 'mean_absolute_return': 0.030606, 'max_adverse_excursion': -0.064325, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.033411, 'median_return': 0.038268, 'mean_absolute_return': 0.056334, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.174756}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 15, 'both_miss': 5}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.025, 'both_hit': 15, 'both_miss': 5}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.2, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.3, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.425, 'both_hit': 12, 'both_miss': 8}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.006735, 'median_return': 0.010917, 'mean_absolute_return': 0.016666, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.004676, 'median_return': 0.00971, 'mean_absolute_return': 0.019432, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.044543}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.009438, 'median_return': 0.011431, 'mean_absolute_return': 0.025477, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.022005, 'median_return': 0.028264, 'mean_absolute_return': 0.033821, 'max_adverse_excursion': -0.064325, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.037838, 'median_return': 0.054522, 'mean_absolute_return': 0.055889, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.117712}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002289, 'median_return': 0.004004, 'mean_absolute_return': 0.013583, 'max_adverse_excursion': -0.035175, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002324, 'median_return': 0.003714, 'mean_absolute_return': 0.017102, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.0086, 'median_return': 0.010559, 'mean_absolute_return': 0.021962, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.013946, 'median_return': 0.01443, 'mean_absolute_return': 0.028769, 'max_adverse_excursion': -0.055489, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.036688, 'median_return': 0.048421, 'mean_absolute_return': 0.059898, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.174756}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.007079`, median `0.010917`, mae `0.017141`
- 5d: sample `20`, hit `0.45`, avg `0.001381`, median `-0.003328`, mae `0.018011`
- 10d: sample `20`, hit `0.5`, avg `0.008212`, median `0.006053`, mae `0.02041`
- 20d: sample `20`, hit `0.9`, avg `0.029876`, median `0.030297`, mae `0.0339`
- 60d: sample `20`, hit `0.9`, avg `0.069068`, median `0.081091`, mae `0.074915`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.007079`, median `0.010917`, mae `0.017141`
- 5d: sample `20`, hit `0.45`, avg `0.001381`, median `-0.003328`, mae `0.018011`
- 10d: sample `20`, hit `0.5`, avg `0.008212`, median `0.006053`, mae `0.02041`
- 20d: sample `20`, hit `0.9`, avg `0.029876`, median `0.030297`, mae `0.0339`
- 60d: sample `20`, hit `0.9`, avg `0.069068`, median `0.081091`, mae `0.074915`

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
