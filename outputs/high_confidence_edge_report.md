# High Confidence Edge Report

Generated at: `2026-10-13T03:17:10.467976+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `96`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `96`, gate `moderate_evidence`
- 5d: completed `96`, gate `moderate_evidence`
- 10d: completed `96`, gate `moderate_evidence`
- 20d: completed `96`, gate `moderate_evidence`
- 60d: completed `96`, gate `moderate_evidence`

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
- 3d: sample `60`, hit `0.3667`, avg `-0.008588`, median `-0.010033`, mae `0.018332`
- 5d: sample `60`, hit `0.4167`, avg `-0.011773`, median `-0.014596`, mae `0.021539`
- 10d: sample `60`, hit `0.3833`, avg `-0.009846`, median `-0.007314`, mae `0.019785`
- 20d: sample `60`, hit `0.7`, avg `0.013603`, median `0.018431`, mae `0.031154`
- 60d: sample `60`, hit `0.7667`, avg `0.045958`, median `0.053855`, mae `0.072593`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.1`, avg `-0.014013`, median `-0.010273`, mae `0.019343`
- 5d: sample `20`, hit `0.15`, avg `-0.01978`, median `-0.020895`, mae `0.025444`
- 10d: sample `20`, hit `0.35`, avg `-0.013922`, median `-0.032571`, mae `0.04421`
- 20d: sample `20`, hit `0.55`, avg `0.024568`, median `0.039427`, mae `0.05771`
- 60d: sample `20`, hit `0.85`, avg `0.073998`, median `0.092008`, mae `0.082643`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.016807`, median `-0.030499`, mae `0.024878`
- 5d: sample `8`, hit `0.375`, avg `-0.01718`, median `-0.016421`, mae `0.022862`
- 10d: sample `8`, hit `0.25`, avg `-0.012488`, median `-0.011432`, mae `0.015647`
- 20d: sample `8`, hit `0.75`, avg `0.014597`, median `0.029166`, mae `0.044724`
- 60d: sample `8`, hit `0.875`, avg `0.053341`, median `0.072696`, mae `0.088622`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.016807`, median `-0.030499`, mae `0.024878`
- 5d: sample `8`, hit `0.375`, avg `-0.01718`, median `-0.016421`, mae `0.022862`
- 10d: sample `8`, hit `0.25`, avg `-0.012488`, median `-0.011432`, mae `0.015647`
- 20d: sample `8`, hit `0.75`, avg `0.014597`, median `0.029166`, mae `0.044724`
- 60d: sample `8`, hit `0.875`, avg `0.053341`, median `0.072696`, mae `0.088622`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.008588, 'median_return': -0.010033, 'mean_absolute_return': 0.018332, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.011773, 'median_return': -0.014596, 'mean_absolute_return': 0.021539, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.009846, 'median_return': -0.007314, 'mean_absolute_return': 0.019785, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.047243}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.013603, 'median_return': 0.018431, 'mean_absolute_return': 0.031154, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076702}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.045958, 'median_return': 0.053855, 'mean_absolute_return': 0.072593, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.19082}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.016807, 'median_return': -0.030499, 'mean_absolute_return': 0.024878, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.01718, 'median_return': -0.016421, 'mean_absolute_return': 0.022862, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.012488, 'median_return': -0.011432, 'mean_absolute_return': 0.015647, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.011031}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.014597, 'median_return': 0.029166, 'mean_absolute_return': 0.044724, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.053341, 'median_return': 0.072696, 'mean_absolute_return': 0.088622, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3056, 'avg_return': -0.009181, 'median_return': -0.010033, 'mean_absolute_return': 0.017886, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.3472, 'avg_return': -0.013396, 'median_return': -0.015413, 'mean_absolute_return': 0.022477, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.010685, 'median_return': -0.010456, 'mean_absolute_return': 0.027029, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.016538, 'median_return': 0.016027, 'mean_absolute_return': 0.037023, 'max_adverse_excursion': -0.090946, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.052927, 'median_return': 0.059007, 'mean_absolute_return': 0.073604, 'max_adverse_excursion': -0.134617, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.4375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.010619, 'median_return': -0.010094, 'mean_absolute_return': 0.019293, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.015603, 'median_return': -0.017712, 'mean_absolute_return': 0.023303, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.013631, 'median_return': -0.010456, 'mean_absolute_return': 0.021881, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.00802, 'median_return': 0.016745, 'mean_absolute_return': 0.033925, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.031802, 'median_return': 0.050438, 'mean_absolute_return': 0.06851, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.275, 'avg_return': -0.009269, 'median_return': -0.010023, 'mean_absolute_return': 0.017877, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.011946, 'median_return': -0.013446, 'mean_absolute_return': 0.021727, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.008099, 'median_return': -0.012317, 'mean_absolute_return': 0.029901, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.024668, 'median_return': 0.02093, 'mean_absolute_return': 0.041661, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.074134, 'median_return': 0.077304, 'mean_absolute_return': 0.081701, 'max_adverse_excursion': -0.058227, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.010619`, median `-0.010094`, mae `0.019293`
- 5d: sample `40`, hit `0.35`, avg `-0.015603`, median `-0.017712`, mae `0.023303`
- 10d: sample `40`, hit `0.325`, avg `-0.013631`, median `-0.010456`, mae `0.021881`
- 20d: sample `40`, hit `0.6`, avg `0.00802`, median `0.016745`, mae `0.033925`
- 60d: sample `40`, hit `0.725`, avg `0.031802`, median `0.050438`, mae `0.06851`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.275`, avg `-0.009269`, median `-0.010023`, mae `0.017877`
- 5d: sample `40`, hit `0.35`, avg `-0.011946`, median `-0.013446`, mae `0.021727`
- 10d: sample `40`, hit `0.425`, avg `-0.008099`, median `-0.012317`, mae `0.029901`
- 20d: sample `40`, hit `0.725`, avg `0.024668`, median `0.02093`, mae `0.041661`
- 60d: sample `40`, hit `0.85`, avg `0.074134`, median `0.077304`, mae `0.081701`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.010619`, median `-0.010094`, mae `0.019293`
- 5d: sample `40`, hit `0.35`, avg `-0.015603`, median `-0.017712`, mae `0.023303`
- 10d: sample `40`, hit `0.325`, avg `-0.013631`, median `-0.010456`, mae `0.021881`
- 20d: sample `40`, hit `0.6`, avg `0.00802`, median `0.016745`, mae `0.033925`
- 60d: sample `40`, hit `0.725`, avg `0.031802`, median `0.050438`, mae `0.06851`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.010619`, median `-0.010094`, mae `0.019293`
- 5d: sample `40`, hit `0.35`, avg `-0.015603`, median `-0.017712`, mae `0.023303`
- 10d: sample `40`, hit `0.325`, avg `-0.013631`, median `-0.010456`, mae `0.021881`
- 20d: sample `40`, hit `0.6`, avg `0.00802`, median `0.016745`, mae `0.033925`
- 60d: sample `40`, hit `0.725`, avg `0.031802`, median `0.050438`, mae `0.06851`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.010619`, median `-0.010094`, mae `0.019293`
- 5d: sample `40`, hit `0.35`, avg `-0.015603`, median `-0.017712`, mae `0.023303`
- 10d: sample `40`, hit `0.325`, avg `-0.013631`, median `-0.010456`, mae `0.021881`
- 20d: sample `40`, hit `0.6`, avg `0.00802`, median `0.016745`, mae `0.033925`
- 60d: sample `40`, hit `0.725`, avg `0.031802`, median `0.050438`, mae `0.06851`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.010619`, median `-0.010094`, mae `0.019293`
- 5d: sample `40`, hit `0.35`, avg `-0.015603`, median `-0.017712`, mae `0.023303`
- 10d: sample `40`, hit `0.325`, avg `-0.013631`, median `-0.010456`, mae `0.021881`
- 20d: sample `40`, hit `0.6`, avg `0.00802`, median `0.016745`, mae `0.033925`
- 60d: sample `40`, hit `0.725`, avg `0.031802`, median `0.050438`, mae `0.06851`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.275`, avg `-0.009269`, median `-0.010023`, mae `0.017877`
- 5d: sample `40`, hit `0.35`, avg `-0.011946`, median `-0.013446`, mae `0.021727`
- 10d: sample `40`, hit `0.425`, avg `-0.008099`, median `-0.012317`, mae `0.029901`
- 20d: sample `40`, hit `0.725`, avg `0.024668`, median `0.02093`, mae `0.041661`
- 60d: sample `40`, hit `0.85`, avg `0.074134`, median `0.077304`, mae `0.081701`

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
- 3d: sample `80`, hit `0.3`, avg `-0.009944`, median `-0.010094`, mae `0.018585`
- 5d: sample `80`, hit `0.35`, avg `-0.013774`, median `-0.016062`, mae `0.022515`
- 10d: sample `80`, hit `0.375`, avg `-0.010865`, median `-0.011432`, mae `0.025891`
- 20d: sample `80`, hit `0.6625`, avg `0.016344`, median `0.018431`, mae `0.037793`
- 60d: sample `80`, hit `0.7875`, avg `0.052968`, median `0.059104`, mae `0.075105`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.010619`, median `-0.010094`, mae `0.019293`
- 5d: sample `40`, hit `0.35`, avg `-0.015603`, median `-0.017712`, mae `0.023303`
- 10d: sample `40`, hit `0.325`, avg `-0.013631`, median `-0.010456`, mae `0.021881`
- 20d: sample `40`, hit `0.6`, avg `0.00802`, median `0.016745`, mae `0.033925`
- 60d: sample `40`, hit `0.725`, avg `0.031802`, median `0.050438`, mae `0.06851`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.008634`, median `-0.003995`, mae `0.017606`
- 5d: sample `20`, hit `0.4`, avg `-0.012383`, median `-0.015413`, mae `0.021424`
- 10d: sample `20`, hit `0.45`, avg `-0.011103`, median `-0.006933`, mae `0.021158`
- 20d: sample `20`, hit `0.6`, avg `0.008818`, median `0.015416`, mae `0.027894`
- 60d: sample `20`, hit `0.75`, avg `0.03062`, median `0.046407`, mae `0.052303`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.008634`, median `-0.003995`, mae `0.017606`
- 5d: sample `20`, hit `0.4`, avg `-0.012383`, median `-0.015413`, mae `0.021424`
- 10d: sample `20`, hit `0.45`, avg `-0.011103`, median `-0.006933`, mae `0.021158`
- 20d: sample `20`, hit `0.6`, avg `0.008818`, median `0.015416`, mae `0.027894`
- 60d: sample `20`, hit `0.75`, avg `0.03062`, median `0.046407`, mae `0.052303`

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
