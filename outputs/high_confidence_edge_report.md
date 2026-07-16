# High Confidence Edge Report

Generated at: `2026-07-16T21:32:18.591647+00:00`

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
- 3d: sample `40`, hit `0.475`, avg `-0.00652`, median `-0.0002`, mae `0.014958`
- 5d: sample `40`, hit `0.4`, avg `-0.007658`, median `-0.002525`, mae `0.016786`
- 10d: sample `40`, hit `0.225`, avg `-0.011541`, median `-0.014881`, mae `0.020399`
- 20d: sample `40`, hit `0.625`, avg `0.004637`, median `0.016437`, mae `0.037446`
- 60d: sample `40`, hit `0.575`, avg `0.010622`, median `0.029066`, mae `0.080922`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003044`, median `0.000603`, mae `0.014229`
- 5d: sample `40`, hit `0.575`, avg `0.000991`, median `0.001695`, mae `0.017553`
- 10d: sample `40`, hit `0.55`, avg `0.0042`, median `0.001455`, mae `0.024227`
- 20d: sample `40`, hit `0.675`, avg `0.016398`, median `0.014918`, mae `0.026511`
- 60d: sample `40`, hit `0.625`, avg `0.030148`, median `0.043741`, mae `0.058884`

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
- 3d: sample `8`, hit `0.25`, avg `-0.014876`, median `-0.010033`, mae `0.021558`
- 5d: sample `8`, hit `0.375`, avg `-0.018532`, median `-0.022295`, mae `0.022979`
- 10d: sample `8`, hit `0.0`, avg `-0.015696`, median `-0.011432`, mae `0.015696`
- 20d: sample `8`, hit `0.75`, avg `0.016079`, median `0.029166`, mae `0.046206`
- 60d: sample `8`, hit `0.875`, avg `0.049114`, median `0.072696`, mae `0.084395`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.014876`, median `-0.010033`, mae `0.021558`
- 5d: sample `8`, hit `0.375`, avg `-0.018532`, median `-0.022295`, mae `0.022979`
- 10d: sample `8`, hit `0.0`, avg `-0.015696`, median `-0.011432`, mae `0.015696`
- 20d: sample `8`, hit `0.75`, avg `0.016079`, median `0.029166`, mae `0.046206`
- 60d: sample `8`, hit `0.875`, avg `0.049114`, median `0.072696`, mae `0.084395`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.00652, 'median_return': -0.0002, 'mean_absolute_return': 0.014958, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.022026}, '5d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.007658, 'median_return': -0.002525, 'mean_absolute_return': 0.016786, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.022754}, '10d': {'sample_size': 40, 'hit_rate': 0.225, 'avg_return': -0.011541, 'median_return': -0.014881, 'mean_absolute_return': 0.020399, 'max_adverse_excursion': -0.047759, 'max_favorable_excursion': 0.04263}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.004637, 'median_return': 0.016437, 'mean_absolute_return': 0.037446, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.010622, 'median_return': 0.029066, 'mean_absolute_return': 0.080922, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.014876, 'median_return': -0.010033, 'mean_absolute_return': 0.021558, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.018532, 'median_return': -0.022295, 'mean_absolute_return': 0.022979, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.015696, 'median_return': -0.011432, 'mean_absolute_return': 0.015696, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016079, 'median_return': 0.029166, 'mean_absolute_return': 0.046206, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.049114, 'median_return': 0.072696, 'mean_absolute_return': 0.084395, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.00366, 'median_return': 0.000603, 'mean_absolute_return': 0.01382, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001644, 'median_return': 0.000415, 'mean_absolute_return': 0.016524, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.002335, 'median_return': -0.007491, 'mean_absolute_return': 0.023048, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.0099, 'median_return': 0.01128, 'mean_absolute_return': 0.030398, 'max_adverse_excursion': -0.098604, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.017193, 'median_return': 0.029164, 'mean_absolute_return': 0.068293, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.004353, 'median_return': -0.0002, 'mean_absolute_return': 0.01573, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.003405, 'median_return': -0.000413, 'mean_absolute_return': 0.017251, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.00353, 'median_return': -0.010327, 'mean_absolute_return': 0.024463, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.01089, 'median_return': 0.014918, 'mean_absolute_return': 0.035406, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.022754, 'median_return': 0.044771, 'mean_absolute_return': 0.079273, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19082}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.00607, 'median_return': 0.000603, 'mean_absolute_return': 0.011186, 'max_adverse_excursion': -0.03466, 'max_favorable_excursion': 0.011487}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.00312, 'median_return': 0.001303, 'mean_absolute_return': 0.016927, 'max_adverse_excursion': -0.047389, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.004092, 'median_return': -0.007117, 'mean_absolute_return': 0.015862, 'max_adverse_excursion': -0.03706, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.009399, 'median_return': 0.015416, 'mean_absolute_return': 0.021695, 'max_adverse_excursion': -0.042211, 'max_favorable_excursion': 0.046563}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.013278, 'median_return': 0.029164, 'mean_absolute_return': 0.041793, 'max_adverse_excursion': -0.08246, 'max_favorable_excursion': 0.077439}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.004353`, median `-0.0002`, mae `0.01573`
- 5d: sample `60`, hit `0.4667`, avg `-0.003405`, median `-0.000413`, mae `0.017251`
- 10d: sample `60`, hit `0.3833`, avg `-0.00353`, median `-0.010327`, mae `0.024463`
- 20d: sample `60`, hit `0.6667`, avg `0.01089`, median `0.014918`, mae `0.035406`
- 60d: sample `60`, hit `0.6`, avg `0.022754`, median `0.044771`, mae `0.079273`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003044`, median `0.000603`, mae `0.014229`
- 5d: sample `40`, hit `0.575`, avg `0.000991`, median `0.001695`, mae `0.017553`
- 10d: sample `40`, hit `0.55`, avg `0.0042`, median `0.001455`, mae `0.024227`
- 20d: sample `40`, hit `0.675`, avg `0.016398`, median `0.014918`, mae `0.026511`
- 60d: sample `40`, hit `0.625`, avg `0.030148`, median `0.043741`, mae `0.058884`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011174`, median `-0.010033`, mae `0.017641`
- 5d: sample `20`, hit `0.35`, avg `-0.012393`, median `-0.004989`, mae `0.017111`
- 10d: sample `20`, hit `0.2`, avg `-0.010775`, median `-0.011432`, mae `0.016157`
- 20d: sample `20`, hit `0.65`, avg `0.007788`, median `0.021759`, mae `0.035407`
- 60d: sample `20`, hit `0.6`, avg `0.024932`, median `0.046132`, mae `0.073186`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.005596`, median `-0.009383`, mae `0.017457`
- 5d: sample `40`, hit `0.475`, avg `-0.003645`, median `-0.002525`, mae `0.017646`
- 10d: sample `40`, hit `0.45`, avg `0.000858`, median `-0.003071`, mae `0.024374`
- 20d: sample `40`, hit `0.7`, avg `0.015593`, median `0.020068`, mae `0.033367`
- 60d: sample `40`, hit `0.625`, avg `0.035975`, median `0.054272`, mae `0.07458`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003044`, median `0.000603`, mae `0.014229`
- 5d: sample `40`, hit `0.575`, avg `0.000991`, median `0.001695`, mae `0.017553`
- 10d: sample `40`, hit `0.55`, avg `0.0042`, median `0.001455`, mae `0.024227`
- 20d: sample `40`, hit `0.675`, avg `0.016398`, median `0.014918`, mae `0.026511`
- 60d: sample `40`, hit `0.625`, avg `0.030148`, median `0.043741`, mae `0.058884`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011174`, median `-0.010033`, mae `0.017641`
- 5d: sample `20`, hit `0.35`, avg `-0.012393`, median `-0.004989`, mae `0.017111`
- 10d: sample `20`, hit `0.2`, avg `-0.010775`, median `-0.011432`, mae `0.016157`
- 20d: sample `20`, hit `0.65`, avg `0.007788`, median `0.021759`, mae `0.035407`
- 60d: sample `20`, hit `0.6`, avg `0.024932`, median `0.046132`, mae `0.073186`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.005596`, median `-0.009383`, mae `0.017457`
- 5d: sample `40`, hit `0.475`, avg `-0.003645`, median `-0.002525`, mae `0.017646`
- 10d: sample `40`, hit `0.45`, avg `0.000858`, median `-0.003071`, mae `0.024374`
- 20d: sample `40`, hit `0.7`, avg `0.015593`, median `0.020068`, mae `0.033367`
- 60d: sample `40`, hit `0.625`, avg `0.035975`, median `0.054272`, mae `0.07458`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003044`, median `0.000603`, mae `0.014229`
- 5d: sample `40`, hit `0.575`, avg `0.000991`, median `0.001695`, mae `0.017553`
- 10d: sample `40`, hit `0.55`, avg `0.0042`, median `0.001455`, mae `0.024227`
- 20d: sample `40`, hit `0.675`, avg `0.016398`, median `0.014918`, mae `0.026511`
- 60d: sample `40`, hit `0.625`, avg `0.030148`, median `0.043741`, mae `0.058884`

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
- 3d: sample `40`, hit `0.475`, avg `-0.00652`, median `-0.0002`, mae `0.014958`
- 5d: sample `40`, hit `0.4`, avg `-0.007658`, median `-0.002525`, mae `0.016786`
- 10d: sample `40`, hit `0.225`, avg `-0.011541`, median `-0.014881`, mae `0.020399`
- 20d: sample `40`, hit `0.625`, avg `0.004637`, median `0.016437`, mae `0.037446`
- 60d: sample `40`, hit `0.575`, avg `0.010622`, median `0.029066`, mae `0.080922`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00607`, median `0.000603`, mae `0.011186`
- 5d: sample `20`, hit `0.55`, avg `-0.00312`, median `0.001303`, mae `0.016927`
- 10d: sample `20`, hit `0.4`, avg `-0.004092`, median `-0.007117`, mae `0.015862`
- 20d: sample `20`, hit `0.6`, avg `0.009399`, median `0.015416`, mae `0.021695`
- 60d: sample `20`, hit `0.6`, avg `0.013278`, median `0.029164`, mae `0.041793`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.003968`, median `0.000744`, mae `0.01173`
- 5d: sample `40`, hit `0.5`, avg `-0.003021`, median `0.000688`, mae `0.016694`
- 10d: sample `40`, hit `0.325`, avg `-0.0082`, median `-0.010413`, mae `0.020251`
- 20d: sample `40`, hit `0.6`, avg `0.005442`, median `0.012291`, mae `0.030591`
- 60d: sample `40`, hit `0.575`, avg `0.004795`, median `0.018072`, mae `0.065226`

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
