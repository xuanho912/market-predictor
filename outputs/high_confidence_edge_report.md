# High Confidence Edge Report

Generated at: `2026-08-07T13:42:37.300782+00:00`

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
- 3d: sample `60`, hit `0.5833`, avg `0.002017`, median `0.003538`, mae `0.012748`
- 5d: sample `60`, hit `0.7333`, avg `0.006481`, median `0.006452`, mae `0.014176`
- 10d: sample `60`, hit `0.6`, avg `0.005287`, median `0.00903`, mae `0.020911`
- 20d: sample `60`, hit `0.6833`, avg `0.008266`, median `0.01666`, mae `0.035739`
- 60d: sample `60`, hit `0.55`, avg `0.015276`, median `0.032982`, mae `0.065556`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.0101`, median `0.012584`, mae `0.017395`
- 5d: sample `20`, hit `0.65`, avg `0.006042`, median `0.010281`, mae `0.021312`
- 10d: sample `20`, hit `0.65`, avg `0.016306`, median `0.01246`, mae `0.028822`
- 20d: sample `20`, hit `0.75`, avg `0.030987`, median `0.029029`, mae `0.052041`
- 60d: sample `20`, hit `0.7`, avg `0.054799`, median `0.079128`, mae `0.092625`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003813`, median `0.001448`, mae `0.013805`
- 5d: sample `8`, hit `0.75`, avg `0.000899`, median `0.004014`, mae `0.010054`
- 10d: sample `8`, hit `0.5`, avg `0.002265`, median `0.011426`, mae `0.018665`
- 20d: sample `8`, hit `0.625`, avg `0.009259`, median `0.020068`, mae `0.026767`
- 60d: sample `8`, hit `0.375`, avg `-0.012738`, median `-0.03081`, mae `0.04907`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.003813`, median `0.001448`, mae `0.013805`
- 5d: sample `8`, hit `0.75`, avg `0.000899`, median `0.004014`, mae `0.010054`
- 10d: sample `8`, hit `0.5`, avg `0.002265`, median `0.011426`, mae `0.018665`
- 20d: sample `8`, hit `0.625`, avg `0.009259`, median `0.020068`, mae `0.026767`
- 60d: sample `8`, hit `0.375`, avg `-0.012738`, median `-0.03081`, mae `0.04907`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.002017, 'median_return': 0.003538, 'mean_absolute_return': 0.012748, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.006481, 'median_return': 0.006452, 'mean_absolute_return': 0.014176, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.005287, 'median_return': 0.00903, 'mean_absolute_return': 0.020911, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.008266, 'median_return': 0.01666, 'mean_absolute_return': 0.035739, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.015276, 'median_return': 0.032982, 'mean_absolute_return': 0.065556, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003813, 'median_return': 0.001448, 'mean_absolute_return': 0.013805, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.000899, 'median_return': 0.004014, 'mean_absolute_return': 0.010054, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002265, 'median_return': 0.011426, 'mean_absolute_return': 0.018665, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009259, 'median_return': 0.020068, 'mean_absolute_return': 0.026767, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012738, 'median_return': -0.03081, 'mean_absolute_return': 0.04907, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.00491, 'median_return': 0.006565, 'mean_absolute_return': 0.013921, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.006979, 'median_return': 0.00774, 'mean_absolute_return': 0.016617, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.008684, 'median_return': 0.010691, 'mean_absolute_return': 0.023358, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.014467, 'median_return': 0.01666, 'mean_absolute_return': 0.041264, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.029367, 'median_return': 0.052998, 'mean_absolute_return': 0.074907, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.4875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.125, 'both_hit': 35, 'both_miss': 25}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.075, 'both_hit': 44, 'both_miss': 16}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.075, 'both_hit': 36, 'both_miss': 24}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.125, 'both_hit': 41, 'both_miss': 19}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 33, 'both_miss': 27}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.006188, 'median_return': 0.009966, 'mean_absolute_return': 0.015801, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.007007, 'median_return': 0.008121, 'mean_absolute_return': 0.017808, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.009711, 'median_return': 0.011168, 'mean_absolute_return': 0.025569, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.017028, 'median_return': 0.021844, 'mean_absolute_return': 0.045919, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.035435, 'median_return': 0.061844, 'mean_absolute_return': 0.079903, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.002412, 'median_return': 0.000145, 'mean_absolute_return': 0.008236, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.004463, 'median_return': 0.005084, 'mean_absolute_return': 0.010418, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.025304}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003036, 'median_return': 0.007467, 'mean_absolute_return': 0.01485, 'max_adverse_excursion': -0.028317, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004702, 'median_return': 0.012291, 'mean_absolute_return': 0.021499, 'max_adverse_excursion': -0.050277, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.005679, 'median_return': -0.01711, 'mean_absolute_return': 0.049585, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.096597}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002017`, median `0.003538`, mae `0.012748`
- 5d: sample `60`, hit `0.7333`, avg `0.006481`, median `0.006452`, mae `0.014176`
- 10d: sample `60`, hit `0.6`, avg `0.005287`, median `0.00903`, mae `0.020911`
- 20d: sample `60`, hit `0.6833`, avg `0.008266`, median `0.01666`, mae `0.035739`
- 60d: sample `60`, hit `0.55`, avg `0.015276`, median `0.032982`, mae `0.065556`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.0101`, median `0.012584`, mae `0.017395`
- 5d: sample `20`, hit `0.65`, avg `0.006042`, median `0.010281`, mae `0.021312`
- 10d: sample `20`, hit `0.65`, avg `0.016306`, median `0.01246`, mae `0.028822`
- 20d: sample `20`, hit `0.75`, avg `0.030987`, median `0.029029`, mae `0.052041`
- 60d: sample `20`, hit `0.7`, avg `0.054799`, median `0.079128`, mae `0.092625`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002017`, median `0.003538`, mae `0.012748`
- 5d: sample `60`, hit `0.7333`, avg `0.006481`, median `0.006452`, mae `0.014176`
- 10d: sample `60`, hit `0.6`, avg `0.005287`, median `0.00903`, mae `0.020911`
- 20d: sample `60`, hit `0.6833`, avg `0.008266`, median `0.01666`, mae `0.035739`
- 60d: sample `60`, hit `0.55`, avg `0.015276`, median `0.032982`, mae `0.065556`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.0101`, median `0.012584`, mae `0.017395`
- 5d: sample `20`, hit `0.65`, avg `0.006042`, median `0.010281`, mae `0.021312`
- 10d: sample `20`, hit `0.65`, avg `0.016306`, median `0.01246`, mae `0.028822`
- 20d: sample `20`, hit `0.75`, avg `0.030987`, median `0.029029`, mae `0.052041`
- 60d: sample `20`, hit `0.7`, avg `0.054799`, median `0.079128`, mae `0.092625`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002017`, median `0.003538`, mae `0.012748`
- 5d: sample `60`, hit `0.7333`, avg `0.006481`, median `0.006452`, mae `0.014176`
- 10d: sample `60`, hit `0.6`, avg `0.005287`, median `0.00903`, mae `0.020911`
- 20d: sample `60`, hit `0.6833`, avg `0.008266`, median `0.01666`, mae `0.035739`
- 60d: sample `60`, hit `0.55`, avg `0.015276`, median `0.032982`, mae `0.065556`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.0101`, median `0.012584`, mae `0.017395`
- 5d: sample `20`, hit `0.65`, avg `0.006042`, median `0.010281`, mae `0.021312`
- 10d: sample `20`, hit `0.65`, avg `0.016306`, median `0.01246`, mae `0.028822`
- 20d: sample `20`, hit `0.75`, avg `0.030987`, median `0.029029`, mae `0.052041`
- 60d: sample `20`, hit `0.7`, avg `0.054799`, median `0.079128`, mae `0.092625`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001027`, median `0.000201`, mae `0.012257`
- 5d: sample `40`, hit `0.75`, avg `0.006189`, median `0.005319`, mae `0.012621`
- 10d: sample `40`, hit `0.6`, avg `0.006587`, median `0.011426`, mae `0.018359`
- 20d: sample `40`, hit `0.7`, avg `0.012895`, median `0.020226`, mae `0.031235`
- 60d: sample `40`, hit `0.425`, avg `0.00398`, median `-0.012792`, mae `0.055333`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.0101`, median `0.012584`, mae `0.017395`
- 5d: sample `20`, hit `0.65`, avg `0.006042`, median `0.010281`, mae `0.021312`
- 10d: sample `20`, hit `0.65`, avg `0.016306`, median `0.01246`, mae `0.028822`
- 20d: sample `20`, hit `0.75`, avg `0.030987`, median `0.029029`, mae `0.052041`
- 60d: sample `20`, hit `0.7`, avg `0.054799`, median `0.079128`, mae `0.092625`

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
