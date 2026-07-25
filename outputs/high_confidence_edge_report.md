# High Confidence Edge Report

Generated at: `2026-07-25T06:08:20.789050+00:00`

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
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.002147`, median `0.00033`, mae `0.019204`
- 5d: sample `40`, hit `0.5`, avg `0.004653`, median `0.00295`, mae `0.023039`
- 10d: sample `40`, hit `0.8`, avg `0.019294`, median `0.025661`, mae `0.029373`
- 20d: sample `40`, hit `0.875`, avg `0.032239`, median `0.034151`, mae `0.03999`
- 60d: sample `40`, hit `0.625`, avg `0.013223`, median `0.061203`, mae `0.09627`

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
- 3d: sample `8`, hit `0.5`, avg `0.00231`, median `0.012272`, mae `0.016338`
- 5d: sample `8`, hit `0.875`, avg `0.011766`, median `0.021578`, mae `0.018329`
- 10d: sample `8`, hit `0.75`, avg `0.011279`, median `0.013069`, mae `0.019001`
- 20d: sample `8`, hit `0.875`, avg `0.034564`, median `0.043456`, mae `0.035742`
- 60d: sample `8`, hit `1.0`, avg `0.096074`, median `0.119272`, mae `0.096074`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.00231`, median `0.012272`, mae `0.016338`
- 5d: sample `8`, hit `0.875`, avg `0.011766`, median `0.021578`, mae `0.018329`
- 10d: sample `8`, hit `0.75`, avg `0.011279`, median `0.013069`, mae `0.019001`
- 20d: sample `8`, hit `0.875`, avg `0.034564`, median `0.043456`, mae `0.035742`
- 60d: sample `8`, hit `1.0`, avg `0.096074`, median `0.119272`, mae `0.096074`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.004306, 'median_return': 0.005804, 'mean_absolute_return': 0.013587, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.008969, 'median_return': 0.010241, 'mean_absolute_return': 0.017174, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.014466, 'median_return': 0.014276, 'mean_absolute_return': 0.020742, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.030712, 'median_return': 0.033582, 'mean_absolute_return': 0.034566, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.975, 'avg_return': 0.086127, 'median_return': 0.084597, 'mean_absolute_return': 0.087168, 'max_adverse_excursion': -0.020815, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00231, 'median_return': 0.012272, 'mean_absolute_return': 0.016338, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.011766, 'median_return': 0.021578, 'mean_absolute_return': 0.018329, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011279, 'median_return': 0.013069, 'mean_absolute_return': 0.019001, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.034564, 'median_return': 0.043456, 'mean_absolute_return': 0.035742, 'max_adverse_excursion': -0.00471, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.096074, 'median_return': 0.119272, 'mean_absolute_return': 0.096074, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.003329, 'median_return': 0.004542, 'mean_absolute_return': 0.016402, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.006261, 'median_return': 0.006036, 'mean_absolute_return': 0.020304, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.017502, 'median_return': 0.021351, 'mean_absolute_return': 0.025731, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 72, 'hit_rate': 0.8472, 'avg_return': 0.031133, 'median_return': 0.033597, 'mean_absolute_return': 0.037448, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.044519, 'median_return': 0.075061, 'mean_absolute_return': 0.091235, 'max_adverse_excursion': -0.190158, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.475}, '60d': {'sample_size': 80, 'hit_rate': 0.675}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 27, 'both_miss': 13}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 27, 'both_miss': 13}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.8125, 'primary_minus_secondary': -0.3, 'both_hit': 33, 'both_miss': 7}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.85, 'primary_minus_secondary': -0.375, 'both_hit': 33, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.125, 'both_hit': 39, 'both_miss': 1}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.003227, 'median_return': 0.004542, 'mean_absolute_return': 0.016396, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.006811, 'median_return': 0.007948, 'mean_absolute_return': 0.020106, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 80, 'hit_rate': 0.8125, 'avg_return': 0.01688, 'median_return': 0.020334, 'mean_absolute_return': 0.025058, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 80, 'hit_rate': 0.85, 'avg_return': 0.031476, 'median_return': 0.033597, 'mean_absolute_return': 0.037278, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.049675, 'median_return': 0.076106, 'mean_absolute_return': 0.091719, 'max_adverse_excursion': -0.190158, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.002147`, median `0.00033`, mae `0.019204`
- 5d: sample `40`, hit `0.5`, avg `0.004653`, median `0.00295`, mae `0.023039`
- 10d: sample `40`, hit `0.8`, avg `0.019294`, median `0.025661`, mae `0.029373`
- 20d: sample `40`, hit `0.875`, avg `0.032239`, median `0.034151`, mae `0.03999`
- 60d: sample `40`, hit `0.625`, avg `0.013223`, median `0.061203`, mae `0.09627`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.00371`, median `-0.002952`, mae `0.017836`
- 5d: sample `20`, hit `0.45`, avg `-0.001041`, median `-0.002452`, mae `0.023014`
- 10d: sample `20`, hit `0.75`, avg `0.017444`, median `0.023905`, mae `0.030127`
- 20d: sample `20`, hit `0.85`, avg `0.029889`, median `0.035693`, mae `0.043262`
- 60d: sample `20`, hit `0.6`, avg `0.013073`, median `0.076106`, mae `0.100015`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.002147`, median `0.00033`, mae `0.019204`
- 5d: sample `40`, hit `0.5`, avg `0.004653`, median `0.00295`, mae `0.023039`
- 10d: sample `40`, hit `0.8`, avg `0.019294`, median `0.025661`, mae `0.029373`
- 20d: sample `40`, hit `0.875`, avg `0.032239`, median `0.034151`, mae `0.03999`
- 60d: sample `40`, hit `0.625`, avg `0.013223`, median `0.061203`, mae `0.09627`

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
- 3d: sample `80`, hit `0.5875`, avg `0.003227`, median `0.004542`, mae `0.016396`
- 5d: sample `80`, hit `0.5875`, avg `0.006811`, median `0.007948`, mae `0.020106`
- 10d: sample `80`, hit `0.8125`, avg `0.01688`, median `0.020334`, mae `0.025058`
- 20d: sample `80`, hit `0.85`, avg `0.031476`, median `0.033597`, mae `0.037278`
- 60d: sample `80`, hit `0.8`, avg `0.049675`, median `0.076106`, mae `0.091719`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.003227`, median `0.004542`, mae `0.016396`
- 5d: sample `80`, hit `0.5875`, avg `0.006811`, median `0.007948`, mae `0.020106`
- 10d: sample `80`, hit `0.8125`, avg `0.01688`, median `0.020334`, mae `0.025058`
- 20d: sample `80`, hit `0.85`, avg `0.031476`, median `0.033597`, mae `0.037278`
- 60d: sample `80`, hit `0.8`, avg `0.049675`, median `0.076106`, mae `0.091719`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004306`, median `0.005804`, mae `0.013587`
- 5d: sample `40`, hit `0.675`, avg `0.008969`, median `0.010241`, mae `0.017174`
- 10d: sample `40`, hit `0.825`, avg `0.014466`, median `0.014276`, mae `0.020742`
- 20d: sample `40`, hit `0.825`, avg `0.030712`, median `0.033582`, mae `0.034566`
- 60d: sample `40`, hit `0.975`, avg `0.086127`, median `0.084597`, mae `0.087168`

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
