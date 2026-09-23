# High Confidence Edge Report

Generated at: `2026-09-23T06:21:00.398159+00:00`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.005324`, median `0.010897`, mae `0.019253`
- 5d: sample `80`, hit `0.6125`, avg `0.005862`, median `0.01152`, mae `0.023579`
- 10d: sample `80`, hit `0.6125`, avg `0.008679`, median `0.012215`, mae `0.034284`
- 20d: sample `80`, hit `0.7875`, avg `0.031343`, median `0.032954`, mae `0.047841`
- 60d: sample `80`, hit `0.825`, avg `0.066044`, median `0.081441`, mae `0.08268`

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
- 3d: sample `8`, hit `0.75`, avg `0.010261`, median `0.0207`, mae `0.018956`
- 5d: sample `8`, hit `0.75`, avg `0.011464`, median `0.013852`, mae `0.019267`
- 10d: sample `8`, hit `0.625`, avg `0.014702`, median `0.024811`, mae `0.023489`
- 20d: sample `8`, hit `1.0`, avg `0.059682`, median `0.062955`, mae `0.059682`
- 60d: sample `8`, hit `0.875`, avg `0.089216`, median `0.099838`, mae `0.100706`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.010261`, median `0.0207`, mae `0.018956`
- 5d: sample `8`, hit `0.75`, avg `0.011464`, median `0.013852`, mae `0.019267`
- 10d: sample `8`, hit `0.625`, avg `0.014702`, median `0.024811`, mae `0.023489`
- 20d: sample `8`, hit `1.0`, avg `0.059682`, median `0.062955`, mae `0.059682`
- 60d: sample `8`, hit `0.875`, avg `0.089216`, median `0.099838`, mae `0.100706`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.005324, 'median_return': 0.010897, 'mean_absolute_return': 0.019253, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.005862, 'median_return': 0.01152, 'mean_absolute_return': 0.023579, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.008679, 'median_return': 0.012215, 'mean_absolute_return': 0.034284, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.031343, 'median_return': 0.032954, 'mean_absolute_return': 0.047841, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.825, 'avg_return': 0.066044, 'median_return': 0.081441, 'mean_absolute_return': 0.08268, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010261, 'median_return': 0.0207, 'mean_absolute_return': 0.018956, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022679}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011464, 'median_return': 0.013852, 'mean_absolute_return': 0.019267, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.032969}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.014702, 'median_return': 0.024811, 'mean_absolute_return': 0.023489, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.04237}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.059682, 'median_return': 0.062955, 'mean_absolute_return': 0.059682, 'max_adverse_excursion': 0.031464, 'max_favorable_excursion': 0.07754}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.089216, 'median_return': 0.099838, 'mean_absolute_return': 0.100706, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.004775, 'median_return': 0.009349, 'mean_absolute_return': 0.019286, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.00524, 'median_return': 0.01152, 'mean_absolute_return': 0.024058, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.00801, 'median_return': 0.012215, 'mean_absolute_return': 0.035484, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.028194, 'median_return': 0.029348, 'mean_absolute_return': 0.046525, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.063469, 'median_return': 0.074246, 'mean_absolute_return': 0.080677, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.7875}, '60d': {'sample_size': 80, 'hit_rate': 0.825}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7875, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': 0.0, 'both_hit': 63, 'both_miss': 17}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.825, 'secondary_hit_rate': 0.825, 'primary_minus_secondary': 0.0, 'both_hit': 66, 'both_miss': 14}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.005324, 'median_return': 0.010897, 'mean_absolute_return': 0.019253, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.005862, 'median_return': 0.01152, 'mean_absolute_return': 0.023579, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.008679, 'median_return': 0.012215, 'mean_absolute_return': 0.034284, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.031343, 'median_return': 0.032954, 'mean_absolute_return': 0.047841, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.825, 'avg_return': 0.066044, 'median_return': 0.081441, 'mean_absolute_return': 0.08268, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000998`, median `0.004542`, mae `0.01293`
- 5d: sample `20`, hit `0.5`, avg `-0.000165`, median `0.006609`, mae `0.016006`
- 10d: sample `20`, hit `0.6`, avg `-0.004112`, median `0.004196`, mae `0.023229`
- 20d: sample `20`, hit `0.7`, avg `0.01599`, median `0.032299`, mae `0.039849`
- 60d: sample `20`, hit `0.85`, avg `0.058882`, median `0.065995`, mae `0.068908`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.005324`, median `0.010897`, mae `0.019253`
- 5d: sample `80`, hit `0.6125`, avg `0.005862`, median `0.01152`, mae `0.023579`
- 10d: sample `80`, hit `0.6125`, avg `0.008679`, median `0.012215`, mae `0.034284`
- 20d: sample `80`, hit `0.7875`, avg `0.031343`, median `0.032954`, mae `0.047841`
- 60d: sample `80`, hit `0.825`, avg `0.066044`, median `0.081441`, mae `0.08268`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000998`, median `0.004542`, mae `0.01293`
- 5d: sample `20`, hit `0.5`, avg `-0.000165`, median `0.006609`, mae `0.016006`
- 10d: sample `20`, hit `0.6`, avg `-0.004112`, median `0.004196`, mae `0.023229`
- 20d: sample `20`, hit `0.7`, avg `0.01599`, median `0.032299`, mae `0.039849`
- 60d: sample `20`, hit `0.85`, avg `0.058882`, median `0.065995`, mae `0.068908`

