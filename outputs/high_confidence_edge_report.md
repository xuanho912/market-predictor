# High Confidence Edge Report

Generated at: `2026-10-17T15:39:22.247834+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `112`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `112`, gate `stronger_evidence`
- 5d: completed `112`, gate `stronger_evidence`
- 10d: completed `112`, gate `stronger_evidence`
- 20d: completed `112`, gate `stronger_evidence`
- 60d: completed `112`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.525`, avg `0.001899`, median `0.00234`, mae `0.018644`
- 5d: sample `80`, hit `0.6375`, avg `0.003446`, median `0.003554`, mae `0.02206`
- 10d: sample `80`, hit `0.5375`, avg `0.009098`, median `0.005477`, mae `0.03418`
- 20d: sample `80`, hit `0.675`, avg `0.02482`, median `0.022359`, mae `0.038145`
- 60d: sample `80`, hit `0.6875`, avg `0.050394`, median `0.059948`, mae `0.084651`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.000912`, median `0.009176`, mae `0.01291`
- 5d: sample `8`, hit `0.75`, avg `0.000977`, median `0.003554`, mae `0.005543`
- 10d: sample `8`, hit `0.375`, avg `-0.007047`, median `-0.007491`, mae `0.024716`
- 20d: sample `8`, hit `0.75`, avg `0.016257`, median `0.026806`, mae `0.027394`
- 60d: sample `8`, hit `0.25`, avg `-0.01494`, median `-0.030476`, mae `0.054484`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.013527`, median `0.016307`, mae `0.01434`
- 5d: sample `8`, hit `1.0`, avg `0.012781`, median `0.009709`, mae `0.012781`
- 10d: sample `8`, hit `0.5`, avg `0.006912`, median `0.011031`, mae `0.026542`
- 20d: sample `8`, hit `0.875`, avg `0.033985`, median `0.043002`, mae `0.035653`
- 60d: sample `8`, hit `0.75`, avg `0.053013`, median `0.085257`, mae `0.082526`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013527, 'median_return': 0.016307, 'mean_absolute_return': 0.01434, 'max_adverse_excursion': -0.001658, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.012781, 'median_return': 0.009709, 'mean_absolute_return': 0.012781, 'max_adverse_excursion': 0.000208, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.006912, 'median_return': 0.011031, 'mean_absolute_return': 0.026542, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.050818}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.033985, 'median_return': 0.043002, 'mean_absolute_return': 0.035653, 'max_adverse_excursion': -0.006669, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.053013, 'median_return': 0.085257, 'mean_absolute_return': 0.082526, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.000607, 'median_return': 0.000766, 'mean_absolute_return': 0.019122, 'max_adverse_excursion': -0.047619, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.002408, 'median_return': 0.002786, 'mean_absolute_return': 0.023091, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.009341, 'median_return': 0.005477, 'mean_absolute_return': 0.035029, 'max_adverse_excursion': -0.088606, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.023802, 'median_return': 0.022339, 'mean_absolute_return': 0.038422, 'max_adverse_excursion': -0.081434, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.050103, 'median_return': 0.059948, 'mean_absolute_return': 0.084887, 'max_adverse_excursion': -0.145377, 'max_favorable_excursion': 0.229735}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.3625}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.325}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.000792, 'median_return': 0.001405, 'mean_absolute_return': 0.011637, 'max_adverse_excursion': -0.03413, 'max_favorable_excursion': 0.028553}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.001517, 'median_return': 0.003554, 'mean_absolute_return': 0.013822, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.04165}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001832, 'median_return': 0.000397, 'mean_absolute_return': 0.020916, 'max_adverse_excursion': -0.040694, 'max_favorable_excursion': 0.047872}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.01927, 'median_return': 0.026806, 'mean_absolute_return': 0.02602, 'max_adverse_excursion': -0.02849, 'max_favorable_excursion': 0.053054}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.015194, 'median_return': 0.046407, 'mean_absolute_return': 0.054645, 'max_adverse_excursion': -0.070843, 'max_favorable_excursion': 0.098228}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.002796, 'median_return': 0.002744, 'mean_absolute_return': 0.02098, 'max_adverse_excursion': -0.047619, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.004088, 'median_return': 0.003829, 'mean_absolute_return': 0.024806, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.011521, 'median_return': 0.005519, 'mean_absolute_return': 0.038601, 'max_adverse_excursion': -0.088606, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.02667, 'median_return': 0.022359, 'mean_absolute_return': 0.042187, 'max_adverse_excursion': -0.081434, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.062127, 'median_return': 0.082366, 'mean_absolute_return': 0.094653, 'max_adverse_excursion': -0.145377, 'max_favorable_excursion': 0.229735}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.000121`, median `0.001405`, mae `0.014618`
- 5d: sample `40`, hit `0.7`, avg `0.000984`, median `0.003829`, mae `0.015778`
- 10d: sample `40`, hit `0.5`, avg `0.00247`, median `0.000197`, mae `0.021006`
- 20d: sample `40`, hit `0.725`, avg `0.022457`, median `0.02865`, mae `0.030041`
- 60d: sample `40`, hit `0.575`, avg `0.028599`, median `0.048963`, mae `0.064699`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.003919`, median `0.006343`, mae `0.022669`
- 5d: sample `40`, hit `0.575`, avg `0.005907`, median `0.002721`, mae `0.028342`
- 10d: sample `40`, hit `0.575`, avg `0.015727`, median `0.019731`, mae `0.047354`
- 20d: sample `40`, hit `0.625`, avg `0.027184`, median `0.016764`, mae `0.046249`
- 60d: sample `40`, hit `0.8`, avg `0.072188`, median `0.098816`, mae `0.104602`

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
- 3d: sample `20`, hit `0.55`, avg `-0.000792`, median `0.001405`, mae `0.011637`
- 5d: sample `20`, hit `0.7`, avg `0.001517`, median `0.003554`, mae `0.013822`
- 10d: sample `20`, hit `0.55`, avg `0.001832`, median `0.000397`, mae `0.020916`
- 20d: sample `20`, hit `0.7`, avg `0.01927`, median `0.026806`, mae `0.02602`
- 60d: sample `20`, hit `0.5`, avg `0.015194`, median `0.046407`, mae `0.054645`

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
- 3d: sample `20`, hit `0.55`, avg `-0.000792`, median `0.001405`, mae `0.011637`
- 5d: sample `20`, hit `0.7`, avg `0.001517`, median `0.003554`, mae `0.013822`
- 10d: sample `20`, hit `0.55`, avg `0.001832`, median `0.000397`, mae `0.020916`
- 20d: sample `20`, hit `0.7`, avg `0.01927`, median `0.026806`, mae `0.02602`
- 60d: sample `20`, hit `0.5`, avg `0.015194`, median `0.046407`, mae `0.054645`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.003919`, median `0.006343`, mae `0.022669`
- 5d: sample `40`, hit `0.575`, avg `0.005907`, median `0.002721`, mae `0.028342`
- 10d: sample `40`, hit `0.575`, avg `0.015727`, median `0.019731`, mae `0.047354`
- 20d: sample `40`, hit `0.625`, avg `0.027184`, median `0.016764`, mae `0.046249`
- 60d: sample `40`, hit `0.8`, avg `0.072188`, median `0.098816`, mae `0.104602`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000792`, median `0.001405`, mae `0.011637`
- 5d: sample `20`, hit `0.7`, avg `0.001517`, median `0.003554`, mae `0.013822`
- 10d: sample `20`, hit `0.55`, avg `0.001832`, median `0.000397`, mae `0.020916`
- 20d: sample `20`, hit `0.7`, avg `0.01927`, median `0.026806`, mae `0.02602`
- 60d: sample `20`, hit `0.5`, avg `0.015194`, median `0.046407`, mae `0.054645`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001899`, median `0.00234`, mae `0.018644`
- 5d: sample `80`, hit `0.6375`, avg `0.003446`, median `0.003554`, mae `0.02206`
- 10d: sample `80`, hit `0.5375`, avg `0.009098`, median `0.005477`, mae `0.03418`
- 20d: sample `80`, hit `0.675`, avg `0.02482`, median `0.022359`, mae `0.038145`
- 60d: sample `80`, hit `0.6875`, avg `0.050394`, median `0.059948`, mae `0.084651`

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
- 3d: sample `80`, hit `0.525`, avg `0.001899`, median `0.00234`, mae `0.018644`
- 5d: sample `80`, hit `0.6375`, avg `0.003446`, median `0.003554`, mae `0.02206`
- 10d: sample `80`, hit `0.5375`, avg `0.009098`, median `0.005477`, mae `0.03418`
- 20d: sample `80`, hit `0.675`, avg `0.02482`, median `0.022359`, mae `0.038145`
- 60d: sample `80`, hit `0.6875`, avg `0.050394`, median `0.059948`, mae `0.084651`

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
- 3d: sample `80`, hit `0.525`, avg `0.001899`, median `0.00234`, mae `0.018644`
- 5d: sample `80`, hit `0.6375`, avg `0.003446`, median `0.003554`, mae `0.02206`
- 10d: sample `80`, hit `0.5375`, avg `0.009098`, median `0.005477`, mae `0.03418`
- 20d: sample `80`, hit `0.675`, avg `0.02482`, median `0.022359`, mae `0.038145`
- 60d: sample `80`, hit `0.6875`, avg `0.050394`, median `0.059948`, mae `0.084651`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
