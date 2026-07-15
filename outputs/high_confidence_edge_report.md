# High Confidence Edge Report

Generated at: `2026-07-15T04:20:39.052981+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.002258`, median `0.004573`, mae `0.013533`
- 5d: sample `40`, hit `0.6`, avg `0.002965`, median `0.008121`, mae `0.020276`
- 10d: sample `40`, hit `0.75`, avg `0.014057`, median `0.017201`, mae `0.023805`
- 20d: sample `40`, hit `0.85`, avg `0.022983`, median `0.026005`, mae `0.03126`
- 60d: sample `40`, hit `0.775`, avg `0.044041`, median `0.062103`, mae `0.066712`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.005246`, median `0.012272`, mae `0.016574`
- 5d: sample `40`, hit `0.55`, avg `0.005519`, median `0.009709`, mae `0.021172`
- 10d: sample `40`, hit `0.55`, avg `0.009626`, median `0.004187`, mae `0.023564`
- 20d: sample `40`, hit `0.95`, avg `0.032493`, median `0.027502`, mae `0.033557`
- 60d: sample `40`, hit `0.75`, avg `0.038948`, median `0.034496`, mae `0.058352`

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
- 3d: sample `8`, hit `0.375`, avg `-0.003861`, median `-0.0002`, mae `0.018283`
- 5d: sample `8`, hit `0.5`, avg `-0.000193`, median `0.018277`, mae `0.024553`
- 10d: sample `8`, hit `0.625`, avg `0.014219`, median `0.034277`, mae `0.037535`
- 20d: sample `8`, hit `0.75`, avg `0.011471`, median `0.026005`, mae `0.036406`
- 60d: sample `8`, hit `0.625`, avg `0.039214`, median `0.074246`, mae `0.07818`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.006147`, median `0.00745`, mae `0.010554`
- 5d: sample `8`, hit `0.875`, avg `0.014296`, median `0.012953`, mae `0.015303`
- 10d: sample `8`, hit `0.875`, avg `0.019439`, median `0.021584`, mae `0.019492`
- 20d: sample `8`, hit `1.0`, avg `0.031098`, median `0.033582`, mae `0.031098`
- 60d: sample `8`, hit `1.0`, avg `0.077273`, median `0.087238`, mae `0.077273`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.002258, 'median_return': 0.004573, 'mean_absolute_return': 0.013533, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002965, 'median_return': 0.008121, 'mean_absolute_return': 0.020276, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.014057, 'median_return': 0.017201, 'mean_absolute_return': 0.023805, 'max_adverse_excursion': -0.036599, 'max_favorable_excursion': 0.067122}, '20d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.022983, 'median_return': 0.026005, 'mean_absolute_return': 0.03126, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.044041, 'median_return': 0.062103, 'mean_absolute_return': 0.066712, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.006147, 'median_return': 0.00745, 'mean_absolute_return': 0.010554, 'max_adverse_excursion': -0.017627, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.014296, 'median_return': 0.012953, 'mean_absolute_return': 0.015303, 'max_adverse_excursion': -0.004032, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.019439, 'median_return': 0.021584, 'mean_absolute_return': 0.019492, 'max_adverse_excursion': -0.000214, 'max_favorable_excursion': 0.032557}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.031098, 'median_return': 0.033582, 'mean_absolute_return': 0.031098, 'max_adverse_excursion': 0.019193, 'max_favorable_excursion': 0.04151}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.077273, 'median_return': 0.087238, 'mean_absolute_return': 0.077273, 'max_adverse_excursion': 0.043741, 'max_favorable_excursion': 0.10629}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.003486, 'median_return': 0.004815, 'mean_absolute_return': 0.015553, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.003125, 'median_return': 0.006036, 'mean_absolute_return': 0.021326, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.010997, 'median_return': 0.00693, 'mean_absolute_return': 0.024151, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 72, 'hit_rate': 0.8889, 'avg_return': 0.027365, 'median_return': 0.024743, 'mean_absolute_return': 0.032554, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.037519, 'median_return': 0.046273, 'mean_absolute_return': 0.060894, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.147541}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.1, 'both_hit': 26, 'both_miss': 14}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.05, 'both_hit': 24, 'both_miss': 16}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.05, 'both_hit': 30, 'both_miss': 10}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.9, 'primary_minus_secondary': -0.45, 'both_hit': 34, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.25, 'both_hit': 31, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.003752, 'median_return': 0.005804, 'mean_absolute_return': 0.015053, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.004242, 'median_return': 0.008121, 'mean_absolute_return': 0.020724, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.011842, 'median_return': 0.012215, 'mean_absolute_return': 0.023685, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 80, 'hit_rate': 0.9, 'avg_return': 0.027738, 'median_return': 0.026005, 'mean_absolute_return': 0.032409, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.041495, 'median_return': 0.053855, 'mean_absolute_return': 0.062532, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.147541}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.003777`, median `0.006198`, mae `0.012761`
- 5d: sample `40`, hit `0.575`, avg `0.003883`, median `0.00774`, mae `0.017847`
- 10d: sample `40`, hit `0.625`, avg `0.007895`, median `0.00693`, mae `0.017471`
- 20d: sample `40`, hit `0.925`, avg `0.022083`, median `0.024701`, mae `0.023622`
- 60d: sample `40`, hit `0.75`, avg `0.028336`, median `0.036513`, mae `0.046483`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.00525`, median `0.007259`, mae `0.01387`
- 5d: sample `60`, hit `0.6167`, avg `0.006707`, median `0.009709`, mae `0.018722`
- 10d: sample `60`, hit `0.65`, avg `0.011059`, median `0.011031`, mae `0.020638`
- 20d: sample `60`, hit `0.95`, avg `0.030523`, median `0.02865`, mae `0.031549`
- 60d: sample `60`, hit `0.8167`, avg `0.044111`, median `0.046407`, mae `0.057741`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.003777`, median `0.006198`, mae `0.012761`
- 5d: sample `40`, hit `0.575`, avg `0.003883`, median `0.00774`, mae `0.017847`
- 10d: sample `40`, hit `0.625`, avg `0.007895`, median `0.00693`, mae `0.017471`
- 20d: sample `40`, hit `0.925`, avg `0.022083`, median `0.024701`, mae `0.023622`
- 60d: sample `40`, hit `0.75`, avg `0.028336`, median `0.036513`, mae `0.046483`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.00525`, median `0.007259`, mae `0.01387`
- 5d: sample `60`, hit `0.6167`, avg `0.006707`, median `0.009709`, mae `0.018722`
- 10d: sample `60`, hit `0.65`, avg `0.011059`, median `0.011031`, mae `0.020638`
- 20d: sample `60`, hit `0.95`, avg `0.030523`, median `0.02865`, mae `0.031549`
- 60d: sample `60`, hit `0.8167`, avg `0.044111`, median `0.046407`, mae `0.057741`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000743`, median `0.0017`, mae `0.018601`
- 5d: sample `20`, hit `0.45`, avg `-0.003151`, median `-0.007916`, mae `0.026729`
- 10d: sample `20`, hit `0.65`, avg `0.01419`, median `0.023905`, mae `0.032826`
- 20d: sample `20`, hit `0.75`, avg `0.019383`, median `0.017648`, mae `0.034989`
- 60d: sample `20`, hit `0.6`, avg `0.033644`, median `0.069306`, mae `0.076905`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.003777`, median `0.006198`, mae `0.012761`
- 5d: sample `40`, hit `0.575`, avg `0.003883`, median `0.00774`, mae `0.017847`
- 10d: sample `40`, hit `0.625`, avg `0.007895`, median `0.00693`, mae `0.017471`
- 20d: sample `40`, hit `0.925`, avg `0.022083`, median `0.024701`, mae `0.023622`
- 60d: sample `40`, hit `0.75`, avg `0.028336`, median `0.036513`, mae `0.046483`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.005246`, median `0.012272`, mae `0.016574`
- 5d: sample `40`, hit `0.55`, avg `0.005519`, median `0.009709`, mae `0.021172`
- 10d: sample `40`, hit `0.55`, avg `0.009626`, median `0.004187`, mae `0.023564`
- 20d: sample `40`, hit `0.95`, avg `0.032493`, median `0.027502`, mae `0.033557`
- 60d: sample `40`, hit `0.75`, avg `0.038948`, median `0.034496`, mae `0.058352`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.005246`, median `0.012272`, mae `0.016574`
- 5d: sample `40`, hit `0.55`, avg `0.005519`, median `0.009709`, mae `0.021172`
- 10d: sample `40`, hit `0.55`, avg `0.009626`, median `0.004187`, mae `0.023564`
- 20d: sample `40`, hit `0.95`, avg `0.032493`, median `0.027502`, mae `0.033557`
- 60d: sample `40`, hit `0.75`, avg `0.038948`, median `0.034496`, mae `0.058352`

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
