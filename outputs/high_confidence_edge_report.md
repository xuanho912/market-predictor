# High Confidence Edge Report

Generated at: `2026-07-31T04:46:19.369332+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003632`, median `0.001558`, mae `0.017602`
- 5d: sample `20`, hit `0.5`, avg `-0.006515`, median `0.000415`, mae `0.019243`
- 10d: sample `20`, hit `0.35`, avg `-0.00105`, median `-0.006017`, mae `0.018293`
- 20d: sample `20`, hit `0.65`, avg `0.018438`, median `0.029166`, mae `0.038839`
- 60d: sample `20`, hit `0.7`, avg `0.036923`, median `0.046132`, mae `0.071246`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.00399`, median `0.002067`, mae `0.013907`
- 5d: sample `60`, hit `0.6167`, avg `0.005022`, median `0.0019`, mae `0.017318`
- 10d: sample `60`, hit `0.5`, avg `0.0027`, median `0.000254`, mae `0.028512`
- 20d: sample `60`, hit `0.6167`, avg `0.009831`, median `0.015444`, mae `0.046231`
- 60d: sample `60`, hit `0.5167`, avg `0.00639`, median `0.016177`, mae `0.080672`

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
- 3d: sample `8`, hit `0.375`, avg `-0.014537`, median `-0.009383`, mae `0.017746`
- 5d: sample `8`, hit `0.25`, avg `-0.02117`, median `-0.016062`, mae `0.022879`
- 10d: sample `8`, hit `0.125`, avg `-0.010848`, median `-0.007755`, mae `0.015656`
- 20d: sample `8`, hit `0.625`, avg `0.006054`, median `0.020068`, mae `0.033882`
- 60d: sample `8`, hit `0.625`, avg `0.027723`, median `0.046132`, mae `0.063035`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.014537`, median `-0.009383`, mae `0.017746`
- 5d: sample `8`, hit `0.25`, avg `-0.02117`, median `-0.016062`, mae `0.022879`
- 10d: sample `8`, hit `0.125`, avg `-0.010848`, median `-0.007755`, mae `0.015656`
- 20d: sample `8`, hit `0.625`, avg `0.006054`, median `0.020068`, mae `0.033882`
- 60d: sample `8`, hit `0.625`, avg `0.027723`, median `0.046132`, mae `0.063035`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.003632, 'median_return': 0.001558, 'mean_absolute_return': 0.017602, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.029522}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.006515, 'median_return': 0.000415, 'mean_absolute_return': 0.019243, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.00105, 'median_return': -0.006017, 'mean_absolute_return': 0.018293, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.043492}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.018438, 'median_return': 0.029166, 'mean_absolute_return': 0.038839, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.036923, 'median_return': 0.046132, 'mean_absolute_return': 0.071246, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.014537, 'median_return': -0.009383, 'mean_absolute_return': 0.017746, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.02117, 'median_return': -0.016062, 'mean_absolute_return': 0.022879, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.003829}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.010848, 'median_return': -0.007755, 'mean_absolute_return': 0.015656, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006054, 'median_return': 0.020068, 'mean_absolute_return': 0.033882, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.027723, 'median_return': 0.046132, 'mean_absolute_return': 0.063035, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003931, 'median_return': 0.002067, 'mean_absolute_return': 0.014507, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.040779}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.004727, 'median_return': 0.002451, 'mean_absolute_return': 0.017235, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.003164, 'median_return': 0.000254, 'mean_absolute_return': 0.027102, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.012641, 'median_return': 0.017237, 'mean_absolute_return': 0.04555, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.012501, 'median_return': 0.027637, 'mean_absolute_return': 0.080013, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.15, 'both_hit': 11, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 10, 'both_miss': 10}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.0, 'both_hit': 7, 'both_miss': 13}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.175, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.025, 'both_hit': 14, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.00399, 'median_return': 0.002067, 'mean_absolute_return': 0.013907, 'max_adverse_excursion': -0.0325, 'max_favorable_excursion': 0.040779}, '5d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.005022, 'median_return': 0.0019, 'mean_absolute_return': 0.017318, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.0027, 'median_return': 0.000254, 'mean_absolute_return': 0.028512, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.009831, 'median_return': 0.015444, 'mean_absolute_return': 0.046231, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.00639, 'median_return': 0.016177, 'mean_absolute_return': 0.080672, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21366}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.003632, 'median_return': 0.001558, 'mean_absolute_return': 0.017602, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.029522}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.006515, 'median_return': 0.000415, 'mean_absolute_return': 0.019243, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.00105, 'median_return': -0.006017, 'mean_absolute_return': 0.018293, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.043492}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.018438, 'median_return': 0.029166, 'mean_absolute_return': 0.038839, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.036923, 'median_return': 0.046132, 'mean_absolute_return': 0.071246, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002515`, median `0.000603`, mae `0.014733`
- 5d: sample `40`, hit `0.55`, avg `-0.004593`, median `0.000762`, mae `0.01449`
- 10d: sample `40`, hit `0.275`, avg `-0.007728`, median `-0.01051`, mae `0.01814`
- 20d: sample `40`, hit `0.4`, avg `-0.001804`, median `-0.003522`, mae `0.034462`
- 60d: sample `40`, hit `0.5`, avg `0.01246`, median `8.1e-05`, mae `0.056333`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.006684`, median `0.009701`, mae `0.014928`
- 5d: sample `40`, hit `0.625`, avg `0.008868`, median `0.006838`, mae `0.021109`
- 10d: sample `40`, hit `0.65`, avg `0.011253`, median `0.01795`, mae `0.033774`
- 20d: sample `40`, hit `0.85`, avg `0.025769`, median `0.038303`, mae `0.054305`
- 60d: sample `40`, hit `0.625`, avg `0.015588`, median `0.048484`, mae `0.100298`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003632`, median `0.001558`, mae `0.017602`
- 5d: sample `20`, hit `0.5`, avg `-0.006515`, median `0.000415`, mae `0.019243`
- 10d: sample `20`, hit `0.35`, avg `-0.00105`, median `-0.006017`, mae `0.018293`
- 20d: sample `20`, hit `0.65`, avg `0.018438`, median `0.029166`, mae `0.038839`
- 60d: sample `20`, hit `0.7`, avg `0.036923`, median `0.046132`, mae `0.071246`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003632`, median `0.001558`, mae `0.017602`
- 5d: sample `20`, hit `0.5`, avg `-0.006515`, median `0.000415`, mae `0.019243`
- 10d: sample `20`, hit `0.35`, avg `-0.00105`, median `-0.006017`, mae `0.018293`
- 20d: sample `20`, hit `0.65`, avg `0.018438`, median `0.029166`, mae `0.038839`
- 60d: sample `20`, hit `0.7`, avg `0.036923`, median `0.046132`, mae `0.071246`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003632`, median `0.001558`, mae `0.017602`
- 5d: sample `20`, hit `0.5`, avg `-0.006515`, median `0.000415`, mae `0.019243`
- 10d: sample `20`, hit `0.35`, avg `-0.00105`, median `-0.006017`, mae `0.018293`
- 20d: sample `20`, hit `0.65`, avg `0.018438`, median `0.029166`, mae `0.038839`
- 60d: sample `20`, hit `0.7`, avg `0.036923`, median `0.046132`, mae `0.071246`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003632`, median `0.001558`, mae `0.017602`
- 5d: sample `20`, hit `0.5`, avg `-0.006515`, median `0.000415`, mae `0.019243`
- 10d: sample `20`, hit `0.35`, avg `-0.00105`, median `-0.006017`, mae `0.018293`
- 20d: sample `20`, hit `0.65`, avg `0.018438`, median `0.029166`, mae `0.038839`
- 60d: sample `20`, hit `0.7`, avg `0.036923`, median `0.046132`, mae `0.071246`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.006684`, median `0.009701`, mae `0.014928`
- 5d: sample `40`, hit `0.625`, avg `0.008868`, median `0.006838`, mae `0.021109`
- 10d: sample `40`, hit `0.65`, avg `0.011253`, median `0.01795`, mae `0.033774`
- 20d: sample `40`, hit `0.85`, avg `0.025769`, median `0.038303`, mae `0.054305`
- 60d: sample `40`, hit `0.625`, avg `0.015588`, median `0.048484`, mae `0.100298`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002084`, median `0.001558`, mae `0.014831`
- 5d: sample `80`, hit `0.5875`, avg `0.002137`, median `0.001695`, mae `0.017799`
- 10d: sample `80`, hit `0.4625`, avg `0.001763`, median `-0.002045`, mae `0.025957`
- 20d: sample `80`, hit `0.625`, avg `0.011983`, median `0.017237`, mae `0.044383`
- 60d: sample `80`, hit `0.5625`, avg `0.014024`, median `0.027637`, mae `0.078315`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003632`, median `0.001558`, mae `0.017602`
- 5d: sample `20`, hit `0.5`, avg `-0.006515`, median `0.000415`, mae `0.019243`
- 10d: sample `20`, hit `0.35`, avg `-0.00105`, median `-0.006017`, mae `0.018293`
- 20d: sample `20`, hit `0.65`, avg `0.018438`, median `0.029166`, mae `0.038839`
- 60d: sample `20`, hit `0.7`, avg `0.036923`, median `0.046132`, mae `0.071246`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003245`, median `0.003785`, mae `0.01582`
- 5d: sample `60`, hit `0.5833`, avg `0.00374`, median `0.003829`, mae `0.020487`
- 10d: sample `60`, hit `0.55`, avg `0.007152`, median `0.008202`, mae `0.028614`
- 20d: sample `60`, hit `0.7833`, avg `0.023326`, median `0.03392`, mae `0.049149`
- 60d: sample `60`, hit `0.65`, avg `0.0227`, median `0.046132`, mae `0.090614`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003632`, median `0.001558`, mae `0.017602`
- 5d: sample `20`, hit `0.5`, avg `-0.006515`, median `0.000415`, mae `0.019243`
- 10d: sample `20`, hit `0.35`, avg `-0.00105`, median `-0.006017`, mae `0.018293`
- 20d: sample `20`, hit `0.65`, avg `0.018438`, median `0.029166`, mae `0.038839`
- 60d: sample `20`, hit `0.7`, avg `0.036923`, median `0.046132`, mae `0.071246`

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
