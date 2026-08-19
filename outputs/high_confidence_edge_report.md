# High Confidence Edge Report

Generated at: `2026-08-19T02:35:21.871514+00:00`

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
- 3d: sample `20`, hit `0.7`, avg `0.008118`, median `0.01297`, mae `0.013282`
- 5d: sample `20`, hit `0.8`, avg `0.008722`, median `0.010593`, mae `0.017514`
- 10d: sample `20`, hit `0.7`, avg `0.010894`, median `0.019861`, mae `0.030659`
- 20d: sample `20`, hit `0.7`, avg `0.007486`, median `0.025784`, mae `0.05197`
- 60d: sample `20`, hit `0.65`, avg `0.023778`, median `0.056189`, mae `0.102409`

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
- 3d: sample `2`, hit `0.5`, avg `0.00246`, median `0.005642`, mae `0.003182`
- 5d: sample `2`, hit `0.5`, avg `0.004634`, median `0.010593`, mae `0.005959`
- 10d: sample `2`, hit `1.0`, avg `0.016892`, median `0.024755`, mae `0.016892`
- 20d: sample `2`, hit `0.5`, avg `-0.000888`, median `0.041566`, mae `0.042454`
- 60d: sample `2`, hit `0.5`, avg `-0.014766`, median `0.056189`, mae `0.070955`

