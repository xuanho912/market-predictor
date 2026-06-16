# High Confidence Edge Report

Generated at: `2026-06-16T14:42:19.012766+00:00`

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
- 3d: sample `80`, hit `0.625`, avg `0.004683`, median `0.005458`, mae `0.014211`
- 5d: sample `80`, hit `0.6375`, avg `0.00603`, median `0.005876`, mae `0.018125`
- 10d: sample `80`, hit `0.6`, avg `0.007406`, median `0.00903`, mae `0.022975`
- 20d: sample `80`, hit `0.6875`, avg `0.009061`, median `0.017608`, mae `0.035702`
- 60d: sample `80`, hit `0.6125`, avg `0.02811`, median `0.032982`, mae `0.062405`

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
- 3d: sample `8`, hit `0.375`, avg `-0.007736`, median `-0.001811`, mae `0.0134`
- 5d: sample `8`, hit `0.125`, avg `-0.011553`, median `-0.012956`, mae `0.01755`
- 10d: sample `8`, hit `0.625`, avg `0.005967`, median `0.0076`, mae `0.016428`
- 20d: sample `8`, hit `1.0`, avg `0.027023`, median `0.029166`, mae `0.027023`
- 60d: sample `8`, hit `0.75`, avg `0.04658`, median `0.065295`, mae `0.059314`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.007736`, median `-0.001811`, mae `0.0134`
- 5d: sample `8`, hit `0.125`, avg `-0.011553`, median `-0.012956`, mae `0.01755`
- 10d: sample `8`, hit `0.625`, avg `0.005967`, median `0.0076`, mae `0.016428`
- 20d: sample `8`, hit `1.0`, avg `0.027023`, median `0.029166`, mae `0.027023`
- 60d: sample `8`, hit `0.75`, avg `0.04658`, median `0.065295`, mae `0.059314`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.004683, 'median_return': 0.005458, 'mean_absolute_return': 0.014211, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.00603, 'median_return': 0.005876, 'mean_absolute_return': 0.018125, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.007406, 'median_return': 0.00903, 'mean_absolute_return': 0.022975, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.009061, 'median_return': 0.017608, 'mean_absolute_return': 0.035702, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.02811, 'median_return': 0.032982, 'mean_absolute_return': 0.062405, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007736, 'median_return': -0.001811, 'mean_absolute_return': 0.0134, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011553, 'median_return': -0.012956, 'mean_absolute_return': 0.01755, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005967, 'median_return': 0.0076, 'mean_absolute_return': 0.016428, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.027023, 'median_return': 0.029166, 'mean_absolute_return': 0.027023, 'max_adverse_excursion': 0.012958, 'max_favorable_excursion': 0.03323}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.04658, 'median_return': 0.065295, 'mean_absolute_return': 0.059314, 'max_adverse_excursion': -0.03081, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.006062, 'median_return': 0.006722, 'mean_absolute_return': 0.014302, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.007984, 'median_return': 0.007324, 'mean_absolute_return': 0.018189, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.007566, 'median_return': 0.009675, 'mean_absolute_return': 0.023702, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007066, 'median_return': 0.015661, 'mean_absolute_return': 0.036667, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.026058, 'median_return': 0.03283, 'mean_absolute_return': 0.062749, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': 0.0, 'both_hit': 55, 'both_miss': 25}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.004683, 'median_return': 0.005458, 'mean_absolute_return': 0.014211, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.00603, 'median_return': 0.005876, 'mean_absolute_return': 0.018125, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.007406, 'median_return': 0.00903, 'mean_absolute_return': 0.022975, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.009061, 'median_return': 0.017608, 'mean_absolute_return': 0.035702, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.02811, 'median_return': 0.032982, 'mean_absolute_return': 0.062405, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.004683`, median `0.005458`, mae `0.014211`
- 5d: sample `80`, hit `0.6375`, avg `0.00603`, median `0.005876`, mae `0.018125`
- 10d: sample `80`, hit `0.6`, avg `0.007406`, median `0.00903`, mae `0.022975`
- 20d: sample `80`, hit `0.6875`, avg `0.009061`, median `0.017608`, mae `0.035702`
- 60d: sample `80`, hit `0.6125`, avg `0.02811`, median `0.032982`, mae `0.062405`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.004683`, median `0.005458`, mae `0.014211`
- 5d: sample `80`, hit `0.6375`, avg `0.00603`, median `0.005876`, mae `0.018125`
- 10d: sample `80`, hit `0.6`, avg `0.007406`, median `0.00903`, mae `0.022975`
- 20d: sample `80`, hit `0.6875`, avg `0.009061`, median `0.017608`, mae `0.035702`
- 60d: sample `80`, hit `0.6125`, avg `0.02811`, median `0.032982`, mae `0.062405`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003283`, median `0.006718`, mae `0.014182`
- 5d: sample `40`, hit `0.525`, avg `0.002905`, median `0.002616`, mae `0.017992`
- 10d: sample `40`, hit `0.575`, avg `0.009061`, median `0.00903`, mae `0.022128`
- 20d: sample `40`, hit `0.725`, avg `0.017079`, median `0.020431`, mae `0.033793`
- 60d: sample `40`, hit `0.725`, avg `0.047778`, median `0.064286`, mae `0.07248`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.004683`, median `0.005458`, mae `0.014211`
- 5d: sample `80`, hit `0.6375`, avg `0.00603`, median `0.005876`, mae `0.018125`
- 10d: sample `80`, hit `0.6`, avg `0.007406`, median `0.00903`, mae `0.022975`
- 20d: sample `80`, hit `0.6875`, avg `0.009061`, median `0.017608`, mae `0.035702`
- 60d: sample `80`, hit `0.6125`, avg `0.02811`, median `0.032982`, mae `0.062405`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003283`, median `0.006718`, mae `0.014182`
- 5d: sample `40`, hit `0.525`, avg `0.002905`, median `0.002616`, mae `0.017992`
- 10d: sample `40`, hit `0.575`, avg `0.009061`, median `0.00903`, mae `0.022128`
- 20d: sample `40`, hit `0.725`, avg `0.017079`, median `0.020431`, mae `0.033793`
- 60d: sample `40`, hit `0.725`, avg `0.047778`, median `0.064286`, mae `0.07248`

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
- 3d: sample `40`, hit `0.525`, avg `0.000862`, median `0.001558`, mae `0.013802`
- 5d: sample `40`, hit `0.55`, avg `0.00067`, median `0.003026`, mae `0.01643`
- 10d: sample `40`, hit `0.6`, avg `0.006691`, median `0.0076`, mae `0.016622`
- 20d: sample `40`, hit `0.8`, avg `0.016872`, median `0.022652`, mae `0.028511`
- 60d: sample `40`, hit `0.575`, avg `0.018007`, median `0.029917`, mae `0.059771`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.008503`, median `0.009928`, mae `0.01462`
- 5d: sample `40`, hit `0.725`, avg `0.01139`, median `0.009832`, mae `0.019819`
- 10d: sample `40`, hit `0.6`, avg `0.00812`, median `0.01246`, mae `0.029328`
- 20d: sample `40`, hit `0.575`, avg `0.001251`, median `0.009812`, mae `0.042893`
- 60d: sample `40`, hit `0.65`, avg `0.038214`, median `0.050225`, mae `0.06504`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000862`, median `0.001558`, mae `0.013802`
- 5d: sample `40`, hit `0.55`, avg `0.00067`, median `0.003026`, mae `0.01643`
- 10d: sample `40`, hit `0.6`, avg `0.006691`, median `0.0076`, mae `0.016622`
- 20d: sample `40`, hit `0.8`, avg `0.016872`, median `0.022652`, mae `0.028511`
- 60d: sample `40`, hit `0.575`, avg `0.018007`, median `0.029917`, mae `0.059771`

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
- 3d: sample `80`, hit `0.625`, avg `0.004683`, median `0.005458`, mae `0.014211`
- 5d: sample `80`, hit `0.6375`, avg `0.00603`, median `0.005876`, mae `0.018125`
- 10d: sample `80`, hit `0.6`, avg `0.007406`, median `0.00903`, mae `0.022975`
- 20d: sample `80`, hit `0.6875`, avg `0.009061`, median `0.017608`, mae `0.035702`
- 60d: sample `80`, hit `0.6125`, avg `0.02811`, median `0.032982`, mae `0.062405`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.004683`, median `0.005458`, mae `0.014211`
- 5d: sample `80`, hit `0.6375`, avg `0.00603`, median `0.005876`, mae `0.018125`
- 10d: sample `80`, hit `0.6`, avg `0.007406`, median `0.00903`, mae `0.022975`
- 20d: sample `80`, hit `0.6875`, avg `0.009061`, median `0.017608`, mae `0.035702`
- 60d: sample `80`, hit `0.6125`, avg `0.02811`, median `0.032982`, mae `0.062405`

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
