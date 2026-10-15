# High Confidence Edge Report

Generated at: `2026-10-15T05:58:16.378194+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `104`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `104`, gate `stronger_evidence`
- 5d: completed `104`, gate `stronger_evidence`
- 10d: completed `104`, gate `stronger_evidence`
- 20d: completed `104`, gate `stronger_evidence`
- 60d: completed `104`, gate `stronger_evidence`

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
- 3d: sample `40`, hit `0.475`, avg `-0.005894`, median `-0.001658`, mae `0.01652`
- 5d: sample `40`, hit `0.45`, avg `-0.010436`, median `-0.010073`, mae `0.019136`
- 10d: sample `40`, hit `0.4`, avg `-0.005031`, median `-0.006933`, mae `0.018999`
- 20d: sample `40`, hit `0.625`, avg `0.013728`, median `0.01983`, mae `0.030711`
- 60d: sample `40`, hit `0.75`, avg `0.036857`, median `0.053855`, mae `0.067104`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009173`, median `-0.013524`, mae `0.018949`
- 5d: sample `20`, hit `0.4`, avg `-0.006805`, median `-0.009879`, mae `0.018402`
- 10d: sample `20`, hit `0.55`, avg `0.000736`, median `0.003262`, mae `0.02036`
- 20d: sample `20`, hit `0.75`, avg `0.023116`, median `0.02093`, mae `0.029945`
- 60d: sample `20`, hit `0.8`, avg `0.077188`, median `0.0765`, mae `0.096541`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.011745`, median `-0.010273`, mae `0.01435`
- 5d: sample `20`, hit `0.2`, avg `-0.018067`, median `-0.021517`, mae `0.022421`
- 10d: sample `20`, hit `0.25`, avg `-0.020527`, median `-0.034842`, mae `0.040017`
- 20d: sample `20`, hit `0.45`, avg `0.013366`, median `-0.00018`, mae `0.04779`
- 60d: sample `20`, hit `0.9`, avg `0.079642`, median `0.092689`, mae `0.090342`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.00704`, median `-0.001658`, mae `0.020286`
- 5d: sample `8`, hit `0.5`, avg `-0.006894`, median `0.005072`, mae `0.019191`
- 10d: sample `8`, hit `0.25`, avg `-0.00497`, median `-0.006017`, mae `0.015872`
- 20d: sample `8`, hit `0.875`, avg `0.044382`, median `0.058396`, mae `0.044798`
- 60d: sample `8`, hit `1.0`, avg `0.09719`, median `0.121826`, mae `0.09719`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.00704`, median `-0.001658`, mae `0.020286`
- 5d: sample `8`, hit `0.5`, avg `-0.006894`, median `0.005072`, mae `0.019191`
- 10d: sample `8`, hit `0.25`, avg `-0.00497`, median `-0.006017`, mae `0.015872`
- 20d: sample `8`, hit `0.875`, avg `0.044382`, median `0.058396`, mae `0.044798`
- 60d: sample `8`, hit `1.0`, avg `0.09719`, median `0.121826`, mae `0.09719`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.005894, 'median_return': -0.001658, 'mean_absolute_return': 0.01652, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.010436, 'median_return': -0.010073, 'mean_absolute_return': 0.019136, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.005031, 'median_return': -0.006933, 'mean_absolute_return': 0.018999, 'max_adverse_excursion': -0.062837, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.013728, 'median_return': 0.01983, 'mean_absolute_return': 0.030711, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.036857, 'median_return': 0.053855, 'mean_absolute_return': 0.067104, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.00704, 'median_return': -0.001658, 'mean_absolute_return': 0.020286, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006894, 'median_return': 0.005072, 'mean_absolute_return': 0.019191, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00497, 'median_return': -0.006017, 'mean_absolute_return': 0.015872, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.044382, 'median_return': 0.058396, 'mean_absolute_return': 0.044798, 'max_adverse_excursion': -0.001666, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.09719, 'median_return': 0.121826, 'mean_absolute_return': 0.09719, 'max_adverse_excursion': 0.037425, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.008303, 'median_return': -0.009843, 'mean_absolute_return': 0.016173, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 72, 'hit_rate': 0.3611, 'avg_return': -0.011941, 'median_return': -0.014596, 'mean_absolute_return': 0.019838, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.007741, 'median_return': -0.009464, 'mean_absolute_return': 0.025563, 'max_adverse_excursion': -0.062837, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.012829, 'median_return': 0.015416, 'mean_absolute_return': 0.033677, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.053241, 'median_return': 0.059131, 'mean_absolute_return': 0.078393, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.625}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.2}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.6, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.005894, 'median_return': -0.001658, 'mean_absolute_return': 0.01652, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.010436, 'median_return': -0.010073, 'mean_absolute_return': 0.019136, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.005031, 'median_return': -0.006933, 'mean_absolute_return': 0.018999, 'max_adverse_excursion': -0.062837, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.013728, 'median_return': 0.01983, 'mean_absolute_return': 0.030711, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.036857, 'median_return': 0.053855, 'mean_absolute_return': 0.067104, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.3, 'avg_return': -0.010459, 'median_return': -0.011068, 'mean_absolute_return': 0.016649, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.019015}, '5d': {'sample_size': 40, 'hit_rate': 0.3, 'avg_return': -0.012436, 'median_return': -0.014596, 'mean_absolute_return': 0.020412, 'max_adverse_excursion': -0.043999, 'max_favorable_excursion': 0.026734}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.009896, 'median_return': -0.014015, 'mean_absolute_return': 0.030189, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.018241, 'median_return': 0.015713, 'mean_absolute_return': 0.038867, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.078415, 'median_return': 0.079633, 'mean_absolute_return': 0.093442, 'max_adverse_excursion': -0.12745, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.005894`, median `-0.001658`, mae `0.01652`
- 5d: sample `40`, hit `0.45`, avg `-0.010436`, median `-0.010073`, mae `0.019136`
- 10d: sample `40`, hit `0.4`, avg `-0.005031`, median `-0.006933`, mae `0.018999`
- 20d: sample `40`, hit `0.625`, avg `0.013728`, median `0.01983`, mae `0.030711`
- 60d: sample `40`, hit `0.75`, avg `0.036857`, median `0.053855`, mae `0.067104`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.010459`, median `-0.011068`, mae `0.016649`
- 5d: sample `40`, hit `0.3`, avg `-0.012436`, median `-0.014596`, mae `0.020412`
- 10d: sample `40`, hit `0.4`, avg `-0.009896`, median `-0.014015`, mae `0.030189`
- 20d: sample `40`, hit `0.6`, avg `0.018241`, median `0.015713`, mae `0.038867`
- 60d: sample `40`, hit `0.85`, avg `0.078415`, median `0.079633`, mae `0.093442`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.005894`, median `-0.001658`, mae `0.01652`
- 5d: sample `40`, hit `0.45`, avg `-0.010436`, median `-0.010073`, mae `0.019136`
- 10d: sample `40`, hit `0.4`, avg `-0.005031`, median `-0.006933`, mae `0.018999`
- 20d: sample `40`, hit `0.625`, avg `0.013728`, median `0.01983`, mae `0.030711`
- 60d: sample `40`, hit `0.75`, avg `0.036857`, median `0.053855`, mae `0.067104`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.005894`, median `-0.001658`, mae `0.01652`
- 5d: sample `40`, hit `0.45`, avg `-0.010436`, median `-0.010073`, mae `0.019136`
- 10d: sample `40`, hit `0.4`, avg `-0.005031`, median `-0.006933`, mae `0.018999`
- 20d: sample `40`, hit `0.625`, avg `0.013728`, median `0.01983`, mae `0.030711`
- 60d: sample `40`, hit `0.75`, avg `0.036857`, median `0.053855`, mae `0.067104`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.010459`, median `-0.011068`, mae `0.016649`
- 5d: sample `40`, hit `0.3`, avg `-0.012436`, median `-0.014596`, mae `0.020412`
- 10d: sample `40`, hit `0.4`, avg `-0.009896`, median `-0.014015`, mae `0.030189`
- 20d: sample `40`, hit `0.6`, avg `0.018241`, median `0.015713`, mae `0.038867`
- 60d: sample `40`, hit `0.85`, avg `0.078415`, median `0.079633`, mae `0.093442`

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
- 3d: sample `80`, hit `0.3875`, avg `-0.008176`, median `-0.009843`, mae `0.016585`
- 5d: sample `80`, hit `0.375`, avg `-0.011436`, median `-0.014596`, mae `0.019774`
- 10d: sample `80`, hit `0.4`, avg `-0.007464`, median `-0.009464`, mae `0.024594`
- 20d: sample `80`, hit `0.6125`, avg `0.015984`, median `0.018431`, mae `0.034789`
- 60d: sample `80`, hit `0.8`, avg `0.057636`, median `0.059948`, mae `0.080273`

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
