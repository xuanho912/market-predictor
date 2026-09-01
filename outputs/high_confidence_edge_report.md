# High Confidence Edge Report

Generated at: `2026-09-01T06:19:07.965193+00:00`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.001546`, median `0.000766`, mae `0.016267`
- 5d: sample `80`, hit `0.5`, avg `-0.002145`, median `0.000208`, mae `0.019127`
- 10d: sample `80`, hit `0.4125`, avg `0.000536`, median `-0.007117`, mae `0.025553`
- 20d: sample `80`, hit `0.7`, avg `0.011436`, median `0.018868`, mae `0.036732`
- 60d: sample `80`, hit `0.7125`, avg `0.036535`, median `0.053843`, mae `0.070425`

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
- 3d: sample `8`, hit `0.625`, avg `-0.001645`, median `0.00234`, mae `0.010468`
- 5d: sample `8`, hit `0.375`, avg `-0.006459`, median `-0.012956`, mae `0.016199`
- 10d: sample `8`, hit `0.75`, avg `0.012529`, median `0.020918`, mae `0.02209`
- 20d: sample `8`, hit `1.0`, avg `0.027693`, median `0.031196`, mae `0.027693`
- 60d: sample `8`, hit `0.875`, avg `0.065639`, median `0.092646`, mae `0.070671`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.000513`, median `0.000766`, mae `0.00639`
- 5d: sample `8`, hit `0.5`, avg `-0.003726`, median `0.000688`, mae `0.008699`
- 10d: sample `8`, hit `0.375`, avg `-0.00377`, median `-0.007117`, mae `0.019328`
- 20d: sample `8`, hit `0.625`, avg `0.014435`, median `0.02086`, mae `0.021208`
- 60d: sample `8`, hit `0.875`, avg `0.056012`, median `0.06608`, mae `0.061215`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.001546, 'median_return': 0.000766, 'mean_absolute_return': 0.016267, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.002145, 'median_return': 0.000208, 'mean_absolute_return': 0.019127, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': 0.000536, 'median_return': -0.007117, 'mean_absolute_return': 0.025553, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.011436, 'median_return': 0.018868, 'mean_absolute_return': 0.036732, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.036535, 'median_return': 0.053843, 'mean_absolute_return': 0.070425, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000513, 'median_return': 0.000766, 'mean_absolute_return': 0.00639, 'max_adverse_excursion': -0.016886, 'max_favorable_excursion': 0.010897}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003726, 'median_return': 0.000688, 'mean_absolute_return': 0.008699, 'max_adverse_excursion': -0.018136, 'max_favorable_excursion': 0.01145}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.00377, 'median_return': -0.007117, 'mean_absolute_return': 0.019328, 'max_adverse_excursion': -0.03706, 'max_favorable_excursion': 0.031945}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.014435, 'median_return': 0.02086, 'mean_absolute_return': 0.021208, 'max_adverse_excursion': -0.016058, 'max_favorable_excursion': 0.039296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.056012, 'median_return': 0.06608, 'mean_absolute_return': 0.061215, 'max_adverse_excursion': -0.020815, 'max_favorable_excursion': 0.088884}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.00166, 'median_return': 0.001558, 'mean_absolute_return': 0.017364, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.00197, 'median_return': 0.000208, 'mean_absolute_return': 0.020285, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': 0.001015, 'median_return': -0.00676, 'mean_absolute_return': 0.026245, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.011102, 'median_return': 0.018139, 'mean_absolute_return': 0.038457, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.034371, 'median_return': 0.046132, 'mean_absolute_return': 0.071449, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.6}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.001402, 'median_return': 0.002329, 'mean_absolute_return': 0.019188, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.001124, 'median_return': 0.000415, 'mean_absolute_return': 0.022192, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 0.003308, 'median_return': -0.001932, 'mean_absolute_return': 0.027411, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.018374, 'median_return': 0.026531, 'mean_absolute_return': 0.037321, 'max_adverse_excursion': -0.093242, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.043088, 'median_return': 0.058598, 'mean_absolute_return': 0.073777, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001977, 'median_return': -0.001428, 'mean_absolute_return': 0.007504, 'max_adverse_excursion': -0.016886, 'max_favorable_excursion': 0.015419}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00521, 'median_return': -0.00244, 'mean_absolute_return': 0.009932, 'max_adverse_excursion': -0.027002, 'max_favorable_excursion': 0.011571}, '10d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.007779, 'median_return': -0.01051, 'mean_absolute_return': 0.01998, 'max_adverse_excursion': -0.037654, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.00938, 'median_return': 0.007004, 'mean_absolute_return': 0.034963, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.042268}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.016874, 'median_return': 0.032982, 'mean_absolute_return': 0.060369, 'max_adverse_excursion': -0.090808, 'max_favorable_excursion': 0.098228}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001977`, median `-0.001428`, mae `0.007504`
- 5d: sample `20`, hit `0.45`, avg `-0.00521`, median `-0.00244`, mae `0.009932`
- 10d: sample `20`, hit `0.3`, avg `-0.007779`, median `-0.01051`, mae `0.01998`
- 20d: sample `20`, hit `0.55`, avg `-0.00938`, median `0.007004`, mae `0.034963`
- 60d: sample `20`, hit `0.6`, avg `0.016874`, median `0.032982`, mae `0.060369`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `1.1e-05`, median `0.002329`, mae `0.019162`
- 5d: sample `40`, hit `0.475`, avg `-0.001736`, median `-0.004438`, mae `0.023665`
- 10d: sample `40`, hit `0.45`, avg `0.005894`, median `-0.001222`, mae `0.02843`
- 20d: sample `40`, hit `0.775`, avg `0.021485`, median `0.029166`, mae `0.038694`
- 60d: sample `40`, hit `0.85`, avg `0.065879`, median `0.079427`, mae `0.080654`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001977`, median `-0.001428`, mae `0.007504`
- 5d: sample `20`, hit `0.45`, avg `-0.00521`, median `-0.00244`, mae `0.009932`
- 10d: sample `20`, hit `0.3`, avg `-0.007779`, median `-0.01051`, mae `0.01998`
- 20d: sample `20`, hit `0.55`, avg `-0.00938`, median `0.007004`, mae `0.034963`
- 60d: sample `20`, hit `0.6`, avg `0.016874`, median `0.032982`, mae `0.060369`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002852`, median `-0.001658`, mae `0.015174`
- 5d: sample `20`, hit `0.45`, avg `-0.005709`, median `-0.004438`, mae `0.017498`
- 10d: sample `20`, hit `0.4`, avg `0.002758`, median `-0.001222`, mae `0.019557`
- 20d: sample `20`, hit `0.85`, avg `0.024854`, median `0.031658`, mae `0.03844`
- 60d: sample `20`, hit `0.8`, avg `0.059262`, median `0.085257`, mae `0.082428`

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
- 3d: sample `20`, hit `0.45`, avg `-0.001977`, median `-0.001428`, mae `0.007504`
- 5d: sample `20`, hit `0.45`, avg `-0.00521`, median `-0.00244`, mae `0.009932`
- 10d: sample `20`, hit `0.3`, avg `-0.007779`, median `-0.01051`, mae `0.01998`
- 20d: sample `20`, hit `0.55`, avg `-0.00938`, median `0.007004`, mae `0.034963`
- 60d: sample `20`, hit `0.6`, avg `0.016874`, median `0.032982`, mae `0.060369`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.00354`, median `0.001558`, mae `0.017207`
- 5d: sample `40`, hit `0.525`, avg `-0.002804`, median `0.000415`, mae `0.018371`
- 10d: sample `40`, hit `0.425`, avg `0.000447`, median `-0.001932`, mae `0.022465`
- 20d: sample `40`, hit `0.775`, avg `0.018503`, median `0.031073`, mae `0.036508`
- 60d: sample `40`, hit `0.675`, avg `0.028384`, median `0.058598`, mae `0.071226`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002874`, median `0.010018`, mae `0.023149`
- 5d: sample `20`, hit `0.5`, avg `0.002237`, median `0.007909`, mae `0.029833`
- 10d: sample `20`, hit `0.5`, avg `0.00903`, median `0.012111`, mae `0.037303`
- 20d: sample `20`, hit `0.7`, avg `0.018116`, median `0.014522`, mae `0.038947`
- 60d: sample `20`, hit `0.9`, avg `0.072497`, median `0.064104`, mae `0.07888`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001977`, median `-0.001428`, mae `0.007504`
- 5d: sample `20`, hit `0.45`, avg `-0.00521`, median `-0.00244`, mae `0.009932`
- 10d: sample `20`, hit `0.3`, avg `-0.007779`, median `-0.01051`, mae `0.01998`
- 20d: sample `20`, hit `0.55`, avg `-0.00938`, median `0.007004`, mae `0.034963`
- 60d: sample `20`, hit `0.6`, avg `0.016874`, median `0.032982`, mae `0.060369`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `1.1e-05`, median `0.002329`, mae `0.019162`
- 5d: sample `40`, hit `0.475`, avg `-0.001736`, median `-0.004438`, mae `0.023665`
- 10d: sample `40`, hit `0.45`, avg `0.005894`, median `-0.001222`, mae `0.02843`
- 20d: sample `40`, hit `0.775`, avg `0.021485`, median `0.029166`, mae `0.038694`
- 60d: sample `40`, hit `0.85`, avg `0.065879`, median `0.079427`, mae `0.080654`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002852`, median `-0.001658`, mae `0.015174`
- 5d: sample `20`, hit `0.45`, avg `-0.005709`, median `-0.004438`, mae `0.017498`
- 10d: sample `20`, hit `0.4`, avg `0.002758`, median `-0.001222`, mae `0.019557`
- 20d: sample `20`, hit `0.85`, avg `0.024854`, median `0.031658`, mae `0.03844`
- 60d: sample `20`, hit `0.8`, avg `0.059262`, median `0.085257`, mae `0.082428`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `-0.001546`, median `0.000766`, mae `0.016267`
- 5d: sample `80`, hit `0.5`, avg `-0.002145`, median `0.000208`, mae `0.019127`
- 10d: sample `80`, hit `0.4125`, avg `0.000536`, median `-0.007117`, mae `0.025553`
- 20d: sample `80`, hit `0.7`, avg `0.011436`, median `0.018868`, mae `0.036732`
- 60d: sample `80`, hit `0.7125`, avg `0.036535`, median `0.053843`, mae `0.070425`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.003019`, median `-0.001428`, mae `0.013973`
- 5d: sample `60`, hit `0.5`, avg `-0.003606`, median `0.000208`, mae `0.015558`
- 10d: sample `60`, hit `0.3833`, avg `-0.002295`, median `-0.007117`, mae `0.021636`
- 20d: sample `60`, hit `0.7`, avg `0.009209`, median `0.020226`, mae `0.035993`
- 60d: sample `60`, hit `0.65`, avg `0.024548`, median `0.046132`, mae `0.067607`

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
