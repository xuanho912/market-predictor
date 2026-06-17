# High Confidence Edge Report

Generated at: `2026-06-17T00:01:27.119404+00:00`

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
- 3d: sample `80`, hit `0.65`, avg `0.005941`, median `0.006718`, mae `0.01524`
- 5d: sample `80`, hit `0.65`, avg `0.007072`, median `0.007324`, mae `0.020817`
- 10d: sample `80`, hit `0.65`, avg `0.01112`, median `0.012964`, mae `0.023752`
- 20d: sample `80`, hit `0.7625`, avg `0.0172`, median `0.02086`, mae `0.036412`
- 60d: sample `80`, hit `0.6375`, avg `0.033499`, median `0.043741`, mae `0.065776`

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
- 3d: sample `8`, hit `0.375`, avg `-0.009751`, median `-0.001811`, mae `0.015415`
- 5d: sample `8`, hit `0.125`, avg `-0.01508`, median `-0.013034`, mae `0.021076`
- 10d: sample `8`, hit `0.75`, avg `0.009728`, median `0.012964`, mae `0.015908`
- 20d: sample `8`, hit `0.875`, avg `0.023574`, median `0.029166`, mae `0.024809`
- 60d: sample `8`, hit `0.75`, avg `0.041325`, median `0.065295`, mae `0.064569`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.009751`, median `-0.001811`, mae `0.015415`
- 5d: sample `8`, hit `0.125`, avg `-0.01508`, median `-0.013034`, mae `0.021076`
- 10d: sample `8`, hit `0.75`, avg `0.009728`, median `0.012964`, mae `0.015908`
- 20d: sample `8`, hit `0.875`, avg `0.023574`, median `0.029166`, mae `0.024809`
- 60d: sample `8`, hit `0.75`, avg `0.041325`, median `0.065295`, mae `0.064569`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.005941, 'median_return': 0.006718, 'mean_absolute_return': 0.01524, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.007072, 'median_return': 0.007324, 'mean_absolute_return': 0.020817, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.01112, 'median_return': 0.012964, 'mean_absolute_return': 0.023752, 'max_adverse_excursion': -0.061818, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.0172, 'median_return': 0.02086, 'mean_absolute_return': 0.036412, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.033499, 'median_return': 0.043741, 'mean_absolute_return': 0.065776, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.183622}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.009751, 'median_return': -0.001811, 'mean_absolute_return': 0.015415, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.01508, 'median_return': -0.013034, 'mean_absolute_return': 0.021076, 'max_adverse_excursion': -0.033198, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009728, 'median_return': 0.012964, 'mean_absolute_return': 0.015908, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.023574, 'median_return': 0.029166, 'mean_absolute_return': 0.024809, 'max_adverse_excursion': -0.004939, 'max_favorable_excursion': 0.03323}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.041325, 'median_return': 0.065295, 'mean_absolute_return': 0.064569, 'max_adverse_excursion': -0.072844, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.007685, 'median_return': 0.008337, 'mean_absolute_return': 0.015221, 'max_adverse_excursion': -0.026663, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.009533, 'median_return': 0.010385, 'mean_absolute_return': 0.020789, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.011275, 'median_return': 0.013144, 'mean_absolute_return': 0.024623, 'max_adverse_excursion': -0.061818, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.016492, 'median_return': 0.019987, 'mean_absolute_return': 0.037701, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.03263, 'median_return': 0.036062, 'mean_absolute_return': 0.06591, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.183622}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.65}, '5d': {'sample_size': 80, 'hit_rate': 0.65}, '10d': {'sample_size': 80, 'hit_rate': 0.65}, '20d': {'sample_size': 80, 'hit_rate': 0.7625}, '60d': {'sample_size': 80, 'hit_rate': 0.6375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 52, 'both_miss': 28}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 52, 'both_miss': 28}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 52, 'both_miss': 28}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7625, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': 0.0, 'both_hit': 61, 'both_miss': 19}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.005941, 'median_return': 0.006718, 'mean_absolute_return': 0.01524, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.007072, 'median_return': 0.007324, 'mean_absolute_return': 0.020817, 'max_adverse_excursion': -0.052675, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.01112, 'median_return': 0.012964, 'mean_absolute_return': 0.023752, 'max_adverse_excursion': -0.061818, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.0172, 'median_return': 0.02086, 'mean_absolute_return': 0.036412, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.033499, 'median_return': 0.043741, 'mean_absolute_return': 0.065776, 'max_adverse_excursion': -0.155484, 'max_favorable_excursion': 0.183622}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.005941`, median `0.006718`, mae `0.01524`
- 5d: sample `80`, hit `0.65`, avg `0.007072`, median `0.007324`, mae `0.020817`
- 10d: sample `80`, hit `0.65`, avg `0.01112`, median `0.012964`, mae `0.023752`
- 20d: sample `80`, hit `0.7625`, avg `0.0172`, median `0.02086`, mae `0.036412`
- 60d: sample `80`, hit `0.6375`, avg `0.033499`, median `0.043741`, mae `0.065776`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.005941`, median `0.006718`, mae `0.01524`
- 5d: sample `80`, hit `0.65`, avg `0.007072`, median `0.007324`, mae `0.020817`
- 10d: sample `80`, hit `0.65`, avg `0.01112`, median `0.012964`, mae `0.023752`
- 20d: sample `80`, hit `0.7625`, avg `0.0172`, median `0.02086`, mae `0.036412`
- 60d: sample `80`, hit `0.6375`, avg `0.033499`, median `0.043741`, mae `0.065776`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005926`, median `0.00861`, mae `0.016296`
- 5d: sample `60`, hit `0.6167`, avg `0.006981`, median `0.008121`, mae `0.022751`
- 10d: sample `60`, hit `0.65`, avg `0.012066`, median `0.014843`, mae `0.026148`
- 20d: sample `60`, hit `0.7667`, avg `0.019673`, median `0.026531`, mae `0.039525`
- 60d: sample `60`, hit `0.7333`, avg `0.04741`, median `0.062356`, mae `0.070694`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.005941`, median `0.006718`, mae `0.01524`
- 5d: sample `80`, hit `0.65`, avg `0.007072`, median `0.007324`, mae `0.020817`
- 10d: sample `80`, hit `0.65`, avg `0.01112`, median `0.012964`, mae `0.023752`
- 20d: sample `80`, hit `0.7625`, avg `0.0172`, median `0.02086`, mae `0.036412`
- 60d: sample `80`, hit `0.6375`, avg `0.033499`, median `0.043741`, mae `0.065776`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005926`, median `0.00861`, mae `0.016296`
- 5d: sample `60`, hit `0.6167`, avg `0.006981`, median `0.008121`, mae `0.022751`
- 10d: sample `60`, hit `0.65`, avg `0.012066`, median `0.014843`, mae `0.026148`
- 20d: sample `60`, hit `0.7667`, avg `0.019673`, median `0.026531`, mae `0.039525`
- 60d: sample `60`, hit `0.7333`, avg `0.04741`, median `0.062356`, mae `0.070694`

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
- 3d: sample `40`, hit `0.575`, avg `0.003681`, median `0.004542`, mae `0.014537`
- 5d: sample `40`, hit `0.575`, avg `0.002283`, median `0.003026`, mae `0.0169`
- 10d: sample `40`, hit `0.625`, avg `0.009027`, median `0.007467`, mae `0.017062`
- 20d: sample `40`, hit `0.825`, avg `0.018923`, median `0.02284`, mae `0.030183`
- 60d: sample `40`, hit `0.6`, avg `0.019821`, median `0.03283`, mae `0.059055`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.008202`, median `0.009928`, mae `0.015943`
- 5d: sample `40`, hit `0.725`, avg `0.01186`, median `0.015031`, mae `0.024735`
- 10d: sample `40`, hit `0.675`, avg `0.013213`, median `0.018412`, mae `0.030442`
- 20d: sample `40`, hit `0.7`, avg `0.015477`, median `0.020431`, mae `0.042641`
- 60d: sample `40`, hit `0.675`, avg `0.047178`, median `0.062356`, mae `0.072497`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.003681`, median `0.004542`, mae `0.014537`
- 5d: sample `40`, hit `0.575`, avg `0.002283`, median `0.003026`, mae `0.0169`
- 10d: sample `40`, hit `0.625`, avg `0.009027`, median `0.007467`, mae `0.017062`
- 20d: sample `40`, hit `0.825`, avg `0.018923`, median `0.02284`, mae `0.030183`
- 60d: sample `40`, hit `0.6`, avg `0.019821`, median `0.03283`, mae `0.059055`

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
- 3d: sample `80`, hit `0.65`, avg `0.005941`, median `0.006718`, mae `0.01524`
- 5d: sample `80`, hit `0.65`, avg `0.007072`, median `0.007324`, mae `0.020817`
- 10d: sample `80`, hit `0.65`, avg `0.01112`, median `0.012964`, mae `0.023752`
- 20d: sample `80`, hit `0.7625`, avg `0.0172`, median `0.02086`, mae `0.036412`
- 60d: sample `80`, hit `0.6375`, avg `0.033499`, median `0.043741`, mae `0.065776`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.005941`, median `0.006718`, mae `0.01524`
- 5d: sample `80`, hit `0.65`, avg `0.007072`, median `0.007324`, mae `0.020817`
- 10d: sample `80`, hit `0.65`, avg `0.01112`, median `0.012964`, mae `0.023752`
- 20d: sample `80`, hit `0.7625`, avg `0.0172`, median `0.02086`, mae `0.036412`
- 60d: sample `80`, hit `0.6375`, avg `0.033499`, median `0.043741`, mae `0.065776`

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
