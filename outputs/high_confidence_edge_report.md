# High Confidence Edge Report

Generated at: `2026-08-14T21:55:01.132633+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `20`
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
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `2`
- 3d: sample `2`, hit `1.0`, avg `0.015904`, median `0.022579`, mae `0.015904`
- 5d: sample `2`, hit `1.0`, avg `0.015529`, median `0.017206`, mae `0.015529`
- 10d: sample `2`, hit `1.0`, avg `0.023382`, median `0.024811`, mae `0.023382`
- 20d: sample `2`, hit `0.5`, avg `0.027687`, median `0.062955`, mae `0.035268`
- 60d: sample `2`, hit `0.5`, avg `0.024401`, median `0.087104`, mae `0.062703`

### confidence_score top 10%
- sample_size: `2`
- 3d: sample `2`, hit `1.0`, avg `0.015904`, median `0.022579`, mae `0.015904`
- 5d: sample `2`, hit `1.0`, avg `0.015529`, median `0.017206`, mae `0.015529`
- 10d: sample `2`, hit `1.0`, avg `0.023382`, median `0.024811`, mae `0.023382`
- 20d: sample `2`, hit `0.5`, avg `0.027687`, median `0.062955`, mae `0.035268`
- 60d: sample `2`, hit `0.5`, avg `0.024401`, median `0.087104`, mae `0.062703`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -1.1e-05, 'median_return': 0.001448, 'mean_absolute_return': 0.015562, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.002265, 'median_return': 0.004014, 'mean_absolute_return': 0.016652, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004346, 'median_return': 0.010691, 'mean_absolute_return': 0.023037, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.012746, 'median_return': 0.024743, 'mean_absolute_return': 0.040849, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.01137, 'median_return': 0.030553, 'mean_absolute_return': 0.069144, 'max_adverse_excursion': -0.152845, 'max_favorable_excursion': 0.099719}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 2, 'by_horizon': {'3d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.015904, 'median_return': 0.022579, 'mean_absolute_return': 0.015904, 'max_adverse_excursion': 0.009229, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.015529, 'median_return': 0.017206, 'mean_absolute_return': 0.015529, 'max_adverse_excursion': 0.013852, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.023382, 'median_return': 0.024811, 'mean_absolute_return': 0.023382, 'max_adverse_excursion': 0.021953, 'max_favorable_excursion': 0.024811}, '20d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': 0.027687, 'median_return': 0.062955, 'mean_absolute_return': 0.035268, 'max_adverse_excursion': -0.007581, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': 0.024401, 'median_return': 0.087104, 'mean_absolute_return': 0.062703, 'max_adverse_excursion': -0.038302, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 18, 'by_horizon': {'3d': {'sample_size': 18, 'hit_rate': 0.4444, 'avg_return': -0.001779, 'median_return': -0.003214, 'mean_absolute_return': 0.015524, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 18, 'hit_rate': 0.4444, 'avg_return': 0.000791, 'median_return': -0.002525, 'mean_absolute_return': 0.016777, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 18, 'hit_rate': 0.6111, 'avg_return': 0.002231, 'median_return': 0.004187, 'mean_absolute_return': 0.022998, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 18, 'hit_rate': 0.7778, 'avg_return': 0.011086, 'median_return': 0.024743, 'mean_absolute_return': 0.041469, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 18, 'hit_rate': 0.5, 'avg_return': 0.009922, 'median_return': 0.030553, 'mean_absolute_return': 0.069859, 'max_adverse_excursion': -0.152845, 'max_favorable_excursion': 0.099719}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 20, 'hit_rate': 0.5}, '5d': {'sample_size': 20, 'hit_rate': 0.5}, '10d': {'sample_size': 20, 'hit_rate': 0.65}, '20d': {'sample_size': 20, 'hit_rate': 0.75}, '60d': {'sample_size': 20, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 20, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 10, 'both_miss': 10}, '5d': {'sample_size': 20, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 10, 'both_miss': 10}, '10d': {'sample_size': 20, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 13, 'both_miss': 7}, '20d': {'sample_size': 20, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': 0.0, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 20, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 10, 'both_miss': 10}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -1.1e-05, 'median_return': 0.001448, 'mean_absolute_return': 0.015562, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.002265, 'median_return': 0.004014, 'mean_absolute_return': 0.016652, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004346, 'median_return': 0.010691, 'mean_absolute_return': 0.023037, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.012746, 'median_return': 0.024743, 'mean_absolute_return': 0.040849, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.01137, 'median_return': 0.030553, 'mean_absolute_return': 0.069144, 'max_adverse_excursion': -0.152845, 'max_favorable_excursion': 0.099719}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

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
