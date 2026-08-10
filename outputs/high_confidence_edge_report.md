# High Confidence Edge Report

Generated at: `2026-08-10T13:48:17.521889+00:00`

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
- 3d: sample `80`, hit `0.6125`, avg `0.002422`, median `0.004542`, mae `0.014469`
- 5d: sample `80`, hit `0.6625`, avg `0.004202`, median `0.005319`, mae `0.018428`
- 10d: sample `80`, hit `0.5375`, avg `0.003927`, median `0.005616`, mae `0.025744`
- 20d: sample `80`, hit `0.65`, avg `0.005182`, median `0.014007`, mae `0.04172`
- 60d: sample `80`, hit `0.5375`, avg `0.018203`, median `0.020144`, mae `0.065524`

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
- 3d: sample `8`, hit `0.625`, avg `0.000217`, median `0.006714`, mae `0.01232`
- 5d: sample `8`, hit `0.75`, avg `0.003846`, median `0.005319`, mae `0.013`
- 10d: sample `8`, hit `0.625`, avg `0.009059`, median `0.021953`, mae `0.019583`
- 20d: sample `8`, hit `0.75`, avg `0.018489`, median `0.022652`, mae `0.024168`
- 60d: sample `8`, hit `0.375`, avg `-0.002859`, median `-0.02013`, mae `0.039191`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.002267`, median `0.004004`, mae `0.00728`
- 5d: sample `8`, hit `0.875`, avg `0.00781`, median `0.010385`, mae `0.012391`
- 10d: sample `8`, hit `0.75`, avg `0.009169`, median `0.013144`, mae `0.014044`
- 20d: sample `8`, hit `0.625`, avg `0.001038`, median `0.007988`, mae `0.016242`
- 60d: sample `8`, hit `0.25`, avg `-0.013073`, median `-0.018455`, mae `0.042065`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.002422, 'median_return': 0.004542, 'mean_absolute_return': 0.014469, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.004202, 'median_return': 0.005319, 'mean_absolute_return': 0.018428, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.003927, 'median_return': 0.005616, 'mean_absolute_return': 0.025744, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.005182, 'median_return': 0.014007, 'mean_absolute_return': 0.04172, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.018203, 'median_return': 0.020144, 'mean_absolute_return': 0.065524, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002267, 'median_return': 0.004004, 'mean_absolute_return': 0.00728, 'max_adverse_excursion': -0.009803, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.00781, 'median_return': 0.010385, 'mean_absolute_return': 0.012391, 'max_adverse_excursion': -0.018322, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009169, 'median_return': 0.013144, 'mean_absolute_return': 0.014044, 'max_adverse_excursion': -0.012383, 'max_favorable_excursion': 0.020167}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001038, 'median_return': 0.007988, 'mean_absolute_return': 0.016242, 'max_adverse_excursion': -0.024012, 'max_favorable_excursion': 0.025541}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.013073, 'median_return': -0.018455, 'mean_absolute_return': 0.042065, 'max_adverse_excursion': -0.07448, 'max_favorable_excursion': 0.082988}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.002439, 'median_return': 0.005642, 'mean_absolute_return': 0.015268, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.003801, 'median_return': 0.004606, 'mean_absolute_return': 0.019099, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.003345, 'median_return': 0.001517, 'mean_absolute_return': 0.027044, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.005643, 'median_return': 0.015275, 'mean_absolute_return': 0.044551, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.021678, 'median_return': 0.02283, 'mean_absolute_return': 0.068131, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.4375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.05, 'both_hit': 21, 'both_miss': 19}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.05, 'both_hit': 27, 'both_miss': 13}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.025, 'both_hit': 22, 'both_miss': 18}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.0, 'both_hit': 26, 'both_miss': 14}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.05, 'both_hit': 17, 'both_miss': 23}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.004067, 'median_return': 0.009229, 'mean_absolute_return': 0.016513, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.004782, 'median_return': 0.005327, 'mean_absolute_return': 0.020581, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.005051, 'median_return': 0.005616, 'mean_absolute_return': 0.028665, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.008069, 'median_return': 0.015275, 'mean_absolute_return': 0.046125, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.027366, 'median_return': 0.045044, 'mean_absolute_return': 0.069636, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.002515, 'median_return': 0.000145, 'mean_absolute_return': 0.008339, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.002463, 'median_return': 0.005084, 'mean_absolute_return': 0.011971, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.025304}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.000558, 'median_return': 0.007467, 'mean_absolute_return': 0.016979, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.003476, 'median_return': 0.012291, 'mean_absolute_return': 0.028504, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.009285, 'median_return': -0.018455, 'mean_absolute_return': 0.05319, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.096597}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002085`, median `0.000201`, mae `0.012961`
- 5d: sample `40`, hit `0.675`, avg `0.003035`, median `0.004606`, mae `0.014723`
- 10d: sample `40`, hit `0.55`, avg `0.003946`, median `0.010691`, mae `0.019616`
- 20d: sample `40`, hit `0.65`, avg `0.006119`, median `0.020068`, mae `0.034816`
- 60d: sample `40`, hit `0.425`, avg `0.004189`, median `-0.01711`, mae `0.055676`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007758`, median `0.010849`, mae `0.019263`
- 5d: sample `20`, hit `0.6`, avg `0.004451`, median `0.010281`, mae `0.025849`
- 10d: sample `20`, hit `0.55`, avg `0.009234`, median `0.011168`, mae `0.038583`
- 20d: sample `20`, hit `0.65`, avg `0.01616`, median `0.015261`, mae `0.058776`
- 60d: sample `20`, hit `0.6`, avg `0.042095`, median `0.02283`, mae `0.084177`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002085`, median `0.000201`, mae `0.012961`
- 5d: sample `40`, hit `0.675`, avg `0.003035`, median `0.004606`, mae `0.014723`
- 10d: sample `40`, hit `0.55`, avg `0.003946`, median `0.010691`, mae `0.019616`
- 20d: sample `40`, hit `0.65`, avg `0.006119`, median `0.020068`, mae `0.034816`
- 60d: sample `40`, hit `0.425`, avg `0.004189`, median `-0.01711`, mae `0.055676`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007758`, median `0.010849`, mae `0.019263`
- 5d: sample `20`, hit `0.6`, avg `0.004451`, median `0.010281`, mae `0.025849`
- 10d: sample `20`, hit `0.55`, avg `0.009234`, median `0.011168`, mae `0.038583`
- 20d: sample `20`, hit `0.65`, avg `0.01616`, median `0.015261`, mae `0.058776`
- 60d: sample `20`, hit `0.6`, avg `0.042095`, median `0.02283`, mae `0.084177`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001655`, median `0.003785`, mae `0.017584`
- 5d: sample `20`, hit `0.6`, avg `0.003606`, median `0.004014`, mae `0.017476`
- 10d: sample `20`, hit `0.6`, avg `0.007335`, median `0.011426`, mae `0.022252`
- 20d: sample `20`, hit `0.7`, avg `0.015715`, median `0.024743`, mae `0.041127`
- 60d: sample `20`, hit `0.5`, avg `0.017662`, median `0.012092`, mae `0.058161`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002085`, median `0.000201`, mae `0.012961`
- 5d: sample `40`, hit `0.675`, avg `0.003035`, median `0.004606`, mae `0.014723`
- 10d: sample `40`, hit `0.55`, avg `0.003946`, median `0.010691`, mae `0.019616`
- 20d: sample `40`, hit `0.65`, avg `0.006119`, median `0.020068`, mae `0.034816`
- 60d: sample `40`, hit `0.425`, avg `0.004189`, median `-0.01711`, mae `0.055676`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007758`, median `0.010849`, mae `0.019263`
- 5d: sample `20`, hit `0.6`, avg `0.004451`, median `0.010281`, mae `0.025849`
- 10d: sample `20`, hit `0.55`, avg `0.009234`, median `0.011168`, mae `0.038583`
- 20d: sample `20`, hit `0.65`, avg `0.01616`, median `0.015261`, mae `0.058776`
- 60d: sample `20`, hit `0.6`, avg `0.042095`, median `0.02283`, mae `0.084177`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001655`, median `0.003785`, mae `0.017584`
- 5d: sample `20`, hit `0.6`, avg `0.003606`, median `0.004014`, mae `0.017476`
- 10d: sample `20`, hit `0.6`, avg `0.007335`, median `0.011426`, mae `0.022252`
- 20d: sample `20`, hit `0.7`, avg `0.015715`, median `0.024743`, mae `0.041127`
- 60d: sample `20`, hit `0.5`, avg `0.017662`, median `0.012092`, mae `0.058161`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002515`, median `0.000145`, mae `0.008339`
- 5d: sample `20`, hit `0.75`, avg `0.002463`, median `0.005084`, mae `0.011971`
- 10d: sample `20`, hit `0.5`, avg `0.000558`, median `0.007467`, mae `0.016979`
- 20d: sample `20`, hit `0.6`, avg `-0.003476`, median `0.012291`, mae `0.028504`
- 60d: sample `20`, hit `0.35`, avg `-0.009285`, median `-0.018455`, mae `0.05319`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002422`, median `0.004542`, mae `0.014469`
- 5d: sample `80`, hit `0.6625`, avg `0.004202`, median `0.005319`, mae `0.018428`
- 10d: sample `80`, hit `0.5375`, avg `0.003927`, median `0.005616`, mae `0.025744`
- 20d: sample `80`, hit `0.65`, avg `0.005182`, median `0.014007`, mae `0.04172`
- 60d: sample `80`, hit `0.5375`, avg `0.018203`, median `0.020144`, mae `0.065524`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.001196`, median `0.004004`, mae `0.015062`
- 5d: sample `60`, hit `0.65`, avg `0.003507`, median `0.004606`, mae `0.018432`
- 10d: sample `60`, hit `0.55`, avg `0.005709`, median `0.010691`, mae `0.025938`
- 20d: sample `60`, hit `0.65`, avg `0.009466`, median `0.015261`, mae `0.042803`
- 60d: sample `60`, hit `0.4833`, avg `0.016824`, median `-0.003049`, mae `0.065176`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002422`, median `0.004542`, mae `0.014469`
- 5d: sample `80`, hit `0.6625`, avg `0.004202`, median `0.005319`, mae `0.018428`
- 10d: sample `80`, hit `0.5375`, avg `0.003927`, median `0.005616`, mae `0.025744`
- 20d: sample `80`, hit `0.65`, avg `0.005182`, median `0.014007`, mae `0.04172`
- 60d: sample `80`, hit `0.5375`, avg `0.018203`, median `0.020144`, mae `0.065524`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.001196`, median `0.004004`, mae `0.015062`
- 5d: sample `60`, hit `0.65`, avg `0.003507`, median `0.004606`, mae `0.018432`
- 10d: sample `60`, hit `0.55`, avg `0.005709`, median `0.010691`, mae `0.025938`
- 20d: sample `60`, hit `0.65`, avg `0.009466`, median `0.015261`, mae `0.042803`
- 60d: sample `60`, hit `0.4833`, avg `0.016824`, median `-0.003049`, mae `0.065176`

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
