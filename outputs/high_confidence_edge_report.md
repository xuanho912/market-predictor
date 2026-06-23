# High Confidence Edge Report

Generated at: `2026-06-23T23:39:15.778194+00:00`

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
- 3d: sample `20`, hit `0.6`, avg `0.008143`, median `0.008337`, mae `0.015578`
- 5d: sample `20`, hit `0.6`, avg `0.007611`, median `0.011986`, mae `0.014784`
- 10d: sample `20`, hit `0.5`, avg `0.004441`, median `0.000242`, mae `0.025191`
- 20d: sample `20`, hit `0.6`, avg `0.009014`, median `0.016065`, mae `0.033559`
- 60d: sample `20`, hit `0.75`, avg `0.045925`, median `0.073435`, mae `0.072883`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001397`, median `-0.001811`, mae `0.014676`
- 5d: sample `60`, hit `0.45`, avg `-0.003411`, median `-0.006464`, mae `0.018481`
- 10d: sample `60`, hit `0.4333`, avg `-0.001069`, median `-0.00174`, mae `0.023323`
- 20d: sample `60`, hit `0.8167`, avg `0.017335`, median `0.024811`, mae `0.033608`
- 60d: sample `60`, hit `0.7167`, avg `0.037836`, median `0.060303`, mae `0.066297`

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
- 3d: sample `8`, hit `0.375`, avg `-0.005153`, median `-0.004861`, mae `0.010636`
- 5d: sample `8`, hit `0.375`, avg `-0.001032`, median `-0.002002`, mae `0.011749`
- 10d: sample `8`, hit `0.25`, avg `-0.011333`, median `-0.009595`, mae `0.025158`
- 20d: sample `8`, hit `0.5`, avg `-0.004369`, median `0.01666`, mae `0.030502`
- 60d: sample `8`, hit `0.875`, avg `0.056387`, median `0.073435`, mae `0.072273`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.005153`, median `-0.004861`, mae `0.010636`
- 5d: sample `8`, hit `0.375`, avg `-0.001032`, median `-0.002002`, mae `0.011749`
- 10d: sample `8`, hit `0.25`, avg `-0.011333`, median `-0.009595`, mae `0.025158`
- 20d: sample `8`, hit `0.5`, avg `-0.004369`, median `0.01666`, mae `0.030502`
- 60d: sample `8`, hit `0.875`, avg `0.056387`, median `0.073435`, mae `0.072273`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.008143, 'median_return': 0.008337, 'mean_absolute_return': 0.015578, 'max_adverse_excursion': -0.032103, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.007611, 'median_return': 0.011986, 'mean_absolute_return': 0.014784, 'max_adverse_excursion': -0.018916, 'max_favorable_excursion': 0.031797}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.004441, 'median_return': 0.000242, 'mean_absolute_return': 0.025191, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.009014, 'median_return': 0.016065, 'mean_absolute_return': 0.033559, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.045925, 'median_return': 0.073435, 'mean_absolute_return': 0.072883, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.164619}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.001397, 'median_return': -0.001811, 'mean_absolute_return': 0.014676, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.003411, 'median_return': -0.006464, 'mean_absolute_return': 0.018481, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.001069, 'median_return': -0.00174, 'mean_absolute_return': 0.023323, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.017335, 'median_return': 0.024811, 'mean_absolute_return': 0.033608, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.081363}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.037836, 'median_return': 0.060303, 'mean_absolute_return': 0.066297, 'max_adverse_excursion': -0.111942, 'max_favorable_excursion': 0.156405}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.005153, 'median_return': -0.004861, 'mean_absolute_return': 0.010636, 'max_adverse_excursion': -0.032103, 'max_favorable_excursion': 0.010308}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.001032, 'median_return': -0.002002, 'mean_absolute_return': 0.011749, 'max_adverse_excursion': -0.017255, 'max_favorable_excursion': 0.018277}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.011333, 'median_return': -0.009595, 'mean_absolute_return': 0.025158, 'max_adverse_excursion': -0.050161, 'max_favorable_excursion': 0.042458}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004369, 'median_return': 0.01666, 'mean_absolute_return': 0.030502, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.03495}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.056387, 'median_return': 0.073435, 'mean_absolute_return': 0.072273, 'max_adverse_excursion': -0.063544, 'max_favorable_excursion': 0.086982}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.00167, 'median_return': -0.000756, 'mean_absolute_return': 0.015375, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.000613, 'median_return': 0.000208, 'mean_absolute_return': 0.018202, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.001602, 'median_return': -0.001083, 'mean_absolute_return': 0.023638, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.017435, 'median_return': 0.02086, 'mean_absolute_return': 0.033939, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.038022, 'median_return': 0.060303, 'mean_absolute_return': 0.067462, 'max_adverse_excursion': -0.111942, 'max_favorable_excursion': 0.164619}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.7625}, '60d': {'sample_size': 80, 'hit_rate': 0.725}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 30, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 30, 'both_miss': 30}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.05, 'both_hit': 28, 'both_miss': 32}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7625, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': 0.1, 'both_hit': 47, 'both_miss': 13}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': 0.05, 'both_hit': 46, 'both_miss': 14}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': 0.000988, 'median_return': -0.001166, 'mean_absolute_return': 0.014902, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.052736}, '5d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.000655, 'median_return': -0.000371, 'mean_absolute_return': 0.017557, 'max_adverse_excursion': -0.045904, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': 0.000309, 'median_return': -0.00174, 'mean_absolute_return': 0.02379, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.015255, 'median_return': 0.020751, 'mean_absolute_return': 0.033596, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.039858, 'median_return': 0.062356, 'mean_absolute_return': 0.067943, 'max_adverse_excursion': -0.111942, 'max_favorable_excursion': 0.164619}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.002728`, median `-0.000722`, mae `0.013012`
- 5d: sample `40`, hit `0.525`, avg `0.001093`, median `0.002786`, mae `0.015421`
- 10d: sample `40`, hit `0.45`, avg `-0.000644`, median `-0.004417`, mae `0.023755`
- 20d: sample `40`, hit `0.65`, avg `0.002808`, median `0.015404`, mae `0.03292`
- 60d: sample `40`, hit `0.675`, avg `0.028266`, median `0.044344`, mae `0.063868`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001397`, median `-0.001811`, mae `0.014676`
- 5d: sample `60`, hit `0.45`, avg `-0.003411`, median `-0.006464`, mae `0.018481`
- 10d: sample `60`, hit `0.4333`, avg `-0.001069`, median `-0.00174`, mae `0.023323`
- 20d: sample `60`, hit `0.8167`, avg `0.017335`, median `0.024811`, mae `0.033608`
- 60d: sample `60`, hit `0.7167`, avg `0.037836`, median `0.060303`, mae `0.066297`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.002728`, median `-0.000722`, mae `0.013012`
- 5d: sample `40`, hit `0.525`, avg `0.001093`, median `0.002786`, mae `0.015421`
- 10d: sample `40`, hit `0.45`, avg `-0.000644`, median `-0.004417`, mae `0.023755`
- 20d: sample `40`, hit `0.65`, avg `0.002808`, median `0.015404`, mae `0.03292`
- 60d: sample `40`, hit `0.675`, avg `0.028266`, median `0.044344`, mae `0.063868`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.001397`, median `-0.001811`, mae `0.014676`
- 5d: sample `60`, hit `0.45`, avg `-0.003411`, median `-0.006464`, mae `0.018481`
- 10d: sample `60`, hit `0.4333`, avg `-0.001069`, median `-0.00174`, mae `0.023323`
- 20d: sample `60`, hit `0.8167`, avg `0.017335`, median `0.024811`, mae `0.033608`
- 60d: sample `60`, hit `0.7167`, avg `0.037836`, median `0.060303`, mae `0.066297`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.008143`, median `0.008337`, mae `0.015578`
- 5d: sample `20`, hit `0.6`, avg `0.007611`, median `0.011986`, mae `0.014784`
- 10d: sample `20`, hit `0.5`, avg `0.004441`, median `0.000242`, mae `0.025191`
- 20d: sample `20`, hit `0.6`, avg `0.009014`, median `0.016065`, mae `0.033559`
- 60d: sample `20`, hit `0.75`, avg `0.045925`, median `0.073435`, mae `0.072883`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.000752`, median `-0.001658`, mae `0.016792`
- 5d: sample `40`, hit `0.45`, avg `-0.002404`, median `-0.004216`, mae `0.019692`
- 10d: sample `40`, hit `0.45`, avg `0.001261`, median `-0.001083`, mae `0.023826`
- 20d: sample `40`, hit `0.875`, avg `0.027701`, median `0.031196`, mae `0.034271`
- 60d: sample `40`, hit `0.775`, avg `0.05145`, median `0.068046`, mae `0.072018`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.002728`, median `-0.000722`, mae `0.013012`
- 5d: sample `40`, hit `0.525`, avg `0.001093`, median `0.002786`, mae `0.015421`
- 10d: sample `40`, hit `0.45`, avg `-0.000644`, median `-0.004417`, mae `0.023755`
- 20d: sample `40`, hit `0.65`, avg `0.002808`, median `0.015404`, mae `0.03292`
- 60d: sample `40`, hit `0.675`, avg `0.028266`, median `0.044344`, mae `0.063868`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.000752`, median `-0.001658`, mae `0.016792`
- 5d: sample `40`, hit `0.45`, avg `-0.002404`, median `-0.004216`, mae `0.019692`
- 10d: sample `40`, hit `0.45`, avg `0.001261`, median `-0.001083`, mae `0.023826`
- 20d: sample `40`, hit `0.875`, avg `0.027701`, median `0.031196`, mae `0.034271`
- 60d: sample `40`, hit `0.775`, avg `0.05145`, median `0.068046`, mae `0.072018`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.008143`, median `0.008337`, mae `0.015578`
- 5d: sample `20`, hit `0.6`, avg `0.007611`, median `0.011986`, mae `0.014784`
- 10d: sample `20`, hit `0.5`, avg `0.004441`, median `0.000242`, mae `0.025191`
- 20d: sample `20`, hit `0.6`, avg `0.009014`, median `0.016065`, mae `0.033559`
- 60d: sample `20`, hit `0.75`, avg `0.045925`, median `0.073435`, mae `0.072883`

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
- 3d: sample `40`, hit `0.475`, avg `0.002728`, median `-0.000722`, mae `0.013012`
- 5d: sample `40`, hit `0.525`, avg `0.001093`, median `0.002786`, mae `0.015421`
- 10d: sample `40`, hit `0.45`, avg `-0.000644`, median `-0.004417`, mae `0.023755`
- 20d: sample `40`, hit `0.65`, avg `0.002808`, median `0.015404`, mae `0.03292`
- 60d: sample `40`, hit `0.675`, avg `0.028266`, median `0.044344`, mae `0.063868`

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
- 3d: sample `80`, hit `0.4625`, avg `0.000988`, median `-0.001166`, mae `0.014902`
- 5d: sample `80`, hit `0.4875`, avg `-0.000655`, median `-0.000371`, mae `0.017557`
- 10d: sample `80`, hit `0.45`, avg `0.000309`, median `-0.00174`, mae `0.02379`
- 20d: sample `80`, hit `0.7625`, avg `0.015255`, median `0.020751`, mae `0.033596`
- 60d: sample `80`, hit `0.725`, avg `0.039858`, median `0.062356`, mae `0.067943`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `0.000988`, median `-0.001166`, mae `0.014902`
- 5d: sample `80`, hit `0.4875`, avg `-0.000655`, median `-0.000371`, mae `0.017557`
- 10d: sample `80`, hit `0.45`, avg `0.000309`, median `-0.00174`, mae `0.02379`
- 20d: sample `80`, hit `0.7625`, avg `0.015255`, median `0.020751`, mae `0.033596`
- 60d: sample `80`, hit `0.725`, avg `0.039858`, median `0.062356`, mae `0.067943`

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
