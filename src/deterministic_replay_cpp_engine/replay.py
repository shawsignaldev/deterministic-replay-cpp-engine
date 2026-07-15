from dataclasses import dataclass

@dataclass(frozen=True)
class Event:
    sequence: int
    delta: int

def replay(events: list[Event]) -> list[int]:
    state = 0
    trace: list[int] = []
    for event in sorted(events, key=lambda item: item.sequence):
        state += event.delta
        trace.append(state)
    return trace

def first_divergence(expected: list[int], actual: list[int]) -> int | None:
    for index, (left, right) in enumerate(zip(expected, actual)):
        if left != right:
            return index
    return None if len(expected) == len(actual) else min(len(expected), len(actual))
