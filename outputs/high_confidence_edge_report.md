# High Confidence Edge Report

Generated at: `2026-06-23T05:17:12.975591+00:00`

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
- 3d: sample `40`, hit `0.575`, avg `0.001373`, median `0.004243`, mae `0.016199`
- 5d: sample `40`, hit `0.475`, avg `-0.003496`, median `-0.003328`, mae `0.020007`
- 10d: sample `40`, hit `0.525`, avg `0.002161`, median `0.004301`, mae `0.019324`
- 20d: sample `40`, hit `0.75`, avg `0.014246`, median `0.026531`, mae `0.034037`
- 60d: sample `40`, hit `0.725`, avg `0.039343`, median `0.062356`, mae `0.065417`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000679`, median `-0.001166`, mae `0.008728`
- 5d: sample `20`, hit `0.5`, avg `-0.003409`, median `0.002786`, mae `0.01258`
- 10d: sample `20`, hit `0.35`, avg `-0.008895`, median `-0.007117`, mae `0.017379`
- 20d: sample `20`, hit `0.7`, avg `-0.004368`, median `0.01251`, mae `0.032877`
- 60d: sample `20`, hit `0.35`, avg `-0.017907`, median `-0.006198`, mae `0.048761`

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
- 3d: sample `8`, hit `0.375`, avg `-0.006049`, median `-0.001811`, mae `0.014664`
- 5d: sample `8`, hit `0.125`, avg `-0.014197`, median `-0.013034`, mae `0.020193`
- 10d: sample `8`, hit `0.75`, avg `0.009468`, median `0.0076`, mae `0.014441`
- 20d: sample `8`, hit `1.0`, avg `0.027297`, median `0.029166`, mae `0.027297`
- 60d: sample `8`, hit `0.875`, avg `0.065314`, median `0.092646`, mae `0.070346`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.003937`, median `0.003538`, mae `0.014375`
- 5d: sample `8`, hit `0.5`, avg `0.003281`, median `0.008121`, mae `0.017004`
- 10d: sample `8`, hit `0.5`, avg `0.012288`, median `0.020503`, mae `0.029688`
- 20d: sample `8`, hit `0.625`, avg `0.004341`, median `0.01666`, mae `0.038544`
- 60d: sample `8`, hit `0.75`, avg `0.047065`, median `0.069875`, mae `0.06854`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.003281, 'median_return': 0.002889, 'mean_absolute_return': 0.013453, 'max_adverse_excursion': -0.032103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.004539, 'median_return': 0.005327, 'mean_absolute_return': 0.014942, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.002708, 'median_return': 0.000242, 'mean_absolute_return': 0.023798, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000345, 'median_return': 0.004543, 'mean_absolute_return': 0.027201, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.041442, 'median_return': 0.064286, 'mean_absolute_return': 0.064984, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.139575}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001373, 'median_return': 0.004243, 'mean_absolute_return': 0.016199, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.036588}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.003496, 'median_return': -0.003328, 'mean_absolute_return': 0.020007, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.002161, 'median_return': 0.004301, 'mean_absolute_return': 0.019324, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.014246, 'median_return': 0.026531, 'mean_absolute_return': 0.034037, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.039343, 'median_return': 0.062356, 'mean_absolute_return': 0.065417, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003937, 'median_return': 0.003538, 'mean_absolute_return': 0.014375, 'max_adverse_excursion': -0.012528, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003281, 'median_return': 0.008121, 'mean_absolute_return': 0.017004, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.012288, 'median_return': 0.020503, 'mean_absolute_return': 0.029688, 'max_adverse_excursion': -0.024633, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004341, 'median_return': 0.01666, 'mean_absolute_return': 0.038544, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.047065, 'median_return': 0.069875, 'mean_absolute_return': 0.06854, 'max_adverse_excursion': -0.063544, 'max_favorable_excursion': 0.114016}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.001049, 'median_return': 0.002267, 'mean_absolute_return': 0.013564, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001993, 'median_return': 0.000208, 'mean_absolute_return': 0.016871, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.001884, 'median_return': -0.001676, 'mean_absolute_return': 0.018875, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.006123, 'median_return': 0.015661, 'mean_absolute_return': 0.031315, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.023165, 'median_return': 0.032524, 'mean_absolute_return': 0.060323, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.7}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 20, 'both_miss': 20}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.05, 'both_hit': 18, 'both_miss': 22}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.125, 'both_hit': 19, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.075, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.075, 'both_hit': 33, 'both_miss': 7}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.000689, 'median_return': 0.002267, 'mean_absolute_return': 0.013709, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.036588}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.003467, 'median_return': -0.001796, 'mean_absolute_return': 0.017531, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.001524, 'median_return': -0.001676, 'mean_absolute_return': 0.018676, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.008042, 'median_return': 0.01775, 'mean_absolute_return': 0.03365, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.020259, 'median_return': 0.031838, 'mean_absolute_return': 0.059865, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.164609}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.003281, 'median_return': 0.002889, 'mean_absolute_return': 0.013453, 'max_adverse_excursion': -0.032103, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.004539, 'median_return': 0.005327, 'mean_absolute_return': 0.014942, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.002708, 'median_return': 0.000242, 'mean_absolute_return': 0.023798, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000345, 'median_return': 0.004543, 'mean_absolute_return': 0.027201, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.041442, 'median_return': 0.064286, 'mean_absolute_return': 0.064984, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.139575}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.003281`, median `0.002889`, mae `0.013453`
- 5d: sample `20`, hit `0.55`, avg `0.004539`, median `0.005327`, mae `0.014942`
- 10d: sample `20`, hit `0.5`, avg `0.002708`, median `0.000242`, mae `0.023798`
- 20d: sample `20`, hit `0.5`, avg `-0.000345`, median `0.004543`, mae `0.027201`
- 60d: sample `20`, hit `0.7`, avg `0.041442`, median `0.064286`, mae `0.064984`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.000689`, median `0.002267`, mae `0.013709`
- 5d: sample `60`, hit `0.4833`, avg `-0.003467`, median `-0.001796`, mae `0.017531`
- 10d: sample `60`, hit `0.4667`, avg `-0.001524`, median `-0.001676`, mae `0.018676`
- 20d: sample `60`, hit `0.7333`, avg `0.008042`, median `0.01775`, mae `0.03365`
- 60d: sample `60`, hit `0.6`, avg `0.020259`, median `0.031838`, mae `0.059865`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.003281`, median `0.002889`, mae `0.013453`
- 5d: sample `20`, hit `0.55`, avg `0.004539`, median `0.005327`, mae `0.014942`
- 10d: sample `20`, hit `0.5`, avg `0.002708`, median `0.000242`, mae `0.023798`
- 20d: sample `20`, hit `0.5`, avg `-0.000345`, median `0.004543`, mae `0.027201`
- 60d: sample `20`, hit `0.7`, avg `0.041442`, median `0.064286`, mae `0.064984`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001373`, median `0.004243`, mae `0.016199`
- 5d: sample `40`, hit `0.475`, avg `-0.003496`, median `-0.003328`, mae `0.020007`
- 10d: sample `40`, hit `0.525`, avg `0.002161`, median `0.004301`, mae `0.019324`
- 20d: sample `40`, hit `0.75`, avg `0.014246`, median `0.026531`, mae `0.034037`
- 60d: sample `40`, hit `0.725`, avg `0.039343`, median `0.062356`, mae `0.065417`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.003281`, median `0.002889`, mae `0.013453`
- 5d: sample `20`, hit `0.55`, avg `0.004539`, median `0.005327`, mae `0.014942`
- 10d: sample `20`, hit `0.5`, avg `0.002708`, median `0.000242`, mae `0.023798`
- 20d: sample `20`, hit `0.5`, avg `-0.000345`, median `0.004543`, mae `0.027201`
- 60d: sample `20`, hit `0.7`, avg `0.041442`, median `0.064286`, mae `0.064984`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001373`, median `0.004243`, mae `0.016199`
- 5d: sample `40`, hit `0.475`, avg `-0.003496`, median `-0.003328`, mae `0.020007`
- 10d: sample `40`, hit `0.525`, avg `0.002161`, median `0.004301`, mae `0.019324`
- 20d: sample `40`, hit `0.75`, avg `0.014246`, median `0.026531`, mae `0.034037`
- 60d: sample `40`, hit `0.725`, avg `0.039343`, median `0.062356`, mae `0.065417`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000679`, median `-0.001166`, mae `0.008728`
- 5d: sample `20`, hit `0.5`, avg `-0.003409`, median `0.002786`, mae `0.01258`
- 10d: sample `20`, hit `0.35`, avg `-0.008895`, median `-0.007117`, mae `0.017379`
- 20d: sample `20`, hit `0.7`, avg `-0.004368`, median `0.01251`, mae `0.032877`
- 60d: sample `20`, hit `0.35`, avg `-0.017907`, median `-0.006198`, mae `0.048761`

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
- 3d: sample `20`, hit `0.5`, avg `0.003281`, median `0.002889`, mae `0.013453`
- 5d: sample `20`, hit `0.55`, avg `0.004539`, median `0.005327`, mae `0.014942`
- 10d: sample `20`, hit `0.5`, avg `0.002708`, median `0.000242`, mae `0.023798`
- 20d: sample `20`, hit `0.5`, avg `-0.000345`, median `0.004543`, mae `0.027201`
- 60d: sample `20`, hit `0.7`, avg `0.041442`, median `0.064286`, mae `0.064984`

### surface_only_strength
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.000689`, median `0.002267`, mae `0.013709`
- 5d: sample `60`, hit `0.4833`, avg `-0.003467`, median `-0.001796`, mae `0.017531`
- 10d: sample `60`, hit `0.4667`, avg `-0.001524`, median `-0.001676`, mae `0.018676`
- 20d: sample `60`, hit `0.7333`, avg `0.008042`, median `0.01775`, mae `0.03365`
- 60d: sample `60`, hit `0.6`, avg `0.020259`, median `0.031838`, mae `0.059865`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001373`, median `0.004243`, mae `0.016199`
- 5d: sample `40`, hit `0.475`, avg `-0.003496`, median `-0.003328`, mae `0.020007`
- 10d: sample `40`, hit `0.525`, avg `0.002161`, median `0.004301`, mae `0.019324`
- 20d: sample `40`, hit `0.75`, avg `0.014246`, median `0.026531`, mae `0.034037`
- 60d: sample `40`, hit `0.725`, avg `0.039343`, median `0.062356`, mae `0.065417`

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
- 3d: sample `60`, hit `0.55`, avg `0.002009`, median `0.002998`, mae `0.015284`
- 5d: sample `60`, hit `0.5`, avg `-0.000818`, median `0.000208`, mae `0.018319`
- 10d: sample `60`, hit `0.5167`, avg `0.002343`, median `0.001785`, mae `0.020816`
- 20d: sample `60`, hit `0.6667`, avg `0.009382`, median `0.01666`, mae `0.031758`
- 60d: sample `60`, hit `0.7167`, avg `0.040042`, median `0.062356`, mae `0.065272`

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
