# High Confidence Edge Report

Generated at: `2026-07-29T14:33:55.619699+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.000236`, median `0.001405`, mae `0.016403`
- 5d: sample `80`, hit `0.6125`, avg `0.001025`, median `0.002774`, mae `0.021069`
- 10d: sample `80`, hit `0.45`, avg `0.000325`, median `-0.005891`, mae `0.030334`
- 20d: sample `80`, hit `0.6375`, avg `0.021637`, median `0.022339`, mae `0.045381`
- 60d: sample `80`, hit `0.675`, avg `0.043363`, median `0.058473`, mae `0.077367`

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
- 3d: sample `8`, hit `0.625`, avg `0.005922`, median `0.016307`, mae `0.015436`
- 5d: sample `8`, hit `0.75`, avg `-0.001516`, median `0.002223`, mae `0.014223`
- 10d: sample `8`, hit `0.375`, avg `-0.000459`, median `-0.0004`, mae `0.020675`
- 20d: sample `8`, hit `0.75`, avg `0.035935`, median `0.055822`, mae `0.040452`
- 60d: sample `8`, hit `0.625`, avg `0.055966`, median `0.120808`, mae `0.093205`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.005922`, median `0.016307`, mae `0.015436`
- 5d: sample `8`, hit `0.75`, avg `-0.001516`, median `0.002223`, mae `0.014223`
- 10d: sample `8`, hit `0.375`, avg `-0.000459`, median `-0.0004`, mae `0.020675`
- 20d: sample `8`, hit `0.75`, avg `0.035935`, median `0.055822`, mae `0.040452`
- 60d: sample `8`, hit `0.625`, avg `0.055966`, median `0.120808`, mae `0.093205`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005922, 'median_return': 0.016307, 'mean_absolute_return': 0.015436, 'max_adverse_excursion': -0.026364, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': -0.001516, 'median_return': 0.002223, 'mean_absolute_return': 0.014223, 'max_adverse_excursion': -0.040664, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.000459, 'median_return': -0.0004, 'mean_absolute_return': 0.020675, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.035935, 'median_return': 0.055822, 'mean_absolute_return': 0.040452, 'max_adverse_excursion': -0.0114, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.055966, 'median_return': 0.120808, 'mean_absolute_return': 0.093205, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': -0.000395, 'median_return': 0.001139, 'mean_absolute_return': 0.016511, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.001307, 'median_return': 0.003554, 'mean_absolute_return': 0.021829, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': 0.000412, 'median_return': -0.007117, 'mean_absolute_return': 0.031408, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.020048, 'median_return': 0.02086, 'mean_absolute_return': 0.045929, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.041962, 'median_return': 0.057625, 'mean_absolute_return': 0.075607, 'max_adverse_excursion': -0.097363, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4125}, '5d': {'sample_size': 80, 'hit_rate': 0.3875}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.3625}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': -0.000228, 'median_return': 0.002067, 'mean_absolute_return': 0.015244, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': -0.000387, 'median_return': 0.002774, 'mean_absolute_return': 0.019039, 'max_adverse_excursion': -0.053563, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 8.6e-05, 'median_return': -0.001222, 'mean_absolute_return': 0.025066, 'max_adverse_excursion': -0.052866, 'max_favorable_excursion': 0.065408}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.018829, 'median_return': 0.02086, 'mean_absolute_return': 0.039549, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.038314, 'median_return': 0.059104, 'mean_absolute_return': 0.073505, 'max_adverse_excursion': -0.087508, 'max_favorable_excursion': 0.1448}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.00163, 'median_return': 0.001122, 'mean_absolute_return': 0.019882, 'max_adverse_excursion': -0.044533, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005261, 'median_return': 0.005662, 'mean_absolute_return': 0.027156, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.057302}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.001042, 'median_return': -0.010145, 'mean_absolute_return': 0.046141, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.03006, 'median_return': 0.063545, 'mean_absolute_return': 0.062878, 'max_adverse_excursion': -0.083854, 'max_favorable_excursion': 0.117383}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.058508, 'median_return': 0.058473, 'mean_absolute_return': 0.088954, 'max_adverse_excursion': -0.097363, 'max_favorable_excursion': 0.21366}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.003731`, median `0.001139`, mae `0.014972`
- 5d: sample `40`, hit `0.55`, avg `-0.006845`, median `0.001087`, mae `0.017317`
- 10d: sample `40`, hit `0.375`, avg `-0.005985`, median `-0.006017`, mae `0.020006`
- 20d: sample `40`, hit `0.55`, avg `0.007725`, median `0.00745`, mae `0.032676`
- 60d: sample `40`, hit `0.525`, avg `0.020723`, median `0.034496`, mae `0.062405`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.004204`, median `0.005633`, mae `0.017835`
- 5d: sample `40`, hit `0.675`, avg `0.008894`, median `0.012885`, mae `0.02482`
- 10d: sample `40`, hit `0.525`, avg `0.006634`, median `0.014312`, mae `0.040663`
- 20d: sample `40`, hit `0.725`, avg `0.035549`, median `0.06042`, mae `0.058086`
- 60d: sample `40`, hit `0.825`, avg `0.066002`, median `0.093098`, mae `0.092329`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.003731`, median `0.001139`, mae `0.014972`
- 5d: sample `40`, hit `0.55`, avg `-0.006845`, median `0.001087`, mae `0.017317`
- 10d: sample `40`, hit `0.375`, avg `-0.005985`, median `-0.006017`, mae `0.020006`
- 20d: sample `40`, hit `0.55`, avg `0.007725`, median `0.00745`, mae `0.032676`
- 60d: sample `40`, hit `0.525`, avg `0.020723`, median `0.034496`, mae `0.062405`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.006777`, median `0.010615`, mae `0.015787`
- 5d: sample `20`, hit `0.7`, avg `0.012527`, median `0.013131`, mae `0.022484`
- 10d: sample `20`, hit `0.6`, avg `0.012226`, median `0.023905`, mae `0.035186`
- 20d: sample `20`, hit `0.75`, avg `0.041037`, median `0.06042`, mae `0.053294`
- 60d: sample `20`, hit `0.85`, avg `0.073496`, median `0.103071`, mae `0.095705`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.003731`, median `0.001139`, mae `0.014972`
- 5d: sample `40`, hit `0.55`, avg `-0.006845`, median `0.001087`, mae `0.017317`
- 10d: sample `40`, hit `0.375`, avg `-0.005985`, median `-0.006017`, mae `0.020006`
- 20d: sample `40`, hit `0.55`, avg `0.007725`, median `0.00745`, mae `0.032676`
- 60d: sample `40`, hit `0.525`, avg `0.020723`, median `0.034496`, mae `0.062405`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.004204`, median `0.005633`, mae `0.017835`
- 5d: sample `40`, hit `0.675`, avg `0.008894`, median `0.012885`, mae `0.02482`
- 10d: sample `40`, hit `0.525`, avg `0.006634`, median `0.014312`, mae `0.040663`
- 20d: sample `40`, hit `0.725`, avg `0.035549`, median `0.06042`, mae `0.058086`
- 60d: sample `40`, hit `0.825`, avg `0.066002`, median `0.093098`, mae `0.092329`

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
- 3d: sample `80`, hit `0.5875`, avg `0.000236`, median `0.001405`, mae `0.016403`
- 5d: sample `80`, hit `0.6125`, avg `0.001025`, median `0.002774`, mae `0.021069`
- 10d: sample `80`, hit `0.45`, avg `0.000325`, median `-0.005891`, mae `0.030334`
- 20d: sample `80`, hit `0.6375`, avg `0.021637`, median `0.022339`, mae `0.045381`
- 60d: sample `80`, hit `0.675`, avg `0.043363`, median `0.058473`, mae `0.077367`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.000236`, median `0.001405`, mae `0.016403`
- 5d: sample `80`, hit `0.6125`, avg `0.001025`, median `0.002774`, mae `0.021069`
- 10d: sample `80`, hit `0.45`, avg `0.000325`, median `-0.005891`, mae `0.030334`
- 20d: sample `80`, hit `0.6375`, avg `0.021637`, median `0.022339`, mae `0.045381`
- 60d: sample `80`, hit `0.675`, avg `0.043363`, median `0.058473`, mae `0.077367`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.000236`, median `0.001405`, mae `0.016403`
- 5d: sample `80`, hit `0.6125`, avg `0.001025`, median `0.002774`, mae `0.021069`
- 10d: sample `80`, hit `0.45`, avg `0.000325`, median `-0.005891`, mae `0.030334`
- 20d: sample `80`, hit `0.6375`, avg `0.021637`, median `0.022339`, mae `0.045381`
- 60d: sample `80`, hit `0.675`, avg `0.043363`, median `0.058473`, mae `0.077367`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
