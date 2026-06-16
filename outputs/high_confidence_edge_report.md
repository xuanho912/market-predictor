# High Confidence Edge Report

Generated at: `2026-06-16T00:16:16.331825+00:00`

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
- 3d: sample `80`, hit `0.6125`, avg `0.003775`, median `0.004569`, mae `0.013554`
- 5d: sample `80`, hit `0.625`, avg `0.004915`, median `0.005327`, mae `0.016347`
- 10d: sample `80`, hit `0.5875`, avg `0.006102`, median `0.006913`, mae `0.02153`
- 20d: sample `80`, hit `0.675`, avg `0.005719`, median `0.015404`, mae `0.034535`
- 60d: sample `80`, hit `0.5875`, avg `0.022988`, median `0.03283`, mae `0.060465`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006356`, median `0.001558`, mae `0.014327`
- 5d: sample `8`, hit `0.25`, avg `-0.007284`, median `-0.007788`, mae `0.017582`
- 10d: sample `8`, hit `0.625`, avg `0.005714`, median `0.0076`, mae `0.016175`
- 20d: sample `8`, hit `0.875`, avg `0.022118`, median `0.028791`, mae `0.024013`
- 60d: sample `8`, hit `0.625`, avg `0.029911`, median `0.046132`, mae `0.052222`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006356`, median `0.001558`, mae `0.014327`
- 5d: sample `8`, hit `0.25`, avg `-0.007284`, median `-0.007788`, mae `0.017582`
- 10d: sample `8`, hit `0.625`, avg `0.005714`, median `0.0076`, mae `0.016175`
- 20d: sample `8`, hit `0.875`, avg `0.022118`, median `0.028791`, mae `0.024013`
- 60d: sample `8`, hit `0.625`, avg `0.029911`, median `0.046132`, mae `0.052222`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.003775, 'median_return': 0.004569, 'mean_absolute_return': 0.013554, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.004915, 'median_return': 0.005327, 'mean_absolute_return': 0.016347, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.053265}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.006102, 'median_return': 0.006913, 'mean_absolute_return': 0.02153, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.005719, 'median_return': 0.015404, 'mean_absolute_return': 0.034535, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.022988, 'median_return': 0.03283, 'mean_absolute_return': 0.060465, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.178887}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006356, 'median_return': 0.001558, 'mean_absolute_return': 0.014327, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.007284, 'median_return': -0.007788, 'mean_absolute_return': 0.017582, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005714, 'median_return': 0.0076, 'mean_absolute_return': 0.016175, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.022118, 'median_return': 0.028791, 'mean_absolute_return': 0.024013, 'max_adverse_excursion': -0.007581, 'max_favorable_excursion': 0.03323}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.029911, 'median_return': 0.046132, 'mean_absolute_return': 0.052222, 'max_adverse_excursion': -0.038302, 'max_favorable_excursion': 0.094627}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.004901, 'median_return': 0.004697, 'mean_absolute_return': 0.013468, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.006271, 'median_return': 0.00596, 'mean_absolute_return': 0.016209, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.053265}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.006145, 'median_return': 0.006913, 'mean_absolute_return': 0.022125, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.003897, 'median_return': 0.012291, 'mean_absolute_return': 0.035705, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.022219, 'median_return': 0.03283, 'mean_absolute_return': 0.061381, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.178887}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.625}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': 0.0, 'both_hit': 54, 'both_miss': 26}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.003775, 'median_return': 0.004569, 'mean_absolute_return': 0.013554, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.004915, 'median_return': 0.005327, 'mean_absolute_return': 0.016347, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.053265}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.006102, 'median_return': 0.006913, 'mean_absolute_return': 0.02153, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.005719, 'median_return': 0.015404, 'mean_absolute_return': 0.034535, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.022988, 'median_return': 0.03283, 'mean_absolute_return': 0.060465, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.178887}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003775`, median `0.004569`, mae `0.013554`
- 5d: sample `80`, hit `0.625`, avg `0.004915`, median `0.005327`, mae `0.016347`
- 10d: sample `80`, hit `0.5875`, avg `0.006102`, median `0.006913`, mae `0.02153`
- 20d: sample `80`, hit `0.675`, avg `0.005719`, median `0.015404`, mae `0.034535`
- 60d: sample `80`, hit `0.5875`, avg `0.022988`, median `0.03283`, mae `0.060465`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003775`, median `0.004569`, mae `0.013554`
- 5d: sample `80`, hit `0.625`, avg `0.004915`, median `0.005327`, mae `0.016347`
- 10d: sample `80`, hit `0.5875`, avg `0.006102`, median `0.006913`, mae `0.02153`
- 20d: sample `80`, hit `0.675`, avg `0.005719`, median `0.015404`, mae `0.034535`
- 60d: sample `80`, hit `0.5875`, avg `0.022988`, median `0.03283`, mae `0.060465`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001826`, median `0.003952`, mae `0.013342`
- 5d: sample `40`, hit `0.475`, avg `0.0002`, median `-0.001324`, mae `0.015767`
- 10d: sample `40`, hit `0.525`, avg `0.004721`, median `0.00479`, mae `0.020099`
- 20d: sample `40`, hit `0.675`, avg `0.010931`, median `0.017881`, mae `0.031107`
- 60d: sample `40`, hit `0.7`, avg `0.039427`, median `0.052998`, mae `0.066904`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003775`, median `0.004569`, mae `0.013554`
- 5d: sample `80`, hit `0.625`, avg `0.004915`, median `0.005327`, mae `0.016347`
- 10d: sample `80`, hit `0.5875`, avg `0.006102`, median `0.006913`, mae `0.02153`
- 20d: sample `80`, hit `0.675`, avg `0.005719`, median `0.015404`, mae `0.034535`
- 60d: sample `80`, hit `0.5875`, avg `0.022988`, median `0.03283`, mae `0.060465`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001826`, median `0.003952`, mae `0.013342`
- 5d: sample `40`, hit `0.475`, avg `0.0002`, median `-0.001324`, mae `0.015767`
- 10d: sample `40`, hit `0.525`, avg `0.004721`, median `0.00479`, mae `0.020099`
- 20d: sample `40`, hit `0.675`, avg `0.010931`, median `0.017881`, mae `0.031107`
- 60d: sample `40`, hit `0.7`, avg `0.039427`, median `0.052998`, mae `0.066904`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `1.4e-05`, median `0.000145`, mae `0.013611`
- 5d: sample `40`, hit `0.525`, avg `-0.000205`, median `0.002694`, mae `0.015777`
- 10d: sample `40`, hit `0.575`, avg `0.005657`, median `0.007467`, mae `0.016719`
- 20d: sample `40`, hit `0.775`, avg `0.014007`, median `0.02086`, mae `0.028817`
- 60d: sample `40`, hit `0.55`, avg `0.015953`, median `0.029831`, mae `0.060328`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007536`, median `0.008815`, mae `0.013496`
- 5d: sample `40`, hit `0.725`, avg `0.010036`, median `0.009832`, mae `0.016916`
- 10d: sample `40`, hit `0.6`, avg `0.006547`, median `0.006913`, mae `0.026341`
- 20d: sample `40`, hit `0.575`, avg `-0.002568`, median `0.00514`, mae `0.040254`
- 60d: sample `40`, hit `0.625`, avg `0.030023`, median `0.046677`, mae `0.060603`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `1.4e-05`, median `0.000145`, mae `0.013611`
- 5d: sample `40`, hit `0.525`, avg `-0.000205`, median `0.002694`, mae `0.015777`
- 10d: sample `40`, hit `0.575`, avg `0.005657`, median `0.007467`, mae `0.016719`
- 20d: sample `40`, hit `0.775`, avg `0.014007`, median `0.02086`, mae `0.028817`
- 60d: sample `40`, hit `0.55`, avg `0.015953`, median `0.029831`, mae `0.060328`

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
- 3d: sample `80`, hit `0.6125`, avg `0.003775`, median `0.004569`, mae `0.013554`
- 5d: sample `80`, hit `0.625`, avg `0.004915`, median `0.005327`, mae `0.016347`
- 10d: sample `80`, hit `0.5875`, avg `0.006102`, median `0.006913`, mae `0.02153`
- 20d: sample `80`, hit `0.675`, avg `0.005719`, median `0.015404`, mae `0.034535`
- 60d: sample `80`, hit `0.5875`, avg `0.022988`, median `0.03283`, mae `0.060465`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003775`, median `0.004569`, mae `0.013554`
- 5d: sample `80`, hit `0.625`, avg `0.004915`, median `0.005327`, mae `0.016347`
- 10d: sample `80`, hit `0.5875`, avg `0.006102`, median `0.006913`, mae `0.02153`
- 20d: sample `80`, hit `0.675`, avg `0.005719`, median `0.015404`, mae `0.034535`
- 60d: sample `80`, hit `0.5875`, avg `0.022988`, median `0.03283`, mae `0.060465`

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
