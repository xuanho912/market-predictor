# High Confidence Edge Report

Generated at: `2026-11-20T02:01:48.409188+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `208`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `208`, gate `stronger_evidence`
- 5d: completed `208`, gate `stronger_evidence`
- 10d: completed `208`, gate `stronger_evidence`
- 20d: completed `208`, gate `stronger_evidence`
- 60d: completed `208`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.625`, avg `0.007862`, median `0.007729`, mae `0.022713`
- 5d: sample `80`, hit `0.55`, avg `0.013062`, median `0.00438`, mae `0.028628`
- 10d: sample `80`, hit `0.75`, avg `0.032398`, median `0.034952`, mae `0.043933`
- 20d: sample `80`, hit `0.925`, avg `0.070886`, median `0.06925`, mae `0.074803`
- 60d: sample `80`, hit `0.925`, avg `0.137117`, median `0.130696`, mae `0.141063`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.005957`, median `-0.009147`, mae `0.019529`
- 5d: sample `8`, hit `0.125`, avg `-0.007021`, median `-0.00697`, mae `0.018844`
- 10d: sample `8`, hit `0.625`, avg `0.011987`, median `0.015974`, mae `0.023702`
- 20d: sample `8`, hit `1.0`, avg `0.066842`, median `0.076296`, mae `0.066842`
- 60d: sample `8`, hit `1.0`, avg `0.123538`, median `0.133324`, mae `0.123538`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.005957`, median `-0.009147`, mae `0.019529`
- 5d: sample `8`, hit `0.125`, avg `-0.007021`, median `-0.00697`, mae `0.018844`
- 10d: sample `8`, hit `0.625`, avg `0.011987`, median `0.015974`, mae `0.023702`
- 20d: sample `8`, hit `1.0`, avg `0.066842`, median `0.076296`, mae `0.066842`
- 60d: sample `8`, hit `1.0`, avg `0.123538`, median `0.133324`, mae `0.123538`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.005957, 'median_return': -0.009147, 'mean_absolute_return': 0.019529, 'max_adverse_excursion': -0.037834, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.007021, 'median_return': -0.00697, 'mean_absolute_return': 0.018844, 'max_adverse_excursion': -0.03572, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011987, 'median_return': 0.015974, 'mean_absolute_return': 0.023702, 'max_adverse_excursion': -0.031484, 'max_favorable_excursion': 0.050818}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.066842, 'median_return': 0.076296, 'mean_absolute_return': 0.066842, 'max_adverse_excursion': 0.020118, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.123538, 'median_return': 0.133324, 'mean_absolute_return': 0.123538, 'max_adverse_excursion': 0.048963, 'max_favorable_excursion': 0.156899}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.009398, 'median_return': 0.008447, 'mean_absolute_return': 0.023067, 'max_adverse_excursion': -0.076776, 'max_favorable_excursion': 0.079056}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.015293, 'median_return': 0.015202, 'mean_absolute_return': 0.029716, 'max_adverse_excursion': -0.040197, 'max_favorable_excursion': 0.090739}, '10d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.034666, 'median_return': 0.037328, 'mean_absolute_return': 0.04618, 'max_adverse_excursion': -0.047337, 'max_favorable_excursion': 0.125958}, '20d': {'sample_size': 72, 'hit_rate': 0.9167, 'avg_return': 0.071336, 'median_return': 0.065459, 'mean_absolute_return': 0.075688, 'max_adverse_excursion': -0.062877, 'max_favorable_excursion': 0.20526}, '60d': {'sample_size': 72, 'hit_rate': 0.9167, 'avg_return': 0.138626, 'median_return': 0.130696, 'mean_absolute_return': 0.14301, 'max_adverse_excursion': -0.065523, 'max_favorable_excursion': 0.29713}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.375}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.25}, '20d': {'sample_size': 80, 'hit_rate': 0.075}, '60d': {'sample_size': 80, 'hit_rate': 0.075}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.5, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.075, 'secondary_hit_rate': 0.925, 'primary_minus_secondary': -0.85, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.075, 'secondary_hit_rate': 0.925, 'primary_minus_secondary': -0.85, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.007862, 'median_return': 0.007729, 'mean_absolute_return': 0.022713, 'max_adverse_excursion': -0.076776, 'max_favorable_excursion': 0.079056}, '5d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.013062, 'median_return': 0.00438, 'mean_absolute_return': 0.028628, 'max_adverse_excursion': -0.040197, 'max_favorable_excursion': 0.090739}, '10d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.032398, 'median_return': 0.034952, 'mean_absolute_return': 0.043933, 'max_adverse_excursion': -0.047337, 'max_favorable_excursion': 0.125958}, '20d': {'sample_size': 80, 'hit_rate': 0.925, 'avg_return': 0.070886, 'median_return': 0.06925, 'mean_absolute_return': 0.074803, 'max_adverse_excursion': -0.062877, 'max_favorable_excursion': 0.20526}, '60d': {'sample_size': 80, 'hit_rate': 0.925, 'avg_return': 0.137117, 'median_return': 0.130696, 'mean_absolute_return': 0.141063, 'max_adverse_excursion': -0.065523, 'max_favorable_excursion': 0.29713}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00571`, median `0.01272`, mae `0.019125`
- 5d: sample `20`, hit `0.5`, avg `0.007988`, median `0.015202`, mae `0.02513`
- 10d: sample `20`, hit `0.75`, avg `0.024138`, median `0.032575`, mae `0.034343`
- 20d: sample `20`, hit `0.85`, avg `0.048166`, median `0.059673`, mae `0.055786`
- 60d: sample `20`, hit `0.9`, avg `0.094155`, median `0.120937`, mae `0.100938`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.006859`, median `0.008447`, mae `0.023678`
- 5d: sample `60`, hit `0.55`, avg `0.013292`, median `0.012519`, mae `0.028424`
- 10d: sample `60`, hit `0.75`, avg `0.032718`, median `0.035154`, mae `0.044157`
- 20d: sample `60`, hit `0.9167`, avg `0.069246`, median `0.063619`, mae `0.074242`
- 60d: sample `60`, hit `0.9167`, avg `0.131328`, median `0.120937`, mae `0.134405`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.006859`, median `0.008447`, mae `0.023678`
- 5d: sample `60`, hit `0.55`, avg `0.013292`, median `0.012519`, mae `0.028424`
- 10d: sample `60`, hit `0.75`, avg `0.032718`, median `0.035154`, mae `0.044157`
- 20d: sample `60`, hit `0.9167`, avg `0.069246`, median `0.063619`, mae `0.074242`
- 60d: sample `60`, hit `0.9167`, avg `0.131328`, median `0.120937`, mae `0.134405`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.007862`, median `0.007729`, mae `0.022713`
- 5d: sample `80`, hit `0.55`, avg `0.013062`, median `0.00438`, mae `0.028628`
- 10d: sample `80`, hit `0.75`, avg `0.032398`, median `0.034952`, mae `0.043933`
- 20d: sample `80`, hit `0.925`, avg `0.070886`, median `0.06925`, mae `0.074803`
- 60d: sample `80`, hit `0.925`, avg `0.137117`, median `0.130696`, mae `0.141063`

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
- 3d: sample `80`, hit `0.625`, avg `0.007862`, median `0.007729`, mae `0.022713`
- 5d: sample `80`, hit `0.55`, avg `0.013062`, median `0.00438`, mae `0.028628`
- 10d: sample `80`, hit `0.75`, avg `0.032398`, median `0.034952`, mae `0.043933`
- 20d: sample `80`, hit `0.925`, avg `0.070886`, median `0.06925`, mae `0.074803`
- 60d: sample `80`, hit `0.925`, avg `0.137117`, median `0.130696`, mae `0.141063`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
