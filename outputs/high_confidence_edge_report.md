# High Confidence Edge Report

Generated at: `2026-06-24T23:47:20.531353+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004201`, median `0.008337`, mae `0.018862`
- 5d: sample `20`, hit `0.55`, avg `0.001736`, median `0.007338`, mae `0.017922`
- 10d: sample `20`, hit `0.5`, avg `0.005043`, median `0.000514`, mae `0.026165`
- 20d: sample `20`, hit `0.65`, avg `0.009407`, median `0.01859`, mae `0.048593`
- 60d: sample `20`, hit `0.85`, avg `0.061082`, median `0.074154`, mae `0.093158`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.001519`, median `-0.000756`, mae `0.014833`
- 5d: sample `60`, hit `0.4167`, avg `-0.002971`, median `-0.006048`, mae `0.019587`
- 10d: sample `60`, hit `0.4667`, avg `-0.000311`, median `-0.001222`, mae `0.0214`
- 20d: sample `60`, hit `0.7833`, avg `0.015059`, median `0.020783`, mae `0.031553`
- 60d: sample `60`, hit `0.7667`, avg `0.042458`, median `0.060303`, mae `0.064407`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.005045`, median `0.0017`, mae `0.012808`
- 5d: sample `8`, hit `0.5`, avg `0.004988`, median `0.011986`, mae `0.013456`
- 10d: sample `8`, hit `0.375`, avg `0.00317`, median `-0.004946`, mae `0.02712`
- 20d: sample `8`, hit `0.625`, avg `0.006138`, median `0.01859`, mae `0.040341`
- 60d: sample `8`, hit `0.875`, avg `0.06146`, median `0.076199`, mae `0.077346`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.005045`, median `0.0017`, mae `0.012808`
- 5d: sample `8`, hit `0.5`, avg `0.004988`, median `0.011986`, mae `0.013456`
- 10d: sample `8`, hit `0.375`, avg `0.00317`, median `-0.004946`, mae `0.02712`
- 20d: sample `8`, hit `0.625`, avg `0.006138`, median `0.01859`, mae `0.040341`
- 60d: sample `8`, hit `0.875`, avg `0.06146`, median `0.076199`, mae `0.077346`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.004201, 'median_return': 0.008337, 'mean_absolute_return': 0.018862, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001736, 'median_return': 0.007338, 'mean_absolute_return': 0.017922, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.005043, 'median_return': 0.000514, 'mean_absolute_return': 0.026165, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009407, 'median_return': 0.01859, 'mean_absolute_return': 0.048593, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.061082, 'median_return': 0.074154, 'mean_absolute_return': 0.093158, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.001519, 'median_return': -0.000756, 'mean_absolute_return': 0.014833, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.002971, 'median_return': -0.006048, 'mean_absolute_return': 0.019587, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.000311, 'median_return': -0.001222, 'mean_absolute_return': 0.0214, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.015059, 'median_return': 0.020783, 'mean_absolute_return': 0.031553, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.042458, 'median_return': 0.060303, 'mean_absolute_return': 0.064407, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.164609}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.005045, 'median_return': 0.0017, 'mean_absolute_return': 0.012808, 'max_adverse_excursion': -0.012528, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004988, 'median_return': 0.011986, 'mean_absolute_return': 0.013456, 'max_adverse_excursion': -0.013303, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.00317, 'median_return': -0.004946, 'mean_absolute_return': 0.02712, 'max_adverse_excursion': -0.032048, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006138, 'median_return': 0.01859, 'mean_absolute_return': 0.040341, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.06146, 'median_return': 0.076199, 'mean_absolute_return': 0.077346, 'max_adverse_excursion': -0.063544, 'max_favorable_excursion': 0.114016}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.001872, 'median_return': 0.001558, 'mean_absolute_return': 0.016177, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.002548, 'median_return': -0.004216, 'mean_absolute_return': 0.019806, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.000789, 'median_return': -0.001083, 'mean_absolute_return': 0.022088, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.01448, 'median_return': 0.020783, 'mean_absolute_return': 0.03531, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.04552, 'median_return': 0.062356, 'mean_absolute_return': 0.070956, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.75}, '60d': {'sample_size': 80, 'hit_rate': 0.7875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.075, 'both_hit': 33, 'both_miss': 27}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.075, 'both_hit': 29, 'both_miss': 31}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.025, 'both_hit': 29, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': 0.075, 'both_hit': 47, 'both_miss': 13}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7875, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': 0.05, 'both_hit': 51, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': 0.00219, 'median_return': 0.001558, 'mean_absolute_return': 0.01584, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.001794, 'median_return': -0.003879, 'mean_absolute_return': 0.019171, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.001027, 'median_return': -0.001222, 'mean_absolute_return': 0.022591, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.013646, 'median_return': 0.020751, 'mean_absolute_return': 0.035813, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.047114, 'median_return': 0.065295, 'mean_absolute_return': 0.071595, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `0.000459`, median `-0.003228`, mae `0.01544`
- 5d: sample `40`, hit `0.45`, avg `-0.002582`, median `-0.002002`, mae `0.016833`
- 10d: sample `40`, hit `0.475`, avg `-0.001238`, median `-0.003263`, mae `0.024242`
- 20d: sample `40`, hit `0.65`, avg `0.002014`, median `0.016065`, mae `0.040008`
- 60d: sample `40`, hit `0.725`, avg `0.033811`, median `0.047238`, mae `0.074856`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.001519`, median `-0.000756`, mae `0.014833`
- 5d: sample `60`, hit `0.4167`, avg `-0.002971`, median `-0.006048`, mae `0.019587`
- 10d: sample `60`, hit `0.4667`, avg `-0.000311`, median `-0.001222`, mae `0.0214`
- 20d: sample `60`, hit `0.7833`, avg `0.015059`, median `0.020783`, mae `0.031553`
- 60d: sample `60`, hit `0.7667`, avg `0.042458`, median `0.060303`, mae `0.064407`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `0.000459`, median `-0.003228`, mae `0.01544`
- 5d: sample `40`, hit `0.45`, avg `-0.002582`, median `-0.002002`, mae `0.016833`
- 10d: sample `40`, hit `0.475`, avg `-0.001238`, median `-0.003263`, mae `0.024242`
- 20d: sample `40`, hit `0.65`, avg `0.002014`, median `0.016065`, mae `0.040008`
- 60d: sample `40`, hit `0.725`, avg `0.033811`, median `0.047238`, mae `0.074856`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.001519`, median `-0.000756`, mae `0.014833`
- 5d: sample `60`, hit `0.4167`, avg `-0.002971`, median `-0.006048`, mae `0.019587`
- 10d: sample `60`, hit `0.4667`, avg `-0.000311`, median `-0.001222`, mae `0.0214`
- 20d: sample `60`, hit `0.7833`, avg `0.015059`, median `0.020783`, mae `0.031553`
- 60d: sample `60`, hit `0.7667`, avg `0.042458`, median `0.060303`, mae `0.064407`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004201`, median `0.008337`, mae `0.018862`
- 5d: sample `20`, hit `0.55`, avg `0.001736`, median `0.007338`, mae `0.017922`
- 10d: sample `20`, hit `0.5`, avg `0.005043`, median `0.000514`, mae `0.026165`
- 20d: sample `20`, hit `0.65`, avg `0.009407`, median `0.01859`, mae `0.048593`
- 60d: sample `20`, hit `0.85`, avg `0.061082`, median `0.074154`, mae `0.093158`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.00392`, median `0.004243`, mae `0.01624`
- 5d: sample `40`, hit `0.45`, avg `-0.001006`, median `-0.004216`, mae `0.021509`
- 10d: sample `40`, hit `0.475`, avg `0.003293`, median `-0.001083`, mae `0.02094`
- 20d: sample `40`, hit `0.85`, avg `0.025278`, median `0.028791`, mae `0.031618`
- 60d: sample `40`, hit `0.85`, avg `0.060418`, median `0.069629`, mae `0.068334`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `0.000459`, median `-0.003228`, mae `0.01544`
- 5d: sample `40`, hit `0.45`, avg `-0.002582`, median `-0.002002`, mae `0.016833`
- 10d: sample `40`, hit `0.475`, avg `-0.001238`, median `-0.003263`, mae `0.024242`
- 20d: sample `40`, hit `0.65`, avg `0.002014`, median `0.016065`, mae `0.040008`
- 60d: sample `40`, hit `0.725`, avg `0.033811`, median `0.047238`, mae `0.074856`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.00392`, median `0.004243`, mae `0.01624`
- 5d: sample `40`, hit `0.45`, avg `-0.001006`, median `-0.004216`, mae `0.021509`
- 10d: sample `40`, hit `0.475`, avg `0.003293`, median `-0.001083`, mae `0.02094`
- 20d: sample `40`, hit `0.85`, avg `0.025278`, median `0.028791`, mae `0.031618`
- 60d: sample `40`, hit `0.85`, avg `0.060418`, median `0.069629`, mae `0.068334`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004201`, median `0.008337`, mae `0.018862`
- 5d: sample `20`, hit `0.55`, avg `0.001736`, median `0.007338`, mae `0.017922`
- 10d: sample `20`, hit `0.5`, avg `0.005043`, median `0.000514`, mae `0.026165`
- 20d: sample `20`, hit `0.65`, avg `0.009407`, median `0.01859`, mae `0.048593`
- 60d: sample `20`, hit `0.85`, avg `0.061082`, median `0.074154`, mae `0.093158`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `0.000459`, median `-0.003228`, mae `0.01544`
- 5d: sample `40`, hit `0.45`, avg `-0.002582`, median `-0.002002`, mae `0.016833`
- 10d: sample `40`, hit `0.475`, avg `-0.001238`, median `-0.003263`, mae `0.024242`
- 20d: sample `40`, hit `0.65`, avg `0.002014`, median `0.016065`, mae `0.040008`
- 60d: sample `40`, hit `0.725`, avg `0.033811`, median `0.047238`, mae `0.074856`

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

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.003653`, median `0.006264`, mae `0.018444`
- 5d: sample `40`, hit `0.575`, avg `0.002339`, median `0.007338`, mae `0.022011`
- 10d: sample `40`, hit `0.525`, avg `0.004209`, median `0.002755`, mae `0.028337`
- 20d: sample `40`, hit `0.725`, avg `0.018583`, median `0.032112`, mae `0.043745`
- 60d: sample `40`, hit `0.8`, avg `0.056939`, median `0.071203`, mae `0.078478`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.003653`, median `0.006264`, mae `0.018444`
- 5d: sample `40`, hit `0.575`, avg `0.002339`, median `0.007338`, mae `0.022011`
- 10d: sample `40`, hit `0.525`, avg `0.004209`, median `0.002755`, mae `0.028337`
- 20d: sample `40`, hit `0.725`, avg `0.018583`, median `0.032112`, mae `0.043745`
- 60d: sample `40`, hit `0.8`, avg `0.056939`, median `0.071203`, mae `0.078478`

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
