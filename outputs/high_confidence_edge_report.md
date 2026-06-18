# High Confidence Edge Report

Generated at: `2026-06-18T00:01:45.104344+00:00`

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
- 3d: sample `80`, hit `0.5125`, avg `0.001033`, median `0.001558`, mae `0.014551`
- 5d: sample `80`, hit `0.5`, avg `-0.000965`, median `0.000208`, mae `0.018683`
- 10d: sample `80`, hit `0.475`, avg `0.002485`, median `-0.001222`, mae `0.02177`
- 20d: sample `80`, hit `0.775`, avg `0.015948`, median `0.02086`, mae `0.033243`
- 60d: sample `80`, hit `0.6875`, avg `0.036343`, median `0.054765`, mae `0.068675`

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
- 3d: sample `8`, hit `0.75`, avg `0.007885`, median `0.009928`, mae `0.01344`
- 5d: sample `8`, hit `0.375`, avg `-0.000723`, median `-0.000371`, mae `0.013092`
- 10d: sample `8`, hit `0.125`, avg `-0.006283`, median `-0.010791`, mae `0.022747`
- 20d: sample `8`, hit `0.625`, avg `0.002386`, median `0.017881`, mae `0.036589`
- 60d: sample `8`, hit `0.625`, avg `0.030679`, median `0.050225`, mae `0.056366`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.000126`, median `0.004542`, mae `0.006956`
- 5d: sample `8`, hit `0.625`, avg `-0.000928`, median `0.005084`, mae `0.014868`
- 10d: sample `8`, hit `0.75`, avg `0.00645`, median `0.019466`, mae `0.016518`
- 20d: sample `8`, hit `0.625`, avg `-0.004764`, median `0.011728`, mae `0.023408`
- 60d: sample `8`, hit `0.25`, avg `-0.039334`, median `-0.043292`, mae `0.059315`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.001033, 'median_return': 0.001558, 'mean_absolute_return': 0.014551, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.000965, 'median_return': 0.000208, 'mean_absolute_return': 0.018683, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.002485, 'median_return': -0.001222, 'mean_absolute_return': 0.02177, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.775, 'avg_return': 0.015948, 'median_return': 0.02086, 'mean_absolute_return': 0.033243, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.036343, 'median_return': 0.054765, 'mean_absolute_return': 0.068675, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.178543}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000126, 'median_return': 0.004542, 'mean_absolute_return': 0.006956, 'max_adverse_excursion': -0.019093, 'max_favorable_excursion': 0.011487}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000928, 'median_return': 0.005084, 'mean_absolute_return': 0.014868, 'max_adverse_excursion': -0.0231, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.00645, 'median_return': 0.019466, 'mean_absolute_return': 0.016518, 'max_adverse_excursion': -0.038595, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.004764, 'median_return': 0.011728, 'mean_absolute_return': 0.023408, 'max_adverse_excursion': -0.075882, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.039334, 'median_return': -0.043292, 'mean_absolute_return': 0.059315, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.043741}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.001162, 'median_return': 0.001558, 'mean_absolute_return': 0.015395, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.00097, 'median_return': -0.000371, 'mean_absolute_return': 0.019107, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': 0.002045, 'median_return': -0.001932, 'mean_absolute_return': 0.022353, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.018249, 'median_return': 0.026531, 'mean_absolute_return': 0.034336, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.044752, 'median_return': 0.062356, 'mean_absolute_return': 0.069715, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.178543}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 12, 'both_miss': 8}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.075, 'both_hit': 11, 'both_miss': 9}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.025, 'both_hit': 9, 'both_miss': 11}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.2, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.075, 'both_hit': 16, 'both_miss': 4}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001625, 'median_return': 0.001558, 'mean_absolute_return': 0.017958, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.001594, 'median_return': -0.003328, 'mean_absolute_return': 0.02226, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.004859, 'median_return': 0.001785, 'mean_absolute_return': 0.022588, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.022614, 'median_return': 0.028791, 'mean_absolute_return': 0.035863, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.045265, 'median_return': 0.068046, 'mean_absolute_return': 0.074949, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.000441, 'median_return': 0.0017, 'mean_absolute_return': 0.011143, 'max_adverse_excursion': -0.031519, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.000337, 'median_return': 0.002694, 'mean_absolute_return': 0.015106, 'max_adverse_excursion': -0.058927, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.000112, 'median_return': -0.003263, 'mean_absolute_return': 0.020951, 'max_adverse_excursion': -0.050724, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.009282, 'median_return': 0.01775, 'mean_absolute_return': 0.030624, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.027421, 'median_return': 0.039879, 'mean_absolute_return': 0.0624, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.178543}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.000441`, median `0.0017`, mae `0.011143`
- 5d: sample `40`, hit `0.525`, avg `-0.000337`, median `0.002694`, mae `0.015106`
- 10d: sample `40`, hit `0.45`, avg `0.000112`, median `-0.003263`, mae `0.020951`
- 20d: sample `40`, hit `0.75`, avg `0.009282`, median `0.01775`, mae `0.030624`
- 60d: sample `40`, hit `0.6`, avg `0.027421`, median `0.039879`, mae `0.0624`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.001625`, median `0.001558`, mae `0.017958`
- 5d: sample `40`, hit `0.475`, avg `-0.001594`, median `-0.003328`, mae `0.02226`
- 10d: sample `40`, hit `0.5`, avg `0.004859`, median `0.001785`, mae `0.022588`
- 20d: sample `40`, hit `0.8`, avg `0.022614`, median `0.028791`, mae `0.035863`
- 60d: sample `40`, hit `0.775`, avg `0.045265`, median `0.068046`, mae `0.074949`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.000441`, median `0.0017`, mae `0.011143`
- 5d: sample `40`, hit `0.525`, avg `-0.000337`, median `0.002694`, mae `0.015106`
- 10d: sample `40`, hit `0.45`, avg `0.000112`, median `-0.003263`, mae `0.020951`
- 20d: sample `40`, hit `0.75`, avg `0.009282`, median `0.01775`, mae `0.030624`
- 60d: sample `40`, hit `0.6`, avg `0.027421`, median `0.039879`, mae `0.0624`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002499`, median `0.004243`, mae `0.01703`
- 5d: sample `20`, hit `0.4`, avg `-0.002688`, median `-0.006798`, mae `0.018317`
- 10d: sample `20`, hit `0.5`, avg `0.00809`, median `0.006053`, mae `0.016336`
- 20d: sample `20`, hit `0.9`, avg `0.029847`, median `0.029166`, mae `0.031294`
- 60d: sample `20`, hit `0.9`, avg `0.064389`, median `0.074055`, mae `0.073687`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003683`, median `0.003373`, mae `0.013771`
- 5d: sample `20`, hit `0.55`, avg `0.003307`, median `0.00596`, mae `0.017556`
- 10d: sample `20`, hit `0.45`, avg `0.004858`, median `-0.003263`, mae `0.024722`
- 20d: sample `20`, hit `0.8`, avg `0.018558`, median `0.020431`, mae `0.036032`
- 60d: sample `20`, hit `0.8`, avg `0.064773`, median `0.076199`, mae `0.076024`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.001625`, median `0.001558`, mae `0.017958`
- 5d: sample `40`, hit `0.475`, avg `-0.001594`, median `-0.003328`, mae `0.02226`
- 10d: sample `40`, hit `0.5`, avg `0.004859`, median `0.001785`, mae `0.022588`
- 20d: sample `40`, hit `0.8`, avg `0.022614`, median `0.028791`, mae `0.035863`
- 60d: sample `40`, hit `0.775`, avg `0.045265`, median `0.068046`, mae `0.074949`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.000441`, median `0.0017`, mae `0.011143`
- 5d: sample `40`, hit `0.525`, avg `-0.000337`, median `0.002694`, mae `0.015106`
- 10d: sample `40`, hit `0.45`, avg `0.000112`, median `-0.003263`, mae `0.020951`
- 20d: sample `40`, hit `0.75`, avg `0.009282`, median `0.01775`, mae `0.030624`
- 60d: sample `40`, hit `0.6`, avg `0.027421`, median `0.039879`, mae `0.0624`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002499`, median `0.004243`, mae `0.01703`
- 5d: sample `20`, hit `0.4`, avg `-0.002688`, median `-0.006798`, mae `0.018317`
- 10d: sample `20`, hit `0.5`, avg `0.00809`, median `0.006053`, mae `0.016336`
- 20d: sample `20`, hit `0.9`, avg `0.029847`, median `0.029166`, mae `0.031294`
- 60d: sample `20`, hit `0.9`, avg `0.064389`, median `0.074055`, mae `0.073687`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003683`, median `0.003373`, mae `0.013771`
- 5d: sample `20`, hit `0.55`, avg `0.003307`, median `0.00596`, mae `0.017556`
- 10d: sample `20`, hit `0.45`, avg `0.004858`, median `-0.003263`, mae `0.024722`
- 20d: sample `20`, hit `0.8`, avg `0.018558`, median `0.020431`, mae `0.036032`
- 60d: sample `20`, hit `0.8`, avg `0.064773`, median `0.076199`, mae `0.076024`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000752`, median `0.000453`, mae `0.018887`
- 5d: sample `20`, hit `0.55`, avg `-0.0005`, median `0.006107`, mae `0.026203`
- 10d: sample `20`, hit `0.5`, avg `0.001628`, median `0.001785`, mae `0.028841`
- 20d: sample `20`, hit `0.7`, avg `0.01538`, median `0.028065`, mae `0.040432`
- 60d: sample `20`, hit `0.65`, avg `0.02614`, median `0.061367`, mae `0.076212`

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
- 3d: sample `40`, hit `0.5`, avg `0.000441`, median `0.0017`, mae `0.011143`
- 5d: sample `40`, hit `0.525`, avg `-0.000337`, median `0.002694`, mae `0.015106`
- 10d: sample `40`, hit `0.45`, avg `0.000112`, median `-0.003263`, mae `0.020951`
- 20d: sample `40`, hit `0.75`, avg `0.009282`, median `0.01775`, mae `0.030624`
- 60d: sample `40`, hit `0.6`, avg `0.027421`, median `0.039879`, mae `0.0624`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.001625`, median `0.001558`, mae `0.017958`
- 5d: sample `40`, hit `0.475`, avg `-0.001594`, median `-0.003328`, mae `0.02226`
- 10d: sample `40`, hit `0.5`, avg `0.004859`, median `0.001785`, mae `0.022588`
- 20d: sample `40`, hit `0.8`, avg `0.022614`, median `0.028791`, mae `0.035863`
- 60d: sample `40`, hit `0.775`, avg `0.045265`, median `0.068046`, mae `0.074949`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002499`, median `0.004243`, mae `0.01703`
- 5d: sample `20`, hit `0.4`, avg `-0.002688`, median `-0.006798`, mae `0.018317`
- 10d: sample `20`, hit `0.5`, avg `0.00809`, median `0.006053`, mae `0.016336`
- 20d: sample `20`, hit `0.9`, avg `0.029847`, median `0.029166`, mae `0.031294`
- 60d: sample `20`, hit `0.9`, avg `0.064389`, median `0.074055`, mae `0.073687`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `0.001033`, median `0.001558`, mae `0.014551`
- 5d: sample `80`, hit `0.5`, avg `-0.000965`, median `0.000208`, mae `0.018683`
- 10d: sample `80`, hit `0.475`, avg `0.002485`, median `-0.001222`, mae `0.02177`
- 20d: sample `80`, hit `0.775`, avg `0.015948`, median `0.02086`, mae `0.033243`
- 60d: sample `80`, hit `0.6875`, avg `0.036343`, median `0.054765`, mae `0.068675`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `0.001127`, median `0.0017`, mae `0.013105`
- 5d: sample `60`, hit `0.4833`, avg `-0.00112`, median `-0.000371`, mae `0.016176`
- 10d: sample `60`, hit `0.4667`, avg `0.002771`, median `-0.001676`, mae `0.019413`
- 20d: sample `60`, hit `0.8`, avg `0.016137`, median `0.020431`, mae `0.030847`
- 60d: sample `60`, hit `0.7`, avg `0.039744`, median `0.054522`, mae `0.066162`

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
