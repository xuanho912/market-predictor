# High Confidence Edge Report

Generated at: `2026-08-07T05:25:08.443142+00:00`

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
- 3d: sample `80`, hit `0.6375`, avg `0.002543`, median `0.004569`, mae `0.01482`
- 5d: sample `80`, hit `0.7`, avg `0.0048`, median `0.006133`, mae `0.016883`
- 10d: sample `80`, hit `0.55`, avg `0.005329`, median `0.004462`, mae `0.024303`
- 20d: sample `80`, hit `0.675`, avg `0.012039`, median `0.015261`, mae `0.038092`
- 60d: sample `80`, hit `0.55`, avg `0.019304`, median `0.026715`, mae `0.071296`

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
- 3d: sample `8`, hit `0.5`, avg `-0.004255`, median `0.001448`, mae `0.014248`
- 5d: sample `8`, hit `0.625`, avg `-0.00032`, median `0.003005`, mae `0.009943`
- 10d: sample `8`, hit `0.375`, avg `-0.001054`, median `-0.007011`, mae `0.019127`
- 20d: sample `8`, hit `0.5`, avg `0.003945`, median `0.020068`, mae `0.029765`
- 60d: sample `8`, hit `0.375`, avg `-0.015481`, median `-0.03081`, mae `0.051813`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.002284`, median `-0.001166`, mae `0.010793`
- 5d: sample `8`, hit `0.75`, avg `0.003727`, median `0.007324`, mae `0.014475`
- 10d: sample `8`, hit `0.5`, avg `0.003494`, median `0.007467`, mae `0.011392`
- 20d: sample `8`, hit `0.625`, avg `0.003134`, median `0.012291`, mae `0.018338`
- 60d: sample `8`, hit `0.375`, avg `-0.015125`, median `-0.018455`, mae `0.048635`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.002543, 'median_return': 0.004569, 'mean_absolute_return': 0.01482, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.0048, 'median_return': 0.006133, 'mean_absolute_return': 0.016883, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.005329, 'median_return': 0.004462, 'mean_absolute_return': 0.024303, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.012039, 'median_return': 0.015261, 'mean_absolute_return': 0.038092, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.019304, 'median_return': 0.026715, 'mean_absolute_return': 0.071296, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.002284, 'median_return': -0.001166, 'mean_absolute_return': 0.010793, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.003727, 'median_return': 0.007324, 'mean_absolute_return': 0.014475, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003494, 'median_return': 0.007467, 'mean_absolute_return': 0.011392, 'max_adverse_excursion': -0.012383, 'max_favorable_excursion': 0.02016}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003134, 'median_return': 0.012291, 'mean_absolute_return': 0.018338, 'max_adverse_excursion': -0.024012, 'max_favorable_excursion': 0.025645}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.015125, 'median_return': -0.018455, 'mean_absolute_return': 0.048635, 'max_adverse_excursion': -0.08246, 'max_favorable_excursion': 0.082988}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.00308, 'median_return': 0.006565, 'mean_absolute_return': 0.015268, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.004919, 'median_return': 0.005763, 'mean_absolute_return': 0.01715, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.005533, 'median_return': 0.004462, 'mean_absolute_return': 0.025738, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.013029, 'median_return': 0.015661, 'mean_absolute_return': 0.040287, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.023129, 'median_return': 0.043741, 'mean_absolute_return': 0.073814, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.7}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.55}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.25, 'both_hit': 21, 'both_miss': 19}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.2, 'both_hit': 28, 'both_miss': 12}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 20, 'both_miss': 20}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.225, 'both_hit': 25, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.175, 'both_hit': 17, 'both_miss': 23}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.004132, 'median_return': 0.009349, 'mean_absolute_return': 0.016952, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.00505, 'median_return': 0.008088, 'mean_absolute_return': 0.019174, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.007128, 'median_return': 0.005616, 'mean_absolute_return': 0.027763, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.015498, 'median_return': 0.019547, 'mean_absolute_return': 0.044085, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.027932, 'median_return': 0.052998, 'mean_absolute_return': 0.07922, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.002223, 'median_return': 0.000145, 'mean_absolute_return': 0.008425, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.004052, 'median_return': 0.005084, 'mean_absolute_return': 0.010007, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -6.9e-05, 'median_return': -0.001676, 'mean_absolute_return': 0.013926, 'max_adverse_excursion': -0.028317, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001663, 'median_return': 0.007988, 'mean_absolute_return': 0.020113, 'max_adverse_excursion': -0.050277, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.006581, 'median_return': -0.012792, 'mean_absolute_return': 0.047526, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.096597}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002491`, median `0.000201`, mae `0.012566`
- 5d: sample `40`, hit `0.7`, avg `0.002874`, median `0.004606`, mae `0.012844`
- 10d: sample `40`, hit `0.5`, avg `0.002086`, median `0.001517`, mae `0.017658`
- 20d: sample `40`, hit `0.625`, avg `0.007193`, median `0.012291`, mae `0.029125`
- 60d: sample `40`, hit `0.425`, avg `0.002874`, median `-0.005534`, mae `0.055478`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.009738`, median `0.012584`, mae `0.020028`
- 5d: sample `20`, hit `0.7`, avg `0.006547`, median `0.010281`, mae `0.024787`
- 10d: sample `20`, hit `0.6`, avg `0.015025`, median `0.006604`, mae `0.033293`
- 20d: sample `20`, hit `0.75`, avg `0.035495`, median `0.029029`, mae `0.050172`
- 60d: sample `20`, hit `0.7`, avg `0.056092`, median `0.079128`, mae `0.086353`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002491`, median `0.000201`, mae `0.012566`
- 5d: sample `40`, hit `0.7`, avg `0.002874`, median `0.004606`, mae `0.012844`
- 10d: sample `40`, hit `0.5`, avg `0.002086`, median `0.001517`, mae `0.017658`
- 20d: sample `40`, hit `0.625`, avg `0.007193`, median `0.012291`, mae `0.029125`
- 60d: sample `40`, hit `0.425`, avg `0.002874`, median `-0.005534`, mae `0.055478`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.009738`, median `0.012584`, mae `0.020028`
- 5d: sample `20`, hit `0.7`, avg `0.006547`, median `0.010281`, mae `0.024787`
- 10d: sample `20`, hit `0.6`, avg `0.015025`, median `0.006604`, mae `0.033293`
- 20d: sample `20`, hit `0.75`, avg `0.035495`, median `0.029029`, mae `0.050172`
- 60d: sample `20`, hit `0.7`, avg `0.056092`, median `0.079128`, mae `0.086353`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002491`, median `0.000201`, mae `0.012566`
- 5d: sample `40`, hit `0.7`, avg `0.002874`, median `0.004606`, mae `0.012844`
- 10d: sample `40`, hit `0.5`, avg `0.002086`, median `0.001517`, mae `0.017658`
- 20d: sample `40`, hit `0.625`, avg `0.007193`, median `0.012291`, mae `0.029125`
- 60d: sample `40`, hit `0.425`, avg `0.002874`, median `-0.005534`, mae `0.055478`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.007578`, median `0.012132`, mae `0.017075`
- 5d: sample `40`, hit `0.7`, avg `0.006726`, median `0.010281`, mae `0.020921`
- 10d: sample `40`, hit `0.6`, avg `0.008572`, median `0.005616`, mae `0.030949`
- 20d: sample `40`, hit `0.725`, avg `0.016885`, median `0.015661`, mae `0.047059`
- 60d: sample `40`, hit `0.675`, avg `0.035734`, median `0.061844`, mae `0.087114`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002223`, median `0.000145`, mae `0.008425`
- 5d: sample `20`, hit `0.8`, avg `0.004052`, median `0.005084`, mae `0.010007`
- 10d: sample `20`, hit `0.45`, avg `-6.9e-05`, median `-0.001676`, mae `0.013926`
- 20d: sample `20`, hit `0.55`, avg `0.001663`, median `0.007988`, mae `0.020113`
- 60d: sample `20`, hit `0.35`, avg `-0.006581`, median `-0.012792`, mae `0.047526`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002543`, median `0.004569`, mae `0.01482`
- 5d: sample `80`, hit `0.7`, avg `0.0048`, median `0.006133`, mae `0.016883`
- 10d: sample `80`, hit `0.55`, avg `0.005329`, median `0.004462`, mae `0.024303`
- 20d: sample `80`, hit `0.675`, avg `0.012039`, median `0.015261`, mae `0.038092`
- 60d: sample `80`, hit `0.55`, avg `0.019304`, median `0.026715`, mae `0.071296`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002543`, median `0.004569`, mae `0.01482`
- 5d: sample `80`, hit `0.7`, avg `0.0048`, median `0.006133`, mae `0.016883`
- 10d: sample `80`, hit `0.55`, avg `0.005329`, median `0.004462`, mae `0.024303`
- 20d: sample `80`, hit `0.675`, avg `0.012039`, median `0.015261`, mae `0.038092`
- 60d: sample `80`, hit `0.55`, avg `0.019304`, median `0.026715`, mae `0.071296`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002543`, median `0.004569`, mae `0.01482`
- 5d: sample `80`, hit `0.7`, avg `0.0048`, median `0.006133`, mae `0.016883`
- 10d: sample `80`, hit `0.55`, avg `0.005329`, median `0.004462`, mae `0.024303`
- 20d: sample `80`, hit `0.675`, avg `0.012039`, median `0.015261`, mae `0.038092`
- 60d: sample `80`, hit `0.55`, avg `0.019304`, median `0.026715`, mae `0.071296`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002543`, median `0.004569`, mae `0.01482`
- 5d: sample `80`, hit `0.7`, avg `0.0048`, median `0.006133`, mae `0.016883`
- 10d: sample `80`, hit `0.55`, avg `0.005329`, median `0.004462`, mae `0.024303`
- 20d: sample `80`, hit `0.675`, avg `0.012039`, median `0.015261`, mae `0.038092`
- 60d: sample `80`, hit `0.55`, avg `0.019304`, median `0.026715`, mae `0.071296`

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
