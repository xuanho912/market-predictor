# High Confidence Edge Report

Generated at: `2026-09-22T01:36:24.531194+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `36`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `36`, gate `early_evidence`
- 5d: completed `36`, gate `early_evidence`
- 10d: completed `36`, gate `early_evidence`
- 20d: completed `36`, gate `early_evidence`
- 60d: completed `36`, gate `early_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.004027`, median `-0.001658`, mae `0.015795`
- 5d: sample `60`, hit `0.4667`, avg `-0.007545`, median `-0.004438`, mae `0.017441`
- 10d: sample `60`, hit `0.4`, avg `-0.003424`, median `-0.007011`, mae `0.017677`
- 20d: sample `60`, hit `0.6167`, avg `0.013183`, median `0.015416`, mae `0.031954`
- 60d: sample `60`, hit `0.7333`, avg `0.031351`, median `0.04207`, mae `0.061553`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.010554`, median `-0.008838`, mae `0.012681`
- 5d: sample `20`, hit `0.15`, avg `-0.018657`, median `-0.020895`, mae `0.022028`
- 10d: sample `20`, hit `0.15`, avg `-0.030954`, median `-0.032571`, mae `0.036168`
- 20d: sample `20`, hit `0.35`, avg `-0.004843`, median `-0.011553`, mae `0.052864`
- 60d: sample `20`, hit `0.7`, avg `0.022645`, median `0.059007`, mae `0.089828`

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
- 3d: sample `8`, hit `0.0`, avg `-0.018856`, median `-0.010094`, mae `0.018856`
- 5d: sample `8`, hit `0.25`, avg `-0.01519`, median `-0.022295`, mae `0.017721`
- 10d: sample `8`, hit `0.0`, avg `-0.015127`, median `-0.015123`, mae `0.015127`
- 20d: sample `8`, hit `0.625`, avg `0.017035`, median `0.029166`, mae `0.040233`
- 60d: sample `8`, hit `0.625`, avg `0.034259`, median `0.072696`, mae `0.086871`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.0`, avg `-0.018856`, median `-0.010094`, mae `0.018856`
- 5d: sample `8`, hit `0.25`, avg `-0.01519`, median `-0.022295`, mae `0.017721`
- 10d: sample `8`, hit `0.0`, avg `-0.015127`, median `-0.015123`, mae `0.015127`
- 20d: sample `8`, hit `0.625`, avg `0.017035`, median `0.029166`, mae `0.040233`
- 60d: sample `8`, hit `0.625`, avg `0.034259`, median `0.072696`, mae `0.086871`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.004027, 'median_return': -0.001658, 'mean_absolute_return': 0.015795, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.007545, 'median_return': -0.004438, 'mean_absolute_return': 0.017441, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.003424, 'median_return': -0.007011, 'mean_absolute_return': 0.017677, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.067569}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.013183, 'median_return': 0.015416, 'mean_absolute_return': 0.031954, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.031351, 'median_return': 0.04207, 'mean_absolute_return': 0.061553, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.162638}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.018856, 'median_return': -0.010094, 'mean_absolute_return': 0.018856, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': -0.001658}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01519, 'median_return': -0.022295, 'mean_absolute_return': 0.017721, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.015127, 'median_return': -0.015123, 'mean_absolute_return': 0.015127, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.017035, 'median_return': 0.029166, 'mean_absolute_return': 0.040233, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.034259, 'median_return': 0.072696, 'mean_absolute_return': 0.086871, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.004192, 'median_return': -0.003649, 'mean_absolute_return': 0.01459, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.009782, 'median_return': -0.00863, 'mean_absolute_return': 0.018684, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.009771, 'median_return': -0.009882, 'mean_absolute_return': 0.023097, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.067569}, '20d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.007748, 'median_return': 0.010824, 'mean_absolute_return': 0.036843, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.02861, 'median_return': 0.04207, 'mean_absolute_return': 0.066594, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.162638}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 20, 'both_miss': 20}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.1, 'both_hit': 21, 'both_miss': 19}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.05, 'both_hit': 19, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.125, 'both_hit': 25, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.025, 'both_hit': 31, 'both_miss': 9}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.3875, 'avg_return': -0.005659, 'median_return': -0.00402, 'mean_absolute_return': 0.015016, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 80, 'hit_rate': 0.3875, 'avg_return': -0.010323, 'median_return': -0.009444, 'mean_absolute_return': 0.018588, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.3375, 'avg_return': -0.010307, 'median_return': -0.01051, 'mean_absolute_return': 0.0223, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.067569}, '20d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.008677, 'median_return': 0.011528, 'mean_absolute_return': 0.037182, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.029175, 'median_return': 0.046132, 'mean_absolute_return': 0.068622, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.162638}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.005425`, median `-0.001641`, mae `0.014604`
- 5d: sample `20`, hit `0.45`, avg `-0.007573`, median `-0.006464`, mae `0.015205`
- 10d: sample `20`, hit `0.4`, avg `-0.005327`, median `-0.007491`, mae `0.016208`
- 20d: sample `20`, hit `0.6`, avg `0.015794`, median `0.01927`, mae `0.025113`
- 60d: sample `20`, hit `0.75`, avg `0.037812`, median `0.059948`, mae `0.055196`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.3875`, avg `-0.005659`, median `-0.00402`, mae `0.015016`
- 5d: sample `80`, hit `0.3875`, avg `-0.010323`, median `-0.009444`, mae `0.018588`
- 10d: sample `80`, hit `0.3375`, avg `-0.010307`, median `-0.01051`, mae `0.0223`
- 20d: sample `80`, hit `0.55`, avg `0.008677`, median `0.011528`, mae `0.037182`
- 60d: sample `80`, hit `0.725`, avg `0.029175`, median `0.046132`, mae `0.068622`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.005425`, median `-0.001641`, mae `0.014604`
- 5d: sample `20`, hit `0.45`, avg `-0.007573`, median `-0.006464`, mae `0.015205`
- 10d: sample `20`, hit `0.4`, avg `-0.005327`, median `-0.007491`, mae `0.016208`
- 20d: sample `20`, hit `0.6`, avg `0.015794`, median `0.01927`, mae `0.025113`
- 60d: sample `20`, hit `0.75`, avg `0.037812`, median `0.059948`, mae `0.055196`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.004027`, median `-0.001658`, mae `0.015795`
- 5d: sample `60`, hit `0.4667`, avg `-0.007545`, median `-0.004438`, mae `0.017441`
- 10d: sample `60`, hit `0.4`, avg `-0.003424`, median `-0.007011`, mae `0.017677`
- 20d: sample `60`, hit `0.6167`, avg `0.013183`, median `0.015416`, mae `0.031954`
- 60d: sample `60`, hit `0.7333`, avg `0.031351`, median `0.04207`, mae `0.061553`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011622`, median `-0.010033`, mae `0.018361`
- 5d: sample `20`, hit `0.35`, avg `-0.015428`, median `-0.016062`, mae `0.021071`
- 10d: sample `20`, hit `0.25`, avg `-0.010245`, median `-0.010456`, mae `0.017449`
- 20d: sample `20`, hit `0.6`, avg `0.007168`, median `0.020068`, mae `0.037839`
- 60d: sample `20`, hit `0.65`, avg `0.025099`, median `0.046132`, mae `0.078837`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.005425`, median `-0.001641`, mae `0.014604`
- 5d: sample `20`, hit `0.45`, avg `-0.007573`, median `-0.006464`, mae `0.015205`
- 10d: sample `20`, hit `0.4`, avg `-0.005327`, median `-0.007491`, mae `0.016208`
- 20d: sample `20`, hit `0.6`, avg `0.015794`, median `0.01927`, mae `0.025113`
- 60d: sample `20`, hit `0.75`, avg `0.037812`, median `0.059948`, mae `0.055196`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003328`, median `-0.001658`, mae `0.01639`
- 5d: sample `40`, hit `0.475`, avg `-0.007531`, median `-0.001562`, mae `0.018559`
- 10d: sample `40`, hit `0.4`, avg `-0.002473`, median `-0.006017`, mae `0.018412`
- 20d: sample `40`, hit `0.625`, avg `0.011878`, median `0.013156`, mae `0.035374`
- 60d: sample `40`, hit `0.725`, avg `0.028121`, median `0.031273`, mae `0.064731`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.010554`, median `-0.008838`, mae `0.012681`
- 5d: sample `20`, hit `0.15`, avg `-0.018657`, median `-0.020895`, mae `0.022028`
- 10d: sample `20`, hit `0.15`, avg `-0.030954`, median `-0.032571`, mae `0.036168`
- 20d: sample `20`, hit `0.35`, avg `-0.004843`, median `-0.011553`, mae `0.052864`
- 60d: sample `20`, hit `0.7`, avg `0.022645`, median `0.059007`, mae `0.089828`

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
- 3d: sample `80`, hit `0.3875`, avg `-0.005659`, median `-0.00402`, mae `0.015016`
- 5d: sample `80`, hit `0.3875`, avg `-0.010323`, median `-0.009444`, mae `0.018588`
- 10d: sample `80`, hit `0.3375`, avg `-0.010307`, median `-0.01051`, mae `0.0223`
- 20d: sample `80`, hit `0.55`, avg `0.008677`, median `0.011528`, mae `0.037182`
- 60d: sample `80`, hit `0.725`, avg `0.029175`, median `0.046132`, mae `0.068622`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.004027`, median `-0.001658`, mae `0.015795`
- 5d: sample `60`, hit `0.4667`, avg `-0.007545`, median `-0.004438`, mae `0.017441`
- 10d: sample `60`, hit `0.4`, avg `-0.003424`, median `-0.007011`, mae `0.017677`
- 20d: sample `60`, hit `0.6167`, avg `0.013183`, median `0.015416`, mae `0.031954`
- 60d: sample `60`, hit `0.7333`, avg `0.031351`, median `0.04207`, mae `0.061553`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003328`, median `-0.001658`, mae `0.01639`
- 5d: sample `40`, hit `0.475`, avg `-0.007531`, median `-0.001562`, mae `0.018559`
- 10d: sample `40`, hit `0.4`, avg `-0.002473`, median `-0.006017`, mae `0.018412`
- 20d: sample `40`, hit `0.625`, avg `0.011878`, median `0.013156`, mae `0.035374`
- 60d: sample `40`, hit `0.725`, avg `0.028121`, median `0.031273`, mae `0.064731`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003328`, median `-0.001658`, mae `0.01639`
- 5d: sample `40`, hit `0.475`, avg `-0.007531`, median `-0.001562`, mae `0.018559`
- 10d: sample `40`, hit `0.4`, avg `-0.002473`, median `-0.006017`, mae `0.018412`
- 20d: sample `40`, hit `0.625`, avg `0.011878`, median `0.013156`, mae `0.035374`
- 60d: sample `40`, hit `0.725`, avg `0.028121`, median `0.031273`, mae `0.064731`

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
