# High Confidence Edge Report

Generated at: `2026-07-21T21:39:47.191471+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.010447`, median `-0.009383`, mae `0.018892`
- 5d: sample `20`, hit `0.35`, avg `-0.015121`, median `-0.016062`, mae `0.021837`
- 10d: sample `20`, hit `0.25`, avg `-0.005842`, median `-0.007011`, mae `0.015876`
- 20d: sample `20`, hit `0.65`, avg `0.013934`, median `0.026113`, mae `0.040487`
- 60d: sample `20`, hit `0.7`, avg `0.04197`, median `0.059495`, mae `0.078895`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.001445`, median `0.000616`, mae `0.01141`
- 5d: sample `60`, hit `0.4833`, avg `-0.000528`, median `-0.000371`, mae `0.013331`
- 10d: sample `60`, hit `0.4333`, avg `-0.003076`, median `-0.007491`, mae `0.026085`
- 20d: sample `60`, hit `0.6667`, avg `0.004681`, median `0.014918`, mae `0.038337`
- 60d: sample `60`, hit `0.5667`, avg `0.00898`, median `0.029164`, mae `0.079057`

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
- 3d: sample `8`, hit `0.375`, avg `-0.012643`, median `-0.001658`, mae `0.015853`
- 5d: sample `8`, hit `0.375`, avg `-0.016654`, median `-0.016062`, mae `0.02079`
- 10d: sample `8`, hit `0.125`, avg `-0.011849`, median `-0.007011`, mae `0.016657`
- 20d: sample `8`, hit `0.875`, avg `0.025786`, median `0.033999`, mae `0.039612`
- 60d: sample `8`, hit `0.875`, avg `0.065978`, median `0.099838`, mae `0.080196`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.012643`, median `-0.001658`, mae `0.015853`
- 5d: sample `8`, hit `0.375`, avg `-0.016654`, median `-0.016062`, mae `0.02079`
- 10d: sample `8`, hit `0.125`, avg `-0.011849`, median `-0.007011`, mae `0.016657`
- 20d: sample `8`, hit `0.875`, avg `0.025786`, median `0.033999`, mae `0.039612`
- 60d: sample `8`, hit `0.875`, avg `0.065978`, median `0.099838`, mae `0.080196`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010447, 'median_return': -0.009383, 'mean_absolute_return': 0.018892, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.015121, 'median_return': -0.016062, 'mean_absolute_return': 0.021837, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.005842, 'median_return': -0.007011, 'mean_absolute_return': 0.015876, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.013934, 'median_return': 0.026113, 'mean_absolute_return': 0.040487, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.04197, 'median_return': 0.059495, 'mean_absolute_return': 0.078895, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012643, 'median_return': -0.001658, 'mean_absolute_return': 0.015853, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.016654, 'median_return': -0.016062, 'mean_absolute_return': 0.02079, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011849, 'median_return': -0.007011, 'mean_absolute_return': 0.016657, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.025786, 'median_return': 0.033999, 'mean_absolute_return': 0.039612, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.065978, 'median_return': 0.099838, 'mean_absolute_return': 0.080196, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.002701, 'median_return': 0.000603, 'mean_absolute_return': 0.012994, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.00279, 'median_return': -0.001212, 'mean_absolute_return': 0.014865, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.002869, 'median_return': -0.007491, 'mean_absolute_return': 0.024297, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.004906, 'median_return': 0.014918, 'mean_absolute_return': 0.038792, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.076702}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.011811, 'median_return': 0.032982, 'mean_absolute_return': 0.078885, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.3375}, '60d': {'sample_size': 80, 'hit_rate': 0.4}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010447, 'median_return': -0.009383, 'mean_absolute_return': 0.018892, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.015121, 'median_return': -0.016062, 'mean_absolute_return': 0.021837, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.005842, 'median_return': -0.007011, 'mean_absolute_return': 0.015876, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.013934, 'median_return': 0.026113, 'mean_absolute_return': 0.040487, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.04197, 'median_return': 0.059495, 'mean_absolute_return': 0.078895, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.001445, 'median_return': 0.000616, 'mean_absolute_return': 0.01141, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.000528, 'median_return': -0.000371, 'mean_absolute_return': 0.013331, 'max_adverse_excursion': -0.035224, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.003076, 'median_return': -0.007491, 'mean_absolute_return': 0.026085, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.004681, 'median_return': 0.014918, 'mean_absolute_return': 0.038337, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.076702}, '60d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.00898, 'median_return': 0.029164, 'mean_absolute_return': 0.079057, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.005798`, median `-0.001428`, mae `0.014785`
- 5d: sample `40`, hit `0.475`, avg `-0.008455`, median `-0.001429`, mae `0.016981`
- 10d: sample `40`, hit `0.3`, avg `-0.006177`, median `-0.007755`, mae `0.017776`
- 20d: sample `40`, hit `0.55`, avg `0.005486`, median `0.01927`, mae `0.035949`
- 60d: sample `40`, hit `0.65`, avg `0.028506`, median `0.046132`, mae `0.062561`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004392`, median `-0.002441`, mae `0.01516`
- 5d: sample `20`, hit `0.45`, avg `-0.001842`, median `-0.007381`, mae `0.016781`
- 10d: sample `20`, hit `0.65`, avg `0.010078`, median `0.017789`, mae `0.029977`
- 20d: sample `20`, hit `0.95`, avg `0.032445`, median `0.041262`, mae `0.035407`
- 60d: sample `20`, hit `0.65`, avg `0.041355`, median `0.069439`, mae `0.083255`

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
- 3d: sample `20`, hit `0.4`, avg `-0.010447`, median `-0.009383`, mae `0.018892`
- 5d: sample `20`, hit `0.35`, avg `-0.015121`, median `-0.016062`, mae `0.021837`
- 10d: sample `20`, hit `0.25`, avg `-0.005842`, median `-0.007011`, mae `0.015876`
- 20d: sample `20`, hit `0.65`, avg `0.013934`, median `0.026113`, mae `0.040487`
- 60d: sample `20`, hit `0.7`, avg `0.04197`, median `0.059495`, mae `0.078895`

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
- 3d: sample `20`, hit `0.4`, avg `-0.010447`, median `-0.009383`, mae `0.018892`
- 5d: sample `20`, hit `0.35`, avg `-0.015121`, median `-0.016062`, mae `0.021837`
- 10d: sample `20`, hit `0.25`, avg `-0.005842`, median `-0.007011`, mae `0.015876`
- 20d: sample `20`, hit `0.65`, avg `0.013934`, median `0.026113`, mae `0.040487`
- 60d: sample `20`, hit `0.7`, avg `0.04197`, median `0.059495`, mae `0.078895`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004392`, median `-0.002441`, mae `0.01516`
- 5d: sample `20`, hit `0.45`, avg `-0.001842`, median `-0.007381`, mae `0.016781`
- 10d: sample `20`, hit `0.65`, avg `0.010078`, median `0.017789`, mae `0.029977`
- 20d: sample `20`, hit `0.95`, avg `0.032445`, median `0.041262`, mae `0.035407`
- 60d: sample `20`, hit `0.65`, avg `0.041355`, median `0.069439`, mae `0.083255`

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
- 3d: sample `80`, hit `0.5`, avg `-0.003695`, median `0.000201`, mae `0.01328`
- 5d: sample `80`, hit `0.45`, avg `-0.004176`, median `-0.001429`, mae `0.015458`
- 10d: sample `80`, hit `0.3875`, avg `-0.003767`, median `-0.007491`, mae `0.023533`
- 20d: sample `80`, hit `0.6625`, avg `0.006994`, median `0.016437`, mae `0.038874`
- 60d: sample `80`, hit `0.6`, avg `0.017227`, median `0.043615`, mae `0.079016`

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
