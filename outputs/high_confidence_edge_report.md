# High Confidence Edge Report

Generated at: `2026-06-16T15:33:50.035723+00:00`

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
- 3d: sample `80`, hit `0.625`, avg `0.00492`, median `0.006228`, mae `0.014049`
- 5d: sample `80`, hit `0.6375`, avg `0.007156`, median `0.006452`, mae `0.018671`
- 10d: sample `80`, hit `0.6125`, avg `0.007918`, median `0.009675`, mae `0.023561`
- 20d: sample `80`, hit `0.7125`, avg `0.010482`, median `0.018868`, mae `0.036185`
- 60d: sample `80`, hit `0.625`, avg `0.027871`, median `0.032982`, mae `0.062084`

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
- 3d: sample `8`, hit `0.375`, avg `-0.007791`, median `-0.001811`, mae `0.013454`
- 5d: sample `8`, hit `0.125`, avg `-0.011833`, median `-0.012956`, mae `0.017829`
- 10d: sample `8`, hit `0.75`, avg `0.008706`, median `0.0076`, mae `0.014887`
- 20d: sample `8`, hit `1.0`, avg `0.028852`, median `0.031196`, mae `0.028852`
- 60d: sample `8`, hit `0.875`, avg `0.054535`, median `0.065295`, mae `0.059567`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.007791`, median `-0.001811`, mae `0.013454`
- 5d: sample `8`, hit `0.125`, avg `-0.011833`, median `-0.012956`, mae `0.017829`
- 10d: sample `8`, hit `0.75`, avg `0.008706`, median `0.0076`, mae `0.014887`
- 20d: sample `8`, hit `1.0`, avg `0.028852`, median `0.031196`, mae `0.028852`
- 60d: sample `8`, hit `0.875`, avg `0.054535`, median `0.065295`, mae `0.059567`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.00492, 'median_return': 0.006228, 'mean_absolute_return': 0.014049, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.007156, 'median_return': 0.006452, 'mean_absolute_return': 0.018671, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.007918, 'median_return': 0.009675, 'mean_absolute_return': 0.023561, 'max_adverse_excursion': -0.061818, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.010482, 'median_return': 0.018868, 'mean_absolute_return': 0.036185, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.027871, 'median_return': 0.032982, 'mean_absolute_return': 0.062084, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007791, 'median_return': -0.001811, 'mean_absolute_return': 0.013454, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011833, 'median_return': -0.012956, 'mean_absolute_return': 0.017829, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008706, 'median_return': 0.0076, 'mean_absolute_return': 0.014887, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.028852, 'median_return': 0.031196, 'mean_absolute_return': 0.028852, 'max_adverse_excursion': 0.012958, 'max_favorable_excursion': 0.037283}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.054535, 'median_return': 0.065295, 'mean_absolute_return': 0.059567, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.006332, 'median_return': 0.006718, 'mean_absolute_return': 0.014115, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.009265, 'median_return': 0.008121, 'mean_absolute_return': 0.018764, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.007831, 'median_return': 0.01246, 'mean_absolute_return': 0.024524, 'max_adverse_excursion': -0.061818, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.008441, 'median_return': 0.01666, 'mean_absolute_return': 0.036999, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.024909, 'median_return': 0.029917, 'mean_absolute_return': 0.062364, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.7125}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': 0.0, 'both_hit': 57, 'both_miss': 23}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.00492, 'median_return': 0.006228, 'mean_absolute_return': 0.014049, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.007156, 'median_return': 0.006452, 'mean_absolute_return': 0.018671, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.007918, 'median_return': 0.009675, 'mean_absolute_return': 0.023561, 'max_adverse_excursion': -0.061818, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.010482, 'median_return': 0.018868, 'mean_absolute_return': 0.036185, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.027871, 'median_return': 0.032982, 'mean_absolute_return': 0.062084, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.00492`, median `0.006228`, mae `0.014049`
- 5d: sample `80`, hit `0.6375`, avg `0.007156`, median `0.006452`, mae `0.018671`
- 10d: sample `80`, hit `0.6125`, avg `0.007918`, median `0.009675`, mae `0.023561`
- 20d: sample `80`, hit `0.7125`, avg `0.010482`, median `0.018868`, mae `0.036185`
- 60d: sample `80`, hit `0.625`, avg `0.027871`, median `0.032982`, mae `0.062084`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.00492`, median `0.006228`, mae `0.014049`
- 5d: sample `80`, hit `0.6375`, avg `0.007156`, median `0.006452`, mae `0.018671`
- 10d: sample `80`, hit `0.6125`, avg `0.007918`, median `0.009675`, mae `0.023561`
- 20d: sample `80`, hit `0.7125`, avg `0.010482`, median `0.018868`, mae `0.036185`
- 60d: sample `80`, hit `0.625`, avg `0.027871`, median `0.032982`, mae `0.062084`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002283`, median `0.003952`, mae `0.013981`
- 5d: sample `40`, hit `0.5`, avg `0.003295`, median `0.000415`, mae `0.018586`
- 10d: sample `40`, hit `0.6`, avg `0.010617`, median `0.012903`, mae `0.022553`
- 20d: sample `40`, hit `0.775`, avg `0.020475`, median `0.02284`, mae `0.034999`
- 60d: sample `40`, hit `0.75`, avg `0.048471`, median `0.065295`, mae `0.071905`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.00492`, median `0.006228`, mae `0.014049`
- 5d: sample `80`, hit `0.6375`, avg `0.007156`, median `0.006452`, mae `0.018671`
- 10d: sample `80`, hit `0.6125`, avg `0.007918`, median `0.009675`, mae `0.023561`
- 20d: sample `80`, hit `0.7125`, avg `0.010482`, median `0.018868`, mae `0.036185`
- 60d: sample `80`, hit `0.625`, avg `0.027871`, median `0.032982`, mae `0.062084`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002283`, median `0.003952`, mae `0.013981`
- 5d: sample `40`, hit `0.5`, avg `0.003295`, median `0.000415`, mae `0.018586`
- 10d: sample `40`, hit `0.6`, avg `0.010617`, median `0.012903`, mae `0.022553`
- 20d: sample `40`, hit `0.775`, avg `0.020475`, median `0.02284`, mae `0.034999`
- 60d: sample `40`, hit `0.75`, avg `0.048471`, median `0.065295`, mae `0.071905`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000553`, median `0.001558`, mae `0.013493`
- 5d: sample `40`, hit `0.525`, avg `-0.000152`, median `0.002694`, mae `0.016118`
- 10d: sample `40`, hit `0.575`, avg `0.006246`, median `0.007467`, mae `0.016329`
- 20d: sample `40`, hit `0.8`, avg `0.016528`, median `0.022652`, mae `0.028167`
- 60d: sample `40`, hit `0.575`, avg `0.016301`, median `0.029917`, mae `0.058065`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.009287`, median `0.009928`, mae `0.014605`
- 5d: sample `40`, hit `0.75`, avg `0.014463`, median `0.014114`, mae `0.021224`
- 10d: sample `40`, hit `0.65`, avg `0.009591`, median `0.016142`, mae `0.030792`
- 20d: sample `40`, hit `0.625`, avg `0.004437`, median `0.01666`, mae `0.044202`
- 60d: sample `40`, hit `0.675`, avg `0.039441`, median `0.054765`, mae `0.066103`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000553`, median `0.001558`, mae `0.013493`
- 5d: sample `40`, hit `0.525`, avg `-0.000152`, median `0.002694`, mae `0.016118`
- 10d: sample `40`, hit `0.575`, avg `0.006246`, median `0.007467`, mae `0.016329`
- 20d: sample `40`, hit `0.8`, avg `0.016528`, median `0.022652`, mae `0.028167`
- 60d: sample `40`, hit `0.575`, avg `0.016301`, median `0.029917`, mae `0.058065`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.00492`, median `0.006228`, mae `0.014049`
- 5d: sample `80`, hit `0.6375`, avg `0.007156`, median `0.006452`, mae `0.018671`
- 10d: sample `80`, hit `0.6125`, avg `0.007918`, median `0.009675`, mae `0.023561`
- 20d: sample `80`, hit `0.7125`, avg `0.010482`, median `0.018868`, mae `0.036185`
- 60d: sample `80`, hit `0.625`, avg `0.027871`, median `0.032982`, mae `0.062084`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.00492`, median `0.006228`, mae `0.014049`
- 5d: sample `80`, hit `0.6375`, avg `0.007156`, median `0.006452`, mae `0.018671`
- 10d: sample `80`, hit `0.6125`, avg `0.007918`, median `0.009675`, mae `0.023561`
- 20d: sample `80`, hit `0.7125`, avg `0.010482`, median `0.018868`, mae `0.036185`
- 60d: sample `80`, hit `0.625`, avg `0.027871`, median `0.032982`, mae `0.062084`

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
