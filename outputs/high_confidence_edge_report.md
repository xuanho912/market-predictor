# High Confidence Edge Report

Generated at: `2026-10-20T00:55:55.430300+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `116`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `116`, gate `stronger_evidence`
- 5d: completed `116`, gate `stronger_evidence`
- 10d: completed `116`, gate `stronger_evidence`
- 20d: completed `116`, gate `stronger_evidence`
- 60d: completed `116`, gate `stronger_evidence`

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
- 3d: sample `40`, hit `0.7`, avg `0.005901`, median `0.00745`, mae `0.014175`
- 5d: sample `40`, hit `0.675`, avg `0.008222`, median `0.012091`, mae `0.01694`
- 10d: sample `40`, hit `0.75`, avg `0.012288`, median `0.017201`, mae `0.020727`
- 20d: sample `40`, hit `0.85`, avg `0.032776`, median `0.034704`, mae `0.036117`
- 60d: sample `40`, hit `0.925`, avg `0.076928`, median `0.084301`, mae `0.082025`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002622`, median `-0.009843`, mae `0.020628`
- 5d: sample `40`, hit `0.45`, avg `-0.000557`, median `-0.005632`, mae `0.022423`
- 10d: sample `40`, hit `0.55`, avg `0.002279`, median `0.004306`, mae `0.03096`
- 20d: sample `40`, hit `0.725`, avg `0.025945`, median `0.024701`, mae `0.040895`
- 60d: sample `40`, hit `0.8`, avg `0.09766`, median `0.113901`, mae `0.108303`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.000905`, median `-0.001591`, mae `0.015632`
- 5d: sample `8`, hit `0.75`, avg `0.00475`, median `0.009709`, mae `0.016887`
- 10d: sample `8`, hit `0.625`, avg `0.0103`, median `0.015799`, mae `0.019526`
- 20d: sample `8`, hit `1.0`, avg `0.047185`, median `0.058396`, mae `0.047185`
- 60d: sample `8`, hit `0.875`, avg `0.080594`, median `0.121826`, mae `0.089385`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.000905`, median `-0.001591`, mae `0.015632`
- 5d: sample `8`, hit `0.75`, avg `0.00475`, median `0.009709`, mae `0.016887`
- 10d: sample `8`, hit `0.625`, avg `0.0103`, median `0.015799`, mae `0.019526`
- 20d: sample `8`, hit `1.0`, avg `0.047185`, median `0.058396`, mae `0.047185`
- 60d: sample `8`, hit `0.875`, avg `0.080594`, median `0.121826`, mae `0.089385`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.000905, 'median_return': -0.001591, 'mean_absolute_return': 0.015632, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.00475, 'median_return': 0.009709, 'mean_absolute_return': 0.016887, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.0103, 'median_return': 0.015799, 'mean_absolute_return': 0.019526, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.047185, 'median_return': 0.058396, 'mean_absolute_return': 0.047185, 'max_adverse_excursion': 0.017149, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.080594, 'median_return': 0.121826, 'mean_absolute_return': 0.089385, 'max_adverse_excursion': -0.035165, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001922, 'median_return': 0.004542, 'mean_absolute_return': 0.017599, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.060601}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.003731, 'median_return': 0.00288, 'mean_absolute_return': 0.019992, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.075704}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.006949, 'median_return': 0.012215, 'mean_absolute_return': 0.026546, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.084731}, '20d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.02738, 'median_return': 0.031464, 'mean_absolute_return': 0.037542, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.101843}, '60d': {'sample_size': 72, 'hit_rate': 0.8611, 'avg_return': 0.088039, 'median_return': 0.090809, 'mean_absolute_return': 0.095806, 'max_adverse_excursion': -0.064821, 'max_favorable_excursion': 0.212071}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.35}, '20d': {'sample_size': 80, 'hit_rate': 0.2125}, '60d': {'sample_size': 80, 'hit_rate': 0.1375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.575, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1375, 'secondary_hit_rate': 0.8625, 'primary_minus_secondary': -0.725, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.005901, 'median_return': 0.00745, 'mean_absolute_return': 0.014175, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.008222, 'median_return': 0.012091, 'mean_absolute_return': 0.01694, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.012288, 'median_return': 0.017201, 'mean_absolute_return': 0.020727, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.050818}, '20d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.032776, 'median_return': 0.034704, 'mean_absolute_return': 0.036117, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.076928, 'median_return': 0.084301, 'mean_absolute_return': 0.082025, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.002622, 'median_return': -0.009843, 'mean_absolute_return': 0.020628, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.060601}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.000557, 'median_return': -0.005632, 'mean_absolute_return': 0.022423, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.075704}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002279, 'median_return': 0.004306, 'mean_absolute_return': 0.03096, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.084731}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.025945, 'median_return': 0.024701, 'mean_absolute_return': 0.040895, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.101843}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.09766, 'median_return': 0.113901, 'mean_absolute_return': 0.108303, 'max_adverse_excursion': -0.064821, 'max_favorable_excursion': 0.212071}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.005901`, median `0.00745`, mae `0.014175`
- 5d: sample `40`, hit `0.675`, avg `0.008222`, median `0.012091`, mae `0.01694`
- 10d: sample `40`, hit `0.75`, avg `0.012288`, median `0.017201`, mae `0.020727`
- 20d: sample `40`, hit `0.85`, avg `0.032776`, median `0.034704`, mae `0.036117`
- 60d: sample `40`, hit `0.925`, avg `0.076928`, median `0.084301`, mae `0.082025`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002622`, median `-0.009843`, mae `0.020628`
- 5d: sample `40`, hit `0.45`, avg `-0.000557`, median `-0.005632`, mae `0.022423`
- 10d: sample `40`, hit `0.55`, avg `0.002279`, median `0.004306`, mae `0.03096`
- 20d: sample `40`, hit `0.725`, avg `0.025945`, median `0.024701`, mae `0.040895`
- 60d: sample `40`, hit `0.8`, avg `0.09766`, median `0.113901`, mae `0.108303`

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
- 3d: sample `40`, hit `0.7`, avg `0.005901`, median `0.00745`, mae `0.014175`
- 5d: sample `40`, hit `0.675`, avg `0.008222`, median `0.012091`, mae `0.01694`
- 10d: sample `40`, hit `0.75`, avg `0.012288`, median `0.017201`, mae `0.020727`
- 20d: sample `40`, hit `0.85`, avg `0.032776`, median `0.034704`, mae `0.036117`
- 60d: sample `40`, hit `0.925`, avg `0.076928`, median `0.084301`, mae `0.082025`

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
- 3d: sample `40`, hit `0.7`, avg `0.005901`, median `0.00745`, mae `0.014175`
- 5d: sample `40`, hit `0.675`, avg `0.008222`, median `0.012091`, mae `0.01694`
- 10d: sample `40`, hit `0.75`, avg `0.012288`, median `0.017201`, mae `0.020727`
- 20d: sample `40`, hit `0.85`, avg `0.032776`, median `0.034704`, mae `0.036117`
- 60d: sample `40`, hit `0.925`, avg `0.076928`, median `0.084301`, mae `0.082025`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002622`, median `-0.009843`, mae `0.020628`
- 5d: sample `40`, hit `0.45`, avg `-0.000557`, median `-0.005632`, mae `0.022423`
- 10d: sample `40`, hit `0.55`, avg `0.002279`, median `0.004306`, mae `0.03096`
- 20d: sample `40`, hit `0.725`, avg `0.025945`, median `0.024701`, mae `0.040895`
- 60d: sample `40`, hit `0.8`, avg `0.09766`, median `0.113901`, mae `0.108303`

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
- 3d: sample `80`, hit `0.55`, avg `0.00164`, median `0.003921`, mae `0.017402`
- 5d: sample `80`, hit `0.5625`, avg `0.003833`, median `0.006047`, mae `0.019682`
- 10d: sample `80`, hit `0.65`, avg `0.007284`, median `0.012215`, mae `0.025844`
- 20d: sample `80`, hit `0.7875`, avg `0.02936`, median `0.032954`, mae `0.038506`
- 60d: sample `80`, hit `0.8625`, avg `0.087294`, median `0.092689`, mae `0.095164`

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
- 3d: sample `80`, hit `0.55`, avg `0.00164`, median `0.003921`, mae `0.017402`
- 5d: sample `80`, hit `0.5625`, avg `0.003833`, median `0.006047`, mae `0.019682`
- 10d: sample `80`, hit `0.65`, avg `0.007284`, median `0.012215`, mae `0.025844`
- 20d: sample `80`, hit `0.7875`, avg `0.02936`, median `0.032954`, mae `0.038506`
- 60d: sample `80`, hit `0.8625`, avg `0.087294`, median `0.092689`, mae `0.095164`

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
- 3d: sample `80`, hit `0.55`, avg `0.00164`, median `0.003921`, mae `0.017402`
- 5d: sample `80`, hit `0.5625`, avg `0.003833`, median `0.006047`, mae `0.019682`
- 10d: sample `80`, hit `0.65`, avg `0.007284`, median `0.012215`, mae `0.025844`
- 20d: sample `80`, hit `0.7875`, avg `0.02936`, median `0.032954`, mae `0.038506`
- 60d: sample `80`, hit `0.8625`, avg `0.087294`, median `0.092689`, mae `0.095164`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
