# High Confidence Edge Report

Generated at: `2026-06-15T13:55:23.103830+00:00`

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
- 3d: sample `80`, hit `0.6125`, avg `0.003619`, median `0.004569`, mae `0.013223`
- 5d: sample `80`, hit `0.6125`, avg `0.004389`, median `0.004655`, mae `0.016901`
- 10d: sample `80`, hit `0.5875`, avg `0.006657`, median `0.007467`, mae `0.022654`
- 20d: sample `80`, hit `0.6875`, avg `0.009317`, median `0.017608`, mae `0.035892`
- 60d: sample `80`, hit `0.5875`, avg `0.025805`, median `0.03283`, mae `0.060677`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.003619, 'median_return': 0.004569, 'mean_absolute_return': 0.013223, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.004389, 'median_return': 0.004655, 'mean_absolute_return': 0.016901, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.006657, 'median_return': 0.007467, 'mean_absolute_return': 0.022654, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.009317, 'median_return': 0.017608, 'mean_absolute_return': 0.035892, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.025805, 'median_return': 0.03283, 'mean_absolute_return': 0.060677, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007791, 'median_return': -0.001811, 'mean_absolute_return': 0.013454, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011833, 'median_return': -0.012956, 'mean_absolute_return': 0.017829, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008706, 'median_return': 0.0076, 'mean_absolute_return': 0.014887, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.028852, 'median_return': 0.031196, 'mean_absolute_return': 0.028852, 'max_adverse_excursion': 0.012958, 'max_favorable_excursion': 0.037283}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.054535, 'median_return': 0.065295, 'mean_absolute_return': 0.059567, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.004886, 'median_return': 0.005458, 'mean_absolute_return': 0.013198, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.006191, 'median_return': 0.005876, 'mean_absolute_return': 0.016798, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.006429, 'median_return': 0.007467, 'mean_absolute_return': 0.023517, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007147, 'median_return': 0.016109, 'mean_absolute_return': 0.036674, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.022613, 'median_return': 0.026139, 'mean_absolute_return': 0.060801, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': 0.0, 'both_hit': 55, 'both_miss': 25}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.003619, 'median_return': 0.004569, 'mean_absolute_return': 0.013223, 'max_adverse_excursion': -0.03197, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.004389, 'median_return': 0.004655, 'mean_absolute_return': 0.016901, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.056069}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.006657, 'median_return': 0.007467, 'mean_absolute_return': 0.022654, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.071017}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.009317, 'median_return': 0.017608, 'mean_absolute_return': 0.035892, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.105374}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.025805, 'median_return': 0.03283, 'mean_absolute_return': 0.060677, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.183622}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003619`, median `0.004569`, mae `0.013223`
- 5d: sample `80`, hit `0.6125`, avg `0.004389`, median `0.004655`, mae `0.016901`
- 10d: sample `80`, hit `0.5875`, avg `0.006657`, median `0.007467`, mae `0.022654`
- 20d: sample `80`, hit `0.6875`, avg `0.009317`, median `0.017608`, mae `0.035892`
- 60d: sample `80`, hit `0.5875`, avg `0.025805`, median `0.03283`, mae `0.060677`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003619`, median `0.004569`, mae `0.013223`
- 5d: sample `80`, hit `0.6125`, avg `0.004389`, median `0.004655`, mae `0.016901`
- 10d: sample `80`, hit `0.5875`, avg `0.006657`, median `0.007467`, mae `0.022654`
- 20d: sample `80`, hit `0.6875`, avg `0.009317`, median `0.017608`, mae `0.035892`
- 60d: sample `80`, hit `0.5875`, avg `0.025805`, median `0.03283`, mae `0.060677`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001621`, median `0.003952`, mae `0.012671`
- 5d: sample `40`, hit `0.475`, avg `0.000407`, median `-0.001324`, mae `0.016329`
- 10d: sample `40`, hit `0.525`, avg `0.006965`, median `0.006235`, mae `0.021405`
- 20d: sample `40`, hit `0.7`, avg `0.017004`, median `0.020431`, mae `0.034592`
- 60d: sample `40`, hit `0.7`, avg `0.043304`, median `0.052998`, mae `0.069086`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003619`, median `0.004569`, mae `0.013223`
- 5d: sample `80`, hit `0.6125`, avg `0.004389`, median `0.004655`, mae `0.016901`
- 10d: sample `80`, hit `0.5875`, avg `0.006657`, median `0.007467`, mae `0.022654`
- 20d: sample `80`, hit `0.6875`, avg `0.009317`, median `0.017608`, mae `0.035892`
- 60d: sample `80`, hit `0.5875`, avg `0.025805`, median `0.03283`, mae `0.060677`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001621`, median `0.003952`, mae `0.012671`
- 5d: sample `40`, hit `0.475`, avg `0.000407`, median `-0.001324`, mae `0.016329`
- 10d: sample `40`, hit `0.525`, avg `0.006965`, median `0.006235`, mae `0.021405`
- 20d: sample `40`, hit `0.7`, avg `0.017004`, median `0.020431`, mae `0.034592`
- 60d: sample `40`, hit `0.7`, avg `0.043304`, median `0.052998`, mae `0.069086`

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
- 3d: sample `40`, hit `0.525`, avg `0.000304`, median `0.001558`, mae `0.013244`
- 5d: sample `40`, hit `0.525`, avg `-0.000905`, median `0.000579`, mae `0.015366`
- 10d: sample `40`, hit `0.6`, avg `0.006569`, median `0.007467`, mae `0.016134`
- 20d: sample `40`, hit `0.825`, avg `0.017433`, median `0.022652`, mae `0.028067`
- 60d: sample `40`, hit `0.575`, avg `0.01777`, median `0.029917`, mae `0.056597`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.006934`, median `0.008337`, mae `0.013203`
- 5d: sample `40`, hit `0.7`, avg `0.009682`, median `0.008121`, mae `0.018436`
- 10d: sample `40`, hit `0.575`, avg `0.006745`, median `0.00903`, mae `0.029173`
- 20d: sample `40`, hit `0.55`, avg `0.001201`, median `0.004543`, mae `0.043716`
- 60d: sample `40`, hit `0.6`, avg `0.033841`, median `0.047759`, mae `0.064758`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000304`, median `0.001558`, mae `0.013244`
- 5d: sample `40`, hit `0.525`, avg `-0.000905`, median `0.000579`, mae `0.015366`
- 10d: sample `40`, hit `0.6`, avg `0.006569`, median `0.007467`, mae `0.016134`
- 20d: sample `40`, hit `0.825`, avg `0.017433`, median `0.022652`, mae `0.028067`
- 60d: sample `40`, hit `0.575`, avg `0.01777`, median `0.029917`, mae `0.056597`

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
- 3d: sample `80`, hit `0.6125`, avg `0.003619`, median `0.004569`, mae `0.013223`
- 5d: sample `80`, hit `0.6125`, avg `0.004389`, median `0.004655`, mae `0.016901`
- 10d: sample `80`, hit `0.5875`, avg `0.006657`, median `0.007467`, mae `0.022654`
- 20d: sample `80`, hit `0.6875`, avg `0.009317`, median `0.017608`, mae `0.035892`
- 60d: sample `80`, hit `0.5875`, avg `0.025805`, median `0.03283`, mae `0.060677`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003619`, median `0.004569`, mae `0.013223`
- 5d: sample `80`, hit `0.6125`, avg `0.004389`, median `0.004655`, mae `0.016901`
- 10d: sample `80`, hit `0.5875`, avg `0.006657`, median `0.007467`, mae `0.022654`
- 20d: sample `80`, hit `0.6875`, avg `0.009317`, median `0.017608`, mae `0.035892`
- 60d: sample `80`, hit `0.5875`, avg `0.025805`, median `0.03283`, mae `0.060677`

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
