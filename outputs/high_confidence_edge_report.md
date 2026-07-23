# High Confidence Edge Report

Generated at: `2026-07-23T14:42:16.179161+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.009177`, median `-0.001591`, mae `0.020087`
- 5d: sample `20`, hit `0.45`, avg `-0.014144`, median `-0.001429`, mae `0.024182`
- 10d: sample `20`, hit `0.35`, avg `-0.004903`, median `-0.006017`, mae `0.019784`
- 20d: sample `20`, hit `0.7`, avg `0.013193`, median `0.026113`, mae `0.042441`
- 60d: sample `20`, hit `0.75`, avg `0.041425`, median `0.059131`, mae `0.080664`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `-0.000739`, median `0.004815`, mae `0.017058`
- 5d: sample `60`, hit `0.5333`, avg `0.001088`, median `0.002451`, mae `0.020521`
- 10d: sample `60`, hit `0.65`, avg `0.007555`, median `0.016791`, mae `0.029881`
- 20d: sample `60`, hit `0.6833`, avg `0.018353`, median `0.026005`, mae `0.045293`
- 60d: sample `60`, hit `0.6167`, avg `0.01953`, median `0.049403`, mae `0.083427`

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
- 3d: sample `8`, hit `0.25`, avg `-0.01363`, median `-0.010033`, mae `0.024795`
- 5d: sample `8`, hit `0.375`, avg `-0.025133`, median `-0.022295`, mae `0.031476`
- 10d: sample `8`, hit `0.125`, avg `-0.011762`, median `-0.007755`, mae `0.014861`
- 20d: sample `8`, hit `0.375`, avg `-0.007317`, median `-0.001666`, mae `0.045176`
- 60d: sample `8`, hit `0.5`, avg `0.011993`, median `0.037425`, mae `0.076436`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.01363`, median `-0.010033`, mae `0.024795`
- 5d: sample `8`, hit `0.375`, avg `-0.025133`, median `-0.022295`, mae `0.031476`
- 10d: sample `8`, hit `0.125`, avg `-0.011762`, median `-0.007755`, mae `0.014861`
- 20d: sample `8`, hit `0.375`, avg `-0.007317`, median `-0.001666`, mae `0.045176`
- 60d: sample `8`, hit `0.5`, avg `0.011993`, median `0.037425`, mae `0.076436`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.009177, 'median_return': -0.001591, 'mean_absolute_return': 0.020087, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.014144, 'median_return': -0.001429, 'mean_absolute_return': 0.024182, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.004903, 'median_return': -0.006017, 'mean_absolute_return': 0.019784, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.013193, 'median_return': 0.026113, 'mean_absolute_return': 0.042441, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.041425, 'median_return': 0.059131, 'mean_absolute_return': 0.080664, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01363, 'median_return': -0.010033, 'mean_absolute_return': 0.024795, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.025133, 'median_return': -0.022295, 'mean_absolute_return': 0.031476, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.010589}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011762, 'median_return': -0.007755, 'mean_absolute_return': 0.014861, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.012396}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007317, 'median_return': -0.001666, 'mean_absolute_return': 0.045176, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.011993, 'median_return': 0.037425, 'mean_absolute_return': 0.076436, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': -0.001651, 'median_return': 0.00372, 'mean_absolute_return': 0.017039, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.000229, 'median_return': 0.002451, 'mean_absolute_return': 0.020321, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.006241, 'median_return': 0.013648, 'mean_absolute_return': 0.028745, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.019772, 'median_return': 0.026806, 'mean_absolute_return': 0.044514, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.026449, 'median_return': 0.057625, 'mean_absolute_return': 0.083436, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.3125}, '60d': {'sample_size': 80, 'hit_rate': 0.35}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': -0.00292, 'median_return': 0.00234, 'mean_absolute_return': 0.01742, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.001351, 'median_return': 0.003005, 'mean_absolute_return': 0.01993, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.052328}, '10d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.0063, 'median_return': 0.006847, 'mean_absolute_return': 0.024311, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.061544}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.021839, 'median_return': 0.02865, 'mean_absolute_return': 0.041722, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.110689}, '60d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.032584, 'median_return': 0.053855, 'mean_absolute_return': 0.076913, 'max_adverse_excursion': -0.177732, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.002636, 'median_return': 0.000707, 'mean_absolute_return': 0.019, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.006825, 'median_return': -0.005124, 'mean_absolute_return': 0.025956, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.001139, 'median_return': 0.016791, 'mean_absolute_return': 0.036493, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002737, 'median_return': 0.017237, 'mean_absolute_return': 0.053155, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002262, 'median_return': 0.029625, 'mean_absolute_return': 0.100206, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.1448}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.004423`, median `0.001199`, mae `0.015781`
- 5d: sample `40`, hit `0.525`, avg `-0.007167`, median `0.001303`, mae `0.018253`
- 10d: sample `40`, hit `0.425`, avg `-0.003938`, median `-0.006017`, mae `0.019156`
- 20d: sample `40`, hit `0.65`, avg `0.011153`, median `0.020226`, mae `0.036858`
- 60d: sample `40`, hit `0.675`, avg `0.028878`, median `0.046407`, mae `0.06451`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.001274`, median `0.005296`, mae `0.019849`
- 5d: sample `40`, hit `0.5`, avg `0.001728`, median `0.002451`, mae `0.02462`
- 10d: sample `40`, hit `0.725`, avg `0.012818`, median `0.022558`, mae `0.035556`
- 20d: sample `40`, hit `0.725`, avg `0.022973`, median `0.045022`, mae `0.052303`
- 60d: sample `40`, hit `0.625`, avg `0.021129`, median `0.06167`, mae `0.100962`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.004423`, median `0.001199`, mae `0.015781`
- 5d: sample `40`, hit `0.525`, avg `-0.007167`, median `0.001303`, mae `0.018253`
- 10d: sample `40`, hit `0.425`, avg `-0.003938`, median `-0.006017`, mae `0.019156`
- 20d: sample `40`, hit `0.65`, avg `0.011153`, median `0.020226`, mae `0.036858`
- 60d: sample `40`, hit `0.675`, avg `0.028878`, median `0.046407`, mae `0.06451`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.004423`, median `0.001199`, mae `0.015781`
- 5d: sample `40`, hit `0.525`, avg `-0.007167`, median `0.001303`, mae `0.018253`
- 10d: sample `40`, hit `0.425`, avg `-0.003938`, median `-0.006017`, mae `0.019156`
- 20d: sample `40`, hit `0.65`, avg `0.011153`, median `0.020226`, mae `0.036858`
- 60d: sample `40`, hit `0.675`, avg `0.028878`, median `0.046407`, mae `0.06451`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.001274`, median `0.005296`, mae `0.019849`
- 5d: sample `40`, hit `0.5`, avg `0.001728`, median `0.002451`, mae `0.02462`
- 10d: sample `40`, hit `0.725`, avg `0.012818`, median `0.022558`, mae `0.035556`
- 20d: sample `40`, hit `0.725`, avg `0.022973`, median `0.045022`, mae `0.052303`
- 60d: sample `40`, hit `0.625`, avg `0.021129`, median `0.06167`, mae `0.100962`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `-0.002849`, median `0.001405`, mae `0.017815`
- 5d: sample `80`, hit `0.5125`, avg `-0.00272`, median `0.001303`, mae `0.021437`
- 10d: sample `80`, hit `0.575`, avg `0.00444`, median `0.006847`, mae `0.027356`
- 20d: sample `80`, hit `0.6875`, avg `0.017063`, median `0.026005`, mae `0.04458`
- 60d: sample `80`, hit `0.65`, avg `0.025003`, median `0.050438`, mae `0.082736`

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
