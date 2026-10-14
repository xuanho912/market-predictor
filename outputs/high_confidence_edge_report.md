# High Confidence Edge Report

Generated at: `2026-10-14T17:14:59.826701+00:00`

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
- 3d: sample `40`, hit `0.45`, avg `-0.006483`, median `-0.002755`, mae `0.017079`
- 5d: sample `40`, hit `0.425`, avg `-0.011464`, median `-0.010073`, mae `0.019933`
- 10d: sample `40`, hit `0.35`, avg `-0.008689`, median `-0.007491`, mae `0.020577`
- 20d: sample `40`, hit `0.575`, avg `0.009985`, median `0.016745`, mae `0.03245`
- 60d: sample `40`, hit `0.75`, avg `0.036815`, median `0.053855`, mae `0.067062`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.00827`, median `-0.013524`, mae `0.019952`
- 5d: sample `20`, hit `0.45`, avg `-0.004971`, median `-0.002776`, mae `0.018736`
- 10d: sample `20`, hit `0.55`, avg `0.0007`, median `0.003262`, mae `0.019022`
- 20d: sample `20`, hit `0.7`, avg `0.022395`, median `0.02093`, mae `0.03014`
- 60d: sample `20`, hit `0.85`, avg `0.087076`, median `0.106573`, mae `0.102386`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.15`, avg `-0.011039`, median `-0.011068`, mae `0.016124`
- 5d: sample `20`, hit `0.15`, avg `-0.01653`, median `-0.020895`, mae `0.022193`
- 10d: sample `20`, hit `0.3`, avg `-0.018576`, median `-0.037229`, mae `0.044689`
- 20d: sample `20`, hit `0.4`, avg `0.009553`, median `-0.00045`, mae `0.044948`
- 60d: sample `20`, hit `0.9`, avg `0.075711`, median `0.079633`, mae `0.086411`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.006483, 'median_return': -0.002755, 'mean_absolute_return': 0.017079, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.011464, 'median_return': -0.010073, 'mean_absolute_return': 0.019933, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.008689, 'median_return': -0.007491, 'mean_absolute_return': 0.020577, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.009985, 'median_return': 0.016745, 'mean_absolute_return': 0.03245, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.036815, 'median_return': 0.053855, 'mean_absolute_return': 0.067062, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.00704, 'median_return': -0.001658, 'mean_absolute_return': 0.020286, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006894, 'median_return': 0.005072, 'mean_absolute_return': 0.019191, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00497, 'median_return': -0.006017, 'mean_absolute_return': 0.015872, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.044382, 'median_return': 0.058396, 'mean_absolute_return': 0.044798, 'max_adverse_excursion': -0.001666, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.09719, 'median_return': 0.121826, 'mean_absolute_return': 0.09719, 'max_adverse_excursion': 0.037425, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3611, 'avg_return': -0.008183, 'median_return': -0.010273, 'mean_absolute_return': 0.017255, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.3472, 'avg_return': -0.011575, 'median_return': -0.013229, 'mean_absolute_return': 0.020311, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.00924, 'median_return': -0.010145, 'mean_absolute_return': 0.027366, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.009491, 'median_return': 0.002759, 'mean_absolute_return': 0.033908, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.054872, 'median_return': 0.059131, 'mean_absolute_return': 0.078901, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.1875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.275, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.275, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_minus_secondary': -0.625, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.006483, 'median_return': -0.002755, 'mean_absolute_return': 0.017079, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.011464, 'median_return': -0.010073, 'mean_absolute_return': 0.019933, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.008689, 'median_return': -0.007491, 'mean_absolute_return': 0.020577, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.009985, 'median_return': 0.016745, 'mean_absolute_return': 0.03245, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.036815, 'median_return': 0.053855, 'mean_absolute_return': 0.067062, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.275, 'avg_return': -0.009655, 'median_return': -0.013218, 'mean_absolute_return': 0.018038, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.3, 'avg_return': -0.01075, 'median_return': -0.013229, 'mean_absolute_return': 0.020465, 'max_adverse_excursion': -0.043999, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.008938, 'median_return': -0.01314, 'mean_absolute_return': 0.031856, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.015974, 'median_return': 0.01128, 'mean_absolute_return': 0.037544, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.081393, 'median_return': 0.079633, 'mean_absolute_return': 0.094398, 'max_adverse_excursion': -0.12745, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.006483`, median `-0.002755`, mae `0.017079`
- 5d: sample `40`, hit `0.425`, avg `-0.011464`, median `-0.010073`, mae `0.019933`
- 10d: sample `40`, hit `0.35`, avg `-0.008689`, median `-0.007491`, mae `0.020577`
- 20d: sample `40`, hit `0.575`, avg `0.009985`, median `0.016745`, mae `0.03245`
- 60d: sample `40`, hit `0.75`, avg `0.036815`, median `0.053855`, mae `0.067062`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.275`, avg `-0.009655`, median `-0.013218`, mae `0.018038`
- 5d: sample `40`, hit `0.3`, avg `-0.01075`, median `-0.013229`, mae `0.020465`
- 10d: sample `40`, hit `0.425`, avg `-0.008938`, median `-0.01314`, mae `0.031856`
- 20d: sample `40`, hit `0.55`, avg `0.015974`, median `0.01128`, mae `0.037544`
- 60d: sample `40`, hit `0.875`, avg `0.081393`, median `0.079633`, mae `0.094398`

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
- 3d: sample `40`, hit `0.45`, avg `-0.006483`, median `-0.002755`, mae `0.017079`
- 5d: sample `40`, hit `0.425`, avg `-0.011464`, median `-0.010073`, mae `0.019933`
- 10d: sample `40`, hit `0.35`, avg `-0.008689`, median `-0.007491`, mae `0.020577`
- 20d: sample `40`, hit `0.575`, avg `0.009985`, median `0.016745`, mae `0.03245`
- 60d: sample `40`, hit `0.75`, avg `0.036815`, median `0.053855`, mae `0.067062`

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
- 3d: sample `40`, hit `0.45`, avg `-0.006483`, median `-0.002755`, mae `0.017079`
- 5d: sample `40`, hit `0.425`, avg `-0.011464`, median `-0.010073`, mae `0.019933`
- 10d: sample `40`, hit `0.35`, avg `-0.008689`, median `-0.007491`, mae `0.020577`
- 20d: sample `40`, hit `0.575`, avg `0.009985`, median `0.016745`, mae `0.03245`
- 60d: sample `40`, hit `0.75`, avg `0.036815`, median `0.053855`, mae `0.067062`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.275`, avg `-0.009655`, median `-0.013218`, mae `0.018038`
- 5d: sample `40`, hit `0.3`, avg `-0.01075`, median `-0.013229`, mae `0.020465`
- 10d: sample `40`, hit `0.425`, avg `-0.008938`, median `-0.01314`, mae `0.031856`
- 20d: sample `40`, hit `0.55`, avg `0.015974`, median `0.01128`, mae `0.037544`
- 60d: sample `40`, hit `0.875`, avg `0.081393`, median `0.079633`, mae `0.094398`

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
- 3d: sample `80`, hit `0.3625`, avg `-0.008069`, median `-0.010094`, mae `0.017558`
- 5d: sample `80`, hit `0.3625`, avg `-0.011107`, median `-0.013229`, mae `0.020199`
- 10d: sample `80`, hit `0.3875`, avg `-0.008813`, median `-0.010145`, mae `0.026216`
- 20d: sample `80`, hit `0.5625`, avg `0.01298`, median `0.015416`, mae `0.034997`
- 60d: sample `80`, hit `0.8125`, avg `0.059104`, median `0.059948`, mae `0.08073`

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
