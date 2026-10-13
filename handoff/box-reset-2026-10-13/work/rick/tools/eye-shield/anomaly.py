"""Rate-based early-warning score for rising attack attempts."""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
import math, time

@dataclass
class WindowHit:
    ts: float
    count: int
    kinds: dict

class AnomalyScorer:
    """EMA of event rate; warn when current rate exceeds baseline * factor."""
    def __init__(self, window_s: float = 300.0, warn_factor: float = 3.0):
        self.window_s = window_s
        self.warn_factor = warn_factor
        self.history: deque[WindowHit] = deque(maxlen=48)  # ~4h if 5min windows
        self.baseline = 0.5  # prior
        self.last_score = 0.0

    def update(self, event_count: int, kinds: dict | None = None, ts: float | None = None) -> dict:
        ts = ts or time.time()
        self.history.append(WindowHit(ts, event_count, kinds or {}))
        # recent rate = events in last window
        recent = sum(h.count for h in self.history if ts - h.ts <= self.window_s)
        # baseline = EMA of prior windows (exclude current)
        prior = [h.count for h in list(self.history)[:-1]]
        if prior:
            avg = sum(prior) / len(prior)
            self.baseline = 0.7 * self.baseline + 0.3 * avg
        rate = recent / max(self.window_s / 60.0, 1.0)  # per minute
        base_rate = self.baseline / max(self.window_s / 60.0, 1.0)
        ratio = rate / max(base_rate, 0.05)
        # squash to 0..100
        score = 100.0 * (1.0 - math.exp(-0.4 * max(ratio - 1.0, 0.0)))
        if event_count >= 5:
            score = max(score, 40.0)
        if event_count >= 15:
            score = max(score, 70.0)
        self.last_score = score
        level = "ok"
        if score >= 70:
            level = "critical"
        elif score >= 40:
            level = "warn"
        elif score >= 20:
            level = "elevated"
        return {
            "score": round(score, 1),
            "level": level,
            "recent_events": recent,
            "baseline": round(self.baseline, 2),
            "ratio": round(ratio, 2),
            "warn": score >= 40,
        }
