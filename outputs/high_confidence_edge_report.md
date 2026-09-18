# High Confidence Edge Report

Generated at: `2026-09-18T23:35:55.765011+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `32`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `32`, gate `early_evidence`
- 5d: completed `32`, gate `early_evidence`
- 10d: completed `32`, gate `early_evidence`
- 20d: completed `32`, gate `early_evidence`
- 60d: completed `32`, gate `early_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `-0.003042`, median `0.002101`, mae `0.01648`
- 5d: sample `60`, hit `0.55`, avg `-0.005896`, median `0.001104`, mae `0.018862`
- 10d: sample `60`, hit `0.4667`, avg `-0.002354`, median `-0.004767`, mae `0.020318`
- 20d: sample `60`, hit `0.6167`, avg `0.01406`, median `0.015725`, mae `0.032027`
- 60d: sample `60`, hit `0.75`, avg `0.037455`, median `0.053855`, mae `0.064449`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.01034`, median `-0.008838`, mae `0.017579`
- 5d: sample `20`, hit `0.15`, avg `-0.018347`, median `-0.017697`, mae `0.025774`
- 10d: sample `20`, hit `0.2`, avg `-0.030129`, median `-0.037905`, mae `0.042549`
- 20d: sample `20`, hit `0.35`, avg `-0.013419`, median `-0.011553`, mae `0.049732`
- 60d: sample `20`, hit `0.65`, avg `0.007643`, median `0.050036`, mae `0.090108`

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
- 3d: sample `8`, hit `0.75`, avg `0.011118`, median `0.012573`, mae `0.014543`
- 5d: sample `8`, hit `0.625`, avg `-0.00482`, median `0.001104`, mae `0.013369`
- 10d: sample `8`, hit `0.375`, avg `-0.005498`, median `-0.006389`, mae `0.014961`
- 20d: sample `8`, hit `0.5`, avg `-0.003211`, median `0.001268`, mae `0.01353`
- 60d: sample `8`, hit `0.625`, avg `0.003417`, median `0.020144`, mae `0.04004`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.00704`, median `-0.001658`, mae `0.020286`
- 5d: sample `8`, hit `0.5`, avg `-0.006894`, median `0.005072`, mae `0.019191`
- 10d: sample `8`, hit `0.25`, avg `-0.00497`, median `-0.006017`, mae `0.015872`
- 20d: sample `8`, hit `0.875`, avg `0.044382`, median `0.058396`, mae `0.044798`
- 60d: sample `8`, hit `1.0`, avg `0.09719`, median `0.121826`, mae `0.09719`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.003042, 'median_return': 0.002101, 'mean_absolute_return': 0.01648, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.005896, 'median_return': 0.001104, 'mean_absolute_return': 0.018862, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.002354, 'median_return': -0.004767, 'mean_absolute_return': 0.020318, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.01406, 'median_return': 0.015725, 'mean_absolute_return': 0.032027, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.037455, 'median_return': 0.053855, 'mean_absolute_return': 0.064449, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.00704, 'median_return': -0.001658, 'mean_absolute_return': 0.020286, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006894, 'median_return': 0.005072, 'mean_absolute_return': 0.019191, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00497, 'median_return': -0.006017, 'mean_absolute_return': 0.015872, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.044382, 'median_return': 0.058396, 'mean_absolute_return': 0.044798, 'max_adverse_excursion': -0.001666, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.09719, 'median_return': 0.121826, 'mean_absolute_return': 0.09719, 'max_adverse_excursion': 0.037425, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.004625, 'median_return': -0.0002, 'mean_absolute_return': 0.016363, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.009244, 'median_return': -0.006464, 'mean_absolute_return': 0.020745, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.009779, 'median_return': -0.009882, 'mean_absolute_return': 0.026987, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.003058, 'median_return': 0.001268, 'mean_absolute_return': 0.035526, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.022537, 'median_return': 0.044771, 'mean_absolute_return': 0.067939, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.275}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.003042, 'median_return': 0.002101, 'mean_absolute_return': 0.01648, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.005896, 'median_return': 0.001104, 'mean_absolute_return': 0.018862, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.002354, 'median_return': -0.004767, 'mean_absolute_return': 0.020318, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.01406, 'median_return': 0.015725, 'mean_absolute_return': 0.032027, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.037455, 'median_return': 0.053855, 'mean_absolute_return': 0.064449, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.01034, 'median_return': -0.008838, 'mean_absolute_return': 0.017579, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.018347, 'median_return': -0.017697, 'mean_absolute_return': 0.025774, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.030129, 'median_return': -0.037905, 'mean_absolute_return': 0.042549, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.013419, 'median_return': -0.011553, 'mean_absolute_return': 0.049732, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.086975}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.007643, 'median_return': 0.050036, 'mean_absolute_return': 0.090108, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.004867`, median `-0.001058`, mae `0.016755`
- 5d: sample `80`, hit `0.45`, avg `-0.009009`, median `-0.006464`, mae `0.02059`
- 10d: sample `80`, hit `0.4`, avg `-0.009298`, median `-0.009882`, mae `0.025875`
- 20d: sample `80`, hit `0.55`, avg `0.007191`, median `0.010824`, mae `0.036453`
- 60d: sample `80`, hit `0.725`, avg `0.030002`, median `0.050036`, mae `0.070864`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.006593`, median `-0.001641`, mae `0.016635`
- 5d: sample `40`, hit `0.45`, avg `-0.00952`, median `-0.006464`, mae `0.019262`
- 10d: sample `40`, hit `0.4`, avg `-0.00503`, median `-0.007011`, mae `0.018686`
- 20d: sample `40`, hit `0.65`, avg `0.016413`, median `0.02865`, mae `0.034644`
- 60d: sample `40`, hit `0.75`, avg `0.039507`, median `0.059131`, mae `0.068815`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.004867`, median `-0.001058`, mae `0.016755`
- 5d: sample `80`, hit `0.45`, avg `-0.009009`, median `-0.006464`, mae `0.02059`
- 10d: sample `80`, hit `0.4`, avg `-0.009298`, median `-0.009882`, mae `0.025875`
- 20d: sample `80`, hit `0.55`, avg `0.007191`, median `0.010824`, mae `0.036453`
- 60d: sample `80`, hit `0.725`, avg `0.030002`, median `0.050036`, mae `0.070864`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.004867`, median `-0.001058`, mae `0.016755`
- 5d: sample `80`, hit `0.45`, avg `-0.009009`, median `-0.006464`, mae `0.02059`
- 10d: sample `80`, hit `0.4`, avg `-0.009298`, median `-0.009882`, mae `0.025875`
- 20d: sample `80`, hit `0.55`, avg `0.007191`, median `0.010824`, mae `0.036453`
- 60d: sample `80`, hit `0.725`, avg `0.030002`, median `0.050036`, mae `0.070864`

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
