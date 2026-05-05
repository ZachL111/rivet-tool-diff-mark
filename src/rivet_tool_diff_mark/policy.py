from __future__ import annotations

from dataclasses import dataclass

THRESHOLD = 177
RISK_PENALTY = 7
LATENCY_PENALTY = 4
WEIGHT_BONUS = 3


@dataclass(frozen=True)
class Signal:
    demand: int
    capacity: int
    latency: int
    risk: int
    weight: int


def score(signal: Signal) -> int:
    return (
        signal.demand * 2
        + signal.capacity
        + signal.weight * WEIGHT_BONUS
        - signal.latency * LATENCY_PENALTY
        - signal.risk * RISK_PENALTY
    )


def classify(signal: Signal) -> str:
    return "accept" if score(signal) >= THRESHOLD else "review"
