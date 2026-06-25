# High Confidence Edge Report

Generated at: `2026-06-25T05:18:44.056687+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.003281`, median `0.002889`, mae `0.013453`
- 5d: sample `20`, hit `0.55`, avg `0.004539`, median `0.005327`, mae `0.014942`
- 10d: sample `20`, hit `0.5`, avg `0.002708`, median `0.000242`, mae `0.023798`
- 20d: sample `20`, hit `0.5`, avg `-0.000345`, median `0.004543`, mae `0.027201`
- 60d: sample `20`, hit `0.7`, avg `0.041442`, median `0.064286`, mae `0.064984`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000476`, median `-0.000756`, mae `0.01203`
- 5d: sample `40`, hit `0.425`, avg `-0.004897`, median `-0.004389`, mae `0.014901`
- 10d: sample `40`, hit `0.4`, avg `-0.002877`, median `-0.001932`, mae `0.01619`
- 20d: sample `40`, hit `0.825`, avg `0.012061`, median `0.020751`, mae `0.03116`
- 60d: sample `40`, hit `0.65`, avg `0.026063`, median `0.036062`, mae `0.060403`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.00302`, median `0.008815`, mae `0.017066`
- 5d: sample `20`, hit `0.6`, avg `-0.000608`, median `0.005876`, mae `0.022791`
- 10d: sample `20`, hit `0.6`, avg `0.001181`, median `0.006378`, mae `0.023648`
- 20d: sample `20`, hit `0.55`, avg `2e-06`, median `0.003484`, mae `0.038631`
- 60d: sample `20`, hit `0.5`, avg `0.008653`, median `0.003923`, mae `0.058788`

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
- 3d: sample `8`, hit `0.5`, avg `0.003937`, median `0.003538`, mae `0.014375`
- 5d: sample `8`, hit `0.5`, avg `0.003281`, median `0.008121`, mae `0.017004`
- 10d: sample `8`, hit `0.5`, avg `0.012288`, median `0.020503`, mae `0.029688`
- 20d: sample `8`, hit `0.625`, avg `0.004341`, median `0.01666`, mae `0.038544`
- 60d: sample `8`, hit `0.75`, avg `0.047065`, median `0.069875`, mae `0.06854`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001053`, median `0.002267`, mae `0.006029`
- 5d: sample `8`, hit `0.625`, avg `-0.001165`, median `0.005084`, mae `0.014631`
- 10d: sample `8`, hit `0.5`, avg `-0.003818`, median `0.003491`, mae `0.01682`
- 20d: sample `8`, hit `0.75`, avg `0.000151`, median `0.012291`, mae `0.023028`
- 60d: sample `8`, hit `0.375`, avg `-0.034684`, median `-0.069824`, mae `0.062796`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.003281, 'median_return': 0.002889, 'mean_absolute_return': 0.013453, 'max_adverse_excursion': -0.032103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.004539, 'median_return': 0.005327, 'mean_absolute_return': 0.014942, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.002708, 'median_return': 0.000242, 'mean_absolute_return': 0.023798, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000345, 'median_return': 0.004543, 'mean_absolute_return': 0.027201, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.041442, 'median_return': 0.064286, 'mean_absolute_return': 0.064984, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.139575}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.000476, 'median_return': -0.000756, 'mean_absolute_return': 0.01203, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.02763}, '5d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.004897, 'median_return': -0.004389, 'mean_absolute_return': 0.014901, 'max_adverse_excursion': -0.032974, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.002877, 'median_return': -0.001932, 'mean_absolute_return': 0.01619, 'max_adverse_excursion': -0.047482, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.012061, 'median_return': 0.020751, 'mean_absolute_return': 0.03116, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.026063, 'median_return': 0.036062, 'mean_absolute_return': 0.060403, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.117712}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001053, 'median_return': 0.002267, 'mean_absolute_return': 0.006029, 'max_adverse_excursion': -0.019093, 'max_favorable_excursion': 0.006722}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001165, 'median_return': 0.005084, 'mean_absolute_return': 0.014631, 'max_adverse_excursion': -0.0231, 'max_favorable_excursion': 0.017467}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003818, 'median_return': 0.003491, 'mean_absolute_return': 0.01682, 'max_adverse_excursion': -0.038595, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.000151, 'median_return': 0.012291, 'mean_absolute_return': 0.023028, 'max_adverse_excursion': -0.075882, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.034684, 'median_return': -0.069824, 'mean_absolute_return': 0.062796, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.043741}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.001603, 'median_return': 0.002889, 'mean_absolute_return': 0.014491, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.001499, 'median_return': -0.001324, 'mean_absolute_return': 0.017134, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -9.4e-05, 'median_return': -0.00174, 'mean_absolute_return': 0.020305, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.006589, 'median_return': 0.01666, 'mean_absolute_return': 0.033039, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.032248, 'median_return': 0.046132, 'mean_absolute_return': 0.060961, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 20, 'both_miss': 20}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.05, 'both_hit': 18, 'both_miss': 22}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.125, 'both_hit': 19, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.075, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.075, 'both_hit': 33, 'both_miss': 7}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.000689, 'median_return': 0.002267, 'mean_absolute_return': 0.013709, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.036588}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.003467, 'median_return': -0.001796, 'mean_absolute_return': 0.017531, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.001524, 'median_return': -0.001676, 'mean_absolute_return': 0.018676, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.008042, 'median_return': 0.01775, 'mean_absolute_return': 0.03365, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.020259, 'median_return': 0.031838, 'mean_absolute_return': 0.059865, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.003281, 'median_return': 0.002889, 'mean_absolute_return': 0.013453, 'max_adverse_excursion': -0.032103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.004539, 'median_return': 0.005327, 'mean_absolute_return': 0.014942, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.002708, 'median_return': 0.000242, 'mean_absolute_return': 0.023798, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000345, 'median_return': 0.004543, 'mean_absolute_return': 0.027201, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.041442, 'median_return': 0.064286, 'mean_absolute_return': 0.064984, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.139575}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001301`, median `-0.000722`, mae `0.01109`
- 5d: sample `40`, hit `0.525`, avg `0.000565`, median `0.002786`, mae `0.013761`
- 10d: sample `40`, hit `0.425`, avg `-0.003094`, median `-0.006043`, mae `0.020588`
- 20d: sample `40`, hit `0.6`, avg `-0.002356`, median `0.009812`, mae `0.030039`
- 60d: sample `40`, hit `0.525`, avg `0.011767`, median `0.029945`, mae `0.056872`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.000689`, median `0.002267`, mae `0.013709`
- 5d: sample `60`, hit `0.4833`, avg `-0.003467`, median `-0.001796`, mae `0.017531`
- 10d: sample `60`, hit `0.4667`, avg `-0.001524`, median `-0.001676`, mae `0.018676`
- 20d: sample `60`, hit `0.7333`, avg `0.008042`, median `0.01775`, mae `0.03365`
- 60d: sample `60`, hit `0.6`, avg `0.020259`, median `0.031838`, mae `0.059865`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001301`, median `-0.000722`, mae `0.01109`
- 5d: sample `40`, hit `0.525`, avg `0.000565`, median `0.002786`, mae `0.013761`
- 10d: sample `40`, hit `0.425`, avg `-0.003094`, median `-0.006043`, mae `0.020588`
- 20d: sample `40`, hit `0.6`, avg `-0.002356`, median `0.009812`, mae `0.030039`
- 60d: sample `40`, hit `0.525`, avg `0.011767`, median `0.029945`, mae `0.056872`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000476`, median `-0.000756`, mae `0.01203`
- 5d: sample `40`, hit `0.425`, avg `-0.004897`, median `-0.004389`, mae `0.014901`
- 10d: sample `40`, hit `0.4`, avg `-0.002877`, median `-0.001932`, mae `0.01619`
- 20d: sample `40`, hit `0.825`, avg `0.012061`, median `0.020751`, mae `0.03116`
- 60d: sample `40`, hit `0.65`, avg `0.026063`, median `0.036062`, mae `0.060403`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001373`, median `0.004243`, mae `0.016199`
- 5d: sample `40`, hit `0.475`, avg `-0.003496`, median `-0.003328`, mae `0.020007`
- 10d: sample `40`, hit `0.525`, avg `0.002161`, median `0.004301`, mae `0.019324`
- 20d: sample `40`, hit `0.75`, avg `0.014246`, median `0.026531`, mae `0.034037`
- 60d: sample `40`, hit `0.725`, avg `0.039343`, median `0.062356`, mae `0.065417`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001301`, median `-0.000722`, mae `0.01109`
- 5d: sample `40`, hit `0.525`, avg `0.000565`, median `0.002786`, mae `0.013761`
- 10d: sample `40`, hit `0.425`, avg `-0.003094`, median `-0.006043`, mae `0.020588`
- 20d: sample `40`, hit `0.6`, avg `-0.002356`, median `0.009812`, mae `0.030039`
- 60d: sample `40`, hit `0.525`, avg `0.011767`, median `0.029945`, mae `0.056872`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000273`, median `0.001558`, mae `0.015332`
- 5d: sample `20`, hit `0.35`, avg `-0.006385`, median `-0.007788`, mae `0.017222`
- 10d: sample `20`, hit `0.45`, avg `0.003141`, median `-0.001222`, mae `0.015001`
- 20d: sample `20`, hit `0.95`, avg `0.02849`, median `0.028791`, mae `0.029443`
- 60d: sample `20`, hit `0.95`, avg `0.070033`, median `0.074055`, mae `0.072046`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.00302`, median `0.008815`, mae `0.017066`
- 5d: sample `20`, hit `0.6`, avg `-0.000608`, median `0.005876`, mae `0.022791`
- 10d: sample `20`, hit `0.6`, avg `0.001181`, median `0.006378`, mae `0.023648`
- 20d: sample `20`, hit `0.55`, avg `2e-06`, median `0.003484`, mae `0.038631`
- 60d: sample `20`, hit `0.5`, avg `0.008653`, median `0.003923`, mae `0.058788`

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
- 3d: sample `40`, hit `0.475`, avg `0.001301`, median `-0.000722`, mae `0.01109`
- 5d: sample `40`, hit `0.525`, avg `0.000565`, median `0.002786`, mae `0.013761`
- 10d: sample `40`, hit `0.425`, avg `-0.003094`, median `-0.006043`, mae `0.020588`
- 20d: sample `40`, hit `0.6`, avg `-0.002356`, median `0.009812`, mae `0.030039`
- 60d: sample `40`, hit `0.525`, avg `0.011767`, median `0.029945`, mae `0.056872`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001337`, median `0.002267`, mae `0.013645`
- 5d: sample `80`, hit `0.5`, avg `-0.001466`, median `0.000208`, mae `0.016884`
- 10d: sample `80`, hit `0.475`, avg `-0.000466`, median `-0.001676`, mae `0.019956`
- 20d: sample `80`, hit `0.675`, avg `0.005945`, median `0.015661`, mae `0.032038`
- 60d: sample `80`, hit `0.625`, avg `0.025555`, median `0.036062`, mae `0.061145`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `0.000777`, median `-0.000722`, mae `0.012504`
- 5d: sample `60`, hit `0.4667`, avg `-0.001752`, median `-0.001796`, mae `0.014915`
- 10d: sample `60`, hit `0.4333`, avg `-0.001016`, median `-0.001932`, mae `0.018726`
- 20d: sample `60`, hit `0.7167`, avg `0.007926`, median `0.017608`, mae `0.02984`
- 60d: sample `60`, hit `0.6667`, avg `0.031189`, median `0.046132`, mae `0.06193`

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
