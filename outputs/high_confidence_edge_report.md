# High Confidence Edge Report

Generated at: `2026-07-23T21:35:07.703172+00:00`

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
- 3d: sample `20`, hit `0.5`, avg `-0.00586`, median `0.001199`, mae `0.019135`
- 5d: sample `20`, hit `0.5`, avg `-0.009813`, median `0.003005`, mae `0.02201`
- 10d: sample `20`, hit `0.4`, avg `-0.001455`, median `-0.0004`, mae `0.016791`
- 20d: sample `20`, hit `0.75`, avg `0.018056`, median `0.026113`, mae `0.039053`
- 60d: sample `20`, hit `0.8`, avg `0.053827`, median `0.059495`, mae `0.079604`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `-0.000354`, median `0.005296`, mae `0.017784`
- 5d: sample `60`, hit `0.5333`, avg `0.001434`, median `0.002451`, mae `0.021728`
- 10d: sample `60`, hit `0.6667`, avg `0.009728`, median `0.017201`, mae `0.03014`
- 20d: sample `60`, hit `0.6833`, avg `0.020641`, median `0.02865`, mae `0.048219`
- 60d: sample `60`, hit `0.65`, avg `0.022882`, median `0.057625`, mae `0.089115`

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
- 3d: sample `8`, hit `0.25`, avg `-0.01363`, median `-0.010033`, mae `0.024795`
- 5d: sample `8`, hit `0.375`, avg `-0.025133`, median `-0.022295`, mae `0.031476`
- 10d: sample `8`, hit `0.125`, avg `-0.011762`, median `-0.007755`, mae `0.014861`
- 20d: sample `8`, hit `0.375`, avg `-0.007317`, median `-0.001666`, mae `0.045176`
- 60d: sample `8`, hit `0.5`, avg `0.011993`, median `0.037425`, mae `0.076436`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.01363`, median `-0.010033`, mae `0.024795`
- 5d: sample `8`, hit `0.375`, avg `-0.025133`, median `-0.022295`, mae `0.031476`
- 10d: sample `8`, hit `0.125`, avg `-0.011762`, median `-0.007755`, mae `0.014861`
- 20d: sample `8`, hit `0.375`, avg `-0.007317`, median `-0.001666`, mae `0.045176`
- 60d: sample `8`, hit `0.5`, avg `0.011993`, median `0.037425`, mae `0.076436`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.00586, 'median_return': 0.001199, 'mean_absolute_return': 0.019135, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.009813, 'median_return': 0.003005, 'mean_absolute_return': 0.02201, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.001455, 'median_return': -0.0004, 'mean_absolute_return': 0.016791, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.018056, 'median_return': 0.026113, 'mean_absolute_return': 0.039053, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.053827, 'median_return': 0.059495, 'mean_absolute_return': 0.079604, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01363, 'median_return': -0.010033, 'mean_absolute_return': 0.024795, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.025133, 'median_return': -0.022295, 'mean_absolute_return': 0.031476, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.010589}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011762, 'median_return': -0.007755, 'mean_absolute_return': 0.014861, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.012396}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007317, 'median_return': -0.001666, 'mean_absolute_return': 0.045176, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.011993, 'median_return': 0.037425, 'mean_absolute_return': 0.076436, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': -0.000408, 'median_return': 0.004815, 'mean_absolute_return': 0.01738, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.001262, 'median_return': 0.002453, 'mean_absolute_return': 0.020723, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.009009, 'median_return': 0.016212, 'mean_absolute_return': 0.028129, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.075}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.023029, 'median_return': 0.029166, 'mean_absolute_return': 0.046011, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.032688, 'median_return': 0.059131, 'mean_absolute_return': 0.087882, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.425}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.35}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.4625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': -0.00095, 'median_return': 0.004815, 'mean_absolute_return': 0.017474, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.00143, 'median_return': 0.003829, 'mean_absolute_return': 0.019515, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.052328}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.009111, 'median_return': 0.010509, 'mean_absolute_return': 0.024084, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.075}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.026066, 'median_return': 0.033999, 'mean_absolute_return': 0.0432, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.042339, 'median_return': 0.059104, 'mean_absolute_return': 0.07998, 'max_adverse_excursion': -0.177732, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.004072, 'median_return': -0.0002, 'mean_absolute_return': 0.020064, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.009801, 'median_return': -0.00693, 'mean_absolute_return': 0.02865, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000397, 'median_return': 0.016791, 'mean_absolute_return': 0.034958, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.00178, 'median_return': 0.017237, 'mean_absolute_return': 0.054112, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.004543, 'median_return': 0.029625, 'mean_absolute_return': 0.107011, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.1448}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `-0.002652`, median `0.001405`, mae `0.015418`
- 5d: sample `40`, hit `0.55`, avg `-0.004899`, median `0.002774`, mae `0.01727`
- 10d: sample `40`, hit `0.475`, avg `-0.001255`, median `-0.000231`, mae `0.017282`
- 20d: sample `40`, hit `0.675`, avg `0.014329`, median `0.020226`, mae `0.035908`
- 60d: sample `40`, hit `0.725`, avg `0.038497`, median `0.053855`, mae `0.064773`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.00081`, median `0.006247`, mae `0.020826`
- 5d: sample `40`, hit `0.5`, avg `0.002143`, median `0.002451`, mae `0.026327`
- 10d: sample `40`, hit `0.725`, avg `0.01512`, median `0.023883`, mae `0.036322`
- 20d: sample `40`, hit `0.725`, avg `0.025661`, median `0.045973`, mae `0.055948`
- 60d: sample `40`, hit `0.65`, avg `0.022739`, median `0.072268`, mae `0.108702`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00586`, median `0.001199`, mae `0.019135`
- 5d: sample `20`, hit `0.5`, avg `-0.009813`, median `0.003005`, mae `0.02201`
- 10d: sample `20`, hit `0.4`, avg `-0.001455`, median `-0.0004`, mae `0.016791`
- 20d: sample `20`, hit `0.75`, avg `0.018056`, median `0.026113`, mae `0.039053`
- 60d: sample `20`, hit `0.8`, avg `0.053827`, median `0.059495`, mae `0.079604`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `-0.002652`, median `0.001405`, mae `0.015418`
- 5d: sample `40`, hit `0.55`, avg `-0.004899`, median `0.002774`, mae `0.01727`
- 10d: sample `40`, hit `0.475`, avg `-0.001255`, median `-0.000231`, mae `0.017282`
- 20d: sample `40`, hit `0.675`, avg `0.014329`, median `0.020226`, mae `0.035908`
- 60d: sample `40`, hit `0.725`, avg `0.038497`, median `0.053855`, mae `0.064773`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002453`, median `0.009701`, mae `0.021587`
- 5d: sample `20`, hit `0.65`, avg `0.014087`, median `0.019244`, mae `0.024005`
- 10d: sample `20`, hit `0.85`, avg `0.029843`, median `0.031521`, mae `0.037687`
- 20d: sample `20`, hit `0.85`, avg `0.049542`, median `0.054665`, mae `0.057784`
- 60d: sample `20`, hit `0.75`, avg `0.050021`, median `0.075265`, mae `0.110393`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00586`, median `0.001199`, mae `0.019135`
- 5d: sample `20`, hit `0.5`, avg `-0.009813`, median `0.003005`, mae `0.02201`
- 10d: sample `20`, hit `0.4`, avg `-0.001455`, median `-0.0004`, mae `0.016791`
- 20d: sample `20`, hit `0.75`, avg `0.018056`, median `0.026113`, mae `0.039053`
- 60d: sample `20`, hit `0.8`, avg `0.053827`, median `0.059495`, mae `0.079604`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `-0.002652`, median `0.001405`, mae `0.015418`
- 5d: sample `40`, hit `0.55`, avg `-0.004899`, median `0.002774`, mae `0.01727`
- 10d: sample `40`, hit `0.475`, avg `-0.001255`, median `-0.000231`, mae `0.017282`
- 20d: sample `40`, hit `0.675`, avg `0.014329`, median `0.020226`, mae `0.035908`
- 60d: sample `40`, hit `0.725`, avg `0.038497`, median `0.053855`, mae `0.064773`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.00081`, median `0.006247`, mae `0.020826`
- 5d: sample `40`, hit `0.5`, avg `0.002143`, median `0.002451`, mae `0.026327`
- 10d: sample `40`, hit `0.725`, avg `0.01512`, median `0.023883`, mae `0.036322`
- 20d: sample `40`, hit `0.725`, avg `0.025661`, median `0.045973`, mae `0.055948`
- 60d: sample `40`, hit `0.65`, avg `0.022739`, median `0.072268`, mae `0.108702`

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
- 3d: sample `80`, hit `0.575`, avg `-0.001731`, median `0.00234`, mae `0.018122`
- 5d: sample `80`, hit `0.525`, avg `-0.001378`, median `0.002451`, mae `0.021799`
- 10d: sample `80`, hit `0.6`, avg `0.006932`, median `0.010509`, mae `0.026802`
- 20d: sample `80`, hit `0.7`, avg `0.019995`, median `0.026113`, mae `0.045928`
- 60d: sample `80`, hit `0.6875`, avg `0.030618`, median `0.058473`, mae `0.086738`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00586`, median `0.001199`, mae `0.019135`
- 5d: sample `20`, hit `0.5`, avg `-0.009813`, median `0.003005`, mae `0.02201`
- 10d: sample `20`, hit `0.4`, avg `-0.001455`, median `-0.0004`, mae `0.016791`
- 20d: sample `20`, hit `0.75`, avg `0.018056`, median `0.026113`, mae `0.039053`
- 60d: sample `20`, hit `0.8`, avg `0.053827`, median `0.059495`, mae `0.079604`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004072`, median `-0.0002`, mae `0.020064`
- 5d: sample `20`, hit `0.35`, avg `-0.009801`, median `-0.00693`, mae `0.02865`
- 10d: sample `20`, hit `0.6`, avg `0.000397`, median `0.016791`, mae `0.034958`
- 20d: sample `20`, hit `0.6`, avg `0.00178`, median `0.017237`, mae `0.054112`
- 60d: sample `20`, hit `0.55`, avg `-0.004543`, median `0.029625`, mae `0.107011`

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
