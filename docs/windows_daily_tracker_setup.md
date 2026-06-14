# Windows Daily Tracker Setup

This guide schedules Alpha v1 forward-only forecast observation after the market close.

Alpha v1 is fixed:

- Signal: `bounce_probability_top_decile_v1`
- Threshold: `0.32534311`
- Status: `RESEARCH ALPHA CANDIDATE`
- Validation mode: `forward_only`

The tracker must not tune thresholds, add features, or use synthetic data to create forecast signals.

## Manual Command

From the repository root:

```powershell
.\scripts\run_forward_tracker_windows.ps1
```

The script writes:

- `outputs/forward_alpha_v1_signals.csv`
- `outputs/forward_alpha_v1_daily_checks.csv`
- `outputs/forward_alpha_v1_report.md`
- `outputs/forward_alpha_v1_tracker.log`

## Task Scheduler Setup

1. Open Windows Task Scheduler.
2. Choose **Create Task**.
3. Name it `market-predictor-alpha-v1-forward-tracker`.
4. On **Triggers**, add a daily trigger after the US market close, for example `17:30` New York time adjusted to your local timezone.
5. On **Actions**, choose **Start a program**.
6. Program/script:

```text
powershell.exe
```

7. Add arguments:

```text
-ExecutionPolicy Bypass -File "C:\Users\xuanx\Documents\Codex\2026-06-13\codex-skill-github-codex-skill-market\market-predictor\scripts\run_forward_tracker_windows.ps1"
```

8. Start in:

```text
C:\Users\xuanx\Documents\Codex\2026-06-13\codex-skill-github-codex-skill-market\market-predictor
```

9. Save the task.
10. Right-click the task and choose **Run** once to verify it works.

## Expected Behavior

- If real data succeeds, the tracker checks SPY, QQQ, IWM, and DIA against the frozen threshold.
- If a symbol triggers, the forecast signal is appended to `outputs/forward_alpha_v1_signals.csv` with `validation_period=forward_only`.
- If no symbol triggers, the daily check is still saved.
- If real data fails, the tracker records `synthetic_fallback_no_signal` and does not write a forecast signal.
- Pending forecast signals are backfilled when 3d/5d/10d/20d/60d future returns become available.

## Safety Rules

- Do not use synthetic data for Alpha v1 forecast signals.
- Do not use `down_probability` or `crash_probability` as order triggers or execution recommendations.
- Do not change the Alpha v1 threshold.
- Do not turn forecast validation into an order-simulation workflow. The tracker is only for scenario validation and prediction accuracy tracking.
