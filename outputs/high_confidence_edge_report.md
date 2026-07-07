# High Confidence Edge Report

Generated at: `2026-07-07T23:44:40.105826+00:00`

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
- 3d: sample `40`, hit `0.45`, avg `-0.003951`, median `-0.002441`, mae `0.01765`
- 5d: sample `40`, hit `0.5`, avg `-0.004698`, median `0.000415`, mae `0.018281`
- 10d: sample `40`, hit `0.45`, avg `-0.00159`, median `-0.005891`, mae `0.020576`
- 20d: sample `40`, hit `0.675`, avg `0.009439`, median `0.007676`, mae `0.02996`
- 60d: sample `40`, hit `0.625`, avg `0.024643`, median `0.019715`, mae `0.062403`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.001013`, median `-0.000317`, mae `0.00945`
- 5d: sample `40`, hit `0.525`, avg `-0.003092`, median `0.003026`, mae `0.015219`
- 10d: sample `40`, hit `0.55`, avg `0.000918`, median `0.00273`, mae `0.017632`
- 20d: sample `40`, hit `0.575`, avg `-0.002482`, median `0.009737`, mae `0.025876`
- 60d: sample `40`, hit `0.325`, avg `-0.02045`, median `-0.03023`, mae `0.058236`

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
- 3d: sample `8`, hit `0.125`, avg `-0.015259`, median `-0.010033`, mae `0.016937`
- 5d: sample `8`, hit `0.25`, avg `-0.014866`, median `-0.022295`, mae `0.018045`
- 10d: sample `8`, hit `0.0`, avg `-0.013065`, median `-0.010456`, mae `0.013065`
- 20d: sample `8`, hit `0.75`, avg `0.025458`, median `0.029166`, mae `0.036827`
- 60d: sample `8`, hit `0.75`, avg `0.048165`, median `0.072696`, mae `0.075988`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.015259`, median `-0.010033`, mae `0.016937`
- 5d: sample `8`, hit `0.25`, avg `-0.014866`, median `-0.022295`, mae `0.018045`
- 10d: sample `8`, hit `0.0`, avg `-0.013065`, median `-0.010456`, mae `0.013065`
- 20d: sample `8`, hit `0.75`, avg `0.025458`, median `0.029166`, mae `0.036827`
- 60d: sample `8`, hit `0.75`, avg `0.048165`, median `0.072696`, mae `0.075988`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.003951, 'median_return': -0.002441, 'mean_absolute_return': 0.01765, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.035273}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.004698, 'median_return': 0.000415, 'mean_absolute_return': 0.018281, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.037278}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.00159, 'median_return': -0.005891, 'mean_absolute_return': 0.020576, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.051039}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.009439, 'median_return': 0.007676, 'mean_absolute_return': 0.02996, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.024643, 'median_return': 0.019715, 'mean_absolute_return': 0.062403, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.001013, 'median_return': -0.000317, 'mean_absolute_return': 0.00945, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025242}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.003092, 'median_return': 0.003026, 'mean_absolute_return': 0.015219, 'max_adverse_excursion': -0.058308, 'max_favorable_excursion': 0.023659}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.000918, 'median_return': 0.00273, 'mean_absolute_return': 0.017632, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.002482, 'median_return': 0.009737, 'mean_absolute_return': 0.025876, 'max_adverse_excursion': -0.087798, 'max_favorable_excursion': 0.068982}, '60d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.02045, 'median_return': -0.03023, 'mean_absolute_return': 0.058236, 'max_adverse_excursion': -0.138565, 'max_favorable_excursion': 0.105138}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.015259, 'median_return': -0.010033, 'mean_absolute_return': 0.016937, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.014866, 'median_return': -0.022295, 'mean_absolute_return': 0.018045, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.013065, 'median_return': -0.010456, 'mean_absolute_return': 0.013065, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.025458, 'median_return': 0.029166, 'mean_absolute_return': 0.036827, 'max_adverse_excursion': -0.033249, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.048165, 'median_return': 0.072696, 'mean_absolute_return': 0.075988, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001062, 'median_return': 0.000145, 'mean_absolute_return': 0.013174, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.035273}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.002676, 'median_return': 0.003026, 'mean_absolute_return': 0.016607, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.037278}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001078, 'median_return': 0.002896, 'mean_absolute_return': 0.019775, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.001036, 'median_return': 0.007366, 'mean_absolute_return': 0.026928, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.003022, 'median_return': -0.009954, 'mean_absolute_return': 0.058578, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.475}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.0, 'both_hit': 37, 'both_miss': 43}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.0, 'both_hit': 41, 'both_miss': 39}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 40}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.0, 'both_hit': 38, 'both_miss': 42}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.002482, 'median_return': -0.001166, 'mean_absolute_return': 0.01355, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.035273}, '5d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.003895, 'median_return': 0.001104, 'mean_absolute_return': 0.01675, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.037278}, '10d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.000336, 'median_return': 0.000242, 'mean_absolute_return': 0.019104, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.003479, 'median_return': 0.007988, 'mean_absolute_return': 0.027918, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.002097, 'median_return': -0.005293, 'mean_absolute_return': 0.060319, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.002482`, median `-0.001166`, mae `0.01355`
- 5d: sample `80`, hit `0.5125`, avg `-0.003895`, median `0.001104`, mae `0.01675`
- 10d: sample `80`, hit `0.5`, avg `-0.000336`, median `0.000242`, mae `0.019104`
- 20d: sample `80`, hit `0.625`, avg `0.003479`, median `0.007988`, mae `0.027918`
- 60d: sample `80`, hit `0.475`, avg `0.002097`, median `-0.005293`, mae `0.060319`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.002482`, median `-0.001166`, mae `0.01355`
- 5d: sample `80`, hit `0.5125`, avg `-0.003895`, median `0.001104`, mae `0.01675`
- 10d: sample `80`, hit `0.5`, avg `-0.000336`, median `0.000242`, mae `0.019104`
- 20d: sample `80`, hit `0.625`, avg `0.003479`, median `0.007988`, mae `0.027918`
- 60d: sample `80`, hit `0.475`, avg `0.002097`, median `-0.005293`, mae `0.060319`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003951`, median `-0.002441`, mae `0.01765`
- 5d: sample `40`, hit `0.5`, avg `-0.004698`, median `0.000415`, mae `0.018281`
- 10d: sample `40`, hit `0.45`, avg `-0.00159`, median `-0.005891`, mae `0.020576`
- 20d: sample `40`, hit `0.675`, avg `0.009439`, median `0.007676`, mae `0.02996`
- 60d: sample `40`, hit `0.625`, avg `0.024643`, median `0.019715`, mae `0.062403`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.002482`, median `-0.001166`, mae `0.01355`
- 5d: sample `80`, hit `0.5125`, avg `-0.003895`, median `0.001104`, mae `0.01675`
- 10d: sample `80`, hit `0.5`, avg `-0.000336`, median `0.000242`, mae `0.019104`
- 20d: sample `80`, hit `0.625`, avg `0.003479`, median `0.007988`, mae `0.027918`
- 60d: sample `80`, hit `0.475`, avg `0.002097`, median `-0.005293`, mae `0.060319`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003951`, median `-0.002441`, mae `0.01765`
- 5d: sample `40`, hit `0.5`, avg `-0.004698`, median `0.000415`, mae `0.018281`
- 10d: sample `40`, hit `0.45`, avg `-0.00159`, median `-0.005891`, mae `0.020576`
- 20d: sample `40`, hit `0.675`, avg `0.009439`, median `0.007676`, mae `0.02996`
- 60d: sample `40`, hit `0.625`, avg `0.024643`, median `0.019715`, mae `0.062403`

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
- 3d: sample `40`, hit `0.45`, avg `-0.004773`, median `-0.001658`, mae `0.013808`
- 5d: sample `40`, hit `0.55`, avg `-0.005063`, median `0.003005`, mae `0.015439`
- 10d: sample `40`, hit `0.425`, avg `-0.003277`, median `-0.001676`, mae `0.014321`
- 20d: sample `40`, hit `0.675`, avg `0.007378`, median `0.011728`, mae `0.027532`
- 60d: sample `40`, hit `0.475`, avg `-0.004452`, median `-0.005523`, mae `0.064245`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000192`, median `-0.000317`, mae `0.013292`
- 5d: sample `40`, hit `0.475`, avg `-0.002726`, median `-0.001324`, mae `0.018061`
- 10d: sample `40`, hit `0.575`, avg `0.002605`, median `0.003262`, mae `0.023888`
- 20d: sample `40`, hit `0.575`, avg `-0.00042`, median `0.004543`, mae `0.028304`
- 60d: sample `40`, hit `0.475`, avg `0.008646`, median `-0.001675`, mae `0.056394`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.004773`, median `-0.001658`, mae `0.013808`
- 5d: sample `40`, hit `0.55`, avg `-0.005063`, median `0.003005`, mae `0.015439`
- 10d: sample `40`, hit `0.425`, avg `-0.003277`, median `-0.001676`, mae `0.014321`
- 20d: sample `40`, hit `0.675`, avg `0.007378`, median `0.011728`, mae `0.027532`
- 60d: sample `40`, hit `0.475`, avg `-0.004452`, median `-0.005523`, mae `0.064245`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.003113`, median `-0.001658`, mae `0.014481`
- 5d: sample `60`, hit `0.55`, avg `-0.002766`, median `0.003005`, mae `0.016288`
- 10d: sample `60`, hit `0.5`, avg `-0.000275`, median `0.001607`, mae `0.01827`
- 20d: sample `60`, hit `0.7`, avg `0.008491`, median `0.01128`, mae `0.027422`
- 60d: sample `60`, hit `0.5`, avg `0.003723`, median `0.003095`, mae `0.060335`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.003113`, median `-0.001658`, mae `0.014481`
- 5d: sample `60`, hit `0.55`, avg `-0.002766`, median `0.003005`, mae `0.016288`
- 10d: sample `60`, hit `0.5`, avg `-0.000275`, median `0.001607`, mae `0.01827`
- 20d: sample `60`, hit `0.7`, avg `0.008491`, median `0.01128`, mae `0.027422`
- 60d: sample `60`, hit `0.5`, avg `0.003723`, median `0.003095`, mae `0.060335`

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