### breadth_conflicted_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.005324`, median `0.010897`, mae `0.019253`
- 5d: sample `80`, hit `0.6125`, avg `0.005862`, median `0.01152`, mae `0.023579`
- 10d: sample `80`, hit `0.6125`, avg `0.008679`, median `0.012215`, mae `0.034284`
- 20d: sample `80`, hit `0.7875`, avg `0.031343`, median `0.032954`, mae `0.047841`
- 60d: sample `80`, hit `0.825`, avg `0.066044`, median `0.081441`, mae `0.08268`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004952`, median `0.009349`, mae `0.022229`
- 5d: sample `40`, hit `0.6`, avg `0.00577`, median `0.014114`, mae `0.028369`
- 10d: sample `40`, hit `0.575`, avg `0.012294`, median `0.023905`, mae `0.042131`
- 20d: sample `40`, hit `0.775`, avg `0.032613`, median `0.030922`, mae `0.051756`
- 60d: sample `40`, hit `0.8`, avg `0.065084`, median `0.074246`, mae `0.088779`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000998`, median `0.004542`, mae `0.01293`
- 5d: sample `20`, hit `0.5`, avg `-0.000165`, median `0.006609`, mae `0.016006`
- 10d: sample `20`, hit `0.6`, avg `-0.004112`, median `0.004196`, mae `0.023229`
- 20d: sample `20`, hit `0.7`, avg `0.01599`, median `0.032299`, mae `0.039849`
- 60d: sample `20`, hit `0.85`, avg `0.058882`, median `0.065995`, mae `0.068908`

### bounce_without_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.006765`, median `0.012542`, mae `0.021361`
- 5d: sample `60`, hit `0.65`, avg `0.007871`, median `0.013852`, mae `0.026103`
- 10d: sample `60`, hit `0.6167`, avg `0.012943`, median `0.023826`, mae `0.037969`
- 20d: sample `60`, hit `0.8167`, avg `0.036461`, median `0.034158`, mae `0.050505`
- 60d: sample `60`, hit `0.8167`, avg `0.068431`, median `0.085781`, mae `0.08727`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.625`, avg `0.005324`, median `0.010897`, mae `0.019253`
- 5d: sample `80`, hit `0.6125`, avg `0.005862`, median `0.01152`, mae `0.023579`
- 10d: sample `80`, hit `0.6125`, avg `0.008679`, median `0.012215`, mae `0.034284`
- 20d: sample `80`, hit `0.7875`, avg `0.031343`, median `0.032954`, mae `0.047841`
- 60d: sample `80`, hit `0.825`, avg `0.066044`, median `0.081441`, mae `0.08268`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.005324`, median `0.010897`, mae `0.019253`
- 5d: sample `80`, hit `0.6125`, avg `0.005862`, median `0.01152`, mae `0.023579`
- 10d: sample `80`, hit `0.6125`, avg `0.008679`, median `0.012215`, mae `0.034284`
- 20d: sample `80`, hit `0.7875`, avg `0.031343`, median `0.032954`, mae `0.047841`
- 60d: sample `80`, hit `0.825`, avg `0.066044`, median `0.081441`, mae `0.08268`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.005324`, median `0.010897`, mae `0.019253`
- 5d: sample `80`, hit `0.6125`, avg `0.005862`, median `0.01152`, mae `0.023579`
- 10d: sample `80`, hit `0.6125`, avg `0.008679`, median `0.012215`, mae `0.034284`
- 20d: sample `80`, hit `0.7875`, avg `0.031343`, median `0.032954`, mae `0.047841`
- 60d: sample `80`, hit `0.825`, avg `0.066044`, median `0.081441`, mae `0.08268`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.005324`, median `0.010897`, mae `0.019253`
- 5d: sample `80`, hit `0.6125`, avg `0.005862`, median `0.01152`, mae `0.023579`
- 10d: sample `80`, hit `0.6125`, avg `0.008679`, median `0.012215`, mae `0.034284`
- 20d: sample `80`, hit `0.7875`, avg `0.031343`, median `0.032954`, mae `0.047841`
- 60d: sample `80`, hit `0.825`, avg `0.066044`, median `0.081441`, mae `0.08268`

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
