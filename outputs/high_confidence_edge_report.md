# High Confidence Edge Report

Generated at: `2026-06-19T00:14:28.630699+00:00`

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
- 3d: sample `80`, hit `0.55`, avg `0.001938`, median `0.003538`, mae `0.01339`
- 5d: sample `80`, hit `0.525`, avg `0.000279`, median `0.002616`, mae `0.016981`
- 10d: sample `80`, hit `0.475`, avg `0.000578`, median `-0.001676`, mae `0.021394`
- 20d: sample `80`, hit `0.65`, avg `0.004095`, median `0.016175`, mae `0.033188`
- 60d: sample `80`, hit `0.625`, avg `0.023666`, median `0.032982`, mae `0.06134`

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
- 3d: sample `8`, hit `0.375`, avg `-0.007525`, median `-0.001811`, mae `0.013188`
- 5d: sample `8`, hit `0.125`, avg `-0.014321`, median `-0.013034`, mae `0.020317`
- 10d: sample `8`, hit `0.625`, avg `0.007866`, median `0.0076`, mae `0.014529`
- 20d: sample `8`, hit `1.0`, avg `0.026213`, median `0.029166`, mae `0.026213`
- 60d: sample `8`, hit `0.875`, avg `0.060567`, median `0.081091`, mae `0.0656`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.000814`, median `-0.001166`, mae `0.006502`
- 5d: sample `8`, hit `0.5`, avg `-0.00151`, median `0.003714`, mae `0.01362`
- 10d: sample `8`, hit `0.75`, avg `0.007896`, median `0.009675`, mae `0.01245`
- 20d: sample `8`, hit `0.875`, avg `0.011749`, median `0.012291`, mae `0.015566`
- 60d: sample `8`, hit `0.25`, avg `-0.036088`, median `-0.03635`, mae `0.059294`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.001938, 'median_return': 0.003538, 'mean_absolute_return': 0.01339, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.000279, 'median_return': 0.002616, 'mean_absolute_return': 0.016981, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.000578, 'median_return': -0.001676, 'mean_absolute_return': 0.021394, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.004095, 'median_return': 0.016175, 'mean_absolute_return': 0.033188, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.023666, 'median_return': 0.032982, 'mean_absolute_return': 0.06134, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.000814, 'median_return': -0.001166, 'mean_absolute_return': 0.006502, 'max_adverse_excursion': -0.013293, 'max_favorable_excursion': 0.011487}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.00151, 'median_return': 0.003714, 'mean_absolute_return': 0.01362, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007896, 'median_return': 0.009675, 'mean_absolute_return': 0.01245, 'max_adverse_excursion': -0.016537, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.011749, 'median_return': 0.012291, 'mean_absolute_return': 0.015566, 'max_adverse_excursion': -0.015267, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.036088, 'median_return': -0.03635, 'mean_absolute_return': 0.059294, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.049084}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002244, 'median_return': 0.003924, 'mean_absolute_return': 0.014155, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.000478, 'median_return': 0.002616, 'mean_absolute_return': 0.017354, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.000235, 'median_return': -0.002528, 'mean_absolute_return': 0.022388, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.003244, 'median_return': 0.017608, 'mean_absolute_return': 0.035146, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.030305, 'median_return': 0.036183, 'mean_absolute_return': 0.061567, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.425}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 10, 'both_miss': 10}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.125, 'both_hit': 9, 'both_miss': 11}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.1, 'both_hit': 8, 'both_miss': 12}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.275, 'both_hit': 11, 'both_miss': 9}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.15, 'both_hit': 14, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001716, 'median_return': 0.004243, 'mean_absolute_return': 0.015865, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.036588}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001199, 'median_return': 0.001259, 'mean_absolute_return': 0.019689, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001831, 'median_return': 0.005417, 'mean_absolute_return': 0.022174, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009262, 'median_return': 0.026531, 'mean_absolute_return': 0.038725, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.036348, 'median_return': 0.054522, 'mean_absolute_return': 0.066969, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.002161, 'median_return': 0.002889, 'mean_absolute_return': 0.010915, 'max_adverse_excursion': -0.032103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001757, 'median_return': 0.002694, 'mean_absolute_return': 0.014273, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.000675, 'median_return': -0.004918, 'mean_absolute_return': 0.020615, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': -0.001072, 'median_return': 0.005428, 'mean_absolute_return': 0.02765, 'max_adverse_excursion': -0.092026, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.010983, 'median_return': 0.029945, 'mean_absolute_return': 0.055712, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.139575}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002161`, median `0.002889`, mae `0.010915`
- 5d: sample `40`, hit `0.525`, avg `0.001757`, median `0.002694`, mae `0.014273`
- 10d: sample `40`, hit `0.425`, avg `-0.000675`, median `-0.004918`, mae `0.020615`
- 20d: sample `40`, hit `0.6`, avg `-0.001072`, median `0.005428`, mae `0.02765`
- 60d: sample `40`, hit `0.55`, avg `0.010983`, median `0.029945`, mae `0.055712`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001716`, median `0.004243`, mae `0.015865`
- 5d: sample `40`, hit `0.525`, avg `-0.001199`, median `0.001259`, mae `0.019689`
- 10d: sample `40`, hit `0.525`, avg `0.001831`, median `0.005417`, mae `0.022174`
- 20d: sample `40`, hit `0.7`, avg `0.009262`, median `0.026531`, mae `0.038725`
- 60d: sample `40`, hit `0.7`, avg `0.036348`, median `0.054522`, mae `0.066969`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002161`, median `0.002889`, mae `0.010915`
- 5d: sample `40`, hit `0.525`, avg `0.001757`, median `0.002694`, mae `0.014273`
- 10d: sample `40`, hit `0.425`, avg `-0.000675`, median `-0.004918`, mae `0.020615`
- 20d: sample `40`, hit `0.6`, avg `-0.001072`, median `0.005428`, mae `0.02765`
- 60d: sample `40`, hit `0.55`, avg `0.010983`, median `0.029945`, mae `0.055712`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001392`, median `0.001558`, mae `0.016451`
- 5d: sample `20`, hit `0.35`, avg `-0.006396`, median `-0.007788`, mae `0.017234`
- 10d: sample `20`, hit `0.45`, avg `0.003574`, median `-0.001222`, mae `0.015435`
- 20d: sample `20`, hit `0.9`, avg `0.027892`, median `0.028791`, mae `0.029339`
- 60d: sample `20`, hit `0.9`, avg `0.062746`, median `0.074055`, mae `0.072044`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.002552`, median `0.002889`, mae `0.012653`
- 5d: sample `20`, hit `0.45`, avg `0.002535`, median `-0.000371`, mae `0.014195`
- 10d: sample `20`, hit `0.4`, avg `0.001001`, median `-0.004946`, mae `0.022911`
- 20d: sample `20`, hit `0.55`, avg `0.001215`, median `0.004543`, mae `0.0268`
- 60d: sample `20`, hit `0.7`, avg `0.037461`, median `0.054765`, mae `0.061003`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001392`, median `0.001558`, mae `0.016451`
- 5d: sample `20`, hit `0.35`, avg `-0.006396`, median `-0.007788`, mae `0.017234`
- 10d: sample `20`, hit `0.45`, avg `0.003574`, median `-0.001222`, mae `0.015435`
- 20d: sample `20`, hit `0.9`, avg `0.027892`, median `0.028791`, mae `0.029339`
- 60d: sample `20`, hit `0.9`, avg `0.062746`, median `0.074055`, mae `0.072044`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002161`, median `0.002889`, mae `0.010915`
- 5d: sample `40`, hit `0.525`, avg `0.001757`, median `0.002694`, mae `0.014273`
- 10d: sample `40`, hit `0.425`, avg `-0.000675`, median `-0.004918`, mae `0.020615`
- 20d: sample `40`, hit `0.6`, avg `-0.001072`, median `0.005428`, mae `0.02765`
- 60d: sample `40`, hit `0.55`, avg `0.010983`, median `0.029945`, mae `0.055712`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001392`, median `0.001558`, mae `0.016451`
- 5d: sample `20`, hit `0.35`, avg `-0.006396`, median `-0.007788`, mae `0.017234`
- 10d: sample `20`, hit `0.45`, avg `0.003574`, median `-0.001222`, mae `0.015435`
- 20d: sample `20`, hit `0.9`, avg `0.027892`, median `0.028791`, mae `0.029339`
- 60d: sample `20`, hit `0.9`, avg `0.062746`, median `0.074055`, mae `0.072044`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.002552`, median `0.002889`, mae `0.012653`
- 5d: sample `20`, hit `0.45`, avg `0.002535`, median `-0.000371`, mae `0.014195`
- 10d: sample `20`, hit `0.4`, avg `0.001001`, median `-0.004946`, mae `0.022911`
- 20d: sample `20`, hit `0.55`, avg `0.001215`, median `0.004543`, mae `0.0268`
- 60d: sample `20`, hit `0.7`, avg `0.037461`, median `0.054765`, mae `0.061003`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004824`, median `0.008815`, mae `0.015278`
- 5d: sample `20`, hit `0.7`, avg `0.003998`, median `0.012139`, mae `0.022144`
- 10d: sample `20`, hit `0.6`, avg `8.9e-05`, median `0.01246`, mae `0.028913`
- 20d: sample `20`, hit `0.5`, avg `-0.009369`, median `0.002867`, mae `0.048112`
- 60d: sample `20`, hit `0.5`, avg `0.009951`, median `0.009335`, mae `0.061894`

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
- 3d: sample `40`, hit `0.525`, avg `0.002161`, median `0.002889`, mae `0.010915`
- 5d: sample `40`, hit `0.525`, avg `0.001757`, median `0.002694`, mae `0.014273`
- 10d: sample `40`, hit `0.425`, avg `-0.000675`, median `-0.004918`, mae `0.020615`
- 20d: sample `40`, hit `0.6`, avg `-0.001072`, median `0.005428`, mae `0.02765`
- 60d: sample `40`, hit `0.55`, avg `0.010983`, median `0.029945`, mae `0.055712`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001716`, median `0.004243`, mae `0.015865`
- 5d: sample `40`, hit `0.525`, avg `-0.001199`, median `0.001259`, mae `0.019689`
- 10d: sample `40`, hit `0.525`, avg `0.001831`, median `0.005417`, mae `0.022174`
- 20d: sample `40`, hit `0.7`, avg `0.009262`, median `0.026531`, mae `0.038725`
- 60d: sample `40`, hit `0.7`, avg `0.036348`, median `0.054522`, mae `0.066969`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001392`, median `0.001558`, mae `0.016451`
- 5d: sample `20`, hit `0.35`, avg `-0.006396`, median `-0.007788`, mae `0.017234`
- 10d: sample `20`, hit `0.45`, avg `0.003574`, median `-0.001222`, mae `0.015435`
- 20d: sample `20`, hit `0.9`, avg `0.027892`, median `0.028791`, mae `0.029339`
- 60d: sample `20`, hit `0.9`, avg `0.062746`, median `0.074055`, mae `0.072044`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.001938`, median `0.003538`, mae `0.01339`
- 5d: sample `80`, hit `0.525`, avg `0.000279`, median `0.002616`, mae `0.016981`
- 10d: sample `80`, hit `0.475`, avg `0.000578`, median `-0.001676`, mae `0.021394`
- 20d: sample `80`, hit `0.65`, avg `0.004095`, median `0.016175`, mae `0.033188`
- 60d: sample `80`, hit `0.625`, avg `0.023666`, median `0.032982`, mae `0.06134`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `0.000976`, median `0.002267`, mae `0.01276`
- 5d: sample `60`, hit `0.4667`, avg `-0.000961`, median `-0.001324`, mae `0.01526`
- 10d: sample `60`, hit `0.4333`, avg `0.000741`, median `-0.001932`, mae `0.018888`
- 20d: sample `60`, hit `0.7`, avg `0.008583`, median `0.017608`, mae `0.028213`
- 60d: sample `60`, hit `0.6667`, avg `0.028238`, median `0.043741`, mae `0.061156`

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
