# High Confidence Edge Report

Generated at: `2026-08-14T23:33:55.141294+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `20`
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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

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
- sample_size: `2`
- 3d: sample `2`, hit `1.0`, avg `0.008028`, median `0.011487`, mae `0.008028`
- 5d: sample `2`, hit `1.0`, avg `0.014749`, median `0.022174`, mae `0.014749`
- 10d: sample `2`, hit `1.0`, avg `0.019931`, median `0.02016`, mae `0.019931`
- 20d: sample `2`, hit `0.0`, avg `-0.018402`, median `-0.015267`, mae `0.018402`
- 60d: sample `2`, hit `0.0`, avg `-0.039821`, median `-0.03635`, mae `0.039821`

### confidence_score top 10%
- sample_size: `2`
- 3d: sample `2`, hit `1.0`, avg `0.008028`, median `0.011487`, mae `0.008028`
- 5d: sample `2`, hit `1.0`, avg `0.014749`, median `0.022174`, mae `0.014749`
- 10d: sample `2`, hit `1.0`, avg `0.019931`, median `0.02016`, mae `0.019931`
- 20d: sample `2`, hit `0.0`, avg `-0.018402`, median `-0.015267`, mae `0.018402`
- 60d: sample `2`, hit `0.0`, avg `-0.039821`, median `-0.03635`, mae `0.039821`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.003311, 'median_return': 0.000145, 'mean_absolute_return': 0.009605, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.002904, 'median_return': 0.005084, 'mean_absolute_return': 0.010294, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.000463, 'median_return': -0.000214, 'mean_absolute_return': 0.015062, 'max_adverse_excursion': -0.030947, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.00291, 'median_return': 0.012291, 'mean_absolute_return': 0.026751, 'max_adverse_excursion': -0.080367, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.004822, 'median_return': -0.01711, 'mean_absolute_return': 0.0492, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.096597}}}, 'confidence_top_10': {'sample_size': 2, 'by_horizon': {'3d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.008028, 'median_return': 0.011487, 'mean_absolute_return': 0.008028, 'max_adverse_excursion': 0.004569, 'max_favorable_excursion': 0.011487}, '5d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.014749, 'median_return': 0.022174, 'mean_absolute_return': 0.014749, 'max_adverse_excursion': 0.007324, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.019931, 'median_return': 0.02016, 'mean_absolute_return': 0.019931, 'max_adverse_excursion': 0.019702, 'max_favorable_excursion': 0.02016}, '20d': {'sample_size': 2, 'hit_rate': 0.0, 'avg_return': -0.018402, 'median_return': -0.015267, 'mean_absolute_return': 0.018402, 'max_adverse_excursion': -0.021537, 'max_favorable_excursion': -0.015267}, '60d': {'sample_size': 2, 'hit_rate': 0.0, 'avg_return': -0.039821, 'median_return': -0.03635, 'mean_absolute_return': 0.039821, 'max_adverse_excursion': -0.043292, 'max_favorable_excursion': -0.03635}}}, 'ordinary_confidence': {'sample_size': 18, 'by_horizon': {'3d': {'sample_size': 18, 'hit_rate': 0.4444, 'avg_return': -0.004571, 'median_return': -0.001166, 'mean_absolute_return': 0.00978, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 18, 'hit_rate': 0.7222, 'avg_return': 0.001588, 'median_return': 0.004606, 'mean_absolute_return': 0.009799, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.019686}, '10d': {'sample_size': 18, 'hit_rate': 0.3889, 'avg_return': -0.0017, 'median_return': -0.001676, 'mean_absolute_return': 0.014521, 'max_adverse_excursion': -0.030947, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 18, 'hit_rate': 0.6667, 'avg_return': -0.001189, 'median_return': 0.013178, 'mean_absolute_return': 0.027678, 'max_adverse_excursion': -0.080367, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 18, 'hit_rate': 0.4444, 'avg_return': -0.000933, 'median_return': -0.003049, 'mean_absolute_return': 0.050243, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.096597}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 20, 'hit_rate': 0.5}, '5d': {'sample_size': 20, 'hit_rate': 0.75}, '10d': {'sample_size': 20, 'hit_rate': 0.45}, '20d': {'sample_size': 20, 'hit_rate': 0.6}, '60d': {'sample_size': 20, 'hit_rate': 0.4}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 20, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 10, 'both_miss': 10}, '5d': {'sample_size': 20, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': 0.0, 'both_hit': 15, 'both_miss': 5}, '10d': {'sample_size': 20, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.0, 'both_hit': 9, 'both_miss': 11}, '20d': {'sample_size': 20, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 12, 'both_miss': 8}, '60d': {'sample_size': 20, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.0, 'both_hit': 8, 'both_miss': 12}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.003311, 'median_return': 0.000145, 'mean_absolute_return': 0.009605, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.002904, 'median_return': 0.005084, 'mean_absolute_return': 0.010294, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.000463, 'median_return': -0.000214, 'mean_absolute_return': 0.015062, 'max_adverse_excursion': -0.030947, 'max_favorable_excursion': 0.023034}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.00291, 'median_return': 0.012291, 'mean_absolute_return': 0.026751, 'max_adverse_excursion': -0.080367, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.004822, 'median_return': -0.01711, 'mean_absolute_return': 0.0492, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.096597}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

### mixed_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003311`, median `0.000145`, mae `0.009605`
- 5d: sample `20`, hit `0.75`, avg `0.002904`, median `0.005084`, mae `0.010294`
- 10d: sample `20`, hit `0.45`, avg `0.000463`, median `-0.000214`, mae `0.015062`
- 20d: sample `20`, hit `0.6`, avg `-0.00291`, median `0.012291`, mae `0.026751`
- 60d: sample `20`, hit `0.4`, avg `-0.004822`, median `-0.01711`, mae `0.0492`

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
