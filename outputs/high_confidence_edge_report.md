# High Confidence Edge Report

Generated at: `2026-08-04T23:50:50.627601+00:00`

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
- 3d: sample `60`, hit `0.5833`, avg `-6.1e-05`, median `0.001999`, mae `0.012187`
- 5d: sample `60`, hit `0.7`, avg `0.00292`, median `0.005084`, mae `0.01367`
- 10d: sample `60`, hit `0.4833`, avg `-0.000406`, median `-0.001676`, mae `0.02035`
- 20d: sample `60`, hit `0.6167`, avg `0.003837`, median `0.01011`, mae `0.030138`
- 60d: sample `60`, hit `0.5333`, avg `0.014565`, median `0.018072`, mae `0.059532`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.007649`, median `0.010664`, mae `0.015258`
- 5d: sample `20`, hit `0.7`, avg `0.006476`, median `0.010908`, mae `0.017633`
- 10d: sample `20`, hit `0.65`, avg `0.01202`, median `0.016085`, mae `0.024053`
- 20d: sample `20`, hit `0.65`, avg `0.010483`, median `0.010824`, mae `0.034829`
- 60d: sample `20`, hit `0.65`, avg `0.02114`, median `0.022085`, mae `0.0708`

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
- 3d: sample `8`, hit `0.5`, avg `-0.004255`, median `0.001448`, mae `0.014248`
- 5d: sample `8`, hit `0.625`, avg `-0.00032`, median `0.003005`, mae `0.009943`
- 10d: sample `8`, hit `0.375`, avg `-0.001054`, median `-0.007011`, mae `0.019127`
- 20d: sample `8`, hit `0.5`, avg `0.003945`, median `0.020068`, mae `0.029765`
- 60d: sample `8`, hit `0.375`, avg `-0.015481`, median `-0.03081`, mae `0.051813`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004255`, median `0.001448`, mae `0.014248`
- 5d: sample `8`, hit `0.625`, avg `-0.00032`, median `0.003005`, mae `0.009943`
- 10d: sample `8`, hit `0.375`, avg `-0.001054`, median `-0.007011`, mae `0.019127`
- 20d: sample `8`, hit `0.5`, avg `0.003945`, median `0.020068`, mae `0.029765`
- 60d: sample `8`, hit `0.375`, avg `-0.015481`, median `-0.03081`, mae `0.051813`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': -6.1e-05, 'median_return': 0.001999, 'mean_absolute_return': 0.012187, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.00292, 'median_return': 0.005084, 'mean_absolute_return': 0.01367, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.000406, 'median_return': -0.001676, 'mean_absolute_return': 0.02035, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.003837, 'median_return': 0.01011, 'mean_absolute_return': 0.030138, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.014565, 'median_return': 0.018072, 'mean_absolute_return': 0.059532, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004255, 'median_return': 0.001448, 'mean_absolute_return': 0.014248, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00032, 'median_return': 0.003005, 'mean_absolute_return': 0.009943, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.001054, 'median_return': -0.007011, 'mean_absolute_return': 0.019127, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003945, 'median_return': 0.020068, 'mean_absolute_return': 0.029765, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.015481, 'median_return': -0.03081, 'mean_absolute_return': 0.051813, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.002547, 'median_return': 0.004569, 'mean_absolute_return': 0.012811, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.033392}, '5d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.004267, 'median_return': 0.006133, 'mean_absolute_return': 0.015185, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.003118, 'median_return': 0.004807, 'mean_absolute_return': 0.021514, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.067569}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.005671, 'median_return': 0.01011, 'mean_absolute_return': 0.031482, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.019729, 'median_return': 0.02283, 'mean_absolute_return': 0.06352, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.162638}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.55}, '60d': {'sample_size': 80, 'hit_rate': 0.4875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.1, 'both_hit': 14, 'both_miss': 6}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.15, 'both_hit': 12, 'both_miss': 8}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 14, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.175, 'both_hit': 16, 'both_miss': 4}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.001867, 'median_return': 0.004542, 'mean_absolute_return': 0.012954, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.033392}, '5d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.003809, 'median_return': 0.005327, 'mean_absolute_return': 0.014661, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.002701, 'median_return': 0.003491, 'mean_absolute_return': 0.021275, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.067569}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.005498, 'median_return': 0.01011, 'mean_absolute_return': 0.031311, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.016208, 'median_return': 0.020144, 'mean_absolute_return': 0.062349, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.162638}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.002364`, median `0.000603`, mae `0.011498`
- 5d: sample `40`, hit `0.7`, avg `0.001255`, median `0.004014`, mae `0.011613`
- 10d: sample `40`, hit `0.425`, avg `-0.001994`, median `-0.003071`, mae `0.016549`
- 20d: sample `40`, hit `0.575`, avg `0.004252`, median `0.007988`, mae `0.025172`
- 60d: sample `40`, hit `0.4`, avg `-0.001098`, median `-0.012792`, mae `0.051671`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.007649`, median `0.010664`, mae `0.015258`
- 5d: sample `20`, hit `0.7`, avg `0.006476`, median `0.010908`, mae `0.017633`
- 10d: sample `20`, hit `0.65`, avg `0.01202`, median `0.016085`, mae `0.024053`
- 20d: sample `20`, hit `0.65`, avg `0.010483`, median `0.010824`, mae `0.034829`
- 60d: sample `20`, hit `0.65`, avg `0.02114`, median `0.022085`, mae `0.0708`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.002364`, median `0.000603`, mae `0.011498`
- 5d: sample `40`, hit `0.7`, avg `0.001255`, median `0.004014`, mae `0.011613`
- 10d: sample `40`, hit `0.425`, avg `-0.001994`, median `-0.003071`, mae `0.016549`
- 20d: sample `40`, hit `0.575`, avg `0.004252`, median `0.007988`, mae `0.025172`
- 60d: sample `40`, hit `0.4`, avg `-0.001098`, median `-0.012792`, mae `0.051671`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.00264`, median `0.003785`, mae `0.014436`
- 5d: sample `20`, hit `0.6`, avg `-0.001378`, median `0.003829`, mae `0.013382`
- 10d: sample `20`, hit `0.45`, avg `-0.001728`, median `-0.003071`, mae `0.019283`
- 20d: sample `20`, hit `0.65`, avg `0.010362`, median `0.020068`, mae `0.029617`
- 60d: sample `20`, hit `0.5`, avg `0.012099`, median `0.003095`, mae `0.057762`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.007649`, median `0.010664`, mae `0.015258`
- 5d: sample `20`, hit `0.7`, avg `0.006476`, median `0.010908`, mae `0.017633`
- 10d: sample `20`, hit `0.65`, avg `0.01202`, median `0.016085`, mae `0.024053`
- 20d: sample `20`, hit `0.65`, avg `0.010483`, median `0.010824`, mae `0.034829`
- 60d: sample `20`, hit `0.65`, avg `0.02114`, median `0.022085`, mae `0.0708`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.002364`, median `0.000603`, mae `0.011498`
- 5d: sample `40`, hit `0.7`, avg `0.001255`, median `0.004014`, mae `0.011613`
- 10d: sample `40`, hit `0.425`, avg `-0.001994`, median `-0.003071`, mae `0.016549`
- 20d: sample `40`, hit `0.575`, avg `0.004252`, median `0.007988`, mae `0.025172`
- 60d: sample `40`, hit `0.4`, avg `-0.001098`, median `-0.012792`, mae `0.051671`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004546`, median `0.005642`, mae `0.013565`
- 5d: sample `20`, hit `0.7`, avg `0.006248`, median `0.010393`, mae `0.017784`
- 10d: sample `20`, hit `0.6`, avg `0.002772`, median `0.005616`, mae `0.027951`
- 20d: sample `20`, hit `0.7`, avg `0.003006`, median `0.014007`, mae `0.04007`
- 60d: sample `20`, hit `0.8`, avg `0.045889`, median `0.064286`, mae `0.075256`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.00264`, median `0.003785`, mae `0.014436`
- 5d: sample `20`, hit `0.6`, avg `-0.001378`, median `0.003829`, mae `0.013382`
- 10d: sample `20`, hit `0.45`, avg `-0.001728`, median `-0.003071`, mae `0.019283`
- 20d: sample `20`, hit `0.65`, avg `0.010362`, median `0.020068`, mae `0.029617`
- 60d: sample `20`, hit `0.5`, avg `0.012099`, median `0.003095`, mae `0.057762`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.007649`, median `0.010664`, mae `0.015258`
- 5d: sample `20`, hit `0.7`, avg `0.006476`, median `0.010908`, mae `0.017633`
- 10d: sample `20`, hit `0.65`, avg `0.01202`, median `0.016085`, mae `0.024053`
- 20d: sample `20`, hit `0.65`, avg `0.010483`, median `0.010824`, mae `0.034829`
- 60d: sample `20`, hit `0.65`, avg `0.02114`, median `0.022085`, mae `0.0708`

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
- 3d: sample `80`, hit `0.6375`, avg `0.001867`, median `0.004542`, mae `0.012954`
- 5d: sample `80`, hit `0.7`, avg `0.003809`, median `0.005327`, mae `0.014661`
- 10d: sample `80`, hit `0.525`, avg `0.002701`, median `0.003491`, mae `0.021275`
- 20d: sample `80`, hit `0.625`, avg `0.005498`, median `0.01011`, mae `0.031311`
- 60d: sample `80`, hit `0.5625`, avg `0.016208`, median `0.020144`, mae `0.062349`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `-6.1e-05`, median `0.001999`, mae `0.012187`
- 5d: sample `60`, hit `0.7`, avg `0.00292`, median `0.005084`, mae `0.01367`
- 10d: sample `60`, hit `0.4833`, avg `-0.000406`, median `-0.001676`, mae `0.02035`
- 20d: sample `60`, hit `0.6167`, avg `0.003837`, median `0.01011`, mae `0.030138`
- 60d: sample `60`, hit `0.5333`, avg `0.014565`, median `0.018072`, mae `0.059532`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.001867`, median `0.004542`, mae `0.012954`
- 5d: sample `80`, hit `0.7`, avg `0.003809`, median `0.005327`, mae `0.014661`
- 10d: sample `80`, hit `0.525`, avg `0.002701`, median `0.003491`, mae `0.021275`
- 20d: sample `80`, hit `0.625`, avg `0.005498`, median `0.01011`, mae `0.031311`
- 60d: sample `80`, hit `0.5625`, avg `0.016208`, median `0.020144`, mae `0.062349`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `-6.1e-05`, median `0.001999`, mae `0.012187`
- 5d: sample `60`, hit `0.7`, avg `0.00292`, median `0.005084`, mae `0.01367`
- 10d: sample `60`, hit `0.4833`, avg `-0.000406`, median `-0.001676`, mae `0.02035`
- 20d: sample `60`, hit `0.6167`, avg `0.003837`, median `0.01011`, mae `0.030138`
- 60d: sample `60`, hit `0.5333`, avg `0.014565`, median `0.018072`, mae `0.059532`

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
