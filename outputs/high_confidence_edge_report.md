# High Confidence Edge Report

Generated at: `2026-10-24T01:33:14.483939+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `132`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `132`, gate `stronger_evidence`
- 5d: completed `132`, gate `stronger_evidence`
- 10d: completed `132`, gate `stronger_evidence`
- 20d: completed `132`, gate `stronger_evidence`
- 60d: completed `132`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.002023`, median `0.003072`, mae `0.01431`
- 5d: sample `40`, hit `0.625`, avg `0.002546`, median `0.006571`, mae `0.017292`
- 10d: sample `40`, hit `0.65`, avg `0.006865`, median `0.009031`, mae `0.021267`
- 20d: sample `40`, hit `0.675`, avg `0.012834`, median `0.014692`, mae `0.027787`
- 60d: sample `40`, hit `0.7`, avg `0.022456`, median `0.01956`, mae `0.049725`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `0.000175`, median `-0.001811`, mae `0.017725`
- 5d: sample `40`, hit `0.475`, avg `-0.000128`, median `-0.003328`, mae `0.018065`
- 10d: sample `40`, hit `0.6`, avg `0.009283`, median `0.0076`, mae `0.023358`
- 20d: sample `40`, hit `0.775`, avg `0.018803`, median `0.027343`, mae `0.032362`
- 60d: sample `40`, hit `0.875`, avg `0.054825`, median `0.068046`, mae `0.068589`

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
- 3d: sample `8`, hit `0.75`, avg `0.006022`, median `0.006372`, mae `0.009491`
- 5d: sample `8`, hit `0.625`, avg `0.002367`, median `0.003402`, mae `0.015364`
- 10d: sample `8`, hit `0.625`, avg `0.007339`, median `0.009373`, mae `0.026061`
- 20d: sample `8`, hit `0.875`, avg `0.027829`, median `0.028859`, mae `0.028837`
- 60d: sample `8`, hit `0.5`, avg `0.004239`, median `0.000768`, mae `0.043246`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.001306`, median `0.001558`, mae `0.012732`
- 5d: sample `8`, hit `0.25`, avg `-0.00114`, median `-0.006798`, mae `0.014265`
- 10d: sample `8`, hit `0.625`, avg `0.009246`, median `0.0076`, mae `0.018137`
- 20d: sample `8`, hit `0.875`, avg `0.029442`, median `0.031196`, mae `0.031823`
- 60d: sample `8`, hit `1.0`, avg `0.073875`, median `0.074055`, mae `0.073875`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002023, 'median_return': 0.003072, 'mean_absolute_return': 0.01431, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.002546, 'median_return': 0.006571, 'mean_absolute_return': 0.017292, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.044543}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.006865, 'median_return': 0.009031, 'mean_absolute_return': 0.021267, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.059334}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.012834, 'median_return': 0.014692, 'mean_absolute_return': 0.027787, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.022456, 'median_return': 0.01956, 'mean_absolute_return': 0.049725, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.152478}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001306, 'median_return': 0.001558, 'mean_absolute_return': 0.012732, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.02763}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00114, 'median_return': -0.006798, 'mean_absolute_return': 0.014265, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009246, 'median_return': 0.0076, 'mean_absolute_return': 0.018137, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.029442, 'median_return': 0.031196, 'mean_absolute_return': 0.031823, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.073875, 'median_return': 0.074055, 'mean_absolute_return': 0.073875, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.103268}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.001076, 'median_return': 0.000732, 'mean_absolute_return': 0.016382, 'max_adverse_excursion': -0.043793, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.00147, 'median_return': 0.003714, 'mean_absolute_return': 0.018058, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.007944, 'median_return': 0.009031, 'mean_absolute_return': 0.022777, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.014305, 'median_return': 0.016175, 'mean_absolute_return': 0.02988, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.034725, 'median_return': 0.041644, 'mean_absolute_return': 0.057522, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.166476}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.05, 'both_hit': 22, 'both_miss': 18}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 25, 'both_miss': 15}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.05, 'both_hit': 26, 'both_miss': 14}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.075, 'both_hit': 27, 'both_miss': 13}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.025, 'both_hit': 28, 'both_miss': 12}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.00197, 'median_return': 0.000732, 'mean_absolute_return': 0.017674, 'max_adverse_excursion': -0.042672, 'max_favorable_excursion': 0.041157}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002574, 'median_return': 0.006832, 'mean_absolute_return': 0.018761, 'max_adverse_excursion': -0.054326, 'max_favorable_excursion': 0.044543}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.011701, 'median_return': 0.011431, 'mean_absolute_return': 0.02018, 'max_adverse_excursion': -0.049389, 'max_favorable_excursion': 0.056786}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.018678, 'median_return': 0.024811, 'mean_absolute_return': 0.030293, 'max_adverse_excursion': -0.047796, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.04705, 'median_return': 0.060303, 'mean_absolute_return': 0.061509, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.152478}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.000228, 'median_return': 0.001534, 'mean_absolute_return': 0.01436, 'max_adverse_excursion': -0.043793, 'max_favorable_excursion': 0.038776}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.000155, 'median_return': 0.003026, 'mean_absolute_return': 0.016596, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.050537}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.004447, 'median_return': 0.007161, 'mean_absolute_return': 0.024445, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.06329}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.012959, 'median_return': 0.013021, 'mean_absolute_return': 0.029856, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.030231, 'median_return': 0.033062, 'mean_absolute_return': 0.056805, 'max_adverse_excursion': -0.099346, 'max_favorable_excursion': 0.166476}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.002221`, median `0.001558`, mae `0.015575`
- 5d: sample `60`, hit `0.55`, avg `0.001434`, median `0.003402`, mae `0.017202`
- 10d: sample `60`, hit `0.6167`, avg `0.007432`, median `0.007467`, mae `0.020451`
- 20d: sample `60`, hit `0.7333`, avg `0.015849`, median `0.016838`, mae `0.028649`
- 60d: sample `60`, hit `0.7667`, avg `0.035644`, median `0.052632`, mae `0.057379`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002268`, median `-0.007802`, mae `0.017345`
- 5d: sample `20`, hit `0.55`, avg `0.000535`, median `0.00338`, mae `0.019107`
- 10d: sample `20`, hit `0.65`, avg `0.010001`, median `0.015652`, mae `0.027897`
- 20d: sample `20`, hit `0.7`, avg `0.015729`, median `0.023931`, mae `0.034352`
- 60d: sample `20`, hit `0.85`, avg `0.047629`, median `0.04945`, mae `0.064492`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.002221`, median `0.001558`, mae `0.015575`
- 5d: sample `60`, hit `0.55`, avg `0.001434`, median `0.003402`, mae `0.017202`
- 10d: sample `60`, hit `0.6167`, avg `0.007432`, median `0.007467`, mae `0.020451`
- 20d: sample `60`, hit `0.7333`, avg `0.015849`, median `0.016838`, mae `0.028649`
- 60d: sample `60`, hit `0.7667`, avg `0.035644`, median `0.052632`, mae `0.057379`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.002671`, median `0.003072`, mae `0.014739`
- 5d: sample `40`, hit `0.475`, avg `-0.000818`, median `-0.003328`, mae `0.015553`
- 10d: sample `40`, hit `0.55`, avg `0.003729`, median `0.006053`, mae `0.019905`
- 20d: sample `40`, hit `0.775`, avg `0.016034`, median `0.018139`, mae `0.027866`
- 60d: sample `40`, hit `0.775`, avg `0.037426`, median `0.057501`, mae `0.060902`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.002221`, median `0.001558`, mae `0.015575`
- 5d: sample `60`, hit `0.55`, avg `0.001434`, median `0.003402`, mae `0.017202`
- 10d: sample `60`, hit `0.6167`, avg `0.007432`, median `0.007467`, mae `0.020451`
- 20d: sample `60`, hit `0.7333`, avg `0.015849`, median `0.016838`, mae `0.028649`
- 60d: sample `60`, hit `0.7667`, avg `0.035644`, median `0.052632`, mae `0.057379`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.002671`, median `0.003072`, mae `0.014739`
- 5d: sample `40`, hit `0.475`, avg `-0.000818`, median `-0.003328`, mae `0.015553`
- 10d: sample `40`, hit `0.55`, avg `0.003729`, median `0.006053`, mae `0.019905`
- 20d: sample `40`, hit `0.775`, avg `0.016034`, median `0.018139`, mae `0.027866`
- 60d: sample `40`, hit `0.775`, avg `0.037426`, median `0.057501`, mae `0.060902`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002268`, median `-0.007802`, mae `0.017345`
- 5d: sample `20`, hit `0.55`, avg `0.000535`, median `0.00338`, mae `0.019107`
- 10d: sample `20`, hit `0.65`, avg `0.010001`, median `0.015652`, mae `0.027897`
- 20d: sample `20`, hit `0.7`, avg `0.015729`, median `0.023931`, mae `0.034352`
- 60d: sample `20`, hit `0.85`, avg `0.047629`, median `0.04945`, mae `0.064492`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.002221`, median `0.001558`, mae `0.015575`
- 5d: sample `60`, hit `0.55`, avg `0.001434`, median `0.003402`, mae `0.017202`
- 10d: sample `60`, hit `0.6167`, avg `0.007432`, median `0.007467`, mae `0.020451`
- 20d: sample `60`, hit `0.7333`, avg `0.015849`, median `0.016838`, mae `0.028649`
- 60d: sample `60`, hit `0.7667`, avg `0.035644`, median `0.052632`, mae `0.057379`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.002023`, median `0.003072`, mae `0.01431`
- 5d: sample `40`, hit `0.625`, avg `0.002546`, median `0.006571`, mae `0.017292`
- 10d: sample `40`, hit `0.65`, avg `0.006865`, median `0.009031`, mae `0.021267`
- 20d: sample `40`, hit `0.675`, avg `0.012834`, median `0.014692`, mae `0.027787`
- 60d: sample `40`, hit `0.7`, avg `0.022456`, median `0.01956`, mae `0.049725`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `0.001099`, median `0.000732`, mae `0.016017`
- 5d: sample `80`, hit `0.55`, avg `0.001209`, median `0.00338`, mae `0.017679`
- 10d: sample `80`, hit `0.625`, avg `0.008074`, median `0.0076`, mae `0.022313`
- 20d: sample `80`, hit `0.725`, avg `0.015819`, median `0.016838`, mae `0.030074`
- 60d: sample `80`, hit `0.7875`, avg `0.03864`, median `0.04945`, mae `0.059157`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.002023`, median `0.003072`, mae `0.01431`
- 5d: sample `40`, hit `0.625`, avg `0.002546`, median `0.006571`, mae `0.017292`
- 10d: sample `40`, hit `0.65`, avg `0.006865`, median `0.009031`, mae `0.021267`
- 20d: sample `40`, hit `0.675`, avg `0.012834`, median `0.014692`, mae `0.027787`
- 60d: sample `40`, hit `0.7`, avg `0.022456`, median `0.01956`, mae `0.049725`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.002221`, median `0.001558`, mae `0.015575`
- 5d: sample `60`, hit `0.55`, avg `0.001434`, median `0.003402`, mae `0.017202`
- 10d: sample `60`, hit `0.6167`, avg `0.007432`, median `0.007467`, mae `0.020451`
- 20d: sample `60`, hit `0.7333`, avg `0.015849`, median `0.016838`, mae `0.028649`
- 60d: sample `60`, hit `0.7667`, avg `0.035644`, median `0.052632`, mae `0.057379`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.000473`, median `-0.002446`, mae `0.017295`
- 5d: sample `40`, hit `0.625`, avg `0.003237`, median `0.007116`, mae `0.019804`
- 10d: sample `40`, hit `0.7`, avg `0.012419`, median `0.016016`, mae `0.02472`
- 20d: sample `40`, hit `0.675`, avg `0.015604`, median `0.016584`, mae `0.032283`
- 60d: sample `40`, hit `0.8`, avg `0.039855`, median `0.033062`, mae `0.057412`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
