# High Confidence Edge Report

Generated at: `2026-08-18T23:33:49.123855+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `40`
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
- 3d: sample `20`, hit `0.45`, avg `-0.008136`, median `-0.005488`, mae `0.016267`
- 5d: sample `20`, hit `0.45`, avg `-0.008622`, median `-0.002525`, mae `0.015219`
- 10d: sample `20`, hit `0.4`, avg `-0.00779`, median `-0.007011`, mae `0.020844`
- 20d: sample `20`, hit `0.6`, avg `-0.008311`, median `0.009259`, mae `0.038529`
- 60d: sample `20`, hit `0.45`, avg `-0.006407`, median `-0.004982`, mae `0.066518`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001069`, median `0.000603`, mae `0.010641`
- 5d: sample `20`, hit `0.65`, avg `-0.000319`, median `0.001303`, mae `0.011472`
- 10d: sample `20`, hit `0.25`, avg `-0.010985`, median `-0.01051`, mae `0.019065`
- 20d: sample `20`, hit `0.25`, avg `-0.01956`, median `-0.009023`, mae `0.033523`
- 60d: sample `20`, hit `0.4`, avg `-0.008795`, median `-0.005534`, mae `0.044392`

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
- sample_size: `4`
- 3d: sample `4`, hit `0.75`, avg `0.000689`, median `0.009229`, mae `0.015939`
- 5d: sample `4`, hit `0.75`, avg `0.000861`, median `0.013852`, mae `0.016675`
- 10d: sample `4`, hit `0.75`, avg `0.013584`, median `0.024811`, mae `0.022564`
- 20d: sample `4`, hit `0.5`, avg `0.017351`, median `0.029166`, mae `0.028709`
- 60d: sample `4`, hit `0.5`, avg `0.012383`, median `0.046132`, mae `0.054235`

### confidence_score top 10%
- sample_size: `4`
- 3d: sample `4`, hit `0.75`, avg `0.000689`, median `0.009229`, mae `0.015939`
- 5d: sample `4`, hit `0.75`, avg `0.000861`, median `0.013852`, mae `0.016675`
- 10d: sample `4`, hit `0.75`, avg `0.013584`, median `0.024811`, mae `0.022564`
- 20d: sample `4`, hit `0.5`, avg `0.017351`, median `0.029166`, mae `0.028709`
- 60d: sample `4`, hit `0.5`, avg `0.012383`, median `0.046132`, mae `0.054235`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.008136, 'median_return': -0.005488, 'mean_absolute_return': 0.016267, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.008622, 'median_return': -0.002525, 'mean_absolute_return': 0.015219, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.00779, 'median_return': -0.007011, 'mean_absolute_return': 0.020844, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.008311, 'median_return': 0.009259, 'mean_absolute_return': 0.038529, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.006407, 'median_return': -0.004982, 'mean_absolute_return': 0.066518, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.101282}}}, 'confidence_top_10': {'sample_size': 4, 'by_horizon': {'3d': {'sample_size': 4, 'hit_rate': 0.75, 'avg_return': 0.000689, 'median_return': 0.009229, 'mean_absolute_return': 0.015939, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 4, 'hit_rate': 0.75, 'avg_return': 0.000861, 'median_return': 0.013852, 'mean_absolute_return': 0.016675, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 4, 'hit_rate': 0.75, 'avg_return': 0.013584, 'median_return': 0.024811, 'mean_absolute_return': 0.022564, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 4, 'hit_rate': 0.5, 'avg_return': 0.017351, 'median_return': 0.029166, 'mean_absolute_return': 0.028709, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 4, 'hit_rate': 0.5, 'avg_return': 0.012383, 'median_return': 0.046132, 'mean_absolute_return': 0.054235, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 36, 'by_horizon': {'3d': {'sample_size': 36, 'hit_rate': 0.4722, 'avg_return': -0.00519, 'median_return': -0.001428, 'mean_absolute_return': 0.013178, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 36, 'hit_rate': 0.5278, 'avg_return': -0.005063, 'median_return': 0.000688, 'mean_absolute_return': 0.012976, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 36, 'hit_rate': 0.2778, 'avg_return': -0.01194, 'median_return': -0.012383, 'mean_absolute_return': 0.019664, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.02188}, '20d': {'sample_size': 36, 'hit_rate': 0.4167, 'avg_return': -0.017412, 'median_return': -0.004441, 'mean_absolute_return': 0.036839, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.039296}, '60d': {'sample_size': 36, 'hit_rate': 0.4167, 'avg_return': -0.009821, 'median_return': -0.005534, 'mean_absolute_return': 0.05559, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.101282}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 40, 'hit_rate': 0.5}, '5d': {'sample_size': 40, 'hit_rate': 0.45}, '10d': {'sample_size': 40, 'hit_rate': 0.675}, '20d': {'sample_size': 40, 'hit_rate': 0.575}, '60d': {'sample_size': 40, 'hit_rate': 0.575}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 40, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 40, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 40, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.325, 'primary_minus_secondary': 0.35, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 40, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 40, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.004602, 'median_return': 0.000201, 'mean_absolute_return': 0.013454, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.004471, 'median_return': 0.000762, 'mean_absolute_return': 0.013346, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.009387, 'median_return': -0.01051, 'mean_absolute_return': 0.019954, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.013936, 'median_return': -0.004441, 'mean_absolute_return': 0.036026, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.007601, 'median_return': -0.005534, 'mean_absolute_return': 0.055455, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.101282}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.004602`, median `0.000201`, mae `0.013454`
- 5d: sample `40`, hit `0.55`, avg `-0.004471`, median `0.000762`, mae `0.013346`
- 10d: sample `40`, hit `0.325`, avg `-0.009387`, median `-0.01051`, mae `0.019954`
- 20d: sample `40`, hit `0.425`, avg `-0.013936`, median `-0.004441`, mae `0.036026`
- 60d: sample `40`, hit `0.425`, avg `-0.007601`, median `-0.005534`, mae `0.055455`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.004602`, median `0.000201`, mae `0.013454`
- 5d: sample `40`, hit `0.55`, avg `-0.004471`, median `0.000762`, mae `0.013346`
- 10d: sample `40`, hit `0.325`, avg `-0.009387`, median `-0.01051`, mae `0.019954`
- 20d: sample `40`, hit `0.425`, avg `-0.013936`, median `-0.004441`, mae `0.036026`
- 60d: sample `40`, hit `0.425`, avg `-0.007601`, median `-0.005534`, mae `0.055455`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.004602`, median `0.000201`, mae `0.013454`
- 5d: sample `40`, hit `0.55`, avg `-0.004471`, median `0.000762`, mae `0.013346`
- 10d: sample `40`, hit `0.325`, avg `-0.009387`, median `-0.01051`, mae `0.019954`
- 20d: sample `40`, hit `0.425`, avg `-0.013936`, median `-0.004441`, mae `0.036026`
- 60d: sample `40`, hit `0.425`, avg `-0.007601`, median `-0.005534`, mae `0.055455`

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
