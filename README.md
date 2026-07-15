# Deterministic Replay Cpp Engine

Deterministic event replay and first-divergence detection for trading-system debugging.

This repository is part of the ShawSignalDev advanced portfolio layer for low-latency trading systems,
market microstructure research, and hardware-aware AI acceleration. It keeps the implementation
deliberately small, deterministic, and testable so reviewers can inspect the core model quickly.

## What it demonstrates

- A focused model for replay, debugging, determinism
- Deterministic examples suitable for CI and recruiter review
- Clear public boundaries: no auth tokens, no live broker integration, no unsupported live-execution claims
- Research-oriented documentation that explains where the prototype fits in a larger system

## Run

```powershell
python -m pytest -q
```

## Portfolio context

The goal is to show engineering judgment across quant research, cyber-physical systems,
low-latency infrastructure, and hardware/software co-design. This is a public prototype,
not a live trading system.
