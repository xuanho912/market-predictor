# High Confidence Edge Report

Generated at: `2026-08-20T04:22:10.477576+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `40`
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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001546`, median `0.001534`, mae `0.012012`
- 5d: sample `40`, hit `0.65`, avg `0.005035`, median `0.005319`, mae `0.014053`
- 10d: sample `40`, hit `0.65`, avg `0.003137`, median `0.010495`, mae `0.020628`
- 20d: sample `40`, hit `0.725`, avg `0.010455`, median `0.013178`, mae `0.030912`
- 60d: sample `40`, hit `0.5`, avg `0.014207`, median `0.004698`, mae `0.057023`

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
- sample_size: `4`
- 3d: sample `4`, hit `0.75`, avg `0.006853`, median `0.009229`, mae `0.009775`
- 5d: sample `4`, hit `1.0`, avg `0.010098`, median `0.013852`, mae `0.010098`
- 10d: sample `4`, hit `1.0`, avg `0.02093`, median `0.024811`, mae `0.02093`
- 20d: sample `4`, hit `0.5`, avg `0.012375`, median `0.009259`, mae `0.023733`
- 60d: sample `4`, hit `0.25`, avg `-0.00754`, median `-0.033557`, mae `0.051091`

### confidence_score top 10%
- sample_size: `4`
- 3d: sample `4`, hit `0.75`, avg `0.006853`, median `0.009229`, mae `0.009775`
- 5d: sample `4`, hit `1.0`, avg `0.010098`, median `0.013852`, mae `0.010098`
- 10d: sample `4`, hit `1.0`, avg `0.02093`, median `0.024811`, mae `0.02093`
- 20d: sample `4`, hit `0.5`, avg `0.012375`, median `0.009259`, mae `0.023733`
- 60d: sample `4`, hit `0.25`, avg `-0.00754`, median `-0.033557`, mae `0.051091`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001546, 'median_return': 0.001534, 'mean_absolute_return': 0.012012, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.005035, 'median_return': 0.005319, 'mean_absolute_return': 0.014053, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.003137, 'median_return': 0.010495, 'mean_absolute_return': 0.020628, 'max_adverse_excursion': -0.078064, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.010455, 'median_return': 0.013178, 'mean_absolute_return': 0.030912, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.014207, 'median_return': 0.004698, 'mean_absolute_return': 0.057023, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.102896}}}, 'confidence_top_10': {'sample_size': 4, 'by_horizon': {'3d': {'sample_size': 4, 'hit_rate': 0.75, 'avg_return': 0.006853, 'median_return': 0.009229, 'mean_absolute_return': 0.009775, 'max_adverse_excursion': -0.005844, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 4, 'hit_rate': 1.0, 'avg_return': 0.010098, 'median_return': 0.013852, 'mean_absolute_return': 0.010098, 'max_adverse_excursion': 0.004014, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 4, 'hit_rate': 1.0, 'avg_return': 0.02093, 'median_return': 0.024811, 'mean_absolute_return': 0.02093, 'max_adverse_excursion': 0.011426, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 4, 'hit_rate': 0.5, 'avg_return': 0.012375, 'median_return': 0.009259, 'mean_absolute_return': 0.023733, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 4, 'hit_rate': 0.25, 'avg_return': -0.00754, 'median_return': -0.033557, 'mean_absolute_return': 0.051091, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 36, 'by_horizon': {'3d': {'sample_size': 36, 'hit_rate': 0.5278, 'avg_return': 0.000957, 'median_return': 0.001534, 'mean_absolute_return': 0.012261, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 36, 'hit_rate': 0.6111, 'avg_return': 0.004473, 'median_return': 0.004606, 'mean_absolute_return': 0.014492, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 36, 'hit_rate': 0.6111, 'avg_return': 0.001159, 'median_return': 0.007467, 'mean_absolute_return': 0.020595, 'max_adverse_excursion': -0.078064, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 36, 'hit_rate': 0.75, 'avg_return': 0.010242, 'median_return': 0.019193, 'mean_absolute_return': 0.03171, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 36, 'hit_rate': 0.5278, 'avg_return': 0.016623, 'median_return': 0.023755, 'mean_absolute_return': 0.057682, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.102896}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 40, 'hit_rate': 0.55}, '5d': {'sample_size': 40, 'hit_rate': 0.65}, '10d': {'sample_size': 40, 'hit_rate': 0.65}, '20d': {'sample_size': 40, 'hit_rate': 0.725}, '60d': {'sample_size': 40, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 40, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 22, 'both_miss': 18}, '5d': {'sample_size': 40, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 26, 'both_miss': 14}, '10d': {'sample_size': 40, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 26, 'both_miss': 14}, '20d': {'sample_size': 40, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': 0.0, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 40, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 20, 'both_miss': 20}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001527, 'median_return': 0.009229, 'mean_absolute_return': 0.015883, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.004948, 'median_return': 0.005319, 'mean_absolute_return': 0.016237, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.005827, 'median_return': 0.011426, 'mean_absolute_return': 0.023032, 'max_adverse_excursion': -0.078064, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.022569, 'median_return': 0.027502, 'mean_absolute_return': 0.036432, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.028804, 'median_return': 0.046132, 'mean_absolute_return': 0.061999, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.102896}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001566, 'median_return': 0.001534, 'mean_absolute_return': 0.008141, 'max_adverse_excursion': -0.014409, 'max_favorable_excursion': 0.019264}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.005123, 'median_return': 0.006452, 'mean_absolute_return': 0.011868, 'max_adverse_excursion': -0.018642, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000446, 'median_return': 0.009675, 'mean_absolute_return': 0.018225, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.027042}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': -0.001659, 'median_return': 0.007988, 'mean_absolute_return': 0.025392, 'max_adverse_excursion': -0.092026, 'max_favorable_excursion': 0.035222}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00039, 'median_return': -0.01711, 'mean_absolute_return': 0.052048, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.096597}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001546`, median `0.001534`, mae `0.012012`
- 5d: sample `40`, hit `0.65`, avg `0.005035`, median `0.005319`, mae `0.014053`
- 10d: sample `40`, hit `0.65`, avg `0.003137`, median `0.010495`, mae `0.020628`
- 20d: sample `40`, hit `0.725`, avg `0.010455`, median `0.013178`, mae `0.030912`
- 60d: sample `40`, hit `0.5`, avg `0.014207`, median `0.004698`, mae `0.057023`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001527`, median `0.009229`, mae `0.015883`
- 5d: sample `20`, hit `0.55`, avg `0.004948`, median `0.005319`, mae `0.016237`
- 10d: sample `20`, hit `0.7`, avg `0.005827`, median `0.011426`, mae `0.023032`
- 20d: sample `20`, hit `0.8`, avg `0.022569`, median `0.027502`, mae `0.036432`
- 60d: sample `20`, hit `0.55`, avg `0.028804`, median `0.046132`, mae `0.061999`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001546`, median `0.001534`, mae `0.012012`
- 5d: sample `40`, hit `0.65`, avg `0.005035`, median `0.005319`, mae `0.014053`
- 10d: sample `40`, hit `0.65`, avg `0.003137`, median `0.010495`, mae `0.020628`
- 20d: sample `40`, hit `0.725`, avg `0.010455`, median `0.013178`, mae `0.030912`
- 60d: sample `40`, hit `0.5`, avg `0.014207`, median `0.004698`, mae `0.057023`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001527`, median `0.009229`, mae `0.015883`
- 5d: sample `20`, hit `0.55`, avg `0.004948`, median `0.005319`, mae `0.016237`
- 10d: sample `20`, hit `0.7`, avg `0.005827`, median `0.011426`, mae `0.023032`
- 20d: sample `20`, hit `0.8`, avg `0.022569`, median `0.027502`, mae `0.036432`
- 60d: sample `20`, hit `0.55`, avg `0.028804`, median `0.046132`, mae `0.061999`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001546`, median `0.001534`, mae `0.012012`
- 5d: sample `40`, hit `0.65`, avg `0.005035`, median `0.005319`, mae `0.014053`
- 10d: sample `40`, hit `0.65`, avg `0.003137`, median `0.010495`, mae `0.020628`
- 20d: sample `40`, hit `0.725`, avg `0.010455`, median `0.013178`, mae `0.030912`
- 60d: sample `40`, hit `0.5`, avg `0.014207`, median `0.004698`, mae `0.057023`

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
- 3d: sample `40`, hit `0.55`, avg `0.001546`, median `0.001534`, mae `0.012012`
- 5d: sample `40`, hit `0.65`, avg `0.005035`, median `0.005319`, mae `0.014053`
- 10d: sample `40`, hit `0.65`, avg `0.003137`, median `0.010495`, mae `0.020628`
- 20d: sample `40`, hit `0.725`, avg `0.010455`, median `0.013178`, mae `0.030912`
- 60d: sample `40`, hit `0.5`, avg `0.014207`, median `0.004698`, mae `0.057023`

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
- 3d: sample `40`, hit `0.55`, avg `0.001546`, median `0.001534`, mae `0.012012`
- 5d: sample `40`, hit `0.65`, avg `0.005035`, median `0.005319`, mae `0.014053`
- 10d: sample `40`, hit `0.65`, avg `0.003137`, median `0.010495`, mae `0.020628`
- 20d: sample `40`, hit `0.725`, avg `0.010455`, median `0.013178`, mae `0.030912`
- 60d: sample `40`, hit `0.5`, avg `0.014207`, median `0.004698`, mae `0.057023`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001546`, median `0.001534`, mae `0.012012`
- 5d: sample `40`, hit `0.65`, avg `0.005035`, median `0.005319`, mae `0.014053`
- 10d: sample `40`, hit `0.65`, avg `0.003137`, median `0.010495`, mae `0.020628`
- 20d: sample `40`, hit `0.725`, avg `0.010455`, median `0.013178`, mae `0.030912`
- 60d: sample `40`, hit `0.5`, avg `0.014207`, median `0.004698`, mae `0.057023`

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
