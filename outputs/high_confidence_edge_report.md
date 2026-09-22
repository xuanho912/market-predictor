# High Confidence Edge Report

Generated at: `2026-09-22T23:47:56.196472+00:00`

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
- 3d: sample `60`, hit `0.4833`, avg `-0.003773`, median `-0.001227`, mae `0.015995`
- 5d: sample `60`, hit `0.4833`, avg `-0.007418`, median `-0.000423`, mae `0.016026`
- 10d: sample `60`, hit `0.4`, avg `-0.005051`, median `-0.007019`, mae `0.020372`
- 20d: sample `60`, hit `0.6`, avg `0.010308`, median `0.01927`, mae `0.035277`
- 60d: sample `60`, hit `0.7`, avg `0.023588`, median `0.037425`, mae `0.059299`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.00475`, median `-0.003823`, mae `0.013381`
- 5d: sample `20`, hit `0.15`, avg `-0.013547`, median `-0.012239`, mae `0.020975`
- 10d: sample `20`, hit `0.15`, avg `-0.024798`, median `-0.031826`, mae `0.033995`
- 20d: sample `20`, hit `0.4`, avg `-0.011795`, median `-0.027406`, mae `0.046525`
- 60d: sample `20`, hit `0.55`, avg `0.003609`, median `0.010749`, mae `0.073283`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.003773, 'median_return': -0.001227, 'mean_absolute_return': 0.015995, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.032214}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.007418, 'median_return': -0.000423, 'mean_absolute_return': 0.016026, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026269}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.005051, 'median_return': -0.007019, 'mean_absolute_return': 0.020372, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.051845}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.010308, 'median_return': 0.01927, 'mean_absolute_return': 0.035277, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.125103}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.023588, 'median_return': 0.037425, 'mean_absolute_return': 0.059299, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.154168}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.020054, 'median_return': -0.022062, 'mean_absolute_return': 0.021733, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.016882, 'median_return': -0.004438, 'mean_absolute_return': 0.020165, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.018343, 'median_return': -0.017071, 'mean_absolute_return': 0.018343, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00332, 'median_return': 0.021759, 'mean_absolute_return': 0.046531, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.0071, 'median_return': 0.046132, 'mean_absolute_return': 0.081046, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.002236, 'median_return': -0.001227, 'mean_absolute_return': 0.014632, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.008069, 'median_return': -0.004989, 'mean_absolute_return': 0.016941, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.009059, 'median_return': -0.010456, 'mean_absolute_return': 0.024381, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.005682, 'median_return': 0.009364, 'mean_absolute_return': 0.037151, 'max_adverse_excursion': -0.096041, 'max_favorable_excursion': 0.125103}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.01987, 'median_return': 0.02999, 'mean_absolute_return': 0.060767, 'max_adverse_excursion': -0.193228, 'max_favorable_excursion': 0.154168}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.6}, '60d': {'sample_size': 80, 'hit_rate': 0.6375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.025, 'both_hit': 22, 'both_miss': 18}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.125, 'both_hit': 21, 'both_miss': 19}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.05, 'both_hit': 19, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.125, 'both_hit': 23, 'both_miss': 17}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.05, 'both_hit': 29, 'both_miss': 11}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.003083, 'median_return': -0.001658, 'mean_absolute_return': 0.015122, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.00851, 'median_return': -0.004438, 'mean_absolute_return': 0.017431, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 60, 'hit_rate': 0.3333, 'avg_return': -0.00897, 'median_return': -0.013981, 'mean_absolute_return': 0.024795, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.003484, 'median_return': 0.013156, 'mean_absolute_return': 0.041503, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.125103}, '60d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.01719, 'median_return': 0.02999, 'mean_absolute_return': 0.065804, 'max_adverse_excursion': -0.193228, 'max_favorable_excursion': 0.154168}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.006821, 'median_return': -0.007923, 'mean_absolute_return': 0.016, 'max_adverse_excursion': -0.03413, 'max_favorable_excursion': 0.023395}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010271, 'median_return': -0.010337, 'mean_absolute_return': 0.016759, 'max_adverse_excursion': -0.049407, 'max_favorable_excursion': 0.018625}, '10d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.01304, 'median_return': -0.009882, 'mean_absolute_return': 0.020726, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.008675, 'median_return': 0.015416, 'mean_absolute_return': 0.027847, 'max_adverse_excursion': -0.051442, 'max_favorable_excursion': 0.057835}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.022801, 'median_return': 0.057625, 'mean_absolute_return': 0.053767, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.098228}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.006821`, median `-0.007923`, mae `0.016`
- 5d: sample `20`, hit `0.4`, avg `-0.010271`, median `-0.010337`, mae `0.016759`
- 10d: sample `20`, hit `0.35`, avg `-0.01304`, median `-0.009882`, mae `0.020726`
- 20d: sample `20`, hit `0.5`, avg `0.008675`, median `0.015416`, mae `0.027847`
- 60d: sample `20`, hit `0.65`, avg `0.022801`, median `0.057625`, mae `0.053767`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.004018`, median `-0.003649`, mae `0.015342`
- 5d: sample `80`, hit `0.4`, avg `-0.00895`, median `-0.004989`, mae `0.017263`
- 10d: sample `80`, hit `0.3375`, avg `-0.009988`, median `-0.011432`, mae `0.023778`
- 20d: sample `80`, hit `0.55`, avg `0.004782`, median `0.013156`, mae `0.038089`
- 60d: sample `80`, hit `0.6625`, avg `0.018593`, median `0.02999`, mae `0.062795`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.006821`, median `-0.007923`, mae `0.016`
- 5d: sample `20`, hit `0.4`, avg `-0.010271`, median `-0.010337`, mae `0.016759`
- 10d: sample `20`, hit `0.35`, avg `-0.01304`, median `-0.009882`, mae `0.020726`
- 20d: sample `20`, hit `0.5`, avg `0.008675`, median `0.015416`, mae `0.027847`
- 60d: sample `20`, hit `0.65`, avg `0.022801`, median `0.057625`, mae `0.053767`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.003773`, median `-0.001227`, mae `0.015995`
- 5d: sample `60`, hit `0.4833`, avg `-0.007418`, median `-0.000423`, mae `0.016026`
- 10d: sample `60`, hit `0.4`, avg `-0.005051`, median `-0.007019`, mae `0.020372`
- 20d: sample `60`, hit `0.6`, avg `0.010308`, median `0.01927`, mae `0.035277`
- 60d: sample `60`, hit `0.7`, avg `0.023588`, median `0.037425`, mae `0.059299`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.009815`, median `-0.010033`, mae `0.019492`
- 5d: sample `20`, hit `0.4`, avg `-0.014033`, median `-0.004989`, mae `0.019008`
- 10d: sample `20`, hit `0.25`, avg `-0.011873`, median `-0.011432`, mae `0.018552`
- 20d: sample `20`, hit `0.65`, avg `0.006174`, median `0.021759`, mae `0.039313`
- 60d: sample `20`, hit `0.65`, avg `0.021662`, median `0.046132`, mae `0.076249`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.006821`, median `-0.007923`, mae `0.016`
- 5d: sample `20`, hit `0.4`, avg `-0.010271`, median `-0.010337`, mae `0.016759`
- 10d: sample `20`, hit `0.35`, avg `-0.01304`, median `-0.009882`, mae `0.020726`
- 20d: sample `20`, hit `0.5`, avg `0.008675`, median `0.015416`, mae `0.027847`
- 60d: sample `20`, hit `0.65`, avg `0.022801`, median `0.057625`, mae `0.053767`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.00225`, median `0.00234`, mae `0.015993`
- 5d: sample `40`, hit `0.525`, avg `-0.005991`, median `0.000863`, mae `0.01566`
- 10d: sample `40`, hit `0.425`, avg `-0.001056`, median `-0.006017`, mae `0.020195`
- 20d: sample `40`, hit `0.65`, avg `0.011124`, median `0.021759`, mae `0.038992`
- 60d: sample `40`, hit `0.725`, avg `0.023981`, median `0.037425`, mae `0.062065`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.00475`, median `-0.003823`, mae `0.013381`
- 5d: sample `20`, hit `0.15`, avg `-0.013547`, median `-0.012239`, mae `0.020975`
- 10d: sample `20`, hit `0.15`, avg `-0.024798`, median `-0.031826`, mae `0.033995`
- 20d: sample `20`, hit `0.4`, avg `-0.011795`, median `-0.027406`, mae `0.046525`
- 60d: sample `20`, hit `0.55`, avg `0.003609`, median `0.010749`, mae `0.073283`

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
- 3d: sample `80`, hit `0.4375`, avg `-0.004018`, median `-0.003649`, mae `0.015342`
- 5d: sample `80`, hit `0.4`, avg `-0.00895`, median `-0.004989`, mae `0.017263`
- 10d: sample `80`, hit `0.3375`, avg `-0.009988`, median `-0.011432`, mae `0.023778`
- 20d: sample `80`, hit `0.55`, avg `0.004782`, median `0.013156`, mae `0.038089`
- 60d: sample `80`, hit `0.6625`, avg `0.018593`, median `0.02999`, mae `0.062795`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.003773`, median `-0.001227`, mae `0.015995`
- 5d: sample `60`, hit `0.4833`, avg `-0.007418`, median `-0.000423`, mae `0.016026`
- 10d: sample `60`, hit `0.4`, avg `-0.005051`, median `-0.007019`, mae `0.020372`
- 20d: sample `60`, hit `0.6`, avg `0.010308`, median `0.01927`, mae `0.035277`
- 60d: sample `60`, hit `0.7`, avg `0.023588`, median `0.037425`, mae `0.059299`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.004018`, median `-0.003649`, mae `0.015342`
- 5d: sample `80`, hit `0.4`, avg `-0.00895`, median `-0.004989`, mae `0.017263`
- 10d: sample `80`, hit `0.3375`, avg `-0.009988`, median `-0.011432`, mae `0.023778`
- 20d: sample `80`, hit `0.55`, avg `0.004782`, median `0.013156`, mae `0.038089`
- 60d: sample `80`, hit `0.6625`, avg `0.018593`, median `0.02999`, mae `0.062795`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.003773`, median `-0.001227`, mae `0.015995`
- 5d: sample `60`, hit `0.4833`, avg `-0.007418`, median `-0.000423`, mae `0.016026`
- 10d: sample `60`, hit `0.4`, avg `-0.005051`, median `-0.007019`, mae `0.020372`
- 20d: sample `60`, hit `0.6`, avg `0.010308`, median `0.01927`, mae `0.035277`
- 60d: sample `60`, hit `0.7`, avg `0.023588`, median `0.037425`, mae `0.059299`

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
