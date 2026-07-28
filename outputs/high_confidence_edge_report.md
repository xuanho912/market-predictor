# High Confidence Edge Report

Generated at: `2026-07-28T22:39:07.302797+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.004464`, median `0.000603`, mae `0.01284`
- 5d: sample `20`, hit `0.5`, avg `-0.003731`, median `0.000688`, mae `0.014634`
- 10d: sample `20`, hit `0.4`, avg `-0.006977`, median `-0.007491`, mae `0.017669`
- 20d: sample `20`, hit `0.5`, avg `0.000456`, median `0.003675`, mae `0.028791`
- 60d: sample `20`, hit `0.55`, avg `0.010504`, median `0.006294`, mae `0.040245`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.001178`, median `0.001199`, mae `0.021611`
- 5d: sample `60`, hit `0.55`, avg `-0.001349`, median `0.003476`, mae `0.027092`
- 10d: sample `60`, hit `0.5833`, avg `0.009669`, median `0.012396`, mae `0.033055`
- 20d: sample `60`, hit `0.7167`, avg `0.025147`, median `0.030922`, mae `0.053077`
- 60d: sample `60`, hit `0.75`, avg `0.050717`, median `0.072268`, mae `0.088591`

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
- 3d: sample `8`, hit `0.5`, avg `-0.011661`, median `0.000201`, mae `0.014348`
- 5d: sample `8`, hit `0.5`, avg `-0.013005`, median `0.000688`, mae `0.015306`
- 10d: sample `8`, hit `0.25`, avg `-0.01125`, median `-0.009882`, mae `0.015758`
- 20d: sample `8`, hit `0.5`, avg `0.003144`, median `0.003675`, mae `0.011901`
- 60d: sample `8`, hit `0.625`, avg `0.02412`, median `0.032982`, mae `0.034452`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.014227`, median `-0.010033`, mae `0.024406`
- 5d: sample `8`, hit `0.375`, avg `-0.017589`, median `-0.022295`, mae `0.027899`
- 10d: sample `8`, hit `0.125`, avg `-0.009168`, median `-0.007755`, mae `0.017312`
- 20d: sample `8`, hit `0.625`, avg `0.024604`, median `0.043456`, mae `0.044537`
- 60d: sample `8`, hit `0.75`, avg `0.061034`, median `0.099838`, mae `0.08247`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.004464, 'median_return': 0.000603, 'mean_absolute_return': 0.01284, 'max_adverse_excursion': -0.03466, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.003731, 'median_return': 0.000688, 'mean_absolute_return': 0.014634, 'max_adverse_excursion': -0.047389, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.006977, 'median_return': -0.007491, 'mean_absolute_return': 0.017669, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.000456, 'median_return': 0.003675, 'mean_absolute_return': 0.028791, 'max_adverse_excursion': -0.0919, 'max_favorable_excursion': 0.053054}, '60d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.010504, 'median_return': 0.006294, 'mean_absolute_return': 0.040245, 'max_adverse_excursion': -0.087508, 'max_favorable_excursion': 0.084597}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.014227, 'median_return': -0.010033, 'mean_absolute_return': 0.024406, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.017589, 'median_return': -0.022295, 'mean_absolute_return': 0.027899, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.009168, 'median_return': -0.007755, 'mean_absolute_return': 0.017312, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.024604, 'median_return': 0.043456, 'mean_absolute_return': 0.044537, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.061034, 'median_return': 0.099838, 'mean_absolute_return': 0.08247, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.000641, 'median_return': 0.001139, 'mean_absolute_return': 0.018864, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.057206}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.000207, 'median_return': 0.002721, 'mean_absolute_return': 0.023542, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.007138, 'median_return': 0.011031, 'mean_absolute_return': 0.030531, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.094092}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.018349, 'median_return': 0.020226, 'mean_absolute_return': 0.04728, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.0384, 'median_return': 0.057625, 'mean_absolute_return': 0.075842, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.3125}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.002, 'median_return': 0.000744, 'mean_absolute_return': 0.019419, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.057206}, '5d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': -0.001945, 'median_return': 0.002451, 'mean_absolute_return': 0.023978, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.005508, 'median_return': 0.001574, 'mean_absolute_return': 0.029209, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.094092}, '20d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.018974, 'median_return': 0.02086, 'mean_absolute_return': 0.047006, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.040664, 'median_return': 0.057625, 'mean_absolute_return': 0.076504, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21366}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.007012`, median `0.000201`, mae `0.016654`
- 5d: sample `40`, hit `0.45`, avg `-0.009495`, median `-0.001429`, mae `0.018835`
- 10d: sample `40`, hit `0.35`, avg `-0.005806`, median `-0.007117`, mae `0.016789`
- 20d: sample `40`, hit `0.6`, avg `0.008465`, median `0.01927`, mae `0.034206`
- 60d: sample `40`, hit `0.65`, avg `0.029508`, median `0.046132`, mae `0.058821`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.003013`, median `0.004667`, mae `0.022183`
- 5d: sample `40`, hit `0.625`, avg `0.005606`, median `0.006676`, mae `0.029121`
- 10d: sample `40`, hit `0.725`, avg `0.016821`, median `0.027869`, mae `0.041629`
- 20d: sample `40`, hit `0.725`, avg `0.029483`, median `0.045022`, mae `0.059806`
- 60d: sample `40`, hit `0.75`, avg `0.051819`, median `0.073403`, mae `0.094187`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.007012`, median `0.000201`, mae `0.016654`
- 5d: sample `40`, hit `0.45`, avg `-0.009495`, median `-0.001429`, mae `0.018835`
- 10d: sample `40`, hit `0.35`, avg `-0.005806`, median `-0.007117`, mae `0.016789`
- 20d: sample `40`, hit `0.6`, avg `0.008465`, median `0.01927`, mae `0.034206`
- 60d: sample `40`, hit `0.65`, avg `0.029508`, median `0.046132`, mae `0.058821`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.007012`, median `0.000201`, mae `0.016654`
- 5d: sample `40`, hit `0.45`, avg `-0.009495`, median `-0.001429`, mae `0.018835`
- 10d: sample `40`, hit `0.35`, avg `-0.005806`, median `-0.007117`, mae `0.016789`
- 20d: sample `40`, hit `0.6`, avg `0.008465`, median `0.01927`, mae `0.034206`
- 60d: sample `40`, hit `0.65`, avg `0.029508`, median `0.046132`, mae `0.058821`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.007012`, median `0.000201`, mae `0.016654`
- 5d: sample `40`, hit `0.45`, avg `-0.009495`, median `-0.001429`, mae `0.018835`
- 10d: sample `40`, hit `0.35`, avg `-0.005806`, median `-0.007117`, mae `0.016789`
- 20d: sample `40`, hit `0.6`, avg `0.008465`, median `0.01927`, mae `0.034206`
- 60d: sample `40`, hit `0.65`, avg `0.029508`, median `0.046132`, mae `0.058821`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.007012`, median `0.000201`, mae `0.016654`
- 5d: sample `40`, hit `0.45`, avg `-0.009495`, median `-0.001429`, mae `0.018835`
- 10d: sample `40`, hit `0.35`, avg `-0.005806`, median `-0.007117`, mae `0.016789`
- 20d: sample `40`, hit `0.6`, avg `0.008465`, median `0.01927`, mae `0.034206`
- 60d: sample `40`, hit `0.65`, avg `0.029508`, median `0.046132`, mae `0.058821`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.003013`, median `0.004667`, mae `0.022183`
- 5d: sample `40`, hit `0.625`, avg `0.005606`, median `0.006676`, mae `0.029121`
- 10d: sample `40`, hit `0.725`, avg `0.016821`, median `0.027869`, mae `0.041629`
- 20d: sample `40`, hit `0.725`, avg `0.029483`, median `0.045022`, mae `0.059806`
- 60d: sample `40`, hit `0.75`, avg `0.051819`, median `0.073403`, mae `0.094187`

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
- 3d: sample `80`, hit `0.525`, avg `-0.002`, median `0.000744`, mae `0.019419`
- 5d: sample `80`, hit `0.5375`, avg `-0.001945`, median `0.002451`, mae `0.023978`
- 10d: sample `80`, hit `0.5375`, avg `0.005508`, median `0.001574`, mae `0.029209`
- 20d: sample `80`, hit `0.6625`, avg `0.018974`, median `0.02086`, mae `0.047006`
- 60d: sample `80`, hit `0.7`, avg `0.040664`, median `0.057625`, mae `0.076504`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.007012`, median `0.000201`, mae `0.016654`
- 5d: sample `40`, hit `0.45`, avg `-0.009495`, median `-0.001429`, mae `0.018835`
- 10d: sample `40`, hit `0.35`, avg `-0.005806`, median `-0.007117`, mae `0.016789`
- 20d: sample `40`, hit `0.6`, avg `0.008465`, median `0.01927`, mae `0.034206`
- 60d: sample `40`, hit `0.65`, avg `0.029508`, median `0.046132`, mae `0.058821`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001027`, median `0.001139`, mae `0.018747`
- 5d: sample `40`, hit `0.625`, avg `0.005545`, median `0.003727`, mae `0.022068`
- 10d: sample `40`, hit `0.6`, avg `0.010053`, median `0.017201`, mae `0.031524`
- 20d: sample `40`, hit `0.65`, avg `0.0248`, median `0.02086`, mae `0.0469`
- 60d: sample `40`, hit `0.725`, avg `0.048312`, median `0.057625`, mae `0.074423`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.004464`, median `0.000603`, mae `0.01284`
- 5d: sample `20`, hit `0.5`, avg `-0.003731`, median `0.000688`, mae `0.014634`
- 10d: sample `20`, hit `0.4`, avg `-0.006977`, median `-0.007491`, mae `0.017669`
- 20d: sample `20`, hit `0.5`, avg `0.000456`, median `0.003675`, mae `0.028791`
- 60d: sample `20`, hit `0.55`, avg `0.010504`, median `0.006294`, mae `0.040245`

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