### confidence_score top 10%
- sample_size: `2`
- 3d: sample `2`, hit `0.5`, avg `0.00246`, median `0.005642`, mae `0.003182`
- 5d: sample `2`, hit `0.5`, avg `0.004634`, median `0.010593`, mae `0.005959`
- 10d: sample `2`, hit `1.0`, avg `0.016892`, median `0.024755`, mae `0.016892`
- 20d: sample `2`, hit `0.5`, avg `-0.000888`, median `0.041566`, mae `0.042454`
- 60d: sample `2`, hit `0.5`, avg `-0.014766`, median `0.056189`, mae `0.070955`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.008118, 'median_return': 0.01297, 'mean_absolute_return': 0.013282, 'max_adverse_excursion': -0.017989, 'max_favorable_excursion': 0.028964}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.008722, 'median_return': 0.010593, 'mean_absolute_return': 0.017514, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.010894, 'median_return': 0.019861, 'mean_absolute_return': 0.030659, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.007486, 'median_return': 0.025784, 'mean_absolute_return': 0.05197, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.023778, 'median_return': 0.056189, 'mean_absolute_return': 0.102409, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'confidence_top_10': {'sample_size': 2, 'by_horizon': {'3d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': 0.00246, 'median_return': 0.005642, 'mean_absolute_return': 0.003182, 'max_adverse_excursion': -0.000722, 'max_favorable_excursion': 0.005642}, '5d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': 0.004634, 'median_return': 0.010593, 'mean_absolute_return': 0.005959, 'max_adverse_excursion': -0.001324, 'max_favorable_excursion': 0.010593}, '10d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.016892, 'median_return': 0.024755, 'mean_absolute_return': 0.016892, 'max_adverse_excursion': 0.00903, 'max_favorable_excursion': 0.024755}, '20d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': -0.000888, 'median_return': 0.041566, 'mean_absolute_return': 0.042454, 'max_adverse_excursion': -0.043342, 'max_favorable_excursion': 0.041566}, '60d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': -0.014766, 'median_return': 0.056189, 'mean_absolute_return': 0.070955, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.056189}}}, 'ordinary_confidence': {'sample_size': 18, 'by_horizon': {'3d': {'sample_size': 18, 'hit_rate': 0.7222, 'avg_return': 0.008746, 'median_return': 0.013042, 'mean_absolute_return': 0.014404, 'max_adverse_excursion': -0.017989, 'max_favorable_excursion': 0.028964}, '5d': {'sample_size': 18, 'hit_rate': 0.8333, 'avg_return': 0.009177, 'median_return': 0.018277, 'mean_absolute_return': 0.018798, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 18, 'hit_rate': 0.6667, 'avg_return': 0.010228, 'median_return': 0.019861, 'mean_absolute_return': 0.032188, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 18, 'hit_rate': 0.7222, 'avg_return': 0.008417, 'median_return': 0.025784, 'mean_absolute_return': 0.053027, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 18, 'hit_rate': 0.6667, 'avg_return': 0.02806, 'median_return': 0.064286, 'mean_absolute_return': 0.105903, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 20, 'hit_rate': 0.7}, '5d': {'sample_size': 20, 'hit_rate': 0.8}, '10d': {'sample_size': 20, 'hit_rate': 0.7}, '20d': {'sample_size': 20, 'hit_rate': 0.7}, '60d': {'sample_size': 20, 'hit_rate': 0.65}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 20, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.0, 'both_hit': 14, 'both_miss': 6}, '5d': {'sample_size': 20, 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': 0.0, 'both_hit': 16, 'both_miss': 4}, '10d': {'sample_size': 20, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.0, 'both_hit': 14, 'both_miss': 6}, '20d': {'sample_size': 20, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.0, 'both_hit': 14, 'both_miss': 6}, '60d': {'sample_size': 20, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 13, 'both_miss': 7}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.008118, 'median_return': 0.01297, 'mean_absolute_return': 0.013282, 'max_adverse_excursion': -0.017989, 'max_favorable_excursion': 0.028964}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.008722, 'median_return': 0.010593, 'mean_absolute_return': 0.017514, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.010894, 'median_return': 0.019861, 'mean_absolute_return': 0.030659, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.007486, 'median_return': 0.025784, 'mean_absolute_return': 0.05197, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.023778, 'median_return': 0.056189, 'mean_absolute_return': 0.102409, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008118`, median `0.01297`, mae `0.013282`
- 5d: sample `20`, hit `0.8`, avg `0.008722`, median `0.010593`, mae `0.017514`
- 10d: sample `20`, hit `0.7`, avg `0.010894`, median `0.019861`, mae `0.030659`
- 20d: sample `20`, hit `0.7`, avg `0.007486`, median `0.025784`, mae `0.05197`
- 60d: sample `20`, hit `0.65`, avg `0.023778`, median `0.056189`, mae `0.102409`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008118`, median `0.01297`, mae `0.013282`
- 5d: sample `20`, hit `0.8`, avg `0.008722`, median `0.010593`, mae `0.017514`
- 10d: sample `20`, hit `0.7`, avg `0.010894`, median `0.019861`, mae `0.030659`
- 20d: sample `20`, hit `0.7`, avg `0.007486`, median `0.025784`, mae `0.05197`
- 60d: sample `20`, hit `0.65`, avg `0.023778`, median `0.056189`, mae `0.102409`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008118`, median `0.01297`, mae `0.013282`
- 5d: sample `20`, hit `0.8`, avg `0.008722`, median `0.010593`, mae `0.017514`
- 10d: sample `20`, hit `0.7`, avg `0.010894`, median `0.019861`, mae `0.030659`
- 20d: sample `20`, hit `0.7`, avg `0.007486`, median `0.025784`, mae `0.05197`
- 60d: sample `20`, hit `0.65`, avg `0.023778`, median `0.056189`, mae `0.102409`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008118`, median `0.01297`, mae `0.013282`
- 5d: sample `20`, hit `0.8`, avg `0.008722`, median `0.010593`, mae `0.017514`
- 10d: sample `20`, hit `0.7`, avg `0.010894`, median `0.019861`, mae `0.030659`
- 20d: sample `20`, hit `0.7`, avg `0.007486`, median `0.025784`, mae `0.05197`
- 60d: sample `20`, hit `0.65`, avg `0.023778`, median `0.056189`, mae `0.102409`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008118`, median `0.01297`, mae `0.013282`
- 5d: sample `20`, hit `0.8`, avg `0.008722`, median `0.010593`, mae `0.017514`
- 10d: sample `20`, hit `0.7`, avg `0.010894`, median `0.019861`, mae `0.030659`
- 20d: sample `20`, hit `0.7`, avg `0.007486`, median `0.025784`, mae `0.05197`
- 60d: sample `20`, hit `0.65`, avg `0.023778`, median `0.056189`, mae `0.102409`

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
