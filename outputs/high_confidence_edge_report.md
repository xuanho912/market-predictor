# High Confidence Edge Report

Generated at: `2026-10-23T17:12:06.775112+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `132`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `132`, gate `stronger_evidence`
- 5d: completed `132`, gate `stronger_evidence`
- 10d: completed `132`, gate `stronger_evidence`
- 20d: completed `132`, gate `stronger_evidence`
- 60d: completed `132`, gate `stronger_evidence`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004178`, median `0.006274`, mae `0.015789`
- 5d: sample `40`, hit `0.5`, avg `0.001279`, median `0.000208`, mae `0.015985`
- 10d: sample `40`, hit `0.525`, avg `0.003269`, median `0.006053`, mae `0.020622`
- 20d: sample `40`, hit `0.775`, avg `0.017987`, median `0.027343`, mae `0.030008`
- 60d: sample `40`, hit `0.8`, avg `0.038932`, median `0.05488`, mae `0.060339`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001297`, median `-0.002028`, mae `0.017524`
- 5d: sample `40`, hit `0.6`, avg `0.003676`, median `0.007145`, mae `0.019744`
- 10d: sample `40`, hit `0.675`, avg `0.010838`, median `0.011727`, mae `0.024236`
- 20d: sample `40`, hit `0.65`, avg `0.015104`, median `0.010428`, mae `0.034598`
- 60d: sample `40`, hit `0.8`, avg `0.032479`, median `0.029982`, mae `0.048885`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.008415`, median `0.006722`, mae `0.011593`
- 5d: sample `8`, hit `0.75`, avg `0.006168`, median `0.011571`, mae `0.014585`
- 10d: sample `8`, hit `0.625`, avg `0.007932`, median `0.012215`, mae `0.026654`
- 20d: sample `8`, hit `0.875`, avg `0.030828`, median `0.028859`, mae `0.031835`
- 60d: sample `8`, hit `0.625`, avg `0.023923`, median `0.032524`, mae `0.044309`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.008415`, median `0.006722`, mae `0.011593`
- 5d: sample `8`, hit `0.75`, avg `0.006168`, median `0.011571`, mae `0.014585`
- 10d: sample `8`, hit `0.625`, avg `0.007932`, median `0.012215`, mae `0.026654`
- 20d: sample `8`, hit `0.875`, avg `0.030828`, median `0.028859`, mae `0.031835`
- 60d: sample `8`, hit `0.625`, avg `0.023923`, median `0.032524`, mae `0.044309`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.008415, 'median_return': 0.006722, 'mean_absolute_return': 0.011593, 'max_adverse_excursion': -0.012711, 'max_favorable_excursion': 0.022499}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006168, 'median_return': 0.011571, 'mean_absolute_return': 0.014585, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.027075}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.007932, 'median_return': 0.012215, 'mean_absolute_return': 0.026654, 'max_adverse_excursion': -0.052222, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.030828, 'median_return': 0.028859, 'mean_absolute_return': 0.031835, 'max_adverse_excursion': -0.004032, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.023923, 'median_return': 0.032524, 'mean_absolute_return': 0.044309, 'max_adverse_excursion': -0.069824, 'max_favorable_excursion': 0.099148}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.002106, 'median_return': 0.000732, 'mean_absolute_return': 0.017219, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.002067, 'median_return': 0.003714, 'mean_absolute_return': 0.018229, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.006956, 'median_return': 0.006878, 'mean_absolute_return': 0.021959, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.014959, 'median_return': 0.016838, 'mean_absolute_return': 0.032355, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.099029}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.037015, 'median_return': 0.042761, 'mean_absolute_return': 0.055757, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.166476}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.5625}, '60d': {'sample_size': 80, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.05, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.15, 'both_hit': 12, 'both_miss': 8}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.175, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.025, 'both_hit': 14, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.1, 'both_hit': 14, 'both_miss': 6}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.003649, 'median_return': 0.005726, 'mean_absolute_return': 0.016612, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.003951, 'median_return': 0.006571, 'mean_absolute_return': 0.017579, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.044543}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.007306, 'median_return': 0.007161, 'mean_absolute_return': 0.021506, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.017532, 'median_return': 0.024811, 'mean_absolute_return': 0.031475, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.099029}, '60d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.032261, 'median_return': 0.041644, 'mean_absolute_return': 0.053656, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.103268}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': 1e-06, 'median_return': -0.007802, 'mean_absolute_return': 0.016789, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001944, 'median_return': -0.00459, 'mean_absolute_return': 0.018719, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006293, 'median_return': 0.009975, 'mean_absolute_return': 0.025197, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.013585, 'median_return': 0.019238, 'mean_absolute_return': 0.034789, 'max_adverse_excursion': -0.055489, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.04604, 'median_return': 0.042761, 'mean_absolute_return': 0.05748, 'max_adverse_excursion': -0.099346, 'max_favorable_excursion': 0.166476}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.003649`, median `0.005726`, mae `0.016612`
- 5d: sample `60`, hit `0.5833`, avg `0.003951`, median `0.006571`, mae `0.017579`
- 10d: sample `60`, hit `0.6`, avg `0.007306`, median `0.007161`, mae `0.021506`
- 20d: sample `60`, hit `0.7167`, avg `0.017532`, median `0.024811`, mae `0.031475`
- 60d: sample `60`, hit `0.7833`, avg `0.032261`, median `0.041644`, mae `0.053656`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `1e-06`, median `-0.007802`, mae `0.016789`
- 5d: sample `20`, hit `0.45`, avg `-0.001944`, median `-0.00459`, mae `0.018719`
- 10d: sample `20`, hit `0.6`, avg `0.006293`, median `0.009975`, mae `0.025197`
- 20d: sample `20`, hit `0.7`, avg `0.013585`, median `0.019238`, mae `0.034789`
- 60d: sample `20`, hit `0.85`, avg `0.04604`, median `0.042761`, mae `0.05748`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004178`, median `0.006274`, mae `0.015789`
- 5d: sample `40`, hit `0.5`, avg `0.001279`, median `0.000208`, mae `0.015985`
- 10d: sample `40`, hit `0.525`, avg `0.003269`, median `0.006053`, mae `0.020622`
- 20d: sample `40`, hit `0.775`, avg `0.017987`, median `0.027343`, mae `0.030008`
- 60d: sample `40`, hit `0.8`, avg `0.038932`, median `0.05488`, mae `0.060339`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003995`, median `0.004243`, mae `0.018831`
- 5d: sample `20`, hit `0.4`, avg `-0.000286`, median `-0.004216`, mae `0.017528`
- 10d: sample `20`, hit `0.5`, avg `0.006417`, median `0.006053`, mae `0.017915`
- 20d: sample `20`, hit `0.85`, avg `0.02117`, median `0.028264`, mae `0.029663`
- 60d: sample `20`, hit `0.9`, avg `0.060119`, median `0.073586`, mae `0.070785`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004178`, median `0.006274`, mae `0.015789`
- 5d: sample `40`, hit `0.5`, avg `0.001279`, median `0.000208`, mae `0.015985`
- 10d: sample `40`, hit `0.525`, avg `0.003269`, median `0.006053`, mae `0.020622`
- 20d: sample `40`, hit `0.775`, avg `0.017987`, median `0.027343`, mae `0.030008`
- 60d: sample `40`, hit `0.8`, avg `0.038932`, median `0.05488`, mae `0.060339`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003995`, median `0.004243`, mae `0.018831`
- 5d: sample `20`, hit `0.4`, avg `-0.000286`, median `-0.004216`, mae `0.017528`
- 10d: sample `20`, hit `0.5`, avg `0.006417`, median `0.006053`, mae `0.017915`
- 20d: sample `20`, hit `0.85`, avg `0.02117`, median `0.028264`, mae `0.029663`
- 60d: sample `20`, hit `0.9`, avg `0.060119`, median `0.073586`, mae `0.070785`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `1e-06`, median `-0.007802`, mae `0.016789`
- 5d: sample `20`, hit `0.45`, avg `-0.001944`, median `-0.00459`, mae `0.018719`
- 10d: sample `20`, hit `0.6`, avg `0.006293`, median `0.009975`, mae `0.025197`
- 20d: sample `20`, hit `0.7`, avg `0.013585`, median `0.019238`, mae `0.034789`
- 60d: sample `20`, hit `0.85`, avg `0.04604`, median `0.042761`, mae `0.05748`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.003649`, median `0.005726`, mae `0.016612`
- 5d: sample `60`, hit `0.5833`, avg `0.003951`, median `0.006571`, mae `0.017579`
- 10d: sample `60`, hit `0.6`, avg `0.007306`, median `0.007161`, mae `0.021506`
- 20d: sample `60`, hit `0.7167`, avg `0.017532`, median `0.024811`, mae `0.031475`
- 60d: sample `60`, hit `0.7833`, avg `0.032261`, median `0.041644`, mae `0.053656`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `0.002737`, median `0.002296`, mae `0.016656`
- 5d: sample `80`, hit `0.55`, avg `0.002477`, median `0.003714`, mae `0.017864`
- 10d: sample `80`, hit `0.6`, avg `0.007053`, median `0.007161`, mae `0.022429`
- 20d: sample `80`, hit `0.7125`, avg `0.016545`, median `0.019238`, mae `0.032303`
- 60d: sample `80`, hit `0.8`, avg `0.035706`, median `0.041644`, mae `0.054612`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004178`, median `0.006274`, mae `0.015789`
- 5d: sample `40`, hit `0.5`, avg `0.001279`, median `0.000208`, mae `0.015985`
- 10d: sample `40`, hit `0.525`, avg `0.003269`, median `0.006053`, mae `0.020622`
- 20d: sample `40`, hit `0.775`, avg `0.017987`, median `0.027343`, mae `0.030008`
- 60d: sample `40`, hit `0.8`, avg `0.038932`, median `0.05488`, mae `0.060339`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001297`, median `-0.002028`, mae `0.017524`
- 5d: sample `40`, hit `0.6`, avg `0.003676`, median `0.007145`, mae `0.019744`
- 10d: sample `40`, hit `0.675`, avg `0.010838`, median `0.011727`, mae `0.024236`
- 20d: sample `40`, hit `0.65`, avg `0.015104`, median `0.010428`, mae `0.034598`
- 60d: sample `40`, hit `0.8`, avg `0.032479`, median `0.029982`, mae `0.048885`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
