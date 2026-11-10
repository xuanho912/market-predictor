# High Confidence Edge Report

Generated at: `2026-11-10T04:36:44.116572+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `176`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `176`, gate `stronger_evidence`
- 5d: completed `176`, gate `stronger_evidence`
- 10d: completed `176`, gate `stronger_evidence`
- 20d: completed `176`, gate `stronger_evidence`
- 60d: completed `176`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.6375`, avg `0.0051`, median `0.007362`, mae `0.017732`
- 5d: sample `80`, hit `0.625`, avg `0.009923`, median `0.008117`, mae `0.021498`
- 10d: sample `80`, hit `0.7125`, avg `0.017436`, median `0.021778`, mae `0.034983`
- 20d: sample `80`, hit `0.7375`, avg `0.026853`, median `0.032319`, mae `0.046478`
- 60d: sample `80`, hit `0.8125`, avg `0.050551`, median `0.062489`, mae `0.065446`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.011527`, median `0.01968`, mae `0.023887`
- 5d: sample `8`, hit `0.875`, avg `0.024533`, median `0.032932`, mae `0.034656`
- 10d: sample `8`, hit `0.75`, avg `0.026699`, median `0.04786`, mae `0.042404`
- 20d: sample `8`, hit `0.75`, avg `0.031554`, median `0.053017`, mae `0.048685`
- 60d: sample `8`, hit `0.75`, avg `0.036447`, median `0.056005`, mae `0.062182`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.011527`, median `0.01968`, mae `0.023887`
- 5d: sample `8`, hit `0.875`, avg `0.024533`, median `0.032932`, mae `0.034656`
- 10d: sample `8`, hit `0.75`, avg `0.026699`, median `0.04786`, mae `0.042404`
- 20d: sample `8`, hit `0.75`, avg `0.031554`, median `0.053017`, mae `0.048685`
- 60d: sample `8`, hit `0.75`, avg `0.036447`, median `0.056005`, mae `0.062182`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.011527, 'median_return': 0.01968, 'mean_absolute_return': 0.023887, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.033003}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.024533, 'median_return': 0.032932, 'mean_absolute_return': 0.034656, 'max_adverse_excursion': -0.04049, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.026699, 'median_return': 0.04786, 'mean_absolute_return': 0.042404, 'max_adverse_excursion': -0.037736, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.031554, 'median_return': 0.053017, 'mean_absolute_return': 0.048685, 'max_adverse_excursion': -0.060735, 'max_favorable_excursion': 0.064912}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.036447, 'median_return': 0.056005, 'mean_absolute_return': 0.062182, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.10012}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.004386, 'median_return': 0.006372, 'mean_absolute_return': 0.017048, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.0083, 'median_return': 0.006712, 'mean_absolute_return': 0.020036, 'max_adverse_excursion': -0.033198, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.016407, 'median_return': 0.020918, 'mean_absolute_return': 0.034158, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.02633, 'median_return': 0.031196, 'mean_absolute_return': 0.046232, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.052118, 'median_return': 0.062764, 'mean_absolute_return': 0.065808, 'max_adverse_excursion': -0.072844, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.3625}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001102, 'median_return': 0.006372, 'mean_absolute_return': 0.015619, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.033003}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.008439, 'median_return': 0.011065, 'mean_absolute_return': 0.02045, 'max_adverse_excursion': -0.04049, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.014582, 'median_return': 0.015002, 'mean_absolute_return': 0.028529, 'max_adverse_excursion': -0.054516, 'max_favorable_excursion': 0.072069}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.01855, 'median_return': 0.024146, 'mean_absolute_return': 0.039501, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.038068, 'median_return': 0.044733, 'mean_absolute_return': 0.054294, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.136877}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009099, 'median_return': 0.010441, 'mean_absolute_return': 0.019845, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.011407, 'median_return': 0.004924, 'mean_absolute_return': 0.022547, 'max_adverse_excursion': -0.033198, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.020291, 'median_return': 0.033298, 'mean_absolute_return': 0.041436, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.035156, 'median_return': 0.052608, 'mean_absolute_return': 0.053454, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.063034, 'median_return': 0.072891, 'mean_absolute_return': 0.076597, 'max_adverse_excursion': -0.072844, 'max_favorable_excursion': 0.140054}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001102`, median `0.006372`, mae `0.015619`
- 5d: sample `40`, hit `0.65`, avg `0.008439`, median `0.011065`, mae `0.02045`
- 10d: sample `40`, hit `0.7`, avg `0.014582`, median `0.015002`, mae `0.028529`
- 20d: sample `40`, hit `0.675`, avg `0.01855`, median `0.024146`, mae `0.039501`
- 60d: sample `40`, hit `0.75`, avg `0.038068`, median `0.044733`, mae `0.054294`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.009099`, median `0.010441`, mae `0.019845`
- 5d: sample `40`, hit `0.6`, avg `0.011407`, median `0.004924`, mae `0.022547`
- 10d: sample `40`, hit `0.725`, avg `0.020291`, median `0.033298`, mae `0.041436`
- 20d: sample `40`, hit `0.8`, avg `0.035156`, median `0.052608`, mae `0.053454`
- 60d: sample `40`, hit `0.875`, avg `0.063034`, median `0.072891`, mae `0.076597`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002983`, median `0.00955`, mae `0.019136`
- 5d: sample `20`, hit `0.75`, avg `0.01344`, median `0.012136`, mae `0.024496`
- 10d: sample `20`, hit `0.85`, avg `0.025349`, median `0.021778`, mae `0.033027`
- 20d: sample `20`, hit `0.7`, avg `0.023235`, median `0.042224`, mae `0.044891`
- 60d: sample `20`, hit `0.75`, avg `0.046274`, median `0.055822`, mae `0.060226`

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
- 3d: sample `20`, hit `0.65`, avg `0.002983`, median `0.00955`, mae `0.019136`
- 5d: sample `20`, hit `0.75`, avg `0.01344`, median `0.012136`, mae `0.024496`
- 10d: sample `20`, hit `0.85`, avg `0.025349`, median `0.021778`, mae `0.033027`
- 20d: sample `20`, hit `0.7`, avg `0.023235`, median `0.042224`, mae `0.044891`
- 60d: sample `20`, hit `0.75`, avg `0.046274`, median `0.055822`, mae `0.060226`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.009099`, median `0.010441`, mae `0.019845`
- 5d: sample `40`, hit `0.6`, avg `0.011407`, median `0.004924`, mae `0.022547`
- 10d: sample `40`, hit `0.725`, avg `0.020291`, median `0.033298`, mae `0.041436`
- 20d: sample `40`, hit `0.8`, avg `0.035156`, median `0.052608`, mae `0.053454`
- 60d: sample `40`, hit `0.875`, avg `0.063034`, median `0.072891`, mae `0.076597`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002983`, median `0.00955`, mae `0.019136`
- 5d: sample `20`, hit `0.75`, avg `0.01344`, median `0.012136`, mae `0.024496`
- 10d: sample `20`, hit `0.85`, avg `0.025349`, median `0.021778`, mae `0.033027`
- 20d: sample `20`, hit `0.7`, avg `0.023235`, median `0.042224`, mae `0.044891`
- 60d: sample `20`, hit `0.75`, avg `0.046274`, median `0.055822`, mae `0.060226`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001984`, median `0.004243`, mae `0.014737`
- 5d: sample `40`, hit `0.525`, avg `0.004567`, median `0.002812`, mae `0.017432`
- 10d: sample `40`, hit `0.675`, avg `0.013112`, median `0.014227`, mae `0.027609`
- 20d: sample `40`, hit `0.725`, avg `0.023281`, median `0.028589`, mae `0.038964`
- 60d: sample `40`, hit `0.775`, avg `0.037905`, median `0.052632`, mae `0.059969`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.0051`, median `0.007362`, mae `0.017732`
- 5d: sample `80`, hit `0.625`, avg `0.009923`, median `0.008117`, mae `0.021498`
- 10d: sample `80`, hit `0.7125`, avg `0.017436`, median `0.021778`, mae `0.034983`
- 20d: sample `80`, hit `0.7375`, avg `0.026853`, median `0.032319`, mae `0.046478`
- 60d: sample `80`, hit `0.8125`, avg `0.050551`, median `0.062489`, mae `0.065446`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.0051`, median `0.007362`, mae `0.017732`
- 5d: sample `80`, hit `0.625`, avg `0.009923`, median `0.008117`, mae `0.021498`
- 10d: sample `80`, hit `0.7125`, avg `0.017436`, median `0.021778`, mae `0.034983`
- 20d: sample `80`, hit `0.7375`, avg `0.026853`, median `0.032319`, mae `0.046478`
- 60d: sample `80`, hit `0.8125`, avg `0.050551`, median `0.062489`, mae `0.065446`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002983`, median `0.00955`, mae `0.019136`
- 5d: sample `20`, hit `0.75`, avg `0.01344`, median `0.012136`, mae `0.024496`
- 10d: sample `20`, hit `0.85`, avg `0.025349`, median `0.021778`, mae `0.033027`
- 20d: sample `20`, hit `0.7`, avg `0.023235`, median `0.042224`, mae `0.044891`
- 60d: sample `20`, hit `0.75`, avg `0.046274`, median `0.055822`, mae `0.060226`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002983`, median `0.00955`, mae `0.019136`
- 5d: sample `20`, hit `0.75`, avg `0.01344`, median `0.012136`, mae `0.024496`
- 10d: sample `20`, hit `0.85`, avg `0.025349`, median `0.021778`, mae `0.033027`
- 20d: sample `20`, hit `0.7`, avg `0.023235`, median `0.042224`, mae `0.044891`
- 60d: sample `20`, hit `0.75`, avg `0.046274`, median `0.055822`, mae `0.060226`

### risk_path_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.005806`, median `0.006372`, mae `0.017264`
- 5d: sample `60`, hit `0.5833`, avg `0.008751`, median `0.006571`, mae `0.020499`
- 10d: sample `60`, hit `0.6667`, avg `0.014799`, median `0.021836`, mae `0.035634`
- 20d: sample `60`, hit `0.75`, avg `0.028059`, median `0.031658`, mae `0.047006`
- 60d: sample `60`, hit `0.8333`, avg `0.051977`, median `0.065766`, mae `0.067185`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
