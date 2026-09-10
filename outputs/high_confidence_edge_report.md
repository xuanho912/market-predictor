# High Confidence Edge Report

Generated at: `2026-09-10T16:27:27.477426+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `8`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `8`, gate `insufficient`
- 5d: completed `8`, gate `insufficient`
- 10d: completed `8`, gate `insufficient`
- 20d: completed `8`, gate `insufficient`
- 60d: completed `8`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002593`, median `0.00531`, mae `0.014362`
- 5d: sample `80`, hit `0.6375`, avg `0.001489`, median `0.003829`, mae `0.016672`
- 10d: sample `80`, hit `0.45`, avg `-0.000248`, median `-0.00367`, mae `0.025647`
- 20d: sample `80`, hit `0.6125`, avg `0.011049`, median `0.019977`, mae `0.038266`
- 60d: sample `80`, hit `0.6875`, avg `0.036506`, median `0.059495`, mae `0.082008`

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
- 3d: sample `8`, hit `0.625`, avg `-0.001516`, median `0.007289`, mae `0.018284`
- 5d: sample `8`, hit `0.625`, avg `-0.011121`, median `0.001087`, mae `0.015744`
- 10d: sample `8`, hit `0.125`, avg `-0.014794`, median `-0.01796`, mae `0.023768`
- 20d: sample `8`, hit `0.75`, avg `0.018164`, median `0.029166`, mae `0.033657`
- 60d: sample `8`, hit `0.625`, avg `0.035099`, median `0.059495`, mae `0.078831`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.001516`, median `0.007289`, mae `0.018284`
- 5d: sample `8`, hit `0.625`, avg `-0.011121`, median `0.001087`, mae `0.015744`
- 10d: sample `8`, hit `0.125`, avg `-0.014794`, median `-0.01796`, mae `0.023768`
- 20d: sample `8`, hit `0.75`, avg `0.018164`, median `0.029166`, mae `0.033657`
- 60d: sample `8`, hit `0.625`, avg `0.035099`, median `0.059495`, mae `0.078831`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001516, 'median_return': 0.007289, 'mean_absolute_return': 0.018284, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.011121, 'median_return': 0.001087, 'mean_absolute_return': 0.015744, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.014794, 'median_return': -0.01796, 'mean_absolute_return': 0.023768, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.018164, 'median_return': 0.029166, 'mean_absolute_return': 0.033657, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.035099, 'median_return': 0.059495, 'mean_absolute_return': 0.078831, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.00305, 'median_return': 0.00531, 'mean_absolute_return': 0.013926, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.002891, 'median_return': 0.006047, 'mean_absolute_return': 0.016775, 'max_adverse_excursion': -0.048238, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.001368, 'median_return': -0.0004, 'mean_absolute_return': 0.025856, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.010258, 'median_return': 0.019977, 'mean_absolute_return': 0.038778, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.036662, 'median_return': 0.059948, 'mean_absolute_return': 0.082361, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3875}, '5d': {'sample_size': 80, 'hit_rate': 0.3625}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.00851, 'median_return': 0.012091, 'mean_absolute_return': 0.017545, 'max_adverse_excursion': -0.025173, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.011254, 'median_return': 0.012316, 'mean_absolute_return': 0.021301, 'max_adverse_excursion': -0.026699, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.01655, 'median_return': 0.019731, 'mean_absolute_return': 0.029703, 'max_adverse_excursion': -0.044039, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.032921, 'median_return': 0.030862, 'mean_absolute_return': 0.035881, 'max_adverse_excursion': -0.019772, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.080293, 'median_return': 0.106076, 'mean_absolute_return': 0.094632, 'max_adverse_excursion': -0.108365, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.000621, 'median_return': 0.003785, 'mean_absolute_return': 0.013301, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.025832}, '5d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': -0.001765, 'median_return': 0.002453, 'mean_absolute_return': 0.015129, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.038591}, '10d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.005847, 'median_return': -0.007491, 'mean_absolute_return': 0.024295, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.049674}, '20d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.003758, 'median_return': 0.00745, 'mean_absolute_return': 0.039061, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.02191, 'median_return': 0.049411, 'mean_absolute_return': 0.0778, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.1448}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002593`, median `0.00531`, mae `0.014362`
- 5d: sample `80`, hit `0.6375`, avg `0.001489`, median `0.003829`, mae `0.016672`
- 10d: sample `80`, hit `0.45`, avg `-0.000248`, median `-0.00367`, mae `0.025647`
- 20d: sample `80`, hit `0.6125`, avg `0.011049`, median `0.019977`, mae `0.038266`
- 60d: sample `80`, hit `0.6875`, avg `0.036506`, median `0.059495`, mae `0.082008`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.00851`, median `0.012091`, mae `0.017545`
- 5d: sample `20`, hit `0.7`, avg `0.011254`, median `0.012316`, mae `0.021301`
- 10d: sample `20`, hit `0.7`, avg `0.01655`, median `0.019731`, mae `0.029703`
- 20d: sample `20`, hit `0.8`, avg `0.032921`, median `0.030862`, mae `0.035881`
- 60d: sample `20`, hit `0.9`, avg `0.080293`, median `0.106076`, mae `0.094632`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002593`, median `0.00531`, mae `0.014362`
- 5d: sample `80`, hit `0.6375`, avg `0.001489`, median `0.003829`, mae `0.016672`
- 10d: sample `80`, hit `0.45`, avg `-0.000248`, median `-0.00367`, mae `0.025647`
- 20d: sample `80`, hit `0.6125`, avg `0.011049`, median `0.019977`, mae `0.038266`
- 60d: sample `80`, hit `0.6875`, avg `0.036506`, median `0.059495`, mae `0.082008`

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
- 3d: sample `80`, hit `0.6125`, avg `0.002593`, median `0.00531`, mae `0.014362`
- 5d: sample `80`, hit `0.6375`, avg `0.001489`, median `0.003829`, mae `0.016672`
- 10d: sample `80`, hit `0.45`, avg `-0.000248`, median `-0.00367`, mae `0.025647`
- 20d: sample `80`, hit `0.6125`, avg `0.011049`, median `0.019977`, mae `0.038266`
- 60d: sample `80`, hit `0.6875`, avg `0.036506`, median `0.059495`, mae `0.082008`

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
