# High Confidence Edge Report

Generated at: `2026-07-14T21:30:01.030994+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001147`, median `0.000766`, mae `0.009308`
- 5d: sample `40`, hit `0.625`, avg `0.003582`, median `0.006452`, mae `0.013368`
- 10d: sample `40`, hit `0.525`, avg `-0.001125`, median `0.002362`, mae `0.020143`
- 20d: sample `40`, hit `0.65`, avg `0.004813`, median `0.011728`, mae `0.031359`
- 60d: sample `40`, hit `0.525`, avg `0.000724`, median `0.009227`, mae `0.064146`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.002126`, median `0.00234`, mae `0.014731`
- 5d: sample `40`, hit `0.5`, avg `-0.004696`, median `0.001104`, mae `0.017967`
- 10d: sample `40`, hit `0.425`, avg `-0.003591`, median `-0.004767`, mae `0.022091`
- 20d: sample `40`, hit `0.7`, avg `0.002696`, median `0.013156`, mae `0.033926`
- 60d: sample `40`, hit `0.55`, avg `0.010015`, median `0.012273`, mae `0.059562`

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
- 3d: sample `8`, hit `0.5`, avg `-0.000267`, median `0.000744`, mae `0.005599`
- 5d: sample `8`, hit `0.375`, avg `0.000765`, median `-0.000413`, mae `0.008337`
- 10d: sample `8`, hit `0.5`, avg `-0.007274`, median `0.000242`, mae `0.021514`
- 20d: sample `8`, hit `0.5`, avg `-0.007645`, median `0.005003`, mae `0.036252`
- 60d: sample `8`, hit `0.625`, avg `0.026771`, median `0.074246`, mae `0.084886`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.000267`, median `0.000744`, mae `0.005599`
- 5d: sample `8`, hit `0.375`, avg `0.000765`, median `-0.000413`, mae `0.008337`
- 10d: sample `8`, hit `0.5`, avg `-0.007274`, median `0.000242`, mae `0.021514`
- 20d: sample `8`, hit `0.5`, avg `-0.007645`, median `0.005003`, mae `0.036252`
- 60d: sample `8`, hit `0.625`, avg `0.026771`, median `0.074246`, mae `0.084886`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.001147, 'median_return': 0.000766, 'mean_absolute_return': 0.009308, 'max_adverse_excursion': -0.03466, 'max_favorable_excursion': 0.022489}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.003582, 'median_return': 0.006452, 'mean_absolute_return': 0.013368, 'max_adverse_excursion': -0.047389, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001125, 'median_return': 0.002362, 'mean_absolute_return': 0.020143, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.004813, 'median_return': 0.011728, 'mean_absolute_return': 0.031359, 'max_adverse_excursion': -0.087798, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.000724, 'median_return': 0.009227, 'mean_absolute_return': 0.064146, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.132762}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000267, 'median_return': 0.000744, 'mean_absolute_return': 0.005599, 'max_adverse_excursion': -0.01345, 'max_favorable_excursion': 0.013919}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.000765, 'median_return': -0.000413, 'mean_absolute_return': 0.008337, 'max_adverse_excursion': -0.013784, 'max_favorable_excursion': 0.018358}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.007274, 'median_return': 0.000242, 'mean_absolute_return': 0.021514, 'max_adverse_excursion': -0.036679, 'max_favorable_excursion': 0.039489}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.007645, 'median_return': 0.005003, 'mean_absolute_return': 0.036252, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026771, 'median_return': 0.074246, 'mean_absolute_return': 0.084886, 'max_adverse_excursion': -0.093084, 'max_favorable_excursion': 0.116132}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.000514, 'median_return': 0.00234, 'mean_absolute_return': 0.012733, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': -0.000704, 'median_return': 0.004014, 'mean_absolute_return': 0.016482, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.001812, 'median_return': -0.0004, 'mean_absolute_return': 0.021073, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.005021, 'median_return': 0.013156, 'mean_absolute_return': 0.032242, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.002992, 'median_return': 0.009227, 'mean_absolute_return': 0.059295, 'max_adverse_excursion': -0.146695, 'max_favorable_excursion': 0.132762}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.475}, '60d': {'sample_size': 80, 'hit_rate': 0.4875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.1, 'both_hit': 14, 'both_miss': 6}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.05, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.075, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.125, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 13, 'both_miss': 7}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': -0.000489, 'median_return': 0.001448, 'mean_absolute_return': 0.01202, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': -0.000557, 'median_return': 0.003888, 'mean_absolute_return': 0.015667, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': -0.002358, 'median_return': -0.0004, 'mean_absolute_return': 0.021117, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.003754, 'median_return': 0.011728, 'mean_absolute_return': 0.032643, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.00537, 'median_return': 0.010234, 'mean_absolute_return': 0.061854, 'max_adverse_excursion': -0.146695, 'max_favorable_excursion': 0.132762}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.000334`, median `0.000324`, mae `0.010635`
- 5d: sample `40`, hit `0.575`, avg `-0.001102`, median `0.003888`, mae `0.015923`
- 10d: sample `40`, hit `0.5`, avg `-0.002247`, median `0.002362`, mae `0.021256`
- 20d: sample `40`, hit `0.675`, avg `0.000253`, median `0.01128`, mae `0.029369`
- 60d: sample `40`, hit `0.45`, avg `-0.007797`, median `-0.009954`, mae `0.052693`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.00267`, median `0.000324`, mae `0.01296`
- 5d: sample `60`, hit `0.5333`, avg `-0.003758`, median `0.003005`, mae `0.016734`
- 10d: sample `60`, hit `0.45`, avg `-0.004015`, median `-0.001676`, mae `0.020774`
- 20d: sample `60`, hit `0.6833`, avg `0.00171`, median `0.011728`, mae `0.030919`
- 60d: sample `60`, hit `0.5`, avg `9.9e-05`, median `0.003923`, mae `0.059139`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003758`, median `-0.002654`, mae `0.009417`
- 5d: sample `20`, hit `0.6`, avg `-0.001881`, median `0.003888`, mae `0.014267`
- 10d: sample `20`, hit `0.5`, avg `-0.004861`, median `0.002362`, mae `0.018139`
- 20d: sample `20`, hit `0.65`, avg `-0.000262`, median `0.011728`, mae `0.024905`
- 60d: sample `20`, hit `0.4`, avg `-0.019735`, median `-0.018455`, mae `0.058295`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003758`, median `-0.002654`, mae `0.009417`
- 5d: sample `20`, hit `0.6`, avg `-0.001881`, median `0.003888`, mae `0.014267`
- 10d: sample `20`, hit `0.5`, avg `-0.004861`, median `0.002362`, mae `0.018139`
- 20d: sample `20`, hit `0.65`, avg `-0.000262`, median `0.011728`, mae `0.024905`
- 60d: sample `20`, hit `0.4`, avg `-0.019735`, median `-0.018455`, mae `0.058295`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00309`, median `0.009349`, mae `0.011852`
- 5d: sample `20`, hit `0.55`, avg `-0.000322`, median `0.004655`, mae `0.017578`
- 10d: sample `20`, hit `0.5`, avg `0.000368`, median `0.003262`, mae `0.024373`
- 20d: sample `20`, hit `0.7`, avg `0.000768`, median `0.01128`, mae `0.033834`
- 60d: sample `20`, hit `0.5`, avg `0.004141`, median `0.003923`, mae `0.047091`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.002126`, median `0.00234`, mae `0.014731`
- 5d: sample `40`, hit `0.5`, avg `-0.004696`, median `0.001104`, mae `0.017967`
- 10d: sample `40`, hit `0.425`, avg `-0.003591`, median `-0.004767`, mae `0.022091`
- 20d: sample `40`, hit `0.7`, avg `0.002696`, median `0.013156`, mae `0.033926`
- 60d: sample `40`, hit `0.55`, avg `0.010015`, median `0.012273`, mae `0.059562`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003758`, median `-0.002654`, mae `0.009417`
- 5d: sample `20`, hit `0.6`, avg `-0.001881`, median `0.003888`, mae `0.014267`
- 10d: sample `20`, hit `0.5`, avg `-0.004861`, median `0.002362`, mae `0.018139`
- 20d: sample `20`, hit `0.65`, avg `-0.000262`, median `0.011728`, mae `0.024905`
- 60d: sample `20`, hit `0.4`, avg `-0.019735`, median `-0.018455`, mae `0.058295`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006052`, median `0.006983`, mae `0.009198`
- 5d: sample `20`, hit `0.65`, avg `0.009044`, median `0.01169`, mae `0.012469`
- 10d: sample `20`, hit `0.55`, avg `0.002611`, median `0.008202`, mae `0.022146`
- 20d: sample `20`, hit `0.65`, avg `0.009888`, median `0.026005`, mae `0.037813`
- 60d: sample `20`, hit `0.65`, avg `0.021184`, median `0.045044`, mae `0.069998`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00309`, median `0.009349`, mae `0.011852`
- 5d: sample `20`, hit `0.55`, avg `-0.000322`, median `0.004655`, mae `0.017578`
- 10d: sample `20`, hit `0.5`, avg `0.000368`, median `0.003262`, mae `0.024373`
- 20d: sample `20`, hit `0.7`, avg `0.000768`, median `0.01128`, mae `0.033834`
- 60d: sample `20`, hit `0.5`, avg `0.004141`, median `0.003923`, mae `0.047091`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.002126`, median `0.00234`, mae `0.014731`
- 5d: sample `40`, hit `0.5`, avg `-0.004696`, median `0.001104`, mae `0.017967`
- 10d: sample `40`, hit `0.425`, avg `-0.003591`, median `-0.004767`, mae `0.022091`
- 20d: sample `40`, hit `0.7`, avg `0.002696`, median `0.013156`, mae `0.033926`
- 60d: sample `40`, hit `0.55`, avg `0.010015`, median `0.012273`, mae `0.059562`

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
- 3d: sample `20`, hit `0.4`, avg `-0.003758`, median `-0.002654`, mae `0.009417`
- 5d: sample `20`, hit `0.6`, avg `-0.001881`, median `0.003888`, mae `0.014267`
- 10d: sample `20`, hit `0.5`, avg `-0.004861`, median `0.002362`, mae `0.018139`
- 20d: sample `20`, hit `0.65`, avg `-0.000262`, median `0.011728`, mae `0.024905`
- 60d: sample `20`, hit `0.4`, avg `-0.019735`, median `-0.018455`, mae `0.058295`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.002126`, median `0.00234`, mae `0.014731`
- 5d: sample `40`, hit `0.5`, avg `-0.004696`, median `0.001104`, mae `0.017967`
- 10d: sample `40`, hit `0.425`, avg `-0.003591`, median `-0.004767`, mae `0.022091`
- 20d: sample `40`, hit `0.7`, avg `0.002696`, median `0.013156`, mae `0.033926`
- 60d: sample `40`, hit `0.55`, avg `0.010015`, median `0.012273`, mae `0.059562`

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
