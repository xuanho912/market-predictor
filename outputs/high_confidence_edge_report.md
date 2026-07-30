# High Confidence Edge Report

Generated at: `2026-07-30T06:14:22.503354+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002009`, median `0.005296`, mae `0.016944`
- 5d: sample `80`, hit `0.6`, avg `0.003815`, median `0.003554`, mae `0.02247`
- 10d: sample `80`, hit `0.5625`, avg `0.007665`, median `0.010509`, mae `0.032364`
- 20d: sample `80`, hit `0.65`, avg `0.026051`, median `0.026005`, mae `0.048912`
- 60d: sample `80`, hit `0.6625`, avg `0.051898`, median `0.059948`, mae `0.085257`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004292`, median `0.007289`, mae `0.019723`
- 5d: sample `8`, hit `0.625`, avg `-0.009125`, median `0.002223`, mae `0.02178`
- 10d: sample `8`, hit `0.375`, avg `-0.000565`, median `-0.000336`, mae `0.020782`
- 20d: sample `8`, hit `0.5`, avg `0.015938`, median `0.006559`, mae `0.031568`
- 60d: sample `8`, hit `0.375`, avg `0.02124`, median `-0.019653`, mae `0.07061`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004292`, median `0.007289`, mae `0.019723`
- 5d: sample `8`, hit `0.625`, avg `-0.009125`, median `0.002223`, mae `0.02178`
- 10d: sample `8`, hit `0.375`, avg `-0.000565`, median `-0.000336`, mae `0.020782`
- 20d: sample `8`, hit `0.5`, avg `0.015938`, median `0.006559`, mae `0.031568`
- 60d: sample `8`, hit `0.375`, avg `0.02124`, median `-0.019653`, mae `0.07061`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004292, 'median_return': 0.007289, 'mean_absolute_return': 0.019723, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.009125, 'median_return': 0.002223, 'mean_absolute_return': 0.02178, 'max_adverse_excursion': -0.048238, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.000565, 'median_return': -0.000336, 'mean_absolute_return': 0.020782, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.015938, 'median_return': 0.006559, 'mean_absolute_return': 0.031568, 'max_adverse_excursion': -0.022761, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.02124, 'median_return': -0.019653, 'mean_absolute_return': 0.07061, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.124768}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.002709, 'median_return': 0.005296, 'mean_absolute_return': 0.016636, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.005253, 'median_return': 0.003829, 'mean_absolute_return': 0.022546, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.008579, 'median_return': 0.011031, 'mean_absolute_return': 0.033651, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.095798}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.027174, 'median_return': 0.026806, 'mean_absolute_return': 0.050839, 'max_adverse_excursion': -0.0919, 'max_favorable_excursion': 0.13778}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.055305, 'median_return': 0.060145, 'mean_absolute_return': 0.086885, 'max_adverse_excursion': -0.097363, 'max_favorable_excursion': 0.255401}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3625}, '5d': {'sample_size': 80, 'hit_rate': 0.4}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.3375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.000805, 'median_return': 0.003757, 'mean_absolute_return': 0.018739, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.004999, 'median_return': 0.002223, 'mean_absolute_return': 0.020741, 'max_adverse_excursion': -0.048238, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': 0.002309, 'median_return': -0.0004, 'mean_absolute_return': 0.018155, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.050818}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.015992, 'median_return': 0.006559, 'mean_absolute_return': 0.029469, 'max_adverse_excursion': -0.034684, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.037948, 'median_return': 0.048963, 'mean_absolute_return': 0.069545, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.002947, 'median_return': 0.00531, 'mean_absolute_return': 0.016346, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.006754, 'median_return': 0.004027, 'mean_absolute_return': 0.023046, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.00945, 'median_return': 0.017481, 'mean_absolute_return': 0.037101, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.095798}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.029403, 'median_return': 0.039296, 'mean_absolute_return': 0.055393, 'max_adverse_excursion': -0.0919, 'max_favorable_excursion': 0.13778}, '60d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.056548, 'median_return': 0.064934, 'mean_absolute_return': 0.090494, 'max_adverse_excursion': -0.097363, 'max_favorable_excursion': 0.255401}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.001629`, median `0.001405`, mae `0.014511`
- 5d: sample `40`, hit `0.575`, avg `-0.003778`, median `0.001303`, mae `0.015441`
- 10d: sample `40`, hit `0.425`, avg `-0.003009`, median `-0.001222`, mae `0.019977`
- 20d: sample `40`, hit `0.525`, avg `0.007946`, median `0.006559`, mae `0.031`
- 60d: sample `40`, hit `0.525`, avg `0.021756`, median `0.034496`, mae `0.061483`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.005647`, median `0.010008`, mae `0.019378`
- 5d: sample `40`, hit `0.625`, avg `0.011409`, median `0.014789`, mae `0.029498`
- 10d: sample `40`, hit `0.7`, avg `0.018339`, median `0.026124`, mae `0.044752`
- 20d: sample `40`, hit `0.775`, avg `0.044155`, median `0.060847`, mae `0.066824`
- 60d: sample `40`, hit `0.8`, avg `0.08204`, median `0.099631`, mae `0.109031`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000805`, median `0.003757`, mae `0.018739`
- 5d: sample `20`, hit `0.6`, avg `-0.004999`, median `0.002223`, mae `0.020741`
- 10d: sample `20`, hit `0.4`, avg `0.002309`, median `-0.0004`, mae `0.018155`
- 20d: sample `20`, hit `0.55`, avg `0.015992`, median `0.006559`, mae `0.029469`
- 60d: sample `20`, hit `0.6`, avg `0.037948`, median `0.048963`, mae `0.069545`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000805`, median `0.003757`, mae `0.018739`
- 5d: sample `20`, hit `0.6`, avg `-0.004999`, median `0.002223`, mae `0.020741`
- 10d: sample `20`, hit `0.4`, avg `0.002309`, median `-0.0004`, mae `0.018155`
- 20d: sample `20`, hit `0.55`, avg `0.015992`, median `0.006559`, mae `0.029469`
- 60d: sample `20`, hit `0.6`, avg `0.037948`, median `0.048963`, mae `0.069545`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.005647`, median `0.010008`, mae `0.019378`
- 5d: sample `40`, hit `0.625`, avg `0.011409`, median `0.014789`, mae `0.029498`
- 10d: sample `40`, hit `0.7`, avg `0.018339`, median `0.026124`, mae `0.044752`
- 20d: sample `40`, hit `0.775`, avg `0.044155`, median `0.060847`, mae `0.066824`
- 60d: sample `40`, hit `0.8`, avg `0.08204`, median `0.099631`, mae `0.109031`

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
- 3d: sample `80`, hit `0.6375`, avg `0.002009`, median `0.005296`, mae `0.016944`
- 5d: sample `80`, hit `0.6`, avg `0.003815`, median `0.003554`, mae `0.02247`
- 10d: sample `80`, hit `0.5625`, avg `0.007665`, median `0.010509`, mae `0.032364`
- 20d: sample `80`, hit `0.65`, avg `0.026051`, median `0.026005`, mae `0.048912`
- 60d: sample `80`, hit `0.6625`, avg `0.051898`, median `0.059948`, mae `0.085257`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002009`, median `0.005296`, mae `0.016944`
- 5d: sample `80`, hit `0.6`, avg `0.003815`, median `0.003554`, mae `0.02247`
- 10d: sample `80`, hit `0.5625`, avg `0.007665`, median `0.010509`, mae `0.032364`
- 20d: sample `80`, hit `0.65`, avg `0.026051`, median `0.026005`, mae `0.048912`
- 60d: sample `80`, hit `0.6625`, avg `0.051898`, median `0.059948`, mae `0.085257`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002009`, median `0.005296`, mae `0.016944`
- 5d: sample `80`, hit `0.6`, avg `0.003815`, median `0.003554`, mae `0.02247`
- 10d: sample `80`, hit `0.5625`, avg `0.007665`, median `0.010509`, mae `0.032364`
- 20d: sample `80`, hit `0.65`, avg `0.026051`, median `0.026005`, mae `0.048912`
- 60d: sample `80`, hit `0.6625`, avg `0.051898`, median `0.059948`, mae `0.085257`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002009`, median `0.005296`, mae `0.016944`
- 5d: sample `80`, hit `0.6`, avg `0.003815`, median `0.003554`, mae `0.02247`
- 10d: sample `80`, hit `0.5625`, avg `0.007665`, median `0.010509`, mae `0.032364`
- 20d: sample `80`, hit `0.65`, avg `0.026051`, median `0.026005`, mae `0.048912`
- 60d: sample `80`, hit `0.6625`, avg `0.051898`, median `0.059948`, mae `0.085257`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
