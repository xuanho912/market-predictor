# High Confidence Edge Report

Generated at: `2026-06-15T15:11:16.400719+00:00`

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
- 3d: sample `80`, hit `0.6375`, avg `0.00465`, median `0.005458`, mae `0.01376`
- 5d: sample `80`, hit `0.6375`, avg `0.00584`, median `0.005327`, mae `0.017287`
- 10d: sample `80`, hit `0.6125`, avg `0.008005`, median `0.0076`, mae `0.022232`
- 20d: sample `80`, hit `0.7`, avg `0.009334`, median `0.017881`, mae `0.036062`
- 60d: sample `80`, hit `0.6`, avg `0.027594`, median `0.032982`, mae `0.062297`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006411`, median `0.001558`, mae `0.014382`
- 5d: sample `8`, hit `0.25`, avg `-0.007563`, median `-0.007788`, mae `0.017861`
- 10d: sample `8`, hit `0.75`, avg `0.008453`, median `0.0076`, mae `0.014633`
- 20d: sample `8`, hit `0.875`, avg `0.023947`, median `0.029166`, mae `0.025842`
- 60d: sample `8`, hit `0.75`, avg `0.037866`, median `0.046132`, mae `0.052474`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006411`, median `0.001558`, mae `0.014382`
- 5d: sample `8`, hit `0.25`, avg `-0.007563`, median `-0.007788`, mae `0.017861`
- 10d: sample `8`, hit `0.75`, avg `0.008453`, median `0.0076`, mae `0.014633`
- 20d: sample `8`, hit `0.875`, avg `0.023947`, median `0.029166`, mae `0.025842`
- 60d: sample `8`, hit `0.75`, avg `0.037866`, median `0.046132`, mae `0.052474`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.00465, 'median_return': 0.005458, 'mean_absolute_return': 0.01376, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.00584, 'median_return': 0.005327, 'mean_absolute_return': 0.017287, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.008005, 'median_return': 0.0076, 'mean_absolute_return': 0.022232, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.009334, 'median_return': 0.017881, 'mean_absolute_return': 0.036062, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.027594, 'median_return': 0.032982, 'mean_absolute_return': 0.062297, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006411, 'median_return': 0.001558, 'mean_absolute_return': 0.014382, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.007563, 'median_return': -0.007788, 'mean_absolute_return': 0.017861, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008453, 'median_return': 0.0076, 'mean_absolute_return': 0.014633, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.023947, 'median_return': 0.029166, 'mean_absolute_return': 0.025842, 'max_adverse_excursion': -0.007581, 'max_favorable_excursion': 0.037283}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.037866, 'median_return': 0.046132, 'mean_absolute_return': 0.052474, 'max_adverse_excursion': -0.038302, 'max_favorable_excursion': 0.094627}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.005879, 'median_return': 0.006228, 'mean_absolute_return': 0.013691, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.007329, 'median_return': 0.00596, 'mean_absolute_return': 0.017223, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.007955, 'median_return': 0.00903, 'mean_absolute_return': 0.023077, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.007711, 'median_return': 0.016175, 'mean_absolute_return': 0.037198, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.026452, 'median_return': 0.032982, 'mean_absolute_return': 0.063389, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.7}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.0, 'both_hit': 56, 'both_miss': 24}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.00465, 'median_return': 0.005458, 'mean_absolute_return': 0.01376, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.00584, 'median_return': 0.005327, 'mean_absolute_return': 0.017287, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.008005, 'median_return': 0.0076, 'mean_absolute_return': 0.022232, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.009334, 'median_return': 0.017881, 'mean_absolute_return': 0.036062, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.027594, 'median_return': 0.032982, 'mean_absolute_return': 0.062297, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.00465`, median `0.005458`, mae `0.01376`
- 5d: sample `80`, hit `0.6375`, avg `0.00584`, median `0.005327`, mae `0.017287`
- 10d: sample `80`, hit `0.6125`, avg `0.008005`, median `0.0076`, mae `0.022232`
- 20d: sample `80`, hit `0.7`, avg `0.009334`, median `0.017881`, mae `0.036062`
- 60d: sample `80`, hit `0.6`, avg `0.027594`, median `0.032982`, mae `0.062297`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.00465`, median `0.005458`, mae `0.01376`
- 5d: sample `80`, hit `0.6375`, avg `0.00584`, median `0.005327`, mae `0.017287`
- 10d: sample `80`, hit `0.6125`, avg `0.008005`, median `0.0076`, mae `0.022232`
- 20d: sample `80`, hit `0.7`, avg `0.009334`, median `0.017881`, mae `0.036062`
- 60d: sample `80`, hit `0.6`, avg `0.027594`, median `0.032982`, mae `0.062297`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.002946`, median `0.006228`, mae `0.013845`
- 5d: sample `40`, hit `0.5`, avg `0.00215`, median `0.000415`, mae `0.017748`
- 10d: sample `40`, hit `0.55`, avg `0.008018`, median `0.0076`, mae `0.021887`
- 20d: sample `40`, hit `0.7`, avg `0.016502`, median `0.022652`, mae `0.035015`
- 60d: sample `40`, hit `0.725`, avg `0.047252`, median `0.054765`, mae `0.071954`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.00465`, median `0.005458`, mae `0.01376`
- 5d: sample `80`, hit `0.6375`, avg `0.00584`, median `0.005327`, mae `0.017287`
- 10d: sample `80`, hit `0.6125`, avg `0.008005`, median `0.0076`, mae `0.022232`
- 20d: sample `80`, hit `0.7`, avg `0.009334`, median `0.017881`, mae `0.036062`
- 60d: sample `80`, hit `0.6`, avg `0.027594`, median `0.032982`, mae `0.062297`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.002946`, median `0.006228`, mae `0.013845`
- 5d: sample `40`, hit `0.5`, avg `0.00215`, median `0.000415`, mae `0.017748`
- 10d: sample `40`, hit `0.55`, avg `0.008018`, median `0.0076`, mae `0.021887`
- 20d: sample `40`, hit `0.7`, avg `0.016502`, median `0.022652`, mae `0.035015`
- 60d: sample `40`, hit `0.725`, avg `0.047252`, median `0.054765`, mae `0.071954`

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
- 3d: sample `40`, hit `0.525`, avg `0.000553`, median `0.001558`, mae `0.013494`
- 5d: sample `40`, hit `0.525`, avg `-0.000612`, median `0.000579`, mae `0.015658`
- 10d: sample `40`, hit `0.625`, avg `0.00739`, median `0.0076`, mae `0.016051`
- 20d: sample `40`, hit `0.825`, avg `0.018345`, median `0.02284`, mae `0.028979`
- 60d: sample `40`, hit `0.575`, avg `0.019441`, median `0.029917`, mae `0.058268`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.008748`, median `0.009928`, mae `0.014027`
- 5d: sample `40`, hit `0.75`, avg `0.012292`, median `0.01025`, mae `0.018915`
- 10d: sample `40`, hit `0.6`, avg `0.00862`, median `0.00903`, mae `0.028414`
- 20d: sample `40`, hit `0.575`, avg `0.000324`, median `0.005458`, mae `0.043146`
- 60d: sample `40`, hit `0.625`, avg `0.035747`, median `0.047759`, mae `0.066327`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000553`, median `0.001558`, mae `0.013494`
- 5d: sample `40`, hit `0.525`, avg `-0.000612`, median `0.000579`, mae `0.015658`
- 10d: sample `40`, hit `0.625`, avg `0.00739`, median `0.0076`, mae `0.016051`
- 20d: sample `40`, hit `0.825`, avg `0.018345`, median `0.02284`, mae `0.028979`
- 60d: sample `40`, hit `0.575`, avg `0.019441`, median `0.029917`, mae `0.058268`

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
- 3d: sample `80`, hit `0.6375`, avg `0.00465`, median `0.005458`, mae `0.01376`
- 5d: sample `80`, hit `0.6375`, avg `0.00584`, median `0.005327`, mae `0.017287`
- 10d: sample `80`, hit `0.6125`, avg `0.008005`, median `0.0076`, mae `0.022232`
- 20d: sample `80`, hit `0.7`, avg `0.009334`, median `0.017881`, mae `0.036062`
- 60d: sample `80`, hit `0.6`, avg `0.027594`, median `0.032982`, mae `0.062297`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.00465`, median `0.005458`, mae `0.01376`
- 5d: sample `80`, hit `0.6375`, avg `0.00584`, median `0.005327`, mae `0.017287`
- 10d: sample `80`, hit `0.6125`, avg `0.008005`, median `0.0076`, mae `0.022232`
- 20d: sample `80`, hit `0.7`, avg `0.009334`, median `0.017881`, mae `0.036062`
- 60d: sample `80`, hit `0.6`, avg `0.027594`, median `0.032982`, mae `0.062297`

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
