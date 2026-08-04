# High Confidence Edge Report

Generated at: `2026-08-04T00:16:40.042472+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.000415`, median `0.001199`, mae `0.01558`
- 5d: sample `80`, hit `0.6`, avg `-1.5e-05`, median `0.003005`, mae `0.017514`
- 10d: sample `80`, hit `0.4375`, avg `0.001177`, median `-0.006017`, mae `0.025921`
- 20d: sample `80`, hit `0.55`, avg `0.003883`, median `0.007762`, mae `0.042719`
- 60d: sample `80`, hit `0.5375`, avg `0.00449`, median `0.009227`, mae `0.075032`

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
- 3d: sample `8`, hit `0.25`, avg `-0.019958`, median `-0.022062`, mae `0.022583`
- 5d: sample `8`, hit `0.25`, avg `-0.023775`, median `-0.016062`, mae `0.02463`
- 10d: sample `8`, hit `0.125`, avg `-0.017739`, median `-0.01796`, mae `0.022547`
- 20d: sample `8`, hit `0.5`, avg `-0.016002`, median `0.020068`, mae `0.047675`
- 60d: sample `8`, hit `0.5`, avg `-0.011664`, median `0.012092`, mae `0.076501`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.019958`, median `-0.022062`, mae `0.022583`
- 5d: sample `8`, hit `0.25`, avg `-0.023775`, median `-0.016062`, mae `0.02463`
- 10d: sample `8`, hit `0.125`, avg `-0.017739`, median `-0.01796`, mae `0.022547`
- 20d: sample `8`, hit `0.5`, avg `-0.016002`, median `0.020068`, mae `0.047675`
- 60d: sample `8`, hit `0.5`, avg `-0.011664`, median `0.012092`, mae `0.076501`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.019958, 'median_return': -0.022062, 'mean_absolute_return': 0.022583, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.023775, 'median_return': -0.016062, 'mean_absolute_return': 0.02463, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.003005}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.017739, 'median_return': -0.01796, 'mean_absolute_return': 0.022547, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.016002, 'median_return': 0.020068, 'mean_absolute_return': 0.047675, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.011664, 'median_return': 0.012092, 'mean_absolute_return': 0.076501, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002679, 'median_return': 0.00234, 'mean_absolute_return': 0.014802, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.057206}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.002625, 'median_return': 0.004613, 'mean_absolute_return': 0.016723, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.063326}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.003278, 'median_return': -0.001676, 'mean_absolute_return': 0.026295, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.094092}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.006093, 'median_return': 0.007762, 'mean_absolute_return': 0.042169, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.006285, 'median_return': 0.009227, 'mean_absolute_return': 0.074869, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.3875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.000415, 'median_return': 0.001199, 'mean_absolute_return': 0.01558, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.057206}, '5d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': -1.5e-05, 'median_return': 0.003005, 'mean_absolute_return': 0.017514, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.063326}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': 0.001177, 'median_return': -0.006017, 'mean_absolute_return': 0.025921, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.094092}, '20d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.003883, 'median_return': 0.007762, 'mean_absolute_return': 0.042719, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.00449, 'median_return': 0.009227, 'mean_absolute_return': 0.075032, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.003619`, median `0.000603`, mae `0.014931`
- 5d: sample `40`, hit `0.575`, avg `-0.00587`, median `0.001303`, mae `0.014597`
- 10d: sample `40`, hit `0.225`, avg `-0.009891`, median `-0.011432`, mae `0.016768`
- 20d: sample `40`, hit `0.375`, avg `-0.009114`, median `-0.00751`, mae `0.028855`
- 60d: sample `40`, hit `0.425`, avg `-0.006731`, median `-0.012792`, mae `0.050674`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006116`, median `0.010664`, mae `0.019224`
- 5d: sample `20`, hit `0.55`, avg `0.005832`, median `0.009517`, mae `0.023199`
- 10d: sample `20`, hit `0.7`, avg `0.022924`, median `0.033374`, mae `0.037127`
- 20d: sample `20`, hit `0.85`, avg `0.046183`, median `0.049691`, mae `0.057828`
- 60d: sample `20`, hit `0.8`, avg `0.059007`, median `0.073651`, mae `0.103632`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000791`, median `0.000603`, mae `0.012019`
- 5d: sample `20`, hit `0.75`, avg `0.001215`, median `0.004473`, mae `0.010969`
- 10d: sample `20`, hit `0.25`, avg `-0.008216`, median `-0.01051`, mae `0.016296`
- 20d: sample `20`, hit `0.3`, avg `-0.012247`, median `-0.009023`, mae `0.023876`
- 60d: sample `20`, hit `0.35`, avg `-0.010392`, median `-0.012792`, mae `0.039381`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006116`, median `0.010664`, mae `0.019224`
- 5d: sample `20`, hit `0.55`, avg `0.005832`, median `0.009517`, mae `0.023199`
- 10d: sample `20`, hit `0.7`, avg `0.022924`, median `0.033374`, mae `0.037127`
- 20d: sample `20`, hit `0.85`, avg `0.046183`, median `0.049691`, mae `0.057828`
- 60d: sample `20`, hit `0.8`, avg `0.059007`, median `0.073651`, mae `0.103632`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000791`, median `0.000603`, mae `0.012019`
- 5d: sample `20`, hit `0.75`, avg `0.001215`, median `0.004473`, mae `0.010969`
- 10d: sample `20`, hit `0.25`, avg `-0.008216`, median `-0.01051`, mae `0.016296`
- 20d: sample `20`, hit `0.3`, avg `-0.012247`, median `-0.009023`, mae `0.023876`
- 60d: sample `20`, hit `0.35`, avg `-0.010392`, median `-0.012792`, mae `0.039381`

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
- 3d: sample `20`, hit `0.65`, avg `0.006116`, median `0.010664`, mae `0.019224`
- 5d: sample `20`, hit `0.55`, avg `0.005832`, median `0.009517`, mae `0.023199`
- 10d: sample `20`, hit `0.7`, avg `0.022924`, median `0.033374`, mae `0.037127`
- 20d: sample `20`, hit `0.85`, avg `0.046183`, median `0.049691`, mae `0.057828`
- 60d: sample `20`, hit `0.8`, avg `0.059007`, median `0.073651`, mae `0.103632`

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
- 3d: sample `80`, hit `0.55`, avg `0.000415`, median `0.001199`, mae `0.01558`
- 5d: sample `80`, hit `0.6`, avg `-1.5e-05`, median `0.003005`, mae `0.017514`
- 10d: sample `80`, hit `0.4375`, avg `0.001177`, median `-0.006017`, mae `0.025921`
- 20d: sample `80`, hit `0.55`, avg `0.003883`, median `0.007762`, mae `0.042719`
- 60d: sample `80`, hit `0.5375`, avg `0.00449`, median `0.009227`, mae `0.075032`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000791`, median `0.000603`, mae `0.012019`
- 5d: sample `20`, hit `0.75`, avg `0.001215`, median `0.004473`, mae `0.010969`
- 10d: sample `20`, hit `0.25`, avg `-0.008216`, median `-0.01051`, mae `0.016296`
- 20d: sample `20`, hit `0.3`, avg `-0.012247`, median `-0.009023`, mae `0.023876`
- 60d: sample `20`, hit `0.35`, avg `-0.010392`, median `-0.012792`, mae `0.039381`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.000415`, median `0.001199`, mae `0.01558`
- 5d: sample `80`, hit `0.6`, avg `-1.5e-05`, median `0.003005`, mae `0.017514`
- 10d: sample `80`, hit `0.4375`, avg `0.001177`, median `-0.006017`, mae `0.025921`
- 20d: sample `80`, hit `0.55`, avg `0.003883`, median `0.007762`, mae `0.042719`
- 60d: sample `80`, hit `0.5375`, avg `0.00449`, median `0.009227`, mae `0.075032`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000791`, median `0.000603`, mae `0.012019`
- 5d: sample `20`, hit `0.75`, avg `0.001215`, median `0.004473`, mae `0.010969`
- 10d: sample `20`, hit `0.25`, avg `-0.008216`, median `-0.01051`, mae `0.016296`
- 20d: sample `20`, hit `0.3`, avg `-0.012247`, median `-0.009023`, mae `0.023876`
- 60d: sample `20`, hit `0.35`, avg `-0.010392`, median `-0.012792`, mae `0.039381`

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
