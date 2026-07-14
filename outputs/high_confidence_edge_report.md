# High Confidence Edge Report

Generated at: `2026-07-14T14:16:51.417068+00:00`

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
- 3d: sample `40`, hit `0.55`, avg `0.00105`, median `0.000744`, mae `0.008505`
- 5d: sample `40`, hit `0.6`, avg `0.003822`, median `0.00596`, mae `0.013067`
- 10d: sample `40`, hit `0.525`, avg `1.6e-05`, median `0.002362`, mae `0.020073`
- 20d: sample `40`, hit `0.7`, avg `0.00618`, median `0.01329`, mae `0.029244`
- 60d: sample `40`, hit `0.475`, avg `-0.001415`, median `-0.00976`, mae `0.065716`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.003435`, median `0.001448`, mae `0.014823`
- 5d: sample `40`, hit `0.5`, avg `-0.004527`, median `0.000415`, mae `0.017953`
- 10d: sample `40`, hit `0.425`, avg `-0.003352`, median `-0.007011`, mae `0.023393`
- 20d: sample `40`, hit `0.65`, avg `0.000256`, median `0.007676`, mae `0.035606`
- 60d: sample `40`, hit `0.525`, avg `0.009919`, median `0.012092`, mae `0.059863`

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
- 3d: sample `8`, hit `0.75`, avg `0.004856`, median `0.004667`, mae `0.007178`
- 5d: sample `8`, hit `0.5`, avg `0.003711`, median `0.006133`, mae `0.010142`
- 10d: sample `8`, hit `0.5`, avg `-0.004766`, median `0.000242`, mae `0.020327`
- 20d: sample `8`, hit `0.625`, avg `0.003316`, median `0.007748`, mae `0.036378`
- 60d: sample `8`, hit `0.625`, avg `0.014702`, median `0.048484`, mae `0.07048`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.004856`, median `0.004667`, mae `0.007178`
- 5d: sample `8`, hit `0.5`, avg `0.003711`, median `0.006133`, mae `0.010142`
- 10d: sample `8`, hit `0.5`, avg `-0.004766`, median `0.000242`, mae `0.020327`
- 20d: sample `8`, hit `0.625`, avg `0.003316`, median `0.007748`, mae `0.036378`
- 60d: sample `8`, hit `0.625`, avg `0.014702`, median `0.048484`, mae `0.07048`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.00105, 'median_return': 0.000744, 'mean_absolute_return': 0.008505, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.031673}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003822, 'median_return': 0.00596, 'mean_absolute_return': 0.013067, 'max_adverse_excursion': -0.034587, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 1.6e-05, 'median_return': 0.002362, 'mean_absolute_return': 0.020073, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.00618, 'median_return': 0.01329, 'mean_absolute_return': 0.029244, 'max_adverse_excursion': -0.087798, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.001415, 'median_return': -0.00976, 'mean_absolute_return': 0.065716, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.132762}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.004856, 'median_return': 0.004667, 'mean_absolute_return': 0.007178, 'max_adverse_excursion': -0.005568, 'max_favorable_excursion': 0.01687}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003711, 'median_return': 0.006133, 'mean_absolute_return': 0.010142, 'max_adverse_excursion': -0.013784, 'max_favorable_excursion': 0.019001}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004766, 'median_return': 0.000242, 'mean_absolute_return': 0.020327, 'max_adverse_excursion': -0.036679, 'max_favorable_excursion': 0.039489}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003316, 'median_return': 0.007748, 'mean_absolute_return': 0.036378, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.014702, 'median_return': 0.048484, 'mean_absolute_return': 0.07048, 'max_adverse_excursion': -0.093084, 'max_favorable_excursion': 0.11101}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.001864, 'median_return': 0.000324, 'mean_absolute_return': 0.012162, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.031673}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.000804, 'median_return': 0.003829, 'mean_absolute_return': 0.016106, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.001323, 'median_return': -0.0004, 'mean_absolute_return': 0.02189, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.003207, 'median_return': 0.012291, 'mean_absolute_return': 0.031986, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.003091, 'median_return': -0.001675, 'mean_absolute_return': 0.061935, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.132762}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.525}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.0, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.075, 'both_hit': 11, 'both_miss': 9}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 10, 'both_miss': 10}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.225, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.025, 'both_hit': 11, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.001093, 'median_return': 0.000766, 'mean_absolute_return': 0.009904, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.031673}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.002779, 'median_return': 0.00596, 'mean_absolute_return': 0.015186, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.001429, 'median_return': 0.003262, 'mean_absolute_return': 0.022223, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.004552, 'median_return': 0.011728, 'mean_absolute_return': 0.03101, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.001491, 'median_return': -0.001675, 'mean_absolute_return': 0.060562, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.132762}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.008048, 'median_return': -0.001658, 'mean_absolute_return': 0.016945, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.009747, 'median_return': -0.002525, 'mean_absolute_return': 0.016481, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.010959, 'median_return': -0.015123, 'mean_absolute_return': 0.020263, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.000783, 'median_return': 0.020068, 'mean_absolute_return': 0.036668, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.012535, 'median_return': 0.037425, 'mean_absolute_return': 0.069474, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.121826}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00042`, median `0.000324`, mae `0.010196`
- 5d: sample `40`, hit `0.6`, avg `0.000849`, median `0.005084`, mae `0.015921`
- 10d: sample `40`, hit `0.575`, avg `0.000951`, median `0.003491`, mae `0.021735`
- 20d: sample `40`, hit `0.675`, avg `0.000624`, median `0.010653`, mae `0.029832`
- 60d: sample `40`, hit `0.45`, avg `-0.006603`, median `-0.009954`, mae `0.05466`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.002963`, median `0.000145`, mae `0.012446`
- 5d: sample `60`, hit `0.55`, avg `-0.002683`, median `0.003714`, mae `0.016108`
- 10d: sample `60`, hit `0.4667`, avg `-0.003019`, median `-0.0004`, mae `0.021245`
- 20d: sample `60`, hit `0.65`, avg `0.000155`, median `0.010653`, mae `0.032111`
- 60d: sample `60`, hit `0.4833`, avg `-0.000223`, median `-0.001675`, mae `0.059598`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001178`, median `0.007619`, mae `0.012701`
- 5d: sample `20`, hit `0.55`, avg `0.000692`, median `0.010281`, mae `0.019425`
- 10d: sample `20`, hit `0.6`, avg `0.004256`, median `0.005417`, mae `0.026524`
- 20d: sample `20`, hit `0.7`, avg `0.001295`, median `0.007676`, mae `0.034543`
- 60d: sample `20`, hit `0.5`, avg `0.007302`, median `0.003923`, mae `0.050252`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001178`, median `0.007619`, mae `0.012701`
- 5d: sample `20`, hit `0.55`, avg `0.000692`, median `0.010281`, mae `0.019425`
- 10d: sample `20`, hit `0.6`, avg `0.004256`, median `0.005417`, mae `0.026524`
- 20d: sample `20`, hit `0.7`, avg `0.001295`, median `0.007676`, mae `0.034543`
- 60d: sample `20`, hit `0.5`, avg `0.007302`, median `0.003923`, mae `0.050252`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004118`, median `0.004667`, mae `0.009318`
- 5d: sample `20`, hit `0.55`, avg `0.006637`, median `0.006133`, mae `0.013716`
- 10d: sample `20`, hit `0.5`, avg `0.002387`, median `0.000242`, mae `0.0232`
- 20d: sample `20`, hit `0.75`, avg `0.012406`, median `0.018868`, mae `0.033367`
- 60d: sample `20`, hit `0.55`, avg `0.017678`, median `0.010234`, mae `0.072366`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001178`, median `0.007619`, mae `0.012701`
- 5d: sample `20`, hit `0.55`, avg `0.000692`, median `0.010281`, mae `0.019425`
- 10d: sample `20`, hit `0.6`, avg `0.004256`, median `0.005417`, mae `0.026524`
- 20d: sample `20`, hit `0.7`, avg `0.001295`, median `0.007676`, mae `0.034543`
- 60d: sample `20`, hit `0.5`, avg `0.007302`, median `0.003923`, mae `0.050252`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.002963`, median `0.000145`, mae `0.012446`
- 5d: sample `60`, hit `0.55`, avg `-0.002683`, median `0.003714`, mae `0.016108`
- 10d: sample `60`, hit `0.4667`, avg `-0.003019`, median `-0.0004`, mae `0.021245`
- 20d: sample `60`, hit `0.65`, avg `0.000155`, median `0.010653`, mae `0.032111`
- 60d: sample `60`, hit `0.4833`, avg `-0.000223`, median `-0.001675`, mae `0.059598`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002018`, median `-0.001166`, mae `0.007692`
- 5d: sample `20`, hit `0.65`, avg `0.001007`, median `0.005084`, mae `0.012417`
- 10d: sample `20`, hit `0.55`, avg `-0.002355`, median `0.003491`, mae `0.016947`
- 20d: sample `20`, hit `0.65`, avg `-4.6e-05`, median `0.011728`, mae `0.025121`
- 60d: sample `20`, hit `0.4`, avg `-0.020507`, median `-0.03023`, mae `0.059067`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.003435`, median `0.001448`, mae `0.014823`
- 5d: sample `40`, hit `0.5`, avg `-0.004527`, median `0.000415`, mae `0.017953`
- 10d: sample `40`, hit `0.425`, avg `-0.003352`, median `-0.007011`, mae `0.023393`
- 20d: sample `40`, hit `0.65`, avg `0.000256`, median `0.007676`, mae `0.035606`
- 60d: sample `40`, hit `0.525`, avg `0.009919`, median `0.012092`, mae `0.059863`

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
