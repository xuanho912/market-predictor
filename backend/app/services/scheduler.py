from __future__ import annotations

import os
from typing import Callable


try:
    from apscheduler.schedulers.background import BackgroundScheduler
except ImportError:  # pragma: no cover - optional until dependencies are installed
    BackgroundScheduler = None  # type: ignore[assignment]


_scheduler = None


def start_scheduler(refresh_job: Callable[[], None], forward_tracker_job: Callable[[], object] | None = None) -> str:
    global _scheduler
    if BackgroundScheduler is None:
        return "apscheduler_unavailable"
    if _scheduler is not None and _scheduler.running:
        return "already_running"
    _scheduler = BackgroundScheduler(timezone="UTC")
    _scheduler.add_job(refresh_job, "interval", hours=6, id="refresh-market-predictions", replace_existing=True)
    if forward_tracker_job is not None:
        tracker_hour = int(os.getenv("FORWARD_TRACKER_UTC_HOUR", "22"))
        tracker_minute = int(os.getenv("FORWARD_TRACKER_UTC_MINUTE", "30"))
        _scheduler.add_job(
            forward_tracker_job,
            "cron",
            day_of_week="mon-fri",
            hour=tracker_hour,
            minute=tracker_minute,
            id="alpha-v1-forward-observation",
            replace_existing=True,
        )
    _scheduler.start()
    return "started"
