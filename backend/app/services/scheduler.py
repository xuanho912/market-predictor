from __future__ import annotations

from typing import Callable


try:
    from apscheduler.schedulers.background import BackgroundScheduler
except ImportError:  # pragma: no cover - optional until dependencies are installed
    BackgroundScheduler = None  # type: ignore[assignment]


_scheduler = None


def start_scheduler(refresh_job: Callable[[], None]) -> str:
    global _scheduler
    if BackgroundScheduler is None:
        return "apscheduler_unavailable"
    if _scheduler is not None and _scheduler.running:
        return "already_running"
    _scheduler = BackgroundScheduler(timezone="UTC")
    _scheduler.add_job(refresh_job, "interval", hours=6, id="refresh-market-predictions", replace_existing=True)
    _scheduler.start()
    return "started"
