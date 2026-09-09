# High Confidence Edge Report

Generated at: `2026-09-09T23:30:56.099269+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `4`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `4`, gate `insufficient`
- 5d: completed `4`, gate `insufficient`
- 10d: completed `4`, gate `insufficient`
- 20d: completed `4`, gate `insufficient`
- 60d: completed `4`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.002258`, median `0.002329`, mae `0.013337`
- 5d: sample `80`, hit `0.625`, avg `0.003204`, median `0.003829`, mae `0.01635`
- 10d: sample `80`, hit `0.425`, avg `0.002289`, median `-0.00676`, mae `0.023706`
- 20d: sample `80`, hit `0.6625`, avg `0.013072`, median `0.02086`, mae `0.037657`
- 60d: sample `80`, hit `0.7375`, avg `0.04334`, median `0.059495`, mae `0.073132`

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
- 3d: sample `8`, hit `0.5`, avg `-0.0016`, median `0.001558`, mae `0.012858`
- 5d: sample `8`, hit `0.375`, avg `-0.007978`, median `-0.004438`, mae `0.011774`
- 10d: sample `8`, hit `0.5`, avg `0.004226`, median `0.0076`, mae `0.017872`
- 20d: sample `8`, hit `0.875`, avg `0.020874`, median `0.031196`, mae `0.029186`
- 60d: sample `8`, hit `0.875`, avg `0.059214`, median `0.085257`, mae `0.07309`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.0016`, median `0.001558`, mae `0.012858`
- 5d: sample `8`, hit `0.375`, avg `-0.007978`, median `-0.004438`, mae `0.011774`
- 10d: sample `8`, hit `0.5`, avg `0.004226`, median `0.0076`, mae `0.017872`
- 20d: sample `8`, hit `0.875`, avg `0.020874`, median `0.031196`, mae `0.029186`
- 60d: sample `8`, hit `0.875`, avg `0.059214`, median `0.085257`, mae `0.07309`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.0016, 'median_return': 0.001558, 'mean_absolute_return': 0.012858, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007978, 'median_return': -0.004438, 'mean_absolute_return': 0.011774, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004226, 'median_return': 0.0076, 'mean_absolute_return': 0.017872, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.020874, 'median_return': 0.031196, 'mean_absolute_return': 0.029186, 'max_adverse_excursion': -0.033249, 'max_favorable_excursion': 0.055822}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.059214, 'median_return': 0.085257, 'mean_absolute_return': 0.07309, 'max_adverse_excursion': -0.055503, 'max_favorable_excursion': 0.120808}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002686, 'median_return': 0.003785, 'mean_absolute_return': 0.01339, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.004446, 'median_return': 0.006452, 'mean_absolute_return': 0.016859, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': 0.002074, 'median_return': -0.007011, 'mean_absolute_return': 0.024354, 'max_adverse_excursion': -0.049389, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.012206, 'median_return': 0.020226, 'mean_absolute_return': 0.038598, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.041576, 'median_return': 0.057625, 'mean_absolute_return': 0.073136, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.425}, '5d': {'sample_size': 80, 'hit_rate': 0.375}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.3375}, '60d': {'sample_size': 80, 'hit_rate': 0.2625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.475, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.002258, 'median_return': 0.002329, 'mean_absolute_return': 0.013337, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.003204, 'median_return': 0.003829, 'mean_absolute_return': 0.01635, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': 0.002289, 'median_return': -0.00676, 'mean_absolute_return': 0.023706, 'max_adverse_excursion': -0.049389, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.013072, 'median_return': 0.02086, 'mean_absolute_return': 0.037657, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 80, 'hit_rate': 0.7375, 'avg_return': 0.04334, 'median_return': 0.059495, 'mean_absolute_return': 0.073132, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.001182`, median `-0.001641`, mae `0.008672`
- 5d: sample `20`, hit `0.6`, avg `-0.002159`, median `0.001303`, mae `0.010065`
- 10d: sample `20`, hit `0.3`, avg `-0.008195`, median `-0.01051`, mae `0.020678`
- 20d: sample `20`, hit `0.5`, avg `-0.008574`, median `0.007004`, mae `0.036227`
- 60d: sample `20`, hit `0.55`, avg `0.01961`, median `0.057625`, mae `0.060108`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.003404`, median `0.006714`, mae `0.014892`
- 5d: sample `60`, hit `0.6333`, avg `0.004991`, median `0.008039`, mae `0.018445`
- 10d: sample `60`, hit `0.4667`, avg `0.005783`, median `-0.001222`, mae `0.024715`
- 20d: sample `60`, hit `0.7167`, avg `0.020288`, median `0.029029`, mae `0.038134`
- 60d: sample `60`, hit `0.8`, avg `0.051249`, median `0.064104`, mae `0.077473`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.003404`, median `0.006714`, mae `0.014892`
- 5d: sample `60`, hit `0.6333`, avg `0.004991`, median `0.008039`, mae `0.018445`
- 10d: sample `60`, hit `0.4667`, avg `0.005783`, median `-0.001222`, mae `0.024715`
- 20d: sample `60`, hit `0.7167`, avg `0.020288`, median `0.029029`, mae `0.038134`
- 60d: sample `60`, hit `0.8`, avg `0.051249`, median `0.064104`, mae `0.077473`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.003404`, median `0.006714`, mae `0.014892`
- 5d: sample `60`, hit `0.6333`, avg `0.004991`, median `0.008039`, mae `0.018445`
- 10d: sample `60`, hit `0.4667`, avg `0.005783`, median `-0.001222`, mae `0.024715`
- 20d: sample `60`, hit `0.7167`, avg `0.020288`, median `0.029029`, mae `0.038134`
- 60d: sample `60`, hit `0.8`, avg `0.051249`, median `0.064104`, mae `0.077473`

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
- 3d: sample `80`, hit `0.575`, avg `0.002258`, median `0.002329`, mae `0.013337`
- 5d: sample `80`, hit `0.625`, avg `0.003204`, median `0.003829`, mae `0.01635`
- 10d: sample `80`, hit `0.425`, avg `0.002289`, median `-0.00676`, mae `0.023706`
- 20d: sample `80`, hit `0.6625`, avg `0.013072`, median `0.02086`, mae `0.037657`
- 60d: sample `80`, hit `0.7375`, avg `0.04334`, median `0.059495`, mae `0.073132`

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
