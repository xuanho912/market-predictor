# High Confidence Edge Report

Generated at: `2026-09-02T16:38:15.624270+00:00`

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
- 3d: sample `20`, hit `0.4`, avg `-0.006736`, median `-0.001811`, mae `0.016361`
- 5d: sample `20`, hit `0.4`, avg `-0.012013`, median `-0.012956`, mae `0.017997`
- 10d: sample `20`, hit `0.3`, avg `-0.002862`, median `-0.006017`, mae `0.016882`
- 20d: sample `20`, hit `0.65`, avg `0.016067`, median `0.029166`, mae `0.034104`
- 60d: sample `20`, hit `0.7`, avg `0.041198`, median `0.059495`, mae `0.07585`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.001732`, median `0.000766`, mae `0.012832`
- 5d: sample `60`, hit `0.6`, avg `0.003517`, median `0.002786`, mae `0.017442`
- 10d: sample `60`, hit `0.4667`, avg `0.000741`, median `-0.007117`, mae `0.028432`
- 20d: sample `60`, hit `0.6333`, avg `0.004431`, median `0.01927`, mae `0.038991`
- 60d: sample `60`, hit `0.6667`, avg `0.019416`, median `0.049712`, mae `0.082406`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006969`, median `0.001558`, mae `0.013246`
- 5d: sample `8`, hit `0.375`, avg `-0.013984`, median `-0.013034`, mae `0.020155`
- 10d: sample `8`, hit `0.375`, avg `-0.001725`, median `-0.0004`, mae `0.017407`
- 20d: sample `8`, hit `0.875`, avg `0.026443`, median `0.033999`, mae `0.040269`
- 60d: sample `8`, hit `0.875`, avg `0.070816`, median `0.101282`, mae `0.085035`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006969`, median `0.001558`, mae `0.013246`
- 5d: sample `8`, hit `0.375`, avg `-0.013984`, median `-0.013034`, mae `0.020155`
- 10d: sample `8`, hit `0.375`, avg `-0.001725`, median `-0.0004`, mae `0.017407`
- 20d: sample `8`, hit `0.875`, avg `0.026443`, median `0.033999`, mae `0.040269`
- 60d: sample `8`, hit `0.875`, avg `0.070816`, median `0.101282`, mae `0.085035`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.006736, 'median_return': -0.001811, 'mean_absolute_return': 0.016361, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.012013, 'median_return': -0.012956, 'mean_absolute_return': 0.017997, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.002862, 'median_return': -0.006017, 'mean_absolute_return': 0.016882, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.016067, 'median_return': 0.029166, 'mean_absolute_return': 0.034104, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.041198, 'median_return': 0.059495, 'mean_absolute_return': 0.07585, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006969, 'median_return': 0.001558, 'mean_absolute_return': 0.013246, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.013984, 'median_return': -0.013034, 'mean_absolute_return': 0.020155, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.001725, 'median_return': -0.0004, 'mean_absolute_return': 0.017407, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.026443, 'median_return': 0.033999, 'mean_absolute_return': 0.040269, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.070816, 'median_return': 0.101282, 'mean_absolute_return': 0.085035, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000346, 'median_return': 0.000707, 'mean_absolute_return': 0.013766, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001148, 'median_return': 0.001239, 'mean_absolute_return': 0.017295, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': 1.4e-05, 'median_return': -0.007117, 'mean_absolute_return': 0.026448, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.005218, 'median_return': 0.01927, 'mean_absolute_return': 0.037491, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.019756, 'median_return': 0.048484, 'mean_absolute_return': 0.080292, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.3625}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.001053, 'median_return': -0.001428, 'mean_absolute_return': 0.014937, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.002692, 'median_return': 0.000415, 'mean_absolute_return': 0.017022, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': 0.001517, 'median_return': -0.006017, 'mean_absolute_return': 0.022386, 'max_adverse_excursion': -0.037654, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.012693, 'median_return': 0.020226, 'mean_absolute_return': 0.032077, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.038159, 'median_return': 0.057625, 'mean_absolute_return': 0.069001, 'max_adverse_excursion': -0.118336, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.00162, 'median_return': 0.003026, 'mean_absolute_return': 0.010046, 'max_adverse_excursion': -0.025004, 'max_favorable_excursion': 0.020414}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006615, 'median_return': 0.011391, 'mean_absolute_return': 0.019257, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.005189, 'median_return': -0.011522, 'mean_absolute_return': 0.035019, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.008718, 'median_return': 0.007748, 'mean_absolute_return': 0.054844, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.01503, 'median_return': 0.048484, 'mean_absolute_return': 0.116062, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.117141}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005298`, median `-0.001811`, mae `0.012677`
- 5d: sample `40`, hit `0.475`, avg `-0.008538`, median `-0.00244`, mae `0.014665`
- 10d: sample `40`, hit `0.3`, avg `-0.005246`, median `-0.008511`, mae `0.018364`
- 20d: sample `40`, hit `0.575`, avg `0.006443`, median `0.012958`, mae `0.032427`
- 60d: sample `40`, hit `0.625`, avg `0.031657`, median `0.046132`, mae `0.064835`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.000773`, median `0.00234`, mae `0.015288`
- 5d: sample `60`, hit `0.55`, avg `0.0012`, median `0.003005`, mae `0.019664`
- 10d: sample `60`, hit `0.4667`, avg `0.00233`, median `-0.001222`, mae `0.027443`
- 20d: sample `60`, hit `0.6833`, avg `0.010847`, median `0.025442`, mae `0.040109`
- 60d: sample `60`, hit `0.7167`, avg `0.025777`, median `0.059495`, mae `0.089749`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.006736`, median `-0.001811`, mae `0.016361`
- 5d: sample `20`, hit `0.4`, avg `-0.012013`, median `-0.012956`, mae `0.017997`
- 10d: sample `20`, hit `0.3`, avg `-0.002862`, median `-0.006017`, mae `0.016882`
- 20d: sample `20`, hit `0.65`, avg `0.016067`, median `0.029166`, mae `0.034104`
- 60d: sample `20`, hit `0.7`, avg `0.041198`, median `0.059495`, mae `0.07585`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.00035`, median `0.00234`, mae `0.017909`
- 5d: sample `40`, hit `0.5`, avg `-0.001507`, median `0.000208`, mae `0.019867`
- 10d: sample `40`, hit `0.475`, avg `0.00609`, median `-0.0004`, mae `0.023655`
- 20d: sample `40`, hit `0.725`, avg `0.020629`, median `0.028804`, mae `0.032741`
- 60d: sample `40`, hit `0.775`, avg `0.04618`, median `0.064104`, mae `0.076592`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.006736`, median `-0.001811`, mae `0.016361`
- 5d: sample `20`, hit `0.4`, avg `-0.012013`, median `-0.012956`, mae `0.017997`
- 10d: sample `20`, hit `0.3`, avg `-0.002862`, median `-0.006017`, mae `0.016882`
- 20d: sample `20`, hit `0.65`, avg `0.016067`, median `0.029166`, mae `0.034104`
- 60d: sample `20`, hit `0.7`, avg `0.041198`, median `0.059495`, mae `0.07585`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.000773`, median `0.00234`, mae `0.015288`
- 5d: sample `60`, hit `0.55`, avg `0.0012`, median `0.003005`, mae `0.019664`
- 10d: sample `60`, hit `0.4667`, avg `0.00233`, median `-0.001222`, mae `0.027443`
- 20d: sample `60`, hit `0.6833`, avg `0.010847`, median `0.025442`, mae `0.040109`
- 60d: sample `60`, hit `0.7167`, avg `0.025777`, median `0.059495`, mae `0.089749`

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
- 3d: sample `80`, hit `0.5375`, avg `-0.000385`, median `0.000707`, mae `0.013714`
- 5d: sample `80`, hit `0.55`, avg `-0.000366`, median `0.000873`, mae `0.017581`
- 10d: sample `80`, hit `0.425`, avg `-0.00016`, median `-0.007011`, mae `0.025544`
- 20d: sample `80`, hit `0.6375`, avg `0.00734`, median `0.020068`, mae `0.037769`
- 60d: sample `80`, hit `0.675`, avg `0.024862`, median `0.049712`, mae `0.080767`

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
