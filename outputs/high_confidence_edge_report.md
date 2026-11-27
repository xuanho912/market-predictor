# High Confidence Edge Report

Generated at: `2026-11-27T21:20:19.972107+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `228`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `228`, gate `stronger_evidence`
- 5d: completed `228`, gate `stronger_evidence`
- 10d: completed `228`, gate `stronger_evidence`
- 20d: completed `228`, gate `stronger_evidence`
- 60d: completed `228`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.375`, avg `-0.003468`, median `-0.007311`, mae `0.020695`
- 5d: sample `80`, hit `0.425`, avg `-0.003034`, median `-0.00589`, mae `0.022859`
- 10d: sample `80`, hit `0.475`, avg `0.004071`, median `-0.00174`, mae `0.025027`
- 20d: sample `80`, hit `0.5`, avg `0.003921`, median `0.000519`, mae `0.03791`
- 60d: sample `80`, hit `0.4875`, avg `0.014162`, median `-0.004733`, mae `0.070856`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.010295`, median `-0.007923`, mae `0.011864`
- 5d: sample `8`, hit `0.25`, avg `-0.013203`, median `-0.015413`, mae `0.014478`
- 10d: sample `8`, hit `0.375`, avg `-0.012174`, median `-0.01051`, mae `0.015989`
- 20d: sample `8`, hit `0.5`, avg `0.003577`, median `0.029348`, mae `0.030485`
- 60d: sample `8`, hit `0.375`, avg `0.008535`, median `-0.006198`, mae `0.050852`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.010295`, median `-0.007923`, mae `0.011864`
- 5d: sample `8`, hit `0.25`, avg `-0.013203`, median `-0.015413`, mae `0.014478`
- 10d: sample `8`, hit `0.375`, avg `-0.012174`, median `-0.01051`, mae `0.015989`
- 20d: sample `8`, hit `0.5`, avg `0.003577`, median `0.029348`, mae `0.030485`
- 60d: sample `8`, hit `0.375`, avg `0.008535`, median `-0.006198`, mae `0.050852`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.010295, 'median_return': -0.007923, 'mean_absolute_return': 0.011864, 'max_adverse_excursion': -0.031875, 'max_favorable_excursion': 0.006274}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.013203, 'median_return': -0.015413, 'mean_absolute_return': 0.014478, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.003402}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012174, 'median_return': -0.01051, 'mean_absolute_return': 0.015989, 'max_adverse_excursion': -0.038784, 'max_favorable_excursion': 0.009373}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003577, 'median_return': 0.029348, 'mean_absolute_return': 0.030485, 'max_adverse_excursion': -0.051042, 'max_favorable_excursion': 0.040895}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.008535, 'median_return': -0.006198, 'mean_absolute_return': 0.050852, 'max_adverse_excursion': -0.051413, 'max_favorable_excursion': 0.092194}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.00271, 'median_return': -0.005064, 'mean_absolute_return': 0.021676, 'max_adverse_excursion': -0.060978, 'max_favorable_excursion': 0.071126}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.001904, 'median_return': -0.004438, 'mean_absolute_return': 0.02379, 'max_adverse_excursion': -0.061828, 'max_favorable_excursion': 0.087795}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.005875, 'median_return': -0.000555, 'mean_absolute_return': 0.026031, 'max_adverse_excursion': -0.065085, 'max_favorable_excursion': 0.13116}, '20d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.003959, 'median_return': 0.000519, 'mean_absolute_return': 0.038735, 'max_adverse_excursion': -0.087865, 'max_favorable_excursion': 0.117235}, '60d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.014787, 'median_return': 0.003374, 'mean_absolute_return': 0.073079, 'max_adverse_excursion': -0.200412, 'max_favorable_excursion': 0.195631}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.425}, '5d': {'sample_size': 80, 'hit_rate': 0.35}, '10d': {'sample_size': 80, 'hit_rate': 0.4}, '20d': {'sample_size': 80, 'hit_rate': 0.5}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.35, 'avg_return': -0.004188, 'median_return': -0.007311, 'mean_absolute_return': 0.017097, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.036532}, '5d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.007168, 'median_return': -0.006798, 'mean_absolute_return': 0.018165, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.062512}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.001891, 'median_return': -0.003866, 'mean_absolute_return': 0.018671, 'max_adverse_excursion': -0.055936, 'max_favorable_excursion': 0.097457}, '20d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.008222, 'median_return': 0.004024, 'mean_absolute_return': 0.035439, 'max_adverse_excursion': -0.059023, 'max_favorable_excursion': 0.117235}, '60d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.019799, 'median_return': -0.004733, 'mean_absolute_return': 0.069195, 'max_adverse_excursion': -0.170201, 'max_favorable_excursion': 0.195631}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00131, 'median_return': -0.005064, 'mean_absolute_return': 0.031491, 'max_adverse_excursion': -0.060978, 'max_favorable_excursion': 0.071126}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.009367, 'median_return': 0.013949, 'mean_absolute_return': 0.036943, 'max_adverse_excursion': -0.061828, 'max_favorable_excursion': 0.087795}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.021954, 'median_return': 0.022482, 'mean_absolute_return': 0.044096, 'max_adverse_excursion': -0.065085, 'max_favorable_excursion': 0.13116}, '20d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.008983, 'median_return': -0.017449, 'mean_absolute_return': 0.045325, 'max_adverse_excursion': -0.087865, 'max_favorable_excursion': 0.089385}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.002749, 'median_return': 0.003374, 'mean_absolute_return': 0.07584, 'max_adverse_excursion': -0.200412, 'max_favorable_excursion': 0.147455}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.35`, avg `-0.004188`, median `-0.007311`, mae `0.017097`
- 5d: sample `60`, hit `0.3833`, avg `-0.007168`, median `-0.006798`, mae `0.018165`
- 10d: sample `60`, hit `0.4333`, avg `-0.001891`, median `-0.003866`, mae `0.018671`
- 20d: sample `60`, hit `0.55`, avg `0.008222`, median `0.004024`, mae `0.035439`
- 60d: sample `60`, hit `0.4833`, avg `0.019799`, median `-0.004733`, mae `0.069195`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00131`, median `-0.005064`, mae `0.031491`
- 5d: sample `20`, hit `0.55`, avg `0.009367`, median `0.013949`, mae `0.036943`
- 10d: sample `20`, hit `0.6`, avg `0.021954`, median `0.022482`, mae `0.044096`
- 20d: sample `20`, hit `0.35`, avg `-0.008983`, median `-0.017449`, mae `0.045325`
- 60d: sample `20`, hit `0.5`, avg `-0.002749`, median `0.003374`, mae `0.07584`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.006017`, median `-0.007923`, mae `0.016571`
- 5d: sample `40`, hit `0.275`, avg `-0.012347`, median `-0.013733`, mae `0.016666`
- 10d: sample `40`, hit `0.375`, avg `-0.006976`, median `-0.005223`, mae `0.014605`
- 20d: sample `40`, hit `0.5`, avg `0.003085`, median `0.003056`, mae `0.031672`
- 60d: sample `40`, hit `0.525`, avg `0.020826`, median `0.05488`, mae `0.067772`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.006017`, median `-0.007923`, mae `0.016571`
- 5d: sample `40`, hit `0.275`, avg `-0.012347`, median `-0.013733`, mae `0.016666`
- 10d: sample `40`, hit `0.375`, avg `-0.006976`, median `-0.005223`, mae `0.014605`
- 20d: sample `40`, hit `0.5`, avg `0.003085`, median `0.003056`, mae `0.031672`
- 60d: sample `40`, hit `0.525`, avg `0.020826`, median `0.05488`, mae `0.067772`

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
- 3d: sample `20`, hit `0.45`, avg `-0.00131`, median `-0.005064`, mae `0.031491`
- 5d: sample `20`, hit `0.55`, avg `0.009367`, median `0.013949`, mae `0.036943`
- 10d: sample `20`, hit `0.6`, avg `0.021954`, median `0.022482`, mae `0.044096`
- 20d: sample `20`, hit `0.35`, avg `-0.008983`, median `-0.017449`, mae `0.045325`
- 60d: sample `20`, hit `0.5`, avg `-0.002749`, median `0.003374`, mae `0.07584`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.006017`, median `-0.007923`, mae `0.016571`
- 5d: sample `40`, hit `0.275`, avg `-0.012347`, median `-0.013733`, mae `0.016666`
- 10d: sample `40`, hit `0.375`, avg `-0.006976`, median `-0.005223`, mae `0.014605`
- 20d: sample `40`, hit `0.5`, avg `0.003085`, median `0.003056`, mae `0.031672`
- 60d: sample `40`, hit `0.525`, avg `0.020826`, median `0.05488`, mae `0.067772`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000528`, median `-0.000261`, mae `0.018147`
- 5d: sample `20`, hit `0.6`, avg `0.003191`, median `0.003248`, mae `0.021163`
- 10d: sample `20`, hit `0.55`, avg `0.00828`, median `0.006356`, mae `0.026801`
- 20d: sample `20`, hit `0.65`, avg `0.018496`, median `0.013823`, mae `0.042972`
- 60d: sample `20`, hit `0.4`, avg `0.017744`, median `-0.014864`, mae `0.072042`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00131`, median `-0.005064`, mae `0.031491`
- 5d: sample `20`, hit `0.55`, avg `0.009367`, median `0.013949`, mae `0.036943`
- 10d: sample `20`, hit `0.6`, avg `0.021954`, median `0.022482`, mae `0.044096`
- 20d: sample `20`, hit `0.35`, avg `-0.008983`, median `-0.017449`, mae `0.045325`
- 60d: sample `20`, hit `0.5`, avg `-0.002749`, median `0.003374`, mae `0.07584`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.006017`, median `-0.007923`, mae `0.016571`
- 5d: sample `40`, hit `0.275`, avg `-0.012347`, median `-0.013733`, mae `0.016666`
- 10d: sample `40`, hit `0.375`, avg `-0.006976`, median `-0.005223`, mae `0.014605`
- 20d: sample `40`, hit `0.5`, avg `0.003085`, median `0.003056`, mae `0.031672`
- 60d: sample `40`, hit `0.525`, avg `0.020826`, median `0.05488`, mae `0.067772`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.375`, avg `-0.003468`, median `-0.007311`, mae `0.020695`
- 5d: sample `80`, hit `0.425`, avg `-0.003034`, median `-0.00589`, mae `0.022859`
- 10d: sample `80`, hit `0.475`, avg `0.004071`, median `-0.00174`, mae `0.025027`
- 20d: sample `80`, hit `0.5`, avg `0.003921`, median `0.000519`, mae `0.03791`
- 60d: sample `80`, hit `0.4875`, avg `0.014162`, median `-0.004733`, mae `0.070856`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.006017`, median `-0.007923`, mae `0.016571`
- 5d: sample `40`, hit `0.275`, avg `-0.012347`, median `-0.013733`, mae `0.016666`
- 10d: sample `40`, hit `0.375`, avg `-0.006976`, median `-0.005223`, mae `0.014605`
- 20d: sample `40`, hit `0.5`, avg `0.003085`, median `0.003056`, mae `0.031672`
- 60d: sample `40`, hit `0.525`, avg `0.020826`, median `0.05488`, mae `0.067772`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.375`, avg `-0.003468`, median `-0.007311`, mae `0.020695`
- 5d: sample `80`, hit `0.425`, avg `-0.003034`, median `-0.00589`, mae `0.022859`
- 10d: sample `80`, hit `0.475`, avg `0.004071`, median `-0.00174`, mae `0.025027`
- 20d: sample `80`, hit `0.5`, avg `0.003921`, median `0.000519`, mae `0.03791`
- 60d: sample `80`, hit `0.4875`, avg `0.014162`, median `-0.004733`, mae `0.070856`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
