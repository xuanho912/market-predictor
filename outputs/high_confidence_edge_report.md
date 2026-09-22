# High Confidence Edge Report

Generated at: `2026-09-22T17:00:21.628979+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `40`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `40`, gate `early_evidence`
- 5d: completed `40`, gate `early_evidence`
- 10d: completed `40`, gate `early_evidence`
- 20d: completed `40`, gate `early_evidence`
- 60d: completed `40`, gate `early_evidence`

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
- 3d: sample `60`, hit `0.5167`, avg `-0.003089`, median `0.001405`, mae `0.015715`
- 5d: sample `60`, hit `0.5`, avg `-0.007024`, median `0.000415`, mae `0.015921`
- 10d: sample `60`, hit `0.4`, avg `-0.00565`, median `-0.007019`, mae `0.019946`
- 20d: sample `60`, hit `0.6`, avg `0.008197`, median `0.015416`, mae `0.033166`
- 60d: sample `60`, hit `0.7`, avg `0.021901`, median `0.037425`, mae `0.057893`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.003414`, median `-0.003723`, mae `0.012045`
- 5d: sample `20`, hit `0.15`, avg `-0.014038`, median `-0.013446`, mae `0.021465`
- 10d: sample `20`, hit `0.2`, avg `-0.025159`, median `-0.032485`, mae `0.037578`
- 20d: sample `20`, hit `0.35`, avg `-0.016913`, median `-0.032304`, mae `0.053226`
- 60d: sample `20`, hit `0.6`, avg `0.002308`, median `0.029066`, mae `0.083785`

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
- 3d: sample `8`, hit `0.125`, avg `-0.020054`, median `-0.022062`, mae `0.021733`
- 5d: sample `8`, hit `0.375`, avg `-0.016882`, median `-0.004438`, mae `0.020165`
- 10d: sample `8`, hit `0.0`, avg `-0.018343`, median `-0.017071`, mae `0.018343`
- 20d: sample `8`, hit `0.625`, avg `-0.00332`, median `0.021759`, mae `0.046531`
- 60d: sample `8`, hit `0.625`, avg `0.0071`, median `0.046132`, mae `0.081046`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.020054`, median `-0.022062`, mae `0.021733`
- 5d: sample `8`, hit `0.375`, avg `-0.016882`, median `-0.004438`, mae `0.020165`
- 10d: sample `8`, hit `0.0`, avg `-0.018343`, median `-0.017071`, mae `0.018343`
- 20d: sample `8`, hit `0.625`, avg `-0.00332`, median `0.021759`, mae `0.046531`
- 60d: sample `8`, hit `0.625`, avg `0.0071`, median `0.046132`, mae `0.081046`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.003089, 'median_return': 0.001405, 'mean_absolute_return': 0.015715, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.007024, 'median_return': 0.000415, 'mean_absolute_return': 0.015921, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026269}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.00565, 'median_return': -0.007019, 'mean_absolute_return': 0.019946, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.051845}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.008197, 'median_return': 0.015416, 'mean_absolute_return': 0.033166, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.021901, 'median_return': 0.037425, 'mean_absolute_return': 0.057893, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.020054, 'median_return': -0.022062, 'mean_absolute_return': 0.021733, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.016882, 'median_return': -0.004438, 'mean_absolute_return': 0.020165, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.018343, 'median_return': -0.017071, 'mean_absolute_return': 0.018343, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00332, 'median_return': 0.021759, 'mean_absolute_return': 0.046531, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.0071, 'median_return': 0.046132, 'mean_absolute_return': 0.081046, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001294, 'median_return': 0.000744, 'mean_absolute_return': 0.014027, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.007877, 'median_return': -0.006464, 'mean_absolute_return': 0.01699, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.009659, 'median_return': -0.010456, 'mean_absolute_return': 0.025022, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.002501, 'median_return': 0.001407, 'mean_absolute_return': 0.037253, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.086975}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.018103, 'median_return': 0.031273, 'mean_absolute_return': 0.062513, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.05, 'both_hit': 23, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.125, 'both_hit': 22, 'both_miss': 18}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.025, 'both_hit': 19, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.15, 'both_hit': 23, 'both_miss': 17}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.05, 'both_hit': 28, 'both_miss': 12}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.00317, 'median_return': -0.001227, 'mean_absolute_return': 0.014797, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': -0.008777, 'median_return': -0.006464, 'mean_absolute_return': 0.017307, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.35, 'avg_return': -0.010527, 'median_return': -0.011432, 'mean_absolute_return': 0.024354, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.001919, 'median_return': 0.002867, 'mean_absolute_return': 0.038181, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086975}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.017003, 'median_return': 0.031273, 'mean_absolute_return': 0.064366, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.005907`, median `0.000766`, mae `0.015226`
- 5d: sample `20`, hit `0.45`, avg `-0.008694`, median `-0.006464`, mae `0.016523`
- 10d: sample `20`, hit `0.35`, avg `-0.012805`, median `-0.009882`, mae `0.020961`
- 20d: sample `20`, hit `0.5`, avg `0.009454`, median `0.015416`, mae `0.028626`
- 60d: sample `20`, hit `0.65`, avg `0.02105`, median `0.053855`, mae `0.052016`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.00317`, median `-0.001227`, mae `0.014797`
- 5d: sample `80`, hit `0.4125`, avg `-0.008777`, median `-0.006464`, mae `0.017307`
- 10d: sample `80`, hit `0.35`, avg `-0.010527`, median `-0.011432`, mae `0.024354`
- 20d: sample `80`, hit `0.5375`, avg `0.001919`, median `0.002867`, mae `0.038181`
- 60d: sample `80`, hit `0.675`, avg `0.017003`, median `0.031273`, mae `0.064366`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.005907`, median `0.000766`, mae `0.015226`
- 5d: sample `20`, hit `0.45`, avg `-0.008694`, median `-0.006464`, mae `0.016523`
- 10d: sample `20`, hit `0.35`, avg `-0.012805`, median `-0.009882`, mae `0.020961`
- 20d: sample `20`, hit `0.5`, avg `0.009454`, median `0.015416`, mae `0.028626`
- 60d: sample `20`, hit `0.65`, avg `0.02105`, median `0.053855`, mae `0.052016`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.003089`, median `0.001405`, mae `0.015715`
- 5d: sample `60`, hit `0.5`, avg `-0.007024`, median `0.000415`, mae `0.015921`
- 10d: sample `60`, hit `0.4`, avg `-0.00565`, median `-0.007019`, mae `0.019946`
- 20d: sample `60`, hit `0.6`, avg `0.008197`, median `0.015416`, mae `0.033166`
- 60d: sample `60`, hit `0.7`, avg `0.021901`, median `0.037425`, mae `0.057893`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.008696`, median `-0.009383`, mae `0.019405`
- 5d: sample `20`, hit `0.4`, avg `-0.014191`, median `-0.008162`, mae `0.019167`
- 10d: sample `20`, hit `0.25`, avg `-0.012133`, median `-0.011432`, mae `0.018813`
- 20d: sample `20`, hit `0.65`, avg `0.005254`, median `0.020068`, mae `0.038393`
- 60d: sample `20`, hit `0.7`, avg `0.028024`, median `0.059131`, mae `0.07953`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.005907`, median `0.000766`, mae `0.015226`
- 5d: sample `20`, hit `0.45`, avg `-0.008694`, median `-0.006464`, mae `0.016523`
- 10d: sample `20`, hit `0.35`, avg `-0.012805`, median `-0.009882`, mae `0.020961`
- 20d: sample `20`, hit `0.5`, avg `0.009454`, median `0.015416`, mae `0.028626`
- 60d: sample `20`, hit `0.65`, avg `0.02105`, median `0.053855`, mae `0.052016`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00168`, median `0.003785`, mae `0.015959`
- 5d: sample `40`, hit `0.525`, avg `-0.006189`, median `0.000863`, mae `0.015621`
- 10d: sample `40`, hit `0.425`, avg `-0.002073`, median `-0.006017`, mae `0.019438`
- 20d: sample `40`, hit `0.65`, avg `0.007568`, median `0.016027`, mae `0.035436`
- 60d: sample `40`, hit `0.725`, avg `0.022327`, median `0.037425`, mae `0.060832`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.003414`, median `-0.003723`, mae `0.012045`
- 5d: sample `20`, hit `0.15`, avg `-0.014038`, median `-0.013446`, mae `0.021465`
- 10d: sample `20`, hit `0.2`, avg `-0.025159`, median `-0.032485`, mae `0.037578`
- 20d: sample `20`, hit `0.35`, avg `-0.016913`, median `-0.032304`, mae `0.053226`
- 60d: sample `20`, hit `0.6`, avg `0.002308`, median `0.029066`, mae `0.083785`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.00317`, median `-0.001227`, mae `0.014797`
- 5d: sample `80`, hit `0.4125`, avg `-0.008777`, median `-0.006464`, mae `0.017307`
- 10d: sample `80`, hit `0.35`, avg `-0.010527`, median `-0.011432`, mae `0.024354`
- 20d: sample `80`, hit `0.5375`, avg `0.001919`, median `0.002867`, mae `0.038181`
- 60d: sample `80`, hit `0.675`, avg `0.017003`, median `0.031273`, mae `0.064366`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.003089`, median `0.001405`, mae `0.015715`
- 5d: sample `60`, hit `0.5`, avg `-0.007024`, median `0.000415`, mae `0.015921`
- 10d: sample `60`, hit `0.4`, avg `-0.00565`, median `-0.007019`, mae `0.019946`
- 20d: sample `60`, hit `0.6`, avg `0.008197`, median `0.015416`, mae `0.033166`
- 60d: sample `60`, hit `0.7`, avg `0.021901`, median `0.037425`, mae `0.057893`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.002258`, median `-0.001227`, mae `0.014654`
- 5d: sample `60`, hit `0.4`, avg `-0.008805`, median `-0.004858`, mae `0.017569`
- 10d: sample `60`, hit `0.35`, avg `-0.009768`, median `-0.013981`, mae `0.025485`
- 20d: sample `60`, hit `0.55`, avg `-0.000593`, median `0.002867`, mae `0.041366`
- 60d: sample `60`, hit `0.6833`, avg `0.015654`, median `0.031273`, mae `0.068483`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.00168`, median `0.003785`, mae `0.015959`
- 5d: sample `40`, hit `0.525`, avg `-0.006189`, median `0.000863`, mae `0.015621`
- 10d: sample `40`, hit `0.425`, avg `-0.002073`, median `-0.006017`, mae `0.019438`
- 20d: sample `40`, hit `0.65`, avg `0.007568`, median `0.016027`, mae `0.035436`
- 60d: sample `40`, hit `0.725`, avg `0.022327`, median `0.037425`, mae `0.060832`

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
