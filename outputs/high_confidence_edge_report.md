# High Confidence Edge Report

Generated at: `2026-08-06T14:37:34.797583+00:00`

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
- 3d: sample `80`, hit `0.6`, avg `0.002206`, median `0.004542`, mae `0.014976`
- 5d: sample `80`, hit `0.6875`, avg `0.004269`, median `0.005763`, mae `0.017062`
- 10d: sample `80`, hit `0.5875`, avg `0.006071`, median `0.007467`, mae `0.023918`
- 20d: sample `80`, hit `0.7`, avg `0.013643`, median `0.015261`, mae `0.037196`
- 60d: sample `80`, hit `0.5625`, avg `0.024541`, median `0.032982`, mae `0.068292`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003813`, median `0.001448`, mae `0.013805`
- 5d: sample `8`, hit `0.75`, avg `0.000899`, median `0.004014`, mae `0.010054`
- 10d: sample `8`, hit `0.5`, avg `0.002265`, median `0.011426`, mae `0.018665`
- 20d: sample `8`, hit `0.625`, avg `0.009259`, median `0.020068`, mae `0.026767`
- 60d: sample `8`, hit `0.375`, avg `-0.012738`, median `-0.03081`, mae `0.04907`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.001728`, median `0.000145`, mae `0.006817`
- 5d: sample `8`, hit `0.75`, avg `0.007078`, median `0.010385`, mae `0.012108`
- 10d: sample `8`, hit `0.625`, avg `0.005261`, median `0.012215`, mae `0.01291`
- 20d: sample `8`, hit `0.625`, avg `0.001977`, median `0.007988`, mae `0.017181`
- 60d: sample `8`, hit `0.125`, avg `-0.029143`, median `-0.030864`, mae `0.04989`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.002206, 'median_return': 0.004542, 'mean_absolute_return': 0.014976, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.004269, 'median_return': 0.005763, 'mean_absolute_return': 0.017062, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.006071, 'median_return': 0.007467, 'mean_absolute_return': 0.023918, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.013643, 'median_return': 0.015261, 'mean_absolute_return': 0.037196, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.024541, 'median_return': 0.032982, 'mean_absolute_return': 0.068292, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001728, 'median_return': 0.000145, 'mean_absolute_return': 0.006817, 'max_adverse_excursion': -0.009803, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007078, 'median_return': 0.010385, 'mean_absolute_return': 0.012108, 'max_adverse_excursion': -0.018322, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005261, 'median_return': 0.012215, 'mean_absolute_return': 0.01291, 'max_adverse_excursion': -0.016537, 'max_favorable_excursion': 0.02016}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001977, 'median_return': 0.007988, 'mean_absolute_return': 0.017181, 'max_adverse_excursion': -0.024012, 'max_favorable_excursion': 0.029258}, '60d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.029143, 'median_return': -0.030864, 'mean_absolute_return': 0.04989, 'max_adverse_excursion': -0.08246, 'max_favorable_excursion': 0.082988}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.002259, 'median_return': 0.005642, 'mean_absolute_return': 0.015883, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.003957, 'median_return': 0.005327, 'mean_absolute_return': 0.017613, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.006161, 'median_return': 0.005616, 'mean_absolute_return': 0.025141, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.014939, 'median_return': 0.015661, 'mean_absolute_return': 0.039419, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.030506, 'median_return': 0.046132, 'mean_absolute_return': 0.070336, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.4625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.125, 'both_hit': 23, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.025, 'both_hit': 30, 'both_miss': 10}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.05, 'both_hit': 23, 'both_miss': 17}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.025, 'both_hit': 27, 'both_miss': 13}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.125, 'both_hit': 22, 'both_miss': 18}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.003123, 'median_return': 0.008973, 'mean_absolute_return': 0.016601, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.004041, 'median_return': 0.006133, 'mean_absolute_return': 0.01888, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.006842, 'median_return': 0.00903, 'mean_absolute_return': 0.0267, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.016169, 'median_return': 0.01666, 'mean_absolute_return': 0.041974, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.036908, 'median_return': 0.056189, 'mean_absolute_return': 0.074493, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000546, 'median_return': 0.000145, 'mean_absolute_return': 0.010101, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.038451}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.004954, 'median_return': 0.005084, 'mean_absolute_return': 0.011608, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003758, 'median_return': 0.007467, 'mean_absolute_return': 0.015572, 'max_adverse_excursion': -0.028317, 'max_favorable_excursion': 0.032872}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006064, 'median_return': 0.012291, 'mean_absolute_return': 0.022861, 'max_adverse_excursion': -0.050277, 'max_favorable_excursion': 0.063131}, '60d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.012558, 'median_return': -0.018455, 'mean_absolute_return': 0.049688, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.096921}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000297`, median `0.001999`, mae `0.013448`
- 5d: sample `60`, hit `0.7`, avg `0.00445`, median `0.005327`, mae `0.014873`
- 10d: sample `60`, hit `0.5667`, avg `0.003448`, median `0.005616`, mae `0.021495`
- 20d: sample `60`, hit `0.6833`, avg `0.006842`, median `0.013823`, mae `0.033267`
- 60d: sample `60`, hit `0.5167`, avg `0.013194`, median `0.018072`, mae `0.061442`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007934`, median `0.012584`, mae `0.019561`
- 5d: sample `20`, hit `0.65`, avg `0.003726`, median `0.010281`, mae `0.023628`
- 10d: sample `20`, hit `0.65`, avg `0.013941`, median `0.01246`, mae `0.031187`
- 20d: sample `20`, hit `0.75`, avg `0.034045`, median `0.029029`, mae `0.048983`
- 60d: sample `20`, hit `0.7`, avg `0.058582`, median `0.079128`, mae `0.088842`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000297`, median `0.001999`, mae `0.013448`
- 5d: sample `60`, hit `0.7`, avg `0.00445`, median `0.005327`, mae `0.014873`
- 10d: sample `60`, hit `0.5667`, avg `0.003448`, median `0.005616`, mae `0.021495`
- 20d: sample `60`, hit `0.6833`, avg `0.006842`, median `0.013823`, mae `0.033267`
- 60d: sample `60`, hit `0.5167`, avg `0.013194`, median `0.018072`, mae `0.061442`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000297`, median `0.001999`, mae `0.013448`
- 5d: sample `60`, hit `0.7`, avg `0.00445`, median `0.005327`, mae `0.014873`
- 10d: sample `60`, hit `0.5667`, avg `0.003448`, median `0.005616`, mae `0.021495`
- 20d: sample `60`, hit `0.6833`, avg `0.006842`, median `0.013823`, mae `0.033267`
- 60d: sample `60`, hit `0.5167`, avg `0.013194`, median `0.018072`, mae `0.061442`

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
- 3d: sample `20`, hit `0.75`, avg `0.007934`, median `0.012584`, mae `0.019561`
- 5d: sample `20`, hit `0.65`, avg `0.003726`, median `0.010281`, mae `0.023628`
- 10d: sample `20`, hit `0.65`, avg `0.013941`, median `0.01246`, mae `0.031187`
- 20d: sample `20`, hit `0.75`, avg `0.034045`, median `0.029029`, mae `0.048983`
- 60d: sample `20`, hit `0.7`, avg `0.058582`, median `0.079128`, mae `0.088842`

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
- 3d: sample `20`, hit `0.5`, avg `-0.000546`, median `0.000145`, mae `0.010101`
- 5d: sample `20`, hit `0.8`, avg `0.004954`, median `0.005084`, mae `0.011608`
- 10d: sample `20`, hit `0.55`, avg `0.003758`, median `0.007467`, mae `0.015572`
- 20d: sample `20`, hit `0.65`, avg `0.006064`, median `0.012291`, mae `0.022861`
- 60d: sample `20`, hit `0.3`, avg `-0.012558`, median `-0.018455`, mae `0.049688`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.002206`, median `0.004542`, mae `0.014976`
- 5d: sample `80`, hit `0.6875`, avg `0.004269`, median `0.005763`, mae `0.017062`
- 10d: sample `80`, hit `0.5875`, avg `0.006071`, median `0.007467`, mae `0.023918`
- 20d: sample `80`, hit `0.7`, avg `0.013643`, median `0.015261`, mae `0.037196`
- 60d: sample `80`, hit `0.5625`, avg `0.024541`, median `0.032982`, mae `0.068292`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000297`, median `0.001999`, mae `0.013448`
- 5d: sample `60`, hit `0.7`, avg `0.00445`, median `0.005327`, mae `0.014873`
- 10d: sample `60`, hit `0.5667`, avg `0.003448`, median `0.005616`, mae `0.021495`
- 20d: sample `60`, hit `0.6833`, avg `0.006842`, median `0.013823`, mae `0.033267`
- 60d: sample `60`, hit `0.5167`, avg `0.013194`, median `0.018072`, mae `0.061442`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.002206`, median `0.004542`, mae `0.014976`
- 5d: sample `80`, hit `0.6875`, avg `0.004269`, median `0.005763`, mae `0.017062`
- 10d: sample `80`, hit `0.5875`, avg `0.006071`, median `0.007467`, mae `0.023918`
- 20d: sample `80`, hit `0.7`, avg `0.013643`, median `0.015261`, mae `0.037196`
- 60d: sample `80`, hit `0.5625`, avg `0.024541`, median `0.032982`, mae `0.068292`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000297`, median `0.001999`, mae `0.013448`
- 5d: sample `60`, hit `0.7`, avg `0.00445`, median `0.005327`, mae `0.014873`
- 10d: sample `60`, hit `0.5667`, avg `0.003448`, median `0.005616`, mae `0.021495`
- 20d: sample `60`, hit `0.6833`, avg `0.006842`, median `0.013823`, mae `0.033267`
- 60d: sample `60`, hit `0.5167`, avg `0.013194`, median `0.018072`, mae `0.061442`

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
