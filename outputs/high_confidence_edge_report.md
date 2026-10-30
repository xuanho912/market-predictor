# High Confidence Edge Report

Generated at: `2026-10-30T10:29:44.465053+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `148`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `148`, gate `stronger_evidence`
- 5d: completed `148`, gate `stronger_evidence`
- 10d: completed `148`, gate `stronger_evidence`
- 20d: completed `148`, gate `stronger_evidence`
- 60d: completed `148`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.65`, avg `0.005207`, median `0.006274`, mae `0.014717`
- 5d: sample `60`, hit `0.5833`, avg `0.00738`, median `0.006712`, mae `0.020722`
- 10d: sample `60`, hit `0.6667`, avg `0.013284`, median `0.014227`, mae `0.030471`
- 20d: sample `60`, hit `0.7667`, avg `0.024294`, median `0.028626`, mae `0.036594`
- 60d: sample `60`, hit `0.7333`, avg `0.03881`, median `0.054522`, mae `0.060903`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-3.5e-05`, median `0.003648`, mae `0.021878`
- 5d: sample `20`, hit `0.55`, avg `-0.000596`, median `0.006018`, mae `0.023582`
- 10d: sample `20`, hit `0.6`, avg `0.01282`, median `0.009015`, mae `0.027676`
- 20d: sample `20`, hit `0.65`, avg `0.019802`, median `0.029038`, mae `0.039511`
- 60d: sample `20`, hit `0.9`, avg `0.066658`, median `0.055515`, mae `0.075466`

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
- 3d: sample `8`, hit `0.625`, avg `0.003864`, median `0.004243`, mae `0.015101`
- 5d: sample `8`, hit `0.5`, avg `0.008008`, median `0.013109`, mae `0.020881`
- 10d: sample `8`, hit `0.75`, avg `0.019334`, median `0.023979`, mae `0.02779`
- 20d: sample `8`, hit `0.875`, avg `0.033152`, median `0.031196`, mae `0.035534`
- 60d: sample `8`, hit `0.875`, avg `0.061844`, median `0.073586`, mae `0.066877`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.003864`, median `0.004243`, mae `0.015101`
- 5d: sample `8`, hit `0.5`, avg `0.008008`, median `0.013109`, mae `0.020881`
- 10d: sample `8`, hit `0.75`, avg `0.019334`, median `0.023979`, mae `0.02779`
- 20d: sample `8`, hit `0.875`, avg `0.033152`, median `0.031196`, mae `0.035534`
- 60d: sample `8`, hit `0.875`, avg `0.061844`, median `0.073586`, mae `0.066877`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.005207, 'median_return': 0.006274, 'mean_absolute_return': 0.014717, 'max_adverse_excursion': -0.028651, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.00738, 'median_return': 0.006712, 'mean_absolute_return': 0.020722, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.013284, 'median_return': 0.014227, 'mean_absolute_return': 0.030471, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.024294, 'median_return': 0.028626, 'mean_absolute_return': 0.036594, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.03881, 'median_return': 0.054522, 'mean_absolute_return': 0.060903, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.139575}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003864, 'median_return': 0.004243, 'mean_absolute_return': 0.015101, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.008008, 'median_return': 0.013109, 'mean_absolute_return': 0.020881, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.019334, 'median_return': 0.023979, 'mean_absolute_return': 0.02779, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.033152, 'median_return': 0.031196, 'mean_absolute_return': 0.035534, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.061844, 'median_return': 0.073586, 'mean_absolute_return': 0.066877, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.101208}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.0039, 'median_return': 0.006274, 'mean_absolute_return': 0.016664, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.005095, 'median_return': 0.006571, 'mean_absolute_return': 0.021499, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.012483, 'median_return': 0.010559, 'mean_absolute_return': 0.029993, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.022062, 'median_return': 0.028626, 'mean_absolute_return': 0.037523, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.043986, 'median_return': 0.052632, 'mean_absolute_return': 0.064285, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.575}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 21}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.025, 'both_hit': 35, 'both_miss': 25}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.05, 'both_hit': 40, 'both_miss': 20}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.075, 'both_hit': 46, 'both_miss': 14}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.775, 'primary_minus_secondary': -0.2, 'both_hit': 44, 'both_miss': 16}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006952, 'median_return': 0.010582, 'mean_absolute_return': 0.01733, 'max_adverse_excursion': -0.028651, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.015129, 'median_return': 0.020876, 'mean_absolute_return': 0.026336, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.025791, 'median_return': 0.037056, 'mean_absolute_return': 0.037496, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.033667, 'median_return': 0.043749, 'mean_absolute_return': 0.043697, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.077201}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.059722, 'median_return': 0.066779, 'mean_absolute_return': 0.074114, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.139575}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.002878, 'median_return': 0.004243, 'mean_absolute_return': 0.016234, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.002138, 'median_return': 0.003402, 'mean_absolute_return': 0.019804, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.008961, 'median_return': 0.009031, 'mean_absolute_return': 0.027198, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.063285}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.019673, 'median_return': 0.025541, 'mean_absolute_return': 0.035199, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.041122, 'median_return': 0.049084, 'mean_absolute_return': 0.061354, 'max_adverse_excursion': -0.077484, 'max_favorable_excursion': 0.188184}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005207`, median `0.006274`, mae `0.014717`
- 5d: sample `60`, hit `0.5833`, avg `0.00738`, median `0.006712`, mae `0.020722`
- 10d: sample `60`, hit `0.6667`, avg `0.013284`, median `0.014227`, mae `0.030471`
- 20d: sample `60`, hit `0.7667`, avg `0.024294`, median `0.028626`, mae `0.036594`
- 60d: sample `60`, hit `0.7333`, avg `0.03881`, median `0.054522`, mae `0.060903`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-3.5e-05`, median `0.003648`, mae `0.021878`
- 5d: sample `20`, hit `0.55`, avg `-0.000596`, median `0.006018`, mae `0.023582`
- 10d: sample `20`, hit `0.6`, avg `0.01282`, median `0.009015`, mae `0.027676`
- 20d: sample `20`, hit `0.65`, avg `0.019802`, median `0.029038`, mae `0.039511`
- 60d: sample `20`, hit `0.9`, avg `0.066658`, median `0.055515`, mae `0.075466`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005207`, median `0.006274`, mae `0.014717`
- 5d: sample `60`, hit `0.5833`, avg `0.00738`, median `0.006712`, mae `0.020722`
- 10d: sample `60`, hit `0.6667`, avg `0.013284`, median `0.014227`, mae `0.030471`
- 20d: sample `60`, hit `0.7667`, avg `0.024294`, median `0.028626`, mae `0.036594`
- 60d: sample `60`, hit `0.7333`, avg `0.03881`, median `0.054522`, mae `0.060903`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004785`, median `0.006372`, mae `0.014137`
- 5d: sample `40`, hit `0.625`, avg `0.008414`, median `0.011074`, mae `0.020692`
- 10d: sample `40`, hit `0.7`, avg `0.012759`, median `0.014227`, mae `0.030966`
- 20d: sample `40`, hit `0.75`, avg `0.02234`, median `0.028859`, mae `0.035075`
- 60d: sample `40`, hit `0.7`, avg `0.034066`, median `0.049084`, mae `0.059051`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005207`, median `0.006274`, mae `0.014717`
- 5d: sample `60`, hit `0.5833`, avg `0.00738`, median `0.006712`, mae `0.020722`
- 10d: sample `60`, hit `0.6667`, avg `0.013284`, median `0.014227`, mae `0.030471`
- 20d: sample `60`, hit `0.7667`, avg `0.024294`, median `0.028626`, mae `0.036594`
- 60d: sample `60`, hit `0.7333`, avg `0.03881`, median `0.054522`, mae `0.060903`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004785`, median `0.006372`, mae `0.014137`
- 5d: sample `40`, hit `0.625`, avg `0.008414`, median `0.011074`, mae `0.020692`
- 10d: sample `40`, hit `0.7`, avg `0.012759`, median `0.014227`, mae `0.030966`
- 20d: sample `40`, hit `0.75`, avg `0.02234`, median `0.028859`, mae `0.035075`
- 60d: sample `40`, hit `0.7`, avg `0.034066`, median `0.049084`, mae `0.059051`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-3.5e-05`, median `0.003648`, mae `0.021878`
- 5d: sample `20`, hit `0.55`, avg `-0.000596`, median `0.006018`, mae `0.023582`
- 10d: sample `20`, hit `0.6`, avg `0.01282`, median `0.009015`, mae `0.027676`
- 20d: sample `20`, hit `0.65`, avg `0.019802`, median `0.029038`, mae `0.039511`
- 60d: sample `20`, hit `0.9`, avg `0.066658`, median `0.055515`, mae `0.075466`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004335`, median `0.004391`, mae `0.013411`
- 5d: sample `40`, hit `0.525`, avg `0.003505`, median `0.003026`, mae `0.017915`
- 10d: sample `40`, hit `0.6`, avg `0.007031`, median `0.009373`, mae `0.026959`
- 20d: sample `40`, hit `0.75`, avg `0.019608`, median `0.025541`, mae `0.033043`
- 60d: sample `40`, hit `0.7`, avg `0.028354`, median `0.034688`, mae `0.054298`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006952`, median `0.010582`, mae `0.01733`
- 5d: sample `20`, hit `0.7`, avg `0.015129`, median `0.020876`, mae `0.026336`
- 10d: sample `20`, hit `0.8`, avg `0.025791`, median `0.037056`, mae `0.037496`
- 20d: sample `20`, hit `0.8`, avg `0.033667`, median `0.043749`, mae `0.043697`
- 60d: sample `20`, hit `0.8`, avg `0.059722`, median `0.066779`, mae `0.074114`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-3.5e-05`, median `0.003648`, mae `0.021878`
- 5d: sample `20`, hit `0.55`, avg `-0.000596`, median `0.006018`, mae `0.023582`
- 10d: sample `20`, hit `0.6`, avg `0.01282`, median `0.009015`, mae `0.027676`
- 20d: sample `20`, hit `0.65`, avg `0.019802`, median `0.029038`, mae `0.039511`
- 60d: sample `20`, hit `0.9`, avg `0.066658`, median `0.055515`, mae `0.075466`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004335`, median `0.004391`, mae `0.013411`
- 5d: sample `40`, hit `0.525`, avg `0.003505`, median `0.003026`, mae `0.017915`
- 10d: sample `40`, hit `0.6`, avg `0.007031`, median `0.009373`, mae `0.026959`
- 20d: sample `40`, hit `0.75`, avg `0.019608`, median `0.025541`, mae `0.033043`
- 60d: sample `40`, hit `0.7`, avg `0.028354`, median `0.034688`, mae `0.054298`

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
- 3d: sample `80`, hit `0.6125`, avg `0.003897`, median `0.006228`, mae `0.016508`
- 5d: sample `80`, hit `0.575`, avg `0.005386`, median `0.006571`, mae `0.021437`
- 10d: sample `80`, hit `0.65`, avg `0.013168`, median `0.012215`, mae `0.029772`
- 20d: sample `80`, hit `0.7375`, avg `0.023171`, median `0.028626`, mae `0.037324`
- 60d: sample `80`, hit `0.775`, avg `0.045772`, median `0.054522`, mae `0.064544`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003897`, median `0.006228`, mae `0.016508`
- 5d: sample `80`, hit `0.575`, avg `0.005386`, median `0.006571`, mae `0.021437`
- 10d: sample `80`, hit `0.65`, avg `0.013168`, median `0.012215`, mae `0.029772`
- 20d: sample `80`, hit `0.7375`, avg `0.023171`, median `0.028626`, mae `0.037324`
- 60d: sample `80`, hit `0.775`, avg `0.045772`, median `0.054522`, mae `0.064544`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005207`, median `0.006274`, mae `0.014717`
- 5d: sample `60`, hit `0.5833`, avg `0.00738`, median `0.006712`, mae `0.020722`
- 10d: sample `60`, hit `0.6667`, avg `0.013284`, median `0.014227`, mae `0.030471`
- 20d: sample `60`, hit `0.7667`, avg `0.024294`, median `0.028626`, mae `0.036594`
- 60d: sample `60`, hit `0.7333`, avg `0.03881`, median `0.054522`, mae `0.060903`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005207`, median `0.006274`, mae `0.014717`
- 5d: sample `60`, hit `0.5833`, avg `0.00738`, median `0.006712`, mae `0.020722`
- 10d: sample `60`, hit `0.6667`, avg `0.013284`, median `0.014227`, mae `0.030471`
- 20d: sample `60`, hit `0.7667`, avg `0.024294`, median `0.028626`, mae `0.036594`
- 60d: sample `60`, hit `0.7333`, avg `0.03881`, median `0.054522`, mae `0.060903`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-3.5e-05`, median `0.003648`, mae `0.021878`
- 5d: sample `20`, hit `0.55`, avg `-0.000596`, median `0.006018`, mae `0.023582`
- 10d: sample `20`, hit `0.6`, avg `0.01282`, median `0.009015`, mae `0.027676`
- 20d: sample `20`, hit `0.65`, avg `0.019802`, median `0.029038`, mae `0.039511`
- 60d: sample `20`, hit `0.9`, avg `0.066658`, median `0.055515`, mae `0.075466`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
