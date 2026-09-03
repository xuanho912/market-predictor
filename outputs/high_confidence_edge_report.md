# High Confidence Edge Report

Generated at: `2026-09-03T05:52:39.215576+00:00`

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
- 3d: sample `60`, hit `0.5833`, avg `0.002238`, median `0.000766`, mae `0.012884`
- 5d: sample `60`, hit `0.6`, avg `0.004194`, median `0.002786`, mae `0.016692`
- 10d: sample `60`, hit `0.4667`, avg `0.001626`, median `-0.007117`, mae `0.027686`
- 20d: sample `60`, hit `0.6667`, avg `0.007461`, median `0.020226`, mae `0.038626`
- 60d: sample `60`, hit `0.6667`, avg `0.02218`, median `0.049712`, mae `0.079054`

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
- 3d: sample `8`, hit `0.5`, avg `-0.007732`, median `0.001558`, mae `0.01401`
- 5d: sample `8`, hit `0.375`, avg `-0.012817`, median `-0.012956`, mae `0.018988`
- 10d: sample `8`, hit `0.5`, avg `0.001642`, median `0.0076`, mae `0.01927`
- 20d: sample `8`, hit `0.875`, avg `0.020806`, median `0.031196`, mae `0.034631`
- 60d: sample `8`, hit `0.875`, avg `0.064394`, median `0.092646`, mae `0.078612`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.007732`, median `0.001558`, mae `0.01401`
- 5d: sample `8`, hit `0.375`, avg `-0.012817`, median `-0.012956`, mae `0.018988`
- 10d: sample `8`, hit `0.5`, avg `0.001642`, median `0.0076`, mae `0.01927`
- 20d: sample `8`, hit `0.875`, avg `0.020806`, median `0.031196`, mae `0.034631`
- 60d: sample `8`, hit `0.875`, avg `0.064394`, median `0.092646`, mae `0.078612`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.006736, 'median_return': -0.001811, 'mean_absolute_return': 0.016361, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.012013, 'median_return': -0.012956, 'mean_absolute_return': 0.017997, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.002862, 'median_return': -0.006017, 'mean_absolute_return': 0.016882, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.016067, 'median_return': 0.029166, 'mean_absolute_return': 0.034104, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.041198, 'median_return': 0.059495, 'mean_absolute_return': 0.07585, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.007732, 'median_return': 0.001558, 'mean_absolute_return': 0.01401, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012817, 'median_return': -0.012956, 'mean_absolute_return': 0.018988, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001642, 'median_return': 0.0076, 'mean_absolute_return': 0.01927, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.020806, 'median_return': 0.031196, 'mean_absolute_return': 0.034631, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.064394, 'median_return': 0.092646, 'mean_absolute_return': 0.078612, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000853, 'median_return': 0.000707, 'mean_absolute_return': 0.013725, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001583, 'median_return': 0.001239, 'mean_absolute_return': 0.0168, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': 0.000378, 'median_return': -0.007117, 'mean_absolute_return': 0.02562, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.008368, 'median_return': 0.020068, 'mean_absolute_return': 0.037813, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.022773, 'median_return': 0.048484, 'mean_absolute_return': 0.078213, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.3375}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.00035, 'median_return': 0.00234, 'mean_absolute_return': 0.017909, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001507, 'median_return': 0.000208, 'mean_absolute_return': 0.019867, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.00609, 'median_return': -0.0004, 'mean_absolute_return': 0.023655, 'max_adverse_excursion': -0.033774, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.020629, 'median_return': 0.028804, 'mean_absolute_return': 0.032741, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.04618, 'median_return': 0.064104, 'mean_absolute_return': 0.076592, 'max_adverse_excursion': -0.118336, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.000361, 'median_return': 0.000616, 'mean_absolute_return': 0.009598, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.022026}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.001792, 'median_return': 0.001303, 'mean_absolute_return': 0.01417, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.005082, 'median_return': -0.01051, 'mean_absolute_return': 0.026314, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': -0.001405, 'median_return': 0.011528, 'mean_absolute_return': 0.042249, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.007689, 'median_return': 0.032982, 'mean_absolute_return': 0.079914, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.117141}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.5375`, avg `-6e-06`, median `0.000707`, mae `0.013753`
- 5d: sample `80`, hit `0.55`, avg `0.000143`, median `0.000873`, mae `0.017018`
- 10d: sample `80`, hit `0.425`, avg `0.000504`, median `-0.007011`, mae `0.024985`
- 20d: sample `80`, hit `0.6625`, avg `0.009612`, median `0.020226`, mae `0.037495`
- 60d: sample `80`, hit `0.675`, avg `0.026935`, median `0.049712`, mae `0.078253`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `-6e-06`, median `0.000707`, mae `0.013753`
- 5d: sample `80`, hit `0.55`, avg `0.000143`, median `0.000873`, mae `0.017018`
- 10d: sample `80`, hit `0.425`, avg `0.000504`, median `-0.007011`, mae `0.024985`
- 20d: sample `80`, hit `0.6625`, avg `0.009612`, median `0.020226`, mae `0.037495`
- 60d: sample `80`, hit `0.675`, avg `0.026935`, median `0.049712`, mae `0.078253`

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
- 3d: sample `80`, hit `0.5375`, avg `-6e-06`, median `0.000707`, mae `0.013753`
- 5d: sample `80`, hit `0.55`, avg `0.000143`, median `0.000873`, mae `0.017018`
- 10d: sample `80`, hit `0.425`, avg `0.000504`, median `-0.007011`, mae `0.024985`
- 20d: sample `80`, hit `0.6625`, avg `0.009612`, median `0.020226`, mae `0.037495`
- 60d: sample `80`, hit `0.675`, avg `0.026935`, median `0.049712`, mae `0.078253`

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
