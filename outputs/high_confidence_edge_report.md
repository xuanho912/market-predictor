# High Confidence Edge Report

Generated at: `2026-10-16T08:31:28.517431+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `108`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `108`, gate `stronger_evidence`
- 5d: completed `108`, gate `stronger_evidence`
- 10d: completed `108`, gate `stronger_evidence`
- 20d: completed `108`, gate `stronger_evidence`
- 60d: completed `108`, gate `stronger_evidence`

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
- 3d: sample `40`, hit `0.475`, avg `-0.006261`, median `-0.000285`, mae `0.015689`
- 5d: sample `40`, hit `0.4`, avg `-0.009411`, median `-0.006464`, mae `0.017711`
- 10d: sample `40`, hit `0.35`, avg `-0.005415`, median `-0.007491`, mae `0.017872`
- 20d: sample `40`, hit `0.575`, avg `0.011282`, median `0.01927`, mae `0.032887`
- 60d: sample `40`, hit `0.675`, avg `0.031497`, median `0.053855`, mae `0.066194`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.006876`, median `-0.013524`, mae `0.017653`
- 5d: sample `20`, hit `0.45`, avg `-0.005296`, median `-0.002776`, mae `0.018532`
- 10d: sample `20`, hit `0.5`, avg `-0.002423`, median `0.001455`, mae `0.018794`
- 20d: sample `20`, hit `0.8`, avg `0.023927`, median `0.018431`, mae `0.025121`
- 60d: sample `20`, hit `0.8`, avg `0.074972`, median `0.074296`, mae `0.085082`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.009429`, median `-0.008838`, mae `0.014653`
- 5d: sample `20`, hit `0.25`, avg `-0.014186`, median `-0.017697`, mae `0.023519`
- 10d: sample `20`, hit `0.25`, avg `-0.020132`, median `-0.032571`, mae `0.039558`
- 20d: sample `20`, hit `0.55`, avg `0.022897`, median `0.039427`, mae `0.051908`
- 60d: sample `20`, hit `0.9`, avg `0.07432`, median `0.092689`, mae `0.08502`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.002404`, median `0.004815`, mae `0.010167`
- 5d: sample `8`, hit `0.5`, avg `-0.003861`, median `0.000688`, mae `0.016887`
- 10d: sample `8`, hit `0.5`, avg `-0.00401`, median `0.000197`, mae `0.014368`
- 20d: sample `8`, hit `0.5`, avg `0.011979`, median `0.01927`, mae `0.021466`
- 60d: sample `8`, hit `0.625`, avg `0.020146`, median `0.046407`, mae `0.042916`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.002404`, median `0.004815`, mae `0.010167`
- 5d: sample `8`, hit `0.5`, avg `-0.003861`, median `0.000688`, mae `0.016887`
- 10d: sample `8`, hit `0.5`, avg `-0.00401`, median `0.000197`, mae `0.014368`
- 20d: sample `8`, hit `0.5`, avg `0.011979`, median `0.01927`, mae `0.021466`
- 60d: sample `8`, hit `0.625`, avg `0.020146`, median `0.046407`, mae `0.042916`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.006261, 'median_return': -0.000285, 'mean_absolute_return': 0.015689, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.009411, 'median_return': -0.006464, 'mean_absolute_return': 0.017711, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.005415, 'median_return': -0.007491, 'mean_absolute_return': 0.017872, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.011282, 'median_return': 0.01927, 'mean_absolute_return': 0.032887, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.031497, 'median_return': 0.053855, 'mean_absolute_return': 0.066194, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.002404, 'median_return': 0.004815, 'mean_absolute_return': 0.010167, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.010897}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003861, 'median_return': 0.000688, 'mean_absolute_return': 0.016887, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.00401, 'median_return': 0.000197, 'mean_absolute_return': 0.014368, 'max_adverse_excursion': -0.025298, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.011979, 'median_return': 0.01927, 'mean_absolute_return': 0.021466, 'max_adverse_excursion': -0.016058, 'max_favorable_excursion': 0.046563}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.020146, 'median_return': 0.046407, 'mean_absolute_return': 0.042916, 'max_adverse_excursion': -0.046594, 'max_favorable_excursion': 0.059948}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.007741, 'median_return': -0.008838, 'mean_absolute_return': 0.01656, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.3611, 'avg_return': -0.010211, 'median_return': -0.011925, 'mean_absolute_return': 0.019644, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.3472, 'avg_return': -0.008828, 'median_return': -0.011432, 'mean_absolute_return': 0.024541, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.017943, 'median_return': 0.018431, 'mean_absolute_return': 0.037282, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.05673, 'median_return': 0.06608, 'mean_absolute_return': 0.079257, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.375}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.006261, 'median_return': -0.000285, 'mean_absolute_return': 0.015689, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.009411, 'median_return': -0.006464, 'mean_absolute_return': 0.017711, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.005415, 'median_return': -0.007491, 'mean_absolute_return': 0.017872, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.011282, 'median_return': 0.01927, 'mean_absolute_return': 0.032887, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.031497, 'median_return': 0.053855, 'mean_absolute_return': 0.066194, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.008152, 'median_return': -0.009843, 'mean_absolute_return': 0.016153, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.009741, 'median_return': -0.013229, 'mean_absolute_return': 0.021025, 'max_adverse_excursion': -0.044779, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.011277, 'median_return': -0.015101, 'mean_absolute_return': 0.029176, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.023412, 'median_return': 0.018431, 'mean_absolute_return': 0.038514, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.074646, 'median_return': 0.079528, 'mean_absolute_return': 0.085051, 'max_adverse_excursion': -0.103316, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.006261`, median `-0.000285`, mae `0.015689`
- 5d: sample `40`, hit `0.4`, avg `-0.009411`, median `-0.006464`, mae `0.017711`
- 10d: sample `40`, hit `0.35`, avg `-0.005415`, median `-0.007491`, mae `0.017872`
- 20d: sample `40`, hit `0.575`, avg `0.011282`, median `0.01927`, mae `0.032887`
- 60d: sample `40`, hit `0.675`, avg `0.031497`, median `0.053855`, mae `0.066194`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.008152`, median `-0.009843`, mae `0.016153`
- 5d: sample `40`, hit `0.35`, avg `-0.009741`, median `-0.013229`, mae `0.021025`
- 10d: sample `40`, hit `0.375`, avg `-0.011277`, median `-0.015101`, mae `0.029176`
- 20d: sample `40`, hit `0.675`, avg `0.023412`, median `0.018431`, mae `0.038514`
- 60d: sample `40`, hit `0.85`, avg `0.074646`, median `0.079528`, mae `0.085051`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003754`, median `0.000766`, mae `0.01237`
- 5d: sample `20`, hit `0.45`, avg `-0.00489`, median `-0.000513`, mae `0.014016`
- 10d: sample `20`, hit `0.45`, avg `-0.002824`, median `-0.007314`, mae `0.017702`
- 20d: sample `20`, hit `0.5`, avg `0.008488`, median `0.015416`, mae `0.025761`
- 60d: sample `20`, hit `0.65`, avg `0.022555`, median `0.046407`, mae `0.048128`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.006261`, median `-0.000285`, mae `0.015689`
- 5d: sample `40`, hit `0.4`, avg `-0.009411`, median `-0.006464`, mae `0.017711`
- 10d: sample `40`, hit `0.35`, avg `-0.005415`, median `-0.007491`, mae `0.017872`
- 20d: sample `40`, hit `0.575`, avg `0.011282`, median `0.01927`, mae `0.032887`
- 60d: sample `40`, hit `0.675`, avg `0.031497`, median `0.053855`, mae `0.066194`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003754`, median `0.000766`, mae `0.01237`
- 5d: sample `20`, hit `0.45`, avg `-0.00489`, median `-0.000513`, mae `0.014016`
- 10d: sample `20`, hit `0.45`, avg `-0.002824`, median `-0.007314`, mae `0.017702`
- 20d: sample `20`, hit `0.5`, avg `0.008488`, median `0.015416`, mae `0.025761`
- 60d: sample `20`, hit `0.65`, avg `0.022555`, median `0.046407`, mae `0.048128`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.006261`, median `-0.000285`, mae `0.015689`
- 5d: sample `40`, hit `0.4`, avg `-0.009411`, median `-0.006464`, mae `0.017711`
- 10d: sample `40`, hit `0.35`, avg `-0.005415`, median `-0.007491`, mae `0.017872`
- 20d: sample `40`, hit `0.575`, avg `0.011282`, median `0.01927`, mae `0.032887`
- 60d: sample `40`, hit `0.675`, avg `0.031497`, median `0.053855`, mae `0.066194`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.008152`, median `-0.009843`, mae `0.016153`
- 5d: sample `40`, hit `0.35`, avg `-0.009741`, median `-0.013229`, mae `0.021025`
- 10d: sample `40`, hit `0.375`, avg `-0.011277`, median `-0.015101`, mae `0.029176`
- 20d: sample `40`, hit `0.675`, avg `0.023412`, median `0.018431`, mae `0.038514`
- 60d: sample `40`, hit `0.85`, avg `0.074646`, median `0.079528`, mae `0.085051`

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
- 3d: sample `20`, hit `0.55`, avg `-0.003754`, median `0.000766`, mae `0.01237`
- 5d: sample `20`, hit `0.45`, avg `-0.00489`, median `-0.000513`, mae `0.014016`
- 10d: sample `20`, hit `0.45`, avg `-0.002824`, median `-0.007314`, mae `0.017702`
- 20d: sample `20`, hit `0.5`, avg `0.008488`, median `0.015416`, mae `0.025761`
- 60d: sample `20`, hit `0.65`, avg `0.022555`, median `0.046407`, mae `0.048128`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.007207`, median `-0.007923`, mae `0.015921`
- 5d: sample `80`, hit `0.375`, avg `-0.009576`, median `-0.011804`, mae `0.019368`
- 10d: sample `80`, hit `0.3625`, avg `-0.008346`, median `-0.01051`, mae `0.023524`
- 20d: sample `80`, hit `0.625`, avg `0.017347`, median `0.018431`, mae `0.035701`
- 60d: sample `80`, hit `0.7625`, avg `0.053071`, median `0.059495`, mae `0.075623`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003754`, median `0.000766`, mae `0.01237`
- 5d: sample `20`, hit `0.45`, avg `-0.00489`, median `-0.000513`, mae `0.014016`
- 10d: sample `20`, hit `0.45`, avg `-0.002824`, median `-0.007314`, mae `0.017702`
- 20d: sample `20`, hit `0.5`, avg `0.008488`, median `0.015416`, mae `0.025761`
- 60d: sample `20`, hit `0.65`, avg `0.022555`, median `0.046407`, mae `0.048128`

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
