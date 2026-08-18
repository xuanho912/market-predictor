# High Confidence Edge Report

Generated at: `2026-08-18T20:47:07.955753+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `60`
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
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.004594`, median `0.010322`, mae `0.016428`
- 5d: sample `40`, hit `0.575`, avg `0.004792`, median `0.005327`, mae `0.0191`
- 10d: sample `40`, hit `0.6`, avg `0.003834`, median `0.005422`, mae `0.027045`
- 20d: sample `40`, hit `0.7`, avg `0.005933`, median `0.01666`, mae `0.045343`
- 60d: sample `40`, hit `0.625`, avg `0.010358`, median `0.052998`, mae `0.088464`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006735`, median `0.009966`, mae `0.015032`
- 5d: sample `20`, hit `0.6`, avg `0.004066`, median `0.004787`, mae `0.020907`
- 10d: sample `20`, hit `0.7`, avg `0.016672`, median `0.016085`, mae `0.032427`
- 20d: sample `20`, hit `0.65`, avg `0.032569`, median `0.015261`, mae `0.053706`
- 60d: sample `20`, hit `0.8`, avg `0.056577`, median `0.061844`, mae `0.073964`

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
- sample_size: `6`
- 3d: sample `6`, hit `0.8333`, avg `0.001102`, median `0.012355`, mae `0.018283`
- 5d: sample `6`, hit `0.6667`, avg `0.003127`, median `0.010241`, mae `0.011978`
- 10d: sample `6`, hit `0.8333`, avg `0.007415`, median `0.021953`, mae `0.018584`
- 20d: sample `6`, hit `0.5`, avg `-0.00051`, median `0.024743`, mae `0.03891`
- 60d: sample `6`, hit `0.6667`, avg `0.033664`, median `0.082251`, mae `0.061566`

### confidence_score top 10%
- sample_size: `6`
- 3d: sample `6`, hit `0.8333`, avg `0.001102`, median `0.012355`, mae `0.018283`
- 5d: sample `6`, hit `0.6667`, avg `0.003127`, median `0.010241`, mae `0.011978`
- 10d: sample `6`, hit `0.8333`, avg `0.007415`, median `0.021953`, mae `0.018584`
- 20d: sample `6`, hit `0.5`, avg `-0.00051`, median `0.024743`, mae `0.03891`
- 60d: sample `6`, hit `0.6667`, avg `0.033664`, median `0.082251`, mae `0.061566`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.004594, 'median_return': 0.010322, 'mean_absolute_return': 0.016428, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030961}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.004792, 'median_return': 0.005327, 'mean_absolute_return': 0.0191, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003834, 'median_return': 0.005422, 'mean_absolute_return': 0.027045, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.005933, 'median_return': 0.01666, 'mean_absolute_return': 0.045343, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.010358, 'median_return': 0.052998, 'mean_absolute_return': 0.088464, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 6, 'by_horizon': {'3d': {'sample_size': 6, 'hit_rate': 0.8333, 'avg_return': 0.001102, 'median_return': 0.012355, 'mean_absolute_return': 0.018283, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.003127, 'median_return': 0.010241, 'mean_absolute_return': 0.011978, 'max_adverse_excursion': -0.018503, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 6, 'hit_rate': 0.8333, 'avg_return': 0.007415, 'median_return': 0.021953, 'mean_absolute_return': 0.018584, 'max_adverse_excursion': -0.033507, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 6, 'hit_rate': 0.5, 'avg_return': -0.00051, 'median_return': 0.024743, 'mean_absolute_return': 0.03891, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.033664, 'median_return': 0.082251, 'mean_absolute_return': 0.061566, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 54, 'by_horizon': {'3d': {'sample_size': 54, 'hit_rate': 0.6111, 'avg_return': 0.005775, 'median_return': 0.009966, 'mean_absolute_return': 0.015705, 'max_adverse_excursion': -0.034061, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 54, 'hit_rate': 0.5741, 'avg_return': 0.004709, 'median_return': 0.005319, 'mean_absolute_return': 0.020561, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 54, 'hit_rate': 0.6111, 'avg_return': 0.008191, 'median_return': 0.011168, 'mean_absolute_return': 0.029979, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 54, 'hit_rate': 0.7037, 'avg_return': 0.016514, 'median_return': 0.015261, 'mean_absolute_return': 0.049155, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 54, 'hit_rate': 0.6852, 'avg_return': 0.024886, 'median_return': 0.052998, 'mean_absolute_return': 0.086082, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 60, 'hit_rate': 0.5333}, '5d': {'sample_size': 60, 'hit_rate': 0.5167}, '10d': {'sample_size': 60, 'hit_rate': 0.5}, '20d': {'sample_size': 60, 'hit_rate': 0.5833}, '60d': {'sample_size': 60, 'hit_rate': 0.4833}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 60, 'primary_hit_rate': 0.5333, 'secondary_hit_rate': 0.6333, 'primary_minus_secondary': -0.1, 'both_hit': 25, 'both_miss': 15}, '5d': {'sample_size': 60, 'primary_hit_rate': 0.5167, 'secondary_hit_rate': 0.5833, 'primary_minus_secondary': -0.0667, 'both_hit': 23, 'both_miss': 17}, '10d': {'sample_size': 60, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.6333, 'primary_minus_secondary': -0.1333, 'both_hit': 24, 'both_miss': 16}, '20d': {'sample_size': 60, 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.6833, 'primary_minus_secondary': -0.1, 'both_hit': 28, 'both_miss': 12}, '60d': {'sample_size': 60, 'primary_hit_rate': 0.4833, 'secondary_hit_rate': 0.6833, 'primary_minus_secondary': -0.2, 'both_hit': 25, 'both_miss': 15}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.005308, 'median_return': 0.009966, 'mean_absolute_return': 0.015963, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.00455, 'median_return': 0.005319, 'mean_absolute_return': 0.019702, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.008113, 'median_return': 0.011168, 'mean_absolute_return': 0.028839, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.014812, 'median_return': 0.015261, 'mean_absolute_return': 0.048131, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.025764, 'median_return': 0.052998, 'mean_absolute_return': 0.083631, 'max_adverse_excursion': -0.253302, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001631`, median `0.009229`, mae `0.015293`
- 5d: sample `20`, hit `0.55`, avg `0.003688`, median `0.005319`, mae `0.017822`
- 10d: sample `20`, hit `0.7`, avg `0.005895`, median `0.011426`, mae `0.024279`
- 20d: sample `20`, hit `0.75`, avg `0.01096`, median `0.022652`, mae `0.039062`
- 60d: sample `20`, hit `0.5`, avg `0.004284`, median `0.030553`, mae `0.076229`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006735`, median `0.009966`, mae `0.015032`
- 5d: sample `20`, hit `0.6`, avg `0.004066`, median `0.004787`, mae `0.020907`
- 10d: sample `20`, hit `0.7`, avg `0.016672`, median `0.016085`, mae `0.032427`
- 20d: sample `20`, hit `0.65`, avg `0.032569`, median `0.015261`, mae `0.053706`
- 60d: sample `20`, hit `0.8`, avg `0.056577`, median `0.061844`, mae `0.073964`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001631`, median `0.009229`, mae `0.015293`
- 5d: sample `20`, hit `0.55`, avg `0.003688`, median `0.005319`, mae `0.017822`
- 10d: sample `20`, hit `0.7`, avg `0.005895`, median `0.011426`, mae `0.024279`
- 20d: sample `20`, hit `0.75`, avg `0.01096`, median `0.022652`, mae `0.039062`
- 60d: sample `20`, hit `0.5`, avg `0.004284`, median `0.030553`, mae `0.076229`

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
- 3d: sample `20`, hit `0.65`, avg `0.006735`, median `0.009966`, mae `0.015032`
- 5d: sample `20`, hit `0.6`, avg `0.004066`, median `0.004787`, mae `0.020907`
- 10d: sample `20`, hit `0.7`, avg `0.016672`, median `0.016085`, mae `0.032427`
- 20d: sample `20`, hit `0.65`, avg `0.032569`, median `0.015261`, mae `0.053706`
- 60d: sample `20`, hit `0.8`, avg `0.056577`, median `0.061844`, mae `0.073964`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001631`, median `0.009229`, mae `0.015293`
- 5d: sample `20`, hit `0.55`, avg `0.003688`, median `0.005319`, mae `0.017822`
- 10d: sample `20`, hit `0.7`, avg `0.005895`, median `0.011426`, mae `0.024279`
- 20d: sample `20`, hit `0.75`, avg `0.01096`, median `0.022652`, mae `0.039062`
- 60d: sample `20`, hit `0.5`, avg `0.004284`, median `0.030553`, mae `0.076229`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.007557`, median `0.013042`, mae `0.017564`
- 5d: sample `20`, hit `0.6`, avg `0.005897`, median `0.010393`, mae `0.020377`
- 10d: sample `20`, hit `0.5`, avg `0.001772`, median `0.004807`, mae `0.029811`
- 20d: sample `20`, hit `0.65`, avg `0.000906`, median `0.01666`, mae `0.051623`
- 60d: sample `20`, hit `0.75`, avg `0.016432`, median `0.063119`, mae `0.100698`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006735`, median `0.009966`, mae `0.015032`
- 5d: sample `20`, hit `0.6`, avg `0.004066`, median `0.004787`, mae `0.020907`
- 10d: sample `20`, hit `0.7`, avg `0.016672`, median `0.016085`, mae `0.032427`
- 20d: sample `20`, hit `0.65`, avg `0.032569`, median `0.015261`, mae `0.053706`
- 60d: sample `20`, hit `0.8`, avg `0.056577`, median `0.061844`, mae `0.073964`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.005308`, median `0.009966`, mae `0.015963`
- 5d: sample `60`, hit `0.5833`, avg `0.00455`, median `0.005319`, mae `0.019702`
- 10d: sample `60`, hit `0.6333`, avg `0.008113`, median `0.011168`, mae `0.028839`
- 20d: sample `60`, hit `0.6833`, avg `0.014812`, median `0.015261`, mae `0.048131`
- 60d: sample `60`, hit `0.6833`, avg `0.025764`, median `0.052998`, mae `0.083631`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.004594`, median `0.010322`, mae `0.016428`
- 5d: sample `40`, hit `0.575`, avg `0.004792`, median `0.005327`, mae `0.0191`
- 10d: sample `40`, hit `0.6`, avg `0.003834`, median `0.005422`, mae `0.027045`
- 20d: sample `40`, hit `0.7`, avg `0.005933`, median `0.01666`, mae `0.045343`
- 60d: sample `40`, hit `0.625`, avg `0.010358`, median `0.052998`, mae `0.088464`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.005308`, median `0.009966`, mae `0.015963`
- 5d: sample `60`, hit `0.5833`, avg `0.00455`, median `0.005319`, mae `0.019702`
- 10d: sample `60`, hit `0.6333`, avg `0.008113`, median `0.011168`, mae `0.028839`
- 20d: sample `60`, hit `0.6833`, avg `0.014812`, median `0.015261`, mae `0.048131`
- 60d: sample `60`, hit `0.6833`, avg `0.025764`, median `0.052998`, mae `0.083631`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.004594`, median `0.010322`, mae `0.016428`
- 5d: sample `40`, hit `0.575`, avg `0.004792`, median `0.005327`, mae `0.0191`
- 10d: sample `40`, hit `0.6`, avg `0.003834`, median `0.005422`, mae `0.027045`
- 20d: sample `40`, hit `0.7`, avg `0.005933`, median `0.01666`, mae `0.045343`
- 60d: sample `40`, hit `0.625`, avg `0.010358`, median `0.052998`, mae `0.088464`

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
