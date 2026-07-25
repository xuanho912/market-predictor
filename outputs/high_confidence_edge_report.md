# High Confidence Edge Report

Generated at: `2026-07-25T04:32:29.262210+00:00`

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
- 3d: sample `80`, hit `0.6125`, avg `0.004561`, median `0.0054`, mae `0.016593`
- 5d: sample `80`, hit `0.6375`, avg `0.008785`, median `0.009709`, mae `0.020663`
- 10d: sample `80`, hit `0.775`, avg `0.016591`, median `0.021584`, mae `0.025739`
- 20d: sample `80`, hit `0.8375`, avg `0.030276`, median `0.033597`, mae `0.037597`
- 60d: sample `80`, hit `0.7875`, avg `0.04647`, median `0.074897`, mae `0.090511`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.004561, 'median_return': 0.0054, 'mean_absolute_return': 0.016593, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.008785, 'median_return': 0.009709, 'mean_absolute_return': 0.020663, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 80, 'hit_rate': 0.775, 'avg_return': 0.016591, 'median_return': 0.021584, 'mean_absolute_return': 0.025739, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 80, 'hit_rate': 0.8375, 'avg_return': 0.030276, 'median_return': 0.033597, 'mean_absolute_return': 0.037597, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.04647, 'median_return': 0.074897, 'mean_absolute_return': 0.090511, 'max_adverse_excursion': -0.190158, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00231, 'median_return': 0.012272, 'mean_absolute_return': 0.016338, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.011766, 'median_return': 0.021578, 'mean_absolute_return': 0.018329, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011279, 'median_return': 0.013069, 'mean_absolute_return': 0.019001, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.034564, 'median_return': 0.043456, 'mean_absolute_return': 0.035742, 'max_adverse_excursion': -0.00471, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.096074, 'median_return': 0.119272, 'mean_absolute_return': 0.096074, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.004811, 'median_return': 0.0054, 'mean_absolute_return': 0.016621, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.008453, 'median_return': 0.008152, 'mean_absolute_return': 0.020922, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.017181, 'median_return': 0.022558, 'mean_absolute_return': 0.026488, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.0298, 'median_return': 0.033597, 'mean_absolute_return': 0.037803, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.040959, 'median_return': 0.071518, 'mean_absolute_return': 0.089893, 'max_adverse_excursion': -0.190158, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.4875}, '60d': {'sample_size': 80, 'hit_rate': 0.6625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.05, 'both_hit': 27, 'both_miss': 13}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.075, 'both_hit': 28, 'both_miss': 12}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.775, 'primary_minus_secondary': -0.275, 'both_hit': 31, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.8375, 'primary_minus_secondary': -0.35, 'both_hit': 33, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.125, 'both_hit': 38, 'both_miss': 2}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.004561, 'median_return': 0.0054, 'mean_absolute_return': 0.016593, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.008785, 'median_return': 0.009709, 'mean_absolute_return': 0.020663, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 80, 'hit_rate': 0.775, 'avg_return': 0.016591, 'median_return': 0.021584, 'mean_absolute_return': 0.025739, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 80, 'hit_rate': 0.8375, 'avg_return': 0.030276, 'median_return': 0.033597, 'mean_absolute_return': 0.037597, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.090062}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.04647, 'median_return': 0.074897, 'mean_absolute_return': 0.090511, 'max_adverse_excursion': -0.190158, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004881`, median `0.005804`, mae `0.013897`
- 5d: sample `40`, hit `0.7`, avg `0.010233`, median `0.0154`, mae `0.018688`
- 10d: sample `40`, hit `0.775`, avg `0.013995`, median `0.01704`, mae `0.021819`
- 20d: sample `40`, hit `0.825`, avg `0.031002`, median `0.033597`, mae `0.034855`
- 60d: sample `40`, hit `0.95`, avg `0.081442`, median `0.084301`, mae `0.084829`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004241`, median `0.001761`, mae `0.01929`
- 5d: sample `40`, hit `0.575`, avg `0.007336`, median `0.00641`, mae `0.022637`
- 10d: sample `40`, hit `0.775`, avg `0.019187`, median `0.027869`, mae `0.02966`
- 20d: sample `40`, hit `0.85`, avg `0.029551`, median `0.033791`, mae `0.04034`
- 60d: sample `40`, hit `0.625`, avg `0.011499`, median `0.060145`, mae `0.096193`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004881`, median `0.005804`, mae `0.013897`
- 5d: sample `40`, hit `0.7`, avg `0.010233`, median `0.0154`, mae `0.018688`
- 10d: sample `40`, hit `0.775`, avg `0.013995`, median `0.01704`, mae `0.021819`
- 20d: sample `40`, hit `0.825`, avg `0.031002`, median `0.033597`, mae `0.034855`
- 60d: sample `40`, hit `0.95`, avg `0.081442`, median `0.084301`, mae `0.084829`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004881`, median `0.005804`, mae `0.013897`
- 5d: sample `40`, hit `0.7`, avg `0.010233`, median `0.0154`, mae `0.018688`
- 10d: sample `40`, hit `0.775`, avg `0.013995`, median `0.01704`, mae `0.021819`
- 20d: sample `40`, hit `0.825`, avg `0.031002`, median `0.033597`, mae `0.034855`
- 60d: sample `40`, hit `0.95`, avg `0.081442`, median `0.084301`, mae `0.084829`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004241`, median `0.001761`, mae `0.01929`
- 5d: sample `40`, hit `0.575`, avg `0.007336`, median `0.00641`, mae `0.022637`
- 10d: sample `40`, hit `0.775`, avg `0.019187`, median `0.027869`, mae `0.02966`
- 20d: sample `40`, hit `0.85`, avg `0.029551`, median `0.033791`, mae `0.04034`
- 60d: sample `40`, hit `0.625`, avg `0.011499`, median `0.060145`, mae `0.096193`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004881`, median `0.005804`, mae `0.013897`
- 5d: sample `40`, hit `0.7`, avg `0.010233`, median `0.0154`, mae `0.018688`
- 10d: sample `40`, hit `0.775`, avg `0.013995`, median `0.01704`, mae `0.021819`
- 20d: sample `40`, hit `0.825`, avg `0.031002`, median `0.033597`, mae `0.034855`
- 60d: sample `40`, hit `0.95`, avg `0.081442`, median `0.084301`, mae `0.084829`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004881`, median `0.005804`, mae `0.013897`
- 5d: sample `40`, hit `0.7`, avg `0.010233`, median `0.0154`, mae `0.018688`
- 10d: sample `40`, hit `0.775`, avg `0.013995`, median `0.01704`, mae `0.021819`
- 20d: sample `40`, hit `0.825`, avg `0.031002`, median `0.033597`, mae `0.034855`
- 60d: sample `40`, hit `0.95`, avg `0.081442`, median `0.084301`, mae `0.084829`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004241`, median `0.001761`, mae `0.01929`
- 5d: sample `40`, hit `0.575`, avg `0.007336`, median `0.00641`, mae `0.022637`
- 10d: sample `40`, hit `0.775`, avg `0.019187`, median `0.027869`, mae `0.02966`
- 20d: sample `40`, hit `0.85`, avg `0.029551`, median `0.033791`, mae `0.04034`
- 60d: sample `40`, hit `0.625`, avg `0.011499`, median `0.060145`, mae `0.096193`

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
- 3d: sample `80`, hit `0.6125`, avg `0.004561`, median `0.0054`, mae `0.016593`
- 5d: sample `80`, hit `0.6375`, avg `0.008785`, median `0.009709`, mae `0.020663`
- 10d: sample `80`, hit `0.775`, avg `0.016591`, median `0.021584`, mae `0.025739`
- 20d: sample `80`, hit `0.8375`, avg `0.030276`, median `0.033597`, mae `0.037597`
- 60d: sample `80`, hit `0.7875`, avg `0.04647`, median `0.074897`, mae `0.090511`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004881`, median `0.005804`, mae `0.013897`
- 5d: sample `40`, hit `0.7`, avg `0.010233`, median `0.0154`, mae `0.018688`
- 10d: sample `40`, hit `0.775`, avg `0.013995`, median `0.01704`, mae `0.021819`
- 20d: sample `40`, hit `0.825`, avg `0.031002`, median `0.033597`, mae `0.034855`
- 60d: sample `40`, hit `0.95`, avg `0.081442`, median `0.084301`, mae `0.084829`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.004561`, median `0.0054`, mae `0.016593`
- 5d: sample `80`, hit `0.6375`, avg `0.008785`, median `0.009709`, mae `0.020663`
- 10d: sample `80`, hit `0.775`, avg `0.016591`, median `0.021584`, mae `0.025739`
- 20d: sample `80`, hit `0.8375`, avg `0.030276`, median `0.033597`, mae `0.037597`
- 60d: sample `80`, hit `0.7875`, avg `0.04647`, median `0.074897`, mae `0.090511`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004881`, median `0.005804`, mae `0.013897`
- 5d: sample `40`, hit `0.7`, avg `0.010233`, median `0.0154`, mae `0.018688`
- 10d: sample `40`, hit `0.775`, avg `0.013995`, median `0.01704`, mae `0.021819`
- 20d: sample `40`, hit `0.825`, avg `0.031002`, median `0.033597`, mae `0.034855`
- 60d: sample `40`, hit `0.95`, avg `0.081442`, median `0.084301`, mae `0.084829`

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
