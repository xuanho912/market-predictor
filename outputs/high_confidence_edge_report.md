# High Confidence Edge Report

Generated at: `2026-09-12T15:34:46.781857+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `12`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `12`, gate `insufficient`
- 5d: completed `12`, gate `insufficient`
- 10d: completed `12`, gate `insufficient`
- 20d: completed `12`, gate `insufficient`
- 60d: completed `12`, gate `insufficient`

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
- 3d: sample `80`, hit `0.5625`, avg `-0.002009`, median `0.00099`, mae `0.014541`
- 5d: sample `80`, hit `0.5`, avg `-0.004909`, median `0.000688`, mae `0.017964`
- 10d: sample `80`, hit `0.3875`, avg `-0.004386`, median `-0.007491`, mae `0.02632`
- 20d: sample `80`, hit `0.55`, avg `0.002905`, median `0.007672`, mae `0.04189`
- 60d: sample `80`, hit `0.6`, avg `0.015041`, median `0.043615`, mae `0.089148`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006324`, median `0.00234`, mae `0.013891`
- 5d: sample `8`, hit `0.5`, avg `-0.011979`, median `0.003005`, mae `0.018901`
- 10d: sample `8`, hit `0.25`, avg `-0.003551`, median `-0.006017`, mae `0.017333`
- 20d: sample `8`, hit `0.875`, avg `0.027332`, median `0.033999`, mae `0.041158`
- 60d: sample `8`, hit `0.875`, avg `0.068599`, median `0.101282`, mae `0.082817`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006324`, median `0.00234`, mae `0.013891`
- 5d: sample `8`, hit `0.5`, avg `-0.011979`, median `0.003005`, mae `0.018901`
- 10d: sample `8`, hit `0.25`, avg `-0.003551`, median `-0.006017`, mae `0.017333`
- 20d: sample `8`, hit `0.875`, avg `0.027332`, median `0.033999`, mae `0.041158`
- 60d: sample `8`, hit `0.875`, avg `0.068599`, median `0.101282`, mae `0.082817`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006324, 'median_return': 0.00234, 'mean_absolute_return': 0.013891, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.011979, 'median_return': 0.003005, 'mean_absolute_return': 0.018901, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.003551, 'median_return': -0.006017, 'mean_absolute_return': 0.017333, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.027332, 'median_return': 0.033999, 'mean_absolute_return': 0.041158, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.068599, 'median_return': 0.101282, 'mean_absolute_return': 0.082817, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': -0.001529, 'median_return': 0.00099, 'mean_absolute_return': 0.014613, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.004123, 'median_return': 0.000688, 'mean_absolute_return': 0.01786, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.004479, 'median_return': -0.007755, 'mean_absolute_return': 0.027318, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.000191, 'median_return': 0.002095, 'mean_absolute_return': 0.041971, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.00909, 'median_return': 0.037425, 'mean_absolute_return': 0.089851, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.4}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.002411, 'median_return': 0.006513, 'mean_absolute_return': 0.018005, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.004852, 'median_return': 0.000935, 'mean_absolute_return': 0.020242, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.005478, 'median_return': -0.0004, 'mean_absolute_return': 0.023898, 'max_adverse_excursion': -0.044039, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.024201, 'median_return': 0.029166, 'mean_absolute_return': 0.036887, 'max_adverse_excursion': -0.056353, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.044324, 'median_return': 0.064104, 'mean_absolute_return': 0.085269, 'max_adverse_excursion': -0.12745, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.001606, 'median_return': 0.000616, 'mean_absolute_return': 0.011076, 'max_adverse_excursion': -0.034534, 'max_favorable_excursion': 0.022454}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.004965, 'median_return': 0.000688, 'mean_absolute_return': 0.015687, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.038591}, '10d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.01425, 'median_return': -0.01977, 'mean_absolute_return': 0.028741, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.049674}, '20d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.018391, 'median_return': -0.003522, 'mean_absolute_return': 0.046892, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.067188}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.014243, 'median_return': 0.019812, 'mean_absolute_return': 0.093026, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.116367}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `-0.002009`, median `0.00099`, mae `0.014541`
- 5d: sample `80`, hit `0.5`, avg `-0.004909`, median `0.000688`, mae `0.017964`
- 10d: sample `80`, hit `0.3875`, avg `-0.004386`, median `-0.007491`, mae `0.02632`
- 20d: sample `80`, hit `0.55`, avg `0.002905`, median `0.007672`, mae `0.04189`
- 60d: sample `80`, hit `0.6`, avg `0.015041`, median `0.043615`, mae `0.089148`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00468`, median `0.010664`, mae `0.017336`
- 5d: sample `20`, hit `0.6`, avg `0.004265`, median `0.008593`, mae `0.019576`
- 10d: sample `20`, hit `0.65`, avg `0.016686`, median `0.017789`, mae `0.030954`
- 20d: sample `20`, hit `0.8`, avg `0.030581`, median `0.033791`, mae `0.039786`
- 60d: sample `20`, hit `0.75`, avg `0.04655`, median `0.069439`, mae `0.097686`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `-0.002009`, median `0.00099`, mae `0.014541`
- 5d: sample `80`, hit `0.5`, avg `-0.004909`, median `0.000688`, mae `0.017964`
- 10d: sample `80`, hit `0.3875`, avg `-0.004386`, median `-0.007491`, mae `0.02632`
- 20d: sample `80`, hit `0.55`, avg `0.002905`, median `0.007672`, mae `0.04189`
- 60d: sample `80`, hit `0.6`, avg `0.015041`, median `0.043615`, mae `0.089148`

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
- 3d: sample `80`, hit `0.5625`, avg `-0.002009`, median `0.00099`, mae `0.014541`
- 5d: sample `80`, hit `0.5`, avg `-0.004909`, median `0.000688`, mae `0.017964`
- 10d: sample `80`, hit `0.3875`, avg `-0.004386`, median `-0.007491`, mae `0.02632`
- 20d: sample `80`, hit `0.55`, avg `0.002905`, median `0.007672`, mae `0.04189`
- 60d: sample `80`, hit `0.6`, avg `0.015041`, median `0.043615`, mae `0.089148`

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
