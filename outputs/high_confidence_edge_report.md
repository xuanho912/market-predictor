# High Confidence Edge Report

Generated at: `2026-06-15T14:41:14.540767+00:00`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004916`, median `0.006228`, mae `0.014116`
- 5d: sample `80`, hit `0.6375`, avg `0.005673`, median `0.005876`, mae `0.018468`
- 10d: sample `80`, hit `0.5875`, avg `0.007044`, median `0.007467`, mae `0.023308`
- 20d: sample `80`, hit `0.6875`, avg `0.009445`, median `0.017608`, mae `0.036921`
- 60d: sample `80`, hit `0.5875`, avg `0.028139`, median `0.034688`, mae `0.063347`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004916, 'median_return': 0.006228, 'mean_absolute_return': 0.014116, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.005673, 'median_return': 0.005876, 'mean_absolute_return': 0.018468, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.007044, 'median_return': 0.007467, 'mean_absolute_return': 0.023308, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.009445, 'median_return': 0.017608, 'mean_absolute_return': 0.036921, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.028139, 'median_return': 0.034688, 'mean_absolute_return': 0.063347, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007791, 'median_return': -0.001811, 'mean_absolute_return': 0.013454, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011833, 'median_return': -0.012956, 'mean_absolute_return': 0.017829, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008706, 'median_return': 0.0076, 'mean_absolute_return': 0.014887, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.028852, 'median_return': 0.031196, 'mean_absolute_return': 0.028852, 'max_adverse_excursion': 0.012958, 'max_favorable_excursion': 0.037283}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.054535, 'median_return': 0.065295, 'mean_absolute_return': 0.059567, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.006328, 'median_return': 0.006722, 'mean_absolute_return': 0.01419, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.007618, 'median_return': 0.007324, 'mean_absolute_return': 0.018539, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.006859, 'median_return': 0.007467, 'mean_absolute_return': 0.024243, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007288, 'median_return': 0.016109, 'mean_absolute_return': 0.037818, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.025206, 'median_return': 0.032982, 'mean_absolute_return': 0.063767, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': 0.0, 'both_hit': 55, 'both_miss': 25}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004916, 'median_return': 0.006228, 'mean_absolute_return': 0.014116, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.005673, 'median_return': 0.005876, 'mean_absolute_return': 0.018468, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.007044, 'median_return': 0.007467, 'mean_absolute_return': 0.023308, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.009445, 'median_return': 0.017608, 'mean_absolute_return': 0.036921, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.028139, 'median_return': 0.034688, 'mean_absolute_return': 0.063347, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004916`, median `0.006228`, mae `0.014116`
- 5d: sample `80`, hit `0.6375`, avg `0.005673`, median `0.005876`, mae `0.018468`
- 10d: sample `80`, hit `0.5875`, avg `0.007044`, median `0.007467`, mae `0.023308`
- 20d: sample `80`, hit `0.6875`, avg `0.009445`, median `0.017608`, mae `0.036921`
- 60d: sample `80`, hit `0.5875`, avg `0.028139`, median `0.034688`, mae `0.063347`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004916`, median `0.006228`, mae `0.014116`
- 5d: sample `80`, hit `0.6375`, avg `0.005673`, median `0.005876`, mae `0.018468`
- 10d: sample `80`, hit `0.5875`, avg `0.007044`, median `0.007467`, mae `0.023308`
- 20d: sample `80`, hit `0.6875`, avg `0.009445`, median `0.017608`, mae `0.036921`
- 60d: sample `80`, hit `0.5875`, avg `0.028139`, median `0.034688`, mae `0.063347`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003147`, median `0.006228`, mae `0.014045`
- 5d: sample `40`, hit `0.525`, avg `0.00309`, median `0.002616`, mae `0.018177`
- 10d: sample `40`, hit `0.55`, avg `0.008949`, median `0.0076`, mae `0.022926`
- 20d: sample `40`, hit `0.7`, avg `0.01638`, median `0.020431`, mae `0.034893`
- 60d: sample `40`, hit `0.725`, avg `0.04549`, median `0.052998`, mae `0.070191`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004916`, median `0.006228`, mae `0.014116`
- 5d: sample `80`, hit `0.6375`, avg `0.005673`, median `0.005876`, mae `0.018468`
- 10d: sample `80`, hit `0.5875`, avg `0.007044`, median `0.007467`, mae `0.023308`
- 20d: sample `80`, hit `0.6875`, avg `0.009445`, median `0.017608`, mae `0.036921`
- 60d: sample `80`, hit `0.5875`, avg `0.028139`, median `0.034688`, mae `0.063347`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003147`, median `0.006228`, mae `0.014045`
- 5d: sample `40`, hit `0.525`, avg `0.00309`, median `0.002616`, mae `0.018177`
- 10d: sample `40`, hit `0.55`, avg `0.008949`, median `0.0076`, mae `0.022926`
- 20d: sample `40`, hit `0.7`, avg `0.01638`, median `0.020431`, mae `0.034893`
- 60d: sample `40`, hit `0.725`, avg `0.04549`, median `0.052998`, mae `0.070191`

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
- 3d: sample `40`, hit `0.55`, avg `0.002013`, median `0.004004`, mae `0.013473`
- 5d: sample `40`, hit `0.575`, avg `0.001711`, median `0.003026`, mae `0.016237`
- 10d: sample `40`, hit `0.625`, avg `0.008323`, median `0.0076`, mae `0.017088`
- 20d: sample `40`, hit `0.8`, avg `0.017079`, median `0.02086`, mae `0.028718`
- 60d: sample `40`, hit `0.55`, avg `0.015295`, median `0.029917`, mae `0.057985`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007819`, median `0.009928`, mae `0.014759`
- 5d: sample `40`, hit `0.7`, avg `0.009635`, median `0.009832`, mae `0.020698`
- 10d: sample `40`, hit `0.55`, avg `0.005764`, median `0.006913`, mae `0.029528`
- 20d: sample `40`, hit `0.575`, avg `0.00181`, median `0.009112`, mae `0.045124`
- 60d: sample `40`, hit `0.625`, avg `0.040982`, median `0.050225`, mae `0.068708`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.002013`, median `0.004004`, mae `0.013473`
- 5d: sample `40`, hit `0.575`, avg `0.001711`, median `0.003026`, mae `0.016237`
- 10d: sample `40`, hit `0.625`, avg `0.008323`, median `0.0076`, mae `0.017088`
- 20d: sample `40`, hit `0.8`, avg `0.017079`, median `0.02086`, mae `0.028718`
- 60d: sample `40`, hit `0.55`, avg `0.015295`, median `0.029917`, mae `0.057985`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004916`, median `0.006228`, mae `0.014116`
- 5d: sample `80`, hit `0.6375`, avg `0.005673`, median `0.005876`, mae `0.018468`
- 10d: sample `80`, hit `0.5875`, avg `0.007044`, median `0.007467`, mae `0.023308`
- 20d: sample `80`, hit `0.6875`, avg `0.009445`, median `0.017608`, mae `0.036921`
- 60d: sample `80`, hit `0.5875`, avg `0.028139`, median `0.034688`, mae `0.063347`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004916`, median `0.006228`, mae `0.014116`
- 5d: sample `80`, hit `0.6375`, avg `0.005673`, median `0.005876`, mae `0.018468`
- 10d: sample `80`, hit `0.5875`, avg `0.007044`, median `0.007467`, mae `0.023308`
- 20d: sample `80`, hit `0.6875`, avg `0.009445`, median `0.017608`, mae `0.036921`
- 60d: sample `80`, hit `0.5875`, avg `0.028139`, median `0.034688`, mae `0.063347`

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
