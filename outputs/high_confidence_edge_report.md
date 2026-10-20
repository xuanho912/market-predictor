# High Confidence Edge Report

Generated at: `2026-10-20T06:06:05.679339+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001781`, median `0.001405`, mae `0.01211`
- 5d: sample `20`, hit `0.55`, avg `-0.00337`, median `0.000688`, mae `0.013058`
- 10d: sample `20`, hit `0.45`, avg `-0.002427`, median `-0.006933`, mae `0.015948`
- 20d: sample `20`, hit `0.55`, avg `0.011007`, median `0.015416`, mae `0.025075`
- 60d: sample `20`, hit `0.6`, avg `0.016362`, median `0.029164`, mae `0.047984`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `60`
- 3d: sample `60`, hit `0.3333`, avg `-0.00811`, median `-0.010094`, mae `0.019362`
- 5d: sample `60`, hit `0.4333`, avg `-0.00605`, median `-0.005632`, mae `0.021244`
- 10d: sample `60`, hit `0.4667`, avg `-0.001357`, median `-0.0004`, mae `0.029062`
- 20d: sample `60`, hit `0.6333`, avg `0.021872`, median `0.017149`, mae `0.037976`
- 60d: sample `60`, hit `0.75`, avg `0.061207`, median `0.076106`, mae `0.094912`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.008796`, median `-0.010033`, mae `0.017039`
- 5d: sample `8`, hit `0.375`, avg `-0.012434`, median `-0.022295`, mae `0.023462`
- 10d: sample `8`, hit `0.25`, avg `-0.00345`, median `-0.005891`, mae `0.014352`
- 20d: sample `8`, hit `0.75`, avg `0.037655`, median `0.058396`, mae `0.046085`
- 60d: sample `8`, hit `0.75`, avg `0.072565`, median `0.121826`, mae `0.094285`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.008796`, median `-0.010033`, mae `0.017039`
- 5d: sample `8`, hit `0.375`, avg `-0.012434`, median `-0.022295`, mae `0.023462`
- 10d: sample `8`, hit `0.25`, avg `-0.00345`, median `-0.005891`, mae `0.014352`
- 20d: sample `8`, hit `0.75`, avg `0.037655`, median `0.058396`, mae `0.046085`
- 60d: sample `8`, hit `0.75`, avg `0.072565`, median `0.121826`, mae `0.094285`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008796, 'median_return': -0.010033, 'mean_absolute_return': 0.017039, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012434, 'median_return': -0.022295, 'mean_absolute_return': 0.023462, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00345, 'median_return': -0.005891, 'mean_absolute_return': 0.014352, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.037655, 'median_return': 0.058396, 'mean_absolute_return': 0.046085, 'max_adverse_excursion': -0.02149, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.072565, 'median_return': 0.121826, 'mean_absolute_return': 0.094285, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.006276, 'median_return': -0.00589, 'mean_absolute_return': 0.017606, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.004596, 'median_return': -0.001429, 'mean_absolute_return': 0.018724, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.059418}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.001422, 'median_return': -0.000231, 'mean_absolute_return': 0.027054, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.0171, 'median_return': 0.013402, 'mean_absolute_return': 0.033491, 'max_adverse_excursion': -0.062788, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.047488, 'median_return': 0.059007, 'mean_absolute_return': 0.081946, 'max_adverse_excursion': -0.145377, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.2875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.425, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.3875, 'avg_return': -0.006528, 'median_return': -0.007083, 'mean_absolute_return': 0.017549, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.04966}, '5d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.00538, 'median_return': -0.002452, 'mean_absolute_return': 0.019198, 'max_adverse_excursion': -0.047223, 'max_favorable_excursion': 0.059418}, '10d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.001625, 'median_return': -0.004074, 'mean_absolute_return': 0.025783, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.019156, 'median_return': 0.015713, 'mean_absolute_return': 0.034751, 'max_adverse_excursion': -0.062788, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.049996, 'median_return': 0.059104, 'mean_absolute_return': 0.08318, 'max_adverse_excursion': -0.145377, 'max_favorable_excursion': 0.21267}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.004765`, median `-0.000285`, mae `0.014807`
- 5d: sample `40`, hit `0.525`, avg `-0.00622`, median `0.000688`, mae `0.015799`
- 10d: sample `40`, hit `0.375`, avg `-0.004422`, median `-0.006933`, mae `0.018428`
- 20d: sample `40`, hit `0.6`, avg `0.014476`, median `0.017149`, mae `0.028943`
- 60d: sample `40`, hit `0.625`, avg `0.025578`, median `0.037425`, mae `0.061335`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.00829`, median `-0.014765`, mae `0.020292`
- 5d: sample `40`, hit `0.4`, avg `-0.004539`, median `-0.009371`, mae `0.022596`
- 10d: sample `40`, hit `0.55`, avg `0.001172`, median `0.003921`, mae `0.033139`
- 20d: sample `40`, hit `0.625`, avg `0.023835`, median `0.015713`, mae `0.040558`
- 60d: sample `40`, hit `0.8`, avg `0.074414`, median `0.079633`, mae `0.105025`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.00829`, median `-0.014765`, mae `0.020292`
- 5d: sample `40`, hit `0.4`, avg `-0.004539`, median `-0.009371`, mae `0.022596`
- 10d: sample `40`, hit `0.55`, avg `0.001172`, median `0.003921`, mae `0.033139`
- 20d: sample `40`, hit `0.625`, avg `0.023835`, median `0.015713`, mae `0.040558`
- 60d: sample `40`, hit `0.8`, avg `0.074414`, median `0.079633`, mae `0.105025`

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
- 3d: sample `80`, hit `0.3875`, avg `-0.006528`, median `-0.007083`, mae `0.017549`
- 5d: sample `80`, hit `0.4625`, avg `-0.00538`, median `-0.002452`, mae `0.019198`
- 10d: sample `80`, hit `0.4625`, avg `-0.001625`, median `-0.004074`, mae `0.025783`
- 20d: sample `80`, hit `0.6125`, avg `0.019156`, median `0.015713`, mae `0.034751`
- 60d: sample `80`, hit `0.7125`, avg `0.049996`, median `0.059104`, mae `0.08318`

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
- 3d: sample `80`, hit `0.3875`, avg `-0.006528`, median `-0.007083`, mae `0.017549`
- 5d: sample `80`, hit `0.4625`, avg `-0.00538`, median `-0.002452`, mae `0.019198`
- 10d: sample `80`, hit `0.4625`, avg `-0.001625`, median `-0.004074`, mae `0.025783`
- 20d: sample `80`, hit `0.6125`, avg `0.019156`, median `0.015713`, mae `0.034751`
- 60d: sample `80`, hit `0.7125`, avg `0.049996`, median `0.059104`, mae `0.08318`

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
- 3d: sample `80`, hit `0.3875`, avg `-0.006528`, median `-0.007083`, mae `0.017549`
- 5d: sample `80`, hit `0.4625`, avg `-0.00538`, median `-0.002452`, mae `0.019198`
- 10d: sample `80`, hit `0.4625`, avg `-0.001625`, median `-0.004074`, mae `0.025783`
- 20d: sample `80`, hit `0.6125`, avg `0.019156`, median `0.015713`, mae `0.034751`
- 60d: sample `80`, hit `0.7125`, avg `0.049996`, median `0.059104`, mae `0.08318`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
