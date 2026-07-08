# High Confidence Edge Report

Generated at: `2026-07-08T21:38:52.758509+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.00041`, median `0.00234`, mae `0.013819`
- 5d: sample `40`, hit `0.525`, avg `-0.001874`, median `0.003005`, mae `0.015528`
- 10d: sample `40`, hit `0.5`, avg `0.003134`, median `0.000242`, mae `0.016683`
- 20d: sample `40`, hit `0.775`, avg `0.017386`, median `0.021759`, mae `0.031787`
- 60d: sample `40`, hit `0.75`, avg `0.041715`, median `0.052998`, mae `0.06781`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000989`, median `-0.001166`, mae `0.011846`
- 5d: sample `40`, hit `0.5`, avg `-0.001796`, median `0.000688`, mae `0.016413`
- 10d: sample `40`, hit `0.45`, avg `-0.001642`, median `-0.007117`, mae `0.022862`
- 20d: sample `40`, hit `0.6`, avg `-0.004668`, median `0.007366`, mae `0.034073`
- 60d: sample `40`, hit `0.4`, avg `-0.009562`, median `-0.013501`, mae `0.054227`

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
- 3d: sample `8`, hit `0.375`, avg `-0.014051`, median `-0.001658`, mae `0.015972`
- 5d: sample `8`, hit `0.25`, avg `-0.017492`, median `-0.013034`, mae `0.020876`
- 10d: sample `8`, hit `0.375`, avg `-0.006656`, median `-0.0004`, mae `0.018593`
- 20d: sample `8`, hit `0.875`, avg `0.01926`, median `0.031196`, mae `0.033086`
- 60d: sample `8`, hit `0.875`, avg `0.061772`, median `0.092646`, mae `0.07599`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.014051`, median `-0.001658`, mae `0.015972`
- 5d: sample `8`, hit `0.25`, avg `-0.017492`, median `-0.013034`, mae `0.020876`
- 10d: sample `8`, hit `0.375`, avg `-0.006656`, median `-0.0004`, mae `0.018593`
- 20d: sample `8`, hit `0.875`, avg `0.01926`, median `0.031196`, mae `0.033086`
- 60d: sample `8`, hit `0.875`, avg `0.061772`, median `0.092646`, mae `0.07599`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.00041, 'median_return': 0.00234, 'mean_absolute_return': 0.013819, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001874, 'median_return': 0.003005, 'mean_absolute_return': 0.015528, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.003134, 'median_return': 0.000242, 'mean_absolute_return': 0.016683, 'max_adverse_excursion': -0.036679, 'max_favorable_excursion': 0.042458}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.017386, 'median_return': 0.021759, 'mean_absolute_return': 0.031787, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.041715, 'median_return': 0.052998, 'mean_absolute_return': 0.06781, 'max_adverse_excursion': -0.093084, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.000989, 'median_return': -0.001166, 'mean_absolute_return': 0.011846, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001796, 'median_return': 0.000688, 'mean_absolute_return': 0.016413, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.001642, 'median_return': -0.007117, 'mean_absolute_return': 0.022862, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': -0.004668, 'median_return': 0.007366, 'mean_absolute_return': 0.034073, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.062475}, '60d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.009562, 'median_return': -0.013501, 'mean_absolute_return': 0.054227, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.106573}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.014051, 'median_return': -0.001658, 'mean_absolute_return': 0.015972, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.003785}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.017492, 'median_return': -0.013034, 'mean_absolute_return': 0.020876, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.006656, 'median_return': -0.0004, 'mean_absolute_return': 0.018593, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.020918}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.01926, 'median_return': 0.031196, 'mean_absolute_return': 0.033086, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.061772, 'median_return': 0.092646, 'mean_absolute_return': 0.07599, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.00124, 'median_return': 0.000766, 'mean_absolute_return': 0.012484, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -9.6e-05, 'median_return': 0.001303, 'mean_absolute_return': 0.015426, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.001568, 'median_return': -0.001222, 'mean_absolute_return': 0.019904, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.004925, 'median_return': 0.012291, 'mean_absolute_return': 0.032913, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.010999, 'median_return': 0.014933, 'mean_absolute_return': 0.059355, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.575}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 22, 'both_miss': 18}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.0, 'both_hit': 21, 'both_miss': 19}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 20, 'both_miss': 20}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.1, 'both_hit': 31, 'both_miss': 9}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.1, 'both_hit': 30, 'both_miss': 10}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002044, 'median_return': 0.003026, 'mean_absolute_return': 0.013903, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.002496, 'median_return': 0.00596, 'mean_absolute_return': 0.017889, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.005424, 'median_return': 0.00903, 'mean_absolute_return': 0.023425, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.004453, 'median_return': 0.013877, 'mean_absolute_return': 0.033648, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.062475}, '60d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.007851, 'median_return': 0.010234, 'mean_absolute_return': 0.055394, 'max_adverse_excursion': -0.118336, 'max_favorable_excursion': 0.106573}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.002623, 'median_return': -0.001166, 'mean_absolute_return': 0.011763, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.006166, 'median_return': 0.000208, 'mean_absolute_return': 0.014052, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.003932, 'median_return': -0.00676, 'mean_absolute_return': 0.016121, 'max_adverse_excursion': -0.03706, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.008265, 'median_return': 0.020068, 'mean_absolute_return': 0.032213, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.024302, 'median_return': 0.037425, 'mean_absolute_return': 0.066644, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `-0.00029`, median `0.000603`, mae `0.012833`
- 5d: sample `80`, hit `0.5125`, avg `-0.001835`, median `0.000688`, mae `0.015971`
- 10d: sample `80`, hit `0.475`, avg `0.000746`, median `-0.001222`, mae `0.019773`
- 20d: sample `80`, hit `0.6875`, avg `0.006359`, median `0.013877`, mae `0.03293`
- 60d: sample `80`, hit `0.575`, avg `0.016077`, median `0.023755`, mae `0.061019`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `-0.00029`, median `0.000603`, mae `0.012833`
- 5d: sample `80`, hit `0.5125`, avg `-0.001835`, median `0.000688`, mae `0.015971`
- 10d: sample `80`, hit `0.475`, avg `0.000746`, median `-0.001222`, mae `0.019773`
- 20d: sample `80`, hit `0.6875`, avg `0.006359`, median `0.013877`, mae `0.03293`
- 60d: sample `80`, hit `0.575`, avg `0.016077`, median `0.023755`, mae `0.061019`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.00012`, median `0.001999`, mae `0.014492`
- 5d: sample `60`, hit `0.4833`, avg `-0.002014`, median `-0.000371`, mae `0.01785`
- 10d: sample `60`, hit `0.5167`, avg `0.003356`, median `0.003262`, mae `0.020918`
- 20d: sample `60`, hit `0.7667`, avg `0.011709`, median `0.018868`, mae `0.034195`
- 60d: sample `60`, hit `0.6333`, avg `0.026826`, median `0.045044`, mae `0.063313`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `-0.00029`, median `0.000603`, mae `0.012833`
- 5d: sample `80`, hit `0.5125`, avg `-0.001835`, median `0.000688`, mae `0.015971`
- 10d: sample `80`, hit `0.475`, avg `0.000746`, median `-0.001222`, mae `0.019773`
- 20d: sample `80`, hit `0.6875`, avg `0.006359`, median `0.013877`, mae `0.03293`
- 60d: sample `80`, hit `0.575`, avg `0.016077`, median `0.023755`, mae `0.061019`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.00012`, median `0.001999`, mae `0.014492`
- 5d: sample `60`, hit `0.4833`, avg `-0.002014`, median `-0.000371`, mae `0.01785`
- 10d: sample `60`, hit `0.5167`, avg `0.003356`, median `0.003262`, mae `0.020918`
- 20d: sample `60`, hit `0.7667`, avg `0.011709`, median `0.018868`, mae `0.034195`
- 60d: sample `60`, hit `0.6333`, avg `0.026826`, median `0.045044`, mae `0.063313`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001519`, median `-0.001166`, mae `0.007856`
- 5d: sample `20`, hit `0.6`, avg `-0.001297`, median `0.001303`, mae `0.010332`
- 10d: sample `20`, hit `0.35`, avg `-0.007083`, median `-0.007491`, mae `0.016337`
- 20d: sample `20`, hit `0.45`, avg `-0.009691`, median `-0.003522`, mae `0.029136`
- 60d: sample `20`, hit `0.4`, avg `-0.016172`, median `-0.020815`, mae `0.054136`

### mixed_internal_resonance
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.00012`, median `0.001999`, mae `0.014492`
- 5d: sample `60`, hit `0.4833`, avg `-0.002014`, median `-0.000371`, mae `0.01785`
- 10d: sample `60`, hit `0.5167`, avg `0.003356`, median `0.003262`, mae `0.020918`
- 20d: sample `60`, hit `0.7667`, avg `0.011709`, median `0.018868`, mae `0.034195`
- 60d: sample `60`, hit `0.6333`, avg `0.026826`, median `0.045044`, mae `0.063313`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001519`, median `-0.001166`, mae `0.007856`
- 5d: sample `20`, hit `0.6`, avg `-0.001297`, median `0.001303`, mae `0.010332`
- 10d: sample `20`, hit `0.35`, avg `-0.007083`, median `-0.007491`, mae `0.016337`
- 20d: sample `20`, hit `0.45`, avg `-0.009691`, median `-0.003522`, mae `0.029136`
- 60d: sample `20`, hit `0.4`, avg `-0.016172`, median `-0.020815`, mae `0.054136`

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
