# High Confidence Edge Report

Generated at: `2026-07-10T15:04:32.646135+00:00`

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
- 3d: sample `40`, hit `0.5`, avg `-0.002777`, median `0.001448`, mae `0.012946`
- 5d: sample `40`, hit `0.5`, avg `-0.003085`, median `0.000415`, mae `0.016862`
- 10d: sample `40`, hit `0.475`, avg `0.002241`, median `-0.0004`, mae `0.02064`
- 20d: sample `40`, hit `0.65`, avg `0.006513`, median `0.01011`, mae `0.033019`
- 60d: sample `40`, hit `0.625`, avg `0.025137`, median `0.046132`, mae `0.067166`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001284`, median `0.000145`, mae `0.010473`
- 5d: sample `40`, hit `0.525`, avg `-0.002672`, median `0.002694`, mae `0.014121`
- 10d: sample `40`, hit `0.55`, avg `-0.00217`, median `0.003491`, mae `0.020474`
- 20d: sample `40`, hit `0.7`, avg `-0.004007`, median `0.011728`, mae `0.033556`
- 60d: sample `40`, hit `0.425`, avg `-0.010945`, median `-0.009954`, mae `0.050924`

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
- 3d: sample `8`, hit `0.5`, avg `-0.011085`, median `0.00234`, mae `0.017505`
- 5d: sample `8`, hit `0.25`, avg `-0.01495`, median `-0.008162`, mae `0.020208`
- 10d: sample `8`, hit `0.25`, avg `-0.012357`, median `-0.01796`, mae `0.022654`
- 20d: sample `8`, hit `0.75`, avg `0.008856`, median `0.022652`, mae `0.024576`
- 60d: sample `8`, hit `0.625`, avg `0.034648`, median `0.059495`, mae `0.066144`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.011085`, median `0.00234`, mae `0.017505`
- 5d: sample `8`, hit `0.25`, avg `-0.01495`, median `-0.008162`, mae `0.020208`
- 10d: sample `8`, hit `0.25`, avg `-0.012357`, median `-0.01796`, mae `0.022654`
- 20d: sample `8`, hit `0.75`, avg `0.008856`, median `0.022652`, mae `0.024576`
- 60d: sample `8`, hit `0.625`, avg `0.034648`, median `0.059495`, mae `0.066144`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002777, 'median_return': 0.001448, 'mean_absolute_return': 0.012946, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.003085, 'median_return': 0.000415, 'mean_absolute_return': 0.016862, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.002241, 'median_return': -0.0004, 'mean_absolute_return': 0.02064, 'max_adverse_excursion': -0.036679, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.006513, 'median_return': 0.01011, 'mean_absolute_return': 0.033019, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.025137, 'median_return': 0.046132, 'mean_absolute_return': 0.067166, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001284, 'median_return': 0.000145, 'mean_absolute_return': 0.010473, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.002672, 'median_return': 0.002694, 'mean_absolute_return': 0.014121, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.032674}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.00217, 'median_return': 0.003491, 'mean_absolute_return': 0.020474, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.045189}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': -0.004007, 'median_return': 0.011728, 'mean_absolute_return': 0.033556, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.062475}, '60d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.010945, 'median_return': -0.009954, 'mean_absolute_return': 0.050924, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.08481}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.011085, 'median_return': 0.00234, 'mean_absolute_return': 0.017505, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.010322}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01495, 'median_return': -0.008162, 'mean_absolute_return': 0.020208, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.012357, 'median_return': -0.01796, 'mean_absolute_return': 0.022654, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.021953}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008856, 'median_return': 0.022652, 'mean_absolute_return': 0.024576, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.034648, 'median_return': 0.059495, 'mean_absolute_return': 0.066144, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001025, 'median_return': 0.000145, 'mean_absolute_return': 0.011065, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.001537, 'median_return': 0.003005, 'mean_absolute_return': 0.014967, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.001413, 'median_return': 0.003262, 'mean_absolute_return': 0.020324, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.000408, 'median_return': 0.010788, 'mean_absolute_return': 0.034255, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.004035, 'median_return': 0.012092, 'mean_absolute_return': 0.058256, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.525}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 30, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 32, 'both_miss': 28}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 32, 'both_miss': 28}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.05, 'both_hit': 42, 'both_miss': 18}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.025, 'both_hit': 33, 'both_miss': 27}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001119, 'median_return': 0.001999, 'mean_absolute_return': 0.011493, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.00012, 'median_return': 0.003197, 'mean_absolute_return': 0.016839, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.00173, 'median_return': 0.004067, 'mean_absolute_return': 0.024701, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.005332, 'median_return': 0.007366, 'mean_absolute_return': 0.038107, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.013459, 'median_return': 0.026139, 'mean_absolute_return': 0.058966, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.137137}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.005181, 'median_return': -0.001166, 'mean_absolute_return': 0.011925, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.005637, 'median_return': 0.000415, 'mean_absolute_return': 0.014144, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.001659, 'median_return': -0.0004, 'mean_absolute_return': 0.016413, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.007838, 'median_return': 0.019193, 'mean_absolute_return': 0.028468, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.000733, 'median_return': -0.004982, 'mean_absolute_return': 0.059124, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.00388`, median `-0.001166`, mae `0.012192`
- 5d: sample `60`, hit `0.4833`, avg `-0.00514`, median `-0.001796`, mae `0.015014`
- 10d: sample `60`, hit `0.45`, avg `-0.004008`, median `-0.001676`, mae `0.019716`
- 20d: sample `60`, hit `0.6833`, avg `-0.000874`, median `0.012291`, mae `0.033471`
- 60d: sample `60`, hit `0.4667`, avg `-0.001817`, median `-0.005523`, mae `0.055839`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001278`, median `0.000324`, mae `0.012726`
- 5d: sample `20`, hit `0.45`, avg `-0.004147`, median `-0.004461`, mae `0.016756`
- 10d: sample `20`, hit `0.45`, avg `-0.008707`, median `-0.010743`, mae `0.026322`
- 20d: sample `20`, hit `0.6`, avg `-0.018299`, median `0.003662`, mae `0.043477`
- 60d: sample `20`, hit `0.45`, avg `-0.006916`, median `-0.005997`, mae `0.049268`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.00388`, median `-0.001166`, mae `0.012192`
- 5d: sample `60`, hit `0.4833`, avg `-0.00514`, median `-0.001796`, mae `0.015014`
- 10d: sample `60`, hit `0.45`, avg `-0.004008`, median `-0.001676`, mae `0.019716`
- 20d: sample `60`, hit `0.6833`, avg `-0.000874`, median `0.012291`, mae `0.033471`
- 60d: sample `60`, hit `0.4667`, avg `-0.001817`, median `-0.005523`, mae `0.055839`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001278`, median `0.000324`, mae `0.012726`
- 5d: sample `20`, hit `0.45`, avg `-0.004147`, median `-0.004461`, mae `0.016756`
- 10d: sample `20`, hit `0.45`, avg `-0.008707`, median `-0.010743`, mae `0.026322`
- 20d: sample `20`, hit `0.6`, avg `-0.018299`, median `0.003662`, mae `0.043477`
- 60d: sample `20`, hit `0.45`, avg `-0.006916`, median `-0.005997`, mae `0.049268`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.009072`, median `-0.001658`, mae `0.015631`
- 5d: sample `20`, hit `0.4`, avg `-0.010078`, median `-0.004438`, mae `0.016801`
- 10d: sample `20`, hit `0.25`, avg `-0.007685`, median `-0.011432`, mae `0.018202`
- 20d: sample `20`, hit `0.65`, avg `0.005392`, median `0.020068`, mae `0.033301`
- 60d: sample `20`, hit `0.55`, avg `0.016439`, median `0.029831`, mae `0.065668`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.00388`, median `-0.001166`, mae `0.012192`
- 5d: sample `60`, hit `0.4833`, avg `-0.00514`, median `-0.001796`, mae `0.015014`
- 10d: sample `60`, hit `0.45`, avg `-0.004008`, median `-0.001676`, mae `0.019716`
- 20d: sample `60`, hit `0.6833`, avg `-0.000874`, median `0.012291`, mae `0.033471`
- 60d: sample `60`, hit `0.4667`, avg `-0.001817`, median `-0.005523`, mae `0.055839`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003517`, median `0.003538`, mae `0.010261`
- 5d: sample `20`, hit `0.6`, avg `0.003907`, median `0.008121`, mae `0.016923`
- 10d: sample `20`, hit `0.7`, avg `0.012168`, median `0.008202`, mae `0.023079`
- 20d: sample `20`, hit `0.65`, avg `0.007635`, median `0.009812`, mae `0.032737`
- 60d: sample `20`, hit `0.7`, avg `0.033834`, median `0.055266`, mae `0.068665`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.009072`, median `-0.001658`, mae `0.015631`
- 5d: sample `20`, hit `0.4`, avg `-0.010078`, median `-0.004438`, mae `0.016801`
- 10d: sample `20`, hit `0.25`, avg `-0.007685`, median `-0.011432`, mae `0.018202`
- 20d: sample `20`, hit `0.65`, avg `0.005392`, median `0.020068`, mae `0.033301`
- 60d: sample `20`, hit `0.55`, avg `0.016439`, median `0.029831`, mae `0.065668`

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
- 3d: sample `40`, hit `0.475`, avg `-0.005181`, median `-0.001166`, mae `0.011925`
- 5d: sample `40`, hit `0.5`, avg `-0.005637`, median `0.000415`, mae `0.014144`
- 10d: sample `40`, hit `0.45`, avg `-0.001659`, median `-0.0004`, mae `0.016413`
- 20d: sample `40`, hit `0.725`, avg `0.007838`, median `0.019193`, mae `0.028468`
- 60d: sample `40`, hit `0.475`, avg `0.000733`, median `-0.004982`, mae `0.059124`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001278`, median `0.000324`, mae `0.012726`
- 5d: sample `20`, hit `0.45`, avg `-0.004147`, median `-0.004461`, mae `0.016756`
- 10d: sample `20`, hit `0.45`, avg `-0.008707`, median `-0.010743`, mae `0.026322`
- 20d: sample `20`, hit `0.6`, avg `-0.018299`, median `0.003662`, mae `0.043477`
- 60d: sample `20`, hit `0.45`, avg `-0.006916`, median `-0.005997`, mae `0.049268`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001278`, median `0.000324`, mae `0.012726`
- 5d: sample `20`, hit `0.45`, avg `-0.004147`, median `-0.004461`, mae `0.016756`
- 10d: sample `20`, hit `0.45`, avg `-0.008707`, median `-0.010743`, mae `0.026322`
- 20d: sample `20`, hit `0.6`, avg `-0.018299`, median `0.003662`, mae `0.043477`
- 60d: sample `20`, hit `0.45`, avg `-0.006916`, median `-0.005997`, mae `0.049268`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002031`, median `0.000145`, mae `0.011709`
- 5d: sample `80`, hit `0.5125`, avg `-0.002878`, median `0.001259`, mae `0.015491`
- 10d: sample `80`, hit `0.5125`, avg `3.6e-05`, median `0.002362`, mae `0.020557`
- 20d: sample `80`, hit `0.675`, avg `0.001253`, median `0.010788`, mae `0.033287`
- 60d: sample `80`, hit `0.525`, avg `0.007096`, median `0.012273`, mae `0.059045`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002031`, median `0.000145`, mae `0.011709`
- 5d: sample `80`, hit `0.5125`, avg `-0.002878`, median `0.001259`, mae `0.015491`
- 10d: sample `80`, hit `0.5125`, avg `3.6e-05`, median `0.002362`, mae `0.020557`
- 20d: sample `80`, hit `0.675`, avg `0.001253`, median `0.010788`, mae `0.033287`
- 60d: sample `80`, hit `0.525`, avg `0.007096`, median `0.012273`, mae `0.059045`

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
