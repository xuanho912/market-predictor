# High Confidence Edge Report

Generated at: `2026-08-10T22:12:54.177713+00:00`

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
- 3d: sample `80`, hit `0.625`, avg `0.001919`, median `0.004542`, mae `0.015163`
- 5d: sample `80`, hit `0.675`, avg `0.004169`, median `0.005327`, mae `0.018129`
- 10d: sample `80`, hit `0.55`, avg `0.003762`, median `0.007467`, mae `0.026575`
- 20d: sample `80`, hit `0.65`, avg `0.004651`, median `0.013877`, mae `0.042697`
- 60d: sample `80`, hit `0.5375`, avg `0.012992`, median `0.020144`, mae `0.070318`

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
- 3d: sample `8`, hit `0.5`, avg `-0.007498`, median `0.001448`, mae `0.01749`
- 5d: sample `8`, hit `0.625`, avg `-0.001465`, median `0.004014`, mae `0.012315`
- 10d: sample `8`, hit `0.5`, avg `0.001015`, median `0.011426`, mae `0.019915`
- 20d: sample `8`, hit `0.625`, avg `0.00323`, median `0.020068`, mae `0.032795`
- 60d: sample `8`, hit `0.5`, avg `0.003476`, median `0.012092`, mae `0.040494`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.007498`, median `0.001448`, mae `0.01749`
- 5d: sample `8`, hit `0.625`, avg `-0.001465`, median `0.004014`, mae `0.012315`
- 10d: sample `8`, hit `0.5`, avg `0.001015`, median `0.011426`, mae `0.019915`
- 20d: sample `8`, hit `0.625`, avg `0.00323`, median `0.020068`, mae `0.032795`
- 60d: sample `8`, hit `0.5`, avg `0.003476`, median `0.012092`, mae `0.040494`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.001919, 'median_return': 0.004542, 'mean_absolute_return': 0.015163, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.004169, 'median_return': 0.005327, 'mean_absolute_return': 0.018129, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.003762, 'median_return': 0.007467, 'mean_absolute_return': 0.026575, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.004651, 'median_return': 0.013877, 'mean_absolute_return': 0.042697, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.012992, 'median_return': 0.020144, 'mean_absolute_return': 0.070318, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.007498, 'median_return': 0.001448, 'mean_absolute_return': 0.01749, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001465, 'median_return': 0.004014, 'mean_absolute_return': 0.012315, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001015, 'median_return': 0.011426, 'mean_absolute_return': 0.019915, 'max_adverse_excursion': -0.033507, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.00323, 'median_return': 0.020068, 'mean_absolute_return': 0.032795, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003476, 'median_return': 0.012092, 'mean_absolute_return': 0.040494, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.002965, 'median_return': 0.004569, 'mean_absolute_return': 0.014904, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.004796, 'median_return': 0.006133, 'mean_absolute_return': 0.018776, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.004067, 'median_return': 0.007467, 'mean_absolute_return': 0.027314, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.004808, 'median_return': 0.013877, 'mean_absolute_return': 0.043797, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.014049, 'median_return': 0.022085, 'mean_absolute_return': 0.073631, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.675}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 20, 'both_miss': 20}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.2, 'both_hit': 26, 'both_miss': 14}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.075, 'both_hit': 21, 'both_miss': 19}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.15, 'both_hit': 26, 'both_miss': 14}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.15, 'both_hit': 17, 'both_miss': 23}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.007353, 'median_return': 0.010849, 'mean_absolute_return': 0.01671, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.006753, 'median_return': 0.010281, 'mean_absolute_return': 0.022081, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.004707, 'median_return': 0.011168, 'mean_absolute_return': 0.033053, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.005628, 'median_return': 0.015261, 'mean_absolute_return': 0.050667, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.024819, 'median_return': 0.046677, 'mean_absolute_return': 0.084444, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.003516, 'median_return': 0.000145, 'mean_absolute_return': 0.013616, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.001585, 'median_return': 0.004014, 'mean_absolute_return': 0.014178, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.002816, 'median_return': 0.007467, 'mean_absolute_return': 0.020096, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.003674, 'median_return': 0.013178, 'mean_absolute_return': 0.034726, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': 0.001165, 'median_return': -0.01711, 'mean_absolute_return': 0.056192, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.101282}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003516`, median `0.000145`, mae `0.013616`
- 5d: sample `40`, hit `0.65`, avg `0.001585`, median `0.004014`, mae `0.014178`
- 10d: sample `40`, hit `0.525`, avg `0.002816`, median `0.007467`, mae `0.020096`
- 20d: sample `40`, hit `0.65`, avg `0.003674`, median `0.013178`, mae `0.034726`
- 60d: sample `40`, hit `0.425`, avg `0.001165`, median `-0.01711`, mae `0.056192`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007129`, median `0.011125`, mae `0.020216`
- 5d: sample `20`, hit `0.6`, avg `0.003877`, median `0.010281`, mae `0.026503`
- 10d: sample `20`, hit `0.6`, avg `0.01225`, median `0.016085`, mae `0.037626`
- 20d: sample `20`, hit `0.7`, avg `0.025182`, median `0.025442`, mae `0.053595`
- 60d: sample `20`, hit `0.7`, avg `0.056405`, median `0.061844`, mae `0.086438`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003516`, median `0.000145`, mae `0.013616`
- 5d: sample `40`, hit `0.65`, avg `0.001585`, median `0.004014`, mae `0.014178`
- 10d: sample `40`, hit `0.525`, avg `0.002816`, median `0.007467`, mae `0.020096`
- 20d: sample `40`, hit `0.65`, avg `0.003674`, median `0.013178`, mae `0.034726`
- 60d: sample `40`, hit `0.425`, avg `0.001165`, median `-0.01711`, mae `0.056192`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007129`, median `0.011125`, mae `0.020216`
- 5d: sample `20`, hit `0.6`, avg `0.003877`, median `0.010281`, mae `0.026503`
- 10d: sample `20`, hit `0.6`, avg `0.01225`, median `0.016085`, mae `0.037626`
- 20d: sample `20`, hit `0.7`, avg `0.025182`, median `0.025442`, mae `0.053595`
- 60d: sample `20`, hit `0.7`, avg `0.056405`, median `0.061844`, mae `0.086438`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001874`, median `0.003785`, mae `0.016976`
- 5d: sample `20`, hit `0.6`, avg `0.002691`, median `0.004014`, mae `0.016933`
- 10d: sample `20`, hit `0.6`, avg `0.007331`, median `0.011426`, mae `0.022968`
- 20d: sample `20`, hit `0.75`, avg `0.016395`, median `0.024743`, mae `0.038483`
- 60d: sample `20`, hit `0.5`, avg `0.013799`, median `0.012092`, mae `0.061377`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003516`, median `0.000145`, mae `0.013616`
- 5d: sample `40`, hit `0.65`, avg `0.001585`, median `0.004014`, mae `0.014178`
- 10d: sample `40`, hit `0.525`, avg `0.002816`, median `0.007467`, mae `0.020096`
- 20d: sample `40`, hit `0.65`, avg `0.003674`, median `0.013178`, mae `0.034726`
- 60d: sample `40`, hit `0.425`, avg `0.001165`, median `-0.01711`, mae `0.056192`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.007353`, median `0.010849`, mae `0.01671`
- 5d: sample `40`, hit `0.7`, avg `0.006753`, median `0.010281`, mae `0.022081`
- 10d: sample `40`, hit `0.575`, avg `0.004707`, median `0.011168`, mae `0.033053`
- 20d: sample `40`, hit `0.65`, avg `0.005628`, median `0.015261`, mae `0.050667`
- 60d: sample `40`, hit `0.65`, avg `0.024819`, median `0.046677`, mae `0.084444`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001874`, median `0.003785`, mae `0.016976`
- 5d: sample `20`, hit `0.6`, avg `0.002691`, median `0.004014`, mae `0.016933`
- 10d: sample `20`, hit `0.6`, avg `0.007331`, median `0.011426`, mae `0.022968`
- 20d: sample `20`, hit `0.75`, avg `0.016395`, median `0.024743`, mae `0.038483`
- 60d: sample `20`, hit `0.5`, avg `0.013799`, median `0.012092`, mae `0.061377`

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
- 3d: sample `20`, hit `0.45`, avg `-0.005157`, median `-0.001166`, mae `0.010256`
- 5d: sample `20`, hit `0.7`, avg `0.00048`, median `0.004606`, mae `0.011423`
- 10d: sample `20`, hit `0.45`, avg `-0.001699`, median `-0.001676`, mae `0.017224`
- 20d: sample `20`, hit `0.55`, avg `-0.009048`, median `0.007988`, mae `0.030969`
- 60d: sample `20`, hit `0.35`, avg `-0.011469`, median `-0.018455`, mae `0.051006`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001874`, median `0.003785`, mae `0.016976`
- 5d: sample `20`, hit `0.6`, avg `0.002691`, median `0.004014`, mae `0.016933`
- 10d: sample `20`, hit `0.6`, avg `0.007331`, median `0.011426`, mae `0.022968`
- 20d: sample `20`, hit `0.75`, avg `0.016395`, median `0.024743`, mae `0.038483`
- 60d: sample `20`, hit `0.5`, avg `0.013799`, median `0.012092`, mae `0.061377`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007129`, median `0.011125`, mae `0.020216`
- 5d: sample `20`, hit `0.6`, avg `0.003877`, median `0.010281`, mae `0.026503`
- 10d: sample `20`, hit `0.6`, avg `0.01225`, median `0.016085`, mae `0.037626`
- 20d: sample `20`, hit `0.7`, avg `0.025182`, median `0.025442`, mae `0.053595`
- 60d: sample `20`, hit `0.7`, avg `0.056405`, median `0.061844`, mae `0.086438`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.005157`, median `-0.001166`, mae `0.010256`
- 5d: sample `20`, hit `0.7`, avg `0.00048`, median `0.004606`, mae `0.011423`
- 10d: sample `20`, hit `0.45`, avg `-0.001699`, median `-0.001676`, mae `0.017224`
- 20d: sample `20`, hit `0.55`, avg `-0.009048`, median `0.007988`, mae `0.030969`
- 60d: sample `20`, hit `0.35`, avg `-0.011469`, median `-0.018455`, mae `0.051006`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007129`, median `0.011125`, mae `0.020216`
- 5d: sample `20`, hit `0.6`, avg `0.003877`, median `0.010281`, mae `0.026503`
- 10d: sample `20`, hit `0.6`, avg `0.01225`, median `0.016085`, mae `0.037626`
- 20d: sample `20`, hit `0.7`, avg `0.025182`, median `0.025442`, mae `0.053595`
- 60d: sample `20`, hit `0.7`, avg `0.056405`, median `0.061844`, mae `0.086438`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.001919`, median `0.004542`, mae `0.015163`
- 5d: sample `80`, hit `0.675`, avg `0.004169`, median `0.005327`, mae `0.018129`
- 10d: sample `80`, hit `0.55`, avg `0.003762`, median `0.007467`, mae `0.026575`
- 20d: sample `80`, hit `0.65`, avg `0.004651`, median `0.013877`, mae `0.042697`
- 60d: sample `80`, hit `0.5375`, avg `0.012992`, median `0.020144`, mae `0.070318`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.001919`, median `0.004542`, mae `0.015163`
- 5d: sample `80`, hit `0.675`, avg `0.004169`, median `0.005327`, mae `0.018129`
- 10d: sample `80`, hit `0.55`, avg `0.003762`, median `0.007467`, mae `0.026575`
- 20d: sample `80`, hit `0.65`, avg `0.004651`, median `0.013877`, mae `0.042697`
- 60d: sample `80`, hit `0.5375`, avg `0.012992`, median `0.020144`, mae `0.070318`

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
