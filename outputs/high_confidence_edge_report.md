# High Confidence Edge Report

Generated at: `2026-07-07T15:17:51.051671+00:00`

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
- 3d: sample `40`, hit `0.425`, avg `-0.004529`, median `-0.006856`, mae `0.017879`
- 5d: sample `40`, hit `0.475`, avg `-0.004913`, median `-0.004438`, mae `0.018958`
- 10d: sample `40`, hit `0.5`, avg `0.002056`, median `0.001607`, mae `0.021552`
- 20d: sample `40`, hit `0.75`, avg `0.013478`, median `0.015661`, mae `0.033145`
- 60d: sample `40`, hit `0.625`, avg `0.026047`, median `0.029831`, mae `0.063806`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.001107`, median `-0.000317`, mae `0.009296`
- 5d: sample `40`, hit `0.55`, avg `-0.001287`, median `0.003026`, mae `0.013799`
- 10d: sample `40`, hit `0.5`, avg `0.001315`, median `0.000242`, mae `0.016574`
- 20d: sample `40`, hit `0.625`, avg `-0.000154`, median `0.01011`, mae `0.024105`
- 60d: sample `40`, hit `0.35`, avg `-0.014785`, median `-0.022357`, mae `0.053532`

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
- 3d: sample `8`, hit `0.125`, avg `-0.013768`, median `-0.010033`, mae `0.015446`
- 5d: sample `8`, hit `0.375`, avg `-0.011794`, median `-0.004438`, mae `0.015076`
- 10d: sample `8`, hit `0.0`, avg `-0.01387`, median `-0.010456`, mae `0.01387`
- 20d: sample `8`, hit `0.625`, avg `0.016823`, median `0.029166`, mae `0.040022`
- 60d: sample `8`, hit `0.625`, avg `0.026683`, median `0.046132`, mae `0.079296`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.013768`, median `-0.010033`, mae `0.015446`
- 5d: sample `8`, hit `0.375`, avg `-0.011794`, median `-0.004438`, mae `0.015076`
- 10d: sample `8`, hit `0.0`, avg `-0.01387`, median `-0.010456`, mae `0.01387`
- 20d: sample `8`, hit `0.625`, avg `0.016823`, median `0.029166`, mae `0.040022`
- 60d: sample `8`, hit `0.625`, avg `0.026683`, median `0.046132`, mae `0.079296`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.004529, 'median_return': -0.006856, 'mean_absolute_return': 0.017879, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.004913, 'median_return': -0.004438, 'mean_absolute_return': 0.018958, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.002056, 'median_return': 0.001607, 'mean_absolute_return': 0.021552, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.013478, 'median_return': 0.015661, 'mean_absolute_return': 0.033145, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.026047, 'median_return': 0.029831, 'mean_absolute_return': 0.063806, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.001107, 'median_return': -0.000317, 'mean_absolute_return': 0.009296, 'max_adverse_excursion': -0.03396, 'max_favorable_excursion': 0.025242}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.001287, 'median_return': 0.003026, 'mean_absolute_return': 0.013799, 'max_adverse_excursion': -0.058308, 'max_favorable_excursion': 0.023659}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.001315, 'median_return': 0.000242, 'mean_absolute_return': 0.016574, 'max_adverse_excursion': -0.054187, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.000154, 'median_return': 0.01011, 'mean_absolute_return': 0.024105, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.068982}, '60d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.014785, 'median_return': -0.022357, 'mean_absolute_return': 0.053532, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.105138}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.013768, 'median_return': -0.010033, 'mean_absolute_return': 0.015446, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011794, 'median_return': -0.004438, 'mean_absolute_return': 0.015076, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.01387, 'median_return': -0.010456, 'mean_absolute_return': 0.01387, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016823, 'median_return': 0.029166, 'mean_absolute_return': 0.040022, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026683, 'median_return': 0.046132, 'mean_absolute_return': 0.079296, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.001602, 'median_return': -0.000317, 'mean_absolute_return': 0.013381, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.002134, 'median_return': 0.003026, 'mean_absolute_return': 0.016523, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.003414, 'median_return': 0.003262, 'mean_absolute_return': 0.01964, 'max_adverse_excursion': -0.054187, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.005533, 'median_return': 0.010788, 'mean_absolute_return': 0.027359, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.003292, 'median_return': -0.005293, 'mean_absolute_return': 0.056377, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.4875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.0, 'both_hit': 36, 'both_miss': 44}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.0, 'both_hit': 41, 'both_miss': 39}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 40}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': 0.0, 'both_hit': 55, 'both_miss': 25}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 41}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.002818, 'median_return': -0.001658, 'mean_absolute_return': 0.013587, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.0031, 'median_return': 0.001695, 'mean_absolute_return': 0.016378, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': 0.001685, 'median_return': 0.000242, 'mean_absolute_return': 0.019063, 'max_adverse_excursion': -0.054187, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.006662, 'median_return': 0.01128, 'mean_absolute_return': 0.028625, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.005631, 'median_return': -0.001675, 'mean_absolute_return': 0.058669, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.002818`, median `-0.001658`, mae `0.013587`
- 5d: sample `80`, hit `0.5125`, avg `-0.0031`, median `0.001695`, mae `0.016378`
- 10d: sample `80`, hit `0.5`, avg `0.001685`, median `0.000242`, mae `0.019063`
- 20d: sample `80`, hit `0.6875`, avg `0.006662`, median `0.01128`, mae `0.028625`
- 60d: sample `80`, hit `0.4875`, avg `0.005631`, median `-0.001675`, mae `0.058669`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.002818`, median `-0.001658`, mae `0.013587`
- 5d: sample `80`, hit `0.5125`, avg `-0.0031`, median `0.001695`, mae `0.016378`
- 10d: sample `80`, hit `0.5`, avg `0.001685`, median `0.000242`, mae `0.019063`
- 20d: sample `80`, hit `0.6875`, avg `0.006662`, median `0.01128`, mae `0.028625`
- 60d: sample `80`, hit `0.4875`, avg `0.005631`, median `-0.001675`, mae `0.058669`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.004529`, median `-0.006856`, mae `0.017879`
- 5d: sample `40`, hit `0.475`, avg `-0.004913`, median `-0.004438`, mae `0.018958`
- 10d: sample `40`, hit `0.5`, avg `0.002056`, median `0.001607`, mae `0.021552`
- 20d: sample `40`, hit `0.75`, avg `0.013478`, median `0.015661`, mae `0.033145`
- 60d: sample `40`, hit `0.625`, avg `0.026047`, median `0.029831`, mae `0.063806`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.002818`, median `-0.001658`, mae `0.013587`
- 5d: sample `80`, hit `0.5125`, avg `-0.0031`, median `0.001695`, mae `0.016378`
- 10d: sample `80`, hit `0.5`, avg `0.001685`, median `0.000242`, mae `0.019063`
- 20d: sample `80`, hit `0.6875`, avg `0.006662`, median `0.01128`, mae `0.028625`
- 60d: sample `80`, hit `0.4875`, avg `0.005631`, median `-0.001675`, mae `0.058669`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.004529`, median `-0.006856`, mae `0.017879`
- 5d: sample `40`, hit `0.475`, avg `-0.004913`, median `-0.004438`, mae `0.018958`
- 10d: sample `40`, hit `0.5`, avg `0.002056`, median `0.001607`, mae `0.021552`
- 20d: sample `40`, hit `0.75`, avg `0.013478`, median `0.015661`, mae `0.033145`
- 60d: sample `40`, hit `0.625`, avg `0.026047`, median `0.029831`, mae `0.063806`

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
- 3d: sample `40`, hit `0.4`, avg `-0.006226`, median `-0.002789`, mae `0.013613`
- 5d: sample `40`, hit `0.55`, avg `-0.005116`, median `0.002694`, mae `0.014555`
- 10d: sample `40`, hit `0.425`, avg `-0.001491`, median `-0.001676`, mae `0.013461`
- 20d: sample `40`, hit `0.675`, avg `0.007909`, median `0.012958`, mae `0.028215`
- 60d: sample `40`, hit `0.45`, avg `-0.0041`, median `-0.01711`, mae `0.062727`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.00059`, median `0.001999`, mae `0.013562`
- 5d: sample `40`, hit `0.475`, avg `-0.001085`, median `-0.000371`, mae `0.018202`
- 10d: sample `40`, hit `0.575`, avg `0.004861`, median `0.005417`, mae `0.024665`
- 20d: sample `40`, hit `0.7`, avg `0.005415`, median `0.01011`, mae `0.029035`
- 60d: sample `40`, hit `0.525`, avg `0.015362`, median `0.010234`, mae `0.054611`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.006226`, median `-0.002789`, mae `0.013613`
- 5d: sample `40`, hit `0.55`, avg `-0.005116`, median `0.002694`, mae `0.014555`
- 10d: sample `40`, hit `0.425`, avg `-0.001491`, median `-0.001676`, mae `0.013461`
- 20d: sample `40`, hit `0.675`, avg `0.007909`, median `0.012958`, mae `0.028215`
- 60d: sample `40`, hit `0.45`, avg `-0.0041`, median `-0.01711`, mae `0.062727`

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
- 3d: sample `40`, hit `0.4`, avg `-0.006226`, median `-0.002789`, mae `0.013613`
- 5d: sample `40`, hit `0.55`, avg `-0.005116`, median `0.002694`, mae `0.014555`
- 10d: sample `40`, hit `0.425`, avg `-0.001491`, median `-0.001676`, mae `0.013461`
- 20d: sample `40`, hit `0.675`, avg `0.007909`, median `0.012958`, mae `0.028215`
- 60d: sample `40`, hit `0.45`, avg `-0.0041`, median `-0.01711`, mae `0.062727`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.006226`, median `-0.002789`, mae `0.013613`
- 5d: sample `40`, hit `0.55`, avg `-0.005116`, median `0.002694`, mae `0.014555`
- 10d: sample `40`, hit `0.425`, avg `-0.001491`, median `-0.001676`, mae `0.013461`
- 20d: sample `40`, hit `0.675`, avg `0.007909`, median `0.012958`, mae `0.028215`
- 60d: sample `40`, hit `0.45`, avg `-0.0041`, median `-0.01711`, mae `0.062727`

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
