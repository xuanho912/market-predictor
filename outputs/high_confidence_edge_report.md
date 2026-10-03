# High Confidence Edge Report

Generated at: `2026-10-03T16:21:07.707026+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `72`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `72`, gate `moderate_evidence`
- 5d: completed `72`, gate `moderate_evidence`
- 10d: completed `72`, gate `moderate_evidence`
- 20d: completed `72`, gate `moderate_evidence`
- 60d: completed `72`, gate `moderate_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.00448`, median `-0.003244`, mae `0.016388`
- 5d: sample `80`, hit `0.4625`, avg `-0.005432`, median `-0.002452`, mae `0.017761`
- 10d: sample `80`, hit `0.5`, avg `-0.005318`, median `0.000397`, mae `0.029279`
- 20d: sample `80`, hit `0.6`, avg `0.008373`, median `0.016027`, mae `0.041677`
- 60d: sample `80`, hit `0.85`, avg `0.053333`, median `0.059104`, mae `0.076429`

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
- 3d: sample `8`, hit `0.5`, avg `-0.001136`, median `0.003898`, mae `0.010042`
- 5d: sample `8`, hit `0.625`, avg `0.001316`, median `0.009651`, mae `0.010072`
- 10d: sample `8`, hit `0.625`, avg `0.007222`, median `0.014793`, mae `0.022199`
- 20d: sample `8`, hit `0.875`, avg `0.024373`, median `0.034024`, mae `0.045211`
- 60d: sample `8`, hit `1.0`, avg `0.045787`, median `0.05019`, mae `0.045787`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.011601`, median `0.012486`, mae `0.0126`
- 5d: sample `8`, hit `0.875`, avg `0.008475`, median `0.008152`, mae `0.011784`
- 10d: sample `8`, hit `0.75`, avg `0.006179`, median `0.011619`, mae `0.015235`
- 20d: sample `8`, hit `0.75`, avg `0.022474`, median `0.045453`, mae `0.028373`
- 60d: sample `8`, hit `1.0`, avg `0.068211`, median `0.084216`, mae `0.068211`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.011601, 'median_return': 0.012486, 'mean_absolute_return': 0.0126, 'max_adverse_excursion': -0.003995, 'max_favorable_excursion': 0.023486}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.008475, 'median_return': 0.008152, 'mean_absolute_return': 0.011784, 'max_adverse_excursion': -0.013237, 'max_favorable_excursion': 0.022638}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006179, 'median_return': 0.011619, 'mean_absolute_return': 0.015235, 'max_adverse_excursion': -0.022813, 'max_favorable_excursion': 0.030335}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.022474, 'median_return': 0.045453, 'mean_absolute_return': 0.028373, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.056558}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.068211, 'median_return': 0.084216, 'mean_absolute_return': 0.068211, 'max_adverse_excursion': 0.002294, 'max_favorable_excursion': 0.142584}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.006267, 'median_return': -0.004137, 'mean_absolute_return': 0.016808, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.006977, 'median_return': -0.005796, 'mean_absolute_return': 0.018425, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.006595, 'median_return': -0.004767, 'mean_absolute_return': 0.030839, 'max_adverse_excursion': -0.078601, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.006806, 'median_return': 0.016027, 'mean_absolute_return': 0.043156, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.05168, 'median_return': 0.057507, 'mean_absolute_return': 0.077343, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.4}, '60d': {'sample_size': 80, 'hit_rate': 0.15}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_minus_secondary': -0.7, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.003533, 'median_return': -0.002952, 'mean_absolute_return': 0.014704, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.003202, 'median_return': 0.000591, 'mean_absolute_return': 0.016272, 'max_adverse_excursion': -0.053563, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': -0.000712, 'median_return': 0.005535, 'mean_absolute_return': 0.02952, 'max_adverse_excursion': -0.078601, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.013841, 'median_return': 0.021801, 'mean_absolute_return': 0.041626, 'max_adverse_excursion': -0.083836, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.058375, 'median_return': 0.060702, 'mean_absolute_return': 0.074399, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.154804}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.007323, 'median_return': -0.004137, 'mean_absolute_return': 0.021439, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.012122, 'median_return': -0.007994, 'mean_absolute_return': 0.022227, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.019137, 'median_return': -0.017071, 'mean_absolute_return': 0.028557, 'max_adverse_excursion': -0.065338, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00803, 'median_return': -0.001589, 'mean_absolute_return': 0.041833, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.038208, 'median_return': 0.056537, 'mean_absolute_return': 0.082522, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.00448`, median `-0.003244`, mae `0.016388`
- 5d: sample `80`, hit `0.4625`, avg `-0.005432`, median `-0.002452`, mae `0.017761`
- 10d: sample `80`, hit `0.5`, avg `-0.005318`, median `0.000397`, mae `0.029279`
- 20d: sample `80`, hit `0.6`, avg `0.008373`, median `0.016027`, mae `0.041677`
- 60d: sample `80`, hit `0.85`, avg `0.053333`, median `0.059104`, mae `0.076429`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.00448`, median `-0.003244`, mae `0.016388`
- 5d: sample `80`, hit `0.4625`, avg `-0.005432`, median `-0.002452`, mae `0.017761`
- 10d: sample `80`, hit `0.5`, avg `-0.005318`, median `0.000397`, mae `0.029279`
- 20d: sample `80`, hit `0.6`, avg `0.008373`, median `0.016027`, mae `0.041677`
- 60d: sample `80`, hit `0.85`, avg `0.053333`, median `0.059104`, mae `0.076429`

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
- 3d: sample `80`, hit `0.4375`, avg `-0.00448`, median `-0.003244`, mae `0.016388`
- 5d: sample `80`, hit `0.4625`, avg `-0.005432`, median `-0.002452`, mae `0.017761`
- 10d: sample `80`, hit `0.5`, avg `-0.005318`, median `0.000397`, mae `0.029279`
- 20d: sample `80`, hit `0.6`, avg `0.008373`, median `0.016027`, mae `0.041677`
- 60d: sample `80`, hit `0.85`, avg `0.053333`, median `0.059104`, mae `0.076429`

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
- 3d: sample `80`, hit `0.4375`, avg `-0.00448`, median `-0.003244`, mae `0.016388`
- 5d: sample `80`, hit `0.4625`, avg `-0.005432`, median `-0.002452`, mae `0.017761`
- 10d: sample `80`, hit `0.5`, avg `-0.005318`, median `0.000397`, mae `0.029279`
- 20d: sample `80`, hit `0.6`, avg `0.008373`, median `0.016027`, mae `0.041677`
- 60d: sample `80`, hit `0.85`, avg `0.053333`, median `0.059104`, mae `0.076429`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
