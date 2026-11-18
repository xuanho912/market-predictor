# High Confidence Edge Report

Generated at: `2026-11-18T04:11:34.280895+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `200`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `200`, gate `stronger_evidence`
- 5d: completed `200`, gate `stronger_evidence`
- 10d: completed `200`, gate `stronger_evidence`
- 20d: completed `200`, gate `stronger_evidence`
- 60d: completed `200`, gate `stronger_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.005391`, median `0.008733`, mae `0.022263`
- 5d: sample `80`, hit `0.65`, avg `0.008873`, median `0.010394`, mae `0.023856`
- 10d: sample `80`, hit `0.65`, avg `0.018392`, median `0.013222`, mae `0.0326`
- 20d: sample `80`, hit `0.725`, avg `0.03139`, median `0.036447`, mae `0.047343`
- 60d: sample `80`, hit `0.6125`, avg `0.047937`, median `0.054472`, mae `0.085988`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.024709`, median `0.028518`, mae `0.028595`
- 5d: sample `8`, hit `0.75`, avg `0.014645`, median `0.028794`, mae `0.025683`
- 10d: sample `8`, hit `0.75`, avg `0.022843`, median `0.01609`, mae `0.032501`
- 20d: sample `8`, hit `1.0`, avg `0.045188`, median `0.049731`, mae `0.045188`
- 60d: sample `8`, hit `0.875`, avg `0.088635`, median `0.123132`, mae `0.094529`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.010561`, median `0.017427`, mae `0.019502`
- 5d: sample `8`, hit `0.875`, avg `0.010055`, median `0.011143`, mae `0.015391`
- 10d: sample `8`, hit `0.5`, avg `0.007601`, median `0.005519`, mae `0.030241`
- 20d: sample `8`, hit `0.625`, avg `0.016553`, median `0.030297`, mae `0.027174`
- 60d: sample `8`, hit `0.5`, avg `0.019755`, median `0.048963`, mae `0.06089`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010561, 'median_return': 0.017427, 'mean_absolute_return': 0.019502, 'max_adverse_excursion': -0.030262, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.010055, 'median_return': 0.011143, 'mean_absolute_return': 0.015391, 'max_adverse_excursion': -0.021344, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.007601, 'median_return': 0.005519, 'mean_absolute_return': 0.030241, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016553, 'median_return': 0.030297, 'mean_absolute_return': 0.027174, 'max_adverse_excursion': -0.034684, 'max_favorable_excursion': 0.055822}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.019755, 'median_return': 0.048963, 'mean_absolute_return': 0.06089, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.120808}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.004816, 'median_return': 0.007812, 'mean_absolute_return': 0.02257, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.008742, 'median_return': 0.010394, 'mean_absolute_return': 0.024797, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.019591, 'median_return': 0.014135, 'mean_absolute_return': 0.032862, 'max_adverse_excursion': -0.04664, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.033038, 'median_return': 0.037433, 'mean_absolute_return': 0.049583, 'max_adverse_excursion': -0.081434, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.051068, 'median_return': 0.061042, 'mean_absolute_return': 0.088777, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.247486}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4125}, '5d': {'sample_size': 80, 'hit_rate': 0.35}, '10d': {'sample_size': 80, 'hit_rate': 0.35}, '20d': {'sample_size': 80, 'hit_rate': 0.275}, '60d': {'sample_size': 80, 'hit_rate': 0.3875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.011021, 'median_return': 0.010671, 'mean_absolute_return': 0.021512, 'max_adverse_excursion': -0.026721, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.014051, 'median_return': 0.011235, 'mean_absolute_return': 0.024769, 'max_adverse_excursion': -0.031683, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.024669, 'median_return': 0.016658, 'mean_absolute_return': 0.036047, 'max_adverse_excursion': -0.038784, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.043759, 'median_return': 0.038598, 'mean_absolute_return': 0.046673, 'max_adverse_excursion': -0.02849, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.072447, 'median_return': 0.088624, 'mean_absolute_return': 0.088002, 'max_adverse_excursion': -0.053675, 'max_favorable_excursion': 0.247486}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.00024, 'median_return': 0.006898, 'mean_absolute_return': 0.023015, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.054095}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003695, 'median_return': 0.005846, 'mean_absolute_return': 0.022944, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.05994}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.012115, 'median_return': 0.006881, 'mean_absolute_return': 0.029152, 'max_adverse_excursion': -0.04664, 'max_favorable_excursion': 0.08567}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.01902, 'median_return': 0.030297, 'mean_absolute_return': 0.048012, 'max_adverse_excursion': -0.081434, 'max_favorable_excursion': 0.157009}, '60d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.023426, 'median_return': -0.000735, 'mean_absolute_return': 0.083975, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.243748}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.00828`, median `0.009123`, mae `0.020531`
- 5d: sample `60`, hit `0.65`, avg `0.00904`, median `0.007726`, mae `0.02187`
- 10d: sample `60`, hit `0.6333`, avg `0.017042`, median `0.011432`, mae `0.03141`
- 20d: sample `60`, hit `0.8`, avg `0.037703`, median `0.037433`, mae `0.043531`
- 60d: sample `60`, hit `0.6833`, avg `0.059722`, median `0.067623`, mae `0.084484`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003279`, median `0.005908`, mae `0.027461`
- 5d: sample `20`, hit `0.65`, avg `0.008372`, median `0.016321`, mae `0.029816`
- 10d: sample `20`, hit `0.7`, avg `0.022443`, median `0.019876`, mae `0.036168`
- 20d: sample `20`, hit `0.5`, avg `0.012449`, median `0.001287`, mae `0.058777`
- 60d: sample `20`, hit `0.4`, avg `0.012581`, median `-0.00906`, mae `0.090501`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003279`, median `0.005908`, mae `0.027461`
- 5d: sample `20`, hit `0.65`, avg `0.008372`, median `0.016321`, mae `0.029816`
- 10d: sample `20`, hit `0.7`, avg `0.022443`, median `0.019876`, mae `0.036168`
- 20d: sample `20`, hit `0.5`, avg `0.012449`, median `0.001287`, mae `0.058777`
- 60d: sample `20`, hit `0.4`, avg `0.012581`, median `-0.00906`, mae `0.090501`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.003542`, median `0.006898`, mae `0.017436`
- 5d: sample `40`, hit `0.625`, avg `0.002751`, median `0.00438`, mae `0.016468`
- 10d: sample `40`, hit `0.55`, avg `0.005677`, median `0.005356`, mae `0.023178`
- 20d: sample `40`, hit `0.725`, avg `0.026052`, median `0.032299`, mae `0.034654`
- 60d: sample `40`, hit `0.6`, avg `0.03272`, median `0.049411`, mae `0.066444`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.010279`, median `0.010671`, mae `0.022645`
- 5d: sample `40`, hit `0.625`, avg `0.010318`, median `0.007726`, mae `0.024372`
- 10d: sample `40`, hit `0.6`, avg `0.020779`, median `0.014135`, mae `0.035005`
- 20d: sample `40`, hit `0.8`, avg `0.043298`, median `0.039227`, mae `0.049266`
- 60d: sample `40`, hit `0.7`, avg `0.073998`, median `0.113901`, mae `0.099006`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.005391`, median `0.008733`, mae `0.022263`
- 5d: sample `80`, hit `0.65`, avg `0.008873`, median `0.010394`, mae `0.023856`
- 10d: sample `80`, hit `0.65`, avg `0.018392`, median `0.013222`, mae `0.0326`
- 20d: sample `80`, hit `0.725`, avg `0.03139`, median `0.036447`, mae `0.047343`
- 60d: sample `80`, hit `0.6125`, avg `0.047937`, median `0.054472`, mae `0.085988`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.005391`, median `0.008733`, mae `0.022263`
- 5d: sample `80`, hit `0.65`, avg `0.008873`, median `0.010394`, mae `0.023856`
- 10d: sample `80`, hit `0.65`, avg `0.018392`, median `0.013222`, mae `0.0326`
- 20d: sample `80`, hit `0.725`, avg `0.03139`, median `0.036447`, mae `0.047343`
- 60d: sample `80`, hit `0.6125`, avg `0.047937`, median `0.054472`, mae `0.085988`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
