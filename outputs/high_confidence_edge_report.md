# High Confidence Edge Report

Generated at: `2026-08-05T14:35:57.952996+00:00`

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
- 3d: sample `60`, hit `0.5833`, avg `0.001022`, median `0.003538`, mae `0.014036`
- 5d: sample `60`, hit `0.7`, avg `0.005339`, median `0.005327`, mae `0.014456`
- 10d: sample `60`, hit `0.55`, avg `0.003134`, median `0.005616`, mae `0.021665`
- 20d: sample `60`, hit `0.6833`, avg `0.007017`, median `0.013823`, mae `0.034701`
- 60d: sample `60`, hit `0.5333`, avg `0.015747`, median `0.030553`, mae `0.060286`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005393`, median `0.010849`, mae `0.017956`
- 5d: sample `20`, hit `0.6`, avg `0.002841`, median `0.010281`, mae `0.023937`
- 10d: sample `20`, hit `0.6`, avg `0.008014`, median `0.01246`, mae `0.036668`
- 20d: sample `20`, hit `0.65`, avg `0.015932`, median `0.015261`, mae `0.058703`
- 60d: sample `20`, hit `0.65`, avg `0.053839`, median `0.071905`, mae `0.083701`

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
- 3d: sample `8`, hit `0.625`, avg `-0.000325`, median `0.009229`, mae `0.015832`
- 5d: sample `8`, hit `0.75`, avg `0.005691`, median `0.013852`, mae `0.014846`
- 10d: sample `8`, hit `0.625`, avg `0.007415`, median `0.021953`, mae `0.022062`
- 20d: sample `8`, hit `0.625`, avg `0.015667`, median `0.026531`, mae `0.033175`
- 60d: sample `8`, hit `0.375`, avg `0.000291`, median `-0.02013`, mae `0.058742`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.000325`, median `0.009229`, mae `0.015832`
- 5d: sample `8`, hit `0.75`, avg `0.005691`, median `0.013852`, mae `0.014846`
- 10d: sample `8`, hit `0.625`, avg `0.007415`, median `0.021953`, mae `0.022062`
- 20d: sample `8`, hit `0.625`, avg `0.015667`, median `0.026531`, mae `0.033175`
- 60d: sample `8`, hit `0.375`, avg `0.000291`, median `-0.02013`, mae `0.058742`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.001022, 'median_return': 0.003538, 'mean_absolute_return': 0.014036, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.038451}, '5d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.005339, 'median_return': 0.005327, 'mean_absolute_return': 0.014456, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.003134, 'median_return': 0.005616, 'mean_absolute_return': 0.021665, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.007017, 'median_return': 0.013823, 'mean_absolute_return': 0.034701, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.015747, 'median_return': 0.030553, 'mean_absolute_return': 0.060286, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000325, 'median_return': 0.009229, 'mean_absolute_return': 0.015832, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005691, 'median_return': 0.013852, 'mean_absolute_return': 0.014846, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.007415, 'median_return': 0.021953, 'mean_absolute_return': 0.022062, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.015667, 'median_return': 0.026531, 'mean_absolute_return': 0.033175, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.000291, 'median_return': -0.02013, 'mean_absolute_return': 0.058742, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.102896}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.002386, 'median_return': 0.004569, 'mean_absolute_return': 0.014925, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.004606, 'median_return': 0.005327, 'mean_absolute_return': 0.017046, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.004014, 'median_return': 0.005616, 'mean_absolute_return': 0.025788, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.008532, 'median_return': 0.013178, 'mean_absolute_return': 0.041537, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.028046, 'median_return': 0.043546, 'mean_absolute_return': 0.066962, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.625}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.6}, '60d': {'sample_size': 80, 'hit_rate': 0.4875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.125, 'both_hit': 26, 'both_miss': 14}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.075, 'both_hit': 27, 'both_miss': 13}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.05, 'both_hit': 23, 'both_miss': 17}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.025, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.175, 'both_hit': 26, 'both_miss': 14}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.002115, 'median_return': 0.004569, 'mean_absolute_return': 0.015016, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.004715, 'median_return': 0.005327, 'mean_absolute_return': 0.016826, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.004354, 'median_return': 0.007467, 'mean_absolute_return': 0.025416, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.009246, 'median_return': 0.013823, 'mean_absolute_return': 0.040701, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.02527, 'median_return': 0.032982, 'mean_absolute_return': 0.06614, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.001022`, median `0.003538`, mae `0.014036`
- 5d: sample `60`, hit `0.7`, avg `0.005339`, median `0.005327`, mae `0.014456`
- 10d: sample `60`, hit `0.55`, avg `0.003134`, median `0.005616`, mae `0.021665`
- 20d: sample `60`, hit `0.6833`, avg `0.007017`, median `0.013823`, mae `0.034701`
- 60d: sample `60`, hit `0.5333`, avg `0.015747`, median `0.030553`, mae `0.060286`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005393`, median `0.010849`, mae `0.017956`
- 5d: sample `20`, hit `0.6`, avg `0.002841`, median `0.010281`, mae `0.023937`
- 10d: sample `20`, hit `0.6`, avg `0.008014`, median `0.01246`, mae `0.036668`
- 20d: sample `20`, hit `0.65`, avg `0.015932`, median `0.015261`, mae `0.058703`
- 60d: sample `20`, hit `0.65`, avg `0.053839`, median `0.071905`, mae `0.083701`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.001022`, median `0.003538`, mae `0.014036`
- 5d: sample `60`, hit `0.7`, avg `0.005339`, median `0.005327`, mae `0.014456`
- 10d: sample `60`, hit `0.55`, avg `0.003134`, median `0.005616`, mae `0.021665`
- 20d: sample `60`, hit `0.6833`, avg `0.007017`, median `0.013823`, mae `0.034701`
- 60d: sample `60`, hit `0.5333`, avg `0.015747`, median `0.030553`, mae `0.060286`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.001022`, median `0.003538`, mae `0.014036`
- 5d: sample `60`, hit `0.7`, avg `0.005339`, median `0.005327`, mae `0.014456`
- 10d: sample `60`, hit `0.55`, avg `0.003134`, median `0.005616`, mae `0.021665`
- 20d: sample `60`, hit `0.6833`, avg `0.007017`, median `0.013823`, mae `0.034701`
- 60d: sample `60`, hit `0.5333`, avg `0.015747`, median `0.030553`, mae `0.060286`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005393`, median `0.010849`, mae `0.017956`
- 5d: sample `20`, hit `0.6`, avg `0.002841`, median `0.010281`, mae `0.023937`
- 10d: sample `20`, hit `0.6`, avg `0.008014`, median `0.01246`, mae `0.036668`
- 20d: sample `20`, hit `0.65`, avg `0.015932`, median `0.015261`, mae `0.058703`
- 60d: sample `20`, hit `0.65`, avg `0.053839`, median `0.071905`, mae `0.083701`

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
- 3d: sample `80`, hit `0.6125`, avg `0.002115`, median `0.004569`, mae `0.015016`
- 5d: sample `80`, hit `0.675`, avg `0.004715`, median `0.005327`, mae `0.016826`
- 10d: sample `80`, hit `0.5625`, avg `0.004354`, median `0.007467`, mae `0.025416`
- 20d: sample `80`, hit `0.675`, avg `0.009246`, median `0.013823`, mae `0.040701`
- 60d: sample `80`, hit `0.5625`, avg `0.02527`, median `0.032982`, mae `0.06614`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.001022`, median `0.003538`, mae `0.014036`
- 5d: sample `60`, hit `0.7`, avg `0.005339`, median `0.005327`, mae `0.014456`
- 10d: sample `60`, hit `0.55`, avg `0.003134`, median `0.005616`, mae `0.021665`
- 20d: sample `60`, hit `0.6833`, avg `0.007017`, median `0.013823`, mae `0.034701`
- 60d: sample `60`, hit `0.5333`, avg `0.015747`, median `0.030553`, mae `0.060286`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002115`, median `0.004569`, mae `0.015016`
- 5d: sample `80`, hit `0.675`, avg `0.004715`, median `0.005327`, mae `0.016826`
- 10d: sample `80`, hit `0.5625`, avg `0.004354`, median `0.007467`, mae `0.025416`
- 20d: sample `80`, hit `0.675`, avg `0.009246`, median `0.013823`, mae `0.040701`
- 60d: sample `80`, hit `0.5625`, avg `0.02527`, median `0.032982`, mae `0.06614`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.001022`, median `0.003538`, mae `0.014036`
- 5d: sample `60`, hit `0.7`, avg `0.005339`, median `0.005327`, mae `0.014456`
- 10d: sample `60`, hit `0.55`, avg `0.003134`, median `0.005616`, mae `0.021665`
- 20d: sample `60`, hit `0.6833`, avg `0.007017`, median `0.013823`, mae `0.034701`
- 60d: sample `60`, hit `0.5333`, avg `0.015747`, median `0.030553`, mae `0.060286`

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
