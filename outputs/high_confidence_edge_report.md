# High Confidence Edge Report

Generated at: `2026-08-18T21:53:45.831770+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.002945`, median `0.006198`, mae `0.014613`
- 5d: sample `60`, hit `0.65`, avg `0.00592`, median `0.007324`, mae `0.016352`
- 10d: sample `60`, hit `0.6167`, avg `0.005242`, median `0.010495`, mae `0.022646`
- 20d: sample `60`, hit `0.7333`, avg `0.011459`, median `0.021844`, mae `0.037731`
- 60d: sample `60`, hit `0.6167`, avg `0.020677`, median `0.045044`, mae `0.069054`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008956`, median `0.010849`, mae `0.016873`
- 5d: sample `20`, hit `0.55`, avg `0.004673`, median `0.001654`, mae `0.023064`
- 10d: sample `20`, hit `0.7`, avg `0.019097`, median `0.016536`, mae `0.034853`
- 20d: sample `20`, hit `0.7`, avg `0.039422`, median `0.029018`, mae `0.060334`
- 60d: sample `20`, hit `0.85`, avg `0.066715`, median `0.065495`, mae `0.078815`

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
- 3d: sample `8`, hit `0.625`, avg `0.004628`, median `0.009229`, mae `0.00991`
- 5d: sample `8`, hit `0.625`, avg `0.003822`, median `0.005319`, mae `0.008836`
- 10d: sample `8`, hit `0.875`, avg `0.010374`, median `0.011426`, mae `0.014655`
- 20d: sample `8`, hit `0.75`, avg `0.016632`, median `0.022652`, mae `0.022311`
- 60d: sample `8`, hit `0.375`, avg `0.01085`, median `-0.020268`, mae `0.052934`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.004628`, median `0.009229`, mae `0.00991`
- 5d: sample `8`, hit `0.625`, avg `0.003822`, median `0.005319`, mae `0.008836`
- 10d: sample `8`, hit `0.875`, avg `0.010374`, median `0.011426`, mae `0.014655`
- 20d: sample `8`, hit `0.75`, avg `0.016632`, median `0.022652`, mae `0.022311`
- 60d: sample `8`, hit `0.375`, avg `0.01085`, median `-0.020268`, mae `0.052934`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.002945, 'median_return': 0.006198, 'mean_absolute_return': 0.014613, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030961}, '5d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.00592, 'median_return': 0.007324, 'mean_absolute_return': 0.016352, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.005242, 'median_return': 0.010495, 'mean_absolute_return': 0.022646, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.011459, 'median_return': 0.021844, 'mean_absolute_return': 0.037731, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.020677, 'median_return': 0.045044, 'mean_absolute_return': 0.069054, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004628, 'median_return': 0.009229, 'mean_absolute_return': 0.00991, 'max_adverse_excursion': -0.012068, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003822, 'median_return': 0.005319, 'mean_absolute_return': 0.008836, 'max_adverse_excursion': -0.00805, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.010374, 'median_return': 0.011426, 'mean_absolute_return': 0.014655, 'max_adverse_excursion': -0.017124, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016632, 'median_return': 0.022652, 'mean_absolute_return': 0.022311, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.01085, 'median_return': -0.020268, 'mean_absolute_return': 0.052934, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.004428, 'median_return': 0.006714, 'mean_absolute_return': 0.015763, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.005807, 'median_return': 0.006452, 'mean_absolute_return': 0.019051, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.00852, 'median_return': 0.012215, 'mean_absolute_return': 0.026925, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.018651, 'median_return': 0.023636, 'mean_absolute_return': 0.045723, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.034557, 'median_return': 0.046273, 'mean_absolute_return': 0.073557, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.0, 'both_hit': 25, 'both_miss': 15}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.1, 'both_hit': 24, 'both_miss': 16}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.025, 'both_hit': 24, 'both_miss': 16}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.025, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.15, 'both_hit': 26, 'both_miss': 14}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004448, 'median_return': 0.006714, 'mean_absolute_return': 0.015178, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.005608, 'median_return': 0.005327, 'mean_absolute_return': 0.01803, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.008706, 'median_return': 0.011426, 'mean_absolute_return': 0.025698, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.01845, 'median_return': 0.022652, 'mean_absolute_return': 0.043382, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.032187, 'median_return': 0.046132, 'mean_absolute_return': 0.071494, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.000638`, median `0.004542`, mae `0.013137`
- 5d: sample `40`, hit `0.675`, avg `0.005932`, median `0.007324`, mae `0.014339`
- 10d: sample `40`, hit `0.675`, avg `0.006977`, median `0.011426`, mae `0.019064`
- 20d: sample `40`, hit `0.775`, avg `0.016735`, median `0.023636`, mae `0.030785`
- 60d: sample `40`, hit `0.55`, avg `0.0228`, median `0.030553`, mae `0.053233`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008956`, median `0.010849`, mae `0.016873`
- 5d: sample `20`, hit `0.55`, avg `0.004673`, median `0.001654`, mae `0.023064`
- 10d: sample `20`, hit `0.7`, avg `0.019097`, median `0.016536`, mae `0.034853`
- 20d: sample `20`, hit `0.7`, avg `0.039422`, median `0.029018`, mae `0.060334`
- 60d: sample `20`, hit `0.85`, avg `0.066715`, median `0.065495`, mae `0.078815`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.000638`, median `0.004542`, mae `0.013137`
- 5d: sample `40`, hit `0.675`, avg `0.005932`, median `0.007324`, mae `0.014339`
- 10d: sample `40`, hit `0.675`, avg `0.006977`, median `0.011426`, mae `0.019064`
- 20d: sample `40`, hit `0.775`, avg `0.016735`, median `0.023636`, mae `0.030785`
- 60d: sample `40`, hit `0.55`, avg `0.0228`, median `0.030553`, mae `0.053233`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.000638`, median `0.004542`, mae `0.013137`
- 5d: sample `40`, hit `0.675`, avg `0.005932`, median `0.007324`, mae `0.014339`
- 10d: sample `40`, hit `0.675`, avg `0.006977`, median `0.011426`, mae `0.019064`
- 20d: sample `40`, hit `0.775`, avg `0.016735`, median `0.023636`, mae `0.030785`
- 60d: sample `40`, hit `0.55`, avg `0.0228`, median `0.030553`, mae `0.053233`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008956`, median `0.010849`, mae `0.016873`
- 5d: sample `20`, hit `0.55`, avg `0.004673`, median `0.001654`, mae `0.023064`
- 10d: sample `20`, hit `0.7`, avg `0.019097`, median `0.016536`, mae `0.034853`
- 20d: sample `20`, hit `0.7`, avg `0.039422`, median `0.029018`, mae `0.060334`
- 60d: sample `20`, hit `0.85`, avg `0.066715`, median `0.065495`, mae `0.078815`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.000638`, median `0.004542`, mae `0.013137`
- 5d: sample `40`, hit `0.675`, avg `0.005932`, median `0.007324`, mae `0.014339`
- 10d: sample `40`, hit `0.675`, avg `0.006977`, median `0.011426`, mae `0.019064`
- 20d: sample `40`, hit `0.775`, avg `0.016735`, median `0.023636`, mae `0.030785`
- 60d: sample `40`, hit `0.55`, avg `0.0228`, median `0.030553`, mae `0.053233`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.007557`, median `0.013042`, mae `0.017564`
- 5d: sample `20`, hit `0.6`, avg `0.005897`, median `0.010393`, mae `0.020377`
- 10d: sample `20`, hit `0.5`, avg `0.001772`, median `0.004807`, mae `0.029811`
- 20d: sample `20`, hit `0.65`, avg `0.000906`, median `0.01666`, mae `0.051623`
- 60d: sample `20`, hit `0.75`, avg `0.016432`, median `0.063119`, mae `0.100698`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.000638`, median `0.004542`, mae `0.013137`
- 5d: sample `40`, hit `0.675`, avg `0.005932`, median `0.007324`, mae `0.014339`
- 10d: sample `40`, hit `0.675`, avg `0.006977`, median `0.011426`, mae `0.019064`
- 20d: sample `40`, hit `0.775`, avg `0.016735`, median `0.023636`, mae `0.030785`
- 60d: sample `40`, hit `0.55`, avg `0.0228`, median `0.030553`, mae `0.053233`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008956`, median `0.010849`, mae `0.016873`
- 5d: sample `20`, hit `0.55`, avg `0.004673`, median `0.001654`, mae `0.023064`
- 10d: sample `20`, hit `0.7`, avg `0.019097`, median `0.016536`, mae `0.034853`
- 20d: sample `20`, hit `0.7`, avg `0.039422`, median `0.029018`, mae `0.060334`
- 60d: sample `20`, hit `0.85`, avg `0.066715`, median `0.065495`, mae `0.078815`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004448`, median `0.006714`, mae `0.015178`
- 5d: sample `80`, hit `0.625`, avg `0.005608`, median `0.005327`, mae `0.01803`
- 10d: sample `80`, hit `0.6375`, avg `0.008706`, median `0.011426`, mae `0.025698`
- 20d: sample `80`, hit `0.725`, avg `0.01845`, median `0.022652`, mae `0.043382`
- 60d: sample `80`, hit `0.675`, avg `0.032187`, median `0.046132`, mae `0.071494`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.002945`, median `0.006198`, mae `0.014613`
- 5d: sample `60`, hit `0.65`, avg `0.00592`, median `0.007324`, mae `0.016352`
- 10d: sample `60`, hit `0.6167`, avg `0.005242`, median `0.010495`, mae `0.022646`
- 20d: sample `60`, hit `0.7333`, avg `0.011459`, median `0.021844`, mae `0.037731`
- 60d: sample `60`, hit `0.6167`, avg `0.020677`, median `0.045044`, mae `0.069054`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004448`, median `0.006714`, mae `0.015178`
- 5d: sample `80`, hit `0.625`, avg `0.005608`, median `0.005327`, mae `0.01803`
- 10d: sample `80`, hit `0.6375`, avg `0.008706`, median `0.011426`, mae `0.025698`
- 20d: sample `80`, hit `0.725`, avg `0.01845`, median `0.022652`, mae `0.043382`
- 60d: sample `80`, hit `0.675`, avg `0.032187`, median `0.046132`, mae `0.071494`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.002945`, median `0.006198`, mae `0.014613`
- 5d: sample `60`, hit `0.65`, avg `0.00592`, median `0.007324`, mae `0.016352`
- 10d: sample `60`, hit `0.6167`, avg `0.005242`, median `0.010495`, mae `0.022646`
- 20d: sample `60`, hit `0.7333`, avg `0.011459`, median `0.021844`, mae `0.037731`
- 60d: sample `60`, hit `0.6167`, avg `0.020677`, median `0.045044`, mae `0.069054`

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
