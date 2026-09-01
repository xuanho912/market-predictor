# High Confidence Edge Report

Generated at: `2026-09-01T16:43:19.552548+00:00`

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
- 3d: sample `40`, hit `0.425`, avg `-0.00357`, median `-0.001658`, mae `0.012883`
- 5d: sample `40`, hit `0.45`, avg `-0.0086`, median `-0.004438`, mae `0.015572`
- 10d: sample `40`, hit `0.4`, avg `-0.002227`, median `-0.006017`, mae `0.018397`
- 20d: sample `40`, hit `0.675`, avg `0.013698`, median `0.02086`, mae `0.033944`
- 60d: sample `40`, hit `0.725`, avg `0.043787`, median `0.061042`, mae `0.068862`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.006845`, median `0.010018`, mae `0.01619`
- 5d: sample `40`, hit `0.65`, avg `0.009003`, median `0.009517`, mae `0.01955`
- 10d: sample `40`, hit `0.45`, avg `0.003437`, median `-0.010327`, mae `0.03143`
- 20d: sample `40`, hit `0.65`, avg `0.011628`, median `0.023981`, mae `0.038318`
- 60d: sample `40`, hit `0.8`, avg `0.040347`, median `0.069439`, mae `0.086433`

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
- 3d: sample `8`, hit `0.5`, avg `-0.007732`, median `0.001558`, mae `0.01401`
- 5d: sample `8`, hit `0.375`, avg `-0.012817`, median `-0.012956`, mae `0.018988`
- 10d: sample `8`, hit `0.5`, avg `0.001642`, median `0.0076`, mae `0.01927`
- 20d: sample `8`, hit `0.875`, avg `0.020806`, median `0.031196`, mae `0.034631`
- 60d: sample `8`, hit `0.875`, avg `0.064394`, median `0.092646`, mae `0.078612`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.007732`, median `0.001558`, mae `0.01401`
- 5d: sample `8`, hit `0.375`, avg `-0.012817`, median `-0.012956`, mae `0.018988`
- 10d: sample `8`, hit `0.5`, avg `0.001642`, median `0.0076`, mae `0.01927`
- 20d: sample `8`, hit `0.875`, avg `0.020806`, median `0.031196`, mae `0.034631`
- 60d: sample `8`, hit `0.875`, avg `0.064394`, median `0.092646`, mae `0.078612`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.00357, 'median_return': -0.001658, 'mean_absolute_return': 0.012883, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.025832}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.0086, 'median_return': -0.004438, 'mean_absolute_return': 0.015572, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.002227, 'median_return': -0.006017, 'mean_absolute_return': 0.018397, 'max_adverse_excursion': -0.037654, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.013698, 'median_return': 0.02086, 'mean_absolute_return': 0.033944, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.043787, 'median_return': 0.061042, 'mean_absolute_return': 0.068862, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.007732, 'median_return': 0.001558, 'mean_absolute_return': 0.01401, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012817, 'median_return': -0.012956, 'mean_absolute_return': 0.018988, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001642, 'median_return': 0.0076, 'mean_absolute_return': 0.01927, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.020806, 'median_return': 0.031196, 'mean_absolute_return': 0.034631, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.064394, 'median_return': 0.092646, 'mean_absolute_return': 0.078612, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002678, 'median_return': 0.002067, 'mean_absolute_return': 0.014595, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001648, 'median_return': 0.00175, 'mean_absolute_return': 0.017403, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': 0.000489, 'median_return': -0.007117, 'mean_absolute_return': 0.025541, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.011758, 'median_return': 0.02086, 'mean_absolute_return': 0.036298, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.039586, 'median_return': 0.064905, 'mean_absolute_return': 0.07754, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.425}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.3375}, '60d': {'sample_size': 80, 'hit_rate': 0.2375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.525, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.000607, 'median_return': -0.001428, 'mean_absolute_return': 0.01482, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.003433, 'median_return': -0.00244, 'mean_absolute_return': 0.017797, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': 0.003147, 'median_return': -0.001222, 'mean_absolute_return': 0.022463, 'max_adverse_excursion': -0.037654, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.018072, 'median_return': 0.025442, 'mean_absolute_return': 0.032752, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.053948, 'median_return': 0.065995, 'mean_absolute_return': 0.071832, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.008371, 'median_return': 0.01152, 'mean_absolute_return': 0.013687, 'max_adverse_excursion': -0.022578, 'max_favorable_excursion': 0.035961}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.011104, 'median_return': 0.013131, 'mean_absolute_return': 0.016855, 'max_adverse_excursion': -0.027115, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.007021, 'median_return': -0.020543, 'mean_absolute_return': 0.032266, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.003564, 'median_return': 0.002095, 'mean_absolute_return': 0.046269, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006424, 'median_return': 0.031643, 'mean_absolute_return': 0.095094, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.117141}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.00357`, median `-0.001658`, mae `0.012883`
- 5d: sample `40`, hit `0.45`, avg `-0.0086`, median `-0.004438`, mae `0.015572`
- 10d: sample `40`, hit `0.4`, avg `-0.002227`, median `-0.006017`, mae `0.018397`
- 20d: sample `40`, hit `0.675`, avg `0.013698`, median `0.02086`, mae `0.033944`
- 60d: sample `40`, hit `0.725`, avg `0.043787`, median `0.061042`, mae `0.068862`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.002577`, median `0.003785`, mae `0.015987`
- 5d: sample `60`, hit `0.5667`, avg `0.002153`, median `0.003005`, mae `0.019187`
- 10d: sample `60`, hit `0.4167`, avg `0.002237`, median `-0.006017`, mae `0.026697`
- 20d: sample `60`, hit `0.6667`, avg `0.014637`, median `0.025442`, mae `0.036865`
- 60d: sample `60`, hit `0.7833`, avg `0.044042`, median `0.069439`, mae `0.083012`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.00357`, median `-0.001658`, mae `0.012883`
- 5d: sample `40`, hit `0.45`, avg `-0.0086`, median `-0.004438`, mae `0.015572`
- 10d: sample `40`, hit `0.4`, avg `-0.002227`, median `-0.006017`, mae `0.018397`
- 20d: sample `40`, hit `0.675`, avg `0.013698`, median `0.02086`, mae `0.033944`
- 60d: sample `40`, hit `0.725`, avg `0.043787`, median `0.061042`, mae `0.068862`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.00032`, median `0.001558`, mae `0.017138`
- 5d: sample `40`, hit `0.475`, avg `-0.002323`, median `-0.004438`, mae `0.020354`
- 10d: sample `40`, hit `0.475`, avg `0.006866`, median `-0.0004`, mae `0.023913`
- 20d: sample `40`, hit `0.75`, avg `0.023738`, median `0.029166`, mae `0.032164`
- 60d: sample `40`, hit `0.85`, avg `0.062852`, median `0.073651`, mae `0.076971`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.00357`, median `-0.001658`, mae `0.012883`
- 5d: sample `40`, hit `0.45`, avg `-0.0086`, median `-0.004438`, mae `0.015572`
- 10d: sample `40`, hit `0.4`, avg `-0.002227`, median `-0.006017`, mae `0.018397`
- 20d: sample `40`, hit `0.675`, avg `0.013698`, median `0.02086`, mae `0.033944`
- 60d: sample `40`, hit `0.725`, avg `0.043787`, median `0.061042`, mae `0.068862`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.002577`, median `0.003785`, mae `0.015987`
- 5d: sample `60`, hit `0.5667`, avg `0.002153`, median `0.003005`, mae `0.019187`
- 10d: sample `60`, hit `0.4167`, avg `0.002237`, median `-0.006017`, mae `0.026697`
- 20d: sample `60`, hit `0.6667`, avg `0.014637`, median `0.025442`, mae `0.036865`
- 60d: sample `60`, hit `0.7833`, avg `0.044042`, median `0.069439`, mae `0.083012`

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
- 3d: sample `80`, hit `0.575`, avg `0.001637`, median `0.001558`, mae `0.014536`
- 5d: sample `80`, hit `0.55`, avg `0.000202`, median `0.001303`, mae `0.017561`
- 10d: sample `80`, hit `0.425`, avg `0.000605`, median `-0.007011`, mae `0.024914`
- 20d: sample `80`, hit `0.6625`, avg `0.012663`, median `0.023289`, mae `0.036131`
- 60d: sample `80`, hit `0.7625`, avg `0.042067`, median `0.064905`, mae `0.077647`

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
