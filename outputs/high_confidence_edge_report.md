# High Confidence Edge Report

Generated at: `2026-07-17T14:06:23.268787+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.002278`, median `0.00234`, mae `0.014946`
- 5d: sample `40`, hit `0.55`, avg `-0.001476`, median `0.003005`, mae `0.017578`
- 10d: sample `40`, hit `0.325`, avg `-0.003803`, median `-0.011522`, mae `0.023998`
- 20d: sample `40`, hit `0.725`, avg `0.014709`, median `0.01983`, mae `0.033944`
- 60d: sample `40`, hit `0.7`, avg `0.039856`, median `0.070559`, mae `0.081922`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001009`, median `0.000603`, mae `0.010227`
- 5d: sample `40`, hit `0.575`, avg `0.000905`, median `0.002485`, mae `0.013682`
- 10d: sample `40`, hit `0.475`, avg `0.000126`, median `-0.002081`, mae `0.026087`
- 20d: sample `40`, hit `0.7`, avg `0.010364`, median `0.013402`, mae `0.033355`
- 60d: sample `40`, hit `0.525`, avg `0.024275`, median `0.043615`, mae `0.061434`

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
- 3d: sample `8`, hit `0.75`, avg `0.002832`, median `0.009937`, mae `0.01551`
- 5d: sample `8`, hit `0.5`, avg `-0.000744`, median `0.002453`, mae `0.01981`
- 10d: sample `8`, hit `0.25`, avg `-0.004297`, median `-0.013321`, mae `0.023421`
- 20d: sample `8`, hit `0.625`, avg `0.008811`, median `0.005003`, mae `0.02496`
- 60d: sample `8`, hit `0.625`, avg `0.027216`, median `0.099631`, mae `0.08318`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.002832`, median `0.009937`, mae `0.01551`
- 5d: sample `8`, hit `0.5`, avg `-0.000744`, median `0.002453`, mae `0.01981`
- 10d: sample `8`, hit `0.25`, avg `-0.004297`, median `-0.013321`, mae `0.023421`
- 20d: sample `8`, hit `0.625`, avg `0.008811`, median `0.005003`, mae `0.02496`
- 60d: sample `8`, hit `0.625`, avg `0.027216`, median `0.099631`, mae `0.08318`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.002278, 'median_return': 0.00234, 'mean_absolute_return': 0.014946, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.031673}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.001476, 'median_return': 0.003005, 'mean_absolute_return': 0.017578, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.003803, 'median_return': -0.011522, 'mean_absolute_return': 0.023998, 'max_adverse_excursion': -0.047759, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.014709, 'median_return': 0.01983, 'mean_absolute_return': 0.033944, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.039856, 'median_return': 0.070559, 'mean_absolute_return': 0.081922, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.1448}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.002832, 'median_return': 0.009937, 'mean_absolute_return': 0.01551, 'max_adverse_excursion': -0.037263, 'max_favorable_excursion': 0.022026}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000744, 'median_return': 0.002453, 'mean_absolute_return': 0.01981, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.004297, 'median_return': -0.013321, 'mean_absolute_return': 0.023421, 'max_adverse_excursion': -0.029192, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.008811, 'median_return': 0.005003, 'mean_absolute_return': 0.02496, 'max_adverse_excursion': -0.047767, 'max_favorable_excursion': 0.046529}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.027216, 'median_return': 0.099631, 'mean_absolute_return': 0.08318, 'max_adverse_excursion': -0.137725, 'max_favorable_excursion': 0.116132}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.002141, 'median_return': 0.000744, 'mean_absolute_return': 0.012262, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.031673}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': -0.000235, 'median_return': 0.002774, 'mean_absolute_return': 0.015165, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.001565, 'median_return': -0.007011, 'mean_absolute_return': 0.025223, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.059577}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.012951, 'median_return': 0.017149, 'mean_absolute_return': 0.034615, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.032604, 'median_return': 0.046132, 'mean_absolute_return': 0.0704, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': -0.001643, 'median_return': 0.001122, 'mean_absolute_return': 0.012586, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.031673}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': -0.000285, 'median_return': 0.002485, 'mean_absolute_return': 0.01563, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.001838, 'median_return': -0.007117, 'mean_absolute_return': 0.025043, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.012537, 'median_return': 0.014918, 'mean_absolute_return': 0.033649, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.032065, 'median_return': 0.046132, 'mean_absolute_return': 0.071678, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `-0.001643`, median `0.001122`, mae `0.012586`
- 5d: sample `80`, hit `0.5625`, avg `-0.000285`, median `0.002485`, mae `0.01563`
- 10d: sample `80`, hit `0.4`, avg `-0.001838`, median `-0.007117`, mae `0.025043`
- 20d: sample `80`, hit `0.7125`, avg `0.012537`, median `0.014918`, mae `0.033649`
- 60d: sample `80`, hit `0.6125`, avg `0.032065`, median `0.046132`, mae `0.071678`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001009`, median `0.000603`, mae `0.010227`
- 5d: sample `40`, hit `0.575`, avg `0.000905`, median `0.002485`, mae `0.013682`
- 10d: sample `40`, hit `0.475`, avg `0.000126`, median `-0.002081`, mae `0.026087`
- 20d: sample `40`, hit `0.7`, avg `0.010364`, median `0.013402`, mae `0.033355`
- 60d: sample `40`, hit `0.525`, avg `0.024275`, median `0.043615`, mae `0.061434`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.002278`, median `0.00234`, mae `0.014946`
- 5d: sample `40`, hit `0.55`, avg `-0.001476`, median `0.003005`, mae `0.017578`
- 10d: sample `40`, hit `0.325`, avg `-0.003803`, median `-0.011522`, mae `0.023998`
- 20d: sample `40`, hit `0.725`, avg `0.014709`, median `0.01983`, mae `0.033944`
- 60d: sample `40`, hit `0.7`, avg `0.039856`, median `0.070559`, mae `0.081922`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `-0.002572`, median `0.001122`, mae `0.013915`
- 5d: sample `60`, hit `0.5167`, avg `-0.0008`, median `0.002453`, mae `0.017312`
- 10d: sample `60`, hit `0.4167`, avg `0.000516`, median `-0.00367`, mae `0.02574`
- 20d: sample `60`, hit `0.7833`, avg `0.019926`, median `0.020068`, mae `0.033954`
- 60d: sample `60`, hit `0.6833`, avg `0.043201`, median `0.066114`, mae `0.077823`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003161`, median `-0.002441`, mae `0.011851`
- 5d: sample `20`, hit `0.45`, avg `0.000551`, median `-0.001324`, mae `0.01678`
- 10d: sample `20`, hit `0.6`, avg `0.009153`, median `0.013648`, mae `0.029224`
- 20d: sample `20`, hit `0.9`, avg `0.03036`, median `0.041262`, mae `0.033974`
- 60d: sample `20`, hit `0.65`, avg `0.04989`, median `0.066114`, mae `0.069625`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.002278`, median `0.00234`, mae `0.014946`
- 5d: sample `40`, hit `0.55`, avg `-0.001476`, median `0.003005`, mae `0.017578`
- 10d: sample `40`, hit `0.325`, avg `-0.003803`, median `-0.011522`, mae `0.023998`
- 20d: sample `40`, hit `0.725`, avg `0.014709`, median `0.01983`, mae `0.033944`
- 60d: sample `40`, hit `0.7`, avg `0.039856`, median `0.070559`, mae `0.081922`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `-0.002572`, median `0.001122`, mae `0.013915`
- 5d: sample `60`, hit `0.5167`, avg `-0.0008`, median `0.002453`, mae `0.017312`
- 10d: sample `60`, hit `0.4167`, avg `0.000516`, median `-0.00367`, mae `0.02574`
- 20d: sample `60`, hit `0.7833`, avg `0.019926`, median `0.020068`, mae `0.033954`
- 60d: sample `60`, hit `0.6833`, avg `0.043201`, median `0.066114`, mae `0.077823`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001009`, median `0.000603`, mae `0.010227`
- 5d: sample `40`, hit `0.575`, avg `0.000905`, median `0.002485`, mae `0.013682`
- 10d: sample `40`, hit `0.475`, avg `0.000126`, median `-0.002081`, mae `0.026087`
- 20d: sample `40`, hit `0.7`, avg `0.010364`, median `0.013402`, mae `0.033355`
- 60d: sample `40`, hit `0.525`, avg `0.024275`, median `0.043615`, mae `0.061434`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `-0.001137`, median `0.002067`, mae `0.012832`
- 5d: sample `60`, hit `0.6`, avg `-0.000564`, median `0.002786`, mae `0.015246`
- 10d: sample `60`, hit `0.3333`, avg `-0.005502`, median `-0.012383`, mae `0.023649`
- 20d: sample `60`, hit `0.65`, avg `0.006595`, median `0.012025`, mae `0.033541`
- 60d: sample `60`, hit `0.6`, avg `0.026123`, median `0.037425`, mae `0.072362`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.575`, avg `-0.001643`, median `0.001122`, mae `0.012586`
- 5d: sample `80`, hit `0.5625`, avg `-0.000285`, median `0.002485`, mae `0.01563`
- 10d: sample `80`, hit `0.4`, avg `-0.001838`, median `-0.007117`, mae `0.025043`
- 20d: sample `80`, hit `0.7125`, avg `0.012537`, median `0.014918`, mae `0.033649`
- 60d: sample `80`, hit `0.6125`, avg `0.032065`, median `0.046132`, mae `0.071678`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.002278`, median `0.00234`, mae `0.014946`
- 5d: sample `40`, hit `0.55`, avg `-0.001476`, median `0.003005`, mae `0.017578`
- 10d: sample `40`, hit `0.325`, avg `-0.003803`, median `-0.011522`, mae `0.023998`
- 20d: sample `40`, hit `0.725`, avg `0.014709`, median `0.01983`, mae `0.033944`
- 60d: sample `40`, hit `0.7`, avg `0.039856`, median `0.070559`, mae `0.081922`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001009`, median `0.000603`, mae `0.010227`
- 5d: sample `40`, hit `0.575`, avg `0.000905`, median `0.002485`, mae `0.013682`
- 10d: sample `40`, hit `0.475`, avg `0.000126`, median `-0.002081`, mae `0.026087`
- 20d: sample `40`, hit `0.7`, avg `0.010364`, median `0.013402`, mae `0.033355`
- 60d: sample `40`, hit `0.525`, avg `0.024275`, median `0.043615`, mae `0.061434`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
