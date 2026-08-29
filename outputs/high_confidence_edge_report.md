# High Confidence Edge Report

Generated at: `2026-08-29T03:21:25.251046+00:00`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.001004`, median `0.001558`, mae `0.01599`
- 5d: sample `80`, hit `0.5125`, avg `-0.001687`, median `0.000415`, mae `0.019302`
- 10d: sample `80`, hit `0.425`, avg `0.000368`, median `-0.007117`, mae `0.025722`
- 20d: sample `80`, hit `0.675`, avg `0.008283`, median `0.016175`, mae `0.034607`
- 60d: sample `80`, hit `0.6875`, avg `0.035709`, median `0.046132`, mae `0.06369`

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
- 3d: sample `8`, hit `0.5`, avg `-0.004637`, median `0.001558`, mae `0.009103`
- 5d: sample `8`, hit `0.375`, avg `-0.006638`, median `-0.012956`, mae `0.01602`
- 10d: sample `8`, hit `0.75`, avg `0.011856`, median `0.020918`, mae `0.021416`
- 20d: sample `8`, hit `1.0`, avg `0.026272`, median `0.031196`, mae `0.026272`
- 60d: sample `8`, hit `0.875`, avg `0.063734`, median `0.092646`, mae `0.068767`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004637`, median `0.001558`, mae `0.009103`
- 5d: sample `8`, hit `0.375`, avg `-0.006638`, median `-0.012956`, mae `0.01602`
- 10d: sample `8`, hit `0.75`, avg `0.011856`, median `0.020918`, mae `0.021416`
- 20d: sample `8`, hit `1.0`, avg `0.026272`, median `0.031196`, mae `0.026272`
- 60d: sample `8`, hit `0.875`, avg `0.063734`, median `0.092646`, mae `0.068767`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.001004, 'median_return': 0.001558, 'mean_absolute_return': 0.01599, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.001687, 'median_return': 0.000415, 'mean_absolute_return': 0.019302, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': 0.000368, 'median_return': -0.007117, 'mean_absolute_return': 0.025722, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.008283, 'median_return': 0.016175, 'mean_absolute_return': 0.034607, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.035709, 'median_return': 0.046132, 'mean_absolute_return': 0.06369, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004637, 'median_return': 0.001558, 'mean_absolute_return': 0.009103, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.006638, 'median_return': -0.012956, 'mean_absolute_return': 0.01602, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011856, 'median_return': 0.020918, 'mean_absolute_return': 0.021416, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.026272, 'median_return': 0.031196, 'mean_absolute_return': 0.026272, 'max_adverse_excursion': 0.000213, 'max_favorable_excursion': 0.044453}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.063734, 'median_return': 0.092646, 'mean_absolute_return': 0.068767, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.105571}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.000601, 'median_return': 0.001824, 'mean_absolute_return': 0.016755, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.001137, 'median_return': 0.000548, 'mean_absolute_return': 0.019666, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.000909, 'median_return': -0.008084, 'mean_absolute_return': 0.0262, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.006284, 'median_return': 0.014522, 'mean_absolute_return': 0.035534, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.032595, 'median_return': 0.032982, 'mean_absolute_return': 0.063126, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.6875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.0, 'both_hit': 32, 'both_miss': 28}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.0, 'both_hit': 31, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.1, 'both_hit': 28, 'both_miss': 32}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.025, 'both_hit': 43, 'both_miss': 17}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.075, 'both_hit': 42, 'both_miss': 18}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.001004, 'median_return': 0.001558, 'mean_absolute_return': 0.01599, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.001687, 'median_return': 0.000415, 'mean_absolute_return': 0.019302, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': 0.000368, 'median_return': -0.007117, 'mean_absolute_return': 0.025722, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.008283, 'median_return': 0.016175, 'mean_absolute_return': 0.034607, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.035709, 'median_return': 0.046132, 'mean_absolute_return': 0.06369, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.000531`, median `0.001558`, mae `0.014499`
- 5d: sample `60`, hit `0.5`, avg `-0.001975`, median `0.000208`, mae `0.018311`
- 10d: sample `60`, hit `0.45`, avg `0.002423`, median `-0.006017`, mae `0.025017`
- 20d: sample `60`, hit `0.6833`, avg `0.009242`, median `0.018139`, mae `0.034377`
- 60d: sample `60`, hit `0.7333`, avg `0.046436`, median `0.059948`, mae `0.070087`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.000531`, median `0.001558`, mae `0.014499`
- 5d: sample `60`, hit `0.5`, avg `-0.001975`, median `0.000208`, mae `0.018311`
- 10d: sample `60`, hit `0.45`, avg `0.002423`, median `-0.006017`, mae `0.025017`
- 20d: sample `60`, hit `0.6833`, avg `0.009242`, median `0.018139`, mae `0.034377`
- 60d: sample `60`, hit `0.7333`, avg `0.046436`, median `0.059948`, mae `0.070087`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003964`, median `-0.001811`, mae `0.015103`
- 5d: sample `20`, hit `0.4`, avg `-0.006574`, median `-0.004989`, mae `0.017131`
- 10d: sample `20`, hit `0.45`, avg `0.003641`, median `-0.001222`, mae `0.020869`
- 20d: sample `20`, hit `0.8`, avg `0.021173`, median `0.031196`, mae `0.035517`
- 60d: sample `20`, hit `0.7`, avg `0.046338`, median `0.081091`, mae `0.076415`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.001004`, median `0.001558`, mae `0.01599`
- 5d: sample `80`, hit `0.5125`, avg `-0.001687`, median `0.000415`, mae `0.019302`
- 10d: sample `80`, hit `0.425`, avg `0.000368`, median `-0.007117`, mae `0.025722`
- 20d: sample `80`, hit `0.675`, avg `0.008283`, median `0.016175`, mae `0.034607`
- 60d: sample `80`, hit `0.6875`, avg `0.035709`, median `0.046132`, mae `0.06369`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.001004`, median `0.001558`, mae `0.01599`
- 5d: sample `80`, hit `0.5125`, avg `-0.001687`, median `0.000415`, mae `0.019302`
- 10d: sample `80`, hit `0.425`, avg `0.000368`, median `-0.007117`, mae `0.025722`
- 20d: sample `80`, hit `0.675`, avg `0.008283`, median `0.016175`, mae `0.034607`
- 60d: sample `80`, hit `0.6875`, avg `0.035709`, median `0.046132`, mae `0.06369`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.001004`, median `0.001558`, mae `0.01599`
- 5d: sample `80`, hit `0.5125`, avg `-0.001687`, median `0.000415`, mae `0.019302`
- 10d: sample `80`, hit `0.425`, avg `0.000368`, median `-0.007117`, mae `0.025722`
- 20d: sample `80`, hit `0.675`, avg `0.008283`, median `0.016175`, mae `0.034607`
- 60d: sample `80`, hit `0.6875`, avg `0.035709`, median `0.046132`, mae `0.06369`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.001004`, median `0.001558`, mae `0.01599`
- 5d: sample `80`, hit `0.5125`, avg `-0.001687`, median `0.000415`, mae `0.019302`
- 10d: sample `80`, hit `0.425`, avg `0.000368`, median `-0.007117`, mae `0.025722`
- 20d: sample `80`, hit `0.675`, avg `0.008283`, median `0.016175`, mae `0.034607`
- 60d: sample `80`, hit `0.6875`, avg `0.035709`, median `0.046132`, mae `0.06369`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.001004`, median `0.001558`, mae `0.01599`
- 5d: sample `80`, hit `0.5125`, avg `-0.001687`, median `0.000415`, mae `0.019302`
- 10d: sample `80`, hit `0.425`, avg `0.000368`, median `-0.007117`, mae `0.025722`
- 20d: sample `80`, hit `0.675`, avg `0.008283`, median `0.016175`, mae `0.034607`
- 60d: sample `80`, hit `0.6875`, avg `0.035709`, median `0.046132`, mae `0.06369`

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
