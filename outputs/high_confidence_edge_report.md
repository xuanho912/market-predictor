# High Confidence Edge Report

Generated at: `2026-11-06T01:03:52.132526+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `168`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `168`, gate `stronger_evidence`
- 5d: completed `168`, gate `stronger_evidence`
- 10d: completed `168`, gate `stronger_evidence`
- 20d: completed `168`, gate `stronger_evidence`
- 60d: completed `168`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.65`, avg `0.003837`, median `0.011636`, mae `0.025744`
- 5d: sample `80`, hit `0.65`, avg `0.008413`, median `0.012762`, mae `0.028475`
- 10d: sample `80`, hit `0.625`, avg `0.010262`, median `0.020801`, mae `0.048358`
- 20d: sample `80`, hit `0.675`, avg `0.005687`, median `0.033017`, mae `0.065963`
- 60d: sample `80`, hit `0.725`, avg `0.033874`, median `0.059797`, mae `0.088976`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.003923`, median `0.013309`, mae `0.021341`
- 5d: sample `8`, hit `0.875`, avg `0.013152`, median `0.020079`, mae `0.023681`
- 10d: sample `8`, hit `0.625`, avg `0.001856`, median `0.032676`, mae `0.052534`
- 20d: sample `8`, hit `0.75`, avg `-0.020003`, median `0.052467`, mae `0.092618`
- 60d: sample `8`, hit `0.625`, avg `0.019104`, median `0.053559`, mae `0.068235`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.009711`, median `0.02076`, mae `0.025253`
- 5d: sample `8`, hit `0.625`, avg `0.012135`, median `0.014974`, mae `0.025351`
- 10d: sample `8`, hit `0.625`, avg `0.006787`, median `0.029984`, mae `0.060517`
- 20d: sample `8`, hit `0.625`, avg `-0.025414`, median `0.033017`, mae `0.089952`
- 60d: sample `8`, hit `0.75`, avg `0.046625`, median `0.068318`, mae `0.072533`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009711, 'median_return': 0.02076, 'mean_absolute_return': 0.025253, 'max_adverse_excursion': -0.052423, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.012135, 'median_return': 0.014974, 'mean_absolute_return': 0.025351, 'max_adverse_excursion': -0.039693, 'max_favorable_excursion': 0.048375}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006787, 'median_return': 0.029984, 'mean_absolute_return': 0.060517, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.025414, 'median_return': 0.033017, 'mean_absolute_return': 0.089952, 'max_adverse_excursion': -0.222293, 'max_favorable_excursion': 0.085922}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.046625, 'median_return': 0.068318, 'mean_absolute_return': 0.072533, 'max_adverse_excursion': -0.053355, 'max_favorable_excursion': 0.110811}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.003184, 'median_return': 0.011636, 'mean_absolute_return': 0.025798, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.061209}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.007999, 'median_return': 0.012762, 'mean_absolute_return': 0.028822, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.06431}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.010648, 'median_return': 0.020801, 'mean_absolute_return': 0.047007, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.109782}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.009143, 'median_return': 0.033112, 'mean_absolute_return': 0.063297, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.032457, 'median_return': 0.054522, 'mean_absolute_return': 0.090803, 'max_adverse_excursion': -0.331416, 'max_favorable_excursion': 0.213753}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.35}, '5d': {'sample_size': 80, 'hit_rate': 0.35}, '10d': {'sample_size': 80, 'hit_rate': 0.3625}, '20d': {'sample_size': 80, 'hit_rate': 0.325}, '60d': {'sample_size': 80, 'hit_rate': 0.275}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.2625, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.008001, 'median_return': 0.012603, 'mean_absolute_return': 0.021618, 'max_adverse_excursion': -0.059623, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.010399, 'median_return': 0.014974, 'mean_absolute_return': 0.025731, 'max_adverse_excursion': -0.056798, 'max_favorable_excursion': 0.053731}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.008922, 'median_return': 0.016492, 'mean_absolute_return': 0.043669, 'max_adverse_excursion': -0.125677, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.000857, 'median_return': 0.025065, 'mean_absolute_return': 0.063669, 'max_adverse_excursion': -0.236646, 'max_favorable_excursion': 0.096037}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.039921, 'median_return': 0.053913, 'mean_absolute_return': 0.063825, 'max_adverse_excursion': -0.092242, 'max_favorable_excursion': 0.136738}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': -0.000327, 'median_return': 0.010905, 'mean_absolute_return': 0.029869, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.061209}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.006427, 'median_return': 0.012749, 'mean_absolute_return': 0.031218, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.06431}, '10d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.011601, 'median_return': 0.024864, 'mean_absolute_return': 0.053047, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.109782}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.012231, 'median_return': 0.04796, 'mean_absolute_return': 0.068257, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.027827, 'median_return': 0.078127, 'mean_absolute_return': 0.114126, 'max_adverse_excursion': -0.331416, 'max_favorable_excursion': 0.213753}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003389`, median `0.010905`, mae `0.025315`
- 5d: sample `60`, hit `0.6167`, avg `0.004052`, median `0.012625`, mae `0.029149`
- 10d: sample `60`, hit `0.55`, avg `0.000531`, median `0.011842`, mae `0.04642`
- 20d: sample `60`, hit `0.6`, avg `-0.009587`, median `0.016803`, mae `0.06752`
- 60d: sample `60`, hit `0.7`, avg `0.019639`, median `0.052268`, mae `0.077113`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.005181`, median `0.012424`, mae `0.02703`
- 5d: sample `20`, hit `0.75`, avg `0.021497`, median `0.020777`, mae `0.026452`
- 10d: sample `20`, hit `0.85`, avg `0.039454`, median `0.057851`, mae `0.054171`
- 20d: sample `20`, hit `0.9`, avg `0.05151`, median `0.066558`, mae `0.061291`
- 60d: sample `20`, hit `0.8`, avg `0.076579`, median `0.111231`, mae `0.124564`

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
- 3d: sample `20`, hit `0.75`, avg `0.005181`, median `0.012424`, mae `0.02703`
- 5d: sample `20`, hit `0.75`, avg `0.021497`, median `0.020777`, mae `0.026452`
- 10d: sample `20`, hit `0.85`, avg `0.039454`, median `0.057851`, mae `0.054171`
- 20d: sample `20`, hit `0.9`, avg `0.05151`, median `0.066558`, mae `0.061291`
- 60d: sample `20`, hit `0.8`, avg `0.076579`, median `0.111231`, mae `0.124564`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.008001`, median `0.012603`, mae `0.021618`
- 5d: sample `40`, hit `0.65`, avg `0.010399`, median `0.014974`, mae `0.025731`
- 10d: sample `40`, hit `0.575`, avg `0.008922`, median `0.016492`, mae `0.043669`
- 20d: sample `40`, hit `0.625`, avg `-0.000857`, median `0.025065`, mae `0.063669`
- 60d: sample `40`, hit `0.75`, avg `0.039921`, median `0.053913`, mae `0.063825`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.005836`, median `0.005555`, mae `0.032709`
- 5d: sample `20`, hit `0.55`, avg `-0.008644`, median `0.004527`, mae `0.035984`
- 10d: sample `20`, hit `0.5`, avg `-0.016251`, median `0.006027`, mae `0.051923`
- 20d: sample `20`, hit `0.55`, avg `-0.027047`, median `0.003153`, mae `0.075224`
- 60d: sample `20`, hit `0.6`, avg `-0.020925`, median `0.023684`, mae `0.103689`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.003837`, median `0.011636`, mae `0.025744`
- 5d: sample `80`, hit `0.65`, avg `0.008413`, median `0.012762`, mae `0.028475`
- 10d: sample `80`, hit `0.625`, avg `0.010262`, median `0.020801`, mae `0.048358`
- 20d: sample `80`, hit `0.675`, avg `0.005687`, median `0.033017`, mae `0.065963`
- 60d: sample `80`, hit `0.725`, avg `0.033874`, median `0.059797`, mae `0.088976`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.003837`, median `0.011636`, mae `0.025744`
- 5d: sample `80`, hit `0.65`, avg `0.008413`, median `0.012762`, mae `0.028475`
- 10d: sample `80`, hit `0.625`, avg `0.010262`, median `0.020801`, mae `0.048358`
- 20d: sample `80`, hit `0.675`, avg `0.005687`, median `0.033017`, mae `0.065963`
- 60d: sample `80`, hit `0.725`, avg `0.033874`, median `0.059797`, mae `0.088976`

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
- 3d: sample `80`, hit `0.65`, avg `0.003837`, median `0.011636`, mae `0.025744`
- 5d: sample `80`, hit `0.65`, avg `0.008413`, median `0.012762`, mae `0.028475`
- 10d: sample `80`, hit `0.625`, avg `0.010262`, median `0.020801`, mae `0.048358`
- 20d: sample `80`, hit `0.675`, avg `0.005687`, median `0.033017`, mae `0.065963`
- 60d: sample `80`, hit `0.725`, avg `0.033874`, median `0.059797`, mae `0.088976`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
