# High Confidence Edge Report

Generated at: `2026-11-20T12:12:41.802847+00:00`

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
- 3d: sample `80`, hit `0.5875`, avg `0.005744`, median `0.007812`, mae `0.021469`
- 5d: sample `80`, hit `0.6375`, avg `0.008611`, median `0.007726`, mae `0.023534`
- 10d: sample `80`, hit `0.675`, avg `0.018242`, median `0.018992`, mae `0.037291`
- 20d: sample `80`, hit `0.7125`, avg `0.031963`, median `0.039212`, mae `0.0537`
- 60d: sample `80`, hit `0.5875`, avg `0.042632`, median `0.054472`, mae `0.089019`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.013871`, median `0.010671`, mae `0.023731`
- 5d: sample `8`, hit `0.625`, avg `0.009745`, median `0.005082`, mae `0.021021`
- 10d: sample `8`, hit `0.875`, avg `0.035268`, median `0.046989`, mae `0.043907`
- 20d: sample `8`, hit `1.0`, avg `0.064782`, median `0.060628`, mae `0.064782`
- 60d: sample `8`, hit `0.75`, avg `0.114108`, median `0.162502`, mae `0.127741`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.008082`, median `0.01272`, mae `0.017173`
- 5d: sample `8`, hit `0.625`, avg `0.003343`, median `0.002223`, mae `0.018197`
- 10d: sample `8`, hit `0.5`, avg `0.000688`, median `0.015974`, mae `0.039532`
- 20d: sample `8`, hit `0.625`, avg `0.022529`, median `0.030606`, mae `0.042909`
- 60d: sample `8`, hit `0.375`, avg `0.01279`, median `-0.007199`, mae `0.074485`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.008082, 'median_return': 0.01272, 'mean_absolute_return': 0.017173, 'max_adverse_excursion': -0.029226, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003343, 'median_return': 0.002223, 'mean_absolute_return': 0.018197, 'max_adverse_excursion': -0.032741, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000688, 'median_return': 0.015974, 'mean_absolute_return': 0.039532, 'max_adverse_excursion': -0.070803, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.022529, 'median_return': 0.030606, 'mean_absolute_return': 0.042909, 'max_adverse_excursion': -0.073721, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.01279, 'median_return': -0.007199, 'mean_absolute_return': 0.074485, 'max_adverse_excursion': -0.069357, 'max_favorable_excursion': 0.156899}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.005484, 'median_return': 0.007812, 'mean_absolute_return': 0.021946, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.009196, 'median_return': 0.010572, 'mean_absolute_return': 0.024127, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.020193, 'median_return': 0.019564, 'mean_absolute_return': 0.037042, 'max_adverse_excursion': -0.156643, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.033012, 'median_return': 0.039227, 'mean_absolute_return': 0.054899, 'max_adverse_excursion': -0.247086, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.045948, 'median_return': 0.065834, 'mean_absolute_return': 0.090634, 'max_adverse_excursion': -0.32028, 'max_favorable_excursion': 0.268228}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4125}, '5d': {'sample_size': 80, 'hit_rate': 0.3625}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.2875}, '60d': {'sample_size': 80, 'hit_rate': 0.4125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.425, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.005744, 'median_return': 0.007812, 'mean_absolute_return': 0.021469, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.008611, 'median_return': 0.007726, 'mean_absolute_return': 0.023534, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.018242, 'median_return': 0.018992, 'mean_absolute_return': 0.037291, 'max_adverse_excursion': -0.156643, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.031963, 'median_return': 0.039212, 'mean_absolute_return': 0.0537, 'max_adverse_excursion': -0.247086, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.042632, 'median_return': 0.054472, 'mean_absolute_return': 0.089019, 'max_adverse_excursion': -0.32028, 'max_favorable_excursion': 0.268228}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003945`, median `0.007289`, mae `0.017424`
- 5d: sample `20`, hit `0.6`, avg `0.000676`, median `0.002223`, mae `0.015683`
- 10d: sample `20`, hit `0.45`, avg `0.000896`, median `-0.000336`, mae `0.026884`
- 20d: sample `20`, hit `0.55`, avg `0.012537`, median `0.009738`, mae `0.036589`
- 60d: sample `20`, hit `0.5`, avg `0.023077`, median `0.048963`, mae `0.069652`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.001945`, median `0.006898`, mae `0.020224`
- 5d: sample `60`, hit `0.6167`, avg `0.003722`, median `0.005846`, mae `0.01982`
- 10d: sample `60`, hit `0.6167`, avg `0.01015`, median `0.008464`, mae `0.031991`
- 20d: sample `60`, hit `0.65`, avg `0.022152`, median `0.030606`, mae `0.0487`
- 60d: sample `60`, hit `0.5333`, avg `0.024534`, median `0.003488`, mae `0.079449`

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
- 3d: sample `60`, hit `0.55`, avg `0.001945`, median `0.006898`, mae `0.020224`
- 5d: sample `60`, hit `0.6167`, avg `0.003722`, median `0.005846`, mae `0.01982`
- 10d: sample `60`, hit `0.6167`, avg `0.01015`, median `0.008464`, mae `0.031991`
- 20d: sample `60`, hit `0.65`, avg `0.022152`, median `0.030606`, mae `0.0487`
- 60d: sample `60`, hit `0.5333`, avg `0.024534`, median `0.003488`, mae `0.079449`

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
- 3d: sample `80`, hit `0.5875`, avg `0.005744`, median `0.007812`, mae `0.021469`
- 5d: sample `80`, hit `0.6375`, avg `0.008611`, median `0.007726`, mae `0.023534`
- 10d: sample `80`, hit `0.675`, avg `0.018242`, median `0.018992`, mae `0.037291`
- 20d: sample `80`, hit `0.7125`, avg `0.031963`, median `0.039212`, mae `0.0537`
- 60d: sample `80`, hit `0.5875`, avg `0.042632`, median `0.054472`, mae `0.089019`

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
- 3d: sample `80`, hit `0.5875`, avg `0.005744`, median `0.007812`, mae `0.021469`
- 5d: sample `80`, hit `0.6375`, avg `0.008611`, median `0.007726`, mae `0.023534`
- 10d: sample `80`, hit `0.675`, avg `0.018242`, median `0.018992`, mae `0.037291`
- 20d: sample `80`, hit `0.7125`, avg `0.031963`, median `0.039212`, mae `0.0537`
- 60d: sample `80`, hit `0.5875`, avg `0.042632`, median `0.054472`, mae `0.089019`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
