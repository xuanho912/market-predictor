# High Confidence Edge Report

Generated at: `2026-06-26T23:46:17.935010+00:00`

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
- 3d: sample `40`, hit `0.5`, avg `0.001433`, median `0.0017`, mae `0.016637`
- 5d: sample `40`, hit `0.525`, avg `0.002016`, median `0.002616`, mae `0.02064`
- 10d: sample `40`, hit `0.5`, avg `0.001167`, median `0.000514`, mae `0.025676`
- 20d: sample `40`, hit `0.675`, avg `0.013547`, median `0.028065`, mae `0.04135`
- 60d: sample `40`, hit `0.8`, avg `0.053231`, median `0.069875`, mae `0.075352`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `0.000524`, median `-0.001166`, mae `0.013438`
- 5d: sample `40`, hit `0.35`, avg `-0.00517`, median `-0.007788`, mae `0.015903`
- 10d: sample `40`, hit `0.45`, avg `-0.000645`, median `-0.001663`, mae `0.01688`
- 20d: sample `40`, hit `0.8`, avg `0.011852`, median `0.019987`, mae `0.02625`
- 60d: sample `40`, hit `0.8`, avg `0.039988`, median `0.054522`, mae `0.064644`

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
- 3d: sample `8`, hit `0.5`, avg `0.003004`, median `0.006537`, mae `0.016355`
- 5d: sample `8`, hit `0.75`, avg `0.008808`, median `0.028762`, mae `0.024503`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.009212`, mae `0.036506`
- 20d: sample `8`, hit `0.875`, avg `0.030931`, median `0.037002`, mae `0.034027`
- 60d: sample `8`, hit `0.875`, avg `0.054415`, median `0.062356`, mae `0.055199`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.003004`, median `0.006537`, mae `0.016355`
- 5d: sample `8`, hit `0.75`, avg `0.008808`, median `0.028762`, mae `0.024503`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.009212`, mae `0.036506`
- 20d: sample `8`, hit `0.875`, avg `0.030931`, median `0.037002`, mae `0.034027`
- 60d: sample `8`, hit `0.875`, avg `0.054415`, median `0.062356`, mae `0.055199`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.001433, 'median_return': 0.0017, 'mean_absolute_return': 0.016637, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.002016, 'median_return': 0.002616, 'mean_absolute_return': 0.02064, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.001167, 'median_return': 0.000514, 'mean_absolute_return': 0.025676, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.013547, 'median_return': 0.028065, 'mean_absolute_return': 0.04135, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.053231, 'median_return': 0.069875, 'mean_absolute_return': 0.075352, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.000524, 'median_return': -0.001166, 'mean_absolute_return': 0.013438, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.028209}, '5d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.00517, 'median_return': -0.007788, 'mean_absolute_return': 0.015903, 'max_adverse_excursion': -0.032974, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.000645, 'median_return': -0.001663, 'mean_absolute_return': 0.01688, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.011852, 'median_return': 0.019987, 'mean_absolute_return': 0.02625, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.039988, 'median_return': 0.054522, 'mean_absolute_return': 0.064644, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.117712}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003004, 'median_return': 0.006537, 'mean_absolute_return': 0.016355, 'max_adverse_excursion': -0.01871, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008808, 'median_return': 0.028762, 'mean_absolute_return': 0.024503, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002268, 'median_return': 0.009212, 'mean_absolute_return': 0.036506, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.030931, 'median_return': 0.037002, 'mean_absolute_return': 0.034027, 'max_adverse_excursion': -0.012383, 'max_favorable_excursion': 0.060178}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.054415, 'median_return': 0.062356, 'mean_absolute_return': 0.055199, 'max_adverse_excursion': -0.003136, 'max_favorable_excursion': 0.087998}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.000754, 'median_return': -0.001166, 'mean_absolute_return': 0.014891, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.002731, 'median_return': -0.006048, 'mean_absolute_return': 0.017579, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 3.8e-05, 'median_return': -0.001663, 'mean_absolute_return': 0.019586, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.010673, 'median_return': 0.019987, 'mean_absolute_return': 0.033775, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.045742, 'median_return': 0.067551, 'mean_absolute_return': 0.071642, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.6375}, '60d': {'sample_size': 80, 'hit_rate': 0.725}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.075, 'both_hit': 31, 'both_miss': 29}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.05, 'both_hit': 27, 'both_miss': 33}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.0, 'both_hit': 28, 'both_miss': 32}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.1, 'both_hit': 45, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.075, 'both_hit': 51, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.000979, 'median_return': -0.001166, 'mean_absolute_return': 0.015037, 'max_adverse_excursion': -0.036103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.001577, 'median_return': -0.004216, 'mean_absolute_return': 0.018272, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.000261, 'median_return': -0.001222, 'mean_absolute_return': 0.021278, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.7375, 'avg_return': 0.012699, 'median_return': 0.020431, 'mean_absolute_return': 0.0338, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.046609, 'median_return': 0.06458, 'mean_absolute_return': 0.069998, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.200358}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00143`, median `-0.003036`, mae `0.014851`
- 5d: sample `20`, hit `0.45`, avg `-0.000944`, median `-0.000371`, mae `0.017177`
- 10d: sample `20`, hit `0.45`, avg `-0.000836`, median `-0.003263`, mae `0.022728`
- 20d: sample `20`, hit `0.6`, avg `0.004185`, median `0.01859`, mae `0.045117`
- 60d: sample `20`, hit `0.8`, avg `0.053574`, median `0.073435`, mae `0.087811`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.001782`, median `-0.000756`, mae `0.015099`
- 5d: sample `60`, hit `0.4333`, avg `-0.001788`, median `-0.005653`, mae `0.018636`
- 10d: sample `60`, hit `0.4833`, avg `0.000627`, median `-0.001083`, mae `0.020795`
- 20d: sample `60`, hit `0.7833`, avg `0.015537`, median `0.020783`, mae `0.030028`
- 60d: sample `60`, hit `0.8`, avg `0.044287`, median `0.060303`, mae `0.06406`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00143`, median `-0.003036`, mae `0.014851`
- 5d: sample `20`, hit `0.45`, avg `-0.000944`, median `-0.000371`, mae `0.017177`
- 10d: sample `20`, hit `0.45`, avg `-0.000836`, median `-0.003263`, mae `0.022728`
- 20d: sample `20`, hit `0.6`, avg `0.004185`, median `0.01859`, mae `0.045117`
- 60d: sample `20`, hit `0.8`, avg `0.053574`, median `0.073435`, mae `0.087811`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004516`, median `0.004243`, mae `0.016437`
- 5d: sample `40`, hit `0.45`, avg `1.1e-05`, median `-0.004216`, mae `0.020511`
- 10d: sample `40`, hit `0.475`, avg `0.00319`, median `-0.001083`, mae `0.019999`
- 20d: sample `40`, hit `0.825`, avg `0.022852`, median `0.028626`, mae `0.030961`
- 60d: sample `40`, hit `0.875`, avg `0.060463`, median `0.069629`, mae `0.067881`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00143`, median `-0.003036`, mae `0.014851`
- 5d: sample `20`, hit `0.45`, avg `-0.000944`, median `-0.000371`, mae `0.017177`
- 10d: sample `20`, hit `0.45`, avg `-0.000836`, median `-0.003263`, mae `0.022728`
- 20d: sample `20`, hit `0.6`, avg `0.004185`, median `0.01859`, mae `0.045117`
- 60d: sample `20`, hit `0.8`, avg `0.053574`, median `0.073435`, mae `0.087811`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.001782`, median `-0.000756`, mae `0.015099`
- 5d: sample `60`, hit `0.4333`, avg `-0.001788`, median `-0.005653`, mae `0.018636`
- 10d: sample `60`, hit `0.4833`, avg `0.000627`, median `-0.001083`, mae `0.020795`
- 20d: sample `60`, hit `0.7833`, avg `0.015537`, median `0.020783`, mae `0.030028`
- 60d: sample `60`, hit `0.8`, avg `0.044287`, median `0.060303`, mae `0.06406`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00143`, median `-0.003036`, mae `0.014851`
- 5d: sample `20`, hit `0.45`, avg `-0.000944`, median `-0.000371`, mae `0.017177`
- 10d: sample `20`, hit `0.45`, avg `-0.000836`, median `-0.003263`, mae `0.022728`
- 20d: sample `20`, hit `0.6`, avg `0.004185`, median `0.01859`, mae `0.045117`
- 60d: sample `20`, hit `0.8`, avg `0.053574`, median `0.073435`, mae `0.087811`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004516`, median `0.004243`, mae `0.016437`
- 5d: sample `40`, hit `0.45`, avg `1.1e-05`, median `-0.004216`, mae `0.020511`
- 10d: sample `40`, hit `0.475`, avg `0.00319`, median `-0.001083`, mae `0.019999`
- 20d: sample `40`, hit `0.825`, avg `0.022852`, median `0.028626`, mae `0.030961`
- 60d: sample `40`, hit `0.875`, avg `0.060463`, median `0.069629`, mae `0.067881`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00143`, median `-0.003036`, mae `0.014851`
- 5d: sample `20`, hit `0.45`, avg `-0.000944`, median `-0.000371`, mae `0.017177`
- 10d: sample `20`, hit `0.45`, avg `-0.000836`, median `-0.003263`, mae `0.022728`
- 20d: sample `20`, hit `0.6`, avg `0.004185`, median `0.01859`, mae `0.045117`
- 60d: sample `20`, hit `0.8`, avg `0.053574`, median `0.073435`, mae `0.087811`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003687`, median `-0.003921`, mae `0.012423`
- 5d: sample `20`, hit `0.4`, avg `-0.005385`, median `-0.009648`, mae `0.014887`
- 10d: sample `20`, hit `0.5`, avg `-0.0045`, median `0.003491`, mae `0.022386`
- 20d: sample `20`, hit `0.7`, avg `0.000907`, median `0.015404`, mae `0.028161`
- 60d: sample `20`, hit `0.65`, avg `0.011937`, median `0.039348`, mae `0.056418`

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
- 3d: sample `40`, hit `0.5`, avg `0.001653`, median `0.001558`, mae `0.014652`
- 5d: sample `40`, hit `0.375`, avg `-0.002949`, median `-0.006048`, mae `0.017048`
- 10d: sample `40`, hit `0.425`, avg `0.001187`, median `-0.00174`, mae `0.01705`
- 20d: sample `40`, hit `0.75`, avg `0.01349`, median `0.020431`, mae `0.034728`
- 60d: sample `40`, hit `0.875`, avg `0.060807`, median `0.073435`, mae `0.08034`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003687`, median `-0.003921`, mae `0.012423`
- 5d: sample `20`, hit `0.4`, avg `-0.005385`, median `-0.009648`, mae `0.014887`
- 10d: sample `20`, hit `0.5`, avg `-0.0045`, median `0.003491`, mae `0.022386`
- 20d: sample `20`, hit `0.7`, avg `0.000907`, median `0.015404`, mae `0.028161`
- 60d: sample `20`, hit `0.65`, avg `0.011937`, median `0.039348`, mae `0.056418`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `0.000979`, median `-0.001166`, mae `0.015037`
- 5d: sample `80`, hit `0.4375`, avg `-0.001577`, median `-0.004216`, mae `0.018272`
- 10d: sample `80`, hit `0.475`, avg `0.000261`, median `-0.001222`, mae `0.021278`
- 20d: sample `80`, hit `0.7375`, avg `0.012699`, median `0.020431`, mae `0.0338`
- 60d: sample `80`, hit `0.8`, avg `0.046609`, median `0.06458`, mae `0.069998`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `0.002534`, median `0.0017`, mae `0.015909`
- 5d: sample `60`, hit `0.45`, avg `-0.000307`, median `-0.003328`, mae `0.0194`
- 10d: sample `60`, hit `0.4667`, avg `0.001848`, median `-0.001222`, mae `0.020909`
- 20d: sample `60`, hit `0.75`, avg `0.01663`, median `0.028065`, mae `0.03568`
- 60d: sample `60`, hit `0.85`, avg `0.058167`, median `0.072277`, mae `0.074524`

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
