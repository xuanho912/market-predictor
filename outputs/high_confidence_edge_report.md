# High Confidence Edge Report

Generated at: `2026-08-20T21:58:16.610162+00:00`

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
- 3d: sample `40`, hit `0.675`, avg `0.004181`, median `0.006714`, mae `0.015692`
- 5d: sample `40`, hit `0.725`, avg `0.006924`, median `0.008088`, mae `0.018229`
- 10d: sample `40`, hit `0.6`, avg `0.005644`, median `0.010691`, mae `0.025757`
- 20d: sample `40`, hit `0.725`, avg `0.007995`, median `0.01666`, mae `0.039172`
- 60d: sample `40`, hit `0.625`, avg `0.017708`, median `0.046132`, mae `0.068583`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.002609`, median `0.002329`, mae `0.013437`
- 5d: sample `40`, hit `0.575`, avg `0.001385`, median `0.000873`, mae `0.017675`
- 10d: sample `40`, hit `0.425`, avg `0.001359`, median `-0.007491`, mae `0.029983`
- 20d: sample `40`, hit `0.475`, avg `0.006615`, median `-0.001203`, mae `0.047184`
- 60d: sample `40`, hit `0.55`, avg `0.028275`, median `0.02283`, mae `0.069795`

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
- 3d: sample `8`, hit `0.5`, avg `-0.001457`, median `0.001448`, mae `0.011449`
- 5d: sample `8`, hit `0.625`, avg `-3e-05`, median `0.004014`, mae `0.010879`
- 10d: sample `8`, hit `0.625`, avg `0.00654`, median `0.011426`, mae `0.017063`
- 20d: sample `8`, hit `0.75`, avg `0.016255`, median `0.020068`, mae `0.021934`
- 60d: sample `8`, hit `0.375`, avg `-0.002876`, median `-0.020268`, mae `0.039208`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001457`, median `0.001448`, mae `0.011449`
- 5d: sample `8`, hit `0.625`, avg `-3e-05`, median `0.004014`, mae `0.010879`
- 10d: sample `8`, hit `0.625`, avg `0.00654`, median `0.011426`, mae `0.017063`
- 20d: sample `8`, hit `0.75`, avg `0.016255`, median `0.020068`, mae `0.021934`
- 60d: sample `8`, hit `0.375`, avg `-0.002876`, median `-0.020268`, mae `0.039208`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.004181, 'median_return': 0.006714, 'mean_absolute_return': 0.015692, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.006924, 'median_return': 0.008088, 'mean_absolute_return': 0.018229, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.005644, 'median_return': 0.010691, 'mean_absolute_return': 0.025757, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.007995, 'median_return': 0.01666, 'mean_absolute_return': 0.039172, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.017708, 'median_return': 0.046132, 'mean_absolute_return': 0.068583, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001457, 'median_return': 0.001448, 'mean_absolute_return': 0.011449, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -3e-05, 'median_return': 0.004014, 'mean_absolute_return': 0.010879, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.00654, 'median_return': 0.011426, 'mean_absolute_return': 0.017063, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016255, 'median_return': 0.020068, 'mean_absolute_return': 0.021934, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.002876, 'median_return': -0.020268, 'mean_absolute_return': 0.039208, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.003934, 'median_return': 0.005642, 'mean_absolute_return': 0.01491, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.004619, 'median_return': 0.004473, 'mean_absolute_return': 0.018738, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.003164, 'median_return': 0.001517, 'mean_absolute_return': 0.029071, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.006311, 'median_return': 0.010656, 'mean_absolute_return': 0.045538, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.025866, 'median_return': 0.045044, 'mean_absolute_return': 0.07252, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.1, 'both_hit': 16, 'both_miss': 4}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.0, 'both_hit': 16, 'both_miss': 4}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.15, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.15, 'both_hit': 14, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.05, 'both_hit': 15, 'both_miss': 5}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.003395, 'median_return': 0.005581, 'mean_absolute_return': 0.014564, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.004154, 'median_return': 0.004014, 'mean_absolute_return': 0.017952, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.003502, 'median_return': 0.002739, 'mean_absolute_return': 0.02787, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.007305, 'median_return': 0.010656, 'mean_absolute_return': 0.043178, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.022992, 'median_return': 0.032982, 'mean_absolute_return': 0.069189, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.001239`, median `0.000766`, mae `0.012071`
- 5d: sample `40`, hit `0.65`, avg `0.001754`, median `0.003005`, mae `0.012875`
- 10d: sample `40`, hit `0.45`, avg `-0.001952`, median `-0.007117`, mae `0.021388`
- 20d: sample `40`, hit `0.525`, avg `-0.002182`, median `0.005803`, mae `0.035009`
- 60d: sample `40`, hit `0.4`, avg `-0.002188`, median `-0.020268`, mae `0.056783`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001986`, median `0.00558`, mae `0.017531`
- 5d: sample `40`, hit `0.575`, avg `0.002666`, median `0.003005`, mae `0.021772`
- 10d: sample `40`, hit `0.625`, avg `0.011034`, median `0.016085`, mae `0.031443`
- 20d: sample `40`, hit `0.7`, avg `0.023421`, median `0.020068`, mae `0.048888`
- 60d: sample `40`, hit `0.65`, avg `0.041263`, median `0.046132`, mae `0.073696`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001862`, median `0.00234`, mae `0.016166`
- 5d: sample `20`, hit `0.65`, avg `0.003035`, median `0.004014`, mae `0.016972`
- 10d: sample `20`, hit `0.65`, avg `0.007723`, median `0.011426`, mae `0.022849`
- 20d: sample `20`, hit `0.75`, avg `0.014624`, median `0.022652`, mae `0.036712`
- 60d: sample `20`, hit `0.5`, avg `0.0108`, median `0.012092`, mae `0.060684`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001862`, median `0.00234`, mae `0.016166`
- 5d: sample `20`, hit `0.65`, avg `0.003035`, median `0.004014`, mae `0.016972`
- 10d: sample `20`, hit `0.65`, avg `0.007723`, median `0.011426`, mae `0.022849`
- 20d: sample `20`, hit `0.75`, avg `0.014624`, median `0.022652`, mae `0.036712`
- 60d: sample `20`, hit `0.5`, avg `0.0108`, median `0.012092`, mae `0.060684`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001862`, median `0.00234`, mae `0.016166`
- 5d: sample `20`, hit `0.65`, avg `0.003035`, median `0.004014`, mae `0.016972`
- 10d: sample `20`, hit `0.65`, avg `0.007723`, median `0.011426`, mae `0.022849`
- 20d: sample `20`, hit `0.75`, avg `0.014624`, median `0.022652`, mae `0.036712`
- 60d: sample `20`, hit `0.5`, avg `0.0108`, median `0.012092`, mae `0.060684`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001986`, median `0.00558`, mae `0.017531`
- 5d: sample `40`, hit `0.575`, avg `0.002666`, median `0.003005`, mae `0.021772`
- 10d: sample `40`, hit `0.625`, avg `0.011034`, median `0.016085`, mae `0.031443`
- 20d: sample `40`, hit `0.7`, avg `0.023421`, median `0.020068`, mae `0.048888`
- 60d: sample `40`, hit `0.65`, avg `0.041263`, median `0.046132`, mae `0.073696`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001862`, median `0.00234`, mae `0.016166`
- 5d: sample `20`, hit `0.65`, avg `0.003035`, median `0.004014`, mae `0.016972`
- 10d: sample `20`, hit `0.65`, avg `0.007723`, median `0.011426`, mae `0.022849`
- 20d: sample `20`, hit `0.75`, avg `0.014624`, median `0.022652`, mae `0.036712`
- 60d: sample `20`, hit `0.5`, avg `0.0108`, median `0.012092`, mae `0.060684`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.010224`, median `0.013042`, mae `0.015218`
- 5d: sample `20`, hit `0.8`, avg `0.010812`, median `0.018025`, mae `0.019486`
- 10d: sample `20`, hit `0.55`, avg `0.003565`, median `0.006819`, mae `0.028665`
- 20d: sample `20`, hit `0.7`, avg `0.001366`, median `0.015275`, mae `0.041631`
- 60d: sample `20`, hit `0.75`, avg `0.024617`, median `0.055465`, mae `0.076482`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001862`, median `0.00234`, mae `0.016166`
- 5d: sample `20`, hit `0.65`, avg `0.003035`, median `0.004014`, mae `0.016972`
- 10d: sample `20`, hit `0.65`, avg `0.007723`, median `0.011426`, mae `0.022849`
- 20d: sample `20`, hit `0.75`, avg `0.014624`, median `0.022652`, mae `0.036712`
- 60d: sample `20`, hit `0.5`, avg `0.0108`, median `0.012092`, mae `0.060684`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.005833`, median `0.009966`, mae `0.018897`
- 5d: sample `20`, hit `0.5`, avg `0.002297`, median `0.000863`, mae `0.026572`
- 10d: sample `20`, hit `0.6`, avg `0.014345`, median `0.016536`, mae `0.040038`
- 20d: sample `20`, hit `0.65`, avg `0.032219`, median `0.015261`, mae `0.061063`
- 60d: sample `20`, hit `0.8`, avg `0.071726`, median `0.065495`, mae `0.086708`

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
- 3d: sample `80`, hit `0.65`, avg `0.003395`, median `0.005581`, mae `0.014564`
- 5d: sample `80`, hit `0.65`, avg `0.004154`, median `0.004014`, mae `0.017952`
- 10d: sample `80`, hit `0.5125`, avg `0.003502`, median `0.002739`, mae `0.02787`
- 20d: sample `80`, hit `0.6`, avg `0.007305`, median `0.010656`, mae `0.043178`
- 60d: sample `80`, hit `0.5875`, avg `0.022992`, median `0.032982`, mae `0.069189`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004181`, median `0.006714`, mae `0.015692`
- 5d: sample `40`, hit `0.725`, avg `0.006924`, median `0.008088`, mae `0.018229`
- 10d: sample `40`, hit `0.6`, avg `0.005644`, median `0.010691`, mae `0.025757`
- 20d: sample `40`, hit `0.725`, avg `0.007995`, median `0.01666`, mae `0.039172`
- 60d: sample `40`, hit `0.625`, avg `0.017708`, median `0.046132`, mae `0.068583`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.003395`, median `0.005581`, mae `0.014564`
- 5d: sample `80`, hit `0.65`, avg `0.004154`, median `0.004014`, mae `0.017952`
- 10d: sample `80`, hit `0.5125`, avg `0.003502`, median `0.002739`, mae `0.02787`
- 20d: sample `80`, hit `0.6`, avg `0.007305`, median `0.010656`, mae `0.043178`
- 60d: sample `80`, hit `0.5875`, avg `0.022992`, median `0.032982`, mae `0.069189`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004181`, median `0.006714`, mae `0.015692`
- 5d: sample `40`, hit `0.725`, avg `0.006924`, median `0.008088`, mae `0.018229`
- 10d: sample `40`, hit `0.6`, avg `0.005644`, median `0.010691`, mae `0.025757`
- 20d: sample `40`, hit `0.725`, avg `0.007995`, median `0.01666`, mae `0.039172`
- 60d: sample `40`, hit `0.625`, avg `0.017708`, median `0.046132`, mae `0.068583`

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
