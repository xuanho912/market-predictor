# High Confidence Edge Report

Generated at: `2026-08-31T19:11:00.328491+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

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
- 3d: sample `80`, hit `0.55`, avg `-7.7e-05`, median `0.002067`, mae `0.015831`
- 5d: sample `80`, hit `0.525`, avg `-0.000224`, median `0.000548`, mae `0.018921`
- 10d: sample `80`, hit `0.4375`, avg `0.001752`, median `-0.00367`, mae `0.025496`
- 20d: sample `80`, hit `0.7`, avg `0.012278`, median `0.02086`, mae `0.037917`
- 60d: sample `80`, hit `0.725`, avg `0.036168`, median `0.049712`, mae `0.070696`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003731`, median `0.001558`, mae `0.010009`
- 5d: sample `8`, hit `0.375`, avg `-0.008244`, median `-0.012956`, mae `0.014414`
- 10d: sample `8`, hit `0.75`, avg `0.012486`, median `0.020918`, mae `0.022047`
- 20d: sample `8`, hit `1.0`, avg `0.029933`, median `0.031658`, mae `0.029933`
- 60d: sample `8`, hit `1.0`, avg `0.081351`, median `0.095045`, mae `0.081351`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.003731`, median `0.001558`, mae `0.010009`
- 5d: sample `8`, hit `0.375`, avg `-0.008244`, median `-0.012956`, mae `0.014414`
- 10d: sample `8`, hit `0.75`, avg `0.012486`, median `0.020918`, mae `0.022047`
- 20d: sample `8`, hit `1.0`, avg `0.029933`, median `0.031658`, mae `0.029933`
- 60d: sample `8`, hit `1.0`, avg `0.081351`, median `0.095045`, mae `0.081351`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': -7.7e-05, 'median_return': 0.002067, 'mean_absolute_return': 0.015831, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.000224, 'median_return': 0.000548, 'mean_absolute_return': 0.018921, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': 0.001752, 'median_return': -0.00367, 'mean_absolute_return': 0.025496, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.012278, 'median_return': 0.02086, 'mean_absolute_return': 0.037917, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.036168, 'median_return': 0.049712, 'mean_absolute_return': 0.070696, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003731, 'median_return': 0.001558, 'mean_absolute_return': 0.010009, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008244, 'median_return': -0.012956, 'mean_absolute_return': 0.014414, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.012486, 'median_return': 0.020918, 'mean_absolute_return': 0.022047, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.029933, 'median_return': 0.031658, 'mean_absolute_return': 0.029933, 'max_adverse_excursion': 0.000213, 'max_favorable_excursion': 0.055822}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.081351, 'median_return': 0.095045, 'mean_absolute_return': 0.081351, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.120808}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.000329, 'median_return': 0.002329, 'mean_absolute_return': 0.016477, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000667, 'median_return': 0.000688, 'mean_absolute_return': 0.019422, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': 0.000559, 'median_return': -0.00676, 'mean_absolute_return': 0.025879, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.010316, 'median_return': 0.018139, 'mean_absolute_return': 0.038805, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.031148, 'median_return': 0.036184, 'mean_absolute_return': 0.069512, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.7}, '60d': {'sample_size': 80, 'hit_rate': 0.725}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.075, 'both_hit': 21, 'both_miss': 19}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.075, 'both_hit': 19, 'both_miss': 21}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.075, 'both_hit': 18, 'both_miss': 22}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.125, 'both_hit': 31, 'both_miss': 9}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.1, 'both_hit': 34, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': -7.7e-05, 'median_return': 0.002067, 'mean_absolute_return': 0.015831, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.000224, 'median_return': 0.000548, 'mean_absolute_return': 0.018921, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': 0.001752, 'median_return': -0.00367, 'mean_absolute_return': 0.025496, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.012278, 'median_return': 0.02086, 'mean_absolute_return': 0.037917, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.036168, 'median_return': 0.049712, 'mean_absolute_return': 0.070696, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000893`, median `0.000603`, mae `0.007721`
- 5d: sample `20`, hit `0.45`, avg `-0.005075`, median `-0.00244`, mae `0.010068`
- 10d: sample `20`, hit `0.3`, avg `-0.007915`, median `-0.013241`, mae `0.020116`
- 20d: sample `20`, hit `0.55`, avg `-0.00979`, median `0.007004`, mae `0.035372`
- 60d: sample `20`, hit `0.6`, avg `0.014482`, median `0.032982`, mae `0.062762`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000453`, median `0.002329`, mae `0.018719`
- 5d: sample `40`, hit `0.475`, avg `-0.000883`, median `-0.004438`, mae `0.022812`
- 10d: sample `40`, hit `0.45`, avg `0.006302`, median `-0.001222`, mae `0.028022`
- 20d: sample `40`, hit `0.775`, avg `0.02199`, median `0.030297`, mae `0.039199`
- 60d: sample `40`, hit `0.85`, avg `0.065605`, median `0.069439`, mae `0.08038`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000893`, median `0.000603`, mae `0.007721`
- 5d: sample `20`, hit `0.45`, avg `-0.005075`, median `-0.00244`, mae `0.010068`
- 10d: sample `20`, hit `0.3`, avg `-0.007915`, median `-0.013241`, mae `0.020116`
- 20d: sample `20`, hit `0.55`, avg `-0.00979`, median `0.007004`, mae `0.035372`
- 60d: sample `20`, hit `0.6`, avg `0.014482`, median `0.032982`, mae `0.062762`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000453`, median `0.002329`, mae `0.018719`
- 5d: sample `40`, hit `0.475`, avg `-0.000883`, median `-0.004438`, mae `0.022812`
- 10d: sample `40`, hit `0.45`, avg `0.006302`, median `-0.001222`, mae `0.028022`
- 20d: sample `40`, hit `0.775`, avg `0.02199`, median `0.030297`, mae `0.039199`
- 60d: sample `40`, hit `0.85`, avg `0.065605`, median `0.069439`, mae `0.08038`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002852`, median `-0.001658`, mae `0.015174`
- 5d: sample `20`, hit `0.45`, avg `-0.005709`, median `-0.004438`, mae `0.017498`
- 10d: sample `20`, hit `0.4`, avg `0.002758`, median `-0.001222`, mae `0.019557`
- 20d: sample `20`, hit `0.85`, avg `0.024854`, median `0.031658`, mae `0.03844`
- 60d: sample `20`, hit `0.8`, avg `0.059262`, median `0.085257`, mae `0.082428`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000893`, median `0.000603`, mae `0.007721`
- 5d: sample `20`, hit `0.45`, avg `-0.005075`, median `-0.00244`, mae `0.010068`
- 10d: sample `20`, hit `0.3`, avg `-0.007915`, median `-0.013241`, mae `0.020116`
- 20d: sample `20`, hit `0.55`, avg `-0.00979`, median `0.007004`, mae `0.035372`
- 60d: sample `20`, hit `0.6`, avg `0.014482`, median `0.032982`, mae `0.062762`

### bounce_without_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.000195`, median `0.003026`, mae `0.018534`
- 5d: sample `60`, hit `0.55`, avg `0.001393`, median `0.001239`, mae `0.021873`
- 10d: sample `60`, hit `0.4833`, avg `0.004974`, median `-0.0004`, mae `0.027289`
- 20d: sample `60`, hit `0.75`, avg `0.019633`, median `0.030297`, mae `0.038766`
- 60d: sample `60`, hit `0.7667`, avg `0.043397`, median `0.053843`, mae `0.073341`

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

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

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
- 3d: sample `80`, hit `0.55`, avg `-7.7e-05`, median `0.002067`, mae `0.015831`
- 5d: sample `80`, hit `0.525`, avg `-0.000224`, median `0.000548`, mae `0.018921`
- 10d: sample `80`, hit `0.4375`, avg `0.001752`, median `-0.00367`, mae `0.025496`
- 20d: sample `80`, hit `0.7`, avg `0.012278`, median `0.02086`, mae `0.037917`
- 60d: sample `80`, hit `0.725`, avg `0.036168`, median `0.049712`, mae `0.070696`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `-7.7e-05`, median `0.002067`, mae `0.015831`
- 5d: sample `80`, hit `0.525`, avg `-0.000224`, median `0.000548`, mae `0.018921`
- 10d: sample `80`, hit `0.4375`, avg `0.001752`, median `-0.00367`, mae `0.025496`
- 20d: sample `80`, hit `0.7`, avg `0.012278`, median `0.02086`, mae `0.037917`
- 60d: sample `80`, hit `0.725`, avg `0.036168`, median `0.049712`, mae `0.070696`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `-7.7e-05`, median `0.002067`, mae `0.015831`
- 5d: sample `80`, hit `0.525`, avg `-0.000224`, median `0.000548`, mae `0.018921`
- 10d: sample `80`, hit `0.4375`, avg `0.001752`, median `-0.00367`, mae `0.025496`
- 20d: sample `80`, hit `0.7`, avg `0.012278`, median `0.02086`, mae `0.037917`
- 60d: sample `80`, hit `0.725`, avg `0.036168`, median `0.049712`, mae `0.070696`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `-7.7e-05`, median `0.002067`, mae `0.015831`
- 5d: sample `80`, hit `0.525`, avg `-0.000224`, median `0.000548`, mae `0.018921`
- 10d: sample `80`, hit `0.4375`, avg `0.001752`, median `-0.00367`, mae `0.025496`
- 20d: sample `80`, hit `0.7`, avg `0.012278`, median `0.02086`, mae `0.037917`
- 60d: sample `80`, hit `0.725`, avg `0.036168`, median `0.049712`, mae `0.070696`

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
