# High Confidence Edge Report

Generated at: `2026-07-09T15:37:24.312763+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001963`, median `0.001558`, mae `0.013615`
- 5d: sample `40`, hit `0.475`, avg `-0.004745`, median `-0.000371`, mae `0.016333`
- 10d: sample `40`, hit `0.475`, avg `0.003836`, median `-0.0004`, mae `0.018162`
- 20d: sample `40`, hit `0.7`, avg `0.011784`, median `0.017881`, mae `0.030477`
- 60d: sample `40`, hit `0.675`, avg `0.03347`, median `0.052998`, mae `0.065432`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.00053`, median `-0.001166`, mae `0.011125`
- 5d: sample `40`, hit `0.525`, avg `-0.001271`, median `0.000873`, mae `0.015272`
- 10d: sample `40`, hit `0.475`, avg `-0.001147`, median `-0.001676`, mae `0.023114`
- 20d: sample `40`, hit `0.65`, avg `-0.00292`, median `0.007676`, mae `0.033679`
- 60d: sample `40`, hit `0.425`, avg `-0.007156`, median `-0.01215`, mae `0.053363`

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
- 3d: sample `8`, hit `0.375`, avg `-0.014051`, median `-0.001658`, mae `0.015972`
- 5d: sample `8`, hit `0.25`, avg `-0.017492`, median `-0.013034`, mae `0.020876`
- 10d: sample `8`, hit `0.375`, avg `-0.006656`, median `-0.0004`, mae `0.018593`
- 20d: sample `8`, hit `0.875`, avg `0.01926`, median `0.031196`, mae `0.033086`
- 60d: sample `8`, hit `0.875`, avg `0.061772`, median `0.092646`, mae `0.07599`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.014051`, median `-0.001658`, mae `0.015972`
- 5d: sample `8`, hit `0.25`, avg `-0.017492`, median `-0.013034`, mae `0.020876`
- 10d: sample `8`, hit `0.375`, avg `-0.006656`, median `-0.0004`, mae `0.018593`
- 20d: sample `8`, hit `0.875`, avg `0.01926`, median `0.031196`, mae `0.033086`
- 60d: sample `8`, hit `0.875`, avg `0.061772`, median `0.092646`, mae `0.07599`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001963, 'median_return': 0.001558, 'mean_absolute_return': 0.013615, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.004745, 'median_return': -0.000371, 'mean_absolute_return': 0.016333, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.030501}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.003836, 'median_return': -0.0004, 'mean_absolute_return': 0.018162, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.011784, 'median_return': 0.017881, 'mean_absolute_return': 0.030477, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.077493}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.03347, 'median_return': 0.052998, 'mean_absolute_return': 0.065432, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.00053, 'median_return': -0.001166, 'mean_absolute_return': 0.011125, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001271, 'median_return': 0.000873, 'mean_absolute_return': 0.015272, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.001147, 'median_return': -0.001676, 'mean_absolute_return': 0.023114, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': -0.00292, 'median_return': 0.007676, 'mean_absolute_return': 0.033679, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.062475}, '60d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.007156, 'median_return': -0.01215, 'mean_absolute_return': 0.053363, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.087998}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.014051, 'median_return': -0.001658, 'mean_absolute_return': 0.015972, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.003785}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.017492, 'median_return': -0.013034, 'mean_absolute_return': 0.020876, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.006656, 'median_return': -0.0004, 'mean_absolute_return': 0.018593, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.020918}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.01926, 'median_return': 0.031196, 'mean_absolute_return': 0.033086, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.061772, 'median_return': 0.092646, 'mean_absolute_return': 0.07599, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.000176, 'median_return': 0.000324, 'mean_absolute_return': 0.01197, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.001398, 'median_return': 0.000688, 'mean_absolute_return': 0.015239, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.002234, 'median_return': -0.001222, 'mean_absolute_return': 0.020865, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.002785, 'median_return': 0.010788, 'mean_absolute_return': 0.031966, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.077493}, '60d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.007755, 'median_return': 0.010234, 'mean_absolute_return': 0.057554, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.55}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 41}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 40}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.0, 'both_hit': 38, 'both_miss': 42}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': 0.0, 'both_hit': 54, 'both_miss': 26}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 44, 'both_miss': 36}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001616, 'median_return': 0.003538, 'mean_absolute_return': 0.012025, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.000241, 'median_return': 0.00596, 'mean_absolute_return': 0.017198, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.030501}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.010729, 'median_return': 0.004067, 'mean_absolute_return': 0.01942, 'max_adverse_excursion': -0.024582, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005358, 'median_return': 0.009812, 'mean_absolute_return': 0.027768, 'max_adverse_excursion': -0.052049, 'max_favorable_excursion': 0.077493}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.022128, 'median_return': 0.045044, 'mean_absolute_return': 0.057306, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.120324}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.0022, 'median_return': -0.001428, 'mean_absolute_return': 0.012485, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.004091, 'median_return': -0.001796, 'mean_absolute_return': 0.015337, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.001783, 'median_return': -0.00676, 'mean_absolute_return': 0.021044, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.004124, 'median_return': 0.012958, 'mean_absolute_return': 0.033515, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.010167, 'median_return': 0.012273, 'mean_absolute_return': 0.060095, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.001246`, median `-0.000317`, mae `0.01237`
- 5d: sample `80`, hit `0.5`, avg `-0.003008`, median `0.000208`, mae `0.015802`
- 10d: sample `80`, hit `0.475`, avg `0.001345`, median `-0.001222`, mae `0.020638`
- 20d: sample `80`, hit `0.675`, avg `0.004432`, median `0.011728`, mae `0.032078`
- 60d: sample `80`, hit `0.55`, avg `0.013157`, median `0.018072`, mae `0.059398`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.001246`, median `-0.000317`, mae `0.01237`
- 5d: sample `80`, hit `0.5`, avg `-0.003008`, median `0.000208`, mae `0.015802`
- 10d: sample `80`, hit `0.475`, avg `0.001345`, median `-0.001222`, mae `0.020638`
- 20d: sample `80`, hit `0.675`, avg `0.004432`, median `0.011728`, mae `0.032078`
- 60d: sample `80`, hit `0.55`, avg `0.013157`, median `0.018072`, mae `0.059398`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001963`, median `0.001558`, mae `0.013615`
- 5d: sample `40`, hit `0.475`, avg `-0.004745`, median `-0.000371`, mae `0.016333`
- 10d: sample `40`, hit `0.475`, avg `0.003836`, median `-0.0004`, mae `0.018162`
- 20d: sample `40`, hit `0.7`, avg `0.011784`, median `0.017881`, mae `0.030477`
- 60d: sample `40`, hit `0.675`, avg `0.03347`, median `0.052998`, mae `0.065432`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.001246`, median `-0.000317`, mae `0.01237`
- 5d: sample `80`, hit `0.5`, avg `-0.003008`, median `0.000208`, mae `0.015802`
- 10d: sample `80`, hit `0.475`, avg `0.001345`, median `-0.001222`, mae `0.020638`
- 20d: sample `80`, hit `0.675`, avg `0.004432`, median `0.011728`, mae `0.032078`
- 60d: sample `80`, hit `0.55`, avg `0.013157`, median `0.018072`, mae `0.059398`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001963`, median `0.001558`, mae `0.013615`
- 5d: sample `40`, hit `0.475`, avg `-0.004745`, median `-0.000371`, mae `0.016333`
- 10d: sample `40`, hit `0.475`, avg `0.003836`, median `-0.0004`, mae `0.018162`
- 20d: sample `40`, hit `0.7`, avg `0.011784`, median `0.017881`, mae `0.030477`
- 60d: sample `40`, hit `0.675`, avg `0.03347`, median `0.052998`, mae `0.065432`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002111`, median `-0.001166`, mae `0.007194`
- 5d: sample `20`, hit `0.6`, avg `-0.001629`, median `0.001303`, mae `0.010554`
- 10d: sample `20`, hit `0.35`, avg `-0.005448`, median `-0.007491`, mae `0.016413`
- 20d: sample `20`, hit `0.55`, avg `-0.003524`, median `0.007004`, mae `0.02521`
- 60d: sample `20`, hit `0.35`, avg `-0.014933`, median `-0.020815`, mae `0.050522`

### mixed_internal_resonance
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.000958`, median `0.000324`, mae `0.014095`
- 5d: sample `60`, hit `0.4667`, avg `-0.003467`, median `-0.001324`, mae `0.017552`
- 10d: sample `60`, hit `0.5167`, avg `0.003609`, median `0.00273`, mae `0.022046`
- 20d: sample `60`, hit `0.7167`, avg `0.007084`, median `0.014918`, mae `0.034367`
- 60d: sample `60`, hit `0.6167`, avg `0.02252`, median `0.037425`, mae `0.062356`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002111`, median `-0.001166`, mae `0.007194`
- 5d: sample `20`, hit `0.6`, avg `-0.001629`, median `0.001303`, mae `0.010554`
- 10d: sample `20`, hit `0.35`, avg `-0.005448`, median `-0.007491`, mae `0.016413`
- 20d: sample `20`, hit `0.55`, avg `-0.003524`, median `0.007004`, mae `0.02521`
- 60d: sample `20`, hit `0.35`, avg `-0.014933`, median `-0.020815`, mae `0.050522`

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
