# High Confidence Edge Report

Generated at: `2026-08-05T21:41:35.457971+00:00`

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
- 3d: sample `80`, hit `0.6`, avg `0.001416`, median `0.004004`, mae `0.014284`
- 5d: sample `80`, hit `0.6625`, avg `0.003466`, median `0.005319`, mae `0.016653`
- 10d: sample `80`, hit `0.55`, avg `0.004241`, median `0.005616`, mae `0.023913`
- 20d: sample `80`, hit `0.6875`, avg `0.00947`, median `0.013178`, mae `0.03726`
- 60d: sample `80`, hit `0.5375`, avg `0.021114`, median `0.020144`, mae `0.064251`

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
- 3d: sample `8`, hit `0.625`, avg `-0.00181`, median `0.006714`, mae `0.014347`
- 5d: sample `8`, hit `0.75`, avg `0.003233`, median `0.004014`, mae `0.012387`
- 10d: sample `8`, hit `0.5`, avg `0.004693`, median `0.021953`, mae `0.021093`
- 20d: sample `8`, hit `0.625`, avg `0.011417`, median `0.022652`, mae `0.028925`
- 60d: sample `8`, hit `0.375`, avg `-0.011059`, median `-0.02013`, mae `0.047391`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.00181`, median `0.006714`, mae `0.014347`
- 5d: sample `8`, hit `0.75`, avg `0.003233`, median `0.004014`, mae `0.012387`
- 10d: sample `8`, hit `0.5`, avg `0.004693`, median `0.021953`, mae `0.021093`
- 20d: sample `8`, hit `0.625`, avg `0.011417`, median `0.022652`, mae `0.028925`
- 60d: sample `8`, hit `0.375`, avg `-0.011059`, median `-0.02013`, mae `0.047391`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.001416, 'median_return': 0.004004, 'mean_absolute_return': 0.014284, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.003466, 'median_return': 0.005319, 'mean_absolute_return': 0.016653, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.004241, 'median_return': 0.005616, 'mean_absolute_return': 0.023913, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.00947, 'median_return': 0.013178, 'mean_absolute_return': 0.03726, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.021114, 'median_return': 0.020144, 'mean_absolute_return': 0.064251, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00181, 'median_return': 0.006714, 'mean_absolute_return': 0.014347, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.003233, 'median_return': 0.004014, 'mean_absolute_return': 0.012387, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004693, 'median_return': 0.021953, 'mean_absolute_return': 0.021093, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011417, 'median_return': 0.022652, 'mean_absolute_return': 0.028925, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011059, 'median_return': -0.02013, 'mean_absolute_return': 0.047391, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.001775, 'median_return': 0.004004, 'mean_absolute_return': 0.014276, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.003492, 'median_return': 0.005327, 'mean_absolute_return': 0.017127, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.00419, 'median_return': 0.005616, 'mean_absolute_return': 0.024227, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.009254, 'median_return': 0.012958, 'mean_absolute_return': 0.038186, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.024689, 'median_return': 0.030553, 'mean_absolute_return': 0.066125, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6}, '5d': {'sample_size': 80, 'hit_rate': 0.6625}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.1, 'both_hit': 14, 'both_miss': 6}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.275, 'both_hit': 12, 'both_miss': 8}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.075, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.25, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.0, 'both_hit': 13, 'both_miss': 7}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.002071, 'median_return': 0.006714, 'mean_absolute_return': 0.015678, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.00297, 'median_return': 0.005327, 'mean_absolute_return': 0.018335, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.004402, 'median_return': 0.005616, 'mean_absolute_return': 0.026694, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.010605, 'median_return': 0.014007, 'mean_absolute_return': 0.04206, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.032338, 'median_return': 0.046677, 'mean_absolute_return': 0.069106, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000546, 'median_return': 0.000145, 'mean_absolute_return': 0.010101, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.038451}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.004954, 'median_return': 0.005084, 'mean_absolute_return': 0.011608, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003758, 'median_return': 0.007467, 'mean_absolute_return': 0.015572, 'max_adverse_excursion': -0.028317, 'max_favorable_excursion': 0.032872}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006064, 'median_return': 0.012291, 'mean_absolute_return': 0.022861, 'max_adverse_excursion': -0.050277, 'max_favorable_excursion': 0.063131}, '60d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.012558, 'median_return': -0.018455, 'mean_absolute_return': 0.049688, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.096921}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.000163`, median `0.001999`, mae `0.013131`
- 5d: sample `60`, hit `0.6833`, avg `0.00361`, median `0.005319`, mae `0.014468`
- 10d: sample `60`, hit `0.55`, avg `0.00215`, median `0.005616`, mae `0.02091`
- 20d: sample `60`, hit `0.6667`, avg `0.004187`, median `0.012958`, mae `0.031689`
- 60d: sample `60`, hit `0.5`, avg `0.010028`, median `0.012092`, mae `0.057509`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005177`, median `0.009966`, mae `0.017741`
- 5d: sample `20`, hit `0.6`, avg `0.003033`, median `0.010061`, mae `0.023209`
- 10d: sample `20`, hit `0.55`, avg `0.010512`, median `0.011168`, mae `0.032924`
- 20d: sample `20`, hit `0.75`, avg `0.025319`, median `0.015661`, mae `0.053975`
- 60d: sample `20`, hit `0.65`, avg `0.054371`, median `0.079128`, mae `0.084477`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.000163`, median `0.001999`, mae `0.013131`
- 5d: sample `60`, hit `0.6833`, avg `0.00361`, median `0.005319`, mae `0.014468`
- 10d: sample `60`, hit `0.55`, avg `0.00215`, median `0.005616`, mae `0.02091`
- 20d: sample `60`, hit `0.6667`, avg `0.004187`, median `0.012958`, mae `0.031689`
- 60d: sample `60`, hit `0.5`, avg `0.010028`, median `0.012092`, mae `0.057509`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005177`, median `0.009966`, mae `0.017741`
- 5d: sample `20`, hit `0.6`, avg `0.003033`, median `0.010061`, mae `0.023209`
- 10d: sample `20`, hit `0.55`, avg `0.010512`, median `0.011168`, mae `0.032924`
- 20d: sample `20`, hit `0.75`, avg `0.025319`, median `0.015661`, mae `0.053975`
- 60d: sample `20`, hit `0.65`, avg `0.054371`, median `0.079128`, mae `0.084477`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.000163`, median `0.001999`, mae `0.013131`
- 5d: sample `60`, hit `0.6833`, avg `0.00361`, median `0.005319`, mae `0.014468`
- 10d: sample `60`, hit `0.55`, avg `0.00215`, median `0.005616`, mae `0.02091`
- 20d: sample `60`, hit `0.6667`, avg `0.004187`, median `0.012958`, mae `0.031689`
- 60d: sample `60`, hit `0.5`, avg `0.010028`, median `0.012092`, mae `0.057509`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005177`, median `0.009966`, mae `0.017741`
- 5d: sample `20`, hit `0.6`, avg `0.003033`, median `0.010061`, mae `0.023209`
- 10d: sample `20`, hit `0.55`, avg `0.010512`, median `0.011168`, mae `0.032924`
- 20d: sample `20`, hit `0.75`, avg `0.025319`, median `0.015661`, mae `0.053975`
- 60d: sample `20`, hit `0.65`, avg `0.054371`, median `0.079128`, mae `0.084477`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.001416`, median `0.004004`, mae `0.014284`
- 5d: sample `80`, hit `0.6625`, avg `0.003466`, median `0.005319`, mae `0.016653`
- 10d: sample `80`, hit `0.55`, avg `0.004241`, median `0.005616`, mae `0.023913`
- 20d: sample `80`, hit `0.6875`, avg `0.00947`, median `0.013178`, mae `0.03726`
- 60d: sample `80`, hit `0.5375`, avg `0.021114`, median `0.020144`, mae `0.064251`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.001416`, median `0.004004`, mae `0.014284`
- 5d: sample `80`, hit `0.6625`, avg `0.003466`, median `0.005319`, mae `0.016653`
- 10d: sample `80`, hit `0.55`, avg `0.004241`, median `0.005616`, mae `0.023913`
- 20d: sample `80`, hit `0.6875`, avg `0.00947`, median `0.013178`, mae `0.03726`
- 60d: sample `80`, hit `0.5375`, avg `0.021114`, median `0.020144`, mae `0.064251`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.001416`, median `0.004004`, mae `0.014284`
- 5d: sample `80`, hit `0.6625`, avg `0.003466`, median `0.005319`, mae `0.016653`
- 10d: sample `80`, hit `0.55`, avg `0.004241`, median `0.005616`, mae `0.023913`
- 20d: sample `80`, hit `0.6875`, avg `0.00947`, median `0.013178`, mae `0.03726`
- 60d: sample `80`, hit `0.5375`, avg `0.021114`, median `0.020144`, mae `0.064251`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.001416`, median `0.004004`, mae `0.014284`
- 5d: sample `80`, hit `0.6625`, avg `0.003466`, median `0.005319`, mae `0.016653`
- 10d: sample `80`, hit `0.55`, avg `0.004241`, median `0.005616`, mae `0.023913`
- 20d: sample `80`, hit `0.6875`, avg `0.00947`, median `0.013178`, mae `0.03726`
- 60d: sample `80`, hit `0.5375`, avg `0.021114`, median `0.020144`, mae `0.064251`

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
