# High Confidence Edge Report

Generated at: `2026-06-15T15:20:52.567547+00:00`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004789`, median `0.005458`, mae `0.013899`
- 5d: sample `80`, hit `0.6375`, avg `0.005953`, median `0.005327`, mae `0.017399`
- 10d: sample `80`, hit `0.625`, avg `0.008715`, median `0.00903`, mae `0.022165`
- 20d: sample `80`, hit `0.7125`, avg `0.009907`, median `0.017881`, mae `0.035735`
- 60d: sample `80`, hit `0.6`, avg `0.02784`, median `0.032982`, mae `0.062543`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006411`, median `0.001558`, mae `0.014382`
- 5d: sample `8`, hit `0.25`, avg `-0.007563`, median `-0.007788`, mae `0.017861`
- 10d: sample `8`, hit `0.75`, avg `0.008453`, median `0.0076`, mae `0.014633`
- 20d: sample `8`, hit `0.875`, avg `0.023947`, median `0.029166`, mae `0.025842`
- 60d: sample `8`, hit `0.75`, avg `0.037866`, median `0.046132`, mae `0.052474`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006411`, median `0.001558`, mae `0.014382`
- 5d: sample `8`, hit `0.25`, avg `-0.007563`, median `-0.007788`, mae `0.017861`
- 10d: sample `8`, hit `0.75`, avg `0.008453`, median `0.0076`, mae `0.014633`
- 20d: sample `8`, hit `0.875`, avg `0.023947`, median `0.029166`, mae `0.025842`
- 60d: sample `8`, hit `0.75`, avg `0.037866`, median `0.046132`, mae `0.052474`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004789, 'median_return': 0.005458, 'mean_absolute_return': 0.013899, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.005953, 'median_return': 0.005327, 'mean_absolute_return': 0.017399, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.008715, 'median_return': 0.00903, 'mean_absolute_return': 0.022165, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.009907, 'median_return': 0.017881, 'mean_absolute_return': 0.035735, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.02784, 'median_return': 0.032982, 'mean_absolute_return': 0.062543, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006411, 'median_return': 0.001558, 'mean_absolute_return': 0.014382, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.007563, 'median_return': -0.007788, 'mean_absolute_return': 0.017861, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008453, 'median_return': 0.0076, 'mean_absolute_return': 0.014633, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.023947, 'median_return': 0.029166, 'mean_absolute_return': 0.025842, 'max_adverse_excursion': -0.007581, 'max_favorable_excursion': 0.037283}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.037866, 'median_return': 0.046132, 'mean_absolute_return': 0.052474, 'max_adverse_excursion': -0.038302, 'max_favorable_excursion': 0.094627}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.006033, 'median_return': 0.006228, 'mean_absolute_return': 0.013845, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.007454, 'median_return': 0.00596, 'mean_absolute_return': 0.017348, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.008744, 'median_return': 0.009675, 'mean_absolute_return': 0.023002, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.008347, 'median_return': 0.016175, 'mean_absolute_return': 0.036834, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.026726, 'median_return': 0.032982, 'mean_absolute_return': 0.063662, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.625}, '20d': {'sample_size': 80, 'hit_rate': 0.7125}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': 0.0, 'both_hit': 57, 'both_miss': 23}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004789, 'median_return': 0.005458, 'mean_absolute_return': 0.013899, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.005953, 'median_return': 0.005327, 'mean_absolute_return': 0.017399, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.008715, 'median_return': 0.00903, 'mean_absolute_return': 0.022165, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.009907, 'median_return': 0.017881, 'mean_absolute_return': 0.035735, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.02784, 'median_return': 0.032982, 'mean_absolute_return': 0.062543, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004789`, median `0.005458`, mae `0.013899`
- 5d: sample `80`, hit `0.6375`, avg `0.005953`, median `0.005327`, mae `0.017399`
- 10d: sample `80`, hit `0.625`, avg `0.008715`, median `0.00903`, mae `0.022165`
- 20d: sample `80`, hit `0.7125`, avg `0.009907`, median `0.017881`, mae `0.035735`
- 60d: sample `80`, hit `0.6`, avg `0.02784`, median `0.032982`, mae `0.062543`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004789`, median `0.005458`, mae `0.013899`
- 5d: sample `80`, hit `0.6375`, avg `0.005953`, median `0.005327`, mae `0.017399`
- 10d: sample `80`, hit `0.625`, avg `0.008715`, median `0.00903`, mae `0.022165`
- 20d: sample `80`, hit `0.7125`, avg `0.009907`, median `0.017881`, mae `0.035735`
- 60d: sample `80`, hit `0.6`, avg `0.02784`, median `0.032982`, mae `0.062543`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003223`, median `0.006228`, mae `0.014122`
- 5d: sample `40`, hit `0.5`, avg `0.002375`, median `0.000415`, mae `0.017973`
- 10d: sample `40`, hit `0.575`, avg `0.009437`, median `0.00903`, mae `0.021752`
- 20d: sample `40`, hit `0.725`, avg `0.017646`, median `0.022652`, mae `0.034361`
- 60d: sample `40`, hit `0.725`, avg `0.047744`, median `0.064286`, mae `0.072446`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004789`, median `0.005458`, mae `0.013899`
- 5d: sample `80`, hit `0.6375`, avg `0.005953`, median `0.005327`, mae `0.017399`
- 10d: sample `80`, hit `0.625`, avg `0.008715`, median `0.00903`, mae `0.022165`
- 20d: sample `80`, hit `0.7125`, avg `0.009907`, median `0.017881`, mae `0.035735`
- 60d: sample `80`, hit `0.6`, avg `0.02784`, median `0.032982`, mae `0.062543`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003223`, median `0.006228`, mae `0.014122`
- 5d: sample `40`, hit `0.5`, avg `0.002375`, median `0.000415`, mae `0.017973`
- 10d: sample `40`, hit `0.575`, avg `0.009437`, median `0.00903`, mae `0.021752`
- 20d: sample `40`, hit `0.725`, avg `0.017646`, median `0.022652`, mae `0.034361`
- 60d: sample `40`, hit `0.725`, avg `0.047744`, median `0.064286`, mae `0.072446`

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
- 3d: sample `40`, hit `0.525`, avg `0.000553`, median `0.001558`, mae `0.013494`
- 5d: sample `40`, hit `0.525`, avg `-0.000612`, median `0.000579`, mae `0.015658`
- 10d: sample `40`, hit `0.625`, avg `0.00739`, median `0.0076`, mae `0.016051`
- 20d: sample `40`, hit `0.825`, avg `0.018345`, median `0.02284`, mae `0.028979`
- 60d: sample `40`, hit `0.575`, avg `0.019441`, median `0.029917`, mae `0.058268`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.009025`, median `0.009928`, mae `0.014304`
- 5d: sample `40`, hit `0.75`, avg `0.012517`, median `0.01025`, mae `0.01914`
- 10d: sample `40`, hit `0.625`, avg `0.01004`, median `0.01246`, mae `0.028279`
- 20d: sample `40`, hit `0.6`, avg `0.001469`, median `0.009112`, mae `0.042492`
- 60d: sample `40`, hit `0.625`, avg `0.036239`, median `0.050225`, mae `0.066819`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000553`, median `0.001558`, mae `0.013494`
- 5d: sample `40`, hit `0.525`, avg `-0.000612`, median `0.000579`, mae `0.015658`
- 10d: sample `40`, hit `0.625`, avg `0.00739`, median `0.0076`, mae `0.016051`
- 20d: sample `40`, hit `0.825`, avg `0.018345`, median `0.02284`, mae `0.028979`
- 60d: sample `40`, hit `0.575`, avg `0.019441`, median `0.029917`, mae `0.058268`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004789`, median `0.005458`, mae `0.013899`
- 5d: sample `80`, hit `0.6375`, avg `0.005953`, median `0.005327`, mae `0.017399`
- 10d: sample `80`, hit `0.625`, avg `0.008715`, median `0.00903`, mae `0.022165`
- 20d: sample `80`, hit `0.7125`, avg `0.009907`, median `0.017881`, mae `0.035735`
- 60d: sample `80`, hit `0.6`, avg `0.02784`, median `0.032982`, mae `0.062543`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004789`, median `0.005458`, mae `0.013899`
- 5d: sample `80`, hit `0.6375`, avg `0.005953`, median `0.005327`, mae `0.017399`
- 10d: sample `80`, hit `0.625`, avg `0.008715`, median `0.00903`, mae `0.022165`
- 20d: sample `80`, hit `0.7125`, avg `0.009907`, median `0.017881`, mae `0.035735`
- 60d: sample `80`, hit `0.6`, avg `0.02784`, median `0.032982`, mae `0.062543`

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
