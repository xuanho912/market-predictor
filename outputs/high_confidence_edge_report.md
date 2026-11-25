# High Confidence Edge Report

Generated at: `2026-11-25T05:06:57.000390+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `220`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `220`, gate `stronger_evidence`
- 5d: completed `220`, gate `stronger_evidence`
- 10d: completed `220`, gate `stronger_evidence`
- 20d: completed `220`, gate `stronger_evidence`
- 60d: completed `220`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.5`, avg `0.001871`, median `0.003429`, mae `0.022621`
- 5d: sample `80`, hit `0.5625`, avg `0.005122`, median `0.003435`, mae `0.026737`
- 10d: sample `80`, hit `0.6`, avg `0.011755`, median `0.005519`, mae `0.028125`
- 20d: sample `80`, hit `0.55`, avg `0.008501`, median `0.006559`, mae `0.0373`
- 60d: sample `80`, hit `0.725`, avg `0.05066`, median `0.062004`, mae `0.076945`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.004061`, median `0.010671`, mae `0.023786`
- 5d: sample `8`, hit `0.75`, avg `0.013582`, median `0.005082`, mae `0.023601`
- 10d: sample `8`, hit `0.625`, avg `0.023553`, median `0.005477`, mae `0.030057`
- 20d: sample `8`, hit `0.875`, avg `0.037298`, median `0.036029`, mae `0.041814`
- 60d: sample `8`, hit `0.625`, avg `0.08833`, median `0.113901`, mae `0.105679`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.004061`, median `0.010671`, mae `0.023786`
- 5d: sample `8`, hit `0.75`, avg `0.013582`, median `0.005082`, mae `0.023601`
- 10d: sample `8`, hit `0.625`, avg `0.023553`, median `0.005477`, mae `0.030057`
- 20d: sample `8`, hit `0.875`, avg `0.037298`, median `0.036029`, mae `0.041814`
- 60d: sample `8`, hit `0.625`, avg `0.08833`, median `0.113901`, mae `0.105679`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004061, 'median_return': 0.010671, 'mean_absolute_return': 0.023786, 'max_adverse_excursion': -0.036638, 'max_favorable_excursion': 0.036579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013582, 'median_return': 0.005082, 'mean_absolute_return': 0.023601, 'max_adverse_excursion': -0.027012, 'max_favorable_excursion': 0.056292}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.023553, 'median_return': 0.005477, 'mean_absolute_return': 0.030057, 'max_adverse_excursion': -0.018077, 'max_favorable_excursion': 0.123482}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.037298, 'median_return': 0.036029, 'mean_absolute_return': 0.041814, 'max_adverse_excursion': -0.018063, 'max_favorable_excursion': 0.125356}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.08833, 'median_return': 0.113901, 'mean_absolute_return': 0.105679, 'max_adverse_excursion': -0.030956, 'max_favorable_excursion': 0.355869}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.001627, 'median_return': -6.1e-05, 'mean_absolute_return': 0.022492, 'max_adverse_excursion': -0.057125, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.004182, 'median_return': 0.002462, 'mean_absolute_return': 0.027086, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.010444, 'median_return': 0.006053, 'mean_absolute_return': 0.02791, 'max_adverse_excursion': -0.088606, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.005302, 'median_return': 0.001287, 'mean_absolute_return': 0.036798, 'max_adverse_excursion': -0.098675, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.046474, 'median_return': 0.062004, 'mean_absolute_return': 0.073752, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.193298}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.4625}, '20d': {'sample_size': 80, 'hit_rate': 0.55}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.0625, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006734, 'median_return': 0.010671, 'mean_absolute_return': 0.025634, 'max_adverse_excursion': -0.047619, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.014071, 'median_return': 0.012749, 'mean_absolute_return': 0.03201, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.02009, 'median_return': 0.011842, 'mean_absolute_return': 0.03756, 'max_adverse_excursion': -0.088606, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.019633, 'median_return': 0.016764, 'mean_absolute_return': 0.044363, 'max_adverse_excursion': -0.071567, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.084524, 'median_return': 0.062195, 'mean_absolute_return': 0.091464, 'max_adverse_excursion': -0.030956, 'max_favorable_excursion': 0.355869}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': 0.000249, 'median_return': -0.000756, 'mean_absolute_return': 0.021617, 'max_adverse_excursion': -0.057125, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.002139, 'median_return': 0.002223, 'mean_absolute_return': 0.02498, 'max_adverse_excursion': -0.061828, 'max_favorable_excursion': 0.083508}, '10d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.008977, 'median_return': 0.005519, 'mean_absolute_return': 0.02498, 'max_adverse_excursion': -0.049389, 'max_favorable_excursion': 0.107737}, '20d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.004791, 'median_return': 0.001287, 'mean_absolute_return': 0.034945, 'max_adverse_excursion': -0.098675, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.039371, 'median_return': 0.062004, 'mean_absolute_return': 0.072105, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.156899}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006734`, median `0.010671`, mae `0.025634`
- 5d: sample `20`, hit `0.65`, avg `0.014071`, median `0.012749`, mae `0.03201`
- 10d: sample `20`, hit `0.65`, avg `0.02009`, median `0.011842`, mae `0.03756`
- 20d: sample `20`, hit `0.7`, avg `0.019633`, median `0.016764`, mae `0.044363`
- 60d: sample `20`, hit `0.85`, avg `0.084524`, median `0.062195`, mae `0.091464`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `0.000249`, median `-0.000756`, mae `0.021617`
- 5d: sample `60`, hit `0.5333`, avg `0.002139`, median `0.002223`, mae `0.02498`
- 10d: sample `60`, hit `0.5833`, avg `0.008977`, median `0.005519`, mae `0.02498`
- 20d: sample `60`, hit `0.5`, avg `0.004791`, median `0.001287`, mae `0.034945`
- 60d: sample `60`, hit `0.6833`, avg `0.039371`, median `0.062004`, mae `0.072105`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006734`, median `0.010671`, mae `0.025634`
- 5d: sample `20`, hit `0.65`, avg `0.014071`, median `0.012749`, mae `0.03201`
- 10d: sample `20`, hit `0.65`, avg `0.02009`, median `0.011842`, mae `0.03756`
- 20d: sample `20`, hit `0.7`, avg `0.019633`, median `0.016764`, mae `0.044363`
- 60d: sample `20`, hit `0.85`, avg `0.084524`, median `0.062195`, mae `0.091464`

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
- 3d: sample `20`, hit `0.6`, avg `0.006734`, median `0.010671`, mae `0.025634`
- 5d: sample `20`, hit `0.65`, avg `0.014071`, median `0.012749`, mae `0.03201`
- 10d: sample `20`, hit `0.65`, avg `0.02009`, median `0.011842`, mae `0.03756`
- 20d: sample `20`, hit `0.7`, avg `0.019633`, median `0.016764`, mae `0.044363`
- 60d: sample `20`, hit `0.85`, avg `0.084524`, median `0.062195`, mae `0.091464`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `0.000249`, median `-0.000756`, mae `0.021617`
- 5d: sample `60`, hit `0.5333`, avg `0.002139`, median `0.002223`, mae `0.02498`
- 10d: sample `60`, hit `0.5833`, avg `0.008977`, median `0.005519`, mae `0.02498`
- 20d: sample `60`, hit `0.5`, avg `0.004791`, median `0.001287`, mae `0.034945`
- 60d: sample `60`, hit `0.6833`, avg `0.039371`, median `0.062004`, mae `0.072105`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006734`, median `0.010671`, mae `0.025634`
- 5d: sample `20`, hit `0.65`, avg `0.014071`, median `0.012749`, mae `0.03201`
- 10d: sample `20`, hit `0.65`, avg `0.02009`, median `0.011842`, mae `0.03756`
- 20d: sample `20`, hit `0.7`, avg `0.019633`, median `0.016764`, mae `0.044363`
- 60d: sample `20`, hit `0.85`, avg `0.084524`, median `0.062195`, mae `0.091464`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `0.001871`, median `0.003429`, mae `0.022621`
- 5d: sample `80`, hit `0.5625`, avg `0.005122`, median `0.003435`, mae `0.026737`
- 10d: sample `80`, hit `0.6`, avg `0.011755`, median `0.005519`, mae `0.028125`
- 20d: sample `80`, hit `0.55`, avg `0.008501`, median `0.006559`, mae `0.0373`
- 60d: sample `80`, hit `0.725`, avg `0.05066`, median `0.062004`, mae `0.076945`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006734`, median `0.010671`, mae `0.025634`
- 5d: sample `20`, hit `0.65`, avg `0.014071`, median `0.012749`, mae `0.03201`
- 10d: sample `20`, hit `0.65`, avg `0.02009`, median `0.011842`, mae `0.03756`
- 20d: sample `20`, hit `0.7`, avg `0.019633`, median `0.016764`, mae `0.044363`
- 60d: sample `20`, hit `0.85`, avg `0.084524`, median `0.062195`, mae `0.091464`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006734`, median `0.010671`, mae `0.025634`
- 5d: sample `20`, hit `0.65`, avg `0.014071`, median `0.012749`, mae `0.03201`
- 10d: sample `20`, hit `0.65`, avg `0.02009`, median `0.011842`, mae `0.03756`
- 20d: sample `20`, hit `0.7`, avg `0.019633`, median `0.016764`, mae `0.044363`
- 60d: sample `20`, hit `0.85`, avg `0.084524`, median `0.062195`, mae `0.091464`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `0.001871`, median `0.003429`, mae `0.022621`
- 5d: sample `80`, hit `0.5625`, avg `0.005122`, median `0.003435`, mae `0.026737`
- 10d: sample `80`, hit `0.6`, avg `0.011755`, median `0.005519`, mae `0.028125`
- 20d: sample `80`, hit `0.55`, avg `0.008501`, median `0.006559`, mae `0.0373`
- 60d: sample `80`, hit `0.725`, avg `0.05066`, median `0.062004`, mae `0.076945`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
