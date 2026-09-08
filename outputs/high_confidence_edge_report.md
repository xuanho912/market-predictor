# High Confidence Edge Report

Generated at: `2026-09-08T22:49:59.082311+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `-0.000452`, median `0.000616`, mae `0.013634`
- 5d: sample `80`, hit `0.5625`, avg `0.000652`, median `0.001303`, mae `0.017367`
- 10d: sample `80`, hit `0.4125`, avg `0.001371`, median `-0.007011`, mae `0.023938`
- 20d: sample `80`, hit `0.675`, avg `0.011166`, median `0.020068`, mae `0.036298`
- 60d: sample `80`, hit `0.75`, avg `0.041163`, median `0.058598`, mae `0.07189`

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
- 3d: sample `8`, hit `0.5`, avg `-0.002268`, median `0.000616`, mae `0.012909`
- 5d: sample `8`, hit `0.75`, avg `0.010126`, median `0.01181`, mae `0.015281`
- 10d: sample `8`, hit `0.375`, avg `-0.001276`, median `-0.011522`, mae `0.030449`
- 20d: sample `8`, hit `0.625`, avg `0.005107`, median `0.007572`, mae `0.039905`
- 60d: sample `8`, hit `0.875`, avg `0.044291`, median `0.085054`, mae `0.080767`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004996`, median `0.001558`, mae `0.009462`
- 5d: sample `8`, hit `0.25`, avg `-0.008407`, median `-0.012956`, mae `0.015361`
- 10d: sample `8`, hit `0.625`, avg `0.006152`, median `0.019233`, mae `0.019493`
- 20d: sample `8`, hit `0.875`, avg `0.016559`, median `0.029166`, mae `0.024871`
- 60d: sample `8`, hit `0.75`, avg `0.0436`, median `0.059495`, mae `0.062508`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004996, 'median_return': 0.001558, 'mean_absolute_return': 0.009462, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008407, 'median_return': -0.012956, 'mean_absolute_return': 0.015361, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006152, 'median_return': 0.019233, 'mean_absolute_return': 0.019493, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.016559, 'median_return': 0.029166, 'mean_absolute_return': 0.024871, 'max_adverse_excursion': -0.033249, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.0436, 'median_return': 0.059495, 'mean_absolute_return': 0.062508, 'max_adverse_excursion': -0.055503, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 5.3e-05, 'median_return': 0.000616, 'mean_absolute_return': 0.014097, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.001658, 'median_return': 0.002786, 'mean_absolute_return': 0.01759, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': 0.00084, 'median_return': -0.007117, 'mean_absolute_return': 0.024431, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.010567, 'median_return': 0.015261, 'mean_absolute_return': 0.037567, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.040892, 'median_return': 0.058598, 'mean_absolute_return': 0.072933, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.375}, '60d': {'sample_size': 80, 'hit_rate': 0.425}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.001406, 'median_return': 0.000603, 'mean_absolute_return': 0.011624, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.000421, 'median_return': 0.001303, 'mean_absolute_return': 0.014414, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.001032, 'median_return': -0.007011, 'mean_absolute_return': 0.021844, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.059577}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.004667, 'median_return': 0.013877, 'mean_absolute_return': 0.037061, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.029809, 'median_return': 0.046132, 'mean_absolute_return': 0.068668, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002411, 'median_return': 0.008973, 'mean_absolute_return': 0.019661, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.001344, 'median_return': 0.007909, 'mean_absolute_return': 0.026226, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.008578, 'median_return': -0.00367, 'mean_absolute_return': 0.030218, 'max_adverse_excursion': -0.033079, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.030665, 'median_return': 0.025442, 'mean_absolute_return': 0.034006, 'max_adverse_excursion': -0.019772, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.075224, 'median_return': 0.079128, 'mean_absolute_return': 0.081558, 'max_adverse_excursion': -0.035018, 'max_favorable_excursion': 0.19145}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003443`, median `-0.003594`, mae `0.007894`
- 5d: sample `20`, hit `0.5`, avg `-0.003933`, median `0.000688`, mae `0.010268`
- 10d: sample `20`, hit `0.25`, avg `-0.009551`, median `-0.012383`, mae `0.020848`
- 20d: sample `20`, hit `0.45`, avg `-0.015866`, median `-0.003522`, mae `0.038993`
- 60d: sample `20`, hit `0.5`, avg `0.011287`, median `0.032982`, mae `0.062327`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000205`, median `0.002329`, mae `0.016201`
- 5d: sample `40`, hit `0.525`, avg `-0.001485`, median `0.000415`, mae `0.01989`
- 10d: sample `40`, hit `0.425`, avg `0.004884`, median `-0.00367`, mae `0.023901`
- 20d: sample `40`, hit `0.825`, avg `0.025495`, median `0.029166`, mae `0.035574`
- 60d: sample `40`, hit `0.825`, avg `0.059442`, median `0.067551`, mae `0.077788`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000205`, median `0.002329`, mae `0.016201`
- 5d: sample `40`, hit `0.525`, avg `-0.001485`, median `0.000415`, mae `0.01989`
- 10d: sample `40`, hit `0.425`, avg `0.004884`, median `-0.00367`, mae `0.023901`
- 20d: sample `40`, hit `0.825`, avg `0.025495`, median `0.029166`, mae `0.035574`
- 60d: sample `40`, hit `0.825`, avg `0.059442`, median `0.067551`, mae `0.077788`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001226`, median `0.004487`, mae `0.014237`
- 5d: sample `20`, hit `0.7`, avg `0.00951`, median `0.011391`, mae `0.019419`
- 10d: sample `20`, hit `0.55`, avg `0.005267`, median `0.004883`, mae `0.0271`
- 20d: sample `20`, hit `0.6`, avg `0.009542`, median `0.007572`, mae `0.035049`
- 60d: sample `20`, hit `0.85`, avg `0.034481`, median `0.039842`, mae `0.069657`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000205`, median `0.002329`, mae `0.016201`
- 5d: sample `40`, hit `0.525`, avg `-0.001485`, median `0.000415`, mae `0.01989`
- 10d: sample `40`, hit `0.425`, avg `0.004884`, median `-0.00367`, mae `0.023901`
- 20d: sample `40`, hit `0.825`, avg `0.025495`, median `0.029166`, mae `0.035574`
- 60d: sample `40`, hit `0.825`, avg `0.059442`, median `0.067551`, mae `0.077788`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.000452`, median `0.000616`, mae `0.013634`
- 5d: sample `80`, hit `0.5625`, avg `0.000652`, median `0.001303`, mae `0.017367`
- 10d: sample `80`, hit `0.4125`, avg `0.001371`, median `-0.007011`, mae `0.023938`
- 20d: sample `80`, hit `0.675`, avg `0.011166`, median `0.020068`, mae `0.036298`
- 60d: sample `80`, hit `0.75`, avg `0.041163`, median `0.058598`, mae `0.07189`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001226`, median `0.004487`, mae `0.014237`
- 5d: sample `20`, hit `0.7`, avg `0.00951`, median `0.011391`, mae `0.019419`
- 10d: sample `20`, hit `0.55`, avg `0.005267`, median `0.004883`, mae `0.0271`
- 20d: sample `20`, hit `0.6`, avg `0.009542`, median `0.007572`, mae `0.035049`
- 60d: sample `20`, hit `0.85`, avg `0.034481`, median `0.039842`, mae `0.069657`

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
