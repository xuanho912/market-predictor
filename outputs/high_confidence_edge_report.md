# High Confidence Edge Report

Generated at: `2026-11-19T20:40:57.732725+00:00`

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
- 3d: sample `80`, hit `0.6`, avg `0.006192`, median `0.008447`, mae `0.022493`
- 5d: sample `80`, hit `0.65`, avg `0.008995`, median `0.010572`, mae `0.024488`
- 10d: sample `80`, hit `0.675`, avg `0.018345`, median `0.01609`, mae `0.037174`
- 20d: sample `80`, hit `0.7`, avg `0.030247`, median `0.038387`, mae `0.055027`
- 60d: sample `80`, hit `0.5875`, avg `0.042044`, median `0.054472`, mae `0.088431`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.019725`, median `0.028518`, mae `0.029319`
- 5d: sample `8`, hit `0.75`, avg `0.018908`, median `0.028794`, mae `0.026445`
- 10d: sample `8`, hit `0.875`, avg `0.04092`, median `0.046989`, mae `0.041939`
- 20d: sample `8`, hit `1.0`, avg `0.068048`, median `0.056586`, mae `0.068048`
- 60d: sample `8`, hit `0.625`, avg `0.076573`, median `0.113901`, mae `0.111516`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.008082`, median `0.01272`, mae `0.017173`
- 5d: sample `8`, hit `0.625`, avg `0.003343`, median `0.002223`, mae `0.018197`
- 10d: sample `8`, hit `0.5`, avg `0.000688`, median `0.015974`, mae `0.039532`
- 20d: sample `8`, hit `0.625`, avg `0.022529`, median `0.030606`, mae `0.042909`
- 60d: sample `8`, hit `0.375`, avg `0.01279`, median `-0.007199`, mae `0.074485`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.008082, 'median_return': 0.01272, 'mean_absolute_return': 0.017173, 'max_adverse_excursion': -0.029226, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003343, 'median_return': 0.002223, 'mean_absolute_return': 0.018197, 'max_adverse_excursion': -0.032741, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000688, 'median_return': 0.015974, 'mean_absolute_return': 0.039532, 'max_adverse_excursion': -0.070803, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.022529, 'median_return': 0.030606, 'mean_absolute_return': 0.042909, 'max_adverse_excursion': -0.073721, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.01279, 'median_return': -0.007199, 'mean_absolute_return': 0.074485, 'max_adverse_excursion': -0.069357, 'max_favorable_excursion': 0.156899}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.005982, 'median_return': 0.008447, 'mean_absolute_return': 0.023084, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.069923}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.009623, 'median_return': 0.010832, 'mean_absolute_return': 0.025188, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.020306, 'median_return': 0.018992, 'mean_absolute_return': 0.036912, 'max_adverse_excursion': -0.156643, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.031104, 'median_return': 0.039212, 'mean_absolute_return': 0.056374, 'max_adverse_excursion': -0.247086, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.045294, 'median_return': 0.065834, 'mean_absolute_return': 0.08998, 'max_adverse_excursion': -0.32028, 'max_favorable_excursion': 0.268228}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4}, '5d': {'sample_size': 80, 'hit_rate': 0.35}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.3}, '60d': {'sample_size': 80, 'hit_rate': 0.4125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.4, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.006192, 'median_return': 0.008447, 'mean_absolute_return': 0.022493, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.069923}, '5d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.008995, 'median_return': 0.010572, 'mean_absolute_return': 0.024488, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.018345, 'median_return': 0.01609, 'mean_absolute_return': 0.037174, 'max_adverse_excursion': -0.156643, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.030247, 'median_return': 0.038387, 'mean_absolute_return': 0.055027, 'max_adverse_excursion': -0.247086, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.042044, 'median_return': 0.054472, 'mean_absolute_return': 0.088431, 'max_adverse_excursion': -0.32028, 'max_favorable_excursion': 0.268228}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.005083`, median `0.008733`, mae `0.018361`
- 5d: sample `20`, hit `0.65`, avg `0.00361`, median `0.007726`, mae `0.017524`
- 10d: sample `20`, hit `0.45`, avg `0.001335`, median `-0.000336`, mae `0.026445`
- 20d: sample `20`, hit `0.55`, avg `0.010842`, median `0.009738`, mae `0.038285`
- 60d: sample `20`, hit `0.5`, avg `0.020845`, median `0.007623`, mae `0.067421`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.001499`, median `0.006898`, mae `0.020904`
- 5d: sample `60`, hit `0.6167`, avg `0.003329`, median `0.005846`, mae `0.020527`
- 10d: sample `60`, hit `0.6167`, avg `0.009901`, median `0.008464`, mae `0.031448`
- 20d: sample `60`, hit `0.6333`, avg `0.018931`, median `0.030297`, mae `0.049538`
- 60d: sample `60`, hit `0.5333`, avg `0.022998`, median `0.003488`, mae `0.077913`

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
- 3d: sample `60`, hit `0.55`, avg `0.001499`, median `0.006898`, mae `0.020904`
- 5d: sample `60`, hit `0.6167`, avg `0.003329`, median `0.005846`, mae `0.020527`
- 10d: sample `60`, hit `0.6167`, avg `0.009901`, median `0.008464`, mae `0.031448`
- 20d: sample `60`, hit `0.6333`, avg `0.018931`, median `0.030297`, mae `0.049538`
- 60d: sample `60`, hit `0.5333`, avg `0.022998`, median `0.003488`, mae `0.077913`

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
- 3d: sample `80`, hit `0.6`, avg `0.006192`, median `0.008447`, mae `0.022493`
- 5d: sample `80`, hit `0.65`, avg `0.008995`, median `0.010572`, mae `0.024488`
- 10d: sample `80`, hit `0.675`, avg `0.018345`, median `0.01609`, mae `0.037174`
- 20d: sample `80`, hit `0.7`, avg `0.030247`, median `0.038387`, mae `0.055027`
- 60d: sample `80`, hit `0.5875`, avg `0.042044`, median `0.054472`, mae `0.088431`

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
- 3d: sample `80`, hit `0.6`, avg `0.006192`, median `0.008447`, mae `0.022493`
- 5d: sample `80`, hit `0.65`, avg `0.008995`, median `0.010572`, mae `0.024488`
- 10d: sample `80`, hit `0.675`, avg `0.018345`, median `0.01609`, mae `0.037174`
- 20d: sample `80`, hit `0.7`, avg `0.030247`, median `0.038387`, mae `0.055027`
- 60d: sample `80`, hit `0.5875`, avg `0.042044`, median `0.054472`, mae `0.088431`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
