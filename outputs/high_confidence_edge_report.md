# High Confidence Edge Report

Generated at: `2026-10-14T06:13:45.191734+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `100`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `100`, gate `moderate_evidence`
- 5d: completed `100`, gate `moderate_evidence`
- 10d: completed `100`, gate `moderate_evidence`
- 20d: completed `100`, gate `moderate_evidence`
- 60d: completed `100`, gate `moderate_evidence`

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
- 3d: sample `40`, hit `0.425`, avg `-0.007474`, median `-0.003244`, mae `0.017271`
- 5d: sample `40`, hit `0.425`, avg `-0.010743`, median `-0.016062`, mae `0.021655`
- 10d: sample `40`, hit `0.35`, avg `-0.012662`, median `-0.010456`, mae `0.022444`
- 20d: sample `40`, hit `0.6`, avg `0.00677`, median `0.015416`, mae `0.032556`
- 60d: sample `40`, hit `0.675`, avg `0.017781`, median `0.050438`, mae `0.074206`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.005008`, median `-0.00402`, mae `0.015742`
- 5d: sample `40`, hit `0.375`, avg `-0.009917`, median `-0.013229`, mae `0.020692`
- 10d: sample `40`, hit `0.4`, avg `-0.00903`, median `-0.014005`, mae `0.028181`
- 20d: sample `40`, hit `0.6`, avg `0.020114`, median `0.015713`, mae `0.039595`
- 60d: sample `40`, hit `0.8`, avg `0.054695`, median `0.059007`, mae `0.067101`

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
- 3d: sample `8`, hit `0.25`, avg `-0.016625`, median `-0.030499`, mae `0.025059`
- 5d: sample `8`, hit `0.375`, avg `-0.014933`, median `-0.016421`, mae `0.025109`
- 10d: sample `8`, hit `0.25`, avg `-0.010376`, median `-0.011432`, mae `0.017759`
- 20d: sample `8`, hit `0.75`, avg `0.007481`, median `0.026113`, mae `0.037607`
- 60d: sample `8`, hit `0.75`, avg `0.018653`, median `0.059131`, mae `0.090609`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.016625`, median `-0.030499`, mae `0.025059`
- 5d: sample `8`, hit `0.375`, avg `-0.014933`, median `-0.016421`, mae `0.025109`
- 10d: sample `8`, hit `0.25`, avg `-0.010376`, median `-0.011432`, mae `0.017759`
- 20d: sample `8`, hit `0.75`, avg `0.007481`, median `0.026113`, mae `0.037607`
- 60d: sample `8`, hit `0.75`, avg `0.018653`, median `0.059131`, mae `0.090609`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.007474, 'median_return': -0.003244, 'mean_absolute_return': 0.017271, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.010743, 'median_return': -0.016062, 'mean_absolute_return': 0.021655, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.012662, 'median_return': -0.010456, 'mean_absolute_return': 0.022444, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.00677, 'median_return': 0.015416, 'mean_absolute_return': 0.032556, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.017781, 'median_return': 0.050438, 'mean_absolute_return': 0.074206, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.016625, 'median_return': -0.030499, 'mean_absolute_return': 0.025059, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.014933, 'median_return': -0.016421, 'mean_absolute_return': 0.025109, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.025923}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.010376, 'median_return': -0.011432, 'mean_absolute_return': 0.017759, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007481, 'median_return': 0.026113, 'mean_absolute_return': 0.037607, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.018653, 'median_return': 0.059131, 'mean_absolute_return': 0.090609, 'max_adverse_excursion': -0.146695, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.005087, 'median_return': -0.003676, 'mean_absolute_return': 0.015556, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.009819, 'median_return': -0.013446, 'mean_absolute_return': 0.020736, 'max_adverse_excursion': -0.053563, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.010898, 'median_return': -0.010456, 'mean_absolute_return': 0.026152, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.014104, 'median_return': 0.013156, 'mean_absolute_return': 0.035905, 'max_adverse_excursion': -0.095423, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.038192, 'median_return': 0.053855, 'mean_absolute_return': 0.068437, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.188643}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.475}, '60d': {'sample_size': 80, 'hit_rate': 0.3375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.007474, 'median_return': -0.003244, 'mean_absolute_return': 0.017271, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.010743, 'median_return': -0.016062, 'mean_absolute_return': 0.021655, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.012662, 'median_return': -0.010456, 'mean_absolute_return': 0.022444, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.00677, 'median_return': 0.015416, 'mean_absolute_return': 0.032556, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.017781, 'median_return': 0.050438, 'mean_absolute_return': 0.074206, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.005008, 'median_return': -0.00402, 'mean_absolute_return': 0.015742, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.009917, 'median_return': -0.013229, 'mean_absolute_return': 0.020692, 'max_adverse_excursion': -0.053563, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.00903, 'median_return': -0.014005, 'mean_absolute_return': 0.028181, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.020114, 'median_return': 0.015713, 'mean_absolute_return': 0.039595, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.054695, 'median_return': 0.059007, 'mean_absolute_return': 0.067101, 'max_adverse_excursion': -0.063058, 'max_favorable_excursion': 0.188643}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.007474`, median `-0.003244`, mae `0.017271`
- 5d: sample `40`, hit `0.425`, avg `-0.010743`, median `-0.016062`, mae `0.021655`
- 10d: sample `40`, hit `0.35`, avg `-0.012662`, median `-0.010456`, mae `0.022444`
- 20d: sample `40`, hit `0.6`, avg `0.00677`, median `0.015416`, mae `0.032556`
- 60d: sample `40`, hit `0.675`, avg `0.017781`, median `0.050438`, mae `0.074206`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.005008`, median `-0.00402`, mae `0.015742`
- 5d: sample `40`, hit `0.375`, avg `-0.009917`, median `-0.013229`, mae `0.020692`
- 10d: sample `40`, hit `0.4`, avg `-0.00903`, median `-0.014005`, mae `0.028181`
- 20d: sample `40`, hit `0.6`, avg `0.020114`, median `0.015713`, mae `0.039595`
- 60d: sample `40`, hit `0.8`, avg `0.054695`, median `0.059007`, mae `0.067101`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.006743`, median `-0.001658`, mae `0.017181`
- 5d: sample `20`, hit `0.45`, avg `-0.009108`, median `-0.016062`, mae `0.022558`
- 10d: sample `20`, hit `0.35`, avg `-0.011188`, median `-0.010456`, mae `0.022635`
- 20d: sample `20`, hit `0.65`, avg `0.007836`, median `0.021759`, mae `0.03949`
- 60d: sample `20`, hit `0.65`, avg `0.012065`, median `0.059131`, mae `0.101151`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.007474`, median `-0.003244`, mae `0.017271`
- 5d: sample `40`, hit `0.425`, avg `-0.010743`, median `-0.016062`, mae `0.021655`
- 10d: sample `40`, hit `0.35`, avg `-0.012662`, median `-0.010456`, mae `0.022444`
- 20d: sample `40`, hit `0.6`, avg `0.00677`, median `0.015416`, mae `0.032556`
- 60d: sample `40`, hit `0.675`, avg `0.017781`, median `0.050438`, mae `0.074206`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.006743`, median `-0.001658`, mae `0.017181`
- 5d: sample `20`, hit `0.45`, avg `-0.009108`, median `-0.016062`, mae `0.022558`
- 10d: sample `20`, hit `0.35`, avg `-0.011188`, median `-0.010456`, mae `0.022635`
- 20d: sample `20`, hit `0.65`, avg `0.007836`, median `0.021759`, mae `0.03949`
- 60d: sample `20`, hit `0.65`, avg `0.012065`, median `0.059131`, mae `0.101151`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.007474`, median `-0.003244`, mae `0.017271`
- 5d: sample `40`, hit `0.425`, avg `-0.010743`, median `-0.016062`, mae `0.021655`
- 10d: sample `40`, hit `0.35`, avg `-0.012662`, median `-0.010456`, mae `0.022444`
- 20d: sample `40`, hit `0.6`, avg `0.00677`, median `0.015416`, mae `0.032556`
- 60d: sample `40`, hit `0.675`, avg `0.017781`, median `0.050438`, mae `0.074206`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.005008`, median `-0.00402`, mae `0.015742`
- 5d: sample `40`, hit `0.375`, avg `-0.009917`, median `-0.013229`, mae `0.020692`
- 10d: sample `40`, hit `0.4`, avg `-0.00903`, median `-0.014005`, mae `0.028181`
- 20d: sample `40`, hit `0.6`, avg `0.020114`, median `0.015713`, mae `0.039595`
- 60d: sample `40`, hit `0.8`, avg `0.054695`, median `0.059007`, mae `0.067101`

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
- 3d: sample `80`, hit `0.3875`, avg `-0.006241`, median `-0.00402`, mae `0.016506`
- 5d: sample `80`, hit `0.4`, avg `-0.01033`, median `-0.014596`, mae `0.021173`
- 10d: sample `80`, hit `0.375`, avg `-0.010846`, median `-0.011432`, mae `0.025313`
- 20d: sample `80`, hit `0.6`, avg `0.013442`, median `0.015416`, mae `0.036076`
- 60d: sample `80`, hit `0.7375`, avg `0.036238`, median `0.053855`, mae `0.070654`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.006743`, median `-0.001658`, mae `0.017181`
- 5d: sample `20`, hit `0.45`, avg `-0.009108`, median `-0.016062`, mae `0.022558`
- 10d: sample `20`, hit `0.35`, avg `-0.011188`, median `-0.010456`, mae `0.022635`
- 20d: sample `20`, hit `0.65`, avg `0.007836`, median `0.021759`, mae `0.03949`
- 60d: sample `20`, hit `0.65`, avg `0.012065`, median `0.059131`, mae `0.101151`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.006074`, median `-0.00402`, mae `0.016281`
- 5d: sample `60`, hit `0.3833`, avg `-0.010738`, median `-0.013446`, mae `0.020711`
- 10d: sample `60`, hit `0.3833`, avg `-0.010732`, median `-0.013412`, mae `0.026205`
- 20d: sample `60`, hit `0.5833`, avg `0.01531`, median `0.013156`, mae `0.034938`
- 60d: sample `60`, hit `0.7667`, avg `0.044295`, median `0.053855`, mae `0.060488`

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
