# High Confidence Edge Report

Generated at: `2026-07-15T14:12:50.287124+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.00185`, median `0.000603`, mae `0.010204`
- 5d: sample `60`, hit `0.5667`, avg `0.001736`, median `0.005084`, mae `0.015043`
- 10d: sample `60`, hit `0.5167`, avg `-0.001458`, median `0.002362`, mae `0.020509`
- 20d: sample `60`, hit `0.6833`, avg `-0.001782`, median `0.01011`, mae `0.031398`
- 60d: sample `60`, hit `0.4333`, avg `-0.007443`, median `-0.009954`, mae `0.056735`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.005267`, median `0.001448`, mae `0.015969`
- 5d: sample `20`, hit `0.5`, avg `-0.005904`, median `0.000415`, mae `0.018269`
- 10d: sample `20`, hit `0.5`, avg `-0.003263`, median `0.001517`, mae `0.021528`
- 20d: sample `20`, hit `0.65`, avg `0.001048`, median `0.020068`, mae `0.036482`
- 60d: sample `20`, hit `0.45`, avg `-0.004853`, median `-0.004982`, mae `0.080455`

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
- 3d: sample `8`, hit `0.5`, avg `0.002558`, median `0.001999`, mae `0.007215`
- 5d: sample `8`, hit `0.625`, avg `0.007858`, median `0.011917`, mae `0.011728`
- 10d: sample `8`, hit `0.625`, avg `0.006281`, median `0.008202`, mae `0.018574`
- 20d: sample `8`, hit `0.5`, avg `-0.012556`, median `0.002818`, mae `0.027093`
- 60d: sample `8`, hit `0.75`, avg `0.020729`, median `0.048484`, mae `0.06543`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.002558`, median `0.001999`, mae `0.007215`
- 5d: sample `8`, hit `0.625`, avg `0.007858`, median `0.011917`, mae `0.011728`
- 10d: sample `8`, hit `0.625`, avg `0.006281`, median `0.008202`, mae `0.018574`
- 20d: sample `8`, hit `0.5`, avg `-0.012556`, median `0.002818`, mae `0.027093`
- 60d: sample `8`, hit `0.75`, avg `0.020729`, median `0.048484`, mae `0.06543`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.00185, 'median_return': 0.000603, 'mean_absolute_return': 0.010204, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.001736, 'median_return': 0.005084, 'mean_absolute_return': 0.015043, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.001458, 'median_return': 0.002362, 'mean_absolute_return': 0.020509, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': -0.001782, 'median_return': 0.01011, 'mean_absolute_return': 0.031398, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.007443, 'median_return': -0.009954, 'mean_absolute_return': 0.056735, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.116132}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002558, 'median_return': 0.001999, 'mean_absolute_return': 0.007215, 'max_adverse_excursion': -0.008613, 'max_favorable_excursion': 0.022489}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.007858, 'median_return': 0.011917, 'mean_absolute_return': 0.011728, 'max_adverse_excursion': -0.013784, 'max_favorable_excursion': 0.023659}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006281, 'median_return': 0.008202, 'mean_absolute_return': 0.018574, 'max_adverse_excursion': -0.036679, 'max_favorable_excursion': 0.042458}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.012556, 'median_return': 0.002818, 'mean_absolute_return': 0.027093, 'max_adverse_excursion': -0.048034, 'max_favorable_excursion': 0.030922}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.020729, 'median_return': 0.048484, 'mean_absolute_return': 0.06543, 'max_adverse_excursion': -0.093084, 'max_favorable_excursion': 0.096756}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.000206, 'median_return': 0.000603, 'mean_absolute_return': 0.012138, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.001066, 'median_return': 0.003714, 'mean_absolute_return': 0.016307, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.002819, 'median_return': 0.001517, 'mean_absolute_return': 0.021007, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.000201, 'median_return': 0.01128, 'mean_absolute_return': 0.033289, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.009854, 'median_return': -0.013501, 'mean_absolute_return': 0.062358, 'max_adverse_excursion': -0.158935, 'max_favorable_excursion': 0.145114}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.4}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.05, 'both_hit': 14, 'both_miss': 6}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.05, 'both_hit': 12, 'both_miss': 8}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 10, 'both_miss': 10}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.275, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.15, 'both_hit': 11, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.00185, 'median_return': 0.000603, 'mean_absolute_return': 0.010204, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.001736, 'median_return': 0.005084, 'mean_absolute_return': 0.015043, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.001458, 'median_return': 0.002362, 'mean_absolute_return': 0.020509, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': -0.001782, 'median_return': 0.01011, 'mean_absolute_return': 0.031398, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.007443, 'median_return': -0.009954, 'mean_absolute_return': 0.056735, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.116132}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.005267, 'median_return': 0.001448, 'mean_absolute_return': 0.015969, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.005904, 'median_return': 0.000415, 'mean_absolute_return': 0.018269, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.025923}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.003263, 'median_return': 0.001517, 'mean_absolute_return': 0.021528, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.001048, 'median_return': 0.020068, 'mean_absolute_return': 0.036482, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.004853, 'median_return': -0.004982, 'mean_absolute_return': 0.080455, 'max_adverse_excursion': -0.158935, 'max_favorable_excursion': 0.145114}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.000297`, median `-0.002441`, mae `0.010146`
- 5d: sample `40`, hit `0.55`, avg `-0.000911`, median `0.003888`, mae `0.015675`
- 10d: sample `40`, hit `0.525`, avg `-0.002591`, median `0.003262`, mae `0.020235`
- 20d: sample `40`, hit `0.7`, avg `-0.003638`, median `0.01128`, mae `0.03217`
- 60d: sample `40`, hit `0.375`, avg `-0.018075`, median `-0.013501`, mae `0.051825`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.001954`, median `-0.00162`, mae `0.012087`
- 5d: sample `60`, hit `0.5333`, avg `-0.002576`, median `0.003026`, mae `0.01654`
- 10d: sample `60`, hit `0.5167`, avg `-0.002815`, median `0.002362`, mae `0.020666`
- 20d: sample `60`, hit `0.6833`, avg `-0.002076`, median `0.01128`, mae `0.033608`
- 60d: sample `60`, hit `0.4`, avg `-0.013668`, median `-0.013501`, mae `0.061368`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006145`, median `0.006214`, mae `0.010322`
- 5d: sample `20`, hit `0.6`, avg `0.007032`, median `0.006676`, mae `0.013777`
- 10d: sample `20`, hit `0.5`, avg `0.000808`, median `0.000242`, mae `0.021055`
- 20d: sample `20`, hit `0.65`, avg `0.00193`, median `0.009812`, mae `0.029854`
- 60d: sample `20`, hit `0.55`, avg `0.013821`, median `0.045044`, mae `0.066556`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.001954`, median `-0.00162`, mae `0.012087`
- 5d: sample `60`, hit `0.5333`, avg `-0.002576`, median `0.003026`, mae `0.01654`
- 10d: sample `60`, hit `0.5167`, avg `-0.002815`, median `0.002362`, mae `0.020666`
- 20d: sample `60`, hit `0.6833`, avg `-0.002076`, median `0.01128`, mae `0.033608`
- 60d: sample `60`, hit `0.4`, avg `-0.013668`, median `-0.013501`, mae `0.061368`

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
- 3d: sample `80`, hit `0.525`, avg `7.1e-05`, median `0.000603`, mae `0.011646`
- 5d: sample `80`, hit `0.55`, avg `-0.000174`, median `0.003888`, mae `0.015849`
- 10d: sample `80`, hit `0.5125`, avg `-0.001909`, median `0.001517`, mae `0.020764`
- 20d: sample `80`, hit `0.675`, avg `-0.001075`, median `0.01011`, mae `0.032669`
- 60d: sample `80`, hit `0.4375`, avg `-0.006795`, median `-0.009954`, mae `0.062665`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006145`, median `0.006214`, mae `0.010322`
- 5d: sample `20`, hit `0.6`, avg `0.007032`, median `0.006676`, mae `0.013777`
- 10d: sample `20`, hit `0.5`, avg `0.000808`, median `0.000242`, mae `0.021055`
- 20d: sample `20`, hit `0.65`, avg `0.00193`, median `0.009812`, mae `0.029854`
- 60d: sample `20`, hit `0.55`, avg `0.013821`, median `0.045044`, mae `0.066556`

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
