# High Confidence Edge Report

Generated at: `2026-08-17T23:34:08.594926+00:00`

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
- 3d: sample `40`, hit `0.575`, avg `0.002084`, median `0.005642`, mae `0.015016`
- 5d: sample `40`, hit `0.575`, avg `0.00187`, median `0.003209`, mae `0.017914`
- 10d: sample `40`, hit `0.6`, avg `0.006032`, median `0.010691`, mae `0.028137`
- 20d: sample `40`, hit `0.7`, avg `0.010277`, median `0.024743`, mae `0.050625`
- 60d: sample `40`, hit `0.6`, avg `0.019265`, median `0.045044`, mae `0.082824`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003001`, median `0.002067`, mae `0.012252`
- 5d: sample `40`, hit `0.675`, avg `0.003311`, median `0.001695`, mae `0.014548`
- 10d: sample `40`, hit `0.475`, avg `0.003429`, median `-0.001676`, mae `0.026539`
- 20d: sample `40`, hit `0.525`, avg `0.010272`, median `0.007988`, mae `0.04264`
- 60d: sample `40`, hit `0.6`, avg `0.023867`, median `0.020144`, mae `0.059858`

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
- 3d: sample `8`, hit `0.5`, avg `-0.00677`, median `0.001448`, mae `0.018219`
- 5d: sample `8`, hit `0.625`, avg `-0.000561`, median `0.005319`, mae `0.013219`
- 10d: sample `8`, hit `0.625`, avg `0.002081`, median `0.011426`, mae `0.019229`
- 20d: sample `8`, hit `0.625`, avg `0.003814`, median `0.022652`, mae `0.03338`
- 60d: sample `8`, hit `0.5`, avg `0.012687`, median `0.030553`, mae `0.049705`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.00677`, median `0.001448`, mae `0.018219`
- 5d: sample `8`, hit `0.625`, avg `-0.000561`, median `0.005319`, mae `0.013219`
- 10d: sample `8`, hit `0.625`, avg `0.002081`, median `0.011426`, mae `0.019229`
- 20d: sample `8`, hit `0.625`, avg `0.003814`, median `0.022652`, mae `0.03338`
- 60d: sample `8`, hit `0.5`, avg `0.012687`, median `0.030553`, mae `0.049705`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002084, 'median_return': 0.005642, 'mean_absolute_return': 0.015016, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030961}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.00187, 'median_return': 0.003209, 'mean_absolute_return': 0.017914, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.006032, 'median_return': 0.010691, 'mean_absolute_return': 0.028137, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.010277, 'median_return': 0.024743, 'mean_absolute_return': 0.050625, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.019265, 'median_return': 0.045044, 'mean_absolute_return': 0.082824, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003001, 'median_return': 0.002067, 'mean_absolute_return': 0.012252, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.003311, 'median_return': 0.001695, 'mean_absolute_return': 0.014548, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.003429, 'median_return': -0.001676, 'mean_absolute_return': 0.026539, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.010272, 'median_return': 0.007988, 'mean_absolute_return': 0.04264, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.023867, 'median_return': 0.020144, 'mean_absolute_return': 0.059858, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.171512}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.00677, 'median_return': 0.001448, 'mean_absolute_return': 0.018219, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000561, 'median_return': 0.005319, 'mean_absolute_return': 0.013219, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002081, 'median_return': 0.011426, 'mean_absolute_return': 0.019229, 'max_adverse_excursion': -0.033507, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003814, 'median_return': 0.022652, 'mean_absolute_return': 0.03338, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.012687, 'median_return': 0.030553, 'mean_absolute_return': 0.049705, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.003577, 'median_return': 0.002997, 'mean_absolute_return': 0.013125, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.002941, 'median_return': 0.003005, 'mean_absolute_return': 0.016565, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.005025, 'median_return': 0.00903, 'mean_absolute_return': 0.028239, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.010993, 'median_return': 0.01666, 'mean_absolute_return': 0.048105, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.022552, 'median_return': 0.032982, 'mean_absolute_return': 0.073745, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.625}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.0, 'both_hit': 43, 'both_miss': 37}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.007975, 'median_return': 0.008336, 'mean_absolute_return': 0.01433, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.004528, 'median_return': 0.003684, 'mean_absolute_return': 0.018912, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.011915, 'median_return': 0.016085, 'mean_absolute_return': 0.034001, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.018859, 'median_return': 0.029018, 'mean_absolute_return': 0.060107, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.039535, 'median_return': 0.056189, 'mean_absolute_return': 0.087699, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.00289, 'median_return': 0.000145, 'mean_absolute_return': 0.012938, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.000653, 'median_return': 0.001695, 'mean_absolute_return': 0.01355, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.002454, 'median_return': -0.003071, 'mean_absolute_return': 0.020674, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001691, 'median_return': 0.008658, 'mean_absolute_return': 0.033158, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.003597, 'median_return': -0.004982, 'mean_absolute_return': 0.054983, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.099719}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000143`, median `0.000603`, mae `0.012974`
- 5d: sample `60`, hit `0.6333`, avg `0.001665`, median `0.003197`, mae `0.015264`
- 10d: sample `60`, hit `0.5`, avg `0.001259`, median `0.001517`, mae `0.025006`
- 20d: sample `60`, hit `0.6`, avg `0.003769`, median `0.01666`, mae `0.042679`
- 60d: sample `60`, hit `0.5333`, avg `0.011059`, median `0.030553`, mae `0.07163`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00974`, median `0.010849`, mae `0.015613`
- 5d: sample `20`, hit `0.6`, avg `0.005366`, median `0.003684`, mae `0.019131`
- 10d: sample `20`, hit `0.65`, avg `0.015145`, median `0.016536`, mae `0.034333`
- 20d: sample `20`, hit `0.65`, avg `0.029792`, median `0.028499`, mae `0.058492`
- 60d: sample `20`, hit `0.8`, avg `0.053087`, median `0.059829`, mae `0.070475`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000143`, median `0.000603`, mae `0.012974`
- 5d: sample `60`, hit `0.6333`, avg `0.001665`, median `0.003197`, mae `0.015264`
- 10d: sample `60`, hit `0.5`, avg `0.001259`, median `0.001517`, mae `0.025006`
- 20d: sample `60`, hit `0.6`, avg `0.003769`, median `0.01666`, mae `0.042679`
- 60d: sample `60`, hit `0.5333`, avg `0.011059`, median `0.030553`, mae `0.07163`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00974`, median `0.010849`, mae `0.015613`
- 5d: sample `20`, hit `0.6`, avg `0.005366`, median `0.003684`, mae `0.019131`
- 10d: sample `20`, hit `0.65`, avg `0.015145`, median `0.016536`, mae `0.034333`
- 20d: sample `20`, hit `0.65`, avg `0.029792`, median `0.028499`, mae `0.058492`
- 60d: sample `20`, hit `0.8`, avg `0.053087`, median `0.059829`, mae `0.070475`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002042`, median `0.001448`, mae `0.016983`
- 5d: sample `20`, hit `0.5`, avg `4.9e-05`, median `0.003005`, mae `0.017135`
- 10d: sample `20`, hit `0.6`, avg `0.003379`, median `0.004187`, mae `0.022603`
- 20d: sample `20`, hit `0.75`, avg `0.012629`, median `0.022652`, mae `0.039527`
- 60d: sample `20`, hit `0.5`, avg `0.012548`, median `0.012092`, mae `0.060725`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000143`, median `0.000603`, mae `0.012974`
- 5d: sample `60`, hit `0.6333`, avg `0.001665`, median `0.003197`, mae `0.015264`
- 10d: sample `60`, hit `0.5`, avg `0.001259`, median `0.001517`, mae `0.025006`
- 20d: sample `60`, hit `0.6`, avg `0.003769`, median `0.01666`, mae `0.042679`
- 60d: sample `60`, hit `0.5333`, avg `0.011059`, median `0.030553`, mae `0.07163`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00974`, median `0.010849`, mae `0.015613`
- 5d: sample `20`, hit `0.6`, avg `0.005366`, median `0.003684`, mae `0.019131`
- 10d: sample `20`, hit `0.65`, avg `0.015145`, median `0.016536`, mae `0.034333`
- 20d: sample `20`, hit `0.65`, avg `0.029792`, median `0.028499`, mae `0.058492`
- 60d: sample `20`, hit `0.8`, avg `0.053087`, median `0.059829`, mae `0.070475`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002042`, median `0.001448`, mae `0.016983`
- 5d: sample `20`, hit `0.5`, avg `4.9e-05`, median `0.003005`, mae `0.017135`
- 10d: sample `20`, hit `0.6`, avg `0.003379`, median `0.004187`, mae `0.022603`
- 20d: sample `20`, hit `0.75`, avg `0.012629`, median `0.022652`, mae `0.039527`
- 60d: sample `20`, hit `0.5`, avg `0.012548`, median `0.012092`, mae `0.060725`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.00289`, median `0.000145`, mae `0.012938`
- 5d: sample `40`, hit `0.625`, avg `0.000653`, median `0.001695`, mae `0.01355`
- 10d: sample `40`, hit `0.45`, avg `-0.002454`, median `-0.003071`, mae `0.020674`
- 20d: sample `40`, hit `0.575`, avg `0.001691`, median `0.008658`, mae `0.033158`
- 60d: sample `40`, hit `0.45`, avg `0.003597`, median `-0.004982`, mae `0.054983`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00974`, median `0.010849`, mae `0.015613`
- 5d: sample `20`, hit `0.6`, avg `0.005366`, median `0.003684`, mae `0.019131`
- 10d: sample `20`, hit `0.65`, avg `0.015145`, median `0.016536`, mae `0.034333`
- 20d: sample `20`, hit `0.65`, avg `0.029792`, median `0.028499`, mae `0.058492`
- 60d: sample `20`, hit `0.8`, avg `0.053087`, median `0.059829`, mae `0.070475`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00974`, median `0.010849`, mae `0.015613`
- 5d: sample `20`, hit `0.6`, avg `0.005366`, median `0.003684`, mae `0.019131`
- 10d: sample `20`, hit `0.65`, avg `0.015145`, median `0.016536`, mae `0.034333`
- 20d: sample `20`, hit `0.65`, avg `0.029792`, median `0.028499`, mae `0.058492`
- 60d: sample `20`, hit `0.8`, avg `0.053087`, median `0.059829`, mae `0.070475`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002542`, median `0.002887`, mae `0.013634`
- 5d: sample `80`, hit `0.625`, avg `0.00259`, median `0.003197`, mae `0.016231`
- 10d: sample `80`, hit `0.5375`, avg `0.00473`, median `0.00903`, mae `0.027338`
- 20d: sample `80`, hit `0.6125`, avg `0.010275`, median `0.01666`, mae `0.046633`
- 60d: sample `80`, hit `0.6`, avg `0.021566`, median `0.030786`, mae `0.071341`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002542`, median `0.002887`, mae `0.013634`
- 5d: sample `80`, hit `0.625`, avg `0.00259`, median `0.003197`, mae `0.016231`
- 10d: sample `80`, hit `0.5375`, avg `0.00473`, median `0.00903`, mae `0.027338`
- 20d: sample `80`, hit `0.6125`, avg `0.010275`, median `0.01666`, mae `0.046633`
- 60d: sample `80`, hit `0.6`, avg `0.021566`, median `0.030786`, mae `0.071341`

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
