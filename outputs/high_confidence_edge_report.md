# High Confidence Edge Report

Generated at: `2026-08-28T12:50:58.881522+00:00`

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
- 3d: sample `80`, hit `0.55`, avg `0.000302`, median `0.002329`, mae `0.015519`
- 5d: sample `80`, hit `0.5375`, avg `-2.6e-05`, median `0.001239`, mae `0.018508`
- 10d: sample `80`, hit `0.45`, avg `0.000362`, median `-0.007011`, mae `0.026356`
- 20d: sample `80`, hit `0.65`, avg `0.006331`, median `0.018139`, mae `0.036983`
- 60d: sample `80`, hit `0.65`, avg `0.02914`, median `0.028986`, mae `0.061525`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006581`, median `0.001558`, mae `0.011047`
- 5d: sample `8`, hit `0.375`, avg `-0.0078`, median `-0.012956`, mae `0.014858`
- 10d: sample `8`, hit `0.625`, avg `0.005104`, median `0.019233`, mae `0.020541`
- 20d: sample `8`, hit `0.875`, avg `0.014801`, median `0.029166`, mae `0.02663`
- 60d: sample `8`, hit `0.75`, avg `0.038143`, median `0.059495`, mae `0.067965`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006581`, median `0.001558`, mae `0.011047`
- 5d: sample `8`, hit `0.375`, avg `-0.0078`, median `-0.012956`, mae `0.014858`
- 10d: sample `8`, hit `0.625`, avg `0.005104`, median `0.019233`, mae `0.020541`
- 20d: sample `8`, hit `0.875`, avg `0.014801`, median `0.029166`, mae `0.02663`
- 60d: sample `8`, hit `0.75`, avg `0.038143`, median `0.059495`, mae `0.067965`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.000302, 'median_return': 0.002329, 'mean_absolute_return': 0.015519, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': -2.6e-05, 'median_return': 0.001239, 'mean_absolute_return': 0.018508, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': 0.000362, 'median_return': -0.007011, 'mean_absolute_return': 0.026356, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.006331, 'median_return': 0.018139, 'mean_absolute_return': 0.036983, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.02914, 'median_return': 0.028986, 'mean_absolute_return': 0.061525, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006581, 'median_return': 0.001558, 'mean_absolute_return': 0.011047, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.0078, 'median_return': -0.012956, 'mean_absolute_return': 0.014858, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005104, 'median_return': 0.019233, 'mean_absolute_return': 0.020541, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.014801, 'median_return': 0.029166, 'mean_absolute_return': 0.02663, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.038143, 'median_return': 0.059495, 'mean_absolute_return': 0.067965, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001066, 'median_return': 0.003026, 'mean_absolute_return': 0.016016, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.000838, 'median_return': 0.001695, 'mean_absolute_return': 0.018914, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.000165, 'median_return': -0.007117, 'mean_absolute_return': 0.027002, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.00539, 'median_return': 0.017881, 'mean_absolute_return': 0.038133, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.028139, 'median_return': 0.022085, 'mean_absolute_return': 0.060809, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.65}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 24, 'both_miss': 16}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.05, 'both_hit': 21, 'both_miss': 19}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.125, 'both_hit': 21, 'both_miss': 19}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.1, 'both_hit': 28, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.075, 'both_hit': 29, 'both_miss': 11}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.000302, 'median_return': 0.002329, 'mean_absolute_return': 0.015519, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': -2.6e-05, 'median_return': 0.001239, 'mean_absolute_return': 0.018508, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': 0.000362, 'median_return': -0.007011, 'mean_absolute_return': 0.026356, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.006331, 'median_return': 0.018139, 'mean_absolute_return': 0.036983, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.02914, 'median_return': 0.028986, 'mean_absolute_return': 0.061525, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00054`, median `0.002067`, mae `0.014767`
- 5d: sample `60`, hit `0.5333`, avg `-0.000898`, median `0.000873`, mae `0.018288`
- 10d: sample `60`, hit `0.45`, avg `0.000887`, median `-0.007011`, mae `0.026731`
- 20d: sample `60`, hit `0.65`, avg `0.00709`, median `0.020068`, mae `0.038183`
- 60d: sample `60`, hit `0.7`, avg `0.041054`, median `0.049712`, mae `0.066776`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.00054`, median `0.002067`, mae `0.014767`
- 5d: sample `60`, hit `0.5333`, avg `-0.000898`, median `0.000873`, mae `0.018288`
- 10d: sample `60`, hit `0.45`, avg `0.000887`, median `-0.007011`, mae `0.026731`
- 20d: sample `60`, hit `0.65`, avg `0.00709`, median `0.020068`, mae `0.038183`
- 60d: sample `60`, hit `0.7`, avg `0.041054`, median `0.049712`, mae `0.066776`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003809`, median `0.001558`, mae `0.014221`
- 5d: sample `20`, hit `0.45`, avg `-0.004774`, median `-0.004438`, mae `0.016219`
- 10d: sample `20`, hit `0.45`, avg `0.00238`, median `-0.006017`, mae `0.02213`
- 20d: sample `20`, hit `0.75`, avg `0.01779`, median `0.029166`, mae `0.035366`
- 60d: sample `20`, hit `0.65`, avg `0.035029`, median `0.059495`, mae `0.072298`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.000302`, median `0.002329`, mae `0.015519`
- 5d: sample `80`, hit `0.5375`, avg `-2.6e-05`, median `0.001239`, mae `0.018508`
- 10d: sample `80`, hit `0.45`, avg `0.000362`, median `-0.007011`, mae `0.026356`
- 20d: sample `80`, hit `0.65`, avg `0.006331`, median `0.018139`, mae `0.036983`
- 60d: sample `80`, hit `0.65`, avg `0.02914`, median `0.028986`, mae `0.061525`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.000302`, median `0.002329`, mae `0.015519`
- 5d: sample `80`, hit `0.5375`, avg `-2.6e-05`, median `0.001239`, mae `0.018508`
- 10d: sample `80`, hit `0.45`, avg `0.000362`, median `-0.007011`, mae `0.026356`
- 20d: sample `80`, hit `0.65`, avg `0.006331`, median `0.018139`, mae `0.036983`
- 60d: sample `80`, hit `0.65`, avg `0.02914`, median `0.028986`, mae `0.061525`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.000302`, median `0.002329`, mae `0.015519`
- 5d: sample `80`, hit `0.5375`, avg `-2.6e-05`, median `0.001239`, mae `0.018508`
- 10d: sample `80`, hit `0.45`, avg `0.000362`, median `-0.007011`, mae `0.026356`
- 20d: sample `80`, hit `0.65`, avg `0.006331`, median `0.018139`, mae `0.036983`
- 60d: sample `80`, hit `0.65`, avg `0.02914`, median `0.028986`, mae `0.061525`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.000302`, median `0.002329`, mae `0.015519`
- 5d: sample `80`, hit `0.5375`, avg `-2.6e-05`, median `0.001239`, mae `0.018508`
- 10d: sample `80`, hit `0.45`, avg `0.000362`, median `-0.007011`, mae `0.026356`
- 20d: sample `80`, hit `0.65`, avg `0.006331`, median `0.018139`, mae `0.036983`
- 60d: sample `80`, hit `0.65`, avg `0.02914`, median `0.028986`, mae `0.061525`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.000302`, median `0.002329`, mae `0.015519`
- 5d: sample `80`, hit `0.5375`, avg `-2.6e-05`, median `0.001239`, mae `0.018508`
- 10d: sample `80`, hit `0.45`, avg `0.000362`, median `-0.007011`, mae `0.026356`
- 20d: sample `80`, hit `0.65`, avg `0.006331`, median `0.018139`, mae `0.036983`
- 60d: sample `80`, hit `0.65`, avg `0.02914`, median `0.028986`, mae `0.061525`

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
