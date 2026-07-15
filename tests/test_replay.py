from deterministic_replay_cpp_engine.replay import Event, first_divergence, replay

def test_replay_returns_state_trace() -> None:
    assert replay([Event(1, 5), Event(2, -2), Event(3, 4)]) == [5, 3, 7]

def test_first_divergence_returns_first_mismatch_index() -> None:
    assert first_divergence([1, 2, 3], [1, 4, 3]) == 1
    assert first_divergence([1, 2], [1, 2]) is None
