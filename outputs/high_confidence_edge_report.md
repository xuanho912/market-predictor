# High Confidence Edge Report

Generated at: `2026-10-08T18:54:14.005949+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `88`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `88`, gate `moderate_evidence`
- 5d: completed `88`, gate `moderate_evidence`
- 10d: completed `88`, gate `moderate_evidence`
- 20d: completed `88`, gate `moderate_evidence`
- 60d: completed `88`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.3375`, avg `-0.007093`, median `-0.004907`, mae `0.017055`
- 5d: sample `80`, hit `0.4`, avg `-0.010863`, median `-0.013229`, mae `0.020937`
- 10d: sample `80`, hit `0.4375`, avg `-0.010199`, median `-0.006933`, mae `0.027143`
- 20d: sample `80`, hit `0.575`, avg `0.008941`, median `0.016027`, mae `0.04328`
- 60d: sample `80`, hit `0.75`, avg `0.030744`, median `0.046407`, mae `0.072218`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.009664`, median `-0.001658`, mae `0.024261`
- 5d: sample `8`, hit `0.5`, avg `-0.011557`, median `0.005072`, mae `0.02438`
- 10d: sample `8`, hit `0.125`, avg `-0.012306`, median `-0.013832`, mae `0.019287`
- 20d: sample `8`, hit `0.75`, avg `0.00631`, median `0.021759`, mae `0.036436`
- 60d: sample `8`, hit `0.75`, avg `0.017567`, median `0.050438`, mae `0.089522`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.009664`, median `-0.001658`, mae `0.024261`
- 5d: sample `8`, hit `0.5`, avg `-0.011557`, median `0.005072`, mae `0.02438`
- 10d: sample `8`, hit `0.125`, avg `-0.012306`, median `-0.013832`, mae `0.019287`
- 20d: sample `8`, hit `0.75`, avg `0.00631`, median `0.021759`, mae `0.036436`
- 60d: sample `8`, hit `0.75`, avg `0.017567`, median `0.050438`, mae `0.089522`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.3375, 'avg_return': -0.007093, 'median_return': -0.004907, 'mean_absolute_return': 0.017055, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.010863, 'median_return': -0.013229, 'mean_absolute_return': 0.020937, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.010199, 'median_return': -0.006933, 'mean_absolute_return': 0.027143, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.008941, 'median_return': 0.016027, 'mean_absolute_return': 0.04328, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.030744, 'median_return': 0.046407, 'mean_absolute_return': 0.072218, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154613}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.009664, 'median_return': -0.001658, 'mean_absolute_return': 0.024261, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.011557, 'median_return': 0.005072, 'mean_absolute_return': 0.02438, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.025923}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.012306, 'median_return': -0.013832, 'mean_absolute_return': 0.019287, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.00631, 'median_return': 0.021759, 'mean_absolute_return': 0.036436, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.017567, 'median_return': 0.050438, 'mean_absolute_return': 0.089522, 'max_adverse_excursion': -0.146695, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3333, 'avg_return': -0.006807, 'median_return': -0.004907, 'mean_absolute_return': 0.016254, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.010786, 'median_return': -0.013229, 'mean_absolute_return': 0.020554, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.009965, 'median_return': -0.006017, 'mean_absolute_return': 0.028015, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.009234, 'median_return': 0.015416, 'mean_absolute_return': 0.04404, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.032208, 'median_return': 0.046407, 'mean_absolute_return': 0.070295, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154613}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.5}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.3375, 'avg_return': -0.007093, 'median_return': -0.004907, 'mean_absolute_return': 0.017055, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.010863, 'median_return': -0.013229, 'mean_absolute_return': 0.020937, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.010199, 'median_return': -0.006933, 'mean_absolute_return': 0.027143, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.008941, 'median_return': 0.016027, 'mean_absolute_return': 0.04328, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.030744, 'median_return': 0.046407, 'mean_absolute_return': 0.072218, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154613}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.009733`, median `-0.010094`, mae `0.019559`
- 5d: sample `20`, hit `0.4`, avg `-0.012103`, median `-0.016421`, mae `0.025171`
- 10d: sample `20`, hit `0.3`, avg `-0.015491`, median `-0.011432`, mae `0.025015`
- 20d: sample `20`, hit `0.55`, avg `0.001066`, median `0.016745`, mae `0.04284`
- 60d: sample `20`, hit `0.6`, avg `-0.000463`, median `0.046132`, mae `0.102085`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.006633`, median `-0.00402`, mae `0.016506`
- 5d: sample `40`, hit `0.375`, avg `-0.011394`, median `-0.011684`, mae `0.01956`
- 10d: sample `40`, hit `0.475`, avg `-0.006604`, median `-0.004767`, mae `0.030511`
- 20d: sample `40`, hit `0.575`, avg `0.012846`, median `0.016027`, mae `0.04858`
- 60d: sample `40`, hit `0.8`, avg `0.044491`, median `0.050036`, mae `0.06586`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.009733`, median `-0.010094`, mae `0.019559`
- 5d: sample `20`, hit `0.4`, avg `-0.012103`, median `-0.016421`, mae `0.025171`
- 10d: sample `20`, hit `0.3`, avg `-0.015491`, median `-0.011432`, mae `0.025015`
- 20d: sample `20`, hit `0.55`, avg `0.001066`, median `0.016745`, mae `0.04284`
- 60d: sample `20`, hit `0.6`, avg `-0.000463`, median `0.046132`, mae `0.102085`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.009733`, median `-0.010094`, mae `0.019559`
- 5d: sample `20`, hit `0.4`, avg `-0.012103`, median `-0.016421`, mae `0.025171`
- 10d: sample `20`, hit `0.3`, avg `-0.015491`, median `-0.011432`, mae `0.025015`
- 20d: sample `20`, hit `0.55`, avg `0.001066`, median `0.016745`, mae `0.04284`
- 60d: sample `20`, hit `0.6`, avg `-0.000463`, median `0.046132`, mae `0.102085`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.005373`, median `-0.003244`, mae `0.015649`
- 5d: sample `20`, hit `0.45`, avg `-0.008561`, median `-0.013237`, mae `0.019454`
- 10d: sample `20`, hit `0.5`, avg `-0.012096`, median `0.000197`, mae `0.022533`
- 20d: sample `20`, hit `0.6`, avg `0.009007`, median `0.01927`, mae `0.033121`
- 60d: sample `20`, hit `0.8`, avg `0.034457`, median `0.053855`, mae `0.055066`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.006633`, median `-0.00402`, mae `0.016506`
- 5d: sample `40`, hit `0.375`, avg `-0.011394`, median `-0.011684`, mae `0.01956`
- 10d: sample `40`, hit `0.475`, avg `-0.006604`, median `-0.004767`, mae `0.030511`
- 20d: sample `40`, hit `0.575`, avg `0.012846`, median `0.016027`, mae `0.04858`
- 60d: sample `40`, hit `0.8`, avg `0.044491`, median `0.050036`, mae `0.06586`

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
- 3d: sample `80`, hit `0.3375`, avg `-0.007093`, median `-0.004907`, mae `0.017055`
- 5d: sample `80`, hit `0.4`, avg `-0.010863`, median `-0.013229`, mae `0.020937`
- 10d: sample `80`, hit `0.4375`, avg `-0.010199`, median `-0.006933`, mae `0.027143`
- 20d: sample `80`, hit `0.575`, avg `0.008941`, median `0.016027`, mae `0.04328`
- 60d: sample `80`, hit `0.75`, avg `0.030744`, median `0.046407`, mae `0.072218`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.007553`, median `-0.007923`, mae `0.017604`
- 5d: sample `40`, hit `0.425`, avg `-0.010332`, median `-0.015413`, mae `0.022313`
- 10d: sample `40`, hit `0.4`, avg `-0.013793`, median `-0.009882`, mae `0.023774`
- 20d: sample `40`, hit `0.575`, avg `0.005036`, median `0.016745`, mae `0.03798`
- 60d: sample `40`, hit `0.7`, avg `0.016997`, median `0.046407`, mae `0.078575`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.3375`, avg `-0.007093`, median `-0.004907`, mae `0.017055`
- 5d: sample `80`, hit `0.4`, avg `-0.010863`, median `-0.013229`, mae `0.020937`
- 10d: sample `80`, hit `0.4375`, avg `-0.010199`, median `-0.006933`, mae `0.027143`
- 20d: sample `80`, hit `0.575`, avg `0.008941`, median `0.016027`, mae `0.04328`
- 60d: sample `80`, hit `0.75`, avg `0.030744`, median `0.046407`, mae `0.072218`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.007553`, median `-0.007923`, mae `0.017604`
- 5d: sample `40`, hit `0.425`, avg `-0.010332`, median `-0.015413`, mae `0.022313`
- 10d: sample `40`, hit `0.4`, avg `-0.013793`, median `-0.009882`, mae `0.023774`
- 20d: sample `40`, hit `0.575`, avg `0.005036`, median `0.016745`, mae `0.03798`
- 60d: sample `40`, hit `0.7`, avg `0.016997`, median `0.046407`, mae `0.078575`

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
